# BC1 — DIVISION-EVENT COMPOSITION CONSISTENCY (RESULT)

**Status:** GREEN-UNREVIEWED, STRICT, 2026-07-28.  Not citable; terminal
is conferred by a hostile round.
**Programme:** BC — the Barandes consistency programme (bc/LOG.md #1).
**Pin:** bc/note-bc1-division-event-composition-pin.md.
**Receipt:** bc/code/bc1_composition_exact.py → bc/code/bc1_output.txt
(40 gates, 0 failures, 0 anchor failures, 28.5 s).

## Scope

The findings are formal properties of the framework of [B3]
(J. A. Barandes, *Quantum Systems as Indivisible Stochastic Processes*,
arXiv:2507.21192, 30 July 2025) as written, at the tested dimensions
(three qubits, |C| = 8; processes of dimension 2, 4 and 8) and the
tested dynamics (eight declared models plus an exhaustive population of
1,296 depth-4 circuits).  They are claims about that framework and about
nothing else: not about nature, not about quantum field theory, not about
any other programme in this corpus.  [B3]'s equivalence theorem is not
under test.  Every model here has rational transition matrices by
construction — a declared restriction on the tested dynamics, not on the
framework.  Nothing is sampled and nothing is random: every matrix entry
is a declared constant and every population is enumerated exhaustively.

## Verdict

**C-OBSTRUCTION**, with C-CROSS established a fortiori.

The division-event assignment of [B3] is not a restriction-compatible
family on the subsystem lattice.  There is no global, system-independent
division-event structure at these dimensions, and on some slices there is
no non-empty consistent assignment at all.

## The [B3] axioms used

Quoted verbatim and page-cited in the receipt's SEC 0 registry; the seven
that carry weight here are:

- **Kinematical axiom** ([B3] p.29): the configuration space is "a fixed
  feature of the model, meaning that it does not vary between real-world
  runs or instantiations of the model."
- **Dynamical axiom** ([B3] p.29): "For arbitrary target times, and for
  conditioning times corresponding to division events, the model's
  dynamical laws consist of transition probabilities that take the form of
  conditional probabilities…"
- **Epistemic axiom** ([B3] p.29): the standalone distribution "is
  contingent, meaning that it can vary between runs of the model."
- **Division events** ([B3] p.9): "Allowed conditioning times t_0 are
  called division events for the given system, and, without any real loss
  of generality, are assumed to include an 'initial' time 0."
- **System-centricity** ([B3] p.10): "Division events are not global
  properties of the whole universe, but are system-centric… they may be
  generated to an extremely good approximation through interactions with
  other systems, after marginalizing over those other systems."
- **The law of total probability and eqs. 22–23** ([B3] pp.9–10): the
  divisibility relation Γ(t←t_0) = Γ̃(t←t')Γ(t'←t_0) with Γ̃ = Γ(t←t_0)
  Γ⁻¹(t'←t_0), which "will generically fail to be a column stochastic
  matrix."
- **Unistochasticity and the stochastic-quantum theorem** ([B3] pp.18–19).

## The predicate

Conjoining the dynamical axiom, the division-event definition and the law
of total probability gives the operational predicate the receipt computes:

> DIV_S(t_k) holds iff for **every** grid target t_b ≥ t_k there **exists**
> a column-stochastic X_b on C_S with X_b Γ_S(t_k←0) = Γ_S(t_b←0).

Universal over targets, existential over bridges; sources are the initial
time alone, which [B3] p.9 guarantees is a division event, so no later
time is assumed to be one.  This is U1's (D1) conjoined over the spanning
pairs that straddle t_k, and it is decided by U1's committed cascade
(candidate bridge → [B3] eq. 22 algebraic interpolant → row certificate →
exact rational LP with a verified Farkas certificate).

## The two readings

Both are declared, both are censused separately, and neither is merged
into the other.

- **Reading M (marginal).** Γ^M_S[u][v] = Σ_{i|_S=u} Σ_{j|_S=v}
  Γ(t←0)[i][j] p₀(j) / Σ_{j|_S=v} p₀(j).  Depends on p₀; three strictly
  positive p₀ are declared (uniform, product, correlated).
- **Reading C (conditional-on-outcome).** Γ^{C,c}_S[u][v] = Σ_{i|_S=u}
  Γ(t←0)[i][(v,c)], conditioned on the complement's configuration at the
  conditioning time.  Independent of p₀; indexed by a full configuration
  c* of the composite so that all seven subsystems are conditioned on one
  and the same global outcome, which makes the family functorial.

Reading M is exactly the column-wise p₀-mixture of the reading-C
processes, Γ^M[u][v] = Σ_c w_c(v) Γ^{C,c}[u][v] with w_c(v) = p₀((v,c)) /
Σ_{c'} p₀((v,c')); the identity is verified entry for entry (FUN.3).

## The sheaf structure

F(S) is the set of column-stochastic families on C_S for S in the lattice
{A,B,C,AB,AC,BC,ABC}; the restriction ρ^S_{S'} is marginalisation
(reading M) or conditioning (reading C).  Both restrictions are **verified
transitive** (FUN.1, FUN.2: 1,440 and 1,680 nested instances, zero
disagreements), so F is a presheaf and the language is load-bearing rather
than decorative.

The axioms for a global division-event assignment D: L → P(T), stated in
the receipt before any of them is evaluated:

- **GS0 initiality.** 0 ∈ D(S) for every S.  Ground: [B3] p.9.
- **GS1 restriction-compatibility.** S'' ⊆ S' ⟹ D(S') ⊆ D(S'').  Ground:
  the restriction map is marginalisation, which [B3] p.10 names as the
  operation relating a system to its parts.  [B3] nowhere asserts GS1;
  GS1 is the weakest condition under which the assignment is a compatible
  family for the restriction presheaf.
- **GS2 gluing.** S' ∩ S'' ≠ ∅ ⟹ D(S') ∩ D(S'') ⊆ D(S' ∪ S'').
- **GS3 system-independence.** ∃ G with D(S) = G for all S.  This is the
  hypothesis [B3] p.10 explicitly denies; it is computed so the denial is
  quantified rather than quoted.

A global section, in the compatible-family sense, exists exactly when
GS0 ∧ GS1 ∧ GS2 hold of the computed family.  Where they do not, the
receipt computes the **maximal sub-section**: the largest d' ≤ d
satisfying GS1 ∧ GS2, by exhaustive search over all 2⁷ = 128 assignments
per grid slice.  The identically-empty d' always satisfies the axioms, so
the informative statements are (i) whether the data itself is a section
and (ii) whether the maximal sub-section is non-empty.

## R1 — The model census

Eight models on three qubits over the grid t_0 … t_4: a classical Markov
product control; a quantum product/separable model (Pythagorean rotations,
ℚ); a GHZ-generating real Clifford circuit (ℚ(√2)); a W-generating
rational orthogonal model (ℚ); an algebraic generic Cayley rational
orthogonal model (ℚ); a complex Clifford circuit (ℚ(ζ₈)); a
controlled-rotation entangler (ℚ); and a SWAP scrambler (ℚ(√2)).  Eleven
readings each, seven subsystems, five grid times: 616 census rows, 6,160
(D1) queries, 1,082 distinct decisions, 124 exact-simplex invocations.
Every unitary is exactly unitary in its ring with zero residual entries;
every |U_ij|² is exactly rational; no decision is excluded by a cap and
none is structurally vacuous.

The axioms, over the 88 (model, reading) pairs:

| axiom | holds |
|---|---|
| GS0 initiality | 88/88 |
| GS1 restriction-compatibility | 66/88 |
| GS2 gluing | 88/88 |
| GS3 system-independence | 22/88 |
| the family IS a global section | 66/88 |

Containments over the 1,056 (model, reading, nested pair) instances: the
downward containment DIV_{S'} ⊆ DIV_{S''} holds in 979 and fails in 77;
the upward containment holds in 706 and fails in 350.  Counted as
time-witnesses, 77 downward and 412 upward; collapsed over readings, 7
distinct downward and 70 distinct upward.

The containment the pin names, DIV_ABC ⊆ DIV_A ∩ DIV_B ∩ DIV_C, holds in
77 of 88 and fails in 11; the converse holds in 74 and fails in 14.

## R2 — The crossings, with exact witnesses

All seven distinct GS1 crossings reproduce in all eleven readings.

- **GHZ-generating Clifford, ABC > BC at t_2.**  DIV_ABC = {0,1,2,3,4},
  DIV_BC = {0,1,3,4}.  The obstructed spanning pair on BC is (t_2 → t_3):
  Γ_BC(t_2←0) has columns uniform on {00,10} and {01,11}, Γ_BC(t_3←0) has
  columns uniform on {00,11} and {01,10}, and the row certificate returns
  four obstructed targets with Farkas vector w = (1,−1,−1,1) and wᵀb = 1 >
  0 on each.  On ABC both spanning pairs from t_2 carry a bridge.
- **SWAP scrambler, six pairs at t_1** — ABC > A, ABC > B, ABC > AC,
  ABC > BC, AB > A, AB > B.  Γ_ABC(t_1←0) is a permutation matrix, which
  [B3] p.10's own lemma identifies as the only stochastic matrix with a
  stochastic inverse, so t_1 is a division event for the composite by the
  strongest available route; the single-system marginals at t_1 are flat
  and cannot reach the identity at t_2, so t_1 is not a division event for
  A or for B.

The upward crossings (a subsystem divides where its container does not)
occur in five of the seven quantum models and are the generic case.

## R3 — The exhaustive circuit sweep

Every circuit of depth 4 over the six-letter alphabet {H_A, H_B,
CNOT_{A→B}, CNOT_{B→C}, SWAP_{AC}, R_A(3/5,4/5)} — 1,296 circuits,
exhaustive, unsampled, five Clifford letters and one non-Clifford letter.
Each gate is written U = √w · V with w rational and V rational, so Γ = w ·
V∘V is rational by construction and unitarity is w · VᵀV = 1, checked
exactly on every partial product.  181,440 (D1) queries, 3,807 distinct
decisions, 3,817 exact-simplex invocations, 600 Farkas certificates
verified, zero eq.-22 disagreements.

| outcome | reading M (p_unif) | reading C (c\* = 000) |
|---|---|---|
| GS1 fails | 527 / 1296 | 361 / 1296 |
| GS2 fails | 85 / 1296 | 77 / 1296 |
| GS3 fails | 1004 / 1296 | 884 / 1296 |
| the family IS a global section | 688 / 1296 | 865 / 1296 |

All twelve nested pairs of the lattice carry GS1 crossings under the
conditional reading, and ten of the twelve do under the marginal reading;
ABC > BC is the most frequent (604 under reading M, 419 under reading C).
All three overlapping triples carry GS2 failures.  The
DIV_ABC spectrum runs from the full grid (727 circuits) down to {0,4} (68
circuits).

**GS2 fails in the population although it holds across all eight
hand-chosen models.**  The obstruction is therefore not confined to the
restriction axiom.

## R4 — The hard obstruction

Ten grid slices in the sweep admit **no non-empty** assignment d' ≤ d
satisfying GS1 ∧ GS2.  The mechanism is exact: a composite carries a
division event while none of its three constituent single systems does, so
GS1 forces every atom of that composite into any non-empty section and the
data does not supply them.  Exemplar, reproduced under both readings:

    circuit H_B · SWAP_AC · H_B · SWAP_AC, at t_2
    A=0  B=0  C=0  AB=0  AC=1  BC=0  ABC=0

This is the marginal-problem obstruction in its strongest available form
at these dimensions.

## R5 — The reduced processes are generally not unistochastic

U3's committed criterion, anchored on its own known-answer battery before
use, applied to every screened instance.  The composite: 21 of 32
certified unistochastic with the model's own unitary exhibited as the
certificate, 4 rejected for failing double stochasticity (the classical
control), 7 excluded by the declared cost cap.  The reduced processes,
1,152 instances: 402 are column-stochastic but not doubly stochastic,
hence not unistochastic; a further 12 are doubly stochastic and still fail
the polygon obstruction; 438 (all n = 2) are certified orthostochastic;
300 are excluded by the declared caps and reported as neither.  This is
[B3] p.19's second disjunct made concrete: the subsystem of a
unistochastic process is an indivisible stochastic process that is not
itself unistochastic and would need a dilation.

## R6 — The two readings are not the same census

Over the 280 (model, subsystem, grid index) slices: the marginal reading
depends on p₀ on 6 slices, the conditional reading depends on which
outcome the complement is conditioned on for 16 slices, and the marginal
and conditional readings disagree on 18.  Reading M carries 21 of the 77
GS1 time-witnesses and reading C carries 56.

## R7 — [B3]'s own candidate bridge

For a closed unistochastic system, |U(t←t')|² with U(t←t') = U(t←0)
U(t'←0)† is always column-stochastic and is the natural candidate for
Γ(t←t').  Over the 70 spanning pairs of the seven unitary models it
satisfies eq. 23 in 46 and fails in 24.  Wherever it satisfies eq. 23 the
existence test returns DIVISIBLE, as it must; the converse does not hold
and is not claimed.

## Anchors

- **SRC.1–SRC.3.** Both reused instruments pass an AST signature pass and
  are lifted by AST from the committed files, never retyped.
- **KA-LP1–KA-LP3.** The exact Phase-I simplex finds a hand-known feasible
  point; returns a hand-known infeasibility with an independently verified
  Farkas certificate; and agrees with the [B3] eq. 22 algebraic instrument
  and with the closed form |λ_b| ≤ |λ_k| on the 2×2 bistochastic family in
  both directions.
- **KA-U3a–KA-U3e.** U3's own known-answer battery reproduces: J/3 has
  T = +1/27 and no polygon violation; (J−I)/2 is bistochastic with
  T = −1/16 and a flagged polygon obstruction; the n = 2 construction is
  exactly orthogonal; the doubly-stochastic precondition is not a no-op;
  Sylvester's H₈ satisfies HHᵀ = 8I.
- **KA-RING, MOD.1, MOD.4, SWP.0.** The exact rings behave; every
  transition matrix is exactly rational; every declared U is exactly
  unitary with zero residual entries; every alphabet letter is exactly
  unitary.
- **SAN.1, SAN.2.** The classical Markov product control divides
  everywhere — 385 (reading, subsystem, time) slots, all true — and
  satisfies all four axioms including GS3, so the axiom set is satisfiable
  and the obstruction is not an artefact of stating an unsatisfiable set.
- **SAN.3, SAN.4.** The known-indivisible reference, a single qubit under
  R(3/5,4/5), has DIV = {0,2,3,4}, a proper subset of the grid, and the
  instrument reproduces the closed form exactly; the reference is the
  product model's own A factor rather than a separate fixture.

## Two results worth stating separately

- **Separability does not confer divisibility.**  The quantum product
  model, whose dynamics and whose state both factorise across A, B and C
  at every time, has DIV_ABC = {0,4}, a proper subset of the grid.  What
  divides everywhere is the classical Markov product, not the separable
  quantum one.
- **GS0 and GS2 survive the model census; GS1 and GS3 do not.**  Locating
  the failure matters: the assignment is not merely non-global, it is not
  restriction-compatible, and in the wider population it is not even
  locally coherent.

## Caps, and what they can hide

The LP caps inherited from U1 (≤ 700 variables, ≤ 400 constraints,
≤ 400,000 pivots) are never approached: every system here has at most 64
variables and 72 constraints, so no division-event decision is excluded by
a cap and none is structurally vacuous.  One cost cap is declared and does
bite: U3's polygon oracle needs an exact square-free factorisation, and it
is invoked only when the integer handed to it is at most 10⁹ or is
1000-smooth; 65 screened instances are reported as EXCLUDED-BY-COST on
that ground, and a further 242 as EXCLUDED-BY-CAP because at n = 4 the
criterion supplies necessary conditions only.  Neither is ever reported as
a pass in either direction.  That cap touches only
the unistochasticity screen of R5, which is decided by factorisation; the
division-event census is decided entirely in Fractions by an LP with no
factorisation anywhere.

## What this does not say

[B3] is not shown to be inconsistent.  [B3] nowhere asserts GS1, and p.10
asserts the opposite of GS3.  What the census establishes is that
system-centricity is forced rather than merely permitted — it holds on
1,004 of 1,296 circuits under the marginal reading — and that the
resulting assignment has the shape of a marginal problem with exact
witnesses, up to and including slices where the only consistent global
assignment is the empty one.  Whether a weaker set of consistency axioms
than GS1 ∧ GS2 admits a non-trivial global structure is not addressed
here.

## Determinism

The receipt reproduces byte-identically under PYTHONHASHSEED 0 and 12345
with timestamps excluded; every printed aggregate is ordered by U1's
hash-seed-independent key sk().

## Files

- bc/code/bc1_composition_exact.py
- bc/code/bc1_output.txt
- bc/note-bc1-division-event-composition-pin.md (the pin)
