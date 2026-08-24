# Bitcoin: A Peer-to-Peer Electronic Cash System — research note

This is an original, compact research note for testing the lab; it is not a copy of the source paper.

The paper proposes a peer-to-peer electronic cash system in which a public history of transactions is ordered by proof of work. Nodes accept the chain representing the greatest accumulated proof of work, making revision increasingly expensive as confirmations accumulate. Digital signatures establish authorization, while the shared transaction history addresses double spending without a central clearing party.

The threat model assumes honest participants control more computational power than any coordinated attacker. Network propagation, incentives, privacy tradeoffs, and simplified payment verification are part of the design. The paper is foundational context, but current Bitcoin behavior must be checked against later consensus code, BIPs, review discussions, and deployment history.

