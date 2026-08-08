# The State-Side Curvature

## One commutator law, and the preparation inside it: a sweep on base G at fixed declarations

**Status:** `TERMINAL (v13 PSI)` — panel #254–#256, adjudicated #257 ACCEPT-WITH-MAJOR-REPAIRS, repair P-1..P-5 verified byte-identical and conferred terminal at v13 LOG #265. The third witness pair (psi-S1, psi-N1) is panel-unseen and flagged for successors.
panel, unreviewed. Freeze-on-delivery in force.

**Date:** 2026-08-08

**Frozen pin:** `v13/note-psi-curvature-pin.md`, commit `095c6f7`
(sha `c12749532eae`)

**Immutable base:** `1426984` — the generality-check unit TERMINAL (v13 LOG #222).
No object of GEN's model is imported anywhere in this unit: the only thing read
from it is its committed receipt, which is hash-pinned, and every number taken
out of it is anchored exit-1.

**Receipts:** `v13/code/psi_curvature_exact.py` → `psi_curvature_output.txt`,
`psi_curvature_receipt.json`

**Lean:** NONE.

---

## Abstract

The generality check earned a holonomy group on a second base and then measured
where it came from. Both of its curvature sources turned out to be
declaration-side: the identification multiplicity is a consequence of the
declared gluing rules, and the completion's non-equivariance defect obeys
$D = (\Sigma Q^{\mathsf T}\Sigma Q)\otimes I_9$, in which the preparation vector
$\psi$ cancels identically. That unit registered the obvious next question as an
open one, its §11.12: **does any curvature carried by the state rather than by a
declaration exist anywhere in this theory?**

This unit answers it, and the answer turns out to be one line of algebra with a
measurement attached to every clause.

**One law.** The wing exchange $P_W$ is measured to be an involution, so the
four-factor defect **is** the group commutator of the exchange with the
preparation leg,

$$D(\psi) \;=\; [\,P_W,\;u(\psi)\,] \;=\; P_W\,u(\psi)^{-1}P_W\,u(\psi),
\qquad u(\psi) = V(\psi)\otimes I_9 .$$

The commutator splits off the pointer pair and leaves
$\delta(V) := [\Sigma, V]$ at $9\times9$; and $\delta$ is a **1-cocycle** for the
right-conjugation action, $\delta(XY) = \delta(Y)\,Y^{-1}\delta(X)\,Y$, so the
declared factorisation $V = H(\psi)\,Q$ expands as

$$\delta(HQ) \;=\; \delta(Q)\cdot Q^{-1}\delta\bigl(H(\psi)\bigr)\,Q ,$$

which **is** the $\psi$-law, with $D_{\text{GEN}} = \delta(Q)$ the declaration
factor and $E(\psi) = \delta(H(\psi))$ the state factor. Existence, group order,
forcing and state-modulation are its four readings; every vanishing condition is
a **centralizer** condition. The identity is gated at all **11** members and on
**300** randomised triples $(\Sigma, X, Y)$ drawn from a generator seeded from
the declared data alone, with **0** deviations, and the order in the law is
measured rather than assumed: the mirror-ordered expansion computes
$\delta(YX)$ and gives a different answer at **6** of the 11 members and at
**300** of the 300 triples. The residual is owned and measured: refactoring the
same $V$ as $Q\cdot H'$ is an equally valid expansion whose state factor differs
at those same **6** members, so the world/description split is
**factorisation-relative** — what is canonical is the commutator, not the split.

**The preparation inside the law.** On base G, with $Q$ held **fixed** at GEN's
pinned value and every other declaration — the two gluing rules, the six
settings, the two frames, the four checkpoints, the read times, the 162-element
relabelling scope and its two admitted elements — held identical, a declared
**eleven-member family of preparations** `[SAMP]` is swept, and the
preparation's two channels do different jobs.

**The Born shadow fixes the arena.** Every clause of the four-clause admission
predicate reads Born-level data alone, and that is measured rather than assumed:
the nine members sharing an exchange-symmetric Born shadow have **identical
admission tables at all 48 cells**, identical graphs and identical loop
spaces — **34,024** reduced paths, **5,864** closed paths, **760** loops based at
the declared base point — while the two members whose Born shadow is not
exchange-symmetric lose the realized rule's identifications at **8** cells and
collapse onto the flat baseline the four asymmetric settings already carry.

**The sign structure carries the curvature.** An exhaustive census of all
**55** unordered pairs of the family measures **5** pairs at a *fixed Born
shadow* — every Born-level object the model builds identical: the Born shadow of
$\psi$, the Born shadow of the completion entry by entry, the Born-level key of
every declared and realized leg, the law at every node, the whole 48-cell
admission table, the whole loop space. **Two** of the five agree on every common
loop. **Three** do not:

| fixed-Born-shadow pair | common loops at GP-E | Born holonomy differs | $\langle\psi_a\vert\psi_b\rangle$ |
|---|---|---|---|
| $(\psi_G,\ \psi_{N1})$ | 364 | **206** | $1/9$ |
| $(\psi_{S1},\ \psi_{N1})$ | 364 | **206** | $-1/9$ |
| $(\psi_{I4},\ \psi_{N2})$ | 364 | **196** | $\mathbf{0}$ |

The third is between two states that are exactly **orthogonal** and yet
identical in every Born-level object the model contains. At the first, **2** of
the 206 loops are **flat at one preparation and not flat at the other**. What
$\psi$ does to GEN's own invariant is measured in its positive form: the
readable holonomy collapses from the reference's **Klein four-group** (4 values,
fixed-configuration counts $\{9,9,45,81\}$) to a group of **order 2** at both
$\psi_{N1}$ and $\psi_{N2}$, with 206 and 196 loops leaving the readable class
entirely.

**What "Born-level indistinguishable" means here, and what it does not.** It
means indistinguishable by the entrywise squares **in the declared basis**,
which is the only Born-level datum any declaration of this model reads. It is
not a claim about quantum mechanics: $\langle\psi_G\vert\psi_{N1}\rangle = 1/9$,
so a projective measurement outside the declared settings separates those two
preparations in a single shot with probability $80/81$, and the orthogonal pair
is separated with probability $1$.

The mechanism of the invisibility is measured too, and it says where such
witnesses live: the **interference width** of the declared leg sequence — the
largest number of nonzero paths $j_0\to i$ through the first $t$ legs — is
**1** at the reference, so every declared amplitude there is a single product
and the declared law is a function of $\lvert\psi\rvert$ alone. The set of
census members whose law layer moves under some sign flip is measured to
**coincide** with the set of census members of width $\ge 2$.

The controls are the pin's. Positive: at GEN's pinned preparation this
independently rebuilt instrument reproduces GEN's terminal admission table cell
for cell, its link and path counts, its Klein four-group and its defect —
**56** anchors against the hash-pinned committed receipt, all passed. Negative,
with teeth: two alternative declared transpositions move the holonomy by exactly
the amount the dihedral reading predicts — order **6** and non-abelian at one,
**flat with the identifications refused** at the other. Both of those
transpositions lie inside the sub-family GEN rebuilt exhaustively, so the
control is a **reproduction of committed measurements** as well as a prediction
test, and all ten of its readings are anchored exit-1 as such. Nothing in
this unit is an out-of-sample prediction and nothing claims to be.

**Unit verdict:** `PSI-CURVATURE-EXISTS-AT-FIXED-BORN-SHADOW`, at the committed
finite scope, at the declared preparation family, at the declared completion
form and its pinned $Q$, per coordinate. The verdict string **and its
qualifier** are re-derived inside the verdict's own gate from the recorded
tables and gated against the string that was emitted; three computation mutants
— a branch-order swap, an emptied witness input and a suppressed qualifier —
each make the derivation fail and each dies there.

---

## 1. The question, and what it is asked of

The transport geometry of this programme has, until now, been made of
declarations. The links are drawn by declared rules over a declared scope; the
loops live in a declared path space; and the generality check measured that the
one element of the holonomy group which is not the base's own wing exchange — the
completion's non-equivariance defect — is manufactured by the declared
transposition $Q$ alone. Its §8.1 theorem is explicit: for $V = H\cdot Q$ with an
exchange-**invariant** preparation vector, the Householder cancels identically
and $\psi$ does not appear in $D$ at all.

That theorem was measured on a family of five preparation vectors, four
exchange-invariant and one not, and what it measured was the **defect**. It did
not ask what the **holonomy** does; it did not ask whether the loops carrying the
defect still exist when $\psi$ moves; and it did not ask what happens on the
whole of the non-invariant locus. GEN registered the gap itself, as its §11.12:

> Whether any curvature carried by the *state* rather than by a declaration
> exists anywhere in this theory is not decided here.

This unit is that question, posed as an instrument and frozen before its fixtures
were computed. The instrument is a sweep: hold every declaration fixed, vary the
preparation, and compare the resulting geometries **at matched coordinates**.

Three things make the comparison meaningful, and each is a declaration of this
unit.

**The completion form is fixed, and so is its $Q$.** A preparation does not
determine its own orthogonal completion, and GEN measured that the completion is
the parameter which selects the isomorphism type of the group. If $\psi$ and $Q$
both moved, nothing could be attributed to either. So every member of the family
is completed by the same declared construction $V = H(\psi)\cdot Q$ with the
**same** declared transposition $Q$ — GEN's pinned one — and $Q$ is typed in the
instrument and anchored.

**The comparison is at matched coordinates.** Every link of every graph carries a
$\psi$-independent name, $(\text{leg}, \text{frame}, \text{leg})$ or
$(\text{id}, \text{checkpoint}, \text{rule})$, so a loop is a sequence of
(name, direction) pairs and "the same loop at two preparations" is a statement
about names, not about positions in a list that moved. A loop is **common** to two
members when both graphs contain every link it names. The matched table is the
primary object and every contrast in this paper is derived from it.

**The holonomy is read twice, and both readings are gauge-invariant.** The
declared switching group assigns a sign to each link, so a closed loop's matrix is
defined only up to a global $\pm1$. This unit therefore reads the **permutation
part** of the closed-loop link product — GEN's own invariant, undefined when the
product is not a signed permutation — and the **Born shadow** of the holonomy
matrix, its entrywise squares, which is invariant under the same action and is
**always defined**. The Born shadow is the primary comparator; §9 self-tests both
under the switching action itself. The second reading is not a second
*measurement* at the members where the witnesses live, and §6.4 says exactly why.

---

## 2. The declarations

Everything in this section is a **declaration**, recorded before any transport
quantity is evaluated. The instrument records the freeze as its first gate with
the transport-datum evaluation counter measured at zero, and a separate gate
measures that every declaration gate sits strictly before the first transport gate
in the receipt's own gate order. That records the ordering **within one
execution**; it is not, and is not offered as, proof that the family was fixed
before any fixture truth was seen, which no in-run measurement can establish.

### 2.1 Base G, carried unchanged and rebuilt natively

| coordinate | value |
|---|---|
| configurations $(s_A, s_B, p_A, p_B)$ | **81** |
| system per wing | a qutrit, $s_X\in\{0,1,2\}$ |
| pointer per wing | three states, $0$ = ready |
| index | $i = ((s_A\cdot3+s_B)\cdot3+p_A)\cdot3+p_B$; $j_0 = 0$ |
| measurements | $R_0, R_1, R_2$ from the integer quaternions $(1,0,0,0)$, $(2,1,0,0)$, $(3,0,0,2)$ |
| settings | six: GP-A … GP-F, **2** of them symmetric |
| frames | $F_1 = (\text{prep}, A, B)$, $F_2 = (\text{prep}, B, A)$ |
| legs per frame / checkpoints | **3** / **4**, division events $\{0,3\}$ |
| nodes per setting / path bound | **8** / **8** |
| declared relabelling scope | **162**, measured closed under composition over all **26,244** compositions |
| admitted after the $j_0$ filter | **2**: the identity and the wing exchange |

Nothing of GEN's module is imported. The three rotation matrices are
reconstructed from their quaternions by Euler–Rodrigues and anchored against the
pinned matrices entry by entry; each local leg is measured equal, entry by entry,
to a sum assembled from the **pinned** rotations and an **independently declared**
shift table, so a perturbation of either moves one side of the comparison and not
the other; every rotation is measured exactly orthogonal over $\mathbb{Q}$, the
record shift injective, and the two wings' legs commuting at every declared pair.

### 2.2 The completion form, the transposition held fixed, and what anchors it

The preparation leg is $U_{\text{prep}} = V\otimes I_9$ with

$$V \;=\; H(\psi)\cdot Q,$$

$H(\psi) = I - 2ww^{\mathsf T}/(w^{\mathsf T}w)$ the Householder reflection of
$w = \psi - e_{(0,0)}$, which carries $e_{(0,0)}$ exactly to $\psi$, and $Q$ the
**declared transposition** of the system-pair basis states $\lvert 0,1\rangle$ and
$\lvert 0,2\rangle$, i.e. $Q = [0,2,1,3,4,5,6,7,8]$ on the nine system-pair labels.

$Q$ is the same for every member of the family. It is typed in the instrument and
anchored, and for GEN's own $\psi$ the constructed $V$ is compared entry by entry
against a $9\times9$ matrix **typed in this same file** — **81** anchors. Those
81 are **self-anchors**, and they are labelled as such at every one of them:
GEN's committed receipt does not carry $V$'s entries at all, so external
anchoring of $V$ was not available. What a self-anchor buys is that no
constructor can drift from the printed declaration without the run dying; it
does not establish that this unit's completion *is* GEN's rather than a faithful
rebuild of it, and no such inference is drawn.

The completion's provenance does have one genuinely external anchor, and it is
taken. GEN's receipt records the declared completion's own **defect
permutation**, $\delta(Q) = [0,2,1,6,4,5,3,7,8]$ on the nine system-pair labels.
This unit computes $\delta(Q) = \sigma Q^{-1}\sigma Q$ from the declared
transposition alone and anchors it against GEN's recorded value **entry by
entry** — **9** external anchors — and separately measures that the same
permutation is what the $9\times9$ commutator matrix $[\Sigma, Q]$ carries, by a
second route.

### 2.3 The preparation family, declared as data  `[SAMP]`

**The family is a declaration, not a sample of anything.** It is not drawn at
random, it is not exhaustive over the preparations of base G, and no property of
it is extrapolated to preparations outside it. Every **measured** quantifier in
this paper that ranges over preparations ranges over these eleven, over the 48
members of the exhaustive sign-flip census of §7.2, and over the exhaustive
55-member census of their unordered pairs, and nowhere else. The one quantifier
that ranges further is the characterisation in §7.1, which is licensed by
**proof** rather than by the family and is labelled there. The tag is carried
here, in the receipt, and at §11.3.

Eleven declared rational unit vectors on the nine system-pair basis states. Only
the name, the coefficients and the role are declared; the norm, the Schmidt rank,
the support, the exchange behaviour and the Born shadow's symmetry are all
**computed** by the instrument, never typed.

| member | $\lVert\psi\rVert^2$ | Schmidt rank | support | exchange-invariant | Born shadow exchange-symmetric | interference width | role |
|---|---|---|---|---|---|---|---|
| **psi-G** | 1 | **3** | 3 | yes | yes | **1** | GEN's pinned preparation, carried unchanged |
| psi-I1 | 1 | **1** | 4 | yes | yes | 2 | an exchange-invariant product state $v\otimes v$, $v=(\tfrac35,\tfrac45,0)$ |
| psi-I2 | 1 | **2** | 2 | yes | yes | 1 | invariant, on the diagonal, unequal weights |
| psi-I3 | 1 | **3** | 3 | yes | yes | 2 | invariant, on a different support |
| psi-I4 | 1 | **2** | 4 | yes | yes | 2 | invariant, four equal weights |
| psi-S1 | 1 | 3 | 3 | yes | yes | 1 | psi-G with the sign flipped at a $\Sigma$-**fixed** index |
| psi-S2 | 1 | 2 | 2 | yes | yes | 1 | psi-I2 with the sign flipped at a $\Sigma$-**fixed** index |
| **psi-N1** | 1 | 3 | 3 | **no** | yes | **1** | psi-G with the sign flipped at **one index of a $\Sigma$-pair** |
| psi-N2 | 1 | 2 | 4 | **no** | yes | 2 | anti-invariant; the same Born shadow as psi-I4 |
| psi-N3 | 1 | 2 | 2 | **no** | **no** | 1 | non-invariant, Born shadow also asymmetric |
| psi-N4 | 1 | 1 | 2 | **no** | **no** | 2 | a non-invariant product state, Born-asymmetric |

Explicitly, in the basis $(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)$:

$$\psi_G = \tfrac23\lvert 0,1\rangle + \tfrac23\lvert 1,0\rangle + \tfrac13\lvert 2,2\rangle,
\qquad
\psi_{N1} = \tfrac23\lvert 0,1\rangle - \tfrac23\lvert 1,0\rangle + \tfrac13\lvert 2,2\rangle,$$

$$\psi_{I1} = \tfrac{9}{25}\lvert 0,0\rangle + \tfrac{12}{25}\lvert 0,1\rangle + \tfrac{12}{25}\lvert 1,0\rangle + \tfrac{16}{25}\lvert 1,1\rangle,
\qquad
\psi_{I2} = \tfrac45\lvert 0,0\rangle + \tfrac35\lvert 1,1\rangle,$$

$$\psi_{I3} = \tfrac13\lvert 0,0\rangle + \tfrac23\lvert 1,2\rangle + \tfrac23\lvert 2,1\rangle,
\qquad
\psi_{I4} = \tfrac12\bigl(\lvert 0,1\rangle + \lvert 1,0\rangle + \lvert 0,2\rangle + \lvert 2,0\rangle\bigr),$$

$$\psi_{S1} = \tfrac23\lvert 0,1\rangle + \tfrac23\lvert 1,0\rangle - \tfrac13\lvert 2,2\rangle,
\qquad
\psi_{S2} = \tfrac45\lvert 0,0\rangle - \tfrac35\lvert 1,1\rangle,$$

$$\psi_{N2} = \tfrac12\bigl(\lvert 0,1\rangle - \lvert 1,0\rangle + \lvert 0,2\rangle - \lvert 2,0\rangle\bigr),
\qquad
\psi_{N3} = \tfrac35\lvert 0,1\rangle + \tfrac45\lvert 1,0\rangle,
\qquad
\psi_{N4} = \tfrac35\lvert 0,0\rangle + \tfrac45\lvert 0,1\rangle.$$

Sizes computed from the declaration: family size **11**; **7** exchange-invariant
at Schmidt ranks **{1, 2, 3}**; **4** exchange-non-invariant; **9** whose Born
shadow is exchange-symmetric; **11** distinct coefficient vectors. Every member is
measured to be an exact rational unit vector whose completion $V = H(\psi)\cdot Q$
is exactly orthogonal with $\psi$ as its first column, so every member is a
legitimate preparation of the very same declared form.

The family is built to make the comparison decide something. `psi-I1` … `psi-I4`
vary the Schmidt rank across its whole available range while staying invariant.
`psi-S1` and `psi-S2` are sign flips at $\Sigma$-**fixed** indices, which leave the
state invariant — the in-family negative controls. `psi-N1` and `psi-N2` are sign
flips across a $\Sigma$-**pair**, which do not. `psi-N3` and `psi-N4` break the
Born shadow's symmetry as well.

### 2.4 The arena (declared, sizes computed)

| coordinate | declaration |
|---|---|
| **boundary** | the final division event, checkpoint 3 |
| **family** | the six declared settings and the eleven declared preparations |
| **law** | the exact Born law of the declared leg sequence, read at the node's declared read time |
| **state** | $p(0) = \delta_{j_0}$ |
| **arena** | the declared 162-element relabelling scope; the **2** of its elements surviving the $j_0$ filter — the identity and the wing exchange — over which every admission search runs |

The arena is measured **identical for every member**, since $\psi$ is the only
thing the sweep varies. The declared 216-element extension admits **8** and is
carried as a declaration only.

### 2.5 The two gluing rules

Two corridor-bound rules, each a four-clause admissibility predicate applied in
order — the $j_0$ filter, the rule's own leg list matched order-free at the Born
level, the occupied-set clause, the exact-law clause — with a link drawn only where
the rule admits **uniquely**. **FULL** matches the full declared legs; **REALIZED**
matches each leg restricted to the configurations the process actually occupies
before and after it.

Every clause of that predicate reads **Born-level data only**. That is not a
remark; it is the hinge of the whole unit, and §5 turns it into a measurement.

---

## 3. The admission tables, per member

Measured at all $6\times4\times2 = 48$ cells for every member, with the cell
count itself computed from the declared setting, checkpoint and rule lists and
gated against every member's table and against the comparison that reads it:

| member | cells where FULL draws | cells where REALIZED draws |
|---|---|---|
| psi-G, psi-I1 … psi-I4, psi-S1, psi-S2, psi-N1, psi-N2 | **18** | **8** |
| psi-N3, psi-N4 | **18** | **0** |

The nine members with an exchange-symmetric Born shadow reproduce GEN's table
exactly: the full-leg rule draws the identity at $t\in\{0,1,3\}$ at every setting
and nothing at $t=2$; the realized rule draws the **wing exchange** at all four
checkpoints at the two symmetric settings and nothing at the four asymmetric ones.
The two Born-asymmetric members lose every realized-rule identification, at
**8** cells, and gain none.

The mechanism is visible in the predicate. At $t=1$ both frames' law is the Born
shadow of $\psi$, and the wing exchange acts on the system pair by $\Sigma$; the
exact-law clause therefore admits it exactly when $\lvert\psi_{ab}\rvert =
\lvert\psi_{ba}\rvert$. The realized rule's identifications are the ones that carry
the defect, so **the Born shadow's symmetry is what decides whether the
geometry-bearing loops exist at all**.

---

## 4. The loop spaces, per member

Enumerated at the declared length bound $L_{\max} = 8$, from every node, with every
size computed and none typed:

| member | links per setting | reduced paths | closed paths | loops based at $F_1@t{=}0$ |
|---|---|---|---|---|
| psi-G, psi-I1 … psi-I4, psi-S1, psi-S2, psi-N1, psi-N2 | 9, 9, 9, 9, **13**, **13** | **34,024** | **5,864** | **760** |
| psi-N3, psi-N4 | 9, 9, 9, 9, **9**, **9** | **2,532** | **336** | **48** |

At the symmetric setting GP-E the first group carries **364** based loops and the
second **8**. Four properties are recomputed *from the delivered rows themselves*:
that no delivered loop traverses one link twice in immediate succession, that
every delivered loop is a genuine walk returning to the node it declares, that the
delivered rows are as many as the counted loops, and that each graph is connected
by union-find over its own links with the declared cycle rank equal to Euler's.

The first row's counts are GEN's own, and they are anchored as such: 34,024
reduced paths and the per-setting link, path, closed-path and based-loop counts are
all anchored exit-1 against the committed GEN receipt.

---

## 5. The comparison, at matched coordinates

### 5.1 Does the preparation change which loops exist?

The admission tables of all eleven members are compared **cell by cell**, in the
number of admitted permutations and in the permutation each rule draws, with the
comparison itself measured to have ranged over all 48 declared cells for every
member:

| member | admission cells that move | loop space |
|---|---|---|
| psi-I1, psi-I2, psi-I3, psi-I4, psi-S1, psi-S2, psi-N1, psi-N2 | **0 of 48** | identical to the reference at every setting |
| psi-N3, psi-N4 | **8 of 48** | 13 → 9 links, 364 → 8 based loops at GP-E |

**Yes, for two of the eleven, and the eight cells are named.** They are exactly the
realized rule at $t\in\{0,1,2,3\}$ at GP-E and GP-F — the cells whose admission
turns on the Born shadow's exchange symmetry. Both halves are clauses of the
gate's own predicate, so the reading comes out both ways on one family.

What happens there is a **collapse onto the flat baseline**, not a reshaping. The
cells that move are the whole of the realized rule at the two symmetric settings,
and what is left is the connection the four asymmetric settings already carry:
13 links become 9, 364 based loops become 8, and the geometry-bearing
identifications are destroyed outright rather than rearranged.

### 5.2 Does a common loop's holonomy change?

For the nine members whose loop space is identical, every one of the 364 based
loops at GP-E is **common**, and the comparison is total rather than partial.
Read at matched coordinates — same setting, same base point, same sequence of named
links with directions, same read times:

| member | common loops at GP-E | Born holonomy differs | readability flips | permutation parts both defined and different | flat at the reference, not here |
|---|---|---|---|---|---|
| psi-I1 | 364 | **0** | 0 | 0 | 0 |
| psi-I2 | 364 | **0** | 0 | 0 | 0 |
| psi-I3 | 364 | **0** | 0 | 0 | 0 |
| psi-I4 | 364 | **0** | 0 | 0 | 0 |
| psi-S1 | 364 | **0** | 0 | 0 | 0 |
| psi-S2 | 364 | **0** | 0 | 0 | 0 |
| **psi-N1** | 364 | **206** | **206** | **0** | **2** |
| **psi-N2** | 364 | **196** | **196** | **0** | 0 |
| psi-N3 | 8 | 0 | 0 | 0 | 0 |
| psi-N4 | 8 | 0 | 0 | 0 | 0 |

**Yes.** The column that used to read "permutation part differs" is a
**readability-flip** count and is named as one: every one of those 206 rows is a
row where the permutation part is a signed permutation at the reference and is
**undefined** at the other member, and the count of common loops whose
permutation parts are **both defined and different** is measured to be **0**
everywhere, at every member and every setting. The permutation part is therefore
not an independent second reading at the members where the witnesses live; the
Born shadow is what carries the comparison, and §6.4 states the positive form of
what the permutation reading does say.

The witness pair is $(\psi_G, \psi_{N1})$, and it is as clean as this question
admits, because the Born-level identity of the two is **measured** and not
argued (§9): the same $\lvert\psi_i\rvert$, the same $\lvert V_{ij}\rvert$
entry by entry, the same canonical Born-level key of every declared and every
realized leg at every (setting, frame) — that is, the same input to every clause
of the admission predicate — hence the same occupied sets, the same exact laws at
every node, the same admission table at all 48 cells, the same graph and the same
loop space. And on 206 of their 364 common loops the holonomy differs.

They differ in one sign of one coefficient in the declared basis, and that is the
whole of the difference the model's Born-level objects can see. It is **not** a
small difference between the states: $\langle\psi_G\mid\psi_{N1}\rangle = 1/9$,
so a projective measurement in another basis separates them in a single shot with
probability $80/81$. "Born-level indistinguishable" here means indistinguishable
by the entrywise squares in **this declared basis**, which is the only Born-level
datum any declaration of this model reads; it is not a claim that the two
preparations are operationally indistinguishable in quantum mechanics, and no such
claim is made anywhere in this paper. It is worth noting in the same breath that
$\langle\psi_G\mid\psi_{N3}\rangle = 14/15$ — `psi-N3` is far *closer* to the
reference than the witness is, and it is `psi-N3` that collapses the arena.

Note the shape of the table, because it contains its own control. Exactly two
members of the family are indistinguishable from the reference at the Born level
of the declared basis: `psi-S1`, a sign flip at a $\Sigma$-**fixed** index, which
stays exchange-invariant, and `psi-N1`, a sign flip across a $\Sigma$-**pair**,
which does not. They sit at identical Born-level coordinates. `psi-S1` agrees with
the reference on all 364 loops; `psi-N1` differs on 206. And the six
exchange-**invariant** members agree with the reference on every common loop
whatever their Schmidt rank, support or Born shadow. That is the dependence law
showing itself before §6 derives it.

### 5.3 The witnesses, named

Two witnesses are extracted and printed, and each one's two holonomies are rebuilt
by an **independent route** — a plain left-to-right product of freshly constructed
link variables, sharing no interning, no step memo and no value cache with the
enumeration that produced the row — with the rebuilds measured to reproduce the
rows *and* to differ from each other. The independence is of the accumulation,
the interning and the caches; the link variables themselves are the base's own
declared data, which any two routes must share, and that is what the claim covers.

**The shortest differing loop**, length four, at GP-E:

$$\bigl(\text{id}@t{=}0,\ \text{FULL}\bigr)^{-1}\ \to\
\bigl(\text{leg},F_2,1\bigr)\ \to\
\bigl(\text{id}@t{=}1,\ \text{REAL}\bigr)\ \to\
\bigl(\text{leg},F_1,1\bigr)^{-1}$$

— the bigon that leaves $F_1$ at the initial division event along the full-leg
rule's identity, runs frame 2's preparation leg, returns along the realized rule's
wing exchange at $t=1$, and comes back down frame 1's preparation leg. Its
holonomy at $\psi_G$ is a signed permutation; at $\psi_{N1}$ it is **not a signed
permutation at all**. Both facts are switching-invariant, so the difference is
gauge-invariant twice over: in the always-defined Born shadow, and in the
readability predicate itself.

**The flat-to-non-flat witness**, length eight, at GP-E: the realized prep bigon
traversed **twice**. At $\psi_G$ its holonomy is exactly the identity — the defect
is an involution, so the doubled bigon is flat. At $\psi_{N1}$ it is not. **A loop
that is flat at one preparation and not flat at another, with every declaration
identical and the loop present in both graphs**, is the sharpest form the witness
can take, and at $\psi_{N1}$ there are **2** such loops among the 364. This
witness is rebuilt by the same independent route as the other, with the rebuild
measured to be exactly the identity at the reference and not the identity at
$\psi_{N1}$.

### 5.4 The witness-pair census, exhaustive

The existence claim does not rest on the reference member. All
$\binom{11}{2} = 55$ unordered pairs of the family are compared — the number of
pairs computed from the declared family size and gated — on **six** Born-level
equalities: the Born shadow of $\psi$; the Born shadow of the completion $V$
entry by entry; the Born-level canonical key of every declared and every realized
leg at every (setting, frame); the exact law at every node of every setting; the
whole 48-cell admission table; the whole loop space. A pair passing all six is
**at a fixed Born shadow**. Measured: **5** such pairs, of which **3** carry a
common loop whose Born holonomy differs and **2** agree on every common loop.

| pair | fixed Born shadow | common loops at GP-E | Born holonomy differs | $\langle\psi_a\vert\psi_b\rangle$ | one-shot separation |
|---|---|---|---|---|---|
| $(\psi_G, \psi_{S1})$ | yes | 364 | 0 | $7/9$ | $32/81$ |
| $(\psi_{I2}, \psi_{S2})$ | yes | 364 | 0 | $7/25$ | $576/625$ |
| $(\psi_G, \psi_{N1})$ | yes | 364 | **206** | $1/9$ | $80/81$ |
| $(\psi_{S1}, \psi_{N1})$ | yes | 364 | **206** | $-1/9$ | $80/81$ |
| $(\psi_{I4}, \psi_{N2})$ | yes | 364 | **196** | $\mathbf 0$ | $1$ |

The last row is the sharpest form the phenomenon takes in this family: two states
that are **exactly orthogonal** — perfectly distinguishable in one shot by a
measurement outside the declared settings — and identical in every Born-level
object the model builds, at Schmidt rank 2 and on a different support from the
reference pair, with 196 of their 364 common loops carrying different holonomy.
That pair, and the pair $(\psi_{S1}, \psi_{N1})$, are what make the existence
claim independent of the inherited reference member.

---

## 6. The one law

### 6.1 The defect is a commutator, and $\delta$ is a cocycle

$P_W$ is measured to be an involution — and to equal the product of the
independently declared system-only and pointer-only wing exchanges, which is a
comparator built from data other than $P_W$'s own constructor. Therefore the
four-factor product that GEN and this unit both call the non-equivariance defect
**is** the group commutator:

$$D(\psi) \;=\; P_W\,U_{\text{prep}}^{-1}\,P_W\,U_{\text{prep}}
\;=\;\bigl[\,P_W,\ u(\psi)\,\bigr],
\qquad u(\psi) = V(\psi)\otimes I_9 .$$

The wing exchange moves the system pair and the pointer pair together, so
$P_W = \Sigma\otimes\Sigma$; the preparation leg acts on the system pair alone;
the commutator's pointer factor is $\Sigma I\Sigma I = I$ and cancels. Measured
entry by entry at all **11** members, the $81\times81$ commutator equals

$$\delta(V)\otimes I_9, \qquad \delta(X) \;:=\; [\,\Sigma,\ X\,] \;=\;
\Sigma X^{-1}\Sigma X .$$

**$\delta$ is a 1-cocycle** for the right-conjugation action:

$$\delta(XY) \;=\; \delta(Y)\cdot Y^{-1}\delta(X)\,Y .$$

Given the measured $\Sigma^2 = I$ this is forced by algebra for any invertible
$X$ and $Y$ — one line: $\Sigma Y^{-1}\Sigma Y\cdot Y^{-1}\Sigma X^{-1}\Sigma XY
= \Sigma Y^{-1}X^{-1}\Sigma XY = \delta(XY)$ — and it is recorded as a
disclosure rather than advertised as a discovery. What is **not** forced is the
order, and that is measured: the mirror-ordered expansion
$\delta(X)\,X^{-1}\delta(Y)\,X$ computes $\delta(YX)$, and it is measured to give
a **different** answer at **6** of the 11 members and at **300** of the 300
randomised triples.

Instantiating the cocycle at the declared factorisation $V = H(\psi)\,Q$ gives
the whole $\psi$-law in one step:

$$\boxed{\ \delta\bigl(H(\psi)\,Q\bigr) \;=\; \delta(Q)\cdot Q^{-1}\,
\delta\bigl(H(\psi)\bigr)\,Q\ }$$

with $D_{\text{GEN}} = \delta(Q) = \Sigma Q^{\mathsf T}\Sigma Q$ the declaration
factor and $E(\psi) = \delta(H(\psi)) = \Sigma H\Sigma H$ the state factor — the
second equality because $H(\psi)$ is measured to be an involution at all eleven
members, so $H^{-1} = H$. Every factor here is $9\times9$; the tensor with the
pointer identity is applied once, to the product:

$$D(\psi) \;=\; \bigl(D_{\text{GEN}}^{\,9}\cdot Q^{\mathsf T}E(\psi)\,Q\bigr)
\otimes I_9 .$$

**The randomised gate.** The identity is checked on **300** triples
$(\Sigma, X, Y)$ with $X$ and $Y$ exactly orthogonal rational $9\times9$
matrices — products of signed permutations, Givens rotations from declared
Pythagorean triples and Householder reflections of declared rational unit
vectors — drawn from a generator seeded by the SHA-256 of the **declared data
alone**: the family's names and exact coefficients, the pinned transposition and
the exchange. No wall-clock value and no operating-system entropy enters, so two
runs draw the same sequence. Measured: **300** of 300 draws exactly orthogonal,
**0** deviations from the identity, **300** triples where the mirror order gives
a different answer, **300** with $\delta(X)\neq I$ — the sweep is not vacuous in
either direction.

### 6.2 The four readings

Everything this unit reports is a reading of that one law.

**EXISTENCE.** Curvature at a declaration exists exactly when the commutator does
not vanish, and the vanishing condition is a **centralizer** condition:
$D(\psi) = I \iff V\in C(\Sigma)$. Measured at all eleven members, both
directions, **0** mismatches.

**GROUP ORDER.** The based holonomy group's order is twice the order of the
commutator $\delta(Q)$, and $1$ with the identifications themselves refused where
$\delta(Q) = I$. Measured at all three declared transpositions:

| declared $Q$ | $\operatorname{ord}\delta(Q)$ | the reading predicts | measured group order at GP-E |
|---|---|---|---|
| the pinned $Q$ | **2** | 4 | **4** |
| Q-negA | **3** | 6 | **6** |
| Q-negB | **1** | 1, links refused | **1**, links refused |

The permutation $\delta(Q)$ is read by two routes — off the $9\times9$ commutator
matrix and off the label formula $\sigma q^{-1}\sigma q$ — and the two are
measured to agree at all three.

**FORCING.** When the state factor lies in the centraliser —
$H(\psi)\in C(\Sigma)$, equivalently $\psi$ exchange-invariant — the cocycle's
second factor is the identity and the commutator is $\delta(Q)$ alone: the
completion's declared $Q$ determines the defect and $\psi$ cancels. That is GEN's
§8.1 theorem, as a corollary of the cocycle, and it holds at exactly the seven
invariant members and no others.

**STATE-MODULATION.** Off that locus, $Q^{-1}\delta(H(\psi))\,Q$ is what the
preparation contributes, and it is the whole of it. $E(\psi) = I$ if and only if
$H(\psi)\in C(\Sigma)$, measured at all eleven members in both directions.

The three centralizer readings — $E = I \iff H\in C(\Sigma)$;
$D_{\text{GEN}} = I \iff Q\in C(\Sigma)$; $D(\psi) = I \iff V\in C(\Sigma)$ —
are measured with **0** mismatches, and they are the same condition in three
variables.

### 6.3 The residual: the split is factorisation-relative

$D(\psi)$ depends on the completion $V$ and on nothing else. The **split** of it
into a declaration factor and a state factor does not.

Refactor the same $V$ as $Q\cdot H'$ with $H' = Q^{\mathsf T}HQ$ — measured to be
the same completion, entry by entry. The cocycle expands it equally validly the
other way round,

$$\delta(Q\,H') \;=\; \delta(H')\cdot H'^{-1}\delta(Q)\,H' ,$$

measured to reproduce $\delta(V)$ at all eleven members. But its state factor
$E'(\psi) = [\Sigma, H']$ is measured **different** from $E(\psi)$ at **6** of
the eleven — `psi-G`, `psi-I1`, `psi-N1`, `psi-N3`, `psi-N4`, `psi-S1` — and it
coincides at the others, which is why a single example would not have found it.

So "the curvature's $\psi$-part is $E(\psi)$" is a statement **given the declared
completion form** $V = H(\psi)\cdot Q$. The world/description split is
factorisation-relative; what is canonical is the commutator, not its factors.
Every claim in this paper about $E(\psi)$ is a claim at the declared
factorisation and is scoped there.

### 6.4 What $\psi$ does to GEN's own invariant

GEN's declared invariant is the **permutation part** of the closed-loop link
product, undefined where the product is not a signed permutation. Applied at the
members where this unit's witnesses live, it does not permute the group's
elements — it removes the defect from the class in which it is defined at all.
Measured at GP-E:

| member | based loops | readable | readable values | closed | fixed configurations |
|---|---|---|---|---|---|
| psi-G (measured identical at all seven invariant members) | 364 | 364 | **4** | yes | $\{9, 9, 45, 81\}$ — the Klein four-group |
| **psi-N1** | 364 | 158 | **2** | yes | $\{9, 81\}$ |
| **psi-N2** | 364 | 168 | **2** | yes | $\{9, 81\}$ |

**The readable holonomy collapses from order 4 to order 2**, with **206** and
**196** loops leaving the readable class entirely. That is the positive statement
behind §5.2's readability-flip column, it is gated, and it is why this unit
carries the always-defined Born shadow as its primary comparator rather than
filtering the unreadable loops away — which would have hidden the finding
altogether.

One further fact belongs beside the law, and it is stated as measured rather
than as folklore. $H(\psi)$ is the symmetric orthogonal **involution** of this
construction, at all eleven members. $E(\psi)$ is **orthogonal** at all eleven —
$E^{\mathsf T} = E^{-1}$ by construction — but it is an involution, equivalently
symmetric, at only **8** of the eleven: the seven invariant members, where it is
the identity, together with `psi-N2`. At `psi-N1`, `psi-N3` and `psi-N4` it is
neither. Conjugating $\Sigma$ by a Householder generically leaves the
signed-permutation class, and that is why $D$ off the invariant locus is measured
not to be a signed permutation at all.

---

## 7. The law at the family, and the sign-flip census

### 7.1 The $\psi$-law, measured member by member

**Theorem (the $\psi$-law, gated).** Let $\Sigma$ be the exchange of the two labels
of the system pair, $Q$ the declared transposition, $H(\psi)$ the Householder of
$w = \psi - e_{(0,0)}$ and $V = H(\psi)Q$. Then

$$D(\psi)\;=\;\bigl(\Sigma Q^{\mathsf T}\,H\Sigma H\,Q\bigr)\otimes I_9
\;=\;\bigl(D_{\text{GEN}}^{\,9}\cdot Q^{\mathsf T}E(\psi)\,Q\bigr)\otimes I_9 ,
\qquad E(\psi) = \Sigma H(\psi)\Sigma H(\psi),$$

and $E(\psi) = I$ **if and only if** $\psi$ is exchange-invariant (for
$\psi \neq e_{(0,0)}$).

*Proof.* §6.1, in one line, from the cocycle. For the characterisation,
$E(\psi) = I \iff H\Sigma = \Sigma H \iff$ the Householder of $\Sigma w$ is the
Householder of $w$ $\iff \Sigma w = \pm w$; and since $\Sigma e_{(0,0)} =
e_{(0,0)}$, $\Sigma w = w \iff \Sigma\psi = \psi$, while $\Sigma w = -w$ forces
$\psi = e_{(0,0)}$, which the family excludes. $\square$

This is the one quantifier in the paper that ranges beyond the declared
family — it is licensed by that proof, not by the eleven, and it is the only
one.

Both clauses are gated, and neither is left as algebra:

- **The law.** For every member of the family the $9\times9$ law tensored with the
  pointer identity is measured **equal, entry by entry**, to the direct
  $81\times81$ four-factor product built from that member's own preparation leg.
  The two evaluations differ in dimension, in operator decomposition ($H$ and $Q$
  separately against $V = HQ$ composed) and in inversion path, but they are
  related by the identity under test: they are two **routes to one identity**,
  not two independent computations of one number, and the paper does not trade
  on the stronger reading.
- **The characterisation, in both directions.** The list of members whose defect
  equals GEN's is measured to **coincide** with the list of exchange-invariant
  members: both are exactly `psi-G, psi-I1, psi-I2, psi-I3, psi-I4, psi-S1, psi-S2`.
  Neither inclusion is assumed.

Measured member by member:

| members | $E(\psi) = I$ | exchange-invariant | law reproduces the direct $81\times81$ | $D = D_{\text{GEN}}$ | $D$ is a signed permutation | $D$: fixed configurations, order |
|---|---|---|---|---|---|---|
| psi-G, psi-I1 … psi-I4, psi-S1, psi-S2 | **yes** | **yes** | yes | **yes** | yes | **45**, **2** |
| psi-N1, psi-N2, psi-N3, psi-N4 | **no** | **no** | yes | **no** | **no** | — |

The two "yes/no" columns coincide row for row, in both directions, and that
coincidence is the gate's own predicate rather than a table beside it.

### 7.2 The sign-flip census, and what it does and does not settle

The $\psi$-law says what the *defect* does. What the *holonomy* does at a fixed Born
shadow is settled by an exhaustive census, because the one remaining freedom inside
a fixed Born shadow is exactly the sign pattern.

For each declared exchange-invariant member, **every** sign pattern on its support
that fixes the initial coefficient is enumerated — the count computed by
enumeration and gated against the count the declared coefficient dictionaries
force — and each one is **rebuilt in full** at GP-E: new preparation, new
completion, new admission table, new graph, new enumeration, new based holonomy.

| quantity | value |
|---|---|
| members swept | **7** |
| sign patterns swept, exhaustively | **48** |
| patterns whose holonomy differs from the reference at GP-E | **26** |
| patterns whose holonomy agrees on every common loop at GP-E | **22** |
| patterns where agreement and exchange-invariance disagree | **0** |
| patterns that move a node law at some setting | **21** |
| patterns that move an admission cell at some setting | **8** |

Three things are measured at every one of the 48, at the declared setting GP-E.
The **Born shadow** of $\psi$ and of $V$ is unchanged by a sign pattern — by
algebra, since $V(\varepsilon\psi) = S\,H\,S\,Q$ with
$S = \operatorname{diag}(\varepsilon)$, and left or right multiplication by a
diagonal $\pm1$ and a column permutation preserve entrywise absolute values. At
GP-E both local legs are permutation matrices, so every downstream Born-level
datum — the occupied sets, the node laws at all four checkpoints, the Born key of
every declared and realized leg — is likewise unchanged, and the **loop space** is
therefore identical and every loop is common. Both of these are consequences of
the declaration rather than contingent measurements, and they are recorded as
such. Off GP-E the first does not follow: a local leg that is not a permutation
superposes distinct support entries of $\psi$, and **21** of the 48 patterns move
a node law at some setting while **8** of them move two admission cells at GP-F
— exactly `GP-F/t2/REAL` and `GP-F/t3/REAL`, so at GP-F their loop space is not
the reference's. The census's reading is a GP-E reading and is stated at that
scope. The one contingent measurement is the third: the **holonomy** agrees with
the reference on every common loop **if and only if** the flipped state is still
exchange-invariant.

The comparison target is the reference member throughout, and what makes that
legitimate is the separately measured fact of §5.2: every exchange-invariant
member of the family agrees with the reference on every common loop, whatever its
Schmidt rank, support or Born shadow. So "agrees with the reference" and "agrees
with its own unflipped member" coincide on the invariant locus, and the census
does not smuggle a second comparison in.

Part of the census's outcome is forced by §7.1's law: an invariant flip has
$E = I$, hence $D = D_{\text{GEN}}$, and the 22/26 split is exactly the split of
the 48 patterns into those constant on every $\Sigma$-pair of the support and
those not. What is *not* forced, and is what the census measures, is that the
loop holonomies — which involve $U_{\text{prep}}$ directly and not only $D$ —
agree across six invariant members with *different* completions, over the whole
common loop set, with zero exceptions.

That is the dependence law, stated at the level the evidence carries:

> At a fixed Born shadow, at the declared setting GP-E, the holonomy is a
> function of the preparation's sign pattern modulo the $\Sigma$-symmetric sign
> patterns; it moves exactly when the pattern differs across some $\Sigma$-pair of
> the support.

### 7.3 The mechanism of the invisibility: interference width

Why *can* $\psi_G$ and $\psi_{N1}$ have identical laws at all 48 nodes, when 21 of
the census's 48 sign patterns move a law somewhere?

The **interference width** of a member is the largest number of nonzero paths
$j_0 \to i$ through the first $t$ declared legs, over every setting, frame and
checkpoint. At width 1 every declared amplitude is a **single product**, so the
declared law is a function of $\lvert\psi\rvert$ alone and **cannot** see any
sign. At width 2 or more, a local leg superposes distinct support entries of
$\psi$ and a Born-shadow-preserving flip is generically visible in the law layer.
Measured across the family: width **1** at `psi-G`, `psi-I2`, `psi-S1`, `psi-S2`,
`psi-N1`, `psi-N3`; width **2** at `psi-I1`, `psi-I3`, `psi-I4`, `psi-N2`,
`psi-N4`.

And the prediction is exact, in both directions: the set of census members whose
law layer moves under some sign pattern — `psi-I1`, `psi-I3`, `psi-I4` — is
measured to **coincide** with the set of census members of width $\ge 2$, with
both sets and their complements non-empty. Width 2 is necessary and not
sufficient: `psi-N2`'s flip is a global sign on the one interfering block, which
is why the pair $(\psi_{I4},\psi_{N2})$ stays Born-level invisible.

So the fixed-Born-shadow witness exists at the reference **because $\psi_G$'s
support makes this model interference-free there**. There is no steering in that
— $\psi_G$ is inherited from GEN, not chosen — but the scope is narrower than
"the sign structure carries the curvature" would suggest on its own, and stating
the mechanism says exactly where such witnesses live.

### 7.4 What this does to GEN §8.1

GEN's $\psi$-independence theorem is not contradicted anywhere; it is **located**.
Its hypothesis — an exchange-invariant preparation — is measured here to be
exactly the centraliser condition under which the cocycle's state factor is
trivial, over a family that includes four further invariant members at three
Schmidt ranks and two invariant members obtained by sign flips. Inside that
hypothesis, this unit reproduces GEN's reading exactly: same defect, same group,
same class counts, at seven members.

What changes is the **scope of the conclusion**. GEN's §8.1 licensed "both
curvature sources on this base are declaration-side"; what the family licenses is
that both curvature sources are declaration-side **on the exchange-invariant
locus**, and that off it the geometry moves with a feature of the state that no
declaration in the model reads.

---

## 8. The two controls

### 8.1 The positive control: GEN's preparation reproduces GEN's unit

At `psi-G` this independently rebuilt instrument is anchored, exit-1, against the
committed GEN receipt — which is itself pinned by hash, with its sha256, its schema
string and the generator hash it records for its own instrument all anchored before
any number is read out of it.

| anchored against the committed GEN receipt | value |
|---|---|
| the admission table, all 48 cells, cell by cell in the permutation each rule draws | reproduced |
| links / reduced paths / closed paths / based loops, per setting | reproduced |
| based holonomy group order per setting | 1, 1, 1, 1, **4**, **4** |
| the value set at GP-E: size, closure at the declared bound, abelian, element orders | 4, closed, abelian, $\{1,2\}$ — **the Klein four-group** |
| the four elements' fixed configurations | $\{9, 9, 45, 81\}$ |
| the defect: order, fixed configurations | **2**, **45** |
| the declared completion's own defect permutation $\delta(Q)$, entry by entry | $[0,2,1,6,4,5,3,7,8]$ |

**56** anchors against GEN, all passed. If any of these had moved, the instrument
would be measuring something other than GEN's geometry and no comparison across
$\psi$ would mean anything.

### 8.2 The negative control: a prediction test that is also a reproduction

The pin requires that a **declaration** change move the holonomy by an amount
fixed in advance. Two alternative declared transpositions are run at the **same**
preparation `psi-G` with every other declaration untouched, and the dihedral
reading of §6.2 fixes the answer before the enumeration: a group of order $2n$
with $n = \operatorname{ord}\delta(Q)$, and order 1 with the links themselves
refused on the equivariant locus where $\delta(Q)$ is the identity.

| control | $Q$ | $\delta(Q)$ | the reading predicts | measured | abelian | identification links |
|---|---|---|---|---|---|---|
| the pinned $Q$ | $(0,1)\leftrightarrow(0,2)$ | order **2** | 4 | **4** | yes | 7 |
| **Q-negA** | $(0,1)\leftrightarrow(1,1)$ | order **3** | 6 | **6** | **no** | 7 |
| **Q-negB** | $(0,1)\leftrightarrow(1,0)$ | **the identity** | 1, links refused | **1** | yes | **5** |

Both compound predictions are met — to the number, to the abelian/non-abelian
distinction, and, on the equivariant locus, to the link refusal, which is in the
gate's own predicate and not merely printed beside it. The gate additionally
requires that the holonomy have actually **moved** from the pinned $Q$'s reading.
The instrument can be moved by a declaration, so its report that the state also
moves it is worth something.

**And it is a reproduction.** Both alternative transpositions are single
transpositions of the nine system-pair labels fixing the first, hence members of
the 28-member sub-family GEN rebuilt **exhaustively**, each a full rebuild. Their
group orders, abelianness, defect orders, identification-link counts — and the
dihedral reading's own prediction, including the $n = 1$ branch, which is
therefore anchored rather than typed into this instrument — are committed values,
and all **ten** of those readings are anchored exit-1 here against GEN's
receipt. The control is at once a prediction test and a reproduction of a
committed measurement. **It is not an out-of-sample prediction**, nothing in this
unit is, and no claim of one is made.

---

## 9. The gauge layer, the self-test and the flip-tests

**The switching self-test is complete at the declared setting.** The declared
switching group assigns one sign to each of the graph's 13 links at GP-E and is
swept **complete**, $2^{13} = 8{,}192$ per probe, over four declared probe loops at
two declared members; the **checkpoint subgroup** — the switchings induced by a sign
at each node, $2^{8-1} = 128$ — is swept complete beside it. The tested set is fixed
by **declaration**, in the order the probes are declared, and is never selected by
the verdicts under audit; the number of (member, probe) instances realized is
measured against the number declared, so a probe that silently failed to resolve
would shrink the sweep and be caught.

Measured: **66,560** exact matrix comparisons; **0** deviations from the global
scalar action; **0** loops whose signed-permutation readability moved under a
switching; **0** checkpoint switchings that failed to telescope; and the sweep is
measured **complete** at every probe, the universe size checked against $2^{L}$
for the graph's own measured link count $L$ rather than assumed. The Born shadow
of the holonomy — this unit's primary comparator — is measured invariant at every
one of the 66,560.

**The bypass is measured against a cache that is measured to work.** Every
holonomy in the sweep is rebuilt from the link variables with the value cache
bypassed, and the bypass is not a claim about an empty cache. Before the sweep
the cache is **primed** with the very keys the sweep will request — **8** entries
written, one per (member, probe), measured against the declared count — and a
second pass over those keys is measured to return the **8** stored values, so the
read path is measured to exist and to work. The sweep then requests a key that
**is** in the populated cache **65,544** times and its hit count is nevertheless
**zero** against **65,544** measured misses. A zero-hit count over zero lookups
would be vacuous; this one is 65,544 refusals to read a cache that had an answer.

**Two flip-tests.** The **direction flip-test** re-traverses every declared probe
loop with the direction convention flipped and measures the product of the two
matrices to be exactly the identity, at all **8** declared (member, probe)
instances. Its positive content is forced by algebra — the link variables are
measured orthogonal and the reverse traversal is the transpose — so what it
retains is instrument integrity, and the mutant that reads a reverse traversal
without transposing dies there.

The **bookkeeping-split flip-test** is the one with teeth, because this unit's two
transported objects divide exactly along Born data against sign data — and the
division is measured at the level where the invisibility is claimed, not one level
downstream.

The Born-level data the admission predicate actually keys on is compared directly:
the Born shadow of the **completion** $V$ entry by entry, and the canonical
Born-level key of **every declared leg and every realized leg** at every
(setting, frame). Those are measured to agree with the reference for **exactly**
the members that share the reference's Born shadow, neither more nor fewer — so
for those members no clause of the predicate has any input that differs at all.
The **law layer** is measured to agree at every node of every setting for exactly
the same members. And the members whose **amplitude layer** nevertheless disagrees
on a common loop are **named**: `psi-N1`.

The split is therefore not a story about the instrument but a measured fact about
it. Two members, `psi-S1` and `psi-N1`, are identical to the reference at the Born
level of the declared basis in every object the model builds; their law layers
agree; their amplitude layers do not both agree; and the one that parts company
is the one whose sign pattern is not constant across a $\Sigma$-pair.

---

## 10. The verdict

The decision rule is pre-registered: `PSI-CURVATURE-EXISTS` if a common loop's
holonomy is measured to differ between two preparations; otherwise
`PSI-PATH-SPACE-DEPENDENCE` if the loop space is measured to move while every
common loop agrees; otherwise `PSI-DECLARATION-ONLY`; and
`PSI-BLOCKED-AT-⟨object⟩` where the census cannot be posed.

> **`PSI-CURVATURE-EXISTS-AT-FIXED-BORN-SHADOW`**, at the committed finite scope,
> at the declared preparation family, at the declared completion form and its
> pinned $Q$, per coordinate.

**The whole string, its qualifier included, is derived inside the verdict's own
gate and gated against what was emitted.** The emitter applies the rule to the
measured booleans; the gate then re-derives the same string from the recorded
tables — the witness census's member list, the arena census's mover list, and the
witness-pair census's rows — by an evaluation that does not call the emitter and
reads none of its variables, and measures the two strings equal. The qualifier is
**not a literal**: `-AT-FIXED-BORN-SHADOW` is appended if and only if the
witness-pair census records at least one pair whose six Born-level equalities all
hold and whose common loops nevertheless differ in holonomy. Remove the witnesses
and the qualifier goes with them. Three **computation** mutants prove the
derivation can fail and each dies at that gate: `verdict-order` swaps the rule's
branch order, `verdict-nowitness` empties the witness input the emitter sees while
the recorded tables keep their measurements, and `verdict-qual` suppresses the
measured qualifier.

The qualifier is not decoration. It names where the witnesses live, and it is the
strongest place they could live: at a fixed Born shadow the arena, the admission
table, the loop space and the law layer are all **measured** identical, so nothing
about the comparison is left to argument. Each witness is a loop present in both
graphs, named identically in both, based at the same node, read at the same times,
with different holonomy. And it is scoped to what it means: "Born-level" is the
entrywise squares in the declared basis of this model, not operational
indistinguishability in quantum mechanics. The three witness pairs are made of
physically distinct preparations, separated in one shot with probability $80/81$,
$80/81$ and $1$ by measurements outside the declared settings.

**Beside it, folded into no verdict but reported as measured:** the phenomenon
`PSI-PATH-SPACE-DEPENDENCE` names also occurs in this family, at `psi-N3` and
`psi-N4`. The pre-registered outcome of that name is a conjunction — the loop
space moves **and** every common loop's holonomy is $\psi$-invariant — and this
family refutes the second conjunct, so it is not the verdict. But the phenomenon
is real here and the cells that move are printed. Its gate is named
`PSI-ARENA-MOVES` rather than after the outcome, so that a reader scanning the
receipt cannot mistake a passing gate for the verdict. The two phenomena are not
the same and are not confused: the Born shadow decides **which loops exist**, the
sign structure decides **what they carry**.

**What this answers.** GEN §11.12 asked whether any curvature carried by the state
rather than by a declaration exists anywhere in this theory. On this base, at this
completion form, at this pinned $Q$, over this family: **it does** — and the law
that carries it is one commutator, whose declaration factor and state factor are
the two values of a single cocycle.

---

## 11. Scope and non-claims

1. **No claim about nature.** Every result is a statement about declared finite
   models, a declared gauge and declared finite search scopes.
2. **One base, one completion form, one $Q$.** The sweep varies the preparation and
   nothing else. It does not establish that the phenomenon survives a change of
   base, of completion form, or of $Q$; the negative control varies $Q$ only to give
   the instrument teeth, and its readings are folded into no positive claim about
   other completions.
3. **Eleven preparations are eleven preparations `[SAMP]`.** The family is a
   declared family, not a random or exhaustive sample of the preparations of base
   G, and no quantifier over states is entered anywhere except the one licensed by
   the proof in §7.1. The exhaustive objects in the unit are the sign-flip census
   over every sign pattern of the seven declared invariant members that fixes the
   initial coefficient — 48 of them — and the census of all 55 unordered pairs of
   the family; what they decide, they decide there. The existence claim the verdict
   makes needs one witness pair at a fixed Born shadow and has **three**, measured
   by that pair census: $(\psi_G,\psi_{N1})$ and $(\psi_{S1},\psi_{N1})$, differing
   on 206 of 364 common loops, and $(\psi_{I4},\psi_{N2})$, differing on 196 —
   the last between two states that are orthogonal and yet identical in every
   Born-level object the model builds. The non-existence half of every gate is
   scoped to the declared family by construction.
4. **"Born-level indistinguishable" is a declared-basis statement.** It means
   indistinguishable by the entrywise squares of declared vectors in the declared
   basis fixed by §2.1's index map and listed at §2.3, which is the only
   Born-level datum any declaration of this model reads. In full quantum
   mechanics the sign structure it hides is measurable: the
   overlaps and one-shot separation probabilities of every witness pair are
   computed and printed. No claim of operational indistinguishability is made
   anywhere.
5. **The holonomy is read up to the switching action, and twice — but only one
   reading is a comparator at the witnesses.** The Born shadow is always defined
   and is the primary comparator; the permutation part is GEN's invariant and is
   undefined on the very loops where the witnesses live, so the count of common
   loops whose permutation parts are both defined and different is **0**. Both
   readings are self-tested under the switching action. No claim is made about any
   quantity that is not switching-invariant.
6. **The state factor is factorisation-relative.** $D(\psi)$ depends only on $V$;
   the split into $D_{\text{GEN}}$ and $E(\psi)$ depends on the declared
   factorisation $V = H(\psi)\cdot Q$, and $E'\neq E$ at 6 of the 11 members under
   the equally valid refactoring $V = Q\cdot H'$. Everything said about $E(\psi)$
   is said at the declared factorisation.
7. **The path space is bounded** at $L_{\max}=8$, the canonical loop's own length,
   and every count is a count at that bound.
8. **The admission criterion is a declaration** — uniqueness of the admitted
   transport over the declared 2-element admitted set — and it is scope-dependent.
9. **Every claim is per coordinate.** The read time is a coordinate of the node and
   of the law datum; the matched table pairs only loops sharing every coordinate;
   and the count of law data read at different checkpoints that nevertheless compare
   equal is gated at zero.
10. **Nothing is claimed about locality, topology, causality, spacetime, fields, QFT
    or gravity.** "Holonomy", "connection", "corridor" and "arena" are operational
    vocabulary for declared finite objects. "State", "preparation" and "Born shadow"
    are names for declared vectors and their entrywise squares.
11. **Nothing of GEN's model is imported.** Only its committed receipt is read; the
    file is hash-pinned and the numbers taken from it are anchored exit-1, so a
    drift in either kills the run.

---

## 12. The receipt

`v13/code/psi_curvature_exact.py` → `psi_curvature_output.txt` +
`psi_curvature_receipt.json`.

- **Anchors:** 165, exit-1-only. **109** are self-anchors against this unit's own
  pinned declaration of base G — the three rotation matrices entry by entry, the
  declared transposition $Q$, and the full $9\times9$ completion of the reference
  preparation entry by entry — and each one says so in its own source field.
  **56** are external anchors against the committed terminal receipt of the
  generality-check unit: three pin that receipt itself — its sha256, its schema
  string and the generator hash it records for its own instrument — before any
  value is read out of it; 30 carry the per-setting path-space and group readings;
  four carry the value set, the fixed configurations, the 48-cell admission table
  and the defect; **nine** carry the declared completion's own defect permutation
  entry by entry, which is the completion's one genuinely external anchor; and
  **ten** carry the negative control's two rebuilt completions, whose readings are
  committed values in GEN's exhaustive sub-family rebuild. That most of the anchors
  are self-anchors is a disclosure, not a secret: what they buy is that no
  constructor can drift from the printed declaration without the run dying, and
  they do not license any claim of identity with GEN's own objects.
- **Gates:** 26, every one must-pass; there are **no disclosures**, and every gate
  carries at least one declared falsifier. The falsification census runs against
  a denominator of **25** — it excludes itself, since the census gate does not
  exist inside a mutant and cannot be falsified by this mechanism at all.
- **Mutants:** 45, each run to completion, each measured to exit 1 and to falsify at
  least one named gate or anchor. **The set of must-pass gates that no mutant
  falsifies is EMPTY**, and both denominators are printed: the count falsified by
  some mutant, and the smaller count falsified by a mutant that perturbs a
  **computation**. Both counts are computed and printed by the census itself; the
  gates carried by a waiver alone are named, not averaged away, and after this
  repair they are `PSI-EXACT` and `PSI-NO-MUTANT-EXEMPTION` only — both because
  their input is this module's own source text, which freeze-on-delivery forbids
  editing. `PSI-VERDICT` is no longer among them: a verdict gate can be violated by
  a well-formed but **wrong** string, which is exactly the failure the runbook's
  §13 addendum names, and three computation mutants now reach it. Each mutant
  declares its kind and the split is counted from the declaration. A waiver
  overwrites a gate's computed predicate after the fact; what it measures is that
  the predicate carries the exit code, not that the gate would catch a
  computational defect, and the two are not claimed to be the same thing.
- **Cell completeness, on every census.** Each census's size is recomputed from
  the **declaration** — the declared setting, checkpoint and rule lists; the
  declared coefficient dictionaries; the declared family size — and compared
  against the size the census actually ran: 48 admission cells per member with a
  key set measured identical to the reference's, 48 cells ranged over by every
  member's cell-by-cell delta, 48 sign patterns, 55 pairs. Four computation
  mutants drop exactly one cell from the table, one cell from the comparison, half
  the sign-flip census and one pair, and each dies there.
- **No gate predicate references mutant identity**, measured as the headline says
  it: an AST sweep finds every `gate(...)` and `anchor(...)` call site, walks its
  argument expressions to any depth, and measures the number reaching the mutant
  flag to be **zero**; the four exemption forms are counted separately anywhere in
  the source, the one occurrence found lies outside every call site, and the `!=`
  count is gated at zero.
- **Independent comparators.** The record decomposition is rebuilt from the pinned
  rotations and an independently declared shift table. $P_W$ is compared against
  the product of the two independently declared half-exchanges. Each witness's two
  holonomies — the differing witness and the flat-to-non-flat witness alike — are
  rebuilt by a plain left-to-right product of freshly constructed link variables,
  sharing no interning, no step memo and no value cache with the enumeration that
  produced the row under audit; that independence is of the accumulation and the
  caches, and the link variables themselves are the base's own declared data,
  which any two routes share. The verdict's re-derivation inside its gate reads the
  recorded tables and does not call the emitter it audits.
- **The fresh-evaluation gate is measured, not vacuous.** The value cache is primed
  before the self-test with the **8** keys the self-test will request; the priming
  pass is measured to return all **8** stored values on its second visit; the sweep
  is measured to request a key already in the populated cache **65,544** times; and
  its hit count is gated at **zero** against **65,544** measured misses.
- **Exactness:** `fractions.Fraction` throughout. Every declared operator has
  rational entries and is exactly orthogonal over $\mathbb{Q}$, and every declared
  preparation is an exact rational unit vector, so equality of matrices is equality
  of exact rationals and no tolerance exists anywhere in the instrument. An AST
  sweep finds no float literal and no call to `float`, and a runtime sweep finds no
  float in any value that reached a gate or an anchor. The randomised sweep of
  §6.1 draws exactly orthogonal **rational** matrices and its generator is seeded
  from the declared data by SHA-256, so it introduces neither a float nor a
  nondeterminism.
- **Determinism:** no wall-clock value enters the receipt or the rendered output;
  two delivery-mode runs were executed and their artifacts are byte-identical.
- **A delivery run computes its exit code before it writes anything.** A
  delivery-mode run with any must-pass failure writes no artifact at all and says
  so on stderr, so a failing run can no longer overwrite a good artifact pair.

---

## Appendix: deviations

**D1 — "three further exchange-invariant states of differing Schmidt rank" is
satisfied at the ceiling the carrier allows.** A qutrit pair admits Schmidt ranks
1, 2 and 3 and no more, so "differing Schmidt rank" ranges over exactly three
values. The family carries **six** exchange-invariant members beyond the pinned one
— more than the pin's three — realising **all three** available ranks, and the rank
of each is computed by exact elimination over $\mathbb{Q}$ rather than typed. Two of
the six (`psi-S1`, `psi-S2`) are sign variants included deliberately: they are the
in-family negative controls that make §5.2's table a measurement rather than a
correlation with "was anything changed at all".

**D2 — the pin's "at least 3 exchange-non-invariant states" is met with four, and
they are chosen to span the two mechanisms.** `psi-N1` and `psi-N2` keep the Born
shadow exchange-symmetric and so keep the arena fixed; `psi-N3` and `psi-N4` break
it and so move the arena. Without both kinds the unit could not have separated
question (i) from question (ii), and the four are declared with that purpose stated.

**D3 — the negative control's second transposition refuses links as well as
flattening, and the branch that says so is anchored rather than typed.** `Q-negB`
lies on the exchange-equivariant locus, where GEN's §7.2 measured that the
full-leg rule admits two permutations at the symmetric settings and the links are
refused for want of uniqueness. The prediction tested there is therefore the
compound one — order 1 **with links refused** — and both halves are in the gate's
predicate. The instrument's own $n = 1 \Rightarrow 1$ branch is not left as a
typed special case: it is anchored exit-1 against the prediction GEN's receipt
itself records for that member of its exhaustive rebuild.

**D4 — the sign-flip census fixes the initial coefficient's sign.** A sign pattern
with $\varepsilon_{(0,0)} = -1$ does not act on the Householder by conjugation,
because $w = \psi - e_{(0,0)}$ is not homogeneous in $\psi$, so such a flip changes
the Born shadow of $V$ and leaves the fixed-Born-shadow comparison. The census is
exhaustive over the patterns that fix it — **48**, gated against the count the
declared coefficient dictionaries force — and the restriction is declared rather
than silent.

**D5 — the two census sweeps enumerate from the declared base point alone.** The
sign-flip census and the negative control read only the based loop set, so they
enumerate from $F_1@t{=}0$; the unit's own sweep enumerates from every node, which
is where the reduced-path and closed-path counts anchored against GEN come from.
The scope is printed in the receipt.

**D6 — the switching self-test is complete at one declared setting for two declared
members.** GP-E is the symmetric setting where the geometry lives, and the two
members are the reference pair. The sweep is complete over the full switching group
there — $2^{13}$ per probe — and over the full checkpoint subgroup; it is not
repeated at the other five settings, and that scope is stated at the claim rather
than implied by the word "complete".

**D7 — the holonomy is compared by its Born shadow first, and the permutation
part is not a second reading where the witnesses live.** GEN's declared
invariant is undefined on the very loops where this unit's witness lives, because
off the exchange-invariant locus the defect stops being a signed permutation.
Rather than filter those loops away — which would have hidden the finding — the
unit adds an always-defined comparator that is invariant under the same switching
action, self-tests it under that action, and reports both readings. But the
readings are not independent there: the count of common loops whose permutation
parts are both defined and different is measured to be **0**, so §5.2's second
column is a readability-flip count and is labelled as one, and §6.4 states the
positive form — the readable group collapses from order 4 to order 2.

**D8 — no Lean.** As the pin states.

**D9 — the "loop space" is counted at the declared bound and from the declared
node.** "The loop space, size computed" is delivered as four computed numbers per
member per setting — links, cycle rank, reduced paths from every node, closed paths
at every base point — plus the based loop count at the declared base point, which is
the object the holonomy comparison actually runs over. No claim is entered about
loops longer than $L_{\max} = 8$.

**D10 — the unit reports two pre-registered phenomena and only one verdict.** Both
`PSI-CURVATURE-EXISTS` and the phenomenon named by `PSI-PATH-SPACE-DEPENDENCE`
occur in this family. The pre-registered outcomes are exclusive by their own
wording — the second requires every common loop's holonomy to be $\psi$-invariant —
so the verdict is the first, and the second is reported beside it as a measured
co-finding with its own gate, its own printed cell list and a gate name
(`PSI-ARENA-MOVES`) that is not a verdict token. Nothing is folded. The
pre-registered vocabulary was written for a homogeneous family and the delivered
family is heterogeneous — curvature at `psi-N1` and `psi-N2`, arena movement at
`psi-N3` and `psi-N4`; the split is that fact, reported rather than resolved by
fiat.

**D11 — the second witness pair entered this unit from its own hostile panel, not
from a blind construction.** The pair $(\psi_{I4},\psi_{N2})$ was identified by a
reviewer of the delivered instrument, from members the family already declared.
It is not a new declaration and no member was added to reach it; what the repair
added is the **exhaustive** 55-pair census that finds all such pairs by
measurement rather than by nomination, and that census also recovered a third,
$(\psi_{S1},\psi_{N1})$, which no one had named. The provenance is recorded here
because the family, not the pair, is what was frozen before fixture truth.

**D12 — the verdict qualifier was a hard-coded literal in the first delivery, and
that is the #24 disease at the unit's central object.** The delivered
`-AT-FIXED-BORN-SHADOW` was a string appended unconditionally, so the verdict gate
could not fail on any in-vocabulary miscomputation: with every witness removed the
instrument still printed the qualified verdict and still exited zero. The runbook's
failure catalogue names this exact shape at ledger #24 — "hard-coded 6561 (true
729) survived unit + round" — and its §13 addendum, written at #234, forbids it by
name. It is owned here as the same disease, one unit after the addendum. The
repair derives the qualifier inside the gate from the witness-pair census and
proves the derivation can fail with three computation mutants; the adjudication
that ordered it also recorded the general form as precedent — **a verdict's
qualifiers are part of the verdict and must be computed, never typed.**

**D13 — the adjudicator's own earlier wording is corrected by name.** The v13
ledger entry #241, recording this unit's first delivery, called the Q-negA control
"the law's first successful out-of-sample prediction". That is wrong: both control
transpositions lie inside the 28-member sub-family GEN rebuilt exhaustively (GEN
§8.4), so both are reproductions of committed measurements at a moved declaration.
The reading is withdrawn here, the control is relabelled throughout §8.2, and the
committed values it reproduces are now anchored exit-1 — ten of them, including
the dihedral prediction itself. Nothing in this unit is an out-of-sample
prediction.

**D14 — one instrument-hygiene item disclosed in the first delivery is fixed
rather than disclosed again.** A delivery-mode run used to write its two artifacts
before computing its exit code, so a failing delivery run would have replaced a
good artifact pair with a failing one. The exit code is now computed first and a
failing delivery run writes nothing.

---

*Method note (one sentence, per programme convention): this paper is the repair
delivery ordered by the joint adjudication of the three-lens hostile panel at v13
LOG #257, and the physics it reports — the law, the witnesses, the census — is
the physics the panel reproduced on three independent instruments and did not
move.*
