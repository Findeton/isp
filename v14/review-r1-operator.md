# R1 HOSTILE REVIEW — REVIEWER R1, OPERATOR LENS

**Object:** the frozen R1 delivery — paper `2c75772098eb`, code `7c04500ec178`,
output `624ab5236ea1`, receipt `2130abe58b9e`.  **Protocol:**
`v14/note-r1-hostile-protocol.md` (`0647aeba4d9e`), kill-shots K1–K5 binding.
**Pin:** `v14/note-r1-continuum-pin.md` (`27c9f1144ffa`).  **Base:** the R0
founding pin + the v14 LOG #4 erratum.

**Lens:** from-scratch reconstruction on an independent instrument.
Permutations as dicts (unit: tuples); F₂ rank by elimination on frozensets
with a MIN-element pivot (unit: bitmask ints, high/low-bit pivots);
components by BFS over an adjacency dict (unit: union-find + F₂ rank);
rationals as reduced `(num, den)` integer pairs (unit: `fractions.Fraction`);
cyclic groups by iterated dict composition with an explicit closure set;
orbits by BFS closure.  **Nothing was imported from the unit's code.**  Every
number below was rebuilt from the pinned declarations and the pinned v13
receipts alone.

**Grade: ACCEPT-WITH-FIXES.**
**Recomputations: 1,620.**
**Repo writes by this reviewer: this file only.**

---

## 0. Hash verification

Verified **before** reading and **again after** the run; all unchanged:

| artifact | sha256-12 | state |
|---|---|---|
| `v14/paper-01-continuum-rung.md` | `2c75772098eb` | unchanged |
| `v14/code/r1_continuum_exact.py` | `7c04500ec178` | unchanged |
| `v14/code/r1_continuum_output.txt` | `624ab5236ea1` | unchanged |
| `v14/code/r1_continuum_receipt.json` | `2130abe58b9e` | unchanged |

Pinned v13 sources also verified at both ends: RSQ `85f3cf809544`, LCB
`3e502f685ab3`, TB3 `c9bc956fe751`, TOP `65bb1fc5231f`.  Protocol
`0647aeba4d9e` and pin `27c9f1144ffa` verified.

## 0.1 What reproduced

**Every number I checked reproduced exactly.  Zero false numerical results.**

Rebuilt independently and matched: the generator rule extracted from the RSQ
declaration string (base 2, exponent 3 ⟹ width 7, |L_m| = 7m+1); all **28**
scale-threshold cells at all seven primes (member, labels, elementary-abelian
threshold, divisibility threshold); the I6 width cross-anchor (8−1 = 7) and
the wing count; A₁'s nine from 40 320 = 8!; A₂'s sixteen from rank 3, record
space 125 = 5³, p = 5, rank·p+1; A₃'s forty-three at m*(7) = 6; A₄, A₅.
Every member's coordinates (labels, block count, block sizes, ord Σ, Σ cycle
type, basepoint fixedness, Σ-stability).  The whole §4 census (cells, transport
orders, drawn pairs per cell, overlap edges, 1-cells, 2-cells, coherent
2-cells).  The whole §7 trajectory, all 25 cells.  The whole §7 Betti table
(b₀, b₁, b₂ on both complexes).  The L₁₀/L₁₂ probes.  The §4.1 calibration
against I3's published counts (χ 198 984 / 79 320, rank ∂₂ 5 261 / 5 240,
cycle rank 5 401, b₁ 140 / 161, and 4·35 = 140).  The four functoriality
outcomes with their named obstructions.  The §10 negative-control table, the
scramble (shift 6, **240** drawn maps moved, coherent count falling to 0), and
the §10 discrimination table (W₅ 5/6 & 2/5, W₆ 20/17 & 1/2, W₇ 35/24 & 4/7).
The K-window fixture (1/2, 1/3, 2/5, 2/5: not stabilised at K=3, stabilised at
K=1).  The receipt's headline counts (60 anchors, 33 gates, 4 disclosures, 47
mutants, 177 measured data).

**K5 result up front:** rebuilding the verdict from *my own* recomputed table
through the unit's stated derivation reproduces the emitted string
**verbatim**, character for character.

---

## 1. Findings, most severe first

### F1 — MAJOR. The paper's stated mechanism is a false general theorem, and I have the counterexample.

The abstract and §9 carry the unit's entire explanation:

> "the declared growth rule refines by **disjoint addition** — it adds a block
> rather than dividing one.  **Under that operation a ratio of two per-cell
> counts is invariant** and a ratio normalised by label count is not…"

The emphasised clause is **false as stated**.  Disjoint addition alone does not
make a ratio of two per-cell counts invariant.  The load-bearing hypothesis is
disjoint addition **of an isomorphic copy**.

*Measured counterexample.*  I declared, before computing it, the mixed family
MX_m = {0} ⊔ (m copies of the 7-block) ⊔ (one 3-block on which Σ acts as a
3-cycle).  It satisfies every property the paper names as the mechanism: pure
disjoint addition, blocks Σ-stable, no cell crossing a block, ord(Σ) = 3, and
b₀(N) = blocks + 1 at every member.  Measured through my instrument:

| member | n | blocks | b₀(N) | 1-cells | coherent | b₂(N_coh) | N_coh density | b₂ density |
|---|---|---|---|---|---|---|---|---|
| MX₆ | 46 | 7 | 8 | 168 | 230 | 124 | 115/84 | 62/115 |
| MX₇ | 53 | 8 | 9 | 195 | 267 | 144 | 89/65 | 48/89 |
| MX₈ | 60 | 9 | 10 | 222 | 304 | 164 | 152/111 | 41/76 |

Both densities move.  The paper's operation is present in full; the constancy
is not.

This also shows the unit's **discrimination control is aimed at the wrong
contrast**.  The widening family W₅, W₆, W₇ changes the block *size*, so it
separates "same block" from "different block" — it never separates "additive"
from "additive-with-isomorphic-blocks", which is the distinction the mechanism
actually turns on.  §10's conclusion ("their constancy … is a property of that
family's additive rule") is therefore not established by the control that is
run; MX is the control that establishes it, and MX shows the correct predicate
is *isomorphic copying*, not *additivity*.

**Repair (exact).**  (i) §9 and the abstract: replace "Under that operation a
ratio of two per-cell counts is invariant" with "Under addition of an
**isomorphic copy** a ratio of two block-additive counts is invariant".  (ii)
Add MX (or any additive family with a non-isomorphic block) to §10 as a second
discrimination control, gated, with its measured moving densities.  (iii)
§10's sentence "So their constancy on the declared family is a property of
that family's additive rule" must become "…of that family's *copying* rule".

### F2 — MAJOR. The atlas is an un-swept arena coordinate; under a fourth natural declaration the two headline invariants are not defined at all.

The atlas (charts = labels; cells = (block, FULL/REAL); drawn iff a *unique*
transport element) is the unit's own declaration, disclosed in §12 in one
sentence and never swept.  RUNBOOK §15 binds arena coordinates as data whose
*dependence is measured*, and the TOP precedent is explicit — I3's P* is
declared "an ARENA COORDINATE, not a fact about the base … All five
non-identity wing symmetries are swept and the sweep is reported (RUNBOOK
§15)."  The unit demonstrably knows the discipline: it sweeps the *other*
arena coordinate, the family index, at G30 (L₁₀, L₁₂).  It did not sweep the
atlas.

I swept it.  Four alternative declarations, each stated precisely in advance,
all over A₃, A₄, A₅ with the same five invariants:

| alternative atlas | declaration | N_coh density | b₂ density | moves? |
|---|---|---|---|---|
| BASE | REAL := Σ_k∘γ_k, γ = increasing-index cycle | 37/27, 37/27, 37/27 | 20/37 ×3 | — |
| ALT-A | REAL := γ_k∘Σ_k (composition order swapped) | 37/27 ×3 | 20/37 ×3 | no |
| ALT-B | block cyclic order := reversed (γ := γ⁻¹) | 37/27 ×3 | 20/37 ×3 | no |
| ALT-C | block cyclic order := step-2 (γ := γ²) | 37/27 ×3 | 20/37 ×3 | no |
| **ALT-D** | **one cell per block, transport group ⟨γ_k, Σ_k⟩** | **UNDEFINED ×3** | **UNDEFINED ×3** | **yes** |

ALT-A/B/C are a genuinely favourable result and belong in the paper: the two
values survive three re-declarations of the transport convention.  **ALT-D is
the problem.**  It changes nothing about charts, the drawn rule, or the nerve
rule — it only declares one coordinate cell per block carrying the group
generated by both transports, instead of two cyclic cells.  The generated group
has order 21 acting on a 7-label block, so exactly three of its elements carry
any given ordered pair, the uniqueness admission rule refuses every candidate,
and the atlas draws **nothing**: 0 one-cells, 0 coherent 2-cells, both
registered densities undefined at all three tail members.

So the sensitivity is not nil, and it is not merely a value shift: an equally
natural declaration of the same atlas schema makes the unit's two headline
invariants *ill-defined*.  §12's one-sentence disclosure does not discharge
§15 against that.

**Repair (exact).**  Add a gated atlas sweep over at least the three
transport-convention variants (measured invariant — this strengthens the
paper) and at least one cell-structure variant (measured to make the
invariants undefined), and carry the outcome as a computed verdict qualifier,
e.g. `|ATLAS=CONVENTION-INVARIANT-3-OF-3;CELL-STRUCTURE-DEPENDENT`.

### F3 — MODERATE. The emitted stabilised values do not follow the pin's own wording; both alternatives also stabilise, at different values.

The pin registers invariant 2 as "**coherence classes per drawn chart pair**"
and the paper restates it as "coherent 2-cells per **drawn chart pair**,
|F(N_coh)|/|E(N)|".  The formula and the words disagree.  |E(N)| is defined in
§4 as "one per unordered drawn pair **per coordinate cell**" — it counts
(pair, cell) incidences.  The drawn chart *pairs* are the overlap edges |E(G)|.
Measured:

| member | drawn chart pairs \|E(G)\| | 1-cells \|E(N)\| | coherent | emitted (per 1-cell) | pin's words (per pair) |
|---|---|---|---|---|---|
| A₁ | 28 | 40 | 96 | 12/5 | 24/7 |
| A₂ | 30 | 30 | 30 | 1 | 1 |
| A₃ | 126 | 162 | 222 | **37/27** | **37/21** |
| A₄ | 147 | 189 | 259 | **37/27** | **37/21** |
| A₅ | 168 | 216 | 296 | **37/27** | **37/21** |

The same applies to invariant 5.  The pin says "b₂ **per 2-cell**" without
naming the complex; taking N's 2-cells instead of N_coh's gives 20/73,
20/73, 20/73.

Both alternative readings **also stabilise**, so the verdict *head* is safe
under either — but two of the five values printed inside the verdict string are
denominator-convention-dependent, and the convention used is not the one the
pin's words specify.  Separately, "coherence **classes**" is silently read as
"coherent **2-cells**"; those are not the same notion and the substitution is
not disclosed.

**Repair.**  In §5, state that "per drawn chart pair" means "per drawn
(pair, coordinate cell) incidence", record the |E(G)| variant 37/21 and the
|F(N)| variant 20/73 in the receipt beside the emitted values, and note that
the head is stable under all four readings.

### F4 — MODERATE. The eigenvalue-1 anchor chain is a tautology, and it is not I2's wall.

The predicate is `spectral_anchor_chain(mu1) = (mu1 >= 1)` with `mu1` = the
readout permutation's cycle count.  Every permutation of a non-empty set has at
least one cycle, so the clause cannot fail on any input the instrument can
produce.  Measured: 400 random permutation readouts, **0 failures** — the data
clause has no discriminating power at all.  Its own mutant confirms this:
`spec-anchor` dies at G17 on the *calibration* half (`chain(0) is False`), never
on the per-member census, so the "confirmed at every readout of every member"
claim carries no death certificate.  Under #208 an analytically-forced clause
is a disclosure, not a must-pass gate; this one sits inside must-pass G17.

Worse, it is not I2's operator.  I2's E is HA's record↔metric **readout over
F_p** (d = 2…5, size 3, both directions × both orderings — the 112 rows, RSQ
gate G47).  R1's E is the arena's **chart-symmetry permutation matrix over Q**.
The unit confirms a trivial property of a different operator.  I2's actual
content — that a bridge at a wing symmetry of order n forces spec(I−E) into the
n-th roots of unity and 0 is on no unit circle, dimension-independently — is
not touched.

**Repair.**  Demote the per-member eigenvalue-1 census to a disclosure and say
in §5 that it is a property of permutation readouts, not a re-confirmation of
I2.  If a riding anchor with teeth is wanted, the non-vacuous statement is
available: spec(I−E) meets the unit circle only at the ord(Σ)-th roots of
unity, which is checkable and can fail.

### F5 — MODERATE. The declared failure mode `UNDEFINED-AT-A-MEMBER` is unreachable on the delivery path: the partial case is handled by exclusion, not by measurement.

K3 asks whether the verdict's derivation handles b₂ density's partiality by
measurement or by accident.  **By exclusion, and the branch is dead code.**

I constructed the input that hits it — the unit's own scramble at A₃, shift 6,
reproduced independently: **240** drawn maps moved, coherent 2-cell count falls
to **0**, N_coh density → 0, b₂ density → undefined.  That reproduces the
receipt exactly.  But that path never reaches the verdict.  Pushing an
undefined cell through the derivation as reimplemented from the unit's source:

* G20 (cell-completeness, must-pass) demands `all(v is not None)` over the
  **whole** table.  Measured: `False` for a None in the window and `False` for
  a None outside it.  Any undefined cell exits 1 at G20 **before** the verdict
  is derived.
* G19 separately gates |F(N_coh)| > 0 at every member.
* `scalar_mode`/`profile_mode` inspect only `values[-K:]`.  Measured: a None
  **outside** the window returns `CONSTANT`, not `UNDEFINED-AT-A-MEMBER`.  The
  declared label therefore means "undefined *in the window*", not "at a
  member".

So the invariant is total on the delivered domain by gating — which is
legitimate — but the `UNDEFINED-AT-A-MEMBER` mode declared in
`declarations.failure_modes` for both scalar and profile kinds can never be
emitted, and the verdict derivation's handling of partiality is never
exercised.  My ALT-D atlas (F2) is a real, natural input that hits it.

**Repair.**  Either delete `UNDEFINED-AT-A-MEMBER` from the declared failure
modes (it cannot fire) or exhibit it on a real trajectory — ALT-D supplies one
— and relax G20 to distinguish "cell absent" (a dropped row: fatal) from "cell
measured undefined" (a datum: carried into the qualifier).

### F6 — MODERATE. The heterogeneous head produces three of the five verdict qualifiers, and two of them are artifacts of the gluing.

K2, measured segment by segment.  Restricting to the homogeneous tail
A₃, A₄, A₅ and re-deriving through the unit's own rule:

```
delivered : …|WINDOW=K=3-OF-5-MEMBERS-NO-CAP|FUNCTORIALITY=FAMILY-NON-FUNCTORIAL-AT-2-OF-4-STEPS|R2-GATEWAY=A1>
tail only : …|WINDOW=K=3-OF-3-MEMBERS-NO-CAP|FUNCTORIALITY=FAMILY-FUNCTORIAL|R2-GATEWAY=A3>
L6..L10   : …|WINDOW=K=3-OF-5-MEMBERS-NO-CAP|FUNCTORIALITY=FAMILY-FUNCTORIAL|R2-GATEWAY=L6>
```

The stabilised values and all three divergence modes are **identical** in all
three.  A₁ and A₂ contribute exactly nothing to the stabilisation claim — K=3
covers precisely the homogeneous members — and produce the entire
non-functoriality headline and the handed-forward R2 arena.  On the rule's own
five-member family the verdict is `FAMILY-FUNCTORIAL`.

Two consequences.  First, `FAMILY-NON-FUNCTORIAL-AT-2-OF-4-STEPS` is a
statement about the *gluing choice*, not about the growth rule; the paper's §6
reading ("a real structural statement about the corpus's own measured line") is
defensible but the verdict does not say that the rule's own family is
functorial.  Second, **R2 is handed A₁ — an arena the growth rule does not
generate, and to which no admissible morphism runs from or to any family
member.**  That should be flagged where it is handed over.

The pin ordered this family (§2), so the unit complied; the finding is that the
verdict does not name the split.

**Repair.**  Add the tail-restricted trajectory as a gated table; name the
tail's homogeneity in the window qualifier
(`…-NO-CAP-ON-A-HOMOGENEOUS-TAIL-OF-3`); and state in §11 that A₁ is not a
member of the growth family.

### F7 — MODERATE. A sixth intensive quantity stabilises, excluded on a rationale the unit's own measurement contradicts.

The pin excludes b₁ because it is "trivial by I3's ordered measurement and
carries no identification content".  The unit measures b₁(N) = 0 at every
member — consistent — but b₁(N_coh) = 2, 0, **24, 28, 32**: not trivial, and
non-zero exactly where the identification data is imposed.  I measured its
density:

> b₁(N_coh) / |F(N_coh)| = 24/222 = 28/259 = 32/296 = **4/37**, constant on
> A₃/A₄/A₅ **and** at L₁₀ and L₁₂.

So the exclusion rationale is false at this substrate for the coherent
sub-nerve, and the headline score is a registry artifact: **3 of 6** would have
stabilised, not 2 of 5.  The paper's §8 gloss — "they are exactly the two the
pin identifies as carrying the identification data" — reads as a confirmation
when the third identification-carrying quantity was excluded by declaration.

**Repair.**  X-B1 should record the measured density 4/37 and state that b₁ is
excluded by pin declaration, not because it is trivial here — the unit's own
measurement shows b₁ on N_coh is not trivial and does move with the
identification data.

### F8 — MINOR. Two of the three "divergent" invariants diverge only by the basepoint's 1/n share.

Measured, renormalising by the moved labels (n−1 = 7m) rather than by n:

| m | spectral, per label | spectral, per moved label | dimension, per moved label |
|---|---|---|---|
| 6 | {1:19/43, 3:12/43} | **{1:3/7, 3:2/7}** | **{6:1}** |
| 7 | {1:11/25, 3:7/25} | **{1:3/7, 3:2/7}** | **{6:1}** |
| 8 | {1:25/57, 3:16/57} | **{1:3/7, 3:2/7}** | **{6:1}** |
| 10 | {1:31/71, 3:20/71} | **{1:3/7, 3:2/7}** | **{6:1}** |
| 12 | {1:37/85, 3:24/85} | **{1:3/7, 3:2/7}** | **{6:1}** |

`SPECTRAL_PROFILE:SUPPORT-CONSTANT-WEIGHTS-MOVING` and
`DIMENSION_PROFILE:SUPPORT-CONSTANT-WEIGHTS-MOVING` are therefore reports about
the choice of normaliser, not about the substrate.  Only φ diverges
structurally: measured 6/(7m+1) per chart pair and 6/(7m−1) per moved-chart
pair — non-constant either way, because the drawn pairs grow linearly while
the chart pairs grow quadratically.  The verdict is entitled to say φ → 0; it
is not entitled to present three independent divergences.

### F9 — MINOR. The eigenvalue-1 "two routes" are one route plus an implementation check.

Cycle count and dim ker(I−P) are the same invariant by orbit counting;
measured to agree at 400/400 random readouts.  The paper does disclose the
identity ("which **IS** dim ker(I − E)"), so under #234 this is a labelling
matter rather than a hidden one — but G17's claim "computed twice" overstates
it.  Word it as a numerical implementation check.

### F10 — MINOR. The dimension profile carries no dimension content, and "link dimension" is an undisclosed substitution.

Measured link-vertex counts realised at each member: A₁ {0, 7}, A₂ {0, 4},
A₃/A₄/A₅ {0, 6}.  The profile is two-valued at every member — the basepoint at
0 and every other chart at (block width − 1).  It is the block width plus a
basepoint, restated.  Separately, the pin's "link-**dimension** distribution"
is implemented as the link **vertex count**, which is one component of I3's own
four-entry `link` vector; the reading is defensible but undisclosed.

### F11 — NOTE. The provenance handling is correct.

Verified independently on disk: `v13/paper-rsq-reposed-square.md` measures
`f80317a25037` against R0's recorded `07bea42728a2`, and
`v13/paper-top-topology.md` measures `379194959fbc` against `4e4cd4f11bab`.
All eight carrying receipts and the other six companions verify.  Carried as
disclosure `X-COMPANION-HASH`, errata of record at LOG #4.  Handled correctly
and to the letter; no number of this unit reads from a paper.

### F12 — NOTE. Two favourable results the paper does not claim.

(a) The two stabilised values hold at **every** member of the growth rule, not
only on the window.  Measured at m = 1…12: 1-cells = 27m, overlap edges = 21m,
2-cells = 73m, coherent = 37m, b₂(N_coh) = 20m, b₁(N_coh) = 4m, b₀(N) = m+1,
φ = 6/(7m+1) — exactly, at every m.  N_coh density = 37/27 and b₂ density =
20/37 already at **L₁, the single-block member**.  Nothing converges; there is
no window in which the values settle, because they never differed.
(b) The values survive three transport-convention re-declarations (F2,
ALT-A/B/C).  Both belong in §9.

---

## 2. Kill-shot adjudications

### K1 — THE COPYING QUESTION. **Adjudicated: the constancy is ALGEBRAICALLY FORCED. No non-copied quantity stabilises non-vacuously.**

**The theorem, stated precisely.**

> *Copy-forcing.*  Let A be an arena with labels L = {0} ⊔ ⨆_{k=1}^{m} B_k,
> a declared symmetry Σ fixing 0 with Σ(B_k) = B_k, and declared cyclic orders
> on the B_k, such that for each k there is a bijection β_k : B₁ → B_k with
> β_k∘Σ|_{B₁} = Σ|_{B_k}∘β_k carrying B₁'s declared cyclic order to B_k's.
> Then (i) every transport of the declared atlas has support inside a single
> block, so the coordinate-resolved nerve N and its coherent sub-nerve N_coh
> are the disjoint union of m copies of the block-1 atlas together with the
> isolated chart 0; (ii) hence for any two quantities X, Y additive over
> connected components and vanishing on an isolated vertex,
> X(A_m)/Y(A_m) = X(A₁)/Y(A₁), independent of m; (iii) every counting quantity
> of the atlas has the form (am+b)/(cm+d) with b, d the basepoint's
> contributions, and is constant in m **iff ad = bc**.

**Checked against the unit's claims.**  All three hypotheses hold *by the
declaration*, not by discovery.  Measured: β_k(x) = x + 7(k−1) intertwines Σ
and carries the declared increasing-index cyclic order, at every k, for
m = 1, 2, 6, 7, 8, 10, 12.  Σ-saturation(B_k) = B_k, cross-block 1-cells = 0,
every drawn pair inside its own block, b₀(N) = blocks + 1 — all measured at
m = 6, 7, 8.  The single-block census at L₁ is (27 one-cells, 21 overlap edges,
73 two-cells, 37 coherent, b₂(N_coh) = 20, b₁(N_coh) = 4), and every closed
form predicted by (i)–(ii) holds at **m = 1…12** (measured, 12 × 8 checks).

So: **what is measured** is the single-block census (27, 37, 20) and, strictly,
that the rule's blocks are isomorphic — but that isomorphism is readable off
the declaration string "*m copies of TB3's seven moved labels, with S₃ acting
on the F₂³ factor alone*" without computing anything.  **What is forced given
that** is the entire tail trajectory: both constant densities, φ's strict
decrease (6/(7m+1)), and both profiles' weight drift.  Not one cell of the
A₃–A₅ trajectory is independent information beyond the L₁ census.

Note the unit's mechanism gate G24 is *not* a #208 violation — its predicate is
false on my MX family, so it is not "true by algebra for every input".  The
problem is not the gate; it is that the paper reports as a *measured mechanism*
what the declaration already fixes, and states it via a theorem that is false
(F1).

**The sharpest form — does ANY non-copied quantity stabilise?**  I declared a
grid of 24 natural intensive quantities in advance, classified each as *copied*
(both numerator and denominator block-additive, no basepoint term),
*basepoint-involving*, or *cross-block*, and measured all of them at
m = 6, 7, 8, 10, 12.  Result:

| class | count | constant on the tail |
|---|---|---|
| copied | 10 | **10** |
| basepoint-involving | 8 | **0** |
| cross-block | 6 | 3 — and all three vacuous |

The three cross-block "constants" are b₀(N_coh)/b₀(N) = 1 (the two complexes
share a 1-skeleton), cross-block 1-cells / |E(N)| = 0 (the numerator is
identically zero), and the number of component isomorphism types = 2 — which
*is* the copying statement itself, not an independent invariant.  Every
non-vacuous non-copied quantity moves: φ, 1-cells per chart, coherent cells per
chart, b₂ per chart, charts per component, overlap edges per chart, the
non-isolated fraction, the component-concentration index, and the largest
component's share.

I then ran the ad = bc test exhaustively over the 14 available affine counts
(182 ordered pairs): **90 constant ratios, of which the number that involve a
basepoint term is 0**.  This is not a search artifact — it is the theorem's
clause (iii) instantiated: the only pairs whose basepoint contributions are
proportional are those where both are zero, i.e. the copied ones.

**Verdict wording.**  The honest content is *"the declared rule is a copying
rule; two block-additive ratios are therefore constant, and their values are
the single block's."*  I propose the head carry that:

```
R1-STABILIZES-BY-DISJOINT-ISOMORPHIC-COPY-AT-<NCOH_DENSITY=37/27;B2_DENSITY=20/37|…>
```

or, minimally, that a computed qualifier segment
`|MECHANISM=DISJOINT-ISOMORPHIC-COPY;VALUES-ATTAINED-AT-M=1` be appended — the
second clause being measured (F12a) and being the plainest statement that no
limit is being taken.

### K2 — THE FAMILY'S LEGITIMACY. **Adjudicated: the verdict survives restriction to the tail unchanged in substance; the 5-member family adds only qualifiers, two of which are artifacts.**

Recomputed at every member independently (§0.1) and re-derived at three
family scopes (F6).  Gluing three constructions is faithful to the pin's §2 —
the pin names A₁, A₂, A₃ by construction and A₄, A₅ by rule — so this is
compliance, not overreach.  But: the stabilisation window K=3 covers exactly
the homogeneous members, the stabilised values and divergence modes are
identical on the tail alone, and the rule's own five-member family L₆…L₁₀ is
**FAMILY-FUNCTORIAL** with gateway L₆.  The claim is therefore "one rule, whose
every member gives the same two ratios" — measured at m = 1…12, stronger than
"3 members + 2 probes" and weaker than a stabilisation.  **The qualifier does
need the tail's homogeneity named**, and R2 needs to be told that A₁ is outside
the rule's family.

### K3 — THE INVARIANT DEFINITIONS. **Adjudicated: well-defined on the delivered domain, but three of the five deviate from the pin's wording and the partial case is handled by exclusion.**

* N_coh density is **not** the pin's "per drawn chart pair" — it is per (pair,
  cell) incidence; the pin's literal reading gives 37/21 (F3).  "Coherence
  classes" → "coherent 2-cells" is an undisclosed substitution.
* b₂ density's complex is unnamed in the pin; the alternative literal reading
  gives 20/73 (F3).  b₂ is read on N_coh, gated at G19, justified from I3 —
  that part is sound.
* The eigenvalue-1 chain is a tautology and confirms a different operator than
  I2's wall (F4).  It is a **weaker surrogate**, and the answer to the
  protocol's question is: not I2's wall.
* The DIMENSION_PROFILE exclusion of the raw estimator **was honoured**
  everywhere: I traced the raw counts and they appear only inside the negative
  control, never in a registered invariant, never in the verdict.  Confirmed.
  But the profile is two-valued at every member and carries no dimension
  content (F10).
* **The UNDEFINED path: I constructed the input that hits it** (the scramble,
  reproduced exactly — 240 maps moved, 0 coherent cells) and measured that G20
  kills the run before the verdict derivation sees it, and that a None outside
  the window is invisible to the mode functions.  **Handled by exclusion, not
  by measurement; the declared failure mode is dead code** (F5).

### K4 — ATLAS-RELATIVITY. **Adjudicated: §12's disclosure does NOT suffice; the P*-precedent demands the sweep in-unit.**

Four alternative declared atlases measured (F2).  37/27 and 20/37 **do not
move** under three transport-convention re-declarations — a real and
publishable robustness result the unit did not claim.  They **do become
undefined** under a fourth, equally natural cell-structure declaration, and
they **do move** (to 37/21 and 20/73) under the pin's own literal denominator
wording (F3).  Since the measured sensitivity is non-nil and reaches
well-definedness, the qualifier must carry the atlas declaration, and the sweep
belongs in the unit — exactly as I3 swept P*.

### K5 — INSTRUMENT (at the operator lens's depth). **Adjudicated: PASS.**

The verdict string regenerates **verbatim** from my independently recomputed
table through the unit's stated derivation — head from the non-emptiness of the
constant set, values from the measured tail, each divergence mode from
`scalar_mode`/`profile_mode`, the window from K and the built length against
the target, the functoriality count from the four step outcomes, the gateway
from the first φ < 1.  I also re-derived the string at two other family scopes
and it tracked the measurement each time (F6), so the derivation is genuinely
data-driven and each qualifier is flippable.  The 28 scale-threshold anchors
and the I6 width cross-anchor trace to the pinned bytes (§0.1).  Every paper
number I checked matches its receipt path; **no false numbers found, by value
or otherwise.**

---

## 3. Recomputation count

| pass | content | count |
|---|---|---|
| 1 | family rebuild from pinned declarations; 28 thresholds; member coordinates; full atlas census; trajectory; Betti; L₁₀/L₁₂ probes; functoriality | 170 |
| K1 | block-isomorphism checks; cross-block census; L₁ census; closed forms at m = 1…12; the 24-quantity grid at 5 members; the 182-pair ad=bc scan | 432 |
| K2–K5 | three verdict regenerations; NCOH/b₂ denominator variants; 400-readout tautology sweep + 400 kernel-dimension agreements; dimension profiles; scramble reconstruction; UNDEFINED-path probes; four alternative atlases at three members | 923 |
| final | I3 calibration; discrimination family; negative control; A₂ X-REAL-EMPTY; the MX counterexample family; receipt-vs-paper counts | 70 |
| extra | moved-label renormalisation at 5 members; φ variants; companion hashes | 25 |
| **total** | | **1,620** |

Of these, 800 are the random-readout sweep establishing F4's tautology; the
remaining **820** are substantive recomputations of delivered quantities and
declared alternatives.  Diffs against the delivery: **zero** (three apparent
diffs in pass 1 were my formatter rendering `1` as `1/1` and profiles as lists
rather than strings; the values were identical).

---

## 4. Grade

**ACCEPT-WITH-FIXES.**

Not REJECT: not one computed number is wrong, the verdict head is correct under
every convention I tested, the derivation regenerates verbatim from an
independent table, the inheritance traces to the pinned bytes, the provenance
erratum is handled correctly, and the two headline values are robust to the
family index and to three atlas conventions.

Not ACCEPT: two MAJORs stand.  The paper's stated mechanism is a false general
theorem with a measured counterexample (F1), and the atlas is an un-swept arena
coordinate against an engraved rule and a live precedent, with a measured
sensitivity that reaches well-definedness (F2).  Both repairs are local and
definite; neither disturbs a number.

The adjudicator should note that F1 and K1 together change what the unit is
*for*.  The measured content of R1 is: **this substrate's declared growth rule
copies a block, so two block-additive ratios take the single block's values at
every member, and the overlap fraction falls to zero like 6/(7m+1).**  That is
a legitimate, publishable, two-sided result — it is the pin's
NO-CONTINUUM-LIMIT side in substance, reported under the STABILIZES head
because the pin's operational definition of stabilisation does not distinguish
"settles" from "was never anything else".  The verdict wording proposed in K1
is the minimum that says so.
