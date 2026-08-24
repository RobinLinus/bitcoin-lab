# Subchains: an embedded blockchain whose blocks are published inside Bitcoin blocks / thikcs-subchains.md

Source: https://gist.github.com/RobinLinus/3c9c91f701a420c13f90b1c70616e77a#file-thikcs-subchains-md

Retrieved: 2026-08-24T21:53:25Z

Extraction note: Current public gist file at revision 94dd8f6b11a335201f08cb9bbb2a67b9a0592f3e.

---

````markdown
# Subchains with THIKCS

## Summary

A **subchain** is an embedded blockchain whose blocks are published inside Bitcoin blocks. It is defined by a sequence of Bitcoin **publish transactions**. Bitcoin consensus enforces the ordering and cadence of publication; subchain clients enforce whatever meta-consensus rules they want over the published data.

This construction assumes the THIKCS upgrade: `OP_TEMPLATEHASH`, `OP_INTERNALKEY`, and `OP_CHECKSIGFROMSTACK`, as proposed in BIP-448. The important property is that `OP_TEMPLATEHASH` commits to the spending transaction template, but not to the prevouts, input amounts, input scriptPubKeys, or other inputs' annexes.

The construction uses two Bitcoin transactions per applied subblock:

- a **commit transaction** `K_i`, which consumes the previous anchor output and creates a payload-specific commit output; and
- a **publish transaction** `P_i`, which consumes the previous next output, consumes the commit output, publishes the payload in an annex, and creates the next carrier state.

The subchain chaintip after subblock `i` is `txid(P_i)`. For valid data blocks, this `txid` commits transitively to the entire subchain history, including the data published in the annexes.

## Basic structure

A subchain is identified by a genesis carrier state:

```text
(O_0, A_0)
```

where:

- `O_i` is the covenant-controlled **next output**, and
- `A_i` is a minimal-value **anchor output** used to sequence the next commit transaction.

For each subblock `i`:

```text
K_i:
  spends A_i
  creates C_i

P_i:
  spends O_i
  spends C_i
  publishes subblock_payload_i in vin[1]'s annex
  creates O_{i+1}
  creates A_{i+1}
```

Diagrammatically:

```text
       K_i spends A_i and creates C_i
        ┌───────────────────────────┐
        ▼                           │
P_{i-1}: O_i, A_i ────────────────> P_i: O_{i+1}, A_{i+1}
                  P_i spends O_i and C_i
```

There is at most one valid successor for each `O_i`, because all candidate publish transactions conflict on the same covenant-controlled input. There is also at most one anchored commit transaction for each `A_i`, because all honest commit transactions for the next slot spend the same anchor.

The covenant commits to a 1-block relative lock on `O_i`, so there is at most one publish transaction per Bitcoin block. Skipped Bitcoin blocks are allowed. The protocol guarantees "at most one publish per Bitcoin block", not "exactly one".

## Canonical publish transaction

A publish transaction has the following shape:

```text
tx.version  = 2
tx.locktime = 0

vin[0]: covenant input
  prevout    = previous next output O_i
  nSequence  = 1
  annex      = absent
  witness    = covenant witness

vin[1]: commit input
  prevout    = commit output C_i, created by K_i
  nSequence  = 0xffffffff
  annex      = 0x50 || subblock_payload_i
  witness    = Taproot spend satisfying C_i's script

vout[0]: next output
  value      = V_next
  scriptPubKey = next covenant output

vout[1]: anchor output
  value      = V_anchor
  scriptPubKey = anchor script
```

`V_next` is a fixed minimal amount for the covenant-controlled next output. `V_anchor` is a fixed minimal amount for the persistent anchor output. The anchor cannot be zero-value if it must survive until the next slot; it should be high enough for the desired relay/mining policy.

The publish transaction has no change output. The publisher chooses the value of `C_i` so that `P_i` pays the desired fee exactly:

```text
fee(P_i) = value(O_i) + value(C_i) - V_next - V_anchor
```

No `OP_CHECKSEQUENCEVERIFY` is needed. The covenant commits to `tx.version = 2` and to the full sequence vector via `sha_sequences`. Since `vin[0].nSequence = 1`, BIP-68 interprets it as a block-based 1-block relative lock. Therefore `P_{i+1}` cannot be mined in the same Bitcoin block as `P_i`.

`vin[1].nSequence = 0xffffffff` avoids imposing an accidental relative lock on the commit input. `vin[0].nSequence = 1` also makes the transaction opt-in replaceable under ordinary RBF policy.

## Commit transaction and anchor

The commit transaction `K_i` has the following role:

```text
K_i:
  vin[*] includes A_i
  vin[*] includes publisher funding inputs
  vout[c] = C_i
  optional change outputs
```

`C_i` is an exact-value Taproot output. It commits to the data-bearing publish transaction through a script leaf such as:

```text
<publisher_key> OP_CHECKSIGVERIFY
OP_TEMPLATEHASH <T_i> OP_EQUAL
```

`T_i` is the template hash of `P_i` as evaluated by `vin[1]`. It commits to the publish transaction's version, locktime, sequence vector, outputs, input index, and `vin[1]` annex hash. Therefore `T_i` commits to:

```text
annex = 0x50 || subblock_payload_i
```

The publisher signature prevents third parties from spending `C_i` in a fake publish-shaped transaction. `OP_TEMPLATEHASH` does not commit to prevouts, so the signature should be a normal Taproot signature, not `ANYONECANPAY`.

`K_i` should not be considered a valid reservation by itself. For subchain validity, `K_i` and `P_i` must confirm in the same Bitcoin block. If `K_i` confirms without the corresponding `P_i`, it is treated like an arbitrary anchor spend: the anchor has been burned and the next carrier publish is a no-op repair.

## Why the covenant can stay payload-free

`OP_TEMPLATEHASH` executed in `vin[0]` commits to:

- `nVersion`,
- `nLockTime`,
- `sha_sequences`,
- `sha_outputs`,
- whether `vin[0]` has an annex,
- `vin[0]`'s input index, and
- `vin[0]`'s annex hash if it has one.

It does **not** commit to `vin[1]`'s prevout, amount, scriptPubKey, witness, or annex.

So the covenant can force the transaction shape, output shape, and cadence while leaving the publisher free to choose:

- the commit output `C_i`,
- the value of `C_i`,
- the fee paid by `P_i`, and
- the annex payload in `vin[1]`.

The covenant should commit to `vin[0]` having no annex. The subchain data lives only in `vin[1]`'s annex. The payload commitment is provided by the separate commit output `C_i`, not by the recursive covenant input.

## Subblock data

The subblock is simply:

```text
subblock_payload_i = annex[1:]
```

The first annex byte is the mandatory `0x50` marker. The remaining bytes are arbitrary and have no Bitcoin-level format.

Because the annex is witness data, it receives witness weight treatment. A publish transaction can therefore carry up to roughly one Bitcoin block's worth of witness payload, minus transaction overhead: about 4 MB in the extreme case.

Bitcoin consensus does not require `vin[1]` to contain an annex. Subchain clients must define how to treat missing, malformed, or invalid payloads. In this construction, such cases are treated as no-op subblocks: the carrier state advances, but the subchain state does not.

## Publisher competition

Publishers compete to create the next subblock by broadcasting conflicting packages:

```text
same O_i
same A_i
different K_i
different C_i
different annex payload
different fee
```

All honest `K_i` candidates spend the same `A_i`, so only one anchored commit transaction can confirm. All `P_i` candidates spend the same `O_i`, so only one publish transaction can confirm.

This avoids the wasteful case where many publishers get commit transactions mined but only one publisher gets a block. Losing commit transactions conflict on `A_i` and remain unconfirmed.

The remaining failure cases are bounded per slot:

```text
1. O_i is spent by a publish-shaped transaction whose commit parent did not spend A_i.
   Result: one no-op carrier block.

2. A_i is spent arbitrarily, or K_i confirms without a same-block P_i.
   Result: the anchor is burned; the next O_i spend is a no-op repair block.
```

These failures do not corrupt the subchain. They only create empty/no-op carrier steps. A repeated attacker can still cause liveness griefing by repeatedly winning the anchor race or publishing junk, but each attempt must consume fees and blockspace.

In the public mempool, competition can use RBF and package relay. Out of band, miners can simply choose the package they prefer, usually the one paying the highest fee.

## Covenant variant A: finite TH-only chain

The trustless construction uses only `OP_TEMPLATEHASH`.

At height `i`, the covenant script is:

```text
OP_TEMPLATEHASH <H_i> OP_EQUAL
```

`H_i` is the template hash of the valid publish transaction at that height. The transaction creates both:

```text
vout[0] = O_{i+1}
vout[1] = A_{i+1}
```

The hashes are computed backwards from a terminal height:

```text
choose terminal script S_N
compute H_{N-1} for a publish tx paying to S_N and creating A_N
define S_{N-1} = OP_TEMPLATEHASH <H_{N-1}> OP_EQUAL
compute H_{N-2} for a publish tx paying to S_{N-1} and creating A_{N-1}
...
```

For a 100-year horizon, this requires about 5.26 million publish templates. That is finite but practical: the raw hashes are about 168 MB, and publishers can store a window or recompute batches as needed.

Advantages:

- no trusted setup,
- no deleted-key assumption,
- only requires `OP_TEMPLATEHASH`.

Disadvantages:

- finite lifetime,
- changing script at every step,
- publishers/indexers need access to the hash schedule.

## Covenant variant B: recursive deleted-key chain

The compact construction uses `OP_TEMPLATEHASH`, `OP_INTERNALKEY`, and `OP_CHECKSIGFROMSTACK`.

The covenant script is constant:

```text
OP_TEMPLATEHASH
OP_INTERNALKEY
OP_CHECKSIGFROMSTACK
```

The spend witness provides a single reusable signature:

```text
<S>
```

Setup:

1. Generate signing key `x` and public key `P`.
2. Use `P` as the Taproot internal key.
3. Construct the recursive covenant output and canonical publish template.
4. Compute the invariant template hash `H`.
5. Sign `H` with `x`, producing `S`.
6. Publish `S`.
7. Delete `x`.

Every future publish transaction reuses the same signature `S`. This works because the template hash does not commit to prevouts or input amounts, and because the output pays back to the same covenant script while recreating the same anchor output shape.

Advantages:

- infinite lifetime,
- constant script and address,
- no hash schedule,
- simple publisher flow.

Disadvantages:

- trusted setup / key-deletion assumption,
- if `x` survives, the holder can authorize other templates,
- if `P` is also the Taproot internal key, a surviving `x` can also key-spend the output.

A safer but slightly larger variant embeds `<P>` directly in the script and uses a NUMS internal key:

```text
OP_TEMPLATEHASH
<P>
OP_CHECKSIGFROMSTACK
```

This avoids a key-path escape hatch but still relies on deletion of `x` to make the recursive covenant binding.

## Subchain validation

A subchain client follows Bitcoin blocks and tracks the current carrier state:

```text
(O_i, A_i)
```

For each Bitcoin block:

1. find the confirmed transaction `P_i` spending the current next output `O_i`, if any;
2. check that `P_i` has the canonical publish shape and creates `O_{i+1}` and `A_{i+1}`;
3. find the transaction `K_i` that created `P_i.vin[1].prevout`;
4. check that `K_i` confirms in the same Bitcoin block as `P_i`;
5. check that `K_i` spends the current anchor `A_i`;
6. check that the commit output `C_i` commits, via `OP_TEMPLATEHASH`, to `P_i` at input index 1 and to `vin[1]`'s annex hash;
7. extract `vin[1]`'s annex payload, if present;
8. apply the subchain's own consensus rules to the payload; and
9. update the carrier state to `(O_{i+1}, A_{i+1})`.

If any data-validity check fails, the transaction is treated as an empty/no-op subblock. The client still updates the carrier state to `(O_{i+1}, A_{i+1})`, because Bitcoin has already advanced the covenant chain by spending `O_i`.

Reorgs are handled like ordinary Bitcoin reorgs: roll back publish transactions from disconnected blocks and apply the new best chain.

Bitcoin does not validate the subchain's internal rules. It only provides ordering, timestamping, data publication, and fee-based publisher selection.

## Deployment notes

- BIP-448 is a proposed soft fork, not an active Bitcoin consensus rule.
- Annex-bearing transactions are consensus-valid under Taproot rules, but may be nonstandard under default relay policy.
- Until relay policy changes, publish transactions may require direct miner submission or miners/pools willing to mine nonstandard transactions.
- The commit/publish pair is best relayed and mined as a package. For subchain validity, they must confirm in the same Bitcoin block.
- The anchor output is a persistent sequencing token, not a zero-value ephemeral anchor. It should use the smallest value compatible with the desired relay/mining policy.
- High fees can incentivize miners to include these transactions even if ordinary relay does not support them.
- Long-term subchain nodes must retain the annex payloads; ordinary pruned Bitcoin nodes may discard old witness data.
- The subchain must define how to handle empty, missing, malformed, or invalid payloads. Bitcoin will still advance the covenant chain if the publish transaction is valid.

## TXID as the subblock chain tip

The subchain chaintip after subblock `i` is:

```text
tip_i = txid(P_i)
```

Although the annex is witness data and is not directly included in a Bitcoin `txid`, this construction makes `txid(P_i)` commit to the subblock payload indirectly:

```text
txid(P_i)
  commits to vin[1].prevout = C_i
    commits to txid(K_i)
      commits to C_i's script
        commits to T_i
          commits to P_i's vin[1] annex hash
            commits to 0x50 || subblock_payload_i
```

`txid(P_i)` also commits to `vin[0].prevout = O_i`, which was created by `P_{i-1}`. Therefore, by induction:

```text
txid(P_i) commits to every valid subblock payload from genesis through i.
```

The anchor adds the anti-waste property. Since `K_i` must spend `A_i`, all honest commit transactions for slot `i` conflict with each other. Only the winning anchored commit can be mined, and the publish transaction that spends `O_i` becomes the next Bitcoin-level chaintip for the subchain.

If a publish transaction is malformed, unanchored, or carries an invalid payload, its `txid` still becomes the carrier tip, but it represents an empty/no-op subblock. Thus the rule is simple:

```text
valid anchored payload  -> txid commits to the applied subblock data
invalid or unanchored   -> txid commits to an empty/no-op carrier step
```

This gives the desired blockhash-like property: the latest publish transaction ID is the subchain chaintip, and for every applied subblock, that `txid` commits to all data in the subchain history.

## References

- [BIP-448: Taproot-native (Re)bindable Transactions](https://github.com/bitcoin/bips/blob/master/bip-0448.md)
- [BIP-446: OP_TEMPLATEHASH](https://github.com/bitcoin/bips/blob/master/bip-0446.md)
- [BIP-348: OP_CHECKSIGFROMSTACK](https://github.com/bitcoin/bips/blob/master/bip-0348.md)
- [BIP-349: OP_INTERNALKEY](https://github.com/bitcoin/bips/blob/master/bip-0349.md)
- [BIP-341: Taproot](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki)
- [BIP-68: Relative lock-time using consensus-enforced sequence numbers](https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki)
- [Recursive covenant with CTV and CSFS](https://groups.google.com/g/bitcoindev/c/Tu7mr419jWQ/m/4bJ3UpaSAQAJ)
````
