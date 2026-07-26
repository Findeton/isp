# D50 — result: THE FORM IS A CHOICE. B2's restriction is PERMANENT.

**Status:** ROUND-1 REVIEWED AND REPAIRED, 2026-07-26.  Round 1 was
an independent Opus 5 hostile batch review of seven units, frozen at
`v10/reviews/batch-round1-d50-to-d60.md` — for D50, REVISE, 1
BLOCKER / 1 MAJOR / 5 MINOR / 2 NIT.  The AST surgery is sound, the
sweep runs, the trend is real, and the unit's headline survives
everything and is **stronger** than the first draft claimed.  What did
not survive is the arithmetic of the quantity the headline is stated
in: **the I2/I3/I5 constraint rows were not the demand's
differential.**  Every number in §2 below has moved, and D49/B2's
much-quoted **119 becomes 137**.  Repairs applied; receipt rerun
green.  Pin `note-d50-is-the-form-a-law-pin.md` (STRICT, LOG #421,
committed before the receipt existed).  Receipt:
`v10/code/d50_form_law_or_choice_exact.py` (13 PASS / 0 FAIL, exit
0), output `v10/data/d50_form_law_or_choice_exact.out`.  An
independent hostile round is required before anything here is
citable.

---

## 1. The verdict, and it is the pin's FALSIFIER

> **`[MEASURED, and now CONSTRUCTIVE in this direction]`**
>
> **DEPTH-STATIONARITY DOES NOT FORCE THE STATIONARY FORM.**  The
> space of distinct completions satisfying it has dimension
> **12, 32, 125** at truncation depths 2, 3, 4 — it **GROWS** with
> depth rather than collapsing to a single ray.
>
> **Therefore paper 30 §5.7's form is a genuine CHOICE, D49's
> round-1 restriction (B2) is PERMANENT, and every citation of D49
> must carry it: "the record law is forward-complete" is true of the
> law PLUS the form, and may never be quoted without it.**

**The pin pre-registered the opposite** (§3: *"EXPECTED: I3 FORCES
THE FORM"*), with its argument written out before the measurement.
The expectation is refuted.  Recording it in advance is what makes
this a result rather than a story.

**The negative is CONSTRUCTIVE, not doctrinal** (round-1 MINOR 2).
The pin's one-sidedness doctrine declared a tangent count > 1 modulo
scaling "RIGOROUS in the negative"; round 1 pointed out that this is
not automatic — a kernel of the linearization exhibits a nearby
*solution* only at a regular point of the (quadratic) variety, and
the receipt never argued regularity.  The stronger fact is true and
is now certified.  Along `b* + t·v` with `v` in the kernel of the
corrected rows, `F(b*+t·v) = t²·Q(v)`, so the line lies in the
variety exactly when `Q(v) = 0`; the kernel is searched for such a
`v`, and the residual is then verified zero at four distinct `t`
(0, 1, 1/3, 2), which makes the quadratic identically zero — no
numerics, no regularity assumption.  At small `t` the perturbed `Z`
is **strictly positive everywhere** and the induced completion
**genuinely differs** from `b*`'s.

> **There is an exact one-parameter family of strictly positive,
> genuinely different completions satisfying depth-stationarity.**

Two facts are reported and both are basis-free: such a direction
exists, and `Q` is *not* identically zero on the kernel — so not
every tangent direction integrates, which is exactly round 1's
objection, conceded and then answered.  (The *count* of qualifying
basis vectors is basis-dependent and is deliberately not reported as
a number.)

## 2. The measurements — CORRECTED BY ROUND 1

**BLOCKER 1.**  The demand is *"the completed class-to-class transfer
is a function of the class"*:
`F_c(b) = A_c(b)·Z_{h1}(b) − B_c(b)·Z_{h0}(b) = 0`, which is
**quadratic** in `b`.  Its differential needs the product rule in
full:

```
 dF_c[v] = A_c(v)·Z_h1(b*) + A_c(b*)·Z_h1(v)
         − B_c(v)·Z_h0(b*) − B_c(b*)·Z_h0(v)
```

The committed receipt computed only the first and third terms.  The
same file got it right in the `'ren'` branch (I1) — one demand was
linearized correctly and the other was not, in the same function.
The receipt now carries the **exact-in-`t` certificate**: `F` is
quadratic, so `(F(b*+v) − F(b*−v))/2` *is* `dF/dt|₀` exactly, over
Fractions, with no numerics.

```
[EXACT-IN-t TEST at D = 2, deterministic rational direction v]
  rows tested = 16;  b* OFF the demand variety (residual != 0) in 0
  d50's row . v  == dF/dt|0  in   0/16
  FULL  row . v  == dF/dt|0  in  16/16
```

`b*` sits exactly on the demand variety at every row and every depth,
so the tangent-space framing was legitimate; only the tangent was
miscomputed.

| depth | boundary dim | demand | boundary-free | **completion dim** | (committed, defective) |
|---|---|---|---|---|---|
| 2 | 23 | I1 renewal agreement | 23 | 22 | 22 |
| | | I2 bisimulation (same depth) | 14 | 13 | 12 |
| | | **I3 depth-stationarity** | 13 | **12** | *10* |
| | | **I5 = I3 + foliation-invariance** | 13 | **12** | *10* |
| 3 | 84 | I1 | 84 | 83 | 83 |
| | | I2 | 38 | 37 | 34 |
| | | **I3** | 33 | **32** | *28* |
| | | **I5** | 33 | **32** | *28* |
| 4 | 313 | I1 | 308 | 307 | 307 |
| | | I2 | **137** | 136 | *118* |
| | | **I3** | 126 | **125** | *107* |
| | | **I5** | 126 | **125** | *107* |

> **FORWARD CORRECTION, corpus-wide: D49/B2's published
> "bisimulation-invariance leaves 119 of 313 boundary directions
> free" is 119 under D49's own linearization and 137 under the
> corrected differential.  Wherever 119 is quoted, it must become
> 137.**

SF0(b), the port check, is restated rather than dropped: it
reproduces D49's 119 **exactly** — and that is precisely why it could
not catch the error.  Porting D49's *method* ports its product-rule
error with it, so the anchor certifies the error instead of detecting
one.  A port check cannot be an independence check.

**The damage is that the conclusion strengthens.**  The corrected
dimensions are *larger*, still monotone, still far from 0: I3 fails
to force the form more freely than the first draft reported.  Every
qualitative claim of LOG #422 stands; every quantitative one is
restated here.

I3 is genuinely stronger than I2 as a constraint system at every
depth (16 vs 14, 109 vs 101, 610 vs 589 constraints; ranks 10 vs 9,
51 vs 46, 187 vs 176), so this unit is not re-measuring B2 — the
cross-depth comparisons B2's same-depth grouping omitted are really
there.  They simply do not bite hard enough.

## 3. The sharper half: FOLIATION-INVARIANCE ADDS NOTHING

I5 imposes I3 **and** paper 30 demand (b) — foliation-invariance, in
its Z-level sufficient form.  It **strictly increases** the
constraint count (25 vs 16, 210 vs 109, **1,374 vs 610** — factors
1.56×, 1.93×, 2.25×) and leaves the completion dimension **exactly
unchanged** at every depth, **under both linearizations**, so the
conclusion is linearization-independent.

> **The residual freedom is not gauge freedom.**  It survives both
> record-level demands imposed together.

Round-1 MINOR 1: the committed label and LOG #422 said I5 "MORE THAN
DOUBLES" the constraint count.  It more than doubles only at D = 4.
The gate's predicate was always the correct one (`>`); only the
sentence overstated, in three places.

## 4. Why the pin's §3 argument failed — diagnosed, not hand-waved

The sketch ran: I2 makes `r = Z(h+e)/Z(h)` a function of
`(class(h), class(h+e))`; path-consistency then forces
`r(s,s') = g(s')/(c·g(s))`, which is the form.

**The hypothesis is false of the demand actually at issue.**  The
record-level demand is **AGGREGATED**: it equates the class-to-class
transfer *summed over events*, so it constrains **sums, not
individual ratios**, and the path-consistency step never obtains its
per-event hypothesis.

**And the aggregated reading is the CORRECT one**, which is what
makes this fatal rather than fixable.  What is observable in the
record is the probability of moving from class `s` to class `s'`.  A
per-event version would be a demand on unobservable event labels —
exactly the kind of demand-on-`Z` that B2 disqualified.

## 5. What is untouched

**D49's existence result stands, entirely.**  A root-free completion
exists; `Zhat` is one; **horn (II) holds**; paper 30 §5.7's
`[OPEN, declared]` question is answered in the affirmative.  Nothing
in this unit bears on existence — only on the account of uniqueness.

## 6. Instrument corrections carried by round 1

- **SF6, the negative control, was VACUOUS at two of its three
  depths** (round-1 MAJOR 1).  I1 imposes **zero** constraints below
  depth 4 — the renewal pair `H3`/`h2e` does not exist in a depth-2
  or depth-3 truncation — so `compdim = rank(M) = NB − 1` is forced
  and `> 0` was a theorem-pass there.  The receipt *printed* the
  zeros and counted them as passes anyway.  **The instrument is
  validated at ONE depth, not three**, and the gate now says so.
- **SF3 is labelled a REPORTING gate** (round-1 MINOR 3): its
  predicate is `len(stat_dims) > 0` and cannot fail.  That is
  legitimate under the pin's exit-0-either-way falsifier, but D58's
  A3 shows the house style is to say so.  The falsifiable content
  moved to SF3b (§1).
- **The pinned PYTHONHASHSEED gate is built** (round-1 MINOR 4).
  Pin §5 SF7 marked it "non-optional" — D49's own A4 defect makes it
  so — and the committed receipt implemented only the AST scan.  The
  receipt now re-runs *itself* in probe mode under seeds 0/7/61/999
  and compares.
- **The AST strip is gated to bind no enclosing-scope names**
  (round-1 MINOR 5), so the surgery provably cannot have removed a
  side effect the imported state depends on.
- **`rank(M) = NB − 1` at every depth, and the 1-dimensional kernel
  IS the overall-scaling direction** — verified pointwise (round-1
  NIT 2).  That is *why* "compdim = 0 ⇔ one ray" is the right reading
  of the quantity the headline is stated in; the receipt relied on it
  and never said it.
- **The depth cap is a measured artefact, not a comment** (round-1
  NIT 1): the per-depth wall-clock rank cost is printed
  (0.2 s / 7.3 s / 256 s), and D = 5 is cut against that trend.

## 7. Defects in this receipt's own construction, owned

- **Run 1 exited 0 having run NO gates.**  D49's module-level
  `sys.exit(1 if FAIL else 0)` survived the AST strip and killed the
  process at D49's verdict.  A receipt that exits 0 silently is the
  worst possible failure mode; it is stripped explicitly and gated
  (`_exits == 1`).
- **Run 2 crashed on rank.**  D49's `_rank` closes over its global
  `NB = 313` and cannot be reused at other truncation depths.  A
  width-taking rank is local to this receipt.
- **My own anchor assertion was wrong.**  I asserted 1,191 histories
  *at* depth 4.  Paper 30's much-quoted "1,191 histories" is the
  **cumulative** count through depth 4; **976** sit at the layer
  itself.  Worth knowing generally — the figure is routinely quoted
  as if it were a layer count.

## 8. Residues

1. **Is there ANY record-level demand that forces the form?**  This
   unit refutes the two strongest candidates plus their conjunction.
2. **Does the freedom grow without bound?**  12 → 32 → 125 is
   monotone but three points, and D = 5 was not reached.
3. **The corpus-wide 119 → 137 forward correction** must land
   wherever D49/B2's figure is quoted.
4. **Transport scope**, as always, remains open regardless.
