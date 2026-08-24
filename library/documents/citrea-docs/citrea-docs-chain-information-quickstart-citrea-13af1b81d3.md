# Chain Information - Quickstart | Citrea

Source: https://docs.citrea.xyz/welcome/chain-information-quickstart

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

Chain Information - Quickstart

Core Parameters

Network Name

Citrea Mainnet

Chain ID

4114

Currency Symbol*

cBTC

Currency Decimals

18

Currency Name

Citrea Bitcoin

HTTP RPC URL

https://rpc.mainnet.citrea.xyz

Block Explorer

https://explorer.mainnet.citrea.xyz

Network Type

EVM-compatible ZK Rollup (Type II zkEVM)

Block Time

2 seconds

Block Gas Limit

10,000,000

Latest Supported EVM Version

Pectra**

Settlement & Data Availability Layer

Bitcoin

Genesis Specs

evm.json

Currency Logo

cBTC Logo

Chain Logo

Citrea Brand Kit

*native currency, not ERC-20

\

**differences explained in the

Execution Environment

page

Kickstart Development

Add Citrea to your Wallet / Code

For wallets, you can either use the information above, click & add using

Chainlist

,

or the following JSON as the baseline:

Network Name

Citrea Mainnet

Default RPC URL

https://rpc.mainnet.citrea.xyz

ChainID

4114

Currency Symbol

cBTC

Block Explorer URL

https://explorer.mainnet.citrea.xyz/

Get cBTC

cBTC is used as the native currency to cover gas, which is necessary to deploy smart contracts & use the network.

Head over to

Bridge Hub

to Bridge BTC from Bitcoin; USDC, USDT or WBTC from Ethereum.

Where to go from here?

Here are quick links you might be looking for:

RPC Endpoints

includes support for

eth_

endpoints, along with useful Bitcoin & finality related endpoints of Citrea

Ecosystem Tooling

partners to check out for Interop, Oracles, Indexers, Wallets, Account Abstraction...

Citrea Execution Environment

explainers on subtle differences of Citrea compared to Ethereum and other EVM environments

System Contracts

a set of pre-deployed smart contracts on Citrea that can be used to verify Bitcoin transactions, execute bridge logic, and more

Previous

Getting started

Next

Bridge to Citrea

Last updated

6 months ago

Was this helpful?

Core Parameters

Kickstart Development

Add Citrea to your Wallet / Code

Get cBTC

Where to go from here?

Was this helpful?

Copy

{

"chainId": "0x1012",

"chainName": "Citrea Mainnet",

"nativeCurrency": { "name": "cBTC", "symbol": "cBTC", "decimals": 18 },

"rpcUrls": ["https://rpc.mainnet.citrea.xyz"],

"blockExplorerUrls": ["https://explorer.mainnet.citrea.xyz"]

}
