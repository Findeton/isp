# The Generality Check

## The Nomological-Transport Geometry on a Second Base

**Status:** `GREEN-UNREVIEWED`

**Date:** 2026-08-07

**Frozen pin:** `v13/note-gen-generality-pin.md`, commit `5e8bc58`
(sha `0da6205815a6`)

**Immutable base:** `fceb614` — the nomological-transport unit TERMINAL (v13 LOG
#211). No object of the first base's model is imported anywhere in this unit:
the only thing read from it is its committed receipt's reported numbers, and
those are anchored exit-1.

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
**All five hold.**

**P1.** A nontrivial based holonomy group exists: at the two symmetric settings
**1,896 of 2,820** closed paths carry a non-identity holonomy, while at the
other four settings **0 of 56** do; and the negative control — a deliberately
twisted comparator — is measured non-identity at every one of the six settings,
so the flat readings are not vacuous.

**P2.** Counted as **permutation tuples** and never as labels, the based
holonomy group at the declared base point has order **4**, is measured already
**closed** at the declared length bound, is abelian with every element of order
dividing two, and is therefore **the Klein four-group** — the same isomorphism
type the first base earns, on a base that shares none of its flesh.

**P3.** Both curvature sources are exhibited. Identification multiplicity: six
coordinates carry two different admitted maps. And, isolated by running the
single-rule sub-connections separately, the **preparation's own swap-defect**
$P_W U_{\text{prep}}^{-1} P_W U_{\text{prep}}$ already makes the realized-rule
sub-connection non-flat — **8 of its 18** closed paths — at a connection every
coordinate of which has multiplicity exactly one. Multiplicity is sufficient
and is measured not necessary, on this base as on the first.

**P4.** That defect is measured to **be an element** of the group, at both
settings whose group is nontrivial and at none of the four where it is trivial.

**P5.** **Two of the four** elements lie outside the declared 162-element
relabelling scope, outside its declared 216-element extension, and outside both
admitted sets. The connection is **not principal** for this base's own
isomorphisms either.

**What varies is the element, not the pattern.** On the first base the
preparation-defect is one *half* of the wing exchange — the wing swap of the
system pair alone. Here it is measured to be neither half and no wing swap at
all: a permutation of order two fixing **45 of the 81** configurations, which
the declared **completion** of the preparation manufactures. The declared
completion flip-test measures how load-bearing that is: rebuilt on the bare
Householder completion of the *same* preparation vector, the base's holonomy
group order is **1 at every setting** and the defect is **the identity** — the
geometry vanishes. The group is a function of the base's declared data,
completion included; the geometry is a property of the species.

**Unit verdict:** `GEN-STRUCTURE-REPRODUCES`, at the committed finite scope, at
the declared admission scope, per coordinate — with the computed differences
between the two bases reported beside it and folded into nothing.

---

## 1. The question, and what it is asked of

The transport unit measured, on one committed base, that lawful transport
between declared contexts is path-dependent; that the group the loops generate
is the Klein four-group; that it has two sources, one of them the preparation's
failure to intertwine under the wing exchange; and that half of it lies outside
the base's own declared permutation scopes.

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
rather than a generality check. Every clause of the species is *measured* on the
constructed operators in §2 and gated, not asserted.

**Its flesh must be genuinely different.** Not a re-parameterisation: a
different system dimension, a different number of outcomes, a different
arithmetic, a different preparation. §8 tabulates the two bases coordinate by
coordinate and gates that they differ where they must.

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

Wing $A$ is the pair $(s_A, p_A)$ and wing $B$ the pair $(s_B, p_B)$.

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
measured, not assumed: the projectors are measured orthonormal, the outcome
shift map is measured **injective**, and every declared local leg is measured
equal, entry by entry, to that sum — which is what makes the pointer value at
the final division event a **record** of the outcome.

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
gluing rule of §3 admit **one** permutation rather than two, and hence what makes
the base's full-leg identifications exist at all. It is a species requirement,
not a result; §7.2 measures what happens without it, and the answer is that the
whole geometry disappears.

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
survives the $j_0$ filter where the cycles do not. The scope is measured
**closed under composition**, so it is a group and not a list. The wing exchange
$W$ — which moves the system pair **and** the pointer pair together — is
measured to factorise as $X_S \cdot X_P$, the system-only and pointer-only
exchanges, and that factorisation is measured rather than assumed.

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
The reduced condition and three further properties are recomputed *from the
delivered rows themselves*: that no enumerated path traverses one link twice in
succession, that every path is a genuine walk ending at the node it declares,
that the graph is connected by union-find over its links, and that the cycle rank
is Euler's with that measured component count.

The matched table pairs only paths sharing **both** endpoints, so every contrast
is read at matched coordinates; and the read time is inside the L datum, so two
law data read at different checkpoints are measured never to compare equal — a
count gated at zero over every pair of the declared nodes at every setting.

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
| the twisted comparator | GP-E, GP-F | **another permutation** |

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

**The negative control has teeth.** Replacing one identification of the
canonical loop by the wing exchange, at a coordinate where the base itself
supplies the identity, produces a matrix that is **not even a signed
permutation** at the four settings whose genuine loops are all flat, and a
different permutation at the two symmetric ones. The instrument can see a twist;
the flatness readings above are therefore not vacuous.

**The direction flip-test passes on every loop that carries an edge list** —
**14** loops — each re-traversed with the direction convention flipped yielding
the **inverse** permutation. Coverage is stated: the twisted comparator is the
canonical loop with one link overwritten and carries no edge list of its own, so
**the negative control is not flip-tested**.

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
measured *absent* at the other four — so the gate is a measurement that comes out
both ways on one base, and not a fixture of the instrument.

A disclosure belongs with the count. At the **declared base point** every closed
path's holonomy is a signed permutation — the count that are not is measured
**0** at every setting — so nothing is dropped from §6.2's value set. Over
*all* base points that is no longer true: **600 of 2,820** closed paths at GP-E
and **820 of 2,820** at GP-F have holonomies that are not signed permutations,
and for those the declared invariant is simply undefined. That is a fact about
the connection, and it is printed rather than filtered away.

### 6.2 P2 — the group, computed

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
| $D$, **the preparation-defect element** | **45** | 2 |
| $W\!\cdot\!D$ | 9 | 2 |

$D$ is *not* the system-only wing exchange (27 fixed points), *not* the
pointer-only wing exchange (27), and *not* $W$ (9). The first base's group is
$\{1, W, X, WX\}$ with $X$ and $WX$ the two **halves** of its wing exchange; base
G's group is the same abstract group built from a different second generator.
Reproducing the Klein four-group was not required, and the isomorphism type
reproducing while the elements differ is the unit's sharpest single finding.

### 6.3 P3 — two curvature sources

**Source (i), identification multiplicity.** Six coordinates — GP-E and GP-F at
$t \in \{0,1,3\}$ — carry **two** distinct admitted maps, the full-leg rule's
identity and the realized rule's wing exchange. The bigon each forms has
holonomy exactly the wing exchange (§5). Everywhere else the multiplicity is at
most one.

**Source (ii), the preparation's swap-defect, isolated.** Multiplicity is
measured **not necessary**: the single-rule sub-connections, in which every
coordinate carries at most one admitted map, are built and enumerated
separately.

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
$W$.

**P3 holds, with both sources exhibited.**

### 6.4 P4 — the preparation-defect is a group element

The defect's permutation, computed in §6.3 from the declared preparation and the
wing exchange, is tested against the group computed in §6.2 from the enumerated
closed paths — **two independent computations, compared as tuples and never as
names**.

| setting | group order | $D$ is an element |
|---|---|---|
| GP-A … GP-D | 1 | **no** |
| GP-E, GP-F | 4 | **yes** |

The second row is what makes the first a measurement: where the group is trivial
the defect is measured *not* to belong to it. **P4 holds.**

### 6.5 P5 — non-principality

Membership of **every** holonomy element in **every** declared and admitted
collection, computed:

| element | declared scope (162) | declared extension (216) | admitted (2) | admitted extension (8) |
|---|---|---|---|---|
| the identity | yes | yes | yes | yes |
| the wing exchange $W$ | yes | yes | yes | yes |
| **$D$** | **no** | **no** | **no** | **no** |
| **$W\!\cdot\!D$** | **no** | **no** | **no** | **no** |

**Two of the four** elements lie outside every declared collection, at both
settings whose group is nontrivial, and **zero of one** at the four where it is
trivial. Every *link* of this connection is a transport the base admits; the
*group those links generate around loops* is not a subgroup of the base's own
isomorphisms. **P5 holds** — the connection is not principal for base G's
certified relabellings either.

For the record, and measured: the two halves of base G's wing exchange, $X_S$
and $X_P$, are also outside the declared scope, whose wing flag always moves the
system pair and the pointer pair together — but on this base neither of them is
in the holonomy group. The escape is real and its witnesses are different ones.

---

## 7. The gauge layer, and the two declaration flip-tests

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
loops whose sign moves under the checkpoint subgroup. The self-test's cache-hit
count is gated at **zero** against **85,760** measured misses, so the bypass is
a measured fact and not an absence. The tested set is fixed by **declaration** —
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
| identification links per setting | 3 / 3 / 3 / 3 / **5** / **5** (declared: 3 / 3 / 3 / 3 / 7 / 7) |
| **holonomy group order per setting** | **1, 1, 1, 1, 1, 1** |
| the preparation's swap-defect | **the identity**, 81 fixed points |

**The geometry vanishes.** With the exchange-symmetric completion the wing
exchange satisfies the full-leg rule too, so that rule no longer admits
uniquely and its links are refused where the multiplicity would have arisen;
and the Householder built from an exchange-invariant $\psi$ is
exchange-equivariant, so the preparation manufactures no defect at all. Both
sources of §6.3 are removed by one declaration.

This is reported and folded into **no verdict**. What it licenses is the scope
statement: every result of this unit stands at the **declared** completion, and
the completion is part of the base's declaration exactly as the preparation
vector is.

### 7.3 The admission scope

Every admission search that feeds a link, a profile or a verdict runs over the
**2** elements of the declared 162-element scope that survive the $j_0$ filter.
The declared 216-element extension, which admits **8**, is searched with the same
four-clause predicate, and the cells where the two disagree are printed in the
receipt. Because admission is by uniqueness, a wider scope can *refuse* a link
the narrower one draws; the settings at which the canonical loop would cease to
exist are named there. The measurement is folded into no verdict.

---

## 8. The two bases, coordinate by coordinate

The first base's numbers are read from its committed terminal receipt and
**anchored exit-1** (A08–A12). No object of its model is imported.

| coordinate | first base | base G |
|---|---|---|
| carrier | 36 | **81** |
| system dimension per wing | 2 | **3** |
| outcomes per measurement | 2 | **3** |
| arithmetic | the quartic field $\mathbb{Q}(\cos \pi/8)$ | **the rationals $\mathbb{Q}$** |
| preparation vector under the wing exchange | anti-invariant (the singlet) | **invariant** |
| preparation Schmidt rank | 2 | **3** |
| declared relabelling scope | 72 | **162** |
| settings | 6 | 6 |
| symmetric settings | 2 | 2 |
| admitted after the $j_0$ filter | 2 | 2 |
| admitted at the extension | 8 | 8 |
| total reduced paths | 34,024 | 34,024 |
| path pairs sharing both endpoints | 4,972,096 | 4,972,096 |
| holonomy group order at a symmetric setting | 4 | 4 |
| holonomy group structure | the Klein four-group | the Klein four-group |
| value set closed at the declared bound | yes | yes |
| elements outside every declared collection | 2 | 2 |
| realized-rule sub-connection: closed paths | 18 | 18 |
| realized-rule sub-connection: group order | 2 | 2 |
| **the preparation-defect element** | **a half of the wing exchange** | **neither half, 45 fixed points** |
| **the defect is one half of the wing exchange** | **yes** | **no** |

Of the twenty-one compared coordinates, **nine** are measured different and
**twelve** measured the same. The differences are the flesh; the agreements are
the geometry.

Two agreements deserve a word rather than a claim. The path counts and pair
counts agree because the two bases' path **graphs** are isomorphic — same node
set, same link structure — which follows from the admission tables of §3 being
the same shape, not from any deeper coincidence; they are counts of combinatorics
that both bases happen to share, and no significance is attached to them beyond
that. The **holonomy class counts** at the symmetric settings agree the same way
and for the same reason — 82 identity, 86 $W$, 90 $D$, 106 $W\!D$ on base G, and
the same four numbers on the first base against its own $\{1, W, X, WX\}$ —
because the group is Klein-four in both and the word structure of the loops is
fixed by the graph.

---

## 9. The verdict

The decision rule is pre-registered and the verdict is derived from the five
pattern gates and from nothing else: `GEN-STRUCTURE-ABSENT` if P1 fails;
`GEN-STRUCTURE-REPRODUCES` if all five pattern gates pass;
`GEN-STRUCTURE-VARIES-⟨list⟩`, with the failing patterns named in the tag,
otherwise; `GEN-BLOCKED-AT-⟨object⟩` where a census cannot be posed.

All five pattern gates pass.

> **`GEN-STRUCTURE-REPRODUCES`**, at the committed finite scope, at the declared
> admission scope, per coordinate.

Derived: the transport geometry is **not** an artifact of the first committed
base. On a second base of the same species and none of the same flesh — a qutrit
system, three outcomes, rational arithmetic, a different and
oppositely-symmetric preparation, a different completion, a larger relabelling
scope — a nontrivial holonomy group exists; it is the Klein four-group, measured
closed; it has the same two sources, with multiplicity again sufficient and
again measured not necessary; the preparation's swap-defect is again an element
of it; and half of it again escapes the base's own declared isomorphisms.

And the computed difference, reported beside the verdict and folded into
nothing: **the group's elements are a function of the base's declared data**.
The first base's second generator is a half of its wing exchange; base G's is a
permutation with 45 fixed points that the declared completion manufactures. The
pattern is the theory's; the elements are the base's.

---

## 10. Scope and non-claims

1. **No claim about nature.** Every result is a statement about declared finite
   models, a declared gauge and declared finite search scopes.
2. **Two bases are two bases.** This unit measures that the patterns survive one
   change of flesh. It does not establish that they survive every change, and no
   quantifier over bases is entered anywhere.
3. **The completion is a declaration, and it is load-bearing.** §7.2 measures
   that the same preparation vector with a different orthogonal completion
   carries no geometry at all. Every result here stands at the declared
   completion.
4. **The admission criterion is a declaration** — uniqueness of the admitted
   transport — and it is scope-dependent; the alternative scope is searched and
   disclosed, not silently taken.
5. **Every claim is per coordinate.** The read time is a coordinate of the node
   and of the L datum; the matched table pairs only paths sharing both endpoints.
6. **The path space is bounded** at $L_{\max}=8$, the canonical loop's own
   length, and every count is a count at that bound. The holonomy *value set* is
   a value set at that bound; the group it generates is computed separately by
   closure, and the two are measured equal here rather than assumed to be.
7. **The species is a declaration of this unit**, and its clauses are measured
   on the constructed operators rather than asserted: two wings with commuting
   local legs, a preparation, records at the final division event, exact
   orthogonality everywhere.
8. **The switching sweep is complete** at every setting over every declared loop
   that carries an edge list, and the checkpoint subgroup is swept complete as
   well. One clause of that sweep is analytically forced and is reported as a
   disclosure, not as a measurement.
9. **The negative control is not flip-tested**, because it carries no edge list
   of its own; that coverage gap is stated at the claim.
10. **Nothing is claimed about locality, topology, causality, spacetime, fields,
    QFT or gravity.** "Holonomy", "connection", "corridor" and "arena" are
    operational vocabulary for declared finite objects, and no continuum,
    curvature or geometric interpretation is entered.
11. **Nothing of the first base's model is imported.** Only its committed
    receipt's reported numbers are read, and they are anchored exit-1 so that a
    drift in either kills the run.

---

## 11. The receipt

`v13/code/gen_generality_exact.py` → `gen_generality_output.txt` +
`gen_generality_receipt.json`.

- **Anchors:** 12, exit-1-only. Seven are **self-anchors against this unit's own
  pinned base declaration** — the three rotation matrices entry by entry, the
  preparation vector as the first column of the completion, the full $9\times 9$
  completion matrix entry by entry, the orthogonality of every declared operator
  at every (setting, frame), the commutation of the two wings at every declared
  pair of rotations, the injectivity of the record shift, and the unit-norm and
  orthogonality of the completion. Five are **external anchors against the
  committed terminal receipt of the first base** — its group order, its value-set
  size and closure, its elements outside every declared scope at both symmetric
  settings, its total reduced paths and path pairs, and its realized-rule
  sub-connection's closed-path count and group order. That the first kind is
  self-anchoring is a disclosure, not a secret: a second base has no prior
  committed numbers to reuse, and what those anchors buy is that no constructor
  can drift from the printed declaration without the run dying.
- **Gates:** 28, of which 25 are must-pass and 3 are declared disclosures (the
  analytically-forced permutation-part clause, the admission-scope search, and
  the completion flip-test — none of them carrying a verdict). The falsification
  census below covers 24 of the 25 — the twenty-fifth is the census's own gate.
- **The path space:** 34,024 reduced paths; 4,972,096 path pairs; every count
  computed from the enumeration and none typed. Four properties of the delivered
  rows are recomputed from the rows themselves.
- **Mutants:** 26, each run to completion, **26 of 26 died** — each measured to
  exit 1 and to falsify at least one named gate or anchor. **The set of must-pass
  gates that no mutant falsifies is EMPTY**, at denominator **24**. Of those 24,
  **23 are falsified by a mutant that perturbs a computation** and one —
  `GEN-VOCABULARY` — only by a waiver, because every branch that emits a verdict
  builds it from a pre-registered template; both denominators are printed and the
  gate that sits between them is named. Each mutant declares its kind and the
  split is counted from the declaration: **23 perturb a computation and 3 are
  waivers.** A waiver overwrites a gate's computed predicate after the fact, so
  what it measures is that the predicate carries the exit code — not that the
  gate would catch a computational defect, and the two are not claimed to be the
  same thing. The one gate excluded from the denominator is the census's own,
  which does not run inside a mutant.
- **No gate predicate references mutant identity.** Every mutation is injected
  where the computation happens; an AST sweep of the instrument measures the
  number of `MUTANT != …` comparisons anywhere in its source to be **zero**, and
  the `exempt-lax` mutant registers one and dies at that gate.
- **The suite covers** the base declaration (`anchor-completion`, `anchor-rot`,
  `anchor-record`, `completion-Q`), the reused first-base values (`anchor-nt`),
  the alignment profile (`prefix-lax`), the path space (`path-collapse`,
  `reduce-lax`), the holonomy count (`label-collapse`, `hol-basepoint`), the
  gauge layer (`gauge-sign`, `gauge-subsample`), the fresh-evaluation layer
  (`memo-lax`), the freeze and its gate order (`freeze-lax`, `order-lax`), the
  read-time coordinate (`readtime-conflate`), the defect's composition order
  (`defect-order`), two direction conventions (`orient-flip`, `flip-lax`), the
  identification admissibility (`id-lax`), the declared scopes (`scope-lax`,
  `scope-gen`), exactness (`float-lax`), gate integrity (`exempt-lax`), and
  waivers of the positive control, the flip-test and the verdict vocabulary.
- **Exactness:** `fractions.Fraction` throughout. Every declared operator of base
  G has rational entries and is exactly orthogonal over $\mathbb{Q}$, so equality
  of matrices is equality of exact rationals and no tolerance exists anywhere in
  the instrument. An AST sweep finds no float literal and no call to `float`, and
  a runtime sweep finds no float in any value that reached a gate or an anchor.
- **Determinism:** no wall-clock value enters the receipt or the rendered output;
  two delivery-mode runs were executed and their artifacts are byte-identical.

---

## Appendix: deviations

**D1 — the second base is this unit's own construction, so its anchors are
mostly self-anchors.** A generality check on a new base has no prior committed
numbers of its own to reproduce. The response is to *pin the base as data* — the
rotation matrices and the full $9\times 9$ completion typed in the instrument —
and to anchor every constructor against the pinned declaration entry by entry,
so the anchors catch constructor drift rather than reuse drift. Five genuine
external anchors are carried against the first base's committed receipt, and the
split is printed.

**D2 — the completion was chosen so that the base is of the species, and the
alternative is measured rather than hidden.** The full-leg gluing rule admits by
uniqueness, so a preparation whose completion has an exchange-symmetric Born
shadow admits *two* permutations and its links are refused: such a base has no
full-leg identifications and no canonical loop, and the five patterns cannot be
posed on it at all. The declared completion $V = H\cdot Q$ satisfies the species
requirement; the bare Householder does not. Rather than leave that choice
implicit, the instrument rebuilds the entire base on the alternative and reports
what it measures (§7.2): the holonomy group order becomes 1 at every setting and
the preparation-defect becomes the identity. The choice is a species
requirement, its consequence is measured, and every verdict is scoped to the
declared completion.

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
without the closure measurement beside it.

**D5 — the agreement of the path counts and the holonomy class counts between the
two bases is combinatorial, and is stated as such.** 34,024 paths, 4,972,096
pairs, and the class counts 82 / 86 / 90 / 106 agree because the two bases'
path graphs are isomorphic and both groups are Klein-four. That is reported as a
consequence of the graph, not as an independent confirmation, in §8.

**D6 — the field's own products are memoised inside the switching sweep.** The
sweep spends its time on structure rather than on recomputing identical exact
rational products. Nothing is approximated and nothing is cached at the level of
a transported value: every quantity the self-test measures is rebuilt from the
link variables on every switching, with the transported-value cache bypassed and
its hit count gated at zero. The memoising product routine is measured against
the plain one on **every** swept instance, since an all-positive switching is an
exact equality test between them.

**D7 — the path length bound is a declaration.** $L_{\max} = 2\cdot\text{NLEGS}+2$
is computed from the model as the canonical loop's own length, so the pin's loop
lies inside the enumerated space; every count is a count at that bound and no
claim is entered about longer paths.

**D8 — no Lean.** As the pin states.
