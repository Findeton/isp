# D42a — the generated-proposal grammar + the smallest conflict fixtures

**Status:** CAMPAIGN PIN (strict; receipts run only against this text),
2026-07-15. Parent: note-d42 (the double mandate; entry condition MET at
D41 #280 — item 7 opportunity structure IRREDUCIBLE). This artifact is
the D42 pin's named first deliverable: the grammar pin (what a generated
proposal IS, typed, with base-version semantics) + the smallest conflict
fixtures. Receipt: `v10/code/d42a_generated_conflict_exact.py`.

## 1. The claim under test

Paper 25 §10 closes with: K1/K2 "require a supplied finite contender
batch" and "remain alternative supplied kernels." D42a's claim splits
that dependency in half and discharges exactly one half:

- **GENERATED (claimed here):** the contender batch, the conflict, the
  arbitration OPPORTUNITY, and the post-arbitration re-proposal
  opportunity are all computed from the record — no external scheduler,
  no supplied batch, no supplied conflict list.
- **STILL SUPPLIED (declared, inherited):** the kernel LAW itself
  (K1 vs K2 remain posited alternatives, per paper 25); the boundary
  genesis version (D41 item-1 class); the measure completion (mu stays
  a product-of-local-conditionals WEIGHT SYSTEM with per-record
  telescopes — d34a's round-1 honest noun; d34b's placement problem is
  INHERITED, not solved).

## 2. The grammar [POSITED; conventions ported from d34a/#152/D33]

Carriers ("wires"): participants and version objects. Event poset =
carrier-wise wire closure (d34a `event_poset` convention); causal order
physical, incomparable order gauge (D33). All weights exact Fractions.

Event alphabet (typed; initiator IN the type — paper 28: type-data
load-bearing):

- `('g', v0)` — genesis: version v0 held by all participants.
  BOUNDARY, SUPPLIED (declared).
- `('p', a, b, x)` — participant a proposes payload x in {0,1} against
  base version b. Carriers {a, b}. **Admission (the H1 CAUSAL
  certificate, paper 28):** the event creating b is in past(e); NO
  supersession of b (arb-on-b) is in past(e); no prior `('p', a, b, .)`
  in past(e). Issuance-valid-but-superseded-outside-past proposals are
  ADMISSIBLE (optimistic concurrency) and may ORPHAN (declared
  phenomenon, censused, never silently dropped).
- `('r', a, C, w)` — arbitration: initiator a (a member of C's proposer
  set) resolves conflict component C selecting feasible winner set w.
  Carriers: C's proposers + base + the new version. **Admission:** all
  proposals of C in past(e); C maximal in past(e); base unsuperseded in
  past(e); no prior arb on the base in past(e); w a MAXIMAL independent
  set of C's conflict graph. The arb event IS acceptance: it creates
  version v' = (base, value(w), authors(w)). Fork-free by construction
  (one arb per base); the optimistic-fork regime is a named future arm,
  out of scope.
- `('n', a)` — recorded idle (budget absorber).

**Conflict [POSITED]:** p1=('p',a1,b,x1), p2=('p',a2,b,x2) conflict iff
same b, x1 != x2, and the two events are INCOMPARABLE (neither in the
other's past). Same-payload proposals are compatible (co-authorship).
Payloads {0,1} on one register make three proposals (0,1,0) on one base
generate the conflict PATH P–Q–R with maximal independent sets {P,R}
and {Q} — paper 25 §10's discriminating instance, here GENERATED.

**The local weight law [#152 fixed-budget, POSITED]:** at each
participant local step, conditioned on causal past only:
propose-total 1/4 split equally over enabled (base, payload) options;
arbitrate-total 1/4 split equally over enabled components with the
initiator in the proposer set, times the kernel law's winner
distribution P_K(w|C) (the winner draw = a RECORDED click, #152);
idle = remainder (absorbs each unavailable total — redistribution,
never dilution). Kernel laws, both computed exactly on the SAME
enumerated alphabet: **K1** = uniform recorded order-click over |C|!
orders + greedy acceptance; **K2** = uniform over maximal independent
sets. On P–Q–R: K1 gives {P,R} 2/3, {Q} 1/3; K2 gives 1/2, 1/2
[EXACT, must match paper 25 §10].

## 3. Fixtures

**ARM-1 (two actors A, B; genesis v0; depth <= 6):** the minimal
conflict — concurrent ('p',A,v0,0) vs ('p',B,v0,1), arb, and the
GENERATED re-proposal opportunity against the new version.
**ARM-2 (three actors A, B, C on v0, payloads 0/1/0):** the generated
path component; K1-vs-K2 discrimination on the generated batch.

## 4. Gates (exit 1 on any failure; exact equality — zero tolerance)

- **G1 closure/resequence:** enumeration interleaving is bookkeeping;
  every enabled-set and every mu factor recomputed along every linear
  extension of every enumerated history is INVARIANT (d34a-H1's real
  gate, ported). No external-scheduler token in any factor.
- **G2 conflict genesis + serialized control:** exact census of
  generated conflicts (> 0); the SERIALIZED sub-family (no incomparable
  proposal pairs) contains EXACTLY ZERO conflicts — conflict is born
  from generated concurrency, exhibited as conditioning (D32C lesson),
  not a separate lottery.
- **G3 generated opportunity + deletion control:** the arb option is
  enabled at H iff its component is in the record; at the prefix
  lacking the second proposal the option set contains NO arb; the
  re-proposal against v' is enabled ONLY in histories containing the
  arb. Set-level exact.
- **G4 staleness — causal vs authentication-only:** supersession IN the
  proposer's past ⇒ inadmissible; the authentication-only check
  (issuance validity alone) ADMITS that same proposal — paper 28's H1
  causal certificate exhibited load-bearing. Orphan census printed.
- **G5 kernel nonvacuity + discrimination (ARM-2):** the path component
  appears with positive weight; P_K1({P,R}) = 2/3 vs P_K2 = 1/2 exact;
  total-variation distance EXACTLY 1/6; numbers match paper 25 §10.
- **G6 joins:** arb in-degree >= 2 censused exactly (>0); the successor
  version carries the join in its past. D23's identifiability limit and
  the NSE/D25/D27 isometry gates are CARRIED OBLIGATIONS of the quantum
  lift (d42b), declared not gated; Hegerfeldt pre-registered there.
- **G7 budget/telescope:** at every enumerated extension point the
  per-participant local-step conditionals sum to EXACTLY 1; totals
  conserved under redistribution (#152).
- **G8 record basis (the D41 eighth residue):** per-type declared
  distinctions (proposer, base, payload, component, winner set,
  authors, initiator); gate: declared-distinct histories yield distinct
  typed DAGs; gauge-equivalent orderings yield the SAME typed DAG.

## 5. Fronts and risks (pinned before the run)

RF1 the actor-layer hazard (d34a-M3): no race/sampling claim anywhere;
mu is a weight system on typed DAGs, gates are law-level. RF2 orphan
proposals are a real generated phenomenon — censused and declared, and
their arbitration-starvation is a named open question for d42b. RF3 the
K1/K2 winner draw enters as one recorded composite click; its
refinement into elementary clicks is d42b's. RF4 the root-free
completion attempt and any action-level (flat-square, paper 28/29
levels) check are campaign fronts, NOT this receipt's. RF5 depth caps
are declared in the receipt banner; any cap is printed, never silent.

## 6. Pre-receipt amendments (forward corrections, 2026-07-15 — found at
## first executable contact, BEFORE the receipt ran; §§1–5 text retained)

**A1 (carriers).** A proposal's carrier set is {a} ALONE — the proposal
is a local record event on the proposer's wire referencing a HELD COPY
of b. Version wires are touched only by arb events. Rationale: with b
as a shared carrier, wire closure would chain same-base proposals into
comparability and conflict would be grammatically impossible. Holdings:
a holds v0 (genesis) plus v'(r) for every arb r in a's past with a in
proposers(C_r); versions propagate ONLY through participation — there
is no delivery event in this grammar (declared; delivery is a d42b
front).

**A2 (fork honesty; supersedes §2's "fork-free by construction" —
that claim was FALSE as stated).** Admission is past-relative, so
INCOMPARABLE arbs on one base are grammatical: optimistic replication
forks, exactly as in distributed version control. What IS enforced and
gated: NO observer past contains two arbs on the same base
(per-observer-past fork-freeness, exact sweep). Incomparable forks are
CENSUSED as a declared phenomenon; reconciliation/merge is a d42b
front. Version identity carries (base, value, authors, initiator) so
incomparable forks are distinct records (initiator disambiguates:
same-initiator double-arb is blocked past-relatively).

**A3 (proposal re-admission).** The prior-proposal blocker applies to
UNRESOLVED priors only: a prior ('p', a, b, .) in past(e) blocks iff it
is not resolved (member of an arb'd component) in past(e). This makes
the G4 causal branch REACHABLE: after the arb, a same-actor re-proposal
on the superseded base has staleness as its SOLE blocker (the causal
certificate rejects; the authentication-only check admits). Supersession
still blocks re-proposal on the old base, so no proposal spam reopens.

**A4 (G7 restated; the joint-event placement problem surfaces here and
is INHERITED, not solved — consistent with §1).** Budget-split
denominators: the propose split uses the INITIATOR'S view; the arb
split uses past(e) (the join's own past — the initiator alone cannot
see the component; the join is precisely where it first exists as a
record). Consequently GLOBAL per-step normalization is NOT claimed —
that is d34b's placement problem, declared open. G7 gates what is
exactly true: (a) propose-sector normalization in the initiator's view;
(b) kernel normalization sum_w P_K(w|C) = 1 exactly, both kernels,
every encountered component; (c) conservation — every weight has the
pinned total/count form. **G2 sharpened:** the zero-conflict-without-
incomparability half is DEFINITIONAL (declared, not gated); the gates
are the hand-derivable depth-2 conflict census (= 4 exactly) and
positive mu-weight of a conflict history (mu([pA0, pB1]) = 1/64
exactly under the pinned law).
