# v15 — THE HOMONYM AUDIT (E-34.3 registry note)

**Ordered:** v15 LEDGER #55 (v15/LOG.md:1888–1988), after the user's binding
diagnosis that "division event" named two incompatible objects for an era and
that the conflation surfaced as ECC's Mp=3q infeasibility.  **Status:** a
READ-ONLY sweep and a REGISTRATION.  It edits nothing, retracts nothing, and
moves no number.  This file is the registry RUNBOOK E-34.3 names ("the
registry note v15/note-homonym-audit.md carries the terminology map",
RUNBOOK.md:1979–1980): sealed papers are not rewritten; the map below is how
their words are to be read.

**Scope:** the live corpus — v15/*.md (papers 43–47, 50, pins, PLAN,
QUESTIONS), v14/paper-01…42 and the v14 pins, RUNBOOK.md; older eras only
where a live paper inherits the term (the one such inheritance found is v11's
division-event POSIT, carried by v14 papers 09/13/14).

**Method and conservatism rule:** for each candidate term, formal
definitions and formal uses were collected with file:line anchors, then
ruled.  Only FORMAL objects count as senses — objects that are defined,
measured, gated, or equated.  A metaphor, an informal gloss, or ordinary
mathematical English ("saturates the bound", a table's "cells") is not a
second sense and is not counted.  Verdict key:

- **SINGLE-SENSE** — one formal object everywhere in the live corpus.
- **DISCLOSED-POLYSEMY** — multiple formal senses, but every use is
  disambiguated at point of use (a qualifier, a unit's own binding table, or
  an explicit measured fork), with the disclosure cited.
- **TYPE-ERROR-CANDIDATE** — multiple formal objects under one
  undisambiguated name, with at least one located place where an argument,
  equation, or transported law could conflate them.

Line numbers cite the bytes as of this audit (post-#55 tree, wave-1 repairs
folded).

---

## 1. The terminology map: "division event" / CELL-HIT (the E-34.3 registry)

### 1.1 The three formal senses

| sense | the object | defining bytes |
|---|---|---|
| **R — renewal marker** | v11's POSIT: "division events are the renewal events" — a renewal/indivisibility marker of the process timeline; operationally a DECLARED TIME at which a leg is conditioned ("division-event times") | inherited: v14/paper-09-renewal-transport.md:60 ("S3 the type declaration \| division event ≡ renewal"), :400 (the POSIT verbatim); v14/paper-13-weld2-carrier-census.md:102–104 |
| **G — three-actor grammar event** | an arbitration-tagged grammar event whose register footprint is its conflict group: "A division event is a set of three actors. The record of an event is the set of cells both of whose actors take part in it — for most events three cells" (v14/paper-41-rec.md:96–98); "a division event's footprint **is** its conflict group" (v14/paper-19-r3-weld.md:289–290); "the three-actor group as the unit of a division event \| forced" (v14/paper-40-sec2.md:722); deposits EXACTLY THREE cell incidences (v14/paper-40-sec2.md:326–329; v14/paper-30-lor.md:330–331) | predicate = the arbitration tag, SOURCE-FORCED (v14/paper-13-weld2-carrier-census.md:261–263); register set = the proposers = the conflict group (v14/paper-33-aid.md:159–164) |
| **C — CELL-HIT (walk emission)** | the coupled walk's primitive: one selected pair-cell per step — "A division event on cell (x, l) increments n_l(x) by one" (v14/paper-20-coupling.md:277–278); "the walk emits exactly one division event per step" (v14/paper-20-coupling.md:482; v14/paper-24-sig.md:293, :394–395); the state is NOT collapsed onto the emitted cell (v14/paper-20-coupling.md:633–636) | renamed **CELL-HIT** forward-binding at #55 (RUNBOOK.md:1976–1980; v15/note-scout-pin-addendum.md:13–14, 21–24) |

R vs G was identified by a disclosed [POSIT] and was type-audited in place:
paper-09's type census names the C1 conflation ("equates a division-event
count with a grammar-event count") and its type-honest repair C2
(v14/paper-09-renewal-transport.md:402–406).  G vs C was the UNDISCLOSED
identification — the type error #55 engraves.

### 1.2 The shared register — why the homonym stayed hidden

Both G and C write the SAME register, the count field n_ℓ(x), whose founding
definition is event-structure-neutral: "n_ℓ(x) is the number of division
events in the record interval between x and x+ℓ" (v14/paper-04-refinement-grammar.md:24,
:46–47; v14/paper-05-accumulation.md:53–55; v14/paper-07-coarse-graining.md:71).
The grammar writes it three cells per event (v14/paper-40-sec2.md:328–329);
the walk writes it one cell per step (v14/paper-20-coupling.md:277).  One
register, two writers of different arity.  SIG measured the symptom and
classed it channel asymmetry: "A round's deposit on a cell comes with 8
deposits it does not choose; an emission's comes with 0"
(v14/paper-24-sig.md:393–397).  ECC attempted the repair and Mp=3q is where
the conflation surfaced: P(c among the three written cells) = 3q(c) is an
inclusion probability, ≤ 1, so q ≤ 1/3, and the committed cell's 4/9 would
need 133% (v15/LOG.md:1908–1918).  The confusion, engraved: MUTUALLY
EXCLUSIVE ALTERNATIVES (which cell triggered) vs SIMULTANEOUS CONSEQUENCES
(which three relations were written) — not the same observable (E-34.4/5,
RUNBOOK.md:1981–1989; W4-TYPE-IDENTITY, v15/PLAN.md:10).

### 1.3 The per-paper sense map

| file | sense | anchor |
|---|---|---|
| v14/paper-04-refinement-grammar.md | R (count-abstract interval semantics) | :24, :46–47 |
| v14/paper-05-accumulation.md | R (count-abstract; front = events committed at a site) | :53–55, :91 |
| v14/paper-06-stochastic-split.md | R (count-abstract) | :15, :48 |
| v14/paper-07-coarse-graining.md | R (count-abstract) | :71 |
| v14/paper-09-renewal-transport.md | R, with the R↔G identification type-audited (C1/C2) | :60, :400–406 |
| v14/paper-10-defect-on-the-stage.md | R (declared division-event TIMES: t=0, t=2) | :342–344 |
| v14/paper-15-momentum.md | R (indivisibility declared by the division-event times) | :576, :708 |
| v14/paper-18-gauge-rung.md | R (division-event times, a declared free axis) | :211, :450, :457–459 |
| v14/paper-22-multi.md | R (inherited-as-declared times) | :249, :616, :653 |
| v14/paper-13-weld2-carrier-census.md | G (predicate = arbitration tag, SOURCE-FORCED) | :258–263 |
| v14/paper-14-u4-renewal-crystals.md | G (with the D1 initiator-vs-footprint site fork MEASURED) | :128–133, :453 |
| v14/paper-17-schedule-census.md | G (footprint reading a census artifact; initiator reading) | :231–246, :315, :684 |
| v14/paper-19-r3-weld.md | G (footprint = conflict group; 9 events → 27 incidences; arbitration re-seats the event within its own group) | :148–151, :175, :259–260, :289–290 |
| v14/paper-21-r4dec.md | G (one arbitration per conflict group per round) | :213, :243 |
| v14/paper-29-perr.md | G | :709 |
| v14/paper-30-lor.md | G (deposits exactly 3 cell incidences) | :330–331, :368 |
| v14/paper-31-occ.md | G | :248, :614 |
| v14/paper-32-sec.md | G, with a COMPRESSED sentence (see §1.4) | :122–123, :624–641 |
| v14/paper-33-aid.md | G (history = sequence of division events; footprint = the group) | :43, :159–164 |
| v14/paper-35-fac.md | G | :103, :134 |
| v14/paper-39-ndep.md | G ("every division event has exactly q members") | :240 |
| v14/paper-40-sec2.md | G (three actors, three incidences; forced unit row) | :131, :326–329, :722 |
| v14/paper-41-rec.md | G (the crisp definition) | :96–98 |
| v14/paper-23-measure.md | G (quotes paper-13's motivated-map wording) | :270 |
| v14/paper-20-coupling.md | **C** (the CELL-HIT definition site) | :41, :277–278, :482, :633–636 |
| v14/paper-24-sig.md | **C** (one emission per step; the 8-vs-0 symptom) | :293, :311, :393–397 |
| v14/paper-25-gdl.md | **C** (re-implements the update semantics) | :99, :220 |
| v15/paper-43-contract.md | **C** in the influence table ("the menu weights the next division event") — sealed pre-rename; read as CELL-HIT | :420 |
| v15/paper-44-arity.md | G, arity-parametrized (a = actors in one division event; a≠3 rows are the EXTENSION FAMILY, declared) | :57, :74, :123–125 |
| v15/paper-50-arity16.md | G, arity-parametrized (same dial at n=16) | :144–147 |
| v15/paper-45-autoglue.md | G (register idiom: how many division events a cell/seam carries) | :737, :872 |
| v15/paper-46-ecc.md | **BOTH, disclosed as such**: the committed arm binds G (":210 a division event is a group of three actors"; table row DIVISION-EVENT :133; the a-dial row :187; the a=2 BRANCH is pair-events, :208) while :447–449 quotes DISC's C-sense emission verbatim — the collision the LP then measured | :133, :187, :208–210, :447–449 |
| v15/paper-47-disc.md | **C** (emission rule: one division event per step, on a cell) — sealed pre-rename; read as CELL-HIT | :260, :457, :486 |
| v14/note-coupling-pin.md | C's transport charter: the law confirmed on the (A,B) 2-actor carrier, BLOCKED-AT-THE-LAW-TRANSPORT first-class | :63–70 |
| v15/note-scout-pin.md | post-diagnosis: record-writing at selected division events (S1); kernel K(e\|c,G,R) (S2) | :48–49, :55 |
| v15/note-scout-pin-addendum.md | the rename mandatory; primitive selection = the deliverable question | :13–14, :21–24 |

Papers 01, 02, 03, 27, 28, 34, 37, 38, 42 use the term zero times.

### 1.4 Intra-G forks and compressions (disclosed, and where resolved)

- **Initiator vs footprint** (which site a G-event attaches to): posed as an
  UNSETTLED fork and measured — "Which of the two the corpus means is not
  settled anywhere.  Agreement or divergence between them is a measured
  output" (v14/paper-14-u4-renewal-crystals.md:128–133); paper-17 measures
  the footprint reading to be a census artifact at its arena
  (v14/paper-17-schedule-census.md:231–246).  Named readings, disclosed.
- **Seat vs footprint**: a G-event's seat is arbitrated within its own
  conflict group ("re-seating moves one division event to another cell of
  its own conflict group", v14/paper-19-r3-weld.md:259–260) while its
  footprint writes the whole group.  Both objects are formal; the corpus
  keeps them apart by the words "seat"/"re-seating" vs "footprint".
- **The paper-32 compression**: "A division event knows an actor pair and
  nothing else" (v14/paper-32-sec.md:122–123) is a per-deposit statement
  (each written incidence is keyed by a co-division pair and carries no
  chart index); the same line's own unit family states the three-actor unit
  as FORCED (v14/paper-40-sec2.md:722) and three incidences per event
  (:326–329).  Read :122 as "each deposit knows an actor pair", never as a
  pair-primitive event.

### 1.5 Forward bindings (engraved elsewhere, indexed here)

Paper-20's primitive is **CELL-HIT**; "division event" in new work refers
only to the three-actor grammar object (RUNBOOK E-34.3).  At extension arms
the arity is stated ("a-actor division event"; the a=2 arm says
"pair-events" — v15/paper-46-ecc.md:208, v15/PLAN.md:23).  Recommendation of
this registry (no proof owed): successors inheriting the R-sense stages
(papers 10/15/18/22) should say "renewal times" for "division-event times",
since the R↔G identification remains a scrutinized [POSIT], not a theorem.
Probability claims declare their sample space before any equation and
normalize over mutually exclusive complete local successors (E-34.4).

---

## 2. The per-term table

Senses listed are FORMAL objects only.  TEC = TYPE-ERROR-CANDIDATE
(details and repairs in §3); DP = DISCLOSED-POLYSEMY; SS = SINGLE-SENSE.

| term | formal senses found | verdict | key evidence |
|---|---|---|---|
| **division event** | R renewal marker / G three-actor grammar event / C CELL-HIT | **TYPE-ERROR (REALIZED at G↔C; repaired at #55)** | §1; the repair = the CELL-HIT rename + this registry + E-34.1–5 |
| **event** | grammar event of any kind (menus offer 124, 44 division; 76 realised of any kind, 20 division — v14/paper-13:300–303) / division event (the bound subset) / walk emission (renamed CELL-HIT) / a-parametrized event (ARITY dial) | DP (post-#55) | ECC's binding: "an event is a set of actors of the declared arity dividing together, and nothing else is called one" (v15/paper-46-ecc.md:170); no spacetime-point sense anywhere (papers 01–03: zero uses) |
| **menu** | grammar menu offering EVENTS / the walk's emission menu offering CELLS with two weightings (Born menu / record menu) / FAC's grain menu ("the admissible actor grains") / observable menu | **TEC #1** | §3.1 |
| **carrier** | record-lattice carrier / grammar-side carrier / actor-participants of an event / quantum host H_G / support idiom / ECC's table column (ONE-STATE vs ENSEMBLE) | **TEC #2** | §3.2 |
| **seam** | the shared site itself ("A seam is a shared site", v14/paper-40-sec2.md:131) / the completion datum at a shared site ("the seam \| the completion at a shared site", v15/paper-43-contract.md:583; v15/paper-46-ecc.md:198) | **TEC #3** | §3.3 |
| **history** | grammar history (sequence of division events, v14/paper-33-aid.md:43) / emission (branch) history of the walk (v14/paper-24-sig.md:553; v15/paper-47-disc.md:458) | **TEC #4** | §3.4 |
| **chart** | AG(2,q) patch (SEC/AUTOGLUE/ECC; Q28–33) / the seam chart = the direct-sum identification MAP (v14/paper-32-sec.md:844) / the seam's spanned 4-dimensional local chart (v15/paper-45-autoglue.md:291–293) / "pinned chart group" on split fibers (v14/paper-30-lor.md:164, a paper-06 object) / continuum-rung charts (v14/paper-01:218) / ECC's dial row "the two-sector overlap type" (v15/paper-46-ecc.md:190) | **TEC #5** | §3.5 |
| **cell** | record/Born cell = co-division pair with a direction (bound: v15/paper-46-ecc.md:171; v14/paper-41-rec.md:96) / census candidate cell with a well-typedness predicate (v14/paper-13:305–307) / coordinate cells (k, rule) and nerve 0/1/2-cells (v14/paper-01:209–222) | DP | every non-record sense is prefix-qualified at point of use; WATCH: the R-line continuation merging paper-01/02's topological cells with weld cells owes a binding line.  Note the inverse hazard: cell / link / record interval are near-coextensive with distinct intensions (a link IS an unordered pair of sites, v14/paper-32-sec.md:118–119; a cell carries the direction, v15/paper-46-ecc.md:171) — a synonym cluster, one binding-table line recommended |
| **site** | a vertex of the record lattice / actor position (identity map actor→site exhibited, v14/paper-13:306–308) | SS | paper-13's generator SLOT "site ← {ACTOR, MENU-CLASS, …}" is a declared axis of that census, named as such (v14/paper-13:288–292) |
| **block** | cross block of the seam form (v15/paper-45-autoglue.md:355, :752) / record block = one event's written cell-set (v14/paper-41-rec.md:161–165, :274) / partition block (v14/paper-35-fac.md:126) / substrate block index (v14/paper-01:209; v14/paper-02:138) | DP | always compound-qualified ("cross block", "record block", "block of π", "block index") |
| **sector** | one of the two glued 9-actor arenas (v14/paper-32-sec.md:84 ff.; live in AUTOGLUE :77) / qualified subspace strata: "front sector", "register sector" (v14/paper-03:320, :515–516), "the q₁₂=0 sector" (v14/paper-04:87) | DP | bare "sector" = the arena copy only in SEC-line units; every subspace sector carries its qualifier |
| **state** | the one-instant machine state, RULED reading-relative with branch weight excluded as ensemble bookkeeping (v15/paper-43-contract.md:187–250; sealed at Q2, v15/QUESTIONS.md:5) / SEAM-SUBSYSTEM STATE, "a structural state and not the state of the process" (v15/paper-45-autoglue.md:295–297) / the run-level ensemble ("the state is an ensemble over emission histories", v15/paper-47-disc.md:458) / the open universal state (v15/paper-43-contract.md:187–192) | DP | consistency with CONTRACT's ruling checked: ECC re-binds it verbatim and stamps its two READING-RELATIVE rows with WHICH reading (v15/paper-46-ecc.md:174, :149–157, :628); AUTOGLUE discloses structural-vs-process.  The one tension: DISC:458's bare "the state" names the run-ensemble — disclosed by its row label ("the branch structure") but crossing CONTRACT's binding; future prose should say "the ensemble/process state" (registry line, no edit owed) |
| **record** | the run's event sequence ("The record is FORCED at 1,040 of 1,040 driven window schedules", v14/paper-19:173) / the count field–co-division relation with multiplicities ("The record is n_ℓ(x)", v14/paper-35:103; bound: v15/paper-46-ecc.md:173) / THE BARE RECORD (ordered cell-set sequence, v14/paper-41:96–99) | DP (borderline) | the sequence→field identification is the count semantics itself, explicit everywhere; ECC binds one sense for the live layer; recommendation: every new unit's term table binds record(sequence) vs record(field) before any blanket predicate ("forced", "blind", "invariant"), since those predicates change truth value with the sense |
| **window** | driven-schedule window (bound: "the window \| the driven schedule set", v15/paper-46-ecc.md:192; v14/paper-19:173) / the count window between two declared arbitration cuts (v14/paper-13:666–667) / coset windows BLOCKWISE/SLIDING (v14/paper-02:196–197) / sliding observable window over a history (v15/paper-43-contract.md:347) / enumeration windows ("grouping window", "permutation window", v15/paper-44-arity.md:771–772) | DP | each instance qualified at point of use; ECC's table binds its own |
| **saturating** | grouping/record saturation with the MEASURED FORK: LITERAL (weight = budget n) vs MAXIMAL (v15/paper-44-arity.md:129, :219–228; coincidence at q=3 disclosed at v14/paper-39-ndep.md:120–123; the fork SELECTS the characteristic at n=16, v15/paper-50-arity16.md:15) / ⟨Σ⟩-saturation = group closure (v14/paper-01:213, :279) | DP | ARITY publishes both readings on every row; paper-01's operator is prefix-bound; "saturates the bound" elsewhere is ordinary math English, not a sense |
| **footprint** | the event's register/actor set, site-projected for the count semantics (v14/paper-33-aid.md:159–164; v14/paper-14:453) | SS | footprint-vs-initiator are NAMED READINGS of site attachment, measured (v14/paper-14:128–133; v14/paper-17:231–246); the written cell-set is called "the record of an event" (v14/paper-41:96–98), not the footprint |
| **division** | derivative cluster of the G-object (co-division pair/relation, division count, division predicate, division-set edit) | SS | caveat carried by the register, not the word: "division count" inherits the arity of its writer (§1.2) |
| **crossing** | seam-spanning pair/event (v14/paper-40-sec2.md:303–309; "108 lawful crossings", v15/paper-46-ecc.md:261) | SS | v14/paper-12:532's "the crossing" (gravity–quantum) is programmatic metaphor, not counted |
| **weld** | the record↔metric identification ("the division count the weld identifies with the metric", v15/paper-43-contract.md:195; "the geometry is … the object the weld reads", v15/paper-46-ecc.md:172); unit names (weld 2, R3-weld) derivative | SS | v12's "THE WELD" (composition defect) is another era; no live paper inherits that referent |
| **completion** | seam-form completion (lattice of 31 at kernel 4, v15/paper-46-ecc.md:263; v15/paper-45-autoglue.md:880) / refinement-split completion ("the declared minimal completion", v14/paper-04:91; "3 declared split rules × 2 declared completions", v14/paper-13:271–272) | DP | both always attach to their construction |
| **reading** | the corpus's term of art for a declared interpretive fork; instances: THE-READING = Born/record menu (v15/paper-43-contract.md:219), persistence vs re-solved (v15/paper-46-ecc.md:155–157), F4-LINEAR vs ABSTRACT (v15/paper-50-arity16.md:15), EMBEDDING/QUOTIENT, footprint/initiator, LITERAL/MAXIMAL | DP | every live stamp names its fork at point of use (ECC:155–157 exemplary; ARITY-16 "EVERY WORD … CARRIES ITS READING", :23); registry caution: the bare stamp "reading-relative" transported ACROSS units names DIFFERENT forks — a transported stamp must name its fork |
| **fiber / fibre** | the value-set of a free declaration or of a map, base always given (W3, v15/PLAN.md:11; "declaration fiber", v14/paper-40:402; "site fiber", v14/paper-04:183) | SS (template) | — |
| **extension** | extension family (arities off the committed grammar, v15/paper-44-arity.md:125) / extended carrier (v14/paper-32-sec.md:394, §4.3) / EXTENSION-EDGE (v14/paper-13:288) | DP | compound-qualified everywhere |
| **price** | the declaration-accounting idiom (a named cost of a choice; e.g. v15/paper-46-ecc.md:731) / SEC2's measured link cost ("a link costs the division events that realise it", v14/paper-40-sec2.md:241) | DP | both local and explicit |
| **free** | free declaration (CONTRACT census class; heterogeneous categories, NEVER a count of physical constants — legislated at v15/PLAN.md:23) / free numbers (adjustable constants column, v15/paper-47-disc.md:454) / free fibre (W3) | DP | the declaration-vs-constant split is legislated and typed (ECC carries the 15 free rows WITH TYPES, v15/paper-46-ecc.md:176–178) |
| **law** | the confirmed emission/probability law (v14/note-coupling-pin.md:67–68) / "law-selected" classifier (CONTRACT: FREE-ROWS-A-LAW-SELECTS=0, v15/paper-43-contract.md:48) | DP | noun vs hyphenated classifier; no crossing found |
| **rule** | declared-map template; instances always named (emission rule, feedback rule, packing rule, split rules, seed rule) | SS (template) | v15/paper-47-disc.md:454–460 |
| **round** | grammar round = a partition of all nine sites realised as division events ("A round is a partition of all nine sites", v14/paper-24-sig.md:395–397; "R \| the depth in rounds", v15/paper-46-ecc.md:188) / review round (process register: LOG/RUNBOOK/pins only) | DP | registers disjoint; no paper uses "round" for a walk step ("step" is the walk's word, v15/paper-47-disc.md:457) |
| **gauge** | the W2-earned redundancy word — DEFINED and WITHHELD ("gauge = identical values for EVERY observable and experiment", v15/PLAN.md:9; "The gauge word is withheld here", v15/paper-43-contract.md:28) / subject-matter gauge structure in the R5 line ("residual gauge group on the carrier", v14/paper-27-smu.md:157–159; v14/paper-18 passim) | DP (hazard noted) | any unit quoting paper-27/34's "gauge group" must not read it as an EARNED redundancy claim; W2 + CONTRACT's withholding are the guard; binding-table line owed by any unit citing those groups |
| **defect** | measured physics mismatch (register-sector defect, v14/paper-03:515–516) / programme defect class (v14/note-d60-defect-register.md:1–10) | DP | registers disjoint |
| **instrument** | the unit's verification code (every unit; e.g. v15/paper-43-contract.md:221–223) / the classical–quantum instrument {p_G, ρ_G} (ECC step-3 candidate formalism, v15/PLAN.md:23; "CPTP-instrumented", ibid.) | DP | the quantum sense is always compound-qualified; both live inside ECC |
| **budget** | the packing/actor budget n (LITERAL saturation reads it, v15/paper-44-arity.md:129) / the incidence budget 3k ("a law of the budget", v14/paper-30-lor.md:338) / achievable budgets = attainable mass sums (v14/paper-39-ndep.md:112, :336–340) | DP | quantitative cousins, each computed in place; ARITY's tables key them apart ("saturating at the budget", "achievable budgets") |
| **link** | the record edge: "a link IS an unordered pair of sites" (v14/paper-32-sec.md:118–119), with the individuation FORK a measured declaration — SIMPLE vs CHARTED, spent at exactly two places (v14/paper-32-sec.md:118–124, :841) | SS (fork disclosed) | see the cell row for the cell/link/interval synonym-cluster line |
| **cut** | a record/timeline position at which a record is split or a leg conditioned (arbitration cuts, v14/paper-13:666–667; declared cut times, v14/paper-10:342–344) | SS | — |

---

## 3. TYPE-ERROR-CANDIDATEs, ranked by risk (load-bearing × conflatable)

The anchor case — division event, G vs C — is REALIZED and REPAIRED (§1);
it heads the list as precedent, not as an open item.  Five open candidates:

### 3.1 MENU (highest risk)

**Senses.** (a) Grammar menus offer EVENTS: "the **124** its menus offer (of
which **44** are division events)" (v14/paper-13-weld2-carrier-census.md:300–303;
"every specification matched by exactly one menu candidate",
v14/paper-19:148–150).  (b) The walk's emission menu offers CELLS: "The menu
at site x is the three link traversals" (v14/paper-20-coupling.md:216–217),
with Born menu / record menu its two declared weightings (:216–219); also
"site menu" (v15/paper-43-contract.md:481), "the walk's menu … in cells"
(v15/paper-46-ecc.md:572), "emission menu" (:581).  (c) A THIRD object in
CONTRACT's own census: "the menu \| the admissible actor grains"
(v15/paper-43-contract.md:593, FAC's grain object).  (d) "observable menu"
(v15/paper-46-ecc.md:76), qualified.

**Why TEC.** The menu word sits exactly on the diagnosed fault line: the
grammar's menu-alternatives are events, the walk's are cells, and the type
error WAS the identification of a menu-selected cell with a grammar event.
**Risky site:** v15/paper-43-contract.md:420 — "the menu weights the next
division event" — a sealed influence-table row in which bare "menu" (walk
sense) and un-renamed "division event" (CELL-HIT sense) co-occur, one line
from a paper whose OTHER row :593 binds "the menu" to FAC's grains; a
successor citing "CONTRACT's menu" can grab either object.  The scout's S2
kernel K(e\|c,G,R) (v15/note-scout-pin.md:55) will condition cells on events
— menu language will carry that bridge.

**Cheapest repair.** Term-binding entries, no proof owed: EVENT-MENU
(grammar), EMISSION-MENU with Born/record as its two WEIGHTINGS (walk),
GRAIN-MENU (FAC).  Registry line for the sealed rows: paper-43:420's "menu"
= the emission menu and its "division event" = CELL-HIT; paper-43:593's
"menu" = FAC's grains.

### 3.2 CARRIER

**Senses.** (a) The record-lattice carrier — the census object (the whole of
v14/paper-13; "the carrier is a family, not a record", :580; "the carrier is
ACTOR ⊕ PAIR", v14/paper-30-lor.md:307; "the (A,B) 2-actor carrier",
v14/note-coupling-pin.md:67–68).  (b) The GRAMMAR-side carrier — "a
MOTIVATED map … from the transport grammar's carrier"
(v14/note-weld2-census-pin.md:14, :71–73 "BOTH carriers").  (c)
Actor-participants of an event: "15 carriers, 54 realised pairs"
(v15/paper-46-ecc.md:261); "a footprint whose carriers have been replaced by
opaque tokens" (v15/paper-45-autoglue.md:53, :243).  (d) The quantum host:
"§7 The variable carrier" — H_G, growing 27→28 cells
(v15/paper-46-ecc.md:526, :540–544; v15/PLAN.md:23 step 3).  (e) The support
idiom: "The walk's emission menu is its own carrier: every weight lands on a
realised cell" (v15/paper-46-ecc.md:581–582).  (f) ECC's interface-table
COLUMN "carrier" ∈ {ONE-STATE, ENSEMBLE} (v15/paper-46-ecc.md:120, :127).

**Why TEC.** Four-plus formal referents, three of them inside ECC — the
spine's parent.  **Risky site:** v15/paper-46-ecc.md:540–542, "the growing
carriers host the created cell and the fixed carriers host the
fixed-background state", one sentence in which "carrier" is the quantum
host, adjacent to §6's "15 carriers" (actors) and :581's support idiom; DC
will compose ECC's three maps over "the carrier" and must know which object
the complete state X contains.

**Cheapest repair.** Rename going forward, entries in every new pin's
binding table: actor-participants → "actors" (pure prose); "the carrier"
bare = the record-lattice carrier; "the quantum carrier / H_G host" for §7's
object; ECC's table column read as "bearer kind" (registry line; the sealed
table is not edited).

### 3.3 SEAM

**Senses.** (a) The shared site: "A seam is a shared site, and its type is
the pair of count vectors its two [sectors carry]"
(v14/paper-40-sec2.md:131); "seam-spanning division event" (:754) uses this
sense.  (b) The completion datum AT a shared site: "the seam \| the
completion at a shared site" (v15/paper-43-contract.md:583;
v15/paper-46-ecc.md:198, typed COMPLETION-DATUM); the seam decision
(persistent vs re-solved, v15/paper-46-ecc.md:241 ff.) and AUTOGLUE's
SEAM-SUBSYSTEM STATE (v15/paper-45-autoglue.md:295–297) target this object.

**Why TEC.** Two incompatible type bindings for the bare noun across sealed
papers — precisely E-34 rule 1's refusal condition for any new pin that
inherits both.  **Risky site:** v15/paper-46-ecc.md:60, "a transition
relation on a seam" — on the site or on the datum?  (It is the
datum/subsystem state; the sentence does not say so.)

**Cheapest repair.** Bind bare "seam" = the shared site (SEC2's sealed
definition); mandate "seam datum / seam completion" for the data — ECC
already uses "the seam datum" (v15/paper-46-ecc.md:305–308), so the split
costs one binding-table line in the DC and scout pins.

### 3.4 HISTORY

**Senses.** (a) Grammar history: "A committed history is a sequence of
division events" (v14/paper-33-aid.md:43; CONTRACT's census histories,
v15/paper-43-contract.md:347, :383).  (b) Emission/branch history of the
walk: "the *same* measure over emission histories"
(v14/paper-24-sig.md:553); "the state is an ensemble over emission
histories" (v15/paper-47-disc.md:458).  Post-split these are sequences of
DIFFERENT event types (division events vs CELL-HITs).

**Why TEC.** **Risky site:** v15/paper-43-contract.md:221 — "A state list is
sufficient when it screens the history off the update" — an un-typed
"history" inside a load-bearing sufficiency claim (the measured content is
layer-neutral; the sentence is not).  The scout's S4 joint successor law
(v15/note-scout-pin-addendum.md, item 6) will define JOINT histories
(recorded event + state update) and must not inherit the bare word.

**Cheapest repair.** Binding entries GRAMMAR-HISTORY / EMISSION-HISTORY
(both qualified forms already exist in the corpus; make the qualifier
mandatory in new work); registry line that CONTRACT:221's history is
whatever past produced the listed state, either layer.

### 3.5 CHART

**Senses.** (a) The AG(2,q) patch — the two glued copies (SEC/AUTOGLUE/ECC:
"chart-preserving maps", v15/paper-45-autoglue.md:251–256; "the committed
chart", v15/paper-46-ecc.md:20, :723) and Q28–33's overlapping charts
(v15/QUESTIONS.md:40–45).  (b) The seam chart — an identification MAP: "the
seam chart: the direct-sum chart \| declared" (v14/paper-32-sec.md:844;
v14/paper-40-sec2.md:707), doing load-bearing algebra in "rank 6 on 10 by
the chart alone, kernel 4" (v15/paper-43-contract.md:640).  (c) The seam's
spanned local space: "the two charts' directions span a four-dimensional
chart whose form has rank 6 on 10 unknowns"
(v15/paper-45-autoglue.md:291–293) — two chart-objects in one sentence.
(d) "the pinned chart group" on split fibers (v14/paper-30-lor.md:164, a
paper-06 inheritance, unrelated to patches).  (e) Continuum-rung charts
(v14/paper-01:218).  (f) ECC's dial row: "the chart \| the two-sector
overlap type" (v15/paper-46-ecc.md:190).

**Why TEC.** Every current use is locally qualified, but a REGISTERED
argument is coming that turns on the word: COSET-FROM-COMPATIBILITY
(v15/PLAN.md:27) will decide whether the coset event principle FOLLOWS from
"chart compatibility" — if its "charts" silently absorb the seam-chart (a
map), the spanned local chart (a subspace), or the dial (an overlap type),
the a=q upgrade could be argued at the wrong object.

**Cheapest repair.** The charts-successor pin's term-binding table (already
owed under E-34.1) with the six entries above; in new prose "chart" = the
patch only, "seam chart" always compound, the spanned space renamed ("the
seam's four-dimensional direction space").

---

## 4. Summary

The sweep confirms the corpus's one realized type error and finds no second
realized one: "division event" named three formal objects across the live
corpus — renewal marker (v11 POSIT, carried by papers 04–10/15/18/22, with
the R↔G identification disclosed and type-audited in paper-09), three-actor
grammar event (papers 13–41 grammar line, bound forward by E-34.3), and the
walk's one-cell emission (papers 20/24/25, DISC, and CONTRACT's influence
table — now CELL-HIT) — and the G↔C pair stayed hidden because both writers
share the register n_ℓ(x) at different arities (3 vs 1), surfacing only as
ECC's Mp=3q infeasibility.  Of 36 terms audited, 5 are open
TYPE-ERROR-CANDIDATEs, all repairable by binding-table lines and prose
renames with no proof obligations: MENU (grammar event-menus vs the walk's
cell-menu vs FAC's grain row, with CONTRACT:420 the risky sealed row),
CARRIER (lattice carrier vs actor-participants vs quantum host, three of
them inside ECC), SEAM (SEC2 binds the shared site, CONTRACT/ECC bind the
completion datum — E-34 rule 1's refusal condition already standing between
sealed papers), HISTORY (grammar vs emission histories astride CONTRACT's
sufficiency sentence and the scout's S4), and CHART (patch vs seam-map vs
spanned space vs chart-group, with the registered COSET-FROM-COMPATIBILITY
argument the place a conflation would bite).  Everything else is
SINGLE-SENSE (site, footprint, division, crossing, weld, fiber, rule, link,
cut) or DISCLOSED-POLYSEMY with the disclosure located (event, cell, block,
sector, state — CONTRACT's reading-relative ruling is honored everywhere,
with DISC:458's run-ensemble "state" the one flagged tension — record,
window, saturating, reading, completion, extension, price, free, law, round,
gauge, defect, instrument, budget); the recurrent healthy pattern is that
the corpus's own units measured their forks (paper-14's D1, paper-17's
footprint-reading, ARITY's saturation split, SEC's link individuation) and
named them, which is what E-34 now makes mandatory rather than customary.
