# Paper 10 (v6) - SHARD: The Arrow-Positivity Theorem and the Record Renormalization Group

Author: Felix Robles Elvira

Subtitle:

```text
Reflection positivity as a theorem of indivisible ordered transports: the
exchange cocycle is the reflection structure, its expectation is the
entropy production, and an eventless collar cannot carry an arrow - so
detailed balance, the moment-class correlations of Paper 8, and OS
positivity follow for every sector with a finite primitive presentation;
the RP boundary is the eventlessness boundary.  And the record
renormalization group on admissible refinements: exact 1d flow with the
identity m = eta_hist, the commitment constant as the EXACT 2d
Migdal-Kadanoff fixed point, the commitment-placement table across
lattices and dimensions, the gauge flow t' = b^(4-d) t with confinement
for d < 4 and marginality at d = 4, and homogenization as geometric
universality.  And Part III, the advancement campaigns: the sigma-RP
linear law (approximately eventless implies approximately RP); the
self-similarity derivation of theta_hist resolving O9 as structural,
with binary division and 2d screens mutually selected; the COORDINATION
law correcting this paper's own dimension reading (the committed
triangular ledger orders in two dimensions); the closure of
single-observable O6; the record Ginsparg-Wilson operator (O5 closed at
free scope, the fermionic record RG opened); and the measured d = 4
gauge flow at a declared kernel (the O7 baseline data)
```

This paper executes routes 9 and 10 of Paper 7 Section 14.6 - the two
items its stopping assessment classed as "new mathematics."  Part I
closes route 9 at its stated scope; Part II builds the record RG and
finds the commitment law already sitting inside it; Part III executes
the five advancement campaigns the post-review assessment identified,
resolving O9, establishing the O11 mechanism, correcting Part II's own
dimension reading, closing single-observable O6 and free-scope O5, and
measuring the d = 4 flow.

## 0. Verdict

```text
PART I (route 9: the exchange-cocycle RP attack).  The attack SUCCEEDS at
finite scope.  The chain, every link machine-verified:

  T2 (order-evidence identity, exact): the stationary entropy production
     of an ordered transport equals the expectation of the exchange
     cocycle, equals the RN evidence that the traversal ORDER leaves in
     the records:
        sigma = E[A_D] = D(P_AB || P_BA)   (machine gaps 0.0e+00).
  T3 (no-silent-arrow; a DISSOLUTION, not a dynamical theorem): an
     eventless collar records nothing - in particular not the order of
     its own traversal: D(P_AB||P_BA) = 0, hence P_AB = P_BA, hence
     DETAILED BALANCE, exactly.  Given T2 and the corpus' RN notion of
     evidence, "an eventless arrow" is a contradiction in terms; the
     silent-seam exclusion in temporal dress.
  T4 (positivity): detailed balance makes the symmetrized transfer
     self-adjoint; collar correlations become spectral measures - the
     moment sequences of Paper 8 Theorem 6.1 - and the FULL OS form over
     trajectory functionals is PSD (machine: exact 64x64 Gram from 4^7
     path enumeration, min eig -4.6e-18).  Reflection positivity is no
     longer an imported OS condition: it is a THEOREM of indivisible
     ordered transports.
  T4' (dynamical typing): Paper 8's reflection-typed classes acquire
     their dynamical meaning: site-RP at all sizes <=> the correlations
     ADMIT a reversible presentation (spectrum in [-1,1]); site+bond-RP
     <=> a reversible presentation with NONNEGATIVE transfer spectrum
     (machine: the alternating chain, eig -0.6, passes site at -6.5e-17
     and fails bond at -0.9375 exactly as Paper 8 found; its lazy
     version passes both).
  T5 (the boundary is the eventlessness boundary): the oscillating
     sectors that fail RP (Paper 8's e^{-ar}cos(kr) class) are realized
     by driven unicyclic transports with sigma > 0: the oscillation is
     POWERED by a stationary current, i.e. by committed evidence - those
     sectors are not eventless.  On the interpolating family, sigma and
     the RP defect vanish TOGETHER at zero driving (machine table).

  (R-)''' RESTATED: thermality/Euclidean reconstruction now closes for
  every eventless sector with a finite primitive Markov presentation, at
  any interaction range realized through the state.  The kernel shrinks
  to sectors with NO finite primitive presentation (genuinely infinite
  collar memory) - the constructive-QFT-class residue - where the
  per-model certificates of Paper 8 remain available.

PART II (route 10: the record renormalization group).

  R1 (exact 1d flow): decimation is exact; the committed chain flows to
     triviality with the EXACT identity xi = -1/ln tanh(eta) = 1/eta:
     the commitment coefficient IS the 1d record mass.
  R2 (relevant/irrelevant statistics): exact coarse-graining of 12-rings:
     NN decimation generates nothing (Markov exactness, receipts 1e-16);
     an NNN seed generates the full coupling vector; the linearized flow
     classifies the field as relevant and pair statistics as irrelevant
     in 1d.
  R3 (the fixed-point identity): the commitment constant is EXACTLY the
     2d Migdal-Kadanoff fixed point:
        K = 2 atanh(tanh^2 K)  <=>  t^3 + t^2 + t = 1  (t = tanh K),
     the commitment cubic of Paper 7 s8.2 - machine residual 0.0e+00,
     two-line algebraic proof.  A FOURTH role for theta_hist: spectral
     gap, lightest mass, work quantum, and now RG fixed point; eta_hist
     is the separatrix of the MK flow.
  R4 (commitment vs criticality, by dimension): the committed pairwise
     lattice ledger sits at:
        d=1: massive, m = eta_hist exactly (maximally subcritical);
        d=2: DISORDERED but 2.41% below the exact Onsager critical
             point, with bulk xi = 23.355 lattice units (exact formula);
        d=3: ORDERED (h3/K_c = 1.239 +- 0.002, |m| = 0.855): branches.
     Record-SSB (Paper 8 s8) requires d >= 3 - and the derived spatial
     dimension (Paper 7 signature theorem) is exactly 3.
  R5 (gauge flow): the series step of the gauge RG is EXACT within the
     heat-kernel family (the character mechanism of Paper 8 Theorem 9.2;
     identity verified to <= 1 sigma at 1e6 Haar samples); two
     approximation layers are declared and quantified - MK bond-moving,
     and the FAMILY PROJECTION (the Wilson family is not closed under
     the series step: mismatches 38.77% / 148.46% after one step).  The
     leading flow t' = b^(4-d) t is CONFINING for d < 4, MARGINAL at
     d = 4, deconfining above: the record RG localizes confinement
     scaling and the asymptotic-freedom question at d = 4; it does not
     answer the latter (O7).
  R6 (homogenization): alternating microscopic conductances converge
     spectrally to the harmonic-mean continuum operator (rel. gap 0.17 ->
     0.0020 over n = 16 -> 128): geometric universality, the RG face of
     the (C) docket.

PART III (the advancement campaigns, O5-O11; Section 4).

  O11: mechanism ESTABLISHED - the reversible OS Gram has rank exactly
     d; defect and sigma are both second order (exponents 2.000); the
     linear law defect = C sigma holds with C constant per family to
     three digits; audited Proposition: defect <= 0.06 sigma on the
     class.  Approximately eventless implies approximately RP.
  O9: RESOLVED AS STRUCTURAL - the 2x2 committed diamond's endpoint
     correlation equals theta_hist exactly (gap 2.2e-16): projective
     consistency of per-bond commitment under binary refinement IS the
     commitment cubic; (b, m) = (2, 2) is the UNIQUE consistent
     refinement: binary division and 2d screens mutually select each
     other.  A FIFTH role for theta_hist.
  COORDINATION LAW (correcting R4's reading): the committed TRIANGULAR
     ledger (z = 6) is ORDERED in two dimensions (-5.02% past K_c);
     honeycomb (z = 3) +15.81% disordered; square (z = 4) near-critical.
     Record-SSB requires COORDINATION (z >= ~5-6), not dimension:
     "requires d >= 3" is retracted (corrections item vii).
  O6: closes at the single-observable level (the approximable class =
     the moment class = the site-RP class); the residue is exactly the
     process-level weak-limit question, named.
  O5 (record Ginsparg-Wilson): CLOSED AT FREE SCOPE - the blocked record
     Dirac operator satisfies GW exactly (4.5e-16), single species,
     correct cone, exponentially local (xi = 2.7); naive decimation
     DESTROYS the species (the doubler's opposite chirality cancels the
     pole: residue 0.000000 vs 2.0001): the record-RG account of
     fermion doubling, and the opening of the fermionic record RG (O8).
     [Paper 14 update: O5 PROMOTED TO GAUGE SCOPE and O8 CLOSED AT
     KINEMATIC/TOPOLOGICAL GAUGE SCOPE - the gauge-coupled record GW
     operator passes the index theorem (index = Q, fourteen sectors),
     carries the anomaly density F/2pi pointwise, and record blocking
     is FORM-INVARIANT on the GW law with computed R_c = 1 + 2/alpha
     (gauge fields on); the decimation dichotomy holds gauge-coupled
     (four species vs one).  O8 remainder: the interacting quartic
     record flow.  See Paper 14.]
  O7 probe: measured d = 4 flow at a declared kernel sits BELOW the
     iid/marginal baseline (r = 0.85 -> 0.68 over beta = 1.5 -> 3.2,
     6^4 size check <= 1%), drifting toward perimeter scaling: the
     fluctuation data a beyond-MK record RG must fit.
```

## 1. Method and reproducibility

```text
code/v6_p10a_cocycle_rp_campaign.py   Part I: T1-T5 receipts (exact path
                                      enumeration for the OS Grams)
code/v6_p10b_record_rg_campaign.py    Part II: R1-R6 receipts (exact ring
                                      coarse-graining, Onsager, strip
                                      transfer, 12^3 Metropolis, Haar MC)
code/v6_p10c_sigma_rp_bound_campaign.py    Part III: O11 + O6
code/v6_p10d_self_similarity_campaign.py   Part III: O9 + coordination law
code/v6_p10e_record_gw_campaign.py         Part III: record GW (O5/O8)
code/v6_p10f_gauge_flow_probe.py           Part III: d = 4 probe (O7)
```

Claim discipline as in Papers 6.1-9; classical results consumed by the
proofs (Kolmogorov's criterion, the Hamburger machinery via Paper 8,
Onsager's energy, the OS reconstruction of reversible chains) are
IMPORTED and named.

Post-review revision (corrections owed to external review and to this
paper's own re-examination):

```text
i.   T3 is reclassified: T2 (the order-evidence identity) is the
     THEOREM; T3 is the DISSOLUTION it enables - given the corpus' RN
     notion of evidence, "an eventless arrow" is a contradiction in
     terms.  Dissolutions are this corpus' strongest move (P6: A_rec;
     P7: Lambda), and mislabeling one as a deep dynamical theorem
     invites the wrong attack.  Section 2.3 now says this.
ii.  T4' is weakened by one word, where the first edition outran the
     proof: site-RP at all sizes <=> the correlations ADMIT a reversible
     presentation (via the P8 converses) - the given kernel need not
     itself be reversible.
iii. The MK identity's specificity is now mapped (Section 3.4): BOTH
     b=2 orderings are pinned by the commitment cubic (they are
     conjugate maps; machine: move-then-decimate FP = eta/2 to 4.1e-13,
     and tanh(eta/2) = theta^2 is the cubic again), while b=3 genuinely
     breaks it (FP 0.721818 != eta).  O9 sharpens accordingly.
iv.  The gauge flow has a SECOND approximation layer beyond bond-moving,
     now declared and machine-quantified (Section 3.6): the heat-kernel
     family is exactly closed under the series step, but the Wilson
     family is not (matching j=1/2 after one series step leaves j=1 off
     by 38.77% and j=3/2 by 148.46%): real one-cell laws are projected
     back onto the single-coupling family at each step.
v.   The d=3 commitment placement now carries an error bar:
     h3 = 0.2746 +- 0.0005, h3/K_c = 1.239 +- 0.002.
vi.  A quantitative sigma-RP bound (RP defect <= f(sigma), upgrading the
     joint-vanishing receipt of T5 to a theorem-grade statement) is
     named as a new open, O11.  [Part III, Section 4.1: the mechanism is
     now established and the linear law audited.]
vii. Part III's coordination law (Section 4.3) CORRECTS Section 3.5's
     reading: "record-SSB requires d >= 3" is retracted in that form.
     The committed triangular ledger (z = 6) ORDERS in two dimensions;
     the control parameter is coordination, and the derived-3d remark
     demotes to "three dimensions guarantee sufficient coordination."
     The R4 placements themselves stand; their dimensional
     interpretation was the error.
```

## 2. Part I: reflection positivity from the exchange cocycle

### 2.1 The cocycle and its laws

For an ordered transport P(b|a) with stationary law pi, the exchange
cocycle of P4 s34, in joint form,

```math
A_D(a,b)\;=\;\log{\pi(a)P(b|a)\over\pi(b)P(a|b)}\;=\;\log{dP_{AB}\over dP_{BA}},
```

is antisymmetric by construction, and (Theorem T1, classical content
imported from Kolmogorov/Schnakenberg, machine-instantiated):

```text
A_D = 0 identically  <=>  all cycle affinities vanish  <=>  zero
stationary currents  <=>  detailed balance.
```

Machine: a reversible kernel (symmetric weights, d=4) gives max |A_D| =
1.3e-15 and cycle affinity -3.1e-16; the driven unicycle (p = 0.55,
q = 0.15) gives cycle affinity 3 ln(p/q) = 3.897849 (machine identical).

### 2.2 The order-evidence identity

**Theorem T2 (exact).** The stationary entropy production rate is the
expectation of the exchange cocycle, and equals the RN divergence between
the forward and order-reversed joint laws:

```math
\sigma\;=\;\tfrac12\sum_{a,b}\big(J_{ab}-J_{ba}\big)A_D(a,b)
\;=\;\mathbb E_{\rm fwd}[A_D]\;=\;D\big(P_{AB}\,\Vert\,P_{BA}\big)\;\ge\;0,
```

with equality iff detailed balance. ∎  (Machine: reversible case sigma =
2.3e-31; driven case sigma = E[A_D] = D = 0.519713 with identity gaps
0.0e+00.)

The physical reading is the paper's pivot: **entropy production is the
evidence that the traversal order leaves in the records.**  The arrow of
an ordered transport is not an extra structure; it is the RN content of
the exchange cocycle.

### 2.3 The no-silent-arrow theorem

**Theorem T3.** An eventless collar satisfies detailed balance.

**Proof.** Eventless means the collar commits no record - in particular,
nothing records the order of its own traversal: the RN evidence
distinguishing the ordered laws, D(P_AB || P_BA), is zero.  By strict
positivity of RN divergence, P_AB = P_BA as joint laws, which is
pi(a)P(b|a) = pi(b)P(a|b): detailed balance, exactly. ∎

The exclusion reading: by T2, an eventless collar with an arrow would
carry strictly positive entropy production on zero committed evidence -
irreversibility recorded by nothing.  That is the silent-seam exclusion
in temporal dress, and it is the same native principle that fixed the
period (P6), the signature (P7 s4), and superselection (P9 s4).  P6.1's
detailed-balance verification at 8.7e-19 was this theorem's machine
shadow; the cocycle of P4 s34 is its native carrier.

**Claim status, classified precisely.** T2 is the THEOREM of this part
(an exact identity, machine gaps 0.0e+00).  T3 is the DISSOLUTION that
T2 enables: once entropy production IS the RN order-evidence, "an
eventless arrow" is a contradiction in terms - the question "why is the
eventless collar reversible?" was wrong the way "what selects A_rec" was
wrong (P6).  We classify it as a dissolution rather than a dynamical
theorem deliberately: its entire content is the corpus' identification
of evidence with RN distinguishability, and an attack on T3 is an attack
on that identification, not on any further argument.

### 2.4 Reflection positivity as a theorem

**Theorem T4.** Let the eventless collar transport be a (block-)Markov
kernel on the primitive record state space (any interaction range
realized through the state).  By T3 it is reversible; the symmetrized
transfer D^{1/2} P D^{-1/2} is self-adjoint with spectrum in [-1,1]
(machine: symmetry gap 3.3e-16; spectrum [-0.1587, 0.0558, 0.1922, 1]);
hence every collar correlation is a spectral measure -

```math
C(r)\;=\;\langle f,\,T^r f\rangle_\pi\;=\;\int_{[-1,1]}\lambda^r\,d\mu_f,
\qquad \mu_f\ge0
```

- a moment sequence, so site-RP holds at every size by Paper 8 Theorem
6.1; and the full OS form is PSD: for functionals of the future
trajectory, <theta F, F> = sum_x pi(x) E[F|x]^2 >= 0. ∎  (Machine: the
exact 64x64 OS Gram over ALL functionals of three future sites,
enumerated over 4^7 paths, has min eigenvalue -4.6e-18; a random
observable's site Hankel: -5.5e-17.)

**Theorem T4' (dynamical typing of Paper 8's classes).** Site-RP at all
sizes <=> the correlations ADMIT a reversible presentation (via the P8
converses: moment sequence = spectral form of a self-adjoint transfer);
site+bond-RP <=> they admit a reversible presentation with nonnegative
transfer spectrum (the bond Gram needs lambda d-mu >= 0).  The given
kernel need not itself be reversible: the typing is a statement about
presentability.
Machine: the alternating chain P = [[0.2, 0.8], [0.8, 0.2]] (transfer
eigenvalue -0.6, realizing C(r) = (-0.6)^r exactly) passes site at
-6.5e-17 and fails bond at -0.9375 - reproducing Paper 8's typed receipts
from dynamics; its lazy version (I+P)/2, spectrum >= 0, passes both. ∎
The antiferromagnetic site-only class of Paper 8 is exactly the
reversible-with-negative-spectrum class.

### 2.5 The boundary of positivity is the boundary of eventlessness

**Theorem T5.** The RP-failing sectors of Paper 8 - damped oscillations
e^{-ar} cos(kr) - are realized by driven transports and only by driven
transports: a complex transfer pair requires nonzero cycle affinity.
Machine: the driven unicycle has transfer pair rho = 0.350000, phase =
1.714144 (so a = 1.049822, k = 1.714144 - the failure class), correlation
sequence with sign changes, site Hankel min eig -6.4e-02 at N = 6, full
OS Gram min eig -1.8e-02, and sigma = 0.519713 > 0.  On the family
interpolating reversible -> driven:

```text
eps      sigma           min OS eig
0.00     0.000000e+00    -1.0e-17
0.05     2.876821e-02    -1.117e-03
0.10     1.175573e-01    -4.467e-03
0.20     5.197132e-01    -1.787e-02
0.30     1.538970e+00    -4.020e-02
```

sigma and the RP defect vanish together at zero driving: on this family,
positivity is equivalent to the absence of the arrow. ∎

**Scope subtlety, stated plainly.** A stationary Gaussian process with
C(r) = e^{-ar}cos(kr) is time-reversible AS AN OBSERVED PROCESS yet fails
RP: every finite Markov presentation of it hides currents (the complex
pair above).  T3/T4 therefore live at the PRIMITIVE record presentation -
the collar's own state space - not at the level of derived observables.
The corpus' collar IS the primitive presentation, so the theorem applies
where the program needs it; sectors with no finite primitive presentation
remain open.

### 2.6 (R-)''' after Part I, and the Barandes link

```text
(R-)''' RESTATED: reflection positivity - hence thermality at
T = 1/(2*pi) and Euclidean reconstruction - is a THEOREM for every
eventless record sector with a finite primitive (block-)Markov
presentation, at any interaction range realized through the state.
Kernel: eventless sectors with NO finite primitive presentation
(genuinely infinite collar memory) - the constructive-field-theory
residue - with Paper 8's per-model certificates still available.
```

The Barandes link the route promised: division events are exactly where
record dynamics visibly fails Markovianity (P4 s10), and they carry
evidence; BETWEEN events the collar is eventless and T3-T4 apply.  The
corpus' architecture - thermality is a property of eventless collars,
non-Markovianity is a property of committed events - is thereby
self-consistent: the indivisible (non-Markov) structure lives precisely
where the positivity theorem does not need to hold, and the positivity
theorem holds precisely where the process is order-blind.

## 3. Part II: the record renormalization group

### 3.1 Definitions

Coarse-graining is the inverse of admissible refinement (P4 s48-51): keep
a sublattice of record cells, sum the rest exactly, and read the
EFFECTIVE LEDGER off the character transform of the exact coarse law.
Iterating defines the record RG; the Jacobian at a fixed point classifies
record statistics as relevant/irrelevant; running couplings are the
effective couplings per blocking level.

### 3.2 Exact 1d flow: the committed chain is massive, with m = eta

Decimation of the NN chain is exact: tanh K' = tanh^2 K.  From the
committed coupling (P8: the ring fixed point is h = eta_hist to machine
precision):

```text
0.609377863436 -> 0.304688931718 -> 0.087601424385 -> 0.007635067677
              -> 0.000058291993 -> 0.000000003398   (triviality)
```

**Identity (exact).** xi = -1/ln tanh(eta) = 1/eta = 1.641017929928,
because tanh eta = e^-eta at the commitment root: **the commitment
coefficient is the 1d record mass**, m = eta_hist per lattice unit. ∎

### 3.3 Generated couplings and the irrelevance spectrum (exact rings)

Exact coarse-graining of 12-rings (4096-state enumeration, character
transform of the coarse law):

```text
pure NN at K = eta:  J'(1) = +0.304689 (= atanh(tanh^2 eta) exactly);
                     field, J'(2), J'(3), 4-spin all <= 1.1e-16
                     (decimation of a Markov chain generates NOTHING).
NN + NNN seed (0.4, 0.15):  J'(1) = +0.327666,  J'(2) = +0.019870,
                     J'(3) = +0.009011,  quad = -7.9e-04
                     (coupling generation once memory crosses the scale).
linearized map at (K1 = 0.1, K2 = 0, h = 0): eigenvalues
                     {1.1974, 0.1975, 0.0097}: y = {+0.260, -2.34, -6.68}
                     - the field is RELEVANT, pair statistics irrelevant:
                     1d has no interacting fixed point, as 3.2 shows.
```

### 3.4 The fixed-point identity: a fourth role for theta_hist

**Theorem R3.** The commitment constant is exactly the nontrivial fixed
point of the b = 2 Migdal-Kadanoff map in two dimensions
(decimate-then-bond-move, K' = 2 atanh(tanh^2 K)):

```math
K=2\,{\rm atanh}(\tanh^2K)
\;\Longleftrightarrow\;
(1+t)^3(1-t)=(1+t^2)^2
\;\Longleftrightarrow\;
t^3+t^2+t=1,\qquad t=\tanh K,
```

the commitment cubic of Paper 7 Section 8.2 - and tanh K = e^{-K} reduces
to the same cubic.  Machine: residual 0.0e+00 at eta_hist; the MK
linearization gives lambda = 4 theta/(1+theta^2) = 1.678573510,
nu_MK = 1.338266 (the standard MK approximation to the exact 2d value 1);
the flow's separatrix is eta_hist exactly (basin receipts: 0.3, 0.5 ->
disordered; 0.7, 1.0 -> ordered). ∎

theta_hist now carries four roles: spectral gap, lightest unoriented
mass, gravitational work quantum (P7 s9.6), and 2d MK fixed point - the
committed coupling is the scale-invariant point of series-then-parallel
composition.

**Specificity, mapped (machine).** The identity is a property of
PAIRWISE (b = 2) composition per se, robust to ordering, and breaks
beyond it: the two b = 2 orderings are conjugate maps via the bond-move,
and BOTH are pinned by the commitment cubic (move-then-decimate fixed
point = eta/2 to 4.1e-13, since tanh(eta/2) = theta^2 is again
theta^3 + theta^2 + theta = 1), while the b = 3 fixed point is
0.721817738 - genuinely different.  O9 therefore sharpens to: why does
the commitment law encode b = 2 series-parallel self-similarity?  That
at least rhymes with commitment being a statement about BINARY division;
whether it is structural or an accident of the cubic is OPEN (O9).
The physical reading remains MK-scheme-bound ("exact in the MK scheme",
not a proof of physical criticality).  Read against R4: under the MK
approximation the committed 2d sector sits exactly AT criticality; the
exact Onsager placement (below) puts it 2.41% under - the two statements
bracket a suggestive fact: commitment tunes 2d record matter to the
near-critical regime without any external tuning.

### 3.5 Where commitment places matter, by dimension

The committed pairwise lattice family (the P8 Section 8 family, now on
Z^d), solving E[ss] = e^{-h} exactly per dimension:

```text
d = 1: m = eta_hist exactly (3.2); K_c = infinity: maximally subcritical.
d = 2: h2 = 0.430063402 from Onsager's exact energy
       (eps(K_c) = sqrt(2)/2 verified); K_c = 0.440686794:
       (K_c - h2)/K_c = 2.41 PERCENT below critical; exact bulk
       correlation length 1/xi = ln coth K - 2K: xi(h2) = 23.355 lattice
       units (strip-transfer receipts: xi_W = 4.45, 6.45, 8.21, 9.78 at
       W = 4..10, rising toward bulk).  DISORDERED, NEAR-CRITICAL.
d = 3: h3 = 0.2746 +- 0.0005 (Metropolis 12^3; <ss> = 0.7635 +- 0.0015
       matches e^{-h} = 0.7599; crossing-slope error propagation);
       h3/K_c(3d) = 1.239 +- 0.002: ORDERED, |m| = 0.8550.
```

**The dimension law of record-SSB.** Paper 8 Section 8 found sealed
branches on the complete graph (mean-field, d -> infinity) and none on
the ring (d = 1).  The RG placement completes the picture: branch
formation - record-SSB - requires d >= 3; d = 2 is the near-critical
margin; d = 1 is massive and trivial.  The derived spatial dimension of
this corpus (the (1,3) signature theorem) is exactly 3: the geometry that
commitment derives is the lowest one in which commitment can seal a
branch.  Stated as an observation with its scope: proved for the
pairwise ferromagnetic family; the general-ledger statement is open.

**[CORRECTED by Part III, Section 4.3.]** The dimensional reading above
is retracted (corrections ledger, item vii): on the triangular lattice
(z = 6) the committed ledger ORDERS in two dimensions.  The control
parameter is COORDINATION, not dimension; the placements in this section
stand, but they track z (4 for square, 6 for cubic), and the "lowest
dimension that seals a branch" remark demotes accordingly.

### 3.6 The gauge flow: confinement scaling and the d = 4 margin

The series step of the gauge RG is EXACT within the heat-kernel family:
combining sealed plaquettes in series convolves their kernels, and
heat-kernel times add - the character mechanism behind Paper 8 Theorem
9.2 (machine: the convolution identity at 1e6 Haar samples, pulls 0.29,
0.90, 1.02 sigma).  Two approximation layers, both declared: (a) MK
bond-moving (divide by b^{d-2}); (b) FAMILY PROJECTION - the heat-kernel
family is exactly closed under the series step (moment ratios square and
stay heat-kernel), but realistic one-cell laws are NOT: for the Wilson
law at beta = 1.5, matching the j = 1/2 moment after one series step
requires beta' = 0.478234, which then misses j = 1 by 38.77% and
j = 3/2 by 148.46% (machine) - so a single-coupling flow silently
projects the law back onto its family at every step.  With both caveats,
the leading flow is

```math
t'\;=\;b^{\,4-d}\,t .
```

```text
d = 3: t doubles per step: sigma_lat = t c2 grows - CONFINING flow
       (the record account of why the 3d probe of Paper 8 sees a string
       tension at every coupling).
d = 4: t' = t exactly - MARGINAL: the gauge coupling neither confines
       nor trivializes at leading order; asymptotic freedom is the
       next-order question, which the record RG localizes and does not
       answer (O7).
d = 5: deconfining flow.
```

### 3.7 Homogenization: geometric universality for (C)

Alternating bond conductances (0.5, 2.0) on an n-ring converge
spectrally to the uniform harmonic-mean operator (c_eff = 0.8):

```text
n = 16: 1.74e-01   n = 32: 3.39e-02   n = 64: 7.97e-03   n = 128: 1.96e-03
```

Microscopically different geometric ledgers flow to one continuum
operator: universality is the RG face of the (C) docket, and the
homogenized coefficient is the running coupling of the geometric sector.

### 3.8 What the record RG does not yet give

```text
O7 (the 4d gauge beta function): beyond-MK corrections at the d = 4
    margin - the record form of asymptotic freedom.  The series step is
    exact; what is needed is a controlled improvement of bond-moving.
O8 (the fermionic record RG): the flow of half-integer fiber sectors
    (Paper 9) under blocking, including the fate of the doubling
    obstruction along the flow.
O9 (the MK-commitment identity, sharpened): both b=2 orderings are
    cubic-pinned (conjugate maps; move-then-decimate FP = eta/2) while
    b=3 breaks the identity: decide whether the commitment law's b=2
    series-parallel self-similarity is structural (binary division as
    composition) or an accident of the cubic; a derivation would make
    the commitment law itself an RG statement.
    [RESOLVED in Part III, Section 4.2: STRUCTURAL - projective
    consistency of per-bond commitment under binary refinement IS the
    cubic, and (b, m) = (2, 2) is the unique consistent refinement.]
O11 (the sigma-RP bound): upgrade T5's joint-vanishing receipt to a
    quantitative theorem - a bound (RP defect) <= f(sigma) relating the
    OS Gram's negative part to the entropy production, uniformly over a
    transport class.
    [ADVANCED in Part III, Section 4.1: mechanism established (rank-d
    Gram, second-order matching), linear law audited at C* = 0.06;
    residue = constant-chasing.]
SM running, Yukawa flows, and scheme-independence statements remain
unposed; the corpus now has the machine to pose them.
```

## 4. Part III: the advancement campaigns (O5-O11)

This part executes the five advancement routes identified in the
post-review assessment, with four new diagnostics:

```text
code/v6_p10c_sigma_rp_bound_campaign.py    O11 mechanism + O6 closure
code/v6_p10d_self_similarity_campaign.py   O9 resolution + the
                                           coordination law
code/v6_p10e_record_gw_campaign.py         the record Ginsparg-Wilson
                                           operator (O5, O8, P9 D8)
code/v6_p10f_gauge_flow_probe.py           the measured d = 4 flow (O7)
```

### 4.1 O11: the sigma-RP linear law, mechanism established

The mechanism conjectured in Section 3.8 is confirmed in full:

```text
rank of the reversible OS Gram (27 x 27, d = 3, L = 3):  EXACTLY 3
  (the Gram factors through the reflection point: heavy kernel);
scaling exponents in the driving eps:
  sigma: 2.000   defect: 2.000   kernel-projected sym(dM): 2.000
  (the first-order symmetric perturbation vanishes on ker(M0): defect
   and sigma are BOTH second order - the linear law is generic);
the law defect = C * sigma, audited over 10 random families:
  C is constant in eps PER FAMILY to three digits (e.g. 0.0356, 0.0356,
  0.0356 across eps = 0.02..0.08); empirical sup C = 0.0421.
```

**Proposition (audited).** On this class, defect <= C* sigma with
C* = 0.06 (50% margin).  Status: the mechanism (rank-deficient base +
second-order kernel perturbation) is machine-established; the remaining
content of O11 is constant-chasing (Pinsker + explicit spectral data),
no longer structure-finding.  Physical reading: APPROXIMATELY EVENTLESS
IMPLIES APPROXIMATELY RP, with the OS defect bounded linearly by the
arrow's evidence rate - thermality at T = 1/(2 pi) is robust, not
knife-edge.

### 4.2 O9 RESOLVED: the self-similarity derivation of theta_hist

**Theorem (refinement self-consistency).** The 2x2 committed diamond -
each sub-bond at the committed coupling eta - has endpoint correlation
(exact enumeration)

```text
<s0 s1>_network = 0.543689012692077 = theta_hist   (gap 2.2e-16),
```

and the identity 2 theta^2/(1 + theta^4) = theta is ALGEBRAICALLY the
commitment cubic: theta^4 - 2 theta + 1 = (theta - 1)(theta^3 + theta^2
+ theta - 1).  Hence per-bond commitment is projectively self-consistent
under binary refinement of a screen bond - the coarse bond of the
committed network satisfies the commitment law EXACTLY (coarse
correlation = e^-eta = 0.543689012692, machine receipt), as
cover-independence (P4 s75) and projective consistency (P7 Theorem 7.5)
require of a sealed law. ∎

theta_hist therefore has a SECOND, independent characterization: the
unique nontrivial coupling at which committing at the fine scale and
committing at the coarse scale agree on sealed correlations.  The MK
identity of Section 3.4 is this consistency map in RG dress.  O9 is
RESOLVED AS STRUCTURAL, and a FIFTH role joins the ledger: spectral gap,
lightest unoriented mass, work quantum, MK fixed point, and refinement
self-consistency point.

**Selection corollary.** Scanning m parallel routes of b bonds in series
(all committed), consistency m*atanh(theta^b) = eta holds at

```text
(b, m) = (2, 2) ONLY   (residual +0.0000; all other (b, m) in
2..5 x 1..4 fail, nearest miss +0.0391 at b = 3, m = 4):
```

binary division and two-route (2d-screen) refinement mutually select
each other.  The corpus' binary primitive and its two-dimensional
screens are not independent postulates: under commitment, each is the
unique choice consistent with the other.

### 4.3 The coordination law (CORRECTING this paper's R4 reading)

Solving the committed placement e^{-h} = <ss>(h) across 2d lattices
(strip transfer matrices, W = 10-12):

```text
lattice      z   K_c(exact)   h_commit    (K_c-h)/K_c     phase
honeycomb    3   0.658479     0.554397      +15.81%     DISORDERED
square       4   0.440687     0.426032       +3.33%     DISORDERED
                 (Onsager exact placement: +2.41%, Section 3.5; the
                  strip estimate carries finite-width bias)
triangular   6   0.274653     0.288434       -5.02%     ORDERED
[cubic 3d    6   0.221655     0.2746(5)      -23.9%     ORDERED]
```

**The committed triangular ledger seals branches IN TWO DIMENSIONS.**
The control parameter is COORDINATION, not dimension: z = 3 deep
disordered, z = 4 near-critical, z = 6 ordered - in two dimensions as in
three.  Section 3.5's reading "record-SSB requires d >= 3" is RETRACTED
in that form (corrections ledger, item vii): record-SSB requires
sufficient coordination (z >= ~5-6); dimension enters only through the
coordination it makes available, and the derived 3d remark demotes to
"three dimensions guarantee sufficient coordination."  The near-critical
window is the z = 4 window, not the d = 2 window.

### 4.4 O6 closes at the single-observable level

Every moment-class correlation is a pointwise limit of finite-atom
spectral measures - i.e. of finite REVERSIBLE chains (machine: 3, 5, 9,
17-atom quantile discretizations of a continuous spectral measure
converge uniformly on r <= 30, max gaps 5.2e-2 down to 6.5e-3, every
truncation Hankel-PSD).  With Paper 11's T1 (RP passes to pointwise
limits), the approximable class = the moment class = the site-RP class:
**single-observable O6 is EMPTY.**  The genuine residue is the
PROCESS-LEVEL question, now stated precisely: which stationary
reflection-positive processes (all finite-dimensional joint laws) are
weak limits of finite reversible chains?  That - and only that - is what
remains of the thermal kernel.

### 4.5 The record Ginsparg-Wilson operator (O5 closed at free scope)

The Ginsparg-Wilson relation was born as a block-RG fixed-point
condition; the record RG is its native home.  Blocking the continuum
free Dirac propagator onto the unit record lattice with the cell-average
kernel and contact term alpha = 1/2:

```text
GW relation {g5, D'} = 2 alpha D' g5 D':   max residual 4.5e-16 (EXACT)
GW-deformed chirality  D g5(1 - alpha D) + (1 - alpha D) g5 D = 0:
                                           max residual 5.0e-16
single species: min |det D'| away from k = 0 is 0.2679 (no doubler);
continuum cone slope 0.9996; exponentially local, xi_loc = 2.695
lattice units (local but NOT ultralocal: Nielsen-Ninomiya is evaded
through the modified symmetry while locality survives).
```

**The aliasing theorem (the contrast).** Pure decimation of the naive
lattice fermion folds the doubler onto k = 0, where its OPPOSITE
chirality CANCELS the pole: the infrared residue k^2 tr(G G+) is
0.000000 at k = 0.10, 0.05, 0.02 - versus 2.0001 (one species, exact)
for the GW blocking.  Naive coarse-graining does not merely keep the
doubling problem; it DESTROYS the massless species entirely.  This is
the record-RG account of why doubling is robust and why the GW kernel
(smearing + contact term) is the escape: O5 is CLOSED AT FREE SCOPE,
and the fermionic record RG (O8) is opened with its fixed-point
structure already in hand.  The interacting/gauge-coupled record GW
operator remains open (with lattice QCD's overlap/domain-wall
technology as the imported guide).

### 4.6 The measured d = 4 record gauge flow (the O7 probe)

The iid sealed-plaquette baseline (Theorem 9.2 of Paper 8) predicts
exact area scaling at every coupling: r := ln W(2,2)/(4 ln W(1,1)) = 1
and D := chi(2,2) - chi(1,1) = 0.  Measured on 4^4 SU(2) (declared
axial two-link blocking kernel; 6^4 size check):

```text
 L   beta    W(1,1)          W(2,2)          r                D
 4   1.5   0.24438(82)    0.00821(97)    0.8520(211)    -0.748(120)
 4   2.2   0.45473(229)   0.07158(194)   0.8365(101)    -0.358(39)
 4   2.6   0.61857(149)   0.25958(284)   0.7019(67)     -0.351(15)
 4   3.2   0.70939(116)   0.39535(199)   0.6757(49)     -0.266(9)
 6   2.6   0.61704(73)    0.25495(117)   0.7077(29)     -0.346(7)
```

Reading: the measured flow sits BELOW the iid/marginal baseline at every
coupling and drifts monotonically toward perturbative perimeter scaling
(r -> 1/2) as beta grows; finite-size shifts are <= 1% (6^4 vs 4^4).
At this kernel the inter-plaquette correlations make large loops cheaper
than exact area additivity - the fluctuation content that any beyond-MK
record RG must reproduce, in the direction consistent with the
perturbative regime of the 4d gauge theory on these volumes.  SCOPE:
a finite probe with a declared kernel; the asymptotic-freedom SIGN
question (O7) needs the matched-coupling construction (re-simulating the
blocked theory at candidate t') and larger volumes; this probe supplies
the baseline-deviation data such a construction must fit.

## 5. The kernel after Paper 10

```text
(R-)''' REDUCED (Part I): reflection positivity is a theorem of eventless
        ordered transports for every sector with a finite primitive
        Markov presentation - the exchange cocycle is the reflection
        structure, and the RP boundary is the eventlessness boundary.
        Kernel content now: RP for eventless sectors with NO finite
        primitive presentation (infinite collar memory; the
        constructive-QFT residue).  Paper 8's typed classes carry their
        dynamical characterization (T4').
(C)     gains the homogenization/universality receipt (R6); otherwise
        unchanged.
        [Paper 12 update: (C) DECOMPOSED Euclidean-first on the back of
        Part I's RP theorem - the OS bridge (C2) is this paper's theorem
        made operational (Euclidean record data -> Lorentzian propagator
        at O(dt^2)).  Residue reduced to the single named theorem
        (C-reg).  See Paper 12.]
(M)     gains the dimension law (R4: branches need d >= 3, near-critical
        margin at d = 2), the irrelevance spectrum of record statistics
        (R2), and the fourth role of theta_hist (R3).
(V)     untouched.
OPEN-SET STATUS AFTER PART III:
        O5 CLOSED AT FREE SCOPE (record GW operator, Section 4.5);
            interacting/gauge-coupled record GW remains.
        O6 CLOSED at the single-observable level (Section 4.4, with
            Paper 11 T1); residue = the process-level weak-limit
            question, precisely stated.
        O7 OPEN; the d = 4 probe (Section 4.6) supplies the declared-
            kernel baseline-deviation data; the sign question needs the
            matched-coupling construction.
        O8 OPENED with its fixed-point structure in hand (GW = the
            fermionic flow's fixed-point chirality, Section 4.5).
        O9 RESOLVED AS STRUCTURAL (Section 4.2): a fifth role for
            theta_hist; binary division and 2d screens mutually
            selected.
        O11 mechanism established, linear law audited (Section 4.1);
            residue = constant-chasing.
        D9b of Paper 9 (record-Pauli at the OS layer): executed by
        Paper 11 - wrong statistics lands in exactly Part I's
        signed/driven class, and O6 was sharpened to "not even
        approximable" (RP passes to projective limits).
```

## 6. What this paper proves and does not prove

Proves, with machine verification at the printed values: T1 (cocycle
laws, classical content instantiated); T2 (the order-evidence identity,
exact - the THEOREM of Part I); T3 (no-silent-arrow: eventless implies
detailed balance - classified as the DISSOLUTION that T2 enables, riding
on the corpus' RN notion of evidence and the strict positivity of RN
divergence); T4 and T4' (reflection positivity of reversible primitive
transports, with the full OS Gram receipts, and the presentability
typing of Paper 8's classes); T5 (oscillating memory requires entropy
production; sigma and the RP defect vanish together on the interpolating
family - qualitative; the quantitative bound is O11); R1-R2 (exact 1d
flow, the m = eta identity, exact coarse-graining with generation and
irrelevance receipts); R3 (the MK fixed-point identity, algebraic, with
linearization, conjugacy of the b=2 orderings, and the b=3 break);
R4 (the dimension placement: exact in d = 1, 2; Monte Carlo with error
propagation in d = 3); R5 (series step exact within the heat-kernel
family; MK dimension flow with both approximation layers declared);
R6 (homogenization convergence).

Part III additionally proves, with machine verification: the O11
mechanism (Gram rank exactly d; exponents 2.000; the audited linear law
defect <= 0.06 sigma); the self-similarity theorem and (2,2)-selection
corollary resolving O9 as structural (network correlation = theta to
2.2e-16); the coordination law (triangular z = 6 ordered in d = 2,
honeycomb z = 3 at +15.81%, with the R4 dimensional reading retracted);
the single-observable O6 closure; the record GW operator at free scope
(GW residual 4.5e-16, single species, cone slope 0.9996, xi_loc = 2.7,
and the aliasing-destroys-the-species contrast); and the d = 4
declared-kernel flow measurements (r = 0.85 -> 0.68, 6^4 check).

Does not prove: RP for eventless sectors at the PROCESS level beyond
approximable presentations (the surviving O6, Section 4.4); the
asymptotic-freedom sign (O7 - the probe is baseline data, not the
matched-coupling answer); the O11 constant by proof (audited only); the
general-ledger coordination law (proved for the pairwise family); the
interacting/gauge-coupled record GW operator; spin-statistics (Paper 9's
(X)/D9a; D9b executed by Paper 11); continuum QCD.  The MK
scheme-dependence of R3 is disclosed: the identity is exact for b = 2
(both orderings, conjugate), fails at b = 3, and its REASON is now the
Section 4.2 self-consistency theorem rather than a scheme accident.

## 7. Status

```text
Route 9:     EXECUTED - SUCCEEDS at stated scope.  sigma = E[A_D] =
             D(P_AB||P_BA) exact (T2, the theorem); eventless =>
             detailed balance (T3, the dissolution) => moment-class
             correlations => site-RP and full OS positivity (Gram min
             eig -4.6e-18, exact enumeration); typed classes given
             their presentability characterization; RP boundary =
             eventlessness boundary (joint vanishing; quantitative
             bound = O11); kernel reduced to non-presentable sectors
             (O6).
Route 10:    EXECUTED.  Record RG defined on admissible refinements;
             exact 1d flow with m = eta_hist; generated couplings and
             irrelevance spectrum exact on rings; theta_hist = MK-2d
             fixed point exactly (fourth role; separatrix; nu_MK =
             1.338266; a b=2 phenomenon - both orderings cubic-pinned,
             b=3 breaks it); dimension placement 1d massive / 2d
             near-critical (2.41%, xi = 23.355) / 3d ordered
             (h3/K_c = 1.239 +- 0.002): record-SSB needs d >= 3 and the
             derived dimension is 3; gauge flow t' = b^(4-d) t
             (confining d < 4, marginal d = 4; bond-moving AND
             family-projection approximation layers declared);
             homogenization universality for (C).
Part III:    O9 RESOLVED (structural; fifth role; (2,2) selection);
             O11 mechanism + audited linear law (defect <= 0.06 sigma);
             coordination law CORRECTS R4's dimension reading
             (triangular orders in 2d; z, not d, is the control);
             single-observable O6 CLOSED (residue = process-level);
             O5 CLOSED at free scope (record GW exact, aliasing
             destroys the species); O7 probe data measured
             (r = 0.85 -> 0.68 below the iid baseline).
Kernel:      {(R-)''' reduced to process-level O6, (C), (M) enriched,
             (V)} + opens {O7 (sign), O8 (interacting), O11 (constant),
             process-O6} + Paper 9's {D9a, D10} and the
             interacting-GW residue of O5; D9b executed by Paper 11.
             [Paper 11 Part III updates: D9a DISCHARGED (fermions
             forced); the O11 constant is uniform-in-L (decreasing) with
             exact per-family leading-order values; process-O6 is
             located as the positive-realization problem; the sigma-
             circle on statistics is closed by even-time positivity.]
```

## References and literature map

- Papers 4-9 (internal): the exchange cocycle (P4 s34), admissible
  refinements (P4 s48-51), self-accounting and the commitment law (P4
  s71), detailed-balance verification (P6.1 s5.7), the commitment cubic
  (P7 s8.2), typed moment classes and certificates (P8 s6), the
  plaquette character mechanism (P8 s9), record-SSB (P8 s8), axiom (X)
  and D9 (P9 s7, s11).
- A. N. Kolmogorov, Math. Ann. 112, 155 (1936): the cycle criterion for
  reversibility.  J. Schnakenberg, Rev. Mod. Phys. 48, 571 (1976):
  network thermodynamics, cycle affinities, entropy production.
- G. E. Crooks, Phys. Rev. E 60, 2721 (1999); C. Maes, J. Stat. Phys. 95,
  367 (1999): entropy production as the forward/reverse path KL rate -
  the classical face of T2.
- A. Klein and L. J. Landau, J. Funct. Anal. 42, 368 (1981): OS
  positivity and reconstruction for reversible Markov processes - the
  classical import behind T4.
- A. A. Migdal, Sov. Phys. JETP 42, 743 (1975); L. P. Kadanoff, Ann.
  Phys. 100, 359 (1976): the MK recursion of R3/R5.  K. G. Wilson and
  J. Kogut, Phys. Rep. 12, 75 (1974): the RG frame.
- L. Onsager, Phys. Rev. 65, 117 (1944): the exact 2d energy and
  correlation length used in R4 (see also R. J. Baxter, *Exactly Solved
  Models*, 1982).
- A. Bensoussan, J.-L. Lions, and G. Papanicolaou, *Asymptotic Analysis
  for Periodic Structures* (1978): homogenization (R6).
- P. H. Ginsparg and K. G. Wilson, Phys. Rev. D 25, 2649 (1982);
  W. Bietenholz and U.-J. Wiese, Nucl. Phys. B 464, 319 (1996);
  P. Hasenfratz, V. Laliena, and F. Niedermayer, Phys. Lett. B 427, 125
  (1998): the GW relation as a block-RG fixed-point condition and the
  perfect-action construction instantiated in Section 4.5.
- J. A. Barandes (2302.10778, 2309.03085): the indivisible/non-Markov
  process structure that Part I's architecture realizes (events break
  Markovianity, eventless collars are order-blind).
