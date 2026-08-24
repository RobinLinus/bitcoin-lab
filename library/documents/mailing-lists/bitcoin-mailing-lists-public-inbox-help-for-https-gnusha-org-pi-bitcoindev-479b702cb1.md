# public-inbox help for https://gnusha.org/pi/bitcoindev/

Source: https://gnusha.org/pi/bitcoindev/_/text/help/

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

public-inbox help for

https://gnusha.org/pi/bitcoindev/

overview -------- public-inbox uses Message-ID identifiers in URLs. One may look up messages by substituting Message-IDs (without the leading '<' or trailing '>') into the URL. Forward slash ('/') characters in the Message-IDs need to be escaped as "%2F" (without quotes). Thus, it is possible to retrieve any message by its Message-ID by going to:

https://gnusha.org/pi/bitcoindev/

<Message-ID>/ (without the '<' or '>') Message-IDs are described at:

https://en.wikipedia.org/wiki/Message-ID

search ------ This public-inbox has search functionality provided by Xapian. It supports typical AND, OR, NOT, '+', '-' queries present in other search engines. We also support search prefixes to limit the scope of the search to certain fields. Prefixes supported in this installation include: s: match within Subject e.g. s:"a quick brown fox" d: match date-time range, git "approxidate" formats supported Open-ended ranges such as `d:last.week..' and `d:..2.days.ago' are supported b: match within message body, including text attachments nq: match non-quoted text within message body q: match quoted text within message body n: match filename of attachment(s) t: match within the To header c: match within the Cc header f: match within the From header a: match within the To, Cc, and From headers tc: match within the To and Cc headers l: match contents of the List-Id header bs: match within the Subject and body dfn: match filename from diff dfa: match diff removed (-) lines dfb: match diff added (+) lines dfhh: match diff hunk header context (usually a function name) dfctx: match diff context lines dfpre: match pre-image git blob ID dfpost: match post-image git blob ID dfblob: match either pre or post-image git blob ID patchid: match `git patch-id --stable' output rt: match received time, like `d:' if sender's clock was correct Most prefixes are probabilistic, meaning they support stemming and wildcards ('*'). Ranges (such as 'd:') and boolean prefixes do not support stemming or wildcards. The upstream Xapian query parser documentation fully explains the query syntax:

https://xapian.org/docs/queryparser.html

message threading ----------------- Message threading is enabled for this public-inbox, additional endpoints for message threads are available: *

https://gnusha.org/pi/bitcoindev/

<Message-ID>/T/#u Loads the thread belonging to the given <Message-ID> in flat chronological order. The "#u" anchor focuses the browser on the given <Message-ID>. *

https://gnusha.org/pi/bitcoindev/

<Message-ID>/t/#u Loads the thread belonging to the given <Message-ID> in threaded order with nesting. For deep threads, this requires a wide display or horizontal scrolling. Both of these HTML endpoints are suitable for offline reading using the thread overview at the bottom of each page. The gzipped mbox for a thread is available for downloading and importing into your favorite mail client: *

https://gnusha.org/pi/bitcoindev/

<Message-ID>/t.mbox.gz We use the mboxrd variant of the mbox format described at:

https://en.wikipedia.org/wiki/Mbox

Users of feed readers may follow a particular thread using: *

https://gnusha.org/pi/bitcoindev/

<Message-ID>/t.atom Which loads the thread in Atom Syndication Standard described at Wikipedia and RFC4287:

https://en.wikipedia.org/wiki/Atom_(standard)

https://tools.ietf.org/html/rfc4287

Atom Threading Extensions (RFC4685) are supported:

https://tools.ietf.org/html/rfc4685

contact ------- This help text is maintained by public-inbox developers reachable via plain-text email at: meta@public-inbox.org Their inbox is archived at:

https://public-inbox.org/meta/

This is a public inbox, see

mirroring instructions

for how to clone and mirror all data and code used for this inbox
