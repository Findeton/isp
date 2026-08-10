# Γ-MAIN (paper-12) — HOSTILE REVIEW, R2 / EFFECTUS (the meaning audit)

**Object (hashes verified before and after all work):** paper
`d85a629a9378`, code `51c3b4cf3f3c`, output `b2b45be500b7`, receipt
`974f36b1251a`; pin `8529ddc4a319`; protocol `a3a39813e5b5` (PANEL A).
**Assigned depth:** K2 (primary), K3, K4, K5, the settlement
re-evaluation, the next-iteration recommendation.
**Method:** full independent rebuild in scratch — the d42b1 layer
exec'd from its own committed bytes at the pin's declared sha
(`576275d55ecf` verified), the carrier, the potentials, both quotients,
the square census, the three holonomy readings, the leg ensembles, the
CK census, the eq-22 candidates and the inventory all recomputed from
first principles. No import of the unit's code; no run of the unit's
delivery script (a plain run writes repo artifacts); one repo write.

**Standing: 113 independent recomputations, ZERO numerical divergences.
Every delivered number I recomputed reproduced exactly, to the last
rational.** The defects are in what the verdict *concludes*, in one
must-pass gate that cannot fail, and in a settlement conjunct that no
object of this kind could ever have satisfied.

**Grade: ACCEPT-WITH-FIXES (fixes BLOCKING).**

---

## 1. Findings, ranked

### F-1 (MAJOR, decisive for K2) — the settlement is evaluated across two different arenas, and §15 forbids its second conjunct

The unit declares `readout` as an **arena coordinate** (§2 arena table,
`OCCUPANCY primary, COUNT alternative — the fiber is 2`). RUNBOOK §15:

> Claims of physical significance are entered only for quantities GATED
> as invariant across the unit's admissible arenas; arena-artifacts may
> serve as instruments but never as conclusions.

The position law is **not** invariant across the unit's own two
declared readouts — (3/7,1/7,3/7)/(4/9,1/9,4/9) at COUNT versus
(3/8,1/4,3/8) at OCCUPANCY, all four values recomputed here. It is
therefore an arena-relative quantity, admissible as an instrument and
**inadmissible as a conclusion**. `SETTLEMENT.targets_hit` enters it as
a conclusion.

Worse, the four conjuncts are not evaluated at one arena:

| conjunct | the readout at which it holds |
|---|---|
| constructed (exact column-stochastic) | **OCCUPANCY only** — see F-3 |
| targets hit | **COUNT only** |
| holonomy consistent | neither (see F-4) |
| motivation non-empty | readout-free, but measures the wrong thing (F-7) |

A conjunction whose conjuncts are true at different coordinates is the
§15-addendum disease verbatim ("a class-vs-class verdict whose classes
are read at different coordinates is a coordinate effect in disguise").
**Repair:** fix the readout first, evaluate every conjunct there, and
run the other readout as a control. At the unit's own declared PRIMARY
the second conjunct is **False**.

### F-2 (MAJOR, new measurement — the readout question is decided by the unit's own controls)

The unit never runs its battery at the COUNT readout. I did. Adopted
consistently at the class level, the count readout destroys three
things the unit relies on, and buys exactly one:

| quantity | OCCUPANCY | COUNT |
|---|---|---|
| position-law targets | **missed** (3/8,1/4,3/8) | **hit** |
| REC holonomy (the mandatory negative control) | flat, 473/473 unit | **NOT flat: 296/473 non-unit, primes [2,3,5,7], rank 4** |
| REC Chapman–Kolmogorov (exact lumpability) | 0 of 10 triples fail | **10 of 10 fail** |
| MENU non-Markov census | 4 of 10 | 10 of 10 |
| Γ-family group | [2,3,5,13,19,97,389] rank 7 | [2,3,5,7] rank 4 |
| CR-B's missing object | **exists** (one point at both legs) | does not exist |
| column-stochastic as literally described | yes, 544/544 columns | **no: 0 of 544** (F-3) |

The pin's holonomy gate *itself* requires "REC flat". **The readout at
which the targets are hit is the readout at which the pin's own
negative control fails.** That is not a tie between two readings; it is
the unit's own control structure selecting OCCUPANCY, and it is
measurable in one afternoon. It must be in the paper.

### F-3 (MAJOR) — only one member of the fiber is a law; the class-level COUNT readout is never built

`gamma_family` is called twice, both times with the occupancy weights
`W`. **No count-readout Γ exists in the code.** The inventory item
`I-READOUT` is declared as "the class-level readout" and its `measured`
field is filled with **leg-level** statistics (`CNT1/WGT1/CNT2/WGT2`) —
a fiber-2 claim about the class-level lift whose only evidence is a
statistic computed on objects at depths 3…10, outside the d≤4 carrier
and outside the d≤5 anchor. The unit's own arena string admits the
slippage: it defines COUNT as "**equiprobable admissible legs**" while
the inventory calls the same item "the class-level readout". Those are
two different choices sharing one name, and the verdict rides on the
conflation.

And the count readout as the code describes it ("the same construction
with the uniform measure on the admissible objects in place of w") is
**not a law**: I built it and 0 of 90 MENU columns and 0 of 454 REC
columns sum to 1 (they sum to the branching factors 7, 8, 53, 60, 452,
3448). It becomes column-stochastic only after an *undeclared* second
choice — renormalising by the descendant count rather than the class
size. So the "fiber of two" is really: one member that is the process's
own disintegration (the flow identity `w(h)k_r(e|h) = w(h+e)`, verified
exact at 3968/3968 transitions), and one member that needs a repair
nobody declared before it is even a family.

### F-4 (MAJOR, K3) — "holonomy consistent" is unsatisfiable-by-construction at this carrier; the reported failed link is an artefact of a mis-posed conjunct (my own pin — I rule against it)

Two facts, both recomputed:

1. The pinned weight law is **not** stochastic: Σ_e q(e|root) = 2
   (= G(root,1)). Horizon normalisation is not a stylistic choice, it
   is the only route to a column-stochastic family — the unit's "the
   step that makes the construction possible at all" is exactly right.
2. **The deviation is an identity, not a census.** For every closed
   exchange square,
   `r_k = r_q · G(h e_A e_B, r−2) / G(h e_B e_A, r−2)` —
   verified at **1546 of 1546** squares, 0 violations. The correction
   factor is 1 exactly when the potential agrees at the two endpoints;
   the endpoints of a *closing* square lie in the same class; so the
   factor is 1 **iff the potential descends**. Exactly 8 squares carry
   a non-unit factor (6 at 64/65, 2 at 65/64, all at base depth 0), and
   their endpoint classes are precisely the 4 of 13 depth-2 classes on
   which G(·,2) is multi-valued.

Therefore: *any* column-stochastic construction from the pinned law on
a carrier where the potential fails to descend has a k-holonomy group
strictly larger than the q-group. `holonomy_consistent = (T2_VERDICT ==
'AGREE')` demanded that the normalised connection carry the group of an
object that is **not a law**. It could not have come out otherwise. A
conjunct no admissible object can satisfy is not a test.

The pin's §3.2 wording was well posed — "agreement **or the measured
deviation, exactly**". The pin's §4 settlement clause silently
converted a measure-and-report gate into an agreement demand. **That
conversion is the effectus's error (my predecessor's ruling produced
the gate) and I own it here.** The unit inherited it faithfully and
reported PARTIAL against it.

Second, independent defect in the same conjunct: `AGREE` additionally
requires the **Γ-family**'s group to equal ⟨2,3⟩. Γ's entries aggregate
every event carrying one class into another; its "holonomy" is the
curvature of a coarse-grained *law*, not of a connection. Demanding
that an aggregated transfer ratio equal a connection's holonomy is a
category error, and no carrier makes it true (see F-5: even where the
connection is exactly ⟨2,3⟩, the family is rank 4).

**What the third conjunct should have demanded** (all three measured,
all three flippable): (i) the q-reading reproduces D74's rung on the
carrier digit for digit — measured, 1402 closing / 44 obstruction / 44
self-loops / cycle rank 134; (ii) every derived reading's deviation is
attributed to a named cause and **gated by the identity above**; (iii)
REC flat at all readings **at the declared readout**. At that conjunct
the unit passes.

### F-5 (MAJOR, new construction — the successor carrier exists and is derivable, not new)

The protocol asks whether the quotient lattice between MENU and REC
contains a carrier with **both** descent and holonomy, and whether it
is derivable from the pinned artefacts. **It is derivable, in one
line:** refine MENU by the value of the horizon potential the
construction actually uses,

> `MENU+G := (MENU class, G(h, 4−|h|))`.

Measured here:

| | MENU (the declared carrier) | **MENU+G** | REC |
|---|---|---|---|
| classes | 113 | **181** | 2477 |
| dims per cut | [1,5,13,45,113] | **[1,5,17,45,113]** | [1,8,51,324,2093] |
| lattice position | — | **MENU ≼ MENU+G ≼ REC** (both verified) | — |
| G(·,r) multi-valued | 4/13 at r=2 | **0 at every r** | 0 |
| q-reading | 1402 close, obstr 44, ⟨2,3⟩ rank 2 | **1394 close, obstr 44, ⟨2,3⟩ rank 2** | flat |
| k-reading | primes [2,3,5,13] rank 3 | **[2,3] rank 2 — IDENTICAL to q** | flat |
| Γ column-stochastic | exact | **exact (0 violations)** | exact |
| 44 + 44 dichotomy | 44 / 44 | **44 / 44 preserved** | — |
| CK failures | 4 of 10 | **2 of 10** (still non-Markov) | 0 of 10 |
| Γ-family group | rank 7 | rank 4, [2,3,13,19] | trivial |

Only the depth-2 cut splits (13 → 17), and exactly the 8 deviating
squares stop closing (1402 − 8 = 1394), which is why the 64/65 and
65/64 self-loops vanish while D74's 44-obstruction row survives intact.
**On MENU+G the horizon-normalised connection carries exactly D74's
⟨2,3⟩, descent holds at every horizon, the curvature is still
non-trivial, and Γ is still exactly column-stochastic.** The conjunct
the unit reports as failed is satisfiable one refinement away, at a
carrier the pinned artefacts already determine.

Consequence for the inventory: `I-CARRIER = FORCED, fiber 1` is
**wrong** as stated. It is forced among *D74's six committed rungs*;
among quotients it is not, and one derivable alternative meets the
unit's own stated criterion (descent of the quantity the construction
uses) strictly better. Reclassify as
`FORCED-AMONG-D74-RUNGS / GENUINELY-FREE-IN-THE-LATTICE`, with MENU+G
printed.

### F-6 (MAJOR, instrument, but it is my gate) — T2-HOLONOMY cannot fail, and its stated justification is false

```
T2_VERDICT = 'AGREE' if (...) else 'DEVIATE-AT-' + ('BOTH'|'K'|'GAMMA')
gate('T2-HOLONOMY', 'MUST', ..., T2_VERDICT in ('AGREE','DEVIATE-AT-K',
     'DEVIATE-AT-GAMMA','DEVIATE-AT-BOTH'), ...)
```

The predicate tests membership of a string in the exact set of strings
its own constructor can produce. It is **analytically forced for every
input** — RUNBOOK §14 (v13 #208): "Analytically-forced clauses (true by
algebra for every input) are **disclosures, not must-pass gates**."
The unit's compliance sweep reports "literal-True consumers 0", which
is true *syntactically* and false *semantically*: the check is for the
literal `True`, and an always-true expression walks through it.

Its declared falsifier does not touch it. `MUT-HOLONOMY-DRIFT` injects
5/4 into the **q-spectrum** and dies to `T2-D74-ANCHOR`'s predicate; it
can never move T2-HOLONOMY's. The never-falsified census scores
T2-HOLONOMY as covered because a killed mutant *names* it in a target
string — coverage by declaration, not by "dies by the gate's own
predicate", which is what the gate's own statement promises.

And the sentence that justifies its falsifiability — "the comparison
could have come out either way (**REC returns AGREE-trivially on the
same instrument**)" — is false under that instrument: on REC the
k-reading has primes `[]` and rank 0, so `_agree_k` and `_agree_g` are
both False and the same code returns **DEVIATE-AT-BOTH**, not AGREE.

**This is the gate the previous effectus round demanded precisely so
that "Γ-main lands" would be falsifiable.** It must be rebuilt as a
gate that can fail — the natural one is F-4's identity: *the k-group
equals the q-group iff the potential descends on every closing square*,
which a one-value perturbation of G kills.

### F-7 (MEDIUM) — `motivation_non_empty` does not measure motivation of the load-bearing choices

`(len(_forced) + len(_stab_i) > 0)` is satisfied by I-CARRIER, I-CAP,
I-RENEWAL, I-BLOCKS and I-PRUNE — none of which is in dispute. The
unit's own text says "the free item that carries the unit is
I-READOUT". At the RSQ standard the question is not whether the
inventory has a motivated row; it is whether the choices the *verdict
rides on* are motivated. Measured honestly: the carrier/holonomy
segments ride on motivated choices; the targets segment rides on a free
one. **Repair:** compute, per verdict segment, the class of the choices
it descends from, and report `MOTIVATION` per segment. (And with F-5,
I-CARRIER's own class moves.)

### F-8 (MEDIUM, K4) — the eq-22 refutation exists only at the identity padding; the other conventions are silent, not contrary

I tested three completions. Under the identity padding the padded
transfer is invertible at all four non-degenerate triples and Ḡ carries
36 / 104 / 108 / 164 negative entries with column sums exactly 1 —
reproducing the unit's numbers exactly. Under a **reset** padding
(unrealised configurations sent to a declared default) and a
**uniform** padding, the padded transfer is **SINGULAR at all four
triples**: eq. 22 has no unique candidate and the algebraic reading
says nothing at all. So the convention is not one choice among equals
with a competing answer — it is the only one of the three that lets the
test speak. That strengthens the choice and simultaneously fixes its
scope: **the refutation is of eq. 22's *form* at the identity padding,
and it does not transfer off the convention.** `I-PADDING fiber 2` is
counting conventions, not conventions that support a result — a
different quantity from the fiber-2 that carries I-READOUT (where both
members yield opposite results). State which fiber semantics is in use.

### F-9 (MEDIUM, K5) — three verdict segments carry arena-variant quantities without their restriction, and two are hard-coded

- `REC-FLAT-AT-ALL-THREE-READINGS` is a **string literal** in
  `SEG_REQ`, not rendered from `_rq/_rk/_rg` — and it is true only at
  the occupancy readout (F-2). §13 addendum (#234): the verdict string
  must be derived inside a gate from the measured counts.
- `D74-{2,3}-RANK-2-REPRODUCED`, `KERNEL=INDUCED;N-INDEXED-AT-...`,
  `MOVER=BLOCKED-AT-REFERENT-...` are likewise literals. The paper's
  "every segment computed in-gate" overstates what the code does.
- `GAMMA-PRIMES-{...}-RANK-7` and
  `INTERPOLANT=NON-MARKOV-AT-4-OF-10-...-REC-EXACTLY-LUMPABLE` are
  occupancy-only measurements printed without the readout stamp; at the
  other declared readout they read rank 4 and 10-of-10 / not-lumpable.
- `SCREEN=...S-PASS:1` reads as a positive in the head. The unit's own
  prose says that pass "carries no quantum content whatever" (J/8 is
  column-constant and unistochastic at every n). The qualifier belongs
  in the segment: `S-PASS:1-DEGENERATE-J/8`.
- `KERNEL=...N-INDEXED-AT-OCCUPANCY` rests on **one value of n**: both
  censused cells are n = 4. Constancy across two cells at the same n is
  not n-indexing. And paper-09's measured three-way confound — "ordinal
  position, absolute depth and ensemble identity move together across
  the only two data points" — is a restriction the R6b′ adjudication
  ordered carried; it appears nowhere in paper-12. Restate as
  `CONSTANT-ACROSS-THE-TWO-CENSUSED-CELLS-AT-n=4;
  ORDINAL/DEPTH/ENSEMBLE-CONFOUNDED`.

What the verdict **does** carry honestly: the cap, the grain, the
horizon, the padding, `LEGS=...-AT-DEPTHS-3..10` (so the legs' scope
outside the carrier is disclosed), the no-curvature⇒quantum and
no-indivisibility-at-renewal-grain restrictions, and the naming of the
readout split in the TARGETS segment itself.

### F-10 (MEDIUM, K2) — the pre-registered targets are census statistics, not values of the law, and their provenance says so

Paper-09 §6 reads the targets off S2's leaf counts
`1024/512/512/1024/512` — i.e. off the **uniform measure on legs**. The
pin then pre-registered those rationals as the thing Γ must reproduce.
Nothing in the pinned rows declares a typicality postulate that would
make the uniform measure the law; U1b's own committed formula for a
leaf set is `P(leaf) = Π q_t / G(root,D)` — the weighted one. So the
target values were convention-laden at birth, and the unit has, without
quite saying so, **discovered that the pre-registered targets are not
values of the process's law**. That is a better finding than "targets
hit at one readout", and it should be the headline of §5.1.

### F-11 (MINOR, and a genuine gain) — the readout-invariant residue of the position law was measured and not reported

Recomputed at both readouts, both legs:

| | COUNT | OCCUPANCY |
|---|---|---|
| no-delivery conditional | (1/3,1/3,1/3) | **(1/3,1/3,1/3)** |
| delivery-only conditional | (1/2,0,1/2) | **(1/2,0,1/2)** |
| (p,d,p,r) occurrences | 0 | 0 |
| renewal transfer | one column, all 1/8 | one column, all 1/8 |

**Both sector-conditional laws and the F8 exclusion are
readout-invariant.** The entire readout dependence is one scalar — the
delivery:idle mixing weight, which is 2 then 3 by count and **1/2 at
both legs** by mass (delivery sector mass 1/2, idle sector mass 1, at
renewal 1 and renewal 2 alike). Both readouts obey the *same* law
`((m+1),1,(m+1))/(2m+3)`: m = 2, 3 by count; m = 1/2, 1/2 by mass. This
is the §15-admissible version of the whole §5.1 result and it is
strictly stronger than what the paper claims.

### F-12 (MINOR) — the occupancy readout's answer is horizon-stable; the count readout's is not the ensemble's law either

The unit's occupancy weight on a leg is the raw product Π q, i.e. the
horizon terminated at the leg's end, while the arena table calls
OCCUPANCY "the process's own **horizon-normalized** law". I closed the
gap: extending each leg to U1b's own E2 horizon (the renewal at depth
10; 16 continuations per leg on a 30-leg sample across all five
patterns, total 3584 × 16 = **57,344** = U1b's committed E2 leaf count)
and weighting by the raw 10-event product returns **(3/8, 1/4, 3/8)** —
the same law. So the occupancy answer is stable between the two
horizons the sources declare, and the count answer is the equal-a-priori
convention at either. (U1b's "raw mass 1/8192" for E2 is the
ensemble's *total* mass, not a per-leaf value: the leaves carry two
values in ratio 4:1, which I verified sums to 1/8192.)

### F-13 (MINOR, render) — three quotation defects in the paper

§4 ends mid-quotation: "it is a monotone non-decreasing" — the sentence
and the claim it carries are truncated (the anchor `V-LADDER` binds
exactly that truncated string, so the anchor passes on a fragment).
§5.1 splices the F8 quotation with a stray `**` and no opening marker.
§1's CR-A head `CRA-BLOCKED-AT-STATIC-GEOMETRY-<MISSING=...` is missing
its closing `>`. Quote fidelity is the anchor kind's declared job
(§14, #62); a fragment that ends mid-clause binds bytes, not meaning.

### F-14 (MINOR) — the F8 *mechanism*'s premise is asserted, not gated

`T1-F8-MECHANISM` measures comparability (512/512 after (p,d,p); 0/256
after (p,n,p) — both reproduced here) but the premise that carries the
explanation, "a pair-arbitration needs two incomparable live
proposals", is stated in prose and never gated against the committed
admission rule. The *fact* (0 deliveries in slot 2) is measured and
readout-free; the *cause* is a correlation until that premise is gated.

---

## 2. K2 — adjudication (the decisive head)

**(a) Is either readout motivated by pinned structure?**

**OCCUPANCY: yes, four times over.** (i) It is the unique measure for
which Γ(cut'←cut) is a disintegration of one object across cuts — the
flow identity `w(h)k_r(e|h) = w(h+e)`, exact at 3968/3968, is what makes
the class law "the exact conditional" and what makes all 544 columns sum
to 1. (ii) It is the arena table's declared PRIMARY. (iii) It is the
only readout under which the pin's mandatory negative control (REC
flat) survives — and under which REC is exactly lumpable. (iv) It is
the readout under which the unit's positive answer to CR-B exists.

**COUNT: motivated only by the target's own provenance.** It is the
measure S2/paper-09 used to *define* the target values (leaf counting).
That is a real motivation and it is not the RSQ "arbitrary relabelling"
pattern — but it is provenance-motivation, not law-motivation, and it
makes the test near-tautological: reproducing a leaf census by
re-running the leaf census tests the enumeration, not Γ. Multiplicity
counting is a declared feature of **no** pinned dynamical row; the one
pinned row that states a measure on a leaf set (U1b's
`P(leaf) = Π q_t / G(root,D)`) states the weighted one.

**(b) The honest head.** `TARGETS-HIT` is readout-selected, and the
selection is by the property under test. The honest head is:

> `TARGETS=MISSED-AT-THE-DECLARED-PRIMARY-READOUT-(3/8,1/4,3/8)-AT-BOTH-LEGS-AND-AT-BOTH-DECLARED-HORIZONS |
> REPRODUCED-ONLY-AT-THE-COUNTING-MEASURE-THAT-DEFINED-THEM |
> THE-TARGETS-ARE-CENSUS-STATISTICS-NOT-VALUES-OF-THE-LAW |
> READOUT-INVARIANT-RESIDUE=(1/3,1/3,1/3)-NO-DELIVERY-AND-(1/2,0,1/2)-DELIVERY-ONLY-AND-THE-F8-EXCLUSION`

and the settlement's second conjunct is then **False**, not True. It
does not "split": a conjunction must be evaluated at one arena, and at
the declared arena it fails. (If a future pin declares COUNT primary,
the *first* conjunct fails instead — see F-3 — so no declaration makes
both true.)

**(c) Which is the physical reading, and what would decide it?**

**The occupancy law is the process's own measure; the count law is a
typicality convention with no pinned warrant.** Decisive evidence, all
measured here: it is the only one that is a disintegration of a single
measure (so only it can be called "the law at two cuts at once"); it is
horizon-stable across both declared horizons (F-12); and adopting the
alternative makes the *record* quotient curved and non-lumpable
(F-2) — i.e. the count readout manufactures curvature at the carrier
D74 proved flat, which is the signature of an observer artefact, not of
a process.

What would decide it beyond this: **a pinned typicality postulate.**
If any pinned row declares equal a priori weight on histories at a
declared grain, the count readout becomes the law at that grain and the
targets become law-values; absent one, they are counts. That is a
single, answerable question for the corpus, and it is the right form of
"what would decide it" — not a deeper cap, not more legs.

---

## 3. K3 — adjudication (the holonomy deviation)

1. **Cause, corrected.** The k-enlargement `{5,13}` is **not** caused by
   the readout. The k-connection is defined at history level and is
   readout-free; the enlargement is caused by the *required* horizon
   normalisation acting on a *non-descending* potential, and it is an
   identity, not a census (F-4). The Γ-family's rank-7 group **is**
   readout-caused (rank 4 at the other readout) and its printed row is
   missing that stamp (F-9). The protocol's framing ("the enlargement is
   caused by the declared readout on a non-descending potential") is
   therefore half right and the halves belong to different readings.
2. **Well-posedness ruling.** "Holonomy consistent", read as equality of
   groups, is **ILL-POSED at a carrier where the potential does not
   descend**: unsatisfiable by any column-stochastic construction from
   the pinned law (F-4). Read as equality for the *aggregated family*,
   it is a category error at any carrier (F-4, F-5). The pin's §3.2 gate
   was well posed; the §4 settlement clause was not, and the fault is
   the effectus's, not the unit's.
3. **What the third conjunct should have demanded:**
   `HOLONOMY=REPRODUCED-AND-LOCATED` — (i) the connection reproduces
   D74's rung on the carrier digit for digit; (ii) every derived
   reading's deviation is exactly attributed to a named measured cause,
   **gated by the identity `r_k = r_q · G(hAB,r−2)/G(hBA,r−2)`**
   (1546/1546) so that the deviation is derived rather than observed;
   (iii) REC flat at all readings at the declared readout. At that
   conjunct this unit **passes**.
4. **The successor question, answered by measurement:** the lattice
   between MENU and REC **does** contain a carrier with both descent and
   holonomy, it is **derivable from the pinned artefacts** (MENU refined
   by the potential the construction uses), it is 181 classes, and on it
   the k-connection carries exactly ⟨2,3⟩ with the 44-obstruction
   intact (F-5). The Γ-family reading still deviates there — which is
   the measurement that proves the family reading is the wrong object
   for this conjunct.

---

## 4. K4 — the quantum-shape claims: at what strength may the paper speak?

- **Non-Markovianity:** citable at cut grain, at the declared readout:
  the class chain fails CK at **4 of 10** depth-cut triples, at 34, 112,
  12 and 12 cells (reproduced); REC is exactly lumpable (0 of 10). Both
  statements are occupancy-relative and must be stamped (10/10 and
  10/10 at the other readout).
- **eq. 22:** citable only as *no interpolant of eq. 22's form exists
  under the identity padding* — the unique candidate carries negative
  entries at all four triples (36/104/108/164, reproduced), and the
  alternative paddings make the reading silent rather than contrary
  (F-8). It is **not** a divisibility claim about the process, and the
  paper says so.
- **The U3 screen:** the census is 5 N/A-SHAPE, 4 S-FAIL-DS, 1 S-PASS,
  and the single pass is J/8 — column-constant, doubly stochastic only
  because its column is uniform, unistochastic at every n. **The one
  pass is the known degenerate and carries zero quantum content**; the
  n=3 discriminant cell is empty by shape. So the positive half of the
  Barandes correspondence is **empty at every object this unit built**.
- **The 44 squares:** the dichotomy reproduces (44 + 44; base depths
  {1:4, 2:40}); Γ is non-unit on all 44 that close (spectrum
  {1/4:2, 1/3:8, 8/13:2, 13/8:6, 3:24, 4:2} reproduced exactly) and has
  no loop at all on the other 44 (0 of 44 share a carrier class). The
  *qualitative* half is readout-stable (non-unit at 44/44 under both
  readouts); the spectrum is not.

**Ruling:** the paper may claim `NON-MARKOVIAN-AT-DEPTH-CUT-GRAIN-AT-THE-
DECLARED-READOUT` and `NO-EQ-22-FORM-INTERPOLANT-AT-THE-IDENTITY-
PADDING`, and it may claim nothing whatever with the word
"indivisibility-shaped" in it: Barandes' notion is a conjunction of a
non-divisible stochastic process **with** a unistochastic/Born half, and
the unistochastic half measured here is empty apart from the degenerate.
U2's W-CROSS independently forbids the curvature⇒quantum bridge, and the
unit's claim count of zero is correct and should stay zero. The unit's
§8 discipline is, on this axis, exactly right — the only repair is to
stamp the readout on the two survivors.

---

## 5. K5 — do the verdict segments carry every measured restriction?

**No — five omissions, listed with their repairs in F-9**, plus the
settlement's own mis-scoping (F-1) and the unstamped `N-INDEXED`
inference from a single n. The segments that *do* carry their
restrictions are the scope segment (cap, grain, horizon, padding, the
depths 3…10 of the leg ensembles, the two no-claim disciplines) and the
TARGETS segment, which names the readout split rather than hiding it —
the unit deserves credit for the latter; the defect is that having
named it, the settlement then scores it True.

---

## 6. THE SETTLEMENT RE-EVALUATION

Evaluated at the unit's own declared primary arena (readout =
OCCUPANCY, carrier = MENU-113 at (A,B) d≤4, horizon H4, depth cuts):

| link | as reported | **as adjudicated** |
|---|---|---|
| constructed | True | **TRUE** — 544/544 columns exact, dims [1,5,13,45,113], flow identity 3968/3968, provenance 23 shas |
| targets hit | True (at COUNT) | **FALSE** — the law returns (3/8,1/4,3/8) at both legs and both declared horizons; the targets are the counting measure's values, reproduced by re-running the census that defined them (F-1, F-2, F-10) |
| holonomy consistent | False | **ILL-POSED as written** — unsatisfiable by any column-stochastic construction on a non-descending carrier, and a category error for the aggregated family. Under the well-posed replacement (REPRODUCED-AND-LOCATED): **TRUE** (F-4) |
| motivation non-empty | True | **TRUE as computed, but the predicate measures the wrong quantity**; per-segment: motivated for carrier/holonomy, free-choice-carried for targets (F-7) |

**The honest settlement statement:**

> `SETTLEMENT=PARTIAL-FAILED-LINK-TARGETS-HIT-AT-THE-DECLARED-PRIMARY-READOUT
> <HOLONOMY-CONJUNCT-WITHDRAWN-AS-ILL-POSED-AT-A-NON-DESCENDING-CARRIER;
> REPLACED-BY-HOLONOMY=REPRODUCED-AND-LOCATED-WHICH-THIS-UNIT-MEETS;
> THE-TARGETS-ARE-CENSUS-STATISTICS-NOT-VALUES-OF-THE-LAW;
> NO-SINGLE-READOUT-SATISFIES-CONSTRUCTED-AND-TARGETS-HIT-TOGETHER>`

So the result stands as PARTIAL — **but the paper names the wrong
failed link.** The holonomy link is the one this unit actually earned
(it reproduced D74's rung digit for digit and located every deviation
in a measured cause with an exact identity); the targets link is the
one that fails, and it fails for a reason more interesting than a
miss: the pre-registered targets were never values of the law.

And the structural result the campaign should carry forward: **the
settlement condition as posed cannot be met by any construction of this
family** — conjunct 1 requires the weighted readout and conjunct 2
requires the counting one. Whether some *other* horizon convention
makes the law's own value 3/7 is open, and is the one substantive
escape route (F-12 closes the two horizons the sources declare).

---

## 7. THE NEXT-ITERATION RECOMMENDATION (posed precisely)

The next Γ pin must fix, in this order:

1. **One readout, chosen by a criterion declared before the battery and
   independent of any target.** The criterion I recommend, because it is
   a one-gate check and it selects uniquely: *the readout under which Γ
   is a disintegration of a single measure across cuts* (the flow
   identity). It selects OCCUPANCY. The other readout runs as a control
   whose declared job is to show the battery can move — and it does:
   REC gains a rank-4 holonomy and fails CK at 10 of 10.
2. **Re-pose the targets as values of the law.** Pre-register
   **(3/8, 1/4, 3/8) at both legs** and demote (3/7,1/7,3/7)/(4/9,1/9,4/9)
   to the **declared census shadow** — exactly the status the R6b′
   register gives the delivery-free shadow ("a control, never a
   target"). If the corpus wants the counting values back as targets it
   must first pin a typicality postulate; that is a separate, nameable
   decision and it should be taken in the open.
3. **Carry the arena over the carrier: build on MENU+G (181 classes).**
   It is derivable, it is in the declared lattice, the potential
   descends at every horizon, the connection carries exactly D74's
   ⟨2,3⟩, the 44+44 dichotomy survives, Γ stays exactly
   column-stochastic, and non-Markovianity survives at 2 of 10 triples.
   Then the holonomy conjunct is met *on the connection*, and the
   remaining Γ-family deviation (rank 4) is reported as what it is: the
   curvature of a coarse-grained law, a different object.
4. **Re-pose the third conjunct** as `REPRODUCED-AND-LOCATED` with the
   identity `r_k = r_q · G(hAB,r−2)/G(hBA,r−2)` as a must-pass gate
   (falsifier: perturb one potential value), and drop the aggregated
   family from the consistency demand.
5. **Rebuild T2-HOLONOMY as a gate that can fail**, and re-audit the
   never-falsified census for coverage-by-declaration (a gate is covered
   only when a mutant flips *its own* predicate).
6. **Decide the [B3] existence question with the exact feasibility LP.**
   It is row-decomposable — at the (1,2,3) triple it is 45 independent
   13-variable non-negative feasibility problems plus one column-sum
   coupling — so the scope-out is not forced by cost, and the LP is the
   only convention-free route (F-8 shows the padded-algebra route speaks
   at exactly one padding).
7. **Carry the R6b′ inheritance in full:** paper-09's three-way confound
   (ordinal position / absolute depth / ensemble identity move together
   across the only two cells) must stamp every leg-indexed claim, and
   `N-INDEXED` must not be inferred from a single value of n.
8. **Evaluate the settlement at one arena**, with each conjunct either
   gated as arena-invariant (§15) or stamped arena-relative in the head.

---

## 8. Recomputation ledger (113, zero divergences)

Layer + carrier (10): per-level census [1,8,60,452,3448,26760];
cumulative [1,9,69,521,3969,30729]; carrier 3969; MENU 113; REC 2477;
G(root,1..5) = 2, 4, 257/32, 1035/64, 4173/128; MENU dims [1,5,13,45,113];
REC dims [1,8,51,324,2093]; cut masses 1 at all five cuts; Σq(·|root) = 2.
Squares + holonomy (30): census {closed 1546, AB-only 28, BA-only 12,
both-blocked 142}; r_q spectrum {1/2:70, 2/3:2, 3/2:6, 2:10}; r_k
spectrum incl. 64/65 ×6 and 65/64 ×2; 88 defective; MENU/q 1402 closes,
44 self-loops, cycle rank 134, obstruction 44, ⟨2,3⟩ rank 2; MENU/k 52
self-loops, [2,3,5,13] rank 3; Γ-occ [2,3,5,13,19,97,389] rank 7,
416/1402 non-unit, 27 distinct values; 144 non-closing; REC flat at q, k
and Γ (473/473 unit); 90/90 and 454/454 columns exact; the descent
identity 1546/1546; 8 non-unit G-ratio squares, all at depth 0, all
closing; G(·,2) multi-valued on 4/13; endpoint classes ⊆ that set;
literal count-Γ 0/544 stochastic; repaired count-Γ 544/544; count-Γ MENU
[2,3,5,7] rank 4; count-Γ REC 296/473 non-unit rank 4.
Legs (19): 16 bases all (p,p,r); 152,672 raw continuations; 3584 legs;
five patterns 1024/512/512/1024/512; (3/7,1/7,3/7); (3/8,1/4,3/8); 256
R2 bases; 73,728 legs; (4/9,1/9,4/9); (3/8,1/4,3/8) at leg 2; sector
masses 1/2 and 1 at both legs; count multiplicities 2 and 3; mass
multiplicity 1/2 at both; slot×kind at both legs; the no-delivery
conditional at both readouts; the delivery-only conditional at both
readouts; ((m+1),1,(m+1))/(2m+3) at four (readout, leg) pairs.
Horizon (7): base masses 1/512 ×16; leg masses {1/4096:2048, 1/1024:1536};
mass by pattern; 16 E2 continuations per leg (30 sampled, all five
patterns); two leaf-mass values; implied E2 total 57,344 = U1b's
committed count; the ensemble-horizon law (3/8,1/4,3/8).
CK + 44 (9): MENU/occ 4 of 10 at 34/112/12/12; MENU/count 10 of 10;
REC/occ 0 of 10; REC/count 10 of 10; 44+44; base depths {1:4, 2:40};
the 44-spectrum at occupancy; at count; 0 of 44 descent-obstruction
squares share a class.
eq. 22 (8): 36 / 104 / 108 / 164 negatives at the four triples;
invertibility under the identity padding at all four; column sums
exactly 1 at all four; reset padding singular at all four; uniform
padding singular at all four.
Structure (9): flow identity 3968/3968; R-SIG 5161; R-MENU 1365; blocks
{(1,1):1365, (2,2):3788, (2,3):4, (3,2):4}; (p,d,p) comparable 512/512;
(p,n,p) 0/256; renewal transfer 8×8 one column all 1/8 at count and at
occupancy; (p,d,p,r) occurrences 0.
Successor carrier (12): 181 classes; dims [1,5,17,45,113]; REC refines
it; it refines MENU; G-descent at all five horizons; q-reading 1394
closes / obstruction 44 / ⟨2,3⟩ rank 2; k-reading identical to q;
Γ-family [2,3,13,19] rank 4; column-stochastic 0 violations; CK 2 of 10;
44+44 preserved.
Instrument (9): the six delivery/pin/protocol hashes verified before and
after all work; the layer blob `576275d55ecf`; T2-HOLONOMY's predicate
shown analytically forced; T2_VERDICT on REC under the unit's own
predicate = DEVIATE-AT-BOTH, not the AGREE its gate statement claims.

Section totals: 10 + 30 + 19 + 7 + 9 + 8 + 9 + 12 + 9 = **113**.

---

## 9. Grade

**ACCEPT-WITH-FIXES — fixes BLOCKING.**

The construction is real and every number in it survived an independent
rebuild: 113 recomputations, zero numerical divergences, no false
theorem, and a prose discipline that names its own weakest point (the
readout selection, the group's non-discriminating status at the
q-reading, the padding convention, the zero curvature⇒quantum claims,
the CR-B inversion) more candidly than most units in this corpus. What
fails is the last step: a settlement conjunction assembled from
conjuncts true at different arena coordinates, with the wrong link
named as failed, resting on a must-pass gate that cannot fail.

Blocking fixes: F-1 (evaluate at one arena; conjunct 2 False at the
primary), F-2 (run and print the count-readout control), F-3 (build the
class-level count readout or withdraw the fiber-2 claim to the leg
level where it was measured), F-4 (withdraw/replace the holonomy
conjunct; gate the deviation identity), F-5 (print MENU+G and reclassify
I-CARRIER), F-6 (rebuild T2-HOLONOMY; strike the false control claim),
F-9 (compute the literal segments; stamp the readout), F-10 (restate
§5.1's headline). Non-blocking: F-7, F-8, F-11, F-12, F-13, F-14.
