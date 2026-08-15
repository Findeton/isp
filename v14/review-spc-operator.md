# SPC (paper-37) — K1 OPERATOR-LENS REVIEW

**Seat:** K1, the operator lens — the representation theory itself, rebuilt
from the pin's and the parents' definitions on code that shares nothing with
`v14/code/spc_exact.py`.
**Stance:** hostile; every number assumed wrong until independently rebuilt.
**All rulings below are candidate until adjudication.**

**Objects, sha256-12, verified at open AND at close (all five match at both
ends):**

| object | sha256-12 |
|---|---|
| `v14/paper-37-spc.md` | `1555d049d558` |
| `v14/code/spc_exact.py` | `6b399487f286` |
| `v14/code/spc_output.txt` | `dc6410c72036` |
| `v14/code/spc_receipt.json` | `3958fe51495b` |
| `v14/note-spc-pin.md` (pin) | `7f0b1e9d5071` |

All twelve pinned sources re-hashed by me independently of the receipt, all
twelve matching what the paper and the receipt claim: `S-PIN` `7f0b1e9d5071`,
`S-ACT-PAPER` `d933221780ed`, `S-ACT-CODE` `a90559ee0e0f`, `S-ACT-RECEIPT`
`7fd1267bddc7`, `S-AID-PAPER` `ecdd3fbf1d06`, `S-AID-RECEIPT` `2dd2a9879984`,
`S-OCC-PAPER` `0092caa4d9ad`, `S-OCC-RECEIPT` `455ddec78dda`, `S-SMU-PAPER`
`6df0db523d32`, `S-R5-PAPER` `62cfe5689d2c`, `S-CRB-PAPER` `c350caab17ee`,
`S-CRB-CODE` `5f2a54ea8a98`.

---

## GRADE: **AWF** (accept with fixes)

**No computed number in this unit was found to be wrong.** I rebuilt the
representation theory from scratch — my own cyclotomic field, my own
Burnside–Dixon engine, my own Murnaghan–Nakayama engine on beta-numbers, my
own Young-subgroup product tables, my own semistandard-tableau enumerator —
and **every one of the 220 conjugacy classes, 220 species, 19 carrier rows,
246 available and 156 hosted species, 2,154 composite rules, 2,610 branching
multiplicities, 210 tableau counts, the 192/14/9/31 statistics split, the six
acting-group orders and the whole one-species price theorem reproduced
exactly**, at 340 from-scratch recomputations with zero disagreements. I
additionally ran a route the instrument does not have — the sum of the squared
multiplicities against the number of orbits on **ordered pairs** — and it
agrees at all 19 rows. The sharpest claim in the paper, the price theorem,
survives a **strictly stronger** reading than the one the instrument tests.

Two **majors** stand, and neither is a wrong number.

* **M1** is a methodological paragraph in §2 that is false for 12 of the 22
  rows of the table it introduces, and whose exception clause names three rows
  where the measurement says eight.
* **M2** is a demonstrated **gating gap**: the verdict head's universal
  `EVERY-TABLE-GATED-BY-TWO-ROUTES` and §3's "Every table this unit publishes
  is gated twice over" are not implemented for 7 of the 18 tables. I corrupted
  six Young-subgroup character tables until they carried **136 row- and 126
  column-orthogonality failures**, and the full delivery pipeline exited 0
  with every gate green, publishing those failure counts in the receipt.

Both have cheap repairs. M1 is prose-only. M2 is three lines of instrument
plus one falsifier, or a two-clause narrowing of the head. Ten minors follow
them. Nothing here touches a delivered figure.

---

## 0. What I did, and how independent it is

**Independent primitives, nothing imported.** My rebuild carries
$\mathbb{Q}(\zeta_n)$ as $\mathbb{Q}[x]/\Phi_n(x)$ with `Fraction`
coefficients in the power basis, where $\Phi_n$ is built by the **Möbius
product** $\prod_{d\mid n}(x^{n/d}-1)^{\mu(d)}$ and cross-checked against
$\deg\Phi_n=\varphi(n)$ at every construction — a different derivation from
the instrument's iterated division of $x^n-1$ by every proper divisor's
polynomial. Every group is turned into an **index-based Cayley table** at
construction, so classes, inverses and class multiplication coefficients are
integer arithmetic on indices. My Dixon engine picks its own prime (the
smallest $p\equiv 1 \bmod \exp G$ with $p>2\lfloor\sqrt{|G|}\rfloor+1$), splits
the class algebra by **Krylov minimal polynomials with a full-scan fallback**
rather than by repeated eigenspace descent, recovers the degree by requiring
both $d^2\equiv|G|/\sum_j\omega_j\omega_{\bar\jmath}|C_j|^{-1}$ **and**
$d\mid|G|$, and lifts each value out of $\mathbb{F}_p$ by a Fourier inversion
that **asserts** every recovered eigenvalue multiplicity is a non-negative
integer and that they sum to the degree — a check the instrument does not
make. My symmetric-group engine recurses on **beta-numbers** (removing a rim
hook is replacing $b$ by $b-r$ when $b-r\notin B$, with height read off the
beta-set), not on rim-hook scanning. My Kostka route enumerates semistandard
tableaux **cell by cell in row-major order** rather than by peeling horizontal
strips. Orbits are counted by **breadth-first flooding**, not union-find.
Nothing is imported from `spc_exact.py`, no literal is copied from it, and no
product of it is re-read except as a target to compare against.

**What I read from the instrument.** Only the definitions: the coin alphabet
and family, the twist/swap/sector/quartic-sign maps, the $L=4$ lattice with its
links, plaquettes and point symmetries, the AG(2,3) arena, the three stencils
and the gauge-image / chart-stabiliser / action-composition laws, the carrier
row list, the stabilizer shapes and the crystallization flag. Those are
declarations; the mathematics on top of them is mine.

**Recomputations, in full.**

| battery | count | disagreements |
|---|---|---|
| arena, chart, acting-group and carrier census (my engines) | 301 | 0 |
| extra hostile probes (§4 below) | 20 | 0 |
| degree lists, mine vs published, all 19 rows | 19 | 0 |
| paper-table cells vs receipt, all 15 tables | 940 | 0 (3 artefacts of unescaped pipes — see m4) |
| provenance digests re-hashed | 12 | 0 |
| blockquote windows located verbatim in their pinned sources | 13 | 0 |
| distinct numerals in the paper body licensed by a receipt integer | 83 | 0 |
| object digests at open and at close | 10 | 0 |
| instrument runs (`--verify-paper`, `--selftest`) and AST scan | 7 | 0 |
| the four control arms rebuilt through my own engines | 22 | 0 |
| outcome-feasibility witnesses checked against the row they name | 7 | 0 |
| the corruption experiment of M2 | 9 | — |
| **total** | **1,443** | **0 false numbers** |

**Instrument runs I made.** `--verify-paper` exits 0 and writes nothing;
`--selftest` reports `FATAL AT EVERY ANCHOR CLASS :: [('FILE-BYTES', True),
('PATH-VALUE', True), ('VERBATIM', True)] :: artifacts unchanged True` and
exits 0. I never ran the delivery writer; `git status` shows the three SPC
artifacts untouched throughout.

---

## 1. The inventory — all 22 orders re-derived by my own routes

Every order rebuilt from its own construction, never read: the coin alphabet
enumerated to **25** elements, the admissible rows to **80**, the coin family
to **640** splitting **64 / 64 / 512** into diagonal / antidiagonal /
balanced; the coin-map group closed to **16** with the elementary twist of
order **8**; the AG(2,3) point group built as the maximal set of matrices
carrying the declared link set into its signed closure at order **12**, the
arena group **108**, the chart group **18**, translations **9**, cells **27**;
the chart groups **32** and **128**, both faithful on the 32 links, transitive
on links, sites and plaquettes (1/1/1). All match.

**The four above-cap orders, rebuilt from the stencils.** I re-derived the
gauge image on each stencil by enumerating the site phases the stencil touches
and reading each link's own twist, built the chart stabiliser of each stencil
with its slot permutation and swap conjugations, and composed. All six rows
reproduce exactly, column for column:

| grain | reading | gauge image | chart stab | acting order | carrier sees | induced |
|---|---|---|---|---|---|---|
| LINK | ANCHORED | 8 | 1 | 8 | 8 | 136 |
| LINK | EXTENSION | 8 | 4 | 16 | 16 | 80 |
| PLAQUETTE | ANCHORED | 512 | 2 | 1024 | 8 | 136 |
| PLAQUETTE | EXTENSION | 512 | 8 | 4096 | 16 | 80 |
| SITE | ANCHORED | 4096 | 2 | 8192 | 8 | 136 |
| SITE | EXTENSION | 4096 | 8 | 32768 | 16 | 80 |

**220 classes and 220 species.** My inventory returns 22 groups; 18 with a
table (11 distinct Dixon/MN groups on carrier rows plus the 7 Young
subgroups); classes summing to **220** and species to **220**; distinct orders
`[1,2,4,8,9,16,18,24,32,108,128,216,1024,4096,4320,8192,32768,362880]`, all
matching. Every one of the 22 `(order, classes, species)` triples matches the
published inventory row for row.

---

## 2. The character tables — both routes, both engines, my own

Every table I built passes **row orthogonality**, **column orthogonality**,
the **class equation**, the **degree sum of squares**, `degrees | order` and
`classes = irreps`, computed in my own field arithmetic. The degree lists
reproduce exactly at all 19 carrier rows. The spot tables the seat asks for:

| group | order | classes | degrees | $\sum d^2$ |
|---|---|---|---|---|
| S9 | 362880 | 30 | 1,1,8,8,27,27,28,28,42,42,42,48,48,56,56,70,84,84,105,105,120,120,162,162,168,168,189,189,216,216 | 362880 |
| CHART-32 | 32 | 14 | $1^8, 2^6$ | 32 |
| CHART-128 | 128 | 20 | $1^8, 2^6, 4^6$ | 128 |
| EXT-108 | 108 | 11 | $1^4, 2^4, 4, 6^2$ | 108 |
| TORUS-TRANSLATIONS-16 | 16 | 16 | $1^{16}$ | 16 |
| CHART-18 | 18 | 9 | $1^6, 2^3$ | 18 |
| TRANS-9 | 9 | 9 | $1^9$ | 9 |
| GAMMA-16 | 16 | 7 | $1^4, 2^3$ | 16 |
| RESIDUAL-GAUGE-8 | 8 | 5 | $1^4, 2$ | 8 |

The stabilizer lattice returns **1 / 2 / 4 / 8 / 12 / 27 / 33** classes and the
same species counts, with orders **1 / 2 / 4 / 8 / 24 / 216 / 4320** agreeing
on all three routes. The S9 degrees are re-derived by my own hook-length
formula and are identical to the published list; the table is integer-valued
at every entry; the two engines (my Dixon on explicit permutations, my MN on
partitions) agree on S2, S3 and S4 in classes and degrees — and, going beyond
the unit's own triple, on **S5** as well, table for table (see m10).

**One check the instrument does not make and mine does.** For every recovered
character I assert that the Fourier-inverted eigenvalue multiplicities are
non-negative integers summing to the degree. The instrument instead lifts each
coefficient to a *signed* residue (`c = acc if acc <= p // 2 else acc - p`);
the signed branch is unreachable given $p > 2\sqrt{|G|}$, so it is harmless
here, but the positivity of the multiplicity is never tested there. No finding
— recorded so the panel knows the stronger check was run and passed.

---

## 3. The scope-closer — the mechanism, verified and correctly located

The claim rebuilt: at every one of the six (grain, reading) rows the set of
**constant** coin-map tuples reachable by the acting group is closed, is the
same set at all three grains, has order 8 at the anchored reading and 16 at
the extension, and the partition it induces on the 640 uniform configurations
is exactly the partition the whole acting group induces there — 136 anchored,
80 at the extension. **All of that reproduces.** I additionally identified the
two groups: the anchored one is exactly $\langle \tau_1\rangle$ and the
extension one is exactly $\Gamma$, as sets of permutations of the 640 coins.

**The mechanism is real, and it is a partition-level mechanism.** The union-find
in the instrument merges $x\sim y$ whenever *some* acting element sends
uniform-$x$ to uniform-$y$, which is a weaker relation than the orbit relation
of the constant subgroup — non-constant tuples can agree at particular coins.
The measurement is that they contribute nothing extra: I recomputed the induced
partition and the orbit count of the constant subgroup separately at all six
rows and they agree 6/6. So the grain-invariance ACT reports is genuinely
explained, and explained by a measurement rather than by an argument.

What the mechanism does **not** establish is a species census at six rows; see
minor **m2**. There is no action of the order-1024/4096/8192/32768 groups on
COIN-640 at all — a general element carries a uniform configuration off the
carrier — so there are four carrier rows on COIN-640, not six, and the
transportable statement is about identifications, not about modules.

---

## 4. The carrier decomposition, and a route the unit does not have

All 19 rows rebuilt: classes, irreps, hosted, homeless, orbits by character,
the full multiplicity multiset, composite rules, exit sets and the four-class
statistics split. **156 of 246 hosted, 9 rows with a homeless species, 7
carriers, the widest gap ACTOR-9-UNDER-S9 at 2 of 30** — all reproduced.
ACT's four carrier numbers come back as trivial-species multiplicities:
**208 / 136 / 120 / 80**, each by a character inner product and by an
independent flood-fill.

**The extra route.** For a permutation module,
$\sum_i m_i^2 = \langle\pi,\pi\rangle$ is the number of orbits of the group on
**ordered pairs** of carrier points. That is a check on the whole multiplicity
vector, not just on its trivial component, and the instrument does not have
it. I computed it by flooding $n^2$ points at every row. **It agrees at all 19
rows.** Together with $\sum_i m_i d_i = n$, $m_{\text{triv}} = \#\text{orbits}$
and both square-dimension identities, the multiplicity vectors are pinned from
four directions.

Additional probes, all clean:

* the rows that close are **exactly** the rows with no homeless species — I
  compared the two sets, not the two counts, and they are equal;
* $\mathrm{Sym}^2$ of the actor module decomposes as $\{(9),(8,1),(7,2)\}$ and
  $\Lambda^2$ as $\{(8,1),(7,1,1)\}$, so the split 1/2/1/26 and the
  "trivial species is not compatible with the selected shape" headline are
  structural, not numerical accidents;
* the actor row hosts exactly $\{(9),(8,1)\}$ and standard $\otimes$ standard
  reaches $\{(9),(8,1),(7,2),(7,1,1)\}$ each once — the published composite
  table, cell for cell.

---

## 5. The one-species price theorem — it survives a stronger reading

Rebuilt and confirmed at both readings:

* the odd-twist species is **unique**, its multiplicity is **72** anchored and
  **40** at the extension, and each equals the drop in the trivial multiplicity
  ($208-136$, $120-80$) and equals ACT's identified orbit-pair count;
* the observable, rebuilt from ACT's own verbatim description, is non-zero at
  **288 of 640** coins, has a non-zero component in **exactly one** isotypic
  component — that species and no other — and **136 of 136** orbit sums vanish.

**Three things I add.**

1. **The instrument tests a weaker statement than the paper asserts.** The
   paper says "exactly one species on which the odd twist acts by minus one
   while every twist the torus itself realises acts trivially". The instrument
   filters on *degree one* and character value $-1$. A higher-dimensional
   species acting by the scalar $-I$ would satisfy the paper's sentence and
   escape the instrument's filter. I ran the stronger filter —
   $\chi(\tau_1)=-\deg$, $\chi(\tau_2)=+\deg$, and $\chi(\sigma)=+\deg$ at the
   extension — over the full tables. **It also returns exactly one species at
   both readings, and it is the same one.** The headline is therefore true
   under the reading its own sentence invites, not only under the reading the
   gate tests. Recorded as a strengthening, not a finding.

2. **The price is a theorem, and I verified its hypothesis.** $\langle
   \mathrm{Res}_H\pi, 1\rangle = \langle\pi,1\rangle + \langle\pi,\chi\rangle$
   for $H$ of index 2 with non-trivial quotient character $\chi$. I confirmed
   the two containments the identity needs and that both have index exactly 2:
   $\langle\tau_2\rangle < \langle\tau_1\rangle$ and
   $\langle\tau_2,\sigma\rangle < \langle\tau_1,\sigma\rangle$. So 72 and 40
   are forced, not coincidental.

3. **The `[0,0]` pinning is forced, not measured-and-hoped.** ACT's three
   declared properties of the observable all hold exactly on my rebuild:
   invariant under the even twist, invariant under the swap, and **reversed**
   by the odd twist ($\mathrm{obs}\circ\tau_1 = -\mathrm{obs}$ pointwise at all
   640 coins). Sign reversal under a generator makes every orbit sum vanish
   identically, and an orbit-constant weight then pairs to zero. ACT's
   `range_over_the_reachable_set = ["0","0"]` follows. The paper's §5 argument
   is correct and its measured leg is correct.

---

## 6. Branching, selection, statistics

**2,610 branching multiplicities** by my restriction route and my Frobenius
reciprocity route, **0 disagreements**; **210 tableau counts** by my direct
SSYT enumerator, **0 disagreements**; the 30-row distinguished branching table
at YOUNG-216 reproduces species by species, degree, constituents and invariant
dimension. The invariant counts along the lattice are **30, 29, 28, 26, 22, 12,
4** and along the exhibited flag **4, 12, 12, 26, 30, 30**, with the flag
verified nested and the orders 4320/216/216/8/1/1 matching AID's published
profile entry for entry.

**A structural confirmation the paper does not claim but which supports it:**
the seven stabilizer shapes form a **dominance chain**, and $K_{\lambda\mu}>0
\iff \lambda \trianglerighteq \mu$; I recomputed the seven invariant counts by
dominance alone and got the same 30/29/28/26/22/12/4. So "the inventory
collapses as the stabilizer grows" is monotone by a theorem along this
particular lattice, not only by measurement.

**Selection:** 2,154 composite rules, 10 rows close, 9 exit, per-row exit
sets all matching. **Statistics:** the ANTISYMMETRIC shape is what 0-against-81
derives; the aggregate is **192 / 14 / 9 / 31** over 246, 4 rows split
properly, and every per-row quadruple matches.

---

## 7. The falsification battery, from my seat

The mutant registry is the instrument seat's business; I checked only what
bears on the mathematics.

* `--selftest` is green and writes nothing: fatal at all three anchor classes.
* The registry's own claim that `MUT-DROP-SPECIES` "leaves ROW orthogonality
  intact and breaks only the column route" is **true**, and I verified it on my
  own S9 table rather than on theirs: dropping the last species leaves 0
  row-orthogonality failures and produces column failures. So the two
  orthogonality gates really are independent measurements where they are
  applied.
* The registry contains no falsifier that plants a wrong value into a
  Young-subgroup character table; see M2.
* I launched the full `--all-mutants` sweep (55 complete pipeline runs, each
  about 22 s of CPU). It was still running at close — roughly 8.5 minutes of
  CPU consumed on a contended machine — and its output buffer had not flushed,
  so I have **no partial result to report either way**. The receipt is honest
  that the sweep is
  `AN-EXTERNAL-BATTERY-RESULT-THE-DELIVERY-RUN-DOES-NOT-PRODUCE-IT`, so this
  seat records it as **not independently completed here** and defers it to the
  instrument seat. Nothing in my findings depends on it, and the paper's
  status-line claim "every declared mutant dead at its declared target" is
  therefore **unverified by this seat**, neither confirmed nor contradicted.

---

## MAJOR 1 — the order-route paragraph is false for 12 of the 22 rows

**Where.** §2, the paragraph beginning "**No order in this table is typed.**"
(paper lines 135–142).

**What it says.** That every group's order is re-derived (i) by the length of
its own closed element list, (ii) by the sum of its own conjugacy class sizes,
(iii) by the sum of the squares of its species degrees, and (iv) wherever the
elements are enumerable, by orbit × stabilizer; and that "**The three
symmetric-group rows** take the first three routes only".

**The measurement.** I enumerated, row by row, which routes the instrument
actually takes for each of the 22 inventory rows:

| how the order is re-derived | rows |
|---|---|
| element list + class equation + degree sum + orbit·stabilizer | **10** |
| the factorial + class equation + degree sum (S9) | **1** |
| a product of block factorials + class equation + degree sum (the 7 Young rows) | **7** |
| the number of distinct actions on the stencil datum — **none of the four named routes** | **4** |

So **eight** rows take a reduced route, not three; for all eight the first
route is not an element list at all; and the **four** above-cap rows are not
excepted by the paragraph even though they take none of its four routes (they
have `classes = 0` and `species = 0`, so neither the class equation nor the
degree sum exists for them). Twelve of twenty-two rows are misdescribed. The
above-cap route is described correctly three paragraphs later and in §9, so
the defect is confined to this paragraph; the numeral "three" is a spelled
numeral at or below twelve and therefore outside the instrument's own numeral
gate, which scans spelled numerals **above** twelve only — that is why it
survived delivery. The paragraph is prose and not a rendered claim, so the
repair touches the paper alone.

**No number moves.** Every order in the table is right; I re-derived all 22.

**Licensed replacement** (drop-in for the whole paragraph):

> **No order in this table is typed.** Ten of the twenty-two groups have their
> order re-derived four ways: by the length of their own closed element list,
> by the sum of their own conjugacy class sizes, by the sum of the squares of
> their species degrees, and by the product of one declared point's orbit with
> that point's stabilizer. Eight rows are indexed by partitions rather than
> enumerated as permutations — the nine-actor group and the seven Young
> subgroups — and take three routes, the first of which is a product of
> factorials rather than an element list: the order by construction, the sum
> of the class sizes, and the sum of the squares of the degrees; no permutation
> is ever written down for them. The four acting groups above the table cap
> take none of those four: their order is the number of distinct actions on
> the stencil datum, re-derived below and gated against the parent's receipt
> row by row.

---

## MAJOR 2 — `EVERY-TABLE-GATED-BY-TWO-ROUTES` is not implemented for 7 of 18 tables

**Where.** The verdict head, segment
`IRREPS=EVERY-TABLE-GATED-BY-TWO-ROUTES-COLUMN-ORTHOGONALITY-AND-ROW-ORTHOGONALITY-AS-SEPARATE-GATES-…`,
and §3, "Every table this unit publishes is gated twice over, and the two
gates are separate rows of the ledger because they are not the same
measurement."

**The gap.** Grepping the instrument for every consumer of
`row_orthogonality_failures` / `column_orthogonality_failures` gives exactly
three: `row_gate_failures` (line 1929/1931), which covers the 19 carrier rows
and therefore the 10 enumerated groups plus S9; and the two S9 gates
`G-CHARACTER-TABLE-ROW-ORTHOGONALITY` / `-COLUMN-ORTHOGONALITY` (lines
2439–2459), which read only `tg9` and `stg`. The seven Young-subgroup tables
record their orthogonality at lines 2568–2570 — the receipt publishes
`identity_layer/rows/*/row_orthogonality_failures` and
`…/column_orthogonality_failures` for all seven — and **no gate reads either
field**. Those seven tables carry **87 of the published 220 classes and 87 of
the 220 species**, 39.5% of the inventory. Their class equation and degree sum
*are* gated (inside `G-IDENTITY-LATTICE-IS-THE-PARENTS`); only the two
orthogonality routes are not.

**The demonstration.** I loaded the instrument in process, wrapped
`ct_from_young` so that one **non-identity-column** entry of each Young table
is shifted by one — leaving degrees, class sizes and the branching engine's
own `young_char` untouched — and ran the full pipeline with `--verify-paper`
(write=False; artifacts verified unchanged). Result:

```
PUBLISHED identity_layer orthogonality under the corruption:
   FORCED-TRIVIAL row_orth_failures=0   col_orth_failures=0
   YOUNG-2        row_orth_failures=3   col_orth_failures=3
   YOUNG-4        row_orth_failures=7   col_orth_failures=7
   YOUNG-8        row_orth_failures=15  col_orth_failures=15
   YOUNG-24       row_orth_failures=23  col_orth_failures=23
   YOUNG-216      row_orth_failures=53  col_orth_failures=35
   YOUNG-4320     row_orth_failures=35  col_orth_failures=43
EXIT: 0   artifacts unchanged: True
```

**136 row-orthogonality failures and 126 column-orthogonality failures across
six tables, and the run is green.** (FORCED-TRIVIAL is $1\times1$; there is
nothing to corrupt.) A first attempt that perturbed the identity column died
at `G-IDENTITY-LATTICE-IS-THE-PARENTS` because the degree sum moved — which is
the correct behaviour and shows precisely which leg is doing the work: the
class equation and the degree sum, not orthogonality.

**No falsifier covers it either.** The 55-mutant registry has
`MUT-CHARACTER-VALUE` (EXT-108, a Dixon table, caught at
`G-CARRIER-DECOMPOSITION`), `MUT-MN-VALUE` and `MUT-DROP-SPECIES` (the S9
table), `MUT-LATTICE-SHAPE`, `MUT-BRANCHING` and `MUT-KOSTKA` (the identity
layer's *other* legs). Nothing plants a bad Young character. The
`waiver_ledger` reports `uncovered: []`, but its denominator is
`EVERY-GATE-ON-THE-CLEAN-PATH` — it measures whether existing gates have
falsifiers, and cannot see a published object that has no gate at all.

**Nothing published is wrong.** I verified all seven Young tables
independently: row and column orthogonality failures are genuinely zero, the
class equations hold, the degree sums are 1/2/4/8/24/216/4320. The defect is
that the head asserts a discipline the instrument does not apply, and a
verdict head is compared character for character precisely so that its
universals can be relied on.

**Repair, preferred (three lines and one falsifier).** In
`measure_the_identity_layer`, add a gate beside the three that exist:

> `G-YOUNG-TABLE-ORTHOGONALITY` — "the seven stabilizer tables are gated by
> the same two routes as every other table this unit publishes: every pair of
> distinct species has inner product zero and every species one with itself,
> and for every pair of classes the column inner product vanishes off the
> diagonal and returns the centralizer order on it", predicated on
> `all(r["row_orthogonality_failures"] == 0 and
> r["column_orthogonality_failures"] == 0 for r in rows)`,

with a falsifier `MUT-YOUNG-TABLE` that shifts one non-identity value of one
Young table by one and is declared to die there.

**Repair, alternative (disclosure only).** If the head is to stand unchanged
in shape, narrow it and §3 together. Head segment:

> `IRREPS=EVERY-ENUMERATED-TABLE-AND-THE-NINE-ACTOR-TABLE-GATED-BY-TWO-ROUTES-COLUMN-ORTHOGONALITY-AND-ROW-ORTHOGONALITY-AS-SEPARATE-GATES-WITH-THE-CLASS-EQUATION-AND-THE-DEGREE-SUM-BESIDE-THEM;THE-SEVEN-STABILIZER-TABLES-GATED-ON-THE-CLASS-EQUATION-AND-THE-DEGREE-SUM-WITH-THEIR-ORTHOGONALITY-MEASURED-AND-PUBLISHED-BUT-NOT-GATED`

and §3's opening sentence:

> Every table this unit builds by enumerating a group, and the nine-actor
> table, is gated twice over, and the two gates are separate rows of the
> ledger because they are not the same measurement. The seven Young-subgroup
> tables carry the class equation and the sum of the squares of the degrees as
> gates; their orthogonality is measured and published at every row and is not
> itself a gate.

I recommend the first repair: the gate costs three lines, and the numbers it
would check are already computed and already zero.

---

## MINORS

**m1 — "4 of which stand above the declared cap of 128" (§2, line 130; and the
head's `4-STAND-ABOVE-THE-DECLARED-CAP-128`).** Seven of the twenty-two
groups have order above 128, and three of them — YOUNG-216 (216),
YOUNG-4320 (4320) and S9 (362880) — carry full exact character tables. The cap
is a cap on the *element-list* engine, not on order; the MN engine is not
capped. As written the sentence licenses the inference "order > 128 ⇒ no
table", which is false for three rows listed in the paper's own order list.
Licensed replacement for the first sentence of §2:

> 22 groups, 18 of which carry a full exact character table and 4 of which —
> the acting groups at the plaquette and site grains — stand above the
> declared cap of 128 on the group this unit will enumerate element by
> element.

Note for the author: unlike M1's paragraph, this sentence **is** a rendered
claim (`build_claims`, the first entry: `"%d groups, %d of which carry a full
exact character table and %d of which stand above the declared cap of %d"`),
so repairing it means editing the format string in the instrument and the
paper together, or the claim gate will refuse.

**m2 — "the species census on this carrier is complete at all six rows"
(§2, line 197).** There are four carrier rows on COIN-640, not six, and no
species census exists over the four above-cap groups because they do not act
on that carrier: a general element of the order-1024 group carries a uniform
configuration off it. What is measured is a partition, and the partition is
sufficient. Licensed replacement:

> That is why nothing the carrier census reads changes at any of the six rows
> although four of the six acting groups have no table here: the
> identifications those four make on this carrier are exactly the orbits of
> the order-eight group at the anchored reading and of the order-sixteen group
> at the extension, and both of those do carry a table.

**m3 — the "species index" column is engine-relative (§5 table).** The values
0 and 1 are row indices into this instrument's own Dixon table, which is
sorted on the identity-column value and then on the string rendering of the
whole row (`dixon_table`, line 1159), over a class ordering fixed by the
element list. My engine, sorting on its own key over its own coin enumeration,
assigns different indices to the same species. The column is not reproducible
by an independent rebuild. The paper's own prose already fixes the species
invariantly, so the cheapest repair is a footnote to the table:

> The species index is this unit's own table row index for that group and is
> engine-relative; the species itself is fixed without reference to any
> ordering as the unique one-dimensional species with $\chi(\text{odd
> twist}) = -1$ and $\chi(\text{torus twist}) = +1$, and $\chi(\text{swap}) =
> +1$ at the extension.

**m4 — the control-arm table does not render (§1, lines 123–125).** Three of
the four data rows carry unescaped `|` inside the last cell (the emitted head
ends `…SPLITS-3|0|0|0`). The header row has 7 pipes; those data rows have 10.
Under GitHub-flavoured markdown the rows render as nine columns against a
six-column header and the `|0|0|0` tail of each control head is dropped from
the rendered table. The instrument's `render_cell` (line 4170) does not escape
`|`, and `verify_paper` tests only whether the rendered claim string is a
substring of the paper's raw table line (line ~4480), so both sides carry the
same unescaped pipes and the gate cannot see it. Fix: escape as `\|` in
`render_cell`, or render the statistics split with a different separator in
the control head.

**m5 — "6 stabilizer shapes" (§12, line 656).** The stabilizer lattice this
unit builds has **seven** shapes; §6's table publishes seven rows and the
choice inventory records `THE-STABILIZER-LATTICE … instances built 7`. Only
the six *nontrivial* shapes are read from AID. §12's list is introduced as
"each named in the choice inventory", which says 7. Licensed replacement:
"19 carrier rows, 22 groups, 7 stabilizer shapes — the six nontrivial ones the
parent measured and the forced-trivial one — and one chain".

**m6 — "The corpus has spent fourteen units measuring symmetries" (§1, line
70).** This numeral binds to no measured object; the numeral gate licenses it
only by coincidence with unrelated 14s in the receipt (14 classes of CHART-32,
14 symmetric-only species). Either bind it to a countable list or drop the
count ("The corpus has spent many units measuring symmetries").

**m7 — the glued-world sentence carries an unstamped parent (§9, last
bullet).** "The sector union's automorphism group is larger than any single
sector's" is a SEC result; SEC is not among the twelve pinned sources. The
claim is inherited from the pin's successor note (which *is* pinned), but the
paper does not say so. Add "as the pin's successor note records" or equivalent.

**m8 — "156 of 246" is a count over (row, species) pairs.** There are 220
distinct species in the inventory; 246 is the sum of the per-row species
counts, so a group censused on three carriers is counted three times. §4's
table and the "property of the pair" paragraph make this clear in the paper;
the head segment `156-OF-246-SPECIES-HOSTED` does not. Consider
`156-OF-246-ROW-SPECIES-PAIRS-HOSTED`.

**m9 — §10's anchor sentence attaches five properties to all 74 anchors
(lines 601–605).** "12 file-bytes anchors, 43 path-value anchors and 19
verbatim-text anchors, 74 anchors in all, each window pinned by its own digest
and its own character count against a declared floor, each located exactly
once …, each perturbed at a content-bearing token …, and each bound to the
gate that consumes it." Measured: only the 19 verbatim rows carry `chars`,
`floor`, `digest`, `located` and `perturbed_located`; and
`consumer_register.anchors` is **62** (43 path-value + 19 verbatim) — the 12
provenance rows carry no `consumer` field at all. The paper's own header
paragraph (lines 30–36) gets this right by writing "each **verbatim window**
pinned by …"; §10 dropped the qualifier. Restore it there.

**m10 — "wherever both can run" is a hard-coded triple (§3, line 227; and the
`G-TWO-ENGINES-AGREE` gate text).** §3 says the two engines "are required to
agree wherever both can run", and the gate's own sealed rationale says "on
every symmetric group **small enough for both**". `measure_the_two_engines`
iterates `for n in (2, 3, 4)`. S5 has **120** elements — *fewer* than the 128
of CHART-128, which this same instrument already enumerates and Dixon-izes. I
ran S5 through my own two engines: 7 classes, degrees $1,1,4,4,5,5,6$, row and
column orthogonality clean, and **the two tables agree**, in 0.1 s. So the
range is a declaration, not a size limit, and neither the paper nor the gate
declares it. The head's `TWO-ENGINES-AGREE-ON-3-SYMMETRIC-GROUPS` is honest
about the count but not about the reason. Cheapest repair: extend the loop to
`(2, 3, 4, 5)` — it costs a tenth of a second and makes the sentence true.
Otherwise declare the range: "on the three symmetric groups this unit puts
through both engines".

---

## What I could not fault

* **Every measured number.** 340 from-scratch representation-theory
  recomputations, zero disagreements — including every table, every degree,
  every multiplicity multiset, every composite count, every branching
  multiplicity and every tableau count.
* **The price theorem**, which survives a strictly stronger reading than the
  instrument tests, and whose two legs (72 = 208−136, 40 = 120−80) are forced
  by an index-2 identity whose hypothesis I verified.
* **The observable**, which satisfies all three of ACT's declared invariance
  properties exactly, with $\mathrm{obs}\circ\tau_1=-\mathrm{obs}$ pointwise —
  making the `[0,0]` pinning a theorem.
* **The scope-closer**, whose mechanism is measured and not argued, including
  the non-obvious leg that non-constant tuples add no identifications.
* **The binding.** 940 table cells against the receipt with no drift, 15 tables
  and 15 headers all bound, 13 of 13 blockquotes located verbatim in their own
  pinned sources under markdown-prefix normalisation, 12 of 12 source digests
  re-hashed, every one of the 83 distinct numerals in the body licensed by a
  receipt integer, the fenced verdict identical to `receipt.verdict`, the
  paper/code/pin digests self-consistent, `transcript_head` reproducible as
  `digest(json.dumps(transcript))`, 0 float literals under my own AST scan and
  no `math` import anywhere.
* **The control arm and the feasibility table.** I rebuilt all four synthetic
  arenas on my own engines and reproduced every published field: the regular
  $\mathbb{Z}_3$ row at 3/3 hosted, 9 rules, split 3\|0\|0\|0; the trivial
  action at 1 of 3, 1 rule, 1\|0\|0\|2; the two-orbit $\mathbb{Z}_6$ at 4 of 6
  with the composites exiting; and the fourth probe measured **not** to be
  closed under composition, so the refusal word is genuinely reachable. Each of
  the seven live outcome arms is witnessed by the row the table names, and I
  checked each witness against my own numbers for that row: every-species-hosted
  and all-in-both at COIN-640-UNDER-RESIDUAL-GAUGE-4 (4 hosted, 0 homeless,
  4\|0\|0\|0), some-species-homeless and composites-exit at
  SITE-16-UNDER-CHART-32 (4 homeless, exits to 4), a-proper-split at
  SITE-16-UNDER-CHART-128 (11\|5\|2\|2).
* **The honesty of the scope section.** §9 names the four above-cap groups'
  open inventories, the carrier row list's unbounded fibre, the granted
  nine-actor grain and the glued-world census as undecided, and the walls'
  ANALOGY licence is registered and unused.

## Recommendation

**AWF.** Fix M1 (prose), fix M2 (three lines of instrument and one falsifier,
or the disclosed narrowing of the head and §3), and take the ten minors.
None of the fixes moves a delivered figure, and the unit's headline results —
the inventory, the hosting contrast, the one-species price, the branching
profile, the selection census and the statistics split — stand as measured.

---

**Close.** All five objects re-hashed at close and unchanged: paper
`1555d049d558`, instrument `6b399487f286`, transcript `dc6410c72036`, receipt
`3958fe51495b`, pin `7f0b1e9d5071`. Git status shows no SPC artifact modified
by this review; this file is my only repo write.
