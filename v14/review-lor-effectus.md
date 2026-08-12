# LOR (paper-30) — K2 EFFECTUS-LENS REVIEW

**Seat:** K2 (EFFECTUS — licensure, register, walls, choice inventory,
prose↔receipt). **Protocol:** v14 ledger #253 (row K2), launch corrected
at #257; protocol unchanged. **Object at `2369290`:**
`v14/paper-30-lor.md` `f3e9e9df2c70`, `v14/code/lor_exact.py`
`878e6007b785`, `v14/code/lor_output.txt` `427a5da397aa`,
`v14/code/lor_receipt.json` `8b4ca74d954c`; pin `v14/note-lor-pin.md`
`5239c4671f1a`.

**Hashes verified at start and at end of this review: all five match,
byte for byte.** No repo state outside the declared set was read; no
sibling's uncommitted work was opened (`v14/paper-24-sig.md`,
`paper-29-perr.md`, `note-paper23-correction.md` and the `smu`
modifications are untracked or modified working-tree state and were
NOT read).

---

## GRADE

**ACCEPT-WITH-FIXES (AWF).**

**50 independent recomputations, 0 disagreements. No false number was
found — not one delivered value moved under an independent rebuild of
the whole arena from nothing.** Every finding below is a **licensure**
finding: a sentence whose measured content is narrower, or differently
shaped, than the sentence. Three are MAJOR (one of them inverts a
scaling in a printed gloss), four are MINOR. No verdict segment is
overturned; segments 1–4 survive as *candidate readings* with the
scope words this review rules.

Four of the fifty recomputations are measurements the unit did **not**
take and this review supplies (marked ★ below): the per-witness
abstract-isomorphism census (864/864), the witness-independence of the
R = 9 control, the places-versus-budget scaling, and the live-cut
formula 9m − 17 that closes one of the unit's own successor questions.

---

## 1. THE RECOMPUTATION LEDGER (50 / 50 agree)

Rebuilt from nothing in `python3.13`, exact integers/`Fraction` only,
sharing no code with the unit. All agree with the delivered artifacts.

| # | quantity | recomputed | delivered |
|---|---|---|---|
| 1–2 | partitions of 9 into 3 triples, enumerated / closed form 9!/(3!³3!) | 280 / 280 | 280 |
| 3 | incidence spectrum | {0:1, 4:27, 6:54, 7:162, 9:36} | same |
| 4–6 | max incidence per round / six-round budget / saturating partitions | 9 / 54 / 36 | same |
| 7–8 | declared (site,link) cells = declared unordered pairs; all unordered pairs | 27; 36 | 27 |
| 9–12 | AG(2,3) lines / declared lines / non-collinear triples / declared triangles | 12 / 9 / 72 / 18 | 9, 18 |
| 13 | I7-STRICT triples, route 1 (field ≡ 1) | 12 unordered × 6 orders = **72** | 72 |
| 14 | I7-STRICT triples, route 2 (pair-cover exactly once) | **72** | 72 |
| 15 | ordered concatenations at count 2 in every cell | 144 × 36 = **5,184** | 5,184 |
| 16–19 | refined sites / slots / determined / free | 36 / 108 / 54 / 54 | same |
| 20 | carrier 9 actors + 27 pairs → 36 refined sites, bijection | **True** | True |
| 21–23 | determined links = actor-in-pair incidences; free links spanning a triangle; per triangle | 54 / 54 / 3 over 18 | same |
| 24 | new sites by direction | 9 / 9 / 9 | same |
| 25 | the 9-class census | 36, 324, 648, 72, 144, 1944, 1296, 648, 72 | **all nine match** |
| 26 | edge-count census (81 / 99 / 108) | 432 / 3,888 / **864** | 864 |
| 27–28 | canonical-carrier isomorphisms; 864 − 72 | **72**; **792** = the two dead classes exactly | 72; 792 |
| 29 ★ | **abstract isomorphism per witness** over all edge-count-108 witnesses | **864 of 864 isomorphic** | measured at 2 representatives |
| 30–31 | R = 6 cut census; split at the live locus | single live locus {9} at every witness; (1,1) at 27/27 | same |
| 32 ★ | **R = 9 control across witnesses** | live set {9,…,18}, **10 loci, at 1,728 of 1,728** | 10 (one control) |
| 33 | R = 9 raw split fiber | 2²⁷ = 134,217,728 | same |
| 34–38 | det coarse / refined / ratio / p04-minimal spectrum / posdef | 3 / 3⁄4 / 4 = 2² / {3⁄4, 1, 7⁄4} / True | same |
| 39–41 | I7 box (n₁,n₂ ≤ 6, n₃ ≤ 12): points / admissible / splittable / unique raw-fiber-1 vector | 432 / **361** / **261** / (2,2,2) | 361, 261, (2,2,2) |
| 42–43 | ladder rows m = 1,2,3,4,8; dyadic budgets; L = R iff m dyadic | ceilings 0,1,1,2,3; sides 3,6,6,12,24; places 9,36,36,144,576; [3,6,12,24] | same |
| 44 ★ | **places versus budget** | places = R² **exactly** at 3, 6, 12, 24; strictly < R² at 9, 15, 18, 21 | not taken |
| 45–46 | DIA counterfactual: unreached without / with the diagonal | 9, odd-odd class / 0 | same |
| 47 | **Aut of the refined arena**, independent backtracking count | **432** = 36 translations × 12 linear | 432 |
| 48 | coarse arena identified as K₃,₃,₃; \|Aut\| | **1,296** | 1,296 (and paper-19's own `\|AUT(K333)\|`) |
| 49 | refined relation = Cayley graph of (Z₆)² on the three declared directions | **True** | implied |
| 50 ★ | **live-cut count at R = 3m** | **9m − 17**, live loci = the integers in [9, 9(m−1)] | m = 2 and m = 3 rows only |

Two conventions worth recording because they cost this reviewer a pass:
the **72 triples are ORDERED** three-round schedules (12 unordered ×
3! — the code says so at its own construction), and **I7's declared
count box is n₁,n₂ ∈ [1,6], n₃ ∈ [1,12]** (432 points, 361 admissible).
Both are correct as delivered; neither is stated in the paper.

---

## 2. FINDINGS

### MAJOR-1 — the dyadic-ladder gloss inverts the measured scaling *(row 3)*

§7 prints: *"**places are logarithmically expensive.**"* That sentence
is **not licensed by the arithmetic it claims to read**, and the two
sentences immediately after it in the same paragraph are the correct
ones.

Measured (recomputation 42–44, and the unit's own ladder table): the
reachable side is L = 3·2^⌊log₂ m⌋ ≤ R with equality exactly at the
dyadic budgets, and places = L². Therefore **at the dyadic budgets the
reachable place-count is exactly R²** — 9 at R = 3, 36 at R = 6, 144 at
R = 12, 576 at R = 24 — and strictly below R² elsewhere. Places are
**quadratic** in the budget, which is *cheap*, not logarithmically
expensive. What the logarithm governs is the **depth**: k lawful steps
require R = 3·2^k rounds, so depth is **exponentially** expensive in the
budget, equivalently the reachable depth grows logarithmically with it.
The printed slogan names neither quantity correctly, and under the
natural reading ("cost ∝ log places") it asserts the opposite of the
measurement (cost ∝ √places).

**Exact repair** (prose only; no number moves, no re-run needed).
Replace the sentence in §7 with:

> Read plainly, and this is a candidate reading of the ladder rather
> than a measurement beyond it: **refinement DEPTH is exponentially
> expensive and places are quadratically cheap.** Each further level
> costs a doubling of the process — k levels need R = 3·2^k rounds —
> while at the dyadic budgets the reachable place-count is exactly R²:
> the process buys at most one unit of refined lattice length per
> round.

and in §12 replace the bullet's `"places are logarithmically
expensive"` with `"the depth/places scaling"`. The ledger's #252
bracket (`the places-are-logarithmically-expensive gloss: candidate,
only the R=6 row driven`) inherits the same repair: the candidate stamp
was right, the slogan was not.

### MAJOR-2 — `COMPOSE-AND-AGREE` is forced, not discriminating *(row 3 / row 7)*

Head segment 2 carries `COMPATIBILITY=COMPOSE-AND-AGREE(06-SUPPORT-IS-
04-WHOLE-FIBER-AT-27-OF-27; THE-TWO-ORDERS-AGREE-AT-108-OF-108-SLOTS;
CONFLICT-FALSE)`, and §11 reads it out as *"the two live laws agree
everywhere they are both defined."* At this arena that conjunction
**could not have come out otherwise**:

- §3.3 measures 04's split fiber to be the **single point** (1,1) at
  all 27 intervals;
- §4.1 measures 06's law **non-empty** at all 27;
- 06's support is by construction a subset of the split fiber.

Non-empty subset of a one-point set ⟹ set equality at 27/27 ⟹ the two
refined records coincide at 108/108 slots. The whole of Stage 4 is a
corollary of Stage 1, and no arena is exhibited at which the two laws
*could* disagree. `MUT-COMPAT` kills the gate; it does not make the
measurement two-way.

This does not make the row false — it makes it **empty of
discriminating content**, which is exactly the register a headline may
not hide.

**Exact repair.** In §5, after "Measured: the support of paper-06's law
is exactly paper-04's whole split fiber at 27 of 27 intervals", add:

> Both facts are forced once §3.3 is in hand: at count 2 the dyadic
> fiber is a single point, and a non-empty subset of a one-point set is
> that set. At this arena `CONFLICT-FALSE` therefore carries no
> discriminating content — any non-empty per-interval law would have
> agreed. The first arena at which the comparison can fail is n = 4,
> where paper-06's invariant simplex has dimension n − 2 = 2 and the
> dyadic fiber has three points per interval; that is R = 12, and it is
> LOR-B's question, not this unit's.

Optional (only if the unit re-runs for another reason): head segment 2
gains `COMPOSE-AND-AGREE-FORCED-AT-THE-POINT-FIBER`. **The licensed
claim section below binds the reading in the meantime.**

### MAJOR-3 — the verdict's own carrier is missing from the choice inventory *(row 6)*

§10 lists 13 items. The **extended carrier** — `SITE ← ACTOR ⊕
CO-DIVISION-PAIR`, the object segment 3 is entirely about — is not one
of them. Row 3 of the inventory covers only "the site carrier: actors
to the coarse sites".

What is measured: the un-extended carrier is `ARITY-DEAD` (9 objects
against 36 sites, and the detector's own reason — "a declared
restriction can only shrink a site set" — makes the death structural,
not a search failure). What is **not** measured: any alternative
extension. Exactly one 36-object carrier was constructed and tested; no
census of alternative extensions (ordered pairs, triangles, mixed
carriers) exists anywhere in the run. So "forced" is licensed for the
**necessity** and not for the **choice**.

The defence is real and should be stated rather than left implicit: the
27 objects are not invented here — they are the committed dictionary's
own second clause (`CO-DIVISION-ACTOR-PAIR → LINK`, paper-19's WELD3,
fiber 1) **re-typed** onto sites one level down. That makes the
extension canonical, not arbitrary. It does not make it censused.

**Exact repair.** Add to §10:

| 14 | **the extended carrier `SITE ← ACTOR ⊕ CO-DIVISION-PAIR`** | **declared, VERDICT-DETERMINING** | **1 tried; alternative 36-object carriers uncensused** | §6.2 — the necessity is forced (the 9-actor carrier is ARITY-DEAD against 36 sites); the objects are the committed dictionary's second clause re-typed, not invented |

and amend §10's closing sentence ("One genuinely free item… and one
**measured** item") to name the third class: one free, one measured,
one **declared-and-verdict-determining**.

### MINOR-1 — the abstract-isomorphism half of §6.4 is representative-level *(row 5)*

§6.4: *"Two of the dead classes carry a relation that is abstractly
isomorphic to the refined lattice… A witness can have the right space
and the wrong map onto it, and 792 of the 864 right-shaped witnesses
do."* The code measures the dead classes **at one representative each**
(`# the dead classes, at their own representatives`), and the receipt
key is `abstractly_isomorphic_dead_arenas` — *arenas*, two of them. The
counts 864, 72 and 792 are exhaustive; the *shape* attribution to all
792 is an extrapolation from two objects, and the receipt's own name for
the 864 is `witnesses_with_the_refined_lattices_edge_count` — an edge
count, which is necessary and not sufficient for isomorphism.

★ **This review supplies the missing census: all 864 are in fact
abstractly isomorphic to the refined lattice, per witness** (24
unordered × 36 = 864, backtracking isomorphism search against the
Cayley graph; 864/864 True). The sentence is **true**; only its stamp
was missing.

**Exact repair.** "…and 792 of the 864 right-shaped witnesses do — the
edge count and the carrier verdict exhaustive over all 5,184, the
abstract shape measured at one representative per class."

### MINOR-2 — "structurally live" is undefined, and the theorem's second clause is unsourced *(row 3)*

§7's arena theorem says *"At budget R = 3m a **structurally live**
schedule reaches the link-constant record (m,m,m) **and no other
homogeneous record**"*. The term is never defined in the paper, and the
receipt's `ceiling/budget_law` string carries only the first clause
("reaches the link-constant record (m,m,m) at exactly R = 3m") — the
"no other homogeneous record" clause appears in the paper alone.

It is true and one line deep: a saturating round deposits 9 incidences
(measured exhaustively over all 280 partitions, so it binds at every R),
m such blocks deposit 27m, a homogeneous (n,n,n) needs 27n, hence n = m.
**Repair:** define "structurally live" = every round saturating, and
carry the one-line ground; or drop the second clause from the paper to
match the receipt.

### MINOR-3 — the expansion falsifier proves the receipt side only *(row 8)*

Verified: `MUT-WALL-COSMO` injects *"the universe expands as the record
refines and new space is created by the process"* into the **declared
measurement surface** (receipt keys + gate statements/evidence) and dies
at `G-WALL-COSMO`. The falsifier is honest and on target.

But the gate's paper-side clause is **positive only**: the paper must
contain the confinement stamp; it is never scanned for expansion
language, unlike `G-WALL-L1`, which scans the paper itself for a banned
sentence and whose mutant injects there.

**No code repair is asked**, because the asymmetry is defensible: topic
needles ("cosmological", "expansion of space") occur in the paper twice
already — inside the wall's own denials (§9, §12) — so a paper-side
needle scan would fire on the abstention itself. L-1 escapes this only
because it bans an exact sentence rather than a topic.

The consequence is the thing to record: **the confinement of the
new-places language outside the object under test is a discipline, not a
gate.** Downstream prose — this ledger, the successor pins, any
orchestrator gloss — is unreachable by any falsifier in this unit. The
ledger row drafted in §4 below carries the stamp with the sentence for
exactly this reason.

### MINOR-4 — an unanchored "respectively"

§6.4's *"the field it induces carries 27 and 18 zero cells
respectively"* has no antecedent order in the sentence. It matches the
table's row order (9|9 before 12|6) and contradicts the receipt's sorted
arena list (`triangles12-lines6` before `triangles9-lines9`). Both
numbers are correct (recomputed from the receipt rows). **Repair:** name
the classes — "27 at the nine-triangle class and 18 at the
twelve-triangle class".

### NOTE (an upgrade the unit is entitled to and does not take)

The driven window is **one schedule per census class plus six at the
surviving stratum plus two seed-fan** — the eight `W6-DEAD-*` strata are
exactly the eight dead classes. So every one of the nine classes in the
5,184-witness census carries at least one schedule shown reachable by
the committed grammar. The paper describes W6 only as "six at the
surviving stratum, eight one per measured dead class"; it never draws
the consequence, which is that the census is **class-wise
grammar-realised, 9 of 9**, not merely combinatorial. Worth one sentence
in §2 or §3.2.

---

## 3. THE LICENSED CLAIM

What follows is what may be said, and in what words, on the delivered
evidence. Every sentence here is *candidate* until adjudication.

### 3.1 The new places *(row 1 — the decisive row)*

**RULED.** The paper's own form — §6.2's *"The refinement's new places
are the old links"* — **is licensed**, at the site level, as an exact
canonical bijection, and it is **stronger than the paper says**: it is
witness-independent.

The measured content, split into the two halves the paper runs together:

- **Site level (witness-independent, exact).** The 27 new refined sites
  are the interiors of the 27 coarse intervals, and the coarse intervals
  *are* the co-division pairs {x, x+l} — because I7-STRICTness forces
  every witness's nine conflict groups to cover each of the 27 declared
  pairs exactly once (recomputation 14), so the co-division relation is
  the same 27 objects at **every** one of the 5,184 witnesses. The
  carrier map (actor ↦ its coarse image, pair ↦ the interior of its own
  interval) is a bijection onto the 36 refined sites, and the 54
  determined links are the 54 actor-in-pair incidences. None of this
  varies over the family.
- **Free-half level (witness-dependent).** Whether the *process*
  realises the 54 free links as division footprints holds at 72 of
  5,184, COUNTING-ONLY. This is where the head's stamp belongs and where
  it is correctly placed.

**Licensed sentence (site level):**

> At the R = 6 welded record (2,2,2), the one lawful refinement step
> inserts exactly 27 new sites, and those sites are in canonical
> bijection with the 27 co-division pairs of actors — the coarse
> record's own links. The refinement's new places are the old links.
> The old places remain actors: the refined carrier is ACTOR ⊕ PAIR,
> 9 + 27 = 36.

**"The new places are the old RELATIONSHIPS" — RULED: licensed only as
a stamped process-side paraphrase, and NOT in the bare form.** The
object in bijection with the new sites is the unordered co-division
pair, which is an element of the co-division *relation* (the unit's own
arena row), so "relationship" is a faithful rendering of the object.
What the bare slogan smuggles is a generalisation the same measurement
**refutes at this very arena**: it invites "places are relations", and
the measured carrier is ACTOR ⊕ PAIR — three quarters relations, one
quarter actors. The nine old places are not relations, and nothing here
makes them so.

**The licensed form of the process-side sentence, if it is wanted:**

> The refinement's new places are the process's old co-division pairs —
> the coarse record's own links — 27 for 27 at this arena. The old
> places remain actors: this is a mixed carrier, not a relational one.

**Barred:** "places are relations"; "space is made of relations"; "the
world grows new places" without the §4.3 stamp attached; any use of the
27 ↔ 27 bijection to license a claim about levels above 1 (see 3.5).

The description stamp itself (§4.3, gated word for word) is present,
correct, and does the work the pin asked of it. `G-WALL-COSMO` verifies
it in the object under test.

### 3.2 LOR ↔ OCC *(row 2)*

**No OCC review is committed** (`git ls-tree` at HEAD: no
`review-occ-*`); #256 launched its three seats and they are in flight.
So the reconciliation below is against OCC's **delivered** artifacts at
`7ab2f21` (paper `1b140f7973d4`) only, and both units are
**delivered-not-terminal**. Nothing here may be cited by either
adjudication as independent confirmation of the other.

**What is true, and it is worth the ledger's ink.** The 27 objects are
literally the same objects. OCC: *"cell (x, l) IS the unordered
co-division pair {x, x+l}"*, 27 cells, the carrier the excitations use;
`ACTOR→SITE` reaches 9 of 27, `excitation→actor` is not a function.
LOR: the 27 new refined sites are the interiors of the coarse intervals,
i.e. those same 27 pairs; the bare 9-actor carrier is `ARITY-DEAD`.
Both units are built on the same nine actors and the same committed
three-link list (LOR reads it at (path,value) from I7's own receipt; OCC
gates its rebuild against the coupled machine's committed receipt), so
the identification is **construction-level and anchored, but no run has
computed it**.

**And the deflation, which must travel with it.** The convergence is not
two independent measurements pointing at one fact. Both units hit the
**same arity mismatch of the same first dictionary leg** and both were
repaired by the **same committed second clause**
(`CO-DIVISION-ACTOR-PAIR → LINK`, paper-19's WELD3, fiber 1), which was
committed before either unit ran. The independence is of the two
workers' investigations, not of the objects or of the repair.

**Licensed cross-unit sentence (delivered stage):**

> Two units delivered the same hour found the same 27 objects load-
> bearing in different directions: OCC measured that the coupled
> machine's excitations ride the unordered co-division pair (27 cells,
> 2 actors per cell, 6 cells per actor, excitation→actor not a
> function), and LOR measured that the one lawful refinement step's new
> places are those same 27 pairs (9 + 27 = 36, bijection). In both, the
> ACTOR leg of the committed dictionary is the leg that fails — 9 of 27
> in OCC, ARITY-DEAD against 36 in LOR — and in both the repair is the
> dictionary's own second clause. The identification of the two
> 27-sets is construction-level, from the same pinned actor set and
> link list; no run has yet computed it, and no cross-unit measurement
> exists. Both units are delivered-not-terminal.

**Barred at this stage:** "matter lives where the new places appear";
"refinement creates places at the carrier of matter"; any sentence
joining the two arenas. They are different records — OCC runs on the
welded landing record (count 1 at every cell), LOR on the R = 6 (2,2,2)
— and no map between the two units' objects has been computed by
anything. This is a **lead**, and it is the first item in 3.5.

**Draft ledger row — STAGE 1 (now, both delivered):**

> **THE PAIR CONVERGENCE, DELIVERED-STAGE (LOR #252 + OCC #255).** Two
> delivered-not-terminal units, same hour, same 27 objects: the
> unordered co-division pairs {x, x+l}. OCC: the coupled machine's
> carrier IS the pair (27 cells; 2 actors/cell 27/27; 6 cells/actor 9/9;
> excitation→actor NOT a function; ACTOR→SITE covers 9 of 27). LOR: the
> refinement step's 27 new places ARE the pairs (carrier 9+27=36
> bijection; the bare 9-actor carrier ARITY-DEAD). Both failures are of
> the SAME first dictionary leg; both repairs are the SAME committed
> second clause (`CO-DIVISION-ACTOR-PAIR→LINK`, paper-19 WELD3, fiber
> 1) — so this is one committed clause proving load-bearing in two
> directions, NOT two independent confirmations. The two 27-sets are
> identified by shared construction from the same pinned actor set and
> link list; NO run computes the identification, and the two arenas
> differ (OCC: the landing record, count 1; LOR: (2,2,2) at R = 6).
> Barred until measured: any sentence placing matter at the new places.
> Both stamps candidate; K-seats in flight on both.

**Draft ledger row — STAGE 2 (only after BOTH adjudications; conditions
stated so the row cannot be written early):**

> **THE PAIR CONVERGENCE, TERMINAL-STAGE.** Writable only when (i) LOR
> and OCC are both terminal, (ii) some unit has COMPUTED the
> identification of the two 27-sets rather than inheriting it by
> construction, and (iii) a map between the two arenas (landing record
> ↔ (2,2,2), or their common refinement) has been measured. Absent
> (ii)–(iii) the terminal row says exactly what the delivered row says,
> with the candidate stamps removed and nothing added.

### 3.3 The dyadic ladder *(row 3)*

Licensed: the ladder's rows as **arithmetic** from the ceiling law and
the budget law, driven at m = 2 only, exactly as §12 stamps. Licensed
as printed: "each further level of refinement costs a doubling of the
process" and "the process buys at most one unit of refined lattice
length per round". **Not licensed as printed:** "places are
logarithmically expensive" (MAJOR-1). Licensed in its place: depth is
exponentially expensive in the budget; places are quadratic, exactly R²
at the dyadic budgets (recomputation 44).

### 3.4 Completion-relativity, the landing on 3/4, and the SIG handoff *(row 4)*

**Completion-relativity: licensed as printed, and it is the unit's most
honest row.** det is completion-relative ({3/4} process-supplied vs
{3/4, 1, 7/4} at paper-04's declared minimal completion), signature is
completion-blind (positive definite at 36/36 under both) — recomputed.
The choice-inventory class (**measured**, 2 declared, reported as a
relativity rather than resolved) is the right class, and §12's non-claim
("no claim that the process-supplied completion is *forced*") is
correctly worded.

**The landing on paper-19's 3/4: RULED — neither self-similarity nor a
numerical coincidence. It is a forced record-vector identity, and it is
a theorem now, not something R = 12 will settle.** The chain is closed:
count 2 at every interval ⟹ the split is the single point (1,1) ⟹ the
refined record is link-constant at 1 ⟹ q = [[1,−1/2],[−1/2,1]] ⟹ det =
3/4; and paper-19's landing record is *also* (1,1,1), whose determinant
is a function of the vector alone. Two objects with the same record
vector have the same determinant. Nothing is being confirmed by the
agreement.

**Licensed sentence:**

> The step's output is the record vector (1,1,1) on 36 places — the same
> vector paper-19 committed on 9 places, hence necessarily the same
> determinant 3/4. The agreement is forced by the (1,1) split, not
> discovered; what is measured is that the refinement carries the
> record vector down a level while quartering the determinant, det
> falling by exactly 2^d.

**"Self-similarity": NOT licensed.** The refined object is not
isomorphic to the coarse one (36 places against 9; and it is admissible
by I7's predicate while outside I7's declared arena L = 3 — the paper's
§6.1 scope sentence is exactly right and should be the one quoted). A
self-similar **tower** — (2^k,…) at side 3 stepping k times to (1,1,1)
at side 3·2^k — is a candidate structure the ladder permits, and it is
**undriven above m = 2 and not even well-posed there**: at n = 4 the
split fiber has three points per interval, so a tower needs a selection
rule the record layer has not been shown to carry. That is LOR-B's
question (3.5), not a coincidence pending R = 12.

**The SIG handoff: written, and correctly scoped from this side** — det
completion-relative, signature completion-blind, 36/36, the induced form
NAMED AND NOT READ under a mandatory gate whose falsifier deletes the
sentence (verified present). The consumer side is **out of scope for
this review**: the SIG unit's artifacts are untracked working-tree state
and were not read, per the discipline.

### 3.5 The abstract ≠ dictionary register *(row 5)*

**"Being shaped like space is cheaper than being space" — RULED:
licensed in substance, and the unit's measurement is stronger than the
slogan.** The slogan understates it in one direction and overstates it
in another.

Understates: the 792 do not merely have the right *shape*. Run through
the **RSQ standard's own detector** they return `FOUND-candidate`, 432
isomorphisms at both readings, fibers 1/1/1, **zero free items** — the
full motivated-weld verdict — while the canonical process carrier on
them is not an isomorphism and induces 27 and 18 zero cells. The
standard by which this corpus has been declaring dictionaries **does not
separate them from the real one**; only the canonical carrier does.

Overstates: "cheaper" is a cost word over a space carrying **no declared
measure**. The unit stamps every fraction COUNTING-ONLY (4 stamped rows,
gated) and the head carries the stamp adjacent to the 72. So "cheaper"
is licensed strictly as a count comparison — 864 against 72 out of
5,184, exhaustively enumerated — and never as typicality, probability
or "most witnesses".

**Licensed sentence:**

> At this arena the RSQ standard's own verdict — FOUND, zero free items,
> fibers 1/1/1 — is attained by relations whose canonical
> process-supplied carrier is not an isomorphism at all: 864 of the
> 5,184 witnesses carry the refined lattice's edge count and (this
> review's census) all 864 are abstractly isomorphic to it, while the
> canonical carrier is an isomorphism at 72. Structural adequacy is not
> carrier adequacy. Counts are COUNTING-ONLY; no measure on the witness
> space is declared.

**The connection to weld-2's EMPTY, licensed and in this exact
asymmetric form.** Weld 2 (paper-13) censused 60 candidates and returned
**0 FOUND / 0 SMUGGLED under both readings**, and its blades were
structural: gradedness forbids I7's odd cycle, and *"the only link
generator carrying a target-type cycle at this carrier is the actor
pair, and it has exactly 2 site objects"* — arity. So in weld 2,
structure was **sufficient to kill**. In LOR, structure — up to and
including the full zero-free-items verdict — is **insufficient to
certify**. The licensed synthesis:

> Structural shape is a sufficient disqualifier and an insufficient
> qualifier. Weld 2 killed 60 candidates on shape alone; LOR shows 792
> witnesses passing every shape test the corpus has, including the RSQ
> standard's own, while failing the one map the process actually
> supplies. The dictionary was never the shape.

And the arity blade is the same blade twice: weld 2 died at "2 site
objects against 9"; LOR's bare carrier dies at "9 site objects against
36". Which is 3.6.

### 3.6 The arity-death of the bare carrier *(row 6)*

**RULED: the extension is forced in its NECESSITY and declared in its
CHOICE.** Licensed:

> The un-extended dictionary cannot survive refinement: nine actors
> cannot carry thirty-six sites, and the detector's reason is structural
> — a declared restriction can only shrink a site set — so the death is
> not a failed search. What survives is not a rescue of the old carrier
> but a re-typing of the committed dictionary's own second clause:
> `CO-DIVISION-ACTOR-PAIR → LINK` becomes `CO-DIVISION-ACTOR-PAIR →
> SITE` one level down. Exactly one extension was constructed and
> tested; no alternative 36-object carrier was censused.

**Barred:** "the extension is forced" without the split; "the process
had no choice"; any claim of uniqueness of the extended carrier.
(MAJOR-3 adds the inventory row that carries this.)

### 3.7 What is really being measured at R = 6 — the synthesis this review adds

Three of the unit's cleanest results are the **same degeneracy** seen
three times, and the paper discloses the first two and not the third:

1. the split fiber is a single point **because n = 2** (§3.3);
2. paper-06's law is unique **by triviality, not by selection** — the
   invariant simplex has dimension n − 2 = 0 (§4.1, quoting paper-06's
   own words, honestly);
3. ★ the live cut locus is unique **because m = 2**. For a record built
   by concatenating m I7-STRICT triples, a cut at event k leaves every
   cell positive on both sides **iff** the left contains block 1 and the
   right contains block m — i.e. iff 9 ≤ k ≤ 9(m−1) — because k < 9
   groups cover exactly 3k < 27 distinct cells. So the live loci are the
   integers in [9, 9(m−1)] and their count is **9m − 17**: one at m = 2,
   ten at m = 3, nineteen at m = 4. Measured exhaustively at m = 3 by
   this review (1,728 three-block schedules, live set {9,…,18} at every
   one — the unit's single R = 9 control is witness-independent), and at
   m = 2 by the unit (5,184/5,184).

**Consequence for the unit's own successor register:** §13's fourth
bullet — *"The seam. The cut is unique at R = 6 and tenfold at R = 9.
Where between those the uniqueness fails, and whether it is the block
structure or the count that carries it, is a one-parameter question"* —
**is closed**. There is no interior (m is an integer), **the block
structure carries it entirely, and the count plays no role.** The
uniqueness at R = 6 is a boundary effect of the smallest non-degenerate
arena, not a determination property of the process. The paper's own
"the process-supplied cut selects but does not determine in general.
R = 6 is the arena at which it determines" is correct and can now be
sharpened to "R = 6 is the *only* arena at which it determines, because
9m − 17 = 1 has one solution."

**Licensed synthesis sentence for the unit as a whole:**

> Everything that comes out forced at R = 6 is forced by the same
> smallness: n = 2 makes the split a point and paper-06 unique by
> triviality, and m = 2 makes the seam unique. The unit's achievement is
> that the refinement *acts at all* and that the dictionary survives at
> an extended carrier — not that the acting is uniquely determined by
> the law. The first arena where any of these has a fiber to choose
> from is R = 12.

---

## 4. THE WALLS, AND THE CHOICE INVENTORY *(row 8)*

**Verified.**

- **L-1** — argued before any test and declined; the banned sentence is
  absent from the paper; the gate normalises whitespace, folds ASCII and
  strips markdown prefixes on both sides, and its mutant injects into
  the paper. Correct, and the only wall whose scan reaches the object
  under test.
- **BHS / KR** — abstentions measured on the declared surface with
  falsifiers that write the forbidden reading in and die. Correct in
  kind; the surface is the receipt, not the paper (see MINOR-3).
- **COSMO** — falsifier verified on target; the confinement stamp is
  present in the paper word for word and gated. **No cosmological or
  expansion reading survives anywhere in the object under test** — the
  two occurrences of the words are inside the wall's own denials (§9,
  §12), which is the correct place for them. The residual exposure is
  downstream prose, which no gate reaches (MINOR-3).
- **LORENTZ-NAMED** — the naming sentence is present verbatim and
  mandatory; its falsifier deletes it and dies. §6.6's "NAMED AND NOT
  READ" is the right register for a determinant that has just become a
  positive-definite Euclidean form, and it is exactly paper-19's
  precedent.
- **E-24 measure stamps** — 4 published fractions, all COUNTING-ONLY
  with reasons, gated for completeness. The 72/5,184 and 864/5,184 rows
  carry it. Correct.

**Choice inventory.** 13 rows; classes and fibers correct as far as they
go; row 6 ("the split — forced — three independent routes agree") is
right (and the three routes are genuinely independent: arithmetic,
symmetry, the seam). Row 11 (the completion — **measured**, 2 declared)
is the model of how a relativity should be filed. **One item is
missing** — the extended carrier (MAJOR-3). One genuinely free item,
instrument-side, correctly identified.

**Prose ↔ receipt.** The 14 rendered claims are the numeric backbone and
each appears verbatim in the paper; 13 table rows render; the numeral
scan covers 771 numerals with 2 declared exemptions, both firing. Spot-
checked independently: every number I recomputed (50 quantities) appears
in the paper with the value the receipt carries. **The interpretive
sentences are, as expected, the unrendered ones** — "the new places are
the old links" (also in a gate statement), "the abstract structure is
cheaper than the dictionary" (also in the head and a gate statement),
"places are logarithmically expensive" (free prose, and the one that
broke — MAJOR-1). That is the register boundary this seat exists to
police, and it held everywhere except MAJOR-1.

---

## 5. THE SUCCESSOR REGISTER *(row 7)*

### LOR-B (R = 12, the record (4,4,4)) — what a second step needs

1. **The split stops being forced.** At n = 4 the dyadic fiber has 3
   points per interval (3²⁷ raw) and paper-06's invariant simplex has
   dimension 2. Everything this unit reports as *forced* becomes a
   *choice with a fiber*. **This is where `COMPOSE-AND-AGREE` first has
   teeth** (MAJOR-2), and where a self-similar tower would need a
   selection rule (3.4).
2. **The seam question is answered before it is asked.** 9m − 17 = 19
   live loci at m = 4 (3.7). LOR-B should not re-open it; it should ask
   the *next* question: does the process still supply a *canonical* cut
   when it supplies nineteen — e.g. is the balanced one distinguished by
   anything the record layer carries?
3. **The pair-of-pairs question, and its arity bookkeeping is already
   forced.** At level k the lattice has side 3·2^k, so sites_k = (3·2^k)²
   and links_k = 3·sites_k, hence **sites_{k+1} = sites_k + links_k**
   exactly (36 = 9 + 27 at k = 0; **144 = 36 + 108** at k = 1, which is
   R = 12's place-count). So *if* a carrier exists at every level it must
   be `SITE_{k+1} ← SITE_k ⊕ LINK_k` — at level 2, actors ⊕ pairs ⊕
   pairs-of-{actor,pair}. The arity is a **theorem**; the dictionary's
   survival is not. LOR-B's real question is whether the *process*
   supplies the level-2 free half, which is four times larger, and
   whether the analogue of the 72/5,184 class survives at all.
4. **The 792, and what they are records of** (the unit's own third
   bullet) is now sharper: all 864 are abstractly isomorphic (MINOR-1
   ★), so the class is *exactly* "right space, wrong map", with no
   shape-level residue to explain it. What distinguishes them is a
   process fact — which conflict groups are lines — and the mechanism is
   already exact.

### SEC cross-feed (PLAN.md #254 names LOR terminal as a pin parent "for the extended-carrier lesson")

Two lessons transfer, and they are not the same lesson:

- **Arity first.** Before asking whether the union of two welded sectors
  admits a forced dictionary, count the target's places against the
  carrier's objects. The un-extended carrier can be arity-dead, and the
  repair that worked here was *not* inventing objects: it was re-typing
  the committed dictionary's next clause. For SEC: a union of two
  9-actor sectors sharing k actors has its own co-division pairs, and
  the arity ledger (actors, pairs, cross-sector pairs) should be the
  first gate, before any isomorphism search.
- **And the harder one: do not let the RSQ standard adjudicate the
  gluing alone.** At LOR's arena 792 witnesses returned FOUND with zero
  free items on a relation whose canonical carrier is not an
  isomorphism. If SEC prices its gluing fiber only by "a motivated map
  exists", it will count right-shaped wrong maps. **The gluing must be
  tested against the canonical, process-supplied cross-sector map** —
  the analogue of LOR's canonical carrier — and the two verdicts
  reported separately, exactly as LOR reports 864 against 72.

A third, weaker feed: LOR's completion-relativity is the shape SEC's
"gluing fiber" will most likely take — an object admissible under two
declared completions, motivated under one. File it as **measured**, not
resolved, when it appears.

---

## 6. SUMMARY FOR THE ADJUDICATION

- **Grade: AWF.** 50 recomputations, 0 disagreements, no false number.
- **MAJOR-1:** "places are logarithmically expensive" inverts the
  scaling — places are quadratic (exactly R² at dyadic budgets), depth
  is exponential. Prose repair given; the ledger's #252 bracket inherits
  it.
- **MAJOR-2:** `COMPOSE-AND-AGREE` / `CONFLICT-FALSE` is forced by the
  point fiber and carries no discriminating content at this arena;
  clause supplied; n = 4 named as the first arena with teeth.
- **MAJOR-3:** the extended carrier — the verdict's own object — is
  absent from the choice inventory; row 14 supplied; "forced" splits
  into forced-necessity / declared-choice.
- **MINOR-1..4:** representative-level shape claim (this review supplies
  the exhaustive census: **864/864**); "structurally live" undefined and
  the theorem's second clause unsourced; the expansion falsifier proves
  the receipt side only (defensibly — the confinement downstream is a
  discipline, not a gate); one unanchored "respectively".
- **Row 1 ruled:** "the new places are the old links" is licensed and is
  witness-independent at the site level; "the new places are the old
  relationships" is licensed only as a stamped process-side paraphrase,
  never bare, because the measured carrier is ACTOR ⊕ PAIR and the bare
  form invites "places are relations", which this arena refutes.
- **Row 2 ruled:** the convergence is real and is **one committed clause
  proving load-bearing in two directions**, not two independent
  confirmations; the two 27-sets are identified by construction and by
  no run; both units delivered-not-terminal; two ledger rows drafted,
  the terminal one gated on conditions so it cannot be written early.
- **Row 4 ruled:** the landing on 3/4 is a **forced record-vector
  identity**, not self-similarity and not a coincidence pending R = 12.
- **Row 5 ruled:** the slogan is licensed in substance and understates
  the finding — the RSQ standard's own verdict does not separate the 792
  from the real dictionary.
- **★ Review contribution:** the live-cut count at R = 3m is **9m − 17**
  (block structure carries it; the count plays no role), which **closes
  the unit's own fourth successor question** and exhibits the third
  instance of the R = 6 degeneracy theme.

*Hashes re-verified at close of review: paper `f3e9e9df2c70`, code
`878e6007b785`, output `427a5da397aa`, receipt `8b4ca74d954c`, pin
`5239c4671f1a` — all unchanged.*
