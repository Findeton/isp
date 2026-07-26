# D60p — (H1): the exploratory probe, and a depth-free proof route that closes

**Status: ADVISORY PRE-PIN PROBE. NOT A PIN. NOT COMMITTED. NOT A
CAMPAIGN RESULT.**  Everything below is to be independently
re-verified before any pinned unit cites it.  Receipt:
`v10/code/d60p_h1_probe.py`; output `v10/data/d60p_h1_probe.out`.

Scope throughout: **d42a, DELIVERY-FREE, two actors** — D44b's
boundary.  Nothing here transfers to transport scope.

Labels used: **[EXACT]** = a mechanical gate in the receipt;
**[MEASURED]** = a finite-depth measurement, evidence only;
**[PROOF]** = an argument written out here in full, each step either a
direct reading of the committed layer's code or a stated induction;
**[GAP]** = named and open.

---

## 1. The target and the two dead routes

**(H1)** at d42a scope: for all histories `h, h'` of ANY depth,
`sigma(h) = sigma(h')` implies `menu(h) = menu(h')` as renamed
event-multisets with exact weights.  `sigma` is the D44a §2 full-view
abstraction (per-actor holdings pattern modulo base renaming, live
proposal structure with conflict components, superseded marks
restricted to referenced bases).

Two routes are dead and were **not re-walked**:

1. **D46a's `tau` / own-view route** — `tau` is not an own-view object;
   the menu view strictly exceeds the noop cone on 1,016/12,942
   actor-histories at depth ≤ 5, all excess opponent-authored.
2. **D51's wire-closure / monotonicity route** — view-monotonicity
   FAILS: `prop_options_in_view` excludes a base on which the actor
   already holds a live own proposal, so a view that MISSES that
   proposal INCLUDES the base.  A smaller view can yield MORE options.

The surviving asset (D51): the menu reads each candidate's own view
through exactly four projections, and `admissible(acts, e)` builds that
view from **the candidate event's own causal past**.

---

## 2. Result summary

**No counterexample.**  (H1) survived:

- an **exhaustive** sweep to **depth 8 — 930,631 histories**
  (layer census `[1, 6, 32, 176, 976, 5280, 27904, 145408, 750848]`);
  every history enumerated, `sigma` and the *committed* `canon_menu`
  computed for each, every one of the 36 sigma classes checked for menu
  agreement.  Zero splitting classes — **[MEASURED]**;
- **deterministic deep sampling to depth 40** (6,000 trajectories,
  240,000 history visits, seed `20260726` printed) checked against the
  running sigma → menu table.  Zero splits, zero new sigma values
  — **[MEASURED]**;
- the **widest own-view-lag pair** (span 6) and the **widest
  dead-structure pair** (span 2 superseded bases) the depth-6 family
  contains inside a single sigma class — identical menus — **[MEASURED]**;
- **opponent-renewal pumping** families: same-sigma histories of length
  up to **44**, differing by up to **20 buried renewal cycles**, in
  classes of up to 21 members — identical menus — **[MEASURED]**;
- five hand-built adversarial constructions aimed at the D51
  monotonicity failure — **[MEASURED]**.

**Proof status: the route closes, subject to one clearly-stated
induction.**  §3–§7 give a depth-free argument: the candidate view is
computed in closed form, the own-cone structure is shown rigid, and the
menu is exhibited as an **explicit finite formula `G` in sigma's own
recorded data**.  `G` is gated `[EXACT]` entrywise against the true menu
on every history to depth 8.  Given `G`, (H1) is immediate and **no
induction on depth appears**.  The single non-mechanical step is
Lemma 5 (§5), an induction **on history construction**; its case
analysis is written out here in full and each case is a reading of the
layer, but it has not been machine-checked as an induction — only its
conclusions have been gated exhaustively.  That is the honest residual
(§8).

---

## 3. [PROOF] The register geometry — Lemma 1

Read directly off the committed layer (`d42b3_placement_exact.py`):

```
def regs_of(op):
    if op[0] in ('p', 'n'): return frozenset([op[1]])
    props = {t[0] for t in op[2]}
    base = next(iter(op[2]))[1]
    return frozenset(props | {vname(base, op[3], op[1])})
```

So the *registers* are **actor names**, not bases: a `p` or `n` event
occupies the single register of its actor; an `r` event occupies the
registers of the **proposers of its ckey**, plus one fresh **version
register** `vname(base, W, a)` whose last component is the
**arbitrator**.  `event_poset` chains, per register, each event to the
previous event on that register and closes transitively.

**Lemma 1.**
(a) For every register `r`, the events occupying `r` form a **chain** in
the poset. *(Immediate: `pred[j] ⊇ pred[last[r]] ∪ {last[r]}`, and
`pred` is transitively closed.)*
(b) Every event occupies at least one **actor** register (`p`/`n`: its
actor; `r`: the proposers of a non-empty ckey).
(c) Write `cone_a(h)` for the past-cone the layer builds for the
candidate `('n', a)` — the downset of the register-`a` chain.  By (a),
`cone_a(h)` contains **every** event with `a` among its actors.
(d) Therefore **`cone_A(h) ∪ cone_B(h) = every event of h`.**
(e) A version register `vname(·,·,a)` is only ever created by an `r`
event **by `a`**, so it is never occupied by the opponent, and its cone
is contained in `cone_a(h)`.

**[EXACT]** gate S1: (a)–(d) hold with zero violations on the entire
depth-6 family (34,375 histories); (a), (c), (d) are re-gated on every
history to depth 8 (S4(c)).

---

## 4. [PROOF] The candidate-view dichotomy — Lemma 2, and the cone form

**Lemma 2 (the closed form for candidate views).**  For a candidate
event `e` by actor `a` appended to `h`, the view
`View(acts+[e], pred, pred[j])` that `admissible` builds has index set:

| candidate | view |
|---|---|
| `('n', a)` | `cone_a(h)` |
| `('p', a, b, x)` | `cone_a(h)` |
| `('r', a, C, W)` with `proposers(C) = {a}` (**self-arb**) | `cone_a(h)` |
| `('r', a, C, W)` with `proposers(C) = {A, B}` (**pair-arb**) | **the FULL view** |

*Proof.*  `regs_of` for `p`/`n` is `{a}`, so the view is the register-`a`
cone — note that **`b` and `x` do not enter `regs_of`**: a propose
candidate sees exactly what an idle sees.  For a self-arb, the registers
are `{a}` plus the fresh version register, whose cone is inside
`cone_a(h)` by Lemma 1(e).  For a pair-arb, the registers include both
actors, so the view contains `cone_A ∪ cone_B` = everything by Lemma
1(d).  Finally, an admitted `r` candidate always has `a ∈ proposers(C)`,
because `arb_components_in_view(view, a)` only returns components
containing an `a`-proposal and `triples()` records the proposer — a
ckey without `a` can never match, whatever the view.  **There is no
third case.** ∎

**Lemma 3 (the cone closed form).**  Let `P` be the **last pair-arb** of
`h`.  Then `cone_a(h) = {j : j ≤ P} ∪ {j > P : a ∈ actors(h_j)}`; with
no pair-arb at all, `cone_a(h) = {j : a ∈ actors(h_j)}`.

*Proof.*  `P` occupies both actor registers, so `pred[P]` contains
`cone_A ∪ cone_B` evaluated at `P`, i.e. every event before `P`.  After
`P`, the two actor chains share no register: `p`/`n` events carry only
their own actor's name, self-arbs carry their actor's name plus a
version register that Lemma 1(e) confines to that actor. ∎

**Consequence.**  *The entire own-view lag is exactly the opponent's
events after the last pair-arb* — which is precisely D46a's measured
finding ("all excess opponent-authored"), now derived rather than
observed.

**[EXACT]** gates S1 and S4(c): the candidate-view dichotomy and the
cone closed form hold with zero violations on all 34,375 depth-6
histories **and on every history to depth 8** — the dichotomy is checked
candidate-by-candidate, not inferred from `G`.

---

## 5. [PROOF] Own-cone rigidity — Lemma 4 and Lemma 5

**Lemma 4 (what the cone never misses).**
(a) `holdings(a)` computed on `cone_a(h)` equals `holdings(a)` computed
on the full view.  *(An arb contributes to `holdings(a)` only if
`a ∈ proposers`, and then it occupies register `a`, hence lies in
`cone_a` by Lemma 1(c).)*
(b) All of `a`'s own proposals lie in `cone_a(h)`.
(c) An `a`-proposal is resolved in `cone_a(h)` iff it is resolved in the
full view.  *(A resolving arb has `a ∈ proposers`, hence is in
`cone_a`.)*  **So `a`'s own live proposals are cone-invariant.**

**Lemma 5 (the one-token invariant).**  By induction on the construction
of an admissible history:

- **(5a)** `alive_a := holdings_{cone_a}(a) \ superseded_{cone_a}` is a
  **singleton** `{X_a(h)}`.
- **(5b)** `a` has **at most one live proposal**, and its base is `X_a`.
- **(5c)** At most one base held by *both* actors is non-superseded at
  any time; once either actor self-arbitrates it, **no pair-arb is ever
  admissible again** (the diverged sector).
- **(5d)** No opponent proposal is live in `cone_a(h)` on the base `X_a`.
- **(5e)** At most **one** actor can have `X_a` full-view-superseded.

*Proof.*  Base case `h = []`: `holdings = {V0}`, nothing superseded,
`alive = {V0}`, no proposals.  Step, by the appended event:

- `('n', x)`: nothing changes.
- `('p', x, b, y)`: admissibility requires `(b,y) ∈
  prop_options_in_view(cone_x, x)`, so `b ∈ alive_x = {X_x}` (5a) and
  `x` had no live proposal on `b`; by (5b) it had none at all, so now it
  has exactly one, on `X_x`.  Holdings and superseded are untouched.
- `('r', x, C, W)` **self**: `C` must be the triple-set of a component of
  `cone_x` containing an `x`-proposal.  By (5b)+(5d) the only live
  proposal available on a non-cone-superseded base is `x`'s own one on
  `X_x`, so `C = {(x, X_x, y)}` — a **singleton**.  Effect: `X_x` enters
  `superseded_{cone_x}`; `holdings_x` gains the fresh
  `v = vname(X_x, W, x)`, which nothing has superseded, so
  `alive_x = {v}`; `x`'s proposal is resolved, so `x` has 0 live.  For
  the opponent `y`: `holdings_y` is unchanged and the arb is **not** in
  `cone_y` (its registers are `x` and an `x`-only version), so
  `alive_y` is unchanged — this is the invisible supersession, and it is
  exactly the mechanism behind D51's monotonicity failure.
- `('r', x, C, W)` **pair**: the view is the full view (Lemma 2), so `C`
  is a full-view component with both actors' proposals on one base `b`;
  by (5b) `X_x = X_y = b`.  Effect: `b` is superseded in **both** cones
  (the pair-arb is in both, Lemma 1(c)), both actors gain
  `v = vname(b, W, x)`, both live proposals are resolved.  `alive = {v}`
  for both. ∎ *(for 5a, 5b)*

  *`alive_a` is never **empty**:* that would need `X_a` superseded
  **inside** `cone_a`, i.e. an arb on `X_a` lying in `cone_a`.  It is
  either `a`'s own (which mints a new version for `a` in the same step),
  or a pair-arb (likewise, for both), or an **opponent self-arb** — but
  an opponent self-arb occupies only `{y, v_y}`, so it can enter
  `cone_a` only behind a *later* pair-arb, and by (5c) no pair-arb can
  follow it.  So `alive_a` never empties.  *`alive_a` never exceeds
  one*, because every arb that adds a version to `holdings(a)` lies in
  `cone_a` and supersedes the previous alive base there.

*(5c)*: the only bases both actors hold are `V0` and the versions minted
by pair-arbs; each pair-arb supersedes the previous shared base, so at
most one is alive.  A self-arb by `y` on the shared base makes it
full-superseded, and a pair-arb requires a full-view component on a
**non-full-superseded** base with both proposers — impossible thereafter,
since no new shared base can be minted. ∎

*(5d)*: with no pair-arb, `cone_a` contains no opponent event at all
(Lemma 3).  With last pair-arb `P`, `X_a` is either `v_P` (minted by `P`)
or a later `a`-only version; opponent proposals on `v_P` occur after `P`
hence lie outside `cone_a`, and the opponent cannot propose on an
`a`-only version because it does not hold it. ∎

*(5e)*: `X_a` full-superseded but cone-alive requires a supersession
outside `cone_a`, i.e. a **self-arb by the opponent on a base `a`
holds** — necessarily the shared base, so `X_a = X_y` at that instant.
That very arb advances `X_y` to a `y`-only version, which only `y` can
ever supersede, always visibly.  And by (5c) no new shared base appears.
So the opponent's own token is never invisibly superseded afterwards. ∎

**Lemma 6 (the cone menu, in closed form).**  For each actor `a`:

- `prop_options_in_view(cone_a, a) = []` if `a` has a live proposal, and
  `[(X_a,0), (X_a,1)]` otherwise.  *(By 5a the only candidate base is
  `X_a`; by Lemma 4(c) "`a` has a live proposal on `X_a`" is a full-view
  fact; by 5b `a` has no other.)*
- `arb_components_in_view(cone_a, a) = []` if `a` has no live proposal,
  else exactly `[(X_a, {a`'s proposal`})]` — **one singleton component**
  (5b + 5d).
- Hence **`has_p` XOR `has_r`**, so the idle weight is the constant
  `1 - 1/4 = 3/4`; the self-arb weight is `(1/4)/1 · 1 = 1/4`; each
  propose weight is `(1/4)/2 = 1/8`.

> **This dissolves D51's MV2 obstruction rather than answering it.**
> MV2 correctly found that the cone-level `(has_p, has_r)` pair is *not*
> a function of the full-view pair — the fibre over `(False, False)`
> contains both `(False, True)` and `(True, False)`.  But those are the
> **only two** cone-level values that ever occur (D51's own printout
> confirms it), they are exactly the two complementary ones, and the
> idle weight `1 - ¼·has_p - ¼·has_r` cannot tell them apart.  The
> obstruction was real at the level of the 2-bit proxy and empty at the
> level of the menu.

**Lemma 7 (the full-view menu).**  `arb_components_in_view(full, a)` has
**at most one** element, because components are made of live proposals
and `a` has at most one (5b).  So the pair-arb weights are
`(1/4) · PK1(ckey, et)[W]` — the `1/|comps|` factor is always 1.
Moreover a size-2 component always carries exactly one conflict edge
(same base, opposite bits; and two same-base proposals by different
actors after the last pair-arb are always poset-incomparable, by Lemma
3), so `mis_of` returns the two singletons and `PK1` is `(1/2, 1/2)`.
**Every pair-arb weight is therefore `1/8`, and every "blind" group sums
to exactly `1/4`.**

> This **derives** d42b3's G-L2 quarter-quantization law, which that
> receipt could only gate and scope ("additivity for k ≥ 2 carried,
> untested").  At d42a scope `k ≤ 1` — a per-actor menu mass of exactly
> `1` or `5/4` and a total of `2`, `9/4` or `5/2`.  **[EXACT]** gate
> S3(d) confirms this on the whole family: propose weights `{1/8}`,
> self-arb `{1/4}`, pair-arb `{1/8}`, per-actor masses `{1, 5/4}`.

---

## 6. [EXACT] G — the menu as an explicit formula in sigma's data

Assembling Lemmas 2, 6 and 7, define `G(hold, live, comps, refs, sup)`
— reading **nothing** but `sigma_raw`'s output, no history, no poset,
no view:

```
for each actor a:
    L  = the live triple with proposer a           (at most one, 5b)
    X  = hold[a]            if hold[a] is not None
         L.base             elif L exists          (5b)
         EXTRA              otherwise              (dropped base)
    ('n', a)                       -> 3/4
    if L is None:
        ('p', a, X, 0), ('p', a, X, 1)   -> 1/8 each
    else:
        ('r', a, {L}, {L})                -> 1/4
        c = the full-view component carrying L, if its base is not
            in `sup`                              (at most one, L7)
        if c has two members:
            for W in mis_of(ckey(c), edges(c)):
                ('r', a, ckey(c), W)      -> 1/4 * PK1(ckey(c), edges(c))[W]
```

**[EXACT] S3:** `G(sigma_raw(h))` reproduces `menu(h)` **entrywise with
exact Fraction weights** on every history of the depth-6 family, and
**[EXACT] S4(b)** on every history to depth 8 — same event set, same
weights, zero mismatches.

**[EXACT] S3(b):** at most **one** base is mentioned by the menu but
dropped by `sigma`, and it is always `X_a` for the unique actor with
`hold[a] = None` and no live proposal (Lemma 5e).  So the single opaque
`EXTRA` token is forced and renaming it costs nothing.  *(Proof that it
is outside `refs`: `refs` = non-None holds ∪ live-carrying bases;
`X_a` is full-superseded so `hold[a] = None`; `hold[b] ≠ X_a`;
and `X_b ≠ X_a` after the opponent's self-arb, so no live proposal sits
on it.)*

---

## 7. [PROOF] (H1), depth-free

Suppose `sigma(h) = sigma(h')`.  By construction of `canon_sigma`, the
raw tuples `(hold, live, comps, refs, sup)` of `h` and `h'` correspond
under a base bijection `m`.  `G` only ever **copies base tokens from its
input**, so it is equivariant: `G(raw') = m(G(raw))`, with the single
`EXTRA` token mapped to `EXTRA`.  By §6, `menu(h) = G(raw)` and
`menu(h') = G(raw')`.  Hence the two menus are identical as renamed
event-multisets with exact weights. **∎ — and the argument mentions no
depth anywhere.**

**Corollary (H2).**  The same induction (Lemma 5's step analysis) writes
the effect of each event on `(hold, live, comps, refs, sup)` purely in
terms of that tuple and the renamed event, so `sigma(h+e)` is a function
of `(sigma(h), renamed e)`.  This matches D51's MV4 at the projection
level.  Stated as **[PROOF, sketch]** — the update table has not been
written out event-by-event here.

---

## 8. [GAP] What resisted, stated precisely

1. **Lemma 5 is not machine-checked as an induction.**  Its *conclusions*
   (5a)–(5e) are gated exhaustively — in full detail on the depth-6
   family (S2) and in lean form on **every history to depth 8** (S4(c),
   together with Lemmas 1–3) — and `G`, which depends on all of them, is
   gated to depth 8 (S4(b)).
   But the receipt verifies the invariants, not the inductive step.  A
   referee-grade version should mechanize the step: for every
   `(sigma-state, admissible event)` pair, check that the invariants are
   preserved — a **finite** check over the 36-state sigma space, not a
   depth sweep.  *This is the one thing standing between this note and a
   clean [THEOREM].*  It is a bounded, well-defined job.
2. **The `EXTRA`-token argument (§6, S3(b)) leans on Lemma 5e.**  If 5e
   failed, two dropped bases could appear and the canonical renaming
   would have a genuine choice.  5e is gated, not mechanized.
3. **Lemma 7's incomparability clause** ("two same-base proposals by
   different actors are always incomparable") is argued from Lemma 3;
   the corresponding counter `SG_VIOL['cmp']` in the committed d44a
   sigma port reads 0 family-wide, which is a gate, not the proof.
4. **Scope.**  Everything is delivery-free two-actor d42a.  Deliveries
   reopen the absorbing sector; more actors break "at most one shared
   base" (5c) and "at most one component per actor" (Lemma 7) is likely
   to survive but "pair-arb ⇒ full view" (Lemma 2) is **not**: with
   three actors, an arb over a two-actor component sees the union of two
   cones, not everything.  **The dichotomy of Lemma 2 is a two-actor
   fact and must not be quoted beyond it.**

---

## 9. The single most important insight

**The candidate's own view is not a general sub-view: at two-actor d42a
scope it is either the actor's register cone or the whole history, with
no third case** (Lemma 2) — because `regs_of` keys the event poset on
**actor names**, not on bases, and a pair-arb therefore occupies both
actor registers at once.  Both dead routes assumed the menu view was
some intermediate object that had to be tracked; it never is.  On the
cone the layer is rigid to the point of triviality (one alive base, at
most one live proposal, one component, `has_p` XOR `has_r`), and the
whole menu collapses to the six-line formula `G`.  The own-view lag is
real and unbounded, and it is **menu-invisible for the exact reason the
monotonicity failure suggested it would not be**: what the lagging actor
misses is never its own structure, and its own structure is all the cone
projections can see.

---

## 10. Receipts

- `v10/code/d60p_h1_probe.py` — PROBE-labelled, exact Fractions,
  deterministic (seed printed), layer + `sigma`/`canon_menu` ported by
  **text extraction** from the committed `d42b3` and `d44a` receipts.
- `v10/data/d60p_h1_probe.out` — full output, depths printed.
- Reproduce: `python3 v10/code/d60p_h1_probe.py 8 40` (deeper sweeps by
  raising the first argument; runtime roughly ×5 per extra level).
