# D74 — result: **TH-II with a find.** The transport curvature is genuine, irremovable, and its group is `⟨2,3⟩` at **four mutually non-nested evidence pools** (two-, three- and four-actor, plus the asymmetric sub-grammars); the **scalar** phase is empty on the honest carrier (`0/304`); and the reversal-**EVEN** channel carries **`J`** — an invariant that equals 1 exactly on flat squares and 0 exactly on curved ones. The phase remains unfound; the even channel is not silent.

**Read the scope before the headline.** Every number below is a
window-dependent measurement on the d42b1 transport grammar at the
declared depths and pools. The *proportions* move a great deal across
windows — the curvature/descent-obstruction split runs 44/88, 0/12,
604/960, 132/540, 218/334, 60/228 — so the "exactly in half" of the
anchor window is an `(A,B) d ≤ 4` coincidence and is **not** a fact about
the grammar. What does **not** move across ten scopes and four actor
pools is the **value set** `{1/2, 2/3, 3/2, 2}` and hence the group.

**Status: ROUND-1 REVIEWED AND REPAIRED, 2026-07-27.** Hostile round:
`v10/reviews/d74-round1-hostile-review.md` (independent worker,
recompute-never-trust; **VERDICT REVISE, 5 MAJOR / 6 MODERATE / 6
MINOR**). Every repair below is applied to the receipt and to this note;
**§7 is the round ledger, item by item**. The round's central find —
that the reversal-even channel this unit had declared empty is not empty
— is **the referee's**, built out of raw material this unit's own D5 arm
had computed and never looked at outside the 88 defective squares; it is
credited as such throughout, and gated at D9.1. The two structural
results (the removability threshold at `μ`-descent, and the
curvature / descent-obstruction dichotomy) survived every attack the
round mounted, including four weakenings of "descent" and a new actor
pool, and both are **stronger** after the round than before it.

Pin `v10/note-d74-transport-holonomy-pin.md` (STRICT, frozen and
committed before any code was written). Parents: D72 TERMINAL
(`note-d72-weld-result.md` — the census this unit anchors on), D65
(`note-d65-descent-conditions-result.md`), D71b
(`note-d71b-holonomy-phase-identity.md`), D64
(`note-d64-cocycle-result.md` — the coboundary-first discipline and the
C7 idiom), D73 (`note-d73-even-gram-result.md` — the generic-geometry
requirement). Receipt `v10/code/d74_transport_holonomy_exact.py`, output
`v10/data/d74_transport_holonomy_exact.out` — run from the repository
root, **exit 0**, **48 PASS / 0 FAIL** of which **7 carry no independent
information and are labelled as such** (**41 independent-evidence
passes**), **302 s wall clock** against the pin's ~25 min budget. Re-run
at `PYTHONHASHSEED=7`: **output identical apart from timings and the
echoed seed** (0 differing substantive lines).

**Every D72 number this unit rests on was re-derived from the committed
layers and reproduces exactly** — the `(A,B) d ≤ 4` census
(`1,546` closed, `88` non-unit, spectrum `{1/2: 70, 2/3: 2, 3/2: 6,
2: 10}`, kinds `{(r,d): 68, (d,r): 8, (d,n): 6, (d,d): 4, (n,d): 2}`,
`142` both-blocked, `40` half-open with its kind census, delivery-bearing
`88/88`, shallowest depth 3), the `(A,B,C) d ≤ 3` census (`12` of
`1,554`), the blindness rows (`0/88`, `0/12`), the record-graph rows
(`3969/2477/2900/424` and `3424/2128/2772/645`, `μ` class-constant
everywhere), the idle row (`{1/2: 7738, 3/4: 200}`, `1,073` comparable,
`533` without an idle) and the minimal witness digit for digit. **Exit 1
is reserved for those anchors and was not reached.** The round-1 referee
reproduced all of them independently, and re-ran the receipt at
`PYTHONHASHSEED=7` against its own instrument.

Where this note and the receipt disagree, **the receipt is
authoritative** (LOG #477's standing rule).

---

## 0. The one-paragraph answer

D72 handed over three questions: what carries the transport holonomy at
record level, is there an odd-sector `U(1)` part, and is the defect a
coboundary. **All three are answered, one of them had to be re-posed
before it could be, and one of the answers was wrong in the first pass
and is corrected here.** The naive coboundary test on this object
**cannot fail**: `r = μ(h·e_A·e_B)/μ(h·e_B·e_A)` is an **algebraic
identity of `μ`'s own recursion**, not a measurement — `μ(h·e) := μ(h)
q(e|h)`, so that ratio *is* the defining expression for `r`, on every
product-weighted grammar at every depth — and the sequence layer is a
tree, so every connection on it is a coboundary with the removing gauge
forced to `1/μ`, which sets every weight to 1. Removability is only
informative **relative to what the potential may see**, and relative to
that there is a sharp **threshold**: the twist is a coboundary exactly on
the abstractions where `μ` itself descends — the sequence and the
**record** — and on none coarser. **That is a structural explanation of
D72's blindness theorem**: the record functor is the coarsest committed
identification that keeps `μ` single-valued, and keeping `μ`
single-valued is exactly what forbids a defective square from closing.
Go one step coarser and the holonomy appears. The coarsest quotient on
which the connection **descends** is the weighted-**menu** partition —
and that existence statement is **definitional**, not a construction:
"descent quotient" means "refines `ker(menu)`", and the set of
equivalences refining a fixed kernel has a maximum by definition. What
is *measured*, and what carries the claim, is that the coarsest weighted
**congruence** (partition refinement to a fixed point) closes **exactly
the same** defective squares on every arm, and that on the quotient the
closing defective squares are **self-loops** with holonomy `≠ 1` — and a
self-loop's holonomy is gauge-invariant outright: **not removable, and
this verdict could have gone the other way**. But the carrier does not
carry all of it. A **descent** quotient may identify two histories only
if their weighted menus agree, so a square whose two orders have
different menus **closes in no descent quotient whatsoever** — at
`(A,B) d ≤ 4` that is 44 of the 88. **The qualifier "descent" is
load-bearing and was missing from the first pass**: coarser quotient
*graphs* do close that half — MULT, rung 3 of this unit's own ladder,
closes **88 of 88** — what they lose is descent. The group is `⟨2,3⟩`,
free abelian of rank 2, the full group of 3-smooth positive rationals,
and it does not move from depth 4 to depth 6, from two actors to three,
under either asymmetric sub-grammar, or — the round's added scope, and
the first genuinely **independent** one — at a **fourth actor pool**
`(A,B,C,D)` with its own new menu masses `{4, 9/2}` and 1,728 defective
squares. It is **not** D65's object: normalising by the menu mass leaves
every one of the raw-defective squares **exactly unchanged** and adds a
**disjoint** family of new defects at the mass ratios. And the odd
sector: **the SCALAR odd sector — the `U(1)` part — is empty, and D2
settles that a priori in one line** (a positive-rational holonomy's only
possible unimodular content is `−1`, realised nowhere); the honest
order-dual carrier is empty too, and **more emphatically than the first
pass established**: of **all 304 linear extensions** of the opposite
poset of the 176 defective endpoints, **0 are admissible**, and the
reason is not that this grammar blocks reversal (**2,196 of 3,092**
closed-square endpoints *are* reverse-admissible) but that the defect
locus is sharply special. **What is NOT empty is the reversal-EVEN
channel.** The first pass said it was, on the strength of a tautology
about `log r`. The round-1 referee built, from this receipt's own D5 raw
material, the predicate
`J(square) := [both endpoint sequences are reverse-admissible]` — a
symmetric, hence reversal-**even**, substrate-supplied invariant — and it
is not constant: across three arms **`J = 1` on 8,600 closed squares,
every one of them with holonomy exactly 1**, and **`J = 0` on every one
of the 1,060 defective squares**. `J` is a flatness predicate that
locates the curvature, and it is not a relabelling of the register
invariant this unit already had. **TH-II fires — with `J`.**

---

## 1. What each arm returned

Gates marked **[NO INDEPENDENT INFORMATION]** are run and printed but
excluded from the evidence count: they are identities of their own
definitions. Five of the seven were tagged at round 1.

### TH-C — REMOVABILITY (run and reported first, per the pin and D64)

| gate | result |
|---|---|
| **C0.1 the vacuity lemma** **[NO INDEPENDENT INFORMATION]** | `r = μ(h·e_A·e_B)/μ(h·e_B·e_A)` on **3,100/3,100** closed squares of the two anchor arms. This is an **identity of `mu_map`'s recursion** `μ(h·e) := μ(h) q(e|h)` together with the definition of `r`; it holds on every product-weighted grammar at every depth and cannot return an exception. The only thing it can detect is a disagreement between `candidates_for`'s weights and `admissible`'s — our own plumbing. It is reported because the **conclusion** is load-bearing, not because the count is evidence |
| **C0.2 therefore the naive test carries no information** **[NO INDEPENDENT INFORMATION]** | the sequence layer is a tree, so `H¹ = 0` there for v8 p1:77's reason; the potential is unique up to a constant per component, so `1/μ` is **the** removing gauge and it gauges every weight to 1 |
| **C1 the D65 test** | `r = M(h·e_B)/M(h·e_A)` holds on **1,254 of 1,546** (`AB4`) and **1,410 of 1,554** (`ABC3`) — and on **none** of the defective squares. The intermediate mass ratio restricted to the raw-defective squares is `{1: 88}` and `{1: 12}`: **normalisation moves them not at all**. It adds a disjoint family: `AB4` normalised spectrum `{4/5: 114, 1: 1254, 5/4: 90}` **plus** the untouched `{1/2: 70, 2/3: 2, 3/2: 6, 2: 10}` |
| **C2.1 the threshold, route 1** (potential propagation) | coboundary at **SEQ** and **REC**; **NOT** at MULT, STATE, PORT, MENU. The quantity that is 88 at each of those four rungs is **independent cycles + defective self-loops** (the table below prints the two columns separately: R1 obstruction `0,0,0,0,44,44`; self-loops `0,0,88,88,44,44`). `μ` descends on `3969/3969` and `2477/2477`, and on `514/578`, `84/125`, `24/65`, `44/113` |
| **C2.2 the threshold, route 2** (relabelled recount — D64's C7 idiom on `R⁺`) | the spanning-forest potential propagated over each quotient's own up-graph, the whole census re-run with the gauged weights `q' = q·φ(α(h·e))/φ(α(h))`: **survivors 0 exactly where the obstruction is 0**, rung for rung (`0, 0, 88, 88, 96, 180`). The direction of this gauge is the receipt's own tripwire — getting it backwards squares the defect instead of cancelling it, and the SEQ rung, where `φ` is `μ` exactly, is what caught it |
| **C2.3 anti-vacuity** | at SEQ the exchange graph is a **perfect matching** — 1,546 edges on 3,092 nodes, **cycle rank 0**. The coarse rungs carry 134 / 80 independent cycles and 88 defective self-loops, so a flat answer was available there and was not returned |
| **C2.4 the `σ`-port rung** | the pin's prediction upheld: PORT closes **44 of 88**, not all — D62's machinery at transport scope does not carry it. **Round-1 addition:** PORT closes **exactly the same 44 as MENU, as sets** and not merely in number |

**The ladder in full** (`AB4`; `sq close` and `DEF close` are how many of
the 1,546 closed and 88 defective squares the rung identifies):

| α | classes | μ descends | menu descends | multi-valued edges | sq close | DEF close | ex. cycle rank | R1 obstruction | self-loops | R2 survivors |
|---|---|---|---|---|---|---|---|---|---|---|
| SEQ | 3969 | 3969/3969 | 3969/3969 | 0 | 0/1546 | 0/88 | 0 | 0 | 0 | 0 |
| REC | 2477 | 2477/2477 | 2477/2477 | 0 | 473/1546 | 0/88 | 145 | 0 | 0 | 0 |
| MULT | 578 | 514/578 | 492/578 | 8 | 1546/1546 | 88/88 | 0 | 0 | 88 | 88 |
| STATE | 125 | 84/125 | 103/125 | 4 | 1546/1546 | 88/88 | 0 | 0 | 88 | 88 |
| PORT | 65 | 24/65 | 29/65 | 0 | 1458/1546 | 44/88 | 80 | 44 | 44 | 96 |
| MENU | 113 | 44/113 | 113/113 | 0 | 1402/1546 | 44/88 | 134 | 44 | 44 | 180 |

Route 2's survivor count is **not** route 1's obstruction count and is
not claimed to be: the relabelled recount applies **one** spanning-forest
potential, which removes what it can along the forest and can push other
squares **off** 1 in the process (96 and 180 against an obstruction of
44). What the gate asserts, and what holds rung for rung, is the
zero/non-zero agreement: **survivors are 0 exactly where the obstruction
is 0.**

MULT and STATE close every square but only by **losing descent** (8 and 4
multi-valued labelled edges at `AB4`); their obstruction is carried
entirely by defective self-loops. **The verdict: removable at `[SEQ,
REC]`, NOT removable at `[MULT, STATE, PORT, MENU]`.**

### TH-A — THE CARRIER

| gate | result |
|---|---|
| **A1.1 the census extended** | `(A,B) d ≤ 5`: **960 of 11,814** non-unit; `(A,B,C) d ≤ 4`: **540 of 22,482**; `(A,B) d ≤ 6`: **8,536 of 94,542**; `(A,B,C) d ≤ 5`: **14,736 of 331,860**. Every defect delivery-bearing in every arm; shallowest defect at total depth 3 in every arm |
| **A1.1 the asymmetric arms** | ASYM-1 (`(A,B)`, the one-way link `A→B` only, `d ≤ 5`): **334 of 5,504**; ASYM-2 (`(A,B,C)`, the defected directed ring `A→B→C→A`, `d ≤ 4`): **228 of 8,673**. Declared **sub-grammars**: the support is restricted, the committed weights untouched |
| **A1.2 the asymmetric arms are not vacuous** | they really remove support — 11,814 → 5,504 and 22,482 → 8,673 closed squares — and the defect survives the removal |
| **A1.3 the FOURTH ACTOR POOL** (added at round 1) | `(A,B,C,D) d ≤ 3`: **24 of 6,624**; `(A,B,C,D) d ≤ 4`: **1,728 of 155,704**. New **menu masses** `{4: 569, 9/2: 24}`, **disjoint** from the two-actor `{2, 5/2}` and the three-actor `{3, 7/2, 19/4}` — so this pool is *not* a re-count of squares already seen. Every defect delivery-bearing; shallowest still total depth 3; value set exactly `{1/2, 2/3, 3/2, 2}`, **no new prime at four actors** |
| **A2.1 the classification** | **every** defective square is register-overlapping and the overlap is **always on an ACTOR register**, never on a version register alone — `{actor: 88}`, `{actor: 12}`, `{actor: 960}`, `{actor: 334}`. Against D72's T2.3b (a square closes at record level exactly when register-disjoint) this makes the blindness **exact, not statistical** |
| **A3.1 the carrier** | the coarsest **descent** quotient — the weighted-menu partition — closes a non-zero number of defective squares on **five of the six** full arms; the coarsest weighted **congruence** (partition refinement, 4–6 rounds to a fixed point) closes **exactly the same** defective squares on **all six**. The *existence* of a coarsest descent quotient is **definitional** (see §3(i)); the measured content is this agreement |
| **A3.2 the descent dichotomy, in its orientation-invariant form** | `AB4`: **44 curvature-type + 44 descent-obstruction-type = 88**, and that split is invariant under CTL-ORDER. The *kind-clean* refinement is **not** invariant and is now reported as an orientation reading: forward the invisible half is `(r,d)` at `1/2`, reversed it is `(d,r)` at `2`. The invariant statement is the **unordered class** `{r, 1/r}`: `{1/2 ≡ 2}: 44` both ways |
| **A3.3 not removable on the carrier** **[NO INDEPENDENT INFORMATION]** | the closing defective squares are **self-loops** at a single menu class carrying `{1/2: 26, 2: 10, 2/3: 2, 3/2: 6}`; a self-loop's holonomy is gauge-invariant outright, so **no** potential on the carrier removes them. The **argument** is sound and the verdict stands; the **gate** is definitional — a square's edge runs between the classes of its two endpoints, so "closes in the quotient" *is* "self-loop", and the count cannot fail. Non-unit self-loops on the six arms: 44, 0, 604, 132, 218, 60 |
| **A3.4 the dichotomy under four WEAKER notions of descent** (added at round 1) | of the 44 descent-obstruction squares, identified by **labelled-edge single-valuedness 0**, by the **normalised menu `q/M`** (D65's own measure-twisted repair) **0**, by **equal support 0**, by **proportional menus** (projective descent) **0**. The obstruction does not depend on the strong notion this unit chose: the two orders genuinely disagree on the weight of a **shared** event |
| **A3.5 a quotient GRAPH that closes the "unclosable" half** (added at round 1) | **MULT closes 88 of 88**, including **44 of 44** of the menu quotient's invisible set — at the price of 8 multi-valued labelled edges, i.e. no descent. So "no quotient graph can carry it" is **false**; the true statement is that the descent-obstruction half is closable **only by quotients on which the connection is not well defined** |

**The carrier, arm by arm:**

| arm | menu classes | congruence classes | DEF closed (menu = congruence) | curvature-type | descent-obstruction-type |
|---|---|---|---|---|---|
| `AB4 (A,B) d≤4` | 113 | 185 | 44 / 88 | 44 | 44 |
| `ABC3 (A,B,C) d≤3` | 117 | 162 | **0 / 12** | 0 | 12 |
| `(A,B) d≤5` | 265 | 462 | 604 / 960 | 604 | 356 |
| `(A,B,C) d≤4` | 525 | 747 | 132 / 540 | 132 | 408 |
| `ASYM-1 (A,B) d≤5` | 245 | 438 | 218 / 334 | 218 | 116 |
| `ASYM-2 (A,B,C) d≤4` | 525 | 747 | 60 / 228 | 60 | 168 |

**The `ABC3` row is reported and not buried**: at three actors and depth
3 the carrier sees **none** of the 12; the whole defect there is of the
descent-obstruction type. One depth further out (`(A,B,C) d ≤ 4`) the
carrier sees 132.

### TH-B — THE GROUP

**What the scopes are, honestly** (round-1 MODERATE 5). The `(A,B)` and
`(A,B,C)` rows are **two nested depth chains** — the census enumerates
bases to depth `d−2`, so the `d ≤ 5` arm re-counts every `d ≤ 4` square
and the `d ≤ 6` arm every `d ≤ 5` square; the 88 defective squares of
`AB4` are literally a **subset** of the 960 of `(A,B) d ≤ 5` — plus **two
sub-grammars** of them. Nesting is not nothing (along a chain the value
set can only *grow*, so stability there is a real constraint) but it is
not independent replication, and the cumulative count double-counts. The
`(A,B,C,D)` rows **are** independent: a new pool, new menu masses, no
square in common with any other arm.

| scope | non-unit spectrum | value set | group |
|---|---|---|---|
| `AB4` | `{1/2: 70, 2/3: 2, 3/2: 6, 2: 10}` | `{1/2, 2/3, 3/2, 2}` | `⟨2,3⟩`, rank 2 |
| `ABC3` | `{1/2: 12}` | `{1/2}` | `⟨2⟩`, rank 1 |
| `(A,B) d≤5` | `{1/2: 654, 2/3: 58, 3/2: 118, 2: 130}` | same four | `⟨2,3⟩` |
| `(A,B,C) d≤4` | `{1/2: 456, 2/3: 6, 3/2: 18, 2: 60}` | same four | `⟨2,3⟩` |
| `(A,B) d≤6` | `{1/2: 4846, 2/3: 1114, 3/2: 1358, 2: 1218}` | same four | `⟨2,3⟩` |
| `(A,B,C) d≤5` | `{1/2: 10968, 2/3: 372, 3/2: 948, 2: 2448}` | same four | `⟨2,3⟩` |
| ASYM-1 | `{1/2: 184, 2/3: 10, 3/2: 68, 2: 72}` | same four | `⟨2,3⟩` |
| ASYM-2 | `{1/2: 190, 2/3: 2, 3/2: 10, 2: 26}` | same four | `⟨2,3⟩` |
| **`(A,B,C,D) d≤3`** (new pool) | `{1/2: 24}` | `{1/2}` | `⟨2⟩`, rank 1 |
| **`(A,B,C,D) d≤4`** (new pool) | `{1/2: 1500, 2/3: 12, 3/2: 36, 2: 180}` | same four | `⟨2,3⟩` |
| **cumulative** | 27,186 non-unit squares over the ten scopes (nested arms double-counted) | `{1/2, 2/3, 3/2, 2}` | **`⟨2,3⟩` = the FULL group of 3-smooth positive rationals, free abelian of rank 2, index 1 in `Z²`** |

**B.1** the value set does not move: every scope's set is contained in
the anchor window's, and the cumulative set **equals** it, while the
counts run 88 → 14,736 and the pool runs from two actors to four.
**B.2** the group is computed as an integer exponent lattice (Hermite
reduction on the prime valuations, basis `[[-1,0],[0,1]]`, index 1), not
read off four values by eye; it is **rank 2 and not cyclic**. The rank-1
comparison object `⟨5/4⟩` on primes `{2,5}` is **D72's** — its licensed
claim 6 / T4.3, on the *normalised* d42b3 kernel — **not D65's**; D65
writes no group notation anywhere (attribution corrected at round 1).
**B.3** the carrier's **own** holonomy group — the group of the menu
quotient's loops, the basis-independent object — is also `⟨2,3⟩`; the
count of non-trivial basis cycles is forest-dependent and is **not**
licensed as a number.

### TH-D — THE ODD SECTOR, AND (round 1) THE EVEN ONE

| gate | result |
|---|---|
| **D1 the reversal acts on `r` by inversion** **[NO INDEPENDENT INFORMATION]** | `r` is *defined* as `q(e_A\|h)q(e_B\|h·e_A) / q(e_B\|h)q(e_A\|h·e_B)`; swapping the two events exchanges numerator and denominator, so the swapped value is `1/r`. A one-line lemma with **no positive-exception branch on any grammar**. The first pass's "1,546/1,546, gap exactly 0" implied a measurement it is not. What follows is that **`log r` is purely odd** — a statement about `log r` **alone**. The first pass promoted it to "the reversal-even channel is empty, the mirror of v7's amplitude". **That promotion is withdrawn**: see D9 |
| **D2 the unimodular part** | every committed weight is a positive rational, so every holonomy is; the only positive rational of modulus 1 is 1. **A `U(1)` part of a rational-valued holonomy could only ever be the sign `−1`** — the search reduces exactly to a search for a canonical sign, and `−1` is realised nowhere. **This settles the scalar odd sector a priori, in one line, before any fixture is run** |
| **D3.1 the label-local no-go** **[NO INDEPENDENT INFORMATION]** | any connection whose value depends only on the **event label** has trivial holonomy on **every** exchange square: the two sides use the same two events, each once, so a label-indexed cochain cancels. Now gated on the structural fact itself — the two paths carry the **same event multiset**, verified on 3,100/3,100 closed squares of the anchor arms — instead of on the bare constant `True` the first pass used. It says where not to look |
| **D4.1 the i-twist correspondence, controlled** **[NO INDEPENDENT INFORMATION]** | in the real form `L = r`, v7's law `rev(L) = conj(L)` fails on **exactly the 88** defective squares. For the twist `L' = e^{i log r}` the law reads `r(rev)·r = 1` — which **is D1's identity**, so the twist restores it on every square and adds nothing. The first pass's "500 adversarial rationals" control evaluated `−x == −x` and never applied a reversal at all; it is replaced by a **discriminating** control that can and does fail: on 500 drawn `(forward, reversed)` pairs whose reversal is **not** inversion the twisted law fails **500 of 500**, and holds **500 of 500** when the reversal is made inverting. The evidence for "content-free" is the **argument**, not a count |
| **D5.0 the grammar is NOT reversal-blocking** (added at round 1) | the first pass's stated reason for the 0/176 — "the reversed sequences are overwhelmingly not admissible histories of this grammar" — is **false**. Measured on the complement it never looked at: **2,456 of 3,960** histories with `\|h\| ≥ 2` reverse into admissible histories (`56/60` at 2, `352/452` at 3, `2,048/3,448` at 4), and **2,196 of 3,092** closed-square endpoints are reverse-admissible, including **1,798 of 2,286** delivery-bearing ones. The 0-of-everything on the defect locus is therefore **not** a generic support fact; it is a sharp, highly non-generic property **of the defect locus** |
| **D5.1 the order-dual arm** | **0 of 88** defective squares have an in-family dual square, so there is no second value to read a conjugating residue off. D72's T1.4 showed `*` and the transport reversal coincide only on 2-event histories; every defect here sits at total depth ≥ 3 |
| **D5.2 the honest order-dual: EVERY linear extension** (added at round 1) | the first pass tested **one enumeration-chosen sequence** per endpoint and mis-cited it as "D71b's linear-extension carrier". D71b's carrier is the committed **unlabeled record order** and its `*` is **poset reversal**, which is defined on every poset and is never "not defined"; **linear extensions are D72's** construction (claim 2, 2-event scope). Rebuilt honestly: for the 176 endpoints of the 88 defective squares, **all 304 linear extensions** of the committed `event_poset` — all 304 admissible forwards — **0 of 304 admissible reversed**. The negative is real and **stronger** than the first pass established: the **opposite poset has no admissible realisation at all, in any order** |
| **D6.1 the canonical orientation — and its failure** | a substrate-supplied orientation does exist (order each mixed-kind square so the **delivery is second**) and under it **84 of the 84 orientable** defective squares of `AB4` (4 are unorientable, equal kind rank) and **12 of 12** at `ABC3` land strictly **below 1**: acting before delivering always suppresses the joint weight. **It does not survive the wider arms.** `(A,B) d ≤ 5`: `{<1: 868, >1: 8}` (84 unorientable); `(A,B) d ≤ 6`: `{<1: 7116, >1: 344}` (1,076 unorientable); `(A,B,C) d ≤ 5`: `{<1: 13464, >1: 24}`; ASYM-1: `{<1: 332, >1: 2}`. Sign-definite on `AB4`, `ABC3`, `(A,B,C) d ≤ 4`, ASYM-2 only |
| **D7.1 the asymmetric substrates** | same `U(1)` verdict: `R⁺`-valued, same group `⟨2,3⟩`, no unimodular part — **breaking the actor symmetry does not create a phase**. It does independently confirm D6.1's break |
| **D9.1 THE REVERSAL-EVEN CHANNEL IS NOT EMPTY — the round's find** | define `J(square) := [both endpoint sequences are reverse-admissible]`, i.e. `rev(h·e_A·e_B)` and `rev(h·e_B·e_A)` are both admissible histories from the empty history. `J` is **symmetric in `(e_A, e_B)`**, hence **reversal-even**; it is never mixed (no square has exactly one reverse-admissible endpoint, in any arm). It is **not constant**, and: `AB4` `J=1` on 1,098 (all `r = 1`), `J=0` on 448 (360 unit + **88 defective**); `ABC3` `J=1` on 1,476 (all `r=1`), `J=0` on 78 (66 + **12**); `(A,B) d≤5` `J=1` on 6,026 (all `r=1`), `J=0` on 5,788 (4,828 + **960**). **`J = 1 ⟹ r = 1` on 8,600 closed squares across three arms, zero exceptions; `J = 0` on all 1,060 defective squares.** Not a relabelling of A2.1's register invariant: **793** `J=1` squares are register-**overlapping**, and **168** register-disjoint squares have `J=0`. Not a depth artefact: within the deepest `AB4` stratum alone, **912 of 1,252** unit squares carry `J=1` and **0 of 84** defective ones do |
| **D8 the verdict** | **no SCALAR orientation-sensitive residue exists on this carrier.** Every scalar quantity this unit could build on the holonomy-carrying loops inverts under reversal; nothing conjugates. This is the `U(1)` statement, settled a priori by D2 — **not** the statement that the even channel is empty, which D9.1 refutes |
| **OUT.1 the outcome selector is three-way, demonstrated** (added at round 1) | the first pass's selector **could not return TH-III on any input**: one disjunct ranged over unimodular values in a set D2 had already proved contains only positive rationals, the other over a counter incremented inside a loop body that never executed. The selector is now a **function**, and it is fed input on which each branch must fire — flat carrier → `TH-I`; holonomy set `+ (−1)` → `TH-III`; one conjugating dual square → `TH-III`; the substrate's own inputs → `TH-II`. The negative at this address is now a reportable negative |

**The delivered outcome: TH-II WITH `J`** — non-coboundary, `R⁺`-valued,
the **scalar** odd sector empty, and a non-trivial **reversal-even**
invariant that equals 1 exactly on the flat squares and 0 exactly on the
curved ones, on every window run.

---

## 2. The controls

| control | what it shows |
|---|---|
| **CTL-FLAT** | the d42b3 closed grammar through **this** receipt's own census code returns `{1: 403}` and **no** half-open square — the pipeline does not manufacture defects |
| **CTL-TAMPER** | multiplying **one** committed step weight by `3/2` moves the census (88 → 94 non-unit). Unlike D72's T2.NC — which perturbed one edge of an exact gradient and therefore **could not fail** — this control can fail |
| **CTL-ORDER** | **a control the corpus did not run, and it bites.** See §3(a) — and, after round 1, §3(j), where it is turned on **this unit's own** dichotomy headline |
| **CTL-DET** | forward and reversed spanning-forest builds agree on nodes, components, cycle rank, obstruction count and the holonomy value **set**; D72's lesson that the count of non-trivial **basis** cycles is forest-dependent is carried, and that count is not licensed |
| **anti-vacuity (C2.3)** | the removability test at the coarse rungs is not a test on a forest — the sequence-level exchange graph **is** a forest (a perfect matching), which is precisely why C0's verdict there is empty |
| **the i-twist control, rebuilt (D4.1)** | the replacement control **can fail and does**: 500/500 failures when the reversal is not inversion, 500/500 successes when it is. The first pass's version verified `−x = −x` |
| **OUT.1, the outcome selector's own control** | each of the three pre-registered branches is exercised on constructed input |

---

## 3. Findings, including the ones that correct this unit's own first
instincts

**(a) D72's spectrum split and its half-open split are ENUMERATION-
ORIENTATION readings, not substrate facts — and the correction is
addressed to D72's TABLE ROWS, not to its licensed claim.**
`[MEASURED]`. Re-running the identical census with the candidate list
traversed in the opposite order leaves the closed / half-open /
both-blocked **totals** and the defect **count** invariant, and leaves the
multiset of **unordered** value classes `{r, 1/r}` invariant
(`{1/2: 80, 2/3: 8, 1: 1458}` both ways) — but it **transposes** the
spectrum to `{1/2: 10, 2/3: 6, 3/2: 2, 2: 70}` and the half-open split
from `(28, 12)` to `(12, 28)`. **Addressee corrected at round 1
(MODERATE 1):** those multiplicities and that split are D72's rows
**T6.1 / T6.2** (`note-d72-weld-result.md:150-151`) and its DELTA. They
are **not** in D72's licensed claim 7, which licenses the **value set**
and the **totals** — and every one of D72's licensed claims survives
CTL-ORDER **untouched**, which is a credit to the parent the first
draft withheld. The routing is against the rows and the DELTA; D72 is
TERMINAL and this unit edits nothing.

**(b) The removability question, as the corpus had been posing it, cannot
fail — and the fix is a threshold, not a yes/no.** `[THEOREM, gated]`.
C0.1/C0.2. This is D72's own MAJOR 3 (`T2` is a corollary of `T1.8`) one
level up, and it was very nearly repeated here — and, at round 1, was
found to have been *partly* repeated: C0.1, the actual tautology, was
counted as evidence while C0.2, which at least says something about the
shape of the sequence layer, was the one tagged. Both are tagged now.
What is informative is **where** in the abstraction ladder the coboundary
property dies, and it dies immediately below the record functor.

**(c) The record functor sits exactly at the threshold, and that explains
D72's blindness theorem instead of restating it.** `[MEASURED]`. `μ` is
class-constant on records (D72's own anchor) — so `1/μ` is a per-record
potential and the twist is a record-level coboundary. But a potential
that is single-valued on classes is exactly what makes a square's two
orders land in **different** classes when `r ≠ 1`. **The instrument is
blind because it is fine enough to be flat.** Any coarser committed
abstraction breaks `μ`'s single-valuedness and the holonomy appears.

**(d) Half the transport defect is not curvature but a DESCENT
obstruction — and the qualifier is the whole content.** `[THEOREM +
MEASURED]`. A **descent** quotient can only identify histories with equal
weighted menus; a defective square whose two orders have different menus
therefore closes in **no descent quotient**. At `AB4` that is 44 of the
88. The proportion is **strongly window-dependent** (44/88, 0/12,
604/960, 132/540, 218/334, 60/228), which is why the "exactly in half" is
not a headline. **Corrected at round 1 (MAJOR 5):** the first pass wrote
"a descent obstruction **that no quotient graph can carry**, and for
which the exchange square is the only instrument". That is false on this
unit's own page — **MULT**, rung 3 of the ladder, closes **88 of 88**,
including **all 44** — and MULT is a perfectly good quotient graph; what
it fails is *descent*, by the **8 multi-valued labelled edges** (of
1,288 labelled edges at that rung, carrying 3,968 up-moves) that the
ladder's `multi-w` column already printed. The true and
sharper statement: **the descent-obstruction half is closable only by
quotients on which the connection is not well defined.** The obstruction
is also **robust**: four strictly weaker notions of descent —
labelled-edge single-valuedness, the normalised menu `q/M` (D65's own
measure-twisted repair), equal support, and proportional (projective)
menus — identify **0 of 44** each. The dichotomy is therefore **stronger
than the first pass argued**, and now correctly scoped.

**(e) The transport twist and D65's mass twist are orthogonal — and the
three-actor mass set CONFIRMS D65's own residue 2 rather than correcting
it.** `[MEASURED]`. Normalising to the process's own conditional kernel
multiplies each square ratio by `M(h·e_B)/M(h·e_A)`, and that factor is
**identically 1** on every raw-defective square in both anchor arms. The
normalisation defect lives on a disjoint set of squares and its values
are mass ratios. At two actors those are `{4/5, 5/4}` (from masses
`{2, 5/2}`, D65's committed set exactly); **at three actors they are
not** — the menu masses are `{3: 3100, 7/2: 288, 19/4: 36}` and the
normalised defects are `{6/7: 84, 7/6: 48}`. **Re-attributed and
downgraded at round 1 (MODERATE 3):** D65 says this itself, twice — its
residue 2 reads *"`M` takes two values here because the quarter law's
excess is binary at two actors. At three actors or with delivery the mass
spectrum changes and the coboundary statement must be **re-derived, not
carried**"*, and its explicitly-not-licensed list already forbids the
claim at three-actor and **at transport** scope. So this is a
**confirmation of the parent at a scope the parent explicitly refused**,
not a correction routed against it. Separately: the infinite cyclic group
`⟨5/4⟩` is **D72's** object (claim 6 / T4.3), not D65's — D65 writes no
group notation at all.

**(f) The odd sector's most attractive candidate died at depth 5.**
`[MEASURED]`, self-corrected. The kind-canonical orientation (delivery
second) makes the defect sign-definite on **both** anchor arms — **84 of
the 84 orientable** squares strictly below 1 at `AB4` (4 unorientable),
12 of 12 at `ABC3` — and it is exactly the transport-scope echo one would
want of D72's unexplained sign-definiteness of `O` (T3.B2). It is
**false** at `(A,B) d ≤ 5` (8 squares above 1), at `(A,B) d ≤ 6` (344),
at `(A,B,C) d ≤ 5` (24) and on ASYM-1 (2). **The breakage is a depth
effect first and a symmetry effect second** — D73's requirement landed,
but the deeper symmetric window would have caught it on its own. Had this
unit run only the pin's inherited window it would have published a false
headline.

**(g) The kind census of the defect grows with depth.** `[MEASURED]`.
D72's five kind pairs are a `d ≤ 4` fact: at `(A,B) d ≤ 6` two more
appear among the **closed** defective squares, `(p,d): 48` and
`(d,p): 48` — kinds that at `d ≤ 4` occur only among the **half-open**
squares. The value group does not grow with them.

**(h) A phase cannot be label-local.** `[THEOREM]`. D3.1. Any `U(1)`
cochain attached to event labels cancels on every exchange square. The
transport modulus is non-trivial precisely because `q(e|h)` reads the
history. If a phase exists anywhere in this grammar it must read the
history too — and nothing in the committed layer produces a non-positive
number to read it with.

**(i) The coarsest descent quotient is a DEFINITION, not a
construction.** `[DEFINITIONAL]`, corrected at round 1 (MODERATE 4).
"Descent quotient" means `h ~ h' ⟹ q(·|h) = q(·|h')`, i.e. "`~` refines
`ker(menu)`". The set of equivalences refining the kernel of a fixed
function has a maximum — the kernel — by definition, so existence,
uniqueness and the identification with the menu partition are one and the
same triviality; the join-closure argument is decoration, and "it is not
a search" is true because the definition names the answer. **The choice
of notion is also now declared:** the weaker and arguably more natural
notion for a labelled quotient graph — agree only on events admissible at
both — is *not* join-closed and has no unique coarsest, which is why it
was not chosen; A3.4 runs it anyway, and it changes nothing. What carries
claim 4 is the **measured** agreement between the menu partition and the
independently computed coarsest congruence.

**(j) CTL-ORDER, turned on this unit's own headline.** `[MEASURED]`,
added at round 1 (MODERATE 2). Re-running the dichotomy under the
reversed candidate order: the **44 + 44 split is invariant**, and so is
the unordered class multiset `{1/2 ≡ 2}: 44` on the invisible half; but
the *kind-clean* refinement is **not** — forward the invisible half is
`(r,d)` at the single value `1/2`, reversed it is `(d,r)` at `2`. A gate
whose predicate asserted an orientation-dependent value set is exactly
the defect §3(a) routes upstream, and it has been rewritten to assert the
invariant form. (The deeper arms' unseen spectra, `{1/2: 348, 2/3: 8}` at
`d ≤ 5` and `{1/2: 378, 2: 30}` at `(A,B,C) d ≤ 4`, are genuinely
two-valued and so partly orientation-robust; the `AB4` row is the fragile
one.)

**(k) The reversal-EVEN channel carries a non-trivial invariant.**
`[MEASURED]` on three windows, **not a theorem** — **this is round 1's
find and it is the referee's, not this unit's**. See D9.1. The
consequence for the unit's most quoted sentence is direct: v7's amplitude
puts the **modulus** in the even channel and the phase in the odd one;
the first pass concluded that the transport object "puts its modulus in
the odd channel and leaves the even one empty — the mirror image of v7".
That conclusion was drawn **entirely from `log r`**, where "no even part"
is the tautology of D1. On the carrier itself there **is** non-trivial
even-channel structure; it is supplied by the substrate rather than by
the enumeration — which is exactly what D6 was hunting and failed to find
in the odd channel — and it is a **flatness predicate**. The corrected
sentence: **the SCALAR ODD (U(1)) sector is empty, confirmed at greater
strength than the first pass established; the reversal-EVEN channel
carries a non-trivial invariant that predicts the curvature's location.**

**(l) The order-dual negative is real, and stronger than it was.**
`[MEASURED]`, corrected at round 1 (MAJOR 4). The carrier was
mis-attributed (D71b's is the record order under poset reversal; linear
extensions are D72's, at 2-event scope), the arm tested a third object,
and the committed `linear_extensions` was declared as an AST dependency
and never called. Rebuilt: **0 of 304** linear extensions of the opposite
posets are admissible. And the *reason* is corrected — the grammar is
**not** reversal-blocking (**2,196 of 3,092** closed-square endpoints are
reverse-admissible) — so the inadmissibility is specific to the defective
squares' structure. This is the same measurement that, viewed on the
complement, is `J`.

---

## 4. Licensed claims — no wider than the fixtures run

1. **On the d42b1 transport grammar**, at `(A,B)` depths 4, 5 and 6, at
   `(A,B,C)` depths 3, 4 and 5, at **`(A,B,C,D)` depths 3 and 4**, and on
   the two declared asymmetric sub-grammars, the closed exchange squares
   have `dP_AB/dP_BA` in `{1/2, 2/3, 3/2, 2}` and the multiplicative
   group generated is **`⟨2,3⟩`, free abelian of rank 2, the full group of
   3-smooth positive rationals**, with prime support `{2,3}` and index 1
   in `Z²`. `[MEASURED]`, exact arithmetic, on those windows. The two
   depth chains are **nested**; the four-actor pool is the one
   independent replication and it introduces **no new prime**.
2. **`r = μ(h·e_A·e_B)/μ(h·e_B·e_A)` on every closed square of both
   anchor arms** (3,100/3,100) — an **identity of the product weight**,
   not a measurement of this substrate. Hence the transport connection is
   a coboundary at sequence resolution and at record resolution, with the
   removing potential forced to `1/μ`. `[THEOREM at sequence level,
   MEASURED at record level]`. **This is not a flatness result** — see
   claim 3.
3. **The twist is NOT a coboundary of any committed state abstraction
   coarser than the record**: MULT, STATE, PORT and MENU all return a
   non-zero obstruction by both routes, on a carrier gated to be
   non-degenerate. `[MEASURED]`, `(A,B) d ≤ 4`.
4. **The coarsest quotient on which the connection descends is the
   weighted-menu partition** — an identification that is **definitional**
   (claim 4's content is not that it exists) — and the coarsest weighted
   **congruence**, computed independently by partition refinement, closes
   exactly the same defective squares on all six full arms. On the menu
   quotient the closing defective squares are **self-loops** with
   holonomy `≠ 1`, which no potential removes. `[MEASURED]`; the
   gauge-invariance of a self-loop is the argument, and the self-loop
   count itself is definitional.
5. **A defective square whose two orders have different weighted menus
   closes in no DESCENT quotient**, and in none of four strictly weaker
   notions of descent either (0 of 44 under each). Hence the census
   splits into curvature-type and descent-obstruction-type, 44 + 44 at
   `(A,B) d ≤ 4` — a split that is invariant under CTL-ORDER, unlike the
   value and kind labels of the two halves. `[THEOREM + MEASURED]`.
6. **Normalisation does not remove the transport twist**: the
   intermediate mass ratio is 1 on every raw-defective square of both
   anchor arms, and the normalisation defect is supported on a disjoint
   set. `[MEASURED]`.
7. **Every defective square is register-overlapping on an ACTOR
   register**, in every arm run. `[MEASURED]`.
8. **The reversal acts by inversion on `r`** — an algebraic identity of
   the definition of `r`, so the transport log-holonomy is purely
   reversal-odd **as a statement about `log r`**. `[IDENTITY]`. No claim
   whatever is made, from this, about the reversal-even channel: see
   claim 11.
9. **No unimodular holonomy is exhibited anywhere in this unit**, and a
   rational-valued holonomy's only possible unimodular content is `−1`,
   which is realised nowhere; the scalar `U(1)` question is therefore
   settled a priori by D2. The order-dual carrier is empty at this scope
   in the strong sense: **0 of 304** linear extensions of the opposite
   posets of the 176 defective endpoints are admissible, on a grammar
   which is **not** reversal-blocking (2,196 of 3,092 closed-square
   endpoints reverse-admissible). The i-twist restores v7's
   dual-conjugation law because for the twisted form that law **is** the
   inversion identity, so it is content-free as evidence.
   `[EXACT + CONTROLLED]`.
10. **`J = 1 ⟹ r = 1`, with zero exceptions on 8,600 closed squares
    across three arms, and `J = 0` on all 1,060 defective squares** —
    a non-constant **reversal-even** invariant, supplied by the
    substrate, that is not a relabelling of the register invariant of
    claim 7. `[MEASURED]` on `(A,B) d ≤ 4`, `(A,B,C) d ≤ 3` and
    `(A,B) d ≤ 5` **only**. **Not a theorem and not licensed as one.**
11. **Not claimed:** that the reversal-even channel is empty (it is not —
    claim 10); that `J = 1 ⟹ r = 1` holds at greater depth, at more
    actors, or in general; that anything found here is the v7 phase
    (correspondence ≠ identity; D4.1 shows the correspondence is a change
    of variables); that a measure exists on these loops (D70's bound is
    open); anything at infinite volume or outside the declared families,
    depths and pools; that the AB-only/BA-only split or the unpaired
    spectrum are substrate facts (CTL-ORDER) — **nor this unit's own
    unseen-half spectrum and kind census**, which CTL-ORDER transposes;
    the count of non-trivial basis cycles, which is forest-dependent;
    that the descent-obstruction half is or is not removable by anything;
    and **not** that the corpus has no object for it — D65 §3.1's repair
    cone computes the same criterion under a different functor (see
    residue 1).

---

## 5. Residues, ranked

1. **The descent-obstruction half has no formalism AT TRANSPORT SCOPE,
   and none that quantifies over quotients.** 44 of 88 at the anchor
   window, and a majority at three actors. It is neither a coboundary nor
   a curvature: the two orders are not identifiable by any quotient on
   which the connection lives, and four weakenings of "descent" do not
   help. **Re-scoped at round 1 (MODERATE 6):** the first pass wrote "the
   corpus has no object for this", and that is too strong. **D65 §3.1
   computes the same object** — two linear systems over `Q`, "repairs the
   defect" and "descends to the record", reporting at `D = 4` that
   **152 of 403** repair rows are not implied by record-constancy,
   *exactly the rows whose two corners carry different records*, with the
   transverse dimension counted (313 record-constant, 205 in the
   intersection) and a positive witness that annihilates all 403 square
   identities while still failing to descend. That is the same criterion
   under a different functor at a different scope, and D65's **residue
   3** — the record functor is a *choice*; a coarser functor breaks the
   containment — is the standing warning this dichotomy should be read
   against. The sharpened D75 question is therefore: **is there a
   formalism for a defect that is visible only after descent is
   abandoned** — and does D65's repair-cone machinery reach transport
   scope? It is the same shape as D72's residue 3 (the `±∞` half-open
   squares), which also survives here and is also unformalised — at
   `(A,B) d ≤ 6` there are **4,608** half-open squares.
2. **`J` is measured, not explained, and not tested where it matters
   most.** It holds without exception on `(A,B) d ≤ 4`, `(A,B,C) d ≤ 3`
   and `(A,B) d ≤ 5`. Whether `J = 1 ⟹ r = 1` survives `(A,B) d ≤ 6`,
   three and four actors, and the asymmetric sub-grammars is **the
   successor's first line**, and the referee said so. Two further
   questions sit behind it: *why* does reverse-admissibility of both
   endpoints force flatness, and is `J` the shadow of a genuine
   even-channel object (a real-valued reversal-even functional) rather
   than merely a predicate?
3. **The carrier's window dependence is unexplained.** The fraction the
   menu quotient sees runs 50 % / 0 % / 63 % / 24 % / 65 % / 26 % across
   the six arms with no evident law. Whether it converges, and to what,
   is open.
4. **`⟨2,3⟩` is exhibited but not derived.** The four values are
   `1/2, 2/3, 3/2, 2` and the mechanism D72 identified — a menu
   denominator that doubles when arbitration precedes delivery — is a
   plausible account of `2^{±1}` but not of `3^{±1}`. A mechanism account
   of the `2/3` squares (only 2 at the anchor window, 1,114 at `d ≤ 6`,
   12 at the new four-actor pool) is missing. The four-actor pool makes
   this sharper, not softer: a new pool with new menu masses `{4, 9/2}`
   produces the *same* four values.
5. **The `(p,d)` and `(d,p)` defective kinds first appear at depth 6**
   and have not been analysed at all.
6. **D6.1's failure has no mechanism either.** The oriented ratio is
   above 1 on a small, stable-looking minority (8 / 344 / 24 / 2). What
   distinguishes those squares is not known.
7. **The `ABC3` zero.** At three actors and depth 3 the carrier sees none
   of the 12 defects; one depth out it sees 132 of 540. Whether the
   three-actor carrier is genuinely later-starting or the `d ≤ 3` window
   is simply too shallow to contain a menu coincidence is open. The
   four-actor pool shows the same shape (24 defects at `d ≤ 3`, 1,728 at
   `d ≤ 4`), which suggests a window effect rather than an actor effect.
8. **L6a still deserves a receipt** (inherited from D72 residue 2,
   untouched here).

---

## 6. What this unit does *not* touch

No committed file was edited. No paper, no LOG entry, no pin, no earlier
note. The three deliverables are
`v10/code/d74_transport_holonomy_exact.py`,
`v10/data/d74_transport_holonomy_exact.out`, and this note.

**Routed to the principal, not applied:**

* the **status** (not the correctness) of D72's rows T6.1/T6.2 and its
  DELTA — the spectrum multiplicities and the 28/12 half-open split are
  enumeration-orientation readings (§3(a)). D72's **licensed claims are
  untouched by CTL-ORDER**; the earlier draft's routing against licensed
  claim 7 was mis-addressed and is withdrawn;
* **LOG #494's** four clauses that the round found wanting: (i) "the
  order-dual IS NOT DEFINED here (0/176)" → the order-dual **is** defined
  (poset reversal); what is measured is that the dual poset has **no
  admissible realisation**, 0/304; (ii) "passes on 500 adversarial
  rationals" as the evidence that the i-twist is content-free → cite the
  **argument** (`exp(i·)` turns any odd real into a conjugating
  unimodular), not the control; (iii) "0-for-4 at the grammar's native
  addresses" → this address was scored by a predicate with no positive
  branch until OUT.1; (iv) "the even channel is empty / the mirror of v7"
  → withdrawn, see §3(k).

**Nothing here is Lean** — the pin bet nothing. On phase location the
campaign remains **0-for-4 in the scalar odd sector**; the
enrichment-fork framing stands, and stands honestly: the **U(1) question
at record-category / transport scope is the one address this unit did not
probe**, because the object it would have to be probed on is D71b's
record order under poset reversal, and this unit worked at transport
scope where that carrier is empty. That is the fork's live address, not a
closed one.

---

## 7. The round-1 ledger

Review: `v10/reviews/d74-round1-hostile-review.md`, frozen 2026-07-27.
**VERDICT REVISE, 5 MAJOR / 6 MODERATE / 6 MINOR.** Every item is
adjudicated and applied. The referee reproduced every anchor and every
headline number from its own instrument, could not break either
structural theorem, and strengthened both.

| item | finding | disposition |
|---|---|---|
| **MAJOR 1** | C0.1, D1 and D4.1 are identities of their own definitions, counted as independent evidence | **UPHELD.** All three tagged `[NO INDEPENDENT INFORMATION]` (with A3.3 and the join-closure remark, and C0.2 and D3.1 already tagged): **7 corollaries, 41 independent passes** (was 3 and 38). D1 restated as a one-line lemma; D4.1's tautological 500-rational control replaced by a discriminating one |
| **MAJOR 2** | the outcome predicate cannot return TH-III; a three-way pin decided by a two-way test | **UPHELD.** The selector is now a function with all three branches exercised on constructed input (**OUT.1**). Delivered outcome: **TH-II with `J`** |
| **MAJOR 3** | the reversal-EVEN channel is not empty; the receipt's own D5 arm computed the raw material and never looked at the complement | **UPHELD — THE ROUND'S FIND, credited to the referee.** `J` gated at **D9.1**: `J = 1 ⟹ r = 1` on **8,600** squares across three arms, **0** exceptions; `J = 0` on all **1,060** defective squares; **793** register-overlapping `J=1` squares and **168** register-disjoint `J=0` squares show it is not the register invariant. "The even channel is empty / the mirror of v7" **struck**; restated as the **scalar odd (U(1))** sector being empty |
| **MAJOR 4** | "D71b's linear-extension carrier" is a mis-citation; the arm builds neither carrier it names; `linear_extensions` required and never called | **UPHELD.** Attribution corrected (D71b = record order under poset reversal; linear extensions = D72 claim 2). Arm rebuilt at **D5.2**: **0 of 304** linear extensions of the opposite posets admissible, all 304 admissible forwards. The negative survives **at greater strength** |
| **MAJOR 5** | "no quotient graph can carry it" is false — MULT closes all 44; the "descent" qualifier missing in three places | **UPHELD.** Qualifier inserted everywhere; **A3.5** gates MULT closing **88/88** including **44/44** of the invisible half; residue 1 re-posed |
| **MODERATE 1** | the §3(a) correction is mis-addressed to D72's licensed claim 7 | **UPHELD.** Re-addressed to rows T6.1/T6.2 and the DELTA; D72's licensed claims noted as surviving CTL-ORDER untouched |
| **MODERATE 2** | CTL-ORDER applied to the parent, not to this unit's own dichotomy headline | **UPHELD.** **A3.2** rewritten to the invariant form (44+44, unordered class `{1/2 ≡ 2}: 44`); the orientation-dependent spectrum and kinds reported as readings |
| **MODERATE 3** | §3(e)'s "correction" is D65's own committed residue 2; `⟨5/4⟩` is D72's, not D65's | **UPHELD.** Downgraded to a **confirmation** of D65 residue 2 at a scope D65 explicitly refused; `⟨5/4⟩` re-attributed to D72 claim 6 |
| **MODERATE 4** | the coarsest-quotient "theorem" is definitional; A3.3's self-loop is a tautology of the exchange graph | **UPHELD.** Both labelled; the choice of descent notion declared; **A3.4** runs the weaker notion the unit did not choose (and three more): **0 of 44** each |
| **MODERATE 5** | "eight scopes" = two nested chains + two sub-grammars, none beyond three actors; the referee ran the missing scope | **UPHELD, and the referee's scope adopted.** Scopes restated honestly; **A1.3** adds `(A,B,C,D)` at depths 3 and 4 — 1,728 defective squares, new menu masses `{4, 9/2}`, value set still `{1/2, 2/3, 3/2, 2}`, **no new prime**. The group claim now rests on **four mutually non-nested evidence pools** — the two-actor chain, the three-actor chain, the two asymmetric sub-grammars, and the four-actor pool (three actor pools in all) |
| **MODERATE 6** | "no corpus formalism handles the second kind" is too strong — D65 §3.1's 152/403 split computes the same object | **UPHELD.** Residue 1 re-scoped to "no formalism **at transport scope**, and none that quantifies over quotients", with D65 §3.1 cited and D65 residue 3 carried as the standing warning |
| **MINOR 1** | §1 D6.1 says "every ... of both anchor arms"; 4 of 88 are unorientable | fixed: **84 of 84 orientable**, aligned with §3(f) |
| **MINOR 2** | C2.1's "(obstruction 88 at every one)" silently sums two columns | fixed: the quantity is named (independent cycles + defective self-loops) and both columns are cited |
| **MINOR 3** | D3.1's predicate is the bare constant `True`, plus dead code | fixed: predicate now evaluates the event-multiset identity on 3,100 squares; dead code deleted |
| **MINOR 4** | `linear_extensions` required by the AST pass, never called | fixed: it is what D5.2 runs on |
| **MINOR 5** | the title leads with "the census splits exactly in half"; the hedge arrives later | fixed: the window-dependence hedge is now above the headline, and the split is not in the title |
| **MINOR 6** | LOG #494 cites the 500 rationals as the evidence | the control is rebuilt; the LOG clause is **routed to the principal** (§6) — this unit edits no LOG entry |

**One incidental review number, checked and re-sourced.** MAJOR 5 writes
"8 multi-valued labelled edges **out of 3,391**". The 8 is right and
reproduces; 3,391 is not a labelled-edge count — it is the receipt's own
**`up rank`** column for the MULT rung (`.out:185`), i.e. the independent
cycles of the MULT up-graph. The MULT rung carries **1,288** labelled
edges on 3,968 up-moves. Nothing in the finding depends on it; the
denominator is corrected in §3(d). Every other number in the review
reproduced exactly from an independent rebuild before it was gated.

**What the round did not break.** Every anchor; the whole six-rung ladder
column for column; 113 menu classes and the 185-class congruence; the
44 + 44 dichotomy; the group `⟨2,3⟩`; the sign-definiteness
self-correction (f); CTL-ORDER; CTL-TAMPER's ability to fail;
CTL-FLAT; the determinism probe and the exit protocol; A2.1's register
profile; the C1 orthogonality; and the scope discipline of §4. Two of the
referee's own attacks came back as **strengthenings**: PORT closes
exactly the same 44 as MENU *as sets*, and the dichotomy survives four
weakenings of descent.
