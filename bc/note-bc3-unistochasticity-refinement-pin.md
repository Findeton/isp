# BC3 — UNISTOCHASTICITY UNDER REFINEMENT: does the class survive
# the operations QFT needs? (PIN)

**Status:** PIN, STRICT, 2026-07-28.  **Program:** BC (bc/LOG.md #1).

## The question

[B3]'s quantum criterion — Γ_ij = |U_ij|² — is a basis-anchored,
discrete-matrix notion.  Field theory needs limits: finer time steps,
finer configuration bins, dimension → ∞.  **Is the unistochastic class
closed under the operations a continuum limit performs — and does the
naive continuum object even exist?**  Known already (cite, do not
re-prove): marginalization LEAVES the class ([B3]'s own dilation
clause); at fixed dimension the class is topologically closed (image
of the compact unitary group under a continuous map — state and prove
in-receipt at the dimensions used).  The open, QFT-relevant
questions are refinement and composition.

## The unit

- **Arm A — the binned propagator.**  The free particle (and one
  harmonic-oscillator control) on a ring of n sites (discrete
  configuration space; exact unitary: the discrete free propagator
  diagonal in the DFT basis, entries in cyclotomic fields).  For each
  n in a declared ladder (e.g., 4, 8, 16, 32) and a declared time
  grid: (i) is U_n's entrywise |·|² doubly stochastic (it is — gate
  the classical fact for unitaries); (ii) now BIN: compress k sites
  into one (the coarse-graining the continuum limit undoes) and
  measure EXACTLY how far the binned matrix is from bistochastic and
  from unistochastic (the U3 criterion at n = 3 where applicable;
  polygon/triangle obstructions; exact defects).  The deliverable is
  the DEFECT LAW: how the distance behaves as n grows at fixed
  physical parameters — vanishing (the continuum claim survives at
  toy scale), persistent, or growing.
- **Arm B — the continuum object itself.**  The known analytic fact
  to make exact at toy scale: the free-particle continuum propagator
  has |K(x',x;t)|² = 1/(2πt), which is NOT a probability kernel (its
  x'-integral diverges).  Exhibit the discrete shadow of this
  exactly: the n-site |U|² row masses vs the bin width, the
  normalization's dependence on the discretization, and state
  precisely which limits exist and which do not.  No continuum
  analysis beyond what the discrete family exhibits — the discrete
  family IS the receipt.
- **Arm C — composition closure.**  At n = 3 (where the exact
  unistochasticity criterion is committed — reuse U3's, anchored):
  hunt an exact counterexample pair U, V (algebraic entries) such
  that |U|² and |V|² are unistochastic (trivially — they are entrywise
  squares of unitaries) but the PRODUCT LAW question misbehaves:
  census the relation between |UV|² and |U|²·|V|² exactly (they
  differ generically — that difference IS indivisibility, fine and
  expected; gate it as the expected control), and test whether the
  matrix |U|²·|V|² (the divisible composition a coarse observer would
  write) is itself unistochastic — if not, exhibit the exact
  obstruction: the divisible shadow of a unistochastic process leaves
  the class.  This is the discrete engine of the refinement problem.
- **Known-answer controls** (from U3's committed battery, reused and
  anchored): the flat J/n, the (1/2)(J−I) bistochastic-not-
  unistochastic reference, the n = 2 classical fact.

## Pre-registered outcomes (lean NONE)

- **Q-STABLE:** binning defects vanish along the ladder — the
  continuum claim survives at toy scale; the rate is the deliverable.
- **Q-UNSTABLE:** defects persist or grow — "QFT as an indivisible
  unistochastic process" needs a new idea at the first technical
  step; the exact defect law is the deliverable.
- **Q-ILLDEFINED:** the discrete family exhibits the continuum
  object's non-existence exactly (Arm B) — the criterion is
  finite-dimensional in an essential way; state what any continuum
  version would have to replace.
- Arm C either way: closure or the exact counterexample.

## Gates

Exact arithmetic (cyclotomic/algebraic entries; exact defect
computations; no floats in substantive paths); reused U3 instruments
anchored exit-1-only; the two classical facts gated in-receipt
(unitary ⇒ |U|² doubly stochastic; fixed-n topological closure at the
dims used); substantive negatives exit 0; determinism; declared
ladder and caps printed; runtime < ~35 min with progress prints.
STRICT, no leans, GREEN-UNREVIEWED.

## Scope

Toy lattice scale; no continuum analysis is claimed beyond what the
discrete family exhibits; no renormalization claims; no claim about
interacting QFT; no claim about nature.  Findings are formal
properties of [B3]'s criterion under the stated operations.
