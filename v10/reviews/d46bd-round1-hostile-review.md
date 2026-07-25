# D46b + D46d — round 1, hostile review (one round, two units)

**Reviewer:** independent referee (fresh session; no build context).
**Date:** 2026-07-24.  **Objects under review (both GREEN-UNREVIEWED,
first round):**

- **UNIT 1 — D46b (LOG #384):** `v10/note-d46b-martin-at-transport.md`,
  `v10/code/d46b_martin_transport_exact.py`,
  `v10/data/d46b_martin_transport_exact.out`.
- **UNIT 2 — D46d (LOG #386):** `v10/note-d46d-typicality.md`,
  `v10/code/d46d_typicality_exact.py`,
  `v10/data/d46d_typicality_exact.out`.

Nothing in this review edits a committed file.  Every number below was
recomputed by the referee from the committed `d42b1`/`d42b3` layers
unless explicitly marked as a citation check.  The sibling round
(`v10/reviews/d46ac-round1-hostile-review.md`) was read first; its four
failure patterns — (i) prose asserting more than the gates deliver,
(ii) claims surviving in the receipt after the note retracts them,
(iii) controls that cannot fire, (iv) a negative localized where the
localization is an artifact of a restricted search — **all four recur
in D46b, and (i)+(iii) recur in D46d.**

---

## COMBINED VERDICT

| unit | verdict | BLOCKER | MAJOR | minor | nit |
|---|---|---|---|---|---|
| **D46b** — Martin/R-theory at transport | **REVISE — the mechanics reproduce exactly and MB1 is confirmed, but two of the four headline findings REVERSE under referee recomputation and a third is unearned** | 3 | 4 | 6 | 2 |
| **D46d** — typicality under the completed measure | **REVISE — the exact layer is sound and reproduces, but the headline "width spreads with depth" is a near-tautology measured through a proxy that counts idlers, and the like-for-like scaling test points the other way** | 2 | 4 | 5 | 2 |

**One line each.**

- **D46b.** Every gate reproduces byte-identically; MB1's ladder claim is
  independently confirmed and extended (the referee re-censused the
  delivery-free family directly: the value set really is `{2, 5/2}` on
  both sides).  But **MB5 reverses**: the receipt compares a
  remaining-horizon-**4** root kernel against a remaining-horizon-**1**
  witness kernel, and at *matched* remaining horizon the witness's
  per-kind sector masses are **exactly equal** to the root's at
  r = 1, 2, 3 — so "the delivery-free root = renewal identity DOES NOT
  TRANSFER" is a horizon-mismatch artifact.  **MB4 reverses**: the
  referee computed the delivery-free chain's own finite-horizon ratios
  from the committed d42b3 layer, and they are **larger** than
  transport's at every horizon where they differ (2.0175 vs 2.0136 at
  D = 4), so "deliveries add branching" has the wrong sign; and "RISES"
  is falsified at the next horizon (the transport ratio peaks at D = 5
  and turns down at D = 6).  **MB3-c's contraction claim is true** —
  the referee confirmed it in three norms out to D = 6 and uniformly
  over the state space — but it is not gated, and three of the twelve
  gates are tautologies while `MB6-b` ("no unconditional gate") passes.
- **D46d.** The exact arm is clean: the path measure really is proper,
  the exact profiles reproduce, the calibration gap really is
  3457/9464832 and (referee-checked) does not blow up at the reachable
  depths.  But the headline is comparing incomparable things.  The
  referee's like-for-like series (same pool, same law, growing depth)
  shows the touched-width mass climbing monotonically to 1 — **width is
  a monotone functional of depth, so "width spreads with depth" cannot
  fail** — and the same series computed on a *delivery-joined* width
  gives 0.135 where the receipt reports 0.615, because the receipt's
  proxy counts an actor as "touched" by an **idle**.  At fixed depth the
  full-width mass *falls* as the pool grows (0.557 -> 0.307 in the
  receipt's own numbers), which is the direction that matters for
  unbounded dimension and is not read.

---

# UNIT 1 — D46b (LOG #384), Martin/R-theory at transport scope

## 1.1 What the referee confirms (independent recomputation)

| claim | source | referee finding |
|---|---|---|
| receipt reproduces | rerun | **exit 0, 12 PASS / 0 FAIL, byte-identical** to `v10/data/d46b_martin_transport_exact.out`; ~3.0 s wall |
| ARM-1T census `[1, 9, 69, 521, 3969]` | MB0 | confirmed by an independent level-order rebuild (the receipt uses a stack; the referee used BFS): level sizes 1, 8, 60, 452, 3448 |
| ladder values `{2, 5/2}` with 3757 / 212 | MB1 | **confirmed**, and extended: at depth 5 the value set is still `{2, 5/2}` (25,848 / 912 at that level; 29,605 / 1,124 cumulative to depth 5) |
| "exactly the delivery-free values" | MB1 prose | **confirmed independently** — the referee built the delivery-free family from `v10/code/d42b3_placement_exact.py` (the layer d43b/D44a use) to depth 6: menu-sum census `{2: 32139, 5/2: 2236}`, value set `{2, 5/2}`.  Also consistent with d43b MG2d's row sums `(2,2,2,5/2,2,2)` |
| `G_2 = 4`, `G_3 = 257/32`, `G_4 = 1035/64` | MB2 | confirmed; referee extension: `G_5 = 4173/128`, `G_6 = 134587/2048` |
| kernels proper (sum to 1) | MB3-a | confirmed at every horizon D = 1..6, exactly |
| the 1/256 chain weight | MB5-a | confirmed: `[pA0, blind self-seal, deliver v1 to B]` is admissible with chain weight exactly 1/256 |
| **the drift contracts** | MB3-c | **confirmed and strengthened** — see MAJOR B-M3 for the caveats.  Root L-inf drifts: 0, 1/1028, 191/265995, 412/1439685, 4629/187210517 (D1->D2 .. D5->D6).  L1 and sector-L-inf give the *same* ratios to the digit, so the claim is not norm-dependent.  Uniformly over the state space at fixed *relative* horizon: 3/110, 3/253, 373/69230, 2333/1838829 — contraction ~0.44/level |

The three delivered outcomes and the summary line are consistent with
the printed values; the arithmetic in the receipt is not in question
anywhere.  What is in question is what the numbers are compared with.

## 1.2 Findings

### BLOCKER B-A1 — MB5 reverses: "root = renewal does not transfer" is an artifact of comparing kernels at different remaining horizons

**Where.** `note-d46b-martin-at-transport.md` §4 "MB5 — THE
DELIVERY-FREE root = renewal IDENTITY DOES NOT TRANSFER"; receipt
lines 206-227 and the `[VERDICT]` clause "the kernel at the 1/256
reconvergence witness differs from the root's in sector mass"; LOG #384
finding (4).

**The defect.** `kernel(G, h)` (lines 128-133) computes
`k(e|h) = q · G(h+e)/G(h)` where `G = G_D` is a potential to **absolute**
depth D.  The receipt compares

- `s4 = sector(kernel(G4, []))` — the root, **remaining horizon 4**; with
- `sw = sector(kernel(G4, WIT))` — a depth-3 history, **remaining
  horizon 1**.

At remaining horizon 1 the kernel degenerates to the normalized one-step
menu (`q/menu-sum`) with no lookahead at all.  The two objects are not
the same functional of the state; finding them different measures the
horizon mismatch, not the renewal structure.

**Referee recomputation (matched remaining horizon r).** Defining
`G_rel(h, r)` = potential of h's subtree to relative depth r (the
horizon-invariant object the d44f lesson actually names):

| r | root per-kind sector masses | witness per-kind sector masses | equal? |
|---|---|---|---|
| 1 | d 1/4, n 1/2, p 1/4 | d 1/4, n 1/2, p 1/4 | **YES** |
| 2 | d 1/4, n 1/2, p 1/4 | d 1/4, n 1/2, p 1/4 | **YES** |
| 3 | d 64/257, n 128/257, p 65/257 | d 64/257, n 128/257, p 65/257 | **YES** |
| receipt's pairing (root r=4 vs witness r=1) | d 257/1035, n 514/1035, p 88/345 | d 1/4, n 1/2, p 1/4 | no |

**At every matched horizon the referee can compute, the witness's
sector masses are exactly the root's.**  The receipt's negative is
produced entirely by the r = 4 vs r = 1 pairing.  This is the sibling
round's pattern (iv) in its sharpest form.

**Second, independent defect in the same gate.** Even granting the
comparison, the witness is not a renewal point *of the root*.  D44a's
identity is "root = renewal **AS ONE SIGMA-STATE**"; the 1/256 witness
ends with A and B holding `v1`, which is not the root's holdings state,
so nothing in D44a predicts their kernels should agree.  The receipt
asks whether an object that was never claimed to be the root's renewal
looks like the root — and, by the table above, it does anyway.

**Prescribed fix.** Retract the MB5 headline from the note §4, the
receipt verdict and LOG #384 (forward-correcting entry).  Replace with
the referee's finding, restated and re-gated by the author: *at matched
remaining horizon the reconvergence witness's per-kind sector masses
are exactly the root's at r = 1, 2, 3 — the transport analogue of
root = renewal is SUPPORTED in sector mass at every computable
horizon, and is untested for the full kernel because the two states
carry different option sets.*  Then either (a) re-pose MB5 against a
history that is genuinely in the root's sigma-state, or (b) declare
that no transport history returns to the root state and say so.  The
sentence "reconvergence restores HOLDINGS without restoring the
FUTURE" is not supported by any computation in the receipt and must go.

### BLOCKER B-A2 — MB4 reverses: the growth comparison is a category error, "RISES" is false at the next horizon, and the causal story has the wrong sign

**Where.** note §4 "MB2/MB4 — THE GROWTH PARAMETER EXCEEDS 2 AND RISES
... the delivery-free lambda = 2 is a LOWER NEIGHBOUR of the transport
growth, not its value — deliveries add branching, exactly as the
reopening (D44b) implies"; receipt lines 116-124 and the `[VERDICT]`;
LOG #384 finding (2).

**Defect 1 — category error.**  `lambda = 2` (D44a CG5b) is the **Perron
eigenvalue** of the six-state delivery-free transfer, i.e. the
D -> infinity limit of that chain's ratios.  `G_D/G_{D-1}` at D = 3, 4 is
a **finite-horizon** ratio.  A finite-horizon ratio exceeding an
asymptotic eigenvalue is not evidence of anything: the delivery-free
chain's *own* finite-horizon ratios exceed its own lambda = 2, because
the conflict state carries row sum 5/2 — a fact the receipt itself
establishes one gate earlier in MB1.

**Defect 2 — the sign is backwards.**  The referee built the
delivery-free family directly from `v10/code/d42b3_placement_exact.py`
(the committed layer d43b/D44a run on) to depth 6 and computed the
like-for-like finite-horizon ratios from the same root:

| D | delivery-free `G_D(root)` | transport `G_D(root)` | df ratio | transport ratio |
|---|---|---|---|---|
| 1 | 2 | 2 | 2 | 2 |
| 2 | 4 | 4 | 2 | 2 |
| 3 | 257/32 | 257/32 | 2.007812 | 2.007812 |
| 4 | **1037/64** | **1035/64** | **2.017510** | **2.013619** |
| 5 | 2101/64 | 4173/128 | **2.026037** | **2.015942** |
| 6 | 68313/1024 | 134587/2048 | **2.032157** | **2.015741** |
| 7 | 139065/1024 | (above cap) | 2.035703 | — |

(The delivery-free column was also cross-checked against `T_REF` from
`v10/code/d43b_state_chain_exact.py` propagated from the root class,
which reproduces it digit for digit.)

Deliveries do **not** add branching at this scope: at every horizon
where the two differ, the **delivery-free** potential and ratio are
*strictly larger*.  `G_4` is 1037/64 delivery-free against 1035/64 with
transport.  "Deliveries add branching, exactly as the reopening
implies" is falsified by the like-for-like comparison the claim invites.

**Defect 3 — "RISES" is a two-point read that reverses at the next
horizon.**  Transport ratios: 2, 2, 2.007812, 2.013619, **2.015942**,
**2.015741**.  The sequence peaks at D = 5 and turns *down* at D = 6.
Two ascending points were read as a trend.

**Prescribed fix.** Retract the whole MB2/MB4 headline sentence from
note §4, the receipt verdict and LOG #384.  The defensible residue is:
*the transport finite-horizon growth ratios are 257/128 then 1035/514
then 1391/690 then 134587/66768, all slightly above 2 and turning over
by D = 6; the delivery-free family's finite-horizon ratios at the same
horizons are uniformly larger, so at the reachable caps deliveries
REDUCE finite-horizon branching.*  If the author wants a comparison
with `lambda = 2` at all, it must be labelled as a comparison against
an asymptotic quantity, and the delivery-free finite-horizon column
must be printed beside the transport one in the same receipt.

### BLOCKER B-A3 — three of the twelve gates are tautologies, and `MB6-b` ("no unconditional gate") passes anyway; all three surviving headline outcomes flip under mutation with 12 PASS / exit 0

**Where.** `MB4` (line 122: `r23 > 0 and r34 > 0`); `MB3-b` (line 165:
`isinstance(drift, Fr)`); `MB3-c` (line 244:
`isinstance(d23, Fr) and isinstance(d34, Fr)`); the hygiene gate
`MB6-b` (lines 286-292), whose needles are `", True)"` and `", True,"`.

**The defect.** The needle scan detects only the *literal* `True`
argument.  A gate whose predicate is `isinstance(x, Fraction)` on a
quantity that was just constructed as a `Fraction` is unconditional in
substance and invisible to the scan.  Consequently the receipt's
headline quantities — the growth ratios, the drift magnitudes, the
`shrinking` boolean (line 233, computed and **never gated**, only used
to select outcome prose), and the `sw == s4` verdict (line 221, likewise
only prose) — are not gated at all.  This is the sibling round's
pattern (iii).

**Mutation evidence (all mutants are copies under the referee's
scratch directory; no committed file was touched).**

| mutant | change | expected | observed |
|---|---|---|---|
| **b5** | reverse the drift trend at the point of use (`d34 = drift*3`) | catch | **exit 0, 12 PASS**, outcome text flips to "the root kernel's horizon drift does NOT shrink ... no Cauchy evidence"; `[VERDICT]` still says "their drift SHRINKS level over level" |
| **b6** | force the growth ratios to 1/3 and 1/2 (below 2) | catch | **exit 0, 12 PASS**; `[VERDICT]` still says "THE GROWTH PARAMETER EXCEEDS 2 and rises" |
| **b7** | force `sw = s4` (root = renewal holds) | catch | **exit 0, 12 PASS**, MB5 outcome flips to "MATCHES ... supported"; `[VERDICT]` still says "DOES NOT TRANSFER" |

Note the second half of each row: the static `[VERDICT]` string
contradicts the dynamically-selected `[OUTCOME]` in the same output.
That is the sibling round's pattern (ii) — the retracting branch fires
while the asserting text survives.

**Prescribed fix.** (a) Gate the three quantities: `MB4` must assert the
exact rationals `r23 == Fr(257,128) and r34 == Fr(1035,514)` (and the
delivery-free comparison column, per B-A2); `MB3-c` must assert
`d34 < d23` with both exact values; `MB5-b` must assert the sector-mass
verdict exactly.  (b) Make the `[VERDICT]` string a function of the
delivered outcomes rather than a literal, so a flipped outcome cannot
leave an asserting verdict behind.  (c) Strengthen `MB6-b` to reject
predicates that are provably constant — at minimum add `isinstance(`
and `> 0` on a freshly-constructed positive rational to the needle set.

### MAJOR B-M1 — `MB5-a` does not identify the object it names

**Where.** receipt lines 189-205, "the D44b reconvergence witness
re-admitted through the committed layer ... chain weight exactly 1/256".

**The defect.** After `[pA0, blind self-seal]`, A holds `{v0, v1}` and
B is the only receiver, so `deliver_options_in_view` has exactly two
entries and **every** delivery from A prices at `1/4 / 2 = 1/8`.  Mutant
**b3** replaces the delivered version `V1` by the genesis `V0` — a chain
that reconverges nothing, since B already holds `v0` — and the receipt
**passes 12/12, exit 0**, reporting the same "1/256 reconvergence
witness" language and computing MB5's verdict at the wrong point.  The
gate pins a weight, not an object.

**Prescribed fix.** Add to `MB5-a` an assertion that the delivery's
payload is the arb-created version (`DELIV[3] == V1 and V1 != V0`) and
that the post-chain holdings of A and B actually coincide (the
"reconvergence" predicate), gated exactly.

### MAJOR B-M2 — the pin's MB3 object (the SECTOR-NORMALIZED CONDITIONAL) was never computed; sector *masses* were substituted, and the real object gives the opposite verdict

**Where.** note §2 MB3: "the ABSOLUTE values and the **SECTOR-NORMALIZED
CONDITIONALS** compared exactly at the root and at a reconvergence
point"; note §1: "The d44f lesson binds the reading: absolute values may
shift with the horizon while CONDITIONALS do not; the horizon-stable
object is the physical one."  Receipt `sector()` (lines 140-144) returns
the **mass** of each kind, i.e. `sum_e k(e)` over `e` of that kind — not
the conditional `k(e) / sector-mass(kind(e))`.

**The defect and what the real object shows.** The referee computed the
pinned object.  At the root the within-sector conditional is
**exactly identical at every horizon r = 1..6, drift exactly 0**.  The
receipt's MB3 branch instead fires the "BOTH ... DRIFT ... the
finite-horizon kernel has not stabilized by D = 4 — the escape structure
(D44b) reaching the potentials themselves" text.  The unit reports a
negative on a substituted object where its own pinned object gives an
exact positive.

**Honesty requirement on the repair.** The referee also checked
off-root, and the root's exact stability is partly a symmetry artifact
(at the root all options within a sector are exchangeable, forcing a
uniform conditional at every horizon).  Off-root the conditional does
drift, and it contracts: sup over the family = 1/18, 4/171, 8/741,
176/32877 at r = 1->2 .. 4->5 (ratios ~0.42, 0.46, 0.50), with only
700/3969 histories carrying any conditional drift at all.  So the
correct statement is *the d44f conditional is exactly horizon-stable at
the root (by symmetry) and contracts uniformly off it* — stronger than
what the receipt claims, and about the object the pin named.

**Prescribed fix.** Compute the pinned object; report both the mass and
the conditional; correct the MB3 outcome text; state the symmetry caveat
on the root.

### MAJOR B-M3 — "a contraction ratio ~0.738 per level" is a root-only, two-point artifact

**Where.** note §4 MB3 ("the drift CONTRACTS: 1/1028 (D2->D3) then
191/265995 (D3->D4), a contraction ratio ~0.738 per level"); receipt
lines 247-252 ("SHRINKS by a factor ~{ratio:.3f} per level"); LOG #384
("ratio ~0.738/level").

**The defect.** Three horizons give two drifts and therefore exactly
**one** ratio; "per level" asserts a rate from a single datum.  The
referee's extension shows the rate is nowhere near constant: root
L-inf ratios are 0.738, then **0.399**, then **0.086**.  The uniform
off-root rate is ~0.44.  The number 0.738 is not a property of the
kernel; it is the D3/D4 pair.

**Also.** The drift `D1->D2` at the root is exactly **0**, so of the
"three reachable horizons" only two contribute a nonzero drift.

**Standing.** The *qualitative* claim survives the referee's attack:
contraction holds in L-inf, L1 and sector-L-inf (identical ratios), at
the root out to D = 6, and uniformly over the state space at fixed
relative horizon.  It is not norm-dependent.  Report it that way,
without a rate.

### MAJOR B-M4 — the prose attributes to "the kernel candidates" a measurement made only at the root

**Where.** note §4 "MB3 — THE KERNELS ARE PROPER AND THEIR DRIFT
SHRINKS ... Both the absolute values and the per-kind sector masses
DRIFT between horizons — but the drift CONTRACTS"; receipt `[VERDICT]`
"THE KERNEL CANDIDATES are proper at every horizon and their drift
SHRINKS level over level".

**The defect.** `drift`, `d23`, `d34` are computed at `h = []` only
(lines 135-136, 157, 230-232).  Properness is likewise checked at the
root only (`MB3-a`, line 156).  The plural "the kernel candidates" and
"level over level" claim a state-space-wide fact from a one-point
measurement.  Pattern (i).

**Prescribed fix.** Either restrict the prose to the root, or add the
sup-over-histories gate (the referee's numbers above are exact and cheap
— the whole computation runs in under 4 s on the depth-5 cache).

### minor findings (D46b)

- **B-m1.** `G_3 = 257/32` is *numerically identical* to the
  delivery-free value at the same horizon, and `G_2 = 4` likewise; the
  transport and delivery-free potentials first separate at D = 4
  (1035/64 vs 1037/64).  The receipt presents `G_3 = 257/32` as a
  transport datum with no note that it coincides.  Say so — it is a
  genuine (and interesting) finding that deliveries are invisible to the
  potential below depth 4.
- **B-m2.** There is **no determinism gate** in the receipt and there are
  **no seeds** in it, yet note §4 opens "12 PASS / 0 FAIL, 3 delivered
  outcomes, **seeds byte-identical**" and LOG #384 repeats "verified exit
  0, 12 PASS / 0 FAIL, **seeds byte-identical**".  The phrase is
  imported from a sampled unit and is meaningless here.  The pin's MB6
  promises "determinism"; it is not delivered.  Strike or implement.
- **B-m3.** MB1's "across the whole ARM-1T family" is cap-bound
  (depth <= 4).  The referee extended the census to depth 5 — value set
  unchanged, multiplicities 29,605 / 1,124 — so the claim survives, but
  the multiplicities 3757/212 should be labelled "at the committed
  cap".
- **B-m4.** The output contains two outcomes in direct tension: MB3
  ("at transport scope the finite-horizon kernel **has not stabilized**
  by D = 4") and MB3-c ("**Cauchy-consistent with a limit kernel**").
  Both are printed without any reconciling sentence.
- **B-m5.** `MB6-c` is labelled "SCOPE, mechanical" but its predicate is
  `CAP == 4 and len(OUT) >= 3` — it checks a constant and a list length,
  and asserts nothing about the scope language it certifies.  It cannot
  detect a boundary-existence claim if one were added.
- **B-m6.** MB1's `LADDER_REF = {'2': 3757, '5/2': 212}` is a hard-coded
  self-anchor; the "exactly the delivery-free values" comparison is made
  only in prose.  The delivery-free census should be recomputed in the
  receipt (it costs ~12 s from the committed d42b3 layer — the referee
  did it) or cited to a specific line of
  `v10/data/d43b_state_chain_exact.out`.

### nits (D46b)

- **B-n1.** The `[VERDICT]` string is a literal; per B-A3(b) it should be
  assembled from the delivered outcomes.
- **B-n2.** LOG #384's four-finding summary is now wrong in findings (2)
  and (4) and over-specified in (3); it needs a forward-correcting entry,
  not a silent edit.

## 1.3 D46b mutation table

All mutants are copies in the referee's scratch directory; the committed
receipt was never modified.

| # | kind | mutation | expect | exit | PASS/FAIL | verdict |
|---|---|---|---|---|---|---|
| b1 | physics | halve the layer's idle weight | exit 1 | **1** | 10/2 | **caught** (MB1, MB2) |
| b2 | physics | scale every delivery weight by 3/4 | exit 1 | **1** | 10/2 | **caught** (MB1, MB2) |
| b3 | physics | MB5 witness delivers `v0` instead of `v1` (no reconvergence) | exit 1 | **0** | 12/0 | **MISSED** — see MAJOR B-M1 |
| b4 | anchor | `CAP = 3` | exit 1 | **1** | 0/2 | **caught** (MB0, MB1) |
| b5 | gate-vacuity | drift trend reversed (`d34 = 3·d34`) | exit 1 | **0** | 12/0 | **MISSED** — headline flips silently |
| b6 | gate-vacuity | growth ratios forced below 2 | exit 1 | **0** | 12/0 | **MISSED** — headline flips silently |
| b7 | gate-vacuity | `sw := s4` (root = renewal forced true) | exit 1 | **0** | 12/0 | **MISSED** — headline flips silently |

**4 of 7 mutants survive**, and the four survivors are precisely the
four that attack the unit's delivered findings.  Only the census and the
potentials are genuinely defended.

---

# UNIT 2 — D46d (LOG #386), typicality under the completed measure

## 2.1 What the referee confirms (independent recomputation)

| claim | source | referee finding |
|---|---|---|
| receipt reproduces | rerun | **exit 0, 11 PASS / 0 FAIL, byte-identical** to `v10/data/d46d_typicality_exact.out`; ~3 min 27 s wall |
| the path measure is proper | TY1-a | confirmed — and note it telescopes: `path_mass(h) = w(h)/G(root)`, i.e. the "completed" measure is exactly the weight-proportional measure over depth-4 leaves |
| exact width profiles 0.961 / 0.450 / 0.108 / 0.019 | TY1-b/TY2 | confirmed exactly (221/230, 130/289, 994/9243, 3/160), rebuilt independently |
| calibration gap `3457/9464832` at pool 4 / depth 3 | TY3-a | confirmed exactly |
| calibration gap does not blow up | referee probe | the referee computed the completed-vs-local width-mass gap at 12 (pool, depth) pairs.  It is **exactly 0** at every depth <= 2 for every pool, and 27/65792 (~4.10e-4) at 2a/d3, 99/235520 (~4.20e-4) at 2a/d4, 47/97104 (~4.84e-4) at 3a/d3, 3457/9464832 (~3.65e-4) at 4a/d3.  **The "MAJOR if it grows with depth" horn does not fire** at the depths the referee could reach |
| the sampled numbers | TY3/TY4 | independently reproduced with a different N and the same law: referee N=600 at 6 actors / depth 8 gives width>=4 = 0.978 and full width = 0.333, against the receipt's 0.981 / 0.307 |
| the estimator's reproducibility gate is meaningful | TY3-b | **yes** — see the mutation table (a deterministic sampler is caught).  This is the unit's one control that genuinely fires |
| doctrine compliance in substance | TY5-a | **holds**: the note and receipt speak only of ORDER dimension / clock complexity and explicitly disclaim a spacetime reading, per note-d45b §1.  The *scan* that certifies it is vacuous (see D-M4), but the substance is clean |

## 2.2 Findings

### BLOCKER D-A1 — the headline compares incomparable things, and the like-for-like comparison makes it near-tautological

**Where.** Receipt `[OUTCOME TY]` (lines 304-317) and `[VERDICT]`
(lines 393-395); note §4 "TY4/TY — THE READING. **WIDTH SPREADS WITH
DEPTH UNDER THE THEORY'S OWN LAW**"; LOG #386's bolded headline.

**The defect.** The outcome sentence is a single inference chaining

- four **exact** numbers under the **completed** law at four different
  `(pool, depth)` pairs — (2, d4), (3, d3), (4, d3), (5, d2) — reporting
  the mass at each pool's **maximum realizable width**; to
- one **sampled** number under the **local-normalized** law at a fifth
  pair — (6, d8) — reporting the mass above a **fixed threshold of 4**.

Four things vary at once: the law, the pool, the depth, and the
statistic.  Nothing in that chain isolates depth.

**Referee's like-for-like series (same pool, same law, growing depth;
local-normalized law, N = 600, seed 20260719, both width notions).**

pool 4 actors:

| depth | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 16 |
|---|---|---|---|---|---|---|---|---|
| touched-width >= 4 (= full) | 0.010 | 0.110 | 0.290 | 0.615 | 0.782 | 0.892 | 0.957 | 0.988 |
| delivery-joined width >= 4 | 0.010 | 0.027 | 0.062 | **0.135** | 0.238 | 0.382 | 0.467 | 0.665 |

pool 6 actors:

| depth | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 16 |
|---|---|---|---|---|---|---|---|---|
| touched-width >= 4 | 0.027 | 0.242 | 0.578 | 0.903 | 0.978 | 1.000 | 1.000 | 1.000 |
| touched full width 6 | 0.000 | 0.002 | 0.010 | 0.130 | 0.333 | 0.532 | 0.658 | 0.872 |
| delivery-joined >= 4 | 0.027 | 0.070 | 0.135 | 0.270 | **0.432** | 0.543 | 0.633 | 0.787 |
| delivery-joined full 6 | 0.000 | 0.002 | 0.000 | 0.013 | **0.030** | 0.062 | 0.103 | 0.207 |

**The claim survives the like-for-like test — and that is the problem.**
Actor width is a **monotone non-decreasing functional of the path**: a
longer history can only touch more actors.  At a fixed pool the width
mass therefore climbs to 1 for *any* law with full support, and the
tables show exactly that saturation.  "Width spreads with depth" is
not a discriminating statement about "the theory's own law"; it is a
property of the observable.  A control that cannot fail is not
evidence.

**What the discriminating question is, and what it answers.**  D45b's
result is **unbounded** order dimension, which needs width growing with
the pool.  The referee therefore ran the two scalings the claim
actually needs:

*Fixed depth 8, growing pool (N = 600):*

| pool | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|
| touched width >= 4 | 0.000 | 0.782 | 0.938 | 0.978 | 0.987 | 0.998 |
| touched **full** width | 0.963 | 0.782 | 0.568 | **0.333** | 0.137 | **0.037** |
| delivery-joined full width | 0.525 | 0.240 | 0.105 | **0.030** | 0.005 | 0.003 |

*The diagonal depth = 2 x pool (D45b's own constructor ratio: 6 actors,
~8-12 events; N = 300):*

| pool / depth | 3/6 | 4/8 | 5/10 | 6/12 | 7/14 |
|---|---|---|---|---|---|
| touched full width | 0.867 | 0.770 | 0.757 | 0.690 | 0.623 |
| delivery-joined full width | 0.340 | 0.240 | 0.163 | 0.120 | 0.073 |

The mass above the **fixed** threshold 4 rises to 1 — trivially, because
the threshold is fixed while the pool grows.  The mass at **full**
width, which is the axis unbounded dimension lives on, **decays with
the pool under every scaling the referee tested**, and decays roughly
geometrically (~0.75x per added actor on the diagonal, faster at fixed
depth).

**Prescribed fix.** Retract the outcome sentence and the note §4
headline as written; retract LOG #386's bolded claim by a
forward-correcting entry.  Replace with the two separated statements the
data support: (1) *at a fixed pool the width mass saturates with depth —
a monotonicity fact about the observable, not a discriminating property
of the law*; (2) *the mass above the fixed width-4 threshold (the
necessary condition for order dimension > 2) does become large as pool
and depth grow, while the mass at the pool's FULL width decays with the
pool — so what is typical-in-the-making is dimension >= 3, not unbounded
dimension.*  Both statements must be produced by one law at one scaling
in one gated table.

### BLOCKER D-A2 — "the theory's OWN law" is not established; two different laws are used, and the layer supplying the weights explicitly disclaims a measure

**Where.** note §1 ("under the theory's OWN law — the completed transfer
/ kernel candidate, not a hand-imposed distribution"), §4 headline;
receipt lines 11-12 and the `[VERDICT]`; LOG #386.

**The defect.** The weights come from `v10/code/d42b1_transport_exact.py`,
whose own docstring states: *"Weight-system level only (RF4): **no
measure claim**; the placement front (d42b3) owns normalization."*  The
menus do not sum to 1 — they sum to 2 or 5/2 (D46b MB1) — so a
probability law has to be *chosen*.  D46d chooses **two different ones**:

- the exact arm uses the lookahead normalization
  `k(e|h) = q·G(h+e)/G(h)`, which telescopes to `w(path)/G(root)`;
- the sampled arm uses the local normalization `q/sum q`.

Neither is pinned anywhere in the corpus as "the theory's own law", and
they are demonstrably different objects (that is what TY3-a measures).
Calling both "the theory's OWN law", and putting that phrase in the
headline of the unit that the program treats as its main typicality
evidence, asserts more than any gate delivers.

**Prescribed fix.** Either cite the corpus line that licenses the
normalization as *the* law, or rename throughout: "the
lookahead-normalized weight measure" (exact arm) and "the
local-normalized weight measure" (sampled arm), with every number
labelled by which one produced it.  The note-level claim then becomes
what it is: a statement about two candidate normalizations of a weight
system that its own layer declares unnormalized.

### MAJOR D-M1 — the width proxy counts idlers, and the receipt presents the resulting inflation as supporting evidence

**Where.** `actors_touched` (receipt lines 131-139): `s.add(e[1])` runs
for **every** event kind, including `'n'` (idle), which the layer prices
as the unconditional residual.  Note §4 "Event-kind mass shows the
measure is IDLE-HEAVY (about half of all event mass is idle at every
pool) — the same idles D45b found LOAD-BEARING for the dimension
escape."

**The defect.** An actor that only ever idles is "touched".  Its events
form an isolated chain in the event poset and cannot raise order
dimension.  D45b's escape does need idles — but as **marks interleaved
with deliveries among actors that participate**; an actor with no
delivery contributes nothing to a crown.  So the receipt's proxy is the
*liberal* end of a range whose *conservative* end (actors joined by at
least one delivery — the shape of d43d's W6, "six deliveries among six
actors") is materially smaller.  Referee recomputation, exact, at the
same enumerable pools:

| pool / depth | statistic | touched (receipt) | non-idle active | delivery-joined |
|---|---|---|---|---|
| 2 / d4 | mass at width 2 | 0.9609 | 0.7599 | 0.6783 |
| 3 / d3 | mass at width 3 | 0.4498 | 0.2042 | 0.1073 |
| 4 / d3 | mass at width 4 | 0.1075 | 0.0452 | 0.0316 |
| 5 / d2 | mass at width 4 | 0.0187 | 0.0187 | 0.0187 |

and at the headline configuration (sampled, pool 6 / depth 8): width >= 4
mass **0.978 -> 0.432**, full width mass **0.333 -> 0.030**.  The
headline "98% of the sampled mass sits at or above the dimension
threshold width 4" becomes 43% on the conservative proxy, and the full
width figure falls by an order of magnitude.

Presenting idle-heaviness as *support* ("the same idles D45b found
LOAD-BEARING") inverts its role here: in this measurement idles are the
**confound** that inflates the proxy.

**Prescribed fix.** Report all three width notions in TY1/TY2/TY4, state
at the point of use that `actors_touched` counts idlers and is therefore
an upper bound on dimension-relevant width, and move the headline number
onto the conservative proxy or onto an explicit bracket
[delivery-joined, touched].

### MAJOR D-M2 — TY4 and TY1 each implement half of their pin

**Where.** pin §2 TY1: "compute the exact distribution of ... (iii)
**poset width where cheap**" — never computed; the receipt reports actor
counts only.  Pin §2 TY4: "the exact/estimated mass of the D45b
courier-witness SHAPE class (records whose actor count **and delivery
pattern** could host the constructor)" — the receipt's TY4 (lines
287-303) measures the actor-count half only.

**The defect.** The delivery-pattern half is exactly the half that
would have caught D-M1, and the poset-width half is exactly the
quantity that stands between "actor width" and "order dimension".  Both
were pre-registered and both were silently dropped; the receipt's TY4
label instead re-describes the reduced measurement as answering "does
the LAW go where the CONSTRUCTION goes".

**Also.** TY4's label cites the constructor's per-event weight
(1/212 at n = 6 — the referee checked this against note-d45b line 139,
`1/(4(n^2+3n-1))`, and it is correct) but never uses it.  The direct,
honest form of "does the law go where the construction goes" is the mass
of the constructor's own record class, which is computable in closed
form from that weight and is astronomically small.  Citing the weight
and then reporting a width statistic instead reads as a substitution.

**Prescribed fix.** Implement both halves, or amend the pin and say in
§4 which pre-registered gates were dropped and why.

### MAJOR D-M3 — width >= 4 is a NECESSARY condition; the mass above it upper-bounds the dimension mass, and the direction is never stated

**Where.** Receipt TY4 label ("actor-width >= 4 (the D44c/d43d dimension
threshold)"); note §4 ("98% of the sampled mass sits at or above the
dimension threshold width 4 ... dimension-capable width is
TYPICAL-IN-THE-MAKING"); LOG #386.

**The defect.** d43d TERMINAL (#342) reads "TRANSPORT GENERATES
DIMENSION at actor-width >= 4 ... S3 sharply at 6 actors", and d44c AG5
records that *all* 219 four-event and *all* 4,231 five-event labelled
posets have dim <= 2.  Width >= 4 is therefore **necessary and not
sufficient**.  `mass(width >= 4) = 0.98` bounds `mass(dim > 2)` from
**above** only; it is consistent with `mass(dim > 2) = 0`.  The note does
hedge ("a PROXY", "the per-record dimension test is the named
successor"), which is to its credit, but nowhere states the direction of
the bound — and the word "capable" in "dimension-capable width" reads as
sufficiency.

**Second, subtler defect.** D45b's result is **unbounded** dimension.
Fixing the threshold at 4 converts the inherited typicality question
into a question about dimension >= 3.  The narrowing is never declared.

**Prescribed fix.** State the bound direction explicitly wherever the
number appears, and separate "typicality of dimension >= 3" (which the
data support) from "typicality of unbounded dimension" (which the
referee's scaling tables in D-A1 point *against*).

### MAJOR D-M4 — three gates cannot fire, and the doctrine scan certifies nothing

**Where.** `TY2-b` (line 197: `isinstance(conc, bool)`); `TY4` (line
300: `0 <= mass_ge4 <= 1 and 0 <= mass_ge6 <= 1`); `TY3-a` (line 234:
`lt4 == 1 and isinstance(gap, Fr)`); `TY5-a` (lines 321-332).

**The defects.**

1. `TY2-b`'s label promises "the concentration reading (is the top-width
   mass below one half everywhere?) is **computed, not assumed**".  It
   is computed — into the variable `conc` (line 191) — and then **never
   printed and never gated**.  The reading the gate is named for does not
   appear in the output.
2. `TY4`'s predicate is that two frequencies lie in [0, 1].  Mutant
   **d4** forces `mass_ge4 = 0.01` (the headline reversed) and the
   receipt still exits 0 with 11 PASS.
3. `TY3-a`'s gate does not bound the gap at all; the bound lives only in
   `TY5-d` (`gap < 1/100`).  As written, TY3-a would pass with a gap of
   0.9.
4. `TY5-a` scans **only the receipt's own source text**, and exempts any
   line containing `'not '`, `'never'`, `'no '`, `'binds'`, `'doctrine'`,
   `'successor'` or `'scan-exempt'`.  Mutant **d5** inserts the line
   `the generated record has spacetime dimension 3+1, not fewer` and the
   scan passes it (the word "not" exempts it).  The note and the LOG
   entry — where a doctrine violation would actually be published — are
   not scanned at all.  This is the sibling round's pattern (iii).

**Prescribed fix.** Gate the exact rationals (`conc` and the four
top-width masses, exactly); gate the headline masses against their exact
sampled values; move the gap bound into TY3-a; make the doctrine scan
run over the note and the LOG entry and drop the blanket negation
exemption (require an explicit marker token instead).

### minor findings (D46d)

- **D-m1.** The exact arm and the sampled arm run under **different
  laws**, and the `[OUTCOME TY]` sentence joins them with "so".  Even
  granting the calibration, an inference that crosses a law boundary
  must say so in the sentence that makes it.
- **D-m2.** The calibration is performed at **pool 4, depth 3** only.
  The pools actually sampled are **5 and 6**, and the depths are **6 and
  8** — none of them calibrated.  (Referee extension: see the table in
  §2.1 and the appendix; the gap does not grow at the reachable depths,
  so the extrapolation is not falsified — but it is an extrapolation of
  2x-2.7x in depth and 1.5x in pool, and the receipt's phrase
  "licensing the sampled extension" overstates what a single-point
  calibration licenses.)
- **D-m3.** The sampler is **not exactly rational**.
  `Fr(rng.randrange(10**9), 10**9) * tot` compares against cumulative
  thresholds `acc`; in a 200-path probe at pool 4 / depth 6 the referee
  found **5,644** thresholds for which `acc/tot * 10^9` is not an
  integer, so the realized law is a 1e-9-grid perturbation of the local
  law.  The bias is bounded by (#options)·1e-9 ~ 1e-8 per step, i.e.
  ~1e-7 over 8 steps — utterly negligible against the N=4000 Monte-Carlo
  error of ~8e-3, and a referee cross-check at pool 3 / depth 3 with
  N = 20,000 (0.0450 / 0.5016 / 0.4534) agrees with the exact profile
  (0.0467 / 0.5035 / 0.4498) to within ~1 standard error.  **The
  estimator is fine in practice**; what is wrong is describing it as
  exact.  State the bound.
- **D-m4.** The exact series "0.961 / 0.450 / 0.108 / 0.019 **as the
  pool grows**" also has the depth *shrinking* (4, 3, 3, 2).  The
  depth-limitation caveat is present, but the series is still presented
  as a pool trend.  The referee's fixed-depth-8 row (0.782, 0.568,
  0.333, 0.137, 0.037 for pools 4-8) is the honest version and happens to
  confirm the direction.
- **D-m5.** `TY5-b`'s purity walk covers `PROFILES, lp4, kp4, gap,
  G[root], MASS` — the exact layer only, correctly labelled.  But the
  headline numbers are floats from the sampled layer and no gate
  constrains them; the "exact/sampled separation is structural" claim
  (TY5-d) is about *labels*, not about the inference made from them,
  which is where the separation actually broke (D-A1).

### nits (D46d)

- **D-n1.** `[OUTCOME TY]` hard-codes the four exact profile numbers as
  literals in the string while recomputing `mass_ge4`/`mass_ge6` — if a
  profile changed, the outcome text would silently lie.
- **D-n2.** "the corpus's first sampled study, hence also a METHOD unit"
  (note §1, LOG #385) — a method unit should carry a Monte-Carlo error
  bar on every reported frequency.  None of the sampled numbers has one
  (at N = 4000 the standard error on 0.307 is ~0.007).

## 2.3 D46d mutation table

All mutants are copies in the referee's scratch directory; the committed
receipt was never modified.  Each run is a full ~3.5 min execution of the
mutated receipt.

| # | kind | mutation | expect | exit | PASS/FAIL | verdict |
|---|---|---|---|---|---|---|
| d1 | physics | halve the layer's idle weight | exit 1 | **1** | 10/1 | **caught** (TY0 anchors `G_4(root) = 1035/64`) |
| d2 | anchor | `CAP = 3` | exit 1 | **1** | 9/2 | **caught** (TY0, TY1-a) |
| d3 | proxy swap | `actors_touched` stops counting idle-only actors (a legitimate rival proxy) | flag or fail | **0** | **11/0** | **MISSED** — every exact profile changes (0.961->0.760, 0.450->0.204, 0.108->0.045) and the headline drops from 0.981/0.307 to **0.672/0.077**, yet the hard-coded `[OUTCOME TY]` and `[VERDICT]` still print "0.961 / 0.450 / 0.108 / 0.019" — the receipt's own summary is then *false about numbers printed 20 lines above it* |
| d4 | gate-vacuity | force `mass_ge4 = 0.01` (headline reversed) | exit 1 | **0** | **11/0** | **MISSED** — `TY4`'s predicate is `0 <= x <= 1` |
| d5 | doctrine-scan vacuity | insert the line `the generated record has spacetime dimension 3+1, not fewer` | exit 1 | **0** | **11/0** | **MISSED** — the word "not" exempts the line; `TY5-a` reports "undisclaimed lines = none" |
| d6 | sampler | make the sampler deterministic (always the first candidate) | exit 1 | **1** | 10/1 | **caught** (`TY3-b`: `dif != SAMPLED` fails) — the unit's one control that genuinely fires |

**4 of 6 mutants survive.**  The two that are caught defend the exact
anchor and the estimator's stochasticity; nothing defends the width
proxy, the headline mass, or the doctrine claim.

---

# 3. Independent-recomputation inventory

Everything below was computed by the referee from the committed layers,
not read out of a receipt.

**For D46b:**

1. ARM-1T family rebuilt in level order (BFS) to depth 5 from
   `d42b1_transport_exact.py` — 1 / 8 / 60 / 452 / 3448 / 26760 per level
   (30,729 histories with cached menus).
2. Menu-weight-sum census per level to depth 5 (value set and
   multiplicities).
3. Finite-horizon potentials `G_1 .. G_6` at the root, exact rationals.
4. Growth ratios `G_D/G_{D-1}` for D = 1..6.
5. The **delivery-free** family rebuilt independently from
   `d42b3_placement_exact.py` to depth 6 (1 / 6 / 32 / 176 / 976 / 5280 /
   27904; cumulative `[1,7,39,215,1191,6471,34375]`, matching d43b MG0),
   its menu-sum census, and its finite-horizon potentials and ratios to
   D = 7 — cross-checked against `T_REF` from `d43b_state_chain_exact.py`
   propagated from the root class (agreement digit for digit).
6. Root kernels at every horizon; drift in L-inf, L1, sector-L-inf, and
   the within-sector conditional; successive ratios.
7. Sup-over-histories drift at fixed *relative* horizon (the correct
   uniform test) and at fixed *absolute* horizon (the receipt's
   convention).
8. Relative-horizon kernels `k_r(h)` for arbitrary h, and the root-vs-
   witness comparison at matched r = 1, 2, 3.
9. A census of how many histories share the root's per-kind sector
   masses at matched horizon (8196/30728 at r=1; 1060/3968 at r=2;
   104/520 at r=3) — the receipt's "renewal" question asked of the whole
   family rather than one hand-picked point.

**For D46d:**

10. The full exact width-mass profiles at 12 `(pool, depth)` pairs under
    **both** laws (completed-lookahead and local-normalized), giving the
    calibration gap at each — including the two pools the receipt
    actually samples but never calibrates: **pool 5 at depth 3** (42,065
    terminals, gap `1539/5646080` ~ 2.73e-4) and **pool 6 at depth 3**
    (109,212 terminals, gap `5451/19210880` ~ 2.84e-4).
11. The same exact profiles under three width notions: the receipt's
    `actors_touched`, "non-idle active", and "delivery-joined".
12. The like-for-like sampled series (same pool, same law, depths
    2..16) at pools 4 and 6, both width notions, N = 600.
13. The fixed-depth-8 pool series (pools 3..8) and the diagonal
    `depth = 2 x pool` series (pools 3..7), both width notions.
14. A sampler-exactness probe (5,644 non-representable thresholds in a
    200-path probe) and an empirical-vs-exact check at pool 3 / depth 3
    with N = 20,000.

---

# 4. Reproduction appendix

All commands are run from `/Users/felixrobles/workspace/isp`.  The
referee's scripts live under the session scratchpad
(`.../scratchpad/`) and are listed here by content, not committed.

```
# byte-identical reproduction of both receipts
python3 v10/code/d46b_martin_transport_exact.py   # exit 0, 12 PASS, ~3 s
python3 v10/code/d46d_typicality_exact.py         # exit 0, 11 PASS, ~3 min 27 s
diff <(python3 v10/code/d46b_martin_transport_exact.py) \
     v10/data/d46b_martin_transport_exact.out      # empty
diff <(python3 v10/code/d46d_typicality_exact.py) \
     v10/data/d46d_typicality_exact.out            # empty
```

**Referee script 1 — `ref_b_build.py`** (~27 s): execs the committed
`d42b1` prefix (`_src[:_src.index('print("[d42b1')]`), rebuilds the
ARM-1T family in level order to `CAP = 5`, pickles `{CACHE, levels}`.
Because menus are cached at depth 5, this single artifact supports
potentials `G_1 .. G_6`.

**Referee script 2 — `ref_b_analyze.py` / `ref_b2.py` / `ref_b3.py`**
(~4 s each): sections A (per-level ladder census), B (potentials and
ratios), C (delivery-free `T_REF` propagation), D (root drift in three
norms), E (sup drift, absolute and relative horizon), F (root vs the
1/256 witness at matched horizon), G (the sector-mass census).  The
relative-horizon potential is

```python
def Grel(h, r):                       # memoised
    return Fr(1) if r == 0 else sum(q * Grel(h + (e,), r - 1)
                                    for e, q in CACHE[h])
def krel(h, r):
    tot = Grel(h, r)
    return {e: q * Grel(h + (e,), r - 1) / tot for e, q in CACHE[h]}
```

**Referee script 3 — `ref_df.py`** (~12 s): the delivery-free partner,
built from `v10/code/d42b3_placement_exact.py` (the layer d43b/D44a use)
to depth 6; prints the census `[1,7,39,215,1191,6471,34375]`, the
menu-sum census `{2: 32139, 5/2: 2236}`, and `G_D(root)` /ratios to
D = 7.

**Referee script 4 — `ref_d1.py`** (~75 s): the 12-pair calibration
table and the three-width-notion exact profiles.
**`ref_d4.py`** (~6 min): the calibration extended to pool 5 at depth 3.

**Referee script 5 — `ref_d2.py` / `ref_d3.py`**: the sampler-exactness
probe, the like-for-like depth series, the fixed-depth pool series, and
the `depth = 2 x pool` diagonal.  The sampler is the receipt's
`sample_widths` verbatim, instrumented with a second width statistic.

**Mutants.** Each mutant is produced by a single `str.replace` on a copy
of the committed receipt (the exact replacements are listed in the two
mutation tables above) written to `.../scratchpad/mut/<name>.py` and run
with cwd = the repo root, so the `_SRC` path-anchored `exec` of the
committed layer still resolves.  No committed file was modified at any
point in this review.

---

# 5. What the referee is NOT objecting to

To keep the repair honest, the following were attacked and **survived**:

- **D46b MB1** — the ladder value set `{2, 5/2}` at transport really is
  the delivery-free value set; the referee confirmed it from the
  delivery-free layer directly and extended the transport census a level
  deeper.  This is the unit's solid finding.
- **D46b MB3-c's qualitative contraction** — real, norm-independent
  (L-inf, L1 and sector-L-inf give identical ratios), holds at the root
  out to D = 6 and uniformly over the family at fixed relative horizon.
  Only the *rate* and the *scope of the prose* are wrong.
- **D46b MB3-a properness** — exact at every horizon checked.
- **D46d's exact arm** — proper measure, correct profiles, correct
  calibration gap; the referee extended the calibration to eight further
  `(pool, depth)` pairs and to a sampled pool and **could not** make it
  grow.  The "calibration is overstated" horn does **not** fire.
- **D46d's estimator** — reproducible, genuinely stochastic (mutant d6
  is caught), and empirically unbiased to within Monte-Carlo error
  despite the 1e-9 grid.
- **D46d's doctrine compliance in substance** — order dimension only,
  explicitly disclaimed as a clock-complexity grade, consistent with
  note-d45b §1.  Only the *scan* is vacuous.

---
---

# ROUND-1 DELTA (referee, 2026-07-24)

**Objects:** commit `e0721f5` (repairs), LOG #398 (conversions and
retractions) and #399 (receipt repairs).  Round-1 body above is
untouched.  Nothing here edits a committed file and nothing is
committed.

## D-0. Reproduction and independent confirmation

| item | referee finding |
|---|---|
| `d46b` rerun | **exit 0, 19 PASS / 0 FAIL, byte-identical** to the committed `.out`; ~3 s |
| `d46d` rerun | **exit 0, 17 PASS / 0 FAIL, byte-identical** to the committed `.out` |
| **matched-horizon sector masses** (the coordinator's confirmation request) | **CONFIRMED against my own `Grel`/`krel` computation, value for value**: r = 1 and r = 2 give `d 1/4, n 1/2, p 1/4` at both root and witness; r = 3 gives `d 64/257, n 128/257, p 65/257` at both.  The old mismatched pairing (root r = 4 `d 257/1035, n 514/1035, p 88/345` vs witness r = 1) is printed as the artifact, correctly |
| MB5-c renewal census | **CONFIRMED exactly**: 8196/30728, 1060/3968, 104/520 — these are my numbers to the digit |
| MB4 two-family table | **CONFIRMED exactly**, both columns, D = 1..6, including the separation at D = 4 (1037/64 vs 1035/64) and the transport turnover (peak 1391/690 at D = 5, 134587/66768 at D = 6) |
| MB3-b/e drift data | **CONFIRMED exactly** in all three norms: L-inf `0, 1/1028, 191/265995, 412/1439685, 4629/187210517`; L1 `0, 3/514, 382/88665, 824/479895, 27774/187210517`; family-uniform sup `3/110, 3/253, 373/69230, 2333/1838829` |
| MB3-c/d conditional | **CONFIRMED exactly**: root drift 0 at r = 1..6; off-root sup `1/18, 4/171, 8/741, 176/32877` with 700/3969, 140/521, 36/69, 4/9 histories carrying drift |
| MB1-b delivery-free census | **CONFIRMED**: `{2: 5963, 5/2: 508}` to depth 5 is consistent with my own depth-6 census `{2: 32139, 5/2: 2236}` and the d43b cumulative `[1,7,39,215,1191,6471]` |
| **TY1-c poset widths (a NEW claim, not in round 1)** | **INDEPENDENTLY RECOMPUTED FROM SCRATCH AND CONFIRMED**, exact rational for exact rational: 2a/d4 `w1 833/2070, w2 1237/2070`; 3a/d3 `78/289, 184/289, 27/289`; 4a/d3 `1459/9243, 5840/9243, 216/1027`; 5a/d2 `49/160, 111/160`; max widths 2/3/3/2 |
| three-proxy exact masses | **CONFIRMED**: 221/230 vs 1573/2070 vs 78/115; 130/289 vs 59/289 vs 31/289; 994/9243 vs 418/9243 vs 292/9243 |
| TY4-b/c/d sampled series | **CONFIRMED** — every figure in the like-for-like, fixed-depth and diagonal tables is the referee's own number, reproduced under the same seed |
| d42b1 disclaimer quote | **verbatim** in `v10/code/d42b1_transport_exact.py`, as TY0-a claims |

## D-1. The round-1 mutants, re-run against the repaired receipts

All four D46b survivors are **closed**:

| mutant | round 1 | after repair |
|---|---|---|
| **b3** — witness delivers `v0` instead of `v1` | exit 0, 12 PASS (**missed**) | **exit 1, 17 PASS / 2 FAIL** — MB5-a *and* MB5-b fire |
| **b5** — contraction reversed | exit 0, 12 PASS (**missed**) | **exit 1, 18/1** — MB3-e fires |
| **b6** — growth sign reversed | exit 0, 12 PASS (**missed**) | **exit 1, 18/1** — MB4-b fires |
| **b7** — matched-horizon agreement broken | exit 0, 12 PASS (**missed**) | **exit 1, 18/1** — MB5-b fires |

The `[VERDICT]` interpolation also works as advertised: in each of
these the verdict clause moves with its outcome instead of outliving
it.  **B-A1, B-A2, B-A3, B-M1, B-M2, B-M3, B-M4, B-m1..B-m6 and both
D46b nits are addressed.**

## D-2. New attacks on the new controls (D46b)

The two new scanners are real improvements over the needle scan they
replace, and neither is exploited by any predicate currently in either
receipt.  Both, however, are advertised more strongly than they can
enforce.  Three fresh mutants, all run against the committed repaired
receipt:

### minor d-b1 — MB6-b's AST scan is defeated by hoisting

`vacuity_scan` walks `nd.args[1]` of each `check(...)` call.  A
predicate that is *computed into a variable first* presents as a bare
`ast.Name` and is invisible.

- **Mutant b8** inserts `_hoisted_ok = isinstance(G4R, Fr) if False else True` followed by `check("SMUGGLED-1 ...", _hoisted_ok)`.
- Result: **exit 0, 20 PASS / 0 FAIL**; MB6-b reports "gate predicates parsed = 20; vacuous predicates = **none**" while gate 20 is a hoisted literal `True`.

The same hole covers an aliased call (`chk = check`, since the scan
keys on `getattr(nd.func, 'id', '') == 'check'`) and a keyword-passed
predicate (`check(label, ok=...)`, since only positional `args[1]` is
walked).

### minor d-b2 — three vacuous *shapes* dodge all three rejectors

The scan rejects a literal boolean, an `isinstance()` call, and a
`>`/`>=` against the constant `0`.  It does not reject:

- `len(X) >= 1` on a list known non-empty (comparison against 1);
- `type(x) is int` (a type probe that is not `isinstance`);
- `x > -1` (the comparator is `UnaryOp(USub, Constant(1))`, not `Constant(0)`).

- **Mutant b9** adds `check("SMUGGLED-2 ...", len(OUT) >= 1 and type(CAP) is int and CAP > -1)`.
- Result: **exit 0, 20 PASS / 0 FAIL**, "vacuous predicates = none".

**Prescribed fix for d-b1 + d-b2 (both minor).** Either (a) resolve a
single-`Name` predicate to its unique assignment in the module before
scanning, reject `type(...) is ...`, and reject any comparison whose
constant comparator is a literal number regardless of sign; or
(b) — cheaper and honest — retitle the gate from the absolute
"**NO VACUOUS GATE**" to "no gate of the three shapes round 1 found
surviving (declared vocabulary)" and record the residual holes
in-gate.  What must not stand is a control whose label claims more
coverage than it has: that is the very pattern the gate exists to
prevent.

### minor d-b3 — MB6-c's scope scan is a fixed four-word vocabulary

- **Mutant b10** prints `the transport chain is R-recurrent and its Martin limit is attained in the infinite-depth sense` — an unqualified infinite-volume assertion.  None of the four needles matches (`limit kernel` != `Martin limit`; `infinite-volume` != `infinite-depth`; no `boundary`, no `converges`).
- Result: **exit 0, 19 PASS / 0 FAIL**, "undisclaimed = none".

Note also that the marker list includes `'open'`, `'candidate'` and
`'reachable'` — broad enough that a genuine violation sharing a line
with any of them is exempted.

**Prescribed fix (minor).** Widen the needle set (`recurren`,
`R-recurrent`, `infinite`, `limit`, `exists`, `at infinity`, `n ->
infinity`) and declare the vocabulary as the gate's stated scope.

## D-3. The one repair-side residue that reaches a reader: §4 is not stamped

### minor d-b4 (applies to BOTH units)

`v10/note-d46b-martin-at-transport.md` §4 and
`v10/note-d46d-typicality.md` §4 are **unchanged and unmarked**.  §4 of
D46b still reads, in full assertive form:

- "**MB2/MB4 — THE GROWTH PARAMETER EXCEEDS 2 AND RISES** ... deliveries add branching" (line 74-79) — withdrawn;
- "a contraction ratio **~0.738 per level**" (line 86) — withdrawn;
- "**MB5 — THE DELIVERY-FREE root = renewal IDENTITY DOES NOT TRANSFER** ... **Reconvergence restores HOLDINGS without restoring the FUTURE**" (line 91-98) — withdrawn by name in §5, LOG #398 and the receipt;

and its heading still says "round **queued behind** paper-32's and
D46a/D46c's", which is no longer true.  D46d §4 likewise still carries
"**WIDTH SPREADS WITH DEPTH UNDER THE THEORY'S OWN LAW**" (line 93) and
"the same idles D45b found **LOAD-BEARING**" (line 81).

The retractions exist — in §5 — and LOG #399's "grep discipline" claim
("each surviving hit sits inside an explicit withdrawal") is **true of
the source and the `.out`, and false of the notes' §4**.  This is the
sibling round's pattern (ii) in mirror image: a reader, a grep, or a
future paper-drafting pass that lands on a "## 4. Result" section gets
the withdrawn headline with nothing on the page to warn it.

**Prescribed fix.** Stamp §4 in place in both notes — a heading marker
(`## 4. Result [SUPERSEDED — see §5 amendments and §6 repairs]`) and a
one-line strike on each of the four withdrawn paragraphs. Do not delete
the text; the record of what was claimed is the point.

### nit d-b5 — two loose sentences in the amendments

1. `note-d46b` §5 B6: "the transport ladder is exactly {2: 3757, 5/2: 212}, confirmed independently **on both sides**".  What was confirmed on both sides is the **value set** `{2, 5/2}`; the multiplicities 3757/212 are transport-only (delivery-free at the same cap is 1067/124, and 5963/508 to depth 5).  The receipt's MB1-b states this correctly — the note sentence should match it.
2. LOG #399's "verified pre-commit: both receipts exit 0, independent reruns BYTE-IDENTICAL, **determinism across seeds**" — d46b carries no seeds (its MB0-b says so explicitly and gates traversal-order independence instead, which is the right fix for round-1 B-m2).  The phrase is the same import that produced B-m2 in the first place.  `note-d46b` §4's "seeds byte-identical" is also still unannotated (covered by d-b4).

## D-4. The declared non-application: ACCEPTED

The coordinator declined to extend D46d's doctrine scan over the note
and the LOG entry, on the ground that gating a receipt on author-owned
files under active edit would make it non-reproducible from the repo
state the receipt controls.

**The referee accepts this and does not ask for it to be revisited as a
receipt gate.**  The reasoning is sound and the scope is declared
in-gate, which is what the round asked for.  One rider: the exposure the
suggestion was aimed at is then unmitigated by *any* gate — and d-b4
above is an instance of exactly that class (a withdrawn claim standing
un-stamped in an author-owned file).  The right home for it is an
authoring/pre-commit check outside the receipt, not inside it.

## D-5. New attacks on the new controls (D46d)

### MAJOR d-d1 — TY5-c's AST scan does not reject one of the three round-1 gates it names

**Where.** `vacuity_scan` docstring (receipt lines 787-791): *"Round 1,
D-M4: three gates could not fire (`isinstance(conc, bool)`,
`0 <= x <= 1`, `isinstance(gap, Fr)`).  This AST scan ... rejects
predicates that are constant by construction."*  The TY5-c label makes
the same claim.

**The defect.** The referee lifted the committed `vacuity_scan` out of
the source and ran it on the three round-1 predicates verbatim:

| round-1 predicate | scanner |
|---|---|
| `isinstance(conc, bool)` | **CAUGHT** |
| `lt4 == 1 and isinstance(gap, Fr)` | **CAUGHT** |
| `0 <= mass_ge4 <= 1 and 0 <= mass_ge6 <= 1` | **PASSED** |

The one that passes is precisely the predicate mutant **d4** walked
through in round 1.  A chained comparison parses as a single `Compare`
with **two** ops and `LtE` operators, so it misses the scanner's
`len(sub.ops) == 1` + `Gt/GtE` + `Constant(0)` pattern on all three
counts.

**Standing.** No *live* gate in either repaired receipt is vacuous —
the referee re-ran the scan over both files and confirms the reported
"vacuous predicates = none" is true of what is actually there.  So this
reverses nothing.  What is wrong is the **advertised coverage**: a
control that names a shape as covered and does not cover it is the same
species of defect the control was built to catch.

**Prescribed fix.** Add the chained/`Lt`/`LtE` case (any `Compare`
whose comparator set is entirely literal constants), or amend the
docstring and label to name the two shapes actually covered.

### minor d-d2 — the doctrine scan catches the round's own mutant, and is defeated by any of its fifteen markers

The coordinator asked the referee to verify the catch and to try
another smuggle.  The referee lifted `doctrine_scan` out of the
committed source and probed it directly:

| line | scanner |
|---|---|
| `the generated record has spacetime dimension 3+1, not fewer` (the round's mutant-d5 line) | **CAUGHT** — as claimed |
| `order dimension is a clock-complexity grade, never a spacetime-dimension estimator` | **passed** — correct |
| `the measured width shows the spacetime dimension of the record is 3+1` | **SMUGGLED THROUGH** (marker `width`) |
| `the event poset fixes the spacetime dimension of the world at 3+1` | **SMUGGLED THROUGH** (marker `poset`) |
| `the spacetime dimension of the generated record is 3+1 and never otherwise` | **SMUGGLED THROUGH** (marker `never`) |
| `these records live in four dimensions of real physical space and one of time` | **CAUGHT** (the `dimen`+`sion` needle) |

**The verification the coordinator asked for is positive**: the repair
does catch the round-1 mutant, and the bare `'no '`/`'not '` exemptions
really are gone.  But `'never'` is still in `_DMARKERS` — a bare
negation by any other name — and `'width'`, `'poset'`, `'crown'`,
`'proxy'`, `'grade'`, `'d44c'` and `'d45b'` are common enough words
that any real doctrine violation in this unit would almost certainly
share a line with one of them.

**Prescribed fix (minor).** Drop `'never'`; require the marker to be
one of the genuinely scoping phrases (`order dimension`,
`order-dimension`, `clock-complexity`, `scan-exempt`, `note-d45b`), and
declare in-gate that the scan is a fixed-vocabulary check, not a
semantic one.

### confirmed: the new D46d headline IS gated

**Mutant dR4** inverts the fixed-depth pool-scaling verdict
(`t_decays` negated at the point of use): **exit 1, 16 PASS / 1 FAIL**,
`TY4-c` fires.  Round 1's D-M4(2) — a headline resting on
`0 <= x <= 1` — is closed: the discriminating scaling that now carries
the unit's reading is anchored count by count.

## D-6. Delta mutation tables

**D46b (against commit `e0721f5`):**

| # | mutation | round 1 | after repair |
|---|---|---|---|
| b3 | witness delivers `v0` | 0 / 12 PASS | **1 / 17 PASS, 2 FAIL** (MB5-a, MB5-b) |
| b5 | contraction reversed | 0 / 12 PASS | **1 / 18 PASS, 1 FAIL** (MB3-e) |
| b6 | growth sign reversed | 0 / 12 PASS | **1 / 18 PASS, 1 FAIL** (MB4-b) |
| b7 | matched-horizon agreement broken | — | **1 / 18 PASS, 1 FAIL** (MB5-b) |
| b8 | hoisted vacuous predicate | — | 0 / 20 PASS — **survives** (d-b1) |
| b9 | `len>=1`, `type() is`, `> -1` | — | 0 / 20 PASS — **survives** (d-b2) |
| b10 | undisclaimed "R-recurrent / Martin limit at infinite depth" | — | 0 / 19 PASS — **survives** (d-b3) |

**D46d (against commit `e0721f5`):**

| # | mutation | round 1 | after repair |
|---|---|---|---|
| dR4 | fixed-depth pool scaling inverted | (d4: 0 / 11 PASS) | **1 / 16 PASS, 1 FAIL** (TY4-c) |
| scanner probes | the two scanners lifted from source and probed on 6 doctrine lines + 12 predicate shapes | — | mutant-d5 line **caught**; 3 doctrine smuggles and 8 predicate smuggles **survive** (d-d1, d-d2) |

(The four full-run scanner mutants were terminated once the isolated
probes settled the question conclusively — the scanners are pure
functions of the source text, so probing them directly is equivalent
and does not require a 15-minute sampling run.)

---

## D-7. DELTA VERDICT

| unit | delta verdict | new BLOCKER | new MAJOR | new minor | new nit |
|---|---|---|---|---|---|
| **D46b** | **DELTA-CLEAN** — every round-1 finding addressed; both reversals gated; the strengthened contraction credited and anchored | 0 | 0 | 3 | 1 |
| **D46d** | **DELTA-CLEAN** — headline retired and replaced by a gated discriminating scaling; law named; three proxies; both dropped pin halves delivered | 0 | 1 | 2 | 1 |

**Both units convert.**  The terminal statements as stamped are
**accurate** and the referee confirms them.  Specifically:

- Every reversal is now produced by a gate rather than narrated, and
  the four round-1 survivor mutants all exit 1.
- Every number in both repaired receipts that the referee could
  recompute — the matched-horizon masses, the renewal census, the
  two-family ratio table, all three drift norms, the conditional at and
  off the root, the three-proxy exact masses, all three sampled
  scalings, **and the entirely new TY1-c poset-width profiles** — was
  recomputed independently and agrees exact rational for exact
  rational.
- The retractions in note §5 (both units) and LOG #398 state the
  findings accurately, including the two the coordinator asked about by
  name: "reconvergence restores HOLDINGS without restoring the FUTURE"
  and "WIDTH SPREADS WITH DEPTH UNDER THE THEORY'S OWN LAW" are both
  withdrawn explicitly.  **LOG #399 does not overstate** what the
  repairs establish; its scope language ("evidence at the reachable
  horizons", "no existence claim", "upper-bounds the dimension mass",
  "calibrated at the single pair where both are computable") is
  correct.

**One condition on conversion (d-b4, two-line edit).** Stamp §4 in
place in both notes as SUPERSEDED.  As committed, a reader landing on
`## 4. Result` gets "THE GROWTH PARAMETER EXCEEDS 2 AND RISES",
"reconvergence restores HOLDINGS without restoring the FUTURE" and
"WIDTH SPREADS WITH DEPTH UNDER THE THEORY'S OWN LAW" asserted in full,
with nothing on the page saying they were withdrawn.  LOG #399's grep
discipline holds for the source and the `.out`; it does not hold for
the notes' §4.  This is the one residue that reaches a reader.

**Carried forward to round 2 (none blocking):** d-b1, d-b2, d-b3,
d-d1, d-d2 — five control-hygiene items, all of the same shape: a
scanner whose *label* claims more coverage than its *implementation*
has.  No live gate in either receipt exploits any of them, and no
delivered claim depends on them.

**Two wording riders for the stamped terminal statements (nits).**

1. D46b's "the kernel candidates are proper at every relative horizon"
   — MB3-a gates r = 1..6 at the root, r = 1 family-wide (30,729
   histories) and r = 2 family-wide (3,969).  Read "at every computed
   relative horizon".
2. D46d's "calibrated to < 1e-2" — the calibration has **one** anchor
   (pool 4, depth 3), which TY3-a states honestly in-gate.  If the
   author wants more anchors, the referee's are available and free:
   pool 5 / depth 3 gives `1539/5646080` (~2.73e-4) over 42,065
   terminals and pool 6 / depth 3 gives `5451/19210880` (~2.84e-4) over
   109,212 terminals — the two pools the sampled arm actually uses.
