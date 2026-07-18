# D42b3 — placement: two no-gos, two laws, and the discrete TS-condition
# (front 5; the front-9 bridge identified)

**Status:** CAMPAIGN PIN (strict), 2026-07-18. Base: the d42a TERMINAL
grammar (#289) and its declared 1+k/4 ladder (A7/A7'). Receipt:
`v10/code/d42b3_placement_exact.py` (enumerates the d42a family; the
d42b1 extension inherits by the same arguments — carried, not gated
here while its round runs).

## 1. Pinned claims (stated before the receipt)

- **T1 (actor-local no-go, THEOREM-class).** No initiator-view-local
  re-weighting (counter-term) can restore per-initiator normalization:
  there exist history pairs where the initiator's OWN view is
  IDENTICAL (equal own-view canonical DAG) but the per-initiator sum
  differs (1 vs 5/4) — the excess depends on join-view data absent
  from the actor's view, so no function of that view can cancel it.
  Witness: A at [pA0] vs A at [pA0, pB1].
- **T2 (cut-normalization is the lottery, reconvicted on the
  generated grammar).** The naive cut-transfer completion — normalize
  the enabled-event weights at each frontier by N(prefix) = Σ q — is
  GAUGE-DEPENDENT: on the A7 witness pair ([pA0, selfA, pB1] vs
  [pA0, pB1, selfA]; ONE canonical DAG, mu = 1/256 both) the
  cut-normalized products differ (1/2048 vs 1/2560, exact), because
  N jumps from 2 to 5/2 when the blind pair becomes visible. This is
  d34a-H5's census-denominator conviction reproduced exactly on the
  generated opportunity structure.
- **T3 (the discrete TS-condition; the front-5 ≡ front-9 bridge).**
  Define: a PLACEMENT COMPLETION is a cut-attached normalizer Z(cut)
  making the normalized transfer extension-invariant (equal over all
  linear extensions of every history — foliation-change invariance).
  T2 says Z ≡ N fails. The existence of a globally consistent Z is
  precisely the DISCRETE TOMONAGA-SCHWINGER INTEGRABILITY CONDITION
  for the record functional: per-pair the two-path constraint is
  solvable (underdetermined), and the global question is whether the
  ladder excess is a COBOUNDARY (the obstruction is a cocycle on the
  cut complex). IDENTIFICATION, PINNED: v6 paper 1's gravity-sector
  residue (TS-integrability of the interacting reconstruction) is the
  continuum shadow of exactly this condition — front 5's open core =
  front 9's open core. Status: the condition is DEFINED and its
  failure-for-naive-N gated; global existence OPEN (the honest
  successor of d34b), now with a precise cocycle formulation.
- **L1 (ratio locality, positive law).** What IS well-defined without
  completion: mu-ratios. Gate: (i) gauge-invariance (mu equal across
  linear extensions — inherited); (ii) RATIO LOCALITY — for history
  pairs (H1, H2) and a common admissible extension e whose past-view
  is identical in both, mu(H1+e)/mu(H2+e) = mu(H1)/mu(H2) exactly
  (the paper-28 ratios-only structure recovered as the invariant
  content of the weight system). Swept deterministically over the
  family.
- **L2 (obstruction additivity, positive law).** The per-actor excess
  (sum − 1) equals (#blind ckey groups)/4 with each blind group
  contributing EXACTLY 1/4, family-wide (the d42a delta verified this
  mechanically; here it becomes OUR gated law) — i.e. the obstruction
  functional is COMPONENT-ADDITIVE and quarter-quantized. This is the
  cocycle's local form; any admissible Z must integrate exactly this
  density.

## 2. Scope

The completion itself is NOT claimed. The program's standing
expectation (paper 29 / the identified-law audit) is that
normalization arrives at the LIFT: the decoherence functional's
diagonal supplies Born weights; the classical weight system supplies
ratios. d42b3 fixes what any classical completion must satisfy
(T1/T2/T3 constraints; L2 the density it must integrate) and what is
already invariant (L1). If the discrete TS-condition later FAILS
globally, the classical placement problem is UNSOLVABLE and the lift
is the only completion — that outcome would itself be a theorem-class
result (pre-registered here).

## 3. Gates (exit 1; exact)

G-T1 the identical-own-view witness (own-view canons equal; sums 1 vs
5/4) + the no-go sentence. G-T2 the cut-product witness on the A7
pair (1/2048 vs 1/2560 exact; same canonical DAG; N-values 2, 2, 2
vs 2, 2, 5/2). G-T3 the two-path Z-constraint exhibited and solved
per-pair (underdetermination shown: one equation, two unknowns);
the cocycle statement printed; global existence declared OPEN.
G-L1 ratio locality swept (deterministic triple selection over the
d42a family; zero violations). G-L2 excess = quarter-quantized blind
count, family-wide (both arms), zero violations.

## 4. Round-1 amendments (2026-07-18; round frozen at #302; the
## condition is DECIDED at depth 4)

**D1 (F1 — T3 re-posed and DECIDED; supersedes §1-T3's "OPEN").** A
placement completion, stated with the normalization clause: cut data
Z > 0 with the transfer q'(e|h) = q(e|h)·Z(h+e)/Z(h) required (a)
per-cut normalized (Σ q' = 1) and (b) foliation-invariant. TWO
CLASSES, both decided on the depth-4 complex (427 canonical classes,
202 diamonds): **(i) RATIO-PRESERVING (within-cut ratios untouched)
— REFUTED: Z = N is forced and 36 diamonds violate chain-consistency
(two bad components; G-T2's witness is one certificate). THEOREM.
(ii) GRADIENT (h-transform) — SOLVED at every finite depth:** the
backward recursion from a unit boundary gives Z(∅) = 64/1037,
positivity throughout, per-cut normalization at all 215 interior
histories, the A7 witness pair equalizing at 1/2074, with
313-parameter boundary freedom — **at the unavoidable cost of
WITHIN-CUT RATIO DEFORMATION at 21/114 interior cut classes, the
root included (16/133 vs 32/257); no boundary choice avoids it.**
Honest residues: infinite-volume positive-harmonic existence; whether
ratio deformation is physical given G-L1. Round-2 decidable target:
the actor-factored intermediate class. The v6 paper 1 identification
ATTACHES TO THE DECIDED STATEMENT: the continuum shadow of
"ratio-preserving TS fails / gradient TS holds at finite volume with
ratio deformation" is the reopening condition's discrete form.

**D2 (F2 — T2's diagnosis corrected, STRENGTHENING).** The printed
"N is NOT cut-attached data" was FALSE: N is constant on all 427
canonical classes (gated now). The true statement: N IS cut-attached
but NOT A DISCRETE GRADIENT — its chain-products are foliation-
dependent (it double-counts the blind layer along foliations that
expose it). T2 stands, generalized from one witness to the 36-diamond
census.

**D3 (F3 — T1 gains its positivity hypothesis).** The no-go as
worded was refuted by the degenerate ZERO-CLASS counterterm (the
own-view component filter: gauge-invariant, restores sums ≡ 1 — by
exactly L2's k·(1/4) — and kills ALL join arbitration). T1 holds for
SUPPORT-PRESERVING (strictly positive) counterterms — the nesting
argument (subset candidates, equal shared weights, positive extra
mass) now printed and gated. The zero class is declared excluded:
a completion that abolishes joint arbitration abolishes the physics
it was meant to normalize.

**D4 (F4 — the pre-registration corrected).** §2's dichotomy was too
strong. Corrected: ratio-preserving classical placement is
UNSOLVABLE (decided); classical completions EXIST but must deform
within-cut ratios (gradient class) or attach non-cut data; **the
LIFT is the only ratio-preserving normalized completion** — the
sharpened bridge to d42b4.

**D5 (the d42b1-delta hand-off: h12 as the third witness).** The
transport grammar's h12 (d42b1 #304: one dead component inflating a
live singleton's view-relative arb denominator; sum 23/24, off-
ladder; the admission-based arb-D fix flattens the anchored blind
spectra) is PINNED here as a completion constraint: any Z must
price dead-component inflation on the EXTENDED grammar too; the
general-depth ladder is FALSE under current pricing, so the
completion problem, not the pricing patch, owns the reconciliation.

**D6 (F5/F6/F7 declarations).** L1 is a THEOREM at depth <= 4 (all
same-branch factors constant; referee proof recorded); its empirical
content begins where factors vary — census demoted to tripwire with
the q-spectrum disclosure printed. L2's exact-1/4 quantization is
scoped to single-component join views (the d42a delta's
parenthetical); additivity (k >= 2) is d42a-delta-carried, untested
in this 2-actor family. The kernel is fixed to K1; PK1 == PK2 on
every ARM-1 component (max size 2) — immaterial, declared.
