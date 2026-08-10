# WELD 2 (paper-13, the carrier census) — EFFECTUS-LENS HOSTILE REVIEW

**Reviewer:** EFFECTUS (meaning, scope, motivation).
**Protocol:** `v14/note-w2-hostile-protocol.md` (`e7b99e05557d`), ledger #93.
**Object, hashes verified at start (sha256-12, all seven match):**
paper `535e288ff412`, code `290149118b9d`, output `5e35e7a0115f`,
receipt `bacdb7a5e985`, pin `9d19515cb3ae`, protocol `e7b99e05557d`,
scout `425303a8ce1e` (worktree; the pin and paper cite `e1f771a9d0ed`,
the pre-#89 bytes, and §8.5 discloses exactly this — see D5 below).
**Execution:** scratch only,
`…/scratchpad/w2-ef/`, `/opt/homebrew/bin/python3.13`, exact arithmetic.
Repo unmodified by this review (`git status` carries no `w2_*` entry).

**GRADE: ACCEPT-WITH-FIXES.**
**Recomputations: 110** (ledger at the end).
**Findings: MAJOR-3, MINOR-9** (MINOR-9 is a bookkeeping/disclosure item,
not a defect).
**False computed numbers reaching the paper: 0.**
**False prose claims reaching the paper: 3** (one in the abstract, one in
§5, one in §8.2) — all repairable in a clause each, none overturning the
verdict.
**Wrong numbers in the receipt: 1 field** (`subsets_excluded`, MINOR-3),
which the paper silently corrected rather than rendered.

The verdict **survives every attack I ran**, including a constructed
counter-candidate. What does not survive intact is the *head's own
sharpening*: the obstruction the head names — the arity–cyclicity
scissors — is a theorem under a reading of "map" that the census
implements and the pin does not state, and under the pin's own reading
it decides 40 of 60 cells rather than 60. The repairs below are exact
and the unit's own machinery supports every one of them.

---

## 1. THE HEAD

`WELD2-EMPTY-AT-THE-DECLARED-FAMILY-THE-ARITY-CYCLICITY-SCISSORS@BOTH:MENU-113+CONG-185`

### 1.1 Is EMPTY-AT-THE-DECLARED-FAMILY the honest head?

**Yes, and it is the pin's own pre-registered outcome string** (pin
OUTCOMES: `WELD2-EMPTY-AT-THE-DECLARED-FAMILY-<obstruction>`). The
delivered string instantiates it and carries the obstruction, the
carrier stamp, the counts and the scope. On form, the head is clean:
nothing is asserted as a corpus theorem that is only a census outcome,
and §7's closing line ("Between delivery and adjudication this is a
candidate reading") is honoured in the gate statement itself
(`G-VERDICT` ends with the same clause), which is the #234 discipline
working as intended.

### 1.2 Is the FAMILY the pin's family?

**It is wider than the pin's on one axis and narrower on two, and only
one of the three is disclosed.**

| axis | pin R3 | delivered | direction |
|---|---|---|---|
| site | 5 generators | 5 | same |
| link | 3 generators | 3 | same |
| count | 1 generator | 1 | same |
| arity treatment | *not in the pin* | `{NONE, DECLARED-RESTRICTION}` | **widened ×2** |
| carrier | both, stamped | both | **inert ×2** (MAJOR-3) |
| "event subset" | *event* subset | *division-event* subset (2²⁰, not 2¹²⁴) | narrowed |
| admissibility | "a map sending grammar objects to sites" | a bijection + induced-subgraph isomorphism | **narrowed** (MAJOR-1) |

The arity-treatment widening is *conservative* — offering a repair can
only make FOUND easier, so EMPTY over 30 cells is a stronger negative
than EMPTY over 15 — and §3's lead-in ("The pin's generator vocabulary,
**and the arity treatments the census offers each cell**") is careful.
No finding; the arithmetic line `5×3×1×2×2` and the verdict's
`CANDIDATES=60` should nonetheless say which factors are the pin's.

The two narrowings are the findings. The event-subset one is harmless
(MINOR-8); the admissibility one is MAJOR-1 and is the decisive item of
this review.

### 1.3 Candidate readings of the head, enumerated

1. **"No motivated map exists from the AB4 transport grammar to I7's
   lattice."** — NOT licensed. Too strong on three counts: the family is
   a declared 5×3×1 vocabulary, not all maps; the scope is 2 actors at
   depth ≤ 4; and the admissibility test is the embedding reading
   (MAJOR-1).
2. **"No motivated map exists in the pin's declared vocabulary."** —
   NOT licensed as delivered. 20 of 60 cells are decided by gates
   stricter than the pin's wording (MAJOR-1); under the pin's own words
   those 20 are undecided by this unit.
3. **"No candidate in the declared vocabulary carries I7's lattice into
   the grammar as a sub-structure at this scope."** — **LICENSED.** This
   is what the code measures, and it is measured exhaustively and
   exactly.
4. **"36 of 60 cells fail a type test that no reading of 'map'
   repairs."** — **LICENSED, and reading-robust.** The type gate asks
   whether a pinned choice-free map carries the link generator's
   endpoint type to the site generator's object type; that question is
   the same in both directions. This is the reading-independent core of
   the result and the paper under-sells it.
5. **"The grammar is geometry-blind."** — NOT licensed, and §7
   explicitly disclaims it. Good.

### 1.4 Is the scissors a theorem about the CORPUS or about this unit's
vocabulary?

**About this unit's declared vocabulary, at this carrier, under the
embedding reading.** Two of its three quantifiers are honest and one is
not:

- *Over restrictions:* **genuinely a theorem.** A subgraph of a DAG is a
  DAG, so acyclicity decides all C(113,9), C(185,9), C(2²⁰,9), C(3969,9)
  restrictions at once, with no sampling. Verified: the topological sort
  completes on all 113 and all 185 vertices, and I confirmed acyclicity a
  third way (DFS three-colouring) at both carriers.
- *Over the target's periodicity:* **genuinely a theorem.** I verified
  that every declared link closes a 3-cycle on 3 distinct sites at all
  9 × 3 (site, link) pairs — 3 is prime and no declared displacement is
  zero. And "a self-loop is not a generator cycle" is right: a bijection
  sends distinct sites to distinct objects, so a loop is unusable.
- *Over link generators:* **not a theorem — a census of three.** The
  abstract's blade reads "**Every** link generator with 9 or more objects
  is acyclic." Unqualified, that is a claim about all link generators.
  It is true of the three declared ones. MINOR-7.

**Attack, run:** is there a generator or quotient outside the checked set
that is both ≥ 9 and cyclic? At the level of *this* vocabulary, no — the
three graded generators (Boolean-lattice cardinality, address length,
poset height) are acyclic by an identity of their definitions, which is
exact. But the attack lands one level up, and that is MAJOR-1: the
*lattice* has cycles and the *class graph* does not, yet a map from the
class graph **onto** the lattice does not need the class graph to have
cycles at all. I built one.

---

## 2. MAJOR FINDINGS

### MAJOR-1 — THE ADMISSIBILITY READING IS NARROWER THAN THE PIN'S QUESTION, AND THE NARROWING IS UNDECLARED; 20 OF 60 CELLS ARE READING-DEPENDENT

**The pin asks (R1/THE QUESTION, verbatim):** "a map sending grammar
objects to sites, grammar object-pairs/channels to links, and SETS OF
DIVISION EVENTS to link counts." That is a map **from** the grammar
**to** the lattice. Nothing in it requires injectivity, and nothing
requires the grammar's link relation to *contain* the lattice.

**The code implements the opposite direction.** `detect` step (2)
demands `arity == len(X)` — a **bijection** between site objects and the
nine sites — and step (3) demands an **induced-subgraph isomorphism**
(`graph_isomorphisms`, the `((u,w) in src) != ((x,phi[w]) in tgt)`
test). The comment at line 1653 and §5.1's prose then say "embedding":

> *"An embedding must carry those cycles into the candidate's link
> relation."*  (§5.1)

"Embedding" appears nowhere in the pin. The substitution is silent, and
it is what converts an absence into a theorem.

**Why it bites.** A quotient map φ: classes → X is exactly what the
pin's words admit, and acyclicity is no obstruction to one — a DAG maps
homomorphically onto a cyclic Cayley graph routinely. **Measured, on the
unit's own objects:**

| probe | MENU-113 | CONG-185 |
|---|---|---|
| Z₃ level grading (φ(v) = φ(u)+1 on every extension edge) | **fails** (the 45 self-loops force displacement 0) | **EXISTS** |
| arc-consistency for φ: classes → (Z₃)², every edge displacement in {(1,0),(0,1),(1,1)} | **domains wipe out — no solution, exactly** | **survives** |
| explicit witness φ | — | **FOUND** (fibre sizes 53, 21, 13, 6, 5, 13, 34, 26, 14) |
| best induced count field over 40 randomised solutions | — | **18 of 27 cells strictly positive** |

So on CONG-185 the cell `CONG-CLASS × EXTENSION-EDGE` is **not decided by
acyclicity**: a map exists, the site and direction choices are real, and
the fate would be decided further down the detector — at count
positivity (`COUNT-DEAD`, step 4) or, if some φ covered all 27 cells, at
the **choice inventory**. My 40 randomised solutions do not settle which;
the point is that **this unit never asked**.

**Which cells are affected.** Robust under both readings: the 36
TYPE-DEAD (the type question is direction-free), and the 4 ACTOR rows
(2 objects cannot cover 9 sites in either direction). Reading-dependent:
the **10 over-large ARITY-DEAD** (113, 185, 2²⁰, 3969 against 9 — a
quotient is exactly what over-largeness invites) and the **10
STRUCT-DEAD** (all acyclicity-based). **40 of 60 robust, 20 of 60
reading-dependent.**

**Why this is the decisive finding rather than a quibble.** The pin
pre-registered `I-SITE-ASSIGNMENT`, `I-DIRECTION-LABEL`, `I-ORIENT` as
*expected free items* — a pin expecting candidates to reach the inventory
and die there, as R6b′'s five did. §6 reports all three as "not reached"
and then reads that as a *strengthening*:

> *"The EMPTY is structural, not a matter of accumulated freedom. That is
> a stronger negative than the five UNMOTIVATED identifications R6b′
> recorded."*  (§6)

That sentence is the over-read. The inventory was not reached because a
gate the pin did not declare fired first. **FOUND = 0 with
UNMOTIVATED = 0 is honest about the census's own reading and misleading
about the pin's** — and the answer to the panel's question "does any
cell hide an UNMOTIVATED under a structural fate?" is **yes, 20 of them
may, and the unit cannot say which.**

**REPAIRS (exact).**
1. §1 and §5.1: replace "map" with the reading actually tested, once,
   explicitly: *"This census tests the **embedding** reading — a bijection
   from site objects to sites under which the grammar's link relation
   contains the lattice's. The pin's wording also admits the **quotient**
   reading, a surjection from grammar objects onto sites; that reading is
   not tested here."*
2. Head: insert the reading.
   `WELD2-EMPTY-AT-THE-DECLARED-FAMILY-UNDER-THE-EMBEDDING-READING-THE-ARITY-CYCLICITY-SCISSORS@…`
   and add a scope segment
   `READING=EMBEDDING(LATTICE-INTO-GRAMMAR)|MAP-READING-OPEN-AT-20-OF-60`.
3. §5 table: add a `reading-robust?` column — 36 TYPE-DEAD and 4 ACTOR
   rows YES, 10 ARITY-DEAD and 10 STRUCT-DEAD NO.
4. §6: delete "That is a stronger negative than the five UNMOTIVATED
   identifications R6b′ recorded" and replace with *"Under the embedding
   reading nothing reaches the inventory. Under the quotient reading the
   inventory is where 20 of the 60 cells would be decided, and this unit
   does not decide them."*
5. §9: register the quotient reading as the unit's **first open**, with
   the measured entry point (a Z₃ grading of the CONG-185 class graph
   exists; the MENU class graph admits none, exactly, because of its 45
   self-loops).

**The unit's own mutant confirms the diagnosis.** `--mutant
MUT-CYCLE-PLANT` plants a 3-cycle in the class-extension graph — exactly
the counterfactual MAJOR-1 describes. The fates then redistribute:

| fate | plain run | MUT-CYCLE-PLANT |
|---|---|---|
| TYPE-DEAD | 36 | 36 |
| ARITY-DEAD | 12 | 12 |
| ARITY-DEAD-BELOW | 2 | 2 |
| STRUCT-DEAD | **10** | **6** |
| **ARITY-REPAIR-UNDECIDED** | **0** | **4** |

The four `MENU-CLASS`/`CONG-CLASS` × `EXTENSION-EDGE` ×
`DECLARED-RESTRICTION` cells fall through to
`ARITY-REPAIR-UNDECIDED` — reason string *"cyclic and over-large;
handled at the repair row"* — and there **is no repair row**: this row
*is* the repair row. So the detector **never performs a declared
restriction**; it has no machinery to select 9 of 113 classes and no
fallback if acyclicity fails. `G-VERDICT`'s own pass condition encodes
this: it requires `fates.get("ARITY-REPAIR-UNDECIDED", 0) == 0`.

Consequence: §5.1's *"That decides all C(113,9), C(185,9), C(2²⁰,9) and
C(3969,9) restrictions in one step, with no sampling and no cap"* is
true — but only because acyclicity happens to hold. **Acyclicity is not
merely the census's stated mechanism; it is the only route by which this
detector can terminate on an over-large cell at all.** Under the quotient
reading, where acyclicity does not decide, the census as built would
return UNDECIDED on those four cells rather than a fate. That is the
measured cost of MAJOR-1, delivered by the unit's own instrument.
`G-CENSUS-COMPLETE`'s "every cell carries a measured fate, none is
skipped" is therefore **contingent on the scissors closing**, not true by
construction, and should say so.

**What the repair costs:** nothing in the verdict. EMPTY still stands at
the declared family. What it costs is the *claim to be structural rather
than choice-theoretic*, which is precisely the sentence the unit sells.

**What the repair BUYS:** a sharper and reading-independent mechanism at
MENU. Under the quotient reading MENU-113 dies **exactly**, by arc
consistency, because its 45 self-loops demand a displacement of zero and
no declared link is zero. That is a *second* blade, valid under both
readings, and the unit already has the datum (45) but does not use it
this way.

---

### MAJOR-2 — THE FOUND BRANCH HAS NEVER BEEN DEMONSTRATED AT THE TARGET THE VERDICT IS ABOUT, AND THE PIN'S OWN NAMED CONTROL RETURNS STRUCT-DEAD

Pin R5 carries HA §14 requirement 3 verbatim: *"A predicate that cannot
return its other value anywhere in the declared arena is not a
measurement."* The delivery honours it — at **a different target**.

Read from the code (lines 2179–2211): the census judges every candidate
against `TGT_I7` (`links7`, three links). Both FOUND-side controls
(`ctrl_found`, `ctrl_empty_flip`) are run against `TGT_CRY`
(`links7[:2]`, **two** links). **At `TGT_I7` the machinery has returned
only deaths — ever.**

I re-ran the detector across the (link generator × target) grid on the
crystal record:

| link generator | @ CRYSTAL-CARRIED-L2 | @ I7-DECLARED-L3 |
|---|---|---|
| ACTOR-PAIR (co-division incidence) | **FOUND**, isos 72, inventory 1/1/1 | **STRUCT-DEAD**, isos 0 |
| COVER-PAIR (**the generator the pin names**) | **STRUCT-DEAD**, isos 0 | **STRUCT-DEAD**, isos 0 |
| EXTENSION-EDGE | TYPE-DEAD | TYPE-DEAD |

Two things fall out.

**(a) The FOUND branch is reachable at exactly one of six
(generator, target) combinations**, and that combination is neither the
target the census judges nor the mechanism the pin named. Pin R5 says the
crystal control must return FOUND "**(the record's own cover structure
forcing the lattice)**" — the delivery substituted co-division incidence
on the ordered actor pair and did not report that the pinned generator
fails. Had the parenthetical been read as a requirement, the pin's own
abort clause ("else the detector is broken and the unit aborts") would
have fired.

**(b) The two controls are not the same standard.** The FOUND control's
"all three fibers 1" is measured over a strictly smaller arena of
choices than the census target would demand:

| | CRYSTAL-CARRIED-L2 (control) | I7-DECLARED-L3 (census) |
|---|---|---|
| links | 2 | 3 |
| incidence graph | rook's 3×3 (4-regular) | K₃,₃,₃ (6-regular) |
| \|Aut\| | **72** | **1296** |
| direction-label permutations | **2** | **6** |
| orientations | 2 | 2 |
| total configurations the inventory ranges over | **288** | **15 552** |

So `I-DIRECTION-LABEL = 1` at the control means "the **2** label
permutations give one field"; at the census target it would have to mean
"the **6** do". The control's zero-free-items is established over **1/54**
of the choice arena. And the 72 is not a coincidence: it is exactly
|Aut| of the target graph, i.e. the crystal's actor incidence **is** the
target, so the "72 site assignments all giving one count field" is the
automorphism group acting on an invariant — informative about
homogeneity, silent about the free-item accounting the census would use.

**On the smuggled-blueprint question specifically:** the smuggling is not
in the blueprint, it is in the target. The crystal's row/column actor
arrangement is a declared blueprint (scout SEED-2, d47 pin §3), §8.1
cites that, and the control's job — showing the FOUND branch exists —
would survive it. What does not survive is the substitution of a 2-link
target for the 3-link one under a segment (`CONTROLS=FOUND-AT-CRYSTAL(…)`)
that carries no target stamp while the *very next* segment
(`CRYSTAL-AT-I7(STRUCT-DEAD)`) does.

**(c) The falsifier's own description is false in one coordinate.** §4.3
and `G-CTRL-EMPTY-FALSIFIABLE` both say:

> *"the **identical call** on the crystal record returns FOUND"*

`ctrl_empty` is `detect(walk_arena, …, TGT_I7)`; `ctrl_empty_flip` is
`detect(cry_arena, …, TGT_CRY)`. **Two** coordinates change, not one.
The conclusion drawn ("EMPTY at the walk is a property of the walk")
happens to be true — the walk dies on 2-vs-9 arity, which is a property
of the walk — but it is not what the exhibited call shows.

**REPAIRS (exact).**
1. Verdict string: stamp the target into the FOUND segment —
   `FOUND-AT-CRYSTAL@CRYSTAL-CARRIED-L2(FOUND-candidate,ISOS=72,FIBERS-ALL-1,LABEL-PERMS=2)`
   and add `FOUND-AT-I7-TARGET=NEVER-DEMONSTRATED`.
2. §4.1: add the arena-of-choices row — 72 × 2 × 2 = 288 configurations
   at the control against 1296 × 6 × 2 = 15 552 at the census target.
3. §4.2 / new deviation: report that the **pin's named control
   generator** (the record's own cover structure) returns STRUCT-DEAD at
   both targets, and that the delivered control substitutes co-division
   incidence. This is a disclosure, not a defect — the substitution is
   defensible — but it must be in the paper, not only in my probe.
4. §4.3 and `G-CTRL-EMPTY-FALSIFIABLE`: replace "the identical call"
   with "the same call with the arena **and the target** replaced".

---

### MAJOR-3 — THE CARRIER AXIS IS INERT: `CANDIDATES=60` IS 30 COMPUTATIONS PERFORMED TWICE, AND §5's JUSTIFICATION OF `@BOTH` IS FALSE AS A DESCRIPTION OF THE CODE

The census loop (lines 2341–2356) builds the carrier arena as

```
car = {"name": f"AB4-TRANSPORT-CARRIER@{carrier}", "kind": "carrier",
       "carrier": carrier, "cache": cache, "menu": menu, "cong": cong, …}
```

— **identical payload for both values of `carrier`**; only the label
differs. `arena_sites`/`arena_linkrel` then select `menu` or `cong` by
the **site generator**, never by `arena["carrier"]`. So for
`carrier = "MENU"` the census also runs the CONG-CLASS site generator on
the congruence, and vice versa.

**Measured:** of the 30 (site, link, repair) cells, **30 of 30 are
byte-identical across the two carrier labels** once the two label fields
(`carrier`, `arena`) are removed. Zero differing cells.

Consequences.

1. `CANDIDATES=60` overstates the census by exactly 2×. The `#24`
   "computed, not typed" discipline is satisfied — the number *is*
   computed — but it counts labels, not candidates.
2. §5's justification is false as written:
   > *"The verdict is carrier-stamped `@BOTH` for that reason, and not
   > because the carriers were assumed interchangeable: the link
   > relations were built separately on each carrier's own class graph."*

   The link relations were built separately **per site generator**
   (MENU-CLASS on `menu`, CONG-CLASS on `cong`), not per carrier. The two
   carrier labels indexed the same computation, so "the two carriers
   return identical fate distributions" is an identity, not an agreement.
3. §9's carrier-relativity row draws the wrong kind of blank:
   > *"The two carriers returned identical fates here, so this unit adds
   > no evidence either way… That silence is a result and is recorded as
   > one."*

   It is **not** a result. It is a non-measurement: the carrier
   coordinate was never varied. Registering a non-measurement as a
   "result" is exactly the species the RSQ line has been killing since
   #156.

**What IS genuinely carrier-comparative** — and it is good work — is the
**site-generator** axis: MENU-CLASS and CONG-CLASS extension graphs were
built and measured separately, and they genuinely differ (243 edges /
45 self-loops against 376 edges / 0 self-loops; I reproduced all four
numbers). §5.1's mechanism table does this correctly. The science is
sound; the bookkeeping and the stamp are not.

**REPAIRS (exact).**
1. Verdict: `CANDIDATES=30(EACH-LABELLED-AT-2-CARRIERS)` — or keep 60
   and add `DISTINCT-COMPUTATIONS=30`.
2. §5: replace the false sentence with
   *"The carrier label does not enter any cell: the two quotients enter
   the census as **site generators**, and it is there that they were built
   and measured separately (MENU 243 edges / 45 self-loops; CONG 376
   edges / 0). The 60 rows are 30 computations under two labels, and the
   `@BOTH` stamp records that both quotients were exercised as site
   generators, not that a carrier coordinate was varied."*
3. Head: `@BOTH-QUOTIENTS-AS-SITE-GENERATORS:MENU-113+CONG-185`.
4. §9: change "That silence is a result and is recorded as one" to
   *"The carrier coordinate was not varied, so this unit is silent on
   carrier-relativity by construction. Registered as NOT-MEASURED, not as
   agreement."*

---

## 3. MINOR FINDINGS

**MINOR-1 — the abstract's strict-positivity conjunct is false, and the
gate knows it.** Abstract: *"Across the whole committed crystal family
the axis link counts are homogeneous and strictly positive, and the
diagonal link count is identically zero at 9 of 9 sites in 5 of 5
crystals."* `D60-GRID(3,12)` has **n_{e1} = n_{e2} = 0 at 9/9** (receipt
`crystals[4]`; I reproduced it: 46 events, 1 division, 0 ordered pairs
with co-divisions). `G-CRYSTAL-DIAGONAL-EMPTY` says it correctly —
"strictly positive **on the arbitration crystals**" — and §8.7 explains
why. The abstract dropped the qualifier. *Repair:* insert "on the four
arbitration crystals" into the abstract's first conjunct; keep "5 of 5"
on the diagonal conjunct, which is true.

**MINOR-2 — §8.2 makes a false claim about the receipt.** *"It is an
argument, not an enumeration, and it is marked as such in the receipt's
waiver census."* The receipt has exactly **3** waivers — `G-TWO-WAY`,
`G-DEAD-LIST-CITED`, `G-U4-REGISTERED` — and **none** is the grading
argument. §10's own count (3, "all of class DECLARATION-CARRIED or
REGISTER-ONLY") contradicts §8.2. What the receipt *does* carry is a
per-row `acyclicity_basis` field naming the grading. *Repair:* point
§8.2 at `acyclicity_basis` in the census rows, or add a fourth waiver of
class ARGUMENT-CARRIED. This one matters more than its size because it
is a false statement about the receipt made *inside the deviations
register*.

**MINOR-3 — the receipt carries a wrong quantity that the paper silently
corrected.** `subsets_excluded` uses two different formulas:
`f"all {arity}-choose-{len(X)} restrictions"` when the objects are
materialised (correct — "all 113-choose-9", "all 185-choose-9") and
`f"2^{arity}"` when they are not, giving **`"2^1048576"`** and
**`"2^3969"`**. Those are power-set cardinalities of the site-object
sets, not counts of 9-element restrictions. The paper prints the correct
binomials — C(2²⁰,9) and C(3969,9) — so the prose is right and the
receipt is wrong, which inverts #20. *Repair:* use the `choose` form in
both branches.

**MINOR-4 — two paper numbers with no receipt row and no citation.**
§8.3: *"Deeper carriers ((A,B) d≤5: 265 MENU / 462 CONG classes)"*. Not
in the receipt payload. I verified both against
`v10/note-d74-transport-holonomy-result.md` line 192 (`| (A,B) d≤5 | 265
| 462 | …`), so they are **correct** — but they are uncited in the paper
and unrendered from the receipt. *Repair:* cite D74 `0180e21c7127` inline
or add a `cited_d5` payload row.

**MINOR-5 — `SMUGGLED=0` is unreachable by construction and was never
evaluated, and only two of the three zeros are flagged.** For a census
candidate the classifier is fed `count_fn = lambda i7rec: base_field` — a
**constant** function of its argument — so `classify_smuggling` cannot
return True for any candidate this detector builds. And in fact no
candidate reached step (5) at all. §6 marks `FOUND`/`UNMOTIVATED` as "not
reached"; `SMUGGLED` gets no such mark anywhere. *Repair:* verdict
segment `SMUGGLED=0(NOT-REACHED;NO-CANDIDATE-COUNT-FUNCTION-IS-S-VALUED-BY-CONSTRUCTION)`
and one clause in §4.4.

**MINOR-6 — a modal over-read at §4.2.** *"they **cannot express**
curvature in the off-diagonal sector at all."* The measurement is "do
not", over five committed records, and §4.2 itself supplies the cause:
"Row arbitrations touch a row, column arbitrations touch a column, and
the deliveries stay inside their group." That cause **is the declared
blueprint** — which the scout already priced as a construction choice
(d47 pin §3, "the direction set is a construction choice"). *Repair:*
"do not" for "cannot", plus the clause *"and the cause is the crystals'
declared row/column blueprint, so the zero is a property of a
construction choice and not a law of grammar records."* See §5 below.

**MINOR-7 — blade 2 is stated unqualified in the abstract.** *"Every link
generator with 9 or more objects is acyclic."* True of the three
declared ones. *Repair:* "Every **declared** link generator…".

**MINOR-8 — `EVENT-SUBSET` silently instantiated as
`DIVISION-EVENT-SUBSET`.** The site arity is 2²⁰ because the family has
**20 distinct division events**; it has **124 distinct events of any
kind** (recomputed). The receipt's `site_note` says so ("all subsets of
the 20 distinct division events of the family"); §3's arity list just
says "EVENT-SUBSET 2²⁰". Harmless to every fate (the cardinality grading
is acyclic for any Boolean lattice) but it is a narrowing of the pin's
word. *Repair:* one clause in §3.

**MINOR-9 (bookkeeping, not a defect) — "336 in each direction" is one
set of 336 occurrences of 8 distinct events.** The relation
`rel[(u,v)] = #{division events with u and v both in the register
footprint}` is symmetric by construction, so `A→B` and `B→A` are the
**same** 336. Recomputed: 336 occurrences both ways, the multisets
identical, **8 distinct events** behind them, at 42.0 occurrences each
across the 3969 prefixes. §5.1's table ("A→B (336 division events) and
B→A (336)") reads as 672 events; the verdict's
`336-DIVISION-EVENTS-ON-THE-(A,B)-CHANNEL` reads as 336 events. Neither
is verdict-bearing — blade 1 needs only "a cycle exists at 2 objects",
which 8 distinct events supply. *Repair:* "336 occurrences of 8 distinct
pair arbitrations, the same set in both directions".

---

## 4. K3 — WHAT THE CRYSTAL FOUND CONTROL LICENSES, AND THE SAME-STANDARD AUDIT

**What it licenses.** That the detector's FOUND branch is not dead code:
on a grammar record whose co-division incidence happens to be the target
graph, the machinery returns FOUND with every fiber 1. That is real and
it is worth having. It licenses **"a forced map exists on the right
arena"** and nothing about the transport carrier.

**What it does not license, and the audit.** Not the same standard —
three ways, in increasing severity:

1. *Different target* (MAJOR-2): 2 links against 3.
2. *Different choice arena*: 288 configurations against 15 552; the
   direction-label fiber is measured over 2 permutations where the census
   would demand 6.
3. *Different generator from the one the pin named*: the pin's cover
   structure returns STRUCT-DEAD; only co-division incidence fires.

The gates and the code path are indeed identical — the control runs
through `detect` like everything else, which is a genuine strength and
answers the crude form of the smuggled-blueprint worry. The smuggling, to
the extent there is any, is in the **target**, not the blueprint.

**What the withheld-arbitration flip teaches.** It is the sharpest thing
in the unit. Withdraw one row-group arbitration and `I-SITE-ASSIGNMENT`
goes 1 → 6 and `I-DIRECTION-LABEL` 1 → 2, while the isomorphism count
stays at **72**. The graph did not change; the *count field carried on
it* did. So what forces the crystal map is not the incidence at all — it
is **homogeneity of the counts across the automorphism orbit**. §4.1 says
this ("The mechanism is homogeneity") and it is right.

That has a consequence the unit does not draw: **forcing is a property of
the count field, not of the graph** — which means the whole scissors
argument, which is purely graph-theoretic, is arguing at the wrong level
for FOUND and only at the right level for the embedding gate. Under the
quotient reading (MAJOR-1), the thing that would decide a candidate is
exactly what the falsifier isolates: whether the induced counts are
homogeneous enough to collapse the orbit. That is the successor
experiment, and the crystal falsifier is its prototype.

---

## 5. K4 — THE EMPTY DIAGONAL

### 5.1 The measurement

Reproduced from the receipt and independently rebuilt:

| crystal | events | divisions | n_{e1} | n_{e2} | n_{e1+e2} | ordered pairs with co-divisions |
|---|---|---|---|---|---|---|
| DOUBLE-GRID(3,2) | 72 | 18 | 2 at 9/9 | 2 at 9/9 | **0 at 9/9** | 36 |
| DOUBLE-GRID(3,3) | 96 | 24 | 3 | 3 | **0** | 36 |
| CONFLICT-GRID(3,2) | 30 | 6 | 1 | 1 | **0** | 36 |
| CONFLICT-GRID(3,4) | 66 | 12 | 2 | 2 | **0** | 36 |
| D60-GRID(3,12) | 46 | 1 | **0** | **0** | **0** | **0** |

### 5.2 THE LICENSED READING

> **Under this unit's declared reading — site ← the record's actor pool,
> link ← co-division incidence on the ordered actor pair, count ←
> division events in the first-to-last-arbitration window — the five
> committed crystal records never write the (1,1) link. Four of them
> write both axis links homogeneously and positively; the fifth writes
> nothing. So the committed crystal family fixes q₁₁ and q₂₂ and never
> fixes q₁₂.**

Scope stamps that must travel with it: **5 records**, **one** link-relation
definition, **one** window, **one** site generator, **d = 2**. And the
mechanism, which the paper supplies and should carry into the claim: the
crystals' arbitrations are **row-group and column-group** arbitrations by
their blueprint, and no event's register footprint meets a diagonal pair.

### 5.3 THE OVER-READINGS, KILLED

- **"Grammar records cannot carry off-diagonal curvature."** NO. Five
  authored records under one incidence definition. The measured *cause*
  is a declared row/column blueprint (d47 pin §3), which is a
  construction choice, not a law. A crystal built with diagonal
  arbitration groups would write the link; nobody has built one, which is
  a fact about the corpus's construction history.
- **"The declared lattice is wrong / the (1,1) link is unphysical."** NO.
  Nothing here bears on I7's declaration. I7's own records carry non-zero
  q₁₂ (G-CURVED, G-CURVOFF) and were read as data.
- **"q₁₂ is unfixable from grammar."** NO — only "from the committed
  crystal family under this reading."
- **"It says something about ALL grammar records."** NO. It says nothing
  about the transport carrier at all: at the carrier the diagonal
  question never arises, because every candidate dies before a count
  field exists.
- **"n_{e1+e2} ≡ 0 shows the crystals are flat."** NO — and the true
  statement is **stronger than the paper's and free**. Push the measured
  counts through HA §3.2's own readout,
  q₁₂ = (n_{e1+e2} − n_{e1} − n_{e2})/2. With homogeneous axis counts
  n₁ = n₂ = k and diagonal 0 this gives q₁₂ = −k, hence
  **det = q₁₁q₂₂ − q₁₂² = k² − k² = 0 at every site of every crystal**:

  | crystal | (n₁, n₂, n_diag) | (q₁₁, q₂₂, q₁₂) | det | admissible? |
  |---|---|---|---|---|
  | DOUBLE-GRID(3,2) | (2, 2, 0) | (2, 2, −2) | **0** | no |
  | DOUBLE-GRID(3,3) | (3, 3, 0) | (3, 3, −3) | **0** | no |
  | CONFLICT-GRID(3,2) | (1, 1, 0) | (1, 1, −1) | **0** | no |
  | CONFLICT-GRID(3,4) | (2, 2, 0) | (2, 2, −2) | **0** | no |
  | D60-GRID(3,12) | (0, 0, 0) | (0, 0, 0) | **0** | no |

  So **no committed crystal induces an admissible I7 record** by the
  exact Sylvester criterion this unit itself applies to I7's family — and
  the failure is *exactly degenerate*, not merely negative. That is a
  third, independent route to §4.2's STRUCT-DEAD, arrived at from the
  metric side rather than the graph side, and it is one line of code
  (`admissible_record`, already in the file at line 1047, is called only
  on I7's own family at line 1060 and never on the crystal field).
  *Recommended addition to §4.2* — it costs nothing and it is the
  sharpest form of the empty-diagonal result.

### 5.4 THE R4 RESONANCE, RULED AT CITABLE SCOPE

R4's adjudication (§1, `note-r4-adjudication.md`) relocated the headline
onto the declared diagonal: `G-LINKS-IN-BALL` is decided by the anchored
link **(1,1)** having sum-norm 2, so *"the connective is FORCED by I7's
declared link set"* and *"the unique scale is a theorem about I7's
declared link set, not a law of the substrate."* That adjudication
itself flagged the resonance: *"this is now the SECOND result resting on
the declared lattice — the weld-2 census (paper-13) carries exactly that
weight."*

**The one sentence licensed by both artifacts together:**

> **The declared link that forces R4's connective — and with it R4's
> unique locality scale — is the one link that no committed grammar
> record writes: measured at 0 of 9 sites in 5 of 5 crystals.**

**Licensed additions:** that both results are *declaration-resting* in
the same coordinate, so a future change to I7's declared link set moves
**both**; and that the corpus therefore has one declaration doing double
duty, which is a concentration worth registering (compare BRG's sector
concentration open).

**NOT licensed:** that R4's theorem is threatened, weakened, or
conditional on the crystals; that the (1,1) link should be dropped; that
R4's scale is "unphysical"; or any inference from crystals (2-link,
blueprint-declared, d=2, 9 actors) to I7's record family (declared data,
3-link). The two arenas share a coordinate label and no object — which is
the scout's own §(e) finding, now with a second instance.

---

## 6. THE ≥9-ACTOR SUCCESSOR — NOT WELL-POSED AS NAMED

§9: *"does a transport carrier over ≥ 9 actors — which the crystals show
the layer supports — give the cyclic generator enough objects? **A
positive answer to (ii) is the first place a motivated weld could
exist**, and it is posable now."*

Arity is **necessary, not sufficient**, and this unit's own controls say
so. At 9 actors the ACTOR/ACTOR-PAIR cell clears the arity gate — and
then meets the structure gate, which asks for an **exact** incidence
match with a Cayley graph of (Z₃)²: rook's 3×3 (4-regular, |Aut| 72) at
the 2-link target, K₃,₃,₃ (6-regular, |Aut| 1296) at I7's. A richer
transport family over 9 actors drives co-division incidence toward the
complete graph K₉, i.e. **away** from either target, not toward it. And
the crystals show what actually produces the match: not the actor count
but the **row/column blueprint** — a declared construction choice, which
is precisely why the crystals are disqualified as a seed.

So (ii) as named repairs the blade the crystals already show is
repairable, and leaves untouched the obstruction that actually bites.
*Repair:* restate as
*"(ii) does any generated grammar record — one not shaped by a declared
actor blueprint — have co-division incidence isomorphic to a Cayley graph
of (Z₃)² on the declared link set, with a homogeneous count field? Actor
count ≥ 9 is necessary for this and is not sufficient; the crystals show
the sufficient condition is currently supplied by a blueprint."*
That restatement is **U4**, which §9 already registers — the two bullets
should be merged.

Experiment (i) — cycles at depth ≥ 5 — is well posed and cheap, and my
MAJOR-1 probe sharpens it: at MENU the obstruction is already **not**
acyclicity but the 45 self-loops, so (i) should measure self-loops at
d ≥ 5 as well as cycles.

---

## 7. THE LICENSED CLAIM

The sharpest sentence the artifacts support:

> **At the (A,B) depth-≤4 transport carrier, no candidate in the pin's
> declared generator vocabulary carries I7's declared nine-site
> three-link lattice into the grammar as a sub-structure: 36 of 60 cells
> fail a type test that holds in either direction of the map, and the
> remaining 24 fail on arity or on acyclicity under the embedding reading
> the census implements. The corpus's only lattice-carrying grammar
> records — five committed crystals — carry a two-link lattice whose
> diagonal count is identically zero, so the FOUND branch has been
> demonstrated at a two-link target and never at I7's.**

And, as a second sentence with independent standing:

> **The one motivated ingredient survives every test the unit put to it:
> the count semantics is verbatim-anchored, the division predicate is
> source-forced at 1536 of 1536 tagged instances, and additivity
> reproduces at 972 of 972 with 0 violations. What is missing is not the
> *what* but the *where* — exactly the scout's verdict, now with the
> obstruction located at the type gate rather than at the choice
> standard.**

What may **not** be claimed at citable scope: that weld 2 is impossible;
that the lattice cannot be derived from the grammar; that the census
answers "can the lattice be derived from the grammar" in the negative.
It answers a narrower question — *does the declared vocabulary contain a
sub-structure embedding at this scope* — and answers it exhaustively and
exactly. The broader question is where the pin pointed and where MAJOR-1
leaves it: **open, at 20 of 60 cells, with the entry point measured.**

---

## 8. THE SUCCESSOR REGISTER

### (a) To the Γ-iteration pin

| row | content | grade |
|---|---|---|
| W2→Γ-1 | **CONG-185 re-derived independently, six of six.** 185 classes in 5 rounds (inside D74's 4–6 window); comparator = coarsest bisimulation by explicit pair-splitting, no signature hashing. P1 descent (0 non-constant classes at every horizon, against MENU's 4 at G(·,2)); P2 0/0 multi-valued (MENU 0/4); P3 44 of 88 defective close, 44 non-unit self-loops {1/2:26, 2:10, 3/2:6, 2/3:2}, obstruction 44, 1362 of 1546 (MENU 44 / 1402); P4 q-holonomy ⟨2,3⟩ rank 2; P5 k-holonomy collapses onto q, ⟨2,3⟩ rank 2 (MENU ⟨2,3,5,13⟩ rank 3); P6 CK 10/10 (MENU 6/10). The derivation is genuinely independent of the frozen review's construction. | **CITABLE at AB4** |
| W2→Γ-2 | **The unweighted partition at AB4 also returns 113.** The weights add no refinement at this scope, so any Γ claim that loads on "weighted" at AB4 is untested. Volunteered by the unit; I confirm it. | **CITABLE, and a caution** |
| W2→Γ-3 | **Carrier-relativity: NOT-MEASURED, not agreement.** The carrier coordinate was inert (MAJOR-3); 30 of 30 cells identical across labels. Do not read weld 2 as evidence that the carriers agree. | **CORRECTION to §9** |
| W2→Γ-4 | **Structure of the two class graphs**, freshly measured: MENU 113 nodes / 243 edges / 45 self-loops; CONG 185 nodes / 376 edges / 0 self-loops; both acyclic on distinct vertices (three independent methods: Kahn sort, ≤6-cycle enumeration, DFS colouring). New here: **the CONG class graph admits a Z₃ level grading; the MENU one admits none, exactly, because of its self-loops.** | **NEW DATUM** |

### (b) To any Route-B declaration the user later orders

| row | content |
|---|---|
| W2→B-1 | **The scout's own named Route-B map does not type-check at this carrier.** "site ← actor, link ← delivery channel" is **ARITY-DEAD**: 2 actor objects against 9 sites, and a declared restriction can only shrink (ARITY-DEAD-BELOW). A Route-B declaration cannot use the scout's example as written. |
| W2→B-2 | **What a declaration must now invent by hand**, itemised by this census: (i) **a nine-element site set** — the only actor-typed site generator has 2 objects, and every ≥9-object site generator is type-incompatible with the delivery channel (no pinned map class→actor, subset→actor, address→actor); (ii) **a direction labelling over 3 links** (6 permutations) and an orientation; (iii) **a link relation realising all three declared displacements** — the best of 40 randomised quotient maps on CONG-185 covers 18 of 27 cells; (iv) **a strictly positive diagonal count**, which no committed crystal supplies. |
| W2→B-3 | **Price the declaration at its true arity.** It is not one free item. It is at minimum the pin's three inventory items — `I-SITE-ASSIGNMENT`, `I-DIRECTION-LABEL`, `I-ORIENT` — each at fiber > 1, plus the window. Recommended stamp: `DECLARATION-RELATIVE(SITE-SET+DIRECTION-LABEL+ORIENT+WINDOW)`, not the flat `DECLARATION-RELATIVE` the scout priced. |
| W2→B-4 | **Route B is not foreclosed and is not cheapened.** §9's sentence "This census does not foreclose it; it establishes what a *derivation* would have to supply" is correct and should be kept verbatim. |

### (c) To a ≥9-actor carrier unit

| row | content |
|---|---|
| W2→9A-1 | **Re-pose the question** (see §6 above): incidence shape, not actor count. Actor count ≥ 9 is necessary and not sufficient; a richer family moves co-division incidence toward K₉ and away from any Cayley graph of (Z₃)². |
| W2→9A-2 | **Run both targets, and demonstrate the FOUND branch at the I7 target before taking any verdict.** Weld 2's two-way gate is discharged only at a 2-link target (MAJOR-2); a successor that inherits that gap inherits an undemonstrated predicate. |
| W2→9A-3 | **Only one cell is repaired by the widening.** ACTOR/ACTOR-PAIR clears arity at 9 actors; MENU-CLASS, CONG-CLASS, EVENT-SUBSET and ULAM-PREFIX stay type-dead against the delivery channel and arity-dead against the extension edge. Expected yield: 4 of 30 cells move, 26 do not. |
| W2→9A-4 | **Carry the choice-arena numbers**: at the I7 target the inventory must range over 1296 × 6 × 2 = 15 552 configurations, not the control's 288. |

### (d) To a U4 unit

| row | content |
|---|---|
| W2→U4-1 | U4 ("the division events of a crystal form a crystal", v11 paper 0 §7 `37a428321f46`) is **registered and never run**, correctly waived REGISTER-ONLY here. It is the only successor that makes the FOUND-side control a **generated** carrier rather than a declared blueprint, and it therefore also repairs the blueprint half of MAJOR-2. |
| W2→U4-2 | **Data handed over:** division-event yields 18/72, 24/96, 6/30, 12/66, 1/46. The renewal sublattice is non-degenerate for the four arbitration crystals and degenerate for the delivery grid — §8.7's distinction ("a delivery crystal, not a division crystal") is exactly U4's question and should open the U4 pin. |
| W2→U4-3 | **U4 must be run against the 3-link target** to close what weld 2 left open, and to do so it must produce a strictly positive diagonal count. If it cannot, the empty diagonal is promoted from a property of five committed records to a property of the crystal *construction*, which is a much stronger and citable result. |
| W2→U4-4 | **Merge §9's bullets.** The "≥9 actors" experiment and U4 are the same experiment posed twice; U4 is the well-posed form. |

### (e) To the weld-2 adjudication itself

| row | content |
|---|---|
| W2→ADJ-1 | Rule on the **reading** (MAJOR-1) before ruling on the head. If the panel adopts the embedding reading as *the* reading, say so in the head and register the quotient reading as an open. If it adopts the pin's wording, 20 of 60 cells revert to undecided and the head's obstruction segment must change. |
| W2→ADJ-2 | Rule whether a control at a **different target** discharges HA §14 requirement 3 for a predicate applied at another (MAJOR-2). This is a precedent question that outlives weld 2. |
| W2→ADJ-3 | Rule the **carrier-stamp convention** (MAJOR-3): may `@BOTH` be stamped when the carrier coordinate is inert? Recommend: no — `@BOTH-QUOTIENTS-AS-SITE-GENERATORS`. |
| W2→ADJ-4 | Rule whether an **offered-but-never-executed repair** may be counted as a generator axis. `DECLARED-RESTRICTION` doubles the candidate count but the detector never selects a 9-subset; if a cell is ever both cyclic and over-large it returns `ARITY-REPAIR-UNDECIDED`, and `G-VERDICT` is conditioned on that count being zero. The axis is decided entirely by the scissors. Recommend: keep the axis (it is conservative) but stamp it `OFFERED-NOT-EXECUTED` and qualify `G-CENSUS-COMPLETE` as contingent on the scissors closing. |

---

## 9. THE DEVIATIONS REGISTER, AUDITED

| # | disclosed | priced honestly? |
|---|---|---|
| 1 | control fires at the crystal's lattice, not I7's | **UNDER-priced** — MAJOR-2: the FOUND branch is *never* demonstrated at I7, the choice arena is 1/54 the size, and the pin's *named* control generator (cover structure) returns STRUCT-DEAD unreported |
| 2 | two generators decided by a grading theorem | honest as an argument; **but** "marked as such in the receipt's waiver census" is **false** (MINOR-2), and the receipt field is wrong (MINOR-3) |
| 3 | scope (A,B) d≤4, I7 at d=2 L=3 | honest; the d≤5 numbers are uncited and un-receipted (MINOR-4) |
| 4 | window and division predicate declared | **honest, and the defence checks out.** I verified that no fate in the census consults the count generator — TYPE/ARITY/ARITY-BELOW/STRUCT all resolve before step (4) — so "a reader who classes either as free reads the same census with the same fates" is exactly true |
| 5 | scout amended after the pin froze; reads via `git show 95c3b77:` | **honest and well executed.** G-PROVENANCE resolves 24 of 24, reroutes 2 (scout `425303a8ce1e`, gamma-main `05f5dc7c7273`) at a pinned commit; V09 reads through the same route |
| 6 | unweighted partition also returns 113 | **honest and volunteered.** Good practice |
| 7 | D60-GRID(3,12) carries one division event | honest — but this is the crystal that falsifies the abstract's own conjunct (MINOR-1), and the deviation names the cause without noticing |
| — | **MISSING: the reading substitution** | MAJOR-1 |
| — | **MISSING: the carrier axis's inertness** | MAJOR-3 |
| — | **MISSING: `SMUGGLED=0` unreachable by construction** | MINOR-5 |
| — | **MISSING: the pin's cover-structure control fails** | part of MAJOR-2 |
| — | **MISSING: `DECLARED-RESTRICTION` is offered but never executed**, and `G-CENSUS-COMPLETE`'s completeness is contingent on the scissors closing | MAJOR-1 (mutant evidence) |

Seven disclosures, four omissions. The register is a real register — it
volunteers things (6 especially) that a defensive unit would bury — but
it is incomplete in exactly the direction that flatters the head.

---

## 10. PROSE ↔ RECEIPT ↔ OUTPUT SWEEP

Every numeric token in the paper checked against the receipt and against
my own rebuilds. **No computed number in the paper is wrong.** Findings
are confined to the four rows below.

| token | paper | receipt | verdict |
|---|---|---|---|
| 3969 / 113 / 185 / 5 rounds | ✓ | ✓ | reproduced independently |
| 1546 / 88 / {1/2:70, 2:10, 3/2:6, 2/3:2} (sums 88) | ✓ | ✓ | ✓ |
| 1402 / 44 (MENU), 1362 / 44 / 44 / {1/2:26, 2:10, 3/2:6, 2/3:2} (sums 44) | ✓ | ✓ | ✓ |
| ⟨2,3⟩ rank 2 ×2; MENU ⟨2,3,5,13⟩ rank 3; CK 10/10 vs 6/10 | ✓ | ✓ | ✓ |
| 9 sites / 3 links / 11 records / 9 admissible / 6 splittable | ✓ | ✓ | ✓ |
| 972 / 0 / 36 refinements | ✓ | ✓ | ✓ |
| 1536 / 1536 / 20 / 8 | ✓ | ✓ | ✓ (occurrence counts — see MINOR-9) |
| 2 / 113 / 185 / 1 048 576 / 3969; depths 1, 8, 60, 452, 3448 (sum 3969) | ✓ | ✓ | ✓ |
| 60 / 36 / 12 / 2 / 10; 18/6/1/5 per carrier | ✓ | ✓ | ✓ (but see MAJOR-3 on what 60 counts) |
| 45 / 0 self-loops; 0 cycles at lengths 2–6 | ✓ | ✓ | ✓ (third method agrees) |
| 72 isos, fibers 1/1/1; falsifier 6 and 2 | ✓ | ✓ | ✓ (72 = \|Aut\| of the 2-link target) |
| 30 events / 4 divisions / 0 on the channel (walk) | ✓ | ✓ | ✓ |
| 5 crystals: 72/18, 96/24, 30/6, 66/12, 46/1 | ✓ | ✓ | ✓ |
| 32 gates / 0 failures / 7+11 anchors / 3 waivers / 13 mutants | ✓ | ✓ | ✓ |
| §10's selftest claim (18 corrupted individually, all 18 would fail, 0 vacuous, exit path returns 1, writes nothing) | ✓ | — | **verified by execution, exactly as written** |
| **"strictly positive" across the whole family** | ✗ | gate says "on the arbitration crystals" | **MINOR-1** |
| **"marked in the receipt's waiver census"** | ✗ | 3 waivers, none is the grading | **MINOR-2** |
| **C(2²⁰,9), C(3969,9)** | ✓ (correct) | `"2^1048576"`, `"2^3969"` | **MINOR-3** (receipt wrong) |
| **265 / 462 at d≤5** | ✓ (correct vs D74) | absent | **MINOR-4** |
| **"built separately on each carrier's own class graph"** | ✗ | code contradicts | **MAJOR-3** |
| **"the identical call"** (§4.3) | ✗ | two coordinates change | **MAJOR-2(c)** |

---

## 11. RECOMPUTATION LEDGER (110)

- **Reproduction (2):** plain run in an off-tree scratch mirror →
  `w2_census_output.txt` and `w2_census_receipt.json` **byte-identical**
  to the committed artifacts (`5e35e7a0115f`, `bacdb7a5e985`).
- **Carrier arena (7):** 3969 histories; 113 menu classes; 185
  congruence classes; 5 refinement rounds; 20 distinct division-event
  labels; 1536 division-event occurrences; 124 distinct events of any
  kind.
- **Class graphs (8):** MENU 113 nodes / 243 edges / 45 self-loops /
  acyclic by DFS colouring; CONG 185 / 376 / 0 / acyclic by DFS
  colouring.
- **Blade 1 (5):** 336 occurrences A→B; 336 B→A; the two multisets
  identical; 8 distinct events behind them; 20 distinct arbitrations of
  which 8 are pair arbitrations.
- **Target geometry (5):** all 27 (site, link) pairs close a 3-cycle on 3
  distinct sites; \|Aut\| = 72 at 2 links; \|Aut\| = 1296 at 3 links;
  degrees 4 and 6; 2 and 6 label permutations.
- **Reading probe (6):** MENU Z₃-grading fails; MENU (Z₃)²
  arc-consistency wipes out; CONG Z₃-grading exists; CONG witness φ
  exists; its fibre profile; 18 of 27 cells positive over 40 randomised
  solutions.
- **Ulam (6):** total 3969; depths 1, 8, 60, 452, 3448; sum check.
- **Crystals (36):** 5 × (events, divisions, ordered co-division pairs)
  rebuilt; 5 × 3 link count values read from the receipt; 5 × the induced
  (q₁₁, q₂₂, q₁₂) and its determinant through HA §3.2's readout, all
  **exactly 0**; `admissible_record` confirmed called only on I7's own
  family.
- **Census rows (6):** 60 rows; fates 36/12/2/10; 30 cells per carrier;
  **30 of 30 identical across carrier labels**.
- **Controls re-run (6):** ACTOR-PAIR@L2 FOUND (72, 1/1/1);
  ACTOR-PAIR@I7 STRUCT-DEAD (0); COVER-PAIR@L2 STRUCT-DEAD;
  COVER-PAIR@I7 STRUCT-DEAD; EXTENSION-EDGE/ACTOR TYPE-DEAD ×2.
- **Receipt bookkeeping (6):** 32 gates, 0 failures; 7 numeric anchors;
  11 verbatim anchors; 18 total; 3 waivers; 13 mutants.
- **CLI and selftest (5):** unknown flag → exit 2; unknown mutant →
  exit 2; `--list-mutants` → 13 rows; `--selftest` → 18 anchors (7
  numeric, 11 verbatim), **18 of 18 would fail the run, vacuous = []**,
  the real exit path with one injected failure returns 1, **wrote
  nothing** — §10's prose confirmed exactly.
- **MUT-CYCLE-PLANT (4):** `G-SCISSORS` and `G-VERDICT` both fail;
  artifacts not written; fates redistribute 10 STRUCT-DEAD → 6
  STRUCT-DEAD + **4 ARITY-REPAIR-UNDECIDED** (the MAJOR-1 confirmation).
- **Cross-source (5):** D74 line 192 carries 265 / 462; scout worktree
  `425303a8ce1e` against pinned `e1f771a9d0ed`; 24 pinned sources, 2
  rerouted; verbatim anchor routes.
- **Structural reads (3):** no fate consults the count generator; the
  smuggling classifier is fed a constant for every candidate; fibers are
  counted as distinct count fields, not as choices.

**Cross-lens note (instrument's territory, recorded because I hit it):**
the plain run outside a repo layout dies with an unhandled
`FileNotFoundError` traceback from `sha12`, because `REPO` is derived
from `__file__`. The protocol's engraving asks for "off-tree/git-less
byte-reproduction"; byte-reproduction succeeds in a **mirrored** tree but
there is no clean abort and no `--repo` override. Not my finding to
grade.

---

## 12. WHAT SURVIVES

Unmoved by everything I ran:

- **The verdict.** EMPTY at the declared family, at both quotients, at
  this scope. My constructed counter-candidate does not reach FOUND; it
  reaches `COUNT-DEAD` on the evidence available.
- **The type gate.** 36 of 60 cells die at a question that has the same
  answer in either direction of the map. This is the reading-robust core
  and it is the strongest thing in the unit.
- **The ingredient.** Count semantics verbatim-anchored; division
  predicate source-forced, 1536 of 1536 tagged, with the S4 sensitivity
  disclosed and not adopted; additivity 972 of 972, 0 violations, with an
  independent arithmetic comparator.
- **CONG-185 re-derived six of six.** No mismatch, independently
  comparated, and now independently confirmed here.
- **The empty diagonal.** A real, unanticipated measurement, correctly
  reported at 9/9 and 5/5, correctly refused as a weld, and correctly
  handed to the successor register — needing only the modal repair of
  MINOR-6 and the scope stamps of §5.2.
- **The disclosure culture.** Deviation 6 (unweighted 113) and deviation
  7 (D60-GRID) are volunteered against interest. Deviation 4's defence is
  exactly true. The candidate-reading discipline is carried into the
  gate statements.

**AWF.** Three MAJOR repairs, two of which touch the head string; nine
MINOR repairs, all one-clause. Zero false computed numbers. The unit's
own artifacts contain everything needed to make every repair.
