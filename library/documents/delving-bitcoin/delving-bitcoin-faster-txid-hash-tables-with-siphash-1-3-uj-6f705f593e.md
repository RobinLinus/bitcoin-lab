# Faster txid hash tables with SipHash-1-3-UJ

Source: https://delvingbitcoin.org/t/faster-txid-hash-tables-with-siphash-1-3-uj/2834

Retrieved: 2026-08-24T21:52:39Z

---

## Pieter Wuille

I’d like to briefly highlight a small improvement that is coming in Bitcoin Core 32.0 (to be

released

in october): a custom variant of

SipHash

.

For context, Bitcoin Core’s validation and P2P logic extensively makes use of hash tables, for remembering what peers already gave us, for deduplicating things, for indexes, and for caching UTXOs and other things.

For several of these, these is a (mild) concern about denial of service: the data in the tables is ultimately provided by our peers, who may be in a position to give us data specifically crafted to trigger collisions in the hash tables. Individual collisions are not a problem, and to some extent even expected, but a large amount of entries that all collide with one another (a multi-collision) would end up in the same hash table bucket, causing severe performance degradation. For this reason, Bitcoin Core uses the salted hash function SipHash (with a secret salt randomly generated at startup) where relevant.

SipHash is designed as a (salted) cryptographic hash function (technically, a

PRF

), but with just a 64-bit output. This is simpler and faster than a traditional “full” cryptographic hash function, but obviously its collision resistance cannot be better than

2^{32}

. Apart from that, it is as unpredictable as a 64-bit function can be. This makes it a great choice for DoS-resistant hash tables, and it is the default in several programming language implementations for this reason (including Rust and Python).

In one particular instance, the UTXO set cache (a very performance-critical component) it is overkill, however. UTXOs are indexed by the txid of the transaction that created them, and the position in its outputs. The crucial point here is that txids are

already

cryptographic hashes (double SHA256), so it is worth asking if that fact cannot be exploited in the hash function applied on top for computing hash table buckets.

To explain where improvements are possible, consider what the current (Bitcoin Core up to 31.x) hash function used for UTXOs is.

h

is the txid here, and

i

is the output position.

siphash24_diagram

3400×2020 240 KB

sipround_diagram

3400×950 107 KB

In total this involves 14 SipRound calls.

To improve upon this, we make three changes:

Switch to SipHash-1-3.

This is a fairly common choice for hashtables (and the default in Python and Rust), as SipHash-2-4 is designed for a stronger notion of security (indistinguishability from random) than what is actually needed for hash tables (ease of creating (multi-)collisions). This just drops the number of SipRounds per compression from 2 to 1, and per finalized from 4 to 3.

Make it unpadded and block-based.

SipHash is traditionally defined over inputs that are sequences of

bytes

, which requires some padding to convert it to a sequence of 64-bit inputs fed to the Compress calls. This padding guarantees that inputs of different length cannot easily be made to collide, but we do not actually care about that here, as all inputs are the same size. The result is that we treat our hash function now in terms of an input that consists of 64-bit blocks directly, rather than bytes. To prevent confusion with the old scheme, the final constant XOR’ed into v

2

is changed from 0xff to 0x6465646461706e75 (“unpadded”).

Add support for “jumbo” blocks.

With the above in place, we now allow each input block to be

either

a normal 64-bit block, or a large 256-bit jumbo block, allowing the latter

only

when they are themselves the output of a cryptographic hash. This means that 256-bit hashes in the input (like our txid) can now be processed as a single SipRound, rather than 4 of them. This is justified by the fact that while attackers have control over the input indirectly, the cryptographic hash in between means they cannot simultaneously control many bits (control

n

bits at a cost of

2^n

grinding work).

So Bitcoin Core 32.0 will use:

siphash13uj_diagram

3400×2450 362 KB

All together, this means we reduce the number of SipRounds from 14 to 5, or with all constant-time overheads, from 17.0 ns to 10.6 ns per lookup on my Ryzen 5950X CPU.

This construction has not received significant scrutiny from cryptographers, though I did run it by

Jean-Philippe Aumasson

, one of the authors of SipHash, who did not see a way to attack it after looking at it for 20 minutes. I believe that is acceptable in this context, because we are working in a setting where the SipHash keys k

0

, k

1

are randomly generated and not known to attackers. Despite that, there does not appear to be ways to construct speed up multi-collisions (over brute force) even if the keys

are

known, so this construction is likely still significant overkill.

This was introduced in

this PR

, and is just one (rather small) performance improvement in Bitcoin Core 32.0. The biggest one is probably

fetch block input prevouts in parallel during ConnectBlock

. The SipHash-1-3-UJ function was later also used in

hash keys and pack positions to reduce disk usage

, and may end up being used in more contexts in later releases.

Thanks to all who helped us get this in, including

@l0rinc

and

@andrewtoth

.
