# D17 hostile round-2 opening ledger

**Round-2 verdict:** narrow nonselection accepted; integrated construction
received major revision.  
**Repair status:** submitted to focused round 3, 2026-07-11.

| Opening | Exact repair |
|---|---|
| Action/record cell, causal skeleton and memory circuit disconnected | New `d17_integrated_causal_history_exact.py` uses one node map from visible cylinders to actual orders, owned collars and one D14 network |
| Skeleton stopped before size four | The diamond is relabeled by old-to-new `(3,0,1,2)`, making its first three elements exactly `V3`; both branches reach the action leaves |
| No `history -> order`, `pi`, or all-depth causal map | Every mark has one `GrowthNode`; induced restriction checks every edge through depth six and maximal extension gives the printed all-depth continuation |
| `Ext(C)`, owners, joins and rejection absent | Executable declared grammar checks the live-collar owner; valid-but-undeclared and foreign-owner moves reject; a two-owner join requires exact entitlement |
| Memory not a causal boundary field | Every node collar contains the same owner-typed two-state D14 carrier and carries the branch bit locally |
| Record morphisms disconnected | Three composable owner-local D14 morphisms seal `X,Y,Z`, emit live collars and preserve prior records |
| Second packet stopped before local H6 network | `(3/5,4/5)` amplitudes pass through the same network to exact `(9/25,16/25)` records |
| Orbit packet stopped before tower | Raw inverse-automorphism amplitudes reach `(2/3,1/3)` records and the same causal tower; labeled/groupoid counting agrees |
| Reset was in a separate circuit | Owner-local CPTP reset on the integrated boundary changes support from `000/101` to `000/100` |
| Validators crashed or silently accepted malformed domains | Depth `<3`, empty, non-unit-start and nonbinary controls all reject cleanly |

The repair deliberately leaves the extension grammar, kernel and commit
supplied.  Its result is integrated **nonselection**, not an action-derived
interacting universe law.
