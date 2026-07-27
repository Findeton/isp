# D73 — result: **on the fixture paper 30 itself selected, the even Gram is anisotropic with a trivial stabiliser — that is the genuine G2 survivor.** The promoted-`K` question was **fixture-dead at the old anchor** (the triple this unit first anchored on is the one paper 30 `§26.2` declares *falsified*; the `1.676e-5` it called "the committed `TV_9`" is the rank-11 loser's score, and that residual is a **sector-selection** artefact no function of the even 3-vector can reach) and is **re-posed at the new one**, where the floor is `0` exactly and a wrong `K` is visibly punished. And the v10 transfer hint **INVERTS**: the 59 "anisotropic direction Grams" are **two matrices**, degenerate and over-symmetric — the tensor stage needs an asymmetry the hand-built crystals lack.

**Status: ROUND-1 REVIEWED AND REPAIRED, 2026-07-27.**
Round: `v10/reviews/d73-round1-hostile-review.md` — **1 BLOCKER /
4 MAJOR / 5 MODERATE / 5 MINOR, verdict REVISE.** Every defect is
repaired below or explicitly carried. The round's own recomputations
were reproduced here, from this receipt's own instrument, before being
used; **not one of them failed to reproduce.** The round is credited at
every point where its number, its table or its argument is the thing
being carried — its author found the BLOCKER by reading 130 lines
further down a paper this unit had already opened, and found the
transfer probe's inversion inside the unit's own evidence.

Pin `v10/note-d73-even-gram-pin.md` (STRICT, FROZEN, committed
**before** any code was written; it names claim P2, tests 1–3 and
falsifiers F1–F4). **The pin is not rewritten by this note**, and the
first delivery's central procedural error was that it tried to (`§3`).
Receipt `v10/code/d73_even_gram_exact.py`, output
`v10/data/d73_even_gram_exact.out` — run from the repository root under
`python3.13` (the committed v7 campaign uses `int.bit_count`, so it
needs `>= 3.10`; the repo's default `python3` is 3.8 and cannot run it —
the receipt now carries a version guard that says so instead of
crashing), **38 PASS / 0 FAIL, 5 delivered outcomes, wall clock
523.6 s**. Exit 0, which by this receipt's own declared semantics is a
statement about the G0/G1 anchors and **not** a summary of the `FAIL`
count.
Parents: D71c (`note-d71c-spin2-archaeology.md`), v2 paper 10 Prop 10.6,
v6 paper 4 `:1064` (`FAILS-FULL-GR`), v6 paper 54, D63/D67.

Every number below is quoted from the receipt's own stdout. **Where the
receipt and this note disagree, the receipt is authoritative.** Where a
number is the round's and was not recomputed here, it is tagged
`[ROUND 1, cited]`.

---

## 0. The one-paragraph answer

**The fixture first, because it changes what every other number means.**
`v7/code/p30_reflection_positive_campaign.py:394-406` was lifted by AST
extraction and its seven committed principal minors reproduced
**character for character** against paper 30 `:2991-2997`; the matrix
itself was then printed — the corpus printed the minors and never
printed the matrix — and it is **not** a multiple of the identity and
**not** diagonal at `N = 9`. That much stands. But the three dual pairs
that Gram is built on are the ones paper 30 `§26.2` **audits and
falsifies**: they rank **11th** in the `N = 9` frontier, and the number
this unit's first delivery called "the committed `TV_9`",
`1.67603622405300634803560e-5`, is the score paper 30 prints for the
loser, directly above the sentence *"So the previous theorem target is
falsified if read as a final predictive law."* Paper 30 `§27` then
selects `{(912,25104), (17288,525076), (24576,540672)}` by a
record-intrinsic admissibility rule, at `TV9 = 0` and `rec9 = 0`
**exactly**. All four of `§26.2`'s frontier triples are re-run here
through p30's own `weights_by_mode(..., pairs=T)` and all four reproduce
`TV_9 = 0` as an exact Fraction with the paper's own atom counts
(`65703 / 65570 / 65544 / 65523`). **So `1.676e-5` is not "the family's
floor". It is a sector-selection residual — paper 30 drives it to zero
by changing which flags to look at — and no function whatever of the
even 3-vector can reach it. The first delivery's central negative,
"eleven quadratic forms and nothing moved", was guaranteed by the
fixture and discovered nothing about the even channel.**

**What survives is the better half.** Rebuilt on the **selected**
triple, the even Gram is *more* anisotropic, not less: off-diagonals
`25.0626 / 29.3697 / 17.3517`, all three nonzero, three distinct
diagonal entries, `S_3` stabiliser of order **1**, anisotropy ratio
**`0.511428`** against the falsified fixture's `0.395835`. **F1 does not
fire on either fixture, and P2's factual half — the corpus computed a
rank-2 object on the even channel and priced its trace — is confirmed
where it counts.** Re-posed on the selected fixture, where the floor is
`0`, the trace, the componentwise ceiling and that fixture's own Gram as
`N` all attain `TV_9 = 0` exactly, while the two `h`-identity-breaking
controls are punished — so the promotion still buys nothing, but now for
an honest reason (there is nothing left to buy) on an instrument that is
demonstrably live. And the *mechanism* for "they all agree" is not the
unproved monotonicity lemma the first delivery argued from: it is the
**`h`-weight identity** — a candidate whose atom-average weight function
equals `full`'s at every record has an identical `forward_tv` by
construction — gated here at 18 candidates across both fixtures with
zero mismatches.

---

## 1. Gate-by-gate

| gate | verdict | what it settles |
|---|---|---|
| **G0-a/b/c** (3 anchors) | **PASS ×3** | the campaign, the primitives and the *committed numbers* are each a single source. **Round 1's repair:** G0-c now text-slices `§26.2`'s frontier table, the fence naming the old target, the fence printing its rank-11 score, and `§27`'s selected triple — the four slices whose absence produced the BLOCKER. |
| **G1-a/b/c** | **PASS ×3** [ANCHOR] | record census `[1,2,5,16,63,315,1956,14794,131526]`; the seven committed even principal minors string-for-string; the odd diagonal and the seven `i`-twisted minors. |
| **G1-d** | **PASS** [ANCHOR] | paper 30 `§25.3`'s `L1 / L2 / Linf` rows reproduce, atoms **and** 24-digit `TV_9`: `66039 / 66057 / 66036`. |
| **G1-e** | **PASS** [ANCHOR] | the two ceiling identities — **with the correctly targeted control.** The even axis is ablated by `odd_abs`, not by `known`: removing the even coordinate entirely costs **`43.1×`**. |
| **G1-f** | **PASS** [ANCHOR] | **THE BLOCKER, GATED AT ITS SOURCE.** All four `§26.2` frontier triples reproduce `TV9 = 0` and `rec9 = 0` exactly with the paper's atom counts; this unit's first anchor **is** the paper's "old reflection-positive target"; its `TV_9` string is character-identical to the loser's score. |
| **G1-g** | **PASS** [ANCHOR] | **THE SELECTED FIXTURE.** `§27`'s triple scores `TV_9 = 0` for `full`, `even_abs` and `agg_l2` alike, atoms `65523`. The floor is `0`. |
| **G2-a…G2-h** | **PASS ×8** | symmetry-for-a-reason; **F1 decided, does not fire**; the reflection is the identity on the even channel; three distinct eigenvalues, discriminant exactly `> 0`; anisotropy nonzero, reported as a minority; survives centring; survives reweighting; the `N = 5` Gram exactly diagonal by disjoint support. |
| **G2-i** | **PASS** | **THE GENUINE G2 SURVIVOR.** The same Gram on `§27`'s selected triple: 3/3 nonzero off-diagonals, 3 distinct diagonal entries, `S_3` stabiliser order **1**, anisotropy **`0.511428` > `0.395835`**. F1's non-firing is not a fixture artefact. |
| **G3-a** | PASS | operationalization fidelity gated **on both fixtures** before anything is promoted. |
| **G3-b** | PASS | **F2 does not fire** — the quadratic matches the falsified fixture's committed `TV_9`. |
| **G3-c** | PASS | **[MEASURED, no longer `[THEOREM]`]** No candidate moves the number *on that fixture* — and the first delivery's *reason* is retracted: monotonicity of `TV_9` under refinement was asserted, never proved, and the committed table itself contains a counterexample to its premise (`agg_linf` has fewer atoms than `agg_l1` and a **better** `TV_9`). |
| **G3-d** | PASS | dual conjugation, atom identity and non-lookup hold for all 11 candidates. |
| **G3-e** | PASS | at `N = 9` the trace is lossy as a colouring (`66057 → 66059`) and lossless as a predictor — **two senses of "lossless" disagree there**, which is narrower than the first delivery's headline. |
| **G3-e2** | PASS | **F1's IMPLICATION IS NOWHERE VIOLATED IN THE WINDOW.** The refinement comparison run across `N = 5..9` instead of at `N = 9` alone: the trace is exactly as fine as componentwise at `N = 5, 6, 7` and becomes lossy at `N = 8` — one step *after* the off-diagonal switches fully on. And the effect is 2 atoms in 66057, against 98.9 % of the *observable's* distinctions destroyed. |
| **G3-f** | PASS | **THE BLOCKER'S REPAIR.** The promoted-`K` question re-posed on the selected fixture: trace, componentwise and the fixture's own Gram all at `TV_9 = 0` exactly; the two `h`-identity controls move it off zero. |
| **G3-g** | PASS | **THE MECHANISM.** `max_R |h(R) − h_full(R)| = 0` **iff** the candidate lands on that fixture's baseline `TV_9`, at 18 candidates over two fixtures, zero mismatches. |
| **G3-h** | PASS | **the eleven rows are TWO colourings** (9 + 2), computed by canonical relabelling of the blocks, not inferred. |
| **G4-a** | PASS | the per-record object is rank ≤ 1 — **labelled the triviality it is**; the measured content is that all three `2×2` minors vanish at every record and that `3862` records carry `E(R) = 0`. |
| **G4-b** | PASS | `S_3` stabiliser of `G^even` = order **1**; the order-dual acts trivially; no sign freedom. |
| **G4-c** | PASS | the `FAILS-FULL-GR` answer — with the units corrected: `789150` is **p4's counting rule applied to D73's record count**, *not* "p4's own units", and is *not commensurable* with p4's `8193`. |
| **G4-d** | PASS | the Prop-10.6 relation, stated as a *distinction*, with the one shared datum located. |
| **G5 / G5-b / G5-c** | **PASS ×3** [SAMPLED] | **the transfer probe, swept and inverted** — seven blueprints; the winner's 59 charts are **two** matrices; every `DOUBLE-RING` is 100 % stabiliser-8; `wide_brick(8,14,2)` breaks the uniformity at 5 of 12; the narrow control **measured**, and **4 of its 42 charts are exactly `(1/4)I` — F1's literal condition firing on the v10 side.** |
| **G6-a/b/c** | **PASS ×3** | every gate predicate parsed, none flagged, the hoisting defect named; determinism under `PYTHONHASHSEED 0/7/999`; the `7I` negative control. |
| **[F3]** | **OPEN, EXPLICITLY DEFERRED** | not decided — and now *visibly* not decided (`§11.3`). |

Exit 1 was reachable only at G0/G1 and was not reached. **`exit 0` is a
statement about the anchors and nothing else — it is not a summary of
the `FAIL` count, and this note does not quote it as one.**

---

## 2. The matrix the corpus never printed — on both fixtures

`G^even_{jk} = Σ_R P(R) E_j(R) E_k(R*)` at `N = 9`.

**On the falsified `§25` triple** `((24576,540672), (25488,525208),
(24606,549648))`, exact:

```text
  17902637/181440        411581/30240       1623817/90720
     411581/30240         203491/5040            6331/378
    1623817/90720             6331/378          57923/1620
```

```text
  98.6697365520282187   13.6104828042328042   17.8992173721340388
  13.6104828042328042   40.3751984126984127   16.7486772486772487
  17.8992173721340388   16.7486772486772487   35.7549382716049383
```

| quantity | value |
|---|---|
| eigenvalues (float port of certified rational brackets) | `108.044928115558159`, `45.922634116580272`, `20.832311004193138` |
| cubic discriminant (exact) | `1.84785e10 > 0` — three distinct real roots |
| condition number `λ_max/λ_min` | `5.18641105607` |
| `‖G − (tr/3)I‖²_F` / `‖G‖²_F` | `0.283583072514` |
| anisotropy ratio `‖traceless‖²_F / (tr²/3)` | `0.395835248491` |
| channel means `μ` | `(63/10, 21/5, 21/5)` — **channels 2 and 3 coincide** |
| `Cov = G − μμᵀ` off-diagonals | `−12.8495, −8.5608, −0.8913` — **all negative**; anisotropy `0.4455` |
| raw (class-uniform) off-diagonals | `14.1265, 15.6007, 20.5577`; anisotropy `0.2814` |
| `S_3` stabiliser | order **1** |

**On the `§27` SELECTED triple** `((912,25104), (17288,525076),
(24576,540672))` — the object the first delivery never built, exact:

```text
     203491/5040          378947/15120          44407/1512
    378947/15120           399649/9072         157415/9072
      44407/1512           157415/9072      17902637/181440
```

```text
  40.3751984126984127   25.0626322751322751   29.3697089947089947
  25.0626322751322751   44.0530202821869489   17.3517416225749559
  29.3697089947089947   17.3517416225749559   98.6697365520282187
```

(The two fixtures share the pair `(24576,540672)`, so `98.6697…` and
`40.3751…` recur — diagonal entries of a shared channel. Every
off-diagonal is new.)

| quantity | falsified `§25` fixture | **SELECTED `§27` fixture** |
|---|---|---|
| nonzero off-diagonals | 3 / 3 | **3 / 3** |
| distinct diagonal entries | 3 | **3** |
| anisotropy ratio | `0.395835248491` | **`0.511428065828`** |
| `S_3` stabiliser order | 1 | **1** |
| cubic discriminant | `1.84785e10 > 0` | **`5.840335e10 > 0`** |
| the whole family's `TV_9` floor | `1.676e-5` — a **sector residual** | **`0` exactly** |

Both were computed through p30's own `even_func` + `matrix_entries`,
with `DUAL_PAIRS` rebound in the lifted namespace and gated restored;
each selected pair is first gated to be a genuine order-dual pair
(`dual_key(left, 5) == right`), exactly as G2-c gates the old ones.

> **P2's factual claim — that the corpus computed a rank-2 object on the
> even channel and threw it away — is confirmed, and confirmed *more
> strongly* on the fixture the corpus's own selection rule chose.**

---

## 3. F1, decided — and the conviction of the pin, retracted

**The retraction first, because the first delivery's opening sentence
was wrong.** F1 as pinned reads: *"`G^even_{jk}` is diagonal, or is a
multiple of the identity. **Then** `E_total` is lossless, `K` is
correctly scalar, and the even channel provably cannot host a metric."*
That is an **implication**. It says nothing whatever about what follows
from a *non*-diagonal Gram. The first delivery attributed the
**converse** to it — "a non-identity Gram implies `E_total` is lossy in
the sense that matters" — found the converse false, and reported the pin
refuted "as a biconditional". **The converse is not in the pin. A pin
frozen before the code is the one document a unit may not rewrite, and
this was the unit's headline.** `[RETRACTED]`

**And the implication survives the entire declared window.** The
refinement comparison, now run at every `N` in the window rather than at
`N = 9` alone:

| `N` | trace atoms | componentwise atoms | trace lossy as a colouring? | Gram diagonal? |
|---:|---:|---:|---|---|
| 5 | 39 | 39 | **no** | **yes** (`diag(1/20,1/30,1/30)`) |
| 6 | 181 | 181 | **no** | half (2/3 off-diagonals zero) |
| 7 | 1027 | 1027 | **no** | no |
| 8 | 7559 | 7561 | yes (+2) | no |
| 9 | 66057 | 66059 | yes (+2) | no |

At `N = 5`, **where F1's antecedent holds, the consequent holds too**.
The off-diagonal switches fully on at `N = 7` and the colouring becomes
lossy at `N = 8` — a one-step **lag**, which is the opposite of "the two
halves come apart". What the unit actually established is that F1's
*antecedent* is `N`-dependent (a real and useful finding) and that at
`N = 9` two senses of "lossless" disagree. Neither is a refutation of
the pin.

The `N = 5` mechanism is structural and gated, not observed: the three
even channels count **5-element** induced subposets, so at `N = 5` every
record has exactly one `flags5` entry, of value 1; the three channel
indicators have **disjoint support** (0 of 63 records carry two channels
at once) and `E_a E_b ≡ 0` for `a ≠ b`.

> **The off-diagonal is generated by record depth exceeding the flag
> size.** Round 1 sharpened this correctly and the sharpening is
> adopted: **that is a statement that the fixture must exceed the flag
> size for the observable to be defined at second order, not a statement
> that the off-diagonal is an artefact.** Records are depth-graded
> objects in this corpus; "generated by depth" is not a category of
> unreality here. The `N = 5` row is the *least* informative row in the
> table, not the sharpest — it is the one regime where the observable is
> degenerate by construction.

**The deflation standard, applied symmetrically.** The first delivery
deflated its own positive result and not its negative one. Stated in
full, as the receipt now prints it: at `N = 9` the even 3-vector takes
**4505** distinct values over the 131526 records and the trace collapses
them onto **49** — destroying 98.9 % of the even channel's distinctions
— **and the atom count moves by two**. Essentially all of the separating
is done by p30's `known` base coordinate, not by the even channel. *"The
trace genuinely discards information"* is true of the **observable** and
very nearly false of the **colouring**. By contrast the anisotropy is
present at every `N` in the window and rises monotonically
`0.0408 → 0.0882 → 0.1732 → 0.2812 → 0.3958` with no sign of saturating.

---

## 4. What the "reflected Gram" actually is — the deflation

Each of the three `DUAL_PAIRS` is gated to be a genuine order-dual pair
of 5-element record types (`dual_key(left, 5) == right`). It follows —
and the receipt verifies it exhaustively, **0 violations in 394578
tests** — that

```text
  E_j(R*) = +E_j(R)      O_j(R*) = -O_j(R)
```

identically. Therefore, as exact Fraction identities: the **reflected**
even Gram **equals** the ordinary second-moment matrix `E[E_j E_k]`, and
the **reflected** odd Gram **equals** `−E[O_j O_k]`.

So paper 30 `§25.4`'s two results are algebra, not measurement. "The
even sector's reflected Gram is positive semidefinite" is the statement
that a second-moment matrix of three real observables is PSD — true of
every such matrix. **The `i`-twist is not a discovery about the odd
channel; it is the sign the grading puts there by construction.**
`[MEASURED]`, and this note claims nothing about whether paper 30
believed otherwise.

Round 1 checked this section independently, found it clean, and
**strengthened it**: Osterwalder–Schrader reflection positivity also
requires a half-space support restriction on the test functions, and
p30's Gram has none at all — so `§25.4` is not a *weakened*
reflection-positivity statement, it is a *differently-shaped* one.
`[ROUND 1, cited]`

What survives as content: the odd channel's means are **exactly zero**
in all three channels, and its off-diagonals are mixed-sign (`−0.01220,
−5.64990, +0.39107`) — so the odd sector's off-diagonal structure, which
paper 30 never scanned (it swept 253 *diagonal* `M`), is nontrivial and
remains unexplored. That is residue 4.

---

## 5. The quadratic promotion: what actually happened

### 5.1 On the falsified fixture — a question that could not have an answer

`K(E) = k·E_total` was replaced by `K(E) = EᵀNE` in **exactly one slot**
of p30's own `colors_for_mode(..., 'agg_l2')` branch; a fidelity gate
(G3-a) requires the promoted colouring to reproduce p30's `agg_l2`
colour dictionary key-for-key at every `N` in the window, on **both**
fixtures, before anything is measured. All eleven candidates — the
identity, the Gram, its adjugate, its covariance, two diagonals, two
off-diagonal forms, a linear control and the componentwise ceiling —
land on `1.67603622405300634803560e-5` exactly, with zero dual
conjugation error, zero coarsening violations and zero `h`-difference.

**That is the rank-11 target's score, and the residual it names is a
sector-selection artefact** (G1-f): it is the error the *full
componentwise colouring of those three pairs* cannot remove, and it
lives in the choice of which flags to look at, where no function of the
even 3-vector can reach it. **"Nothing moved" was fixture-guaranteed.**
`pair_values`, `colors_for_mode` and `weights_by_mode` all take `pairs`
as an argument precisely so this can be varied; the first delivery
lifted all three and then hard-coded `DUAL_PAIRS` at every call site.

**And it is not eleven tests.** Every `colors_for_K` colour is
`(base, (fn(E), Σ O_j²))`, so every candidate's partition is a
coarsening of `comp`'s; a coarsening has strictly fewer atoms unless it
merges nothing, i.e. unless it *equals* `comp`. Computed directly by
canonical relabelling of the blocks (G3-h): **eleven rows, two
colourings** — nine are literally `comp`'s partition, and `lin` and
`quad-OD1` are literally each other's (`EᵀJE = (ΣE_j)²` is a bijection
of `ΣE_j` on nonnegative integers). The table's visual weight overstates
the evidence by a factor of five and a half.

### 5.2 On the selected fixture — the question re-posed

| candidate, `§27` fixture | atoms₉ | `TV_9` | `max_R \|h − h_full\|` |
|---|---:|---|---:|
| `k·E_total` (the trace) | 65523 | **`0`** | 0 |
| componentwise `(E₁,E₂,E₃)` | 65525 | **`0`** | 0 |
| `N = G^even(SELECTED)` | 65525 | **`0`** | 0 |
| `K(E) = E₃` only | 65511 | `2.29303211214171225609383e-5` | 8/3 |
| `K(E) = (ΣE_j) mod 2` | 65496 | `1.08654141668609553205786e-4` | 8/3 |

The floor is `0`; the trace attains it; so does the Gram-as-`N`; and a
wrong `K` is **visibly punished**. The promotion still buys nothing —
but for an honest reason (there is nothing left to buy), on an
instrument that is demonstrably live rather than fixture-dead.

### 5.3 The mechanism: the `h`-weight identity, not a monotonicity lemma

The first delivery argued: *any `K` is a function of `E`, so its
colouring coarsens the componentwise one, so
`TV_9(any N) ≥ TV_9(comp) ≥ TV_9(full)`; the trace already sits at the
family's floor.* The second step assumes **`TV_9` is monotone under
refinement of the colouring**. That was asserted in prose, never proved,
never gated — and it is not a general fact. `forward_tv` is a nonlinear
forward propagation of `exact_by_n[1]` through eight `forward_step`s
built from *ratios* of atom-average weights. **The committed table
itself contains a counterexample to the premise: `agg_linf` has *fewer*
atoms than `agg_l1` (66036 vs 66039) and a *better* `TV_9` (3.77e-5 vs
4.65e-5).** The `[THEOREM at the fixture]` label is **removed**;
licensed claim 5 is now `[MEASURED]`.

The correct mechanism was already in the receipt's own G3-d, unnoticed:
**`max h-difference 0 at 11/11`.** `forward_tv` depends on a colouring
*only* through its atom-average weight function `h`; if a candidate's
`h` is identical to `full`'s at every record, its `forward_tv` is
identical **by construction, in one line, with no assumption about
partition order**. That is why the candidates agree to the twentieth
decimal, and it is paper 30's own `§25.5` exact atom identity restated —
not a new result. G3-g now gates the biconditional across both fixtures:
**`max_R |h − h_full| = 0` iff the candidate lands on that fixture's
baseline `TV_9`, at 18 candidates, zero mismatches**, with
`h`-identity-breaking controls on each fixture as the non-vacuity half
(falsified fixture: `E₃`-only costs `41.729×` at `h`-difference 1;
`(ΣE_j) mod 2` costs `43.051×` at `h`-difference 8/3).

Round 1 ran a wider hunt than this unit did — fourteen functions of the
even 3-vector — and found the correlation exact and total: *every*
candidate with `max|h − h_full| = 0` lands on the committed value and
*every* candidate with `max|h − h_full| ≠ 0` moves it; none came in
below. It also notes that `max E_j` is **not** a quadratic form and also
sits at the value, so "the family" whose value the trace attains is much
larger than `{EᵀNE}`. `[ROUND 1, cited; the two controls above were
re-run here]`

---

## 6. The `FAILS-FULL-GR` answer

v6 paper 4 `:1064` rejected the scalar→tensor shortcut on a component
count: *"a scalar potential equation has one response component per
screen atom; a two-dimensional symmetric tensor equation has three
components per atom, with differential constraints"* —
`missing_components = 8193`, verdict `FAILS-FULL-GR`.

**Half-cleared, still failing, and for a sharper reason.**

1. **Cleared, globally.** `G^even` supplies **6** independent components
   where `K(E) = k·E_total` supplied **1**.
2. **Failed, at the level p4 actually stated it.** Those 6 components are
   **one global form** for the entire `N = 9` window; p4's row counts
   components *per atom*. Applying p4's **counting rule** to D73's record
   count gives `6 × 131526 − 6 = 789150`. **THE UNITS, CORRECTED (round
   1's MODERATE 4): that is *not* "in p4's own units" and must never be
   quoted as such.** p4's `8193` is a component count on a
   **2-dimensional screen** at that paper's own grid resolution; D73's
   `6` is `dim Sym²(R³)` on an index of three named 5-element record
   types, and `131526` counts record classes. The index has no dimension
   in the geometric sense, the atoms are not screen atoms, and **the two
   numbers are not commensurable.** p4's own receipt is absent from the
   tree and `8193` was **not recomputed**. `[STATED, not verified — and
   the qualification travels with the number.]`
3. **Failed again — and this one is a triviality, labelled as one.** The
   per-record summand is `E_j(R)E_k(R)`, an outer product, rank ≤ 1. But
   `vvᵀ` has rank ≤ 1 for *every* vector `v`, so this is true of every
   second-moment matrix ever written down; the first delivery presented
   it as a third independent failure mode "at a level p4 never needed",
   which gave a triviality the weight of a finding, on a gate predicate
   that could not fail. `[RETRACTED as a finding.]` What is measured:
   all three `2×2` minors vanish at every one of the 131526 records
   (computed, not read off the census key), and `3862` records carry
   `E(R) = 0`. The content is only that **rank 3 appears solely after
   averaging**.
4. **Failed a third time, on equivariance — the decisive one.** A metric
   response must transform, `N → A N Aᵀ`, under whatever acts on the
   index it carries. Three candidates, all empty: the order-dual `*`
   acts **trivially** on the even index and as a **sign** on the odd one;
   the `S_3` stabiliser of `G^even` is the **identity alone** (**on both
   fixtures**); and every `E_j` is a nonnegative count, so the basis is
   **canonically oriented** and no analogue of Prop 10.6's frame flip
   exists.

> **A scalar did not become a metric by interpretation. It became a
> covariance matrix, which is a different thing.**

---

## 7. The Prop-10.6 relation, stated carefully

**This is the unit's biggest risk of being misquoted, so the statement is
made twice and gated once (G4-d).** Round 1 examined this section
independently and had no objection to any part of it; it stands
unchanged.

v2 paper 10 Prop 10.6 is an all-order no-go: the **signed** off-diagonal
`h^{12}` of a *frame* metric cannot be recovered from `Γ`-level
(endpoint-probability) data, because the staggered conjugation `S_2`
flips `h^{12}` while leaving every Born-squared kernel invariant.

> **`G^even₁₂ ≠ 0` is NOT a counterexample to Prop 10.6 and must never be
> cited as one.**

Reason, the same both ways: `G^even` is built **from** the endpoint
measure `P(R)`, so by Prop 10.6's own argument it is invariant under any
representational sign flip. Its off-diagonal is nonzero **not** because
the shadow recovered an orientation, but because the channel basis is
*canonically oriented by counting*. The two objects live on different
index sets and have different symmetry groups (a frame `Z/2` versus
nothing at all).

What they **do** share, located exactly: **the orientation datum sits in
the odd sector in both.** The even Gram is blind to the order-dual; the
odd Gram changes sign under it. It is a structural correspondence, not a
numerical one, and no numerical relation is claimed. `[STATED, not
computed]`

---

## 8. The transfer probe `[SAMPLED]` — **the hint INVERTS**

The first delivery ran one blueprint at one depth, printed one example
matrix and a stabiliser histogram, and concluded that *"the index a
rank-2 object should live on is the generated line's DIRECTION index,
not v7's channel index"*. **That conclusion is WITHDRAWN. On this
unit's own evidence, swept, the direction index is the *worse* stage.**

**(a) It is not a field. It is a constant.** D63's winner
`DOUBLE-RING(8,10,8)` (177 events) carries 59 wide charts at `d = 2` —
and **exactly two distinct matrices** among them (51 + 8). A metric
response is an object that *varies over its base*; this one takes two
values on a 177-event crystal. The first delivery printed one example
and a histogram, both blind to the collapse, and never counted distinct
matrices.

| matrix | charts | first row (sorted order) | eigenvalues (exact, certified by exact eigenvectors) | structure |
|---|---:|---|---|---|
| A | 51 | `(3/8, 1/8, 1/4, 1/8)` | `{7/8, 3/8, 1/8, 1/8}` — **3** distinct | `D_4`-invariant, one **repeated** eigenvalue |
| B | 8 | `(2/7, 0, 1/7, 0)` | `{3/7, 3/7, 1/7, 1/7}` — **2** distinct | **block-decomposable**: `{d0,d2}` and `{d1,d3}` never co-occur |

(Both are symmetric circulants in the canonical sorted order, so their
spectra are exact; the receipt prints the same multisets in eigenvector
order — `7/8, 1/8, 1/8, 3/8` and `3/7, 1/7, 1/7, 3/7` — and certifies
each eigenvalue against an exact rational eigenvector.)

**(c) The spectra are degenerate.** Matrix B has only **two** distinct
eigenvalues, each doubled, and is a direct sum of two `2×2` blocks
wearing a `4×4` index. Against v7's three *distinct* eigenvalues
`108.04 / 45.92 / 20.83`, **the v10 forms are the more degenerate
objects.**

**(b) A large stabiliser is *less* metric data, not more — and this
receipt's own negative control says so.** G4-b's criterion is correct:
*a metric response must transform under whatever acts on the index it
carries.* But what the census measures is the **stabiliser**, the
subgroup that *fixes* the form — and a bigger stabiliser means *fewer*
independent components. With a trivial stabiliser v7's Gram is a generic
point of the 6-dimensional `Sym²(R³)`; a `D_4`-invariant `4×4` symmetric
form is confined to the **3-dimensional** span `{I, adjacent, opposite}`
inside the 10-dimensional `Sym²(R⁴)` — which is exactly the observed
`(3/8, 1/8, 1/4)` shape. **And G6-c, this receipt's own demonstration
that "the F1 instrument fires when F1 is TRUE", is a `7I` whose `S_3`
stabiliser is the full group of order 6. By the unit's own construction
a large stabiliser is the *death* condition — and `§8` then offered
order 8 of 24 as the promising lead.**

**The uniformity is hand-built, not substrate.** The sweep that the
false uniqueness claim suppressed (each blueprint builds in about a
second):

| blueprint | events | wide charts | distinct matrices | stabiliser census | identity-proportional |
|---|---:|---:|---:|---|---:|
| `DOUBLE-RING(8,10,8)` (winner) | 177 | 59 | **2** | `{(4,8): 59}` | 0 |
| `DOUBLE-RING(6,14,6)` | 181 | 71 | **2** | `{(4,8): 71}` | 0 |
| `DOUBLE-RING(4,26,4)` | 217 | 97 | **2** | `{(4,8): 97}` | 0 |
| `DOUBLE-RING(4,10,4)` | 89 | 33 | **2** | `{(4,8): 33}` | 0 |
| `DOUBLE-RING(8,10,2)` | 117 | 8 | 3 | `{(4,8): 8}` | 0 |
| `wide_brick(8,14,2)` | 121 | 12 | 4 | **`{(4,8): 7, (4,2): 5}`** | 0 |
| `brick(8,14)` (narrow, `|D| ≥ 3`) | 65 | 42 | 5 | **`{(3,6): 38, (3,2): 4}`** | **4** |

Every `DOUBLE-RING` gives 100 % stabiliser-8 and exactly two matrices,
**because a double ring is built with cyclic symmetry and the direction
index inherits it.** The first delivery's disclaimer offered the wrong
alternative — "substrate symmetry *or* arithmetic coincidence of one
small circuit"; the real alternative is "substrate symmetry *or* the
symmetry the blueprint was hand-built with", and the sweep says the
latter. The uniformity breaks on the very first non-ring wide record:
`wide_brick(8,14,2)` gives **5 of 12** charts at stabiliser **2**. And
`§8`'s first-paragraph claim that the winner was *"the only
configuration D63 found carrying 4-direction charts at `d = 2`"* is
**false** and is withdrawn: several D63 configurations carry them; the
winner wins on a composed tiling-plus-width criterion.

**The narrow control, measured — and it fires F1 on the v10 side.** The
first delivery built it, computed its Grams and reported only
`len(CGn)`, so it controlled nothing. Measured: of 42 narrow charts
(`|D| = 3`, the *same index size as v7's three channels*), **4 have a
direction Gram equal to exactly `(1/4)·I`** — F1's literal antecedent,
*a multiple of the identity* — 34 are the maximally symmetric
`(1/4)I + (1/4)J`, and **38 of 42 carry the full `S_3` stabiliser of
order 6**. On the comparator blueprint the direction Gram is *more*
isotropic than v7's channel Gram, sometimes exactly `λI`.

**And it is not the same treatment.** v7's object is
`Σ_R P(R) E_j(R) E_k(R*)`: a second moment of integer **counts**, under
the **order-dual reflection**, against the pushforward of the uniform
permutation measure. The v10 object is
`Σ_rows (1/|rows|) 1[d ∈ row] 1[d' ∈ row]`: a co-occurrence of **0/1
indicators**, with **no reflection at all**, against a uniform measure on
shadow rows. Three of the four ingredients differ and the missing one is
the reflection — the entire subject of `§4`. It is a second-moment
matrix, so its positive semidefiniteness is the same tautology `§4`
deflates, and "59 anisotropic, 0 identity-proportional" is the same
non-result. `[MINOR 5]` "Circulant" holds in the **canonical sorted
direction order** only; the invariant statement is the stabiliser order,
and better the isomorphism type `D_4`.

> **THE REDIRECTION'S REDIRECTION `[MY READING]` — guidance, not a
> claim, and licensed by nothing here.** The v10 direction Grams *as
> measured* are more degenerate and more symmetric than v7's channel
> Gram. The one defensible part of the original hint is conceptual and
> the census neither tests nor supports it: a chart's direction index is
> something a group *could* act on, where a list of three named record
> types is not. **If a rank-2 object on this programme is ever to be a
> form rather than a table, it needs a stage with *generic* direction
> geometry — stabiliser 1 — which means charts WITHOUT hand-built
> symmetry: sprinkling-like substrates, or crystals with deliberate
> defects. A form with a big stabiliser is a cage, not a metric.**

`[SAMPLED]`, seven blueprints, one depth. Nothing in `§2–§7` depends on
any of it.

---

## 9. Licensed claims, fixture-scoped

Every claim below names **which of two fixtures** it is about: the
falsified `§25` triple (rank 11 in paper 30's own `N = 9` frontier) or
the `§27` SELECTED triple (`TV9 = 0`). Both are the `N = 5..9` record
window of v7 paper 30's rooted boundary law under one measure. No
gravity claim, no continuum claim, and no claim that any object here is
a metric.

1. `[MEASURED, N = 9, BOTH FIXTURES]` `G^even` is a positive-definite
   symmetric form with three distinct nonzero off-diagonals and three
   distinct diagonal entries; eigenvalues
   `108.0449 / 45.9226 / 20.8323` on the falsified fixture; anisotropy
   ratio `0.395835` there and **`0.511428`** on the selected one; `S_3`
   stabiliser order 1 on both. **F1 does not fire on either fixture.**
2. `[ANCHOR, GATED]` Paper 30 `§26.2`'s four frontier triples reproduce
   `TV_9 = 0` and `rec9 = 0` exactly with the paper's own atom counts
   `65703 / 65570 / 65544 / 65523`; the triple this unit first anchored
   on is the paper's "old reflection-positive target", which the paper
   ranks 11th and declares falsified as a final predictive law.
3. `[THEOREM at the fixture, gated]` `E_j(R*) = E_j(R)` and
   `O_j(R*) = −O_j(R)` identically; hence the reflected even Gram **is**
   `E[E_jE_k]` and the reflected odd Gram **is** `−E[O_jO_k]`. Paper 30
   `§25.4`'s positivity results are algebraic consequences of the
   grading.
4. `[MEASURED, window]` The `N = 5` Gram is exactly
   `diag(1/20,1/30,1/30)` because the three channel indicators have
   disjoint support at `N = 5`. **F1's literal antecedent holds at
   `N = 5` and fails from `N = 7`; where it holds, F1's consequent holds
   too — F1's implication is nowhere violated in the declared window.**
5. `[MEASURED]` **(was `[THEOREM at the fixture]`; the label is
   withdrawn.)** On the falsified fixture no candidate `K` moves `TV_9`;
   on the selected fixture the trace, the componentwise ceiling and that
   fixture's own Gram all attain `TV_9 = 0` exactly. The **mechanism**
   is the `h`-weight identity (`max_R|h − h_full| = 0` iff the candidate
   lands on the baseline; 18 candidates, two fixtures, zero mismatches),
   **not** monotonicity of `TV_9` under refinement, which is unproved
   and whose premise the committed table itself contradicts.
6. `[MEASURED]` The eleven promoted-`K` rows are **two** colourings
   (9 + 2).
7. `[MEASURED]` The trace is lossy as a colouring only from `N = 8`
   (`66057 → 66059` at `N = 9`, 2 atoms split) and lossless as a
   predictor throughout the window. At `N = 9` the trace destroys 98.9 %
   of the even 3-vector's distinctions (4505 values → 49) and moves the
   atom count by two.
8. `[MEASURED]` The per-record even Gram summand has rank ≤ 1 — **a
   triviality true of every outer product**, measured here as the
   vanishing of all `2×2` minors at all 131526 records. The `S_3`
   stabiliser of `G^even` is trivial on both fixtures; the order-dual
   acts trivially on the even index. **A Gram-derived `N` is an ensemble
   summary statistic, not a metric response.**
9. `[STATED, not computed]` The relation to Prop 10.6 is a *distinction*
   (`§7`). The shared content is that the orientation datum lives in the
   odd sector.
10. `[STATED, not verified, NOT in p4's units]` `789150` is p4's
    counting rule applied to D73's record count; it is not commensurable
    with p4's `8193`, which was not recomputed.
11. `[SAMPLED]` Seven v10 blueprints. The winner's 59 wide charts carry
    **two** distinct direction Grams with repeated eigenvalues, one of
    them block-decomposable; every `DOUBLE-RING` is 100 % stabiliser-8;
    `wide_brick(8,14,2)` breaks it at 5 of 12; the narrow control has
    **4 charts at exactly `(1/4)I`** and 38 of 42 at the maximal
    stabiliser. **The direction index is not shown to be a better stage
    than v7's channel index; on this evidence it is a worse one.**
12. `[MEASURED]` Removing the even coordinate entirely (`odd_abs`) costs
    `43.1×`; removing the odd one (`even_only`) costs `63.7×`; removing
    both (`known`) costs `299.7×`.

**Not licensed, and explicitly disclaimed:** that `G^even₁₂ ≠ 0` evades
Prop 10.6; that anything here is a metric, a response, a field, or a
graviton; that the anisotropy survives to any other window, substrate or
measure; that the v10 charts' stabilisers are substrate symmetries;
**that the direction index is the stage a rank-2 object should live on**;
**that `1.676e-5` is any kind of floor**; and that F3 has been decided.

---

## 10. What this does to P2, and to D71c `§7`

P2 asserted three things.

**Fact one — the corpus computed a rank-2 object on the even channel and
discarded it in favour of its trace — is CONFIRMED**, exactly, at the
named line, and *on the fixture the corpus's own selection rule chose*,
where the object is *more* anisotropic than on the falsified one.

**Fact two — that `K` should be `EᵀNE` — is ADMISSIBLE but EMPTY, and
the first delivery's proof that it must be empty is retracted.** The
promotion passes every gate the committed law imposes and buys nothing.
On the falsified fixture that was guaranteed by the fixture; on the
selected fixture it is a measurement, and it holds because the trace
already carries the whole `h`-weight.

**Fact three — that the orientation is the datum that decides geometry
versus bookkeeping — SURVIVES AND SHARPENS**: the orientation is exactly
what the even channel lacks (its basis is canonically oriented, so there
is no orientation to have) and exactly what the odd channel carries (the
`Z/2` sign). D71c `§4.3`'s parallel — the corpus prices the trace of a
rank-2 object and discards the traceless part — is confirmed at the
mechanical level and **deflated at the significance level**: the
discarded traceless part is a covariance, and it was inert.

**F1 is an implication and needs no restatement; the first delivery's
demand that it be restated is withdrawn.** The no-go the corpus gains,
re-scoped to name its fixtures:

> **D73 no-go (fixture-scoped, two named fixtures).** *At the `N = 5..9`
> window of v7 paper 30's rooted boundary law, under both the falsified
> `§25` dual-pair triple and the `§27` SELECTED one, the dual-even
> channel's second-moment form is anisotropic and positive-definite with
> a trivial relabelling stabiliser, and is nonetheless predictively
> equivalent to its trace for the deletion-graph law: on the selected
> fixture the trace attains `TV_9 = 0` exactly, and the reason no
> promotion improves on it is the `h`-weight identity, not a ceiling.
> The form carries no atom index, has rank 1 locally, and admits no
> group action on its channel index. On this substrate the even channel
> hosts a covariance, not a metric response.*

**What the no-go is NOT.** It is not a statement about "the `N = 5..9`
window of the rooted boundary law" as such — the first delivery's `§10`
used the paper's own phrase for something else. It is a statement about
two named dual-pair triples at one window under one measure.

---

## 11. Residues

1. **The `N`-dependence is unexplained.** The anisotropy ratio rises
   monotonically `0.0408 → 0.3958` across `N = 5..9` on the falsified
   fixture and shows no sign of saturating. Whether it converges,
   diverges or is a finite-`N` artefact of `9!` is **open**; `N = 10` was
   not attempted (the universe build already dominates the runtime at
   `N = 9`).
2. **F4 remains undecided by this unit** (the orientation test /
   cross-link to D71b's P1). That is D72's object.
3. **F3 IS OPEN AND IS NOW EXPLICITLY DEFERRED, NOT DROPPED.** The pin
   pre-registers four falsifiers under a "NO NULL OUTCOME" header. The
   first delivery decided F1 and F2, deferred F4 properly, and **never
   named F3 at all** — round 1 was right to call that a first-class
   omission. F3 asks whether *the anticommutator of the generated line's
   own transports* is symmetric and rank-2. G5 forms a **co-occurrence
   matrix over chart directions**, which is not an anticommutator of the
   generated line's transports under any reading, so **G5 is not an F3
   test and this unit will not relabel it as one.** F3 needs the d42b1
   transport pair itself, symmetrised — a unit of work, not a gate — and
   is carried forward OPEN. No claim in this note rests on it.
4. **The odd sector's off-diagonal is still unexplored.** Paper 30 swept
   253 *diagonal* `M` for `Q_M(O) = OᵀMO` and never scanned the
   off-diagonal sector. Measured here: `−0.01220, −5.64990, +0.39107` —
   mixed sign, one of them large. The obvious successor is the *odd*
   sector promotion, **on the selected fixture** (the old ceiling
   argument that would have made it hopeless is retracted along with the
   monotonicity lemma).
5. **The even channel matters; the decomposition beyond the trace does
   not.** Ablating the even coordinate alone costs `43.1×`. Anyone
   reading `§5` as "the even channel does not matter" has misread it.
6. **The environment fact.** The committed v7 campaign calls
   `int.bit_count()` (`:165`), requiring Python `>= 3.10`; the repo's
   default `python3` is 3.8 and crashes inside a lifted namespace with
   no diagnostic. The receipt now carries a version guard and a
   `python3.13` shebang.
7. **`missing_components = 8193` was not recomputed** and `789150` is
   not in p4's units (`§6.2`). `[STATED]`
8. **The selected fixture's Gram was not swept over `N`, centred, or
   reweighted.** G2-f/G2-g/G2-h were run on the falsified fixture only.
   Whether the selected fixture's `0.511428` also survives centring,
   reweighting and the `N` window is **open**, and it is the cheapest
   remaining question in this unit.
9. **Round 1's fourteen-function hunt was not re-run in full**; two of
   its functions were, as G3-g's controls. `[ROUND 1, cited]`

---

## 12. Successor guidance, honest

The rank-2 hunt has exactly two live routes, and neither is the one the
first delivery pointed at.

1. **Understand the selected v7 fixture's structure.** It is the one
   place in this corpus where a genuinely anisotropic even Gram with a
   trivial stabiliser sits on a law whose forward error is *exactly
   zero*. Why `§27`'s coarseness rule lands on a triple whose second
   moment is *more* anisotropic than the falsified target's is not
   known, and it is a question about the selection rule, not about the
   Gram.
2. **Get charts with generic direction geometry.** Everything the v10
   side offered here is a hand-built crystal whose direction index
   inherits the blueprint's cyclic symmetry — two matrices, `D_4`
   stabilisers, repeated eigenvalues, and a narrow control that is
   sometimes exactly `λI`. A form with a large stabiliser has *fewer*
   free components, not more. **What a tensor stage needs is
   stabiliser-1 direction geometry: sprinkling-like substrates, or
   crystals with defects deliberately introduced.** `[MY READING]`

Everything else this unit produced is a covariance matrix wearing a
metric's index, and the corpus should stop asking it to be a metric.
