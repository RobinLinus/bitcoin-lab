# Proof of Work

Source: https://www.alpen.org/blog/proof-of-work

Retrieved: 2026-08-24T21:53:09Z

---

Skip to content

Docs

Ecosystem

Research

About

Blog

Written content

Research

June 6, 2024

Proof of Work

Early research efforts at Alpen Labs

We started Alpen Labs in June 2022. Our founders have personal backgrounds in Nepal, a country where 25% of the GDP comes from remittances. This background primed us to see early on the powerful potential for bitcoin to disintermediate middle-men and lower the cost of global payments.

When we first started Alpen Labs, we knew we wanted to build something on bitcoin that would democratize global access to payments and finance. We started by exploring the Lightning Network, an exciting and relatively new protocol built on bitcoin that enabled fast and low-cost payments. After a deeper dive, we realized that Lightning itself would face numerous challenges and tradeoffs as usage grew, particularly around privacy, centralization, and UX. We explored alternative ways to safely expand the utility of bitcoin that could help Lightning and other L2 protocols scale. Later in 2022, we concluded that zk-SNARKS will be a core part of scaling bitcoin globally.

The

rapid evolution

of this cryptographic primitive finally made it a practical tool to expand the accessibility and utility of bitcoin. Further, it was consistent with bitcoin's design philosophy that blockchains should primarily

verify

computation, not

execute

complex computation. We found that zk-SNARKs were the best tools to build secure bridges, off-chain protocols, and services that improve the privacy, scalability, and programmability of bitcoin. Later, we discovered that more people in the bitcoin community had arrived at similar conclusions, even as early as 2013 with Greg Maxwell’s ideas on

CoinWitness

when zk-SNARKs were much less practical.

In early 2022, Trey Del Bonis, who now works as a protocol engineer at Alpen Labs,

published a relatively detailed sketch

of how a zk rollup built on bitcoin would work. Trey's design used the Liquid script extension suite along with a hypothetical "OP_ZKPVERIFY" opcode to enable building a Layer 2 validity rollup on bitcoin. Toward the end of his article, Trey mentioned that "rollups could work super well for Lightning", which got our attention. We peer-reviewed Trey’s design and began exploring ways to simplify the design further with Taproot and new innovations around scaling in other blockchains.

Near the end of 2022, bitcoin rollups received a big boost in attention thanks to the publication of

Validity Rollups on Bitcoin

, a research report by John Light, who now works on product at Alpen Labs. This research report was commissioned earlier in the year by the Human Rights Foundation, StarkWare, and CMS Holdings as part of the ZK Rollup Research Fellowship. The goal of the fellowship was to answer key questions about the viability of zk rollups on bitcoin, including investigating and analyzing the features and use cases of zk rollups, how they could be built on bitcoin, and if they could be built on bitcoin, what risk/reward tradeoffs were associated with them. Our team went deep into the report, and found that we shared many of the report's conclusions.

We had started working on our own rollup design in Fall of 2022. We took liberties to imagine what the ideal zk rollup on bitcoin would look like, and worked backward from there to figure out what additional new building blocks would be needed to make it possible. This work culminated in

ZK Rollup on Bitcoin

, a whitepaper detailing the design we came up with. Simanta Gautam, one of our co-founders, presented a summary of this design in a

talk

at BTC++ in April 2023. We are excited to release the full whitepaper today to the public as free and open source research.

The “ZK Rollup on Bitcoin” whitepaper represents a snapshot of our views at a formative time in the history of Alpen Labs. Today, our work on the zk rollup design described in the whitepaper, which requires a bitcoin soft fork, is on pause in favor of a rollup design that is possible to build on bitcoin today, based on our recently published

SNARKnado

research. But the long-term vision of trustless zk rollups on bitcoin is still very much of interest to us, and we look forward to contributing where we can to help make this vision a reality.

‍

Read the "ZK Rollup on Bitcoin" whitepaper

here

.

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
