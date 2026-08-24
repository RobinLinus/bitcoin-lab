# Replay Protection via Reserved nLockTime Values / replay-protection.md

Source: https://gist.github.com/RobinLinus/c9bde57d6e7eda9e447909fae35ec0b1#file-replay-protection-md

Retrieved: 2026-08-24T21:53:25Z

Extraction note: Current public gist file at revision 4c803dd8892811acafd3ccf408dbf8a95aa0b21d.

---

````markdown
# Replay Protection via Reserved `nLockTime` Values

A Bitcoin-derived hard fork can use a reserved `nLockTime` value as a replay-protection marker.

For example, a fork can define:

```cpp
nLockTime == LOCKTIME_THRESHOLD - 1
```

as immediately final, while Bitcoin continues to interpret the same value as block height `499,999,999`. With a non-final `nSequence`, the transaction is therefore valid on the fork but non-final on Bitcoin.

Because `nLockTime` is part of the signed transaction data, an attacker cannot remove or change the marker without invalidating the signatures.

The core consensus change can be as small as:

```diff
- if (tx.nLockTime == 0)
+ if (tx.nLockTime == 0 || tx.nLockTime == LOCKTIME_THRESHOLD - 1)
    return true;
```

## Advantages

* **Very small code change.** The core finality rule can be implemented in a single line.
* **No dedicated splitting tool is required.** Users can use an existing wallet setup as long as it supports setting `nLockTime`, which many Bitcoin wallets do.
* **Works with hardware wallets and multisig.** Signers do not need a fork-specific sighash algorithm or transaction format.
* **No special transaction serialization.** The transaction remains an ordinary Bitcoin-format transaction.
* **Supports multiple forks.** Different hard forks can reserve different values, for example `LOCKTIME_THRESHOLD - 1`, `LOCKTIME_THRESHOLD - 2`, `LOCKTIME_THRESHOLD - 3`, and so on.

A production implementation should also ensure that the reserved value cannot be used to satisfy `OP_CHECKLOCKTIMEVERIFY`, since the value no longer represents a real block-height lock on that fork.

This mechanism has been implemented in [eCash](https://github.com/ecash-com/bitcoin/commit/d2dec2fe9bde6787686b9673c00a643d8196c09e)

Alternatively, users can use [chain-unique dust inputs](https://gist.github.com/RobinLinus/48d08307e960e4461b3e4b4feabf29e9) to build splitting UTXOs.
````
