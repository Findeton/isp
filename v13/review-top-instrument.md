# TOP — HOSTILE REVIEW R3 (INSTRUMENT LENS)

**Reviewer:** R3, the instrument lens.  **Protocol:**
`v13/note-top-hostile-protocol.md` (FROZEN, v13 #302), kill-shots K1–K5,
primary weight on **K5**.  **Pin:** `v13/note-top-topology-pin.md`.
**Object reviewed, SHA-256 verified before reading a line of it:**

| artifact | declared | measured | ok |
|---|---|---|---|
| `v13/paper-top-topology.md` | `ab09d091ed1d` | `ab09d091ed1d…` | yes |
| `v13/code/top_topology_exact.py` | `e2d0200e4a06` | `e2d0200e4a06…` | yes |
| `v13/code/top_topology_output.txt` | `bd213b18d1b1` | `bd213b18d1b1…` | yes |
| `v13/code/top_topology_receipt.json` | `0fb290cf4bfd` | `0fb290cf4bfd…` | yes |
| `v13/code/tb3_third_base_receipt.json` (the pin source) | `c9bc956fe751…` (typed in the instrument) | `c9bc956fe751…` | yes |

**Independent recomputations and probes performed: 434 recomputed values**
(172 of them anchor-provenance traces), from **six from-scratch
reimplementations** and **41 top-level executions of the instrument** (2 clean
delivery runs, 20 hostile source injections, 3 corrupt-and-fire runs, 15
receipt-emission runs, 1 timing run; the two delivery runs spawned a further 58
mutant subprocesses).  The reimplementations use a deliberately different
representation and a different algorithm — dense tuple-of-tuple `Fraction`
matrices against the instrument's sparse-column `Mat`, and full Gauss–Jordan
reduction to RREF against the instrument's pivot-dictionary partial elimination
— and import nothing from `top_topology_exact.py`.  All scratch work is in the
session scratchpad; no repository file was modified other than this review.

---

## 0. Summary

**The measurements are sound and the instrument is, by v13 standards, a strong
one.**  My from-scratch rebuild reproduces the reference invariant row exactly —
36 charts, 5,436 1-cells, 204,384 2-cells, `b = (1, 140, 199,123)`,
χ = 198,984, rank ∂₂ = 5,261 — together with the coherent row (84,720 → 161),
the whole per-checkpoint decomposition, the wing quotient `(1, 25, 33,138)`,
the entire 5,040-completion selector census including the 252 and its
`{1:4, 2:48, 3:72, 4:128}` distribution, and all three manifold standards.  Two
full delivery runs are **byte-identical to the frozen artifacts**.  The
196 anchors all pass, and each one is genuinely exit-1: I broke two anchors that
no gate predicate references and the run still exited 1 with `failed_gates: []`.

**K5(b) is met.**  I reconstructed the OR-vs-XOR boundary-row bug, confirmed the
quotient delta **b₁ = 24 (OR) versus 25 (XOR)** on my own instrument, and
confirmed that injecting it into the delivered source kills a delivered
must-pass gate (`TOP-QUOTIENT`).  The bug the construction caught is now a bug
the instrument catches — with a residue, recorded as F8.

What fails is, again, the instrument's **account of itself**, plus one delivered
number:

1. the verdicts' **computed qualifiers are ungated** — a typed literal survives
   in all three (MAJOR, and a **recurrence** of TB3-R3's F1 against this unit's
   own immutable base);
2. the atlas's **`link` and `star`** computations have **no falsifier**; the
   declared `link-lax` mutant dies on the *control* code path, not the audited
   one, and the load-bearing 16,998 can be replaced by 0 with zero failures
   (MAJOR);
3. §5.2's **C7 clause-(c) cell is a false number** — the paper prints `0`,
   bolded as a pass; the instrument measured `6` and so do I, with six explicit
   witnesses (MAJOR).

Four moderate items (F4–F7) and five minor ones (F8–F12) follow.  Nothing I
found overturns a claim about the atlas's topology.

**Grade: ACCEPT-WITH-FIXES** (stated in full at the end).

---

## 1. MAJOR — F1.  The verdicts' computed qualifiers are ungated; three probes survive

**Claim under test.**  §8: "Each verdict string is derived **inside** a gate
from the measured counts, re-derived there independently of the emitter, and a
verdict-flip mutant proves the derivation can fail."  RUNBOOK §13 addendum
(#234): "the printed verdict string must be derived inside a gate from the
measured counts … an ungated verdict is a typo away from fiction."

**Evidence.**  Three source perturbations, each replacing exactly one *computed
qualifier* inside `⟨…⟩` by a literal while every recorded table keeps its
measured value.  Each ran to completion:

| probe | perturbation | receipt fields changed | result |
|---|---|---|---|
| **H10** | unit verdict's `ref["b1"]` → `141` | **1** (`findings/unit_verdict`) | **exit 0**, `must_pass_failures: 0` |
| **H11** | manifold verdict's link b₁ → `16999` | **1** (`findings/manifold_verdict`) | **exit 0**, `must_pass_failures: 0` |
| **H12** | selector verdict's `len(locus)` → `385` | **1** (`findings/selector_verdict`) | **exit 0**, `must_pass_failures: 0` |

H10's delivered verdict string, emitted with zero failures:

```
TOP-GLOBAL-STRUCTURE-<charts 36, 1-cells 5436, 2-cells 204384; components 1,
cycle rank 5401, chi 198984, F_2 ranks (b0,b1,b2) = (1,141,199123); ...>
```

while `tables/q1_invariants/…/the_nerve_N/b1` in the same receipt still reads
`140`.  H12 emits "the order-2 locus holds **385** completions" beside a
candidate table that says 384 in thirteen places.

What is actually re-derived is the verdict **name**, never the qualifier:

- `TOP-VERDICT` (line 2727): `unit.startswith(derived)` where `derived` is
  `"TOP-GLOBAL-STRUCTURE-"` or `"TOP-BLOCKED-AT-"`.  The prefix ends before the
  `<`.
- `TOP-DIM-READING` (line 1813): `manifold_verdict.startswith(derived.split("<")[0])`
  — the `split("<")` explicitly discards everything the qualifier contains.
- `TOP-SELECTOR` (line 2113): checks `bool(derived_named) ==
  verdict.startswith("TOP-FANO-SELECTOR-<")` and the pre-registered vocabulary.
  The interpolated 13 / 2 / 384 / 48 / 252 / `(1,2,3,4)` are never rebuilt.

`verdict-flip`, the mutant §8 names, moves the *branch* (`unit` becomes
`TOP-BLOCKED-AT-<the nerve>`), which the prefix check catches.  It proves the
branch derivation can fail.  It says nothing about the qualifiers, and no
declared mutant does.

**This is a recurrence.**  `v13/review-tb3-instrument.md` §1 raised exactly this
finding as MAJOR against TB3 — the unit that is TOP's immutable base — and
recommended "rebuild the qualifier string from `tab` inside the gate and gate it
against `FINDINGS[…]`".  TOP's §8 states a *stronger* guarantee than TB3's §10
did, and the repair was not carried across.

**Severity: MAJOR** — as a claim.  All three qualifiers are, as delivered,
numerically correct (I recomputed 140, 16,998, 384, 48, 252 independently).
What is false is the guarantee attached to how they are printed.

**Repair.**  (a) In each of the three gates, rebuild the full verdict string
from the recorded tables and gate string equality against the emitted one.
(b) Declare three typed-value mutants (`unit-typed`, `manifold-typed`,
`selector-typed`) so the falsification census records that the qualifier
derivation can fail.  (c) Failing (a)–(b), replace §8's sentence with the true
one: "each verdict's *branch* is derived inside a gate; its qualifiers are
interpolated from the recorded tables and are not separately gated."

---

## 2. MAJOR — F2.  The atlas's `link` and `star` have no falsifier; `link-lax` dies on the control path

**Claim under test.**  §4.1 declares the estimator as the triple
(`dimprofile`, `star`, `link`) and says its per-cell dimension "is cross-checked
inside its gate against a component census … a comparator built independently of
the estimator it audits."  §4.2 rests on "every link has b₁ = 16,998" — the
number that carries the paper's deepest §4 sentence ("a link is never a circle
and the uniformity is NOT manifoldhood") and appears verbatim inside the
`TOP-MANIFOLD-READING-CONSISTENT` verdict.  The mutant table declares `link-lax`
("the vertex link built from the 1-cells alone … so it is a star and never a
circle") as its falsifier.

**Evidence.**  `link-lax` flips **two** functions at once — `local_profiles`
(line 1579, the atlas path) and `control_links` (line 1645, the control path).
I injected the identical bug class into **`local_profiles` alone**:

| probe | perturbation | result |
|---|---|---|
| **H9** | atlas link built from the 1-cells alone; `control_links` untouched | **exit 0**, `must_pass_failures: 0`, **17 receipt fields moved** |
| **H16** | `star` inflated by +1 at every chart, both components | **exit 0**, `must_pass_failures: 0` |

Under H9 the delivered numbers move and nothing objects:

| field | frozen | H9 |
|---|---|---|
| reference `link_V_E_b0_b1` | `[35, 17032, 1, **16998**]` | `[35, **34**, 1, **0**]` |
| partially-symmetric majority link | `[35, 4828, 1, 4794]` | `[35, 34, 1, 0]` |
| partially-symmetric witness link | `[35, 4648, 1, 4614]` | `[35, 34, 1, 0]` |
| asymmetric common link | `[35, 3010, 1, 2976]` | `[35, 34, 1, 0]` |
| negative control's witness link | `[…, 5282, …, 5248]` | `[…, 34, …, 0]` |

and the emitted verdict duly prints the corrupted number.

The reason is structural.  `TOP-DIM-READING`'s predicate is
`ok_vocab and manifold_verdict.startswith(derived.split("<")[0]) and dim_cross`,
and `dim_cross` (lines 1720–1733) compares **only** `dimprofile` against its
comparator.  Neither `star` nor `link` is compared with anything, at any
instance, in any gate.  `link-lax` dies solely on `TOP-DIM-CONTROLS`, whose
predicate reads `ctrl[…]["every_link_is_a_circle"]` — a value produced by
`control_links`, a *different implementation on different data*.  This is
RUNBOOK §14 verbatim ("a wholesale-replacement mutant does not test that the
RIGHT invariant is computed") layered on the #38→#40 disease: the mutant's death
is carried entirely by the code path that is not under audit.

**Severity: MAJOR.**  Two of the three components of the *declared estimator* —
including the one the manifold verdict quotes — are computed by an ungated path.
The delivered values are correct (I recompute `star = (302, 17032)` and
`link = (35, 17032, 1, 16998)` at all 36 charts from scratch), so no number in
the paper is wrong; the falsification census, which reports `never_falsified:
EMPTY`, is nevertheless blind here because it counts *gates*, not code paths.

**Repair.**  (a) Add to `TOP-DIM-READING` an independent comparator for the
other two components — the identities `Σ_v star_e(v) = 2|E|`,
`Σ_v star_f(v) = 3|F|` and `link_E(v) = star_f(v)` are computable from the cell
counts alone and pin both.  (b) Split `link-lax` into `link-lax-atlas` and
`link-lax-control` so each implementation carries its own falsifier.  (c) Add a
`star-lax` mutant.

---

## 3. MAJOR — F3.  §5.2's C7 clause-(c) cell is a false number

**Claim under test.**  §5.2's table row `| C7 | involutive profile | 12/384 | 8 |
**0** | 20 | **0** |`, with the bolded `0` marking a passed clause, and the
prose beneath it: "C4, C5, **C7**, C9 and C10 predict linearity perfectly."

**Evidence.**  The instrument's own receipt disagrees with its paper:

```
tables/q3_selector/the_candidate_table/C7:
    c_completions_with_a_non_linear_K = 6        <-- paper prints 0
    clauses_passed = 0
```

My independent census over all 5,040 completions returns **6**, and names them.
Twenty completions satisfy C7 (`ord(d_P(q)) ≤ 2 for every P ∈ S₃`); six of them
have a defect subgroup containing a non-linear element:

| Q | ord[P*] | \|K\| | linear elements of K |
|---|---|---|---|
| `(0,1,2,5,4,3,7,6)` | 2 | 4 | 1 |
| `(0,1,2,6,4,7,3,5)` | 2 | 4 | 1 |
| `(0,1,2,7,4,6,5,3)` | 1 | 4 | 1 |
| `(0,6,5,1,3,7,4,2)` | 2 | 4 | 1 |
| `(0,6,5,2,3,4,7,1)` | 2 | 4 | 1 |
| `(0,6,5,7,3,1,2,4)` | 1 | 4 | 1 |

Each has `|K| = 4` with the identity as its only F₂-linear element.  So C7
passes **none** of the three clauses, exactly as the receipt's
`clauses_passed = 0` records, and the paper's table and prose both present it as
passing clause (c).

I swept the remaining 64 cells of the §5.2 table against the receipt: **all 64
agree.**  I swept 67 further paper-table checks (§3.1, §3.2, §3.3, §3.4, §4.2,
§4.3, §5.1, §5.3, §6.2, §6.3, §7.1, §7.2, §10) against the receipt: **all
agree.**  C7's (c) is the single false number I found.

**Severity: MAJOR** — a delivered table carries a number the instrument did not
measure, presented with the typographic mark that means "this clause passed".
It does **not** move the verdict: `TOP-FANO-SELECTOR-NOT-FOUND` is unchanged
(no candidate passes all three either way), and "the best reach 2 of 3" is
C1/C2/C8, unaffected.

**Repair.**  Set the cell to **6**; strike C7 from the sentence "C4, C5, C7, C9
and C10 predict linearity perfectly" (leaving C4, C5, C9, C10); optionally note
that C7 passes 0 of 3.  No recomputation is required — the receipt is right.

---

## 4. MODERATE — F4.  Three "external" anchors have a declared side typed in the instrument, and are structurally incapable of failing

**Claim under test.**  §2.1: "**196 anchors** are then gated exit-1 against the
pinned receipt's own bytes."  §10: "**172 external** (TB3's hash-pinned
receipt) and **24 declared-standard**."

**Evidence.**  I wrote an independent tracer that reads the TB3 receipt and
resolves each anchor's declared side to a real path in it.  Of the 172
external-labelled anchors, **168 trace exactly**; four do not:

| anchor | why not |
|---|---|
| `A-PIN-TB3` | declared side is the SHA-256 typed in the instrument (the source string says so: `"this file, pinned SHA-256"`) — legitimate, but it is a self-pin, not a read |
| `A-TG-NODES-equivariant completion` | declared side is the literal `30` |
| `A-TG-NODES-a different declared transposition` | declared side is the literal `30` |
| `A-TG-NODES-an asymmetric setting` | declared side is the literal `30` |

`run_transport_controls` (lines 2461–2464) builds the three negative controls'
comparison dictionaries as `{"links": cm["links"], "identification_links":
cm["identification_links"], "cycle_rank": cm["cycle_rank"], **"nodes": 30**}` —
the first three read from the TB3 receipt, the fourth typed.  I verified that
`tables.negative_controls.per_control[*]` in the TB3 receipt carries **no
`nodes` field at all**, so there is nothing to read.  Worse, the computed side
is `len(nodes) = |FRAMES| × |CKPTS| = 6 × 5`, which is 30 for every input at
three wings: these three anchors **cannot fail**.

`TOP-ANCHOR-PROVENANCE` cannot see this.  Its predicate only checks that each
anchor's `source` **string** is a key of `ANCHOR_PROVENANCE`; it never asks
whether an "external" anchor's declared value came from external bytes.  It is a
vocabulary check wearing a provenance label.

**Severity: MODERATE.**  Bookkeeping, not science — 30 is forced by A-FRAMES
(6) and A-CKPTS (5), both genuinely external.  But the failure class is exactly
the one the RUNBOOK failure catalogue records at ledger #24 ("hard-coded 6561
(true 729) survived unit + round → counts computed, never typed"), and the
honest split is **169 external / 3 typed-structural / 24 declared-standard**.

**Repair.**  (a) Replace `"nodes": 30` by `len(sp.FRAMES) * len(sp.CKPTS)` and
relabel those three anchors `DECLARED-STRUCTURAL`, or drop them.  (b) Correct
§10's "172 external" and §2.1's "gated exit-1 against the pinned receipt's own
bytes" (false for the 24 declared-standard and the 4 above; §10 and deviation 10
already state the 24 correctly).  (c) Strengthen `TOP-ANCHOR-PROVENANCE` to
require that every anchor claiming external provenance names the receipt path
its declared value was read from, and gate that the path resolves.

---

## 5. MODERATE — F5.  `provenance-lax` is a waiver declared as a computation mutant; both denominators in §10 are off by one

**Claim under test.**  §10: "falsified by a **computation** mutant | 26 of 28"
and "falsified **only by a waiver** | 2, named: `TOP-EXACTNESS`,
`TOP-NO-MUTANT-EXEMPTION`", with §10's own definition: "A waiver registers a
value in a gate's own evidence list **after that gate's sweep has run**."

**Evidence.**  `run_anchor_provenance` (lines 2617–2627):

```python
for a in ANCHORS:
    p = ANCHOR_PROVENANCE.get(a["source"])
    ...
if register_a_bad_label:          # MUTANT == "provenance-lax"
    unknown.append("injected")
```

The append happens **after** the sweep over `ANCHORS`.  No anchor is ever
registered with a bad provenance; no computation is perturbed.  That is the
unit's own definition of a waiver, and it is structurally identical to
`float-lax` and `exempt-lax`, which *are* declared waivers.  The receipt
confirms `provenance-lax` falsifies `TOP-ANCHOR-PROVENANCE` and nothing else,
and that no other mutant reaches that gate.

**Consequence.**  The honest kind split is **26 computation / 3 waiver**, the
waiver-only set is **3** — `TOP-EXACTNESS`, `TOP-NO-MUTANT-EXEMPTION`,
**`TOP-ANCHOR-PROVENANCE`** — and "falsified by a computation mutant" is
**25 of 28**, not 26.  §10's decision to report both denominators "because they
differ" is the right instinct; the classification underneath it is wrong.

**Severity: MODERATE.**  `never_falsified` remains **EMPTY** at the honest
denominator of 28 either way (I verified the denominator: 30 gates − 1
disclosure `TOP-EULER-POINCARE` − `TOP-FALSIFICATION`, which is excluded and
named).  What moves is which gates are certified to catch a *computational*
defect.

**Repair.**  Reclassify `provenance-lax` as a waiver and update §10's two
counts and the named waiver-only list; or replace it with a genuine computation
mutant that registers a real anchor with an undeclared source string (e.g. one
`anchor(...)` call given `"TB3 receipt"` instead of `"TB3 committed receipt"`).

---

## 6. MODERATE — F6.  `TOP-SIMPLICIAL`'s χ clause is analytically forced, and the maximal-face size is never gated

**Claim under test.**  §3.1: χ of the simplicial nerve is "computed as an exact
alternating binomial sum **and** predicted independently by the cone argument" —
presented as two routes — and "at the reference instance the unique maximal face
is the whole 36-chart set".  Appendix deviation 3 correctly disclaims χ-from-Betti
as "an algebraic identity in the ranks … recorded as a disclosure".

**Evidence.**  Σ_{j=1..k} (−1)^{j+1} C(k,j) = **1 for every k ≥ 1**; I evaluated
it for k = 1…40 and the value set is `{1}`.  So `chi_route_1_alternating_
binomial_sum == 1` is true for *any* maximal face of any size — it is exactly
the same class of analytically-forced clause the unit caught for χ-from-Betti,
and missed here.  RUNBOOK §14 addendum (#208): "Analytically-forced clauses
(true by algebra for every input) are disclosures, not must-pass gates."

The consequence is measurable:

| probe | perturbation | result |
|---|---|---|
| **H13** | the unique maximal face replaced by a 12-element subset of itself | **exit 0**, `must_pass_failures: 0`; `maximal_face_sizes` **36 → 12** and `top_dimension` **35 → 11** at all four 36-chart instances |

The gate's `simp_cone` is `(len(maximal) == 1) and (chi == 1)`.  The first
conjunct is a genuine measurement (a complex with a unique maximal face is a
simplex, hence a cone, hence contractible — the argument is sound).  The second
is a tautology.  The number the paper defends — that the face is the **whole
36-chart set**, hence Δ³⁵ — is reported and never gated.  `simp-lax`, the only
mutant aimed at this clause, flips the *expected constant* from 1 to 0 and never
exercises the sum.

**Severity: MODERATE.**  The delivered value is right (`maximal_face_sizes:
[36]`, `top_dimension: 35`, and I independently confirm the overlap graph is
K₃₆ with 630 edges and that all ten coordinate-cell graphs are disjoint unions
of complete graphs).  What is overstated is that it was checked.

**Repair.**  Demote the binomial χ to a disclosure beside `TOP-EULER-POINCARE`;
add `maximal_face_sizes == [len(charts)]` at the reference instance and
`== [6]` at the equivariant control to `TOP-SIMPLICIAL`'s predicate; reword
§3.1 so the cone argument is the route and the binomial sum is a consistency
print.

---

## 7. MODERATE — F7.  Burnside's floor division absorbs a fixed-cell census error of 1–5

**Claim under test.**  §6.3: orbit counts "by two genuinely independent routes —
direct enumeration … and Burnside's lemma applied to the fixed-cell census".
§6.2's table (each transposition fixes **180** 1-cells, each 3-cycle **120**
2-cells) and §6.3's "the fixed-cell census accounts for the whole of it".

**Verdict on independence: the route pair is legitimate.**  Unlike χ-from-Betti,
the two routes consume *different data* — direct enumeration reads images under
the action, Burnside reads a separately-computed fixed-cell census — and neither
is derived from the other by algebra on the same measured numbers.  I reproduced
both from scratch: `(6, 996, 34104)` by enumeration and by
`(5436+180·3)/6 = 996`, `(204384+120·2)/6 = 34104`.  Dropped-orbit probes bite:

| probe | perturbation | result |
|---|---|---|
| **H6** | one 2-cell orbit dropped from the direct enumeration only | **exit 1**, `TOP-ORBITS` |
| **H5** | one 1-cell orbit dropped from the direct enumeration only | **exit 1** (the gate registers 995 ≠ 996; the process then dies in `eo[x]` before printing) |

**The defect is the divisor.**  `bv/be/bf` use `//` (floor):

| probe | perturbation | result |
|---|---|---|
| **H7** | every non-identity element's fixed-1-cell count inflated by +1 | **exit 0**, `must_pass_failures: 0`; §6.2's published census moves `ACB/BAC/CBA: 180 → 181`, `BCA/CAB: 0 → 1` |

`(5436 + 181·3 + 1·2) // 6 = 5981 // 6 = 996`, unchanged.  The fixed-cell
census has no second route and no external anchor, so an error of 1–5 in its
total is invisible.  Note `5981 mod 6 = 5` — an exact-divisibility gate would
have caught it immediately.

**Severity: MODERATE.**  The delivered census is correct (I reproduce
180/180/0/0/180 and 0/0/120/120/0 independently, along with the orbit-size
histograms 816×6 + 180×3 = 5,436 and 34,044×6 + 60×2 = 204,384, and the −50
correction from the 90 and 40 excesses).  The gate simply cannot certify it.

**Repair.**  Gate `sum(fix) % |G| == 0` for all three dimensions, and gate the
orbit-size histograms against the cell counts (`Σ size·count = |E|`, `= |F|`),
which pins the census exactly.

---

## 8. K5(b) — THE OR-vs-XOR BUG: reconstructed, delta confirmed, gate confirmed, with a residue (F8, MINOR–MODERATE)

**Reconstruction.**  The buggy version replaces the mod-2 boundary row
`(1 << a) ^ (1 << b)` by an incidence bit pattern `(1 << a) | (1 << b)`.  On the
nerve `N` this is inert — every 1-cell joins two *distinct* charts — so the bug
bites only where a cell meets a face twice, which is exactly the wing quotient.
I measured that the quotient's 1-skeleton carries **240 loop 1-cells** (`a == b`,
because both endpoint charts share a seed), and that a loop's OR row
`(1<<a)|(1<<a) = 1<<a ≠ 0` contributes a spurious pivot.  On my own
implementation:

| quotient complex | rank ∂₁ | b₀ | cycle rank | **b₁** | b₂ | χ |
|---|---|---|---|---|---|---|
| **XOR (correct)** | 5 | **1** | 991 | **25** | 33,138 | 33,114 |
| **OR (the bug)** | 6 | **0** | 990 | **24** | 33,138 | 33,114 |

**The stated delta 24 vs 25 is confirmed exactly**, and the mechanism is
isolated: b₂ and χ do not move; b₀, the cycle rank and b₁ do.

**A delivered gate now catches it.**  Injecting the bug into the delivered
source:

| probe | perturbation | result |
|---|---|---|
| **H1** | OR in `d1_rows` | **exit 1**, `TOP-QUOTIENT`, `TOP-VERDICT` |
| **H2** | OR in `d1_rows` and `d2_rows` | **exit 1**, `TOP-QUOTIENT`, `TOP-VERDICT` |

`TOP-QUOTIENT`'s clause `components_route_1_union_find ==
components_route_2_F2_rank` fires: union-find still returns 1, the F₂-rank route
returns 6 − 6 = 0.  **K5(b) is satisfied** — the bug the construction caught by
luck is a bug the instrument catches by design.

**Residue (F8).**  Three sibling bugs of the same class in the same file are
*not* caught:

| probe | perturbation | result |
|---|---|---|
| **H3** | OR in `d2_rows` alone | **exit 0**, zero receipt fields changed (inert on this data: rank ∂₂ = 966 either way) |
| **H4** | OR in the transposed-column accumulation (`cols[a] ^= …` → `|=`) | **exit 0**, `must_pass_failures: 0`, while the quotient's published `components_route_3_transposed_rank` goes **1 → 0** and `rank_d1_transposed` **5 → 6** |

`TOP-QUOTIENT` compares only routes 1 and 2; `TOP-COMPONENTS` compares all four
but runs only on the five nerve instances, where routes 2 and 3 agree trivially
because there are no loops.  So the quotient publishes a component count of 0 —
an impossibility for a non-empty complex — with zero failures.  And
`TOP-QUOTIENT`'s **only** declared falsifier is `rank-lax`, which disables the
elimination globally: the gate that catches the historical bug has no mutant
that exercises it specifically.

**Repair.**  (a) Declare the OR/XOR bug itself as a mutant — it is this unit's
own history and belongs in the table.  (b) Extend `TOP-QUOTIENT` to gate all
four component routes.  (c) Gate that the quotient's loop count is > 0, so the
mod-2 convention is exercised by construction rather than by circumstance.

---

## 9. MINOR findings

**F9.  The H₂-additivity measurement is real but has no declared falsifier.**
Deviation 4's claim is that the instrument "**measures** that additivity rather
than assuming it".  I verified the measurement is genuine and true:
Σ_t b₂ᵗ = 199,123 = b₂(N) and, for the coherent sub-nerve, Σ_t b₂ᵗ = 79,480 =
b₂(N_coh); and the second route to b₁ reproduces exactly,
`1 + 144 + 0 − 5 = 140` and `1 + 144 + 21 − 5 = 161`, with the 21 coherent
classes matching §3.4's `161 − 1 − 144 + 5`.  But **H14** (hard-coding the
additivity clause to `True`) exits 0, and no declared mutant makes additivity
false, so the clause's load-bearingness is undemonstrated.  A falsifier exists —
**H15** (dropping one 2-cell from each per-checkpoint sub-complex only) exits 1
on `TOP-HOMOLOGY` — it is simply not declared.  *Repair: declare H15.*

**F10.  §2.1's anchor tally is wrong in one row.**  "the committed two-wing and
three-wing transport graphs | **24** anchors": the actual count is
`A-2W` (14) + `A-TG` (16) = **30**.  (24 is the `A-CTRL` count — a likely copy
slip.)  Every other row of that table checks out: 64/6/5/6, `(0,3,2,1,4,5,6,7)`,
36/6 at five instances, 50 cells, 1,226,304 with its five parts, 6 defect
values, 5,040 with 48/384/1728/1152/1152/576, 6 lex-first permutations, 25
ladder anchors.

**F11.  The scramble control's stated reason is correct but asserted, not
measured.**  §7.2 explains b₀ and b₁ not moving by "a scramble that preserves
per-checkpoint connectivity and simple-connectivity cannot move them."  The gate
never computes that.  I did: every checkpoint sub-complex of the scrambled atlas
has **b₀ᵗ = 1 and b₁ᵗ = 0** (E/F per checkpoint 944/23972, 944/24174,
620/6718, 620/6703, 944/24078), so the gluing formula pins
`1 + 144 + 0 − 5 = 140` exactly.  **The stated reason is right.**  It is also
not vacuous: a density sweep shows b₁ *does* move once the retained fraction
drops — 3/4 → 140, 1/2 → 140, 1/3 → 140, **1/4 → 157**, 1/6 → 250, 1/10 → 335 —
so ⌊3m/4⌋ sits inside the regime where the mechanism holds, and the disclosure
in §7.2 and deviation 8 is honest.  *Repair: put the scrambled per-checkpoint
census in the gate's evidence, so the explanation is measured rather than
narrated (RUNBOOK #38→#40).*

**F12.  "A comparator built independently of the estimator it audits" (§4.1)
oversells.**  The gate's comparator (lines 1720–1733) rebuilds `und` from the
pair table separately — genuinely independent of `local_profiles`' construction —
but then calls the **same** `components_unionfind` primitive.  The claim is
defensible, because that primitive is itself four-route gated by
`TOP-COMPONENTS`; the wording implies more independence than exists.  I confirm
the comparator does bite on the estimator's own arithmetic (`dim-lax` dies on
`TOP-DIM-READING`).

---

## 10. K1 and K4 at the depth the brief assigns

**K1 — one independent recomputation of the reference invariant row.**  Done
from scratch, different representation and different algorithm.  Every quantity
matches:

| quantity | delivered | R3 independent |
|---|---|---|
| charts / seeds / Q | 36 / 6 / `(0,3,2,1,4,5,6,7)` | same |
| edges per cell (ten) | 1260×8, 396×2 | same |
| 1-cells / 2-cells | 5,436 / 204,384 | same |
| ordered triangle census | 1,226,304 | same |
| ordered defect multiset | ABC 508,320; ACB/BAC/CBA 151,200; BCA/CAB 132,192 | same |
| coherent 2-cells | 84,720 (= 508,320 / 6) | same |
| b₀ / cycle rank / rank ∂₂ | 1 / 5,401 / 5,261 | same |
| **b₁ / b₂ / χ** | **140 / 199,123 / 198,984** | same |
| coherent b₁ / b₂ / χ | 161 / 79,480 / 79,320 | same |
| per-checkpoint (5 rows) | §3.3's table | same, and Σb₂ᵗ = b₂ |

The 11 and 35 of the dimprofile also reproduce: the two cells where the
local simplex dimension is 11 are `(2, FULL)` and `(3, FULL)`, each with 396 =
3 × 12 × 11 ordered pairs — three complete blocks of twelve, exactly as §4.2
says.

**K4 — the 252 distribution spot-checked.**  Recomputed exhaustively, not
sampled.  |GL(3,2)| = **168** by brute force over all 8! permutations, order
spectrum `{1:1, 2:21, 3:56, 4:42, 7:48}`, element orders `{1,2,3,4,7}`.
Completion family 5,040; ord distribution at P\* `{1:48, 2:384, 3:1728, 4:1152,
5:1152, 6:576}`; locus 384 of which **48** reach GL(3,2); **K = GL(3,2) at 252
completions**, distributed `{1:4, 2:48, 3:72, 4:128}` with **zero at 5 and 6**;
`K ⊆ GL(3,2)` at 336.

The "never at 5 or 6" is a **theorem, not a coincidence**, and §5.3 derives it
correctly: `d_{P*}(q) ∈ K(q)`, and GL(3,2) has no element of order 5 or 6
(verified: the missing orders are exactly {5, 6}), so `ord[P*,u] ∈ {5,6}` makes
`K ⊆ GL(3,2)` impossible — and 1,152 + 576 = **1,728** completions are excluded
by it, matching §5.3.  I also confirmed §5.3's mechanism claim: the lex-first
ord-2 target is `Q = (0,1,2,3,5,4,7,6)`, which **is** F₂-linear and **is** the
transvection `(s_A,s_B,s_C) ↦ (s_A,s_B,s_C ⊕ s_A)`, with `|K| = 168 = GL(3,2)`.

---

## 11. Verified with no defect found (recorded so the panel need not repeat it)

- **Determinism.**  Two independent full delivery runs in clean directories both
  produce `top_topology_output.txt` = `bd213b18d1b1…` and
  `top_topology_receipt.json` = `0fb290cf4bfd…` — **byte-identical to the frozen
  artifacts**.  §10's determinism claim reproduces.
- **Exit-1 discipline.**  The clean run exits 0.  Every anchor is genuinely
  exit-1 independently of any gate: `build_receipt` adds failing anchors to
  `must_pass_failures`, and I confirmed it by corrupting two anchors that **no**
  gate predicate references (`A-CHARTS-an asymmetric setting`,
  `A-TRICK-a partially symmetric setting-3`) — the run exited **1** with
  `failed_gates: []`.
- **Corrupt-and-fire on the TB3 pin.**  Appending one byte to the pinned receipt
  → `A-PIN-TB3` fails, `TOP-PIN-TB3` + `TOP-BASE` + `TOP-VERDICT` die.
  Separately, changing three anchored values in the receipt **and re-pinning the
  SHA in the source** so the hash gate passes → `A-EDGES-…-2/FULL`, `A-ORD-2`,
  `A-K-A1 target ord = 2` all fail and `TOP-SELECTOR-ANCHORS` dies.  The anchors
  are load-bearing independently of the pin.
- **Anchor tracing.**  168 of 172 external-labelled anchors resolve to real
  paths in the TB3 receipt with the declared side matching **exactly**; the
  other four are F4.  Zero anchors have `declared != computed`.
- **Falsification census.**  `never_falsified` is **EMPTY** at an honest
  denominator of **28** (30 gates − 1 disclosure − `TOP-FALSIFICATION`, which is
  excluded, named, and legitimately so — it does not run inside a mutant).  All
  29 mutants exit 1, **none crashed before reporting**, and every one names at
  least one gate or anchor.  The AST sweeps are real: no float literal, no
  negated `MUTANT` comparison anywhere in the source (I re-ran both sweeps).
- **Mutants reconstructed from prose** (injected at different sites, not via the
  flag): `cell-drop` → **H8**, exit 1 on `TOP-CELL-COMPLETENESS` + `TOP-CHI` +
  `TOP-ORBITS`; `route1-drop` → **H18** (one *rule*, not a checkpoint, dropped
  from route 1 only), exit 1 on `TOP-CENSUS-ROUTES` + `TOP-CELL-COMPLETENESS`
  **and** on the external `A-TRI`/`A-TRICK` anchors; `link-lax` → **H9**, which
  is F2.  Two of three behave as advertised.
- **Cell-completeness.**  The delivered dropped-cell probe is real: the ordered
  census is measured to be exactly 6 × the geometric count at every instance,
  and removing one geometric cell breaks it.  Independently, the census is
  externally anchored 80 ways (50 `A-EDGES`, 5 `A-TRI`, 25 `A-TRICK`), which is
  the strongest completeness guarantee in the unit.
- **Two-route claims other than F7/F8.**  `TOP-CENSUS-ROUTES` (adjacency walk vs
  multiplicity-product triple loop) is a genuine pair — neither consumes the
  other's output — and I reproduced the census by the multiplicity route.
  `TOP-HOMOLOGY`'s rank-∂₂ pair (high-pivot edge-indexed vs low-pivot
  cotree-projected, rows reversed) reproduces at 5,261, and my third algorithm
  (dense RREF) agrees.  The b₁ decomposition route is legitimate: with Σb₁ᵗ = 0
  it reduces to union-find counts and `(T−1)|V|` alone.  Deviation 3's refusal
  to count χ-from-Betti as a route is correct.
- **Manifold standards (K5e).**  All three verified independently.  ∂-tetrahedron
  `(4,6,4)`, χ = 2, `b = (1,0,1)`, every link a circle; 9-vertex torus
  `(9,27,18)`, χ = 0, `b = (1,2,1)`, every link a circle; pinch `(7,12,8)`,
  χ = 3, `b = (1,0,2)`, links not all circles with **witness vertex 0**, whose
  link is two disjoint triangles.  I additionally confirmed the first two are
  genuine closed surfaces (every edge in exactly two 2-cells; every link a single
  6-cycle for the torus, 3-cycle for the sphere) — the "declared-standard"
  labelling in deviation 10 is honest and the calibration is real.
- **Wing action self-test (§6.1).**  Homomorphism on all 36 ordered pairs, free
  on the 36 charts, drawn table carried to itself with each drawn map
  conjugated, 2-cells permuted — all four reproduce.  The action is measured
  under its own symmetry, satisfying RUNBOOK §14.
- **Positive controls (§7.1).**  Two-wing rows `(8, 11, 5, 4, b₁=4)` and
  `(8, 13, 7, 6, b₁=6)`, the two-wing atlas `(4, 44, 104, 56, b=(1,9,72),
  χ=64)`, and all four three-wing transport graphs (150/126/121, 99/75/70,
  111/87/82, 75/51/46) match the receipt and their external anchors.

---

## 12. Grade

**ACCEPT-WITH-FIXES.**

Nothing I found overturns a claim about the atlas.  Every headline number in
§3, §4, §6 and §7 reproduces on an instrument that shares no code with the
delivered one; the delivery is byte-reproducible; the anchors fire under
corruption; `never_falsified` is genuinely EMPTY at a denominator the unit
computes and names honestly; and **K5(b) is met** — the OR-vs-XOR bug's
24-versus-25 delta reproduces exactly and a delivered must-pass gate now kills
it.  REJECT would be wrong.

ACCEPT would also be wrong.  Three MAJOR items stand.  **F3** is a delivered
table carrying a number the instrument did not measure, marked as a pass;
it is a five-character correction, but it is a false number in a frozen paper
and it should be recorded as one.  **F1** and **F2** are the instrument
describing a guarantee it does not provide — and F1 is a **recurrence of the
identical finding this lens made against TB3**, the immutable base of this very
unit, whose recommended repair was not carried forward.  Between them, three
verdict qualifiers and two of the three components of the declared dimension
estimator — including the 16,998 that carries §4's deepest sentence — sit on
code paths that no gate and no mutant can falsify, in a unit whose §10 reports
`must-pass gates never falsified by any mutant: EMPTY`.  That table is true
about gates and misleading about coverage.

The four moderate items are all repairable without re-running the science:
**F4** (three typed anchors wearing an external label, and a provenance gate
that checks vocabulary rather than provenance), **F5** (a waiver declared as a
computation, moving both §10 denominators by one), **F6** (an analytically-forced
χ clause presented as a route, and the maximal-face size never gated), **F7**
(Burnside's floor division absorbing a fixed-cell census error of 1–5).  F8–F12
are small.

Priority for the repair pass: **F3** (one cell and one clause of prose), then
**F1** and **F2** (real gate work — rebuild the verdict strings inside their
gates; give `star` and `link` a comparator and their own mutants), then F5, F4,
F6, F7 (bookkeeping plus four small gate clauses), then F8–F12.  With those, and
with the OR/XOR mutant declared, this instrument would be the strongest in the
v13 ladder.
