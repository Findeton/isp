# Paper 22 v3 — joint adjudication of the three-seat delta panel

Date: 2026-08-22

Adjudicator: separate from all three seats; repo ground truth per
RUNBOOK §12. This note joins the frozen reports and rules. It is the
terminal event for the unit unless it orders repair.

## 1. Panel state

| seat | file | ordinary SHA-256 | verdict |
|---|---|---|---|
| C (category/source/functor) | `v16/review-paper22-v3-category.md` | `0d611e8aaa8b2b6a59d0e3587b827f519994e5977d8969602b0c629590851472` | ACCEPT-WITH-FIXES |
| P (probability/instrument) | `v16/review-paper22-v3-probability.md` | `55e07cec4897443ddc5dc32e2432d52c7be13b4fd50f604a3459bf3492e8f87a` | ACCEPT-WITH-FIXES |
| Q (quantum/no-hiding) | `v16/review-paper22-v3-quantum.md` | `4892baa59db0adf2b8a9803637731c7ffe9f5edca9936a82ef496579be6cb66d` | ACCEPT-WITH-FIXES |

All three reports were frozen before this adjudication. Hashes recomputed
from disk at adjudication time and match the ledger entries #303–#305.

## 2. Independent adjudicator verification

Before joining the seats I ran my own checks, independent of their prose:

1. **Provenance.** All fourteen pin evidence-table hashes match disk.
   Pin `703784ec…` (379 LF), candidate `4064f66b…` (1024 LF),
   construction note `1dbef0dc…` (120 LF): verified, and the pin was
   committed before construction existed in the worktree chronology
   recorded at #303.
2. **Inheritance.** v3 §§2–4 are content-identical to v2 §§2–4; v3
   §§8–14 are the v2 §§7–14 with disclosed renumbering plus exactly the
   pin-slot additions (Thm 11 items 2/6, five control rows). No third
   change exists anywhere in the inherited material.
3. **Restoration.** v3 §5 reproduces v1 §§5.1–5.3 content verbatim
   (formulas, closure proof, kickback, discriminator); Theorem 4 is new
   and its proof is correct. No biased carrier, coarse bit, repartition,
   or undefined isometry exists.
4. **Arithmetic.** Law (V) re-derived from the residual-environment Born
   rule with first-lift amplitudes; 400,000 exact cells agree to float
   rounding; anchors (`B`, `R`, `C_phi`, `B^2`, `K_phi` endpoints,
   neutral odds), the four registered consequences, and the beta-clause/
   visibility-label provenance all reproduce.

## 3. Rulings on findings

The three seats independently converge on the same four MINOR defects,
all inside repaired prose:

| finding | C | P | Q | ruling |
|---|---|---|---|---|
| Theorem 7 proof intermediate scalar `±12/25` (true product `±144/625`; sign phrase ambiguous) | F-C1 | F-P1 | F-Q1 | UPHELD — arithmetic slip in narration; matrix (17) correct |
| Corollary 7.1 "unit visibility on both rows" contradicts Corollary 7.3's `(288/337)|gamma|` / `|gamma|` | F-C2 | F-P2 | F-Q2 | UPHELD — internal contradiction |
| Corollary 7.1 exemplar kets give `gamma=-i`, not registered `+i` | F-C3 | F-P3 | F-Q3 | UPHELD — exemplar sign error |
| Theorem 9 joint law printed only at `gamma=1` without stating the scope | F-C4 | F-P4 | F-Q4 | UPHELD — unscoped equation |

None moves a number, definition, theorem result, control value, or scope
wall. All three seats also record the same NOTE (inherited parenthesized
pseudo-math rendering, verbatim from v1/v2); Seat C additionally requests
the calibrated-lift gauge reading be bound as precedent.

**Disposition: ACCEPT-WITH-FIXES → bounded prose repair ordered.** The
repair applies the three seats' convergent replacement sentences
(identical across seats up to whitespace) for F-C1–F-C4/F-P1–F-P4/
F-Q1–F-Q4, plus optional whitespace-class normalization of the inherited
pseudo-math (F-C5). Numbers may not move. Seat C's precedent request
(F-C6) is granted at zero byte cost: the gauge reading recorded below.

**Precedent bound (no byte change):** within the calibrated lift, the
gauge group of `R` is exactly {diagonal input phases, diagonal output
phases, simultaneous exchange of the two physically typed modes}; naked
label swaps are not gauge arrows and change typed controls.

## 4. Terminal ruling

All nine pre-registered coordinates stand CONSTRUCTED simultaneously:
both repairs confirmed by all three seats, every v2 survivor confirmed by
all three seats' regression sweeps, no third independent semantic
counterexample found by any seat or by the adjudicator. **One strike is
NOT triggered. The Paper 22 line does not terminate.**

`TERMINAL — ACCEPT-WITH-SCOPE` is conferred on
`v16/paper-22-reversible-structural-instrument-v3.md` at the pinned
scope: complete triggered local structural instrument on homogeneous
source fibers, on the bound uniform fine-seed apparatus, with the exact
partial-visibility family. Provenance chain: pin #303 (freeze), candidate
#303, seats #303/#304/#305, this adjudication. Status line to be set
post-repair, since ACCEPT-WITH-FIXES orders a bounded repair first; the
terminal status takes effect when the repair is verified and committed
(same unit, no re-review of unchanged content).

Unchanged walls: occurrence, activity, root, chronology, dimension,
metric, gravity, actuality, source superposition, same-source multi-mark
composition, simultaneous-fusion algebra remain UNCONSTRUCTED and
unclaimed. Paper 23 may bind this instrument only through its own fresh
hash-bound freeze after the repaired bytes exist.

## 5. Repair order

Bounded, forward-only, single pass, paths limited to
`v16/paper-22-reversible-structural-instrument-v3.md`:

1. Replace the Theorem 7 interference sentence per F-C1's replacement.
2. Replace Corollary 7.1's final fringe-shift sentence per F-C2.
3. Replace Corollary 7.1's exemplar sentence per F-C3.
4. Replace Theorem 9's opening sentence per F-C4.
5. Optional: normalize inherited `( ... )` pseudo-math delimiters
   (whitespace-class).
6. Update the construction-note line counts if the candidate's size
   changes (forward-only correction in that file, marked as such).

After commit: adjudicator verifies hashes, confirms numbers did not move,
and records the terminal ledger entry. Then, and only then, the Paper 23
preparation pin's input coordinate may be corrected forward-only to bind
an accepted successor through its own fresh freeze — with the user asked
before Units B/C/D open.
