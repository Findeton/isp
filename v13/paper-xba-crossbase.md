# The Cross-Base Agreement

## What Forces the Holonomy Class-Count Profile on Two Unrelated Bases

**Status:** `GREEN-UNREVIEWED`

**Date:** 2026-08-08

**Frozen pin:** `v13/note-xba-crossbase-pin.md` (sha `7cbde5da4280`), commit
`095c6f7`

**Immutable base:** commit `1426984` — the nomological-transport unit TERMINAL
(v13 LOG #211) and the generality check TERMINAL (v13 LOG #222). No object of
either unit's instrument, and no object of the frozen operator review's
construction, is imported anywhere here: the three files are read, hash-pinned,
and the numbers taken from them are anchored exit-1.

**Receipts:** `v13/code/xba_crossbase_exact.py` →
`xba_crossbase_output.txt`, `xba_crossbase_receipt.json`

**Lean:** NONE.

The dimension-4 third species of §9.4 is a construction contributed by this
unit's external operator round and is rebuilt and gated here (v13 LOG #249).

---

## Abstract

Two bases with no flesh in common — a 36-configuration qubit base over the
quartic field $\mathbb{Q}(\cos\pi/8)$ with an anti-invariant singlet
preparation, and an 81-configuration qutrit base over $\mathbb{Q}$ with an
invariant preparation and a declared completion — carry, at their symmetric
settings, the same based holonomy class counts **82 / 86 / 90 / 106**. The
generality unit registered that agreement OPEN, and a frozen external review
measured how surprising it is: on the common gauge-fixed graph only **96 of the
4,096** Klein-four connections reproduce that profile, against **89** distinct
profiles.

This unit rebuilds the graph, the enumeration and both bases independently and
answers the question. The answer is not a shared statistic. **The two bases'
connections are one and the same point of the 4,096-element space**, and that
point is forced, cycle by cycle, by **five** clauses both bases satisfy — four
facts about the species, each measurable on a base without computing any
holonomy, and one about the declared completion, which is a fact about the
defect that the other four leave behind:

- the **preparation leg is common to the two frames** — the two frames are two
  orders of the same two local events, so the full-leg square around the
  preparation leg closes;
- the **two local legs commute** — so the canonical loop closes;
- at a symmetric setting the **wing exchange intertwines both local legs** — so
  the two realized-rule squares around them close;
- the wing exchange **does not intertwine the preparation leg** — so the one
  remaining realized-rule square carries the defect $D$;
- and **$D$ is an involution** — which is what puts the connection in the
  Klein-four space at all. The first four clauses derive
  $\texttt{SQ\_REAL\_1} = D^{-1}$, and only the fifth makes that $D$.

The fifth clause is not a species fact and not a bookkeeping boundary. An
instance satisfying the first four with a defect of order three is built here:
it carries **the same thirteen gauge-fixed label names** as the two bases and a
**different profile, 42 / 46 / 46 / 72 / 78 / 80**, because its four named
elements do not close into a group. Of the 40,320 members of the declared
completion family, **864** have a non-trivial involutive defect and **96** have
a trivial one.

**The unit's central result is one law.** With $P$ the wing exchange and $u$
the preparation leg,

$$D \;=\; P\,u^{-1}\,P\,u \;=\; [P,\,u],$$

verified on all eight instances against a defect constructed from the
completion alone. Three earlier declaration→structure laws are its corollaries,
each gated: geometry exists exactly where the commutator is non-trivial (the
centraliser criterion, with $\langle P\rangle$ the chart-generating group); the
holonomy group is dihedral of order twice the commutator's order (the
completion-selection law); and the connection's values are what the
completion's determination of that commutator forces.

Three things carry the forcing beyond a restatement. The connection is
**derived** — the thirteen labels and the six cycle values are computed as
normal forms in the group the clauses present, and the derivation is measured
unable to return $\texttt{SQ\_REAL\_1} = D$ unless the fifth premise is
supplied. A **third species** — wings and pointers of dimension four, 256
configurations, sharing no carrier, no rotation, no preparation and no
completion with either base — satisfies the five clauses and reproduces
**82 / 86 / 90 / 106**.
And an **exchange-equivariant** control has $D = \mathbf 1$ and breaks the
profile at once.

The pin's own three candidates are measured and do not force. The source-split
property shrinks the space to **42** and leaves **6** of those reproducing the
profile. Equivariance under the graph's automorphism group is measured
**vacuous** in its rule-preserving form and **fails membership** in its full
form. The admission pattern shrinks the space to **1,728** and is measured
**necessary** but not sufficient.

What is *not* explained is stated as plainly, and there are **two** items. The
two bases' 24-cell admission tables agree, which is what makes the graph common
— an input here, not a result. And both bases' completions have a non-trivial
involutive defect, reached by unrelated routes, which is what puts them in one
connection space — 864 of 40,320, and also not explained here.

**Unit verdict:**
`XBA-SHARED-STRUCTURE-IDENTIFIED`, the property named
**COMPLETION-FORCED-SPLIT**, at the common gauge-fixed graph, at the two
symmetric settings, over the declared Klein-four connection space, per
coordinate.

---

## 1. The question, and the arena it is asked in

The transport unit measured a four-element holonomy group on one committed base;
the generality unit measured the same group on a second base built to share the
species and nothing else. Among the coordinates the two bases were found to
share, one refused to be explained: the **class counts** of the 364 based closed
paths, 82 / 86 / 90 / 106 on both. An isomorphic graph and an isomorphic group
do not fix them — the frozen operator review enumerated every Klein-four
connection on the graph and found that only about one in forty reproduces the
profile. The generality unit recorded the agreement as an open question and
claimed it as confirmation of nothing.

This unit asks what forces it, and answers with a law, a derivation and a
prediction.

### 1.0 The declared arena

| coordinate | this unit's declaration |
|---|---|
| **boundary** | the common gauge-fixed graph at a **symmetric** setting: 8 nodes, 13 links, cycle rank 6 |
| **family** | the $4^6 = 4{,}096$ Klein-four connections on that graph, gauge classes |
| **law** | a connection's holonomy on a closed walk, read as the ordered product of its labels |
| **state** | the 364 reduced closed walks based at $F_1@t{=}0$, bounded at $L_{\max}=8$ |
| **arena action** | the node-valued gauge group ($4^7$ after a declared section) and the graph's automorphism group |
| **admission condition** | the instance's defect is a **non-trivial involution** — E4 and E5 of §2; instances failing it are measured, and lie outside this arena |
| **provenance** | two committed terminal receipts and one frozen review, hash-pinned; every reused number read from them |

Nothing outside this arena is decided. In particular the four asymmetric
settings, whose graphs have nine links and a trivial holonomy group, are not in
it; nor are the instances of §9.3, which satisfy the four species clauses and
whose connections are not Klein-valued.

### 1.1 The graph, rebuilt from the two receipts' own admission tables

The arena is not assumed. Both terminal receipts carry their unit's admission
table cell by cell — for each (setting, checkpoint) coordinate, which gluing
rule draws a link and which permutation it draws. This instrument reads both,
matches them at (setting index, checkpoint) coordinates, and measures the
agreement itself:

| measured | value |
|---|---|
| cells compared | **24** |
| cells where the two bases draw the same rule and the same permutation | **24** |
| **distinct values those 24 cells take between them** | **4** |

The last row calibrates the first two, and it is printed because it is a clue
to the open question rather than a qualification of the answer. The four values
are (FULL draws the identity, REAL draws nothing) at 12 cells, (neither draws)
at 4, (identity, wing exchange) at 6, and (nothing, wing exchange) at 2:
**wherever either rule draws at all, the full-leg rule draws the identity and
the realized rule draws the wing exchange**, so the permutation coordinate is
constant across the whole table and the agreement is an agreement of two
admission *masks*.

The graph is then built from that table at a symmetric setting, and nothing
else:

| coordinate | value | how obtained |
|---|---|---|
| nodes | **8** — (frame, checkpoint), two frames, $t \in \{0,1,2,3\}$ | computed |
| leg links | **6** — three per frame | computed from the leg count |
| identification links | **7** — the full-leg rule at $t \in \{0,1,3\}$ drawing the identity, the realized rule at $t \in \{0,1,2,3\}$ drawing the wing exchange | read from the admission table |
| links | **13** | computed |
| components | **1** | union-find over the links |
| cycle rank | **6** | Euler's formula with the measured component count |

The identification links form four *rungs* between the two frames, of
multiplicities 2, 2, 1, 2 at $t = 0, 1, 2, 3$: at three checkpoints both rules
draw and at $t=2$ only the realized rule does.

### 1.2 The path space

A path is **reduced** — it never traverses one link twice in immediate
succession, a backtrack carrying no transport content — and bounded at
$L_{\max} = 2\cdot\text{NLEGS} + 2 = 8$, the canonical loop's own length.

| measured | value |
|---|---|
| reduced walks, all base points, length zero included | **16,168** |
| closed walks, all base points, length zero excluded | **2,820** |
| closed walks based at $F_1@t{=}0$ | **364** |
| distinct cycle classes those 364 walks carry | **27** |
| closed walks of the full-leg sub-connection | **8** |
| closed walks of the realized-rule sub-connection | **18** |

Every one of those is anchored exit-1 against the two committed receipts. The
delivered rows are audited from themselves: no enumerated walk repeats a link in
immediate succession, every walk is a genuine walk ending at the node it
declares, the graph is connected, and the cycle rank is Euler's.

### 1.3 The connection space, and why it is linear

A **connection** here assigns to each link an element of the Klein four-group
$V = \{\mathbf 1, W, D, WD\}$; two assignments differing by a group element at
each node are the same connection. Gauge-fixing on a spanning tree leaves one
free label per cotree link, so the space has $4^6 = 4{,}096$ points — the
frozen review's own count, reproduced here from an independently chosen tree.

Because $V$ is abelian, the holonomy of a closed walk depends only on the
**parity** with which the walk traverses each link. A connection is therefore a
linear map from the cycle space $H_1(G;\mathbb{F}_2) \cong \mathbb{F}_2^6$ to
$V \cong \mathbb{F}_2^2$, and a walk's holonomy is that map applied to the
walk's cycle class. Two consequences are used throughout and both are measured
rather than assumed: the class-count profile is a function of the connection's
values on **any** basis of the cycle space, and it is invariant under the whole
gauge group (§11).

That the group is abelian is a *fact about the instance*, not a convention:
§9.3 exhibits an instance whose thirteen labels carry the same four names and
whose named elements do not close, and there the linear model is measured to be
wrong on 89 of the 364 walks.

### 1.4 The declared cycle basis

Six cycles are declared, each built from the graph and the two rules and each
the *elementary* cycle of one structural fact:

| cycle | edges | what it is |
|---|---|---|
| `SQ_FULL_1` | `FULL@0`, leg 1 of $F_1$, `FULL@1`, leg 1 of $F_2$ | the full-leg square around the **preparation** leg |
| `CANON` | `FULL@0`, the three legs of $F_1$, `FULL@3`, the three legs of $F_2$ | the **canonical loop** |
| `SQ_REAL_1` | `REAL@0`, leg 1 of $F_1$, `REAL@1`, leg 1 of $F_2$ | the realized-rule square around the **preparation** leg |
| `SQ_REAL_2` | `REAL@1`, leg 2 of $F_1$, `REAL@2`, leg 2 of $F_2$ | the realized-rule square around the **first local** leg |
| `SQ_REAL_3` | `REAL@2`, leg 3 of $F_1$, `REAL@3`, leg 3 of $F_2$ | the realized-rule square around the **second local** leg |
| `BIGON_0` | `FULL@0`, `REAL@0` | the **bigon** where the two rules meet at $t=0$ |

Their independence over $\mathbb{F}_2$ is measured (rank **6**) and the change of
coordinates to the cotree basis is measured invertible. Every candidate
predicate below is stated on these six values, so every one of them is a
statement about the connection and not about the bookkeeping — §11's
spanning-tree flip-test measures exactly that.

---

## 2. The candidate properties, declared

Everything in this section is a **declaration**, recorded before any profile of
any member of the 4,096 was computed. The instrument gates the freeze with the
census-profile counter measured at **zero** at the declaration point, and the
`freeze-lax` mutant, which evaluates one profile first, dies at that gate. Two
things are *not* claimed by that gate and are stated here instead: the realized
class counts are an **anchored input**, read out of the two terminal receipts
before anything is declared, and they are recomputed from the rebuilt bases by
the comparator of §3 and by the positive control before the declaration point.
What the counter measures is that no member of the 4,096 had had its profile
evaluated.

The graph's automorphism group is computed first, because one candidate needs
it:

| measured | value |
|---|---|
| $\lvert\mathrm{Aut}\rvert$, rule-preserving (leg / full-leg / realized links preserved) | **2** |
| its distinct induced actions on the cycle space | **1** — the trivial one |
| $\lvert\mathrm{Aut}\rvert$, the bare multigraph | **16** |
| its distinct induced actions on the cycle space | **8** |

The rule-preserving group is generated by the frame swap, which **fixes each of
the seven identification links and exchanges the six leg links in matching
pairs** — 7 fixed and 6 moved, measured; because every declared cycle contains
the matching pair of legs, each cycle's edge set is carried to itself and the
induced action on $H_1$ is trivial. That is recorded here, before the candidate
is measured, because it is what makes one form of the equivariance candidate
vacuous.

**The candidates.** The pin names three. One of them — equivariance — admits
more than one honest reading, so it is declared in all three of them rather than
in whichever one would flatter the result; that makes **five** pin rows. Seven
more are this unit's, each naming one clause of the species the two bases were
built to share.

| candidate | source | the predicate |
|---|---|---|
| **C1** source-split | pin | the full-leg sub-connection is flat; the realized-rule sub-connection's holonomy group has order exactly two; every two-rule coordinate carries a non-flat bigon; the whole connection generates a group of order four |
| **C2a** equivariance, rule-preserving | pin | invariant under the induced action of the rule-preserving automorphism group |
| **C2b** equivariance, full | pin | invariant under the induced action of the full multigraph automorphism group |
| **C2c** equivariance up to naming | pin | for every graph automorphism there is an automorphism of the Klein group carrying the pullback back to the connection |
| **C3** admission pattern | pin | every coordinate at which the two rules draw *different* permutations carries a non-flat bigon |
| **C4** clause-split, named | worker | the six declared cycles take the values the clauses *derive* (§7), with the group elements named |
| **C5** clause-split, naming-closed | worker | there are distinct non-identity $d, w$ with the six declared cycles at $(\mathbf 1, \mathbf 1, d, \mathbf 1, \mathbf 1, w)$ |
| **C6** common preparation leg | worker | `SQ_FULL_1` is flat |
| **C7** commuting local legs | worker | `CANON` is flat |
| **C8** intertwined local legs | worker | `SQ_REAL_2` and `SQ_REAL_3` are flat |
| **C9** unintertwined preparation leg | worker | `SQ_REAL_1` is neither flat nor equal to `BIGON_0` |
| **C10** group of order four | worker | the connection's labels generate a group of order four — the explanation the generality unit offered |

**What C3 can and cannot say.** The 24-cell admission table fixes *which* links
exist and *which permutation each draws*. On a connection it therefore
constrains exactly one thing: where two rules meet and draw different
permutations, their bigon cannot be flat. It says nothing about any cycle that
traverses a leg, because what such a cycle picks up is a property of the legs
and not of the table. C3 is that one constraint and no more, and it is declared
that way.

**The five clauses.** Each of C6–C9 is the elementary cycle of one clause, in
the correspondence §7 derives. The fifth clause is not a cycle condition: it is
the arena's admission condition, and it is measured on each instance directly.

| clause | what it is | measured on both bases | forces |
|---|---|---|---|
| **E0** the two rules draw different maps at $t=0$ | admission fact | the admission table | `BIGON_0` $= W$ |
| **E1** the preparation leg is common to the two frames | species clause | structural, and gated | `SQ_FULL_1` $= \mathbf 1$ |
| **E2** the two local legs commute | species clause | measured at all nine declared pairs by both units | `CANON` $= \mathbf 1$ |
| **E3** at a symmetric setting the wing exchange intertwines both local legs | species clause | measured by both units | `SQ_REAL_2` = `SQ_REAL_3` $= \mathbf 1$ |
| **E4** the wing exchange does not intertwine the preparation leg | species clause | measured by both units | `SQ_REAL_1` $= D^{-1} \neq \mathbf 1, W$ |
| **E5** the defect $D$ is an involution | **completion fact** | measured on each instance | $D^{-1} = D$, so `SQ_REAL_1` $= D$ |

E1–E4 are the four clauses of the species the generality unit declared and
measured. **E5 is not among them**: it is a property of the declared completion,
it is what the arena's Klein-four family assumes, and §7 measures that without
it the derivation stops one step short.

---

## 3. The two bases, rebuilt, and the connection they realize

Neither base is imported. The first is rebuilt over the totally real quartic
field $\mathbb{Q}(\cos\pi/8)$, elements carried as rational 4-tuples reduced by
$x^4 = x^2 - \tfrac18$ so that tuple equality is field equality; base G is
rebuilt over $\mathbb{Q}$ from the rotation matrices and the $9\times9$
completion the generality paper prints, anchored against them entry by entry.

Each base is read at **both** of its symmetric settings, so there are four
readings in all.

| measured, per rebuilt instance | base 1 | base G |
|---|---|---|
| configurations | **36** | **81** |
| wing-exchange fixed configurations | **6** | **9** |
| defect $D = P_W U_{\text{prep}}^{-1} P_W U_{\text{prep}}$, fixed configurations | **18** | **45** |
| **E5** — $D$ is an involution | yes | yes |
| **E5** — the four named elements close into a group | yes | yes |
| **E1** — the preparation leg is common to the two frames | yes | yes |
| **E2** — the two local legs commute | yes | yes |
| **E3** — the wing exchange intertwines the local legs | yes | yes |
| **E4** — the wing exchange intertwines the preparation leg | **no** | **no** |
| every declared operator exactly orthogonal | yes | yes |

The gauge-fixed labels are then computed directly: with $T_n$ the transport
along the spanning tree from the base node, a link $\ell : a \to b$ carrying the
matrix $M_\ell$ gets the label $T_b^{-1} M_\ell T_a$. Measured, at all four
readings:

| link | label |
|---|---|
| all six leg links | $\mathbf 1$ |
| `FULL@0`, `FULL@1`, `FULL@3` | $\mathbf 1$ |
| `REAL@0` | $W$ |
| `REAL@1`, `REAL@2`, `REAL@3` | $WD$ |

Every one of the 13 labels lies in the Klein four-group, at every reading, and
**all four readings give the same connection**: one point of the 4,096.

*Under which identification.* Each base has its own Klein four-group, of
permutations of its own 36 or 81 configurations; they are identified with the
abstract $\{\mathbf 1, W, D, WD\}$ by **what their elements are** — the
identity, that base's own wing exchange, that base's own defect
$P_W U_{\text{prep}}^{-1} P_W U_{\text{prep}}$, and their product. That
identification is a declaration, it is measured to be a bijection on each base
(the four elements are gated distinct) and to be a group (they are gated
closed), and it is the same one both terminal receipts use when they name their
class counts. Everything element-wise in this paper is at that identification;
everything multiset-wise is independent of it.

On the declared cycle basis the shared point is

$$(\texttt{SQ\_FULL\_1},\ \texttt{CANON},\ \texttt{SQ\_REAL\_1},\ \texttt{SQ\_REAL\_2},\ \texttt{SQ\_REAL\_3},\ \texttt{BIGON\_0}) \;=\; (\mathbf 1,\ \mathbf 1,\ D,\ \mathbf 1,\ \mathbf 1,\ W).$$

**An independent comparator, with no gauge-fixing in it.** The holonomy of each
of the 364 based closed walks is recomputed by multiplying the raw link matrices
of the base itself — $36\times36$ over the quartic field, $81\times81$ over
$\mathbb{Q}$ — and its permutation part taken. Measured: **4** distinct
holonomies with class counts 82 / 86 / 90 / 106, and **0 of 364** walks where
the two routes disagree, on both bases. The comparator shares no component with
the gauge-fixing it audits: the `direct-order` mutant, which composes the link
matrices in the wrong order, and the `reverse-lax` mutant, which traverses a
link backwards without transposing, both die there.

**The positive control.** Each of the four readings' class counts is recomputed
a third way — from that reading's own thirteen measured labels, by the ordered
walk product of §4 — and compared **against the numbers read out of the two
terminal receipts**, element by element. All four give
$\mathbf 1{:}82,\ W{:}86,\ D{:}90,\ WD{:}106$. This control does not pass
through the shared connection or through the census profiler, so it is not
carried by the gate that measures the four readings to agree; the
`anchor-classcounts` mutant, which perturbs the number read from the receipt,
and the `route2-lax` mutant, which perturbs the walk product, both die on it.

---

## 4. The connection space, enumerated — by two different algorithms

| measured | value |
|---|---|
| connections on the graph | **4,096** |
| distinct class-count profiles | **89** |
| the realized profile | $\mathbf 1{:}\,82$, $W{:}\,86$, $D{:}\,90$, $WD{:}\,106$ |
| connections reproducing it **as a multiset** | **96** of 4,096 |
| connections reproducing it **element by element** | **16** |
| connections whose labels generate the whole group | **3,906** |
| of those, reproducing the profile | **96** |
| most common profile | $(78, 90, 94, 102)$ at **384** connections |

The frozen review's numbers are read out of the review's own table and out of
the generality receipt and anchored exit-1 against these; the 3,906 is also the
count of surjective linear maps $\mathbb{F}_2^6 \to \mathbb{F}_2^2$, which is
why it comes out of an independent rebuild unchanged.

The profile's four counts are distinct, so each element-wise hit has six
distinct relabellings: the 96 multiset-hits are exactly the six relabellings of
the 16 element-wise hits.

**Two routes, and why they are two.** The first route works in the cotree cycle
coordinates: each walk is reduced to a six-bit cycle class and a connection's
profile is a function of those classes. The second reconstructs the **thirteen
link labels** of each connection — the identity on the tree, the six free values
on the cotree — and takes the ordered walk product over each walk's own
thirteen-link parity vector. It builds no cycle coordinate and inverts no change
of basis, so a defect in the cycle bookkeeping corrupts the first route alone —
the `cycle-lax` and `basis-lax` mutants do exactly that, and die upstream, at
the reused-number anchors and at the basis gate respectively. What kills this
gate itself is `route2-lax`, which drops one link from the second route's walk
product. Measured: **0 of 4,096** connections where the two routes disagree,
with all three census numbers identical and the second route's 27 distinct walk
parity vectors matching the first route's 27 distinct cycle classes.

The second spanning tree of §11 is **not** a second route in this sense, and is
reported there as the disclosure it is.

---

## 5. The candidates, measured

Exhaustive over the whole space; "forces" means every member of the constrained
subset reproduces the profile.

| candidate | both bases satisfy | subset | shrink | members reproducing the profile | forces (multiset) | forces (element-wise) |
|---|---|---|---|---|---|---|
| **C1** source-split | yes | **42** | 97.5$\times$ | 6 | no | no |
| **C2a** equivariance, rule-preserving | yes | **4,096** | 1$\times$ | 96 | no | no |
| **C2b** equivariance, full | **no** | 64 | 64$\times$ | 0 | no | no |
| **C2c** equivariance up to naming | **no** | 136 | 30.1$\times$ | 0 | no | no |
| **C3** admission pattern | yes | **1,728** | 2.37$\times$ | 96 | no | no |
| **C4** clause-split, named | yes | **1** | 4096$\times$ | 1 | **yes** | **yes** |
| **C5** clause-split, naming-closed | yes | **6** | 682.7$\times$ | 6 | **yes** | no |
| **C6** common preparation leg | yes | 1,024 | 4$\times$ | 24 | no | no |
| **C7** commuting local legs | yes | 1,024 | 4$\times$ | 24 | no | no |
| **C8** intertwined local legs | yes | 256 | 16$\times$ | 24 | no | no |
| **C9** unintertwined preparation leg | yes | 2,304 | 1.78$\times$ | 48 | no | no |
| **C10** group of order four | yes | 3,906 | 1.05$\times$ | 96 | no | no |

**The pin's three candidates, read out.**

*C1 does not force, and the gap is exactly measured.* The source-split property
— full-leg sub-connection flat, realized-rule sub-connection of group order two,
every bigon non-flat, whole group of order four — is satisfied by both bases and
cuts 4,096 to **42**, a shrink of 97.5. Of those 42, **6** reproduce the
profile. What the 36 others have and the 6 do not is a single clause: the
realized-rule sub-connection's group can be of order two while its three
elementary squares carry $d$ in some pattern other than "the preparation square
alone". C1 is therefore **PARTIAL** in the pin's sense, with the residual
named.

*C2 is vacuous in one form and false in the others.* The rule-preserving
automorphism group acts trivially on the cycle space, so C2a is satisfied by
every one of the 4,096 connections — measured, and reported as the vacuity it
is. Its non-vacuous forms fail membership: the realized connection is **not**
invariant under the full multigraph automorphism group, which permutes the two
links of a doubled rung, and is not equivariant up to a relabelling of the Klein
group either. That is a real reading and not a defect of the instrument: the two
gluing rules are not interchangeable, one drawing the identity and the other the
wing exchange, so a symmetry that swaps them is not a symmetry of this
connection. It is also the demonstration that the equivariance machinery can
fire at all: C2b and C2c evaluate through the same induced-action code and both
return **False** on the realized connection, with subsets 64 and 136.

*C3 is necessary and not sufficient.* The admission pattern cuts 4,096 to
**1,728**, and every one of the 96 profile-reproducing connections lies inside
it — measured by the exhaustive violator census below, which finds **0**
violators of C3 reproducing the profile. So the 24-cell table is load-bearing;
it is simply not enough.

**C4 and C5 force, and what that does and does not mean.** C5's subset has six
members, which are one orbit under the six relabellings of the Klein group, and
all six carry the profile; C4 fixes the naming and its subset is the realized
connection alone. As a statement about subsets, forcing at size one is trivial,
and this paper says so rather than trading on it. The content is elsewhere and
is measured in §6, §7 and §8: the clauses of C4 and C5 are not read off the
answer but are the elementary cycles of five facts both bases satisfy, the
connection is *derived* from those facts, and instances built to satisfy them —
including one of a different species — reproduce the profile.

**Sufficiency and necessity, separated.** For each candidate the instrument
counts, exhaustively, the connections that violate it and reproduce the profile
anyway:

| candidate | violators reproducing the profile anyway | reading |
|---|---|---|
| C3 admission pattern | **0** of 2,368 | **necessary**, not sufficient |
| C10 group of order four | **0** of 190 | **necessary**, not sufficient — *analytically forced* |
| C1 source-split | 90 of 4,054 | neither |
| C5 clause-split, naming-closed | **90** of 4,090 | **sufficient**, not necessary |
| C4 clause-split, named | 95 of 4,095 | **sufficient**, not necessary |
| C6 / C7 | 72 of 3,072 | neither |
| C8 intertwined local legs | 72 of 3,840 | neither |
| C9 unintertwined preparation leg | 48 of 1,792 | neither |

Two disclosures belong with that table. C10's necessity **could not have come
out otherwise**: the target profile has four non-zero counts, so any connection
reproducing it attains all four group elements and generates the group; the row
is a disclosure, and C3's zero — for which no such argument exists — is the real
measurement. And this column is *not* an independent second census: the
instrument iterates the complement rather than subtracting, but every entry
equals $96 - (\text{hits in subset})$ as an algebraic identity, so the two
columns are one route and the table is not corroboration of itself.

Ninety connections outside C5 carry the profile. The clauses are a sufficient
explanation of *this* agreement, not a characterisation of the profile.

---

## 6. Where the 4,096 collapses

The clauses are added in their declared order and the survivors counted. The
chain begins one step earlier than the space: the **first** cut is the one that
puts an instance into this connection space at all.

| clause added | survivors | of which reproduce the profile |
|---|---|---|
| the declared completion family | **40,320** | — |
| **E4 + E5** the defect is a non-trivial involution | **864** | — |
| — the Klein-four connections it then has | 4,096 | 96 |
| **E0** the two rules draw different maps at $t=0$ | **3,072** | 96 |
| **E1** the preparation leg is common to the two frames | **768** | 24 |
| **E2** the two local legs commute | **192** | 12 |
| **E3** the wing exchange intertwines both local legs | **12** | 6 |
| **E4** the wing exchange does not intertwine the preparation leg | **6** | **6** |

The top two rows are a census of completions, not of connections, and they are
measured here from the permutation algebra alone: of the 40,320 members of the
declared family, **96** have a trivial defect (the exchange-equivariant locus)
and **864** have a non-trivial involutive one. Both figures reproduce the
generality unit's own terminal table, which was measured on $81\times81$
operators, and both are anchored exit-1 against it.

Two things about the lower six rows should be said at the claim. First, **the
survivor counts in that column are analytically forced** once the six declared
cycles are a basis: each clause pins coordinates and the factor records how many
— $4^6, 3\cdot4^5, 3\cdot4^4, 3\cdot4^3, 3\cdot4, 3\cdot2$. The measurement is
in the second column. Second, because the six survivors are a single
relabelling orbit and the multiset profile is relabelling-invariant, the last
row carries the same content as the positive control; the work is done by the
rows above it. On those twelve E3-survivors, E4 holds if and only if the
connection generates the whole group — so what the clause account adds over the
generality unit's "group of order four" is the four clauses above it, not this
one.

---

## 7. The derivation, computed

### 7.1 The group the clauses present

Write $u$ for the preparation leg, $a$ and $b$ for the two local legs, and $P$
for the wing exchange. The clauses are relations:

$$P^2 = \mathbf 1, \qquad ab = ba \quad (\mathbf{E2}), \qquad PaP = b,\ \ PbP = a \quad (\mathbf{E3}),$$

and E1 says the two frames carry the **same** $u$. Nothing relates $u$ to $P$.
So the clauses present the free product

$$G \;=\; \bigl(\mathbb{Z}^2 \rtimes C_2\bigr) * \mathbb{Z}, \qquad \mathbb{Z} = \langle u\rangle,$$

in which every element has a normal form — an alternating list of syllables
$a^\alpha b^\beta P^\pi$ and $u^n$ — and equality of normal forms is equality in
the group. The instrument evaluates in $G$. Nothing in this section is typed.

### 7.2 The thirteen labels, derived

With the spanning tree taken to be the six leg links together with `FULL@0`, the
transports are the ordered leg products of each frame ($u, a, b$ along frame 1;
$u, b, a$ along frame 2), and the label of a link $\ell : x \to y$ carrying $M$
is $T_y^{-1} M T_x$. Evaluated in $G$:

| links | derived label |
|---|---|
| the six legs, `FULL@0`, `FULL@1`, `FULL@3` | $e$ |
| `REAL@0` | $P$ |
| `REAL@1`, `REAL@2`, `REAL@3` | $u^{-1}Pu$ |

Nine of the thirteen are the identity **for any instance whatever**: seven
because they are tree links and two because E1 and E2 close the full-leg
squares. The three equalities in the last row use E3 twice each. The derived
labels are measured to agree with the labels read off every rebuilt instance,
under $u^{-1}Pu = P\cdot D$.

### 7.3 The six cycle values, and where the fifth premise enters

Each declared cycle is traversed as an ordered closed walk and its holonomy word
evaluated in $G$:

$$\texttt{SQ\_FULL\_1} = e,\quad \texttt{CANON} = e,\quad \texttt{SQ\_REAL\_2} = e,\quad \texttt{SQ\_REAL\_3} = e,\quad \texttt{BIGON\_0} = P,$$

$$\texttt{SQ\_REAL\_1} \;=\; u^{-1}P\,u\,P \;=\; D^{-1}, \qquad D := P u^{-1} P u .$$

**The four species clauses derive $D^{-1}$, not $D$.** In $G$ the two are
different elements
— the instrument measures $D^2 \neq e$ there — and $D^{-1} = D$ is exactly the
fifth premise. Supplied, the six values are

$$(\mathbf 1,\ \mathbf 1,\ D,\ \mathbf 1,\ \mathbf 1,\ W),$$

which is measured equal, entry by entry, to the tuple both rebuilt bases
realize. Withheld, the derivation returns a value that is not in the Klein group
at all and the gate fails: the `involutive-lax` mutant does exactly that and
dies, and the `species-lax` mutant, which drops the relation $PaP = b$, kills
$\texttt{SQ\_REAL\_2} = e$ and dies too. A derivation that cannot be run without
naming its premises is the point of running it.

The general law is therefore $\texttt{SQ\_REAL\_1} = D^{-1}$: it equals $D$ when
the defect is an involution, and $D^{2}$ when the defect has order three — which
is the case §9.3 builds.

*Orientation.* $\texttt{SQ\_REAL\_1}$ is $D^{-1}$ in the traversal the
instrument takes and $D$ in the reverse one; the two coincide exactly when the
fifth premise holds, which is why the Klein-valued answer does not depend on the
convention and the counter-instance of §9.3 does.

---

## 8. The commutator law, and the three laws that are its corollaries

### 8.1 The law

$$\boxed{\;D \;=\; P\,u^{-1}\,P\,u \;=\; [P,\,u]\;}$$

The defect is the **commutator of the declared exchange with the declared
preparation leg**. It is stated here as this unit's central result and it is
gated on every instance the unit builds, against a defect constructed from the
completion alone — the generality unit's own law
$D = (\Sigma V^{\mathsf T}\Sigma V)\otimes I$, in which neither the wing
exchange operator nor the preparation leg operator appears. The comparator is
therefore not the constructor.

| instance | carrier | $P^2 = \mathbf 1$ | $D = [P,u]$ | $D$ = the completion's own defect | $PDP = D^{-1}$ | $\mathrm{ord}(D)$ | $\lvert\langle W,D\rangle\rvert$ | distinct holonomies | class counts |
|---|---|---|---|---|---|---|---|---|---|
| base 1 @ SP-E | 36 | yes | yes | yes | yes | 2 | 4 | 4 | 82/86/90/106 |
| base 1 @ SP-F | 36 | yes | yes | yes | yes | 2 | 4 | 4 | 82/86/90/106 |
| base G @ GP-E | 81 | yes | yes | yes | yes | 2 | 4 | 4 | 82/86/90/106 |
| base G @ GP-F | 81 | yes | yes | yes | yes | 2 | 4 | 4 | 82/86/90/106 |
| base S — third instance | 81 | yes | yes | yes | yes | 2 | 4 | 4 | 82/86/90/106 |
| base S′ — equivariant control | 81 | yes | yes | yes | yes | 1 | 2 | 2 | 172/192 |
| base T — counter-instance | 81 | yes | yes | yes | yes | 3 | 6 | 6 | 42/46/46/72/78/80 |
| species 4 — third species | 256 | yes | yes | yes | yes | 2 | 4 | 4 | 82/86/90/106 |

The relation $PDP = D^{-1}$ is also derived symbolically in $G$, so the group
$\langle W, D\rangle$ is dihedral by algebra and measured dihedral on every row.

### 8.2 Corollary one — existence: geometry is the failure to centralise

$\langle W,D\rangle$ is larger than $\langle W\rangle$ **exactly** where
$[P,u] \neq \mathbf 1$, that is exactly where the declared exchange fails to
centralise the declared preparation leg. Both sides of the equivalence occur
among the instances above: the equivariant control centralises and has two
holonomies, the other seven do not and have four or six. This is the closure
criterion of the cocycle unit with the chart-generating group taken to be
$\langle P\rangle$: where the declared symmetry centralises a declared leg, the
loop around that leg closes; where it does not, **the commutator is the
curvature**.

### 8.3 Corollary two — order: the group is twice the commutator

$$\lvert\langle W, D\rangle\rvert \;=\; 2\cdot\mathrm{ord}\bigl([P,u]\bigr) \;=\; \text{the number of distinct holonomies the 364 walks carry},$$

measured on all eight instances, at the three orders 1, 2 and 3 that occur. This
is the generality unit's completion-selection law — the completion selects the
holonomy group's isomorphism type within a dihedral family — restated as a
property of one commutator, and it is why the whole 40,320-member census of §6
is a census of $\mathrm{ord}([P,u])$.

### 8.4 Corollary three — forcing: the profile is a function of that order

Across every instance measured here the class-count profile is a function of
$\mathrm{ord}([P,u])$ **alone**, and the three orders that occur give three
different profiles:

| $\mathrm{ord}([P,u])$ | profile | instances |
|---|---|---|
| 1 | 172 / 192 | the equivariant control |
| 2 | 82 / 86 / 90 / 106 | both bases at both settings, the third instance, the third species |
| 3 | 42 / 46 / 46 / 72 / 78 / 80 | the counter-instance |

Carrier dimension, number field, preparation vector, Schmidt rank, measurement
rotation and pointer geometry all vary across those rows and none of them moves
the profile. **That is the forcing, stated at its true strength**: not that a
species forces a profile, but that a completion's commutator does, and the
species clauses are what make the connection depend on nothing else.

This is why the property is named **COMPLETION-FORCED-SPLIT**. The forcing
declaration is the completion, not the species: the exchange-equivariant control
of §9.2 satisfies **every clause of the declared species** — the generality unit
measures it so — and carries a different profile.

And it is why this unit claims **no third declaration→structure law**. The
transport-generality law and the closure criterion are the same statement read
at two places: a declared symmetry's centraliser decides the geometry. Where the
declared exchange centralises a declared leg the loop around it closes; where it
fails to, the commutator *is* the holonomy; and the order of that commutator —
a property of the declared completion — selects the group and hence the profile.
What this unit adds is the refinement from the group's isomorphism type to the
connection's gauge class, and the measurement that nothing else about the
instance enters.

---

## 9. Four instances

### 9.1 A third instance, and exactly what it risked

A third instance of the species was built and its class counts measured
afterwards: a fresh integer quaternion $(5,1,2,3)$ appearing in neither unit, an
exchange-invariant preparation of **Schmidt rank two** where base G's has rank
three, and a different completion transposition.

| measured on the third instance | value |
|---|---|
| defect fixed configurations | **45** of 81 |
| distinct holonomies over the 364 based closed walks | **4** |
| class counts | **82 / 86 / 90 / 106** |
| declared cycle basis | $(\mathbf 1, \mathbf 1, D, \mathbf 1, \mathbf 1, W)$ |

**Two of its three declared variations are measured inert, and the prediction
risked one bit.** The preparation cancels out of the defect — over all 36 single
transpositions of the system-pair labels, the two declared exchange-invariant
preparations give the **same** defect, 36 of 36 — and the measurement rotation
enters neither the preparation leg nor the wing exchange, so the defect is
measured identical across six integer quaternions, with E2 and E3 holding at all
six. The single live parameter is the completion transposition, and its only
effect is to select $\mathrm{ord}([P,u])$: of the 36 single transpositions, 6
give order 1, **12** give order 2 and **18** give order 3 — a defect of order
three whose connection is not Klein-valued and therefore not in this arena, and
E5 is exactly what selects the first twelve. What the third instance tests is
that its transposition falls in the twelve — one bit — and that the
implementation is sound. It is claimed at that strength and no more.

### 9.2 The control that breaks it

The same construction with an **exchange-equivariant** completion — the bare
Householder, with the transposition removed — satisfies every clause of the
declared species and every clause here except E4: the wing exchange then
intertwines the preparation leg as well, and the defect is the identity.
Measured: $D$ fixes all **81** configurations, the 364 walks carry only **2**
distinct holonomies, and the class counts are **172 / 192**. The
`control-completion` mutant, which gives that control a defect after all, dies
at the gate.

### 9.3 The counter-instance: four clauses, and a different profile

The completion is not chosen but computed: **the lexicographically first single
transposition of the system-pair labels, fixing the first label, whose defect
has order three** — the transposition $(1,4)$.

| measured on the counter-instance | value |
|---|---|
| E1, E2, E3, E4 | **all hold** |
| E5 — the defect is an involution | **fails**: $\mathrm{ord}(D) = 3$ |
| the four named elements close into a group | **no** |
| the thirteen gauge-fixed label **names** | **identical to the two bases'** |
| distinct holonomies over the 364 walks | **6** |
| class counts | **42 / 46 / 46 / 72 / 78 / 80** |

This is the sharpest form of the fifth premise. A reader who applies the four
species clauses to a new instance gets the wrong answer 18 times out of 36; and
the failure is not visible in the labels, because the labels are the same four
names. What fails is that the names no longer determine the holonomy: the linear
model over the four names disagrees with the raw matrix product on **89 of the
364** walks, against 0 of 364 on every instance inside the arena.

### 9.4 A third species

The clauses do not fix the carrier. An instance of a genuinely different species
was built: **wings of dimension four, pointers of dimension four, 256
configurations**, a rational orthogonal rotation built from two Pythagorean
blocks, an exchange-invariant preparation of Schmidt rank two, and a completion
transposition of the sixteen system-pair labels — again the lexicographically
first involutive one, $(1,2)$.

| measured on the third species | value |
|---|---|
| carrier | **256** configurations |
| wing-exchange fixed configurations | **16** of 256 |
| defect fixed configurations | **192** of 256 |
| E1–E5 | **all hold** |
| the thirteen gauge-fixed labels | $\mathbf 1^{\times 9},\ W,\ WD,\ WD,\ WD$ — identical |
| distinct holonomies over the 364 walks | **4** |
| class counts | **82 / 86 / 90 / 106** |
| its own completion family | 120 transpositions, splitting **12 / 60 / 48** by defect order |

It shares no carrier, no rotation, no preparation and no completion with
either base, and it reproduces the profile element by element.
That is the different-flesh confirmation the third instance of §9.1 could not
supply, and it shows that the carrier shape is a fourth inert parameter. Its
transposition family splits in the same three-way pattern as at dimension three,
which is corollary two again at a new dimension.

---

## 10. Controls

**Positive.** §3: all four readings of the two bases, each rebuilt from scratch,
each at both symmetric settings, recomputed from their own labels by the second
route and compared against the two receipts' own numbers. The computational
mutants that perturb either rebuild die on the way: `rot-lax` (one entry of a
declared rotation), `completion-lax` (one entry of the declared completion),
`field-lax` (the wrong reduction in the quartic field), `wingswap-lax` (a wing
exchange that moves the systems only), `prep-lax` (two different preparation
legs) and `base1-angle` (the first base read at an asymmetric setting).

**Negative, with teeth, one per candidate.** The violator is *constructed*, not
sampled: it is the lexicographically first single-coordinate edit of the
realized connection, in the declared basis order, that fails the candidate's
predicate. No seed enters anywhere in this unit.

| candidate | declared violator | its profile | breaks the profile |
|---|---|---|---|
| C1 source-split | `SQ_FULL_1 := W` | 80 / 88 / 100 / 96 | yes |
| C2a equivariance, rule-preserving | *none exists — the subset is the whole space* | — | — |
| C2b equivariance, full | `SQ_FULL_1 := W` | 80 / 88 / 100 / 96 | yes |
| C2c equivariance up to naming | `SQ_FULL_1 := W` | 80 / 88 / 100 / 96 | yes |
| C3 admission pattern | `SQ_FULL_1 := WD` | 90 / 86 / 90 / 98 | yes |
| C4 clause-split, named | `SQ_FULL_1 := W` | 80 / 88 / 100 / 96 | yes |
| C5 clause-split, naming-closed | `SQ_FULL_1 := W` | 80 / 88 / 100 / 96 | yes |
| C6 common preparation leg | `SQ_FULL_1 := W` | 80 / 88 / 100 / 96 | yes |
| C7 commuting local legs | `CANON := W` | 80 / 88 / 96 / 100 | yes |
| C8 intertwined local legs | `SQ_REAL_2 := W` | 80 / 88 / 96 / 100 | yes |
| C9 unintertwined preparation leg | `SQ_REAL_1 := 1` | 172 / 192 / 0 / 0 | yes |
| C10 group of order four | `SQ_REAL_1 := 1` | 172 / 192 / 0 / 0 | yes |

Every declared violator breaks the profile. **That is not the same as the
converse**, and the exhaustive violator census of §5 is what settles the
converse: for C4 and C5 it fails — 95 and 90 connections respectively violate
the candidate and carry the profile anyway. The `violator-lax` mutant, which
offers the realized connection itself as a violator, dies at the gate.

**One candidate has no violator at all**, and it is named rather than skipped:
C2a's subset is the whole space, so nothing violates it — not an omission but an
impossibility. The machinery is nevertheless exercised, as §5 records: C2b and
C2c run the identical induced-action path and both return False.

---

## 11. The gauge layer and the flip-tests

**The gauge sweep, complete.** The declared gauge group assigns one Klein-group
element to each of the eight nodes; fixing the base node as a declared section
leaves $4^7 = \mathbf{16{,}384}$ elements, and every one is swept. For each,
every one of the 364 walks' holonomies is **rebuilt from the link variables**,
and the class-count profile recomputed.

| measured | value |
|---|---|
| gauge elements swept | **16,384** |
| profiles differing from the realized one | **0** |
| fresh evaluations | **442,368** |
| cache hits | **0** |
| refused lookups into a cache that held the answer | **442,368** |
| primed entries **read back and measured equal to what was stored** | **27 / 27** |
| mis-conventioned control (a head-only action) that moves the profile | **12,288** of 16,384 |

Two things are separated here. With the correct convention the invariance is
**analytically forced** — a closed walk enters and leaves each node the same
number of times, so a node-valued gauge telescopes away — and that clause is
reported as a **disclosure**, not as evidence. What is measured, and is
must-pass, is that the instrument implements that convention: the
mis-conventioned control moves the profile at three quarters of the group, and
the `gauge-head` mutant, which makes the sweep itself head-only, dies there.

**The self-test evaluates fresh, against a cache that works.** A value cache is
primed before the sweep with the very keys the sweep will request — keyed by the
walk, which is exactly how a naive memoiser would key a holonomy and exactly the
bug the fresh-evaluation rule exists to catch. The primed entries are **read
back and compared with what was stored**, the sweep is measured to request keys
that are present **442,368** times, and its hit count is nevertheless **zero**.
A zero-hit count over zero lookups would be vacuous; this one is 442,368
refusals to read a cache that had an answer. The `memo-lax` mutant, which lets
the sweep read it, dies; so does `cache-garbage`, which primes the cache with a
wrong value and is caught by the read-back. This cache is a prop the self-test
erects for the self-test: the instrument memoises nothing else, and the claim is
only that the sweep refuses a cache that would have answered.

**The spanning-tree flip-test is a disclosure, and the cell-completeness gate is
not.** The entire census is recomputed on a **second** declared tree — the six
legs together with `REAL@0` instead of `FULL@0`. Its three census numbers agree
with the first tree's; but a second spanning tree induces an **invertible change
of cycle coordinates**, and all three numbers are invariant under any such
change, so that clause could not have come out otherwise once the cycle-rank
gate has passed. It is reported as a disclosure with that argument, and the
genuinely independent census is the ordered-walk-product route of §4. What *is*
must-pass here is completeness and equality of the compared cells: **all twelve**
candidate subsets are recomputed in the second tree's own coordinates — the
automorphism actions included, which the comparison previously dropped — the two
cell sets are gated equal, the cell count is gated at twelve, and the
`cells-lax` mutant, which drops the compared cells, dies at it.

**The direction flip-test** is a disclosure: every element of the group is an
involution, so a reversed walk carries the same holonomy for any input, and the
measurement (0 of 364 walks differ) could not have come out otherwise. What
carries instrument integrity in that direction is the raw-matrix comparator of
§3, where reversal is a transpose and the `reverse-lax` mutant dies.

**The steering residual, in its sharp form.** The freeze gate protects the
declaration against the profiles; it does not protect the **choice of the six
declared cycles**, which was made after the realized labels were computed. That
choice is what C4 and C5 assert, and the measurement says how much:
**3,906 of the 4,096** connections — every one whose labels generate the group —
admit the shape $(\mathbf 1,\mathbf 1,d,\mathbf 1,\mathbf 1,w)$ on *some* basis
of the cycle space, and the instrument exhibits and verifies such a basis for
every one of them. The remaining 190 cannot, because a connection whose image is
smaller than the group cannot take two distinct non-identity values on any
basis. So what protects C4 and C5 is not the freeze: it is the correspondence of
§2 between the six cycles and five facts both terminal papers state without
reference to holonomy, together with the derivation of §7 — and those are where
a reader should press.

---

## 12. The verdict

> **`XBA-SHARED-STRUCTURE-IDENTIFIED`** — the property named
> **COMPLETION-FORCED-SPLIT** — at the common gauge-fixed graph, at the two
> symmetric settings, over the declared Klein-four connection space, per
> coordinate.

The verdict string is derived inside a gate from the measured lists — a forcing
candidate both bases satisfy exists, so the positive outcome is the one the
counts require — and checked against an independently written truth table over
the same two booleans; the `verdict-swap` mutant, which exchanges the
derivation's two branches, dies there, and the `verdict-lax` waiver, which
overwrites the string, dies on the vocabulary clause.

Stated once, plainly: the two bases' holonomy class-count profiles agree because
their connections are **one point** of the 4,096, and that point is forced,
cycle by cycle, by four clauses about the species — a preparation leg common to
the two frames, commuting local legs, a wing exchange that intertwines the local
legs at a symmetric setting, and a wing exchange that does not intertwine the
preparation leg — **together with one clause about the declared completion, that
the defect those four leave behind is an involution**, and together with the
admission table's datum that the two rules draw different permutations where
they meet. The agreement is not a one-in-forty coincidence, because the two
bases are not two independent draws from the 4,096.

What the frozen review called "the same gauge class of connection on the same
graph" is confirmed, and the connection half of it is given its mechanism.

The pin's own three candidates are answered as measured: C1 **PARTIAL** with a
shrink of 97.5 and a residual of 6 in 42; C2 **vacuous** in its rule-preserving
form and **refuted at membership** in the other two; C3 **necessary but not
sufficient**, cutting 4,096 to 1,728. On those three alone the honest outcome
would be `XBA-PARTIAL`; the positive outcome is entered on the worker candidates
C4 and C5, whose content is not the subset statement but the derivation of §7
and the law of §8, and that is recorded in the deviations rather than argued
away.

---

## 13. Scope and non-claims

1. **No claim about nature.** Every result is a statement about declared finite
   models, a declared graph, a declared connection space and declared finite
   search scopes.
2. **Two things are inputs, not results.** The two bases' 24-cell tables agree,
   which is what makes the graph common. And both bases' completions have a
   non-trivial involutive defect — 864 of the declared family's 40,320 — which
   is what puts them in one connection space; they reach that condition by
   unrelated routes, base 1 through the singlet completion whose defect is a
   qubit-only wing swap, base G through a transposition drawn from 12 of 36.
   This unit measures both agreements and uses them; it explains neither. The
   generality unit registered two things OPEN; this unit closes the class-count
   one and leaves the admission-table one exactly where it was, and names a
   second open of the same kind that was not previously stated.
3. **The connection space is the Klein-four one, and that is a condition on the
   instance.** Both bases realize a connection inside it — measured, all 13
   labels, at all four readings, with the four named elements gated closed.
   Instances whose defect has another order are outside this arena; §9.3 builds
   one and measures what goes wrong, and the generality unit's own census
   measures defects of order 3, 4, 5, 6, 7 and 15 elsewhere in the family.
4. **Forcing at subset size one is trivial as a subset statement**, and this
   paper does not trade on it. What carries the result is the derivation of §7,
   the law of §8, the clause chain of §6, and the instances of §9 — of which the
   third species is the one that shares no flesh with either base.
5. **The candidate declaration is frozen before any census profile, not before
   the realized labels.** The realized class counts are an anchored input; the
   two bases' gauge-fixed labels were computed before the declaration, because
   membership needs them. The residual — that a worker candidate could be framed
   with the realized labels in view — is measured in §11 in its sharp form and
   recorded in the deviations, not argued away.
6. **Sufficiency is not necessity.** Ninety connections outside C5 carry the
   profile. The clauses explain this agreement; they do not characterise the
   profile.
7. **The path space is bounded** at $L_{\max}=8$, and every count is a count at
   that bound.
8. **Every claim is per coordinate**: the graph is the one the admission table
   draws at a **symmetric** setting, and nothing here is claimed at the four
   asymmetric settings, whose graphs have nine links and a trivial holonomy
   group.
9. **The completion census is exhaustive at dimension three only.** The 40,320
   figures are an exhaustive sweep of the declared family at the qutrit carrier.
   At the dimension-4 carrier only the 120-member single-transposition
   sub-family is swept, and the scope is printed with the number.
10. **Nothing is claimed about locality, topology, causality, spacetime, fields,
    QFT or gravity.** "Connection", "holonomy", "curvature" and "gauge" are
    operational vocabulary for a declared finite graph.
11. **The two curvature sources remain declaration-side**, as the generality
    unit measured. This unit adds that their *values* are forced by the declared
    **completion** — through its commutator with the declared exchange — and
    that the species clauses are what make the connection depend on nothing
    else. The generality unit's terminal species has four clauses; E5 is not one
    of them, and the exchange-equivariant control is species-compliant with a
    different profile.

---

## 14. The receipt

`v13/code/xba_crossbase_exact.py` → `xba_crossbase_output.txt` +
`xba_crossbase_receipt.json`.

- **Anchors: 38, exit-1-only.** Four hash-pin the frozen sources — the XBA pin,
  the two committed terminal receipts, and the frozen operator review. Seven
  pin this unit's rebuild to the **frozen review's own construction numbers**,
  read out of the review's table and the generality receipt rather than typed.
  Ten anchor the rebuilt arena against the two committed receipts. Seven anchor
  the two rebuilt bases against the printed declarations of the papers they come
  from: two rotation matrices, the $9\times9$ completion entry by entry, and
  four fixed-point counts. Two anchor the completion-family census — the 864
  involutive members and the 96 equivariant ones — against the generality
  receipt's own table, recomputed here from the permutation algebra alone. The
  remaining eight anchor the census.
- **Gates:** 40, of which 34 are must-pass and 6 are declared disclosures. The
  disclosures are the four analytically-forced clauses — gauge invariance under
  a correct convention, the direction flip-test, the spanning-tree flip-test's
  census numbers, and the freeze-order predicate, each printed with the argument
  that forces it — together with the candidate declaration itself and the
  candidate results table, whose teeth are the freeze gate before them and the
  consistency gate after them.
- **The freeze.** The census-profile counter is measured **zero** at the
  candidate declaration point. The gate order is printed as a disclosure with
  its forcing argument, since gates are appended in execution order and the four
  named calls textually follow the declaration.
- **Exhaustive everywhere.** All 4,096 connections by both routes; all 16,384
  gauge elements; all 364 walks by both routes on both bases and on all four
  further instances; every candidate's subset and its complement; the whole
  40,320-member completion family at dimension three; all 36 and all 120
  single-transposition sub-families. No sampling is used anywhere in this unit
  and there is no `[SAMP]` disclosure to make.
- **Independent comparators.** The gauge-fixed route is audited against the raw
  matrix product along every walk, which shares no component with it; the census
  is audited against the ordered walk product over the thirteen reconstructed
  labels, which uses no cycle coordinate; and the commutator law is audited
  against a defect built from the completion alone, which uses neither $P$ nor
  $u$.
- **Mutants: 44**, each run to completion, **44 of 44 died** — each measured to
  exit 1 and to falsify at least one gate or anchor **by its full name**. **The
  set of must-pass gates that no mutant falsifies is EMPTY**, at denominator 33
  (the thirty-fourth must-pass gate is the census's own, which does not exist
  inside a mutant run and cannot be falsified by this mechanism at all). **All
  33 are falsified by a mutant that perturbs a computation**, so the set of
  must-pass gates carried only by a waiver is EMPTY as well: the four the
  previous delivery carried have been
  re-founded (the positive control now compares against the receipts' own
  numbers by an independent route; the verdict is derived inside its gate) or
  reclassified as the disclosures they were (the flip-test census, the freeze
  order). One waiver remains declared — `verdict-lax`, which overwrites the
  derived verdict with an out-of-vocabulary string — and it falsifies a gate
  that a computation mutant also falsifies. Both denominators are printed.
- **The suite covers** the four hash pins and the reused numbers
  (`anchor-pin-hash`, `anchor-review-hash`, `anchor-nt-hash`, `anchor-gen-hash`,
  `anchor-classcounts`, `anchor-census`), the graph (`graph-drop-real2`,
  `graph-add-full2`, `admission-lax`), the path space (`reduce-lax`,
  `lmax-lax`), the cycle bookkeeping (`tree-lax`, `cycle-lax`, `basis-lax`),
  both rebuilds (`field-lax`, `rot-lax`, `completion-lax`, `wingswap-lax`,
  `prep-lax`, `base1-angle`), the gauge-free comparator (`direct-order`,
  `reverse-lax`), the second census route (`route2-lax`), the freeze
  (`freeze-lax`), the candidates (`candidate-lax`), the cell completeness
  (`cells-lax`), the controls (`violator-lax`, `control-completion`), the gauge
  layer (`gauge-head`, `memo-lax`, `cache-garbage`), the derivation
  (`species-lax`, `involutive-lax`), the commutator law (`defect-lax`) and its
  corollaries (`group-lax`), the further instances (`counter-lax`, `dim4-lax`),
  the inertness sweep (`inert-lax`), the completion census (`family-lax`), the
  steering residual (`residual-lax`), the verdict (`verdict-swap`,
  `verdict-lax`), and exactness and gate hygiene (`float-lax`, `exempt-lax`).
- **No gate predicate references mutant identity.** An AST sweep finds every
  `gate(...)` and `anchor(...)` call site, walks its argument expressions to any
  depth, and measures the number reaching the mutant flag — read as **either**
  `MUTANT` **or** `M_ON` — to be **zero**; the count of `!=`, `not in` and
  `is not` comparisons against the flag anywhere in the source is gated at
  **zero** as well, and the `exempt-lax` mutant, which registers one, dies
  there. The sweep also lists every assignment to a gate's own predicate
  variable made under a test of the flag, with the mutant that guards it; each
  such guard is gated to be a **declared** mutant, and the census measures that
  every one of those mutants dies — which is what "in the falsifying direction"
  means as a measurement.
- **Fail-closed.** Two prerequisites refuse every downstream measurement rather
  than crashing: if the declared cycle basis is measured not to be a basis, and
  if no base yields a readable connection. Both paths are exercised — by the
  `basis-lax` and `prep-lax` mutants respectively — and both exit 1 with the
  failed gate named.
- **Exactness:** `fractions.Fraction` and the quartic field $\mathbb{Q}(\cos\pi/8)$
  as reduced rational 4-tuples, where tuple equality is field equality. An AST
  sweep finds **no** float literal and **no** call to `float`. No tolerance
  exists anywhere in the instrument.
- **Determinism:** no wall-clock value enters the receipt or the rendered
  output; the mutant census runs its members in parallel and reports them in
  their declared order; two delivery-mode runs were executed and their artifacts
  are byte-identical.

---

## Appendix: deviations

**D1 — the declaration is frozen before any census profile, not before the
realized labels.** The pin asks for the candidate family to be frozen "before
any profile is computed", and that is the gate: the census-profile counter is
measured zero at the declaration point. The realized class counts, however, are
an **anchored input** read from the two terminal receipts, and the two bases'
gauge-fixed labels are computed earlier, because candidate *membership* is a
statement about them. So a reader is entitled to ask whether the worker
candidates C4–C9 were framed with the answer in view. The sharp form of that
residual is measured rather than deflected: on a freely chosen basis of the
cycle space, **3,906 of the 4,096** connections take the C5 shape, so the
declared basis is the whole of what C4 and C5 assert and the freeze gate does
not protect it. What protects it is the one-to-one correspondence of §2 between
the six cycles and five facts both terminal papers state without reference to
holonomy, together with the derivation of §7 and the law of §8 — and the
instances of §9, of which one is of a different species. The residual is real
and is recorded here rather than argued away.

**D2 — C4's forcing is trivial as a subset statement, and the pin's vocabulary
cannot grade what carries the content.** A predicate whose subset has one member
forces anything that member has. The paper says so at the claim (§5, §12) and
rests the result on the derivation, the law, the chain and the instances. On the
pin's own three candidates the honest outcome is `XBA-PARTIAL`; the positive
outcome is entered on C4 and C5, whose content as *properties of connections* is
the answer written as a predicate. The object that carries this unit's content —
the implication *five clauses ⟹ that orbit* — is not a property of connections
at all, and the pin's outcome vocabulary did not anticipate it. The verdict is
stated at C5, the naming-closed form with six members, and this deviation
records that the vocabulary is being satisfied at its letter.

**D3 — the first base's model is re-implemented, not imported.** Its committed
model lives in the paper-1 code bundle; this unit rebuilds it from the printed
declaration — the singlet completion, the rank-one projectors at the declared
half-angles, the pointer 3-cycle, the index map — in its own arithmetic, and
anchors the rebuild against the transport receipt's own fixed-point counts for
the wing exchange (6 of 36) and for the defect (18 of 36). Base G is rebuilt the
same way, against the generality paper's printed rotations and its $9\times9$
completion entry by entry. Neither instrument is imported and neither model file
is read.

**D4 — an involutive defect does not need system dimension three, and this
unit's own first base is the witness.** Base 1 has qubit wings — system
dimension **two** — and its defect is measured involutive, 18 of 36
configurations fixed. Any claim that an involutive defect *requires* a system
dimension of at least three is therefore withdrawn: it can hold at most within
the single-transposition sub-family of completions, and base 1's completion is
the singlet one, which is not a single transposition. The third instance of
§9.1 shares base G's carrier shape for convenience only, and the work a
genuinely different carrier would do is done instead by the third species of
§9.4, at dimension four.

**D5 — the instances of §9 are tested at the level of the labels, on a declared
graph.** Their admission tables are not recomputed: the graph is the common one
this unit's arena declares, and what is measured on each instance is the
connection the clauses predict on that graph, by the raw matrix product.
Reproducing the four-clause admissibility predicate would be a re-implementation
of two terminal instruments, which the pin does not ask for and which this unit
does not attempt. The scope is stated at the claim.

**D6 — the equivariant control is a control on E4, not a rebuild.** The bare
Householder instance is measured on the same declared graph for the same reason.
It satisfies every clause of the generality unit's declared species — that unit
measures it so, and this paper does not say otherwise. The generality unit's own
flip-test, which does rebuild that base's admission table, measures that its
full-leg rule then admits two permutations at the symmetric settings and the
links are refused; nothing here contradicts that, and nothing here rests on it.

**D7 — one candidate is measured vacuous and one has no violator.** C2a is
satisfied by all 4,096 connections, because the rule-preserving automorphism
group acts trivially on the cycle space — the frame swap fixes the seven
identification links and exchanges the six leg links in matching pairs, so every
declared cycle's edge set is preserved. It is kept in the table with its
measured size rather than dropped, and its missing negative control is named as
the consequence it is; the machinery it would exercise is exercised by C2b and
C2c through the same code path.

**D8 — the profile is compared in two ways, and both are printed.** The
class-count profile as a **multiset** is what the frozen review counts (96 of
4,096), and it is naming-independent. The profile **element by element** —
$\mathbf 1$ to 82, $W$ to 86, $D$ to 90, $WD$ to 106 — is the stronger agreement
the two terminal receipts actually record, since each names its own group
elements, and only 16 of the 4,096 connections carry it. Both are measured for
every candidate and both are in the receipt.

**D9 — four measurements are analytically forced and are reported as
disclosures, with their arguments printed.** The gauge invariance under a
correct node-valued action; the direction flip-test; the spanning-tree
flip-test's three census numbers, which are invariant under any invertible
change of cycle coordinates and so cannot fail once the cycle-rank gate has
passed; and the freeze-order predicate, which is forced by the order in which
the gate calls appear in the source. Their must-pass counterparts are,
respectively, the mis-conventioned control at 12,288 of 16,384, the raw-matrix
comparator, the cell-completeness gate over all twelve candidates, and the
census-profile counter. The C10 necessity row of §5 and the survivor-count
column of §6 are forced in the same way and are marked at the claim.

**D10 — the earlier delivery's derivation was a typed constant, and this one is
not.** The tuple $(\mathbf 1,\mathbf 1,D,\mathbf 1,\mathbf 1,W)$ was previously
returned as a literal with the algebra in a docstring — the engraved lesson of
"counts computed, never typed", landing on this unit's own central object. It is
replaced by an evaluation in the group the clauses present, which is why the
fifth premise could not stay unnamed: the computation returns $D^{-1}$ without
it. This deviation is recorded by name because the failure was this unit's.

**D11 — the third instance's prediction risked one bit, and that is now
measured.** Two of its three advertised variations — the preparation vector and
the measurement rotation — are measured incapable of reaching the connection,
and the third selects one of three classes of completion. The instance remains a
real consistency check, and it is claimed at that strength; the risk that the
delivered version implied is carried instead by the third species of §9.4 and by
the counter-instance of §9.3.

**D12 — no Lean.** As the pin states.
