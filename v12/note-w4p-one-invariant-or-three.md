# v12 W4′ — ONE INVARIANT OR THREE: THE EXACT RELATION TABLE

**Status:** GREEN-UNREVIEWED-REPAIRED, STRICT, 2026-07-28.  Not
citable; terminal is conferred by a hostile round.  The first hostile
round returned ACCEPT-WITH-FIXES (3 M, 8 m, 5 n; nothing computed
wrong); the fixes are applied throughout, and this file and its
receipt are the repaired state.
**Pin:** `note-w4p-one-invariant-or-three-pin.md`, frozen before this
file existed.
**Binding:** paper 0 v2.1 §1 (T2′ Δᴮ and the three-defect
distinction; T3′), §2 (the evidence table's W4′ row), §4 (W4′), §5
(non-claims); LOG #1–#8; `bc/LOG.md` #2–#4, committed state only.
**Receipt:** `v12/code/w4p_relation_table_exact.py` →
`v12/code/w4p_output.txt`.  14 anchors, **66 gates, 66 pass, 0 fail**;
runtime 5.1 s; byte-identical under `PYTHONHASHSEED` 0, 12345 and
default, modulo timings.  Gate disclosures: §11.

**Verdict: W4′-NEITHER-ONE-NOR-THREE.**

The three objects the pin names are not one invariant.  They are not
three either.  At the resolution this receipt measures they are
**nine**, related by exactly **four strict implications**, **one
ingredient containment**, and **zero constructed equivalences**.  All
six cross-object pairs are **INDEPENDENT**, each carried by a pair of
exact models that agree on one invariant and differ on the other.

**The counting convention, stated once, both ways.**  Entries 4, 5 and
6 of §6 — AB, LC, SC — are three *nested levels of one* [AB]
hierarchy, not three unrelated objects: SC ⇒ LC ⇒ AB, both inclusions
strict on this zoo.  The headline **nine** counts the levels
separately, because each is separately decided here and each carries
its own witness.  Under the collapsed convention — one [AB] hierarchy
counted once — the number is **seven**.  Nothing in the relation table
turns on the choice: X enters every cell as the pair (level, γ ≠ 0),
and all six cross-object verdicts are identical under either
convention (gate H, §6).

Arithmetic: `fractions.Fraction` for rationals; ℚ(√2) with an exact
sign oracle, cross-anchored against W1′'s committed `Q2` oracle, for
the probability layer; W1′'s cyclotomic class `Cyc` (ℚ(ζ₈), ℚ(ζ₁₂))
for the amplitude layer, AST-lifted from the committed file; integer
column Hermite normal form for the [AMB] obstruction, which lives over
ℤ; an exact Phase-I simplex as the declared divisibility fallback (it
is never invoked — a certificate cascade decides all 144 queries).  No
float, no tolerance.  Substantive negatives exit 0; exit 1 is
anchor-only.

---

## 1. What is measured, and what is only cited

BC1 and BC2 are **not re-run**.  Their verdicts enter as fixed data
points, and every quoted constant is verified byte-wise against the
committed blob by `git show` — 25 quotations, all matched, as an
exit-1 anchor.  The bc working tree is dirty with frozen partial
edits; no code path here reads it.

Two things this unit does build:

1. **The contextual invariant on BC2's own quoted statistics.**  BC2's
   four unequal setting pairs `SP-A (0°,45°)`, `SP-B (0°,135°)`,
   `SP-C (90°,45°)`, `SP-D (90°,135°)` are exactly a CHSH 4-cycle, and
   its quoted law `P(α,β) = (1 − αβ cos(a−b))/4` gives E_ab =
   −cos(a−b).  Computing |CHSH| on those numbers is a **new invariant
   on old numbers**, not a re-run.
2. **A common-domain zoo.**  The corpus's own carriers have disjoint
   domains: BC1's models are closed unitary circuits with no
   measurement cover, so the contextual invariant is undefined on
   them; BC2's model carries no subsystem-lattice census, and BC2 §7
   E3c defers that question to BC1 by name.  Co-variation cannot be
   measured where the invariants are not simultaneously defined, so a
   zoo on which all four are defined is constructed here.

## 2. The objects, formalized

### 2.1 T — the temporal object, which is already three

    Δᴮ(U₂,U₁) = B(U₂U₁) − B(U₂)B(U₁)        the Born-shadow defect
    D₂₁₀      = Γ₂₀ − Γ₂₁Γ₁₀                 a DECLARED law's residual
    d_div     = 0 iff SOME column-stochastic K has K Γ₁₀ = Γ₂₀

W1′'s machinery is reused by AST lift from the committed receipt (31
functions and classes plus the one module constant `cyclotomic` closes
over; an AST signature pass on eight of them; the on-disk file is
gated byte-identical to the committed blob).  Six exit-1 anchors
reproduce W1′'s committed numbers: Δᴮ(H,H) = [[½,−½],[−½,½]];
**Δᴮ(H,W) = 0 with both factors fully unbiased**; the cross-term
identity on both pairs; the closed form Δᴮ = 0 ⟺ t+u ≡ ±2 (mod 8) on
all 4096 unbiased quadruples; Δᴮ₀₀ = −4032/15625 with the stochastic
divisor K = S(−175/527).

Two internal relations, both gated:

- **Δᴮ = 0 ⇒ d_div = 0**, *for the Born-declared pair* Γ₁₀ := B(U₁),
  Γ₂₀ := B(U₂U₁) — the divisor is K = B(U₂).  **What is gated is the
  substance, not the implication.**  Δᴮ = 0 *says* B(U₂U₁) =
  B(U₂)B(U₁), which is the witness equation itself, so the implication
  is definitional once the divisor is admissible; the non-trivial
  ingredient is that K = B(U₂) is a legal divisor at all.  That is
  what the gate checks: eight census Born shadows, each exactly
  rational with unit column sums.  The 16-pair walk is retained as an
  arithmetic consistency check and is, as coded, a tautology — said so
  in-receipt.
- **Strict**: d_div = 0 while Δᴮ ≠ 0 (W1′ C+1's rational instance).

D₂₁₀ equals Δᴮ **only** under the Born declaration Γ₂₁ := B(U₂).  So T
is a three-element family with one implication and no identities
before any other object is met.

### 2.2 X — the contextual object, which is also not one

The scenario is the CHSH 4-cycle: X = {A₀,A₁,B₀,B₁}, cover
C₁={A₀,B₀}, C₂={A₀,B₁}, C₃={A₁,B₁}, C₄={A₁,B₀}, outcomes {±1}.
Adjacent contexts meet in one measurement; opposite contexts meet in
the empty set, whose only section is the empty one, so those overlaps
impose equality of coefficient sums.

Six empirical models are declared exactly, each verified normalized,
non-negative and no-signaling in ℚ(√2):

| model | max CHSH | level | consistent global assignments | non-extendable local sections |
|---|---|---|---|---|
| DET | 2 | NC | 1 | 0 |
| UNIF | 0 | NC | 16 | 0 |
| LCORR | 2 | NC | 2 | 0 |
| SINGLET | 2√2 | PC | 16 | 0 |
| HARDY | 12/5 | LC | 5 | 1 |
| PR | 4 | SC | 0 | 8 |

The probabilistic obstruction is decided by **certificates in both
directions**: a positive exhibits a global section and verifies all
sixteen induced marginals; a negative exhibits a linear functional
whose maximum over all sixteen deterministic global sections is
computed in-receipt (it is 2) and is strictly below the model's value.
[F] enters only as an independent cross-check, and agrees on all six.

The [AMB] cohomological witness is computed for the definition printed
in full in the receipt: with S the support presheaf and F = F_ℤS the
free abelian presheaf it generates, γ(s₀) = 0 iff there are
r_i ∈ F(C_i) with r_{C₀} = s₀ agreeing on every overlap, the empty
ones included.  That is an integer linear feasibility problem, decided
by Hermite normal form.  Results:

| model | γ ≠ 0 at | over ℚ |
|---|---|---|
| DET / UNIF / LCORR | 0 of 4 / 16 / 8 | 0 |
| SINGLET | **0 of 16** | 0 |
| HARDY | **0 of 13** | 0 |
| PR | **8 of 8** | 8 |

**Attribution, before the numbers: both vanishing results are [AMB]'s
own.**  They are **reproduced independently here — [AMB]'s own
examples** — and are not this unit's findings.

- **HARDY.**  [AMB] §5 *"Examples"* **opens** with Hardy — *"We begin
  with an example to show that false positives do indeed arise"* — and
  exhibits the same support table up to outcome relabelling (support
  fingerprint (3,3,3,4), 13 sections; gated here) together with the
  same ℤ-family mechanism, r₂ = s₆ + s₇ − s₈, the negative coefficient
  that defeats the support restriction, concluding that γ(s₁)
  vanishes.
- **SINGLET.**  [AMB] Proposition 4.5's first clause: *if the model is
  possibilistically extendable, the obstruction vanishes for every
  section in the support.*  supp(SINGLET) = supp(UNIF) is full and
  UNIF is extendable, so the singlet verdict is an immediate corollary
  of [AMB]'s own proposition.  ([AMB] Prop. 4.3 is the
  compatible-family criterion this receipt implements.)

**[AMB]'s terminology is "false positive"** (§4: a compatible family
exists but determines no bona fide global section) — the obstruction
vanishes though the model *is* contextual.  What this note elsewhere
calls a "false zero of γ" names the same thing.

With that attribution in place: γ vanishes identically on the singlet
at the CHSH settings — a model with *no global section at all* —
because full support lets every local section extend to a compatible
ℤ-family.  It also vanishes on HARDY, which has a genuinely
non-extendable local section.  On this zoo the witness fires on the
strongly contextual PR and on nothing else.  **γ is therefore a
separate object, strictly weaker than the AB obstruction** — [AMB]'s
own stated status for it — and any argument treating it as *the*
contextual invariant is wrong on the corpus's own headline model.
This unit's contribution here is the exact integer certificate and the
placement of these known facts inside the relation table.

**Scope, engraved:** the γ verdicts above are verdicts about the
definition implemented, which is printed in the receipt.  No claim is
made to reproduce any published per-model table.

### 2.3 B1, B2 — the measured BC obstructions

**BC1** (cited, `bc/note-bc1-...` @ `42d8610`).  Its predicate, quoted
verbatim: *DIV_S(t_k) holds iff for every grid target t_b ≥ t_k there
exists a column-stochastic X_b on C_S with X_b Γ_S(t_k←0) =
Γ_S(t_b←0).*  **BC1's predicate is built from d_div** — the third
member of T's family, neither Δᴮ nor D₂₁₀.  In its honest form (the
same phrasing §5 uses, carried here so the claim never appears bare):
**B1 is a functional of the lattice-extended d_div family** — the
∀-over-targets conjunction of the d_div *atom*, evaluated on
*per-subsystem reduced* matrices.  It is not the atom itself, and this
is a containment of **ingredients**, not of **values**.  BC1's own
text already states the connection: *"This is U1's (D1) conjoined over
the spanning pairs that straddle t_k"* — the identification is BC1's,
quoted (and gated for provenance), not this unit's discovery.  It is
not an identification of the invariants (§5).  Data points used: GS0 88/88, GS1 66/88, GS2 88/88,
GS3 22/88; GHZ-Clifford with DIV_ABC = {0,1,2,3,4} and
DIV_BC = {0,1,3,4}; the quantum product model with DIV_ABC = {0,4} and
no crossing; the classical Markov control dividing everywhere (385
slots) and satisfying all four axioms; ten grid slices with no
non-empty consistent assignment.

**BC2** (cited, `bc/note-bc2-...` @ `cbb7279`), **with `bc/LOG.md`
#4's corrections carried forward, not the superseded text**:

- **M-1**: the declared intermediate division event violates the law
  of total probability at SP-C/D/F; on that model *"legitimate
  division event ⟺ the process divides at it"*.  The legitimate census
  therefore lives on the divisible instances, and the negatives at
  SP-C/D/F are carried by initial-division-event objects
  (round-verified).
- **M-2**: E2 was mis-scored — with all target times kept it fails.
  **This unit uses no E2-based witness anywhere.**
- **M-3**: the non-mappable object is the intermediate-slice composite
  description, not the final-time law.
- The pointer-free replication: 24/24 permutations fail.

Data points used: 16 of 16 cells empty at unequal settings, both
correspondences, all four grains; `PI` at grain G-SUPP for SP-E and
SP-F; and the divisibility census — Γ(3←2)Γ(2←0) **equals** Γ(3←0) at
SP-A, SP-B, SP-E and differs in 576 entries at SP-C, SP-D, SP-F, in
both frames.

**On BC2's own model, in one place:** X = PC (contextual, |CHSH| =
2√2) with γ = 0; the frame obstruction nonzero at all four CHSH
settings; the temporal residual zero at SP-A/SP-B and nonzero at
SP-C/SP-D.  Three invariants, one model, three different patterns.

## 3. The common-domain zoo

**Carrier.**  Configurations C = {(p_A,p_B)}, p_X ∈ {r,+,−}: two
measurement-outcome pointers ([B3] p.16), |C| = 9, initial (r,r).
A-MEASURE overwrites p_A with x ~ P_A(·|a), p_B untouched; B-MEASURE
overwrites p_B with y ~ P(·|p_A,b), p_A untouched, using the marginal
P_B(·|b) whenever p_A = r or the conditioning event has probability
zero — a declared convention on unreachable columns.  Frames F1 =
(A,B) and F2 = (B,A) order the same two events.

**Prefix** NONE, or SWAPBACK: two pointer-exchange steps first, so
Γ(2←0) = I.  The prologue is gated to change **no statistic** — the
final-time distribution is identical, hence the empirical model, hence
X, is literally the same object.

**Variant** REC: the declared second leg is the true conditional law
(a stable record of the first outcome is read).  **Variant COH**: the
declared second leg **discards the classical record** and uses the
bare marginal P_B(·|b), so its residual D₂₁₀ = joint − product is a
**declared-law residual** at the wing cut.

**Naming discipline, engraved** (paper 0 v2.1's three defects).  There
are **no phases anywhere in this zoo**: the tables are stochastic and
no amplitude realization is built for any of them (§9.5).  What COH
discards is a *classical record*, not a phase — "phase-forgetting" was
the wrong word and is withdrawn.  What is measured at the wing cut is
therefore **D₂₁₀ and nothing else**.  It is **not** Δᴮ and is not
called a Born-shadow defect: Δᴮ requires a unitary pair, D₂₁₀ = Δᴮ
holds only under the Born declaration Γ₂₁ := B(U₂), and that
declaration is unavailable here.  Every finding of §3.1 is a finding
about D₂₁₀.

6 tables × 2 variants × 2 prefixes = **24 processes**, each on all
four contexts.

### 3.1 T on the zoo

| prefix / variant | T = (some D₂₁₀ ≠ 0, some d_div ≠ 0) |
|---|---|
| NONE, REC | (F,F) on every table |
| NONE, COH | (F,F) on DET, UNIF; **(T,F)** on LCORR, SINGLET, HARDY, PR |
| SWAPBACK, REC | (F,F) on every table |
| SWAPBACK, COH | as NONE, COH |

Three gated findings:

- **REC kills the declared residual** at every cut and every context —
  T3′'s constructive instance on a Bell carrier.
- **COH's residual is nonzero exactly on the correlated tables.**
  D₂₁₀ at the wing cut is joint − product: **a correlation measure.**
  The *local* LCORR table carries the same D₂₁₀ as the singlet, and
  the superquantum PR carries no more.  The object measured is D₂₁₀
  alone; no Δᴮ is defined on any Bell table in this receipt.
- **d_div = 0 across the whole zoo — and that is forced by the
  carrier, not measured.**  New structural gate: at **all 144 cuts**
  the distinct source columns are **pairwise support-disjoint**
  (144/144, distinct-column counts {3, 9}).  The reason is explicit:
  the A-step's column at (u,v) is δ_v on the B pointer tensored with
  p_A on the A pointer — it does not depend on u, so the cut carries
  at most **three** distinct columns, one per v-block, with disjoint
  supports; the SWAPBACK prologue cut is a permutation, nine columns
  of support size one, also disjoint.  Whenever that holds, the
  disjoint-support construction builds a column-stochastic divisor for
  **any** column-stochastic target, so d_div = 0 here is independent
  of table, variant, prefix *and* target.  The construction is run
  unconditionally at all 144 cuts and verified, not only where the
  certificate cascade happened to reach it.  Consequently: **d_div is
  constant on this carrier by construction; W1′ C+1's separation is
  re-anchored from the committed value Δᴮ₀₀ = −4032/15625 with
  K = S(−175/527), not re-measured here.**  What the zoo does show is
  that the *declared* residual D₂₁₀ separates on a carrier where the
  existential one is constant.  All 144 divisibility queries of this
  layer are decided by exact certificates (114 declared-bridge, 30
  disjoint-support construction); the LP fallback is never invoked and
  nothing is UNDECIDED-BY-CAP.

### 3.2 B1 on the zoo

BC1's axioms on the lattice {A, B, AB}, reading C (conditional on the
complement's configuration, p₀-independent), c* = r.

| prefix | D(A) | D(B) | D(AB) | (GS0, GS1, GS2) |
|---|---|---|---|---|
| NONE | {0,1,2} | {0,1,2} | {0,1,2} | (T, T, T) |
| SWAPBACK | {0,2,3,4} | {0,2,3,4} | {0,1,2,3,4} | (T, **F**, T) |

SWAPBACK reproduces **BC1's crossing mechanism exactly**: the
composite divides at a permutation step where the atom cannot, because
the atom's reduced matrix there has constant columns and cannot reach
the identity.  Independent of table and variant.

### 3.3 B2 on the zoo

**This is not BC2 re-run.**  It is a reduced analogue at |C| = 9,
structurally modelled on BC2's declared comparison: the compared
content is {p(t)} and {Γ(t←0)} under a declared time correspondence;
the forward second legs are not index-matched under φ_LOR and are
dropped (BC2 §5.1); the admissible map class is the permutations of C
(L-1(a), quoted by BC2); the search is exhaustive by invariant-pruned
DFS, so a negative is a proof of non-existence inside that class (max
10 nodes used, cap 200 000).  Grains: G-FULL, G-FIX, G-SUPP.

Verdict vector (φ_LOR: FULL, FIX, SUPP | φ_ORD: FULL, FIX, SUPP); `T`
= a permutation exists and is verified entrywise, `-` = none exists.
Independent of variant and prefix:

| table | B2 |
|---|---|
| DET, LCORR, PR | `- - T \| T T T` |
| UNIF, SINGLET | `- - - \| T T T` |
| HARDY | `- - - \| - - -` |

Three gated facts: the coarse grains are empty under φ_LOR and maps
live only at G-SUPP — the same shape as BC2's own table; the
instrument is sensitive to the **time correspondence** (φ_ORD admits
the wing-exchange map on the outcome-symmetric tables where φ_LOR
admits nothing), reproducing BC2's two-correspondence structure; and
**the separating invariant at G-SUPP is support size, gated as a
biconditional on all six tables and all 24 processes**:

    T at φ_LOR/G-SUPP  ⟺  max joint support ≤ 2

with maxima DET 1 (T), LCORR 2 (T), PR 2 (T), UNIF 4 (−),
SINGLET 4 (−), HARDY 4 (−) — six for six.  It is the same invariant
`bc/LOG.md` #4 reports for its pointer-free replication.

## 4. THE RELATION TABLE

The test is declared before any model is built.  For an ordered pair
(P, Q): **Q is not a function of P** iff two zoo models exist with
equal P and different Q.  Witnesses both ways ⇒ INDEPENDENT.  One way
only ⇒ MAPPED-BUT-INEQUIVALENT.  Neither ⇒ UNSEPARATED-ON-THIS-ZOO —
which is *not* reported as IDENTICAL, since IDENTICAL would require a
constructed equivalence, gated.  Witness pairs are chosen to differ in
the fewest model coordinates, preferring pairs that share the table
(for those the empirical model is literally the same object, not
merely equal in invariant value); ties break lexicographically, so the
choice is deterministic.

| pair | verdict | witness: Q not a function of P | witness: P not a function of Q |
|---|---|---|---|
| **T vs X** | **INDEPENDENT** | DET/REC/NONE and HARDY/REC/NONE: T = (F,F) both, X = NC vs LC | HARDY/COH/NONE and HARDY/REC/NONE: X identical (LC, γ=0), T = (T,F) vs (F,F) |
| **T vs B1** | **INDEPENDENT** | DET/COH/NONE and DET/COH/SWAPBACK: T = (F,F) both, GS1 T vs F | HARDY/COH/NONE and HARDY/REC/NONE: B1 identical, T = (T,F) vs (F,F) |
| **T vs B2** | **INDEPENDENT** | DET/COH/NONE and UNIF/COH/NONE: T = (F,F) both, B2 differs at G-SUPP | HARDY/COH/NONE and HARDY/REC/NONE: B2 identical, T = (T,F) vs (F,F) |
| **X vs B1** | **INDEPENDENT** | DET/COH/NONE and DET/COH/SWAPBACK: X literally the same model, GS1 T vs F | DET/COH/NONE and HARDY/COH/NONE: B1 identical, X = NC vs LC |
| **X vs B2** | **INDEPENDENT** | DET/COH/NONE and UNIF/COH/NONE: X = (NC, γ=0) both, B2 differs | DET/COH/NONE and PR/COH/NONE: B2 identical, X = NC vs **SC** |
| **B1 vs B2** | **INDEPENDENT** | DET/COH/NONE and HARDY/COH/NONE: B1 identical, B2 differs | DET/COH/NONE and DET/COH/SWAPBACK: B2 identical, GS1 T vs F |

Six of six INDEPENDENT.  Zero IDENTICAL.  Zero
MAPPED-BUT-INEQUIVALENT.

**The witness choice is a tie-break, not a necessity.**  The selector
prefers the pair differing in the fewest model coordinates, so where a
same-table pair exists it wins.

*Three* cells — **T vs B1**, **X vs B1** and **B1 vs B2**, i.e. every
cell whose partner is B1 — are carried by DET/COH/NONE against
DET/COH/SWAPBACK, which shares the table, so the two models induce
*the same empirical model* (identical statistics, identical X) while
GS1 flips.  (Gated: exactly those three cells, and no other.)

The three **T-row** cells are carried by HARDY/COH against HARDY/REC,
where the empirical model is untouched and only the declared leg
changes.  Those are the tie-break's choice, **not the only witnesses
available**: a *physics-varying* witness exists for all three T-row
cells as well, and is gated — **DET/COH/NONE against LCORR/COH/NONE**,
different tables and different physics, holds X = (NC, γ=0),
B1 = (T,T,T) and B2 = `- - T | T T T` all equal while T moves from
(F,F) to (T,F).  So none of the three T-row verdicts rests on
declaration-only separation.

### 4.1 The pin's named separating models, each in-receipt

**(a) A single-context composition with Δᴮ ≠ 0 and no contextuality.**
The pair (H,H) over ℚ(ζ₈) has Δᴮ = [[½,−½],[−½,½]] ≠ 0.  **The induced
empirical model is now built, not assumed** (the earlier gate checked
only a uniform section's marginal and was mislabelled; repaired): the
two declared cuts of the (H,H) composition are read as the one context
{A₀,B₀}, A₀ the intermediate outcome and B₀ the final one, with the
declared two-time law P(x,y) = B(H)_{y,x} B(H)_{x,0} computed from the
lifted Born shadow and converted exactly to ℚ (basis 0 ↦ +1,
1 ↦ −1).  It comes out uniform, P ≡ ¼, and is gated normalized and
non-negative.  A one-context model always has a global section —
extend by a product with an arbitrary distribution on the unmeasured
A₁, B₁ — and the uniform 16-atom global distribution is exhibited and
verified to restrict to *that model* entrywise.  Temporal defect
present, contextual obstruction absent.

**(b) Contextuality without a quantum realization.**  PR is strongly
contextual with CHSH = 4.  Every U(1)-Gram correlator obeys the AM-QM
certificate, gated here as an exact polynomial identity
8 − (p+q)² = (p−q)² + 2(4 − p² − q²), so |CHSH| ≤ 2√2 < 4 ("Gram =
quantum" imported from [T], exactly as W1′ does).  **The map X → T is
partial**: at PR there is no temporal defect to compare to.

**(c) The BC2 model at settings where the legs divide and the frame
obstruction stands** — cited, inside a single committed model, with
M-1 carried:

- **SP-A**: legs divide; frame cells empty at all four grains, both
  correspondences.
- **SP-E**: legs divide; frame cell `PI` at G-SUPP — a map exists.
  ⇒ **equal temporal value, different frame value.**
- **SP-C**: legs do not divide (576 differing entries) *and* the
  declared division event is illegitimate there (M-1); frame cells
  empty exactly as at SP-A, carried by initial-division-event objects.
  ⇒ **different temporal value, equal frame value.**

Both directions of independence, inside one committed model, with no
re-run and no new arithmetic.

**(d) The Δᴮ(H,W) = 0 witness.**  Both factors fully unbiased —
maximal amplitude coherence — and the defect exactly zero, by phase
alignment (W1′'s closed form t+u ≡ ±2 mod 8).  A vanishing temporal
defect certifies nothing classical.  Its structural twin is the
vanishing γ on the contextual singlet — which is **[AMB]'s own
result** (Prop. 4.5), and which [AMB] calls a *false positive* of the
compatible-family criterion: **two invariants, two false zeros, on
different models** — the zero-loci do not agree even where both are
defined.  The two ingredients are W1′'s and [AMB]'s respectively; only
the juxtaposition is this unit's.

## 5. The one genuine containment

BC1's predicate is built from d_div — it is the ∀-over-targets
conjunction of the d_div atom on per-subsystem reduced matrices, and
BC1's own text says so ("This is U1's (D1) conjoined over the spanning
pairs that straddle t_k") — so **B1 is a functional of the
lattice-extended d_div family**, not of the atom.  Gated: no two zoo
models share (D(A), D(B), D(AB)) and differ in (GS0, GS1, GS2).  And
that family is
**strictly finer** than T as declared — gated: T, which is a function
of the composite's declared cuts, does not determine the lattice
family.

This is a containment of **ingredients**, not of **values**.  As
declared invariants of a model, B1 and T separate both ways (§4).  The
honest statement is that they share an ingredient and are not
functions of one another.  Nothing in the corpus licenses more.

## 6. The count

| # | invariant | where |
|---|---|---|
| 1 | Δᴮ, the Born-shadow defect | §2.1, W1′ |
| 2 | D₂₁₀, a declared law's residual | §3.1 |
| 3 | d_div, existential divisibility | §3.1, W1′ |
| 4 | the AB no-global-section obstruction | §2.2 |
| 5 | logical contextuality | §2.2 |
| 6 | strong contextuality | §2.2 |
| 7 | γ, the [AMB] cohomological witness | §2.2 |
| 8 | B1, lattice non-gluing | §2.3, §3.2 |
| 9 | B2, frame non-mappability | §2.3, §3.3 |

Entries 4, 5 and 6 are one [AB] hierarchy's three nested levels;
counted once, the total is **seven**.  Both conventions are stated at
the head of this note and gated in-receipt; the relation table is the
same either way.

**Strict implications found (four):** Δᴮ = 0 ⇒ d_div = 0 (strict, W1′
C+1; for the Born-declared pair, §2.1); SC ⇒ LC ⇒ AB (both strict: PR,
HARDY, SINGLET); γ ≠ 0 ⇒ AB (strict: **SINGLET *and* HARDY** — both
are contextual with γ = 0 at every section; the receipt prints both
witnesses).
**Ingredient containment found (one):** §5.
**Constructed equivalences found: none.**

## 7. What this decides for the programme

- **Paper 0 v1's T5, "BC1/BC2 as one class", is falsified as stated.**
  B1 and B2 are independent, with witnesses both ways; and on the
  corpus's own carriers they are not even simultaneously defined.
- **Paper 0 v2.1's refusal to assert that Δᴮ governs contextual
  gluing is vindicated** and can now be restated as a measurement
  rather than a caution: T and X are independent, with witnesses of
  *two* kinds — one holding the empirical model fixed and moving only
  the declared leg (HARDY/COH vs HARDY/REC), one moving the physics
  (DET/COH/NONE vs LCORR/COH/NONE, X held fixed).  Neither is "the
  strongest"; the receipt's tie-break picks the first, and the second
  is gated so the verdict does not rest on declaration-only
  separation.
- **U2's warning is discharged by measurement, not by quotation.**
  One was assumed; nine are measured (seven under the collapsed
  convention — the head of this note states both).
- **A finding beyond the pin — about D₂₁₀, and only about D₂₁₀.**
  D₂₁₀ at a wing cut is joint − product, i.e. the covariance at the
  COH leg: a *correlation* measure.  The local LCORR table carries
  exactly the D₂₁₀ the singlet does, and PR carries no more.  So the
  **declared-law residual** does not distinguish local correlation
  from quantum correlation from superquantum correlation at this cut.
  **Scope, engraved (paper 0 v2.1's three-defect discipline).**  This
  is *not* a statement about Δᴮ.  No amplitude realization is built
  for any Bell table in this receipt (§9.5), so Δᴮ is undefined on all
  six.  The statement transfers to Δᴮ **only** for a composition that
  makes the Born declaration Γ₂₁ := B(U₂) available, and no such
  composition is exhibited here; whether a Born-declared realization
  of these tables would inherit the collapse is **not decided by this
  unit**.  The earlier form of this bullet — that a programme
  statement reading Δᴮ ≠ 0 as a mark of quantumness "fails on a
  classical two-bit table" — conflated the two objects and is
  withdrawn.
- **A second finding beyond the pin.**  Both of the programme's two
  candidate "master" invariants have **false zeros**: Δᴮ vanishes on a
  fully unbiased pair by phase alignment, γ vanishes on the
  Tsirelson-saturating singlet by full support.  They do not vanish
  together.  A single master invariant would have to have a zero-locus
  that both of these agree with, and no such locus exists in this zoo.

## 8. Antecedents, and what is this unit's

- **[AB]** Abramsky–Brandenburger, NJP **13** 113036 (2011) — the
  presheaf formulation, the global-section criterion, the
  possibilistic hierarchy.  **Imported whole**; gates X1, X2, X3.
- **[AMB]** Abramsky–Mansfield–Barbosa, *The Cohomology of
  Non-Locality and Contextuality*, arXiv:1111.3620 — the
  cohomological obstruction and its sufficient-not-necessary status.
  **The notion is theirs, the criterion implemented is theirs
  (Prop. 4.3), the terminology is theirs ("false positive", §4), and
  *both vanishing verdicts below are theirs*: §5's opening example
  *is* Hardy, with the same ℤ-family r₂ = s₆ + s₇ − s₈, and
  Prop. 4.5's first clause (possibilistic extendability ⇒ vanishing
  obstruction on the whole support) delivers the singlet as a
  corollary.**  This unit contributes an independent exact-integer
  reproduction of both, on the definition printed in the receipt, and
  their placement in the relation table.  Gates X4.
- **[F]** Fine, PRL **48** 291 (1982) — used as a cross-check only;
  both directions of the contextuality decision are certified
  independently in-receipt.
- **[T]** Tsirelson — "Gram = quantum" imported at gate SEP(b), not
  re-derived; the same import W1′ makes.
- **[B1]**, **[B3]** Barandes — the Born projection's cross-term; the
  division-event kinematics and measurement-outcome configurations.
- **[REV2]** — the three-defect distinction, re-anchored and
  re-measured here.
- **[BC1]**, **[BC2]** — cited data points with verified provenance,
  BC2 with `bc/LOG.md` #4's corrections carried.
- **W1′** — every reused function and every reused number, AST-lifted
  and anchored exit-1.

**This unit's own:** the relation table and its declared test; the
common-domain zoo and the three toy instruments on it; the observation
that D₂₁₀ at the COH wing cut is a correlation measure (about D₂₁₀
only — §7); the juxtaposition of the two false zeros; and the
carrying-forward, from BC1's own text, that BC1's predicate is built
from d_div rather than Δᴮ.

**Explicitly *not* this unit's:** the vanishing of γ on Hardy and on
the singlet — those are [AMB]'s own published results (§5 and
Prop. 4.5), reproduced independently here; the sufficient-not-
necessary status of γ, which is [AMB]'s stated result; and the
d_div/(D1) connection in BC1's predicate, which BC1 states itself.

## 9. Caps and scope

1. **No claim about nature.**  One measurement scenario (the CHSH
   4-cycle), binary outcomes, six empirical models, 24 processes,
   |C| = 9, three or five grid times.
2. **INDEPENDENT means what the test says**: neither invariant is a
   function of the other *on this zoo*.  It is a negative result about
   determination, not a claim that no relation of any kind exists —
   §5 exhibits one that does.
3. **The toy B1 and B2 instruments are declared reduced analogues**,
   not BC1 and BC2.  The lattice has two atoms, so BC1's GS2 is
   vacuous here; BC1's third atom, its GS2 failures, its ten hard
   obstructions and its 1 296-circuit sweep are cited, not reproduced.
   The frame search proves non-existence **inside the permutation
   class** (L-1(a)), not outside it.
4. **γ is computed for the definition of the receipt's §3.4 and no
   other** — which is [AMB] Prop. 4.3's criterion.  That HARDY is a
   false positive of it is **[AMB]'s own settled result** (§5), not an
   open question, and this receipt reproduces it; no cell of the
   relation table depends on HARDY's γ.
5. **No amplitude realization is built for the Bell tables.**  The
   amplitude layer is W1′'s (H, W, F₃); the bridge to the stochastic
   layer is the Born-declaration identity, stated and not smuggled.
   Consequently **Δᴮ is undefined on all six Bell tables**, and every
   zoo finding is about D₂₁₀ or d_div.
6. **Δᴮ is never equated with indivisibility.**  W1′ C+1's separation
   is **re-anchored** here, not re-measured: d_div is constant on this
   carrier by construction (§3.1).
7. Paper 0 v2.1 §5's non-claims stand unmodified.  v11 and BC remain
   halted; this unit touches neither.

## 10. What this unit hands over

- **Paper 0** owes a dated correction at §2's evidence table: the W4′
  row's hypothesis is decided, negatively, and T5's BC1/BC2 bundling
  is dead.  The T2′ scoping sentence ("whether it also governs
  contextual gluing is W4′'s open question") can be replaced by the
  measurement.
- **W3′** receives §3.1: the record kills D₂₁₀ at every cut and every
  context on a Bell carrier, with d_div identically zero throughout —
  the latter *forced by the carrier*, so it carries no information.
  The theorem W3′ wants is about D₂₁₀ on the record algebra, and the
  carrier here is a worked instance, not a proof.
- **W5** receives §2.3's carried quotation: BC1's predicate is built
  from d_div (BC1's own "(D1) conjoined over the spanning pairs"),
  which is where a Barandes recast of "division events = where the
  defect dies" has to be anchored — not on Δᴮ.
- **W2a/W2b/W2c** receive nothing from this unit.

## 11. Disclosures

The receipt AST-audits itself for these; the counts below are printed
by the receipt at §7.4 and cannot drift from the code.

- **11 of the 66 gates are asserted, not computed** — their predicate
  is the literal `True`, and they record a declared scope, a
  provenance already established by an exit-1 anchor, or a quotation:
  T-int ×2 (the W1′ C+1 strictness anchor; the Born-declaration
  scoping), B1c, B2c (both provenance, anchored at §0.2), SEP(c) (the
  cited BC2 settings), and H ×6 (the honesty gates: BC cited-not-run;
  `bc/LOG` #4 carried; reduced analogues; the [AMB] definition
  reported; Δᴮ never equated with indivisibility; no claim about
  nature).
- **~8 further gates re-assert an already-gated or already-anchored
  boolean**: T-int (phase alignment), SEP(a) Δᴮ ≠ 0, SEP(b) PR's CHSH,
  SEP(d), X4 (sufficiency), Z3 (the coarse grains), and the two H
  gates that restate the six REL verdicts.
- **SEP(a) is repaired.**  It previously checked a uniform section's
  marginal while claiming to construct the (H,H)-induced empirical
  model.  The model is now built from the lifted Born shadow and the
  global section is verified against it entrywise (§4.1a).
- **The [AMB] verdicts on HARDY and the singlet are [AMB]'s own**
  (§5, Prop. 4.5), reproduced independently here — see §2.2 and §8.
- **d_div ≡ 0 on the zoo is forced by the carrier**, not measured
  (§3.1); W1′ C+1's separation is re-anchored, not re-instantiated.
- **The Bell layer carries no amplitudes**, so no zoo finding is a Δᴮ
  finding (§9.5).
- The zoo is **this unit's construction**, built after the pin; only
  the four separating models of §4.1 and the independence test itself
  were fixed in advance.
