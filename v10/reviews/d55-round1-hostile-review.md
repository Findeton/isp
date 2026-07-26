# D55 — ROUND 1 INDEPENDENT HOSTILE REVIEW

**Frozen:** 2026-07-26.
**Unit under review:** D55 "the dimension meter" — `note-d55-dimension-meter-pin.md`,
`code/d55_shatter5_exact.py` + `data/d55_shatter5_exact.out`,
`code/d55b_sphere_calibration_exact.py` + `data/d55b_sphere_calibration_exact.out`,
`note-d55-dimension-meter-result.md`, LOG #430 / #431.
**Reviewer:** independent Opus 5 worker, no prior context, recompute-not-trust.
Every number below was produced by code I wrote for this review, run against the
committed layers from the repo root; scratch under `/tmp/d55rev/`. The only thing
I imported from the corpus is the transport layer itself (`d42b1`) — the poset
closure, heights, SKY-B, shattering, the builder schedule, the chain-cover
computation, the sphere certificates and both Radon dependences are all mine.

**VERDICT: REVISE. 1 BLOCKER / 2 MAJOR / 8 MINOR / 3 NIT.**

The construction survives everything. The 84-event record is real, and it is
real at *full width*: I re-derived the builder from the pin and replayed it
against `candidates_for` with **all 42 actors at every one of the 84 steps**
(375 s of menus 1,847–3,565 events wide) and got back the identical record, so
the tractability instrument did not touch the object. My own closure, my own
SKY-B, my own shatter search: 32 distinct traces, all 32 subsets, a shattered
5-set, at depths 5, 6 and 7 and nowhere else in 1..17. The realized family's
exact minimum chain cover is 10 — Dilworth-tight. A2's 48 cap certificates and
both Radon dependences recompute exactly, and the Radon inequality chain as
written is correct including its strictness. The BLOCKER is, as in D54, a
sentence rather than a computation: **"caps on S² never shatter 5, so this sky
exceeds the sphere / the meter reads beyond 3+1" needs the arrow "a discrete 3+1
sky is a cap system on S²" — the exact arrow `d47a` demoted one rung down and
that D54 round 1 forced K7 to stipulate.** D55 uses it unstipulated, one rung
up, with no control.

---

## BLOCKER 1 — "the admissibility layer does not select 3+1" rests on the arrow the corpus retired 24 hours earlier

**Where.** Result note title and §1 boxed claim ("Caps on S² shatter 4 and never
5, **so this sky exceeds the sphere**"), §2 ("the m = 5 record's sky fits S³ and
provably not S² — **beyond 3+1**"), gate **G6**'s label ("so this sky is not
realizable by caps on S^2. **THE METER READS BEYOND 3+1**: the admissibility
layer does not select the sphere"), the `d55` VERDICT block, pin §4, and LOG
#431 ("caps on S^2 stop at 4, so this sky exceeds the sphere — THE
ADMISSIBILITY LAYER DOES NOT SELECT 3+1").

**What is proven and what is assumed.** The chain is

1. the layer admits a record whose SKY-B sky shatters a 5-set — **theorem, and I
   verified it independently** (see CLEAN B/D);
2. caps on S² shatter at most 4 — **theorem, Radon, and I re-certified it three
   ways** (see CLEAN F);
3. therefore this sky is not cap-realizable on S² — **valid**;
4. *therefore this sky is not a 3+1 sky / the layer does not select 3+1* —
   **this step needs "every discrete 3+1 sky is a cap system on the celestial
   S²", which is nowhere established and whose one-rung-down analogue is
   FALSE.**

`d47a` itself demoted the analogue ("a discrete sky of real Minkowski is
therefore NOT generally an arc system"); D54 round 1 recounted it at 218 of 397
decided genuine 2+1 SKY-B skies; and the D54 delta rewrote K7 to read
"'not a 2+1 celestial sky' holds **ONLY under the strict stipulation** that a
2+1 sky means an arc system … The sound discrete separation is EMPIRICAL"
(committed, `d54b` line K7). D55 restates the same inference one dimension up
with none of that apparatus: no stipulation, no demotion carried, no control.

**My recomputation of the analogue** (`/tmp/d55rev/mink3.py`; exact integer
`M^{2+1}` records, exact squared-interval causal order, my own heights and
SKY-B at every depth, arc-realizability decided by **brute force over all
cyclic orders** — so each NOT-ARC is a certificate, not a search failure):

```
   N=80   skies=27  ARC=25  NOT-ARC=2
   N=100  skies=67  ARC=65  NOT-ARC=2
   N=120  skies=128 ARC=124 NOT-ARC=4
   N=140  skies=215 ARC=205 NOT-ARC=10
   N=160  skies=317 ARC=306 NOT-ARC=11
   N=200  skies=453 ARC=436 NOT-ARC=17
   TOTAL  genuine M^{2+1} SKY-B skies (4..8 directions): 453
          arc-realizable 436   NOT arc-realizable 17  (3.8%)
```

Seventeen exact counterexamples of my own to "a discrete `d`-dimensional sky is
the continuum trace system of dimension `d`". The premise D55 needs at 3+1 is
the same statement, and nothing in the corpus supports it.

**And the empirical rescue that saved D54 is not currently available here.** D54
was re-founded on a 1,925-pair zero-shattering control over genuine `M^{2+1}`
records. I ran the 3+1 analogue (`/tmp/d55rev/mink4.py`, `/tmp/d55rev/diamond.py`;
exact integer `M^{3+1}` records, lattice boxes and causal diamonds, SKY-B at
every depth):

```
  lattice boxes (8 records): 361 SKY-B skies with >= 4 directions,
        SC-capable(>=16 traces, empty) = 9,  shatter-4 = 0,  shatter-5 = 0
  causal diamonds (3 records): 990 SKY-B skies with 5..14 directions,
        SC5-capable (>= 5 dirs, >= 32 distinct traces, empty present) = 33,
        SHATTER-5 = 0,  non-cap-by-trace-count = 0
  max distinct traces seen at |dirs| = 5 : 14   (shatter-5 needs 32)
```

Zero shatterings — but only **33 capable skies**, versus D54's 1,925, and at
`|dirs| = 5` the richest sky I could sample carried 14 traces where 32 are
needed, i.e. most of the sample is structurally incapable (D53's tautology
trap). So the honest position after this round is: the separation D55 asserts as
a theorem is not a theorem, and its empirical substitute is presently too thin
to carry it either.

**What survives, and the repair.** Everything mathematical: *the transport
layer's shatter capacity is not capped at 4*; *the m = 5 sky is not
cap-realizable on S²*; *B₅ is cap-realizable on S³*; *the ladder measures
capacity, priced at C(k,⌊k/2⌋) actors*. The sentence that must change is the
dimensional one. Either it retreats to the model-relative form — "not a cap
system on the celestial sphere, i.e. beyond 3+1 **under the stipulation that a
3+1 sky means a cap system on S²**, a stipulation `d47a` showed fails for
discrete records one rung down" — or it must be re-founded empirically on a 3+1
control large enough to have SC5-capable skies in quantity. Until one of those
lands, "the admissibility layer does not select 3+1" is not a licensed reading
of this record; "the admissibility layer does not cap the shatter ladder at the
sphere's rung" is.

---

## MAJOR 1 — the restricted-menu instrument is sound, but for a reason the unit states backwards, and the equivalence it gates is membership-only

**Where.** Pin §2 ("This cannot change membership — `admissible(acts, e)` reads
only `(acts, e)`, no actor list"); `d55` docstring (same); gate **G2**'s label
("the initiator-restricted menu is **EXACTLY** the full menu filtered to those
initiators — admissible(acts, e) reads no actor list, and this gates it");
result note §1 ("the soundness claim held for `admissible()`, not for
enumeration"); LOG #430 and #431 (same diagnosis).

**The defect.** `admissible` takes `actors` as its third positional argument and
uses it. Its delivery branch is literally

```python
if kind == 'd':
    s, r, v = e[1], e[2], e[3]
    if r == s or r not in actors: return False, None      # <-- reads actors
    sv = own_view(acts, s)
    opts = deliver_options_in_view(sv, s, actors)          # <-- reads actors
    if (r, v) not in opts: return False, None
    return True, F(1, 4) / len(opts)                       # <-- weight reads actors
```

so the receiver-membership refusal that the unit found in run 1 lives *inside
`admissible`*, not only in `candidates_for`'s enumeration. My exhibit — same
`acts`, same `e`, three actor lists:

```
e = ('d','X','D0', v1)   at the D55 prefix H[:2]
   admissible(H[:2], e, ('X',))        -> (False, None)
   admissible(H[:2], e, ('X','D0'))    -> (True, Fraction(1,8))
   admissible(H[:2], e, ALL 42 actors) -> (True, Fraction(1,328))
```

Both the pin's stated reason and the note's post-repair diagnosis are therefore
false as written, and the second is the one a future reader would reuse.

**The correct theorem** (which I state, prove from the layer, and sweep). For
any prefix `H` and any actor set `A ⊆ Ω`:

> events(`candidates_for(H, A)`) = { `e` ∈ events(`candidates_for(H, Ω)`) :
> `e[1] ∈ A` and (`e[0] ≠ 'd'` or `e[2] ∈ A`) }.

*Enumeration:* `'p'` ranges over `bases` (from the full `View` — actors-free),
`'r'` over `live_by_base` (actors-free), `'m'` over `full.holdings(a)`
(actors-free), `'d'` over receivers drawn from `actors`, `'n'` unconditionally.
*Admission:* the `'p'`, `'r'`, `'m'` membership tests never touch `actors` (in
`'m'`, `actors` reaches only the denominator `D`, and only via
`admissible_arb_ckeys`, which calls `admissible` on `'r'` events — an
actors-free branch); `'n'` always admits; `'d'` requires `r ∈ A` **and**
`v ∈ holdings(s)`, and once `r ∈ A` is imposed by the filter the residual test
is actors-free. ∎

**But the weights are not preserved**, and "EXACTLY the full menu filtered" is
false at the level of the `(e, q)` pairs the menu actually consists of:
`q('d') = ¼ / ((|A|−1)·|holdings(s)|)` and `q('n')` depends on
`has_d = (|A| ≥ 2)`. Observed at every sampled step:

```
 step  event                        |full| |restr| membership-eq  weight-eq
   2   ('d','X','D0',v1)             1889     9      True          False   (3/9 differ)
   3   ('d','X','D1',v1)             1930     9      True          False
  10   ('n','D0')                    2094     3      True          False   q: 1/2 vs 3/4
  20   ('p','D3',v1,0)               2091     3      True          False
  40   ('d','C7','A2',v1)            2540    10      True          False
  60   ('d','D0','C16',v1)           2991     8      True          False
  75   ('d','D4','C22',v1)           3360     8      True          False
  83   ('d','C25','A9',v1)  (LAST)   3565    10      True          False   (4/10 differ)
      example: ('d','D0','C16',v1)  full q = 1/328   restricted q = 1/8
```

and swept exhaustively over a family the D55 record never reaches
(`/tmp/d55rev/eqsweep.py`, the complete 3-actor history tree to depth 4, all 7
non-empty actor subsets at every prefix):

```
  prefixes = 50,617    comparisons = 354,319
  MEMBERSHIP MISMATCHES = 0            (the theorem above, corroborated)
  weight mismatches: 'n' 151,851 , 'd' 331,446
```

**Damage: bounded, and I bounded it by rebuilding.** The builder discards `q`,
no gate reads `q`, and the full-menu replay returns the identical record (CLEAN
B). So the m = 5 record is safe. What is not safe is the sentence: the unit's
own headline is that *selection lives in the MEASURE*, and the instrument being
carried toward the measure is precisely the one whose weights the restriction
changes by a factor of 41. G2's label must say "membership-equal, weights NOT
preserved — the builder reads no weight", and the reason must name the `'d'`
branch of `admissible`.

---

## MAJOR 2 — the "meter" is not a property of a record: the same record reads 0, 3, 4 and 5

**Where.** Pin §1: "the maximum k the transport layer can shatter is the
framework's **dimension signature**", with the ladder table
(`max shatter | compatible with | actor cost`) and no column for the sky
definition or the depth; `d55b`'s verdict ("max-shatter 4 = sphere-compatible,
max-shatter 5 = S^3"); result note §2 ("the meter's scale is concrete").

**The defect.** Max-shatter is a function of *(record, base event, sky kind,
depth)*, and on this very record it takes almost every value in range. My
complete table (`/tmp/d55rev`, my own SKY-B, my own shatter search, all 17
depths the record actually has — the receipt stops at 9, see MINOR 2):

```
   d  |dirs| traces  max-shatter        d  |dirs| traces  max-shatter
   1     1      1        0              10    8     23        4
   2     2      4        2              11    9     17        3
   3     3      8        3              12    9     17        3
   4     4     16        4              13    6     10        2
   5     5     32        5              14    6      9        2
   6     5     32        5              15    2      3        1
   7     5     32        5              16    2      3        1
   8     6     29        4              17    2      3        1
   9     7     26        4
```

and, on the *same* record under the corpus's other two committed sky
definitions:

```
   SKY-A at E: |dirs| = 1, traces = 1, empty absent, max-shatter = 0
   SKY-C at E: |dirs| = 1, traces = 1, empty absent, max-shatter = 0
```

So the "dimension signature" of one object is 0 under SKY-A/SKY-C, 3 at
SKY-B(3), 4 at SKY-B(4), 5 at SKY-B(5..7) and back to 2 at SKY-B(14). Read as
a *capacity* — a supremum over readings, which is what A1 actually establishes —
the claim is fine and I do not dispute it. Read as a *signature*, i.e. a number
a record has, it is not well defined, and what it tracks is the number of
directions and traces the reading exposes: exactly D54 round 1's correction
("width prices SKY SIZE, not dimension") reappearing. The unit's own §3 says
"reading-relative to SKY-B" — that scope line must reach the pin's meter table
and the "signature" sentence, which are where the meter is defined.

Second, smaller, edge of the same defect: the table's "**compatible with**"
column is only valid in the unit's own special case — a sky with exactly `k`
directions whose family is all of `2^[k]`. In general max-shatter `k` gives a
*lower bound* on sphere rank; a sky with 9 directions and max-shatter 3 is not
thereby "compatible with the circle". The word is doing quiet work.

---

## MINOR 1 — at m = 5 the tractability instrument is not gated at all: the sample is computed and discarded

`build(5, sample_steps=(3,))` fills `b5.eq_samples`, and **`b5.eq_samples` is
never read** (`grep` confirms: written at line 133, read only for `b4` at lines
256–261). G2 is explicitly `[ANCHOR]` — it gates three m = 4 steps (labels
`X delivers v1 to D0`, `D0 pads`, `mint C1 <- D2`, i.e. steps 3/9/20 of 44) and
nothing at m = 5. The one m = 5 sample costs a full 42-actor menu call and is
thrown away. This is D54 MINOR 4's dead-variable class landing on the unit's own
headline build. Damage nil: I discharged the obligation at eight m = 5 steps
including the final courier send, and by the 354,319-comparison sweep and the
proof in MAJOR 1.

## MINOR 2 — the per-depth table is silently capped at d = 9 while the record runs to d = 17

`for dd in range(1, 10)` — against the pin's own "no silent caps; depths
printed" and against D54 K11's lesson (which the receipt cites by name). The
record has 82 events above `E` and depths up to **17**. G8's label says the
shattering depths are "enumerated, not sampled"; at the committed range that is
not established. I completed it (table in MAJOR 2): no 5-set shatters at
d = 8..17, so the reported `[5, 6, 7]` is correct and complete. Damage nil,
claim not established by the receipt.

## MINOR 3 — the anchor gate never looks at D54; "same trace family" is carried by an outside fact

Pin §2 promises the m = 4 anchor reproduce "the same trace family as D54's".
G1 checks `need4 <= have4` (all 16 subsets) and `shattered_set(...) is not None`
— it never reads D54's record, so what is gated is *completeness of B₄*, not
*equality with D54's family*. The equality does follow, but only because both
families are the **full** power set (D54's K7: 16/16), i.e. from D54's receipt,
not from this one. Two consequences worth writing down: (i) the anchor could not
distinguish "reproduces D54" from "reproduces any complete B₄ family"; (ii) the
identification of trace elements with the direction actors is enforced at m = 4
only by the absence of a `KeyError` in `family_of`'s `name[i]` lookup — there is
no m = 4 analogue of G4's `sorted(dirs5) == didx5`. I checked both by hand: my
m = 4 rebuild has `dirs == the four direction events` at depth 5, 16/16 subsets,
unique shattered 4-set, min chain cover 6. The record genuinely differs from
D54's (22 actors / 44 events / 6 accumulators versus 20 / 42 / 4+2 late
deliveries) and the difference is immaterial exactly because both families are
complete — which is the sentence the note should carry.

## MINOR 4 — A2a and A2c carry no record-specific information

A2a exhibits 16 caps on a tetrahedron; A2c exhibits 32 caps on a 4-simplex.
Both are instances of one textbook fact — halfspaces in `R^d` shatter `d+1`
points — so **every** sky with at most 4 directions is cap-realizable on S² and
every sky with at most 5 is cap-realizable on S³, whatever its family. "D54's
record upgrades from 'not an arc system' to **sphere-compatible**" (note §2, LOG
#431) is therefore automatic for any 4-direction sky and says nothing about D54's
record. The informative half of A2 is A2b, the negative. (I verified all 48
certificates myself, CLEAN F; the point is what they license, not whether they
hold.)

## MINOR 5 — theorem-pass / implication audit: 7 of the 16 gates carry independent falsifiable content

Per LOG #403 MA-2 and D49 M1:

* **G5 ⊂ G6.** `need5 <= have5` (all 32 subsets, G6) *implies* `len(r5) >= 32`
  and `frozenset() in r5` (G5). G5 cannot fail while G6 passes.
* **G7 is mostly implied.** `tight = mid5 <= have5 and have5 >= need5` is
  implied by G6; and given `nested` plus G6, `contributing >= 10` is *forced* by
  the Dilworth gate itself (a 10-element antichain cannot be covered by fewer
  than 10 chains) — so it is a theorem-pass of the very theorem being "checked
  for consistency". Only `nested` is independently falsifiable. (Both are true:
  I recomputed the exact minimum chain cover of the realized family via
  |F| − maximum matching = **32 − 22 = 10**.)
* **G8 ⊂ G6.** `DEP5 in sh_ds` re-runs the identical computation G6 already
  passed; `len(sh_ds) >= 1` follows.
* **G4's `inc5` ⊂ the SKY-B definition.** Directions are selected by equal
  height and `x < y ⇒ h[x] < h[y]`. D54 round 1 flagged exactly this in K4 and
  the D54 delta labelled it; D55 reintroduces it unlabelled. (Real content in
  G4: `len(dirs5) == 5` and `sorted(dirs5) == didx5`.)
* **G0** is a smoke test (`callable(...)`).
* **A2b cannot fail** for any five points in `R³`: the 4×5 homogeneous system
  always has a nonzero kernel, and `Σλ = 0` with `λ ≠ 0` forces both sign
  classes non-empty. It is honestly labelled `[THEOREM, certificated]`, so this
  is bookkeeping, not misdescription. **A2a-0/A2c-0** are typo checks on
  hand-written unit vectors.

Independently falsifiable: **G1, G2, G3, G6, G7-`nested`, A2a, A2c** — 7 of 16.
G2's failure in run 1 is the unit's own evidence that the set is non-empty, and
that failure is honestly recorded.

## MINOR 6 — "selection, if anywhere, lives in the MEASURE" is not an exhaustive dichotomy

Note §1 and LOG #431 state it flatly (§4's stronger "the only remaining
candidate inside the corpus" is at least labelled `[MY READING]`). At least four
non-measure candidates are live, three of them inside this very unit:

* **the reading.** SKY-A and SKY-C give max-shatter 0 on this record (MAJOR 2),
  and D53 established they can *never* shatter. If dimension is read off a sky,
  a selection principle could live in the sky definition — which is a choice the
  corpus has already had to make twice.
* **price, not prohibition.** The unit's own ladder prices shatter-k at
  `C(k,⌊k/2⌋)` contributing actors (3 / 6 / 10 / 20 / 252 …) and the builder
  spends 42 actors for m = 5 against 22 for m = 4. A cost that grows
  superexponentially is a selection-shaped structure *inside the admissibility
  layer*, and "does not select" reads it as "does not forbid". The unit should
  say which it means; on the evidence the layer is not indifferent, it is
  merely permissive.
* **actor-count physicality (D48)** and **typicality by counting**, which do not
  require a completed measure to be posable (a ratio of admissible histories is
  not a normalized weight).

## MINOR 7 — the pin sends the general Radon argument to the note; the note does not carry it

Pin §3 A2b: "the general argument is dimension counting and **goes in the
note**." The note's §2 has a one-clause version ("the Radon argument closes it,
and five points in R³ always carry a dependence"); the actual inequality chain
survives only inside the receipt's gate label. That chain is **correct** — I
checked it symbol by symbol: with `Pos = {i : λᵢ > 0}`, `c = Σ_pos λᵢ =
Σ_neg |λⱼ| > 0`, a cap `{x : u·x ≥ t}` cutting off exactly `Pos` gives
`t·c ≤ Σ_pos λᵢ(u·pᵢ) = Σ_neg |λⱼ|(u·pⱼ) < t·c`; the first `≤` uses `u·pᵢ ≥ t`
on `Pos`, the strict `<` uses `u·pⱼ < t` on `Neg` and needs `Neg ≠ ∅`, which the
`split` gate supplies and which `Σλ = 0`, `λ ≠ 0` forces anyway. Numerically on
config 1: `c = 132/49` on both sides. The defect is placement, not content.

## MINOR 8 — the pinned schedule and the built schedule differ

Pin §2: "Schedule **exactly as D54 §8 A2**: clean first receipts, then mints,
then one courier send per step in chain order." `courier_step` interleaves:
mint `C_i ← D_j` immediately followed by `A ← C_i`, per step. The record is
unaffected (each courier is fresh at its mint, so its wire carries exactly one
direction either way — I verified the resulting per-wire trace families are
nested and the family is complete), but a pinned schedule was silently
substituted.

## NIT 1 — G9 counts a gate that never runs

`check() calls = 11` while 10 gates execute: the AST scan counts the
unexecuted `else:` branch of the m = 4 anchor. Also, both AST scans
(`G9`, `H1`) still lack the run-bound-name requirement that D54's delta added
after MINOR 7 — `_vac` tests only `isinstance(c.args[1], ast.Constant)`.

## NIT 2 — dead branch in the builder

`if len(ch2) == 1 and len(next(iter(ch2))) == 1: continue` never fires at
m ∈ {4, 5}: after removing `∅`, the B₄ and B₅ symmetric chain decompositions
contain no singleton-only chain (B₄'s two length-1 chains carry 2-element sets).
It matters only for m ≤ 3, which is never built.

## NIT 3 — `family_of` reads the depth off one direction

`DEPTH = hh[didx[0]] - hh[E_IDX]` takes the height of the lowest-indexed
direction event. The equal-height fact that makes this well defined is gated at
m = 5 (G4) and not at m = 4.

---

## Checked and CLEAN

Everything below is my own recomputation.

**A. Receipts rerun.** From the repo root: `python3 v10/code/d55_shatter5_exact.py`
→ **10 PASS / 0 FAIL**, `EXIT 0`, rc 0, 16.4 s; `python3
v10/code/d55b_sphere_calibration_exact.py` → **6 PASS / 0 FAIL**, `EXIT 0`,
rc 0. Both byte-identical to the committed `.out` files (`d55b` exactly;
`d55` modulo the wrapper's trailing `RC=0` line). No nondeterminism across runs.

**B. The record rebuilt at FULL WIDTH — the headline's strongest form.** I
re-derived `scd(m)` and the whole schedule from the pin (`/tmp/d55rev/build.py`,
sharing no line with `d55`) and ran it in two modes:

* `restricted` — 84 events, 42 actors, 15 s; identical to the committed record;
* `full` — **every menu call made with all 42 actors, at every one of the 84
  steps** (375 s; menus 1,847 to 3,565 events wide) — **the identical
  84-event record**, and every specification matched **exactly one** menu entry
  in full mode as well (`max hits = 1`), so the selection is forced, not
  tie-broken.

Same at m = 4: full-menu and restricted-menu builds agree event for event (44
events, 22 actors). **The initiator restriction did not change the record**, and
"every event menu-offered" holds against the unrestricted layer. Actor accounting
checks out: `1 + 5 + 10 + 26 = 42` named actors, **all 42 actually act**; event
census `d 67 / n 10 / p 6 / r 1 / m 0`; `10` chains and `26` couriers agree with
`Σ (|S₁|−1) + (len−1)` over the B₅ symmetric chain decomposition (4 + 4·3 + 5·2).

**C. The poset, independently.** I rebuilt the cover graph from my own
`regs_of`/`vname` reimplementation and computed reachability with my own DFS.
It equals the layer's `event_poset` on both records, and is irreflexive,
antisymmetric and transitive over all triples.

**D. The sky and the shattering, independently.** My own `heights`, my own
SKY-B, my own shatter search (nothing from `d47a`): at depth **6** the
directions are exactly the five `('p', Dᵢ, v1, 0)` events, all at height 7, all
strictly above `E` (height 1), pairwise incomparable; **32 distinct traces**;
**all 32 subsets realized**, none missing; the shattered 5-set is unique and is
`(D0,…,D4)`. The record shatters a 5-set at **d = 5, 6, 7** — three different
direction sets (`[6,10,14,17,19]`, `[11,15,18,20,21]`, `[22,23,25,27,29]`) —
and at no other depth in **1..17**. The receipt's `d = 1..9` rows reproduce
exactly (traces 1/4/8/16/32/32/32/29/26).

**E. Dilworth.** Per-initiator trace families are chains (zero crossings), and
so are the per-*wire* families under the alternative attribution; 32 contributing
initiators (bound 10); and the exact minimum chain cover of the realized family,
computed as `|F| − maximum matching` in the strict-comparability bipartite graph,
is **10** — the `C(5,2)` bound attained, Dilworth-tight, as claimed. (m = 4
anchor: 16 traces, min cover **6**, matching D54 round 1's recomputation.)

**F. A2 recomputed end to end.** All by my own `Fraction` dot products
(`/tmp/d55rev/a2check.py`):
* 16/16 caps on the tetrahedron, every certificate re-verified
  (`{i : u·pᵢ ≥ t} == S`); the tetrahedron is affinely independent;
* 32/32 caps on S³, every certificate re-verified; the five S³ points are
  affinely independent (my exact `det = 3`), which is precisely the condition
  the certificates need — and they *are* the proof of it, so there is no hidden
  general-position assumption;
* both Radon dependences re-derived by a different method (cofactor expansion of
  the 4×5 system, not the receipt's elimination): mine are
  `[46/49, 38/49, 48/49, −34/49, −2] = −2 ×` the receipt's, and
  `[−32/27, 0, 16/9, 16/9, −64/27] = −64/27 ×` the receipt's — the same
  dependences, same splits `{0,1,2}|{3,4}` and `{2,3}|{0,4}`;
* a **third** configuration of my own (stereographic images of
  `(0,0),(1,0),(0,1),(2,3),(−1,2)`): dependence exact, split `{1,4}|{0,2,3}`;
* constructive corroboration on all three: enumerating every cap trace over
  rational normals in `[−4,4]³` with all midpoint thresholds realizes
  **30/32, 28/32, 28/32** — and the missing sets are exactly the Radon-blocked
  complementary pairs (30 is the general-position maximum
  `2·Σ_{i≤3} C(4,i)`, so config 1 is optimal and still cannot shatter).

**G. The Radon argument as stated.** Correct, including the strictness and the
normalization — see MINOR 7 for the chain and the `c = 132/49` check. The
general claim ("any five points in `R³` carry a dependence, by dimension count")
is right, and both sign classes are automatically non-empty.

**H. Record fidelity.** `git log` order is clean: `242fff9` (LOG #430 + pin,
**two files, no code**) → `019aa89` (both receipts, both `.out`s, result note,
LOG #431), five minutes later. The pin genuinely preceded the code. Every number
in LOG #430/#431 matches actual output: 42 actors / 84 events / 10 chains / 26
couriers / 22 actors / 44 events / 16 subsets / 32 subsets / depths 5,6,7 /
Dilworth-tight at 10 / 10 PASS / 6 PASS / 16 and 32 certificates. The result
note's §4 is labelled `[MY READING]`, §3 holds the scope lines that matter
("ONE engineered record — no genericity claim"; "'Fits S³' is cap-realizability
of the shadow family, nothing stronger"), and the residues are honest (general-m
unrun and unclaimed; minimality open).

**I. The pre-registration.** Exemplary and not counted against the unit
anywhere: CONSTRUCTIBLE pinned before any code, with the consequence pre-stated
in *both* directions (a refusal declared "the more important result"), and with
the author's own corrected-prediction record cited against himself. The in-run
instrument repair is recorded in three places (note §1, LOG #431, an in-code
comment) — nothing was silently fixed. That its stated mechanism is wrong is
MAJOR 1; that it was disclosed at all is to the unit's credit.

---

## Final verdict

**REVISE.** The object is real and the arithmetic is clean. I rebuilt the
84-event record from the pin and replayed it against the committed layer with
all 42 actors at every step — same record, every event forced, every event
menu-offered — and then recomputed the poset, the heights, the sky, the traces
and the shattering with code that shares nothing with `d47a`: 32 traces, all 32
subsets, a shattered 5-set at three depths and nowhere else in 1..17, with the
realized family Dilworth-tight at exactly 10 chains. A2's 48 cap certificates,
both Radon dependences (re-derived by a different method, plus a third
configuration of mine) and the Radon inequality chain all hold. Headline claims
1 and 3 stand as verified.

Headline 2 does not, as stated. **"Caps on S² never shatter 5, so this sky
exceeds the sphere / the meter reads beyond 3+1" requires that a discrete 3+1
sky be a cap system on S² — the exact arrow `d47a` demoted and that D54's own
delta, one day earlier, forced K7 to state as a stipulation with the demotion
attached.** D55 re-uses it one rung up, bare. My 17 brute-forced non-arc
counterexamples among 453 genuine `M^{2+1}` skies say the premise class is
false; my 3+1 control (1,351 skies, 33 SC5-capable, zero shatterings) is clean
but far too thin to substitute for it, and at five directions the sampled skies
carry 14 traces where 32 are needed. So the dimensional sentence must either
retreat to its model-relative form or be re-founded on a real 3+1 control. What
survives untouched is the capacity statement, which is the interesting one:
**the admissibility layer does not cap the shatter ladder at the sphere's rung.**

Two further things must change. The restricted-menu instrument is sound — I
proved it from the layer and swept 354,319 comparisons with zero membership
mismatches — but *not for the reason given three times in the record*:
`admissible` does read the actor list, in the delivery branch, and the
equivalence is membership-only while the weights differ by up to a factor of 41.
For a unit whose closing move is "selection lives in the measure", that
correction is not cosmetic. And the meter must stop being described as a
signature: on this one record it reads 0 under SKY-A and SKY-C, 3 at SKY-B(3),
4 at SKY-B(4), 5 at SKY-B(5–7) and 2 at SKY-B(14). It is a capacity, taken as a
supremum over readings, and it prices sky size — D54 round 1's correction,
which has to reach the pin's table.

Nothing here needs new physics or a new construction: one withdrawal-and-restate,
one corrected soundness statement (proved in this review), one scope line moved
into the meter's definition, plus the eight minors. Nothing in this unit is
citable until those land and a delta records them.

---

# DELTA — repairs verified, 2026-07-26

Post-repair: `d55_shatter5_exact.py` **11 PASS / 0 FAIL** (G2b added),
`d55b` unchanged at 6 PASS, both exit 0.

**BLOCKER 1 REPAIRED.**  The headline is restated everywhere — receipt
G6, verdict block, result-note title and §1, LOG #433 — to the licensed
CAPACITY claim: *the admissibility layer does not cap the shatter
ladder at the sphere's rung*.  "Not a 3+1 sky" now carries the
cap-system stipulation aloud, the demotion is cited, and the referee's
thin 3+1 control (1,351 skies / 33 capable / 0 shatter-5) is carried as
`[REFEREE-CARRIED]` and labelled thin.  The construction itself needed
no repair: the round rebuilt it with full menus at all 84 steps and
found it FORCED.

**MAJOR 1 REPAIRED.**  The restricted-menu story corrected: membership
is the preserved object (the referee's theorem + 354,319-comparison
sweep, referee-carried); `admissible()` DOES read the actor list in the
delivery branch and weights differ; the builder discards weights, so
the record is unaffected.  G2's text restated; G2b now gates the m = 5
samples (MINOR 1); the per-depth table runs the full height range with
a max-shatter meter per depth (MINOR 2).

**MAJOR 2 REPAIRED/EMBRACED.**  The meter is a (record, reading) pair
property; the record's value is the SUP over committed readings (= 5);
G8 gates the full meter-by-depth profile.

**MINORS/NITS.**  3: the anchor's outside-fact dependence noted in the
note.  4: A2a/A2c relabelled SCALE calibrations.  5: derived-gate
labels added (G5).  6: "selection lives in the measure" widened to
candidate homes (measure, resource cost, counting typicality).  7: the
general Radon argument carried in the note.  8: the schedule deviation
recorded.  NITs acknowledged; dead branch and depth-read left as
recorded residues.

**TERMINAL** for round 1.  Standing after the round: shatter-5 is
constructible and forced; the ladder is uncapped at the sphere's rung;
all sphere calibrations exact; the 3+1 empirical control is the named
gap (a full-strength control at M^{3+1} is a residue).
