# Paper 27 (v6) - SHARD: Three Walls - (PR-RP+), (F-fiber), and the Graded Detector

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
The three-track campaign ordered by ripeness x payoff.  PART I runs
the (PR-RP+) collision and the proof lane wins at every reachable
scope: the OS representation turns every block operator into a product
of PSD matrices, which PROVES the block-moment theorem through block
length 4 (Theorem PR2: real spectrum, machine-verified at 0.0e+00);
lengths 5-6 are empirically real (the Hillar-Johnson phenomenon);
rotations first appear at length 8 - and there the VALIDITY WALL
stops them: among deeply valid RP-form processes the best complex
subordination collapses from an apparent 1.000000 to 0.205, with
every s = 1 impostor dissected by the exact mechanism (a pure top
rotation has no Perron weight, so its diagonal must go negative -
caught by the sound eigen-residue filter).  Refined conjecture
(PR-RP++): bond-RP peripheral block spectra are rho x roots of unity.
PART II DISCHARGES (F-fiber) into the weaker premise (R-id): the copy
rotation commutes with the unbroken ledger EXACTLY iff the copies are
identical (0.0e+00 vs linear breaking), family-breaking seams are
covariant fiber data whose records are invariants only (Jarlskog and
masses invariant to 1e-15 while Yukawa entries move freely - the
record-native reason CKM is physical and Yukawa bases are not), and
the chain recorded-replication => fiber => U(g) gauge => g >= 3 =>
nu_R closes: THE NEUTRINO PREDICTION NOW RIDES ON (R-id) + OBSERVED
REPLICATION + CORPUS THEOREMS ALONE.  PART III delivers the graded
detector law for (C-reg-b): decay exponents GRADE the Holder class -
measured 0.243 / 0.465 / 0.706 / 0.956 against predicted
min(1, alpha/2) = 0.25 / 0.50 / 0.75 / 1.00 - and the smooth anchor's
first heat coefficient is measured (leading -1/4 c'', metric-
independent to 1e-3).  Three walls, three honest outcomes: a theorem
plus a measured wall, a discharge, and a graded law
```

This paper executes the post-review priority stack in its corrected
geometry: the (PR-RP+) flagship with the two-lane collision design,
the (F-fiber) derivation in parallel (cheap, theorem-shaped, carrying
the prediction upgrade), and the (C-reg-b) background track advanced
to its graded form.

## 0. Verdict

```text
PART I ((PR-RP+); p27a).
  THE RP-FORM (Prop. 1.1): bond-RP stationary processes are exactly
  those with p(w) = <Omega| A_{x_1} ... A_{x_n} |Omega>, A_x PSD
  summing to the transfer T, T Omega = Omega - a POVM-type QUANTUM
  ledger.  (PR-RP+) becomes: is every valid finite-rank quantum
  record process classically sealable?
  THEOREM PR2 (proved): every block operator is similar to a product
  of PSD matrices; cyclic two-factor reduction gives REAL nonnegative
  spectrum for ALL blocks of length <= 4 - the clock mechanism is
  excluded through block scale 4.  Receipt: max |Im lambda| = 0.0e+00
  over 400 random PSD pairs x every binary block of lengths 2-4.
  THE REALITY MAP (empirical): lengths 5-6 real across the search
  (Hillar-Johnson positivity, named anchor); first rotation at length
  7 (marginal, 2e-5) and length 8 (robust, 0.255; cyclic run pattern
  (3,3,1,1)).
  THE VALIDITY WALL (the collision outcome): 2500 sampled RP-form
  processes; 2241 pass the shallow word scan; 1882 pass the SOUND
  deep-diagonal filter (every 4-run length-8 block, p(W^n) >= 0 to
  block depth 4000 via eigen-residues).  Best complex subordination
  among survivors: s = |lambda_c|/rho = 0.205.  Every apparent s = 1
  candidate FAILS the deep filter by the exact predicted mechanism:
  pure top rotation (no Perron weight at the radius), fitted
  positivity margin a - |b| = -1.35: not a process.
  REFINED CONJECTURE (PR-RP++): for valid bond-RP processes every
  block operator's peripheral spectrum is rho x (roots of unity).
  Status: THEOREM to block length 4; measured wall at length 8;
  multi-letter Anderson assembly = the named residue.

PART II ((F-fiber) discharged; p27b).
  THEOREM F1 (recorded replication is fiber replication): if g copies
  of a matter ledger are EXACTLY identical at the unbroken level
  (premise (R-id)), the copy label is gauge - receipt: the commutator
  ||[U x 1, H]|| = 0.0e+00 exactly at delta = 0 and grows linearly in
  the detuning (ratios 1.45/1.33) - and any RECORDED replication
  (copies counted, compared, mixed) carries inter-copy seams, which
  are covariant data on the fiber.  Silent-seam exclusion (P4) rules
  out the only alternative (absolutely silent copies are unrecordable
  - not a physics alternative; and empirically false: the copies are
  seen).
  THE OBSERVABLE SIGNATURE: records = family invariants ONLY:
  Jarlskog |dJ|/|J| = 3.7e-15 and masses 1.3e-15 invariant under
  random family rotations while Yukawa entries move by O(1): CKM is
  physical, Yukawa bases are not - because two seams break ONE fiber
  incompatibly.
  THE UPGRADE: (F-fiber) -> (R-id).  The chain recorded replication
  => seams => transport => fiber => U(g) gauge (P18) => protected iff
  g >= 3 (P21 G1) => nu_R forced with the unique embedding (P21 G2)
  now carries only (R-id) as premise: P-nu rides on (R-id) + observed
  replication + theorems.

PART III ((C-reg-b) graded; p27c).
  THE GRADED DETECTOR LAW: sup_x |r_t| ~ t^min(1, alpha/2) for
  C^(0,alpha) record metrics - measured exponents 0.243, 0.465,
  0.706, 0.956 for alpha = 0.5, 1.0, 1.5, smooth, against predictions
  0.25, 0.50, 0.75, 1.00: THE DETECTOR GRADES THE REGULARITY STRATUM.
  The smooth anchor: r_t = t a_1(x) + O(t^2) with a_1 in
  span{c'', (c')^2/c}, leading coefficient -1/4 metric-independent to
  1e-3 (the record operator's first heat coefficient, measured).
  (C-reg-b) acquires its "with rates" structure; the rigidity
  converse (exponent => class) is the named residue in its evidenced
  graded form (C-reg-b').
```

## 1. Method and reproducibility

```text
code/v6_p27a_prrp_collision_campaign.py   Part I
code/v6_p27b_ffiber_campaign.py           Part II
code/v6_p27c_graded_detector_campaign.py  Part III
```

All three scripts rerun bit-identically (fixed seeds; search scopes
printed in place).  Named imports: the OS reconstruction for
reversible/RP processes (Klein-Landau; P10's theorem at corpus scope);
the spectral reality of products of two PSD matrices (classical); the
Hillar-Johnson positivity phenomenon for words in two positive
definite letters (the empirical anchor of the reality map); P16's
Theorem B (the corpus' own, used as the obstruction engine); local
heat-kernel asymptotics (the Part III frame).  Corpus inputs: P4
silent-seam, P8 typed moment theorems, P16 clock/cone, P18 R2/R3,
P21 G1/G2, P24's detector.

## 2. Part I: the (PR-RP+) collision

### 2.1 The RP-form: bond-RP processes are quantum ledgers

**Proposition 1.1 (the RP-form).**  A stationary binary process $p$ is
bond-reflection-positive with self-adjoint positive transfer iff it
admits the representation

$$
p(x_1 \dots x_n) \;=\; \langle \Omega \,|\, A_{x_1} A_{x_2} \cdots
A_{x_n} \,|\, \Omega\rangle ,
\qquad A_x \succeq 0,\quad A_0 + A_1 = T,\quad T\Omega = \Omega,
\quad 0 \preceq T \preceq \mathbb 1 .
$$

*Proof sketch.*  ($\Leftarrow$) The reflected Gram is
$G[u,v] = p(\bar u \circ v) = \langle A_{u_1}\cdots A_{u_k}\Omega,\,
A_{v_1}\cdots A_{v_l}\Omega\rangle \succeq 0$ since the $A_x$ are
self-adjoint.  Consistency: $\sum_x p(wx) = \langle\Omega, A_w T\Omega
\rangle = p(w)$, and stationarity likewise via $T\Omega = \Omega$.
($\Rightarrow$) The OS construction (Klein-Landau; P10): the GNS space
of the reflected form carries the positive self-adjoint transfer $T$
and the symbol multiplications $E_x \succeq 0$ with $\sum_x E_x =
\mathbb 1$; setting $A_x = T^{1/2} E_x T^{1/2}$ and using $T^{-1/2}
\Omega = \Omega$ on the invariant vector gives the display.  $\square$

The reading changes the question's character: the $A_x$ are a
POVM-type structure - **bond-RP processes are exactly the finite-rank
QUANTUM record ledgers**, and (PR-RP+) asks whether every valid
quantum record process is classically sealable (admits a finite
Heller cone, P16).

### 2.2 Theorem PR2: the block-moment theorem to length 4

**Theorem PR2.**  For any RP-form process, every block operator
$A_W = A_{x_1}\cdots A_{x_k}$ with $|W| \le 4$ (binary alphabet) has
real nonnegative spectrum; consequently every block diagonal
$p(W^n)$, $|W|\le 4$, is a Hamburger moment sequence, and the clock
obstruction (P16 Theorem B) cannot operate at block scales $\le 4$.

*Proof.*  The spectrum of a product of two PSD matrices is real and
nonnegative ($\mathrm{spec}(AB) = \mathrm{spec}(A^{1/2}BA^{1/2})$ for
$A \succ 0$, extended to $A \succeq 0$ by continuity), and spectra are
invariant under cyclic rotation of the product.  Over a binary
alphabet, every word of length $\le 4$ is cyclically equivalent to a
grouped product of at most two PSD factors:

$$
\underbrace{A_0^a A_1^b}_{2\ \text{runs}},\qquad
A_0 A_1 A_0 \sim A_0^2 A_1,\qquad
(A_0A_1)^2 \;\Rightarrow\; \mathrm{spec} = \mathrm{spec}(A_0A_1)^2
\subset \mathbb R_{\ge 0},
$$

covering all run patterns of lengths 1-4 (1, 2, and 3 runs reduce by
cyclic merging; the only 4-run length-4 word is $0101 = (A_0A_1)^2$).
$\square$

Receipt: $\max|\mathrm{Im}\,\lambda| = 0.0\mathrm{e}{+00}$ across 400
random PSD pairs $\times$ every binary block of lengths 2-4.

### 2.3 The reality map and the relocation

Beyond the theorem's reach, the machine maps where products of two PSD
letters can rotate:

```text
   L     max |Im lambda| / |lambda|_max     first witness
   5         0.00000                        (empirically real)
   6         0.00000                        (empirically real)
   7         0.00002                        0100111  (marginal)
   8         0.25547                        00011101 (robust;
                                            cyclic runs (3,3,1,1))
```

Lengths 5-6 are real across the search - beyond PR2's reach; this is
the Hillar-Johnson positivity phenomenon for words in two positive
definite letters (named anchor).  The collision therefore relocates to
length-8 blocks with four cyclic runs.

### 2.4 The validity wall

The counterexample lane needs a VALID process (all $p(w) \ge 0$)
whose length-8 block diagonal oscillates irrationally on its decay
circle.  The search: 2500 RP-form samples; shallow word scan to
length 12; then the SOUND deep filter - for every 4-run length-8
block $W$, the diagonal

$$
p(W^n) \;=\; \sum_k c_k \lambda_k^n
\qquad (\text{eigen-residues of } A_W)
$$

is evaluated to block depth 4000 and required nonnegative.  Results:

```text
   2241 / 2500 pass the shallow scan; 1882 pass the deep filter.
   best complex subordination among survivors:
        s = |lambda_c| / rho = 0.205
   every apparent s = 1.000000 candidate FAILS the deep filter.
```

The impostor dissection (the mechanism receipt): a shallow-valid
sample with $s = 1$ has block spectrum
$\{\,1.000\,e^{\pm 0.1511 i},\ 0.536,\dots\}$ - a PURE top rotation
with **no Perron weight at the radius**.  Its diagonal fit
$a + b\cos(n\theta + c)$ returns $a = 0.0003$, $|b| = 1.35$:
positivity margin $a - |b| = -1.35 < 0$ - the diagonal must go
negative, and the deep filter catches it.  Validity-at-depth is
EXACTLY the enforcer that Theorem B's positivity argument predicts:
a rotation can only reach the top by abandoning the Perron weight
that positivity requires.

### 2.5 The collision outcome and (PR-RP++)

```text
LANE A (composite clock): stopped by the validity wall at every
   tested scope (s <= 0.205 among genuine processes; impostors
   dissected by mechanism).
LANE B (block-moment theorem): THEOREM to block length 4 (PR2);
   empirical reality at 5-6; the wall at 8.
REFINED CONJECTURE (PR-RP++): for valid bond-RP processes, every
   block operator's peripheral spectrum is rho x (roots of unity) -
   no clock mechanism at any scale.  Proved to length 4; measured
   beyond; if true, the only remaining gap to (PR-RP+) is the
   multi-letter Anderson assembly (classical positive-systems
   theory, named residue).
```

Honest scope: the wall is MEASURED (search scopes printed), not
proved; the quantum-ledger reading of Prop. 1.1 means a (PR-RP+)
failure would have said "quantum record processes exceed classical
ones even under reflection positivity" - the search found validity
policing that boundary instead.

## 3. Part II: (F-fiber) discharged into (R-id)

### 3.1 Theorem F1 and its proof

**Theorem F1 (recorded replication is fiber replication).**  Let a
matter sector consist of $g$ copies of one ledger, exactly identical
at the unbroken level (premise (R-id)), whose replication is RECORDED
(the copies are counted, compared, or mixed in sealed records).  Then
the multiplicity index is a degeneracy fiber: the copy label is gauge,
the family group $U(g)$ is reconstructed (P18 R3b), and the breaking
seams are covariant fiber data.

*Proof.*  (a) (R-id) means the unbroken ledger commutes with every
copy rotation: $[\,U \otimes \mathbb 1,\ H\,] = 0$ for all
$U \in U(g)$ - the copy label carries no invariant content: it is
gauge, and the multiplicity is a degeneracy fiber in the sense of P18.
(b) Recorded replication requires sealed words whose probabilities
depend on relative copy structure; such words are inter-copy SEAMS -
operators off-diagonal in the index - and seams are precisely
transport data on the fiber.  (c) The only alternative - copies with
NO seams ever - makes every relative copy datum silent for all time:
by P4's silent-seam exclusion such a label is not record data, and a
replication that is nowhere recorded is not an observed replication
(empirically: the three generations ARE compared and mixed - masses
and CKM are records).  Hence the recorded case is the fiber case.
$\square$

### 3.2 Receipts

```text
(i) the gauge condition = (R-id), machine-sharp:
   H(delta) = diag(H_base, H_base + delta V):
   delta = 0.00:  max ||[U x 1, H]|| = 0.000e+00   (EXACT symmetry)
   delta = 0.05:  7.27e-2   (ratio/delta = 1.45)
   delta = 0.20:  2.66e-1   (ratio/delta = 1.33)
(ii) records = family invariants only (3 copies, two breaking seams):
   under random family rotations (V_Q, V_u, V_d):
   |dJ|/|J| = 3.7e-15 (Jarlskog INVARIANT); masses 1.3e-15
   (INVARIANT); Yukawa entries move by O(1) (gauge data, not records)
```

Receipt (ii) is the theorem's phenomenological face: MIXING MATRICES
EXIST because two seams ($Y_u$, $Y_d$) break ONE fiber incompatibly -
the misalignment invariants (the CKM class, e.g. the Jarlskog
determinant $J = \mathrm{Im}\,\det[Y_uY_u^\dagger,\ Y_dY_d^\dagger]$)
are the records; the bases are not.  The record ontology thus explains
WHY a CKM matrix is physical while Yukawa entries are convention.

### 3.3 The upgrade

```text
recorded replication => inter-copy seams         [F1(b)]
  => transport on the index => DEGENERACY FIBER  [F1(a,c)]
  => U(g) family gauge                           [P18 R3(b)]
  => protected iff g >= 3                        [P21 G1]
  => anomaly-free iff nu_R exists, unique
     embedding (Q, L | u^c, d^c, e^c, nu^c)      [P21 G2]
```

(F-fiber) - formerly a free-standing hypothesis - is DISCHARGED into
the far weaker (R-id): "the copies are exactly identical at the
unbroken level," which is simultaneously the gauge condition of
receipt (i) and the standard reading of universality of gauge
couplings across generations (tested physics).  The prediction P-nu
(the right-handed neutrino exists) now rides on (R-id) + observed
replication + corpus theorems alone - the largest single upgrade
available to the Paper 25 ledger, executed.

## 4. Part III: the graded detector law

### 4.1 The smooth anchor: the first heat coefficient

For the record operator $-\partial(c\,\partial)$ on the circle, the
detector of P24 is

$$
r_t(x) \;=\; K_t(x,x)\,\sqrt{4\pi c(x)\, t}\; -\; 1
\;=\; t\, a_1(x) + O(t^2) \qquad (c \text{ smooth}),
$$

with the coefficient field $a_1$ a local curvature-type invariant.
Machine extraction (Richardson in $t$, two independent metrics, fit to
the complete two-term basis):

$$
a_1(x) \;=\; \alpha\, c''(x) \;+\; \beta\, \frac{c'(x)^2}{c(x)},
\qquad \alpha = -0.2482 / -0.2495\ (\approx -\tfrac14),\quad
\beta \approx 0.08\text{-}0.10\ (\text{extraction-limited}).
$$

The leading coefficient $-\tfrac14$ is metric-independent to
$\sim 10^{-3}$; the subleading one is bounded but not pinned (the
$t \to 0$ and $h \to 0$ limits compete).  The closed form is classical
parametrix calculus - the bookkeeping residue; the corpus content is
the measured universality.

### 4.2 The graded law

For Holder-class metrics $c \in C^{0,\alpha}$ (a kink of exponent
$\alpha$: $c_\alpha = 1 + \tfrac12|\sin \pi x|^\alpha$), diffusion at
time $t$ sees the metric at resolution $\sqrt t$, so the local Weyl
remainder should scale as $(\sqrt t)^{\alpha}$ until the smooth rate
$t^1$ saturates it:

$$
\sup_x |r_t| \;\sim\; t^{\min(1,\ \alpha/2)} .
$$

```text
   class                  fitted exponent     predicted min(1, a/2)
   C^0,1/2 (a = 0.5)          0.243                0.25
   C^0,1   (a = 1.0)          0.465                0.50
   C^1,1/2 (a = 1.5)          0.706                0.75
   smooth                     0.956                1.00
```

**The graded detector law (C-reg-b'):** the decay exponent of the
local Weyl remainder MEASURES the Holder class of the limit metric,
saturating at the smooth linear rate with the Section 4.1 coefficient
field.  (C-reg-b) thereby acquires its "with rates" structure: the
detector does not merely separate smooth from singular (P24) - it
GRADES the regularity stratum.  The rigidity converse (exponent
$\Rightarrow$ class) is the named residue, now in its evidenced
graded form.

## 5. What this paper proves and does not prove

Proves: Proposition 1.1 (the RP-form, with the quantum-ledger
reading); Theorem PR2 (block-moment to length 4, with its cyclic
reduction proof and 0.0e+00 receipts); Theorem F1 (with the
silent-seam step and both machine receipts); the graded exponent
measurements at four regularity classes with the predicted law; the
leading heat coefficient $-1/4$ at measured universality.

Establishes empirically, at stated search scopes: the reality of
lengths 5-6 (Hillar-Johnson anchor); the validity wall at length 8
($s \le 0.205$ among sound survivors; impostors dissected by the
predicted mechanism).

Does not prove: (PR-RP++) beyond block length 4 (measured wall, not
theorem); (PR-RP+) itself (the multi-letter Anderson assembly remains
the named residue even granting PR-RP++); (R-id) (a premise - exact
unbroken identity of copies; it is the gauge-universality reading and
is testable, but not derived); the rigidity converse of the graded
law; the closed form of the subleading heat coefficient.

## 6. The kernel after Paper 27

```text
(PR-RP+): the collision ran; LANE B AHEAD AT EVERY SCOPE.
   New theorem: PR2 (block-moment to length 4).  New conjecture:
   (PR-RP++) (peripheral block spectra = rho x roots of unity),
   proved to length 4, measured to length 8 (wall at s = 0.205).
   Residue: PR-RP++ beyond length 4 + multi-letter Anderson.
   New reading: bond-RP = quantum record ledgers (Prop. 1.1) - the
   (PR-RP+) question is the quantum/classical sealability boundary,
   joining P26's (QC-adv) dictionary.
(F-fiber): DISCHARGED into (R-id) (Theorem F1).  P-nu upgraded:
   rides on (R-id) + observed replication + theorems.  The Paper 25
   ledger row strengthens accordingly.
(C-reg-b): advanced to the GRADED law (C-reg-b'): exponent grades
   Holder class (4-point receipt); smooth anchor coefficient
   measured.  Residue: the rigidity converse, graded form.
KERNEL: { (C-reg-b') [graded, evidenced], (PR-RP++) [theorem to
   L = 4 + wall], (V), calibration } + { O7/O8/O11 remainders,
   D10-refinements, mu-dyn, loop-H, (R-id) }.
```

## 7. Status

```text
Part I:   Prop 1.1 proved; PR2 proved (0.0e+00 x 400 pairs x all
          blocks <= 4); reality map (5-6 real; first rotation L = 7
          marginal / L = 8 robust); wall s = 0.205 among 1882 deeply
          valid processes; impostor mechanism dissected (margin
          -1.35).  (PR-RP++) named.
Part II:  F1 proved; gauge condition exact at delta = 0, linear
          breaking (1.45/1.33); J and masses invariant to 1e-15,
          entries free; (F-fiber) -> (R-id); P-nu upgraded.
Part III: graded law measured (0.243/0.465/0.706/0.956 vs
          0.25/0.50/0.75/1.00); leading heat coefficient -1/4 at
          1e-3 universality; (C-reg-b') named.
```

## References and literature map

- Papers 4, 8, 10, 16, 18, 21, 24, 25, 26 (internal): silent-seam
  (P4), typed moment theorems (P8), the OS/transfer construction
  (P10), the clock and Theorem B (P16), R2/R3 (P18), G1/G2 (P21), the
  detector (P24), the ledger this paper upgrades (P25), the
  quantum/classical boundary dictionary (P26).
- A. Klein and L. J. Landau, J. Funct. Anal. 44, 121 (1981): OS
  reconstruction for reversible processes (Prop. 1.1's engine).
- C. J. Hillar and C. R. Johnson, "Eigenvalues of words in two
  positive definite letters," SIAM J. Matrix Anal. 23 (2002): the
  reality phenomenon of Section 2.3 (named anchor).
- F. R. Gantmacher, The Theory of Matrices II: Perron-Frobenius
  peripheral theory (behind P16 Theorem B, used here as engine).
- B. D. O. Anderson et al. (1996-99): positive realization under
  dominant poles (the residual assembly).
- C. Jarlskog, Phys. Rev. Lett. 55, 1039 (1985): the invariant of
  Section 3.2(ii).
- S. Minakshisundaram and A. Pleijel (1949); P. Gilkey, Invariance
  Theory: heat coefficients (Section 4.1's classical frame).
```
