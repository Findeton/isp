# External hostile review — W3 seam stack

## Moduli and higher geometry

**Reviewed pin:** `21d28d1c80a3a9518887c9b257475694fc5843e8`  
**Reviewed paper:** `dc0a662099361355f0219602bdcab9520f4c25ff`

## Overall verdict

\[
\boxed{\texttt{HEADLINE-DOWNGRADE}}
\]

The paper contains several correct and useful results:

- the fixed-type classification of nested commutative algebras;
- the conditional semialgebraic description of finite W3 loci;
- the passive/active symmetry distinction;
- the automorphism no-selection theorem;
- the complete nine-seam branch-memory calculation;
- existence of minimal containing UCP idempotents; and
- a valid Grothendieck fibration after restricting each addressability fiber to its invertible core.

However, none of the three newly registered cumulative rungs is earned under the strict pin. The operational reduction is declared but not incorporated into the seam groupoid, the mandatory inaccessible-spectator theorem is ill-typed for preparations and probes, and the addressability construction discards admitted noninvertible Karoubi morphisms despite the pin requiring the complete admitted category.

The previous terminal result

\[
\boxed{\texttt{RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM}}
\]

therefore remains the highest registered repository result. The strongest new surviving theorem is a fixed-law, fixed-packet W3 seam-locus construction together with the exact nine-seam branch-memory classification.

---

# Independent rebuild

## 1. Candidate parameter spaces

For a fixed nested-algebra type

\[
\tau=(q_1,\ldots,q_n;\pi),
\qquad
\sum_k q_k=d,
\]

the correct stabilizer is

\[
N_\tau
=
\left(\prod_{k=1}^n U(q_k)\right)
\rtimes
\operatorname{Aut}(\tau),
\]

where

\[
\operatorname{Aut}(\tau)
=
\left\{
\sigma\in S_n:
q_{\sigma(k)}=q_k,\ 
\sigma\text{ sends blocks of }\pi\text{ to blocks of }\pi
\right\}.
\]

Thus

\[
U(d)/N_\tau
\]

correctly parameterizes unlabelled embedded pairs \(R\subseteq F\) of the fixed decorated type. Internal block bases and permitted outcome permutations have been removed, while the embedded algebra pair remains.

For a finite packet and a semialgebraic admitted-projector family, the W3 equations are semialgebraic:

- projector, rank, orthogonality and resolution conditions are polynomial;
- write correlation and availability are finite Boolean combinations of polynomial zero conditions;
- no-write failure, erasure and operational use are finite nonvanishing conditions.

The paper also correctly avoids calling the global union a smooth manifold. An infinite packet family can produce an infinite union, and stabilizer type and local dimension can jump.

This rebuild supports Proposition 3.2 and the conditional content of Theorem 5.1.

## 2. Exact branch-memory calculation

The branch-memory classification independently checks out.

Availability forces every coarse projector to be diagonal in the basis

\[
v_0=|+,0\rangle,\quad
v_1=|-,0\rangle,\quad
v_2=|+,1\rangle,\quad
v_3=|-,1\rangle.
\]

In that basis the four write states are the normalized columns of

\[
A=
\begin{pmatrix}
1&1&1&-1\\
1&1&-1&1\\
1&-1&1&1\\
-1&1&1&1
\end{pmatrix}.
\]

For a coarse block \(B\):

- a singleton produces one fine ray;
- a two-element block produces exactly two orthogonal restricted rays;
- a three-element block produces four distinct restricted rays with pairwise inner products \(\pm1\), so no atomic orthogonal refinement can satisfy write correlation.

The all-singleton partition fails the matched no-write discriminator. Every partition made from blocks of size at most two and containing a size-two block passes no-write and erasure. The surviving partitions are therefore exactly

\[
3\text{ of type }2+2
\quad+\quad
6\text{ of type }2+1+1.
\]

Hence the paper’s nine-object atomic result is correct at its stated packet and rank scope. The familiar memory partition is not unique.

## 3. Symmetry and no selection

The passive/active distinction is conceptually correct.

A passive unitary changes the presentation of the whole represented law and candidate together. An active physical automorphism acts inside one fixed represented law and may permute physically distinct seam candidates. The elementary no-selection theorem is valid: a transitive action on at least two candidates has no invariant point, so no law-only equivariant rule can select one.

The paper also respects its claim boundary. It does not quietly restore physical overlaps, a spatial atlas, the rejected Weld stack, topology, or causality.

## 4. Minimal idempotents and the categorical core

The order

\[
e\preceq f
\iff
ef=fe=e
\]

is a partial order on admitted idempotents. If \(e\prec f\), then

\[
\operatorname{Ran}(e)\subsetneq\operatorname{Ran}(f),
\]

so strict descent lowers finite vector-space dimension. Starting from the identity therefore reaches a minimal element in finitely many steps.

Passive conjugation carries minimal containing idempotents to minimal containing idempotents. If one retains only invertible intertwiners, this gives a groupoid-valued functor, and its Grothendieck construction is both a fibration and an opfibration because all base arrows are invertible.

That smaller core theorem is valid. It is not the complete fiber required by the pin.

---

# Ranked findings

## Finding 1 — Major: the contextual operational quotient is not incorporated into the moduli groupoid

**Type:** missing construction and typing gap  
**Affects:** first and second registered rungs

Definition 3.5 says that seams are counted only up to equivalence in the contextual quotient \(\overline D\). But Definition 5.3 constructs the object space from

\[
s\in\operatorname{Seam}^{\mathrm{raw}}_{W3}(D')
\]

and gives it only passive unitary presentation arrows.

No arrows, localization, coequalizer, or second quotient implements the contextual equivalence between projector algebras or packets. Consequently, two candidates that are contextually indistinguishable but are not related by a passive unitary stabilizing the represented law remain separate objects in the displayed action groupoid.

There is also a type mismatch. The quotient \(\overline D\) is proved to exist as a dagger-compatible categorical quotient, but it is not proved to remain faithfully represented on finite Hilbert spaces with well-defined ranks, positivity, and embedded subalgebras of \(B(H)\). The homogeneous-space and semialgebraic arguments are performed before this quotient. They cannot automatically be transferred to equivalence classes in \(\overline D\).

Definition 3.4 only excludes wholly unused atoms. It does not identify candidates whose distinctions lie on operationally invisible structure while every atom retains some visible component.

Therefore the statement that contextual reduction is “the exact finite-scope answer to dormant presentation structure” is not established, and the displayed seam stack is not yet the operationally reduced stack required by W6 and the pin.

## Finding 2 — Major: the inaccessible-spectator theorem is ill-typed

**Type:** false theorem at the declared types  
**Affects:** mandatory control C3 and the first two registered rungs

Proposition 7.6 maps every arrow by

\[
a\longmapsto a\otimes I_K.
\]

That is well typed for an ordinary process arrow

\[
a:H_x\to H_y,
\]

because it gives

\[
a\otimes I_K:H_x\otimes K\to H_y\otimes K.
\]

It is not well typed for the preparations and probes required by Definition 2.1.

A preparation

\[
\eta:\mathbb C\to H_x
\]

is sent to

\[
\eta\otimes I_K:K\to H_x\otimes K,
\]

not to a preparation \(\mathbb C\to H_x\otimes K\). Similarly, a probe

\[
f:H_x\to\mathbb C
\]

is sent to a map

\[
f\otimes I_K:H_x\otimes K\to K,
\]

not a scalar probe. Scalar W3 contexts are therefore not preserved.

Amplifying the tensor unit to \(K\) does not fix the problem: scalar contexts then become \(K\)-endomorphisms rather than complex amplitudes. A fixed spectator state and effect could define a different typed construction, but that construction and its full/essential-surjectivity proof are absent.

Thus the claimed tensor functor, its “evident inverse,” and the mandatory spectator control do not exist as stated for nontrivial \(K\).

Because the pin makes inaccessible-spectator control mandatory even for `RQ0-L0-W3-SEAM-MODULI`, this defect prevents the first registered rung from being earned under the preregistered rules. It independently defeats the presentation-invariance rung.

## Finding 3 — Major: the addressability fiber omits required Karoubi morphisms

**Type:** pin violation and incomplete categorical object  
**Affects:** third registered rung

The pin requires the complete admitted candidate category and says:

> Retain all morphisms induced by admitted Karoubi maps and physical automorphisms.

Definition 12.3 instead retains only

> invertible admitted Karoubi intertwiners.

Minimality of the idempotent object does not make every Karoubi morphism invertible. If \(e\) is minimal, an admitted map

\[
h=ehe
\]

can still be a noninvertible endomorphism of its fixed operator system. Likewise, noninvertible admitted maps may exist between two minimal objects.

Those maps have been deleted solely to force the codomain to be a groupoid. The resulting construction is the invertible core of the requested category, not the complete addressability fiber.

In addition, “preserve the seam-relative operator system” is not supplied with a precise equation for a general arrow between different boundaries, so identity and composition closure of the claimed full physical arrow class are not proved.

A discrete or invertible-core fiber does yield the stated Grothendieck fibration. It does not earn `RQ0-L0-ADDRESSABILITY-FIBRATION` as preregistered.

## Finding 4 — Major: Theorem 7.1 invokes equivariance data not present in Definition 2.4

**Type:** missing hypothesis and proof gap  
**Affects:** second registered rung

Definition 2.4 requires an equivalence of passive presentation groupoids, but it does not require that equivalence to be compatible with their actions on represented packets and seam candidates.

Theorem 7.1 then invokes:

> Naturality with passive presentation arrows

to obtain a functor between the quotient action groupoids.

That naturality is additional data. An equivalence of the underlying passive groupoids by itself does not supply an equivariant map of the action objects \(\mathcal O_D\) and \(\mathcal O_{D'}\). The theorem becomes correct if strong represented equivalence is strengthened to include an equivariant functor and the relevant coherence isomorphisms. As written, full faithfulness on the action groupoids does not follow from the stated definition alone.

The objectwise unitary-conjugation result survives. The quotient-groupoid equivalence needs the missing action compatibility.

## Finding 5 — Moderate: the semialgebraic result is prequotient and conditional

**Type:** scope overstatement

Theorem 5.1 correctly assumes:

- a finite packet;
- a fixed rank/partition type; and
- a semialgebraic admitted-projector family.

The abstract states the semialgebraic conclusion without repeating the third hypothesis. More importantly, the theorem treats the matrix-level candidate locus before contextual operational quotienting. The equivalence relation defined by all represented scalar contexts is not shown to be a finite semialgebraic relation, nor is a semialgebraic quotient constructed.

Thus the exact supported statement is:

> the unreduced fixed-packet, fixed-type matrix locus is semialgebraic under a semialgebraic admission hypothesis.

It is not yet a theorem that the operationally reduced seam moduli object is semialgebraic.

The paper correctly avoids a global smooth-manifold claim, so this is scope inflation rather than a wholesale failure of the finite matrix theorem.

## Finding 6 — Moderate: packet invariance is narrower than grammar invariance suggests

**Type:** missing discriminator and terminology inflation

The packet family \(\mathsf{Pkt}(D)\), including the division into candidate preserving and erasing families, is part of the supplied represented theory. “Complete” is described informally as containing every finite typed choice allowed by the frozen comparison grammar, but no categorical quotient identifies duplicate packet presentations, redundant subfamily choices, or alternative role bookkeeping.

Corollary 7.2 assumes not just the same represented arrows and instruments but the same completed packet family and matched-control relation. It therefore proves invariance after packet semantics have already been held fixed. It does not prove that two grammars presenting the same operational arrows but different redundant packet bookkeeping yield the same seam groupoid.

This does not make the fixed-law construction circular: the paper clearly says it is law-relative. It does mean that “intrinsic” is only relative to a represented theory already enriched with frozen packet-comparison data. The stronger grammar-independent reading is not earned.

## Finding 7 — Minor: the active semidirect-product groupoid is specified only schematically

**Type:** formal presentation gap

The passive transformation groupoid has explicit objects and arrows. The active object

\[
\operatorname{Aut}_{\mathrm{phys}}(D)
\ltimes
\mathfrak{Seam}_{W3}(D)
\]

is stated without a corresponding explicit arrow/composition definition or coherence between the active action and passive presentation arrows.

The intended construction is standard and the no-selection theorem does not depend on the omitted formalism. This is not a reason to reject the symmetry result, but it is weaker than the paper’s otherwise explicit groupoid standard.

No material bibliographic defect was found.

---

# Separate rung assessment

| Registered rung | Assessment | Reason |
|---|---|---|
| `RQ0-L0-W3-SEAM-MODULI` | **Not earned under the strict pin** | The fixed-packet raw locus and passive action groupoid exist, but contextual operational reduction is not incorporated and mandatory inaccessible-spectator control C3 is ill-typed. |
| `RQ0-L0-PRESENTATION-INVARIANT-W3-SEAMS` | **Not earned** | It is cumulative on the failed first rung; moreover the spectator theorem fails and the action-equivariance hypothesis needed by Theorem 7.1 is absent. |
| `RQ0-L0-ADDRESSABILITY-FIBRATION` | **Not earned** | It is cumulative on the earlier failures and replaces the required complete Karoubi category by its invertible core. |

---

# Highest exact result that survives

The strongest new result supported by the immutable paper is:

\[
\boxed{
\begin{minipage}{0.88\linewidth}
For a fixed represented operational theory, frozen finite W3 packet, fixed
rank/partition type, and semialgebraic admitted-projector family, the
matrix-level W3-positive nested algebra pairs form a real semialgebraic
locus covariant under passive unitary presentation changes. The associated
prequotient transformation groupoid retains stabilizers. In the declared
four-dimensional atomic branch-memory packet, the locus contains exactly
nine unlabelled seams: six of type \(2+1+1\) and three of type \(2+2\).
Active symmetry forbids invariant selection from a nontrivial transitive
orbit. Minimal admitted containing idempotents exist, and their invertible
cores assemble into a Grothendieck bifibration.
\end{minipage}
}
\]

This is a substantial analytical result. It is narrower than any of the three preregistered headlines because it does not yet control the operational quotient, the required spectator equivalence, or the complete Karoubi fibers.

The previous terminal result

\[
\boxed{\texttt{RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM}}
\]

remains intact and is not weakened by this review.

## Final registered verdict

\[
\boxed{\texttt{HEADLINE-DOWNGRADE}}
\]
