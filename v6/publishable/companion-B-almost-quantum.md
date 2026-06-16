# Transverse record correlations land on the almost-quantum set: a foundations companion

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, companion to publishable Paper Va/Vb (foundations), version 2026-06-15.

## Abstract

This is a companion note to the sealed-records foundations paper. The
parent papers reconstruct single-chain quantum structure from a ledger of
committed records; here we ask the *transverse* question — what the records
can say about the correlations of two entangled chains — and report a
positioning result, not a new theorem. The setup is sharp and the honesty
mandate of this companion is to state it up front. **What is external (the
field's, not ours):** that a positive-semidefiniteness constraint on a
bipartite moment matrix is the NPA hierarchy and at its lowest cross-party
level caps the CHSH expression at Tsirelson's `2√2` (Navascués–Pironio–Acín
2007; Tsirelson 1980); that the feasible set of such a moment matrix at the
level `1 + AB` — positive-semidefinite, commuting-on-the-state, with **no**
Hilbert tensor factorization — *is* the **almost-quantum set
`Q̃ = Q^{1+AB}`** of Navascués–Guryanova–Hoban–Acín (2015), which strictly
contains the quantum set `Q`; and that the input which would cut a
tensor-product theory down to complex quantum theory is **local
tomography** `K_AB = K_A·K_B` (Hardy 2001; Chiribella–D'Ariano–Perinotti
2011; Wootters). All of this is the device-independent and
quantum-reconstruction literature. The records **instantiate** these
constructions; they do not invent them. **What is program-internal (the
contribution of this note):** a **no-go about the records**. A
self-consistency principle that the record substrate can host is, by the
substrate's own structure, a **moment-positivity** (Gram-PSD) condition on
the shared cross-moments `⟨A_x B_y⟩` of the two chains — and *therefore* it
cannot pin the entangling content `χ_AB` below `Q̃`, because the records
furnish no composite state space (no tensor product, hence no local
tomography). The supraquantum gap `Q̃ ∖ Q` is permanent for any
record-internal principle; `χ_AB` is free up to `Q̃`; and the same
moment-positivity that fails to pin `χ_AB` does *inherit* Tsirelson's
`CHSH ≤ 2√2` as a bound. The net statement is a positioning: the records
reproduce the field's `Q`-versus-`Q̃` wall **from the inside**, and the one
missing input is named — the composite state space. Numeric claims are
carried by receipts `t1`, `t2`, `t3` in the program's v7 code repository.

## 1. What is external and what is internal (stated first)

This companion makes one program-internal claim, and it is a claim *about
the records*, not a mainstream theorem. To keep the boundary clean we draw
it before any argument.

**External — inherited wholesale, cited not claimed.**

- *Moment positivity bounds CHSH at `2√2`.* That positive-semidefiniteness
  of a bipartite moment (Gram) matrix at the lowest cross-party level
  already certifies the Tsirelson ceiling is the NPA hierarchy at level
  one (Navascués–Pironio–Acín 2007); the bound itself is Tsirelson's
  (1980). We do not rederive it; we observe the records' constraint *is*
  this constraint.
- *The almost-quantum set.* The feasible correlation set of a moment matrix
  at level `1 + AB` — PSD, with on-state commutation `B_y A_x = A_x B_y`
  but **no** tensor factorization — is by definition the almost-quantum set
  `Q̃ = Q^{1+AB}` of Navascués–Guryanova–Hoban–Acín (2015), with `Q̃ ⊋ Q`.
  This set, its definition, and its strict containment of `Q` are theirs.
- *Local tomography selects complex quantum theory.* That `K_AB = K_A·K_B`
  — the joint state is fixed by local measurements — is the axiom which,
  inside a tensor-product world, distinguishes complex quantum theory from
  its real-vector (rebit) twin is Hardy (2001), Chiribella–D'Ariano–
  Perinotti (2011), and Wootters. We do not motivate it anew.
- *Tsirelson's problem.* That commuting-on-the-state is strictly weaker than
  tensor-factorization at every finite level (the commuting-operator and
  tensor-product correlation sets differ) is Slofstra (2019) and
  Ji–Natarajan–Vidick–Wright–Yuen (2020).

**Internal — the contribution of this note, a no-go about the records.**

> *Any self-consistency principle the record substrate can express is a
> moment-positivity condition on the chains' shared cross-moments; therefore
> it cannot pin `χ_AB` below the almost-quantum boundary. The records carry
> no composite state space, so the supraquantum gap `Q̃ ∖ Q` is permanent,
> `χ_AB` is free up to `Q̃`, and the field's `Q`-versus-`Q̃` wall is
> reproduced from inside the records — with its one missing input named: the
> composite state space (the tensor product, and within it local
> tomography).*

The corollary is also internal but smaller: the *same* moment-positivity
**inherits** the Tsirelson bound — it caps the records' own CHSH at `2√2`.
Everything below is the argument for these two statements; nothing below
claims a new result in quantum foundations proper.

## 2. The transverse arena is a moment matrix

The parent's single-chain self-consistency principle (axiom C) is a balance
between two functionals of the *same* one-diamond law, and it fixes the
single-chain constants. Its transverse analog must be a closure condition
on the *joint* correlations of two chains `A` and `B` that share entangled
content. The decisive structural fact is **how the two chains are
coupled**, and the answer is what makes the no-go.

In the record substrate the two chains are not glued into a global state
space. They meet only where their seals meet — through the joint moments
`⟨A_x B_y⟩` of the bipartite correlation. A record interface commits a
single joint outcome pair `(a, b)`, furnishing the degree-`(1,1)` cross
moment `⟨A_x B_y⟩` together with the within-chain moments, and nothing
higher. The coupling between the chains is the algebraic relation
`B_y A_x = A_x B_y` *on the state* — the joint moment is symmetric — and
**not** a tensor factorization `H_A ⊗ H_B`. There is no global product space
to factor through; there is only the shared moment and its symmetry.

Consequently a self-consistency condition is a positivity requirement on the
matrix of these moments: the Gram/moment matrix `Γ`, whose entries are
`⟨A_x⟩`, `⟨B_y⟩`, `⟨A_x B_y⟩`, and the within-chain moments, must be
positive-semidefinite — it is a matrix of inner products of the substrate's
own statistical observables, so `Γ ⪰ 0` is *forced*. This is exactly the
data that defines a moment-matrix relaxation of the quantum correlation
problem at the level **`1 + AB`** (the identity, the single operators
`A_x`, `B_y`, and their products `A_x B_y`). Receipt `t1` builds `Γ` for the
CHSH scenario and confirms the load-bearing point: the chains meet through
`⟨A_x B_y⟩ = E_xy` with `B_y A_x = A_x B_y` on the state, *not* through a
tensor product (`t1` checks the trivial point `E = 0` and the full CHSH
sweep are feasible exactly as moment-PSD problems). Any self-consistency
principle the substrate can host is a balance or extremum over the PSD cone
of such moment matrices.

One premise is flagged, not hidden: that the level is `1 + AB` and no
higher is a *substrate-modeling* assumption — a record interface commits a
single joint outcome pair, furnishing only degree-`(1,1)` cross moments. A
substrate that committed higher cross-party words would reach a higher
relaxation level. The qualitative no-go below does not depend on this
premise (§3); only *how far* above `Q` the records land does.

## 3. The no-go: the records land on `Q̃` and cannot pin `χ_AB`

By the Navascués–Guryanova–Hoban–Acín definition, the set of bipartite
correlations realizable by a moment matrix at level `1 + AB` — PSD,
on-state commutation, no Hilbert tensor factorization — *is* the
almost-quantum set `Q̃ = Q^{1+AB}`. So under the substrate model of §2,
every self-consistency principle the records can express selects a subset
of `Q̃`. This is the externally-named set; what is internal is that the
records' own self-consistency lands exactly on it.

**`Q̃` is necessary — the parent's envelope falls out.** The
almost-quantum boundary reproduces the entire envelope the joint click-law
respected, with nothing imported. Receipt `t1` solves the SDP over the
`1 + AB` moment cone:

- moment-positivity **caps** `CHSH` at the Tsirelson value: the NPA
  level-1 maximum equals the analytic bound `2√2 = 2.8284271247…` to SCS
  solver tolerance (SDP residual `|max − 2√2| ≲ 10⁻⁹`, run-dependent at
  that level — the last digit is solver noise, not a derived figure);
- the **PR-box** `(CHSH = 4)` is **excluded** — the correlator
  `E = (1, 1, 1, −1)` is **infeasible** in the `1 + AB` moment matrix;
- the **Tsirelson point** `(+,+,+,−)/√2` (`CHSH = 2√2`) is feasible/optimal,
  and a point just past it (`CHSH = 2.9084`) is infeasible — a sharp
  boundary.

So no-signaling (the marginals decouple in `Γ`), the Tsirelson ceiling, and
PR-box exclusion are entailments of moment-positivity, not extra postulates.
A quantum (tensor-product) realization gives a moment matrix of exactly this
form, so `Q ⊆ Q̃`: any transverse self-consistency principle the records
can host **necessarily** admits at least the quantum envelope.

**`Q̃` is not sufficient — it strictly overshoots `Q`.** The containment is
strict: `Q̃ ⊋ Q`. The CHSH facet does not witness it (there `Q̃` and `Q`
coincide at `2√2`, which is why the bound above looked like "just `Q`"), but
higher Bell functionals do. Receipt `t1` exhibits the strict relaxation
*nesting* on the three-input `I3322` functional: the `1 + AB` (level-1)
optimum `8.748210` strictly exceeds the level-2 optimum `8.000000`
(gap `0.748210 > 0`), so the `1 + AB` set is a strict outer relaxation, not
yet `Q`; and the converged quantum value (Collins–Gisin
`0.2508753845139766`) requires NPA level `≥ 4` (Pál–Vértesi), which the
substrate's `1 + AB` data cannot express. A principle confined to `1 + AB`
moment positivity therefore admits supraquantum correlations in `Q̃ ∖ Q`;
it cannot single out `Q`, let alone one `χ_AB` within it.

**The gap is permanent and level-independent.** The conclusion that `χ_AB`
is free *strictly above* `Q` survives whether or not the level is exactly
`1 + AB`. At *every* finite NPA level the records still furnish no global
tensor factorization: commutation-on-the-state is strictly weaker than a
tensor product — the negative resolution of Tsirelson's problem (Slofstra
2019; Ji–Natarajan–Vidick–Wright–Yuen 2020). What the level controls is
only *how far* above `Q` the records land — `Q̃` if the level is `1 + AB`,
a tighter supraquantum set if higher moments are committed — never *whether*
the gap exists. The gap `Q̃ ∖ Q` is therefore **permanent** for any
record-internal self-consistency principle, because every balance condition
expressible on the shared moment matrix lives at or below a finite moment
level by construction, and no finite level reaches `Q`.

**Verdict.** A transverse self-consistency principle is
*necessary-but-not-sufficient*: it reproduces the joint-law envelope and
leaves `χ_AB` free across the whole almost-quantum set. The entangling
content is **not** forced by anything the records can express. The
parallel-chain analog of the single-chain balance does not exist as a
content-pinning principle — only as an envelope-pinning one.

## 4. The one missing input: a composite state space

The supraquantum gap is not a vague deficiency. It traces to a single
missing structure — the records furnish no composite state space at all —
which shows up as two distinct, externally-named inputs the records lack.

The first would cut `Q̃` down to `Q`: the **global tensor product**, the
composite factorization that the commuting-on-the-state moment data lack
(§3). The second is what would then single complex quantum theory out from
its real-vector twin *within* the tensor-product world: **local tomography**
`K_AB = K_A·K_B`. These are not the same axiom — a real-vector (rebit)
theory *has* a tensor product yet *fails* local tomography — but they share
one origin: a substrate with no composite state space supplies neither.
Receipt `t2` makes the second quantitative through the information-dimension
count `K` (the number of real parameters fixing a state):

- complex quantum theory satisfies local tomography: `K_qubit = 4`,
  `K_2qubit = 16 = 4·4`;
- real-vector (rebit) theory does **not**: `K_rebit = 3`, but
  `K_2rebit = 10 ≠ 9 = 3·3` — a limited-holism deficit
  `K_AB − K_A·K_B = 1`, joint parameters invisible to local measurements.

The record seal is **blind to both**. The single-chain forcing that fixes
the seal — orthogonal projection `E = E² = E*` and the `q = 2`
Banach–Lamperti norm screen of the parent paper — holds *identically* over a
real and a complex Hilbert space. Receipt `t2` verifies this field-blindness
directly: the real (rebit) seal satisfies `E = E²` (`True`) and `E = E*`,
the complex seal satisfies `E = E²` (`True`), and the `q = 2` argument uses
the norm only, so it cannot tell the two fields apart. A real-vector theory
is the explicit foil: same marginals, same Tsirelson bound `2√2`, but a
different entangling content `χ_AB`. Because the seal cannot tell the real
theory from the complex one — and the moment data cannot tell a
commuting-operator model from a tensor-product one — no principle built on
the seal can supply either input.

The two faces are one obstruction: the records carry every constraint that
lives on the shared moment matrix and none that requires a composite state
space. That obstruction is *why* the moment-positivity of §3 cannot reach
below `Q̃`.

## 5. The positive corollary: Tsirelson is inherited

The no-go has a genuine positive complement. Although the substrate cannot
*pin* `χ_AB`, it does *bound* it, and the bound is Tsirelson's — inherited
from the records' own self-consistency rather than imported.

**The bound is a corollary of moment-positivity.** The same condition that
defines the no-go arena already supplies the ceiling. `Γ` is a Gram matrix
of the substrate's own observables, so `Γ ⪰ 0` is forced; and §3's SDP shows
`Γ ⪰ 0` caps `CHSH` at exactly `2√2` (receipt `t1`: maximum equal to the
analytic `2√2 = 2.8284271247…` to SCS solver tolerance, with a point just
past the bound infeasible).
For the records, then, Tsirelson's ceiling is not an external postulate
respected from outside — it is *inherited* from `Γ ⪰ 0`, the records' own
moment-positivity. (The theorem that moment-positivity caps CHSH at `2√2`
is, again, Navascués–Pironio–Acín / Tsirelson, not ours; what is internal is
only that the records' constraint coincides with it.) What stays free is
`χ_AB` *within* the ceiling; what is now sourced is the ceiling itself.

**An independent witness: the records own IC's static core.** The substrate
also carries the static information-theoretic core of Information Causality
(Pawłowski et al. 2009). In their derivation `CHSH ≤ 2√2` follows from a
mutual-information functional with four properties — non-negativity,
consistency (vanishing exactly on product distributions), a data-processing
inequality, and a chain rule — and receipt `t3` verifies the record KL
mutual information has all four: KL non-negativity, `I(A:B) = 0` iff
factorized (no-signaling-consistent), DPI, and a chain rule with residual
`3.63 × 10⁻¹²²`. The IC facet `V(E) = E² − ½` then lands at the Tsirelson
point and nowhere else (`t3`: `V < 0` sub-Tsirelson, `V = −9.7 × 10⁻¹²²`
i.e. `0` exactly at `E = 1/√2`, `V > 0` super-Tsirelson, PR-box maximally
violating; CHSH at `E* = 1/√2` equals `2.8284271247…`). So the records own
the static substrate of the IC route to the same bound.

**What it does not do.** Neither route pins `χ_AB`. Tsirelson's ceiling is
field-blind — the rebit foil of §4 saturates it too — so inheriting the
bound is fully consistent with `χ_AB` remaining free across `Q̃`. And the IC
route specifically is one lever short of full Information-Causality-as-
theorem: the static functional core is present, but the *operational*
random-access-code protocol that turns it into the dynamical IC statement is
not itself forced by the seal-law (receipt `t3`: the static substrate is
present, the operational protocol is not entailed). The honest scope is
therefore "Tsirelson inherited as a bound — as a corollary of
moment-positivity, additionally witnessed by the static IC core" — not
"Information Causality derived in full."

## 6. Positioning: the program's recurring shape

The contribution is a *positioning*: the records do not *answer* the open
device-independent question of what physical principle selects `Q` from
`Q̃` — they **reproduce that wall from the inside**, reaching exactly `Q̃`
and naming the one structure that would carry them to `Q` (the composite
state space). This is the program's recurring shape: the single-chain
self-consistency fixes the constants and the spacing's ceiling but never
the absolute scale (the parent line's scale no-gos for Newton's `G` and the
dimension `d`); the transverse self-consistency fixes the correlation
*envelope* — `Q̃`, the Tsirelson bound, PR-box exclusion — but never the
last record-blind structural input. Same shape, different missing input:
there an absolute length, here a composition rule.

## 7. What this companion claims and does not claim

**Claims (all program-internal, all about the records).** (1) Any transverse
self-consistency principle expressible on the record substrate is a
**moment-positivity** condition on the chains' shared cross-moments; under
the flagged substrate-modeling premise that a record interface commits a
single joint outcome pair, the level is `1 + AB` and the feasible set is
exactly `Q̃`. (2) That principle is **necessary** — it reproduces
no-signaling, the Tsirelson ceiling `2√2` (receipt `t1`: SDP max equal to
`2√2 = 2.8284271247…` to solver tolerance), and PR-box exclusion — but **not
sufficient**, strictly overshooting `Q` (receipt `t1`: `I3322` level-1
`8.748210` > level-2 `8.000000`, and `Q` needs NPA level `≥ 4`). (3) The
*qualitative* gap (`χ_AB` free strictly above `Q`) is **level-independent**:
commutation-on-the-state is not tensor-factorization at any finite level
(Tsirelson's problem), so the gap is permanent. (4) The one missing input is
the **composite state space** — the global tensor product (which would close
`Q̃ ∖ Q`) and, within it, local tomography `K_AB = K_A·K_B` (the
complex-over-real selector); the seal is blind to both (receipt `t2`:
`E = E² = E*` over `ℝ` and `ℂ`; rebit deficit `K_AB − K_A·K_B = 1`). (5) The
records **inherit** Tsirelson as a bound — a corollary of moment-positivity,
additionally witnessed by the static IC core (receipt `t3`: chain-rule
residual `3.63 × 10⁻¹²²`, IC margin `−9.7 × 10⁻¹²²` at saturation), one
operational lever short of full IC.

**Non-claims.** This companion does **not** derive complex quantum theory,
local tomography, or the tensor product — it proves their *absence* is the
obstruction. It does **not** pin `χ_AB` to any value, and does **not** claim
`Q̃ = Q` (the gap is strict and permanent). It does **not** claim to derive
Information Causality in full — only its static functional core. Crucially,
it claims **no novelty** in quantum foundations proper: the NPA hierarchy,
the almost-quantum set `Q̃`, the local-tomography selector, and Tsirelson's
problem are all external results, itemized with attributions in §1. The
records *instantiate* these constructions. The contribution is the **no-go
about the records**: their self-consistency is moment-positivity, so it
cannot pin `χ_AB` below `Q̃` — reproducing the field's `Q`-versus-`Q̃` wall
from the inside, with the missing input named.

## Reproducibility

Every numeric claim regenerates from fixed-seed scripts in the program's v7
code repository (`v7/code/`); reruns are deterministic for the exact and
mpmath quantities, and reproducible to SCS solver tolerance for the one SDP
value. Three receipts carry this companion. **`t1_npa_q_vs_qtilde.py`**
builds the `1 + AB` moment matrix, solves the CHSH SDP (max equal to the
analytic `2√2 = 2.8284271247…` to solver tolerance, `|max − 2√2| ≲ 10⁻⁹`
and run-dependent at that level), certifies PR-box infeasibility and the
sharp boundary at `2√2`, and exhibits the `I3322` relaxation nesting
(level-1 `8.748210` >
level-2 `8.000000`; `Q` needs NPA level `≥ 4`) — all checks pass (requires
`cvxpy`). **`t2_purification_uniqueness.py`** verifies the information-
dimension counts (`K_qubit = 4`, `K_2qubit = 16 = 4·4`; `K_rebit = 3`,
`K_2rebit = 10`, deficit `1`) and the field-blindness of the seal
(`E = E² = E*` over `ℝ` and `ℂ`) — all checks pass. **`t3_tsirelson_
derivation.py`** verifies the four IC functional properties of the record
KL mutual information (non-negativity, no-signaling-consistency, DPI,
chain-rule residual `3.63 × 10⁻¹²²`) and that the IC facet saturates exactly
at `E = 1/√2` (margin `−9.7 × 10⁻¹²²`, `CHSH = 2.8284271247…`), and audits
the one missing operational lever — all checks pass. Numeric residuals are
at mpmath `dps ≥ 100`; the SDP gap is at solver (SCS) tolerance.

## References

**Companion (this program).**
- *Quantum theory from sealed records I: Born composition, Lorentz
  signature, and the arrow of time* (publishable Paper Va, this batch) — the
  parent foundations paper: the sealed-records ontology (axioms R, S, C) and
  the single-chain reconstruction this companion extends transversally.
- *Quantum theory from sealed records II* (publishable Paper Vb) — statistics
  and the exchange-holonomy / dimension input.
- *The record click-law, IV* (v7) — the joint click-law and the free
  complement `χ_AB`; *The record click-law, VI: the transverse entangling
  content is free up to the almost-quantum set* (v7) — the full v7 treatment
  this note condenses.

**External.**
- M. Navascués, S. Pironio, A. Acín, *Bounding the set of quantum
  correlations*, Phys. Rev. Lett. **98**, 010401 (2007) — the NPA
  moment-matrix hierarchy; moment-positivity bounds CHSH at Tsirelson.
- M. Navascués, Y. Guryanova, M. J. Hoban, A. Acín, *Almost quantum
  correlations*, Nature Communications **6**, 6288 (2015); arXiv:1403.4621 —
  the set `Q̃ = Q^{1+AB}`.
- B. S. Tsirelson (Cirel'son), *Quantum generalizations of Bell's
  inequality*, Lett. Math. Phys. **4**, 93 (1980) — the `2√2` bound.
- W. Slofstra, *The set of quantum correlations is not closed*, Forum of
  Mathematics, Pi **7**, e1 (2019); Z. Ji, A. Natarajan, T. Vidick,
  J. Wright, H. Yuen, *MIP\* = RE*, arXiv:2001.04383 (2020) — the negative
  resolution of Tsirelson's problem (commuting-operator ≠ tensor-product
  correlation sets), the level-independent support for §3.
- L. Hardy, *Quantum theory from five reasonable axioms*,
  arXiv:quant-ph/0101012 (2001) — local tomography as an axiom.
- G. Chiribella, G. M. D'Ariano, P. Perinotti, *Informational derivation of
  quantum theory*, Phys. Rev. A **84**, 012311 (2011) — purification and
  local tomography.
- W. K. Wootters, *Local accessibility of quantum states*, in *Complexity,
  Entropy and the Physics of Information* (1990); *Entanglement sharing in
  real-vector-space quantum theory*, Found. Phys. **42**, 19 (2012) — real
  (rebit) quantum theory, the local-tomography foil.
- K. T. Pál, T. Vértesi, *Quantum bounds on Bell inequalities*, Phys. Rev. A
  **79**, 022120 (2009) — the `I3322` NPA-level analysis.
- M. Pawłowski, T. Paterek, D. Kaszlikowski, V. Scarani, A. Winter,
  M. Żukowski, *Information causality as a physical principle*, Nature
  **461**, 1101 (2009) — the static functional core the records own.
- J. A. Barandes, *The stochastic-quantum correspondence* (2023) — the
  indivisible-stochastic substrate underlying the record laws.
