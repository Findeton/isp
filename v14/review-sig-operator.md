# SIG / paper-24 — OPERATOR-LENS REVIEW (K1)

**Seat:** K1, operator lens (hostile). **Object:** commit `025c4a6`.
**Grade: ACCEPT-WITH-FIXES (AWF). Zero MAJOR. Four MINOR, none touching a
published number.**

**Object verified at start and at end** (sha256-12, recomputed from the
committed blobs, not from the working tree):

| file | declared | found |
|---|---|---|
| `v14/paper-24-sig.md` | `72175d6fa85b` | `72175d6fa85b` |
| `v14/code/sig_exact.py` | `a41b6d549e14` | `a41b6d549e14` |
| `v14/code/sig_output.txt` | `f28b550c151e` | `f28b550c151e` |
| `v14/code/sig_receipt.json` | `ca9cd4ceb387` | `ca9cd4ceb387` |
| `v14/note-sig-pin.md` (pin) | `ab73239daff5` | `ab73239daff5` |

Parents verified at their pinned bytes: paper-21 `ef4a8c35a0c4`, paper-20
`4824d190af73`, `coupling_exact.py` `72e7b299f66e`; and the other seven
declared sources (`a4538c7019e6`, `55273f6b6068`, `f286ba10d2d9`,
`542b8735daf0`, `93ea24591c3c`, `0cebe543e814`) all match. The GDL
quotation cited at commit `4c85ca4` is present in `v14/paper-25-gdl.md` at
that commit, whitespace-normalised.

**Method.** Everything below was rebuilt in a standalone library written for
this review from paper-20's *declared* machinery (coin `C(x) = G·D(x)`,
`D(x) = diag(ω^{n_l(x)})`, shift `|x,l> → |x+l,l>`, one non-selective
division event per step at the law-native kernel's weight). `sig_exact.py`
was read for semantics and audited, and was never executed or used as an
oracle: every number in this review comes from my own arithmetic (Python
ints, `Fraction`, `Z[ω]` as integer pairs).

**Recomputations: 342 published receipt values compared row by row, zero
disagreements** (`static`, `dynamic/profiles`, `dynamic/floors`,
`polarity/{A,B}/steps`, `polarity/arena_rows`, `forcedness/rows`,
`prune/rows`, `clearing`, `mod3`, `constraint_b`, `arena`), plus eight
censuses rebuilt from scratch and listed below.

---

## 1. What was independently reproduced

**The five parent anchor rows** (against paper-20's committed receipt, from
my own walk): exit probability `927415552/847288609443` (Born) and
`37440224/5811307335` (record); branch ladders `3, 27, 486, 10527, 284078`
and `3, 27, 486, 11664, 314928`; the exit census `{4,1,1: 379; 1,4,1: 471;
1,1,4: 466}` over all 1,316 inadmissible leaves, every one with exactly one
site out and excess `(0,0,3)`; the return-time row — support schedule
`1,3,6,8,9`, site `(0,0)` at steps `1,4,5`, site `(1,1)` at `2,3,5`,
**earliest third visit step 5**, and no fourth visit inside horizon 5 (which
is the A3 first-indefinite=6 bound). Three further parent rows my rebuild
also lands, unasked: the frozen-arm ladder `…, 9234, 212382`; the coin-fiber
leaf counts `284078 / 314627 / 214772 / 313842 / 192258`; and the alternative
coin order's exit `2922723584/847288609443` at `226404` leaves.

**The static ladder.** 280 partitions; **deposit theorem: max 1 incidence per
cell per round, max 2 per site**, incidence spectrum `0:1, 4:27, 6:54, 7:162,
9:36` — which I also verified is byte-for-byte paper-21's committed
`/family/incidence_spectrum`. R=1 unrestricted: the ROW parallel class
induces `(1,0,0)` at 9 of 9 sites, `4 det q = −1`, INDEFINITE. Floors over the
2,197-code box: cheapest full-site SINGULAR `(1,1,4)` (max 4, sum 6),
cheapest full-site INDEFINITE `(1,1,5)` (max 5, sum 7). Collinear ladder
`det4 = 3, 4, 3, 0, −5, −12, 12` with regions as published.

**R=5 non-attainment — the hardest object — by two independent routes.**
Pool of partitions hitting a fixed cell = **70**, multisets of five =
**16,108,764**. Route 1 (branch-and-bound over the 12,103,014 five-subsets;
repeats can only lose coverage, so the subset maximum is the multiset
maximum): max coverage **25**, hence **min uncovered 2**. Route 2 (exact
union-closure by level, dedup): max coverage `9, 16, 21, 24, 25, 26` for
k = 1…6 — the k=5 entry re-derives the same 25 by a different algorithm.
Combined with the theorem *covering ⇒ every site full ⇒ an indefinite site
needs a cell at 5 ⇒ all five rounds hit it*, the R=5 row is sound. The
full-site attainment **2,210,000** I re-derived in closed form from the
target-site profile census (10 · 10 · C(52,3)), a different route from the
delivered sweep, and the witness leaves **13 of 27** cells at zero.

**The covering floors.** R=4 both pools: NO by arithmetic. R=5 both pools: NO
by the sweep. R=6 ALL: YES — my own witness (six rounds, code `(1,5,1)`,
41 incidences), independent of the delivered one. **R=6 LIVE: NO** by my own
reduction (covering + indefinite ⇒ ≥5 of the 6 rounds hit the cell that
reaches 5; live pool per cell = 12) — 157,248 combinations, none covering
with an indefinite site. R=7 ALL and LIVE: YES, `ROW·COL·DIA^5` → `(1,1,5)`
at all nine sites, covering, foreign-pair-free, 63 incidences.

**The orbit licence, strengthened.** The delivered gate measures the orbit
size. I additionally verified the property the licence actually needs: the
deposit map **commutes** with the order-108 group (12 link-set-preserving
linear maps × 9 translations) at **30,240 checks, 0 failures**, and the
induced action on the 27 cells is transitive. Fixing one cell is genuinely
WLOG.

**The dynamic ladder.** A3 `(1,1,1)`, A4 `(1,1,2)`, A5 `(1,1,3)` at both
readings to horizon 5: every per-step Born and null mass in
`dynamic/profiles` and `polarity/*/steps` reproduced exactly, including
A4's `58985/59049 | 64/59049` at t=3 and `1146312331/1162261467 |
15949136/1162261467` at t=4, and A5's `367635432032/7625597484987` and
`269625780848/1016978783625`. First-occupancy steps `A3(sing 5, indef —)`,
`A4(3, 5)`, `A5(1, 3)` measured, and each is consistent with its own event
budget (`5−c` to indefinite, `4−c` to singular) *and* with the return-time
row: 2 events on one cell first possible at step 3, 3 events at step 5,
4 events at step 6.

**THE PRUNING AUDIT — closed decisively.** I re-derived the prune from the
region arithmetic (at A3 every cell stays ≥ 1, so by Heron a site is
non-POSDEF iff its max cell is ≥ 4; hence a branch with max cell m at step t
cannot leave POSDEF by step T unless m + (T−t) ≥ 4) and reproduced the
extension: retained `72199` at t=5, `INDEFINITE =
5526190575616/150094635296999121` and `SINGULAR =
5219452727662592/450283905890997363` at t=6. I then did the thing the
delivered gate does not do: **the FULL unpruned horizon-6 tree, 7,666,574
branches, no prune of any kind** — identical masses to the last digit, and
the branch count with max cell ≥ 4 is exactly the receipt's `retained:
109210`. The three region masses sum to exactly 1. **No pruned branch could
have reached indefinite, or singular, earlier or at all.** The delivered
`need` is computed along the base's largest component, which is the *minimal*
threshold direction for a `(1,1,c)` base, so the criterion is conservative on
the other two link classes as well.

**The polarity numbers.** Born `146623744/847288609443` against
`148895641/90632341800`, ratio `675143691622400/6409469116243161`, AVOIDED.
Record `5072320/1162261467` against `53/34992`, ratio `81157120/28166373`,
SELECTED. Stage-frozen `34816/129140163` and `325184/71744535`, both larger
than their coupled counterparts. Arena-invariance confirmed at A5 (AVOIDED /
SELECTED). Paper-20's frozen control is 0 by theorem — the arena record is
POSDEF and never changes.

**The null measure is what it claims.** Uniform on the support of each node's
emission distribution, on the same tree, carried as a denominator product;
it is not a re-weighting of the Born numbers and it is not uniform-over-leaves.
I rebuilt it independently and it agrees everywhere. **Both measures sum to
exactly 1 at every step of every reading: 60 checks, 0 failures** (the
delivered gate takes 10).

**The coin fiber, 5/5 both ways, all rebuilt.** All five classes verified
exactly unitary (`CC* = I` in `Z[ω]`) *and* exactly S₃-covariant, and all four
published numbers per row reproduced: GROVER `146623744/847288609443` /
`148895641/90632341800` / `5072320/1162261467` / `53/34992`; W
`170531816/847288609443` / `94739/62775648` / `365607521/92980917360` /
`53/34992`; MW `392/531441` / `10273973819/7653397752000` / `13789/1574640` /
`13805/8817984`; MMW `85264186/847288609443` / `74201/49043475` /
`359609459/92980917360` / `53/34992`; M2W `478/531441` /
`156109153/150124340520` / `4573/524880` / `6917/4408992`. AVOIDED at the
Born menu and SELECTED at the record menu on every member.

**The mod-3 theorem, two-way.** Branch-weight maps compared path by path
(path = the emitted-cell sequence) at horizon 4 on all three pairs:
**identical at 12 of 12 under the Born menu, 0 of 12 under the record menu.**

**Constraint B.** The ensemble site marginal at A4 and A7 agrees in all nine
entries exactly and sums to 1, while the indefinite masses are
`146623744/847288609443` and `1` — and the `1` is a theorem, not a
coincidence: at `(1,1,5)` every site is indefinite and five emissions touch at
most five of the nine.

**The 2,197 codes, third route.** Beyond the delivered two (Fraction readout;
symmetric integer form), I added exact **LDL^T pivots** — Sylvester by pivots
rather than by determinants. All three routes agree on all 2,197 codes,
0 disagreements, and all nine I7 records classify as published.

**Numeral sweep.** 63 distinct numeric tokens / 433 occurrences in the paper.
Every one is either a value I recomputed here, a record code or spectrum pair
(comma artifacts), or a provenance/ledger reference (`#211`, `#233`, `#82`,
`#125`, `2026`, sha fragments). **No unbacked numeral.** The mandatory naming
sentence is present and its numbers are the measured ones (`(1,1,5)`,
`4 det q = −5`); every resonance word in the paper occurs inside a naming or
abstention sentence.

## 2. Two mutants outside the delivered harness

The delivered 38 falsifiers all target this unit's own gates. I ran mutants
against a surface none of them covers: **paper-20's declared fibers that
SIG's §9 carries as `forced, fiber 1`.** My D·G implementation was first bound
against paper-20's own committed row (`2922723584/847288609443`, `226404`
leaves) so the mutant machinery is not free.

| variant | indefinite mass (Born, A4, T=5) | word A | word B | first indef |
|---|---|---|---|---|
| delivered `G·D, +l, coin 0, (0,0)` | `146623744/847288609443` | AVOIDED | SELECTED | 5 |
| `D·G` (paper-20 F6) | `270801152/847288609443` | AVOIDED | SELECTED | 5 |
| `−l` (F7) | `146623744/847288609443` | AVOIDED | SELECTED | 5 |
| init coin 1 (F8) | `146623744/847288609443` | AVOIDED | SELECTED | 5 |
| init coin 2 (F8) | `1783653376/2541865828329` | AVOIDED | SELECTED | 5 |
| start `(1,1)` (F9) | `146623744/847288609443` | AVOIDED | SELECTED | 5 |

The masses **move** under two of them, so the fibers are not inert; the
polarity word and the first-occupancy step are invariant across all six.
The verdict does not move. See MINOR-1.

## 3. Findings

**MAJOR: none.**

**MINOR-1 — §9 item 3 misclassifies four inherited fibers as `forced, 1`.**
Paper-20's own inventory declares `F6-COIN-ORDER` (fiber 2, stamped there
**DECLARED-VERDICT-RELEVANT**), `F7-ORIENT` (2), `F8-INIT-COIN` (3) and
`F9-INIT-SITE` (3). SIG inherits one member of each. §11 prices exactly one
inherited fiber (`F12`, halt-on-inadmissibility, deviation 7), which makes
the silence on the other four conspicuous. **Exact repair:** add one row to
§9 — *"the walk's inherited fiber members (paper-20 F6/F7/F8/F9) | declared
(inherited) | 2/2/3/3 | one member run at paper-20's delivered choice"* —
and, if wanted, cite the table above: the sign is invariant across all four,
the masses move under `D·G` and `INIT-COIN-2`. The measurement is supplied,
so the repair costs a row and strengthens the forcedness claim rather than
weakening it.

**MINOR-2 — §7.2, "differ by three at every cell", is false as written.**
A4 `(1,1,2)` and A7 `(1,1,5)` are *identical* at 18 of the 27 cells and
differ by 3 at the 9 diagonal-link cells. The load-bearing property is the
one §6.3 and the receipt already state correctly. **Exact repair:** replace
with *"Two arenas whose records agree modulo three at every cell"*.

**MINOR-3 — §1's "Nine of I7's records are positive definite" is correct but
contradicts this unit's own receipt.** It is I7's own row (*"Nine records
admissible; the two declared negative controls rejected"*), and it counts
I7's two **inhomogeneous** records `G-CURVED` and `G-CURVOFF`, which this unit
never carries. SIG's receipt publishes 9 declared records of which **7** are
POSDEF. A reader checking the sentence against §2.1's table finds a
mismatch. **Exact repair:** *"Nine of I7's eleven declared records are
admissible — seven of the nine homogeneous ones this unit carries, plus its
two inhomogeneous ones — and two are not."*

**MINOR-4 — G-PRUNE-SOUND's warrant at the horizon it publishes is the
theorem, not the gate.** The 20 cross-checks are taken at `T = 5`, where the
same rule is exercised (it does bite there) but where the *extension's*
numbers do not live; nothing in the delivered run compares the `T = 6` row
against an unpruned engine. The theorem is sound and the row is right — I
confirmed it against the full 7,666,574-branch unpruned tree — so this is a
statement about the gate's reach, not about the number. **Exact repair:**
either soften §4.2's "checked rather than trusted" to name what is checked
(*"the same prune rule is gated against the full engine at the shared
horizon; the extension itself rests on the theorem"*), or record the
now-available full-tree confirmation.

**Observation, not a finding.** The walk-beats-grammar comparison is
resource-heterogeneous — 4 rounds + 5 emissions is 41 incidences against the
grammar's 54 at R=6 — and the paper discloses exactly this by publishing the
INCIDENCES cost order (A3 wins at 33) and by naming the emission channel as a
different resource. Both sides recompute correctly; the claim is about
rounds and is true as stated.

**Peripheral row checked and standing.** "R = 8 for the one such record I7
declares": no covering record at R=6 can carry a cell at 6 at all (my
union-closure gives max coverage 26 < 27 for six rounds on one cell), and no
structurally live covering record at R=7 carries an I7 `G-INDEF` `(1,1,6)`
site. The R=8 cost stands in the live class.

## 4. The verdict word

`SIG-BLOCKED-AT-THE-EMISSION-READING` is correctly derived, not chosen. Both
of paper-20's declared readings were run; both give exact, coin-invariant,
arena-invariant masses; they disagree in sign; neither is derived anywhere in
the corpus. Stage 0's licence is real — the region is occupied with positive
exact mass at two arenas inside the declared horizon and at the third at the
extension — so the polarity sentences are licensed rather than vacuous, and
the mod-3 theorem correctly scopes the absolute masses as
representative-relative. The four segments, the window string, and the
`what may not be inherited` row are all consistent with what I measured.

---

*K1 operator lens. 342 published values recomputed at zero disagreement,
plus eight censuses rebuilt from scratch (280-partition deposit map; 30,240
commutation checks; 12,103,014-subset and union-closure sweeps at R=5;
157,248-combination R=6 LIVE search; 7,666,574-branch unpruned horizon-6
recomputation; 2,197 codes by three routes; 24 path-by-path branch-weight map
comparisons; 60 measure normalisation checks). No computed number in the
object under test was found wrong.*
