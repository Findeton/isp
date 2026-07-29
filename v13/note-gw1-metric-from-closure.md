# v13 GW1 — METRIC RECONSTRUCTION FROM DEFORMATION CLOSURE:
# THE INSTRUMENT CENSUS

**Status:** GREEN-UNREVIEWED, STRICT, 2026-07-28.
**Pin:** `v13/note-gw1-metric-from-closure-pin.md` (STEP 0, the
instrument census, promoted there to a first-class verdict).
**Binding:** v13 paper 0 `[DRAFT]` §2 (the three-defect separation),
§3 (the closure relation), §6 (GW1's five steps, controls and kill
condition); v13 LOG #1.  The draft stays `[DRAFT]`; nothing in it is
adjudicated here.
**Verdict:** **GW1-BLOCKED-AT-KERNEL.**
**Deliverable:** this census.  No `v13/code/gw1_*` receipt exists,
because STEP 0 does not pass and STEPS 1–5 are therefore not run.

---

## Scope box

The pin's three-defect separation is engraved and is not relaxed
anywhere below.  Quoting v13 paper 0 §2:

> $$\Delta^B \;\neq\; \Omega_{\mathrm{hypersurface}} \;\neq\;
> R^{\rho}{}_{\sigma\mu\nu}.$$
>
> They can be related, but identifying them would repeat the v1 $H^1$
> mistake at a higher level.

Nothing below identifies any two of them.  No claim about Einstein
dynamics of any kind is made: v13 paper 0 §5 is out of scope, and the
census carries no statement about field equations, backreaction,
constraint preservation or a geometry-update law.  Grades quoted for
located objects are the cited papers' own; this note confers none.

---

## 1. What STEP 0 requires

Two instruments, in runnable form, **on one and the same committed
substrate**:

- **(i)** an order/count metric-reconstruction instrument
  `q^ij_order`;
- **(ii)** committed finite deformation kernels `J_a[N]` carrying the
  exchange two-cell
  `Ω_a[N,M] = J_a[M|N] J_a[N] ( J_a[N|M] J_a[M] )⁻¹`,
  whose construction is exhibited **without the metric**.

Instrument (i) is present and runnable.  Instrument (ii) is not.  Every
committed kernel family drops one of the three things the pin requires
— the lapse argument, the metric-freeness, or a nontrivial two-cell —
and the one family that drops none carries no code and is 1+1D, where
there is no metric to recover.  No substrate carries both instruments.

---

## 2. Instrument (i): PRESENT, RUNNABLE

The causal-set/sprinkling substrate carries an order+count metric
reconstruction, and it runs.

| object | file | what it returns | grade owner |
|---|---|---|---|
| flat metric from interval cardinalities | `code/v6_task2b_metric_extraction.py` | full `g_{μν}` from order+number | v6 |
| curved conformal factor, two channels | `code/v6_p2d_curved_coefficient.py:74-139` | `Ω` from longest chains and from counts | v6 paper 2 §4 |
| oriented spatial frame | `code/v6_p2_spatial_direction.py`, `code/v6_p2b_local_frame.py` | slice coordinates from the causal graph Laplacian | v6 paper 2 §2 |
| conformal class, volume measure | `v8/code/r1_order_to_conformal_direction.py`, `r2_number_volume_lstep.py`, `r3_manifoldlikeness_myrheim_meyer.py` | directions and volume ratios; absolute scale walled | v8 paper 4 §1–§2 |
| order dimension, volume-faithfulness | v9 papers 4, 6 | `dim ≤ 2`, `D*_N → 0`; **no spatial metric** | v9 |
| frozen ruler card, incl. a spacelike distance | `v10/code/d29_ruler_validation.py` (`:72-140`; the common-diamond distance at `:111-113`) | order-only `d_MM`, chain rulers, spacelike separation; validated against held-out truth at `d = 2,3,4` | v10 D29 |
| transverse coordinates from order | `v8/code/k3_decoration_probe.py`, `l2_intrinsic_finder.py`, `m1_intrinsic_4d.py`, `m2_intrinsic_4d_scale.py`; `v9/code/n1_chi_dictionary.py`, `n2_chi_geometry.py` | MDS transverse seed from cross-chain coupling, scored by Procrustes against held-out geometry | v8, v9 |
| proper time from chains | `v9/code/dimwall_lorentz1.py` | interval-DP longest chain against the round interval | v9 |

Re-run under `code/.venv/bin/python3.13` (numpy 2.4.6, scipy 1.17.1):

- `v6_task2b`: 2D returns `g_tt = +1.00`, `g_tx = +0.01`,
  `g_xx = −1.01`, hence `g^xx = +0.99` against flat `+1`; 3D returns a
  spatial block `≈ −I₂`; the extraction is boost-covariant at
  `β = 0.5`.  1.9 s.
- `v6_p2d` PART 2 (`Ω` never inserted, declared at `:76`): the
  chain channel correlates `+0.993` with the true `1/Ω²`, the density
  channel `+1.000`, and the two independent causal channels agree at
  `+0.995`; centre/wing `0.214`.  0.35 s.
- `v6_p2_spatial_direction`: 1+1 Fiedler `|corr| = 0.94`; 2+1
  `R² = 0.95 / 0.92`.  16.7 s.

**Not this instrument.**  v4 paper 4's "metric detector table" is a
declared readout of an inserted background, not an order/count
reconstruction: Definition 11.1
(`v4/relativistic-isp-v4-paper4-operational-orientation-quorum-or-enriched-only-metric-diagnostic.md:820`)
writes the response law as `P = ½(1 + o λ_{ij} h^{ij}(x))` with
`h^{ij}` the fixed background, and Proposition 11.3 (`:866`) returns
`C_op^{ij}(x) = h^{ij}(x)`.  v4 carries no code directory; the object
is definition-only.

---

## 3. Instrument (ii): four families, none qualifying

Two independent requirements have to hold at once: the kernel must be
built without the metric, **and** it must carry a lapse argument, since
the closure relation `(Ω_a − I)/ε² ≈ K_i[q̃^{ij}(N∂_jM − M∂_jN)]` is
posed in `N`, `M` and `ε`.  Each committed family drops one.

### 3.1 Record-native kernels — metric-free, two-cell identically trivial

`code/v6_task2_antichain_deformations.py` advances a down-set by
absorbing minimal available events; the rule reads only the causal
order.  Its own scope line (`:14-16`) states that the structure
function "is NOT obtained here".

The two-order test is `code/v6_task2d_bracket_closure.py`, with the
diagnostic `v6_task2e` and the theorem `v6_task2f`.  The theorem
(`code/v6_task2f_nogo_confirm.py:4-8`): if a deformation absorbs `e`
iff a height field satisfies `h(e,D) ≤ s·N(e)` and `h` composes
pointwise-additively, then both orders reach
`D ∪ { e : h(e,D) ≤ s·(N(e)+M(e)) }`, symmetric in `N, M` — the
commutator is **exactly zero**.

Re-run: `|comm| = 0` at `N = 2000, 4000, 8000`; the recomputed-height
variant leaves `19 / 13 / 31` events of boundary residue, which
`v6_task2e` measures as gradient-blind (enrichment `~0.8`, no
localization on the target profile).  0.59 s.

Two consequences, both structural:

- `Ω_a[N,M] − I ≡ 0` for the whole pointwise-additive class, so the
  closure relation `(Ω_a − I)/ε² ≈ K_i[q̃^{ij}(N∂_jM − M∂_jN)]`
  carries no metric content: with `K_i` faithful it forces `q̃ = 0`,
  which is not `q^ij_order`.
- The down-set advance is irreversible (set union), so `J_a[N]⁻¹` does
  not exist and the pinned two-cell cannot be formed at all.  The
  corpus's substitute is the symmetric difference of the two final
  down-sets.

### 3.2 Embedding-flow / grid kernels — genuine two-cell, metric inserted

These carry a real two-order composition and a real two-cell.  The
metric enters their construction, at the line where the normal is
normalized.

| file:line | the insertion |
|---|---|
| `code/v6_p2c_flow_drift.py:32-36` | `nt = 1/sqrt(1-sl²)`, `nx = sl/sqrt(1-sl²)` — the Minkowski normalization of the normal |
| `code/v6_p2d_curved_coefficient.py:50-54` | `fac = (1.0/Omega(x)) if curved else 1.0`; `nt = fac/sqrt(1-sl²)` |
| `code/v6_p2e_3d_tensor_coefficient.py:42-47` | `gx = ixx*Tx + ixy*Ty` (raise with `h^{ab}`), `norm = sqrt(1 − h^{cd}∂_cT ∂_dT)` |
| `code/v6_p2f_4d_tensor_coefficient.py:38-47` | `raise_idx(cov)` = `h^{ab} cov_b`; same normalization in 3+1 |

Re-run results, and the control that prices them:

- `v6_p2c` PART 1: commutator drift vs `−ε²(NM′−MN′)` correlates
  `+1.0000`, slope`/(−ε²) = 1.001`.
- `v6_p2d` PART 1 — **the insertion, exhibited on one target by a
  committed control**.  With `Ω` in the normal: `corr(C, 1/Ω²) =
  +1.0000`, centre/wing `0.239` against the target `0.232`.  With `Ω`
  removed from the normal and nothing else changed:
  `corr(C, 1/Ω²) = +0.0109`, centre/wing `1.000`.  The two-cell
  returns the coefficient placed in the kernel, and returns a constant
  when none is placed there.
- `v6_p2e`, `v6_p2f`: measured drift vector against the tensor
  prediction `cos = 1.0000`; against the isotropic null `0.9729`
  (2+1) and `0.9739` (3+1); rotation measured `13.38°` vs predicted
  `13.38°`, and `13.13°` vs `13.13°`.  The measurement and the
  prediction read the same `h^{ab}` field (`v6_p2e:44` and `:58`), so
  the agreement is a kinematic consistency check, not a recovery from
  independent data.

At theorem level the same structure is declared, not concealed.  v4
paper 5 Definition 3.3
(`v4/relativistic-isp-v4-paper5-operational-curvature-compatibility-source.md:289-301`)
sets `J^{emb}_{op,a}[N] := T_a(Φ_N^ε)` and states it "is enriched
because `Φ_N^ε` is fixed-background geometric input"; Proposition 8.2
(`:663-674`) states the maps "are declared from fixed-background
normal deformation transports.  They are not derived as passive
functions of the current Gamma endpoint kernels."  The paper's exchange
two-cell (Definition 1.2, `:132-149`) and normalized curvature
(Definition 1.3, `:151-162`) are the pin's objects exactly, and are
definition-only: v4 has no code.

### 3.3 The Γ-level lattice kernels — two-cell real, metric inserted, recovery provably partial

v2 paper 1 proves that the finite exchange defect reaches the
tangential bracket in 1+1D.  v2 paper 10 asks whether its coefficient
is readable as inverse spatial metric data in higher spatial
dimension, on a fixed background.

- `h^{ij}` is fixed background geometry
  (`v2/relativistic-isp-v2-paper10-metric-data-from-stochastic-exchange-curvature-investigation.md:63`),
  entering through the Clifford relation
  `½{γ^i,γ^j} = h^{ij} I` (`:1825`).
- Proposition 10.4 (`:1237`): the leading Born-squared coefficient
  fails the rotated-metric cross-term test — it sees `h^{11}` and
  `h^{22}`, not `h^{12}`.
- Proposition 10.5 (`:1464`): the first higher-order signal is
  signless, giving `(h^{12})²`.
- Proposition 10.6 (`:1659`): an all-order sign-ambiguity no-go.  The
  frame flip `E₂ → −E₂` leaves every `Γ`-level datum invariant while
  sending `h^{12} → −h^{12}`.
- Verdict §14 (`:2001`): "not a positive full-metric reconstruction
  paper".

This substrate carries no order/count instrument; its geometry is a
fixed lattice with `h^{ij}` supplied.

The exact form of the same commutator `E = J_R J_S J_R⁻¹ J_S⁻¹` is
runnable at `v10/code/d43a_lie_trotter_exact.py:18-20` (order-12 exact
truncated series, `mp.dps = 50`), and in float at
`validate_minimal_interacting_gauge_matter_benchmark.py:93` and
`validate_truncated_u1_benchmark.py:119`.  In all three, `J` is
`Γ(U_loc)Γ(U_free)⁻¹` from a lattice Dirac Hamiltonian: region-supported
and parameterized by a slab thickness `Δ`, not by a lapse profile.

### 3.4 Record-history diamond and holonomy machinery — metric-free, nontrivial two-cell, no lapse argument

The corpus carries exact, runnable, order-native two-order-mismatch
machinery whose output is **not** trivial.  It is built from record
histories (down-sets) and `Fraction`-exact admission weights, with no
coordinates, no unit normal and no background field:

| file:line | the two orders | the measured mismatch |
|---|---|---|
| `v10/code/d42b3_placement_exact.py:390-398` | `h + [e1,e2]` vs `h + [e2,e1]` on record histories, gated on `canon(h12v) == canon(h21)` | 202 canonical diamonds, 36 chain-consistency violations |
| `v10/code/d49_dichotomy_settlement_exact.py:384-401`, `:890-909` | the same diamond census, chain-product form | the flatness ladder |
| `v10/code/d44f_foliation_measure_exact.py:394-410` | `def commutes(h, e1, e2)` with a positive and a gated negative control | exact commutation, and its designed failure |
| `v10/code/d74_transport_holonomy_exact.py:574-580` | `holonomy_of(edges, reverse_order)`, closed-square census | 88 of 1,546 closed squares non-unit |
| `v10/code/d72_weld_exact.py:927-960`, `v11/code/ld_reversal_probe_exact.py`, `u2_three_address_weld_exact.py`, `u3_unistochasticity_screen_exact.py` | reversal holonomy on closed squares | the corresponding censuses |
| `code/v6_p4n_exchange_cocycle_law.py:1-14` | the two internally available orderings of the same sealed record transports | `A_D = log dP_AB/dP_BA` |

None of these takes a lapse.  They advance a history by one **event**,
not by a profile `N(x)`, and they carry no `ε` and no `∂_j`.  The
closure relation cannot be posed on them: `N`, `M`, `ε_a` and the
gradient all lack referents.  What they measure is an exchange defect
of record placement, which the scope box keeps distinct from
`Ω_hypersurface`.

### 3.5 The closest committed lapse-parameterized metric-free construction — definition-only

`v3/relativistic-isp-v3-paper2-primitive-smooth-lapse-hypersurface-kernels.md`
builds `J_a[N]` from a smooth compactly supported lapse profile without
a metric in the kernel: Candidate B (`:204-237`) sets
`Γ_a^mix[N;Δ] := (1−ηa∑N_n)Γ_0(Δ) + ηa∑N_nΓ_n(Δ)`, hence
`J_a^mix[N;Δ] = I + ηa∑N_n(J_n − I)`, from exact endpoint stochastic
kernels; §6 (`:298-313`) then forms `E_a^mix[N,M;Δ] = J_N J_M J_N⁻¹ J_M⁻¹`,
with Theorem 6.1 (`:335-377`) and Theorem 7.2 (`:469-593`).  The
construction is metric-free; the lapse profile and the background
lattice are external input, and the target coefficient is the metric.
**`v3/` contains no code**: the family is definition-only, with no
receipt anywhere in the corpus, and no order/count instrument on its
substrate.

Theorem 6.1's limit is
`(E_a^mix[N,M;Δ] − I)/(η²Δ⁴) → K_∥[N∂_xM − M∂_xN]`, in **one** spatial
dimension.  v2 paper 10 prices what that can and cannot decide
(`:48-51`): "in one spatial dimension the metric question is almost
invisible: the coefficient is one scalar, and many normalizations can
hide inside the lapse, the lattice spacing, or the tangential
generator convention."  A GW1 run on this family would therefore need
`d ≥ 2` spatial dimensions, which is where §3.3's all-order
sign-ambiguity no-go applies.

---

## 4. The cross-cut

| substrate | instrument (i) | instrument (ii) | drops |
|---|---|---|---|
| causal set / sprinkling (v6 task2, v6 p2 PART 2; v8 §1–2; v9; v10 D29) | **runnable** | metric-free, lapse-parameterized kernels exist; two-cell **identically trivial**; the pinned two-cell not formable (no inverse) | the two-cell |
| record histories (v10 d42b3/d49/d44f/d72/d74; v11 ld/u2/u3; `v6_p4n`) | partial — the same order data | metric-free, exact, **two-cell nontrivial** | the lapse: no `N`, no `ε`, no `∂_j` |
| grid embedding-flow (v6 p2c/d/e/f PART 1; v4 p5 Def 3.3) | absent — the metric is declared input, not reconstructed | runnable two-cell, **metric inserted** at the normal | metric-freeness |
| Γ-level lattice (v2 p1, p10; v10 d43a; the root validators) | absent — fixed lattice | two-cell real and exact, **metric inserted** via `γ`; recovery blocked at `h^{12}` all-order; parameterized by `Δ`, not by a lapse | metric-freeness and the lapse |
| smooth-lapse kernels (v3 paper 2 Candidate B) | absent | metric-free, lapse-parameterized, two-cell nontrivial at Theorem 6.1 — **definition-only, no code in `v3/`**, and 1+1D | runnability; and, at `d = 1`, the metric itself |

No single committed substrate carries both instruments in runnable
form.  **GW1-BLOCKED-AT-KERNEL.**

The block has two faces, and neither is repairable by choosing a
different committed substrate.  Where the two-cell machinery is
metric-free and nontrivial, it has no lapse argument, so the closure
relation has no referents.  Where it is lapse-parameterized, the
two-cell is either identically trivial (record-native) or the metric is
inserted into the kernel (grid, lattice).  The one construction that is
both metric-free and lapse-parameterized carries no code.

**Where the runnable code is, and is not.**  `v1/`, `v2/`, `v3/`,
`v4/`, `v5/` and `publishable/` contain no `.py` at all, so every
object located in them — including v4 paper 5's exchange two-cell
(Definition 1.2) and embedding-flow kernels (Definition 3.3), v4
paper 4's metric detector table, v3 paper 2's smooth-lapse kernels, and
v2 paper 10's benchmark — is definition-only.  The runnable trees are
`code/`, `v7/code/`, `v8/code/`, `v9/code/`, `v10/code/`, `v11/code/`,
`v12/code/`.  Of these, only `code/` carries lapse-parameterized
deformation maps: the token `lapse` does not occur as a word in any
`.py` under `v7/code/` through `v12/code/` (0 occurrences),
`hypersurface` occurs in none of them (0 occurrences), and every
occurrence of `antichain` there is a poset-shape counting statistic
(e.g. `v7/code/p22_marked_manifold_audit.py:149`), not a deformation.
The v10/v11 two-order machinery of §3.4 is therefore exactly what that
count says it is: exchange defects of record placement, without a lapse.

---

## 5. The corpus states the gap itself

Five committed statements, none of which this census overturns:

1. `code/v6_task2b_metric_extraction.py:116-119` — "REMAINING
   (honest): … (ii) the final HKT closure — verify the
   antichain-deformation bracket `{H_perp,H_perp}` actually closes on
   `g^{ij} H_j` with THIS extracted metric.  That last step is what
   turns the dynamics leg from 'ingredients present' into 'GR
   derived'."
2. `v6/relativistic-isp-v6-paper2-spatial-direction-and-interacting-integrability.md:182`
   — open: "build the actual direction-coupled antichain deformation
   rule, not just the diagnostic formula".  The causal-set arm of
   `v6_p2c` (PART 2, `:51-103`) is that diagnostic formula: at `:92`
   it evaluates `Mv*gN − Nv*gM` directly from lapse values and frame
   gradients.  No kernel is composed and no two-cell is formed there.
3. `v4/relativistic-isp-v4-paper5-operational-curvature-compatibility-source.md:185-201`
   — Theorem 2.1: the same metric detector table admits both
   `J_{op,a}[N] = I` for every `N` (zero two-cell) and the
   embedding-flow completion (the Dirac–Schwinger two-cell).  This is
   v13 paper 0 §6's kill condition, already carried as a theorem at
   v4 scope, in the direction metric → kernels.
4. `v4/relativistic-isp-v4-paper7-finite-constraint-dynamics-or-gr-no-go.md:462-492`
   — Theorem 6.1: the current corpus does not source the GR-like
   finite dynamics package, whose Hypothesis 5.1 (`:408-425`) lists
   metric reconstruction as item 1 and, as item 8, "continuum
   identification: the limiting structure functions are the recovered
   metric coefficients from the same finite geometry records".
5. `publishable/paper2-hypersurface-deformation-obstruction.md:228-232`
   — residue (R-c), the geometry branch's methodological residue with
   no field-theory analogue: the admissibility gates may be "the
   desired geometry encoded as gate language", and "until each gate
   has an independent finite-record derivation, the descent risks
   assuming what it reconstructs".  That paper is a map, not a
   reconstruction, and carries no receipts.

---

## 6. What the census settles, and what it does not

**Settled.**  GW1's STEPS 1–5 cannot be run on the committed corpus.
The blocking instrument is the deformation kernel, not the metric: the
order/count reconstruction is in hand and runs, in flat and curved
2D and in flat 3D, with an oriented frame, a validated ruler card and
transverse-coordinate finders.

**Settled, and sharper than the pin's binary.**  The block is not the
absence of two-order machinery.  The corpus has exact, metric-free,
runnable two-order machinery with nontrivial output (§3.4).  What it
lacks is a *lapse* on that machinery: the object `J_a[N]` with a
profile argument, metric-free, with a receipt, in `d ≥ 2` spatial
dimensions.  The nearest committed construction of exactly that object,
v3 paper 2's Candidate B, has no code and is 1+1D.  The missing
instrument is therefore nameable to one definition and one dimension
count, not to a research direction.

**Recorded, and not the verdict.**  On every substrate where a
two-cell is runnable, the metric-freeness gate of GW1 STEP 2 fails by
exhibition, with the exhibit already committed: `v6_p2d`'s own
`curved`/flat-normal control moves the recovered coefficient's
correlation with the target metric from `+1.0000` to `+0.0109` on the
same target when the metric is taken out of the normal.  Had STEP 0
been forced through on the grid substrate, GW1-INSERTED would be the
outcome, and the exhibit is the line
`code/v6_p2d_curved_coefficient.py:52`.

**Recorded, and not the verdict.**  v2 Proposition 10.6 is an
underdetermination of the kind GW1 pre-registers, on the Γ-level
substrate: one record law, two backgrounds differing in the sign of
`h^{12}`, identical two-cell data.  It is an all-order finite-regulator
statement, not a truncation artifact.

**Not settled, and not claimed.**  Whether a metric-free
lapse-parameterized record-native kernel with a nontrivial two-cell
exists; whether v3 paper 2's Candidate B admits a receipt on a
record-native substrate rather than a background lattice; whether the
oriented frame of v6 paper 2 §2 supports such a kernel; the continuum
limit of any such construction; whether the §3.4 record-placement
exchange defect relates to `Ω_hypersurface` at all.  The census locates
instruments; it builds none, and it forecasts none.

---

## 7. Non-claims

- No Einstein-dynamics claim, in any form.  No field equation, no
  backreaction, no stress-response, no constraint closure.
- `Δᴮ`, `Ω_hypersurface` and `R^ρ_{σμν}` remain three distinct
  objects; no two are identified.
- No grade is conferred on any located object; the grades are the
  cited papers' own, and v13 paper 0 remains `[DRAFT]`.
- This note is GREEN-UNREVIEWED and is not citable as terminal.

---

## 8. Reproduction

Interpreter `code/.venv/bin/python3.13` (numpy 2.4.6, scipy 1.17.1).
All seven re-runs are of files already committed; no file in the corpus
is modified and no new receipt is written.  Total re-run wall time
21.2 s:

    v6_task2b_metric_extraction.py      1.9 s
    v6_task2f_nogo_confirm.py           0.6 s
    v6_p2c_flow_drift.py                0.8 s
    v6_p2d_curved_coefficient.py        0.4 s
    v6_p2e_3d_tensor_coefficient.py     0.2 s
    v6_p2f_4d_tensor_coefficient.py     0.7 s
    v6_p2_spatial_direction.py         16.7 s

**Disclosed re-run drift.**  The `v6_p2c` PART 2 causal-set arm
re-runs below the values tabulated in v6 paper 2 §3 (`:129-132`):
drift correlation `0.540` against the recorded `0.63`, enrichment
`1.26` against the recorded `1.38`.  The remaining re-runs reproduce
their recorded values (`v6_p2_spatial_direction` `0.94` and
`0.95/0.92`; `v6_p2d` PART 2 `+0.99` twice; `v6_p2e`/`v6_p2f`
`cos = 1.0000`, isotropic `0.973`/`0.974`, rotation `13.4°`/`13.1°`).
The drift is disclosed and is not load-bearing for this census: the
`v6_p2c` PART 2 arm is a diagnostic formula (§5, item 2), not a
two-cell, at either value.
