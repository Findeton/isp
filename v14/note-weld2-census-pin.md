# WELD 2 — THE CARRIER CENSUS (paper-13) — PIN (FROZEN)

**Frozen:** 2026-08-10, v14 ledger #85.  **User's order (verbatim):
"ok do route A"** — on the scout report of record
(v14/note-weld2-referent-scout.md `e1f771a9d0ed`, ledger #83).
**Unit:** paper-13-weld2-carrier-census — a BRG-shaped census at
the level BRG explicitly declined (its §14 open 4), posed to
return EMPTY well.  Artifacts: v14/paper-13-weld2-carrier-census.md,
v14/code/w2_census_exact.py, w2_census_output.txt,
w2_census_receipt.json.

## THE QUESTION (frozen)

Does a MOTIVATED map exist from the transport grammar's carrier to
the spatial record lattice — a map sending grammar objects to
sites, grammar object-pairs/channels to links, and SETS OF
DIVISION EVENTS to link counts n_ℓ(x) — where motivated means
ZERO free items at the RSQ standard?  The scout's verdict
(NO-SEED-AT-THE-CARRIER, two-agent convergent, #83) is the
candidate reading this census must confirm, refute, or scope.

## R1 — THE TWO SIDES, DECLARED AS DATA (§15)

- **Deformation side:** I7's arena (X, L, s, n, m) — sites ×
  links × counts × front × register.  Sources: I7 receipt
  `542b8735daf0` (v13/code/ha_successor_receipt.json), HA paper
  `f286ba10d2d9`, HA code `d44cb72f8ee9`.
- **Grammar side, BOTH carriers (the #82 amendment; verdicts
  carrier-stamped @MENU / @CONG-185 / both):**
  - **MENU**: the 113-class quotient of the 3,969 histories at
    (A,B), d≤4, with its event-extension graph and D74's 1,546
    closed squares as 2-cells.  Sources: Γ-main paper
    `d85a629a9378` (read at commit 822bb15 via git show — the
    repair worker is writing this file concurrently), D74 result
    `0180e21c7127` (v10/note-d74-transport-holonomy-result.md),
    D74 pin `b9997d125ef5`.
  - **CONG-185**: d74's coarsest weighted congruence.  NOT taken
    on faith: RE-DERIVED here from the D74 pinned artifacts per
    the definitional source (review-gmain-operator.md
    `f67871bc51f5`; adjudication `972e54741330`), with its six
    ruling properties GATED before use — descent at every
    horizon, 0 multi-valued edges, all 44 curvature squares
    intact, q-holonomy ⟨2,3⟩, k-holonomy ⟨2,3⟩, exact
    lumpability.  A derivation mismatch is a deliverable finding,
    not a silent substitution.

## R2 — THE ONLY MOTIVATED INGREDIENT, ISOLATED AND GATED

The count semantics: n_ℓ(x) = the number of division events in
the record interval (HA §3.1–3.2 `f286ba10d2d9`); division events
ARE the renewal events (v11 paper 0 §4 [POSIT] `37a428321f46`).
Every candidate map must (i) send a set of grammar division
events to the count register of a specific link, and (ii)
reproduce R6a's ADDITIVITY-972-OF-972 (paper-04 `dfa5090f26b1`
§1) under the induced subdivision.  Any candidate requiring a
POSITION INSIDE a leg is dead on arrival (R6b′ §9 type census,
paper-09 `006f96aaa2ff`: a leg has no interior division event).

## R3 — THE CANDIDATE FAMILY, DECLARED AS DATA (the EMPTY scope)

EMPTY is a statement about a DECLARED family, per BRG's species
discipline (`371e38742059`).  Generator vocabulary (from the seed
inventory, #83):
- **site ←** { actor, MENU class, CONG-185 class, event subset,
  Ulam address prefix }
- **link ←** { ordered actor pair / delivery channel, extension
  edge, cover pair }
- **count ←** { division-event count on the chosen link object
  between two declared arbitration cuts }
The census enumerates the generator combinations exhaustively
over this vocabulary at both carriers; the count of candidates is
COMPUTED, never typed (#24).  Arity/type obstructions (e.g. the
2-actor carrier vs 9 sites) are measured outcomes, not skipped
cells.  The verdict string carries the family:
EMPTY-AT-THE-DECLARED-FAMILY if EMPTY.

## R4 — THE CHOICE INVENTORY (RSQ standard)

Every construction choice classified declared / forced (forcing
exhibited) / free (fiber measured and printed).  MOTIVATED ⟺
zero free items.  Pre-registered expected free items:
I-SITE-ASSIGNMENT, I-DIRECTION-LABEL, I-ORIENT — their exact
fibers printed.  Pre-registered dead list (may not be re-run,
only cited): C1–C5 with free-item counts 6/5/1/4/1 (`006f96aaa2ff`
§9; C3 the least-unmotivated AND degenerate — admissible only at
count 1, 29/201, split fiber 0); BRG-EMPTY-AT-CARRIER
(`371e38742059`); order-only spatial instruments (GW1 §2
`6f825ef6e1ce`); v12 Γ objects (`17111fd19022`); naive 9↔9
(L≥4 measured, paper-02 `1a80a5bf1a1b` §11).

## R5 — TWO-WAY GATES: BOTH VERDICTS REACHABLE, EACH FALSIFIED

HA §14 requirement 3 verbatim: "A predicate that cannot return
its other value anywhere in the declared arena is not a
measurement."
- **FOUND-side positive control — THE CRYSTAL ARENA:** rebuild a
  crystal record from its committed spec (D60 pin `2c715308c22b`,
  result `19e50d34635f`; D66 pin `f09c9091bf58`, result
  `c32eb7814993`; D67 pin `598c429fcc9c`, result `13712723c0cd`)
  — a grammar record PROVABLY carrying a lattice (forced,
  exactly-one-candidate, sprinkling-grade homogeneity, width
  ceiling k·b ≤ k² saturated).  The census machinery, run on the
  crystal arena, must return FOUND (the record's own cover
  structure forcing the lattice) — else the detector is broken
  and the unit aborts.  Register (successor, not this unit's
  claim): v11 paper 0 §7's U4 — "the division events of a
  crystal form a crystal" (`37a428321f46`) — the renewal
  sublattice as the generated-carrier form of this control.
- **EMPTY-side negative control:** the generic 2-actor walk
  (D58 result `ce536758fbaa`; homogeneity 0.067) — the census
  must return EMPTY there by a declared falsifier.
- Both control verdicts carried by gates with mutants that flip
  them; a control that cannot fail is a finding against the unit.

## R6 — THE SHARPENED NO-SMUGGLING GATE

At I7, record ↔ metric is an invertible linear re-encoding (HA
§2/G28, det 2): ANY map supplying n_ℓ supplies the metric, so
GW1 §1.2's what-it-may-see exclusions cannot discriminate here.
The gate tests WHICH FUNCTION of grammar data each candidate
computes: the candidate's count values must be derived from
grammar-side data alone (division-event sets on the chosen
objects), never read back from I7's s.  A candidate whose counts
are I7-readbacks is classified SMUGGLED, a separate species from
UNMOTIVATED, and both species are counted.

## R7 — ARENA-INVARIANCE (§15) + STANDARDS

The prime, the labelling, the completion, and the specific
history sample appear as instrument readings, never premises
(BRG requirement 4).  Full era standards in force at
CONSTRUCTION (not as repair debt): the #82 CLI-contract minimum
(argv parsing; unknown flags exit 2; real --selftest
corrupt-one-anchor/exit-1/write-nothing; --mutant NAME harness);
comparator independence at the #82-strengthened standard (no
shared code, inputs, or typed literals); #34 waiver standard;
#62 verbatim anchors (meaning-binding, consumer-gated,
mutant-falsified); #46 no unanchored runtime inputs — all pinned
reads sha-verified at start, abort on mismatch, git show for any
file with a live concurrent writer; #24 counts computed; #20
prose renders from the receipt; exact arithmetic
(fractions.Fraction) throughout; byte-reproducible plain run.

## OUTCOMES (pre-registered)

`WELD2-CARRIER-MAP-FOUND-<map>` /
`WELD2-EMPTY-AT-THE-DECLARED-FAMILY-<obstruction>` /
`WELD2-BLOCKED-AT-<object>` — carrier-stamped (@MENU /
@CONG-185 / both), with the SMUGGLED count and the free-item
fibers in the verdict's readout segments.  Between delivery and
adjudication every headline reading is a candidate reading.
