# D42b7 round 1 — hostile review (pin + receipt + out)

**Reviewer round:** 2026-07-18, against HEAD 83c0382. Objects: the pin
`v10/note-d42b7-second-grammar-and-dimension-pilot.md` (e952dc4, #301),
the receipt `v10/code/d42b7_second_grammar_exact.py`, the output
`v10/data/d42b7_second_grammar_exact.out` (#313), read against
note-d41b (the Bin U/T/X protocol this round executes), note-d42a
§2 + A1–A8 (the grammar text G3 varies), the committed
`v10/code/d42b3_placement_exact.py` (the exec'd layer source and its
gated anchors), note-d42b2 B2 (the triangle as declared abstract
control), the d42b1-F3 / d42a-F1 / d42b4-B1 conviction classes, and
LOG #301/#313. Method: 4 reruns (plain + PYTHONHASHSEED 0, 7,
20260718), byte-compared to the committed .out; a FROM-SCRATCH
rebuild of the A1–A8 semantics (own poset, own views, own
admissibility and weights, own kernels, own SUPERSET candidate
generator — all prop-subsets x all winner subsets, strictly wider
than the receipt's full-view-live filter) compared exactly against
the receipt's candidate caches at every history of both families; a
mechanical normalized diff of the two overridden functions against
the d42b3 originals plus a behavioral drive of the binary override
against the original committed functions; the four missing pinned
gates run by the referee; a 3-actor pre-verification of the GG4
repair; and a five-mutant battery. Scripts in the session scratchpad
(`d42b7/verify_main.py`, `verify_3actor.py`, `make_mutants.py`,
`mutant_A..E.py`). Nothing in the repo modified except this file.

## VERDICT: 1 BLOCKER / 3 MAJOR / 3 minor / 1 nit

**Every internally printed number reproduces exactly, twice over**
(receipt rerun byte-identical on all seeds; my independent rebuild
reproduces 215/405, the 12 and the 4, 1/64 and 1/144, both ladder
spectra, the 1/3-uniform triangle and the 2/3-vs-1/2 path by my own
3!-order tally, 386/771 and 290/579 by my own mu-weighted count, and
the chain's exact 1). The isolation claim — the round's foundation —
is CONFIRMED at both the textual and the behavioral level (§2). The
zero-false-numbers streak holds at seven rounds.

What does not hold is, once again, the relation between what is
CLAIMED and what is COMPUTED:

- **B1 (GG5):** the bin table — the d41b protocol's own deliverable —
  prints "LIFTED (2-of-2)" for claims whose second-grammar gates
  never ran in this or any committed receipt (opportunity-generation
  iff-sweeps, the quarter DENSITY, the L1-uniqueness census), behind
  a literal `check(..., True)`. The table's STATUS column is partly
  unearned; the protocol's currency is exactly that column.
- **M1 (GG4):** the pin says GENERATED triangle (§2-N1 and §4-GG4,
  verbatim); the receipt hand-constructs the triple (its own comment
  admits it) — the two-actor depth-3 family cannot contain a
  three-proposal component. Same for the "generated path" in G3.
- **M2 (GG3):** of the pinned GG3 battery ("iff-sweeps, ladder +
  density, ratio locality, L1-uniqueness census") the receipt
  implements the ladder alone — the d42b1-F3 class, fourth
  recurrence.
- **M3 (anchors):** no count, spectrum, or fraction is gated; two
  mutants that break the kernel law and delete the A7 blind
  pair-arbitration outright run 6/6 GREEN.

The saving grace, and it is substantial: I ran every missing gate
myself and pre-verified the GG4 repair in full — **every absent
computation comes back green** (§6). The findings are
claim-provenance defects, not false physics. On R1–R4 the round's
headline survives with its content strengthened.

---

## 1. Reproduction inventory (referee values, all exact)

| Object | Receipt prints | My rebuild | Verdict |
|---|---|---|---|
| binary family (depth<=3) | 215 | 215 (depth-hist 1/6/32/176) | CONFIRMED; = d42b3's gated interior 215 |
| ternary family | 405 | 405 (1/8/52/344) | CONFIRMED |
| GG1 points | 93 | 93 = 61 identity + 32 nontrivial swaps | CONFIRMED, de-inflated (F5) |
| depth-2 conflict census | 12 (ternary gated; binary 4 label-only) | 12 and 4, own rule; hand-derivation 2x6 / 2x2; all cross-actor propose-propose on V0 | CONFIRMED (F7 on the 4) |
| mu(seed) | 1/144, 1/64 | 1/144, 1/64 (own admissibility chain) | CONFIRMED |
| ladder spectra | {1: 374, 5/4: 56} / {1: 642, 5/4: 168} | identical, own counter; actor-points 430/810 = 2x families | CONFIRMED |
| density (UNGATED) | — | tot == 1 + k/4 with EVERY blind group == 1/4 exactly, family-wide, both grammars; k-spec {0: 374, 1: 56} / {0: 642, 1: 168} | TRUE, receipt never checks it (M2) |
| triangle | 3 MIS at 1/3 | own 3!-greedy tally: K1 = 1/3 each, support == MIS set, all singletons; K2 uniform 1/3 | CONFIRMED (constructed — M1) |
| path | K1 2/3 vs K2 1/2 | own tally: {P,R} 2/3, {Q} 1/3; 2 MIS | CONFIRMED (constructed — M1) |
| ordering fractions | 386/771, 290/579, chain 1 | identical, own mu-weighted computation; wsum = 257/32, 193/24; chain in-family with mu = 3/128 | CONFIRMED (anatomy in §4) |
| exit / seeds | 0; "0/83" | exit 0; byte-identical plain + 3 seeds | CONFIRMED (4-seed sample) |

## 2. The isolation claim (attack a) — CONFIRMED, both levels

The standing conviction class (hidden inequivalent relation smuggled
in through a "same text" claim) does NOT recur here. Three
independent certifications:

1. **Textual.** Mechanical normalized diff of the two reimplemented
   bodies (receipt lines 34–43, 46–81) against the d42b3 originals
   (lines 142–150, 185–218): after rewriting `ns['X']` -> `X`,
   removing the captured `vname = ns['vname']` alias, and mapping
   `for x in payloads` -> `for x in (0, 1)`, both bodies are
   CHARACTER-IDENTICAL modulo whitespace. Nothing else differs — no
   filter, no reordering, no changed relation.
2. **Behavioral, against the committed originals.** I exec'd the
   d42b3 head unmodified and drove the ORIGINAL `candidates_for`
   at all 215 binary histories against the override's cache:
   0 mismatches (events AND exact weights); the original-enumerated
   depth<=3 family is identical as a set. The binary layer of this
   receipt IS the committed d42b3 layer.
3. **Behavioral, against a true superset generator.** My rebuild
   generates arb candidates from ALL subsets of ALL prop triples in
   the record (live or resolved) x all winner subsets — strictly
   wider than the receipt's full-view-live filter — plus all
   constructible (base, payload) proposals, and filters by my own
   past-local admissibility. At every history of BOTH families the
   resulting (event, weight) sets equal the receipt's caches exactly
   (215 + 405 histories, 0 mismatches). So the full-view generator
   misses nothing past-locally admissible at these depths, i.e. the
   A7 superset-generator condition holds here (note: this is
   depth-contingent — sight of a proposal implies sight of its
   resolution only because every joint event resolves what it
   joins; at d42b1-style depths with transport this needs re-proof).
4. **Liveness.** Mutant A (G3 built with payloads (0,1)) exits 1 at
   GG2 (census 4, mu 1/64) — the gates DO see the varied structure;
   the layer separation is not decorative.

The exec-head hygiene is sound: `_head` cuts at the unique
`print("[d42b3` banner, contains every def through `mu_of` and no
executable tail; the d42b3 head contains EXACTLY two payload
hardcode sites, and both are the overridden functions (grep-counted).
One irony recorded as part of F8: the receipt binds
`base_prop`/`base_cand` (lines 33, 45) as if to compare override
against original — and never uses them. The comparison those dead
bindings gesture at is precisely the isolation GATE the receipt
lacks; I had to run it externally.

## 3. Findings

### B1 (BLOCKER, CONFIRMED) — GG5: the protocol deliverable asserts
### unearned instantiation status behind `check(True)`

Receipt lines 209–222: the bin table is print-only prose sealed by
`check("GG5 the bin table printed: ...", True, "table above")` — the
literal cannot-fail gate, the conviction class of six prior rounds,
now placed on the round's DELIVERABLE. Row-by-row against what
actually ran:

| Row | Printed | Actually gated in-receipt | Referee verdict |
|---|---|---|---|
| opportunity generation / closure | LIFTED (2-of-2) | GG1 = candidate-set equality on a depth<=2 slice ONLY; iff-sweeps: NOWHERE | unearned as printed; TRUE (my §6 runs) |
| 1+k/4 ladder + quarter density | LIFTED (2-of-2) | ladder only (quarter-multiples + tot >= 1); density: NOWHERE | half-unearned; density TRUE (my run) |
| L1 uniqueness | LIFTED (2-of-2) | NOTHING ran; A8 argument is genuinely payload-blind | unearned as "2-of-2"; census TRUE (my run) |
| depth-2 census 4 vs 12 | TOY-RELATIVE | 12 gated; the 4 never recomputed for this layer | sound via carry (F7); verified 4 |
| mu(seed) | TOY-RELATIVE | both gated (GG2) | EARNED |
| triangle realizability no vs yes | TOY-RELATIVE | NOTHING ran in either grammar in this receipt | unearned; TRUE (my §6.5) |
| K1-vs-K2 discrimination | SHAPE-DEPENDENT | GG4 (constructed objects — M1) | earned modulo M1 |

Why BLOCKER and not MAJOR: this round IS the d41b protocol
execution, and the protocol's whole content is the movement of
claims between "argued, single-grammar" and "twice-instantiated" —
d41b's closing rule is explicit ("No Bin-U claim enters a paper's
abstract without either the second instantiation or the explicit
'argued, single-grammar' label"). A table that prints "(2-of-2)"
for gates that never executed corrupts the exact ledger the
protocol exists to keep, and it does so behind the one gate form
this campaign has convicted six times. That every row's CONTENT is
true (I ran them all — §6) makes the repair wiring rather than
retraction; it does not make the printed status earned.

### M1 (MAJOR, CONFIRMED) — GG4: pinned GENERATED, delivered
### CONSTRUCTED (headline-wider-than-computation, sixth recurrence)

Pin §2-N1: "on the GENERATED triangle (payloads 0,1,2)"; pin §4-GG4:
"the GENERATED triangle exists in G3 with K1 == K2 == 1/3". The
receipt (lines 184–199) builds `tri` by hand directly on triples —
its own comment says "the ternary triangle needs 3 actors; construct
directly on triples" — and equally hand-builds the path. Facts:

- The enumerated families are TWO-actor. By L1/A8 (one live proposal
  per (actor, base)) a three-proposal component needs three actors:
  the pinned object CANNOT exist in the family the receipt
  enumerates. The existence clause of GG4 as pinned is not tested by
  the receipt at all — the check verifies kernel arithmetic on a
  supplied graph, which is exactly d42b2-B2's declared ABSTRACT
  CONTROL, while the pin promised d42b2's "boundary control becomes
  in-grammar" as the V1 upgrade. The receipt silently re-delivers
  the d42b2 object under the pinned upgrade's headline, with no
  forward-correction recorded (the A5'/A7' convention exists for
  precisely this).
- `et_tri` is hardcoded as the complete graph rather than derived
  from the conflict rule (payload inequality); it coincides here
  because 0,1,2 pairwise differ — certified by direct comparison —
  but the construction does not track the rule it claims to
  instantiate (the path's `et_path` does; the asymmetry is F8).
- The "in BOTH grammars" clause for the path rests on the kernels
  being alphabet-blind (true — one computation serves both), but
  neither grammar's path is generated anywhere in this receipt; the
  binary generation lives in d42a ARM-2 (committed), the ternary
  generation lived nowhere until this review.

**Repair pre-verified in full (referee, both routes — my rebuild AND
the receipt's own `make_layer`/`enum_family`, which are already
actor-generic):** 3-actor depth-3 enumeration, both alphabets
(binary 724, ternary 1,471 histories). Ternary: generated K3
components exist — census EXACTLY 36 histories (6 payload bijections
x 3! orders), each with mu = 1/1728, total K3 mass 1/48; the pinned
witness [pA0, pB1, pC2] is in-family; EVERY generated triangle
component is kernel-degenerate with K1 == K2 == uniform 1/3 over 3
singleton MIS; the kernel click on the generated triangle is
admissible at depth 4 with weight exactly 1/12. Binary control: ZERO
K3 components (pigeonhole: three pairwise-differing payloads need
alphabet >= 3 — this also makes the bin-table row's binary "no"
airtight as an argument). Paths: GENERATED in both grammars (36
binary / 108 ternary component instances), every one discriminating
K1(ends) = 2/3 vs K2 = 1/2. N1 as pinned is TRUE and now
instantiated; the receipt just never computed it.

### M2 (MAJOR, CONFIRMED) — GG3: the pinned battery is one-quarter
### delivered (the d42b1-F3 class)

Pin §4: "GG3 the U1 forms: iff-sweeps, ladder + density (zero
violations, both grammars), ratio locality, L1-uniqueness census."
Receipt GG3 (lines 162–180): the ladder alone — and the ladder check
itself gates only `tot >= 1` and quarter-quantization of the excess,
NOT the pinned density law (component-additivity: k = #blind ckey
groups with EVERY group summing to exactly 1/4). The full
pinned-but-undischarged list for this round (attack g):

1. pair/component iff-sweeps — absent (both grammars);
2. quarter DENSITY (per-group 1/4, component-additive) — absent;
3. ratio locality (L1) — absent;
4. L1-uniqueness census — absent (A8 argument correctly
   payload-blind, but the pin promised the census);
5. per-observer fork-freeness sweep (pin §2-U1) — absent;
6. extension closure beyond the depth<=2 candidate-set slice — absent
   (F5);
7. the ordering-fraction SPECTRUM (pin §3) — absent; a single mean is
   printed (F6);
8. the shape census behind "triangles REALIZABLE in G3" (pin §2-V1)
   — absent (M1).

Items 1–5 all PASS when actually run (referee, §6): iff-sweep 0
violations both grammars; density 0 violations family-wide with
k-spectra {0: 374, 1: 56} / {0: 642, 1: 168}; ratio-locality port of
d42b3 G-L1: binary 28 tested / 0 violations, ternary 90 / 0;
L1-uniqueness 0; fork-freeness 0. The bin table (B1) then prints
LIFTED for rows 1, 3 on the strength of gates in this list that do
not exist.

### M3 (MAJOR, CONFIRMED by mutation) — nothing structural is
### anchored: two inequivalent grammars run 6/6 GREEN

The receipt gates values (12, 1/144, 1/64, 1/3, 2/3, 1/2, chain 1)
and ranges (0 < OF < 1), but NOT ONE structural anchor: family
counts, ladder spectra, k-spectra, and both OF values are printed
[MEASURED] and never gated. d42b3 — the layer this receipt exec's —
gated its anchors (215, 427, 202, 36, 114, 21). Consequences,
demonstrated on scratch copies:

- **Mutant B (kernel-law break, support-preserving):** scale the two
  winner weights of every 2-component 3/2 vs 1/2 (group sums and
  actor totals preserved; winner ratio 1:1 -> 3:1, i.e. a DIFFERENT
  kernel law). Result: **6/6 PASS, exit 0, gate lines byte-identical
  to the committed .out.** No gate in the receipt touches the arb
  sector's weight LAW in either grammar (GG2's two factors are
  propose-sector; GG4 recomputes PK1 from scratch on supplied
  graphs; GG6 uses mu_of, not the caches).
- **Mutant E (opportunity-relation break):** generate only the
  full-winner-set arb per component (sub-MIS winners dropped) — this
  DELETES pair arbitration wholesale, i.e. the A7 blind-pricing
  structure that is d42a's central discovery. Result: **6/6 PASS,
  exit 0**, printing families 199/357, spectra {1: 398}/{1: 714}
  (the entire 5/4 spectrum GONE), OF = 1/2 exactly in both grammars.
  A grammar with NO conflict resolution of pairs — materially
  inequivalent to the pin — passes every gate; the difference
  survives only in ungated prints.
- **Credit where due — mutant C (component-filter break):** generate
  arbs only for the full live set per base. CAUGHT: exit 1 at GG3,
  spectra grow 3/4 entries (56 binary / 84 ternary). Anatomy: at
  co-authorship pairs (same payload, two singleton components) the
  full-set ckey is not a component, so BOTH self-arbs vanish while
  idle still prices the arb sector open in the past view — tot
  drops to 3/4 < 1. The generator-vs-idle-pricing cross-check gives
  the ladder real teeth against opportunity DELETION in the
  own-view sector; it is blind to deletion in the blind sector
  (mutant E: the deleted 1/4 was the excess itself, so tot falls
  back exactly to 1) and to any support-preserving re-weighting
  (mutant B). Gate-integrity controls: mutant A exit 1 (GG2),
  mutant D (GG4 target 1/3 -> 1/4) exit 1 — the exit-1 plumbing is
  live.

### F5 (minor, CONFIRMED) — GG1: 93 points are 61 reflexive + 32
### real; "closure" names a check the gate does not perform

The 93 candidate-set points decompose as 61 identity extensions
(depth<=1 histories have one linear extension each; 20 comparable
depth-2 histories likewise) + 32 nontrivial swaps (the 32 cross-actor
depth-2 histories) — hand-derivation reproduced: 52 depth-2
histories = 6x6 + 2x8, of which 32 incomparable. The gate compares
candidate SETS across reorderings; it never checks that a reordered
history is IN-FAMILY (A7(i)'s actual closure clause, which the d42a
terminal receipt gated at its witness points alongside the
invariance battery), and never checks mu invariance. The pin did
declare the slice ("on the declared slice"), so the depth cap
itself is pinned; the label word "closure" is not backed by the
computation. Referee full-depth run (both grammars, ALL histories,
every linear extension): binary 501 points (286 nontrivial), ternary
965 (560 nontrivial) — 0 missing from family, 0 candidate-set
violations, 0 mu violations. True at full depth; gated at a third of
one grammar's slice.

### F6 (minor, CONFIRMED) — GG6: the pilot's one dynamical number is
### already fixed by GG2; the label decorates a cannot-fail clause

Anatomy of the measured means (referee decomposition, exact):
the depth-3 OF distribution is THREE-POINT in both grammars —
support {1/3, 2/3, 1} with unnormalized mu-masses

- binary: {1/3: 6, 2/3: 1/32, 1: 2}, wsum = 257/32;
- ternary: {1/3: 6, 2/3: 1/24, 1: 2}, wsum = 193/24.

The 1/3 bin is mixed-actor-no-join (mass 6 in BOTH grammars), the
1 bin is single-actor (mass 2 in both), and the ENTIRE
binary-ternary difference is the 2/3 bin = the pair-arb join mass
(16 histories x 1/512 = 1/32 vs 48 x 1/1152 = 1/24) — which is the
GG2 census times the arb weight. Equivalently OF − 1/2 = 1/1542
resp. 1/1158, and mutant E (joins deleted) lands on 1/2 EXACTLY in
both grammars. So at this depth the pilot is an affine readout of
already-gated quantities; its honest new content is the exact join
masses, which the receipt does not print (the pinned "spectrum"
would have carried them; only the mean is printed). Further:
"generated adjacency sits strictly below" (gate text, line 248) is
entailed by census > 0 plus idle positivity — a cannot-fail clause
on a declared verdict-free pilot (142 binary / 288 ternary depth-3
histories carry an incomparable pair); and the "STATIC chain
baseline" is itself an in-family generated history (mu = 3/128), so
the pilot compares generated-vs-generated-serial and does not
instantiate paper 20's static-vs-dynamic fork — fine for a declared
pilot, wrong to read as the fork's first data point. The pin's
verdict-free scope (§3) is honored by the gate structure; the label
dressing is not free.

### F7 (minor, CONFIRMED) — the binary half of GG2's headline is
### carried, not computed

"4 -> 12" and "1/64 -> 1/144": the receipt gates 12, 1/144 AND 1/64,
but never recomputes the binary census 4 for the layer it actually
runs (the reimplemented one). The carry is SOUND — §2 proves the
layer identical to committed d42b3, and the 4 is gated upstream
(d42a G2a) — but the receipt's banner claims the values exhibited,
and one of the four is exhibited nowhere in it. Referee value: 4
(own rule, 1 line). Fold into R4.

### F8 (nit bundle) — dead and misdirected text

(i) `base_prop` (line 33), `base_cand` (line 45): dead bindings that
mime the original-vs-override comparison the receipt never performs
(see §2 — recommended: make them the isolation gate). (ii) `h3`
(line 184) unused. (iii) `et_tri` hardcodes K3 instead of deriving
edges from the payload rule as `et_path` does (coincides here;
certified). (iv) `spectrum()` returns a mean, not a spectrum.
(v) GG6's well-definedness gates "weights positive / spectra
nonempty" (pin §3) exist only as crash-by-ZeroDivision, unlabeled.

## 4. Attack summary against the brief

- (a) isolation: CLEAN — textual + behavioral + superset
  certification, §2; binary override == committed originals at all
  215 histories; mutant A proves gate liveness.
- (b) GG1 slice: content true at full depth (referee), gate covers
  32 nontrivial points of one grammar and omits the membership half
  of closure — F5. Extension-closure of the ternary family: checked
  NOWHERE in the receipt; checked HERE (965 points, 0 violations).
- (c) census 12: hand-derivation 2 orders x 6 ordered payload pairs
  confirmed; the `view.edges(set(view.props))` line is correct and
  robust over arb/idle-containing depth-2 histories (verified by
  direct sweep; `set(view.props)` is the prop-index set, edges
  requires both-props/same-base/differing-payload/incomparable).
- (d) GG4: constructed != pinned GENERATED — M1; repair pre-verified
  (36-triangle census, mass 1/48, degenerate everywhere; binary 0).
- (e) GG5: B1 — row-by-row audit above; mechanical version in R3.
- (f) GG6: F6 — three-point distribution, join-mass anatomy,
  cannot-fail "strictly below", in-family chain.
- (g) pinned-but-undischarged: the eight-item list in M2.

## 5. Plumbing

- Reruns byte-identical to the committed .out: plain, seeds 0, 7,
  20260718; exit 0. (LOG's 0/83 claim: sampled 4/4 here.)
- Exit-1 path live: mutants A, C, D all exit 1 with [VERDICT] FAIL.
- Worktree clean at HEAD for all three objects; pin commit e952dc4
  verified to introduce the pin text (#301) before the receipt
  (#313, 83c0382); receipt docstring's pin reference matches.
- Exec-head hygiene sound (§2): unique cut marker, defs-only head,
  exactly two payload hardcode sites, both overridden; the two
  `make_layer` namespaces share only the immutable V0.
- Determinism by construction (sorted iteration everywhere;
  frozenset-keyed dicts only printed after sorting) — consistent
  with the 4-seed byte-identity.

## 6. What survives (all referee-verified, most now TWICE-computed)

1. **The isolation construction** — the round's method: one text,
   one varied structure, certified three ways (§2).
2. **V1 toy-relativity, exhibited exactly:** census 4 -> 12
   (2x2 -> 2x6, all cross-actor propose-propose on V0), mu(seed)
   1/64 -> 1/144 (propose split 1/8 -> 1/12).
3. **The U1 ladder lift, and MORE than the receipt claims:** both
   spectra reproduced ({1: 374, 5/4: 56} / {1: 642, 5/4: 168});
   the FULL pinned density law verified family-wide in both
   grammars by the referee — tot == 1 + k/4 with every blind group
   exactly 1/4, k-spectra {0: 374, 1: 56} / {0: 642, 1: 168}. The
   ladder's load-bearing depth cap (<= 3) is declared in the
   banner; the d42b1-h12 general-depth breakage is a
   transport-grammar fact and does not contradict this slice.
4. **Every missing pinned gate passes when run:** iff-sweeps (0/0),
   L1-uniqueness (0/0), per-observer fork-freeness (0/0), ratio
   locality (28 and 90 tested, 0/0), full-depth closure + mu
   invariance (501/965 points, 0 violations).
5. **N1, now GENERATED (the review's main positive delta):** the
   3-actor depth-3 run realizes d42b2-B2's prediction in-grammar —
   36 ternary K3 histories (each mu = 1/1728, mass 1/48), every
   generated triangle kernel-degenerate at K1 == K2 == uniform 1/3;
   binary K3 count 0 (pigeonhole); generated paths in BOTH grammars
   (36/108) all discriminating 2/3 vs 1/2; the triangle's kernel
   click admissible at depth 4 with weight 1/12.
   Component-shape-dependence of K-discrimination STANDS, upgraded
   from constructed to generated.
6. **The dimension pilot's numbers and its declared verdict-freedom:**
   386/771, 290/579, chain exactly 1; plus the referee anatomy (F6)
   that should become its printed content: three-point spectrum,
   join masses 1/32 vs 1/24, OF − 1/2 = 1/1542 vs 1/1158.
7. **Plumbing** (§5), including one genuine robustness discovery:
   the ladder's tot >= 1 clause cross-checks the generator against
   past-view idle pricing and catches own-sector opportunity
   deletion (mutant C).

## 7. Prescribed repairs (all pre-verified this review)

- **R1 (M1, the flagship).** Add the 3-actor depth-3 enumeration for
  both alphabets through the receipt's own `make_layer`/`enum_family`
  (they are already actor-generic; ~25 lines). Gate: ternary K3
  census == 36 with per-history mu == 1/1728 and mass == 1/48;
  kernel degeneracy (3 singleton MIS, K1 == 1/3 each, support ==
  MIS) on EVERY generated triangle; binary K3 == 0; generated-path
  censuses 36/108 with K1(ends) == 2/3 and |MIS| == 2 on every one;
  the depth-4 click spot check (q == 1/12). This discharges pin
  §2-N1/§4-GG4 as written AND the §2-V1 shape-census clause, and
  turns the bin table's triangle row mechanical. (Alternative — an
  A5'-style re-scope amendment demoting GENERATED to CONSTRUCTED —
  is strictly worse: the generated computation is green and costs
  ~1 s.)
- **R2 (M2).** Port the four missing gates; every one is a short
  loop verified green here: density (tot == 1 + k/4, every blind
  group == 1/4 — my counter is ~20 lines and subsumes the current
  ladder check), the pair iff-sweep, the L1-uniqueness census, the
  fork-freeness sweep, the G-L1 ratio-locality port (ternary seeds
  [pA0], [pA1], [pA2]).
- **R3 (B1).** Make the bin table mechanical: build each row from
  the flag of the gate that earned it or an explicit tag —
  [ARGUED: A8] (permitted by d41b for the argument half),
  [CARRIED: d42a G2a] (or recompute the 4: one line), [R1], [R2] —
  and gate `check("GG5", all(row_flags))` instead of
  `check(..., True)`. Rows whose gates fail must print DEMOTED, per
  the d41b FAIL branch.
- **R4 (M3).** Gate the anchors: len(FAM2) == 215, len(FAM3) == 405,
  both ladder spectra dicts, both k-spectra, OF == 386/771 and
  290/579 (mutants B and E then exit 1; the true values are
  seed-stable). Print the OF distribution (it is the pinned
  spectrum) — the join masses 1/32 vs 1/24 are the pilot's actual
  finding.
- **R5 (F8/F6).** Delete or use the dead bindings — recommended USE:
  an in-receipt isolation gate asserting override == original at
  all 215 binary histories (~6 lines; §2.2 shows it passes); derive
  `et_tri` from the payload rule; rename `spectrum` or make it one;
  label the GG6 well-definedness crashes as gates.

## 8. Reproduction inventory

- Reruns: `python3 v10/code/d42b7_second_grammar_exact.py` (plain;
  PYTHONHASHSEED 0, 7, 20260718) -> byte-identical to committed
  .out, exit 0, 6/6.
- `verify_main.py` (scratchpad): 25 referee checks, ALL OK — head
  hygiene; hardcode census; families + depth histograms; Tier-2
  superset rebuild == caches (620 histories, 0 mismatches);
  original-d42b3 drive (0 mismatches, family identical); censuses
  4/12 + hand-derivations + robustness sweep; mu seeds; ladder
  spectra + full density law; full-depth closure (501/965 pts);
  GG1 accounting (61 + 32); kernel tallies (triangle, path,
  et_tri coincidence); OF values + wsum + decomposition + 3-point
  distributions; chain in-family (mu 3/128); strictly-below
  entailment counts (142/288); iff-sweep; L1 census; fork sweep;
  ratio-locality port (28/90, 0/0).
- `verify_3actor.py`: 6 checks, ALL OK — 3-actor families 724/1471;
  K3 census 36 / mass 1/48 / witness in-family; degeneracy on every
  generated triangle; binary 0 + paths 36/108; path discrimination
  everywhere; depth-4 click q = 1/12.
- Mutants: A exit 1 (GG2 catches the alphabet), B exit 0 (kernel
  law UNGATED), C exit 1 (ladder catches own-sector deletion,
  spectra 3/4 x 56/84), D exit 1 (gate integrity), E exit 0 (blind
  pair-arbitration deleted, families 199/357, OF exactly 1/2 —
  anchors UNGATED).

**Disposition:** the mathematics of this round is fully confirmed
and in several places strengthened by the review's own runs; the
convictions are all in the claim/computation seam: the deliverable
table's unearned status column (B1), the constructed-for-generated
substitution (M1), the one-quarter-delivered gate battery (M2), and
the unanchored structure (M3). On R1–R4 — every ingredient of which
ran green here — d42b7's headline stands as: forms lift two-of-two
WITH the density, values toy-relative as predicted, kernel
degeneracy GENERATED in G3, discrimination component-shape-
dependent, and a dimension pilot whose honest content is the exact
join masses. The named next fronts inherit: the carrier-level third
grammar (pin §5), the superset-generator condition at transport
depths (§2.3's caveat), and h12's standing general-depth ladder
constraint.
