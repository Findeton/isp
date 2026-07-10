# note-stem-level4 — the level-4 covtree census

**Status:** design note, 2026-07-10 (v9 round 39; paper XIV outlook (c)). Receipt: `v9/code/stem_level4_census.py` (pinned here, committed strictly before running). Reviews ON.

## The object

Covtree level-4 nodes = sets Q of unlabeled 4-posets such that Q = the exact-size-4 stem set of some causet with >= 4 elements (equivalently, by the paper-XIV extension lemma + Theorem 6, the non-empty atoms of B_4 on the history space). There are 16 unlabeled 4-posets (A000112), so candidates are the 65535 non-empty subsets; level 3 has 22 of 31 (DIOSZ, confirmed round 38). The level-4 count is in no literature (DIOSZ stop at level 3; Gutzeit et al. prove witness-size bounds, not censuses).

## The instrument (the round-38 interface machine, scaled)

**The boundary.** For 4-stems only elements with |past| <= 2 matter for FUTURE stems (an element inside a future 4-stem with top y satisfies |down(y)| <= 4, so every non-top member has |past| <= 2; a birth above P with |P| = 3 fires its bundle at birth and never appears in a later small stem). So the interface B = the induced structure on {x : |past(x)| <= 2}: minimals m; children c (past = one minimal); grandchildren g (past = a 2-chain {m,c}); joins j (past = a 2-antichain {m,m'}). Nothing attaches above g or j within B.

**Moves.** Choose a down-set P inside B with |P| <= 3 (the nine structural kinds: empty; {m}; {m,m'}; {m,c}; 3-antichain; L; V; 3-chain; Lambda). A new element x above exactly P creates the stem {x} + D for EVERY down-set D >= P with |D| <= 3 (x is above exactly P inside D — clean because P is a down-set); the bundle registers in the signature (sig2, sig3, sig4 tracked as bitmasks; 4-types via a precomputed 6-bit-relation -> type table). B updates only when |P| <= 2 (x joins as minimal / child / join / grandchild), subject to the caps.

**Caps and soundness.** Caps (max minimals, children per minimal, grandchildren per child, joins per pair) bound the state space. A capped add fires its bundle but is forgotten. SOUNDNESS IS FREE: every machine path is a literal growth construction (the abstract state is a faithful sub-record of a real causet's boundary), so every reached signature is realizable — witnessed by replaying the BFS path. Only COMPLETENESS depends on the caps.

**State + search.** State = (canonical B, signature); canonical B = the multiset of minimal-descriptors (each: sorted child descriptors, each child: grandchild count) + the join multiset over minimal pairs, canonicalized over permutations of minimals. Transitions cached per distinct B-canon (independent of signature). BFS to closure — no size bound needed; the census = the distinct sig4 parts over states with sig4 non-empty (sig4 non-empty iff the underlying causet has >= 4 elements, since down-sets of every size <= n exist).

## Registered gates (exit 1 on refusal)

- **G1 (brute anchor):** streaming labeled enumeration to n = 8 with incremental signatures (child sig = parent sig | birth bundle — the same bundle logic as the machine, applied to concrete causets); labeled counts must print 1/2/7/40/357/4824/96428 (recounted round 38) and n = 8 must equal 2800472 (A006455); per-n cumulative exact-4 censuses printed, monotone.
- **G2 (level-3 back-check):** the machine's exact-3 census must be 22 (round-38 anchor).
- **G3 (exhaustive cross-validation):** the machine run n-tracked to n = 8 must reproduce the brute cumulative census EXACTLY at every n <= 8 (all three signature layers) — the move/bundle logic validated against the full enumeration.
- **G4 (cap-stability):** the production census must be IDENTICAL at two increasing cap settings (pinned: (4,2,1,1) and (5,3,2,1)); disagreement = refusal (caps too small; rerun larger).
- **G5 (witness soundness):** for EVERY census node, replay the BFS path into an explicit labeled causet, recompute its signature from scratch (independent code path: subset enumeration + canonization), and require equality. The lower bound is then exhibition-grade regardless of the machine.
- **G6 (determination shadow):** each distinct sig4 part must carry exactly one full (sig2, sig3, sig4) signature among sig4-nonempty states (the paper-XIV extension lemma's census-level shadow; violation = bug).
- **Outputs:** the level-4 count; the per-n new-node counts to n = 8 (the analogue of level 3's "21 at 6, 22 at 7"); minimal witness sizes per node as reached; the node list with signatures, machine-run witness sizes vs the Gutzeit-class bound cited as frame.

**Grade semantics:** the node LIST + count = [MEASURED — every node witness-verified (exhibition-grade lower bound); completeness cap-stable under G4 and exhaustively brute-validated to n = 8 under G3]. Completeness for all n under NO cap assumption is NOT claimed without a proved truncation lemma (a named opening for the review).

## References

paper XIV (shard: Theorem 6, the extension lemma, rB3's level-3 machine); DIOSZ 1910.07292 (level 3, App. B.1); Gutzeit et al. 2605.00622 (witness bounds); A006455, A000112; round-38 LOG + LEDGER #100-#102.
