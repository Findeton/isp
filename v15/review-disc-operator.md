# DISC (paper-47) — K1 OPERATOR review

**Seat:** K1 OPERATOR, three-seat hostile panel, v15 DISC.
**Object, hash-verified at open and at close:**

| file | sha256-12 (open) | sha256-12 (close) |
|---|---|---|
| `v15/paper-47-disc.md` | `b12c4c67bac8` | `b12c4c67bac8` |
| `v15/code/disc_exact.py` | `1d98d618c6bc` | `1d98d618c6bc` |
| `v15/code/disc_output.txt` | `dc79343de5d0` | `dc79343de5d0` |
| `v15/code/disc_receipt.json` | `c745ef39fded` | `c745ef39fded` |
| `v15/note-disc-pin.md` | `dbe7b26bb0d0` | `dbe7b26bb0d0` |

Parents verified at their pinned bytes as the paper declares them:
`v14/paper-20-coupling.md` `4824d190af73`, `v14/paper-34-act.md` `d933221780ed`,
`v14/paper-36-pot.md` `1e495318252d`, `v14/paper-39-ndep.md` `e2293b8c3858`,
`v14/code/era_template.py` `d04a3eb58fbc`. All five match the paper's
inheritance block. Authority read: HANDOFF-PROMPT §4/§9, RUNBOOK through E-33,
v15/PLAN.md (W1/W2 and the v15 #2 reclassification), v15/LOG.md #2–#5.

**Method.** Everything below was rebuilt from the parents' definitions in a
scratch tree with **no code, no constant and no intermediate shared** with
`disc_exact.py`: my own Z[ζ₁₂] (reduction table derived by iteration, then
cross-checked against an independent numeric evaluation, 1,603 checks, 0
failures), my own Z[ζ₈], my own arena, coin census, both walks, both lattice
carriers. Where the object under test uses one traversal I used another (the
tick-*t* ensemble accumulated from the level-(*t*−1) frontier rather than from
the materialised level-*t* frontier; holonomies by dense matrix product and by
uniform-scale row update, cross-checked 48/48). Repo access was read-only; this
file is the sole write.

**Between delivery and adjudication every headline here — the object's and
mine — is a candidate reading.**

---

## GRADE: **ACCEPT WITH FIXES (AWF)**

**Zero false numbers.** Every recomputable value in the paper is exactly right:
54 published numerals independently re-derived (26 fractions, 28 multi-digit
integer measurements), **0 discrepancies**, across 132,187 individual
recomputations. The primary result — the demotion census — survives intact, row
by row, and is the strongest thing in the unit.

Three MAJORs, all repairable without re-running anything, and none of them a
computational error. Two touch the head, one touches the front matter. The
grade is AWF rather than A because MAJOR-1 shows the verdict word's own tick
number moving on a parent-declared axis the paper never names, while §11 asserts
in terms that it does not move.

---

## What reproduced, exactly

Every one of these was computed from the parents' definitions by an independent
implementation and compared afterwards. Nothing below was tuned to agree.

### The ablation effect and its values

| claim | paper | my rebuild |
|---|---|---|
| AG(2,3) tick-3 ISP site row | `1/81, 68/729, 116/729, 32/729, 0, 2620/19683, 32/729, 1324/19683, 8800/19683` | identical |
| AG(2,3) tick-3 null site row | `1/81, 68/729, 116/729, 32/729, 0, 116/729, 32/729, 68/729, 32/81` | identical |
| AG(2,3) ISP / null IPR | `33596579/129140163` / `40411/177147` | identical |
| AG(2,3) total variation | `1024/19683` | identical |
| AG(2,2) tick-3 ISP site row | `9824/19683, 8480/59049, 12617/59049, 8480/59049` | identical |
| AG(2,2) tick-3 null site row | `32/81, 80/729, 281/729, 80/729` | identical |
| AG(2,2) ISP / null IPR | `43392899/129140163` / `58235/177147` | identical |
| AG(2,2) total variation | `10144/59049` | identical |
| tick-3 branch counts | 486 / 306 | identical |
| shots by Chebyshev at δ=100 | 36948 / 3389 | `⌈100/gap²⌉` = 36948 / 3389 |

The four fractions and both TVs are re-derived, not merely re-checked against
the published site tables. §6's structural sentence also holds: at the larger
plane the two rows agree at six of nine sites, the parting is confined to
(1,2), (2,1), (2,2), and the moved probability is −512, −512, +1024 over 19683,
summing to zero.

### The agreement census and the sweep

| claim | paper | my rebuild |
|---|---|---|
| fiber points | 372 | 372 (2·4·3·2 + 6·9·3·2) |
| site-by-tick checks through tick 2 | 6216, 0 violations | 6216, **0 violations** |
| interfering points first differing at tick 3 | 294 of 294 | 294 of 294 |
| scalar-coin points never differing | 78 of 78 | 78 of 78 |
| row split | 24 / 24 / 270 / 54 | identical |

PR3 verified **structurally**, not by assertion: at every one of the 372 points
the sweep constructs one coin object and passes that same object to both arms
(`disc_exact.py:1560–1568`). The null is handed ISP's coin at every fiber point.
The anti-strawman rule holds — and see MAJOR-3, where it holds harder than the
paper claims.

### The paper-20 fidelity anchors

All four sealed parent quantities re-derived from paper-20's definitions:

| quantity | parent's sealed value | my rebuild |
|---|---|---|
| coupled branch ladder | 3 27 486 10527 284078 | identical |
| control branch ladder | 3 27 486 9234 212382 | identical |
| coupled inverse participation | `35971074413334039128803/239299329230617529590083` | identical |
| control inverse participation | `2306155/14348907` | identical |

The coin census also reproduces the parent's own fiber: the six classes at
AG(2,3) have b/a ∈ {0, −2/3, ω/3, (−1+ω)/3, (−1−ω)/3, (−2−ω)/3}, **exactly**
paper-20 §3.2's declared set, and the AG(2,2) census collapses to 4 solutions /
2 classes / 1 trivial with the non-trivial class ±Grover. The census is stable
at coordinate bounds 6, 9 and 12, so `bound=6` in `coin_census` is not
load-bearing — the "enumerated exhaustively" claim is sound (the a-priori bound
is |A|=3 and |B|≤2/3·|A|, both inside the box).

### The demotion census, row by row

| row | ruling | my measurement |
|---|---|---|
| POT perimeter-only law | REPRODUCED | **3200** equal-perimeter comparisons, **0** disagreements; the 1280 area-discriminating sub-basis also 0 |
| POT three-term closed form | REPRODUCED | **0** failures over **640** coins (3 coefficients fitted at P=2,3,4, verified at P=5,6, both components) |
| POT halving mode and gap | REPRODUCED | present at **512** of 640; the null's own coin fits (A,B,C) = (**2, −1, 1**) |
| POT plaquette counting expectation | REPRODUCED | **11** distinct values, expectation **13/10**, **56** non-flat diagonal coins |
| ACT off-diagonal quartic sign | REPRODUCED | distribution {−2: **144**, 0: **352**, +2: **144**}, counting expectation **0**; odd twists reverse it 2560/2560, even twists preserve it 2560/2560 |
| paper-20 coin-register restriction | REPRODUCED | link stencil: 6 differences at multiplicity 1, **18** unitary, **0** non-monomial over **50653** maps; collinear stencil: 2 differences at multiplicity 3, **216** unitary, **198** non-monomial |
| paper-20 walk at ticks 1–2 | REPRODUCED | 6216/6216 — but see MAJOR-2 on this row's status |
| paper-20 walk from tick 3 | NOT-REPRODUCED | confirmed; but see MAJOR-1 and MAJOR-3 |
| paper-39 connection modulus | NOT-REPRODUCED | confirmed: **5 distinct** IPRs over the 5 runnable moduli |
| paper-20 record-side observable set | NOT-EXPRESSIBLE | ruling correct: a definitional absence, and the paper says so; not a discriminant |

The lattice coin family rebuilds independently: alphabet **25**, coins **640**,
sectors 64 diagonal / 64 antidiagonal / 512 balanced.

### The m = q descent and the modulus observable

| leg | paper | my rebuild |
|---|---|---|
| descent over moduli 1–12 × orders {2,3,5,7} | m = q at every order | q=2→[2], q=3→[3], q=5→[5], q=7→[7] |
| AG(2,2) tick-3 IPR, m = 1 / 2 / 3 / 4 / 6 | `58235/177147`, `43392899/129140163`, `4680635/14348907`, `41546723/129140163`, `41655923/129140163` | identical, **5 of 5 distinct** |
| branches, m = 1 / 2 / 3 / 4 / 6 | 270 / 306 / 324 / 324 / 324 | identical |
| m = 12 | leaves the rationals | confirmed: Born weights land in Q(√3) |

Separating the two conditions: `descends` selects exactly the divisors of q and
`separates` selects exactly m ≥ q, at all four orders. See MINOR-4.

### The instrument

`--no-write` reproduces `disc_output.txt` **byte-identically** (sole difference:
the trailing `NO-WRITE:` line), exits 0, writes nothing — `git status` clean for
every DISC file after the run. The single fenced block in the paper equals the
receipt's derived head, 1587 characters, by string equality. 36 gates, all PASS;
34 carry falsifiers, 2 carry waivers, 0 sentinels. The `+1` on `shots3` at
line 2211 is inside `mut("MUT-FALSIFIER")` and is not delivered behaviour.
`k_shots`'s published description matches its code (E-23): variance bounded by
1/4 gives P ≤ 1/(Nδ²), so N ≥ C/δ² is the stated guarantee.

### One ungated account, corroborated

§8's explanation of the tick — that it is the closure time of the arena's
elementary triangle — is registered as unproved and ungated, and §14 asks a
successor to prove it or find the arena where it fails. I built the
discriminating test:

| declared directions | closed under addition? | first difference |
|---|---|---|
| (1,0), (0,1), (1,1) — the declared set | yes, d₁+d₂ = d₃ | tick **3** |
| (1,0), (0,1), (1,2) | yes, d₂+d₃ = d₁ | tick **3** |
| (1,0), (0,1), (2,2) | **no** two-shift path returns to a one-shift site | tick **4** |

The account is right, and the mechanism is the one §8 names. This is
corroboration the unit did not have and can be lifted into §8 or §14 as a
measurement.

---

## MAJOR findings

### MAJOR-1 — the headline tick moves on a parent-declared, parent-flagged verdict-relevant axis that the paper never names

**Establishing measurement.** paper-20 item `F6-COIN-ORDER` is stamped
**DECLARED-VERDICT-RELEVANT**, fiber 2 (G·D against D·G), and paper-20 §11 and
§13.4 both price it. DISC inherits paper-20's walk wholesale and silently fixes
F6 = G·D. Rebuilding the other member from paper-20's own definition — the count
phase applied *after* the coin, which paper-20 characterises by
|D·Gψ|² = |Gψ|² — gives:

| arena | coin order | first difference | tick-3 distribution |
|---|---|---|---|
| AG(2,3) | G·D (delivered) | tick 3 | `1/81 … 8800/19683` |
| AG(2,3) | **D·G** | **tick 4** | **equals the null's exactly** |
| AG(2,2) | G·D (delivered) | tick 3 | `9824/19683 …` |
| AG(2,2) | **D·G** | **tick 4** | **equals the null's exactly** |

The mechanism is paper-20's own and is clean: under D·G the emission menu is
stage-blind, so the record cannot enter that step's Born weights, and the whole
effect is displaced by exactly one tick.

**Why this is a MAJOR.** The verdict word is
`RECORD-BACKREACTION-DETECTED-AT-TICK-3` and §11 states "the sweep shows that
the tick at which the two models part does not move with any declared axis."
Read against the declarations this unit inherits, that sentence is false: the
tick moves from 3 to 4 on a fiber the parent declared, ran, and stamped
verdict-relevant. RUNBOOK §15 is explicit — claims of significance only for
quantities gated invariant across declared free axes, else arena-relative. The
tick is order-relative. I checked the neighbouring axes so the finding is
bounded: the orientation fiber (−l shift) is **inert** on both the tick and the
tick-3 IPR at both arenas, so F6 is the one that moves it.

**Exact repair.** (a) In §6 and §11, replace "any declared axis" with the axis
list the sweep actually covers, and add F6 to it as a measured row: at the
alternative coin order the first difference is at tick 4 at both planes and the
tick-3 distribution equals the null's. (b) Either scope the head word — e.g. an
`ORDER=G-DOT-D` clause alongside the existing `SCOPE=` segment — or widen the
sweep by the F6 fiber and report the tick per member. (c) Add F6 to §12's "Not
decided" list. No measurement in the paper changes.

### MAJOR-2 — the primary census's headline number contradicts §12, and its seventh row is not a parent result

**Establishing measurements.** (i) The front matter (line 36) reads "the seven
reproductions are the primary result: they say that **seven of the corpus's own
sealed results** do not distinguish this theory from a plain coined walk."
§12's first bullet reads "Seven of the ten tested results are reproduced …
**Six of them are sealed results of three parents**, and none of the six
distinguishes this theory from a plain coined walk." These two sentences
contradict each other, and §1 sides with §12 by listing six.

(ii) The seventh row — "paper-20 the walk's distribution at the first two
ticks" — is not a result paper-20 states. `grep -c "first two ticks"
v14/paper-20-coupling.md` returns **0**; paper-20 publishes the branch ladder,
the support schedule and horizon-5 observables, never a tick-1 or tick-2
distribution. The row is constructed by this unit.

(iii) Rows 7 and 8 are complementary halves of a **single** parent observable
(paper-20's site distribution p_t(x)): ticks 1–2 in the numerator, ticks ≥3 in
the denominator. Counting p_t(x) once, the census reads 6 reproduced / 2 not /
1 not-expressible over **9** rows, not 7 of 10.

**Why this is a MAJOR.** "7 of 10" is the head, the section title, the §2 count
and the paper's declared primary result. It is construction-relative in two
independent ways, and the paper already knows one of them in §12 while asserting
the opposite in the front matter. The underlying finding — six sealed results of
three parents do not distinguish this theory from a plain coined walk — is
strong, correct, and needs none of this.

**Exact repair.** (a) Line 36: "seven of the corpus's own sealed results" →
"six of the corpus's own sealed results, together with a seventh row this unit
carved out of the walk's own distribution". (b) In §2's table, mark row 7 as
carved from the same parent observable as row 8, or merge them into one row with
a two-part ruling. (c) State the census both ways in §2 — 7 of 10 as tested
rows, 6 of 9 as parent results — so the head's number is defined rather than
chosen.

### MAJOR-3 — the null is provably identical to paper-20's own frozen-stage control on the compared observable, and this is not disclosed

**Establishing measurement.** The frozen control holds n ≡ 1, so D_t(x) = ζ_q·I
at every site and C_frozen = ζ_q·G — the null's coin times a global phase.
Hence every frozen branch carries the null's state up to phase and the ensemble
distribution is the null's, at every tick. Measured over all 372 fiber points ×
3 ticks: **1116 equal, 0 unequal**. Independently, my frozen horizon-5 arm
returns tick-3 IPR `40411/177147` — the null's own value — while the delivered
run's own fidelity leg reports the frozen control's max cell count as 1.

**Why this is a MAJOR.** It cuts both ways and both matter.

*In the paper's favour, decisively:* the null is not an opponent invented here.
It is the parent's own **mandatory** control, on the observable being compared.
That is a far stronger anti-strawman statement than PR1–PR7 make, and the paper
should be claiming it.

*Against the paper's framing:* the NOT-REPRODUCED row is then paper-20's
already-sealed `G-NONTRIVIALITY=PASS` ("18 of 18 declared-observable rows differ
from the mandatory frozen-stage control") restricted to the p_site row. That the
record layer moves the walk's distribution is not new. What *is* new, and is
genuinely this unit's, is **when** (tick 3), **by how much** (exact site values
both planes), and **how universally** (294/294 interfering points, never at the
78 scalar points). §12's "Not decided" bullet says the null is memoryless; it
does not say the null is the parent's control, which changes what the
ablation-effect row is evidence *for*.

**Exact repair.** Add to §5 (which already quotes the control) two sentences:
the identity with its one-line proof, and its consequence — that the ablation
row localises and quantifies a difference the parent had already established at
horizon 5, and that this is what makes the null unimpeachable rather than what
makes the row new. Adjust the §12 bullet accordingly. Nothing measured changes.

---

## MINOR findings

**MINOR-1 — the gap row's ratio cannot fail.** The "gap reproduced" ruling is
carried by "the ratio the fitted halving term actually carries between
consecutive perimeters", gated as `ratio 1/2`. That ratio is
C·2^−(P+1) / C·2^−P = 1/2 identically, for any non-zero C: it is the ansatz's
own basis function, not a measurement. The row's entire load is the presence
bit (C ≠ 0), which is real and is falsified by `MUT-GAP`. paper-20 §6 sets the
corpus precedent of stamping rows `contentful` vs `definitional`; this row
should carry the same stamp. *Repair:* in §10, say that the ratio is
definitional given a non-zero halving coefficient and that the measured content
is the coefficient's presence at 512 of 640 coins and at the null's own.

**MINOR-2 — the lattice null's coin is an unnamed declaration.** PR3 selects the
null's coin by identity with ISP's, but the lattice carrier has no ISP coin —
it is all 640. The instrument fixes the null's lattice coin to the **Hadamard**
coin (`disc_exact.py:1879`), which the paper never names; §10's column reads
only "the null's own coin". *Repair:* name it in §10 and state that on the
lattice PR3 cannot select, so this is a declaration with the fiber left unswept.

**MINOR-3 — the two-route null corroboration is uncarried and its coverage is
unstated.** `null_two_routes` seals 39 checks, 0 violations, but "39" does not
occur in the paper and the routes are compared at **one** point per arena
(origin, direction 0, Grover — the only rational-integral coin), i.e. 2 of the
372 fiber points. I reproduced the agreement (my own two null routes agree at
45/45, their 39-check scheme at 39/39, 0 violations). *Repair:* carry the number
into §13 with its coverage stated, since the integer route is available only at
integral coins.

**MINOR-4 — the descent's sweep is decoration on a two-line lemma.** The
computed predicate reduces exactly to: `descends` ⟺ m | q, `separates` ⟺ m ≥ q,
hence m = q. I confirmed both equivalences at all four orders. Primality enters
nowhere in the computation — only in the interpretive claim that the additive
group is cyclic — and the same predicate returns m = q at composite q too. §9's
"At every prime field order swept, one modulus survives both conditions" reads
as a swept empirical finding. *Repair:* state the lemma (m | q and m ≥ q ⟹ m = q)
and present the four orders as instances, keeping the prime-power opening where
it is.

**MINOR-5 — the two waivers' forcings are existence checks.** `G-SCOPE-DECLARED`
is forced by `len(declared_free_axes) > 0` and `G-READS-DECLARED` by
`reads > 0`. Neither forces the claim a waiver owes under #34 — that the gate
has no corruptible measured predicate. They are true but do not do the work.
*Repair:* replace with forcings that bind the absence (e.g. that the scope row's
every field is carried into the head string that `G-VERDICT-EQUALITY` compares).

**MINOR-6 — "the arena's own ring" is imprecise.** The census ring is
(1/3)Z[ζ_q]; the 1/3 is the *register's* dimension, not the arena's, and at
q = 2 the ring reduces to (1/3)Z so the census is simply the rational one and
coincides with paper-20 §3.2's real-rational census. The code's docstring is
precise; §4 and PR3 are not. *Repair:* one clause in §4.

**MINOR-7 — the q=2 headline row mixes horizons inside one sealed object.**
`discriminant.q2` carries `horizon: 5` with `branches: 306` and `isp_dist` at
tick 3, while its `record_side` (`max_cell_count: 5`) is read off the level-5
frontier. Receipt-only; nothing in the paper is affected. *Repair:* split the
row or label the two ticks.

---

## Recomputation count (honest)

| bucket | recomputations |
|---|---|
| my ring primitives vs independent numeric route | 1,603 |
| coin censuses (2 arenas × 3 bounds) + class ratios vs paper-20 | 26 |
| headline distributions, IPRs, TVs, gaps, branches | 36 |
| fiber sweep: ISP and null runs over 372 points | 744 |
| agreement census, site by tick | 6,216 |
| first-difference determinations | 372 |
| paper-20 fidelity anchors (ladders + IPRs, both arms) | 12 |
| frozen-control vs null, tick by tick over the sweep | 1,116 |
| modulus rows (branches, IPRs, rationality) | 13 |
| m = q descent decisions (4 orders × 12 moduli × 2 conditions) | 96 |
| null two-route comparisons (my scheme) | 45 |
| ISP two-route comparisons (accumulated vs materialised) | 39 |
| lattice loop observables (640 coins × 9 shapes) | 5,760 |
| perimeter-law comparisons | 3,200 |
| area-discriminating comparisons | 1,280 |
| closed-form verification points | 2,560 |
| halving-mode decisions | 640 |
| plaquette values and non-flat classification | 1,280 |
| quartic-sign values | 640 |
| odd- and even-twist checks | 5,120 |
| stencil map evaluations (2 stencils × 50,653) | 101,306 |
| dense vs uniform-scale holonomy cross-route | 48 |
| §8 mechanism probe (3 direction sets) | 15 |
| F6 coin-order probe / F7 orientation probe | 16 |
| Chebyshev shot derivations | 2 |
| output byte-comparison, head-string equality | 2 |
| **total** | **132,187** |

**Published numerals independently re-derived:** 54 (26 fractions, 28
multi-digit integer measurements), **0 discrepancies**. The remaining prose
integers are section and paper references (7, 8, 9, 10, 12, 13, 14, 20, 34, 39,
47) and small declared counts (5 structures, 6/6 expressibility, 12 observables,
2 waivers, 3 walls, confidence denominator 100), all checked against the
receipt.

---

## Summary for the adjudicator

The arithmetic is clean end to end — 132,187 recomputations, 54 published
numerals, not one wrong. The null is honest and is in fact stronger than the
paper claims it to be (MAJOR-3). The demotion census, which the v15 #2 review
promoted to primary, holds row by row on independent rebuilds of three parents'
carriers, and it is the right result to lead with.

What needs fixing before this is terminal is confined to the positive half:
the verdict word's tick is order-relative and the paper says it is not
(MAJOR-1); the census headline "7 of 10" contradicts §12 and rests on a carved
row (MAJOR-2); and the null's identity with the parent's own control is
undisclosed in both directions (MAJOR-3). All three are edits to scope and
disclosure. No measurement in the paper moves, no gate needs to change its
verdict, and the instrument does not need to be re-run except to re-render.

Candidate until adjudication.
