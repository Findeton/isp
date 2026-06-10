# Paper 6 (v6.1) - SHARD: A_rec Is Gauge; the Intrinsic Coupling Is kappa*sigma_A

Author: Felix Robles Elvira

Subtitle:

```text
One-line gauge theorem, full naturality audit, the record passivity theorem,
and conditional branch-A closure with a single named axiom
```

## 0. Verdict

This revision replaces v6.0 of Paper 6 under stricter claim discipline. Every
claim below carries one of five statuses:

```text
PROVED-STRUCTURAL : proved by the structure of the definitions; finite
                    diagnostics are implementation audits, not the proof.
PROVED-FINITE     : proved at finite scope with complete finite proofs and
                    machine verification.
AXIOM-NAMED       : an explicitly named axiom; the claim is conditional on it.
IMPORTED-VERIFIED : standard external structure, verified at finite scope,
                    not yet derived from record primitives.
OPEN              : not established.
```

The verdict table:

```text
Absolute A_rec selection theorem (as posed in Paper 5 / the campaign brief):
  REFUTED AS ILL-POSED. PROVED-STRUCTURAL. No intrinsic functional of
  dimensionless record data can equal a quantity of nonzero unit weight.
  Paper 5's sigma_A split STANDS and is the finite witness of this fact.

A_rec gauge theorem (lambda-rescaling acts trivially on all intrinsic
readouts):
  PROVED-STRUCTURAL (one line, Section 2), conditional on the naturality
  audit, which is now executed: Section 3. Gate G1: CLOSED.

Naturality audit (no corpus law consumes A_rec outside the labeling map;
the refinement normalization n^2 is chart gauge):
  PROVED-FINITE for the executed corpus; interface-level for v1-v3 texts
  not in this corpus (explicitly scoped). The n^2 covariance lemma is
  PROVED-FINITE with exact machine verification.

Modular temperature T = 1/(2*pi):
  Decomposed. (G2-a) eventless => passive => completely passive => Gibbs:
  PROVED-FINITE (the record passivity theorem, Section 5, full proof).
  (G2-b) identification of the imaginary boost-flow period with the
  Euclidean normal-frame angle: AXIOM-NAMED, axiom (R), Section 7.
  Period = 2*pi given (R): PROVED-FINITE (silent-seam theorem, Paper 6 p6b).

Coupling product kappa*sigma_A = 2*pi (hence G*sigma_A = 1/4):
  PROVED-FINITE conditional on (R) and on the continuum focusing gate;
  premise ledger in Section 4 discloses that the v6.0 numerical scan was an
  implementation audit, not independent evidence.

Branch A:
  CONDITIONALLY CLOSED on the unit-gauge quotient: closed modulo exactly
  (i) axiom (R) and (ii) the Paper 5 continuum tensor gates, which this
  paper does not touch. The lambda direction itself is unconditionally
  gauge (G1). "Branch A closed" without these conditions, as v6.0's thesis
  block said, was an overclaim and is retracted in that form.

Successor problem:
  the matter/gravity hierarchy invariant, now stated with its
  equivalence-principle prerequisite and its difficulty class. OPEN.
```

The structural slogan survives v6.0 unchanged, because it was the part that
was right:

```text
representatives are not physical; closed invariants are.
A_rec is a representative. kappa*sigma_A is the invariant.
```

## 1. Review of v6.0

v6.0 is audited claim by claim before being rebuilt.

| v6.0 claim | review verdict | disposition in v6.1 |
|---|---|---|
| absolute A_rec selection is impossible in principle | SUSTAINED | restated as PROVED-STRUCTURAL with the invariant-ring lemma (Sec. 2) |
| Paper 5 counterfamily members are isomorphic record theories | SUSTAINED | kept; stated explicitly that Paper 5's split result is correct and is the witness, not an error (Sec. 2.3) |
| lambda-invariance "proved" by a 15-readout finite battery | MISCAST | the battery can never prove a universally quantified claim; the proof is structural (one line) plus the naturality audit; the battery is demoted to an implementation audit (Sec. 2-3) |
| "no-silent-seam forces period 2*pi" | SUSTAINED at its stated scope | kept; the cone-deficit theorem is native and proved (p6b) |
| modular temperature derived | OVERSTATED | the Unruh/Bisognano-Wichmann import was disclosed in v6.0 Sec. 5/11 but the thesis block outran it; now decomposed into the PROVED passivity theorem (G2-a) plus the single named axiom (R) (Secs. 5-7) |
| kappa*sigma_A = 2*pi "to 2.7e-15 across twelve configurations" | OVERSOLD AS EVIDENCE | the scan is near-circular: given the premise chain, the product is one-line algebra and the cross-sigma universality is the gauge statement, true by construction; the scan verifies consistent implementation only; all weight moves to the premise ledger (Sec. 4) |
| "branch A closed" / "the theory finally closes" | OVERCLAIMED | replaced by the conditional closure of Section 8 with the two outstanding gates named |
| hierarchy successor "the genuine open quantity" | SUSTAINED BUT BREEZY | hardened with the equivalence-principle prerequisite and an honest difficulty class (Sec. 9) |

Nothing in the physics of v6.0 is reversed. What changes is the location of
the load: off the diagnostics, onto the structure and the named premises,
where it belongs.

## 2. The one-line gauge theorem

### 2.1 Setup

A sealed record theory is presented as a pair:

```math
T=(\mathcal R,\ \ell),
```

where `R` is the record sector — all record data and all record laws: counts,
capacities `C`, RN/KL evidence, holonomy classes, `Z_perp`, sources, the
whole-history law `P_hist`, transports, Born screens — and `ell` is the
continuum labeling map:

```math
\ell(S)=A_{\rm op}(S)=A_{\rm rec}\,C(S).
```

Define the unit action `g_lambda`: the identity on `R`, and
`A_rec -> lambda*A_rec` on the label, with the induced action on all labeled
quantities. An **intrinsic readout** is, by definition, a function of `R`
alone.

### 2.2 Theorem and proof

**Theorem G (gauge triviality).** Every intrinsic readout is invariant under
`g_lambda`.

**Proof.** `g_lambda` restricted to `R` is the identity; an intrinsic readout
factors through `R`; therefore its value is unchanged. ∎

This is one line because the entire nontrivial content has been moved into a
presupposition: that the corpus really factors as `(R, ell)`, i.e. that no
stated law consumes `A_rec` anywhere except through `ell`. That presupposition
is gate G1, and it is discharged by audit, not by assertion, in Section 3.

Two corollaries fix the v6.0 framing errors:

```text
Corollary 1 (role of finite batteries). No finite battery of readouts can
prove Theorem G, and none is needed. The p6a battery is retained as an
implementation audit: it checks that the CODE realizing the corpus respects
the factorization. Its value 0.0e+00 gaps certify the implementation, not
the theorem.

Corollary 2 (invariant ring). A monomial readout in
(A_rec, areas, sigma_A, kappa) is g_lambda-invariant iff its total area
weight is zero; the invariant ring is generated by area ratios and the
product kappa*sigma_A. (Finite Buckingham-pi lemma; machine scan in p6a:
1750 invariant vs 13874 non-invariant monomials in the exponent box
[-2,2]^6, all invariants of weight zero.)
```

### 2.3 Paper 5 stands

Paper 5 Section 13 proved: same sealed horizon data, two `sigma_A` values.
That theorem is correct and untouched. What changes is its reading: by
Paper 5's own Feynman-split criterion, a physical split requires an intrinsic
`chi` with `chi(q_0) != chi(q_1)` on the same shadow. Here the full record
theory is the shadow, the two members are isomorphic as record theories
(identity map on atoms; machine check: max gap over all nine record-level
structures = 0.0e+00), and the differing entry is the unit label. The split
is real and it is a gauge orbit. Paper 5 found the orbit; this paper names
the group.

## 3. Full naturality audit (gate G1)

The audit has four parts: the clause-by-clause corpus table, the
audit-by-execution, the n^2 covariance lemma, and the cofinal equivariance
theorem. Diagnostic script:

```text
code/v6_p6e_naturality_audit_campaign.py
```

### 3.1 Clause-by-clause corpus table

Classification: NONE (the law never mentions area), LABEL-ONLY (the law uses
`A_op` only through the labeling map `ell`), PRODUCT-ONLY (the law constrains
only the weight-zero combination `kappa*sigma_A`), CHART (the law contains a
continuum-chart convention, resolved by the covariance lemma of 3.3).

| corpus law | sections | A_rec class |
|---|---|---|
| sealed diamond, exchange holonomy, event identity, eventless repair | P4 1-4 | NONE |
| single-diamond saturation law and constants | P4 5-7 | NONE |
| two-diamond Born composition, p=2 selection, interference | P4 8-10 | NONE |
| record-gravity packet: L, rho, phi, K_phi (record units) | P4 11-13 | NONE |
| scalar refinement L_n = n^2 (D-A) | P4 14-15 | CHART (3.3) |
| causal-screen tensor, screen stack | P4 16-19 | NONE / CHART (3.3) |
| no-twist transport, double-null kinematics, null-work, deletion/focusing | P4 20-27 | NONE |
| enriched RN deletion, A_D generation, T_D classification | P4 28-33 | NONE |
| exchange-cocycle law, transport-law campaign | P4 34-37 | NONE |
| whole-history determination, closed-holonomy law and field equation | P4 38-43 | NONE |
| source gluing, cellular source conservation | P4 44-47 | NONE |
| cofinal continuum reconstruction, admissible refinement | P4 48-51 | NONE / CHART (3.3) |
| readout completeness, cofinal readout completeness | P4 52-55 | NONE |
| closed-holonomy dynamics, source/period origin, law selection | P4 56-61 | NONE |
| closed-exchange action, h_G field equation, overlap/sheaf | P4 62-67 | NONE |
| division-event commitment law and cofinal/cover stability | P4 68-76 | NONE |
| finite Born representation theorem | P5 2-5 | NONE |
| GR falsification attacks; finite record gravity receipt | P5 6-9 | LABEL-ONLY at A_op; PRODUCT-ONLY at kappa |
| normal-normal split and minimal datum Z_perp | P5 10-11 | NONE |
| Einstein-form (Lovelock/HKT) gate | P5 12.1 | PRODUCT-ONLY (the kappa slot) |
| sigma_A determinacy campaign | P5 12.2-13 | LABEL-ONLY (this campaign IS the gauge orbit) |
| v1 gauge benchmark (cited interface) | v1 | NONE |
| v1-v5 seam/boundary-flux discipline (cited interface) | v1-v5 | NONE |
| v4 low-energy Lovelock repair (cited interface) | v4 | PRODUCT-ONLY (kappa slot) |
| v5 black-hole record counting (cited interface) | v5 | LABEL-ONLY (record count intrinsic; area enters via ell) |

Scope caveat, stated plainly: the v1-v3 full texts are not in this corpus;
their rows are audited at the interface level, through every property
Papers 4-5 cite from them. A future revision that imports those texts must
re-run this table. Within the present corpus, the audit is complete: no row
consumes `A_rec` outside `ell`, and the only convention sites are CHART rows.

### 3.2 Audit-by-execution

Every executable law of the corpus is implemented as a function with an
explicit `A_rec` argument and evaluated at `A_rec in {1, 3, 1/4}`. The gauge
parameter must be dead code in every law.

| executed law | A_rec-dependence gap | verdict |
|---|---:|---|
| saturation root (P4 s5) | 0.0e+00 | NONE |
| commitment root (P4 s71) | 0.0e+00 | NONE |
| coupled ledger h (P4 s71) | 0.0e+00 | NONE |
| Born p-selection (P4 s8 / P5 s3) | 0.0e+00 | NONE |
| interference table (P4 s9) | 0.0e+00 | NONE |
| survival gluing (P4 s71) | 0.0e+00 | NONE |
| record-gravity packet rho/phi/K (P4 s11-12) | 0.0e+00 | NONE |
| seam cancellation (P4 s44-47) | 0.0e+00 | NONE |

Worst gap over all executed laws: 0.0e+00. This is the implementation audit
that the v6.0 battery was mistaken for a proof.

### 3.3 The n^2 covariance lemma (the one convention site)

The refinement operator `L_n = n^2 (D - A)` contains the only scale
convention in the corpus: the factor `n^2` (more generally `c n^2`) that
identifies record steps with continuum derivatives. The lemma:

**Lemma (chart covariance).** For every level `n`: (i) the level-`n` record
law uses `(D - A)` only, so all record outputs are exactly `c`-independent;
(ii) intrinsic spectral ratios of `L_n` are exactly `c`-independent;
(iii) labeled spectra carry weight `+1` in `c`; (iv) the continuum limit
operator transforms covariantly, so changing `c` is a change of continuum
coordinate unit and nothing else.

**Proof.** (i) by inspection of the corpus laws (3.1-3.2: the record
dynamics never references `n^2`); (ii) `lambda_k(cL)/lambda_1(cL) =
lambda_k(L)/lambda_1(L)`; (iii) linearity of the spectrum in `c`;
(iv) `c n^2 (D-A) -> -c\,{\rm div}(G\,{\rm grad})`, which is the statement
that `c` rescales the chart metric, i.e. the length unit. ∎

Machine verification (circle, `c in {1, 2.7}`):

```text
n=16: spectral ratios [1, 3.847759, 3.847759, 8.109732] identical, gap 9.2e-14
n=64: spectral ratios [1, 3.990369, 3.990369, 8.942309] identical, gap 9.1e-14
      (converging to the circle-degenerate k^2 pattern [1,4,4,9])
chart covariance: ev(c=2.7)/ev(c=1) = 2.700000 exactly
record-step walk distribution gap (c=1 vs c=2.7): 0.0e+00
```

### 3.4 Cofinal equivariance and joint unit coherence

**Theorem (cofinal equivariance).** The unit action commutes with admissible
refinement and sealed gluing, and projective limits of record data are fixed
points of the action.

**Proof.** Refinement and gluing are maps of record data (3.1); the action is
the identity on record data at every level; a level-wise identity commutes
with every level-wise map and fixes every projective limit. The chart side
transforms with definite weight by 3.3. ∎

The unit group acts coherently with weight equal to area dimension
(length unit `l_0 -> mu l_0` induces `A_rec -> mu^2 A_rec`, chart coefficient
weight `-2`, `sigma_A` weight `-2`, `kappa` weight `+2`), and the weight-zero
ring — area ratios and `kappa*sigma_A` — is the intrinsic ring (machine
table in p6e Part 3; `kappa*sigma_A` and ratios exactly fixed under
`mu = 1.7`).

Gate G1 is closed at the stated scope.

## 4. Premise ledger for the coupling product

The coupling theorem of v6.0 Section 7 is retained with its evidence
honestly re-weighted.

**Theorem (coupling product, conditional).** Given premises N1-N3 and I1
below, Clausius balance for all flux profiles forces

```math
\kappa\,\sigma_A = 2\pi,
\qquad
G\,\sigma_A = {1\over4},
```

with the individual factors pure gauge (Theorem G).

The premise ledger:

```text
N1 (native, P4 s71): commitment law; record entropy change = RN evidence,
    delta S = delta I, in nats.
N2 (native, P5 record-area campaign): area form law delta S = sigma_A
    delta A_op; sigma_A is the gauge representative.
N3 (native modulo axiom (R)): modular temperature T = 1/(2*pi). Upgraded in
    this paper: the Gibbs form at SOME beta is now PROVED (Section 5); the
    identification beta = 2*pi is the silent-seam theorem (proved) THROUGH
    axiom (R) (named, Section 7).
I1 (imported, continuum gate): the linearized continuum focusing equation
    theta' = -R_kk. The finite double-null focusing readouts of P4 s22-27
    are native; their continuum limit is part of the Paper 5 tensor gates
    and remains OPEN.
```

Disclosure, replacing the v6.0 presentation: given N1-N3 and I1, the product
is one-line algebra (`delta Q` and `delta A` share the boost-weighted
integral form, so Clausius pins the ratio). The twelve-configuration scan of
p6c (max deviation 2.7e-15 from `2*pi`, BH coefficient 0.25 exactly,
local-Rindler error vanishing as 3.96e-09 -> 7.08e-10 -> 1.13e-10) verifies
that the implementation realizes the algebra consistently. It is not
independent evidence for the theorem, and the cross-`sigma_A` universality is
Theorem G in action, true by construction. The theorem's entire weight rests
on N1-N3 and I1; after this paper, exactly one axiom (R) and one continuum
gate (I1) remain open in that chain.

## 5. The record passivity theorem (gate G2-a)

This section proves the missing statistical half of the temperature: that
the eventless collar law is Gibbs in the boost weight at some inverse
temperature `beta >= 0`, from record-native premises. It is the finite
classical Pusz-Woronowicz/Lenard chain realized inside the sealed record
ontology. Diagnostic script:

```text
code/v6_p6f_record_passivity_campaign.py
```

### 5.1 Setting and definitions

A finite boost collar is a finite record atom set `Omega` with a boost
weight readout `K: Omega -> R` (the generator readout attached to the
oriented normal holonomy `Z_perp`), and a sealed law `p` on `Omega` with
`p > 0` unless stated. The sealed cyclic transports available to a sealed
operator are the count-preserving reversible record cycles: bijections
`pi: Omega -> Omega` restoring all collar structure. The record boost work
extracted by `pi` from `p` is

```math
W(\pi,p)=\mathbb E_p[K]-\mathbb E_{\pi_*p}[K]
=\sum_\omega p(\omega)\big(K(\omega)-K(\pi(\omega))\big).
```

```text
Definition (passive):    W(pi, p) <= 0 for every sealed cycle pi.
Definition (eventless):  the collar commits no record under any sealed cycle.
```

### 5.2 Lemma 0: eventless implies passive

Suppose an eventless collar admitted a sealed cycle with `W(pi,p) > 0`. The
cycle extracts positive boost work while the record ledger is unchanged: the
extracted action is carried by zero record evidence. By the RN
self-accounting law of Paper 4 Section 71 — the eventless collar contains no
hidden action besides the evidence it carries — this is exactly a silent
seam, and silent seams are excluded. Hence `W(pi,p) <= 0` for all `pi`. ∎

(Native status: Lemma 0 consumes only the corpus' own self-accounting law.
It is the same exclusion that fixed `lambda = 1` in the commitment proof.)

### 5.3 Lemma 1: passive iff anti-ordered

**Lemma 1.** `p` is passive for `K` iff for all `omega, omega'`:

```math
K(\omega)<K(\omega')\ \Rightarrow\ p(\omega)\ \ge\ p(\omega').
```

**Proof.** (Necessity) If `K(a) < K(b)` and `p(a) < p(b)`, the transposition
`pi = (a b)` extracts

```math
W=(p(b)-p(a))(K(b)-K(a))>0.
```

(Sufficiency) Suppose `p` anti-ordered. For any bijection `pi`, if there is
an inversion — a pair `a, b` with `K(pi(a)) > K(pi(b))` but `p(a) > p(b)` —
swap the images: the value `sum p(omega) K(pi(omega))` does not increase
(same product-pairing exchange as the transposition computation, with the
sign reversed). Finitely many exchanges produce an order-respecting pairing
of `p`-values with `K`-values whose sum equals the identity's (ties give
equality). Hence the identity is a minimizer of
`sum p(omega) K(pi(omega))`, i.e. `W(pi,p) <= 0`. ∎

This is the Hardy-Littlewood-Polya rearrangement inequality in record dress.
Machine check (d=4, all 24 permutations, 1200 random states): equivalence
1200/1200.

### 5.4 Lemma 2: sealed gluing forces complete passivity

**Lemma 2.** If every eventless collar is passive (Lemma 0), then for an
eventless collar `(Omega, K, p)` the product law `p^{\otimes N}` on
`Omega^N` with the additive weight `K_N = sum_i K(omega_i)` is passive for
every `N`.

**Proof.** Independent sealed collars glue to one sealed collar whose law is
the product law (Paper 4 independent composition) and whose RN/boost weight
is additive (the chain rule `I(D_1 \sqcup D_2) = I(D_1)+I(D_2)` of Paper 4
Section 71). A gluing of eventless collars is eventless. Apply Lemma 0 to
the glued collar. ∎

Complete passivity is therefore a theorem of the gluing structure, not an
extra axiom — the step that, in the operator-algebraic literature, must be
postulated, is here supplied by the corpus' own composition law.

### 5.5 Theorem: completely passive iff Gibbs

**Theorem (finite record Lenard).** Let `(Omega, K)` be a finite boost
collar and `p` a law that is completely passive (passive at every `N` in the
sense of Lemma 2). Then exactly one of:

```text
(a) p has full support and p(omega) = exp(-beta K(omega))/Z for a unique
    beta >= 0 (uniform p is the case beta = 0);
(b) supp(p) is contained in argmin K (frozen / ground sector states).
```

Conversely every law of type (a) or (b) is completely passive.

**Proof.**

*Converse.* For (a): `p^{\otimes N}(\vec\omega) = e^{-\beta K_N(\vec\omega)}/Z^N`
is a non-increasing function of `K_N` for `beta >= 0`, hence anti-ordered,
hence passive at every `N` by Lemma 1. For (b): any `pi` moves ground mass
to weights `>=` the minimum, so `W <= 0` at every `N`.

*Direct, Step 1 (support is a K-lower set).* If `K(a) < K(b)`,
`p(b) > 0`, then anti-ordering at `N=1` gives `p(a) >= p(b) > 0`.

*Step 2 (within-level equality on mixed support).* Suppose the support
contains two levels and two atoms `a, b` with `K(a) = K(b)` but
`p(a) > p(b) > 0`; let `c` be a supported atom on a different level. If
`K(c) > K(a)`: at level `N`, the all-`b` configuration has weight
`N K(a)` and probability `p(b)^N`, while the configuration with `N-1`
copies of `a` and one `c` has strictly larger weight and probability
`p(a)^{N-1} p(c)`. Anti-ordering requires

```math
p(b)^N \ \ge\ p(a)^{N-1}p(c)
\quad\Longleftrightarrow\quad
p(c)\ \le\ p(b)\Big({p(b)\over p(a)}\Big)^{N-1}\ \xrightarrow[N\to\infty]{}\ 0,
```

contradicting `p(c) > 0`. If instead `K(c) < K(a)`, run the mirrored
comparison (mostly-`c` configurations against one `a` versus one `b`).
Hence `p` factors through `K` on its support: `p = g(K)`, `g` non-increasing
(Lemma 1).

*Step 2'(no cutoff-Gibbs).* Suppose the support is a proper lower set with
at least two levels; let `E^* = max K(supp)`, `E_0 = min K`, and let
`E_a > E^*` be an unsupported level. For `k` large,
`k E^* > E_a + (k-1)E_0`, so the all-`E^*` configuration (probability
`g(E^*)^k > 0`) sits at strictly higher weight than a configuration using
the unsupported atom (probability `0`). Anti-ordering then demands
`g(E^*)^k <= 0`, a contradiction. So the support is either full or a single
(bottom) level — case (b).

*Step 3 (functional inequality).* Full support; write
`h(E) = log g(E)` on the spectrum `spec(K) = {E_1 < ... < E_m}`. For
occupation vectors, complete passivity (Lemma 1 at level `N`) says: for all
integer vectors `v` with `sum_i v_i = 0` (the difference of two occupation
multisets of equal size, always realizable as `v = v^+ - v^-`):

```math
v\cdot E>0\ \Rightarrow\ v\cdot h\le 0,
\qquad
v\cdot E=0\ \Rightarrow\ v\cdot h=0 .
```

*Step 4 (Farkas / density).* Consider the hyperplane
`H = {v in R^m : sum v_i = 0}` and the half `H^+ = H ∩ {v·E >= 0}`.
Rational directions are dense in `H`; every rational direction strictly
inside `H^+` has an integer representative, on which Step 3 gives
`v·h <= 0`; by continuity `v·h <= 0` on all of `H^+`. A linear functional on
`H` that is non-positive exactly on the half cut by `E|_H` is a non-positive
multiple of it (supporting-hyperplane/Farkas): `h|_H = -beta E|_H`,
`beta >= 0`. Extending off `H` by the normalization direction `1`:

```math
h(E)=\alpha-\beta E
\quad\Longrightarrow\quad
p(\omega)={e^{-\beta K(\omega)}\over Z}.
```

*Uniqueness (Lemma 3).* With at least two supported levels,
`beta = (h(E_i)-h(E_j))/(E_j-E_i)` is the same for every gap by affinity,
hence unique. ∎

### 5.6 What the proof mechanism predicts, and the machine confirms

The Step 3-4 inequality structure makes a sharp finite prediction. Take
`K = (0, 1, sqrt 2)` and the perturbed family
`p_t ∝ (1, e^{-beta}, e^{-beta(1+t)\sqrt2})`, `beta = 0.8`. A violation
needs an integer vector `v = (v_1, v_2, v_3)`, `sum v = 0`, with
`v_2 + sqrt2\,v_3 > 0` but small, and `v_3` negative enough that the
perturbation flips the sign: `v_2 + sqrt2 v_3 < t\,sqrt2\,|v_3|`. For
`t = 0.03` the first such vector is `v = (-3, 10, -7)`:
`10 - 7 sqrt2 = 0.1005 < 0.03·sqrt2·7 = 0.2970`, requiring
`N = max(\Sigma v^+, \Sigma v^-) = 10`.

The sieve finds exactly that:

```text
t = 0.00 : passive at every tested N = 1..14   (Gibbs; proved for all N)
t = 0.03 : fails first at N = 10, violation 1.700e-07
t = 0.10 : fails first at N = 3,  violation 1.473e-03
t = 0.30 : fails first at N = 3,  violation 8.014e-03
```

The within-level collapse is likewise explicit: `K = (0,0,1)`,
`p = (0.45, 0.35, 0.20)` is passive for `N <= 3` and fails at `N = 4`
(`min^4 = 0.01500625 < max^3 p_c = 0.018225`), with the extracting
transposition `(b,b,b,b) <-> (a,a,a,c)` yielding work `0.003219 > 0`. And
the gap-wise `beta` readout: spread `2.2e-16` for Gibbs, `8.0e-02` for the
perturbed law.

### 5.7 Passivity diagnostic

| target | test | result | value | verdict |
|---|---|---|---:|---|
| Lemma 1 | brute force over all 24 permutations, d=4, 1200 random states | passive <=> anti-ordered | 1200/1200 | EQUIVALENCE-EXACT |
| Gibbs converse | `p_0` (Gibbs) at N = 1..14 | anti-ordered at every level | no violation | PASSIVE-ALL-N (proved for all N) |
| complete-passivity sieve | perturbed `p_t`, K = (0,1,sqrt2) | first violating N and magnitude | t=0.03: N=10, 1.7e-07; t=0.1: N=3, 1.5e-03; t=0.3: N=3, 8.0e-03 | NON-GIBBS-REJECTED |
| Diophantine match | predicted first vector v=(-3,10,-7) for t=0.03 | predicted N=10 | observed N=10 | MECHANISM-CONFIRMED |
| within-level collapse | K=(0,0,1), p=(0.45,0.35,0.20) | passive N<=3, fails N=4; explicit transposition | work = 0.003219 | LEVEL-EQUALITY-FORCED |
| beta uniqueness | gap-wise beta readout | Gibbs spread 2.2e-16; perturbed spread 8.0e-02 | unique iff Gibbs | LEMMA-3 |
| gluing anchor | independent sealed composition | product law exact | gap 0.0e+00 | LEMMA-2-PREMISE |
| detailed balance | reversible boost ladder, Gibbs(beta) stationary | `p_i w_{ij} = p_j w_{ji}`; rate ratios `e^{-beta dE}` | gaps <= 8.7e-19 | KMS-RATIO-CARRIES-BETA |

Gate G2-a is closed: the eventless collar law is Gibbs at some
`beta >= 0`, from Lemma 0 (self-accounting), Lemma 2 (the corpus' gluing),
and the finite Lenard theorem.

## 6. From Gibbs(beta) to beta = 2*pi

Two further steps fix the value.

**Step 1 (proved, p6b).** The defect-free Euclidean normal-frame period is
exactly `2*pi`: a conical deficit `delta` is a closed normal-frame rotation
holonomy carried by zero record evidence on the transport loop — a silent
seam — and is excluded. Finite verification: triangulated-cone transport
recovers `hol = delta` to `4.2e-12` across `delta in {0, 0.3, 1}`.

**Step 2 (axiom-conditional).** The Gibbs parameter `beta` of the eventless
collar equals the angular period of the Euclidean section of the boost flow.
This is the analytic identification of imaginary modular/boost flow with
normal-frame rotation. Finite verification of its content: the boost
two-point correlator is KMS exactly at `beta = 2*pi` per unit surface
gravity and at no other `beta` (regulator-scaling gaps 1.2e-03 ->
1.2e-06 -> 1.2e-09 at `beta = 2*pi`; regulator-independent gaps ~ 4.7e+01
elsewhere); detailed-balance ratios carry `e^{-Theta omega}` with
`Theta` the period.

Given Step 2, Steps 1-2 give `beta = 2*pi`, i.e.

```math
T_{\rm mod}={1\over2\pi}=0.15915494309189535 .
```

## 7. Axiom (R), isolated

The single remaining import in the temperature chain is now stated as an
axiom rather than absorbed silently:

```text
Axiom (R) (Euclidean regularity / rotation identification):
  the eventless boost transport of a sealed collar admits an analytic
  continuation in its flow parameter, and the continued flow at imaginary
  parameter is the Euclidean normal-frame rotation, so that the KMS period
  of the eventless state equals the angular period of its Euclidean section.
```

Remarks, for honesty and for the successor work:

```text
1. (R) is the record-ontology residue of Bisognano-Wichmann/Unruh. Before
   this paper the entire mechanism (thermality AND its temperature) was
   imported. After this paper, thermality at some beta is PROVED (Section 5)
   and the period selection is PROVED (p6b); (R) carries only the
   identification between the statistical period and the geometric angle.

2. The abelian subtlety is acknowledged: in a commutative record algebra the
   modular flow of a state is trivial, so the boost flow must be supplied as
   dynamics — and it is: the ordered transport laws P_AB of Paper 4 Section
   34. KMS is then realized as stochastic detailed balance (verified to
   8.7e-19), which is the correct classical form. A noncommutative upgrade
   of the ledger (the Petz direction already flagged in Paper 4's
   references) would let (R) be attacked with Tomita-Takesaki tools; that is
   the natural route to discharging it.

3. Nothing else in the corpus depends on (R). If (R) fell, the theory would
   keep Gibbs thermality with beta a single undetermined intrinsic number -
   one real modulus - and branch A would fail by exactly that one dimension.
   The campaign therefore localizes the entire remaining temperature risk in
   one named, attackable statement.
```

## 8. Conditional branch-A closure

**Theorem (conditional closure).** Modulo axiom (R) and the Paper 5
continuum tensor gates (full tensor source readout; covariant 3+1
convergence; the continuum focusing limit I1), every intrinsic dimensionless
coupling of the gravity/record sector is derived, and the moduli space of
such couplings is a single point:

```text
primitive event tilt eta_evt (D = J saturation)   = 1.090344354879492
commitment root eta_c (tanh eta = e^-eta)          = 0.609377863436006
modular temperature x 2*pi                         = 1            [(R)]
kappa * sigma_A / 2*pi                             = 1            [(R), I1]
Bekenstein-Hawking coefficient G * sigma_A         = 1/4          [(R), I1]
```

The `lambda` direction is unconditionally gauge (Theorem G + the executed
audit, gate G1). Deformation attacks on each entry violate a derived
identity (commitment residual +0.060776; KMS gap 5.0e+01; Clausius residual
-1.69e-03; p6d).

What "closed" means here, exactly: nothing dimensionful remains to be
derived because nothing dimensionful is intrinsically definable (Section 2);
everything dimensionless that the sector can define is pinned, conditional
on one named axiom and the already-listed continuum gates. v6.0's
unconditional phrasing is retracted; this conditional statement is what the
mathematics supports.

## 9. The successor problem, hardened

The first intrinsic, gauge-invariant, unfixed number appears only with a
second record sector. The successor problem is stated in two parts, in
order, because the second is ill-typed without the first:

```text
H1 (equivalence-principle prerequisite): universal record footprint.
   Prove that every matter record event of unit RN evidence sources the same
   deletion response in the record-gravity packet, independent of the matter
   species/ledger that produced it. Without H1, "the" matter area per event
   is not well-defined and the ratio below is not a single number. H1 is the
   record-language equivalence principle / universality of coupling.

H2 (hierarchy selection): derive the intrinsic ratio
   c_m = A_matter / A_grav-quantum
   from the sealed whole-history law. This is the record analog of
   G m^2 / (hbar c) ~ (l_Planck / l_Compton)^2 ~ 1e-38 for the proton.
```

Finite status (p6d part ii): the ratio is intrinsic and `lambda`-invariant,
and toy values `c_m = 12` and `c_m = 1200` both pass every current identity
(`kappa*sigma_A / 2*pi = 1.000000000000` in all four cells): NOT-SELECTED.

Difficulty disclosure, owed and now given: H2 is the hierarchy problem in
record dress. No existing framework derives it — the Immirzi ambiguity of
loop quantum gravity is the same one-parameter area rescaling, fixed there
only by external Bekenstein-Hawking matching, and the cutoff dependence of
entanglement-entropy density is its continuum form. The honest expectation
class for H2 is: beyond all current corpus technology, requiring at minimum
a constructed matter sector with its own commitment-fixed ledger. Calling it
"cleaner" than the A_rec question, as the earlier review did, is true only
in the sense that it is well-posed; it is not easier.

## 10. What this paper proves and does not prove

It proves:

```text
1. Theorem G (one line) and its corollaries; the finite invariant-ring
   lemma; the dissolution of the Paper 5 split as a gauge orbit, with
   Paper 5's own theorem standing as the witness.
2. Gate G1: the full naturality audit of the present corpus (clause table +
   audit-by-execution, worst gap 0.0e+00), the n^2 chart-covariance lemma
   (exact), joint unit coherence, and cofinal equivariance.
3. Gate G2-a: the record passivity theorem - Lemma 0 from RN
   self-accounting, Lemma 1 (rearrangement), Lemma 2 from the corpus'
   product gluing, and the finite Lenard theorem with full proof, uniqueness
   of beta, and machine confirmation including the Diophantine prediction of
   the first violating copy number.
4. The period-selection theorem (defect-free 2*pi; carried over from p6b,
   proved and verified).
5. The conditional closure of Section 8, with its premise ledger.
```

It does not prove:

```text
1. Axiom (R). Named, isolated, attackable (Tomita-Takesaki route flagged).
2. The continuum tensor gates of Paper 5, including the continuum focusing
   limit I1. Unchanged by this paper.
3. H1 or H2.
4. Any empirical number distinguishing SHARD from GR + QM.
5. The naturality of the v1-v3 full texts beyond their cited interfaces.
```

## 11. Status

```text
Absolute A_rec:           ill-posed; refuted structurally; Paper 5 split is
                          the witness and stands.
Gauge theorem (G1):       proved; one line plus executed naturality audit;
                          n^2 is the lone convention site and is chart gauge.
Thermality (G2-a):        proved; eventless => passive => completely passive
                          => Gibbs(beta), with full finite Lenard proof.
Temperature value:        beta = 2*pi conditional on axiom (R) alone;
                          period selection itself is proved.
Coupling product:         kappa*sigma_A = 2*pi conditional on (R) + I1;
                          numerics reclassified as implementation audit.
Branch A:                 conditionally closed on the unit-gauge quotient;
                          the condition set is exactly {(R), Paper 5
                          continuum tensor gates}.
Successor:                H1 (universal record footprint) then H2 (hierarchy
                          selection); difficulty class disclosed.
```

## References and literature map

- Paper 4 (v6) and Paper 5 (v6), internal: the commitment and
  self-accounting laws (P4 s71), independent composition and additive RN
  evidence, the ordered transports (P4 s34), the double-null focusing
  readouts (P4 s22-27), the record-area form law and the sigma_A
  counterfamily (P5 s12-13), and the Z_perp datum.
- W. Pusz and S. L. Woronowicz, "Passive states and KMS states for general
  quantum systems," Commun. Math. Phys. 58, 273 (1978); A. Lenard,
  "Thermodynamical proof of the Gibbs formula for elementary quantum
  systems," J. Stat. Phys. 19, 575 (1978). The passivity-to-Gibbs chain of
  Section 5 is their finite classical form, with complete passivity supplied
  by the corpus' gluing law instead of postulate.
- G. H. Hardy, J. E. Littlewood, and G. Polya, *Inequalities* (1934),
  rearrangement inequality (Lemma 1).
- T. Jacobson, "Thermodynamics of Spacetime," Phys. Rev. Lett. 75, 1260
  (1995), `https://arxiv.org/abs/gr-qc/9504004`. The Clausius construction
  of Section 4; note that only the entropy-density combination of the
  coupling appears there, the continuum shadow of Theorem G.
- W. G. Unruh, Phys. Rev. D 14, 870 (1976); J. J. Bisognano and
  E. H. Wichmann, J. Math. Phys. 17, 303 (1976). The content of axiom (R)
  and the finite KMS verifications.
- R. H. Dicke, "Mach's principle and invariance under transformation of
  units," Phys. Rev. 125, 2163 (1962); M. J. Duff, L. B. Okun, and
  G. Veneziano, "Trialogue on the number of fundamental constants," JHEP 03
  (2002) 023, `https://arxiv.org/abs/physics/0110060`. The units-as-gauge
  discipline of Sections 2-3.
- G. Immirzi, `https://arxiv.org/abs/gr-qc/9701052`; C. Rovelli and
  T. Thiemann, `https://arxiv.org/abs/gr-qc/9705059`. The loop-gravity
  instance of the same rescaling freedom, compared in Section 9.
- T. Regge, "General relativity without coordinates," Nuovo Cimento 19, 558
  (1961). Deficit-angle curvature behind the cone diagnostic.
- D. Petz, on relative entropy and sufficiency (flagged in Paper 4): the
  noncommutative route to attacking axiom (R).
