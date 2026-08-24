# Using Clementine | Citrea

Source: https://docs.citrea.xyz/essentials/using-clementine

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

Clementine Web App

Clementine CLI

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

Using Clementine

Clementine is Citrea’s trust-minimized Bitcoin bridge. You can use it only at

fixed size

: each deposit moves

10 BTC

from Bitcoin to Citrea (minting

10 cBTC

), and each withdrawal moves

10 cBTC

from Citrea to Bitcoin (paying out approximately

10 BTC

, subject to fees). There are no partial or custom amounts for a single Clementine operation; larger totals require separate 10 BTC (or 10 cBTC) operations.

To learn how the bridge works and read about its security properties, see

Clementine: trust-minimized Bitcoin Bridge

.

If you need to bridge

less than 10 BTC

, use third-party bridges. See

Bridge to Citrea

and

citrea.xyz/bridge

for options.

If you run into issues with Clementine tooling, email

clementine-cli@citrea.xyz

.

Clementine Web App

The

Clementine Web App

runs in your browser and walks you through Clementine deposit and withdrawal operations with on-screen steps and status. Use

clementine.citrea.xyz

on mainnet and

clementine.testnet.citrea.xyz

on testnet.

Clementine CLI

The

Clementine CLI

is a wallet-agnostic command-line tool for the same 10 BTC / 10 cBTC operations. It suits advanced setups (for example, air-gapped signing and scripting). The CLI docs cover installation, wallet usage, deposit and withdrawal guides, and reproducible builds.

Previous

Clementine: trust-minimized Bitcoin Bridge

Next

Clementine Web App

Last updated

3 months ago

Was this helpful?

Clementine Web App

Clementine CLI

Was this helpful?
