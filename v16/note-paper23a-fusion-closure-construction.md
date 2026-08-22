# Paper 23a construction note

Date: 2026-08-22

Disposition: **CONSTRUCTION COMPLETE — SUBMITTED FOR THREE-SEAT BLIND
REVIEW**

This note binds the construction to its frozen Unit B pin and records
coverage, provenance, and discipline. It is not an adjudication.

## 1. Frozen inputs

All hashes verified on disk at freeze time of this note; the pin was
frozen and recorded at ledger #309 before the candidate file existed.

| object | ordinary SHA-256 |
|---|---|
| P23a pin (frozen before construction) | `aafb35591bcc5e87417b8d2ee91e13d42935f9f75e9191a0e9dff60cd9d16b0c` |
| P23a candidate (this construction) | `9cab8d2e78ee5365b0facc86ff059074f482091bbb3621cfd328939b9e247a5a` |
| Paper 13D law | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` |
| Paper 13D math adjudication | `ae2c4ef066335c39a0b8057c897c947b06e4270be67d1ed3ec59bf8d6d0a00c9` |
| Paper 22 v3 terminal bytes | `be0822c81d58eee487925191b3156e22172bcc372012fd6cfc4f23b2ca890349` |
| Paper 22 v3 adjudication | `521784834d0aa97308a05f2d638d436dcd61c011d41f94bcae35e459b857ab10` |
| Paper 23 parent preparation pin (#308 bytes) | `7ea147879dff9334fed241e628feec7b3bb3bece0e4b60e992ff2fc57ec36674` |
| Paper 22 semantic-input audit | `9f33516c001be921178189577ae9435308da00b84a101cf33a4507d351df88b6` |
| Paper 23 pin internal audit | `97cabd7a7446508f06843828fb6f05e178eea7bd2bc104a33d6fc857457694ce` |
| Paper 18 v6 composite | `60a4f0735d967623193f7579fb35fbace3428d7172c1b8f356ff95b304f07bea` |
| Paper 19 adjudication | `2bdfcf588b9e8c6ccc47071fc49a1aba47cbba7d19e5f3dd788429701525a954` |
| Paper 20 adjudication | `18ea13e2bd609439d2cb4e2a03c1f0c4f0fbf7e37e2e38bba15272570001ac14` |

## 2. Stage-by-stage coverage against pin Section 4

1. **Referent census** — candidate §1 enumerates twelve consumed
   referent classes with section pointers; an explicit not-consumed
   paragraph closes the list. No unlisted referent is used anywhere.
2. **Sector congruence** — Definition 2.1 quantifies over all aligned
   admitted readers led by the complete reader (pin control 13);
   Lemma 2.2 proves equivalence; Theorem A proves compatibility with
   tensor, simultaneous fusion, futures/composition, deletion, stable
   words, and erasure. Propositions A.1–A.2 compute the quotient on
   the certified fixtures: classes = family × size × sort. Outcome
   `P23A-SECTOR-CONGRUENCE-CONSTRUCTED`.
3. **Multiplicity descent** — Definition 3.1 uses full-orbit mass
   only; representative mass is named and forbidden. Theorem B proves
   constancy on congruence classes. Section 3.2 prints exact mass
   tables at n=1 for U(n) (96 cells / 64 fixed / six distinct masses)
   and D∘Q⁰(n) (192 cells / 128 fixed / eight masses), plus the
   closed-form endpoint class masses ½, ½ at every size. Outcome
   `P23A-MULTIPLICITY-DESCENT-CONSTRUCTED`.
4. **Fusion classification** — Theorems C/D prove countable-tower
   closure and finite escape; semiring axioms hold (≅ (ℕ,+),
   indecomposable); involution fails by the explicit dual argument;
   Proposition E proves a continuum of positive characters,
   refuting uniqueness constructively rather than assuming it.
   Outcomes earned exactly:
   `P23A-FUSION-CLOSURE-FAILS` (finite-closure sense, fixture scope),
   `P23A-COMMON-POSITIVE-CHARACTER-NONUNIQUE`. Not earned:
   `…FINITE-NONNEGATIVE-SEMIRING-CONSTRUCTED`,
   `…FINITE-FUSION-RING-CONSTRUCTED`. The pre-registered outcome names
   are neither renamed, split, nor merged (pin kill condition 3).
5. **Classification table** — candidate §4.5, one row per computed
   cell, each with theorem-level scope.

No stage required any referent outside the census; no stage is
BLOCKED.

## 3. Control coverage against pin Section 6

Candidate §5 disposes all twelve carried controls and all six
stage-specific controls (18 rows), one row each with a concrete
disposition naming where in the candidate it is enforced. The five
mandatory review regressions (controls 3, 14, 15, 16, 17) map to:
orbit-size handling in Definitions 3.1/§4.1; full-orbit-sum-only rule
in Def 3.1; countable-not-finite closure statement and failed
involution test in Thm D/Cor C.1; constructive nonuniqueness in Prop
E; blocked FP route in Cor E.1. Parent-pin control 40 (fixture-scoped
negative result ≠ global no-go) is discharged verbatim in candidate
§4.5.

## 4. Paper 22 v3 topology

The candidate consumes Paper 22 v3 nowhere. Its bound terminal bytes
were verified available and unused: no definition, number, amplitude,
phase, instrument object, or proof step derives from them. Pin kill
condition 2 (`BLOCKED-AT-INPUT-TYPOLOGY`) did not fire.

## 5. Independent arithmetic verification

Exact rational arithmetic (`fractions.Fraction`, no floating point),
run independently of drafting as audit scaffolding before this note
froze:

- κ seed census reproduces C = (49, 576; 576, 49)/625 per column
  exactly over all 1250 seed pairs;
- β seed census reproduces B per column (25 seeds);
- B² recomputed from B entries equals (337, 288; 288, 337)/625;
- n=1 relational evaluator: sixteen reachable packets from
  (c; η_X, η_Y, e⁰); labeled supports and orbit partitions of
  U(1) and D∘Q⁰(1) enumerated exhaustively; cell counts (96/64-fixed
  and 192/128-fixed), the six and eight distinct orbit masses, and
  normalization to 1 confirmed exactly;
- composite endpoint conditional equals B² entrywise on the D∘Q⁰(1)
  fixture (the joint P(q₂,q₀) has entries B²_{ba}/2, conditionalizing
  on q₀ recovers B² exactly);
- cross-bond marginal ½; three-pair pattern (ℓ₁₂, ℓ₁₃) uniform on the
  four outcomes (exact enumeration over shared color and thresholds);
- set-level C₂-orbit reference value for B₁⁰(1): (4096 + 256)/2 =
  2176.

The harness was scaffolding only; it enters no printed proof and is
not part of any constructed coordinate. Two harness bugs found and
fixed during verification (seed-count normalization; joint vs
conditional comparison); both were errors in the checker, not in any
printed value, and the final run is clean.

## 6. Discipline statements

- No code, evaluator fixture, implementation artifact, or generated
  dataset is part of the constructed object; prose and exact
  arithmetic only.
- No downstream artifact beyond the bound inputs was consulted during
  construction.
- Construction-stage writes scoped to
  `v16/paper-23a-sector-multiplicity-fusion-closure.md` and this note.
- Line counts at freeze: pin 212 LF; candidate 606 LF; this note as
  hashed below.
- Scope walls restated: no channel odds, opportunity/activity/root
  law, Pi_phys, Gamma_struct, chronology, dimension, metric, gravity,
  or actuality; Paper 17 gate CLOSED throughout.

## 7. Review request

Three-seat blind review per pin Section 10 — sector/category seat,
probability/multiplicity seat, fusion-algebra/representation seat —
repo read-only, each seat rebuilding from published prose, reports
frozen separately before joint adjudication. Mandatory regressions:
controls 3, 14, 15, 16, 17. Verdicts ACCEPT / ACCEPT-WITH-FIXES /
REJECT, findings most-severe-first with replacement sentences
verbatim. Adjudication confers or refuses terminal per house rules;
no automatic successor exists.
