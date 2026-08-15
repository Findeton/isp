# EPR (paper-38) — OPERATOR REVIEW (K1 seat)

**GRADE: AWF — ACCEPT WITH FIXES.**

Every number this seat was ordered to rebuild reproduces **exactly** from an
instrument written from scratch on different primitives, with no code, no
input file and no typed literal shared with `v14/code/epr_exact.py`. **Zero
false computed numbers.** The head word `EPR-CRITERION-INAPPLICABLE-AT-THE-
PAIR-LOCALIZED-BLOCK-QUANTITY` stands, and it is invariant under the one
declared axis (the state) that could have moved it. Five majors follow, and
none of them moves a number: all five are about what the measured numbers are
allowed to be said to establish. Two of the five come with strengthenings
this seat can license — one of which upgrades a 64-state sweep to a theorem.

**Between delivery and adjudication every reading here is a candidate
reading, this review's included.**

**Objects verified at open and at close (sha256-12):**
`v14/paper-38-epr.md` 550e3c8fff93 · `v14/code/epr_exact.py` 9ed817d9649d ·
`v14/code/epr_output.txt` 1b30c6761281 · `v14/code/epr_receipt.json`
a51326de11a8 · `v14/note-epr-pin.md` b1e4cf9a8b9f. Source of record
`v14/sources/epr-1935-physrev-47-777.pdf` 66b5deb150c4, **read in the
original** (image-only PDF; no text layer; read page by page).

**Independent recomputations: 145.** Scratch:
`.../scratchpad/epr_k1/` (`k1_rebuild.py`, `k1_census.py`, `k1_e4.py`,
`k1_stage3.py`, `k1_probe.py`). Repo writes: this file only; git read-only.

---

## 1. What the rebuild reproduced

Primitives deliberately different: sites are `Z_3^2` pairs, cells are
`(direction index, tail site)` keys, groupings are frozensets of frozensets,
the record is measured as a **27-cell field** and collapsed to a triple only
after site-constancy is measured, and the corpus is assembled from
paper-21's window description rather than from FAC's receipt.

**The arena and the theorem.** 9 sites; 27 cells in bijection with 27
unordered co-division pairs; two actors per cell; six cells per actor;
72 of 72 ordered site pairs agree that **UNLINKED ⟺ common line of the one
undeclared parallel class**; degrees all 6; three parts. The link graph is
complete multipartite, as claimed.

**The 512-lattice.** 490 own a record quantity; 19 have a nonempty far
region; **0 both**; the nineteen are exactly `{∅ ×1, singletons ×9, unlinked
pairs ×9}`. The theorem behind it verifies as stated: if `S` has a nonempty
far region, `S ∪ {y}` lies in one line of the undeclared class, and such a
line contains no linked pair, hence no cell.

**The corpus, rebuilt not cited.** 280 groupings (enumeration and the closed
form `9!/(3!^3·3!)` agree); 36 saturating; `36^4 = 1,679,616`; **72**
I7-STRICT triples in **12** multisets; **276** G-FLAT quadruples of which
**12** are already class quadruples; W4-CLASS `4^4 = 256` with **35** distinct
records; 5,856 histories; **site-constant at 5,856 of 5,856**; **36** distinct
records.

*Cross-validation worth recording:* the corpus's seed-fan stratum is 80
histories whose record my rebuild could not read off any committed paper. I
solved for it: site-constancy forces the repeated grouping to be a declared
parallel class, and only **the third declared direction (1,1)** reproduces the
delivered E4 fibre `{3: 594, 4: 8,514, 5: 96,300}`; the other two give
`{3: 594, 4: 7,074, 5: 97,740}`. An undisclosed corpus datum was therefore
**recovered from the delivered numbers and then confirmed to be consistent
with every other arm**. This is strong evidence the corpus is what the paper
says it is.

**The block census.** 421,656 ordered block pairs = `5,852×72 + 4×78`;
105,408 link-disjoint = `5,856×18`, all of them singleton pairs; 18
quantity-bearing at LOC-PAIR (the three declared-class-repeating schedules,
6 ordered pairs each); **0 both**; 105,408 premise instances at LOC-WALK.

**The four arms** reproduce cell for cell, including the two columns the
paper does not print (shadow-self-certified, and without-a-record-
counterpart):

| localization | separation | pairs | quantities | certified | shadow-certified | no record ctpt | no shadow ctpt |
|---|---|---|---|---|---|---|---|
| LOC-PAIR | SEP-LINK-DISJOINT | 0 | 0 | 0 | 0 | 0 | 0 |
| LOC-PAIR | SEP-ACTOR-DISJOINT | 18 | 54 | 54 | 0 | 0 | 54 |
| LOC-WALK | SEP-LINK-DISJOINT | 105,408 | 316,224 | 316,224 | 0 | 0 | 316,224 |
| LOC-WALK | SEP-ACTOR-DISJOINT | 421,656 | 1,265,112 | 1,265,112 | 0 | 0 | 1,265,112 |

**The shadow's ceiling.** 36 records → **9** residue classes (mod the global
site phase); **0** of the 64 declared states separates two records of one
class; sweep maximum **4**; PSI-FLAT attains it.

**The readings.** 36/1, 4/12, 1/36, 23/4, 3/13; 25 ordered pairs; **3** not
jointly declarable — `BORN-GD|RECORD-MENU`, `BORN-GD|CURVATURE`,
`RECORD-MENU|CURVATURE`; READ-RECORD refines all five; Born-carries-record-
menu **0 of 36**, converse **24 of 36**. Section 7's two existence claims are
witnessed: 137 pairs share a Born menu with different record menus (e.g.
`(0,0,0)`/`(0,0,3)`), 9 pairs share a record menu with different Born menus
(e.g. `(0,0,1)`/`(0,0,3)`).

**E3, E4, E5, the dynamical census, the measure leg, three controls.**
`G·D ≠ D·G` at **30 of 36**; record carries both members at 5,856 of 5,856.
E4 fibres `{4: 18}`, `{3: 594, 4: 8,514, 5: 96,300}`,
`{3: 2,382, 4: 34,062, 5: 385,212}`. E5 `105,408 / 0 / 0 / 105,408`.
Event shapes **84**, confined **24**, cell probes **54**, disturbances **0**,
unconfined that do reach **342**. Measure leg **1,080/1,080**, with the
polarity genuinely two-sided (298 certain probe cells against 242 not).
Controls: punctured record **105,228** (the surviving two directions pin the
third at 10 histories, ×18 pairs), one-declared-direction arena **35,136 /
105,408**. FAC's cited receipt is `240bad74217a` at commit `f4172ea` and its
working-tree copy has indeed drifted (`c7135ba5884c`) — the abstention the
paper claims is real.

**The six E-anchors, against the print.** E1 (p.777), E2 (p.777), E3
(p.778), E5 (p.780), E6 (p.780) are **verbatim**. E4 (p.779) is verbatim up
to a silent truncation — see MINOR-5.

---

## 2. MAJORS

### MAJOR-1 — `RECORD-COMPLETE` is analytic, not measured, and it is half the head word.

**Establishing measurement.** In `pair_specs` the quantity list and the
block's own direction set are built from the *same* localization call:
`qs = tuple(sorted(k % 3 for k in locf(B)))` and
`db = tuple(sorted({k % 3 for k in locf(B)}))`. Hence `d ∈ db` for every
quantity of every pair of every arm, so `epr_counterpart_at(d, FR[(db, r)])`
is true identically. My rebuild returns *without a counterpart in D-RECORD =
0* on all four arms and **cannot return anything else on any arena**: the
column is forced by the construction of the localization, not by the corpus.
Only `CTRL-D-RECORD-SYNTH-PUNCTURED`, which deletes a direction from the
description by hand, can move it.

The pin knew this ("D-RECORD trivially contains every record-defined value").
The paper does not say it. §5 presents the zero as a census result ("The
record's own counterpart count is the complement: no certified element lacks
a record counterpart, on any arm"), and the head word carries
`RECORD-COMPLETE` beside the contentful `SHADOW-INCOMPLETE`.

**Licensed replacement (§5, after "…on any arm."):**
> The record's own counterpart count is the complement, and it is analytic
> rather than measured: a quantity of a block is by construction a record
> entry the block's own localization carries, so D-RECORD's content at the
> block contains the value being predicted at every arm, at every history,
> and on any arena whatever. The census can only put this zero at risk
> through the punctured control of section 10, where it duly moves to
> 105,228. `RECORD-COMPLETE` is therefore a statement about what the record
> is, not a finding about this corpus; the contentful half of the head word
> is `SHADOW-INCOMPLETE`.

### MAJOR-2 — the shadow-incompleteness census carries no information beyond the §4 ceiling, and EPR's own argument form does not run against the description under test.

**Establishing measurement.** (i) *No per-probe structure*: on every arm the
"without a counterpart in D-SHADOW" column **equals** the certified column
exactly — 54/54, 316,224/316,224, 1,265,112/1,265,112 — so the census
distinguishes no probe from any other; 316,224 is `105,408 × 3` and nothing
more. (ii) *What actually does the work*: the whole column reduces to a fact
about the reading's fibres, which I measured directly — **0 of the 9 residue
classes of this corpus is a single record, and 0 of the 9 has a direction
constant across it** (class sizes 6,6,2,6,2,3,2,3,6). (iii) *EPR's own form
is empty here*: `D-SHADOW` certifies **0** elements on all four arms, so the
argument EPR actually run — certify with the description under test, then ask
that description for the counterpart — has no elements to run on. The
contentful arm certifies with the *finer* description and asks the *coarser*
one for a counterpart, which is coarse-graining, not EPR's dilemma.

The paper does disclose (iii) in one sentence of §5 and does not carry it into
the head or into §7's "That is EPR's conclusion reached inside a committed
theory".

**Licensed replacement (§5, replacing the paragraph beginning "And the shadow
certifies nothing of its own"):**
> Two things about the shadow's zero belong in the open. The shadow
> certifies 0 elements at every arm, so EPR's argument in its own form — the
> description under test certifies an element and is then asked to carry it —
> has nothing to run on here; the reading measured above is the
> cross-description one, elements certified by the theory's own state and
> asked for a counterpart in the candidate description. And that
> cross-description column is uniform: it equals the certified column at
> every arm, because the shadow's fibres are the residue classes and no
> residue class of this corpus is a single record or is constant in any
> direction. `316,224` is `105,408 × 3`; the content is section 4's ceiling,
> counted once per block pair.

### MAJOR-3 — "not at a strawman" is not sustained at the parent's own alphabet: the declared state family has 4 letters where paper-20 declares 37, and the shadow's true best case is the ceiling, 9 menus, not 4.

**Establishing measurement.** I swept the state space over paper-20's own
discriminating alphabet — the 37 elements of `(1/3)Z[ω]` of modulus at most 1,
the ring the walk's phases and the coin's entries both live in, `37^3 =
50,653` states. Distinct-menu distribution: `{1: 109, 2: 1,296, 3: 2,592,
4: 324, 5: 6,156, 8: 5,184, 9: 34,992}`. **The maximum is 9 — the ceiling
itself — attained at 34,992 states**, e.g. `ψ = ((-3,-3), (-3,-3), (-3,-2))/3`.
The declared family `{0, 1, ω, ω²}^3` caps at 4. So the audited "best case"
resolves the record 2.25× more coarsely than the arena's own alphabet
permits, and §4's "The audit is run at that best state, not at a strawman"
asserts what the parent's alphabet contradicts.

**The verdict survives, and this seat can strengthen it into a theorem.**
Every Born-menu partition, at every state whatever, is a coarsening of the
residue-class partition (equal residue vectors give the same `D`; a global
shift multiplies every post-coin amplitude by a common phase, which the
modulus cannot see). The residue partition itself carries nothing: no class
is a singleton and no class is constant in any direction. Therefore the
shadow carries **0** of the certified elements **at every state, by theorem** —
not at 64 sampled ones. I confirmed this computationally as well: carried = 0
at all 64 declared states, and at all 46,656 states of the 37-alphabet whose
menu count is at least 4.

**Licensed replacement (§4, replacing "Second, the audit is given the
shadow's best case…" and the sentence "The audit is run at that best state,
not at a strawman." in "The short of it"):**
> Second, the audit does not depend on which state is declared. Every
> Born-menu partition, at every state whatever, coarsens the residue-class
> partition, because equal residues give the same D and a global shift of the
> residues multiplies all three post-coin amplitudes by one phase that the
> modulus cannot see. And the residue partition already carries nothing: `no
> residue class of this corpus is a single record, and none is constant in
> any direction`. So the shadow carries none of the certified elements at
> every state, by theorem, and the state family below is a check on the
> theorem rather than the ground of the result. Within the declared family
> `{0, 1, ω, ω²}^3` the best state separates 4 menus and the primary state
> attains it; over paper-20's own 37-value alphabet the best state attains the
> ceiling of 9, and carries 0 there too.

### MAJOR-4 — E3's operator leg does not instantiate EPR's antecedent; it measures the residue degeneracy of the phase encoding.

**Establishing measurement.** `G·D(x) = D(x)·G` holds **exactly when the
three counts are equal modulo three** (agreement with that criterion: 36 of
36). The six agreeing records are `(0,0,0), (0,0,3), (0,3,0), (1,1,1),
(2,2,2), (3,0,0)`. At **three of the six** — `(3,0,0)`, `(0,3,0)`, `(0,0,3)` —
the record observable `diag(n)` is **not** scalar, so the two quantities' own
operators do *not* commute there, while the leg reports agreement. The leg is
therefore blind to exactly the thing EPR's horn (2) is about: it tracks
`ω^{n}`, i.e. `n mod 3`, not the observables. Further, `G·D` and `D·G` are
paper-20's two declared **coin orders** — a declaration fibre, two candidate
unitaries — not the operators of two physical quantities; no operator for the
Born menu or for the record menu is exhibited anywhere in the unit. The
content of E3 here is carried entirely by the reading-level leg (3 pairs
where neither partition refines the other), which is a legitimate finite-arena
rendering of "cannot have simultaneous reality".

**Licensed replacement (§7, replacing "At the operator level, … compared
exactly in Z[w].") :**
> One half of the antecedent is available in the corpus's own terms and one is
> not. At the reading level, the five declared readings are measured as
> partitions and three pairs admit no common refinement — that is this
> arena's rendering of two quantities that cannot be declared together, and
> it carries the argument below. At the operator level the unit exhibits no
> operator for either member of the pair; what it can measure is paper-20's
> declared coin-order fibre, `the two declared coin orders differ at 30 of the
> 36 committed records`, and that number tracks `n mod 3` rather than the
> record: the two orders agree exactly when the three counts are equal modulo
> three, which at `(3,0,0)`, `(0,3,0)` and `(0,0,3)` happens while the record
> observable is not degenerate at all. The 30 is a disclosure about the
> encoding, not an instance of EPR's antecedent.

### MAJOR-5 — E5's zero is forced by the formalisation of "reading"; the falsifier tests the instrument, not the arena.

**Establishing measurement.** `record_at_B_under(rd, row, qs)` returns
`tuple(row[d] for d in qs)` and `shadow_at_B_under(rd, row)` returns
`shadow_menu(row, PSI_PRIMARY)`; neither consults `rd` outside the mutant
branch. In the formalism a "reading declared at A" is a function on records,
not an operation on histories, so **no path from A's declaration to B's record
exists to be measured**. My rebuild returns 0/0/105,408 and would do so on
any arena, any corpus, any separation. `MUT-E5-LEAK` demonstrates that the
instrument's plumbing is clean; it cannot demonstrate that the arena is.

The paper's §8 says "The zero is a measurement, not a blind spot" and reads it
as SEC's seam-confinement seen from the other side. Neither is sustained: SEC's
ruling would be tested by an *operation* on A, and there is none in this unit.

**Licensed replacement (§8, replacing the paragraph beginning "The
test-declaration duty is discharged rather than promised."):**
> What the zero is, exactly. A reading in this unit is a function on records,
> not an operation on a history, so nothing declared at A has a path to
> anything B holds; the zero is forced by that formalisation and would be
> returned on any arena. The falsifier `MUT-E5-LEAK` routes the reading's own
> index into B's record and into B's shadow and dies at this gate, which
> establishes that the instrument carries no such path by accident — it does
> not establish that the arena forbids one. Testing SEC's ruling in EPR's own
> sense would require an operation on A that the corpus's dynamics admits,
> and this unit declares none; that is the honest scope of the row, and the
> successor obligation.

---

## 3. MINORS

**MINOR-1 — the E4 assignment is a per-quantity marginal box, and the
published distribution is definition-relative.** `assigned_description`
returns `tuple(tuple(sorted({z[d] for z in fibre})) for d in qs)` — the
product of the marginals, which discards correlations between B's three
quantities. Under the equally natural joint reading (the set of value-tuples
the fibre admits) I measure the walk/link arm as `{4: 7,146, 5: 98,262}` with
**no 3s at all**, against the published `{3: 594, 4: 8,514, 5: 96,300}`. The
head value 5 is robust under both, and the marginal reading is the
conservative one, so nothing is inflated. *Repair:* one clause in §6 — "the
set of values each of its quantities can still take, taken quantity by
quantity" — and a receipt field naming the joint reading as the declared
alternative.

**MINOR-2 — `E4-ASSIGNMENTS-AT-ONE-RECORD=5` carries no state stamp and is
state-relative.** Over the 64 declared states the per-state maximum is 5 at
**54** states and 4 at **10**. PSI-FLAT is among the 54, so the head is
correct at the declared primary — but the verdict string stamps the arena,
the histories and the separation, and not the state. *Repair:* add
`STATE=PSI-FLAT` to segment 3, or `E4-ASSIGNMENTS-AT-ONE-RECORD=5-AT-THE-
DECLARED-PRIMARY-STATE`.

**MINOR-3 — §11's "the subset lattice is the only complete one" is not
sustained.** The dynamical no-disturbance census runs over **every event
shape the arena admits**, `C(9,3) = 84`, which is exhaustive; it is not among
the six declared windows at all. And `W-BLOCKS = 6` is itself complete, by
FAC's closed form over the complete 21,147-partition lattice. *Repair:*
declare a seventh window `W-EVENT-SHAPES` bound 84 marked complete, and
rewrite the sentence as "three of the seven windows are complete — the subset
lattice, the event shapes and the block lattice; the corpus, the states, the
readings and the measures are declared bounds."

**MINOR-4 — at LOC-PAIR the zero is carried by the grain at 421,638 of the
421,656 ordered pairs, and by the theorem at 18.** Only 18 pairs ever reach
the separation test; the other 421,638 fail because the block is a single
actor (or an undeclared-class line) and a record quantity is a two-actor
object. The theorem's *general* form is carried by the complete 512-lattice,
where it is not grain-limited, and §3 should say so rather than let the block
count appear to carry it. *Repair:* in §3, after the block-pair sentence —
"of those 421,656 pairs only 18 reach the separation test at all, the rest
failing because a block of one actor cannot own a quantity of two; the
general statement is the lattice's, where every quantity-bearing region in
the arena is tested."

**MINOR-5 — E4 quotation hygiene.** EPR's sentence (p.779) is "Thus, it is
possible to assign two different wave functions (in our example ψ_k and φ_r)
to the same reality (the second system after the interaction with the
first)." §6 ends the quotation at "to the same reality." with a full stop and
no ellipsis, silently dropping the clause that identifies which reality is
meant — the one clause that most directly licenses this unit's own reading of
the separated block. The subscripted Greek is also transliterated to
`psi_k`/`phi_r` inside quotation marks. *Repair:* restore the parenthetical
(it strengthens §6) and mark the transliteration once.

**MINOR-6 — "FAC's forced per-history decomposition" (§3) overstates FAC.**
FAC's own verdict is unique at 5,852 of 5,856; this unit's own census runs
over two decompositions at four histories and needs them (they supply the 18
quantity-bearing pairs the head is about). *Repair:* "FAC's per-history
decomposition inventory — forced at 5,852 of 5,856 histories, two-membered at
the other four".

---

## 4. What this seat could not fault

- The head word, and its two-armed verdict string. The head is at
  LOC-PAIR × SEP-LINK-DISJOINT and is **state-invariant** (that arm is empty
  before any state is declared). The second word is state-invariant too, now
  by theorem (MAJOR-3).
- The complete-multipartite theorem and its one-line proof: exact as stated,
  72/72, and the lattice consequence 490/19/0 is complete and correct.
- §9's finding — that where the criterion is instantiable, the certified
  quantity's referent straddles the block's boundary. I checked the harder
  half: the straddling partner `x+l` is linked to `x`, hence lies in neither
  the block nor any admissible conditioning region.
- The Bell wall. No sentence of the paper claims restored locality, an evaded
  Bell theorem or a vindicated hidden-variable completion; the two
  constrained rows are the two that carry joint value assignments.
- The FAC/SEC candidate-under-repair handling: the cited receipt digest is
  right, the drift is real, and every consumed value is independently
  re-derivable — my rebuild derived the block inventory from FAC's two binding
  legs without reading FAC at all, and got the same 421,656.

---

## 5. Repair order, smallest first

1. §6 clause (MINOR-1), §3 clause (MINOR-4), §3 wording (MINOR-6), §11
   sentence + seventh window (MINOR-3), §6 quotation (MINOR-5) — text only.
2. Segment 3 state stamp (MINOR-2) — one field.
3. §5 two paragraphs (MAJOR-1, MAJOR-2), §8 one paragraph (MAJOR-5),
   §7 one paragraph (MAJOR-4) — text only, no number moves.
4. §4 (MAJOR-3) — text, plus one new gate: the residue partition carries 0
   in every direction (`0 of 9 classes singleton, 0 of 9 direction-constant`),
   which converts the 64-state sweep from ground to check. Optionally extend
   the sweep to paper-20's 37-value alphabet and publish the ceiling
   attainment (9 menus at 34,992 of 50,653 states) as the disclosure it is.

No number in the paper, the output or the receipt changes under any of these.

**Candidate until adjudication.**
