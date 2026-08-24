# Source snapshot rights policy

The ingestion tool visits only public URLs allowed by each host's `robots.txt`. It does not authenticate, evade access controls, expand private pages, or collect credentials. A denied or unavailable robots policy is recorded as a skipped source rather than bypassed.

Public availability does not imply an open-content license. Unless a source item explicitly states otherwise, its text remains copyrighted by the named author or publisher. Local snapshots are retained for the repository owner's research, with canonical URL, retrieval time, HTTP metadata, and SHA-256 provenance. No redistribution license is asserted. Review the source's current terms and the intended jurisdiction before publishing or redistributing any snapshot.

The registry deliberately caps large sources and sleeps between requests. `latest-report.json` records discovered/fetched/skipped items, errors, and the boundary applied to each source. Re-running the fetcher is incremental: stable canonical URLs produce stable document IDs, while changed bytes update their checksums and retrieval record.
