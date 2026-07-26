# D62 — (H2) IS A THEOREM: the update table, written out

**Status:** RESULT, 2026-07-26.  Pin: `note-d62-h2-update-table-pin.md`
(STRICT, frozen before this note).  Parents: `note-d61-h1-closure-result.md`
((H1) [THEOREM]; (H0) fully discharged, clause 4 = **Lemma 7b**; D44a
left CONDITIONAL ON (H2) ALONE), the adopted proof note
`note-d60p-h1-probe.md` §3–§9 (Lemmas 1–7b, invariants 5a–5e, `ser()`,
the (H2) corollary with its **three obligations**), d44a's conditional
closure theorem, and the D61 round-1 hostile review
(`reviews/d61-round1-hostile-review.md`, BLOCKER 1's repair list —
where the three obligations were first named — MAJOR 2, MINOR 10).

Receipt: `v10/code/d62_h2_update_table_exact.py`; output
`v10/data/d62_h2_update_table_exact.out` (**24 PASS / 0 FAIL**, exit 0,
79 s, exact `Fraction`s where weights appear, byte-identical under
three `PYTHONHASHSEED`s at the anchored depth).

Labels: **[PROOF]** = written out here, each step either a direct
reading of the committed layer (source line quoted) or a named theorem
of D61; **[EXACT]** = a mechanical gate in the receipt; **[MEASURED]**
= a finite-depth measurement, evidence only; **[GAP]** = named and open.

**Scope, unchanged and non-negotiable: TWO-ACTOR, DELIVERY-FREE, d42a.**
Three actors and transport are out of scope and nothing here may be
quoted beyond it.

---

## 1. The theorem

> **(H2) [THEOREM, two-actor delivery-free d42a scope].**  For every
> history `h` of ANY depth and every event `e` admissible at `h`,
> `sigma(h + [e])` is a function of `(sigma(h), e renamed into
> sigma(h)'s token language)`.

Together with D61's results this closes the hypothesis set:

> **(H0)** discharged (D61: clauses 1–3 from Lemmas 4/5, clause 4 =
> Lemma 7b) + **(H1)** [THEOREM] (D61) + **(H2)** [THEOREM] (here)
> ⟹ **d44a's closure theorem is UNCONDITIONAL at two-actor
> delivery-free d42a scope**: the 36-state closure, the six-state
> chain and the Perron package hold **at every depth**;
> **residue 1 is CLOSED at that scope**; D49's root-free completion is
> unconditional at every depth there — still inside the stationary
> **form** (D50: the form remains a choice), still delivery-free.

What carries the theorem is **§4–§7 below**: five rows, each a reading
of the committed layer plus D61's invariants.  The receipt's gates are
**evidence for the rows and were never premises of them** — the D61
§4/§5 lesson, restated in the pin in advance: *a cache-gated table
check alone cannot close the depth gap.*  §9 says exactly which
sentence each gate does and does not buy.

---

## 2. What the table transforms

`sigma` is `canon_sigma`, the minimum over base bijections of `ser()`'s
serialisation.  Per D61 round-1 **MINOR 10** the serialised part is
**not** all of `sigma_raw`: the full superseded set is dead structure
`sigma` was designed to drop.  So the table's state — call it the
**serialised state** `Σ` — is exactly what `ser()` writes:

```
    def ser(hold, live, comps, refs, sup, m):
        return repr((tuple((a, m.get(hold[a])) for a in AB),
                     tuple(sorted(((t[0], m[t[1]], t[2]) for t in live), ...)),
                     tuple(sorted(((m[c[0]], c[1], c[2]) for c in comps), ...)),
                     tuple(sorted((m[b], b in sup) for b in refs))))
```

that is, in a **token language** `m : refs → {0, …, k−1}` (`k ≤ 2` at
this scope):

| field | content |
|---|---|
| `hold` | per actor, its token or `None` |
| `live` | the live-proposal triples `(proposer, token, bit)` |
| `comps` | the conflict components `(token, members, edges)` |
| `sup∣refs` | the superseded **flag** of each referenced token |

Three layer facts fix the meaning of the fields; each is a quoted line
of the committed source.

* **(F1)** `hold[a]` is the actor's own alive token, dropped to `None`
  when that token is full-view superseded:
  `hold[a] = X[a] if X[a] not in sup else None` (d44a `sigma_raw`),
  with `X[a] = own_alive(h, a)`, a **singleton** by invariant (5a).
* **(F2)** `refs = sorted({b for b in (hold['A'], hold['B']) if b is
  not None} | {t[1] for t in live}, key=repr)` — *held or
  live-carrying, nothing else*.
* **(F3)** the flags are `tuple(sorted((m[b], b in sup) for b in
  refs))` — the superseded set is consulted **only on `refs`**.

And three theorems of D61 fix its shape, at every depth:

* **(5a)** `alive_a` is a singleton `{X_a}`; **(5b)** each actor has at
  most one live proposal, and its base is `X_a`; **(5e)** at most one
  actor can have `X_a` full-view superseded.

> **The one structural claim the table must earn.**  `Σ` is a *lossy*
> projection of the history — dropped superseded marks are gone.  The
> table is legitimate only if **no row ever consults a dropped mark**.
> Rows R1–R4 below consult `sup` in exactly two places: the flag of a
> token in `refs` (present in `Σ` by F3) and the flag of the **one**
> token a dropped-base propose re-imports, which is **forced to
> `True`** by obligation O1.  Nothing else is read.  **[PROOF]**

The **renamed event** is `canon_pair`'s `ebest`: `e` under a bijection
`m` that attains `sigma(h)`, extended over any base of `e` outside
`refs` by `m2[extras[i]] = 100 + eperm[i]` (d44a), and minimised.

---

## 3. The layer lines the rows read

All quoted verbatim from `v10/code/d42b3_placement_exact.py`; the
receipt asserts each against the source (**[EXACT]** N0(c)/N0(d), 18
lines, 0 missing).

```
def vname(base, wkey, init):
    value = tuple(sorted({t[2] for t in wkey}))
    authors = tuple(sorted({t[0] for t in wkey}))
    return ('v', base, value, authors, init)          # (L1)

class View:
    ...
        for op in self.arbs.values():
            self.resolved |= set(op[2])                              # (L2)
            self.superseded.add(next(iter(op[2]))[1])                # (L3)
        self.live = {i: op for i, op in self.props.items()
                     if (op[1], op[2], op[3]) not in self.resolved}   # (L4)

    def holdings(self, a):
        h = {V0}
        for i, op in self.arbs.items():
            if a in {t[0] for t in op[2]}:                           # (L5)
                base = next(iter(op[2]))[1]
                h.add(vname(base, op[3], op[1]))                     # (L6)
        return h

    def edges(self, idx_set):
        ...
                if (pi[2] == pk[2] and pi[3] != pk[3]
                        and self.incomparable(i, k)):                # (L7)

def prop_options_in_view(view, a):
    for b in view.holdings(a):
        if b in view.superseded: continue                            # (L8)
        if any(op[1] == a and op[2] == b for op in view.live.values()):
            continue                                                 # (L9)
        for x in (0, 1): out.append((b, x))

def arb_components_in_view(view, a):
    for base, comp in view.components():
        if base in view.superseded: continue                         # (L10)
        if a in {view.props[i][1] for i in comp}:                    # (L11)
            out.append((base, comp))

def admissible(acts, e):
    ...
    comps = arb_components_in_view(view, a)                          # (L12)
    match = [c for c in comps if triples(view, c[1]) == ckey]        # (L13)
```

Two consequences used constantly, both from D61's adopted note:

* **Lemma 2 (the dichotomy).**  A candidate's own view is the
  initiator's register cone (`n`, `p`, self-arb) or the **full** view
  (pair-arb) — *no third case*.  The exclusion of the third case is
  (L11), `arb_components_in_view`'s **proposer test**: every *admitted*
  `'r'` has its initiator among the ckey's proposers.  (D61 round-1
  MAJOR 3: `regs_of` **creates** the third case; (L11) kills it.)
* **Lemma 1(c).**  `cone_a(h)` contains **every** event occupying
  register `a` — and by `regs_of`, an arb occupies the registers of its
  ckey's *proposers*.

---

## 4. Row 0 — `comps` is a function of `live` (obligation O3)

> **Row 0 [PROOF].**  `comps(Σ) = f(live)`, with
> `f`: group the live triples by base; a base carrying two triples with
> **opposite** bits yields one 2-member component with one edge; every
> other base yields one singleton component per triple.

*Proof.*  `components()` groups `view.live` by base and unions by
`edges()`.  By (5b) each actor has at most one live proposal, so at two
actors a base carries at most two, by **different** actors.  (L7) makes
an edge iff same base, opposite bits, **and incomparable** — and by
**Lemma 7b** (D61 round 1: two conflicting live proposals are *always*
poset-incomparable) the third conjunct is automatically true whenever
the first two are.  So the edge relation is decided by the bits alone,
and the union-find output is `f(live)`. ∎

This is exactly obligation **O3** — `comps(h+e)` is built from
`edges()`, which is built from `incomparable()`, i.e. from the poset
the serialised state does not carry.  Lemma 7b removes the poset from
the update.  **The table therefore never transports an order relation.**

**[EXACT] T1(d):** the layer's own `components()/edges()/incomparable()`
output equals `f(live)` at **all 34,375 states**, 0 failures.
**[EXACT] T4(e):** the same-bit branch is not vacuous — **2,236** states
carry two live proposals on one base with the same bit (two singleton
components on one base, no edge).

---

## 5. The update table

Write `x` for the event's actor, `y` for the opponent, `L_a` for `a`'s
unique live triple (5b), and `X_a` for `a`'s alive token:
`X_a = hold[a]` if that is not `None`, else `L_a`'s base if `L_a`
exists, else the **dropped token** (O1).  `v` denotes the fresh token
minted by an arb (O2).

| row | event | `hold` | `live` | `comps` | `refs` | `sup∣refs` |
|---|---|---|---|---|---|---|
| **R1** | `('n', x)` | — | — | — | — | — |
| **R2** | `('p', x, b, i)`, `b ∈ refs` | — | `+ (x, b, i)` | `f(live')` | — | — |
| **R2′** | `('p', x, b, i)`, `b ∉ refs` | — | `+ (x, b, i)` | `f(live')` | `+ b` | `b ↦ True` |
| **R3** | self-arb on `b` | `x ↦ v`; `y ↦ None` iff `hold[y] = b` | `− L_x` | `f(live')` | recomputed (F2) | `b ↦ True`, `v ↦ False` |
| **R4** | pair-arb on `b` | `A, B ↦ v` | `= ()` | `= ()` | `= {v}` | `v ↦ False` |

Rows are selected by `(event tag, base ∈ refs?, |proposers(ckey)|)` —
a partition, with no fall-through (**[EXACT] T4(a)**, 179,782
transitions, 0 unmatched, every row non-empty).

### R1 — idle, `('n', x)` [PROOF]

**Precondition:** none; `admissible` always returns `True` for `('n',
a)` (it only computes a weight).

**Effect: `sigma(h + [('n', x)]) = sigma(h)`, identically.**  `View`
builds `props` and `arbs` by the event tag, so an `'n'` enters
neither; `holdings` (L5/L6) and `superseded` (L3) read `arbs` only,
`live` (L4) reads `props` only, `components()` reads `live` only.
Appending an event does not change `pred[j]` for any earlier `j`, so no
existing comparability changes either.  Hence every field of
`sigma_raw` is untouched, `refs` is untouched, and the minimisation in
`canon_sigma` is over the same set. ∎

*(Row R1 is 68,750 of the 179,782 cached transitions — exactly
`2 × 34,375`, an idle by each actor at every history; the D61 round-1
review's 68,750 `(h, actor)` pairs.  **[EXACT] T4(b)**.)*

### R2 — propose on a held base, `('p', x, b, i)` with `b ∈ refs` [PROOF]

**Preconditions.**  `admissible` requires `(b, i) ∈
prop_options_in_view(cone_x, x)` (Lemma 2: a propose candidate's view
is the initiator's cone — `regs_of` of a `'p'` is `{x}`, so `b` and `i`
do **not** enter the view).  By (L8) `b` is a non-superseded holding of
`x` in `cone_x`, i.e. `b ∈ alive_x = {X_x}` by (5a), so **`b = X_x`**;
by (L9) `x` has no live proposal on `b` in `cone_x`, and by Lemma 4(c)
`x`'s own live proposals are cone-invariant, so by (5b) **`x` has no
live proposal at all**.  With `b ∈ refs` and `b = X_x`, (F1)+(F2) give
`hold[x] = b` (if `X_x` were superseded, `hold[x]` would be `None` and
`X_x ∉ refs` by O1 — that is row R2′).

**Effects.**  A `'p'` event adds nothing to `arbs`, so **`holdings`,
`superseded` and every `hold[·]` are unchanged** (L3/L5/L6), and
`sup∣refs` is unchanged.  It adds one entry to `props`, unresolved by
(L2)/(L4) — no arb can have resolved a triple that did not yet exist —
so `live' = live + (x, b, i)`.  `comps' = f(live')` by Row 0.  `refs`
is unchanged because `b` was already in it. ∎

**[EXACT] T4(c):** at all **57,020** R2 instances, the renamed base
equals `hold[x]` and `x` had no live triple; 0 violations.

### R2′ — propose on a **dropped** base, `b ∉ refs` [PROOF] (obligation O1)

**Preconditions.**  As in R2, `b = X_x` and `x` has no live proposal.
Here `b ∉ refs`, so by (F2) `b` is neither actor's `hold` and carries no
live triple.  By (F1) and (5a), `X_x ∉ refs` forces **`hold[x] = None`**,
i.e. `X_x ∈ sup`: `x`'s own token is alive in `cone_x` but superseded
in the full view.  This is the **invisible supersession** — the
opponent self-arbitrated the shared base and `x` cannot see it (Lemma
5's self-arb case) — and it is the single place where the table meets
a token `sigma(h)` does not record.

**The token is forced (O1).**  See §6.1.  In one line: by (5e) at most
one actor's token is full-superseded, so the dropped token is unique
and **its superseded flag is `True` by construction, computed rather
than read**; `canon_pair` renames it deterministically to `100`.

**Effects.**  Exactly R2's, plus: `refs' = refs ∪ {b}` (it is now
live-carrying, F2) and the new flag `b ↦ True`.  `hold` and every old
flag are unchanged (no arb was added). ∎

**[EXACT] T3(a):** at all **9,656** R2′ instances the discarded token
is exactly `own_alive(h, x)`, is in `sup`, is **not** in `refs`, is not
the opponent's hold, and carries no live proposal — 0 violations.
**[EXACT] T4(c):** every R2′ instance has `hold[x] = None`, no live
`x`-triple, and renamed base `100`.
**[MEASURED]** `9,656` is *exactly* the D61 round-1 review's count of
cone-extra propose options caused by **missed supersession** — the
dropped-base proposes **are** that excess, now identified as a row.

### R3 — self-arb, `('r', x, C, W)` with `proposers(C) = {x}` [PROOF]

**Preconditions.**  By Lemma 2 the view is `cone_x`.  (L12)/(L13)
require `C` to be the triple-set of a `cone_x` component containing an
`x`-proposal (L11), on a base not superseded **in `cone_x`** (L10).  By
(5b)+(5d) the only live proposal on such a base is `x`'s own one on
`X_x`, so **`C = {L_x}`, a singleton**, and `b = X_x`.  Note `b` may
nevertheless be in the **full-view** `sup` — that is the state R2′
creates — so the precondition is `hold[x] = b` **or**
(`hold[x] = None` and flag(`b`) `= True`).  `b ∈ refs` always, since it
carries `L_x` (F2).

**Effects, field by field.**

* `sup' = sup ∪ {b}` — (L3), the arb's base is superseded in every view
  containing it, and the full view contains it.
* `holdings_x` gains `v = vname(b, W, x)` — (L5)+(L6), since
  `x ∈ proposers(C)`.  `v ∉ sup'` by **O2** (§6.2: `v` is fresh, and
  `v ≠ b` because `b` is a proper component of the tuple `v`).  So
  `X_x(h+e) = v` and **`hold'[x] = v`** by (F1).
* **`hold'[y] = None` iff `hold[y] = b`, else unchanged.**  `y`'s own
  alive token `X_y` is untouched: the arb's registers are `{x}` and the
  version register `vname(·,·,x)`, which Lemma 1(e) confines to `x`, so
  the arb is **outside `cone_y`** — `holdings_y` and
  `superseded_{cone_y}` are unchanged.  But `hold` is the *full-view*
  test (F1), and `sup'` gained `b`: so `hold'[y] = None` exactly when
  `X_y = b`, i.e. when `hold[y] = b`.  *(If `hold[y]` was already
  `None` it stays `None`; and `hold[y] = None` together with
  `hold[x] = None` is excluded by (5e), so at most one of the two
  branches is live in any state.)*  **This entry is the whole
  invisible-supersession phenomenon, and it is expressible in tokens.**
* `live' = live \ C` — (L2)/(L4): the arb resolves **exactly** its ckey
  triples.  In particular an opponent proposal on the *same* base with
  the *same* bit is **not** resolved (no edge, hence a different
  component, hence not in `C`) and survives, now sitting on a base
  marked superseded.
* `comps' = f(live')` — Row 0.
* `refs'` by (F2), `sup∣refs'` from `sup'`: every token of `refs'` lies
  in `refs ∪ {v}` (hold' values are `v` or `hold[y]`; live' bases are
  old live bases), so **every flag needed is already in `Σ`** or is
  `v ↦ False`. ∎

**[EXACT] T4(c):** all **35,412** R3 instances have a singleton ckey of
the initiator's own live triple on its token, 0 violations.
**[EXACT] T4(e)** — every sub-branch occurs: `x` self-arbs a **held**
token 24,236 / a **dropped** token 11,176; the opponent's token is
dropped by the arb 14,772, of which **8,944** also leave the opponent a
live proposal **stranded on the now-superseded base**; opponent already
dropped 6,744; opponent wholly untouched 13,896.
**[MEASURED]** the 14,772 opponent-dropping self-arbs are *exactly*
D61's N2(c) count of **first-self-arb candidates** — as (5c) predicts:
a self-arb hits a base the opponent also holds precisely while the
shared base is still alive, i.e. exactly before the first self-arb.

### R4 — pair-arb, `('r', x, C, W)` with `proposers(C) = {A, B}` [PROOF]

**Preconditions.**  By Lemma 2 the view is the **full** view.  (L10)
forbids a superseded base, so `b ∉ sup` and by (5b) `b = X_A = X_B`,
whence `hold[A] = hold[B] = b` with flag `False`.  `C` is a full-view
component carrying **both** actors' live proposals; by (5b) each has at
most one, so `|C| = 2` and `C = {L_A, L_B}`, opposite bits (Row 0).

**Effects.**  `sup' = sup ∪ {b}` (L3).  Both actors are in
`proposers(C)`, so by (L5)/(L6) **both** gain `v = vname(b, W, x)`, and
the arb occupies both actor registers, so it lies in both cones
(Lemma 1(c)): `hold'[A] = hold'[B] = v`, fresh by O2.  (L2) resolves
both triples, and by (5b) there are no others: **`live' = ()`**, hence
`comps' = ()` (Row 0) and `refs' = {v}` (F2), with the single flag
`v ↦ False`. ∎

**[EXACT] T4(c):** all **8,944** R4 instances sit on a base that is both
actors' non-superseded token, with both live triples in the ckey.

---

## 6. The three obligations, discharged

### 6.1 O1 — the dropped-base token is forced [PROOF]

*Claim.*  In row R2′ the successor serialised state is determined by
`(Σ, e^m)` even though the event's base is a token `Σ` does not record.

*Proof.*  Let `hold[x] = None` and `x` have no live proposal; the
propose is on `b = X_x` (R2′'s precondition).  Then:

1. `X_x ∈ sup` — immediate from (F1) and `hold[x] = None`.
2. `X_x ∉ refs`.  By (F2) `refs` is holds ∪ live-carrying bases.
   `hold[x] = None`.  For the opponent: if `X_y = X_x` then *both*
   actors' tokens are full-superseded, contradicting **(5e)**; so
   `X_y ≠ X_x` and `hold[y] ≠ X_x`.  For live: every live triple's base
   is its proposer's `X` by **(5b)**; `x` has none, and `y`'s would sit
   on `X_y ≠ X_x`.  Hence no field of `Σ` mentions `X_x`. ∎
3. Therefore the successor's new flag is **computed, not read**: the
   re-imported token carries `True` because step 1 says so — the table
   never has to recall a mark it dropped.
4. Uniqueness of the token: by (5e) at most one actor's token is
   full-superseded, so at most **one** base can ever be re-imported
   this way, and `canon_pair`'s extension `100 + i` assigns it the
   single name `100` with no residual choice.  Everything else about
   it — that it is superseded, unheld, and distinct from every token in
   `refs` — is fixed by 1–3.  ∎

*(This is the §6/S3(b) argument of the adopted note, promoted from a
gate to a proof and localised to the row that consumes it.  Its premise
(5e) is one of Lemma 5's five invariants — a theorem of D61, gated
there at every history to depth 8 and re-gated here at every state:
**[EXACT] T3(c)**, 34,375 states, 0 violations.)*

### 6.2 O2 — a minted version name can never collide [PROOF]

*Claim.*  Let `e = ('r', x, C, W)` be **admissible** at `h`, on base
`b`, and let `v = vname(b, W, x)`.  Then `v` is not a base present in
`h`.  ("Present" = `{V0} ∪ {`the versions minted by `h`'s arbs`}` —
`candidates_for`'s own base set.)

*Proof.*  Suppose `v = b'` with `b'` present.  `V0 = ('v', 'v0')` is a
2-tuple and `vname` returns a 5-tuple (L1), so `b' ≠ V0`; hence `b'`
was minted by some arb `h[j] = ('r', x_j, C_j, W_j)`, i.e.
`b' = vname(b_j, W_j, x_j)`.  Tuple equality in (L1) forces, component
by component,

```
b_j = b,   values(W_j) = values(W),   authors(W_j) = authors(W),   x_j = x
```

— in particular **`h[j]` is an arb by `x` on the very base `b`**.  *(It
need not be the same event: `vname` keys on the **winner** `W`, not on
the ckey.  §6.2's witness below exhibits two distinct admissible arbs
minting one name.)*  Now let `V` be the view `admissible` builds for
`e`:

* **`e` a pair-arb.**  `V` is the full view (Lemma 2), which contains
  `h[j]`.
* **`e` a self-arb.**  `V` is `cone_x` (Lemma 2).  `h[j]` was itself
  admitted, so by the proposer test (L11) `x ∈ proposers(C_j)`, so by
  `regs_of` the event `h[j]` occupies register `x`, so by **Lemma
  1(c)** `h[j] ∈ cone_x = V`.

Either way `h[j] ∈ V`, so by (L3) `b ∈ V.superseded`, so (L10) skips
`b` in `arb_components_in_view(V, x)`, so `match` is empty at (L13) and
`admissible` **returns `False`** — contradicting admissibility. ∎

*Corollaries used by rows R3/R4:* `v ∉ sup` (`sup` consists of bases of
arbs in `h`, all present), `v ∉ refs`, and `v ≠ b` (`b` is a proper
component of the tuple `v`).  So the table's fresh token is genuinely
fresh and the successor's token count is right.

**[EXACT] T2(a)** the census, re-run: **44,356** admissible arbs at
every cached transition, **0** collisions — the D61 round-1 review's
number, reproduced.
**[EXACT] T2(b)** the *premise* gated adversarially: over a pool of
157,888 arb events drawn from the layer's own outputs (the arbs of `h`
and the arb candidates at every prefix of `h`), **49,964** would
re-mint a name already present in `h` — **11,584 of them are events
that are not in `h` at all** — and the committed `admissible()` refuses
**every one**: 0 admitted.
**[EXACT] T2(c)** the named witness, which shows the obligation is not
vacuous: at `h = [pA(v0,0), pB(v0,1)]` the self-arb `('r','A',{tA},
{tA})` and the pair-arb `('r','A',{tA,tB},{tA})` are **both
admissible** and mint the **same** name `('v', v0, (0,), ('A',), 'A')`.
Once either fires, the other is refused — the base is superseded in the
survivor's view.  *The collision is excluded by admissibility, not by
luck.*

### 6.3 O3 — incomparability feeding `comps` [PROOF]

Discharged in **Row 0** (§4) by **Lemma 7b**, which D61 round 1 proved
and D61 adopted as (H0)'s fourth clause.  Cited exactly where the
arb and propose rows rebuild `comps`.

---

## 7. Assembling: (H2) [PROOF]

Fix `h`, an admissible `e`, and a token language `m : refs(h) →
{0,…,k−1}`.  Extend `m` to `m'` by sending the minted base to a fresh
token (row R3/R4; legitimate by **O2**) or the re-imported dropped base
to `100` (row R2′; legitimate by **O1**).  `m'` restricted to
`refs(h+e)` is a bijection: `refs(h+e) ⊆ refs(h) ∪ {v} ∪ {X_x}`, and
the added token differs from all of `refs(h)` by O1/O2.

1. **Row correctness.**  §5 establishes, for each of the five rows,
   `Σ_{m'}(h + [e]) = F(Σ_m(h), e^{m'})` where `F` is the table.  Every
   step is (L1)–(L13) or one of (5a)–(5e), Lemma 1(c), Lemma 2, Lemma
   4, Lemma 7b — all theorems at **every depth**; **no step is an
   induction on depth and no step reads the history.**
2. **`F` is equivariant.**  `F` only *copies* tokens from its input,
   introduces one fresh token, and computes flags; it never inspects a
   token's identity.  So for any bijection `π` of tokens,
   `F(π·Σ, π·e) = π·F(Σ, e)`.
3. **Canonicalisation commutes.**  `canon_sigma(h+e)` is the minimum of
   `ser` over all bijections of `refs(h+e)`; the table takes the same
   minimum over relabellings of its own output.  With (2) the two
   minima agree.
4. **Well-definedness of the input.**  `canon_pair` picks `m` among the
   bijections attaining `sigma(h)` and minimises `e^{m'}`; the pair
   `(sigma(h), renamed e)` is therefore a coherent (state, event) pair
   in one token language.  If two histories give the same pair, (1)–(3)
   give the same `canon_sigma` successor.

Hence `sigma(h+e)` is a function of `(sigma(h), renamed e)`, at every
depth. **∎ — and the argument mentions no depth anywhere.**

---

## 8. Two corollaries the table hands over

* **The arbitration WINNER is invisible to `sigma`.**  Rows R3/R4 use
  `W` only through `vname(b, W, x)`, which the table abstracts to one
  fresh token.  So `sigma(h+e)` does not depend on `W` at all.
  **[EXACT] T1(e):** across the 52 `(sigma, ckey)` groups the receipt
  sees, **0** have split targets.  *(The `PK1` split moves menu weight
  between the two winners but never the successor state; no claim is
  made here about the chain's weights, only about its states.)*
* **Every pair-arb is a RENEWAL to the root state.**  Row R4 outputs
  `hold = {A: v, B: v}`, `live = ()`, `comps = ()`, `refs = {v}`,
  `flag(v) = False` — serialisation-identical to `sigma([])`.  D44a's
  renewal/pumping structure is thus a *row of the table*, not a
  measured coincidence.

---

## 9. The receipt: what each gate buys, and what none of them buys

`v10/code/d62_h2_update_table_exact.py` — **24 PASS / 0 FAIL**, exit 0,
79 s, family depth **6**, transitions into depth **7** (printed, no
silent cap; the depth is a CLI argument).  The TABLE is implemented as
one function reading **only** `(serialised sigma, renamed event)` — gated
**[EXACT] N0(e)**: its code names no history, poset, view or
enumerator, and calls only the committed `ser()`.

| gate | buys |
|---|---|
| **N0(a)–(f)** | single sources by text slice (the d61 idiom); **slice hygiene** — 0 `sys.exit`, 0 `check(`, 0 `print(` survive the three d44a slices (the d50 lesson); the 18 source lines the rows quote; the census `[1,6,32,176,976,5280,27904]` |
| **T1(a)** | the table equals the layer at all **179,782** cached transitions into depth 7 — string-identical serialisation, 0 mismatches |
| **T1(b)** | the anchors: **176** distinct `(sigma, renamed e)` keys and **36** states (d44a CG2's 160 + CG7c's 16; CG3a's traversed-edge count) |
| **T1(c)** | closure: 0 escapes from the reachable set |
| **T1(d)** | Row 0 at all 34,375 states |
| **T1(e)** | the `W`-blindness corollary |
| **T2(a)/(b)/(c)** | O2: census 44,356 / 0; the *premise* adversarially (49,964 colliding-name candidates, 0 admitted); the named witness |
| **T3(a)/(b)/(c)** | O1: forcedness at all 9,656 instances; no split within any `(sigma, e)` class; (5e) at every state |
| **T4(a)–(e)** | row coverage (a partition, 0 fall-through), the census anchors, the row preconditions at every instance, token discipline (no arb ever carries the extra token), sub-case non-vacuity |
| **T5** | the frontier-exhausted BFS on sigma-space: 36 states expanded, **176** edges, the table correct on **every abstract transition key**, key set identical to the cached sweep's |

> **What none of them buys.**  Every gate is finite-depth or
> quotient-level.  **T5 in particular is NOT an independent proof:** the
> BFS uses one representative per class, which is licensed *by* (H2),
> i.e. by the rows.  The theorem force is §4–§7.  This sentence is
> printed in the receipt itself, at the gate, because D61 over-promised
> the analogous point twice and the pin forbids a third time.

Falsifiability was checked, not assumed: **eleven mutants** — six of
the table's rows (including the invisible-supersession clause
`hold'[y] = None`, Row 0's bit test, O1's flag, O2's freshness) and
five of the gate predicates (R3's precondition, O1's forcedness, O2's
adversarial non-vacuity, (5e), the sub-case census) — each produce
`[FAIL]` on the gate that owns them, and on no other.  Output is
byte-identical under `PYTHONHASHSEED` 0/1/7.

---

## 10. Residues and scope

1. **Lean-grade mechanization** of the induction — unchanged from D61.
   Lemma 5 is still prose-over-code; (H2) inherits **exactly** the
   standing (H1) has, no better: the rows are proofs, the invariants
   they consume are theorems of the same style, and no machine has
   checked the induction *as* an induction.
2. **Three actors** — out of scope; the wall is Lemma 2's proposer test
   (L11) (D61 round 1: 5,904 admissible third-case views at depth ≤ 4).
   Rows R3/R4 are stated for two actors throughout: "the opponent" is a
   single actor, and (5c)/(5e) are two-actor facts.
3. **Transport / deliveries** — untouched, as always.
4. **The form is still a choice** (D50).  Closing residue 1 closes the
   *closure theorem*, not the selection of the stationary form.

**Quotation discipline.**  The D61 embargo lifts to exactly this:
(H2) is a theorem at two-actor delivery-free d42a scope; D44a's closure
theorem is unconditional **there**; residue 1 is closed **there**.
Nothing wider.  Paper 30/32 and book updates land **after** this unit's
hostile round, per campaign discipline.

## 11. Receipts

- `v10/code/d62_h2_update_table_exact.py` — exact `Fraction`s,
  deterministic, layers by text slice, depth printed.
- `v10/data/d62_h2_update_table_exact.out` — 24 PASS / 0 FAIL, exit 0.
- Reproduce: `python3 v10/code/d62_h2_update_table_exact.py`
  (optional argument = family depth; the anchors apply at 6).
