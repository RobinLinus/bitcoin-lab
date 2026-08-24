# [bitcoindev] [BIP Proposal] Anti-Fee-Sniping with LockTime

Source: https://gnusha.org/pi/bitcoindev/wWGWjMw9TI22vp4VzCm4xJJS3IGA1UhndMKynUkB04BqeoRjhe-QbDbJU-GMQq0nnOnXuB__u8KcdIcxU5i8Cy9pbTbtJ7Hi583FzLVojek=@pm.me/T/

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

[bitcoindev] [BIP Proposal] Anti-Fee-Sniping with LockTime

@ 2026-08-18 8:00 'nervana21' via Bitcoin Development Mailing List

2026-08-19 13:31 `

[bitcoindev]

" b10c

0 siblings, 1 reply; 3+ messages in thread

From: 'nervana21' via Bitcoin Development Mailing List @ 2026-08-18 8:00 UTC (

permalink

/

raw

) To: bitcoindev Hello all, Anti-fee-sniping with nLockTime has been present in Bitcoin Core since 2014 and in Electrum since 2017. BIP326 assumes this nLockTime behavior as the baseline and uses nSequence instead for some taproot spends. However, the nLockTime rules themselves were never specified in a BIP.

https://github.com/nervana21/bips/blob/anti-fee-snipe/bip-anti-fee-sniping-with-locktime.md

The BIP draft follows Bitcoin Core's DiscourageFeeSniping and IsCurrentForAntiFeeSniping functions. nLockTime is set to the current tip height. With probability 10%, a uniform random integer in 0..99 is subtracted and the result is clamped at 0. A locktime equal to the tip height cannot be included in a remine of the tip. An older locktime chosen on the privacy branch can. nLockTime is set to 0 during initial block download or when the tip is more than 8 hours old. The policy is not applied when nLockTime is already set or when any input already has a preset nSequence. Test vectors are included. Constructive criticism is greatly appreciated. Cheers, nervana21 -- You received this message because you are subscribed to the Google Groups "Bitcoin Development Mailing List" group. To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups•com. To view this discussion visit

https://groups.google.com/d/msgid/bitcoindev/wWGWjMw9TI22vp4VzCm4xJJS3IGA1UhndMKynUkB04BqeoRjhe-QbDbJU-GMQq0nnOnXuB__u8KcdIcxU5i8Cy9pbTbtJ7Hi583FzLVojek%3D%40pm.me

.

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

[bitcoindev] Re: [BIP Proposal] Anti-Fee-Sniping with LockTime

2026-08-18 8:00

[bitcoindev] [BIP Proposal] Anti-Fee-Sniping with LockTime

'nervana21' via Bitcoin Development Mailing List

@ 2026-08-19 13:31 ` b10c

2026-08-21 20:29 `

'nervana21' via Bitcoin Development Mailing List

0 siblings, 1 reply; 3+ messages in thread

From: b10c @ 2026-08-19 13:31 UTC (

permalink

/

raw

) To: Bitcoin Development Mailing List

[-- Attachment #1.1: Type: text/plain, Size: 3239 bytes --]

Hi nervana21, some comments in random order on the BIP proposal and Anti-Fee-Sniping: - You mention BIP125 a couple of times in Specification. Note that in recent versions of Bitcoin Core, BIP125 signaling is no longer required for a transaction to be replaceable under the default mempool policy. - While the 10%-back-date-rule in Anti-Fee-Sniping is a privacy feature for some people, it is also a privacy leak for others:

https://github.com/bitcoin/bitcoin/issues/26526:

When fee-bumping a previously not back-date transaction, Bitcoin Core might back-date the replacement. This is fingerprint that you likely back-dated the replacement transaction. There is also

https://github.com/bitcoin/bitcoin/issues/26527

, which I'm not sure if it's an actual problem or not (haven't had the time to double-check). Maybe documenting some of these edge-cases in the BIP makes sense. This allows potential future/other implementations not to make similar mistakes. - There has been a case where the trying to do Anti-Fee-Sniping 1) wasn't implemented properly in a wallet so it didn't work 2) ended up being a clear fingerprint for this wallet:

https://b10c.me/observations/01-locktime-stairs/

. By now, this wallet doesn't have much usage anymore (

https://mainnet.observer/charts/transactions-not-enforced-locktime/

) but this still shows some of it's pitfalls. - Note that currently only around 5% of the transactions set a heigt-based time-lock:

https://mainnet.observer/charts/transactions-height-based-locktime/

- growing this anonymity set might be interesting to some wallets, but currently, do don't stick out if you don't do Anti-Fee-Sniping (or use locktime). Best b10c On Tuesday, 18 August 2026 at 11:17:44 UTC+2 nervana21 wrote:

> Hello all, > > Anti-fee-sniping with nLockTime has been present in Bitcoin Core since > 2014 and in Electrum since 2017. BIP326 assumes this nLockTime behavior > as the baseline and uses nSequence instead for some taproot spends. > However, the nLockTime rules themselves were never specified in a BIP. > > >

https://github.com/nervana21/bips/blob/anti-fee-snipe/bip-anti-fee-sniping-with-locktime.md

> > The BIP draft follows Bitcoin Core's DiscourageFeeSniping and > IsCurrentForAntiFeeSniping functions. nLockTime is set to the current tip > height. > With probability 10%, a uniform random integer in 0..99 is subtracted > and the result is clamped at 0. A locktime equal to the tip height > cannot be included in a remine of the tip. An older locktime chosen on > the privacy branch can. nLockTime is set to 0 during initial block > download or when the tip is more than 8 hours old. The policy is not > applied when nLockTime is already set or when any input already has a > preset nSequence. Test vectors are included. > > Constructive criticism is greatly appreciated. > > Cheers, > nervana21 >

-- You received this message because you are subscribed to the Google Groups "Bitcoin Development Mailing List" group. To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups•com. To view this discussion visit

https://groups.google.com/d/msgid/bitcoindev/2b19cd5e-84aa-4779-b1a6-490cc918cc52n%40googlegroups.com

.

[-- Attachment #1.2: Type: text/html, Size: 4360 bytes --]

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

Re: [bitcoindev] Re: [BIP Proposal] Anti-Fee-Sniping with LockTime

2026-08-19 13:31 `

[bitcoindev]

" b10c

@ 2026-08-21 20:29 ` 'nervana21' via Bitcoin Development Mailing List

0 siblings, 0 replies; 3+ messages in thread

From: 'nervana21' via Bitcoin Development Mailing List @ 2026-08-21 20:29 UTC (

permalink

/

raw

) To: b10c;

+Cc:

Bitcoin Development Mailing List Hi b10c, Thanks for the comments, my replies are inline below. On Wednesday, August 19th, 2026 at 9:21 AM, b10c <0xb10c@gmail•com> wrote:

> Hi nervana21, > > some comments in random order on the BIP proposal and Anti-Fee-Sniping: > > > - You mention BIP125 a couple of times in Specification. Note that in recent versions of Bitcoin Core, BIP125 signaling is no longer required for a transaction to be replaceable under the default mempool policy.

You're right. I've updated the draft to remove references to BIP125. For this BIP the only sequence requirement is that at least one input is non-final so that nLockTime is enforced. The pseudocode uses 2**32 - 2 as one conventional choice.

> - While the 10%-back-date-rule in Anti-Fee-Sniping is a privacy feature for some people, it is also a privacy leak for others:

https://github.com/bitcoin/bitcoin/issues/26526:

When fee-bumping a previously not back-date transaction, Bitcoin Core might back-date the replacement. This is fingerprint that you likely back-dated the replacement transaction. There is also

https://github.com/bitcoin/bitcoin/issues/26527

, which I'm not sure if it's an actual problem or not (haven't had the time to double-check). Maybe documenting some of these edge-cases in the BIP makes sense. This allows potential future/other implementations not to make similar mistakes.

I added a Rationale section that cites

https://github.com/bitcoin/bitcoin/issues/26526

and the related type flip case

https://github.com/bitcoin/bitcoin/issues/35628

. The BIP now says implementations should document replacement locktime policy, including locktime type across replacements. When re-running the privacy branch on a height based previous locktime, it floors at that height and does not go older unless that policy is intentional and documented. The spec already covers that a child nLockTime does not protect an unconfirmed parent, so I left

https://github.com/bitcoin/bitcoin/issues/26527

out of the BIP. Separately, there is currently an open Core PR that aims at the same floor on bumpfee via minimum_height.

https://github.com/bitcoin/bitcoin/pull/36040

> - There has been a case where the trying to do Anti-Fee-Sniping 1) wasn't implemented properly in a wallet so it didn't work 2) ended up being a clear fingerprint for this wallet:

https://b10c.me/observations/01-locktime-stairs/

. By now, this wallet doesn't have much usage anymore (

https://mainnet.observer/charts/transactions-not-enforced-locktime/

) but this still shows some of it's pitfalls.

Got it. I've updated the BIP to warn implementers of this pitfall. I cited your locktime stairs writeup and the unenforced locktime chart.

> - Note that currently only around 5% of the transactions set a heigt-based time-lock:

https://mainnet.observer/charts/transactions-height-based-locktime/

- growing this anonymity set might be interesting to some wallets, but currently, do don't stick out if you don't do Anti-Fee-Sniping (or use locktime).

Makes sense. The draft now mentions this point explicitly and keeps broader adoption as the anonymity set goal. Updated draft

https://github.com/nervana21/bips/blob/anti-fee-snipe/bip-anti-fee-sniping-with-locktime.md

Best, nervana21

> > > Best > b10c > On Tuesday, 18 August 2026 at 11:17:44 UTC+2 nervana21 wrote: > > > Hello all, > > > > Anti-fee-sniping with nLockTime has been present in Bitcoin Core since > > 2014 and in Electrum since 2017. BIP326 assumes this nLockTime behavior > > as the baseline and uses nSequence instead for some taproot spends. > > However, the nLockTime rules themselves were never specified in a BIP. > > > >

https://github.com/nervana21/bips/blob/anti-fee-snipe/bip-anti-fee-sniping-with-locktime.md

> > > > The BIP draft follows Bitcoin Core's DiscourageFeeSniping and > > IsCurrentForAntiFeeSniping functions. nLockTime is set to the current tip height. > > With probability 10%, a uniform random integer in 0..99 is subtracted > > and the result is clamped at 0. A locktime equal to the tip height > > cannot be included in a remine of the tip. An older locktime chosen on > > the privacy branch can. nLockTime is set to 0 during initial block > > download or when the tip is more than 8 hours old. The policy is not > > applied when nLockTime is already set or when any input already has a > > preset nSequence. Test vectors are included. > > > > Constructive criticism is greatly appreciated. > > > > Cheers, > > nervana21 > > -- > You received this message because you are subscribed to the Google Groups "Bitcoin Development Mailing List" group. > To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups•com. > To view this discussion visit

https://groups.google.com/d/msgid/bitcoindev/2b19cd5e-84aa-4779-b1a6-490cc918cc52n%40googlegroups.com

.

-- You received this message because you are subscribed to the Google Groups "Bitcoin Development Mailing List" group. To unsubscribe from this group and stop receiving emails from it, send an email to bitcoindev+unsubscribe@googlegroups•com. To view this discussion visit

https://groups.google.com/d/msgid/bitcoindev/WCgkJmyQ8exgIWF_AXmaycRFvGbLtOwTExlanZ3qkAS1to6Ecb4VduhTFqC42Bc3XE9AIPvpx30Ebe5Vl2NeKarBMUzw8syjsAzgxIZOVso%3D%40pm.me

.

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

~2026-08-21 20:35 UTC

|

newest

]

Thread overview:

3+ messages (download:

mbox.gz

/ follow:

Atom feed

) -- links below jump to the message on this page -- 2026-08-18 8:00

[bitcoindev] [BIP Proposal] Anti-Fee-Sniping with LockTime

'nervana21' via Bitcoin Development Mailing List 2026-08-19 13:31 `

[bitcoindev]

" b10c 2026-08-21 20:29 `

'nervana21' via Bitcoin Development Mailing List

This is a public inbox, see

mirroring instructions

for how to clone and mirror all data and code used for this inbox
