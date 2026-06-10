# Paper 24 (v6) - SHARD: Continuum Consolidation

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

## 2. What this paper proves and does not prove

Proves/validates: the three-strata separation by the detector at
machine level (with the smooth-class linear rate); the RP exclusion of
the clock mechanism (typed-theorem reduction, machine-checked both
sides); the generic dominant-pole property of sampled RP processes.

Does not prove: the detector-smoothness equivalence theorem (named,
classical); (PR-RP+) (conjecture, sharpest form stated); the continuum
DR category statement (listed).

## 3. The kernel after Paper 24

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
