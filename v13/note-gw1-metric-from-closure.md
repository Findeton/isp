# v13 GW1 — METRIC RECONSTRUCTION FROM DEFORMATION CLOSURE:
# THE INSTRUMENT CENSUS

**Status:** GREEN-UNREVIEWED-REPAIRED, STRICT, 2026-07-28.
**Pin:** `v13/note-gw1-metric-from-closure-pin.md` (STEP 0, the
instrument census, promoted there to a first-class verdict).
**Binding:** v13 paper 0 `[DRAFT]` §2 (the three-defect separation),
§3 (the closure relation), §6 (GW1's five steps, controls and kill
condition); v13 LOG #1, and the corrections carried at v13 LOG #3 and
LOG #4.  The draft stays `[DRAFT]`; nothing in it is adjudicated here.
**Verdict:** **GW1-NOT-RUNNABLE — PRIMARY LOCATED BLOCK AT THE
DEFORMATION INTERFACE.**
**Deliverable:** this census and its STEP 0 receipt.  A failed
instrument gate carries a receipt on the same terms as a successful
experiment: `v13/code/gw1_step0_census.py` emits
`v13/receipts/gw1_step0_census.json` and `gw1_step0_runs.txt`
(audited SHA, working-tree status, interpreter and library versions,
47 inspected paths with blob hashes, the token sweep with counts, nine
re-runs with exit codes, wall times and stdout digests, and the
classification table in the 15-field schema for every located family).
`v13/code/gw1_repair_diagnostics.py` carries the two numeric statements
below that no committed script prints.  **No GW1 STEPS 1–5 receipt
exists**: STEP 0 does not pass, so no closure relation is solved, no
`q̃^{ij}` is fitted, and no control is run.

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

The draft's kill condition, quoted once, verbatim from v13 paper 0
§6 (`v13/relativistic-isp-v13-paper0-gravity.md:433`):

> If the metric must already be inserted into $J[N]$, or if the same
> record law permits inequivalent recovered tensors, then the
> deformation algebra is representing geometry rather than explaining
> it.

The kill does not fire here.  It is not reached: STEP 0 fails first,
and the exhibits below record where it *would* fire on each substrate.

---

## 1. What STEP 0 requires

### 1.1 The five conditions

GW1 becomes runnable when one substrate carries all five of:

1. a **lapse-profiled comparison family** `J_a[N]` — a profile
   argument `N(x)`, not a slab thickness and not a single event;
2. a **no-smuggling construction** of that family (§1.2);
3. a **defined, nontrivial transported two-cell** — the pinned
   `Ω_a[N,M] = J_a[M|N] J_a[N] ( J_a[N|M] J_a[M] )⁻¹`, with the second
   step transported along the first and with the inverses actually
   available;
4. an **intrinsic tangential decoder** `K_i` with a usable inverse, so
   that `(Ω_a − I)/ε_a²` can be read as `K_i[q̃^{ij}(N∂_jM − M∂_jN)]`;
5. **`q^{ij}_order` on the same hypersurface**, from order and count
   data on the same substrate.

No committed substrate carries all five.  The primary located block is
at the deformation interface: conditions 1–3 fail jointly on every
runnable family, and condition 4 is unbuilt everywhere (§5).

### 1.2 "Metric-free" — the no-smuggling definition

Syntactic absence of a metric-named argument is retired.  A
construction `F_a` is **no-smuggling** when:

- it **may** use the causal order, event counts, record adjacency, and
  eventwise lapse values;
- it **may not** call the metric estimator `G_a`, use held-out
  embedding coordinates, use background unit normals, use planted
  frames, or use algebraic data equivalent to the target metric;
- it is **frozen before** `q^{ij}_order` is evaluated.

Every use of "metric-free" below is this predicate.  Under it, several
constructions that pass the syntactic test fail: the record-growth
rules apply the lapse at an embedding coordinate
(`code/v6_task2d_bracket_closure.py:11-13`, whose own scope line calls
this "a coordinate-assisted readout; a fully coordinate-free version
needs combinatorial spatial position, an open problem"), and v3 paper 2's
convex-mixture kernels import singleton kernels from a fixed flat
lattice Dirac benchmark (§3.5).

### 1.3 Object types

Five distinct objects are in play, and "kernel" does not distinguish
them.  The vocabulary used below:

| type | what it is | where |
|---|---|---|
| `Γ` endpoint kernel | a column-stochastic endpoint transition matrix | v2 p10, v3 p2 |
| `J` algebraic comparison map | `Γ` relative to a reference, invertible as an algebraic map | v2 p1/p10, v3 p2, v4 p5/p7 |
| `Φ` monotone history update | a record-growth or embedding-flow map on states, not a comparison map | v6 task2 family, v6 p2c–p2f, v4 p5 Def 3.3 |
| `Ω` group two-cell | `J[M|N]J[N](J[N|M]J[M])⁻¹`, needing inverses and transport | the pin's object |
| record-holonomy weight ratio | a ratio of path-ordered admission weights on histories | v10/v11 exact receipts |

`Φ` and `Ω` are not interchangeable.  A nonzero difference between two
forward orders of a `Φ` is a **forward swap defect** `δ_swap`, not the
pinned `Ω`.

---

## 2. Instrument (i): runnable partial diagnostics; end-to-end intrinsic instrument not yet exhibited

The causal-set/sprinkling substrate carries order+count metric
diagnostics, and they run.  Each is **partial** in a declared way: the
fit or the score reaches outside order and count data.

| object | file | what it returns | reach outside order+count | grade owner |
|---|---|---|---|---|
| flat metric from interval cardinalities | `code/v6_task2b_metric_extraction.py` | `g_{μν}` from a least-squares fit | the fit is against **embedding coordinate separations** `dx = P[b] − P[a]` (`:48`, `:60-65`); only `τ̂²` comes from order+count, and its constant `K` is **calibrated against the true interval** `τ²_true` (`:57-58`) | v6 |
| curved conformal factor, two channels | `code/v6_p2d_curved_coefficient.py:74-139` | `Ω` from longest chains and from counts | bins and slabs are **coordinate-chart** cuts (`:103`, `:110-112`, `:115`); the density channel is near-tautological — the sprinkling is *generated* with density `∝ Ω²` (`:84`) | v6 paper 2 §4 |
| spatial frame | `code/v6_p2_spatial_direction.py`, `code/v6_p2b_local_frame.py` | slice coordinates from the causal graph Laplacian | **unoriented**: scored as `|corr|` and as `R²` after a best linear fit, both sign-blind; the script's own flag is that the spectral embedding is "global, so a genuinely k-LOCAL version must be shown" (`:104-106`) | v6 paper 2 §2 |
| conformal class, volume measure | `v8/code/r1_order_to_conformal_direction.py`, `r2_number_volume_lstep.py`, `r3_manifoldlikeness_myrheim_meyer.py` | directions and volume ratios; absolute scale walled | conformal class only; no metric | v8 paper 4 §1–§2 |
| order dimension, volume-faithfulness | v9 papers 4, 6 | `dim ≤ 2`, `D*_N → 0`; **no spatial metric** | — | v9 |
| frozen ruler card, incl. a spacelike distance | `v10/code/d29_ruler_validation.py` (`:72-140`; the common-diamond distance at `:111-113`) | order-only `d_MM`, chain rulers, spacelike separation | validated **against held-out truth** at `d = 2,3,4` | v10 D29 |
| transverse coordinates from order | `v8/code/k3_decoration_probe.py`, `l2_intrinsic_finder.py`, `m1_intrinsic_4d.py`, `m2_intrinsic_4d_scale.py`; `v9/code/n1_chi_dictionary.py`, `n2_chi_geometry.py` | MDS transverse seed from cross-chain coupling | scored **after Procrustes** against held-out geometry (`k3:141-148`) — an orientation- and reflection-blind score | v8, v9 |
| proper time from chains | `v9/code/dimwall_lorentz1.py` | interval-DP longest chain against the round interval | — | v9 |

The "oriented spatial frame" description of the Laplacian modes is
retracted: no committed run fixes an orientation from order data.  The
global sign of the Fiedler coordinate is set against the hidden truth
at `code/v6_p2c_flow_drift.py:88` ("fix global sign vs true x"), and
the transverse finders are scored after a Procrustes alignment that
quotients out exactly the orientation in question.

Re-run under `code/.venv/bin/python3.13` (numpy 2.4.6, scipy 1.17.1):

- `v6_task2b`: 2D returns `g_tt = +1.00`, `g_tx = +0.01`,
  `g_xx = −1.01`, hence `g^xx = +0.99` against flat `+1`; 3D returns a
  spatial block `≈ −I₂`; the extraction is boost-covariant at
  `β = 0.5`.  Single seed, one realization per dimension; no error
  control declared.
- `v6_p2d` PART 2 (`Ω` never inserted into the *estimator*, declared at
  `:76`): the chain channel correlates `+0.993` with the true `1/Ω²`,
  the density channel `+1.000`, and the two channels agree at `+0.995`;
  centre/wing `0.214` against the GR target `0.160` printed on the same
  line — a 34% overshoot.  Mean over 6 sprinklings; no spread reported,
  no error control declared.
- `v6_p2_spatial_direction`: 1+1 `|corr| = 0.94` (per-trial
  `0.84 … 0.99` over 6 trials); 2+1 `R² = 0.95 / 0.92`.  Per-trial
  values printed; no error control declared.

**Provisional acceptance, engraved.**  These diagnostics are accepted
**for purposes of this census only** — as evidence that order and count
data carry metric information sufficient to make the STEP 0 question
about instrument (ii) meaningful.  This note is **not adjudicating
their promotion into one intrinsic record-native instrument**, and the
end-to-end intrinsic instrument the pin's STEP 1 needs is not exhibited
anywhere.

**Not this instrument.**  v4 paper 4's "metric detector table" is a
declared readout of an inserted background, not an order/count
reconstruction: Definition 11.1
(`v4/relativistic-isp-v4-paper4-operational-orientation-quorum-or-enriched-only-metric-diagnostic.md:820`)
writes the response law as `P = ½(1 + o λ_{ij} h^{ij}(x))` with
`h^{ij}` the fixed background, and Proposition 11.3 (`:866`) returns
`C_op^{ij}(x) = h^{ij}(x)`.  v4 carries no code directory; the object
is definition-only.

---

## 3. Instrument (ii): the committed families, none qualifying

Six committed constructions are located.  Four are runnable (§3.1–§3.4);
two are definition-only (§3.5, §3.6).  Each is classified against the
15-field schema in `v13/receipts/gw1_step0_census.json`.

### 3.1 Record-growth updates — two distinct committed rules

`code/v6_task2_antichain_deformations.py` advances a down-set by
absorbing minimal available events; the rule reads the causal order and
applies the lapse at the event's embedding coordinate.  Its own scope
line (`:14-16`) states that the structure function "is NOT obtained
here".  The object type is `Φ`, a monotone history update: two forward
orders are composed, no inverse is formed, and the pinned `Ω` is not
the measured object anywhere in this family.

Two rules are committed, and they behave differently.

| | **A. pointwise-additive (threshold)** | **B. recomputed height** |
|---|---|---|
| where | `code/v6_task2f_nogo_confirm.py:38-47` | `code/v6_task2d_bracket_closure.py:30-36`; `v6_task2f:56-58`; `v6_task2e:24-26` |
| state | threshold field `T`, down-set `= {h ≤ T}` with `h` a `D`-independent height | the down-set `D` itself |
| the update | `T ↦ T + s·N(x)` | `D ↦ D ∪ { e : ha(e,D) < s·N(e) }`, `ha` recomputed against the current slice |
| invertibility | **empirically invertible, bitwise, on all tested instances** [measured]: `J[−N]∘J[+N] = id` on the state at `N = 2000, 4000, 8000` | **not injective**: exhaustive down-set census at \|V\| = 9/10/11/12 gives 40/44/57/71 down-sets collapsing to 3/5/8/8 images (37/39/49/63 collisions); non-injective at every `s ∈ {0.25, 0.5, 1, 2, 3, 6}`; strictly growing on 70 of 71 down-sets — a set union has no inverse |
| forward swap defect `δ_swap` | **exactly zero** [theorem] (`v6_task2f:4-8`): both orders reach `D ∪ {e : h(e,D) ≤ s(N(e)+M(e))}`, symmetric in `N,M`; re-run `\|comm\| = 0` at all three `N` | **nonzero**: 7 / 13 / 20 / 21 events at `(N,s) = (3000,6), (4000,6), (4000,10), (6000,8)`, i.e. 0.23% / 0.33% / 0.50% / 0.35% of events, with the equal-lapse control exactly 0 in every row |
| gradient content | none — no `∂N` is ever formed | **gradient-blind**: enrichment `0.83 / 0.92 / 0.73 / 0.84` at `N = 1500/3000/6000/10000`, all below 1, with histogram correlations `−0.67 / −0.32 / −0.76 / −0.54`; control 0 at every `N` |
| pinned `Ω` | **formable and equal to `I` exactly**: the three maps are additive translations of `T`, so `Ω` is translation by `sN + sM − sM − sN = 0`; verified bitwise | **undefined as supplied**: no inverse exists, so `Ω` cannot be written down |

Both rows are receipted at `v13/code/gw1_repair_diagnostics.py`
(PART A).  The consequences for GW1:

- Rule A has an invertible advance and a formable `Ω`, and `Ω = I`
  identically.  The closure relation `(Ω_a − I)/ε² ≈ K_i[q̃^{ij}(N∂_jM
  − M∂_jN)]` then carries no metric content: with `K_i` faithful it
  forces `q̃ = 0`, which is not `q^{ij}_order`.
- Rule B has a nonzero forward swap defect, and that defect does not
  track the lapse gradient at any resolution tested.  Its pinned `Ω`
  does not exist.
- Neither rule supplies what the corpus never supplies anywhere: an
  **invertible algebraic comparison-map family** on a record substrate.
  v4 declares one (§3.6); nothing constructs one.

### 3.2 Embedding-flow / grid — the metric is inserted at the normal

These carry a real two-order composition.  The object type is `Φ` — an
embedding flow on tracer labels — and the second step is genuinely
**transported**: it acts on the already-pushed slice.  The metric
enters their construction, at the line where the normal is normalized.

| file:line | the insertion |
|---|---|
| `code/v6_p2c_flow_drift.py:32-36` | `nt = 1/sqrt(1-sl²)`, `nx = sl/sqrt(1-sl²)` — the Minkowski normalization of the normal |
| `code/v6_p2d_curved_coefficient.py:50-54` | `fac = (1.0/Omega(x)) if curved else 1.0`; `nt = fac/sqrt(1-sl²)` |
| `code/v6_p2e_3d_tensor_coefficient.py:42-47` | `gx = ixx*Tx + ixy*Ty` (raise with `h^{ab}`), `norm = sqrt(1 − h^{cd}∂_cT ∂_dT)` |
| `code/v6_p2f_4d_tensor_coefficient.py:38-47` | `raise_idx(cov)` = `h^{ab} cov_b`; same normalization in 3+1 |

Re-run results, and the control that prices them:

- `v6_p2c` PART 1: the measured object is the **difference of two
  forward orders of the flow on comoving tracer labels**, `x1 − x2`, at
  leading order in `ε`; no `J⁻¹` is formed and the pinned `Ω` is not
  assembled.  That leading-order surrogate correlates `+1.0000` with
  `−ε²(NM′−MN′)`, slope`/(−ε²) = 1.001`.  Deterministic grid, 400
  tracers; the computation is deterministic and no error control is
  declared.
- `v6_p2d` PART 1 — **the insertion, exhibited on one target by a
  committed control**.  With `Ω` in the normal: `corr(C, 1/Ω²) =
  +1.0000`, centre/wing `0.239` against the target `0.232`.  With `Ω`
  removed from the normal and nothing else changed:
  `corr(C, 1/Ω²) = +0.0109`, centre/wing `1.000`.  The surrogate
  returns the coefficient placed in the kernel, and returns a constant
  when none is placed there.  Deterministic grid; no error control
  declared.
- `v6_p2e`, `v6_p2f`: measured drift vector against the tensor
  prediction `cos = 1.0000`; against the isotropic null `0.9729`
  (2+1) and `0.9739` (3+1); rotation measured `13.38°` vs predicted
  `13.38°`, and `13.13°` vs `13.13°`.  The measurement and the
  prediction read the same `h^{ab}` field (`v6_p2e:44` and `:58`), so
  the agreement is a kinematic consistency check, not a recovery from
  independent data.  Deterministic grids; no error control declared.

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

### 3.3 The Γ-level lattice — two-cell real and exact, metric inserted

v2 paper 1 proves that the finite exchange defect reaches the
tangential bracket in 1+1D.  v2 paper 10 asks whether its coefficient
is readable as inverse spatial metric data in higher spatial
dimension, on a fixed background.  This family **is** lapse-profiled at
paper level, and it drops **metric-freeness only**.

- The lapse-profiled comparison family exists as a theorem object:
  `𝕁_{a,h}[N;Δ] := exp L_{a,h}[N;Δ]`, `L_{a,h}[N;Δ] = a²Σ_x N_x log
  J_{a,h}[x;Δ]`
  (`v2/relativistic-isp-v2-paper10-metric-data-from-stochastic-exchange-curvature-investigation.md:747-760`),
  with the group commutator `E_{a,h}[N,M;Δ] = 𝕁[N]𝕁[M]𝕁[N]⁻¹𝕁[M]⁻¹`
  (`:773-778`), invertibility for small `|Δ|` (`:804-808`) and the
  normalized finite-slab curvature (`:813-815`).  v2 paper 1 (`:17`,
  and the log-smeared construction at `:327`) carries the same object
  and its continuum target `K_∥[N∂_xM − M∂_xN]` (`:497`).
- It is **not primitive for signed lapses**: for sign-changing profiles
  `𝕁_{a,h}[N;Δ]` is "an algebraic pseudo-stochastic comparison map
  rather than a primitive positive stochastic kernel … not an
  operational instrument without extra structure" (`:765-768`).
- The metric is inserted at the **frame**, not at the Clifford escape:
  a constant frame matrix `E_A^{\ j}` defines `h_0^{ij} = Σ_A E_A^i
  E_A^j` and enters the finite one-particle Hamiltonian `H_{a,h} =
  α^A E_A^{\ j} D_{j,a} + mβ` from which the kernels are built
  (`:655-671`); `h^{ij}` is declared fixed background geometry at
  `:63`.  (The Clifford relation `½{γ^i,γ^j} = h^{ij}I` at `:1825` is
  the paper's **enriched-representation escape**, which it explicitly
  labels "**not** `Gamma`-level metric reconstruction" at `:1836-1838`;
  it is not the insertion point.)
- Proposition 10.4 (`:1237`): the leading Born-squared coefficient
  fails the rotated-metric cross-term test — it sees `h^{11}` and
  `h^{22}`, not `h^{12}`.
- Proposition 10.5 (`:1464`): the first higher-order signal is
  signless, giving `(h^{12})²`.
- Proposition 10.6 (`:1659`): a sign-ambiguity no-go to all orders.
  The frame flip `E₂ → −E₂` leaves every `Γ`-level datum invariant
  while sending `h^{12} → −h^{12}`.  **Scoped modulo gauge:** this is a
  component-level ambiguity in a fixed labelled presentation.  Whether
  it is physical nonuniqueness or an unresolved frame gauge awaits an
  orientation convention which the order instruments — unoriented, per
  §2 — do not supply.  The clean GW1 comparison is not componentwise
  but `q♯_comp(ω) =? q♯_order(ω)` on intrinsic spanning covectors.
- Verdict §14 (`:2001`): "not a positive full-metric reconstruction
  paper".

This substrate carries no order/count instrument; its geometry is a
fixed lattice with `h^{ij}` supplied.

The **code** implementations of this family are a different, narrower
object.  The exact form of the same commutator
`E = J_R J_S J_R⁻¹ J_S⁻¹` is runnable at
`v10/code/d43a_lie_trotter_exact.py:18-20` (order-12 exact truncated
series, `mp.dps = 50`), and in float at
`validate_minimal_interacting_gauge_matter_benchmark.py:93` and
`validate_truncated_u1_benchmark.py:119`.  In all three, `J` is
`Γ(U_loc)Γ(U_free)⁻¹` from a lattice Dirac Hamiltonian: region-supported
and parameterized by a slab thickness `Δ`, **not** by a lapse profile.
The lapse lives in the theorems; the slab thickness lives in the code.

### 3.4 Record-history holonomies — exact, nontrivial, no lapse profile

The corpus carries exact, runnable, order-native two-order-mismatch
machinery whose output is **not** trivial.  The object type is a
record-holonomy weight ratio: path-ordered `Fraction`-exact admission
weights on histories (down-sets), with no coordinates, no unit normal
and no background field.

| file:line | the two orders | the measured mismatch |
|---|---|---|
| `v10/code/d42b3_placement_exact.py:390-398` | `h + [e1,e2]` vs `h + [e2,e1]` on record histories, gated on `canon(h12v) == canon(h21)` | 202 canonical diamonds, 36 chain-consistency violations |
| `v10/code/d49_dichotomy_settlement_exact.py:384-401`, `:890-909` | the same diamond census, chain-product form | the flatness ladder |
| `v10/code/d44f_foliation_measure_exact.py:394-410` | `def commutes(h, e1, e2)` with a positive and a gated negative control | exact commutation, and its designed failure |
| `v10/code/d74_transport_holonomy_exact.py:574-580` | `holonomy_of(edges, reverse_order)`, closed-square census | 88 of 1,546 closed squares non-unit |
| `v10/code/d72_weld_exact.py:927-960`, `v11/code/ld_reversal_probe_exact.py`, `u2_three_address_weld_exact.py`, `u3_unistochasticity_screen_exact.py` | reversal holonomy on closed squares | the corresponding censuses |
| `code/v6_p4n_exchange_cocycle_law.py:1-14` | the two internally available orderings of the same sealed record transports | `A_D = log dP_AB/dP_BA` |

None of these takes a lapse profile.  They advance a history by one
**event**, not by a profile `N(x)`, and they carry no `ε` and no `∂_j`.
The closure relation cannot be posed on them: `N`, `M`, `ε_a` and the
gradient all lack referents.  What they measure is an exchange defect
of record placement, which the scope box keeps distinct from
`Ω_hypersurface`.

### 3.5 Smooth-lapse convex-mixture kernels (v3 paper 2, Candidate B) — lapse-profiled, definition-only, background-encoded

`v3/relativistic-isp-v3-paper2-primitive-smooth-lapse-hypersurface-kernels.md`
builds a lapse-profiled family from a smooth compactly supported lapse
without a metric symbol in the kernel: Candidate B (`:202-237`) sets
`Γ_a^mix[N;Δ] := (1−ηa∑N_n)Γ_0(Δ) + ηa∑N_nΓ_n(Δ)`, hence
`J_a^mix[N;Δ] = I + ηa∑N_n(J_n − I)`, from exact endpoint stochastic
kernels; §6 (`:298-313`) then forms
`E_a^mix[N,M;Δ] = J_N J_M J_N⁻¹ J_M⁻¹`.  The object types are clean:
a `Γ` endpoint kernel, a `J` comparison map, and a fixed-space group
commutator (the second step is **not** transported).

Re-graded under §1.2's no-smuggling definition, this family **fails**:
the singleton kernels `Γ_n(Δ)` and `J_n(a,Δ)` are imported from V2's
fixed flat lattice Dirac benchmark, whose background normalization is
encoded in them.  The metric symbol is absent; the background is not.

Three further scope facts:

- **Theorem 6.1** (`:335-377`) holds on the **positive cone** only
  (`N,M ≥ 0`, a bounded positive-lapse class), under the V2 thin-slab
  scaling `Δ(a)/a² → 0` and under the **assumed** uniform boundedness
  of the singleton remainders in the V2 finite-slab topology.  The
  paper's own summary: "positive-cone, declared-protocol, and
  leading-curvature level.  It is not yet a theorem for all signed
  lapses or all regulator families."
- **Theorem 7.2** (`:469-593`) recovers the signed bracket only as a
  continuum bilinear extension by polarization; its own scope note
  (`:596-610`) states that it "does not construct a finite-regulator
  stochastic kernel for a signed lapse", and that the uniform
  finite-regulator residual estimate "is a next proof burden, not
  silently included here".
- Candidate B is **primitive stochastic only via a declared external
  randomization**: it is "Barandes-compatible if interpreted as one
  declared randomized whole-process operation.  If the random choice is
  recorded, it belongs to the instrument layer" (`:232-236`).

**`v3/` contains no code**: the family is definition-only, with no
receipt anywhere in the corpus, and no order/count instrument on its
substrate.  Theorem 6.1's limit is
`(E_a^mix[N,M;Δ] − I)/(η²Δ⁴) → K_∥[N∂_xM − M∂_xN]`, in **one** spatial
dimension, where the coefficient is a single scalar not separately
identifiable from the lapse, the lattice spacing and the
tangential-generator normalizations.  v2 paper 10 prices exactly that
(`:48-51`): "in one spatial dimension the metric question is almost
invisible: the coefficient is one scalar, and many normalizations can
hide inside the lapse, the lattice spacing, or the tangential generator
convention."  A GW1 run on this family would therefore need `d ≥ 2`,
which is where §3.3's sign-ambiguity no-go applies.

### 3.6 Declared normal comparison maps (v4 paper 7) — the nearest committed statement of GW1's object, and it constructs nothing

`v4/relativistic-isp-v4-paper7-finite-constraint-dynamics-or-gr-no-go.md`
states GW1's object more nearly than any other committed text.

- **Definition 1.3** (`:159-166`): for a finite lapse test `N`, a
  normal comparison map is an **invertible algebraic map**
  `H_a[N] : V_a^tot → V_a^tot` on total finite matter-geometry records.
  A `J`-type comparison map, lapse-profiled, invertible **by
  declaration**.
- **Definition 1.4** (`:175-193`): given a finite geometry record
  `g_a`, with metric candidate `I_a(g_a)^{ij}`, the finite bracket
  vector is `β_a^i(g;N,M) := I_a(g)^{ij}(N∂_jM − M∂_jN)`, the
  derivatives being declared finite differences or reconstructed first
  jets.  This is in **general spatial dimension**, and the metric is
  **read from the finite geometry record**, not supplied as background:
  `:238` states "Because `g` is now a finite configuration variable,
  this residual is tested on total effects sectorwise or in expectation
  under a declared total law."
- **Definition 2.3** (`:227-236`): `R_{HH,a}[N,M] := H_a[N]H_a[M]
  H_a[N]⁻¹H_a[M]⁻¹ D_a[−β_a(g;N,M)]` — the pin's residual exactly, with
  the tangential correction included rather than fitted.
- The two-cell is **not excluded from being nontrivial**.  v4 paper 12
  Definition 11.6M (`:2546-2580`) builds the three-normal switch
  detector `W_{N|ML,a} := C(H_a[N], D_a[B_{ML,a}]) H_a[L_{B,a}N]` from
  these maps, and v4 paper 13 Proposition 3.6 (`:858-901`) exhibits a
  **nonzero** detector: on the two-state metric alphabet `X^met =
  {0,1}` with `G(x) = x`, choosing `W_{N|ML} = T`, `W_{M|LN} =
  W_{L|NM} = I` with `T(0)=1, T(1)=0` gives `SW_{HHH} = T` and
  `‖SW_{HHH}G − G‖ > 0`.  The paper's own reading: "the mere existence
  of `H`, `D`, `β`, and metric readouts does not force equivalence
  response.  A new compatibility principle is needed."  (v4 paper 13
  imports the same objects at `:124-153`.)

This family is **outside** Proposition 10.6's scope: the metric is
record-read rather than a fixed background presented in a labelled
frame, so the frame-flip construction does not apply to it as stated.

Its disqualification is of a different kind from the other five:
metric-freeness under §1.2 is **vacuous** here, because there is no
construction to test.  `H_a[N]` is invertible by declaration and
`I_a(g)^{ij}` is a metric candidate by declaration; neither is built,
and v4 carries no code directory.  The dropped requirement is
**runnability** — kernels declared, never constructed.

---

## 4. The cross-cut

| substrate | object type | instrument (i) | instrument (ii) | drops |
|---|---|---|---|---|
| causal set / sprinkling (v6 task2 family; v6 p2 PART 2; v8 §1–2; v9; v10 D29) | `Φ` monotone history update | runnable partial diagnostics (§2) | lapse-profiled but coordinate-assisted; rule A: invertible, `δ_swap = 0`, `Ω = I` exactly; rule B: `δ_swap ≠ 0` but gradient-blind, `Ω` undefined | a nontrivial pinned two-cell (and, under §1.2, strict metric-freeness) |
| record histories (v10 d42b3/d49/d44f/d72/d74; v11 ld/u2/u3; `v6_p4n`) | record-holonomy weight ratio | partial — the same order data | metric-free, exact, mismatch **nontrivial** | the lapse profile: no `N`, no `ε`, no `∂_j` |
| grid embedding-flow (v6 p2c/d/e/f PART 1; v4 p5 Def 3.3) | `Φ` embedding flow | absent — the metric is declared input | transported two-order surrogate at `O(ε²)`, **metric inserted** at the normal; the pinned `Ω` is not assembled | metric-freeness |
| Γ-level lattice (v2 p1, p10; v10 d43a; the root validators) | `Γ` → `J` → `Ω` | absent — fixed lattice | lapse-profiled at **paper** level (`v2 p10:747-760`); `Ω` real and exact; **metric inserted** via the frame (`:655-671`); recovery blocked at `h^{12}` to all orders, modulo gauge; the **code** family is `Δ`-parameterized, not lapse-parameterized | metric-freeness only |
| smooth-lapse convex mixture (v3 p2 Candidate B) | `Γ` → `J` → `Ω` | absent | lapse-profiled, `Ω` nontrivial at Theorem 6.1 — **definition-only, no code in `v3/`**; positive cone; background encoded in the imported singleton kernels | runnability, and metric-freeness under §1.2 |
| declared normal comparison maps (v4 p7 Defs 1.3/1.4/2.3; p12/p13 switch) | `J` + the pinned residual `R_{HH,a}` | absent on a v4 substrate | lapse-profiled, general-`d`, metric **record-read**, invertible **by declaration**, two-cell nontriviality **not excluded** (p13 Prop 3.6) | runnability — kernels declared, never constructed |

Two columns deserve separating, because the pinned `Ω` requires the
second step to be transported along the first:

| family | transported second step | fixed-space group commutator only |
|---|---|---|
| grid embedding-flow | **yes** — the second push acts on the pushed slice | no |
| Γ-lattice (v2), convex mixture (v3) | no | **yes** — `J_N J_M J_N⁻¹ J_M⁻¹` on a fixed space |
| record-growth updates | neither — two forward orders, no inverse | no |
| record-history holonomies | path-order ratios on closed squares | no |
| v4 p7 declared maps | declared, via `D_a[−β_a(g;N,M)]` | no |

No single committed substrate carries the five conditions of §1.1 in
runnable form.  **GW1-NOT-RUNNABLE — PRIMARY LOCATED BLOCK AT THE
DEFORMATION INTERFACE.**

The block has two faces, and neither is repairable by choosing a
different committed substrate.  Where the two-order machinery is
metric-free and nontrivial, it has no lapse profile, so the closure
relation has no referents.  Where it is lapse-profiled, either the
pinned two-cell is trivial or undefined (record-growth) or the metric
is inserted into the construction (grid, lattice, convex mixture).
The one family that states all of GW1's conditions at once constructs
none of them.

**Where the runnable code is, and is not.**  `v1/`, `v2/`, `v3/`,
`v4/`, `v5/` and `publishable/` contain **no `.py` at all**, so every
object located in them — including v4 paper 5's exchange two-cell
(Definition 1.2) and embedding-flow kernels (Definition 3.3), v4
paper 7's normal comparison maps, v4 paper 4's metric detector table,
v3 paper 2's smooth-lapse kernels, and v2 paper 10's benchmark — is
definition-only.  The complete list of runnable trees, with `.py`
counts, is:

    code/                                 353
    v7/code/                              273
    v10/code/                             137
    v8/code/                              101
    v9/code/                               84
    _archive_low_value_2026-06-14/code/     9
    external/walsh-delta-code/              8
    v11/code/                               7
    v12/code/                               5
    bc/code/                                3
    <repository root>                       3
    v6/code/                                1

Of these, **only `code/` carries lapse-parameterized deformation maps**:
the token `lapse` occurs as a word in 12 of `code/`'s 353 `.py` files
and in **0** files in every other tree — `v6/code/` through
`v12/code/`, `bc/code/`, `external/walsh-delta-code/`,
`_archive_low_value_2026-06-14/code/`, and the three root `.py`.  The token `hypersurface` occurs in 2 files, both under
`code/` and both prose references to the Dirac–Schwinger algebra, and
in **0** files everywhere else.  Every occurrence of `antichain`
outside `code/` is a poset-shape counting statistic (e.g.
`v7/code/p22_marked_manifold_audit.py:149`), not a deformation.  The
v10/v11 two-order machinery of §3.4 is therefore exactly what that
count says it is: exchange defects of record placement, without a lapse
profile.  All counts are re-executed and recorded in
`v13/receipts/gw1_step0_census.json` under `search_protocol`.

---

## 5. The interface inventory: the kernel is not the only block

Even a family satisfying §1.1's conditions 1–3 leaves the rest of the
pipeline unbuilt.  The following are separate, and none is committed on
a record substrate:

1. **`∇_j` on the slice.**  `N∂_jM − M∂_jN` needs a derivative on the
   hypersurface.  The record substrates supply none; `v6_p2c:76-81`
   estimates it by a `polyfit` along a spectral coordinate, and its own
   paper lists "build the actual direction-coupled antichain
   deformation rule, not just the diagnostic formula" as open.
2. **The tangential decoder `K_i`, and its inverse.**  GW1 STEP 4 reads
   `(Ω − I)/ε²` *through* `K_i`.  v4 paper 2 Theorem 3.2 (`:210-241`)
   requires as hypothesis 5 that "`K_i` is locally faithful modulo
   declared tangential gauge", and returns `C^{ij}` unique only
   **modulo tangential gauge**.  No committed object supplies `K_i` on
   a record substrate, and no committed object inverts it.
3. **Transported second steps.**  Only the grid family implements one
   (§4); the pinned `Ω` is not a fixed-space commutator.
4. **`ε` pinning.**  The closure relation divides by `ε_a²`.  No record
   substrate carries a deformation-size parameter to pin.
5. **Density-weight conventions.**  v4 paper 2 Corollary 3.3
   (`:267-279`) reads the extracted `C^{ij}` as inverse metric data
   "or inverse metric density data, **according to the normalization
   convention**"; v2 paper 10's `R_a` is likewise "not a convention-free
   input" (`:818-821`).
6. **The `q_comp` / `q_order` gauge and scale identification.**  The two
   tensors are compared only after fixing tangential gauge, orientation
   and absolute scale — and v8 paper 4 walls absolute scale, while §2
   retracts orientation.
7. **Lapse-pair rank and identifiability.**  v4 paper 2's extraction is
   pointwise by lapse-jet tests realizing an arbitrary covector `ω` at
   `x` (`:230-241`); recovering the full `C^{ij}` requires a **spanning**
   set of such covectors, i.e. a lapse-pair family of full rank at each
   point.  No committed run tests rank.

v4 paper 2 Definition 4.1 (`:281-300`) collects eight such conditions
as `V4P2-METRIC-REC`, and v4 paper 2's own verdict (`:450`) is that its
theorem is conditional on them.  Naming the kernel as the only block
is therefore too narrow: the kernel is the **primary located** block,
and the interface behind it is unbuilt.

---

## 6. The corpus states the gap itself

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

## 7. What the census settles, and what it does not

**Settled.**  No runnable end-to-end GW1 pipeline is exhibited on the
committed corpus.  Every runnable construction that produces a
nontrivial closure-shaped quantity is background-enriched: the grid
embedding-flow inserts the metric at the unit normal, and the Γ-level
lattice inserts it at the frame.  Every record-native construction
either has an undefined pinned two-cell (the recomputed-height rule has
no inverse) or a forward swap defect that is exactly zero by theorem
(the pointwise-additive rule) or nonzero but gradient-blind (the
recomputed-height rule's residue).  The record-history holonomies are
exact and nontrivial but are not lapse-profiled, so the closure
relation has no referents on them.

**Settled, and sharper than the pin's binary.**  The block is not the
absence of two-order machinery.  The corpus has exact, metric-free,
runnable two-order machinery with nontrivial output (§3.4).  What it
lacks is a **lapse profile** on that machinery, together with the
interface of §5.  Committed **definitions** of the missing object exist
in four places — v4 paper 7 Defs 1.3/1.4/2.3 (general-`d`, record-read
metric, invertibility declared), v4 paper 5 Defs 1.2/1.3/3.3
(fixed-background by declaration), v2 paper 10 `:747-760`
(fixed-background frame), and v3 paper 2 Candidate B (background
encoded in imported singleton kernels).  What is absent is instrument
(ii) **in runnable, no-smuggling form co-located with instrument (i)**.
The nearest statement is v4 paper 7's, which is general-`d`,
record-read and outside Proposition 10.6's fixed-background scope, and
which constructs nothing.

**Recorded, and not the verdict.**  On every substrate where a
two-order surrogate is runnable, the metric-freeness gate of GW1
STEP 2 fails by exhibition, with the exhibit already committed:
`v6_p2d`'s own `curved`/flat-normal control moves the recovered
coefficient's correlation with the target metric from `+1.0000` to
`+0.0109` on the same target when the metric is taken out of the
normal.  Had STEP 0 been forced through on the grid substrate,
GW1-INSERTED would be the outcome, and the exhibit is the line
`code/v6_p2d_curved_coefficient.py:52`.

**Recorded, and not the verdict.**  v2 Proposition 10.6 is an
underdetermination of the kind GW1 pre-registers, on the Γ-level
substrate: one record law, two backgrounds differing in the sign of
`h^{12}`, identical two-cell data.  It is an all-order finite-regulator
statement, not a truncation artifact — scoped per §3.3 to a
component-level ambiguity in a fixed labelled presentation.

**Not settled, and not claimed.**  Instrument (i) is accepted
**provisionally** for this census (§2) and is **not** adjudicated
complete: the end-to-end intrinsic record-native instrument is not
exhibited, and its promotion is a separate unit.  Nonexistence outside
the receipted search protocol is **not** proven: the census's negative
is exactly as wide as the paths, trees and tokens recorded in
`v13/receipts/gw1_step0_census.json`.  Also open: whether a
no-smuggling lapse-profiled record-native comparison family with a
nontrivial transported two-cell exists; whether v3 paper 2's Candidate
B admits a receipt on a record-native substrate rather than a
background lattice; whether the spectral frame of v6 paper 2 §2
supports such a family once oriented; the continuum limit of any such
construction; whether the §3.4 record-placement exchange defect relates
to `Ω_hypersurface` at all.  The census locates instruments; it builds
none, and it forecasts none.

**The conclusion this census reaches.**

> The corpus can either obtain nontrivial closure by supplying
> geometry, or remain record-native and fail to produce the required
> closure.

### 7.1 The successor, ordered

**First — construct a record-native `H_a[N]` to v4 paper 7
Definition 1.3, and measure `R_{HH,a}[N,M]` against
`β_a^i = I_a(g)^{ij}(N∂_jM − M∂_jN)` with `I_a(g)^{ij}` supplied by the
order+count extraction of `v6_task2b`.**  This is the nearest route:
general spatial dimension, metric read from the finite geometry record
rather than a background, invertibility declared at Definition 1.3, the
residual already written in the pin's form at Definition 2.3, a nonzero
detector already exhibited at v4 paper 13 Proposition 3.6, and outside
Proposition 10.6's scope.  The missing piece is exactly GW1's object:
a construction of `H_a[N]` that satisfies §1.2.  Co-requisites, from
§5: `∇_j` on the slice, `K_i` and its inverse, a transported second
step, an `ε` to pin, a fixed density-weight convention, the
`q_comp`/`q_order` gauge-and-scale identification, and a lapse-pair
family of full rank at each point.

**Second — graft a lapse profile onto the record-history holonomy
machinery of §3.4**, which is exact, metric-free and nontrivial and
lacks only the profile argument, the `ε` and the gradient.

**Candidate B is demoted** to third.  It lives in one spatial
dimension, where the coefficient is a single scalar not separately
identifiable from the lapse, the lattice spacing and the
tangential-generator normalizations; it fails
the no-smuggling test through its imported singleton kernels; its
positive-cone theorem carries a conditional remainder assumption; and
its signed-lapse extension is continuum-level only, with the
finite-regulator residual declared an open proof burden.

---

## 8. Non-claims

- No Einstein-dynamics claim, in any form.  No field equation, no
  backreaction, no stress-response, no constraint closure.
- `Δᴮ`, `Ω_hypersurface` and `R^ρ_{σμν}` remain three distinct
  objects; no two are identified.
- No grade is conferred on any located object; the grades are the
  cited papers' own, and v13 paper 0 remains `[DRAFT]`.
- Instrument (i) is accepted provisionally for this census only; no
  promotion is adjudicated.
- The negative is scoped to the receipted search protocol; no
  nonexistence theorem is claimed.
- This note is GREEN-UNREVIEWED-REPAIRED and is not citable as
  terminal.

---

## 9. Reproduction

Interpreter `code/.venv/bin/python3.13` (python 3.13.5, numpy 2.4.6,
scipy 1.17.1).  The audited commit, the working-tree status and the
blob hash of every inspected path are recorded by the receipt at run
time; at the time of writing all 47 inspected paths match their HEAD
blobs exactly, and the working tree's dirty entries belong to other
units apart from this unit's own `v13/code/` and `v13/receipts/`.  All
nine re-runs are of files already committed; no file in the corpus is
modified.
Measured wall times:

    v6_task2b_metric_extraction.py      2.9 s
    v6_task2d_bracket_closure.py        0.6 s
    v6_task2e_AvsB_diagnostic.py        7.9 s
    v6_task2f_nogo_confirm.py           0.6 s
    v6_p2c_flow_drift.py                1.1 s
    v6_p2d_curved_coefficient.py        0.4 s
    v6_p2e_3d_tensor_coefficient.py     0.1 s
    v6_p2f_4d_tensor_coefficient.py     0.9 s
    v6_p2_spatial_direction.py         27.5 s

Total 42.0 s cold; the census receipt re-runs all nine in one pass
(34–36 s warm across repeats), records each exit code, wall time and
stdout sha256, and all nine exit 0.  **Error control: none of the nine scripts prints a
standard error, a standard deviation or a repeat-to-repeat spread.**  Every number quoted from them is a
single-seed point estimate; `v6_task2e` and `v6_p2d` average over
realizations without reporting a spread, `v6_p2c` PART 2 prints its
five per-trial values without one, and the remaining runs are
single-realization or deterministic-grid.

The two receipts written by this unit:

    v13/code/gw1_step0_census.py         the STEP 0 census receipt
    v13/code/gw1_repair_diagnostics.py   the two-rule split and the
                                         drift root cause

### 9.1 The `v6_p2c` PART 2 drift, root-caused

`v6_p2c` PART 2 re-runs below the values tabulated in v6 paper 2 §3
(`:129-132`): drift correlation `0.540` against the recorded `0.63`,
enrichment `1.26` against the recorded `1.38`.  The cause is a
degenerate Laplacian null space, and it is not a change in the
substrate.

`recover_u` (`code/v6_p2c_flow_drift.py:59-74`) builds a kNN graph on
the slice events, forms `Lap = diag(W.sum(1)) − W`, calls `eigh(Lap)`,
and returns `V[:, 1]` — the Fiedler vector **if the graph is
connected**.  Reproducing the committed loop at its own seed:

| trial | \|A\| | components | nullity | `λ₀` | `λ₁` | `λ₂` | corr |
|---|---|---|---|---|---|---|---|
| 0 | 74 | **2** | **2** | `−2.735e−15` | `+6.375e−16` | `+2.561e−01` | `+0.0134` |
| 1 | 91 | 1 | 1 | `+9.166e−16` | `+1.271e−01` | `+6.544e−01` | `+0.7237` |
| 2 | 99 | 1 | 1 | `−1.689e−15` | `+5.924e−02` | `+1.473e−01` | `+0.8410` |
| 3 | 83 | 1 | 1 | `+7.212e−15` | `+1.468e−01` | `+6.128e−01` | `+0.7957` |
| 4 | 85 | 1 | 1 | `−3.341e−15` | `+1.018e−01` | `+4.135e−01` | `+0.3260` |

Trial 0's slice graph has two connected components, so the Laplacian
nullity is 2 and `V[:, 1]` is an **arbitrary basis vector of a
two-dimensional null space** — fixed by nothing but LAPACK's internal
tie-breaking.  Perturbing that trial's Laplacian by symmetric noise of
size `1e−13` over 60 draws moves its correlation across
`[−0.606, +0.675]` (sd `0.275`; unperturbed `+0.0134`), which moves the
five-trial mean across `[0.416, 0.672]` — a range that covers the
recorded `0.63` and the re-run `0.540` alike.  The recorded and re-run
values are two samples of the same arbitrary choice.

A 40-trial population reference at seed 20260728 puts both in
context: correlation mean `+0.722`, sd `0.197`, SE `0.031`; enrichment
mean `1.134`, sd `0.225`, SE `0.036`.  One of the 40 slice graphs is
disconnected, and it is the only trial with a near-zero score
(`−0.066`); the 39 connected trials give mean `+0.742`, sd `0.152`.
Across eight disjoint five-trial campaigns drawn from that population,
the campaign enrichment means run `0.99 … 1.27` — the recorded `1.38`
lies **above all eight**.  The committed campaign's own per-trial
spread is sd `0.32` on five trials, so neither `0.63` nor `0.540` is
distinguishable from the other at that sample size.

**The required guard.**  Any re-use of this construction must gate on
connectivity before consuming a spectral coordinate: compute the number
of connected components of `W` (or the Laplacian nullity) and reject or
re-draw when it exceeds 1; consuming `eigh(L)`'s second column is only
meaningful on a connected graph.  **The same unguarded pattern is a
live instrument-(i) receipt**: `code/v6_p2_spatial_direction.py:48-50`
forms `L = D − W`, calls `vals, vecs = eigh(L)` and returns
`vecs[:, 1:1+n_modes]` with no connectivity check, and it is the source
of §2's `0.94` and `0.95/0.92`.

This drift is disclosed and is not load-bearing for the census: the
`v6_p2c` PART 2 arm is a diagnostic formula (§6, item 2), not a
two-cell, at either value.
