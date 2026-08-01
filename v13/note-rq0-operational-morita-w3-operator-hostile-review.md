# External hostile review — Operational Morita Geometry of W3 Records

## Operator algebra and Morita theory

**Reviewed pin:** `35a4878`  
**Reviewed paper:** `a1fa2c9`  
**Verified paper SHA-256:** `cb36418645f845fc35b9e1c77e71a37f1c5a9d6779cae8526a2dfba2ff138537`

## Overall verdict

\[
\boxed{\texttt{HEADLINE-DOWNGRADE}}
\]

The paper successfully repairs the complete-instrument W3 layer. Its universal block condition, sharp-readout distinction, hostile singleton-probe rejection, fixed branch-memory classification, and basic imprimitivity-module transport are sound.

The full headline is not earned. The marked operational localization is not constructed with sufficient categorical typing to support the claimed Grothendieck category; the ineffective-isotropy quotient conflates strict identity with natural equivalence and does not actually construct the claimed matrix-spectator kernel; the full addressability category leaves its record-interface morphism condition undefined; and the displayed proof of the \(U(1)\times S_4\) benchmark symmetry is false for sixteen of the twenty-four pure permutation lifts.

The highest registered rung that survives is:

\[
\boxed{\texttt{RQ0-L0-COMPLETE-INSTRUMENT-W3}}
\]

The strongest additional unregistered result is a pairwise transport theorem:

> A complete-instrument W3 object is carried bijectively through an explicitly supplied family of boundary endomorphism *-isomorphisms induced by imprimitivity modules, provided every state, effect, channel, instrument, comparison, and scalar context is transported exactly through those isomorphisms.

That theorem is correct but narrower than the paper’s marked-Morita localization, effective-stack, and full-fibration claims.

The first registered obstruction is:

\[
\boxed{\texttt{RQ0-L0-BLOCKED-AT-MARKED-MORITA-TRANSPORT}}
\]

at the categorical-localization level, while the concrete pairwise transport calculation itself survives.

---

# Registered rung dispositions

| Registered rung | Disposition |
|---|---|
| `RQ0-L0-COMPLETE-INSTRUMENT-W3` | **EARNED**, with two local wording/type fixes noted below |
| `RQ0-L0-MORITA-INVARIANT-W3-SEAMS` | **NOT EARNED AS REGISTERED**; exact pairwise transport survives, but the marked operational bicategory/localization and its W3 pseudofunctor are not constructed |
| `RQ0-L0-EFFECTIVE-W3-SEAM-STACK` | **NOT EARNED**; cumulative failure plus an unresolved strict-versus-natural isotropy problem and a false benchmark symmetry proof |
| `RQ0-L0-FULL-ADDRESSABILITY-FIBRATION` | **NOT EARNED**; cumulative failure plus an undefined record-interface compatibility condition |

---

# Ranked findings

## 1. The marked operational localization is not a defined bicategory, and the claimed W3 pseudofunctor exists only on equivalences

**Severity:** Critical  
**Classification:** Missing construction / categorical typing failure  
**Affected lines:** 232–255, 335–380, 391–408, 757–807, 829–843

The paper has three different kinds of morphism:

1. Hilbert-module correspondences and adjointable bimodule intertwiners;
2. CP maps and UCP Heisenberg channels between endomorphism algebras; and
3. states, effects, instrument branches, outcome maps, and scalar experiment contexts.

Definition 2.4 calls the represented image of all these objects an “image category” (lines 232–238), but no common multi-sorted category, double category, equipment, PROP, or pseudofunctor is defined in which they have uniform source and target types and in which all listed constructors compose.

Proposition 2.5 is correct conditionally:

> If there is a typed representation functor into a category of represented operational transformations, equality in its image is a congruence.

It does not construct that representation functor or its heterogeneous codomain.

The problem returns in Definition 3.6. Lines 393–401 introduce

\[
\mathbf{Pres}_D[\mathcal W_{\mathrm{Mor}}^{-1}]
\]

but “marked correspondences and coherent 2-cells” are not defined. In particular, the paper does not specify:

- how a CP process branch is attached to a correspondence;
- how such marked correspondences compose;
- how outcome instruments compose horizontally;
- how scalar contexts transform as 2-cells;
- how parallel composition interacts with interior tensor product; or
- what equality of marked 1- and 2-cells means.

Theorem 7.1 proves transport only along the explicitly marked imprimitivity **equivalences**. It does not define transport along every 1-morphism of \(\mathbf{OpMor}(D)\).

Nevertheless, Definition 7.4 asserts a pseudofunctor on the entire localized bicategory and forms its Grothendieck category (lines 829–843). A pseudofunctor requires action on every base 1-cell and coherence on every composable pair. Those data have not been supplied.

Restricting the base to the core groupoid of complete presentations and marked imprimitivity equivalences would repair the immediate problem. The immutable paper does not make that restriction.

Consequently, the pairwise theorem

\[
D\simeq_{\mathrm{marked}}D'
\Longrightarrow
\mathsf{W3}_{\mathrm{ci}}(D)\simeq
\mathsf{W3}_{\mathrm{ci}}(D')
\]

survives, but the claimed W3 category constructed **on the operational Morita localization** does not.

This withholds `RQ0-L0-MORITA-INVARIANT-W3-SEAMS` at its registered scope.

---

## 2. The ineffective-isotropy definition uses strict identity, while the spectator conclusion uses natural equivalence

**Severity:** Critical  
**Classification:** False inference / unresolved 2-categorical typing  
**Affected lines:** 919–1005, especially 927–939 and 1001–1005

Definition 9.2 puts an automorphism \(g\) in \(K_s\) only when its induced action **is identity** on every marked datum and every addressability object and morphism.

Corollary 9.6 then says that inner spectator transformations “naturally isomorphic to identity” lie in \(K_s\).

These are different conditions:

\[
F_g=\operatorname{id}
\qquad\text{versus}\qquad
F_g\cong\operatorname{id}.
\]

A nontrivial inner automorphism of a coefficient algebra is often implemented by a module isomorphism and hence is 2-isomorphic to the identity Morita presentation. It need not be literally the identity 1-arrow or act strictly as the identity functor on every marked object.

The paper never chooses one of the following:

- a strictification in which the relevant spectator actions become literal identities;
- a 2-kernel defined by specified natural transformations;
- a 1-truncation that identifies 2-isomorphic presentation arrows; or
- a rigidification of a bicategory rather than a groupoid.

Nor does it explicitly construct the claimed raw \(U(n)\) spectator isotropy as automorphisms of \(\mathfrak S(D)\). For the standard row imprimitivity module \(X=\mathbb C^{1\times n}\), ordinary right-\(M_n\)-linear unitary endomorphisms of \(X\) are only scalar. General \(U(n)\) coordinate changes act through coefficient-algebra automorphisms and associated correspondence isomorphisms; their placement in the paper’s 1-groupoid requires precisely the missing 2-categorical construction.

Lemma 9.3 and Theorem 9.5 are correct for an already defined groupoid action with a strict kernel. They do not prove that matrix-spectator presentation transformations form that kernel.

Thus the abstract normal-subgroup quotient survives, while its load-bearing spectator application does not.

This independently blocks `RQ0-L0-EFFECTIVE-W3-SEAM-STACK`.

---

## 3. The full addressability category has no exact record-interface morphism equation

**Severity:** Major  
**Classification:** Incomplete definition  
**Affected lines:** 1027–1072

Definition 10.2 correctly states the Karoubi corner equation

\[
h=fhe.
\]

It then adds that \(h\) must carry “the typed seam observability maps at \(y\) to those at \(z\)” (line 1055), but supplies no equation.

Several inequivalent meanings are possible:

- pointwise preservation:
  \[
  h(\Phi_y^*(p_r))=\Phi_z^*(p_r);
  \]
- preservation after a declared map of record outcomes;
- inclusion of one observability operator system into another;
- intertwining of the complete classical action;
- preservation only modulo the Choi–Effros range products; or
- preservation of the span without preservation of distinguished effects.

Until one is selected, it is impossible to determine the morphism set of \(\mathsf{Addr}(s)\).

Proposition 10.3 says “record-interface compatibility composes,” but this is assumed rather than proved. Theorem 10.4 cannot verify preservation of an unspecified condition.

The two-dephasing arrow

\[
h=e_me_n
\]

does satisfy the corner equation and fixes the displayed operator system pointwise, so Proposition 11.1 survives under the natural pointwise interpretation. That one control does not define the general category.

Therefore the paper has constructed the underlying CP Karoubi category, but not the registered seam-compatible full addressability category.

This blocks `RQ0-L0-FULL-ADDRESSABILITY-FIBRATION` independently of its cumulative dependence on the earlier rungs.

---

## 4. The displayed \(S_4\) symmetry lift is false

**Severity:** Major  
**Classification:** False proof; theorem statement salvageable  
**Affected lines:** 1495–1545

Lines 1513–1535 claim that for every output permutation matrix \(P\), the choice

\[
T_2=P,\qquad
T_1=V^*PV,\qquad
T_0=U^*T_1U
\]

satisfies all four intertwining equations.

It does not.

Use the paper’s basis order

\[
(|00\rangle,|10\rangle,|01\rangle,|11\rangle)
\]

and let \(P\) swap only the last two output basis vectors. Then

\[
P=\operatorname{diag}(I_2,X)
\]

and, since \(V=\operatorname{diag}(H,H)\),

\[
T_1=V^*PV
=
\operatorname{diag}(1,1,1,-1).
\]

Write \(C=\operatorname{CNOT}_{b\to m}\). Since

\[
U=CV,\qquad N=V,\qquad E=VC,
\]

the first equation fixes \(T_0=U^*T_1U\). The second equation is then equivalent to

\[
T_1=CT_1C.
\]

But \(C\) swaps the second and fourth basis coordinates, so

\[
CT_1C
=
\operatorname{diag}(1,-1,1,1)
\ne
T_1.
\]

The fourth intertwining equation fails for the same reason.

Thus the paper’s asserted pure-permutation lift fails for this permutation and, by direct exact enumeration, for sixteen of the twenty-four permutations.

The group statement can be repaired. For every underlying permutation there is a unique signed monomial lift up to common phase. In the example above one may replace \(P\) by

\[
P\,\operatorname{diag}(-1,-1,1,1).
\]

Solving the three adjacent-transposition relations gives signed lifts satisfying the Coxeter presentation of \(S_4\). Hence the corrected raw extension splits as

\[
U(1)\times S_4,
\]

and the effective permutation group is indeed \(S_4\).

So Lemma 13.5’s conclusion is plausible and independently recoverable, but the proof committed in the paper is false. The effective branch classification is therefore not proved by the immutable artifact.

---

## 5. The physical-spectator proposition has an impossible hypothesis in the induced module

**Severity:** Major  
**Classification:** Vacuous proposition / wrong discriminator  
**Affected lines:** 896–906; compare 296–316

Lemma 3.2 says

\[
\Theta_X^M:
\mathcal L_A(M)
\overset{\cong}{\longrightarrow}
\mathcal L_B(M\otimes_A X)
\]

is a surjective *-isomorphism.

Proposition 8.2 then assumes that the amplified presentation contains an effect whose represented operator is not in the image of \(\Theta_X\).

For the same induced boundary module \(M\otimes_A X\), this cannot happen: every represented operator lies in the image of the surjective \(\Theta_X\).

The correct discriminator is not

\[
e'\notin\operatorname{im}\Theta_X
\]

as an operator. It is

\[
e'\notin\Theta_X(\mathcal E_D^{\mathrm{admitted}})
\]

as a member of the transported **marked effect family**.

An algebraic preimage may exist while its preimage is not physically admitted.

Control 12.3 uses a different and valid construction: it replaces the induced right-\(M_n\) module by the ordinary Hilbert space \(H\otimes\mathbb C^n\) over \(\mathbb C\), whose observable algebra is the larger

\[
B(H)\otimes M_n.
\]

That genuinely adds physical spectator observables. It does not prove Proposition 8.2 as written.

The inaccessible-spectator theorem itself survives; the general physical-spectator proposition needs this correction.

---

## 6. Proposition 6.3 states a false logical relation

**Severity:** Moderate  
**Classification:** False wording; intended theorem survives  
**Affected lines:** 716–727

The proposition says:

> Universal block preservation neither implies nor is implied by the existence of a supplied single favorable scalar effect.

But \(\mathcal E\) is unital. The identity effect is always block diagonal:

\[
\mathcal D_R(I)=I.
\]

Thus universal block preservation certainly implies that at least one favorable effect exists.

The proof actually establishes two different correct statements:

1. universal block preservation does not imply **sharp readable availability**; and
2. one favorable effect does not imply universal block preservation.

Those are the distinctions required by the pin and used later. The proposition’s first sentence should state them directly.

This does not defeat `RQ0-L0-COMPLETE-INSTRUMENT-W3`, because Definitions 5.4 and 5.5 and the two explicit counterexamples establish the intended separation.

---

## 7. The Frobenius-object language is not typed in the paper’s correspondence/CP architecture

**Severity:** Moderate  
**Classification:** Terminology and type inflation  
**Affected lines:** 414–450, 502–526

The PVM theorem is correct:

\[
\operatorname{Hom}_{*}(\mathbb C^\Omega,\mathcal L_A(M))
\cong
\{\text{finite PVMs in }\mathcal L_A(M)\}.
\]

The transport theorem

\[
\lambda^X=\Theta_X^M\lambda
\]

is also correct.

What is not constructed is a commutative special symmetric dagger-Frobenius object **inside the declared marked correspondence/process structure**.

Lines 422–432 display copying and deletion maps on \(\mathbb C^\Omega\), but do not specify:

- the ambient dagger monoidal category in which these maps live;
- their multiplication and unit daggers;
- the normalization used for specialness;
- a Frobenius-module action map;
- or its compatibility with the CP operational layer.

The cited CP*/CPM literature establishes appropriate classical structures in specified dagger compact categories. It does not automatically type the paper’s mixture of:

- correspondence 1-morphisms;
- CP maps between endomorphism algebras; and
- *-representations \(\lambda:C_\Omega\to\mathcal L_A(M)\).

The paper has securely constructed a finite classical C*-algebra and its sharp module representation. That is sufficient for its concrete W3 equations. Calling the same datum a Frobenius classical object in the combined Morita process theory requires an additional categorical definition.

This is a scope correction, not a failure of the PVM/action mathematics.

---

## 8. Marked operational Morita equivalence is an exact operational isomorphism, not a general physical Morita theorem

**Severity:** Moderate  
**Classification:** Scope engraving / limited discriminator  
**Affected lines:** 335–389

Definition 3.4 requires all represented observable algebras to be related by the induced *-isomorphisms \(\Theta_X\), and then requires a bijection of every admitted state, effect, CP map, instrument, comparison, and scalar context under those isomorphisms.

Consequently, Theorem 7.1 is essentially invariance under exact isomorphism of the complete represented operational law, with the coefficient algebra and module presentation allowed to change Morita-wise.

This is noncircular—the definition does not mention W3 seams—and it is useful for the matrix-spectator presentation. But it is narrower than established notions of Morita equivalence for CP maps or operational categories. It does not show that empirically equivalent but nonisomorphic complete markings yield the same W3 theory.

The paper mostly engraves this restriction correctly at lines 139–151. The result should consistently be described as:

> invariance under exact transported markings induced by imprimitivity modules,

not a general theorem that physical quantum theories invariantly descend under all relevant Morita equivalences.

---

## 9. “Finite rigidification” is not finite at the stated general scope

**Severity:** Minor  
**Classification:** Scope error  
**Affected lines:** 955–999

The normal-kernel quotient construction works for any small groupoid. Nothing in Definitions 9.1–9.4 proves that:

- the object set is finite;
- the hom-sets are finite; or
- the automorphism groups are finite.

Indeed, the branch example itself has raw \(U(1)\) isotropy before quotienting.

After correctly removing the branch \(U(1)\), its effective action groupoid is finite. The general theorem should be called an explicit groupoid rigidification, with finiteness asserted only for controls where it is proved.

---

# Independent theorem audits

## A. Boundary-module transport theorem

Lemma 3.2 is correct with the stated imprimitivity hypothesis.

For an \(A\)-\(B\) imprimitivity bimodule \(X\), the conjugate module \(\overline X\) supplies

\[
X\otimes_B\overline X\cong A,
\qquad
\overline X\otimes_A X\cong B.
\]

Therefore

\[
M\mapsto M\otimes_A X
\]

is an equivalence of Hilbert-module C*-categories and

\[
T\mapsto T\otimes I_X
\]

is a bijection on adjointable maps.

### Nonfree/direct-sum test

Take

\[
A=\mathbb C\oplus\mathbb C,
\qquad
B=M_2\oplus M_3,
\]

and

\[
X=\mathbb C^{1\times2}\oplus\mathbb C^{1\times3}.
\]

This is an \(A\)-\(B\) imprimitivity bimodule.

For a full module

\[
M=\mathbb C^r\oplus\mathbb C^s,
\]

one obtains

\[
\mathcal L_A(M)=M_r\oplus M_s
\]

and the same endomorphism algebra after transport to \(B\).

Even for the nonfull test module

\[
M=\mathbb C^r\oplus0,
\]

the transported module is supported on the \(M_2\) summand and

\[
\mathcal L_A(M)\cong M_r
\cong
\mathcal L_B(M\otimes_A X).
\]

Thus the Hom-isomorphism itself does not require \(M\) to be full.

### Nonfull correspondence negative

Let \(A=\mathbb C\oplus\mathbb C\), \(B=\mathbb C\), and let \(X=\mathbb C\) carry only the first \(A\)-summand. Tensoring annihilates modules supported on the second summand. It is not an equivalence and the endomorphism map is not generally faithful.

This does not refute the paper because such \(X\) is not an imprimitivity bimodule. It confirms that fullness/invertibility is load-bearing.

### Center-changing negative

A full imprimitivity bimodule cannot strongly Morita-equate finite-dimensional C*-algebras with different centers. For example,

\[
\mathbb C^2
\not\sim_{\mathrm{Morita}}
\mathbb C^3.
\]

This supports the paper’s block-type distinction in Theorem 13.6.

The cited Morita literature supports equivalence by tensoring with an imprimitivity bimodule; see [Blecher’s primary paper](https://arxiv.org/abs/math/9906082). The programme-specific operational marking is not supplied by that source and must stand on the paper’s own definitions.

---

## B. Classical-action theorem

Propositions 4.3 and 4.5 are correct.

A useful mandatory negative is:

\[
A=\mathbb C,
\qquad
B=M_3,
\qquad
M=\mathbb C^2.
\]

A diagonal action

\[
\lambda:\mathbb C^2\to B(\mathbb C^2)
\]

transports to an action on the right-\(M_3\) module

\[
\mathbb C^2\otimes\mathbb C^{1\times3}.
\]

It remains an action in

\[
\mathcal L_{M_3}(M\otimes X)\cong M_2.
\]

It does not canonically become a selected commutative subalgebra of the coefficient algebra \(M_3\).

The paper explicitly respects this distinction at lines 521–526.

The CP* source establishes a category containing finite-dimensional C*-algebras and CP maps, while the Gogioso result classifies special symmetric dagger-Frobenius algebras in CPM(fHilb); see [Coecke–Heunen–Kissinger](https://arxiv.org/abs/1305.3821) and [Gogioso](https://arxiv.org/abs/2110.07074). Neither source by itself supplies the paper’s mixed correspondence/marking category.

---

## C. Universal block theorem

Theorem 6.1 is correct.

For a finite PVM \((p_r)\),

\[
\mathcal D_R(a)=\sum_rp_rap_r
\]

has fixed space equal to the block diagonal algebra:

\[
\operatorname{Fix}(\mathcal D_R)
=
C_R'.
\]

Expanding with \(I=\sum p_r\) proves all four equivalences.

The full-matrix negative is also correct. If \(T\) is a *-isomorphism onto \(B(H)\), then a nontrivial PVM cannot commute with every output operator.

Although Proposition 6.4 uses the nonselfadjoint rank-one operator \(|u\rangle\langle v|\), this is legitimate because the operator system is the complex span \(B(H)\). An equivalent positive-effect witness is the rank-one projector onto \(u+v\).

---

## D. Complete-instrument W3 equations

The equations are correctly typed in the represented observable algebras.

- Write correlation uses every outcome of the selected complete preparation instrument.
- Universal preservation uses the whole admitted output effect operator system.
- Sharp availability uses all outcomes of a complete readout instrument and a declared coarse-graining.
- The eraser uses an admitted output effect and a nonzero operational state evaluation.

The exact singleton-probe counterexample is correctly rejected at lines 1188–1267.

The eraser scalar

\[
\rho_\alpha\!\left(
U^*(q_kE^*(a)q_\ell)
\right)
\]

is invariant under the paper’s exact *-isomorphism transport, since multiplication, CP maps, states, and the classical projectors are all conjugated coherently.

Thus the complete-instrument rung is sound.

---

## E. Bare Morita equivalence and inequivalent markings

The required negative controls behave correctly.

- \(\mathbb C\) and \(M_n\) are strongly Morita equivalent as coefficient algebras.
- A fully accessible \(n\)-level control/effect family need not correspond to a scalar marking.
- The \(M_2\) law with only a \(Z\)-readout and the \(M_2\) law with both \(Z\)- and \(X\)-readouts have inequivalent complete markings.

Likewise, an identity channel cannot be transported into a genuinely depolarizing channel merely by conjugating through endomorphism *-isomorphisms: conjugation preserves multiplicativity and invertibility. The paper correctly excludes CP data that do not match its exact transported marking.

Kodaka studies a broader notion of strong Morita equivalence for CP maps; the paper’s construction is instead exact conjugation of endomorphism-algebra maps. The distinction is visible by comparing the paper with [Kodaka’s primary source](https://arxiv.org/abs/2102.13317).

---

## F. Matrix-spectator theorem

The standard module calculation is correct.

For

\[
X=\mathbb C^{1\times n}
\]

as a \(\mathbb C\)-\(M_n\) imprimitivity bimodule,

\[
H^X=H\otimes X
\]

is a right \(M_n\)-module and

\[
\mathcal L_{M_n}(H^X)\cong B(H).
\]

The concrete vector-space dimension grows, but the adjointable right-module observable algebra does not become \(B(H\otimes\mathbb C^n)\).

Transporting the complete marking through this isomorphism preserves the W3 equations. Theorem 8.1 is valid and avoids the old ill-typed preparation rule.

Adding one genuinely accessible spectator effect requires either:

- adding an effect not belonging to the transported marked effect family, or
- changing to a larger physical boundary module, as in Control 12.3.

The conceptual inaccessible/physical distinction is correct despite Proposition 8.2’s surjectivity error.

---

## G. Full CP Karoubi category

Ignoring the unspecified record-interface condition, the underlying category is correct.

Objects are UCP idempotents \(e\). A CP map \(h\) is a corner arrow when

\[
h=fhe.
\]

The Karoubi identity on \((y,e)\) is \(e\), and composition closes.

For the dephasing control,

\[
h=e_me_n
\]

obeys

\[
e_mhe_n=h.
\]

On the auxiliary Bloch space it is the product of two distinct nonorthogonal rank-one projections, hence noninvertible. The paper correctly restores the arrow deleted by the preceding cycle.

No Choi–Effros product is needed merely to form this CP corner category. It would become necessary if the ranges were promoted to ordinary C*-subalgebras.

---

# Independent branch-memory audit

## Nine complete-instrument W3 objects

The Hadamard calculation reproduces exactly.

The complete output effect system is the diagonal algebra \(\mathcal D_4\). Under \(V\),

\[
V^*(\mathcal D_4)
=
\operatorname{span}
\{|v_i\rangle\langle v_i|\}.
\]

Universal block preservation therefore forces coarse sectors to be spans of blocks of a partition of the four availability vectors.

The restricted write columns give:

- one fine ray for singleton blocks;
- exactly two orthogonal rays for two-element blocks; and
- four distinct nonorthogonal rays for three-element blocks.

The complete no-write and eraser tests then retain exactly:

\[
6\text{ partitions of type }2+1+1
\quad\sqcup\quad
3\text{ partitions of type }2+2.
\]

The familiar memory partition remains one of the three \(2+2\) objects.

The result remains conditional on the benchmark’s explicit admission of every atomic fine classical action and its restricted terminal diagonal readout law.

## Symmetry

The pure-permutation construction in Lemma 13.5 is false, as shown above.

A corrected signed-monomial reconstruction yields one lift per permutation up to common phase. The central \(U(1)\) acts trivially by conjugation, and the effective permutation quotient is \(S_4\).

Therefore the two orbit types remain:

- six \(2+1+1\) objects;
- three \(2+2\) objects.

Since their coarse classical algebras are \(\mathbb C^3\) and \(\mathbb C^2\), no marked Morita equivalence can connect the two types.

The two-component conclusion is mathematically recoverable, but the paper’s proof must not be accepted as written.

## Addressability benchmark

Freezing the admitted idempotent objects to identity avoids planting a preferred pinching. It establishes that no proper idempotent object occurs.

It does not classify every morphism in the full identity-object fibers: admitted process CP maps can still be nontrivial morphisms between identity Karoubi objects when they satisfy the record-interface condition. Because that condition is undefined, the claimed full benchmark addressability classification at lines 1574–1585 is incomplete.

---

# Source audit

The primary sources support only the standard external layers:

- [Blecher](https://arxiv.org/abs/math/9906082) supports Morita equivalence through tensoring module categories with an equivalence bimodule.
- [Coecke, Heunen, and Kissinger](https://arxiv.org/abs/1305.3821) support a CP* setting containing finite-dimensional C*-algebras and CP maps.
- [Gogioso](https://arxiv.org/abs/2110.07074) treats special symmetric dagger-Frobenius algebras in CPM(fHilb).
- [Kodaka](https://arxiv.org/abs/2102.13317) treats strong Morita equivalence for CP maps in a broader operator-algebraic sense.

None of those sources constructs the paper’s marked operational bicategory, its heterogeneous represented image, its W3 pseudofunctor, or its strict ineffective-isotropy kernel. Those are programme-specific obligations and cannot be imported from the citations.

The rigidification references are appropriately described as analogies, not as proofs of Theorem 9.5. The elementary quotient-groupoid theorem itself is sound once a strict normal kernel is supplied.

No bibliographic error changes the verdict.

---

# Final surviving package

The paper genuinely establishes:

1. complete candidate-independent state/effect/instrument scopes for W3;
2. rejection of the singleton-probe false seam;
3. the universal block theorem
   \[
   \operatorname{Fix}(\mathcal D_R)=C_R';
   \]
4. the distinction between universal block preservation and sharp readable availability;
5. the full-matrix unitary negative;
6. exact complete-instrument write, no-write, preserve, readout, and eraser equations;
7. PVM/classical-action equivalence;
8. transport of module actions and every W3 scalar through explicitly supplied endomorphism *-isomorphisms;
9. standard inaccessible matrix-amplification stability for the induced complete marking;
10. the underlying full CP Karoubi category and the noninvertible \(e_me_n\) arrow;
11. the exact nine-object complete branch-memory theorem; and
12. a recoverable signed-monomial \(S_4\) action with two partition-type orbits.

It does not yet establish:

1. a fully typed marked operational Morita bicategory/localization;
2. a W3 pseudofunctor on that localization;
3. a strict or bicategorical ineffective-spectator kernel;
4. the advertised effective rigidified seam stack;
5. an exactly defined record-compatible full addressability category; or
6. the cumulative full addressability fibration.

No topology, influence, causality, field, or gravity objection enters this verdict.
