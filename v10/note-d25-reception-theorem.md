# D25 — the reception theorem: formalizing "received by records" (F1, the load-bearing delta)

**Status:** PIN (pre-receipt), 2026-07-12; committed before `code/d25_reception_theorem_exact.py` runs. Provenance labels per D20. Campaign context: goal clause (3)'s grounding — the principle must discriminate real rivals by theorem, not wording (grounding rule (b)); paper 18 §8 F1.

## 1. The candidate formalizations, and the pre-registered stake

Round 1 proposed two formalizations of No Silent Erasure: (a) **ensemble injectivity** — the closure dynamics is injective on click-defined preparations; (b) **in-ontology record-sector dilation / complementary-channel separation**. This receipt pre-registers a test that (a) is TOO WEAK: partial intrinsic dephasing (`rho -> (1-lambda) rho + lambda Delta_Z(rho)`, `lambda < 1`) is injective on the eta-family (it shrinks the distinction by `1-lambda`, never to zero at finite time) yet receives the lost distinguishability by NOTHING — silent erasure at a slower rate, which is exactly the GRW/CSL-class paper 18 §2 must exclude. If the receipt confirms this, the correct formalization is the stronger:

> **NSE (distinguishability-isometry form).** The closure dynamics preserves the distinguishability of every pair of preparations on the TOTAL record ontology exactly: `D(closure(rho), closure(rho')) = D(rho, rho')` for all pairs (D = trace distance). Equivalently, every distinguishability loss on any subalgebra is exactly compensated by correlations with a declared receiver sector; the admitted closures are the isometric dilations `rho -> V rho V†` (unitaries and append-ancilla-then-unitary maps), which is the dispersal class.

The bridge to unitarity is the Wigner/Kadison/Molnár theorem class [LITERATURE]: surjective trace-distance isometries of state space are unitary/antiunitary conjugations; with a declared receiver sector appended, the admitted class is exactly the isometric dilations. The receipt verifies the equivalence ON THE DECLARED FAMILY (it does not re-prove the general theorem).

## 2. The declared family (all exact rationals)

States: the 3-register GHZ-class `rho_eta = 1/2(|000><000| + |111><111| + eta|000><111| + eta|111><000|)`, eta on the grid {0, 1/4, 1/2, 3/4, 1}; plus diagonal-preparation pairs (different root weights) for the value/content split. `D(rho_eta, rho_eta') = |eta - eta'|/2` exactly (the difference is a symmetric off-diagonal pair on a 2-dim computational subspace; the receipt VERIFIES the block structure before applying the closed form — no float spectra).

Closures (the declared candidate family):
- **U** — a unitary on the 3 registers (identity representative): the trivial dispersal;
- **Q_disp** — the isometry `V = CNOT(A->E) (|0>_E)`: dispersal into a declared quantum receiver E;
- **C_bare** — `Delta_Z` on A: Paper 17's hard-seal endpoint read as the closure;
- **C_half** — `1/2 id + 1/2 Delta_Z`: the weak/scale-dependent intrinsic-collapse representative (the (a)-killer);
- **R_cl** — measure A in Z, record the outcome in a classical register: the classical-receiver (Oppenheim-class) representative, `rho -> sum_s (P_s rho P_s) (x) |s><s|_R`.

## 3. Receipt gates (`code/d25_reception_theorem_exact.py`; stdlib Fractions; exit 1 on any failure)

- **R1 (inputs):** family exact; block structure of every difference verified; `D_in = |Delta eta|/2`.
- **R2 (the invariant table — the theorem's core):** for every eta-pair and every closure, exact `D_out` vs `D_in`: U and Q_disp PRESERVE (`D_out = D_in`); C_bare CONTRACTS TO ZERO; **C_half contracts to `D_in/2` — strictly positive, hence INJECTIVE, hence formalization (a) fails to exclude it** (the pre-registered stake); R_cl contracts the eta-distinction to zero.
- **R3 (mimicry):** Q_disp's system marginal equals C_bare's output exactly at every eta — dispersal and erasure are indistinguishable on the proper shadows; only the receiver sector separates them.
- **R4 (receiver necessity and the correlation subtlety):** the S-only algebra fails to separate eta-pairs after Q_disp (marginals equal); the E-inclusive algebra separates (witness `<XXXX> = eta`, exact); AND E's own marginal is eta-independent (print) — reception is carried by correlations with the receiver, not by the receiver's marginal.
- **R5 (value/content split, theorem-grade):** R_cl preserves the distance between diagonal preparations (the VALUE is received by the classical record) while sending every eta-pair distance to zero (the CONTENT is received by nothing) — the ontology-stream's three-way split as a computation; classical receivers are silent erasure with a middleman, exactly.
- **R6 (the Kadison/Molnár leg, on-family):** every closure in the family preserves all pairwise distances iff it is an isometric dilation (U, Q_disp yes; C_bare, C_half, R_cl no) — the general theorem cited [LITERATURE], verified member by member here.
- **R7 (ledger identity, print):** for Q_disp, the system-marginal distance drops to zero while the total distance is exactly preserved — the loss on the subalgebra is exactly the correlation content with the receiver (the data-processing ledger balancing).

## 4. Consequences, pre-stated

If R2 confirms the stake: paper 18 §2's "selects exactly one equivalence class… (closure injectivity on preparations)" and §8 F1's ensemble-injectivity route are SUPERSEDED by the distinguishability-isometry form (a LEDGER supersession; the assembly paper carries the corrected form). The exclusions then hold with no gap: C-class (contraction to zero), weak intrinsic collapse at every rate (strict contraction), classical receivers (content contraction) — all excluded by theorem on the family; dispersal (isometric dilations) admitted. The experimental falsifier is unchanged (the D21 ladder with the attribution gate). F1 closes at family grade; the general-carrier statement remains cited, not re-proven.

## 5. Round-1 hostile fronts (pinned)

(F1) Is trace distance the right distinguishability functional, or must the statement be measure-independent (fidelity/Chernoff — check the family verdicts are functional-independent)? (F2) The Molnár/Kadison citation: exact theorem statement and surjectivity hypotheses — does the family verification honestly bridge to it? (F3) Does the distinguishability-isometry form exclude anything paper 17's Q-class contains (false positives)? (F4) R_cl's "value received" — is preserving diagonal distances the right formalization of the value/content split?
