# RSQ — JOINT ADJUDICATION (R1 #309, R2 #312, R3 #308)

**Adjudicator:** the coordinating agent.  **Inputs:** the three frozen
reviews (`review-rsq-operator.md` / `review-rsq-effectus.md` /
`review-rsq-instrument.md`), the frozen delivery (paper `f208ff12974b`,
code `18eb651d1ab1`, output `810f923392d8`, receipt `4db809f7b618`),
the frozen protocol (`note-rsq-hostile-protocol.md`).  **Standing:** all
three grades ACCEPT-WITH-FIXES; combined recomputation weight ~495
(R1 84 + R2 199 + R3 212); **zero numerical discrepancies, zero false
theorems, zero false numbers**.  The mathematics survived; the defects
are in what the verdict *names* and what the gates *protect*.

## 1. Resolved grade

**ACCEPT-WITH-FIXES**, unanimous — with the largest verdict-language
repair of the era: the EMPTY half gets **promoted** (census → theorem)
and the FOUND half gets **demoted** (found → found-only-at-unmotivated-
identifications).  Both movements are the reviews' measurements, not
taste.

## 2. The two verdict movements (the panel's core)

**A. The EMPTY half is a THEOREM, not a census** (R1 decisive; R2
corroborating; R3-F3 complaining from the instrument side).
- R1 proved the 20,160-row sweep analytically: the readout profiles
  (0,0,0,0,0,1) and (0,0,0,1,1,2) kill all branches **at every prime
  ≥ 5**; extended to 50,400 rows, still zero.
- R2, independently and beyond scope: **0 of 172,800 rows over all 60
  primes 5..293**; 0 at d=2 (exhaustive) and d=4 (sampled); route A's
  structural premise verified exhaustively (every elementary abelian
  p-subgroup of G_C is cyclic).
- R3-F3's complaint — `UNIVERSAL-FOR-THIS-FAMILY` is "an alias for zero
  criterion hits" — is thereby *resolved by promotion*: after repair the
  name denotes a proved statement with two independent census
  corroborations.  R3-F10's observation that the build-cap's excluded
  primes are decidable by the criterion folds into the same theorem.
- **The master equation** (R1-K1): I − E = α⁻¹ρα, with the three walls
  as readings of ρ — LCB's fixed-point mismatch (ρ invertible), the
  order form (ρ^ord = I), the permutation-module form (ρ = ρ_V(π)).
  The module obstruction is **genuinely new**: it passes LCB's precheck
  AND satisfies the order criterion, arena-free and transport-free —
  the measured independence enters the paper.
- R2's sufficiency check: the criterion is **sufficient** at L₆/p=7/
  ord 3 for every diagonal pattern — one gate from an iff at measured
  scope.

**B. The FOUND half rests on unmotivated identifications** (R2-F-3,
the panel's highest-weighted finding).  The two S₃-equivariant cells
**and HA's own `sym_index`** are **6 of 6 stillborn at all 7 primes**;
every precheck survivor is one of the 1,434 arbitrary relabellings —
selected by the property under test.  Restricted to the pin's motivated
family, the unit's own `derive_verdict` returns
`RSQ-NO-COMPATIBLE-SQUARE`.  Pin-legal; never stated.  Adjacent: the
"held-out verification" contains **no fitting** — H1 and H2 are the
same boolean (R1-F5), and the 43-label control is an algebraic identity
(Ẽ ≡ I−ρ by definition; R2).  The control earns **rung 2** (EMPTY is
not an arena/prime artefact; the machinery detects synthetic bridges)
and not rung 3 (no out-of-sample content).  R3-F5: G19 measures a
cardinality inequality, not the claimed containment.

## 3. Instrument findings (cross-confirmed)

- **Sources are two, not three** (R3-F1 ∥ R2-F-1 ∥ R1): G35's source 1
  *is* `order_criterion` (`src1 = live_full`, code:3418/2731); the 315
  census rows reduce to 126 distinct rows inside source 2's sweep.
  §13 #234 violated; no mutant separates them.  After repair the
  genuinely independent second route exists: R1's readout-profile
  theorem.
- **Forced clauses as gates** (R2-F-2, R3-F11, #208): "0 of 315
  injective" is forced twice over (the criterion + cardinality
  p⁶ > |G_C|); source 3's universality is analytic.  Disclosures, not
  must-passes.
- **Typed functoriality** (R2-F-4): `census_empty_at_this_base: True`
  is a literal G28 never reads.  The true statement — base-independence
  by construction — is better and must be computed.
- **Gate coverage** (R3-F2, R3-F4, R3-F6, R3-F8, R3-F9, R3-F12): no
  cell-completeness gate on the three verdict-carrying censuses
  (engraved rule; recurrence-lite); G20's route-independence is a
  self-report defeated by a silent exception; the precheck's negative
  control is the object under audit; five declared mutants die to a
  carrier assert, not their gates; 13 of 57 mutants never reach the
  totals block; G15 gates the census-cell count only as `>= 8`.
- **Provenance minors** (R3-F7): "four declared instances" is four rows
  from two instances.

## 4. What survived every attack

The order obstruction re-derived step by step (R2); the full delivery
byte-identical for all three reviewers; 57/57 mutants dead and
reproduced; the HA d=3 construct with G29 verbatim (R_HH = translation
by ρ mod p); the p=7 spectral meeting on the stillborn cell — praised
by R2 as "the paper's best moment and the corpus's model"; the grown
43-label arena reaching the criterion natively; the stillborn-precheck
architecture itself.

## 5. THE SCALE-CONVERGENCE THESIS: struck, owned

R2's assigned-question verdict: **narrative**.  LCB explicitly refused
the same inference at its own scope; 43 = 6p+1 is definitional, not
emergent; TB3's torsion is a group-level fact, not a growth result; and
RSQ's own arena-free module obstruction *refutes* the thesis's
direction.  "Four sentences carry it further than the measurements."
The thesis was **adjudicator-introduced framing** (my ledger language
and status messaging around #304–#306; it never reached STATUS.md), the
fourth instance of coordinator narrative outrunning measurement (#241,
#267, the exclusive-Fano visit, now this).  **Retired at this
adjudication; the record keeps only the measured scale table** (prime
derivable at 16 labels *arena-coupled, inference refused by LCB*;
43-label control at rung 2; torsion at 3 wings a group-level fact).
Owned in the ledger entry accompanying this note; the RSQ terminal
STATUS row will carry the measured table, not the thesis.

## 6. Binding repair orders (R-RSQ-1 … R-RSQ-10)

1. **Split and rename the verdict, both halves computed** (#257):
   EMPTY half → the theorem name (readout-profile proof verified
   in-unit, gated, with the 20,160/50,400/172,800 censuses printed as
   corroboration and the excluded-primes clause folded in); FOUND half
   → carries the computed qualifier naming the identification class,
   with the motivated-family census (S₃-equivariant cells + `sym_index`,
   6/6 stillborn at all 7 primes) printed and gated, and
   `derive_verdict`'s motivated-family return
   (`RSQ-NO-COMPATIBLE-SQUARE`) stated in the paper.
2. **The master equation enters the paper** as the unifying statement,
   with the three walls as readings and the measured independence of
   the module obstruction (passes LCB precheck ∧ satisfies order
   criterion ∧ still dies).
3. **Sufficiency gate** (R2): verify criterion-sufficiency at L₆/p=7/
   ord 3 across all diagonal patterns in-unit; state the iff at its
   measured scope.
4. **Demote the held-out language** (R1-F5): H1 ≡ H2 disclosed; the
   43-label control restated at rung 2 (reachability + synthetic
   detectability); "held-out"/"out-of-sample" struck; G19 restated as
   the cardinality fact it measures (R3-F5).
5. **Two sources, honestly** (R3-F1): G35 recounted; the independent
   second route is the profile theorem; #234 satisfied by construction
   thereafter.
6. **Forced clauses reclassified** (#208): R2-F-2, R3-F11 → disclosures.
7. **Functoriality computed** (R2-F-4): base-independence measured or
   derived in-code, the literal removed.
8. **Gate repairs** (R3): cell-completeness on all three verdict-
   carrying censuses; G20 exception-hardened; an independent negative
   control for the precheck; the five carrier-assert mutants given
   dying gates; the 13 short-circuiting mutants routed through totals;
   G15's bound tightened to equality.
9. **Provenance fixes** (R3-F7): rows vs instances corrected.
10. **STATUS rewrite** per §5: the thesis struck, the measured table in.

## 7. RUNBOOK engraving (this adjudication)

- **§13 addendum (precheck doctrine):** *Stillborn-precheck-before-
  census* is standing doctrine for census units.  **A precheck-level
  quantity may gate which candidates are censused, but may never by
  itself name the verdict** (R2's amendment, verbatim).  Verdict-naming
  facts must be measured on the censused objects.

## 8. What the continuum rung inherits from RSQ (consolidated)

R2's successor requirements S-1..S-5, headlined by **the spectral
carry**: drop the thresholds table; carry the order obstruction
spectrally.  HA's readout carries eigenvalue 1 at every dimension, so
**0 ∈ spec(I−E) lies on no unit circle** — the obstruction against
unitary-compatible bridges is dimension-independent in proof form, and
the continuum rung inherits a *theorem*, not a census.  Together with
the master equation this is the bridge line's complete bequest: one
equation, three walls as readings, one spectral invariant that scales.
