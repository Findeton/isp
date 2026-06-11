# Paper 7 (v6.4) - SHARD: The Kernel Frontier Campaign

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
The Triangle Law of binding (settled by exhaustive enumeration), the
commitment variational principle, reflection positivity for the Bernstein
class, two new convergence instances, continuous gauge groups from dilation
degeneracy, existence of the infinite whole-history law, a dynamical-Lambda
mechanism, and the stopping assessment
```

## 0. Verdict

v6.3 left the kernel {(R-)'', (C), (M), (V)} with several sharp finite
sub-problems attached. This edition attacks every kernel item at its honest
frontier. One sub-problem is SETTLED outright by complete enumeration; the
others are advanced by proved theorems and verified instances; and the
edition closes with the assessment the program now owes itself: what
further internal iteration can and cannot buy.

```text
SETTLED:

The binding classification (attached to (M) in v6.3): RESOLVED at small
  scale by exhaustive enumeration. All 127 statistic sets on 3 spins were
  classified by machine. Result - the TRIANGLE LAW:
     relation-free sets:        defect = 0   (theorem; 56/56, gaps < 2e-8)
     sets containing a triangle: defect > 0  (64/64 bind)
     relation-carrying, no triangle: defect < 0 (7/7 anti-bind)
  Zero exceptions on complete data. Four fresh 4-spin probes - including
  the plaquette {xy,yz,zw,wx} and a mixed triangle+4-relation set - all
  confirm the law's predictions. Bonus observation: the plaquette and
  {x,y,z,xyz} defects agree to 8 decimals (-0.016839): the defect is an
  invariant of the relation structure alone, as relabeling covariance
  requires.

NEW THEOREMS:

Commitment variational principle: the commitment fixed point is the unique
  global minimizer of the commitment free energy
     Phi(h) = psi(h) + sum_a exp(-h_a),
  which is strictly convex (Hessian = Cov(chi) + diag(e^-h) > 0). Every
  fixed point used anywhere in this corpus is therefore unique, and the
  binding scan is globally reliable by construction.
L3 existence half: sealed gluing implies Kolmogorov projective consistency
  of refinement marginals (machine: exact); the infinite whole-history law
  EXISTS as the projective limit. Operator/geometry convergence remains
  (C); the existence of the LAW itself is closed.

ADVANCED:

(R-): discharged additionally for Gaussian long-range sectors in the
  Bernstein class (completely monotone couplings J(r) = Laplace transform
  of a positive measure): reflected-block min eigenvalue -1e-17 (holds),
  versus -2.8e-02 for an oscillating coupling (fails - the condition does
  real work). Kernel now (R-)''': non-completely-monotone long-range
  sectors, with the per-model finite PSD check always available.
(C): two new instances. 2d variable-conductance torus converges spectrally
  to -div(c grad) at O(1/n^2) (ratio 4.2 per doubling); 1+1 Lorentzian
  leapfrog dispersion converges to omega = k at O(dx^2) (errors 1.25e-3 ->
  3.13e-4 -> 7.81e-5). The (C) precondition set now includes curved 2d and
  a genuinely Lorentzian instance.
Gauge mechanism completed: continuous gauge groups are DEGENERACY
  REDUNDANCIES of the dilation fiber. A U(2) rotation of an exactly
  degenerate ancilla pair changes no sealed marginal (1.7e-16) while
  transforming fiber holonomy covariantly. Finite ledger automorphisms
  give the discrete skeleton (v6.3); exact fiber degeneracy promotes it to
  the unitary group of the degenerate block. U(1) x SU(2) x SU(3) thus
  requires degeneracy fibers of dimensions 1, 2, 3 - the SM inverse
  problem of v6.3, now with its mechanism fully specified.
(V): a mechanism, not a value. In a growing packet whose capacity outruns
  its events (capacity ~ t^2, events ~ t), Lambda_hat(t) = 2 pi W Ebar(t)
  declines (0.490 -> 0.245 -> 0.123 -> 0.061): state-data cosmology has a
  natural smallness mechanism; the observed value remains open.

KERNEL AFTER v6.4:

(R-)'''  non-completely-monotone long-range reflection positivity
(C)      the full 3+1 spectral convergence theorem
(M)      realized-ledger selection: which Triangle-Law-classified ledgers,
         with which degeneracy fibers, nature instantiates (the SM inverse
         problem and the spectrum value)
(V)      the cosmological state value
```

## 1. The Triangle Law

Diagnostic script:

```text
code/v6_p7h_binding_classification_campaign.py
```

### 1.1 The variational principle

**Theorem 1.1.** Define the commitment free energy Phi(h) = psi(h) +
sum_a e^{-h_a}, with psi the log-MGF of the ledger statistics under the
counting base. Then the commitment law grad psi = e^{-h} is exactly the
stationarity condition of Phi; Phi is strictly convex, since its Hessian
is the statistics covariance plus a positive diagonal; hence the
commitment fixed point exists and is UNIQUE for every ledger. ∎

This retroactively certifies every fixed point computed in Papers 4-7 and
makes the exhaustive scan below globally trustworthy (machine: multi-start
minimizations agree; residuals < 1e-7).

### 1.2 The classification, by complete enumeration

A statistic set on n spins is a subset of the 2^n - 1 nontrivial parity
characters. Its RELATIONS are the subsets whose product is identically 1
(equivalently, exponent vectors summing to zero over F2); a TRIANGLE is a
3-element relation, e.g. {x, y, xy}.

All 127 sets on 3 spins were solved and classified:

```text
relation-free sets:                 56   defect = 0 exactly (Theorem:
                                         relabelings of independent modes;
                                         spot checks < 2e-8)
relation-carrying, with triangle:   64   ALL bind   (defect > 0)
relation-carrying, no triangle:      7   ALL anti-bind (defect < 0)
exceptions:                          0
```

**The Triangle Law (empirically complete at 3 spins).** A coupled ledger
binds iff its statistic set contains a multiplicative triangle; carries
relations but no triangle, it anti-binds; relation-free sets have exactly
zero defect.

Fresh 4-spin tests, none used in forming the law:

```text
plaquette {xy,yz,zw,wx}   (4-relation, no triangle): -0.016839116  anti  OK
{x,y,z,w,xyzw}            (5-relation, no triangle): -0.023567141  anti  OK
{x,y,xy} + free pair      (triangle present):        +0.016876309  bind  OK
{x,y,xy,xyzw,zw}          (triangle + 4-relation):   +0.020844986  bind  OK
```

Two structural observations fall out of the data. First, the mixed probe
shows triangles DOMINATE: one triangle outweighs a coexisting 4-relation.
Second, the plaquette's defect equals the {x,y,z,xyz} defect to eight
decimals: the defect is an invariant of the relation structure alone (the
two sets are relabelings of the same relation type), which is relabeling
covariance acting exactly as the quotient functoriality theorems demand.

**Status.** The binding classification posed in v6.3 is SETTLED at small
scale: theorem for the zero class, complete enumeration at n = 3, and the
law confirmed on all fresh probes. The general-n proof of the Triangle Law
is the residual mathematics; its physical content - pairwise-closed
coupling structures are the binding-favorable ones - feeds directly into
(M): stable composite species should be triangle-rich ledgers.

## 2. Reflection positivity: the Bernstein class

Diagnostic script (Sections 2-6):

```text
code/v6_p7i_kernel_frontier_campaign.py
```

**Theorem 2.1 (imported and instantiated).** For Gaussian record sectors
with reflection-symmetric long-range couplings J(r) that are completely
monotone (Bernstein: J the Laplace transform of a positive measure, e.g.
exponential or power-law decay), reflection positivity holds. Machine: the
reflected covariance block has min eigenvalue -1e-17 for J = 0.3 e^{-0.5r}
(holds to precision), versus -2.8e-02 for the oscillating coupling
0.3 e^{-0.2r} cos(2.5r) (genuinely fails). ∎

With v6.3's site-RP theorem (all nearest-neighbor sectors, interacting
included) and v6.2's Gaussian discharge, the (R-) ledger now reads: NN
sectors closed; Gaussian Bernstein-class long-range closed; kernel (R-)'''
= non-completely-monotone long-range sectors, for which the finite
per-model PSD check remains available. The oscillating counterexample is
kept deliberately: it shows the remaining kernel is not vacuous.

## 3. (C): the instance set now spans curved 2d and Lorentzian

The 2d variable-conductance torus converges spectrally to -div(c grad)
with errors 8.6e-3 (n=20) and 2.0e-3 (n=40), ratio 4.2 per doubling -
clean O(1/n^2). The 1+1 leapfrog dispersion relation sin(omega dt/2) =
(dt/dx) sin(k dx/2) converges to the continuum null cone omega = k at
O(dx^2) (1.25e-3 -> 3.13e-4 -> 7.81e-5). Together with the 1d
Sturm-Liouville instance of v6.3, the (C) docket now contains flat and
curved, 1d and 2d, Euclidean and Lorentzian verified instances; the
theorem itself - uniform spectral convergence of controlled sealed
refinements in 3+1 with Lorentzian signature - remains the program's
central piece of hard analysis, toolset as named in v6.3.

## 4. Gauge structure: the mechanism completed

v6.3 established the discrete skeleton (gauge group = ledger automorphism
group; S3 realized). The continuous half is now demonstrated:

**Theorem 4.1 (degeneracy gauge).** Let two ancilla directions of the
dilation fiber be exactly degenerate. Then any U(2) rotation of that pair
leaves every sealed marginal invariant (machine: max change 1.7e-16,
unitarity preserved to 2.2e-16) while acting covariantly on fiber
holonomy. Exact degeneracy of a k-dimensional fiber block yields a U(k)
redundancy of the dilation: continuous gauge groups are degeneracy groups
of the representation, with the finite ledger automorphisms as their
discrete skeleton. ∎

This is the correct relative placement: the scalar screen phase is the
abelian U(1) of period 2 pi (Papers 7 v1-v2), and non-abelian structure
lives on internal degeneracy fibers - exactly where Yang-Mills structure
lives relative to electromagnetism. The Standard-Model inverse problem of
v6.3 is accordingly sharpened: find the minimal ledger family with
degeneracy fibers of dimensions 1, 2, 3, Triangle-Law-favorable binding
topology, three replicated generations within the record-Bekenstein
bound, (EP)-admissible couplings, and seam-cancellation-consistent
sources. Every clause is finite-checkable per candidate; the search itself
is kernel (M).

## 5. L3: the existence half closed

**Theorem 5.1.** Sealed refinement families are projectively consistent:
the gluing law makes coarse marginals of fine laws equal the coarse laws
identically (machine: 0.0e+00). By the Kolmogorov extension theorem, the
infinite whole-history law exists as the projective limit. ∎

This separates cleanly what v6.3's L3 had fused: EXISTENCE of the
continuum whole-history law is now closed; what remains under (C) is
operator and geometry convergence, and what remains under L3 proper is
the infinite-dimensional ledger reconstruction (the unbounded-operator
analogue of P4 s40), now the only purely quantum-side open item.

## 6. (V): a smallness mechanism

In a growing packet whose record capacity outruns its committed events
(capacity ~ t^2, events ~ t), the sealed mean commitment density falls as
1/t and with it Lambda_hat = 2 pi W Ebar:

```text
t = 2:  Lambda_hat = 0.490432
t = 4:  Lambda_hat = 0.245216
t = 8:  Lambda_hat = 0.122608
t = 16: Lambda_hat = 0.061304
```

State-data cosmology therefore possesses a natural SMALLNESS MECHANISM:
old, capacity-rich packets are generically Lambda-small. This is a
mechanism demonstration and nothing more - the observed value, and whether
our packet's capacity/event history realizes it, is kernel (V).

## 7. Stopping assessment

This corpus has now reached the boundary where further iteration of the
present kind - finite theorems plus machine campaigns - has sharply
diminishing returns, and intellectual honesty requires saying so plainly.

What internal campaigning has bought, cumulatively: the gauge dissolution
of A_rec with kappa sigma_A = 2 pi; thermality with T = 1/(2 pi) for all
nearest-neighbor and Bernstein-class sectors; signature, orientation, and
(1,3) from commitment; the equivalence principle as a theorem and
admissibility condition; the quantum representation closed at finite scope
with its empirical residue graded; the two-constants resolution with the
work quantum identified as the mass quantum; a matter mechanism with the
Triangle Law settled by complete enumeration; gauge structure with its
continuous mechanism; Lambda located as state data with a smallness
mechanism; and a corrected, graded experimental contact surface.

What it cannot buy: (R-)''' and (C) are professional-grade analysis
(constructive-field-theory and spectral-convergence mathematics measured
in months, not campaigns); (M) is a search problem plus the general
Triangle-Law proof; (V) requires cosmological state input. None of these
yields to another round of the same method, and pretending otherwise
would breach the corpus' own first rule.

The handoff package is therefore: four standalone notes ready for
extraction (the gauge resolution; signature-from-commitment;
passivity-to-thermality with the 2 pi unification; the Triangle Law with
the variational principle); the full diagnostic suite (16 scripts, one
dependency-free); and the explicit kernel with per-item attack routes.
The single highest-value next action is no longer internal: it is
adversarial review by the quantum-foundations and mathematical-physics
communities, beginning with the program whose correspondence this corpus
now constructively realizes.

## References

As in v6.3, with: S. N. Bernstein (1928) / D. V. Widder, *The Laplace
Transform* (1941): the completely monotone class of Theorem 2.1; J.
Frohlich, R. Israel, E. H. Lieb, and B. Simon, "Phase transitions and
reflection positivity I," Commun. Math. Phys. 62, 1 (1978): long-range RP;
A. N. Kolmogorov, *Grundbegriffe* (1933): the extension theorem of
Theorem 5.1.
