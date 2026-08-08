# The State-Side Curvature

## Does the physical state contribute geometry? A preparation sweep on base G at fixed declarations

**Status:** `DELIVERED (v13 PSI)` — worker delivery, unreviewed. Freeze-on-delivery
in force.

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

This unit answers it. On base G, with the declared transposition $Q$ held **fixed**
at GEN's pinned value and every other declaration — the two gluing rules, the six
settings, the two frames, the four checkpoints, the read times, the 162-element
relabelling scope and its two admitted elements — held identical, a declared
**eleven-member family of preparations** is swept. It is declared as data in §2
before any transport quantity is evaluated, and the receipt's own gate order is
gated as the proof. Seven members are exchange-invariant, at Schmidt ranks
**1, 2 and 3**; four are not.

The sweep separates the preparation's two channels, and they turn out to do
different jobs.

**The Born shadow fixes the arena.** Every clause of the four-clause admission
predicate reads Born-level data alone, and that is measured rather than assumed:
the nine members sharing an exchange-symmetric Born shadow have **identical
admission tables at all 48 cells**, identical graphs and identical loop spaces —
**34,024** reduced paths, **5,864** closed paths, **760** loops based at the
declared base point — while the two members whose Born shadow is not
exchange-symmetric lose the realized rule's identifications at **8** cells and
collapse to a flat connection with **48** based loops. That is
`PSI-PATH-SPACE-DEPENDENCE` occurring inside the family, and it is reported as
what it is.

**The sign structure carries the curvature.** Exactly **two** members of the
family are measured to be indistinguishable from the reference by every
Born-level object the model contains — the same Born shadow of $\psi$, the same
Born shadow of the completion $V$ entry by entry, the same Born-level key of
every declared and every realized leg at every (setting, frame), the same law at
every node, the same admission table, the same loop space. One of them,
`psi-S1`, agrees with the reference on all **364** common loops. The other,
`psi-N1`, **differs on 206 of them**, and **2** of those loops are **flat at the
reference and not flat at it**. The two differ from the reference by a single
sign each; the sign that moves the geometry is the one that sits across a
$\Sigma$-pair.

The dependence is then characterised in both directions and exhaustively. The
GEN law generalises with a $\psi$-term, derived and gated against the direct
$81\times81$ computation at every member:

$$D(\psi) \;=\; D_{\text{GEN}}\cdot Q^{\mathsf T}E(\psi)\,Q,
\qquad E(\psi) \;=\; \Sigma\,H(\psi)\,\Sigma\,H(\psi),$$

with $E(\psi)$ measured to be the identity **exactly** on the exchange-invariant
locus and nowhere else. And over an exhaustive **48-member** sign-flip census the
holonomy agrees with the reference on every common loop **if and only if** the
flipped state is still exchange-invariant — **0** mismatches. GEN's
$\psi$-independence is therefore not a theorem of the theory but a theorem about
the exchange-invariant locus.

The controls are the pin's. Positive: at GEN's pinned preparation this
independently rebuilt instrument reproduces GEN's terminal admission table cell
for cell, its link and path counts, its Klein four-group and its defect —
**37** anchors against the hash-pinned committed receipt, all passed. Negative,
with teeth: two alternative declared transpositions move the holonomy by exactly
the amount GEN's dihedral law predicts — order **6** and non-abelian at one,
**flat** at the other.

**Unit verdict:** `PSI-CURVATURE-EXISTS-AT-FIXED-BORN-SHADOW`, at the committed
finite scope, at the declared preparation family, at the declared completion form
and its pinned $Q$, per coordinate.

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
**always defined**. The Born shadow is the primary comparator; §8 self-tests both
under the switching action itself.

---

## 2. The declarations

Everything in this section is a **declaration**, recorded before any transport
quantity is evaluated. The instrument records the freeze as its first gate with
the transport-datum evaluation counter measured at zero, and a separate gate
measures that every declaration gate sits strictly before the first transport gate
in the receipt's own gate order.

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

### 2.2 The completion form, and the transposition held fixed

The preparation leg is $U_{\text{prep}} = V\otimes I_9$ with

$$V \;=\; H(\psi)\cdot Q,$$

$H(\psi) = I - 2ww^{\mathsf T}/(w^{\mathsf T}w)$ the Householder reflection of
$w = \psi - e_{(0,0)}$, which carries $e_{(0,0)}$ exactly to $\psi$, and $Q$ the
**declared transposition** of the system-pair basis states $\lvert 0,1\rangle$ and
$\lvert 0,2\rangle$, i.e. $Q = [0,2,1,3,4,5,6,7,8]$ on the nine system-pair labels.

$Q$ is the same for every member of the family. It is typed in the instrument and
anchored, and for GEN's own $\psi$ the constructed $V$ is anchored entry by entry
against GEN's pinned $9\times9$ matrix — **81** anchors — so this unit's
completion of the reference member *is* GEN's completion and not a rebuild of it.

### 2.3 The preparation family, declared as data  `[SAMP]`

**The family is a declaration, not a sample of anything.** It is not drawn at
random, it is not exhaustive over the preparations of base G, and no property of
it is extrapolated to preparations outside it. Every quantifier in this paper
that ranges over preparations ranges over these eleven and over the 48 members of
the exhaustive sign-flip census of §6.2, and nowhere else. The tag is carried
here and repeated at §10.3.

Eleven declared rational unit vectors on the nine system-pair basis states. Only
the name, the coefficients and the role are declared; the norm, the Schmidt rank,
the support, the exchange behaviour and the Born shadow's symmetry are all
**computed** by the instrument, never typed.

| member | $\lVert\psi\rVert^2$ | Schmidt rank | support | exchange-invariant | Born shadow exchange-symmetric | role |
|---|---|---|---|---|---|---|
| **psi-G** | 1 | **3** | 3 | yes | yes | GEN's pinned preparation, carried unchanged |
| psi-I1 | 1 | **1** | 4 | yes | yes | an exchange-invariant product state $v\otimes v$, $v=(\tfrac35,\tfrac45,0)$ |
| psi-I2 | 1 | **2** | 2 | yes | yes | invariant, on the diagonal, unequal weights |
| psi-I3 | 1 | **3** | 3 | yes | yes | invariant, on a different support |
| psi-I4 | 1 | **2** | 4 | yes | yes | invariant, four equal weights |
| psi-S1 | 1 | 3 | 3 | yes | yes | psi-G with the sign flipped at a $\Sigma$-**fixed** index |
| psi-S2 | 1 | 2 | 2 | yes | yes | psi-I2 with the sign flipped at a $\Sigma$-**fixed** index |
| **psi-N1** | 1 | 3 | 3 | **no** | yes | psi-G with the sign flipped at **one index of a $\Sigma$-pair** |
| psi-N2 | 1 | 2 | 4 | **no** | yes | anti-invariant; the same Born shadow as psi-I4 |
| psi-N3 | 1 | 2 | 2 | **no** | **no** | non-invariant, Born shadow also asymmetric |
| psi-N4 | 1 | 1 | 2 | **no** | **no** | a non-invariant product state, Born-asymmetric |

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

Measured at all $6\times4\times2 = 48$ cells for every member:

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
number of admitted permutations and in the permutation each rule draws:

| member | admission cells that move | loop space |
|---|---|---|
| psi-I1, psi-I2, psi-I3, psi-I4, psi-S1, psi-S2, psi-N1, psi-N2 | **0 of 48** | identical to the reference at every setting |
| psi-N3, psi-N4 | **8 of 48** | 13 → 9 links, 364 → 8 based loops at GP-E |

**Yes, for two of the eleven, and the eight cells are named.** They are exactly the
realized rule at $t\in\{0,1,2,3\}$ at GP-E and GP-F — the cells whose admission
turns on the Born shadow's exchange symmetry. Both halves are clauses of the
gate's own predicate, so the reading comes out both ways on one family.

### 5.2 Does a common loop's holonomy change?

For the nine members whose loop space is identical, every one of the 364 based
loops at GP-E is **common**, and the comparison is total rather than partial.
Read at matched coordinates — same setting, same base point, same sequence of named
links with directions, same read times:

| member | common loops at GP-E | Born holonomy differs | permutation part differs | flat at the reference, not here |
|---|---|---|---|---|
| psi-I1 | 364 | **0** | 0 | 0 |
| psi-I2 | 364 | **0** | 0 | 0 |
| psi-I3 | 364 | **0** | 0 | 0 |
| psi-I4 | 364 | **0** | 0 | 0 |
| psi-S1 | 364 | **0** | 0 | 0 |
| psi-S2 | 364 | **0** | 0 | 0 |
| **psi-N1** | 364 | **206** | **206** | **2** |
| **psi-N2** | 364 | **196** | **196** | 0 |
| psi-N3 | 8 | 0 | 0 | 0 |
| psi-N4 | 8 | 0 | 0 | 0 |

**Yes.** The witness pair is $(\psi_G, \psi_{N1})$, and it is as clean as this
question admits, because the Born-level identity of the two is **measured** and
not argued (§8): the same $\lvert\psi_i\rvert$, the same $\lvert V_{ij}\rvert$
entry by entry, the same canonical Born-level key of every declared and every
realized leg at every (setting, frame) — that is, the same input to every clause
of the admission predicate — hence the same occupied sets, the same exact laws at
every node, the same admission table at all 48 cells, the same graph and the same
loop space. They differ only in a sign. And on 206 of their 364 common loops the
holonomy differs.

Note the shape of the table, because it contains its own control. Exactly two
members of the family are Born-level indistinguishable from the reference:
`psi-S1`, a sign flip at a $\Sigma$-**fixed** index, which stays
exchange-invariant, and `psi-N1`, a sign flip across a $\Sigma$-**pair**, which
does not. They sit at identical Born-level coordinates. `psi-S1` agrees with the
reference on all 364 loops; `psi-N1` differs on 206. And the six
exchange-**invariant** members agree with the reference on every common loop
whatever their Schmidt rank, support or Born shadow. That is the dependence law
showing itself before §6 derives it.

### 5.3 The witnesses, named

Two witnesses are extracted and printed, and each one's two holonomies are rebuilt
by an **independent route** — a plain left-to-right product of freshly constructed
link variables, sharing no interning, no step memo and no value cache with the
enumeration that produced the row — with the rebuilds measured to reproduce the
rows *and* to differ from each other.

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
can take, and at $\psi_{N1}$ there are **2** such loops among the 364.

---

## 6. How the holonomy depends on the preparation

### 6.1 The $\psi$-law

**Theorem (the $\psi$-law, gated).** Let $\Sigma$ be the exchange of the two labels
of the system pair, $Q$ the declared transposition, $H(\psi)$ the Householder of
$w = \psi - e_{(0,0)}$ and $V = H(\psi)Q$. Write
$D_{\text{GEN}} = (\Sigma Q^{\mathsf T}\Sigma Q)\otimes I_9$ for GEN's defect and

$$E(\psi) \;:=\; \Sigma\,H(\psi)\,\Sigma\,H(\psi)$$

for the **Householder's own exchange defect** — the same four-factor form as $D$,
one level down. Then

$$D(\psi)\;=\;P_W\,U_{\text{prep}}^{-1}\,P_W\,U_{\text{prep}}
\;=\;\bigl(\Sigma Q^{\mathsf T}\,H\Sigma H\,Q\bigr)\otimes I_9
\;=\;D_{\text{GEN}}\cdot Q^{\mathsf T}E(\psi)\,Q ,$$

and $E(\psi) = I$ **if and only if** $\psi$ is exchange-invariant (for
$\psi \neq e_{(0,0)}$).

*Proof sketch.* The wing exchange moves the system pair and the pointer pair
together, so $P_W = \Sigma\otimes\Sigma$, and the preparation leg acts as $V$ on the
system pair alone, so the four-factor product splits and the pointer factor is
$\Sigma I\Sigma I = I$; that gives $D = (\Sigma V^{\mathsf T}\Sigma V)\otimes I_9$,
GEN's first form, and substituting $V = HQ$ with $H$ symmetric gives the second.
For the third, insert $\Sigma\Sigma$: $\Sigma Q^{\mathsf T}(H\Sigma H)Q =
(\Sigma Q^{\mathsf T}\Sigma)(\Sigma H\Sigma H)Q = D_{\text{GEN}}Q^{\mathsf T}E(\psi)Q$.
For the characterisation, $E(\psi) = I \iff H\Sigma = \Sigma H \iff$ the Householder
of $\Sigma w$ is the Householder of $w$ $\iff \Sigma w = \pm w$; and since
$\Sigma e_{(0,0)} = e_{(0,0)}$, $\Sigma w = w \iff \Sigma\psi = \psi$, while
$\Sigma w = -w$ forces $\psi = e_{(0,0)}$, which the family excludes. $\square$

Both clauses are gated, and neither is left as algebra:

- **The law.** For every member of the family the $9\times9$ law tensored with the
  pointer identity is measured **equal, entry by entry**, to the direct
  $81\times81$ four-factor product built from that member's own preparation leg —
  two independent routes to the same object.
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

One further fact is measured and belongs beside the law: off the exchange-invariant
locus the defect is **not a signed permutation at all** — measured at all four
non-invariant members of the family. $E(\psi)$ is a symmetric orthogonal
involution, and conjugating $\Sigma$ by a Householder generically leaves the
signed-permutation class. So the way $\psi$ enters is not by permuting the
group's elements — it is by taking the holonomy out of the signed-permutation
class in which GEN's declared invariant is defined at all. That is why this unit
carries the Born shadow of the holonomy as its primary comparator.

### 6.2 The sign-flip census

The $\psi$-law says what the *defect* does. What the *holonomy* does at a fixed Born
shadow is settled by an exhaustive census, because the one remaining freedom inside
a fixed Born shadow is exactly the sign pattern.

For each declared exchange-invariant member, **every** sign pattern on its support
that fixes the initial coefficient is enumerated — the count computed, never typed
— and each one is **rebuilt in full** at GP-E: new preparation, new completion, new
admission table, new graph, new enumeration, new based holonomy.

| quantity | value |
|---|---|
| members swept | **7** |
| sign patterns swept, exhaustively | **48** |
| patterns whose holonomy differs from the reference | **26** |
| patterns whose holonomy agrees on every common loop | **22** |
| patterns where agreement and exchange-invariance disagree | **0** |

Three things are measured at every one of the 48. The **Born shadow** is unchanged
by a sign pattern, so no Born-level declaration can see the flip. The **loop space**
is unchanged, so every loop is common and the comparison is total. And the
**holonomy** agrees with the reference on every common loop **if and only if** the
flipped state is still exchange-invariant — that is, if and only if the sign pattern
is constant on every $\Sigma$-pair of the support.

The comparison target is the reference member throughout, and what makes that
legitimate is the separately measured fact of §5.2: every exchange-invariant
member of the family agrees with the reference on every common loop, whatever its
Schmidt rank, support or Born shadow. So "agrees with the reference" and "agrees
with its own unflipped member" coincide on the invariant locus, and the census
does not smuggle a second comparison in.

That is the dependence law, stated at the level the evidence carries:

> At a fixed Born shadow, the holonomy is a function of the preparation's sign
> pattern modulo the $\Sigma$-symmetric sign patterns; it moves exactly when the
> pattern differs across some $\Sigma$-pair of the support.

### 6.3 What this does to GEN §8.1

GEN's $\psi$-independence theorem is not contradicted anywhere; it is **located**.
Its hypothesis — an exchange-invariant preparation — is measured here to be
exactly the condition under which the $\psi$-term is trivial, over a family that
includes four further invariant members at three Schmidt ranks and two invariant
members obtained by sign flips. Inside that hypothesis, this unit reproduces GEN's
reading exactly: same defect, same group, same class counts, at seven members.

What changes is the **scope of the conclusion**. GEN's §8.1 licensed "both
curvature sources on this base are declaration-side"; what the family licenses is
that both curvature sources are declaration-side **on the exchange-invariant
locus**, and that off it the geometry moves with a feature of the state that no
declaration in the model reads.

---

## 7. The two controls

### 7.1 The positive control: GEN's preparation reproduces GEN's unit

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

**37** anchors against GEN, all passed. If any of these had moved, the instrument
would be measuring something other than GEN's geometry and no comparison across
$\psi$ would mean anything.

### 7.2 The negative control, with teeth

The pin requires that a **declaration** change move the holonomy, and that the
amount be predicted rather than observed. GEN's census supplies the prediction: the
family is dihedral, $\langle W, D\mid W^2 = D^n = 1,\ WDW = D^{-1}\rangle$ of order
$2n$ with $n = \operatorname{ord}(\delta(Q))$, $\delta(Q) = \sigma Q^{-1}\sigma Q$,
and order 1 with the links themselves refused on the equivariant locus where
$\delta(Q)$ is the identity.

Two alternative declared transpositions are run at the **same** preparation `psi-G`
with every other declaration untouched:

| control | $Q$ | $\delta(Q)$ | GEN law predicts | measured | abelian |
|---|---|---|---|---|---|
| the pinned $Q$ | $(0,1)\leftrightarrow(0,2)$ | order **2** | 4 | **4** | yes |
| **Q-negA** | $(0,1)\leftrightarrow(1,1)$ | order **3** | 6 | **6** | **no** |
| **Q-negB** | $(0,1)\leftrightarrow(1,0)$ | **the identity** | 1, links refused | **1** | yes |

Both predictions are met, both to the number and to the abelian/non-abelian
distinction, and the gate additionally requires that the holonomy have actually
**moved** from the pinned $Q$'s reading. The instrument can be moved by a
declaration, so its report that the state also moves it is worth something.

---

## 8. The gauge layer, the self-test and the flip-tests

**The switching self-test is complete at the declared setting.** The declared
switching group assigns one sign to each of the graph's 13 links at GP-E and is
swept **complete**, $2^{13} = 8{,}192$ per probe, over four declared probe loops at
two declared members; the **checkpoint subgroup** — the switchings induced by a sign
at each node, $2^{8-1} = 128$ — is swept complete beside it. The tested set is fixed
by **declaration**, in the order the probes are declared, and is never selected by
the verdicts under audit.

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
written, one per (member, probe) — and a second pass over those keys is measured
to return the **8** stored values, so the read path is measured to exist and to
work. The sweep then requests a key that **is** in the populated cache
**65,544** times and its hit count is nevertheless **zero** against **65,544**
measured misses. A zero-hit count over zero lookups would be vacuous; this one is
65,544 refusals to read a cache that had an answer.

**Two flip-tests.** The **direction flip-test** re-traverses every declared probe
loop with the direction convention flipped and measures the product of the two
matrices to be exactly the identity. Its positive content is forced by algebra —
the link variables are measured orthogonal and the reverse traversal is the
transpose — so what it retains is instrument integrity, and the mutant that reads a
reverse traversal without transposing dies there.

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
it. Two members, `psi-S1` and `psi-N1`, are Born-level identical to the reference
in every object the model builds; their law layers agree; their amplitude layers
do not both agree; and the one that parts company is the one whose sign pattern
is not constant across a $\Sigma$-pair.

---

## 9. The verdict

The decision rule is pre-registered and the verdict is derived from the gates and
from nothing else: `PSI-CURVATURE-EXISTS` if a common loop's holonomy is measured
to differ between two preparations; otherwise `PSI-PATH-SPACE-DEPENDENCE` if the
loop space is measured to move while every common loop agrees; otherwise
`PSI-DECLARATION-ONLY`; and `PSI-BLOCKED-AT-⟨object⟩` where the census cannot be
posed. The verdict string is re-derived inside its own gate from the recorded
measurements and measured to be the string the rule selects.

> **`PSI-CURVATURE-EXISTS-AT-FIXED-BORN-SHADOW`**, at the committed finite scope,
> at the declared preparation family, at the declared completion form and its
> pinned $Q$, per coordinate.

The qualifier is not decoration. It names where the witness lives, and it is the
strongest place it could live: at a fixed Born shadow the arena, the admission
table, the loop space and the law layer are all **measured** identical, so nothing
about the comparison is left to argument. The witness is a loop present in both
graphs, named identically in both, based at the same node, read at the same times,
with different holonomy.

**Beside it, folded into no verdict but reported as measured:**
`PSI-PATH-SPACE-DEPENDENCE` also occurs in this family, at `psi-N3` and `psi-N4`.
The pre-registered outcome of that name requires every common loop's holonomy to be
$\psi$-invariant, which this family refutes, so it is not the verdict. But the
phenomenon it names is real here and the cells that move are printed. The two
phenomena are not the same and are not confused: the Born shadow decides **which
loops exist**, the sign structure decides **what they carry**.

**What this answers.** GEN §11.12 asked whether any curvature carried by the state
rather than by a declaration exists anywhere in this theory. On this base, at this
completion form, at this pinned $Q$, over this family: **it does**, and the feature
of the state that carries it is invisible to every Born-level declaration the model
contains.

---

## 10. Scope and non-claims

1. **No claim about nature.** Every result is a statement about declared finite
   models, a declared gauge and declared finite search scopes.
2. **One base, one completion form, one $Q$.** The sweep varies the preparation and
   nothing else. It does not establish that the phenomenon survives a change of
   base, of completion form, or of $Q$; the negative control varies $Q$ only to give
   the instrument teeth, and its readings are folded into no positive claim about
   other completions.
3. **Eleven preparations are eleven preparations `[SAMP]`.** The family is a
   declared family, not a random or exhaustive sample of the preparations of base
   G, and no quantifier over states is entered anywhere. The one exhaustive
   object in the unit is the sign-flip census, over every sign pattern of the
   seven declared invariant members that fixes the initial coefficient — 48 of
   them — and what it decides, it decides there. The existence claim the verdict
   makes needs one witness and has two; the non-existence half of every gate is
   scoped to the declared family by construction.
4. **The holonomy is read up to the switching action, and twice.** The Born shadow
   is always defined and is the primary comparator; the permutation part is GEN's
   invariant and is undefined where the closed-loop matrix is not a signed
   permutation. Both readings are self-tested under the switching action. No claim
   is made about any quantity that is not switching-invariant.
5. **The witness's holonomy at the non-invariant member is not a signed
   permutation.** The difference is therefore registered in the Born shadow and in
   the readability predicate, both switching-invariant, and not as one permutation
   against another. That is stated at the claim and not only in the receipt.
6. **The path space is bounded** at $L_{\max}=8$, the canonical loop's own length,
   and every count is a count at that bound.
7. **The admission criterion is a declaration** — uniqueness of the admitted
   transport over the declared 2-element admitted set — and it is scope-dependent.
8. **Every claim is per coordinate.** The read time is a coordinate of the node and
   of the law datum; the matched table pairs only loops sharing every coordinate;
   and the count of law data read at different checkpoints that nevertheless compare
   equal is gated at zero.
9. **Nothing is claimed about locality, topology, causality, spacetime, fields, QFT
   or gravity.** "Holonomy", "connection", "corridor" and "arena" are operational
   vocabulary for declared finite objects. "State", "preparation" and "Born shadow"
   are names for declared vectors and their entrywise squares.
10. **Nothing of GEN's model is imported.** Only its committed receipt is read; the
    file is hash-pinned and the numbers taken from it are anchored exit-1, so a
    drift in either kills the run.

---

## 11. The receipt

`v13/code/psi_curvature_exact.py` → `psi_curvature_output.txt` +
`psi_curvature_receipt.json`.

- **Anchors:** 146, exit-1-only. **109** are self-anchors against this unit's own
  pinned declaration of base G — the three rotation matrices entry by entry, the
  declared transposition $Q$, and the full $9\times9$ completion of the reference
  preparation entry by entry. **37** are external anchors against the committed
  terminal receipt of the generality-check unit, three of which pin that receipt
  itself — its sha256, its schema string and the generator hash it records for its
  own instrument — before any value is read out of it. That most of the anchors are
  self-anchors is a disclosure, not a secret: what they buy is that no constructor
  can drift from the printed declaration without the run dying, and the external
  ones are what make the positive control a reproduction rather than a rebuild.
- **Gates:** 21, every one must-pass; there are **no disclosures**, and every gate
  carries at least one declared falsifier. The falsification census runs against
  a denominator of **20** — it excludes itself, since the census gate does not
  exist inside a mutant and cannot be falsified by this mechanism at all.
- **Mutants:** 34, each run to completion, each measured to exit 1 and to falsify at
  least one named gate or anchor. **The set of must-pass gates that no mutant
  falsifies is EMPTY**, and both denominators are printed: the count falsified by
  some mutant, and the smaller count falsified by a mutant that perturbs a
  **computation**. All **20** must-pass gates in the denominator are falsified by
  some mutant and **17** of them by a mutant that perturbs a computation; the
  three carried only by a waiver are named — `PSI-EXACT`,
  `PSI-NO-MUTANT-EXEMPTION` and `PSI-VERDICT`, the first two because their input
  is this module's own source text, which freeze-on-delivery forbids editing, and
  the third because a verdict vocabulary can only be violated by emitting a bad
  string. Each mutant declares its kind and the split is counted from the
  declaration — **28 perturb a computation and 6 are waivers**. A waiver overwrites
  a gate's computed predicate after the fact; what it measures is that the predicate
  carries the exit code, not that the gate would catch a computational defect, and
  the two are not claimed to be the same thing. The gates carried by a waiver alone
  are named.
- **No gate predicate references mutant identity**, measured as the headline says
  it: an AST sweep finds every `gate(...)` and `anchor(...)` call site, walks its
  argument expressions to any depth, and measures the number reaching the mutant
  flag to be **zero**; the four exemption forms are counted separately anywhere in
  the source, the one occurrence found lies outside every call site, and the `!=`
  count is gated at zero.
- **Independent comparators.** The record decomposition is rebuilt from the pinned
  rotations and an independently declared shift table. Each witness's two
  holonomies are rebuilt by a plain left-to-right product of freshly constructed
  link variables, sharing no interning, no step memo and no value cache with the
  enumeration that produced the row under audit, and the rebuilds are measured both
  to reproduce the rows and to differ from each other. The $\psi$-law is measured at
  $9\times9$ against the direct $81\times81$ computation.
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
  float in any value that reached a gate or an anchor.
- **Determinism:** no wall-clock value enters the receipt or the rendered output;
  two delivery-mode runs were executed and their artifacts are byte-identical.
- **One instrument-hygiene item is disclosed rather than changed.** A delivery-mode
  run writes its two artifacts before it computes its exit code, so a *failing*
  delivery run would overwrite them with a failing pair rather than leave the last
  good pair in place. The two runs behind these artifacts each exited zero with no
  must-pass failure, and their artifacts are byte-identical to each other.

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
flattening.** `Q-negB` lies on the exchange-equivariant locus, where GEN's §7.2
measured that the full-leg rule admits two permutations at the symmetric settings
and the links are refused for want of uniqueness. The prediction tested there is
therefore GEN's own compound one — order 1 **with links refused** — and the link
count is printed beside the group order rather than folded into it.

**D4 — the sign-flip census fixes the initial coefficient's sign.** A sign pattern
with $\varepsilon_{(0,0)} = -1$ does not act on the Householder by conjugation,
because $w = \psi - e_{(0,0)}$ is not homogeneous in $\psi$, so such a flip changes
the Born shadow of $V$ and leaves the fixed-Born-shadow comparison. The census is
exhaustive over the patterns that fix it — **48** — and the restriction is declared
rather than silent.

**D5 — the two census sweeps enumerate from the declared base point alone.** The
sign-flip census and the negative control read only the based loop set, so they
enumerate from $F_1@t{=}0$; the unit's own sweep enumerates from every node, which
is where the reduced-path and closed-path counts anchored against GEN come from.
The scope is printed in the receipt.

**D6 — the switching self-test is complete at one declared setting for two declared
members.** GP-E is the symmetric setting where the geometry lives, and the two
members are the witness pair. The sweep is complete over the full switching group
there — $2^{13}$ per probe — and over the full checkpoint subgroup; it is not
repeated at the other five settings, and that scope is stated at the claim rather
than implied by the word "complete".

**D7 — the holonomy is compared by its Born shadow first.** GEN's declared
invariant, the permutation part, is undefined on the very loops where this unit's
witness lives, because off the exchange-invariant locus the defect stops being a
signed permutation. Rather than filter those loops away — which would have hidden
the finding — the unit adds an always-defined comparator that is invariant under the
same switching action, self-tests it under that action, and reports both readings.
The permutation-part column is printed beside the Born-shadow column in every table.

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
co-finding with its own gate and its own printed cell list. Nothing is folded.
