# External hostile review — W3 seam stack

## Operator algebra and quantum instruments

**Reviewed pin:** `21d28d1c80a3a9518887c9b257475694fc5843e8`  
**Reviewed paper:** `dc0a662099361355f0219602bdcab9520f4c25ff`

Both stored SHA-256 values reproduce exactly.

## Overall verdict

\[
\boxed{\texttt{HEADLINE-DOWNGRADE}}
\]

The branch-memory calculation and several fixed-packet operator-algebraic results are correct. However, the paper does not earn any of its three newly registered cumulative rungs as written.

The decisive failures are:

1. the inaccessible-spectator invariance theorem is ill-typed and, at the retained-stabilizer groupoid level, false;
2. the packet definition permits postselected probe families that can manufacture apparent preserving availability;
3. the contextual operational quotient is asserted but not incorporated into the seam action groupoid; and
4. the addressability fiber discards admitted noninvertible Karoubi morphisms despite the pin requiring all such morphisms.

The strongest registered result therefore remains the antecedent:

\[
\boxed{\texttt{RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM}}
\]

at its already adjudicated law-relative coarse-graining scope.

The new paper nevertheless establishes useful narrower results:

- a semialgebraic, packet-relative W3 candidate locus for each fixed finite packet and admitted projector type;
- an exact nine-candidate classification for the displayed branch-memory packet at atomic fine rank;
- covariance under same-dimensional unitary presentation changes;
- and a valid core-groupoid fibration for minimal admitted idempotents if one intentionally discards noninvertible process maps.

Those results should be retained.

---

# Ranked findings

## 1. False theorem: inaccessible-spectator invariance is ill-typed and fails with retained stabilizers

**Severity:** Critical  
**Classification:** False theorem / mandatory invariance failure

Proposition 7.6 sends every arrow to \(a\otimes I_K\), explicitly including preparations and probes. But Definition 2.1 types a preparation as

\[
\eta:\mathbb C\longrightarrow H.
\]

Then

\[
\eta\otimes I_K:K\longrightarrow H\otimes K,
\]

not \(\mathbb C\to H\otimes K\). The same source/target problem occurs dually for probes. Thus the claimed tensor functor is not a functor between the represented theories defined by the paper.

Choosing a fixed spectator state \(\kappa\) would repair the elementary typing:

\[
\eta\longmapsto\eta\otimes\kappa,
\qquad
f\longmapsto f\otimes\kappa^\dagger.
\]

It does not repair the claimed action-groupoid equivalence.

For \(\dim K>1\), spectator unitaries fixing \(\kappa\) can act trivially on every admitted tensor-image amplitude, projector, instrument, preparation, and probe. They therefore produce additional automorphisms of the spectator seam object. For example, when \(\dim K\ge3\), the stabilizer contains a copy of \(U(K-1)\).

The original seam object need not have this automorphism group. Equivalence of groupoids preserves object automorphism groups up to isomorphism. Consequently,

\[
\mathfrak{Seam}_{W3}(D)
\not\simeq
\mathfrak{Seam}_{W3}(D\boxtimes K)
\]

in general when the action groupoids retain these ineffective presentation stabilizers.

This is not merely a missing sentence. Retaining all stabilizers and deleting an inaccessible spectator are incompatible unless the presentation groupoid is first rigidified or ineffective gauge isotropy is explicitly quotiented. The paper does neither.

The contextual operational quotient does not rescue Proposition 7.6 because Definition 5.3 still forms its action groupoid from raw seam objects and passive unitary arrows; it does not quotient those arrows by contextual indistinguishability.

This defeats the mandatory inaccessible-spectator case and therefore blocks `RQ0-L0-PRESENTATION-INVARIANT-W3-SEAMS`.

---

## 2. Missing physical hypothesis: arbitrary probe subfamilies create postselected false seams

**Severity:** Critical  
**Classification:** No-smuggling failure / missing hypothesis

Definition 2.2 permits any nonempty admitted probe family \(\mathsf F\). It does not require \(\mathsf F\) to be:

- a complete measurement context;
- normalized;
- jointly separating;
- closed under complementary outcomes; or
- saturated under all probes admitted for the declared continuation.

Definition 2.2 then says that the complete packet family contains every finite typed choice allowed by the grammar. Freezing those choices before testing \(R\) does not remove the problem: if all finite subfamilies are included, the family contains every fortuitously aligned singleton probe.

A concrete exact counterexample exists.

Let the intermediate and final boundary be \(\mathbb C^4\), with fine atoms \(Q_0,\ldots,Q_3\) and coarse sectors

\[
P_A=Q_0+Q_1,
\qquad
P_B=Q_2+Q_3.
\]

Take two preparations and choose a write isometry satisfying

\[
U\eta_0=\frac{|0\rangle+|2\rangle}{\sqrt2},
\qquad
U\eta_1=\frac{|1\rangle+|3\rangle}{\sqrt2}.
\]

Write correlation holds: each preparation has one live fine atom in each coarse sector.

Choose the matched control

\[
N\eta_0=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad
N\eta_1=\frac{|2\rangle+|3\rangle}{\sqrt2}.
\]

The no-write discriminator holds.

Let \(V\) leave \(|0\rangle\) fixed but mix \(|1\rangle\) and \(|2\rangle\) by a nontrivial rotation. Select only the admitted probe

\[
\mathsf F=\{\langle0|\}.
\]

Then

\[
\langle0|V=\langle0|VP_A,
\]

so Definition 4.3 declares \(V\) preserving.

But the also-admitted probe \(\langle1|\), omitted from the packet, has

\[
\langle1|VP_A\ne0,
\qquad
\langle1|VP_B\ne0.
\]

The continuation therefore merges the record sectors under an accessible outcome and fails the original complete-row meaning of H-avail.

Finally choose an eraser whose first row has nonzero entries in all four columns, such as the normalized \(4\times4\) Walsh matrix. The selected \(\langle0|\) then gives nonzero cross-sector terms, and every fine atom satisfies the paper’s operational-use condition. The tuple passes Definitions 4.1–4.5 despite its preserving result being produced by an incomplete, postselected output context.

A parallel issue exists for arbitrary preparation subfamilies: preparations on which write correlation fails may simply be omitted.

The paper’s fixed branch-memory packet avoids this problem because it explicitly uses all four computational preparations and probes. The general seam definition does not.

At minimum, every W3 packet needs a physically complete outcome instrument or a frozen separating probe context, with an explicit rule governing preparation scope. Without it, the raw locus is a moduli space of packet-relative, potentially postselected witnesses—not a moduli space of stable W3 seams.

This directly undermines the first registered rung.

---

## 3. Construction gap: the contextual operational quotient is not the moduli object actually formed

**Severity:** Major  
**Classification:** Proof/construction gap

Definition 3.5 says seams are counted only up to the induced equivalence of packet arrows and projector algebras in \(\overline D\).

Definition 5.3 instead defines objects using

\[
s\in\operatorname{Seam}^{\mathrm{raw}}_{W3}(D')
\]

and permits only passive unitary presentation changes as arrows. It never:

- replaces \(D'\) by \(\overline{D'}\);
- constructs seam objects inside the quotient;
- adds contextual-equivalence arrows;
- proves that nested concrete \(C^*\)-algebras descend to the quotient; or
- constructs a reduced boundary after dormant summands collapse.

Therefore two contextually indistinguishable packet/projector presentations can remain distinct objects of the stated action groupoid.

There is also a smaller algebraic omission in Proposition 3.6. Equality in all listed scalar contexts establishes compatibility with composition and dagger, but a dagger-linear quotient additionally needs explicit compatibility with sums and scalar multiplication. The definition’s list of contexts does not state those constructors, while the proof simply says “every typed constructor.”

In operationally faithful full-matrix controls this quotient may be trivial, so the branch-memory calculation is unaffected. It does not follow that the general dormant-structure obligation has been discharged.

Because dormant structure control is part of the first rung’s preregistered gate, `RQ0-L0-W3-SEAM-MODULI` is not earned as written.

---

## 4. Pin violation: the addressability fiber omits admitted noninvertible Karoubi maps

**Severity:** Major  
**Classification:** Incomplete construction / false completeness claim

The pin requires:

> Retain all morphisms induced by admitted Karoubi maps and physical automorphisms.

Definition 12.3 retains only **invertible** admitted Karoubi intertwiners. This is the core groupoid of a process category, not the complete admitted addressability category.

The paper’s own two-dephasing control supplies an explicit omitted arrow. Let \(e_n\) and \(e_m\) be its two minimal admitted idempotents and set

\[
h=e_m e_n.
\]

Because the admitted maps are closed under composition, \(h\) is admitted. Moreover,

\[
e_m h e_n
=
e_m(e_m e_n)e_n
=
e_m e_n
=
h,
\]

so \(h\) is a valid Karoubi morphism

\[
(B,e_n)\longrightarrow(B,e_m).
\]

Both \(e_n\) and \(e_m\) fix the seam-relative operator system, hence so does \(h\). For nonorthogonal distinct Bloch axes, \(h\) is not invertible. Definition 12.3 discards it.

The Grothendieck construction in Theorem 12.4 is mathematically valid for the chosen core groupoids. It is not the complete addressability fibration preregistered by the pin.

This independently defeats `RQ0-L0-ADDRESSABILITY-FIBRATION`, even setting aside its cumulative dependence on the failed presentation-invariance rung.

---

## 5. Mandatory Q8 control is not self-contained

**Severity:** Moderate  
**Classification:** Evidence/proof gap

Control 10.4 asserts that the public quaternion process and its attached two-level W3 witness have disjoint boundary and arrow types. The paper does not define the quaternion process, the attached packet, their boundary maps, or the represented subtheory in enough detail to verify that assertion from the paper itself.

The stated conclusion is conceptually correct: an external support list cannot move a W3 packet into an unrelated amplitude subtheory. But this is a typing principle, not the requested hand analysis of the actual Q8 construction.

The control therefore remains an unverified reference to repository antecedents rather than a self-contained exact control.

---

## 6. The two-dephasing idempotent claim is correct only for the pure composition monoid

**Severity:** Minor  
**Classification:** Scope engraving / proof compression

Let

\[
P_n=nn^{\mathsf T},
\qquad
P_m=mm^{\mathsf T},
\qquad
c=n\cdot m,
\qquad
0<|c|<1,
\]

and let \(R\) be the Bloch involution exchanging \(n\) and \(m\). Then

\[
R^2=I,\qquad RP_nR=P_m.
\]

Using these relations and \(P_n^2=P_n\), \(P_m^2=P_m\), every word in the composition monoid reduces to \(I\), \(R\), \(P_n\), \(P_m\), or a rank-one map whose only possible nonzero eigenvalue has modulus \(|c|^k\) for some \(k>0\). Such a mixed word is not idempotent. Thus the only idempotents are indeed

\[
I,\quad P_n,\quad P_m
\]

at the Bloch level.

This conclusion depends on “generated channel category” meaning closure under identity and composition only. If convex randomization or linear closure is also admitted, the proof no longer classifies every generated channel. The paper should engrave this scope explicitly.

This issue does not overturn the control’s intended composition-monoid result.

---

# Independent reconstruction of the W3 equations

## Write and no-write conditions

For a nested pair \(R\subseteq F\), the condition

\[
\|Q_kU\eta\|^2\|Q_\ell U\eta\|^2=0
\]

for \(k\ne\ell\) in one coarse block is exactly the support form of H-corr: a prepared column has at most one live fine alternative per record sector.

The matched-control condition is its correct existential negation on the declared preparation scope.

These equations are typed when each \(Q_k\) is an admitted endomorphism of the intermediate boundary. The paper appropriately distinguishes admitted projectors from arbitrary projectors in \(B(H)\).

## Preserving availability

The equation

\[
fV=fVP_r
\]

is the coordinate-free row-support version of H-avail for one probe. When imposed on a complete final probe context, it is correct.

The flaw is not this equation but the absence of a completeness requirement on the family of probes to which it is applied.

## Coherent erasure

If

\[
(fEQ_kU\eta)\overline{(fEQ_\ell U\eta)}\ne0
\]

for atoms in distinct record sectors, then both \(fEQ_k\) and \(fEQ_\ell\) are nonzero. Therefore the same \(E,f\) cannot satisfy availability for any single coarse sector. W4 genuinely witnesses loss of record-sector availability.

Using the individual cross term rather than a summed Born defect is correct and avoids accidental cancellation.

## Classical seam under preservation

If a preserve cross term through distinct \(Q_k,Q_\ell\) were nonzero, W3 availability would put both in one coarse sector while W1 correlation forbids both from being live there. Hence each such cross term vanishes separately.

Proposition 4.6 is correct. Its proof does not actually require rank-one atoms, although the stated narrower scope is harmless.

---

# Independent branch-memory calculation

The fixed branch-memory calculation reproduces.

With the paper’s preparation ordering, the matrix of \(2U\) in the availability basis is

\[
A=
\begin{pmatrix}
1&1&1&-1\\
1&1&-1&1\\
1&-1&1&1\\
-1&1&1&1
\end{pmatrix},
\qquad
A^{*}A=4I.
\]

Availability under \(V=H\otimes I\) places every availability vector \(v_i\) wholly inside one coarse range. Orthogonality and completeness therefore force every coarse projector to be the span of a block in a set partition of \(\{v_0,v_1,v_2,v_3\}\).

For a two-row block, the restricted sign columns give exactly two rays proportional to

\[
(1,1),\qquad(1,-1),
\]

and these are orthogonal.

For a three-row block, deleting row \(t\) from two distinct Hadamard columns gives inner product

\[
-A_{tj}A_{tk}\in\{-1,+1\}.
\]

The four restricted rays are distinct and no pair is orthogonal, so they cannot fit inside a three-ray orthogonal refinement.

The no-write states are the \(v_i\). In every two-element coarse block, \(v_i\) overlaps both derived sum/difference rays, so W2 passes.

Since \(E=U^\dagger\), the selected fine ray in a block \(B\) contributes

\[
\langle j|EQ_{B,j}U|j\rangle=\frac{|B|}{4}.
\]

Every pair of distinct coarse blocks therefore gives a nonzero cross-sector product

\[
\frac{|B||C|}{16}.
\]

Every derived fine atom occurs in a write column and in a nonzero eraser composite, so the paper’s packet-level operational-use condition holds.

The fifteen partitions classify as follows:

- one \(4\)-block partition: excluded for having only one record value;
- four \(3+1\) partitions: fail write correlation;
- three \(2+2\) partitions: pass;
- six \(2+1+1\) partitions: pass;
- one \(1+1+1+1\) partition: fails the no-write discriminator.

Thus the exact count

\[
\boxed{3+6=9}
\]

is correct for the fixed packet and atomic fine rank.

The memory partition

\[
\{v_0,v_1\}\mid\{v_2,v_3\}
\]

is exactly one of the three \(2+2\) partitions. Its derived fine rays are the computational basis projectors.

This result is conditional on the explicit full-projective-access postulate. It selects nine seams from a supplied family of all atomic projective questions; it does not derive that operational access.

---

# Invariance audit

## Same-dimensional basis and handle changes

Correct. Simultaneous unitary conjugation preserves the equations, and handle permutations change only indexing.

## Redundant grammar

Correct under the paper’s strong hypothesis that the represented completed process theory, instruments, and comparison grammar are identical.

## Kraus invariance

Correct at the CP-map/instrument layer. Equal Kraus representations give the same linear CP map. The paper correctly refuses to replace a coherent amplitude arrow by a Kraus list and correctly distinguishes equal POVMs from equal instruments.

## Minimal instrument-preserving dilation

The stated result is valid under its strong hypotheses: bundle the full outcome instrument into one classical-quantum CP map and use minimal Stinespring uniqueness. The outcome central projections and disturbance branches are then intertwined.

It does not imply invariance under POVM-only Naimark equivalence, and the paper correctly says so.

## Inaccessible spectator

Fails for the reasons in Finding 1.

## Scoped Karoubi refinement

The conditional statement is correct but nearly tautological: once the split presentation extends to the strong represented equivalence of Definition 2.4, Theorem 7.1 applies. Abstract Karoubi completion alone supplies no such result, as the paper correctly notes.

---

# Addressability audit

The operator system

\[
\mathcal S_s(y)
=
\operatorname{span}_{\mathbb C}
\{I,\Phi_a^*(P_r),\Phi_a^*(P_r)^*\}
\]

is derived only after a seam is selected. It does not participate in the W3 equations. This ordering is correct.

The inherited effect transport, sharpness defect, and multiplicative-domain criterion are also correctly scoped to propositions and evidence, not actual outcomes or W6 co-reference.

The order

\[
e\preceq f\iff ef=fe=e
\]

is a partial order on admitted idempotents. If \(e\prec f\), then

\[
\operatorname{Ran}(e)\subsetneq\operatorname{Ran}(f).
\]

Thus finite-dimensional range dimension proves that every nonempty candidate set has a minimal element. Lemma 12.2 is correct.

The unique, unadmitted, and global controls are correct. The two-dephasing control correctly has two incomparable minimal idempotents in its composition-only grammar. What fails is the subsequent deletion of noninvertible admitted Karoubi arrows between those minima.

Accordingly, Theorem 12.4 proves a fibration of **cores**, not the complete process-category-valued fibration required by the pin.

---

# Rung assessment

| Registered rung | Assessment |
|---|---|
| `RQ0-L0-W3-SEAM-MODULI` | **Not earned as registered.** Fixed-packet semialgebraic loci and the nine-candidate branch theorem survive, but arbitrary incomplete probe packets admit postselected false seams, and contextual/dormant reduction is not implemented in the action groupoid. |
| `RQ0-L0-PRESENTATION-INVARIANT-W3-SEAMS` | **Not earned.** Same-dimensional strong unitary equivalence is proved, but the mandatory inaccessible-spectator theorem is ill-typed and false at retained-stabilizer groupoid scope. |
| `RQ0-L0-ADDRESSABILITY-FIBRATION` | **Not earned.** It is cumulative on the failed earlier rungs and its fibers omit admitted noninvertible Karoubi morphisms. A core-groupoid fibration survives. |

## Highest exact result surviving this paper

The strongest new exact statement is:

\[
\boxed{
\begin{minipage}{0.86\linewidth}
For a fixed finite, physically complete experiment packet and a
semialgebraic admitted projector family, the W3 equations define a
packet-relative semialgebraic candidate locus covariant under simultaneous
unitary presentation changes. In the displayed atomic branch-memory packet,
that locus contains exactly nine unlabelled concrete candidate algebras:
six of type \(2+1+1\) and three of type \(2+2\).
\end{minipage}}
\]

The strongest surviving registered programme result remains:

\[
\boxed{\texttt{RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM}}
\]

from the prior adjudicated cycle.

No spatial, overlap, causal, topological, field, or gravity claim is introduced by the paper, and I found no illicit crossing of those exclusions. No material bibliographic error affects the mathematical verdict.
