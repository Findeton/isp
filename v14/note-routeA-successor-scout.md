# ROUTE-A SUCCESSORS — THE SCOUT REPORT (of record)

**Date:** 2026-08-10 (ledger #95 launch, #101 record).  Read-only;
zero repo writes confirmed; drifted files read via git show at
pinned commits (both re-verified identical at 95c3b77 and
822bb15).  Purpose: ingredient inventory for the two census-named
Route-A successor pins (the ≥9-actor carrier; U4), plus two
surprises that feed the weld-2 adjudication directly.

## (a) THE ≥9-ACTOR CARRIER — ingredients and THE KILL-RISK

**Ingredients (sha-pinned in the full tables, task record #95):**
the generator is actor-pool-parameterized (d42b1
`enumerate_family(pool,d)`, `576275d55ecf` — a parameter flip,
not a re-authoring); the v14 rebuild hard-codes the pool in
exactly TWO lines (w2 L708/L1486); the pinned windowed-precedent
rows are D74's d≤5 265/462 (`0180e21c7127`) and the dep−2 trick
(`bb852161aced` L1382–86); the declared sub-grammar shapes are
d74's `oneway`/`ring` (L1406–18); **no general-actor-pool menu
COUNT law is committed** (only the mass law 1+(m−1)/4, with THE-
THEORY-SO-FAR L5866's explicit refusal to carry it forward); the
corpus nowhere enumerates a family above 4 actors, and above 4
never beyond depth 2 — every ≥8-actor artifact is one FORCED
record with per-step full-menu replay.

**Compute law (scout-measured, exact n=2..11):** depth-1 menu =
n²+2n (reproduces the pinned 8 at n=2; 99 at n=9); branching at
n=9 ≈ 98.8 per depth.  **Exact enumeration at 9 actors d≤4 is
INFEASIBLE** (~9.6×10⁷ histories; ~10¹⁰ cached candidate tuples);
d≤3 (~9.7×10⁵, ~7–8h) is the realistic ceiling; d≤2 (9,783)
trivial.  A ≥9-actor pin MUST declare a window (three pinned
precedents: depth-3 cap; dep−2; a channel sub-grammar).

**THE KILL-RISK (severe; scout-measured):** actor-relabelling
equivariance from the empty history makes the family
Sₙ-invariant, so the co-division ACTOR-PAIR graph is **COMPLETE
AND CONSTANT** — measured exhaustively at n=3 d≤3 (6/6 ordered
pairs, all counts exactly 16), with the enabling sub-history
verified admissible at 9 actors depth 3.  A symmetric 9-actor
carrier's ACTOR-PAIR relation is **K₉, 8-regular**; measured:
K₉ → I7's 3-link target = **0 isomorphisms**; K₉ → the 2-link
crystal target = 0; the count field is constant (no curvature);
DECLARED-RESTRICTION cannot repair (K₉'s induced subgraphs are
K₉); EXTENSION-EDGE is closed by S2 below.  **Dead-on-arrival
condition: posing (ACTOR, ACTOR-PAIR) at the full symmetric
family re-derives EMPTY by over-connection.**  The one live
move: a DECLARED channel sub-grammar (oneway/ring shape)
breaking S₉ to a 3- or 4-regular incidence — a priced
declaration (a free item; Route-B-adjacent).

## (b) U4 — ingredients and the walls

**Spec (verbatim, v11 paper 0 §7 L336–47, `37a428321f46`):**
"U4 — SPARSE RECORDS ON THE CRYSTALS.  The conflict crystals
rebuilt with renewal-only records: geometry should be invariant
(it is kinematic — paper 0 §10's third falsifier if not); the
bridges between the renewal sublattice — itself periodic: the
division events of a crystal form a crystal — are probed for
indivisible structure."  The POSIT (§4 L144–47): division events
ARE the renewal events.  Renewal = class-0-carrying-an-arb,
SOURCE-FORCED (paper-09 §3, `006f96aaa2ff`; r6bp verdict tag).
Constructors committed twice (v10 originals `684cdb76552b`/
`3d0516ab106e`/`e80edf851d93`/`89e170f40579`; v14 self-contained
rebuilds w2 SEC 6 — five crystals, all FORCED, maxhits=1).
**"The division events of a crystal form a crystal" has never
been checked anywhere** — registered-unrun in the committed gate
G-U4-REGISTERED (w2 L2307–16).

**PRELIMINARY (scout scratch, NOT corpus-grade):** translation
stabilizer of the division-event field on Z₃²:
DOUBLE-GRID(3,2) 72ev/18div → stabilizer **order 3 = ⟨(1,1)⟩**;
DOUBLE-GRID(3,3) 96/24 → ⟨(1,1)⟩; CONFLICT-GRID(3,2) 30/6 →
⟨(1,1)⟩ (footprint constant, order 9); CONFLICT-GRID(3,4) 66/12
→ ⟨(1,1)⟩; D60-GRID(3,12) 46/**1** → order 1.  **First look:
U4's claim reads TRUE on all four ARBITRATION crystals — with
the invariance direction the DIAGONAL — and FALSE on the
delivery crystal** (paper-13 L501–04 already names the
delivery-vs-division distinction).

**The U4 pin's declared-data obligations:** the SITE READING
(initiator `op[1]` vs register footprint `regs_of` — supports
differ 6/9 vs 9/9; stabilizers agree); the RENEWAL-ONLY
OPERATIONALIZATION (nowhere pinned; three candidates: filter the
record to 'r' events / re-run the Builder on a restricted
candidate stream / quotient by non-arbitration events); scope to
ARBITRATION crystals.  **The walls (engrave in the pin):** L-1 —
U4 may test only order-level covariance, a FOURTH form whose
admissibility must be ARGUED BEFORE TESTING (the old "weaker
form" sentence was RETRACTED 2026-07-28 — do not reproduce it);
the BHS wall (finite valency ⟹ sprinkling-grade LI provably
unavailable — testing it manufactures a false negative; catalog
§1.6 "Engrave in the U4 pin"); Kleitman–Rothschild height
control mandatory (§1.7: "a dimension reading without a height
control is worthless"); the crystals' co-division graph is the
rook's graph — **q₁₂ ≡ 0 is inherited unchanged** (diagonal
pairs share neither row nor column).

## (c) SURPRISES (S1–S7)

- **S1 — K₉ IS a Cayley graph on Z₃², just not I7's:**
  Cayley(Z₃², {e₁,e₂,e₁+e₂,e₁−e₂}) is 8-regular ≅ K₉ — measured
  **362,880 = 9! isomorphisms** (vs 0 onto L=2 and L=3).  The
  ≥9-actor obstruction is precisely a **LINK-COUNT MISMATCH:
  the grammar offers 4 directions, I7 declares 3.**  The
  diagonal is NOT structurally absent from the grammar — only
  from the crystals (rows/columns conflict groups).  A ≥9-actor
  carrier would be the corpus's first construction populating a
  diagonal pair (the first nonzero grammar-side q₁₂ = −c/2 at a
  declared assignment) — but the STRUCT gate fires first; only
  a declaration reaches it.
- **S2 — CONG-185 is depth-pure, so its acyclicity is a THEOREM
  at every depth cap** (classes spanning >1 depth: 0 at
  DEPTH=2,3,4; self-loops 0,0,0) — truncation makes
  remaining-height a bisimulation invariant.  The paper's
  registered "cycles at depth ≥5?" test cannot succeed at CONG;
  only MENU is live (its 45 self-loops = exactly its 45
  multi-depth classes, at every cap — S5).  Convergent with the
  weld-2 operator's grading theorem.
- **S3 —** no crystal menu ever BRANCHED at 9 actors in the v14
  rebuild (pool 1–2 per call; the v10 originals replay full
  menus along one forced record) — a successor inherits no
  9-actor menu law and must declare one.
- **S4 —** COVER-PAIR's counts are identically zero by
  construction (w2 L1558, "covers bound no interior") — the
  generator can never carry a count.
- **S6 —** the pin's dead list is named C1–C5 (+4 blanket rows);
  cite, never re-run.
- **S7 —** the scissors' quantifier is SITE-SUBSETS on THIS
  carrier (§8.3: "a statement about this carrier") — both
  successors are genuinely outside the delivered verdict's
  scope.

## (d) Binding engravings for both pins

#82 (CLI + strengthened comparators), #87 (gates bind objects —
any "all 9 sites" gate binds per-site), #91 (pinned-sha reads,
products gated, off-tree/git-less byte-reproduction), §15
(declared-arena; match every coordinate; repair-propagation:
diff gates against every rule engraved since the pin froze).
