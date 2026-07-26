# D61 — ROUND 1 INDEPENDENT HOSTILE REVIEW

**Frozen:** 2026-07-26.
**Unit under review:** D61 "closing (H1)" — `note-d61-h1-closure-pin.md`
(§1–§3 + the §4 first-run amendment), `code/d61_h1_closure_exact.py` +
`data/d61_h1_closure_exact.out`, the **adopted proof note**
`note-d60p-h1-probe.md` §3–§7 with `code/d60p_h1_probe.py` +
`data/d60p_h1_probe.out`, LOG #450 / #451 / #452, and the consequence
text already carried in `THE-THEORY-SO-FAR.md` §B6.13 / §B6.13b / §B6.14
(`GREEN-UNREVIEWED`).
**Reviewer:** independent Opus 5 worker, no prior context,
recompute-not-trust. Every number below was produced by code I wrote for
this review and ran against the committed layers from the repo root;
scratch under `/private/tmp/claude-501/.../scratchpad/d61rev/`.
Calibration: `reviews/d54-round1-hostile-review.md` and
`reviews/batch-round1-d50-to-d60.md`.

**VERDICT: REVISE. 1 BLOCKER / 4 MAJOR / 10 MINOR / 3 NIT.**

**(H1) itself survives everything I threw at it, and then some.** I
re-implemented the d42a admission layer from scratch (DFS reachability
instead of the incremental `pred` union, BFS components instead of
union-find, maximal-independent-sets by extension-closure instead of the
subset-minimality filter, explicit permutation replay for `PK1`), checked
it against `d42b3` on all 6,471 histories to depth 5 — menus *with exact
`Fraction` weights* and posets, **zero mismatches**, and **zero
admissible-but-not-enumerated** events against a strictly wider candidate
surface — and then ran the adopted proof note's **entire lemma list** on
my own layer with my own `sigma`/menu canonicalisation, **exhaustively to
depth 8 — all 930,631 histories**, census
`[1, 6, 32, 176, 976, 5280, 27904, 145408, 750848]`. Lemma 1(a)(c)(d)(e),
Lemma 3's cone closed form, Lemma 2's dichotomy, Lemma 4(a)(c), Lemma 6,
Lemma 7, invariants **(5a)–(5e) including the three the receipts never
gate at that depth**, (H0)'s incomparability clause, the single-`EXTRA`
claim, the quarter law, `G` entrywise in exact `Fraction`s, (H1) **and**
(H2): **zero violations, every one.** My independent count lands on
**36 sigma states and 176 (H2) transition keys** — d44a's committed
CG3a/CG7 anchors exactly.

**The BLOCKER is not in the theorem.** It is the sentence the unit sells
the theorem with. **(H1) is now a theorem; "D44a's closure theorem is
UNCONDITIONAL" and "RESIDUE 1 IS CLOSED" are not.** D44a's conditional
assembly rests on *three* hypotheses; D61 discharges **(H1) and three of
(H0)'s four clauses**, and no more: (H2) is carried by a step the adopted
note itself labels
`[PROOF, sketch]` and by a depth-7 sweep, and (H0)'s fourth clause is
carried by a counter the adopted note itself calls "a gate, not the
proof". The pin's own justification for (H2) — "follows from N2 at
machine level" — points at a gate that the §4 amendment deleted. This is
precisely the move D44a's own round-1 F1 finding convicted, one unit
upstream.

---

## BLOCKER 1 — "D44a is UNCONDITIONAL / RESIDUE 1 IS CLOSED" is not delivered: (H2) is undischarged and (H0) has an undischarged clause

**Where.** Pin §2 ("D44a's closure theorem is UNCONDITIONAL there ((H0) is
the layer's gated invariants; (H2) follows from N2 at machine level);
residue 1 is CLOSED at that scope; D49's root-free completion is
unconditional at every depth"); receipt VERDICT block ("D44a
unconditional at this scope; RESIDUE 1 CLOSED here; D49
unconditional-at-depth here"); LOG #452 ("**(H2) via the committed CG2 +
the closed form; (H0) = the gated invariants** … **RESIDUE 1 … IS
CLOSED**"); book §B6.13's consequences blockquote and §B6.14's
"Unconditional at **all depths**".

**The defect, in three parts.**

**(a) (H2) is not discharged, and the pin's stated ground for it no
longer exists.** D44a §8 states the hypothesis set and is explicit that
"(H2) transition determinism … is **NOT a consequence of (H1)**", and its
conditional theorem consumes (H2) in both legs: step (i) ("a depth-D
history's sigma is reached from a depth-(D-1) sigma by one
**(H2)-determined** transition, and no transition leaves the closed set")
and step (ii) ("(H1)+(H2) give sigma-equal ⇒ equal per-candidate
(weight, class_t)-multisets"). Without (H2) at all depths there is no
36-state closure at all depths, hence no all-depth six-state chain, hence
no all-depth Perron package — i.e. no closure of residue 1.

The adopted proof note's only treatment of (H2) is §7's Corollary, which
says in its own words:

> "Stated as **[PROOF, sketch]** — the update table has not been written
> out event-by-event here."

The pin's §2 grounds (H2) on "N2 at machine level". Pin §1's N2 was
*"determinism: the abstract state of h+e is a function of (abstract
state of h, renamed event class) — exhaustive, zero exceptions"*. The §4
amendment killed that machine; **the delivered receipt has no determinism
gate at all** — its `N2` is the *invariants* gate (5a/5b/5e), and its N-
numbering silently differs from the pin's throughout (see MINOR 1). So
§2's parenthetical cites a gate that does not exist in the receipt it
justifies. And even as pinned it would not have sufficed: it was an
*exhaustive-cache* gate, i.e. finite depth.

LOG #452 and the book restate the ground as "the committed CG2 + the
closed form". Neither works. **CG2 is d44a's depth-6 exhaustive gate**
(CG7b extends it to depth 7) — finite depth, and extrapolating it is
exactly what d44a's F1 called "an extrapolation, not a theorem as
delivered". **And `G` cannot supply (H2)**: `G` maps `sigma_raw(h)` to
`menu(h)`; it says nothing whatever about `sigma(h+e)`. The two objects
have different codomains.

**(b) (H0)'s fourth clause is carried by a gate the adopted note itself
disowns.** (H0) has four clauses (d44a §8); the fourth is "conflicting
live pairs incomparable". The adopted proof note §8 GAP 3 says:

> "Lemma 7's incomparability clause … is argued from Lemma 3; the
> corresponding counter `SG_VIOL['cmp']` in the committed d44a sigma port
> reads 0 family-wide, **which is a gate, not the proof**."

To be fair to the unit: the adopted note **does** prove (H0)'s other
three clauses — clause 1 is (5a), clause 3 is (5b), and clause 2
(full-view non-superseded holdings inside `X_a`) is a one-line corollary,
since every arb contributing to `holdings(a)` lies in `cone_a` and
`sup ⊇ sup_{cone_a}`. Only clause 4 is left standing on a counter. But
the pin's "(H0) is the layer's gated invariants" treats **gating** as
discharge for all four — the move D44a §8 explicitly forbids ("that
verification is EVIDENCE for the hypothesis, **never a premise of this
argument**").

**(c) Consequently the D49/§B6.14 line is over-stated too.** "D49's
root-free completion is unconditional at every depth" and "`Zhat` holds
at **every depth**" inherit (H2) through d44a's step (i).

**My recomputation** (`d61rev/lean8.py`, my own layer and my own
canonicalisation, exhaustive, memory-free DFS):

```
visited by depth {0:1, 1:6, 2:32, 3:176, 4:976, 5:5280, 6:27904,
                  7:145408, 8:750848}          total 930,631   (DEPTH 8)
(H1)  canonical sigma -> canonical menu :  36 sigma states,   0 splits
(H2)  (canonical sigma, renamed event)  -> 176 keys,          0 violations
(H0) clause 4 (conflicting live pairs incomparable)  :        0 violations
```

So both hypotheses are *true* on everything I can reach — **one level
deeper than either receipt gates (H2), under code that shares nothing with
them**. That is still evidence, and it is the same *kind* of standing they
had before D61 ran. Depth 9 is 4.7 M histories and depth ∞ is the claim.

**What is repairable, and how.**

*(H0) clause 4 is a three-line proof and should simply be written into
the note* (I checked each step against the layer):

> Let `i` be a live `A`-proposal and `k` a live `B`-proposal on the same
> base with opposite bits, `i < k`. Suppose `i ∈ pred[k]`. `pred[k]` is
> `cone_B` at time `k`, so by Lemma 3 `i ≤ P`, the last pair-arb before
> `k`. A pair-arb's `ckey` is a full-view component carrying a proposal
> by *each* actor; by (5b) `A` has at most one live proposal, and `i` —
> live at `k > P` — is live at `P`; so `A`'s proposal in `P`'s `ckey`
> **is** `i`, and `P` resolves it. That contradicts `i` live at `k`.
> Hence `i ∉ pred[k]`, and `k ∉ pred[i]` since `k > i`. ∎

*(H2) needs its update table written out*, per event class, on
`(hold, live, comps, refs, sup)`. It is writable — the four cases are the
same four — but it carries **three obligations neither note states**, and
a table that skips them is not a proof:

1. **The propose-on-a-dropped-base case.** When `hold[x] = None` and `x`
   has no live proposal, `X_x` is the base `sigma(h)` **discarded**; a
   propose on it makes `sigma(h+e)` reference a base `sigma(h)` does not
   record. Determinism survives only because that token is forced up to
   renaming (the §6 S3(b) argument, itself resting on 5e — which is
   gated to depth 6 only, MAJOR 1).
2. **Fresh-version-name non-collision.** Each arb mints
   `vname(b, W, x) = ('v', b, values(W), authors(W), x)` and the update
   table must produce a *new* base token. If that name ever coincided
   with a base already present, `sigma(h+e)` would carry fewer distinct
   tokens than the table predicts and determinism would break. It cannot
   (a collision forces `x` to have arbitrated `b` before, hence
   `b ∈ superseded` in `cone_x`, hence the arb inadmissible) — but that
   argument appears nowhere, and the gate does not exist either. I ran it:
   **44,356 admissible arbs to depth 6, 0 collisions.**
3. **(H0) clause 4**, because `comps(h+e)` is built from `edges()`, which
   is built from `incomparable()`.

**Until both land, the honest verdict line is:** *(H1) is a THEOREM at
two-actor delivery-free d42a scope. D44a's closure theorem remains
CONDITIONAL on (H0)-clause-4 and (H2), each verified exhaustively through
depth 7. Residue 1 is decided at every verified depth and its last named
gap has shrunk from three hypotheses to two.* That is still the largest
single step the residue-1 line has taken; it is not closure.

---

## MAJOR 1 — (5c) and (5d), the two invariants the induction's hardest step actually consumes, are gated NOWHERE; and (5c)'s prose proof does not cover its own statement

**Where.** Adopted note §5 (Lemma 5); D61 receipt N2/N3; probe S2/S4(c).

Lemma 5's step consumes (5c) and (5d) **by name**:

* the self-arb case: *"By **(5b)+(5d)** the only live proposal available on
  a non-cone-superseded base is `x`'s own one on `X_x`"*;
* the `alive_a`-never-empty argument: *"an opponent self-arb … can enter
  `cone_a` only behind a later pair-arb, and **by (5c)** no pair-arb can
  follow it."*

Neither is gated anywhere in the unit. D61's N2 covers 5a, 5b, 5e only.
The probe's S2 has no (5c) test at all, and its (5d) coverage is partial:
S2.5 checks that `arb_components_in_view(cone_a, a)` is the one singleton
`{a`'s proposal`}`, which catches an *opposite-bit* opponent proposal on
`X_a` (it would fuse into the component) but **not a same-bit one** —
same-bit proposals carry no conflict edge, form their own component, and
`arb_components_in_view(·, a)` never returns it. So the (5d) that
Lemma 5 cites is not the (5d) the receipts check.

**And (5c)'s own proof does not cover (5c)'s own statement.** The claim is
"once **either actor self-arbitrates**, no pair-arb is ever admissible
again". The proof handles only *"A self-arb by `y` on **the shared
base**"*. The missing step — that the *first* self-arb of any history is
necessarily on the shared base, because before any self-arb `X_A = X_B`
(the only shared bases are `V0` and pair-arb versions, and each pair-arb
advances both) — is derivable from the same paragraph but is not written.
I checked the missing step holds: **3,252 first-self-arb instances to
depth 6, and in every one `X_A = X_B` immediately before it and the arb
sits on that shared base — 0 exceptions.** Since (5c) is the sole reason
`alive_a` never empties, and `alive_a` a singleton is 5a, which is the
root of everything else, this is the load-bearing gap in the induction's
prose.

**Related.** (5e) is gated at **depth ≤ 6 only**. The probe's deep loop
(S4(c)) re-gates `D-S1.1 / D-S1.3 / D-S1.4 / D-S2.2/2.3 / D-S2.3 /
D-S2.7 / D-S2.5/2.8` and **omits `S2.9` and `S2.10`** — the `hold = None`
clauses that *are* 5e. Yet the adopted note says twice (§5's [EXACT]
line, §8 GAP 1) that (5a)–(5e) are gated "in lean form on **every history
to depth 8** (S4(c))". For 5e that is false, and 5c/5d are not in either
gate set.

**My recomputation** — all three, exhaustively and adversarially:

```
exhaustive depth 8 (930,631 histories, my layer):
   (5c)  histories containing a self-arb whose menu offers an admissible pair-arb :  0
   (5c)  histories containing a pair-arb positioned after a self-arb              :  0
   (5d)  opponent proposal live in cone_a on X_a                                  :  0
   (5e)  both actors' X full-view-superseded at once                              :  0

targeted post-self-arb families (5 forced self-arb/pair-arb prefixes,
each expanded exhaustively 5 further levels):
   post-self-arb histories                     18,409
   admissible pair-arb candidates found in them      0

deep walks, three policies (uniform / weight-biased / arb-greedy), two seeds:
   120 trajectories x depth  60 -->  7,320 history visits
   150 trajectories x depth 120 --> 18,150 history visits
0 violations of any of 5a, 5b, 5c, 5d, 5e, the dichotomy, Lemma 3,
Lemma 4, the XOR, Lemma 7, the single-EXTRA claim or the quarter law —
at histories fifteen levels past any exhaustive reach.
```

So (5c)/(5d)/(5e) hold. The finding is that the unit whose one job was
"mechanise Lemma 5's inductive step" gates neither of the two invariants
that step cites by name, and states depth-8 coverage it does not have.

---

## MAJOR 2 — the probe's depth-8 `G` gate is structurally blind to exactly the failure mode the `EXTRA`-token argument guards against

**Where.** Probe S4(b) ("`G` STAYS EXACT AT DEPTH 8 — the predictor is
not a shallow-depth coincidence", `deep G mismatches = 0`); quoted as
"menu = G(sigma) gated entrywise on 930,631 histories" in pin §1, LOG
#450 and book §B6.13.

`observed_menu(h, menu, refs)` maps **every** base outside `refs` to the
single token `EXTRA-BASE`; `G` likewise emits one `EXTRA` per
hold-`None`-and-no-live actor. If a state ever had **two** dropped bases
(one per actor — the 5e failure), the true menu's two distinct bases and
`G`'s two copies of one token land in *different* dict entries (they
differ in the actor field), so the two sides agree entrywise while
describing different objects. The `> 1 extra` guard is `S3(b)`, and
`S3(b)` runs **only over `FAM`, i.e. depth ≤ 6**; the deep loop never
re-checks `len(extras)`.

**Certificate** (`d61rev/extramask.py`, loading the probe's own `G` and
`observed_menu` unmodified):

```
raw = (hold={'A': None, 'B': None}, live=(), comps=(), refs=(), sup={b1, b2})
true menu:  ('p','A',b1,0/1) 1/8   ('p','B',b2,0/1) 1/8   ('n',·) 3/4
dropped bases in the true menu: 2
observed_menu(...) == G(raw)?  True     <- the depth-8 gate's predicate
   both sides say both actors propose on the SAME base: [('EXTRA-BASE',)]
   the true menu has TWO distinct bases:  [('v','b1'), ('v','b2')]
deep-loop `len(extras)` check present?  False
```

**What is honestly gated at depth 8** is `S4`'s `canon_menu` split check —
`canon_menu` renames extras to `100+i` and *does* distinguish two of them.
So (H1)'s depth-8 evidence stands. What does not stand is the sentence
"`G` is gated entrywise on 930,631 histories" as a claim about `G`: at
depths 7–8 it is gated *modulo the extras collapse*, and 5e — the reason
the collapse is safe — is not gated there at all (MAJOR 1).

**I supplied the missing gate.** My depth-8 sweep counts dropped bases
explicitly *before* substituting the token, and checks 5e directly:
**930,631 histories, `|extras| > 1` in 0, both-`hold = None` in 0**, with
`G` compared entrywise against the true menu on the real base names.
So the conclusion is sound at depth 8; the receipt just cannot see it.

---

## MAJOR 3 — §9's "single most important insight" attributes the dichotomy to the wrong mechanism: `regs_of` **produces** the third case; `admissible` kills it

**Where.** Adopted note §9 ("*because* `regs_of` keys the event poset on
**actor names**, not on bases"); reproduced as the engine blockquote in
book §B6.13 ("The reason is register geometry read from the committed
source: `regs_of` keys the poset on **actor names** … so a *pair*
arbitration occupies both actors' registers and therefore sees
everything, while **every other candidate sees exactly its initiator's
cone**").

`regs_of(('r', a, C, W))` returns `proposers(C) ∪ {vname(base, W, a)}` —
the **ckey's** proposers, which need not contain the initiator `a`. For
such a candidate the view is `cone_{opponent} ∪ (a`'s version cone`)`:
**neither the initiator's cone nor the full view**. Register geometry
alone therefore gives *three* cases, not two. The dichotomy is restored
only by the *last* sentence of Lemma 2's proof — `admissible` reaches the
`ckey` through `arb_components_in_view(view, a)`, which filters
components containing an `a`-proposal, so an admitted `'r'` always has
`a ∈ proposers(C)`. Lemma 2's proof gets this right; §9 and the book
blockquote get it exactly backwards, naming the mechanism that *creates*
the third case as the one that excludes it.

**My recomputation** (`d61rev/thirdview.py`, depth ≤ 5):

```
initiator-not-proposer 'r' candidates tested            6,484
  views that are NEITHER cone_a NOR the full view       5,712
  of them ADMISSIBLE                                        0
witness:  h = [ ('n','B'), ('n','B'), ('n','B'), ('n','B'), ('p','A',v0,1) ]
          e = ('r','B', {('A',v0,1)}, {('A',v0,1)})
          view [4]   initiator cone (B) [0,1,2,3]   full [0,1,2,3,4]
```

The correct one-liner is: *the dichotomy is a theorem of `regs_of`
**together with** `arb_components_in_view`'s proposer test* — and that
matters, because the proposer test is exactly the clause a three-actor or
transport-scope extension would have to re-examine.

---

## MAJOR 4 — the adopted proof note imports D51's refuted mechanism (batch-round BLOCKER 2), and the pin's immunity sentence names only the inversion

**Where.** Pin §1 ("D51 … whose batch-round **inversion** finding does not
touch this route"); adopted note **§1 route 2**.

The pin's immunity claim covers batch-round **BLOCKER 1** (the
projections-refine-`sigma` inversion) and is **correct**: D61 loads
`sigma` and `canon_menu` by text slice from the committed d44a receipt
and never touches D51's `projections()`. I verified this by reading and
by reproducing 36 states / 176 keys with my own canonicalisation. But the
pin is silent on batch-round **BLOCKER 2**, which *does* touch this route,
because the adopted note restates it verbatim as its reason for killing
route 2:

> "`prop_options_in_view` excludes a base on which the actor already holds
> a live own proposal, so a view that MISSES that proposal INCLUDES the
> base. A smaller view can yield MORE options."

The batch round proved that mechanism cannot fire (an actor's own live
proposals are always in its own cone). **My independent recomputation**
(`d61rev/d51clause.py`, depth ≤ 6, 68,750 `(h, actor)` pairs):

```
popts(cone) vs popts(full):  equal 63,922   cone STRICTLY MORE 4,828   cone fewer 0
  of the 9,656 cone-extra options:
     reason = MISSED SUPERSESSION      9,656
     reason = missed OWN proposal          0
actor's own live proposals differ between cone and full view:  0 / 68,750
```

The note is **self-contradictory** on this: §5 gets the mechanism right
("this is the invisible supersession, and it is exactly the mechanism
behind D51's monotonicity failure"), §1 gets it wrong. The *conclusion*
("a smaller view can yield more options") is true and is all the probe's
docstring and book §B6.13b assert — so the surviving-content sentences
are fine. What is not fine is that §1, the paragraph a referee reads to
learn *why* route 2 died, is the refuted clause, sitting inside the
artifact D61 adopts as its proof note, one unit after the batch round
struck it from D51. The pin's immunity sentence should name both
blockers and dispose of each separately.

---

## MINOR 1 — the pin's §1 N-programme is left standing after §4 deleted it, and §2 depends on the deleted numbering

Pin §1 still commits N1 (invariants), N2 (determinism), N3 (frontier-
exhausted BFS closure), N4 (the step per reachable pair), N5 (menu law),
N6 (quarter law). The delivered receipt has N0 (anchors), N1
(code-facts), N2 (invariants), N3 (cases + dichotomy), N4 (the
conclusion), N5 (quarter law). **The pin's N2, N3 and N4 were not
delivered at all** — no determinism gate, no abstract-state BFS, no
per-transition step check — and §4 says so obliquely ("run 1's
hand-rolled abstract state was COARSER than sigma") without ever
retracting §1's list or renumbering §2. A reader of §1 will believe
determinism and a frontier-exhausted closure were gated. They were not,
and §2's load-bearing consequence sentence cites the vanished N2
(BLOCKER 1a).

## MINOR 2 — three theorem-passes and two label overreaches in the receipt

* **N0** is `callable(canon_sigma) and callable(canon_menu)` — a smoke
  test presented as an anchor gate (D51 MINOR 5's class).
* **N3(d)** counts menu events with `e[0] not in ('p','r','n')`.
  `candidates_for` constructs only `('p',…)`, `('r',…)`, `('n',a)`;
  the counter **cannot be non-zero**. Presented as "CASE
  EXHAUSTIVENESS … the case split covers the alphabet" and repeated as a
  table row in book §B6.13.
* **N1** asserts three substrings against the committed source:
  `"def regs_of(op):"`, `"if op[0] in ('p', 'n'): return frozenset([op[1]])"`,
  `"props = {t[0] for t in op[2]}"`. It does **not** assert the
  `vname(base, op[3], op[1])` line or the `return frozenset(props | {…})`
  line — i.e. it does not gate the *version-register* half — while its
  label claims it gates "`{proposers} u {fresh vname}` … arbitrator-owned
  version names, **which is the entire basis of the dichotomy**".
* **N5**'s label says "the quarter law **as the closed form `G` derives
  it** (probe §6)". The receipt never evaluates `G` (see MINOR 7); N5 is
  a direct per-actor mass census.

## MINOR 3 — N4's anchor is `>= 30` where the committed anchor is exactly 36

`h1_bad == 0 and len(by_sig) >= 30`. d44a's SG1 gates `NSIG == 36` **and**
the window spectrum `[11, 19, 28, 32, 36]`. A `sigma` port that
coarsened to 30–35 states would pass D61's N4 silently while breaking the
object the theorem is about. Same class as D54 MINOR 5 / d44a F4.

## MINOR 4 — "a total of 2, 9/4 or 5/2" (adopted note §5, Lemma 7): 9/4 is unreachable

A per-actor mass of `5/4` requires a **two-member** full-view component,
which by (5b) contains *both* actors' unique live proposals — so both
actors are at `5/4` together or neither is. The total is always `2` or
`5/2`. Measured at depth ≤ 6:

```
per-actor mass  {1: 64,278,  5/4: 4,472}
TOTAL menu mass {2: 32,139,  5/2: 2,236}      (= 4,472 / 2)
```

The probe's own S3(d) prints `totals = ['2', '5/2']` and its gate is
`set(totsum) <= {2, 9/4, 5/2}`, so the receipt disproves the sentence in
its own output and the `<=` gate never notices. (Damage is contained: the
`9/4` never reached the book — §B2.7 and §B6.13 quote only the per-actor
`{1, 5/4}`.)

## MINOR 5 — the case battery is one level shallower than the invariant gate

N2 runs over all 34,375 histories; N3(a)–(e) run over `h` with
`len(h) < CAP`, i.e. **parents of depth ≤ 5** (6,471 of them, 34,374
candidates). The deepest cached level contributes zero case instances.
"at every cached instance" (receipt banner, pin §4(i), LOG #452, book) is
accurate only for transitions; it should read "at every cached
transition (parents to depth 5)". Book §B6.13 already says "depth ≤ 5"
for the dichotomy while the surrounding text says depth 6 — correct, but
it reads as an inconsistency rather than a scope statement.

## MINOR 6 — the case battery gates the case split's PRECONDITIONS, not the step's CONCLUSIONS

N3(a)/(b)/(c) each check a property of the *appended event relative to
`state_of(h)`* — that a propose is on `X_a`, that a self-arb's `ckey` is
a singleton on `X_a`, that a pair-arb's base is `X_A = X_B`. Those are the
case split's *hypotheses*. None of Lemma 5's asserted *effects* is
checked: the self-arb case's "the arb is **not** in `cone_y`, so
`alive_y` is unchanged" (the invisible supersession — the single most
delicate claim in the note), or the pair-arb case's "`b` is superseded in
**both** cones, both actors gain `v`, both live proposals are resolved,
`alive = {v}` for both". Invariant *preservation* across cached edges does
follow — from N2 holding at every `h`, including every `h+e` in the
cache — but the receipt never says that is the argument, and the pin's
§4(i) wording ("every CASE CLAIM of Lemma 5's step") promises more than
the preconditions.

## MINOR 7 — D61 adopts an artifact whose own banner forbids adoption without re-verification, and re-verifies only part of it

`d60p_h1_probe.py`'s banner:

> ">>> PROBE / ADVISORY. NOT A PIN, NOT A RECEIPT, NOT COMMITTED. <<<
> >>> Every result here is to be **independently re-verified before any
> pinned unit cites it**. Nothing below may be quoted as a campaign
> result."

D61's receipt does not evaluate `G`, does not re-run S3, S3(b), S3(d),
S4, S4(b), S4(c), S5a, S5b or S5c, and does not invoke the probe at all.
`[PROBE-CARRIED]` is a citation label, not the re-verification the probe
demanded. The re-verification is supplied by this review (see "Checked
and CLEAN"), and it passes — but a pinned unit should not have shipped
its central object (`G`, and the depth-8 numbers) carried by an
explicitly non-citable advisory file.

## MINOR 8 — falsifier-protocol mismatch: any gate failure exits 1

Pin §3: "Any N-gate failure is the deliverable (**exit 0 for substantive
negatives**; exit 1 only on anchor breakage)". The receipt's docstring
repeats "Exit 1 only on anchor breakage". Its last line is
`sys.exit(1 if FAIL else 0)` — every `[FAIL]`, substantive or not, exits
1. Either the protocol or the code must move.

## MINOR 9 — the three-actor scope wall is asserted five times and exhibited nowhere

Pin §3, adopted note §8.4 and §9, LOG #450/#452 and book §B6.13 clause 3
all assert that the dichotomy fails at three actors. No file in the unit
constructs a three-actor history. I did (`d61rev/threeactor.py`, my
re-implemented layer run with actors `('A','B','C')`, depth ≤ 4, 6,589
histories):

```
candidate views:  cone 50,877   full 4,296   THIRD CASE 5,904   <- ADMISSIBLE
witness  h = [ ('n','C'), ('n','C'), ('p','B',v0,1), ('p','A',v0,0) ]
         e = ('r','A', {('B',v0,1), ('A',v0,0)}, {('B',v0,1)})
         view [2,3]    initiator cone (A) [3]    full [0,1,2,3]
three-actor status of the OTHER invariants: 5a 0, 5b 0, has_p-XOR-has_r 0,
     Lemma 7 (<=1 full component per actor) 0   -- all still hold at depth 4
```

The wall is real and is **exactly** where §8.4 says: an arb over a
two-actor component sees the union of two cones. The exhibit also sharpens
the scope statement — at three actors it is *only* Lemma 2 that breaks;
the rigidity invariants survive to depth 4. That is worth recording,
because it tells the successor unit which lemma to attack.

## MINOR 10 — §7's equivariance premise is stronger than `canon_sigma` delivers: `sigma` does not serialise all of `sigma_raw`

§7 opens: *"By construction of `canon_sigma`, the raw tuples
`(hold, live, comps, refs, sup)` of `h` and `h'` **correspond under a base
bijection `m`**"*. They do not. `ser()` serialises
`hold`, `live`, `comps`, and `sup` **only restricted to `refs`**
(`tuple(sorted((m[b], b in sup) for b in refs))`). The full superseded set
is the dead structure `sigma` was *designed* to drop, so equal `sigma`
does **not** give a bijection of the raw tuples.

```
depth <= 6, 34,375 histories, 36 sigma classes:
  classes containing members with DIFFERENT |sup|              28 of 36
  |sup \ refs| spectrum across the family                      {0, 1, 2, 3}
```

The step is nevertheless sound, by an observation the note never makes:
**`G` reads `sup` at exactly one place** — `c[0] not in sup`, where
`c[0]` is the base of a live proposal and therefore *in* `refs`. So `G`
factors through the serialised part. One clause fixes §7; as written its
premise is contradicted by 28 of its own 36 classes.

## NIT 1 — no result note

The theorem statement, its scope clauses and its consequences live in a
`print()` block, a LOG entry and a pin *amendment*. D51 NIT 1's class, and
the consequences already reached the book from there.

## NIT 2 — N4's split detector compares against the previous member, not a representative

`by_sig[sg] = cm` overwrites on every history. It is sound (a class whose
members are not all equal must have some consecutive unequal pair in
iteration order), but that is not obvious on the page, and the natural
reading — "compared against the class's menu" — is not what the code does.

## NIT 3 — the `#450`/`#452` LOG entries quote the dichotomy census at "depth ≤ 5" and the family at "34,375"

Both correct (34,374 candidates from parents of depth ≤ 5; 34,375
histories of depth ≤ 6) but placed adjacently without the distinction,
which is what produced MINOR 5's ambiguity in the book.

---

## Checked and CLEAN

* **Receipt rerun:** `10 PASS / 0 FAIL`, exit 0, 27 s; **identical to the
  committed `.out`** except the harness's trailing `RC=0` line; **byte-
  identical output under `PYTHONHASHSEED` 0 / 7 / 12345** (md5
  `d824d218…` all three) — which matters here, because the layer uses
  `next(iter(frozenset))` and `sorted(…, key=repr)` in load-bearing
  places.
* **Probe rerun** at `MAXDEPTH = 7`, `SAMPLE_DEPTH = 20`:
  `14 PASS / 0 FAIL`, 4 min 34 s, all gate texts reproduced.
* **The layer, independently re-implemented** (different reachability,
  different component algorithm, different MIS characterisation): agrees
  with `d42b3` on all **6,471** histories to depth 5 — **0 menu-event
  mismatches, 0 exact-`Fraction` weight mismatches, 0 poset mismatches**.
  Against a **strictly wider candidate surface** (all subsets of *all*
  live proposals regardless of base, plus every base ever named):
  **0 admissible-but-not-enumerated** events.
* **Census reproduced from scratch:** `[1, 6, 32, 176, 976, 5280, 27904,
  145408, 750848]`, cumulative **179,783** at depth 7 and **930,631** at
  depth 8 — matching d44a's and the probe's committed figures from code
  sharing nothing with either.
* **THE ADOPTED PROOF NOTE'S ENTIRE LEMMA LIST, exhaustive to DEPTH 8
  (930,631 histories), my layer and my canonicalisation — zero violations
  of every one:** Lemma 1(a) per-register chains, 1(c) `cone_a ⊇` every
  `a`-authored event, 1(d) `cone_A ∪ cone_B` = everything, 1(e) version
  registers arbitrator-owned; Lemma 3's cone closed form (last pair-arb
  form, both branches); Lemma 2's dichotomy over **every admitted
  candidate**, plus `initiator ∈ proposers(ckey)` on every admitted `'r'`;
  Lemma 4(a) cone-invariant holdings and 4(c) cone-invariant own live
  proposals; Lemma 6 (`has_p` XOR `has_r`; `prop_options = {(X,0),(X,1)}`
  exactly; the cone component a singleton on `X`); Lemma 7 (≤ 1 full-view
  component per actor; component size ≤ 2; exactly one conflict edge in a
  2-component); **(5a), (5b), (5c), (5d), (5e)**; (H0) clause 4; **at most
  one menu-mentioned base dropped by `sigma`**; the quarter law; **`G`
  entrywise in exact `Fraction`s** (my own `G`, written from note §6, and
  compared on the *real* base names, not on a collapsed token);
  **(H1)** (36 classes, 0 splits) and **(H2)** (176 keys, 0 violations).
  Run time 14 min 37 s; a fuller variant (`battery.py`) reproduces the
  same at depth 7 with the additional Lemma-4 and `popts`-form checks.
* **Every arb mints a fresh base name:** 44,356 admissible arbs to depth 6,
  **0 collisions** with a base already present — the unstated obligation
  (2) of BLOCKER 1's repair list holds.
* **Deep and adversarial:** 120 trajectories × depth 60 and 150 × depth
  120, under three policies and two seeds (25,470 history visits), plus
  18,409 post-self-arb histories expanded five further levels — zero
  violations of any lemma, and **zero admissible pair-arbs after any
  self-arb** anywhere.
* **The equivariance step (§7) is sound, and I checked the step the note
  leaves implicit.** `canon_sigma`'s minimising renaming is **unique on
  all 34,375 histories** (spectrum `{1: 34375}`), so `canon_menu`'s inner
  minimisation is never load-bearing at this scope; the renamed menu is a
  function of the serialisation alone; and every `sigma` class agrees on
  `|refs|`, the `hold = None` pattern, the number of menu-only bases and
  the number of live proposals (**0 disagreeing classes**). `mis_of` and
  `PK1` are both renaming-equivariant (set-valued / permutation-averaged),
  so `G`'s only base-token traffic is copying, as §7 claims. Extras
  spectrum `{0: 29547, 1: 4828}` — never 2.
* **D51 immunity from the batch round's inversion (BLOCKER 1): CONFIRMED.**
  D61 and the probe load `sigma_raw` / `canon_sigma` / `canon_menu` by
  text slice from the committed `d44a` receipt and never construct or read
  D51's `projections()`. My independent canonicalisation reproduces 36
  states and 176 transition keys, so the route genuinely goes through
  `sigma`. (Immunity from BLOCKER 2 is MAJOR 4.)
* **The dichotomy explains the lag, as claimed:** the 2,032 full-view
  candidates are exactly D51's 2,032 lag pairs; `popts(cone)` is never
  *smaller* than `popts(full)` (0 of 68,750) and is strictly larger in
  4,828, always for the missed-supersession reason.
* **The quarter law reproduces exactly:** propose weights `{1/8}`,
  self-arb `{1/4}`, pair-arb `{1/8}` in twos, per-actor mass `{1, 5/4}`.
* **The `[PROBE-CARRIED]` depth-8 number is real, and I reproduced it
  independently.** The probe's `S4` genuinely enumerates 930,631
  histories and genuinely compares `canon_menu` per `sigma` class; I
  re-ran the committed probe at `MAXDEPTH = 7` and re-derived the whole
  depth-8 result from my own layer (36 states, 0 splits). Its weakness is
  `G`/5e coverage (MAJOR 2), not the (H1) conclusion.
* **The §4 first-run amendment is exemplary** and is not counted against
  the unit anywhere in this review. Recording "mechanise the induction
  was over-promised, twice", printing the 1,932-mismatch failure, and
  naming *why* a cache-gated machine cannot close the depth gap is the
  behaviour the campaign's discipline is for. It is also, precisely,
  the reasoning that BLOCKER 1 fails to apply to (H2) and (H0).

---

The mathematics here is the strongest single result the residue-1 line
has produced, and nothing I ran dented it: the own-view dichotomy is a
genuine theorem of the layer, the cone rigidity is real, `G` is right, and
(H1) holds on all 930,631 histories to depth 8 under code that shares
nothing with the receipts. What the unit has not done is finish the
sentence it wrote on
the cover. (H1) was one of **three** hypotheses; discharging it leaves
(H2) — which the adopted note itself calls a sketch, which d44a's own note
says is not implied by (H1), and whose only other support is a
finite-depth sweep of exactly the kind d44a's own round 1 refused to call
a theorem (I extended it a level, to depth 8; it is still a sweep) — plus
one clause of (H0) that the adopted note itself calls "a gate, not the
proof". "D44a is unconditional", "residue 1 is CLOSED", and "`Zhat` holds
at every depth" are therefore not yet earned, and they are already in the
book. The repair is small and entirely constructive: write the (H0)
incomparability proof (supplied above, three lines), write (H2)'s
event-by-event update table with its three unstated obligations said
aloud, gate (5c) and (5d), fix §1's imported D51 mechanism and §9's
inverted attribution, and restate the headline as *the last named gap has gone from
three hypotheses to two*. On that statement this unit is the campaign's
biggest step; on the statement it currently ships, it is not citable.

---

# DELTA — adjudication and repairs (campaign side, 2026-07-26)

**Verification of the round.**  Every load-bearing finding was
independently confirmed before repair: the BLOCKER textually in all
three parts (the pin's "(H2) follows from N2 at machine level" cites a
gate absent from the delivered receipt — `grep determinism` returns
nothing; the adopted note's own `[PROOF, sketch]` label at its (H2)
corollary; "a gate, not the proof" at GAP 3; the overclaim live in the
book §B6.13/§B6.14 and LOG #452); MAJOR 3 by an independent run
against the committed layer (the review's witness: `regs_of` returns
`{A, vname(·,·,B)}` for an initiator-not-proposer `'r'` by B — a third
view case — and `admissible` returns `(False, None)`); MAJOR 1/2
structurally (no 5c/5d gate existed anywhere; the deep loop computed
`extras` and never tested it; `sys.exit(1 if FAIL else 0)`).

**Repairs applied, all rerun green:**

1. **The headline is restated everywhere it shipped.**  Pin §2
   withdrawn by a §5 amendment; receipt VERDICT block rewritten ("D44a
   remains CONDITIONAL on (H2) alone; residue 1 DECIDED AT EVERY
   VERIFIED DEPTH; gap three hypotheses → ONE; 'closed'/'unconditional'
   may not be quoted from this unit"); LOG forward-corrected (#455);
   book patch dispatched under the one-go discipline.
2. **(H0) fully discharged.**  The review's clause-4 proof was
   verified step-by-step (Lemma 3's cone form + (5b) + pair-arb
   resolution) and written into the adopted note as **Lemma 7b**; GAP
   3 marked discharged.  BLOCKER part (b) thereby repaired
   constructively; part (a) ((H2)) remains open by design — it is
   D62's pin, with the review's three obligations stated aloud in the
   note's (H2) corollary.
3. **MAJOR 1:** (5c)'s missing first-self-arb-on-the-shared-base step
   written into §5; N2(c)/N2(d) gates added (order + menu + first-
   shared forms; 5d at full strength incl. same-bit): 20,348
   post-self-arb histories, 14,772 first-self-arb candidates, 0
   violations; deep-loop `D-5c`, `D-5c-first-shared`, `D-5d`,
   `D-S2.9`, `D-S2.10` added at depth 8.
4. **MAJOR 2:** `D-extras` guard added to the deep loop; the §8 GAP-1
   text now states what is gated where, truthfully.
5. **MAJOR 3:** §9 rewritten — the dichotomy is a theorem of `regs_of`
   **plus** the proposer test, with the third-case count and the
   scope-relevance sentence.
6. **MAJOR 4:** §1's route-2 paragraph now names missed supersession
   and cites the batch-round refutation of the old clause.
7. **MINORs:** N-programme retraction documented (docstring + pin §5);
   N0/N1 anchors strengthened (slice contents + the version-register
   line); N3(d) converted to a code-fact assertion; N4 gated `== 36` +
   window spectrum `[11, 19, 28, 32, 36]`; 9/4 removed from note,
   blockquote and gate (`{2, 5/2}`); case battery banner scoped to
   "cached transitions (parents to depth ≤ 5)"; EFFECTS gated for all
   three cases incl. the invisible supersession (N3(a)-(c), 0
   violations); §7's premise weakened to the serialised part with the
   `G`-factors-through clause added; probe-adoption caveat superseded
   by this round's independent re-verification; exit protocol fixed
   (exit 1 only on anchor breakage, N0/N1); three-actor wall exhibit
   cited in §8.4.  NIT 1: result note written
   (`note-d61-h1-closure-result.md`); NIT 2/3 noted, no code change
   needed beyond the above.

**Receipt rerun: 12 PASS / 0 FAIL, exit 0.**  Probe rerun at depth 8
with the new gates: launched, output replaces
`v10/data/d60p_h1_probe.out` (result recorded in LOG #455).

**Verdict after repairs: the unit stands as restated.**  (H1) is a
theorem; the residue-1 gap is (H2) alone; D62 pinned as the closing
unit.  The round's review is TERMINAL for round 1.
