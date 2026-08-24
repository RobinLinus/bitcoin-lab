# Rust/libbitcoinkernel Script interpreter

The runtime Script endpoint is backed exclusively by a Rust binary that calls Bitcoin Core's libbitcoinkernel verification engine. There is no Python interpreter fallback.

## Pinned source

- Repository: <https://github.com/sedited/rust-bitcoinkernel>
- Pull request: <https://github.com/sedited/rust-bitcoinkernel/pull/201>
- Immutable revision: `691a90cc0c20761cc9b35a783e0e84c77245d555`
- Cargo feature: `script-trace`, which builds the vendored Bitcoin Core kernel with `ENABLE_SCRIPT_TRACE=ON`

`kernel-interpreter/Cargo.toml` pins the Git revision, and its checked-in `Cargo.lock` pins the remaining Rust dependency graph. The Docker build uses `cargo build --locked` and runs the compiled binary's self-test in both the builder and final image.

The Rust wrapper and the vendored Bitcoin Core source are MIT-licensed. Their license notices and the lockfile must remain with redistributed source/build materials.

## Evaluation model

libbitcoinkernel verifies a transaction input against a previous output's script; it does not expose a standalone `eval(ASM)` API. The lab therefore:

1. compiles the endpoint's unlocking and locking ASM to Bitcoin Script bytecode;
2. places the unlocking bytecode in input zero of a deterministic synthetic legacy transaction;
3. uses the locking bytecode as the spent output's scriptPubKey;
4. calls `bitcoinkernel::verify` with `VERIFY_ALL_PRE_TAPROOT`; and
5. records the PR's per-opcode trace callback frames.

The result uses Bitcoin Core's actual Script interpreter and consensus verification flags. The adapter's synthetic transaction means transaction-dependent opcodes observe its fixed version, sequence, amount, output, and locktime—not a caller-supplied real transaction. Taproot/witness spends and arbitrary transaction context require a future request schema, not a different interpreter.

## ASM compiler

The compiler accepts whitespace-delimited integer literals, `0x` byte strings, `str:` UTF-8 values, and the opcodes listed in `kernel-interpreter/src/main.rs`. This syntax layer only emits bytecode; it never evaluates Script.

Every response must include:

```json
{
  "backend": "rust-bitcoinkernel",
  "backend_revision": "691a90cc0c20761cc9b35a783e0e84c77245d555",
  "consensus_engine": "Bitcoin Core libbitcoinkernel",
  "consensus_compatible": true,
  "verification_flags": "VERIFY_ALL_PRE_TAPROOT",
  "synthetic_transaction": true
}
```

The Python HTTP layer rejects a missing binary, invalid response, backend-name mismatch, or revision mismatch. It does not fall back to the removed educational interpreter.
