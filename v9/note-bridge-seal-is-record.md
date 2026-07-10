# note-bridge — the seal-is-record pair: the first instantiation design

**Status:** design note, 2026-07-10 (v9 round 41). This note is the deliverable; its receipt (`bridge1`, gates §5) is a later round, run only after the §6 obligations clear. Reviews ON (hostile design review after writing). Spine: paper XIV (shard paper-XIV-stem-spectrum) + Martin–Panangaden CMP 267 + Dowker–Johnston–Surya / Surya–Zalel — the duality map's items 1–3.

## 1. The gap this note closes (the round-36 finding, verbatim scope)

The strategic sweep found THE BRIDGE IS EMPTY: zero receipts measure any v6 law on any web; the seal-is-record postulate (v8 paper 6 phenomenology §1.2, [POSITED]) has never been instantiated; and the two σ's are a name collision (PLAN:198). The v6 side owns laws about *seals* (the quarter law, v6 paper 26 Thm A); the v8/v9 side owns theorems about *webs* (click law, churn, dimension). No object has ever been both. This note specifies the first such object and the first falsifiable bridge measurement.

## 2. The objects and the dictionary (definitions fixed here)

**The web.** The wb-line churn web, (N, M, L) = (2048, 32, 16), C = 3 channels, α = 0.75 (the paper-6 pinned class). All constructions below are conditioned continuations of a common prefix.

**The marked pair (the which-path alternative, web-native).** Fix a prefix W_<t* and a marked commit at time t* into slot c*. The binary alternative χ ∈ {0, 1} is a *content* alternative of that one commit — pinned choice for the first receipt: **χ = the channel identity of the marked click** (k = k₀ vs k = k₁, both ≠ the slot's preferred channel, so the alternative is exchangeable a priori). Two ensembles: grow the web forward from (W_<t*, χ = 0) and (W_<t*, χ = 1) with common random numbers NOT shared after t* (independent futures; the prefix is the only shared object).

**The readout.** A window of post-t* web data, in two graded forms:
- **Labeled readout R_lab:** the raw commit stream in a window [t*, t* + T] (slot ids, channel snapshots) — everything the bookkeeping sees.
- **Covariant readout R_cov (the paper-XIV requirement):** the stem statistics of the continuation order in the same window — occupation counts over the level-3/level-4 covtree nodes (the round-38/39 catalogues are the alphabet). Physical observables of a growth process are stem data (BDGHS via paper XIV); a seal whose content is invisible in R_cov is bookkeeping, not physics.

**The two σ's, disambiguated (resolving PLAN:198).**
- **σ_wp (which-path KL):** D(P₀ ‖ P₁) where P_χ = the distribution of the readout given χ. This is the σ of v6 paper 26 Thm A (there: the monitor pair's KL).
- **σ_arrow (arrow KL):** D(P_fwd ‖ P_rev) of the marked commit's local transition (the forward vs time-reversed step statistics at t*) — the substrate σ of the v8 phenomenology text.
These are different functionals of different pairs. The corpus's name collision dissolves by never again writing either as bare σ.

## 3. What the quarter law does and does not test (the universality trap, named)

Thm A (v6 paper 26, verbatim: −ln BC = σ/4 + (ε²/6)σ + O(σ³), BC = Σ√(P₀P₁), symmetric binary monitor): note −ln BC = D_{1/2}(P₀‖P₁)/2 *identically* (Rényi-½ definition), and ALL Rényi orders coincide to leading order as P₀ → P₁ (the shared Fisher/χ² term). So **in the weak-evidence limit the ¼ ratio is measure-theoretic universality — confirming it on the web would be a fake bridge.** The receipt must therefore gate on the *non-universal* content:

1. **The Fisher identity (the postulate's actual falsifiable core).** Seal-is-record says irreversibility and which-path readout are two faces of one record event *sharing one Fisher object J*. Web test: on the SAME marked commits, measure J_wp (from σ_wp's small-χ-contrast quadratic coefficient) and J_arrow (from σ_arrow's quadratic coefficient under the same contrast dial). The postulate ⇒ J_wp / J_arrow is a fixed, contrast-independent constant (unity in the natural normalization, to be derived in the receipt's pin from the v6 text — an obligation, §6). Independent objects with no shared J ⇒ the ratio drifts with the dial. THIS is the bridge measurement.
2. **The monitor class (the correction coefficient).** The ε²/6 second-order coefficient is specific to the symmetric binary monitor. The web's monitor (P₀, P₁) is an emergent object; measuring its (−ln BC)/σ_wp curve vs σ_wp classifies the web's record channel within v6 paper 26's monitor taxonomy (Part II) — a genuine measured import of web structure into a v6 law's fine structure.
3. **Covariant readability.** σ_wp(R_cov) vs σ_wp(R_lab): the postulate needs the seal content physical, i.e. σ_wp(R_cov)/σ_wp(R_lab) bounded away from 0 as the window grows. Ratio → 0 = the KILL: the marked record's content is relabeling gauge, and the postulate as stated dies on the web (a decisive negative — the bridge would then need a different marked object, not a different law).

## 4. The spine (why this design is now well-posed; paper XIV's three imports)

(i) The observable algebra is the stem algebra — R_cov is not one choice among many, it is THE covariant readout (BDGHS/T4); the level-3/4 catalogues make it computable. (ii) The extension question (DJS / Surya–Zalel via paper XIV §6) says when a quantum-side decoherence functional over the web's alternatives is even well-posed — the bridge's quantum half must be phrased as strong additivity on the stem algebra, not on labeled cylinders. (iii) The continuum side (Martin–Panangaden through paper XIV §9–§10): the completion of the web's interval/stem structure is the object that must eventually carry the v6 laws' geometric face; this note's receipt stays entirely on the finite side — no continuum claim.

## 5. The receipt sketch (gates to be pinned verbatim at the receipt round, with fresh seeds)

- **Gb0 (imprint non-degeneracy):** σ_wp(R_lab) > 0 at 5σ over the permutation null (χ-labels shuffled across ensemble members) on 5/5 prefix seeds. Refusal = the marked alternative leaves no record; redesign the mark, not the law.
- **Gb1 (weak-limit calibration, EXPECTED — explicitly not the bridge):** (−ln BC)/σ_wp → 1/4 as the contrast dial → 0. A refusal here is an estimator bug, not physics (universality); gated only as instrument certification.
- **Gb2 (THE FISHER IDENTITY, the postulate's test):** J_wp/J_arrow constant across ≥ 3 dial values within seed bands, at the pinned normalization. Holds ⇒ the postulate earns [MEASURED-ON-WEB] at this class; drifts ⇒ the postulate is REFUTED-AS-STATED for the wb-line class (and the v8 §1.2 elevation is re-graded).
- **Gb3 (monitor class):** the second-order coefficient of (−ln BC)/σ_wp vs σ_wp measured with CI; classified against the symmetric-binary ε²/6 and v6 Part II's taxonomy.
- **Gb4 (covariant readability):** σ_wp(R_cov)/σ_wp(R_lab) printed vs window length T; the kill semantics of §3.3.
- Estimation note (pinned early because it is where such receipts die): P_χ over readouts is high-dimensional; σ_wp and BC are estimated on COARSENED readouts (the covtree-node occupation vector for R_cov; fixed low-dimensional summaries for R_lab), with plug-in bias controlled by split-sample debiasing and the permutation null; all coarsenings pinned before running.

## 6. Obligations before the receipt round (standing-discipline items)

(O1) Re-verify v6 paper 26 Thm A + Part II verbatim at the source (the v6 ledger rows are COARSE — the standing merge rule) and derive the pinned J-normalization for Gb2 from it. (O2) The dimensional wall: everything here is per-commit and dimensionless; the λ = κ·σ̇ rate conversion is scale-walled (v8 §1.2's dissolution) and NOT touched. (O3) The χ-alternative must be checked exchangeable a priori (both channels off-preference); if the α-asymmetry leaks into the prefix, precondition on symmetric prefixes. (O4) Fresh seeds; pins before code; reviews on.

## References

Round-36 strategic sweep (LOG r36 open: the empty bridge, the missing pair, PLAN:198); v8 paper 6 phenomenology §1.2 (the postulate [POSITED], the dissolution, the two-σ disambiguation source); v6 paper 26 §3.1 Thm A (the quarter law, verbatim) + Part II (monitor taxonomy); shard paper XIV (T4 observables; §6 strong additivity; §9–§10 the completion); the level-3/4 catalogues (rounds 38–39) as R_cov's alphabet; note-duality-map items 1–3.
