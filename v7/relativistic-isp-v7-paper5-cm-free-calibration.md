# The record click-law, V: the gravitational coupling per species is a free calibration — and it shares the spacing's one open gate

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-15. Fifth paper of the v7 program (written before Paper IV); it closes the one weight-zero lane the spacing no-go left permitted. Tags: **[FORCED]** = uniquely required (symbolic / high-precision numeric); **[PERMITTED]** = weight-zero, intrinsic-eligible, not forbidden by the scale no-go; **[BLIND]** = provably outside the gravity sector's determination; **[FREE]** = an unconstrained calibration (a genuine constant of nature the records do not fix); **[OPEN]** = a disclosed, unproved requirement. All numeric claims at mpmath `dps ≥ 60` (CODATA SI) and sympy-exact where structural; receipt `v7/code/p5_cm_calibration.py`.

## Abstract

Paper III proved that the seal spacing `d` is not a fixed quantity and that no record-derived gravitational coefficient can manufacture an absolute scale, while leaving *one* lane explicitly permitted and open: a weight-zero *strength* — the dimensionless gravitational coupling-per-species `c_m = Gm²/ℏc = (m/M_Planck)²` (the gravitational analog of the fine-structure constant; `1.75 × 10⁻⁴⁵` for the electron, `5.91 × 10⁻³⁹` for the proton — the weakness of gravity). This paper settles that lane. `c_m` is **weight-zero and intrinsic-eligible** — the scale no-go provably does *not* forbid it (it carries no absolute length; it is gauge-invariant under the record-length rescaling). But it is also provably **not a gravity-sector output**: by the universality/equivalence-principle theorem of the record-gravity program (the analog of "the Einstein equations do not determine the electron mass"), the gravity sector is *complete and blind* with respect to `c_m` — every executed gravity identity is satisfied for *any* value (the toy values `c_m = 12` and `c_m = 1200` both pass `κ·σ_A/2π = 1.000000000000` in every cell). So `c_m` is not a hole *in* record gravity; it is the **matter sector's spectrum problem**, relocated out of gravity. It factors *exactly* as `c_m = γ_G · ν_m²` with `γ_G = G·σ_A = 1/4` a gravity-side convention and the matter content entirely in the mass-amplitude `ν_m` (the area density cancels identically). That gap inherits the firing fixed point's **mode-dependence** — *illustrated* by the toy slices `η_B = 0.609` vs the coupled `h_* = 0.495` (the physical `ν_m ≈ 8 × 10⁻²³` awaits a matter sector and is not these toy values) — so `c_m` and the spacing `d` *share one sub-problem*, the mode-canonicalization, while `c_m` *additionally* requires a constructed matter sector (a burden `d` does not carry; the two are distinct in role, shared in this gate). The honest verdict: `c_m` is **one free dimensionless coupling per species** — the strength-axis analog of the scale no-go's free unit `κ` (the Tier-A conversion rate, *not* the gravitational `8πG` of `κ·σ_A = 2π`): permitted, well-posed, and open, relocatable only to a matter sector that does not yet exist (the physical `c_m ≈ 10⁻⁴⁵` sits ~44 orders below the corpus's toy record gaps, so those gaps pin nothing physical). The paper pins no value: any number (e.g. the illustrative `γ_G·η_B² = 0.093`, ~44 orders above the physical `c_m`) smuggles in the `1/4` area convention and a toy-mode choice, and the strongest record-number coincidence (`θ_B² = 0.29560` against the Srednicki area coefficient `a = 0.29542`) is refuted algebraically (`θ_B` is a cubic irrational). The blindness result is *proved* (the equivalence-principle theorem); the weight-zero classification and the no-record-coefficient closure rest, like the scale no-go, on the single open premise gate G1. Pre-geometric where it matters: `c_m` is a weight-zero ratio of record numbers throughout; the gravitational constants enter only to exhibit the hierarchy and confirm the weight bookkeeping — the result being precisely that gravity cannot output it.

---

## 1. The permitted lane, and what `c_m` is

The scale no-go (Paper III; the record-gravity program) forbids exactly one thing: a record functional cannot carry the one absolute dimensionful unit (the length↔geometry conversion). Everything weight-zero — every dimensionless ratio — is *eligible* to be a record output. Paper III closed the spacing `d` (not a fixed quantity, no record-derived coefficient fixes its absolute scale) but flagged one weight-zero object as genuinely permitted and unexamined: the dimensionless gravitational *strength*

  `c_m = Gm²/ℏc = (m/M_Planck)²`,

the coupling-per-species — the gravitational analog of the fine-structure constant `α`. Numerically it is the weakness of gravity made dimensionless: `c_m(electron) = 1.7518 × 10⁻⁴⁵`, `c_m(proton) = 5.9061 × 10⁻³⁹` (receipt `p5`), so two electrons attract gravitationally `~10⁻⁴³` times more weakly than they repel electrically. A derivation of `c_m` would be a statement about *why gravity is weak* — the hierarchy problem. This paper asks whether the records can output it, and finds: not gravity's to give.

---

## 2. `c_m` is weight-zero and intrinsic-eligible [PERMITTED]

Under the record-length gauge `l → μl`, the generators scale with definite weight: `G ~ l²` (weight `+2`), a mass `m ~ 1/l` (weight `−1`), `ℏc` (weight `0`). Hence

  `weight(c_m) = weight(G) + 2·weight(m) − weight(ℏc) = (+2) + 2(−1) − 0 = 0` **[FORCED]**

(`p5`, sympy), and `c_m` is gauge-invariant: scaling `l → μl` sends `G → μ²G`, `m → m/μ`, so `Gm²` — and therefore `c_m` — is unchanged (verified `c_m(μl)/c_m(l) = 1` to `< 10⁻⁴⁰` for `μ = 1.7, 5`). Equivalently `c_m = (m/M_Planck)²` is a ratio of two masses, squared: the absolute scale cancels. So `c_m` lives entirely inside the intrinsic (weight-zero) ring the records *do* carry, and the scale no-go does **not** forbid it. This is the precise sense in which `c_m` is the permitted lane: unlike `σ_A`, `G`, or the absolute `d` (weight `±2`, forbidden), `c_m` is a legitimate candidate record output.

---

## 3. But gravity cannot output it: the sector is complete-and-blind [BLIND]

Permitted is not the same as produced. Two distinct corpus results combine to place `c_m` *outside* the gravity sector's reach, and they should not be conflated. First, the **record equivalence principle** (H1, the universal record footprint: every unit-evidence matter event sources the *same* deletion response, species-independently) is proved as a quotient-functoriality/covariance theorem; its job is to make "the" matter ratio *well-defined* — without it the matter area per event is not a single number. Second — and this is the blindness proper — the gravity sector is **complete with respect to** that ratio: **no gravity-sector identity constrains its value** (the corpus's blindness scan, operationalized by the toy-value test of §4). The matter content of `c_m` lives entirely in its mass-amplitude factor `ν_m` (§5); the area normalization `γ_G` is a gravity-side convention (§5). What gravity is blind to is the **hierarchy invariant** in this role — the *record analog* of `Gm²/ℏc` (paper6 §9's `A_matter/A_grav` ratio) — which equals the matter ledger's evidence-content per primitive event `m̂` (Thm 6.1's "one constant, three roles": spectral gap = lightest-mass content = deletion work). This is a **role identity across unit systems**, not a numerical one: the same invariant reads `m̂ ≈ 0.156` nats in record-content units and `c_m ≈ 10⁻⁴⁵` in SI-strength units, the two bridged only by the (unbuilt) matter-sector calibration. Gravity is blind to it *in its matter factor* and carries `γ_G` only as a convention — neither is gravity's to fix.

This is the record-gravity analog of a familiar statement: the Einstein equations do not determine the electron mass. `c_m` is **not a hole in record gravity**; it is the matter sector's spectrum problem, relocated out of gravity — and *should* be, since a gravity sector that fixed `c_m` would be one in which the geometry determined the matter spectrum, which neither GR nor record-gravity does. This blindness is **proved** (the EP theorem plus the blindness scan); unlike the weight-zero classification (§2) and the no-record-coefficient closure (§5), it does *not* rest on the scale-no-go's open premise (§7).

---

## 4. `c_m` is currently free: the toy-value test [FREE]

That gravity is blind to `c_m` is shown cleanly by a toy-value test in the corpus (paper6 §9's blindness scan): the values `c_m = 12` and `c_m = 1200` **both** satisfy *every* executed gravity identity — `κ·σ_A/2π = 1.000000000000` in all four cells — i.e. the identities are **NOT-SELECTED** by `c_m`. (This four-cell scan is an inherited corpus result; the present receipt reproduces its *structural* basis — the gravity invariants `κ·σ_A = 2π` and `G·σ_A = 1/4` are functions of `G, σ_A` alone and do not depend on `c_m`, so any value passes; `p5`.) No record relation presently constrains its value. So at the current state of the program `c_m` is a *genuinely free* dimensionless parameter, not a circularly-derived one. This is the positive content of "free calibration": it is not that we have failed to compute `c_m`, but that the structure that could constrain it (a matter sector) is absent, and the structure that exists (gravity) provably cannot — leaving `c_m` exactly as free as the scale no-go's free unit `κ` — the Tier-A content→commit-order conversion *rate*, **distinct** from the fixed gravitational coupling `κ = 8πG` in `κ·σ_A = 2π` above. `c_m` is the **strength-axis analog of that free `κ`**: one free dimensionless coupling per species.

---

## 5. The factorization, and the shared gate with the spacing `d` [OPEN]

`c_m` factors *exactly* as a product of two weight-zero record numbers. Writing the area-law coefficient `γ_G = G·σ_A` and the matter gap `ν_m = m/√σ_A`,

  `c_m = γ_G · ν_m² = (G·σ_A)·(m²/σ_A) = G m²` — the record area density `σ_A` cancels identically (`p5`, sympy-exact).

`γ_G = G·σ_A = 1/4` is the Bekenstein area coefficient — a **ratio-of-twins convention** fixed by the gauge, not physics; the matter content lives **entirely in `ν_m`**, the particle mass in record `√`-area units. (The *same* hierarchy invariant, in the corpus's record-content units, is the matter ledger's evidence-gap `m̂ ≈ 0.156` nats — Thm 6.1's "one constant, three roles" — which is *not* numerically the SI strength `c_m ≈ 10⁻⁴⁵`; the record-content and SI-strength normalizations are bridged only by the unbuilt matter sector, so the content axis and the strength axis must not be conflated.) So fixing `c_m` *is* fixing `ν_m` — a matter-sector question — with `γ_G` a fixed `1/4`.

`ν_m` is the genuine open object, and it is presently *unbuilt*: for the physical electron `ν_m = √(c_m/γ_G) ≈ 8.4 × 10⁻²³`, a number no current record structure supplies. What the corpus *does* have is the **mode-canonicalization structure** any such gap inherits: `ν_m`, like the spacing `d`, would be a root of the firing fixed point `∂ψ/∂h = e^{−h}`, whose root is **mode-dependent** — *illustrated* by the toy slices `η_B = 0.609` (one-mode) vs `h_* = 0.495` (coupled), `|η_B − h_*| = 0.114`, no canonical member (`p5`). These toy lattice values are ~22 orders above the physical `ν_m`; they exhibit the *structure*, not the value, and are not candidate masses.

So the genuinely **shared** bottleneck between `c_m` and `d` is *precisely the mode-canonicalization*: both are mode-dependent firing-fixed-point outputs with no canonical member, and a single canonicalization principle would pin *both* (`d` among `{C(η_B), C(h_*), …}`, and `ν_m` hence `c_m`). It is **not** that the two are the same in every respect — Paper III rightly calls them categorically distinct in *role* (a strength vs a spacing), and `c_m` *additionally* requires a constructed matter sector and a hierarchy-selection principle that `d` does not. The honest, precise unification: **`c_m` and `d` share one sub-problem — the mode-canonicalization — while `c_m` carries the extra matter-sector burden.** That shared gate is the paper's forward-pointing contribution.

One caveat keeps "free" honest in the *other* direction: the corpus's toy record evidence-gap `m̂` is itself bounded (the gap theorem floors it at the one-diamond minimum `C(η_B) = 0.156` nats for the unoriented class), so this toy record gap `m̂` is `O(0.1)` — yet the **physical** `c_m(electron) = 1.75 × 10⁻⁴⁵` lies ~44 orders *below* that toy floor. The toy record gap therefore does **not** bound the physical coupling; the chasm between them *is* the unbuilt matter sector (and, for an oriented/chiral matter ledger, the gap theorem's lower bound is anyway forfeited — the spectrum can run gapless). So the toy gap pins nothing physical: it reinforces, rather than tempers, that `c_m`'s value awaits the matter sector.

---

## 6. What a derivation would require [OPEN]

A non-circular derivation of `c_m` would need, in order:

- **a constructed matter sector** with its own commitment-fixed ledger producing physical masses as canonical record spectral gaps. The corpus has only *toy* gaps (the 1d Ising `1/η_B = 1.641`, the 2d Onsager `23.355`); the proton and electron are not yet record structures. The corpus rates this "beyond all current corpus technology";
- **a mode-canonicalization** selecting *which* gap is "the" mass (the shared bottleneck of §5);
- **a hierarchy-selection principle** (the analog of solving the hierarchy problem). The one named candidate generator is the Chamseddine–Connes spectral action, but it only ever yields the weight-zero invariant `G·Λ²` (a scheme-dependent pure number — `3π²`, Sakharov `192π²/N`), which fixes the *ratio* `G/l_step²`, **not** `c_m = Gm²` (that needs a separate `(m/Λ)²`), and rests on an unverified profile identification. It is a candidate, not a prediction.

None of these exists. The equivalence-principle prerequisite (universality) *is* proved — but only as an admissibility *condition* on theories, not as a statement about a built sector. So `c_m` is **derivable only modulo a matter sector that does not yet exist**, and that matter sector is itself a multi-paper program.

---

## 7. What this paper claims and does not

It **claims**, with receipts: that `c_m = Gm²/ℏc` is weight-zero and intrinsic-eligible (gauge-invariant; the scale no-go does not forbid it) (§2); that it is nonetheless provably **not a gravity-sector output** — the sector is complete-and-blind with respect to it, exactly as GR does not fix `m_e` (§3); that it is **currently free** (the toy-value `12`/`1200` both pass every gravity identity, which are `c_m`-independent) (§4); that it factors *exactly* as `γ_G·ν_m²` (with `γ_G = G·σ_A = 1/4` a convention, the matter content entirely in `ν_m`) and shares the spacing `d`'s **mode-canonicalization** sub-problem, while `c_m` *additionally* requires a constructed matter sector (§5–6); so that `c_m` is **one free dimensionless coupling per species — the strength-axis analog of the scale no-go's free unit `κ`** (the Tier-A conversion rate, not the gravitational `8πG`) (§4–5).

It does **not** claim: a *value* for `c_m` — any number smuggles in the `1/4` convention and a mode choice, and the one illustrative number `γ_G·η_B² = 0.093` is ~44 orders of magnitude above the physical `c_m(electron) = 1.75 × 10⁻⁴⁵` (it uses a toy lattice tilt, not a physical mass), so it is self-evidently not a candidate; that the hierarchy problem (H2) is solved (it is relocated, not solved); or that any record-number coincidence is a derivation — the strongest, `θ_B² = 0.295598` against the Srednicki area coefficient `a = 0.295417`, is refuted algebraically (`θ_B²` is the root of the irreducible `s³+s²+3s−1`, a cubic irrational, distinct from `a` and on the wrong axis). On scope: the **blindness result of §3 is proved** — we lean only on its G1-*free* sub-results (the equivalence-principle theorem and the algebraic `c_m`-independence of the executed gravity invariants), not the pinned-sector form of Thm 6.1 — so blindness is independent of any open premise; it is the weight-zero classification (§2) and the no-record-coefficient closure (§5) that rest — like the scale no-go — on the single open premise **gate G1** (no sealed law consumes the record area outside the continuum labeling map). The honest one-line summary: **`c_m` is permitted (weight-zero) but is not gravity's to give — it is the matter sector's free per-species calibration, the strength-axis twin of the scale no-go's free unit, sharing the spacing's mode-canonicalization gate while carrying the extra matter-sector burden.**

---

## 8. Precision discipline

Every numeric quantity was computed in mpmath at `dps ≥ 60` (CODATA-2018 SI) and sympy-exact where structural. The hierarchy values (`c_m(e) = 1.7518 × 10⁻⁴⁵`, `c_m(p) = 5.9061 × 10⁻³⁹`, `c_m = (m/M_Planck)²`, `c_m ∝ m²` with ratio `(m_p/m_e)²`), the weight-zero classification and gauge invariance (`weight(c_m) = +2 + 2(−1) − 0 = 0`; `c_m(μl)/c_m(l) = 1`), the *exact* factorization `c_m = γ_G·ν_m² = Gm²` with `σ_A` cancelling and `γ_G = G·σ_A = 1/4` (sympy), the `c_m`-independence of the gravity invariants `κ·σ_A, G·σ_A` (the NOT-SELECTED structure), the physical `ν_m(e) ≈ 8.4 × 10⁻²³` (≫ below the toy gaps), the mode-dependence of the matter gap (`η_B = 0.609 ≠ h_* = 0.495`, the shared bottleneck), the `~44`-order gap between the illustrative `0.093` and the physical `c_m`, and the algebraic refutation of the `θ_B²`/Srednicki numerology are all in `v7/code/p5_cm_calibration.py` (10 machine checks, all pass). Never float64.

---

## References

**Companion (this program).**

[I] *The record click-law, I* (`v7/relativistic-isp-v7-paper1-record-click-law`).
[II] *The record click-law, II: the content supply* (`v7/relativistic-isp-v7-paper2-content-supply`).
[III] *The record click-law, III: the seal-spacing no-go* (`v7/relativistic-isp-v7-paper3-seal-spacing-no-go`) — the scale no-go, the permitted weight-zero `c_m` lane this paper closes, and the mode-canonicalization bottleneck `c_m` shares with `d`.
[6] *`A_rec` gauge closure* (v6 paper6) — Theorem G (the weight grading); §9 the H1 (equivalence-principle prerequisite) / H2 (hierarchy selection) framing; the toy-value `c_m` NOT-SELECTED result.
[7] *Record-gravity universality* (v6 paper7) — the universal record footprint / equivalence principle as a theorem (gravity is complete-and-blind to the matter spectrum); Theorem 6.1.
[57] *Gravity from sealed records* (v6 paper57) — the scale no-go; `c_m` as weight-zero / intrinsic-eligible (the open hierarchy question).
[XI] *Emergent Einstein equations without an emergent Newton constant* (`v6/publishable/paper-XI-sealed-record-gravity-no-go`) — the scale no-go and the matter-sector hierarchy `c_m` the no-go does not forbid.
