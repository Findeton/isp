# D50 — result: THE FORM IS A CHOICE. B2's restriction is PERMANENT.

**Result note, 2026-07-25.**  GREEN-UNREVIEWED.  Pin:
`note-d50-is-the-form-a-law-pin.md` (STRICT, LOG #421, committed
before the receipt existed).  Receipt:
`v10/code/d50_form_law_or_choice_exact.py`, output
`v10/data/d50_form_law_or_choice_exact.out`.

---

## 1. The verdict, and it is the pin's FALSIFIER

> **`[MEASURED, rigorous in this direction]`**
>
> **DEPTH-STATIONARITY DOES NOT FORCE THE STATIONARY FORM.**  The
> space of distinct completions satisfying it has dimension
> **10, 28, 107** at truncation depths 2, 3, 4 — it **GROWS** with
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

**Why the negative is rigorous while a positive would not have
been.**  The pin's one-sidedness doctrine (§4) fixes this in
advance: a tangent-space dimension **> 1 modulo scaling exhibits
nearby non-proportional completions** satisfying the demand, so the
demand demonstrably does not force the form.  A dimension of 1
would only have been local evidence.  The measurement landed on the
side where the count is conclusive.

## 2. The measurements

Boundary directions are the free parameters; **completion
dimension** is the quantity that matters — B1's lesson from D49's
round was that these are different objects, and a direction can be
free while still moving the completion.

| depth | boundary dim | demand | boundary-free | **completion dim** |
|---|---|---|---|---|
| 2 | 23 | I1 renewal agreement | 23 | 22 |
| | | I2 bisimulation (same depth) | 13 | 12 |
| | | **I3 depth-stationarity** | 11 | **10** |
| | | **I5 = I3 + foliation-invariance** | 11 | **10** |
| 3 | 84 | I1 | 84 | 83 |
| | | I2 | 35 | 34 |
| | | **I3** | 29 | **28** |
| | | **I5** | 29 | **28** |
| 4 | 313 | I1 | 308 | 307 |
| | | I2 | 119 | 118 |
| | | **I3** | 108 | **107** |
| | | **I5** | 108 | **107** |

I3 is genuinely stronger than I2 as a constraint system at every
depth (16 vs 14, 109 vs 101, 610 vs 589 constraints), so this unit
is not re-measuring B2 — the cross-depth comparisons B2's
same-depth grouping omitted are really there.  They simply do not
bite hard enough.

## 3. The sharper half: FOLIATION-INVARIANCE ADDS NOTHING

I5 imposes I3 **and** paper 30 demand (b) — foliation-invariance,
in its Z-level sufficient form.  It **more than doubles** the
constraint count (25 vs 16, 210 vs 109, **1,374 vs 610**) and
leaves the completion dimension **exactly unchanged** at every
depth.

> **The residual freedom is not gauge freedom.**  It survives both
> record-level demands imposed together.

This closes off the obvious rescue.  One cannot say "of course
stationarity alone is too weak; add gauge-invariance and it will
collapse" — it was tried, and it does not.

## 4. Why the pin's §3 argument failed — diagnosed, not hand-waved

The sketch ran: I2 makes `r = Z(h+e)/Z(h)` a function of
`(class(h), class(h+e))`; path-consistency then forces
`r(s,s') = g(s')/(c·g(s))`, which is the form.

**The hypothesis is false of the demand actually at issue.**  The
record-level demand is **AGGREGATED**: it equates the class-to-class
transfer *summed over events*,
`Σ_{e : cls(h+e) = c} q(e|h)·Z(h+e) / Z(h)`, across histories.  It
constrains **sums, not individual ratios**, so the path-consistency
step never obtains its per-event hypothesis and the gradient
argument never starts.

**And the aggregated reading is the CORRECT one**, which is what
makes this fatal rather than fixable.  What is observable in the
record is the probability of moving from class `s` to class `s'`.
A per-event version would be a demand on unobservable event labels
— exactly the kind of demand-on-`Z` that B2 disqualified.  So the
stronger hypothesis my sketch needed is not available as a
record-level demand at all.

## 5. What is untouched

**D49's existence result stands, entirely.**  A root-free
completion exists; `Zhat` is one; **horn (II) holds**; paper 30
§5.7's `[OPEN, declared]` question is answered in the affirmative.
Nothing in this unit bears on existence — only on the account of
uniqueness, which was already narrowed by B2 and is now narrowed
permanently.

## 6. Defects in this receipt's own construction, owned

- **Run 1 exited 0 having run NO gates.**  D49's module-level
  `sys.exit(1 if FAIL else 0)` survived the AST strip and killed
  the process at D49's verdict.  A receipt that exits 0 silently is
  the worst possible failure mode; it is now stripped explicitly
  and gated (`_exits == 1`).
- **Run 2 crashed on rank.**  D49's `_rank` closes over its global
  `NB = 313` and cannot be reused at other truncation depths.  A
  width-taking rank is now local to this receipt.
- **My own anchor assertion was wrong.**  I asserted 1,191
  histories *at* depth 4.  Paper 30's much-quoted "1,191 histories"
  is the **cumulative** count through depth 4; **976** sit at the
  layer itself (1191 − 215).  Gated correctly now, and worth
  knowing generally — the figure is routinely quoted as if it were
  a layer count.
- **Depth cap declared, not silent:** D = 5 has ~5,280 layer
  histories and a boundary dimension in the thousands; its exact
  rank did not finish in 10 minutes and was cut.  The trend across
  2, 3, 4 is monotone and decisive without it.

## 7. Residues

1. **Is there ANY record-level demand that forces the form?**  This
   unit refutes the two strongest candidates plus their
   conjunction.  The question is now open with the obvious answers
   eliminated, which is a better state than it was in.
2. **Does the freedom grow without bound?**  10 → 28 → 107 is
   monotone but three points, and D = 5 was not reached.
3. **Transport scope**, as always, remains open regardless.
