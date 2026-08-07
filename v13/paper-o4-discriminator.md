# The O4 Discriminator

## Unrecorded Actuality on the Record Co-reference Base

**Status:** `GREEN-UNREVIEWED (v13 O4-DISCRIMINATOR)` — delivered against the
frozen pin; the three-lens panel, the adjudication and the STATUS update
follow.

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
whether unrecorded configuration facts descend **under the same instrument**.

One transport instrument, ten gates, three declared fact-classes, applied
identically. The record class reproduces the base's terminal descent results
under this instrument (positive control). A deliberately mis-conventioned
name-reading class fails (negative control). The unrecorded-configuration
class is obstructed, and the obstructing object is exhibited: at every one of
the six committed settings the two frames' **occupied configuration sets at
the intermediate time are disjoint** — not merely unequal, but sharing no
configuration at all, so no proposition of the form *"the configuration
between the division events is $i$"* is true in both frames.

Four candidate co-reference rules are declared inside the pin's corridor —
covariant, name-blind, no global slice — before any fixture value is computed.
The naive slice rule is gated out by the no-slice gate, which is measured to
bite. The descent-restriction rule and the modal-carrier rule (the one the
base's own "identification is carried by transitions the process never takes"
suggests) both leave the unrecorded class ABSENT at every coordinate. The
realized-only rule admits exactly one transport, at the two settings where the
measurement angles coincide — and what it would carry is **LTP-BARE**: W5's
forcing lemma fires at SP-F, and at SP-E the shared record subalgebra at that
time is measured empty, so no committed law conditions on the transported
datum there either.

The arena test decides the shape of the result. Pushed through the base's
admitted isomorphism group and the checkpoint-phase switchings, the record
class's truth-values move only with the setting coordinate; the
unrecorded-configuration class's truth-values move with the **frame** and
**relabelling** coordinates as well, in orbits of measured size 2, with four
distinct truth-value vectors over an arena of size 192.

**Unit verdict: `O4-DISCRIMINATED-RECORD-ACTUALISM + O4-ARENA-RELATIVE`**, at
the committed finite scope, per coordinate. The charter fork is **not**
adjudicated here.

---

## 1. The question, made decidable

Paper 0 v2.4 §5 states the fork and its prices.

> **O4-A (configuration realism):** unrecorded local configurations are actual
> but ephemeral. **Price:** a new covariant co-reference rule for unrecorded
> local configurations is required; the slice-indexed composite formalism does
> not provide one; W5's LTP-forcing lemma is the fulcrum, since under O4-A the
> composite has definite actuality at intermediate times to which no
> probability law attaches.
>
> **O4-B (record actualism):** only records are actual. **Price:** the atlas
> postulate must be rewritten; definite pre-record configurations cease to be
> ontic; several of W5's correspondences change type.

The charter's scope sentence binds this unit: *no global present, no global
configuration history, no global event set.* A candidate rule that recovers
co-reference by imposing a single time index shared across contexts is
therefore outside the corridor by construction, and this unit's job is to make
that exclusion a **measurement** rather than a stipulation.

The discriminator's form, from the pin: on the record co-reference base — where
record facts provably descend — **construct the rule O4-A needs, or exhibit its
obstruction, at the committed finite scope.**

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
| arena, part 1 | the admitted isomorphisms: **2** of the declared 72-element permutation scope (96 with its declared extension) after the base's own $j_0$ filter | W6 SCOPE clause 2 |
| arena, part 2 | the checkpoint-phase switchings: **8** $= 2^3$, one sign per declared leg | W6's declared *sign* matching level |
| **arena size** | **192** | computed as $6 \times 2 \times 2 \times 8$ |

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

### 3.1 Three fact-classes, one gate set

A **fact-class** assigns to each chart a set of carriers with declared data,
and a rule for pushing that data along a configuration bijection. Three
classes are declared, and all three are routed through the same ten gates by
the same code path; the like-for-like property is itself gated (the three
transport functions are measured to share one signature).

| class | carriers | datum | role |
|---|---|---|---|
| **F-REC** | the chart's record tokens | the joint law of their declared values on the actual (positive-probability) value tuples, read at the time every token has been written | **positive control** |
| **F-CFG** | the 36 configuration propositions "the configuration is $i$" | at the intermediate time, between the declared division event $0$ and the final time: the actuality bit and the exact probability of every configuration | **the object** |
| **F-CTRL** | the same 36 carriers | the configuration's own integer **name** | **negative control** |

F-CTRL is mis-conventioned in exactly one respect: it reads a label the
declared gauge is free to change. It must fail the gates records pass; a pass
would mean the instrument cannot tell a fact from a name, and the run says so
in that case.

### 3.2 The ten gates

| gate | what it measures |
|---|---|
| **EXIST** | a transport exists on every declared edge |
| **FORCED** | the transport is unique on every declared edge |
| **INV** | the inverse of an admitted transport is admitted in reverse |
| **TRI** | triple coherence on the declared triple |
| **GLUE** | a coherent family in one gauge orbit with an injective colimit |
| **CERT** | the transported datum is *certified*, not merely compatible |
| **COVAR** | the verdict is equivariant under the admitted arena action |
| **NAMEBLIND** | the verdict survives a pure configuration relabelling |
| **NOSLICE** | the verdict survives a pure time re-indexing |
| **LTP** | a committed probability law conditions on the transported datum |

EXIST/FORCED are read through the base's own five-valued discriminator
(FORCED / UNDERDETERMINED / ABSENT / VACUOUS / NO-INSTRUMENT), so the
vocabulary is emitted rather than typed. TRI/GLUE are read through the base's
own descent solver on the base's own declared triple: the two frames plus the
second frame presented on a relabelled configuration set, built as its own
object with its own legs, its own initial configuration and its law
recomputed. CERT is the base's ROUTE-EXT construction with its pair guard
intact: a configuration on which the two charts disagree disqualifies the pair,
because a certificate on the remainder certifies nothing about the pair.

### 3.3 The no-slice gate, and how it bites

The gate must exclude any rule that recovers co-reference from a shared global
time index, and it must do so by measurement.

> **The test.** Prepend an identity leg to a chart. The process is the same
> object, presented on a shifted index; no transition has been added. A rule
> inside the corridor identifies the chart with its own re-indexed
> presentation exactly as it identifies the chart with itself. A rule that
> reads a global time slice cannot, because the index moved.

The reference is the rule's *own self-transport count*, so a rule cannot pass
by returning zero twice. A rule inside the corridor normalises by dropping
legs that carry every configuration in their own domain to itself — an
identity leg is no transition at all — and matches the remaining legs
order-free, which is the base's own declared choice (two frames of one
experiment differ exactly by the order of two commuting legs).

Measured: the naive slice rule fails NOSLICE at **every one of the twelve
charts**, for all three fact-classes, and is the only declared rule that does.
The `global-now-smuggler` mutant restores the index-reading normalisation
inside an otherwise corridor-bound rule; the no-slice rows then empty the
corridor census's inside set, and the mutant dies there.

---

## 4. The candidate rules, declared before fixture truth

The freeze gate measures that the fact-datum evaluation counter is **zero**
when the declarations are recorded, and that no gate has yet been entered; the
receipt's gate order is the proof (§13(4)). The `freeze-lax` mutant evaluates
one fixture datum first and dies there.

| id | rule | matching level | search scope | corridor claim |
|---|---|---|---|---|
| **C1** | **NAIVE-SLICE** — same configuration label at the same declared time index; legs matched *in order*, identity legs counted | exact | 72 | declared *outside*: the gated-out control |
| **C2** | **DESCENT-RESTRICTION** — co-reference only where the base's groupoid acts: an admitted frame-isomorphism, order-free, blind to identity legs, carrying the intermediate datum | Born | 72 | inside |
| **C2X** | **DESCENT-RESTRICTION-AT-THE-AMPLITUDE-LEVEL** — C2 with one declaration changed: legs must match on the nose | exact | 72 | inside (claimed) |
| **C3** | **MODAL-CARRIER** — carried by the **full declared legs, including never-taken transitions**, matched up to the per-leg sign | sign | 96 | inside |
| **C4** | **REALIZED-ONLY** — carried by the realized process alone: each leg restricted to the configurations actually occupied before and after it | Born | 72 | inside |

**Why C2's level is Born.** The base measured that what cuts the record-level
wing tie is the legs' **Born shadows alone** — amplitude phases play no part.
C2 is the rule "co-reference where the groupoid acts", so it inherits the level
at which the groupoid is measured to act.

**Why C2X exists.** So that what the corridor does to the matching level is
*reported* rather than chosen. C2X is C2 read at the amplitude level, and it is
then asked to be invariant under the checkpoint-phase switchings, which are
exactly the amplitude gauge.

**Why C3 is the candidate the base suggests.** The base's deepest finding is
that at the symmetric settings the record-token identification is carried by
$U_{\text{prep}}$'s columns on the 35 configurations the process never
occupies — *the identification is carried by transitions the process never
takes.* C3 asks whether F-CFG transport can be carried by the same modal
structure. C4 is its mirror: nothing counterfactual is consulted.

---

## 5. The fact-class gate table

`PASS` / `fail` as measured. The LTP column is §7.

| candidate | class | EXIST | FORCED | INV | TRI | GLUE | CERT | COVAR | NAMEBLIND | NOSLICE |
|---|---|---|---|---|---|---|---|---|---|---|
| **C1** NAIVE-SLICE | F-REC | fail | fail | fail | fail | fail | PASS | PASS | PASS | **fail** |
| | F-CFG | fail | fail | fail | fail | fail | fail | PASS | PASS | **fail** |
| | F-CTRL | fail | fail | fail | fail | fail | fail | PASS | fail | **fail** |
| **C2** DESCENT-RESTRICTION | **F-REC** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| | **F-CFG** | **fail** | fail | fail | fail | fail | **fail** | PASS | PASS | PASS |
| | F-CTRL | PASS | PASS | PASS | fail | fail | **fail** | PASS | **fail** | PASS |
| **C2X** at the amplitude level | F-REC | PASS | PASS | PASS | PASS | PASS | PASS | **fail** | PASS | PASS |
| | F-CFG | fail | fail | fail | fail | fail | fail | PASS | PASS | PASS |
| | F-CTRL | PASS | PASS | PASS | fail | fail | fail | **fail** | fail | PASS |
| **C3** MODAL-CARRIER | **F-REC** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| | **F-CFG** | **fail** | fail | fail | fail | fail | **fail** | PASS | PASS | PASS |
| | F-CTRL | PASS | PASS | PASS | fail | fail | fail | PASS | **fail** | PASS |
| **C4** REALIZED-ONLY | F-REC | fail | fail | fail | PASS | PASS | PASS | PASS | PASS | PASS |
| | F-CFG | fail | fail | fail | fail | fail | fail | PASS | PASS | PASS |
| | F-CTRL | fail | fail | fail | fail | fail | fail | PASS | fail | PASS |

**The transport counts, per setting.**

| candidate | class | SP-A | SP-B | SP-C | SP-D | SP-E | SP-F |
|---|---|---|---|---|---|---|---|
| C1 | F-REC / F-CFG / F-CTRL | 0 | 0 | 0 | 0 | 0 | 0 |
| C2, C2X, C3 | **F-REC** | **1** | **1** | **1** | **1** | **1** | **1** |
| C2, C2X, C3 | **F-CFG** | **0** | **0** | **0** | **0** | **0** | **0** |
| C2, C2X, C3 | F-CTRL | 1 | 1 | 1 | 1 | 1 | 1 |
| C4 | F-REC | 0 | 0 | 0 | 0 | **1** | **1** |
| C4 | **F-CFG** | 0 | 0 | 0 | 0 | **1** | **1** |
| C4 | F-CTRL | 0 | 0 | 0 | 0 | 0 | 0 |

Three readings, each measured.

1. **The positive control fires.** Routed through *this* unit's instrument —
   the same ten gates, the same discriminator, the same solver — the record
   class reproduces the base's terminal results: FORCED at every setting, the
   inverse law holding, the declared triple descending over all six ordered
   edges and all six ordered triples. Twenty-seven anchors pin the reused
   values exit-1 against their committed receipts.

2. **The negative control fails, under every candidate.** F-CTRL fails at
   least one gate for each of the five rules; where it admits a transport at
   all, it fails NAMEBLIND — the gate its mis-convention was built to fail —
   and the certificate.

3. **C4 reproduces the base's realized-legs finding, and extends it.** The
   record class under the realized restriction is ABSENT at the four
   asymmetric settings and FORCED at the two where the angles coincide,
   exactly as the base measured. The unrecorded class under the same
   restriction has the *same* profile — which is the one place in this unit
   where an F-CFG transport exists at all.

---

## 6. The obstruction, named

The instrument's central negative is not a bare zero. The obstructing object
is exhibited as data: the occupied configuration sets at the intermediate
time, computed from the model's own declared initial configuration.

| setting | frame F1 occupied | frame F2 occupied | $\lvert \cap \rvert$ | $\lvert \cup \rvert$ |
|---|---|---|---|---|
| SP-A | $\{12,24\}$ | $\{1,2,10,11,19,20,28,29\}$ | **0** | 10 |
| SP-B | $\{12,24\}$ | $\{1,2,10,11,19,20,28,29\}$ | **0** | 10 |
| SP-C | $\{3,6,12,15,21,24,30,33\}$ | $\{1,2,10,11,19,20,28,29\}$ | **0** | 16 |
| SP-D | $\{3,6,12,15,21,24,30,33\}$ | $\{1,2,10,11,19,20,28,29\}$ | **0** | 16 |
| SP-E | $\{12,24\}$ | $\{11,19\}$ | **0** | 4 |
| SP-F | $\{3,6,12,15,21,24,30,33\}$ | $\{1,2,10,11,19,20,28,29\}$ | **0** | 16 |

> **The obstruction.** At every one of the six committed settings the two
> frames' occupied configuration sets at the intermediate time are
> **disjoint**. No proposition of the form *"the configuration between the
> division events is $i$"* is true in both frames — not at the setting where
> the two sets have the same size (SP-E), and not anywhere else. That is the
> object on which every F-CFG transport count in §5 is measured to die, and it
> is why the certificate refuses the pair: the pair guard sees a configuration
> on which the two charts disagree at every setting.

This is the support-side form of the base's own control 4 (the shared record
subalgebra at the intermediate time is derived empty at every setting, against
two at the final time). Where the base measured that the *records* do not
overlap there, this unit measures that the *configurations* do not either.

The `support-lax` mutant reads the class's datum at the final time instead of
the intermediate one, at which point the two frames agree and the
intersections become nonzero; it dies at this gate.

---

## 7. The LTP gate

Every candidate must state what probability law attaches to the actuality it
transports. The gate computes it rather than asserting it, in three steps.

1. **The intermediate-time actuality is exhibited** — §6's table.
2. **W5's forcing lemma is evaluated at that time**, on the model's own
   admissible $p(0) = \delta_{j_0}$. Writing $D_{210} = \Gamma(3{\leftarrow}0)
   - \Gamma(3{\leftarrow}2)\,\Gamma(2{\leftarrow}0)$ for the declared-law
   residual, the lemma's contrapositive says: if $D_{210}\,p(0) \neq 0$ then
   the intermediate time **is not a division event of that model as
   declared** — so no committed law conditions on the transported
   configuration there.
3. **The record side is checked too:** a committed *record* law would
   condition on the datum only if some declared record token had been written,
   in both frames, by the intermediate time. That count is measured.

**The residual, recomputed on this base (both frames identical):**

| setting | SP-A | SP-B | SP-C | SP-D | SP-E | SP-F |
|---|---|---|---|---|---|---|
| $\lVert r \rVert_0$ of 36 | 0 | 0 | **16** | **16** | 0 | **16** |
| shared record partitions at that time | 0 | 0 | 0 | 0 | 0 | 0 |

The value censuses reproduce the committed ones exactly: at SP-C, four
distinct values with **zero** rational entries of the sixteen; at SP-F, six
distinct values with **eight of sixteen** rational. Rationality is decided by
the field's own test, never by a tolerance.

**The gate's verdict, per candidate and per coordinate.**

| candidate | SP-A | SP-B | SP-C | SP-D | SP-E | SP-F |
|---|---|---|---|---|---|---|
| C1, C2, C2X, C3 | n/a | n/a | n/a | n/a | n/a | n/a |
| **C4** | n/a | n/a | n/a | n/a | **LTP-BARE-UNWITNESSED** | **LTP-BARE** |

`n/a` = no transport admitted, so no actuality is transported and the gate has
nothing to attach a law to. For C4 the two live coordinates read:

- **SP-F — LTP-BARE, forced.** The residual is nonzero, so by the lemma the
  intermediate time is not a division event of the model as declared. The
  transport carries actuality; nothing in the committed law conditions on it.
- **SP-E — LTP-BARE-UNWITNESSED.** The residual vanishes, so the forcing
  lemma does not fire; but the shared record subalgebra at that time is
  measured empty, so no committed law conditions on the datum there either.
  The gate distinguishes the two cases and does not report the second as the
  first.

`LTP-LAWFUL` is reachable by the gate — it fires whenever a shared record law
conditions on the datum — and is measured never to obtain on this base. That
is a measured negative, not a stipulation.

---

## 8. The arena test

Both classes' truth-values are pushed through the same admitted action, over
all 192 arena points.

| quantity | role | verdict | moves under | distinct values over the family | orbit per chart |
|---|---|---|---|---|---|
| **QA1** F-CFG truth-value vector (the 36 named propositions) | the object | **ARENA-ARTIFACT** | setting, **frame**, **relabelling** | **4** | **2** |
| **QA2** F-REC truth-value set (the actual record values) | positive control | ARENA-ARTIFACT | setting | 2 | 1 |

Neither quantity moves under the checkpoint-phase switchings — the Born shadow
is switching-invariant, and the sweep is run to show it rather than assumed.

The discriminating comparison is the last three columns.

> **Measured.** The record class's truth-values are invariant under the frame
> coordinate and under the admitted relabellings: orbit size **1** at every one
> of the twelve charts. The unrecorded-configuration class's truth-values move
> under both: orbit size **2** at every one of the twelve charts, four distinct
> truth-value vectors over the whole arena.

The frame coordinate is the sharp one. The two frames are declared by the base
to be *the same two local events in the two orders, on one configuration
space* — one experiment. The record facts of that experiment are the same
facts in both frames, and this unit's positive control certifies it. The
unrecorded configuration facts are not: which configuration is actual between
the division events is a function of the frame, and the frame is arena data.

**The corridor's own two controls.** At least one declared candidate is
measured inside the corridor and at least one outside — a corridor every
candidate passes tests nothing, and a corridor no candidate passes tests only
the corridor. Measured: C2, C3 and C4 inside; C1 (no-slice) and C2X
(covariance) outside.

**The level census.** The same rule run at all three declared matching levels,
with its invariance under the checkpoint-phase switchings measured at each:
the **exact** level is measured *not* invariant, the **sign** and **Born**
levels are. The corridor's covariance clause therefore selects the matching
level as a measurement, and the sign/orientation mutants die at this row.

---

## 9. Verdicts

### 9.1 Per candidate

| candidate | verdict (per coordinate) |
|---|---|
| **C1** NAIVE-SLICE | `O4-BLOCKED-AT-<NOSLICE: the rule leaves the declared corridor>` |
| **C2** DESCENT-RESTRICTION | `O4-DISCRIMINATED-RECORD-ACTUALISM` [SP-A, SP-B, SP-C, SP-D, SP-E, SP-F] |
| **C2X** at the amplitude level | `O4-BLOCKED-AT-<COVAR: the rule leaves the declared corridor>` |
| **C3** MODAL-CARRIER | `O4-DISCRIMINATED-RECORD-ACTUALISM` [SP-A, SP-B, SP-C, SP-D, SP-E, SP-F] |
| **C4** REALIZED-ONLY | `O4-BLOCKED-AT-<no certified transport for either class>` [SP-A, SP-B, SP-C, SP-D] `+ O4-DISCRIMINATED-RECORD-ACTUALISM` [SP-E, SP-F]; LTP gate **LTP-BARE** |

Every verdict is derived from the measured gate rows and from nothing else. A
declaration flip-test gate re-derives each candidate's verdict with its
declared corridor claim flipped to its opposite; the results must be
identical, and are. The `declaration-lax` mutant lets the declaration reach
the result and dies there. The vocabulary gate measures that every verdict
emitted begins with one of the pin's five pre-registered names.

**The modal candidate's answer, stated plainly.** C3 asks whether the modal
structure that carries the base's record-token identification — the columns of
$U_{\text{prep}}$ on the 35 configurations the process never occupies — can
also carry unrecorded configuration facts. Measured: it cannot. Those columns
identify record *tokens* because tokens are partitions of the whole
configuration space and a never-taken transition still constrains a partition.
They cannot identify configuration *propositions*, because the datum a
configuration proposition carries is its actuality at the intermediate time,
and that datum lives on the occupied support, which the frames do not share.

### 9.2 The unit

> **`O4-DISCRIMINATED-RECORD-ACTUALISM + O4-ARENA-RELATIVE`**

Both parts are pre-registered outcomes of the pin and both are earned by
measurement, at the committed finite scope, per coordinate:

- **O4-DISCRIMINATED-RECORD-ACTUALISM** — the record control is green (FORCED
  at all six settings under C2 and C3, with the declared triple descending),
  while the unrecorded class is obstructed at every coordinate at which the
  record class is green, with the obstruction constructive and named (§6).
- **O4-ARENA-RELATIVE** — F-CFG's truth-values are measured to move under the
  admitted arena action at coordinates where F-REC's do not, with the orbit
  computed (§8).

The other three pre-registered outcomes do **not** obtain.
`O4-RULE-EXISTS` does not obtain at any coordinate: no candidate delivers a
certified, unique, covariant transport for the unrecorded class anywhere.
`O4-RULE-EXISTS-LTP-BARE` does not obtain as a candidate verdict — the one
rule that admits a transport (C4 at SP-E/SP-F) fails the certificate that
records pass, so it does not "pass all the descent gates records pass"; what
it *would* transport is measured LTP-BARE, and that is reported as the LTP
gate's finding rather than promoted to a verdict. `O4-BLOCKED-AT-⟨object⟩`
obtains only per candidate and per coordinate as tabulated, never as the
unit's outcome: the census does not block.

---

## 10. What each charter branch pays under this verdict

This section states prices. It adjudicates nothing; the fork's resolution, if
any, is paper 0's to record and the user's to route.

**O4-A pays, at this scope, in one of two currencies.** Its stated
requirement is a covariant co-reference rule for unrecorded configurations.
Inside the declared corridor, no candidate delivers one: the transport dies on
an object that is exhibited, not merely absent. The two ways out that this
unit measured both cost something the charter has already priced:

- *Leave the corridor.* The naive slice rule reads a single time index shared
  across contexts — the global present the charter's scope sentence
  withdraws — and the no-slice gate is measured to bite on it at every one of
  the twelve charts. And leaving the corridor does not even buy a rule here:
  measured on this base, the slice rule admits **zero** transports at every
  setting for every fact-class, because the two frames of one experiment
  differ exactly by the order of two commuting legs and an index-bound rule
  cannot match them. The illegitimate route is not merely illegitimate; on
  this base it is empty.
- *Accept lawless actuality.* The only rule that admits any transport at all
  (the realized-only rule, at the two settings where the angles coincide)
  transports actuality to which no committed law attaches: forced by W5's
  lemma at SP-F, and unwitnessed-but-equally-bare at SP-E. This is the
  charter's own fulcrum sentence, now instantiated with numbers on the base.

**O4-B pays what the charter says it pays** — the atlas postulate rewritten,
definite pre-record configurations no longer ontic, several correspondences
changing type — and this unit adds one further clause, which is not in the
charter's statement of either branch:

> Record actualism as measured here is *sharper* than "only records are
> actual". What the arena test finds is that the truth-values of unrecorded
> configuration propositions **move with the arena** — with the frame and with
> the admitted relabelling — while record truth-values do not. On this base,
> "the configuration between the division events is $i$" is not a
> frame-independent proposition at all; it is arena-relative data. A branch
> that keeps unrecorded configurations as variables of the nomological
> representation is consistent with that; a branch that keeps them as actual
> must say which arena's actuality is meant.

---

## 11. Scope and non-claims

1. **No claim about nature.** Every result is a statement about declared
   finite models, a declared gauge and declared finite search scopes.
2. **The fork is not adjudicated.** This unit measures prices; it does not
   choose a branch, and it claims no resolution of O4.
3. **The permutation scopes are declared and their effective content is
   gated.** The base scope has 72 elements and its $j_0$ filter admits exactly
   2; the declared extension has 96 and admits 8. Every negative in this unit
   is a negative at the stated scope.
4. **Every claim is per coordinate.** The six settings and two frames are
   coordinates of the declared arena, and no claim is entered at a wider scope
   than the coordinate at which it was measured.
5. **The intermediate time is the model's own.** "Between division events"
   means: after the declared division event $0$ and before the final time, at
   the slice the base's own control 4 examines. No other intermediate
   structure is constructed.
6. **The LTP gate speaks about the exact, unmarginalised declaration.** W5's
   scope clause is inherited verbatim: the lemma tests the model's exact
   division-event declaration for the unmarginalised 36-configuration
   composite; an approximate, marginalised reading is a different claim and is
   untested here.
7. **W6, paper 2 and W5 are anchored, not re-derived.** Twenty-seven anchors
   reproduce their committed values exit-1; one divergence is disclosed in the
   deviations appendix.
8. **Nothing is claimed about locality, topology, causality, spacetime,
   fields, QFT or gravity.** "Arena" is operational vocabulary for a declared
   tuple of committed fixtures.

---

## 12. The receipt

`v13/code/o4_discriminator_exact.py` → `o4_discriminator_output.txt` +
`o4_discriminator_receipt.json`.

- **Anchors:** 27, exit-1-only, against the committed W6 note and receipt, the
  committed paper-2 bundle, and W5's LTP lemma.
- **Gates:** 21 in delivery mode, of which 18 are must-pass, 2 are declared
  disclosures, and one is the falsification suite's own gate.
- **Mutants:** 23, each perturbing a *computation* — none overwrites a
  computed field after the fact — each run to completion, each required to
  exit 1 and to falsify at least one named gate or anchor. The set of
  must-pass gates that no mutant falsifies is **empty**: the census covers 17
  and reports `never falsified []`, and the eighteenth — the vocabulary gate,
  which the census's own ordering places after it — is falsified by the
  out-of-vocabulary mutant, recorded in the mutant table's kill list.
- **The suite covers** the reused anchors (the base's realized-legs finding
  and $U_{\text{prep}}$'s never-occupied block; the LTP residual's
  composition order), two direction conventions — the sign at which legs are
  matched, and the time orientation of the realized restriction — a
  name-reader, a global-now smuggler that must be caught by the no-slice
  gate, the record-level tie left uncut, an action-weakener, a cache-reading
  self-test, a stubbed LTP gate, a negative control made to pass, a
  pre-freeze evaluation, an out-of-vocabulary verdict, a
  declaration-consulting verdict rule, a subsampled search scope, a
  subsampled gauge sweep, a float, a truncated descent triple, a collapsed
  canonicaliser, a waived covariance gate, a wrong-time support read, a
  waived certificate and a waived like-for-like check.
- **Self-test:** evaluates **fresh** — the value cache is bypassed and the
  phase's cache-hit count is gated at zero with its miss count gated positive
  (§14 addendum). The tested set is fixed by declaration (the full arena
  action at every setting), never selected by the verdicts under audit, and
  the count of instances at which the action is nontrivial is gated positive.
  The self-test's failure counts are reconciled against the covariance gate's
  own counts, so neither row can report only its own number.
- **Exactness:** the totally real quartic field $\mathbb{Q}(\cos\pi/8)$ of the
  committed model, where tuple equality is field equality, plus
  `fractions.Fraction`. An AST sweep finds no float literal and no call to
  `float` in any substantive path, and a runtime type sweep finds no float in
  any value that reached a gate or an anchor.
- **Determinism:** no wall-clock value enters the receipt or the rendered
  output; two delivery-mode runs are byte-identical, verified.

---

## Appendix: deviations

**D1 — one committed count does not reproduce, and the reason is a finding.**
W5's anchor A3 prints the divisibility census $(0,0,576,576,0,576)$: the
matrix residual differing in 16 entries in each of the 36 columns. Recomputed
on *this* base the count is $(0,0,288,288,0,288)$ — 16 differing entries in
each of 18 columns. The cause is measured and disclosed: W5 rebuilt the model
from the singlet dictionary and chose a **different orthogonal completion of
$U_{\text{prep}}$ off the $j_0$ column**, and the matrix residual reads those
columns. The $j_0$ column — the only column the model's own admissible $p(0)$
ever reads, and the one W5's own G1 says carries the whole residual — agrees
exactly, which is anchor A25 ($\lVert r\rVert_0 = 16$ at SP-C, SP-D, SP-F in
both frames, 0 elsewhere), together with both value censuses (A27). The
anchor that survives is therefore the completion-independent one: *every
column of the matrix residual that differs at all differs in exactly 16
entries*, which is W5's own "the same fact, seen once per column", and it
reproduces. The divergence is carried as a disclosure gate rather than
smoothed. It is also an independent confirmation, from a second direction, of
the base's finding that $U_{\text{prep}}$'s arbitrary completion off $j_0$ is
doing work.

**D2 — the descent-restriction rule ships at two matching levels, not one.**
The pin names candidate rules but does not fix their matching level, and the
level is not a free parameter here: the corridor's covariance clause selects
it. Both readings are therefore declared and both are measured — **C2** at the
Born level, which is the level at which the base measures its own groupoid to
act, and **C2X** at the exact amplitude level, whose measured covariance
failure under the checkpoint-phase switchings is reported as a result and
whose verdict is `O4-BLOCKED-AT-<COVAR>`. The level census gate (§8) makes the
underlying fact a standalone measurement at all three declared levels, so
neither reading is privileged by declaration.

**D3 — the acting group is the admitted 2, not the declared 8.** The pin names
"the admitted isomorphism group of that base". The base declares a 72-element
scope admitting 2 after its $j_0$ filter, and a 96-element extension admitting
8. The 96-element set is not closed under its own conjugation, so an action
drawn from it was measured to fail covariance for rules whose declared search
scope is the 72 — testing the scope rather than the rule. The acting group is
therefore the admitted 2, which every candidate's search scope contains; the
8-element figure is carried in the arena declaration as a disclosure, and C3's
search scope is the full 96.

**D4 — CERT is a class-level certificate, so it repeats across candidate
rows.** The ROUTE-EXT certificate reads the two charts' data, not the
transport, so its value depends on the fact-class and the setting but not on
the candidate. It appears once per (candidate, class) cell for like-for-like
presentation; the underlying measurement is per (class, setting) and is
reported that way in the receipt.

**D5 — an empty corridor row is declared empty.** Where a candidate admits no
F-CFG transport, its covariance row is satisfied vacuously. The verdict
derivation therefore reads the corridor on **every** class the rule is applied
to, so no rule reaches a verdict on a vacuous covariance row; and the
coordinates at which each candidate's F-CFG corridor rows are vacuous are
listed in a disclosure gate. Name-blindness is the one corridor gate carved
out of the all-classes reading, because the negative control is *defined* as
the class that reads names: its failure there is the control firing, not the
rule leaving the corridor. The carve-out is declared, and the corridor census
carries both of its controls.

**D6 — the falsification census counts 17 of the 18 must-pass gates.** The
census is taken when the mutant table runs, and the vocabulary gate is entered
after it, so the census's denominator is 17 and its `never falsified` set is
empty at that denominator. The eighteenth gate is not uncovered: the
out-of-vocabulary mutant is measured to falsify it, and that kill is recorded
in the mutant table itself. The bookkeeping gap is disclosed rather than
closed by reordering, because reordering would move the receipt.

**D7 — no Lean.** As the pin states.
