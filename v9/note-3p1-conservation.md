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

## The leak = sealing connection (user-posed, 2026-07-10; appended)

The user's question — "can the leaks be basically entanglement?" — resolves into three layers, recorded for the diffusion round and the bridge program:

1. **Strictly: no bipartite entanglement.** The webs are classical stochastic processes; leaks create correlations-through-shared-history (two slots holding content of common lineage), which is classical mutual information. The corpus's own sobriety results stand (v5 paper 14's Bell verdict; magic ≠ indivisibility).
2. **But leak-to-the-fleet IS the structure of entanglement-with-the-ENVIRONMENT — i.e., DECOHERENCE — i.e., SHARD's own sealing.** A slot's content dispersing irreversibly into many other slots is which-path information becoming environmental record: the microscopic mechanism of a SEAL. This is the missing substrate the round-41 bridge design needed — the coupled builder gives the quarter-law/Fisher-identity program its first concrete mechanism (σ_wp of a marked slot vs leak rate; the readout ensembles of note-bridge-seal-is-record §2 now have a dynamics that actually disperses the mark).
3. **The separating signature is MONOGAMY** (the corpus already owns the theorem import: Toner–Verstraete, v8 paper 16). Broadcast/diffusive leaks → promiscuous many-party correlations → classical, decoherence-like (the environment reading). EXCLUSIVE PAIRED exchange (two slots swapping content with each other only) → the only in-ontology candidate for entanglement-LIKE two-party structure, testable with the corpus's CHSH/χ_AB instruments (the ml3b two-party locus line). Named as the round-48+ fork: diffusion-churn (the decoherence/sealing pole) vs paired-exchange churn (the correlation pole), with the monogamy structure of induced correlations as the printed discriminator.

## Receipt 48 — diffusion-churn (pinned here, committed strictly before running; NO-REVIEW, token-lean)

Builder = round 47 verbatim except churn: each tick, one random slot transfers a FRACTION g of its content to one random receiver (no zeroing, no jumps anywhere; conservation holds). Rate matched to the old per-slot content turnover: g = 1/L = 0.0625 (main, 10 seeds 20264000+); g = 0.25 (fast-mixing probe, 5 seeds). Measures: F both conventions vs the 45e lines; d_ball (45e VOLREF); refusals; S₄; eig3/1 + fraction (the registered collapse watch: continuous mixing homogenizes slot velocities → drift-branch risk); the influence curve (3 pairs); dipole-drift disclosure. Exit 1 only on non-finite F at the main dial. Registered honestly both ways: if the scars own the residual, F drops toward the lines; if mixing homogenizes, the dichotomy's drift signature appears instead.
