# 3p1-conservation — round 47: conservation-churn (the coupled builder) + the first influence measurement

**Status:** design note, 2026-07-10 (v9 round 47). Receipt: `v9/code/dimwall_conservation.py` (pinned here, committed strictly before running). NO-REVIEW MODE (standing; on record); exit-1 wiring + the free-web control are the compensating discipline.

## 1. The change and its registered expectations

**The builder:** the 45e ballistic class verbatim (K = 24, dipole kernel, α = 0.75, c = 0.5, split-sample τ) with ONE change: churn TRANSFERS — the victim slot's whole accumulator is ADDED to a uniformly chosen receiver slot, then the victim zeroes (`acc[r] += acc[v]; acc[v] = 0`). Content is conserved fleet-wide. Registered consequences to watch, honestly both ways: (i) INTERACTION EXISTS for the first time — the influence probe below is meaningful; (ii) teleportation is REDISTRIBUTED, not removed (the victim still snaps to the origin; the receiver jumps outward by the victim's dipole) — whether the occupied cone rounds is an open empirical read, NOT a registered win; (iii) stationarity changes — total content grows without bound (nothing leaves the fleet); the monopole-free relation removes the per-slot common part, but the per-slot dipole law may drift across windows — the drift is printed as a disclosure, and the split-sample τ + same-pipeline comparison logic carries what it carries.

## 2. Pinned gates (exit 1 on G0 only)

- **G0 (wiring/control):** the destructive-churn twin (same code path, transfer flag off) at 3 seeds reproduces 45e's P0 statistics within seed noise (F_dom/F_m4 bands overlapping 45e's ±3 SE), AND **the free-web influence control**: with destructive churn and common random numbers, a marked extra deposit at t* = N/2 must alter the snapshots of EXACTLY ONE slot forever (the influence theorem verified mechanically).
- **G1 [MEASURED, unreviewed]:** the conservation web, 10 seeds (20263900+): F both conventions vs the 45e lines (reused — the relation pipeline is identical; z printed as a read, not a pre-registered decision); d_ball on 45e's O2 reference; in-window refusals; S₄ (window-1024); the content-growth and dipole-drift disclosures.
- **G2 (THE INFLUENCE MEASUREMENT — the program's first):** 5 common-rng pairs; the marked deposit (10× mean magnitude, fixed direction) into slot c* at t* = N/2; per-commit divergence |χ_B − χ_A| for t > t*: (a) the AFFECTED-SLOT COUNT vs Δb (the epidemic curve — must be ≡ 1 in the control, growing in the conservation web); (b) the affected-commit fraction vs Δb; (c) INFO: the dipole-space front — the max dipole displacement of affected commits vs Δb, against the cone slope τ. All reads; the deliverable is the first measured propagation of influence through a record fleet.

## References

45e (protocol, lines, O2 reference — reused verbatim); the round-46 pin (the free-web influence theorem; conservation-churn named); the particle reframe (note-3p1-manifoldweb, final section); the user's conservation challenge (this round's cause).
