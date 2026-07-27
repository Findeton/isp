# D74 — result: **TH-II. The transport twist is GENUINE MODULUS CURVATURE with NO PHASE — but only half of it is curvature at all.** The carrier exists and is constructed (the coarsest descent quotient = the weighted-menu partition, confirmed by the coarsest weighted congruence); the group is `⟨2,3⟩`, the FULL 3-smooth group, free abelian of rank 2, stable across eight scopes and two asymmetric sub-grammars; the twist is **not removable** on the carrier and **not** D65's coboundary — normalisation leaves every defective square exactly where it was. The odd sector is **empty**, and the search's own best candidate — a substrate-supplied orientation under which the defect is sign-definite — **fails one depth out from the anchor window**.

**Status: GREEN-UNREVIEWED, 2026-07-27.** No hostile round has been run
on this unit. Pin `v10/note-d74-transport-holonomy-pin.md` (STRICT,
frozen and committed before any code was written). Parents: D72 TERMINAL
(`note-d72-weld-result.md` — the census this unit anchors on), D65
(`note-d65-descent-conditions-result.md`), D71b
(`note-d71b-holonomy-phase-identity.md`), D64
(`note-d64-cocycle-result.md` — the coboundary-first discipline and the
C7 idiom), D73 (`note-d73-even-gram-result.md` — the generic-geometry
requirement). Receipt `v10/code/d74_transport_holonomy_exact.py`, output
`v10/data/d74_transport_holonomy_exact.out` — run from the repository
root, **exit 0**, **41 PASS / 0 FAIL** of which **3 carry no independent
information and are labelled as such** (38 independent-evidence passes),
**282 s wall clock** against the pin's ~25 min budget. Re-run at
`PYTHONHASHSEED=7`: **output byte-identical apart from timings and the
echoed seed** (0 differing lines).

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
is reserved for those anchors and was not reached.**

Where this note and the receipt disagree, **the receipt is
authoritative** (LOG #477's standing rule).

---

## 0. The one-paragraph answer

D72 handed over three questions: what carries the transport holonomy at
record level, is there an odd-sector `U(1)` part, and is the defect a
coboundary. **All three are answered, and the third had to be re-posed
before it could be.** The naive coboundary test on this object **cannot
fail**: the product weight `μ` is a global potential — `r =
μ(h·e_A·e_B)/μ(h·e_B·e_A)` on **3,100 of 3,100** closed squares of the
anchor arms, not just on D72's single witness — and the sequence layer is
a tree, so every connection on it is a coboundary and the removing gauge
is forced to be `1/μ`, which sets every weight to 1. Removability is only
informative **relative to what the potential may see**, and relative to
that there is a sharp **threshold**: the twist is a coboundary exactly on
the abstractions where `μ` itself descends — the sequence and the
**record** — and on none coarser. **That is a structural explanation of
D72's blindness theorem**: the record functor is the coarsest committed
identification that keeps `μ` single-valued, and keeping `μ`
single-valued is exactly what forbids a defective square from closing.
Go one step coarser and the holonomy appears. The coarsest quotient on
which the connection descends is canonical and is **not a search**: the
weighted-**menu** partition (descent is closed under joins, so a coarsest
descent quotient exists and is unique), and the coarsest weighted
**congruence**, computed by partition refinement to a fixed point, closes
**exactly the same** defective squares on every arm. On it the defective
squares are **self-loops** with holonomy `≠ 1`, and a self-loop's
holonomy is gauge-invariant outright: **not removable, and this verdict
could have gone the other way**. But the carrier does not carry all of
it. A descent quotient may identify two histories only if their weighted
menus agree, so a square whose two orders have different menus **cannot
close in any descent quotient whatsoever** — and at `(A,B) d ≤ 4` the
census splits **exactly in half**: 44 squares of genuine connection
curvature, 44 of a **descent obstruction** that no quotient graph can
carry. The group is `⟨2,3⟩` — free abelian of rank 2, the full group of
3-smooth positive rationals, computed as an integer exponent lattice —
and it does not move from depth 4 to depth 6, from two actors to three,
or under either asymmetric sub-grammar, while the defect count runs from
88 to 14,736. It is **not** D65's object: normalising by the menu mass
leaves every one of the raw-defective squares **exactly unchanged**
(the intermediate mass ratio is identically 1 there) and adds a
**disjoint** family of new defects at the mass ratios. And the odd sector
is **empty**: reversal is exactly inversion, so the log-holonomy is
purely odd and has **no even part at all** — the mirror image of v7's
amplitude, which puts the modulus in the even channel and the phase in
the odd one. **TH-II fires.**

---

## 1. What each arm returned

### TH-C — REMOVABILITY (run and reported first, per the pin and D64)

| gate | result |
|---|---|
| **C0.1 the vacuity lemma** | `r = μ(h·e_A·e_B)/μ(h·e_B·e_A)` on **3,100/3,100** closed squares of the two anchor arms, exactly. D72 checked this identity on **one** witness (T6.4) and drew no conclusion from it. It is the whole removability question at history resolution |
| **C0.2 therefore the naive test carries no information** | the sequence layer is a tree, so `H¹ = 0` there for v8 p1:77's reason; the potential is unique up to a constant per component, so `1/μ` is **the** removing gauge and it gauges every weight to 1. *Labelled: no independent information* |
| **C1 the D65 test** | `r = M(h·e_B)/M(h·e_A)` holds on **1,254 of 1,546** (`AB4`) and **1,410 of 1,554** (`ABC3`) — and on **none** of the defective squares. The intermediate mass ratio restricted to the raw-defective squares is `{1: 88}` and `{1: 12}`: **normalisation moves them not at all**. It adds a disjoint family: `AB4` normalised spectrum `{4/5: 114, 1: 1254, 5/4: 90}` **plus** the untouched `{1/2: 70, 2/3: 2, 3/2: 6, 2: 10}` |
| **C2.1 the threshold, route 1** (potential propagation, obstruction count) | coboundary at **SEQ** and **REC** (obstruction 0); **NOT** at MULT, STATE, PORT, MENU (obstruction 88 at every one). `μ` descends on `3969/3969` and `2477/2477`, and on `514/578`, `84/125`, `24/65`, `44/113` |
| **C2.2 the threshold, route 2** (relabelled recount — D64's C7 idiom on `R⁺`) | the spanning-forest potential propagated over each quotient's own up-graph, the whole census re-run with the gauged weights `q' = q·φ(α(h·e))/φ(α(h))`: **survivors 0 exactly where the obstruction is 0**, rung for rung (`0, 0, 88, 88, 96, 180`). The direction of this gauge is the receipt's own tripwire — getting it backwards squares the defect instead of cancelling it, and the SEQ rung, where `φ` is `μ` exactly, is what caught it |
| **C2.3 anti-vacuity** | at SEQ the exchange graph is a **perfect matching** — 1,546 edges on 3,092 nodes, **cycle rank 0**. The coarse rungs carry 134 / 80 independent cycles and 88 defective self-loops, so a flat answer was available there and was not returned |
| **C2.4 the `σ`-port rung** | the pin's prediction upheld: PORT (the per-actor option data the weights actually read) closes **44 of 88**, not all — D62's machinery at transport scope does not carry it |

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
| **A2.1 the classification** | **every** defective square is register-overlapping and the overlap is **always on an ACTOR register**, never on a version register alone — `{actor: 88}`, `{actor: 12}`, `{actor: 960}`, `{actor: 334}`. Against D72's T2.3b (a square closes at record level exactly when register-disjoint) this makes the blindness **exact, not statistical** |
| **A3.1 the carrier** | the coarsest descent quotient — the weighted-menu partition — closes a non-zero number of defective squares on **five of the six** full arms; the coarsest weighted **congruence** (partition refinement, 4–6 rounds to a fixed point) closes **exactly the same** defective squares on **all six** |
| **A3.2 the dichotomy theorem** | `AB4`: **44 curvature-type + 44 descent-obstruction-type = 88**, and the split is kind-clean — every invisible one is an `(r,d)` pair at the single value `1/2`, while the visible half carries all five kind pairs and the whole spectrum |
| **A3.3 not removable on the carrier** | the closing defective squares are **self-loops** at a single menu class carrying `{1/2: 26, 2: 10, 2/3: 2, 3/2: 6}`; a self-loop's holonomy is gauge-invariant outright, so **no** potential on the carrier removes them. Non-unit self-loops on the six arms: 44, 0, 604, 132, 218, 60 |

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
| **cumulative** | 25,434 non-unit squares over the eight scopes | `{1/2, 2/3, 3/2, 2}` | **`⟨2,3⟩` = the FULL group of 3-smooth positive rationals, free abelian of rank 2, index 1 in `Z²`** |

**B.1** the value set does not move: every scope's set is contained in
the anchor window's, and the cumulative set **equals** it, while the
counts run 88 → 14,736. **B.2** the group is computed as an integer
exponent lattice (Hermite reduction on the prime valuations, basis
`[[-1,0],[0,1]]`, index 1), not read off four values by eye; it is
**rank 2 and not cyclic**, where D65's `⟨5/4⟩` is rank 1 on primes
`{2,5}`. **B.3** the carrier's **own** holonomy group — the group of the
menu quotient's loops, the basis-independent object — is also `⟨2,3⟩`;
the count of non-trivial basis cycles is forest-dependent and is **not**
licensed as a number.

### TH-D — THE ODD SECTOR

| gate | result |
|---|---|
| **D1 reversal is exactly inversion** | `r(reversed) = 1/r` on **1,546/1,546** closed squares, gap exactly 0 on Fractions. So `log r` is **purely odd** and the reversal-**even** part is **identically zero**. Read against `QUOTES['Ldual']` this is the striking half: **v7's amplitude puts the modulus in the EVEN channel and the phase in the ODD one; the transport holonomy puts its modulus in the ODD channel and leaves the even one empty.** The two objects do not occupy the same slots |
| **D2 the unimodular part** | every committed weight is a positive rational, so every holonomy is; the only positive rational of modulus 1 is 1. **A `U(1)` part of a rational-valued holonomy could only ever be the sign `−1`** — the search reduces exactly to a search for a canonical sign, and `−1` is realised nowhere |
| **D3.1 the label-local no-go** | any connection whose value depends only on the **event label** has trivial holonomy on **every** exchange square: the two sides use the same two events, each once, so a label-indexed cochain cancels. A phase `e^{iθ(e)}` on events contributes nothing. A non-trivial phase must be **history**-dependent, exactly as `q(e\|h)` is. *Labelled: no independent information — but it says where not to look* |
| **D4.1 the i-twist correspondence, controlled** | in the real form `L = r`, v7's law `rev(L) = conj(L)` fails on **exactly the 88** defective squares (for reals, conj is the identity, so the law demands `r = 1/r`). The twist `L' = e^{i log r}` restores it on every square — **and on 500 adversarially drawn positive rationals with no connection to the substrate**. `exp(i·)` turns any odd real into a conjugating unimodular: the i-twist is a **change of variables, not a discovery**. D72's T3.CTRL made the same point about `L_dual`'s zero |
| **D5.1 the order-dual arm** | **0 of 176** reversed endpoint sequences of the defective squares are themselves admissible histories, so **0 of 88** defective squares have an in-family dual square. D72's T1.4 showed `*` and the transport reversal coincide only on 2-event histories; every defect here sits at total depth ≥ 3. **D71b's carrier is real and it is empty at this scope** |
| **D6.1 the canonical orientation — and its failure** | a substrate-supplied orientation does exist (order each mixed-kind square so the **delivery is second**) and under it **every** defective square of **both anchor arms** lands strictly **below 1**: acting before delivering always suppresses the joint weight. **It does not survive the wider arms.** `(A,B) d ≤ 5`: `{<1: 868, >1: 8}`; `(A,B) d ≤ 6`: `{<1: 7116, >1: 344}`; `(A,B,C) d ≤ 5`: `{<1: 13464, >1: 24}`; ASYM-1: `{<1: 332, >1: 2}`. Sign-definite on `AB4`, `ABC3`, `(A,B,C) d ≤ 4`, ASYM-2 only |
| **D7.1 the asymmetric substrates** | same `U(1)` verdict: `R⁺`-valued, same group `⟨2,3⟩`, purely odd, no unimodular part — **breaking the actor symmetry does not create a phase**. It does independently confirm D6.1's break |
| **D8 the verdict** | **no orientation-sensitive residue exists on this carrier.** Everything invertible under reversal; nothing conjugating |

---

## 2. The controls

| control | what it shows |
|---|---|
| **CTL-FLAT** | the d42b3 closed grammar through **this** receipt's own census code returns `{1: 403}` and **no** half-open square — the pipeline does not manufacture defects |
| **CTL-TAMPER** | multiplying **one** committed step weight by `3/2` moves the census (88 → 94 non-unit). Unlike D72's T2.NC — which perturbed one edge of an exact gradient and therefore **could not fail** — this control can fail |
| **CTL-ORDER** | **a control the corpus did not run, and it bites.** See §3(a) |
| **CTL-DET** | forward and reversed spanning-forest builds agree on nodes, components, cycle rank, obstruction count and the holonomy value **set**; D72's lesson that the count of non-trivial **basis** cycles is forest-dependent is carried, and that count is not licensed |
| **anti-vacuity (C2.3)** | the removability test at the coarse rungs is not a test on a forest — the sequence-level exchange graph **is** a forest (a perfect matching), which is precisely why C0's verdict there is empty |

---

## 3. Findings, including the ones that correct this unit's own first
instincts

**(a) D72's spectrum split and its half-open split are ENUMERATION-
ORIENTATION readings, not substrate facts.** `[MEASURED]`. Re-running the
identical census with the candidate list traversed in the opposite order
leaves the closed / half-open / both-blocked **totals** and the defect
**count** invariant, and leaves the multiset of **unordered** value
classes `{r, 1/r}` invariant (`{1/2: 80, 2/3: 8, 1: 1458}` both ways) —
but it **transposes** the spectrum to `{1/2: 10, 2/3: 6, 3/2: 2, 2: 70}`
and the half-open split from `(28, 12)` to `(12, 28)`. The square census
enumerates unordered pairs and calls the first one "A"; which of the two
orders is `AB` is an artefact of `candidates_for`'s output order. **D72's
committed values are correct as printed and are not being contradicted;
what changes is their STATUS.** `{1/2: 70, …, 2: 10}` and `AB-only 28,
BA-only 12` (licensed claim 7) should be restated as the totals `80 + 8`
and `40`, or else stated together with the orientation convention that
produced them. This is routed to the principal, not applied — D72 is
TERMINAL and this unit edits nothing.

**(b) The removability question, as the corpus had been posing it, cannot
fail — and the fix is a threshold, not a yes/no.** `[THEOREM, gated]`.
C0.1/C0.2. This is D72's own MAJOR 3 (`T2` is a corollary of `T1.8`) one
level up, and it was very nearly repeated here: the first thing a
D64-disciplined receipt wants to do is propagate a potential over the
exchange graph and report the obstruction, and at sequence level that
graph is a **perfect matching** whose obstruction is 0 for reasons that
have nothing to do with physics. What is informative is **where** in the
abstraction ladder the coboundary property dies, and it dies immediately
below the record functor.

**(c) The record functor sits exactly at the threshold, and that explains
D72's blindness theorem instead of restating it.** `[MEASURED]`. `μ` is
class-constant on records (D72's own anchor) — so `1/μ` is a per-record
potential and the twist is a record-level coboundary. But a potential
that is single-valued on classes is exactly what makes a square's two
orders land in **different** classes when `r ≠ 1`. **The instrument is
blind because it is fine enough to be flat.** Any coarser committed
abstraction breaks `μ`'s single-valuedness and the holonomy appears.

**(d) Half the transport defect is not curvature at all.** `[THEOREM +
MEASURED]`. A descent quotient can only identify histories with equal
weighted menus; a defective square whose two orders have different menus
therefore closes in **no** descent quotient. At `AB4` that is exactly 44
of the 88, all of them `(r,d)` pairs at `1/2`. **This is a new object in
the corpus**: not a coboundary, not a curvature, a **descent
obstruction** — and the exchange square is the only instrument that sees
it. The proportion is strongly window-dependent (44/88, 0/12, 604/960,
132/540, 218/334, 60/228).

**(e) The transport twist and D65's mass twist are orthogonal.**
`[MEASURED]`. Normalising to the process's own conditional kernel
multiplies each square ratio by `M(h·e_B)/M(h·e_A)`, and that factor is
**identically 1** on every raw-defective square in both anchor arms. The
normalisation defect lives on a disjoint set of squares and its values
are mass ratios. At two actors those are D65's committed `{4/5, 5/4}`
(from masses `{2, 5/2}`, which reproduce D65's set exactly); **at three
actors they are not** — the menu masses are `{3: 3100, 7/2: 288, 19/4:
36}` and the normalised defects are `{6/7: 84, 7/6: 48}`. **D65's
committed `{4/5, 5/4}` is a two-actor statement** and should not be
carried as the shape of the mass twist in general.

**(f) The odd sector's most attractive candidate died at depth 5.**
`[MEASURED]`, self-corrected. The kind-canonical orientation (delivery
second) makes the defect sign-definite on **both** anchor arms — 84 of 84
orientable squares strictly below 1 at `AB4`, 12 of 12 at `ABC3` — and it
is exactly the transport-scope echo one would want of D72's unexplained
sign-definiteness of `O` (T3.B2). It is **false** at `(A,B) d ≤ 5` (8
squares above 1), at `(A,B) d ≤ 6` (344), at `(A,B,C) d ≤ 5` (24) and on
ASYM-1 (2). **The breakage is a depth effect first and a symmetry effect
second** — D73's requirement landed, but the deeper symmetric window
would have caught it on its own. Had this unit run only the pin's
inherited window it would have published a false headline.

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

---

## 4. Licensed claims — no wider than the fixtures run

1. **On the d42b1 transport grammar**, at `(A,B)` depths 4, 5 and 6, at
   `(A,B,C)` depths 3, 4 and 5, and on the two declared asymmetric
   sub-grammars, the closed exchange squares have `dP_AB/dP_BA` in
   `{1/2, 2/3, 3/2, 2}` and the multiplicative group generated is
   **`⟨2,3⟩`, free abelian of rank 2, the full group of 3-smooth positive
   rationals**, with prime support `{2,3}` and index 1 in `Z²`.
   `[MEASURED]`, exact arithmetic, on those windows.
2. **`r = μ(h·e_A·e_B)/μ(h·e_B·e_A)` on every closed square of both
   anchor arms** (3,100/3,100). Hence the transport connection is a
   coboundary at sequence resolution and at record resolution, with the
   removing potential forced to `1/μ`. `[THEOREM at sequence level,
   MEASURED at record level]`. **This is not a flatness result** — see
   claim 3.
3. **The twist is NOT a coboundary of any committed state abstraction
   coarser than the record**: MULT, STATE, PORT and MENU all return a
   non-zero obstruction by both routes, on a carrier gated to be
   non-degenerate. `[MEASURED]`, `(A,B) d ≤ 4`.
4. **The coarsest quotient on which the connection descends is the
   weighted-menu partition** (descent is join-closed, so it exists and is
   unique), and the coarsest weighted **congruence** closes exactly the
   same defective squares on all six full arms. On the menu quotient the
   closing defective squares are **self-loops** with holonomy `≠ 1`,
   which no potential removes. `[CONSTRUCTED + MEASURED]`.
5. **A defective square whose two orders have different weighted menus
   closes in no descent quotient.** Hence the census splits into
   curvature-type and descent-obstruction-type, 44 + 44 at `(A,B) d ≤ 4`.
   `[THEOREM + MEASURED]`.
6. **Normalisation does not remove the transport twist**: the
   intermediate mass ratio is 1 on every raw-defective square of both
   anchor arms, and the normalisation defect is supported on a disjoint
   set. `[MEASURED]`.
7. **Every defective square is register-overlapping on an ACTOR
   register**, in every arm run. `[MEASURED]`.
8. **The reversal acts by exact inversion on all 1,546 closed squares of
   the anchor arm**, so the transport log-holonomy is purely
   reversal-odd with zero even part. `[EXACT]`.
9. **No unimodular holonomy is exhibited anywhere in this unit**, and a
   rational-valued holonomy's only possible unimodular content is `−1`,
   which is realised nowhere. The i-twist restores v7's dual-conjugation
   law identically **and** on adversarial input, so it is content-free as
   evidence. `[EXACT + CONTROLLED]`.
10. **Not claimed:** that anything found here is the v7 phase
    (correspondence ≠ identity; D4.1 shows the correspondence is a change
    of variables); that a measure exists on these loops (D70's bound is
    open); anything at infinite volume or outside the declared families,
    depths and pools; that the AB-only/BA-only split or the unpaired
    spectrum are substrate facts (CTL-ORDER); the count of non-trivial
    basis cycles, which is forest-dependent; that the descent-obstruction
    half is or is not removable by anything (no formalism in the corpus
    currently handles it — residue 1).

---

## 5. Residues, ranked

1. **The descent-obstruction half has no formalism.** 44 of 88 at the
   anchor window, and a majority at three actors. It is neither a
   coboundary nor a curvature: the two orders of the square are not
   identifiable by any quotient on which the connection lives. The
   corpus has no object for this. It is the natural D75 question, and it
   is the same shape as D72's residue 3 (the `±∞` half-open squares),
   which also survives here and is also unformalised — at `(A,B) d ≤ 6`
   there are **4,608** half-open squares.
2. **The carrier's window dependence is unexplained.** The fraction the
   menu quotient sees runs 50 % / 0 % / 63 % / 24 % / 65 % / 26 % across
   the six arms with no evident law. Whether it converges, and to what,
   is open.
3. **`⟨2,3⟩` is exhibited but not derived.** The four values are
   `1/2, 2/3, 3/2, 2` and the mechanism D72 identified — a menu
   denominator that doubles when arbitration precedes delivery — is a
   plausible account of `2^{±1}` but not of `3^{±1}`. A mechanism
   account of the `2/3` squares (only 2 of them at the anchor window,
   1,114 at `d ≤ 6`) is missing.
4. **The `(p,d)` and `(d,p)` defective kinds first appear at depth 6**
   and have not been analysed at all.
5. **D6.1's failure has no mechanism either.** The oriented ratio is
   above 1 on a small, stable-looking minority (8 / 344 / 24 / 2). What
   distinguishes those squares is not known.
6. **The `ABC3` zero.** At three actors and depth 3 the carrier sees none
   of the 12 defects; one depth out it sees 132 of 540. Whether the
   three-actor carrier is genuinely later-starting or the `d ≤ 3` window
   is simply too shallow to contain a menu coincidence is open.
7. **L6a still deserves a receipt** (inherited from D72 residue 2,
   untouched here).

---

## 6. What this unit does *not* touch

No committed file was edited. No paper, no LOG entry, no pin, no earlier
note. The three deliverables are
`v10/code/d74_transport_holonomy_exact.py`,
`v10/data/d74_transport_holonomy_exact.out`, and this note. The
corrections this unit implies for **D72's licensed claim 7** (the
orientation status of the spectrum and the half-open split, §3(a)) and
for **D65's `{4/5, 5/4}`** (a two-actor statement, §3(e)) are **recorded
here and routed to the principal**, not applied. Nothing here is Lean —
the pin bet nothing, and the campaign remains 0-for-4 on
phase-location intuitions.
