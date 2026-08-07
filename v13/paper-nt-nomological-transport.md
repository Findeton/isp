# Nomological Transport

## Path-Dependence of Lawful Data on the W6 Co-reference Base

**Status:** `GREEN-UNREVIEWED (v13 NT unit)` — delivered against the frozen pin;
the §13 protocol freeze, the three-lens panel (whose mandatory first anchor is
this unit's independent PREFIX-DECIDES re-derivation, §2) and the adjudication
follow.

**Date:** 2026-08-07

**Frozen pin:** `v13/note-nt-transport-pin.md`, commit `26cc502`
(sha `ee22c5aadbcf`)

**Immutable base:** `a264a06` — O4 TERMINAL (v13 LOG #199), W6 TERMINAL
(v12 LOG #41), paper 1 TERMINAL, W5's LTP-forcing lemma. No new fixture is
built anywhere in this unit.

**Receipts:** `v13/code/nt_transport_exact.py` →
`v13/code/nt_transport_output.txt`, `v13/code/nt_transport_receipt.json`

**Lean:** NONE.

---

## Abstract

The O4 terminal unit bequeathed a question: transportability on this base is
decided by the two frames' declared **leg prefix**, not by the divisibility
residual. This unit asks the next question. Not whether *facts* descend — whether
the **law's own local data** can be carried between declared contexts along the
base's own structure, and whether the carrying is **path-dependent**. Path-dependence
of lawful transport is holonomy, and holonomy is the first geometric structure this
programme could earn rather than assume.

The pin's first clause is discharged first: **PREFIX-DECIDES is re-derived here
independently** — by multiset matching on canonical leg keys rather than the O4
script's permutation search, by this unit's own four-clause admissibility
predicate, and by its own defect matrix — and reproduces the O4 terminal profile
exactly: the leg-prefix profile agrees with the transport profile at **18 of 18**
cells, the residual profile at **12 of 18**, and all six equal-residual /
opposite-transport witnesses reappear. Seven anchors pin it cell by cell against
the committed O4 receipt.

The path space is then built and enumerated: nodes are (frame, checkpoint)
coordinates with the read time a declared coordinate of every node and every
datum; moves are leg applications in both directions and the co-reference
identifications the O4-terminal instrument admits uniquely. **34,024** reduced
paths and **4,972,096** path pairs sharing both endpoints are enumerated, none
typed.

Three results, all measured.

**The pin's canonical loop is exactly flat.** Frame 1's leg order forward against
frame 2's backward, closed by the identifications at the two declared division
events, has closed-loop holonomy **exactly the identity at every one of the six
settings**. The reason is the base's own: the two frames differ by the order of
two legs measured to commute, so the loop is a commutator of commuting operators.

**And the base is nevertheless not flat.** At the two symmetric settings the base
admits a *second* certified identification — the realized-only rule's **wing
exchange**, the same group element the O4 obstruction is about — and the bigon it
forms with the full-leg rule's identity carries closed-loop holonomy **the wing
exchange**, an element of order two, at a **prefix-aligned** checkpoint. That is a
**twisted corridor**. Meanwhile a loop that **crosses** the prefix-divergent
checkpoint has holonomy exactly the identity: a **flat crossing**. Both
pre-registered failure modes obtain, so the central hypothesis —
*the prefix criterion is the flatness condition* — is **REFUTED**, and refuted
twice.

**The layer matters, and the gauge is separated from the content.** At the
amplitude layer the canonical loop returns exactly; at the Born layer the law's
restriction does not, because the declared transposed one-step transition is
measured not to invert the forward one. The composition defect $\Delta^{B}$ — behind
an exact-posability gate that also measures it to be *identical* to W5's
declared-law residual — is carried flatly by every identification except the wing
exchange at SP-F, where it moves. Under the mandatory §14 sweep the closed loop's
**permutation part** is fixed under every switching swept while its **overall sign**
is measured to move, so the invariant is reported and the orbit is not.

**Unit verdict:**
`NT-HOLONOMY-⟨T1⟩ + NT-HOLONOMY-⟨T2⟩ + NT-HOLONOMY-⟨T3⟩ +
NT-PREFIX-FLATNESS-REFUTED`, at the committed finite scope, per coordinate.

---

## 1. The question, and what was inherited

Paper 0's law is a law of transitions between declared contexts. The O4 unit
established, at matched coordinates, that *facts* about unrecorded configurations
do not descend between the two frames at the intermediate checkpoints, and that
what governs descent is the alignment of the two frames' declared leg prefixes.
This unit changes the object. It carries not facts but **law-data**: the law's own
restriction to a context, the composition defect of the law's own factorisation,
and the amplitude layer the law's Born shadow is taken from.

Four things are inherited and anchored exit-1 rather than re-argued:

1. **PREFIX-DECIDES** — the pin's mandatory first anchor, panel-unseen at O4 and
   therefore **independently re-derived** here (§2).
2. **The wing-exchange orbit cause** — at the second intermediate checkpoint the
   two frames' occupied sets are one orbit of the base's admitted wing exchange at
   four of six settings, law-preserving at two, and cardinality-forced apart at the
   other two.
3. **K1 universality** — 36/36 cross-frame chart pairs disjoint and 30/30
   same-frame pairs sharing at that checkpoint; 0/36 at the others.
4. **LTP-LAWFUL at division events only.**

---

## 2. The pin's first clause: PREFIX-DECIDES, re-derived on this base

The pin makes this a clause, not an option: the O4 panel never saw
`O4-PREFIX-DECIDES`, so its independent re-derivation here is the successor
panel's first anchor and is reported before any transport result.

**The route is different from O4's, deliberately.** O4 computed prefix alignment
by searching permutations of leg orders inside its own `prefix_alignment`, and its
transport profile came out of its matched-table machinery. Neither is called here.
This unit computes:

- **the prefix profile** as **multiset equality of canonical leg keys** — a leg's
  key at a declared matching level is a canonical rendering of its Born shadow (or
  of the sign-minimal amplitude form), so order-free matching becomes multiset
  equality and needs no permutation search at all;
- **the transport profile** by its own four-clause admissibility predicate — the
  $j_0$ filter, the rule's own leg list, the occupied-set clause, the exact-law
  clause — over the base's admitted scope;
- **the residual profile** as the $j_0$ column of this unit's own defect matrix,
  which §4 measures to be W5's residual.

| cell | transports? | prefix match? | residual $=0$? | $\lVert r \rVert_0$ |
|---|---|---|---|---|
| $t=1$, SP-A / SP-B / SP-E | yes | yes | yes | 0 |
| $t=1$, SP-C / SP-D / SP-F | yes | yes | **no** | **16** |
| $t=2$, SP-A / SP-B / SP-E | **no** | **no** | yes | 0 |
| $t=2$, SP-C / SP-D / SP-F | **no** | **no** | **no** | **16** |
| $t=3$, all six | yes | yes | yes | 0 |

> **Re-derived.** Over the eighteen (read time, setting) cells the leg-prefix
> profile agrees with the transport profile at **18 of 18**; the
> residual-vanishing profile agrees at **12 of 18**. At every one of the six
> settings the two intermediate read times carry *identical* residual weight and
> *opposite* transport verdicts — six witnesses, all six reproduced.
> **Transportability does not reduce to the divisibility residual.**

Anchors A01–A07 pin every one of these against the committed O4 receipt: the cell
count, both agreement counts, all three profiles cell by cell, and the witness
count. All pass exit-1. The `prefix-lax` mutant reads the whole declared leg list
instead of the prefix and dies at this gate.

**What the re-derivation adds.** O4's finding survives an independent route on the
same base, and the profile it names is what §3 uses to declare which corridors are
*aligned*. The hypothesis this unit tests is built on that profile — and §6 refutes
it. The finding stands; the conjecture it suggested does not.

---

## 3. The declared arena and the path space (data, not prose)

Every coordinate is the base's own committed configuration; every count is
computed by the instrument from the fixtures.

| coordinate | value | provenance |
|---|---|---|
| carrier | 36 configurations $(q_A,q_B,p_A,p_B)$ | the committed composite model |
| initial configuration | $j_0 = 0$ | the committed model |
| family | 6 settings $\times$ 2 frames | the committed model |
| law | the declared legs $(U_{\text{prep}}, U_A(a), U_B(b))$ per setting and frame | the committed model |
| state | $p(0) = \delta_{j_0}$ | the committed model |
| **checkpoints (read times)** | $t \in \{0,1,2,3\}$, computed from the leg count; $t=0$ and $t=3$ are the declared division events | computed |
| **nodes** | $(\text{frame}, t)$ — **8** per setting | computed |
| admitted isomorphisms | **2** of the declared 72-element scope after the $j_0$ filter; **8** of its declared 96-element extension | W6 SCOPE clause 2 |
| switching group | one sign per link of the setting's own graph | computed per setting (§7) |
| path length bound | $L_{\max} = 2\cdot\text{NLEGS} + 2 = 8$, the canonical loop's own length | computed |

**The read time is a coordinate of the node and of the datum.** Every transported
datum carries the checkpoint at which it was read, and two data read at different
checkpoints can never compare equal — the O4 lesson (RUNBOOK §15 addendum) built
into the type rather than checked afterwards. The `readtime-conflate` mutant
restores the defect (every datum read at the final checkpoint) and dies.

### 3.1 The moves

**Leg applications**, forward and reverse: $(\text{fr},t-1) \leftrightarrow
(\text{fr},t)$, three per frame.

**Co-reference identifications** at the coordinates where the O4-terminal
instrument admits a **unique** transport. Two declared corridor-bound rules supply
them, and they supply **different maps**:

| setting | checkpoint | rule | admitted map | prefix-aligned |
|---|---|---|---|---|
| SP-A … SP-F | $t=0,1,3$ | FULL declared legs | **the identity** | yes |
| SP-A … SP-F | $t=2$ | FULL declared legs | *none admitted* | no |
| SP-E, SP-F | $t=0,1,3$ | REALIZED only | **the wing exchange** | yes |
| SP-E, SP-F | $t=2$ | REALIZED only | **the wing exchange** | **no** |
| SP-A … SP-D | any | REALIZED only | *none admitted* | — |

This table is the whole geometry of what follows, and every row of it is a
re-derivation of an O4-terminal measurement: the full-leg rule's counts
($1,0,1$ at $t=1,2,3$), the realized rule's counts ($0,0,0,0,1,1$ constant in the
read time), and the O4 finding that where the realized rule admits a transport the
admitted permutation is **the wing exchange and not the identity**.

### 3.2 The path space, enumerated

| setting | nodes | links | identification links | cycle rank | reduced paths | closed paths |
|---|---|---|---|---|---|---|
| SP-A | 8 | 9 | 3 | **2** | 422 | 56 |
| SP-B | 8 | 9 | 3 | **2** | 422 | 56 |
| SP-C | 8 | 9 | 3 | **2** | 422 | 56 |
| SP-D | 8 | 9 | 3 | **2** | 422 | 56 |
| SP-E | 8 | **13** | **7** | **6** | 16,168 | 2,820 |
| SP-F | 8 | **13** | **7** | **6** | 16,168 | 2,820 |

**Total: 34,024 reduced paths; 4,972,096 path pairs sharing both endpoints.** The
cycle rank is Euler's, computed from the enumeration and gated against it. A path
is *reduced* — it never traverses a link twice in immediate succession, because a
backtrack carries no transport content; the `reduce-lax` mutant drops the
condition and dies.

**A path lies in an aligned-prefix corridor** if every identification it traverses
sits at a checkpoint where the two frames' declared leg prefixes match, and it
**crosses divergence** if any identification it traverses sits at a checkpoint
where they do not. On this base exactly one kind of link crosses: the realized
rule's wing exchange at $t=2$, at SP-E and SP-F.

---

## 4. The three transported objects, each with its declared action

Every action is declared before any fixture value is evaluated; the freeze gate
measures the datum-evaluation counter to be **zero** at the declaration point and
the `freeze-lax` mutant, which evaluates one datum first, dies there.

| object | datum at a node | leg action | identification action |
|---|---|---|---|
| **T1** the law's restriction | the occupied support and the exact law at the node's declared read time | the declared **one-step Born transition**, its transpose in reverse | the admitted permutation |
| **T2** the composition defect | $\Delta^{B} = B(U_2U_1) - B(U_2)B(U_1)$ at the node's own cut, $U_1 = \Theta(t{\leftarrow}0)$, $U_2 = \Theta(N{\leftarrow}t)$ | the matrix carried unchanged, so leg flatness *measures* the defect's stability under moving the cut | **conjugation** by the admitted permutation (paper 1 equivariance (iv)) |
| **T3** the amplitude layer | — (a closed-loop object) | the leg operator, its inverse in reverse | the permutation matrix |

### 4.1 T2's exact-posability gate, evaluated before any T2 result

The RQ0-SYNTH lesson is a pin clause: if the defect question cannot be posed at the
committed laws, the unit reports `NT-BLOCKED-AT-⟨posability⟩` and forces nothing.
It is posable here, and the gate says why in three measured clauses at all **48**
nodes:

1. both cut factors are supplied by the committed laws at every node;
2. the amplitude composition is **exact** — $\Theta(N{\leftarrow}t)\,\Theta(t{\leftarrow}0)
   = \Theta(N{\leftarrow}0)$ on the nose — so $\Delta^{B}$ is the defect of a genuine
   factorisation of the declared process and not of an invented one;
3. **the weld.** The defect matrix built from paper 1's definition is measured
   **identical, entry by entry**, to W5's declared-law residual
   $\Gamma(N{\leftarrow}0) - \Gamma(N{\leftarrow}t)\Gamma(t{\leftarrow}0)$ at every
   node. Paper 1's composition defect and W5's divisibility residual are **one
   object** on this base, not two.

Measured: the defect weight is **0** at $t=0$ and $t=3$ at every setting (the
division events carry no defect, because one cut factor is the identity), **0** at
all four checkpoints at SP-A, SP-B and SP-E, and **288** nonzero entries at
$t \in \{1,2\}$ at SP-C, SP-D and SP-F, of which **16** lie in the $j_0$ column —
which is exactly $\lVert r \rVert_0$ of §2. The `defect-order` mutant composes the
two Born shadows in the wrong order and dies here.

---

## 5. The declared probes, and their exact holonomies

Four probes are declared, each built from the graph rather than typed.

| probe | corridor | role |
|---|---|---|
| **the canonical loop** | aligned | the pin's own loop: F1's leg order forward, the identification at the final division event, F2's leg order backward, the identification at the initial one |
| **the aligned-prefix bigon** | aligned | **the twisted-corridor probe**: the two rules' identifications at the *same* prefix-aligned checkpoint |
| **the prefix-crossing loop** | **crossing** | **the flat-crossing probe**: a loop through an identification at the prefix-divergent checkpoint |
| **the twisted comparator** | aligned | **the negative control with teeth**: the canonical loop with one identification deliberately replaced by the wing exchange where the base supplies the identity |

**Measured, exactly:**

| probe | setting | T3 closed-loop holonomy | T1 returns | T2 returns |
|---|---|---|---|---|
| the canonical loop | **all six** | **the identity** | no | yes |
| the aligned-prefix bigon, $t=0$ | SP-E, SP-F | **the wing exchange** | yes | yes |
| the aligned-prefix bigon, $t=1$ | SP-E | **the wing exchange** | yes | yes |
| the aligned-prefix bigon, $t=1$ | **SP-F** | **the wing exchange** | yes | **no** |
| the aligned-prefix bigon, $t=3$ | SP-E, SP-F | **the wing exchange** | yes | yes |
| the prefix-crossing loop $t{=}1{\leftrightarrow}t{=}2$ | SP-E, SP-F | **the identity** | SP-E yes, SP-F no | yes |
| the twisted comparator | SP-A … SP-D | not a signed permutation | no | yes |
| the twisted comparator | SP-E, SP-F | another permutation, sign orbit $\{-1,+1\}$ | no | yes |

Five readings, each measured.

1. **The pin's canonical loop is exactly flat, at every setting.** Its closed-loop
   holonomy is the identity matrix on the nose. The mechanism is the base's own and
   is anchored: the two frames of one experiment differ exactly by the order of two
   local operators the base measures to **commute** at all nine declared setting
   pairs (anchor A14), so the canonical loop is
   $\Theta_{F_2}(3{\leftarrow}0)^{-1}\Theta_{F_1}(3{\leftarrow}0)$ — a commutator of
   commuting operators. The first geometric structure the pin hoped to earn is, on
   its own canonical loop, **trivial**, and the run says so.

2. **The base is nevertheless not flat.** At SP-E and SP-F the base admits a second
   certified identification, and it is not the identity: it is the **wing exchange**.
   The bigon formed by the two rules' identifications at one and the same
   checkpoint has closed-loop holonomy exactly that element, of order two. The
   holonomy is not manufactured by this unit — both of its links are transports the
   O4-terminal instrument admits uniquely, at coordinates where the prefixes align.

3. **The twist sits at prefix-ALIGNED coordinates and the flatness at a
   prefix-CROSSING one.** The bigons fire at $t=0$, $t=1$ and $t=3$ — every aligned
   checkpoint — and the loop through the divergent checkpoint $t=2$ is measured
   flat. That is the exact opposite of the pre-registered pattern (§6).

4. **The negative control has teeth.** Injecting the wing exchange into the
   canonical loop where the base supplies the identity produces, at SP-A through
   SP-D, a matrix that is **not even a signed permutation**, and at SP-E and SP-F a
   different permutation carrying both signs. The instrument can see a twist; the
   flatness results of reading 1 are therefore not vacuous.

5. **T2 moves at exactly one coordinate, and it is the sharpest cell in the
   table.** Conjugating the composition defect by the wing exchange returns the same
   matrix everywhere except **SP-F at $t=1$ and $t=2$**, where
   $P_W\,\Delta^{B}\,P_W^{-1} \neq \Delta^{B}$. At SP-E the defect is identically
   zero, so nothing can move it; at SP-C and SP-D the wing exchange is not admitted;
   at SP-F both conditions fail at once — the defect is nonzero **and** the wing
   exchange is a certified identification — and the defect is measured **not** to be
   wing-symmetric there even though the two settings' angles are equal. The
   composition defect of the law is path-dependent at one measured coordinate of the
   whole base.

---

## 6. The central hypothesis, decided by the table

Pre-registered: **the prefix criterion is the flatness condition** — paths lying in
aligned-prefix corridors transport flatly, paths crossing prefix divergence are
obstructed or twisted. The matched table of path pairs decides it; both failure
modes were probed with teeth before the truth values were read.

**The matched table of path pairs** — every unordered pair of enumerated paths
sharing **both** endpoints, at matched coordinates:

| object | corridor | agree | disagree |
|---|---|---|---|
| **T1** | aligned | 681,660 | **1,025,340** |
| **T1** | crossing | **1,276,120** | 1,988,976 |
| **T2** | aligned | 1,478,644 | **228,356** |
| **T2** | crossing | **2,769,932** | 495,164 |
| **T3** | aligned | 434,744 | **1,272,256** |
| **T3** | crossing | **917,412** | 2,347,684 |

No pair has an obstructed side: every declared action is defined on every declared
move, so nothing here is a missing measurement.

> **`NT-PREFIX-FLATNESS-REFUTED`**, and refuted twice.
>
> **The twisted corridor exists.** Six witnesses — the aligned-prefix bigons at
> $t \in \{0,1,3\}$ at SP-E and at SP-F — are pairs of paths that stay inside
> prefix alignment and *disagree*, with the exact disagreement named: the wing
> exchange.
>
> **The flat crossing exists.** Two witnesses — the prefix-crossing loops at SP-E
> and SP-F — are paths that cross prefix divergence and transport with holonomy
> exactly the identity.

**What the mechanism is instead.** The measurement locates the twist precisely:
holonomy appears exactly where the base admits **two different certified
identifications at one coordinate**, and the two differ by the base's own **wing
exchange** — the same group element the O4 obstruction is a statement about. Prefix
alignment governs *whether an identification exists*, which is O4's finding and
survives §2 intact. It does not govern *whether the identifications that exist
agree with each other*. Those are two different questions, and this unit is the
measurement that separates them.

The flat crossing has the same explanation from the other side. At SP-E and SP-F
the two settings' angles coincide, so the wing exchange intertwines the two frames'
second legs; a loop that crosses the divergent checkpoint by that element and comes
back by it again is $P_W\,(L^{F_2})^{-1}P_W\,L^{F_1}$, and at those settings that is
exactly the identity. Crossing divergence costs nothing when the crossing is made
by the symmetry that the divergence is a divergence *of*.

---

## 7. The gauge layer, separated from its orbit (§14)

The L5 disease is exhibiting a gauge orbit as physics. The pin makes the sweep
mandatory, and the sweep is built so that a wrong invariant would show.

**The declared switching group** assigns one sign to each link of a setting's own
graph. Its order is computed, never typed: $2^{9} = 512$ at SP-A through SP-D
(six leg links and three identifications) and $2^{13} = 8192$ at SP-E and SP-F
(the four extra realized-rule identifications). **The checkpoint subgroup** — the
switchings induced by a sign at each *node*, which is the base's own
checkpoint-phase redundancy — has order $2^{8-1} = \mathbf{128}$ at every setting,
the graph being connected.

**The declared invariant is the closed loop's permutation part; its overall sign is
the gauge orbit.** Measured, with every holonomy in the sweep **rebuilt from the
link variables**, caches bypassed:

| | swept | distinct permutation parts | distinct sign orbits |
|---|---|---|---|
| the full switching group | 512 per loop (complete at four settings, a declared uniform stride sample of the 8192 at SP-E and SP-F [SAMP]) | **1** at every swept loop | **2** |
| the checkpoint subgroup | 128 per loop, complete everywhere | **1** | **1** |

Three clauses, three teeth.

- **The invariant is fixed.** The permutation part takes exactly one value under
  every switching swept, at every declared loop and every setting.
- **The gauge orbit is fixed under the honest gauge and not under the wider
  redundancy.** The loop's sign is invariant under the whole 128-element checkpoint
  subgroup and *moves* under the full link-sign group — which is what makes it an
  orbit datum and not a result.
- **The mis-conventioned control moves.** A quantity reading the raw sign is
  measured to move; a sweep under which nothing moves cannot certify an invariance,
  so this gate is the sweep's own tooth.

The `gauge-sign` mutant drops the switching on a *reversed* traversal — a
sign/orientation perturbation of exactly the kind §14 requires — and dies; the
`gauge-subsample` mutant collapses the sweep and dies at the group-order clause.

**The self-test evaluates fresh (§14 addendum).** Its cache-hit count is gated at
**zero** and its miss count gated positive, so a self-test reading the instrument's
cache would be testing the cache and not the quantity; the `memo-lax` mutant lets
it read the cache and dies.

---

## 8. Verdicts

### 8.1 Per object, from the measurement

| object | verdict | pairs agreeing | pairs disagreeing | distinct transported values | settings with a nontrivial loop value set |
|---|---|---|---|---|---|
| **T1** | **`NT-HOLONOMY-⟨T1⟩`** | 1,957,780 | 3,014,316 | 223 | all six |
| **T2** | **`NT-HOLONOMY-⟨T2⟩`** | 4,248,576 | 723,520 | 5 | SP-C, SP-D, SP-F |
| **T3** | **`NT-HOLONOMY-⟨T3⟩`** | 1,352,156 | 3,619,940 | 186 | SP-E, SP-F |

Each verdict is derived from that object's own rows of the matched table and from
nothing else. The nondegeneracy clause is gated: none of the three is a constant,
so none is `NT-INERT`.

**T1's holonomy is a statement about the layer, not about the frames.** The law's
restriction is carried forward by the declared one-step Born transition, and
backward by its transpose — and the transpose is measured *not* to invert the
forward step. That is why the canonical loop, exactly flat at the amplitude layer,
does not return T1 at any setting: the Born-level step is irreversible, and a
Born-level parallel transport around a loop that goes forward in one frame and
backward in the other cannot return. Stated as the finding rather than the number:
**the law's restriction transports flatly along the law's own forward steps and is
path-dependent as soon as a reverse step is taken**, at every setting including the
four where the frames' geometry is trivial. This is a property of the declared
Born-level action, and §5 reading 1 is the matched statement one layer up.

**T2's holonomy is the sharpest single cell.** It is carried entirely by SP-F, where
the composition defect is nonzero *and* the wing exchange is a certified
identification *and* the defect is measured not to be wing-symmetric. SP-C and SP-D
appear in the loop-value column for the leg reason — the defect is a datum of the
cut and moving the cut moves it — and not for a frame reason.

**T3's holonomy is the geometric one**, and it lives at exactly the two settings
where a second certified identification exists.

### 8.2 The holonomy value set and the group it generates

Read as the gauge-invariant permutation part of the closed-loop link product, based
at $F_1@t{=}0$, enumerated over **every closed path of the committed path space**:

| setting | holonomy values realized | the group they generate |
|---|---|---|
| SP-A, SP-B, SP-C, SP-D | **1** — the identity alone | trivial |
| SP-E, SP-F | **3** — the identity, **the wing exchange**, and one further permutation | **order 4**, computed by closure |

The value set is enumerated at the declared length bound and need not be closed
under composition there, so the group it generates is computed separately by
closure rather than read off the count — the two are different objects and the
receipt carries both.

### 8.3 The unit

> **`NT-HOLONOMY-⟨T1⟩ + NT-HOLONOMY-⟨T2⟩ + NT-HOLONOMY-⟨T3⟩ +
> NT-PREFIX-FLATNESS-REFUTED`**

Derived: lawful transport on this base **is** path-dependent, at all three declared
layers; the pin's own canonical loop is nevertheless exactly flat at every setting;
and the pre-registered flatness criterion is refuted by witnesses of both kinds.
The geometric structure the theory earns here is small and exactly named — a
two-element wing-exchange holonomy at the two symmetric settings — and it is earned
at the coordinates where the base admits two certified co-reference rules at once,
not at the coordinates where prefixes diverge.

### 8.4 Controls and flip-tests

- **Positive control:** the canonical loop, a path pair that *must* agree because
  the two legs commute — measured to have holonomy exactly the identity at every
  setting. The `control-lax` waiver and the `orient-flip` computational mutant both
  die on it.
- **Negative control with teeth:** the twisted comparator — measured non-identity
  at every setting, and not even a signed permutation at four of them.
- **Direction flip-test (must-pass):** every declared loop re-traversed with the
  direction convention flipped yields the **inverse** permutation, at every loop and
  every setting, so the flatness and holonomy verdicts are invariant under the
  bookkeeping choice. The `flip-lax` waiver dies on it.
- **Admission-criterion disclosure:** identification links are admitted by
  *uniqueness* of the admitted transport (the O4 discriminator's FORCED). The O4
  terminal separately measured that its **certificate** is degenerate at the first
  intermediate checkpoint and refuses the pair at the second, so an admission
  criterion reading the certificate instead would admit links only at the final
  division event and would empty the loop space. Both readings are printed; every
  verdict above is licensed at the declared criterion and at no wider scope.

---

## 9. Scope and non-claims

1. **No claim about nature.** Every result is a statement about declared finite
   models, a declared gauge and declared finite search scopes.
2. **Every claim is per coordinate**, and the read time is a coordinate carried
   inside every datum. No comparison is drawn between data read at different
   checkpoints.
3. **The path space is bounded** at $L_{\max}=8$, the canonical loop's own length,
   and every count is a count at that bound. The holonomy *value set* is therefore a
   value set at that bound; the group it generates is computed by closure and stated
   separately.
4. **The admission criterion is a declaration** (§8.4) and its alternative is
   disclosed, not silently taken.
5. **T1's per-coordinate action is a declaration.** The Born-level one-step
   transition forward and its transpose in reverse; a different declared action —
   for instance transport at the amplitude layer — is a different object, and on
   this base that object is T3, whose canonical-loop verdict is the opposite one.
   The contrast between the two is §8.1's finding, not an inconsistency.
6. **T2's leg action is a declaration.** The defect is a datum of the *cut*, so a
   leg move carries the matrix unchanged and leg flatness measures the defect's
   stability under moving the cut. Paper 1's affine chain law relating consecutive
   cuts is not implemented here and no claim is made about it.
7. **W5's lemma is used in one direction only**, exactly as at O4: a nonzero
   residual shows a checkpoint is not a division event of the model as declared;
   a vanishing residual establishes nothing.
8. **The switching sweep is complete at four settings and sampled at two** — see
   the deviations appendix; the checkpoint subgroup is swept complete everywhere.
9. **The permutation scopes are declared** and every negative is a negative at the
   stated scope: 72 elements admitting 2 after the $j_0$ filter, 96 admitting 8.
10. **Nothing is claimed about locality, topology, causality, spacetime, fields,
    QFT or gravity.** "Holonomy", "connection", "corridor" and "arena" are
    operational vocabulary for declared finite objects. In particular, the
    two-element holonomy of §8.2 is a holonomy of a declared graph connection on a
    declared finite base, and no continuum, curvature or geometric interpretation is
    entered here.

---

## 10. The receipt

`v13/code/nt_transport_exact.py` → `nt_transport_output.txt` +
`nt_transport_receipt.json`.

- **Anchors:** 22, exit-1-only, against the committed O4 terminal receipt (the
  PREFIX-DECIDES gate value, all three profiles cell by cell, the orbit relation,
  the occupied supports, the pair census, the residual weights), the committed W6
  note and output, and the committed model's own orthogonality and commutation
  measurements.
- **Gates:** 15, of which 14 are must-pass and 1 is a declared disclosure; the
  falsification census below covers 13 of the 14 — the fourteenth is the census's
  own gate.
- **The path space:** 34,024 reduced paths; 4,972,096 path pairs sharing both
  endpoints; every count computed from the enumeration and none typed.
- **Mutants:** 21, each run to completion, **21 of 21 died** — each measured to
  exit 1 and to falsify at least one named gate or anchor. **The set of must-pass
  gates that no mutant falsifies is EMPTY**, at denominator 13. Each mutant
  declares its kind and the split is counted from the declaration: **17 perturb a
  computation and 4 are waivers**. A waiver overwrites a gate's computed predicate
  after the fact, so what it measures is that the predicate carries the exit code —
  not that the gate would catch a computational defect, and the two are not claimed
  to be the same thing.
- **The suite covers** the pin's own first clause (`prefix-lax`), the path space
  (`path-collapse`, `reduce-lax`), the gauge layer (`gauge-sign`,
  `gauge-subsample`), the read-time coordinate (`readtime-conflate`), the defect's
  composition order (`defect-order`), two direction conventions (`orient-flip`,
  `flip-lax`), the identification admissibility (`id-lax`), the declared scopes
  (`scope-lax`), the fresh-evaluation layer (`memo-lax`), the freeze
  (`freeze-lax`), exactness (`float-lax`), four reused-anchor perturbations
  (`anchor-o4-prefix`, `anchor-o4-occ`, `anchor-w6-wing`, `anchor-ltp`), and
  waivers of the posability predicate, the positive control, the flip-test and
  the verdict vocabulary.
- **Self-test:** the §14 sweep evaluates **fresh** — every holonomy is rebuilt
  *through* the instrument's own value cache with the cache bypassed, so the
  bypass is a measured fact and not an absence: the phase's cache-hit count is
  gated at **zero** against **6,400** measured misses, one per swept instance.
  The tested set is fixed by **declaration** — one loop per declared probe role,
  in the order the probes are built — and never selected by the verdicts under
  audit.
- **Exactness:** the totally real quartic field $\mathbb{Q}(\cos\pi/8)$ of the
  committed model, where tuple equality is field equality, plus
  `fractions.Fraction`. An AST sweep finds no float literal and no call to `float`,
  and a runtime sweep finds no float in any value that reached a gate or an anchor.
  Path-pair agreement is identity of exact structural keys; no tolerance exists
  anywhere in the instrument.
- **Determinism:** no wall-clock value enters the receipt or the rendered output;
  two delivery-mode runs were executed and their artifacts are byte-identical.

---

## Appendix: deviations

**D1 — the canonical loop does not return T1, and that is the finding, not a
control failure.** As first written, the positive control required the canonical
loop to return *both* the amplitude-layer holonomy (identity) and T1's own value.
It fails the second clause at every setting, because the declared Born-level
backward action — the transposed one-step transition — is measured not to invert
the forward one. The control is therefore scoped to the amplitude layer, where the
"must agree" claim is the one the commuting-legs anchor licenses, and T1's
behaviour is reported as the measurement it is (§8.1). The two are stated as a
layer contrast, not reconciled away.

**D2 — the switching group is 512 at four settings and 8192 at two.** The pin
names "the 512 checkpoint-phase switchings". Measured on this unit's arena, one
sign per link of a setting's own graph gives $2^9 = 512$ where only the full-leg
rule supplies identifications and $2^{13} = 8192$ where the realized rule supplies
four more. The sweep is **complete** at the four 512-settings, and at SP-E and SP-F
it is a declared uniform stride sample of **512** of the 8192, marked `[SAMP]` with
both sizes printed. The checkpoint subgroup (128) is swept **complete** at every
setting.

**D3 — the admission criterion is FORCED, not CERT.** The pin says
"identifications where the O4-terminal instrument certifies them, i.e. at
aligned-prefix/division coordinates". The instrument has two readings of
"certifies": uniqueness of the admitted transport (the discriminator's FORCED) and
the ROUTE-EXT certificate. Only the first agrees with the pin's own gloss — the O4
certificate is degenerate at $t=1$ and refuses the pair at $t=2$, so the second
would admit links at the final division event alone and empty the loop space. The
first is declared, the second disclosed with its measured consequence (§8.4), and
every verdict is licensed at the declared criterion.

**D4 — T2's leg action carries the matrix unchanged.** The defect is a datum of the
cut; the declared leg action therefore measures the defect's stability under moving
the cut rather than implementing paper 1's affine chain law between consecutive
cuts. That law is not used and nothing is claimed about it. The consequence is
visible in §8.1: SP-C and SP-D enter T2's nontrivial-loop column for the leg reason
and not for a frame reason, and the paper says which is which.

**D5 — the holonomy value set is bounded; the group is computed by closure.** The
value set is enumerated over the closed paths of the committed path space, which is
bounded at $L_{\max}=8$, so it need not be closed under composition. The group it
generates is computed separately by closing the observed set under composition, and
both numbers are carried in the receipt. The paper never calls the value-set size a
group order.

**D6 — the declared legs are held in a fixture cache.** Rebuilding the committed
model's operators inside the §14 sweep dominated the run time. The legs are the
**fixture**, not a transported value: they are built once per (setting, frame) from
the committed model and held, exactly as the base itself holds them. Every quantity
the self-test measures — the loop holonomies — is rebuilt from those fixtures on
every switching, with the transported-value caches bypassed, and the fresh-eval
gate is stated over those quantities.

**D7 — the path length bound is a declaration.** $L_{\max} = 2\cdot\text{NLEGS}+2$
is computed from the model as the canonical loop's own length, so the pin's loop is
inside the enumerated space; every count in §3.2 is a count at that bound and no
claim is entered about longer paths.

**D8 — a waiver mutant must exercise its predicate in the failing direction.**
As first written, the three waiver mutants set their gate's computed predicate to
`True`. That cannot fail a gate that already passes, and all three survived. The
defect is the waiver *convention*, not the gates: a waiver's purpose is to measure
that the predicate carries the exit code, which is shown by overwriting it to
`False`. All three are rewritten that way and all three now die. The episode is
recorded because it is exactly the failure the falsification census exists to
catch, and the census caught it before delivery.

**D9 — no Lean.** As the pin states.
