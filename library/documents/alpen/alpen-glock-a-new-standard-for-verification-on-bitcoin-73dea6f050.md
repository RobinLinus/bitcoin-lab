# Glock: A new standard for verification on Bitcoin

Source: https://www.alpen.org/blog/glock-verification-on-bitcoin

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

July 15, 2025

Glock: A new standard for verification on Bitcoin

Introducing a primitive for the safest programmable Bitcoin systems.

Over the last few months, Alpen Labs’ focus has rapidly evolved to a new frontier of minimal-trust verification on Bitcoin. Next week, we will unveil

Glock

, short for

garbled lock or

garbled circuit-based lock. Glock is a new cryptographic primitive that creates a new standard for verifying offchain computation on Bitcoin, with minimal onchain cost. Glock opens up the path that takes the safety of Bitcoin-based systems to new heights. You can now read

the Glock paper

.

We’ve been researching garbled circuits for optimistic verification on Bitcoin for over a year now, after Liam Eagen had an epiphany during a long-distance flight during his time at Alpen. But only recently did the final pieces fall into place, enabling us to transcend the primary drawbacks of BitVM’s model: the costly nature of transactions, the complexity of the overall setup, and concerns that it’s been “hacked” into Bitcoin. With Glock, we’re able to bypass all of these drawbacks and achieve up to

1000x reduction in onchain costs

in verifying offchain computation on Bitcoin.

Our company’s direction now fully orients towards Glock in the development of the Alpen ZK rollup and the Strata bridge. Join the conversation on Glock in

our new Telegram group

, where we'll also share development updates with you.

A new name for a new paradigm

Although the idea of using garbled circuits for verification has been floated already, the primitives suggested thus far are either broken or overlook key details necessary for building a 1-of-N Bitcoin bridge. BitVM3 has gained popularity as an idea, but

Liam Eagen

and

Fairgate Labs

recently reported separate core flaws in its RSA-based construction, rendering it unsafe to build upon. These vulnerabilities have created an even larger void in defining a secure and feasible garbled circuit-based lock on Bitcoin.

We are preparing to release the Glock preprint, authored by Liam Eagen, soon. Included in the paper is a construction of a garbled circuit-based lock using a novel and compact DV-SNARK (designated verifier SNARK), a key innovation that makes Glock feasible today.

Why garbled locks are so enticing

We’ve been one of the biggest contributors to both the research and the development of BitVM2. BitVM2 was able to sufficiently demonstrate the practicality of optimistic verification on Bitcoin, which is a massive achievement for Bitcoin.

But while building BitVM2, we got to the point where we squeezed nearly every ounce of performance from the design. We started hitting the bounds of what was possible within its paradigm of chunked onchain verifiers. The primary limitations we couldn’t get past were: prohibitively expensive transactions, design complexity, and large staking requirements (on the order of 5 BTC). Despite optimizing every aspect of BitVM2, these inherent limitations remained unsolvable within its design.

Then we asked: how can we make a new protocol with 1000× cheaper challenges, simple design & much smaller operator stake? Our long search for elegant optimistic verification on Bitcoin with minimal onchain cost then led us to garbled locks.

A garbled lock achieves this by moving the complexity of verifying computation fully outside Bitcoin while securely binding its integrity to Bitcoin.

This shift brings transformative benefits:

Drastically improved protocol economics

make it more accessible to both operators and challengers,

Radically reduced protocol complexity

makes the protocol more antifragile and auditable,

Freed block space

can be used for other transactions on Bitcoin, and

Low staking requirements

that are far smaller than in BitVM2.

Improving the economics of Bitcoin bridges in this way means less bridging fees and more participants securing the bridge.

Assembling a Glock

In short, the principle behind Glock is the “authenticated” conditional disclosure of secrets. One party simply “authenticates” the input to the computation, and then using cryptography another party can derive a secret if that computation fails. How Glock ties the inputs and outputs of a circuit to Bitcoin is what ultimately allows this to work for our needs. We’ll describe this technique in detail in the paper.

In our proposed construction, we use a DV-SNARK, or designated verifier SNARK. The DV-SNARK has a small proof size, which reduces onchain cost. It also has lower complexity than Groth16, which helps us keep offchain storage and computational costs down by orders of magnitude.

The orchestra that has made Glock possible

The Glock construction draws on several critical innovations:

Tying circuit inputs and outputs directly to Bitcoin lock data,

A highly efficient DV-SNARK, which reduces both proof size and complexity compared to traditional SNARKs like Groth16,

Advances in garbling techniques that meet stringent malicious security requirements.

These advances culminate in a construction where one party authenticates the computation’s input, and another can derive a secret if the computation fails, securely binding computation integrity to Bitcoin itself.

An open initiative

Bitcoin’s innovation era is in full swing. We invite you to join the conversation in

our new Telegram group

, where you can learn and contribute to this exciting new primitive on Bitcoin.

Subscribe to our newsletter to be notified when we release the Glock paper and define a new standard for minimal-trust verification on Bitcoin.

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
