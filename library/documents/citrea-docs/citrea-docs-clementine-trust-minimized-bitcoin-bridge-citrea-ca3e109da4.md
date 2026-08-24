# Clementine: trust-minimized Bitcoin Bridge | Citrea

Source: https://docs.citrea.xyz/essentials/clementine-trust-minimized-bitcoin-bridge

Retrieved: 2026-08-24T21:53:35Z

---

Citrea

⌘

Ctrl

k

Website

Blog

Join The Community

More

Citrea

👋

Welcome

Getting started

Chain Information - Quickstart

Bridge to Citrea

🔎

Essentials

TL;DR

Architecture and Transaction Lifecycle

Clementine: trust-minimized Bitcoin Bridge

Using Clementine

Execution Environment

Security Properties

Transaction Finality

🪙

CTR Token

Overview

Staking & Governance

Supply & Allocations

📖

Developer Documentation

Kickstart

Chain Information

Citrea USD: ctUSD

CTR & xCTR

Canonical Contract Addresses

Canonical Bitcoin Addresses

Run Citrea Full Node

Deployment Guide

Ecosystem Tooling

System Contracts

secp256r1 & Schnorr Precompiles

RPC Documentation

Bitcoin Appchains (L3)

⚙️

Advanced

Fee Model

Proofs

Data Availability

Reorg Handling

Citrea Mempool

Security Council

Clementine Signers

🔒

Security

Audits & Security

Trusted Setup Verification

🔬

Future Research

Decentralized Sequencer Network

Lightning Integration

Multi Prover

Multi VM Approach

Trustless Atomic Swaps

Trustless Settlement

Volition Model

🌐

Community

Citrea Meetups

📕

Glossary

Glossary

Powered by GitBook

On this page

For the complete documentation index, see

llms.txt

. This page is also available as

Markdown

.

Copy

On this page

🔎

Essentials

Clementine: trust-minimized Bitcoin Bridge

Clementine is Citrea’s native two‑way peg that moves BTC ↔ cBTC in a trust-minimized way.

Why Clementine?

Existing Bitcoin bridges usually depend on trusted multisigs or on separate chains/consensus, pushing users to accept an

honest‑majority

assumption and moving economic activity away from Bitcoin.

Clementine is a trust-minimized solution based on

BitVM2

- a new breakthrough that enables optimistic verification of ZK Proofs directly on Bitcoin without any changes / soft-forks.

Using BitVM2, one can:

verify the correctness of a ZK Proof

on Bitcoin

and, in case a provided proof is not correct, can determine and take action against it

on Bitcoin.

With the help of BitVM2 Clementine keeps the safety of funds

on Bitcoin,

reduces the peg-out trust to

“1‑of‑N honesty”,

and achieves trust-minimization:

One honest

Signer

ensures funds can only follow pre‑approved spend paths.

One honest

Watchtower

can block a claim anchored to the wrong Bitcoin chain.

One rational

Challenger

can prove an invalid computation and seize a malicious Operator’s collateral.

As long as 1-of-N honest assumption holds, funds are

protected

against

both

liveness failures and theft.

Clementine is formally described and explained in its

whitepaper

. Clementine is also open-source, you can read the codebase

here

.

In this page, we provide a detailed high-level overview of the protocol. For a formal definition with more explanations, please refer to the whitepaper.

Let's continue with the roles in the Clementine bridge.

Roles and Responsibilities

There are

five

major roles on a functional Clementine bridge. In this section we provide the major definition of these roles, and in the following sections you may understand their exact functions under different conditions.

Users

- start peg‑ins (deposits BTC to mint

cBTC

, Citrea's native asset) and peg‑outs (burn

cBTC

to a system contract to withdraw BTC to Bitcoin).

Signers

- a committee of n signers that

pre‑signs the allowed spend rules

. These signers emulate

covenant

‑like restrictions: funds can only move along Clementine’s approved paths, or they are returned to the user if user deposit is not moved to vault by signers in time.\

A third option is the optimistic payouts, which we discuss in the following sections

.

Operators

- entities who

facilitate fast withdrawals to Bitcoin by fronting BTC

payments to the user and

later claim reimbursement from the bridge vault

if nobody can prove malicious or fraudulent intent. In the case of malicious Operator intent, Clementine initiates a challenge response game described in the sections below.\

to make sure economics are safe, Operators put a slashable bond to the protocol (~ 2 BTC). This is discussed under section 5.

Watchtowers

- entities who monitor both Citrea and Bitcoin. In the case of an initiated challenge transaction where malicious intent by an operator is detected, watchtowers are responsible for publishing the compact

Bitcoin header-chain proof

with total work.

Challengers

- entities who

force

an operator to prove their intent by initiating a Challenge transaction and using the header-chain proof published by the watchtower.

These entities are not mutually exclusive. For example, in mainnet, a signer in Clementine will also function as a watchtower and a challenger. Thus, roughly, the following relation will hold:

Operators ⊆ Signers ⊆ Watchtowers ⊆ Challenger ⊆ Users (permissionless)

How funds move around

In this section we go over the flow of the funds based on the protocol's rules, for both peg-in(s) and peg-out(s).

A) Peg-in (BTC → cBTC)

Peg-in flow to Citrea is fairly simple:

User deposit:

user sends

10 BTC

to a

Taproot

address that encodes two paths:

Bridge path:

spendable only with all Signers' signatures and inscribing the user's EVM address in the witness script.

Refund path:

the user can take funds back after a timelock (

OP_CSV

) if the bridge doesn’t act as described below in 200 Bitcoin blocks. This timeout prevents funds from getting stuck if Step 2 does not happen.

Move BTC to vault:

Signers sign the transaction that moves the deposit into a "vault" UTXO that is only spendable by the bridge’s allowed exits.

This

MovetoVault

transaction

emulates

covenants with pre‑signed transactions and MuSig‑style aggregation. Funds

must

follow the pre‑signed paths if at least one signer is honest.

Mint on Citrea:

Once the

MovetoVault

transaction is successfully finalized (6+ blocks), the

Bridge

system smart contract on Citrea checks its validity using the

BitcoinLightClient

smart contract. The contract then mints

10 cBTC

to the user’s Citrea address (the address is bound in the deposit).

B) Peg‑out (cBTC → BTC)

Bridging from Citrea to Bitcoin (converting cBTC on Citrea to BTC on Bitcoin) is handled in a couple steps.

First, a user should

burn

their cBTC on Citrea using the

Bridge

system contract using the

safeWithdraw

function. Then, they need to submit their request to exit to the Operators of the bridge using a

Payout

transaction template that includes their BTC address and the amount. As a special template, this is a presigned transaction that requires an additional UTXO input from an operator.

After user's burn, there are two scenarios

Optimistic Case

: This is the case where there's no one malicious.

Dispute & Challenge Case

: This is the case where there's an operator with malicious intent.

Let's cover these cases in separate sections, in detail.

Peg-out Scenario 1: Happy Case

If there is no malicious intent from the operators, the payout can be completed in two ways:

Optimistic Payout with n Signers:

If all signers are online, they can give signatures and directly transfer the BTC to the user address without the need of Operator. We call this an

optimistic payout

- just like a regular transfer from an n-of-n multisig.

Operator Payout:

If a signer is not online for

12 hours

, the optimistic payout above cannot be completed. Thus, the user still needs to be paid. In this case, an operator from the operator set steps in and fetches the Payout template from the user. The operator then attaches their own inputs to the template and broadcasts the

Payout

transaction. This template uses

SIGHASH_SINGLE|ANYONECANPAY

, so the user’s output is locked while any Operator can fund it.

From the user’s perspective, once either of these transactions is finalized, the withdrawal is complete.

If the payout is completed through an Operator Payout (step 2), then the operator needs to be

reimbursed

from the bridge vault on Bitcoin. It is completed as follows:

The operator asks for reimbursement by posting a claim transaction (called

KickOff

) on Bitcoin.

This starts a challenge window. If nobody disputes in a predetermined time period (i.e. 1.5 days where everything is fine), the Operator is able to post another transaction called

NoChallenge

, that gets unlocked only upon timelock expiry. Using this

NoChallenge

transaction, Operator can reimburse itself.

For the cases above so far, we assumed that operators are honest. However... what if an Operator claims a payment that did not happen? What if they are malicious?

This leads us to the

Dispute

scenario. Let's go over it.

Peg-out Scenario 2: Dispute & Challenge Case

Green Boxes indicate Operator reimbursement, whereas grey boxes indicate cases that Operator is slashed & kicked out from the vault.

If an Operator makes a fraudulent reimbursement claim (e.g., for a non-existent withdrawal), the protocol enters a dispute resolution phase enforced by Watchtowers and Challengers with the following steps:

Challenge Initiation:

A Challenger detects the fraudulent

KickOff

transaction by the operator and posts a

Challenge

transaction on Bitcoin, which signals the beginning of a dispute.

Watchtower Challenge Transaction:

After waiting enough time to make sure that an Operator is not trying to maliciously make a private Bitcoin fork with exceeding proof-of-work, a Watchtower posts the current finalized canonical Bitcoin header-chain proof with Work.

Challenge-Response Game:

The Operator is now forced to defend their reimbursement claim by providing a zkSNARK Light Client Proof of Bitcoin which shows their committed chain has more proof-of-work (than the Watchtower's claim) and includes the payout transaction in which the operator paid the user that withdrew funds from Citrea.

If the operator is not malicious

, by waiting some time and posting the correct Light Client Proof, it can win the challenge against the Challenger and get reimbursed. The only requirement for the Operator's Light Client Proof is to carry more Work compared to Watchtower's proof.

If the operator is malicious

, it cannot post a valid Light Client Proof with more work included due to hash rate. Whether it posts an invalid proof (or cannot prove that a valid payout exists), it will lose the challenge.

This phase uses BitVM - the complex computation is executed off-chain, but any step in the execution can be disputed and verified on-chain.

To summarize, after all the steps above, if the on-chain step confirms the Operator is dishonest, or if the Operator fails to provide a valid proof, their entire collateral bond is

slashed

.

Once an operator is slashed, they are also effectively

kicked out

of the Signer & Operator set to prevent any other malicious activity.

The disputes and challenges can occur for an honest operator as well. However, operator will win the challenge if it is honest and did not take any malicious actions, and the challenger will pay for the whole transaction fees.

Economics, Security, and Liveness

a) Operator's Bond

In Clementine, each operator locks

their own BTC

as a

bond

. That single bond backs a round of many user withdrawals and continues to persist as long as the operator is honest for consecutive rounds. If

any

paid withdrawal claim by an operator in the round is proven fraudulent (or the operator misses required steps during dispute), the bond is

slashed

and

none

of the reimbursements in that round are paid. This helps keep the bridge safe, as the operator is discouraged from making any malicious attempts, while the stake can be relatively low because one bond works for all claims.

b) Payoff Rounds & Capital Efficiency

Unlike BitVM2, Clementine requires only one successful challenge to slash an Operator's entire bond for a malicious case, preventing them from claiming

any

of their reimbursements for that payoff round. Also, upon the finalization of a round, the same collateral is reused for the next round as well. This drastically reduces the on-chain load and provides a strong economic deterrent against misbehavior.

c) Security & Liveness Guarantees

Let's go over a summary of Clementine's trust assumptions, as stated in the whitepaper too:

Clementine is trust-minimized as

1-of-N

- the bridge’s safety does not depend on a majority of honest actors, as explained in the sections above. It only requires

one honest participant

for each key role, out of N.

Clementine is

secure

as long as an attacker does not control more than 45% of Bitcoin's hash rate for 2 weeks.

Assuming the two conditions above hold,

incorrect peg-outs cannot succeed

, as they will be challenged and stopped. In that case, the user can be paid later by another operator.

Also in a case where a watchtower and challenger duo is malicious, the operator can provide their valid proofs and win the challenge, which prevents any potential DOS attacks.

During a peg-out, the same

Payout

template cannot be used twice. Therefore,

a withdrawal request cannot be paid twice

.

Implementation Notes

The deployed version of Clementine incorporates two design decisions that differ from the whitepaper. These are deliberate engineering choices made for the initial release, with no impact on the core security guarantees of the protocol.

Watchtower Circuit Simplification

In the whitepaper (Section 8), the Watchtower Circuit includes a verification step that checks whether the watchtower's submitted chain contains the block with the

payout_tx_blockhash

. In the deployed implementation, this step is omitted.

This simplification does not weaken Clementine's security model. Even without this additional check, a malicious watchtower would still need to control more than 50% of Bitcoin's total hash rate to affect the outcome of a dispute — the same fundamental security bound that protects the protocol overall.

Challenge Reimbursement

The whitepaper (Section 6.1) describes a mechanism where a Challenger includes an output with their Citrea address in the Challenge transaction, enabling cross-chain reimbursement of the challenge cost (

c

coins) via a light client proof if the challenge is successful.

This reimbursement mechanism is not included in the current deployment. In practice, this means the protocol's "existential honesty" assumption for Challengers is narrowed to Challengers who have sufficient capital to cover the upfront cost of issuing a challenge.

This is an acceptable trade-off for the initial version of Clementine. Ongoing research into

Clementine v2 with Garbled Circuits

is expected to substantially reduce the on-chain cost of challenges, making the financial barrier to challenging negligible in future versions and removing the need for a cross-chain reimbursement mechanism altogether.

Previous

Architecture and Transaction Lifecycle

Next

Using Clementine

Last updated

5 months ago

Was this helpful?

Roles and Responsibilities

How funds move around

A) Peg-in (BTC → cBTC)

B) Peg‑out (cBTC → BTC)

Economics, Security, and Liveness

a) Operator's Bond

b) Payoff Rounds & Capital Efficiency

c) Security & Liveness Guarantees

Implementation Notes

Watchtower Circuit Simplification

Challenge Reimbursement

Was this helpful?
