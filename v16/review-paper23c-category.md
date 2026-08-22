# Paper 23c review — Seat C (category/structure)

Date: 2026-08-22

Disposition: **ACCEPT-WITH-FIXES** (two MAJOR, one MODERATE, one MINOR)

Blind delta review of the #325/#326 construction
`v16/paper-23c-oriented-pair-underdetermination.md`
(`7e90aba64c4abf5585d409f8d9696c76e0308007da3f81607e8e187cf709f126`,
235 LF) against frozen pin `note-paper23c-oriented-pair-pin.md`
(`d50dc41c7a7cf4f42b5caf3489b790990f9d899c113020a495844fbcac5dfcd2`)
and terminal 13D `3b91766f…`. Seat lens: category-theoretic structure —
naturality, quotient soundness, definitional hygiene.

## Findings

**F-C1 (MAJOR). Definition 2.3 is unsatisfiable as stated on all
presented experiments.** It demands naturality "for every presentation
morphism $h$" between experiments, but the groupoid action is only
partial on experiment tuples: $h\widehat e$ must exist and be admitted.
As written the quantifier ranges over morphisms that are not in the
domain of the action, making Def 2.3 ill-typed rather than merely hard.
*Required repair:* restrict to admissible $h$ (those for which
$h\widehat e$ is defined and presented); no mathematical content moves,
but every later proposition citing Def 2.3 inherits the corrected
quantifier.

**F-C2 (MAJOR). Proposition A's stabilizer hypothesis conflates two
different experiments.** The proof asserts the unmarked grand
experiment has full symmetric stabilizer (correct, 13D §14) but states
the proposition for an arbitrary "mark-symmetric" experiment without
defining which marks are swap-invariant; as stated it reads as if any
experiment with $|I|\ge2$ admits a transposition, which is false
(e.g. a fully landmark-rigid or asymmetrically marked experiment).
*Required repair:* state Prop A over the class of experiments whose
stabilizer contains a transposition — explicitly: unmarked
experiments and those whose mark sets are invariant under some
transposition — and note that other experiments are deferred to §4.

**F-C3 (MODERATE). Proposition D's proof contains an editing artifact.**
"specialize B to $(L,L)$" leaves a half-sentence from an earlier draft;
coupling B should simply be *defined* as $(L,L)$ with independent-
uniform first rank. The argument survives verbatim after deletion of
the clause.

**F-C4 (MINOR). §5 "unique maximal" is asserted without a uniqueness
proof.** The residual section calls the undirected bond graph "the
unique maximal $\Gamma_D$-native binary relation". Uniqueness among
equivariant binary relations deserves one sentence (any equivariant
binary relation is a function of the orbit cell; bonds are the only
nontrivial one carried natively at every size) or the word "unique"
must be dropped.

## What survived

The three-obstruction architecture is sound: fixed-point obstruction
(verified by this seat independently for $n\in\{2,3\}$), no-natural-
order (classical, correctly cited to 13D §3.4/§14), and the
rank-coupling law-invariance witness (Lemma C's field-by-field check
against 13D §6.2/§6.3 is exact; the densities 0 vs 1/6 follow). The
landmark closure (Prop F) is the right answer to the obvious loophole
and respects the #237 wall. Control matrix rows 1–10 all PASS as
dispositioned. Outcome `P23C-ORIENTED-PAIR-NOT-DERIVABLE` is earned
modulo the four repairs; none is structural.

Mandatory regressions: controls 1–10 re-run by this seat — PASS
(control 9 conditional on F-C4's resolution).
