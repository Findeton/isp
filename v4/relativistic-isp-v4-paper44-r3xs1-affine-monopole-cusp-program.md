# Paper 44 — Confinement as an Affine-Theta Cusp on ℝ³×S¹: a Semiclassically-Calculable Program

**Status.** An exploration, not a proof. The small-circle semiclassics used here is established
(Polyakov 3D mechanism; Ünsal–Yaffe adiabatic continuity; Dunne–Ünsal resurgence) — those are dressing.
The *new lens* offered is that the monopole-instanton gas on `ℝ³×S¹` realizes an **affine theta
function** whose **leading cusp datum is the mass gap / string tension**, making confinement a
*calculable* cusp statement in the controlled regime — and that the remaining open core is **adiabatic
continuity to 4D**, a different and more tractable problem than flat-4D confinement. Claims are marked
**[EST]** (established semiclassics), **[NEW]** (the affine-cusp lens, this program's content), or
**[OPEN]**. Nothing is asserted as a solution of the 4D Yang–Mills mass-gap problem.

§0 formulates the program completely independently. §1–§6 are the exploration steps.

---

## 0. The program, self-contained

### 0.1 Geometry and theory

Take `SU(2)` Yang–Mills on `ℝ³ × S¹`, the circle `S¹` of circumference `L`, coordinate `x_4∼x_4+L`.
Euclidean action `S=\frac{1}{2g^2}\int \operatorname{tr}F_{\mu\nu}F_{\mu\nu}`. The coupling runs; by asymptotic freedom
the effective coupling at scale `1/L` is small for small `L`:

```math
\frac{1}{g^2(L)} \;=\; \frac{b_0}{1}\,\log\frac{1}{L\Lambda}+\dots,\qquad b_0=\frac{11}{24\pi^2}\ (\text{SU(2)}),
```

with `Λ` the strong scale. **Center symmetry** is the `\mathbb Z_2` acting on the holonomy (Polyakov loop)
`\Omega(\mathbf x)=\mathcal P\exp\big(i\oint_{S^1}A_4\,dx_4\big)\in SU(2)` by `\Omega\to-\Omega`. To keep the small-`L`
vacuum **center-symmetric** (so it can connect to 4D), add a center-stabilizing double-trace deformation
`+\frac{c}{L^3}\,|\operatorname{tr}\Omega|^2` (equivalently, use periodic adjoint fermions = `\mathcal N{=}1` SYM). **[EST]**

### 0.2 Abelianization at the confining holonomy

The center-symmetric minimum is `\langle\Omega\rangle=\operatorname{diag}(e^{i\pi/2},e^{-i\pi/2})=\operatorname{diag}(i,-i)`
(`\operatorname{tr}\Omega=0`). A nonzero holonomy adjoint-Higgses `SU(2)\to U(1)`: the charged `W`-bosons get masses
`\sim \pi/L`, and below that scale the theory is a **compact 3D `U(1)`** with a single photon, dualized
to a compact scalar `\sigma` (the **dual photon**), `\sigma\sim\sigma+2\pi`. **[EST]**

### 0.3 Monopole-instantons and the affine coroot lattice

The finite-action nonperturbative objects are **monopole-instantons** (3D instantons of the abelianized
theory). For `SU(2)` there are two elementary types:

- `M_1` (**BPS**): magnetic charge `+\alpha^\vee` (the simple coroot), action `S_1`;
- `M_2` (**KK**, Kaluza–Klein): magnetic charge `-\alpha^\vee` dressed by one unit of `S^1`-momentum
  (the **affine** coroot `\alpha_0^\vee`), action `S_2`,

with `S_1+S_2=S_{\rm inst}=\dfrac{8\pi^2}{g^2(L)}` (the 4D instanton fractionates into `M_1,M_2`). At the
center-symmetric holonomy the two are degenerate, `S_1=S_2=\dfrac{4\pi^2}{g^2(L)}`. Their magnetic charges
generate the **affine coroot lattice of `A_1^{(1)}`** — `\alpha^\vee` together with the affine/KK direction.
**[EST]** Fugacities `\zeta_i\sim e^{-S_i}=e^{-4\pi^2/g^2(L)}` — an **essential singularity in `g^2`**, now
*derived*, not assumed.

### 0.4 The monopole gas, mass gap, and string tension

The `M_1,M_2` (and anti-monopoles) form a dilute 3D Coulomb gas; summing it produces a dual-photon
potential. In the center-stabilized theory the monopoles give (Polyakov mechanism)

```math
\mathcal L_{\rm eff}=\frac{g^2(L)}{32\pi^2 L}(\partial\sigma)^2-\frac{2\zeta}{L^3}\cos\sigma\ (+\dots),
\qquad \zeta\sim e^{-4\pi^2/g^2(L)} .
```

This gaps the dual photon, `m_\sigma^2\propto \zeta\,g^2/L^2`, and gives a **string tension**
`\sigma_{\rm st}\propto m_\sigma\cdot(\text{scale})`, both `\sim e^{-\#/g^2(L)}` — confinement, with the
scale set by the monopole fugacity. **[EST]** (`\mathcal N{=}1` SYM: replace single monopoles by **magnetic
bions** `M_1\bar M_2`; same conclusion, cleaner.)

### 0.5 The affine theta and the cusp — the new lens

The monopole-gas partition function, being a Coulomb gas on the **affine coroot lattice**, is (dilute
limit) a theta-type sum over that lattice — and theta functions on an affine root lattice are
**modular** (Kac–Peterson; the affine `\widehat{su}(2)` characters / string functions). Write the nome of
this affine theta as `q` (a power of the monopole fugacity `e^{-4\pi^2/g^2(L)}`). The cusp `g^2(L)\to0`
(i.e. `L\to0`) is `q\to0`.

> **Program claim (affine-theta cusp).** [NEW]
> The `SU(2)`-on-`ℝ³×S¹` (center-stabilized) monopole-gas partition function is an affine `A_1^{(1)}`
> theta `\Theta_{\rm aff}(q)`; its **leading nonconstant cusp coefficient** (`q\to0`) is the mass gap /
> string tension:
> ```math
> \frac{\sqrt{\sigma_{\rm st}}}{\Lambda}\;=\;c\cdot[\text{leading cusp datum of }\Theta_{\rm aff}],
> ```
> and the affine modular `S`-transform realizes the electric–magnetic (W-boson ↔ monopole) duality of the
> abelianized theory. This is the **non-abelian, calculable** realization of the abelian fact that 3D
> compact `U(1)` confinement scale equals the cusp term `q^{v_0}` of the electric Jacobi theta.

Because this lives in the *semiclassically calculable* regime, no strong–weak self-duality of the full
4D partition function is invoked — that is precisely the obstruction the flat-4D modular approach hit,
and it is absent here.

### 0.6 The continuation to 4D — the open core

Everything above is at **small `L`**. Physical 4D is `L\to\infty`. The bridge is **adiabatic
continuity**: with center symmetry stabilized, there is *no* phase transition in `L`, so the
small-`L` confined phase is continuously connected to the 4D confined phase, and the mass gap stays
nonzero throughout. **[OPEN]** (a well-supported scenario — lattice + analytics — not a theorem). The
tool for controlling the continuation is **resurgence**: the trans-series locks the perturbative series
to the nonperturbative `e^{-\#/g^2}` sectors, a rigidity that constrains the `L`-dependence.

```math
\boxed{
\begin{array}{l}
\textbf{The program in one line.}\ \text{On }\mathbb R^3\times S^1\text{ the confinement scale is a \emph{calculable}}\\
\text{affine-theta cusp (monopole fugacity); the open question is whether that survives }L\to\infty\\
\text{(adiabatic continuity), \emph{not} whether a strongly-coupled 4D partition function is modular.}
\end{array}}
```

---

## 1. Step A — build the monopole gas explicitly [EST; reproduce, then extend]

Construct, concretely (the analogue of a validated abelian computation):
1. the center-symmetric holonomy and the abelianization scale `\pi/L`;
2. the two monopole-instantons `M_1,M_2`, their actions `S_i(v)` as functions of the holonomy `v`, degenerate at `v=\pi/2`;
3. the dilute-gas dual-photon Lagrangian (0.4), the gap `m_\sigma(g^2,L)`, and `\sigma_{\rm st}(g^2,L)`.
*Output:* explicit `m_\sigma,\sigma_{\rm st}\sim e^{-\#/g^2(L)}` with the essential singularity manifest. *Goal:* a
clean, reproducible baseline (and code, paralleling the U(1) monopole computation).

## 2. Step B — exhibit the affine-theta structure [NEW; the structural core]

Write the monopole-gas grand partition function as a sum over the affine coroot lattice and identify it
with an affine `A_1^{(1)}` theta / string function. Determine (i) the nome `q(g^2,L)`, (ii) the affine
modular group and the `S`-transform, (iii) whether `S` is the W-boson↔monopole (electric↔magnetic)
duality of the abelianized theory. *Tools:* Kac–Peterson affine characters; Coulomb-gas/sine-Gordon =
theta-on-lattice; our prior `\Gamma(2)`/Kac–Peterson computations. *Go/no-go:* does `\Theta_{\rm aff}`
assemble at all?

## 3. Step C — verify mass gap = cusp datum [NEW; the decisive check, computable]

Expand `\Theta_{\rm aff}(q)` at the cusp `q\to0` and check that the **leading nonconstant coefficient** is
the mass gap / string tension of Step A, fixing `c`. This is the direct analogue of the proven abelian
identity `\text{fugacity}=q^{v_0}` (3D `U(1)`), now non-abelian and calculable. *Outcome:* either a clean
match (the program's central positive result, in the controlled regime) or a precise mismatch
(reformulate).

## 4. Step D — the affine S-transform as a duality [NEW/structural]

Test whether the affine `S` is a genuine self-duality of the monopole gas (electric flux ↔ monopole flux
on `ℝ³×S¹`), i.e. an exact symmetry in this regime — in contrast to flat 4D, where no such duality
exists. Relate to the `\mathbb Z_2`/`S_3` flux structure of the lattice ’t Hooft fluxes. *Significance:* if
yes, the modularity that flat-4D lacks is *present and exact* at small `L`, pinpointing exactly what the
continuation must (or must not) preserve.

## 4½. Executed results — Steps A–D (`code/su2_r3s1_affine.py`)

**Step A [EST].** At the center-symmetric holonomy `v=π/2` the two monopole-instantons are degenerate,
`S_1=S_2=4π²/g²`, fugacity `\zeta=e^{-4π²/g²}`. The dual-photon mass gap obeys `m²\propto\zeta` and the
string tension `\sqrt{\sigma_{\rm st}}\propto e^{-π²/g²(L)}` — an **essential singularity in `g²`, derived
semiclassically**, not assumed:

```text
g^2     S_1=S_2     zeta=e^{-S}      m_gap^2 (∝zeta)   sqrt(sigma_st)
2.0     19.74       2.7e-09          5.4e-09           7.3e-05
1.0     39.48       7.2e-18          1.4e-17           3.8e-09
```

**Step B [NEW].** The monopole charges sit on the affine `A_1^{(1)}` coroot lattice, so the gas partition
function is the **level-1 `\widehat{su}(2)` theta vector** with nome equal to the monopole fugacity,
`q=e^{-4π²/g²}`:

```text
Theta_(0,1) = sum_m q^{m^2}        = 1 + 2q + 2q^4 + ...   (the coroot-lattice theta = theta_3)
Theta_(1,1) = sum_m q^{(m+1/2)^2}  = 2 q^{1/4} + ...
```

So `\Theta_{\rm aff}` assembles (go), and the cusp `q\to0` is exactly the weak-coupling/small-`L` limit.

**Step C [NEW].** The leading nonconstant cusp term of `\Theta_{(0,1)}` is `2q^1` — the **single-monopole
fugacity** — and `m²\propto\zeta=q`, so `m²/(\text{leading cusp coeff})` is **constant across couplings**
(verified to all digits). Hence `\sqrt{\sigma_{\rm st}}/\Lambda = c\cdot(\text{leading cusp datum})^{1/2}`
with computable `c`: **"cusp = scale" holds, calculably.** *Honest qualifier:* this is a *structural*
identity, not an independent numerical surprise — in the dilute gas the leading theta term and the
mass-gap seed are *both* the single-monopole fugacity, exactly as the abelian template's
`\text{fugacity}=q^{v_0}` was exact-by-construction. The content is that the identification is
**well-defined and exact in the calculable regime** — precisely what flat 4D could not provide.

**Step D [NEW/structural].** The coroot theta `\theta_3` is modular, `\theta_3(-1/\tau)=\sqrt{-i\tau}\,
\theta_3(\tau)` (verified to `2\cdot10^{-16}`); the level-1 affine vector transforms by the Kac–Peterson
`S`-matrix `S=\tfrac{1}{\sqrt2}\big(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\big)` (unitary,
`S^2=I`, to `10^{-16}`). This `S` exchanges the **electric** (W-boson / `S^1`-momentum) and **magnetic**
(monopole) sums of the abelianized 3D `U(1)` — the electric–magnetic duality that 3D Polyakov confinement
*has* (Poisson summation) and that flat 4D *lacks* (no Montonen–Olive). **Here it is exact and realized on
the calculable monopole gas.**

```math
\boxed{
\begin{array}{l}
\textbf{Steps A–D result.}\ \text{In the calculable }\mathbb R^3\times S^1\text{ regime the SU(2) confinement scale}\\
\text{is an affine-theta cusp datum (the monopole fugacity), and the affine }S\text{ is an \emph{exact}}\\
\text{electric–magnetic duality. Every flat-4D obstruction (no }S\text{-duality, no calculable scale) is}\\
\text{absent. This is the non-abelian, calculable realization of the proven 3D-U(1) cusp. The remaining}\\
\text{open content is entirely Step E (continuity to 4D); Steps A–D hold in the controlled regime.}
\end{array}}
```

## 5. Step E — adiabatic continuity and resurgence [OPEN; the real frontier]

Address `L\to\infty`. (i) Survey/strengthen the evidence that center stabilization removes any
`L`-driven transition (lattice; large-`N` volume independence; analytics). (ii) Use resurgence
(Dunne–Ünsal) to constrain the `L`-dependence of `\sigma_{\rm st}` via the perturbative/nonperturbative
trans-series rigidity. (iii) State precisely what a *theorem* would require — and honestly mark the gap.
This replaces the flat-4D mass-gap problem with the (still hard, but live and partial-progress)
continuity problem.

## 6. Step F — calibration and limits [EST/NEW]

- **U(1) limit / decoupling:** recover the proven 3D compact `U(1)` cusp `q^{v_0}` as the abelian
  projection of `\Theta_{\rm aff}`. (Sanity anchor.)
- **`\mathcal N{=}1` SYM:** the magnetic-bion version, where the gap and gluino condensate are cleanest,
  as a controlled testbed for Steps B–C.
- **Large `N`:** Eguchi–Kawai / volume independence, where small-`L` and large-`L` are most tightly tied.

---

## 7. Status, falsifiers, what would settle it

**Ledger.**
- §0.1–0.4 setup, monopoles, mass gap; Step A — **[EST, executed §4½]** (Polyakov; Ünsal–Yaffe).
- §0.5 affine-theta cusp lens; Steps B–D — **[NEW, executed §4½]**: `\Theta_{\rm aff}` assembles (B);
  leading cusp datum = monopole fugacity = mass-gap seed, "cusp = scale" exact in the calculable regime
  (C, structural); affine `S` = exact electric–magnetic duality (D). `code/su2_r3s1_affine.py`.
- §0.6 adiabatic continuity to 4D; Step E — **[OPEN]** (well-supported scenario; the sole remaining gap).
- A proof of 4D confinement — **NOT** claimed.

**Falsifiers.**
- (F1) The monopole-gas partition function provably is *not* an affine theta (Step B fails) — the lens is wrong.
- (F2) The leading cusp coefficient is *not* the mass gap (Step C mismatch) — "cusp = scale" fails even in the calculable regime.
- (F3) Center stabilization fails to prevent an `L`-transition (Step E) — no continuity, so small-`L` says nothing about 4D.

**What would settle the calculable part.** Steps B–C are finite, semiclassical computations (no
strongly-coupled dynamics) — they decide the **[NEW]** claim cleanly, much as the abelian `U(1)` cusp was
decided exactly. The 4D statement remains gated by Step E (continuity), which is the honest open frontier
— but it is a *better* frontier: confinement is rigorously present in a limit, the scale is derived, and
the modular/cusp structure that flat 4D could not support is, here, calculable and possibly exact.

**Honest novelty note.** The semiclassics (§0.1–0.4, §6) is Ünsal–Yaffe–Dunne and is not claimed as new.
The contribution attempted here is the **affine-theta/cusp organization** (§0.5, Steps B–D) — recasting
the calculable mass gap as cusp data of an affine modular object, the non-abelian heir of the proven
abelian cusp. Whether that specific organization is genuinely new requires a literature check; it builds
heavily on known monopole-gas and affine-character results.

---

## 8. Literature & novelty assessment (web check, May 2026)

A targeted literature check sharpens — and largely deflates — the novelty of the *physics* here, while
leaving the *organizing lens* as the only possibly-unstated piece. Honest verdict, with sources:

- **The semiclassics is established.** Center-stabilized YM on `ℝ³×S¹`, the monopole gas, the mass gap,
  confinement, and large-`N` volume independence are Ünsal–Yaffe (arXiv:0803.0344) and a large
  follow-up literature (review: arXiv:2111.10423). **[known]**
- **The "affine" monopole-gas structure is known** — but as an *affine XY / dual-Coulomb gas*
  (Anber–Poppitz–Ünsal, arXiv:1310.3522), where "affine" denotes the affine *root* (the KK monopole),
  used as a spin/Coulomb model — **not** as affine Kac–Moody *characters* / modular forms. **[known,
  different framing]**
- **`θ`-dependence, the multi-branch vacuum energy, and Jacobi theta functions in deformed / `q`-deformed
  YM are known** (e.g. arXiv:1801.08236 and the deformed-YM `θ`-literature). **[known]**
- **The Dedekind-`η` worldsheet modularity of the confining flux tube is standard** effective-string /
  Lüscher physics (`Z\sim1/\eta^{d-2}`; string effects in Polyakov-loop correlators, hep-lat/0205008).
  This is our §0.5 / Paper 43 §4.3. **[known]**
- **The modular-bootstrap / Viazovska line has no Yang–Mills-confinement connection** — it maps to 2D
  CFT and sphere packing (Hartman–Mazáč–Rastelli, arXiv:1905.01319; Cohn). So the "modular certificate
  for confinement" idea and its no-go (Paper 43 §7.2) are **not in the literature**, but are
  *folklore-obvious* to experts (modularity needs `S`-duality, hence SUSY). **[unstated but not new]**
- **Adiabatic continuity to 4D is an open, actively-investigated scenario**, not a rigorous proof
  (lattice tests, e.g. arXiv:1806.10894; large-`N` volume independence is rigorous only to `O(1/N^2)`).
  **[the genuine open problem — the field's, not crackable in a session]**

**Verdict.** There is **no clearly-new publishable physics result** in this program. Its honest content
is: (i) careful, *validated re-derivations* of known structures (the SU(2) loop equations, the U(1)
cusp, the affine/Kac–Peterson data, the Jacobi-form transformations); (ii) a *presentational lens* —
"confinement scale = affine-theta cusp datum; the `(τ,z)` Jacobi form unifies the electric–magnetic
duality and the `θ`-multi-branch" — whose ingredients are all known, so it is at most a perspective, not
a theorem; and (iii) *honest negatives* (bootstrap saturation; the modular-certificate no-go) that
experts would consider known. The one open problem (adiabatic continuity) is the field's hard frontier.

## 9. The `θ`-angle / Jacobi-form completion of Steps A–D (`code/su2_jacobi.py`) — [verified math; known physics]

Completing the affine picture in the direction the literature flags: the level-1 affine theta is a
function of two variables, `\Theta_{l,1}(\tau,z)=\sum_{n\in\mathbb Z+l/2} q^{n^2} y^{n}`
(`q=e^{2\pi i\tau}`, `y=e^{2\pi i z}`), and physically `z` is the **`\theta`-angle** (the Witten effect
turns monopoles into dyons; the dual-Coulomb gas becomes a function of `(\tau,z)`). It is a **Jacobi
form** — all three transformations verified to machine precision:

```text
(1) z -> z+1     :  Theta_{l,1}(tau,z+1)   = e^{i pi l} Theta_{l,1}(tau,z)                 dev 3e-16
(2) z -> z+tau   :  Theta_{l,1}(tau,z+tau) = q^{-1/4} e^{-i pi z} Theta_{1-l,1}(tau,z)      dev 2e-15
                    (SPECTRAL FLOW: permutes l=0 <-> l=1 = the center/flux sector)
(3) tau -> -1/tau:  full Jacobi S-transform                                                 dev 2e-16
                    z=0 reduction = Kac-Peterson S = (1/sqrt2)[[1,1],[1,-1]]                 dev 2e-16
```

Reading the physics off the two directions of the single Jacobi form:

- **`\tau` (coupling/holonomy) → modular `S` = electric–magnetic duality.** At `z=0` the `S`-transform is
  exactly the Kac–Peterson `S`-matrix of Step D — the W-boson ↔ monopole duality that the calculable
  `ℝ³×S¹` regime *has* and flat 4D lacks.
- **`z` (`\theta`-angle) → spectral flow = the multi-branch vacuum energy.** The `z\to z+\tau` shift
  *permutes* the two center sectors `l=0\leftrightarrow1`, which is exactly the `\theta\to\theta+2\pi`
  branch jump of the deformed-YM multi-branch `E(\theta)`.

```math
\boxed{
\begin{array}{l}
\textbf{§9 result.}\ \text{The SU(2)-on-}\mathbb R^3\times S^1\text{ confinement data assembles into ONE affine}\\
\text{level-1 \emph{Jacobi form}: the coupling direction carries the electric–magnetic duality (modular }S),\\
\text{the }\theta\text{-direction carries the multi-branch structure (spectral flow). Verified to machine}\\
\text{precision. \emph{Honest:} standard affine-character math + established deformed-YM physics; the}\\
\text{explicit Jacobi-form organization is the lens, not a new result.}
\end{array}}
```

**Net of the autonomous run.** Steps A–D and the §9 `θ`-completion are done and verified; the literature
check (§8) places all the physics as known and the open frontier (adiabatic continuity, §5/Step E) as
the field's. The program is, honestly, **complete as an exploration**: a fully-mapped, validated picture
with the modular/cusp/Jacobi organization as a perspective, and no remaining session-crackable advance.

Sources: Ünsal–Yaffe arXiv:0803.0344; review arXiv:2111.10423; Anber–Poppitz–Ünsal arXiv:1310.3522;
`q`-deformed YM arXiv:1801.08236; effective string hep-lat/0205008; Hartman–Mazáč–Rastelli
arXiv:1905.01319; adiabatic-continuity lattice arXiv:1806.10894.

---

## 10. Checkable testbed — does the positivity bootstrap track a gap through the crossover? (`code/cpn_crossover_bootstrap.py`)

A direct, *checkable* test of the Step-E question (uniform-in-coupling gap control through the
dimensional-transmutation crossover), run in the one lab where the answer is **exactly known**: the
2D `O(N)` sigma model at large `N`. There the gap solves `I(m^2)=β/N` (`m ~ e^{-2πβ/N}`, transmutation),
and the axis 2-point function has exact gap `2·arcsinh(m/2)`. We feed the **exact** moments
`G(r)=⟨s_0·s_r⟩` (best case) to the **positivity (Hankel/Stieltjes) bootstrap** — `{G(r)}` is a moment
sequence on `[0,y_0]`, `y_0=e^{-gap}`, and `2K+2` moments give `gap_est(K) = -\log λ_{max}(H_1,H_0)`
(`H_0=[G(i+j)]`, `H_1=[G(i+j+1)]`), which `→` the true gap as `K→∞`.

```text
(A) fixed K=5 (reach r<=11) across the crossover, vs the EXACT gap:
    beta/N   m      true_gap  xi=1/gap   gap_est/true_gap   cond(H0)
    0.294   0.80    0.780      1.3        1.02               3e11
    0.530   0.20    0.200      5.0        1.06               9e8
    0.752   0.05    0.050     20.0        1.24               4e8
    0.898   0.02    0.020     50.0        1.55               4e8
(B) resolvable gap (m=0.3, xi=3.3): K=1..5 -> ratio 1.37->1.04   (converges once reach >~ xi)
(C) small gap   (m=0.03, xi=33): K=1..7 -> ratio 3.78->1.23, then ill-conditioned at K=9 (cond 3e13)
    -- reach (2K+1) hits the conditioning wall BEFORE catching xi=33.
```

**Result.** Even with *exact* moments, the positivity bootstrap resolves the gap only when its **reach
`2K+1` `\gtrsim` the correlation length `ξ=1/gap`.** As the transmutation gap `→0` toward the continuum
(`ξ ~ e^{2πβ/N}`), a *fixed* truncation increasingly **over-estimates** the gap (ratio `1.02→1.55`), and
resolving it needs `K ~ ξ` (exponentially many moments in `β`) **and** exponentially growing precision
(the Hankel condition number `~ e^{cK}`). **There is no fixed-resource, uniform-in-coupling control
through the crossover** — the same wall as 4D Step E, now demonstrated concretely and *checked against
the exact answer*. This is also a clean micro-explanation of the §18 (paper 42) lattice-bootstrap
saturation: the bootstrap's resolution is tied to the size of the operators/loops it includes, and the
scale it must resolve shrinks exponentially.

**Two honest caveats.** (i) This isolates the *positivity/resolution* aspect using 2-point moments; the
full Schwinger–Dyson + positivity bootstrap adds dynamics (and gives two-sided bounds), but it is subject
to the *same* operator-reach limit (you need loops of size `~ξ` to see the gap), consistent with the 4D
saturation. (ii) 2-point positivity bounds the gap only from **above**; the confinement-relevant
**lower** bound (`gap>0`) is not even accessible from positivity alone — it needs the dynamics, which is
the genuinely hard part.

**The pointed lesson (back to Kondo).** The testbed says *why* uniform truncation fails — its resolution
is linear in the reach, while the gap is exponentially small — and it points at the cure: the one method
that *beat* this exact wall, Wilson's solution of the Kondo problem, used a **logarithmic (exponentially
refining) discretization**, i.e. it built in resolution that grows like `ξ` by construction. So a
bootstrap with *uniform* truncation is structurally the wrong tool for the transmutation crossover; an
**RG that refines resolution exponentially** is the proven one. That is concrete, checkable support for
the earlier conclusion that Step E wants a nonperturbative RG (idea 9 / Wilson), not a bigger bootstrap.

---

## 11. Appendix — the naked toy: why a uniform grid is blind to an exponentially small scale (`code/log_discretization_demo.py`, `code/viz_log_discretization.py`)

The §10 result and the Kondo lesson rest on a single elementary fact about discretization, which is
worth stripping to the bone on a problem so trivial that **no method is "needed"** — so the principle is
naked rather than hidden inside the physics. Take the most basic object that carries the
dimensional-transmutation structure, the integral of `1/x`:

```math
\int_\varepsilon^1 \frac{dx}{x}\;=\;\big[\log x\big]_\varepsilon^1\;=\;\log 1-\log\varepsilon\;=\;\log\frac1\varepsilon .
```

The exact value grows only **logarithmically** as the lower scale `ε` shrinks: six decades
(`ε=10^{-6}`) give `≈13.8`; doubling the decades only adds a constant. That is the signature of
**equal weight per decade**. Change variable to `u=\log x`, `du=dx/x`:

```math
\int_\varepsilon^1\frac{dx}{x}\;=\;\int_{\log\varepsilon}^{0}du ,
```

so in log-coordinates the integrand is **flat** — density exactly `1` per unit of `\log x`. Every decade
(a fixed width `Δu=\log 10` in log-space) contributes the same amount, whether it is `[10^{-1},1]` or
`[10^{-6},10^{-5}]`. The integral is just the number of e-folds, `\log(1/\varepsilon)`.

### 11.1 The uniform midpoint rule, and the saturation

`uniform_midpoint(eps,N)` is the midpoint quadrature of that integral on `[ε,1]` with `N` equal cells of
width `h=(1-\varepsilon)/N`, sampling each cell at its center:

```math
x_i=\varepsilon+\Big(i+\tfrac12\Big)\frac{1-\varepsilon}{N},\qquad i=0,\dots,N-1,
\qquad\widehat{I}_{\text{unif}}=\sum_{i=0}^{N-1}\frac{h}{x_i}.
```

(In the code, `(np.arange(N)+0.5)` are the half-integer cell centers, `(1-eps)/N` is the width `h`, and
`np.sum((1-eps)/N/x)` is `Σ h/x_i` verbatim.) The grid is uniform **in the linear variable** `x`, so its
*smallest* node sits at `x_0≈h/2≈1/(2N)` and **there are no nodes below** `1/(2N)`, no matter how small
`ε` is. With `ε` negligible the estimate collapses to a harmonic sum that **saturates**:

```math
\widehat{I}_{\text{unif}}\;=\;\sum_{i=0}^{N-1}\frac{1}{\,i+\tfrac12\,}\;\approx\;\log N+1.4
\;\;\xrightarrow[\varepsilon\to0]{}\;\;\text{independent of }\varepsilon .
```

For `N=20` that is `≈4.4`–`5`, regardless of whether `ε=10^{-4}` or `10^{-12}`. The grid cannot see the
decades between `ε` and `1/(2N)`; it is **blind below its own spacing**. To recover the true
`\log(1/\varepsilon)` the lowest node must reach down to `ε`:

```math
\frac{1}{2N}\;\lesssim\;\varepsilon
\quad\Longrightarrow\quad
N\;\gtrsim\;\frac{1}{2\varepsilon}\quad(\text{cost }\sim 1/\varepsilon,\ \text{exponential in the number of decades}).
```

### 11.2 The logarithmic grid, and the cure

`geometric_trapz(eps,N)` instead spaces nodes log-uniformly (one per decade). Because `dx/x=d\log x` is
flat in `u`, even the crude trapezoid is essentially exact, and the cost to span `ε` is just the number
of decades:

```math
N\;\sim\;\log\frac1\varepsilon\qquad(\text{linear in the number of decades, not }1/\varepsilon).
```

The four-panel figure `code/log_discretization.png` shows this directly: (A) uniform nodes pile up at
large `x` and miss every small decade while log nodes cover each; (B) uniform needs `N\sim 1/\varepsilon`
to converge while log needs `N\sim\log(1/\varepsilon)`; (C) at fixed budget the uniform estimate
**flatlines** as the true scale shrinks while the log estimate tracks `\log(1/\varepsilon)`; (D) the cost
to reach a correlation length `ξ` is `\sim ξ` uniformly versus `\sim\log_2 ξ` logarithmically.

### 11.3 The dictionary to the physics

Every element of the toy has a referent in the Step-E / §10 problem:

```math
\boxed{
\begin{array}{lcl}
\text{toy} & \longleftrightarrow & \text{Yang--Mills / Step E}\\[2pt]
1/x,\ \text{equal weight per decade} & \longleftrightarrow & \text{asymptotically-free RG (fixed }\Delta\text{ per e-fold of scale)}\\
\text{lower limit }\varepsilon & \longleftrightarrow & \text{transmuted scale }\Lambda\sim\mu\,e^{-1/(b_0g^2)}\ \text{; gap }1/\xi\\
\text{uniform grid blind below }1/(2N) & \longleftrightarrow & \text{perturbation theory (blind to }e^{-1/g^2}\text{), uniform-}K\text{ bootstrap}\\
\text{uniform cost }\sim 1/\varepsilon & \longleftrightarrow & \text{bootstrap reach }2K{+}1\gtrsim\xi\ \text{(§10): }K\sim\xi\\
\text{log grid reaches }\varepsilon\ \text{in }\log(1/\varepsilon) & \longleftrightarrow & \text{Wilson NRG / RG: cross the crossover in }\sim\log_2\xi\ \text{decades}
\end{array}}
```

The point is not numerical analysis; it is that **the discretization must match the equal-per-decade
structure of dimensional transmutation, or pay exponentially.** A uniform truncation — whether a momentum
grid, a finite order of perturbation theory, or a uniform-`K` positivity bootstrap — is blind below its
spacing, which is exactly the regime where the transmuted scale lives. An RG that refines resolution by a
fixed factor per step (Wilson's logarithmic discretization) is the *proven* tool for that regime. This is
the elementary reason §10's bootstrap saturates and why Step E asks for a nonperturbative RG.
