# The Generality Check

## The Nomological-Transport Geometry on a Second Base, and the Census of Its Completions

**Status:** `GREEN-UNREVIEWED-REPAIRED`

**Date:** 2026-08-08

**Frozen pin:** `v13/note-gen-generality-pin.md`, commit `5e8bc58`
(sha `0da6205815a6`)

**Immutable base:** `fceb614` — the nomological-transport unit TERMINAL (v13 LOG
#211). No object of the first base's model is imported anywhere in this unit:
the only thing read from it is its committed receipt, which is hash-pinned, and
the numbers read out of it are anchored exit-1.

**Receipts:** `v13/code/gen_generality_exact.py` →
`gen_generality_output.txt`, `gen_generality_receipt.json`

**Lean:** NONE.

---

## Abstract

The transport unit earned a geometric structure — a four-element holonomy group
whose links are transports the base admits and whose loops leave the base's own
declared isomorphisms. It earned it on one committed base. The question this
unit was pinned to answer is whether that geometry is a property of the theory
or of that base.

A **second base** was built. Same structural species — two wings, a
preparation, commuting local legs on the wings, records at the final division
event — and genuinely different flesh at every coordinate: the system on each
wing is a **qutrit** rather than a qubit, so the carrier carries **81**
configurations rather than 36; every measurement has **three** outcomes rather
than two; the arithmetic is the **rationals**, every declared operator being
exactly orthogonal over $\mathbb{Q}$, where the first base needed a totally real
quartic field; the measurement bases are the columns of rational rotation
matrices built from integer quaternions in two different coordinate planes; and
the **preparation is different and its orthogonal completion is pinned
explicitly as data** — the full $9\times 9$ matrix is printed in §2 and the
constructor is anchored against it entry by entry. The base is declared in §2
before any transport quantity is computed, and the receipt's gate order is
gated as the proof.

The five pre-registered patterns were re-measured on it, each gated separately.
**All five hold at the declared completion.**

**P1.** A nontrivial based holonomy group exists: at the two symmetric settings
**1,896 of 2,820** closed paths carry a non-identity holonomy, while at the
other four settings **0 of 56** do — both halves in the gate's own predicate;
and the negative control — a deliberately twisted comparator — is measured
non-identity at every one of the six settings, so the flat readings are not
vacuous.

**P2.** Counted as **permutation tuples** and never as labels, the based
holonomy group at the declared base point has order **4**, is measured already
**closed** at the declared length bound, is abelian with every element of order
dividing two, and is therefore the Klein four-group — **at the declared
completion**, which §8 measures to be the parameter that selects the
isomorphism type.

**P3.** Both curvature sources are exhibited. Identification multiplicity: six
coordinates carry two different admitted maps. And, isolated by running the
single-rule sub-connections separately, the **completion's non-equivariance
defect** $D = P_W U_{\text{prep}}^{-1} P_W U_{\text{prep}}$ already makes the
realized-rule sub-connection non-flat — **8 of its 18** closed paths — at a
connection every coordinate of which has multiplicity exactly one.
Multiplicity is sufficient and is measured not necessary, on this base as on
the first.

**P4.** That defect is measured to **be an element** of the group, at both
settings whose group is nontrivial and at none of the four where it is trivial.

**P5.** **Two of the four** elements lie outside the declared 162-element
relabelling scope, outside its declared 216-element extension, and outside both
admitted sets. The connection is **not principal** for this base's own
isomorphisms either.

**The completion is the parameter that decides, and it is swept exhaustively.**
The defect obeys an exact law, derived and gated two ways:
$D = (\Sigma V^{\mathsf T}\Sigma V)\otimes I_9$ for any orthogonal completion
$V$, which for $V = H\cdot Q$ with an exchange-invariant preparation vector
cancels to $(\Sigma Q^{\mathsf T}\Sigma Q)\otimes I_9$ — the Householder
cancels identically and **the defect does not depend on the preparation vector
at all**. Both curvature sources on this base are therefore declaration-side.
Over the whole declared completion family — $8! = 40{,}320$ members, every one
swept — **40,224 bear geometry** and the **96** that do not are exactly the
exchange-equivariant locus: existence is **generic**, and the completion the
flip-test rebuilds is a member of the rare exceptional class. The **isomorphism
type**, by contrast, is completion-selected: the family is dihedral,
$\langle W, D \mid W^2 = D^n = 1,\ WDW = D^{-1}\rangle$ with $n$ the defect's
order, and the predicted group orders **1, 4, 6, 8, 10, 12, 14, 30** are all
exhibited by full rebuild. Inside the pinned completion's own declared form — a
single basis transposition, 28 members, all rebuilt — **12** give the Klein
four-group, **12** give the **non-abelian** group of order six and **4** are
flat.

What recurs across the two bases is therefore the **presentation** and the
**existence** of a nontrivial group with two sources and a scope-escaping
generator. The group is a function of the base's declared data, completion
included: the geometry is a property of the species **together with a
geometry-bearing completion**, and the completions that bear none are the
exchange-equivariant ones.

**Unit verdict:** `GEN-STRUCTURE-REPRODUCES-AT-DECLARED-COMPLETION`, at the
committed finite scope, at the declared admission scope, at the declared
completion, per coordinate — with the computed differences between the two
bases reported beside it and folded into nothing.

---

## 1. The question, and what it is asked of

The transport unit measured, on one committed base, that lawful transport
between declared contexts is path-dependent; that the group the loops generate
is the Klein four-group; that it has two sources, one of them a failure to
intertwine under the wing exchange; and that half of it lies outside the base's
own declared permutation scopes.

Every one of those readings is a reading on **one base**. A geometry that is a
property of the theory should survive a change of flesh; a geometry that is an
artifact of one committed fixture should not. This unit constructs a second
base and re-measures, with the five patterns pre-registered and gated
separately, and with the honest negative — no nontrivial holonomy at all —
pre-registered as one of the four admissible outcomes.

Two constraints shape what "a second base" may mean, and both are declarations
of this unit.

**It must be of the same species.** Two wings; a preparation common to both
frames; local legs on the wings that commute; records at the final division
event. Without those, "re-measuring the same patterns" is a category error
rather than a generality check. Every clause of the species is *measured* on
the constructed operators in §2 and gated, not asserted.

**Its flesh must be genuinely different.** Not a re-parameterisation: a
different system dimension, a different number of outcomes, a different
arithmetic, a different preparation. §9 tabulates the two bases coordinate by
coordinate and gates that they differ where they must.

The species does not fix the preparation's orthogonal **completion**, and
nothing else does either. The completion is therefore declared as data, and §8
measures what it decides — exhaustively, over the whole family it belongs to.

---

## 2. Base G, declared as data

Everything in this section is a **declaration**, recorded before any transport
quantity is evaluated. The instrument records the freeze as its first gate with
the transport-datum evaluation counter measured at zero, and a separate gate
measures that every base-declaration gate sits strictly before the first
transport gate in the receipt's own gate order.

### 2.1 The carrier

| coordinate | value |
|---|---|
| configurations | $(s_A, s_B, p_A, p_B)$, **81** |
| system per wing | a **qutrit**, $s_X \in \{0,1,2\}$ |
| pointer per wing | three states, $p_X \in \{0,1,2\}$, $0$ = ready |
| index | $i = ((s_A\cdot 3 + s_B)\cdot 3 + p_A)\cdot 3 + p_B$ |
| initial configuration | $j_0 = 0$, i.e. $(0,0,0,0)$ |
| state | $p(0) = \delta_{j_0}$ |

Wing $A$ is the pair $(s_A, p_A)$ and wing $B$ the pair $(s_B, p_B)$. The index
map factorises the carrier as the system pair times the pointer pair,
$i = a\cdot 9 + p$ with $a = 3s_A + s_B$ and $p = 3p_A + p_B$; §8 uses that
factorisation and nothing else.

### 2.2 The measurement family

Three declared measurements, given as **integer quaternions** and converted to
rotation matrices by the Euler–Rodrigues formula. The matrices are pinned as
data and the constructor is anchored against them (A01).

$$R_0 = \begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}\quad
R_1 = \begin{pmatrix}1&0&0\\0&\tfrac35&-\tfrac45\\0&\tfrac45&\tfrac35\end{pmatrix}\quad
R_2 = \begin{pmatrix}\tfrac{5}{13}&-\tfrac{12}{13}&0\\\tfrac{12}{13}&\tfrac{5}{13}&0\\0&0&1\end{pmatrix}$$

from the quaternions $(1,0,0,0)$, $(2,1,0,0)$ and $(3,0,0,2)$. $R_1$ rotates
the $(1,2)$ coordinate plane by the 3-4-5 angle and $R_2$ the $(0,1)$ plane by
the 5-12-13 angle: two **different** planes, so the family is genuinely
three-dimensional and not one plane rotation with a spectator direction. Every
entry is rational and each matrix is measured exactly orthogonal.

The local leg on wing $X$ at setting $g$ is

$$U_X(g) \;=\; \sum_{o=0}^{2} \Pi^{g}_{o} \otimes \mathrm{Sh}^{\,o},$$

with $\Pi^g_o$ the rank-one projector onto column $o$ of $R_g$, $\mathrm{Sh}$
the pointer 3-cycle, and the identity on the other wing. The decomposition is
measured, not assumed, and its comparator is built independently of both
constructors it audits: the projectors are measured orthonormal, the outcome
shift map is measured **injective** (A06), and every declared local leg is
measured equal, entry by entry, to the sum assembled from the **pinned**
rotation matrices and an **independently declared** shift table — so a
perturbation of the rotation constructor or of the shift map moves one side of
the comparison and not the other. Injectivity is what makes the pointer value
at the final division event a **record** of the outcome.

### 2.3 The preparation, and its completion pinned in full

The declared preparation vector on the system pair is

$$\psi \;=\; \tfrac23\left(\lvert 0,1\rangle + \lvert 1,0\rangle\right) \;+\; \tfrac13\,\lvert 2,2\rangle .$$

It is a unit vector; its Schmidt rank is measured **3**, so it is entangled with
three nonzero Schmidt coefficients $(\tfrac23,\tfrac23,\tfrac13)$; and it is
measured **invariant** under the exchange of the two systems. The first base's
preparation vector is the singlet: *anti*-invariant, Schmidt rank two, equal
coefficients. What the two share is exactly one property, and it is the one the
species needs — the **Born shadow** of the preparation column is invariant under
the wing exchange, so the wing exchange is not excluded at the outset from being
a co-reference of the realized process.

The preparation leg is $U_{\text{prep}} = V \otimes I_9$, the identity acting on
the pointer pair, with $V$ the declared orthogonal completion

$$V \;=\; H\cdot Q,$$

$H$ the Householder reflection $I - 2ww^{\mathsf T}/(w^{\mathsf T}w)$ with
$w = \psi - e_{(0,0)}$, which carries $e_{(0,0)}$ exactly to $\psi$, and $Q$ the
**declared transposition** of the system-pair basis states $\lvert 0,1\rangle$
and $\lvert 0,2\rangle$, which fixes $\lvert 0,0\rangle$ so that
$V e_{(0,0)} = \psi$ still.

**A completion is never forced, so it is pinned as data.** In the basis ordered
$(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)$:

$$V=\begin{pmatrix}
0&0&\tfrac23&\tfrac23&0&0&0&0&\tfrac13\\
\tfrac23&0&\tfrac59&-\tfrac49&0&0&0&0&-\tfrac29\\
0&1&0&0&0&0&0&0&0\\
\tfrac23&0&-\tfrac49&\tfrac59&0&0&0&0&-\tfrac29\\
0&0&0&0&1&0&0&0&0\\
0&0&0&0&0&1&0&0&0\\
0&0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&0&1&0\\
\tfrac13&0&-\tfrac29&-\tfrac29&0&0&0&0&\tfrac89
\end{pmatrix}$$

Column 0 is $\psi$. The instrument constructs $V$ from $H$ and $Q$ and anchors
it against this matrix **entry by entry** (A03), and measures it exactly
orthogonal.

**Why the transposition is there, stated plainly.** The Householder $H$ built
from an exchange-invariant $\psi$ is itself exchange-equivariant, so its Born
shadow is exchange-symmetric — measured. The declared $V$'s Born shadow is
measured **not** to be. That single declared choice is what makes the full-leg
rule admit one permutation rather than two at the two symmetric settings, where
the wing exchange would otherwise compete; at the four asymmetric settings the
full rule's identifications do not depend on it. Its deeper role is measured in
§7.2: an exchange-equivariant completion makes the wing exchange intertwine the
preparation leg, and with it the whole leg sequence, so that every loop is
flat. The choice is a free declaration and is disclosed as one; §8 measures
what the family of alternatives does.

### 2.4 The family, the frames, the checkpoints

Six declared settings, the size computed from the declaration:

| setting | wing $A$ | wing $B$ | class |
|---|---|---|---|
| GP-A | $R_0$ | $R_1$ | asymmetric |
| GP-B | $R_0$ | $R_2$ | asymmetric |
| GP-C | $R_1$ | $R_2$ | asymmetric |
| GP-D | $R_2$ | $R_1$ | asymmetric |
| GP-E | $R_0$ | $R_0$ | **symmetric** |
| GP-F | $R_1$ | $R_1$ | **symmetric** |

Which members are symmetric is computed from the family, not typed: **2** of 6.

Two frames, $F_1 = (\text{prep}, A, B)$ and $F_2 = (\text{prep}, B, A)$: the same
two local events in the two orders on one configuration space. The two wings'
legs are measured to **commute** at every one of the nine declared pairs of
rotations (A05) — the fact the positive control rests on.

The leg count is computed, **3**; the checkpoints are computed from it,
$t \in \{0,1,2,3\}$, with $t=0$ and $t=3$ the declared **division events**; the
nodes are $(\text{frame}, t)$, **8** per setting, and the **read time is a
coordinate of the node** and of the law datum; the path length bound is computed
as $L_{\max} = 2\cdot 3 + 2 = 8$, the canonical loop's own length.

### 2.5 The arena (declared, sizes computed)

| coordinate | value | how obtained |
|---|---|---|
| carrier | 81 | enumerated |
| settings / symmetric settings | 6 / 2 | computed from the family |
| frames, legs per frame | 2, 3 | computed |
| checkpoints, division events | 4, $\{0,3\}$ | computed from the leg count |
| nodes per setting | 8 | computed |
| path length bound | 8 | computed |
| **declared relabelling scope** | **162** | generated and deduplicated |
| **declared extension scope** | **216** | generated, deduplicated, unioned |
| admitted after the $j_0$ filter | **2** | filtered |
| admitted at the extension | **8** | filtered |
| switching group per setting | $2^{9} = 512$ or $2^{13} = 8192$ | enumerated |
| checkpoint subgroup | $2^{8-1} = 128$ | enumerated |

The **declared relabelling scope** is generated by a wing-exchange flag, a
cyclic system relabelling per wing and a cyclic pointer relabelling per wing;
its **extension** replaces the cyclic pointer relabelling by the pointer
transposition $1 \leftrightarrow 2$, which fixes the ready state and therefore
survives the $j_0$ filter where the cycles do not. The **relabelling scope, and
that scope alone**, is measured closed under composition, so it is a group and
not a list; the **extension is measured not closed** — it is a union, and
membership in it is a set test, which is all any result here uses it for. The
wing exchange $W$ — which moves the system pair **and** the pointer pair
together — is measured to factorise as $X_S \cdot X_P$, the system-only and
pointer-only exchanges, and that factorisation is measured rather than assumed.

The admitted set after the $j_0$ filter is measured to be exactly
$\{\mathbf{1}, W\}$: two elements, and every admission search in this unit runs
over those two.

---

## 3. The two gluing rules, and what they admit

Two corridor-bound rules are declared, each a **four-clause** admissibility
predicate applied in order — the $j_0$ filter, the rule's own leg list matched
order-free at the Born level, the occupied-set clause, the exact-law clause — and
a link is drawn only where the rule admits **uniquely**.

- **FULL** matches the *full declared legs*.
- **REALIZED** matches each leg *restricted to the configurations the process
  actually occupies before and after it*.

Measured, cell by cell, over all 24 (setting, checkpoint) cells:

| cells | FULL admits | REALIZED admits |
|---|---|---|
| GP-A … GP-D, $t = 0, 1, 3$ | the identity (1) | none |
| GP-A … GP-D, $t = 2$ | none | none |
| GP-E, GP-F, $t = 0, 1, 3$ | the identity (1) | **the wing exchange** (1) |
| GP-E, GP-F, $t = 2$ | none | **the wing exchange** (1) |

The full-leg rule draws at **18** cells and the realized rule at **8**.

**The leg-prefix alignment profile**, computed independently as multiset
equality of canonical Born leg keys over the first $t$ declared legs — order-free
matching without any permutation search — is: aligned at $t=1$ and $t=3$ at
every setting, **divergent at $t=2$** at every setting. It agrees with the
full-leg rule's own transport profile at **18 of 18** cells. A path lies in an
*aligned* corridor if every identification it traverses sits at an aligned
checkpoint, and *crosses divergence* otherwise; on this base exactly one kind of
link crosses, the realized rule's wing exchange at $t=2$.

---

## 4. The path space

Nodes are $(\text{frame}, t)$; moves are leg applications in both directions and
the admitted identifications. A path is **reduced**: it never traverses one link
twice in immediate succession, a backtrack carrying no transport content. Two
objects are carried, each with its declared per-coordinate action:

| object | datum at a node | leg action | identification action |
|---|---|---|---|
| **L** the law's restriction | the occupied support and the exact law at the node's **declared read time**, carried inside the datum | the declared one-step Born transition, its transpose in reverse | the admitted permutation |
| **A** the amplitude layer | — (a closed-loop object) | the leg operator, its inverse in reverse | the permutation matrix |

Enumerated, never typed:

| setting | nodes | links | identification links | cycle rank | reduced paths | closed paths |
|---|---|---|---|---|---|---|
| GP-A | 8 | 9 | 3 | 2 | 422 | 56 |
| GP-B | 8 | 9 | 3 | 2 | 422 | 56 |
| GP-C | 8 | 9 | 3 | 2 | 422 | 56 |
| GP-D | 8 | 9 | 3 | 2 | 422 | 56 |
| GP-E | 8 | **13** | **7** | **6** | 16,168 | 2,820 |
| GP-F | 8 | **13** | **7** | **6** | 16,168 | 2,820 |

**Total: 34,024 reduced paths; 4,972,096 path pairs sharing both endpoints.**
The reduced-path counts include the length-zero path at each node; the
closed-path and based-path counts exclude it, since a length-zero loop carries
no transport content. Both conventions are stated because both appear in this
table. The reduced condition and three further properties are recomputed *from
the delivered rows themselves*: that no enumerated path traverses one link twice
in succession, that every path is a genuine walk ending at the node it declares,
that the graph is connected by union-find over its links, and that the cycle rank
is Euler's with that measured component count.

The matched table pairs only paths sharing **both** endpoints, so every contrast
is read at matched coordinates; and the read time is inside the L datum, so two
law data read at different checkpoints are measured never to compare equal — a
count gated at zero over every pair of the declared nodes at every setting. What
that coordinate does on *this* base is also measured and disclosed: on every
enumerated path carrying a readable law datum the read time inside the datum
equals the checkpoint of the node the path ends at, so here the coordinate is a
function of the endpoint, and the matched-coordinate property of the pair table
is structural rather than measured. The must-pass content is the node-level
count, and the law-conflating mutant is what gives it teeth.

| object | corridor | agree | disagree |
|---|---|---|---|
| **L** | aligned | 502,426 | 1,204,574 |
| **L** | crossing | 977,174 | 2,287,922 |
| **A** | aligned | 434,744 | 1,272,256 |
| **A** | crossing | 917,412 | 2,347,684 |

---

## 5. The probes and the two controls

| probe | setting | closed-loop holonomy (permutation part) |
|---|---|---|
| the canonical loop | **all six** | **the identity** |
| the aligned-prefix bigon, $t = 0, 1, 3$ | GP-E, GP-F | **the wing exchange** |
| the prefix-crossing loop $t{=}1 \leftrightarrow t{=}2$ | GP-E, GP-F | the identity |
| the twisted comparator | GP-A … GP-D | **not a signed permutation** |
| the twisted comparator | GP-E, GP-F | $W\!\cdot\!D$, an element of the group |

**The positive control is a same-order path pair that must agree.** From
$F_1@t{=}0$ to $F_1@t{=}3$ the graph carries two paths: frame 1's three legs
forward, and the path that crosses to frame 2 at the initial division event,
runs frame 2's three legs, and crosses back at the final one. They share both
endpoints, and their amplitude-layer transports are measured **equal** at every
setting — because the two frames differ only by the order of two legs measured
to commute. The closed loop they form, the canonical loop, has holonomy exactly
the identity permutation at all six settings. Its discriminating power is small
and is stated as such: given the commuting-legs anchor it could not have come
out otherwise. What it does exclude is a broken traversal convention.

**The negative control has teeth, and its scope is stated.** Replacing one
identification of the canonical loop by the wing exchange, at a coordinate where
the base itself supplies the identity, produces a matrix that is **not even a
signed permutation** at the four settings whose genuine loops are all flat. At
the two symmetric settings the injected loop's holonomy is exactly
$W\!\cdot\!D$ — an element of the genuine holonomy group — so the control does
not discriminate at the two settings whose loops are already non-flat. The
instrument can see a twist; the flatness readings above are therefore not
vacuous.

**The direction flip-test passes on every loop that carries an edge list** —
**14** loops — each re-traversed with the direction convention flipped yielding
the **inverse** permutation. Its positive content is forced by algebra: the link
variables are measured orthogonal and the reverse traversal is the transpose, so
a reversed loop's matrix is the inverse of the forward one for any input, and
every element of this group is an involution. What the test retains is
instrument integrity, and that is not forced — the mutant that reads a leg's
reverse traversal without transposing breaks the relation and dies there.
Coverage is stated: the twisted comparator is the canonical loop with one link
overwritten and carries no edge list of its own, so **the negative control is
not flip-tested**.

---

## 6. The five patterns, each gated separately

### 6.1 P1 — a nontrivial holonomy group exists

Measured over every closed path of the committed path space:

| setting | closed paths at the base point | non-flat closed paths (all base points) | group order |
|---|---|---|---|
| GP-A … GP-D | 8 | 0 of 56 | 1 |
| **GP-E** | **364** | **1,896 of 2,820** | **4** |
| **GP-F** | **364** | **1,896 of 2,820** | **4** |

**P1 holds.** The pattern is present at the two symmetric settings and is
measured *absent* at the other four, and **both halves are clauses of the gate's
own predicate** rather than a table beside it — so the gate is a measurement that
comes out both ways on one base, and not a fixture of the instrument.

A disclosure belongs with the count. At the **declared base point** every closed
path's holonomy is a signed permutation — the count that are not is measured
**0** at every setting — so nothing is dropped from §6.2's value set. Over
*all* base points that is no longer true: **600 of 2,820** closed paths at GP-E
and **820 of 2,820** at GP-F have holonomies that are not signed permutations,
and for those the declared invariant is simply undefined. Those are counted
against the same denominator as the non-flat count: of the 1,896 non-flat closed
paths at GP-E, 600 are holonomies that are not signed permutations at all, and
820 of the 1,896 at GP-F. That is a fact about the connection, and it is printed
rather than filtered away.

### 6.2 P2 — the group, computed, at the declared completion

Read as the permutation part of the closed-loop link product, based at
$F_1@t{=}0$, enumerated over every closed path based there, and counted as
**permutation tuples** — matrix content — never as name labels:

| setting | value set size | closed at the bound? | generated group order | structure |
|---|---|---|---|---|
| GP-A … GP-D | 1 | yes | 1 | trivial |
| GP-E, GP-F | **4** | **yes** | **4** | **the Klein four-group** |

The value set is measured **already closed** under composition at the declared
length bound, so it *is* the group rather than merely generating it; the group
is measured abelian with every element of order dividing two; and the number of
closed paths based there whose holonomy is not a signed permutation is measured
**0** at every setting, so nothing is dropped from the count.

The four elements, named by what they do:

| element | fixed configurations of 81 | order |
|---|---|---|
| the identity | 81 | 1 |
| $W$, the wing exchange | 9 | 2 |
| $D$, **the completion's non-equivariance defect** | **45** | 2 |
| $W\!\cdot\!D$ | 9 | 2 |

$D$ is *not* the system-only wing exchange (27 fixed points), *not* the
pointer-only wing exchange (27), and *not* $W$ (9). The first base's group is
$\{1, W, X, WX\}$ with $X$ and $WX$ the two **halves** of its wing exchange; base
G's group is the same abstract group built from a different second generator.

**The isomorphism type is a reading at the declared completion.** Swept over the
declared completion family $V = H\cdot Q$ with $Q$ any permutation of the nine
system-pair indices fixing the initial one — 40,320 members, every one of which
has $\psi$ as its first column — a non-trivial defect is measured at **40,224**
of them, so the *existence* of the geometry is generic in the family and the
completion of §7.2 is one of **96** exceptions. The **group**, however, is not
generic: the family is dihedral of order $2n$ in the defect's order $n$, the
whole measured spectrum $1, 4, 6, 8, 10, 12, 14, 30$ is exhibited by full
rebuild, and the Klein four-group is the involutive class — of which the pinned
completion's own class, the defect fixing **45** of the 81 configurations, is
**864 of 40,320, about 2.14%** of the family. Klein-four is therefore a property
of the declared completion and not of the species, and it is reported as one.
§8 is the census.

### 6.3 P3 — two curvature sources

**Source (i), identification multiplicity.** Six coordinates — GP-E and GP-F at
$t \in \{0,1,3\}$ — carry **two** distinct admitted maps, the full-leg rule's
identity and the realized rule's wing exchange. The bigon each forms has
holonomy exactly the wing exchange (§5). Everywhere else the multiplicity is at
most one.

**Source (ii), the completion's non-equivariance defect, isolated.**
Multiplicity is measured **not necessary**: the single-rule sub-connections, in
which every coordinate carries at most one admitted map, are built and
enumerated separately.

| setting / rules | links | cycle rank | closed paths at $F_1@t{=}0$ | classes | group |
|---|---|---|---|---|---|
| GP-A … GP-D / FULL only | 9 | 2 | 8 | identity $\times$ 8 | 1 |
| GP-A … GP-D / REAL only | 6 | — | 0 | — | 1 |
| GP-E, GP-F / FULL only | 9 | 2 | 8 | identity $\times$ 8 | 1 |
| **GP-E, GP-F / REAL only** | 10 | 3 | **18** | **identity $\times$ 10, $D$ $\times$ 8** | **2** |
| GP-E, GP-F / FULL+REAL | 13 | 6 | 364 | identity 82, $W$ 86, $D$ 90, $W\!D$ 106 | 4 |

The realized-rule sub-connection alone — multiplicity exactly one at every
coordinate — is already non-flat, and the element it carries is $D$.

The proximate cause is measured directly. The wing exchange is measured **not**
to intertwine the **preparation** leg at any setting, and

$$D \;=\; P_W\,U_{\text{prep}}^{-1}\,P_W\,U_{\text{prep}}$$

is computed exactly on this base: a **signed permutation**, of order **2**, with
**45** fixed configurations, not the identity, not $W$, and not either half of
$W$. §8.1 derives its closed form and measures that it is a function of the
declared **completion** alone — the preparation vector does not enter it.

**P3 holds, with both sources exhibited.**

### 6.4 P4 — the defect is a group element

The defect's permutation, computed in §6.3 from the declared preparation leg and
the wing exchange, is tested against the group computed in §6.2 from the
enumerated closed paths — **two independent computations, compared as tuples and
never as names**.

| setting | group order | $D$ is an element |
|---|---|---|
| GP-A … GP-D | 1 | **no** |
| GP-E, GP-F | 4 | **yes** |

The second row is what makes the first a measurement: where the group is trivial
the defect is measured *not* to belong to it — which is a real reading given
P3's separate measurement that the defect is not the identity. **P4 holds.**

### 6.5 P5 — non-principality

Membership of every holonomy element in every declared and admitted collection,
computed:

| element | declared scope (162) | declared extension (216) | admitted (2) | admitted extension (8) |
|---|---|---|---|---|
| the identity | yes | yes | yes | yes |
| the wing exchange $W$ | yes | yes | yes | yes |
| **$D$** | **no** | **no** | **no** | **no** |
| **$W\!\cdot\!D$** | **no** | **no** | **no** | **no** |

**Two of the four** elements lie outside every declared collection, at both
settings whose group is nontrivial, and **zero of one** at the four where it is
trivial. **P5 holds** — the connection is not principal for base G's certified
relabellings either.

Three things belong beside that table.

**How much of it is free.** Each of the four collections is measured invariant
under left multiplication by the wing exchange and measured to contain both the
identity and $W$, so those two rows are forced everywhere by the scope's own
generators and the $W\!D$ row is forced to repeat the $D$ row; and the
inclusions between the collections are measured, so a single "no" at the widest
collection forces the other three. **Exactly one cell is free** — whether $D$
lies outside the declared 216-element extension — and P5's verdict is that one
measurement. The table is its consequence and is reported as such.

**What the links are.** Every *identification* link of this connection is a
transport the base admits — by construction, since admission searches the
admitted set. The *leg* links are measured not to be transports the base admits
at all: at a symmetric setting the two preparation legs are measured not to be
signed permutations, and the four local legs, which *are* genuine permutations
of the 81 configurations, are measured outside all four collections. So the
group those links generate around loops is generated in part by transports that
were never in any declared scope.

**How strong the escape is.** It is robust — §8 measures it for every
geometry-bearing completion of this preparation, 40,224 of 40,224 — and its
strength is bounded by how small the declared scope is; the scope is a
declaration and a wider one is searched in §7.3.

For the record, and measured: the two halves of base G's wing exchange, $X_S$
and $X_P$, are also outside the declared scope, whose wing flag always moves the
system pair and the pointer pair together — but on this base neither of them is
in the holonomy group. The escape is real and its witnesses are different ones.

---

## 7. The gauge layer, and the three declaration flip-tests

### 7.1 The switching sweep, complete

The declared switching group assigns one sign to each link of a setting's own
graph. Its order is computed, never typed: $2^{9} = 512$ where only the full-leg
rule supplies identifications and $2^{13} = 8192$ where the realized rule
supplies four more. The **checkpoint subgroup** — the switchings induced by a
sign at each node, the base's own checkpoint-phase redundancy — has order
$2^{8-1} = 128$ at every setting. **The sweep is complete at every setting and
over every declared loop that carries an edge list**, 14 loops in all, with every
holonomy **rebuilt from the link variables**, the value cache bypassed.

Measured: **85,760** exact matrix comparisons; **0** deviations from the global
scalar action; **0** swept holonomies that are not signed permutations; **0**
loops whose sign moves under the checkpoint subgroup. The bypass is measured
against a cache that is measured to exist and measured to work: before the sweep
the cache is **primed** with the very keys the sweep will request — **14**
entries written, one per swept loop — a second pass over those keys is measured
to return the **14** stored values, the sweep is measured to request a key that
is already in the populated cache **13,806** times, and its hit count is
nevertheless **zero** against **85,760** measured misses. A zero-hit count over
zero lookups would be vacuous; this one is 13,806 refusals to read a cache that
had the answer. The tested set is fixed by **declaration** —
every declared loop with an edge list, in the order the probes are built — and
never selected by the verdicts under audit; the one declared probe it does not
reach, the twisted comparator, is named as the exclusion it is.

**One clause is forced by algebra and is reported as a disclosure.** Because the
switching acts on a closed loop by a global $\pm 1$, and a signed permutation
matrix and its negative have the same permutation part, the invariance of the
permutation part is an algebraic identity: no switching and no mutant could make
it fail. The sweep confirms it — exactly one permutation part at every declared
loop over the complete group — and that confirmation is what is reported. The
sweep's must-pass teeth are the scalar-action, signed-permutation and
checkpoint-telescoping clauses; and the mis-conventioned control does move, so
the sweep can certify an invariance at all.

### 7.2 The completion flip-test

A completion is never forced. The instrument rebuilds the **entire base** on the
alternative completion — the bare Householder $H$, i.e. the declared completion
with $Q$ removed, whose first column is the **same** $\psi$ — and re-measures:

| measured at the alternative completion | value |
|---|---|
| Born shadow of the completion is exchange-symmetric | **yes** (at the declared completion: no) |
| the four clauses of the declared species | **all hold** |
| cells where the full-leg rule draws a link | **14** (declared: 18) |
| cells where the realized rule draws a link | **8** (declared: 8) |
| identification links per setting | 3 / 3 / 3 / 3 / **5** / **5** (declared: 3 / 3 / 3 / 3 / 7 / 7) |
| settings at which the canonical loop exists | **4 of 6** (declared: 6 of 6) |
| **holonomy group order per setting** | **1, 1, 1, 1, 1, 1** |
| the completion's non-equivariance defect | **the identity**, 81 fixed points |

**The geometry vanishes, and the mechanism is measured.** At the bare
Householder the completion is exchange-**equivariant**, so the wing exchange
intertwines the preparation leg at every setting and with it the whole leg
sequence: every loop is flat, whichever rule drew its links, and the defect is
the identity. The admission table moves too, and in both directions: at the two
symmetric settings the full-leg rule now admits *two* permutations at
$t \in \{0,1,3\}$, so those links are refused for want of uniqueness, while at
$t = 2$ it admits one and draws a link the declared base does not have. What
survives is not nothing — **14** full-leg identifications, the canonical loop at
the **four** asymmetric settings, and every clause of the declared species — so
the five patterns are **posable** on that base and are posed: the answer is
group order 1 at every setting, which is the pre-registered outcome
`GEN-STRUCTURE-ABSENT`, computed rather than blocked.

This is reported and folded into **no verdict**. What it licenses is the scope
statement: every result of this unit stands at the **declared** completion, and
the completion is part of the base's declaration exactly as the preparation
vector is. What it does *not* license is a claim about the family: this
completion is one member of it, and §8 measures which member.

### 7.3 The admission scope

Every admission search that feeds a link, a profile or a verdict runs over the
**2** elements of the declared 162-element scope that survive the $j_0$ filter.
The declared 216-element extension, which admits **8**, is searched with the same
four-clause predicate, and the cells where the two disagree are printed in the
receipt. Because admission is by uniqueness, a wider scope can *refuse* a link
the narrower one draws; the settings at which the canonical loop would cease to
exist are named there. The measurement is folded into no verdict.

### 7.4 The measurement-family probe

The six-setting family is a free declaration, so what depends on it is measured.
Two **further** symmetric settings are built and the base re-enumerated on them:
one sharing the declared rotation $R_2$ on both wings, and one sharing a
rotation built from the **fresh** integer quaternion $(4,1,2,0)$, which is not
in the declared family at all and is measured exactly orthogonal. At all three
symmetric settings the based holonomy group and the class counts are measured
**identical** — order 4, Klein four, 82 / 86 / 90 / 106. The measurement family
is measured **inert** for the geometry: the holonomy at a symmetric setting does
not depend on which rotation the two wings share. Folded into no verdict; it is
what entitles §9 to say which declared coordinates do work.

---

## 8. The completion census

The completion is the one declared coordinate that moves the outcome, so it is
not left as a caveat. It is swept whole.

### 8.1 The defect law

**Theorem (the defect law, gated).** Write the carrier as the system pair times
the pointer pair, $i = 9a + p$ in the index map of §2.1, and let $\Sigma$ be the
permutation that exchanges the two labels of such a pair — the same $9\times 9$
matrix on the system pair and on the pointer pair. The wing exchange moves both
pairs together, so $P_W = \Sigma\otimes\Sigma$, and the preparation leg acts on
the system pair alone, so $U_{\text{prep}} = V\otimes I_9$. Then for any
orthogonal completion $V$

$$D \;=\; P_W\,U_{\text{prep}}^{-1}\,P_W\,U_{\text{prep}}\;=\;\bigl(\Sigma V^{\mathsf T}\Sigma V\bigr)\otimes I_9 .$$

If moreover $V = H\cdot Q$ with $H$ the Householder of an exchange-**invariant**
$\psi$ and $Q$ a permutation of the system-pair labels, then

$$D \;=\; \bigl(\Sigma Q^{\mathsf T}\Sigma Q\bigr)\otimes I_9 ,$$

in which $\psi$ does not appear at all.

*Proof sketch.* The wing exchange moves the system pair and the pointer pair
together, so in the factorised index map it is $\Sigma\otimes\Sigma$; the
preparation leg acts as $V$ on the system pair and trivially on the pointer
pair. The four-factor product therefore splits, and on the pointer factor it is
$\Sigma\,I\,\Sigma\,I = I$, which gives the first form (using $V^{-1} =
V^{\mathsf T}$). For the second: $\psi$ exchange-invariant makes
$w = \psi - e_{(0,0)}$ exchange-invariant, hence $\Sigma H\Sigma = H$; and $H$ is
an involution. So $\Sigma V^{\mathsf T}\Sigma V = \Sigma Q^{\mathsf T}H\Sigma
HQ = \Sigma Q^{\mathsf T}\Sigma H^2 Q = \Sigma Q^{\mathsf T}\Sigma Q$: the
Householder cancels identically. $\square$

Both forms are measured against the direct $81\times 81$ computation, and the
$\psi$-independence is measured rather than argued: four declared, mutually
different, exchange-invariant preparation vectors — the declared $\psi$ and
three others — are measured to give the **same** defect, entry by entry, and a
fifth declared vector that is **not** exchange-invariant is the negative control
and is measured to give a **different** one. The invariance hypothesis is
load-bearing, and that is measured too. The $9\times 9$ form's fixed-point count
times the nine untouched pointer pairs is measured equal to the
81-configuration count: $5\times 9 = 45$.

Two consequences are recorded where they belong. First, "the preparation's
defect" would be a misnomer: $D$ is the exchange defect of the declared
**completion**, and at these bases it is manufactured by the declared
transposition alone. Second, since the identification multiplicity of §6.3 is
also a consequence of declared rules, **both curvature sources on this base are
declaration-side**. Whether any state-side curvature exists anywhere in the
theory is not decided here and is registered as an open question (§11.12).

### 8.2 The family, swept exhaustively

The law reduces the whole completion question to $9\times 9$, so the declared
family can be swept whole. The family is $V = H\cdot Q$ with $Q$ any permutation
of the nine system-pair indices fixing the initial one, so that **every member
has $\psi$ as its first column**: $8! = 40{,}320$ members, the size computed by
enumeration, and every member measured.

| defect's fixed configurations of 81 | 9 | 18 | 27 | 36 | **45** | 54 | 81 |
|---|---|---|---|---|---|---|---|
| completions | 16,704 | 11,520 | 5,376 | 4,608 | **864** | 1,152 | **96** |

| order of the defect | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 15 |
|---|---|---|---|---|---|---|---|---|
| completions | **96** | 1,440 | 4,224 | 4,608 | 4,608 | 6,912 | 9,216 | 9,216 |

Three facts are gated over the whole family.

1. **The exceptions are exactly the exchange-equivariant locus.** The defect is
   the identity on a member if and only if that member's $Q$ commutes with the
   system exchange — measured member by member, in both directions, with no
   mismatch. There are **96** of them, and the bare Householder of §7.2 is one.
2. **Geometry is generic.** **40,224 of 40,320** members — 99.76% — carry a
   non-trivial defect. The steering question the completion invites therefore
   has a measured answer, and it is the opposite of the suspicion: the declared
   completion is a typical member of its family and the flip-test's comparator
   is the degenerate one.
3. **The escape is universal.** The defect of every geometry-bearing member lies
   outside every declared collection: **40,224 of 40,224**, computed against the
   elements of the declared scope and its extension that act on the system pair
   alone — found by scanning the scopes (nine in each), not assumed.

### 8.3 The group family

The same sweep measures the relation that organises the family: at **every one**
of the 40,320 members, $\Sigma D\Sigma = D^{-1}$. With $W$ measured not to act
on the system pair alone — so no power of $D$ is $W$ — the group the base can
generate is

$$\mathrm{Hol} \;=\; \bigl\langle\, W,\, D \;\bigm|\; W^2 = D^{\,n} = 1,\; WDW = D^{-1} \,\bigr\rangle, \qquad n = \mathrm{ord}(D),$$

of order $2n$: the dihedral family. The measured order spectrum over the family
is $n \in \{1,2,3,4,5,6,7,15\}$, so the predicted holonomy group orders are
**1** (at the equivariant locus, where the links themselves are refused) and
**4, 6, 8, 10, 12, 14, 30**.

That prediction is not left as algebra. The family splits into **12 classes** by
(order of the defect, fixed configurations of the defect), and the
lexicographically first member of **every** class is rebuilt in full — new
completion, new admission table, new graph, new path enumeration, new based
holonomy — at the symmetric setting GP-E and at GP-A as the flat control:

| class | measured group order at GP-E | predicted $2n$ | abelian | at GP-A |
|---|---|---|---|---|
| ord 1, 81 fixed | 1 | — (links refused) | yes | 1 |
| ord 2, 9 fixed | 4 | 4 | yes | 1 |
| **ord 2, 45 fixed** (the pinned class) | **4** | 4 | yes | 1 |
| ord 3, 27 fixed | 6 | 6 | no | 1 |
| ord 3, 54 fixed | 6 | 6 | no | 1 |
| ord 4, 9 fixed | 8 | 8 | no | 1 |
| ord 4, 27 fixed | 8 | 8 | no | 1 |
| ord 5, 36 fixed | 10 | 10 | no | 1 |
| ord 6, 9 fixed | 12 | 12 | no | 1 |
| ord 6, 18 fixed | 12 | 12 | no | 1 |
| ord 7, 18 fixed | 14 | 14 | no | 1 |
| ord 15, 9 fixed | 30 | 30 | no | 1 |

Every rebuilt member's measured group order equals the dihedral prediction, and
the flat control is measured flat at every one. The **Klein four-group is the
involutive class**: both involutive classes rebuild to an abelian group of order
four with every element of order dividing two, and together they are **1,440 of
40,320**, about 3.57% of the family — of which the pinned completion's own
class, the defect fixing **45** configurations, is **864**, about **2.14%**.

One further measured fact belongs here, because it bounds a claim made
elsewhere. The value set at the declared length bound is measured closed at the
classes of defect order 1, 2, 3 and 4 — where it has 1, 4, 6 and 8 elements —
and measured **not** closed at orders 5, 6, 7 and 15, where it has nine elements
against generated groups of order 10, 12, 14 and 30. So the closure measured at
the declared completion (§6.2, D4) is a fact about the low-order case and not
about the construction; the group is always the closure, and the paper never
calls a value-set size a group order without the closure measurement beside it.

### 8.4 The pinned completion's own declared form

The pinned completion's $Q$ is a single transposition of the nine system-pair
labels. That sub-family is small enough to rebuild entirely: **28** members, the
count computed, each a full rebuild at GP-E and GP-A.

| outcome | members |
|---|---|
| flat at both settings (group order 1) | **4** |
| **the Klein four-group** at GP-E | **12** |
| **a non-abelian group of order 6** at GP-E | **12** |

The four flat ones are exactly the transpositions that commute with the system
exchange. So the isomorphism type is selected **inside the pinned completion's
own declared form**, not only across the wider family: 12 of 28 choices of a
single transposition give the Klein four-group and 12 give the non-abelian group
of order six.

### 8.5 What the census decides

- The **existence** of the geometry is generic in the declared completion
  family — 99.76% — and vanishes exactly on the exchange-equivariant locus.
- The **isomorphism type** is completion-selected, and the pinned completion's
  Klein-four class is about 2.14% of the family (the involutive locus, about
  3.57%).
- The **presentation** is family-wide: a wing exchange the base admits, a
  completion defect it does not, and $WDW = D^{-1}$.
- The **escape** is family-wide: 40,224 of 40,224.

So the pattern that survives a change of base is the existence of a nontrivial
group with two sources, one of them a completion-manufactured generator lying
outside the declared scopes, together with the relation that makes them
dihedral — and **not** the isomorphism type.

---

## 9. The two bases, coordinate by coordinate

Fifteen of the twenty-one rows read the first base's value from its committed
terminal receipt, which is itself **hash-pinned** (A13) and whose numbers are
**anchored exit-1** (A08–A12, A17); its group *structure* is not typed either
but named by this unit's own naming rule from the order, element orders and
abelianness the receipt reports. Six rows — marked **declared** — are typed
here because the first base's receipt carries no such field; they are
disclosures, not anchors. No object of its model is imported.

| coordinate | first base | base G | source / why it agrees |
|---|---|---|---|
| carrier | 36 | **81** | read (A17) |
| system dimension per wing | 2 | **3** | declared here |
| outcomes per measurement | 2 | **3** | declared here |
| arithmetic | the quartic field $\mathbb{Q}(\cos \pi/8)$ | **the rationals $\mathbb{Q}$** | declared here |
| preparation vector under the wing exchange | anti-invariant (the singlet) | **invariant** | declared here |
| preparation Schmidt rank | 2 | **3** | declared here |
| declared relabelling scope | 72 | **162** | read (A17) |
| settings | 6 | 6 | read (A17); **a copied design choice** |
| symmetric settings | 2 | 2 | declared here; **a copied design choice** |
| admitted after the $j_0$ filter | 2 | 2 | read (A17); **a consequence of the scope design** |
| admitted at the extension | 8 | 8 | read (A17); **a consequence of the scope design** |
| total reduced paths | 34,024 | 34,024 | read (A11); **graph combinatorics** |
| path pairs sharing both endpoints | 4,972,096 | 4,972,096 | read (A11); **graph combinatorics** |
| holonomy group order at a symmetric setting | 4 | 4 | read (A08); **geometry** |
| holonomy group structure | the Klein four-group | the Klein four-group | derived from the receipt; **geometry, at the declared completion** |
| value set closed at the declared bound | yes | yes | read (A09); **geometry** |
| elements outside every declared collection | 2 | 2 | read (A10); **geometry** |
| realized-rule sub-connection: closed paths | 18 | 18 | read (A12); **graph combinatorics** |
| realized-rule sub-connection: group order | 2 | 2 | read (A12); **geometry** |
| **the second generator** | **the qubit-only wing swap** | **the completion's non-equivariance defect** (neither half, 45 fixed points) | read; differs |
| **the second generator is one half of the wing exchange** | **yes** | **no** | derived from the receipt; differs |

Of the twenty-one compared coordinates, **nine** are measured different and
**twelve** measured the same — but the twelve are not of one kind, and the
distinction is the point. **Four** of them (the setting count, the
symmetric-setting count, and the two admitted-set sizes) agree because this
base's family and scope were *designed* with those shapes, and they carry no
information about the geometry. **Three** (the total reduced paths, the path
pairs, and the realized-rule sub-connection's eighteen closed paths) agree
because the two path graphs are isomorphic, and are counts of combinatorics both
bases happen to share. The remaining **five** — the group order, its isomorphism
type, the closure of the value set at the declared bound, the two elements
outside every declared collection, and the realized-rule sub-connection's group
order — are the geometric agreements, and they are what the verdict rests on.

**Which of the differing coordinates do work.** One of the nine is measured to:
the preparation's Born-shadow symmetry type, which decides whether the wing
exchange can be a co-reference at all. Two more of the nine — what the second
generator is, and whether it is a half of the wing exchange — are measured to be
consequences of the declared **completion** (§8.1), which is not a row of this
table at all, since both bases declare one; it is the parameter that decides the
rest. Of the remaining six, two are measured **inert**: which rotation the two
wings share at a symmetric setting, so the arithmetic and the measurement bases
do no work here (§7.4, including a rotation from a quaternion outside the
declared family), and the preparation vector itself at a fixed completion, as
far as the defect is concerned (§8.1). The carrier size, the system dimension,
the outcome count and the scope size are not separately varied by this unit;
they enter the elements' fixed-point counts and the sizes of the collections,
and no inertness is claimed for them. The agreements are therefore evidence that
the two bases share a mechanism, not that they share it despite nine independent
differences — and the differences are not nine independent variations either.

**The class counts agree for a reason neither base declares, and it is left
open.** The class counts 82 / 86 / 90 / 106 at a symmetric setting are the same
on both bases. That is *not* a consequence of the shared graph and the shared
group, and the instrument measures how far from it: gauge-fixing the connection
on a spanning tree grown from the base node — every one of the 13 links measured
to land in the Klein four-group — the holonomy of a based closed walk is
measured, at every one of the **364** of them, to be the ordered product of the
gauge-fixed labels along it. Enumerating **all $4^6 = 4{,}096$** assignments of
the group's elements to the six independent cycles, the measured profile
82 / 86 / 90 / 106 is reproduced by **96** of them — **2.3%**, and 96 of the
**3,906** assignments whose labels generate the whole group, **2.5%** — against
**89** distinct profiles, the most common being 78 / 90 / 94 / 102 at 384
assignments. So an isomorphic graph and an isomorphic group do not determine
these counts. What the two bases additionally share is measured: their admission
tables coincide **cell for cell in the permutation each rule draws**, at all 24
matched coordinates. Why two bases with none of the same flesh should share that
is **registered OPEN**; this unit does not explain it and does not claim it as
confirmation.

---

## 10. The verdict

The decision rule is pre-registered and the verdict is derived from the five
pattern gates and from nothing else: `GEN-STRUCTURE-ABSENT` if P1 fails;
`GEN-STRUCTURE-REPRODUCES` if all five pattern gates pass;
`GEN-STRUCTURE-VARIES-⟨list⟩`, with the failing patterns named in the tag,
otherwise; `GEN-BLOCKED-AT-⟨object⟩` where a census cannot be posed. The
qualifier slot of the pre-registered `UNIT-OUTCOME(-QUALIFIER)` form carries the
scope; the verdict is re-derived inside its own gate from the recorded gate
results and measured to be the string the rule selects.

All five pattern gates pass.

> **`GEN-STRUCTURE-REPRODUCES-AT-DECLARED-COMPLETION`**, at the committed
> finite scope, at the declared admission scope, at the declared completion,
> per coordinate.

The qualifier is not decoration. The completion is declared arena data by the
pin's own terms, and at another declared orthogonal completion of the very same
preparation vector — the exchange-equivariant one — the same five gates return
`GEN-STRUCTURE-ABSENT`. What the unit measures is that the geometry exists at
the declared completion and is absent exactly on the equivariant locus of the
completion family, which is 96 of its 40,320 members.

**What reproduces, stated at the level the evidence carries.** The transport
geometry is **not** an artifact of the first committed base. On a second base of
the same species and none of the same flesh — a qutrit system, three outcomes,
rational arithmetic, a different and oppositely-symmetric preparation, a
different completion, a larger relabelling scope — the reproduced content is
existence-level and is this:

- a **nontrivial holonomy group** exists;
- it has **two curvature sources**, with multiplicity again sufficient and again
  measured not necessary;
- one of them **manufactures a generator** that lies outside the base's own
  declared isomorphisms, so the connection is again not principal.

And beside it, the computed difference, folded into nothing: the isomorphism
type is selected by the declared completion. Within the completion's own
declared form, 12 of 28 choices give the Klein four-group and 12 give the
non-abelian group of order six. What recurs across the two bases is the
presentation — a wing exchange the base admits, a completion defect it does not,
and the relation $WDW = D^{-1}$ that makes them generate a dihedral group of
order twice the defect's order. Both bases realise the case where the defect is
an involution and the group is the Klein four-group. The isomorphism type is a
function of the declared completion and is not claimed to be a property of the
theory.

---

## 11. Scope and non-claims

1. **No claim about nature.** Every result is a statement about declared finite
   models, a declared gauge and declared finite search scopes.
2. **Two bases are two bases.** This unit measures that the patterns survive one
   change of flesh, and it measures one completion family exhaustively. It does
   not establish that they survive every change, and no quantifier over bases is
   entered anywhere. It also does not re-measure the first base's third
   transported object, the composition defect of the law's own factorisation,
   which is out of the pin's scope and is not carried here (D3).
3. **The completion is a declaration, and it is what the verdict is scoped to.**
   The *group* is completion-selected; only the *existence* of a nontrivial
   group is measured generic in the declared family (99.76% of it). Every result
   here stands at the declared completion.
4. **The admission criterion is a declaration** — uniqueness of the admitted
   transport — and it is scope-dependent; the alternative scope is searched and
   disclosed, not silently taken.
5. **Every claim is per coordinate.** The read time is a coordinate of the node
   and of the L datum; the matched table pairs only paths sharing both endpoints,
   which makes that matching structural on this base, and the coordinate is
   measured to be a function of the endpoint here.
6. **The path space is bounded** at $L_{\max}=8$, the canonical loop's own
   length, and every count is a count at that bound. The holonomy *value set* is
   a value set at that bound; the group it generates is computed separately by
   closure, and the two are measured equal here rather than assumed to be — a
   fact §8.3 measures to belong to the involutive case.
7. **The species is a declaration of this unit**, and its clauses are measured
   on the constructed operators rather than asserted: two wings with commuting
   local legs, a preparation, records at the final division event, exact
   orthogonality everywhere. The species does **not** select the completion:
   both completions of §7.2 are measured to satisfy every clause of it.
8. **The two wings must be isomorphic.** A base with wings of different
   dimensions has no wing exchange and none of the five patterns can be posed on
   it; the second base enlarges both wings for that reason (D9).
9. **The switching sweep is complete** at every setting over every declared loop
   that carries an edge list, and the checkpoint subgroup is swept complete as
   well. One clause of that sweep is analytically forced and is reported as a
   disclosure, not as a measurement; so is the positive content of the direction
   flip-test, whose retained teeth are stated separately.
10. **The negative control is not flip-tested**, because it carries no edge list
    of its own; that coverage gap is stated at the claim. At the two symmetric
    settings its holonomy is $W\!\cdot\!D$, an element of the group under study,
    so it does not discriminate there.
11. **Nothing is claimed about locality, topology, causality, spacetime, fields,
    QFT or gravity.** "Holonomy", "connection", "corridor" and "arena" are
    operational vocabulary for declared finite objects, and no continuum,
    curvature or geometric interpretation is entered.
12. **Both curvature sources on this base are declaration-side, and the
    state-side question is open.** Identification multiplicity is a consequence
    of the declared gluing rules; the defect is measured to be a function of the
    declared completion alone, with the preparation vector cancelling out of it
    identically (§8.1). Whether any curvature carried by the *state* rather than
    by a declaration exists anywhere in this theory is not decided here, is not
    posed by the pin, and is registered as the open question it is.
13. **Nothing of the first base's model is imported.** Only its committed
    receipt is read; the file is hash-pinned and the numbers taken from it are
    anchored exit-1, so a drift in either kills the run.

---

## 12. The receipt

`v13/code/gen_generality_exact.py` → `gen_generality_output.txt` +
`gen_generality_receipt.json`.

- **Anchors:** 17, exit-1-only. Seven are **self-anchors against this unit's own
  pinned base declaration** — the three rotation matrices entry by entry, the
  preparation vector as the first column of the completion, the full $9\times 9$
  completion matrix entry by entry, the orthogonality of every declared operator
  at every (setting, frame), the commutation of the two wings at every declared
  pair of rotations, the injectivity of the record shift, and the unit-norm and
  orthogonality of the completion. Six are **external anchors against the
  committed terminal receipt of the first base** — its group order, its value-set
  size and closure, its elements outside every declared scope at both symmetric
  settings, its total reduced paths and path pairs, its realized-rule
  sub-connection's closed-path count and group order, and its declared arena —
  plus one that pins that receipt **by hash**: the sha256 of the file, the
  generator hash the receipt records for its own instrument, and its schema
  string, so that "the committed NT terminal receipt" is an assertion rather
  than a caption. Three anchor the **census**'s principal counts against the
  independently computed values contributed with it (last sentence of this
  section). That most of the anchors are self-anchors is a disclosure, not a
  secret: a second base has no prior committed numbers to reuse, and what those
  anchors buy is that no constructor can drift from the printed declaration
  without the run dying.
- **Gates:** 36, of which 30 are must-pass and 6 are declared disclosures (the
  analytically-forced permutation-part clause, the admission-scope search, the
  completion flip-test, the forcedness of P5's membership table, what the
  read-time coordinate does on this base, and the measurement-family probe —
  none of them carrying a verdict). The falsification census below covers 29 of
  the 30 — the thirtieth is the census's own gate.
- **The census gates.** The defect law is gated against the direct
  $81\times81$ computation over a declared five-member family of preparation
  vectors with an exchange-non-invariant negative control; the 40,320-member
  completion sweep is **exhaustive** and gated on the equivariant-locus
  characterisation (both directions), the dihedral relation at every member, the
  universal escape, and the agreement of the pinned completion's own census
  entry with the defect measured on the base itself; the rebuild sweep is gated
  on the dihedral prediction at all 28 members of the declared form and at one
  member of each of the 12 measured classes, and on the pinned completion's
  rebuilt row reproducing the group order the main enumeration measures.
- **The path space:** 34,024 reduced paths; 4,972,096 path pairs; every count
  computed from the enumeration and none typed. Four properties of the delivered
  rows are recomputed from the rows themselves.
- **Independent comparators.** Where a construction is checked against a
  rebuild, the rebuild is assembled from data independent of the component under
  audit: the record decomposition is rebuilt from the **pinned** rotation
  matrices and an **independently declared** shift table, so the mutant that
  collapses two outcomes onto one shift dies at the injectivity clause *and* at
  the decomposition clause, and the mutant that perturbs a constructed rotation
  dies at the decomposition clause too.
- **The fresh-evaluation gate is measured, not vacuous.** The value cache is
  primed before the self-test with the keys the self-test will request; the
  priming pass is measured to return stored values on its second visit; the
  self-test is measured to request keys that are in the populated cache; and its
  hit count is gated at zero against 85,760 measured misses. Zero hits over zero
  lookups would be vacuous, and the counts that exclude that reading are printed.
- **Mutants:** 27, each run to completion, **27 of 27 died** — each measured to
  exit 1 and to falsify at least one named gate or anchor. **The set of must-pass
  gates that no mutant falsifies is EMPTY**, at denominator **29**: all 29 are
  falsified by some mutant, **26** of them by a mutant that perturbs a
  computation, and the three carried only by a waiver are named — the exactness
  sweep, the no-mutant-exemption sweep and the verdict vocabulary. Each mutant
  declares its kind and the split is counted from the declaration: **22 perturb
  a computation and 5 are waivers.** A waiver overwrites a gate's computed
  predicate, or registers a sentinel in its evidence list, after the fact; what
  it measures is that the predicate carries the exit code — not that the gate
  would catch a computational defect, and the two are not claimed to be the same
  thing. Two of the gates whose input is this module's own **source text** —
  exactness and the no-mutant-exemption sweep — can only be falsified that way,
  because no mutant flag can perturb a source file that freeze-on-delivery
  forbids editing; they are declared waivers for that reason, and the gates they
  carry are named among those falsified only by a waiver. Both denominators are
  printed.
- **No gate predicate references mutant identity**, measured as the headline
  says it: an AST sweep finds every `gate(...)` and `anchor(...)` call site —
  **54** of them — walks its argument expressions to any depth, and measures the
  number reaching the mutant flag to be **zero**; and the four exemption forms —
  `!=`, `not in`, `is not`, and a negated `==` — are counted separately anywhere
  in the source, where the **one** occurrence found (a `not in` in the
  command-line argument validation) is measured to lie outside every one of the
  54 call sites, and the `!=` count is gated at zero.
- **Exactness:** `fractions.Fraction` throughout. Every declared operator of base
  G has rational entries and is exactly orthogonal over $\mathbb{Q}$, so equality
  of matrices is equality of exact rationals and no tolerance exists anywhere in
  the instrument. An AST sweep finds no float literal and no call to `float`, and
  a runtime sweep finds no float in any value that reached a gate or an anchor.
- **Determinism:** no wall-clock value enters the receipt or the rendered output;
  two delivery-mode runs were executed and their artifacts are byte-identical.
- **One instrument-hygiene item is disclosed rather than changed.** A
  delivery-mode run writes its two artifacts before it computes its exit code,
  so a *failing* delivery run would overwrite them with a failing pair rather
  than leave the last good pair in place. The two runs behind these artifacts
  each exited zero with no must-pass failure, and their artifacts are
  byte-identical to each other.

The defect law, the completion census and the connection enumeration of §9 were
contributed by this unit's review panel and are re-derived, re-measured and
gated natively here (v13 LOG #219).

---

## Appendix: deviations

**D1 — the second base is this unit's own construction, so its anchors are
mostly self-anchors.** A generality check on a new base has no prior committed
numbers of its own to reproduce. The response is to *pin the base as data* — the
rotation matrices and the full $9\times 9$ completion typed in the instrument —
and to anchor every constructor against the pinned declaration entry by entry,
so the anchors catch constructor drift rather than reuse drift. Six genuine
external anchors are carried against the first base's committed receipt, one of
them pinning that receipt by hash, and the split is printed.

**D2 — the completion was chosen to be geometry-bearing, and the alternative is
rebuilt in full and measured rather than hidden.** At the bare Householder the
wing exchange intertwines the preparation leg at every setting, so the
completion manufactures no defect; the full-leg rule then admits two
permutations at the symmetric settings where it had admitted one, and draws the
wing exchange at $t = 2$ instead. Fourteen full-leg identifications survive, the
canonical loop survives at the four asymmetric settings, and the five patterns
are posed on that base and measured: the holonomy group has order 1 at every
setting, which is the pre-registered outcome `GEN-STRUCTURE-ABSENT`. The
alternative completion is measured to satisfy **every clause of the declared
species** — the four clauses of §1 hold on it entry for entry — so the choice
between them is not a species question. It is a free declaration, and the unit
declares the geometry-bearing one: the exchange-equivariant completions form the
degenerate locus of the completion family (96 of 40,320), on which the
completion manufactures no defect and every loop is flat. The choice is
disclosed as a choice, its alternative is rebuilt and measured (§7.2), the whole
family is swept (§8), and every verdict is scoped to the declared completion.

**D3 — the two transported objects are the law's restriction and the amplitude
layer.** The first base's unit carried a third, the composition defect of the
law's own factorisation. It is not carried here: the five pre-registered patterns
are properties of the holonomy, which lives at the amplitude layer, and the law
datum is carried because the matched-coordinate discipline needs an object with a
read-time coordinate. Nothing is claimed about the composition defect on base G,
and no result of this unit rests on it.

**D4 — the holonomy value set is counted as permutation tuples.** The value set
is enumerated over the closed paths of the committed path space, which is bounded
at $L_{\max}=8$, so it *need* not be closed under composition; here it is
measured to be, and the group computed separately by closure is the same
four-element group. The paper never calls the value-set size a group order
without the closure measurement beside it. §8.3 measures that the closure is a
fact about the involutive case: at the higher-order classes the value set at the
same bound is measured not closed while the generated group is the predicted one.

**D5 — the path counts are combinatorial; the class counts are not, and the
agreement is registered open.** 34,024 paths and 4,972,096 pairs agree because
the two bases' path graphs are isomorphic, and that is reported as a consequence
of the graph. The class counts 82 / 86 / 90 / 106 need more than that: they are
fixed by the images of the six independent cycles in the group, and over the
4,096 assignments on this graph — 3,906 of which generate the whole group — they
take 89 distinct values, of which these four occur in about one in forty. An
isomorphic graph and an isomorphic group therefore do not explain the agreement.
What the two bases are additionally measured to share is their admission tables,
cell for cell in the permutation each rule draws. Why they should is registered
as an open question in §9 and is claimed as no confirmation of anything.

**D6 — the field's own products are memoised inside the switching sweep.** The
sweep spends its time on structure rather than on recomputing identical exact
rational products. Nothing is approximated and nothing is cached at the level of
a transported value: every quantity the self-test measures is rebuilt from the
link variables on every switching, with the transported-value cache bypassed and
its hit count gated at zero — against a cache measured populated, measured to
serve stored values, and measured to be asked for them by the sweep itself. The
memoising product routine is measured against the plain one on **every** swept
instance, since an all-positive switching is an exact equality test between them.

**D7 — the path length bound is a declaration.** $L_{\max} = 2\cdot\text{NLEGS}+2$
is computed from the model as the canonical loop's own length, so the pin's loop
lies inside the enumerated space; every count is a count at that bound and no
claim is entered about longer paths.

**D8 — no Lean.** As the pin states.

**D9 — the pin's "one wing enlarged" is read as "both wings enlarged".** The pin
asks for different wing dimensions, illustrating with "one wing enlarged, e.g.
qutrit-or-higher system side or enlarged pointer side". Two wings of *different*
dimensions admit no wing exchange at all, and without the wing exchange none of
the five patterns can be posed — the outcome would have been
`GEN-BLOCKED-AT-⟨the wing exchange⟩`. The reading taken enlarges both wings and
both sides of each (system and pointer, 3 and 3), which satisfies the pin's
intent a fortiori. The constraint is recorded as a non-claim (§11.8).

**D10 — the completion census's scopes, declared with their sizes.** The defect
law is measured on a declared five-member family of preparation vectors, not on
all of them. The 40,320-member completion sweep is **exhaustive**, at the
$9\times9$ level the law licenses, with the law itself measured against the
direct $81\times81$ computation. The **full rebuilds** are not exhaustive and are
not claimed to be: 28 members (every member of the pinned completion's declared
form) plus 12 members (the lexicographically first of each measured class), each
rebuilt at the symmetric setting GP-E and at GP-A as the flat control — the other
four settings are not rebuilt in the sweep, and the rebuild scope is printed in
the receipt. The connection enumeration of §9 is exhaustive over the $4^6$
assignments at one declared symmetric setting, under a declared cap on the size
of the connection space. The census costs about 25 seconds of the run.

**D11 — the measurement-family probe adds two settings that are not in the
declared family.** §7.4 builds two further symmetric settings, one of them on a
rotation from a quaternion outside the declared family, purely to measure whether
the family is inert. It is a disclosure, folded into no verdict, and no count of
the declared arena changes: the declared family remains the six settings of §2.4.
