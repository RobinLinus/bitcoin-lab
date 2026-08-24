# Third-party notices

The `bitcoin-script-kernel` binary statically incorporates code from:

- `sedited/rust-bitcoinkernel`, pinned to `691a90cc0c20761cc9b35a783e0e84c77245d555`, MIT license. See `licenses/rust-bitcoinkernel-LICENSE`.
- Bitcoin Core vendored by that revision, MIT license. See `licenses/bitcoin-core-COPYING`.
- OpenCode `opencode-ai` 1.18.22, installed from the official npm package. Its package files and included license are retained under `/usr/local/lib/node_modules/opencode-ai` in the image.

The Cargo dependency versions and checksums are recorded in `kernel-interpreter/Cargo.lock`.
