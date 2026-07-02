# The record click-law, XV: the everpresent cosmological-constant scaling as a weight-0 record fact — native exponent, imported centering, and the curl-free obstruction to a self-derived Λ-walk

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-16. Fifteenth paper of the v7 program. It is a **positioning / classification** note, not a prediction of dark energy: it asks precisely which part of Sorkin's *everpresent-Λ* argument the record substrate reproduces, which part it merely re-packages, and which part it cannot supply — and finds a structural reason for the last. Tags: **[ROBUST]** / **[NATIVE]** = a record-intrinsic, weight-0, derived fact; **[FORCED]** = uniquely required (symbolic / high-precision numeric); **[IMPORT]** = an input the records provably cannot supply; **[NO-GO]** = a proved impossibility in scope; **[OPEN]** = a disclosed, unproved obligation. Structural / algebraic identities are sympy-exact or at mpmath `dps = 120`; the single Monte-Carlo slope in each scaling receipt is a **numerical estimate, flagged as such, with its sympy-exact target exponent printed alongside**. Receipts `v7/code/p15a_routeA_conjugacy.py` (13 checks), `p15b_routeB_drift_walk.py` (13), `p15c_weight_classification_nogo.py` (27), `p15d_desitter_selfconsistency.py` (18), `p15e_numerology.py` (14), `p15f_routeC_action_density.py` (23), `p15g_zero_mean_equivalence.py` (19) — **127 checks, all pass**.

## Scope — three guards, stated first [FORCED scope discipline]

Because "the cosmological constant" invites overreach, the boundaries come before the results:

1. **This reproduces and classifies the everpresent *scaling*, not the *value*.** The robust, falsifiable content of Sorkin's argument is the *scaling* `δΛ ∼ ±V^{−1/2}` (exponent exactly `−1/2`). That is reproduced and, more, *classified*. The absolute `Λ ∼ 10^{−120}` is **Sorkin's numerology reproduced, not improved** — algebraically one measured ratio (§8). No new prediction of dark energy is claimed.
2. **The argument's heuristic spine is Sorkin's, cited as such.** The `−ΛV` conjugacy, the action random-walk `Λ = S/V` (Ahmed–Dodelson–Greene–Sorkin, *Phys. Rev. D* **69**, 103523 (2004), Eq. 5), and `δΛ ∼ 1/√V` are the literature's. What is the record substrate's is stated separately and narrowly: the *native* status of the inputs, the *weight-classification*, and the *curl-free obstruction* of §7.
3. **The everpresent object is the absolute standard deviation of a *zero-mean* Λ.** Sorkin assumes `⟨Λ⟩ = 0`; the relevant object is `std(Λ)`, which scales as `V^{−1/2}` (exponent `−1/2`). The standard deviation of a *nonzero-mean* `Λ ∼ 1/V` scales as `V^{−3/2}` — a **distinct, excluded** object that every receipt computes and labels the wrong target. The two exponents differ by a clean gap of `1`.

Inside those guards, the results are machine-verified.

---

## 1. What Sorkin's everpresent-Λ is

Sorkin's heuristic (∼1987–1991, a decade before the 1998 supernova discovery; quantified by Ahmed–Dodelson–Greene–Sorkin 2004, hereafter ADGS) has four inputs:

(i) **Conjugacy.** The cosmological term in the gravitational action is `S_Λ = −(1/8πG)·Λ·V`, so Λ is conjugate to the spacetime 4-volume `V` "in the same way energy and time are conjugate." In unimodular gravity this is a clean canonical bracket, with uncertainty relation `(δΛ/8πG)·δV ≳ ℏ/2`.

(ii) **Number = volume.** In fundamental units the discrete element count equals the volume, `⟨N⟩ = V` (unit sprinkling density).

(iii) **Poisson fluctuations.** Local Lorentz invariance forces the order↔geometry map to be Poisson, so holding `N` fixes `V` only up to `δV ∼ √N`.

(iv) **Zero mean.** The target value `⟨Λ⟩ = 0` is *assumed* ("for reasons still to be understood").

Combining (i)–(iii): `δΛ ∼ 1/δV ∼ 1/√V`. Equivalently (ADGS Eq. 5), reading Λ as the action *density* `Λ = S(N)/N` with `S(N) = Σᵢ ξᵢ` a zero-mean random walk, `S ∼ √N` gives `Λ ∼ √N/N = 1/√N = 1/√V`. With (iv), Λ is of order its own fluctuation at every epoch — **everpresent** — and `V ∼ R_H^4 ∼ 10^{240}` Planck volumes gives `Λ ∼ 10^{−120}`, the observed order.

What follows asks: of (i)–(iv), what does the record substrate *own*, what does it *re-package*, and what can it *not* supply?

---

## 2. The four inputs have native record counterparts

Three of the four inputs are corpus theorems, not imports:

- **The seals *are* the causet** (v6 Paper 1, literal, not analogical): each sealed record event is a division event of the discrete order. So the sprinkled set whose statistics drive the argument is the record set itself.
- **Number = volume** `[NATIVE]`: `E[N] = V/l_step^d` (v7 Paper 11 §3 "Number → the volume measure, up to `l_step`", receipt `r2`; Myrheim–Meyer counting). This is input (ii) verbatim.
- **Poisson `δN = √N`** `[NATIVE]`: `Var[N]/E[N] = 0.97 ≈ 1` (v7 Paper 11 §3, receipt `r2`), volume recovered to `∼1/√N`. This is input (iii) verbatim.
- **Λ as a non-sourced integration constant** `[NATIVE, DERIVED]`: the Clausius equation of state `δQ = TδS` on local causal horizons delivers the Einstein form, and divergence + contracted Bianchi demote Λ to a non-sourced integration constant `Λ₀` whose only sourced piece is the drift `∇_ν Λ = 8πG η_ν` (v6 Paper 57 §1.5, residual identically 0). This is the **unimodular fork reached thermodynamically** — input (i)'s *freeness* without a Hamiltonian. Henneaux–Teitelboim unimodular gravity is one rigorous *packaging* of the same freeness; Jacobson reaches it independently.

Only input (iv) — the zero-mean centering — has no native counterpart. §7 shows this is not an accident.

---

## 3. The scaling [ROBUST] — two routes, one statistic

**Route A — conjugacy** (`p15a`, 13/13). With `V = N·l_step^d` (v7 Paper 11 §3, receipt `r2`) and `δN = √N` (Poisson), the conjugate relation `δΛ ∼ ℏ/δV` gives `δΛ ∼ 1/(√N · l_step^d)`; in record-curvature units `δΛ·l_step² = 1/√N`. The exponent in both `V` and `N` is **exactly `−1/2`** (sympy logarithmic derivative); the Monte-Carlo slope of `std(Λ)` over eight volume decades is `−0.49985` (flagged numerical estimate, target `−1/2`, `|err| = 1.5×10^{−4}`). The conjugacy bracket `δΛ·δV ∼ ℏ` is **grep-confirmed absent from the corpus** (0 hits); the only native canonical pair (the HKT metric/momentum pair, Paper 1 line 84) "leaves Λ undetermined." Route A is therefore *conditional on that one import*. The nonzero-mean `V^{−3/2}` object is computed and **excluded** as the wrong target.

**Route B — the corpus's own drift** (`p15b`, 13/13). The corpus owns a *sourced* drift `∇_ν Λ = 8πG η_ν` (Paper 42 line 191, Josset–Perez–Sudarsky form). Random-walking it over `N` Poisson seal increments as `Λ = S(N)/N` (ADGS Eq. 5, the literature heuristic, **not** a record invention) gives two readings:

- **(a) bare one-signed drift:** `S(N) ∼ +N`, so `|⟨Λ⟩| ∼ N^0` — a non-decaying *mean*, the quantity Paper 42 prices as undersourcing `ρ_Λ` by `10^{9.2}`–`10^{17}` across its benchmarks. Slope of `|⟨Λ⟩|` is `≈ 0`, **not** `−1/2`.
- **(b) zero-mean fluctuation:** `S(N) ∼ √N`, so `std(Λ) = √N/N = N^{−1/2}`. Slope `−0.49539` (flagged, target `−1/2`); the normalization `V·δΛ² = N·std²` is flat across `N = 10²…10⁶` (max/min `1.10`).

Reading (b) **reduces sympy-exactly to Route A's conjugate reading**: `δΛ_B − δV/V = 0` (identical `V^{−1/2}` scaling). The two routes are therefore one statement — **the central-limit theorem on the corpus's already-verified Poisson seals** — not competitors. Route B is a genuine *internal link*: the corpus already holds the seal-flux fluctuation `δη` (Paper 4), but routes it to source-density / decoherence, not to a Λ value (the significance of which is §7).

---

## 4. The weight-classification [ROBUST] — the value-add over Sorkin

The relabeling automorphism `g_λ` (Paper 6, Theorem G) grades every quantity by its length-weight. `p15c` (27/27, sympy-exact) computes:

- **Mean** `Λ₀`: `g_λ(Λ₀) = μ^{−2}·Λ₀`, **weight `−2`** — the de Sitter twin of `σ_A/G`, **scale-gated and walled** by the Paper 57 no-go (the de Sitter relation `S_dS = π/(G·Λ₀) = N_dS` fixes only the weight-0 *product* `G·Λ₀ = π/N_dS`, never absolute `Λ₀`).
- **Variance handle** `δΛ·l_step²`: `g_λ`-invariant, **weight `0`**, and sympy returns it exactly as `N^{−1/2}` — a pure number, the seal count. **Record-eligible; the scale no-go explicitly *allows* it.**

The MEAN-sector weights `{−2, −3, −5, +2}` (carrying `Λ₀`, `∇Λ`, `η`, and `G`; the count `N_dS` is a ratio of two weight-`−2` data and is itself weight `0`) are **disjoint** from the everpresent weight `0`. Therefore **both the Paper 57 scale no-go and the Paper 42 drift are silent on the variance** — neither precludes it nor generates it. The everpresent fluctuation is a genuine *third category*, orthogonal to the mean-value no-go and the mean-drift pricing.

This classification — *which part of the prediction is structural and which is imported* — is what the record substrate adds that Sorkin's argument never had. Sorkin asserts the value; the records *grade* it.

---

## 5. De Sitter self-consistency [ROBUST]

`p15d` (18/18, sympy-exact): Paper 57's *own* de Sitter mean already obeys `Λ₀ ∼ V_dS^{−1/2}` — horizon radius `r_dS ∼ Λ₀^{−1/2}`, 4-volume `V_dS ∼ r_dS^4 ∼ Λ₀^{−2}`, hence `Λ₀ ∼ V_dS^{−1/2}`. This is the **same `−1/2` exponent** as the everpresent fluctuation `δΛ ∼ V^{−1/2}` (exponent difference exactly `0`), with fluctuation/mean ratio `O(1)`. So "fluctuation of order the (assumed-zero) mean" is de Sitter **self-consistency, not tension**. The match is of *exponents*; both absolute values remain weight-`−2` imports.

---

## 6. The intensive reading is native [NATIVE] — unimodular gravity is not needed for the *sign*

The everpresent scaling shrinks (`V^{−1/2}`) rather than grows (`V^{+1/2}`) for exactly one reason: Λ is read **intensive** (the action *density* `S/V = ∂S/∂V`) rather than **extensive** (the accumulated action `S`). `p15f` (23/23) makes the dichotomy sharp: building `S(N) = Σᵢ ξᵢ` of zero-mean unit-variance increments, the extensive reading `Λ_ext = S` has slope `+1/2` (the wrong, growing reading), while the intensive reading `Λ_int = S/N` has slope `−1/2`. The exponent's **free-symbol set is `{N}` only** — `ℏ` is *literally absent* from the exponent; the `−1/2` is classical discreteness statistics.

What selects intensive over extensive is the universal `−ΛV` coupling — `Λ = −8πG·dS/dV` is degree-0 (intensive) while `S_Λ = −ΛV/8πG` is degree-1 (extensive). **That coupling is in every GR action, not specifically the unimodular one**, and it is present in the record substrate via the Paper 57 equation of state. This is the entire load-bearing native fact for the *sign*: the intensive reading fixes that the everpresent scaling **shrinks** (`V^{−1/2}`, not `V^{+1/2}`) — it is degree-0 versus degree-1 in `V`, and that dichotomy is **independent of the sign distribution of the per-seal increments**. So Λ is delivered as a local intensive density **natively**, with no unimodular Hamiltonian and no `ℏ` in the exponent. The intensive reading is **silent on the zero-mean centering** — whether the per-seal `Λ`-kick is sign-balanced is a separate question, deferred to §7, where it is found `IMPORT`.

**Conclusion of §6:** for the *sign* of the exponent (and, with §§3–5, for the whole weight-0 structural content), unimodular gravity is **not load-bearing** — at most one rigorous packaging of a coupling the records already carry. The centering — the one remaining ingredient — is taken up next.

---

## 7. The centering is an irreducible import [IMPORT] — and the records say *why* (the curl-free obstruction)

The strong reading would be "unimodular gravity is merely packaging." It is not — and the obstruction is the substantive result of this paper.

**The residual collapses to one fact.** `p15g` (19/19, sympy-exact) proves a three-way equivalence (all residuals `0`): with `Λ = S/V`, `V = N`,
```
[ δΛ·δV ∼ O(1) ]  ⟺  [ δS ∼ √N ]  ⟺  [ zero-mean, O(1)-variance per-seal increment + CLT ].
```
and proves *both* conditions necessary: a biased increment (`m ≠ 0`) gives a non-decaying `N^0` mean (not `−1/2`); a scale-dependent variance (`v ∼ N^p`) gives exponent `(p−1)/2`, off `−1/2` unless `p = 0`. So the entire everpresent residual — everything §§3–6 did *not* already make native — is the single statement: **the per-seal cosmological-action increment is zero-mean and O(1)-variance.** Equivalently, Sorkin's input (iv).

**The records do not supply it — and structurally point the other way.** The corpus splits the non-conservation `η_ν = ⟨η_ν⟩ + δη_ν` (v5 Paper 3 §4; publishable Paper 4 §4). Because Λ is a scalar, consistency requires its source be **curl-free / a gradient** (`η_ν = ∇_ν φ`, v5 Paper 3 lines 148–150), and the corpus then proves:

1. **Only the curl-free mean `⟨η₀⟩ = w(t)` sources Λ**, via `Λ(t) = Λ₀ + 8πG∫w dt` — and it is **one-signed**, equation of state *heating, `w > 0`* (v5 Paper 3 line 302). A monotone *drift*, exactly the non-decaying mean Paper 42 prices (undersourcing by `10`–`17` orders), **not** a zero-mean `√N` walk.
2. **The genuinely sign-balanced fluctuation `δη` is *not* curl-free**, "cannot be absorbed into Λ," and is routed to gravitational **decoherence** (Einstein–Langevin metric noise; v5 Paper 3 lines 186–191).
3. **Foundationally, a seal is one-signed.** The per-seal content increment is `dχ = σ_step = D(P_AB‖P_BA) ≥ 0` (v7 Paper 1 line 56, Arrow-Positivity / Gibbs); the seal hazard `λ ≥ 0`, CP-divisible and monotone (Paper 56 lines 85–88). And the only candidate dynamical tie of a per-seal kick to a rate — "decoherence rate = seal rate = σ" — is itself a **proposed law [TARGET]**, not a theorem (Paper 56 line 52).

So the everpresent bracket needs the **conjunction** {sign-balanced} **and** {Λ-eligible}, and the records deliver each property only on the *wrong* object: sign-balanced → decoherence; Λ-routed → one-signed heating. **Sign-balance and Λ-eligibility are mutually exclusive in the corpus's own construction.** This is a structural *reason* — not merely an unbuilt gap — that the everpresent magnitude is not self-derivable from the record dynamics. Sorkin's input (iv) is genuinely external; unimodular gravity (or any equivalent zero-mean-conjugacy postulate, e.g. the bracket `δΛ·δV ∼ ℏ` that makes Λ the zero-mean conjugate of `V` by construction) is one packaging of exactly this residual.

**[OPEN] The named flip.** No corpus no-go *bars* a native derivation; it is un-built and presently *contradicted* by the curl-free routing. To flip the verdict to native one would have to (i) prove that the curl-free, Λ-sourcing projection of the homogeneous `w`-mode *fluctuation* is itself zero-mean about the one-signed mean `w` (sign-balanced even though `⟨w⟩ > 0`) — overturning the present routing that sends `δη` to decoherence — and (ii) prove a genuine CLT giving `δΛ ∼ V^{−1/2}`. Until then the centering is an irreducible import.

---

## 8. The numerology [IMPORT] — Sorkin's, reproduced not improved

`p15e` (14/14, dps = 120). Two objects must be held apart, because conflating them overcounts the imports.

**The physical fluctuation is scale-free — it does not need `G`.** As a curvature (dimension `1/length²`), the everpresent fluctuation is `δΛ_phys ∼ 1/√V_phys`, and the Planck length **cancels**: `δΛ_phys = (1/l_step²)·(l_step²/√V_phys) = 1/√V_phys ∼ 1/R_H² ∼ H²` — Sorkin's `ρ_Λ ∼ V^{−1/2} ∼ H² ∼ ρ_critical`. So the *physical* everpresent needs only the **cosmic size** `R_H` (one cosmological datum), **not** `G`/`l_step`. This is the literal content of "everpresent": Λ self-tunes to the ambient horizon scale at every epoch.

**The dimensionless `10^{−120}` is the *only* place `l_step` (= `G`) enters — and there it is a tautology.** Expressing Λ in Planck units forms the ratio `Λ·l_step² = (l_step/R_H)²`; with `V = R_H^4` this is `δΛ = 1/√V = R_H^{−2} ≡ 1/R_H² = Λ_obs` *identically* (`log₁₀(predicted/observed) = 0.0`, `|·| < 10^{−90}`; the match is algebraically **consistent with `d = 4` alone** — *given* the everpresent coincidence `δΛ ≈ Λ_obs` taken as exact input, since both sides are by construction `∝ R_H^{−2}`; "forces" would overstate a tautology). The famous `10^{−120}` is then just the one measured ratio `R_H/l_step ∼ 10^{60.93}`, squared — the universe's size in Planck lengths, restated, not a derived number (`N = (R_H/l_step)^4 ∼ 10^{243.7}`, `δΛ ∼ 10^{−121.86}`).

So the magnitude is gated on exactly **two independent scales**: the cosmic size `R_H` (`∼1/H₀`; the *physical* `δΛ ∼ H²` needs only this) and `l_step = Planck` (`= G`; needed only to write the dimensionless Planck-units number, where the Paper 57 no-go forbids *deriving* it but never *importing* it) — with the `O(1)` coefficient riding on the §7 centering. Importing `G` therefore lands the Planck-units number but adds no prediction, and is orthogonal to the §7 obstruction: it fixes the scale *unit*, never the *sign* of the kick. The **exponent is robust**; the magnitude is Sorkin's numerology reproduced, not improved.

---

## 9. Provenance — what is native vs imported, exponent vs magnitude

| Ingredient | Status | Fixes | Receipt / source |
|---|---|---|---|
| Seals are the causet | `NATIVE` | — | Paper 1 (literal) |
| Number = volume `V = N·l_step^d` | `NATIVE` | magnitude | v7 Paper 11 §3 (receipt `r2`) |
| Poisson `δN = √N` | `NATIVE` | **exponent** | v7 Paper 11 §3, receipt `r2` (Var/E=0.97) |
| Λ a non-sourced integration constant | `NATIVE` (derived) | — | Paper 57 §1.5 |
| `−ΛV` coupling → Λ intensive (the *sign*) | `NATIVE` | **exponent** | `p15f`; Paper 42 L184/191 |
| Sign-balanced *Λ-eligible* η-fluctuation | `[OPEN]` (the §7 flip) | — | not curl-free; routed to decoherence (v5 Paper 3 L186–191) |
| Weight-classification (variance wt-0 / mean wt-(−2)) | `NATIVE` | — (value-add) | `p15c` |
| de Sitter `−1/2` self-consistency | `NATIVE` | — | `p15d` |
| **Zero-mean centering of the Λ-kick** | **`IMPORT`** | **exponent** | `p15g`; obstruction §7 |
| O(1) per-seal action quantum (bracket coeff.) | `IMPORT` | magnitude | `p15b` (`c² = N·std²`) |
| Cosmic size `R_H ∼ 1/H₀` (sets the *physical* `δΛ ∼ H²`) | `IMPORT` | magnitude | `p15e` |
| `l_step = Planck` (= `G`; only for the dimensionless `10^{−120}`) | `IMPORT` | magnitude | `p15e` (Paper 57 G no-go) |

The split is unmissable: **every exponent-fixing ingredient is native except one — the zero-mean centering — and that one the records structurally resist (§7). Every magnitude-fixing ingredient is imported.**

---

## 10. Open steps

- **[OPEN] The native centering** (§7): prove the `w`-mode fluctuation is sign-balanced and Λ-eligible, plus a CLT. Not no-go-barred; presently contradicted by the curl-free routing.
- **[OPEN] The manifoldlikeness gate** (field-shared, v7 Paper 11): the Poisson `Var[N] = E[N]` kinematics under the `−1/2` *number* assumes manifold-like sprinkling; Kleitman–Rothschild-dominated non-manifold-like orders would modify it. Orthogonal to the unimodular question, but a genuine premise under the exponent.
- **[OPEN] The equation-of-state conditionals** (Paper 57 §1.4): the Clausius→Einstein-form derivation that delivers the integration-constant fork carries three named, undischarged conditionals (axiom R fixing `β = 2π`; Jacobson's local-equilibrium `θ = σ = 0`; the continuum focusing gate). They gate Job (a), not the unimodular question.

---

## 11. Conclusion

The record substrate **reproduces the robust, falsifiable content of Sorkin's everpresent-Λ — the scaling `δΛ ∼ ±V^{−1/2}` (exponent exactly `−1/2`) — and classifies it**: the exponent is a weight-0, scale-no-go-*allowed* fact riding on the corpus's own Poisson seal statistics, reached identically by the conjugacy route and the corpus's own drift, with the intensive *sign* native (the universal `−ΛV` coupling, degree-0 in `V`) and unimodular gravity needed for neither the sign nor the structure. What the records do **not** give is Sorkin's zero-mean centering of the Λ-kick — and the reason is structural, the paper's substantive find: the corpus's curl-free routing sends the sign-balanced fluctuation to decoherence and leaves only the one-signed heating mean on Λ, so sign-balance and Λ-eligibility are mutually exclusive in its own construction, and the seal is one-signed at the foundation. The zero-mean centering (one packaging of which is unimodular gravity) is therefore an irreducible import with a named, not-no-go-barred open route to discharge. The absolute `10^{−120}` is Sorkin's numerology reproduced, not improved — and even there the *physical* `δΛ ∼ H²` needs only the cosmic size (the Planck length cancels); `G` enters solely the dimensionless Planck-units number, as a restated ratio, never as a prediction and orthogonal to the §7 obstruction. In one line: **the records give the everpresent *exponent* for free and grade it; they do not give the *centering* that fixes its value, and they say structurally why.**

---

*Receipts (all pass, mpmath dps = 120 / sympy-exact; the one Monte-Carlo slope per scaling receipt flagged numerical with its exact target):* `v7/code/p15a_routeA_conjugacy.py` (13), `p15b_routeB_drift_walk.py` (13), `p15c_weight_classification_nogo.py` (27), `p15d_desitter_selfconsistency.py` (18), `p15e_numerology.py` (14), `p15f_routeC_action_density.py` (23), `p15g_zero_mean_equivalence.py` (19). Total 127 checks.
