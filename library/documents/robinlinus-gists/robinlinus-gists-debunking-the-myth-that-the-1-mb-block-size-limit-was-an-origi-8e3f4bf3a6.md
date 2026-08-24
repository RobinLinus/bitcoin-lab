# Debunking the myth that the 1 MB block-size limit was an original, permanent, sacred design constraint. / big-blocks.md

Source: https://gist.github.com/RobinLinus/d46cb202d5c25a37356332c476cac174#file-big-blocks-md

Retrieved: 2026-08-24T21:53:25Z

Extraction note: Current public gist file at revision 85f2455e4ca3558184e7b1fc42fa20e2d718d2a6.

---

````markdown
# I Like Big Blocks And I Cannot Lie

Debunking the myth that the 1 MB block-size limit was an original, permanent, sacred design constraint.

## Satoshi Quotes

> The bandwidth might not be as prohibitive as you think. A typical transaction would be about 400 bytes (ECC is nicely compact). Each transaction has to be broadcast twice, so lets say 1KB per transaction. Visa processed 37 billion transactions in FY2008, or an average of 100 million transactions per day. That many transactions would take 100GB of bandwidth, or the size of 12 DVD or 2 HD quality movies, or about $18 worth of bandwidth at current prices. [Source](https://satoshi.nakamotoinstitute.org/emails/cryptography/threads/1/)

---

> To think about what a really huge transaction load would look like, I look at the existing credit card network.  I found some more estimates about how many transactions are online purchases.  It's about 15 million tx per day for the entire e-commerce load of the Internet worldwide.  At 1KB per transaction, that would be 15GB of bandwidth for each block generating node per day, or about two DVD movies worth.  Seems do-able even with today's technology. [Source](https://mmalmi.github.io/satoshi/#:~:text=It%27s%0Aabout%2015%20million%20tx%20per%20day%20for%20the%20entire%20e%2Dcommerce%20load%20of%20the%0AInternet%20worldwide.%20%20At%201KB%20per%20transaction%2C%20that%20would%20be%2015GB%20of%0Abandwidth%20for%20each%20block%20generating%20node%20per%20day%2C%20or%20about%20two%20DVD%0Amovies%20worth.%20%20Seems%20do%2Dable%20even%20with%20today%27s%20technology.)

---
> The existing Visa credit card network processes about 15 million Internet purchases per day worldwide.  Bitcoin can already scale much larger than that with existing hardware for a fraction of the cost.  It never really hits a scale ceiling.  If you're interested, I can go over the ways it would cope with extreme size.
> 
> By Moore's Law, we can expect hardware speed to be 10 times faster in 5 years and 100 times faster in 10.  Even if Bitcoin grows at crazy adoption rates, I think computer speeds will stay ahead of the number of transactions. [Source](https://plan99.net/~mike/satoshi-emails/thread1.html?utm_source=chatgpt.com#:~:text=It%20never%20really%20hits%20a%20scale%20ceiling)



---

> The current system where every user is a network node is not the intended configuration for large scale.  That would be like every Usenet user runs their own NNTP server.  The design supports letting users just be users.  The more burden it is to run a node, the fewer nodes there will be.  Those few nodes will be big server farms.  The rest will be client nodes that only do transactions and don't generate. [Source](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/287/)

---

> A higher limit can be phased in once we have actual use closer to the limit and make sure it's working OK.
> 
> Eventually when we have client-only implementations, the block chain size won't matter much.  Until then, while all users still have to download the entire block chain to start, it's nice if we can keep it down to a reasonable size.
> 
> With very high transaction volume, network nodes would consolidate and there would be more pooled mining and GPU farms, and users would run client-only.  With dev work on optimising and parallelising, it can keep scaling up.
> 
> Whatever the current capacity of the software is, it automatically grows at the rate of Moore's Law, about 60% per year [Source](https://plan99.net/~mike/satoshi-emails/thread3.html#:~:text=A%20higher%20limit%20can%20be%20phased%20in%20once%20we%20have%20actual%20use%20closer%20to%20the%20limit%20and%20make%20sure%20it%27s%20working%20OK.) [Source](https://blog.plan99.net/the-capacity-cliff-586d1bf7715e#:~:text=A%20higher%20limit,a%20reasonable%20size.)

---

> 100,000 block generating nodes is a good ballpark large-scale size
to think about.  Propagating a transaction across the whole network
twice would consume a total of US$ 0.02 of bandwidth at today's
prices.  In practice, many would be burning off excess allocated
bandwidth or unlimited plans with one of the cheaper backbones.
There could be millions of SPV clients.  [Source](https://mmalmi.github.io/satoshi/#email-24:~:text=There%20could%20be%20millions%20of%20SPV%20clients.%20%20They%20only%20matter%20in%20how%0Amany%20transactions%20they%20generate)

---

> The fee the market would settle on should be minimal.
[Source](https://mmalmi.github.io/satoshi/#email-24:~:text=The%20fee%20the%20market%20would%20settle%20%0Aon%20should%20be%20minimal)

---

> It can be phased in, like:
> 
> if (blocknumber > 115000)
>    maxblocksize = largerlimit
>
> It can start being in versions way ahead, so by the time it reaches that block number and goes into effect, the older versions that don't have it are already obsolete.
> 
> When we're near the cutoff block number, I can put an alert to old versions to make sure they know they have to upgrade.
[Source](https://bitcointalk.org/index.php?topic=1347.msg15366#msg15366)

----

> It is possible to verify payments without running a full network node. A user only needs to keep a copy of the block headers of the longest proof-of-work chain, which he can get by querying network nodes until he's convinced he has the longest chain, and obtain the Merkle branch linking the transaction to the block it's timestamped in. He can't check the transaction for himself, but by linking it to a place in the chain, he can see that a network node has accepted it, and blocks added after it further confirm the network has accepted it. [Source](https://bitcoin.org/bitcoin.pdf)

----

> In a few decades when the reward gets too small, the transaction fee will become the main compensation for nodes.  I'm sure that in 20 years there will either be very large transaction volume or no volume. [Source](https://bitcointalk.org/index.php?topic=48.msg329#msg329:~:text=In%20a%20few%20decades%20when%20the%20reward%20gets%20too%20small)

----

> We can phase in a change later if we get closer to needing it.
[Source](https://bitcointalk.org/index.php?topic=1347.msg15139#msg15139)

---- 
> I anticipate there will never be more than 100K nodes, probably less.  It will reach an equilibrium where it's not worth it for more nodes to join in.  The rest will be lightweight clients, which could be millions. [Source](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/188/#:~:text=I%20anticipate%20there%20will%20never%20be%20more%20than%20100K%20nodes%2C%20probably%20less.%C2%A0%20It%20will%20reach%20an%20equilibrium%20where%20it%27s%20not%20worth%20it%20for%20more%20nodes%20to%20join%20in.%C2%A0%20The%20rest%20will%20be%20lightweight%20clients%2C%20which%20could%20be%20millions)

----

> The eventual solution will be to not care how big it gets.  But for now, while it's still small, it's nice to keep it small so new users can get going faster.  When I eventually implement client-only mode, that won't matter much anymore. [Source](https://satoshi.nakamotoinstitute.org/it/posts/bitcointalk/345/?utm_source=chatgpt.com#:~:text=solution%20will%20be%20to%20not%20care%20how%20big%20it%20gets)

---- 

> As things have evolved, the number of people who need to run full nodes is less than I originally imagined.  The network would be fine with a small number of nodes if processing load becomes heavy. [Source](https://plan99.net/~mike/satoshi-emails/thread3.html#:~:text=The%20network%20would%20be%20fine%20with%20a%20small%20number%20of%20nodes%20if%20processing%20load%20becomes%20heavy)


---- 

> While I don't think Bitcoin is practical for smaller micropayments right now, it will eventually be as storage and bandwidth costs continue to fall.  If Bitcoin catches on on a big scale, it may already be the case by that time.  Another way they can become more practical is if I implement client-only mode and the number of network nodes consolidates into a smaller number of professional server farms.  Whatever size micropayments you need will eventually be practical.  I think in 5 or 10 years, the bandwidth and storage will seem trivial. [Source](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/318/#:~:text=%C2%A0I%20think%20in%205%20or%2010%20years%2C%20the%20bandwidth%20and%20storage%20will%20seem%20trivial)


## Lightning Network White Paper 
> If all transactions using Bitcoin were conducted inside a network of micropayment channels, to enable 7 billion people to make two channels per year with unlimited transactions inside the channel, it would require 133 MB blocks (presuming 500 bytes per transaction and 52560 blocks per year). Current generation desktop computers will be able to run a full node with old blocks pruned out on 2TB of storage. [Source](https://lightning.network/lightning-network-paper.pdf)


## Bitcoin Devs
- BIP 103: Block size following technological growth [Pieter Wuille](https://bips.dev/103)
- _"most devs think the blocksize limit will be increased eventually, but only after other scalability improvements are adopted."_ [Peter Todd](https://www.reddit.com/r/Bitcoin/comments/34riua/comment/cqxfr43)
- _"Strongly agree.  My suggestion 2MB now, then 4MB in 2 years and 8MB in 4years then re-asses.  (Similar to BIP 102)"_ [Adam Back](https://x.com/adam3us/status/636410827969421312)
- _"SegWit is great, but it will take too long to implement to have a major impact. Need to also raise block size limit IMHO. I am very positive about Greg's scaling proposal. I think it would be a lot stronger if there was a date commitment to 2-4-8"_ [Andreas Antonopoulos](https://x.com/aantonop/status/682330638930690049)
- _"Satoshi did plan for Bitcoin to compete with PayPal/Visa in traffic volumes. The block size limit was a quick safety hack that was always meant to be removed."_ [Source](https://bitcointalk.org/index.php?topic=149668.msg1596879#msg1596879:~:text=Ian%2C%20Satoshi%20did%20plan%20for%20Bitcoin%20to%20compete%20with%20PayPal/Visa%20in%20traffic%20volumes.%20The%20block%20size%20limit%20was%20a%20quick%20safety%20hack%20that%20was%20always%20meant%20to%20be%20removed.)
- _I primarily want to keep the limit fixed so we don't have a perverse incentive. Ensuring that everyone can audit the network properly is secondarily. If there was consensus to, say, raise the limit to 100MiB that's something I could be convinced of._" [Peter Todd](https://bitcointalk.org/index.php?topic=144895.msg1537223#msg1537223:~:text=I%20primarily%20want%20to%20keep%20the%20limit%20fixed%20so%20we%20don%27t%20have%20a%20perverse%20incentive.%20Ensuring%20that%20everyone%20can%20audit%20the%20network%20properly%20is%20secondarily.)

> the block size (whether voluntarily or enforced) needs to result in a system that remains verifiable for many. What those many are will probably change gradually. Over time, more and more users will probably move to SPV nodes (or more centralized things like e-wallet sites), and that is fine. But if we give up the ability for non-megacorp entities to be able to verify the chain, we might as well be using those a central clearinghouse. There is of course wide spectrum between "I can download the entire chain on my phone" and "Only 5 bank companies in the world can run a fully verifying node", but I think it's important that we choose what point in between there is acceptable.
> 
> My suggestion would be a one-time increase to perhaps 10 MiB or 100 MiB blocks (to be debated), and after that an at-most slow exponential further growth. This would mean no for-eternity limited size, but also no way for miners to push up block sizes to the point where they are in sole control of the network. I realize that some people will consider this an arbitrary and unnecessary limit, but others will probably consider it dangerous already. In any case, it's a compromise and I believe one will be necessary. [Pieter Wuille](https://bitcointalk.org/index.php?topic=144895.msg1537737#msg1537737:~:text=there%20is%20acceptable.-,My%20suggestion%20would%20be%20a%20one%2Dtime%20increase%20to%20perhaps%2010%20MiB%20or%20100%20MiB%20blocks)

> I am - in general - in favor of increasing the size blocks: as technology grows, there is no reason why the systems built on them can't scale proportionally. [Pieter Wuille](https://www.mail-archive.com/bitcoin-development@lists.sourceforge.net/msg07466.html#:~:text=in%20favor%20of%20increasing%20the%20size%20blocks)

> I'm the guy who went over the blockchain stuff in Satoshi's first cut of the bitcoin code.  Satoshi didn't have a 1MB limit in it. The limit was originally Hal Finney's idea.  Both Satoshi and I objected that it wouldn't scale at 1MB.  Hal was concerned about a potential DoS attack though, and after discussion, Satoshi agreed.  The 1MB limit was there by the time Bitcoin launched.  But all 3 of us agreed that 1MB had to be temporary because it would never scale.
[Ray Dillinger](https://bitcointalk.org/index.php?topic=946236.msg10388435#msg10388435:~:text=I%27m%20the%20guy%20who%20went%20over%20the%20blockchain%20stuff%20in%20Satoshi%27s%20first%20cut%20of%20the%20bitcoin%20code.%C2%A0)

> Yes, the plan was to raise the size of the blocks.  And yes, I think it
should have been done.  The 1MB limit was considered temporary. We got
the current limit just to prevent people from filling space with dumb
stuff but thought, of course they'll make it bigger when people
actually need the space for legit transactions.  But now they can't
make it bigger, because that was a classic case of nerds making a
design mistake by failing to note that we were leaving a decision in
the hands of people with perverse incentives. 
 [Ray Dillinger](https://www.metzdowd.com/pipermail/cryptography/2020-December/036530.html#:~:text=Yes%2C%20the%20plan%20was%20to%20raise%20the%20size%20of%20the%20blocks.%20%C2%A0And%20yes%2C%20I%20think%20it%0Ashould%20have%20been%20done)


## More Recent Talks and Papers
- Tadge Dryja: Scaling L1 Bitcoin. [Talk](https://www.youtube.com/watch?v=yI9pee5mcBw)
- James O’Beirne: Modeling Bitcoin Blocksize Contraints. [Talk](https://www.youtube.com/watch?v=27Qs31E80cA)
- Jameson Lopp: 'Goldiblocks,' A Dynamic Bitcoin Blocksize. [Talk](https://www.youtube.com/watch?v=cPPKok5luk4)
- Arthur Gervais: On the Security and Performance of Proof of Work Blockchains. [Paper](https://eprint.iacr.org/2016/555)
- Mark Friedenbach: 'Forward Blocks', On-chain/settlement capacity increases without the hard-fork. [Paper](https://freico.in/forward-blocks-scalingbitcoin-paper.pdf)
- Scaling Bitcoin with Giacomo Zucco, John Carvalho & Matt Corallo [Interview](https://www.youtube.com/watch?v=Iz81W-_X5gw&t=3192s)

## Misc
- The temporary limit 1 MB limit was added after 1.5 years in mid 2010. Before that it was 32mb (the max network msg size) [Source](https://sourceforge.net/p/bitcoin/code/103/tree//trunk/main.h?diff=515630145fcbc978e39dbaa5:102)

- SegWit was not a real 4x block size increase -- only theoretically. In practice, it merely increased the throughput from 6-7tps to about 11-12tps. Full blocks are about 1.6 MB on average. 

### Economic Effects 
- [Jevons Paradox](https://en.wikipedia.org/wiki/Jevons_paradox)
- [Metcalfes Law](https://en.wikipedia.org/wiki/Metcalfe%27s_law)

#### Stale-Block Rates vs. Miner Revenue
A common objection to larger blocks is that slower propagation and validation increase stale-block rates, reducing the share of honest hash power securing the main chain. This is true all else equal, but it is only a partial analysis because it assumes miner revenue, transaction demand, the Bitcoin price, and hash rate remain constant. If greater on-chain capacity increases adoption and total fee revenue enough for miner revenue to grow faster than the losses caused by stale blocks, overall chain security may increase. The net effect also depends on propagation asymmetries, mining concentration, and the cost of independent validation.
````
