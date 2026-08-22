# Paper 23a adjudication

Date: 2026-08-22

Disposition: **REJECT — TERMINAL STATUS REFUSED FOR THIS CANDIDATE;
THE UNIT REMAINS INVESTIGABLE THROUGH A FRESH FREEZE**

This is the joint adjudication of the three frozen blind seats. It
confirms or refutes each surviving finding, states the verdict, and
fixes the provenance of every coordinate. It constructs nothing.

## 1. Bound corpus

| object | ordinary SHA-256 |
|---|---|
| P23a pin (#309) | `aafb35591bcc5e87417b8d2ee91e13d42935f9f75e9191a0e9dff60cd9d16b0c` |
| P23a candidate (#310) | `9cab8d2e78ee5365b0facc86ff059074f482091bbb3621cfd328939b9e247a5a` |
| construction note (#310) | `cc157c793cca620b680dca1d93b83a6726dee1e3b7e044647a9cffde889ea10c` |
| Seat C report (#311) | `8af0942fa88519363c62ddfd06fe7d81fd05e001d12698576c61ca8252b80372` |
| Seat P report (#312) | `0c6c470fe50eaacd4cc9096c54e6175b91b9a3fb7596c0257a0131b8040eb8f4` |
| Seat F report (#313) | `705a47aeac07b6c774fd0aeae695cefc658da19442ee37e5a5f86879f128e9da` |
| Paper 13D law | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` |

## 2. Finding dispositions

Seat C verdict REJECT; Seat P ACCEPT-WITH-FIXES; Seat F REJECT.
Per finding, with the adjudicator's independent check:

| finding | seat(s) | severity | disposition |
|---|---|---|---|
| Fusion/tensor complexes identified with primitive classes (Thms C/D) | C (F-C1), F (F-F1) | CRITICAL | **CONFIRMED**. Paper 13D §7.1 retains tensor source and fused target values in every fusion history; §10.2 keeps staged traces distinct; the candidate's own Proposition A.2 proves trace shape is complete-reader-visible. $\Phi_s(U_m\boxtimes U_{m'})\not\sim U(m+m')$ by the candidate's own separation principle. Theorem C's determinism premise proves determinism, not congruence. |
| Class-level associativity unavailable; semiring unproved | C (F-C2), F (F-F1(2)/F-F2) | CRITICAL | **CONFIRMED**. Left/right bracketings retain distinct intermediate fused frontiers (carriers $\{1,2\}$ vs $\{2,3\}$); complete reader separates them; union-of-carriers associativity lives only at final-target level, which §4.4 itself concedes is coarser than any sector statement. Proposition E therefore has no subject matter. One correction entered by the adjudicator, narrowing Seat F: sub-point F-F1(3) (commutativity fails) is **REFUTED** — the fusion generator is family-indexed and the ambient category is symmetric monoidal (Paper 13D §§5.2, 10.1–10.2), so component permutation acts trivially at class level. Commutativity holds; associativity still fails; the REJECT grounds are unchanged. |
| Definition 2.1 aligned-pair quantification degenerate for differing diagnostic catalogues | C (F-C3) | MAJOR | **CONFIRMED**. Readers on distinct outcome fibers admit no literal $gRg^{-1}$ counterpart; the quantification is partial where separation is needed. The supplied replacement (Paper 13D §15-style diagonal comparison object) is adopted as the correct formulation for any successor. |
| §4.4 class-equality bullet contradicts Proposition A.2 / parent control 7 | C (F-C4), F (F-F5) | MAJOR | **CONFIRMED.** |
| Involution refutation stands on the unproved algebra | F (F-F3) | MAJOR | **CONFIRMED** as void-as-printed, with the adjudicator's note that the expected no-dual statement likely survives on the honest class set (empty-carrier argument); expectation recorded, proof owed. |
| Multiplicity notion coupled to unrepaired Definition 2.1 | F (F-F4) | MAJOR→MODERATE | **CONFIRMED** with severity reduced: the coupling is real but is a design constraint on the successor, not an additional independent defect. |
| Theorem B chain-descent gap | P (F-P1) | MAJOR | **CONFIRMED**; replacement proof (per-pair transport, composed along chains) adopted. |
| False arithmetic sentence in §3.2 ($2^7\times625=128$) | C (F-C6), P (F-P2), F (noted) | MODERATE | **CONFIRMED**; correct census $16\times4\times2=128$ over $16\times625$ seeds; replacement sentence verbatim in both seats, adopted. |
| Endpoint mass formula hypotheses unstated | P (F-P3) | MODERATE | **CONFIRMED**; replacement adopted. |
| Deletion clause imprecise (C F-C5) / alignment clause (P F-P4) | C, P | MINOR/MODERATE | **CONFIRMED**; replacements adopted. |

All three seats independently recomputed the stage 1–2 fixture
arithmetic (seed censuses, orbit partitions 96/64 and 192/128, six
and eight mass values, $B^2$ endpoint conditional, bond marginals)
with matching results; the arithmetic of stages 1–2 is sound. The
defects are in definitions and stage-3 structure, not in computation.

Mandatory regressions: controls 3 PASS (all seats), 14 PASS (all
seats), 17 PASS (all seats), 15 FAIL (Seats C, F), 16
CONDITIONAL-FAIL (Seats C, F).

## 3. Verdict

**REJECT.** Grounds: the stage-3 classification (Theorems C/D,
Corollary C.1, Proposition E, §4.4 bullets, §4.5 rows 3a–3e, and the
earned-outcome block) is structurally unsound — it rests on class
identifications that the candidate's own Proposition A.2 refutes, and
no bounded prose repair can hold both. Two of three seats reached
REJECT independently; the third flagged the same defect as an
out-of-mandate observation. Terminal status is refused.

Bounded repair was considered and refused: repairing stage 3 while
keeping stage 1 requires rebuilding the class set (primitive, tensor,
fusion, and bracketing-distinct classes all distinct) and reproving
or withdrawing every stage-3 conclusion — new apparatus, not prose
substitution.

## 4. Coordinate provenance after adjudication

Voided as earned by this candidate:
`P23A-FUSION-CLOSURE-FAILS`,
`P23A-COMMON-POSITIVE-CHARACTER-NONUNIQUE` — both stood on the
unproved $(\mathbb N,+)$ identification. Salvageable in a successor:
finite-closure failure is re-earnable by carrier monotonicity (any
product chain strictly increases occurrence-carrier cardinality);
character/involution conclusions return only if an associative class
product is first proved, else `NOT-APPLICABLE`.

Surviving as reviewed salvage input for a successor version, none of
it accepted physics: stage-1 machinery with the adopted Definition
2.1 replacement (diagonal comparison object); Propositions A.1–A.2;
stage-2 definitions, Theorem B with the chain-proof repair, and the
exact fixture tables (independently reproduced by all three seats).

Scope walls held throughout: no channel odds, opportunity, activity,
root, `Pi_phys`, `Gamma_struct`, chronology, dimension, metric,
gravity, or actuality was constructed by the candidate or is
constructed by this adjudication. Paper 17's ensemble gate remains
CLOSED. Paper 22 v3 was consumed nowhere and remains TERMINAL at
#307 untouched.

## 5. One-strike rule

Not triggered. The one-strike rule terminates the Paper 22 line when
an independent semantic counterexample survives review there; this
unit is a Paper 23-line unit consuming terminal Paper 13D only, and
pin Section 10 provides that adjudication "confers or refuses
terminal …; no automatic successor exists," while pin Section 1
provides that a blocked result at one stage does not terminate later
stages' investigability. The present rejection is a candidate-level
refusal with a pinned salvage path, not a line-level termination.

## 6. Next event

Any successor (Paper 23a v2 over the honest class set, Unit C, or
Unit D) requires explicit user authorization and a fresh hash-bound
freeze before construction. None is opened by this entry.
