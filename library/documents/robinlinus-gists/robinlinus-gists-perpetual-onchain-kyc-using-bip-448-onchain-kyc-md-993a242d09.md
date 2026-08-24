# Perpetual Onchain KYC Using BIP 448 / onchain-kyc.md

Source: https://gist.github.com/RobinLinus/e0876dba90f9755103c05ad2bc9b4ee6#file-onchain-kyc-md

Retrieved: 2026-08-24T21:53:25Z

Extraction note: Current public gist file at revision 671cef18a01b9f804487fd42ccf9aae0e8caa728.

---

````markdown
# Onchain KYC and Whitelisted Custody Using BIP 448

A technical sketch of a “perpetual KYC” covenant using BIP 448’s proposed Taproot-native opcode bundle: BIP 446 `OP_TEMPLATEHASH` and BIP 348 `OP_CHECKSIGFROMSTACK`. BIP 448 also includes BIP 349 `OP_INTERNALKEY`, but this construction does not rely on it.

This is hypothetical. BIP 448, BIP 446, and BIP 348 are draft soft-fork proposals, and BIP 448 leaves activation to be determined later. The construction only works if the relevant opcodes are activated.

The same mechanism can be viewed in two ways:

```text
regulated custody:  coins can move only to approved KYC accounts
personal custody:   coins can move only to approved vault / recovery accounts
```

In the personal-custody version, the goal is coercion resistance. A high-net-worth individual can hold coins whose user key alone cannot send funds to an arbitrary attacker address. Even if the user is physically coerced, kidnapped, or forced to sign a ransom transaction, the transaction is invalid unless it matches a pre-approved template in the authority’s signature catalog.

The key design assumption in this writeup is that the authority signs the allowed transaction templates once and for all during setup. After setup, the authority does not participate in normal transfers. Users spend by selecting one of the already-published authority signatures for an approved transaction template.

The signature catalog is append-only. The authority can add more users later by signing and publishing additional template signatures for those users, but previously published signatures remain valid.

See also the original discussion on Delving Bitcoin: [Perpetually KYC’d Coins Using Evil Covenants](https://delvingbitcoin.org/t/perpetually-kycd-coins-using-evil-covenants/556).

## Design Goal

The goal is to keep a set of coins inside a whitelisted transfer graph. A constrained coin should only be spendable into new constrained outputs, so the restriction recurses from spend to spend.

This supports two closely related use cases:

```text
- compliance containment for ETFs, treasury companies, exchanges, and custodians
- coercion-resistant custody for high-net-worth individuals and family offices
```

In both cases, the user key alone is intentionally insufficient. The holder can authorize a spend, but only into an output vector that the authority pre-approved during setup or during a later catalog update.

The covenant does not read an onchain whitelist. Instead, the whitelist is a public catalog of authority signatures over approved transaction templates. The initial catalog is generated during setup, and the authority can extend it later by publishing additional signatures. A spend succeeds only if:

```text
- the user signs the transaction, and
- the witness includes an authority signature for the exact template hash.
```

Because the relevant authority signatures are generated before the spend occurs, the system is non-interactive at spend time. Adding a new user, vault, exchange account, custodian account, or recovery destination is a catalog-update operation, not an online approval step for each transfer.

## Setup Model

During setup, the authority fixes:

```text
- the allowed denominations
- the approved recipient account keys
- the denomination-specific authority keys
- the permitted transfer, split, and optional merge templates
- canonical nVersion, nLockTime, nSequence, annex, and output-ordering rules
- the fee-anchor policy
```

For an institutional deployment, the approved keys might belong to fund vaults, authorized-participant settlement accounts, exchange cold-storage wallets, market-maker accounts, or regulated custodial accounts.

For a high-net-worth personal vault, the approved keys might belong to:

```text
- the owner’s long-term vaults
- a family-office or trust recovery account
- a regulated custodian account controlled by the owner
- a pre-approved exchange account controlled by the owner
- an emergency recovery or legal-fiduciary account
```

An attacker’s fresh ransom address is deliberately absent from this graph. Adding it would require a new catalog update by the authority, not just the victim’s user signature.

For each allowed template, the authority computes the corresponding `OP_TEMPLATEHASH` message and signs it under the relevant denomination key. The resulting signature catalog can be published once.

For the simplest one-input payment template, the catalog is operationally indexed by:

```text
(recipient_key, denomination)
```

More generally, it is indexed by:

```text
(template_shape, output_assignment, denomination_key, input_position)
```

The catalog can be extended at any time. To add a new user, the authority signs the transfer, split, and other approved templates whose outputs contain that user’s key, then publishes those additional signatures. Existing coins and scripts do not need to change, as long as the same denomination authority keys and canonical template grammar are used.

This is still a setup-style model: the authority signs templates, not individual live transfers. New-user onboarding is just an additional batch of pre-signed templates. The tradeoff is that the catalog is naturally append-only. Adding approvals is easy; revoking already-published approvals is not.

## Operational Signing Architecture

The authority keys are high-value signing keys. They should be treated as cold-storage keys and used only to generate the setup catalog or later append-only catalog updates.

One operational model is an offline signing machine that takes a deterministic description of the approved users, denominations, and transition templates, computes the corresponding template hashes, and emits the authority signatures. The signer should not accept arbitrary transaction data from an online system; it should derive the templates from a constrained policy description.

For personal coercion resistance, the authority does not need to be a regulator. It could be the owner’s own cold-storage signing ceremony, a family office, a trust company, an attorney-controlled recovery process, a qualified custodian, or a multi-party committee. The important property is that the authority-signing process is separate from the wallet the victim can be forced to operate under duress.

The signer can also be TEE-backed. For example, a trusted execution environment can run the template-generation and signing code on an offline machine, with the authority relying on attestation, reproducible code, audit logs, and constrained inputs to reduce the chance that an operator signs an unintended template.

For stronger key isolation, the denomination authority key `A_d` can be a MuSig2 aggregate key controlled by multiple independent TEE-backed offline signers:

```text
A_d = MuSig2(TEE_1 key, TEE_2 key, ..., TEE_n key)
```

The output script does not need to know this. MuSig2 produces an ordinary BIP340-compatible Schnorr signature under the aggregate x-only public key, so the covenant script still contains only:

```bitcoin
<A_d> OP_CHECKSIGFROMSTACK OP_VERIFY
```

This turns catalog generation into a joint cold-storage ceremony: each TEE verifies the same policy description, participates in the MuSig2 signing flow, and contributes only if the requested template is allowed. No single TEE or operator needs to hold the full denomination signing key. In the plain MuSig2 model this is an n-of-n signing ceremony; threshold behavior would require an additional threshold-signing design.

This is an operational hardening technique, not a consensus requirement. TEEs and MuSig2 reduce some key-management risks, but they do not remove the need to audit the template generator, protect nonce generation, control policy inputs, and preserve logs of every published catalog update.

## Template Hash Semantics

BIP 446 `OP_TEMPLATEHASH` pushes a tagged hash of selected fields of the spending transaction onto the Tapscript stack.

Conceptually, the template hash commits to:

```text
nVersion
nLockTime
sha_sequences
sha_outputs
annex_present
input_index
sha_annex, if an annex is present
```

where:

```text
sha_sequences = SHA256(serialization of every input's nSequence)
sha_outputs   = SHA256(serialization of every output in CTxOut format)
```

The important consequences are:

```text
- OP_TEMPLATEHASH commits to the ordered nSequence vector for all inputs.
- The number of inputs is therefore committed to implicitly, because each nSequence is a fixed 4-byte field.
- OP_TEMPLATEHASH commits to the current input_index, so different inputs in the same transaction see different template hashes.
- OP_TEMPLATEHASH does not commit to input prevouts, spent amounts, or spent scriptPubKeys.
```

This matches the reference implementation shape:

```text
TemplateHash(
  tx.version,
  tx.nLockTime,
  m_sequences_single_hash,
  m_outputs_single_hash,
  annex_present,
  nIn,
  m_annex_hash if present
)
```

with `m_sequences_single_hash` computed over every input’s `nSequence`.

This omission of prevouts is what makes setup-time signing possible: the authority can sign reusable templates before knowing which exact UTXOs will later spend them.

## Basic Covenant Script

For each denomination `d`, the authority uses a distinct 32-byte x-only public key:

```text
A_d
```

A constrained coin of denomination `d`, owned by user key `U`, is represented as:

```text
KYC(d, U)
```

The name `KYC` is just a label for the examples. In a personal-custody deployment, the same object could be called `VAULT(d, U)` or `RESTRICTED(d, U)`.

`KYC(d, U)` is a Taproot output with amount `d` and a script path:

```bitcoin
OP_TEMPLATEHASH
<A_d> OP_CHECKSIGFROMSTACK OP_VERIFY
<U> OP_CHECKSIG
```

The witness stack for this script path is:

```text
<user_sig> <authority_template_sig>
```

Execution works as follows:

```text
1. OP_TEMPLATEHASH pushes the template hash for the spending transaction.
2. OP_CHECKSIGFROMSTACK verifies authority_template_sig under A_d over that template hash.
3. OP_VERIFY makes the authority check mandatory.
4. OP_CHECKSIG verifies the user’s ordinary Taproot signature under U.
```

Both `A_d` and `U` should be 32-byte x-only pubkeys. Do not rely on non-32-byte pubkey encodings here: unknown key types are future-upgrade hooks, and relying on them would make the script unsafe or policy-dependent.

The Taproot key path must be disabled or constrained by the same policy. If the output has a usable key-path spend, that key path bypasses the covenant script entirely. A typical construction should use an unspendable / NUMS internal key unless the key path is intentionally part of the same restricted policy.

## Recursive Transfer

A simple transfer of a 1 BTC KYC coin from Alice to Bob creates a new KYC output:

```text
KYC(1 BTC, Alice) → KYC(1 BTC, Bob)
```

The setup-time authority signature for this transfer commits to an output vector that recreates the KYC covenant structure with Bob’s approved key:

```text
KYC(d, Bob)
```

Because `sha_outputs` commits to output amounts and scriptPubKeys, the authority signature commits to the exact denomination, recipient key, covenant script, output ordering, and any fixed fee-anchor output.

The signature does not commit to Alice’s specific input UTXO. Any holder of a valid `KYC(d, U)` coin can use the same pre-signed template to pay the approved recipient, provided the holder can produce the user signature for the coin being spent.

## Setup-Time Approval Policy

The authority signs a template during setup only if:

```text
- every non-anchor output is a valid KYC output
- every recipient key appearing in the outputs is approved
- every output denomination is approved
- the output amounts and output scripts match the denomination policy
- the transaction version, locktime, sequence vector, annex policy, and anchor policy are canonical
- the signature is issued under the denomination key for the current input
```

The authority should not describe this as “input value equals output value plus fees” unless it is careful about what is actually enforced. `OP_TEMPLATEHASH` does not commit to input amounts, so exact input-value accounting is not directly checked by the covenant. Instead, the construction relies on fixed denominations, denomination-specific authority keys, and disciplined creation of the KYC UTXOs.

If a UTXO is accidentally or maliciously locked under the wrong denomination script, the covenant will not detect the input amount. Excess value can become miner fee, and insufficient value simply makes the transaction invalid because the outputs cannot be funded.

## Denomination Keys

Using a separate authority key for each denomination prevents template-signature replay across denominations.

For example, a signature under:

```text
A_1BTC
```

cannot satisfy a script containing:

```text
A_0.5BTC
```

This makes the authority key itself a denomination tag. The denomination is also committed through the output amounts and output scripts in `sha_outputs`.

## Fees and Anchors

The parent KYC transaction should use a predictable fee policy so the authority can sign templates once during setup.

A practical pattern is to include a fixed Pay-to-Anchor (P2A) output and use a child transaction to pay the actual feerate via CPFP. The relevant BIP for P2A is BIP 433.

A P2A anchor output has scriptPubKey:

```bitcoin
OP_1 <0x4e73>
```

P2A anchors are keyless and intended as CPFP hooks. In adversarial settings, the design should be paired with anti-pinning relay-policy assumptions, such as TRUC / v3-style topology restrictions. Otherwise, anyone-can-spend anchors can create pinning or griefing risks.

Because the parent template commits to the full output vector and sequence vector, fee variation should happen through the child transaction, not by changing the parent template.

## Splits

Splitting is a transition from one denomination into approved smaller denominations:

```text
1 BTC → 0.5 BTC + 0.5 BTC
```

For example:

```text
KYC(1 BTC, Alice)
  → KYC(0.5 BTC, Alice) + KYC(0.5 BTC, Alice)
```

The authority signs the single-input split template during setup under `A_1BTC`. The output vector commits to both smaller KYC outputs and their exact scripts.

A split template is recipient-specific because the output scripts contain the recipient user keys. If splits are meant to preserve ownership, then the signature catalog needs split templates for each approved user key. Otherwise, a split can also be treated as a payment into multiple approved KYC outputs.

Splits are relatively straightforward because the approved output value is no greater than the current denomination being spent. Extra unrelated parent inputs cannot be added unless the pre-signed template permits the corresponding input count and sequence vector.

## Merges and Coinjoins

Multi-input transitions need more care.

A proposed merge might be:

```text
0.5 BTC + 0.5 BTC → 1 BTC
```

Because `input_index` is part of the template hash, input 0 and input 1 do not see the same template hash. A two-input merge therefore needs position-specific setup signatures:

```text
input 0: signature under A_0.5BTC over template_hash(input_index = 0)
input 1: signature under A_0.5BTC over template_hash(input_index = 1)
```

The shared `sha_sequences` value commits to the full two-input sequence vector, so the input count is fixed implicitly. However, `OP_TEMPLATEHASH` still does not commit to the prevouts, spent amounts, or spent scriptPubKeys of the other inputs.

This means a generic pre-signed merge template does not prove that every input is itself a KYC input. If the authority signs a template that lets one 0.5 BTC KYC input create a 1 BTC KYC output in a two-input transaction, an outside non-KYC input could potentially supply the other 0.5 BTC. That may be acceptable if the system permits outside value to enter the KYC set, but it is not acceptable if the KYC set must be closed to outside coins.

Therefore:

```text
Safe simple case:
  one-input transfers and one-input splits

Careful / policy-dependent case:
  multi-input merges, coinjoins, and any template whose KYC outputs
  exceed the denomination of an individual constrained input
```

If closed-set accounting is required, generic pre-signed merge templates are not enough. The design needs an additional mechanism or a stricter operational policy. Options include:

```text
- disallowing merges entirely
- allowing only single-input splits and transfers
- accepting that outside value can enter but cannot leave except through approved KYC outputs
- using a different covenant/introspection primitive that can bind the relevant spent inputs
```

## Ingress vs. Egress

This construction is primarily an egress-control mechanism. It prevents coins already locked under the KYC covenant from being spent to arbitrary non-KYC outputs.

It does not prevent outside users from voluntarily creating new outputs that match the KYC script template. Anyone can pay into a scriptPubKey. Once such an output exists, whether it is practically spendable depends on whether the signature catalog contains templates for that denomination and recipient key.

So the strongest claim is:

```text
KYC coins cannot leave the approved output graph.
```

A stronger claim such as:

```text
only originally issued KYC coins can ever be in the graph
```

is not enforced by this construction alone.

## Denomination Transition Graph

The simple denomination model is still useful:

```text
nodes: allowed denominations
edges: approved transfer or split transitions
```

For single-input payments and splits, setup-time signature-table size is roughly:

```text
approved recipient keys × denomination-transition templates
```

For multi-input templates, complexity grows with:

```text
transition shape × output assignment × input position × denomination key
```

because each input position has a distinct template hash.

This still avoids pairwise sender-to-recipient approvals for simple transfers, but it does not make arbitrary coinjoins free of complexity or policy risk.

## Revocation and Freshness

Setup-time authority signatures are reusable for as long as the corresponding template remains valid. Publishing a signature is effectively an irrevocable approval for that template.

The catalog can be extended by publishing additional signatures. This is how the authority adds new users: it signs the approved template set whose outputs contain the new user keys and publishes those signatures as a catalog update. Users can then spend into those new accounts without any online authority participation.

`OP_CHECKSEQUENCEVERIFY` and `OP_CHECKLOCKTIMEVERIFY` can enforce “not before” constraints. They do not make an approval expire after a deadline.

Because this construction assumes the authority signs templates ahead of time, the authority cannot freeze ordinary transfers merely by refusing to sign later. For any already-published template, there is no later signing step.

If revocation or freeze capability is required, it must be built into the covenant structure separately, for example by:

```text
- not pre-signing templates for high-risk recipients
- using narrow setup-time approval tables
- using delayed user spends plus a recovery path
- rotating into a new setup epoch with new authority keys
- adding a future expiry primitive, if one exists
```

## Institutional Use Case

A regulated institution could use this construction to keep coins inside an approved transfer graph without requiring the authority to be online for every transfer. The institution can onboard additional approved accounts later by publishing new template signatures for those accounts.

For governments, central banks, ETFs and other funds, the graph could contain only fund vaults, authorized-participant settlement accounts, designated custodians, and recovery paths. For corporate treasury companies, it could contain board-approved vaults, lenders, OTC desks, exchange accounts, and liquidation or acquisition paths. For exchanges, it could constrain cold storage so that coins can only move to approved hot wallets, institutional settlement accounts, recovery accounts, or other internal reserve wallets.

If a user key, custodian key, or operational wallet is compromised, the attacker cannot send the coin to arbitrary non-KYC outputs unless:

```text
- the Taproot key path is usable,
- the attacker spends to an already-approved recipient/template,
- the signature catalog was too broad, or
- the transaction uses a policy-dependent merge/ingress case that the system intended to forbid.
```

So the guarantee is best described as consensus-enforced containment, not absolute theft prevention.

The strongest conservative version requires:

```text
- no usable unrestricted key path
- conservative setup-time authority signatures
- denomination-specific authority keys
- no generic merge templates if closed-set accounting matters
- a recovery or freeze path if compromised keys must be handled quickly
```

## Personal Coercion / Ransom Use Case

The same construction can be used by high-net-worth individuals as a coercion-resistant Bitcoin vault.

The threat model is a “$5 wrench” attack, kidnapping, extortion, or ransom demand where the attacker can force the victim to unlock a wallet or produce a user signature, but cannot force the offline authority-signing ceremony to approve a new destination.

In this setting, the user key is not a complete spending capability. It is only one factor in a constrained spend. The attacker can obtain:

```text
<user_sig>
```

but the transaction still needs:

```text
<authority_template_sig>
```

for the exact template hash. If the attacker’s address is not already in the catalog, the forced transaction cannot satisfy the covenant script.

A personal vault might approve only outputs such as:

```text
KYC(1 BTC, owner_deep_vault)
KYC(1 BTC, family_office_recovery)
KYC(1 BTC, regulated_custodian_account)
KYC(1 BTC, owner_exchange_account)
```

A ransom output such as:

```text
plain_bitcoin_output(attacker_address)
```

is not an approved template, so the victim cannot create a valid spend to it even under coercion. This gives the victim a credible technical constraint: the wallet key they can access under duress is not sufficient to transfer the vault to an arbitrary address.

This can be combined with an intentionally slow recovery design:

```text
- large balances live in delayed covenant vaults
- normal transfers go only to pre-approved personal/custodial accounts
- new destinations require an offline catalog-update ceremony
- emergency recovery paths can race or override delayed user spends
- small day-to-day liquidity is kept separately outside the deep vault
```

A personal anti-coercion deployment should not pre-sign generic exit templates or unrestricted withdrawals to arbitrary addresses. Any path that converts the vault coin into unrestricted BTC can become the path an attacker forces the victim to use. If day-to-day liquidity is needed, it should be kept in a separate small hot wallet rather than in the deep vault.

The offline signing architecture matters here. The authority-signing process should be unavailable to the attacker at the point of coercion. For example, new catalog entries might require a cold-storage ceremony involving a family office, legal fiduciary, custodian, or multiple TEE-backed signers using MuSig2. A single hardware wallet in the victim’s possession should not be able to add new destinations.

This does not make the owner physically safe by itself. It is a financial containment mechanism. It does not help if the attacker can also coerce the recovery authority, compromise the offline signing process, force a transfer to an already-approved destination they control, or hold the victim through a long operational process. The point is narrower: a compromised or coerced user key cannot directly drain the vault to a fresh attacker address.

## Optional Recovery / Freeze Path

A compliance-oriented or anti-coercion version can use a Taproot tree with two script paths.

For institutions, the second path may be a regulatory recovery or seizure path. For personal vaults, it should be thought of as an emergency recovery / freeze path controlled by a fiduciary, family office, custodian, or multi-party recovery committee.

### Path 1: normal KYC spend, delayed

```bitcoin
<N> OP_CHECKSEQUENCEVERIFY OP_DROP
OP_TEMPLATEHASH
<A_d> OP_CHECKSIGFROMSTACK OP_VERIFY
<U> OP_CHECKSIG
```

### Path 2: recovery / freeze, immediate

```bitcoin
<recovery_pubkey> OP_CHECKSIG
```

Use a distinct `recovery_pubkey`; do not reuse the denomination template-signing key unless the authority intentionally wants those powers combined.

The CSV delay in Path 1 means the user cannot normally spend a newly received coin until it has aged by `N` blocks. During that period, the authority can exercise the recovery path first.

This is especially important in the setup-time signing model: the normal-path authority signatures already exist, so the authority cannot withhold them after detecting a compromise. The CSV delay gives the recovery path a first-move window.

The recovery path remains available after `N` blocks as well. After the delay has elapsed, the normal path and recovery path race; whichever valid spend confirms first wins.

Because `OP_TEMPLATEHASH` commits to the full `nSequence` vector, normal-path authority signatures must commit to sequence values compatible with the CSV delay.

As before, the Taproot key path must be disabled or restricted. Otherwise, it bypasses both script paths.

## Summary

The cleanest offline-catalog version of the construction is:

```text
- fixed denominations
- one setup phase for the initial catalog
- append-only catalog updates for new users, vaults, custodians, or recovery accounts
- setup-time template signatures, not online per-spend approvals
- one-input transfers
- one-input splits
- denomination-specific authority keys
- no unrestricted Taproot key path
- P2A / CPFP fee management
- no online authority participation during normal transfers
- optional offline / TEE-backed / MuSig2 catalog-signing ceremony
- institutional containment for funds, treasury companies, exchanges, and custodians
- personal coercion resistance for high-net-worth vaults
```

The main caveats are:

```text
- BIP 448 / 446 / 348 are draft proposals
- OP_TEMPLATEHASH commits to all input nSequence values and input_index
- input count is implicit through sha_sequences
- prevouts, input amounts, and spent scriptPubKeys are not committed
- multi-input merges require per-input-position signatures
- generic merge templates can admit outside value into the KYC set
- outside parties can create matching KYC outputs unless issuance is controlled operationally
- adding users, vaults, custodians, or recovery accounts is easy by publishing more signatures
- already-published approvals are hard to revoke
- coercion resistance depends on keeping the authority-signing process unavailable under duress
```

## References

- [BIP 448: Taproot-native (Re)bindable Transactions](https://github.com/bitcoin/bips/blob/master/bip-0448.md)
- [BIP 446: OP_TEMPLATEHASH](https://github.com/bitcoin/bips/blob/master/bip-0446.md)
- [BIP 348: CHECKSIGFROMSTACK](https://github.com/bitcoin/bips/blob/master/bip-0348.md)
- [BIP 433: Pay to Anchor (P2A)](https://github.com/bitcoin/bips/blob/master/bip-0433.mediawiki)
- [BIP 431: Topology Restrictions for Pinning / TRUC Transactions](https://github.com/bitcoin/bips/blob/master/bip-0431.mediawiki)
- [BIP 327: MuSig2 for BIP340-compatible Multi-Signatures](https://github.com/bitcoin/bips/blob/master/bip-0327.mediawiki)
- [BIP 341: Taproot](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki)
- [Delving Bitcoin: Perpetually KYC’d Coins Using Evil Covenants](https://delvingbitcoin.org/t/perpetually-kycd-coins-using-evil-covenants/556)
````
