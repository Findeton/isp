# D24 — the tree birth kernel: the first exact birth-kernel exhibit, and its click identifiability

**Status:** PIN (pre-receipt), 2026-07-12; committed before `code/d24_tree_birth_kernel_exact.py` runs. Provenance labels per D20. Campaign context: goal clause (1) (birth kernel) + the F8 front inherited from paper 18 §8.

## 1. The two readings of one family

The D23 witness family generalizes to rooted controlled-rotation trees. Read statically, it is the interaction-graph identifiability class (the F7/F8 closure). Read **dynamically, it is a birth process**: each edge is a BIRTH EVENT — a new register is created in `|0>` and coupled to its parent by controlled-Ry — and the tree family becomes the first exact exhibit of a birth kernel satisfying every clause-(1) constraint of the campaign goal:

- **locality (collar attachment):** every birth attaches at one existing register (the control); no global state is consulted;
- **isometry / no silent creation:** the birth map is `V_e : H -> H (x) H_new`, `|psi> -> cRy_e(|psi> (x) |0>)` — an isometry; global purity is preserved at every step; the newborn's content is received FROM the parent sector (its click marginal is an exact function of the parent's content and the edge coupling: `P(child=1) = g_e * P(parent=1)`), never minted from nowhere;
- **ledger balance:** preparation distinctions at the root remain distinguishable in the total state at every growth step (isometries are injective) — nothing lost, nothing silently created, across every birth;
- **construction-order gauge:** all linear extensions of the tree's causal edge order produce the SAME final state and click law. Lemma: two edges sharing no register commute; two edges sharing only the control commute (controls are untouched in the Z basis); an edge into a register and that register's outgoing edges are causally ordered by birth. Hence birth order is bookkeeping — exactly the cg-line requirement.

**The kernel's free data** — which collar attaches next, and the per-birth coupling `g_e` — is NOT fixed by these constraints (paper 8's extension-rulebook-is-extra-physics, now confirmed at the birth level by exhibit). Two admissible kernels differing in that data differ in click law — and the tree theorem makes the difference identifiable: the kernel is empirical, and clicks can pin it.

## 2. Receipt gates (`code/d24_tree_birth_kernel_exact.py`; stdlib Fractions; exit 1 on any failure)

- **G1 (exhibit):** grow trees by sequential births from a prepared root ((cos, sin) = (3/5, 4/5)); exact normalization and positivity of every click table; global purity exactly 1 at every step.
- **G2 (construction-order gauge):** for the 4-register tree {A->B, A->C, B->D}, ALL linear extensions of the causal edge order yield the identical final click table, keyed by register identity (exact equality).
- **G3 (no silent creation / reception at birth):** the newborn's marginal obeys `P(child=1) = g_e * P(parent=1)` exactly at every birth on the coupling grid; root-preparation distinctions have distinct total states at every step (injectivity on a preparation grid).
- **G4 (fixed-carrier reduction, wiring-grade):** the grown web's click law equals the click table of the same circuit built by an independent static constructor (separate code path) — exact byte equality. In windows with no births the law IS the fixed-carrier conditional measure.
- **G5 (identifiability — the tree theorem, exhaustive small cases):** all labeled rooted trees on 3 and 4 registers (3 and 16 trees), per-edge couplings from an interior grid — zero click-law collisions across each class; the recovery procedure verified: ancestor sets from the exact zero-probability patterns `P(child=1, ancestor=0) = 0`, couplings from exact conditional ratios.
- **G6 (family non-uniqueness):** two admissible kernels (chain-growth vs star-growth schedules, same constraints) both pass G1–G4 and print different click laws — the constraints admit a family; selection is empirical.
- **G7 (boundary honesty, prints):** silent edges are click-invisible at all couplings; in-degree >= 2 breaks the cascade (angle addition) — the identifiability-class boundary carried verbatim from the round-1 rebuild.

## 3. What this does and does not claim

**Does:** exhibit an exact birth kernel meeting the goal's clause-(1) constraints (locality, isometry, ledger balance, order gauge); prove the kernel family is click-identifiable within the tree class; confirm the constraints do not select the kernel (extra physics).

**Does not:** select THE kernel of this reality (that is empirical — the cosmological-shadow work of D26); model spacetime, energy scales, or the real attachment law; make any geometry, cone, dimension or G claim; touch V9.

## 4. Round-1 hostile fronts (pinned)

(F1) Is the "reception at birth" gate (G3) the right no-silent-creation formalization, or does it need the D25 complementary-channel form? (F2) Does the order-gauge lemma cover all tree shapes or only the tested one — state the general proof or scope it. (F3) The identifiability recovery at boundary couplings and non-tree targets — boundary carried honestly? (F4) Does the dynamical reading add anything beyond relabeling the static family — name the exact delta (the isometric growth semantics + gauge lemma + reduction gate).
