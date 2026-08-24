# new.atom

Source: https://gnusha.org/pi/bitcoindev/new.atom

Retrieved: 2026-08-24T21:52:29Z

---

<?xml version="1.0" encoding="us-ascii"?>
<feed
xmlns="http://www.w3.org/2005/Atom"
xmlns:thr="http://purl.org/syndication/thread/1.0"><title>public inbox for bitcoindev@googlegroups.com</title><link
rel="alternate"
type="text/html"
href="https://gnusha.org/pi/bitcoindev/"/><link
rel="self"
href="https://gnusha.org/pi/bitcoindev/new.atom"/><id>mailto:bitcoindev@googlegroups.com</id><updated>2026-08-24T13:19:55Z</updated><entry><author><name>blocktraveler</name><email>ueberspannung@gmail.com</email></author><title>Re: [bitcoindev] Add importprivkeys RPC</title><updated>2026-08-24T13:19:55Z</updated><link
href="https://gnusha.org/pi/bitcoindev/7051ea50-7b27-4540-a82f-527be9707f2dn@googlegroups.com/"/><id>urn:uuid:01eaab74-a726-f8c0-0120-39fa1cb92fc9</id><thr:in-reply-to
ref="urn:uuid:ea7fa363-93d5-440b-0f75-de8a1930655b"
href="https://gnusha.org/pi/bitcoindev/370fcce3-843d-4bcd-ac32-a6b157f7dc59n@googlegroups.com/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/7051ea50-7b27-4540-a82f-527be9707f2dn@googlegroups.com/1.1-a.txt">[-- Attachment #1.1: Type: text/plain, Size: 3996 bytes --]</a>



&#8505;&#65039; Meanwhile, I changed the Core Wallet Migration Tools 
&lt;<a
href="https://github.com/namecoin-dev/Core-Wallet-Migration-Tools">https://github.com/namecoin-dev/Core-Wallet-Migration-Tools</a>&gt; to 
combo-import for more address type support (according to my original Proposal: 
Add importprivkeys RPC 
&lt;<a
href="https://gist.github.com/blocktraveler/3e6198c698a272bd8b13b16e0f13d390">https://gist.github.com/blocktraveler/3e6198c698a272bd8b13b16e0f13d390</a>&gt;).

Furthermore, I released the Core Wallet Maintenance Tools 
&lt;<a
href="https://github.com/namecoin-dev/Core-Wallet-Maintenance-Tools/tree/main/Bitcoin">https://github.com/namecoin-dev/Core-Wallet-Maintenance-Tools/tree/main/Bitcoin</a>&gt;, 
including a script for extracting private keys from descriptors. Created it 
for Namecoin a while ago, but published it now on request 
&lt;<a
href="https://github.com/namecoin-dev/Core-Wallet-Migration-Tools/issues/2">https://github.com/namecoin-dev/Core-Wallet-Migration-Tools/issues/2</a>&gt; for 
both, Bitcoin and Namecoin.

Regards,
Uwe



blocktraveler schrieb am Donnerstag, 23. Oktober 2025 um 04:00:02 UTC+2:

<span
class="q">&gt;
&gt; Hy and thx for the feedback, much appreciated!
&gt;
&gt; * Regarding return scheme: Sure, redundant or competing returns should be 
&gt; unified. The question is, at which point the &#39;importprivkeys&#39; call could 
&gt; just proxy or complement the return of the &#39;importdescriptors&#39; routine.
&gt;
&gt; * Regarding checksum flag: Good point as well. Adding an &#39;auto_checksum&#39; 
&gt; boolean to &#39;importdescriptors&#39; would simplify things. Not sure if this has 
&gt; been discussed before or in case, what was the reason for not implementing 
&gt; it.
&gt;
&gt; Happy to address this in the proposal or the PR.
&gt;
&gt; Best regards,
&gt; Uwe
&gt;
&gt;
&gt;
&gt; Email para newsletters schrieb am Mittwoch, 22. Oktober 2025 um 00:28:32 
&gt; UTC+2:
&gt;
&gt;&gt; IMO thats a very good proposal and should be really easy to implement.
&gt;&gt;
&gt;&gt; Allow me to share some points.
&gt;&gt;
&gt;&gt; * The return scheme somewhat extends the one from the already existing 
&gt;&gt; `importdescriptors`. This can be considered a corner to cut if theres 
&gt;&gt; implementation burn.
&gt;&gt;
&gt;&gt; * I do not have any idea about others opinion but I consider a flaw to 
&gt;&gt; not have a checksum induction flag in `importdescriptors`, which could 
&gt;&gt; reduce `importprivkeys` command dependency as well extending them both.
&gt;&gt;
&gt;&gt; Best,
&gt;&gt; Joao Leal
&gt;&gt;
&gt;&gt; Em sexta-feira, 3 de outubro de 2025 &#224;s 05:58, blocktraveler &lt;
&gt;&gt; uebers...@gmail&#8226;com&gt; escreveu:
&gt;&gt;
&gt;&gt;
&gt;&gt; Hy there!
&gt;&gt;
&gt;&gt; Unfortunately, the PRs are locked, so I&#39;m sharing my thoughts this way.
&gt;&gt;
&gt;&gt; Over the years, people have asked countless times on various platforms 
&gt;&gt; how to import private keys (both legacy and Bech32/SegWit) into a Bitcoin 
&gt;&gt; Core descriptor wallet. This issue is especially common in Namecoin. I see 
&gt;&gt; no reason why importing private keys, a very basic feature, should be 
&gt;&gt; restricted to the point that it&#39;s impossible for the average user to 
&gt;&gt; succeed. That&#39;s why I created the Core-Wallet-Migration-Tools 
&gt;&gt; &lt;<a
href="https://github.com/blocktraveler/Core-Wallet-Migration-Tools">https://github.com/blocktraveler/Core-Wallet-Migration-Tools</a>&gt; in Python.
&gt;&gt;
&gt;&gt; However, it would be much easier to have an &#39;importprivkeys&#39; RPC for 
&gt;&gt; descriptor wallets (not to be confused with the legacy &#39;importprivkey&#39; 
&gt;&gt; call). Pls check my initial thoughts:
&gt;&gt;
&gt;&gt; Proposal: Add importprivkeys RPC (helper for WIF &#8594; descriptor import) 
&gt;&gt; &lt;<a
href="https://gist.github.com/blocktraveler/3e6198c698a272bd8b13b16e0f13d390">https://gist.github.com/blocktraveler/3e6198c698a272bd8b13b16e0f13d390</a>&gt;
&gt;&gt;
&gt;&gt; Thx!
&gt;&gt; Uwe
&gt;&gt;
&gt;&gt;
&gt;&gt; -- 
&gt;&gt; You received this message because you are subscribed to the Google Groups 
&gt;&gt; &#34;Bitcoin Development Mailing List&#34; group.
&gt;&gt; To unsubscribe from this group and stop receiving emails from it, send an 
&gt;&gt; email to bitcoindev+...@googlegroups&#8226;com.
&gt;&gt; To view this discussion visit 
&gt;&gt; <a
href="https://groups.google.com/d/msgid/bitcoindev/ad14b140-9e02-466c-8226-304ec651f4ben%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/ad14b140-9e02-466c-8226-304ec651f4ben%40googlegroups.com</a>
&gt;&gt; .
&gt;&gt;
&gt;&gt;
&gt;&gt;
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/7051ea50-7b27-4540-a82f-527be9707f2dn%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/7051ea50-7b27-4540-a82f-527be9707f2dn%40googlegroups.com</a>.

<a
href="https://gnusha.org/pi/bitcoindev/7051ea50-7b27-4540-a82f-527be9707f2dn@googlegroups.com/1.2-a.bin">[-- Attachment #1.2: Type: text/html, Size: 6225 bytes --]</a>
</pre></div></content></entry><entry><author><name>&#39;conduition&#39; via Bitcoin Development Mailing List</name><email>bitcoindev@googlegroups.com</email></author><title
type="html">Re: [bitcoindev] DropKick &#9917;&#65039; - A minimal commit/reveal PQ rescue protocol</title><updated>2026-08-23T23:58:09Z</updated><link
href="https://gnusha.org/pi/bitcoindev/O_i0gml6GTRro49f8c8jlCmgwOH5ZMDsJg4zxe-pX6akiGaibaFP7ilCTX90ZDfKORvmd3YlU4UUZWkwI-NPlvEtY8eVAvCFqO_ckuMG7m8=@proton.me/"/><id>urn:uuid:c5a9a52f-d069-0f00-b809-cfc93179e52c</id><thr:in-reply-to
ref="urn:uuid:fa185733-6e77-db8f-1b71-e94d042094ff"
href="https://gnusha.org/pi/bitcoindev/CAHPaHkr5r4+hodZv6F2S1yCq_UcHSr2iCrkYLgZ_vryNgwbRPA@mail.gmail.com/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/O_i0gml6GTRro49f8c8jlCmgwOH5ZMDsJg4zxe-pX6akiGaibaFP7ilCTX90ZDfKORvmd3YlU4UUZWkwI-NPlvEtY8eVAvCFqO_ckuMG7m8=@proton.me/1.1.1-a.txt">[-- Attachment #1.1.1: Type: text/plain, Size: 12131 bytes --]</a>

Hi Alex,


<span
class="q">&gt; We need to have an already functioning PQC solution for Bitcoin itself, deployed, before any of commit/reveal can help, right?
</span>

Yes. Two reasons:

First, without on-chain PQC, making commitments would be impossible to do safely unless commitment are aggregated directly by miners into the coinbase transaction.

Second, without on-chain PQ-secure addresses, where would one even rescue coins to? Commit/reveal protocols are meant as a tool saving coins in an emergency, not for everyday spending.


PQ signature schemes are therefore needed as a prerequisite.


regards,
conduition
On Saturday, August 22nd, 2026 at 1:46 PM, Alex &lt;alexhultman@gmail&#8226;com&gt; wrote:

<span
class="q">&gt; Am I correct in understanding that commit/reveal always depends on someone else already having a valid PQC UTXO to spend?
&gt; So in other words, this can never be a solution for a (procrastinating Bitcoin system), only a solution for (procrastinating Bitcoin users).
&gt; 
</span>
<span
class="q">&gt; We need to have an already functioning PQC solution for Bitcoin itself, deployed, before any of commit/reveal can help, right?
&gt; 
</span>
<span
class="q">&gt; Den tors 20 aug. 2026 23:56&#39;conduition&#39; via Bitcoin Development Mailing List &lt;bitcoindev@googlegroups.com&gt; skrev:
&gt; 
</span>
<span
class="q">&gt; &gt; Dearest friends, colleagues, and lurkers,
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; I would like to present for your consideration a new commit/reveal rescue protocol to save the coins of quantum procrastinators - those who take no action to move their coins to PQC-enabled wallets by Q-Day.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; <a
href="https://conduition.io/bitcoin/dropkick/">https://conduition.io/bitcoin/dropkick/</a>
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; The term &#34;DropKick&#34; is self-descriptive of its usage: Drop a hidden commitment somewhere on the blockchain, and reveal it later with an SPV-style proof to Kick (spend) your legacy coins forward to a new PQ-secure wallet.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Background
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; As with any post-quantum commit/reveal protocol, DropKick uses the blockchain as a trustless timestamping service to prove than an honest user had earlier chronological knowledge of some secret witness to a quantum-hard one-way function. The honest user hides a commitment in a block, waits for confirmations, and later reveals her commitment to certify she knew the secret witness long before an adversary (like a quantum computer) could have done so. Assuming this witness was indeed kept secret prior to reveal time, it is already too late for the adversary to forge an equivalent proof.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; This general mechanism also allows validators to distinguish an honest bitcoin-holding procrastinator from a CRQC in many situations, and so procrastinators can still authorize spending of their legacy UTXOs even well after Q-day, provided the rescue protocol is deployed before Q-day as a new encumbrance on affected legacy coins.
&gt; &gt; DropKick In One Paragraph
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; DropKick specifically is a commit/reveal protocol where the commitment `H(H(w, Q), Q)` is hidden somewhere in a block, such as an OP_RETURN or inside a taproot tweak. `Q` is a post-quantum public key, and `w` is the witness to a one-way function `f`, such that `s = f(x)` is the script pubkey (address) encumbering a coin. We can later reveal the witness `w` and a signature from pubkey `Q` to authorize a spend, along with an opening proof showing that the commitment was included in a prior block. The verifier checks the commitment opening is valid and sufficiently old, checks `s = f(x)`, and verifies the PQ-signature from `Q`.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; See this section for the actual proving/verifying steps of the protocol.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Features
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Generality: DropKick generalizes to any efficient [1] one-way function based on knowledge asymmetries - things the honest user knows which the adversary doesn&#39;t. In the context of Bitcoin, the one-way function would typically be a computational pipeline that includes hashing of secret data unknown to a CRQC, such as &#34;BIP32 hardened derivation of an address&#34; or &#34;hashing a public key or script to build an address&#34; or &#34;taproot key tweaking&#34;. DropKick can be instantiated with different one-way functions to encumber different coins.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Compatibility: DropKick can be deployed as a soft-fork, as it only tightens spending validation rules, and does so only on certain UTXOs.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Confiscation: DropKick can be deployed without confiscating any coins, if so desired, by deploying it as an encumbrance only on UTXOs with decidable knowledge asymmetries like hashed addresses (see this section). If one wishes to maximize the number of legacy coins rescued, DropKick can also be deployed on undecidable knowledge asymmetries like BIP32-CKD. To be clear, P2PK coins cannot be covered by DropKick or indeed by any rescue protocol, as these UTXOs have no known knowledge asymmetries when a CRQC is in play.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Blockspace Efficiency: DropKick has near zero on-chain impact until reveal time, at which point the commitment opening proofs are included in a reveal transaction spending the legacy coins. Opening proofs could be attached in an OP_RETURN for backwards compatibility, or for better efficiency the proofs could be attached in a new transaction witness field which would allow for the 4x segwit discount to apply. DropKick opening proofs are approximately the same size as SPV or OpenTimestamps proofs (less than a kilobyte) and those proofs can be reused to rescue multiple related UTXOs, e.g. coins on the same address, or coins on addresses derived from the same seed.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Performance: DropKick opening proofs cost very little to verify: a few hash invocations, about as fast to verify as an SPV proof or lamport signature of the same size, and the cost of verification scales linearly with the size of the proof. If one has `txindex=1` enabled, verification is even faster. The only prerequisite data needed to verify the opening proof is the set of all Bitcoin block headers. Verifying the revealed witness `w` is exactly as efficient as evaluating the one-way function `f(w)`.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Ergonomics: Procrastinator do not need to have their own PQ-safe UTXOs available to execute a DropKick rescue: Users can delegate their commitments to untrusted third party servers called &#34;aggregators&#34; who do have PQ-safe UTXOs. These servers take it upon themselves to aggregate the commitments of other users together into a merkle tree, whose root they publish on-chain. Those aggregators can charge a salvage fee for their services if desired, paid in-band from the rescued UTXOs, or up-front out-of-band. Procrastinators can shop between different aggregators, and anyone with PQ-safe UTXOs can operate one.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Comparison to Lifeboat
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; DropKick competes directly with Tadge Dryja&#39;s Lifeboat/Lifejacket proposal (also see this older post), but DropKick aims for a different (lower) degree of security in exchange for a simpler implementation surface, more flexibility, and better efficiency.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; The two protocols fulfill functionally similar roles, so I will take a moment to compare and contrast DropKick and Lifeboat/Lifejacket.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; DropKick includes some novel features which Lifeboat does not, such as key certification (allowing things like RBF, or equivocation, by the honest spender), or generalization to arbitrary one-way functions. Such developments could be easily transferred to Lifeboat as well, so I will mostly ignore these minor differences here.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; The fundamental difference between DropKick and Lifeboat is the commitment ordering requirement.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; -   Lifeboat requires procrastinators to (1) procure a PQ-secure UTXO, and (2) upload a ~96-byte commitment in-the-clear in a new transaction, such as in an OP_RETURN or inscription. Validators must index all such commitments, so that they can chronologically order the revealed commitments later. Reveals reference this index to authorize spending: Only the earliest valid commitment for a given witness is allowed to spend the legacy coin that witness unlocks.
&gt; &gt;     
</span>
<span
class="q">&gt; &gt; -   DropKick encourages procrastinators to hide commitments in merkle trees committed into blocks, such as via a merkle root posted in an OP_RETURN, or in a taproot-style key tweak. Reveals use SPV-style proofs to convince validators that the commitment was included in a past block. Validators therefore do not (and cannot) index all commitments, and so there is no way to confirm any one commitment was earliest.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; By dropping the commitment ordering requirement, DropKick skips the need for a new index database collecting all the commitments, and this frees us from putting commitments on chain in-the-clear. DropKick commitments can be hidden off-chain, but anchored to the chain in merkle trees of arbitrary size, which is the key feature that enables the new role of aggregators, and means procrastinators don&#39;t need PQ-UTXOs to publish a commitment and rescue their legacy coins.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; To gain these benefits, DropKick sacrifices some security, by admitting miner censorship attacks where miners can intentionally censor a reveal transaction to gain a chance to steal the procrastinator&#39;s coins. Lifeboat entirely avoids this class of attacks, whereas DropKick requires a somewhat loose game-theoretical argument that miners will converge on choosing not to censor reveals, provided we enforce a long delay (days or weeks) between commitment and reveal steps, and provided the procrastinator pays a proportional fee to incentivize honest miners. We also have to assume no 51% reorg attacks of course, as a malicious hashrate majority could easily censor any reveal transactions and so steal coins.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; However, if this security loss is acceptable, DropKick offers a much simpler and less complex engineering surface area, and supports rescuing users in more diverse situations than LifeBoat can (because PQ UTXOs are mandatory in Lifeboat).
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; LifeBoat&#39;s UX advantage over DropKick is that because of the ordering, there is no long delay or value-proportional fee needed: Users only need to wait a few blocks between commit and reveal stages, and they pay only regular mining fees as usual. DropKick OTOH requires a delay proportional to the fraction of the UTXO one is willing to sacrifice to miners. E.g. if we assume users are willing to sacrifice 1% of their UTXOs, then we need to enforce a reveal delay period of at least 100 blocks. See here for a derivation of these parameters.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Conclusion
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; So that&#39;s it.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; I&#39;m submitting DropKick here as a sketch for consideration, not as a concrete proposal. I am most interested to know if anyone can think of a better mechanism to avoid miner censorship attacks, or if we can at least reduce the strength of the assumptions needed for DropKick to resist them.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; regards,
&gt; &gt; conduition
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; [1]: The one-way function must be efficient so that verifiers can recompute it to validate reveal transactions without DoS risks. For example, BIP32 master key derivation via BIP39 is not considered efficient because it uses PBKDF2, whereas BIP32 CKD is efficient if restricted to a maximum derivation depth.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; --
&gt; &gt; You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt; &gt; To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
&gt; &gt; To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo%3D%40proton.me">https://groups.google.com/d/msgid/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo%3D%40proton.me</a>.
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/O_i0gml6GTRro49f8c8jlCmgwOH5ZMDsJg4zxe-pX6akiGaibaFP7ilCTX90ZDfKORvmd3YlU4UUZWkwI-NPlvEtY8eVAvCFqO_ckuMG7m8%3D%40proton.me">https://groups.google.com/d/msgid/bitcoindev/O_i0gml6GTRro49f8c8jlCmgwOH5ZMDsJg4zxe-pX6akiGaibaFP7ilCTX90ZDfKORvmd3YlU4UUZWkwI-NPlvEtY8eVAvCFqO_ckuMG7m8%3D%40proton.me</a>.

<a
href="https://gnusha.org/pi/bitcoindev/O_i0gml6GTRro49f8c8jlCmgwOH5ZMDsJg4zxe-pX6akiGaibaFP7ilCTX90ZDfKORvmd3YlU4UUZWkwI-NPlvEtY8eVAvCFqO_ckuMG7m8=@proton.me/1.1.2.1-a.bin">[-- Attachment #1.1.2.1: Type: text/html, Size: 21428 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/O_i0gml6GTRro49f8c8jlCmgwOH5ZMDsJg4zxe-pX6akiGaibaFP7ilCTX90ZDfKORvmd3YlU4UUZWkwI-NPlvEtY8eVAvCFqO_ckuMG7m8=@proton.me/1.2-a.bin">[-- Attachment #1.2: publickey - conduition@proton.me - 0x474891AD.asc --]
[-- Type: application/pgp-keys, Size: 649 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/O_i0gml6GTRro49f8c8jlCmgwOH5ZMDsJg4zxe-pX6akiGaibaFP7ilCTX90ZDfKORvmd3YlU4UUZWkwI-NPlvEtY8eVAvCFqO_ckuMG7m8=@proton.me/2-signature.asc">[-- Attachment #2: OpenPGP digital signature --]
[-- Type: application/pgp-signature, Size: 343 bytes --]</a>
</pre></div></content></entry><entry><author><name>Alex</name><email>alexhultman@gmail.com</email></author><title
type="html">Re: [bitcoindev] DropKick &#9917;&#65039; - A minimal commit/reveal PQ rescue protocol</title><updated>2026-08-22T17:48:55Z</updated><link
href="https://gnusha.org/pi/bitcoindev/CAHPaHkr5r4+hodZv6F2S1yCq_UcHSr2iCrkYLgZ_vryNgwbRPA@mail.gmail.com/"/><id>urn:uuid:fa185733-6e77-db8f-1b71-e94d042094ff</id><thr:in-reply-to
ref="urn:uuid:984f22f8-a646-298c-fe2a-d2461916f5ff"
href="https://gnusha.org/pi/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo=@proton.me/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap"><a
href="https://gnusha.org/pi/bitcoindev/CAHPaHkr5r4+hodZv6F2S1yCq_UcHSr2iCrkYLgZ_vryNgwbRPA@mail.gmail.com/1-a.txt">[-- Attachment #1: Type: text/plain, Size: 12271 bytes --]</a>

Am I correct in understanding that commit/reveal always depends on someone
else already having a valid PQC UTXO to spend?

So in other words, this can never be a solution for a (procrastinating
Bitcoin system), only a solution for (procrastinating Bitcoin users).

We need to have an already functioning PQC solution for Bitcoin itself,
deployed, before any of commit/reveal can help, right?

Den tors 20 aug. 2026 23:56&#39;conduition&#39; via Bitcoin Development Mailing
List &lt;bitcoindev@googlegroups.com&gt; skrev:

<span
class="q">&gt; Dearest friends, colleagues, and lurkers,
&gt;
&gt; I would like to present for your consideration a new commit/reveal rescue
&gt; protocol to save the coins of quantum procrastinators - those who take no
&gt; action to move their coins to PQC-enabled wallets by Q-Day.
&gt;
&gt; <a
href="https://conduition.io/bitcoin/dropkick/">https://conduition.io/bitcoin/dropkick/</a>
&gt;
&gt; The term &#34;DropKick&#34; is self-descriptive of its usage: *Drop* a hidden
&gt; commitment somewhere on the blockchain, and reveal it later with an
&gt; SPV-style proof to *Kick* (spend) your legacy coins forward to a new
&gt; PQ-secure wallet.
&gt;
&gt; Background
&gt;
&gt; As with any post-quantum commit/reveal protocol, DropKick uses the
&gt; blockchain as a trustless timestamping service to prove than an honest user
&gt; had earlier chronological knowledge of some secret *witness* to a
&gt; quantum-hard* one-way function*. The honest user hides a *commitment* in
&gt; a block, waits for confirmations, and later *reveals* her commitment to
&gt; certify she knew the secret witness long before an adversary (like a
&gt; quantum computer) could have done so. Assuming this witness was indeed kept
&gt; secret prior to reveal time, it is already too late for the adversary to
&gt; forge an equivalent proof.
&gt;
&gt;
&gt; This general mechanism also allows validators to distinguish an honest
&gt; bitcoin-holding procrastinator from a CRQC in many situations, and so
&gt; procrastinators can still authorize spending of their legacy UTXOs even
&gt; well after Q-day, provided the rescue protocol is deployed *before* Q-day
&gt; as a new encumbrance on affected legacy coins.
&gt;
&gt; DropKick In One Paragraph
&gt;
&gt; DropKick specifically is a commit/reveal protocol where the commitment H(H(w,
&gt; Q), Q)&#8203; is hidden somewhere in a block, such as an OP_RETURN or inside a
&gt; taproot tweak. Q&#8203; is a post-quantum public key, and w&#8203; is the witness to
&gt; a one-way function f&#8203;, such that s = f(x)&#8203; is the script pubkey (address)
&gt; encumbering a coin. We can later reveal the witness w&#8203; and a signature
&gt; from pubkey Q&#8203; to authorize a spend, along with an *opening proof* showing
&gt; that the commitment was included in a prior block. The verifier checks the
&gt; commitment opening is valid and sufficiently old, checks s = f(x)&#8203;, and
&gt; verifies the PQ-signature from Q&#8203;.
&gt;
&gt; See this section for the actual proving/verifying steps of the protocol.
&gt; &lt;<a
href="https://conduition.io/bitcoin/dropkick/#DropKick">https://conduition.io/bitcoin/dropkick/#DropKick</a>&gt;
&gt;
&gt; Features
&gt;
&gt; *Generality:* DropKick generalizes to any *efficient *[1] one-way
&gt; function based on knowledge asymmetries - things the honest user knows
&gt; which the adversary doesn&#39;t. In the context of Bitcoin, the one-way
&gt; function would typically be a computational pipeline that includes hashing
&gt; of secret data unknown to a CRQC, such as &#34;BIP32 hardened derivation of an
&gt; address&#34; or &#34;hashing a public key or script to build an address&#34; or
&gt; &#34;taproot key tweaking&#34;. DropKick can be instantiated with different one-way
&gt; functions to encumber different coins.
&gt;
&gt; *Compatibility:* DropKick can be deployed as a soft-fork, as it only
&gt; *tightens* spending validation rules, and does so only on certain UTXOs.
&gt;
&gt; *Confiscation:* DropKick can be deployed *without* confiscating any
&gt; coins, if so desired, by deploying it as an encumbrance only on UTXOs with
&gt; *decidable* knowledge asymmetries like hashed addresses (see this section
&gt; &lt;<a
href="https://conduition.io/bitcoin/dropkick/#Knowledge-Asymmetries">https://conduition.io/bitcoin/dropkick/#Knowledge-Asymmetries</a>&gt;). If one
&gt; wishes to maximize the number of legacy coins rescued, DropKick can also be
&gt; deployed on *undecidable* knowledge asymmetries like BIP32-CKD. To be
&gt; clear, P2PK coins cannot be covered by DropKick or indeed by any rescue
&gt; protocol, as these UTXOs have no known knowledge asymmetries when a CRQC is
&gt; in play.
&gt;
&gt; *Blockspace Efficiency:* DropKick has near zero on-chain impact until
&gt; reveal time, at which point the commitment opening proofs are included in a *reveal
&gt; transaction* spending the legacy coins. Opening proofs could be attached
&gt; in an OP_RETURN for backwards compatibility, or for better efficiency the
&gt; proofs could be attached in a new transaction witness field which would
&gt; allow for the 4x segwit discount to apply. DropKick opening proofs are
&gt; approximately the same size as SPV
&gt; &lt;<a
href="https://learnmeabitcoin.com/technical/networking/node/#lightweight-node">https://learnmeabitcoin.com/technical/networking/node/#lightweight-node</a>&gt;
&gt; or OpenTimestamps &lt;<a
href="https://opentimestamps.org/">https://opentimestamps.org/</a>&gt; proofs (less than a
&gt; kilobyte) and those proofs can be reused to rescue multiple related UTXOs,
&gt; e.g. coins on the same address, or coins on addresses derived from the same
&gt; seed.
&gt;
&gt; *Performance:* DropKick opening proofs cost very little to verify: a few
&gt; hash invocations, about as fast to verify as an SPV proof or lamport
&gt; signature of the same size, and the cost of verification scales linearly
&gt; with the size of the proof. If one has txindex=1&#8203; enabled, verification
&gt; is even faster. The only prerequisite data needed to verify the opening
&gt; proof is the set of all Bitcoin block headers. Verifying the revealed
&gt; witness w&#8203; is exactly as efficient as evaluating the one-way function f(w)
&gt; &#8203;.
&gt;
&gt; *Ergonomics: *Procrastinator *do not* need to have their own PQ-safe
&gt; UTXOs available to execute a DropKick rescue: Users can delegate their
&gt; commitments to untrusted third party servers called &#34;aggregators&#34; who *do* have
&gt; PQ-safe UTXOs. These servers take it upon themselves to aggregate the
&gt; commitments of other users together into a merkle tree, whose root they
&gt; publish on-chain. Those aggregators can charge a salvage fee for their
&gt; services if desired, paid in-band from the rescued UTXOs, or up-front out-of-band. Procrastinators
&gt; can shop between different aggregators, and anyone with PQ-safe UTXOs can
&gt; operate one.
&gt;
&gt; Comparison to Lifeboat
&gt;
&gt; DropKick competes directly with Tadge Dryja&#39;s Lifeboat/Lifejacket proposal
&gt; &lt;<a
href="https://www.youtube.com/watch?v=PmW90HX89P8">https://www.youtube.com/watch?v=PmW90HX89P8</a>&gt; (also see this older post
&gt; &lt;<a
href="https://groups.google.com/g/bitcoindev/c/LpWOcXMcvk8/">https://groups.google.com/g/bitcoindev/c/LpWOcXMcvk8/</a>&gt;), but DropKick
&gt; aims for a different (lower) degree of security in exchange for a simpler
&gt; implementation surface, more flexibility, and better efficiency.
&gt;
&gt; The two protocols fulfill functionally similar roles, so I will take a
&gt; moment to compare and contrast DropKick and Lifeboat/Lifejacket.
&gt;
&gt; DropKick includes some novel features which Lifeboat does not, such as *key
&gt; certification *(allowing things like RBF, or equivocation, by the honest
&gt; spender), or generalization to arbitrary one-way functions. Such
&gt; developments could be easily transferred to Lifeboat as well, so I will
&gt; mostly ignore these minor differences here.
&gt;
&gt; The fundamental difference between DropKick and Lifeboat is the commitment
&gt; ordering requirement.
&gt;
&gt;
&gt;    - Lifeboat requires procrastinators to (1) procure a PQ-secure UTXO,
&gt;    and (2) upload a ~96-byte commitment in-the-clear in a new transaction,
&gt;    such as in an OP_RETURN or inscription. Validators must index all such
&gt;    commitments, so that they can *chronologically order* the revealed
&gt;    commitments later. Reveals reference this index to authorize spending: Only
&gt;    the earliest valid commitment for a given witness is allowed to spend
&gt;    the legacy coin that witness unlocks.
&gt;    - DropKick encourages procrastinators to *hide* commitments in merkle
&gt;    trees committed into blocks, such as via a merkle root posted in an
&gt;    OP_RETURN, or in a taproot-style key tweak. Reveals use SPV-style proofs to
&gt;    convince validators that the commitment was included in a past block. *Validators
&gt;    therefore do not (and cannot) index all commitments, and so there is no way
&gt;    to confirm any one commitment was earliest*.
&gt;
&gt;
&gt; By dropping the commitment ordering requirement, DropKick skips the need
&gt; for a new index database collecting all the commitments, and this frees us
&gt; from putting commitments on chain in-the-clear. DropKick commitments can be
&gt; hidden off-chain, but anchored to the chain in merkle trees of arbitrary
&gt; size, which is the key feature that enables the new role of aggregators,
&gt; and means procrastinators don&#39;t need PQ-UTXOs to publish a commitment and
&gt; rescue their legacy coins.
&gt;
&gt; To gain these benefits, DropKick sacrifices some security, by admitting miner
&gt; censorship attacks &lt;<a
href="https://conduition.io/bitcoin/dropkick/#Censorship">https://conduition.io/bitcoin/dropkick/#Censorship</a>&gt; where
&gt; miners can intentionally censor a reveal transaction to gain a chance to
&gt; steal the procrastinator&#39;s coins. Lifeboat entirely avoids this class of
&gt; attacks, whereas DropKick requires a somewhat loose game-theoretical
&gt; argument &lt;<a
href="https://conduition.io/bitcoin/dropkick/#Appendix-Game-Theory">https://conduition.io/bitcoin/dropkick/#Appendix-Game-Theory</a>&gt;
&gt; that miners will converge on choosing *not* to censor reveals, provided
&gt; we enforce a long delay (days or weeks) between commitment and reveal
&gt; steps, and provided the procrastinator pays a proportional fee to
&gt; incentivize honest miners. We also have to assume no 51% reorg attacks of
&gt; course, as a malicious hashrate majority could easily censor any reveal
&gt; transactions and so steal coins.
&gt;
&gt; However, if this security loss is acceptable, DropKick offers a much
&gt; simpler and less complex engineering surface area, and supports rescuing
&gt; users in more diverse situations than LifeBoat can (because PQ UTXOs are
&gt; mandatory in Lifeboat).
&gt;
&gt; LifeBoat&#39;s UX advantage over DropKick is that because of the ordering,
&gt; there is no long delay or value-proportional fee needed: Users only need to
&gt; wait a few blocks between *commit* and *reveal* stages, and they pay only
&gt; regular mining fees as usual. DropKick OTOH requires a delay proportional
&gt; to the fraction of the UTXO one is willing to sacrifice to miners. E.g. if
&gt; we assume users are willing to sacrifice 1% of their UTXOs, then we need to
&gt; enforce a reveal delay period of at least 100 blocks. See here for a
&gt; derivation of these parameters
&gt; &lt;<a
href="https://conduition.io/bitcoin/dropkick/#Parameters">https://conduition.io/bitcoin/dropkick/#Parameters</a>&gt;.
&gt;
&gt; Conclusion
&gt;
&gt; So that&#39;s it.
&gt;
&gt; I&#39;m submitting DropKick here as a sketch for consideration, not as a
&gt; concrete proposal. I am most interested to know if anyone can think of a
&gt; better mechanism to avoid miner censorship attacks, or if we can at least
&gt; reduce the strength of the assumptions needed for DropKick to resist them.
&gt;
&gt; regards,
&gt; conduition
&gt;
&gt;
&gt; [1]: The one-way function must be *efficient* so that verifiers can
&gt; recompute it to validate reveal transactions without DoS risks. For
&gt; example, BIP32 master key derivation via BIP39 is not considered efficient
&gt; because it uses PBKDF2, whereas BIP32 CKD is efficient if restricted to a
&gt; maximum derivation depth.
&gt;
&gt; --
&gt; You received this message because you are subscribed to the Google Groups
&gt; &#34;Bitcoin Development Mailing List&#34; group.
&gt; To unsubscribe from this group and stop receiving emails from it, send an
&gt; email to bitcoindev+unsubscribe@googlegroups&#8226;com.
&gt; To view this discussion visit
&gt; <a
href="https://groups.google.com/d/msgid/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo%3D%40proton.me">https://groups.google.com/d/msgid/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo%3D%40proton.me</a>
&gt; &lt;<a
href="https://groups.google.com/d/msgid/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo%3D%40proton.me?utm_medium=email&#38;utm_source=footer">https://groups.google.com/d/msgid/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo%3D%40proton.me?utm_medium=email&#38;utm_source=footer</a>&gt;
&gt; .
&gt;
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/CAHPaHkr5r4%2BhodZv6F2S1yCq_UcHSr2iCrkYLgZ_vryNgwbRPA%40mail.gmail.com">https://groups.google.com/d/msgid/bitcoindev/CAHPaHkr5r4%2BhodZv6F2S1yCq_UcHSr2iCrkYLgZ_vryNgwbRPA%40mail.gmail.com</a>.

<a
href="https://gnusha.org/pi/bitcoindev/CAHPaHkr5r4+hodZv6F2S1yCq_UcHSr2iCrkYLgZ_vryNgwbRPA@mail.gmail.com/2-a.bin">[-- Attachment #2: Type: text/html, Size: 18995 bytes --]</a>
</pre></div></content></entry><entry><author><name>&#39;nervana21&#39; via Bitcoin Development Mailing List</name><email>bitcoindev@googlegroups.com</email></author><title>Re: [bitcoindev] Re: [BIP Proposal] Anti-Fee-Sniping with LockTime</title><updated>2026-08-21T20:35:17Z</updated><link
href="https://gnusha.org/pi/bitcoindev/WCgkJmyQ8exgIWF_AXmaycRFvGbLtOwTExlanZ3qkAS1to6Ecb4VduhTFqC42Bc3XE9AIPvpx30Ebe5Vl2NeKarBMUzw8syjsAzgxIZOVso=@pm.me/"/><id>urn:uuid:e6df4ce4-4e0f-ed4c-c24c-da2f38594092</id><thr:in-reply-to
ref="urn:uuid:5afdbf42-0517-fd0f-9840-b40d2b2c527a"
href="https://gnusha.org/pi/bitcoindev/2b19cd5e-84aa-4779-b1a6-490cc918cc52n@googlegroups.com/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">Hi b10c,
Thanks for the comments, my replies are inline below.

On Wednesday, August 19th, 2026 at 9:21 AM, b10c &lt;0xb10c@gmail&#8226;com&gt; wrote:

<span
class="q">&gt; Hi nervana21,
&gt; 
&gt; some comments in random order on the BIP proposal and Anti-Fee-Sniping:
&gt; 
&gt; 
&gt; - You mention BIP125 a couple of times in Specification. Note that in recent versions of Bitcoin Core, BIP125 signaling is no longer required for a transaction to be replaceable under the default mempool policy.
</span>
You&#39;re right. I&#39;ve updated the draft to remove references to BIP125. For this BIP the only sequence requirement is that at least one input is non-final so that nLockTime is enforced. The pseudocode uses 2**32 - 2 as one conventional choice.

<span
class="q">&gt; - While the 10%-back-date-rule in Anti-Fee-Sniping is a privacy feature for some people, it is also a privacy leak for others: <a
href="https://github.com/bitcoin/bitcoin/issues/26526:">https://github.com/bitcoin/bitcoin/issues/26526:</a> When fee-bumping a previously not back-date transaction, Bitcoin Core might back-date the replacement. This is fingerprint that you likely back-dated the replacement transaction. There is also <a
href="https://github.com/bitcoin/bitcoin/issues/26527">https://github.com/bitcoin/bitcoin/issues/26527</a>, which I&#39;m not sure if it&#39;s an actual problem or not (haven&#39;t had the time to double-check). Maybe documenting some of these edge-cases in the BIP makes sense. This allows potential future/other implementations not to make similar mistakes.
</span>
I added a Rationale section that cites <a
href="https://github.com/bitcoin/bitcoin/issues/26526">https://github.com/bitcoin/bitcoin/issues/26526</a> and the related type flip case <a
href="https://github.com/bitcoin/bitcoin/issues/35628">https://github.com/bitcoin/bitcoin/issues/35628</a>. The BIP now says implementations should document replacement locktime policy, including locktime type across replacements. When re-running the privacy branch on a height based previous locktime, it floors at that height and does not go older unless that policy is intentional and documented. The spec already covers that a child nLockTime does not protect an unconfirmed parent, so I left <a
href="https://github.com/bitcoin/bitcoin/issues/26527">https://github.com/bitcoin/bitcoin/issues/26527</a> out of the BIP. Separately, there is currently an open Core PR that aims at the same floor on bumpfee via minimum_height. <a
href="https://github.com/bitcoin/bitcoin/pull/36040">https://github.com/bitcoin/bitcoin/pull/36040</a>

<span
class="q">&gt; - There has been a case where the trying to do Anti-Fee-Sniping 1) wasn&#39;t implemented properly in a wallet so it didn&#39;t work 2) ended up being a clear fingerprint for this wallet: <a
href="https://b10c.me/observations/01-locktime-stairs/">https://b10c.me/observations/01-locktime-stairs/</a>. By now, this wallet doesn&#39;t have much usage anymore (<a
href="https://mainnet.observer/charts/transactions-not-enforced-locktime/">https://mainnet.observer/charts/transactions-not-enforced-locktime/</a>) but this still shows some of it&#39;s pitfalls.
</span>
Got it. I&#39;ve updated the BIP to warn implementers of this pitfall. I cited your locktime stairs writeup and the unenforced locktime chart.

<span
class="q">&gt; - Note that currently only around 5% of the transactions set a heigt-based time-lock: <a
href="https://mainnet.observer/charts/transactions-height-based-locktime/">https://mainnet.observer/charts/transactions-height-based-locktime/</a> - growing this anonymity set might be interesting to some wallets, but currently, do don&#39;t stick out if you don&#39;t do Anti-Fee-Sniping (or use locktime).
</span>
Makes sense. The draft now mentions this point explicitly and keeps broader adoption as the anonymity set goal.

Updated draft
<a
href="https://github.com/nervana21/bips/blob/anti-fee-snipe/bip-anti-fee-sniping-with-locktime.md">https://github.com/nervana21/bips/blob/anti-fee-snipe/bip-anti-fee-sniping-with-locktime.md</a>

Best,
nervana21

<span
class="q">&gt; 
&gt; 
&gt; Best
&gt; b10c
&gt; On Tuesday, 18 August 2026 at 11:17:44 UTC+2 nervana21 wrote:
&gt; 
&gt; &gt; Hello all,
&gt; &gt; 
&gt; &gt; Anti-fee-sniping with nLockTime has been present in Bitcoin Core since
&gt; &gt; 2014 and in Electrum since 2017. BIP326 assumes this nLockTime behavior
&gt; &gt; as the baseline and uses nSequence instead for some taproot spends.
&gt; &gt; However, the nLockTime rules themselves were never specified in a BIP.
&gt; &gt; 
&gt; &gt; <a
href="https://github.com/nervana21/bips/blob/anti-fee-snipe/bip-anti-fee-sniping-with-locktime.md">https://github.com/nervana21/bips/blob/anti-fee-snipe/bip-anti-fee-sniping-with-locktime.md</a>
&gt; &gt; 
&gt; &gt; The BIP draft follows Bitcoin Core&#39;s DiscourageFeeSniping and
&gt; &gt; IsCurrentForAntiFeeSniping functions. nLockTime is set to the current tip height.
&gt; &gt; With probability 10%, a uniform random integer in 0..99 is subtracted
&gt; &gt; and the result is clamped at 0. A locktime equal to the tip height
&gt; &gt; cannot be included in a remine of the tip. An older locktime chosen on
&gt; &gt; the privacy branch can. nLockTime is set to 0 during initial block
&gt; &gt; download or when the tip is more than 8 hours old. The policy is not
&gt; &gt; applied when nLockTime is already set or when any input already has a
&gt; &gt; preset nSequence. Test vectors are included.
&gt; &gt; 
&gt; &gt; Constructive criticism is greatly appreciated.
&gt; &gt; 
&gt; &gt; Cheers,
&gt; &gt; nervana21
&gt; 
&gt; --
&gt; You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt; To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
&gt; To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/2b19cd5e-84aa-4779-b1a6-490cc918cc52n%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/2b19cd5e-84aa-4779-b1a6-490cc918cc52n%40googlegroups.com</a>.
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/WCgkJmyQ8exgIWF_AXmaycRFvGbLtOwTExlanZ3qkAS1to6Ecb4VduhTFqC42Bc3XE9AIPvpx30Ebe5Vl2NeKarBMUzw8syjsAzgxIZOVso%3D%40pm.me">https://groups.google.com/d/msgid/bitcoindev/WCgkJmyQ8exgIWF_AXmaycRFvGbLtOwTExlanZ3qkAS1to6Ecb4VduhTFqC42Bc3XE9AIPvpx30Ebe5Vl2NeKarBMUzw8syjsAzgxIZOVso%3D%40pm.me</a>.

</pre></div></content></entry><entry><author><name>&#39;conduition&#39; via Bitcoin Development Mailing List</name><email>bitcoindev@googlegroups.com</email></author><title
type="html">[bitcoindev] DropKick &#9917;&#65039; - A minimal commit/reveal PQ rescue protocol</title><updated>2026-08-20T21:56:39Z</updated><link
href="https://gnusha.org/pi/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo=@proton.me/"/><id>urn:uuid:984f22f8-a646-298c-fe2a-d2461916f5ff</id><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo=@proton.me/1.1.1-a.txt">[-- Attachment #1.1.1: Type: text/plain, Size: 10103 bytes --]</a>

Dearest friends, colleagues, and lurkers,

I would like to present for your consideration a new commit/reveal rescue protocol to save the coins of quantum procrastinators - those who take no action to move their coins to PQC-enabled wallets by Q-Day.

<a
href="https://conduition.io/bitcoin/dropkick/">https://conduition.io/bitcoin/dropkick/</a>

The term &#34;DropKick&#34; is self-descriptive of its usage: Drop a hidden commitment somewhere on the blockchain, and reveal it later with an SPV-style proof to Kick&#160;(spend) your legacy coins forward to a new PQ-secure wallet.

Background

As with any post-quantum commit/reveal protocol, DropKick uses the blockchain as a trustless timestamping service to prove than an honest user had earlier chronological knowledge of some secret witness&#160;to a quantum-hard one-way function. The honest user hides a commitment in a block, waits for confirmations, and later reveals&#160;her commitment to certify she knew the secret witness long before an adversary (like a quantum computer) could have done so. Assuming this witness was indeed kept secret prior to reveal time, it is already too late for the adversary to forge an equivalent proof.


This general mechanism also allows validators to distinguish an honest bitcoin-holding procrastinator from a CRQC in many situations, and so procrastinators can still authorize spending of their legacy UTXOs even well after Q-day, provided the rescue protocol is deployed&#160;before&#160;Q-day as a new encumbrance on affected legacy coins.
DropKick In One Paragraph

DropKick specifically is a&#160;commit/reveal protocol where the commitment&#160;`H(H(w, Q), Q)` is hidden somewhere in a block, such as an OP_RETURN or inside a taproot tweak.&#160;`Q` is a post-quantum public key, and `w`&#160;is the witness to a one-way function `f`, such that `s = f(x)` is the script pubkey (address) encumbering a coin. We can later reveal the witness `w` and a signature from pubkey&#160;`Q` to authorize a spend, along with an opening proof&#160;showing that the commitment was included in a prior block. The verifier checks the commitment opening is valid and sufficiently old, checks `s = f(x)`, and verifies the PQ-signature from `Q`.

See this section for the actual proving/verifying steps of the protocol.

Features


Generality:&#160;DropKick generalizes to any efficient [1]&#160;one-way function based on knowledge asymmetries - things the honest user knows which the adversary doesn&#39;t.&#160;In the context of Bitcoin, the one-way function would typically be a computational pipeline that includes hashing of secret data unknown to a CRQC, such as &#34;BIP32 hardened derivation of an address&#34; or &#34;hashing a public key or script to build an address&#34; or &#34;taproot key tweaking&#34;. DropKick can be instantiated with different one-way functions to encumber different coins.


Compatibility: DropKick can be deployed as a soft-fork, as it only tightens spending validation rules, and does so only on certain UTXOs.

Confiscation: DropKick can be deployed without&#160;confiscating any coins, if so desired, by deploying it as an encumbrance only on UTXOs with&#160;decidable&#160;knowledge asymmetries like hashed addresses (see this section). If one wishes to maximize the number of legacy coins rescued, DropKick can also be deployed on undecidable&#160;knowledge asymmetries like BIP32-CKD. To be clear, P2PK&#160;coins cannot be covered by DropKick or indeed by any rescue protocol, as these UTXOs have no known knowledge asymmetries when a CRQC is in play.

Blockspace Efficiency: DropKick has near zero on-chain impact until reveal time, at which point the commitment opening proofs are included in a reveal transaction&#160;spending the legacy coins. Opening proofs could be attached in an OP_RETURN for backwards compatibility, or for better efficiency the proofs could be attached in a new transaction witness field which would allow for the 4x segwit discount to apply. DropKick opening proofs are approximately the same size as SPV or OpenTimestamps proofs (less than a kilobyte) and those proofs can be reused to rescue multiple related UTXOs, e.g. coins on the same address, or coins on addresses derived from the same seed.

Performance: DropKick opening proofs cost very little to verify: a few hash invocations, about as fast to verify as an SPV proof or lamport signature of the same size, and the cost of verification scales linearly with the size of the proof. If one has&#160;`txindex=1` enabled, verification is even faster.&#160;The only prerequisite data needed to verify the opening proof is the set of all Bitcoin block headers.&#160;Verifying the revealed witness `w`&#160;is exactly as efficient as evaluating the one-way function `f(w)`.


Ergonomics:&#160;Procrastinator do not need to have their own PQ-safe UTXOs available to execute a DropKick rescue: Users can delegate their commitments to untrusted third party servers called &#34;aggregators&#34; who do&#160;have PQ-safe UTXOs. These servers take it upon themselves to aggregate the commitments of other users together into a merkle tree, whose root they publish on-chain. Those aggregators can charge a salvage fee for their services if desired, paid in-band from the rescued UTXOs, or up-front&#160;out-of-band.&#160;Procrastinators can shop between different aggregators, and anyone with PQ-safe UTXOs can operate one.

Comparison to Lifeboat

DropKick competes directly with Tadge Dryja&#39;s Lifeboat/Lifejacket proposal&#160;(also see this older post), but DropKick aims for a different (lower) degree of security in exchange for a simpler implementation surface, more flexibility, and better efficiency.

The two protocols fulfill functionally similar roles, so I will take a moment to compare and contrast DropKick and Lifeboat/Lifejacket.

DropKick includes some novel features which Lifeboat does not, such as key certification (allowing things like RBF, or equivocation, by the honest spender), or generalization to arbitrary one-way functions. Such developments could be easily transferred to Lifeboat as well, so I will mostly ignore these minor differences here.

The fundamental difference between DropKick and Lifeboat is the commitment ordering requirement.


-   Lifeboat requires procrastinators to (1) procure a PQ-secure UTXO, and (2) upload a ~96-byte commitment in-the-clear in a new transaction, such as in an OP_RETURN or inscription. Validators must index all such commitments, so that they can chronologically order&#160;the revealed commitments later. Reveals reference this index to authorize spending: Only the&#160;earliest valid commitment for a given witness is allowed to spend the legacy coin that witness unlocks.
    

-   DropKick encourages procrastinators to hide&#160;commitments in merkle trees committed into blocks, such as via a merkle root posted in an OP_RETURN, or in a taproot-style key tweak. Reveals use SPV-style proofs to convince validators that the commitment was included in a past block. Validators therefore do not (and cannot) index all commitments, and so there is no way to confirm any one commitment was earliest.



By dropping the commitment ordering requirement, DropKick skips the need for a new index database collecting all the commitments, and this frees us from putting commitments on chain in-the-clear. DropKick commitments can be hidden off-chain, but anchored to the chain in merkle trees of arbitrary size, which is the key feature that enables the new role of aggregators, and means procrastinators don&#39;t need PQ-UTXOs to publish a commitment and rescue their legacy coins.

To gain these benefits, DropKick sacrifices some security, by admitting&#160;miner censorship attacks&#160;where miners can intentionally censor a reveal transaction to gain a chance to steal the procrastinator&#39;s coins. Lifeboat entirely avoids this class of attacks, whereas DropKick requires a somewhat loose game-theoretical argument that miners will converge on choosing not&#160;to censor reveals, provided we enforce a long delay (days or weeks) between commitment and reveal steps, and provided the procrastinator pays a proportional fee to incentivize honest miners. We also have to assume no 51% reorg attacks of course, as a malicious hashrate majority could easily censor any reveal transactions and so steal coins.

However, if this security loss is acceptable, DropKick offers a much simpler and less complex engineering surface area, and supports rescuing users in more diverse situations than LifeBoat can (because PQ UTXOs are mandatory in Lifeboat).

LifeBoat&#39;s UX advantage over DropKick is that because of the ordering, there is no long delay or value-proportional fee needed: Users only need to wait a few blocks between commit&#160;and reveal&#160;stages, and they pay only regular mining fees as usual. DropKick OTOH requires a delay proportional to the fraction of the UTXO one is willing to sacrifice to miners. E.g. if we assume users are willing to sacrifice 1% of their UTXOs, then we need to enforce a reveal delay period of at least 100 blocks. See here for a derivation of these parameters.&#160;

Conclusion

So that&#39;s it.

I&#39;m submitting DropKick here as a sketch for consideration, not as a concrete proposal. I am most interested to know if anyone can think of a better mechanism to avoid miner censorship attacks, or if we can at least reduce the strength of the assumptions needed for DropKick to resist them.

regards,
conduition


[1]: The one-way function must be efficient&#160;so that verifiers can recompute it to validate reveal transactions without DoS risks. For example, BIP32 master key derivation via BIP39 is not considered efficient because it uses PBKDF2, whereas BIP32 CKD is efficient if restricted to a maximum derivation depth.

-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo%3D%40proton.me">https://groups.google.com/d/msgid/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo%3D%40proton.me</a>.

<a
href="https://gnusha.org/pi/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo=@proton.me/1.1.2.1-a.bin">[-- Attachment #1.1.2.1: Type: text/html, Size: 18262 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo=@proton.me/1.2-a.bin">[-- Attachment #1.2: publickey - conduition@proton.me - 0x474891AD.asc --]
[-- Type: application/pgp-keys, Size: 649 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/ruufSzDPIml1W5hF-m_IJLeBzuhqey6CGe7-zT1WwY4vlhVj_5NJTSalz43T4ZlZgXs3sDesW61FaU_asfj39Ri1QgSXtz7-OekEt6bbTvo=@proton.me/2-signature.asc">[-- Attachment #2: OpenPGP digital signature --]
[-- Type: application/pgp-signature, Size: 343 bytes --]</a>
</pre></div></content></entry><entry><author><name>&#39;conduition&#39; via Bitcoin Development Mailing List</name><email>bitcoindev@googlegroups.com</email></author><title
type="html">Re: [bitcoindev] post-quantum: solution ideas to &#34;tripwire&#34;game-theory issues + a certificate-based rescue protocol</title><updated>2026-08-20T16:46:26Z</updated><link
href="https://gnusha.org/pi/bitcoindev/UW5dOJNFjgt67sz-2sRUPeMJi0XL6_wSm7zKCmSoj_8IzkQavc-Vo9vwiR7Tbaz7bvP2YrH8b-1JGm-9jNQXQM8dqsw1f1Sl75SHIOt9cOc=@proton.me/"/><id>urn:uuid:b454f49b-a0d6-ff4b-73f4-bc28259cf2f9</id><thr:in-reply-to
ref="urn:uuid:9bc64123-54ff-d80c-37f8-380f60ae07bf"
href="https://gnusha.org/pi/bitcoindev/CALZpt+HRNFdtWUpg4v2aj9CRMamS7eG9Nem3mdxJq4sZEtOL6w@mail.gmail.com/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/UW5dOJNFjgt67sz-2sRUPeMJi0XL6_wSm7zKCmSoj_8IzkQavc-Vo9vwiR7Tbaz7bvP2YrH8b-1JGm-9jNQXQM8dqsw1f1Sl75SHIOt9cOc=@proton.me/1.1.1-a.txt">[-- Attachment #1.1.1: Type: text/plain, Size: 13066 bytes --]</a>

Hi Antoine,


<span
class="q">&gt; One way to alleviate the problem would be to consider thespent of the NUMS point, that can be a hardcoded value that
&gt; one can commit in a dedicated coinbase output as a &#34;proof of
&gt; work in itself&#34; where the CheckProofOfWOrk() would return true
&gt; for it and the nChainWork of the chain in which the NUMS spent
&gt; is included would get a bonus (e.g *20 the last period&#39;s difficulty).
</span>


A very interesting idea! Essentially this gives a one-time difficulty advantage to miners who choose to include the tripwire proof, so a &#34;51% attack&#34; to censor that proof would need a much larger share of hashrate. For example, if the honest miners receive a 2x advantage for mining the tripwire, then censoring miners would need to hold at least double the hashrate of the honest miners (e.g a &#34;67% attack&#34;). If the advantage is 4x, then they&#39;d need at least 4x the hashrate (e.g. an &#34;81% attack&#34;), etc.


It&#39;s clever, but the main problem is that it&#39;s a hard fork, as you mention:


<span
class="q">&gt; All network nodes sharing this consensus mechanism would followthe new and same chain ordering, overruling the most proof of
&gt; work ordering.
</span>


Nodes that don&#39;t upgrade would see the new &#34;advantaged&#34; block containing the tripwire proof as having an invalid PoW, and would reject it.


Granted, this would be a pre-scheduled hard-fork agreed upon presumably well in-advance of the (undefined) fork date, as opposed to an emergency hard fork of the kind that split ETH and ETC back in the day, or the kind that would be needed to reverse a hypothetical mass-quantum-theft event. So maybe you could argue it&#39;d be acceptable as long as enough nodes have upgraded by Q-day.


<span
class="q">&gt; This group signature constituted of a merkle tree of signatureswould be attach a &#34;weight&#34; based on the amount PQ signed for the
&gt; coins, and if the &#34;weight&#34; is superior to some threshold, the
&gt; block attaching this special &#34;one-time&#34; group signature would
&gt; a POW ordering bonus and the &#34;tripwire&#34; effect would be attached.
</span>


I think this would also be a hard fork for similar reasons.&#160;


Plus, as you mentioned, we would run the risk of a dishonest minority colluding to trigger the fork early. I especially worry about corporate actors here, who now control a significant fraction of the supply volume, and might have incentive to jump the gun and ossify bitcoin&#39;s cryptography early.


-----


A UASF-like approach is probably the better option here to prevent miner collusion: Perhaps if we distinguish the set of &#34;active&#34; nodes, and write rules that say &#34;if an active node has seen a tripwire proof, they must disregard any blockchain that doesn&#39;t include a tripwire proof&#34;. Maybe you&#39;d call this a &#34;block policy&#34;.


This obviously doesn&#39;t work for nodes doing IBD (the first block after genesis would be considered invalid!) or nodes that come online after sleeping a while (they&#39;d reject the first new block after seeing the tripwire proof!) so there would need to be some means to distinguish those cases from an active synchronized node. Not sure how that&#39;d work.


<span
class="q">&gt; By leveraging the preimage in some ZK-proof of a PQ-safe schemea legitimate coin owner could be able to prove that her or him
&gt; *knew* the discreet log at some point in time of the bitcoin
&gt; blockchain. This knowledge could be leveraged to allow the transfer
&gt; of the coins a posteriori of the &#34;tripwire&#34; lock in function of
&gt; the post-quantum transition policy opt-ed in by the coin owner.
</span>


Are you describing this as a rescue protocol, or a pre-registration protocol? Pre-registration protocols aren&#39;t that useful if we have a rescue protocol, or even just having PQ-safe wallets, because if one can take the proactive measure to pre-register, why not simply move one&#39;s coins to an address that can be rescued later, or better yet to a PQ-secure address?


A rescue protocol on the other hand must assume zero action from the user prior to Q-day (i.e. tripwire activation).&#160;


<span
class="q">&gt; A simple certificate can have a very simple format, e.g:
&gt; 
</span>
<span
class="q">&gt; &lt;1-byte certificate version&gt; &lt;opt-in tripwire lock&gt; &lt;sha256_hash&gt; &lt;signature&gt;
</span>
What is the &#34;opt-in tripwire lock&#34; field here?


<span
class="q">&gt; The scheme is not bulletproof, as we cannot have certainty, _if_ and_when_ a CQRC will appear, however in its simple logic it could be
&gt; done today (it&#39;s like open-timestamp the marginal cost of a certificate
&gt; is very very low, the witness cost only being encumbered at spending).
&gt; This idea only to add more color on the painture pallet of the technical
&gt; optional to protect EC exposed coins.
</span>


This sounds similar to my own&#160;proposal,&#160;DropKick, which is also OTS-like in the way commitments are opened. I&#39;ll open a new thread soon to discuss that :)


regards,
conduition

On Wednesday, August 19th, 2026 at 6:36 PM, Antoine Riard &lt;antoine.riard@gmail&#8226;com&gt; wrote:

<span
class="q">&gt; Hello,
&gt; 
</span>
<span
class="q">&gt; In this post, I&#39;m detailing (a) what could be a solution for
&gt; the game-theory difficulties of the &#34;tripwire&#34; NUMS point and
&gt; (b) a second solution for the exact same problem, relying on
&gt; different assumptions and (c) a variant of a commit/reveal
&gt; rescue protocol for EC coins based on the strict ordering of
&gt; the bitcoin blockchain.
&gt; 
</span>
<span
class="q">&gt; Most of the ideas are &#34;rough&#34; (and maybe a bit heretical...),
&gt; the whole is for putting more tools on the design table, on
&gt; what can be done in the face of CQRC adversarie(s) aiming to
&gt; compromise the chain finality, among other attacks goals.
&gt; 
</span>
<span
class="q">&gt; ## A. NUMS Spend As a Proof of Equivalence of POW
&gt; 
</span>
<span
class="q">&gt; One of the difficulty previously raised with a PQ-flag
&gt; transaction based on a solution to the &#34;tripwire&#34; is the risk
&gt; of &#34;tx-withold&#34; being coordinated by a majority coalition of
&gt; miners eager to exploit EC coins in coordination with a CQRC [0].
&gt; 
</span>
<span
class="q">&gt; There are able to dictate what is the chain state, of which
&gt; the &#34;tripwire&#34; spend must included it to trigger effect, as
&gt; according to Satoshi paper, the &#34;majority decision is represented
&gt; by the longest chain, which has the greatest proof-of-work
&gt; effort invested in it&#34;.
&gt; 
</span>
<span
class="q">&gt; If the coalition has a 51% advantage, or an appromixative
&gt; amount of hashrate using other techniques, they can maintain
&gt; their advantage on what is getting in the chain. No one will
&gt; be able to produce an equivalent amount of proof of _work_.
&gt; 
</span>
<span
class="q">&gt; One way to alleviate the problem would be to consider the
&gt; spent of the NUMS point, that can be a hardcoded value that
&gt; one can commit in a dedicated coinbase output as a &#34;proof of
&gt; work in itself&#34; where the CheckProofOfWOrk() would return true
&gt; for it and the nChainWork of the chain in which the NUMS spent
&gt; is included would get a bonus (e.g *20 the last period&#39;s difficulty).
&gt; 
</span>
<span
class="q">&gt; By introducing an ordering of the chain among network nodes
&gt; based on multiple factors, of which the NUMS spent would be
&gt; a *one-time* accounted for factor, the bar to trigger the
&gt; activation of the effect of the NUMS spent, whatever they are,
&gt; is removed of the assumption of availing the majority of hashrate [1].
&gt; 
</span>
<span
class="q">&gt; All network nodes sharing this consensus mechanism would follow
&gt; the new and same chain ordering, overruling the most proof of
&gt; work ordering.
&gt; 
</span>
<span
class="q">&gt; This approach still raises some problem of its own, as it&#39;s one
&gt; thing to have a &#34;tripwire&#34; NUMS spent that would be part of
&gt; consensus rules, it is still assuming that an entity availing
&gt; a CRQC would produce a proof to activate the &#34;tripwire&#34;.
&gt; 
</span>
<span
class="q">&gt; It can sounds a high bar for the community to assume there will
&gt; be a nice and kind CRQC-capable entity, just right there at the
&gt; corner to produce such a proof, if real-world quantum computer
&gt; ever becomes a reality.
&gt; 
</span>
<span
class="q">&gt; ## B. Group Signatures of PQ Upgraded Coins
&gt; 
</span>
<span
class="q">&gt; An alternative solution not running in the same issue of
&gt; availing a CQRC would be to rely on a group signatures of
&gt; some threshold of PQ upgraded coins, e.g having more their
&gt; coins to some variant of crystal-dilithium, falcon or whatever.
&gt; 
</span>
<span
class="q">&gt; The idea is on the same line than the one previously introduced,
&gt; a novel merkle tree of PQ &#34;blessing&#34; signatures could be added
&gt; in the commitment extension structure of BIP141 (i.e in the
&gt; commitment hash of the coinbase output&#39;s commitment hash).
&gt; 
</span>
<span
class="q">&gt; This group signature constituted of a merkle tree of signatures
&gt; would be attach a &#34;weight&#34; based on the amount PQ signed for the
&gt; coins, and if the &#34;weight&#34; is superior to some threshold, the
&gt; block attaching this special &#34;one-time&#34; group signature would
&gt; a POW ordering bonus and the &#34;tripwire&#34; effect would be attached.
&gt; 
</span>
<span
class="q">&gt; This scheme comes with the advantage of being CRQC-resistant, as
&gt; a CRQC would not be able to forge a signature, without herself
&gt; or himself already availing some significant amount of coins. It
&gt; would be an &#34;indirect oracle&#34; that a CQRC might be active and is
&gt; more robust than the community.
&gt; 
</span>
<span
class="q">&gt; However, this mechanism, a contrario of the NUMS-based can be
&gt; fooled, even in the absence of a CRQC, therefore making it a
&gt; risk of social blackmail (e.g a proof-of-stake majority meeting
&gt; the threshold deciding to activate the &#34;tripwire&#34; to alter the
&gt; conditions of spendability of numerous coins at their advantage).
&gt; 
</span>
<span
class="q">&gt; A two-phase commit &#34;tripwire&#34; protocol could be designed, where
&gt; the &#34;tripwire&#34; effect is only locked-in (somehow in some analogy
&gt; with BIP9 mechanism), if the threshold is not &#34;challenged&#34; by another
&gt; economic group of coins owner during some period (e.g two to three
&gt; months).
&gt; 
</span>
<span
class="q">&gt; ## C. Chain Timestamped Certificate of Discreet Log Knowledge
&gt; 
</span>
<span
class="q">&gt; On the more technical problem of &#34;what can do procrastinators coin
&gt; owners&#34;, one train of solution in the line of the commit-reveal
&gt; protocol that has been previously discussed would be to use the
&gt; chain itself as a publication space of discreet log ownerships.
&gt; 
</span>
<span
class="q">&gt; The problem with a CRQC it&#39;s enabling someone to crack the DL k
&gt; of a point K, where K = k * G, blurring the ability of the coin
&gt; owner to prove she or he is the legitimate owner of the coins,
&gt; EC cryptography being based on the knowledge of a discreet log.
&gt; 
</span>
<span
class="q">&gt; While once a CRQC appears in the wild, it is not possible anymore
&gt; to assume that anyone in knowledge of the discreet log is the
&gt; legitimate owner of the coin, a proof of &#34;knowledge anteriority&#34;
&gt; could be able to break the tie in multiple transactions claiming
&gt; to be the owner of the coin.
&gt; 
</span>
<span
class="q">&gt; A simple certificate can have a very simple format, e.g:
&gt; 
</span>
<span
class="q">&gt; &lt;1-byte certificate version&gt; &lt;opt-in tripwire lock&gt; &lt;sha256_hash&gt; &lt;signature&gt;
&gt; 
</span>
<span
class="q">&gt; Where the &lt;signature&gt; would commit to all the fields of the
&gt; certificates.
&gt; 
</span>
<span
class="q">&gt; By leveraging the preimage in some ZK-proof of a PQ-safe scheme
&gt; a legitimate coin owner could be able to prove that her or him
&gt; *knew* the discreet log at some point in time of the bitcoin
&gt; blockchain. This knowledge could be leveraged to allow the transfer
&gt; of the coins a posteriori of the &#34;tripwire&#34; lock in function of
&gt; the post-quantum transition policy opt-ed in by the coin owner.
&gt; 
</span>
<span
class="q">&gt; One interesting aspect of this scheme is coin owners could start
&gt; for now building merkle tree of coin certificates and commit them
&gt; in the bip141 commitment structure, a magic number op_return or an
&gt; annex, whatever even if the &#34;proving&#34; consensus logic is only added
&gt; in an ulterior soft-fork.
&gt; 
</span>
<span
class="q">&gt; The scheme is not bulletproof, as we cannot have certainty, _if_ and
&gt; _when_ a CQRC will appear, however in its simple logic it could be
&gt; done today (it&#39;s like open-timestamp the marginal cost of a certificate
&gt; is very very low, the witness cost only being encumbered at spending).
&gt; This idea only to add more color on the painture pallet of the technical
&gt; optional to protect EC exposed coins.
&gt; 
</span>
<span
class="q">&gt; Cheers,
&gt; Antoine
&gt; OTS hash: a5a11d42e13724c04d44b953ae5c5f0d152346a7e2041a0a966a62ef148f5ab7
&gt; 
</span>
<span
class="q">&gt; [0] <a
href="https://groups.google.com/g/bitcoindev/c/DEfcMWSdQRY">https://groups.google.com/g/bitcoindev/c/DEfcMWSdQRY</a>
&gt; [1] To facilitate P2P communication and discovery of this
&gt; bloc, the nVersion field of the header could commit to a bit.
&gt; 
</span>
<span
class="q">&gt; --
&gt; You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt; To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
&gt; To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/CALZpt%2BHRNFdtWUpg4v2aj9CRMamS7eG9Nem3mdxJq4sZEtOL6w%40mail.gmail.com">https://groups.google.com/d/msgid/bitcoindev/CALZpt%2BHRNFdtWUpg4v2aj9CRMamS7eG9Nem3mdxJq4sZEtOL6w%40mail.gmail.com</a>.
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/UW5dOJNFjgt67sz-2sRUPeMJi0XL6_wSm7zKCmSoj_8IzkQavc-Vo9vwiR7Tbaz7bvP2YrH8b-1JGm-9jNQXQM8dqsw1f1Sl75SHIOt9cOc%3D%40proton.me">https://groups.google.com/d/msgid/bitcoindev/UW5dOJNFjgt67sz-2sRUPeMJi0XL6_wSm7zKCmSoj_8IzkQavc-Vo9vwiR7Tbaz7bvP2YrH8b-1JGm-9jNQXQM8dqsw1f1Sl75SHIOt9cOc%3D%40proton.me</a>.

<a
href="https://gnusha.org/pi/bitcoindev/UW5dOJNFjgt67sz-2sRUPeMJi0XL6_wSm7zKCmSoj_8IzkQavc-Vo9vwiR7Tbaz7bvP2YrH8b-1JGm-9jNQXQM8dqsw1f1Sl75SHIOt9cOc=@proton.me/1.1.2.1-a.bin">[-- Attachment #1.1.2.1: Type: text/html, Size: 18365 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/UW5dOJNFjgt67sz-2sRUPeMJi0XL6_wSm7zKCmSoj_8IzkQavc-Vo9vwiR7Tbaz7bvP2YrH8b-1JGm-9jNQXQM8dqsw1f1Sl75SHIOt9cOc=@proton.me/1.2-a.bin">[-- Attachment #1.2: publickey - conduition@proton.me - 0x474891AD.asc --]
[-- Type: application/pgp-keys, Size: 649 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/UW5dOJNFjgt67sz-2sRUPeMJi0XL6_wSm7zKCmSoj_8IzkQavc-Vo9vwiR7Tbaz7bvP2YrH8b-1JGm-9jNQXQM8dqsw1f1Sl75SHIOt9cOc=@proton.me/2-signature.asc">[-- Attachment #2: OpenPGP digital signature --]
[-- Type: application/pgp-signature, Size: 343 bytes --]</a>
</pre></div></content></entry><entry><author><name>Antoine Riard</name><email>antoine.riard@gmail.com</email></author><title
type="html">[bitcoindev] post-quantum: solution ideas to &#34;tripwire&#34;game-theory issues + a certificate-based rescue protocol</title><updated>2026-08-19T22:36:48Z</updated><link
href="https://gnusha.org/pi/bitcoindev/CALZpt+HRNFdtWUpg4v2aj9CRMamS7eG9Nem3mdxJq4sZEtOL6w@mail.gmail.com/"/><id>urn:uuid:9bc64123-54ff-d80c-37f8-380f60ae07bf</id><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap"><a
href="https://gnusha.org/pi/bitcoindev/CALZpt+HRNFdtWUpg4v2aj9CRMamS7eG9Nem3mdxJq4sZEtOL6w@mail.gmail.com/1-a.txt">[-- Attachment #1: Type: text/plain, Size: 7222 bytes --]</a>

Hello,

In this post, I&#39;m detailing (a) what could be a solution for
the game-theory difficulties of the &#34;tripwire&#34; NUMS point and
(b) a second solution for the exact same problem, relying on
different assumptions and (c) a variant of a commit/reveal
rescue protocol for EC coins based on the strict ordering of
the bitcoin blockchain.

Most of the ideas are &#34;rough&#34; (and maybe a bit heretical...),
the whole is for putting more tools on the design table, on
what can be done in the face of CQRC adversarie(s) aiming to
compromise the chain finality, among other attacks goals.

## A. NUMS Spend As a Proof of Equivalence of POW

One of the difficulty previously raised with a PQ-flag
transaction based on a solution to the &#34;tripwire&#34; is the risk
of &#34;tx-withold&#34; being coordinated by a majority coalition of
miners eager to exploit EC coins in coordination with a CQRC [0].

There are able to dictate what is the chain state, of which
the &#34;tripwire&#34; spend must included it to trigger effect, as
according to Satoshi paper, the &#34;majority decision is represented
by the longest chain, which has the greatest proof-of-work
effort invested in it&#34;.

If the coalition has a 51% advantage, or an appromixative
amount of hashrate using other techniques, they can maintain
their advantage on what is getting in the chain. No one will
be able to produce an equivalent amount of proof of _work_.

One way to alleviate the problem would be to consider the
spent of the NUMS point, that can be a hardcoded value that
one can commit in a dedicated coinbase output as a &#34;proof of
work in itself&#34; where the CheckProofOfWOrk() would return true
for it and the nChainWork of the chain in which the NUMS spent
is included would get a bonus (e.g *20 the last period&#39;s difficulty).

By introducing an ordering of the chain among network nodes
based on multiple factors, of which the NUMS spent would be
a *one-time* accounted for factor, the bar to trigger the
activation of the effect of the NUMS spent, whatever they are,
is removed of the assumption of availing the majority of hashrate [1].

All network nodes sharing this consensus mechanism would follow
the new and same chain ordering, overruling the most proof of
work ordering.

This approach still raises some problem of its own, as it&#39;s one
thing to have a &#34;tripwire&#34; NUMS spent that would be part of
consensus rules, it is still assuming that an entity availing
a CRQC would produce a proof to activate the &#34;tripwire&#34;.

It can sounds a high bar for the community to assume there will
be a nice and kind CRQC-capable entity, just right there at the
corner to produce such a proof, if real-world quantum computer
ever becomes a reality.

## B. Group Signatures of PQ Upgraded Coins

An alternative solution not running in the same issue of
availing a CQRC would be to rely on a group signatures of
some threshold of PQ upgraded coins, e.g having more their
coins to some variant of crystal-dilithium, falcon or whatever.

The idea is on the same line than the one previously introduced,
a novel merkle tree of PQ &#34;blessing&#34; signatures could be added
in the commitment extension structure of BIP141 (i.e in the
commitment hash of the coinbase output&#39;s commitment hash).

This group signature constituted of a merkle tree of signatures
would be attach a &#34;weight&#34; based on the amount PQ signed for the
coins, and if the &#34;weight&#34; is superior to some threshold, the
block attaching this special &#34;one-time&#34; group signature would
a POW ordering bonus and the &#34;tripwire&#34; effect would be attached.

This scheme comes with the advantage of being CRQC-resistant, as
a CRQC would not be able to forge a signature, without herself
or himself already availing some significant amount of coins. It
would be an &#34;indirect oracle&#34; that a CQRC might be active and is
more robust than the community.

However, this mechanism, a contrario of the NUMS-based can be
fooled, even in the absence of a CRQC, therefore making it a
risk of social blackmail (e.g a proof-of-stake majority meeting
the threshold deciding to activate the &#34;tripwire&#34; to alter the
conditions of spendability of numerous coins at their advantage).

A two-phase commit &#34;tripwire&#34; protocol could be designed, where
the &#34;tripwire&#34; effect is only locked-in (somehow in some analogy
with BIP9 mechanism), if the threshold is not &#34;challenged&#34; by another
economic group of coins owner during some period (e.g two to three
months).

## C. Chain Timestamped Certificate of Discreet Log Knowledge

On the more technical problem of &#34;what can do procrastinators coin
owners&#34;, one train of solution in the line of the commit-reveal
protocol that has been previously discussed would be to use the
chain itself as a publication space of discreet log ownerships.

The problem with a CRQC it&#39;s enabling someone to crack the DL k
of a point K, where K = k * G, blurring the ability of the coin
owner to prove she or he is the legitimate owner of the coins,
EC cryptography being based on the knowledge of a discreet log.

While once a CRQC appears in the wild, it is not possible anymore
to assume that anyone in knowledge of the discreet log is the
legitimate owner of the coin, a proof of &#34;knowledge anteriority&#34;
could be able to break the tie in multiple transactions claiming
to be the owner of the coin.

A simple certificate can have a very simple format, e.g:

&lt;1-byte certificate version&gt; &lt;opt-in tripwire lock&gt; &lt;sha256_hash&gt;
&lt;signature&gt;

Where the &lt;signature&gt; would commit to all the fields of the
certificates.

By leveraging the preimage in some ZK-proof of a PQ-safe scheme
a legitimate coin owner could be able to prove that her or him
*knew* the discreet log at some point in time of the bitcoin
blockchain. This knowledge could be leveraged to allow the transfer
of the coins a posteriori of the &#34;tripwire&#34; lock in function of
the post-quantum transition policy opt-ed in by the coin owner.

One interesting aspect of this scheme is coin owners could start
for now building merkle tree of coin certificates and commit them
in the bip141 commitment structure, a magic number op_return or an
annex, whatever even if the &#34;proving&#34; consensus logic is only added
in an ulterior soft-fork.

The scheme is not bulletproof, as we cannot have certainty, _if_ and
_when_ a CQRC will appear, however in its simple logic it could be
done today (it&#39;s like open-timestamp the marginal cost of a certificate
is very very low, the witness cost only being encumbered at spending).
This idea only to add more color on the painture pallet of the technical
optional to protect EC exposed coins.

Cheers,
Antoine
OTS hash: a5a11d42e13724c04d44b953ae5c5f0d152346a7e2041a0a966a62ef148f5ab7

[0] <a
href="https://groups.google.com/g/bitcoindev/c/DEfcMWSdQRY">https://groups.google.com/g/bitcoindev/c/DEfcMWSdQRY</a>
[1] To facilitate P2P communication and discovery of this
bloc, the nVersion field of the header could commit to a bit.

-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/CALZpt%2BHRNFdtWUpg4v2aj9CRMamS7eG9Nem3mdxJq4sZEtOL6w%40mail.gmail.com">https://groups.google.com/d/msgid/bitcoindev/CALZpt%2BHRNFdtWUpg4v2aj9CRMamS7eG9Nem3mdxJq4sZEtOL6w%40mail.gmail.com</a>.

<a
href="https://gnusha.org/pi/bitcoindev/CALZpt+HRNFdtWUpg4v2aj9CRMamS7eG9Nem3mdxJq4sZEtOL6w@mail.gmail.com/2-a.bin">[-- Attachment #2: Type: text/html, Size: 8315 bytes --]</a>
</pre></div></content></entry><entry><author><name>Pieter Wuille</name><email>bitcoin-dev@wuille.net</email></author><title>Re: [bitcoindev] Giving teeth to expected EC disabling: P2XX(-T)(-ML)</title><updated>2026-08-19T22:18:53Z</updated><link
href="https://gnusha.org/pi/bitcoindev/Bx0LA0afwRjPIcEol98t7ztodzX7mIBeA1kGLV-rAicu4IuGBkME3A-UzBC5KJOawIciVn1CW3bCILlyVpMJU_MAgqV5OBjSFQiZrX60fb4=@wuille.net/"/><id>urn:uuid:ab78ee1e-9603-5126-dcb3-46fd9b198a09</id><thr:in-reply-to
ref="urn:uuid:b75d9703-91da-ddf4-51b1-1fe50ffa2657"
href="https://gnusha.org/pi/bitcoindev/FhcVTVM6flM4OpPCZpaGbC3msQG9kG48uvyz6T4qdNv8iAq-clhoMmNmRWSSWs78hug3KZSsKG3Mi2lZIzo5PFY-WvbvxdA0Ssj-G2HCz2o=@proton.me/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">Hi,&#160;

On Tuesday, August 18th, 2026 at 10:32 PM, conduition &lt;conduition@proton&#8226;me&gt; wrote:

<span
class="q">&gt; Oh I misunderstood. So to be clear, a &#34;canary&#34; is just a social signal that should push consensus to activate a soft fork, whereas a &#34;tripwire&#34; is an unattended system that automatically triggers a change to consensus rules.
</span>
I like that terminology.

<span
class="q">&gt; &gt; While it&#39;s certainly possible it&#39;s actually triggered by a cooperative CRQC, that&#39;s not how I expect ECC disabling to happen (instead I expect a community consensus-changing effort, effected through Miner Lockdown or otherwise). The Tripwire just sets an unambiguous expectation that disabling is intended by Q-day.
&gt; 
&gt; In the absence of evidence, I expect this fork to be highly contentious or delayed until hard evidence is available.
</span>
I don&#39;t disagree, but I also do expect hard evidence to become available, unless we&#39;re actually taking about scenario where a CRQC appears out of nowhere, and in that case there are really no good outcomes.

<span
class="q">&gt; I agree but for a different reason on top. Given the polynomial efficiency of Shor, and the massive time/money investment needed to build quantum computers, we have no reason to expect anyone will build a QC that can break 192-bit curves but not&#160;256-bit curves. There is actually incentive not&#160;to do so, especially if breaking a 192-bit curve will cause the Bitcoin network (the most ripe target to pay off QC investors) to react by locking itself down.&#160;
&gt; Think of it this way: If you have the mans to build a stable 900 logical-qubit quantum-computer, why not spend the extra time and money to build a 1200 logical-qubit quantum computer? Is a 1.5x factor improvement really so hard at this point? If you do expend the effort, then at least you stand a chance to make some money (e.g. by decrypting old internet traffic on behalf of the NSA).
</span>
You seem to be talking about an adversarial CRQC here? Those won&#39;t trigger any tripwire, nor publish any canaries.

There is a pretty weird philosophical point here: as far as I&#39;m aware, at this point, there isn&#39;t really any application for CRQC-capable hardware except breaking classical cryptography. So beyond scientific curiosity, the only incentive to build one is either adversarial, or to prove it&#39;s possible to build one before one lands in adversarial hands. And the better migrated the world is (including Bitcoin...) for PQC, the lower the incentives for both get.

<span
class="q">&gt; I think I&#39;m coming to the conclusion that a 256-bit ST-ECDLP tripwire is the way to go, because at least then the canary is unambiguously dead, and it&#39;s time to stop using secp256k1, whereas 192-bit curves leave a shred of doubt.
</span>
Agreed.

<span
class="q">&gt; Really interesting idea there. Small correction: I believe Shor&#39;s space (qubit) requirements are dominated primarily by the group order that we are searching for the dlog within, not by the size of the field used for the the elliptic curve group operation. I&#39;m pretty sure the field size would affect runtime complexity (gate count), but not qubit count requirements. (Happy to be corrected). If I&#39;m correct, a group order of approx 2^187 would need approx 842 qubits (at least) to break.
</span>
My friendly neighborhood LLM believes the qubit count is primarily a function of the field size (to represent curve coordinates), while the gate count grows with larger with the group (because point multiplication needs more additions), but I am by no means an expert.

<span
class="q">&gt; Still, as previously discussed, I&#39;m unsure if a canary which is only slightly&#160;harder to break would be meaningful. It&#39;d be nice if we could find some problem which quantum computers of, say, 150 qubits could do, but which classical computers cannot (feasibly) solve. Then we might have a reasonably predictive canary which could be solved by cooperative.
</span>
Agreed.

<span
class="q">&gt; &gt; From a simplicity standpoint, I think just having a &#34;a UTXO with scriptPubKey X is spent&#34; is ideal, because it reuses all existing block and transaction validation logic, and just adds a trivial trigger.
&gt; 
&gt; I would like to make a case that we should expend the extra effort and not bind the canary to a specific UTXO. I will point to Antoine&#39;s game theory arguments about reorgs and miner collusion with CRQCs.&#160;
&gt; 
&gt; If we tie the canary to a specific UTXO, or even to any UTXO with a specific script, then this makes miner censorship of the canary proof very easy: Just block spends of that UTXO (or of any UTXO unlocking the chosen script).
</span>
I hadn&#39;t considered that. But if miners are actively blocking a security feature (as this effectively is), I think we&#39;re in UASF territory already.

<span
class="q">&gt; If, on the other hand, we had nodes check something almost as simple, like for example &#34;check every 32-byte OP_RETURN to see if it happens to be the dlog of the NUMS point&#34;, then any user can choose to include the proof in their transactions at relatively little cost. Any miners who want to censor the canary proof will have to also censor any such transactions, and so they lose out on the potential fee revenue of the entire TX by doing so.
</span>
I think this is pretty unrealistic. Most user software won&#39;t have the ability to include a tripwire in an OP_RETURN (this includes all kinds of higher-level / layer-two constructions that need cooperation to build transactions). It further also relies on this happening at a time when fee income is substantial.

<span
class="q">&gt; I&#39;m not sure if this incentive is meaningful when compared to the potential bribes that a miner could be offered by a CRQC, but still it is worth considering. It does have the down side that it will slow down block validation slightly (one EC mult per 32-byte OP_RETURN). Maybe this could be accounted for somehow in the sigops budget?
</span>
Yeah, these concerns are why I like just triggering on a scriptPubKey, because all cost accounting is dealt with already. That said, I don&#39;t think this is a particularly strong point; if there are good reasons to do the trigger through an OP_RETURN, there are probably fairly easy ways of doing that too.

On Wednesday, August 19th, 2026 at 11:36 AM, waxwing/ AdamISZ &lt;ekaggata@gmail&#8226;com&gt; wrote:

<span
class="q">&gt; Smaller group *canaries* (not tripwires) are still interesting I think. Not amazing, but maybe quite valuable.
</span>
Agreed. I think formalized or not, this will effectively be how the ecosystem decides it&#39;s time to disable ECC.

<span
class="q">&gt; Good point about signature, I wasn&#39;t considering that, earlier. If you publish (R, s) with truly random R=kG choice you are not leaking more than what already existed with the pubkey H; that&#39;s true if HVZK holds and assuming the ROM (except it has to be &#34;QROM&#34; now, right).
</span>
Right.

<span
class="q">&gt; However! There might be a non-technical reason to avoid H directly: it&#39;s a bit like toxic waste in powers-of-tau and similar: suppose a whitehat organization is targeting a tripwire. If that dlog knowledge is exposed (in the process of creating a valid signature) it has to be destroyed &#34;trustfully&#34;, since it&#39;ll allow spending of all kinds of coins[1]. This comment is only relevant of course if there is a CRQC which costs 2 months and $100m to run, if it&#39;s easy to find a specific dlog whenever, then nothing to talk about.
&gt; 
&gt; So yeah I would go with the abundance of caution, myself; don&#39;t see how it hurts.
</span>
Yeah.

I think the important choice is whether to cater to adversarially-constructed proofs or not. I believe we should not, but:

If yes: use AJ&#39;s construction of providing BIP-340 signature on point of the form rG+H with arbitrary r, and arbitrary message. This is incompatible with using UTXO trigger, and needs H (or derivation from H).

If no: no reason to specifically use H, or even support multiple targets. Just pick an &#34;as random as possible&#34; fixed point, are require spending a scriptPubKey with it, or publishing its DLP, or publishing a signature for it.

Cheers,

-- 
Pieter

-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/Bx0LA0afwRjPIcEol98t7ztodzX7mIBeA1kGLV-rAicu4IuGBkME3A-UzBC5KJOawIciVn1CW3bCILlyVpMJU_MAgqV5OBjSFQiZrX60fb4%3D%40wuille.net">https://groups.google.com/d/msgid/bitcoindev/Bx0LA0afwRjPIcEol98t7ztodzX7mIBeA1kGLV-rAicu4IuGBkME3A-UzBC5KJOawIciVn1CW3bCILlyVpMJU_MAgqV5OBjSFQiZrX60fb4%3D%40wuille.net</a>.

</pre></div></content></entry><entry><author><name>waxwing/ AdamISZ</name><email>ekaggata@gmail.com</email></author><title>Re: [bitcoindev] Giving teeth to expected EC disabling: P2XX(-T)(-ML)</title><updated>2026-08-19T15:36:12Z</updated><link
href="https://gnusha.org/pi/bitcoindev/baff534c-a392-4af7-8264-998c3390fe84n@googlegroups.com/"/><id>urn:uuid:ef293ee0-d339-f1ec-a2c0-53331eb9ac14</id><thr:in-reply-to
ref="urn:uuid:b75d9703-91da-ddf4-51b1-1fe50ffa2657"
href="https://gnusha.org/pi/bitcoindev/FhcVTVM6flM4OpPCZpaGbC3msQG9kG48uvyz6T4qdNv8iAq-clhoMmNmRWSSWs78hug3KZSsKG3Mi2lZIzo5PFY-WvbvxdA0Ssj-G2HCz2o=@proton.me/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/baff534c-a392-4af7-8264-998c3390fe84n@googlegroups.com/1.1-a.txt">[-- Attachment #1.1: Type: text/plain, Size: 17041 bytes --]</a>

Hi conduition,

<span
class="q">&gt; Given the polynomial efficiency of Shor, and the massive time/money 
</span>investment needed to build quantum computers, we have no reason to expect 
anyone will build a QC that can break 192-bit curves but *not* 256-bit 
curves. There is actually incentive *not* to do so, especially if breaking 
a 192-bit curve will cause the Bitcoin network (the most ripe target to pay 
off QC investors) to react by locking itself down. 

Well, but this brings me right back to my first comment here (not that it 
is *my* comment, it&#39;s been said elsewhere in thread): this tripwire concept 
is not a defence against an adversary, right; if the first QC is expensive 
and difficult (likely), and if they decide to be adversarial, they won&#39;t be 
tripping any wires. But surely it follows, that they have just as much 
incentive to not trip the 256 wire as the 192 wire.

Anyway I will try to now avoid further nerd sniping (including against 
myself) talking about smaller order curves; I do agree with the points 
raised, that it&#39;s not a sufficiently practical idea (given secp256k1&#39;s most 
excellent property, its cofactor of 1, is extremely unhelpful in this 
particular case! - therefore nice idea, Pieter, with the &#39;algebraically 
similar curve but with subgroups&#39;, but I&#39;m willing to bet you&#39;re right that 
that doesn&#39;t cut it, either) on more than one axis.

Smaller group *canaries* (not tripwires) are still interesting I think. Not 
amazing, but maybe quite valuable.

<span
class="q">&gt; Also found this related paper which proposes an incremental ladder of 
</span>canaries using NUMS points on a sequence of curves of increasing size: 
<a
href="https://arxiv.org/pdf/2508.14011">https://arxiv.org/pdf/2508.14011</a>

interesting find, thanks!

<span
class="q">&gt; If, on the other hand, we had nodes check something almost as simple, 
</span>like for example &#34;check every 32-byte OP_RETURN to see if it happens to be 
the dlog of the NUMS point&#34;, then any user can choose to include the proof 
in their transactions at relatively little cost. Any miners who want to 
censor the canary proof will have to also censor any such transactions, and 
so they lose out on the potential fee revenue of the entire TX by doing so.

Yes that does seem to be better than single utxo. But perhaps the 
difference isn&#39;t that significant in practice?

<span
class="q">&gt; I&#39;m not sure if this incentive is meaningful when compared to the 
</span>potential bribes that a miner could be offered by a CRQC, but still it is 
worth considering. It does have the down side that it will slow down block 
validation slightly (one EC mult per 32-byte OP_RETURN). Maybe this could 
be accounted for somehow in the sigops budget?

I agree it doesn&#39;t seem very reasonable that there&#39;s a way to counter such 
a huge incentive in *a* miner as one related to a QC break.

It also makes me think: that&#39;s not how consensus changes usually work, eh. 
Giving miners the ability to censor an update seems antithetical. It&#39;s also 
weirdly the opposite shape to what you want: it activates with the 
permission of 1 of N miners (weighted by hashrate), which means it&#39;s kind 
of guaranteed to occur once the proof exists, but could be quite slow. The 
counterargument might be: that&#39;s not going to happen! Once the proof is 
public, a miner deliberately not mining it is very transparently a bad 
actor. Not sure. Seems a bit wobbly but not crazy.

Pieter,
<span
class="q">&gt; Regarding using the BIP-341 H itself as canary, I don&#39;t think that&#39;s a 
</span>problem if the ECDLP break proof is a Schnorr signature (as opposed to 
revealing the DLP itself). But it also makes sense to be as conservative as 
possible here; it may make sense to make a selection of hash functions, 
feed them all as much input as possible (the genesis block is a good idea, 
the existing generator G, maybe a block hash from a time when the 
activation parameters are decided, or even a block hash when the block goes 
live as suggested by Tadge though that adds hash-to-curve logic to 
consensus too), and then XOR (or hash) all hash results together.

Good point about signature, I wasn&#39;t considering that, earlier. If you 
publish (R, s) with truly random R=kG choice you are not leaking more than 
what already existed with the pubkey H; that&#39;s true if HVZK holds and 
assuming the ROM (except it has to be &#34;QROM&#34; now, right).

However! There might be a non-technical reason to avoid H directly: it&#39;s a 
bit like toxic waste in powers-of-tau and similar: suppose a whitehat 
organization is targeting a tripwire. If that dlog knowledge is exposed (in 
the process of creating a valid signature) it has to be destroyed 
&#34;trustfully&#34;, since it&#39;ll allow spending of all kinds of coins[1]. This 
comment is only relevant of course if there is a CRQC which costs 2 months 
and $100m to run, if it&#39;s easy to find a specific dlog whenever, then 
nothing to talk about.

So yeah I would go with the abundance of caution, myself; don&#39;t see how it 
hurts.

[1] Uh not actually sure about that. There was a +rG tweak suggested in 
BIP341 for better privacy. Don&#39;t know how widely it was used (curious, in 
codebases I looked at, it wasn&#39;t). Silent Payments BIP352 explicitly carves 
out H which, I dunno if that proves anything, but it&#39;s an example of people 
tacitly assuming no tweaking happens. If the tweaking was used it would at 
least limit how much risk exists with H, though not remove it.

On Tuesday, August 18, 2026 at 8:37:02&#8239;PM UTC-6 conduition wrote:

<span
class="q">&gt; Oh wait, it&#39;s much simpler (not perhaps in character, but concretely): we 
&gt; don&#39;t need to talk about some general ZKP system here, right. If we all 
&gt; agree on a 192 bit curve, and a NUMS point on that curve, then in the 
&gt; OP_RETURN (say), we just need to put the point&#39;s dlog and consensus nodes 
&gt; only have to do a single scalar multiplication on that curve to verify.
&gt;
&gt; Exactly. Also, the canary proof need not be the NUMS discrete log itself, 
&gt; it could also be a signature proving knowledge of the dlog without 
&gt; revealing it outright. Dlog exposure is simpler and faster to verify; 
&gt; Signature allows the first QC to identify itself later. (IDK if useful)
&gt;
&gt;
&gt; Right, so: the QCAP thread was about a canary rather than a full tripwire
&gt;
&gt; Oh I misunderstood. So to be clear, a &#34;canary&#34; is just a social signal 
&gt; that should push consensus to activate a soft fork, whereas a &#34;tripwire&#34; is 
&gt; an unattended system that automatically triggers a change to consensus 
&gt; rules.
&gt;
&gt; While it&#39;s certainly possible it&#39;s actually triggered by a cooperative 
&gt; CRQC, that&#39;s not how I expect ECC disabling to happen (instead I expect a 
&gt; community consensus-changing effort, effected through Miner Lockdown or 
&gt; otherwise). The Tripwire just sets an unambiguous expectation that 
&gt; disabling is intended by Q-day.
&gt;
&gt; In the absence of evidence, I expect this fork to be highly contentious or 
&gt; delayed until hard evidence is available. 
&gt;
&gt; I don&#39;t think the presence of a 192-bit canary changes this expectation 
&gt; much. 192-bit ECDLP broken (or breakable) is certainly a legitimate reason 
&gt; for panic, but nothing prevents that information from being used at the 
&gt; human layer without it needing to have been part of consensus rules.
&gt;
&gt;
&gt; I agree but for a different reason on top. Given the polynomial efficiency 
&gt; of Shor, and the massive time/money investment needed to build quantum 
&gt; computers, we have no reason to expect anyone will build a QC that can 
&gt; break 192-bit curves but *not* 256-bit curves. There is actually 
&gt; incentive *not* to do so, especially if breaking a 192-bit curve will 
&gt; cause the Bitcoin network (the most ripe target to pay off QC investors) to 
&gt; react by locking itself down. 
&gt; Think of it this way: If you have the mans to build a stable 900 
&gt; logical-qubit quantum-computer, why not spend the extra time and money to 
&gt; build a 1200 logical-qubit quantum computer? Is a 1.5x factor improvement 
&gt; really so hard at this point? If you do expend the effort, then at least 
&gt; you stand a chance to make some money (e.g. by decrypting old internet 
&gt; traffic on behalf of the NSA).
&gt; From the google paper:
&gt;
&gt; Given broad progress across multiple hardware architectures, the safe assumption 
&gt; is that there may be little time between the breaking of 256-bit ECDLP and 
&gt; the breaking of 1024-bit ECDLP.
&gt;
&gt; I think I&#39;m coming to the conclusion that a 256-bit ST-ECDLP tripwire is 
&gt; the way to go, because at least then the canary is unambiguously dead, and 
&gt; it&#39;s time to stop using secp256k1, whereas 192-bit curves leave a shred of 
&gt; doubt.
&gt;
&gt; This makes me wonder about using a subgroup of a very related curve: for 
&gt; example y^2 = x^3 + 3 (mod 2^256-2^32-977) has a subgroup of order 
&gt; ~2^187.11, which would use all the same finite field arithmetic and almost 
&gt; the same multiplication logic (only doubling is affected). Keeping the 
&gt; field modulus the same does mean the q-bit count is unaffected though, only 
&gt; the gate count decreases (proportional to logarithm of group order). Like 
&gt; other weaker-curve constructions, I don&#39;t think this is worth it, but want 
&gt; to throw the idea out there.
&gt;
&gt;
&gt; Really interesting idea there. Small correction: I believe Shor&#39;s space 
&gt; (qubit) requirements are dominated primarily by the group order that we are 
&gt; searching for the dlog within, not by the size of the field used for the 
&gt; the elliptic curve group operation. I&#39;m pretty sure the field size would 
&gt; affect runtime complexity (gate count), but not qubit count requirements. 
&gt; (Happy to be corrected). If I&#39;m correct, a group order of approx 2^187 
&gt; would need approx 842 qubits (at least) to break.
&gt;
&gt; Still, as previously discussed, I&#39;m unsure if a canary which is only 
&gt; *slightly* harder to break would be meaningful. It&#39;d be nice if we could 
&gt; find some problem which quantum computers of, say, 150 qubits could do, but 
&gt; which classical computers cannot (feasibly) solve. Then we might have a 
&gt; reasonably predictive canary which could be solved by cooperative.
&gt;
&gt; Also found this related paper which proposes an incremental ladder of 
&gt; canaries using NUMS points on a sequence of curves of increasing size: 
&gt; <a
href="https://arxiv.org/pdf/2508.14011">https://arxiv.org/pdf/2508.14011</a>
&gt;
&gt; I also don&#39;t think optimizing for multi-target ECDLP adds much.
&gt;
&gt;
&gt; Strongly agree.
&gt;
&gt; From a simplicity standpoint, I think just having a &#34;a UTXO with 
&gt; scriptPubKey X is spent&#34; is ideal, because it reuses all existing block and 
&gt; transaction validation logic, and just adds a trivial trigger.
&gt;
&gt;
&gt; I would like to make a case that we should expend the extra effort and not 
&gt; bind the canary to a specific UTXO. I will point to Antoine&#39;s game theory 
&gt; arguments about reorgs and miner collusion with CRQCs. 
&gt;
&gt; If we tie the canary to a specific UTXO, or even to any UTXO with a 
&gt; specific script, then this makes miner censorship of the canary proof very 
&gt; easy: Just block spends of that UTXO (or of any UTXO unlocking the chosen 
&gt; script).
&gt;
&gt; If, on the other hand, we had nodes check something almost as simple, like 
&gt; for example &#34;check every 32-byte OP_RETURN to see if it happens to be the 
&gt; dlog of the NUMS point&#34;, then any user can choose to include the proof in 
&gt; their transactions at relatively little cost. Any miners who want to censor 
&gt; the canary proof will have to also censor any such transactions, and so 
&gt; they lose out on the potential fee revenue of the entire TX by doing so.
&gt;
&gt; In the extreme case, if every transaction in the mempool contained the 
&gt; canary proof as an OP_RETURN, then censoring miners would receive no fee 
&gt; revenue at all - they would have to mine empty blocks.
&gt;
&gt; I&#39;m not sure if this incentive is meaningful when compared to the 
&gt; potential bribes that a miner could be offered by a CRQC, but still it is 
&gt; worth considering. It does have the down side that it will slow down block 
&gt; validation slightly (one EC mult per 32-byte OP_RETURN). Maybe this could 
&gt; be accounted for somehow in the sigops budget?
&gt;
&gt; regards,
&gt; conduition
&gt;
&gt;
&gt; On Tuesday, August 18th, 2026 at 1:30 PM, Pieter Wuille 
&gt; bitco...@wuille&#8226;net wrote:
&gt;
&gt; Hi all,
&gt;
&gt; I&#39;m unconvinced the complexity of a 192-bit canary is worth it. Picking a 
&gt; curve and a NUMS point on it are not hard, but very little of 
&gt; libsecp256k1&#39;s code can be reused (even field arithmetic is optimized 
&gt; specifically for the secp256k1 prime). A more generic implementation is 
&gt; possible of course, but it&#39;s still a pretty big piece of engineering for 
&gt; what is IMO very little gain.
&gt;
&gt; There is a pretty fundamental difference between a secp256k1 Tripwire and 
&gt; a canary for weaker curves, in that the former isn&#39;t intended to be 
&gt; predictive. Its purpose is setting a codified upper bound on when ECC 
&gt; (within PQC output types) is expected to be disabled. While it&#39;s certainly 
&gt; possible it&#39;s actually triggered by a cooperative CRQC, that&#39;s not how I 
&gt; expect ECC disabling to happen (instead I expect a community 
&gt; consensus-changing effort, effected through Miner Lockdown or otherwise). 
&gt; The Tripwire just sets an unambiguous expectation that disabling is 
&gt; intended by Q-day.
&gt;
&gt; I don&#39;t think the presence of a 192-bit canary changes this expectation 
&gt; much. 192-bit ECDLP broken (or breakable) is certainly a legitimate reason 
&gt; for panic, but nothing prevents that information from being used at the 
&gt; human layer without it needing to have been part of consensus rules.
&gt;
&gt; Relatedly, something I don&#39;t know is how &#34;similar&#34; a canary needs to be to 
&gt; the real secp256k1 ECDLP for people to bother building/programming/running 
&gt; a QC for it. This is of course a question that exists for secp256k1 itself: 
&gt; whether a *cooperative* entity with the capability of building a 
&gt; secp256k1-ECDLP QRQC would bother doing so. But it&#39;s even more tenuous for 
&gt; weaker problems, if they&#39;re not so much weaker that they&#39;re trivial. This 
&gt; makes me wonder about using a subgroup of a very related curve: for example 
&gt; y^2 = x^3 + 3 (mod 2^256-2^32-977) has a subgroup of order ~2^187.11, which 
&gt; would use all the same finite field arithmetic and almost the same 
&gt; multiplication logic (only doubling is affected). Keeping the field modulus 
&gt; the same does mean the q-bit count is unaffected though, only the gate 
&gt; count decreases (proportional to logarithm of group order). Like other 
&gt; weaker-curve constructions, I don&#39;t think this is worth it, but want to 
&gt; throw the idea out there.
&gt;
&gt; I also don&#39;t think optimizing for multi-target ECDLP adds much. My 
&gt; understanding is that Shor&#39;s doesn&#39;t benefit from multiple targets? I&#39;m not 
&gt; opposed to giving freedom of finding (m,x) such that H(m) = x*G, but I 
&gt; don&#39;t see why that would encourage a cooperative CRQC to work on breaking 
&gt; it.
&gt;
&gt; Regarding using the BIP-341 H itself as canary, I don&#39;t think that&#39;s a 
&gt; problem if the ECDLP break proof is a Schnorr signature (as opposed to 
&gt; revealing the DLP itself). But it also makes sense to be as conservative as 
&gt; possible here; it may make sense to make a selection of hash functions, 
&gt; feed them all as much input as possible (the genesis block is a good idea, 
&gt; the existing generator G, maybe a block hash from a time when the 
&gt; activation parameters are decided, or even a block hash when the block goes 
&gt; live as suggested by Tadge though that adds hash-to-curve logic to 
&gt; consensus too), and then XOR (or hash) all hash results together.
&gt;
&gt; From a simplicity standpoint, I think just having a &#34;a UTXO with 
&gt; scriptPubKey X is spent&#34; is ideal, because it reuses all existing block and 
&gt; transaction validation logic, and just adds a trivial trigger. It&#39;s not 
&gt; compatible with any weaker curve construction of course, or with AJ&#39;s 
&gt; H-dependent DLP proof which could enlist non-cooperative CRQC, but I don&#39;t 
&gt; think that&#39;s worth complicating matters for.
&gt;
&gt; Cheers,
&gt;
&gt; --
&gt; Pieter
&gt;
&gt; --
&gt;
&gt;
&gt; You received this message because you are subscribed to a topic in the 
&gt; Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt; To unsubscribe from this topic, visit 
&gt; <a
href="https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe">https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe</a>.
&gt; To unsubscribe from this group and all its topics, send an email to 
&gt; bitcoindev+...@googlegroups&#8226;com.
&gt;
&gt; To view this discussion visit 
&gt; <a
href="https://groups.google.com/d/msgid/bitcoindev/td8wPWxRVg0rQIdP41uibTvWuIoCvGYpvfX022TaDurf-qu1TMm1TmWogw-JTs4C7Mt-97cvJCBW66z4g-Vc2fsSoo-Qxfm8Lcnd384Uink%3D%40wuille.net">https://groups.google.com/d/msgid/bitcoindev/td8wPWxRVg0rQIdP41uibTvWuIoCvGYpvfX022TaDurf-qu1TMm1TmWogw-JTs4C7Mt-97cvJCBW66z4g-Vc2fsSoo-Qxfm8Lcnd384Uink%3D%40wuille.net</a>
&gt; .
&gt;
&gt;
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/baff534c-a392-4af7-8264-998c3390fe84n%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/baff534c-a392-4af7-8264-998c3390fe84n%40googlegroups.com</a>.

<a
href="https://gnusha.org/pi/bitcoindev/baff534c-a392-4af7-8264-998c3390fe84n@googlegroups.com/1.2-a.bin">[-- Attachment #1.2: Type: text/html, Size: 26270 bytes --]</a>
</pre></div></content></entry><entry><author><name>b10c</name><email>0xb10c@gmail.com</email></author><title>[bitcoindev] Re: [BIP Proposal] Anti-Fee-Sniping with LockTime</title><updated>2026-08-19T13:34:13Z</updated><link
href="https://gnusha.org/pi/bitcoindev/2b19cd5e-84aa-4779-b1a6-490cc918cc52n@googlegroups.com/"/><id>urn:uuid:5afdbf42-0517-fd0f-9840-b40d2b2c527a</id><thr:in-reply-to
ref="urn:uuid:d9116ae7-b9b7-85e0-9cce-8f168eed7743"
href="https://gnusha.org/pi/bitcoindev/wWGWjMw9TI22vp4VzCm4xJJS3IGA1UhndMKynUkB04BqeoRjhe-QbDbJU-GMQq0nnOnXuB__u8KcdIcxU5i8Cy9pbTbtJ7Hi583FzLVojek=@pm.me/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/2b19cd5e-84aa-4779-b1a6-490cc918cc52n@googlegroups.com/1.1-a.txt">[-- Attachment #1.1: Type: text/plain, Size: 3239 bytes --]</a>

Hi nervana21,

some comments in random order on the BIP proposal and Anti-Fee-Sniping:

- You mention BIP125 a couple of times in Specification. Note that in 
recent versions of Bitcoin Core, BIP125 signaling is no longer required for 
a transaction to be replaceable under the default mempool policy.
- While the 10%-back-date-rule in Anti-Fee-Sniping is a privacy feature for 
some people, it is also a privacy leak for others: <a
href="https://github.com/bitcoin/bitcoin/issues/26526:">https://github.com/bitcoin/bitcoin/issues/26526:</a> 
When fee-bumping a previously not back-date transaction, Bitcoin Core might 
back-date the replacement. This is fingerprint that you likely back-dated 
the replacement transaction. There is 
also <a
href="https://github.com/bitcoin/bitcoin/issues/26527">https://github.com/bitcoin/bitcoin/issues/26527</a>, which I&#39;m not sure if 
it&#39;s an actual problem or not (haven&#39;t had the time to double-check). Maybe 
documenting some of these edge-cases in the BIP makes sense. This allows 
potential future/other implementations not to make similar mistakes.
- There has been a case where the trying to do Anti-Fee-Sniping 1) wasn&#39;t 
implemented properly in a wallet so it didn&#39;t work 2) ended up being a 
clear fingerprint for this wallet: <a
href="https://b10c.me/observations/01-locktime-stairs/">https://b10c.me/observations/01-locktime-stairs/</a>. 
By now, this wallet doesn&#39;t have much usage anymore 
(<a
href="https://mainnet.observer/charts/transactions-not-enforced-locktime/">https://mainnet.observer/charts/transactions-not-enforced-locktime/</a>) but 
this still shows some of it&#39;s pitfalls. 
- Note that currently only around 5% of the transactions set a heigt-based 
time-lock: <a
href="https://mainnet.observer/charts/transactions-height-based-locktime/">https://mainnet.observer/charts/transactions-height-based-locktime/</a> 
- growing this anonymity set might be interesting to some wallets, but 
currently, do don&#39;t stick out if you don&#39;t do Anti-Fee-Sniping (or use 
locktime).

Best
b10c
On Tuesday, 18 August 2026 at 11:17:44 UTC+2 nervana21 wrote:

<span
class="q">&gt; Hello all,
&gt;
&gt; Anti-fee-sniping with nLockTime has been present in Bitcoin Core since
&gt; 2014 and in Electrum since 2017. BIP326 assumes this nLockTime behavior
&gt; as the baseline and uses nSequence instead for some taproot spends.
&gt; However, the nLockTime rules themselves were never specified in a BIP.
&gt;
&gt;
&gt; <a
href="https://github.com/nervana21/bips/blob/anti-fee-snipe/bip-anti-fee-sniping-with-locktime.md">https://github.com/nervana21/bips/blob/anti-fee-snipe/bip-anti-fee-sniping-with-locktime.md</a>
&gt;
&gt; The BIP draft follows Bitcoin Core&#39;s DiscourageFeeSniping and
&gt; IsCurrentForAntiFeeSniping functions. nLockTime is set to the current tip 
&gt; height.
&gt; With probability 10%, a uniform random integer in 0..99 is subtracted
&gt; and the result is clamped at 0. A locktime equal to the tip height
&gt; cannot be included in a remine of the tip. An older locktime chosen on
&gt; the privacy branch can. nLockTime is set to 0 during initial block
&gt; download or when the tip is more than 8 hours old. The policy is not
&gt; applied when nLockTime is already set or when any input already has a
&gt; preset nSequence. Test vectors are included.
&gt;
&gt; Constructive criticism is greatly appreciated.
&gt;
&gt; Cheers,
&gt; nervana21
&gt;
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/2b19cd5e-84aa-4779-b1a6-490cc918cc52n%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/2b19cd5e-84aa-4779-b1a6-490cc918cc52n%40googlegroups.com</a>.

<a
href="https://gnusha.org/pi/bitcoindev/2b19cd5e-84aa-4779-b1a6-490cc918cc52n@googlegroups.com/1.2-a.bin">[-- Attachment #1.2: Type: text/html, Size: 4360 bytes --]</a>
</pre></div></content></entry><entry><author><name>&#39;conduition&#39; via Bitcoin Development Mailing List</name><email>bitcoindev@googlegroups.com</email></author><title>Re: [bitcoindev] Giving teeth to expected EC disabling: P2XX(-T)(-ML)</title><updated>2026-08-19T02:37:12Z</updated><link
href="https://gnusha.org/pi/bitcoindev/FhcVTVM6flM4OpPCZpaGbC3msQG9kG48uvyz6T4qdNv8iAq-clhoMmNmRWSSWs78hug3KZSsKG3Mi2lZIzo5PFY-WvbvxdA0Ssj-G2HCz2o=@proton.me/"/><id>urn:uuid:b75d9703-91da-ddf4-51b1-1fe50ffa2657</id><thr:in-reply-to
ref="urn:uuid:67950890-ccae-69cd-14de-0e3a57b18064"
href="https://gnusha.org/pi/bitcoindev/td8wPWxRVg0rQIdP41uibTvWuIoCvGYpvfX022TaDurf-qu1TMm1TmWogw-JTs4C7Mt-97cvJCBW66z4g-Vc2fsSoo-Qxfm8Lcnd384Uink=@wuille.net/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/FhcVTVM6flM4OpPCZpaGbC3msQG9kG48uvyz6T4qdNv8iAq-clhoMmNmRWSSWs78hug3KZSsKG3Mi2lZIzo5PFY-WvbvxdA0Ssj-G2HCz2o=@proton.me/1.1.1-a.txt">[-- Attachment #1.1.1: Type: text/plain, Size: 11134 bytes --]</a>

<span
class="q">&gt; Oh wait, it&#39;s much simpler (not perhaps in character, but concretely): we don&#39;t need to talk about some general ZKP system here, right. If we all agree on a 192 bit curve, and a NUMS point on that curve, then in the OP_RETURN (say), we just need to put the point&#39;s dlog and consensus nodes only have to do a single scalar multiplication on that curve to verify.
</span>
Exactly. Also, the canary proof need not be the NUMS discrete log itself, it could also be a signature proving knowledge of the dlog without revealing it outright. Dlog exposure is simpler and faster to verify; Signature allows the first QC to identify itself later. (IDK if useful)



<span
class="q">&gt; Right, so: the QCAP thread was about a canary rather than a full tripwire
</span>
Oh I misunderstood. So to be clear, a &#34;canary&#34; is just a social signal that should push consensus to activate a soft fork, whereas a &#34;tripwire&#34; is an unattended system that automatically triggers a change to consensus rules.


<span
class="q">&gt; While it&#39;s certainly possible it&#39;s actually triggered by a cooperative CRQC, that&#39;s not how I expect ECC disabling to happen (instead I expect a community consensus-changing effort, effected through Miner Lockdown or otherwise). The Tripwire just sets an unambiguous expectation that disabling is intended by Q-day.
</span>
In the absence of evidence, I expect this fork to be highly contentious or delayed until hard evidence is available.


<span
class="q">&gt; I don&#39;t think the presence of a 192-bit canary changes this expectation much. 192-bit ECDLP broken (or breakable) is certainly a legitimate reason for panic, but nothing prevents that information from being used at the human layer without it needing to have been part of consensus rules.
</span>
I agree but for a different reason on top. Given the polynomial efficiency of Shor, and the massive time/money investment needed to build quantum computers, we have no reason to expect anyone will build a QC that can break 192-bit curves but not&#160;256-bit curves. There is actually incentive not&#160;to do so, especially if breaking a 192-bit curve will cause the Bitcoin network (the most ripe target to pay off QC investors) to react by locking itself down.&#160;
Think of it this way: If you have the mans to build a stable 900 logical-qubit quantum-computer, why not spend the extra time and money to build a 1200 logical-qubit quantum computer? Is a 1.5x factor improvement really so hard at this point? If you do expend the effort, then at least you stand a chance to make some money (e.g. by decrypting old internet traffic on behalf of the NSA).
From the google paper:

<span
class="q">&gt; Given broad progress across multiple hardware architectures, the safe assumption is that there may be little time between the breaking of 256-bit ECDLP and the breaking of 1024-bit&#160;ECDLP.
</span>
I think I&#39;m coming to the conclusion that a 256-bit ST-ECDLP tripwire is the way to go, because at least then the canary is unambiguously dead, and it&#39;s time to stop using secp256k1, whereas 192-bit curves leave a shred of doubt.

<span
class="q">&gt; This makes me wonder about using a subgroup of a very related curve: for example y^2 = x^3 + 3 (mod 2^256-2^32-977) has a subgroup of order ~2^187.11, which would use all the same finite field arithmetic and almost the same multiplication logic (only doubling is affected). Keeping the field modulus the same does mean the q-bit count is unaffected though, only the gate count decreases (proportional to logarithm of group order). Like other weaker-curve constructions, I don&#39;t think this is worth it, but want to throw the idea out there.
</span>


Really interesting idea there. Small correction: I believe Shor&#39;s space (qubit) requirements are dominated primarily by the group order that we are searching for the dlog within, not by the size of the field used for the the elliptic curve group operation. I&#39;m pretty sure the field size would affect runtime complexity (gate count), but not qubit count requirements. (Happy to be corrected). If I&#39;m correct, a group order of approx 2^187 would need approx 842 qubits (at least) to break.


Still, as previously discussed, I&#39;m unsure if a canary which is only slightly&#160;harder to break would be meaningful. It&#39;d be nice if we could find some problem which quantum computers of, say, 150 qubits could do, but which classical computers cannot (feasibly) solve. Then we might have a reasonably predictive canary which could be solved by cooperative.


Also found this related paper which proposes an incremental ladder of canaries using NUMS points on a sequence of curves of increasing size:&#160;<a
href="https://arxiv.org/pdf/2508.14011">https://arxiv.org/pdf/2508.14011</a>


<span
class="q">&gt; I also don&#39;t think optimizing for multi-target ECDLP adds much.
</span>


Strongly agree.


<span
class="q">&gt; From a simplicity standpoint, I think just having a &#34;a UTXO with scriptPubKey X is spent&#34; is ideal, because it reuses all existing block and transaction validation logic, and just adds a trivial trigger.
</span>


I would like to make a case that we should expend the extra effort and not bind the canary to a specific UTXO. I will point to Antoine&#39;s game theory arguments about reorgs and miner collusion with CRQCs.&#160;


If we tie the canary to a specific UTXO, or even to any UTXO with a specific script, then this makes miner censorship of the canary proof very easy: Just block spends of that UTXO (or of any UTXO unlocking the chosen script).


If, on the other hand, we had nodes check something almost as simple, like for example &#34;check every 32-byte OP_RETURN to see if it happens to be the dlog of the NUMS point&#34;, then any user can choose to include the proof in their transactions at relatively little cost. Any miners who want to censor the canary proof will have to also censor any such transactions, and so they lose out on the potential fee revenue of the entire TX by doing so.


In the extreme case, if every transaction in the mempool contained the canary proof as an OP_RETURN, then censoring miners would receive no fee revenue at all - they would have to mine empty blocks.


I&#39;m not sure if this incentive is meaningful when compared to the potential bribes that a miner could be offered by a CRQC, but still it is worth considering. It does have the down side that it will slow down block validation slightly (one EC mult per 32-byte OP_RETURN). Maybe this could be accounted for somehow in the sigops budget?


regards,
conduition


On Tuesday, August 18th, 2026 at 1:30 PM, Pieter Wuille bitcoin-dev@wuille&#8226;net wrote:

<span
class="q">&gt; Hi all,
&gt; 
</span>
<span
class="q">&gt; I&#39;m unconvinced the complexity of a 192-bit canary is worth it. Picking a curve and a NUMS point on it are not hard, but very little of libsecp256k1&#39;s code can be reused (even field arithmetic is optimized specifically for the secp256k1 prime). A more generic implementation is possible of course, but it&#39;s still a pretty big piece of engineering for what is IMO very little gain.
&gt; 
</span>
<span
class="q">&gt; There is a pretty fundamental difference between a secp256k1 Tripwire and a canary for weaker curves, in that the former isn&#39;t intended to be predictive. Its purpose is setting a codified upper bound on when ECC (within PQC output types) is expected to be disabled. While it&#39;s certainly possible it&#39;s actually triggered by a cooperative CRQC, that&#39;s not how I expect ECC disabling to happen (instead I expect a community consensus-changing effort, effected through Miner Lockdown or otherwise). The Tripwire just sets an unambiguous expectation that disabling is intended by Q-day.
&gt; 
</span>
<span
class="q">&gt; I don&#39;t think the presence of a 192-bit canary changes this expectation much. 192-bit ECDLP broken (or breakable) is certainly a legitimate reason for panic, but nothing prevents that information from being used at the human layer without it needing to have been part of consensus rules.
&gt; 
</span>
<span
class="q">&gt; Relatedly, something I don&#39;t know is how &#34;similar&#34; a canary needs to be to the real secp256k1 ECDLP for people to bother building/programming/running a QC for it. This is of course a question that exists for secp256k1 itself: whether a cooperative entity with the capability of building a secp256k1-ECDLP QRQC would bother doing so. But it&#39;s even more tenuous for weaker problems, if they&#39;re not so much weaker that they&#39;re trivial. This makes me wonder about using a subgroup of a very related curve: for example y^2 = x^3 + 3 (mod 2^256-2^32-977) has a subgroup of order ~2^187.11, which would use all the same finite field arithmetic and almost the same multiplication logic (only doubling is affected). Keeping the field modulus the same does mean the q-bit count is unaffected though, only the gate count decreases (proportional to logarithm of group order). Like other weaker-curve constructions, I don&#39;t think this is worth it, but want to throw the idea out there.
&gt; 
</span>
<span
class="q">&gt; I also don&#39;t think optimizing for multi-target ECDLP adds much. My understanding is that Shor&#39;s doesn&#39;t benefit from multiple targets? I&#39;m not opposed to giving freedom of finding (m,x) such that H(m) = x*G, but I don&#39;t see why that would encourage a cooperative CRQC to work on breaking it.
&gt; 
</span>
<span
class="q">&gt; Regarding using the BIP-341 H itself as canary, I don&#39;t think that&#39;s a problem if the ECDLP break proof is a Schnorr signature (as opposed to revealing the DLP itself). But it also makes sense to be as conservative as possible here; it may make sense to make a selection of hash functions, feed them all as much input as possible (the genesis block is a good idea, the existing generator G, maybe a block hash from a time when the activation parameters are decided, or even a block hash when the block goes live as suggested by Tadge though that adds hash-to-curve logic to consensus too), and then XOR (or hash) all hash results together.
&gt; 
</span>
<span
class="q">&gt; From a simplicity standpoint, I think just having a &#34;a UTXO with scriptPubKey X is spent&#34; is ideal, because it reuses all existing block and transaction validation logic, and just adds a trivial trigger. It&#39;s not compatible with any weaker curve construction of course, or with AJ&#39;s H-dependent DLP proof which could enlist non-cooperative CRQC, but I don&#39;t think that&#39;s worth complicating matters for.
&gt; 
</span>
<span
class="q">&gt; Cheers,
&gt; 
</span>
<span
class="q">&gt; --
&gt; Pieter
&gt; 
</span>
<span
class="q">&gt; --
&gt; You received this message because you are subscribed to a topic in the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt; To unsubscribe from this topic, visit <a
href="https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe">https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe</a>.
&gt; To unsubscribe from this group and all its topics, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
&gt; To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/td8wPWxRVg0rQIdP41uibTvWuIoCvGYpvfX022TaDurf-qu1TMm1TmWogw-JTs4C7Mt-97cvJCBW66z4g-Vc2fsSoo-Qxfm8Lcnd384Uink%3D%40wuille.net">https://groups.google.com/d/msgid/bitcoindev/td8wPWxRVg0rQIdP41uibTvWuIoCvGYpvfX022TaDurf-qu1TMm1TmWogw-JTs4C7Mt-97cvJCBW66z4g-Vc2fsSoo-Qxfm8Lcnd384Uink%3D%40wuille.net</a>.
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/FhcVTVM6flM4OpPCZpaGbC3msQG9kG48uvyz6T4qdNv8iAq-clhoMmNmRWSSWs78hug3KZSsKG3Mi2lZIzo5PFY-WvbvxdA0Ssj-G2HCz2o%3D%40proton.me">https://groups.google.com/d/msgid/bitcoindev/FhcVTVM6flM4OpPCZpaGbC3msQG9kG48uvyz6T4qdNv8iAq-clhoMmNmRWSSWs78hug3KZSsKG3Mi2lZIzo5PFY-WvbvxdA0Ssj-G2HCz2o%3D%40proton.me</a>.

<a
href="https://gnusha.org/pi/bitcoindev/FhcVTVM6flM4OpPCZpaGbC3msQG9kG48uvyz6T4qdNv8iAq-clhoMmNmRWSSWs78hug3KZSsKG3Mi2lZIzo5PFY-WvbvxdA0Ssj-G2HCz2o=@proton.me/1.1.2.1-a.bin">[-- Attachment #1.1.2.1: Type: text/html, Size: 16840 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/FhcVTVM6flM4OpPCZpaGbC3msQG9kG48uvyz6T4qdNv8iAq-clhoMmNmRWSSWs78hug3KZSsKG3Mi2lZIzo5PFY-WvbvxdA0Ssj-G2HCz2o=@proton.me/1.2-a.bin">[-- Attachment #1.2: publickey - conduition@proton.me - 0x474891AD.asc --]
[-- Type: application/pgp-keys, Size: 649 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/FhcVTVM6flM4OpPCZpaGbC3msQG9kG48uvyz6T4qdNv8iAq-clhoMmNmRWSSWs78hug3KZSsKG3Mi2lZIzo5PFY-WvbvxdA0Ssj-G2HCz2o=@proton.me/2-signature.asc">[-- Attachment #2: OpenPGP digital signature --]
[-- Type: application/pgp-signature, Size: 343 bytes --]</a>
</pre></div></content></entry><entry><author><name>Erik Aronesty</name><email>erik@q32.com</email></author><title>Re: [bitcoindev] Giving teeth to expected EC disabling: P2XX(-T)(-ML)</title><updated>2026-08-18T23:20:02Z</updated><link
href="https://gnusha.org/pi/bitcoindev/CAJowKg+E5YMaWopx7VhMmtMYJ93mYMsDzbdJgVoG+B4=a9KaNQ@mail.gmail.com/"/><id>urn:uuid:e153a171-8779-dc02-182d-49852b5204a1</id><thr:in-reply-to
ref="urn:uuid:67950890-ccae-69cd-14de-0e3a57b18064"
href="https://gnusha.org/pi/bitcoindev/td8wPWxRVg0rQIdP41uibTvWuIoCvGYpvfX022TaDurf-qu1TMm1TmWogw-JTs4C7Mt-97cvJCBW66z4g-Vc2fsSoo-Qxfm8Lcnd384Uink=@wuille.net/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap"><a
href="https://gnusha.org/pi/bitcoindev/CAJowKg+E5YMaWopx7VhMmtMYJ93mYMsDzbdJgVoG+B4=a9KaNQ@mail.gmail.com/1-a.txt">[-- Attachment #1: Type: text/plain, Size: 4869 bytes --]</a>

FWIW: there is a very long thread about this here:
<a
href="https://groups.google.com/g/bitcoindev/c/d7o74e-teNo/m/lLKjufQZAgAJ">https://groups.google.com/g/bitcoindev/c/d7o74e-teNo/m/lLKjufQZAgAJ</a>

On Tue, Aug 18, 2026 at 10:30&#8239;AM Pieter Wuille &lt;bitcoin-dev@wuille&#8226;net&gt;
wrote:

<span
class="q">&gt; Hi all,
&gt;
&gt; I&#39;m unconvinced the complexity of a 192-bit canary is worth it. Picking a
&gt; curve and a NUMS point on it are not hard, but very little of
&gt; libsecp256k1&#39;s code can be reused (even field arithmetic is optimized
&gt; specifically for the secp256k1 prime). A more generic implementation is
&gt; possible of course, but it&#39;s still a pretty big piece of engineering for
&gt; what is IMO very little gain.
&gt;
&gt; There is a pretty fundamental difference between a secp256k1 Tripwire and
&gt; a canary for weaker curves, in that the former isn&#39;t intended to be
&gt; predictive. Its purpose is setting a codified upper bound on when ECC
&gt; (within PQC output types) is expected to be disabled. While it&#39;s certainly
&gt; possible it&#39;s actually triggered by a cooperative CRQC, that&#39;s not how I
&gt; expect ECC disabling to happen (instead I expect a community
&gt; consensus-changing effort, effected through Miner Lockdown or otherwise).
&gt; The Tripwire just sets an unambiguous expectation that disabling is
&gt; intended by Q-day.
&gt;
&gt; I don&#39;t think the presence of a 192-bit canary changes this expectation
&gt; much. 192-bit ECDLP broken (or breakable) is certainly a legitimate reason
&gt; for panic, but nothing prevents that information from being used at the
&gt; human layer without it needing to have been  part of consensus rules.
&gt;
&gt; Relatedly, something I don&#39;t know is how &#34;similar&#34; a canary needs to be to
&gt; the real secp256k1 ECDLP for people to bother building/programming/running
&gt; a QC for it. This is of course a question that exists for secp256k1 itself:
&gt; whether a *cooperative* entity with the capability of building a
&gt; secp256k1-ECDLP QRQC would bother doing so. But it&#39;s even more tenuous for
&gt; weaker problems, if they&#39;re not so much weaker that they&#39;re trivial. This
&gt; makes me wonder about using a subgroup of a very related curve: for example
&gt; y^2 = x^3 + 3 (mod 2^256-2^32-977) has a subgroup of order ~2^187.11, which
&gt; would use all the same finite field arithmetic and almost the same
&gt; multiplication logic (only doubling is affected). Keeping the field modulus
&gt; the same does mean the q-bit count is unaffected though, only the gate
&gt; count decreases (proportional to logarithm of group order). Like other
&gt; weaker-curve constructions, I don&#39;t think this is worth it, but want to
&gt; throw the idea out there.
&gt;
&gt; I also don&#39;t think optimizing for multi-target ECDLP adds much. My
&gt; understanding is that Shor&#39;s doesn&#39;t benefit from multiple targets? I&#39;m not
&gt; opposed to giving freedom of finding (m,x) such that H(m) = x*G, but I
&gt; don&#39;t see why that would encourage a cooperative CRQC to work on breaking
&gt; it.
&gt;
&gt; Regarding using the BIP-341 H itself as canary, I don&#39;t think that&#39;s a
&gt; problem if the ECDLP break proof is a Schnorr signature (as opposed to
&gt; revealing the DLP itself). But it also makes sense to be as conservative as
&gt; possible here; it may make sense to make a selection of hash functions,
&gt; feed them all as much input as possible (the genesis block is a good idea,
&gt; the existing generator G, maybe a block hash from a time when the
&gt; activation parameters are decided, or even a block hash when the block goes
&gt; live as suggested by Tadge though that adds hash-to-curve logic to
&gt; consensus too), and then XOR (or hash) all hash results together.
&gt;
&gt; From a simplicity standpoint, I think just having a &#34;a UTXO with
&gt; scriptPubKey X is spent&#34; is ideal, because it reuses all existing block and
&gt; transaction validation logic, and just adds a trivial trigger. It&#39;s not
&gt; compatible with any weaker curve construction of course, or with AJ&#39;s
&gt; H-dependent DLP proof which could enlist non-cooperative CRQC, but I don&#39;t
&gt; think that&#39;s worth complicating matters for.
&gt;
&gt; Cheers,
&gt;
&gt; --
&gt; Pieter
&gt;
&gt; --
&gt; You received this message because you are subscribed to the Google Groups
&gt; &#34;Bitcoin Development Mailing List&#34; group.
&gt; To unsubscribe from this group and stop receiving emails from it, send an
&gt; email to bitcoindev+unsubscribe@googlegroups&#8226;com.
&gt; To view this discussion visit
&gt; <a
href="https://groups.google.com/d/msgid/bitcoindev/td8wPWxRVg0rQIdP41uibTvWuIoCvGYpvfX022TaDurf-qu1TMm1TmWogw-JTs4C7Mt-97cvJCBW66z4g-Vc2fsSoo-Qxfm8Lcnd384Uink%3D%40wuille.net">https://groups.google.com/d/msgid/bitcoindev/td8wPWxRVg0rQIdP41uibTvWuIoCvGYpvfX022TaDurf-qu1TMm1TmWogw-JTs4C7Mt-97cvJCBW66z4g-Vc2fsSoo-Qxfm8Lcnd384Uink%3D%40wuille.net</a>
&gt; .
&gt;
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/CAJowKg%2BE5YMaWopx7VhMmtMYJ93mYMsDzbdJgVoG%2BB4%3Da9KaNQ%40mail.gmail.com">https://groups.google.com/d/msgid/bitcoindev/CAJowKg%2BE5YMaWopx7VhMmtMYJ93mYMsDzbdJgVoG%2BB4%3Da9KaNQ%40mail.gmail.com</a>.

<a
href="https://gnusha.org/pi/bitcoindev/CAJowKg+E5YMaWopx7VhMmtMYJ93mYMsDzbdJgVoG+B4=a9KaNQ@mail.gmail.com/2-a.bin">[-- Attachment #2: Type: text/html, Size: 5855 bytes --]</a>
</pre></div></content></entry><entry><author><name>fanquake</name><email>fanquake@gmail.com</email></author><title>[bitcoindev] Re: static-pie release binaries available for testing</title><updated>2026-08-18T17:31:15Z</updated><link
href="https://gnusha.org/pi/bitcoindev/e938393c-74ad-423f-b230-ab472a72bd04n@googlegroups.com/"/><id>urn:uuid:5ddf8171-2d35-2faf-60e6-e636157f336e</id><thr:in-reply-to
ref="urn:uuid:eafe77e1-385d-4ad8-69d0-178d601aae37"
href="https://gnusha.org/pi/bitcoindev/391ad3ce-2352-42d8-9d15-e011e187cb0fn@googlegroups.com/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/e938393c-74ad-423f-b230-ab472a72bd04n@googlegroups.com/1.1-a.txt">[-- Attachment #1.1: Type: text/plain, Size: 4682 bytes --]</a>

Hi list,

I&#39;ve uploaded a new round of test binaries, available 
here: <a
href="https://github.com/fanquake/bitcoin/releases/tag/static_bitcoind_db73d1623957">https://github.com/fanquake/bitcoin/releases/tag/static_bitcoind_db73d1623957</a>.

Thanks to everyone that has been testing (and reporting) so far.
Compared to the previous round of binaries, the main difference is building 
against a newer version of the glibc 2.44 branch.

Guix hashes:

31732e817019f219471e71cda1b1986a660130cc5e1ebed7020aae3478ce3150 
guix-build-db73d1623957/output/aarch64-linux-gnu/bitcoin-db73d1623957-aarch64-linux-gnu-debug.tar.gz 
27d13309bfc4ec03e8d0fd585b61f4deb00733b833e67a3cc432ffe3c2affccd 
guix-build-db73d1623957/output/aarch64-linux-gnu/bitcoin-db73d1623957-aarch64-linux-gnu.tar.gz 
2d89bed5b00526dd015042f32416bf1085b5bab0e0c36c42d8f6177a3bb7980f 
guix-build-db73d1623957/output/dist-archive/bitcoin-db73d1623957.tar.gz 
eafdc26130f7f059af2ae2185eeae50943b166bad8778c1980b52497d6a14e02 
guix-build-db73d1623957/output/x86_64-linux-gnu/bitcoin-db73d1623957-x86_64-linux-gnu-debug.tar.gz 
71aef249424b98b2ceb137cc4f86894941c2449e83e58e0ff6620343ee17a789 
guix-build-db73d1623957/output/x86_64-linux-gnu/bitcoin-db73d1623957-x86_64-linux-gnu.tar.gz

Thanks,

Michael / fanquake
On Thursday, 6 August 2026 at 16:41:54 UTC+1 fanquake wrote:

<span
class="q">&gt; Hi list,
&gt;
&gt; I&#39;ve been working on producing `-static-pie` release binaries for Bitcoin 
&gt; Core, using our existing Guix infrastructure. The goal is to ship release 
&gt; binaries that are as self-contained as possible, doing away with our few 
&gt; remaining runtime dependencies (libc &#38; friends); this will also make our 
&gt; release binaries more portable. Currently we target any system with glibc 
&gt; 2.31 or later. These new binaries will be able to run on systems with much 
&gt; older glibcs, as well as non-glibc based systems, like Alpine (musl libc).
&gt;
&gt; These changes are currently only for our x86_64 and aarch64 Linux 
&gt; binaries, for bitcoind, and the other utilities; bitcoin-qt and bitcoin-gui 
&gt; (multiprocess) won&#39;t be changing. There are plans to support more targets 
&gt; in future (arm32, riscv64 etc).
&gt;
&gt; The binaries are built with our current Guix toolchain (GCC 14.3.0 + 
&gt; Binutils 2.46.0) and against glibc 2.44 (rather than 2.31), with some 
&gt; patching for reproducibility.
&gt;
&gt; A PR with all the changes is available here: 
&gt; <a
href="https://github.com/bitcoin/bitcoin/pull/25573">https://github.com/bitcoin/bitcoin/pull/25573</a>.
&gt;
&gt; As of v31.1, a release bitcoind, ~18mb, looks like this:
&gt;
&gt; bitcoind: ELF 64-bit LSB pie executable, x86-64, version 1 (GNU/Linux), 
&gt; dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 
&gt; 3.2.0, stripped
&gt;
&gt; ldd bitcoind
&gt; linux-vdso.so.1 (0x00007fffb4d49000)
&gt; libpthread.so.0 =&gt; /lib/x86_64-linux-gnu/libpthread.so.0 
&gt; (0x0000746451893000)
&gt; libm.so.6 =&gt; /lib/x86_64-linux-gnu/libm.so.6 (0x00007464517aa000)
&gt; libc.so.6 =&gt; /lib/x86_64-linux-gnu/libc.so.6 (0x0000746450200000)
&gt; /lib64/ld-linux-x86-64.so.2 (0x00007464518a8000)
&gt;
&gt; With these changes, a release bitcoind, now ~19mb, would look like:
&gt;
&gt; bitcoind: ELF 64-bit LSB pie executable, x86-64, version 1 (GNU/Linux), 
&gt; static-pie linked, for GNU/Linux 3.2.0, stripped
&gt;
&gt; ldd bitcoind
&gt; statically linked
&gt;
&gt; I&#39;m looking for any amount of testing or feedback. Please leave any 
&gt; questions, bugs found or concerns in the PR, or feel free to reach out 
&gt; directly.
&gt;
&gt; You can find Guix built test binaries here:
&gt;
&gt;
&gt; <a
href="https://github.com/fanquake/bitcoin/releases/tag/static_bitcoind_ff01e5af948d">https://github.com/fanquake/bitcoin/releases/tag/static_bitcoind_ff01e5af948d</a>
&gt;
&gt; With the following hashes:
&gt;
&gt; 22b757235729757bf4a225de4b34eca4d20704ad7e1fd6b48ab6902ef6fad407 
&gt;  guix-build-ff01e5af948d/output/aarch64-linux-gnu/bitcoin-ff01e5af948d-aarch64-linux-gnu-debug.tar.gz
&gt; 1f3461c39b1776cbbaa6d216847beb6670df931121d1d4da9fbaaf6a3aad7398 
&gt;  guix-build-ff01e5af948d/output/aarch64-linux-gnu/bitcoin-ff01e5af948d-aarch64-linux-gnu.tar.gz
&gt; 00cc2357b102dd4e1c41bf9fc0c28cc4d43ec1074b7035defc09e4c81f910322 
&gt;  guix-build-ff01e5af948d/output/dist-archive/bitcoin-ff01e5af948d.tar.gz
&gt; 9d886b556d04658019f9882b7e10b3be26a91c5dbcdeedd4813fcaf769a7a750 
&gt;  guix-build-ff01e5af948d/output/x86_64-linux-gnu/bitcoin-ff01e5af948d-x86_64-linux-gnu-debug.tar.gz
&gt; 5abdd153b2fc41f56c341b51c9175196f503d310dde64e109c781e8f05f019de 
&gt;  guix-build-ff01e5af948d/output/x86_64-linux-gnu/bitcoin-ff01e5af948d-x86_64-linux-gnu.tar.gz
&gt;
&gt; Thanks,
&gt;
&gt; Michael / fanquake
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/e938393c-74ad-423f-b230-ab472a72bd04n%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/e938393c-74ad-423f-b230-ab472a72bd04n%40googlegroups.com</a>.

<a
href="https://gnusha.org/pi/bitcoindev/e938393c-74ad-423f-b230-ab472a72bd04n@googlegroups.com/1.2-a.bin">[-- Attachment #1.2: Type: text/html, Size: 6352 bytes --]</a>
</pre></div></content></entry><entry><author><name>Pieter Wuille</name><email>bitcoin-dev@wuille.net</email></author><title>Re: [bitcoindev] Giving teeth to expected EC disabling: P2XX(-T)(-ML)</title><updated>2026-08-18T17:31:00Z</updated><link
href="https://gnusha.org/pi/bitcoindev/td8wPWxRVg0rQIdP41uibTvWuIoCvGYpvfX022TaDurf-qu1TMm1TmWogw-JTs4C7Mt-97cvJCBW66z4g-Vc2fsSoo-Qxfm8Lcnd384Uink=@wuille.net/"/><id>urn:uuid:67950890-ccae-69cd-14de-0e3a57b18064</id><thr:in-reply-to
ref="urn:uuid:ff02dabb-53b2-ebdf-0e7b-049710d2ea08"
href="https://gnusha.org/pi/bitcoindev/f6565311-f62e-4210-8c15-93830c3f71cbn@googlegroups.com/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">Hi all,

I&#39;m unconvinced the complexity of a 192-bit canary is worth it. Picking a curve and a NUMS point on it are not hard, but very little of libsecp256k1&#39;s code can be reused (even field arithmetic is optimized specifically for the secp256k1 prime). A more generic implementation is possible of course, but it&#39;s still a pretty big piece of engineering for what is IMO very little gain.

There is a pretty fundamental difference between a secp256k1 Tripwire and a canary for weaker curves, in that the former isn&#39;t intended to be predictive. Its purpose is setting a codified upper bound on when ECC (within PQC output types) is expected to be disabled. While it&#39;s certainly possible it&#39;s actually triggered by a cooperative CRQC, that&#39;s not how I expect ECC disabling to happen (instead I expect a community consensus-changing effort, effected through Miner Lockdown or otherwise). The Tripwire just sets an unambiguous expectation that disabling is intended by Q-day.

I don&#39;t think the presence of a 192-bit canary changes this expectation much. 192-bit ECDLP broken (or breakable) is certainly a legitimate reason for panic, but nothing prevents that information from being used at the human layer without it needing to have been  part of consensus rules.

Relatedly, something I don&#39;t know is how &#34;similar&#34; a canary needs to be to the real secp256k1 ECDLP for people to bother building/programming/running a QC for it. This is of course a question that exists for secp256k1 itself: whether a *cooperative* entity with the capability of building a secp256k1-ECDLP QRQC would bother doing so. But it&#39;s even more tenuous for weaker problems, if they&#39;re not so much weaker that they&#39;re trivial. This makes me wonder about using a subgroup of a very related curve: for example y^2 = x^3 + 3 (mod 2^256-2^32-977) has a subgroup of order ~2^187.11, which would use all the same finite field arithmetic and almost the same multiplication logic (only doubling is affected). Keeping the field modulus the same does mean the q-bit count is unaffected though, only the gate count decreases (proportional to logarithm of group order). Like other weaker-curve constructions, I don&#39;t think this is worth it, but want to throw the idea out there.

I also don&#39;t think optimizing for multi-target ECDLP adds much. My understanding is that Shor&#39;s doesn&#39;t benefit from multiple targets? I&#39;m not opposed to giving freedom of finding (m,x) such that H(m) = x*G, but I don&#39;t see why that would encourage a cooperative CRQC to work on breaking it.

Regarding using the BIP-341 H itself as canary, I don&#39;t think that&#39;s a problem if the ECDLP break proof is a Schnorr signature (as opposed to revealing the DLP itself). But it also makes sense to be as conservative as possible here; it may make sense to make a selection of hash functions, feed them all as much input as possible (the genesis block is a good idea, the existing generator G, maybe a block hash from a time when the activation parameters are decided, or even a block hash when the block goes live as suggested by Tadge though that adds hash-to-curve logic to consensus too), and then XOR (or hash) all hash results together.

From a simplicity standpoint, I think just having a &#34;a UTXO with scriptPubKey X is spent&#34; is ideal, because it reuses all existing block and transaction validation logic, and just adds a trivial trigger. It&#39;s not compatible with any weaker curve construction of course, or with AJ&#39;s H-dependent DLP proof which could enlist non-cooperative CRQC, but I don&#39;t think that&#39;s worth complicating matters for.

Cheers,

-- 
Pieter

-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/td8wPWxRVg0rQIdP41uibTvWuIoCvGYpvfX022TaDurf-qu1TMm1TmWogw-JTs4C7Mt-97cvJCBW66z4g-Vc2fsSoo-Qxfm8Lcnd384Uink%3D%40wuille.net">https://groups.google.com/d/msgid/bitcoindev/td8wPWxRVg0rQIdP41uibTvWuIoCvGYpvfX022TaDurf-qu1TMm1TmWogw-JTs4C7Mt-97cvJCBW66z4g-Vc2fsSoo-Qxfm8Lcnd384Uink%3D%40wuille.net</a>.

</pre></div></content></entry><entry><author><name>waxwing/ AdamISZ</name><email>ekaggata@gmail.com</email></author><title>Re: [bitcoindev] Giving teeth to expected EC disabling: P2XX(-T)(-ML)</title><updated>2026-08-18T14:41:58Z</updated><link
href="https://gnusha.org/pi/bitcoindev/f6565311-f62e-4210-8c15-93830c3f71cbn@googlegroups.com/"/><id>urn:uuid:ff02dabb-53b2-ebdf-0e7b-049710d2ea08</id><thr:in-reply-to
ref="urn:uuid:da820e58-da1c-cbc2-4f1d-22df3f31b9f2"
href="https://gnusha.org/pi/bitcoindev/22f8b95d-403c-4a3e-ad64-221faf2ea851n@googlegroups.com/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/f6565311-f62e-4210-8c15-93830c3f71cbn@googlegroups.com/1.1-a.txt">[-- Attachment #1.1: Type: text/plain, Size: 5125 bytes --]</a>

(re-sending 2 messages after sending them to the wrong location!):

Right, so: the QCAP thread was about a canary rather than a full tripwire, 
and doing DKG (optionally) plus DLEQAG, rather than NUMS. You&#39;re 
saying/thinking (are you?): do NUMS on 192 bit, then, when proof is 
published, activate the consensus change. But that would mean validating 
the ZKP in consensus right? It&#39;d presumably be simpler than literally 
implementing the 192 bit curve in consensus (doesn&#39;t sound very simple!), 
just for this one action. And it&#39;s more realistic than the idea of having a 
trusted setup to create a small dlog in secp256k1 (because trusted setup in 
consensus is not going to fly in bitcoin). But it *would* mean having a ZKP 
verifier inside our consensus. Heck, if we can do that, we can do lots of 
other nicer things :) 

So tell me if I&#39;m wrong, but I don&#39;t think the fact that it doesn&#39;t have to 
tie to spending of a specific utxo is the thing: I think the thing about 
&#39;tripwire&#39; is creating a consensus rule, which means validating nodes have 
to agree. I tended, after our earlier discussion on this, to come to the 
conclusion that a 192 bit tripwire would be &#39;nice&#39; but doesn&#39;t seem to be 
practical. Could have it as a canary still, ofc. But probably only 256 bit 
is going to work as a tripwire?

2nd message:

Oh wait, it&#39;s much simpler (not perhaps in character, but concretely): we 
don&#39;t need to talk about some general ZKP system here, right. If we all 
agree on a 192 bit curve, and a NUMS point on that curve, then in the 
OP_RETURN (say), we just need to put the point&#39;s dlog and consensus nodes 
only have to do a single scalar multiplication on that curve to verify.

That&#39;s so much simpler that I almost change my mind, i.e. that really is a 
simple extra consensus rule, but I wouldn&#39;t be surprised if the engineers 
still say, no, we should definitely not do that (dependencies?). After all 
there is something very ugly about one-off consensus rules like that that 
are completely unconnected with bitcoin&#39;s central design. Has there been 
any such thing before? Maybe that one about the repeated block hash? (even 
if I&#39;m right, a bug fix like that in the existing rule set, is very 
different).

Not commenting on the gate-scaling because I&#39;m completely clueless about 
how the scaling works / will work (and don&#39;t know if anyone knows). 
Obviously it&#39;s *plausible* that the gap between these two cases will be 
small.

Cheers, waxwing/AdamISZ

On Tuesday, August 18, 2026 at 3:17:32&#8239;AM UTC-6 conduition wrote:

I&#39;m hesitant to say I support a 192-bit canary outright, but I like the 
idea and I think more research is needed to confirm whether it would work, 
or if such a system would be over- or under-sensitive (i.e. triggered too 
late by the first powerful quantum computer, or triggered exceptionally 
early by a classical attack). I&#39;m especially interested in any attempts to 
estimate a rough time delta between the &#34;secp192r is broken&#34; and &#34;secp256k1 
is broken&#34; events. I suppose that&#39;s more a question for the QC experts (not 
me). I&#39;ll have a go anyway.

Based on logical qubit count estimates in the google paper 
&lt;<a
href="https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf">https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf</a>&gt; (see 
page 7), a QC needs at least 4.5 * n qubits to crack a curve of n bits 
(with a practical Toffoli gate count). So secp192r1 might be broken by more 
than 192 * 4.5 = 900 logical qubits. Breaking secp256k1 requires at least 
1200.

So how difficult would it be for a QC to scale from 900 to 1200 qubits? If 
we assume QC scaling will follow moore&#39;s law (if it ever scales at all), 
then that&#39;s worrisome: less than half a doubling of margin. The first QC 
that breaks secp192r1 might very well also be able to break secp256k1.

Also: I read the QCAP thread 
&lt;<a
href="https://delvingbitcoin.org/t/qcap-a-bitcoin-native-quantum-canary-alert/2498">https://delvingbitcoin.org/t/qcap-a-bitcoin-native-quantum-canary-alert/2498</a>&gt;, 
and my initial impression is that using DLEQAG proofs to share the secret 
among a trusted group is overkill: If breaking a 192-bit curve such as 
secp192r1 suffices to prove &#34;QCs are coming&#34; and so activate a soft fork, 
then why go through the effort to map that statement to secp256k1? We can 
just use a secp192r1 canary proof on its own as a self-contained 
cryptographic statement published on-chain. Then the proof can use a NUMS 
point generated in some honest fashion, same as for secp256k1. Nodes could 
activate the canary as soon as they see the canary proof published anywhere 
on-chain (e.g. OP_RETURN). As discussed before in this thread, there&#39;s no 
need to tie the canary specifically to a Bitcoin UTXO being spent.

regards,
conduition

&lt;snip&gt; 

-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/f6565311-f62e-4210-8c15-93830c3f71cbn%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/f6565311-f62e-4210-8c15-93830c3f71cbn%40googlegroups.com</a>.

<a
href="https://gnusha.org/pi/bitcoindev/f6565311-f62e-4210-8c15-93830c3f71cbn@googlegroups.com/1.2-a.bin">[-- Attachment #1.2: Type: text/html, Size: 5801 bytes --]</a>
</pre></div></content></entry><entry><author><name>&#39;nervana21&#39; via Bitcoin Development Mailing List</name><email>bitcoindev@googlegroups.com</email></author><title>[bitcoindev] [BIP Proposal] Anti-Fee-Sniping with LockTime</title><updated>2026-08-18T09:17:50Z</updated><link
href="https://gnusha.org/pi/bitcoindev/wWGWjMw9TI22vp4VzCm4xJJS3IGA1UhndMKynUkB04BqeoRjhe-QbDbJU-GMQq0nnOnXuB__u8KcdIcxU5i8Cy9pbTbtJ7Hi583FzLVojek=@pm.me/"/><id>urn:uuid:d9116ae7-b9b7-85e0-9cce-8f168eed7743</id><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">Hello all,

Anti-fee-sniping with nLockTime has been present in Bitcoin Core since
2014 and in Electrum since 2017. BIP326 assumes this nLockTime behavior
as the baseline and uses nSequence instead for some taproot spends.
However, the nLockTime rules themselves were never specified in a BIP.

<a
href="https://github.com/nervana21/bips/blob/anti-fee-snipe/bip-anti-fee-sniping-with-locktime.md">https://github.com/nervana21/bips/blob/anti-fee-snipe/bip-anti-fee-sniping-with-locktime.md</a>

The BIP draft follows Bitcoin Core&#39;s DiscourageFeeSniping and
IsCurrentForAntiFeeSniping functions. nLockTime is set to the current tip height.
With probability 10%, a uniform random integer in 0..99 is subtracted
and the result is clamped at 0. A locktime equal to the tip height
cannot be included in a remine of the tip. An older locktime chosen on
the privacy branch can. nLockTime is set to 0 during initial block
download or when the tip is more than 8 hours old. The policy is not
applied when nLockTime is already set or when any input already has a
preset nSequence. Test vectors are included.

Constructive criticism is greatly appreciated.

Cheers,
nervana21

-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/wWGWjMw9TI22vp4VzCm4xJJS3IGA1UhndMKynUkB04BqeoRjhe-QbDbJU-GMQq0nnOnXuB__u8KcdIcxU5i8Cy9pbTbtJ7Hi583FzLVojek%3D%40pm.me">https://groups.google.com/d/msgid/bitcoindev/wWGWjMw9TI22vp4VzCm4xJJS3IGA1UhndMKynUkB04BqeoRjhe-QbDbJU-GMQq0nnOnXuB__u8KcdIcxU5i8Cy9pbTbtJ7Hi583FzLVojek%3D%40pm.me</a>.

</pre></div></content></entry><entry><author><name>&#39;conduition&#39; via Bitcoin Development Mailing List</name><email>bitcoindev@googlegroups.com</email></author><title>Re: [bitcoindev] Giving teeth to expected EC disabling: P2XX(-T)(-ML)</title><updated>2026-08-18T09:17:42Z</updated><link
href="https://gnusha.org/pi/bitcoindev/22f8b95d-403c-4a3e-ad64-221faf2ea851n@googlegroups.com/"/><id>urn:uuid:da820e58-da1c-cbc2-4f1d-22df3f31b9f2</id><thr:in-reply-to
ref="urn:uuid:0099bad1-4b7f-e152-0ef5-99e5a30e91ba"
href="https://gnusha.org/pi/bitcoindev/d84e4a53-f3b1-4cd1-9a86-9591ec8c7211n@googlegroups.com/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/22f8b95d-403c-4a3e-ad64-221faf2ea851n@googlegroups.com/1.1-a.txt">[-- Attachment #1.1: Type: text/plain, Size: 28952 bytes --]</a>

I&#39;m hesitant to say I support a 192-bit canary outright, but I like the 
idea and I think more research is needed to confirm whether it would work, 
or if such a system would be over- or under-sensitive (i.e. triggered too 
late by the first powerful quantum computer, or triggered exceptionally 
early by a classical attack). I&#39;m especially interested in any attempts to 
estimate a rough time delta between the &#34;secp192r is broken&#34; and &#34;secp256k1 
is broken&#34; events. I suppose that&#39;s more a question for the QC experts (not 
me). I&#39;ll have a go anyway.

Based on logical qubit count estimates in the google paper 
&lt;<a
href="https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf">https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf</a>&gt; (see 
page 7), a QC needs at least 4.5 * n qubits to crack a curve of n bits 
(with a practical Toffoli gate count). So secp192r1 might be broken by more 
than 192 * 4.5 = 900 logical qubits. Breaking secp256k1 requires at least 
1200.

So how difficult would it be for a QC to scale from 900 to 1200 qubits? If 
we assume QC scaling will follow moore&#39;s law (if it ever scales at all), 
then that&#39;s worrisome: less than half a doubling of margin. The first QC 
that breaks secp192r1 might very well also be able to break secp256k1.

Also: I read the QCAP thread 
&lt;<a
href="https://delvingbitcoin.org/t/qcap-a-bitcoin-native-quantum-canary-alert/2498">https://delvingbitcoin.org/t/qcap-a-bitcoin-native-quantum-canary-alert/2498</a>&gt;, 
and my initial impression is that using DLEQAG proofs to share the secret 
among a trusted group is overkill: If breaking a 192-bit curve such as 
secp192r1 suffices to prove &#34;QCs are coming&#34; and so activate a soft fork, 
then why go through the effort to map that statement to secp256k1? We can 
just use a secp192r1 canary proof on its own as a self-contained 
cryptographic statement published on-chain. Then the proof can use a NUMS 
point generated in some honest fashion, same as for secp256k1. Nodes could 
activate the canary as soon as they see the canary proof published anywhere 
on-chain (e.g. OP_RETURN). As discussed before in this thread, there&#39;s no 
need to tie the canary specifically to a Bitcoin UTXO being spent.

regards,
conduition

On Saturday, August 15, 2026 at 1:12:44&#8239;PM UTC-5 waxwing/ AdamISZ wrote:

<span
class="q">&gt; As if everything wasn&#39;t confusing enough, I also made one very notable 
&gt; error: What I was saying here:
&gt;
&gt; &gt; This is relevant because the hypothetical evil curve-generator who is 
&gt; trying to poison the future H=SHA2(G) has an easier time in doing so, than 
&gt; a future canary-solver who obviously cannot try different values of G :)
&gt;
&gt; is, I&#39;m pretty sure, not correct: the canary-solver only needs 2^128 work 
&gt; anyway (all the normal classical collision finding); it&#39;s not like he has 
&gt; to use pure brute force.
&gt;
&gt; &gt; If we have any doubt about that, we could tweak the hash function with 
&gt; some data that is newer than G but still unbiased, e.g. the hash of the 
&gt; genesis block, or the hash of the first block in which the canary goes live 
&gt; (idea credit: Tadge Dryja 
&gt; &lt;<a
href="https://youtu.be/PmW90HX89P8?si=NhRJSaxKILVAJBkr&#38;t=841">https://youtu.be/PmW90HX89P8?si=NhRJSaxKILVAJBkr&#38;t=841</a>&gt;).
&gt;
&gt; Seems plausible.
&gt;
&gt; I guess two tracks of conversation here; I&#39;m still genuinely curious what 
&gt; people think about 192 bit and whether we can do it practically, because, 
&gt; depending on how it plays out, it might buy very useful time. The delving 
&gt; thread was focused on distributed keygen and ZKP for the canary, but this 
&gt; is obviously way less trustless than NUMS, so perhaps that&#39;s the end of 
&gt; that, or perhaps there&#39;s something else clever I&#39;m not aware of.
&gt;
&gt; On Saturday, August 15, 2026 at 10:54:11&#8239;AM UTC-6 conduition wrote:
&gt;
&gt;&gt; This is relevant because the hypothetical evil curve-generator who is 
&gt;&gt; trying to poison the future H=SHA2(G) has an easier time in doing so, than 
&gt;&gt; a future canary-solver who obviously cannot try different values of G :)
&gt;&gt;
&gt;&gt;
&gt;&gt; Ah sorry, I thought you were talking about canary solvers, didn&#39;t realize 
&gt;&gt; you were talking about curve designers. Agreed then, but still seems 
&gt;&gt; unlikely that G was chosen this way: 
&gt;&gt; <a
href="https://bitcoin.stackexchange.com/questions/58784/how-were-the-secp256k1-base-point-coordinates-decided">https://bitcoin.stackexchange.com/questions/58784/how-were-the-secp256k1-base-point-coordinates-decided</a>
&gt;&gt;
&gt;&gt; If we have any doubt about that, we could tweak the hash function with 
&gt;&gt; some data that is newer than G but still unbiased, e.g. the hash of the 
&gt;&gt; genesis block, or the hash of the first block in which the canary goes live 
&gt;&gt; (idea credit: Tadge Dryja 
&gt;&gt; &lt;<a
href="https://youtu.be/PmW90HX89P8?si=NhRJSaxKILVAJBkr&#38;t=841">https://youtu.be/PmW90HX89P8?si=NhRJSaxKILVAJBkr&#38;t=841</a>&gt;).
&gt;&gt;
&gt;&gt; interesting point is that Shor can target any specific dlog problem, 
&gt;&gt; right. So I do think the ST is the correct version of the problem?
&gt;&gt;
&gt;&gt;
&gt;&gt; Yes, I believe so. I don&#39;t know of any way to batch Shor&#39;s algorithm in a 
&gt;&gt; multi-target attack that is any more efficient than a trivial one-by-one 
&gt;&gt; attack, so using MT-ECDLP seems like it only serves to makes classical 
&gt;&gt; attacks (or Grover&#39;s search) easier.
&gt;&gt;
&gt;&gt; regards,
&gt;&gt; conduition
&gt;&gt;
&gt;&gt; On Saturday, August 15th, 2026 at 10:14 AM, waxwing/ AdamISZ &lt;
&gt;&gt; ekag...@gmail&#8226;com&gt; wrote:
&gt;&gt;
&gt;&gt; &gt; A 192-bit curve i think should be reasonable as a canary, but consider 
&gt;&gt; this: If someone already has a QC that breaks 192-bit ECC, how long until 
&gt;&gt; they build one which breaks 256-bit ECC? A day, a week, a year? No way of 
&gt;&gt; knowing. If the delay is too long, users may see the canary as a 
&gt;&gt; false-positive, and migrate back to vulnerable addresses, and they might 
&gt;&gt; even be right. 192-bit canaries are vulnerable to classical attack with 
&gt;&gt; work approximately 2^96. We should bear in mind the possibility that such a 
&gt;&gt; canary could be activated possibly very early, well before Q-day, possibly 
&gt;&gt; even in the absence of any quantum computers.
&gt;&gt;
&gt;&gt; Agreed that is unlikely a big delta, in the nature of these things (QCs), 
&gt;&gt; between 192 and 256. Including that it&#39;s obvious that going very much below 
&gt;&gt; 192 means classical attack and therefore bad idea. Which is why I said 192 
&gt;&gt; and not sub 160. What&#39;s not obvious is that 192 is worse than 256 here. It 
&gt;&gt; may only give us a small amount of extra time, but it won&#39;t give us 
&gt;&gt; negative extra time. So the tradeoff is, presumably, whether the additional 
&gt;&gt; complexity (which is a bit tricky from what I recall [1], but there will 
&gt;&gt; definitely be experts out there who can clean it up) is worth it.
&gt;&gt;
&gt;&gt; The idea of &#39;people will think it a false positive&#39;, disagree, I think 
&gt;&gt; the whole tripwire idea is likely a *bit* vulnerable to genpop 
&gt;&gt; misunderstanding as I said in my previous post, but this particular thing I 
&gt;&gt; don&#39;t see it: a 192 bit being broken is *very* likely to cause an 
&gt;&gt; appropriate level of panic.
&gt;&gt;
&gt;&gt; &gt; Anyone can find G = a * B&#8203;. Just generate a key and invert your secret 
&gt;&gt; key.
&gt;&gt;
&gt;&gt; &gt; P = a * G&#8203;
&gt;&gt; &gt; G = a**-1 * P
&gt;&gt;
&gt;&gt; &gt; The hard part is then finding some b such that b*G = SHA256(G).
&gt;&gt;
&gt;&gt; You slightly missed my point here, I think? The idea is that if you set 
&gt;&gt; up two sides that are both sample-able, you can birthday. Like, you keep 
&gt;&gt; sampling a on one side and b on the other. Build tables of both sides. Then 
&gt;&gt; all you have to do is check whether SHA2 of the LHS ever matches the RHS. 
&gt;&gt; This gives you a square root style speedup a la birthday attack. Contrast 
&gt;&gt; with if you just fix G, then keep searching for matches: no square root 
&gt;&gt; speedup. This is relevant because the hypothetical evil curve-generator who 
&gt;&gt; is trying to poison the future H=SHA2(G) has an easier time in doing so, 
&gt;&gt; than a future canary-solver who obviously cannot try different values of G 
&gt;&gt; :)
&gt;&gt;
&gt;&gt; About your single-target vs multi-target distinction: interesting point 
&gt;&gt; is that Shor can target any specific dlog problem, right. So I do think the 
&gt;&gt; ST is the correct version of the problem? But actually I am quite unsure 
&gt;&gt; and unclear about those ST, MT, LMT distinctions you&#39;re making; 
&gt;&gt; specifically I mean, I am very unsure about how they differ in costs.
&gt;&gt;
&gt;&gt; As for characterizing the problem, I think it&#39;s fair to say: if you 
&gt;&gt; assumed SHA2 was a proper random oracle then we have with SHA2(enc(G)), 
&gt;&gt; something that&#39;s very tightly equivalent to ECDLP, which is what we want. 
&gt;&gt; If we want to pay attention to the fact that SHA2 is an actual hash 
&gt;&gt; function and not an RO, then I think there&#39;s some statement like &#34;assuming 
&gt;&gt; SHA2 has no structure &#34;matching&#34; secp256k1, then it&#39;s tightly equivalent to 
&gt;&gt; ECDLP on secp256k1&#34; which is obviously horrendously vague, but would not be 
&gt;&gt; very easy to write down properly.
&gt;&gt;
&gt;&gt; Another observation, probably it already exists up-thread: we obviously 
&gt;&gt; don&#39;t want to *literally* use BIP341&#39;s H on a 256 bit tripwire, because 
&gt;&gt; then a Shor-break directly steals a bunch of coins, so what should we use? 
&gt;&gt; Maybe SHA2(SHA2(enc(G)) ?
&gt;&gt;
&gt;&gt;
&gt;&gt; [1] 
&gt;&gt; <a
href="https://delvingbitcoin.org/t/qcap-a-bitcoin-native-quantum-canary-alert/2498/9">https://delvingbitcoin.org/t/qcap-a-bitcoin-native-quantum-canary-alert/2498/9</a>
&gt;&gt; On Friday, August 14, 2026 at 12:34:54&#8239;PM UTC-6 conduition wrote:
&gt;&gt;
&gt;&gt;&gt; An obvious question to raise: would we consider tripwiring a 192 bit 
&gt;&gt;&gt; group break of a similar type (NUMS)? I find that ... plausible?
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; A 192-bit curve i think should be reasonable as a canary, but consider 
&gt;&gt;&gt; this: If someone already has a QC that breaks 192-bit ECC, how long until 
&gt;&gt;&gt; they build one which breaks 256-bit ECC? A day, a week, a year? No way of 
&gt;&gt;&gt; knowing. If the delay is too long, users may see the canary as a 
&gt;&gt;&gt; false-positive, and migrate back to vulnerable addresses, and they might 
&gt;&gt;&gt; even be right. 192-bit canaries are vulnerable to classical attack with 
&gt;&gt;&gt; work approximately 2^96. We should bear in mind the possibility that such a 
&gt;&gt;&gt; canary could be activated possibly very early, well before Q-day, possibly 
&gt;&gt;&gt; even in the absence of any quantum computers.
&gt;&gt;&gt;
&gt;&gt;&gt; Ideally we want a short gap between &#34;192-bit is broken&#34; and &#34;256-bit is 
&gt;&gt;&gt; broken&#34;, but not so short as to make the 192-bit canary effectively 
&gt;&gt;&gt; fungible with a 256-bit canary (because then it&#39;s less likely to be 
&gt;&gt;&gt; activated before theft occurs).
&gt;&gt;&gt;
&gt;&gt;&gt; w.r.t. &#39;This guarantees that the NUMS point cannot predate G&#39; yes based 
&gt;&gt;&gt; on SHA2 preimage resistance, but: isn&#39;t the real point that we&#39;re relying 
&gt;&gt;&gt; on SHA-2 not being a naughty function so that you couldn&#39;t find G = a * B 
&gt;&gt;&gt; and SHA2(G) = b*B for some base B in some feasible computation (sans CQRC 
&gt;&gt;&gt; of course, as was likely back then!). I have no idea what precise name you 
&gt;&gt;&gt; give to that property. OK, this is a ridiculous thing to discuss, perhaps, 
&gt;&gt;&gt; given when SHA2 and secp256k1 were standardized :) And given the encoding 
&gt;&gt;&gt; choices for our BIP341 NUMS (iirc the same as for Elements back in the day? 
&gt;&gt;&gt; using uncompressed encoding?) were able to be counted on the fingers of the 
&gt;&gt;&gt; hand which the sleeve does not cover :)
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; Anyone can find G = a * B&#8203;. Just generate a key and invert your secret 
&gt;&gt;&gt; key.
&gt;&gt;&gt;
&gt;&gt;&gt; P = a * G&#8203;
&gt;&gt;&gt; G = a**-1 * P
&gt;&gt;&gt;
&gt;&gt;&gt; The hard part is then finding some b such that b*G = SHA256(G).
&gt;&gt;&gt;
&gt;&gt;&gt; ---------
&gt;&gt;&gt;
&gt;&gt;&gt; If we reflect on the requirement that G&#8203; is fixed, we see SHA256(G)&#8203; is 
&gt;&gt;&gt; also fixed as a pseudorandom challenge point. The reason for using SHA256 
&gt;&gt;&gt; instead of, say, picking an arbitary point by committee or using digits of 
&gt;&gt;&gt; pi or some other trickery, is that hash outputs are supposed to be random 
&gt;&gt;&gt; and so SHA256(G)&#8203; is (assumably) a random ECDLP challenge. This matches 
&gt;&gt;&gt; the classical definition of ECDLP more tightly: Given an arbitrary point 
&gt;&gt;&gt; P&#8203;, find p&#8203; such that P = p * G&#8203;. The assumption is that if an attacker 
&gt;&gt;&gt; can factor an honestly-sampled challenge point, they can factor any point. 
&gt;&gt;&gt; SHA256 is just a stand-in for the &#34;honestly-sampled&#34; part.
&gt;&gt;&gt;
&gt;&gt;&gt; However, the following two tasks are actually very different:
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt;    1. Given G, find scalar a&#8203; such that a*G = lift_x(SHA256(G))&#8203;.
&gt;&gt;&gt;    2. Given G, find scalar a&#8203; and message m&#8203; such that a*G = 
&gt;&gt;&gt;    lift_x(SHA256(m))&#8203;.
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; In the case of task 1, if we assume SHA256 output is random, then this 
&gt;&gt;&gt; is more tightly equivalent to ECDLP, because the point we&#39;re trying to 
&gt;&gt;&gt; factor is a fixed target, as is the one sampled honestly by the ECDLP 
&gt;&gt;&gt; security game.
&gt;&gt;&gt;
&gt;&gt;&gt; In the case of task 2, the attacker can sample arbitrary messages to 
&gt;&gt;&gt; create multiple *target points*, and the attacker wins if they succeed 
&gt;&gt;&gt; in factoring any of them. The attacker can attack all those target points 
&gt;&gt;&gt; concurrently if they want, and they get a speedup from doing so.
&gt;&gt;&gt;
&gt;&gt;&gt; So I believe it is worth disambiguating canaries between the two cases, 
&gt;&gt;&gt; because they are different security notions. The first (1) I would call *single-target 
&gt;&gt;&gt; ECDLP *(ST-ECDLP), and the second (2) I would call *multi-target ECDLP *
&gt;&gt;&gt; (MT-ECDLP).
&gt;&gt;&gt;
&gt;&gt;&gt; It&#39;s pretty clear that MT-ECDLP is easier to break, because attackers 
&gt;&gt;&gt; can make progress against more than one target concurrently, and breaking 
&gt;&gt;&gt; any one is sufficient to win the security game.
&gt;&gt;&gt;
&gt;&gt;&gt; For example, say I sample 2 different messages m1&#8203; and m2&#8203;, and compute 
&gt;&gt;&gt; ECDLP target points T1 = lift_x(SHA256(m1))&#8203; and T2 = lift_x(SHA256(m2))&#8203;. 
&gt;&gt;&gt; Then if I sample a random scalar r&#8203; and compute R = r*G&#8203;, I have two 
&gt;&gt;&gt; potential chances of success: R == T1&#8203; OR R == T2&#8203;. I can scale up this 
&gt;&gt;&gt; advantage by generating more targets, T3&#8203;, T4&#8203;, ... and so on.
&gt;&gt;&gt;
&gt;&gt;&gt; MT-ECDLP also admits a more efficient basic unit of computation in brute 
&gt;&gt;&gt; force attacks (including Grover) by using hashes instead of EC point 
&gt;&gt;&gt; multiplications. If I instead start by picking scalar t&#8203; and fix the 
&gt;&gt;&gt; target point T = t*G&#8203;, then I can run a brute-force preimage search on 
&gt;&gt;&gt; SHA256 until I find m&#8203; such that SHA256(m) == x(T)&#8203;. This can also be 
&gt;&gt;&gt; scaled up using a multi-target attack [1].
&gt;&gt;&gt;
&gt;&gt;&gt; With ST-ECDLP, we have only a single fixed message m = G&#8203;, and so the 
&gt;&gt;&gt; attacker can&#39;t use those multi-target cheat codes. They can parallelize, 
&gt;&gt;&gt; use pollard-rho or Shor or other algorithms, but they have only a single 
&gt;&gt;&gt; target point that they must break to win the game.
&gt;&gt;&gt;
&gt;&gt;&gt; The method Pieter suggested using for the canary construction is 
&gt;&gt;&gt; equivalent to *single-target* ECDLP.
&gt;&gt;&gt;
&gt;&gt;&gt; I&#39;ve heard others (e.g. Tadge in this thread 
&gt;&gt;&gt; &lt;<a
href="https://groups.google.com/g/bitcoindev/c/LpWOcXMcvk8/m/DjaiWnViAQAJ">https://groups.google.com/g/bitcoindev/c/LpWOcXMcvk8/m/DjaiWnViAQAJ</a>&gt;) 
&gt;&gt;&gt; previously suggest using a script like OP_SHA256 OP_CHECKSIG&#8203; as a 
&gt;&gt;&gt; canary, where any spend of such a script would trigger the canary. This 
&gt;&gt;&gt; would be *multi-target* ECDLP.
&gt;&gt;&gt;
&gt;&gt;&gt; I&#39;m not sure which is better. 
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt;    - ST-ECDLP is less likely to be triggered early or mistakenly, and 
&gt;&gt;&gt;    is more tightly equivalent to ECDLP. 
&gt;&gt;&gt;    
&gt;&gt;&gt;
&gt;&gt;&gt;    - MT-ECDLP is more reflective of how real-world attackers behave on 
&gt;&gt;&gt;    Bitcoin (e.g. with thousands-to-millions of public keys available to attack 
&gt;&gt;&gt;    in parallel, and breaking even one is considered unacceptable).
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; I&#39;m slightly leanings towards a construction like Pieter&#39;s, featuring 
&gt;&gt;&gt; ST-ECDLP, just because I&#39;m not sure what other tricks could be used to 
&gt;&gt;&gt; potentially trigger MT-ECDLP classically or quantumly.
&gt;&gt;&gt;
&gt;&gt;&gt; We could also engineer a compromise between the two, where we limit the 
&gt;&gt;&gt; number of targets. For example, define the game like this:
&gt;&gt;&gt;
&gt;&gt;&gt; Given G&#8203;, find scalar a&#8203;&#8203; and 32-bit integer i&#8203;&#8203; such that a*G = 
&gt;&gt;&gt; lift_x(SHA256(G || i))&#8203;&#8203;.
&gt;&gt;&gt;
&gt;&gt;&gt; Then the adversary can only attack against at most 2^32 unique target 
&gt;&gt;&gt; points, and those targets are fixed forever, for any adversary. This is an 
&gt;&gt;&gt; easier problem than ST-ECDLP, but harder than MT-ECDLP. Maybe call it *limited 
&gt;&gt;&gt; multi-target ECDLP (LMT-ECDLP)*?
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; regards,
&gt;&gt;&gt; conduition
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; [1]: First, generate a bunch of target points. Sample scalar t&#8203; and compute 
&gt;&gt;&gt; T0 = t * G&#8203;, T1 = T0 + T0, and T2 = T1 + T1, and T3 = T2 + T2&#8203;, etc. 
&gt;&gt;&gt; Why double each point? point doubling is cheaper than addition or 
&gt;&gt;&gt; multiplication, and still covers the whole curve. Then we run a 
&gt;&gt;&gt; multi-target SHA256 preimage search over all targets [x(T0), x(T1), x(T2), 
&gt;&gt;&gt; x(T3), ...]&#8203;. If we have n&#8203; targets and curve order N&#8203;, then each message 
&gt;&gt;&gt; hash has an n/N&#8203;&#8203; chance of success. If we find a valid message m&#8203;, 
&gt;&gt;&gt; such that SHA256(m) == x(R_i)&#8203; for some target index i&#8203;, then we have 
&gt;&gt;&gt; found T_i = t * 2**i * G = lift_x(SHA256(m))&#8203;.
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; On Thursday, August 13th, 2026 at 2:02 AM, waxwing/ AdamISZ &lt;
&gt;&gt;&gt; ekag...@gmail&#8226;com&gt; wrote:
&gt;&gt;&gt;
&gt;&gt;&gt; This tripwire idea is interesting. Basically &#34;canary in consensus&#34;.
&gt;&gt;&gt;
&gt;&gt;&gt; I agree it&#39;s valuable. In the scenario of adversarial actor(s) gaining 
&gt;&gt;&gt; access to CQRC first, i.e. no whitehats, only blackhats, obviously nothing 
&gt;&gt;&gt; to discuss; touching a NUMS ECDL is the last thing they&#39;ll do. So I&#39;m 
&gt;&gt;&gt; slightly worried that the general userbase will not notice that point, 
&gt;&gt;&gt; instead thinking it&#39;s a solid defense when it ... depends.
&gt;&gt;&gt;
&gt;&gt;&gt; In the scenario of at least some whitehats, we get wires tripped, or 
&gt;&gt;&gt; canaries singing. Having it in consensus is nice. The blockchain then does 
&gt;&gt;&gt; its job of being an unambiguous signal and we can have all the arguments 
&gt;&gt;&gt; well ahead of time. [1]
&gt;&gt;&gt;
&gt;&gt;&gt; On the other hand, we traditionally design such systems adversarially, 
&gt;&gt;&gt; right, so you could argue that an overfocus on this might be suboptimal - 
&gt;&gt;&gt; it might be better to do other things.
&gt;&gt;&gt;
&gt;&gt;&gt; (Similar comment applies to the &#39;smaller group canary&#39; - definitely 
&gt;&gt;&gt; nothing wrong with it, but it is not in itself a defence unless we strongly 
&gt;&gt;&gt; believe whitehats, and *active* whitehats at that, are keeping up). An 
&gt;&gt;&gt; obvious question to raise: would we consider tripwiring a 192 bit group 
&gt;&gt;&gt; break of a similar type (NUMS)? I find that ... plausible?
&gt;&gt;&gt;
&gt;&gt;&gt; &gt; The BIP341 NUMS point (which I suggest using in this context) is the 
&gt;&gt;&gt; point whose X coordinate is the SHA256 hash of the generator point G. This 
&gt;&gt;&gt; guarantees that the NUMS point cannot predate G (if it did, it would be 
&gt;&gt;&gt; possible in theory that secp256k1&#39;s designers actually chose G in function 
&gt;&gt;&gt; of what we call that NUMS point, giving it a DLP known to them).
&gt;&gt;&gt;
&gt;&gt;&gt; w.r.t. &#39;This guarantees that the NUMS point cannot predate G&#39; yes based 
&gt;&gt;&gt; on SHA2 preimage resistance, but: isn&#39;t the real point that we&#39;re relying 
&gt;&gt;&gt; on SHA-2 not being a naughty function so that you couldn&#39;t find G = a * B 
&gt;&gt;&gt; and SHA2(G) = b*B for some base B in some feasible computation (sans CQRC 
&gt;&gt;&gt; of course, as was likely back then!). I have no idea what precise name you 
&gt;&gt;&gt; give to that property. OK, this is a ridiculous thing to discuss, perhaps, 
&gt;&gt;&gt; given when SHA2 and secp256k1 were standardized :) And given the encoding 
&gt;&gt;&gt; choices for our BIP341 NUMS (iirc the same as for Elements back in the day? 
&gt;&gt;&gt; using uncompressed encoding?) were able to be counted on the fingers of the 
&gt;&gt;&gt; hand which the sleeve does not cover :)
&gt;&gt;&gt;
&gt;&gt;&gt; [1] I take Antoine&#39;s point that making it consensus means the miners are 
&gt;&gt;&gt; involved and there is a non-trivial collusion risk if the stakes are high, 
&gt;&gt;&gt; but I can&#39;t see how this scenario is *worse* than no tripwire?
&gt;&gt;&gt;
&gt;&gt;&gt; On Sunday, July 5, 2026 at 4:07:33&#8239;PM UTC-6 Antoine Riard wrote:
&gt;&gt;&gt;
&gt;&gt;&gt;&gt; Hi Pieter,
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; Thanks for the observations.
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; When I was saying there is a problem with the game theory,
&gt;&gt;&gt;&gt; it&#39;s that strikingly, any activation of the tripwire logic
&gt;&gt;&gt;&gt; would rely on a &#34;flag&#34; transaction being mined in the chain
&gt;&gt;&gt;&gt; for the network nodes starting to enforce at the block N or
&gt;&gt;&gt;&gt; N+1 or whatever the EC disabling threshold.
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; Any &#34;flag&#34; transaction can be itself re-orged out of the chain
&gt;&gt;&gt;&gt; to purely disable the effects of the EC disabling threshold,
&gt;&gt;&gt;&gt; therefore make it null and void as an effect. One might see
&gt;&gt;&gt;&gt; it as a competing race between a group of &#34;sunsetting&#34; users
&gt;&gt;&gt;&gt; and a (majority) coalition of miners in coordination with a
&gt;&gt;&gt;&gt; CRQC adversary, where the latter have an interest and the
&gt;&gt;&gt;&gt; hashrate capabilities to do a tx-withold [0].
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; In pure terms of satoshi fee denominated calculus, empirically
&gt;&gt;&gt;&gt; global miners have won an average of $20 B yearly. If we only
&gt;&gt;&gt;&gt; consider that P2PK are going to be frozen by the tripwire effect,
&gt;&gt;&gt;&gt; as for most of them it might be assumed they will never move to
&gt;&gt;&gt;&gt; a safer format, we talk already about 1.7 M of coins or as of
&gt;&gt;&gt;&gt; today valuation $107 B (the information is on the chain and can
&gt;&gt;&gt;&gt; be verified).
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; That&#39;s $107B can &#34;burn&#34; in revenue or income that a CRQC-enabled
&gt;&gt;&gt;&gt; miners coalition to constantly reorg-out the &#34;flag&#34; tx out of the
&gt;&gt;&gt;&gt; chain. In other terms, something like 5 years of income, and I
&gt;&gt;&gt;&gt; kindly do not count all the loss coins that are likely to amount
&gt;&gt;&gt;&gt; to a far bigger &#34;tripwire&#34; neutralization budget.
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; In the name of what a majority of miners will gracefully let on
&gt;&gt;&gt;&gt; the table an opportunity of massive income ?
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; Leveraging Shor the exploitation might be even done anonymously
&gt;&gt;&gt;&gt; as the mining process is done. Not even certainty, by who the
&gt;&gt;&gt;&gt; EC-protected coins could be covertly exfiltrated.
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; That&#39;s the most striking problem when you think about the math
&gt;&gt;&gt;&gt; with any &#34;tripwire&#34; approach, or even an &#34;hourglass&#34; one relying
&gt;&gt;&gt;&gt; on a &#34;flag&#34; transaction [1]. I&#39;m ruling out &#34;checkpoints&#34; and
&gt;&gt;&gt;&gt; any other trust-the-dev approach, as that&#39;s even worst [2].
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; As you&#39;re introducing post is resounding, what the miners
&gt;&gt;&gt;&gt; are saying now, there are no guarantees on how they would use
&gt;&gt;&gt;&gt; their hashrate down the road, potentially 10 or 20 years from now.
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; Beyond, and to answer back your point, I still think you can
&gt;&gt;&gt;&gt; manage an escape hatch of the &#34;tripwire&#34; effect, it&#39;s all depends
&gt;&gt;&gt;&gt; how the script tripwire logic is implemented, but if you have
&gt;&gt;&gt;&gt; two OP_SUCCESS of different kinds before your EC CHECKSIG, you
&gt;&gt;&gt;&gt; can always have a &#34;soft-fork&#34; after the &#34;tripwire&#34; to return 
&gt;&gt;&gt;&gt; true on the stack, with an EC or hashlock as a success (I agree
&gt;&gt;&gt;&gt; using undefined op_success in a script is not safe at all) [3].
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; Best,
&gt;&gt;&gt;&gt; Antoine
&gt;&gt;&gt;&gt; OTS hash: 
&gt;&gt;&gt;&gt; 4bc91d8dee1625f6e78b27c88bced8e405f25ef6d3d8fd59be8016db5b0fbe66
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; [0] See naumenkog&#39;s 
&gt;&gt;&gt;&gt; <a
href="https://www.bitmex.com/blog/txwithhold-smart-contracts">https://www.bitmex.com/blog/txwithhold-smart-contracts</a>
&gt;&gt;&gt;&gt; [1] This is sad, as the &#34;hourglass&#34; depending how the parameters are 
&gt;&gt;&gt;&gt; chosen
&gt;&gt;&gt;&gt; was a more acceptable trade-off than pure sunsetting.
&gt;&gt;&gt;&gt; [2] Given the amounts at stake to sunset, as a group of developers you
&gt;&gt;&gt;&gt; would just paint yourself a target, there are more even funds at stake
&gt;&gt;&gt;&gt; that Satoshi herself / himself is assumed to have.
&gt;&gt;&gt;&gt; [3] There is no security proof in BIP341 on the unforgeability of the
&gt;&gt;&gt;&gt; NUMS point, if it binds in the ROM or whatever.
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; Le sam. 4 juil. 2026 &#224; 13:47, Sjors Provoost &lt;sj...@sprovoost&#8226;nl&gt; a 
&gt;&gt;&gt;&gt; &#233;crit :
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt;&gt; On Fri, Jul 3, 2026, at 23:23, Pieter Wuille wrote:
&gt;&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt;&gt; [...]
&gt;&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt;&gt; &gt; * Just publishing the DLP in a transaction (e.g. OP_RETURN with a 
&gt;&gt;&gt;&gt;&gt; &gt; specific marker). This is smaller than a full transaction input + 
&gt;&gt;&gt;&gt;&gt; &gt; signature.
&gt;&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt;&gt; &gt; * Similarly, but publishing in the coinbase, and requiring relay 
&gt;&gt;&gt;&gt;&gt; using 
&gt;&gt;&gt;&gt;&gt; &gt; a separate message. Less places a node needs to check, but I&#39;m 
&gt;&gt;&gt;&gt;&gt; &gt; concerned about the difficulty of testing infrastructure that relay 
&gt;&gt;&gt;&gt;&gt; of 
&gt;&gt;&gt;&gt;&gt; &gt; such a message works
&gt;&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt;&gt; [...]
&gt;&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt;&gt; &gt; On Saturday, June 27th, 2026 at 12:33 AM, Anthony Towns 
&gt;&gt;&gt;&gt;&gt; &gt; &lt;a...@erisian&#8226;com.au&gt; wrote:
&gt;&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt;&gt; &gt;&gt; A slight variant of this approach would be to have a 128 byte value 
&gt;&gt;&gt;&gt;&gt; &#34;aRsm&#34;, such that P = N+a*G, N is the BIP-341 NUMS point, and Rs is a 
&gt;&gt;&gt;&gt;&gt; BIP340 signature of m by P. That would allow the victim of post-quantum 
&gt;&gt;&gt;&gt;&gt; theft via a key-path spend of a BIP341 NUMS IPK to trigger the tripwire, in 
&gt;&gt;&gt;&gt;&gt; addition to someone who has direct access to a CRQC.
&gt;&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt;&gt; &gt; Indeed, I had considered something similar, but see above for why 
&gt;&gt;&gt;&gt;&gt; I&#39;m 
&gt;&gt;&gt;&gt;&gt; &gt; not convinced supporting non-cooperative CRQCs is that useful.
&gt;&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt;&gt; &gt; Also, in my view the tripwire isn&#39;t really a security feature on 
&gt;&gt;&gt;&gt;&gt; itself 
&gt;&gt;&gt;&gt;&gt; &gt; (it&#39;s not expected to trigger...), but more something that sets 
&gt;&gt;&gt;&gt;&gt; &gt; expectations around the output type for prospective users.
&gt;&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt;&gt; &gt; In that sense, the question is really whether supporting 
&gt;&gt;&gt;&gt;&gt; &gt; non-cooperative CRQCs helps set that expectation more than only 
&gt;&gt;&gt;&gt;&gt; &gt; cooperative ones, which are definitely easier to support.
&gt;&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt;&gt; &gt;&gt; I think it could make sense to have the tripwire be included in the 
&gt;&gt;&gt;&gt;&gt; block via the coinbase witness commitment output, rather than having it be 
&gt;&gt;&gt;&gt;&gt; locked to a transaction, so you only having to check the coinbase for the 
&gt;&gt;&gt;&gt;&gt; magic rather than every transaction. That would require a separate P2P 
&gt;&gt;&gt;&gt;&gt; message to relay the necessary ECDL-break proof to miners, and would 
&gt;&gt;&gt;&gt;&gt; probably need stratumv2 or a getblocktemplate update in order for the node 
&gt;&gt;&gt;&gt;&gt; to be able to tell pools to actually include that info in the coinbase.
&gt;&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt;&gt; &gt; I worry this is untestable, really. You&#39;d need things like 
&gt;&gt;&gt;&gt;&gt; &gt; fake-tripwires to be supported through the same message which don&#39;t 
&gt;&gt;&gt;&gt;&gt; &gt; require an ECDLP break, and still propagate. And then that needs DoS 
&gt;&gt;&gt;&gt;&gt; &gt; protection measures, 
&gt;&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt;&gt; I whipped something up last weekend:
&gt;&gt;&gt;&gt;&gt; <a
href="https://github.com/Sjors/bitcoin/pull/121">https://github.com/Sjors/bitcoin/pull/121</a>
&gt;&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt;&gt; It seems straightforward, but maybe I missed something:
&gt;&gt;&gt;&gt;&gt; - for test code we use a fake NUMS point, so we can generate &#34;proof&#34; 
&gt;&gt;&gt;&gt;&gt; without a quantum computer
&gt;&gt;&gt;&gt;&gt; - a p2p message floods the proof
&gt;&gt;&gt;&gt;&gt; - nodes ignore the message if they already have *any* valid proof
&gt;&gt;&gt;&gt;&gt; - verifying p2p proof candidates might need some rate limiting, but 
&gt;&gt;&gt;&gt;&gt; it&#39;s as cheap as verifying a transaction signature
&gt;&gt;&gt;&gt;&gt; - mining code includes the proof in a coinbase op_return, until the 
&gt;&gt;&gt;&gt;&gt; freeze activates
&gt;&gt;&gt;&gt;&gt; - with stratum v2 (and ipc mining clients in general this works out of 
&gt;&gt;&gt;&gt;&gt; the box, a small change is needed for getblocktemplate clients)
&gt;&gt;&gt;&gt;&gt; - since the proof is not in the header, we can&#39;t use the normal bip9 
&gt;&gt;&gt;&gt;&gt; style header scan to see if the rule activated. Instead the prototype 
&gt;&gt;&gt;&gt;&gt; stores it in a file along with a merkle inclusion proof, which is read when 
&gt;&gt;&gt;&gt;&gt; the node restarts.
&gt;&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt;&gt; With this mechanism it doesn&#39;t really need to be in the coinbase 
&gt;&gt;&gt;&gt;&gt; transaction, but that does seem more convenient and miners can censor it 
&gt;&gt;&gt;&gt;&gt; anyway.
&gt;&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt;&gt; - Sjors
&gt;&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt;&gt; -- 
&gt;&gt;&gt;&gt;&gt; You received this message because you are subscribed to a topic in the 
&gt;&gt;&gt;&gt;&gt; Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt;&gt;&gt;&gt;&gt; To unsubscribe from this topic, visit 
&gt;&gt;&gt;&gt;&gt; <a
href="https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe">https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe</a>.
&gt;&gt;&gt;&gt;&gt; To unsubscribe from this group and all its topics, send an email to 
&gt;&gt;&gt;&gt;&gt; bitcoindev+...@googlegroups&#8226;com.
&gt;&gt;&gt;&gt;&gt; To view this discussion visit 
&gt;&gt;&gt;&gt;&gt; <a
href="https://groups.google.com/d/msgid/bitcoindev/002f2395-7d5d-4cb6-852c-e991aa1f0eb3%40app.fastmail.com">https://groups.google.com/d/msgid/bitcoindev/002f2395-7d5d-4cb6-852c-e991aa1f0eb3%40app.fastmail.com</a>
&gt;&gt;&gt;&gt;&gt; .
&gt;&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; -- 
&gt;&gt;&gt;
&gt;&gt;&gt; You received this message because you are subscribed to the Google 
&gt;&gt;&gt; Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt;&gt;&gt; To unsubscribe from this group and stop receiving emails from it, send 
&gt;&gt;&gt; an email to bitcoindev+...@googlegroups&#8226;com.
&gt;&gt;&gt; To view this discussion visit 
&gt;&gt;&gt; <a
href="https://groups.google.com/d/msgid/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can%40googlegroups.com</a>
&gt;&gt;&gt; .
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; -- 
&gt;&gt; You received this message because you are subscribed to the Google Groups 
&gt;&gt; &#34;Bitcoin Development Mailing List&#34; group.
&gt;&gt; To unsubscribe from this group and stop receiving emails from it, send an 
&gt;&gt; email to bitcoindev+...@googlegroups&#8226;com.
&gt;&gt;
&gt;&gt; To view this discussion visit 
&gt;&gt; <a
href="https://groups.google.com/d/msgid/bitcoindev/fd947d7c-86fd-407c-98aa-0a63b8be28fan%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/fd947d7c-86fd-407c-98aa-0a63b8be28fan%40googlegroups.com</a>
&gt;&gt; .
&gt;&gt;
&gt;&gt;
&gt;&gt;
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/22f8b95d-403c-4a3e-ad64-221faf2ea851n%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/22f8b95d-403c-4a3e-ad64-221faf2ea851n%40googlegroups.com</a>.

<a
href="https://gnusha.org/pi/bitcoindev/22f8b95d-403c-4a3e-ad64-221faf2ea851n@googlegroups.com/1.2-a.bin">[-- Attachment #1.2: Type: text/html, Size: 42284 bytes --]</a>
</pre></div></content></entry><entry><author><name>waxwing/ AdamISZ</name><email>ekaggata@gmail.com</email></author><title>Re: [bitcoindev] Giving teeth to expected EC disabling: P2XX(-T)(-ML)</title><updated>2026-08-15T18:12:53Z</updated><link
href="https://gnusha.org/pi/bitcoindev/d84e4a53-f3b1-4cd1-9a86-9591ec8c7211n@googlegroups.com/"/><id>urn:uuid:0099bad1-4b7f-e152-0ef5-99e5a30e91ba</id><thr:in-reply-to
ref="urn:uuid:b4162650-79e3-24d2-5820-1e0d61e28c91"
href="https://gnusha.org/pi/bitcoindev/irB0rm4rUG6GyaLnf1vUsNFW8BBJXAuh8-FIJ_s75xjgFgbOuTdaEGQ30PYzjtawVv5UVIC5xs7Uq_Cm9BPSyC73A-xGwT5J2oYsKE8QiPE=@proton.me/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/d84e4a53-f3b1-4cd1-9a86-9591ec8c7211n@googlegroups.com/1.1-a.txt">[-- Attachment #1.1: Type: text/plain, Size: 26191 bytes --]</a>

As if everything wasn&#39;t confusing enough, I also made one very notable 
error: What I was saying here:

<span
class="q">&gt; This is relevant because the hypothetical evil curve-generator who is 
</span>trying to poison the future H=SHA2(G) has an easier time in doing so, than 
a future canary-solver who obviously cannot try different values of G :)

is, I&#39;m pretty sure, not correct: the canary-solver only needs 2^128 work 
anyway (all the normal classical collision finding); it&#39;s not like he has 
to use pure brute force.

<span
class="q">&gt; If we have any doubt about that, we could tweak the hash function with 
</span>some data that is newer than G but still unbiased, e.g. the hash of the 
genesis block, or the hash of the first block in which the canary goes live 
(idea credit: Tadge Dryja 
&lt;<a
href="https://youtu.be/PmW90HX89P8?si=NhRJSaxKILVAJBkr&#38;t=841">https://youtu.be/PmW90HX89P8?si=NhRJSaxKILVAJBkr&#38;t=841</a>&gt;).

Seems plausible.

I guess two tracks of conversation here; I&#39;m still genuinely curious what 
people think about 192 bit and whether we can do it practically, because, 
depending on how it plays out, it might buy very useful time. The delving 
thread was focused on distributed keygen and ZKP for the canary, but this 
is obviously way less trustless than NUMS, so perhaps that&#39;s the end of 
that, or perhaps there&#39;s something else clever I&#39;m not aware of.

On Saturday, August 15, 2026 at 10:54:11&#8239;AM UTC-6 conduition wrote:

<span
class="q">&gt; This is relevant because the hypothetical evil curve-generator who is 
&gt; trying to poison the future H=SHA2(G) has an easier time in doing so, than 
&gt; a future canary-solver who obviously cannot try different values of G :)
&gt;
&gt;
&gt; Ah sorry, I thought you were talking about canary solvers, didn&#39;t realize 
&gt; you were talking about curve designers. Agreed then, but still seems 
&gt; unlikely that G was chosen this way: 
&gt; <a
href="https://bitcoin.stackexchange.com/questions/58784/how-were-the-secp256k1-base-point-coordinates-decided">https://bitcoin.stackexchange.com/questions/58784/how-were-the-secp256k1-base-point-coordinates-decided</a>
&gt;
&gt; If we have any doubt about that, we could tweak the hash function with 
&gt; some data that is newer than G but still unbiased, e.g. the hash of the 
&gt; genesis block, or the hash of the first block in which the canary goes live 
&gt; (idea credit: Tadge Dryja 
&gt; &lt;<a
href="https://youtu.be/PmW90HX89P8?si=NhRJSaxKILVAJBkr&#38;t=841">https://youtu.be/PmW90HX89P8?si=NhRJSaxKILVAJBkr&#38;t=841</a>&gt;).
&gt;
&gt; interesting point is that Shor can target any specific dlog problem, 
&gt; right. So I do think the ST is the correct version of the problem?
&gt;
&gt;
&gt; Yes, I believe so. I don&#39;t know of any way to batch Shor&#39;s algorithm in a 
&gt; multi-target attack that is any more efficient than a trivial one-by-one 
&gt; attack, so using MT-ECDLP seems like it only serves to makes classical 
&gt; attacks (or Grover&#39;s search) easier.
&gt;
&gt; regards,
&gt; conduition
&gt;
&gt; On Saturday, August 15th, 2026 at 10:14 AM, waxwing/ AdamISZ &lt;
&gt; ekag...@gmail&#8226;com&gt; wrote:
&gt;
&gt; &gt; A 192-bit curve i think should be reasonable as a canary, but consider 
&gt; this: If someone already has a QC that breaks 192-bit ECC, how long until 
&gt; they build one which breaks 256-bit ECC? A day, a week, a year? No way of 
&gt; knowing. If the delay is too long, users may see the canary as a 
&gt; false-positive, and migrate back to vulnerable addresses, and they might 
&gt; even be right. 192-bit canaries are vulnerable to classical attack with 
&gt; work approximately 2^96. We should bear in mind the possibility that such a 
&gt; canary could be activated possibly very early, well before Q-day, possibly 
&gt; even in the absence of any quantum computers.
&gt;
&gt; Agreed that is unlikely a big delta, in the nature of these things (QCs), 
&gt; between 192 and 256. Including that it&#39;s obvious that going very much below 
&gt; 192 means classical attack and therefore bad idea. Which is why I said 192 
&gt; and not sub 160. What&#39;s not obvious is that 192 is worse than 256 here. It 
&gt; may only give us a small amount of extra time, but it won&#39;t give us 
&gt; negative extra time. So the tradeoff is, presumably, whether the additional 
&gt; complexity (which is a bit tricky from what I recall [1], but there will 
&gt; definitely be experts out there who can clean it up) is worth it.
&gt;
&gt; The idea of &#39;people will think it a false positive&#39;, disagree, I think the 
&gt; whole tripwire idea is likely a *bit* vulnerable to genpop misunderstanding 
&gt; as I said in my previous post, but this particular thing I don&#39;t see it: a 
&gt; 192 bit being broken is *very* likely to cause an appropriate level of 
&gt; panic.
&gt;
&gt; &gt; Anyone can find G = a * B&#8203;. Just generate a key and invert your secret 
&gt; key.
&gt;
&gt; &gt; P = a * G&#8203;
&gt; &gt; G = a**-1 * P
&gt;
&gt; &gt; The hard part is then finding some b such that b*G = SHA256(G).
&gt;
&gt; You slightly missed my point here, I think? The idea is that if you set up 
&gt; two sides that are both sample-able, you can birthday. Like, you keep 
&gt; sampling a on one side and b on the other. Build tables of both sides. Then 
&gt; all you have to do is check whether SHA2 of the LHS ever matches the RHS. 
&gt; This gives you a square root style speedup a la birthday attack. Contrast 
&gt; with if you just fix G, then keep searching for matches: no square root 
&gt; speedup. This is relevant because the hypothetical evil curve-generator who 
&gt; is trying to poison the future H=SHA2(G) has an easier time in doing so, 
&gt; than a future canary-solver who obviously cannot try different values of G 
&gt; :)
&gt;
&gt; About your single-target vs multi-target distinction: interesting point is 
&gt; that Shor can target any specific dlog problem, right. So I do think the ST 
&gt; is the correct version of the problem? But actually I am quite unsure and 
&gt; unclear about those ST, MT, LMT distinctions you&#39;re making; specifically I 
&gt; mean, I am very unsure about how they differ in costs.
&gt;
&gt; As for characterizing the problem, I think it&#39;s fair to say: if you 
&gt; assumed SHA2 was a proper random oracle then we have with SHA2(enc(G)), 
&gt; something that&#39;s very tightly equivalent to ECDLP, which is what we want. 
&gt; If we want to pay attention to the fact that SHA2 is an actual hash 
&gt; function and not an RO, then I think there&#39;s some statement like &#34;assuming 
&gt; SHA2 has no structure &#34;matching&#34; secp256k1, then it&#39;s tightly equivalent to 
&gt; ECDLP on secp256k1&#34; which is obviously horrendously vague, but would not be 
&gt; very easy to write down properly.
&gt;
&gt; Another observation, probably it already exists up-thread: we obviously 
&gt; don&#39;t want to *literally* use BIP341&#39;s H on a 256 bit tripwire, because 
&gt; then a Shor-break directly steals a bunch of coins, so what should we use? 
&gt; Maybe SHA2(SHA2(enc(G)) ?
&gt;
&gt;
&gt; [1] 
&gt; <a
href="https://delvingbitcoin.org/t/qcap-a-bitcoin-native-quantum-canary-alert/2498/9">https://delvingbitcoin.org/t/qcap-a-bitcoin-native-quantum-canary-alert/2498/9</a>
&gt; On Friday, August 14, 2026 at 12:34:54&#8239;PM UTC-6 conduition wrote:
&gt;
&gt;&gt; An obvious question to raise: would we consider tripwiring a 192 bit 
&gt;&gt; group break of a similar type (NUMS)? I find that ... plausible?
&gt;&gt;
&gt;&gt;
&gt;&gt; A 192-bit curve i think should be reasonable as a canary, but consider 
&gt;&gt; this: If someone already has a QC that breaks 192-bit ECC, how long until 
&gt;&gt; they build one which breaks 256-bit ECC? A day, a week, a year? No way of 
&gt;&gt; knowing. If the delay is too long, users may see the canary as a 
&gt;&gt; false-positive, and migrate back to vulnerable addresses, and they might 
&gt;&gt; even be right. 192-bit canaries are vulnerable to classical attack with 
&gt;&gt; work approximately 2^96. We should bear in mind the possibility that such a 
&gt;&gt; canary could be activated possibly very early, well before Q-day, possibly 
&gt;&gt; even in the absence of any quantum computers.
&gt;&gt;
&gt;&gt; Ideally we want a short gap between &#34;192-bit is broken&#34; and &#34;256-bit is 
&gt;&gt; broken&#34;, but not so short as to make the 192-bit canary effectively 
&gt;&gt; fungible with a 256-bit canary (because then it&#39;s less likely to be 
&gt;&gt; activated before theft occurs).
&gt;&gt;
&gt;&gt; w.r.t. &#39;This guarantees that the NUMS point cannot predate G&#39; yes based 
&gt;&gt; on SHA2 preimage resistance, but: isn&#39;t the real point that we&#39;re relying 
&gt;&gt; on SHA-2 not being a naughty function so that you couldn&#39;t find G = a * B 
&gt;&gt; and SHA2(G) = b*B for some base B in some feasible computation (sans CQRC 
&gt;&gt; of course, as was likely back then!). I have no idea what precise name you 
&gt;&gt; give to that property. OK, this is a ridiculous thing to discuss, perhaps, 
&gt;&gt; given when SHA2 and secp256k1 were standardized :) And given the encoding 
&gt;&gt; choices for our BIP341 NUMS (iirc the same as for Elements back in the day? 
&gt;&gt; using uncompressed encoding?) were able to be counted on the fingers of the 
&gt;&gt; hand which the sleeve does not cover :)
&gt;&gt;
&gt;&gt;
&gt;&gt; Anyone can find G = a * B&#8203;. Just generate a key and invert your secret 
&gt;&gt; key.
&gt;&gt;
&gt;&gt; P = a * G&#8203;
&gt;&gt; G = a**-1 * P
&gt;&gt;
&gt;&gt; The hard part is then finding some b such that b*G = SHA256(G).
&gt;&gt;
&gt;&gt; ---------
&gt;&gt;
&gt;&gt; If we reflect on the requirement that G&#8203; is fixed, we see SHA256(G)&#8203; is 
&gt;&gt; also fixed as a pseudorandom challenge point. The reason for using SHA256 
&gt;&gt; instead of, say, picking an arbitary point by committee or using digits of 
&gt;&gt; pi or some other trickery, is that hash outputs are supposed to be random 
&gt;&gt; and so SHA256(G)&#8203; is (assumably) a random ECDLP challenge. This matches 
&gt;&gt; the classical definition of ECDLP more tightly: Given an arbitrary point 
&gt;&gt; P&#8203;, find p&#8203; such that P = p * G&#8203;. The assumption is that if an attacker 
&gt;&gt; can factor an honestly-sampled challenge point, they can factor any point. 
&gt;&gt; SHA256 is just a stand-in for the &#34;honestly-sampled&#34; part.
&gt;&gt;
&gt;&gt; However, the following two tasks are actually very different:
&gt;&gt;
&gt;&gt;
&gt;&gt;    1. Given G, find scalar a&#8203; such that a*G = lift_x(SHA256(G))&#8203;.
&gt;&gt;    2. Given G, find scalar a&#8203; and message m&#8203; such that a*G = 
&gt;&gt;    lift_x(SHA256(m))&#8203;.
&gt;&gt;
&gt;&gt;
&gt;&gt; In the case of task 1, if we assume SHA256 output is random, then this is 
&gt;&gt; more tightly equivalent to ECDLP, because the point we&#39;re trying to factor 
&gt;&gt; is a fixed target, as is the one sampled honestly by the ECDLP security 
&gt;&gt; game.
&gt;&gt;
&gt;&gt; In the case of task 2, the attacker can sample arbitrary messages to 
&gt;&gt; create multiple *target points*, and the attacker wins if they succeed 
&gt;&gt; in factoring any of them. The attacker can attack all those target points 
&gt;&gt; concurrently if they want, and they get a speedup from doing so.
&gt;&gt;
&gt;&gt; So I believe it is worth disambiguating canaries between the two cases, 
&gt;&gt; because they are different security notions. The first (1) I would call *single-target 
&gt;&gt; ECDLP *(ST-ECDLP), and the second (2) I would call *multi-target ECDLP *
&gt;&gt; (MT-ECDLP).
&gt;&gt;
&gt;&gt; It&#39;s pretty clear that MT-ECDLP is easier to break, because attackers can 
&gt;&gt; make progress against more than one target concurrently, and breaking any 
&gt;&gt; one is sufficient to win the security game.
&gt;&gt;
&gt;&gt; For example, say I sample 2 different messages m1&#8203; and m2&#8203;, and compute 
&gt;&gt; ECDLP target points T1 = lift_x(SHA256(m1))&#8203; and T2 = lift_x(SHA256(m2))&#8203;. 
&gt;&gt; Then if I sample a random scalar r&#8203; and compute R = r*G&#8203;, I have two 
&gt;&gt; potential chances of success: R == T1&#8203; OR R == T2&#8203;. I can scale up this 
&gt;&gt; advantage by generating more targets, T3&#8203;, T4&#8203;, ... and so on.
&gt;&gt;
&gt;&gt; MT-ECDLP also admits a more efficient basic unit of computation in brute 
&gt;&gt; force attacks (including Grover) by using hashes instead of EC point 
&gt;&gt; multiplications. If I instead start by picking scalar t&#8203; and fix the 
&gt;&gt; target point T = t*G&#8203;, then I can run a brute-force preimage search on 
&gt;&gt; SHA256 until I find m&#8203; such that SHA256(m) == x(T)&#8203;. This can also be 
&gt;&gt; scaled up using a multi-target attack [1].
&gt;&gt;
&gt;&gt; With ST-ECDLP, we have only a single fixed message m = G&#8203;, and so the 
&gt;&gt; attacker can&#39;t use those multi-target cheat codes. They can parallelize, 
&gt;&gt; use pollard-rho or Shor or other algorithms, but they have only a single 
&gt;&gt; target point that they must break to win the game.
&gt;&gt;
&gt;&gt; The method Pieter suggested using for the canary construction is 
&gt;&gt; equivalent to *single-target* ECDLP.
&gt;&gt;
&gt;&gt; I&#39;ve heard others (e.g. Tadge in this thread 
&gt;&gt; &lt;<a
href="https://groups.google.com/g/bitcoindev/c/LpWOcXMcvk8/m/DjaiWnViAQAJ">https://groups.google.com/g/bitcoindev/c/LpWOcXMcvk8/m/DjaiWnViAQAJ</a>&gt;) 
&gt;&gt; previously suggest using a script like OP_SHA256 OP_CHECKSIG&#8203; as a 
&gt;&gt; canary, where any spend of such a script would trigger the canary. This 
&gt;&gt; would be *multi-target* ECDLP.
&gt;&gt;
&gt;&gt; I&#39;m not sure which is better. 
&gt;&gt;
&gt;&gt;
&gt;&gt;    - ST-ECDLP is less likely to be triggered early or mistakenly, and is 
&gt;&gt;    more tightly equivalent to ECDLP. 
&gt;&gt;    
&gt;&gt;
&gt;&gt;    - MT-ECDLP is more reflective of how real-world attackers behave on 
&gt;&gt;    Bitcoin (e.g. with thousands-to-millions of public keys available to attack 
&gt;&gt;    in parallel, and breaking even one is considered unacceptable).
&gt;&gt;
&gt;&gt;
&gt;&gt; I&#39;m slightly leanings towards a construction like Pieter&#39;s, featuring 
&gt;&gt; ST-ECDLP, just because I&#39;m not sure what other tricks could be used to 
&gt;&gt; potentially trigger MT-ECDLP classically or quantumly.
&gt;&gt;
&gt;&gt; We could also engineer a compromise between the two, where we limit the 
&gt;&gt; number of targets. For example, define the game like this:
&gt;&gt;
&gt;&gt; Given G&#8203;, find scalar a&#8203;&#8203; and 32-bit integer i&#8203;&#8203; such that a*G = 
&gt;&gt; lift_x(SHA256(G || i))&#8203;&#8203;.
&gt;&gt;
&gt;&gt; Then the adversary can only attack against at most 2^32 unique target 
&gt;&gt; points, and those targets are fixed forever, for any adversary. This is an 
&gt;&gt; easier problem than ST-ECDLP, but harder than MT-ECDLP. Maybe call it *limited 
&gt;&gt; multi-target ECDLP (LMT-ECDLP)*?
&gt;&gt;
&gt;&gt;
&gt;&gt; regards,
&gt;&gt; conduition
&gt;&gt;
&gt;&gt;
&gt;&gt; [1]: First, generate a bunch of target points. Sample scalar t&#8203; and compute 
&gt;&gt; T0 = t * G&#8203;, T1 = T0 + T0, and T2 = T1 + T1, and T3 = T2 + T2&#8203;, etc. Why 
&gt;&gt; double each point? point doubling is cheaper than addition or 
&gt;&gt; multiplication, and still covers the whole curve. Then we run a 
&gt;&gt; multi-target SHA256 preimage search over all targets [x(T0), x(T1), x(T2), 
&gt;&gt; x(T3), ...]&#8203;. If we have n&#8203; targets and curve order N&#8203;, then each message 
&gt;&gt; hash has an n/N&#8203;&#8203; chance of success. If we find a valid message m&#8203;, such 
&gt;&gt; that SHA256(m) == x(R_i)&#8203; for some target index i&#8203;, then we have found T_i 
&gt;&gt; = t * 2**i * G = lift_x(SHA256(m))&#8203;.
&gt;&gt;
&gt;&gt;
&gt;&gt;
&gt;&gt;
&gt;&gt;
&gt;&gt; On Thursday, August 13th, 2026 at 2:02 AM, waxwing/ AdamISZ &lt;
&gt;&gt; ekag...@gmail&#8226;com&gt; wrote:
&gt;&gt;
&gt;&gt; This tripwire idea is interesting. Basically &#34;canary in consensus&#34;.
&gt;&gt;
&gt;&gt; I agree it&#39;s valuable. In the scenario of adversarial actor(s) gaining 
&gt;&gt; access to CQRC first, i.e. no whitehats, only blackhats, obviously nothing 
&gt;&gt; to discuss; touching a NUMS ECDL is the last thing they&#39;ll do. So I&#39;m 
&gt;&gt; slightly worried that the general userbase will not notice that point, 
&gt;&gt; instead thinking it&#39;s a solid defense when it ... depends.
&gt;&gt;
&gt;&gt; In the scenario of at least some whitehats, we get wires tripped, or 
&gt;&gt; canaries singing. Having it in consensus is nice. The blockchain then does 
&gt;&gt; its job of being an unambiguous signal and we can have all the arguments 
&gt;&gt; well ahead of time. [1]
&gt;&gt;
&gt;&gt; On the other hand, we traditionally design such systems adversarially, 
&gt;&gt; right, so you could argue that an overfocus on this might be suboptimal - 
&gt;&gt; it might be better to do other things.
&gt;&gt;
&gt;&gt; (Similar comment applies to the &#39;smaller group canary&#39; - definitely 
&gt;&gt; nothing wrong with it, but it is not in itself a defence unless we strongly 
&gt;&gt; believe whitehats, and *active* whitehats at that, are keeping up). An 
&gt;&gt; obvious question to raise: would we consider tripwiring a 192 bit group 
&gt;&gt; break of a similar type (NUMS)? I find that ... plausible?
&gt;&gt;
&gt;&gt; &gt; The BIP341 NUMS point (which I suggest using in this context) is the 
&gt;&gt; point whose X coordinate is the SHA256 hash of the generator point G. This 
&gt;&gt; guarantees that the NUMS point cannot predate G (if it did, it would be 
&gt;&gt; possible in theory that secp256k1&#39;s designers actually chose G in function 
&gt;&gt; of what we call that NUMS point, giving it a DLP known to them).
&gt;&gt;
&gt;&gt; w.r.t. &#39;This guarantees that the NUMS point cannot predate G&#39; yes based 
&gt;&gt; on SHA2 preimage resistance, but: isn&#39;t the real point that we&#39;re relying 
&gt;&gt; on SHA-2 not being a naughty function so that you couldn&#39;t find G = a * B 
&gt;&gt; and SHA2(G) = b*B for some base B in some feasible computation (sans CQRC 
&gt;&gt; of course, as was likely back then!). I have no idea what precise name you 
&gt;&gt; give to that property. OK, this is a ridiculous thing to discuss, perhaps, 
&gt;&gt; given when SHA2 and secp256k1 were standardized :) And given the encoding 
&gt;&gt; choices for our BIP341 NUMS (iirc the same as for Elements back in the day? 
&gt;&gt; using uncompressed encoding?) were able to be counted on the fingers of the 
&gt;&gt; hand which the sleeve does not cover :)
&gt;&gt;
&gt;&gt; [1] I take Antoine&#39;s point that making it consensus means the miners are 
&gt;&gt; involved and there is a non-trivial collusion risk if the stakes are high, 
&gt;&gt; but I can&#39;t see how this scenario is *worse* than no tripwire?
&gt;&gt;
&gt;&gt; On Sunday, July 5, 2026 at 4:07:33&#8239;PM UTC-6 Antoine Riard wrote:
&gt;&gt;
&gt;&gt;&gt; Hi Pieter,
&gt;&gt;&gt;
&gt;&gt;&gt; Thanks for the observations.
&gt;&gt;&gt;
&gt;&gt;&gt; When I was saying there is a problem with the game theory,
&gt;&gt;&gt; it&#39;s that strikingly, any activation of the tripwire logic
&gt;&gt;&gt; would rely on a &#34;flag&#34; transaction being mined in the chain
&gt;&gt;&gt; for the network nodes starting to enforce at the block N or
&gt;&gt;&gt; N+1 or whatever the EC disabling threshold.
&gt;&gt;&gt;
&gt;&gt;&gt; Any &#34;flag&#34; transaction can be itself re-orged out of the chain
&gt;&gt;&gt; to purely disable the effects of the EC disabling threshold,
&gt;&gt;&gt; therefore make it null and void as an effect. One might see
&gt;&gt;&gt; it as a competing race between a group of &#34;sunsetting&#34; users
&gt;&gt;&gt; and a (majority) coalition of miners in coordination with a
&gt;&gt;&gt; CRQC adversary, where the latter have an interest and the
&gt;&gt;&gt; hashrate capabilities to do a tx-withold [0].
&gt;&gt;&gt;
&gt;&gt;&gt; In pure terms of satoshi fee denominated calculus, empirically
&gt;&gt;&gt; global miners have won an average of $20 B yearly. If we only
&gt;&gt;&gt; consider that P2PK are going to be frozen by the tripwire effect,
&gt;&gt;&gt; as for most of them it might be assumed they will never move to
&gt;&gt;&gt; a safer format, we talk already about 1.7 M of coins or as of
&gt;&gt;&gt; today valuation $107 B (the information is on the chain and can
&gt;&gt;&gt; be verified).
&gt;&gt;&gt;
&gt;&gt;&gt; That&#39;s $107B can &#34;burn&#34; in revenue or income that a CRQC-enabled
&gt;&gt;&gt; miners coalition to constantly reorg-out the &#34;flag&#34; tx out of the
&gt;&gt;&gt; chain. In other terms, something like 5 years of income, and I
&gt;&gt;&gt; kindly do not count all the loss coins that are likely to amount
&gt;&gt;&gt; to a far bigger &#34;tripwire&#34; neutralization budget.
&gt;&gt;&gt;
&gt;&gt;&gt; In the name of what a majority of miners will gracefully let on
&gt;&gt;&gt; the table an opportunity of massive income ?
&gt;&gt;&gt;
&gt;&gt;&gt; Leveraging Shor the exploitation might be even done anonymously
&gt;&gt;&gt; as the mining process is done. Not even certainty, by who the
&gt;&gt;&gt; EC-protected coins could be covertly exfiltrated.
&gt;&gt;&gt;
&gt;&gt;&gt; That&#39;s the most striking problem when you think about the math
&gt;&gt;&gt; with any &#34;tripwire&#34; approach, or even an &#34;hourglass&#34; one relying
&gt;&gt;&gt; on a &#34;flag&#34; transaction [1]. I&#39;m ruling out &#34;checkpoints&#34; and
&gt;&gt;&gt; any other trust-the-dev approach, as that&#39;s even worst [2].
&gt;&gt;&gt;
&gt;&gt;&gt; As you&#39;re introducing post is resounding, what the miners
&gt;&gt;&gt; are saying now, there are no guarantees on how they would use
&gt;&gt;&gt; their hashrate down the road, potentially 10 or 20 years from now.
&gt;&gt;&gt;
&gt;&gt;&gt; Beyond, and to answer back your point, I still think you can
&gt;&gt;&gt; manage an escape hatch of the &#34;tripwire&#34; effect, it&#39;s all depends
&gt;&gt;&gt; how the script tripwire logic is implemented, but if you have
&gt;&gt;&gt; two OP_SUCCESS of different kinds before your EC CHECKSIG, you
&gt;&gt;&gt; can always have a &#34;soft-fork&#34; after the &#34;tripwire&#34; to return 
&gt;&gt;&gt; true on the stack, with an EC or hashlock as a success (I agree
&gt;&gt;&gt; using undefined op_success in a script is not safe at all) [3].
&gt;&gt;&gt;
&gt;&gt;&gt; Best,
&gt;&gt;&gt; Antoine
&gt;&gt;&gt; OTS hash: 
&gt;&gt;&gt; 4bc91d8dee1625f6e78b27c88bced8e405f25ef6d3d8fd59be8016db5b0fbe66
&gt;&gt;&gt;
&gt;&gt;&gt; [0] See naumenkog&#39;s 
&gt;&gt;&gt; <a
href="https://www.bitmex.com/blog/txwithhold-smart-contracts">https://www.bitmex.com/blog/txwithhold-smart-contracts</a>
&gt;&gt;&gt; [1] This is sad, as the &#34;hourglass&#34; depending how the parameters are 
&gt;&gt;&gt; chosen
&gt;&gt;&gt; was a more acceptable trade-off than pure sunsetting.
&gt;&gt;&gt; [2] Given the amounts at stake to sunset, as a group of developers you
&gt;&gt;&gt; would just paint yourself a target, there are more even funds at stake
&gt;&gt;&gt; that Satoshi herself / himself is assumed to have.
&gt;&gt;&gt; [3] There is no security proof in BIP341 on the unforgeability of the
&gt;&gt;&gt; NUMS point, if it binds in the ROM or whatever.
&gt;&gt;&gt;
&gt;&gt;&gt; Le sam. 4 juil. 2026 &#224; 13:47, Sjors Provoost &lt;sj...@sprovoost&#8226;nl&gt; a 
&gt;&gt;&gt; &#233;crit :
&gt;&gt;&gt;
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; On Fri, Jul 3, 2026, at 23:23, Pieter Wuille wrote:
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; [...]
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; &gt; * Just publishing the DLP in a transaction (e.g. OP_RETURN with a 
&gt;&gt;&gt;&gt; &gt; specific marker). This is smaller than a full transaction input + 
&gt;&gt;&gt;&gt; &gt; signature.
&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt; &gt; * Similarly, but publishing in the coinbase, and requiring relay 
&gt;&gt;&gt;&gt; using 
&gt;&gt;&gt;&gt; &gt; a separate message. Less places a node needs to check, but I&#39;m 
&gt;&gt;&gt;&gt; &gt; concerned about the difficulty of testing infrastructure that relay 
&gt;&gt;&gt;&gt; of 
&gt;&gt;&gt;&gt; &gt; such a message works
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; [...]
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt; &gt; On Saturday, June 27th, 2026 at 12:33 AM, Anthony Towns 
&gt;&gt;&gt;&gt; &gt; &lt;a...@erisian&#8226;com.au&gt; wrote:
&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt; &gt;&gt; A slight variant of this approach would be to have a 128 byte value 
&gt;&gt;&gt;&gt; &#34;aRsm&#34;, such that P = N+a*G, N is the BIP-341 NUMS point, and Rs is a 
&gt;&gt;&gt;&gt; BIP340 signature of m by P. That would allow the victim of post-quantum 
&gt;&gt;&gt;&gt; theft via a key-path spend of a BIP341 NUMS IPK to trigger the tripwire, in 
&gt;&gt;&gt;&gt; addition to someone who has direct access to a CRQC.
&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt; &gt; Indeed, I had considered something similar, but see above for why I&#39;m 
&gt;&gt;&gt;&gt; &gt; not convinced supporting non-cooperative CRQCs is that useful.
&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt; &gt; Also, in my view the tripwire isn&#39;t really a security feature on 
&gt;&gt;&gt;&gt; itself 
&gt;&gt;&gt;&gt; &gt; (it&#39;s not expected to trigger...), but more something that sets 
&gt;&gt;&gt;&gt; &gt; expectations around the output type for prospective users.
&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt; &gt; In that sense, the question is really whether supporting 
&gt;&gt;&gt;&gt; &gt; non-cooperative CRQCs helps set that expectation more than only 
&gt;&gt;&gt;&gt; &gt; cooperative ones, which are definitely easier to support.
&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt; &gt;&gt; I think it could make sense to have the tripwire be included in the 
&gt;&gt;&gt;&gt; block via the coinbase witness commitment output, rather than having it be 
&gt;&gt;&gt;&gt; locked to a transaction, so you only having to check the coinbase for the 
&gt;&gt;&gt;&gt; magic rather than every transaction. That would require a separate P2P 
&gt;&gt;&gt;&gt; message to relay the necessary ECDL-break proof to miners, and would 
&gt;&gt;&gt;&gt; probably need stratumv2 or a getblocktemplate update in order for the node 
&gt;&gt;&gt;&gt; to be able to tell pools to actually include that info in the coinbase.
&gt;&gt;&gt;&gt; &gt;
&gt;&gt;&gt;&gt; &gt; I worry this is untestable, really. You&#39;d need things like 
&gt;&gt;&gt;&gt; &gt; fake-tripwires to be supported through the same message which don&#39;t 
&gt;&gt;&gt;&gt; &gt; require an ECDLP break, and still propagate. And then that needs DoS 
&gt;&gt;&gt;&gt; &gt; protection measures, 
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; I whipped something up last weekend:
&gt;&gt;&gt;&gt; <a
href="https://github.com/Sjors/bitcoin/pull/121">https://github.com/Sjors/bitcoin/pull/121</a>
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; It seems straightforward, but maybe I missed something:
&gt;&gt;&gt;&gt; - for test code we use a fake NUMS point, so we can generate &#34;proof&#34; 
&gt;&gt;&gt;&gt; without a quantum computer
&gt;&gt;&gt;&gt; - a p2p message floods the proof
&gt;&gt;&gt;&gt; - nodes ignore the message if they already have *any* valid proof
&gt;&gt;&gt;&gt; - verifying p2p proof candidates might need some rate limiting, but 
&gt;&gt;&gt;&gt; it&#39;s as cheap as verifying a transaction signature
&gt;&gt;&gt;&gt; - mining code includes the proof in a coinbase op_return, until the 
&gt;&gt;&gt;&gt; freeze activates
&gt;&gt;&gt;&gt; - with stratum v2 (and ipc mining clients in general this works out of 
&gt;&gt;&gt;&gt; the box, a small change is needed for getblocktemplate clients)
&gt;&gt;&gt;&gt; - since the proof is not in the header, we can&#39;t use the normal bip9 
&gt;&gt;&gt;&gt; style header scan to see if the rule activated. Instead the prototype 
&gt;&gt;&gt;&gt; stores it in a file along with a merkle inclusion proof, which is read when 
&gt;&gt;&gt;&gt; the node restarts.
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; With this mechanism it doesn&#39;t really need to be in the coinbase 
&gt;&gt;&gt;&gt; transaction, but that does seem more convenient and miners can censor it 
&gt;&gt;&gt;&gt; anyway.
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; - Sjors
&gt;&gt;&gt;&gt;
&gt;&gt;&gt;&gt; -- 
&gt;&gt;&gt;&gt; You received this message because you are subscribed to a topic in the 
&gt;&gt;&gt;&gt; Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt;&gt;&gt;&gt; To unsubscribe from this topic, visit 
&gt;&gt;&gt;&gt; <a
href="https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe">https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe</a>.
&gt;&gt;&gt;&gt; To unsubscribe from this group and all its topics, send an email to 
&gt;&gt;&gt;&gt; bitcoindev+...@googlegroups&#8226;com.
&gt;&gt;&gt;&gt; To view this discussion visit 
&gt;&gt;&gt;&gt; <a
href="https://groups.google.com/d/msgid/bitcoindev/002f2395-7d5d-4cb6-852c-e991aa1f0eb3%40app.fastmail.com">https://groups.google.com/d/msgid/bitcoindev/002f2395-7d5d-4cb6-852c-e991aa1f0eb3%40app.fastmail.com</a>
&gt;&gt;&gt;&gt; .
&gt;&gt;&gt;&gt;
&gt;&gt;&gt; -- 
&gt;&gt;
&gt;&gt; You received this message because you are subscribed to the Google Groups 
&gt;&gt; &#34;Bitcoin Development Mailing List&#34; group.
&gt;&gt; To unsubscribe from this group and stop receiving emails from it, send an 
&gt;&gt; email to bitcoindev+...@googlegroups&#8226;com.
&gt;&gt; To view this discussion visit 
&gt;&gt; <a
href="https://groups.google.com/d/msgid/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can%40googlegroups.com</a>
&gt;&gt; .
&gt;&gt;
&gt;&gt;
&gt;&gt; -- 
&gt; You received this message because you are subscribed to the Google Groups 
&gt; &#34;Bitcoin Development Mailing List&#34; group.
&gt; To unsubscribe from this group and stop receiving emails from it, send an 
&gt; email to bitcoindev+...@googlegroups&#8226;com.
&gt;
&gt; To view this discussion visit 
&gt; <a
href="https://groups.google.com/d/msgid/bitcoindev/fd947d7c-86fd-407c-98aa-0a63b8be28fan%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/fd947d7c-86fd-407c-98aa-0a63b8be28fan%40googlegroups.com</a>
&gt; .
&gt;
&gt;
&gt;
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/d84e4a53-f3b1-4cd1-9a86-9591ec8c7211n%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/d84e4a53-f3b1-4cd1-9a86-9591ec8c7211n%40googlegroups.com</a>.

<a
href="https://gnusha.org/pi/bitcoindev/d84e4a53-f3b1-4cd1-9a86-9591ec8c7211n@googlegroups.com/1.2-a.bin">[-- Attachment #1.2: Type: text/html, Size: 39667 bytes --]</a>
</pre></div></content></entry><entry><author><name>&#39;conduition&#39; via Bitcoin Development Mailing List</name><email>bitcoindev@googlegroups.com</email></author><title>Re: [bitcoindev] Giving teeth to expected EC disabling: P2XX(-T)(-ML)</title><updated>2026-08-15T16:54:20Z</updated><link
href="https://gnusha.org/pi/bitcoindev/irB0rm4rUG6GyaLnf1vUsNFW8BBJXAuh8-FIJ_s75xjgFgbOuTdaEGQ30PYzjtawVv5UVIC5xs7Uq_Cm9BPSyC73A-xGwT5J2oYsKE8QiPE=@proton.me/"/><id>urn:uuid:b4162650-79e3-24d2-5820-1e0d61e28c91</id><thr:in-reply-to
ref="urn:uuid:ed8f2fb9-a063-047b-0d66-0ca087643e48"
href="https://gnusha.org/pi/bitcoindev/fd947d7c-86fd-407c-98aa-0a63b8be28fan@googlegroups.com/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/irB0rm4rUG6GyaLnf1vUsNFW8BBJXAuh8-FIJ_s75xjgFgbOuTdaEGQ30PYzjtawVv5UVIC5xs7Uq_Cm9BPSyC73A-xGwT5J2oYsKE8QiPE=@proton.me/1.1.1-a.txt">[-- Attachment #1.1.1: Type: text/plain, Size: 24646 bytes --]</a>

<span
class="q">&gt; This is relevant because the hypothetical evil curve-generator who is trying to poison the future H=SHA2(G) has an easier time in doing so, than a future canary-solver who obviously cannot try different values of G :)
</span>


Ah sorry, I thought you were talking about canary solvers, didn&#39;t realize you were talking about curve designers. Agreed then, but still seems unlikely that G was chosen this way:&#160;<a
href="https://bitcoin.stackexchange.com/questions/58784/how-were-the-secp256k1-base-point-coordinates-decided">https://bitcoin.stackexchange.com/questions/58784/how-were-the-secp256k1-base-point-coordinates-decided</a>


If we have any doubt about that, we could tweak the hash function with some data that is newer than G but still unbiased, e.g. the hash of the genesis block, or the hash of the first block in which the canary goes live (idea credit: Tadge Dryja).


<span
class="q">&gt; interesting point is that Shor can target any specific dlog problem, right. So I do think the ST is the correct version of the problem?
</span>


Yes, I believe so. I don&#39;t know of any way to batch Shor&#39;s algorithm in a multi-target attack that is any more efficient than a trivial one-by-one attack, so using MT-ECDLP seems like it only serves to makes classical attacks (or Grover&#39;s search) easier.


regards,
conduition


On Saturday, August 15th, 2026 at 10:14 AM, waxwing/ AdamISZ &lt;ekaggata@gmail&#8226;com&gt; wrote:

<span
class="q">&gt; &gt; A 192-bit curve i think should be reasonable as a canary, but consider this: If someone already has a QC that breaks 192-bit ECC, how long until they build one which breaks 256-bit ECC? A day, a week, a year? No way of knowing. If the delay is too long, users may see the canary as a false-positive, and migrate back to vulnerable addresses, and they might even be right. 192-bit canaries are vulnerable to classical attack with work approximately 2^96. We should bear in mind the possibility that such a canary could be activated possibly very early, well before Q-day, possibly even in the absence of any quantum computers.
&gt; 
</span>
<span
class="q">&gt; Agreed that is unlikely a big delta, in the nature of these things (QCs), between 192 and 256. Including that it&#39;s obvious that going very much below 192 means classical attack and therefore bad idea. Which is why I said 192 and not sub 160. What&#39;s not obvious is that 192 is worse than 256 here. It may only give us a small amount of extra time, but it won&#39;t give us negative extra time. So the tradeoff is, presumably, whether the additional complexity (which is a bit tricky from what I recall [1], but there will definitely be experts out there who can clean it up) is worth it.
&gt; The idea of &#39;people will think it a false positive&#39;, disagree, I think the whole tripwire idea is likely a *bit* vulnerable to genpop misunderstanding as I said in my previous post, but this particular thing I don&#39;t see it: a 192 bit being broken is *very* likely to cause an appropriate level of panic.
&gt; 
</span>
<span
class="q">&gt; &gt; Anyone can find G = a * B. Just generate a key and invert your secret key.
&gt; 
</span>
<span
class="q">&gt; &gt; P = a * G
&gt; &gt; G = a**-1 * P
&gt; 
</span>
<span
class="q">&gt; &gt; The hard part is then finding some b such that b*G = SHA256(G).
&gt; 
</span>
<span
class="q">&gt; You slightly missed my point here, I think? The idea is that if you set up two sides that are both sample-able, you can birthday. Like, you keep sampling a on one side and b on the other. Build tables of both sides. Then all you have to do is check whether SHA2 of the LHS ever matches the RHS. This gives you a square root style speedup a la birthday attack. Contrast with if you just fix G, then keep searching for matches: no square root speedup. This is relevant because the hypothetical evil curve-generator who is trying to poison the future H=SHA2(G) has an easier time in doing so, than a future canary-solver who obviously cannot try different values of G :)
&gt; 
</span>
<span
class="q">&gt; About your single-target vs multi-target distinction: interesting point is that Shor can target any specific dlog problem, right. So I do think the ST is the correct version of the problem? But actually I am quite unsure and unclear about those ST, MT, LMT distinctions you&#39;re making; specifically I mean, I am very unsure about how they differ in costs.
&gt; 
</span>
<span
class="q">&gt; As for characterizing the problem, I think it&#39;s fair to say: if you assumed SHA2 was a proper random oracle then we have with SHA2(enc(G)), something that&#39;s very tightly equivalent to ECDLP, which is what we want. If we want to pay attention to the fact that SHA2 is an actual hash function and not an RO, then I think there&#39;s some statement like &#34;assuming SHA2 has no structure &#34;matching&#34; secp256k1, then it&#39;s tightly equivalent to ECDLP on secp256k1&#34; which is obviously horrendously vague, but would not be very easy to write down properly.
&gt; 
</span>
<span
class="q">&gt; Another observation, probably it already exists up-thread: we obviously don&#39;t want to *literally* use BIP341&#39;s H on a 256 bit tripwire, because then a Shor-break directly steals a bunch of coins, so what should we use? Maybe SHA2(SHA2(enc(G)) ?
&gt; 
</span>
<span
class="q">&gt; 
</span>
<span
class="q">&gt; [1] <a
href="https://delvingbitcoin.org/t/qcap-a-bitcoin-native-quantum-canary-alert/2498/9">https://delvingbitcoin.org/t/qcap-a-bitcoin-native-quantum-canary-alert/2498/9</a>
&gt; On Friday, August 14, 2026 at 12:34:54&#8239;PM UTC-6 conduition wrote:
&gt; 
</span>
<span
class="q">&gt; &gt; &gt; An obvious question to raise: would we consider tripwiring a 192 bit group break of a similar type (NUMS)? I find that ... plausible?
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; A 192-bit curve i think should be reasonable as a canary, but consider this: If someone already has a QC that breaks 192-bit ECC, how long until they build one which breaks 256-bit ECC? A day, a week, a year? No way of knowing. If the delay is too long, users may see the canary as a false-positive, and migrate back to vulnerable addresses, and they might even be right. 192-bit canaries are vulnerable to classical attack with work approximately 2^96. We should bear in mind the possibility that such a canary could be activated possibly very early, well before Q-day, possibly even in the absence of any quantum computers.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Ideally we want a short gap between &#34;192-bit is broken&#34; and &#34;256-bit is broken&#34;, but not so short as to make the 192-bit canary effectively fungible with a 256-bit canary (because then it&#39;s less likely to be activated before theft occurs).
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; w.r.t. &#39;This guarantees that the NUMS point cannot predate G&#39; yes based on SHA2 preimage resistance, but: isn&#39;t the real point that we&#39;re relying on SHA-2 not being a naughty function so that you couldn&#39;t find G = a * B and SHA2(G) = b*B for some base B in some feasible computation (sans CQRC of course, as was likely back then!). I have no idea what precise name you give to that property. OK, this is a ridiculous thing to discuss, perhaps, given when SHA2 and secp256k1 were standardized :) And given the encoding choices for our BIP341 NUMS (iirc the same as for Elements back in the day? using uncompressed encoding?) were able to be counted on the fingers of the hand which the sleeve does not cover :)
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Anyone can find `G = a * B`. Just generate a key and invert your secret key.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; `P = a * G`
&gt; &gt; G = a**-1 * P
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; The hard part is then finding some b such that `b*G = SHA256(G).`
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; ---------
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; If we reflect on the requirement that `G` is fixed, we see `SHA256(G)` is also fixed as a pseudorandom challenge point. The reason for using SHA256 instead of, say, picking an arbitary point by committee or using digits of pi or some other trickery, is that hash outputs are supposed to be random and so `SHA256(G)` is (assumably) a random ECDLP challenge. This matches the classical definition of ECDLP more tightly: Given an arbitrary point `P`, find `p` such that `P = p * G`. The assumption is that if an attacker can factor an honestly-sampled challenge point, they can factor any point. SHA256 is just a stand-in for the &#34;honestly-sampled&#34; part.
&gt; &gt; However, the following two tasks are actually very different:
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 1.  Given G, find scalar `a` such that `a*G = lift_x(SHA256(G))`.
&gt; &gt; 2.  Given G, find scalar `a` and message `m` such that `a*G = lift_x(SHA256(m))`.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; In the case of task 1, if we assume SHA256 output is random, then this is more tightly equivalent to ECDLP, because the point we&#39;re trying to factor is a fixed target, as is the one sampled honestly by the ECDLP security game.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; In the case of task 2, the attacker can sample arbitrary messages to create multiple target points, and the attacker wins if they succeed in factoring any of them. The attacker can attack all those target points concurrently if they want, and they get a speedup from doing so.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; So I believe it is worth disambiguating canaries between the two cases, because they are different security notions. The first (1) I would call single-target ECDLP (ST-ECDLP), and the second (2) I would call multi-target ECDLP (MT-ECDLP).
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; It&#39;s pretty clear that MT-ECDLP is easier to break, because attackers can make progress against more than one target concurrently, and breaking any one is sufficient to win the security game.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; For example, say I sample 2 different messages `m1` and `m2`, and compute ECDLP target points `T1 = lift_x(SHA256(m1))` and `T2 = lift_x(SHA256(m2))`. Then if I sample a random scalar `r` and compute `R = r*G`, I have two potential chances of success: `R == T1` OR `R == T2`. I can scale up this advantage by generating more targets, `T3`, `T4`, ... and so on.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; MT-ECDLP also admits a more efficient basic unit of computation in brute force attacks (including Grover) by using hashes instead of EC point multiplications. If I instead start by picking scalar `t` and fix the target point `T = t*G`, then I can run a brute-force preimage search on SHA256 until I find `m` such that `SHA256(m) == x(T)`. This can also be scaled up using a multi-target attack [1].
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; With ST-ECDLP, we have only a single fixed message `m = G`, and so the attacker can&#39;t use those multi-target cheat codes. They can parallelize, use pollard-rho or Shor or other algorithms, but they have only a single target point that they must break to win the game.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; The method Pieter suggested using for the canary construction is equivalent to single-target ECDLP.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; I&#39;ve heard others (e.g. Tadge in this thread) previously suggest using a script like `OP_SHA256 OP_CHECKSIG` as a canary, where any spend of such a script would trigger the canary. This would be multi-target ECDLP.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; I&#39;m not sure which is better.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; -   ST-ECDLP is less likely to be triggered early or mistakenly, and is more tightly equivalent to ECDLP.
&gt; &gt;     
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; -   MT-ECDLP is more reflective of how real-world attackers behave on Bitcoin (e.g. with thousands-to-millions of public keys available to attack in parallel, and breaking even one is considered unacceptable).
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; I&#39;m slightly leanings towards a construction like Pieter&#39;s, featuring ST-ECDLP, just because I&#39;m not sure what other tricks could be used to potentially trigger MT-ECDLP classically or quantumly.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; We could also engineer a compromise between the two, where we limit the number of targets. For example, define the game like this:
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Given `G`, find scalar `a` and 32-bit integer `i` such that `a*G = lift_x(SHA256(G || i))`.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Then the adversary can only attack against at most 2^32 unique target points, and those targets are fixed forever, for any adversary. This is an easier problem than ST-ECDLP, but harder than MT-ECDLP. Maybe call it limited multi-target ECDLP (LMT-ECDLP)?
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; regards,
&gt; &gt; conduition
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; [1]: First, generate a bunch of target points. Sample scalar `t` and compute `T0 = t * G`, T1 = T0 + T0, and T2 = T1 + T1, and T3 = T2 + T2, etc. Why double each point? point doubling is cheaper than addition or multiplication, and still covers the whole curve. Then we run a multi-target SHA256 preimage search over all targets [x(T0), x(T1), x(T2), x(T3), ...]. If we have n targets and curve order N, then each message hash has an `n/N` chance of success. If we find a valid message `m`, such that `SHA256(m) == x(R_i)` for some target index `i`, then we have found `T_i = t * 2**i * G = lift_x(SHA256(m))`.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; On Thursday, August 13th, 2026 at 2:02 AM, waxwing/ AdamISZ &lt;ekag...@gmail&#8226;com&gt; wrote:
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; This tripwire idea is interesting. Basically &#34;canary in consensus&#34;.
&gt; &gt; &gt; I agree it&#39;s valuable. In the scenario of adversarial actor(s) gaining access to CQRC first, i.e. no whitehats, only blackhats, obviously nothing to discuss; touching a NUMS ECDL is the last thing they&#39;ll do. So I&#39;m slightly worried that the general userbase will not notice that point, instead thinking it&#39;s a solid defense when it ... depends.
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; In the scenario of at least some whitehats, we get wires tripped, or canaries singing. Having it in consensus is nice. The blockchain then does its job of being an unambiguous signal and we can have all the arguments well ahead of time. [1]
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; On the other hand, we traditionally design such systems adversarially, right, so you could argue that an overfocus on this might be suboptimal - it might be better to do other things.
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; (Similar comment applies to the &#39;smaller group canary&#39; - definitely nothing wrong with it, but it is not in itself a defence unless we strongly believe whitehats, and *active* whitehats at that, are keeping up). An obvious question to raise: would we consider tripwiring a 192 bit group break of a similar type (NUMS)? I find that ... plausible?
&gt; &gt; &gt; &gt; The BIP341 NUMS point (which I suggest using in this context) is the point whose X coordinate is the SHA256 hash of the generator point G. This guarantees that the NUMS point cannot predate G (if it did, it would be possible in theory that secp256k1&#39;s designers actually chose G in function of what we call that NUMS point, giving it a DLP known to them).
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; w.r.t. &#39;This guarantees that the NUMS point cannot predate G&#39; yes based on SHA2 preimage resistance, but: isn&#39;t the real point that we&#39;re relying on SHA-2 not being a naughty function so that you couldn&#39;t find G = a * B and SHA2(G) = b*B for some base B in some feasible computation (sans CQRC of course, as was likely back then!). I have no idea what precise name you give to that property. OK, this is a ridiculous thing to discuss, perhaps, given when SHA2 and secp256k1 were standardized :) And given the encoding choices for our BIP341 NUMS (iirc the same as for Elements back in the day? using uncompressed encoding?) were able to be counted on the fingers of the hand which the sleeve does not cover :)
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; [1] I take Antoine&#39;s point that making it consensus means the miners are involved and there is a non-trivial collusion risk if the stakes are high, but I can&#39;t see how this scenario is *worse* than no tripwire?
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; On Sunday, July 5, 2026 at 4:07:33&#8239;PM UTC-6 Antoine Riard wrote:
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Hi Pieter,
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Thanks for the observations.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; When I was saying there is a problem with the game theory,
&gt; &gt; &gt; &gt; it&#39;s that strikingly, any activation of the tripwire logic
&gt; &gt; &gt; &gt; would rely on a &#34;flag&#34; transaction being mined in the chain
&gt; &gt; &gt; &gt; for the network nodes starting to enforce at the block N or
&gt; &gt; &gt; &gt; N+1 or whatever the EC disabling threshold.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Any &#34;flag&#34; transaction can be itself re-orged out of the chain
&gt; &gt; &gt; &gt; to purely disable the effects of the EC disabling threshold,
&gt; &gt; &gt; &gt; therefore make it null and void as an effect. One might see
&gt; &gt; &gt; &gt; it as a competing race between a group of &#34;sunsetting&#34; users
&gt; &gt; &gt; &gt; and a (majority) coalition of miners in coordination with a
&gt; &gt; &gt; &gt; CRQC adversary, where the latter have an interest and the
&gt; &gt; &gt; &gt; hashrate capabilities to do a tx-withold [0].
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; In pure terms of satoshi fee denominated calculus, empirically
&gt; &gt; &gt; &gt; global miners have won an average of $20 B yearly. If we only
&gt; &gt; &gt; &gt; consider that P2PK are going to be frozen by the tripwire effect,
&gt; &gt; &gt; &gt; as for most of them it might be assumed they will never move to
&gt; &gt; &gt; &gt; a safer format, we talk already about 1.7 M of coins or as of
&gt; &gt; &gt; &gt; today valuation $107 B (the information is on the chain and can
&gt; &gt; &gt; &gt; be verified).
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; That&#39;s $107B can &#34;burn&#34; in revenue or income that a CRQC-enabled
&gt; &gt; &gt; &gt; miners coalition to constantly reorg-out the &#34;flag&#34; tx out of the
&gt; &gt; &gt; &gt; chain. In other terms, something like 5 years of income, and I
&gt; &gt; &gt; &gt; kindly do not count all the loss coins that are likely to amount
&gt; &gt; &gt; &gt; to a far bigger &#34;tripwire&#34; neutralization budget.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; In the name of what a majority of miners will gracefully let on
&gt; &gt; &gt; &gt; the table an opportunity of massive income ?
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Leveraging Shor the exploitation might be even done anonymously
&gt; &gt; &gt; &gt; as the mining process is done. Not even certainty, by who the
&gt; &gt; &gt; &gt; EC-protected coins could be covertly exfiltrated.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; That&#39;s the most striking problem when you think about the math
&gt; &gt; &gt; &gt; with any &#34;tripwire&#34; approach, or even an &#34;hourglass&#34; one relying
&gt; &gt; &gt; &gt; on a &#34;flag&#34; transaction [1]. I&#39;m ruling out &#34;checkpoints&#34; and
&gt; &gt; &gt; &gt; any other trust-the-dev approach, as that&#39;s even worst [2].
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; As you&#39;re introducing post is resounding, what the miners
&gt; &gt; &gt; &gt; are saying now, there are no guarantees on how they would use
&gt; &gt; &gt; &gt; their hashrate down the road, potentially 10 or 20 years from now.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Beyond, and to answer back your point, I still think you can
&gt; &gt; &gt; &gt; manage an escape hatch of the &#34;tripwire&#34; effect, it&#39;s all depends
&gt; &gt; &gt; &gt; how the script tripwire logic is implemented, but if you have
&gt; &gt; &gt; &gt; two OP_SUCCESS of different kinds before your EC CHECKSIG, you
&gt; &gt; &gt; &gt; can always have a &#34;soft-fork&#34; after the &#34;tripwire&#34; to return
&gt; &gt; &gt; &gt; true on the stack, with an EC or hashlock as a success (I agree
&gt; &gt; &gt; &gt; using undefined op_success in a script is not safe at all) [3].
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Best,
&gt; &gt; &gt; &gt; Antoine
&gt; &gt; &gt; &gt; OTS hash: 4bc91d8dee1625f6e78b27c88bced8e405f25ef6d3d8fd59be8016db5b0fbe66
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; [0] See naumenkog&#39;s <a
href="https://www.bitmex.com/blog/txwithhold-smart-contracts">https://www.bitmex.com/blog/txwithhold-smart-contracts</a>
&gt; &gt; &gt; &gt; [1] This is sad, as the &#34;hourglass&#34; depending how the parameters are chosen
&gt; &gt; &gt; &gt; was a more acceptable trade-off than pure sunsetting.
&gt; &gt; &gt; &gt; [2] Given the amounts at stake to sunset, as a group of developers you
&gt; &gt; &gt; &gt; would just paint yourself a target, there are more even funds at stake
&gt; &gt; &gt; &gt; that Satoshi herself / himself is assumed to have.
&gt; &gt; &gt; &gt; [3] There is no security proof in BIP341 on the unforgeability of the
&gt; &gt; &gt; &gt; NUMS point, if it binds in the ROM or whatever.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Le sam. 4 juil. 2026 &#224; 13:47, Sjors Provoost &lt;sj...@sprovoost&#8226;nl&gt; a &#233;crit :
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; On Fri, Jul 3, 2026, at 23:23, Pieter Wuille wrote:
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; [...]
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; &gt; * Just publishing the DLP in a transaction (e.g. OP_RETURN with a
&gt; &gt; &gt; &gt; &gt; &gt; specific marker). This is smaller than a full transaction input +
&gt; &gt; &gt; &gt; &gt; &gt; signature.
&gt; &gt; &gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt; &gt; &gt; * Similarly, but publishing in the coinbase, and requiring relay using
&gt; &gt; &gt; &gt; &gt; &gt; a separate message. Less places a node needs to check, but I&#39;m
&gt; &gt; &gt; &gt; &gt; &gt; concerned about the difficulty of testing infrastructure that relay of
&gt; &gt; &gt; &gt; &gt; &gt; such a message works
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; [...]
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt; &gt; &gt; On Saturday, June 27th, 2026 at 12:33 AM, Anthony Towns
&gt; &gt; &gt; &gt; &gt; &gt; &lt;a...@erisian&#8226;com.au&gt; wrote:
&gt; &gt; &gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt; &gt; &gt;&gt; A slight variant of this approach would be to have a 128 byte value &#34;aRsm&#34;, such that P = N+a*G, N is the BIP-341 NUMS point, and Rs is a BIP340 signature of m by P. That would allow the victim of post-quantum theft via a key-path spend of a BIP341 NUMS IPK to trigger the tripwire, in addition to someone who has direct access to a CRQC.
&gt; &gt; &gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt; &gt; &gt; Indeed, I had considered something similar, but see above for why I&#39;m
&gt; &gt; &gt; &gt; &gt; &gt; not convinced supporting non-cooperative CRQCs is that useful.
&gt; &gt; &gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt; &gt; &gt; Also, in my view the tripwire isn&#39;t really a security feature on itself
&gt; &gt; &gt; &gt; &gt; &gt; (it&#39;s not expected to trigger...), but more something that sets
&gt; &gt; &gt; &gt; &gt; &gt; expectations around the output type for prospective users.
&gt; &gt; &gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt; &gt; &gt; In that sense, the question is really whether supporting
&gt; &gt; &gt; &gt; &gt; &gt; non-cooperative CRQCs helps set that expectation more than only
&gt; &gt; &gt; &gt; &gt; &gt; cooperative ones, which are definitely easier to support.
&gt; &gt; &gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt; &gt; &gt;&gt; I think it could make sense to have the tripwire be included in the block via the coinbase witness commitment output, rather than having it be locked to a transaction, so you only having to check the coinbase for the magic rather than every transaction. That would require a separate P2P message to relay the necessary ECDL-break proof to miners, and would probably need stratumv2 or a getblocktemplate update in order for the node to be able to tell pools to actually include that info in the coinbase.
&gt; &gt; &gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt; &gt; &gt; I worry this is untestable, really. You&#39;d need things like
&gt; &gt; &gt; &gt; &gt; &gt; fake-tripwires to be supported through the same message which don&#39;t
&gt; &gt; &gt; &gt; &gt; &gt; require an ECDLP break, and still propagate. And then that needs DoS
&gt; &gt; &gt; &gt; &gt; &gt; protection measures,
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; I whipped something up last weekend:
&gt; &gt; &gt; &gt; &gt; <a
href="https://github.com/Sjors/bitcoin/pull/121">https://github.com/Sjors/bitcoin/pull/121</a>
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; It seems straightforward, but maybe I missed something:
&gt; &gt; &gt; &gt; &gt; - for test code we use a fake NUMS point, so we can generate &#34;proof&#34; without a quantum computer
&gt; &gt; &gt; &gt; &gt; - a p2p message floods the proof
&gt; &gt; &gt; &gt; &gt; - nodes ignore the message if they already have *any* valid proof
&gt; &gt; &gt; &gt; &gt; - verifying p2p proof candidates might need some rate limiting, but it&#39;s as cheap as verifying a transaction signature
&gt; &gt; &gt; &gt; &gt; - mining code includes the proof in a coinbase op_return, until the freeze activates
&gt; &gt; &gt; &gt; &gt; - with stratum v2 (and ipc mining clients in general this works out of the box, a small change is needed for getblocktemplate clients)
&gt; &gt; &gt; &gt; &gt; - since the proof is not in the header, we can&#39;t use the normal bip9 style header scan to see if the rule activated. Instead the prototype stores it in a file along with a merkle inclusion proof, which is read when the node restarts.
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; With this mechanism it doesn&#39;t really need to be in the coinbase transaction, but that does seem more convenient and miners can censor it anyway.
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; - Sjors
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; --
&gt; &gt; &gt; &gt; &gt; You received this message because you are subscribed to a topic in the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt; &gt; &gt; &gt; &gt; To unsubscribe from this topic, visit <a
href="https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe">https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe</a>.
&gt; &gt; &gt; &gt; &gt; To unsubscribe from this group and all its topics, send an email to bitcoindev+...@googlegroups&#8226;com.
&gt; &gt; &gt; &gt; &gt; To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/002f2395-7d5d-4cb6-852c-e991aa1f0eb3%40app.fastmail.com">https://groups.google.com/d/msgid/bitcoindev/002f2395-7d5d-4cb6-852c-e991aa1f0eb3%40app.fastmail.com</a>.
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; --
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt; &gt; &gt; To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+...@googlegroups&#8226;com.
&gt; &gt; &gt; To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can%40googlegroups.com</a>.
&gt; 
</span>
<span
class="q">&gt; --
&gt; You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt; To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
&gt; To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/fd947d7c-86fd-407c-98aa-0a63b8be28fan%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/fd947d7c-86fd-407c-98aa-0a63b8be28fan%40googlegroups.com</a>.
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/irB0rm4rUG6GyaLnf1vUsNFW8BBJXAuh8-FIJ_s75xjgFgbOuTdaEGQ30PYzjtawVv5UVIC5xs7Uq_Cm9BPSyC73A-xGwT5J2oYsKE8QiPE%3D%40proton.me">https://groups.google.com/d/msgid/bitcoindev/irB0rm4rUG6GyaLnf1vUsNFW8BBJXAuh8-FIJ_s75xjgFgbOuTdaEGQ30PYzjtawVv5UVIC5xs7Uq_Cm9BPSyC73A-xGwT5J2oYsKE8QiPE%3D%40proton.me</a>.

<a
href="https://gnusha.org/pi/bitcoindev/irB0rm4rUG6GyaLnf1vUsNFW8BBJXAuh8-FIJ_s75xjgFgbOuTdaEGQ30PYzjtawVv5UVIC5xs7Uq_Cm9BPSyC73A-xGwT5J2oYsKE8QiPE=@proton.me/1.1.2.1-a.bin">[-- Attachment #1.1.2.1: Type: text/html, Size: 36014 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/irB0rm4rUG6GyaLnf1vUsNFW8BBJXAuh8-FIJ_s75xjgFgbOuTdaEGQ30PYzjtawVv5UVIC5xs7Uq_Cm9BPSyC73A-xGwT5J2oYsKE8QiPE=@proton.me/1.2-a.bin">[-- Attachment #1.2: publickey - conduition@proton.me - 0x474891AD.asc --]
[-- Type: application/pgp-keys, Size: 649 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/irB0rm4rUG6GyaLnf1vUsNFW8BBJXAuh8-FIJ_s75xjgFgbOuTdaEGQ30PYzjtawVv5UVIC5xs7Uq_Cm9BPSyC73A-xGwT5J2oYsKE8QiPE=@proton.me/2-signature.asc">[-- Attachment #2: OpenPGP digital signature --]
[-- Type: application/pgp-signature, Size: 343 bytes --]</a>
</pre></div></content></entry><entry><author><name>waxwing/ AdamISZ</name><email>ekaggata@gmail.com</email></author><title>Re: [bitcoindev] Giving teeth to expected EC disabling: P2XX(-T)(-ML)</title><updated>2026-08-15T15:14:28Z</updated><link
href="https://gnusha.org/pi/bitcoindev/fd947d7c-86fd-407c-98aa-0a63b8be28fan@googlegroups.com/"/><id>urn:uuid:ed8f2fb9-a063-047b-0d66-0ca087643e48</id><thr:in-reply-to
ref="urn:uuid:8fb65f63-7fc6-1731-cfbf-dfb2888fe4a2"
href="https://gnusha.org/pi/bitcoindev/wftCzgJs2k7H-4R22EOqdOhhXYdFPFhSZhsYHvlzejpJ5emoze0ACgL3rrYiTP-X5QQMpThdRW1cO7mr9IQvs2C4MHxSD2eu_gPFGv-yZs8=@proton.me/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/fd947d7c-86fd-407c-98aa-0a63b8be28fan@googlegroups.com/1.1-a.txt">[-- Attachment #1.1: Type: text/plain, Size: 22481 bytes --]</a>

<span
class="q">&gt; A 192-bit curve i think should be reasonable as a canary, but consider 
</span>this: If someone already has a QC that breaks 192-bit ECC, how long until 
they build one which breaks 256-bit ECC? A day, a week, a year? No way of 
knowing. If the delay is too long, users may see the canary as a 
false-positive, and migrate back to vulnerable addresses, and they might 
even be right. 192-bit canaries are vulnerable to classical attack with 
work approximately 2^96. We should bear in mind the possibility that such a 
canary could be activated possibly very early, well before Q-day, possibly 
even in the absence of any quantum computers.

Agreed that is unlikely a big delta, in the nature of these things (QCs), 
between 192 and 256. Including that it&#39;s obvious that going very much below 
192 means classical attack and therefore bad idea. Which is why I said 192 
and not sub 160. What&#39;s not obvious is that 192 is worse than 256 here. It 
may only give us a small amount of extra time, but it won&#39;t give us 
negative extra time. So the tradeoff is, presumably, whether the additional 
complexity (which is a bit tricky from what I recall [1], but there will 
definitely be experts out there who can clean it up) is worth it.

The idea of &#39;people will think it a false positive&#39;, disagree, I think the 
whole tripwire idea is likely a *bit* vulnerable to genpop misunderstanding 
as I said in my previous post, but this particular thing I don&#39;t see it: a 
192 bit being broken is *very* likely to cause an appropriate level of 
panic.

<span
class="q">&gt; Anyone can find G = a * B&#8203;. Just generate a key and invert your secret 
</span>key.

<span
class="q">&gt; P = a * G&#8203;
&gt; G = a**-1 * P
</span>
<span
class="q">&gt; The hard part is then finding some b such that b*G = SHA256(G).
</span>
You slightly missed my point here, I think? The idea is that if you set up 
two sides that are both sample-able, you can birthday. Like, you keep 
sampling a on one side and b on the other. Build tables of both sides. Then 
all you have to do is check whether SHA2 of the LHS ever matches the RHS. 
This gives you a square root style speedup a la birthday attack. Contrast 
with if you just fix G, then keep searching for matches: no square root 
speedup. This is relevant because the hypothetical evil curve-generator who 
is trying to poison the future H=SHA2(G) has an easier time in doing so, 
than a future canary-solver who obviously cannot try different values of G 
:)

About your single-target vs multi-target distinction: interesting point is 
that Shor can target any specific dlog problem, right. So I do think the ST 
is the correct version of the problem? But actually I am quite unsure and 
unclear about those ST, MT, LMT distinctions you&#39;re making; specifically I 
mean, I am very unsure about how they differ in costs.

As for characterizing the problem, I think it&#39;s fair to say: if you assumed 
SHA2 was a proper random oracle then we have with SHA2(enc(G)), something 
that&#39;s very tightly equivalent to ECDLP, which is what we want. If we want 
to pay attention to the fact that SHA2 is an actual hash function and not 
an RO, then I think there&#39;s some statement like &#34;assuming SHA2 has no 
structure &#34;matching&#34; secp256k1, then it&#39;s tightly equivalent to ECDLP on 
secp256k1&#34; which is obviously horrendously vague, but would not be very 
easy to write down properly.

Another observation, probably it already exists up-thread: we obviously 
don&#39;t want to *literally* use BIP341&#39;s H on a 256 bit tripwire, because 
then a Shor-break directly steals a bunch of coins, so what should we use? 
Maybe SHA2(SHA2(enc(G)) ?


[1] <a
href="https://delvingbitcoin.org/t/qcap-a-bitcoin-native-quantum-canary-alert/2498/9">https://delvingbitcoin.org/t/qcap-a-bitcoin-native-quantum-canary-alert/2498/9</a>
On Friday, August 14, 2026 at 12:34:54&#8239;PM UTC-6 conduition wrote:

<span
class="q">&gt; An obvious question to raise: would we consider tripwiring a 192 bit group 
&gt; break of a similar type (NUMS)? I find that ... plausible?
&gt;
&gt;
&gt; A 192-bit curve i think should be reasonable as a canary, but consider 
&gt; this: If someone already has a QC that breaks 192-bit ECC, how long until 
&gt; they build one which breaks 256-bit ECC? A day, a week, a year? No way of 
&gt; knowing. If the delay is too long, users may see the canary as a 
&gt; false-positive, and migrate back to vulnerable addresses, and they might 
&gt; even be right. 192-bit canaries are vulnerable to classical attack with 
&gt; work approximately 2^96. We should bear in mind the possibility that such a 
&gt; canary could be activated possibly very early, well before Q-day, possibly 
&gt; even in the absence of any quantum computers.
&gt;
&gt; Ideally we want a short gap between &#34;192-bit is broken&#34; and &#34;256-bit is 
&gt; broken&#34;, but not so short as to make the 192-bit canary effectively 
&gt; fungible with a 256-bit canary (because then it&#39;s less likely to be 
&gt; activated before theft occurs).
&gt;
&gt; w.r.t. &#39;This guarantees that the NUMS point cannot predate G&#39; yes based on 
&gt; SHA2 preimage resistance, but: isn&#39;t the real point that we&#39;re relying on 
&gt; SHA-2 not being a naughty function so that you couldn&#39;t find G = a * B and 
&gt; SHA2(G) = b*B for some base B in some feasible computation (sans CQRC of 
&gt; course, as was likely back then!). I have no idea what precise name you 
&gt; give to that property. OK, this is a ridiculous thing to discuss, perhaps, 
&gt; given when SHA2 and secp256k1 were standardized :) And given the encoding 
&gt; choices for our BIP341 NUMS (iirc the same as for Elements back in the day? 
&gt; using uncompressed encoding?) were able to be counted on the fingers of the 
&gt; hand which the sleeve does not cover :)
&gt;
&gt;
&gt; Anyone can find G = a * B&#8203;. Just generate a key and invert your secret 
&gt; key.
&gt;
&gt; P = a * G&#8203;
&gt; G = a**-1 * P
&gt;
&gt; The hard part is then finding some b such that b*G = SHA256(G).
&gt;
&gt; ---------
&gt;
&gt; If we reflect on the requirement that G&#8203; is fixed, we see SHA256(G)&#8203; is 
&gt; also fixed as a pseudorandom challenge point. The reason for using SHA256 
&gt; instead of, say, picking an arbitary point by committee or using digits of 
&gt; pi or some other trickery, is that hash outputs are supposed to be random 
&gt; and so SHA256(G)&#8203; is (assumably) a random ECDLP challenge. This matches 
&gt; the classical definition of ECDLP more tightly: Given an arbitrary point P&#8203;, 
&gt; find p&#8203; such that P = p * G&#8203;. The assumption is that if an attacker can 
&gt; factor an honestly-sampled challenge point, they can factor any point. 
&gt; SHA256 is just a stand-in for the &#34;honestly-sampled&#34; part.
&gt;
&gt; However, the following two tasks are actually very different:
&gt;
&gt;
&gt;    1. Given G, find scalar a&#8203; such that a*G = lift_x(SHA256(G))&#8203;.
&gt;    2. Given G, find scalar a&#8203; and message m&#8203; such that a*G = 
&gt;    lift_x(SHA256(m))&#8203;.
&gt;
&gt;
&gt; In the case of task 1, if we assume SHA256 output is random, then this is 
&gt; more tightly equivalent to ECDLP, because the point we&#39;re trying to factor 
&gt; is a fixed target, as is the one sampled honestly by the ECDLP security 
&gt; game.
&gt;
&gt; In the case of task 2, the attacker can sample arbitrary messages to 
&gt; create multiple *target points*, and the attacker wins if they succeed in 
&gt; factoring any of them. The attacker can attack all those target points 
&gt; concurrently if they want, and they get a speedup from doing so.
&gt;
&gt; So I believe it is worth disambiguating canaries between the two cases, 
&gt; because they are different security notions. The first (1) I would call *single-target 
&gt; ECDLP *(ST-ECDLP), and the second (2) I would call *multi-target ECDLP *
&gt; (MT-ECDLP).
&gt;
&gt; It&#39;s pretty clear that MT-ECDLP is easier to break, because attackers can 
&gt; make progress against more than one target concurrently, and breaking any 
&gt; one is sufficient to win the security game.
&gt;
&gt; For example, say I sample 2 different messages m1&#8203; and m2&#8203;, and compute 
&gt; ECDLP target points T1 = lift_x(SHA256(m1))&#8203; and T2 = lift_x(SHA256(m2))&#8203;. 
&gt; Then if I sample a random scalar r&#8203; and compute R = r*G&#8203;, I have two 
&gt; potential chances of success: R == T1&#8203; OR R == T2&#8203;. I can scale up this 
&gt; advantage by generating more targets, T3&#8203;, T4&#8203;, ... and so on.
&gt;
&gt; MT-ECDLP also admits a more efficient basic unit of computation in brute 
&gt; force attacks (including Grover) by using hashes instead of EC point 
&gt; multiplications. If I instead start by picking scalar t&#8203; and fix the 
&gt; target point T = t*G&#8203;, then I can run a brute-force preimage search on 
&gt; SHA256 until I find m&#8203; such that SHA256(m) == x(T)&#8203;. This can also be 
&gt; scaled up using a multi-target attack [1].
&gt;
&gt; With ST-ECDLP, we have only a single fixed message m = G&#8203;, and so the 
&gt; attacker can&#39;t use those multi-target cheat codes. They can parallelize, 
&gt; use pollard-rho or Shor or other algorithms, but they have only a single 
&gt; target point that they must break to win the game.
&gt;
&gt; The method Pieter suggested using for the canary construction is 
&gt; equivalent to *single-target* ECDLP.
&gt;
&gt; I&#39;ve heard others (e.g. Tadge in this thread 
&gt; &lt;<a
href="https://groups.google.com/g/bitcoindev/c/LpWOcXMcvk8/m/DjaiWnViAQAJ">https://groups.google.com/g/bitcoindev/c/LpWOcXMcvk8/m/DjaiWnViAQAJ</a>&gt;) 
&gt; previously suggest using a script like OP_SHA256 OP_CHECKSIG&#8203; as a 
&gt; canary, where any spend of such a script would trigger the canary. This 
&gt; would be *multi-target* ECDLP.
&gt;
&gt; I&#39;m not sure which is better. 
&gt;
&gt;
&gt;    - ST-ECDLP is less likely to be triggered early or mistakenly, and is 
&gt;    more tightly equivalent to ECDLP. 
&gt;    
&gt;
&gt;    - MT-ECDLP is more reflective of how real-world attackers behave on 
&gt;    Bitcoin (e.g. with thousands-to-millions of public keys available to attack 
&gt;    in parallel, and breaking even one is considered unacceptable).
&gt;
&gt;
&gt; I&#39;m slightly leanings towards a construction like Pieter&#39;s, featuring 
&gt; ST-ECDLP, just because I&#39;m not sure what other tricks could be used to 
&gt; potentially trigger MT-ECDLP classically or quantumly.
&gt;
&gt; We could also engineer a compromise between the two, where we limit the 
&gt; number of targets. For example, define the game like this:
&gt;
&gt; Given G&#8203;, find scalar a&#8203;&#8203; and 32-bit integer i&#8203;&#8203; such that a*G = 
&gt; lift_x(SHA256(G || i))&#8203;&#8203;.
&gt;
&gt; Then the adversary can only attack against at most 2^32 unique target 
&gt; points, and those targets are fixed forever, for any adversary. This is an 
&gt; easier problem than ST-ECDLP, but harder than MT-ECDLP. Maybe call it *limited 
&gt; multi-target ECDLP (LMT-ECDLP)*?
&gt;
&gt;
&gt; regards,
&gt; conduition
&gt;
&gt;
&gt; [1]: First, generate a bunch of target points. Sample scalar t&#8203; and compute 
&gt; T0 = t * G&#8203;, T1 = T0 + T0, and T2 = T1 + T1, and T3 = T2 + T2&#8203;, etc. Why 
&gt; double each point? point doubling is cheaper than addition or 
&gt; multiplication, and still covers the whole curve. Then we run a 
&gt; multi-target SHA256 preimage search over all targets [x(T0), x(T1), x(T2), 
&gt; x(T3), ...]&#8203;. If we have n&#8203; targets and curve order N&#8203;, then each message 
&gt; hash has an n/N&#8203;&#8203; chance of success. If we find a valid message m&#8203;, such 
&gt; that SHA256(m) == x(R_i)&#8203; for some target index i&#8203;, then we have found T_i 
&gt; = t * 2**i * G = lift_x(SHA256(m))&#8203;.
&gt;
&gt;
&gt;
&gt;
&gt;
&gt; On Thursday, August 13th, 2026 at 2:02 AM, waxwing/ AdamISZ &lt;
&gt; ekag...@gmail&#8226;com&gt; wrote:
&gt;
&gt; This tripwire idea is interesting. Basically &#34;canary in consensus&#34;.
&gt;
&gt; I agree it&#39;s valuable. In the scenario of adversarial actor(s) gaining 
&gt; access to CQRC first, i.e. no whitehats, only blackhats, obviously nothing 
&gt; to discuss; touching a NUMS ECDL is the last thing they&#39;ll do. So I&#39;m 
&gt; slightly worried that the general userbase will not notice that point, 
&gt; instead thinking it&#39;s a solid defense when it ... depends.
&gt;
&gt; In the scenario of at least some whitehats, we get wires tripped, or 
&gt; canaries singing. Having it in consensus is nice. The blockchain then does 
&gt; its job of being an unambiguous signal and we can have all the arguments 
&gt; well ahead of time. [1]
&gt;
&gt; On the other hand, we traditionally design such systems adversarially, 
&gt; right, so you could argue that an overfocus on this might be suboptimal - 
&gt; it might be better to do other things.
&gt;
&gt; (Similar comment applies to the &#39;smaller group canary&#39; - definitely 
&gt; nothing wrong with it, but it is not in itself a defence unless we strongly 
&gt; believe whitehats, and *active* whitehats at that, are keeping up). An 
&gt; obvious question to raise: would we consider tripwiring a 192 bit group 
&gt; break of a similar type (NUMS)? I find that ... plausible?
&gt;
&gt; &gt; The BIP341 NUMS point (which I suggest using in this context) is the 
&gt; point whose X coordinate is the SHA256 hash of the generator point G. This 
&gt; guarantees that the NUMS point cannot predate G (if it did, it would be 
&gt; possible in theory that secp256k1&#39;s designers actually chose G in function 
&gt; of what we call that NUMS point, giving it a DLP known to them).
&gt;
&gt; w.r.t. &#39;This guarantees that the NUMS point cannot predate G&#39; yes based on 
&gt; SHA2 preimage resistance, but: isn&#39;t the real point that we&#39;re relying on 
&gt; SHA-2 not being a naughty function so that you couldn&#39;t find G = a * B and 
&gt; SHA2(G) = b*B for some base B in some feasible computation (sans CQRC of 
&gt; course, as was likely back then!). I have no idea what precise name you 
&gt; give to that property. OK, this is a ridiculous thing to discuss, perhaps, 
&gt; given when SHA2 and secp256k1 were standardized :) And given the encoding 
&gt; choices for our BIP341 NUMS (iirc the same as for Elements back in the day? 
&gt; using uncompressed encoding?) were able to be counted on the fingers of the 
&gt; hand which the sleeve does not cover :)
&gt;
&gt; [1] I take Antoine&#39;s point that making it consensus means the miners are 
&gt; involved and there is a non-trivial collusion risk if the stakes are high, 
&gt; but I can&#39;t see how this scenario is *worse* than no tripwire?
&gt;
&gt; On Sunday, July 5, 2026 at 4:07:33&#8239;PM UTC-6 Antoine Riard wrote:
&gt;
&gt;&gt; Hi Pieter,
&gt;&gt;
&gt;&gt; Thanks for the observations.
&gt;&gt;
&gt;&gt; When I was saying there is a problem with the game theory,
&gt;&gt; it&#39;s that strikingly, any activation of the tripwire logic
&gt;&gt; would rely on a &#34;flag&#34; transaction being mined in the chain
&gt;&gt; for the network nodes starting to enforce at the block N or
&gt;&gt; N+1 or whatever the EC disabling threshold.
&gt;&gt;
&gt;&gt; Any &#34;flag&#34; transaction can be itself re-orged out of the chain
&gt;&gt; to purely disable the effects of the EC disabling threshold,
&gt;&gt; therefore make it null and void as an effect. One might see
&gt;&gt; it as a competing race between a group of &#34;sunsetting&#34; users
&gt;&gt; and a (majority) coalition of miners in coordination with a
&gt;&gt; CRQC adversary, where the latter have an interest and the
&gt;&gt; hashrate capabilities to do a tx-withold [0].
&gt;&gt;
&gt;&gt; In pure terms of satoshi fee denominated calculus, empirically
&gt;&gt; global miners have won an average of $20 B yearly. If we only
&gt;&gt; consider that P2PK are going to be frozen by the tripwire effect,
&gt;&gt; as for most of them it might be assumed they will never move to
&gt;&gt; a safer format, we talk already about 1.7 M of coins or as of
&gt;&gt; today valuation $107 B (the information is on the chain and can
&gt;&gt; be verified).
&gt;&gt;
&gt;&gt; That&#39;s $107B can &#34;burn&#34; in revenue or income that a CRQC-enabled
&gt;&gt; miners coalition to constantly reorg-out the &#34;flag&#34; tx out of the
&gt;&gt; chain. In other terms, something like 5 years of income, and I
&gt;&gt; kindly do not count all the loss coins that are likely to amount
&gt;&gt; to a far bigger &#34;tripwire&#34; neutralization budget.
&gt;&gt;
&gt;&gt; In the name of what a majority of miners will gracefully let on
&gt;&gt; the table an opportunity of massive income ?
&gt;&gt;
&gt;&gt; Leveraging Shor the exploitation might be even done anonymously
&gt;&gt; as the mining process is done. Not even certainty, by who the
&gt;&gt; EC-protected coins could be covertly exfiltrated.
&gt;&gt;
&gt;&gt; That&#39;s the most striking problem when you think about the math
&gt;&gt; with any &#34;tripwire&#34; approach, or even an &#34;hourglass&#34; one relying
&gt;&gt; on a &#34;flag&#34; transaction [1]. I&#39;m ruling out &#34;checkpoints&#34; and
&gt;&gt; any other trust-the-dev approach, as that&#39;s even worst [2].
&gt;&gt;
&gt;&gt; As you&#39;re introducing post is resounding, what the miners
&gt;&gt; are saying now, there are no guarantees on how they would use
&gt;&gt; their hashrate down the road, potentially 10 or 20 years from now.
&gt;&gt;
&gt;&gt; Beyond, and to answer back your point, I still think you can
&gt;&gt; manage an escape hatch of the &#34;tripwire&#34; effect, it&#39;s all depends
&gt;&gt; how the script tripwire logic is implemented, but if you have
&gt;&gt; two OP_SUCCESS of different kinds before your EC CHECKSIG, you
&gt;&gt; can always have a &#34;soft-fork&#34; after the &#34;tripwire&#34; to return 
&gt;&gt; true on the stack, with an EC or hashlock as a success (I agree
&gt;&gt; using undefined op_success in a script is not safe at all) [3].
&gt;&gt;
&gt;&gt; Best,
&gt;&gt; Antoine
&gt;&gt; OTS hash: 4bc91d8dee1625f6e78b27c88bced8e405f25ef6d3d8fd59be8016db5b0fbe66
&gt;&gt;
&gt;&gt; [0] See naumenkog&#39;s 
&gt;&gt; <a
href="https://www.bitmex.com/blog/txwithhold-smart-contracts">https://www.bitmex.com/blog/txwithhold-smart-contracts</a>
&gt;&gt; [1] This is sad, as the &#34;hourglass&#34; depending how the parameters are 
&gt;&gt; chosen
&gt;&gt; was a more acceptable trade-off than pure sunsetting.
&gt;&gt; [2] Given the amounts at stake to sunset, as a group of developers you
&gt;&gt; would just paint yourself a target, there are more even funds at stake
&gt;&gt; that Satoshi herself / himself is assumed to have.
&gt;&gt; [3] There is no security proof in BIP341 on the unforgeability of the
&gt;&gt; NUMS point, if it binds in the ROM or whatever.
&gt;&gt;
&gt;&gt; Le sam. 4 juil. 2026 &#224; 13:47, Sjors Provoost &lt;sj...@sprovoost&#8226;nl&gt; a 
&gt;&gt; &#233;crit :
&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; On Fri, Jul 3, 2026, at 23:23, Pieter Wuille wrote:
&gt;&gt;&gt;
&gt;&gt;&gt; [...]
&gt;&gt;&gt;
&gt;&gt;&gt; &gt; * Just publishing the DLP in a transaction (e.g. OP_RETURN with a 
&gt;&gt;&gt; &gt; specific marker). This is smaller than a full transaction input + 
&gt;&gt;&gt; &gt; signature.
&gt;&gt;&gt; &gt;
&gt;&gt;&gt; &gt; * Similarly, but publishing in the coinbase, and requiring relay using 
&gt;&gt;&gt; &gt; a separate message. Less places a node needs to check, but I&#39;m 
&gt;&gt;&gt; &gt; concerned about the difficulty of testing infrastructure that relay of 
&gt;&gt;&gt; &gt; such a message works
&gt;&gt;&gt;
&gt;&gt;&gt; [...]
&gt;&gt;&gt;
&gt;&gt;&gt; &gt;
&gt;&gt;&gt; &gt; On Saturday, June 27th, 2026 at 12:33 AM, Anthony Towns 
&gt;&gt;&gt; &gt; &lt;a...@erisian&#8226;com.au&gt; wrote:
&gt;&gt;&gt; &gt;
&gt;&gt;&gt; &gt;&gt; A slight variant of this approach would be to have a 128 byte value 
&gt;&gt;&gt; &#34;aRsm&#34;, such that P = N+a*G, N is the BIP-341 NUMS point, and Rs is a 
&gt;&gt;&gt; BIP340 signature of m by P. That would allow the victim of post-quantum 
&gt;&gt;&gt; theft via a key-path spend of a BIP341 NUMS IPK to trigger the tripwire, in 
&gt;&gt;&gt; addition to someone who has direct access to a CRQC.
&gt;&gt;&gt; &gt;
&gt;&gt;&gt; &gt; Indeed, I had considered something similar, but see above for why I&#39;m 
&gt;&gt;&gt; &gt; not convinced supporting non-cooperative CRQCs is that useful.
&gt;&gt;&gt; &gt;
&gt;&gt;&gt; &gt; Also, in my view the tripwire isn&#39;t really a security feature on 
&gt;&gt;&gt; itself 
&gt;&gt;&gt; &gt; (it&#39;s not expected to trigger...), but more something that sets 
&gt;&gt;&gt; &gt; expectations around the output type for prospective users.
&gt;&gt;&gt; &gt;
&gt;&gt;&gt; &gt; In that sense, the question is really whether supporting 
&gt;&gt;&gt; &gt; non-cooperative CRQCs helps set that expectation more than only 
&gt;&gt;&gt; &gt; cooperative ones, which are definitely easier to support.
&gt;&gt;&gt; &gt;
&gt;&gt;&gt; &gt;&gt; I think it could make sense to have the tripwire be included in the 
&gt;&gt;&gt; block via the coinbase witness commitment output, rather than having it be 
&gt;&gt;&gt; locked to a transaction, so you only having to check the coinbase for the 
&gt;&gt;&gt; magic rather than every transaction. That would require a separate P2P 
&gt;&gt;&gt; message to relay the necessary ECDL-break proof to miners, and would 
&gt;&gt;&gt; probably need stratumv2 or a getblocktemplate update in order for the node 
&gt;&gt;&gt; to be able to tell pools to actually include that info in the coinbase.
&gt;&gt;&gt; &gt;
&gt;&gt;&gt; &gt; I worry this is untestable, really. You&#39;d need things like 
&gt;&gt;&gt; &gt; fake-tripwires to be supported through the same message which don&#39;t 
&gt;&gt;&gt; &gt; require an ECDLP break, and still propagate. And then that needs DoS 
&gt;&gt;&gt; &gt; protection measures, 
&gt;&gt;&gt;
&gt;&gt;&gt; I whipped something up last weekend:
&gt;&gt;&gt; <a
href="https://github.com/Sjors/bitcoin/pull/121">https://github.com/Sjors/bitcoin/pull/121</a>
&gt;&gt;&gt;
&gt;&gt;&gt; It seems straightforward, but maybe I missed something:
&gt;&gt;&gt; - for test code we use a fake NUMS point, so we can generate &#34;proof&#34; 
&gt;&gt;&gt; without a quantum computer
&gt;&gt;&gt; - a p2p message floods the proof
&gt;&gt;&gt; - nodes ignore the message if they already have *any* valid proof
&gt;&gt;&gt; - verifying p2p proof candidates might need some rate limiting, but it&#39;s 
&gt;&gt;&gt; as cheap as verifying a transaction signature
&gt;&gt;&gt; - mining code includes the proof in a coinbase op_return, until the 
&gt;&gt;&gt; freeze activates
&gt;&gt;&gt; - with stratum v2 (and ipc mining clients in general this works out of 
&gt;&gt;&gt; the box, a small change is needed for getblocktemplate clients)
&gt;&gt;&gt; - since the proof is not in the header, we can&#39;t use the normal bip9 
&gt;&gt;&gt; style header scan to see if the rule activated. Instead the prototype 
&gt;&gt;&gt; stores it in a file along with a merkle inclusion proof, which is read when 
&gt;&gt;&gt; the node restarts.
&gt;&gt;&gt;
&gt;&gt;&gt; With this mechanism it doesn&#39;t really need to be in the coinbase 
&gt;&gt;&gt; transaction, but that does seem more convenient and miners can censor it 
&gt;&gt;&gt; anyway.
&gt;&gt;&gt;
&gt;&gt;&gt; - Sjors
&gt;&gt;&gt;
&gt;&gt;&gt; -- 
&gt;&gt;&gt; You received this message because you are subscribed to a topic in the 
&gt;&gt;&gt; Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt;&gt;&gt; To unsubscribe from this topic, visit 
&gt;&gt;&gt; <a
href="https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe">https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe</a>.
&gt;&gt;&gt; To unsubscribe from this group and all its topics, send an email to 
&gt;&gt;&gt; bitcoindev+...@googlegroups&#8226;com.
&gt;&gt;&gt; To view this discussion visit 
&gt;&gt;&gt; <a
href="https://groups.google.com/d/msgid/bitcoindev/002f2395-7d5d-4cb6-852c-e991aa1f0eb3%40app.fastmail.com">https://groups.google.com/d/msgid/bitcoindev/002f2395-7d5d-4cb6-852c-e991aa1f0eb3%40app.fastmail.com</a>
&gt;&gt;&gt; .
&gt;&gt;&gt;
&gt;&gt; -- 
&gt;
&gt; You received this message because you are subscribed to the Google Groups 
&gt; &#34;Bitcoin Development Mailing List&#34; group.
&gt; To unsubscribe from this group and stop receiving emails from it, send an 
&gt; email to bitcoindev+...@googlegroups&#8226;com.
&gt; To view this discussion visit 
&gt; <a
href="https://groups.google.com/d/msgid/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can%40googlegroups.com</a>
&gt; .
&gt;
&gt;
&gt;
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/fd947d7c-86fd-407c-98aa-0a63b8be28fan%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/fd947d7c-86fd-407c-98aa-0a63b8be28fan%40googlegroups.com</a>.

<a
href="https://gnusha.org/pi/bitcoindev/fd947d7c-86fd-407c-98aa-0a63b8be28fan@googlegroups.com/1.2-a.bin">[-- Attachment #1.2: Type: text/html, Size: 31037 bytes --]</a>
</pre></div></content></entry><entry><author><name>&#39;conduition&#39; via Bitcoin Development Mailing List</name><email>bitcoindev@googlegroups.com</email></author><title>Re: [bitcoindev] Giving teeth to expected EC disabling: P2XX(-T)(-ML)</title><updated>2026-08-14T18:35:03Z</updated><link
href="https://gnusha.org/pi/bitcoindev/wftCzgJs2k7H-4R22EOqdOhhXYdFPFhSZhsYHvlzejpJ5emoze0ACgL3rrYiTP-X5QQMpThdRW1cO7mr9IQvs2C4MHxSD2eu_gPFGv-yZs8=@proton.me/"/><id>urn:uuid:8fb65f63-7fc6-1731-cfbf-dfb2888fe4a2</id><thr:in-reply-to
ref="urn:uuid:871fc212-cd87-b42f-59cc-c47debafa905"
href="https://gnusha.org/pi/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can@googlegroups.com/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/wftCzgJs2k7H-4R22EOqdOhhXYdFPFhSZhsYHvlzejpJ5emoze0ACgL3rrYiTP-X5QQMpThdRW1cO7mr9IQvs2C4MHxSD2eu_gPFGv-yZs8=@proton.me/1.1.1-a.txt">[-- Attachment #1.1.1: Type: text/plain, Size: 18178 bytes --]</a>

<span
class="q">&gt; An obvious question to raise: would we consider tripwiring a 192 bit group break of a similar type (NUMS)? I find that ... plausible?
</span>

A 192-bit curve i think should be reasonable as a canary, but consider this: If someone already has a QC that breaks 192-bit ECC, how long until they build one which breaks 256-bit ECC? A day, a week, a year? No way of knowing. If the delay is too long, users may see the canary as a false-positive, and migrate back to vulnerable addresses, and they might even be right.&#160;192-bit canaries are vulnerable to classical attack with work approximately 2^96. We should bear in mind the possibility that such a canary could be activated possibly very early, well before Q-day, possibly even in the absence of any quantum computers.

Ideally we want a short gap between &#34;192-bit is broken&#34; and &#34;256-bit is broken&#34;, but not so short as to make the 192-bit canary effectively fungible with a 256-bit canary (because then it&#39;s less likely to be activated before theft occurs).


<span
class="q">&gt; w.r.t. &#39;This guarantees that the NUMS point cannot predate G&#39; yes based on SHA2 preimage resistance, but: isn&#39;t the real point that we&#39;re relying on SHA-2 not being a naughty function so that you couldn&#39;t find G = a * B and SHA2(G) = b*B for some base B in some feasible computation (sans CQRC of course, as was likely back then!). I have no idea what precise name you give to that property. OK, this is a ridiculous thing to discuss, perhaps, given when SHA2 and secp256k1 were standardized :) And given the encoding choices for our BIP341 NUMS (iirc the same as for Elements back in the day? using uncompressed encoding?) were able to be counted on the fingers of the hand which the sleeve does not cover :)
</span>

Anyone can find `G = a * B`. Just generate a key and invert your secret key.

`P = a * G`
G = a**-1 * P

The hard part is then finding some b such that `b*G = SHA256(G).`

---------

If we reflect on the requirement that `G` is fixed, we see `SHA256(G)` is also fixed as a pseudorandom challenge point. The reason for using SHA256 instead of, say, picking an arbitary point by committee or using digits of pi or some other trickery, is that hash outputs are supposed to be random and so `SHA256(G)` is (assumably) a random ECDLP challenge. This matches the classical definition of ECDLP more tightly: Given an arbitrary point `P`, find `p` such that `P = p * G`. The assumption is that if an attacker can factor an honestly-sampled challenge point, they can factor any point. SHA256 is just a stand-in for the &#34;honestly-sampled&#34; part.
However, the following two tasks are actually very different:


1.  Given G, find scalar&#160;`a` such that `a*G = lift_x(SHA256(G))`.
2.  Given G, find scalar&#160;`a` and message `m` such that `a*G = lift_x(SHA256(m))`.


In the case of task 1, if we assume SHA256 output is random, then this is more tightly equivalent to ECDLP, because the point we&#39;re trying to factor is a fixed target, as is the one sampled honestly by the ECDLP security game.

In the case of task 2, the attacker can sample arbitrary messages to create multiple target points, and the attacker wins if they succeed in factoring any of them. The attacker can attack all those target points concurrently if they want, and they get a speedup from doing so.

So I believe it is worth disambiguating canaries between the two cases, because they are different security notions. The first (1) I would call&#160;single-target ECDLP (ST-ECDLP), and the second (2) I would call&#160;multi-target ECDLP (MT-ECDLP).

It&#39;s pretty clear that MT-ECDLP is easier to break, because attackers can make progress against more than one target concurrently, and breaking any one is sufficient to win the security game.

For example, say I sample 2 different messages `m1` and `m2`, and compute ECDLP target points&#160;`T1 = lift_x(SHA256(m1))` and `T2 = lift_x(SHA256(m2))`. Then if I sample a random scalar `r` and compute `R = r*G`, I have two potential chances of success: `R == T1` OR `R == T2`. I can scale up this advantage by generating more targets, `T3`, `T4`, ... and so on.

MT-ECDLP also admits a more efficient basic unit of computation in brute force attacks (including Grover) by using hashes instead of EC point multiplications. If I instead start by picking scalar `t` and fix the target point `T = t*G`, then I can run a brute-force preimage search on SHA256 until I find `m` such that `SHA256(m) == x(T)`. This can also be scaled up using a multi-target attack [1].

With ST-ECDLP, we have only a single fixed message `m = G`, and so the attacker can&#39;t use those multi-target cheat codes. They can parallelize, use pollard-rho or Shor or other algorithms, but they have only a single target point that they must break to win the game.

The method Pieter suggested using for the canary construction is equivalent to single-target ECDLP.

I&#39;ve heard others (e.g. Tadge in this thread) previously suggest using a script like `OP_SHA256 OP_CHECKSIG` as a canary, where any spend of such a script would trigger the canary. This would be multi-target ECDLP.

I&#39;m not sure which is better.&#160;


-   ST-ECDLP is less likely to be triggered early or mistakenly, and is more tightly equivalent to ECDLP.&#160;

-   MT-ECDLP is more reflective of how real-world attackers behave on Bitcoin (e.g. with thousands-to-millions of public keys available to attack in parallel, and breaking even one is considered unacceptable).



I&#39;m slightly leanings towards a construction like Pieter&#39;s, featuring ST-ECDLP, just because I&#39;m not sure what other tricks could be used to potentially trigger MT-ECDLP classically or quantumly.

We could also engineer a compromise between the two, where we limit the number of targets. For example, define the game like this:


Given `G`, find scalar `a` and 32-bit integer&#160;`i` such that `a*G = lift_x(SHA256(G || i))`.


Then the adversary can only attack against at most 2^32 unique target points, and those targets are fixed forever, for any adversary. This is an easier problem than ST-ECDLP, but harder than MT-ECDLP. Maybe call it limited multi-target ECDLP (LMT-ECDLP)?


regards,
conduition


[1]: First, generate a bunch of target points. Sample scalar&#160;`t` and compute `T0 = t * G`, T1 = T0 + T0, and T2 = T1 + T1, and T3 = T2 + T2, etc. Why double each point? point doubling is cheaper than addition or multiplication, and still covers the whole curve. Then we run a multi-target SHA256 preimage search over all targets [x(T0), x(T1), x(T2), x(T3), ...]. If we have n targets and curve order N, then each message hash has an `n/N` chance of success. If we find a valid message `m`, such that `SHA256(m) == x(R_i)` for some target index `i`, then we have found `T_i = t * 2**i * G = lift_x(SHA256(m))`.





On Thursday, August 13th, 2026 at 2:02 AM, waxwing/ AdamISZ &lt;ekaggata@gmail&#8226;com&gt; wrote:

<span
class="q">&gt; This tripwire idea is interesting. Basically &#34;canary in consensus&#34;.
&gt; I agree it&#39;s valuable. In the scenario of adversarial actor(s) gaining access to CQRC first, i.e. no whitehats, only blackhats, obviously nothing to discuss; touching a NUMS ECDL is the last thing they&#39;ll do. So I&#39;m slightly worried that the general userbase will not notice that point, instead thinking it&#39;s a solid defense when it ... depends.
&gt; 
</span>
<span
class="q">&gt; In the scenario of at least some whitehats, we get wires tripped, or canaries singing. Having it in consensus is nice. The blockchain then does its job of being an unambiguous signal and we can have all the arguments well ahead of time. [1]
&gt; 
</span>
<span
class="q">&gt; On the other hand, we traditionally design such systems adversarially, right, so you could argue that an overfocus on this might be suboptimal - it might be better to do other things.
&gt; 
</span>
<span
class="q">&gt; (Similar comment applies to the &#39;smaller group canary&#39; - definitely nothing wrong with it, but it is not in itself a defence unless we strongly believe whitehats, and *active* whitehats at that, are keeping up). An obvious question to raise: would we consider tripwiring a 192 bit group break of a similar type (NUMS)? I find that ... plausible?
&gt; &gt; The BIP341 NUMS point (which I suggest using in this context) is the point whose X coordinate is the SHA256 hash of the generator point G. This guarantees that the NUMS point cannot predate G (if it did, it would be possible in theory that secp256k1&#39;s designers actually chose G in function of what we call that NUMS point, giving it a DLP known to them).
&gt; 
</span>
<span
class="q">&gt; w.r.t. &#39;This guarantees that the NUMS point cannot predate G&#39; yes based on SHA2 preimage resistance, but: isn&#39;t the real point that we&#39;re relying on SHA-2 not being a naughty function so that you couldn&#39;t find G = a * B and SHA2(G) = b*B for some base B in some feasible computation (sans CQRC of course, as was likely back then!). I have no idea what precise name you give to that property. OK, this is a ridiculous thing to discuss, perhaps, given when SHA2 and secp256k1 were standardized :) And given the encoding choices for our BIP341 NUMS (iirc the same as for Elements back in the day? using uncompressed encoding?) were able to be counted on the fingers of the hand which the sleeve does not cover :)
&gt; 
</span>
<span
class="q">&gt; [1] I take Antoine&#39;s point that making it consensus means the miners are involved and there is a non-trivial collusion risk if the stakes are high, but I can&#39;t see how this scenario is *worse* than no tripwire?
&gt; 
</span>
<span
class="q">&gt; On Sunday, July 5, 2026 at 4:07:33&#8239;PM UTC-6 Antoine Riard wrote:
&gt; 
</span>
<span
class="q">&gt; &gt; Hi Pieter,
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Thanks for the observations.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; When I was saying there is a problem with the game theory,
&gt; &gt; it&#39;s that strikingly, any activation of the tripwire logic
&gt; &gt; would rely on a &#34;flag&#34; transaction being mined in the chain
&gt; &gt; for the network nodes starting to enforce at the block N or
&gt; &gt; N+1 or whatever the EC disabling threshold.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Any &#34;flag&#34; transaction can be itself re-orged out of the chain
&gt; &gt; to purely disable the effects of the EC disabling threshold,
&gt; &gt; therefore make it null and void as an effect. One might see
&gt; &gt; it as a competing race between a group of &#34;sunsetting&#34; users
&gt; &gt; and a (majority) coalition of miners in coordination with a
&gt; &gt; CRQC adversary, where the latter have an interest and the
&gt; &gt; hashrate capabilities to do a tx-withold [0].
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; In pure terms of satoshi fee denominated calculus, empirically
&gt; &gt; global miners have won an average of $20 B yearly. If we only
&gt; &gt; consider that P2PK are going to be frozen by the tripwire effect,
&gt; &gt; as for most of them it might be assumed they will never move to
&gt; &gt; a safer format, we talk already about 1.7 M of coins or as of
&gt; &gt; today valuation $107 B (the information is on the chain and can
&gt; &gt; be verified).
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; That&#39;s $107B can &#34;burn&#34; in revenue or income that a CRQC-enabled
&gt; &gt; miners coalition to constantly reorg-out the &#34;flag&#34; tx out of the
&gt; &gt; chain. In other terms, something like 5 years of income, and I
&gt; &gt; kindly do not count all the loss coins that are likely to amount
&gt; &gt; to a far bigger &#34;tripwire&#34; neutralization budget.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; In the name of what a majority of miners will gracefully let on
&gt; &gt; the table an opportunity of massive income ?
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Leveraging Shor the exploitation might be even done anonymously
&gt; &gt; as the mining process is done. Not even certainty, by who the
&gt; &gt; EC-protected coins could be covertly exfiltrated.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; That&#39;s the most striking problem when you think about the math
&gt; &gt; with any &#34;tripwire&#34; approach, or even an &#34;hourglass&#34; one relying
&gt; &gt; on a &#34;flag&#34; transaction [1]. I&#39;m ruling out &#34;checkpoints&#34; and
&gt; &gt; any other trust-the-dev approach, as that&#39;s even worst [2].
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; As you&#39;re introducing post is resounding, what the miners
&gt; &gt; are saying now, there are no guarantees on how they would use
&gt; &gt; their hashrate down the road, potentially 10 or 20 years from now.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Beyond, and to answer back your point, I still think you can
&gt; &gt; manage an escape hatch of the &#34;tripwire&#34; effect, it&#39;s all depends
&gt; &gt; how the script tripwire logic is implemented, but if you have
&gt; &gt; two OP_SUCCESS of different kinds before your EC CHECKSIG, you
&gt; &gt; can always have a &#34;soft-fork&#34; after the &#34;tripwire&#34; to return
&gt; &gt; true on the stack, with an EC or hashlock as a success (I agree
&gt; &gt; using undefined op_success in a script is not safe at all) [3].
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Best,
&gt; &gt; Antoine
&gt; &gt; OTS hash: 4bc91d8dee1625f6e78b27c88bced8e405f25ef6d3d8fd59be8016db5b0fbe66
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; [0] See naumenkog&#39;s <a
href="https://www.bitmex.com/blog/txwithhold-smart-contracts">https://www.bitmex.com/blog/txwithhold-smart-contracts</a>
&gt; &gt; [1] This is sad, as the &#34;hourglass&#34; depending how the parameters are chosen
&gt; &gt; was a more acceptable trade-off than pure sunsetting.
&gt; &gt; [2] Given the amounts at stake to sunset, as a group of developers you
&gt; &gt; would just paint yourself a target, there are more even funds at stake
&gt; &gt; that Satoshi herself / himself is assumed to have.
&gt; &gt; [3] There is no security proof in BIP341 on the unforgeability of the
&gt; &gt; NUMS point, if it binds in the ROM or whatever.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Le sam. 4 juil. 2026 &#224; 13:47, Sjors Provoost &lt;sj...@sprovoost&#8226;nl&gt; a &#233;crit :
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; On Fri, Jul 3, 2026, at 23:23, Pieter Wuille wrote:
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; [...]
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; * Just publishing the DLP in a transaction (e.g. OP_RETURN with a
&gt; &gt; &gt; &gt; specific marker). This is smaller than a full transaction input +
&gt; &gt; &gt; &gt; signature.
&gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt; * Similarly, but publishing in the coinbase, and requiring relay using
&gt; &gt; &gt; &gt; a separate message. Less places a node needs to check, but I&#39;m
&gt; &gt; &gt; &gt; concerned about the difficulty of testing infrastructure that relay of
&gt; &gt; &gt; &gt; such a message works
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; [...]
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt; On Saturday, June 27th, 2026 at 12:33 AM, Anthony Towns
&gt; &gt; &gt; &gt; &lt;a...@erisian&#8226;com.au&gt; wrote:
&gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt;&gt; A slight variant of this approach would be to have a 128 byte value &#34;aRsm&#34;, such that P = N+a*G, N is the BIP-341 NUMS point, and Rs is a BIP340 signature of m by P. That would allow the victim of post-quantum theft via a key-path spend of a BIP341 NUMS IPK to trigger the tripwire, in addition to someone who has direct access to a CRQC.
&gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt; Indeed, I had considered something similar, but see above for why I&#39;m
&gt; &gt; &gt; &gt; not convinced supporting non-cooperative CRQCs is that useful.
&gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt; Also, in my view the tripwire isn&#39;t really a security feature on itself
&gt; &gt; &gt; &gt; (it&#39;s not expected to trigger...), but more something that sets
&gt; &gt; &gt; &gt; expectations around the output type for prospective users.
&gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt; In that sense, the question is really whether supporting
&gt; &gt; &gt; &gt; non-cooperative CRQCs helps set that expectation more than only
&gt; &gt; &gt; &gt; cooperative ones, which are definitely easier to support.
&gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt;&gt; I think it could make sense to have the tripwire be included in the block via the coinbase witness commitment output, rather than having it be locked to a transaction, so you only having to check the coinbase for the magic rather than every transaction. That would require a separate P2P message to relay the necessary ECDL-break proof to miners, and would probably need stratumv2 or a getblocktemplate update in order for the node to be able to tell pools to actually include that info in the coinbase.
&gt; &gt; &gt; &gt;
&gt; &gt; &gt; &gt; I worry this is untestable, really. You&#39;d need things like
&gt; &gt; &gt; &gt; fake-tripwires to be supported through the same message which don&#39;t
&gt; &gt; &gt; &gt; require an ECDLP break, and still propagate. And then that needs DoS
&gt; &gt; &gt; &gt; protection measures,
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; I whipped something up last weekend:
&gt; &gt; &gt; <a
href="https://github.com/Sjors/bitcoin/pull/121">https://github.com/Sjors/bitcoin/pull/121</a>
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; It seems straightforward, but maybe I missed something:
&gt; &gt; &gt; - for test code we use a fake NUMS point, so we can generate &#34;proof&#34; without a quantum computer
&gt; &gt; &gt; - a p2p message floods the proof
&gt; &gt; &gt; - nodes ignore the message if they already have *any* valid proof
&gt; &gt; &gt; - verifying p2p proof candidates might need some rate limiting, but it&#39;s as cheap as verifying a transaction signature
&gt; &gt; &gt; - mining code includes the proof in a coinbase op_return, until the freeze activates
&gt; &gt; &gt; - with stratum v2 (and ipc mining clients in general this works out of the box, a small change is needed for getblocktemplate clients)
&gt; &gt; &gt; - since the proof is not in the header, we can&#39;t use the normal bip9 style header scan to see if the rule activated. Instead the prototype stores it in a file along with a merkle inclusion proof, which is read when the node restarts.
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; With this mechanism it doesn&#39;t really need to be in the coinbase transaction, but that does seem more convenient and miners can censor it anyway.
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; - Sjors
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; --
&gt; &gt; &gt; You received this message because you are subscribed to a topic in the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt; &gt; &gt; To unsubscribe from this topic, visit <a
href="https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe">https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe</a>.
&gt; &gt; &gt; To unsubscribe from this group and all its topics, send an email to bitcoindev+...@googlegroups&#8226;com.
&gt; &gt; &gt; To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/002f2395-7d5d-4cb6-852c-e991aa1f0eb3%40app.fastmail.com">https://groups.google.com/d/msgid/bitcoindev/002f2395-7d5d-4cb6-852c-e991aa1f0eb3%40app.fastmail.com</a>.
&gt; 
</span>
<span
class="q">&gt; --
&gt; You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt; To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
&gt; To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can%40googlegroups.com</a>.
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/wftCzgJs2k7H-4R22EOqdOhhXYdFPFhSZhsYHvlzejpJ5emoze0ACgL3rrYiTP-X5QQMpThdRW1cO7mr9IQvs2C4MHxSD2eu_gPFGv-yZs8%3D%40proton.me">https://groups.google.com/d/msgid/bitcoindev/wftCzgJs2k7H-4R22EOqdOhhXYdFPFhSZhsYHvlzejpJ5emoze0ACgL3rrYiTP-X5QQMpThdRW1cO7mr9IQvs2C4MHxSD2eu_gPFGv-yZs8%3D%40proton.me</a>.

<a
href="https://gnusha.org/pi/bitcoindev/wftCzgJs2k7H-4R22EOqdOhhXYdFPFhSZhsYHvlzejpJ5emoze0ACgL3rrYiTP-X5QQMpThdRW1cO7mr9IQvs2C4MHxSD2eu_gPFGv-yZs8=@proton.me/1.1.2.1-a.bin">[-- Attachment #1.1.2.1: Type: text/html, Size: 26286 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/wftCzgJs2k7H-4R22EOqdOhhXYdFPFhSZhsYHvlzejpJ5emoze0ACgL3rrYiTP-X5QQMpThdRW1cO7mr9IQvs2C4MHxSD2eu_gPFGv-yZs8=@proton.me/1.2-a.bin">[-- Attachment #1.2: publickey - conduition@proton.me - 0x474891AD.asc --]
[-- Type: application/pgp-keys, Size: 649 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/wftCzgJs2k7H-4R22EOqdOhhXYdFPFhSZhsYHvlzejpJ5emoze0ACgL3rrYiTP-X5QQMpThdRW1cO7mr9IQvs2C4MHxSD2eu_gPFGv-yZs8=@proton.me/2-signature.asc">[-- Attachment #2: OpenPGP digital signature --]
[-- Type: application/pgp-signature, Size: 343 bytes --]</a>
</pre></div></content></entry><entry><author><name>Ram</name><email>pseudoramdom8@gmail.com</email></author><title>Re: [bitcoindev] [BIP Proposal] Stale Tip Relay</title><updated>2026-08-13T18:58:07Z</updated><link
href="https://gnusha.org/pi/bitcoindev/7bbef0df-dbb5-48d1-9671-b0cec91fcbb0n@googlegroups.com/"/><id>urn:uuid:a18a861e-9f01-087e-d677-f2e89893fdd3</id><thr:in-reply-to
ref="urn:uuid:4145c057-6676-cf74-bed0-2c06f3d84ba1"
href="https://gnusha.org/pi/bitcoindev/CANJiN3+KetUeNjjeRgd7xgCSF+vAakDtH7ysPC+h4DqtHJPsLA@mail.gmail.com/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/7bbef0df-dbb5-48d1-9671-b0cec91fcbb0n@googlegroups.com/1.1-a.txt">[-- Attachment #1.1: Type: text/plain, Size: 7922 bytes --]</a>

Hi Edil,

Appreciate taking the time to review the BIP.

<span
class="q">&gt; But I&#39;m not so sure about how that improves the main purpose of the 
</span>network. 
Quite the contrary, seems to open more DoS and fingerprinting vectors.

For DoS, the concern is whether a small message can cause disproportionate 
processing, disk usage, or outgoing traffic. Merely sending invalid data is
not a new DoS vector; peers already have many ways to do that. It&#39;s not 
possible to prevent all of them.

Currently, I don&#8217;t see any resource-exhaustion or bandwidth amplification 
vector
introduced by this proposal. Processing is bounded by the branch-length,
recency and retained-tip limits. Nodes are not required to download stale 
block
data. Nodes that choose to collect it use the normal block-download 
mechanisms
and resource limits. Implementations may also apply stricter limits, 
rate-limit
abusive peers, or disable the feature.
Also on mainnet, producing stale headers requires real proof of work 
comparable
to the active chain.
  
On fingerprinting - supporting staletip does add another observable 
characteristic.
This is a trade-off the node makes when enabling the feature and is common 
to 
optional P2P features generally. Nodes for which this trade-off is 
unacceptable
can disable staletip relay.

<span
class="q">&gt; About the design, it&#39;s not clear to me how that could work in face of more
</span>than one competing chain.

Each staletip message describes one linear branch. Assuming A1-A2-A3-A4 is 
the 
active chain, the two competing branches would be announced separately:

staletip(fork_point=A2, headers=[B3, B4])
staletip(fork_point=A3, headers=[C4])

The protocol announces competing branches in separate messages. 
I&#8217;ve clarified this in the BIP draft. Thanks for pointing it out :)

Thanks again for reviewing. Hope this addresses your concerns.
Feel free to reach out or leave additional comments.

Cheers,
Ram

On Tuesday, August 11, 2026 at 7:04:41&#8239;AM UTC-7 Edil Guimar&#227;es de Medeiros 
wrote:

<span
class="q">&gt; There&#39;s an ongoing effort to document mainnet stale blocks: 
&gt; <a
href="https://github.com/bitcoin-data/stale-blocks">https://github.com/bitcoin-data/stale-blocks</a>
&gt; As one can imagine, since there is currently no way to recover them from 
&gt; the network itself, this
&gt; requires constantly monitoring several long running nodes in the hope to 
&gt; get them. From a monitoring
&gt; and research perspective, this proposal could be useful.
&gt;
&gt; But I&#39;m not so sure about how that improves the main purpose of the 
&gt; network. Quite the contrary, seems
&gt; to open more DoS and fingerprinting vectors.
&gt;
&gt; About the design, it&#39;s not clear to me how that could work in face of more 
&gt; than one competing chain. For
&gt; instance, suppose I have:
&gt;
&gt;             /- C4
&gt; A1 - A2 - A3 - A4
&gt;        \- B3 - B4
&gt;
&gt; It&#39;s not clear to me how the proposal deals with communicating this, which 
&gt; is quite common in signet and 
&gt; the testnets, since each message is designed to relay a single competing 
&gt; branch (e.g. B3-B4 above).
&gt;
&gt; Left more detailed and editorial comments in the bip repository PR.
&gt;
&gt; Cheers.
&gt; Edil
&gt;
&gt; Em qua., 29 de jul. de 2026 &#224;s 14:28, Ram &lt;pseudo...@gmail&#8226;com&gt; escreveu:
&gt;
&gt;&gt; Hello list,
&gt;&gt;
&gt;&gt; This proposal introduces `staletip`, an opt-in P2P message for relaying 
&gt;&gt; recent
&gt;&gt; stale tips between peers. Building on AJ Towns&#39; initial work, w0xlt and I 
&gt;&gt; have
&gt;&gt; developed the proposal further and built a proof-of-concept 
&gt;&gt; implementation.
&gt;&gt;
&gt;&gt; Draft BIP:
&gt;&gt;
&gt;&gt; <a
href="https://github.com/pseudoramdom/bips/blob/staletip-bip-draft/bip-staletip.md">https://github.com/pseudoramdom/bips/blob/staletip-bip-draft/bip-staletip.md</a>
&gt;&gt;
&gt;&gt; Proof-of-concept:
&gt;&gt; <a
href="https://github.com/w0xlt/bitcoin/tree/staletip-v4">https://github.com/w0xlt/bitcoin/tree/staletip-v4</a>
&gt;&gt;
&gt;&gt; Today, once a block loses a race and goes stale, it stops propagating &#8211; 
&gt;&gt; compact
&gt;&gt; block relay and FIBRE aggressively relay the winning chain, while stale 
&gt;&gt; branches fall away. That&#39;s great for fast propagation, but it makes the 
&gt;&gt; stale
&gt;&gt; rate difficult to observe. Even dedicated monitors [0] have only partial 
&gt;&gt; views:
&gt;&gt; a stale block seen by one monitor may never reach another.
&gt;&gt;
&gt;&gt; The stale rate is a useful network-health signal because it is closely 
&gt;&gt; related
&gt;&gt; to block propagation delay. The longer it takes miners to learn about a 
&gt;&gt; newly
&gt;&gt; found block, the greater the chance that another valid block will be 
&gt;&gt; found at
&gt;&gt; the same height, creating a race in which one of the blocks becomes stale 
&gt;&gt; [1].
&gt;&gt; An elevated stale rate could also expose validation or relay bottlenecks.
&gt;&gt; For example, the May 2023 &#34;inv-to-send&#34; bug degraded block propagation and
&gt;&gt; coincided with a roughly 10x increase in the observed stale rate [2].
&gt;&gt;
&gt;&gt; A stale block does not by itself identify its cause, but changes in the
&gt;&gt; rate or shape of stale branches can provide a reason to investigate:
&gt;&gt;
&gt;&gt;   - a network partition &#8211; when a partition heals, blocks mined on the
&gt;&gt;     losing side become stale, potentially producing several related stale
&gt;&gt;     blocks at once.
&gt;&gt;   - adversarial mining strategies such as selfish mining [3] &#8211; these
&gt;&gt;     can cause honest miners&#39; blocks to become stale.
&gt;&gt;
&gt;&gt; The proposal fills this observability gap with an opt-in P2P message 
&gt;&gt; called
&gt;&gt; `staletip`, allowing nodes to proactively announce recent stale tips to 
&gt;&gt; peers.
&gt;&gt;
&gt;&gt; An added benefit is potentially faster reorg handling: if a node already 
&gt;&gt; knows
&gt;&gt; the relevant headers, and perhaps has the block data, it has less work to 
&gt;&gt; do if
&gt;&gt; that branch later becomes active.
&gt;&gt;
&gt;&gt; At protocol level, nodes advertise support using BIP 434 `feature` 
&gt;&gt; message [4], 
&gt;&gt; and `staletip` messages are only sent to peers that advertised support. 
&gt;&gt; Each
&gt;&gt; announcement contains the fork point, a sequence of compressed headers, 
&gt;&gt; and a
&gt;&gt; flag indicating whether the sender can serve the stale tip block. 
&gt;&gt;
&gt;&gt; The proposed default relay policy:
&gt;&gt;   - relays only tips within 1000 blocks (about seven days) of the active 
&gt;&gt; tip, 
&gt;&gt;     keeping announcements recent and stale-tip spam costly on mainnet.
&gt;&gt;   - limits branches to 20 compressed headers, covering short-term reorgs
&gt;&gt;     without tracking persistent chain splits and keeps each announcement 
&gt;&gt; under
&gt;&gt;     1 kB.
&gt;&gt;   - keeps at most 10 recent tips in the relay cache, so announcing the 
&gt;&gt; full
&gt;&gt;     cache to a new peer remains under 10 kB, excluding any blocks 
&gt;&gt; requested.
&gt;&gt;
&gt;&gt; The BIP text has more background and the full message format. Comments are
&gt;&gt; welcome.
&gt;&gt;
&gt;&gt; Cheers,
&gt;&gt; Ram (pseudoramdom &lt;<a
href="https://github.com/pseudoramdom">https://github.com/pseudoramdom</a>&gt;)
&gt;&gt; &#38; 
&gt;&gt; w0xlt &lt;<a
href="https://github.com/w0xlt">https://github.com/w0xlt</a>&gt;
&gt;&gt;
&gt;&gt; [0] <a
href="https://github.com/bitcoin-data/stale-blocks">https://github.com/bitcoin-data/stale-blocks</a>
&gt;&gt; [1] 
&gt;&gt; <a
href="https://delvingbitcoin.org/t/propagation-delay-and-mining-centralization-modeling-stale-rates/2110">https://delvingbitcoin.org/t/propagation-delay-and-mining-centralization-modeling-stale-rates/2110</a>
&gt;&gt; [2] <a
href="https://b10c.me/observations/15-inv-to-send-queue/">https://b10c.me/observations/15-inv-to-send-queue/</a>
&gt;&gt; [3] <a
href="https://arxiv.org/abs/1311.0243">https://arxiv.org/abs/1311.0243</a>
&gt;&gt; [4] <a
href="https://github.com/bitcoin/bips/blob/master/bip-0434.md">https://github.com/bitcoin/bips/blob/master/bip-0434.md</a>
&gt;&gt;
&gt;&gt; -- 
&gt;&gt; You received this message because you are subscribed to the Google Groups 
&gt;&gt; &#34;Bitcoin Development Mailing List&#34; group.
&gt;&gt; To unsubscribe from this group and stop receiving emails from it, send an 
&gt;&gt; email to bitcoindev+...@googlegroups&#8226;com.
&gt;&gt; To view this discussion visit 
&gt;&gt; <a
href="https://groups.google.com/d/msgid/bitcoindev/d92f1615-368b-4406-b326-a1799c72a555n%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/d92f1615-368b-4406-b326-a1799c72a555n%40googlegroups.com</a> 
&gt;&gt; &lt;<a
href="https://groups.google.com/d/msgid/bitcoindev/d92f1615-368b-4406-b326-a1799c72a555n%40googlegroups.com?utm_medium=email&#38;utm_source=footer">https://groups.google.com/d/msgid/bitcoindev/d92f1615-368b-4406-b326-a1799c72a555n%40googlegroups.com?utm_medium=email&#38;utm_source=footer</a>&gt;
&gt;&gt; .
&gt;&gt;
&gt;
&gt;
&gt; -- 
&gt; Edil
&gt;
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/7bbef0df-dbb5-48d1-9671-b0cec91fcbb0n%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/7bbef0df-dbb5-48d1-9671-b0cec91fcbb0n%40googlegroups.com</a>.

<a
href="https://gnusha.org/pi/bitcoindev/7bbef0df-dbb5-48d1-9671-b0cec91fcbb0n@googlegroups.com/1.2-a.bin">[-- Attachment #1.2: Type: text/html, Size: 12761 bytes --]</a>
</pre></div></content></entry><entry><author><name>waxwing/ AdamISZ</name><email>ekaggata@gmail.com</email></author><title>Re: [bitcoindev] Giving teeth to expected EC disabling: P2XX(-T)(-ML)</title><updated>2026-08-13T07:02:15Z</updated><link
href="https://gnusha.org/pi/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can@googlegroups.com/"/><id>urn:uuid:871fc212-cd87-b42f-59cc-c47debafa905</id><thr:in-reply-to
ref="urn:uuid:bbab4630-838d-9cb6-006c-af603595bb6e"
href="https://gnusha.org/pi/bitcoindev/CALZpt+FMHG3yoOCXPfMhS=KFF9bn+rCi9NL836GDRp1CKTBXRA@mail.gmail.com/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can@googlegroups.com/1.1-a.txt">[-- Attachment #1.1: Type: text/plain, Size: 10568 bytes --]</a>

This tripwire idea is interesting. Basically &#34;canary in consensus&#34;.

I agree it&#39;s valuable. In the scenario of adversarial actor(s) gaining 
access to CQRC first, i.e. no whitehats, only blackhats, obviously nothing 
to discuss; touching a NUMS ECDL is the last thing they&#39;ll do. So I&#39;m 
slightly worried that the general userbase will not notice that point, 
instead thinking it&#39;s a solid defense when it ... depends.

In the scenario of at least some whitehats, we get wires tripped, or 
canaries singing. Having it in consensus is nice. The blockchain then does 
its job of being an unambiguous signal and we can have all the arguments 
well ahead of time. [1]

On the other hand, we traditionally design such systems adversarially, 
right, so you could argue that an overfocus on this might be suboptimal - 
it might be better to do other things.

(Similar comment applies to the &#39;smaller group canary&#39; - definitely nothing 
wrong with it, but it is not in itself a defence unless we strongly believe 
whitehats, and *active* whitehats at that, are keeping up). An obvious 
question to raise: would we consider tripwiring a 192 bit group break of a 
similar type (NUMS)? I find that ... plausible?

<span
class="q">&gt; The BIP341 NUMS point (which I suggest using in this context) is the 
</span>point whose X coordinate is the SHA256 hash of the generator point G. This 
guarantees that the NUMS point cannot predate G (if it did, it would be 
possible in theory that secp256k1&#39;s designers actually chose G in function 
of what we call that NUMS point, giving it a DLP known to them).

w.r.t. &#39;This guarantees that the NUMS point cannot predate G&#39; yes based on 
SHA2 preimage resistance, but: isn&#39;t the real point that we&#39;re relying on 
SHA-2 not being a naughty function so that you couldn&#39;t find G = a * B and 
SHA2(G) = b*B for some base B in some feasible computation (sans CQRC of 
course, as was likely back then!). I have no idea what precise name you 
give to that property. OK, this is a ridiculous thing to discuss, perhaps, 
given when SHA2 and secp256k1 were standardized :) And given the encoding 
choices for our BIP341 NUMS (iirc the same as for Elements back in the day? 
using uncompressed encoding?) were able to be counted on the fingers of the 
hand which the sleeve does not cover :)

[1] I take Antoine&#39;s point that making it consensus means the miners are 
involved and there is a non-trivial collusion risk if the stakes are high, 
but I can&#39;t see how this scenario is *worse* than no tripwire?

On Sunday, July 5, 2026 at 4:07:33&#8239;PM UTC-6 Antoine Riard wrote:

<span
class="q">&gt; Hi Pieter,
&gt;
&gt; Thanks for the observations.
&gt;
&gt; When I was saying there is a problem with the game theory,
&gt; it&#39;s that strikingly, any activation of the tripwire logic
&gt; would rely on a &#34;flag&#34; transaction being mined in the chain
&gt; for the network nodes starting to enforce at the block N or
&gt; N+1 or whatever the EC disabling threshold.
&gt;
&gt; Any &#34;flag&#34; transaction can be itself re-orged out of the chain
&gt; to purely disable the effects of the EC disabling threshold,
&gt; therefore make it null and void as an effect. One might see
&gt; it as a competing race between a group of &#34;sunsetting&#34; users
&gt; and a (majority) coalition of miners in coordination with a
&gt; CRQC adversary, where the latter have an interest and the
&gt; hashrate capabilities to do a tx-withold [0].
&gt;
&gt; In pure terms of satoshi fee denominated calculus, empirically
&gt; global miners have won an average of $20 B yearly. If we only
&gt; consider that P2PK are going to be frozen by the tripwire effect,
&gt; as for most of them it might be assumed they will never move to
&gt; a safer format, we talk already about 1.7 M of coins or as of
&gt; today valuation $107 B (the information is on the chain and can
&gt; be verified).
&gt;
&gt; That&#39;s $107B can &#34;burn&#34; in revenue or income that a CRQC-enabled
&gt; miners coalition to constantly reorg-out the &#34;flag&#34; tx out of the
&gt; chain. In other terms, something like 5 years of income, and I
&gt; kindly do not count all the loss coins that are likely to amount
&gt; to a far bigger &#34;tripwire&#34; neutralization budget.
&gt;
&gt; In the name of what a majority of miners will gracefully let on
&gt; the table an opportunity of massive income ?
&gt;
&gt; Leveraging Shor the exploitation might be even done anonymously
&gt; as the mining process is done. Not even certainty, by who the
&gt; EC-protected coins could be covertly exfiltrated.
&gt;
&gt; That&#39;s the most striking problem when you think about the math
&gt; with any &#34;tripwire&#34; approach, or even an &#34;hourglass&#34; one relying
&gt; on a &#34;flag&#34; transaction [1]. I&#39;m ruling out &#34;checkpoints&#34; and
&gt; any other trust-the-dev approach, as that&#39;s even worst [2].
&gt;
&gt; As you&#39;re introducing post is resounding, what the miners
&gt; are saying now, there are no guarantees on how they would use
&gt; their hashrate down the road, potentially 10 or 20 years from now.
&gt;
&gt; Beyond, and to answer back your point, I still think you can
&gt; manage an escape hatch of the &#34;tripwire&#34; effect, it&#39;s all depends
&gt; how the script tripwire logic is implemented, but if you have
&gt; two OP_SUCCESS of different kinds before your EC CHECKSIG, you
&gt; can always have a &#34;soft-fork&#34; after the &#34;tripwire&#34; to return 
&gt; true on the stack, with an EC or hashlock as a success (I agree
&gt; using undefined op_success in a script is not safe at all) [3].
&gt;  
&gt; Best,
&gt; Antoine
&gt; OTS hash: 4bc91d8dee1625f6e78b27c88bced8e405f25ef6d3d8fd59be8016db5b0fbe66
&gt;
&gt; [0] See naumenkog&#39;s <a
href="https://www.bitmex.com/blog/txwithhold-smart-contracts">https://www.bitmex.com/blog/txwithhold-smart-contracts</a>
&gt; [1] This is sad, as the &#34;hourglass&#34; depending how the parameters are chosen
&gt; was a more acceptable trade-off than pure sunsetting.
&gt; [2] Given the amounts at stake to sunset, as a group of developers you
&gt; would just paint yourself a target, there are more even funds at stake
&gt; that Satoshi herself / himself is assumed to have.
&gt; [3] There is no security proof in BIP341 on the unforgeability of the
&gt; NUMS point, if it binds in the ROM or whatever.
&gt;
&gt; Le sam. 4 juil. 2026 &#224; 13:47, Sjors Provoost &lt;sj...@sprovoost&#8226;nl&gt; a 
&gt; &#233;crit :
&gt;
&gt;&gt;
&gt;&gt;
&gt;&gt; On Fri, Jul 3, 2026, at 23:23, Pieter Wuille wrote:
&gt;&gt;
&gt;&gt; [...]
&gt;&gt;
&gt;&gt; &gt; * Just publishing the DLP in a transaction (e.g. OP_RETURN with a 
&gt;&gt; &gt; specific marker). This is smaller than a full transaction input + 
&gt;&gt; &gt; signature.
&gt;&gt; &gt;
&gt;&gt; &gt; * Similarly, but publishing in the coinbase, and requiring relay using 
&gt;&gt; &gt; a separate message. Less places a node needs to check, but I&#39;m 
&gt;&gt; &gt; concerned about the difficulty of testing infrastructure that relay of 
&gt;&gt; &gt; such a message works
&gt;&gt;
&gt;&gt; [...]
&gt;&gt;
&gt;&gt; &gt;
&gt;&gt; &gt; On Saturday, June 27th, 2026 at 12:33 AM, Anthony Towns 
&gt;&gt; &gt; &lt;a...@erisian&#8226;com.au&gt; wrote:
&gt;&gt; &gt;
&gt;&gt; &gt;&gt; A slight variant of this approach would be to have a 128 byte value 
&gt;&gt; &#34;aRsm&#34;, such that P = N+a*G, N is the BIP-341 NUMS point, and Rs is a 
&gt;&gt; BIP340 signature of m by P. That would allow the victim of post-quantum 
&gt;&gt; theft via a key-path spend of a BIP341 NUMS IPK to trigger the tripwire, in 
&gt;&gt; addition to someone who has direct access to a CRQC.
&gt;&gt; &gt;
&gt;&gt; &gt; Indeed, I had considered something similar, but see above for why I&#39;m 
&gt;&gt; &gt; not convinced supporting non-cooperative CRQCs is that useful.
&gt;&gt; &gt;
&gt;&gt; &gt; Also, in my view the tripwire isn&#39;t really a security feature on itself 
&gt;&gt; &gt; (it&#39;s not expected to trigger...), but more something that sets 
&gt;&gt; &gt; expectations around the output type for prospective users.
&gt;&gt; &gt;
&gt;&gt; &gt; In that sense, the question is really whether supporting 
&gt;&gt; &gt; non-cooperative CRQCs helps set that expectation more than only 
&gt;&gt; &gt; cooperative ones, which are definitely easier to support.
&gt;&gt; &gt;
&gt;&gt; &gt;&gt; I think it could make sense to have the tripwire be included in the 
&gt;&gt; block via the coinbase witness commitment output, rather than having it be 
&gt;&gt; locked to a transaction, so you only having to check the coinbase for the 
&gt;&gt; magic rather than every transaction. That would require a separate P2P 
&gt;&gt; message to relay the necessary ECDL-break proof to miners, and would 
&gt;&gt; probably need stratumv2 or a getblocktemplate update in order for the node 
&gt;&gt; to be able to tell pools to actually include that info in the coinbase.
&gt;&gt; &gt;
&gt;&gt; &gt; I worry this is untestable, really. You&#39;d need things like 
&gt;&gt; &gt; fake-tripwires to be supported through the same message which don&#39;t 
&gt;&gt; &gt; require an ECDLP break, and still propagate. And then that needs DoS 
&gt;&gt; &gt; protection measures, 
&gt;&gt;
&gt;&gt; I whipped something up last weekend:
&gt;&gt; <a
href="https://github.com/Sjors/bitcoin/pull/121">https://github.com/Sjors/bitcoin/pull/121</a>
&gt;&gt;
&gt;&gt; It seems straightforward, but maybe I missed something:
&gt;&gt; - for test code we use a fake NUMS point, so we can generate &#34;proof&#34; 
&gt;&gt; without a quantum computer
&gt;&gt; - a p2p message floods the proof
&gt;&gt; - nodes ignore the message if they already have *any* valid proof
&gt;&gt; - verifying p2p proof candidates might need some rate limiting, but it&#39;s 
&gt;&gt; as cheap as verifying a transaction signature
&gt;&gt; - mining code includes the proof in a coinbase op_return, until the 
&gt;&gt; freeze activates
&gt;&gt;   - with stratum v2 (and ipc mining clients in general this works out of 
&gt;&gt; the box, a small change is needed for getblocktemplate clients)
&gt;&gt; - since the proof is not in the header, we can&#39;t use the normal bip9 
&gt;&gt; style header scan to see if the rule activated. Instead the prototype 
&gt;&gt; stores it in a file along with a merkle inclusion proof, which is read when 
&gt;&gt; the node restarts.
&gt;&gt;
&gt;&gt; With this mechanism it doesn&#39;t really need to be in the coinbase 
&gt;&gt; transaction, but that does seem more convenient and miners can censor it 
&gt;&gt; anyway.
&gt;&gt;
&gt;&gt; - Sjors
&gt;&gt;
&gt;&gt; -- 
&gt;&gt; You received this message because you are subscribed to a topic in the 
&gt;&gt; Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt;&gt; To unsubscribe from this topic, visit 
&gt;&gt; <a
href="https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe">https://groups.google.com/d/topic/bitcoindev/aWYtPLVPZ3U/unsubscribe</a>.
&gt;&gt; To unsubscribe from this group and all its topics, send an email to 
&gt;&gt; bitcoindev+...@googlegroups&#8226;com.
&gt;&gt; To view this discussion visit 
&gt;&gt; <a
href="https://groups.google.com/d/msgid/bitcoindev/002f2395-7d5d-4cb6-852c-e991aa1f0eb3%40app.fastmail.com">https://groups.google.com/d/msgid/bitcoindev/002f2395-7d5d-4cb6-852c-e991aa1f0eb3%40app.fastmail.com</a>
&gt;&gt; .
&gt;&gt;
&gt;
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can%40googlegroups.com">https://groups.google.com/d/msgid/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can%40googlegroups.com</a>.

<a
href="https://gnusha.org/pi/bitcoindev/f6d78499-d551-45ea-89b1-2b9cbd52f5can@googlegroups.com/1.2-a.bin">[-- Attachment #1.2: Type: text/html, Size: 13364 bytes --]</a>
</pre></div></content></entry><entry><author><name>&#39;conduition&#39; via Bitcoin Development Mailing List</name><email>bitcoindev@googlegroups.com</email></author><title>Re: [bitcoindev] The game-theory problems of PQ sunsetting modes</title><updated>2026-08-11T14:56:30Z</updated><link
href="https://gnusha.org/pi/bitcoindev/JyKb0LwJfIGSwrbg-Gj5AUDYFHT1vtcYsug27Plxe6h0gk4zAjTK393yF6mf_a2jLSiGuJRrTnNB7tg3SbCrpIPXSa71pcE9u_RaUuApr4U=@proton.me/"/><id>urn:uuid:7a1325ca-c566-beb6-2e18-e812ce748fa5</id><thr:in-reply-to
ref="urn:uuid:9a7d2a3d-fb47-ecfd-d91d-ff4c5498dd3d"
href="https://gnusha.org/pi/bitcoindev/CA+7C+cbivnG0a5k1+twRbdfR205QLieH1+mrhdDx9cw9eZ6Vxw@mail.gmail.com/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/JyKb0LwJfIGSwrbg-Gj5AUDYFHT1vtcYsug27Plxe6h0gk4zAjTK393yF6mf_a2jLSiGuJRrTnNB7tg3SbCrpIPXSa71pcE9u_RaUuApr4U=@proton.me/1.1.1-a.txt">[-- Attachment #1.1.1: Type: text/plain, Size: 26763 bytes --]</a>

<span
class="q">&gt; It will run for 9-12 days according to my calculations.
</span>


Can you show us these calculations?


<span
class="q">&gt; The CCP publicly stated that they must destroy Bitcoin in order to survive as a country, on the evening news.
</span>

Do you have a source on this claim?


<span
class="q">&gt; Drain the side chain of their coins ...
</span>
<span
class="q">&gt; The next target would likely not be Bitcoin or any side chains of Bitcoin, but Ethereum.
</span>


I&#39;m not sure if that&#39;d be a wise idea, since sidechains and altcoins like Ethereum are more likely to hard fork to undo an attack:&#160;<a
href="https://ethresear.ch/t/how-to-hard-fork-to-save-most-users-funds-in-a-quantum-emergency/18901">https://ethresear.ch/t/how-to-hard-fork-to-save-most-users-funds-in-a-quantum-emergency/18901</a>


Quantum attackers would want plausible deniability, but also finality (no backsies). Otherwise the attack is pointless.


regards,
conduition
On Monday, July 27th, 2026 at 9:50 AM, Ian Quantum &lt;ianquantum2027@gmail&#8226;com&gt; wrote:

<span
class="q">&gt; The first cryptographically relevant quantum computers are likely to be slow, especially if they are neutral atom, trapped ion or some of the NV Diamond variants depending on the speed of the computation and stability of the qubits. Realizing the quantum attacks are going to be a surprise, my game theory approach is different. Quantum Physicists will not suddenly decide to become hackers and start attacking banking networks while living in the USA, EU or China. Chinese strategy as I see it will be covered separately, below.
&gt; Quantum Physics will not offer new near term gains in mining, as Pierre-Luc explained. Attacks against Bitcoin are broken into short and long windows of opportunity. Since the first quantum computer to break Bitcoin will likely be a long window, slow attack neutral atom I will give some more general information. It will run for 9-12 days according to my calculations. With tricks, they currently have a run window that permits an attack. With qubit reuse the attack is a function of time, not the size of the machine assuming it has more than 2000 qubits of operational space. The attacks can be squeezed in under 900 qubits, but the runtime grows to match. The optimal strategy would be full width for a single key break, then switching to running multiple keys concurrently on one machine as soon as funds are available for more qubits. Attack round 2 would likely break 4-100 keys at a time, operating against a single equation like secp256k1, secp256r1, ed25519, x25519, etc. Switching equations is just a change to the python in linux. Adding more physical qubits allows attacking more keys in parallel for the same steps and time (but a little extra bookkeeping). Attacking RSA2048 keys will be 1-3 years after the first secp256k1 break unless it is PSI Quantum in late 2027 and they hit their milestone target.
&gt; 
</span>
<span
class="q">&gt; The long window attack will eventually be surpassed by the short window attack, coming from photonics or superconductors. There are some obscure (not mainstream) fast operations possible on trapped ion and NV Diamond quantum computers. When the short window CRQC comes into play, the runtime will be in minutes but still parallel execution for a small qubit cost and no time cost. 10 private keys in 10-70 minutes would be the target. This is scheduled for 2028 by PSI Quantum, but I hope that they are simply &#34;under retainer&#34; by the NSA and not able to publicly demonstrate their capabilities. PSI Q has already demonstrated qubit reuse, they have already mass produced hundreds of thousands of qubits in horizontally scaling systems. If they start off cracking a single private key, they can switch to breaking 2, then 4 just by continuing mass production and installation.
&gt; 
</span>
<span
class="q">&gt; A strategic CRQC operator would select their first target as one with low reputation and questionable security. Drain the side chain of their coins and don&#39;t touch Satoshi&#39;s Shield or any tripwire transactions. To further increase deniability, the stalwart quantum physicists may decide to launder the gains in the same way that people from North Korea or Iran does. A few hundred million dollars is a likely early target.
&gt; The next target would likely not be Bitcoin or any side chains of Bitcoin, but Ethereum. The public keys are 100% exposed in DeFi. Physicists have urged upgrading prior to 2024 and the upgrades will likely arrive too little, too late. Pocket another $100 billion, ideally with continued plausible deniability.
&gt; 
</span>
<span
class="q">&gt; At this point the quantum attacker could spend 5-15% of the gains and simply purchase the ASIC manufacturer outright. This would allow them to again operate with plausible deniability. Get hired by the company after the purchase. Work on something fun. Now that the quantum achievement has been completed. The purchase of 1-2 ASIC manufacturers would allow them to simply own the hash rate, with any generational improvement. They could choose to sell machines after they have been eclipsed by newer hash rates.
&gt; 
</span>
<span
class="q">&gt; 
</span>
<span
class="q">&gt; China has a different goal. The CCP publicly stated that they must destroy Bitcoin in order to survive as a country, on the evening news. Currently 1/3 of China&#39;s GDP is leaving the country each year and Bitcoin is the most efficient method to do so. Tron and Tether are face value, but Bitcoin is easy to send money overseas. Use Yuan to buy mining equipment, sell Bitcoin for EU or USD. This is done at a profit, while art sales and Tether are done at a significant or small loss respectively. China&#39;s Middle Class faces export controls on sending money overseas, international banking is extremely limited and total control is the CCP bare minimum standard.
&gt; 
</span>
<span
class="q">&gt; 
</span>
<span
class="q">&gt; Against this backdrop, China has thrown millions of dollars at dozens of companies to create a huge number of quantum computers racing to be the first to break Bitcoin. Bitcoin is the stated goal. Destroying Bitcoin as a store of value is the government strategy. Rapid sales of any known public keys will commence ASAP, and CRCQ will be mass produced. So their likely runtime would be targeting Satoshi&#39;s Shield, getting 50 BTC per break. If they can catch exchange funds &#34;proof of reserves&#34; then they will topple most of the economic value. 6.9 million BTC to target. They might trigger a tripwire, the goal is to dump the market and the exchanges.
&gt; 
</span>
<span
class="q">&gt; I suspect the CCP will target Ethereum in order to cause critical damage to the US economy, especially as stablecoins and CBDC have jumped in. Bitcoin sales would allow them to pay down a small portion of their debt. Ethereum sales would allow China to supersede the USA as the dominant economy. As I have said publicly, the strategy is much different depending on the threat actor who gets the first and who gets the fast CRQC.
&gt; 
</span>
<span
class="q">&gt; The game theory for each threat actor is different:
&gt; US Individual: plausible deniability, stealth, money laundering.
&gt; US Company: salvage laws, plausible deniability, can not have govt funding and target US companies like Blackrock, (micro)Strategy, Coinbase, etc.
&gt; EU Company: ideologically driven, might break a few accounts for retirement but not touch most public keys.
&gt; China: must crash all crypto to survive. If they can destroy Bitcoin, mining and pay down debt, great. If they can use this to &#39;break the hegemonic order&#39; they will definitely do so.
&gt; 
</span>
<span
class="q">&gt; I would be happy to discuss here or on Signal.
&gt; 
</span>
<span
class="q">&gt; On Mon, Jul 27, 2026 at 1:53&#8239;AM Antoine Riard &lt;antoine.riard@gmail&#8226;com&gt; wrote:
&gt; 
</span>
<span
class="q">&gt; &gt; Hello Conduition,
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Solid analysis Antoine. However things play out here, activating a PQ sunset fork of any kind while in the company of a CRQC is apparently quite hard to do right without setting the incentives up such that they sabotage the whole effort.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; That&#39;s the insight that my post aims to underscore, effectively
&gt; &gt; that activating a PQ sunset fork of any kind might be very hard
&gt; &gt; in the presence of one or more company with a CQRC, at the very
&gt; &gt; least there is a lot of uncertainty due to the incentives.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; You&#39;re correct that the problem appears as soon as you have a
&gt; &gt; company with one CRQC, where it can just go really deep in the
&gt; &gt; history of the chain. As soon as you start to have two CRQC,
&gt; &gt; there is an advantage to burn more EC coins in fees, to reorg to
&gt; &gt; your advantage, so we&#39;re back with some notion of chain finality.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; See more comments on rough ideas to alleviate the issue.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Very neat observation. For such a rollback to occur, the miners would have to cooperatively elect to stop mining the more mature (&#34;authentic&#34;) chain, where users have already migrated/forked, and instead start mining on an old block (the &#34;revisionist&#34; chain). Any resources they spend on this mining will have no payoff until the cumulative proof-of-work of the revisionist chain surpasses that of the authentic chain. Until then, honest validator nodes will simply sit idle.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Roughly in what you&#39;re describing yes. If you&#39;re a miner, I think
&gt; &gt; you can play even more sneaky chain games on what you&#39;re mentioning
&gt; &gt; about ressources. Let&#39;s say you&#39;re gaining &#34;coins&#34; on the &#34;authentic&#34;
&gt; &gt; chain, and after the 100 blocks maturity rule, you immediately short
&gt; &gt; them on the market to reinvest your proceedings in the energy cost of
&gt; &gt; the &#34;revisionist&#34; chain (or do a mining halt, as not mining might give
&gt; &gt; an advantage to the &#34;revisionist&#34; chain).
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; You&#39;re a miner, if the &#34;authentic&#34; chain wins, that&#39;s fine you&#39;re
&gt; &gt; already re-sell the matured coin. If the &#34;revisionist&#34; chain wins,
&gt; &gt; you got new fresh coinbase on the &#34;revisionist&#34; chain i.e a double-spend,
&gt; &gt; plus any CQRC &#34;bounty&#34; coming from the exploited coins.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; I think there is some &#34;mining silent reorg&#34; advantage here.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Due to the vast incentive towards colluding with the CRQC, maybe this would be feasible for some large miners?
&gt; &gt; &gt;
&gt; &gt; &gt; This would essentially be a massive double-spend attack as well, since miners who successfully roll back the blockchain in this way would be reorging their own mining earnings out of existence, some of which they presumably sold (on the authentic chain) to pay for electricity. This might make the exchanges they sold the coins to extremely unhappy: The miners are effectively retconning their own deposits.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; See my point above, they&#39;re only limited by the 100 block maturity rules.
&gt; &gt; Yes, miners would start to be unable to settle &#34;fresh&#34; coins, but also &#34;old&#34;
&gt; &gt; coins (both EC and PQ), as they are at risk of being roll back (at least for
&gt; &gt; the ones who are weeks recent).
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; For this to happen, miners must be able to withstand significant capex (on mining a revisionist chain), while being blackballed by exchanges, and possibly also devaluing the very coins they were bribed with by the CRQC. And even then, it&#39;s not clear how - assuming they were able to pull the attack off and remain solvent - the miners would actually use the ill-gotten coins, and whether they&#39;d have any value on the other side of a successful deep reorg attack.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; One of the point of the analysis, they might be able to fund their capex, with
&gt; &gt; the exploited coins, if they can get liquidity for them on the exchanges. On the
&gt; &gt; other hand, as long as they&#39;re economically solvent, they can keep the EC-exploited
&gt; &gt; coins, until some far future, when the market price them at an interesting price
&gt; &gt; enough, and slowly and covertly sell them out of their balance sheet by then.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Still, for shallow reorgs (a few blocks) this seems like a worthwhile concern that seriously hampers any tripwire attempts. The best case is if we can deploy the EC disabling fork before such tempting incentives enter the field of play.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; A naive tripwire (there might be more secure design worthy to think more about it),
&gt; &gt; of course sounds it will be always at risk of being keep out of the chain by miners.
&gt; &gt; Even the &#34;we move fast and try to disable EC&#34;, assuming it&#39;s philosophically acceptable
&gt; &gt; by the community, and I&#39;m among the one disagreeing to do so, as I pointed out in my
&gt; &gt; previous post, the stack of &#34;lost&#34; EC coins might be worth 10 years of bitcoins, that&#39;s
&gt; &gt; a lot of reorg budget.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; So in the hypothesis, you have a &#34;sunset&#34; activation, then 3 months after a CRQC
&gt; &gt; getting out of the box, there is a lot of incentives uncertainty. Even worst, there
&gt; &gt; is even a &#34;Lorentz effect&#34;, where the public and well-known &#34;sunset&#34; activation,
&gt; &gt; incentives &#34;advanced adversaries&#34; to reveal the CRQC they were keeping sleeping
&gt; &gt; in the backyard, as they know after the activation the cost structure is altered.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; I&#39;m thinking there are other solutions that we have not explored yet such as
&gt; &gt; PQ-blessed periodic checkpoints. E.g, let&#39;s say that every month, by consensus
&gt; &gt; rule, there is a checkpoint published that needs to be finalized e.g being
&gt; &gt; signed by more than % of PQ-safe pubkeys (e.g %1 of the overall coins).
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; As those pubkeys are PQ-safe, they cannot be forged by a CRQC, and a mining
&gt; &gt; coalition would not be able to go deeper than this checkpoint height, capping
&gt; &gt; up the maximum of EC-unsafe coins that could be used as reorg budget. Of course,
&gt; &gt; that would ask for a number of stakeholders in the ecosystem to have online keys
&gt; &gt; for the &#34;checkpoint&#34; finalization, though that % can be kept low [0] [1].
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; It&#39;s just a &#34;rough idea&#34;, as somehow it&#39;s re-introducing a form of checkpoint
&gt; &gt; (which is meehhhh...but not worse than the sun setting ideas imho). I think there
&gt; &gt; are more imaginative ideas that we can come up on the design table to alleviate
&gt; &gt; the risk of a CQRC acting in coordination with a mining coalition.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Notwithstanding the ultimate direction taken, the first primitive that
&gt; &gt; would need it to give us more design flexibility would be the PQ-safe signing
&gt; &gt; algorithm, be it Falcon, SkiSign or whatever.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Best,
&gt; &gt; Antoine
&gt; &gt; OTS hash: bdb435e6c81eb762bb6a12a03e2c23a83396a3481b8894af79732c2e2b569682
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; [0] This also let the door open for a EC coins owner, of which the pubkey
&gt; &gt; has not been revealed e.g P2TR to exfiltrate their old coins towards
&gt; &gt; safer one.
&gt; &gt; [1] The checkpoint would have to be carefully designed to avoid being tampered
&gt; &gt; by a miner, e.g a PQ-signed checkpoint would gain a proof-of-work bonus discount ?
&gt; &gt; I&#39;m already far in the territory of heretical consensus design ideas...
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Le dim. 19 juil. 2026 &#224; 23:02, conduition &lt;conduition@proton&#8226;me&gt; a &#233;crit :
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Solid analysis Antoine. However things play out here, activating a PQ sunset fork of any kind while in the company of a CRQC is apparently quite hard to do right without setting the incentives up such that they sabotage the whole effort.
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; If a CQRC entity is able to build a coalition with a 51% majority of miners, the &#34;upgradedPQ safe&#34; coins might be also at risk [4]. Indeed, such malicious coalition
&gt; &gt; &gt; &gt; could just roll-back the chain state back to the migration height of
&gt; &gt; &gt; &gt; said coin, solve the DL for this coin and unroll back forward the chain.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; I do not believe that the old chain history would be safe from deep
&gt; &gt; &gt; &gt; reorgs attacks by CQRC capable entities, as soft-fork deployments are
&gt; &gt; &gt; &gt; &#34;height-based&#34; burnt and not &#34;hash-based&#34; burnt (BIP90). Checkpoints
&gt; &gt; &gt; &gt; have been removed from the latest bitcoind versions. Maybe user-activated
&gt; &gt; &gt; &gt; checkpoints or other similar mechanisms might be a more robust defense
&gt; &gt; &gt; &gt; against CQRC entities attacking the chain finality.
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Very neat observation. For such a rollback to occur, the miners would have to cooperatively elect to stop mining the more mature (&#34;authentic&#34;) chain, where users have already migrated/forked, and instead start mining on an old block (the &#34;revisionist&#34; chain). Any resources they spend on this mining will have no payoff until the cumulative proof-of-work of the revisionist chain surpasses that of the authentic chain. Until then, honest validator nodes will simply sit idle.
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Due to the vast incentive towards colluding with the CRQC, maybe this would be feasible for some large miners?
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; This would essentially be a massive double-spend attack as well, since miners who successfully roll back the blockchain in this way would be reorging their own mining earnings out of existence, some of which they presumably sold (on the authentic chain) to pay for electricity. This might make the exchanges they sold the coins to extremely unhappy: The miners are effectively retconning their own deposits.
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; For this to happen, miners must be able to withstand significant capex (on mining a revisionist chain), while being blackballed by exchanges, and possibly also devaluing the very coins they were bribed with by the CRQC. And even then, it&#39;s not clear how - assuming they were able to pull the attack off and remain solvent - the miners would actually use the ill-gotten coins, and whether they&#39;d have any value on the other side of a successful deep reorg attack.
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Still, for shallow reorgs (a few blocks) this seems like a worthwhile concern that seriously hampers any tripwire attempts. The best case is if we can deploy the EC disabling fork before such tempting incentives enter the field of play.
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; regards,
&gt; &gt; &gt; conduition
&gt; &gt; &gt; On Sunday, July 12th, 2026 at 12:13 PM, Antoine Riard &lt;antoine.riard@gmail&#8226;com&gt; wrote:
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Hi list,
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; In this post, I&#39;m extending on the game-theory problems
&gt; &gt; &gt; &gt; underscored for my answer to [ ] to other post-quantum
&gt; &gt; &gt; &gt; sunsetting scenarios previously mentioned on this list.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Firstly, let&#39;s remember the &#34;tripwire&#34; idea [0]. With the
&gt; &gt; &gt; &gt; &#34;tripwire&#34;, if I understand it correctly we introduce a
&gt; &gt; &gt; &gt; consensus level proof of quantum computers e.g with a NUMS
&gt; &gt; &gt; &gt; puzzle.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; This NUMS is committed in a honeypot UTXO let&#39;s say with
&gt; &gt; &gt; &gt; some non-null bitcoin reward to unlock it. When the NUMS
&gt; &gt; &gt; &gt; point is solved by a QC entity, it automatically triggers
&gt; &gt; &gt; &gt; a &#34;freeze&#34; of all the &#34;legacy&#34; coins starting at some block
&gt; &gt; &gt; &gt; height-defined window in the future.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; While it appears feasible engineering-wise, the problem
&gt; &gt; &gt; &gt; is more on the game-theory plane of analysis. As it was
&gt; &gt; &gt; &gt; previously noted by another commentator than me [1], why
&gt; &gt; &gt; &gt; an economically-rational CRQC entity would go to trigger
&gt; &gt; &gt; &gt; such an evident &#34;honeypot&#34; UTXO depriving it from further
&gt; &gt; &gt; &gt; (covert) extractions of the legacy coins to a safe wallet
&gt; &gt; &gt; &gt; owned by this entity.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; A more sophisticated scenario, that I was laying out more
&gt; &gt; &gt; &gt; recently, a 51% majority coalition of miners could coordinate
&gt; &gt; &gt; &gt; with a CRQC entity to censor the transaction inclusion of any
&gt; &gt; &gt; &gt; PQ proof, even an inclusion attempt of a PQ proof generated by
&gt; &gt; &gt; &gt; an honest PQ entity [2].
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Exposing again the economic analysis, a year of mining income
&gt; &gt; &gt; &gt; is evaluated at around $20B. The number of legacy P2Pk coins
&gt; &gt; &gt; &gt; is evaluated to be around 1.7 M of coins or as of today $107B.
&gt; &gt; &gt; &gt; If we go to account the numbers of &#34;coin loss&#34;, the estimated
&gt; &gt; &gt; &gt; number can be more around 3-4 M, so let&#39;s say $215B worth of
&gt; &gt; &gt; &gt; target coins (a coin lost to you is not a coin lost to a CRQC
&gt; &gt; &gt; &gt; entity...).
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; That&#39;s something like ~10 years of potential income, that an
&gt; &gt; &gt; &gt; economically rational miner might not refuse if a miner has
&gt; &gt; &gt; &gt; a credible odd of capturing a share of this magic income to
&gt; &gt; &gt; &gt; the prorata of their hashrate capabilities [3].
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; If we assume a PQ coin extraction game with 2 CQRC entities
&gt; &gt; &gt; &gt; availing roughly the same capabilities, they might compete for
&gt; &gt; &gt; &gt; the majority hashrate of the miners, those miners solely driven
&gt; &gt; &gt; &gt; by economic incentives. The focal point of equilibrium between
&gt; &gt; &gt; &gt; the two strategies is likely going to be the marginal energy cost
&gt; &gt; &gt; &gt; to run a CQRC, assuming that in a fee race a CQRC entity can
&gt; &gt; &gt; &gt; offer to the majority of miners to burn more of a coin value
&gt; &gt; &gt; &gt; as reorg fee.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Secondly, for the second approach of sunsetting, the one very roughly
&gt; &gt; &gt; &gt; described in BIP361 and based on pure &#34;flag-day&#34; activation, the
&gt; &gt; &gt; &gt; security analysis can extend to this approach too. Even assuming
&gt; &gt; &gt; &gt; a week-long period for a BIP9-like activation mechanism, a coalition
&gt; &gt; &gt; &gt; of miners might stil go to reorg in depth the chain before the
&gt; &gt; &gt; &gt; activation of said soft-fork.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Such an approach is only theoretically increasing the coordination cost
&gt; &gt; &gt; &gt; (and one would observe the asymmetry of information is selecting a time
&gt; &gt; &gt; &gt; horizon period, as a CRQC might appear at any time during this period).
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; One can observe that the 2 sunsetting approach, be it &#34;tripwire&#34; or
&gt; &gt; &gt; &gt; &#34;flag-day&#34; approaches are introducing a &#34;choke point&#34; to the chain finality,
&gt; &gt; &gt; &gt; as in the lack of it a CQRC entity might covertly exfiltrate &#34;legacy&#34; coins,
&gt; &gt; &gt; &gt; with no knowledge of the miners, or even without coordination with them.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; After the &#34;choke point&#34;, a CQRC entity might alter its strategy of going
&gt; &gt; &gt; &gt; overt and start to offer fee bounties to reorg the chain as it&#39;s advantage
&gt; &gt; &gt; &gt; to the majority of miners (to not loss an exploitation advantage to another
&gt; &gt; &gt; &gt; CQRC entity).
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Finally, in this analysis we&#39;re only underscoring the risk of &#34;legacy&#34;
&gt; &gt; &gt; &gt; coins, i.e coins that would have not upgraded to a PQ safe format, after
&gt; &gt; &gt; &gt; some time horizon. However, in the Bitcoin blockchain world, time is
&gt; &gt; &gt; &gt; relative, or rather only thermodynamically convergent. If a CQRC entity
&gt; &gt; &gt; &gt; is able to build a coalition with a 51% majority of miners, the &#34;upgraded
&gt; &gt; &gt; &gt; PQ safe&#34; coins might be also at risk [4]. Indeed, such malicious coalition
&gt; &gt; &gt; &gt; could just roll-back the chain state back to the migration height of
&gt; &gt; &gt; &gt; said coin, solve the DL for this coin and unroll back forward the chain.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; I do not believe that the old chain history would be safe from deep
&gt; &gt; &gt; &gt; reorgs attacks by CQRC capable entities, as soft-fork deployments are
&gt; &gt; &gt; &gt; &#34;height-based&#34; burnt and not &#34;hash-based&#34; burnt (BIP90). Checkpoints
&gt; &gt; &gt; &gt; have been removed from the latest bitcoind versions. Maybe user-activated
&gt; &gt; &gt; &gt; checkpoints or other similar mechanisms might be a more robust defense
&gt; &gt; &gt; &gt; against CQRC entities attacking the chain finality.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Current bitcoin mining process and the chain finality is assumed to be
&gt; &gt; &gt; &gt; reasonably secure under the Gambler&#39;s Ruin Problem and some other assumptions
&gt; &gt; &gt; &gt; (e.g a reliable network to relay the blocks). It might be considered that
&gt; &gt; &gt; &gt; the introduction of CQRC computers might not be only a risk for the &#34;legacy&#34;
&gt; &gt; &gt; &gt; coins, though far more concerning for the chain finality itself.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Independently of being philosophically &#34;pro&#34; or &#34;contra&#34; in freezing
&gt; &gt; &gt; &gt; legacy coins, I do believe the irruption of one or more CQRC entities
&gt; &gt; &gt; &gt; and the potential of disruptions on the Bitcoin network stability is
&gt; &gt; &gt; &gt; a subject deserving a bit more research and more work from the development
&gt; &gt; &gt; &gt; community [5].
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Cheers,
&gt; &gt; &gt; &gt; Antoine
&gt; &gt; &gt; &gt; OTS hash: 496d9c26c6f3d805dae88f487600f46990572fc84c4ca907fb85b5441c235cf3
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; [0] <a
href="https://groups.google.com/g/bitcoindev/c/8O857bRSVV8/m/8nr6I5NIAwAJ">https://groups.google.com/g/bitcoindev/c/8O857bRSVV8/m/8nr6I5NIAwAJ</a>
&gt; &gt; &gt; &gt; [1] <a
href="https://groups.google.com/g/bitcoindev/c/8O857bRSVV8/m/7uu4dZNgAwAJ">https://groups.google.com/g/bitcoindev/c/8O857bRSVV8/m/7uu4dZNgAwAJ</a>
&gt; &gt; &gt; &gt; [2] One might consider the following realistic scenario, it
&gt; &gt; &gt; &gt; might that even if a CRQC become relevant, at first it will
&gt; &gt; &gt; &gt; be only operated by big companies let&#39;s say in the US or China
&gt; &gt; &gt; &gt; and they will prefer to keep the existence of such capabilities
&gt; &gt; &gt; &gt; hidden for a while for non-economical reasons.
&gt; &gt; &gt; &gt; Suddenly, one of the actor starts to use those post-quantum
&gt; &gt; &gt; &gt; capabilities and the social equilibrium does not hold anymore
&gt; &gt; &gt; &gt; with impactful second-order implications for the Bitcoin ecosystem.
&gt; &gt; &gt; &gt; [3] On the low time incentive miner hypothesis, one can empirically
&gt; &gt; &gt; &gt; observe (as of June &#39;26) than it has limits given how fast are ready
&gt; &gt; &gt; &gt; mainstream mining companies to reallocate their data centers and
&gt; &gt; &gt; &gt; sources of energies to more generic high-performance computations
&gt; &gt; &gt; &gt; rather than SHA256 hashing.
&gt; &gt; &gt; &gt; [4] For the degree of scientificity of &#34;game-theory&#34; in itself, I can
&gt; &gt; &gt; &gt; only forward the reader to the &#34;Formulation of the Economic Problem&#34;
&gt; &gt; &gt; &gt; chapter in the &#34;Theory of Games and Economic Behavior&#34; book from Von
&gt; &gt; &gt; &gt; Neumann &#38; Morgenstern, 1944
&gt; &gt; &gt; &gt; [5] As quantum raises a number of skeptical eyebrows in the community,
&gt; &gt; &gt; &gt; the first elaboration of quantum physics have been as old as the 30&#39;s,
&gt; &gt; &gt; &gt; and so far no one has got a Nobel Prize, or any other major scientific
&gt; &gt; &gt; &gt; prize to prove the physical impossibility of a large-scale quantum computer
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; --
&gt; &gt; &gt; &gt; You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt; &gt; &gt; &gt; To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
&gt; &gt; &gt; &gt; To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/CALZpt%2BFOUJF3E7YDk5xh-Cv9kxduGiuOPVK5x171%3D25C3ryJPQ%40mail.gmail.com">https://groups.google.com/d/msgid/bitcoindev/CALZpt%2BFOUJF3E7YDk5xh-Cv9kxduGiuOPVK5x171%3D25C3ryJPQ%40mail.gmail.com</a>.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; --
&gt; &gt; You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt; &gt; To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
&gt; &gt; To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/CALZpt%2BEjD5h9387diQvwtUY9nV-GFgN-Ukp9tY%3DuqBofb-w7Tg%40mail.gmail.com">https://groups.google.com/d/msgid/bitcoindev/CALZpt%2BEjD5h9387diQvwtUY9nV-GFgN-Ukp9tY%3DuqBofb-w7Tg%40mail.gmail.com</a>.
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/JyKb0LwJfIGSwrbg-Gj5AUDYFHT1vtcYsug27Plxe6h0gk4zAjTK393yF6mf_a2jLSiGuJRrTnNB7tg3SbCrpIPXSa71pcE9u_RaUuApr4U%3D%40proton.me">https://groups.google.com/d/msgid/bitcoindev/JyKb0LwJfIGSwrbg-Gj5AUDYFHT1vtcYsug27Plxe6h0gk4zAjTK393yF6mf_a2jLSiGuJRrTnNB7tg3SbCrpIPXSa71pcE9u_RaUuApr4U%3D%40proton.me</a>.

<a
href="https://gnusha.org/pi/bitcoindev/JyKb0LwJfIGSwrbg-Gj5AUDYFHT1vtcYsug27Plxe6h0gk4zAjTK393yF6mf_a2jLSiGuJRrTnNB7tg3SbCrpIPXSa71pcE9u_RaUuApr4U=@proton.me/1.1.2.1-a.bin">[-- Attachment #1.1.2.1: Type: text/html, Size: 32477 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/JyKb0LwJfIGSwrbg-Gj5AUDYFHT1vtcYsug27Plxe6h0gk4zAjTK393yF6mf_a2jLSiGuJRrTnNB7tg3SbCrpIPXSa71pcE9u_RaUuApr4U=@proton.me/1.2-a.bin">[-- Attachment #1.2: publickey - conduition@proton.me - 0x474891AD.asc --]
[-- Type: application/pgp-keys, Size: 649 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/JyKb0LwJfIGSwrbg-Gj5AUDYFHT1vtcYsug27Plxe6h0gk4zAjTK393yF6mf_a2jLSiGuJRrTnNB7tg3SbCrpIPXSa71pcE9u_RaUuApr4U=@proton.me/2-signature.asc">[-- Attachment #2: OpenPGP digital signature --]
[-- Type: application/pgp-signature, Size: 343 bytes --]</a>
</pre></div></content></entry><entry><author><name>&#39;conduition&#39; via Bitcoin Development Mailing List</name><email>bitcoindev@googlegroups.com</email></author><title>Re: [bitcoindev] Quantum Recovery Of Hashed Address Secured Coins With No Confiscatory Risk</title><updated>2026-08-11T14:56:19Z</updated><link
href="https://gnusha.org/pi/bitcoindev/EYz75GQ2aP5QVHF_l9zLm8T11xH8jU4w0WfCwzWkB1H0XTSfhdLRF0_Bb4lb7pfsIE3HrX_f9cmDpfk-tCcnAjTrKP8DoO2Pk8Bh4JFlQAs=@proton.me/"/><id>urn:uuid:4c70788d-1853-9eb2-e636-c66a64ef841d</id><thr:in-reply-to
ref="urn:uuid:87fcf0cb-6113-c4ee-c03d-0d35eef272d5"
href="https://gnusha.org/pi/bitcoindev/gJnvMBYdwA6pJzPtnsuBLrymr9Vs1xQ_xejRrEvET1Tz-FJZ6B_b5z0gaT25Fz2RG1N--cVZikyUclGDoLouOTRNVocOTn-fuBuwiyMCs54=@protonmail.com/"/><content
type="xhtml"><div
xmlns="http://www.w3.org/1999/xhtml"><pre
style="white-space:pre-wrap">
<a
href="https://gnusha.org/pi/bitcoindev/EYz75GQ2aP5QVHF_l9zLm8T11xH8jU4w0WfCwzWkB1H0XTSfhdLRF0_Bb4lb7pfsIE3HrX_f9cmDpfk-tCcnAjTrKP8DoO2Pk8Bh4JFlQAs=@proton.me/1.1.1-a.txt">[-- Attachment #1.1.1: Type: text/plain, Size: 32077 bytes --]</a>

Re-sending this (Aug 4), because I forgot to hit reply-all :P


Hey Shinobi, thanks for clarifying your OP.&#160;


<span
class="q">&gt; To deal with the xpub problem, a new set of derivation paths can be defined for each address type which is specced to only use the Electrum protocol for balancing fetching. By only using individual address queries, you avoid the disclosure of the xpub for these sets of addresses and create a path where for end users a transition can happen potentially even without their awareness. New wallet updates can simply start generating addresses using the new derivation paths and new protocol for balance fetching.
</span>


Interesting idea, and maybe it would reduce harm if adopted at scale today, but unfortunately this is only a forward-secure solution. It does not help users whose pubkeys are already exposed unless they take proactive action and move their coins, in which case why not move the coins to a PQ secure address (once those are available)?


<span
class="q">&gt; They do require proactive action, but in the event of failing to do so or losing the proofs after the deadline, the possibility of HD recovery and commit-reveal migration would cover users in that case.
</span>


As i said earlier, the issue with pre-registration protocols is: If proactive action is required, why not just move coins to a PQ-secure address, or lacking that, to one which has a decidable knowledge asymmetry, like P2TR or a hashed address? The juice doesn&#39;t seem worth the squeeze to me.

<span
class="q">&gt; I believe this combination of these recovery mechanisms can achieve 100% recovery coverage for every address type live on the network except P2PK outputs and custom bare scripts with the singular new security assumption of maintaining the secrecy of public keys
</span>


I want to be clear about the qualification on your primary claim here: We can&#39;t go back in time and assume people never reused addresses. Any changes we make to wallet standards, code, or to consensus are only forward-facing. Existing information cannot be un-leaked. At best we can hope users move coins to PQ secure addresses or at least to addresses which are recoverable via rescue protocols (i.e. hashed addresses, P2TR).

Technically you&#39;re correct, but it&#39;s important to be clear that your assumption excludes a huge (1/3)&#160;fraction of today&#39;s UTXO set from the set of &#34;covered&#34; coins. That remaining 1/3 does still stand a chance to be rescued, but just not with 100% coverage.

To summarize, we have the UTXO set we have, not the one we want, and we shall have to deal with it as it exists on Q-day: some coins will have exposed public keys and some won&#39;t. When that time rolls around, the community shall have to decide what matters more: Preserving as much of that remaining 1/3 of the UTXO set as possible, or avoiding all confiscation.

regards,
conduition


On Thursday, July 23rd, 2026 at 5:46 PM, &#39;shinobimonkey&#39; via Bitcoin Development Mailing List &lt;bitcoindev@googlegroups.com&gt; wrote:

<span
class="q">&gt; This is just a rewrite of the original message to address some of conduition&#8217;s remarks in his reply, and more concisely state the implicit assumptions of the overall idea. I just belted out the original post in a few minutes while I was buried under work, so hopefully this gets across the scope and assumptions more clearly.
&gt; 
</span>
<span
class="q">&gt; There are a number of proposed mechanisms for facilitating the recovery of coins by their legitimate owner by applying new additive encumbrances specifying a new proof of secret knowledge in addition to a signature by a private key, as well as commit-reveal schemes to allow for committing to a transaction spending vulnerable coins and requiring such a commitment to attain a certain number of blocks built upon it before the committed transaction is consensus valid.
&gt; 
</span>
<span
class="q">&gt; None of these schemes is capable of providing complete recovery coverage for all coins whose owners still possess a private key if applied blanketly to a given address type. I believe that by layering multiple recovery schemes together additively, and allowing any single one of them to meet the threshold required for spending, 100% coverage can be achieved by taking on only one new security assumption: the requirement to keep your public key/internal script paths secret.
&gt; 
</span>
<span
class="q">&gt; It should also be possible to account for the fact that most users not running their own full node are leaking master public keys to a third party backend server for balance querying.
&gt; 
</span>
<span
class="q">&gt; To deal with the xpub problem, a new set of derivation paths can be defined for each address type which is specced to only use the Electrum protocol for balancing fetching. By only using individual address queries, you avoid the disclosure of the xpub for these sets of addresses and create a path where for end users a transition can happen potentially even without their awareness. New wallet updates can simply start generating addresses using the new derivation paths and new protocol for balance fetching.
&gt; 
</span>
<span
class="q">&gt; The only complications I can see with this is out-of-box middle-ware that is being used to connect wallets to users&#8217; nodes are built around the assumption of xpubs and using Core&#8217;s internal wallet. This is almost certain to be a non-issue in the vast majority of cases as it will be a user connecting to their own node, but even in the small number of cases where a user is connecting to a third party node with such software, it can be adapted to use something like Electrum protocol. I don&#8217;t see this being a major show stopper.
&gt; 
</span>
<span
class="q">&gt; The xpub issue mitigated, now the interaction of the of different recovery mechanisms.
&gt; 
</span>
<span
class="q">&gt; Xpub derivation based recovery:
&gt; -------------------------------
&gt; 
</span>
<span
class="q">&gt; This will cover any BIP 32 based wallet, regardless of what derivation path (?) is used. So this recovery path should encompass both any address generated using legacy derivation paths with exposed public keys, as well as newer derivation paths securing them through the use of the Electrum protocol.
&gt; 
</span>
<span
class="q">&gt; For any hashed-address type (P2PKH, P2SH, P2WPKH, P2WSH) the derivation proof alone is sufficient, and as conduition pointed out in response to my initial post the internal key can additively be used to make this workable for P2TR addresses that do not use the NUMS point.
&gt; 
</span>
<span
class="q">&gt; This specifically ensures that any user with coins using these address types can produce a recovery proof without having to take any kind of proactive action before the activation of a fork implementing additive encumbrances on address types. (It&#8217;s worth noting however these proofs will be pretty big, which is relevant for stateful proofs).
&gt; 
</span>
<span
class="q">&gt; Stateful timestamped proofs
&gt; ---------------------------
&gt; 
</span>
<span
class="q">&gt; This has been pitched multiple times before I can recall but never really described in detail. Simply the basic components of a signature from the existing encumbrance condition over a new authentication mechanism (a public key for a quantum safe scheme), and a timestamp to prove that this attestation was produced before some pre-defined deadline chosen to expire before a viable quantum computer exists.
&gt; 
</span>
<span
class="q">&gt; This could be pretty simply boiled down to the 1) the signature over the new public key/authentication commitment, 2) the timestamp. Given the potential size of ZKPs, and the fact that hash-based signatures can be optimized to ~580 bytes, I think these are still worth considering looking at how much smaller and more efficient with blockspace stateful proofs can be compared to ZKPs.
&gt; 
</span>
<span
class="q">&gt; They do require proactive action, but in the event of failing to do so or losing the proofs after the deadline, the possibility of HD recovery and commit-reveal migration would cover users in that case.
&gt; 
</span>
<span
class="q">&gt; Commit-reveal migration
&gt; -----------------------
&gt; 
</span>
<span
class="q">&gt; For any hashed address type, the old commit-reveal migration scheme requiring an encrypted commitment to a transaction be confirmed in the blockchain for a pre-defined number of blocks before the plain-text transaction can be considered consensus valid. The secrecy of public keys can be maintained using the new derivation specification, but this will still be consensus valid for coins in legacy derived addresses.
&gt; 
</span>
<span
class="q">&gt; Again, as conduition pointed out in his reply to my original post, the internal key forms the basis for a secret inaccessible to an attacker, and can be applied as a requirement for P2TR keyspends as an additional validity requirement while using commit-reveal migration. Any tapscript spends using commit-reveal should work as long as those tapscript paths have never been reused with the same internal variables like public keys.
&gt; 
</span>
<span
class="q">&gt; Wrap up
&gt; -------
&gt; 
</span>
<span
class="q">&gt; So I think I&#8217;ve covered all my bases in terms of implicit assumptions and responding to conduitions comments.
&gt; 
</span>
<span
class="q">&gt; Unless I am fundamentally missing something, or have overlooked important implementation details like those conduition corrected in his replies from my initial post, I believe this combination of these recovery mechanisms can achieve 100% recovery coverage for every address type live on the network except P2PK outputs and custom bare scripts with the singular new security assumption of maintaining the secrecy of public keys (which as noted above can be accomplished with a rather painless migration behind the scenes for users and without the need to go through the process of generating a new master key and migrating funds across seeds).
&gt; 
</span>
<span
class="q">&gt; So I guess, yeah&#8230;what am I overlooking here?
&gt; 
</span>
<span
class="q">&gt; 
</span>
<span
class="q">&gt; 
</span>
<span
class="q">&gt; 
</span>
<span
class="q">&gt; Shinobi
&gt; 
</span>
<span
class="q">&gt; Sent with Proton Mail secure email.
&gt; 
</span>
<span
class="q">&gt; On Wednesday, July 15th, 2026 at 12:58 AM, &#39;conduition&#39; via Bitcoin Development Mailing List &lt;bitcoindev@googlegroups.com&gt; wrote:
&gt; 
</span>
<span
class="q">&gt; &gt; &gt; I don&#39;t see what the point of your response is here, given I specifically and explicitly state in the original post that address types revealing public keys on-chain are out of scope here, uncoverable in this way due to the proposal involving commit-reveal as an allowed mechanism.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; The words you quoted were written as a counterpoint to your claim that &#34;by layering them, and allowing any single one of them&#160;to be used, complete coverage of any conceivable key generation method can be achieved for hashed address types.&#34; My point was that your claim is not true because some coins don&#39;t have KA&#39;s (because of how their address was generated and used previously) and thus can&#39;t be rescued. I used satoshi&#39;s coins as an example but the same is true of some coins on hashed address types (see my reused paper wallet example).
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Any UTXO which does&#160;have a KA is perfectly rescuable, regardless of the type of address it sits on. It just so happens that some address types encourage more KA&#39;s than others (e.g. hashed addresses), but not all coins on such addresses will have a KA and be recoverable after Q-day rolls around. Often it&#39;s impossible to identify those cases with certainty.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Again, I don&#39;t see the point of the reply here, as this would be a completely separate recovery mechanism than the combination of these two/three specific things. These specific mechanisms layered together, and applied as an additional encumbrance only on hashed address types, ignoring P2TR and P2PK, would achieve complete coverage of any feasible key generation scheme.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; You said in your OP that &#34;Coverage of non-hashed address types is fundamentally impossible&#34;, and so you focus mostly on hashed addresses in your proposal. My point is that your claim there was wrong, that P2TR coins can&#160;be rescued because they have one or more KA&#39;s, and the text you quoted shows an example of a KA in P2TR which can be used for rescue.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; I point this out because any rescue protocol proposal should seek to cover as many UTXOs as possible (within reason), so we ought to cover P2TR coins as well if it&#39;s feasible to do so, which it clearly is.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Whether it was generated with BIP 32 or not is irrelevant if the address is reused, obviously in a quantum threat scenario address reuse is a fatal mistake.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; That&#39;s not true, it is highly relevant. If a hashed address has an EC public key exposed on-chain prior to the activation height of the rescue protocol fork, then we can mark that address as having no &#34;hashed address knowledge asymmetry&#34;, and disallow the use of that specific KA for coins on that specific address. Other KA&#39;s like BIP32 derivation would remain completely usable for rescue.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; The same thing is true of revealing your xpubs, which is just as widespread (if not moreso) of a practice. That completely undermines the KA that HD recovery proofs depend on.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; Also not true. Revealing your account-level (i.e. `m/44&#39;/0&#39;/0&#39;`) xpub does not give a quantum adversary any information about the extended key at the coin-level (i.e. `m/44&#39;/0&#39;`). Wallets typically never share these keys, even in complex multisig setups. The hardened derivation of the account-level xpriv key (at `m/44&#39;/0&#39;/0&#39;`) is exactly the quantum hard relation that the BIP32 KA relies upon, and knowing the account-level xpriv doesn&#39;t give you any help in deriving it from the coin-level parent key. I&#39;d encourage you to revisit Laolu&#39;s thread on the ML and you&#39;ll see this is exactly what his best ZKP benchmark does.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; However, revealing your xpub does&#160;give a CRQC the ability to forge the hashed-address KA proof, because they can re-derive the hidden public key, crack it, and forge a signature + KA-proof to steal the coins. Since xpubs are shared off-chain, validator nodes won&#39;t know that they should disable the hashed-address KA for children of the exposed xpub. So there is some meat to the argument that we ought not to allow hashed address KA&#39;s at all, because they would encourage selling of xpubs to CRQCs and enable more theft than would otherwise be possible. I&#39;m personally still undecided on this problem.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; I don&#39;t see how this is a useful response or criticism, unless you also want to apply the same degree of criticism to HD recovery proofs in general as well.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; I&#39;m not trying to criticize you or your proposal, other than by correcting false statements. I&#39;m sorry if my prior reply was confusing, I can write a bit indirectly at times.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; The general idea of layering different KA&#39;s is excellent, and I fully support it. But it&#39;s also important we be accurate about which coins can and can&#39;t be rescued, as this is a very important factor which ML readers will use to weigh the pros/cons of supporting or rejecting a rescue protocol soft-fork, and as i said earlier, misconceptions abound here.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; The most common misconception I see in this field of research is that people think too much about the proving mechanism and not enough about the knowledge asymmetries and hard relations. The exact tooling used to prove &#38; authenticate KA&#39;s (ZKPs, commit/reveal, etc) should IMO be decoupled from the discussion of which coins can/can&#39;t be rescued. Pretty much any KA you can authenticate with a ZKP can be authenticated with commit/reveal, and vice-versa.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; So there should really be two discussions:
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 1.  Which knowledge asymmetries should be allowed for rescue?
&gt; &gt; 2.  Which proving system should we use to authenticate knowledge asymmetries?
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; On the subject of (1), I parsed the point of your OP roughly as &#34;more is better&#34; when it comes to KA&#39;s, and mostly I agree. Unfortunately we can&#39;t recover every UTXO, even if you scope it strictly to certain address types as you do. There will always be confiscation with rescue protocols, unless you limit yourself only to KA&#39;s whose existence can be checked on-chain, like the hashed address KA, leaving all other addresses untouched, which IMO is a bad plan because we&#39;ll have poor practical results (1/3 of the supply remains to be siezed or frozen).
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; On (2), I think you may have some misunderstandings about how commit/reveal works, because you claimed commit/reveal is not useful for proving KA&#39;s in non-hashed address types, which is incorrect: Commit/reveal can prove any KA for any UTXO just as well as ZKPs, no matter what address type the coins sit on.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; regards,
&gt; &gt; conduition
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; 
</span>
<span
class="q">&gt; &gt; On Tuesday, July 14th, 2026 at 6:29 PM, shinobimonkey &lt;shinobius_monk@protonmail&#8226;com&gt; wrote:
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; -   No matter what tool we use to authenticate KA&#39;s, there will exist some UTXOs which have no knowledge asymmetries on Q-day.&#160;I suspect Satoshi&#39;s coins are chief among them, since they are stored on P2PK addresses generated by Bitcoin Core&#39;s old JBOK wallet system.
&gt; &gt; &gt;     
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; I don&#39;t see what the point of your response is here, given I specifically and explicitly state in the original post that address types revealing public keys on-chain are out of scope here, uncoverable in this way due to the proposal involving commit-reveal as an allowed mechanism. The whole point of this proposal of these three&#160;(or as you pointed out validly, just the ZKP + commit/reveal would achieve the same coverage and the stateful proofs is redundant)&#160;specific mechanisms is that they can be applied only to hashed address types, leaving P2TR and P2PK as a separate matter.&#160;&#160;
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; -   Not true. P2TR UTXOs can be rescued using internal keys as a KA, which are essentially preimages hidden to the quantum attacker. Pick an internal pubkey&#160;`P` with output key&#160;`P&#39; = P + H(P) * G`, and give&#160;`P&#39;` to the CRQC. Though they can factor&#160;`P&#39;`, they cannot guess&#160;`P`&#160;other than by brute-force (or Grover&#39;s search).
&gt; &gt; &gt;     
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Again, I don&#39;t see the point of the reply here, as this would be a completely separate recovery mechanism than the combination of these two/three specific things. These specific mechanisms layered together, and applied as an additional encumbrance only on hashed address types, ignoring P2TR and P2PK, would achieve complete coverage of any feasible key generation scheme.&#160;
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; -   It is still possible to have a UTXO on a hashed address which contains no KA.&#160;Consider a paper wallet, generated randomly (not from BIP32), which has already been spent from previously and so has an EC pubkey exposed on chain.
&gt; &gt; &gt;     
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Whether it was generated with BIP 32 or not is irrelevant if the address is reused, obviously in a quantum threat scenario address reuse is a fatal mistake. The same thing is true of revealing your xpubs, which is just as widespread (if not moreso) of a practice. That completely undermines the KA that HD recovery proofs depend on. I don&#39;t see how this is a useful response or criticism, unless you also want to apply the same degree of criticism to HD recovery proofs in general as well.&#160;
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Preparing for a post quantum Bitcoin will require lots of ancillary hygiene practice changes and tightening up when it comes to managing data like that if we don&#39;t want these type of preparatory schemes to be undermined by poor practices.&#160;&#160;
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Accepting this reality, and only applying these three (or I guess two) additional recovery encumbrances to hashed address types (i.e. not P2PK and P2TR), any user should be able to recover all of their hashed address secured coins in all situations except key loss or address reuse (and this is ultimately not special to this proposal, any recovery or preparatory scheme to deal with quantum short of just giving users a new address type and them outright migrating will require that users begin to treat and handle public key material differently for it to work).
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Shinobi
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; Sent with Proton Mail secure email.
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; On Tuesday, July 14th, 2026 at 4:38 PM, conduition &lt;conduition@proton&#8226;me&gt; wrote:
&gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Hi Shinobi,&#160;
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Thanks for raising this item. It&#39;s a heavily contentious subject with a lot of misinformation flying around.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Before we even think about rescue protocols like ZKPs, pre-registration, or commit/reveal, it is important to understand what a rescue protocol even does. So let me first define another term: Knowledge Asymmetry.&#160;
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; In this context, a knowledge asymmetry (or KA for short) is a witness to a quantum-hard relation that has been committed on-chain before Q-day. In plain words, a KA is some piece of high-entropy information which an honest coin-holder knows, but which a future CRQC will not know and cannot easily compute or guess.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Examples of knowledge asymmetries include:
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; -   BIP32 parent keys and chain codes (this is what Lalu used in his RISC0 benchmarks)
&gt; &gt; &gt; &gt; -   EC keys hidden behind a hash, e.g.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; -   Hashed address types which haven&#39;t been spent from
&gt; &gt; &gt; &gt; -   MuSig peer keys
&gt; &gt; &gt; &gt; -   Taproot internal keys
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; -   Pre-registered commitments&#160;
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; KA&#39;s are distinct from private keys because currently there exists no standardized means to authenticate oneself using these KA&#39;s in consensus, and because KA&#39;s are not always perfectly private (e.g. hashed public keys).&#160;
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; The rescue protocols you cite as examples are all merely different ways to modify consensus so that KA&#39;s can be used to rescue coins that don&#39;t move onto explicitly quantum-safe addresses in time.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; -   Lalu&#39;s ZK-STARK benchmarks show how to authenticate a BIP32 KA using the RISC0 STARK prover, but generally a ZKP can prove any computation, and allows fast verification.&#160;
&gt; &gt; &gt; &gt; -   Commit/reveal strategies can prove any KA that can be verified by publishing a witness (e.g. by publishing a preimage and recomputing its hash, in the case of hashed addresses, but it&#39;s more general than that).
&gt; &gt; &gt; &gt; -   Pre-registration is a way to create new KA&#39;s where they may not already exist (e.g. for exposed-pubkey JBOK wallets), under the assumption we will introduce a way to authenticate those KA&#39;s later.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Pre-registration is a bit of a red-herring in my view. If a user can pre-register to create a new KA, why not simply move to a quantum-safe address? Or move to any standard BIP32 wallet or hashed address, where known KA&#39;s abound?&#160;So i will discount pre-registration as a rescue scheme for now because it seems excessively complex and redundant.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; The other two, ZKPs and commit/reveal, are far more interesting as they let us authenticate existing KA&#39;s present on Bitcoin UTXOs, such as BIP32 keys or hashed addresses. Both have their trade-offs.&#160;
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; The more relevant fact to consider in regards to your OP is: No matter what tool we use to authenticate KA&#39;s, there will exist some UTXOs which have no knowledge asymmetries on Q-day. I suspect Satoshi&#39;s coins are chief among them, since they are stored on P2PK addresses generated by Bitcoin Core&#39;s old JBOK wallet system.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; We could theoretically partition the set of all Bitcoin UTXOs into two subsets: Those with KA&#39;s, and those without. I like to call these the &#34;recoverable&#34; and &#34;unrecoverable&#34; sets of UTXOs.&#160;
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; The unrecoverable set unfortunately cannot be rescued from a QC, no matter what rescue protocol we devise, because there exists no provable mathematical distinction between the honest user and the future CRQC. The only route left there is KYC or &#34;trusted salvage&#34; by a CRQC.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; For the recoverable set (those with KA&#39;s), we can further classify them based on the types of KA available to each UTXO: some UTXOs have multiple KA&#39;s.&#160;
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; However, these sets all have unknown size and volume because - with the exception of hashed addresses - it&#39;s hard to tell at a glance which KA&#39;s a particular address has available. This makes it hard to justify what KA&#39;s to prioritize authenticating, so we kinda just have to go by dead-reckoning.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; With this in mind, I would like to correct a few statements in your OP:
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; However, by layering them, and allowing any single one of them&#160;to be used, complete coverage of any conceivable key generation method can be achieved for hashed address types.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; It is still possible to have a UTXO on a hashed address which contains no KA. Consider a paper wallet, generated randomly (not from BIP32), which has already been spent from previously and so has an EC pubkey exposed on chain. Unless a new KA is introduced (by moving coins or pre-registration), no rescue protocol can save this UTXO: it will either be stolen or frozen.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; Coverage of non-hashed address types is fundamentally impossible, because the requirement to allow use of commit-reveal migration would inherently leave such address types still exposed to a quantum attacker.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; Not true. P2TR UTXOs can be rescued using internal keys as a KA, which are essentially preimages hidden to the quantum attacker. Pick an internal pubkey `P` with output key `P&#39; = P + H(P) * G`, and give `P&#39;` to the CRQC. Though they can factor `P&#39;`, they cannot guess `P`&#160;other than by brute-force (or Grover&#39;s search).
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; By default most P2TR software generates the output key with a hidden internal key in this way even if no scripts are present (example), and this is standardized in BIP86 so I believe most P2TR wallets have a KA and so can be rescued. Even if they didn&#39;t have an internal key, any P2TR address can use BIP32 as a KA since most P2TR addresses are derived from an HD wallet.&#160;
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; The same would apply to any P2PK key generated using hashes, though I think these would be very rare.
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; regards,
&gt; &gt; &gt; &gt; conduition
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; On Tuesday, July 14th, 2026 at 9:44 AM, &#39;shinobimonkey&#39; via Bitcoin Development Mailing List &lt;bitcoindev@googlegroups.com&gt; wrote:
&gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; Currently the discussion around how to address the potential risk of a viable quantum computer centers around two primary issues: the quantum-safe signature schemes (or schemes) to integrate for users to migrate to and use if need be, and what (if anything) to do about any coins that remain secured by vulnerable ECC based scripts, specifically should these coins be frozen, and what mechanisms are available to allow legitimate owners to recover those coins if possible without an attacker having the ability to do so.&#160;
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; This second issue is (and always has been) a very socially contentious one, as the common understanding is it is impossible to guarantee with certainty that no user is being left in a position where they are incapable of generating a recovery proof, and therefore are forever prevented from accessing their coins.&#160;
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; My motivation for writing this is to solve this contention (at least partially) in a manner that can hopefully move discussions forward in a productive direction rather than lead to two opposing plans of action eventually colliding in the real world with live implementations of conflicting rules.&#160;
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; The current solution landscape as it stands to my understanding is:&#160;
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; -   BIP 32 hierarchical proofs, as proposed a decade or so ago by Adam Back and recently implemented as a proof-of-concept by roasbeef.&#160;
&gt; &gt; &gt; &gt; &gt; -   Non-deterministic stateful proofs constructed and timestamped before a deadline, showing a vulnerable ECC key signing off on a quantum-safe authentication mechanism to be used for spending after a post-quantum spending restriction is activated
&gt; &gt; &gt; &gt; &gt; -   Tim Ruffing/Tadge Dryja&#39;s idea (I apologize, but I forget who was the actual originator of the proposal) of a commit-reveal migration scheme where a transaction spending vulnerable ECC inputs must&#160;have an encrypted commitment to that exact transaction confirmed in a block with a pre-determined number of confirmations prior to the decrypted plaintext transaction&#39;s confirmation, or the decrypted transaction is invalid.&#160;
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; All three of these proposals leave some subset of coins uncovered. HD proofs are useless for users who generated their keys any other way than BIP 32, stateful timestamped proofs are useless for any inactive user or someone who for any reason does not create them before the creation deadline, and the commit-reveal migration is useless for anyone with an address type that isn&#39;t hashed because any attacker would have access to the material needed to create a valid pre-commitment for a spend.&#160;
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; However, by layering them, and allowing any single one of them&#160;to be used, complete coverage of any conceivable key generation method can be achieved for hashed address types. Coverage of non-hashed address types is fundamentally impossible, because the requirement to allow use of commit-reveal migration would inherently leave such address types still exposed to a quantum attacker.&#160;
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; -   Hierarchical proofs cover any BIP 32 user
&gt; &gt; &gt; &gt; &gt; -   Stateful timestamped proofs cover any active/observant non-BIP 32 user
&gt; &gt; &gt; &gt; &gt; -   Commit-reveal covers any non-BIP 32 user who is inactive/not observant&#160;
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; The only case in which I can see a restriction of hashed address type spends using this layered approach of recovery would leave a user unable to recover their coins is if they have lost access to their private keys. That case is completely outside of the scope of any of these proposals, and inherently impossible to cover.&#160;
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; Shinobi
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; Sent with Proton Mail secure email.
&gt; &gt; &gt; &gt; &gt; 
</span>
<span
class="q">&gt; &gt; &gt; &gt; &gt; --
&gt; &gt; &gt; &gt; &gt; You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt; &gt; &gt; &gt; &gt; To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
&gt; &gt; &gt; &gt; &gt; To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/sdGGYMMWowlFff6Yh8usMel61HVYmV8KPMqT9np2kK7GxPbVaogJ2aJSFe4v16VNLef4eDwNgfReiK-7j-sYn1jlXHPoAPWAwNBbSJxEz3M%3D%40protonmail.com">https://groups.google.com/d/msgid/bitcoindev/sdGGYMMWowlFff6Yh8usMel61HVYmV8KPMqT9np2kK7GxPbVaogJ2aJSFe4v16VNLef4eDwNgfReiK-7j-sYn1jlXHPoAPWAwNBbSJxEz3M%3D%40protonmail.com</a>.
&gt; &gt; 
</span>
<span
class="q">&gt; &gt; --
&gt; &gt; You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt; &gt; To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
&gt; &gt; To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/XeI-rNO4AO9UCO-CL4K8scZ8VZjc_5ctaY4sw98wepKsOgEQkpExB8eagrO_TqplOUpt9WERYxitzsoCaIjoz99M9mfrrIYMKkdMij1_Pls%3D%40proton.me">https://groups.google.com/d/msgid/bitcoindev/XeI-rNO4AO9UCO-CL4K8scZ8VZjc_5ctaY4sw98wepKsOgEQkpExB8eagrO_TqplOUpt9WERYxitzsoCaIjoz99M9mfrrIYMKkdMij1_Pls%3D%40proton.me</a>.
&gt; 
</span>
<span
class="q">&gt; --
&gt; You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
&gt; To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
&gt; To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/gJnvMBYdwA6pJzPtnsuBLrymr9Vs1xQ_xejRrEvET1Tz-FJZ6B_b5z0gaT25Fz2RG1N--cVZikyUclGDoLouOTRNVocOTn-fuBuwiyMCs54%3D%40protonmail.com">https://groups.google.com/d/msgid/bitcoindev/gJnvMBYdwA6pJzPtnsuBLrymr9Vs1xQ_xejRrEvET1Tz-FJZ6B_b5z0gaT25Fz2RG1N--cVZikyUclGDoLouOTRNVocOTn-fuBuwiyMCs54%3D%40protonmail.com</a>.
</span>
-- 
You received this message because you are subscribed to the Google Groups &#34;Bitcoin Development Mailing List&#34; group.
To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups&#8226;com.
To view this discussion visit <a
href="https://groups.google.com/d/msgid/bitcoindev/EYz75GQ2aP5QVHF_l9zLm8T11xH8jU4w0WfCwzWkB1H0XTSfhdLRF0_Bb4lb7pfsIE3HrX_f9cmDpfk-tCcnAjTrKP8DoO2Pk8Bh4JFlQAs%3D%40proton.me">https://groups.google.com/d/msgid/bitcoindev/EYz75GQ2aP5QVHF_l9zLm8T11xH8jU4w0WfCwzWkB1H0XTSfhdLRF0_Bb4lb7pfsIE3HrX_f9cmDpfk-tCcnAjTrKP8DoO2Pk8Bh4JFlQAs%3D%40proton.me</a>.

<a
href="https://gnusha.org/pi/bitcoindev/EYz75GQ2aP5QVHF_l9zLm8T11xH8jU4w0WfCwzWkB1H0XTSfhdLRF0_Bb4lb7pfsIE3HrX_f9cmDpfk-tCcnAjTrKP8DoO2Pk8Bh4JFlQAs=@proton.me/1.1.2.1-a.bin">[-- Attachment #1.1.2.1: Type: text/html, Size: 55688 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/EYz75GQ2aP5QVHF_l9zLm8T11xH8jU4w0WfCwzWkB1H0XTSfhdLRF0_Bb4lb7pfsIE3HrX_f9cmDpfk-tCcnAjTrKP8DoO2Pk8Bh4JFlQAs=@proton.me/1.2-a.bin">[-- Attachment #1.2: publickey - conduition@proton.me - 0x474891AD.asc --]
[-- Type: application/pgp-keys, Size: 649 bytes --]</a>

<a
href="https://gnusha.org/pi/bitcoindev/EYz75GQ2aP5QVHF_l9zLm8T11xH8jU4w0WfCwzWkB1H0XTSfhdLRF0_Bb4lb7pfsIE3HrX_f9cmDpfk-tCcnAjTrKP8DoO2Pk8Bh4JFlQAs=@proton.me/2-signature.asc">[-- Attachment #2: OpenPGP digital signature --]
[-- Type: application/pgp-signature, Size: 343 bytes --]</a>
</pre></div></content></entry></feed>
