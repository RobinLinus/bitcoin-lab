# Alpen enters partner integration phase

Source: https://www.alpen.org/blog/partner-integration-testnet-iii

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

July 28, 2026

Alpen enters partner integration phase

Alpen Testnet III provides a persistent public environment for partner integrations

Alpen Testnet III has launched on Bitcoin Signet, marking the beginning of Alpen's partner integration phase ahead of mainnet.

More than 21 launch partners across infrastructure, applications, and distribution are integrating on Testnet III ahead of Alpen mainnet. The launch moves Alpen from core infrastructure development into shared ecosystem preparation, giving partners a persistent public environment to run under mainnet-like constraints without real BTC at risk.

Across the ecosystem:

Wallets and exchanges looking to pilot Bitcoin-native financial products will integrate existing infrastructure to Testnet III through Bitcoin Signet.

Swap providers and bridge operators will test the plumbing between Alpen, its Strata bridge, and existing Bitcoin Signet infrastructure.

Application and infrastructure teams will get a broader surface for integration work.

The ecosystem is beginning to assemble around Alpen.

Alpen on Bitcoin Signet

Testnet III brings Alpen onto Bitcoin Signet, a Bitcoin public ecosystem testnet.

Alpen now operates alongside existing Signet activity in shared public blockspace. The network is exposed to public testnet conditions, including variable fees, block congestion, reorgs, and a rich ecosystem of Bitcoin protocols. Testnet III is Alpen's most realistic operational environment to date.

Earlier Alpen testnets tested core functionality in more controlled settings. Testnet III brings full Alpen functionality into a public Bitcoin test environment, giving partners a shared place to prepare against conditions closer to the network's long-term operating model.

Independent operators

Stakely

and

Chainflow

have joined Testnet III as bridge operators and are securing deposits and withdrawals.

P2P

will join the operator set soon. Together with Alpen Labs, these operators will test the Strata bridge's 1-of-N trust model for BTC in a distributed setting.

A new verifier architecture

Testnet III introduces the first garbled circuit-based verifier that is usable by the general public for Bitcoin applications. This verifier is at the core of Alpen's glock-based bridge architecture and incorporates the latest iteration of

Mosaic

. It represents a major step forward from our earlier BitVM-based designs, with a significantly smaller onchain footprint.

A lower onchain footprint reduces the cost of staking, which makes participation more accessible to a greater number of operators securing the protocol, while also resulting in lower fees for users. This reduction in cost is a result of the significant reduction in verification complexity that must be handled on Bitcoin itself.

Testnet III also introduces an evolved orchestration layer and upgradeability to the network. In previous testnets, the Alpen execution layer and Strata orchestration layer were tightly coupled, and neither could have their consensus rules changed without requiring a network regenesis. In Testnet III, Alpen and Strata are now decoupled and upgradeable. With this decoupling, along with work on a new type of account system on Strata, it is now possible to deploy additional rollups and other provable programs on Strata alongside Alpen, all sharing access to the same Strata bridge. Upgradeability enables future consensus updates without requiring a regenesis, giving Alpen a more flexible foundation for continued development.

Preparing for Bitcoin-native financial markets

Alpen’s purpose is to make Bitcoin-native financial markets possible. Testnet III is a rehearsal for market formation: a shared environment where operators, applications, liquidity, and distribution can begin moving together before mainnet.

With a persistent public Bitcoin environment, institutional operators, more than 21 launch partners preparing across the ecosystem, and a new verifier architecture, Alpen is entering its final major stage of validation ahead of mainnet.

Bitcoin-native financial markets will form around credible infrastructure. Testnet III is where that infrastructure starts meeting the ecosystem around it.

Docs:

docs.alpen.org

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
