# Paper 18 (v6) - SHARD: D10 - The Record Doplicher-Roberts Theorem

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
The gauge group is not an input.  D10 (nonabelian record statistics)
discharged at stated scope by a four-step chain, each step machine-
receipted: (R1) in screen dimension >= 3 eventless exchange-squared
transport carries NO holonomy (pure-gauge receipts at 2e-14 across an
explicit contraction; holonomy tracks enclosed EVENTS only) - braid
statistics collapses to the symmetric group, with d = 2 surviving as
exactly Paper 9's anyon window; (R2) the two-excitation statistics
operator lies in the two-dimensional transport commutant span{1, P}
(machine: dim 2 for d = 2, 3, 4), the ledger EXCLUDES +-1 (they predict
ABSENT cross-records where the eventless seam seals modulus-1 entries),
and the sign is COMPUTED by D9a's exchange-is-transport: eps =
(-1)^(2m) P.  PARASTATISTICS IS NEVER FUNDAMENTAL in the record
ontology; (R3) Schur-Weyl then makes the Doplicher-Roberts
reconstruction finite linear algebra: the fiber dimension TRUNCATES the
statistics algebra (rank 23 != 24 on (C^3)^4: para-order IS the fiber
dimension, forced both ways by sealed baryon-channel entries), and THE
GAUGE ALGEBRA IS EXACTLY THE COMMUTANT OF THE RECORD STATISTICS
(165 = 165 double-commutant receipt on (C^3)^3): gauge from exchange;
(R4) the color receipts - the baryon is the UNIQUE rank-1 antisymmetric
singlet, four-quark antisymmetrization is EXACTLY ZERO (Pauli for
color), and the baryon transforms only by det U (the abelian/center
shadow); (R5) Paper 17's Z_3 census is DERIVED: the closure predicate
is center neutrality, the abelian search saw precisely the CENTER of
the reconstructed group, as Doplicher-Roberts predicts.  And PART II
opens (M) Phase II inside this paper: the nonabelian anomaly
predicates COMPUTED from explicit generators (A(6) = +7, A(10) = +27
at 1e-15 proportionality; the SU(2) cubic identically zero, Witten in
its place), and the first exhaustive representation search on the Z_6
quotient lattice - WHERE THE STANDARD MODEL GENERATION EMERGES AS THE
UNIQUE MINIMAL GENUINELY CHIRAL ANOMALY-FREE MATTER CONTENT: nothing
below its 15 Weyl fermions, nothing else at 15, robust under the
hypercharge bound.  The inverse search's first positive result
```

This paper executes the agreed flagship target: D10, reframed as the
record-native Doplicher-Haag-Roberts/Doplicher-Roberts theorem - not
"invent braid theory" but "prove that record exchange forces
permutation statistics and reconstructs the gauge group."

## 0. Verdict

```text
THEOREM R1 (permutation forcing; proved from P4 s20 + topology).
d >= 3: eventless exchange-squared transport is trivial: eps^2 = 1 -
braids collapse to S_n.  d = 2: the flat modulus survives: P9's anyon
window is the unique exception.  Receipts: pure-gauge holonomy = 1 to
2.2e-14 at every contraction stage; eventful holonomy 1.99 -> 0.12 as
the contraction empties the loop; d = 2 modulus = arbitrary U(3).

THEOREM R2 (the statistics operator; proved, sign computed).
Transport covariance puts eps in span{1, P} (machine: commutant dim 2
for d = 2, 3, 4); with eps^2 = 1 and unitarity: {+1, -1, +P, -P}.
The LEDGER excludes +-1 (absent cross-records where the eventless seam
seals modulus 1); D9a computes the sign (exchange IS transport, which
carries the 2pi frame rotation: exp(2 pi i Jz) = (-1)^(2m), receipts
m = 1/2, 1, 3/2):
                    eps = (-1)^(2m) P.
COROLLARY: parastatistics is NOT fundamental in the record ontology;
record-Pauli (P11 Part II) becomes downstream.

THEOREM R3 (record Doplicher-Roberts; proved at finite scope).
(a) TRUNCATION = ORDER: dim span(S_n on (C^d)^n) = sum over Young
    diagrams with <= d rows of f_lambda^2 < n! once n > d (receipts:
    23 != 24 at d = 3, n = 4; 5 != 6 at d = 2, n = 3); the order is
    FORCED both ways (sealed baryon-channel weight 0.00964 > 0
    clashes with any lower-order hosting; higher order adds nothing).
(b) GAUGE FROM EXCHANGE: the commutant of the statistics span on
    (C^3)^3 has dimension 165 = 10^2 + 8^2 + 1^2 and EQUALS the span
    of {U x U x U : U in U(3)} (165 = 165, mutual): the gauge algebra
    is RECONSTRUCTED as the symmetry of the record exchange structure.
(c) THE COLLAPSE: sum_lambda dim S_lambda(C^3) f_lambda = 3^n (27,
    81): para-sector state counts ARE ordinary Fermi/Bose with the
    fiber unhidden.

R4 (color receipts).  rank(A_3) = 1 (the unique baryon singlet);
||A_4|| = 0 EXACTLY (Pauli for color); U^3 b = det(U) b to 2.4e-16
(the baryon carries only the determinant: the center shadow).

R5 (Paper 17 derived).  The center omega 1 of SU(3) acts on Lambda^k
by omega^k; P17's closure predicate IS center neutrality; the minimal
bases land on conjugate triality patterns ((1,1,1)|(2,2,2)); the
multiplicity-3 charges lift to single U(3) fundamentals with the
abelian charge on det U(3).  What an abelian search can see of a
reconstructed nonabelian group is exactly its CENTER - the DR
prediction, realized.

PART II ((M) PHASE II, OPENED HERE).  The nonabelian predicates
computed from explicit generators (T(R) = 1/2, 1/2, 3, 5/2, 15/2;
A(R) = +1, -1, 0, +7, +27 for {3, 3bar, 8, 6, 10}, cubic-tensor
proportionality to the d-symbol at 1e-15; SU(2)'s d-tensor identically
ZERO with the Witten even-doublet condition in its place); the
exhaustive representation search (color to the fundamental, weak to
the doublet, Z_6 lattice, <= 5 multiplets): sizes 1-4 EMPTY; size 5:
THE STANDARD MODEL GENERATION AND ITS CONJUGATE, alone; nothing below
15 Weyl, nothing else at 15; robust at |Y6| <= 10, 12.

D10: DISCHARGED AT STATED SCOPE.  Nonabelian gauge-charged matter
exists in SHARD as fiber-dimension >= 2 sectors with eps = (-1)^(2m) P;
the gauge group is reconstructed from exchange; (M) PHASE II IS
EXECUTED at minimal scope with the SM generation as its unique floor.
```

## 1. Method and reproducibility

```text
code/v6_p18a_exchange_topology_campaign.py        R1 (Section 2)
code/v6_p18b_statistics_classification_campaign.py R2 (Section 3)
code/v6_p18c_schur_weyl_dr_campaign.py            R3 + R4 (Section 4)
code/v6_p18d_triality_instance_campaign.py        R5 (Section 5)
code/v6_p18e_nonabelian_predicates_campaign.py    Part II (Section 6)
code/v6_p18f_phase2_search_campaign.py            Part II (Section 7)
```

All six scripts rerun bit-identically.  Named imports: simple-
connectedness of S^(d-1), d >= 3 (topology); Schur-Weyl duality and
Young theory (classical - and machine-verified at the scopes used:
every rank and dimension printed is computed, not quoted); the
continuum DHR/DR theory as the TARGET FRAME (Doplicher-Haag-Roberts
1971/74; Doplicher-Roberts 1989) - the corpus does NOT re-prove the
continuum category theorem; it proves the record-scope finite version;
the Witten SU(2) condition and the 4d cubic structure (Part II).
Corpus inputs: P4 s20 (eventless = flat; silent-seam exclusion), P9
(frame winding, anyon window, projective fibers), P11 Parts II-III
(record-Pauli; D9a: exchange = transport), P17 (the abelian census
this paper derives, and the Z_6 lattice Part II consumes).

## 2. Theorem R1: permutation forcing

### 2.1 Statement and proof

**Theorem R1.**  Let two identical record excitations live on a screen
of spatial dimension d, with fiber transport that is EVENTLESS (no
records form along the exchange).  Then for d >= 3 the exchange
operator satisfies eps^2 = 1; for d = 2 the square of the exchange can
carry an arbitrary unitary holonomy.

*Proof.*  The relative configuration space of the ordered pair is
R^d minus the coincidence point, which deformation-retracts to
S^(d-1); the exchange-squared path is a closed loop in it (the
relative coordinate traverses a great circle).  By P4 s20, eventless
transport is FLAT away from coincidence: events are the only curvature
sources.  For d >= 3, S^(d-1) is simply connected, so every flat fiber
connection is pure gauge and every closed loop - in particular
exchange-squared - has trivial holonomy: the braid generator squares
to the identity, and the braid group representation factors through
the symmetric group S_n.  For d = 2 the relative space retracts to
S^1 with pi_1 = Z: flat connections carry a holonomy modulus (an
arbitrary unitary assigned to the generator), and the braid group
survives - exactly the record-anyon window P9 established.       QED

### 2.2 Receipts (p18a)

```text
(i) eventless (pure-gauge U(3)) transport along exchange-squared and
    its explicit contraction (loop family shrinking to a pole):
    ||holonomy - 1||_max = 2.2e-14 / 1.2e-14 / 7.3e-15
    at stages s = 1.0 / 0.6 / 0.3.
(ii) eventful contrast (curved connection): holonomy 1.99 at the full
    loop, decaying 1.96 -> 0.70 -> 0.12 as the contraction empties
    the enclosed events: holonomy MEASURES ENCLOSED EVENTS, never
    statistics.
(iii) d = 2: flat connection A = X dtheta: exchange-squared holonomy
    = exp(2 pi i X), an arbitrary U(3) element (printed at 1.025
    max deviation from 1): the anyon window.
```

The receipts separate the two faces cleanly: statistics is what
remains when no events are enclosed - and in d >= 3 that remainder
squares to one, at every stage of the contraction, not just in the
limit.

## 3. Theorem R2: the statistics operator

### 3.1 The commutant and the four candidates

The exchange operator eps on the two-excitation fiber space V x V
(V = C^d) must commute with simultaneous fiber transport U x U - the
exchange cannot see a gauge frame.  The commutant of {U x U : U in
SU(d)} on V x V is span{1, P} (P the flip): machine receipt, dimension
2 for d = 2, 3, 4 by exact nullspace computation.  With eps^2 = 1 (R1)
and unitarity, eps = a 1 + b P requires a^2 + b^2 = 1 and 2ab = 0:

```text
                eps in { +1, -1, +P, -P }.
```

### 3.2 The ledger excludes the spectators

**Claim.**  The candidates +-1 are excluded by the ledger itself.

*Argument.*  Consider two excitations with ORTHOGONAL fiber labels
e_1, e_2 - distinguishable words of the ledger.  The exchanged
configuration is a DIFFERENT word, and its cross-record is SEALED by
the eventless seam with modulus 1 (the transport value; the SIGN on
distinguishable words is word-phase gauge).  Machine:

```text
   candidate    |<w'| eps |w>|     sealed cross-record modulus
     +1               0.0                  1.0
     -1               0.0                  1.0
     +P               1.0                  1.0
     -P               1.0                  1.0
```

+-1 predict ABSENCE where the ledger holds a modulus-1 entry - no
phase convention repairs an absent record.  In corpus terms, an
exchange that spectates the labels is a SILENT LABEL-SWAP: excluded by
P4's silent-seam principle, the same mechanism that has carried every
forcing argument since Paper 4.  Surviving: +-P.

### 3.3 The sign is computed, not chosen

By P11 Part III (D9a discharged), record exchange of identical
excitations IS eventless transport along the exchange path, and that
path carries a relative 2pi frame rotation (P9's frame-winding
theorem).  The projective layer therefore CONTRIBUTES the phase of a
2pi rotation on the spin-m fiber:

```text
   exp(2 pi i Jz)|spin-m  =  (-1)^(2m):
   m = 1/2: -1      m = 1: +1      m = 3/2: -1     (machine receipts)
```

**Theorem R2.**  eps = (-1)^(2m) P.  The record exchange is the fiber
PERMUTATION times the computed projective sign; the +-P "freedom" of
3.1-3.2 was apparent only before D9a - the operator was never free.

**Corollary.**  Parastatistics is never fundamental in the record
ontology: statistics carries no fiber structure of its own.
Record-Pauli (P11 Part II) is now downstream of the classification
rather than parallel to it.

## 4. Theorem R3 and the color receipts

### 4.1 Schur-Weyl as the engine

With eps = (-1)^(2m) P, n identical excitations on a d-dim fiber carry
the symmetric group S_n by permutation of tensor factors on V^n.
Schur-Weyl duality (classical; machine-verified at every scope used)
decomposes V^n = sum over Young diagrams lambda of S_lambda(C^d)
tensor M_lambda, with S_lambda the GL(d) irrep (nonzero only for
<= d rows) and M_lambda the S_n irrep of dimension f_lambda.  Three
consequences become the theorem's three clauses.

### 4.2 (a) Truncation = order, forced both ways

dim span(S_n on V^n) = sum over {lambda: <= d rows} f_lambda^2,
strictly less than n! = sum over ALL lambda once n > d.  Receipts:

```text
   d = 3: n = 2: 2; n = 3: 6 (full); n = 4: 23 != 24
          (the (1^4) channel is absent: no 4-fold antisymmetrization
          over a 3-dim fiber)
   d = 2: n = 3: 5 != 6
```

"Para-order d" is the fiber dimension showing through - and it is
FORCED: hosting a d = 3 fiber at order 2 (forbidding the (1,1,1)
channel) deletes the baryon channel, whose sealed weight in a generic
3-excitation record is strictly positive (machine: 0.00964 > 0) - a
CLASH with an existing ledger entry; order above d adds nothing (the
truncation is automatic).  THE STATISTICS ORDER IS THE FIBER
DIMENSION.

### 4.3 (b) Gauge from exchange: the double commutant

```text
   dim commutant of S_3 on (C^3)^3 = 165 = 10^2 + 8^2 + 1^2
   dim span{ U x U x U : U in U(3) } = 165        (EQUAL, mutual)
```

The algebra of transports commuting with the record statistics IS the
gauge algebra, with nothing else in it.  This is the Doplicher-Roberts
reconstruction at record scope: the gauge group's status changes from
input to OUTPUT - the same promotion the corpus earlier won for
Lorentz signature (commitment), fermions (D9a), and reflection
positivity (eventlessness).

### 4.4 (c) The collapse, and R4's color receipts

```text
collapse:  sum_lambda dim S_lambda(C^3) f_lambda = 10 + 16 + 1 = 27
           = 3^3;  15 + 45 + 12 + 9 = 81 = 3^4: the "para-order-3"
           state count IS ordinary Fermi/Bose with the fiber unhidden.
color:     rank A_3 on (C^3)^3 = 1: the baryon is the UNIQUE totally
           antisymmetric singlet;
           ||A_4 on (C^3)^4||_max = 0.0e+00 EXACTLY: PAULI FOR COLOR
           (no four-quark total antisymmetrization);
           ||U^3 b - det(U) b|| = 2.4e-16: the baryon transforms only
           under the determinant U(1) - the abelian (center /
           hypercharge) shadow.
```

The record ontology's first nonabelian hadron-structure statements -
exact at finite scope, and they came from the statistics theorem, not
from dynamics.  (Confinement DYNAMICS remains with O7/O8 - not
claimed.)

## 5. R5: Paper 17 derived

The center omega 1_3 (omega = e^{2 pi i/3}; det(omega 1) = 1, so it
lies in SU(3)) acts on Lambda^k(C^3) by omega^k: quark 1, diquark 2,
baryon 0 (trivial - singlet-capable).  P17's closure predicate (a
charge triple summing to 0 mod 3) is precisely CENTER NEUTRALITY, and
the census table shows every minimal chiral base center-neutral as a
whole, with the L|R stacks landing on conjugate triality patterns
((1,1,1)|(2,2,2) for the smallest base - fundamental vs
antifundamental shadows).  What Phase I could see of the reconstructed
group was exactly its center - the DR prediction for an abelian probe.
The lift dictionary sends each multiplicity-3 charge of the P17 4d
minimal solutions to ONE U(3) fundamental, with the abelian charge on
det U(3): the hypercharge slot, exactly where R4 put the baryon's
residual charge.

## 5.5 PART II - (M) Phase II opened: the predicates and the search

With D10 discharged, Phase II's named first task (the nonabelian
seam/anomaly predicates) and its first run are executed HERE.

### 5.5.1 The predicates, computed from generators (p18e)

Nothing quoted: explicit representation generators (fund = Gell-Mann/2;
antifund; adjoint from computed structure constants; 6 = Sym^2;
10 = Sym^3) feed the trace identities tr(T^a T^b) = T(R) delta and
tr(T^a {T^b, T^c}) = (1/2) A(R) d^abc:

```text
 rep    dim   T(R)     A(R)     proportionality residual
 3        3   0.500    +1.000    0.0
 3bar     3   0.500    -1.000    0.0
 8        8   3.000    +0.000    0.0
 6        6   2.500    +7.000    1.3e-15
 10      10   7.500   +27.000    2.7e-15
SU(2): the d-tensor vanishes IDENTICALLY (machine zero) - the weak
seam constraint is the global WITTEN condition (named import,
pi_4(SU(2)) = Z_2): the number of Weyl doublets must be EVEN.
```

Every rep's cubic trace tensor is exactly proportional to the
d-symbol (1e-15), so one computed number per representation feeds the
stack: SU(3)^3, SU(3)^2-U(1), SU(2)^2-U(1), U(1)^3, U(1)-grav,
Witten-even - plus the Z_6 LATTICE constraint (P17's quotient receipt
promoted to a structural condition: charges live on the quotient
character lattice, as R5 demands).

### 5.5.2 Phase II run 1: the result (p18f)

Candidate space: multisets of Weyl multiplets (c, w, Y6), c up to the
fundamental {1, 3, 3bar}, w up to the doublet {1, 2}, |Y6| <= 8 on the
Z_6 lattice (pool: 16 multiplets; trivial singlet excluded), content
size <= 5 multiplets.  EXHAUSTIVE.  The result:

```text
 size 1: 0    size 2: 0    size 3: 0    size 4: 0
 size 5: 2 genuinely chiral anomaly-free contents -
   (1,1,+6) + (1,2,-3) + (3,2,+1) + (3b,1,-4) + (3b,1,+2)
       = THE STANDARD MODEL GENERATION (15 Weyl)
   and its conjugate (the same theory).
 nothing below 15 Weyl; nothing else at 15.
 robustness: |Y6| <= 10 and <= 12 (pools 20, 24): UNCHANGED.
```

**At stated scope, the Standard Model generation is the UNIQUE minimal
genuinely chiral matter content of the record filter stack.**  Scope
honesty, stated plainly: color/weak representations beyond the
fundamental/doublet (6, 8, weak triplets...) and contents beyond five
multiplets are NOT searched here - that is run 2 (executed in Paper
19, where the floor survives the zoo); and this is a KINEMATIC
selection (anomalies + lattice + chirality), not a dynamical
derivation: nothing here explains three generations, masses, or why
nature picks the minimal solution.  What IS established: the filter
stack built across Papers 14-18, executed on representations of the
fibers that Part I reconstructed from exchange, lands on the SM
generation as its unique floor - the inverse search's first
nontrivial positive result.

## 6. What this paper proves and does not prove

Proves: R1 (Section 2.1, from P4 s20 plus the topology import, with
the event-vs-statistics separation receipts); R2 (commutant computed,
ledger exclusion of +-1 via silent-seam, sign computed via D9a + frame
winding); R3 at finite record scope (truncation, both directions of
order = fiber dimension, the 165 = 165 reconstruction, the collapse
bookkeeping); R4's exact color statements; R5's derivation of the P17
census.  Part II adds, proved/computed at stated scope: the anomaly
coefficients of the SU(3) representations from explicit generators
with the exact d-symbol proportionality; the vanishing of the SU(2)
cubic; and the exhaustive Phase II run-1 result - the SM generation as
the UNIQUE minimal genuinely chiral content of the full stack on the
Z_6 lattice (robust under the hypercharge bound).

Does not prove: the continuum DHR/DR category theorem (named import as
the target frame; the record-scope finite version is what is
established); O(d)/Sp(d) real/quaternionic fiber cases (the receipts
are unitary-fiber; the orthogonal/symplectic refinement is a named
direction); SU(d) vs U(d) splitting beyond the det-charge bookkeeping
(the determinant U(1) is identified as the abelian slot; run 1 fixes
the hypercharge pattern at minimal scope, but its uniqueness beyond
fundamental/doublet reps is run 2's question - answered affirmatively
in Paper 19); any confinement dynamics (O7/O8); the Witten condition
internally (named import); three generations, masses, or dynamical
selection of the minimal solution (kinematic scope, stated in 5.5.2).

## 7. The kernel after Paper 18

```text
D10  DISCHARGED AT STATED SCOPE: record statistics in d >= 3 is
     S_n with eps = (-1)^(2m) P (R1+R2); parastatistics is fiber
     bookkeeping (R3); the gauge algebra is the exchange commutant
     (R3b): GAUGE FROM EXCHANGE.  Residues, named: O(d)/Sp(d) fiber
     refinement; the continuum-scope category statement (rides on
     (C-reg-b) machinery).
(M)  PHASE II RUN 1 EXECUTED (Part II): the nonabelian predicates
     computed from generators; the exhaustive minimal search returns
     THE STANDARD MODEL GENERATION AS THE UNIQUE genuinely chiral
     anomaly-free content at fundamental/doublet scope on the Z_6
     lattice - nothing below 15 Weyl, nothing else at 15, robust in
     the hypercharge bound.  Phase I reinterpreted: the abelian search
     saw the center (R5).  RUN 2 (named): higher representations,
     larger contents, and the generation/mass layer (dynamical).
KERNEL: { (C-reg-b), (M)-Phase-II-run-2, (V), (PR-RP) } +
        { O7, O8-remainder, O11-remainder, D10-refinements }.
```

## 8. Status

```text
R1:  eps^2 = 1 forced in d >= 3 (proof 2.1; pure-gauge holonomy
     2.2e-14 at all contraction stages; eventful contrast 1.99 ->
     0.12; d = 2 modulus = the P9 anyon window).
R2:  commutant dim 2 (d = 2, 3, 4); +-1 excluded by the ledger
     (absent vs sealed modulus-1 cross-records); sign computed:
     eps = (-1)^(2m) P (receipts m = 1/2, 1, 3/2).
R3:  truncation 23 != 24 / 5 != 6; order = fiber dim forced (clash
     0.00964 > 0 vs 0); reconstruction 165 = 165; collapse 27/81.
R4:  baryon rank 1; ||A_4|| = 0 exact; det-receipt 2.4e-16.
R5:  P17's Z_3 census = the center of the reconstructed group;
     closure = center neutrality; lift dictionary stated.
Part II (predicates): A(R) computed from generators (1, -1, 0, +7,
     +27; proportionality 1e-15); SU(2) cubic identically zero;
     Witten named.
Part II (run 1): SM GENERATION = THE UNIQUE MINIMAL CHIRAL CONTENT
     at fundamental/doublet scope on the Z_6 lattice (exhaustive,
     sizes 1-5; nothing below 15 Weyl; robust to |Y6| <= 12).
D10: discharged at stated scope; (M) Phase II open and running.
```

## References and literature map

- Papers 4, 9, 11, 17 (internal): silent-seam exclusion and
  eventless-flat (P4 s20), frame winding and the anyon window (P9),
  record-Pauli and D9a (P11 Parts II-III), the abelian census and the
  Z_6 lattice (P17).
- S. Doplicher, R. Haag, J. E. Roberts, Comm. Math. Phys. 23, 199
  (1971); 35, 49 (1974): superselection sectors and permutation
  statistics in d >= 3.
- S. Doplicher and J. E. Roberts, Invent. Math. 98, 157 (1989): the
  reconstruction of the compact gauge group from the statistics
  category - the continuum face of R3(b).
- H. S. Green, Phys. Rev. 90, 270 (1953); O. W. Greenberg, Phys. Rev.
  Lett. 13, 598 (1964): parastatistics and its order (the structure
  R3 collapses).
- H. Weyl, The Classical Groups (1939); R. Goodman and N. R. Wallach:
  Schur-Weyl duality (the engine of R3, machine-verified at scope).
- J. M. Leinaas and J. Myrheim, Nuovo Cim. B 37, 1 (1977); F. Wilczek
  (1982): the d = 2 exception (anyons; the P9 window).
- E. Witten, Phys. Lett. B 117, 324 (1982): the SU(2) global anomaly
  (Part II's even-doublet predicate; named import).
- R. Slansky, Phys. Rep. 79, 1 (1981): group-theory data (cross-check
  for the COMPUTED coefficients of 5.5.1).
- C. Q. Geng and R. E. Marshak; J. A. Minahan, P. Ramond, R. C. Warner
  (1989-90): anomaly-determined hypercharge - the literature face of
  run 1's uniqueness, here obtained with the Z_6 lattice and Witten
  constraints as part of the record stack.
```
