# Independent hostile review — operator algebra / effectus

**Overall verdict: `ACCEPT-WITH-FIXES`**

**Governing pin:** `e9948073c38a96e92c9b17bbe1009b1fc1337788`  
**Immutable paper:** `a57bed6511fd21511d5e25bf351ef5c371ed7d07`  
**Review mode:** independent, mathematical hostile review, repository read-only  
**Date:** 2026-07-31

No repository file was edited. The final worktree and paper/pin diff checks were clean. Scratch calculations created no repository artifacts.

## 1. Executive disposition

The paper’s load-bearing mathematics survives independent reconstruction:

- general UCP maps give total effect and fixed-outcome POVM transport;
- supplied instruments precompose correctly and have the claimed effect shadow;
- the Kadison–Schwarz defect, projection criterion, both chain laws, positivity qualification and unitary covariance are correct;
- sharpness of every atom of a finite PVM is sufficient to put the generated record algebra in the multiplicative domain;
- `SharpRec_D` and both record functors have the stated displayed-Heisenberg variance;
- the operator-system construction is minimal, monotone, covariant and spectator-clean;
- the Karoubi completion and fixed-range claims are correctly typed;
- the random-unitary, amplitude-damping, noisy-chain, branch-memory, instrument-disturbance, symmetry and idempotent controls all have the claimed exact answers;
- no additional finite word in the declared symmetry grammar is an idempotent below the two stated minima;
- the pin’s literal no-containing-idempotent branch is mathematically impossible because identity is admitted. Replacing it by “no proper containing idempotent / identity only” is a valid logical correction, not evasion.

Three nonfatal corrections are required:

1. the symmetry-word proof does not explicitly handle the trailing-\(\alpha\) normal form, although its conclusion is correct;
2. universal and temporal prose about instrument and “upstream or downstream” transport is broader than the displayed Heisenberg pullback and full-matrix instrument theorem;
3. reference 9 gives incorrect author initials.

These do not change any theorem or cumulative rung.

## 2. Artifact and antecedent integrity

The paper commit is the direct child of the governing pin:

\[
a57bed6^\wedge=e994807.
\]

| Artifact | Immutable scope | SHA-256 | Size |
|---|---|---|---:|
| successor pin | `e994807:v13/note-rq0-w3-effect-transport-pin.md` | `6b68c1a545ab13cb998855d8cec688008a63aba1448fb1d966504f0ba9ed6db1` | 17,859 bytes; 622 lines |
| paper | `a57bed6:v13/paper-rq0-sharp-facts-unsharp-evidence.md` | `6de7743ba614074ca51c68564bd441b870c8210e6f30d49daf3fc297c2970da5` | 58,386 bytes; 1,918 lines |
| Weld paper | `f57eb45:v13/paper-rq0-weld-stack-foundations.md` | `30dcec41d9944780cf9289be16f7f7cbcccd4ddab5ff5a9cebdb3e603d493fda` | 64,293 bytes; 1,952 lines |
| higher Weld report | `ecdd3b7:v13/note-rq0-weld-stack-higher-hostile-review.md` | `128d186d54245619991d45cab1d31d1076937e565a8d2a8777a4fd4e0d5d98ce` | 32,071 bytes; 313 lines |
| operator Weld report | `cbcc9a5:v13/note-rq0-weld-stack-operator-hostile-review.md` | `f108c87937fa88ee929df0e4200f2b6281450f4976e705f8a44b20b7b11e5ba1` | 26,039 bytes; 508 lines |
| joint adjudication | `874d5a1:v13/note-rq0-weld-stack-hostile-adjudication.md` | `901b32139ca6441bee2da4e1e5c8b7d7b7ee9b517a8cd44ab84233288e64d18f` | 17,585 bytes; 461 lines |
| terminal RQ0-A note | `9d8828b:v13/note-rq0-physical-overlap-repair.md` | `cadc7953004f7124160f325929d05fe651f18182a00df1ffd48652eab025546f` | 22,002 bytes; 578 lines |

The inherited scopes are preserved:

- `RQ0-L0-REPRESENTABLE-W3-SKETCH` survives unchanged.
- The Weld chart, Boolean-`Rec`, quantaloid-chart and stack headlines remain withdrawn.
- Terminal RQ0-A remains a finite declared-instrument, signed-permutation/isometric projector-pullback result only.
- The present paper does not promote either antecedent into intrinsic localization or generic overlap.

## 3. Findings requiring correction

### F1 — proof-completeness fix: odd-\(\alpha\) symmetry words

Paper lines 1579–1597 correctly analyze alternating words in \(D_n,D_m\), then say that

\[
\alpha D_n\alpha=D_m,\qquad \alpha^2=I
\]

reduces every word containing \(\alpha\) to those cases. Literally, these relations leave an odd word in the form \(W\alpha\); they do not eliminate its trailing \(\alpha\). Thus the printed reduction is incomplete.

The missing case does not produce a counterexample. On Bloch vectors let

\[
P=nn^{\mathsf T},\qquad Q=mm^{\mathsf T},\qquad R=\alpha_{\rm Bloch},
\qquad c=n\cdot m=\frac12,
\]

with \(Rn=m\), \(Rm=n\), and \(R^2=I\). Every word has normal form

\[
W(P,Q)R^\varepsilon,\qquad \varepsilon\in\{0,1\},
\]

where, after deleting repetitions, \(W=P_{u_1}\cdots P_{u_\ell}\) is alternating. Then

\[
W=c^{\ell-1}u_1u_\ell^{\mathsf T}.
\]

For \(\varepsilon=0\), its only nonzero Bloch eigenvalue is

\[
c^{\ell-1}(u_\ell\cdot u_1),
\]

which equals one only for \(\ell=1\), namely \(P\) or \(Q\).

For \(\varepsilon=1\), the only nonzero Bloch eigenvalue is

\[
c^{\ell-1}(Ru_\ell\cdot u_1)
=
\begin{cases}
c^\ell,&\ell\ \text{odd},\\
c^{\ell-1},&\ell\ \text{even}.
\end{cases}
\]

It is strictly between zero and one for every \(\ell\ge1\). The empty \(W\) gives \(R\), and \(R^2=I\ne R\). Hence the only idempotents in the generated monoid are

\[
I,\quad D_n,\quad D_m.
\]

The stated minima and no-selection conclusion are therefore correct; only the displayed normal-form proof needs completion.

The Karoubi isomorphism can also be typed explicitly. With

\[
f=e_m\alpha e_n=\alpha e_n,\qquad
g=e_n\alpha e_m=\alpha e_m,
\]

one has \(gf=e_n\) and \(fg=e_m\). Thus the two candidates genuinely lie in one physical-symmetry action groupoid.

### F2 — scope and terminology fixes

The formal variance is correct, but some prose is too broad.

First, a Heisenberg arrow

\[
F:B_{\text{record}}\to A
\]

pulls a record effect backward along the corresponding Schrödinger process \(A_*\to B_{\text{record},*}\). It does not canonically push a native record observable forward through an arbitrary downstream Schrödinger channel. Phrases such as “an upstream or downstream channel can blur” and “a later or earlier noisy view” should be read only as referring to boundaries for which an admitted Heisenberg arrow out of the record algebra has actually been supplied. No theorem itself uses the broader reading.

Second, Section 4 proves instrument precomposition on full matrix systems,

\[
\mathcal I_r:\mathcal T(H_A)\to\mathcal T(H_B),
\]

while the opening channel category permits general finite-dimensional unital C*-algebras. The theorem register does narrow the instrument statement to finite-dimensional Schrödinger CP maps, so the displayed theorem is correct. The abstract’s “every admitted UCP map … transports full instruments” needs either that matrix-algebra restriction or the standard finite-C*-predual formulation.

Third, “identity-only/global” must not be confused with

\[
\mathcal S_W(y)=B.
\]

Control 12.2 has a proper \(\mathcal S\) but only identity as an admitted containing idempotent; Control 12.3 is the distinct case \(\mathcal S=B\). The former means globally addressable only relative to the declared idempotent grammar, not global observability in the algebraic sense.

### F3 — bibliographic correction

Reference 9 names the authors as “A. Mestoudjian, M. Wilson, N. Vanrietvelde and P. Arrighi.” The primary arXiv record gives **Octave Mestoudjian, Matt Wilson, Augustin Vanrietvelde and Pablo Arrighi**. The correct initials are O., M., A., P. [The source is used only as comparison](https://arxiv.org/abs/2511.09494), so this has no mathematical consequence.

## 4. Primary-source audit

The cited sources support the scopes assigned to them:

- The effect-module and sharp/unsharp predicate background agrees with [Cho–Jacobs–Westerbaan–Westerbaan](https://arxiv.org/abs/1512.05813) and [Jacobs](https://arxiv.org/abs/1205.3940). The paper’s UCP restriction proof is self-contained and needs only positivity, unitality and linearity.
- The multiplicative-domain definition and homomorphic restriction agree with [Choi–Johnston–Kribs](https://arxiv.org/abs/0811.0947), especially its unital theorem, and ultimately Choi’s [Schwarz-inequality paper](https://doi.org/10.1215/ijm/1256051007).
- The supplied-instrument/effect-shadow distinction is consistent with [Davies–Lewis](https://doi.org/10.1007/BF01647093) and Ozawa’s result relating CP instruments to measurement-induced state change, [DOI 10.1063/1.526000](https://doi.org/10.1063/1.526000).
- The range-product statement is exactly the [Choi–Effros theorem](https://doi.org/10.1016/0022-1236(77)90052-0); a concise theorem statement is also available in [Prunaru’s proof](https://arxiv.org/abs/1304.6664).
- The ordinary-subalgebra/bimodule distinction agrees with [Tomiyama’s norm-one projection theorem](https://doi.org/10.3792/pja/1195524885).
- The categorical comparison to freely split CP idempotents is accurately limited to background; [Heunen–Kissinger–Selinger](https://arxiv.org/abs/1308.4557) is not used to prove physical admission.

No cited source supplies a missing physical idempotent or turns a POVM into an instrument. No citation is doing hidden work in place of an invalid finite calculation.

## 5. Variance, effects and instruments

### 5.1 Displayed-Heisenberg variance

The convention

\[
G:C\to B,\qquad F:B\to A,\qquad F\circ G:C\to A
\]

is used consistently.

- \(\operatorname{POVM}_\Omega(F)\) maps \(\operatorname{POVM}_\Omega(B)\) to \(\operatorname{POVM}_\Omega(A)\), so it is covariant along displayed Heisenberg arrows.
- In \(\mathsf{POVMIfc}_\Omega(D)\), an arrow
  \[
  h:(A,\mathbf E)\to(A',\mathbf E')
  \]
  is \(h:A\to A'\) with \(h(E_r)=E'_r\), the correct category-of-elements orientation.
- In \((B_W\downarrow\mathsf{Chan}_D)\), objects are \(F:B_W\to A\), and an arrow \(F\to F'\) is \(h:A\to A'\) with \(hF=F'\). Therefore
  \[
  h(F(P_r))=F'(P_r)
  \]
  types `Rec_eff`.
- `SharpRec_D` sends \(F:(B,R_B)\to(A,R_A)\) to the Boolean map
  \[
  \operatorname{Proj}(R_B)\to\operatorname{Proj}(R_A),
  \]
  again covariantly in displayed Heisenberg direction.
- Instrument precomposition
  \[
  \mathcal I_r\circ\Lambda:\mathcal T(H_C)\to\mathcal T(H_B)
  \]
  has shadow \(\Lambda^*(E_r)\in B(H_C)\), which matches the same reversal relative to Schrödinger evolution.
- The Karoubi arrow \(f:(B,e)\to(C,d)\) is an ambient \(f:B\to C\) satisfying \(f=dfe\), the standard direction.
- The RQ0-A map \(a\mapsto J^*aJ\) goes from target observables to source observables, as required.

Thus “contravariant” is consistently used only relative to the physical Schrödinger process.

### 5.2 Effects and POVMs

For \(0\le a\le I_B\),

\[
F(a)\ge0,\qquad I_A-F(a)=F(I_B-a)\ge0,
\]

so \(F(a)\in\operatorname{Eff}(A)\). Linearity and unitality preserve zero, unit, complement, \([0,1]\)-scalars and every defined finite partial sum. Identities and composition are exact.

For a finite PVM \((P_r)\),

\[
F(P_r)\ge0,\qquad
\sum_rF(P_r)=F(I)=I,
\]

so the image is a POVM. No projection claim is made without the separate defect/MD proof.

If every member of a normalized finite POVM is a projection, normalization forces orthogonality: for fixed \(i\),

\[
0=P_i(I-P_i)P_i=\sum_{j\ne i}P_iP_jP_i,
\]

and each summand is positive, hence \(P_jP_i=0\). The paper’s PVM criterion is correct.

### 5.3 Instrument shadow and disturbance

For an instrument \(\mathcal I\),

\[
E_r=\mathcal I_r^*(I)\ge0,\qquad
\sum_rE_r=\Bigl(\sum_r\mathcal I_r\Bigr)^*(I)=I.
\]

If \(\Lambda\) is CPTP, then every \(\mathcal I_r\Lambda\) is CP and trace-nonincreasing, their sum is CPTP, and

\[
(\mathcal I_r\Lambda)^*(I)=\Lambda^*(E_r).
\]

The Lüders and reprepare branches have explicit Kraus operators

\[
\mathcal L_r(\rho)=P_r\rho P_r,
\qquad
\mathcal J_r(\rho)=K_r\rho K_r^*,
\qquad
K_r=|+\rangle\langle r|.
\]

Both sums are trace preserving, both effects are \(P_r\), but

\[
\mathcal L_0(P_0)=P_0\ne P_+=\mathcal J_0(P_0).
\]

Thus the POVM/instrument/disturbance separation is exact.

## 6. Defect theorem and exact controls

For a UCP map \(F\),

\[
\Sigma_F(a)=F(a^2)-F(a)^2\ge0
\]

for self-adjoint \(a\) by Kadison–Schwarz. For a projection \(P\),

\[
\Sigma_F(P)=F(P)-F(P)^2,
\]

and \(F(P)\) is already a positive contraction, so zero defect is equivalent to \(F(P)\) being a projection.

Adding and subtracting \(F(G(a)G(b))\) gives exactly

\[
\Delta^{\rm rec}_{FG}(a,b)
=
F(\Delta^{\rm rec}_G(a,b))
+
\Delta^{\rm rec}_F(G(a),G(b)).
\]

For self-adjoint \(a\),

\[
\Sigma_{FG}(a)
=
F(\Sigma_G(a))
+
\Sigma_F(G(a)).
\]

Both terms are positive. If their sum vanishes, each vanishes, but a nonfaithful \(F\) need not detect \(\Sigma_G(a)\). An exact classical UCP example is

\[
G(x_0,x_1)=\left(\frac{x_0+x_1}{2},x_1\right),
\qquad
F(y_0,y_1)=y_1.
\]

For \(P=(1,0)\),

\[
\Sigma_G(P)=\left(\frac14,0\right)\ne0,
\qquad
F(\Sigma_G(P))=0,
\qquad
\Sigma_{FG}(P)=0.
\]

This independently confirms the paper’s qualification.

Under \(F'=\alpha_AF\alpha_B^{-1}\),

\[
\Delta_{F'}(\alpha_Ba,\alpha_Bb)
=\alpha_A(\Delta_F(a,b)),
\qquad
\Sigma_{F'}(\alpha_Ba)=\alpha_A(\Sigma_F(a)).
\]

Zero defect, positivity, spectrum and norm are presentation invariant.

### Exact arithmetic

For

\[
F_p(a)=(1-p)a+pXaX,
\]

one has

\[
F_p(P_0)=
\begin{pmatrix}1-p&0\\0&p\end{pmatrix},
\qquad
\Sigma_{F_p}(P_0)=p(1-p)I.
\]

Thus \(p=1/4\) gives \(3I/16\).

Composition satisfies

\[
F_pF_q=F_{p\star q},
\qquad
p\star q=p+q-2pq.
\]

At \(p=q=1/4\),

\[
p\star q=\frac38,\qquad
\Sigma_{F_{3/8}}(P_0)=\frac{15}{64}I.
\]

The chain terms are

\[
F_{1/4}\!\left(\frac3{16}I\right)=\frac{12}{64}I,
\qquad
\Sigma_{F_{1/4}}\!\left(\frac12I+\frac14Z\right)=\frac3{64}I.
\]

For amplitude damping with \(\gamma=1/2\),

\[
A^*(P_1)=\frac12P_1,
\qquad
\Sigma_{A^*}(P_1)=\frac14P_1.
\]

These are operator-product defects. No Born-shadow stochastic composition appears, so \(\Delta^{\rm rec}\) is not confused with \(\Delta^B\).

## 7. Multiplicative domain and sharp Boolean transport

A concise independent proof of the mixed multiplicative-domain identities uses a Stinespring representation

\[
F(x)=V^*\pi(x)V,\qquad V^*V=I.
\]

Define

\[
\Gamma(x,y)
=
F(x^*y)-F(x)^*F(y)
=
V^*\pi(x)^*(I-VV^*)\pi(y)V.
\]

This is a positive sesquilinear kernel. If \(\Gamma(x,x)=0\), then

\[
(I-VV^*)\pi(x)V=0,
\]

so \(\Gamma(x,y)=0\) for every \(y\). Applying the second Schwarz equality to \(x^*\) gives both

\[
F(xy)=F(x)F(y),\qquad
F(yx)=F(y)F(x).
\]

Consequently \(\operatorname{MD}(F)\) is a unital C*-subalgebra.

For every record atom \(P_r\),

\[
F(P_r)\text{ projection}
\iff
F(P_r)=F(P_r)^2
\iff
P_r\in\operatorname{MD}(F).
\]

Since the multiplicative domain is a C*-subalgebra, sharpness of every atom implies

\[
C^*(P_r:r\in\Omega)\subseteq\operatorname{MD}(F).
\]

This validates the load-bearing implication in Theorem 6.2. All five conditions there are equivalent.

For composable sharp arrows \(G\) and \(F\),

\[
G(R_C)\subseteq R_B\subseteq\operatorname{MD}(F)
\]

and \(R_C\subseteq\operatorname{MD}(G)\) imply

\[
(FG)(ab)=F(G(a)G(b))=FG(a)FG(b)
\]

for \(a,b\in R_C\), with the adjoint equalities giving membership in \(\operatorname{MD}(FG)\). Image containment composes as well. Therefore `SharpRec_D` is a category, and direct and composite Boolean maps agree exactly.

No injectivity or W6 co-reference follows. A Boolean homomorphism may collapse an atom to zero, and even an isomorphic Boolean outcome law does not supply common lineage or a shared occurrence token. The paper consistently states that limitation.

## 8. Operator-system theorem and branch memory

The span

\[
\mathcal S_W(y)
=
\operatorname{span}_{\mathbb C}
\{I,\Phi_a^*(P_r),\Phi_a^*(P_r)^*\}
\]

is exactly the least unital self-adjoint linear space containing the admitted transported record effects. Generator inclusion proves monotonicity; common boundary conjugation proves presentation covariance; labels and handles do not occur in the formula.

Under the exact spectator hypothesis,

\[
(\Phi_a^*\otimes\operatorname{id}_C)(P_r\otimes I_C)
=
\Phi_a^*(P_r)\otimes I_C,
\]

so

\[
\mathcal S_{W\otimes C}
=
\mathcal S_W\otimes\mathbb CI_C.
\]

No inaccessible spectator operator is imported.

For the branch-memory seed,

\[
N^*Z_mN=Z_m,\qquad
U^*Z_mU=X_bZ_m.
\]

The two nonidentity generators are linearly independent commuting involutions, hence

\[
\mathcal S_W(x_0)
=
\operatorname{span}\{I,Z_m,X_bZ_m\},
\qquad
\dim\mathcal S_W=3.
\]

Their product is

\[
Z_m(X_bZ_m)=X_b,
\]

so

\[
C^*(\mathcal S_W)
=
\operatorname{span}\{I,Z_m,X_bZ_m,X_b\},
\qquad
\dim C^*(\mathcal S_W)=4.
\]

The paper correctly labels \(X_b\) an algebraic product in the C*-closure, not an admitted joint experiment.

## 9. Karoubi completion and addressability

For \(f:(B,e)\to(C,d)\) with \(f=dfe\), one obtains \(fe=f=df\). If \(g:(C,d)\to(K,k)\), then

\[
gf=kgd\,dfe=k(gf)e.
\]

Thus the identity on \((B,e)\) is \(e\), and composition is correctly typed.

For a UCP idempotent \(e\),

\[
\operatorname{Fix}(e)=\operatorname{Ran}(e)
\]

is unital, linear and self-adjoint, hence an operator system. It need not be an ambient subalgebra. An exact finite example is:

\[
\rho(A)=A\oplus\tau_2(A):M_2\to M_3,
\qquad
\phi(X)=X_{\{1,2\}\times\{1,2\}}:M_3\to M_2,
\]

where \(\tau_2\) is normalized trace. Both maps are UCP and \(\phi\rho=\operatorname{id}\), so \(e=\rho\phi\) is UCP and idempotent. For \(P=\operatorname{diag}(1,0)\),

\[
\rho(P)=\operatorname{diag}(1,0,1/2),
\]

but

\[
\rho(P)^2=\operatorname{diag}(1,0,1/4)\notin\rho(M_2).
\]

Thus the range is not closed under ambient multiplication. Its Choi–Effros product satisfies

\[
\rho(A)\circ_e\rho(B)=e(\rho(A)\rho(B))=\rho(AB),
\]

and is a C*-algebra under that new product. By contrast, when the range is an ambient C*-subalgebra, Tomiyama’s theorem supplies the ordinary conditional-expectation bimodule law.

The order

\[
e\preceq f\iff ef=fe=e
\]

is reflexive, antisymmetric and transitive, and implies

\[
\operatorname{Fix}(e)\subseteq\operatorname{Fix}(f).
\]

Because every category admits \(\operatorname{id}_B\),

\[
\mathcal S\subseteq\operatorname{Fix}(\operatorname{id}_B)
\]

for every \(\mathcal S\). Therefore the pin’s literal no-containing case is impossible under its own definition. The paper’s identity-only/no-proper replacement is mandatory mathematical consistency.

### Addressability controls

| Control | Independent disposition |
|---|---|
| unique dephasing | Correct: the composition monoid generated by \(I,D_Z\) contains exactly those two idempotents, with \(D_Z\prec I\). |
| abstract but unadmitted expectation | Correct: a group of unitary automorphisms contains no nonidentity idempotent. Abstract \(D_Z\) supplies no physical certificate. |
| full/global system | Correct: if \(\mathcal S=B\subseteq\operatorname{Fix}(e)\), then \(e=\operatorname{id}\). |
| symmetry, \(c=1/2\) | Correct after the missing odd-\(\alpha\) normal-form calculation above. Only \(e_n,e_m\) are proper idempotents. |
| symmetry groupoid | Correct: the two minima are incomparable and exchanged by a typed Karoubi isomorphism. |
| inaccessible spectator | Correct at the exact product-transport premise; only \(\mathcal S\otimes I_C\) is generated. |
| literal no-containing branch | Correctly rejected as empty; identity-only is the exact negative. |
| branch-memory expectation | Correct: joint dephasing in \(X_b,Z_m\) fixes \(\operatorname{span}\{I,Z_m,X_bZ_m,X_b\}\) and contains the three-dimensional operator system. |

No unlisted finite word yields the full depolarizing expectation. Alternating products approach it only as an infinite limit; the declared category is generated by finite composition and has no such topological closure.

## 10. Mandatory-control register

All pin-mandated controls have a secure exact disposition.

| Required control | Result |
|---|---|
| unitary transport | sharp, full multiplicative domain, zero defect |
| deterministic bit flip | nontrivial Boolean atom exchange |
| dephasing | diagonal record algebra fixed and in MD |
| \(3/4\)–\(1/4\) random unitary | commuting unsharp POVM, defect \(3I/16\) |
| amplitude damping | \(P_1\mapsto P_1/2\), defect \(P_1/4\) |
| two noisy channels | composite defect \(15I/64=12I/64+3I/64\) |
| branch-memory W3 seed | inherited W3 seam secure; three-dimensional operator system and four-dimensional C*-closure |
| terminal RQ0-A | exact projector pullback only on its declared finite map scope |
| same POVM, different instruments | Lüders versus reprepare, effects equal and disturbance different |
| admitted versus abstract idempotent | only admitted map yields a Karoubi/addressability certificate |
| presentation gauge | defects, POVMs and operator systems conjugate correctly |
| handle renaming | pure reindexing, no operator change |
| sharp but not co-referential | explicitly separated |
| inaccessible spectator | no operator-system inflation |
| symmetry-related minima | both retained; no arbitrary selector |
| identity-only/global | both grammar-relative and genuinely full-system cases distinguished, subject to the terminology fix |
| no-containing | proved logically impossible under admitted identities |

## 11. Law-relative and no-smuggling audit

The paper remains law-relative in its mathematical claims:

- the W3 diagram, boundary, PVM and admitted transport family are declared inputs;
- \(\mathcal S_W\) changes when the admitted law changes;
- an abstract but unadmitted expectation never earns addressability;
- C*-products are not promoted to admitted experiments;
- Boolean sharpness is not promoted to W6 co-reference;
- identity-only addressability is not called intrinsic support;
- no Weld quantaloid, Isbell concept, overlap, stack, topology, influence, causal, geometric, field or gravity result is restored.

Terms such as “branch” and “memory” label the declared finite control and are expressly denied spatial meaning. The only wording risk is the temporal-direction and “global” terminology identified in F2; the formal statements themselves do not smuggle intrinsic localization.

## 12. Rung disposition

| Registered rung | Disposition | First exact obstruction |
|---|---|---|
| `RQ0-L0-W3-EFFECT-TRANSPORT` | **EARNED** | None. Total effect/POVM transport, supplied-instrument shadow and exact defects are secure. Universal instrument prose must retain its printed full-matrix or finite-predual scope. |
| `RQ0-L0-SHARP-FACT-TRANSPORT` | **EARNED** | None. The atom-sharpness/MD equivalence and typed partial Boolean functor are correct. No co-reference is inferred. |
| `RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM` | **EARNED** | None. Minimal operator systems, admitted Karoubi objects and the exact proper/ambiguous/identity-only controls are secure. The odd-\(\alpha\) proof needs explicit completion, but no counterexample exists. |

The highest surviving cumulative result is therefore:

\[
\boxed{\texttt{RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM}.}
\]

## 13. Surviving theorem register

The following survive without mathematical downgrade:

1. finite-dimensional UCP effect-module transport;
2. total fixed-outcome POVM functor and typed `Rec_eff`;
3. instrument precomposition and effect-shadow theorem at the displayed finite matrix/predual scope;
4. same-effects/different-disturbance construction;
5. Kadison–Schwarz positivity and exact projection criterion;
6. both defect chain laws and the nonfaithful-outer-channel qualification;
7. unitary covariance and exact separation from \(\Delta^B\);
8. the five-way finite-record multiplicative-domain equivalence;
9. categorical closure of `SharpRec_D` and exact `Rec_sharp`;
10. minimal law-relative operator-system observability and spectator law;
11. branch-memory transport and the three-versus-four dimensional separation;
12. admitted Karoubi completion and fixed-range operator-system theorem;
13. Choi–Effros versus ambient-product/conditional-expectation distinction;
14. partial order on admitted idempotents and fixed-range implication;
15. all proper, ambiguous, symmetry-orbit and identity-only addressability controls;
16. the inherited exact W3 seed at `RQ0-L0-REPRESENTABLE-W3-SKETCH`;
17. terminal RQ0-A projector descent at its separate declared finite scope.

No repair, implementation or later-physics work is included in this report.
