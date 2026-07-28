# BC2 — THE BELL-TWO-FRAMES PROBE: the conditioning structure
# needs a foliation

**Status:** RESULT, STRICT, **GREEN-UNREVIEWED** (not citable), 2026-07-28.
**Program:** BC — the Barandes consistency program (`bc/LOG.md` #1), from
scratch, no record substrate.  **Pin:** `bc/note-bc2-bell-two-frames-pin.md`
(frozen before the receipt existed).  **Receipt:**
`bc/code/bc2_two_frames_exact.py` → `bc/code/bc2_output.txt`
(35 gates, 0 failures, 0 anchor failures, 0 control failures, exit 0,
runtime 9.4 s).

**Verdict: R-FOLIATED.**

**Scope.**  This note is about **[B3]'s formal apparatus** — a global
external time parameter with division events located at times — on **one
declared Bell model at toy scale**.  It is **not** a claim about
relativity in nature.  It makes **no Bell-inequality claim and no
locality claim**; the corpus's committed Bell verdict is not cited, used
or touched.  No records, no generated carrier, no gravity.

---

## 1. The statement

Let the model be [B3]'s own kinematics applied to one Bell experiment:
one fixed finite configuration space, an initial division event, a
preparation, and two commuting projective measurements at spacelike
separation.  Write the same experiment as a [B3] indivisible stochastic
process in both frame orderings `F1 = (prep, A, B)` and
`F2 = (prep, B, A)`.

**BC2.**  *The two frames' specified content is not frame-isomorphic.  At
every declared setting pair with two different settings, no permutation
of the configuration space carries `F1`'s specified content onto `F2`'s,
at any of four declared grains, under either of two declared time
correspondences.  At the two equal-setting pairs the only maps that exist
break the identity of the two record sectors.  The outcome statistics are
identical in the two frames, exactly.*

The exclusion is complete over the admissible class, not a failed search:
L-1(a) forces the frame map to be a permutation, and the permutation
search is exhaustive (§6).

---

## 2. The model, exactly

**Configuration space (fixed; [B3] p.29, kinematical axiom, verbatim:
*"The configuration space is a FIXED feature of the model, meaning that
it does not vary between real-world runs or instantiations of the
model."*).**

```
C = { (qA, qB, pA, pB) },  qA, qB in {0,1},  pA, pB in {r, +, -},  |C| = 36
```

`qA, qB` are the two wings' spin configurations in a declared reference
basis; `pA, pB` are the two pointers'.  The pointer configurations are
[B3]'s **measurement-outcome configurations** (p.16: *"the measuring
device will end up in one of its possible MEASUREMENT-OUTCOME
CONFIGURATIONS with a stochastic probability that coincides with the
standard Born rule"*).  The initial configuration is `j0 = (0,0,r,r)`.

**Operators.**  `U_prep` acts on `(qA,qB)` and carries `j0` to the
singlet; `U_A(a)` and `U_B(b)` are von Neumann measurement operators,
`U_X = Σ_s Π^θ_s ⊗ Sh^{n(s)}`, with `Sh` the 3-cycle `r → + → − → r` on
that wing's pointer.  All three are **real orthogonal**, verified entry
by entry (`1296` inner products each, zero residuals), and
`[U_A(a), U_B(b)] = 0` exactly at all `3 × 3` operator pairs.

**Field.**  Everything is computed in `K = Q[x]/(8x⁴ − 8x² + 1) =
Q(cos(π/8))`, a real quartic field whose irreducibility over `Q` is
certified in-receipt (no rational root; no rational quadratic factor), so
the four-coefficient zero test is sound.  `√2 = 4c² − 2`.  Every
transition-matrix entry lands in `Q(√2)`.  No float and no tolerance
appears anywhere.

**Setting pairs (six, declared).**  `SP-A (0°,45°)`, `SP-B (0°,135°)`,
`SP-C (90°,45°)`, `SP-D (90°,135°)`, `SP-E (0°,0°)`, `SP-F (45°,45°)`.
Directions are declared relative to the configuration basis, and the six
span basis-aligned and basis-unaligned directions on both wings.

**The two frames.**  Target times `0, 1, 2, 3`; time-evolution operators
(`[B3]` eq. 25)

```
F1:  Θ(1←0) = U_prep,  Θ(2←0) = U_A U_prep,  Θ(3←0) = U_B U_A U_prep
F2:  Θ(1←0) = U_prep,  Θ(2←0) = U_B U_prep,  Θ(3←0) = U_A U_B U_prep
```

Division events `D = {0, 2, 3}` in each frame: `0` because [B3] p.9
assumes conditioning times *"include an 'initial' time 0"*, and `2, 3`
because [B3] p.29 states *"division events are generated during a
measurement process"*.  `t = 1` is a target time and not a division
event.  The second-leg matrix is `Γ(3←2) = |Θ(3←2)|²` with `Θ(3←2)` the
second measurement's operator: `U_B` in `F1`, `U_A` in `F2`.

**Every leg is unistochastic, by exhibited certificate.**  All `48` legs
(6 setting pairs × 2 frames × 4 legs) pass U3's lifted `ds_report`
(exact unit row and column sums, no negative entry) and carry an
exhibited real orthogonal operator with zero `UᵀU − I` residuals and
`U_ij² = Γ_ij` at all `1296` entries.  This is U3's own positive-verdict
discipline, inherited verbatim; the cited criterion is never
load-bearing on a positive.

---

## 3. The specified-content inventory

**What [B3] specifies** ([B3] p.29 axioms; p.11 eqs. 24–26; p.14
eqs. 41–42, 46): (1) the configuration space, fixed; (2) the
division-event set and its order in the model's time parameter; (3) the
transition matrices `Γ(t←t')` for every division event `t'` and every
target time `t`; (4) the standalone distributions `p(t)`; (5) the
division-event two-time joints `P(i,t ; j,t') = Γ_ij(t←t') p_j(t')`.

**What [B3] refuses to specify** ([B3] p.10–11, verbatim): *"there will
generically exist a large or infinite number of ways of choosing a
complete Kolmogorov tower (3) consistent with those ingredients.  Each
such choice … is called a NON-MARKOVIAN REALIZER. … the specific
non-Markovian realizer is potentially unknowable, and perhaps
meaningless."*  So: no Kolmogorov tower, no trajectory joints, no joint
over two non-division times, no realizer.

**The comparison runs over (1)–(5) and nothing else.**  Nothing the
framework refuses is used against it.  The inventory is printed
completely for both frames in the receipt.  Its `SP-A` shape:

| object | `F1` | `F2` |
|---|---|---|
| `p(1)` | support 2 | support 2 |
| `p(2)` | support 2, at `{(01\|+r), (10\|−r)}` | support 8, both pointers at `r` for neither wing |
| `p(3)` | support 8 | support 8 |
| `Γ(2←0)` | 72 nonzero, column supports `{2: 36}` | 288 nonzero, `{8: 36}` |
| `Γ(3←0)` | 288 nonzero, `{8: 36}` | 288 nonzero, `{8: 36}` |
| `Γ(3←2)` | 144 nonzero, `{4: 36}` | 36 nonzero, `{1: 36}` |

Retrodictive matrices (`t < t'`, permitted by [B3] p.10) are **not
computed**: for a division event `t'` with `p(·,t') > 0` they are
Bayes-determined by the forward matrices and the marginals already in the
inventory, so they carry no content the comparison could separate.  This
is a declared cap.

---

## 4. The QM-statistics control

Both frames reproduce the exact singlet outcome law
`P(α,β) = (1 − αβ cos(a−b))/4` and both single-wing marginals `1/2`, at
all 6 setting pairs — 96 exact identities in `K`.  `SP-A/C/D` give
`(1/4 − √2/8, 1/4 + √2/8, 1/4 + √2/8, 1/4 − √2/8)`; `SP-B` the same with
the signs exchanged; `SP-E, SP-F` give `(0, 1/2, 1/2, 0)`.  Wing A's
outcome marginal is identical across the two values of `b` at fixed `a`,
and symmetrically, in both frames.

**The final-time law is literally identical in the two frames:**
`Γ(3←0)` agrees at all `1296` entries and `p(3)` at all `36`, at every
setting pair, with the identity as the frame map.  This control gate is
exit-1; it passes.

Two structural facts about the model, both exact:

- **Divisibility at the intermediate division event.**  `Γ(3←2) Γ(2←0)`
  equals `Γ(3←0)` at `SP-A, SP-B, SP-E` and differs in `576` entries at
  `SP-C, SP-D, SP-F`, **in both frames**.  So divisibility there is *not*
  itself frame-dependent on this model, and the finding of §5–§6 is not
  a divisibility artefact: it is present at setting pairs where the
  process divides in both frames.
- **[B3] eq. (22)'s own hypothesis fails.**  The interpolant
  `~Γ(3←2) = Γ(3←0) Γ⁻¹(2←0)` requires `Γ(2←0)` invertible; its exact
  rank is `18` or `9`, never `36`, in both frames at every setting pair.
  The pseudo-stochastic diagnosis of [B3] p.10 is not reached — the
  inverse does not exist.  (A datum only; the interpolant census is U1's
  and BC1's subject, not this unit's.)

---

## 5. The mismatch census

Under the **Lorentz correspondence** `φ_LOR` each division event is the
same physical event in the two frames: `prep → prep`, `A → A`, `B → B`.
Because `F1`'s times are `(prep, A, B) = (0, 2, 3)` and `F2`'s are
`(prep, B, A) = (0, 2, 3)`, `φ_LOR` sends `F1`'s `t = 2` to `F2`'s
`t = 3` and `F1`'s `t = 3` to `F2`'s `t = 2`.

### 5.1 The division-event sets (census item iii)

The two division-event sets are in bijection under `φ_LOR` and their
**induced orders disagree on `{A, B}`**.  The consequence is exact and
prior to any probability: `F1` specifies a **forward** leg matrix
`Γ(3←2) = Γ(B ← A)`, whose physical counterpart in `F2` is the
**retrodictive** object `Γ(2←3)`, because in `F2` Bob precedes Alice.
The forward inventories are therefore not index-matched: label `('G',2,3)`
is `F1`-only and `('G',3,2)` is `F2`-only.  That object is dropped from
the searches of §6, which compare only what both frames specify in the
same direction — the frame map's best case.

### 5.2 The identity frame map (the L-1(b) branch)

Every corresponding object differs, at every setting pair.  Exact
differing-entry counts:

| object pair | SP-A | SP-B | SP-C | SP-D | SP-E | SP-F |
|---|---|---|---|---|---|---|
| `p(1)` vs `p(1)` | 0 | 0 | 0 | 0 | 0 | 0 |
| `p(2)` vs `p(3)` (at Alice) | 10 | 10 | 24 | 24 | 4 | 16 |
| `p(3)` vs `p(2)` (at Bob) | 16 | 16 | 24 | 24 | 4 | 16 |
| `Γ(2←0)` vs `Γ(3←0)` | 360 | 360 | 864 | 864 | 144 | 720 |
| `Γ(3←0)` vs `Γ(2←0)` | 576 | 576 | 864 | 864 | 144 | 720 |
| `Γ(3←2)` vs `Γ(3←2)` (second legs) | 180 | 180 | 288 | 288 | 72 | 288 |

The one object that agrees is `p(1)`, the marginal after preparation and
before either measurement — where the two frames have not yet parted.

Support sizes of the marginal at Alice's division event, `(F1, F2)`:
`SP-A (2, 8)`, `SP-B (2, 8)`, `SP-C (8, 16)`, `SP-D (8, 16)`,
`SP-E (2, 2)`, `SP-F (8, 8)`.  Column-support censuses of `Γ` at Alice's
division event, `(F1, F2)`: `SP-A/B ({2:36}, {8:36})`,
`SP-C/D ({8:36}, {16:36})`, `SP-E ({2:36}, {2:36})`,
`SP-F ({8:36}, {8:18, 16:18})`.

### 5.3 The basis-free certificate

At the division event that **is** Alice's measurement, `F1` assigns
probability exactly `1` to *"pointer B is still ready"* and `F2` assigns
exactly `0`; at the division event that **is** Bob's, `F1` assigns
exactly `0` to *"pointer A is still ready"* and `F2` exactly `1`.  This
holds at **all six** setting pairs, including the equal ones.  The
pointer configurations are the measurement-outcome configurations any
[B3] model of a measurement must carry, so this certificate does not
depend on the model's choice of configuration basis for the spin wings.

---

## 6. The test, and why the search is complete

**L-1's C4 declaration.**  *What acts:* the frame change `F1 ↔ F2`.
*On what set:* the model's one fixed finite configuration space `C`,
`|C| = 36`.  *Invertibly:* yes — `F1 → F2 → F1` is the identity, so
`R R' = I` with both stochastic.

**L-1 (a)** (`v11/note-L1-lorentz-no-go-lemma.md`:86–94), verbatim:

> Let `C` be finite.  Let `G` be a group and `g ↦ R_g` an exact
> covariance action on `C` by stochastic maps: each `R_g` is
> row-stochastic on `C`, `R_e = I`, and `R_g R_h = R_{gh}`.  Then every
> `R_g` is a permutation matrix of `C`.

**L-1 (b)** (same file, :107–114), verbatim:

> If `G` contains a one-parameter boost subgroup isomorphic to `(ℝ,+)`,
> the restriction of `R` to that subgroup is trivial: `R_b = I` for every
> boost `b`.

So the candidate frame map is a **permutation** of `C`, and the
**identity** if the boost is taken in a one-parameter subgroup.  The
search below is therefore complete over the admissible class, and a
negative is a proof of non-existence.

**[B3] proves L-1's core lemma itself.**  [B3] p.10, footnote 7,
verbatim: *"one sees that `X` can only have a single nonzero entry in
each row.  If `X` is a stochastic matrix, then each of these nonzero
entries must be the number 1, so `X` must be a permutation matrix."*
That is v3 paper 8 Lemma 2.3, proved in [B3] for its own purpose (the
pseudo-stochasticity of the eq. 22 interpolant).  The identity of the two
statements is a fact about the two texts; nothing is derived from it
here.

**The grains (four, declared).**  `G-FULL` (every target time, every
marginal, every column of every `Γ` — the dynamical axiom read
literally); `G-DIV` (division-event times only, the intermediate target
time and its marginal dropped); `G-FIX` (the model's fixed features only,
no marginals, since [B3]'s epistemic axiom makes `p` contingent);
`G-SUPP` (reachable conditioning only: columns `j` with `p_j(t') > 0`).

**The time correspondences (two).**  `φ_LOR` as above.  `φ_ORD`
(`t ↦ t`), which identifies *the first measurement in `F1`* with *the
first measurement in `F2`* — different physical events, so not the
Lorentz correspondence, tested as the weakest steelman.

**The search.**  Colour refinement with a single shared encoding across
both sides, then individualisation-and-backtracking; every positive is
verified entry by entry against every object.  Node cap `200 000`;
maximum actually used `32`.  Machinery controls both pass: a structure
against its own relabelling by a declared transposition is solved and the
returned permutation verified; two structures differing in one matrix are
separated with the separating invariant printed.

### 6.1 The result table

`-` = no permutation of the 36 configurations exists; `PI` = one exists
and is verified.

| setting | grain | `φ_LOR` | `φ_ORD` |
|---|---|---|---|
| SP-A, SP-B, SP-C, SP-D | G-FULL | `-` | `-` |
| SP-A, SP-B, SP-C, SP-D | G-DIV | `-` | `-` |
| SP-A, SP-B, SP-C, SP-D | G-FIX | `-` | `-` |
| SP-A, SP-B, SP-C, SP-D | G-SUPP | `-` | `-` |
| SP-E (0°,0°) | G-FULL, G-DIV, G-FIX | `-` | `PI` |
| SP-E (0°,0°) | G-SUPP | `PI` | `PI` |
| SP-F (45°,45°) | G-FULL, G-DIV, G-FIX | `-` | `-` |
| SP-F (45°,45°) | G-SUPP | `PI` | `PI` |

**Unequal settings: 16 of 16 cells empty under `φ_LOR`, and 16 of 16
under `φ_ORD`.**  No relabelling of any kind — physical or abstract —
relates the two frames' specified content there.

**Equal settings: every map that exists breaks the identity of the two
record sectors.**  On the configurations the model's own content visits,
each returned permutation carries a configuration in which pointer B is
still ready onto one in which it is not, and symmetrically for pointer A
(2 such configurations at `SP-E`, 8 at `SP-F`; witness at `SP-E`
`G-FULL`: `(01|+r) → (10|r+)`).  A boost relates two descriptions of the
same two laboratories and does not exchange them.  The equal-setting
cells are the coincidence that at `a = b` the two wings carry
interchangeable descriptions; they are not covariance.

---

## 7. The escape-hatch battery

| escape | outcome | exactly where / at what cost |
|---|---|---|
| **E1** drop the intermediate-time marginals, keeping only division-event content | **FAILS** | the dropped object is `p(1)`, which is *already* identical in the two frames; the mismatch sits at `t = 2` and `t = 3`, which are division events and survive the drop.  Grain `G-DIV` is empty at every setting pair under `φ_LOR`. |
| **E1'** drop **all** marginals, keeping only the model's fixed features | **FAILS** | the transition matrices alone already separate: the column-support census of `Γ` at Alice's division event differs between the frames (§5.2), and a column-support census is invariant under conjugation by a permutation.  Grain `G-FIX` is empty at every setting pair under `φ_LOR`. |
| **E2** deny that the first measurement generates a division event on the composite | **WORKS** | with `D = {0}` the content is `Γ(3←0)` and `p(3)`, which agree with the **identity** as the frame map at every setting pair.  Cost: (i) contradicts [B3] p.29 (*"division events are generated during a measurement process"*); (ii) removes the only conditioning the model has after preparation, so the framework can no longer describe the post-measurement update; (iii) makes the process trivially divisible over the remaining single interval. |
| **E3** system-centricity ([B3] p.10: *"Division events are not global properties of the whole universe, but are system-centric"*) | **WORKS AT A GRAIN** | **E3a:** each wing's own configuration marginal, evaluated at **that wing's own** division event, is exactly identical in the two frames at every setting pair (6 exact identities per wing per setting pair).  **E3b:** it fails the moment a wing is evaluated at the **other** system's division event — wing A's marginal at the time of Bob's measurement differs between the frames at every setting pair.  **E3c, the cost:** the product of the two wing-local outcome marginals differs from the composite's outcome joint at every declared setting pair, so the correlations are not recoverable from the two frame-invariant wing descriptions.  The description that carries the correlations is the composite one, and that is exactly the description §6 shows is not frame-mappable.  *The subsystem-lattice consistency of the system-centric assignment is BC1's subject (`bc/note-bc1-division-event-composition-pin.md`) and is not treated here.* |
| **E4** a non-group (semigroup) covariance | **OPEN** | L-1's scope guard leaves exactly this: *"inside a GROUP action L-1(a) DERIVES invertibility, so what actually escapes is a covariance carried by a semigroup or by a non-group action."*  This unit's frame change is a group, so the permutation class is complete for the question posed.  No LP/Farkas search over semigroup maps is run (declared cap).  E4 is neither a working nor a failing escape here. |

---

## 8. Placement on L-1's ladder

| rung | status here |
|---|---|
| **1. exact stochastic covariance** | **EXCLUDED**, and exhibited concretely on a [B3] Bell model: the forced map class (permutations by L-1(a), the identity by L-1(b)) is searched completely and is empty at every unequal setting pair, at every grain, under either time correspondence; at equal settings the surviving maps break the record sectors (§6.1). |
| **2. sprinkling-grade statistical covariance on a generated carrier** | **NOT TOUCHED.**  There is no generated carrier in this program. |
| **3. order-level covariance** | **NOT TOUCHED**, and unavailable as a rescue for this model without a separate argument this unit does not supply: part of the mismatch *is* an order fact — the division-event set's induced order is reversed on `{A, B}` by the physical identification (§5.1). |

**What survives, named in paper 8's admissible list** (imported at
`v11/note-L1-lorentz-no-go-lemma.md`:30–40): **admissible form 1**,
*"equality … of declared finite-battery statistics for sampled
Lorentz-related tests"*, holds here **exactly**, not merely
approximately — the declared outcome battery is identical in the two
frames at all six setting pairs, and the whole final-time law `Γ(3←0)`
and `p(3)` agree entry by entry.  Form 2 (projective compatibility of
batteries at different refinements) is not exercised.  Form 3 (imported
continuum covariance) is not used.

---

## 9. The sparsity hypothesis, settled for this model

The pin's pre-registered positive is that [B3]'s refusal to specify a
Kolmogorov tower might make its specified content frame-mappable
*because it says less*.  It does not, and the reason is exact: **the
objects that fail to correspond are not tower objects.**  They are the
single-time standalone distribution at a division event, the
division-event transition matrices, and the induced order of the
division-event set — the sparsest content the framework has.  [B3] is
sparser than its predecessors in the tower direction and exactly as rich
as they are in the slice direction, and the frame change acts on the
slice direction.

The framework's own resources localise the failure rather than remove
it: the **wing-local** content is frame-invariant (E3a) and the
**final-time** content is frame-invariant (§4), while the **intermediate
division event of the composite system** is where the two descriptions
part.

---

## 10. What this note does not claim

- Nothing about relativity in nature; the finding is about [B3]'s formal
  apparatus on one declared model.
- No Bell-inequality claim and no locality claim.  Every statement about
  the outcome statistics is a statement about the constructed model's
  numbers.
- Nothing about Barandes' equivalence theorem, which is proven
  mathematics and is not under test (`bc/LOG.md` #1).
- Nothing about whether [B3] *could* be given a covariant formulation.
  [B3] p.29 defers the relativistic and Bell-theorem treatment to future
  work in its own words (*"These theorems will be addressed in detail in
  future work"*); this unit tests the apparatus as published, not a
  successor.
- Nothing about semigroup or non-group covariance actions (E4, OPEN).
- Nothing about the subsystem-lattice consistency of system-centric
  division events (BC1's subject, cited, not duplicated).

---

## 11. Import ledger

| item | status | home |
|---|---|---|
| Division events, system-centricity, the initial time 0 | **[IMPORTED, verbatim]** | [B3] p.9–10 |
| eqs. (22)–(23) and the pseudo-stochastic interpolant | **[IMPORTED, verbatim]** | [B3] p.10 |
| footnote 7 (a stochastic map with stochastic inverse is a permutation) | **[IMPORTED, verbatim]**; identical in content to v3 paper 8 Lemma 2.3 | [B3] p.10 fn.7 |
| The refusal to fix a Kolmogorov tower / realizer | **[IMPORTED, verbatim]** | [B3] p.10–11 |
| The dictionary `Γ_ij = |Θ_ij|²`, `ρ(0)` diagonal, the Born rule | **[IMPORTED, verbatim]** | [B3] p.11, p.14 |
| The three axioms; measurement generates division events | **[IMPORTED, verbatim]** | [B3] p.29 |
| Measurement-outcome configurations | **[IMPORTED, verbatim]** | [B3] p.16, p.26 |
| Unistochastic process; subsystem disjunct | **[IMPORTED, verbatim]** | [B3] p.18–19 |
| L-1 (a), L-1 (b), the ladder, C4, the scope guard | **[IMPORTED, verbatim]** | `v11/note-L1-lorentz-no-go-lemma.md`:86–94, :107–114, :217–273, :286–298, :345–346 |
| Paper 8's three admissible covariance statements | **[IMPORTED, verbatim]** via L-1 | `v11/note-L1-...`:30–40 ← v3 paper 8:139–147 |
| `ds_report`, `tri_disc`, `chain_link_squares`, `polygon_violations`, `real_orth_2x2`, `orth_check_surd`, `modsq_check_surd`, `sylvester`, the `Surd` ring | **[REUSED, AST-extracted, anchored]** — signature pass plus KA-1/KA-2/KA-4/KA-5/KA-6 re-run against the committed values (`T = +1/27`; `T = −1/16` with phasor moduli `(0,0,1/2)`, i.e. squares `(0,0,1/4)`; zero 2×2 residuals; `H₈Hᵀ₈ = 8I`) | `v11/code/u3_unistochasticity_screen_exact.py`; values at `v11/note-u3-unistochasticity-screen.md`:141–151 |
| The positive-verdict discipline (certificate, never criterion) | **[IMPORTED, verbatim]** | `v11/code/u3_...`:1244–1248 |
| System-centric composition across the subsystem lattice | **[CITED, NOT DUPLICATED]** | `bc/note-bc1-division-event-composition-pin.md` |
| The Bell model, the two frames, the four grains, the two time correspondences, the search, every number in §2–§9 | **[THIS UNIT]** | `bc/code/bc2_two_frames_exact.py` |

---

## 12. Caps

- One Bell model; 36 configurations; six declared setting pairs; two
  frame orderings; four target times and three division events per frame.
- No continuum of boosts is built.  L-1(b) supplies the continuum
  statement and is quoted, not re-derived.
- Retrodictive transition matrices are not computed (Bayes-determined by
  the inventory; §3).
- No LP/Farkas search over non-group covariance semigroups (E4, OPEN).
- U3's polygon oracle takes rational entries; this model's entries lie in
  `Q(√2)`, so the polygon arm runs on the rational anchors only and the
  legs are decided by the strictly stronger certificate route.
- Frame-map search node cap `200 000` (maximum used `32`); sign-oracle
  refinement cap `8192` bisection steps (maximum used `120`).
