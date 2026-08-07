# The O4 Discriminator

## Unrecorded Actuality on the Record Co-reference Base

**Status:** `GREEN-UNREVIEWED (v13 O4-DISCRIMINATOR, re-derived)` — delivered
against the frozen pin under the adjudication's re-derivation order RD-1..RD-6
(v13 LOG #196); the STATUS update and any successor cycle follow.

**Date:** 2026-08-07

**Frozen pin:** `v13/note-o4-discriminator-pin.md`, commit `e1e8dcd`
(sha `2568bc528796`)

**Immutable base:** `71371ae` — W6 TERMINAL (v12 LOG #41), paper 2 TERMINAL,
paper 0 v2.4 §O4, W5's LTP-forcing lemma (v12 LOG #12). No new fixture is
built anywhere in this unit.

**Receipts:** `v13/code/o4_discriminator_exact.py` →
`v13/code/o4_discriminator_output.txt`, `v13/code/o4_discriminator_receipt.json`

**Lean:** NONE.

---

## Abstract

Paper 0 v2.4 leaves an explicit fork. **O4-A** — unrecorded local
configurations are actual but ephemeral — *requires* a covariant co-reference
rule for those configurations. **O4-B** — only records are actual — pays a
different price. W6 built the base at which the question becomes decidable: on
its committed two-frame model, record facts provably descend. This unit asks
whether unrecorded configuration facts descend **under the same instrument, at
the same coordinates**.

The central object is a **matched table**: three declared fact-classes × every
declared read time × every candidate rule × every setting, one gate set, one
naming convention, name-free matched representatives in the arena test. The
read time is a declared coordinate carried inside each datum and gated for
equality across the classes in every cell, because a class-versus-class
contrast whose classes are read at different times is a coordinate effect in
disguise.

What the table says is that **transportability on this base is time-indexed,
not class-indexed**. At the second intermediate read time nothing transports —
not the unrecorded configuration class, and not the record class either — and
the obstructing object is exhibited and measured as a *relation*: the two
frames' occupied configuration sets are disjoint at **every** cross-frame pair
of the twelve charts, while **every** same-frame pair shares; at four of the
six settings the two sets are one orbit of the base's own admitted wing
exchange (law-preserving at two of them), and where they are not one orbit the
disjointness is cardinality-forced. At the first intermediate read time the
unrecorded class is instead **FORCED at every setting under every
corridor-bound rule matching the full declared legs**, while the certificate is
degenerate there — the two
occupied configurations carry the same probability and no declared value
distinguishes them — so no rule is certified at either intermediate time.

The sharpest measured fact is a negative about the programme's own favourite
quantity. Across the eighteen (read time, setting) cells, whether a
corridor-bound rule transports the unrecorded class agrees with whether the two
frames' declared **leg prefixes** up to that time match order-free at
**18 of 18** cells, and with whether W5's divisibility residual vanishes at
only **12 of 18**; at every one of the six settings the two intermediate read
times carry **identical residual weight and opposite transport verdicts**.
**Transportability does not reduce to the divisibility residual.**

Where a transport of the unrecorded class does exist at an intermediate time it
is LTP-BARE: W5's forcing lemma fires at SP-C, SP-D and SP-F, and at the
remaining settings the shared record subalgebra is measured empty. The LAWFUL
branch is not a stipulation — it is measured to fire at the final declared
division event, where a shared record law does condition on the datum.

**Unit verdict: `O4-BLOCKED-AT-⟨the intermediate read times⟩`**, class-neutral,
at the committed finite scope, per coordinate. The delivered
`O4-DISCRIMINATED-RECORD-ACTUALISM + O4-ARENA-RELATIVE` is **withdrawn**: the
first obtains at exactly one coordinate of the whole matched table, which is a
declared division event and outside the object's scope, and the second is
measured to carry no fact the obstruction does not. The charter fork is **not**
adjudicated here.

---

## 1. The question, made decidable

Paper 0 v2.4 §O4 states the fork and its prices. Quoted verbatim:

> **O4-A (Barandes-compatible configuration realism):** unrecorded local
> configurations are actual but ephemeral. **Price:** O4-A requires a new
> covariant co-reference rule for unrecorded local configurations; BC2 shows
> the current slice-indexed composite formalism does not provide that rule
> (scoped to that formal apparatus, not to relativity in nature); a preferred
> structure is one possible completion, **not yet a forced conclusion**. W5's
> LTP-forcing lemma is the fulcrum: [B3]'s own axioms deny composite division
> events exactly where the process is indivisible, so under O4-A the composite
> has definite actuality at intermediate times to which no probability law
> attaches.
>
> **O4-B (record actualism):** only records are actual; unrecorded
> configurations are variables of the nomological representation. **Price:** T1
> must be rewritten; definite pre-record configurations cease to be ontic;
> several of W5's FAITHFUL correspondences become EXTENSION or TENSION; the
> result departs from Barandes configuration realism.

The charter's scope sentence binds this unit: *no global present, no global
configuration history, no global event set.* A candidate rule that recovers
co-reference by imposing a single time index shared across contexts is
therefore outside the corridor by construction, and this unit's job is to make
that exclusion a **measurement** rather than a stipulation.

The discriminator's form, from the pin: on the record co-reference base — where
record facts provably descend — **construct the rule O4-A needs, or exhibit its
obstruction, at the committed finite scope.**

Two clauses of the charter text above are load-bearing for what follows and are
therefore carried on the page rather than paraphrased away. O4-A's "a preferred
structure is one possible completion, *not yet a forced conclusion*" is the
charter's own hedge against reading a missing co-reference rule as forcing a
preferred structure; nothing below strengthens it. O4-B's "unrecorded
configurations are *variables of the nomological representation*" is already a
representation-relativity clause, so a measured representation-relativity of
unrecorded configuration truth-values is a **measurement of** O4-B's clause and
not an addition to it.

---

## 2. The declared arena (data, not prose)

Every coordinate is the base's own committed configuration. Every count in the
table is computed by the instrument from the fixtures; none is typed.

| coordinate | value | provenance |
|---|---|---|
| carrier | 36 configurations $(q_A,q_B,p_A,p_B)$, $q_X \in \{0,1\}$, $p_X \in \{r,+,-\}$ | the committed composite model |
| initial configuration | $j_0 = 0$, i.e. $(0,0,r,r)$ | the committed model |
| boundary | the record partitions by $(q_A,p_A)$ and $(q_B,p_B)$, with the pointer as declared value | W6 census §1 |
| family | 6 settings $\times$ 2 frames $=$ 12 charts | the committed model |
| law | the declared legs $(U_{\text{prep}}, U_A(a), U_B(b))$ per setting and frame | the committed model |
| state | $p(0) = \delta_{j_0}$ | the committed model |
| **read times** | $t \in \{1,2,3\}$, the number of declared legs applied; $t=0$ and $t=3$ are the model's declared division events, so the pin's object lives at $t \in \{1,2\}$ | computed from the declared leg count |
| arena, part 1 | the admitted isomorphisms: **2** of the declared 72-element permutation scope; **8** of its declared 96-element extension, after the base's own $j_0$ filter | W6 SCOPE clause 2 |
| arena, part 2 | the checkpoint-phase switchings: **8** $= 2^3$, one sign per declared leg | W6's declared *sign* matching level |
| **arena size** | **192** | computed as $6 \times 2 \times 2 \times 8$ |

**The read time is a coordinate, not a convention.** A chart *read at* $t$ is
the same process — the same declared legs, the same law — presented with the
record tokens written by then; W6's own `Chart` reads the joint record law at
the time the last visible token was written, so the read time propagates into
the record datum through the base's own semantics. The construction is not a
choice the results depend on: "read at time $t$" is computed a second,
independent way — the base's own **truncated** process on its first $t$ legs,
the construction W6's M4 control uses — and the two agree in **36 of 36** cells
of both substantive classes at all three read times (gate
`O4-READ-TIME-ROBUST`).

**Why the switchings are the amplitude gauge here.** The base's declared
matching levels are *exact*, *sign* and *Born*, and the sign level exists
because a real orthogonal propagator and its negative generate one stochastic
process. The switching group of a chart with three declared legs is therefore
$\{+1,-1\}^3$, its Born shadow is invariant by construction, and it is exactly
the place amplitude data enters this base. Its size is read off the leg count.

**Why the acting group is the admitted 2 and not the declared 8.** The wider
extension scope is not closed under its own conjugation, so an action drawn
from it would test a candidate's declared search scope rather than the
candidate. The 2-element admitted group — the identity and the pure wing
exchange — is contained in every candidate's search scope, and the wing
exchange is precisely the nontrivial identification the base is about. The
8-element figure is carried as a disclosure.

Per §15, every claim below is licensed **per coordinate** and at no wider
scope.

---

## 3. The instrument

### 3.1 Three fact-classes, one gate set, one read time per cell

A **fact-class** assigns to each chart, *at a declared read time*, a set of
carriers with declared data, and a rule for pushing that data along a
configuration bijection. Three classes are declared, and all three are routed
through the same ten gates by the same code path at the same read time.

| class | carriers | datum | role |
|---|---|---|---|
| **F-REC** | the record tokens written by read time $t$ | the joint law of their declared values on the actual (positive-probability) value tuples at $t$ | **positive control** |
| **F-CFG** | the 36 configuration propositions "the configuration at $t$ is $i$" | the actuality bit and the exact probability of every configuration at $t$ | **the object**, at $t \in \{1,2\}$ |
| **F-CTRL** | the same 36 carriers | the configuration's own integer **name** | **negative control** |

F-CTRL is mis-conventioned in exactly one respect: it reads a label the
declared gauge is free to change. A name has no read time, and that is part of
the mis-convention: its row is measured constant in the read-time coordinate,
and the no-slice gate's index clause is measured **degenerate** on it at all
twelve charts, which is disclosed rather than scored as a pass.

**The like-for-like property is gated semantically, not syntactically.** Each
datum carries the read time at which it was evaluated, and
`O4-LIKE-FOR-LIKE` measures that the three classes' data — and the
certificate's own pair guard — were read at *the same* time, equal to the
cell's declared time, in all **54** cells. The `readtime-conflate` mutant reads
the record class at the final time whatever the cell declares — the defect this
re-derivation exists to remove — and dies there.

### 3.2 The ten gates

| gate | what it measures |
|---|---|
| **EXIST** | a transport exists on every declared edge, on a non-empty carrier set |
| **FORCED** | the base's five-valued discriminator emits FORCED on every declared edge |
| **INV** | the inverse of an admitted transport is admitted in reverse |
| **TRI** | triple coherence on the declared triple **[SP-A]** |
| **GLUE** | a coherent family in one gauge orbit with an injective colimit **[SP-A]** |
| **CERT** | the transported datum is *certified*, not merely compatible |
| **COVAR** | the verdict is equivariant under the admitted arena action |
| **NAMEBLIND** | the verdict survives a pure configuration relabelling |
| **NOSLICE** | the verdict survives a pure time re-indexing, in two clauses |
| **LTP** | a committed probability law conditions on the transported datum |

EXIST/FORCED are read through the base's own five-valued discriminator
(FORCED / UNDERDETERMINED / ABSENT / VACUOUS / NO-INSTRUMENT), so the
vocabulary is emitted rather than typed — and a class with no carriers at a
coordinate is called **VACUOUS** there and never counted as passing. TRI/GLUE
are read through the base's own descent solver on the base's own declared
triple, at SP-A only; the columns are tagged accordingly. CERT is the base's
ROUTE-EXT construction with **both** of its guards intact: the pair guard (a
configuration on which the two charts disagree disqualifies the pair) and the
degeneracy guard (a joint law with fewer than two positive entries certifies
nothing, and is reported VACUOUS — neither a certificate nor a refusal). The
degeneracy guard is load-bearing in this unit and is disclosed cell by cell.

**The position this unit takes on the certificate.** The two frames live on
**one** configuration space with **one** declared labelling: configuration 12
is configuration 12 in both. On that reading the identity *is* the canonical
cross-frame co-reference of configurations, the disjointness of §6 is
substantive, and CERT — which compares the two charts' data pointwise in the
configuration name — is the right certificate. Name-blindness is then a
*within-chart* gauge condition: the declared gauge acts on charts, not across
frames. The consequence is stated where it bites: a transport carried by a
**non-identity** admitted permutation re-identifies configurations rather than
co-referring them, and §6 names the one such transport this unit finds.

### 3.3 The no-slice gate, in two measured clauses, with its scope stated

The gate must exclude any rule that recovers co-reference from a shared global
time index, and it must do so by measurement. Prepend an identity leg to a
chart: the process is the same object presented on a shifted index, and no
transition has been added.

> **Clause N (normalisation).** A rule inside the corridor identifies the chart
> with its own re-indexed presentation exactly as it identifies the chart with
> itself. The reference is the rule's *own* self-transport count, so a rule
> cannot pass by returning zero twice.
>
> **Clause I (index).** The same *moment* lives at index $t+1$ in the
> re-indexed presentation and at index $t$ in the original, so reading the
> index and reading the moment are two different readings. At every chart where
> the two readings are measured to give different data, the rule must not
> identify the uncompensated pair as it identifies the compensated one. Where
> the two readings give the same datum, the probe has no teeth and the chart is
> declared **degenerate** rather than passed.

**The gate's scope, measured and disclosed rather than inferred from its
name.** Swept over all twelve combinations of the three declared matching
levels, the order-free stipulation and the identity-leg normalisation
(`O4-NOSLICE-SENSITIVITY`), clause N passes at exactly the six with the
identity-leg normalisation on, at every level and under both order-free
settings: it is sensitive to that normalisation **alone**, it is the
leg-normalisation clause, and the corridor's order-free stipulation is *not*
what it tests. Clause I is what measures index reading, and it is degenerate
exactly where a class's datum has no read time — all twelve charts of the
name-reading control, and the record class at $t=1$ where no token has been
written in either presentation. Measured: the two declared slice rules, C1 and
C1a, fail NOSLICE at every one of the twelve charts at every read time and are
the only declared rules that do — both count identity legs, which is the
clause's measured sensitivity; the `global-now-smuggler` mutant
makes every rule read the index instead of the moment, which empties the
corridor census's inside set, and it dies there.

Because clause N is measured to be the leg-normalisation clause, the corridor's
second stipulation — order-free matching — is *declared* and its effect is
**measured separately** rather than gated: candidate C1a is C1 with that single
declaration changed (§4), and the difference between them is what tells us
which of the two conventions empties C1.

---

## 4. The candidate rules, declared before fixture truth

The freeze gate measures that the fact-datum evaluation counter is **zero**
when the declarations are recorded, and that no gate has yet been entered; the
receipt's gate order is the proof (RUNBOOK §13(4)). The `freeze-lax` mutant evaluates
one fixture datum first and dies there.

| id | rule | level | scope | corridor claim |
|---|---|---|---|---|
| **C1** | **NAIVE-SLICE** — same configuration label at the same declared time index; legs matched *in order*, identity legs counted | exact | 72 | declared *outside*: the gated-out control |
| **C1a** | **NAIVE-SLICE-ORDER-FREE** — C1 with one declaration changed: legs matched order-free, identity legs still counted | exact | 72 | declared *outside*: the second control |
| **C2** | **DESCENT-RESTRICTION** — co-reference only where the base's groupoid acts: an admitted frame-isomorphism, order-free, blind to identity legs, carrying the read-time datum | Born | 72 | inside |
| **C2X** | **DESCENT-RESTRICTION-AT-THE-AMPLITUDE-LEVEL** — C2 with one declaration changed: legs must match on the nose | exact | 72 | inside (claimed) |
| **C3** | **MODAL-CARRIER** — carried by the **full declared legs, including never-taken transitions**, matched up to the per-leg sign | sign | 96 | inside |
| **C4** | **REALIZED-ONLY** — carried by the realized process alone: each leg restricted to the configurations actually occupied before and after it | Born | 72 | inside |

**Why C1a exists.** So that what empties the naive slice rule is *measured*
rather than attributed. C1 and C1a differ in exactly one declaration.

**Why C2's level is Born.** The base measured that what cuts the record-level
wing tie is the legs' **Born shadows alone** — amplitude phases play no part.
C2 is the rule "co-reference where the groupoid acts", so it inherits the level
at which the groupoid is measured to act.

**Why C2X exists.** So that what the corridor does to the matching level is
*reported* rather than chosen: a rule reading amplitudes on the nose is asked
to be invariant under the checkpoint-phase switchings, which are exactly the
amplitude gauge.

**Why C3 is the candidate the base suggests.** The base's deepest finding is
that at the symmetric settings the record-token identification is carried by
$U_{\text{prep}}$'s columns on the 35 configurations the process never
occupies — *the identification is carried by transitions the process never
takes.* C3 asks whether F-CFG transport can be carried by the same modal
structure. C4 is its mirror: nothing counterfactual is consulted.

---

## 5. The matched table

This is the unit's central object: **54 cells** — six candidate rules × three
fact-classes × three read times — each carrying all nine measured descent
gates (486 gate cells) plus the LTP column of §8, all computed at the cell's
own read time. `PASS` / `fail` as measured.

**The transport counts, per read time, per setting.** $|\Phi|$ on the committed
frame pair; the discriminator's word in brackets where it is not FORCED.

| candidate | class | $t=1$ | $t=2$ | $t=3$ |
|---|---|---|---|---|
| **C1** | F-REC / F-CFG / F-CTRL | 0,0,0,0,0,0 | 0,0,0,0,0,0 | 0,0,0,0,0,0 |
| **C1a** | F-REC | 1×6 [VACUOUS] | 0×6 | **1×6** |
| | F-CFG | **1×6** | 0×6 | 1×6 |
| | F-CTRL | 1×6 | 1×6 | 1×6 |
| **C2 / C2X / C3** | **F-REC** | 1×6 [VACUOUS] | **0×6** | **1×6** |
| | **F-CFG** | **1×6** | **0×6** | 1×6 |
| | F-CTRL | 1×6 | 1×6 | 1×6 |
| **C4** | F-REC | 0,0,0,0,1,1 [VACUOUS] | 0,0,0,0,**1**,**1** | 0,0,0,0,1,1 |
| | F-CFG | 0,0,0,0,**1**,**1** | 0,0,0,0,**1**,**1** | 0,0,0,0,1,1 |
| | F-CTRL | 0×6 | 0×6 | 0×6 |

**The gate rows of the corridor-bound rules.** C2 shown. C3 is identical to it
in every one of its nine cells, gate for gate. C2X differs from C2 in exactly
one gate — COVAR, which is why it is measured outside the corridor — and only
in the cells where its covariance row is non-vacuous: at $t=2$ its record and
configuration rows admit nothing anywhere, so covariance is satisfied vacuously
there and the two rules' rows coincide.

| read time | class | EXIST | FORCED | INV | TRI | GLUE | CERT | COVAR | NAMEBLIND | NOSLICE |
|---|---|---|---|---|---|---|---|---|---|---|
| **$t=1$** | F-REC | fail | fail | fail | PASS | PASS | fail | PASS | PASS | PASS |
| | **F-CFG** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **fail** | **PASS** | **PASS** | **PASS** |
| | F-CTRL | PASS | PASS | PASS | fail | fail | PASS | PASS | **fail** | PASS |
| **$t=2$** | F-REC | fail | fail | fail | fail | fail | fail | PASS | PASS | PASS |
| | **F-CFG** | **fail** | fail | fail | fail | fail | **fail** | PASS | PASS | PASS |
| | F-CTRL | PASS | PASS | PASS | fail | fail | fail | PASS | **fail** | PASS |
| **$t=3$** | **F-REC** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| | F-CFG | PASS | PASS | PASS | PASS | PASS | fail | PASS | PASS | PASS |
| | F-CTRL | PASS | PASS | PASS | fail | fail | PASS | PASS | **fail** | PASS |

**The certificate, per class and read time** (its three outcomes are all
exhibited; `True` = certified, `DISAG` = the pair guard refuses,
`VACUOUS` = the degeneracy guard fires):

| | $t=1$ | $t=2$ | $t=3$ |
|---|---|---|---|
| F-REC | VACUOUS ×6 | DISAGREEMENT ×6 | **True ×6** |
| F-CFG | VACUOUS ×6 | DISAGREEMENT ×6 | True ×5, VACUOUS at SP-E |
| F-CTRL | True ×6 | DISAGREEMENT ×6 | True ×6 |

Six readings, each measured.

1. **At matched read times the two substantive classes have the same
   profile.** At $t=2$, under the rules matching the full declared legs,
   both are ABSENT at every setting, both are refused by the certificate, and
   neither descends on the declared triple. At $t=3$ both are FORCED at every
   setting. At $t=1$ the record class has no carriers at
   all — the discriminator emits VACUOUS, not FORCED — while the configuration
   class is FORCED at every setting. **There is no coordinate at which the
   record class is green and the configuration class is measured to fail** on a
   gate other than the certificate's degeneracy guard.

2. **The positive control fires at its own coordinate, and only there.**
   Routed through *this* unit's instrument — the same ten gates, the same
   discriminator, the same solver — the record class reproduces the base's
   terminal results at the final declared division event: FORCED at every
   setting, the inverse law holding, the declared triple descending over all
   six ordered edges and all six ordered triples. At the intermediate read
   times the same class is measured to have no transport at all, which is the
   base's own control 4 ($|\Phi_B| = 0$ at the intermediate slice, anchor A13)
   reproduced through this instrument. Twenty-seven anchors pin the reused
   values exit-1 against their committed receipts.

3. **The negative control fails, and its tooth is the right one.** F-CTRL
   fails NAME-BLINDNESS — the gate its mis-convention was built to fail — in
   **every one of the 18 (candidate, read time) cells**, and it also fails the
   declared triple everywhere. At $t=1$ and $t=3$ it *passes* the certificate,
   which is the honest reading: the certificate is not a name-detector, and
   where the two charts agree configuration by configuration it certifies the
   name-reading class as readily as any other. The control's failure is
   therefore carried by name-blindness alone, not by four gates re-reporting
   one fact.

4. **The naive slice rule and the leg-order convention are separated.** C1
   admits **zero** transports of every class at every read time. C1a — the same
   rule with the single declaration `order_free` flipped — admits the record
   class at the final time at all six settings and the configuration class at
   $t=1$ at all six. So C1's emptiness is measured to be its **leg-order
   convention**, not its slice reading: the two frames of one experiment differ
   exactly by the order of two commuting legs, and an order-bound rule cannot
   match them. What survives as a statement about the slice reading is the one
   C1a supplies: even order-free, an index-counting rule gets **zero** at
   $t=2$, because at that time the two frames' occupied supports are disjoint.
   Both rules are measured outside the corridor (C1 at NOSLICE; C1a at NOSLICE
   and COVAR).

5. **C4 reproduces the base's realized-legs finding at every read time.** The
   realized restriction leaves both substantive classes ABSENT at the four
   asymmetric settings and FORCED at the two where the angles coincide,
   exactly as the base measured — and the profile is the *same* for the record
   class and the configuration class, at every read time. C4's declared triple
   is measured under C4's own rule and does **not** descend (`ABSENT-PAIR`,
   TRI and GLUE fail); the gate `O4-CANDIDATE-RULE-CONSISTENCY` measures, in
   all 54 cells, that the triple's `F1←F2` edge count equals the edge gate's
   own count at the same coordinate, which is what a candidate's gates being
   computed under another candidate's rule would violate.

6. **The vacuous and the degenerate cells are declared as such.** A class with
   no carriers at a coordinate is VACUOUS there and is never counted as a
   pass — the verdict derivation requires the discriminator's FORCED, not a
   count of one. The record class's TRI and GLUE at $t=1$ are exactly such a
   pass: with no tokens written, the declared triple descends on empty token
   maps, and the derivation reads that as no evidence at all rather than as a
   coherent family. The certificate's degeneracy guard fires at $t=1$ for both
   substantive classes and at SP-E at $t=3$ for the configuration class; both
   lists are printed in `O4-VACUITY-DISCLOSURE` rather than rendered as
   passes.

---

## 6. The obstruction, measured as a relation

At $t=2$ the instrument's central negative is not a bare zero, and it is not
six independent measurements either. The obstructing object is exhibited as
data and then measured as a **relation** between the two occupied sets.

| setting | frame F1 occupied | frame F2 occupied | $\lvert \cap \rvert$ | one orbit of the admitted wing exchange? | law-preserving? | disjointness cardinality-forced? |
|---|---|---|---|---|---|---|
| SP-A | $\{12,24\}$ | $\{1,2,10,11,19,20,28,29\}$ | **0** | no | — | **yes** |
| SP-B | $\{12,24\}$ | $\{1,2,10,11,19,20,28,29\}$ | **0** | no | — | **yes** |
| SP-C | $\{3,6,12,15,21,24,30,33\}$ | $\{1,2,10,11,19,20,28,29\}$ | **0** | **yes** | no | no |
| SP-D | $\{3,6,12,15,21,24,30,33\}$ | $\{1,2,10,11,19,20,28,29\}$ | **0** | **yes** | no | no |
| SP-E | $\{12,24\}$ | $\{11,19\}$ | **0** | **yes** | **yes** | no |
| SP-F | $\{3,6,12,15,21,24,30,33\}$ | $\{1,2,10,11,19,20,28,29\}$ | **0** | **yes** | **yes** | no |

> **The obstruction, and its scope.** At $t=2$ — and at $t=2$ alone among the
> three declared read times — the two frames' occupied configuration sets are
> disjoint. The disjointness is not an artifact of which pair was committed:
> over all 66 unordered pairs of the twelve charts, **all 36 cross-frame pairs
> are disjoint and all 30 same-frame pairs share**, so the disjointness tracks
> the frame coordinate exactly. At $t=1$ and at $t=3$ the census reads
> **0 of 36** cross-frame pairs disjoint: the obstruction is a fact about one
> read time, not about the frame pair as such.

Three things this table says that a bare intersection count cannot.

**(i) At four of the six settings the two sets are ONE ORBIT of the base's own
admitted wing exchange**, and at SP-E and SP-F that element additionally
preserves the exact intermediate law. This is the element the base's own
deepest finding is about. The two sides of the disjointness are therefore
related, not merely unequal, at exactly the settings where the base's structure
says they should be.

**(ii) Where they are not one orbit, the disjointness is cardinality-forced.**
At SP-A and SP-B the two supports have sizes 2 and 8, so *no* bijection
whatever relates them, admitted or otherwise. The gate measures that
implication — every setting outside the orbit is a setting where the
cardinalities differ — rather than reporting six zeros.

**(iii) The disjointness is not what excludes the map that would have
worked.** Decomposing the transport predicate into its four successive clauses
(the $j_0$ filter → leg compatibility → the actual-set clause → the law
clause), for every corridor-bound rule matching the **full** declared legs the
wing exchange is excluded at the **leg** clause — one clause *earlier* than the
support — at every setting and both intermediate read times. The identity, the
only admitted map those rules do admit past the leg clause, then fails the
actual-set clause because the supports are disjoint. So the honest statement is
narrower than "the transport dies on the disjointness": the disjointness is
what the **certificate** refuses — `route_ext_pair` returns DISAGREEMENT
whenever any configuration is assigned different probabilities by the two
charts, and disjoint non-empty supports force that — and the certificate is
candidate-independent, so it refuses every rule at that coordinate for the same
reason.

**And the one transport that does survive is named.** Where C4 admits a
transport of the unrecorded class (SP-E and SP-F, at every read time), the
admitted permutation is measured to be the **wing exchange** and not the
identity. On this unit's stated position (§3.2) that is a *re-identification*
of configurations rather than a co-reference of them: it is the base's own
group element, carrying one frame's occupied set onto the other's and
preserving the exact law there, and it is exactly the map the full declared
legs exclude.

---

## 7. What decides transportability — and what does not

The matched table has one further reading, and it is the unit's bequest to the
nomological-transport pin.

| cell | do the corridor-bound **full-leg** rules transport F-CFG? | do the two frames' declared leg prefixes match order-free? | does W5's divisibility residual vanish? |
|---|---|---|---|
| $t=1$, SP-A/B/E | **yes** | yes | yes |
| $t=1$, SP-C/D/F | **yes** | yes | **no** ($\lVert r \rVert_0 = 16$) |
| $t=2$, SP-A/B/E | **no** | **no** | yes |
| $t=2$, SP-C/D/F | **no** | **no** | **no** ($\lVert r \rVert_0 = 16$) |
| $t=3$, all six | **yes** | yes | yes |

The rules compared are the corridor-bound candidates that match the **full**
declared legs — C2, C2X and C3, selected from the declarations, and measured to
agree with each other at every one of the eighteen cells.

> **Measured.** Over the eighteen (read time, setting) cells, the leg-prefix
> profile agrees with the transport profile at **18 of 18**; the
> residual-vanishing profile agrees at **12 of 18**. At **every one of the six
> settings** the two intermediate read times carry *identical* residual weight
> and *opposite* transport verdicts. **Transportability does not reduce to the
> divisibility residual.**

The equal-residual pair is the sharp form. At SP-C, SP-D and SP-F the residual
is $\lVert r \rVert_0 = 16$ in both frames at $t=1$ *and* at $t=2$ — W5's
forcing lemma fires equally at both times, so both are certified non-division
events of the model as declared — and yet at $t=1$ every corridor-bound
full-leg rule transports the unrecorded class uniquely and at $t=2$ none of them
transports it at all. At SP-A, SP-B and SP-E the residual vanishes at both times and the same
flip occurs. Whatever decides transportability here, it is not the
non-divisibility of the process at that time.

What *is* measured to decide it is the base's own leg structure. The two frames
of one experiment differ exactly by the order of two commuting legs, so their
declared leg prefixes coincide before either local event ($t=1$: both
$(U_{\text{prep}})$), differ strictly between ($t=2$: one frame has performed
$U_A$, the other $U_B$), and coincide again as multisets after both ($t=3$).
The transport profile follows that structure at every cell. Stated as the
mechanism rather than the correlation: **at $t=2$ the two charts' index-2
moments are not the same moment** — the index is shared, the event is not — and
the disjointness of §6 is what that difference looks like on the configuration
support.

The realized-only rule is deliberately **not** folded into this comparison: it
matches a *restricted* leg list, so a statement about the declared leg prefix is
not a statement about it. Its own profile is measured and printed alongside —
constant in the read time, ABSENT at the four asymmetric settings and FORCED at
SP-E and SP-F at all three read times — and it is carried by the wing exchange
on the realized legs (§6), which is exactly the sense in which the criterion
generalises: what a rule can transport at a read time is decided by whether the
two frames' prefixes *at that rule's own leg list* are related by a map the rule
admits.

This is a co-variation measured over eighteen cells at one committed base, not
a proven equivalence, and it is entered as such. It is also the reason the
successor pin is about transport and not about divisibility: the quantity that
governs whether *fact-data* descend between two presentations of one experiment
is measured here to be the alignment of their declared events, and the
divisibility residual is measured not to govern it.

---

## 8. The LTP gate

Every candidate must state what probability law attaches to the actuality it
transports. The gate computes it rather than asserting it, at the same read
time as the fact-data, in three steps.

1. **The actuality at that read time is exhibited** — the occupied support and
   its exact law, at every chart and every read time.
2. **W5's forcing lemma is evaluated at that time**, on the model's own
   admissible $p(0) = \delta_{j_0}$. Writing $D(t) = \Gamma(3{\leftarrow}0)
   - \Gamma(3{\leftarrow}t)\,\Gamma(t{\leftarrow}0)$, the lemma's
   contrapositive says: if $D(t)\,p(0) \neq 0$ then $t$ **is not a division
   event of that model as declared** — so no committed law conditions on the
   transported configuration there. The lemma is one-directional, and this unit
   makes no use of the converse: a vanishing residual does not establish a
   division event.
3. **The record side is checked at the same time:** how many declared record
   partitions have been written, in both frames, by then.

**The residual and the shared record algebra, per read time (both frames
identical):**

| read time | $\lVert r \rVert_0$ of 36, per setting | shared record partitions |
|---|---|---|
| $t=1$ | 0, 0, **16**, **16**, 0, **16** | 0, 0, 0, 0, 0, 0 |
| $t=2$ | 0, 0, **16**, **16**, 0, **16** | 0, 0, 0, 0, 0, 0 |
| $t=3$ | 0, 0, 0, 0, 0, 0 | **2, 2, 2, 2, 2, 2** |

The value censuses reproduce the committed ones exactly at the declared
intermediate time: at SP-C, four distinct values with **zero** rational entries
of the sixteen; at SP-F, six distinct values with **eight of sixteen**
rational. Rationality is decided by the field's own test, never by a tolerance.

**The gate's verdict, per candidate and read time.**

| candidate | $t=1$ | $t=2$ | $t=3$ |
|---|---|---|---|
| C1 | n/a | n/a | n/a |
| C1a, C2, C2X, C3 | **LTP-BARE** (forced at SP-C/D/F; unwitnessed at SP-A/B/E) | n/a | LTP-LAWFUL ×6 |
| C4 | **LTP-BARE** (SP-F forced; SP-E unwitnessed) | **LTP-BARE** (SP-F forced; SP-E unwitnessed) | LTP-LAWFUL at SP-E/SP-F |

`n/a` = no transport admitted, so no actuality is transported and the gate has
nothing to attach a law to. The two live readings at the intermediate times
are:

- **LTP-BARE, forced** — the residual is nonzero, so by the lemma that read
  time is not a division event of the model as declared. The transport carries
  actuality; nothing in the committed law conditions on it. This is the
  charter's own fulcrum sentence, instantiated with numbers on the base.
- **LTP-BARE-UNWITNESSED** — the residual vanishes, so the forcing lemma does
  not fire; but the shared record subalgebra at that time is measured empty, so
  no committed law conditions on the datum there either. The gate distinguishes
  the two cases and does not report the second as the first.

**The LAWFUL branch is witnessed, not stipulated.** It fires on the committed
base at $t=3$, where two record partitions have been written in both frames and
a shared record law does condition on the datum, and the outcome selector emits
`O4-RULE-EXISTS` from it there. It fires nowhere at $t \in \{1,2\}$, and that
is now a *measured* negative at a coordinate where the branch is live rather
than a structural impossibility of the selector (gate
`O4-LTP-LAWFUL-WITNESSED`; the `ltp-shared-lax` mutant injects a shared record
partition where the base has none and dies there). A second gate,
`O4-LTP-RECONCILED`, re-derives every cell's aggregate verdict from that cell's
own per-setting strings, so a stubbed selector cannot pass silently — which is
what the `ltp-stub` mutant, whose only effect is to stub the selector, is for.

---

## 9. The arena test, at name-free matched representatives

Both classes' truth-values are pushed through the same admitted action over all
192 arena points, at every read time — and each class supplies its quantity in
**both representative types**, because a name-indexed object must move under a
relabelling and a name-free one cannot, by type, before any physics is
consulted.

| quantity | class | representative | read time | moves under | distinct values |
|---|---|---|---|---|---|
| **QA1** | F-CFG | name-indexed | $t=2$ | setting, **frame**, **relabelling** | 4 |
| **QA1f** | F-CFG | **name-free** | $t=2$ | setting, **frame** | 3 |
| **QA2** | F-REC | name-free | $t=3$ | setting | 2 |
| **QA2n** | F-REC | **name-indexed** | $t=3$ | **relabelling** | 2 |
| QA2n | F-REC | name-indexed | $t=2$ | **frame**, **relabelling** | 2 |
| QA1 | F-CFG | name-indexed | $t=3$ | setting, **relabelling** | 5 |
| QA1f | F-CFG | name-free | $t=3$ | setting | 3 |
| QA2 | F-REC | name-free | $t=2$ | nothing | 1 |
| QA1, QA1f, QA2, QA2n | both | both | $t=1$ | nothing | 1 |

(The full grid — four quantities × three read times — is in the receipt; every
row is reported, none is selected.)

> **Measured.** The relabelling coordinate separates **representative types,
> not fact-classes**: both name-indexed quantities move under it at every read
> time where anything moves, and neither name-free quantity ever does. The
> record class's *name-indexed* truth-values move under the relabelling exactly
> as the configuration class's do — and at $t=2$ they move under the frame as
> well.

What survives type-matching is the **frame** coordinate at $t=2$, and it is
measured to carry no fact §6 does not already carry: at name-free matched
representatives the two frames' unrecorded-configuration data differ at
$\{$SP-A, SP-B, SP-C, SP-D$\}$ at $t=2$ and nowhere else, a **proper subset**
of the six coordinates at which §6 measures the occupied sets disjoint (gate
`O4-ARENA-NO-RESIDUAL`). At SP-E and SP-F the two frames' name-free
intermediate data are **equal** — the same structure that lets the
realized-only rule admit a transport at exactly those two settings (§6).

Accordingly the arena test is reported **once**, here, as the obstruction
restated in truth-value language and weaker, and no second outcome is drawn
from it. `O4-ARENA-RELATIVE` is **withdrawn** (§10.2).

**The corridor's own two controls.** At least one declared candidate is
measured inside the corridor at every read time and at least one outside — a
corridor every candidate passes tests nothing, and a corridor no candidate
passes tests only the corridor. Measured: C2, C3 and C4 inside at all three
read times; C1 (NOSLICE), C1a (NOSLICE and COVAR) and C2X (COVAR) outside at
all three.

**The level census.** The same rule run at all three declared matching levels,
with its invariance under the checkpoint-phase switchings measured at each: the
**exact** level is measured *not* invariant (24 switching failures of 48), the
**sign** and **Born** levels are (0). The corridor's covariance clause
therefore selects the matching level as a measurement, and the sign-convention
mutant dies at this row.

---

## 10. Verdicts

### 10.1 Per cell of the matched table

Every verdict is derived from the measured gate rows of the cell it belongs to
and from nothing else. A declaration flip-test gate re-derives each cell's
verdict with the candidate's declared corridor claim flipped to its opposite;
the results must be identical, and are. The vocabulary gate measures that
every verdict emitted begins with one of the pin's five pre-registered names.

| candidate | $t=1$ | $t=2$ | $t=3$ (the final declared division event) |
|---|---|---|---|
| **C1** | `O4-BLOCKED-AT-<NOSLICE: the rule leaves the declared corridor>` | same | same |
| **C1a** | `O4-BLOCKED-AT-<COVAR/NOSLICE: …>` | same | same |
| **C2** | `O4-BLOCKED-AT-<the certificate is degenerate: the transported datum takes one value on the whole occupied support>` [all six] | `O4-BLOCKED-AT-<no unique transport (ABSENT)>` [all six] | `O4-RULE-EXISTS` [SP-A..D, SP-F] `+ O4-DISCRIMINATED-RECORD-ACTUALISM` [SP-E] |
| **C2X** | `O4-BLOCKED-AT-<COVAR: …>` | same | same |
| **C3** | as C2 | as C2 | as C2 |
| **C4** | `O4-BLOCKED-AT-<no unique transport (ABSENT)>` [SP-A..D] `+ O4-BLOCKED-AT-<the certificate is degenerate…>` [SP-E, SP-F] | `O4-BLOCKED-AT-<no unique transport>` [SP-A..D] `+ O4-BLOCKED-AT-<the certificate refuses the pair>` [SP-E, SP-F] | `O4-BLOCKED-AT-<no unique transport>` [SP-A..D] `+ O4-DISCRIMINATED-RECORD-ACTUALISM` [SP-E] `+ O4-RULE-EXISTS` [SP-F] |

**The modal candidate's answer, stated plainly.** C3 asks whether the modal
structure that carries the base's record-token identification — the columns of
$U_{\text{prep}}$ on the 35 configurations the process never occupies — can
also carry unrecorded configuration facts. Measured: at $t=2$ it cannot, and
neither can anything else, records included; at $t=1$ and $t=3$ it carries them
exactly as the Born-level rule does. The modal structure is measured to make
**no difference at any coordinate**: C3's row is identical to C2's in all nine of
its cells (three fact-classes x three read times), gate for gate and count
for count. Whatever the never-taken transitions do for record tokens on this
base, they do nothing for configuration propositions, and they do nothing
against them either.

### 10.2 The unit

> **`O4-BLOCKED-AT-⟨the intermediate read times⟩`** — emitted with its blocking
> objects named from the measurement:
>
> `O4-BLOCKED-AT-<the intermediate read times: t=1: no unique transport
> (ABSENT) / the certificate is degenerate: the transported datum takes one
> value on the whole occupied support; t=2: no unique transport (ABSENT) / the
> certificate refuses the pair>`

Two objects are named at each time because the corridor-bound rules produce two
kinds of cell there. At $t=1$: the realized-only rule admits no transport at the
four asymmetric settings, and everywhere a transport does exist — every setting
under C2 and C3, and SP-E/SP-F under C4 — the certificate is degenerate. At
$t=2$: the full-leg rules admit no transport at any setting, and where the
realized-only rule does admit one (SP-E and SP-F) the certificate refuses the
pair.

Derived: over the pin's object — unrecorded configuration facts at the read
times strictly before the final declared division event — **no cell of the
matched table reaches a certified, unique, covariant transport, for any
fact-class**, and the two intermediate read times are blocked by different,
named objects. The record class is not an exception at either: at $t=1$ it has
no carriers and at $t=2$ it is ABSENT at every setting.

**Two withdrawals, both derived from the table rather than conceded.**

**`O4-DISCRIMINATED-RECORD-ACTUALISM` is withdrawn.** As delivered it asserted
that the record control is green while the unrecorded class is obstructed *at
every coordinate at which the record class is green*. Measured on the matched
table, that outcome obtains at exactly **one** (read time, setting) coordinate
of the eighteen — SP-E at $t=3$, under three of the six candidate rules (C2, C3
and C4) — and there it is carried by the
certificate's **degeneracy** guard on the configuration side (at SP-E the
final-time support is two configurations of equal probability, so the datum
takes one value on the whole support) rather than by any refusal. That
coordinate is the final declared division event, which is outside the pin's
object. At the object's own read times the outcome obtains **nowhere**. The
delivered verdict was a coordinate effect: the record class was read at $t=3$
and the configuration class at $t=2$, and at matched read times the
discrimination is null.

**`O4-ARENA-RELATIVE` is withdrawn.** At name-free matched representatives the
unrecorded class's truth-values move under the frame coordinate at a **proper
subset** of the coordinates at which §6 measures the obstruction, and under no
coordinate the obstruction does not already carry; the relabelling leg, which
carried the delivered claim's "orbit size 2", is measured to separate
representative types rather than fact classes. There is one fact here, and §6
states it once.

**What the other pre-registered outcomes do.** `O4-RULE-EXISTS` obtains, but
only at the final declared division event — where the configuration fact is a
fact *at* a division event, both records have been written, and a shared record
law conditions on it. That is the matched control coordinate, not the object,
and no claim about unrecorded actuality is drawn from it.
`O4-RULE-EXISTS-LTP-BARE` does **not** obtain as a cell verdict: at $t=1$,
where a unique corridor-bound transport of the unrecorded class does exist at
every setting under every full-leg corridor-bound rule, the certificate is
degenerate, so the rule does not pass the gates the outcome requires. What that transport
*would* carry is nevertheless measured, and it is LTP-BARE — forced by W5's
lemma at SP-C, SP-D and SP-F, unwitnessed-but-equally-bare at the other three.
That is reported as the LTP gate's finding (§8), not promoted to a verdict.

---

## 11. What each charter branch pays under this verdict

This section states prices. It adjudicates nothing; the fork's resolution, if
any, is paper 0's to record and the user's to route.

**O4-A pays, at this scope, in two currencies — and the bill is now legible
because the coordinates are matched.** Its stated requirement is a covariant
co-reference rule for unrecorded configurations. On this base, at the read
times strictly between the declared division events, no candidate inside the
declared corridor delivers a certified one, and the two failures are of
different kinds:

- *At the second intermediate time*, no rule matching the full declared legs
  delivers a transport at any setting — and neither does the **record** class;
  the realized-only rule's two transports there are refused by the certificate.
  What blocks it is exhibited: the two
  frames' occupied configuration sets are disjoint at every cross-frame pair of
  the twelve charts, related at four settings by the base's own wing exchange
  and cardinality-forced apart at the other two. This is a price on *any*
  cross-frame co-reference at that time, not on unrecorded configurations
  specifically. What O4-A needs there is not merely missing; the coordinate at
  which it would have to live is one at which the two frames' index-2 moments
  are measured not to be the same moment.
- *At the first intermediate time*, a unique, covariant, corridor-bound
  transport of the unrecorded class **does** exist at every setting under every
  corridor-bound rule matching the full declared legs (and at the two symmetric
  settings under the realized-only rule as well) — and what it carries is **LTP-BARE**: at SP-C, SP-D and
  SP-F W5's forcing lemma fires, so that time is not a division event of the
  model as declared and no committed law conditions on the transported
  configuration; at the other three settings the shared record subalgebra is
  empty and nothing conditions on it either. The certificate is degenerate
  there — the two occupied configurations carry the same probability and no
  declared value distinguishes them — which is itself a statement about the
  price: at the one intermediate coordinate where the co-reference rule O4-A
  needs *is* available, the actuality it would carry is both lawless and
  value-indiscernible.

Leaving the corridor buys nothing either, and the measurement now says which
convention does the work. The naive slice rule reads a single time index shared
across contexts — the global present the charter's scope sentence withdraws —
and fails the no-slice gate at every one of the twelve charts. But its
**emptiness** at the final time is measured to be its leg-order convention, not
its slice reading: order-free, the same index-counting rule transports the
record class at every setting (C1a). What survives as a statement about the
slice reading is narrower and true: even order-free, an index-reading rule gets
zero at $t=2$, because the supports at the shared index are disjoint.

**O4-B pays what the charter says it pays** — T1 rewritten, definite pre-record
configurations no longer ontic, several of W5's correspondences changing type.
This unit adds no clause to it. What the arena test measures is O4-B's own
clause: unrecorded configurations are *variables of the nomological
representation*, and a representational variable's values are
representation-relative. Measured at name-free matched representatives, that
relativity is the frame dependence §6 already reports, at a proper subset of
§6's coordinates. The honest statement of the contribution is therefore: **the
charter's own O4-B clause, here measured, with its coordinates named** — and a
price on O4-A, which must say which arena's actuality is meant.

---

## 12. Scope and non-claims

1. **No claim about nature.** Every result is a statement about declared finite
   models, a declared gauge and declared finite search scopes.
2. **The fork is not adjudicated.** This unit measures prices; it does not
   choose a branch, and it claims no resolution of O4.
3. **Every claim is per coordinate**, and the read time is a coordinate. No
   claim is entered at a wider scope than the coordinate at which it was
   measured, and no class contrast is drawn between coordinates.
4. **The permutation scopes are declared and their effective content is
   gated.** The base scope has 72 elements and its $j_0$ filter admits exactly
   2; the declared extension has 96 and admits 8. Every negative is a negative
   at the stated scope.
5. **The read times are the model's own.** $t$ counts declared legs applied;
   $t=0$ and $t=3$ are the model's declared division events, so the pin's
   object — "the configuration between division events" — lives at
   $t \in \{1,2\}$. No other intermediate structure is constructed. The $t=3$
   column is the matched control, not the object.
6. **The matched table is diagonal in the read time.** Every candidate
   co-refers a chart's datum at $t$ with the other chart's datum at the *same*
   $t$ (and, under the no-slice probe, with the same *moment* in a re-indexed
   presentation). No candidate proposes to co-refer $F_1$'s datum at one read
   time with $F_2$'s at a different one; cross-time co-reference is outside
   the declared candidate space and is untested here. §7 is the reason it is
   the interesting successor question: at $t=2$ the two charts' index-2
   moments are measured not to be the same moment.
7. **The LTP selector's precedence is declared.** It tests the forcing lemma
   before the shared-record clause, so a coordinate carrying both a nonzero
   residual and a shared record law would be reported LTP-BARE and could not
   read LTP-LAWFUL. No such coordinate occurs on this base — the shared count
   is 0 at both intermediate read times and the residual is 0 at the final
   one — but the precedence is a declaration, not a measurement.
8. **W5's lemma is used in one direction only.** A nonzero residual shows a
   time is *not* a division event of the model as declared; a vanishing
   residual establishes nothing, and no claim here rests on the converse.
9. **The certificate's cross-frame reading is a declared position** (§3.2), not
   a measurement: the two frames are taken to live on one configuration space
   with one labelling, so the identity is the canonical cross-frame
   co-reference. A reader who rejects that position should read CERT as a
   name-bound test and the §6 obstruction as scoped to it; the transport
   counts, the orbit relation and the read-time structure are unaffected.
10. **The no-slice gate's clause N is measured to be the leg-normalisation
   clause** and the corridor's order-free stipulation is declared rather than
   gated; C1a measures its effect separately (§3.3, §5 reading 4).
11. **NAMEBLIND and the descent triple are decided at one declared
   relabelling** [SAMP]; the full declared scope is swept at the declared
   representative coordinates and reported in `O4-NAMEBLIND-SWEEP`, where the
   corridor verdict is measured uniform over the whole scope (72 of 72 for the
   Born-level rule, 96 of 96 for the sign-level rule, on both substantive
   classes) and the name-reading control is measured to survive at exactly one
   element — the trivial one — in each.
12. **W6, paper 2 and W5 are anchored, not re-derived.** Twenty-seven anchors
    reproduce their committed values exit-1; one divergence is disclosed in the
    deviations appendix.
13. **Nothing is claimed about locality, topology, causality, spacetime,
    fields, QFT or gravity.** "Arena" is operational vocabulary for a declared
    tuple of committed fixtures.

---

## 13. The receipt

`v13/code/o4_discriminator_exact.py` → `o4_discriminator_output.txt` +
`o4_discriminator_receipt.json`.

- **Anchors:** 27, exit-1-only, against the committed W6 note and receipt, the
  committed paper-2 bundle, and W5's LTP lemma. A15–A18 carry both their note
  and their `w6_output.txt` line; A19 is computed from occupancy rather than
  from the carrier size.
- **Gates:** 31, of which 27 are must-pass and 4 are declared disclosures; the
  falsification census below covers 26 of the 27 — the twenty-seventh is the
  falsification suite's own gate. These are the receipt's `O4-*` gates; the
  **ten** descent gates of §3.2 are a different object — they are measured per
  cell of the matched table and are reported there.
- **The matched table:** 54 cells (6 candidates × 3 classes × 3 read times),
  486 measured gate cells, all counts computed and none typed.
- **Mutants:** 31, each run to completion, each measured to exit 1 and to
  falsify at least one named gate or anchor; 31 of 31 died. **The set of
  must-pass gates that no mutant falsifies is empty**, at denominator 26. Each
  mutant declares its kind and the split is counted from the declaration:
  **24 perturb a computation and 7 are waivers** that overwrite a computed
  field after the fact. A waiver proves that a gate's predicate is load-bearing
  for the exit code, not that the gate would catch a computational defect, and
  the two are not claimed to be the same thing.
- **The suite covers** the reused anchors (the base's realized-legs finding and
  $U_{\text{prep}}$'s never-occupied block; the LTP residual's composition
  order), two direction conventions (the sign at which legs are matched, the
  time orientation of the realized restriction), **the read-time coordinate**
  (a class read at the wrong time; a chart's record set taken without its read
  time), **the candidate-rule consistency of the declared triple**, a
  name-reader, a global-now smuggler, a name-mixing arena quantity, a leg-prefix
  widener, an action-weakener, a subsampled gauge and a subsampled scope, a
  cache-reading self-test, a stubbed LTP selector, an injected shared record
  law, a wrong-time support read, a truncated descent triple, **a table
  computed at one declared read time fewer**, a float, and waivers of the
  certificate, the covariance gate, the negative control, the canonicaliser,
  the vocabulary and the declaration.
- **Self-test:** evaluates **fresh** — the value cache, which is also the
  leg-compatibility cache, is bypassed and the phase's cache-hit count is gated
  at zero with its miss count gated positive (§14 addendum). The tested set is
  fixed by declaration (the full arena action at every setting, candidate and
  read time, for both substantive classes — 2,160 instances, 1,728 of them
  under a nontrivial action) and its expected size is gated against the
  **declared** action enumerated independently of the running scope, so a
  subsampled action or gauge cannot shrink the gate in step with the sweep;
  the phase records 11,880 cache misses and 0 hits. The self-test's failure counts are reconciled against the
  covariance gate's own counts, so neither row can report only its own number.
- **Exactness:** the totally real quartic field $\mathbb{Q}(\cos\pi/8)$ of the
  committed model, where tuple equality is field equality, plus
  `fractions.Fraction`. An AST sweep finds no float literal and no call to
  `float` in any substantive path, and a runtime type sweep finds no float in
  any value that reached a gate or an anchor.
- **Determinism:** no wall-clock value enters the receipt or the rendered
  output; two delivery-mode runs were executed and their artifacts are
  byte-identical.

---

## Appendix: deviations

**D0 — the delivered read-time conflation, owned.** As first delivered, this
unit read the record class at the final time and the unrecorded-configuration
class at the intermediate time, and reported the difference between them as a
**class** discrimination. That is a coordinate effect: the class variable was
confounded with the read time, and at matched read times the discrimination is
null (§5 reading 1). The disconfirming measurement was already in the unit's
own anchor list — A13, the base's $|\Phi_B| = 0$ at the intermediate slice,
passing exit-1 — and was never brought to bear on the comparison. The
like-for-like gate as delivered compared function signatures, which cannot see
a read time. Both are repaired here: the read time is a declared coordinate
carried in every datum, the like-for-like gate measures coordinate equality in
every cell, and the `readtime-conflate` mutant reproduces the defect and dies.
The delivered unit verdict `O4-DISCRIMINATED-RECORD-ACTUALISM +
O4-ARENA-RELATIVE` is withdrawn (§10.2). This appendix entry is the deviation;
the rest of the paper states only what the matched table supports.

**D1 — one committed count does not reproduce, and the reason is a finding.**
W5's anchor A3 prints the divisibility census $(0,0,576,576,0,576)$: the matrix
residual differing in 16 entries in each of the 36 columns. Recomputed on
*this* base the count is $(0,0,288,288,0,288)$ — 16 differing entries in each of
18 columns. The diagnosis is that W5 rebuilt the model from the
singlet dictionary and chose a different orthogonal completion of
$U_{\text{prep}}$ off the $j_0$ column, and the matrix residual reads those
columns. What is *measured* here is the divergence itself and what survives it:
two builds of the **same** declared $j_0$ column give different matrix counts
and the same vector count. The $j_0$ column — the only column the model's own
admissible $p(0)$ ever reads — agrees exactly, which is anchor A25, together
with both value censuses (A27), and A26's completion-independent form ("every
column that differs at all differs in exactly 16 entries") reproduces. So the
matrix census is completion-dependent, the vector census is not, and W5's A3/G4
matrix count is not determined by anything W5 anchors. **No claim is entered
here about W6's own quantity:** the base's note states in terms that its finding
is *not* an artifact of $U_{\text{prep}}$'s arbitrary orthogonal completion, so
this divergence is not carried as a second confirmation of it.

**D2 — the descent-restriction rule ships at two matching levels, not one.**
The pin names candidate rules but does not fix their matching level, and the
level is not a free parameter here: the corridor's covariance clause selects
it. Both readings are declared and both are measured — **C2** at the Born
level, which is the level at which the base measures its own groupoid to act,
and **C2X** at the exact amplitude level, whose measured covariance failure
under the checkpoint-phase switchings is reported as a result and whose verdict
is `O4-BLOCKED-AT-<COVAR>` at every read time. The level census gate makes the
underlying fact a standalone measurement at all three declared levels.

**D3 — the acting group is the admitted 2, not the declared 8.** The pin names
"the admitted isomorphism group of that base". The base declares a 72-element
scope admitting 2 after its $j_0$ filter, and a 96-element extension admitting
8. The 96-element set is not closed under its own conjugation, so an action
drawn from it would test a candidate's declared search scope rather than the
candidate. The acting group is therefore the admitted 2, which every
candidate's search scope contains; the 8-element figure is carried in the arena
declaration as a disclosure, and C3's search scope is the full 96.

**D4 — CERT is a class-level certificate, so it repeats across candidate
rows.** The ROUTE-EXT certificate reads the two charts' data at the cell's read
time, not the transport, so its value depends on the fact-class, the setting
and the read time but not on the candidate. It appears once per (candidate,
class, read time) cell for like-for-like presentation; the underlying
measurement is per (class, setting, read time) and is reported that way in the
receipt. Its cross-frame reading is a declared position (§3.2, §12(9)).

**D5 — an empty corridor row is declared empty.** Where a candidate admits no
F-CFG transport, its covariance row is satisfied vacuously. The verdict
derivation therefore reads the corridor on **every** class the rule is applied
to, and the coordinates at which each cell's rows are vacuous — and those at
which the certificate is degenerate — are listed in a disclosure gate.
Name-blindness is the one corridor gate carved out of the all-classes reading,
because the negative control is *defined* as the class that reads names: its
failure there is the control firing, not the rule leaving the corridor. The
carve-out is declared, and the corridor census carries both of its controls.

**D6 — the pin's wording for `O4-ARENA-RELATIVE` is not sustained.** The pin
registers that outcome as "a sharpened form of O4-B, distinct from both charter
branches". Measured against paper 0's actual text, it is not distinct from
O4-B: that branch already holds unrecorded configurations to be variables of
the nomological representation, and a representational variable's values are
representation-relative. The outcome is withdrawn on measurement grounds
(§10.2) and the pin's characterisation is recorded here as the deviation rather
than repeated.

**D7 — the no-slice gate's measured scope.** The gate is named for the global
slice it excludes, and its second clause does measure index-reading; but its
first clause is measured, over an eight-point sweep, to be sensitive to the
identity-leg normalisation alone. The corridor's order-free stipulation is
therefore declared and measured separately (C1a) rather than gated, and clause
I is degenerate wherever a class's datum has no read time — all twelve charts
of the name-reading control. Both facts are disclosed in
`O4-NOSLICE-SENSITIVITY` rather than left to the gate's name.

**D8 — no Lean.** As the pin states.
