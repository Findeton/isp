# D62 — ROUND 1 INDEPENDENT HOSTILE REVIEW

**Frozen:** 2026-07-26.
**Unit under review:** D62 "(H2): the update table" —
`note-d62-h2-update-table-pin.md` (STRICT, frozen first),
`note-d62-h2-update-table.md` (the result note: Row 0 + rows
R1/R2/R2′/R3/R4, obligations O1/O2/O3, the §7 assembly),
`code/d62_h2_update_table_exact.py` + `data/d62_h2_update_table_exact.out`
(24 PASS / 0 FAIL), LOG #457.
**Reviewer:** independent Opus 5 worker, no prior context, no loyalty to
the unit. **Recompute, never trust:** every number below was produced by
code I wrote for this review, run from the repo root; scratch under
`/private/tmp/claude-501/…/scratchpad/d62rev/`. Calibration:
`reviews/d61-round1-hostile-review.md` (whose BLOCKER 1 named the three
obligations this unit claims to discharge).

**VERDICT: REVISE. 0 BLOCKER / 1 MAJOR / 7 MINOR / 3 NIT.**

**(H2) survives everything I threw at it, and the headline is earned this
time.** I re-implemented the serialised state, its canonicalisation, the
`(sigma, renamed event)` pairing and **all five rows of the table** from
the note's prose alone — a different normal form (nested tuples, `live`
as a *set*, not d44a's `repr`), sharing nothing with the D62 receipt —
and compared my table's prediction against the committed layer's own
`sigma(h+e)`:

```
parents to depth 6    34,375 histories      179,782 transitions into depth 7
   table mismatches 0 | (H2) keys 176 | keys with two successors 0 | states 36
parents to depth 7   179,783 histories      930,630 transitions into depth 8
   table mismatches 0 | (H2) keys 176 | keys with two successors 0 | states 36
parents to depth 8   930,631 histories    4,778,310 transitions into depth 9
   table mismatches 0 | (H2) keys 176 | keys with two successors 0 | states 36
```

i.e. **two full levels beyond the receipt** (which gates transitions into
depth 7), under code that shares nothing with it. My canonicalisation
induces exactly d44a's partition (36 ↔ 36, zero splitting classes in
*either* direction), my row census is the
receipt's to the unit (68,750 / 57,020 / 9,656 / 35,412 / 8,944), and I
reproduced every one of the note's unforced cross-identities from scratch.
I then walked the five rows against the layer source by hand, line by
line, and **each step is a legitimate reading of a quoted line or of a
D61 theorem.** The O2 tuple-equality argument is airtight (fixed 5-arity,
base at index 1, `V0` excluded by arity), and I could not admit a single
name-colliding arb on a surface **2.3× wider** than the receipt's.

**Unlike D61, the sentence on the cover is the sentence that was proved.**
The consequence chain in pin §3, note §1/§10, the receipt VERDICT and LOG
#457 is *identical* and no wider; the book still reads "conditional on
**(H2)** alone" — the embargo was honoured.

**What is wrong is the receipt's evidence architecture, not the
mathematics.** Three of the twenty-four gates — including the pin's own
T3 and T4 headline predicates — **cannot fail**: two are entailed by
T1(a), one is a tautology of the way the counter is built. And
the note's falsifiability paragraph makes a claim about its own mutant
battery that is false. That is MAJOR 1. Everything else is label
hygiene.

---

## MAJOR 1 — the gates are not independent: three of the twenty-four cannot fail (two entailed by T1(a), one a tautology), and the "eleven mutants … and on no other" sentence is false

**Where.** Receipt `T1(e)`, `T3(b)`, `T4(a)`; note §5 ("Rows are selected
by … a partition, with no fall-through (**[EXACT] T4(a)**, 179,782
transitions, 0 unmatched)"), §8 ("**[EXACT] T1(e)**", introduced in the
gate label as "**gated because it can fail**"), §6.1/§9 (T3(b)); note §9's
closing paragraph ("**eleven mutants** … each produce `[FAIL]` on the gate
that owns them, **and on no other**"); LOG #457 ("**ELEVEN MUTANTS each
fail exactly their owning gate**").

**The defect, in three parts.**

**(a) `T1(e)` is a theorem of `T1(a)`.** `TABLE`'s arb branch reads
`ck = tuple(e[2])` and **never touches `e[3]`** (the winner key `W`) — the
note says so itself ("Rows R3/R4 use `W` only through `vname(b, W, x)`,
which the table abstracts to one fresh token"). `T1(e)` groups the keys by
`key2 = (sb, e[:3])` — exactly the arguments `TABLE` reads — and checks
that the *layer's* targets agree inside each group. But `T1(a)` has
already asserted that every layer target **equals** `TABLE(sb, eb)`, and
`TABLE` is constant on each `key2` group by construction. So `wbad == 0`
is entailed. The gate's own label ("gated because it can fail") is
therefore wrong.

**(b) `T3(b)` is a theorem of `T1(a)`, identically.** `o1_cls[(sb,eb)]`
collects `canon_sigma(h+e)` per key; `T1(a)` says each equals
`TABLE(sb,eb)`, a single value. `o1_split == 0` cannot be non-zero. This
is the pin's **T3** ("the O1 sub-case isolated … successor sigmas
pairwise identical within each class").

**(c) `T4(a)`'s headline number is identically zero.** `unassigned =
ntr - sum(rowcount.values())`, and `rowcount[row] += 1` runs once per
transition from the row label `TABLE` returns — and `TABLE` returns a row
on **every** path (`'n'` → R1; `'p'` → R2/R2′; `else` → R3/R4). There is
no fall-through path to detect. `unassigned == 0` is `ntr - ntr == 0`.
This is the pin's **T4** ("no silent fall-through"). *(The other two
conjuncts of `T4(a)` — every row non-empty, `set(rowcount) == set(ROWS)`
— are real; it is the advertised number that is vacuous. The genuine
fall-through risk — an admissible event whose class matches no row's
**preconditions** — is caught by `T4(c)`, not by `T4(a)`.)*

**(d) The mutant sentence is false, and I measured it.** I rebuilt the
battery (`d62rev/mutants.py`; every pattern the note names is present in
the source, so the eleven mutants do exist) and ran each against the
committed receipt:

```
BASELINE (CAP=4)                                        FAILs = []          rc=0
M1  R3 invisible-supersession clause hold'[y]           FAILs = T1(a), T5           rc=0
M2  Row 0 opposite-bit test                             FAILs = T1(a), T1(d), T5    rc=0
M3  O1's forced flag (R2' sets sup = True)              FAILs = T1(a), T5           rc=0
M4  O2's freshness (minted token not superseded)        FAILs = T1(a), T5           rc=0
M5  R3 live' = live \ C                                 FAILs = T1(a), T5           rc=0
M6  R4 both actors gain v                               FAILs = T1(a), T5           rc=0
M7  R2/R2' row-selection test                           FAILs = T1(a), T4(a), T5    rc=0
M8  R3 precondition predicate                           FAILs = T4(c)               rc=0
M9  O1 forcedness predicate                             FAILs = T3(a)               rc=0
M10 (5e) predicate                                      FAILs = T3(c)               rc=0
M11 O2 adversarial admitted-counter                     FAILs = T2(b)               rc=0
M12 sub-case census                                     FAILs = T4(e)               rc=0
```

**Every table-side mutant fails at least two gates** — always `T1(a)`
*and* `T5`, because `T5`'s `bfs_bad` runs the very same `TABLE`. That
includes all four the note names by hand (M1 the invisible-supersession
clause, M2 Row 0's bit test, M3 O1's flag, M4 O2's freshness). Re-run at
the **anchored depth** (`CAP = 6`, M1, 79 s): identical — `T1(a)` and
`T5` both `[FAIL]`, `22 PASS / 2 FAIL`, exit 0. The five gate-predicate
mutants **do** fail exactly one gate each, exactly as claimed. So the
sentence is true of the five gate mutants and false of all six row
mutants — and it is this sentence, repeated as a campaign fact in LOG
#457, that carries the unit's entire falsifiability case.

**Why this matters and not more.** None of (a)–(d) touches the
mathematics: I re-derived the rows independently and the table is right.
But the receipt sells **24 PASS** as 24 pieces of evidence, and the pin
sells **T3** and **T4** as two of its four gates; on the count that
matters, T1(a) + T2(a)/(b)/(c) + T1(c)/(d) + T4(c)/(e) + T5 are the
independent ones and T1(e), T3(b) and T4(a)'s number are not. Given that
the pin's own §2 opens with *"a cache-gated table check alone cannot close
the depth gap"*, a reader is owed an accurate map of which gate buys what.

**Repair.** (i) Re-label `T1(e)` and `T3(b)` as **corollaries of T1(a)**
(they are worth printing; they are not worth counting). (ii) Replace
`T4(a)`'s `unassigned` counter with a real one — e.g. re-derive the row
**from the event class alone** (tag, `base ∈ refs`, `|proposers(ckey)|`)
in a second function and assert it equals `TABLE`'s label, which *can*
disagree. (iii) Restate §9's mutant sentence as measured: "five gate
mutants fail exactly their owning gate; six row mutants fail T1(a) and
T5 together, because T5 re-runs the same table" — and forward-correct
LOG #457.

---

## MINOR 1 — `T1(a)`'s failure headline is silently capped at three

**Where.** Receipt: `if len(mism) < 3: mism.append(...)`, then
`f"transitions = {ntr}, mismatches = {len(mism)}"`.

On a genuine falsification the number a reader would quote is `len(mism)`,
which is **capped at 3**. Demonstrated on the M1 mutant at the anchored
depth:

```
[FAIL] T1(a) … (transitions = 179782, mismatches = 3,
                per-row mismatches = {'R3-self-arb': 14772})
```

The true count is **14,772**; the headline says 3. The per-row dict does
disclose it, so nothing is hidden, but the receipt's banner elsewhere
boasts "**No silent cap**" about depth, and the pin's §4 makes the
counterexample *the deliverable*. One line: count separately from the
example list.

## MINOR 2 — `N0(c)`'s code-facts assert continuation lines, not the predicates their labels name; Row 0's own layer line is not asserted anywhere

**Where.** Receipt `_F` (14 strings).

Three labels promise more than the string they assert (I checked each
against the slice):

| label claims | string actually asserted | the missing half |
|---|---|---|
| "`edges()`: a conflict edge needs **same base, opposite bits**, INCOMPARABLE" | `and self.incomparable(i, k)):` | `if (pi[2] == pk[2] and pi[3] != pk[3]` — **the entire content of Row 0** |
| "`holdings(a)`: a gains the minted version **iff a proposed in the ckey**" | `h.add(vname(base, op[3], op[1]))` | `if a in {t[0] for t in op[2]}:` — the note's own **(L5)** |
| "`View.live`: a proposal is live **iff its triple is unresolved**" | `if (op[1], op[2], op[3]) not in self.resolved}` | the comprehension head |

Row 0 *is* obligation O3, and the line it replaces with `f(live)` is the
one line of the layer the receipt never asserts. This is precisely the
class D61 round 1 MINOR 2 convicted (`N1` gating only half the
version-register fact) and the D61 delta repaired — one unit later, in
the same idiom.

## MINOR 3 — O1 step 4 and `T3(c)` attribute the naming's choice-freeness to (5e); for `canon_pair` it is free by construction, and (5e)'s real load is step 2

**Where.** Note §6.1 step 4 ("by (5e) at most one actor's token is
full-superseded, so at most **one** base can ever be re-imported this
way, and `canon_pair`'s extension `100 + i` assigns it the single name
`100` with no residual choice"); receipt `T3(c)`'s label ("If two were,
two distinct dropped bases could be **mentioned** and the canonical
renaming would have a genuine choice").

`canon_pair(hk, e)` calls `_menu_extras([(e, None)], m)` on **one event**.
A propose has **one** base, an arb's ckey/wkey share **one** base. So
`|extras| ≤ 1` **unconditionally**, whatever (5e) does — measured, my own
code: extras spectrum `{0: 4,559,438, 1: 218,872}` over 4,778,310
transitions,
`|extras| ≥ 2` never, and **arbs carrying an extra: 0**. The "genuine
choice" `T3(c)` warns about is a fact about `canon_menu` (D61's object,
where the *whole menu*'s extras are renamed jointly — the adopted note's
§8 GAP 2), not about the object (H2) is stated on.

(5e)'s genuine load in O1 is **step 2** (`X_x ∉ refs`, via "a live triple
on `X_x` would have to be `y`'s, forcing `X_y = X_x`, hence both dropped").
That use is correct and load-bearing; the step-4 citation is decorative
and, as written, invites a reader to think the row would break without it.
*(Worth recording as the stronger fact the unit could have claimed: the
table's R2′ row would still be correct with two dropped bases, since the
second one's flag is already in `Σ`.)*

## MINOR 4 — `N0(e)`'s "the table is blind to history" is a one-call-deep static check

**Where.** Receipt `N0(e)`: it inspects `TABLE.__code__.co_names` and
`comps_of_live.__code__.co_names` only, and separately asserts
`'ser' in canon_parts.__code__.co_names`. It never inspects `canon_parts`
or `parse_sigma` for the forbidden names, so a history read placed one
call down would pass. The label ("its **source** mentions no history,
poset, view or layer enumerator") claims a transitive property from an
intransitive test. *(The property itself is true — I re-implemented the
table from the prose reading nothing but its two arguments and got the
same answers at depth 8 — so this is hygiene, not substance.)*

## MINOR 5 — §3's "All quoted verbatim" is false for one line, and the "18 lines" it credits to itself are a different set

**Where.** Note §3 ("All quoted verbatim from
`v10/code/d42b3_placement_exact.py`; the receipt asserts each against the
source (**[EXACT]** N0(c)/N0(d), 18 lines, 0 missing)").

I diffed the §3 block against the source. Of 34 non-blank quoted lines,
**one is not verbatim**: the note writes
`        for x in (0, 1): out.append((b, x))` where the source has two
lines. And the arithmetic does not line up: §3 carries **13** labelled
lines (L1)–(L13); `N0(c)` asserts **14** strings, of which **two**
(`regs_of`'s body) are *not quoted in §3 at all*, while §3's (L5) is
*not asserted* (MINOR 2). "18" = 14 + 4 is the receipt's count of a
different set. §9's table repeats it as "the 18 source lines **the rows
quote**".

## MINOR 6 — §2's "one structural claim" says the rows *consult* `sup` in two places; the second is a write, and §6.1 says so

**Where.** Note §2 ("Rows R1–R4 below consult `sup` in exactly two
places: the flag of a token in `refs` … and the flag of the **one** token
a dropped-base propose re-imports, which is **forced to `True`** …
Nothing else is read. **[PROOF]**") vs §6.1 step 3 ("the successor's new
flag is **computed, not read**").

As written the sentence concedes a *read* of a mark `Σ` dropped — which
is exactly the thing the paragraph exists to deny — and then denies it
two sections later. The rows in fact **read** a superseded flag in
exactly one place (R3's precondition disjunct `flag(b) = True`) and
**write** two (R2′'s `b ↦ True`, R3/R4's `b ↦ True`, `v ↦ False`).
The paragraph the note itself calls "the one structural claim the table
must earn" should say that.

## MINOR 7 — `T2(b)`'s "GATED ADVERSARIALLY" pool consists only of events the layer once offered

**Where.** Receipt `T2(b)`; pin §2 T2 ("constructed **adversarially** if
reachable"); note §6.2.

The pool is `{arbs of h} ∪ {arb candidates at every prefix of h}` — 157,888
events, all of which the committed enumerator itself produced at some
prefix. That is a *reachability-restricted* surface, not an adversarial
one; the 11,584 "NOT in h" events are still layer-minted.

**I built the adversarial surface the pin asked for** (`d62rev/o2wide.py`):
every syntactically well-formed `('r', a, C, W)` with `C` a non-empty
single-base subset of **all** proposal triples ever uttered in `h` (live
**or** resolved), `W` any non-empty subset of `C`, `a ∈ {A,B}` — most of
which the layer never offered:

```
depth <= 5   58,160 arb events tested   10,164 collide with a present base   0 ADMITTED
depth <= 6  358,800 arb events tested   69,652 collide with a present base   0 ADMITTED
            (breakdown: |C| = 1 and |C| = 2, both actors, all refused)
on-shell:   44,356 admissible arbs, 0 collisions
```

The conclusion is unharmed and now rests on 2.3× the surface. The label
should say what the pool is.

---

## NIT 1 — `T5`'s `not bfs` conjunct is vacuous

The `while bfs:` loop above it drains the queue, so `not bfs` is true by
construction. Cosmetic, but it sits inside a five-way conjunction that is
otherwise real.

## NIT 2 — §7 step 2's "F … never inspects a token's identity" is false as implemented, and harmlessly so

`comps_of_live` iterates `for b in sorted(by, key=repr)` and the note's own
`f` "group[s] the live triples by base" — both order by token identity.
Nothing turns on it, because `ser` re-sorts every field *after* renaming
and `canon_parts` minimises over all relabellings. The clean statement is
"F's output is determined up to relabelling of the tokens it copies".

## NIT 3 — §7 step 4 leans on a uniqueness it never needed (and which I verified holds anyway)

"Well-definedness of the input" would be one line: `canon_pair` returns
`(sbest, ebest)` **because some** sigma-attaining `m` realises that pair;
row correctness applies to *that* `m`; done. As written it reads as
though two `m`'s attaining `sigma(h)` might give different renamed events
and hence different table outputs. They cannot — and in fact the question
never arises at this scope: **the sigma-minimising renaming is unique on
all 4,778,311 histories to depth 9** (spectrum `{1: 4,778,311}`), and the
renamed event is unique on all 4,778,310 transitions
(`{1: 4,778,310}`), by my own canonicalisation. Worth stating, since it is
the step the pin
identified as carrying the highest residual risk.

---

## Checked and CLEAN

* **Receipt rerun:** `24 PASS / 0 FAIL`, exit 0, 112 s (machine), output
  **identical to the committed `.out` modulo the `[t = …s]` timing
  lines**. **Byte-identical under `PYTHONHASHSEED` 0 / 1 / 7 / 12345**
  (md5 `a948655075fe4cc41b385dcc7e06a15c`, all four) — one seed beyond the
  note's claim. This matters: the layer uses `next(iter(frozenset))` and
  `sorted(…, key=repr)` in load-bearing places.
* **Exit protocol verified empirically at the anchored depth**, not just
  read: the M1 row mutant at `CAP = 6` prints the T1 counterexample block,
  fails T1(a) and T5, leaves every `anchor=True` gate green, and **exits
  0**. Pin §4 is honoured. I also confirmed the failure mode a
  closure break would take (a 37th state appearing as a *successor*) trips
  `T1(c)`, which is not an anchor — so substantive negatives cannot exit 1.
* **THE TABLE, INDEPENDENTLY RE-IMPLEMENTED FROM THE NOTE'S PROSE.** My
  own `raw_state` (own `own_alive`, no singleton assumption), my own
  normal form (nested tuples; `live` a **set** where d44a uses a tuple),
  my own minimisation, my own `canon_pair`, my own five rows. Only the
  committed **admission layer** is shared — it is the object under study.
  Results:

```
parents <= 4   1,191 hist |     6,470 transitions | 28 states | 140 keys | 0 splits | 0 mismatches
parents <= 6  34,375 hist |   179,782 transitions | 36 states | 176 keys | 0 splits | 0 mismatches
parents <= 7 179,783 hist |   930,630 transitions | 36 states | 176 keys | 0 splits | 0 mismatches
parents <= 8 930,631 hist | 4,778,310 transitions | 36 states | 176 keys | 0 splits | 0 mismatches
```

  The last two sweeps are **one and two levels past the receipt**
  (transitions into depth 8 out of the 930,631-history family, and into
  depth 9 out of all 4,778,311 histories to depth 9), memory-lean DFS,
  each history's state computed exactly once, 22 min for the last.
  Invariants over the same sweeps: **(5e) violations 0, Row-0
  (`comps = f(live)`) failures 0, alive-not-singleton 0, arbs carrying an
  extra token 0**, `|event extras|` never above 1
  (`{0: 4,559,438, 1: 218,872}` at the deepest), and the sigma-minimising
  renaming **unique on all 4,778,311 histories**.
* **My canonicalisation induces exactly d44a's.** Cross-checked against
  the committed `canon_sigma` by text slice on all 34,375 histories:
  36 classes ↔ 36 classes, **0 of my classes split a d44a class and 0
  d44a classes split mine**. (Corollary, since my `live` is a set and
  d44a's a tuple: **no history ever carries duplicate live triples** —
  the layer resolves by triple, not by index, so this was worth checking
  and the note does not.)
* **Row census reproduced to the unit**, independently:
  `R1 68,750 / R2 57,020 / R2′ 9,656 / R3 35,412 / R4 8,944` at depth ≤ 6;
  `359,566 / 294,332 / 46,264 / 189,268 / 41,200` at depth ≤ 7 and
  `1,861,262 / 1,515,388 / 218,872 / 994,132 / 188,656` at depth ≤ 8 —
  every row non-empty at every level, R2′ and R4 included.
* **Every cross-identity the note calls unforced, recomputed from
  scratch** (`d62rev/crossid.py`, depth ≤ 6): `(h, actor)` pairs with
  `hold = None` and no live own proposal **4,828** (× 2 bits = the
  **9,656** R2′ proposes = the D61 round's missed-supersession excess);
  R3 on a HELD token **24,236** / on a DROPPED token **11,176**;
  opponent token dropped by the arb **14,772**; of those, opponent left
  **STRANDED 8,944**; opponent already dropped **6,744**; opponent
  untouched **13,896**; R3 + R4 = **44,356**; states with two same-bit
  live proposals on one base **2,236**. All exact.
* **The O1 attack the pin invited does not exist — and that is a
  strengthening.** I hunted for long invisible-supersession chains
  (token dropped → re-imported by R2′ → re-superseded → again). They are
  impossible: exhaustively to depth 6, the number of **drop onsets per
  history** is `{0: 14,027, 1: 20,348}` — **never 2**, and the directed
  deep walks agree out to depth 150 (max cycles in any trajectory: 1). The reason is structural: a re-imported token is
  re-superseded only by its owner's own arb (visibly), and by (5c) no new
  shared base is ever minted, so the `100` renaming is asked to name a
  second token *never*. The note's O1 is safe for a stronger reason than
  it gives.
* **O2, walked by hand and attacked.** The tuple-equality step is
  airtight: `vname` returns a **fixed 5-tuple** with the base at index 1,
  so `v = b'` forces `b_j = b` **even when `b` is itself a 5-tuple vname**
  (no nesting ambiguity), and `V0 = ('v','v0')` is excluded by arity, not
  by luck. The view step is if anything stronger than the note says: if
  the name already existed, `regs_of(e)` contains that version register,
  so `h[j] ∈ pred[j]` *directly*, before Lemma 1(c) is even invoked.
  Wide adversarial census above: **0 admitted out of 69,652 colliding
  candidates**.
* **`T2(c)`'s witness reproduced independently:** at `h = [pA(v0,0),
  pB(v0,1)]` the self-arb and the pair-arb both mint
  `('v', ('v','v0'), (0,), ('A',), 'A')`, **both are admissible**, and
  each refuses the other afterwards (`selfA after PAIR = False`,
  `PAIR after selfA = False`, `selfA after selfA = False`). Their
  `canon_pair` renamings differ in the ckey, so they are distinct keys —
  no (H2) hazard. The obligation is genuinely non-vacuous.
* **The five rows, checked step by step against the layer source.** R1
  (`View` partitions events into `props`/`arbs` by tag, so an `'n'`
  enters neither, and appending never changes an earlier `pred[j]`);
  R2 (`regs_of` of a `'p'` is `{x}`, so `b`/`i` do not enter the view;
  (L8)+(5a) force `b = X_x`; (L9)+Lemma 4(c)+(5b) force no live
  `x`-proposal; a `'p'` touches neither `arbs` nor `superseded`);
  R2′ (`b ∉ refs` ⟹ `hold[x] = None`, since `hold[y]` is never a
  superseded token and a live triple on `X_x` would force `X_y = X_x`);
  R3 (the arb's registers are `{x} ∪ {vname(·,·,x)}`, it is the **last**
  event, and `cone_y(h+e)` is the downset of the register-`y` chain — so
  the arb is outside it and `X_y` is untouched, while `hold` is the
  full-view test and `sup' ∋ b`: this is the invisible supersession and
  the note gets it exactly right); R4 (both actor registers ⟹ both cones
  ⟹ both hold `v`, (L2) resolves both triples, (5b) says there are no
  others). `live' = live \ C` is right against a same-bit opponent
  proposal (different component, not in `C`) — and the 2,236 same-bit
  states make that branch non-vacuous. `refs'` recomputation matches
  d44a's `refs` line character for character.
* **§7 assembles.** Row correctness is stated for a fixed `m'`;
  `canon_pair` realises `(sbest, ebest)` under *some* attaining `m`; the
  table's `canon_parts` minimises over the same set of relabellings as
  `canon_sigma`; `m'` is injective on `refs(h+e)` by O1/O2; and
  `refs(h+e) ⊆ refs(h) ∪ {v} ∪ {X_x}` holds row by row. Equivariance is
  real (the table only copies tokens, mints one, and computes flags), so
  even a non-trivial token automorphism of `Σ` would be harmless — and
  there are none at this scope (uniqueness spectrum `{1: 4,778,311}`).
  **`|refs| ≤ 2` is a theorem, not a measurement** (`refs ⊆ {X_A, X_B}` by
  (5b)); measured spectrum `{1: 18,855, 2: 15,520}` at depth ≤ 6.
* **Deep directed walks, far past exhaustive reach.** Four policies
  (including one that maximises R2′ proposes and self-arbs on dropped
  tokens), six seeds each, **150 steps — 3,600 history visits**: my table
  checked against the layer at every step, with (5e), Row 0,
  alive-singleton, `|extras| ≤ 1` and renaming-uniqueness re-checked at
  each visit — **zero violations of any of them**, at histories 140 levels
  past any exhaustive reach, with every row (R2′ 11, R4 5 included) still
  firing. Max drop/re-import cycles in any trajectory: **1**.
* **The scope and the consequence chain are EXACTLY the pin's, and no
  wider.** Pin §3, note §1 blockquote, note §10, receipt VERDICT and LOG
  #457 carry the identical five clauses: (H2) THEOREM at two-actor
  delivery-free d42a scope; d44a unconditional **there**; the 36-state
  closure / six-state chain / Perron package at every depth **there**;
  residue 1 closed **there**; D49's root-free completion unconditional at
  every depth **there** — with **D50 (the form is still a choice)**,
  **delivery-free (transport untouched)** and **three actors out of
  scope** attached in all five places. I checked d44a §8: the hypothesis
  set really is exactly (H0)/(H1)/(H2), and its step (i)'s
  representative-per-class BFS is licensed by (H1) — so the assembly
  closes. `THE-THEORY-SO-FAR.md` still says "conditional on **(H2)**
  alone" at all six places I found it (lines 141, 3941, 4357, 4439, 5688,
  5774); the book patch correctly waited for this round.
* **Anchors are real committed numbers, not this receipt's.** `176` is
  d44a CG3a's traversed-edge count (= CG2's `160` + CG7c's `16`, both
  present in the committed d44a source), `36` is CG1/CG3a, the census
  `[1,6,32,176,976,5280,27904]` is the layer's, `44,356` / `9,656` /
  `68,750` are the D61 round's. I reproduced every one of them from my
  own enumeration.
* **Slice hygiene holds.** The three d44a slices are pure definitions —
  I re-derived the cut points and confirmed `_blk1` (SG_VIOL →
  `canon_sigma`), `_blk2` (`_rename_event` → `canon_menu`) and `_blk3`
  (`canon_pair`) contain no `sys.exit`, no top-level `check(` and no
  top-level `print(`, and that the d42b3 prefix is cut before its first
  `print`. Nothing of d44a's or d42b3's own gate protocol can execute
  inside the receipt.
* **No silent cap on depth.** `CAP` is `sys.argv[1]`, printed with the
  census and the "transitions into depth CAP+1" line; the CAP-dependent
  anchors (`T1(b)`, `T4(b)`, `T2(a)`'s `44,356`) correctly self-disable
  off the anchored depth and the VERDICT refuses to claim the theorem
  when `anchored` is False. I ran `CAP = 4` and `CAP = 6`; both behave as
  documented.
* **§10's residues are the right ones and are honestly stated.**
  "(H2) inherits **exactly** the standing (H1) has, no better … no machine
  has checked the induction *as* an induction" is the correct sentence,
  and `T5`'s in-receipt disclaimer ("the BFS uses one representative per
  class, which is LICENSED BY the rows — coverage evidence, NOT an
  independent proof") is the D61 §4/§5 lesson applied *before* the round
  rather than after it. That is the behaviour the discipline is for.

---

The mathematics is right and the sentence on the cover is the sentence
that was proved — which is more than the previous two attempts on this
claim managed. I re-implemented the object under test from the prose,
compared it with the committed layer on **4,778,310 transitions into
depth 9**, walked all five rows and all three obligations against the source by
hand, ran the O2 collision census on a surface the layer never offered,
and hunted the one structural attack the pin invited (long
invisible-supersession chains) only to find the layer forbids it
outright. Nothing dented (H2). What needs repair is the receipt's account
of itself: two of its twenty-four gates are entailed by a third and a
fourth's headline number is a tautology — two of the three are the pin's
own T3 and T4 — and its one falsifiability sentence is measurably false
for six of its eleven mutants. Those are one
paragraph and one counter each. On the mathematics this unit closes
residue 1 at its declared scope; on the receipt's self-description it
should not ship until MAJOR 1 is fixed and MINORs 1–2 land, because the
next reader of "24 PASS" will believe all twenty-four are evidence.

---

# DELTA — adjudication and repairs (campaign side, 2026-07-26)

MAJOR 1 verified structurally in all four parts before repair (T1(e)'s
targets are TABLE values by T1(a); o1_cls likewise; `unassigned` was
`ntr - ntr`; the mutant co-failure follows from T5 re-running TABLE).
Repairs applied, receipt rerun green — **24 PASS / 0 FAIL**:

1. **MAJOR 1:** T1(e) and T3(b) relabelled `[COROLLARY OF T1(a)]`,
   printed in D58-A3 reporting style, explicitly not counted as
   independent evidence; **T4(a) rebuilt** with an independent row
   classifier (own parse, own tests — it CAN disagree with TABLE's
   label, which is what the old counter could not); the note carries
   an "independent-evidence map" paragraph naming exactly which gates
   can fail; §9's mutant sentence restated AS MEASURED (five gate
   mutants fail their owning gate; six row mutants fail T1(a) AND T5
   together, by design two detections each) and LOG forward-corrected.
2. **MINOR 1:** the T1(a) mismatch count is now total (examples still
   capped at three for printing).
3. **MINOR 2:** N0(c) gains the three missing halves — (L4)'s
   comprehension head, (L5)'s proposer test, and (L7)'s bit predicate
   (the entire content of Row 0); note §3 says which lines are
   asserted.
4. **MINOR 3:** §6.1 step 4 re-attributed — `canon_pair`'s renaming
   is choice-free by construction (one event, one base ⇒ |extras| ≤ 1
   unconditionally); (5e)'s real load is step 2; the round's stronger
   facts recorded (the row survives two dropped bases; the
   two-dropped-base state is unreachable — drop onsets never exceed 1).
5. **MINOR 4:** N0(e) widened to the whole call graph (TABLE,
   comps_of_live, canon_parts, parse_sigma).
6. **MINOR 5/6:** §3's verbatim/count sentence fixed; §2's "one
   structural claim" restated read-vs-write (one read — R3's
   precondition flag, in Σ; two writes).
7. **MINOR 7:** T2(b) relabelled reachability-restricted, with the
   round's truly adversarial surface (69,652 colliding candidates, 0
   admitted, 2.3×) cited.
8. **NITs:** T5's vacuous `not bfs` conjunct dropped; §7 step 2
   restated (output determined up to relabelling); §7 step 4 reduced
   to the one-line argument, with the round's measured uniqueness
   (4,778,311 histories, spectrum {1: …}) recorded as the answer to
   the pin's highest-residual-risk flag.

**Verdict after repairs: the unit stands as written — (H2) [THEOREM
at two-actor delivery-free d42a scope], all three obligations
discharged, the consequence chain exactly the pin's.  With (H0) and
(H1) (D61) and (H2) (here), D44a's closure theorem is UNCONDITIONAL
at that scope and RESIDUE 1 IS CLOSED THERE.  The round is TERMINAL;
the embargo lifts to exactly the pin §3 chain and no wider.**
