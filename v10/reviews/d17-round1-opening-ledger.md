# D17 round-1 opening ledger

**Verdict:** `MAJOR REVISION — INCOMPLETE-INVESTIGATION`  
**Repair status:** submitted to round 2, 2026-07-11.

| Opening | Repair |
|---|---|
| Action, boundary and orbit factors conflated | `amplitudes()` now multiplies separately supplied envelope, orbit square root and fixed phase |
| Orbit convention not propagated | Exact orbit factors pass through the D14 seal and normalize to `(2/3,1/3)` |
| “Interference” was only an amplitude sum | One fixed erasure effect is evaluated before and after the record: `0` versus `1/2` |
| Delta packet failed positive-support H6 | Second normalized envelope is `(3/5,4/5)`, giving `(9/25,16/25)` with both histories positive |
| Mark strings were not causal extensions | Root→chain/antichain→chain3/V3 are verified one-element induced-order extensions |
| Only depths 1–3 | Towers run through depth 6 and have a printed deterministic unique-child continuation induction |
| Non-Markov tuple was a ledger | Same support is realized by a local D14 carried-memory packet |
| Memory deletion missing | Complete reset changes both later branches to `z=0` |
| “Complete laws” overclaimed | Claim narrowed to projective finite-cylinder families with supplied extension/continuation data |

