# Paper 43 — The ’t Hooft-Flux Modular Confinement Conjecture, and an Attempt to Prove It

**Status.** This is an *exploration toward a proof*, not a proof. The conjecture below is stated
precisely and self-containedly in §0. §1–§6 develop a proof strategy: a reduction to two lemmas, a
fully-worked abelian template where the analogous statement is essentially a theorem, and an honest
accounting of exactly which step is open (it is Lemma 2, the dynamical core, which is of Clay-problem
difficulty — the point of the modular framing is the *hope* that it becomes a rigidity statement
rather than a bare dynamical estimate). Every claim is marked **[EXACT]**, **[PARTIAL]**, or
**[OPEN]**. Nothing here is asserted as a solution of the Yang–Mills problem.

External references (’t Hooft 1979; Göpfert–Mack 1982; Polyakov 1977; Kac–Peterson; Viazovska 2017)
are dressing — §0 defines everything it needs from scratch.

---

## 0. The Conjecture (self-contained)

### 0.1 Lattice and gauge field

Let `L ≥ 2` and let the lattice be the periodic 4-torus `Λ = (ℤ/Lℤ)⁴` with lattice spacing `a > 0`,
sites `x`, directions `μ ∈ {1,2,3,4}`, unit vectors `ê_μ`, links `(x,μ)`, and plaquettes `(x,μ,ν)`
with `μ<ν`. A gauge field is a map `U` from links to `SU(2)`; `dU` denotes normalized Haar measure.
The plaquette holonomy is

```math
U_{x,\mu\nu} \;=\; U_{x,\mu}\,U_{x+\hat e_\mu,\nu}\,U_{x+\hat e_\nu,\mu}^{\dagger}\,U_{x,\nu}^{\dagger}\ \in SU(2).
```

The **Wilson action** and partition function, at inverse coupling `β = 4/g² > 0`, are

```math
S[U] \;=\; \beta\sum_{x,\mu<\nu}\Big(1-\tfrac12\operatorname{tr}U_{x,\mu\nu}\Big),
\qquad
Z \;=\; \int \prod_{(x,\mu)} dU_{x,\mu}\; e^{-S[U]} .
```

The **center** of `SU(2)` is `Z(SU(2)) = \{+\mathbb 1,\,-\mathbb 1\} \cong \mathbb Z_2`. Note `\operatorname{tr}` is
real on `SU(2)` and `\operatorname{tr}(-V) = -\operatorname{tr}V`.

### 0.2 ’t Hooft twist and twisted partition functions

Fix the splitting of directions into a *magnetic plane* `(1,2)` and an *electric plane* `(3,4)`.
For `n \in \mathbb Z_2 = \{0,1\}` define the **magnetically twisted partition function** by flipping the
center sign of the action on a coclosed sheet of `(1,2)`-plaquettes that pierces the `(3,4)`-torus
once. Concretely take the sheet `\mathcal S = \{(x,1,2) : x_3 = x_4 = 0\}` (a set of `L^2` plaquettes)
and set

```math
Z_n \;=\; \int \prod dU\;\exp\!\Big[-\beta\!\!\sum_{p\notin\mathcal S}\!\big(1-\tfrac12\operatorname{tr}U_p\big)
\;-\;\beta\!\!\sum_{p\in\mathcal S}\!\big(1-(-1)^{n}\tfrac12\operatorname{tr}U_p\big)\Big].
```

`Z_0 = Z`. The value of `Z_n` is independent of the position and shape of `\mathcal S` within its
`\mathbb Z_2` homology class (a field redefinition `U\to -U` on a 3-volume moves the sheet); this is the
statement that `n` is a genuine `\mathbb Z_2` *magnetic flux* through the `(3,4)`-torus. **[EXACT]**

### 0.3 Flux free energies and the string tension

Define the **magnetic** and (via the `\mathbb Z_2` Fourier / Wilson dual ensemble) **electric** flux free
energies:

```math
F_m(\beta,L) \;=\; -\log\frac{Z_1}{Z_0},
\qquad
\widehat Z_e=\sum_{n\in\mathbb Z_2}(-1)^{en}Z_n,
\qquad
F_e(\beta,L) \;=\; -\log\frac{\widehat Z_1}{\widehat Z_0}=-\log\tanh\!\big(\tfrac12 F_m\big).
```

The **string tension** is the (conjecturally existent) limit measuring the cost per unit worldsheet
area of an electric center-flux string winding the `(3,4)`-torus:

```math
\sigma \;=\; \lim_{L\to\infty}\frac{F_e(\beta,L)}{(L a)^2}\qquad(\text{electric flux string worldsheet area }=(La)^2).
```

`σ > 0` is **confinement**. (That this limit exists and is positive in 4D `SU(2)` is itself open —
it is the Yang–Mills mass-gap problem in disguise; the conjecture below is a *structural* statement
about *how* `σ` is organized, assuming it exists.)

### 0.4 The renormalized scale

By asymptotic freedom the lattice spacing runs with `β`. With the `SU(2)` one- and two-loop
coefficients `b_0 = \tfrac{11}{24\pi^2}`, `b_1 = \tfrac{17}{96\pi^4}` and `g^2 = 4/\beta`,

```math
a(\beta)\,\Lambda \;=\; \exp\!\Big(-\frac{1}{2 b_0 g^2}\Big)\,(b_0 g^2)^{-b_1/2b_0^2}\big(1+O(g^2)\big)
\;=\;\exp\!\Big(-\frac{3\pi^2}{11}\,\beta\Big)\,\beta^{\,51/121}\big(1+O(1/\beta)\big),
```

where `Λ` is the dynamically generated mass scale. The factor `e^{-3\pi^2\beta/11}` is an **essential
singularity** in `g^2`: invisible to every order of perturbation theory. **[EXACT]** (standard
2-loop lattice asymptotic freedom).

### 0.5 The modular object and the conjecture

The pair `(Z_0,Z_1)` — equivalently `(\widehat Z_0,\widehat Z_1)` — is a vector indexed by the `\mathbb Z_2`
flux lattice. ’t Hooft duality acts on the flux labels `(e,m)\in\mathbb Z_2\times\mathbb Z_2` of the
embedded `(3,4)`/`(1,2)` 2-torus by the modular group `SL(2,\mathbb Z)`,

```math
S:(e,m)\mapsto(m,-e),\qquad T:(e,m)\mapsto(e,\,m+e),
```

i.e. `S` exchanges electric and magnetic flux. **[EXACT]** (’t Hooft 1979.)

> **Conjecture (’t Hooft-flux modular confinement).**
> There exist a modular parameter `\tau=\tau(\beta)` with `\tau\to i\infty` (nome `q=e^{2\pi i\tau}\to0`)
> as `\beta\to\infty`, and a function `\Theta(\tau)` assembled from the twisted partition functions
> `\{Z_n(\beta)\}`, such that:
>
> **(a) [Modularity].** `\Theta` is a modular form (of some weight `w` for some finite-index subgroup
> `\Gamma\subset SL(2,\mathbb Z)`), and the `S`-transform `\tau\mapsto-1/\tau` implements the ’t Hooft
> electric–magnetic duality `m\leftrightarrow e`. Hence `\Theta` is determined by its data at the
> finitely many cusps.
>
> **(b) [Cusp = scale].** The continuum string tension is the leading nontrivial **cusp datum** of
> `\Theta`: with `q=e^{2\pi i\tau}`,
> ```math
> \frac{\sqrt\sigma}{\Lambda}\;=\;c\,\cdot\,\big[\text{coefficient of the leading nonconstant power of }q\text{ in }\Theta\big],
> ```
> for a computable constant `c`. In particular `σ>0` follows from the cusp expansion being nonzero.

The conjecture is the **non-abelian counterpart of a theorem** in the abelian case (§1): for 3D
compact `U(1)`, `\Theta` is the electric Jacobi theta, `S` is Poisson summation, and the confinement
scale is literally its cusp term `q^{v_0}` (`v_0` the lattice Coulomb self-energy). The content is
that 4D `SU(2)` confinement is organized the same way, with `\Lambda` (the asymptotic-freedom scale)
playing the role of the abelian monopole fugacity.

---

## 1. The abelian template (where the analogue is a theorem) — [EXACT/PARTIAL]

For compact `U(1)` with the Villain action `\sum_n e^{-(\beta/2)(\phi-2\pi n)^2}` the structure of §0
is realized rigorously:

- **Modularity is Poisson.** The Villain weight equals its magnetic dual
  `(2\pi\beta)^{-1/2}\sum_m e^{-m^2/2\beta}e^{im\phi}`; this *is* the Jacobi imaginary transformation
  `\theta_3(0|{-1/\tau})=\sqrt{-i\tau}\,\theta_3(0|\tau)` with `\tau=2\pi i\beta`, i.e. the `S`-transform =
  electric↔magnetic duality. **[EXACT]**
- **The scale is the cusp.** In 3D, the dual theory is a monopole Coulomb gas; the photon Debye mass
  and string tension are set by the monopole fugacity `e^{-2\pi^2 v_0\beta}=q^{v_0}`, the leading
  nonconstant term of the electric theta at the cusp `q=e^{-2\pi^2\beta}\to0`. That `σ>0` for all `β`
  is the rigorous Göpfert–Mack theorem; the cusp identity `\text{fugacity}=q^{v_0}` is exact algebra.
  **[EXACT identity; PARTIAL for the full `σ(β)` constant, which is dilute-gas.]**

So in the abelian case the Conjecture is true and (modulo prefactors) proved. The abelian proof has
three ingredients we must reproduce non-abelianly: **(i)** an exact duality giving the modular
`S`-transform; **(ii)** a rigorous positivity/lower bound on the dual (magnetic) free energy
(Göpfert–Mack); **(iii)** identification of the leading cusp term with the physical scale.

---

## 2. The exact non-abelian kinematics — [EXACT]

Two pieces of §0 are already rigorous for `SU(2)` and require no dynamics:

1. **’t Hooft `SL(2,\mathbb Z)`.** The twisted `Z_n` are well defined, sheet-independent, and the flux
   labels transform by `S:(e,m)\mapsto(m,-e)`, `T:(e,m)\mapsto(e,m+e)`. This is ingredient (i): the
   modular `S` exists and is the electric–magnetic duality. **[EXACT]**
2. **A modular `S`-matrix exists in the representation category.** The affine `SU(2)_k`
   characters carry an honest `SL(2,\mathbb Z)` action via Kac–Peterson
   `S_{ab}=\sqrt{2/(k+2)}\sin(\pi ab/(k+2))`, `T=\mathrm{diag}\,e^{2\pi i(h_j-c/24)}`, with `S^2=C=\mathbb 1`
   and `(ST)^3=S^2` up to the `c/24` phase. This shows non-abelian modular *data* is available; whether
   it is the *same* `S` as the 4D flux duality is part of Lemma 1. **[EXACT for the data; the link to
   4D is OPEN.]**

What is **not** kinematic, and is the entire difficulty: there is no literal Poisson summation for
`SU(2)` (the dual of a non-abelian charge lattice is the fusion category, not a lattice), so neither
`\Theta` as a holomorphic modular form nor the cusp=scale identity is given for free.

---

## 3. Reduction to two lemmas — [strategy]

The Conjecture follows from:

- **Lemma 1 (Modularity).** The flux generating function `\Theta(\tau)` is a modular form for some
  `\Gamma`, with `S` = the ’t Hooft duality of §2.1. *Status:* the `S`-transform is **[EXACT]**; that
  `\Theta` is *holomorphic of definite weight* (so that "determined by cusp data" has force) is
  **[OPEN/PARTIAL]** — it is a statement about the analytic structure of `Z_n(\beta)` in a complexified
  coupling.
- **Lemma 2 (Cusp = scale).** The leading cusp coefficient of `\Theta` equals `c\,\sqrt\sigma/\Lambda`,
  and is nonzero. *Status:* **[OPEN]**. This is ingredient (ii)+(iii): a rigorous lower bound on the
  electric-flux (vortex) free energy together with its asymptotic-freedom cusp expansion. It implies
  `σ>0` and is therefore *at least as hard as the Yang–Mills mass gap*.

**Why the modular framing might help (the bet).** Proving `σ>0` directly is the open problem. The
*hope* — the Viazovska analogy — is that Lemma 1 supplies **rigidity**: a holomorphic modular form of
bounded weight is determined by *finitely many* Fourier coefficients, so Lemma 2 could reduce from "an
analytic estimate over all scales" to "evaluate a finite, modularity-constrained set of data and check
one coefficient is nonzero." In sphere packing, modularity converted an infinite optimization into the
explicit construction of one magic function. Whether the same rigidity is available here is the
substantive question of this paper; we do **not** establish it.

---

## 4. Toward Lemma 1 (modularity)

### 4.1 Lemma 1 is a THEOREM in 2D — [EXACT, verified `code/theta_2d_lemma.py`]

2D `SU(2)` Yang–Mills is solvable: on a torus (heat-kernel action, area×coupling `=t`) the partition
function is a sum over irreps `j` with Gaussian-in-Casimir weight, and the `\mathbb Z_2` center twist
inserts `(-1)^{2j}`. With `n=2j+1`,

```math
Z_0(t)=\sum_{j\ge0}e^{-\frac t2 j(j+1)}=e^{t/8}\tfrac12(\theta_3(\tau)-1),\quad
Z_1(t)=\sum_{j\ge0}(-1)^{2j}e^{-\frac t2 j(j+1)}=e^{t/8}\tfrac12(1-\theta_4(\tau)),
\quad \tau=\tfrac{i t}{8\pi}.
```

verified to `3\cdot10^{-16}`. The four `\mathbb Z_2\times\mathbb Z_2` flux sectors of the 2-torus map to the
Jacobi thetas `\{\theta_3,\theta_4,\theta_2\}` (weight `1/2`), and `SL(2,\mathbb Z)` **permutes** them: the
`S`-transform `\tau\mapsto-1/\tau` fixes `\theta_3` and **swaps `\theta_2\leftrightarrow\theta_4`** (verified
to `2\cdot10^{-16}`) — i.e. exchanges the space- and time-twist, the electric↔magnetic duality. So in 2D
Lemma 1 holds *exactly*, with a **3-dimensional** (finite) space of forms — precisely the rigidity the
Conjecture's part (a) wants. Caveat: 2D YM has no dynamical scale, so this anchors part (a) only, not (b).

### 4.2 The plaquette-level theta identity carries to any `d` — [EXACT]

Each lattice plaquette factor is a Jacobi-theta object: the `SU(2)` heat kernel obeys, by Poisson
summation on the spin label (`n=2j+1`),

```math
\frac{1}{\sin\theta}\sum_{n\ge1} n\sin(n\theta)\,e^{-t n^2/4}
=\frac{\sqrt{4\pi/t}}{t\sin\theta}\sum_{m\in\mathbb Z}(\theta+2\pi m)\,e^{-(\theta+2\pi m)^2/t},
```

with `t\leftrightarrow(2\pi)^2/t` the modular `S`. **[EXACT]** The **[OPEN]** step is global: that the full
4D twisted sum, after Haar integration and continuum scaling, assembles into one modular form. The
obstruction is non-abelian: Haar integration produces Verlinde fusion (the Kac–Peterson `S` *mixes*
irreps), not a lattice convolution, so the product of plaquette thetas is not manifestly a lattice theta.

### 4.3 The 4D realization is the effective string — and it RELOCATES `\sigma` away from the cusp — [PARTIAL, important]

There *is* a physically-grounded 4D realization of part (a), but examining it sharpens — and partly
undercuts — the Conjecture. In the confined phase the electric flux tube is described at long distance
by an **effective string** (Lüscher; Polchinski–Strominger; Aharony–Komargodski): its worldsheet is a
2D CFT of `d-2=2` transverse modes. The electric-flux free energy of a tube wrapping a spacetime
2-torus of modulus `\tau_{\rm ws}=iT/R` is, to leading orders,

```math
F_e \;=\; \underbrace{\sigma\,R\,T}_{\text{area term}}\;-\;\log\frac{1}{|\eta(\tau_{\rm ws})|^{\,d-2}}\;+\;\cdots,
\qquad \eta(\tau)=q^{1/24}\prod_{n\ge1}(1-q^n).
```

The Dedekind `\eta` is a weight-`1/2` modular form (`\eta(-1/\tau)=\sqrt{-i\tau}\,\eta(\tau)`), and the
worldsheet `S` (`\tau_{\rm ws}\to-1/\tau_{\rm ws}`) is the open/closed channel duality — plausibly the
’t Hooft `e\leftrightarrow m` swap on the tube. So **part (a) (modularity) is realized in 4D, via `\eta`.**
**[PARTIAL — the effective string itself is rigorous as an IR theory; its derivation from YM is open.]**

But note *where `\sigma` sits*: it is the **area coefficient** (the leading, classical term), an *input*
to the worldsheet theory. The cusp (`q\to0`) expansion of `1/\eta^{\,d-2}` is the *universal* Lüscher
tower `q^{-(d-2)/24}(1+\cdots)` — it depends only on `d` and the torus shape, **not on `\sigma`**. So in
the realized modular object, `\sigma` is **not** a cusp datum.

### 4.4 Two modular variables — and the Conjecture needs the wrong one — [the key finding]

There are *two distinct* modular parameters, and they behave oppositely:

- **Worldsheet `\tau_{\rm ws}=iT/R`** (the tube's torus shape): modularity via `\eta`, established
  (effective string). Here `\sigma` is the input area coefficient; the cusp gives the universal Lüscher
  term. *Supports part (a); does NOT make `\sigma` cusp data.*
- **Coupling `\tau_{c}\propto i\beta`** (the abelian-template variable of §1): here
  `\sigma(\beta)\sim\Lambda^2\sim e^{-3\pi^2\beta/11}` would be a *cusp term* `q^{\#}`, exactly the `U(1)`
  monopole-fugacity pattern `q^{v_0}`. *This is the variable part (b) needs.*

The Conjecture's part (b) (`\sigma=` cusp datum) requires `\tau_c`-modularity — that the twisted
*partition function itself*, continued in the coupling, is a modular form whose cusp term is `\sigma`. But
the modularity we can actually exhibit is `\tau_{\rm ws}`-modularity (the effective string), in which
`\sigma` is an input, not a cusp datum. **The accessible modular rigidity constrains the universal
Lüscher data, not `\sigma`.** And `\tau_c`-modularity is precisely the supersymmetry-protected phenomenon
(Vafa–Witten, §2): in pure `SU(2)` there is no known mechanism making `Z(\beta)` a modular form of the
coupling.

```math
\boxed{
\begin{array}{l}
\textbf{Result of working on Lemma 1.}\ \text{Part (a) (modularity) is on solid ground: PROVEN in 2D}\\
\text{(Jacobi thetas, weight 1/2, finite-dimensional) and REALIZED in 4D via the effective-string }\eta.\\
\text{BUT both realizations put }\sigma\ \text{as an \emph{input} (area coefficient), not a cusp datum, so they}\\
\text{do NOT supply part (b). The version that would (}\tau_c\text{-modularity, }\sigma\sim e^{-c\beta}\text{ as a cusp}\\
\text{term) is exactly the supersymmetry-protected one, with no non-SUSY mechanism known. Net: the}\\
\text{Viazovska rigidity that is genuinely available pins the \emph{universal Lüscher term}, not }\sigma\text{ — so}\\
\text{it does not, as hoped, reduce }\sigma>0\ \text{to a finite nonvanishing check. The bet is weakened.}
\end{array}}
```

---

## 5. Toward Lemma 2 (cusp = scale) — [OPEN, the dynamical core]

Granting Lemma 1, the Conjecture reduces to identifying the leading cusp coefficient with
`\sqrt\sigma/\Lambda`. Strategy, mirroring the abelian proof:

1. **Reflection positivity** gives `\widehat Z_1/\widehat Z_0\in(0,1)`, hence `F_e>0` and `F_m>0` — flux free
   energies are well-defined and the `\tanh` relation holds. **[EXACT]**
2. **A vortex lower bound.** One needs the non-abelian analogue of Göpfert–Mack: a *rigorous lower
   bound* `F_e\ge \sigma_*\,(La)^2` with `\sigma_*>0` surviving `a\to0`. This is exactly where the
   essential singularity must be produced dynamically; no proof exists. The original modular hope (§3)
   was that Lemma 1 would make the cusp coefficient a modular-form datum, so a finite-dimensional form
   space would reduce `\sigma>0` to a finite nonvanishing check. **§4.4 weakens this hope:** the
   modularity actually available (2D thetas; 4D effective-string `\eta`) places `\sigma` as an *input*
   area coefficient, while the cusp data is the *universal* Lüscher term — so the available rigidity
   constrains the wrong quantity. The Viazovska reduction would require coupling-variable
   (`\tau_c`) modularity, which is the supersymmetry-protected phenomenon and is not established (likely
   absent) for pure `SU(2)`. **[OPEN; and now with a specific reason for pessimism.]**
3. **Asymptotic-freedom cusp expansion.** Matching the leading `q`-power to `a(\beta)\Lambda` of §0.4
   fixes the constant `c` and identifies `\Lambda` as the cusp scale (the non-abelian counterpart of
   `q^{v_0}`). **[OPEN, conditional on 2.]**

Honest assessment: step 2 is the Yang–Mills mass gap. Paper 43 does **not** prove it. Its claim is the
*reduction*: IF the flux theta is a modular form of bounded weight (Lemma 1), THEN `σ>0` is a finite
nonvanishing check rather than an infinite-volume estimate. The whole program's value rests on whether
that "IF" holds and the resulting space of forms is genuinely finite-dimensional.

---

## 6. Status, falsifiers, and what would settle it

**Status ledger (updated after working on Lemma 1).**
- §0.1–0.4 definitions; §0.5 `S`-duality; §1 abelian template; §2.1 ’t Hooft `S`; §2.2 affine data;
  §4.1 **Lemma 1 in 2D (PROVEN)**; §4.2 plaquette theta identity; §5.1 positivity — **[EXACT]**.
- §4.3 Lemma 1 realized in 4D via the effective-string `\eta` — **[PARTIAL]** (IR-effective; derivation
  from YM open) — *and it places `\sigma` as an input, not a cusp datum.*
- Lemma 1 part (a) (modularity) — **[on solid ground: theorem in 2D, effective-string in 4D]**.
- Lemma 1(b) (definite-weight modularity in the coupling variable, 4D) — **[DECIDED NEGATIVE, §7.2]**:
  fails because modular `S`-covariance is a strong–weak (Montonen–Olive) duality absent in pure `SU(2)`
  (asymptotic freedom breaks `g²↔1/g²`); the ’t Hooft flux duality is exact but only kinematic.
- Lemma 1 → Lemma 2 bridge (the Viazovska reduction of `\sigma>0` to a finite check) — **[CLOSED]**: it
  needed exactly the holomorphic coupling-variable modularity that §7.2 refutes.
- Lemma 2 (`σ>0`) — **[OPEN]**, of mass-gap difficulty; **not** reduced by Lemma 1 (the modular route is shut).
- Conjecture as a whole — part (a) holds only in weak senses (`\sigma` an input); part (b) **refuted**.
  The modular-certificate program does **not** crack confinement. *Decided, mostly negative.*

**Falsifiers.** The Conjecture is wrong if any holds:
- (F1) The continuum `\sqrt\sigma/\Lambda` extracted from `F_e` does **not** match the leading
  `q`-coefficient predicted by any modular form of the weight forced by `S` (testable by the 4D lattice
  campaign + a fit to candidate modular forms).
- (F2) `Z_n(\beta)`, continued in `\tau`, has the wrong analytic structure to be a modular form of
  *bounded* weight (e.g. essential singularities away from cusps), killing the rigidity that makes
  Lemma 2 finite.
- (F3) The fusion-twisted plaquette product (§4) provably fails to be modular — then the abelian
  template has no non-abelian analogue and the program should be abandoned.

**What would settle it.** A theorem for Lemma 1 (the analytic/representation-theoretic part: is the
twisted SU(2) partition function a modular form, and of what weight?) is the decisive near-term target,
because it is *not* dynamical and may be attackable with the heat-kernel/affine-character machinery of
§2–§4. If Lemma 1 holds with a finite-dimensional form space, Lemma 2 becomes a (hard but finite)
nonvanishing problem; if Lemma 1 fails, the Conjecture and the modular-certificate program fall with it.

**Honest summary.** Paper 43 contributes a *precise, self-contained statement* of the conjecture, a
*reduction* to two lemmas with the abelian case as a worked theorem, and — from working on Lemma 1 —
a **theorem in 2D** (the twisted `SU(2)` partition functions are the weight-`1/2` Jacobi thetas, a
3-dimensional modular vector permuted by `SL(2,\mathbb Z)`, with `S` = the electric–magnetic duality)
plus a **4D realization via the effective-string `\eta`**. The same work delivered an honest negative:
in both realizations `\sigma` is an *input* (the worldsheet area coefficient), and the cusp data is the
*universal Lüscher term*, so the available modular rigidity does **not** pin `\sigma` — the
Viazovska-style reduction of `\sigma>0` to a finite check would need coupling-variable modularity, which
is supersymmetry-protected and not available for pure `SU(2)`. So: **part (a) of the conjecture is
supported and partly proved; the deeper bet (part b) is now under specific, well-located doubt.** This
is progress of the honest kind — it advances and prunes simultaneously, and proves none of the open
dynamical content.

---

## 7. A Plan to Rigorously Decide Lemma 1(b) (definite-weight modularity in 4D)

Lemma 1 splits into **(a)** `S` = the ’t Hooft duality (**proven exact**, §2.1) and **(b)** the open core:
that the 4D flux partition vector is a genuine **modular form of definite weight**. This section is a
plan to *decide* (b) rigorously — prove it or refute it cleanly. Given §4.4, the realistic expectation
is a precise refutation pinned to the absence of a holomorphic coupling; the plan is structured to land
either outcome as a theorem.

**Precise statement to prove/refute.** There exist a finite-index `\Gamma\subseteq SL(2,\mathbb Z)`, a
weight `w\in\tfrac12\mathbb Z`, a finite-dimensional multiplier system `\rho:\Gamma\to GL(V)` on the flux
space `V=\{f:\mathbb Z_2\times\mathbb Z_2\to\mathbb C\}`, and a complex `\tau` in which `Z[e,m](\tau)` is
**weakly holomorphic** (poles only at cusps — partition functions *grow* at cusps, e.g. the area-law
factor `e^{\sigma A}=q^{-\#}`) with moderate growth there, such that `Z(\gamma\tau)=(c\tau+d)^{w}\rho(\gamma)Z(\tau)`.

**Phase 0 — Pin the target space `(\Gamma,w,\rho)`.** *[concrete, non-dynamical; executed in §7.1.]*
Compute the `SL(2,\mathbb Z)` representation the exact ’t Hooft `S:(e,m)\mapsto(m,e)`,
`T:(e,m)\mapsto(e,m+e)` generate on `V`. *Tools:* permutation matrices, theta/`\Gamma(2)` theory.

**Phase 1 — The holomorphy test (the crux; likely negative).** Test whether `Z[e,m]` is holomorphic in
the candidate coupling variable `\tau=\theta/2\pi+4\pi i/g^2` (the SUSY S-duality parameter). Pure YM has
`F(\theta)\approx\tfrac12\chi_{\rm top}\theta^2`, even in `\theta` and real — incompatible with holomorphy
in `\tau`. *Tools:* `\theta`-vacuum structure, topological susceptibility, Lee–Yang zeros in complex
`\theta`, reflection positivity. *Expected:* holomorphy fails (no SUSY-protected holomorphic coupling).

**Phase 2A — If holomorphy fails (likely): prove + characterize the obstruction.** Show the would-be
modular transformation holds only up to a holomorphic anomaly, i.e. the flux functions are
**quasimodular** (like `E_2`) or **mock modular** (Zwegers; as Vafa–Witten partition functions are on
non-compact/wall-crossing manifolds), not modular of definite weight. This rigorously **refutes** Lemma
1(b) in the coupling variable and explains the §4.4 doubt. Decisive, publishable, and acceptable.

**Phase 2B — If holomorphy holds (surprise): finish.** Prove moderate growth at both cusps (`\beta\to\infty`
asymptotic freedom; `\beta\to0` strong coupling + reflection-positivity bounds); conclude vector-valued
(weakly holomorphic) modular form via Phase 0 + standard theory.

**Phase 3 — The provable positive (parallel): worldsheet modularity.** Independently establish, rigorously,
that the confining flux free energy is a weight-`-(d-2)/2` modular form in the *worldsheet* modulus
`\tau_{\rm ws}=iT/R` to all orders in `1/(\sigma R^2)` (universal terms fixed by reparametrization
invariance, Aharony–Komargodski–Field). True, but with `\sigma` an input — not the conjecture's version.

**Phase 4 — Calibrate.** The Phase-1 holomorphy test must return *yes* for `\mathcal N{=}4` SYM (known
modular) and *no* for pure YM; reproduce the 2D Jacobi-theta theorem; check large-`N`/finite-`T` limits.

**Honest risk.** Most likely endpoint: a **rigorous negative** for the coupling-variable (b) (Phase 1→2A)
— pure SU(2) lacks the holomorphic coupling, so the flux functions are quasi/mock-modular, not modular of
definite weight; the Viazovska rigidity that would pin `\sigma` is therefore unavailable. The provable
positive is the worldsheet modularity (Phase 3). The decisive near-term steps are Phase 0 (now) and
Phase 1 (the single question that settles it).

### 7.1. Phase 0 result — the target is `\Gamma(2)`, with `S_3` permuting the fluxes — [EXACT]

Executed in `code/flux_modular_rep.py`. The exact ’t Hooft generators act on the 4-dimensional flux
space `V` as permutations:

```text
S: (e,m)->(m,e)  swaps the fluxes (0,1)<->(1,0);   fixes (0,0),(1,1)
T: (e,m)->(e,m+e) swaps the fluxes (1,0)<->(1,1);  fixes (0,0),(0,1)
S^2 = T^2 = (ST)^3 = I ;   |<S,T>| = 6 = S_3 = SL(2,Z_2).
```

Therefore the `SL(2,\mathbb Z)` action **factors through** `SL(2,\mathbb Z)/\Gamma(2)\cong SL(2,\mathbb Z_2)\cong S_3`,
so the level-2 principal congruence subgroup **`\Gamma(2)` acts trivially**: the flux partition vector is
a vector-valued modular form **for `\Gamma(2)`**, with `S_3` permuting the three nontrivial fluxes
`\{(0,1),(1,0),(1,1)\}=\{\text{magnetic, electric, dyonic}\}` and `(0,0)` a singlet. As `S_3`-reps,
`V = 2\cdot(\text{trivial})\oplus(\text{standard, 2-dim})`.

```math
\boxed{
\begin{array}{l}
\textbf{Phase 0 (EXACT).}\ \text{Target space }=\ \text{weakly-holomorphic vector-valued modular forms for}\\
\Gamma(2),\ \text{multiplier }\rho=\text{the }S_3\text{ flux permutation, with poles allowed at the cusps (the}\\
\text{area-law growth }e^{\sigma A}=q^{-\#}\text{).}\ \text{This is \emph{exactly} the home of the Jacobi thetas}\\
\{\theta_2,\theta_3,\theta_4\}\ \text{(weight }1/2\text{), which realize it in 2D (§4.1). Candidate weight: }1/2\text{ in 2D;}\\
-(d-2)/2=-1\text{ in 4D (effective-string }\eta^{-(d-2)}\text{, worldsheet variable). The ring of }\Gamma(2)\text{ forms}\\
\text{is }\mathbb C[\theta_3^4,\theta_4^4]\text{, so each weight gives a \emph{finite-dimensional} space — the rigidity the}\\
\text{conjecture needs is now pinned down explicitly.}
\end{array}}
```

So the structural target of Lemma 1(b) is completely fixed and finite-dimensional, and 2D realizes it
exactly. What remains is whether the **4D** flux vector actually lands in this space — Phase 1.

### 7.2. Phase 1 result — Lemma 1(b) FAILS for pure 4D SU(2) (no Montonen–Olive without SUSY) — [decided NEGATIVE]

Executed in `code/modular_obstruction.py`. A modular form needs both **(H)** holomorphy and **(C)**
covariance, `Z(-1/\tau)=(c\tau+d)^w\rho(S)Z(\tau)`. The test sharpened the obstruction — and it is *not*
the one I first guessed:

- **(H) holomorphy is fine.** In the coupling variable `\tau_c=i\,\#/g^2`, the partition function is
  holomorphic (entire, on a finite lattice) in the complexified coupling. Holomorphy is not the problem.
- **(C) covariance FAILS — this is the obstruction.** The modular `S`, `\tau_c\mapsto-1/\tau_c`, sends
  the coupling to its **strong–weak dual** `g^2\mapsto\#/g^2`. Covariance therefore *demands* a
  Montonen–Olive strong–weak **duality** — a supersymmetric (`\mathcal N{=}4`) phenomenon. Pure `SU(2)`
  has **asymptotic freedom**, which manifestly breaks `g^2\leftrightarrow 1/g^2`: the string tension is
  `\sigma a^2\sim e^{-(3\pi^2/11)\beta}` (tiny) at weak coupling but `\sim-\log(\beta/4)` (`O(1)`) at
  strong coupling — related across the would-be `S`-dual points by **no power-law automorphy factor**
  (their ratio grows exponentially; see the table in the code). So the dynamical `Z` is not
  `S`-covariant. The exact ’t Hooft flux duality of §2.1/§7.1 is only **kinematic** — it permutes flux
  *labels*; it does **not** make the partition function transform with an automorphy factor.
- **The `\theta`-augmented variable is separately dead.** Trying `\tau=\theta/2\pi+4\pi i/g^2` (the SUSY
  `S`-duality parameter) fails by reality/CP: `Z(\theta)` is real and even, so its `\theta`-Fourier
  coefficients are two-sided-symmetric (`\propto I_n(\chi)`, `a_n=a_{-n}`, nonzero on both sides) —
  never a one-sided weakly-holomorphic `q`-expansion. SUSY evades this with a holomorphic *index* (not
  the real partition function); pure YM has no such index.
- **Why 2D was different.** 2D YM *is* modular because its modular `S` is the exact **area duality**
  (Migdal), which 2D possesses. 4D non-SUSY YM has no analogous exact duality to serve as `S`.

```math
\boxed{
\begin{array}{l}
\textbf{Phase 1 verdict: Lemma 1(b) is FALSE for pure 4D SU(2).}\ \text{Not for lack of holomorphy, but}\\
\text{because the modular }S\text{-covariance \emph{is} a strong–weak (Montonen–Olive) duality, which is a}\\
\text{supersymmetric phenomenon absent in pure Yang–Mills (asymptotic freedom breaks }g^2\!\leftrightarrow\!1/g^2).\\
\text{The 't Hooft flux duality is exact but kinematic (labels only); the dynamical }Z\text{ does not transform}\\
\text{covariantly. Hence the flux vector is NOT a holomorphic modular form of definite weight in the}\\
\text{coupling variable — the version the Conjecture's part (b) requires. The Viazovska-style rigidity}\\
\text{(which needs exactly this holomorphic modularity) is therefore unavailable. Decided, negative.}
\end{array}}
```

**Consequence for the Conjecture.** Part (a) [modularity] holds only in the weaker senses already
catalogued — 2D Jacobi thetas (§4.1) and the 4D worldsheet `\eta` (§4.3, Phase 3), where `\sigma` is an
input. Part (b) [`\sigma` = cusp datum via coupling-variable holomorphic modularity] is **refuted**: it
would require a coupling `S`-duality pure YM does not have. So the modular-certificate route to `\sigma>0`
is **closed** — as §4.4 anticipated, now with a precise, well-founded reason (no Montonen–Olive). Rigor
note: the failure of `S`-covariance is demonstrated for the specific (and only natural) variable
`\tau_c=i\#/g^2`; it rests on the well-established absence of strong–weak self-duality in pure YM, which
is physics-rigorous rather than a formal no-go against every conceivable exotic structure. **[strong /
rigorous-physics; not a formal impossibility theorem.]**

---

## 8. Postscript — where the obstruction points: the ℝ³×S¹ semiclassical route

Phase 1 closed the flat-4D modular route for a precise reason: modular `S`-covariance *is* a strong–weak
(`g²↔1/g²`) duality, and pure YM has none. But that diagnosis also says *where the idea can survive*: in a
regime where the nonperturbative scale is **calculable**, so that no duality of the full strongly-coupled
partition function is needed. That regime exists.

**The reframing.** Put `SU(2)` on `ℝ³×S¹` with a small circle of circumference `L`, center-stabilized
(double-trace deformation, or periodic adjoint fermions). For small `L`, asymptotic freedom makes the
theory weakly coupled; the holonomy around `S¹` abelianizes `SU(2)→U(1)` at the center-symmetric point,
and the nonperturbative objects are **monopole-instantons** in a dilute gas — precisely the 3D Polyakov
mechanism whose abelian version this program already settled. Three reasons this is the natural heir:

1. **The essential singularity becomes derived, not conjectured.** The mass gap is
   `m\sim e^{-S_0}`, `S_0=4\pi^2/g^2(L)` — the `e^{-1/g^2}` "wall," now obtained from first-principles
   semiclassics rather than assumed.
2. **§19.1 is its abelian shadow.** We *proved* 3D U(1) confinement scale `=` monopole fugacity `= q^{v_0}`
   (theta cusp). The small-`L` `SU(2)` monopole gas is the non-abelian version of exactly that object.
3. **The affine structure of §19.3 is physical here.** The monopoles carry magnetic charges on the
   **affine coroot lattice** of `SU(2)` (the simple monopole `+\alpha` and the Kaluza–Klein monopole),
   so the monopole-gas partition function is a theta on the affine lattice — affine thetas are modular
   (Kac–Peterson). The modular data we found abstractly is realized by a calculable gas.

**Why this dodges §7.2.** We no longer ask the flat-4D partition function to be modular (it cannot be —
no `S`-duality). We ask whether the *calculable* effective monopole gas has theta structure — and dilute
Coulomb gases generically do (Coulomb gas = sine-Gordon = theta on the charge lattice). The obstruction
was specific to demanding modularity of the full strongly-coupled `Z`; it evaporates once the
nonperturbative sector is semiclassically explicit.

**The conjecture this points to** (developed in **Paper 44**): the `SU(2)`-on-`ℝ³×S¹` monopole-instanton
gas realizes an affine `A_1^{(1)}` theta whose **leading cusp datum is the mass gap / string tension** —
the non-abelian, *calculable* realization of the §19.1 cusp theorem. The remaining open core is no longer
"4D modularity" (shut) but **adiabatic continuity**: that the controlled small-`L` confined phase connects
to 4D without a phase transition. That is a different, more tractable, and actively-studied open problem,
and resurgence (the perturbative/nonperturbative trans-series rigidity) is the tool for the continuation.
Paper 44 formulates and explores this independently.
