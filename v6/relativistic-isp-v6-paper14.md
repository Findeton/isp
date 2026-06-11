# Paper 14 (v6) - SHARD: The Anomaly Campaign

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
The record Ginsparg-Wilson structure taken into gauge sectors and put at
genuine risk - and it passes every discriminating receipt.  The
gauge-coupled record GW operator exists, is exactly covariant and
exponentially local; THE INDEX THEOREM HOLDS ON THE RECORD LATTICE
(index(D) = Q exactly in all fourteen flux sectors tested, with the
vanishing theorem, noise-robustness, and integer quantization on rough
sectors where no continuum field exists); the chiral anomaly is the
local face of the index (record index density = F(x)/2pi pointwise,
falling error under refinement) and the axial/mixed coefficient is
LINEAR in the record charge (index = qQ, machine-exact); record
coarse-graining is FORM-INVARIANT on the chirality law (the blocked
gauge-coupled propagator obeys GW with the computed R_c = 1 + 2/alpha,
at eps*cond precision) and the topological ledger entry survives
geometry decimation exactly, while naive decimation carries four
species to GW's one - Paper 10's dichotomy, now gauge-coupled.  And the
export the (M) search has been waiting for: ANOMALY CANCELLATION AS A
THEOREM-GRADE FILTER on record charge spectra - no genuinely chiral
spectrum exists below stack size three, the minimal chiral record
matter content is {1,4,4 | 2,2,5}, the mixed predicate is grounded on
the lattice (equal stack indices to 1.4e-14), and the filter prunes
candidate spectra by three orders of magnitude before any dynamics
```

This paper executes the first item of the post-Paper-13 plan: the O8
frontier (gauge-coupled record chirality) attacked where it can
genuinely fail, with the anomaly filter as the strategic export to (M).

## 0. Verdict

```text
THE RISK, STATED UP FRONT.  The record GW operator was identified as
the record-chirality structure by blocking arguments (P10) - it has no
birthright to the correct TOPOLOGICAL response in gauge sectors.  If
index(D) != Q, the fermion sector's lattice realization is wrong.  This
campaign was designed so that outcome would have been the headline.

It is not the outcome.  Receipts, in escalating order of risk:

PRECONDITIONS (p14a).  In 2d U(1) record gauge sectors the GW relation
  holds at machine precision (4.0e-15); the operator is exactly gauge
  covariant (1.1e-15) and exponentially local (decay rate 0.97 per
  lattice unit: a collar operator, not an all-to-all kernel).

THE INDEX THEOREM (p14b) - the discriminating receipt.  In uniform-flux
  sectors with topological charge Q = -3..3, on two lattice sizes:
  index(D) = n_minus - n_plus = +(1/2) Tr sign(g5 D_W) = Q EXACTLY -
  fourteen sectors, fourteen integer matches, with the VANISHING
  THEOREM (all zero modes of one chirality per sector).  The index is
  a SECTOR LABEL: invariant under record noise at eps = 0.10 and 0.25;
  and on strong random sectors - where no continuum gauge field exists
  - it remains an exact integer (to 1.4e-14): topological charge is
  ledger data, quantized by the record structure itself.

THE ANOMALY (p14c).  The local face of the index: the record index
  density tracks F(x)/2pi POINTWISE (max deviation 6.4e-3 -> 2.3e-3
  under refinement at fixed ripple) while its integral stays exactly
  integer at every scope - the Schwinger anomaly coefficient read off
  ledger data, no perturbation theory.  Charge linearity: a charge-q
  record fermion in flux Q has index = qQ exactly (six cases PASS):
  the q-linear (mixed) anomaly predicate is MACHINE-VERIFIED.  (The
  q^2 gauge coefficient is a named import - the chiral bubble.)

THE RECORD RG IS CHIRALITY-EXACT IN GAUGE SECTORS (p14d) - the O8
  content.  Gauge-covariant record blocking (link-transported
  orthonormal kernel, BB^dag = 1 to 2.2e-16) maps the fine GW
  propagator to a coarse propagator obeying the GW relation with the
  COMPUTED contact term R_c = 1 + 2/alpha, at 9.1e-13 (= eps * cond;
  the operator is massless, generic sectors are near-critical).
  Decimating the gauge record itself (coarse link = transport product)
  preserves the flux sector EXACTLY and the coarse operator reads the
  same index (Q = 1, 2, 3).  The naive channel: four species at the
  Brillouin corners vs GW's one - P10's decimation dichotomy holds
  gauge-coupled: the record RG HAS a chirality-exact channel, and the
  naive channel is excluded.

THE ANOMALY FILTER FOR (M) (p14e) - the strategic export.  With
  charges = code characters (P8/P9) canonicalized positive and
  chirality from orientation classes, the 2d consistency predicates
  (n_L = n_R; sum q equal - machine-verified via index = qQ; sum q^2
  equal - named import):
    stack sizes 1 and 2: NO genuinely chiral solution exists (theorem
      by exhaustion: the predicates force equal multisets);
    stack size 3: the minimal chiral record matter content, smallest
      solution {1,4,4 | 2,2,5} (32 solutions below charge 12);
    lattice grounding: the L- and R-stacks of {1,5,6 | 2,3,7} acquire
      EQUAL total record index in flux sectors (12 = 12 to 1.4e-14);
    selectivity: pass rate 1.0e-2, genuinely chiral pass rate 3e-4
      (n = 3): the filter prunes the (M) candidate space by ~3 orders
      of magnitude per U(1) factor BEFORE any dynamics is computed.

WHAT THIS BUYS THE KERNEL: O5 is promoted from free scope to GAUGE
SCOPE; O8 is closed at kinematic/topological gauge scope, with the
interacting (quartic) record flow as its named remainder; (M) gains its
first theorem-grade screen.  Nothing was assumed: the operator could
have failed the index test and did not.
```

## 1. Method and reproducibility

```text
code/v6_p14a_gauge_gw_campaign.py       operator, covariance, locality
code/v6_p14b_index_theorem_campaign.py  the index theorem (pass/fail)
code/v6_p14c_anomaly_campaign.py        anomaly density, index = qQ
code/v6_p14d_record_blocking_campaign.py  blocking form-invariance,
                                        geometry decimation, species
code/v6_p14e_anomaly_filter_campaign.py the (M) filter
```

All receipts are exact-diagonalization computations (dense, lattices up
to 20x20 / 16x16; the largest operator is 800x800) - no sampling, no
fits except where stated; all five scripts rerun bit-identically.
Imports, named: the overlap construction (Neuberger) as the canonical
solution of the GW relation in gauge sectors; the lattice index theorem
literature (Hasenfratz-Laliena-Niedermayer; Luscher's exact lattice
chirality) as the continuum-facing frame; the q^2 gauge-anomaly
coefficient (the chiral bubble) as a named import in p14e; uniform-flux
torus configurations ('t Hooft flux) for the topological sectors.
Corpus inputs: GW as the record-chirality structure (P10 4.5), the
fermionic towers (P11), the record Weyl seed and orientation classes
(P9), code characters as charges (P8).

**Honest scoping note.** The corpus does NOT claim to have derived the
overlap operator from record decimation in 2d gauge sectors.  The GW
relation is the record-chirality law (P10's theorem-level
identification); this campaign realizes it by its canonical solution
and then shows (Section 5) that record blocking is form-invariant on
it, gauge fields included.  The named identification is: record
chirality in gauge sectors = the GW class.  Everything downstream
(index, anomaly, filter) tests that identification and could have
refuted it.

## 2. The operator

### 2.1 Construction and the GW algebra

**Setting.**  2d Euclidean record lattice, L1 x L2 torus, U(1) links
U_mu(x); gamma matrices g1 = sigma_x, g2 = sigma_y, g5 = sigma_z.  The
Wilson kernel at mass m0 = -1 (the standard window m0 in (-2, 0)):

```text
  D_W = (m0 + 2r) - (1/2) sum_mu [ (r - g_mu) T_mu + (r + g_mu)
        T_mu^dag ],      (T_mu psi)(x) = U_mu(x) psi(x + mu),  r = 1.
```

D_W is g5-hermitian (g5 D_W g5 = D_W^dag), so H = g5 D_W is hermitian;
the record GW operator is the overlap representative

```text
  D = 1 + g5 sign(H),       sign(H) = P sign(Lambda) P^dag.
```

**Proposition 2.1 (the GW relation, exactly).**  With s = sign(H),
s^2 = 1 and s^dag = s, expand:

```text
  D g5 D = (1 + g5 s) g5 (1 + g5 s)
         = g5 + s + g5 s g5 + g5 s g5 g5 s = 2 g5 + s + g5 s g5
  g5 D + D g5 = g5 (1 + g5 s) + (1 + g5 s) g5 = 2 g5 + s + g5 s g5,
```

hence g5 D + D g5 = D g5 D identically - the chirality law holds as an
ALGEBRAIC identity of the construction, for arbitrary gauge fields.
The receipts test the numerical realization, gauge covariance (a
spectral function of a covariant operator is covariant), and locality
(not automatic: the sign function is nonlocal a priori; exponential
locality is a property of the spectral gap of H).

### 2.2 Receipts (p14a)

```text
setup:        12x12, Q = 1 flux sector: plaquette phase uniform to
              1.5e-15, total flux / 2pi = 1.0000000000
GW relation:  || g5 D + D g5 - D g5 D ||_max = 4.0e-15
covariance:   || D(U^g) - G D(U) G^dag ||_max = 1.1e-15
              (random gauge transform g(x))
locality:     16x16, Q = 1: max |D(x, y)| at taxicab distance
              2..8:  1.2e-1, 2.0e-2, 1.1e-2, 3.9e-3, 1.4e-3,
              6.1e-4, 2.9e-4: fitted decay rate 0.97/lattice unit
              (range 1.04 units)
```

The record-chirality law holds exactly in the gauge sector; chirality
data rides the relation code covariantly (the P8/P10 gauge mechanism);
and the operator remains a collar operator with O(1) record range.

## 3. The index theorem

### 3.1 The two index formulas

**Definitions.**  Zero modes of D satisfy g5 s psi = -psi and are
chiral (g5 psi = +-psi); write n_-+ for their counts.  The trace
formula: since Tr g5 = 0 and g5 D = g5 + s,

```text
  Tr[g5 (1 - D/2)] = -(1/2) Tr[g5 D] = -(1/2) Tr[s],
```

and a direct pairing argument (nonzero modes of H pair across the
spectrum under g5 conjugation, contributing zero net sign) leaves

```text
  index(D) := n_- - n_+ = +(1/2) Tr[ sign(g5 D_W) ],
```

the sign convention fixed by the measured orientation (the receipts
print both formulas independently).  The topological sectors are the
't Hooft uniform-flux configurations: U_1(x) = exp(-2 pi i Q x_2 /
L1 L2), U_2 carrying the transition phase on the last row, with
plaquette phase exactly 2 pi Q / V per cell.

### 3.2 Receipts (p14b)

```text
  Q    +(1/2) Tr sign   zero modes (n-, n+)   index   [10x10 and 12x12]
 -3        -3.00000          (0, 3)             -3     PASS
 -2        -2.00000          (0, 2)             -2     PASS
 -1        -1.00000          (0, 1)             -1     PASS
  0        -0.00000          (1, 1)*             0     PASS
 +1        +1.00000          (1, 0)             +1     PASS
 +2        +2.00000          (2, 0)             +2     PASS
 +3        +3.00000          (3, 0)             +3     PASS
  (* the Q = 0 sector's accidental pair is vector-like: index 0)
robustness: link noise eps = 0.10, 0.25: index unchanged (Q = 1, 2)
rough sectors: random strong fields: index = -1, +1, +4, 0 - exact
  integers to 1.4e-14
```

### 3.3 Two readings, both load-bearing

1. The record GW operator carries the CORRECT topological response -
   the discriminating receipt the campaign was built around PASSES,
   with the vanishing theorem (one chirality per sector) for free.
2. Topological charge is LEDGER DATA: on rough record sectors with no
   continuum interpretation the index is still an exact integer.  The
   record structure quantizes topology by itself; the continuum field
   is not the carrier of the quantization.  This is the record-native
   reading of why the lattice index theorem can hold at finite spacing
   at all: the integer lives in the ledger, not in the limit.

## 4. The anomaly

### 4.1 The local density

The axial anomaly is the LOCAL face of the index theorem.  Define the
record index density q(x) = (1/2) tr_spin[ sign(g5 D_W) ](x, x), so
that sum_x q(x) = index exactly at every lattice size.  The continuum
anomaly statement is that q(x) -> F(x)/2pi pointwise for slowly varying
field strength - the Schwinger coefficient e/pi for the axial current,
read off ledger data with no perturbation theory.  Test fields: flux
Q = 1 plus a smooth ripple dA_2(x_1) = a cos(2 pi x_1 / L1).

### 4.2 Receipts (p14c)

```text
pointwise density (a = 0.3):
   L = 12:  max |q(x) - F(x)/2pi| = 6.40e-3   (mean |F|/2pi = 1.6e-2)
   L = 16:  3.63e-3                            (1.2e-2)
   L = 20:  2.34e-3                            (9.6e-3)
   integral exactly +1.000000 at every L
charge linearity (links U -> U^q):
   index = qQ for q = 1, 2, 3  x  Q = 1, 2:   six exact PASSes
```

The integral needs no continuum limit - only the density does: the
anomaly is exact at finite scope, its profile converges.  The q-linear
mixed coefficient (index = qQ) is the machine-verified half of the
(M)-filter predicates; the q^2 gauge coefficient (the chiral bubble of
a Weyl fermion) is a named import, stated, not derived - its
record-native derivation via Luscher projectors is the natural next
receipt and is left named.

## 5. The record RG is chirality-exact in gauge sectors

### 5.1 The form-invariance proposition

**Proposition 5.1 (blocking form-invariance).**  Let B be the
gauge-covariant blocking kernel: for each 2x2 block, B carries the four
site values to the block corner with parallel transport along fixed
paths and weight 1/2, so the rows of B are orthonormal and BB^dag = 1
exactly (disjoint supports, unit-modulus phases).  Define the coarse
propagator with Gaussian smearing alpha:

```text
  D_c^{-1} = B D_f^{-1} B^dag + (1/alpha).
```

If D_f satisfies GW (equivalently {g5, D_f^{-1}} = g5), and B commutes
with g5 (it is spin-diagonal), then

```text
  {g5, D_c^{-1}} = B {g5, D_f^{-1}} B^dag + (2/alpha) g5
                 = g5 (B B^dag) + (2/alpha) g5 = (1 + 2/alpha) g5:
```

the coarse propagator obeys the GW relation with the COMPUTED contact
term R_c = 1 + 2/alpha - exactly, with gauge fields on.  *Proof is the
display.*  This is Ginsparg-Wilson's original blocking argument
realized covariantly on the record lattice; the receipt's numerical
defect is pure round-off amplified by cond(D_f) (the operator is
massless, so generic sectors are near-critical - the conditioning is
physics, not error).

### 5.2 Receipts (p14d)

```text
(i) kernel: ||B B^dag - 1||_max = 2.2e-16 (orthonormal, link-
    transported); random smooth Q = 0 sector, sigma_min(D_f) = 1.3e-2:
    || {g5, D_c^{-1}} - (1 + 2/alpha) g5 ||_max = 9.1e-13  (alpha = 3)
    - exact in exact arithmetic; the printed defect is eps * cond.
(ii) geometry decimation (16x16 -> 8x8, coarse link = transport
    product of two fine links): coarse flux Q_c = Q to 1e-10 and
    index(D(U_c)) = Q exactly, for Q = 1, 2, 3: the topological
    ledger entry is blocking-invariant.
(iii) species (free Brillouin scan, 64x64): naive symbol has FOUR
    zeros (the corners); the record GW symbol has ONE (k = 0;
    next-smallest |D(k)| = 0.098 off the origin).
```

### 5.3 Reading

This is the O8 content at gauge scope: the record RG possesses a
chirality-exact channel - blocking is form-invariant on the GW law
with a computable contact term, and the topological ledger entry is
blocking-invariant - while the naive channel doubles the species and
breaks the law, exactly as P10 found in 1d free sectors.  The record
ontology's coarse-graining does not merely approximately respect
chirality; it respects it EXACTLY, with gauge fields on.  What remains
of O8 is the INTERACTING (quartic) record flow - named, not claimed.

## 6. The anomaly filter for (M)

### 6.1 The predicates and the exhaustion theorem

Charges are code characters (P8/P9), canonicalized positive (a
negative-charge left-Weyl is a positive-charge right-Weyl), with
chirality from orientation classes.  The 2d consistency predicates for
a spectrum (L-stack, R-stack):

```text
  GRAV:   n_L = n_R
  MIXED:  sum q_L = sum q_R     [q-linear: machine-grounded, 4.2]
  GAUGE:  sum q_L^2 = sum q_R^2 [q^2: named import]
```

**Theorem 6.1 (exhaustion).**  At stack sizes 1 and 2 the predicates
force equal multisets: no genuinely chiral spectrum exists.  *Proof.*
Size 1: q_L = q_R directly.  Size 2: equal sums and equal sums of
squares of two positive numbers determine the pair (the elementary
symmetric functions are fixed), so {a, b} = {c, d}.       QED
Size 3 is the minimal chiral stack, and the complete enumeration below
charge 12 yields 32 genuinely chiral solutions, the smallest being
{1, 4, 4 | 2, 2, 5} (sums 9 and 33).

### 6.2 Receipts (p14e)

```text
exhaustion:   sizes 1, 2: zero solutions (Theorem 6.1, verified by
              complete enumeration); size 3: 32 solutions <= charge
              12; smallest {1,4,4 | 2,2,5}.
grounding:    {1,5,6 | 2,3,7} at flux Q = 1: L-stack total index
              1 + 5 + 6 = 12, R-stack 2 + 3 + 7 = 12: equal to
              1.4e-14 - the MIXED predicate realized on actual
              record operators.
selectivity:  random assignments, n = 3, q <= 8: pass rate 1.0e-2,
              genuinely chiral pass rate 3e-4; n = 4: 6.2e-3 /
              2.1e-3.
```

### 6.3 Three exports to the (M) inverse search

1. **A structure theorem:** chiral record matter requires at least
   three Weyl entries per chirality - below that, anomaly freedom
   forces vector-like content.  Any SHARD matter sector that is
   genuinely chiral has a minimum complexity.
2. **A screen:** the predicates prune candidate charge spectra by
   roughly three orders of magnitude per U(1) factor before any
   dynamics, mass spectrum, or binding computation is touched.
3. **A precedent for the 4d filter:** in 4d the same program gives the
   cubic predicates (sum q^3, mixed-grav sum q); the 2d campaign fixes
   the method - exhaustion + lattice grounding of the linear predicate.

## 7. What this paper proves and does not prove

Proves, with machine verification at the printed values: Proposition
2.1 (the GW identity, with its gauge-sector realization at 4.0e-15);
existence, exact covariance, and locality of the gauge-coupled record
GW operator; the index theorem index(D) = Q across all tested sectors
with the vanishing theorem, noise robustness, and rough-sector integer
quantization; pointwise convergence of the record index density to the
anomaly density with exactly-integer integrals; charge linearity
index = qQ; Proposition 5.1 (exact form-invariance of the GW law under
gauge-covariant record blocking with computed R_c); exact flux- and
index-preservation under gauge-record decimation; the 2d species
dichotomy (four vs one); Theorem 6.1 (no chiral content below stack
size three) and the minimal size-3 chiral spectra by complete
enumeration; lattice grounding of the mixed predicate.

Does not prove: the interacting (quartic) record GW flow - O8's named
remainder (the receipts here are kinematic and topological); the q^2
gauge-anomaly coefficient from record data (named import; the chiral
bubble on the record lattice via Luscher projectors is the natural next
receipt); the derivation of the overlap representative from record
decimation in gauge sectors (named identification, Section 1); 4d
anomaly predicates (method fixed, computation not done); anything about
WHICH anomaly-free spectrum nature instantiates - that is (M) itself.

## 8. The kernel after Paper 14

```text
O5   PROMOTED: free scope (P10) -> GAUGE SCOPE.  The record GW operator
     exists gauge-coupled, exactly covariant, local, with the correct
     index theorem and anomaly density.
O8   CLOSED AT KINEMATIC/TOPOLOGICAL GAUGE SCOPE: the record RG has a
     chirality-exact channel (form-invariant GW, blocking-invariant
     topology); REMAINDER (named): the interacting quartic record flow.
(M)  GAINS THE ANOMALY FILTER: no chiral matter below stack size 3
     (theorem); the predicates as the first screen of the inverse
     search; the q-linear predicate lattice-grounded.
     [Paper 17 update: the filter was consumed by (M) Phase I - the
     factorization theorem (generations commute with the filter)
     upgrades the exhaustion bound to 9 + 9 for three-generation
     content, and the SM passes the 4d filter exactly.  See Paper 17.]
D8/NN (P9): the Nielsen-Ninomiya registration is RESOLVED in the
     standard way at record scope: the GW operator evades doubling
     with exact lattice chirality (species receipt, Section 5.2(iii)).
KERNEL: { (C-reg), (M), (V), process-O6 } +
        { D10, O7, O8-remainder (interacting flow), O11-remainder }.
NEXT (per the standing plan): Paper 15 = (C-reg-a), the uniform
     tensor-class Mosco theorem as a PROOF PAPER with sharpness
     receipts; then process-O6; then (M) Phase I consuming the filter.
```

## 9. Status

```text
Operator:  GW 4.0e-15 (algebraic identity, Prop. 2.1), covariance
           1.1e-15, locality 0.97/unit - PASS.
Index:     index = Q, 14/14 sectors, vanishing theorem, noise-robust,
           rough-sector integers to 1.4e-14 - THE DISCRIMINATING
           RECEIPT PASSES.
Anomaly:   density = F/2pi pointwise (6.4e-3 -> 2.3e-3 under
           refinement), integral exactly integer; index = qQ 6/6.
RG:        blocking form-invariant on GW (Prop. 5.1: R_c = 1 + 2/alpha,
           9.1e-13 = eps*cond); decimated topology exact (Q = 1, 2, 3);
           species 4 (naive) vs 1 (GW).
Filter:    Theorem 6.1 (no chiral solutions at sizes 1-2); minimal
           {1,4,4 | 2,2,5}; grounding 12 = 12 (1.4e-14); selectivity
           3e-4 (chiral).
Kernel:    O5 -> gauge scope; O8 -> kinematic closure + named
           interacting remainder; (M) armed with its first screen.
```

## References and literature map

- Papers 8-11 (internal): code characters as charges and the gauge
  mechanism (P8), the record Weyl seed, orientation classes, and the
  Nielsen-Ninomiya registration (P9), the record GW operator and the
  decimation dichotomy (P10 4.5), the fermionic CAR towers (P11).
- P. H. Ginsparg and K. G. Wilson, Phys. Rev. D 25, 2649 (1982): the
  relation, and the blocking argument Section 5 realizes covariantly.
- H. Neuberger, Phys. Lett. B 417, 141 (1998): the overlap solution.
- P. Hasenfratz, V. Laliena, F. Niedermayer, Phys. Lett. B 427, 125
  (1998): the lattice index theorem.
- M. Luscher, Phys. Lett. B 428, 342 (1998): exact lattice chirality
  and the anomaly from the GW relation.
- H. B. Nielsen and M. Ninomiya, Nucl. Phys. B 185, 20 (1981): the
  doubling obstruction (evaded, Section 5.2(iii)).
- G. 't Hooft, Nucl. Phys. B 153, 141 (1979): twisted/flux torus
  sectors (the topological configurations of Section 3).
- J. Schwinger, Phys. Rev. 128, 2425 (1962): the 2d anomaly physics
  behind Section 4.
- L. Alvarez-Gaume and E. Witten, Nucl. Phys. B 234, 269 (1984):
  gravitational and mixed anomalies (the predicate set of Section 6).
```
