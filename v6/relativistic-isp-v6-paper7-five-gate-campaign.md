# Paper 7 (v6) - SHARD: The Five-Gate Campaign and the Cosmological Term

Subtitle:

```text
Signature from commitment, tensor source from the frame-resolved coboundary,
the record equivalence principle, the native phase algebra, the (R-) and (Q)
reductions, and Lambda as sealed state data
```

## 0. Verdict

This campaign was run under one instruction: do not stop on obstructions.
The honest execution of that instruction is the method Paper 6 already used
on A_rec — when a gate cannot be closed as posed, find the invariant
reformulation under which it either closes, dissolves, or reduces to a
strictly smaller named kernel, and prove the reformulation. Fabricating a
closure of, say, the hierarchy value or the cosmological-constant value would
be determinacy by declaration; this corpus rejects that move, and so does
this paper.

The outcome, gate by gate:

```text
Gate 2a (Lorentzian signature):           CLOSED. PROVED-FINITE.
  Signature emerges from monotone commitment: an invariant proper
  record-order cone excludes SO(2) and forces SO(1,1).

Gate 2b (tensor source + conservation):   CLOSED at finite scope.
  T is the frame-resolved interface coboundary; symmetry and exact internal
  seam cancellation (conservation) are identities; the Paper 5 pressure
  attack is separated.

Gate 2c (focusing limit, linearized):     CLOSED at the stated scope.
  O(delta^2) convergence to the Raychaudhuri integral, machine-verified.

Gate 2d (contracted Bianchi):             CLOSED. Exact finite identity
  (boundary-of-boundary = 0).

Gate 2e (covariant continuum convergence): REDUCED to gate (C), the
  spectral-convergence theorem, with every finite precondition now proved.

Gate 1 (axiom (R)):                       REDUCED to (R-).
  New no-go: no derived structure selects beta. New finite theorem: the
  defect-free rotation-invariant Euclidean record field is EXACTLY thermal
  at beta = total angle. Hence (R) shrinks to (R-): existence of the
  Euclidean record extension. Given (R-), beta = 2*pi is proved.

Gate 3 (H1, equivalence principle):       CLOSED. PROVED-FINITE.
  The gravity source factors through the primitive RN/KL quotient:
  species-blindness is quotient functoriality.

Gate 4 (H2, hierarchy):                   DISSOLVED as a gravity question,
  BOUNDED as a record question. The gravity sector is complete and
  provably blind to m_hat; m_hat <= cell capacity (record-Bekenstein);
  the selection of m_hat is the matter sector's spectrum problem.

Gate 5 (Born/measurement reconstruction): REDUCED to (Q), with B1 DERIVED.
  The phase group is the defect-free rotation group U(1) with canonical
  period 2*pi - the same 2*pi as the temperature. Given (Q) (route-algebra
  representation), Frobenius/Gelfand-Mazur forces the algebra to be C;
  quaternionic phases are excluded by abelian screen holonomy; split
  signature is excluded by negative event weights; Born follows.

Cosmological term:                        DISSOLVED as a law constant.
  Lambda_hat is identified: the trace part of the raw deletion source,
  fixed by sealed solvability to kappa_hat times the mean commitment
  density. It is state data. The Section 8 moduli-point claim of Paper 6 is
  repaired accordingly. The residual "record coincidence problem" (why the
  mean commitment density of the cosmological packet is small) is named.
```

The kernel after Paper 7 is five named items - (R-), (C), (Q), the matter
spectrum, and the record coincidence value - each with an identified attack
route, two of which ((R-) and (Q)) point at one and the same missing
structure.

## 1. Method

Einstein's answer to "what is the gravitational force law" was that the
question was wrong: there is no force, there is geometry. Paper 6's answer
to "what selects A_rec" was that the question was wrong: there is no
physical A_rec, there is kappa*sigma_A. This paper applies the same
operation five more times. Where the result is a closure, it is proved.
Where the result is a dissolution, the wrongness of the original question is
proved. Where the result is a reduction, the equivalence to the smaller
kernel is proved and the kernel is named. Nothing is closed by declaration.

## 2. Gate 1: the (R) -> (R-) reduction

Diagnostic script:

```text
code/v6_p7a_euclidean_transfer_campaign.py
```

### 2.1 No-go: derived structure does not select beta

**Theorem 2.1.** The Gibbs(beta) family on a boost collar satisfies, for
every beta >= 0: passivity, complete passivity, product gluing, and detailed
balance. Hence the structures derived in Papers 6-6.1 leave beta as a
one-parameter family.

**Proof.** Anti-ordering of e^{-beta K} is immediate for beta >= 0
(Lemma 1 of Paper 6.1 then gives passivity at every tensor power); gluing
and detailed balance hold identically in beta. ∎

Machine: beta in {1, 2*pi, 10} all pass with gaps <= 1.1e-16. A selection
principle must therefore add structure. The question is: how little?

### 2.2 Finite transfer theorem: beta equals the total Euclidean angle

**Theorem 2.2 (finite Osterwalder-Schrader/Matsubara mechanism).** Let a
rotation-invariant Gaussian record field live on the defect-free Euclidean
collar circle of total angle Theta (discretized at M sites, lattice action
sum over sites of (x_{k+1}-x_k)^2/(2 delta) + omega^2 delta x_k^2 / 2,
delta = Theta/M). Then the single-ray law and the full angular correlator
are those of the thermal oscillator at inverse temperature

```math
\beta=\Theta,
```

exactly in the continuum limit and with O(delta^2) lattice corrections:

```math
C(\tau)
=
{\cosh\!\big(\omega(\Theta/2-|\tau|)\big)\over 2\omega\,\sinh(\omega\Theta/2)} .
```

**Proof.** The angular transfer kernel of the Gaussian chain is the
imaginary-time oscillator kernel; composing it once around the circle and
closing the trace gives the periodized chain, whose marginal is the Gibbs
state e^{-Theta H} of the transfer generator H. The temperature is the
total angle because the trace closes after total angle Theta - "the
rotation that returns is the trace." The explicit covariance is the
standard periodic Green's function above. ∎

Machine verification:

```text
Theta = 2*pi: max rel error vs thermal(beta=Theta):
  M=100: 8.317e-04   beta_fit = 6.285036040
  M=400: 5.204e-05   beta_fit = 6.283301279
  M=1600: 3.253e-06  beta_fit = 6.283192666   (Theta = 6.283185307)
Theta = pi (conical):
  M=1600: 7.771e-07  beta_fit = 3.141594480   (Theta = 3.141592654)
KMS periodicity |C(tau) - C(Theta - tau)| = 1.2e-14
```

The conical row shows the same mechanism assigning beta = Theta to a
defected collar - which is exactly how the silent-seam theorem then acts:
the defected collar is excluded, so only beta = 2*pi survives.

### 2.3 The reduction

**Definition (R-).** The eventless boost correlations of a sealed collar are
the ray restriction of SOME rotation-invariant record field on the
defect-free Euclidean collar.

**Theorem 2.3.** (i) (R-) implies beta = 2*pi (Theorem 2.2 plus the
silent-seam period theorem). (ii) (R-) is strictly weaker than axiom (R):
it asserts existence of an extension, not analyticity of a continuation,
and Theorem 2.2 supplies the analytic content that (R) previously carried.
(iii) Without (R-), beta is free (Theorem 2.1): (R-) is exactly the minimal
remaining kernel of gate 1.

**Proof.** (i) is composition of the two proved theorems. (ii): any analytic
continuation provides an extension; the converse direction is precisely
what Theorem 2.2 now proves finitely, so the analytic half of (R) is
discharged. (iii) is Theorem 2.1. ∎

The residue (R-) is the record form of reflection positivity. The named
attack route: the exchange-cocycle antisymmetry A_D = log dP_AB/dP_BA of
Paper 4 Section 34 is a reflection structure on ordered transports; proving
that the eventless cocycle data is reflection-positive would discharge (R-)
natively. This is the same noncommutative-ledger direction as gate 5's
kernel (Section 7.5).

### 2.4 Gate-1 diagnostic

| target | test | result | value | verdict |
|---|---|---|---:|---|
| beta family | Gibbs(beta) vs passivity/gluing/detailed balance | all pass for all beta | gaps <= 1.1e-16 | NOT-SELECTED-WITHOUT-EXTENSION |
| transfer theorem | defect-free Euclidean collar, Theta = 2*pi | thermal at beta = Theta | beta_fit -> 6.283193 (Theta = 6.283185) | BETA-EQUALS-ANGLE |
| conical control | Theta = pi | thermal at beta = pi | beta_fit -> 3.141594 | MECHANISM-CONFIRMED |
| KMS form | lattice correlator periodicity | exact | 1.2e-14 | PASS |
| reduction | (R) vs (R-) | analytic half discharged; existence half remains | minimal kernel named | (R)-REDUCED-TO-(R-) |

## 3. Gate 2a: signature from commitment

Diagnostic script (Sections 3-5 and 8):

```text
code/v6_p7b_signature_tensor_lambda_campaign.py
```

### 3.1 The native cone

The corpus supplies an arrow: commitment is irreversible. Division survival
S(I) = e^{-I} is monotone in evidence; committed divisions do not undo
(Paper 4 Section 71). Therefore the normal plane of a record screen carries
an intrinsic proper convex cone C: the directions of eventless transport
along which sealed evidence is non-decreasing. Eventless transports preserve
C, because a transport mapping evidence-increasing directions to
evidence-decreasing ones would un-order commitments - a silent rewrite of
the ledger, excluded by self-accounting.

### 3.2 Signature theorem

**Theorem 3.1.** Let the normal 2-plane carry a nondegenerate symmetric
bilinear form g (from the screen-stack metric data of Paper 4 Sections
16-21) and a proper convex cone C preserved by the eventless transport
group G, with G acting by g-isometries of unit determinant. Then g has
Lorentzian signature and the identity component of G is the boost group
SO(1,1)+.

**Proof.** If g were definite, its unit-determinant isometry group is
SO(2), which acts transitively on rays; a transitive action preserves no
proper cone (the orbit of any boundary ray covers all directions). Hence g
is indefinite: signature (1,1). The isometry group is then O(1,1); its
subgroup preserving a proper cone (the quadrant spanned by the two null
rays) is the identity-component boost group. Conversely boosts preserve the
null-ray quadrant. ∎

Machine: boosts preserve the cone at t = +0.5 and -1.2; rotations violate
it at a = 0.3, 1.0, 2.0; the rotation orbit of a single ray visits 60
distinct directions around the full circle (transitivity witnessed).

**Status.** Gate 2a is CLOSED at finite scope: Lorentzian signature is not
an input. It is the shadow of irreversible commitment - light cones are the
geometry of the fact that records accumulate. The previously presupposed
SO(1,1) typing of Z_perp (flagged in the post-6.1 review) is now derived.

## 4. Gate 2b: tensor source and conservation

**Theorem 4.1.** Define the per-cell tensor source as the frame-resolved
coboundary of the complete oriented interface cochain:

```math
T_i^{(ab)}
=
{\rm sym}\sum_{f\in\partial i}\varepsilon(f,i)\,n^a(f)\,h^b(f).
```

Then: (i) T is symmetric by construction; (ii) summing over any glued
subcomplex, internal faces cancel exactly - conservation is the seam
cancellation of Paper 4 Sections 44-47 in tensor dress; (iii) T separates
the Paper 5 Section 7.4 pressure-attack pair (equal scalar trace, different
anisotropy).

**Proof.** (i) by the symmetrizer; (ii) each internal face contributes with
opposite orientation signs to its two cells, so the glued sum telescopes to
boundary faces only - the cellular coboundary identity; (iii) trace equality
with component inequality is realized by isotropic versus anisotropic
cochain assignments. ∎

Machine: internal-seam cancellation 0.0e+00 exact; symmetry 0.0e+00; attack
pair: trace gap 0, tensor gap 0.300.

**Status.** Gate 2b CLOSED at finite scope. The continuum limit of T rides
on gate (C).

## 5. Gates 2c-2e: focusing, Bianchi, and the convergence kernel

**2c (focusing).** The finite null focusing of Paper 4 Sections 22-27,
integrated with the midpoint scheme, converges to the linearized
Raychaudhuri integral at second order: errors 4.682e-09 (n=100) and
2.940e-10 (n=400), ratio 15.9 against the O(delta^2) prediction 16. CLOSED
at the linearized scalar-channel scope.

**2d (Bianchi).** On the finite cell complex, boundary-of-boundary
vanishes identically: |d1 d2| = 0.0e+00, and the coboundary-built source
sums to zero over any closed complex (0.0e+00). The contracted Bianchi
identity is an exact finite identity, not a limit statement. CLOSED.

**2e (the kernel).** What remains of gate 2 is one theorem:

```text
Gate (C): controlled sealed-diamond refinements (the tightness class of
Paper 4 Sections 48-51) converge spectrally to a Lorentzian 4-geometry on
which the limits of L, T, the focusing identity, and the Bianchi identity
are the continuum operators and identities.
```

Every finite precondition of (C) is now proved (2a-2d above; G1
equivariance from Paper 6.1). (C) itself is a convergence/representation
theorem of the spectral-geometry type. It is the honest irreducible kernel
of gate 2 and is OPEN, with its attack technology named (spectral
convergence of operators under the corpus' own tightness gates).

## 6. Gate 3: H1, the record equivalence principle - CLOSED

Diagnostic script (Sections 6-7):

```text
code/v6_p7c_equivalence_bound_algebra_campaign.py
```

**Theorem 6.1 (quotient functoriality of the source).** The gravity source
and response maps factor through the primitive RN/KL quotient ledger of
Paper 4 Sections 73-76. Consequently, any two matter species whose events
commit equal RN evidence into the same collar produce identical
gravitational response: one nat gravitates the same way regardless of the
ledger that produced it.

**Proof.** The source is built from RN functionals only: the deletion work
W_* (a saturation-law constant), the RN action A_D = log dP_AB/dP_BA
(Paper 4 Section 34, with its covariance identities under law-preserving
relabelings), and the evidence ledger. RN functionals are invariant under
species isomorphisms by construction (the RN derivative does not see
labels). The response equation consumes only the source and collar data.
The composite is therefore constant on quotient fibers. A species-dependent
coupling would require the source map to consume non-quotient data, which
is exactly the free-amplitude attack already refuted in Paper 4 Section 12
(FAILS-BRANCH-A) and is a covariance violation under pure relabeling. ∎

Machine: two engineered ledgers (d=3 and d=4) each committing exactly one
nat (evidence 0.999999999999167 and 1.000000000000000); response gap
0.0e+00; relabeling invariance of evidence 0.0e+00; the species-tagged
coupling attack shifts the response by 2.149e-01 and changes under pure
relabeling of the same quotient datum: COVARIANCE-VIOLATED, rejected.

**Status.** H1 CLOSED. The equivalence principle is not an assumption of
record gravity; it is the statement that gravity couples to evidence and
evidence is species-blind. For the energy form (equal modular energy =>
equal footprint), combine with the universal temperature of gate 1: the
energy version is conditional on (R-) only.

## 7. Gates 4 and 5

### 7.1 Gate 4: H2 dissolved as a gravity question, bounded as a record one

**Theorem 7.1 (reclassification).** Given H1 and the pinned gravity sector
(Paper 6.1 Section 8), the hierarchy invariant equals the matter ledger's
evidence content per primitive event, m_hat. The gravity sector is complete
with respect to m_hat: no gravity-sector identity constrains it (the p6d
blindness scan), and none should - exactly as the Einstein equations do not
determine the electron mass. H2 is therefore not a hole in record gravity;
it is the matter sector's spectrum problem.

**Theorem 7.2 (record-Bekenstein bound).** A primitive event resolved in a
record cell of alphabet size d commits evidence at most the cell capacity:

```math
I_{\rm event}=D(P\Vert\mu_d)=\log d-H(P)\ \le\ \log d=C_{\rm cell},
```

with equality exactly at point-mass laws. Hence m_hat <= C_cell: elementary
record events sit at or below one capacity quantum - the record form of
"elementary masses at or below the Planck scale."

**Proof.** The identity D(P||uniform_d) = log d - H(P) and H(P) >= 0. ∎

Machine: d=3 capacity 1.098612, sampled maximum 1.081992, vertex 1.098612;
d=5 capacity 1.609438, vertex attained.

**Status.** Dissolution proved, bound proved, value OPEN and correctly
located: the successor is the matter sector's commitment-spectrum theorem.
Difficulty class as disclosed in Paper 6.1 Section 9: this is the hierarchy
problem, and no framework derives it.

### 7.2 Gate 5: the native phase algebra

The Born premises B1-B6 of Paper 5 are attacked at their root: where do
complex numbers come from?

**Theorem 7.3 (canonical phase group - B1 derived).** The retained holonomy
of a closed route pair on a sealed screen is valued in the holonomy group
of the 2-dimensional screen plane: the defect-free rotation group SO(2) =
U(1) with canonical period 2*pi (the silent-seam theorem). A retained
alternative therefore carries canonically a nonnegative RN weight and a
U(1) phase: the value space of an alternative is R+ x U(1) cup {0} = C as a
SET, with the canonical 2*pi. ∎

This is the same 2*pi as the modular temperature: the compact period that
fixes T = 1/(2*pi) is the period of quantum phase. One native constant,
two faces.

**Definition (Q).** The retained record of a finite route family is carried
by a representation of the route semiring (alternatives = disjoint union,
concatenation/independence = product) in a finite-dimensional continuous
commutative unital R-algebra in which eventless transports act invertibly.

The ingredients of (Q) are individually native or proved: associativity and
commutativity of merging are sealed-gluing associativity and relabeling
covariance; distributivity is route-counting combinatorics; invertibility
is reversibility of eventless transport; finite dimensionality is finite
record capacity; commutativity of phases is Theorem 7.4 below. What (Q)
adds is only that the bookkeeping is algebraic - a single structural axiom
replacing the six postulates B1-B6.

**Theorem 7.4 (quaternionic exclusion).** Screen-plane holonomies commute
(any two rotations of one 2-plane commute: machine 0.0e+00), while unit
quaternions do not (|ij - ji| = 2.000). Hence the phase object cannot be
H-valued: quaternionic quantum mechanics is excluded by the
2-dimensionality of the screen. ∎

**Theorem 7.5 (the algebra is C).** Under (Q), the carrying algebra is a
finite-dimensional commutative unital real division algebra containing the
nontrivial compact one-parameter group of Theorem 7.3. By the
Frobenius/Gelfand-Mazur classification the algebra is R or C; R contains no
nontrivial compact one-parameter group; hence the algebra is C, merging is
complex addition (B2), independence is complex multiplication (B6). ∎

Machine (2-dimensional commutative unital algebras, e^2 = s): s = -1 (C)
has no nonzero non-invertible elements; s = +1 (split) and s = 0 (dual)
both do - the division property singles out C.

**Theorem 7.6 (split-signature exclusion).** If the phase group is taken
non-compact (split-complex e^{j phi}, j^2 = +1 - the would-be "boost
phase"), two-route composition yields event weights W+- = 1 +- cosh(phi):
total weight is conserved (2.0000) but W- = -0.5431 at phi = 1 and -2.7622
at phi = 2. Negative event weights violate positivity: REJECTED. The phase
group must be the compact normal factor - which Theorem 7.3 supplies. ∎

**Corollary (Born).** With (Q): the algebra is C (7.5), phases are U(1)
(7.3), H is excluded (7.4), split is excluded (7.6); weight conservation
under admissible screen transports then gives B3 (the invariance theorem of
Papers 5-6), B4-B5 follow as in Paper 5 Section 3, and the finite Born
theorem applies unchanged (machine: interference table 1.000, 0.750,
0.500, 0.000 recovered).

**Status.** Gate 5: B1 DERIVED; B2-B6 reduced to the single axiom (Q);
the rival number systems excluded by proved theorems. The kernel (Q) has a
named attack route: exhibit the representation as the unistochastic
dilation of the indivisible whole-history law - the Barandes correspondence
direction already listed as the program's comparison target. Notably this
is the same noncommutative-completion structure that would discharge (R-):
the two deepest kernels are one construction.

## 8. The cosmological term: Lambda dissolved as a law constant

**Theorem 8.1 (identification).** In the sealed response equation the raw
deletion source decomposes uniquely as

```math
\rho_{\rm raw}=\big(\rho_{\rm raw}-\bar\lambda\,\mathbf 1\big)+\bar\lambda\,\mathbf 1 ,
```

and the trace part enters exactly as a cosmological term. In a closed
sealed packet the constant mode of L is gauge, so solvability forces

```math
\hat\Lambda=\hat\kappa\,\bar\lambda=\hat\kappa\cdot{\rm mean}(\rho_{\rm raw})
=2\pi\,W_*\,\bar E :
```

the cosmological term is kappa_hat times the mean commitment density of the
packet. It is sealed STATE data - exactly the "integration data"
classification of Paper 5 Section 12.4, now with its record meaning fixed -
and not a law coupling.

**Proof.** The image of L is the mean-zero subspace; L phi = kappa_hat
(rho_raw - c 1) is solvable iff c = mean(rho_raw); the subtracted constant,
moved to the left side, is by definition the Lambda term of the response
equation. ∎

Machine: sparse packet (3 of 8 cells divided): Lambda_hat = 0.859504294,
solvable to 1.0e-15, fails at half value (residual 4.298e-01); dense packet
(6 of 8): Lambda_hat = 1.719008588, residuals likewise. Same laws, two
packets, two Lambda_hat values: state-dependence demonstrated.

**Repair of Paper 6.1 Section 8.** The moduli-point claim is restated:

```text
the moduli space of LAW couplings of the gravity/record sector is a point;
Lambda_hat is a sealed state datum fixed per packet by the solvability
identity, not a modulus of the law.
```

**The residue, named.** Why the mean commitment density of the cosmological
packet is small in record units - the record coincidence problem - is OPEN.
It is the record form of "why is Lambda ~ 1e-122 in Planck units," shared
with all of physics; the identification above relocates it from "unknown
constant in the law" to "property of the state," which is the unimodular
classification, and the natural direction (the mean division density of an
old, large-capacity packet is generically small) is noted as a direction,
not claimed as a solution.

## 9. The kernel after Paper 7

```text
(R-)  existence of the defect-free Euclidean record extension of eventless
      correlations.            Attack: reflection positivity of the
      exchange-cocycle antisymmetry; noncommutative ledger.
(C)   spectral convergence of controlled sealed refinements to a Lorentzian
      4-geometry.              Attack: spectral-geometry convergence under
      the corpus' tightness gates; all finite preconditions now proved.
(Q)   the route-algebra representation.
                               Attack: unistochastic dilation of P_hist
      (the Barandes correspondence target); same structure as (R-).
(M)   the matter commitment spectrum (selects m_hat within the proved bound
      m_hat <= C_cell).        Attack: construct a matter sector with its
      own commitment-fixed ledger; this is mass generation.
(V)   the record coincidence value (the size of mean commitment density of
      the cosmological packet). Attack: state selection / packet history,
      not law modification.
```

Two structural facts about this kernel: (R-) and (Q) are plausibly one
construction (the noncommutative/dilation completion of the record
ledger), and (M) and (V) are properties of states and sectors, not of the
gravitational law - the law side of the program is, after this paper,
complete up to (R-) and (C).

## 10. What this paper proves and does not prove

Proves: Theorems 2.1-2.3 (beta no-go, transfer theorem, (R) reduction);
Theorem 3.1 (signature from commitment); Theorem 4.1 (tensor source,
conservation, pressure-pair separation); the 2c convergence and 2d exact
Bianchi statements; Theorem 6.1 (H1); Theorems 7.1-7.2 (H2 reclassification
and record-Bekenstein bound); Theorems 7.3-7.6 and the Born corollary
(B1 derived; B2-B6 reduced to (Q); H and split-signature excluded);
Theorem 8.1 (Lambda identification and solvability) - each with machine
verification at the printed values.

Does not prove: (R-), (C), (Q), the matter spectrum (M), the coincidence
value (V) - and states why each is the honest residue rather than a gap
that further campaigning of the present kind could close: (R-)/(Q) need a
new completion structure; (C) needs convergence technology; (M) and (V)
need a matter sector and a state theory that do not yet exist. Claiming
otherwise would be the determinacy-by-declaration this corpus exists to
reject.

## 11. Status

```text
Signature:        derived from irreversible commitment (cone theorem).
Tensor source:    frame-resolved coboundary; conservation = seam
                  cancellation; pressure attack separated.
Focusing/Bianchi: linearized limit O(delta^2); Bianchi exact and finite.
Temperature:      beta-family no-go proved; beta = total angle proved
                  finitely; (R) reduced to (R-); given (R-), T = 1/(2*pi).
Equivalence:      H1 proved by quotient functoriality; species-tagged
                  couplings refuted by covariance.
Hierarchy:        dissolved as a gravity question; bounded by capacity;
                  selection = matter spectrum problem (M).
Phase algebra:    B1 derived (U(1), period 2*pi - the temperature's 2*pi);
                  B2-B6 reduced to (Q); H and split-complex excluded;
                  Born recovered under (Q).
Lambda:           identified as kappa_hat x mean commitment density; state
                  datum; Paper 6.1 moduli claim repaired; coincidence value
                  (V) named.
Kernel:           {(R-), (C), (Q), (M), (V)}; (R-) and (Q) share one
                  attack; the gravitational LAW is complete modulo (R-),(C).
```

## References and literature map

- Papers 4-6.1 (internal): commitment and self-accounting (P4 s71), the
  exchange cocycle and its covariance (P4 s34), seam/coboundary discipline
  (P4 s44-47), tightness/refinement gates (P4 s48-51), the pressure attack
  (P5 s7.4), the silent-seam period theorem and passivity theorem (P6/6.1).
- K. Osterwalder and R. Schrader, "Axioms for Euclidean Green's functions,"
  Commun. Math. Phys. 31, 83 (1973): the continuum form of the (R-) kernel
  and the mechanism finitized in Theorem 2.2.
- F. G. Frobenius (1878); Gelfand-Mazur theorem: the classification behind
  Theorem 7.5. S. L. Adler, *Quaternionic Quantum Mechanics and Quantum
  Fields* (1995); M. P. Soler, "Characterization of Hilbert spaces by
  orthomodular spaces" (1995): the rival-number-system landscape excluded
  in Theorems 7.4/7.6.
- E. C. Zeeman, "Causality implies the Lorentz group," J. Math. Phys. 5,
  490 (1964); D. Malament, "The class of continuous timelike curves
  determines the topology of spacetime," J. Math. Phys. 18, 1399 (1977):
  the order-to-Lorentz tradition behind Theorem 3.1.
- S. Weinberg, "The cosmological constant problem," Rev. Mod. Phys. 61, 1
  (1989); M. Henneaux and C. Teitelboim, "The cosmological constant and
  general covariance," Phys. Lett. B 222, 195 (1989): the
  unimodular/integration-constant classification realized finitely in
  Theorem 8.1.
- J. A. Barandes, the stochastic-quantum correspondence
  (`https://arxiv.org/abs/2302.10778`): the dilation target named as the
  attack on (Q).
- T. Jacobson (gr-qc/9504004), W. G. Unruh (1976), Bisognano-Wichmann
  (1976), Pusz-Woronowicz (1978), Lenard (1978), Dicke (1962),
  Duff-Okun-Veneziano (physics/0110060), Regge (1961): as in Papers 6-6.1.
