# D43a round 1 — hostile review (pin + receipt + out)

**Reviewer round:** 2026-07-19, against HEAD d26770f (d43a objects
identical to 96ca550; verified no drift). Objects: the pin
`v10/note-d43a-lie-trotter-rule-independence.md` (#328 + the §6
first-run amendment, which entered at 96ca550, not 8c2a191 — see F7),
the receipt `v10/code/d43a_lie_trotter_exact.py` (SERIES revision),
the output `v10/data/d43a_lie_trotter_exact.out`, read against v1 p1
(Definitions 2–4, Lemma 1, Theorems 1–3, Propositions 2–5, Lemma 3,
the line-706 orphan), v2 p1 (§3.1–3.5, §5 Theorem 1, §11 burden 4),
v1 p7 (Definition 1 strip basis, Theorem 1 closed form), v1 p8
(Propositions 1–2, Theorem 1, the onset-class contrast remark), the
root validator (`gamma` = entrywise |U|², line 78–84), LOG #328/#332.

**Method:** full independent rebuild in EXACT Gaussian-rational
arithmetic (`fractions.Fraction` re/im pairs, per-order coefficient
matrices, order recursion for inverses — no mpmath, no thresholds:
zero means zero), at BOTH L = 12 and L = 14, both masses; every
anchor, every kappa, every verdict recomputed; the E-coefficient
decomposed into Σ_{a+b}[J^(a),J^(b)]; the p8-faithful F/S/T channel
moments computed; the pin-literal and receipt strip splits both
tested; the v2 p1 §5 smeared (continuum-identified) comparison
computed exactly for both rules — the round's commissioned open
computation; plus byte-determinism (2 runs + committed .out), three
exit-1 mutations, dead-code scan, session-artifact archaeology.
Scripts: session scratchpad `referee_d43a.py`, `referee_extra.py`,
`mut1/2/3.py`; full log `referee_full.out`. Environment: Python
3.8.20, mpmath 1.3.0 (receipt run: ~59 s, exit 0). Nothing in the
repo modified except this file.

## VERDICT: 0 BLOCKER / 4 MAJOR / 3 minor / 2 nit

**Zero false numbers.** All six delivered verdict labels (T2
DIVERGENT ×4; T4 DIVERGENT at d = 1, 2 + SUPPORT-MISMATCH(EXC-zero)
at d = 3 ×2) are CONFIRMED as exact facts by threshold-free rational
recomputation at two lattice sizes. Every printed kappa is a genuine
exact ratio of the compared matrices. The four MAJORs are structural
and interpretive: the §6 amendment's mathematical rationale is false
(the LT defect IS the pure bracket — T4 at d = 2 is literally T2 at
d = 2 re-run on the same matrices), the d = 2 "kappas" are tie-break
artifacts from multi-ratio orbits, the pinned STRUCTURED clause is
vacuous as written, and — the round's centerpiece — the receipt's
own named escape is not merely possible: **I computed the smeared
comparison and the escape OCCURS.** The foundation alarm survives at
lattice-entrywise scope and must be re-aimed, not amplified.

---

## THE SMEARED-COMPARISON RESULT (the commissioned computation)

The orphan (v1 p1 line ~706) asks whether the two rules, "after the
appropriate onset renormalization and continuum identification, land
on the same tangential bracket." The corpus's own continuum
identification is v2 p1 §5: smear the onset-renormalized leading
one-region coefficients, K_a[N] = a Σ_n N(an) A_n, form
C_a[N,M] = [K_a[N], K_a[M]] = Σ N_n M_{n'} [A_n, A_{n'}], and read
the profile action on sampled spinors. For the LT rule the same
construction applies verbatim with A^LT_n := the Δ⁴ (onset)
coefficient of J^LT_n. I computed this exactly for both rules.

Reduction (exact, assumption-free): by commutator antisymmetry the
NM-symmetric part cancels and the leading profile action per
translation-invariant channel (δ = column−row site offset, spin pair)
is governed by the first-moment channel sums
τ(δ,s,s') = Σ_{r>0} r·Σ_i [A_0, A_r]_{(i,s),(i+δ,s')}, the continuum
∂x-coefficient by the collapse D(s,s') = Σ_δ δ·τ(δ,s,s'), and the
½∂xβ layer by the anchor-invariant χ0(s,s') = Σ_δ χ(δ,s,s') with
χ(δ) = Σ_{r>0} r(r·σ_r − 2m1_r) (invariant because Σ_δ τ = 0,
verified). Differences that are discrete divergences die against
smooth profiles at leading order; on the ring this is exactly the
channel-sum criterion.

Results (exact rationals, identical at L = 12; EXC side verified
against v2 p1 §3.5 — my machinery independently reproduces
K_∥ ∝ (β∂x + ½∂xβ)(I − α)):

| object | EXC | LT (m = 1/2) | LT (m = 1) |
|---|---|---|---|
| Com(r) nonzero at | r = 1, 2 | r = 1, 2, 3, 4 | r = 1, 2, 3, 4 |
| τ channel support | δ = ±1 (flip), ±2 (same) | + δ = ±3 (flip), ±4 (same) | same as m = 1/2 |
| τ^LT ∝ τ^exc? | — | **NO (support differs)** | **NO** |
| D collapse | 1·(I − σx) | (13/2304)·(I − σx) | (−1/72)·(I − σx) |
| χ0 collapse | 1·(I − σx) | (13/2304)·(I − σx) | (−1/72)·(I − σx) |

**THE ANSWER: after the corpus's own onset renormalization and
continuum identification, both rules land on the SAME tangential
operator ray K_∥[β] = (β∂x + ½∂xβ)(I − α) at leading order, with a
single per-mass constant covering both derivative layers:
κ(m = 1/2) = 13/2304, κ(m = 1) = −1/72.** The lattice-level channel
data genuinely differ (LT carries δ = ±3, ±4 channels and a
sign-scrambled near field), but all of it collapses/telescopes into
the same continuum bracket — precisely LOG #332's "structured
cancellation in the smooth-smeared continuum limit," now computed
rather than named.

Two sharp corollaries:

1. **The constant is mass-dependent AND changes sign** (positive at
   m = 1/2, negative at m = 1). Since any common Theorem-3 class
   forces the bracket ratio to be c_LT²/c_exc² > 0, the sign flip is
   a clean NEW no-go: there is NO shared local generator K_R with
   positive rule constants behind both rules — bracket-ray
   coincidence holds WITHOUT the shared-generator mechanism Theorem
   3 envisages. (Consistent with A^LT ≁ A^exc: A^LT is not even
   symmetric — 24-entry asymmetric part, entries ±1/16 — and its
   diagonal is mass-carrying: −1/24 at m = 1/2, −13/96 at m = 1 at
   (n0,↑), vs EXC's mass-free +1/2.)
2. **Scope of my computation:** leading order in a, singleton
   generators, free core, two mass points (the sign change is
   certified by two exact points). Subleading-in-a terms differ
   between rules; under v2 p1 §7's thin-slab scaling those are the
   suppressed corrections, but a full LT-side finite-slab (log-
   smeared) theorem remains the successor's job.

Consequence for the stakes: the coefficient anchor's OPERATOR
CONTENT (the tangential bracket ray, the (I − α) spin structure) is
rule-independent at this order and needs no re-scoping. What is
genuinely rule-relative: every lattice-entrywise coefficient
statement, the normalization, and the SIGN of the onset constant.
Downstream claims that use the EXC bracket's normalization or sign
as physical carry the re-scoping obligation; claims using only the
bracket's direction/structure survive.

---

## FINDINGS

**F1 — MAJOR, CONFIRMED. The §6 amendment's rationale is false: the
LT defect at Δ⁸ IS the pure bracket, exactly.** Pin §6 and the
receipt's [VERDICT] line rest on: "the LT defect at Delta^8 is NOT
the pure exchange bracket: it mixes [A^LT_R, A^LT_S] with
second-order one-region cross terms." Exact recomputation:
E^LT[Δ⁸] == [A^LT_R, A^LT_S] entrywise-identically at d = 1, 2, 3,
both masses, both L (and E^LT[Δ⁸] == Σ_{a+b=8}[J^(a),J^(b)] with
(4,4) the ONLY contributing pair — J^LT's ladder is even-only
[0,4,6,8], so no (3,5) terms exist, and the group commutator cancels
all non-commutator quadratic terms identically). Likewise
E^exc[Δ⁴] == [A⁽¹⁾_R, A⁽¹⁾_S] at d = 1, 2 and
E^exc[Δ⁶] == [A⁽¹⁾,A⁽²⁾] + [A⁽²⁾,A⁽¹⁾] at d = 3 (v1 p1 Prop 3
confirmed exactly). Therefore: **T4 at d = 2 compares the identical
matrix pair T2 compares** (verified as dict equality), T4's only
genuine additions are the d = 1 cells and the d = 3 support
corollary, and "T4, not T2, decides the orphan" is an empty
distinction at this fixture. No printed number is false; the
structural narrative is.

**F2 — MAJOR, CONFIRMED. The d = 2 per-cell kappas are tie-break
artifacts; the receipt printed two different "kappas" for the same
comparison.** The receipt anchors kappa at an argmax-|entry| of the
EXC coefficient; at d = 2 the max-magnitude orbit has 12 entries
carrying THREE distinct exact ratios. m = 1/2:
{−137/2304, −5/256, +79/2304}; m = 1: {−7/288, −3/128, +13/576}.
T2 reported −137/2304 and T4 reported 79/2304 (m = 1/2; resp. −7/288
vs 13/576 at m = 1) — but per F1 these are the SAME matrices; the
difference is which tied entry each code path's dict order selected.
−5/256 and −3/128 appear in neither output. The DIVERGENT verdicts
are logically sound (if a global κ existed it would equal the
anchored ratio, so any anchored refutation refutes existence), but
LOG #332's "EXACT RATIONAL mass-dependent ratios" list presents
non-canonical picks as if per-cell constants. Full invariant data
(ratio spectra on common support, each ratio on a 4-entry orbit;
identical at L = 14): d = 2 as above plus 52 LT-only entries;
d = 3 (m = 1/2): {−67/48, −19/48, −13/48, −59/240, −11/240, 1/24} +
4 LT-only; d = 3 (m = 1): {−19/12, −7/12, −11/24, −13/30, −7/30,
−7/48} + 4 LT-only. At d = 3 the max orbit is single-ratio (the T
channel), so −13/48 and −11/24 are well-defined under the receipt's
convention; T4 d = 1 max-orbit kappas −5/384 and 19/384 likewise
(full d = 1 spectra have 5 ratio classes + 36 LT-only entries).

**F3 — MAJOR, CONFIRMED. The pinned STRUCTURED clause is vacuous as
written; the receipt implements a different strip; the verdict is
nevertheless strip-robust.** Pin §4 defines the strip as "entries
with site components at graph distance ≥ d−1 from both interiors" —
under that literal reading the EXC strip is EMPTY at d = 2 and both
strips are EMPTY at d = 3 (computed), so STRUCTURED could never
fire. The receipt instead uses a near-R × near-S block
(N₁(R)-rows × N₁(S)-columns and transpose) — a reasonable
boundary-facing proxy but not the pinned text and not p8's object
either: p8's data are CHANNEL MOMENTS (the F/S/T strip basis of p7
Definition 1), not entry blocks. I computed all three: (i)
receipt-strip: 3 distinct ratios at d = 2, 4 at d = 3 → not
proportional; (ii) pin-literal: undefined (empty); (iii)
p8-faithful channel moments at d = 3: EXC Δ⁶ closes EXACTLY on the
six channels with p7 Theorem 1's closed form reproduced to the
rational (−1/768, +1/192, −1/768; 5/768, 5/768; 1/128 = h⁶·(−1/12,
1/3, −1/12; 5/12, 5/12; 1/2), residual 0), while the LT Δ⁸
coefficient does NOT close on that basis (12 residual entries) and
its channel moments are non-proportional (the six channel ratios =
exactly the F2 d = 3 spectrum; note also the LT bracket breaks the
EXC coefficient's left-right reflection symmetry: F-left 67/36864 vs
F-right 19/36864 at m = 1/2). So DIVERGENT stands under every
definition — broken clause, unaffected verdict.

**F4 — MAJOR, CONFIRMED (interpretive). LOG #332's alarm framing
overstates what the lattice verdict licenses.** "THE ORPHAN
ANSWERED — the free-core bracket is RULE-RELATIVE" + "downstream
coefficient claims carry the re-scoping obligation" reads the
entrywise verdict as the orphan's answer while the orphan explicitly
asks about the bracket AFTER continuum identification — which the
receipt did not compute and which I did (see the centerpiece): the
continuum-identified bracket ray IS rule-independent at leading
order; the honest headline is "rule-relative at lattice-entrywise
scope; rule-independent as a continuum ray; rule- and mass-relative
(sign-indefinite) in its onset constant." The pin itself scoped T2's
DIVERGENT as pre-registered and the LOG names the smeared limit as
the escape/successor, so this is an overstatement pending its own
named successor, not a false claim — but the re-scoping obligation
as broadcast is too broad (see the centerpiece's consequence
paragraph for the correct split).

**F5 — minor, CONFIRMED. The d = 3 SUPPORT-MISMATCH is a filtration
triviality, over-read in the LOG.** [A^exc_R, A^exc_S] = 0 at d = 3
is forced in one line: A⁽¹⁾ is supported in N₁ (v1 p1 Theorem 1),
N₁({n}) ∩ N₁({n+3}) = ∅, so both products vanish — verified exactly;
the LT Δ⁴ coefficient sits at filtration k = 2 (support radius 2,
verified), so its singleton brackets reach d ≤ 4 — nonzero at d = 3
(28 entries, verified). "The onset classes differ even in bracket
support" (LOG) is true but carries zero dynamical information beyond
κ_exc = 1 vs κ_LT = 2. Moreover Theorem 3's hypothesis (2) FAILS for
EXC at d = 3 (the first visible exchange is the mixed
[A⁽¹⁾,A⁽²⁾] + [A⁽²⁾,A⁽¹⁾], not the leading-leading bracket —
verified), so d = 3 was never inside the papers' bracket-level
universality scope; the meaningful d = 3 comparison is the channel-
moment one (F3(iii), genuinely divergent).

**F6 — minor, CONFIRMED. Pin drift on precision/method.** Pin header
and §5 pin dps 80, thresholds 1e-40, Vandermonde fits on
Δ ∈ {3..7}×10⁻²; the receipt runs dps 50, TOL 1e-30, exact series.
§6 discloses "series arithmetic, all anchors 1e-30" and the banner
discloses the rest, but §5 was never amended — under this campaign's
"strict pin" discipline the deviation should be in the pin, not just
the banner. (Substantively safe: my Fraction rebuild confirms every
receipt quantity exactly; the receipt's mpmath values are correct to
all printed digits.)

**F7 — minor, CONFIRMED. T4's pre-registration is retro-fitted.**
§6 entered with the GREEN commit (96ca550), not the pin commit
(8c2a191 ends at §5). Session artifacts show the sequence: T2-only
series build (d43a_series.out, 5 PASS), then a first T4 build that
FAILED — exit 1 with the d = 3 outcome labeled "ONE-ZERO" treated as
breakage (d43a_t4.out) — after which the delivery clause ("every
outcome incl. SUPPORT-MISMATCH is a delivered verdict") was written
to match the observed outcome. Harmless here because the outcome is
provable a priori (F5), but the receipt's "pre-registered" language
should be scoped to T2; T4 is a disclosed post-hoc amendment whose
verdict menu was finalized after first execution.

**F8 — nit, CONFIRMED. Receipt hygiene.** Dead code:
`m_scale_series` defined, never called; `CRl, CSl` assigned, never
read; `Ce = {}` immediately overwritten. Check gaps (no substantive
consequence — I verified the gaps are empty): AN3 tests only even
sub-onset orders of E^LT (odd orders 3, 5, 7 unchecked; they vanish
exactly — J ladders are even-only: J^exc [0,2,4,6,8], J^LT
[0,4,6,8]); AN1 spot-checks the paper entries but not vanishing
OUTSIDE the paper support (full-matrix equality holds — verified);
E^exc sub-onset orders never checked (they vanish — verified);
T4's `comm()` drops entries below a hard-coded 1e-45 inside an
otherwise exact pipeline (safe at dps 50 — smallest true entry
≥ 1/36864).

**F9 — nit, CONFIRMED. "Seed-independent (0/7)" is boilerplate for a
seedless receipt.** The receipt contains zero randomness (0
seed/random references); the meaningful property is byte-determinism,
which holds: two fresh runs byte-identical to each other AND to the
committed .out. The LOG/commit phrasing should say "deterministic;
rerun byte-identical" (the author's own s7 artifact is just an
identical rerun).

**Docstring history note (unverifiable, plausible).** The "first
build's fit floor (~1e-13)" claim has no repo artifact (single
commit); the magnitude is consistent with pin §5's own margin note
(Δ⁸ coefficient ≥ 1e-13 at the fit window's edge) and the session
timeline is coherent. Accepted as disclosed history.

---

## WHAT SURVIVES (verified positive content)

1. **All four anchors, exactly** (my Fractions, both L): AN1 —
   A⁽¹⁾ equals v1 p1 Prop 2 / v2 p1 §3.2 as a FULL matrix (including
   off-support zeros); AN4 — A⁽¹⁾_λ = (3/4)A⁽¹⁾ at λ = 1/2, all
   entries (and v1 p1 Prop 7's operator identity semantics); AN2 —
   the ±1/8 worked case incl. same-spin zeros; AN3 — E^LT onset
   exactly Δ⁸ at d ≤ 3 (all orders 1–7 vanish, odd included).
2. **The six delivered verdicts**: T2 DIVERGENT at all four cells is
   real non-proportionality (3 ratio classes at d = 2, 6 at d = 3,
   plus 52/4 LT-only entries); T4 DIVERGENT at d = 1, 2 (5 and 3
   ratio classes); the d = 3 EXC-zero/LT-nonzero facts. Mass
   dependence of every ratio: real (T3 delivered).
3. **The receipt's printed kappas** are all genuine exact ratios of
   the compared matrices at the anchored entries (well-defined at
   d = 1 and d = 3; orbit-ambiguous at d = 2 per F2).
4. **Conventions faithful**: Γ = entrywise |U|² (validator line
   78–84), J = Γ_loc·Γ_free⁻¹, E = J_R J_S J_R⁻¹ J_S⁻¹ (v1 p1 Def
   4), C_R/B_R splitting (Def 2), LT = bulk-then-collar (Benchmark
   prop.), the LT Δ^{2max(4,d)} law with the SAME J-convention.
5. **Wrap-freeness at L = 12** — proved and confirmed: at order
   p ≤ 8 a wrap needs one long path (total ≥ L = 12 > 8) or two long
   paths in one Γ/J coefficient of order k ≤ 6 (needs short-distance
   ≥ L − k/… ≥ 9 > 6 = max short-distance), impossible; E/bracket
   objects are products of order-≤6 factors. Every extracted
   rational is IDENTICAL at L = 14.
6. **Plumbing**: byte-deterministic; committed .out is a faithful
   byte-identical capture; three mutations (broken AN1 anchor,
   broken c_λ, wrong LT onset) all exit 1 through the anchor/
   extraction-breakage path as designed.
7. **New verified structure delivered by this round** (available for
   the successor): E^rule coefficients are pure/mixed brackets
   exactly (F1 identities); the p8-faithful channel-moment tables at
   d = 3 for both rules; A^LT's asymmetry and mass-carrying
   diagonal; the smeared τ/χ0/D tables and κ(m) = 13/2304, −1/72.

## PRESCRIBED REPAIRS (pre-verified where computable)

**R1 (for F1).** Strike the cross-terms sentence from §6 and the
"T4, not T2, decides" clause from the receipt verdict text; state
the exact identities E^LT[Δ⁸] = [A^LT_R, A^LT_S] and
E^exc[Δ^{2d}] = (pure/mixed brackets per v1 p1 Prop 3); present T4
as: T2's comparison extended to d = 1 plus the d = 3 support
corollary. All identities pre-verified here, both masses, both L.

**R2 (for F2).** Replace per-cell "kappa" at d = 2 with either the
full ratio spectrum (exact values in F2, pre-verified) or a
canonically anchored ratio (recommended: the T/S channel-moment
ratios of F3(iii), which are basis-stated and orbit-free). Amend
LOG #332's kappa list accordingly.

**R3 (for F3).** Amend pin §4's STRUCTURED clause to the p8-faithful
form: "proportional CHANNEL MOMENTS in the p7 strip basis (F/S/T)
with zero residual outside the basis." Pre-verified consequence: the
d = 3 verdict remains DIVERGENT under the repaired clause (six
distinct channel ratios; 12 LT residual entries), so no re-run is
strictly required — but the receipt's strip_split should either be
renamed (boundary-block proxy) or replaced.

**R4 (for F4/centerpiece).** Add the smeared comparison as the
round-1 delta (or adopt this review's computation after independent
confirmation): the continuum-identified bracket ray is shared,
κ(1/2) = 13/2304, κ(1) = −1/72, sign-indefinite ⇒ shared-K_R
Theorem-3 mechanism refuted while bracket-ray universality holds.
Re-scope LOG #332's downstream obligation per the consequence
paragraph above. Named successors: the LT-side log-smeared
finite-slab theorem (v2 p1 §7 analogue), κ(m) as an exact function
(more mass points; locate the zero crossing), the interacting
(p15-fixture) cross-check.

**R5 (for F6/F7/F8/F9).** Amend pin §5 to the as-run precision
(dps 50 / 1e-30 / series); scope "pre-registered" to T2 in the
banner; delete dead code; add the two one-line completeness checks
(odd orders of E^LT; off-support vanishing in AN1) — both
pre-verified to pass; replace "seed-independent (0/7)" with
"deterministic (rerun byte-identical to the committed .out)."

---

## Reproduction appendix

- Independent rebuild: scratchpad `referee_d43a.py` (exact
  Fractions; L = 12 full battery + smear; L = 14 wrap check; ~6 min
  total), `referee_extra.py` (bracket-identity battery). Full output
  preserved in scratchpad `referee_full.out`.
- Receipt runs: 2× byte-identical, identical to committed .out,
  exit 0, ~59 s each.
- Mutations (scratch copies only): AN1 diag 1/2→1/3 ⇒ exit 1;
  c_λ = λ(2+λ) ⇒ exit 1; p_lt = 6 ⇒ EXTRACTION-EMPTY ⇒ exit 1.
- Key exact values for the record: T2/T4 spectra as in F2; channel
  moments as in F3(iii) (m = 1: LT = 19/9216, −7/9216, 7/9216;
  −13/4608, −7/4608; −11/3072); smear tables as in the centerpiece
  (τ^LT at m = 1/2: δ=±1 flip ±1/9216, δ=±2 same ∓23/9216, δ=±3
  flip ∓1/1024, δ=±4 same ±1/512; at m = 1: ∓19/1152, ∓17/2304,
  ±1/128, ±1/512 — note the near-field sign scramble vs EXC's
  δ=±1 flip ∓1/2, δ=±2 same ±1/4).
