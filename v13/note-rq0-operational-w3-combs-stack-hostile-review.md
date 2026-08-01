# Independent hostile review — tester sites, sheaves, and stacks

## Executive verdict

\[
\boxed{\texttt{RQ0-L0-BLOCKED-AT-TESTER-DESCENT}}
\]

The first two registered rungs survive:

\[
\boxed{
\texttt{RQ0-L0-COMB-COMPLETE-W3}
\quad\text{and}\quad
\texttt{RQ0-L0-TESTER-SEPARATED-W3}.
}
\]

The third does not survive as written:

\[
\boxed{\texttt{RQ0-L0-W3-TEST-SHEAF}\ \text{NOT EARNED}.}
\]

The paper correctly discovers the universal/existential variance obstruction and proves a valid abstract coordinate-gluing lemma. It also correctly limits “global section” to the terminal tester context of one finite chart.

However, the object claimed to be the tester-evaluation sheaf is not correctly typed: it applies one fixed tester universe to comparisons with different open-comb types. Independently, the candidate groupoid action needed for the quotient prestack is asserted rather than constructed. Stackification cannot repair either missing datum.

The strongest secure third-layer result is therefore:

> On the finite subset site of a frozen tester inventory, an appropriately typed product of probability-coordinate simplexes would satisfy ordinary coordinate descent. Physical W3 validity remains a predicate on realized terminal-context data; no sheaf or stack of physical W3 seams has been constructed.

## Immutable evidence

I reviewed:

- pin commit `3c958da`;
- paper commit `fa02148`;
- dispatch commit `28e4387`;
- the preceding W3 seam-stack and operational-Morita adjudications.

The immutable digests independently reproduce as:

| Artifact | SHA-256 |
|---|---|
| pin | `ec1e1c5e6ba6e003daf1cb0ccb88f13a7cd709fb26b55614ec2a8465ff9ef1f9` |
| paper | `c2c8a27df423b417bcc8e11b68288f7c7169fee0b0f4b8c18b5ca3f440f1b74a` |
| dispatch | `b7aca670086574134495237fffc4428dd642caec528bf5149b212114d4bb3359` |

Commit ancestry is correct, and the repository remained unmodified. Independent exact checks were performed only in `/private/tmp`.

# Findings

## FATAL 1 — the evaluation sheaf mixes incompatible comb types

Section 10 fixes a category

\[
\mathsf{Tester}_D(\tau)
\]

of testers for one process type \(\tau\), and selects one master set \(A\) inside it.

Section 11 then defines

\[
\mathcal E_s(U)
=
\prod_{a\in U}\prod_\Xi X_{s,a,\Xi}
\]

for

\[
\Xi\in
\{W,N,V\star W,V\star\mathcal D_RW,
E\star W,E\star\mathcal D_RW\}.
\]

But these comparisons are not all of the same comb type.

From the paper’s own wire declarations:

\[
W,N
\]

terminate at the pre-continuation \(H_1\) cut or retain the continuation slot, whereas

\[
V\star W,\ E\star W
\]

have the continuation inserted and terminate at \(H_2\), with additional continuation outcome flags where applicable.

A complete tester for the open pre-continuation comb is not automatically a complete tester for the post-continuation process. Equal Hilbert-space dimensions in a benchmark would not cure the typed-wire mismatch.

Therefore \(X_{s,a,\Xi}\) is undefined for a generic pair \((a,\Xi)\). The product \(\mathcal E_s(U)\), its restriction maps, and Theorem 11.1 are not yet typed objects.

Two legitimate repairs exist, but neither is present in the immutable paper:

1. introduce a multi-sorted tester inventory
   \[
   I_D=\coprod_\Xi \mathsf{Test}_D(\tau_\Xi)
   \]
   and form coordinates only for compatible pairs \((a,\Xi)\); or
2. embed every comparison into one common open-comb type using explicitly supplied deterministic fillers and prove the corresponding tester pullbacks.

Until one is done, the third rung fails at its first typing obligation.

## FATAL 2 — the quotient prestack action is not constructed

The paper declares a candidate presentation groupoid \(\mathfrak S\) and says it acts equivariantly on the family \(\coprod_s\mathcal E_s\). That sentence does not supply the action required to form

\[
[\coprod_s\mathcal E_s/\mathfrak S]^\#.
\]

For every arrow \(g:s\to s'\), one needs natural maps on:

- tester handles or tester contexts;
- outcome alphabets and probability simplexes;
- every named comparison;
- restriction maps;

with identity and composition laws.

This is nontrivial because the paper’s presentation invariance transforms process operators and dual testers together. A presentation change can therefore move a tester \(a\) to another tester \(g(a)\). The paper does not prove that the finite master set \(A\) is \(\mathfrak S\)-stable, does not define an action on \(\mathsf{TestCtx}_D\), and does not provide vertical natural isomorphisms when the intended handles are abstractly fixed.

There is a second inconsistency: \(\mathfrak S\) is defined using presentation-gauge arrows, while physical symmetries are said to be a separate action. The displayed quotient contains only \(\mathfrak S\), yet the realized W3 subgroupoid is said to retain physical-symmetry arrows. No enlarged action groupoid containing those arrows is defined.

Consequently the quotient-stack expression is presently notation over missing action data. Stackification supplies descent only after a valid prestack or category fibered in groupoids exists.

## MAJOR 1 — the physical tester category is discarded by the site

The paper correctly distinguishes:

- the complete tester category with conversion maps \(K_f\); and
- the poset of subsets \(U\subseteq A\).

But the actual site is only the second object. Its arrows delete tester coordinates. Refinements, postprocessings and admitted control insertions are not arrows of the site, and their equations are absent from the raw sheaf.

The paper accurately says conversion equations hold only on physically realized tables. Nevertheless, the resulting descent theorem is simply descent on a discrete inventory of tester labels. It does not prove descent compatible with the physical conversion category.

This is not a false theorem, but the correct description is:

> a subset-indexed probability-coordinate site over a frozen tester inventory,

not a site whose categorical geometry is generated by tester conversions.

## MAJOR 2 — realized W3 data do not have a descent theorem

The paper defines only

\[
\operatorname{Real}_{D,s}(A)
\subseteq
\mathcal E_s(A)
\]

at the terminal context. It does not define \(\operatorname{Real}_{D,s}(U)\) for all contexts or prove locality of physical realizability.

That distinction is necessary. Images of global physical models generally do not satisfy sheaf gluing. A minimal counterexample is:

\[
\operatorname{Real}(A)=\{(0,0),(1,1)\}
\]

for two tester coordinates \(A=\{a,b\}\). Each singleton locally realizes both \(0\) and \(1\), but the matching local choice \((0,1)\) has no global physical realization.

The paper explicitly disclaims such physical gluing, so this is not an internal contradiction. It means that

\[
\mathfrak{Seam}_{W3}(D)
\]

is only a predicate on realized terminal-context data. It is not a sheaf or stack of realized W3 seams.

Thus even after repairing the typing, the registered name must always be expanded as:

> tester-evaluation-data sheaf plus terminal-context realized W3 locus.

It must not be shortened to “W3 seams form a sheaf.”

## MINOR 1 — the coverage is a Grothendieck pretopology

The union-cover rule satisfies the identity, pullback and transitivity axioms. Strictly, the displayed covering-family rule is a Grothendieck pretopology or coverage; it generates the corresponding Grothendieck topology of covering sieves.

This is terminological, not mathematical.

## MINOR 2 — stackification and the empty context

The empty family covers \(\varnothing\), so a stack’s fiber over the empty context must satisfy empty descent. Any unconditional statement that stackification “retains stabilizers” needs qualification there: stackification retains the relevant local isotropy after imposing descent, but it need not preserve a nonterminal raw action groupoid over the empty context unchanged.

# Independent reconstructions

## Tester-context coverage

For the poset of subsets of finite \(A\), with covers defined by union:

- identity covers hold;
- pullback is intersection:
  \[
  \bigcup_i(U_i\cap V)=V;
  \]
- transitivity follows from iterated union;
- the empty family covers \(\varnothing\);
- every cover of a singleton contains a member carrying its sole tester.

I exhaustively checked these properties for finite universes of up to three testers.

A cover of \(U\) is jointly separating for

\[
\mathsf{Comb}_U
=
\mathsf{Comb}/\ker\|\cdot\|_U
\]

by construction. Separation at the master context \(A\) remains a declared law postulate rather than a derived theorem, which the paper states honestly.

## Variance obstruction

The variance analysis is correct.

For \(V\subseteq U\):

- universal zero preservation on \(U\) implies preservation on \(V\);
- an eraser witness in \(V\) remains a witness in \(U\);
- an eraser witness available only in \(U\setminus V\) disappears under restriction.

In the exact real/imaginary control:

- the imaginary tester sees a nonzero individual algebraic cross term but zero probability contrast;
- the real tester gives a total retained-source tester distance \(1/2\);
- the preserving dephasing gives zero contrast for both.

Thus the candidate is W3-valid on \(\{T_+,T_i\}\) but not on \(\{T_i\}\). Contextwise-valid seams do not form a presheaf.

This is a genuine and important result.

## Raw coordinate gluing

Once one assumes correctly typed coordinate sets, the product construction

\[
U\longmapsto\prod_{a\in U}X_a
\]

is a sheaf for union covers. Matching tables glue uniquely coordinate by coordinate.

That lemma survives. It applies to arbitrary probability-coordinate assignments, not necessarily to tables jointly realized by a physical comb.

## Singleton discipline

The paper gets this right.

The raw product sheaf always allows abstract missing coordinates to be filled. Such an abstract extension proves nothing physical. A singleton becomes chart-complete only if it extends to an element of the terminal realized image and that global realized table passes the full W3 predicate.

No actual comb, witness or probability contrast is manufactured by sheafification.

## “Global” scope

No atlas-wide tester or state is smuggled in.

Because \(A_D\) is the terminal object of the one-chart subset site, a global section means a section over \(A_D\). The paper states this repeatedly and excludes cross-chart fact identity, spatial overlap and spacetime conclusions.

This wording is sound.

## Nine-candidate classification

The branch-memory calculation independently reproduces:

\[
6\text{ candidates of type }2+1+1,
\qquad
3\text{ candidates of type }2+2.
\]

The six have

\[
\mathcal C_R=5/4,
\]

and the three have

\[
\mathcal C_R=1.
\]

The reconstruction uses the candidate-dependent fine rays inside each coarse block:

- a two-element block yields two orthogonal \((1,1)\) and \((1,-1)\) rays;
- a three-element block gives nonorthogonal restricted rays and fails;
- all singleton blocks lack the no-write discriminator.

The paper could print these fine projectors more explicitly, but the classification is recoverable and correct.

# Registered rung disposition

| Registered outcome | Verdict | Reason |
|---|---|---|
| `RQ0-L0-COMB-COMPLETE-W3` | **EARNED** | Complete CP branches, weights, classical flags, output systems and typed link compositions are retained. |
| `RQ0-L0-TESTER-SEPARATED-W3` | **EARNED** | The operational seminorm and quotient are correct at the frozen tester scope; the imaginary false eraser fails and the real eraser passes with exact distance \(1/2\). |
| `RQ0-L0-W3-TEST-SHEAF` | **NOT EARNED** | The evaluation product is ill-typed across distinct process types, and the candidate action needed for the quotient prestack is not constructed. |
| `RQ0-L0-BLOCKED-AT-TESTER-DESCENT` | **SELECTED** | First exact obstruction after the two surviving rungs. |

`RQ0-L0-BLOCKED-AT-BRANCH-CLASSIFICATION` is not selected: the nine-candidate benchmark survives independent reconstruction.

# Surviving package

The immutable paper securely establishes:

1. a complete finite comb/instrument W3 object;
2. candidate-independent law-relative tester equivalence;
3. tester-visible preservation and coherent recovery;
4. rejection of algebraically nonzero but probability-silent “erasers”;
5. exact complete-instrument and source-weight controls;
6. the nine-candidate \(6+3\) classification;
7. the universal/existential context-variance obstruction;
8. the union-coverage pretopology on a frozen finite tester inventory;
9. the abstract coordinate-gluing lemma;
10. correct one-chart global-section and singleton-extension discipline.

It does not establish:

- a correctly typed multi-process tester-evaluation sheaf;
- a constructed candidate quotient prestack;
- a stack of physical W3 seams;
- descent of physical realizability;
- any atlas-wide, spatial, causal or relativistic structure.

The correct cycle disposition is therefore:

\[
\boxed{\texttt{RQ0-L0-BLOCKED-AT-TESTER-DESCENT}.}
\]
