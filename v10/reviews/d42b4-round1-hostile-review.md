# D42b4 round 1 — hostile review (pin + receipt + out)

**Reviewer round:** 2026-07-18, against HEAD d102e0e. Objects: the pin
`v10/note-d42b4-quantum-lift.md` (#308), the receipt
`v10/code/d42b4_quantum_lift_exact.py`, the output
`v10/data/d42b4_quantum_lift_exact.out` (#309), read against the d42b3
DECIDED trilemma (note §4 D1–D7 + `reviews/d42b3-round1-hostile-review.md`
incl. the TS-system computation and the delta), d42b2 §5 (B1 click
semantics, the fine-vs-coarse deferral), d42b1 §§2–6 (record types, budgets,
h12), note-d42a A1–A8 + A5' + the committed d42a machinery itself, D23's
actual statement (paper 18 / note-d23), the d41d-R3 negative-control
standard, and LOG #308–#309. Method: 3 reruns (PYTHONHASHSEED 0, 61, 71);
a full independent Fraction/mpmath-dps-80 recomputation of every printed
number plus complete censuses the receipt samples (28/28 checks green); a
four-mutation battery on scratch copies; and — the centerpiece — a
ground-truth extraction of the d42a menus at the A7 cuts via the committed
`candidates_for`/`admissible`/`mu_of`, feeding a pre-verification of the
flagship repair. Scripts in the session scratchpad (`verify_d42b4.py`,
`mut1..4.py`). Nothing in the repo modified except this file.

## VERDICT: 2 BLOCKER / 4 MAJOR / 2 minor / 2 nit

**Every internally printed number reproduces exactly** (2/3 and 1/3; the
1/6 and the 0; overlap 1; 19 record words; Z = 15/4 *of the coded family*;
34 sampled ratio pairs; the control value 0.2599... = 1/√2 − 1/√5 exact;
all norms; byte-identical reruns on three seeds; exit-1 plumbing fires on
expectation breakage). The zero-false-internal-numbers streak holds. What
does NOT hold is the round's claim structure, at its foundation:

- **B1:** the "impossible combination" the receipt exhibits (GLOBAL
  normalization + COMPLETE-HISTORY ratio preservation) is not the
  combination d42b3 decided impossible (PER-CUT normalization +
  WITHIN-CUT ratio preservation) — and the exhibited combination is
  achieved CLASSICALLY by d42b3's own gradient completion at unit
  boundary. The lift, as computed, is the classical completion in
  Hilbert dress; the burden is not discharged.
- **B2:** the foliation-invariance-by-operator-identity claim is backed
  by a gate that is scalar commutativity (it passes for arbitrary,
  even non-isometric inputs — mutation-proved), covering one trivial
  pair; and at the A7 cut where the trilemma actually bites, the
  pinned disjoint-carrier mechanism is REFUTED by the grammar's own
  arithmetic (menus 1 vs 5/4; branch sets differ across the diamond's
  two intermediate cuts — pre-verified from the committed d42a code).

Two of the five prior rounds' failure classes recur here in strengthened
form: gate theater (the d42b3-F1 "declaration wearing a gate" class, now
with a literally unfalsifiable gate) and claim-wider-than-computation at
the round's central sentence. A third class is NEW: the first
pricing-level false attribution — the F-PAIR family is not the d42a slice
it is printed as, and its post-proposal idle implements the exact value
A5' refuted, citing A5' for it.

---

## THE DECIDED TRILEMMA vs THE EXHIBITED COMBINATION (the B1 anatomy)

What d42b3 decided (pin §4 D1, referee-computed both ways, on record):

- A placement completion = **cut-attached** Z with transfer
  q′(e|h) = q·Z(h+e)/Z(h), required (a) **per-cut normalized** (Σ q′ = 1
  at every cut) and (b) foliation-invariant.
- **Ratio-preserving** there means: **within-cut** transfer ratios
  untouched. That class is REFUTED (Z = N forced; 36/202 diamonds).
- The **gradient** class is SOLVED at every finite depth — and, decisive
  for this round: with unit boundary its completed weight is
  P(H) = mu(H)·Z(∅), i.e. it **preserves every COMPLETE-HISTORY
  mu-ratio exactly** (that is literally how the A7 witness pair
  "equalizes at 1/2074" — both weights are proportional to the equal
  mus). Its unavoidable price is WITHIN-cut deformation (21/114
  interior cut classes, root included).

What the receipt exhibits (QG2b/QG7b, the self-declared discharge):

- A state whose Born diagonal is w_mu/Z with Z = Σ w_mu computed and
  **divided out** (lines 215–220: `Zc = sum(...)`, `psi2[i]/nrm`) — the
  flat pushforward, verbatim, wearing square roots. Normalization is by
  explicit global division, not "by unitarity": no unitary or isometric
  circuit producing psi2 exists anywhere in the receipt.
- Ratio checks on **complete words only**. No within-cut conditional is
  ever computed (on F-PAIR it could not be: the word basis integrates
  the interleaving out, so order-mixed cuts are not even representable
  in the state space — see F4).

Consequence, exact: the combination gated — globally normalized +
foliation-invariant + complete-history-ratio-preserving — is satisfied by
the CLASSICAL gradient completion at unit boundary (d42b3's own class-(c)
solution), and on this fixture the lift's Born measure IS that
completion's endpoint measure (Born = w_mu/Σ w_mu = mu·Z(∅) with unit
boundary at the truncation). Wherever a cut algebra is representable, the
conditionals extracted from this measure by projection are mass-ratio
conditionals — the h-transform — so the lift inherits exactly the decided
within-cut deformation; it does not evade the refuted leg, it never
touches it. The printed sentence

> "ratio-preserving + normalized SIMULTANEOUSLY, which d42b3 proved
> impossible for any classical cut-attached completion"

is therefore false as printed: d42b3 proved that combination impossible
only under the WITHIN-CUT reading of "ratio-preserving" and the PER-CUT
reading of "normalized"; under the readings the receipt instantiates, its
own base round exhibits a classical object with the same diagonal. The
verdict line and LOG #309 ("THE BURDEN DISCHARGED AT FIXTURE SCALE")
inherit this. The d42b3-D7 hand-off was precise — "the lift is the only
ratio-preserving normalized completion CANDIDATE — exhibiting it is
d42b4's burden" — and the thing exhibited is not that candidate.

**Mutation proof of the gate's vacuity (mut2):** replacing the entire
classical pricing (1/8 → 1/7, 1/2 → 2/5, 3/4 → 3/5) leaves the receipt
**7/7 GREEN, exit 0**. Born == w_mu/Z is an identity of the construction
for ANY weights; Z appears only in an ungated f-string detail. The
receipt cannot detect wholesale falsification of the measure it claims to
lift. (Contrast mut1, an expectation breakage, which correctly exits 1 —
the plumbing works; the gates just do not gate the claim.)

## F1 — BLOCKER (CONFIRMED): the trilemma-evasion claim is an
## equivocation; the exhibited object is classically available; the
## burden is not discharged

Full anatomy above. Convictions, each verified:

1. Equivocation on "ratio-preserving" (within-cut ↔ endpoint) and on
   "normalized" (per-cut ↔ global). The pin half-admits the second
   ("per-cut normalization is never imposed") while still claiming the
   decided-impossible combination is achieved.
2. The exhibited combination is classical: flat pushforward /
   unit-boundary gradient completion (both in d42b3's record; the
   review's F4 explicitly listed slice normalization as classical
   placement outside the cut-attached class).
3. "Normalized BY UNITARITY ... no cut-attached Z anywhere" (pin Q1) vs
   the code: Z_classical computed and divided out. "Absorbed by the
   state norm" = "divided out globally". The .out's QG7a label ("no cut
   data anywhere") is true only for F-PATH, where the classical chain is
   already per-cut normalized (uniform order lottery × deterministic
   winner) — i.e. exactly where the trilemma is vacuous.
4. mut2: 7/7 green under pricing sabotage — the discharge gate has zero
   discriminating power with respect to the program's measure.

**Classification:** the d42a-F1/d42b3-F1 severity class — the round's
self-declared centerpiece is not what the round claims. Zero false
internal numbers; the conviction is claims-vs-computation at the
foundation. Repair R1 (pre-verified arithmetic below).

## F2 — BLOCKER (CONFIRMED): claim (b) — foliation invariance BY
## OPERATOR IDENTITY — has an unfalsifiable gate, one trivial instance,
## and is refuted-as-stated at the A7 cut by the grammar's own pricing

Four convictions:

1. **The gate cannot fail.** QG1/QG3 builds `AB[i*d+j] = aamp*bamp` and
   `BA[i*d+j] = bamp*aamp` — the same elementwise scalar product with
   factors swapped. ||AB − BA|| = 0 by commutativity of mpf
   multiplication, for ANY inputs. Mutation mut3 (VB = step_iso(7/3,
   5/2, 9) — wildly non-isometric): **7/7 GREEN, exit 0** — the printed
   sentence "each step isometry is exactly norm-preserving" prints PASS
   over a map of squared norm 83/6, because `iso_ok` checks VA only. No
   operator is ever applied or composed in the entire receipt: the
   operator toolkit (`dag`, `mul`, `kron`, `eye`) and the very embedding
   maps that would have made this an operator statement (`embedA`,
   `embedB`, plus `initv`) are ALL dead code (verified: each symbol
   occurs exactly once, at its definition). "Operator-level, both
   application orders" — no application ever executes.
2. **Coverage: one pair, and the trivial one.** Pin QG1 quantifies over
   "all incomparable pairs"; pin QG3 promises "the A7-class gauge pair".
   The receipt checks the single pair (A's step-1 branch map, B's step-1
   branch map) from the empty cut — different actors, product state, no
   arb, no differing intermediate cuts: not A7-class. This is the one
   configuration where disjointness is definitional and the classical
   menus happen to sum to 1 (1/8 + 1/8 + 3/4).
3. **At the A7 cut the mechanism fails — pre-verified from the committed
   d42a code** (`candidates_for`/`admissible`, menus extracted and
   checked this round): A's non-proposal menu at [pA0] is
   {selfA 1/4, idle 3/4} — sum 1, the sqrt-branch map IS an isometry;
   at [pA0,pB1] it is {selfA 1/4, pair-arb 1/8, pair-arb 1/8, idle 3/4}
   — sum **5/4**, the sqrt-branch map is NOT an isometry, and the branch
   SET differs (the pair-arb branches exist only in the joined view, per
   A4). Hence: no cut-independent A-operator reproduces both menus; the
   pinned commutation-by-disjoint-carriers argument requires exactly
   such an operator on A's registers alone; an operator that grows the
   pair branches after pB1 must READ B's record (carrier overlap — the
   argument's premise dies); and dilating the 5/4 map to an isometry
   requires a renormalizer at exactly the T1 excess — cut-attached data
   reappearing, which is the trilemma, not its evasion. The pincer is
   exact: cut-independent ⇒ the pair-arb branches never enter ⇒ the
   d42b3-D3 zero-class completion ("abolishes joint arbitration");
   cut-dependent ⇒ disjointness gone and the commuting-family existence
   question is OPEN — it is the actor-factored/h12 constraint class in
   quantum dress, i.e. the successor problem, not a discharged one.
4. **"Decoherence functional ... foliation-invariant":** no decoherence
   functional (no class operators, no D(α,β)) is computed anywhere; the
   word appears only in labels.

**Grade:** BLOCKER — claim (b) is the lift's load-bearing leg (it is what
per-cut normalization was traded for), its only gate is vacuous, and the
honest minimal instance refutes the pinned mechanism. Repair R1/R4.

## F3 — MAJOR (CONFIRMED): the F-PAIR family is NOT the d42a slice it is
## printed as — the pricing implements the value A5' refuted (citing
## A5'), and the family excludes declared grammar

The receipt's header ("Classical family (d42a grammar, A/B on v0)") and
the printed "Z_classical = 15/4" attribute the family to d42a. Ground
truth, from the committed d42a machinery this round:

- **Post-proposal idle:** d42a = **3/4**. A5' (note-d42a §6) says in so
  many words that "1/2" was FALSE, "an arithmetic slip ... idle = 1 −
  1/4 = 3/4 via the open arb sector alone". The toy's `q_of` returns
  `Fr(1, 2)` with the comment "`# A5': own singleton visible`" — it
  implements the refuted value and cites its refutation as authority.
- **The singleton self-arb is declared grammar** (A5(ii); it is the A7
  witness's own middle event) with q = 1/4 at [pA0] — the toy's family
  has no arb events at all; its truncation comment ("Arbs need a live
  component; at depth 2 only after both proposals") is false against
  A5(ii): A's own singleton is a live component after A's proposal, and
  [pA0, selfA] is a depth-2 d42a history.
- **The true d42a depth-2 family:** 32 sequences, per-actor menus
  summing to 1 at every depth-≤1 cut, Z = **4**. The toy: 28 sequences,
  A-sum 1/2 at [pA0], Z = 15/4. On the shared support, 4 of 28 toy mus
  are wrong against d42a (e.g. (pA0, nA): toy 1/16 vs d42a 3/32); 4
  d42a sequences (self-arb continuations) are absent.
- Nor is it the d42b1 slice: there genesis idle is 1/2 (deliver sector
  open), not the toy's 3/4, and deliver events would appear.

The family is a chimera (d42a genesis idle + refuted-A5 post-proposal
idle + no arb/deliver sectors), matching NEITHER settled grammar. All
downstream F-PAIR quantities (19 words, Z = 15/4, the 34 ratios) are
correct numbers OF THE CHIMERA. First pricing-level false attribution of
the d42 line; the "d42a slice" sentence in pin §2 is false as printed.
(Because of F1's construction-tautology, the ratio gate would pass for
any family — which is how this went unnoticed; mut2 is the proof.)

## F4 — MAJOR (CONFIRMED): the F-PAIR aggregation is a third,
## underived convention that silently resolves the fine-vs-coarse
## question the same receipt declares EMPIRICAL

The pin's formula assigns "each complete depth-D history the amplitude
∏√q". On the toy family that formula does not determine the receipt's
object: a mixed record word has TWO linearizations, and the receipt sets
its amplitude to sqrt(mu₁ + mu₂) — probability-summed, then sqrt'd.
Verified exactly (my Part A): the three candidate conventions are
observably inequivalent —

- class-counted (one basis state per gauge class, amplitude ∏√q — the
  pin's formula read on canonical histories): Z = **11/4**, mixed/pure
  Born ratio = r;
- sequence-summed (the receipt): Z = **15/4**, ratio = 2r;
- coherent (unrecorded order, amplitudes added — the pin's formula read
  on sequences with a word basis): Z = **23/4**, ratio = 4r.

The receipt's choice equals the pushforward of the classical sequential
measure — i.e. the ORDER-SEALED (fine) ontology's class probability —
adopted silently, while QG5/QG6 celebrates that fine-vs-coarse "stays
EMPIRICAL". The two fixtures embody opposite resolutions of the same
question: F-PATH keeps the order coherent until an instrument choice;
F-PAIR integrates it out incoherently by fiat. Additionally, the
linearization count (1 for pure words, 2 for mixed) enters the Born
weights as a foliation-counting factor — the unpriced who-moves-next
choice, the d34a census-denominator ghost, now inside the "record word"
measure — unadjudicated and undeclared. And the aggregation erases the
cut algebra (order-mixed cuts are not representable on the word basis),
which is what makes the pin's "conditionals at cuts come from projection"
unimplementable on this fixture. A hidden choice equivalent to a
foliation-measure: confirmed.

## F5 — MAJOR (CONFIRMED): QG4's "per record type" is one shared toy map;
## the pin's per-type sweeps are not run; the verdict line drops the
## receipt's own qualifier

Pin Q2: "EACH record type's reception map (prop, arb-winner, delivery,
merge) is a distinguishability isometry: pairwise-distance preservation
swept per type". The receipt runs ONE reception form — basis-copy on C³ —
on one 5-probe family, and prints "prop/arb-winner/delivery/merge records
share this reception form — **declared**". The types do NOT share a
carrier/data structure (d42b1 §2: delivery is the two-wire event class,
carriers {s, r}, reception enters a joint register and transports the
sender's chain; merge updates supersession state; arb-winner data is
(ckey, wkey) at a join): whether those structured receptions are
distance-preserving isometries on their actual registers is exactly what
"per type" was pinned to test, and basis-copy on C³ is the trivial common
denominator that cannot see any of it. The gate label is honest
("declared"); the final [VERDICT] line is not: "NSE holds per record
type" — unqualified, the highest-visibility sentence, the exact D-M1
(stale/overclaiming verdict-line) class the last round convicted. The
positive content that does hold: the copy-reception preserves all 10
probe distances (verified) and the negative control genuinely fires
(0.2599... = 1/√2 − 1/√5 exact, a real d41d-R3-standard control).

## F6 — minor (CONFIRMED): the fine half of QG5/QG6 is not computed

`rho_o_fine` is `zeros(6,6)` with only the diagonal ever written;
`off_fine` reads an entry that was never assigned. "EXACTLY 0 under fine
(order) sealing" is gated as: an unwritten entry of a zero-initialized
matrix is zero. No copy-isometry instrument model is built. The claim is
mathematically true (my Part A computes it from the order-copy isometry:
cross terms vanish by ancilla orthogonality — two lines), so this is
gate-form, not substance — but it is the same theater pattern in
miniature: the discriminator's "0" arm is definitional, only its "1/6"
arm is computed from the state.

## F7 — minor (CONFIRMED): the fiber/coherence census is 1 of 15 pairs,
## and the pin's fiber sentence is numerically false

The {P,R} greedy fiber has **FOUR** orders (PQR, PRQ, RPQ, RQP — the
receipt's own `fiber_PR`, a dead variable, holds them); pin Q3's "the two
path orders mapping to {P,R}" is false as written. The receipt gates one
same-fiber pair. Complete census, verified exactly this round: all 7
same-fiber pairs (6 in the PR fiber + 1 in the Q fiber — the pin's
"same-winner" wording also misses that the Q fiber is a second instance)
have coarse coherence exactly 1/6; all 8 cross-fiber pairs are exactly 0;
all same-fiber conditional winner records identical, all cross-fiber
orthogonal. The full statement is TRUE and now anchored — the receipt
just did not compute it. QG5b itself is `greedy(PQR) == greedy(PRQ)` in
vector dress (line 94's assert already contains it). The D23 citation:
corpus-standard principle-naming (the in-degree ≥ 2 identifiability limit
is a standing phrase — d42-pin, d41, d37, README), acceptable as a pin
declaration; but the gate exhibits only deterministic non-invertibility
of the greedy map, not D23's actual mechanism (angle-addition breakage in
the controlled-rotation family) — the citation decorates, the gate does
not instantiate.

## F8 — MAJOR (CONFIRMED): undeclared pin-vs-receipt fixture drift, and a
## false scope banner

- Pin §2 F-PAIR: "depth <= 3 ... full history family ... both
  instruments." Receipt: depth ≤ 2, p/n-only (not full even at depth 2 —
  F3), and NO instrument is ever applied to F-PAIR.
- Pin §2 registers: "one qubit per proposal-payload record, one qudit
  per order click". Receipt: a 19-dim word simplex (no payload qubits);
  a single dim-6 order label (no per-click qudits — the CLICK CHAIN is
  never represented; d42b2's refinement enters nowhere). Docstring says
  "two qutrit-like registers"; the code builds DIM_O = 6.
- The .out banner: "Scope: the CONFLICT core lifted (proposals + arb +
  the click chain)". False on all three counts as a description of what
  was lifted: no grammar arb event is lifted anywhere (F-PAIR has no
  arbs; F-PATH's kernel is an abstract order lottery with no grammar
  embedding, no sector share, no proposal events); the click chain is
  not represented; the two fixtures share no register, state, or map, so
  their union is a gap, not a decomposition — the arb-in-grammar lift,
  the one case the burden is about, happens in neither. This is the
  assigned attack (d)'s suspicion, confirmed at the banner sentence.

## F9 — nit: eleven dead symbols; the linear-algebra apparatus never runs

`dag`, `mul`, `kron`, `eye`, the `matrix` import, `embedA`, `embedB`,
`initv`, `fiber_PR`, `mu_map`, `tot` — each occurs once (definition) or
feeds only another dead symbol. No matrix product, tensor product, or
adjoint executes in the receipt. d34a dead-code hygiene class — and here
the dead embeddings are also F2's evidence: the machinery that would have
made QG1/QG3 an operator statement was written and then not used.

## F10 — nit: QG2b's stride sampling (3, 4 over a repr-sorted list) is
## arbitrary; the full sweep is free

Verified: the 34 sampled pairs do cover all class-pair categories
(pureA/pureB/mixed crossings — no systematic class omission), 8 of 19
words untouched; the full 19×18 = 342 sweep passes (necessarily — F1's
identity). Replace the strides with the full sweep; it costs nothing and
removes a selection surface. Subsumed by F1 for substance.

---

## GATE-QUALITY AUDIT (the assigned attack points)

- **(a) burden scope:** convicted — F1 (equivocation; classical
  availability; mut2) + F2 (the commutation gate covers only the
  trivial disjoint-proposal case and cannot fail; the arb-as-operator
  lift never happens — confirmed by direct inspection: no `('r', ...)`
  event is ever lifted). The honest minimal exhibit is specified and
  pre-verified in R1.
- **(b) record-word aggregation:** convicted — F4 (three inequivalent
  conventions, 11/4 / 15/4 / 23/4; the receipt's is the fine-ontology
  pushforward adopted silently; linearization counting = a foliation
  measure by the back door; the cut algebra erased).
- **(c) ratio sampling:** F10 — arbitrary but not class-blind
  (census run); vacuous either way (F1).
- **(d) q_of fidelity / fixture split:** convicted — F3 (A5'-refuted
  idle, missing self-arbs, chimera family, wrong mus on shared support)
  + F8 (the F-PAIR/F-PATH split is a gap, not a decomposition; the
  banner's scope sentence false).
- **(e) QG5b/D23:** F7 — fiber statement incomplete as gated (1/15
  pairs) and numerically misstated in the pin ("two" ≠ 4); full census
  now referee-anchored (7 × 1/6, 8 × 0); D23 citation is
  principle-naming per corpus convention, gate does not instantiate
  D23's mechanism.
- **(f) QG4 per-type:** convicted — F5 (one toy map + a declaration;
  verdict line overclaims).
- **(g) declarations:** Hegerfeldt properly pre-registered; mid-chain
  drift / forced-click ontology / D24-D26 g-binding properly carried
  (pin Q5 and banner) — EXCEPT the scope banner's "CONFLICT core
  lifted" clause (F8) and the verdict line's "NSE holds per record
  type" (F5), both wider than any computation.
- **(h) numerical hygiene:** clean. dps 80 throughout; all F-PAIR
  rationals dyadic (binary-exact); Fraction→mpf conversions exact;
  1e-60 thresholds honest for ~1e-79 arithmetic error; the 1/100
  control threshold declared in-line; `chop` in prints only; no float
  literals in the computation path. The hygiene discipline is intact —
  the defects of this round are all at the claims layer.

## PLUMBING, SEEDS, DETERMINISM, LOG

- **Reruns:** PYTHONHASHSEED 0, 61, 71 all byte-identical to the
  committed .out, exit 0 (~1 s; LOG #309's "seed-independent (0/71)"
  consistent).
- **Exit-1 by design:** mut1 (expected 2/3 → 7/10): 6 PASS / 1 FAIL,
  exit 1. mut4 (EDGES broken): exits nonzero via the line-94 assert
  (AssertionError, 0 gates run) — acceptable, though the 2/3-1/3
  protection is partly assert-based rather than check-based.
- **The two vacuity mutations (the finding, not the plumbing):** mut2
  (pricing sabotage) 7/7 exit 0; mut3 (non-isometric VB) 7/7 exit 0.
- **Determinism:** no randomness; all iterations over sorted
  structures; `sorted(..., key=repr)` deterministic; verified across
  hash seeds.
- **LOG #308/#309 vs artifacts:** narratives match the pin/receipt/.out;
  #309's "THE BURDEN DISCHARGED AT FIXTURE SCALE", "foliation
  invariance BY IDENTITY", and "NSE ... per record type" inherit
  F1/F2/F5. The #309 numbers themselves are real.

## WHAT SURVIVES (verified)

- **F-PATH as a lift of the kernel layer:** the order-lottery chain is
  genuinely per-cut normalized classically, and its lift is correct:
  winner diagonal exactly (2/3, 1/3) — matching paper 25 §10.2 (checked
  at source); state norm 1 with no division.
- **The fine-vs-coarse discriminator STATEMENT, now with the complete
  census referee-anchored:** all 7 same-fiber coherences exactly 1/6,
  all 8 cross-fiber exactly 0; the 1/6 is robust to the d42b2 click-
  chain refinement (per-click amplitudes multiply to √(1/6)); the
  instrument-pair framing is consistent with d42b2 E6/RF1's deferral,
  and the forced-click ontology hazard is properly carried. This is the
  round's genuinely valuable observable — it survives independently of
  the trilemma claim.
- **The fiber statement's content** (identifiability stops at the greedy
  fiber), true and now complete (F7's census); D23 as principle-name.
- **QG4's positive half:** basis-copy reception preserves all 10 probe
  distances; the negative control is real and fires at exactly
  1/√2 − 1/√5.
- **Numerical hygiene end to end; seeds; determinism; exit plumbing on
  expectation breakage.**
- **The d42b3 decided structure is untouched** — nothing in this round
  disturbs the trilemma theorems themselves; indeed this review's B1
  leans on them.
- **New, this round (referee-computed, offered to the program):** the
  d42a ground-truth menus at the A7 cuts ([] and [pA0]: per-actor sums
  1; [pA0,pB1]: A-menu {selfA 1/4, pair 1/8+1/8, idle 3/4}, sum 5/4, N
  = 5/2; [pA0,selfA]: sums 1, N = 2); the true depth-2 family (32
  sequences, Z = 4); the A7 witness mus 1/256 = 1/256 reconfirmed; the
  three-convention normalizer table (11/4, 15/4, 23/4); the complete
  coherence census; and the A7-lift pincer arithmetic (R1) —
  pre-verified for the repair.

## PRESCRIBED REPAIRS (pre-verified where stated)

- **R1 (F1+F2, the flagship).** Re-pin the burden honestly and build the
  A7 fixture the pin's own QG3 promised. Concretely: lift the depth-3
  d42a sub-family around the A7 witness with the REAL pricing (menus
  above, from the committed machinery — small dims: A's register needs
  4 branch slots, B's 4; the joint space ≤ 64, within the pin's own
  bound). Gate: (i) the cut-local sqrt-branch maps' norms — exactly 1
  at [pA0] and exactly 5/4 at [pA0,pB1] (print the 5/4 as the
  OBSTRUCTION, with its L2 identity: the excess is the blind pair
  group, 2 × 1/8); (ii) the operator inequality between the two
  cut-local A-steps (branch sets 2 vs 4 — no cut-independent A-operator
  exists); (iii) the trichotomy printed as the round's result:
  cut-independent operator ⇒ the d42b3-D3 zero class (arbitration
  abolished); cut-dependent ⇒ carrier overlap (disjointness argument
  void) with existence of a consistent commuting family OPEN (the
  actor-factored/h12 constraint transposed to operators); dilation ⇒
  the normalizer reappears as cut data. All three arms' arithmetic is
  verified this round. THEN the honest pin statement is: the lift
  discharges the burden where the classical chain is already
  normalized (kernel/path layer); at the arb layer the quantum
  completion is the OPEN successor front — OR, if the program can
  exhibit a joint-carrier commuting isometry family reproducing the
  d42a measure at the A7 diamond, THAT is the discharge (none is known
  to this referee; nothing in the receipt attempts it). If any
  endpoint-ratio claim is kept, it must cite d42b3's gradient
  completion as the classical object with the same diagonal and drop
  "impossible classically".
- **R2 (F3).** Rebuild F-PAIR on an actual settled grammar: the true
  d42a depth-2 slice (32 sequences, self-arb continuations in, idle
  3/4, Z = 4 — anchors above) or the d42b1 slice (then genesis idle
  1/2 and deliver events in). Fix the A5' citation — as written it
  cites the correction FOR the corrected-away value.
- **R3 (F4).** Adjudicate the aggregation convention in the pin: state
  that word-basis amplitudes sqrt(Σ_lin mu) = the order-sealed (fine)
  pushforward; either derive it from the record ontology (if clicks
  are sealed records per d42b2-B1, say so and reconcile with QG5/QG6's
  "EMPIRICAL" declaration) or carry both conventions with the 11/4 /
  15/4 / 23/4 anchors as controls. Declare the linearization-count
  factor and its foliation-measure character explicitly.
- **R4 (F2 gate form).** Make QG1/QG3 an actual operator gate: use the
  (currently dead) embedA/embedB, compose (I⊗V_B)(V_A⊗1) and
  (V_A⊗I)(1⊗V_B) as matrix products, compare; add a same-register
  NEGATIVE control (two sequential events on one actor's wire must NOT
  commute) so the gate can fail; check VB's isometry as well as VA's.
- **R5 (F6+F7).** Compute the fine instrument via the order-copy
  isometry (2 lines); run the complete coherence census (7 + 8 pairs,
  anchors above); fix pin Q3's "the two path orders" → four; note the Q
  fiber as the second instance.
- **R6 (F5).** Either implement the four types' actual reception maps
  on their actual registers (delivery on the {s,r} joint register with
  chain transport; merge with supersession update) or scope the verdict
  line to what ran: "one shared reception form gated; per-type sweeps
  carried".
- **R7 (F8-F10 hygiene).** Reconcile pin §2 with the fixtures actually
  built (or build the pinned ones); correct the scope banner; delete
  the 11 dead symbols; full ratio sweep instead of strides; gate Z's
  value itself (mut2 is the proof it currently is print-only).

## Reproduction inventory

- Reruns: `PYTHONHASHSEED={0,61,71} python3
  v10/code/d42b4_quantum_lift_exact.py` → byte-identical to
  `v10/data/d42b4_quantum_lift_exact.out`, exit 0.
- `verify_d42b4.py` (scratchpad; 28/28): fiber sizes 4/2; complete
  coherence census (7 × 1/6 same-fiber incl. Q-fiber, 8 × 0
  cross-fiber); honest fine-instrument 0; toy family 28/19/15/4
  reproduced; full 342-pair ratio sweep; sampled-pair class census + 8
  untouched words; three-convention normalizers 11/4, 15/4, 23/4 with
  mixed/pure ratios r, 2r, 4r; control 1/√2 − 1/√5; scalar-commutativity
  vacuity; d42a ground-truth menus at [], [pA0], [pA0,pB1], [pA0,selfA]
  (sums 1, 1, 5/4-each, 1; idle 3/4; selfA 1/4; N = 5/2 at the pair
  cut); A7 mus 1/256 both orders; true depth-2 family 32 / Z = 4; 4
  shared-support mu mismatches (e.g. (pA0,nA): 1/16 vs 3/32); the R1
  pincer arithmetic (isometry at [pA0], 5/4 at [pA0,pB1], branch-set
  growth 2 → 4).
- `mut1.py` (expectation 2/3 → 7/10): 6/1, exit 1. `mut2.py` (pricing
  1/8 → 1/7, 1/2 → 2/5, 3/4 → 3/5): **7/7, exit 0**. `mut3.py` (VB =
  (7/3, 5/2, 9)): **7/7, exit 0**. `mut4.py` (EDGES broken):
  AssertionError, exit nonzero.

**Disposition:** the round is NOT terminal-fit. The two BLOCKERs sit at
the round's central claim (the trilemma discharge) and its load-bearing
mechanism (operator-identity foliation invariance): what was computed is
a correct lift of the already-normalized kernel layer plus a classical
flat pushforward of a mispriced family, wearing square roots; the case
the burden names — the arb layer, where per-actor menus leave 1 and the
A7 diamond's intermediate cuts differ — is exactly the case never lifted,
and the naive lift of it fails by the grammar's own arithmetic (the R1
pincer, pre-verified). The genuinely new and safe assets of the round —
the fine-vs-coarse 1/6 instrument pair (census now complete), the fiber
statement, the NSE control — survive re-scoping. On R1–R7 and a green
rerun this front can return with an honest result: either a real
joint-carrier discharge at the A7 diamond, or the theorem-grade statement
that the quantum completion problem BEGINS at the arb layer — which is
where d42b3 left the classical one.
