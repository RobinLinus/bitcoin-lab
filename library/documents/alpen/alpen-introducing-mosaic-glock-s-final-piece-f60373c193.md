# Introducing Mosaic: Glock's final piece

Source: https://www.alpen.org/blog/introducing-mosaic-glocks-final-piece

Retrieved: 2026-08-24T21:53:09Z

---

Skip to content

Docs

Ecosystem

Research

About

Blog

Written content

Protocol

May 7, 2026

Introducing Mosaic: Glock's final piece

Mosaic realizes the Glock paper's vision at a low onchain cost.

Today we’re releasing Mosaic, a practical fault-proof verifier with production Rust code and security strong enough to host financial markets on Bitcoin.

Mosaic allows Alpen to verify arbitrary computation on Bitcoin securely and elegantly. It realizes

the Glock paper

vision at a low onchain cost, making the path from research primitive to production protocol much more concrete.

Read the preprint:

Mosaic: Practical Malicious Security for Garbled Circuits on Bitcoin

Explore the codebase:

github.com/alpenlabs/mosaic

Why Mosaic matters

Garbled circuits enable optimistic verification on Bitcoin. A prover commits to a circuit offchain. If the prover submits an invalid proof, the verifier can evaluate the circuit to recover a signature that serves as an onchain fault proof.

The challenge is proving that the garbled circuit was built honestly. The standard cryptographic answer is cut-and-choose: generate many garbled copies, open some at random, and keep the rest for evaluation.

On Bitcoin, that approach is expensive because each saved copy normally needs its own set of signatures posted onchain. Mosaic removes that scaling penalty by generating the copies in a structured way, so one set of onchain signatures can support evaluation across many copies.

More security costs more offchain work for the prover, but it does not require proportionally more permanent Bitcoin blockspace.

From Glock to production

Glock introduced the core idea. Mosaic fills in the production system around it: a protocol specification, security analysis, and a Rust implementation for the cryptography, networking, storage, and state management needed to operate the verifier.

With Mosaic, Alpen Mainnet can bring verifiable financial markets to Bitcoin with the security model that made Glock compelling in the first place.

Alpen powers Bitcoin-native financial markets, secured by zero-knowledge proofs.

Product

Docs

Get started on testnet

Architecture

Solutions

Pages

Ecosystem

Research

Blog

Company

About

Careers

Brand kit

Contact

Social

X

LinkedIn

Telegram

YouTube

©

2026

Alpen

. All rights reserved.

Privacy Policy.

Terms of Service.

Financial infrastructure and research for Bitcoin.
