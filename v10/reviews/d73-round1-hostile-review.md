# D73 — ROUND 1 INDEPENDENT HOSTILE REVIEW

**Frozen:** 2026-07-27.
**Unit under review:** D73 "the even Gram" — `note-d73-even-gram-pin.md`
(STRICT, frozen, committed before any code was written; it names claim P2,
tests 1–3 and falsifiers F1–F4), `note-d73-even-gram-result.md`
(GREEN-UNREVIEWED), `code/d73_even_gram_exact.py` +
`data/d73_even_gram_exact.out` (29 PASS / 0 FAIL, exit 0, 457.5 s), LOG #488.
Context: `note-d71c-spin2-archaeology.md`.
**Reviewer:** independent Opus 5 worker, no prior context, no loyalty to the
unit, recompute-never-trust. Every number below was produced by code I wrote
for this review (`ref_v7.py`, `ref_v7b.py`, `ref_g5.py`, `ref_g5b.py`, under
the session scratchpad): my own Gram loop (not `matrix_entries`), my own
`E_at`/`O_at`, my own characteristic polynomial and discriminant, an
independent `numpy.linalg.eigvalsh` cross-check of the eigenvalues, my own
window sweep, my own reflection-parity audit, my own stabiliser search, my own
`colors_for_K` and adversarial-`K` hunt, my own chart-Gram builder and
blueprint sweep. The only objects I share with the unit are the committed
layers under test (v7 `p29`/`p30`; v10 `d42b1`/`d47a`/`d58`/`d60`/`d63`),
which no unit may re-implement. Nothing was read out of the unit's `.out`.
Calibration: `reviews/d68-round1-hostile-review.md`,
`reviews/d70-round1-hostile-review.md`; `v7/relativistic-isp-v7-paper30-rooted-boundary-law.md`
(**all of it**, not only §25); v2 paper 10 Prop 10.6; v6 paper 4 `:1064`;
`note-d63-wide-crystal-result.md`.

**VERDICT: REVISE. 1 BLOCKER / 4 MAJOR / 5 MODERATE / 5 MINOR.**

**The arithmetic is flawless.** Every number I checked reproduced exactly, from
my own instrument: the record census `[1,2,5,16,63,315,1956,14794,131526]`;
`G^even` entry-for-entry as exact rationals (`17902637/181440`,
`411581/30240`, `1623817/90720`, `203491/5040`, `6331/378`, `57923/1620`); all
seven principal minors string-for-string against paper 30 `:2991-2997`; the
three odd reflected diagonal entries; the characteristic polynomial and the
exactly-positive discriminant `1.847847e10`; the eigenvalues
`108.04492811555816 / 45.92263411658028 / 20.83231100419313` (independent
`eigvalsh`); the whole `N = 5..9` window including `diag(1/20, 1/30, 1/30)` at
`N = 5` and the monotone anisotropy `0.040816327 → 0.395835248`; the
reflection parity `0 / 0` violations in `394578` tests and
`reflected == unreflected` as an exact Fraction identity; `μ = (63/10, 21/5,
21/5)`; the `S_3` stabiliser of order 1; the rank census `{0: 3862, 1: 127664}`;
the odd off-diagonals `−0.012202 / −5.649901 / +0.391071` and zero odd means;
the six committed mode rows and the `299.7×` ratio; and every `TV_9` in the
promotion table. I also ran fourteen adversarial functions of the even
3-vector and found none below the committed value. **I broke nothing in the
arithmetic. I broke the fixture, the transfer probe's hint, and the unit's
reading of its own falsifier.**

The BLOCKER is a fidelity defect of exactly the kind D68 was convicted of, one
level up: **the unit's "committed law" is the object its own source paper
explicitly declares falsified**, and the unit never read that far into the
paper it anchors on.

---

## BLOCKER — THE FIXTURE IS THE TARGET PAPER 30 ITSELF DECLARES FALSIFIED. "THE COMMITTED `TV_9`" IS THE RANK-11 LOSER, AND "THE FAMILY'S FLOOR" IS NOT THE LAW'S FLOOR.

**Where.** Result `§0` ("the committed `TV_9 = 1.67603622405300634803560e-5`"),
`§1` gates G1-d/G1-e, the whole of `§5`, `§9` licensed claims 4 and 5, the D73
no-go in `§10`, `§11` residue 3; receipt gates G1-d ("The `agg_l2` row IS the
committed instantiation of `K(E) = k.E_total`"), G1-e, G3-b, G3-c, G3-e and
the `[OUTCOME G3 / F2]`; the `[VERDICT]` line; LOG #488 ("all eleven quadratic
forms land on the committed `TV_9` EXACTLY — the trace already sits at the
family's floor").

**Defect.** The unit anchors on paper 30 `§25.3` and `§25.4` and stops there.
Paper 30 `§26.2` — 130 lines further down the same file the receipt text-slices
— audits the `N = 7` zero-TV frontier at `N = 9` and prints this table:

| rank | dual-pair triple | atoms at `N=9` | `TV9` | `rec9` |
| --- | --- | ---: | ---: | ---: |
| 1 | `(772,16904)`, `(896,541184)`, `(25496,525212)` | `65703` | `0` | `0` |
| 2 | `(772,16904)`, `(920,25360)`, `(25488,525208)` | `65570` | `0` | `0` |
| 3 | `(772,16904)`, `(920,25360)`, `(17288,525076)` | `65544` | `0` | `0` |
| 4 | `(912,25104)`, `(17288,525076)`, `(24576,540672)` | `65523` | `0` | `0` |

and then, of D73's fixture, verbatim:

> The old reflection-positive target `((24576,540672), (25488,525208),
> (24606,549648))` ranks only `11` in this audited `N=9` frontier:
> `TV9 = 0.0000167603622405300634803560`, `rec9 = 0.0000171467764060356652949246`.
> **So the previous theorem target is falsified if read as a final predictive
> law.**

`§27` then has the paper's own admissibility rule *select* triple 4, with
`TV9 = 0`, `rec9 = 0`. **D73's `DUAL_PAIRS` is the rank-11 target; the number
D73 calls "the committed `TV_9`" is the number paper 30 prints as the loser's
score; and `rec9 = 1.71467764060356653e-5`, which the receipt reports as
"identical recurrence error" across all eleven candidates, is the same
falsified row.** No sentence in the pin, the result note, the receipt or LOG
#488 mentions `§26.2`, `§27`, the four exact alternatives, or the word
"falsified".

The consequence is not cosmetic. The unit's central negative is that the
promotion "buys nothing" because "the trace already sits at the family's
floor". That floor is `TV_9(full) = 1.676e-5` **on this triple** — i.e. the
residual error that *the full componentwise colouring of these three pairs
cannot remove*. That residual is a **sector-selection** artefact: paper 30
drives it to exactly `0` by changing the pairs. No function whatever of the
even 3-vector can touch an error that lives in the choice of which flags to
look at. **So "nothing moved" was guaranteed by the fixture, not discovered
about the even channel** — and the unit chose the one fixture in paper 30's
frontier where the question it asks cannot have a positive answer.

`pair_values`, `colors_for_mode` and `weights_by_mode` all take `pairs` as an
argument precisely so this can be varied; the receipt lifts all three and then
hard-codes `DUAL_PAIRS` at every call site.

**Recomputation.** I built the `N = 1..9` universe from p30's own builder and
called the lifted `weights_by_mode(mode, pairs=T)` on all five triples:

```
rank1  full atoms 126607 TV9=0     even_abs 65710 TV9=0     agg_l2 65703 TV9=0
rank2  full atoms 124946 TV9=0     even_abs 65585 TV9=0     agg_l2 65570 TV9=0
rank3  full atoms 123691 TV9=0     even_abs 65548 TV9=0     agg_l2 65544 TV9=0
rank4  full atoms 123985 TV9=0     even_abs 65525 TV9=0     agg_l2 65523 TV9=0   <- SELECTED by p30 §27
rank11 full atoms 128678 TV9=0.0000167603622405300634803560  ...  agg_l2 66057  <- D73's fixture
```

All four frontier triples reproduce `TV_9 = 0` exactly, and the atom counts
reproduce paper 30's table (`65703 / 65570 / 65544 / 65523`) to the unit. The
D73 fixture reproduces `1.67603622405300634803560e-5`.

I also built the even Gram on the **selected** triple, which the unit never
did: `off-diagonals 25.0626 / 29.3697 / 17.3517`, `3/3` nonzero, anisotropy
ratio `0.511428` (against the fixture's `0.395835`), `S_3` stabiliser order 1,
all three `DUAL_PAIRS` gates (`dual_key(left,5) == right`) satisfied. **So the
G2 half of the unit — F1 does not fire, the Gram is anisotropic — transfers to
the selected triple and is, if anything, stronger there. It is the G3 half
that does not survive contact.** On the selected triple the floor is `0`, so
the promotion cannot buy anything *for a completely different reason* than the
one `§5` gives, and `§5`'s explanation ("the trace already sits at the family's
floor") is a description of one superseded row.

**Required.** (1) Every occurrence of "the committed `TV_9`", "the committed
law", "the family's floor" and "the receipted law" must be relabelled to name
the rank-11 falsified target and cite `§26.2`. (2) The D73 no-go in `§10` must
be re-scoped: as written it says "at the `N = 5..9` window of the rooted
boundary law", which is the paper's own phrase for something else. (3) G3 must
be re-run on at least one of the four `TV_9 = 0` triples before any claim of
the form "the even channel is predictively trace-only" is made about anything
but the rank-11 row. (4) LOG #488's "the trace already sits at the family's
floor" is corpus-facing and must be corrected first.

---

## MAJOR 1 — THE TRANSFER PROBE'S HINT INVERTS ON ITS OWN EVIDENCE. THE 59 "ANISOTROPIC DIRECTION GRAMS" ARE **TWO MATRICES**, AND A LARGE STABILISER IS THE UNIT'S OWN DEATH CONDITION.

**Where.** Result `§8` and licensed claim 8; receipt G5; `§11` residue 4; LOG
#488's forward-pointing sentence ("the rank-2 object's stage is the DIRECTION
INDEX ... not v7's channel index").

**Defect, three ways.**

**(a) It is not a field. It is a constant, and the constant is shared across
the whole blueprint family.** The note says "all 59 wide charts carry
anisotropic direction-indexed 4×4 circulant Grams". True, and hollow: the 59
charts carry **exactly two distinct matrices** (51 charts share one, 8 share
the other). A metric response is an object that *varies over its base*; this
one takes two values on a 177-event crystal. The receipt prints one example
and a stabiliser histogram, both of which are blind to the collapse, and never
counts distinct matrices.

**(b) A large stabiliser is *less* metric data, not more, and the unit's own
negative control says so.** The note's stated criterion (`§6`, G4-b) is
correct: *"a metric response must transform, `N → A N Aᵀ`, under whatever acts
on the index it carries."* That asks whether a group **acts on the index** —
and `S_3` acts on v7's three channels by relabelling exactly as `S_4` acts on
the four directions; the receipt itself computes an `S_3` stabiliser, so it
already presumes the action. What the census actually measures is the
**stabiliser**, i.e. the subgroup that *fixes* the form — and a bigger
stabiliser means the form is *more constrained*, carrying *fewer* independent
components. Concretely: with a trivial stabiliser the v7 Gram is a generic
point of the 6-dimensional `Sym²(R³)`; with a `D_4` stabiliser a `4×4`
symmetric form is confined to the **3-dimensional** span `{I, adjacent,
opposite}` inside the 10-dimensional `Sym²(R⁴)` — which is exactly the
observed `(3/8, 1/8, 1/4)` shape. **The direction Gram has fewer free
components than the channel Gram, not more.**

The unit's own instrument agrees and the unit does not notice: **G6-c's
negative control is `7I`, whose `S_3` stabiliser is the full group of order 6,
and it is offered as the demonstration that "the F1 instrument fires when F1
is TRUE".** A large stabiliser is, by the unit's own construction, the
*death* condition — and `§8` then presents order 8 of 24 as the promising
lead.

**(c) The spectra are degenerate — one of the two matrices is not even an
irreducible 4-direction form.** Recomputed exactly:

| matrix | charts | first row | eigenvalues | structure |
|---|---:|---|---|---|
| A | 51 | `(3/8, 1/8, 1/4, 1/8)` | `7/8, 3/8, 1/8, 1/8` | `D_4`-invariant, one repeated eigenvalue |
| B | 8 | `(2/7, 0, 1/7, 0)` | `3/7, 3/7, 1/7, 1/7` | **block-decomposable**: `{d0,d2}` and `{d1,d3}` never co-occur |

Matrix B has only **two** distinct eigenvalues, each doubled, and its four
directions split into two mutually invisible pairs — it is a direct sum of two
`2×2` blocks wearing a `4×4` index. Against v7's three *distinct* eigenvalues
`108.04 / 45.92 / 20.83`, the v10 forms are the *more degenerate* objects.

**Adjudication.** *The direction index is not shown to be a better stage; on
this unit's own evidence it is a worse one.* The one defensible part of the
hint — that a chart's direction index is geometrically meaningful where a list
of three named record types is not — is a conceptual point the census neither
tests nor supports, and it must be made on its own or not at all. As written,
`§8`'s hint and LOG #488's headline sentence run opposite to the data that are
supposed to license them.

**Recomputation.** `ref_g5.py`: 177 events, 59 wide charts at `d = 2`, **2
distinct matrices**, both circulant in sorted-direction order, both with
stabiliser order 8, both with constant diagonal; eigenvalues and row sums as
tabulated above.

---

## MAJOR 2 — "THE ONLY CONFIGURATION D63 FOUND CARRYING 4-DIRECTION CHARTS AT `d = 2`" IS FALSE, AND THE BLUEPRINT SWEEP THAT COSTS SECONDS BREAKS THE UNIFORMITY CLAIM.

**Where.** Result `§8` first paragraph; receipt G5's gate text ("the only
configuration D63 found carrying 4-direction charts at `d = 2`"); `§11`
residue 4 ("one blueprint at one depth").

**Defect.** D63's own interior-control table (`note-d63-wide-crystal-result.md`
`§5`) lists `WIDE-BRICK(8, 14, C = 2)` at width `0.0992`,
`DOUBLE-RING(6, 14, 6)` at `0.3923` and `DOUBLE-RING(4, 26, 4)` at `0.4470`,
and D63's `§3` names `DR(4, 10, 4)` alongside the winner. Width is D58's
`|D| ≥ 4` column. **Several D63 configurations carry 4-direction charts at
`d = 2`; the winner is the winner on a composed tiling+width criterion, not
the only carrier.** The receipt states the uniqueness as fact inside an
`[ANCHOR]`-adjacent gate text and uses it to justify running one blueprint.

Worse, the uniqueness claim is what suppresses the sweep that would have
falsified the census. I ran it — each blueprint builds in about a second:

| blueprint | events | wide charts | distinct matrices | stabiliser census | identity-proportional |
|---|---:|---:|---:|---|---:|
| `DOUBLE-RING(8,10,8)` (winner) | 177 | 59 | **2** | `{(4,8): 59}` | 0 |
| `DOUBLE-RING(6,14,6)` | 181 | 71 | **2** | `{(4,8): 71}` | 0 |
| `DOUBLE-RING(4,26,4)` | 217 | 97 | **2** | `{(4,8): 97}` | 0 |
| `DOUBLE-RING(4,10,4)` | 89 | 33 | **2** | `{(4,8): 33}` | 0 |
| `DOUBLE-RING(8,10,2)` | 117 | 8 | 3 | `{(4,8): 8}` | 0 |
| `wide_brick(8,14,2)` | 121 | 12 | 4 | **`{(4,8): 7, (4,2): 5}`** | 0 |
| `brick(8,14)` (narrow, `\|D\| ≥ 3`) | 65 | 42 | 5 | **`{(3,6): 38, (3,2): 4}`** | **4** |

Two things follow. **(i) "Stabiliser 8 at 59/59" is a property of the
`DOUBLE-RING` construction, not of the substrate** — every `DOUBLE-RING`
gives 100 % stabiliser-8 and exactly two matrices, because a double ring is
built with cyclic symmetry and the direction index inherits it. The note's
disclaimer offers the wrong alternative: the choice is not "substrate symmetry
*or* arithmetic coincidence of one small circuit", it is "substrate symmetry
*or* the symmetry the blueprint was hand-built with", and the sweep says the
latter. **(ii) The uniformity breaks on the very first non-ring wide record:**
`wide_brick(8,14,2)` gives `5 of 12` wide charts with stabiliser **2**, not 8.

---

## MAJOR 3 — THE UNIT CONVICTS THE PIN OF A BICONDITIONAL THE PIN DID NOT WRITE, AND F1'S IMPLICATION IS NOWHERE FALSIFIED IN THE DECLARED WINDOW.

**Where.** Result title line and `§0` ("**The pin's F1 is a biconditional and
the two halves come apart**"), `§5` ("the pin's F1 — which asserts that a
non-identity Gram implies `E_total` is lossy in the sense that matters — is
**false as a biconditional**"), `§10` ("F1 must be restated before it is
cited"); receipt G3-e and the `[VERDICT]` line; LOG #488.

**Defect (a): the strawman.** F1 as pinned reads: *"`G^even_{jk}` is diagonal,
or is a multiple of the identity. Then `E_total` is lossless, `K` is correctly
scalar, and the even channel provably cannot host a metric."* That is an
**implication**, antecedent → consequent. It says nothing whatever about what
follows from a *non*-diagonal Gram. The unit attributes to F1 the converse
("a non-identity Gram implies `E_total` is lossy in the sense that matters"),
finds the converse false, and reports F1 refuted. The converse is not in the
pin. A pin frozen before the code is the one document a unit may not re-write,
and this is the unit's opening sentence.

**Defect (b): the implication is not violated anywhere in the window — I
checked the one place where it could be.** F1's antecedent is TRUE at `N = 5`
(the Gram is exactly `diag(1/20, 1/30, 1/30)`). The unit never tests the
consequent there; it tests losslessness only at `N = 9`, where the antecedent
is false and the test is therefore vacuous. Running the unit's own refinement
comparison across the declared window:

| `N` | trace-colouring atoms | componentwise atoms | trace lossy as a colouring? | Gram diagonal? |
|---:|---:|---:|---|---|
| 5 | 39 | 39 | **no** | **yes** |
| 6 | 181 | 181 | **no** | half (2/3 off-diagonals zero) |
| 7 | 1027 | 1027 | **no** | no |
| 8 | 7559 | 7561 | yes (+2) | no |
| 9 | 66057 | 66059 | yes (+2) | no |

At `N = 5`, where F1's antecedent holds, **the consequent holds too** — the
trace colouring is exactly as fine as the componentwise one. Under the other
reading of "lossless" (predictive), the consequent holds at every `N` in the
window including `N = 5`. **Under either reading, F1's implication survives
the entire declared window.** What the unit actually established is that F1's
*antecedent* is `N`-dependent — a real and useful finding — and that at
`N = 9` two senses of "lossless" disagree. Neither is "the pin's biconditional
is false".

The two halves also track each other far more closely than `§0` suggests: the
Gram's off-diagonal switches fully on at `N = 7` and the colouring becomes
lossy at `N = 8`. A one-step lag between the antecedent failing and the
consequent failing is the *opposite* of "the two halves come apart", and the
unit never saw it because it ran the refinement comparison at `N = 9` only.

**Defect (c): the deflation standard is applied asymmetrically.** The unit
deflates its own positive result with *"the off-diagonal is generated by
record depth exceeding the flag size. It is not a property of the channels."*
Apply the same standard to the unit's self-declared **central measurement**
(G3-e, "the trace is lossy as a colouring"): it is **exactly false at `N = 5,
6 and 7**, appears first at `N = 8`, and amounts to **2 atoms out of 66,057**
(0.003 %) at `N = 9`. The disproportion is worth stating in full, because it
is the real content of G3-e: at `N = 9` the even 3-vector takes **4505
distinct values** over the 131,526 records and the trace collapses them onto
**49**, destroying 98.9 % of the even channel's distinctions — and the atom
count moves by **two**. Essentially all of the separating is being done by
p30's `known` base coordinate, not by the even channel at all. "The trace
genuinely discards information" is true of the *observable* and very nearly
false of the *colouring*. By the unit's own rule the lossiness is depth-generated
too, and by a far thinner margin than the anisotropy (which is present at
every `N` in the window and rises monotonically `0.0408 → 0.3958` with no sign
of saturating). The unit discounts the finding that supports P2 and does not
discount the finding that deflates it.

**On the substance of "depth-generated, not intrinsic": it is not a
deflation.** `E_j` counts 5-element induced subposets. I confirmed the
mechanism and it is sharper than the note states: at `N = 5` **every record
has exactly one flag5 entry, of value 1** — the even 3-vector takes only four
values (`(0,0,0)` on 57 records, and the three unit vectors on 2 records each)
and is a 0/1 indicator of a 6-record subset of 63. There is no bilinear
content at `N = 5` to be anisotropic *or* isotropic; the Gram is the diagonal
matrix of the three channel probabilities and nothing else. A counting
observable of flag size 5 has no second-order structure until the record is
deeper than 5. **That is a statement that the fixture must exceed the flag
size for the observable to be defined at second order, not a statement that
the off-diagonal is an artefact** — and records *are* depth-graded objects in
this corpus, so "generated by depth" is not a category of unreality here. The
`N = 5` row gives F1's literal condition a foothold in the one regime where
the observable is degenerate by construction; `§3`'s "**the sharpest thing the
unit found about F1**" is, on recomputation, the least informative row in the
table.

---

## MAJOR 4 — LICENSED CLAIM 4'S `[THEOREM at the fixture]` LABEL IS UNEARNED: THE STATED MECHANISM IS AN UNPROVEN MONOTONICITY ASSUMPTION, AND THE RECEIPT'S OWN DATA CARRY THE CORRECT ONE.

**Where.** `§9` licensed claim 4 (`[THEOREM at the fixture]`), `§5` ("Hence
`TV_9(any N) ≥ TV_9(componentwise) ≥ TV_9(full)`. … **The trace already sits
at the family's floor.** No search was needed and none would have helped."),
`§0`, `§10`; receipt G3-c.

**Defect.** The stated argument is: *any `K` is a function of `E`, so its
colouring coarsens the componentwise colouring, so its `TV_9` is at least
`TV_9(componentwise)`.* The second step assumes **`TV_9` is monotone under
refinement of the colouring**. That is asserted in prose, is not proved, and
is not gated anywhere in the receipt. It is not obvious and it is not a
general fact: `forward_tv` is a nonlinear forward-propagation error —
`exact_by_n[1]` pushed through eight `forward_step`s built from *ratios* of
atom-average weights, compared in TV against `exact_by_n[9]`. Nothing about
that functional makes it monotone in the partition order, and the committed
table already shows the atom count does not order it (`agg_linf` has **fewer**
atoms than `agg_l1`, 66036 vs 66039, and a **better** `TV_9`, 3.77e-5 vs
4.65e-5). What G3-c actually gates is that eleven named candidates plus `comp`
came in at the committed value — an empirical statement about a finite list,
correctly labelled `[MEASURED]`, not `[THEOREM]`.

**And the receipt already holds the correct, exact mechanism, in the gate next
door.** G3-d reports `max h-difference 0 at 11/11` against `full` — i.e. every
candidate's atom-average weight function is **identical to `full`'s at every
record**. Identical weights give an identical `forward_tv` by construction, in
one line, with no monotonicity needed. That is why the eleven agree to the
twentieth decimal, and it is also paper 30's own committed `§25.5` exact atom
identity restated — not a new result.

**Recomputation.** Fourteen functions of the even 3-vector, run through p30's
unmodified downstream machinery. The correlation is exact and total:

```
                                                       max |h - h_full|   TV_9
trace  Σ E_j            atoms 66057                    0                  == committed
max    max E_j          atoms 66047                    0                  == committed
comp   (E1,E2,E3)       atoms 66059                    0                  == committed
quad-I Σ E_j²           atoms 66059                    0                  == committed
diag(1,2,3) quadratic   atoms 66059                    0                  == committed
E1 only                 atoms 66027                    8/3                2.996x worse
E1 − E2                 atoms 66041                    8/3                2.368x worse
Σ E_j mod 3             atoms 66046                    8/3                3.617x worse
min(Σ E_j, 3)           atoms 65980                    1                  7.003x worse
E3 only                 atoms 66008                    1                 41.729x worse
E2 only / E1·E2         atoms 65999 / 65998            8/3               42.567x worse
Σ E_j mod 2 / K ≡ 0     atoms 65979                    8/3               43.051x worse
```

**Every candidate with `max |h − h_full| = 0` lands exactly on the committed
`TV_9`; every candidate with `max |h − h_full| ≠ 0` moves it.** No candidate
came in below — so the unit's empirical conclusion is corroborated by an
independent and much wider hunt than it ran — but the *reason* is the h-weight
identity, not a ceiling, and the label must be `[MEASURED]` plus the h-identity
argument, or the monotonicity lemma must be proved.

Two further consequences the note should carry. `max E_j` is not a quadratic
form and it also sits at the floor, so "the family" whose floor the trace
attains is much larger than `{EᵀNE}` — which weakens the pin's F2 framing
further.

And **the eleven candidates are not eleven tests — they are two, and this
follows from the receipt's own atom column with no extra computation.** Every
`colors_for_K(n, ·, fn)` colour is `(base, (fn(E), Σ O_j²))`, so every
candidate's partition is a *coarsening* of `comp`'s partition
`(base, (E, Σ O_j²))`. A coarsening has strictly fewer atoms unless it merges
nothing, i.e. unless it **equals** `comp`. Nine candidates (`quad-I`, `quad-G`,
`quad-adj`, `quad-cov`, `quad-D1`, `quad-D2`, `quad-OD2`, `bilin-G`, `comp`)
report `atoms9 = 66059`; therefore all nine induce **literally the same
colouring** as `comp`. The remaining two (`lin`, `quad-OD1`) report
`atoms9 = 66057`, and `§5` itself observes that `EᵀJE = (Σ E_j)²` is a
bijection of `Σ E_j` — so those two are literally the same colouring as each
other. **Eleven rows, two distinct objects.** `§5`'s "That is not eleven
coincidences" is right for the wrong reason: it is not eleven *anythings*, and
the table's visual weight (eleven rows of identical twenty-digit strings)
overstates the evidence by a factor of five and a half.

---

## MODERATE 1 — G5's "THE SAME BILINEAR TREATMENT THE EVEN CHANNEL GOT" IS NOT THE SAME TREATMENT, AND THE UNIT DOES NOT APPLY ITS OWN DEFLATION TO IT.

**Where.** Receipt G5 gate text; result `§8` ("each wide chart's direction set
was given the same bilinear treatment").

**Defect.** The v7 object is `Σ_R P(R) E_j(R) E_k(R*)`: a second moment of
integer **counts**, under the **order-dual reflection**, against the
**pushforward of the uniform permutation measure**. The v10 object is
`Σ_rows (1/|rows|) 1[d ∈ row] 1[d' ∈ row]`: a co-occurrence of **0/1
indicators**, with **no reflection at all**, against a **uniform measure on
shadow rows**. Three of the four ingredients differ, and the missing one is
the reflection — the entire subject of `§25.4` and of the unit's own `§4`.
This is precisely the operationalization-fidelity failure the unit invokes
G3-a to guard against on the v7 side.

It also means the unit's sharpest deflation applies verbatim to its own
forward-pointing probe and is not applied: a co-occurrence matrix of
indicators is a second-moment matrix, so its positive semidefiniteness is the
same tautology, and "59 anisotropic, 0 identity-proportional" is the same
non-result. `§4` deflates paper 30 for exactly this and `§8` builds a hint on
it.

---

## MODERATE 2 — THE NARROW CONTROL IS A COUNT, NOT A CONTROL; MEASURED, IT FIRES F1 ON THE v10 SIDE.

**Where.** Receipt G5 (`CGn = chart_grams(Cn, wide=3)`, reported only as
"narrow control 42 charts"); result `§8`, which does not mention it at all.

**Defect.** The receipt builds the narrow control, computes its chart Grams,
and then reports only `len(CGn)`. No anisotropy, no stabiliser, no
identity-proportionality is measured on it — so it controls nothing. Measured:

* **4 of 42 narrow charts have a direction Gram equal to `(1/4)·I`** — F1's
  literal condition, *a multiple of the identity*, firing on the v10 side;
* **38 of 42 carry the maximal stabiliser** (order 6, all of `S_3`), 34 of
  them the maximally symmetric `(1/4)I + (1/4)J`;
* only 4 charts have a non-maximal stabiliser.

Had the control been read, `§8` could not have been written as it is: on the
comparator blueprint the direction Gram is *more* isotropic than v7's channel
Gram, sometimes exactly `λI`.

---

## MODERATE 3 — F3 IS SILENTLY DROPPED.

**Where.** Pin F3; result `§11` residue 2 (which defers F4 explicitly and does
not mention F3); receipt (no gate).

**Defect.** The pin pre-registers four falsifiers under a "NO NULL OUTCOME"
header. F1 and F2 are adjudicated; F4 is explicitly deferred to D72, which is
proper. **F3 — "the even/odd algebraic split of `§3` does not survive
transfer: the anticommutator of the generated line's own transports is not
symmetric, or is not rank-2. Then `§3.2`'s table is a coincidence of two
imported representations and should be struck" — is never named, never tested
and never deferred.** G5 is the transfer arm and it forms a co-occurrence
matrix over chart directions, not an anticommutator of the generated line's
transports; it is not an F3 test under any reading. A first-class
pre-registered falsifier must be decided or explicitly and visibly deferred.

---

## MODERATE 4 — `789150` IS NOT "IN p4's OWN UNITS", AND IT TRAVELS UNQUALIFIED INTO THE VERDICT AND THE LOG.

**Where.** `§6` item 2 ("In p4's own units the deficit is `6 × 131526 − 6 =
789150`"); receipt G4-c; `[VERDICT]`; LOG #488. `§11` residue 7 concedes the
row is `[STATED]`.

**Defect.** v6 p4's `missing_components = 8193` is a component count on a
**2-dimensional screen** (a symmetric 2-tensor has 3 components per screen
atom against a scalar's 1) at that paper's own grid resolution. D73's `6` is
`dim Sym²(R³)` on an index of **three named 5-element record types**, and
`131526` is a count of record classes. The index has no dimension in the
geometric sense, the atoms are not screen atoms, and the two numbers are not
commensurable — `6 × 131526 − 6` is arithmetic on D73's record count under
p4's *counting rule*, which is not the same thing as "p4's units". `§11`
residue 7 says the row was not verified against p4's code (which is absent
from the tree); the qualification does not travel with the number into `§6`,
the `[VERDICT]` line, or LOG #488, where `deficit 789150` reads as a
recomputed answer to a committed no-go.

---

## MODERATE 5 — G1-e's NON-VACUITY CONTROL IS MIS-TARGETED, AND THE CORRECTLY TARGETED ONE WAS IN THE LIFTED NAMESPACE, UNRUN.

**Where.** Receipt G1-e ("`known` … is strictly worse, so the identity is not
vacuous", `299.7×`); result `§1` G1-e row and `§11` residue 5.

**Defect.** The identity under test is about the **even** coordinate:
`TV_9(full) = TV_9(even_abs) = TV_9(agg_l2)`. The offered non-vacuity control
is `known`, which ablates **both** the even and the odd data — so it shows the
gate resolves *the pair of channels jointly*, not the even channel. p30's own
`colors_for_mode` carries two further committed modes, `even_only` and
`odd_abs`, which are exactly the single-channel ablations; the receipt lifts
`colors_for_mode` and runs six of its eight modes, skipping precisely those
two. Paper 30 prints both rows (`:2745-2746`).

**Recomputation.** I ran all eight in the lifted namespace:

```
known      atoms9 63745   TV9 = 0.00502233763971961731060572   (299.7x)
full       atoms9 128678  TV9 = 0.0000167603622405300634803560
even_abs   atoms9 66060   TV9 = 0.0000167603622405300634803560
even_only  atoms9 65769   TV9 = 0.00106776883593603131359312
odd_abs    atoms9 65998   TV9 = 0.000721544094503000053957540  (43.1x)   <- even channel ablated
agg_l1     atoms9 66039   TV9 = 0.0000465237596142739437320780
agg_l2     atoms9 66057   TV9 = 0.0000167603622405300634803560
agg_linf   atoms9 66036   TV9 = 0.0000377194687086066037755929
```

`odd_abs` is the control the gate wanted: removing the even coordinate
entirely costs `43.1×`. **The gate's resolution on the even axis is therefore
demonstrably nonzero at the level of "present or absent", and demonstrably
zero at every level finer than the trace.** That is a sharper and more honest
statement than `299.7×` supports, it costs two extra mode runs (~11 s in a
457 s receipt), and it belongs in G1-e.

---

## MINOR 1 — G4-a's "RANK CENSUS" IS DEFINITIONAL AND ITS PREDICATE CANNOT FAIL.

`LOCAL_RANK` is populated by `LOCAL_RANK[0] += 1` or `LOCAL_RANK[1] += 1`
according to whether the even 3-vector is zero; no rank is computed. The gate
predicate `max(LOCAL_RANK) <= 1` maxes over the **keys**, which the code only
ever sets to 0 or 1 — it is true by construction and is exactly the hoisting
defect G6-a names. The mathematical content ("`vvᵀ` has rank ≤ 1") is true of
every outer product and therefore of every second-moment matrix ever written
down; presenting it in `§6` item 3 as a third independent failure mode ("**at
a level p4 never needed**") gives a triviality the weight of a finding. The
only measured number in the gate is `3862`, the count of records with
`E(R) = 0`.

## MINOR 2 — NO PYTHON VERSION GUARD, AND THE SHEBANG POINTS AT THE INTERPRETER THAT CRASHES.

`§11` residue 6 correctly records that the committed v7 campaign needs
`>= 3.10` and that this environment's `python3` is 3.8. The receipt's own
shebang is `#!/usr/bin/env python3` and there is no `sys.version_info`
assertion anywhere in its 1445 lines. A reader following the shebang gets an
`AttributeError` from inside a lifted third-party namespace with no
diagnostic. One line (`assert sys.version_info >= (3, 10), ...`) at the top of
the receipt turns a confusing crash into an instruction, and belongs there
rather than only in the note.

## MINOR 3 — THE EXIT CODE CARRIES NO INFORMATION ABOUT NON-ANCHOR FAILURES.

`sys.exit(0)` is unconditional at `:1445`; `ANCHOR_FAIL` gates the only
`sys.exit(1)`, at `:392`. This is house-consistent ("substantive negatives
exit 0"), but it means "29 PASS / 0 FAIL, **exit 0**" states one fact twice
and zero facts about G2–G6. If the exit code is not a summary of `FAIL`, the
note should stop quoting it as though it were.

## MINOR 4 — THE DOCSTRING OVERCLAIMS THE FLOAT LABELLING.

The header says "every such number is labelled `[float port]` in its gate
detail". It is not: the anisotropy ratios, the traceless Frobenius share, the
condition number, the discriminant, the `Cov` anisotropy and the whole `N`
window table are `dfl(...)` renderings printed without the tag. They are exact
decimal truncations of exact Fractions, so nothing is wrong with the numbers —
only with the claim about the labelling.

## MINOR 5 — "CIRCULANT" IS ORDERING-DEPENDENT; THE STABILISER IS THE INVARIANT.

`chart_grams` sorts the direction set (`dirs = sorted(set(dirs))`) and `§8`
then reports "every one of them is a `4×4` circulant". Circulancy is a
property of an ordering, and the gate text elsewhere correctly says the
direction ordering "is arbitrary — which is G4-b's point, transferred". The
invariant statement is the stabiliser order (and, better, the isomorphism type
`D_4`); the circulant framing should be marked as holding in the canonical
sorted order.

---

## Checked and CLEAN

* **`G^even` and every committed number.** My own Gram loop (independent of
  `matrix_entries`) reproduces all six independent entries as exact rationals;
  all seven principal minors match paper 30 `:2991-2997` string-for-string
  under p30's own `fmt_dec_frac(v, 20)`; the three odd reflected diagonal
  entries match `:3003-3005`.
* **The eigenstructure.** Characteristic polynomial coefficients are exactly
  the committed minors (`c2 = Σ 1×1`, `c1 = Σ 2×2`, `c0 = 3×3`); discriminant
  `1.847847e10 > 0` exactly; eigenvalues cross-checked independently with
  `numpy.linalg.eigvalsh` at `108.04492811555816 / 45.92263411658028 /
  20.83231100419313`, matching the receipt's certified brackets to every digit
  printed; condition number `5.1864`. G2-d's claim that the eigenproblem is a
  rearrangement of numbers paper 30 already printed is exactly right.
* **The reflection-parity theorem (`§4`, licensed claim 2).** `E_j(R*) =
  E_j(R)` and `O_j(R*) = −O_j(R)`: `0` and `0` violations in `394578` tests in
  my instrument; `dual_key(left, 5) == right` for all three pairs; reflected
  even `==` unreflected even as an exact Fraction identity. **The deflation is
  correct and is the strongest thing in the unit.** It is if anything
  *understated*: Osterwalder–Schrader reflection positivity also requires a
  half-space support restriction on the test functions, and p30's Gram has
  none at all — so `§25.4` is not a weakened reflection-positivity statement,
  it is a differently-shaped one. The note's care in saying it "claims nothing
  about whether paper 30 believed otherwise" is correct and should stay; p30's
  own framing ("the finite reflection-positive meaning of the complex idea")
  is what the deflation bites, and it bites fairly.
* **The `N = 5` mechanism.** Support disjointness confirmed (`0 of 63` records
  carry two channels), and I confirmed the stronger fact behind it: at `N = 5`
  every record has exactly one `flags5` entry, of value 1.
* **`μ = (63/10, 21/5, 21/5)`, variances `58.9797 / 22.7352 / 18.1149`, `Cov`
  off-diagonals all negative, `Cov` anisotropy `0.4455`, raw class-uniform
  reweighting `0.2814`** — all reproduce; G2-f and G2-g are real controls and
  they do what they say.
* **`S_3` stabiliser order 1**, and the honesty of reporting the channel-2/3
  mean coincidence against the unit's own interest.
* **The Prop 10.6 handling (`§7`, G4-d).** The distinction is drawn correctly
  and defensively, the "must never be cited as one" warning is the right
  instrument, and no numerical relation is smuggled. The claim is properly
  graded `[STATED, not computed]`. This section is a model and I have no
  objection to any part of it.
* **"The corpus printed the minors and never printed the matrix."** True: I
  grepped the whole tree for the six rational entries and for the decimal
  renderings; they occur nowhere outside D73's own files.
* **`§9`'s "not licensed, and explicitly disclaimed" paragraph** — no metric
  claim, no gravity claim, no continuum claim, no Prop-10.6 evasion. Nothing
  is smuggled past it anywhere in the note.
* **Fixture-boundedness of the *wording*** — every licensed claim carries a
  window or a `[SAMPLED]` tag. The failure is not in the tags; it is in which
  fixture was chosen (BLOCKER).
* **G6-a, G6-b, G6-c** all do what they claim within their stated scope, and
  G6-a's naming of its own hoisting defect is exemplary practice — which is
  why MINOR 1 (a predicate defeated by exactly that defect) is worth naming.
* **`§11` residues 1, 3, 5, 6 and 7** are honest and correctly graded,
  including residue 5's warning that "the even channel does not matter" is a
  misreading — a warning this review's MODERATE 5 confirms quantitatively at
  `43.1×`.

---

# DELTA — adjudication and repairs (campaign side, 2026-07-27)

All findings applied; receipt rerun 38 PASS / 0 FAIL (524 s,
python3.13 with version guard), every referee number reproduced with
zero contradictions.  BLOCKER: the unit is REFIXTURED — the receipt
now text-slices paper 30's §26.2 frontier table and gates that its
old anchor IS the paper's falsified rank-11 target (TV string
character-identical); the four TV9 = 0 frontier triples reproduced
to the unit and as exact Fractions; §27's selected triple scores 0
in all three modes.  **THE G2 SURVIVOR GATED ON THE RIGHT FIXTURE:
the selected triple's even Gram is anisotropic (0.5114, three
nonzero off-diagonals as exact rationals, S_3 stabiliser ORDER 1) —
the genuine rank-2 candidate.**  MAJOR 1: the transfer hint
WITHDRAWN and its inversion gated (59 charts = TWO matrices;
degenerate spectra certified by exact eigenvectors; every
DOUBLE-RING 100% stabiliser-8; the narrow control fires F1 on the
v10 side with 4 charts exactly (1/4)I) — successor guidance graded
[MY READING]: the tensor stage needs stabiliser-1 direction
geometry, which sprinklings and defected crystals have and
hand-built crystals lack.  MAJOR 4: [THEOREM] removed with a
counterexample from the committed table; the true mechanism (the
h-weight identity) gated at 18 candidates / 0 mismatches.  The
sensitivity result retargeted and gated: ablating the EVEN channel
costs 43.1x (odd_abs) — the gates resolve the even channel's
presence and nothing finer than the trace (eleven rows = TWO
colourings, computed).  All MODERATEs/MINORs applied.  TERMINAL for
round 1.
