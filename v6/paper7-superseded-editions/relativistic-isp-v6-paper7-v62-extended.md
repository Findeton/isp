# Paper 7 (v6.2, extended) - SHARD: Five Gates, the Dilation Theorems, the Two Clocks, a Matter Sector, and Predictions

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
Signature and orientability from commitment, the unistochastic dilation
discharging (Q) and Gaussian (R-), the two-constants resolution with closed
forms, a commitment mass spectrum with binding defects, Lambda as state data,
and the experimental contact surface
```

## 0. Verdict

This edition supersedes Paper 7 v1. It incorporates every refinement raised
in external review, proves the dilation theorems that were previously only
named as the attack route, resolves the oldest open item on the books (the
two distinct theta constants), constructs a working toy matter sector, and
adds a predictions layer connecting the framework to existing experiments.
The claim discipline of Papers 6.1-7 is unchanged: every claim carries a
status, and "closed" always means closed at the stated scope.

```text
NEWLY CLOSED in this edition:

(Q)-existence:    DISCHARGED. Every sealed record transition law has a
                  constructive unitary (unistochastic) dilation whose
                  squared-modulus marginals reproduce it (Theorem D1).
(Q)-canonicity:   DISCHARGED AT FINITE SCOPE. The gauge-invariant content of
                  the dilation is its Bargmann loop-phase class, which is in
                  correspondence with the corpus' closed-holonomy ledger;
                  the ledger reconstructs the class (Theorem D3 + P4 s40).
Gaussian (R-):    DISCHARGED. In free record sectors the Euclidean extension
                  exists with the same generator as the Lorentzian transport
                  (Theorem D5); beta = 2*pi is unconditional there. The
                  kernel shrinks to interacting-sector reflection
                  positivity, (R-)'.
Orientability:    CLOSED. A time-orientation flip on an eventless loop is a
                  Z2 holonomy with zero record evidence - a silent seam -
                  excluded. The cone field extends globally (Theorem 3.2).
Full signature:   CLOSED. Positive screen tensor + Lorentzian normal plane
                  gives signature (1,3) (Corollary 3.3).
Two constants:    RESOLVED. The two-clocks theorem: the saturation and
                  commitment laws select coefficients of different
                  statistics; no mode can satisfy both; consumption is
                  disjoint. Closed forms: theta_hist is the real root of
                  theta^3 + theta^2 + theta = 1 (exact radical given);
                  the saturation law is D(p) = 4p(1-p). The residual fork
                  (S) - derive or demote the saturation law - is named with
                  its quantitative discriminant.
Matter mechanism: DEMONSTRATED. The commitment fixed point generates a
                  discrete mass spectrum from ledger topology: additive
                  masses for independent ledgers, binding defects for
                  coupled ones (3 m_P1 - m_C3 = 0.008438105 > 0), all H1
                  compliant. The selection of REALIZED ledgers is (M).

UPDATED KERNEL after v6.2:

(R-)'  reflection positivity of interacting record sectors
(C)    spectral convergence to 3+1 Lorentzian geometry
(S)    derive-or-demote the saturation law (the W-fork)
(M)    selection of realized matter ledgers (the spectrum/hierarchy value)
(V)    the cosmological state value (record coincidence)
```

The structural picture after this edition: the quantum representation gate
is closed at finite scope; the temperature gate is closed in the free sector
and reduced to OS positivity in the interacting sector; the geometry gates
are closed at finite scope modulo one convergence theorem; the remaining
open physics is one representation-theoretic statement, one convergence
statement, one internal law fork, and two state/sector selection problems.

## 1. Method, scope, and reproducibility

The method is unchanged (close, dissolve, or reduce-with-proof; never close
by declaration). Two scope disciplines are added in response to review:

```text
1. Machine verification scope is stated per theorem. In particular, the
   Theorem 2.2 mechanism of v1 was verified in the Gaussian sector; its
   general form is exactly OS positivity, which is the (R-)' kernel. This
   edition makes that explicit (Section 2) and then discharges the Gaussian
   case fully (Theorem D5).
2. Diagnostics require numpy, scipy, mpmath, sympy. A pure-stdlib verifier
   (code/v6_p7_stdlib_core_checks.py) reproduces the core constants, the
   cubic identity, the Sorkin cancellation, and the coupling product in any
   Python 3 environment with no dependencies.
```

## 2. Gate 1, completed to its honest boundary

The v1 chain stands: the beta-family no-go (no derived structure selects
beta), the finite transfer theorem (defect-free rotation-invariant Euclidean
record field => thermal at beta = total angle; beta_fit -> 6.283193 against
Theta = 6.283185), and the reduction (R) -> (R-). Two upgrades:

**Scope correction.** The transfer theorem's machine verification is
Gaussian. Its general form needs only reflection positivity (the transfer
operator is then positive self-adjoint and "the rotation that returns is the
trace" goes through verbatim), so the general statement is not weaker - it
IS the (R-) kernel, stated once instead of hidden.

**Theorem D5 (Gaussian discharge).** In a free (Gaussian) record sector the
Euclidean extension exists with the SAME generator as the Lorentzian boost
transport: the Euclidean correlator at beta = Theta equals the analytically
continued real-time correlator identically,

```math
C_E(\tau)\;=\;C_L(-i\tau)
\;=\;{\cosh\big(\omega(\beta/2-\tau)\big)\over2\omega\sinh(\omega\beta/2)},
```

machine-verified to 5.6e-17 at sampled points. Hence (R-) holds in the free
sector and beta = 2*pi is unconditional there. The kernel is now (R-)':
reflection positivity of interacting record sectors only. The named native
attack stands: the exchange-cocycle antisymmetry A_D = log dP_AB/dP_BA is a
reflection structure; proving its positivity for eventless interacting
sectors would finish gate 1 entirely.

**The 2*pi unification.** With Section 6 below, the constant that fixes the
modular temperature (T = 1/(2*pi)) and the constant that periodizes quantum
phase (the U(1) of retained holonomy) are one and the same native 2*pi of
the silent-seam theorem. Time's thermality and amplitude's phase share one
origin - the record-ontology form of the modular/thermal-time connection
(Connes-Rovelli).

## 3. Geometry gates, completed at finite scope

**Theorem 3.1 (signature, as in v1).** A nondegenerate normal-plane form
preserving a proper record-order cone is Lorentzian, and the transport group
is SO(1,1)+. Scope, per review: this derives signature GIVEN the form; the
form's continuum existence rides on (C).

**Theorem 3.2 (global time-orientability, new).** A time-orientation is a
continuous choice of cone component along the diamond network. The
obstruction on a loop is a Z2 holonomy (a cone-component flip). On an
eventless loop this holonomy is carried by zero record evidence: a silent
seam, excluded. Hence eventless networks are time-orientable.
Machine: defect-free loop holonomy +1; Mobius loop holonomy -1 with evidence
0.0, flagged and excluded.

**Corollary 3.3 (full signature).** The screen conductance tensor is
positive-definite (P4 s16); with the Lorentzian normal plane and global
orientation, the total signature is (1,3) with a consistent time direction.

**Gates 2b-2d** stand as in v1 (tensor source = frame-resolved coboundary
with exact seam-cancellation conservation and pressure-pair separation;
linearized focusing at O(delta^2), ratio 15.9; exact discrete Bianchi).
**Gate (C)** remains the single geometry kernel, now with signature,
orientation, source, conservation, focusing, and Bianchi all proved as
finite preconditions.

## 4. H1 as an admissibility principle

Theorem 6.1 of v1 (the source factors through the primitive RN/KL quotient;
one nat gravitates identically regardless of species) is hereby promoted
from theorem to design principle:

```text
Admissibility (EP): a matter sector is admissible only if its gravitational
coupling is quotient-functorial. Species-tagged couplings are excluded by
covariance (machine: 2.149e-01 shift under pure relabeling, rejected).
```

Every construction in Section 7 is checked against (EP). This is the
correct logical role of an equivalence principle: not an assumption about
nature, but an admissibility condition on theories - violations are not
"new physics," they are inconsistencies.

## 5. The dilation theorems

Diagnostic script:

```text
code/v6_p7d_dilation_campaign.py
```

### 5.1 (Q) unbundled

Review correctly noted that axiom (Q) of v1 bundles several statements:
Q1 existence of an additive amplitude representation; Q2 finite
dimensionality (native: capacity); Q3 continuity; Q4 commutativity (derived:
Theorem 7.4 of v1, screen-plane holonomies commute, 0.0e+00); Q5
invertibility (native: reversibility of eventless transport). Q1 was the
quantum mystery. It is now a theorem.

### 5.2 Theorem D1 (constructive unistochastic dilation): Q1 discharged

**Theorem.** Every sealed record transition law Gamma on d record atoms
admits a unitary dilation: there is a unitary U on C^{d^2} such that

```math
\sum_{a}\big|U_{(j,a),(i,0)}\big|^2=\Gamma(j\,|\,i).
```

**Proof (constructive).** Define the isometry V: C^d -> C^d (x) C^d by
V|i> = sum_j sqrt(Gamma(j|i)) |j>|i>; then V^T V = I (orthonormal ancilla
labels). Complete V's columns to a unitary U by an orthonormal basis of the
complement. The squared-modulus marginal over the output ancilla returns
Gamma by construction. ∎

Machine: isometry and unitarity gaps 1.1e-16; marginal gap 5.6e-17 on a
random 3-state law. Every record process IS representable by amplitudes:
the existence half of the quantum representation is mathematics, not
postulate. (This is the record-side face of the stochastic-quantum
correspondence; the constructive map is Stinespring/Naimark.)

### 5.3 Theorem D3 (loop phases are the retained holonomy): canonicity

A dilation is not unique; the physical question is which of its data is
real. **Theorem.** Under the record-relabeling gauge U -> D U D^dagger
(diagonal phases), the Bargmann loop products

```math
B(\ell)=\prod_{k}U_{i_{k+1}i_k}
```

are invariant (machine: 0.0e+00), and two-route interference is exactly the
loop-phase law P = |A|^2+|B|^2+2|A||B| cos(arg B(loop)) (machine gap
2.8e-17). Hence the gauge-invariant content of the dilation is its loop
class - which is precisely the corpus' closed-exchange holonomy cochain,
and Paper 4 Section 40 proves the complete ledger reconstructs that class
uniquely (Mobius inversion). ∎

**Corollary (gate 5 status).** B1 was derived in v1 (canonical U(1), period
2*pi); D1 discharges Q1; D3 plus P4 s40 ties the dilation class to the
corpus' own primitive ledger; B3 (unitarity) is automatic in the dilation;
B4-B6 follow as in Paper 5. Born is therefore DERIVED AT FINITE SCOPE,
conditional only on the corpus' founding primitive: that physical processes
are presented by their whole-history closed-holonomy ledger. The honest
physical residue is no longer a missing representation theorem; it is the
empirical thesis that nature's processes are of the indivisible class -
which is testable (Section 8).

### 5.4 Theorem D4-D5 (dilation closes the Euclidean circle in the free sector)

The dilated boost generator K is self-adjoint; e^{-theta K} exists; closing
the Euclidean evolution at any angle beta != 2*pi is a conical
representation of the state - a defect carried by no record - excluded.
In the Gaussian sector the identification "Euclidean transfer generator =
Lorentzian boost generator" is exact (Theorem D5, Section 2), so the
exclusion applies and beta = 2*pi without further axiom. In interacting
sectors the identification is the content of (R-)'.

## 6. The two clocks: resolving the oldest open item

Diagnostic script (Sections 6-7):

```text
code/v6_p7e_constants_matter_campaign.py
```

The corpus carries two selection principles for binary exponential tilts:

```math
\hbox{(saturation, P4 s5):}\quad \eta\tanh\eta-\log\cosh\eta=1-\tanh^2\eta,
\qquad \eta_{\rm evt}=1.090344354879492;
```

```math
\hbox{(commitment, P4 s71):}\quad \tanh\eta=e^{-\eta},
\qquad \eta_{\rm hist}=0.609377863436006 .
```

Both tanh values were historically denoted theta_*, a collision flagged at
first external review and unaddressed until now.

### 6.1 Two-clocks theorem

**Theorem.** (i) The two laws select coefficients of DIFFERENT statistics:
the within-diamond readout contrast q (saturation) and the across-diamond
closed-history mode chi (commitment). (ii) No single mode can satisfy both:
the residual of each law at the other's root is order one (saturation
residual at eta_hist = -0.548293; commitment residual at eta_evt =
+0.460903), and each law has a unique positive root by strict monotonicity.
(iii) Consumption is disjoint: the gravity source amplitude consumes only
W_evt = 1 - tanh^2(eta_evt); the whole-history law consumes only h =
eta_hist-type coefficients. There is no inconsistency; there was a notation
collision, repaired as theta_evt vs theta_hist. ∎

### 6.2 Closed forms (new)

**Theorem.** theta_hist is algebraic: substituting x = e^{-eta} into the
commitment law gives

```math
\theta^3+\theta^2+\theta=1,
\qquad
\theta_{\rm hist}
=-{1\over3}-{2\over3\,(17+3\sqrt{33})^{1/3}}+{(17+3\sqrt{33})^{1/3}\over3}
=0.543689012692076,
```

with eta_hist = -log theta_hist (machine gap 1.1e-16). The saturation law,
rewritten with p = (1+tanh eta)/2, is exactly

```math
\log 2-H(p)\;=\;4p(1-p):
```

the event's committed evidence equals its outcome variance (both sides
0.364784952089976 at the root). The history constant is a cubic irrational;
the event constant is transcendental-form. ∎

### 6.3 Unification attacks and the (S) fork

Four natural derivations of the saturation law from the commitment law were
attempted and each FAILS with order-one residual (machine: 0.59, 0.49, 0.46,
0.21 for the four attacks listed in the diagnostic). The saturation law is
therefore an independent postulate of the readout family. The corpus' own
enriched-RN campaign (P4 s28-29: "the old idempotent constants drift" when
the primitive is enriched) already hinted at its non-fundamental status.
This fixes the kernel item:

```text
(S) derive-or-demote: either derive the saturation law from the whole
    sealed process (status of the event constant: law), or demote it and
    re-anchor the deletion-work amplitude to the history family (status:
    convention of the binary readout).
```

The fork is quantitatively discriminating inside the theory:

```math
W_{\rm evt}=0.364784952089976
\quad\hbox{vs}\quad
W_{\rm hist}=D(\eta_{\rm hist})=0.156109200157240,
```

a factor 2.336729 in gravitational work per primitive event - an internal
falsifier for whichever branch a future derivation selects.

## 7. A matter sector

The commitment law is species-independent; ledgers are not. A matter
species is a record ledger type; its mass is its evidence:

```math
\hat m \;=\; \hbox{committed RN evidence per primitive cycle}
\;=\;D\!\left(P_{h}\,\Vert\,U\right)\ \hbox{nats},
```

with h the commitment fixed point of that ledger (modular energy is then
T x evidence rate, T = 1/(2*pi)). This single definition, applied to the
corpus' own ledgers, generates a spectrum:

| species | ledger | m_hat (nats/cycle) | note |
|---|---|---:|---|
| P1 | one parity mode | 0.156109200157240 | the history constant itself |
| P2 | two independent parity modes | 0.312218400314480 | exact additivity |
| C3 | coupled (x, y, xy) ledger | 0.459889495499429 | h = 0.495053264 |

**Theorem 7.1 (additivity).** Independent ledgers glue to product laws with
additive evidence (the P4 s71 chain rule), so masses of non-interacting
composites add exactly. ∎

**Theorem 7.2 (binding defect).** Coupling produces a mass defect: for the
coupled three-mode ledger,

```math
3\,\hat m_{P1}-\hat m_{C3}=0.008438105>0:
```

the bound ledger is lighter than its free constituents. Binding energy is a
theorem of the commitment fixed point, not an added mechanism. ∎

**(EP) compliance.** Per-nat gravitational response is identical across all
species (machine 0.0e+00); per-event responses differ exactly by mass, as
they must. Mass ratios are intrinsic, lambda-invariant, and computable:
m(C3)/m(P1) = 2.945947420.

**What this does and does not establish.** It establishes that (M) is
well-posed and generative: the commitment law converts ledger topology into
a discrete spectrum with additivity and binding for free. It does not
select which ledgers nature realizes - that selection IS (M), the record
form of the mass-generation/hierarchy problem, and remains OPEN. One honest
direction (not a claim): high-dimensional ledgers with weakly selected
modes sit near the uniform base and are naturally light in capacity units,
which is the right qualitative sign for a hierarchy.

## 8. Predictions and experimental contact

Graded by epistemic class.

**Class A - existing experiments the framework must and does pass.**

```text
A1. Triple-slit / Sorkin parameter. Quadratic weights give exactly
    kappa_3 = 0 (machine: +0.0e+00), while p != 2 norms violate it
    (p=1.5: +1.0e-01; p=3: -1.9e-01). The Sinha et al. bound on
    third-order interference is therefore a DIRECT experimental test of
    the p=2 selection theorem - passed.
A2. Equivalence-principle tests. H1 is exact: no composition-dependent
    coupling from the record sector. Eot-Wash-class bounds are satisfied
    identically; any admissible future matter sector inherits this.
A3. Quaternionic interference searches. Excluded by theorem (abelian
    screen holonomy); null results are predicted exactly.
```

**Class B - sharp functional laws, QM-coincident where tested,
discriminating in form.**

```text
B1. Duality law. Visibility = no-division survival through which-path
    record evidence with the Bhattacharyya clock:
        V = sum_x sqrt(p0(x) p1(x)) = exp(-I_B).
    This satisfies V^2 + D^2 <= 1 identically (Fuchs-van de Graaf;
    machine: 0 violations in 20000 trials) - wave-particle duality is
    DERIVED as a record-overlap inequality - and reproduces QM exactly
    for real-Gaussian pointers (gap 5.6e-17). Deviation channel: pointer
    records whose quantum overlap is not the classical Bhattacharyya
    coefficient (complex pointer structure); there SHARD's law and
    textbook QM can be distinguished.
B2. Indivisibility witnesses. Visible event statistics fail first-order
    Markovianity with computable gaps (P4 s10: 0.130069 in the two-diamond
    toy); CP-divisibility violation witnesses in engineered open systems
    are the laboratory handle.
```

**Class C - internal falsifiers and structural signatures.**

```text
C1. The W-fork (Section 6.3): factor 2.336729 in deletion work per event
    discriminates the saturation branch from the history branch.
C2. The 2*pi unification: phase period and inverse modular temperature are
    one constant; frameworks that decouple them differ from SHARD in
    principle.
C3. Mass additivity with binding defects of computable sign and size for
    coupled ledgers (0.008438105 in the toy): the qualitative signature
    that composite masses are sub-additive, with the defect set by ledger
    coupling.
C4. Lambda as state data: the cosmological term may differ between sealed
    epochs/packets while all law couplings are fixed - in-principle
    distinguishable from a constant-Lambda law (effective w(z) departures);
    direction only, no value claimed (kernel V).
C5. Capacity quantization: record entropy changes in ledger quanta; a
    horizon-spectrum discreteness signature in principle, contingent on
    (C) and (M).
```

## 9. Lambda

Unchanged from v1 and restated for completeness: the trace part of the raw
deletion source enters exactly as a cosmological term; sealed solvability
forces Lambda_hat = kappa_hat x mean commitment density (0.859504294 sparse,
1.719008588 dense; residual at the identity 1.0e-15, at half value 0.43);
state data, not a law coupling; the coincidence value is kernel (V).

## 10. The kernel after v6.2

```text
(R-)'  reflection positivity of INTERACTING record sectors (free sector:
       discharged by D5). Attack: positivity of the exchange-cocycle
       reflection; the dilation now supplies the operator framework.
(C)    spectral convergence of controlled refinements to (1,3) geometry,
       with signature, orientation, source, conservation, focusing, and
       Bianchi all proved as finite preconditions.
(S)    derive-or-demote the saturation law; discriminant factor 2.336729.
(M)    selection of realized ledgers (the spectrum value within the proved
       bound m_hat <= cell capacity and the proved mechanism of Section 7).
(V)    the cosmological state value.
```

Structural notes: the former two-for-one ((R-) and (Q) sharing one
construction) has CASHED OUT - the dilation killed (Q) entirely and the
free-sector half of (R-). The remaining kernel splits cleanly into one
analysis theorem ((R-)'), one convergence theorem ((C)), one internal law
question ((S)), and two selection problems ((M),(V)) that belong to states
and sectors, not to the gravitational or quantum law.

## 11. What this paper proves and does not prove

Proves, with machine verification at the printed values: Theorems D1, D3,
D5 (dilation existence, loop-holonomy canonicity, Gaussian Euclidean
discharge); Theorems 3.2-3.3 (orientability, (1,3) signature); the
two-clocks theorem with both closed forms and the four-attack no-go scan;
Theorems 7.1-7.2 (mass additivity, binding defect) and the spectrum table;
the Sorkin cancellation and its p != 2 violation; the duality inequality
and the exact Gaussian-pointer match; (EP) compliance of the matter sector;
the stdlib reproducibility of the core constants.

Does not prove: (R-)', (C), (S), (M), (V). Of these, (S) is plausibly
closable with corpus technology (it is one variational question); (R-)' and
(C) are hard mathematics with their frameworks now in place; (M) and (V)
are the genuine physics frontier and are exactly where the frontier sits in
every other program. Claiming them would be declaration, not derivation.

## 12. Status

```text
Quantum representation: CLOSED at finite scope (D1 + D3 + P4 s40 + P5 Born
                        machinery); residue = the indivisible-class
                        empirical thesis, testable (A1, B2).
Temperature:            CLOSED in free sectors (D5); (R-)' for interacting.
Geometry:               signature, orientation, (1,3), source,
                        conservation, focusing, Bianchi all CLOSED finite;
                        kernel (C).
Equivalence principle:  CLOSED and promoted to admissibility (EP).
Constants:              two-clocks RESOLVED; theta_hist = root of
                        theta^3+theta^2+theta=1 (exact radical);
                        saturation = "evidence equals variance",
                        D(p)=4p(1-p); fork (S) named with discriminant.
Matter:                 mechanism DEMONSTRATED (additivity, binding
                        defects, spectrum ratios); selection = (M).
Lambda:                 state datum; value = (V).
Experiment:             contact surface established: triple-slit (passed),
                        EP (passed), quaternion nulls (predicted), duality
                        law (QM-coincident, deviation channel named),
                        indivisibility witnesses (handle named).
```

## References and literature map

- Papers 4-7 v1 (internal): the commitment law and chain rule (P4 s71),
  the exchange cocycle (P4 s34), closed-holonomy Mobius reconstruction
  (P4 s40), enriched-RN constant drift (P4 s28-29), the Born machinery
  (P5 s3), gates and kernels (P6-P7).
- J. A. Barandes, the stochastic-quantum correspondence and theorem
  (`https://arxiv.org/abs/2302.10778`, `https://arxiv.org/abs/2309.03085`):
  Theorem D1 is the record-side constructive face of the correspondence;
  the indivisible-class thesis is the residual empirical content.
- W. F. Stinespring, "Positive functions on C*-algebras," Proc. AMS 6, 211
  (1955); M. A. Naimark dilation: the construction behind D1.
- V. Bargmann, "Note on Wigner's theorem," J. Math. Phys. 5, 862 (1964);
  S. Pancharatnam (1956): loop-phase invariants behind D3.
- R. D. Sorkin, "Quantum mechanics as quantum measure theory," Mod. Phys.
  Lett. A 9, 3119 (1994); U. Sinha, C. Couteau, T. Jennewein, R. Laflamme,
  and G. Weihs, "Ruling out multi-order interference in quantum mechanics,"
  Science 329, 418 (2010): the kappa_3 test of A1.
- C. A. Fuchs and J. van de Graaf, "Cryptographic distinguishability
  measures," IEEE Trans. Inf. Theory 45, 1216 (1999); B.-G. Englert,
  "Fringe visibility and which-way information," PRL 77, 2154 (1996): the
  duality inequality of B1.
- A. Connes and C. Rovelli, "Von Neumann algebra automorphisms and
  time-thermodynamics relation," Class. Quantum Grav. 11, 2899 (1994): the
  thermal-time reading of the 2*pi unification.
- K. Osterwalder and R. Schrader (1973): the (R-)' kernel. S. L. Adler
  (1995), M. P. Soler (1995): the excluded rivals. E. C. Zeeman (1964),
  D. Malament (1977): the order-to-Lorentz tradition. S. Weinberg (1989),
  M. Henneaux and C. Teitelboim (1989): the Lambda classification.
  Jacobson, Unruh, Bisognano-Wichmann, Pusz-Woronowicz, Lenard, Dicke,
  Duff-Okun-Veneziano, Regge, Frobenius/Gelfand-Mazur: as in Papers 6-7.
