# [bitcoindev] DropKick ⚽️ - A minimal commit/reveal PQ rescue protocol

Source: https://gnusha.org/pi/bitcoindev/O_i0gml6GTRro49f8c8jlCmgwOH5ZMDsJg4zxe-pX6akiGaibaFP7ilCTX90ZDfKORvmd3YlU4UUZWkwI-NPlvEtY8eVAvCFqO_ckuMG7m8=@proton.me/T/

Retrieved: 2026-08-24T21:52:29Z

---

public inbox for bitcoindev@googlegroups.com

help

/

color

/

mirror

/

Atom feed

*

[bitcoindev] DropKick ⚽️ - A minimal commit/reveal PQ rescue protocol

@ 2026-08-20 21:30 'conduition' via Bitcoin Development Mailing List

2026-08-22 17:46 `

Alex

0 siblings, 1 reply; 3+ messages in thread

From: 'conduition' via Bitcoin Development Mailing List @ 2026-08-20 21:30 UTC (

permalink

/

raw

) To: bitcoindev

[-- Attachment #1.1.1: Type: text/plain, Size: 10103 bytes --]

Dearest friends, colleagues, and lurkers, I would like to present for your consideration a new commit/reveal rescue protocol to save the coins of quantum procrastinators - those who take no action to move their coins to PQC-enabled wallets by Q-Day.

https://conduition.io/bitcoin/dropkick/

The term "DropKick" is self-descriptive of its usage: Drop a hidden commitment somewhere on the blockchain, and reveal it later with an SPV-style proof to Kick (spend) your legacy coins forward to a new PQ-secure wallet. Background As with any post-quantum commit/reveal protocol, DropKick uses the blockchain as a trustless timestamping service to prove than an honest user had earlier chronological knowledge of some secret witness to a quantum-hard one-way function. The honest user hides a commitment in a block, waits for confirmations, and later reveals her commitment to certify she knew the secret witness long before an adversary (like a quantum computer) could have done so. Assuming this witness was indeed kept secret prior to reveal time, it is already too late for the adversary to forge an equivalent proof. This general mechanism also allows validators to distinguish an honest bitcoin-holding procrastinator from a CRQC in many situations, and so procrastinators can still authorize spending of their legacy UTXOs even well after Q-day, provided the rescue protocol is deployed before Q-day as a new encumbrance on affected legacy coins. DropKick In One Paragraph DropKick specifically is a commit/reveal protocol where the commitment `H(H(w, Q), Q)` is hidden somewhere in a block, such as an OP_RETURN or inside a taproot tweak. `Q` is a post-quantum public key, and `w` is the witness to a one-way function `f`, such that `s = f(x)` is the script pubkey (address) encumbering a coin. We can later reveal the witness `w` and a signature from pubkey `Q` to authorize a spend, along with an opening proof showing that the commitment was included in a prior block. The verifier checks the commitment opening is valid and sufficiently old, checks `s = f(x)`, and verifies the PQ-signature from `Q`. See this section for the actual proving/verifying steps of the protocol. Features Generality: DropKick generalizes to any efficient [1] one-way function based on knowledge asymmetries - things the honest user knows which the adversary doesn't. In the context of Bitcoin, the one-way function would typically be a computational pipeline that includes hashing of secret data unknown to a CRQC, such as "BIP32 hardened derivation of an address" or "hashing a public key or script to build an address" or "taproot key tweaking". DropKick can be instantiated with different one-way functions to encumber different coins. Compatibility: DropKick can be deployed as a soft-fork, as it only tightens spending validation rules, and does so only on certain UTXOs. Confiscation: DropKick can be deployed without confiscating any coins, if so desired, by deploying it as an encumbrance only on UTXOs with decidable knowledge asymmetries like hashed addresses (see this section). If one wishes to maximize the number of legacy coins rescued, DropKick can also be deployed on undecidable knowledge asymmetries like BIP32-CKD. To be clear, P2PK coins cannot be covered by DropKick or indeed by any rescue protocol, as these UTXOs have no known knowledge asymmetries when a CRQC is in play. Blockspace Efficiency: DropKick has near zero on-chain impact until reveal time, at which point the commitment opening proofs are included in a reveal transaction spending the legacy coins. Opening proofs could be attached in an OP_RETURN for backwards compatibility, or for better efficiency the proofs could be attached in a new transaction witness field which would allow for the 4x segwit discount to apply. DropKick opening proofs are approximately the same size as SPV or OpenTimestamps proofs (less than a kilobyte) and those proofs can be reused to rescue multiple related UTXOs, e.g. coins on the same address, or coins on addresses derived from the same seed. Performance: DropKick opening proofs cost very little to verify: a few hash invocations, about as fast to verify as an SPV proof or lamport signature of the same size, and the cost of verification scales linearly with the size of the proof. If one has `txindex=1` enabled, verification is even faster. The only prerequisite data needed to verify the opening proof is the set of all Bitcoin block headers. Verifying the revealed witness `w` is exactly as efficient as evaluating the one-way function `f(w)`. Ergonomics: Procrastinator do not need to have their own PQ-safe UTXOs available to execute a DropKick rescue: Users can delegate their commitments to untrusted third party servers called "aggregators" who do have PQ-safe UTXOs. These servers take it upon themselves to aggregate the commitments of other users together into a merkle tree, whose root they publish on-chain. Those aggregators can charge a salvage fee for their services if desired, paid in-band from the rescued UTXOs, or up-front out-of-band. Procrastinators can shop between different aggregators, and anyone with PQ-safe UTXOs can operate one. Comparison to Lifeboat DropKick competes directly with Tadge Dryja's Lifeboat/Lifejacket proposal (also see this older post), but DropKick aims for a different (lower) degree of security in exchange for a simpler implementation surface, more flexibility, and better efficiency. The two protocols fulfill functionally similar roles, so I will take a moment to compare and contrast DropKick and Lifeboat/Lifejacket. DropKick includes some novel features which Lifeboat does not, such as key certification (allowing things like RBF, or equivocation, by the honest spender), or generalization to arbitrary one-way functions. Such developments could be easily transferred to Lifeboat as well, so I will mostly ignore these minor differences here. The fundamental difference between DropKick and Lifeboat is the commitment ordering requirement. - Lifeboat requires procrastinators to (1) procure a PQ-secure UTXO, and (2) upload a ~96-byte commitment in-the-clear in a new transaction, such as in an OP_RETURN or inscription. Validators must index all such commitments, so that they can chronologically order the revealed commitments later. Reveals reference this index to authorize spending: Only the earliest valid commitment for a given witness is allowed to spend the legacy coin that witness unlocks. - DropKick encourages procrastinators to hide commitments in merkle trees committed into blocks, such as via a merkle root posted in an OP_RETURN, or in a taproot-style key tweak. Reveals use SPV-style proofs to convince validators that the commitment was included in a past block. Validators therefore do not (and cannot) index all commitments, and so there is no way to confirm any one commitment was earliest. By dropping the commitment ordering requirement, DropKick skips the need for a new index database collecting all the commitments, and this frees us from putting commitments on chain in-the-clear. DropKick commitments can be hidden off-chain, but anchored to the chain in merkle trees of arbitrary size, which is the key feature that enables the new role of aggregators, and means procrastinators don't need PQ-UTXOs to publish a commitment and rescue their legacy coins. To gain these benefits, DropKick sacrifices some security, by admitting miner censorship attacks where miners can intentionally censor a reveal transaction to gain a chance to steal the procrastinator's coins. Lifeboat entirely avoids this class of attacks, whereas DropKick requires a somewhat loose game-theoretical argument that miners will converge on choosing not to censor reveals, provided we enforce a long delay (days or weeks) between commitment and reveal steps, and provided the procrastinator pays a proportional fee to incentivize honest miners. We also have to assume no 51% reorg attacks of course, as a malicious hashrate majority could easily censor any reveal transactions and so steal coins. However, if this security loss is acceptable, DropKick offers a much simpler and less complex engineering surface area, and supports rescuing users in more diverse situations than LifeBoat can (because PQ UTXOs are mandatory in Lifeboat). LifeBoat's UX advantage over DropKick is that because of the ordering, there is no long delay or value-proportional fee needed: Users only need to wait a few blocks between commit and reveal stages, and they pay only regular mining fees as usual. DropKick OTOH requires a delay proportional to the fraction of the UTXO one is willing to sacrifice to miners. E.g. if we assume users are willing to sacrifice 1% of their UTXOs, then we need to enforce a reveal delay period of at least 100 blocks. See here for a derivation of these parameters. Conclusion So that's it. I'm submitting DropKick here as a sketch for consideration, not as a concrete proposal. I am most interested to know if anyone can think of a better mechanism to avoid miner censorship attacks, or if we can at least reduce the strength of the assumptions needed for DropKick to resist them. regards, conduition [1]: The one-way function must be efficient so that verifiers can recompute it to validate reveal transactions without DoS risks. For example, BIP32 master key derivation via BIP39 is not considered efficient because it uses PBKDF2, whereas BIP32 CKD is efficient if restricted to a maximum derivation depth. -- You received this message because you are subscribed to the Google Groups "Bitcoin Development Mailing List" group. To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups•com. To view this discussion visit

https://groups.google.com/d/msgid/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo%3D%40proton.me

.

[-- Attachment #1.1.2.1: Type: text/html, Size: 18262 bytes --]

[-- Attachment #1.2: publickey - conduition@proton.me - 0x474891AD.asc --] [-- Type: application/pgp-keys, Size: 649 bytes --]

[-- Attachment #2: OpenPGP digital signature --] [-- Type: application/pgp-signature, Size: 343 bytes --]

^

permalink

raw

reply

[

flat

|

nested

]

3+ messages in thread

*

Re: [bitcoindev] DropKick ⚽️ - A minimal commit/reveal PQ rescue protocol

2026-08-20 21:30

[bitcoindev] DropKick ⚽️ - A minimal commit/reveal PQ rescue protocol

'conduition' via Bitcoin Development Mailing List

@ 2026-08-22 17:46 ` Alex

2026-08-23 23:28 `

'conduition' via Bitcoin Development Mailing List

0 siblings, 1 reply; 3+ messages in thread

From: Alex @ 2026-08-22 17:46 UTC (

permalink

/

raw

) To: conduition;

+Cc:

bitcoindev

[-- Attachment #1: Type: text/plain, Size: 12271 bytes --]

Am I correct in understanding that commit/reveal always depends on someone else already having a valid PQC UTXO to spend? So in other words, this can never be a solution for a (procrastinating Bitcoin system), only a solution for (procrastinating Bitcoin users). We need to have an already functioning PQC solution for Bitcoin itself, deployed, before any of commit/reveal can help, right? Den tors 20 aug. 2026 23:56'conduition' via Bitcoin Development Mailing List <bitcoindev@googlegroups.com> skrev:

> Dearest friends, colleagues, and lurkers, > > I would like to present for your consideration a new commit/reveal rescue > protocol to save the coins of quantum procrastinators - those who take no > action to move their coins to PQC-enabled wallets by Q-Day. > >

https://conduition.io/bitcoin/dropkick/

> > The term "DropKick" is self-descriptive of its usage: *Drop* a hidden > commitment somewhere on the blockchain, and reveal it later with an > SPV-style proof to *Kick* (spend) your legacy coins forward to a new > PQ-secure wallet. > > Background > > As with any post-quantum commit/reveal protocol, DropKick uses the > blockchain as a trustless timestamping service to prove than an honest user > had earlier chronological knowledge of some secret *witness* to a > quantum-hard* one-way function*. The honest user hides a *commitment* in > a block, waits for confirmations, and later *reveals* her commitment to > certify she knew the secret witness long before an adversary (like a > quantum computer) could have done so. Assuming this witness was indeed kept > secret prior to reveal time, it is already too late for the adversary to > forge an equivalent proof. > > > This general mechanism also allows validators to distinguish an honest > bitcoin-holding procrastinator from a CRQC in many situations, and so > procrastinators can still authorize spending of their legacy UTXOs even > well after Q-day, provided the rescue protocol is deployed *before* Q-day > as a new encumbrance on affected legacy coins. > > DropKick In One Paragraph > > DropKick specifically is a commit/reveal protocol where the commitment H(H(w, > Q), Q)​ is hidden somewhere in a block, such as an OP_RETURN or inside a > taproot tweak. Q​ is a post-quantum public key, and w​ is the witness to > a one-way function f​, such that s = f(x)​ is the script pubkey (address) > encumbering a coin. We can later reveal the witness w​ and a signature > from pubkey Q​ to authorize a spend, along with an *opening proof* showing > that the commitment was included in a prior block. The verifier checks the > commitment opening is valid and sufficiently old, checks s = f(x)​, and > verifies the PQ-signature from Q​. > > See this section for the actual proving/verifying steps of the protocol. > <

https://conduition.io/bitcoin/dropkick/#DropKick

> > > Features > > *Generality:* DropKick generalizes to any *efficient *[1] one-way > function based on knowledge asymmetries - things the honest user knows > which the adversary doesn't. In the context of Bitcoin, the one-way > function would typically be a computational pipeline that includes hashing > of secret data unknown to a CRQC, such as "BIP32 hardened derivation of an > address" or "hashing a public key or script to build an address" or > "taproot key tweaking". DropKick can be instantiated with different one-way > functions to encumber different coins. > > *Compatibility:* DropKick can be deployed as a soft-fork, as it only > *tightens* spending validation rules, and does so only on certain UTXOs. > > *Confiscation:* DropKick can be deployed *without* confiscating any > coins, if so desired, by deploying it as an encumbrance only on UTXOs with > *decidable* knowledge asymmetries like hashed addresses (see this section > <

https://conduition.io/bitcoin/dropkick/#Knowledge-Asymmetries

>). If one > wishes to maximize the number of legacy coins rescued, DropKick can also be > deployed on *undecidable* knowledge asymmetries like BIP32-CKD. To be > clear, P2PK coins cannot be covered by DropKick or indeed by any rescue > protocol, as these UTXOs have no known knowledge asymmetries when a CRQC is > in play. > > *Blockspace Efficiency:* DropKick has near zero on-chain impact until > reveal time, at which point the commitment opening proofs are included in a *reveal > transaction* spending the legacy coins. Opening proofs could be attached > in an OP_RETURN for backwards compatibility, or for better efficiency the > proofs could be attached in a new transaction witness field which would > allow for the 4x segwit discount to apply. DropKick opening proofs are > approximately the same size as SPV > <

https://learnmeabitcoin.com/technical/networking/node/#lightweight-node

> > or OpenTimestamps <

https://opentimestamps.org/

> proofs (less than a > kilobyte) and those proofs can be reused to rescue multiple related UTXOs, > e.g. coins on the same address, or coins on addresses derived from the same > seed. > > *Performance:* DropKick opening proofs cost very little to verify: a few > hash invocations, about as fast to verify as an SPV proof or lamport > signature of the same size, and the cost of verification scales linearly > with the size of the proof. If one has txindex=1​ enabled, verification > is even faster. The only prerequisite data needed to verify the opening > proof is the set of all Bitcoin block headers. Verifying the revealed > witness w​ is exactly as efficient as evaluating the one-way function f(w) > ​. > > *Ergonomics: *Procrastinator *do not* need to have their own PQ-safe > UTXOs available to execute a DropKick rescue: Users can delegate their > commitments to untrusted third party servers called "aggregators" who *do* have > PQ-safe UTXOs. These servers take it upon themselves to aggregate the > commitments of other users together into a merkle tree, whose root they > publish on-chain. Those aggregators can charge a salvage fee for their > services if desired, paid in-band from the rescued UTXOs, or up-front out-of-band. Procrastinators > can shop between different aggregators, and anyone with PQ-safe UTXOs can > operate one. > > Comparison to Lifeboat > > DropKick competes directly with Tadge Dryja's Lifeboat/Lifejacket proposal > <

https://www.youtube.com/watch?v=PmW90HX89P8

> (also see this older post > <

https://groups.google.com/g/bitcoindev/c/LpWOcXMcvk8/

>), but DropKick > aims for a different (lower) degree of security in exchange for a simpler > implementation surface, more flexibility, and better efficiency. > > The two protocols fulfill functionally similar roles, so I will take a > moment to compare and contrast DropKick and Lifeboat/Lifejacket. > > DropKick includes some novel features which Lifeboat does not, such as *key > certification *(allowing things like RBF, or equivocation, by the honest > spender), or generalization to arbitrary one-way functions. Such > developments could be easily transferred to Lifeboat as well, so I will > mostly ignore these minor differences here. > > The fundamental difference between DropKick and Lifeboat is the commitment > ordering requirement. > > > - Lifeboat requires procrastinators to (1) procure a PQ-secure UTXO, > and (2) upload a ~96-byte commitment in-the-clear in a new transaction, > such as in an OP_RETURN or inscription. Validators must index all such > commitments, so that they can *chronologically order* the revealed > commitments later. Reveals reference this index to authorize spending: Only > the earliest valid commitment for a given witness is allowed to spend > the legacy coin that witness unlocks. > - DropKick encourages procrastinators to *hide* commitments in merkle > trees committed into blocks, such as via a merkle root posted in an > OP_RETURN, or in a taproot-style key tweak. Reveals use SPV-style proofs to > convince validators that the commitment was included in a past block. *Validators > therefore do not (and cannot) index all commitments, and so there is no way > to confirm any one commitment was earliest*. > > > By dropping the commitment ordering requirement, DropKick skips the need > for a new index database collecting all the commitments, and this frees us > from putting commitments on chain in-the-clear. DropKick commitments can be > hidden off-chain, but anchored to the chain in merkle trees of arbitrary > size, which is the key feature that enables the new role of aggregators, > and means procrastinators don't need PQ-UTXOs to publish a commitment and > rescue their legacy coins. > > To gain these benefits, DropKick sacrifices some security, by admitting miner > censorship attacks <

https://conduition.io/bitcoin/dropkick/#Censorship

> where > miners can intentionally censor a reveal transaction to gain a chance to > steal the procrastinator's coins. Lifeboat entirely avoids this class of > attacks, whereas DropKick requires a somewhat loose game-theoretical > argument <

https://conduition.io/bitcoin/dropkick/#Appendix-Game-Theory

> > that miners will converge on choosing *not* to censor reveals, provided > we enforce a long delay (days or weeks) between commitment and reveal > steps, and provided the procrastinator pays a proportional fee to > incentivize honest miners. We also have to assume no 51% reorg attacks of > course, as a malicious hashrate majority could easily censor any reveal > transactions and so steal coins. > > However, if this security loss is acceptable, DropKick offers a much > simpler and less complex engineering surface area, and supports rescuing > users in more diverse situations than LifeBoat can (because PQ UTXOs are > mandatory in Lifeboat). > > LifeBoat's UX advantage over DropKick is that because of the ordering, > there is no long delay or value-proportional fee needed: Users only need to > wait a few blocks between *commit* and *reveal* stages, and they pay only > regular mining fees as usual. DropKick OTOH requires a delay proportional > to the fraction of the UTXO one is willing to sacrifice to miners. E.g. if > we assume users are willing to sacrifice 1% of their UTXOs, then we need to > enforce a reveal delay period of at least 100 blocks. See here for a > derivation of these parameters > <

https://conduition.io/bitcoin/dropkick/#Parameters

>. > > Conclusion > > So that's it. > > I'm submitting DropKick here as a sketch for consideration, not as a > concrete proposal. I am most interested to know if anyone can think of a > better mechanism to avoid miner censorship attacks, or if we can at least > reduce the strength of the assumptions needed for DropKick to resist them. > > regards, > conduition > > > [1]: The one-way function must be *efficient* so that verifiers can > recompute it to validate reveal transactions without DoS risks. For > example, BIP32 master key derivation via BIP39 is not considered efficient > because it uses PBKDF2, whereas BIP32 CKD is efficient if restricted to a > maximum derivation depth. > > -- > You received this message because you are subscribed to the Google Groups > "Bitcoin Development Mailing List" group. > To unsubscribe from this group and stop receiving emails from it, send an > email to bitcoindev+unsubscribe@googlegroups•com. > To view this discussion visit >

https://groups.google.com/d/msgid/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo%3D%40proton.me

> <

https://groups.google.com/d/msgid/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo%3D%40proton.me?utm_medium=email&utm_source=footer

> > . >

-- You received this message because you are subscribed to the Google Groups "Bitcoin Development Mailing List" group. To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups•com. To view this discussion visit

https://groups.google.com/d/msgid/bitcoindev/CAHPaHkr5r4%2BhodZv6F2S1yCq_UcHSr2iCrkYLgZ_vryNgwbRPA%40mail.gmail.com

.

[-- Attachment #2: Type: text/html, Size: 18995 bytes --]

^

permalink

raw

reply

[

flat

|

nested

]

3+ messages in thread

*

Re: [bitcoindev] DropKick ⚽️ - A minimal commit/reveal PQ rescue protocol

2026-08-22 17:46 `

Alex

@ 2026-08-23 23:28 ` 'conduition' via Bitcoin Development Mailing List

0 siblings, 0 replies; 3+ messages in thread

From: 'conduition' via Bitcoin Development Mailing List @ 2026-08-23 23:28 UTC (

permalink

/

raw

) To: Alex;

+Cc:

bitcoindev

[-- Attachment #1.1.1: Type: text/plain, Size: 12131 bytes --]

Hi Alex,

> We need to have an already functioning PQC solution for Bitcoin itself, deployed, before any of commit/reveal can help, right?

Yes. Two reasons: First, without on-chain PQC, making commitments would be impossible to do safely unless commitment are aggregated directly by miners into the coinbase transaction. Second, without on-chain PQ-secure addresses, where would one even rescue coins to? Commit/reveal protocols are meant as a tool saving coins in an emergency, not for everyday spending. PQ signature schemes are therefore needed as a prerequisite. regards, conduition On Saturday, August 22nd, 2026 at 1:46 PM, Alex <alexhultman@gmail•com> wrote:

> Am I correct in understanding that commit/reveal always depends on someone else already having a valid PQC UTXO to spend? > So in other words, this can never be a solution for a (procrastinating Bitcoin system), only a solution for (procrastinating Bitcoin users). >

> We need to have an already functioning PQC solution for Bitcoin itself, deployed, before any of commit/reveal can help, right? >

> Den tors 20 aug. 2026 23:56'conduition' via Bitcoin Development Mailing List <bitcoindev@googlegroups.com> skrev: >

> > Dearest friends, colleagues, and lurkers, > >

> > I would like to present for your consideration a new commit/reveal rescue protocol to save the coins of quantum procrastinators - those who take no action to move their coins to PQC-enabled wallets by Q-Day. > >

> >

https://conduition.io/bitcoin/dropkick/

> >

> > The term "DropKick" is self-descriptive of its usage: Drop a hidden commitment somewhere on the blockchain, and reveal it later with an SPV-style proof to Kick (spend) your legacy coins forward to a new PQ-secure wallet. > >

> > Background > >

> > As with any post-quantum commit/reveal protocol, DropKick uses the blockchain as a trustless timestamping service to prove than an honest user had earlier chronological knowledge of some secret witness to a quantum-hard one-way function. The honest user hides a commitment in a block, waits for confirmations, and later reveals her commitment to certify she knew the secret witness long before an adversary (like a quantum computer) could have done so. Assuming this witness was indeed kept secret prior to reveal time, it is already too late for the adversary to forge an equivalent proof. > >

> >

> > This general mechanism also allows validators to distinguish an honest bitcoin-holding procrastinator from a CRQC in many situations, and so procrastinators can still authorize spending of their legacy UTXOs even well after Q-day, provided the rescue protocol is deployed before Q-day as a new encumbrance on affected legacy coins. > > DropKick In One Paragraph > >

> > DropKick specifically is a commit/reveal protocol where the commitment `H(H(w, Q), Q)` is hidden somewhere in a block, such as an OP_RETURN or inside a taproot tweak. `Q` is a post-quantum public key, and `w` is the witness to a one-way function `f`, such that `s = f(x)` is the script pubkey (address) encumbering a coin. We can later reveal the witness `w` and a signature from pubkey `Q` to authorize a spend, along with an opening proof showing that the commitment was included in a prior block. The verifier checks the commitment opening is valid and sufficiently old, checks `s = f(x)`, and verifies the PQ-signature from `Q`. > >

> > See this section for the actual proving/verifying steps of the protocol. > >

> > Features > >

> >

> > Generality: DropKick generalizes to any efficient [1] one-way function based on knowledge asymmetries - things the honest user knows which the adversary doesn't. In the context of Bitcoin, the one-way function would typically be a computational pipeline that includes hashing of secret data unknown to a CRQC, such as "BIP32 hardened derivation of an address" or "hashing a public key or script to build an address" or "taproot key tweaking". DropKick can be instantiated with different one-way functions to encumber different coins. > >

> >

> > Compatibility: DropKick can be deployed as a soft-fork, as it only tightens spending validation rules, and does so only on certain UTXOs. > >

> > Confiscation: DropKick can be deployed without confiscating any coins, if so desired, by deploying it as an encumbrance only on UTXOs with decidable knowledge asymmetries like hashed addresses (see this section). If one wishes to maximize the number of legacy coins rescued, DropKick can also be deployed on undecidable knowledge asymmetries like BIP32-CKD. To be clear, P2PK coins cannot be covered by DropKick or indeed by any rescue protocol, as these UTXOs have no known knowledge asymmetries when a CRQC is in play. > >

> > Blockspace Efficiency: DropKick has near zero on-chain impact until reveal time, at which point the commitment opening proofs are included in a reveal transaction spending the legacy coins. Opening proofs could be attached in an OP_RETURN for backwards compatibility, or for better efficiency the proofs could be attached in a new transaction witness field which would allow for the 4x segwit discount to apply. DropKick opening proofs are approximately the same size as SPV or OpenTimestamps proofs (less than a kilobyte) and those proofs can be reused to rescue multiple related UTXOs, e.g. coins on the same address, or coins on addresses derived from the same seed. > >

> > Performance: DropKick opening proofs cost very little to verify: a few hash invocations, about as fast to verify as an SPV proof or lamport signature of the same size, and the cost of verification scales linearly with the size of the proof. If one has `txindex=1` enabled, verification is even faster. The only prerequisite data needed to verify the opening proof is the set of all Bitcoin block headers. Verifying the revealed witness `w` is exactly as efficient as evaluating the one-way function `f(w)`. > >

> >

> > Ergonomics: Procrastinator do not need to have their own PQ-safe UTXOs available to execute a DropKick rescue: Users can delegate their commitments to untrusted third party servers called "aggregators" who do have PQ-safe UTXOs. These servers take it upon themselves to aggregate the commitments of other users together into a merkle tree, whose root they publish on-chain. Those aggregators can charge a salvage fee for their services if desired, paid in-band from the rescued UTXOs, or up-front out-of-band. Procrastinators can shop between different aggregators, and anyone with PQ-safe UTXOs can operate one. > >

> > Comparison to Lifeboat > >

> > DropKick competes directly with Tadge Dryja's Lifeboat/Lifejacket proposal (also see this older post), but DropKick aims for a different (lower) degree of security in exchange for a simpler implementation surface, more flexibility, and better efficiency. > >

> > The two protocols fulfill functionally similar roles, so I will take a moment to compare and contrast DropKick and Lifeboat/Lifejacket. > >

> > DropKick includes some novel features which Lifeboat does not, such as key certification (allowing things like RBF, or equivocation, by the honest spender), or generalization to arbitrary one-way functions. Such developments could be easily transferred to Lifeboat as well, so I will mostly ignore these minor differences here. > >

> > The fundamental difference between DropKick and Lifeboat is the commitment ordering requirement. > >

> >

> > - Lifeboat requires procrastinators to (1) procure a PQ-secure UTXO, and (2) upload a ~96-byte commitment in-the-clear in a new transaction, such as in an OP_RETURN or inscription. Validators must index all such commitments, so that they can chronologically order the revealed commitments later. Reveals reference this index to authorize spending: Only the earliest valid commitment for a given witness is allowed to spend the legacy coin that witness unlocks. > >

> > - DropKick encourages procrastinators to hide commitments in merkle trees committed into blocks, such as via a merkle root posted in an OP_RETURN, or in a taproot-style key tweak. Reveals use SPV-style proofs to convince validators that the commitment was included in a past block. Validators therefore do not (and cannot) index all commitments, and so there is no way to confirm any one commitment was earliest. > >

> >

> >

> > By dropping the commitment ordering requirement, DropKick skips the need for a new index database collecting all the commitments, and this frees us from putting commitments on chain in-the-clear. DropKick commitments can be hidden off-chain, but anchored to the chain in merkle trees of arbitrary size, which is the key feature that enables the new role of aggregators, and means procrastinators don't need PQ-UTXOs to publish a commitment and rescue their legacy coins. > >

> > To gain these benefits, DropKick sacrifices some security, by admitting miner censorship attacks where miners can intentionally censor a reveal transaction to gain a chance to steal the procrastinator's coins. Lifeboat entirely avoids this class of attacks, whereas DropKick requires a somewhat loose game-theoretical argument that miners will converge on choosing not to censor reveals, provided we enforce a long delay (days or weeks) between commitment and reveal steps, and provided the procrastinator pays a proportional fee to incentivize honest miners. We also have to assume no 51% reorg attacks of course, as a malicious hashrate majority could easily censor any reveal transactions and so steal coins. > >

> > However, if this security loss is acceptable, DropKick offers a much simpler and less complex engineering surface area, and supports rescuing users in more diverse situations than LifeBoat can (because PQ UTXOs are mandatory in Lifeboat). > >

> > LifeBoat's UX advantage over DropKick is that because of the ordering, there is no long delay or value-proportional fee needed: Users only need to wait a few blocks between commit and reveal stages, and they pay only regular mining fees as usual. DropKick OTOH requires a delay proportional to the fraction of the UTXO one is willing to sacrifice to miners. E.g. if we assume users are willing to sacrifice 1% of their UTXOs, then we need to enforce a reveal delay period of at least 100 blocks. See here for a derivation of these parameters. > >

> > Conclusion > >

> > So that's it. > >

> > I'm submitting DropKick here as a sketch for consideration, not as a concrete proposal. I am most interested to know if anyone can think of a better mechanism to avoid miner censorship attacks, or if we can at least reduce the strength of the assumptions needed for DropKick to resist them. > >

> > regards, > > conduition > >

> >

> > [1]: The one-way function must be efficient so that verifiers can recompute it to validate reveal transactions without DoS risks. For example, BIP32 master key derivation via BIP39 is not considered efficient because it uses PBKDF2, whereas BIP32 CKD is efficient if restricted to a maximum derivation depth. > >

> > -- > > You received this message because you are subscribed to the Google Groups "Bitcoin Development Mailing List" group. > > To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups•com. > > To view this discussion visit

https://groups.google.com/d/msgid/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo%3D%40proton.me

.

-- You received this message because you are subscribed to the Google Groups "Bitcoin Development Mailing List" group. To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups•com. To view this discussion visit

https://groups.google.com/d/msgid/bitcoindev/O_i0gml6GTRro49f8c8jlCmgwOH5ZMDsJg4zxe-pX6akiGaibaFP7ilCTX90ZDfKORvmd3YlU4UUZWkwI-NPlvEtY8eVAvCFqO_ckuMG7m8%3D%40proton.me

.

[-- Attachment #1.1.2.1: Type: text/html, Size: 21428 bytes --]

[-- Attachment #1.2: publickey - conduition@proton.me - 0x474891AD.asc --] [-- Type: application/pgp-keys, Size: 649 bytes --]

[-- Attachment #2: OpenPGP digital signature --] [-- Type: application/pgp-signature, Size: 343 bytes --]

^

permalink

raw

reply

[

flat

|

nested

]

3+ messages in thread

end of thread, other threads:[

~2026-08-23 23:58 UTC

|

newest

]

Thread overview:

3+ messages (download:

mbox.gz

/ follow:

Atom feed

) -- links below jump to the message on this page -- 2026-08-20 21:30

[bitcoindev] DropKick ⚽️ - A minimal commit/reveal PQ rescue protocol

'conduition' via Bitcoin Development Mailing List 2026-08-22 17:46 `

Alex

2026-08-23 23:28 `

'conduition' via Bitcoin Development Mailing List

This is a public inbox, see

mirroring instructions

for how to clone and mirror all data and code used for this inbox
