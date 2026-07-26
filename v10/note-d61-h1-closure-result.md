# D61 — result: (H1) IS A THEOREM. The gap is one hypothesis, not three.

**Status:** ROUND-1 REVIEWED AND REPAIRED, 2026-07-26.  Round 1 was
an independent Opus 5 hostile review, frozen at
`reviews/d61-round1-hostile-review.md` — REVISE, 1 BLOCKER / 4 MAJOR
/ 10 MINOR / 3 NIT.  The mathematics survived everything: the
reviewer re-implemented the admission layer from scratch (different
reachability, components, MIS, PK1 — zero mismatches on 6,471
histories), ran the adopted proof note's **entire lemma list
exhaustively to depth 8 — all 930,631 histories — with zero
violations of every one**, and reproduced 36 sigma states / 176
transition keys from code sharing nothing with the receipts.  What
did not survive is the sentence the unit sold the theorem with.
Repairs applied; receipt rerun green (12 PASS / 0 FAIL, exit 0).
Pin `note-d61-h1-closure-pin.md` (§4 first-run amendment; §5 round-1
amendment).  Receipt `v10/code/d61_h1_closure_exact.py`, output
`v10/data/d61_h1_closure_exact.out`.  Adopted proof note:
`note-d60p-h1-probe.md` §3–§9 (repaired on round 1).  An independent
round has now RUN; this note states what it left standing.

---

## 1. The theorem

> **(H1) [THEOREM, two-actor delivery-free d42a scope].**  For all
> histories `h, h'` of ANY depth, `sigma(h) = sigma(h')` implies
> `menu(h) = menu(h')` as renamed event-multisets with exact
> weights.

Carried by the adopted proof note's prose-over-code argument:
register geometry (Lemma 1), the own-view dichotomy (Lemma 2 — a
theorem of `regs_of` **together with** `arb_components_in_view`'s
proposer test), the cone closed form (Lemma 3), cone rigidity
(Lemmas 4–5, invariants 5a–5e), the cone and full-view menus in
closed form (Lemmas 6–7), incomparability (Lemma 7b), the explicit
menu formula `G` (§6), and depth-free equivariance (§7).  The
receipt gates every case claim of the induction — preconditions AND
effects, including the invisible supersession — at every cached
transition, the code-facts against the source, and the conclusion at
36 sigma classes with d44a's exact window spectrum; the probe and
the round-1 review each gate the conclusion independently at depth 8.

## 2. What the theorem does NOT deliver — the round's BLOCKER

D44a's conditional closure rests on (H0), (H1), (H2).  D61 as first
shipped claimed all three and delivered **one and three-quarters**:

- **(H2) — sigma-transition determinism — is UNDISCHARGED.**  The
  pin grounded it on a gate the §4 amendment had deleted; the LOG
  ground ("CG2 + the closed form") is a finite-depth sweep plus an
  object with the wrong codomain (`G` predicts menus, not sigma
  successors).  d44a's own note is explicit that (H2) does not
  follow from (H1).  Standing: verified exhaustively through depth
  8 (round 1, independent layer: 176 transition keys, 0
  violations), plus the adopted note's `[PROOF, sketch]` corollary
  with its **three named obligations** (the propose-on-a-dropped-
  base case; fresh-`vname` non-collision — 44,356 arbs, 0
  collisions; incomparability feeding `comps`).  **D62 is the
  closing unit: write the update table event-by-event and discharge
  the three obligations as theorems.**
- **(H0) — the four structural clauses — is now FULLY DISCHARGED.**
  Clauses 1–3 are corollaries of Lemmas 4/5.  Clause 4 was carried
  by a counter the adopted note itself called "a gate, not the
  proof"; round 1 supplied the proof and it is now **Lemma 7b**,
  each step verified against the layer.

> **The honest headline: residue 1 is DECIDED AT EVERY VERIFIED
> DEPTH, and its last named gap has shrunk from three hypotheses to
> ONE.**  "Residue 1 closed", "D44a unconditional", "Zhat holds at
> every depth" are not delivered here and may not be quoted from
> this unit.  They become quotable if and only if D62 lands.

## 3. Corrections carried by round 1 (all verified before applying)

- **The dichotomy's mechanism was attributed backwards** (MAJOR 3).
  `regs_of` *produces* a third view case (5,712 initiator-not-
  proposer views at depth ≤ 5 — I reproduced the witness against
  the committed layer); `admissible`'s proposer test *kills* it.
  The proposer test is exactly the clause a three-actor or
  transport-scope extension must re-examine.  §9 and the book
  carried the inverted sentence; both corrected.
- **The adopted note imported D51's refuted mechanism** (MAJOR 4):
  §1's route-2 paragraph named the missed-own-proposal clause the
  batch round had struck (0 of 68,750 firings; the real cause is
  missed supersession, 9,656/9,656).  §1 now states the true
  mechanism; §5 always had it right.
- **(5c) and (5d), cited by the induction's hardest step, were
  gated nowhere** (MAJOR 1); (5c)'s prose was missing the step that
  the *first* self-arb sits on the shared base.  The step is now
  written (§5) and everything is gated: shallow (N2(c)/N2(d):
  20,348 post-self-arb histories, 14,772 first-self-arb candidates,
  0 violations) and deep (`D-5c`, `D-5c-first-shared`, `D-5d`,
  `D-S2.9`, `D-S2.10` at depth 8).
- **The depth-8 `G` gate was blind to the two-dropped-base failure
  mode** (MAJOR 2); the `D-extras` guard now closes it, and round 1
  independently confirmed `|extras| ≤ 1` on all 930,631 histories.
- The unreachable `9/4` total removed (per-actor `5/4` is pairwise
  by (5b)); §7's equivariance premise restated to what `ser()`
  delivers, with the missing clause (`G` factors through the
  serialised part) added; anchors tightened to exactly 36 states +
  window spectrum `[11, 19, 28, 32, 36]`; the case battery now
  gates *effects*, not only preconditions; exit protocol fixed
  (exit 1 only on anchor breakage); the pin's dead N-programme
  numbering documented; the three-actor wall is now EXHIBITED
  (round 1: 5,904 admissible third-case views at depth ≤ 4 — and
  only Lemma 2 breaks there, which tells the successor unit which
  lemma to attack).

## 4. What round 1 confirmed clean (its own code, its own layer)

Byte-identical receipt rerun under three `PYTHONHASHSEED`s; the
census `[1, 6, 32, 176, 976, 5280, 27904, 145408, 750848]`
reproduced from scratch; every lemma, invariant, the quarter law,
`G` entrywise on real base names, (H1) AND (H2) — exhaustive to
depth 8, zero violations; deep adversarial walks to depth 120 under
three policies, zero violations; `canon_sigma`'s minimising renaming
unique on all 34,375 histories; the 2,032 full-view candidates are
exactly D51's 2,032 lag pairs.

## 5. Residues

1. **(H2)** — the update table (D62).  The last hypothesis.
2. **Lean-grade mechanization** of the induction (unchanged).
3. **Three actors** — out of scope, wall exhibited; the successor
   knows to attack Lemma 2's proposer clause.
4. **Transport scope** — untouched, as always.
