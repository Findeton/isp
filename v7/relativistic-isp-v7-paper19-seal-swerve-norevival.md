# The record click-law, XIX: the seal-swerve and the no-revival blindness — a testable (scale-gated) covariant momentum-diffusion and a mechanism-blind decoherence, the two experimental channels of the discrete-sealed substrate

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-17. Nineteenth paper of the v7 program; the empirical-channels entry. It asks the question Paper X left sharp — *is there any handle by which the discrete-sealed record substrate touches experiment?* — and answers it with a two-part **MIX**, each part honestly graded. **Channel A** (the **seal-swerve**) is a Lorentz-invariant covariant momentum-diffusion: **[TESTABLE]**, **[NOT-BLIND]** (continuum QFT has no such effect), but **[SCALE-GATED]** (its magnitude rides the imported `l_step`), so it *constrains* a record quantity rather than predicting a number — the SHARD analog of *Testing ER=EPR with Hydrogen* (Javed–Wilson-Ewing 2025). **Channel B** (the **no-revival** / CP-divisibility) is **[NO-GO/BLIND]**: seal-specific yet indistinguishable from standard quantum decoherence. Tags: **[TESTABLE]** = a falsifiable consequence; **[NOT-BLIND]** = distinguishes the discrete substrate from the continuum; **[SCALE-GATED]** = magnitude needs the imported `l_step`; **[NO-GO/BLIND]** = cannot discriminate SHARD from QM; **[INHERITED]** = a causal-set result the records carry; **[SHARD-SPECIFIC]** = the seal contribution. Structural/algebraic identities are sympy-exact; all numeric at mpmath `dps = 140`; bound translations are arithmetic at that precision and flagged. Receipts `v7/code/p19a_seal_swerve.py` (**23/23 checks pass**), `v7/code/p19b_norevival_blindness.py` (**22/22 checks pass**) — no float64 anywhere in the cancellation-sensitive paths.

## Scope — three guards, stated first [scope discipline]

Because "an experimental test of quantum gravity" invites overreach, the boundaries come before the results:

1. **Channel A constrains, it does not predict.** The seal-swerve's *existence* and *form* are forced; its *magnitude* `κ` is gated on the imported scale `l_step` (the program's standing scale no-go, Paper 57). So the deliverable is a **bound** on `σ·l_step⁻³`, not a number for `κ` or `σ`. Claiming a numerical prediction would violate the scale no-go.
2. **The swerve's existence is inherited, not invented.** The Lorentz-invariant momentum diffusion is the causal-set "swerves" of Dowker–Henson–Sorkin (2004) and Dowker–Philpott–Sorkin (2009). What is **SHARD-specific** is the *tie of the diffusion constant to the seal rate* `σ` (the structural relation `κ·l_step³/σ = 1/6`). The records carry the swerve because the records *are* the causal set (Paper 1); the seal-rate tie is the new content.
3. **Channel B is a negative result, stated plainly.** The no-revival discriminates SHARD only from revival-exhibiting (non-CP-divisible) collapse models, **never** from standard quantum mechanics. We do not dress the negative as a test.

Inside those guards, both channels are machine-verified.

---

## 1. Abstract

The discrete-sealed record substrate offers exactly two candidate experimental channels, on two different physical axes, with one common root (the records *are* the causal set, Paper 1).

**Channel A — the seal-swerve [TESTABLE / NOT-BLIND / SCALE-GATED].** A massive particle propagating through the substrate cannot keep a sharp momentum: the only Lorentz-invariant second-order diffusion on the mass shell is `∂f/∂τ = κ·Δ_{H_m} f` (uniqueness forced by probability conservation; receipt `p19a` check 1b), giving the **linear (leading short-τ) covariant heating** `⟨p²⟩(τ) = 2(d−1)κτ = 6κτ` (sympy-exact, `d−1=3`). This is the Dowker–Henson–Sorkin "swerve." SHARD ties the phenomenological constant to the **seal rate** `σ = D(P_{AB}‖P_{BA}) ≥ 0` (the arrow-of-time current, dimensionless seal-content per cell, weight-0): a worldline threads `1/l_step` cells per proper time, so it crosses `ν = σ/l_step` seal events per unit proper time, each a mean-zero momentum kick of variance `l_step⁻²`, giving `κ_swerve = (1/6)·σ·l_step⁻³`. The **relation** `κ·l_step³/σ = 1/6` is weight-0 (record-intrinsic, sympy-exact); the **magnitude** `κ` is length-weight `−3` (`= mass³`, matching its physical dimension), scale-gated by `l_step` — so the channel **constrains** `σ·l_step⁻³ = 6κ`, it does not predict it. Crucially it is **NOT mechanism-blind**: continuum QFT conserves free-particle momentum (`κ_continuum = 0`), so a covariant momentum-diffusion is a genuine **discrete-vs-continuum discriminator**, and existing swerve bounds give `σ·l_step⁻³ = 6κ < ~6×10⁻⁶¹ GeV³` (with `l_step = l_Planck`, `σ < ~3×10⁻¹¹⁸`, conditional on the import — comfortably consistent, a constraint not a prediction).

**Channel B — the no-revival [NO-GO / BLIND].** The seal is a state-independent irreversible commitment, `|ρ_{01}(t)| = exp(−∫₀ᵗ λ)`, `λ ≥ 0` (Paper 56 §3) — CP-divisible, monotone, **no revivals**, with the Gaussian onset `λ ~ t ⇒ |ρ_{01}| ~ exp(−κt²/2)`. We test exhaustively whether this can become a signature that escapes the Paper-X mechanism-blindness, and it cannot: the BLP/RHP non-Markovianity measure gives `N[seal] = N[QM-decoherence] = 0` while `N[revival-model] > 0` (receipt `p19b`, group 3). So the no-revival discriminates **only** against revival-exhibiting collapse models, never against standard QM (with which the seal shares an identical `|ρ_{01}(t)|` to all orders). **Verdict: `BLIND_NO_ESCAPE`.**

**Net.** The two channels live on different axes — the swerve is **geometric/kinematic** (momentum diffusion from covariant discreteness), the no-revival is **thermodynamic/open-system** (irreversible decoherence from the seal) — but share the discrete-sealed root. The **seal-swerve is the only channel that is both seal-specific *and* escapes the mechanism-blindness**; the no-revival is seal-specific but blind.

---

## 2. Two channels, one substrate

The records are a discrete causal set decorated by the seal dynamics (Paper 1; the seal entropy production `σ`, Paper 42). That one substrate radiates two *independent* observable consequences, on orthogonal axes:

- **The geometric/kinematic axis** — how a free particle *propagates* through the discreteness. Because the discreteness is covariant (no preferred frame; Bombelli–Henson–Sorkin), the only Lorentz-invariant effect on propagation is a diffusion of momentum on the mass shell. This is Channel A.
- **The thermodynamic/open-system axis** — how the seal's *irreversibility* destroys quantum coherence. The seal is an entropy-producing commitment (`σ ≥ 0`), so coherence decays monotonically. This is Channel B.

They are different physical quantities (momentum spread vs coherence decay), measured in different experiments (particle spectra/heating vs interferometric revival tests), and — as §5 shows — they differ decisively in whether they escape the Paper-X mechanism-blindness. The common root makes this one paper; the orthogonal axes make it a MIX.

---

## 3. Channel A — the seal-swerve [TESTABLE · NOT-BLIND · SCALE-GATED]

### 3.1 The unique Lorentz-invariant diffusion and the heating law [INHERITED — DHS/DPS]

A free particle of mass `m` lives on the mass hyperboloid `H_m = {p : p² = m², p⁰ > 0}`. A Markovian, Lorentz-invariant, second-order diffusion of its momentum is a Fokker–Planck equation whose generator must be built from Lorentz-invariant operators on `H_m`. The only invariant second-order generator is `a·Δ_{H_m} + b·𝟙`; probability conservation forces `b = 0` (receipt `p19a` check 1b, structural), leaving the **unique**

$$
\frac{\partial f}{\partial \tau}=\kappa\,\Delta_{H_m}f,
\qquad \kappa\ \text{the single swerve diffusion constant},\quad \tau\ \text{proper time}.
$$

(Dowker–Philpott–Sorkin 2009, Thm: a single phenomenological `κ`). In the rest frame the diffusion is, to leading short-proper-time order, isotropic over the `d−1 = 3` spatial momentum directions (the `H³` curvature is a higher-order correction near `χ=0`), giving the **heating law** (sympy-exact + `dps`-quadrature, check 1c)

$$
\langle p_i^2\rangle(\tau)=2\kappa\tau\ \text{per component},\qquad
\langle p^2\rangle(\tau)=2(d-1)\kappa\tau=6\kappa\tau
\quad\text{(leading short-}\tau\text{)}.
$$

**linear** in proper time (the `⟨p²⟩(2τ)/⟨p²⟩(τ) = 2.0` test confirms linearity). This is the slow covariant heating: a particle's momentum random-walks, isotropically and frame-independently, as it ploughs through the discreteness.

### 3.2 The seal-rate tie [SHARD-SPECIFIC]

In plain causal sets `κ` is a free Planck-suppressed constant. SHARD fixes its *structure*. The seal flux `σ = D(P_{AB}‖P_{BA}) ≥ 0` is the **dimensionless** seal entropy production per record cell (the arrow-of-time current; a KL divergence, weight-0, record-intrinsic). Specializing the DPS continuum-limit derivation to sealing: the worldline threads `1/l_step` record cells per unit proper time, each carrying seal-content `σ`, so it crosses `ν = σ/l_step` seal events per unit proper time, each contributing a mean-zero momentum kick of variance set by the cell scale `l_step⁻²`. Accumulating the kicks gives `⟨p²⟩(τ) = (σ·τ/l_step)·l_step⁻² = σ·l_step⁻³·τ`, hence

$$
\kappa_{\mathrm{swerve}}=\frac{1}{6}\sigma\,l_{\mathrm{step}}^{-3},
\qquad
\frac{\kappa\,l_{\mathrm{step}}^3}{\sigma}=\frac{1}{6}.
$$

So the *shape* of the prediction is record-native: the swerve constant is the seal rate measured in cell units.

### 3.3 Scale-gating — a constraint, not a prediction [SCALE-GATED]

The relation `κ·l_step³/σ = 1/6` is **weight-0** (record-intrinsic, `g_λ`-invariant). The **absolute** `κ` carries length-weight `−3` (= its physical dimension `mass³ = length⁻³`; the only dimensionful input is `l_step`), so it is scale-gated by the imported `l_step` — the standing scale no-go (Paper 57). Hence the deliverable is an **inequality**, not a number:

> existing swerve bounds ⇒ `σ·l_step⁻³ = 6κ < ~6×10⁻⁶¹ GeV³`

(receipt `p19a` check 5, arithmetic at `dps = 140`, flagged; with `l_step = l_Planck` this reads `σ < ~3×10⁻¹¹⁸`, conditional on the import, comfortably satisfied). We **constrain** `σ·l_step⁻³`; we do not predict `κ` or `σ` — exactly the move *Testing ER=EPR with Hydrogen* makes for the ER=EPR amplitude.

A caveat on the bound's reach: the quoted Kaloper–Mattingly limit `κ < 10⁻⁶¹ GeV³` is specifically the **relic-neutrino** bound (`m ~ 0.01 eV`). The seal-tie `κ = (1/6)σ·l_step⁻³` carries **no particle mass**, so it asserts a species-*universal* `κ`; applying the neutrino limit across all species therefore uses the single strongest available constraint, an extra (seal-tie-supplied) universality assumption that the bound alone does not establish. The species-independent molecular/cosmic-ray limits (DPS) corroborate more weakly; a mass-dependent `κ(m)` would relax the translation.

### 3.4 Why it is not mechanism-blind [NOT-BLIND]

Continuum QFT conserves a free particle's momentum: `κ_continuum = 0`. The swerve heating `⟨p²⟩ = 6κτ > 0` is therefore a genuine **discrete-substrate-vs-continuum discriminator** — a positive effect the continuum simply does not have. This is the property the gravitational-decoherence channel of Paper X *lacks* (there, sparse sealing and continuous classical noise are bit-identical). The swerve escapes that blindness by being a momentum-space, not a decoherence-channel, signature; the existing bounds (Kaloper–Mattingly; DPS) already constrain it.

---

## 4. Channel B — the no-revival / CP-divisibility [NO-GO / BLIND]

### 4.1 The seal is CP-divisible, monotone, revival-free [SHARD-SPECIFIC]

The seal is a state-independent irreversible commitment: the off-diagonal coherence obeys

$$
|\rho_{01}(t)|=\exp\!\left(-\int_0^t \lambda(s)\,ds\right),
\qquad \lambda(s)\ge 0.
$$

hence **CP-divisible**, **monotone non-increasing**, with **no revivals**, and the Gaussian onset `λ ~ t ⇒ |ρ_{01}| ~ exp(−κt²/2)` near `t = 0` (Paper X). CP-divisibility is incompatible with Barandes-indivisibility — a genuine structural fingerprint of the seal.

### 4.2 The escape attempt fails — `N[seal] = N[QM] = 0` [BLIND]

We test whether this fingerprint is *measurable* against standard QM. Build three dynamics: (i) the seal; (ii) standard QM with ordinary CP-divisible environmental decoherence; (iii) a non-Markovian, revival-exhibiting collapse model (`λ` dips negative ⇒ coherence partially revives). The BLP/RHP non-Markovianity measure `N` (receipt `p19b`, group 3) gives

$$
N[\mathrm{seal}]=N[\mathrm{QM\text{-}decoherence}]=0,
\qquad
N[\mathrm{revival\text{-}model}]>0.
$$

Higher-order/multi-time probes and the specific `λ(t)` shape were checked: a seal and a generic CP-divisible noise with the same `|ρ_{01}(t)|` are **identical to all orders** — Paper X's onset-blindness extends to the whole CP-divisible class. **Verdict: `BLIND_NO_ESCAPE`.**

A note on the inference direction (the computed model is a pure-dephasing qubit): we certify CP-divisibility *directly* from `λ(s) ≥ 0` (the time-local dephasing rate), which gives `N_BLP = N_RHP = 0`. We do **not** invoke the converse `N_BLP = 0 ⇒ CP-divisible`, which is false in general — *eternal-non-Markovian* dynamics are non-CP-divisible yet exhibit no BLP information backflow. The RHP measure, which tests CP-divisibility itself, is the one that certifies it here; for this dephasing family the BLP, RHP, and CP-divisibility lines coincide.

### 4.3 The precise discrimination boundary

The boundary is the **CP-divisibility line** itself (for this pure-dephasing family, where it coincides with the BLP/RHP `N=0` line):

- **[BLIND]** SHARD seal **vs** standard-QM CP-divisible decoherence → **indistinguishable** (`N = 0` both; identical `|ρ_{01}|` to all orders; no escape).
- **[NOT-BLIND]** SHARD seal / QM-decoherence **vs** revival-exhibiting (non-CP-divisible) collapse models (`N > 0`) → **discriminated**.

So the no-revival is **SHARD-specific** (a seal *is* CP-divisible) but **blind versus QM** — it can only rule out a specific exotic class (revival collapse), never separate SHARD from "nothing unusual." It is a seal-specific property with no SHARD-vs-QM discriminating power.

---

## 5. Comparison — why the swerve escapes blindness and the no-revival does not

The two channels both originate in the seal, but their relationship to the Paper-X mechanism-blindness is opposite, and for a clean structural reason:

| | Channel A — seal-swerve | Channel B — no-revival |
|---|---|---|
| Axis | geometric / kinematic (momentum) | thermodynamic / open-system (coherence) |
| Effect | covariant momentum diffusion `⟨p²⟩=6κτ` | monotone decoherence `|ρ_{01}|=e^{−∫λ}` |
| Continuum value | `κ=0` (momentum conserved) — **effect absent** | CP-divisible decoherence **also present** in QM |
| Discriminates vs continuum/QM? | **YES** (positive effect QFT lacks) | **NO** (QM gives the same) |
| Seal-specific? | tie `κ∝σ` is | yes (`λ≥0` is the seal) |
| Magnitude | scale-gated (imported `l_step`) | scale-gated (the rate) |
| Net | **TESTABLE / NOT-BLIND / SCALE-GATED** | **BLIND** (discriminates only revival models) |

The decisive difference: the swerve predicts something the continuum/QM **does not have** (a momentum diffusion), so its mere *presence* is informative; the no-revival predicts something the continuum/QM **also has** (monotone decoherence), so its presence is uninformative. The seal-swerve is therefore the **only** channel that is *both* seal-specific *and* escapes the mechanism-blindness — by being a momentum-space signature rather than a decoherence-channel one.

---

## 6. Honest scope

| Ingredient | Status |
|---|---|
| The swerve (LI momentum diffusion exists) | `INHERITED` (Dowker–Henson–Sorkin; DPS) |
| The seal-rate tie `κ = (1/6)σ·l_step⁻³`, relation weight-0 | `SHARD-SPECIFIC` |
| The swerve *magnitude* `κ` | `SCALE-GATED` (imported `l_step`, Paper 57 wall) |
| The swerve is a discrete-vs-continuum discriminator | `NOT-BLIND` `TESTABLE` (constrains `σ·l_step⁻³`) |
| Numerical prediction of `κ` or `σ` | **not claimed** — the deliverable is a bound |
| The seal is CP-divisible / no revivals | `SHARD-SPECIFIC` (Paper 56) |
| The no-revival vs standard QM | `NO-GO / BLIND` (`N=0` both) |
| The no-revival vs revival collapse models | `NOT-BLIND` (the only thing it discriminates) |

Open: the swerve coefficient's `O(1)` constant and the absolute bound both ride the imported scale; tightening the experimental swerve bound tightens the constraint on `σ·l_step⁻³` but never converts it to a prediction without the scale import. The no-revival has no open route to a SHARD-vs-QM signature (the blindness is structural, not unbuilt).

---

## 7. Conclusion

The discrete-sealed record substrate touches experiment through exactly two channels, and they fall on opposite sides of the Paper-X mechanism-blindness for a clean reason. The **seal-swerve** is a genuine, falsifiable, *not-blind* signature — a Lorentz-invariant covariant momentum-diffusion whose constant is the seal rate in cell units (`κ·l_step³/σ = 1/6`, weight-0), whose *magnitude* is scale-gated, and which therefore **constrains** `σ·l_step⁻³ = 6κ < ~6×10⁻⁶¹ GeV³` against existing heating/cosmic-ray bounds. That is the closest SHARD analog of *Testing ER=EPR with Hydrogen*: a structural claim turned into a precision constraint on an amplitude. The **no-revival** is the honest negative — a real seal fingerprint (CP-divisibility) that is provably **blind** versus standard QM (`N[seal]=N[QM]=0`, identical `|ρ_{01}|` to all orders), discriminating only the revival-exhibiting collapse class. In one line: **the records give one testable-but-scale-gated channel and one blind channel; the seal-swerve is the only place the seal both shows itself *and* escapes mechanism-blindness — a constraint on the world, not a number, exactly as the scale no-go demands.**

---

*Receipts (all pass, sympy-exact structure / mpmath `dps = 140`, no float64 in cancellation-sensitive paths):* `v7/code/p19a_seal_swerve.py` (23/23 — unique LI diffusion, heating `⟨p²⟩=6κτ`, the seal tie `κ=(1/6)σ·l_step⁻³`, the weight-0 relation, the not-blind discriminator, the bound `σ·l_step⁻³<~6×10⁻⁶¹ GeV³`), `v7/code/p19b_norevival_blindness.py` (22/22 — CP-divisible monotone no-revival, the Gaussian onset, `N[seal]=N[QM]=0 < N[revival]`, the `BLIND_NO_ESCAPE` verdict and the CP-divisibility discrimination boundary).

## References

**Companion (this program).**
- *The record click-law, I* (v7) and *v6 Paper 1* — the records are the causal set; the discrete substrate.
- *The record click-law / v6 Paper 42* — the seal entropy production `σ = D(P_{AB}‖P_{BA})`, the arrow-of-time current.
- *The record click-law / v6 Paper 56* — the indivisible gravitational channel: `|ρ_{01}| = exp(−∫λ)`, `λ ≥ 0`, CP-divisible, no revivals.
- *v6 Paper X (gravitational decoherence)* — the Gaussian onset and its mechanism-blindness (sealing ≡ continuous classical noise to all orders).
- *The record click-law, XVII* (v7) — the scale `l_step` import wall the swerve magnitude rides; *Paper 57* — the scale no-go.

**External.**
- F. Dowker, J. Henson, R. D. Sorkin, *Quantum gravity phenomenology, Lorentz invariance and discreteness*, Mod. Phys. Lett. A **19**, 1829 (2004) — the swerves.
- F. Dowker, L. Philpott, R. D. Sorkin, *Energy-momentum diffusion from spacetime discreteness*, Phys. Rev. D **79**, 124047 (2009) — the unique Lorentz-invariant momentum-diffusion Fokker–Planck and its single constant `κ`.
- N. Kaloper, D. Mattingly, *Low energy bounds on Poincaré violation in causal set theory*, Phys. Rev. D **74**, 106001 (2006) — bounds on the swerve diffusion constant.
- H.-P. Breuer, E.-M. Laine, J. Piilo (BLP) and Á. Rivas, S. F. Huelga, M. B. Plenio (RHP) — the non-Markovianity measures `N` distinguishing CP-divisible (no-revival) from revival-exhibiting dynamics.
- I. Javed, E. Wilson-Ewing, *Testing ER = EPR with Hydrogen*, arXiv:2512.02156 (2025) — the template: a structural quantum-gravity claim turned into a precision constraint on an amplitude.
- M. Carlesso et al. / Gran Sasso (2021) — X-ray bounds ruling out the parameter-free Diósi–Penrose collapse rate, constraining the decoherence channel.
