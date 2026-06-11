# Paper 8 (v6) - SHARD: The Tractable Frontier Campaign

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
The Triangle Law refuted and replaced by the exact component laws of the
relation code; ledger chirality as the character group of the code, with
frustrated binding, enantiomer mass splitting, and a falling chiral
frontier (sampled upper bounds <~ 2^-n); the (R-)''' boundary made a
typed two-sided theorem - site reflections = the Hamburger moment class
on [-1,1], site + bond = the Stieltjes class on [0,1] (v6.4's Bernstein
class exactly) - with a size-2 certificate; the (C) docket extended to 3d
Euclidean, 2+1 Lorentzian, and curved Lorentzian with an audited uniform
constant; record symmetry breaking, an electroweak-shaped mechanism
(no-SSB law theorem, bimodal sealed branches, condensate-lifted fiber
stiffness); and the confinement dichotomy: area law iff the primitive
disorder lives on sealed closed-holonomy cells (finite-scope gauge
disorder, not continuum QCD)
```

This paper executes, in full, the seven tractable exploration routes listed
in Paper 7 Section 14.6 (routes 1-7).  Every claim carries a status; every
printed value is machine-verified by the diagnostic suite of Section 1.
This edition incorporates the post-review corrections of Section 2
(items 5-9).

## 0. Verdict

The campaign brief was Paper 7's list of what was "within reach of current
corpus technology."  All seven routes were run to completion.  Two of Paper
7's own results are corrected in the process - one refuted outright, one
restricted in scope - and both corrections open more physics than they
close.

```text
Route 1 (general-n Triangle Law):  EXECUTED - and the law is REFUTED, in
  both directions, by the corpus' own new theorems.  What replaces it is
  exact: the defect is an invariant of the relation code alone; it is
  ADDITIVE over indecomposable code components (machine: 1.6e-15); a
  disjoint triangle + 4-relation ledger at n=5 contains a triangle and
  anti-binds at -0.008401018551, exactly as decomposition predicts.  The
  n=4 exhaustive scan (32767 sets, all solved) finds 1680 triangle-bearing
  anti-binders and 15 no-triangle binders - the minimal binder being the
  [8,4,4] extended-Hamming-type code.  The single-relation case is settled
  for ALL weights (w=3 binds, w>=4 anti-binds, defect -> theta^w(1-w*kappa));
  the marginality 3*kappa - 1 = +0.0318 explains why no weight-based law
  could ever have been robust: all binding is a second-order effect.

Route 2 (binding refinements):  EXECUTED.  The defect is a code-geometry
  invariant; at n<=4 it is determined by the code weight enumerator (35
  connected classes, zero splits) - complete classification table given.
  Binding density of full ledgers GROWS with n (0.0172 -> 0.0432 -> 0.0738
  per mode): saturated ledgers are the binding-favorable species family.

Route 7 (chirality from orientation):  EXECUTED, with the largest yield of
  the campaign.  Orientation classes of a ledger are canonically the
  characters of its relation code (machine: orbit counts match |K| in all
  cases); relation-free ledgers are exactly achiral; orientation enters
  the physics ONLY through codeword signs.  Frustrated (sigma = -1)
  relations BIND HARDER: the frustrated triangle binds at +0.201674235292
  versus +0.008438104972 - an enantiomer mass splitting of 0.193236 nats.
  The 16 orientation classes of the full 3-spin ledger organize into a
  1+7+7+1 multiplet under its automorphism group.  And the mass gap
  theorem of Paper 7 is VIOLATED by oriented ledgers: min m_hat = 0.133531
  < 0.156109 at n=3, falling 0.064539 (n=4, exact) and 0.031749 (n=5),
  0.015748 (n=6) - the latter two SAMPLED, hence upper bounds on the true
  minima.  On these bounds the chiral spectrum is consistent with gapless,
  m_hat_min <~ 2^-n.  Scope, stated plainly: this is a LIGHTNESS mechanism
  and a chiral-LEDGER mechanism inside (M) - ledger chirality (orientation
  classes), not spinor chirality, not fermions, not the Standard Model.

Route 3 ((R-)''' boundary):  EXECUTED, and the boundary is now a TYPED
  theorem, two-sided.  The reflection TYPE selects the support class:
  site-reflection positivity at every size is exactly the (shifted)
  Hamburger moment class on [-1,1] (sufficiency by Gram; converse by the
  classical Hamburger theorem plus covariance boundedness, with the
  index-shift caveat made explicit); site + bond positivity at every size
  is exactly the STIELTJES class on [0,1] - which recovers v6.4's
  Bernstein class as precisely the two-reflection class.  The alternating
  (antiferromagnetic) sector is site-RP but bond-FAILS (rank-one bond
  block, predicted and matched to -0.9375) - the lattice-antiferromagnet
  phenomenon of Frohlich-Israel-Lieb-Simon.  Physical sectors (massive
  free fields in 1d and on a 3d-lattice line, Yukawa, power law) pass
  both reflections; damped oscillations fail at N=2 by an EXACT
  determinant identity C2 C4 - C3^2 = e^{-6a}(cos2k-1)/2: the boundary is
  razor sharp and certified at size 2.

Route 4 ((C) instances):  EXECUTED.  3d variable-conductance torus: error
  ratio 2.23 against the O(1/n^2) prediction 2.25.  2+1 leapfrog: ratios
  4.00/4.00/4.00 with cone isotropy converging at O(dx^2).  Curved
  Lorentzian (variable-speed leapfrog, frequencies measured from ACTUAL
  evolution): ratios 4.03/4.01/4.00; null-cone bending tracks the curved
  characteristic to 1.0e-4.  First uniform-convergence lemma: one constant
  C* = 0.25 bounds |lambda_k(n) - lambda_k| / (h^2 lambda_k^2) over an
  entire conductance class, audited at 2.6x margin.

Route 5 (record symmetry breaking - an EWSB-SHAPED mechanism, not the
  electroweak theory):  EXECUTED.  Three-layer result: (i) the LAW cannot
  break its own symmetry (strict convexity; machine spread 3.3e-16);
  (ii) the sealed collective coordinate of the complete pairwise family is
  BIMODAL with barrier 3.28 -> 1104.78 (N = 8 -> 1024) while the 1d ring
  is unimodal with h = eta_hist to machine precision (it is a single
  weight-N relation - the item-1 theory closing the loop): record-SSB is a
  division event sealing a branch, and it requires binding-favorable
  connectivity; (iii) exact fiber degeneracy = exact gauge (3.3e-16),
  condensate-lifted degeneracy gives broken generators a measured
  stiffness Delta ~ eps^0.92 alpha^1.06 while commuting generators stay
  exact: mass-from-condensate at finite record scope.

Route 6 (confinement probe):  EXECUTED.  Exact dichotomy theorem: with
  independent conjugation-invariant SU(2) disorder, Wilson traces obey an
  EXACT AREA LAW if the disorder lives on plaquettes (sealed closed-
  holonomy cells - the SHARD primitive) and an EXACT PERIMETER LAW if it
  lives on links (transports).  2d link-level Monte Carlo confirms the
  area law (pulls <= 1.2 sigma); the perimeter contrast is confirmed at
  <= 0.7 sigma; the 3d Bianchi-constrained probe gives a nonzero Creutz
  ratio chi(2,2) = 0.5563 +- 0.0463 (12 sigma).  Confinement, in record
  terms, is the statement that the primitive disorder is plaquette-type -
  which is what SHARD's ontology already asserts.
```

The kernel impact is collected in Section 10.  The headline: (M) is
substantially restructured (component law + chirality + lightness
mechanism + EWSB mechanism + confinement criterion all feed it), the
(R-)''' boundary is now exactly located, and the (C) docket includes every
dimension and signature short of the 3+1 theorem itself.

## 1. Method and reproducibility

The method is unchanged: close, dissolve, or reduce with proof; refutations
of the corpus' own conjectures are results and are reported first.  All
diagnostics run on Python 3 with numpy/scipy (mpmath for the 40-digit
fixed points):

```text
code/v6_p8a_triangle_law_campaign.py      routes 1-2: anchors, decomposition,
                                          refutation, 1D theory, exhaustive
                                          n=4, n=5 samples, families
code/v6_p8b_chirality_campaign.py         route 7: orientation classes,
                                          enantiomer spectra, multiplets,
                                          signed gap, chiral frontier
code/v6_p8c_bernstein_boundary_campaign.py route 3: moment theorem, physical
                                          sectors, N=2 certificate, eps*(N)
code/v6_p8d_convergence_instances_campaign.py route 4: 3d torus, 2+1 leapfrog,
                                          curved Lorentzian, uniform lemma
code/v6_p8e_record_ewsb_campaign.py       route 5: no-SSB, bimodality,
                                          stiffness law
code/v6_p8f_wilson_area_law_campaign.py   route 6: character theorems, 2d MC,
                                          perimeter contrast, 3d Creutz
```

All Monte Carlo uses fixed seeds; every number printed below is the output
of these scripts as committed.

## 2. Corrections owed and paid

```text
1. The Triangle Law (Paper 7 Sections 9.5, 14.6 route 1; v6.4 Section 1) is
   REFUTED as a general law, in both directions (Section 3).  Its n=3
   statement stands as proved (complete enumeration); its extrapolation was
   a small-code accident.  Paper 7 carries an annotation.
2. The v6.4 probe FORENSICS (Section 3.2): the probe labeled "triangle +
   free pair" (+0.016876309) was in fact two disjoint triangles (exact
   value 2 x 0.008438104972 = 0.016876209945; the true triangle-plus-free-
   modes defect is 0.008438104972 exactly, by the decomposition theorem).
   The probe labeled "triangle + 4-relation" (+0.020844986) in fact
   contains TWO triangles ({x,y,xy} and {xy,zw,xyzw}; code weights 3,3,4);
   exact value +0.020844970391.  v6.4's four probes therefore never tested
   a triangle against a genuinely disjoint anti-binding relation - which is
   exactly where the law fails.
3. The mass gap theorem (Paper 7 Section 9.6) is RESTRICTED IN SCOPE to
   unoriented ledgers.  Oriented (chiral) ledgers violate it: min m_hat =
   0.133530982072 at n=3, decreasing ~2^-n (Section 5.5).  The proof's
   mechanism (h_a <= eta_hist via Griffiths) fails for frustrated classes
   (h = 1.114142135492 > eta for the frustrated triangle); the theorem and
   its machine verification remain correct on their unoriented domain.
4. The monotone-above-triangle conjecture (raised during this campaign) is
   REFUTED: 10920 strict decreases among 213810 tested extensions
   (min increment -1.672e-02).
```

Post-review revision (corrections owed to external review and to this
paper's own re-examination):

```text
5. The first edition asserted "the all-N-stable class is exactly the
   moment class" on sufficiency plus examples.  The converse is now
   stated with its classical machinery (Hamburger/Stieltjes + covariance
   boundedness, Section 6), together with a subtlety the first edition
   missed entirely: the SITE cross-block pins C(r) only for r >= 2
   (machine demo: a sequence with C(1) = -5 is site-RP at every N), and
   the reflection TYPE selects the support class - site-only = Hamburger
   on [-1,1]; site + bond = Stieltjes on [0,1].  The first edition's
   "alternating sectors are reflection positive" is corrected to
   "site-reflection positive" (the bond block fails at -0.9375, rank one,
   exactly as predicted): the Bernstein class of v6.4 is recovered
   EXACTLY as the two-reflection class.
6. "Lemma 7.1" is demoted to Proposition (audited): its constant is
   machine-audited across the class, but the two-sided proof at the
   stated constant is open (O4).  Calling it a lemma outran the corpus'
   own claim discipline.
7. Section 8 is retitled: the mechanism is RECORD symmetry breaking; the
   electroweak name is an analogy and is now flagged as such wherever it
   appears.  The bimodality table's M*/N column pegs at the lattice
   boundary (a discrete-peak artifact, now annotated in the table and
   the script); sqrt(E[ss]) is the faithful condensate.
8. The n=5 and n=6 oriented-gap minima are SAMPLED and are upper bounds
   on the true minima; the quantitative law "m_hat_min ~ 0.27 * 2^-n" of
   the first edition is downgraded to "consistent with ~2^-n on sampled
   upper bounds" (Section 5.4); the exact statement is part of O2.
9. The 2d area law of Section 9 is KINEMATIC: two-dimensional gauge
   theory confines trivially (abelian included), so the 2d receipts
   certify the dichotomy theorem and the machinery, not confinement
   dynamics; the exact 2d factorization also assumes open boundary
   (torus corrections from Polyakov loops are not modeled).  Stated
   explicitly in Section 9.3.
```

## 3. Route 1: the Triangle Law at general n

### 3.1 The relation code and the exact laws

A ledger is a set S of m distinct nontrivial parity characters on n spins.
Its RELATION CODE K is the kernel of F2^S -> F2^n - a binary linear code of
length m and dimension m - rank(S), with minimum distance >= 3
automatically (weight-1 words are trivial characters, weight-2 words are
repeated characters; both excluded).  The character expansion gives the
exact identity

```math
{Z\over\prod_a\cosh h_a}\;=\;W_K(t)\;=\;\sum_{c\in K}\ \prod_{a\in{\rm supp}(c)}t_a,
\qquad t_a=\tanh h_a .
```

**Theorem 3.1 (code invariance).** psi, the commitment fixed point, m_hat,
and the defect depend on S only through K as a subset structure of S: two
ledgers with isomorphic relation codes have equal defects, at any n.
**Proof.** W_K is a function of K alone; psi = sum log cosh + log W_K;
the fixed point and D(P||U) are functions of psi. ∎

**Theorem 3.2 (component decomposition).** If K = K1 (+) K2 over a
partition of S (no codeword mixes the parts), then W = W1 * W2, the fixed
point decouples, and defect(S) = defect(S1) + defect(S2).  Modes touched by
no codeword contribute exactly zero (the relation-free zero law). ∎

Machine: component additivity verified across the ENTIRE n=4 exhaustive
scan, max gap 1.55e-15, and on 861 random n=5 sets, max gap 1.44e-15.
Code invariance in action: the pairs-only ledger on 4 spins and the
singles+pairs ledger on 3 spins have isomorphic codes and IDENTICAL
defects (+0.060894615327, equal to the last digit); likewise pairs-only
n=5 = singles+pairs n=4 (+0.192478880).

All Paper 6.3/6.4 anchor values are reproduced to 1e-12 (solver residuals
<= 1.8e-14): triangle +0.008438104972; single w4 -0.016839123523; 3-spin
pairwise +0.060894615327; 3-spin full +0.120139064573; single w5
-0.023567123904; plaquette = single w4 exactly (code invariance).

### 3.2 The refutation

Theorem 3.2 plus the anchor values already refute the global Triangle Law:
defect(triangle) + defect(single w4) = +0.008438104972 - 0.016839123523 < 0.

Machine, direct: S* = {x,y,xy} on spins 1-2, disjoint {z,w,u,zwu} on spins
3-5 (n=5, m=7, code weights {3,4,7}, triangle present):

```text
defect(S*) = -0.008401018551    decomposition prediction = -0.008401018551
gap = 1.1e-16.   CONTAINS A TRIANGLE AND ANTI-BINDS.
triangle + disjoint w5 (n=6, m=8): -0.015129018931 (= prediction exactly).
```

And the law does not even survive at n=4, nor for connected codes.  The
exhaustive scan - all 32767 statistic sets on 4 spins, every fixed point
Newton-polished below 1e-13, every set decomposed into indecomposable code
components (24967 distinct connected codes solved):

```text
relation-free:            1380   max |defect| = 1.2e-15  (zero law: exact)
triangle-bearing:        29719   min defect = -0.008284544219
relations-no-triangle:    1668   max defect = +0.012439836169
violations, global:       1680 triangle-anti  +  15 no-triangle-bind
violations, connected:    1680 triangle-anti  +  15 no-triangle-bind
```

### 3.3 Minimal counterexamples

```text
Minimal connected triangle-bearing ANTI-BINDER:
  masks {x, y, xy, z, w, yzw}  (m=6, code weights {3,4,5})
  defect = -0.008284544219
  - one triangle glued to a 4-relation through a shared mode still
    anti-binds; gluing shifted the disjoint value -0.008401 by only +1.2e-4.

Minimal connected NO-TRIANGLE BINDER:
  masks {x, y, z, xyz, w, xyw, xzw, yzw}  (m=8)
  code = the [8,4,4] extended-Hamming-type code (weights 4^14, 8)
  defect = +0.012439836169
  - a distance-4 self-dual code BINDS: binding does not require triangles
    at all; it can be assembled entirely from interacting weight-4 words.
```

### 3.4 The single-relation theorem (all weights, exact)

A single weight-w relation reduces, by code invariance and symmetry of the
unique fixed point, to the scalar problem

```math
\tanh h+(1-\tanh^2h)\,{\tanh^{w-1}h\over1+\tanh^w h}=e^{-h},
```

solved at 40 digits:

```text
  w    defect(w)             first-order theta^w(1-w*kappa)   ratio
  3   +0.008438104972291     -0.005105640645752    -1.65
  4   -0.016839123523194     -0.032827182757183    +0.51
  5   -0.023567123903722     -0.034186341316418    +0.69   (|defect| max)
  6   -0.021780633113267     -0.027469835199371    +0.79
  8   -0.012214241830450     -0.013371668136528    +0.91
 12   -0.002061783361279     -0.002086147023869    +0.99
 16   -0.000262122892964     -0.000262475207817    +0.9987
 24   -0.000003228444384     -0.000003228492885    +0.99999
 30   -0.000000107108657     -0.000000107108709    +1.000000
```

**Theorem 3.3 (single relations).** A single weight-3 relation binds; a
single weight-w relation anti-binds for every w >= 4 (machine-verified at
40 digits through w = 30, with the asymptotic law defect -> theta^w(1 -
w*kappa) confirmed to 6 digits at w = 30); |defect| peaks at w = 5; the
defect of any single-relation ledger AT ANY n equals the table value (code
invariance). ∎

**The marginality.** The first-order theory is exact in the codeword
amplitude: each codeword contributes theta^w (1 - w*kappa) at leading
order, with

```math
\kappa={\eta\,(1-\theta^2)\over1-\theta^2+\theta}=0.343922878815527,
\qquad
3\kappa=1.031768636446582 .
```

The sign boundary sits at w = 1/kappa = 2.9076: weight 3 lies just ABOVE
it (3*kappa - 1 = +0.0318), so even the triangle's first-order
contribution is negative (-0.005106 against the true +0.008438): ALL
binding in this theory is a second-order (codeword self-interaction)
effect.  This single number explains the campaign's refutations: a sign
decided at second order cannot be classified by any first-order
(weight-counting) law - not the Triangle Law, not the parity rule, not
monotonicity.

### 3.5 What survives, and the named residue

Exact and proved: code invariance (3.1), component additivity (3.2), the
relation-free zero law, the single-relation theorem (3.3), the first-order
asymptotics.  Verified at n <= 4 exhaustively and n = 5 by sampling
(861 random relation-carrying sets: additivity exact; the global and
connected "laws" each violated 138 times - the refutation is generic, not
exotic).

**Classification robustness (the referee question, asked and answered).**
The exhaustive classification uses a 1e-9 sign threshold against a 1e-13
solver residual.  Is any class dangerously close?  No: the minimum
|defect| over relation-carrying CONNECTED classes at n <= 4 is
0.008284544 - six orders above the threshold.  But TOTAL defects of
decomposable ledgers can approach zero by component cancellation: the
smallest such composite, two disjoint triangles plus a disjoint
4-relation (first realizable at n = 7, m = 10), has

```text
defect = +0.000037086421   (prediction 2*tri + w4, matched to 1.1e-16)
```

- a near-zero total from exactly cancelling components.  Sign
classification is therefore meaningful only PER COMPONENT; this is one
more reason the component law, not any global sign rule, is the physics.

Empirically complete at n <= 4: the defect is determined by the code
WEIGHT ENUMERATOR - 35 connected classes, zero enumerator classes with
more than one defect value (full table in Section 4).  Caveat, stated
plainly: at these lengths enumerator-equivalent INEQUIVALENT codes may
simply not exist, in which case the determinism is vacuous; the statement
is evidence about n <= 4 only, and the first genuine test is a pair of
inequivalent codes sharing an enumerator at larger n.  This is part of
the residue:

```text
O1 (the sign function of relation codes): characterize sign(defect) - and
   ideally defect itself - as a function of the relation code.  Known:
   additive over components; exact for single relations; determined by the
   enumerator at n <= 4 (possibly vacuously); decided at second order in
   the codeword expansion.
```

## 4. Route 2: binding refinements and stable-species families

The complete classification of connected codes on <= 4 spins (enumerator ->
defect; every value the exact solver output):

```text
[3]                       +0.008438105     [4]                -0.016839124
[5]                       -0.023567124     [3,4,5]            -0.008284544
[3^2,4]                   +0.020844970     [3^2,6]            +0.016876210
[4^3]                     -0.026351161     [3^2,4^3,5^2]      +0.013117622
[3^3,4^2,5,6]             +0.033961746     [3^3,4^3,7]        +0.037610325
[3^4,4^3]                 +0.060894615     [4^7]              -0.017060290
[3^3,4^7,5^4,7]           +0.045945404     [3^4,4^5,5^4,6^2]  +0.059371669
[3^4,4^6,5^4,8]           +0.060852814     [3^5,4^5,5^2,6^2,7]+0.078351024
[3^7,4^7,7]               +0.120139065     [4^14,8]           +0.012439836
... (densest)
[3^35,4^105,...,12^35,15] +0.648143165     (the full n=4 ledger)
```

Structural readings:

```text
1. Triangle dominance is REAL but LOCAL: within these connected classes,
   every class containing >= 2 weight-3 words binds; one triangle alone
   does not survive a glued or disjoint 4/5-relation ([3,4,5] anti-binds).
2. Pure-distance-4 codes change sign with density: [4] and [4^3] and [4^7]
   anti-bind; the dense self-dual [4^14,8] binds.  Binding is a collective
   property of codeword geometry, not of individual relations.
3. Monotonicity fails (Section 2, correction 4): adding modes to a
   triangle-bearing set can lower the defect by as much as 1.7e-2.
```

Binding density of the saturated families (the stable-species direction
for (M)):

```text
family                       m     defect          defect per mode
full set n=3                 7    +0.120139065     +0.017162724
full set n=4                15    +0.648143165     +0.043209544
full set n=5                31    +2.287722188     +0.073797490
singles+pairs n=3            6    +0.060894615     +0.010149103
singles+pairs n=4           10    +0.192478880     +0.019247888
singles+pairs n=5           15    +0.429040990     +0.028602733
```

Binding density GROWS with capacity: the full (maximally relation-dense)
ledgers are the binding-favorable species family, with per-mode binding
roughly doubling per added spin over this range.  Stable composite species
should be sought among dense, enumerator-rich codes - with their chiral
structure now part of the search space (Section 5).

## 5. Route 7: chirality from ledger orientation

**Terminology, fixed before use.** "Chirality" in this section means
LEDGER chirality: inequivalence of a statistic set under sign reversal of
its modes, classified below by orientation characters of the relation
code.  It is NOT spinor chirality (handedness of half-integer rotation
fibers); that is a different structure, constructed in Paper 9, and
parity violation in the record ontology turns out to require BOTH (the
record Weyl seed, Paper 9 Section 9).  The two notions must not be
conflated: a chiral ledger is an Ising-level object.

### 5.1 Orientation classes are the characters of the relation code

An oriented ledger carries signs eps in {+-1}^S: phi_a = eps_a chi_a.
Spin flips realize exactly the sign patterns in K^perp.

**Theorem 5.1.** The orientation classes {+-1}^S / (spin flips) are
canonically the character group of K: the class of eps is sigma_eps(c) =
prod_{a in c} eps_a, and the partition identity becomes

```math
W_{K,\sigma}(t)\;=\;\sum_{c\in K}\sigma(c)\,t^c :
```

orientation enters the commitment physics ONLY through the codeword signs
sigma. ∎  (Machine: brute-force orbit counts equal |K| for the triangle
(2), single w4 (2), relation-free (1), two glued triangles (4), and the
full 3-spin ledger (16).)

**Corollary 5.2 (achirality).** Relation-free ledgers have one orientation
class: they are exactly mirror-symmetric.  A ledger coupling distinguishes
orientation classes IFF it carries a relation - route 7's classification
question, answered.  (Machine: all 16 sign patterns of {x,y,z,w} give
defect 0.)

### 5.2 Enantiomer spectra: frustration binds harder

```text
  w   defect(sigma=+1)    defect(sigma=-1)    splitting Delta m_hat
  3   +0.008438104972     +0.201674235292     0.193236130320
  4   -0.016839123523     +0.105877085870     0.122716209393
  5   -0.023567123904     +0.061267877568     0.084835001472
  6   -0.021780633113     +0.037705561769     0.059486194882
  8   -0.012214241830     +0.014826223488     0.027040465318
```

The sigma = -1 class of a relation is its FRUSTRATED form (for the
triangle: the classic frustrated Ising triangle), and every frustrated
single relation BINDS - the frustrated triangle 24 times harder than the
oriented one.  Chirality is physical in this theory: enantiomer ledgers
have different masses, with splittings of order 0.1 nats/cycle.  The
record seed of parity violation is the codeword sign sigma - a discrete,
gauge-invariant, relation-attached datum (the abelian cousin of a Wilson
sign), exactly as anticipated by "ledger orientation" in Paper 7 Section
14.4.1, and now with its classification theorem.

### 5.3 Chiral multiplets

The orientation classes organize into multiplets under the ledger's
automorphism group.  Two glued triangles (dim K = 2, 4 classes): defects
{+0.0208449704 (1), +0.2400306447 (2), +0.2900693619 (1)}.  The full
3-spin ledger (dim K = 4, 16 classes):

```text
defect +0.9592334190  x 1    m_hat = 0.1335309821
defect +0.4969939626  x 7    m_hat = 0.5957704385
defect +0.4162445803  x 7    m_hat = 0.6765198208
defect +0.1201390646  x 1    m_hat = 0.9726253365
```

a 1+7+7+1 multiplet structure under Aut = GL(3,2) - the first appearance
in this corpus of a generation-like degeneracy pattern: one ledger, four
chiral species masses with multiplicities fixed by representation theory.

### 5.4 The signed gap is violated; the chiral spectrum is gapless

Exhaustive over all 2186 oriented ledgers on 3 spins (residuals < 1e-10):

```text
min m_hat = 0.133530982072  <  m_hat(P1) = 0.156109200157  GAP VIOLATED
attained at the fully frustrated class of the full ledger;
max fixed-point coefficient h_a = 1.984035345 > eta: the gap proof's
Griffiths mechanism fails for frustrated classes (as it must - frustrated
ledgers are not ferromagnets).
```

The frontier, by exact (n = 4) and sampled (n = 5, 6) minimization over
orientation classes of the full ledgers:

```text
n = 3: 0.133531 (exact)      n = 4: 0.064539 (all 2048 classes, exact)
n = 5: 0.031749 (sampled)    n = 6: 0.015748 (sampled)
```

Scope of the trend, stated precisely: the n = 5 and n = 6 values come
from 803 and 122 sampled classes out of 2^26 and 2^57 - they are UPPER
BOUNDS on the true minima.  What is established is therefore: the
oriented minimum is NOT bounded below by the unoriented gap, and it falls
at least as fast as a factor ~2 per spin on the exact points (n = 3, 4)
and on the sampled bounds beyond.  The fitted law m_hat_min ~ 0.27 * 2^-n
is a description of these bounds, not a theorem; the true asymptotics
could fall faster.  Either way the physics stands: maximally frustrated
dense chiral ledgers approach masslessness while remaining committed
matter - a concrete LIGHTNESS mechanism: light species = large-capacity,
maximally frustrated, chiral ledgers.  This is the sharpest tool the
corpus now owns against the hierarchy half of (M), and it supersedes
v6.2's qualitative "weakly selected modes are light" direction with a
computable family.  It is a lightness mechanism and a chiral-ledger
mechanism - not fermions (Paper 9) and not the Standard Model.  Named
residue:

```text
O2 (the oriented gap): prove m_hat_min(n) ~ c 2^-n for the frustrated full
   ledgers (or find its true asymptotics), and determine whether any
   oriented ledger family reaches zero at finite n.  Status: OPEN; data
   through n=6.
```

The unoriented gap theorem stands on its own domain, with the corrected
scope recorded in Paper 7.

## 6. Route 3: the (R-)''' boundary, typed by reflection

### 6.1 The typed moment theorems

Site reflection through the origin makes the Gaussian OS cross-block the
Hankel matrix G_ij = C(i+j), i,j >= 1; bond reflection (through the bond
between sites 0 and 1) makes it G_ij = C(i+j-1).

**Theorem 6.1 (typed sufficiency).** Let C(r) = int lambda^r dnu(lambda)
with nu >= 0.  If supp(nu) is in [-1,1], the SITE cross-block is PSD at
every N (Gram: G = int v v^T dnu, v_i = lambda^i).  If supp(nu) is in
[0,1], the BOND cross-block is also PSD at every N (its Gram form needs
lambda dnu >= 0).  For signed support the bond block can fail. ∎
(Machine: 200 random mixtures on [-0.95, 0.95]: site worst -1.9e-15, bond
worst -7.4e+01; the same mixtures folded onto [0, 0.95]: bond worst
-2.0e-15.)

**Theorem 6.2 (converses, imported classical machinery).**
(i) Site-RP at every N means the Hankel matrices of the SHIFTED sequence
m_k = C(k+2) are PSD at every order; by HAMBURGER's theorem (Shohat-
Tamarkin) m has a representing positive measure on R, and the covariance
bound |C(r)| <= C(0) (Cauchy-Schwarz) forces its support into [-1,1].
Site reflection pins C(r) for r >= 2 ONLY: the values C(0), C(1) are
invisible to it.  (Machine, the index-shift demo: C(1) = -5 with
C(r >= 2) = 0.6^r is site-RP at every tested N - min eig -5.8e-17 at
N = 24 - while the bond block fails instantly at -5.0.)
(ii) Site + bond RP at every N is exactly the STIELTJES condition for
m_k = C(k+1) (the two interlaced Hankel families): representing measure
on [0, infinity), and boundedness forces [0,1]. ∎

**Corollary 6.3 (the class structure).** The all-N-stable classes are:

```text
site reflection only:   (C(r))_{r>=2} a Hamburger moment sequence on [-1,1]
site + bond reflection: (C(r))_{r>=1} a Stieltjes moment sequence on [0,1]
                        = EXACTLY the Bernstein/completely-monotone class
                          of v6.4.
```

The alternating (antiferromagnetic) sector C(r) = (-0.6)^r separates the
two: site-RP at -5.8e-17 while its bond block is the rank-one matrix
-0.6 u u^T with min eigenvalue -0.9375 (machine matches the closed form
exactly).  This is the lattice-antiferromagnet phenomenon of
Frohlich-Israel-Lieb-Simon: reflection positivity through sites but not
bonds.  Since the corpus' OS/transfer construction (v6.3 site-RP theorem)
uses SITE reflections, the operative (R-) class is the larger Hamburger
one, and the kernel content is:

```text
(R-)''' (typed): reflection positivity of long-range record sectors whose
collar correlations are NOT (shifted) Hamburger moment sequences on
[-1,1]; sectors that are Stieltjes (Bernstein class) additionally carry
bond reflections.
```

**[Paper 10 update.]** The typed classes acquired their dynamical
characterization, and the kernel was reduced: site-RP = reversible
primitive transport, site+bond-RP = reversible with nonnegative transfer
spectrum, and the no-silent-arrow theorem (eventless implies detailed
balance, via the exchange cocycle) makes RP a THEOREM for every eventless
sector with a finite primitive Markov presentation - the RP failures of
this section are exactly the DRIVEN (entropy-producing, hence not
eventless) sectors.  See Paper 10 Part I.

### 6.2 Physical sectors

```text
1d lattice massive free field      C(r) = lambda^r (exact geometric)
  (m^2 = 0.1: lambda = 0.729844;  m^2 = 1.0: lambda = 0.381966)
                                                  site + bond RP (Stieltjes)
3d massive lattice field, line restriction (FFT, L=64)  site RP (-1.9e-15)
Yukawa e^{-0.4r}/(1+r)                            site + bond RP (CM)
power law (1+r)^{-1.5}                            site + bond RP (CM)
alternating (-0.6)^r                              site RP ONLY (Hamburger)
damped oscillation e^{-0.2r} cos(kr), k in (0,pi)       FAILS, N=2
RKKY cos(1.2r)/(1+r)^3                                  FAILS, N=1
```

Every massive-free-field-induced collar coupling tested is in the moment
class: the free sectors of conventional physics sit INSIDE the closed
(R-) territory.  The failures are precisely the gapless-background
oscillatory couplings.

### 6.3 The boundary is razor sharp: a size-2 certificate

For C(r) = e^{-ar} cos(kr) the exact identity

```math
C_2C_4-C_3^2\;=\;e^{-6a}\,{\cos 2k-1\over2}\;<\;0
\quad\hbox{for every }k\notin\{0,\pi\}
```

(machine: identity exact to printed digits at eight values of k) makes
every pure damped oscillation fail reflection positivity already at N=2.
From an INTERIOR moment point (continuous mixture), the critical
admixture of a non-moment perturbation falls fast:

```text
eps*(N):  N=2: 0.065092   N=4: 0.000283   N=6: 0.000005   N>=8: 0.000000
```

The all-N-stable site class is exactly the shifted Hamburger moment class
(Theorem 6.2); every non-moment sector fails at a small computable size.
The per-model certificate is correspondingly cheap (demonstrated at N=24
on three sectors), and the practical content for (R-)''' is: candidate
long-range record sectors are decidable at small N - the kernel is a
question about which CLASS nature's collar correlations occupy, not about
hard finite computations.

## 7. Route 4: the (C) docket - 3d, 2+1, curved Lorentzian, uniform bound

```text
(i)  3d Euclidean, variable conductance c(x,y,z) = 1 + 0.3 sin(2pi x)
     cos(2pi y) + 0.2 sin(2pi z), first 7 nonzero eigenvalues, Richardson
     reference from n=16,24:
       max rel err n=8:  5.385e-02
       max rel err n=12: 2.409e-02    ratio 2.23  [O(1/n^2): 2.25]
(ii) 2+1 Lorentzian leapfrog at k = (0.7, 0.4), dt = dx/2:
       dx = 0.1 -> 0.0125: errors 8.27e-05, 2.07e-05, 5.17e-06, 1.29e-06
       ratios 4.00, 4.00, 4.00
     cone isotropy (spread of omega over angle at |k| = 1):
       2.08e-04 -> 5.21e-05 -> 1.30e-05  (O(dx^2))
(iii) curved Lorentzian: u_tt = d_x(c(x) d_x u), c = (1+0.5 sin 2pi x)^2,
     frequencies measured from ACTUAL leapfrog evolution (three-term
     phase recursion); time-dispersion prediction matched to <= 9.3e-07:
       n = 32..256: errors to continuum 1.028e-01, 2.549e-02, 6.359e-03,
       1.589e-03; ratios 4.03, 4.01, 4.00
     null-cone bending: energy peak vs integrated characteristic
     dx/dt = sqrt(c): gaps 1.34e-03 (n=256), 1.80e-04 (512), 1.03e-04
     (1024) against x_char = 0.548338.
```

**Proposition 7.1 (uniform-convergence bound; AUDITED, not proved).** For
the bond-conductance scheme on the circle, over the entire class

```text
c(x) = 1 + three-harmonic Fourier series, sum of |coefficients| <= 0.45
       (hence 0.55 <= c <= 1.45),
```

all refinement levels n and all modes k, the eigenvalue error obeys

```math
|\lambda_k^{(n)}-\lambda_k|\;\le\;C^*\,h^2\,\lambda_k^2,
\qquad C^*={1\over4}.
```

Claim status, per the corpus' discipline: this is NOT a proved lemma.
The proof route is named (min-max comparison of the discrete and
continuum Rayleigh quotients on interpolants of the first k
eigenfunctions; for constant c the exact dispersion gives the sharp
constant 1/12, and the class bounds must control the variable-c
consistency terms), and the constant is MACHINE-AUDITED across the
class - 30 random conductances x n in {32,64,128} x modes 1..12 give

```text
sup |lambda_k(n) - lambda_k| / (h^2 lambda_k^2) = 0.0964  (margin 2.6x)
```

- and the audited statement is what (C) needs: a single constant for a
whole refinement family, not per-instance ratios.  This is the first
uniformity statement in the (C) docket; promoting it to a theorem at the
stated constant is O4.

The docket now spans 1d/2d/3d Euclidean, flat 2+1 and curved 1+1
Lorentzian, all at clean second order, with one audited uniform constant.
What remains for (C) is unchanged in kind - the uniform 3+1 Lorentzian
theorem - but every ingredient now has a verified finite instance.

## 8. Route 5: record symmetry breaking (an electroweak-shaped mechanism)

The name "electroweak" below is an ANALOGY and nothing more: no
electroweak group, scale, representation content, or coupling is derived.
What is established is the record-native MECHANISM - condensate from a
sealed branch, partial lifting of a fiber degeneracy, massive broken
generators with exact residual gauge - which is the shape the electroweak
phenomenon has, at finite scope.

### 8.1 The law cannot break; the record can

**Theorem 8.1 (no-SSB at finite scope).** The commitment free energy is
strictly convex (P7 Theorem 9.2), so the fixed point is unique; for a
ledger with automorphism group Aut, the fixed point is Aut-invariant.
Spontaneous symmetry breaking of the LAW is impossible at finite record
scope. ∎  (Machine: pairs-only n=4 ledger, 12 random starts, fixed-point
spread 3.3e-16, orbit anisotropy 2.2e-16.)

**The bimodal sealed branch.** The complete pairwise family (maximally
triangle-rich, the binding-favorable topology of Section 4) at its own
commitment fixed point, exactly via the magnetization statistic:

```text
   N      h(N)      N*h(N)   sqrt(E[ss])   ln[P(M*)/P(0)]
    8    0.235207   1.8817    0.889048          3.28
   32    0.068260   2.1843    0.966446         14.73
  128    0.020910   2.6765    0.989600         85.22
  512    0.006330   3.2410    0.996840        478.16
 1024    0.003454   3.5369    0.998275       1104.78
```

The sealed law is BIMODAL at every N, with branch barrier growing
superlinearly (~N^1.25 on this range): two macroscopic branches of a
symmetric, unique law.  (Table note: the discrete peak position M*/N pegs
at the lattice boundary because the fixed point forces E[ss] -> 1 - O(1/N),
putting the peak within ~2 lattice steps of |M| = N - a discretization
artifact; sqrt(E[ss]) is the faithful condensate column and is what the
table reports.)  The contrast family - pairwise couplings on a 1d
ring - is UNIMODAL with h = 0.609378 = eta_hist to machine precision:
the ring bonds form a single weight-N relation, so the item-1 theory makes
it near-free (theta^N corrections), no condensate, no branch.

```text
Record-SSB: the symmetry is broken by a DIVISION EVENT that seals one
branch of the bimodal collective coordinate - in the record, never in the
law - and it requires binding-favorable connectivity (relation-dense
codes).  SSB is thereby placed in the same ontological slot as every other
actuality in this corpus: commitment.
```

### 8.2 Condensate-lifted fiber degeneracy: the stiffness law

The composed-holonomy probe (path-dependent fiber transports T_j =
exp(i tau_j K_eps), K_eps = diag(1, 1-eps), gauge rotation G at the seam):

```text
exact degeneracy (eps = 0):    max marginal change under U(2) = 3.3e-16
lifted, COMMUTING generators:  2.2e-16 at eps = 0.4   (exact gauge)
lifted, broken generator:      Delta(alpha, eps) measured:
    eps = 0.05..0.40, alpha = 0.1..0.2:
    alpha-exponent 1.06-1.12, eps-exponent 0.92:  Delta ~ C eps alpha
wiring: sealed branch (x* = 1):     Delta(0.3) = 3.02e-02
        half condensate (eps=0.5):  Delta(0.3) = 1.85e-02
        ring family (no branch):    Delta(0.3) = 3.3e-16
```

A committed branch makes the broken fiber generators physical with
stiffness linear in the lifting, while the commuting subgroup remains
exact gauge: the record analogue of gauge bosons acquiring mass from a
vacuum expectation value, with the "vacuum" replaced by the sealed branch
of a bimodal record law.  Scope: a toy at finite scope - no claim about
the electroweak scale, the Higgs potential, or custodial structure; what
is established is that the MECHANISM (condensate -> partial lifting ->
massive broken generators + exact residual gauge) exists natively in the
record ontology, with all three layers machine-verified.

## 9. Route 6: the confinement dichotomy

### 9.1 Exact theorems

**Theorem 9.1 (character factorization).** For independent conjugation-
invariant SU(2) random elements g_1..g_A and any irreducible character:
E[chi_j(g_1...g_A)] = d_j (E[chi_j(g)]/d_j)^A. ∎  (Schur orthogonality;
machine: MC at A = 1,2,4,6,9 within 1.4 sigma of r^A at 2e5 trials.)

**Theorem 9.2 (area law from sealed plaquettes).** If the primitive
disorder lives on PLAQUETTES (independent sealed closed-holonomy cells),
the fundamental Wilson trace obeys an exact area law <(1/2)tr W(R,T)> =
r^{RT}, sigma = -ln r, with r = I_2(beta)/I_1(beta) for the Wilson
one-cell weight (machine: quadrature vs Bessel, gap <= 1.1e-16; sigma =
1.066695 at beta = 1.5).  Scope: the plaquette-independence presentation
of a 2d lattice gauge field holds for OPEN boundary conditions (axial
gauge); on a torus there are Polyakov-loop corrections not modeled
here. ∎

**Theorem 9.3 (perimeter law from transport noise).** If the disorder
lives on LINKS (independent transports), the same identity gives an exact
perimeter law r^{2(R+T)}. ∎

**What these theorems are and are not.** The 2d area law is KINEMATIC:
two-dimensional gauge theory confines trivially - abelian included - so
Theorem 9.2 by itself is not evidence of confinement dynamics.  The
content of this section is the DICHOTOMY (9.2 vs 9.3): with identical
one-cell disorder, the Wilson-trace law is decided entirely by WHERE the
disorder lives - and the 3d probe, where confinement is a nontrivial
(though, for 2+1d SU(2), expected) property.

### 9.2 Machine verification

2d link-level Wilson-action Monte Carlo (L = 12, beta = 1.5) against
Theorem 9.2:

```text
loop (1,1): 0.343629(1908)  vs  0.344144   0.27 sigma
loop (1,2): 0.119530(1192)  vs  0.118435   0.92 sigma
loop (2,2): 0.012371(4015)  vs  0.014027   0.41 sigma
loop (2,3): -0.000014(1955) vs  0.001661   0.86 sigma
loop (3,3): 0.002672(2158)  vs  0.000068   1.21 sigma
```

Independent-link disorder at the SAME one-cell distribution (800 draws):

```text
loop (1,1): 0.014655(1526) vs perimeter 0.014027 (0.41 sigma) vs area 0.344144
loop (2,2): 0.000487(1503) vs perimeter 0.000197 (0.19 sigma) vs area 0.014027
loop (3,3): -0.001074(1476) vs perimeter 0.000003 (0.73 sigma)
```

3d probe (6^3, beta = 2.2, Metropolis with Bianchi-constrained plaquettes,
loops averaged over the three planes):

```text
W(1,1) = 0.358205(1016)   W(1,2) = 0.135857(1728)   W(2,2) = 0.029542(1141)
W(2,3) = 0.004679(1211)   W(3,3) = -0.000166(1193)
Creutz chi(2,2) = 0.5563 +- 0.0463   (nonzero at 12 sigma)
W(3,3) below measurement resolution; chi(3,3) not quoted.
```

### 9.3 The record reading

```text
The Wilson-trace law is decided by WHERE the primitive holonomy disorder
lives: on closed-holonomy cells (sealed diamonds) -> exact area law; on
transports -> perimeter law.  SHARD's primitive IS the sealed closed-
holonomy cell (P4), so record-primitive gauge disorder sits on the
area-law side of the dichotomy by construction; the 3d Bianchi-
constrained probe is area-law-consistent at the tested coupling.
Scope, restated for emphasis: this is finite-scope gauge DISORDER, not
continuum QCD.  The 2d half is kinematic; the 3d probe is strong/
intermediate coupling on a 6^3 lattice; the continuum and weak-coupling
statements remain (R-)'''/(C)-class and are not claimed.  What this route
establishes is that the confinement QUESTION is now posable - and at
finite scope answerable - in the corpus' own primitive terms, upgrading
Paper 7 Section 14.4.6 from "not yet posed" to "posed, with finite
theorems and a probe."
```

## 10. The kernel after Paper 8

The kernel set is unchanged in name - {(R-)''', (C), (M), (V)} - and
substantially restructured in content:

```text
(R-)''' NARROWED AND TYPED: the closed territory is the (shifted)
        Hamburger moment class on [-1,1] for site reflections (two-sided:
        sufficiency by Gram, converse by Hamburger + boundedness with the
        index-shift caveat), and exactly the Stieltjes/Bernstein class on
        [0,1] when bond reflections are also required (Theorems 6.1-6.2,
        Corollary 6.3); size-2 boundary certificate; every
        free-field-induced sector tested lies inside the closed part.

(C)     UNCHANGED in statement; the docket now contains 1d/2d/3d
        Euclidean, flat 2+1 and curved 1+1 Lorentzian instances, all at
        second order, plus one audited uniform constant (Proposition 7.1,
        C* = 1/4, margin 2.6x - audited, not proved).

(M)     RESTRUCTURED by this campaign:
        - the species classification variable is the relation code with
          its orientation character (K, sigma), not triangle counts;
        - the defect is additive over components, exactly;
        - binding-favorable families are the dense codes (per-mode binding
          grows with capacity); stable species live there;
        - ledger chirality is native: enantiomer splittings ~0.1 nats;
          multiplet structure under Aut (1+7+7+1 realized);
        - the lightness mechanism: maximally frustrated chiral ledgers
          have m_hat <~ 2^-n on sampled upper bounds - a computable route
          at the hierarchy;
        - an EWSB-shaped mechanism available natively (record-SSB +
          degeneracy lifting with measured stiffness law; analogy, not
          the electroweak theory);
        - confinement criterion posable (plaquette-primitive disorder).
        The SM inverse problem of Paper 7 Section 10.4 gains, accordingly,
        two new finite-checkable clauses: (vi) chiral structure from
        orientation characters; (vii) plaquette-primitive disorder for the
        confining factor.

(V)     untouched by this campaign.

NEW NAMED OPEN PROBLEMS:
O1  the sign function of relation codes (Section 3.5).
O2  the oriented gap asymptotics m_hat_min(n) - exact minima beyond
    n = 4 and the true decay law (Section 5.4).
O3  enumerator determinism of the defect beyond n = 4, starting with an
    inequivalent same-enumerator code pair (Section 3.5).
O4  the rigorous two-sided proof of Proposition 7.1 at its stated
    constant.
```

## 11. What this paper proves and does not prove

Proves, with machine verification at the printed values: Theorems 3.1-3.3
(code invariance, component decomposition, single relations at all
weights); the refutation of the Triangle Law in both directions with
minimal counterexamples and the near-cancellation composite
(+0.000037086421 at n = 7, matched to 1.1e-16); Theorem 5.1 and Corollary
5.2 (orientation classes = code characters; achirality of relation-free
ledgers); the enantiomer spectra, multiplet structure, and the violation
+ corrected scope of the gap theorem; Theorems 6.1-6.2 and Corollary 6.3
(typed moment classes, with the imported Hamburger/Stieltjes converses,
the index-shift caveat, and the N=2 determinant certificate); the four
(C) instances; Theorem 8.1 (no-SSB) with the bimodality/connectivity
dichotomy and the stiffness law; Theorems 9.1-9.3 (character
factorization, area/perimeter dichotomy - the 2d half kinematic, stated
as such) with 2d MC confirmation and the 3d Creutz probe.

Does not prove: O1-O4 (in particular Proposition 7.1's constant is
audited, not proved); the gapless limit of the chiral spectrum (exact
data through n = 4; sampled upper bounds at n = 5, 6); enumerator
determinism beyond n = 4 (possibly vacuous even there); any continuum or
weak-coupling confinement statement; anything about the actual
electroweak group, scale, representations, or couplings; spinor chirality
or fermions (Paper 9); the 3+1 theorem (C) itself.  The Triangle Law's
failure is a refutation, not a gap: the corrected exact laws (invariance,
additivity, single-relation table) carry all of its surviving content.

## 12. Status

```text
Triangle Law:    REFUTED at n>=4 (1680 + 15 counterexamples; minimal ones
                 exhibited); replaced by exact code laws; sign function O1.
Single relations: settled for ALL weights at ALL n (w=3 binds, w>=4 anti).
Marginality:     3*kappa - 1 = +0.031769: all binding is second-order.
Chirality:       LEDGER chirality (not spinor; see Paper 9): orientation
                 classes = K-characters (theorem); frustrated relations
                 bind; enantiomer splitting 0.193236 (triangle);
                 multiplets 1+7+7+1; chiral minima fall <~ 2^-n on
                 sampled upper bounds (exact through n=4) (O2);
                 unoriented gap theorem scope corrected.
(R-)''':         TYPED two-sided boundary: site = Hamburger on [-1,1]
                 (converse via Hamburger + boundedness; site pins r >= 2
                 only); site+bond = Stieltjes on [0,1] = v6.4's Bernstein
                 class exactly; alternating sectors site-RP/bond-fail
                 (-0.9375, rank one, matched); N=2 certificate;
                 eps*(N) -> 0 boundary map.
(C):             3d Euclidean ratio 2.23/2.25; 2+1 ratios 4.00 x3 with
                 O(dx^2) isotropy; curved Lorentzian 4.03/4.01/4.00 from
                 actual evolution; null cone tracked to 1e-4; uniform
                 constant C* = 1/4 audited at 2.6x margin - audited, not
                 proved (Proposition 7.1, O4).
Record SSB:      (EWSB-shaped analogy, not the electroweak theory) law
                 cannot break (3.3e-16); sealed branches bimodal, barrier
                 3.3 -> 1104.8 (N=8 -> 1024; M*/N boundary artifact
                 annotated, condensate = sqrt(E[ss])); ring contrast
                 exact (h = eta_hist); stiffness Delta ~ eps^0.92
                 alpha^1.06; commuting generators exact.
Confinement:     dichotomy: area iff plaquette-primitive disorder (exact;
                 2d half kinematic, open-BC scope stated); 2d MC pulls
                 <= 1.2 sigma; perimeter contrast <= 0.7 sigma;
                 3d chi(2,2) = 0.5563(463), 12 sigma; finite-scope gauge
                 disorder, not continuum QCD.
Robustness:      min |connected-class defect| = 0.008285 (six orders
                 above threshold); near-cancellation composite
                 +0.000037086421 at n=7 (matched 1.1e-16): classify per
                 component only.
Kernel:          {(R-)''' (typed, two-sided), (C) (docket grown), (M)
                 (restructured), (V)}; new open set {O1, O2, O3, O4}.
```

## References and literature map

- Papers 4-7 (internal): the commitment law and chain rule (P4 s71), the
  closed-holonomy primitive (P4 s1-2, s40), the variational principle and
  gap theorem (P7 s9.2, s9.6 - scope corrected here), the Triangle Law
  (P7 s9.5 - refuted here), degeneracy gauge (P7 s10.3), the route list
  (P7 s14.6).
- F. J. MacWilliams and N. J. A. Sloane, *The Theory of Error-Correcting
  Codes* (1977): binary linear codes, weight enumerators, the [8,4,4]
  extended Hamming code that appears as the minimal no-triangle binder.
- R. B. Griffiths (1967); G. Toulouse, "Theory of the frustration effect
  in spin glasses" (1977): the ferromagnetic/frustrated dichotomy behind
  the oriented-ledger results.
- J. A. Shohat and J. D. Tamarkin, *The Problem of Moments* (1943): the
  Hamburger and Stieltjes existence theorems invoked in Theorem 6.2;
  F. Hausdorff (1921); S. N. Bernstein (1928): the moment-class theorem.
  J. Frohlich, R. Israel, E. H. Lieb, and B. Simon (1978): long-range
  reflection positivity.
- U. Mosco (1994); Kuwae-Shioya (2003); Cavalletti-Mondino (2020-): the
  (C) toolset, as in Paper 7.
- P. W. Anderson, "More is different" (1972); R. B. Griffiths on
  rounding of transitions: the finite-scope SSB discussion of Section 8.
- K. Wilson, "Confinement of quarks," Phys. Rev. D 10, 2445 (1974);
  M. Creutz, "Asymptotic-freedom scales" / *Quarks, Gluons and Lattices*
  (1983): Wilson loops, Creutz ratios, strong-coupling area law; A. A.
  Migdal (1975): exact 2d factorization behind Theorem 9.2.
- B.-G. Englert; Fuchs-van de Graaf; Barandes (2302.10778): as in Paper 7.
