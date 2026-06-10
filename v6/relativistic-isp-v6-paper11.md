# Paper 11 (v6) - SHARD: The Reconstruction Layer and Record-Pauli

Author: Felix Robles Elvira

Subtitle:

```text
The infinite-dimensional ledger reconstruction (the L3 residue): reflection
positivity passes to projective limits, the Gaussian tower reconstructs the
oscillator spectrum, the unbounded position operator with its ladder and
selection rules, and the WEYL ALGEBRA - the canonical commutation relations
recovered from finite record truncations against exact continuum targets,
landing by Stone-von Neumann on the Schrodinger representation; dilation
towers cohere projectively, and the imported unbounded Naimark/Stinespring
machinery completes them on the tame class.  And the capstone: record-Pauli
at the reconstructed layer - sealed positivity on the exchange collar
FORCES statistics = (-1)^{2m}, Pauli exclusion appears as a derived exact
zero, the wrong sector joins the signed/driven failure class of Papers 8
and 10, and axiom (X) reduces to its association clause alone
```

This paper executes the L3 reconstruction residue (Paper 7 Section 7.4;
existence half closed by Paper 7 Theorem 7.5) and the D9b record-Pauli
campaign (Paper 9 Section 11, wired by Paper 10 to the positivity layer).
The two belong together: Part I builds the bridge from finite ledgers to
continuum operator structure; Part II walks the first physics question
across it.

## 0. Verdict

```text
PART I (L3: the reconstruction half).  CLOSED AT TAME SCOPE.

 T1 (RP passes to limits): every Gram entry of a limit is a limit of
    entries of PSD matrices, and the PSD cone is closed: reflection
    positivity survives pointwise limits of correlations.  COROLLARY:
    any sector APPROXIMABLE by eventless finitely-presented sectors is
    RP - O6 sharpens to "sectors not even approximable."  (Machine:
    binned towers d = 20..160, worst Hankel min eig -1.6e-18.)
 T2/T3 (the Gaussian tower): from binned record data of the free collar
    (the Mehler kernel of P7 D5), the tower reconstructs:
      spectrum: all gap errors at MACHINE FLOOR (<= 7e-15) from d = 40;
      the unbounded position operator: ladder elements <n|x|n+1> equal
      to sqrt((n+1)/2) to 4e-15 (n <= 4), 5e-9 (n = 10); off-ladder
      elements <= 1.8e-14 (SELECTION RULES emerge); sqrt(n) growth
      witnessed (|<20|x|21>|/|<0|x|1>| = 4.5711 vs sqrt(21) = 4.5826):
      the operator is genuinely unbounded in the limit.
 T4 (the Weyl algebra): with P = i[H, X] built from reconstructed
    pieces, the characteristic function matches the EXACT continuum
    answer at machine precision (<0|e^{isX}|0> vs e^{-s^2/4}: 1e-15 at
    every level), and the Weyl group commutator converges to the CCR:
      ||e^{isX} e^{irP} e^{-isX} e^{-irP} - e^{-isr}|| (6x6 block):
      7.0e-02 (K=12) -> 4.5e-11 (K=24) -> 7.2e-11 (K=36, floor).
    By Stone-von Neumann, the reconstructed Weyl pair is unitarily
    equivalent to the Schrodinger representation: the tower lands on
    THE continuum quantum kinematics, not merely on some Hilbert space.
 T5 (dilation towers): every level carries its exact D1 dilation
    (isometry and law-reproduction gaps <= 4.4e-16), and the levels
    cohere projectively (coarse stationary law = block-summed fine law
    to 1.2e-15): the inductive system exists; the imported unbounded
    Naimark/Stinespring theory with Nelson/Kato self-adjointness
    criteria completes it on the TAME class (uniformly controlled
    towers; the Gaussian benchmark is the worked instance).

PART II (D9b: record-Pauli).  RESOLVED, CONDITIONAL ON ASSOCIATION.

 THEOREM (record-Pauli): on the sealed exchange collar - which closes
    with E = (-1)^{2m} SWAP by the frame-winding theorem, GIVEN that the
    fiber is associated to the frame bundle (D9a) - positivity of sealed
    spectral weights FORCES the physical sector to be Fix(E):
      m = 0:   symmetric weights all >= 0; antisymmetric all NEGATIVE;
      m = 1/2: symmetric all NEGATIVE (min -1.0); antisym all >= 0.
    Statistics = (-1)^{2m} is now a POSITIVITY THEOREM, not a
    single-valuedness postulate.
 Pauli exclusion DERIVED: in the forced half-integer sector the
    coincidence probability is an exact zero (machine 0.00e+00) - not
    imposed, computed from the sealed collar.
 The wrong sector is SIGNED: its unprojected twisted correlations fail
    the moment test (Hankel min eig -2.33), placing wrong statistics in
    the same exclusion class as the driven sectors of Paper 10 and the
    non-moment sectors of Paper 8; projection onto Fix(E) restores
    positivity (-3.7e-31).
 AXIOM (X) REDUCED: its single-valuedness clause is replaced by this
    theorem; what remains of (X) is the association clause alone (D9a).
    Fermions in SHARD: available (P9), positivity-rigid (here); FORCED
    awaits only D9a.

PART III (the joint frontier campaigns; Section 4).

 D9a DISCHARGED (4.1): the exchange motion is eventless transport, its
    fiber action lives on open path segments (a connection, not loop
    data), and the no-silent-circulation principle - the theorem of
    P4 s20 - excludes any twist beyond the frame-winding representation
    (sealed positivity first quantizes the freedom to Z2; the silent pi
    is excluded; a record-sourced pi is driving, not eventlessness).
    E = (-1)^{2m} SWAP is DERIVED.  The chain winding -> association ->
    sector closes: STATISTICS = (-1)^{2m} IS A THEOREM OF EVENTLESS
    RECORD TRANSPORT.  Axiom (X): DISCHARGED at stated scope (premise
    ledger named).  FERMIONS IN SHARD: FORCED.
 THE FERMIONIC CAR TOWER (4.2): record presentations are positive
    exactly where JW strings are trivial; the Fock spectrum, binomial
    multiplicities, CAR algebra (8.9e-16), and the quadratic
    Hamiltonian (2.4e-15, non-circular) are reconstructed from sealed
    record data; the 1d record-GW dispersion is recovered bottom-up
    (curve gap 0.146 -> 0.0006): L3 extends to fermionic tame sectors,
    and the reconstruction tower meets the record-RG fixed point.
 THE SIGMA-CIRCLE CLOSED (4.3): even-time positivity (reversible =>
    C(2r) >= 0, a two-line theorem) + C_tw(2) = -0.0168 < 0 prove that
    EVERY presentation of the wrong-statistics sector is driven: wrong
    statistics is a hidden current, with its measured entropy price
    (sigma >= 0.23 / 0.67 / 1.67 at violations 0.05 / 0.15 / 0.30).
    O11 audit: the linear-law constant DECREASES with block length
    (0.049 -> 0.021): the law is uniform-in-L with the small-L constant;
    per-family leading-order constants computed exactly (ratios within
    0.5%): O11 reduced to third-order remainder control.
 PROCESS-LEVEL O6 LOCATED (4.4): non-Markov yet process-RP observable
    processes exist (hidden reversibility suffices); the OS
    reconstruction recovers the hidden reversible transfer exactly
    (1.2e-11); infinite-memory cylinder laws are approximable (gaps
    0.129 -> 0.0018); driven hidden chains fail process-RP: the
    boundary is the arrow, and the general statement is identified as
    the POSITIVE-REALIZATION problem (named, literature-anchored).
```

## 1. Method and reproducibility

```text
code/v6_p11a_ledger_reconstruction_campaign.py   Part I (T1-T5)
code/v6_p11b_record_pauli_campaign.py            Part II
code/v6_p11c_association_campaign.py             Part III: D9a discharged
code/v6_p11d_fermionic_tower_campaign.py         Part III: CAR tower + GW
code/v6_p11e_sigma_circle_campaign.py            Part III: sigma-circle, O11
code/v6_p11f_process_o6_campaign.py              Part III: process-O6
```

Scope discipline: Part I's claims are theorems on the tame class with
classical imports named (Naimark 1940/Stinespring 1955 for dilations;
Nelson/Kato for self-adjointness; Stone-von Neumann for uniqueness);
Part II's theorem is conditional on association (D9a) and says so in its
statement.  What Part I does NOT touch: fields and Poincare structure
(that is (C)); the interacting continuum (O6); the empirical completeness
thesis (L1/L2 of Paper 7 Section 7.4, which remains empirical).

## 2. Part I: the reconstruction layer

### 2.1 What is to be reconstructed

Paper 7 closed the EXISTENCE half of L3: the infinite whole-history law
exists as a Kolmogorov projective limit (P7 Theorem 7.5).  The residue
was reconstruction: when the alphabet/history space is infinite and the
operators unbounded, does the finite machinery - the D1 dilation, the
loop-class ledger (P4 s40), the OS construction - converge to a
continuum Hilbert/operator structure?  Paper 10 supplied the missing
foundation: OS positivity is now a THEOREM for eventless
finitely-presented sectors, so the reconstruction has a derived floor.

### 2.2 Reflection positivity passes to limits (T1)

**Theorem T1.** Let correlations C_d converge pointwise to C as the
refinement tower deepens, with every C_d reflection positive.  Then C is
reflection positive.  **Proof.** Each finite Gram matrix of C is the
entrywise limit of the corresponding PSD Gram matrices of C_d; the PSD
cone is closed. ∎

**Corollary (O6 sharpened).** Any sector approximable in correlations by
eventless finitely-presented sectors is reflection positive.  The honest
residue of (R-)''' is therefore reduced again: from "no finite primitive
presentation" (Paper 10) to "NOT EVEN APPROXIMABLE by eventless
presentations."  (Machine: the binned Gaussian towers d = 20..160 give
worst site-Hankel min eigenvalue -1.6e-18 at every level and in the
pointwise limit.)

### 2.3 The Gaussian tower: spectrum, ladder, unboundedness (T2/T3)

The free record collar (P7 D5) has transfer kernel the Mehler kernel;
binning it at resolution d gives a finite record law - pure ledger data.
Reconstruction receipts (omega = 1, tau = 0.4):

```text
spectrum (gap errors vs omega):
   d = 20:  1.9e-04 .. 3.3e-03
   d = 40:  <= 4.9e-15      d = 80, 160: <= 7.3e-15   (machine floor)

position operator in the reconstructed eigenbasis (d = 160):
   |<n|x|n+1>| vs sqrt((n+1)/2):  n = 0..4: errors <= 4.0e-15;
   n = 10: 5.1e-09;  n = 20: 8.1e-03 (resolution edge, converging)
   max off-ladder element (|n-m| != 1, n,m < 8): 1.8e-14
   growth |<20|x|21>| / |<0|x|1>| = 4.5711  (sqrt(21) = 4.5826)
```

Three structures emerge from record data alone: the harmonic spectrum,
the LADDER with its exact matrix elements, and the SELECTION RULES
(off-ladder elements vanish) - and the sqrt(n) growth of the ladder
witnesses genuine unboundedness: the reconstructed operator has no
bounded extension in the limit.  This is the L3 claim in miniature, with
rates.

### 2.4 The Weyl algebra reconstructed (T4)

Define, entirely from reconstructed pieces, H = diag(E_n) and
P = i[H, X] (the Heisenberg relation at omega = 1; ladder check:
| |<0|P|1>| - sqrt(1/2) | = 3.3e-16).  Then:

```text
characteristic function vs the EXACT continuum answer:
   |<0|e^{isX}|0> - e^{-s^2/4}| <= 1.3e-15 at every tower level (s = 1.3)
the CCR via the Weyl group commutator (s = 1.3, r = 0.9):
   ||e^{isX} e^{irP} e^{-isX} e^{-irP} - e^{-isr} I||  (6x6 block):
   (d, K) = (40, 12): 7.0e-02    (80, 24): 4.5e-11    (160, 36): 7.2e-11
Bargmann-loop gauge invariance of the reconstructed unitaries: 4.2e-17
```

The canonical commutation relations - the continuum quantum kinematics -
are recovered from finite ledger truncations, against exact
infinite-dimensional targets, with quantified convergence in the number
of resolved levels.  **By the Stone-von Neumann theorem, the
reconstructed Weyl pair is unitarily equivalent to the Schrodinger
representation**: the tower does not land on "a" Hilbert space; it lands
on the continuum quantum theory.  And the loop-class machinery (P7 D3)
rides along: the Bargmann invariants of the reconstructed unitaries are
gauge-invariant at every level.

### 2.5 Dilation towers and the tame class (T5)

At every truncation level the P7 D1 dilation exists and is exact
(isometry gap <= 4.4e-16; law reproduction 2.8e-17), and the levels
cohere: block coarse-graining of the fine law has stationary measure
equal to the block-summed fine stationary measure (gaps <= 1.2e-15) -
the projective consistency of P7 Theorem 7.5, realized on an explicit
operator tower.  The inductive system of dilations therefore exists; the
classical unbounded Naimark/Stinespring theory completes it to a
separable-Hilbert-space dilation, with self-adjointness of the limit
generators supplied by Nelson/Kato criteria on the TAME class:

```text
TAME: towers with uniformly controlled generators (the Gaussian/free
sectors exactly; any tower whose resolved-level energies and transition
amplitudes converge with the rates demonstrated above).
```

Honest residues: essential self-adjointness BEYOND the tame class (named
O10); sectors not approximable at all (= the sharpened O6); and the
completeness thesis (L1/L2), which no amount of reconstruction can
settle because it is empirical.

### 2.6 What is now reconstructed, and what is not

Reconstructed at tame scope, from ledger data: a separable Hilbert
space; an unbounded self-adjoint generator with the correct spectrum;
the unbounded position operator with ladder and selection rules; the
Weyl/CCR algebra, hence (Stone-von Neumann) the Schrodinger
representation; gauge-invariant loop classes; coherent dilation towers.
NOT reconstructed (and not claimed): quantum fields and Poincare
representations - that requires the (C) geometry; the interacting
continuum (O6); any selection of which sectors nature instantiates (M).

## 3. Part II: record-Pauli at the reconstructed layer

### 3.1 The exchange collar

For an identical pair of cells, one period of the identified pair collar
is one exchange (the frame-winding theorem, P9 7.1).  GIVEN association
(D9a: the fiber of a weight-m species is carried by the frame bundle),
the collar closes with the framed-exchange operator

```math
E\;=\;e^{2\pi i m}\,{\rm SWAP}\;=\;(-1)^{2m}\,{\rm SWAP}.
```

The per-period pair transfer is PSD without loss of generality: by the
site-RP structure (v6.3), T^2 is PSD for every reversible slice
transfer, so the per-period transfer can be taken PSD.

### 3.2 The record-Pauli theorem

**Theorem (record-Pauli, conditional on association).** On the exchange
collar, the sealed spectral weight of a pair mode v with transfer
eigenvalue lambda is lambda^M <v|E|v>.  Positivity of all sealed weights
forces the physical sector to be Fix(E):

```text
m = 0:    sym weights (6): min +1.9e-11, all >= 0;
          antisym (3): min -1.4e-05, ALL NEGATIVE  -> BOSONIC forced.
m = 1/2:  sym weights (6): min -1.00e+00, ALL NEGATIVE;
          antisym (3): min +6.0e-11, all >= 0      -> FERMIONIC forced.
```

Statistics = (-1)^{2m}: the spin-statistics connection is a POSITIVITY
theorem on the sealed collar - the same exclusion family that killed
split-signature phases (negative event weights, P7 Theorem 7.6) and
silent arrows (P10 T3). ∎

This is the record form of Pauli's own argument: his 1940 proof also
runs on positivity (of energy and norms); here the positive object is
the sealed record law itself.

### 3.3 Exclusion derived; the wrong sector is signed

```text
coincidence probability P(a = b):
  forced half-integer sector: 0.00e+00  - PAULI EXCLUSION as an exact
     zero, DERIVED from the sealed collar, not imposed;
  forced integer sector: 0.342986 > 0 (occupancy allowed; the sharp
     bunching law is P9 Section 8).
the wrong sector: unprojected half-integer twisted correlations have
  site-Hankel min eig -2.33 (SIGNED: fails the moment test - the
  driven/non-moment failure class of Papers 8 and 10); projecting onto
  Fix(E) restores positivity (-3.7e-31).
```

The convergence of three exclusion mechanisms is the structural point:
wrong statistics = negative sealed weights = signed correlations = the
non-moment class.  Statistics, orientation (P8), and the arrow (P10) are
all policed by one principle - sealed positivity.

### 3.4 What this does to axiom (X)

Paper 9's (X) had two clauses: (i) the exchange operator is the framed
transport (association), and (ii) physical states are single-valued
under it (sector selection).  Clause (ii) is now a THEOREM - positivity
selects Fix(E) - so:

```text
(X) REDUCED: the entire spin-statistics load now rests on the
association clause D9a alone.  Fermions in SHARD: AVAILABLE (P9) +
POSITIVITY-RIGID (this paper); FORCED awaits only the derivation that a
weight-m fiber's transport is tied to the frame bundle.
```

**[Part III update: that derivation now exists - Section 4.1 discharges
D9a from the no-silent-circulation theorem of P4 s20, and (X) is gone.]**

The kinematic no-go of P9 7.3 survives in exactly one form: a fiber
that decouples from frames entirely (effective weight zero) can carry
either statistics consistently.  For a fiber that genuinely spins, the
wrong statistics is no longer merely unaesthetic - it is excluded.

## 4. Part III: the joint frontier campaigns

This part executes the five advancement routes identified in the joint
Paper 10/11 review, with four new diagnostics:

```text
code/v6_p11c_association_campaign.py       D9a discharged
code/v6_p11d_fermionic_tower_campaign.py   the fermionic CAR tower + GW
code/v6_p11e_sigma_circle_campaign.py      the sigma-circle, O11 audit
code/v6_p11f_process_o6_campaign.py        process-level O6
```

### 4.1 D9a DISCHARGED: association from no-silent-circulation

The last open clause of axiom (X) falls to a theorem the corpus already
owned.  Paper 4 Section 20 proves the eventless inter-screen connection
is UNIQUE - the least-record-work, no-silent-circulation transport -
and states the principle in exactly the needed form: "nonzero twist =
exchange-defect holonomy source, not a free connection."

**Theorem (association).** The exchange motion of an identical pair is
eventless transport, and its fiber action is defined on OPEN path
segments (records evolve along the motion): it is a connection, not free
loop data.  By the no-silent-circulation principle instantiated on the
pair fiber, the connection carries no oriented circulation beyond what
the record geometry sources; the only geometric source on the exchange
path is the relative frame winding (P9 Theorem 7.1).  An independent
twist is therefore either silent (excluded) or record-sourced (an
exchange-defect source carrying evidence: the sector is driven, not
eventless - P10 Part I).  Hence the exchange twist IS the frame-winding
representation:

```math
E\;=\;(-1)^{2m}\,{\rm SWAP},\qquad\hbox{DERIVED.}
```

Machine receipts: (R1) the Frobenius orthogonality and least-work
uniqueness of the zero-circulation connection (the P4 s20 mechanism,
instantiated: <S,A> = 0.0e+00, W(a) = W0 + a^2 ||A||^2); (R2) sealed
positivity QUANTIZES any extra twist to Z2 before any exclusion acts
(sealed weights are real only at a in {0, pi} - independently recovering
the spin quantization of P9 s6); (R3) the surviving pi is an oriented
circulation sourced by no record-geometric datum (relative record work
9.87 vs 0): silent, excluded. ∎

**The closed chain.** Frame winding (P9 7.1, proved) -> association
(here) -> sector forcing (Part II, proved):

```text
STATISTICS = (-1)^{2m} IS A THEOREM OF EVENTLESS RECORD TRANSPORT.
Axiom (X): DISCHARGED at the stated scope.  FERMIONS IN SHARD: FORCED.
```

(Machine, end to end with the DERIVED closing operator: m = 0 forces the
symmetric sector; m = 1/2 forces the antisymmetric sector with
P(coincident records) = 0.00e+00 - Pauli, derived.)  Premise ledger,
stated for the referee: P1 - the exchange motion between commitments is
eventless transport (architecture); P2 - the no-silent-circulation
principle applies to every fiber the transport carries (its screen
instance is the P4 s20 theorem; the internal-fiber instance is an
identification, the single contestable step, named); P3 - sealed
positivity (P7 7.6 family).  Nothing else is consumed.

### 4.2 The fermionic CAR tower, and the GW bridge

The fermionic mirror of Part I, with three receipts:

```text
(i)  PRESENTATION: the fermionic record transfer is entrywise positive
     exactly where the Jordan-Wigner strings are trivial - open NN
     chain: min entry +0.000000 (positive); ring (wraparound string):
     min entry -0.952 (signed).  The fermion sign problem is the
     record statement "wrong presentation," aligned with Part II's
     signed wrong-statistics sectors.
(ii) THE CAR TOWER (open chain, L = 6): the reconstructed many-body
     record spectrum equals the fermionic Fock subset-sums EXACTLY
     (max gap 7.6e-15 over all 64 levels; binomial multiplicities
     [1,6,15,20,15,6,1] - fermionic, not bosonic); single-particle
     energies extracted from the ONE-PARTICLE record sector match to
     8.3e-16; CAR on the record space exact ({a_i,a_j+} - delta:
     8.9e-16); and the quadratic Hamiltonian rebuilt from the
     reconstructed energies reproduces the record transfer to 2.4e-15
     (non-circular).  The anticommuting continuum kinematics is
     recovered from ledger data - the fermionic mirror of Part I's
     CCR receipt.
(iii) THE GW BRIDGE: the 1d blocked record Dirac operator satisfies
     the GW relation analytically (machine residual 4.4e-16) with the
     correct cone (slope 0.9999), and its dispersion is recovered from
     the sealed spectrum of a positive fermionic record sector along a
     mode-refinement tower (curve gap 0.146 -> 0.0006 over K = 8 ->
     32): the bottom-up L3 reconstruction and the top-down record-RG
     fixed point of Paper 10 Section 4.5 are two faces of one object.
```

L3 is thereby extended to fermionic tame sectors.

### 4.3 The sigma-circle closed, and the O11 audit

**Theorem E1 (even-time positivity).** For any reversible transport and
any observable, C(2r) = ||T^r (f - <f>)||^2 >= 0 in L^2(pi). ∎
(Machine: 300 random reversible transports, min even autocorrelation
0.0e+00.)

The wrong-statistics sector of Part II has C_tw(2) = -0.0168 < 0; by E1
and P10 T3 (contrapositive), EVERY finite presentation of it is driven:
**wrong statistics is a hidden current**, exactly as Paper 10 Section 5
promised - now by theorem, not by wiring.  The explicit driven witness
is Paper 10's unicycle (C(2) = -6.2e-2 at sigma = 0.519713), and the
PRICE CURVE is measured: achieving an even-time violation
-C(2)/C(0) >= x costs at least

```text
x = 0.05: sigma >= 0.23     x = 0.15: sigma >= 0.67     x = 0.30: sigma >= 1.67
```

(minima over 4000 random driven transports per x): the statistics defect
is paid for in arrow evidence, quantitatively.

**O11 audit (the untested assumption of P10 4.1, resolved favorably).**
The linear-law constant at block lengths L = 2, 3, 4 is C(L) = 0.049,
0.036, 0.021: it DECREASES with block length, so the small-L constant is
conservative and the law is uniform-in-L as audited.  And the
leading-order constant is now computed exactly per family from two
Hessian ratios: C_an = defect''(0)/sigma''(0) = 0.0355, 0.0414, 0.0404
on three families, bounding the finite-driving ratio to within 0.5%:
O11 is reduced to third-order remainder control.

### 4.4 Process-level O6: located, and its boundary is the arrow

```text
F1: the observable process of a hidden reversible chain is genuinely
    NON-Markov (order-2 memory gap 0.0174) yet PROCESS-RP (observable
    OS Gram min eig -1.3e-17): reflection positivity does not require
    Markovianity - hidden reversibility suffices.
F2: the record data DETERMINE the reversible presentation: the
    observable OS Gram has rank = hidden dimension (4), and the
    OS-reconstructed transfer spectrum equals the hidden reversible
    spectrum to 1.2e-11.
F3: infinite memory is approximable: the continuous-spectrum reversible
    process (binned-oscillator hidden chain, 2-symbol observable) has
    its length-3 cylinder probabilities reproduced by compressed finite
    reversible presentations with gaps 0.129 -> 0.0018 (d = 4 -> 32).
F4: the driven hidden chain FAILS process-RP (observable Gram min eig
    -1.6e-02): the process-level boundary is the eventlessness boundary,
    again.
```

STATUS: process-O6 is the statement "every stationary process-RP law is
the weak limit of finite hidden-REVERSIBLE presentations" - verified on
the accessible classes above, with its general form identified as the
POSITIVE-REALIZATION problem of stochastic systems theory (Jaeger's
observable operator models; Benvenuti-Farina; Vidyasagar).  The thermal
kernel's final mathematical identity is now a named, literature-anchored
problem rather than an unshaped residue.

## 5. The kernel after Paper 11

```text
L3:      reconstruction half CLOSED AT TAME SCOPE (Part I): Hilbert
         space, unbounded generators, ladder/selection rules, Weyl/CCR
         (hence Schrodinger representation), loop classes, dilation
         towers - all as limits of ledger data with rates.  Residues:
         O10 (beyond-tame self-adjointness); the empirical completeness
         thesis (unchanged, L1/L2).
(R-)'''/O6: sharpened by T1 to "not even approximable"; CLOSED at the
         single-observable level by Paper 10 Part III (with T1); located
         at the process level by Part III here (4.4): the residue is the
         positive-realization question, named and literature-anchored.
D9:      D9b RESOLVED conditionally (Part II), and the condition itself
         - D9a - is DISCHARGED in Part III (4.1) by the
         no-silent-circulation theorem of P4 s20: the chain winding ->
         association -> sector is closed, axiom (X) is gone, and
         STATISTICS = (-1)^{2m} is a theorem of eventless record
         transport.  FERMIONS IN SHARD: FORCED (premise ledger: the
         internal-fiber instance of no-silent-circulation is the single
         named identification).
L3:      extended to FERMIONIC tame sectors (4.2): Fock structure, CAR,
         and the quadratic Hamiltonian reconstructed from record data;
         the record-GW dispersion recovered bottom-up.
O11:     audited uniform-in-L (the constant decreases with block
         length); leading-order constants exact per family (4.3);
         residue = third-order remainder control.
(C), (M), (V): untouched, except that (M)'s species search now carries
         statistics as a THEOREM-level constraint.
REMAINING OPENS: O10 (tame -> general self-adjointness); D10 (nonabelian
         statistics); process-O6 (positive realization); the empirical
         thesis (L1/L2).  [O9 and free-scope O5 were closed by Paper 10
         Part III; the stale listings of earlier editions are corrected.]
[Paper 12 update: (C) was DECOMPOSED AND REDUCED to the single named
         theorem (C-reg), and O10 was RESOLVED AS A CLASSIFICATION -
         non-tame sectors are sectors with missing boundary records,
         the Weyl limit-point/limit-circle alternative realized on
         record towers.  See Paper 12.]
[Paper 16 update: process-O6 RESOLVED AS A CLASSIFICATION - sealable =
         cone-finite (the ledger IS the Heller cone), and STRICTLY
         smaller than reversible + valid + finite-record-rank: the
         record clock (rank exactly 3, reversible, valid analytically)
         is NOT a record law at any finite capacity (Theorem B,
         Frobenius peripheral spectrum).  The clock also fails RP
         exactly as P8's typed moment theorem demands - the RP-
         restricted question is the new named residue (PR-RP).  See
         Paper 16.]
[Paper 18 update: D10 DISCHARGED AT STATED SCOPE - record statistics
         in d >= 3 is S_n with eps = (-1)^(2m) P (the sign computed by
         this paper's D9a), parastatistics is fiber bookkeeping, and
         the gauge algebra is RECONSTRUCTED as the commutant of the
         record statistics (Doplicher-Roberts at record scope).
         Record-Pauli (Part II here) is now downstream of the
         classification.  See Paper 18.]
```

## 6. What this paper proves and does not prove

Proves, with machine verification at the printed values: T1 (RP-limit
lemma, with the O6 corollary); the Gaussian-tower reconstruction of
spectrum, ladder, selection rules, and unboundedness (T2/T3); the
Weyl/CCR reconstruction against exact continuum targets with the
Stone-von Neumann identification (T4); per-level dilation exactness and
projective coherence (T5); the record-Pauli theorem with both sector
forcings, the derived exclusion zero, and the signed-sector receipts
(Part II).

Part III additionally proves, with machine verification: the association
theorem discharging D9a (Frobenius-orthogonality/least-work receipts,
the Z2 quantization of any extra twist by sealed positivity, the
exclusion of the silent pi, and the end-to-end re-derivation of the
forced sectors with the DERIVED closing operator); the fermionic CAR
tower (Fock subset-sums to 7.6e-15, CAR to 8.9e-16, non-circular
quadratic reconstruction to 2.4e-15, the JW-positivity presentation
dichotomy, and the bottom-up GW dispersion); even-time positivity and
the sigma-circle closure with the measured entropy price of wrong
statistics; the favorable O11 block-length audit and the exact
per-family leading-order constants; and the process-O6 receipts (F1-F4)
locating the residue as the positive-realization problem.

Does not prove: the internal-fiber instance-identification inside the
association theorem's premise ledger (named; an attack on it is an
attack on the scope of P4 s20's principle, not on any further argument);
self-adjointness beyond the tame class (O10); the general
positive-realization statement (process-O6); anything about fields,
Poincare structure, or the interacting continuum ((C)); the completeness
thesis (empirical); nonabelian statistics (D10); the interacting record
GW operator.  Claiming any of these would be determinacy by declaration.

## 7. Status

```text
L3 reconstruction:  CLOSED at tame scope.  Spectrum to machine floor
                    from d = 40; ladder to 4e-15; selection rules 1.8e-14;
                    sqrt(n) growth witnessed; CCR group commutator
                    7.0e-02 -> 4.5e-11 along the resolved-level tower;
                    Stone-von Neumann lands the tower on the Schrodinger
                    representation; dilation towers exact and coherent
                    (<= 1.2e-15).
RP at the limit:    survives pointwise limits (PSD closure); O6 = "not
                    even approximable."
Record-Pauli:       statistics = (-1)^{2m} FORCED by sealed positivity
                    (wrong-sector minima -1.4e-05 / -1.00e+00); Pauli
                    zero exact (0.00e+00); wrong sector signed (Hankel
                    -2.33) vs forced sector (-3.7e-31).
Part III:           D9a DISCHARGED (no-silent-circulation; Z2
                    quantization receipt; silent-pi exclusion): axiom
                    (X) is GONE and statistics = (-1)^{2m} is a theorem
                    of eventless record transport - FERMIONS FORCED at
                    stated scope.  Fermionic L3: Fock/CAR/quadratic
                    reconstruction at machine floor; GW bottom-up.
                    Sigma-circle: wrong statistics is a hidden current
                    (even-time positivity + entropy price curve).
                    O11: uniform-in-L (constant decreases), per-family
                    constants exact.  Process-O6: located as positive
                    realization; boundary = the arrow (F4).
Kernel:             {(C), (M), (V), process-O6} + {D10, O7, O8
                    (interacting GW), O10, O11 remainder} + the
                    empirical thesis.  The quantum-kinematics side -
                    representation, statistics, exclusion, CCR/CAR - is
                    CLOSED at tame finite scope.
```

## References and literature map

- Papers 4-10 (internal): the loop-class ledger and Mobius
  reconstruction (P4 s40), projective consistency (P7 Theorem 7.5), the
  dilation theorems D1/D3/D5 (P7 s7.2), the frame-winding theorem and
  axiom (X) (P9 s7), site-RP and T^2 PSD (v6.3, P7 s3.5), the
  arrow-positivity theorem and driven sectors (P10 Part I), typed moment
  classes (P8 s6), split-signature exclusion (P7 s7.1, Theorem 7.6).
- M. A. Naimark (1940); W. F. Stinespring, Proc. AMS 6, 211 (1955):
  dilation theory, including the unbounded case imported in T5.
- E. Nelson, "Analytic vectors," Ann. Math. 70, 572 (1959); T. Kato,
  *Perturbation Theory for Linear Operators*; M. Reed and B. Simon,
  *Methods of Modern Mathematical Physics* I-II: self-adjointness
  criteria and strong resolvent convergence on the tame class.
- M. H. Stone (1930); J. von Neumann, "Die Eindeutigkeit der
  Schrodingerschen Operatoren," Math. Ann. 104, 570 (1931): the
  uniqueness theorem that lands the reconstructed Weyl pair on the
  Schrodinger representation.
- F. G. Mehler (1866): the oscillator kernel of the Gaussian tower.
- A. N. Kolmogorov (1933): the extension theorem (existence half, P7).
- A. Klein and L. J. Landau, J. Funct. Anal. 42, 368 (1981): OS
  positivity/reconstruction for reversible processes (with P10 T4).
- W. Pauli, "The connection between spin and statistics," Phys. Rev. 58,
  716 (1940); R. F. Streater and A. S. Wightman, *PCT, Spin and
  Statistics, and All That* (1964): the positivity-based proof tradition
  that Part II realizes in record form.
- J. A. Barandes (2302.10778, 2309.03085): the correspondence whose
  record side this reconstruction completes at tame scope.
- H. Jaeger, "Observable operator models for discrete stochastic time
  series," Neural Comput. 12, 1371 (2000); L. Benvenuti and L. Farina,
  "A tutorial on the positive realization problem," IEEE Trans. Autom.
  Control 49, 651 (2004); M. Vidyasagar, "The complete realization
  problem for hidden Markov models," Math. Control Signals Syst. 23, 1
  (2011): the positive-realization identity of process-O6 (Section 4.4).
- P. H. Ginsparg and K. G. Wilson (1982); W. Bietenholz and U.-J. Wiese
  (1996): the GW fixed-point structure met bottom-up in Section 4.2.
