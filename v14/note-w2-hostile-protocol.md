# WELD 2 (paper-13, the carrier census) — HOSTILE REVIEW PROTOCOL (FROZEN)

**Frozen:** 2026-08-10, v14 ledger #93.  Three reviewers,
independent, single-file writes, scratch-only, no imports,
read-only git; all mutant/injection work on scratch copies (the
plain run WRITES artifacts and takes ~2 min).  Grades A/AWF/R;
recomputations counted; findings ranked with exact repairs.

**Object (committed as-is, 58195da):** paper
v14/paper-13-weld2-carrier-census.md (`535e288ff412`), code
v14/code/w2_census_exact.py (`290149118b9d`), output
(`5e35e7a0115f`), receipt (`bacdb7a5e985`).  Pin
`9d19515cb3ae` (v14/note-weld2-census-pin.md, commit 95c3b77);
scout report of record `note-weld2-referent-scout.md` (amended
#89).  Reviews: `v14/review-w2-{operator,effectus,instrument}.md`.
Orchestrator verification: plain run BYTE-IDENTICAL; unknown flag
exit 2; selftest/mutant integrity checks completing (see ledger).

**Candidate-reading rule in force**: the delivered verdict
`WELD2-EMPTY-AT-THE-DECLARED-FAMILY-THE-ARITY-CYCLICITY-SCISSORS
@BOTH:MENU-113+CONG-185` (CANDIDATES=60|FOUND=0|SMUGGLED=0|
UNMOTIVATED=0) is a candidate reading until this panel and its
adjudication rule.

- **K1 THE CENSUS MACHINERY:** rebuild the 60-candidate
  enumeration from the pin's generator vocabulary independently
  (site ← {actor, MENU class, CONG-185 class, event subset, Ulam
  address prefix}; link ← {actor pair/channel, extension edge,
  cover pair}; count ← division-event counts between declared
  cuts); verify the fate of every cell (TYPE-DEAD 36, ARITY-DEAD
  12, ARITY-DEAD-BELOW 2, STRUCT-DEAD 10) at BOTH carriers; is
  the enumeration actually exhaustive over the declared
  vocabulary, and is any generator combination silently skipped?
  What does ARITY-DEAD-BELOW mean and is its separation from
  ARITY-DEAD principled?
- **K2 THE SCISSORS THEOREM (decisive):** the claimed obstruction
  — the one cyclic generator has 2 objects; every ≥9-object
  generator is acyclic (0 simple cycles, lengths 2–6); I7 is
  Z₃-periodic so any faithful restriction needs cycles; hence all
  C(113,9)/C(185,9)/C(2²⁰,9)/C(3969,9) restrictions die BY
  THEOREM.  Verify both blades independently; verify the cycle
  search's length bound suffices for Z₃ (and for every torus the
  claim quantifies over); verify the theorem's quantifier
  actually covers the no-enumeration claim; attack: is there a
  generator-combination or quotient object OUTSIDE the checked
  set that is both ≥9 and cyclic?  Does the scissors survive at
  d74's d≤5 window?
- **K3 THE CONTROLS (two-way gates):** the crystal FOUND control
  (DOUBLE-GRID(3,2): 72 isomorphisms → ONE count field, all
  three fibers 1) — rebuild the isomorphism census; audit
  whether the control's FOUND standard is the SAME standard the
  real census applies (same gates, same free-item accounting), or
  whether the crystal's declared blueprint smuggles the answer;
  the withheld-arbitration falsifier (fiber 6); the D58 EMPTY
  control + its independent falsifier (0 of 4 division events on
  the (A,B) channel) + the substitution flip; the crystal-vs-I7
  STRUCT-DEAD (0 of 9! bijections).  Rule: are FOUND and EMPTY
  both genuinely reachable BY THE SAME instrument?
- **K4 THE SURPRISES AND THE RE-DERIVATION:** (a) THE EMPTY
  DIAGONAL — n_{e1+e2} ≡ 0 at 9/9 sites in 5/5 crystals: verify
  the measurement; state its licensed reading (q₁₂ unfixable
  from the committed crystal family) and its candidate
  over-readings; note the R4 resonance (the connective-forcing
  (1,1) link) and rule what may be claimed at citable scope.
  (b) CONG-185 re-derived six-of-six (185 classes, 5 rounds,
  bisimulation comparator; descent everywhere; 0 multi-valued;
  44 squares; ⟨2,3⟩ both holonomies rank 2; CK 10/10) — verify
  against the D74 artifacts and the Γ-main operator review's
  definition; is the re-derivation genuinely independent of the
  frozen review's construction?  (c) the unweighted-113
  disclosure.  (d) the two drifted-source git-show routes
  (#46/no-moving-refs compliance — but note the reads were at
  95c3b77, a pinned commit: verify the products are gated).
- **K5 INSTRUMENT — the first unit BORN under the #82 contract:**
  audit the CLI against the full contract (argv whitelist
  demonstrated in source at 2506–2545; selftest 18/18 anchors
  killable claim — verify a sample, confirm writes-nothing;
  --mutant unknown names exit 2; registries complete 13/13);
  coverage at #34 (32 gates vs 13 mutants — honest denominators,
  assert-unmutated and tautological mutants named); comparator
  independence at #82 (the worker claims independent comparators
  from different primitives for every verdict-bearing number —
  test for shared typed literals); verbatim anchors at #62 (11
  verbatim — quote fidelity, consumer gates, meaning-binding);
  the 3 waivers backed (#34); the no-moving-refs engraving (all
  repo reads at pinned shas, products gated, off-tree/git-less
  byte-reproduction — TEST IT, this unit postdates the
  engraving); verdict-in-gate (#234) and head-derived-not-copied
  (the R4 lesson); prose-renders-from-receipt (#20) over every
  numeric token; paper↔output↔receipt three-way sweep;
  byte-identity; repo hashes unchanged after all work.
