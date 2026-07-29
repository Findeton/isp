# v13 GW1 — METRIC RECONSTRUCTION FROM DEFORMATION CLOSURE (PIN)

**Status:** PIN, STRICT, 2026-07-28.  **Binding:** the v13 draft
paper 0 §6 (GW1, five steps + controls + the kill condition,
verbatim) and §2's three-defect separation (Δᴮ ≠ Ω_hypersurface ≠
Riemann — no identification anywhere).  The draft stays [DRAFT];
this pin is v13's first frozen unit.  Lean NONE.

## The question

Can the spatial metric be RECOVERED from the closure law of local
record deformations — without being inserted into the deformation
kernels — and does it equal the metric read independently from the
record order?  (The draft's kill: if the metric must be inserted
into J[N], or the same record law permits inequivalent recovered
tensors, the deformation algebra REPRESENTS geometry rather than
explaining it — V4's underdetermination wall, made an experiment.)

## The unit, operationalized

- **STEP 0 — THE INSTRUMENT CENSUS (first, and possibly the whole
  unit):** locate in the committed corpus (v4's
  operational-curvature paper and its receipts; the v4
  constraint-dynamics paper; v9's theorem-track webs; any committed
  substrate) the two required instruments: (i) an order/count
  metric reconstruction q^ij_order, and (ii) committed finite
  deformation kernels J_a[N] with the exchange two-cell
  Ω_a[N,M] = J_a[M|N]J_a[N](J_a[N|M]J_a[M])⁻¹.  Cite file:line for
  every located object.  **If NO committed substrate carries BOTH,
  the unit's honest verdict is GW1-BLOCKED-AT-⟨instrument⟩ with the
  missing-instrument census — a first-class outcome that scopes the
  entire v13 programme, not a failure.**
- **STEPS 1–5 (the draft's, on the smallest honest substrate that
  passes step 0):** reconstruct q^ij_order; define J_a[N] WITHOUT
  the metric in their construction (gate this: the kernels'
  definition must be exhibited metric-free, or the insertion is
  declared and the kill fires); measure Ω_a[N,M] exactly; inverse-
  solve for q̃^ij from the closure relation
  (Ω_a − I)/ε² ≈ K_i[q̃^ij(N∂_jM − M∂_jN)]; test q̃ → q_order under
  refinement.  Exact arithmetic wherever the committed instruments
  are exact; declared numerics with printed error control only
  where the committed instruments themselves are numeric.
- **CONTROLS (the draft's, all):** wrong deformation kernels (must
  break recovery); flat and curved targets; randomized update
  order; chart changes; matter-free vs matter-conditioned.
- **Pre-registered outcomes:** GW1-RECOVERED (q̃ = q_order under
  refinement, controls behaving) / GW1-UNDERDETERMINED (inequivalent
  recovered tensors — the kill, censused) / GW1-INSERTED (the
  kernels cannot be defined metric-free — the kill, exhibited) /
  GW1-BLOCKED-AT-⟨instrument⟩ (step 0 fails — the census is the
  deliverable).

Receipt rules: anchors exit-1-only on every committed number
reused; substantive negatives exit 0; caps and substrate declared;
runtime < ~40 min, progress prints (< 8 min silent); STRICT,
GREEN-UNREVIEWED, no leans; the three-defect separation quoted in
the scope box; no Einstein-dynamics claim of any kind (§5 of the
draft is out of scope).  Files: v13/code/gw1_*,
v13/note-gw1-metric-from-closure.md.  Do not touch v11/bc working
trees; v12 read-only.
