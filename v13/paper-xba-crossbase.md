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
point is forced, cycle by cycle, by four clauses both bases satisfy for reasons
that have nothing to do with holonomy:

- the **preparation leg is common to the two frames** — the two frames are two
  orders of the same two local events, so the full-leg square around the
  preparation leg closes;
- the **two local legs commute** — so the canonical loop closes;
- at a symmetric setting the **wing exchange intertwines both local legs** — so
  the two realized-rule squares around them close;
- the wing exchange **does not intertwine the preparation leg** — so the one
  remaining realized-rule square carries the defect $D$.

Together with the admission table's own datum — that at $t=0$ the two gluing
rules draw *different* permutations, the identity and the wing exchange — those
four clauses cut the space **4,096 → 3,072 → 768 → 192 → 12 → 6**, and the six
survivors are one relabelling orbit, all with the profile 82 / 86 / 90 / 106.
With the group elements named by what they do on each base — $\mathbf 1$, the
wing exchange $W$, the preparation defect $D$, and $WD$ — the surviving point is
unique and the profile is forced element by element.

Three things carry that beyond a restatement. The connection is **derived**
symbolically from the four clauses and the derivation matches both rebuilt bases
cycle for cycle. A **third instance** was constructed for the purpose — a fresh
integer quaternion, a different preparation vector of Schmidt rank two, a
different completion transposition — and its class counts were measured
afterwards: **82 / 86 / 90 / 106**. And an **exchange-equivariant** control, the
bare Householder completion, has $D = \mathbf 1$ and breaks the profile at once.

The pin's own three candidates are measured and do not force. The source-split
property shrinks the space to **42** and leaves **6** of those reproducing the
profile. Equivariance under the graph's automorphism group is measured
**vacuous** in its rule-preserving form (that group acts trivially on the cycle
space) and **fails membership** in its full form: the two gluing rules are not
interchangeable. The admission pattern shrinks the space to **1,728** and is
measured **necessary** — every one of the 96 profile-reproducing connections
satisfies it — but not sufficient.

What is *not* explained is stated as plainly: the two bases' 24-cell admission
tables agree, and that agreement — which is what makes the graph common in the
first place — is an input here, not a result.

**Unit verdict:**
`XBA-SHARED-STRUCTURE-IDENTIFIED`, the property named **SPECIES-FORCED-SPLIT**,
at the common gauge-fixed graph, at the two symmetric settings, over the
declared Klein-four connection space, per coordinate.

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

This unit asks what forces it, and answers with a property, a derivation and a
prediction.

### 1.0 The declared arena

| coordinate | this unit's declaration |
|---|---|
| **boundary** | the common gauge-fixed graph at a **symmetric** setting: 8 nodes, 13 links, cycle rank 6 |
| **family** | the $4^6 = 4{,}096$ Klein-four connections on that graph, gauge classes |
| **law** | a connection's holonomy on a closed walk, read as the ordered product of its labels |
| **state** | the 364 reduced closed walks based at $F_1@t{=}0$, bounded at $L_{\max}=8$ |
| **arena action** | the node-valued gauge group ($4^7$ after a declared section) and the graph's automorphism group |
| **provenance** | two committed terminal receipts and one frozen review, hash-pinned; every reused number read from them |

Nothing outside this arena is decided. In particular the four asymmetric
settings, whose graphs have nine links and a trivial holonomy group, are not in
it.

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
gauge group (§9).

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
statement about the connection and not about the bookkeeping — §9's
spanning-tree flip-test measures exactly that.

---

## 2. The candidate properties, declared

Everything in this section is a **declaration**, recorded before any profile of
any connection was computed. The instrument gates the freeze with the
profile-evaluation counter measured at **zero** at the declaration point, and a
separate gate measures that every constrained-subset gate sits strictly later in
the receipt's own gate order. The `freeze-lax` mutant, which evaluates one
profile first, dies at that gate.

The graph's automorphism group is computed first, because one candidate needs
it:

| measured | value |
|---|---|
| $\lvert\mathrm{Aut}\rvert$, rule-preserving (leg / full-leg / realized links preserved) | **2** |
| its distinct induced actions on the cycle space | **1** — the trivial one |
| $\lvert\mathrm{Aut}\rvert$, the bare multigraph | **16** |
| its distinct induced actions on the cycle space | **8** |

The rule-preserving group is generated by the frame swap, which carries every
link to itself and therefore acts trivially on cycles. That is recorded here,
before the candidate is measured, because it is what makes one form of the
equivariance candidate vacuous.

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
| **C4** species-split, named | worker | the six declared cycles take the values $(\mathbf 1, \mathbf 1, D, \mathbf 1, \mathbf 1, W)$ |
| **C5** species-split, naming-closed | worker | there are distinct non-identity $d, w$ with the six declared cycles at $(\mathbf 1, \mathbf 1, d, \mathbf 1, \mathbf 1, w)$ |
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

**Why C6–C9 are the clauses they are.** Each is the elementary cycle of one
species clause, in the correspondence §7 derives:

| clause | measured on both bases | forces |
|---|---|---|
| **E0** the two rules draw different maps at $t=0$ | the admission table | `BIGON_0` $= W$ |
| **E1** the preparation leg is common to the two frames | structural, and gated | `SQ_FULL_1` $= \mathbf 1$ |
| **E2** the two local legs commute | measured at all nine declared pairs by both units | `CANON` $= \mathbf 1$ |
| **E3** at a symmetric setting the wing exchange intertwines both local legs | measured by both units | `SQ_REAL_2` = `SQ_REAL_3` $= \mathbf 1$ |
| **E4** the wing exchange does not intertwine the preparation leg | measured by both units | `SQ_REAL_1` $= D \neq \mathbf 1, W$ |

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
| $D$ is an involution | yes | yes |
| the preparation leg is common to the two frames | yes | yes |
| the two local legs commute | yes | yes |
| the wing exchange intertwines the local legs | yes | yes |
| the wing exchange intertwines the preparation leg | **no** | **no** |
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
(the four elements are gated distinct), and it is the same one both terminal
receipts use when they name their class counts. Everything element-wise in this
paper is at that identification; everything multiset-wise is independent of it.

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

---

## 4. The connection space, enumerated

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
| **C4** species-split, named | yes | **1** | 4096$\times$ | 1 | **yes** | **yes** |
| **C5** species-split, naming-closed | yes | **6** | 682.7$\times$ | 6 | **yes** | no |
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
connection.

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
is measured in §6 and §7: the clauses of C4 and C5 are not read off the answer
but are the elementary cycles of four species facts both bases satisfy, the
connection is *derived* from those facts, and a third instance built to satisfy
them reproduces the profile.

**Sufficiency and necessity, separated.** For each candidate the instrument
counts, exhaustively, the connections that violate it and reproduce the profile
anyway:

| candidate | violators reproducing the profile anyway | reading |
|---|---|---|
| C3 admission pattern | **0** of 2,368 | **necessary**, not sufficient |
| C10 group of order four | **0** of 190 | **necessary**, not sufficient |
| C1 source-split | 90 of 4,054 | neither |
| C5 species-split, naming-closed | **90** of 4,090 | **sufficient**, not necessary |
| C4 species-split, named | 95 of 4,095 | **sufficient**, not necessary |
| C6 / C7 | 72 of 3,072 | neither |
| C8 intertwined local legs | 72 of 3,840 | neither |
| C9 unintertwined preparation leg | 48 of 1,792 | neither |

Ninety connections outside C5 carry the profile. The species clauses are a
sufficient explanation of *this* agreement, not a characterisation of the
profile.

---

## 6. Where the 4,096 collapses

The five clauses are added in their declared order, each a species or admission
fact, and the survivors counted:

| clause added | survivors | of which reproduce the profile |
|---|---|---|
| — | 4,096 | 96 |
| **E0** the two rules draw different maps at $t=0$ | **3,072** | 96 |
| **E1** the preparation leg is common to the two frames | **768** | 24 |
| **E2** the two local legs commute | **192** | 12 |
| **E3** the wing exchange intertwines both local legs | **12** | 6 |
| **E4** the wing exchange does not intertwine the preparation leg | **6** | **6** |

The last row is the result: after the four species clauses and the admission
table's own datum, every survivor carries 82 / 86 / 90 / 106. The heavy cut is
E3 — 192 to 12 — and it is the clause that says the wing exchange is a symmetry
of the *local* legs and of nothing else.

The table also shows that no proper prefix of the chain suffices: at E3 half the
survivors still miss the profile, and the ones that miss are exactly those where
the preparation square is flat or equal to the bigon, which is what E4 excludes.

---

## 7. The derivation, and a third instance built to test it

### 7.1 The derivation

Write $u$ for the preparation leg, $a$ and $b$ for the two local legs, $P$ for
the wing exchange, and $D = P u^{-1} P u$. With the spanning tree taken to be
the six leg links together with `FULL@0`, the transports are
$T_{F_1@t} = L_t\cdots L_1$ along frame 1 and likewise along frame 2, and the
label of a link $\ell : x \to y$ carrying $M$ is $T_y^{-1} M T_x$. Then, using
one clause each:

$$\texttt{SQ\_FULL\_1} = u^{-1}\,u = \mathbf 1 \quad (\mathbf{E1})$$

$$\texttt{CANON} = (a\,b\,u)^{-1}(b\,a\,u) = \mathbf 1 \quad (\mathbf{E2})$$

$$\texttt{SQ\_REAL\_1} = \bigl(u^{-1} P u\bigr)\cdot P = D \quad (\mathbf{E4})$$

$$\texttt{SQ\_REAL\_2} = \bigl((b u)^{-1} P (a u)\bigr)\cdot\bigl(u^{-1}Pu\bigr) = \mathbf 1 \quad (\mathbf{E1},\ \mathbf{E3})$$

$$\texttt{SQ\_REAL\_3} = \bigl((a b u)^{-1} P (b a u)\bigr)\cdot\bigl((b u)^{-1} P (a u)\bigr) = \mathbf 1 \quad (\mathbf{E2},\ \mathbf{E3})$$

$$\texttt{BIGON\_0} = \mathbf 1^{-1}\,P = W \quad (\mathbf{E0})$$

The two realized squares around the **local** legs use $P a P = b$, so that $P$
passes through those legs and cancels; the realized square around the
**preparation** leg is the same computation with $u$ in place of $a$, and there
$P$ cannot be passed through, so what is left over is precisely $D$. The
derived tuple is measured equal, entry by entry, to the tuple both rebuilt bases
realize. The `species-lax` mutant, which drops one clause from the derivation,
dies there.

### 7.2 A third instance

A derivation from clauses predicts. A **third** instance of the species was
built for the purpose, sharing no flesh with either base beyond the carrier
shape: its measurement rotation comes from the integer quaternion $(5,1,2,3)$,
which appears in neither unit; its preparation vector is exchange-invariant of
**Schmidt rank two** where base G's has rank three and base 1's is the
anti-invariant singlet; and its completion is a **different** transposition of
the system-pair labels. Its class counts were measured after it was built, by
the gauge-free route:

| measured on the third instance | value |
|---|---|
| defect fixed configurations | **45** of 81 |
| distinct holonomies over the 364 based closed walks | **4** |
| class counts | **82 / 86 / 90 / 106** |
| declared cycle basis | $(\mathbf 1, \mathbf 1, D, \mathbf 1, \mathbf 1, W)$ |

### 7.3 The control that breaks it

The same construction with an **exchange-equivariant** completion — the bare
Householder, with the transposition removed — satisfies every clause but E4: the
wing exchange then intertwines the preparation leg as well, and the defect is
the identity. Measured: $D$ fixes all **81** configurations, the 364 walks carry
only **2** distinct holonomies, and the class counts are **172 / 192** — not the
profile, and not even four classes. The `control-completion` mutant, which gives
that control a defect after all, dies at the gate.

---

## 8. Controls

**Positive.** All four readings of the two bases — each rebuilt from scratch,
each at both of its symmetric settings — reproduce 82 / 86 / 90 / 106 element by
element. The `control-lax` waiver dies on it, and so do the computational
mutants that perturb either rebuild: `rot-lax` (one entry of a declared rotation),
`completion-lax` (one entry of the declared completion), `field-lax` (the wrong
reduction in the quartic field), `wingswap-lax` (a wing exchange that moves the
systems only), `prep-lax` (two different preparation legs) and `base1-angle`
(the first base read at an asymmetric setting).

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
| C4 species-split, named | `SQ_FULL_1 := W` | 80 / 88 / 100 / 96 | yes |
| C5 species-split, naming-closed | `SQ_FULL_1 := W` | 80 / 88 / 100 / 96 | yes |
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
C2a's subset is the whole space, so nothing violates it. That is the same
measurement as its vacuity, reported twice because it is both a control gap and
a result.

---

## 9. The gauge layer and the flip-tests

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
| entries primed before the sweep, and returned on a second visit | **27 / 27** |
| mis-conventioned control (a head-only action) that moves the profile | **12,288** of 16,384 |

Two things are separated here. With the correct convention the invariance is
**analytically forced** — a closed walk enters and leaves each node the same
number of times, so a node-valued gauge telescopes away — and that clause is
reported as a **disclosure**, not as evidence. What is measured, and is
must-pass, is that the instrument implements that convention: the
mis-conventioned control moves the profile at three quarters of the group, and
the `gauge-head` mutant, which makes the sweep itself head-only, dies there.

**The self-test evaluates fresh, against a cache that works.** The value cache is
primed before the sweep with the very keys the sweep will request — keyed by the
walk, which is exactly how a naive memoiser would key a holonomy and exactly the
bug the fresh-evaluation rule exists to catch. The priming pass is measured to
return its stored values, the sweep is measured to request keys that are present
**442,368** times, and its hit count is nevertheless **zero**. A zero-hit count
over zero lookups would be vacuous; this one is 442,368 refusals to read a cache
that had an answer. The `memo-lax` mutant, which lets the sweep read it, dies.

**The spanning-tree flip-test, an independent comparator.** The bookkeeping split
this unit carries is which link goes into the spanning tree. The entire census
is recomputed on a **second** declared tree — the six legs together with
`REAL@0` instead of `FULL@0` — and its three census numbers are gated against
the **first tree's own computed values**, not against typed ones: 89 distinct
profiles, 96 hits, 3,906 order-4 connections, and every candidate's subset size
identical. The comparator is built from the second tree's own cycle coordinates
and shares no intermediate with the first. The `flip-lax` waiver dies on it.

**The direction flip-test** is a disclosure: every element of the group is an
involution, so a reversed walk carries the same holonomy for any input, and the
measurement (0 of 364 walks differ) could not have come out otherwise. What
carries instrument integrity in that direction is the raw-matrix comparator of
§3, where reversal is a transpose and the `reverse-lax` mutant dies.

---

## 10. The verdict

> **`XBA-SHARED-STRUCTURE-IDENTIFIED`** — the property named
> **SPECIES-FORCED-SPLIT** — at the common gauge-fixed graph, at the two
> symmetric settings, over the declared Klein-four connection space, per
> coordinate.

Stated once, plainly: the two bases' holonomy class-count profiles agree because
their connections are **one point** of the 4,096, and that point is forced,
cycle by cycle, by four clauses both bases satisfy — a preparation leg common to
the two frames, commuting local legs, a wing exchange that intertwines the local
legs at a symmetric setting, and a wing exchange that does not intertwine the
preparation leg — together with the admission table's datum that the two rules
draw different permutations where they meet. The agreement is not a one-in-forty
coincidence, because the two bases are not two independent draws from the 4,096.

What the frozen review called "the same gauge class of connection on the same
graph" is confirmed, and given its mechanism.

The pin's own three candidates are answered as measured: C1 **PARTIAL** with a
shrink of 97.5 and a residual of 6 in 42; C2 **vacuous** in its rule-preserving
form and **refuted at membership** in the other two; C3 **necessary but not
sufficient**, cutting 4,096 to 1,728.

---

## 11. Scope and non-claims

1. **No claim about nature.** Every result is a statement about declared finite
   models, a declared graph, a declared connection space and declared finite
   search scopes.
2. **The admission-table agreement is an input, not a result.** The two bases'
   24-cell tables agree, which is what makes the graph common; this unit
   measures that agreement and uses it, and does not explain it. The generality
   unit registered two things OPEN; this unit closes the class-count one and
   leaves the admission-table one exactly where it was.
3. **The connection space is the Klein-four one.** The pin declares it and both
   bases realize a connection inside it — measured, all 13 labels, at all four
   readings. Connections valued in a larger group are outside this arena
   entirely; the generality unit's own census measures that other completions
   give defects of order 3, 4, 5, 6, 7 and 15, and none of those lives in this
   4,096.
4. **Forcing at subset size one is trivial as a subset statement**, and this
   paper does not trade on it. What carries the result is the derivation of §7.1,
   the clause chain of §6, and the third instance of §7.2 whose profile was
   measured after it was built.
5. **The candidate declaration is frozen before any profile, not before the
   realized labels.** The freeze gate measures zero profiles computed at the
   declaration point; the two bases' gauge-fixed labels were computed before it,
   because membership needs them. The residual — that a worker candidate could be
   framed with the realized labels in view — is answered by the third instance
   and by the clause chain, not by the freeze alone, and is recorded in the
   deviations.
6. **Sufficiency is not necessity.** Ninety connections outside C5 carry the
   profile. The species clauses explain this agreement; they do not characterise
   the profile.
7. **The path space is bounded** at $L_{\max}=8$, and every count is a count at
   that bound.
8. **Every claim is per coordinate**: the graph is the one the admission table
   draws at a **symmetric** setting, and nothing here is claimed at the four
   asymmetric settings, whose graphs have nine links and a trivial holonomy
   group.
9. **Nothing is claimed about locality, topology, causality, spacetime, fields,
   QFT or gravity.** "Connection", "holonomy" and "gauge" are operational
   vocabulary for a declared finite graph.
10. **The two curvature sources remain declaration-side**, as the generality unit
    measured; this unit adds that their *values* are forced by declared species
    clauses too, which sharpens that reading rather than softening it.

---

## 12. The receipt

`v13/code/xba_crossbase_exact.py` → `xba_crossbase_output.txt` +
`xba_crossbase_receipt.json`.

- **Anchors: 36, exit-1-only.** Four hash-pin the frozen sources — the XBA pin,
  the two committed terminal receipts, and the frozen operator review. Seven
  pin this unit's rebuild to the **frozen review's own construction numbers**,
  read out of the review's table and the generality receipt rather than typed:
  the distinct-profile count, the hits and the space size, the order-4 count,
  the most common profile and its count, the gauge-fixing shape (tree, cotree,
  nodes reached), the zero links whose label leaves the group, and the
  **364-walk model agreement** — the count of walks where the combinatorial
  model disagrees with the direct holonomy. Ten anchor the rebuilt arena — the
  admission cells and their agreement, the link and identification-link counts,
  the walk counts at three scopes, the two sub-connection walk counts — against
  the two committed receipts. Seven anchor the two rebuilt bases against the
  printed declarations of the papers they come from: two rotation matrices, the
  $9\times9$ completion entry by entry, and four fixed-point counts. The
  remaining eight anchor the census.
- **Gates:** 28, of which 24 are must-pass and 4 are declared disclosures. The
  disclosures are the two analytically-forced clauses (gauge invariance under a
  correct convention, and the direction flip-test) and the two that record a
  declaration rather than a measurement (the candidate list itself, and the
  candidate results table, whose teeth are the freeze gate before them and the
  consistency gate after them).
- **The freeze.** The profile-evaluation counter is measured **zero** at the
  candidate declaration point, and a separate gate measures that every
  constrained-subset gate has a strictly later index in the receipt's own gate
  order.
- **Exhaustive everywhere.** All 4,096 connections; all 16,384 gauge elements;
  all 364 walks by both routes on both bases; every candidate's subset and its
  complement. No sampling is used anywhere in this unit and there is no `[SAMP]`
  disclosure to make.
- **Independent comparators.** The gauge-fixed route is audited against the raw
  matrix product along every walk, which shares no component with it; the whole
  census is audited against a second spanning tree, whose cycle coordinates are
  built independently.
- **Mutants:** 35, each run to completion, **35 of 35 died** — each measured to
  exit 1 and to falsify at least one named gate or anchor. **The set of must-pass
  gates that no mutant falsifies is EMPTY**, at denominator 23 (the
  twenty-fourth must-pass gate is the census's own, which does not exist inside
  a mutant run and cannot be falsified by this mechanism at all). All 23 are
  falsified by some mutant, **19** of them by a mutant that perturbs a
  computation, and the four carried only by a waiver are named: the positive
  control, the spanning-tree flip-test, the freeze order and the verdict
  vocabulary. Each mutant declares its kind: **30 perturb a computation and 5
  are waivers.** A waiver overwrites a gate's computed predicate after the fact,
  so what it measures is that the predicate carries the exit code — not that the
  gate would catch a computational defect, and the two are not claimed to be the
  same thing. Both denominators are printed.
- **The suite covers** the four hash pins and the reused numbers
  (`anchor-review-hash`, `anchor-nt-hash`, `anchor-gen-hash`,
  `anchor-classcounts`, `anchor-census`), the graph (`graph-drop-real2`,
  `graph-add-full2`, `admission-lax`), the path space (`reduce-lax`,
  `lmax-lax`), the cycle bookkeeping (`tree-lax`, `cycle-lax`, `basis-lax`),
  both rebuilds (`field-lax`, `rot-lax`, `completion-lax`, `wingswap-lax`,
  `prep-lax`, `base1-angle`), the gauge-free comparator (`direct-order`,
  `reverse-lax`), the freeze (`freeze-lax`), the candidates
  (`candidate-lax`), the controls (`violator-lax`, `control-completion`),
  the gauge layer (`gauge-head`, `memo-lax`), the derivation (`species-lax`),
  exactness and gate hygiene (`float-lax`, `exempt-lax`), and five waivers of
  the positive control, the chain consistency, the freeze order, the flip-test
  and the verdict vocabulary.
- **No gate predicate references mutant identity.** An AST sweep finds every
  `gate(...)` and `anchor(...)` call site, walks its argument expressions to any
  depth, and measures the number reaching the mutant flag to be **zero**; the
  count of `!=`, `not in` and `is not` comparisons against the mutant flag
  anywhere in the source is gated at **zero** as well, and the `exempt-lax`
  mutant, which registers one, dies there.
- **Fail-closed.** Two prerequisites refuse every downstream measurement rather
  than crashing: if the declared cycle basis is measured not to be a basis, and
  if no base yields a readable connection. Both paths are exercised — by the
  `basis-lax` and `base1-angle` mutants respectively — and both exit 1 with the
  failed gate named.
- **Exactness:** `fractions.Fraction` and the quartic field $\mathbb{Q}(\cos\pi/8)$
  as reduced rational 4-tuples, where tuple equality is field equality. An AST
  sweep finds **no** float literal and **no** call to `float`. No tolerance
  exists anywhere in the instrument.
- **Determinism:** no wall-clock value enters the receipt or the rendered
  output; two delivery-mode runs were executed and their artifacts are
  byte-identical.

---

## Appendix: deviations

**D1 — the declaration is frozen before any profile, not before the realized
labels.** The pin asks for the candidate family to be frozen "before any profile
is computed", and that is the gate: the profile-evaluation counter is measured
zero at the declaration point. The two bases' gauge-fixed labels, however, are
computed earlier, because candidate *membership* is a statement about them. So a
reader is entitled to ask whether the worker candidates C4–C9 were framed with
the answer in view. Three things are offered in place of a blindness the
instrument cannot provide: the clauses are in one-to-one correspondence with
species facts both terminal papers state and measure independently of any
holonomy; the clause chain of §6 measures each clause's cut separately; and the
third instance of §7.2 was constructed to satisfy the clauses and its profile
measured afterwards. The residual is real and is recorded here rather than
argued away.

**D2 — C4's forcing is trivial as a subset statement.** A predicate whose subset
has one member forces anything that member has. The paper says so at the claim
(§5, §11.4) and rests the result on the derivation, the chain and the
prediction. The naming-closed form C5, with six members, is the same statement
with the arbitrary naming of the group's elements quotiented out, and it is the
one the verdict is stated at.

**D3 — the first base's model is re-implemented, not imported.** Its committed
model lives in the paper-1 code bundle; this unit rebuilds it from the printed
declaration — the singlet completion, the rank-one projectors at the declared
half-angles, the pointer 3-cycle, the index map — in its own arithmetic, and
anchors the rebuild against the transport receipt's own fixed-point counts for
the wing exchange (6 of 36) and for the defect (18 of 36). Base G is rebuilt the
same way, against the generality paper's printed rotations and its $9\times9$
completion entry by entry. Neither instrument is imported and neither model file
is read.

**D4 — the third instance shares the carrier shape of base G.** A completion
$V = H\cdot Q$ over an exchange-invariant preparation has a defect of order 1 or
3 whenever the system dimension is two, so an involutive defect — the case in
which the group is the Klein four-group and the connection lives in the declared
4,096 — needs a system dimension of at least three, and a pointer dimension at
least as large for the record to be injective. The third instance therefore has
base G's carrier shape, and what differs is the measurement rotation (a fresh
integer quaternion), the preparation vector (Schmidt rank two against three) and
the completion (a different transposition). It is a third instance of the
species, not a third species, and it is scoped as one.

**D5 — the third instance is a test of the labels, on a declared graph.** Its
admission table is not recomputed: the graph is the common one this unit's arena
declares, and what is measured on the third instance is the connection the
species clauses predict on that graph. Reproducing the four-clause admissibility
predicate would be a re-implementation of two terminal instruments, which the
pin does not ask for and which this unit does not attempt. The scope is stated
at the claim.

**D6 — the equivariant control is a control on E4, not a rebuild.** The bare
Householder instance is measured on the same declared graph for the same reason.
The generality unit's own flip-test, which does rebuild that base's admission
table, measures that its full-leg rule then admits two permutations at the
symmetric settings and the links are refused; nothing here contradicts that, and
nothing here rests on it.

**D7 — one candidate is measured vacuous and one has no violator.** C2a is
satisfied by all 4,096 connections, because the rule-preserving automorphism
group acts trivially on the cycle space. It is kept in the table with its
measured size rather than dropped, and its missing negative control is named as
the consequence it is.

**D8 — the profile is compared in two ways, and both are printed.** The
class-count profile as a **multiset** is what the frozen review counts (96 of
4,096), and it is naming-independent. The profile **element by element** —
$\mathbf 1$ to 82, $W$ to 86, $D$ to 90, $WD$ to 106 — is the stronger agreement
the two terminal receipts actually record, since each names its own group
elements, and only 16 of the 4,096 connections carry it. Both are measured for
every candidate and both are in the receipt.

**D9 — the gauge invariance is forced and is reported as a disclosure.** With a
correct node-valued gauge action the class-count profile cannot move; the
must-pass content is that the instrument implements that action, evidenced by a
mis-conventioned control that moves the profile at 12,288 of 16,384 elements.

**D10 — no Lean.** As the pin states.
