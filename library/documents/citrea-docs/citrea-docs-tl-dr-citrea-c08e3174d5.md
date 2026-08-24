# TL;DR | Citrea

Source: https://docs.citrea.xyz/essentials/introduction

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

TL;DR

Citrea is the first rollup that enhances the capabilities of Bitcoin blockspace with zero-knowledge technology, making it possible to

build everything on Bitcoin

.

Citrea requires no changes to the network's consensus rules. Citrea and Clementine have been live on Bitcoin since January 2026.

Citrea is a

rollup on Bitcoin

Citrea is a rollup

. It regularly submits

batch proofs

to Bitcoin - which also include the

state differences

for each batch, meaning that any changes from the start to the end of a batch are also available for anyone reading Bitcoin.

A Citrea full node can read the state differences and reconstruct the state directly from Bitcoin - unlike sidechains, in which only small cryptographic commitments are posted and it is impossible to reconstruct the state using that data.

Citrea uses

Bitcoin as a Data Availability layer

, and it's the only source of truth for the system. As long as Bitcoin is secure, the state of Citrea will be accessible and reconstructable.

Citrea is a

Type 2 zkEVM

Citrea is

EVM-compatible

. As a developer, you can write & deploy your smart contracts in Solidity using the standard EVM tooling.

Citrea processes a large number of zkEVM transactions off-chain. In

batches,

using these transactions, it generates succinct

STARK

proofs (later wrapped into succinct

SNARK

proofs). These proofs are then published to Bitcoin directly. This allows for easy client side verification of the batch validity in an inscription-like envelope.

Citrea's currency is Bitcoin

Citrea uses

Bitcoin

as its native currency. To avoid confusion and improve on/off-ramp UX, Citrea’s native Bitcoin is referred to as Citrea Bitcoin,

$cBTC

in short.

Citrea is designed to scale Bitcoin

As a separate execution layer, Citrea has different properties compared to Bitcoin and Ethereum. As an

independent execution layer

, it offers higher throughput, richer smart‑contract functionality, and lower fees than Bitcoin’s base layer, while still anchoring finality to Bitcoin.

Dimension

Citrea

Ethereum

Bitcoin

Execution

zkEVM

EVM

Bitcoin Script

Settlement

Bitcoin

Ethereum

Bitcoin

Data availability

Bitcoin via State Diffs

Ethereum

Bitcoin

Fees & Currency

BTC (cBTC)

ETH

BTC

Citrea has a native trust-minimized two-way peg: Clementine

Clementine is the BitVM-based trust-minimized two-way peg mechanism of Citrea. It uses

Light Client Proofs

that include recursively proven Citrea batch proofs, which enables

optimistic ZK Proof verification

on Bitcoin

using BitVM.

Clementine is

trust-minimized

as it has a

1-of-N trust assumption

, which means that as long as one single entity in the bridge verifier set is honest, no party can steal the pegged BTC from the bridge.

Clementine is deployed on Citrea mainnet. You can read more about Clementine

here

.

Citrea is audited & fully open-source

Citrea & Clementine are built in public.

Both Citrea and Clementine codebases are open-source:

https://github.com/chainwayxyz/citrea

https://github.com/chainwayxyz/clementine

Both Citrea and Clementine codebases are

audited

as of October 2025.

Previous

Bridge to Citrea

Next

Architecture and Transaction Lifecycle

Last updated

2 months ago

Was this helpful?

Citrea is a rollup on Bitcoin

Citrea is a

Type 2 zkEVM

Citrea's currency is Bitcoin

Citrea is designed to scale Bitcoin

Citrea has a native trust-minimized two-way peg: Clementine

Citrea is audited & fully open-source

Was this helpful?
