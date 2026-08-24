# Bridge to Citrea | Citrea

Source: https://docs.citrea.xyz/welcome/bridge-to-citrea

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

👋

Welcome

Bridge to Citrea

This guide explains how to bridge assets to Citrea from Bitcoin and Ethereum.

Bridge from Bitcoin

Citrea offers two bridging options depending on your deposit amount.

Option 1: Clementine (10 BTC or multiples, Web App or CLI)

For deposits of 10 BTC, use

Clementine

—Citrea's canonical, trust-minimized Bitcoin bridge. To use it, follow the

Using Clementine

guide (Clementine Web App or command-line tool).

Clementine is the

canonical bridge

of Citrea. It provides the highest security guarantees by leveraging BitVM-based verification on Bitcoin.

Clementine only supports

10 BTC per transaction

. To bridge larger amounts (e.g., 40 BTC), you must perform multiple separate deposits of 10 BTC each.

Steps:

Open the

Clementine Web App

or install the

Clementine CLI

; see the

Using Clementine

guide for details

Follow the deposit instructions in the app or in the

CLI documentation

Repeat the process for each additional 10 BTC you wish to bridge

Option 2: Symbiosis (Best for Smaller Transactions)

For deposits less than 10 BTC, use

Symbiosis

.

Steps:

Go to

Symbiosis Swap page

Set

Bitcoin

as the source chain and

Citrea

as the destination

Select

cBTC

as token

Enter the amount you want to bridge

Enter a BTC refund address

Enter your Citrea address or connect your wallet

Symbiosis functions as a cross-chain swap. The amount of BTC received is subject to swapping quotes, which depend on the cBTC-syBTC liquidity pool.

Option 3:

Atomiq Exchange

(Supports Bitcoin and Lightning routes)

For deposits less than 10 BTC or deposits via the Bitcoin Lightning network use atomiq.exchange

Steps:

Go to

app.atomiq.exchange

Bitcoin on-chain is pre-selected as the source, if you wish to swap from Bitcoin Lightning Network, select the Bitcoin (lightning L2) asset in the "You pay" section

Enter the amount you want to bridge (you can specify either input or output amounts)

Connect your Citrea wallet or type in the destination Citrea address

Connect your Bitcoin wallet (e.g. UniSat, Xverse or Magic Eden), not required for swap from Bitcoin Lightning Network

Click Initiate swap and confirm the transaction in your Bitcoin wallet, or send over the funds to the presented lightning network invoice (in case of Bitcoin Lightning Network)

The swap settles automatically after the bitcoin transaction gets confirmed (2 confirmations take on average 20 minutes), this is instant for Bitcoin Lightning Network

Atomiq

Bridge from Ethereum and other chains

Citrea supports multiple bridging options from Ethereum and other chains. LayerZero and Hyperlane are integrated directly into

Bridge Hub

, you can complete the entire bridging process without leaving the site.

LayerZero

Bridge (via Bridge Hub)

Bridge

USDT

,

USDC

, or

WBTC

from Ethereum, powered by LayerZero.

Destination Asset

USDT.e

USDC.e

WBTC.e

Assets are bridged at a 1:1 ratio.

Steps:

Go to

Bridge Hub

and select

Ethereum

Choose your source asset

Connect your wallet

Optionally

enable

Refuel Gas

for

gas drop

on Citrea

Complete the transaction

Bridge via Bridge Hub with LayerZero

This route supports gas refuel which allows you to send native gas (cBTC) to the Citrea to cover transaction fees. The equivalent amount is deducted from your source chain balance. Note that this is only available for LayerZero-supported routes where the input and output assets are the same (e.g., USDC → USDC.e, USDT → USDT.e, WBTC → WBTC.e).

Hyperlane

and

Swaps

(via Bridge Hub)

Bridge

USDC

or

USDT

from Ethereum to

ctUSD

, powered by Hyperlane and Swaps.

Steps:

Go to

Bridge Hub

and select

Ethereum

Choose USDC or USDT as the source

Choose ctUSD as destination

Connect your wallet

Complete the transaction

This route does not support gas refuel at this time.

Squid Router

You can also use Squid Router to bridge between Ethereum and Citrea.

Steps:

Go to

Squid’s app

Connect your wallet

Choose the token you want to pay with

Choose the token on Citrea you want to receive.

Submit and sign with your wallet

All bridges should take less than 20 seconds

Squid Router Bridge

Citrea Fast Bridge by

Avail

Bridge your unified USDC or USDT, across several chains, to USDC.e or USDT.e on Citrea, in one click.

Steps:

Go to the

Citrea Fast Bridge

Connect your wallet.

Select the asset on Citrea you want to bridge to (USDC or USDT)

Check your unified balance and break up across chains

Enter the amount and click

Bridge

Verify and Confirm the route (sources to be used and fees)

Avail Citrea Bridge

Citrea only maintains Clementine and USDT.e, USDC.e, WBTC.e bridges natively.

Stargate Bridge by

LayerZero

You can also use LayerZero's

Stargate Bridge

.

Steps:

Connect Wallet

Select source chain and token

Select Citrea as the destination chain and select token

Enter amounts

Optionally

Click advanced settings on the top right corner, select

Medium

for

Gas on Destination

to get your 2.5$ worth of gas drop

Click transfer to bridge

This route supports gas refuel which allows you to send native gas (cBTC) to the Citrea to cover transaction fees. The equivalent amount is deducted from your source chain balance. Note that this is only available for LayerZero-supported routes where the input and output assets are the same (e.g., USDC → USDC.e, USDT → USDT.e, WBTC → WBTC.e).

Previous

Chain Information - Quickstart

Next

TL;DR

Last updated

3 months ago

Was this helpful?

Bridge from Bitcoin

Option 1: Clementine (10 BTC or multiples, Web App or CLI)

Option 2: Symbiosis (Best for Smaller Transactions)

Option 3:

Atomiq Exchange

(Supports Bitcoin and Lightning routes)

Bridge from Ethereum and other chains

LayerZero

Bridge (via Bridge Hub)

Hyperlane

and

Swaps

(via Bridge Hub)

Squid Router

Citrea Fast Bridge by

Avail

Stargate Bridge by

LayerZero

Was this helpful?
