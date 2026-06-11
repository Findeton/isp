# Paper 24 (v6) - SHARD: Continuum Consolidation

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
Tier 3a: the two mathematical residues, advanced to their sharpest
form.  (C-reg-b) is POSED WITH A VALIDATED DETECTOR: the local Weyl
remainder r_t(x) = K_t(x,x) sqrt(4 pi c t) - 1 separates the three
strata at machine level - SMOOTH limits decay linearly in t (ratios
1.89/1.94/1.96), INTERFACE limits fail O(1) exactly AT the seam
(sup pinned at 0.333 while away-values decay), MICROSTRUCTURE limits
fail O(1) globally between scales (pinned at 0.27) - so the
regularity-stratum question is now a precise classical heat-kernel
statement: detector decay <=> smoothness, with rates.  (PR-RP) is
reduced and evidenced: RP forces real-spectrum diagonals (the clock
mechanism - the only known obstruction to sealability - is EXCLUDED
from the RP class; 12/12 samples PSD at -1.5e-17), and Anderson's
dominant-pole condition holds in 12/12 sampled RP processes: the
conjecture (PR-RP+) - record positivity ~ sealability - stands in its
sharpest form with no known counterexample mechanism.  Neither residue
is CLOSED; both are now precise, classical, and bounded
```

## 0. Verdict

```text
(C-reg-b) (p24a): the detector
    r_t(x) = K_t(x,x) sqrt(4 pi c(x) t) - 1
  separates the strata:
    smooth:         sup |r_t| = 0.088 -> 0.012, ratios ~2 per halving
                    of t (LINEAR decay - the regularity signature);
    interface:      sup pinned at 0.3334 AT the seam, decaying away
                    from it (the failure LOCATES the singular locus);
    microstructure: 0.27, t-independent between the micro and macro
                    scales (the homogenized stratum announces itself
                    globally).
  (C-reg-b) RESTATED: a controlled limit lies in the regularity
  stratum iff sup_x |r_t| -> 0 along the tower.  The equivalence-with-
  rates theorem is the named residue - classical heat-kernel analysis,
  no longer an open-ended question.

(PR-RP) (p24b): the reduction - RP => Hamburger diagonal (P8 typed
  theorem; machine: 12/12 reversible samples PSD at -1.5e-17, the P16
  clock fails at -9.96e-3) - EXCLUDES the only known non-realizability
  mechanism from the RP class; the dominant-pole evidence (12/12
  samples real, positive, strictly dominant) places generic RP
  processes inside Anderson's sufficient condition.  CONJECTURE
  (PR-RP+): RP + finite record rank => finite record law (capacity may
  exceed rank).  If true: record positivity ~ sealability.  Residue:
  the multi-letter Anderson theorem (classical positive-systems
  theory, named).

The continuum DR category statement (P18's residue) remains untouched
here - it rides on (C-reg-b)'s machinery and is listed, not advanced.
```

## 1. Method and reproducibility

```text
code/v6_p24a_regularity_detector_campaign.py  the (C-reg-b) detector
code/v6_p24b_prrp_evidence_campaign.py        the (PR-RP) reduction
```

Both scripts rerun bit-identically.  Named imports: local heat-kernel
asymptotics (Weyl; Minakshisundaram-Pleijel) as the detector's
classical frame; Anderson's dominant-pole realizability (the (PR-RP)
outlook).  Corpus inputs: P12's synthetic stratum and P15's
hypothesis-line finding (the detector operationalizes P15 Section 6's
"computable boundary value"); P8's typed moment theorems and P16's
clock (the (PR-RP) reduction).

## 2. The (C-reg-b) detector

### 2.1 Definition and rationale

For the record operator -d(c d.) on the circle in L^2(dx), the local
heat-kernel asymptotic is K_t(x, x) ~ 1/sqrt(4 pi c(x) t) as t -> 0
when c is smooth - the leading local Weyl term, with the first
correction O(t) carrying derivative information.  Define the LOCAL
WEYL REMAINDER

```text
   r_t(x) = K_t(x, x) sqrt(4 pi c(x) t) - 1.
```

The detector criterion: a controlled tower limit lies in the
REGULARITY STRATUM iff sup_x |r_t| -> 0 as t -> 0 along the tower.
Rationale: smoothness of the limit metric is exactly what makes the
local parametrix expansion valid uniformly; interfaces break it at a
point, microstructure breaks it at all points between the micro and
macro scales.

### 2.2 Receipts (n = 512, exact eigendecompositions)

```text
(i) smooth class (c = 1 + 0.5 sin 2 pi x):
   t = 0.0200: sup |r_t| = 0.08845
   t = 0.0100: 0.04669      t = 0.0050: 0.02404
   t = 0.0025: 0.01228
   ratios per halving: 1.89, 1.94, 1.96  [linear in t: 2.00]
(ii) interface class (c: 1 -> 4 step):
   sup |r_t| pinned at 0.3334 across the same t-range, WHILE the
   away-from-seam values decay (0.351 -> 0.124): the failure is O(1)
   and LOCALIZED at the seam - the detector finds the singular locus.
(iii) microstructure class (c = 1 + 0.45 sin(64 pi x)):
   sup |r_t| = 0.271 -> 0.278, t-INDEPENDENT between the micro scale
   (t ~ 1e-3) and the macro scale: global failure - the metric the
   detector tests is not the one the tower converges to (the
   homogenized stratum announces itself).
```

### 2.3 The restatement of (C-reg-b)

The three-strata separation validates the criterion at machine level
and converts (C-reg-b) from an open-ended question into a PRECISE
classical statement:

```text
   (C-reg-b, detector form): for controlled towers, sup_x |r_t| -> 0
   (with rate t^1) along the tower  <=>  the limit is a smooth
   geometry; localized O(1) persistence <=> interface stratum; global
   t-independent persistence <=> microstructured/homogenized stratum.
```

One direction (smooth => linear decay) is classical parametrix
calculus and is the provable half with P15's lemma machinery; the
converse (decay => smoothness) is heat-kernel rigidity - the genuine
residue, now a named theorem target with the expected refinement that
decay RATES grade Holder classes rather than a smooth/non-smooth
binary.

## 3. The (PR-RP) reduction and evidence

### 3.1 The reduction

By P8's typed moment theorem, reflection positivity forces the
diagonal sequence p(1^n) into the Hamburger moment class - REAL
spectrum.  The only proven obstruction to finite positive realization
(P16's Theorem B) requires irrational oscillation ON the decay circle
- complex peripheral spectrum.  Hence THE CLOCK MECHANISM IS EXCLUDED
FROM THE RP CLASS: any counterexample to (PR-RP+) must fail positivity
at word level while keeping a real-spectrum diagonal - no such object
is known, and the corpus' own moment receipts patrol the boundary.

Machine: 12/12 sampled reversible hidden-chain processes (the RP
class's generic members) have PSD diagonal Hankels (min eigenvalue
-1.5e-17); the clock fails at -9.96e-3 - the reduction, checked on
both sides.

### 3.2 The dominant-pole evidence

Anderson's theorem (named import): a rational impulse response with a
unique dominant real positive pole admits a finite positive
realization, possibly at higher dimension.  Machine: 12/12 sampled RP
processes have letter-transfer spectra with a real, positive, STRICTLY
dominant eigenvalue - the generic RP process sits inside Anderson's
sufficient condition for its diagonal channel.  What remains open is
the MULTI-LETTER joint realization (one cone invariant under all
letter maps simultaneously) - classical positive-systems theory,
named.

### 3.3 The conjecture, sharpest form

```text
(PR-RP+): reflection positivity + finite record rank => finite record
   law, with capacity possibly exceeding rank.
Status: OPEN.  Known: the only proven obstruction mechanism is
   excluded from the class (3.1); generic members satisfy the
   dominant-pole condition (3.2); no RP finite-rank non-realizable
   process is known.  If true: record positivity ~ sealability at
   process level - the arrow of record formation and the existence of
   a finite ledger would be one condition.  The identified attack
   lanes (recorded for the campaign that takes this up): the
   composite-letter clock (a counterexample strategy: letter products
   with complex spectrum at block scale) versus the block-moment
   theorem (a proof strategy: RP palindromic Grams forcing moment
   class at every composite scale).
```

## 4. What this paper proves and does not prove

Proves/validates: the three-strata separation by the detector at
machine level (with the smooth-class linear rate); the RP exclusion of
the clock mechanism (typed-theorem reduction, machine-checked both
sides); the generic dominant-pole property of sampled RP processes.

Does not prove: the detector-smoothness equivalence theorem (named,
classical, with the graded-rates refinement expected); (PR-RP+)
(conjecture, sharpest form stated with both attack lanes); the
continuum DR category statement (listed).

## 5. The kernel after Paper 24

```text
(C-reg-b): posed with validated detector; residue = the equivalence
  theorem with rates (heat-kernel analysis).
(PR-RP):   reduced + evidenced; residue = multi-letter Anderson.
Candidacy framing: SM-side results remain conditional on these two,
  with both now PRECISE and classical - the conditional is bounded,
  not open-ended.
```

## References and literature map

- Papers 8, 12, 15, 16 (internal): the typed moment theorems, the
  synthetic stratum, the theorem's hypothesis line, the clock.
- H. Weyl (1911); S. Minakshisundaram and A. Pleijel (1949): local
  heat-kernel asymptotics (the detector's classical frame).
- B. D. O. Anderson et al. (1996-99); L. Benvenuti and L. Farina
  (2004): positive realization theory (the (PR-RP) frame).
```
