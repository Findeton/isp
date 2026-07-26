# D62 — (H2): the update table, written out (PIN)

**Status:** PIN, STRICT, 2026-07-26.  Parents: D61
(`note-d61-h1-closure-result.md` — (H1) [THEOREM], (H0) fully
discharged incl. Lemma 7b, D44a CONDITIONAL ON (H2) ALONE), the
adopted proof note `note-d60p-h1-probe.md` §7's (H2) corollary with
its **three named obligations**, d44a's conditional closure theorem
(consumes (H2) in both legs), and the D61 round-1 review (BLOCKER 1's
repair list; (H2) verified exhaustively through depth 8 on an
independent layer — 176 transition keys, 0 violations — *evidence,
never a premise*).

## 1. The one job

Prove **(H2)**: `sigma(h+e)` is a function of `(sigma(h), renamed e)`
at two-actor delivery-free d42a scope, at every depth.

Method — **THE UPDATE TABLE, AS PROSE-OVER-CODE PROOF.**  Write the
effect of each admissible event class on the **serialised** sigma
data (`hold`, `live`, `comps`, and `sup` restricted to `refs` — what
`ser()` writes, per D61 round-1 MINOR 10) purely in terms of that
data and the renamed event.  The cases are Lemma 5's four — idle,
propose (with the **propose-on-a-dropped-base** sub-case), self-arb,
pair-arb — and each row must be a reading of the committed layer, not
a sweep.  The three obligations are part of the table, not an
afterthought:

- **(O1) the dropped-base token.**  When `hold[x] = None` with no
  live `x`-proposal, a propose on `X_x` references a token `sigma(h)`
  does not record.  Prove the successor sigma is still determined up
  to renaming: the token is forced by 5e (a THEOREM by Lemma 5's
  completed induction) and the single-`EXTRA` argument (§6 S3(b)).
- **(O2) fresh-version-name non-collision.**  Prove
  `vname(b, W, x)` never collides with a base already present (a
  collision forces `x` to have arbitrated `b` before, hence
  `b ∈ superseded` in `cone_x`, hence the arb inadmissible — write
  it out against the layer).  Measured standing: 44,356 admissible
  arbs to depth 6, 0 collisions.
- **(O3) incomparability feeding `comps`.**  `comps(h+e)` is built
  from `edges()` from `incomparable()`; the clause is **Lemma 7b**
  (proved, D61 round 1) — cite it where the table's arb rows use it.

## 2. The receipt

Gates are EVIDENCE for the rows, never premises (the D61 §4/§5
lesson, stated here in advance so it cannot be over-promised a third
time: **a cache-gated table check alone cannot close the depth gap —
the force must come from the rows being proofs**).  The receipt
gates:

- **T1**: every cached transition (parents to depth ≤ 6 at least)
  computes both sides — the layer's `sigma(h+e)` and the TABLE's
  prediction from `(sigma(h), renamed e)` — entrywise equal, zero
  exceptions, with the transition-key count anchored to d44a's
  committed **176** and the state count to **36**.
- **T2**: the O2 collision census, re-run and gated (0 collisions),
  PLUS the inadmissibility argument's premise gated (every arb whose
  minted name would collide is refused by the layer — constructed
  adversarially if reachable, else the refusal branch is exhibited
  on the nearest reachable configuration).
- **T3**: the O1 sub-case isolated: every propose-on-a-dropped-base
  transition, successor sigmas pairwise identical up to renaming
  within each `(sigma, renamed e)` class.
- **T4**: the table's row coverage — every cached transition matched
  to exactly one row (no silent fall-through).

## 3. Pre-stated consequences of success

If every row is proved and T1–T4 gate zero exceptions:

- **(H2) becomes [THEOREM at two-actor delivery-free d42a scope].**
- With (H0) discharged (D61) and (H1) [THEOREM] (D61), **D44a's
  closure theorem becomes UNCONDITIONAL at that scope**; the
  36-state closure, the six-state chain, and the Perron package hold
  at every depth; **RESIDUE 1 IS CLOSED at that scope**; D49's
  root-free completion is unconditional at every depth there —
  still within the stationary form (D50: the form remains a
  choice), still delivery-free (transport untouched).  The D61
  quotation embargo lifts.
- Paper 30/32 and book updates land after THIS unit's hostile round,
  per discipline.

## 4. Falsifiers / scope

Any transition key with two successor sigmas is the deliverable and
kills (H2) as stated (exit 0 for substantive negatives; exit 1 only
on anchor breakage — N0-class anchors are the committed-layer and
d44a slices).  Any obligation that resists proof is the deliverable:
the unit then ships "(H2) conditional on <named sub-obligation>" and
the gap has a new, smaller name.  TWO-ACTOR DELIVERY-FREE d42a ONLY;
three actors and transport are out of scope and the pin forbids
wider quotation.  The table is about the SERIALISED sigma; no claim
about the full raw tuples is made or needed (round-1 MINOR 10).
