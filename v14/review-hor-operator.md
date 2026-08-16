# HOR (paper-42) — K1 OPERATOR-LENS REVIEW

**Seat:** K1, the operator lens — the mathematics itself, rebuilt from the
parents' definitions on code sharing nothing with `v14/code/hor_exact.py`.
**Stance:** hostile; every number assumed wrong until independently rebuilt.
**All rulings below are candidate until adjudication.**

**Objects, sha256-12, verified at open AND at close (all five match at both):**

| object | sha256-12 |
|---|---|
| `v14/paper-42-hor.md` | `376e29746e39` |
| `v14/code/hor_exact.py` | `00c985939230` |
| `v14/code/hor_output.txt` | `87ea30df2a92` |
| `v14/code/hor_receipt.json` | `df3549596b4e` |
| `v14/note-hor-pin.md` (pin) | `0cf8515e184f` |

Parents re-hashed against the paper's own inheritance paragraph, **14 of 14
matching at HEAD**: paper-18-gauge-rung `62cfe5689d2c`, r5_gauge_exact
`0d98de793b79`, r5_gauge_receipt `0c02b7684e5b`, paper-36-pot `1e495318252d`,
pot_receipt `3a48c3806443`, paper-34-act `d933221780ed`, act_receipt
`7fd1267bddc7`, paper-10-defect-on-the-stage `1063401c7bb5`, paper-15-momentum
`89c636906061`, paper-30-lor `0a08203b7e99`, paper-38-epr `22beb6696223`,
paper-01-continuum-rung `c4c8880874bf`, TEMPLATE `809ebe3514ad`, era_template
`d04a3eb58fbc`.

Authority read as law before anything else: the pin, HANDOFF §4/§9, RUNBOOK
through E-33, ledger #374. Repo access read-only; single repo write = this
file. No in-flight REC file was opened.

---

## GRADE: **AWF** (accept with fixes)

**Every physics number in this unit is right.** I rebuilt the field, the
alphabet, the coin family, the parity strata, the tick, the cone, the emergent
c, the contractible and dynamical stability sweeps, the winding census, the
homology, the control arms, the patch gauge group, POT's closed form and
area-blindness, the eighteen-row closure census, the quantifiability gate and
the directed system — from the parents' definitions, on primitives sharing
nothing with the instrument — and **616 published quantities reproduced
exactly, with zero disagreements.** That includes all 449 cells of the eight
published tables, all 51 numerals inside the 18 licensed claim sentences, the
30 inherited (path, value) anchors re-read from the parents' own receipts, and
the 18 verbatim windows re-located in their pinned sources. The verdict word
`HOR-UNDETERMINED-R-NATIVE` is carried by measurements that reproduce.

Beyond that I ran an invariance probe the unit does not itself run, on an axis
it declares free, and **the unit passes it** (§8 below).

Three **majors** stand. None is a wrong physics number. Two are about the
*closure census* — the part of the unit that carries its most quotable
headline, "eight sealed laws were torus-artifacts" — where the classifier is
not consuming the evidence that decides six of its nine `SURVIVES-VERBATIM`
rows and two of its eight `CLOSURE-ARTIFACT` rows. The third is a **published
count that is provably wrong in both delivered artifacts**, produced by typed
offsets that this unit's own no-typed-counts gate is structurally unable to
see. Four minors follow.

---

## 0. What I did, and how independent it is

**Independent primitives.** I carry $\mathbb{Q}(\zeta_8)$ as integer 4-tuples
over $(1,z,z^2,z^3)$ mod $z^4+1$ with my own convolve-then-fold multiply, and
— the load-bearing difference — I compute every holonomy by a **different
scaling route**: the embedded link operator is carried as $2\times$ the true
operator (the $2\times2$ block is the doubled coin, every other diagonal entry
is the scalar 2), so the ordered product of $k$ factors is exactly $2^k$ times
the true holonomy and the trace is divided by $2^k$ once at the end. The
instrument instead tracks a **per-row** power-of-two and levels the rows before
each factor (`hor_exact.py:1965-2016`). The two routes agree on every trace I
compared. Nothing is imported from `hor_exact.py`; I read it only to recover
the declarations (ladders, strides, windows, shape cap, schedule).

**Files** (scratch only, 556 K, well under 5 G):
`…/scratchpad/hor_k1/k1_field.py`, `k1_loops.py`, `k1_part1.py`,
`k1_part2.py`, `k1_part2b.py`, `k1_part3.py`, `k1_vacuity.py`.

**Recomputation count, honestly:** 616 published quantities —
449 table cells (T-CONE 96, T-STRATA 78, T-GAUGE 78, T-CENSUS 90, T-FAMILY 36,
T-DYNAMIC 32, T-HORIZON 24, T-ARMS 15) + 51 claim-sentence numerals + 30
path-value anchors + 18 verbatim windows + 19 digests (14 parent + 5 object) +
9 template family identifiers + 30 gate-ledger evidence scalars + 6 seal /
ledger accounting numbers + 4 head and rendering equalities. **Zero
disagreements on the physics; three disagreements on the accounting, all in
MAJOR-3.**

---

## 1. The tick and the c census — REPRODUCED

Rebuilt from R5's declarations, not imported.

| quantity | published | mine |
|---|---|---|
| alphabet / admissible rows / coins | 25 / 80 / 640 | **25 / 80 / 640** |
| sectors DIAG / ANTI / BAL | 64 / 512 / 64 | **64 / 512 / 64** |
| unitary by a second (column) route | 640 | **640** |
| vanishing patterns | 3: `0110`→64, `1001`→64, `1111`→512 | **identical** |
| coins failing the vanishing theorem | 0 | **0** |
| one-tick reach 0 / 1 / >1 | 64 / 576 / 0 | **64 / 576 / 0** |
| tick columns / probe coins / non-unitary / identity failures | 320 / 5 / 0 / 0 | **320 / 5 / 0 / 0** |
| T-STRATA, all 13 rows × 6 columns | — | **identical** |
| T-CONE, all 16 rows × 6 columns | — | **identical** |
| sum-norm radius = tick at every depth | true | **true** |
| product box at every depth | true | **true** |
| $c$ (sum norm), attained | 1, at 16 of 16 | **1, at 16 of 16** |
| $c$ (max norm) instantaneous / sustained over whole sweeps | 1 / 1/2 | **1 / 1/2** |
| sustained sum-norm over whole sweeps | 1 | **1** |
| amplitude supports escaping the cone | 0 | **0** |
| coins realising the cone radius, per attainment depth | ≥576 at all 8 | **exactly 576 at all 8** |
| attainment depths no coin fills site-for-site | 2 | **2** (depths 5 and 7) |
| depths reflected under the reversed parity order | 16 of 16 | **16 of 16** |
| radii moved under that reversal (either norm) | 0 | **0** |
| asymmetric x-range depths | 16 | **16** |
| every closed size saturates / becomes visible | true / true | **true / true** |

The **parity-reflection self-test is real**: reversing the schedule to
`(X-ODD, X-EVEN, Y-ODD, Y-EVEN)` reflects the x-range at every one of the 16
depths and moves no radius in either norm. The **c-is-a-maximum-not-a-bound**
claim is earned: the sum-norm radius equals the tick number exactly at every
depth, and 576 coins of the carrier realise that radius dynamically at every
attainment depth. The `MAX-NORM-SUSTAINED=1/2` figure is correct and correctly
scoped to whole sweeps (the instantaneous max-norm ratio is 1 at tick 1).

The separation from R4b's group speed is a genuine separation, not a hedge: the
objects live on different sets (dual torus vs site set) and only one of them
needs the identification. No complaint.

---

## 2. The stability split — REPRODUCED

| quantity | published | mine |
|---|---|---|
| shapes present in both core arenas (P-9, T-8) | 16 | **16** |
| core comparisons / mismatches | 10240 / 0 | **10240 / 0** |
| ladder comparisons / mismatches | 650 / 0 | **650 / 0** |
| dynamic rows | 64 | **64** |
| sufficiency violations | 0 | **0** |
| measured slack (agreement without the condition) | 4 | **4** |
| unmoved / moved | 54 / 10 | **54 / 10** |
| T-DYNAMIC, all 8 rows | — | **identical** |
| T-HORIZON, all 8 rows | — | **identical**, and monotone |
| winding cycle at any open size | absent, 6 of 6 | **absent, 6 of 6** |
| winding observable moves across adjacent closed sizes | 8 of 10 | **8 of 10** |
| displacement classes, open vs closed | 1 vs 13 | **1 vs 13** (586 / 8320 walks, 0 / 3420 nonzero) |
| T-FAMILY, all 9 rows | — | **identical** |
| control arms moved / unmoved / wrong side | 4 / 1 / 0 | **4 / 1 / 0** |

The horizon condition is genuinely **predicted before the values are read** —
`predicted_agreement` touches only the cone, the closure rule and the partner
relation, never an amplitude — and it is **sufficient and not necessary**, with
the 4 slack rows published rather than hidden. That is the right shape for a
causal-horizon claim and the unit does not overreach it.

The tester really is blind: `stability_tester` is bare equality and is the same
call on all five arms. The one `UNMOVED` arm and the four `MOVED` arms all land
on the side declared for them.

---

## 3. The closure census — verdicts reproduce, but see MAJOR-1 and MAJOR-2

All 18 rows of T-CENSUS reproduce cell for cell, including the two the mandate
singles out:

- **merging index 1 at every open R — TRUE.** All 7 open sizes realise all 8
  constant twists (measured by propagation over each arena's own links), so the
  index is 1 and 0 orbit pairs merge, at every open size. The closed index is
  $8/\gcd(L,8)$ at every one of the 6 closed sizes — 8, 2, 8, 4, 8, 1 — so the
  patch's value is the closed value **only** where the phase order divides the
  size, exactly as the paper states. All 13 T-GAUGE rows reproduce.
- **The R4 translation family is EMPTY on a patch — TRUE.** 9 of 9 declared
  axes are bijections on T-4 and 0 of 9 on P-9; the translations carrying the
  link set to itself number 16 on T-4 and **1** on P-9 (the identity). A family
  defined by covariance under a group that is trivial is empty, not smaller.
- POT's closed form and area-blindness survive the flush with **0 failures of
  10240 checks and 0 disagreements of 5120 equal-perimeter comparisons** — and
  I confirm the same on the closed arena. The fit is genuinely constraining:
  three constants fitted at $P\in\{2,3,4\}$ and checked at $P\in\{5,6,7,8\}$
  over all 16 shapes, per coin.
- Verdict counts 9 verbatim / 1 scoped / 8 artifact, and the scoped row is
  LAW-STRATIFICATION with the even-torus/odd-torus split (open residual 0,
  closed residual 6 = two non-matching strata at each of T-3, T-5, T-7).
  Correct.

---

## 4. The formulation gate — REPRODUCED

10 of 18 quantifiable, 8 named exceptions, the same 8 identifiers
(LAW-LINK-COUNT, LAW-PLAQUETTE-COUNT, LAW-WINDING-FAMILY, LAW-HOMOLOGY,
LAW-MERGING-INDEX, LAW-PARENT-ORBITS, LAW-TRANSLATION-COVARIANCE,
LAW-DUAL-TORUS). The directed system: 5 open sizes (P-5…P-9), 16 shapes × 5
coins × 5 sizes = **400 comparisons, 0 not carried**, directed under inclusion.
The gate is a pure function of the census verdicts, so it inherits MAJOR-1 and
MAJOR-2 and nothing else.

---

## 5. Template conformance — REPRODUCED

I parsed `era_template.py`'s `FAMILIES` table with my own regex (9 rows:
T-SEAL-PROMOTION, T-TRANSCRIPT-BOUND, T-WALL-SEMANTIC, T-ANCHOR-CONSUMED,
T-CLAIMS-EQUAL, T-REFERENT-BOUND, T-NO-TYPED-COUNTS, T-FALSIFIER-POISONS,
T-READ-SET) and the nine `CHECK = "T-…"` constants carried by the instrument's
classes. **Set-equal, 9 = 9.** Adoption is a measurement here, as claimed. (The
adversarial audit of what those nine mechanisms *do* is K3's seat; I checked
only that the identifiers are parsed and equal — and, in MAJOR-3, one place
where family (g) does not reach.)

---

## 6. Anchors, inheritance and rendering — REPRODUCED

- **18 of 18 verbatim windows** located exactly once in their pinned source
  under whitespace/markdown normalisation, and present in the paper's own
  rendering. No window is quoted from a source it does not appear in.
- **30 of 30 path-value anchors** re-read by me directly from
  `pot_receipt.json`, `act_receipt.json`, `r5_gauge_receipt.json` at HEAD:
  every one carries the value the instrument requires. 0 mismatches.
- The verdict head is **byte-identical in the paper and in the output**, length
  1739 both, matching the gate.
- **106 of 106** markdown table rows in the paper appear in the output;
  **18 of 18** licensed claim sentences appear in the paper.

---

## 7. MAJOR-1 — six of the nine `SURVIVES-VERBATIM` rows are decided by construction, not measured

**The paper's rule** (§"The closure-artifact census"): *"Every sealed law this
unit uses goes through one classifier that sees only the law's residual on the
open arena and its residual on the closed one. A law whose two residuals agree
survives the flush verbatim."* The instrument's own docstring is stronger:
`arena_residuals` returns *"quantities that are a property of ONE arena, so
that a census row never compares a number with itself"* (`hor_exact.py:2980`).

**The measurement.** I swept each witness over **all 13 declared arenas** of
both ladders. Three of them take exactly one value over the whole universe, and
three more are computed with **no arena argument at all**:

| row | witness | value set over all 13 arenas | why it cannot move |
|---|---|---|---|
| LAW-LINK-OPERATOR | `arity + leak` | `{0}` | a link's two ends differ for any $n\ge2$; the tick writes only to arena sites |
| LAW-SINGLE-OCCUPATION | `leak` | `{0}` | `tick_once` writes only keys of `arena.links()` |
| LAW-REFINEMENT-PLACES | `len(links) − len({("MID",l)})` | `{0}` | the map `l ↦ ("MID",l)` is injective on a list of distinct links |
| LAW-COIN-FAMILY | `len(coins)` | 640 | the same argument is passed to both calls |
| LAW-RECTANGLE-FAMILY | `len(shapes)` | 16 | the same intersection list is passed to both calls |
| LAW-CLASS-COUNT | `len(full)` | 136 | `full = twist_orbits(coins, cidx, range(8))` is computed **once**, with no arena |

For contrast, the artifact rows are genuine: `thin` (LAW-LINK-COUNT) takes 8
distinct values over the same 13 arenas and `nop` (LAW-PLAQUETTE-COUNT) takes
8.

**Consequence.** The headline *"9 survive the flush verbatim"* is carried by
**three measured rows** — LAW-HOLONOMY, LAW-CLOSED-FORM, LAW-AREA-BLINDNESS —
and six rows on which the classifier could not have returned anything else. At
those six rows the census literally compares a number with itself, which is the
thing its own docstring says it is built to prevent. The individual *verdicts*
are all defensible (the coin family and the full-stencil class count really are
arena-independent; that is their content) — the defect is that the row is
presented as a measurement and the count 9 as a measured tally.

**Repair (liftable, no physics number moves).** Add a fourth verdict word for
witnesses that are arena-independent by construction — e.g.
`INVARIANT-BY-CONSTRUCTION` — and publish the census as **3 measured-verbatim /
6 invariant-by-construction / 1 scoped / 8 artifact**, with the quantifiability
gate unchanged at 10 of 18. Alternatively, give each of the six a witness that
an arena can move (for LAW-CLASS-COUNT that witness is the orbit count under
the arena's own realisable twists — but that is already LAW-PARENT-ORBITS and
reads ARTIFACT, which is itself the informative fact). The first option is the
honest minimal fix and I recommend it.

---

## 8. MAJOR-2 — two of the eight `CLOSURE-ARTIFACT` verdicts are comparison-size-selected and flip against the unit's own core torus

**The measurement.** The census does not use one closed arena. Ten rows take
their closed witness at **T-8** (`CORE_TORUS`, the arena used for the
residuals, the closed form and the contractible sweep); eight take it at
**T-4** (`PV-POT-L`, the parents' declared size). For six of those eight the
choice is immaterial. For two it is decisive:

| row | open (P-9) | closed at T-4 | verdict as published | closed at T-8 | verdict there |
|---|---|---|---|---|---|
| LAW-MERGING-INDEX | 1 | 2 | CLOSURE-ARTIFACT | **1** | SURVIVES-VERBATIM |
| LAW-PARENT-ORBITS | 136 | 208 | CLOSURE-ARTIFACT | **136** | SURVIVES-VERBATIM |

Both numbers are mine, measured by propagation over T-8's own links: 8
realisable twists, index 1, 136 orbits, 0 merged — identical to every open
size. Had the census used its own core closed arena throughout, the headline
would read **11 verbatim / 1 scoped / 6 artifact**, and the formulation gate
**12 of 18 quantifiable with 6 named exceptions**.

**This is not a claim that the verdicts are wrong.** The right justification is
available inside this unit's own T-GAUGE table: the closed merging index is
$8/\gcd(L,8)$ — it takes 4 distinct values over the 6 closed sizes — while the
open index is 1 at every size, so *no closed value exists to be quantified over
horizons*, and ARTIFACT is correct. But that is **not what the classifier
consumes**; it consumes one pair of integers taken at two different sizes, and
that pair reverses if the closed size changes to the one the rest of the census
uses.

**Repair (liftable, verdict unchanged, and it makes the verdict earned).** Give
these two rows the *set* of closed values over the declared ladder
($\{8,2,8,4,8,1\}$ and the corresponding orbit counts) against the *set* of
open values ($\{1\}$, $\{136\}$), and classify on set-inequality. Additionally,
disclose in the paper that the census's closed side is T-8 for ten rows and T-4
for eight — at present a reader reasonably assumes one closed arena, and the
paper's own §"The open patch and its gauge group" says the patch "sits exactly
where a closed arena sits when the phase order divides its size", which is
precisely the case the census then declines to compare against.

---

## 9. MAJOR-3 — a published totality count is wrong in both delivered artifacts

**The truth on disk.** `hor_receipt.json` has **56** top-level keys (raw parse,
no duplicate keys). Its own `seal_manifest` partitions them exactly: **47
sealed + 8 declared-unsealed + `seal_manifest` itself = 56**. I recomputed the
partition and the residue `set(keys) − sealed − unsealed` is `{'seal_manifest'}`
and nothing else.

**What is published.**

| where | published_keys | sealed |
|---|---|---|
| sealed `seal_shape` block in the receipt | **57** | **48** |
| G-SEAL-TOTALITY line in the promoted `hor_output.txt` | **58** | **49** |
| truth (the receipt's own manifest) | 56 | 47 |

Three different numbers for one quantity, two of them published under the seal
and in the transcript, none equal to the artifact on disk, and the two
published pairs disagree with **each other**.

**Mechanism.** `hor_exact.py:4737-4738` builds the sealed block as
`"published_keys": len(payload) + 9` and `"sealed": len(SEAL.seals) + 8`, and
`:4760` re-evaluates the *same two expressions* for the gate's evidence string
after two more entries have been added — hence the extra +1 on each. These are
typed offsets over a measured count, exactly the class E-31 engraves against
("no typed counts anywhere the unit vouches"), and the gate line's numbers are
the ones that end up in the promoted transcript.

**Why the unit's own gate cannot see it.** `CountRegistry.audit_module`
(`:672-689`) walks the AST for calls to `stmt`/`claim`/`gate` and inspects
**only `ast.Constant` string arguments**, searching their text for digits. A
numeral typed into the *value expression* that fills a `%d` is never examined.
So `G-NO-TYPED-COUNTS` reports `typed-numeral offenders 0` while two typed
offsets are producing wrong published counts a few hundred lines away. The
engraving is "no typed counts anywhere the unit vouches"; the implemented check
is "no typed digits inside published statement strings".

**Scope, in the unit's favour.** The gate's PASS predicate is sound — it is
`not undeclared`, computed from the live key set — so the *partition* really is
verified and no key is unaccounted. Only the published cardinalities are wrong.
No physics number is affected.

**Repair.** (i) Publish `len(payload)` at the door, after every key is in
place, and derive `sealed` from the manifest partition rather than from
`len(SEAL.seals) + 8`. (ii) Extend `audit_module` to flag any `ast.Constant`
integer appearing anywhere in the argument expressions of `stmt`/`claim`/`gate`
— that is a five-line change and it would have caught this. Same class,
elsewhere in the file: `totals["gates"] = len(LD.rows) + 5` happens to be right
(44 = the 44 `[PASS]` lines) and `runtime_inputs["declared"] = len(SOURCES)+1`
is overwritten before publication; both should still be derived.

---

## 10. A probe the unit does not run, on an axis it declares free — IT PASSES

RUNBOOK §15 requires quantities promoted to findings to be gated invariant
across the declared free axes, and this unit declares "the start place's parity
class" among them but sweeps only the even class (`even_c`). I ran the cone
census from the **odd** class and from a **mixed** start:

| start | c (sum) | attained | product box | cone sizes | sustained max-norm |
|---|---|---|---|---|---|
| even (the unit's) | 1 | 16/16 | all | 2,4,8,16,…,256 | 1/2 |
| odd | 1 | 16/16 | all | **identical** | 1/2 |
| mixed (x odd, y even) | 1 | 16/16 | all | **identical** | 1/2 |

Only the *direction* of the asymmetry flips (x-forward/backward becomes
backward/forward) — which is exactly the quantity the paper already reports as
arena-relative. **The unit's §15 claim survives a probe it did not run.** I
record this as a positive finding.

---

## 11. Minors

**MINOR-1 — the threshold sentence is a false universal.** The paper states:
*"the largest extent that stays simple is the size less one, on both
closures."* Measured over both declared ladders, the identity **fails at 7 of
13 rows** — T-6, T-7, T-8, P-6, P-7, P-8, P-9, where the largest extent that
stays simple is 4, the declared shape cap, not $n-1$. The instrument's gate is
honest (it restricts to the 4 rows the ladder can bind and prints "sizes
binding the identity 4"); the paper drops the restriction, and the sentence
carries no numeral so the numeral sweep cannot catch it. *Repair:* "at every
size the declared shape family can bind it ($n\le5$), the largest extent that
stays simple is the size less one" — 6 of 13 rows satisfy it, 7 cannot test it.

**MINOR-2 — `RECT_MAX` is defined twice.** `RECT_MAX = 3` at
`hor_exact.py:1218`, inside the block that presents itself as the declared
ladders, and `RECT_MAX = 4` at `:2025`. The second silently wins at import, and
it is the constant that fixes the entire shape family and therefore 16, 10240,
5120, 650 and 400. A dead declaration that would move every one of those
numbers if the order changed should be deleted, and the live one moved into the
declared-ladder block.

**MINOR-3 — G-TRANSCRIPT-BOUND's evidence is not a comparison.** `:4808-4809`
renders `"ledger rows %d, transcript gate lines %d"` from `len(LD.rows) + 1`
**twice**, so the two numbers it displays as a reconciliation can never differ.
The real reconciliation happens inside `TRANSCRIPT.bind`; the evidence line is
decorative. *Repair:* print each count from its own object.

**MINOR-4 — the seal chain excludes the falsifier gates.** 44 gates fire; the
sealed `gates` list, `gate_digests` and `ledger_shape.rows` cover **42**. The
two omitted are exactly `G-FALSIFIER-MOVES` and `G-FALSIFIER-COVERAGE` — the
rows that vouch the 43-mutant battery. This is declared in the code and
`totals.gates`/`coverage.gates` do carry the true 44, so it is disclosed rather
than hidden; but the digest-chained record does not cover the falsifier
evidence, and `ledger_shape.rows = 42` sits beside 44 `[PASS]` lines in the
promoted output with no note in the paper.

---

## 12. Things I attacked and could not break

- The 640-coin family and its three vanishing patterns: a theorem, and true
  per coin, not per tally.
- $c = 1$ site per tick: not a bound, a maximum, attained at every censused
  depth and realised dynamically by 576 coins at every attainment depth.
- The cone's product-box shape and its behaviour under schedule reversal.
- The causal containment: **0** amplitude escapes across both sweeps, including
  the full 640-coin sweep at depth 8.
- 10240 + 650 contractible comparisons at **0** mismatches — the strongest
  single result in the unit, and it reproduces on an independent holonomy
  route.
- The sufficiency/necessity structure of the horizon condition, with its 4
  published slack rows.
- Winding absent at every open size, and 1 vs 13 displacement classes from an
  exhaustive walk census (586 vs 8320 closed walks).
- The blind one-tester control arms.
- The patch gauge group at every open size, and POT's closed form and
  area-blindness on an arena with no identification.
- The directed system's 400 carried values.
- Every anchor, every inherited path value, every parent digest, the head
  string and the paper-to-output rendering.

---

## 13. Licensed replacements

If the adjudicator lifts the repairs, these are the exact replacements. No
physics number moves.

1. **Census verdict column** (MAJOR-1): six rows — LAW-LINK-OPERATOR,
   LAW-COIN-FAMILY, LAW-SINGLE-OCCUPATION, LAW-RECTANGLE-FAMILY,
   LAW-CLASS-COUNT, LAW-REFINEMENT-PLACES — become
   `INVARIANT-BY-CONSTRUCTION`; the census sentence becomes *"Of the 18 sealed
   laws this unit uses, 3 are measured to survive the flush verbatim, 6 are
   invariant by construction and survive it trivially, 1 survives with a stated
   proviso and 8 were carried by the identification alone."* The head segment
   `18-SEALED-LAWS:9-VERBATIM-1-SCOPED-8-ARTIFACT` becomes
   `18-SEALED-LAWS:3-MEASURED-VERBATIM-6-INVARIANT-BY-CONSTRUCTION-1-SCOPED-8-ARTIFACT`.
2. **Two census rows** (MAJOR-2): LAW-MERGING-INDEX and LAW-PARENT-ORBITS
   publish the closed *value set* over the declared ladder against the open
   one, and the paper gains one sentence disclosing that the census's closed
   side is T-8 for ten rows and T-4 for eight.
3. **Seal accounting** (MAJOR-3): `published_keys` → 56, `sealed` → 47, both
   derived at the door; the G-SEAL-TOTALITY evidence line re-rendered from
   those; `audit_module` extended to integer constants in argument
   expressions.
4. **Threshold sentence** (MINOR-1): scoped to the sizes the declared shape
   family can bind.
5. `RECT_MAX` deduplicated (MINOR-2); G-TRANSCRIPT-BOUND evidence rendered from
   two objects (MINOR-3); one sentence in the paper's scope block noting that
   two gates fire after the ledger seals (MINOR-4).

---

## 14. Ruling

**AWF.** The physics is right and it is right on an independent rebuild: the
emergent speed, the cone, the split, the artifact census's *content* and the
formulation gate all reproduce exactly, 616 for 616. The verdict word stands.
What needs fixing is the census's **bookkeeping of its own evidence** — six
rows that cannot fail and two whose failure is size-selected — and one
published count that is simply wrong in both delivered artifacts. All three
repairs are liftable without re-running the physics; two of them change
published counts about the census, not about the arena.

**Between delivery and adjudication every reading above is a candidate
reading.**
