FROM rust:1.88.0-bookworm AS kernel-builder

RUN apt-get update \
    && apt-get install -y --no-install-recommends cmake git libboost-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build/kernel-interpreter
COPY kernel-interpreter/Cargo.toml kernel-interpreter/Cargo.lock ./
COPY kernel-interpreter/src ./src

RUN cargo build --release --locked \
    && ./target/release/bitcoin-script-kernel --self-test

FROM node:22-bookworm-slim@sha256:d649c27dae7ba0137b3cef5dd75baa422c08dc3d9e3fc0c23dfb172dc3cc6436 AS opencode-builder

ARG OPENCODE_VERSION=1.18.22
RUN npm install -g "opencode-ai@${OPENCODE_VERSION}" --omit=dev \
    && test "$(opencode --version)" = "${OPENCODE_VERSION}"

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LAB_LIBRARY_PATH=/app/library \
    LAB_INDEX_PATH=/data/library.db \
    LAB_SCRIPT_BINARY=/usr/local/bin/bitcoin-script-kernel

WORKDIR /app

RUN useradd --create-home --uid 10001 lab \
    && mkdir -p /data /home/lab/.local/share/opencode /home/lab/.cache/opencode /app/docs \
    && chown -R lab:lab /data /home/lab/.local /home/lab/.cache /app/docs

COPY --chown=lab:lab lab/ /app/lab/
COPY --chown=lab:lab library/ /app/library/
COPY --chown=lab:lab opencode.json /app/opencode.json
COPY --chown=lab:lab .opencode/ /app/.opencode/
COPY --chown=lab:lab docs/ /app/docs/
COPY --from=kernel-builder /build/kernel-interpreter/target/release/bitcoin-script-kernel /usr/local/bin/bitcoin-script-kernel
COPY --from=opencode-builder /usr/local/lib/node_modules/opencode-ai /usr/local/lib/node_modules/opencode-ai
COPY --from=opencode-builder /usr/local/bin/opencode /usr/local/bin/opencode
COPY THIRD_PARTY_NOTICES.md /usr/share/doc/bitcoin-research-lab/THIRD_PARTY_NOTICES.md
COPY licenses/ /usr/share/doc/bitcoin-research-lab/licenses/

RUN /usr/local/bin/bitcoin-script-kernel --self-test \
    && test "$(opencode --version)" = "1.18.22"

USER lab
EXPOSE 8080

HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=5 \
  CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health', timeout=2).read()"]

CMD ["python", "-m", "lab.cli", "serve", "--host", "0.0.0.0", "--port", "8080"]
