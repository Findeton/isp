# Relativistic ISP V4 Paper 45: The Certified Finite-Window Crossing Program For The Fixed-IR Confinement Problem

Author: Felix Robles Elvira

Date: 2026-06-10

Status: research-program paper with one executed demonstration. This paper does
**not** prove 4D continuum Yang–Mills confinement, the mass gap, or
`H_3sec(R, ζ_R)`. Its claims are: (i) a decision-theoretic classification
showing that, after the corpus's no-go map (Papers 40–44), exactly one
technology class remains compatible with every constraint on the fixed-IR
problem — **certified finite computation** — and that this class has never been
applied to the problem; (ii) a precise three-interface architecture (**E/T/X**:
Entry compactness / certified Traversal / open eXit basin) that reduces
`H_3sec(R, ζ_R)` to three named targets, of which two are finite computations
and one is a weak-coupling-only extraction; (iii) an **executed, certified
demonstration** of the architecture on the one exactly-renormalizable cousin of
4D `SU(2)` that has genuine dimensional transmutation (the hierarchical /
Migdal–Kadanoff model), including a proved exit-basin lemma with explicit
constants and a machine-certified window crossing whose step count and
working precision are **linear** in `β₀` (total cost polynomial) — i.e., the
log-refinement principle of Paper 44 §10–11 realized as an actual rigorous
computation through an essential singularity. Claims are
marked **[EXACT]**, **[EST]**, **[NEW]**, or **[OPEN]**.

Searchable tag: `V4P45-CERTIFIED-FINITE-WINDOW-CROSSING-PROGRAM`.

---

## 0. The Inherited Problem And Its Invariant Core

The fixed-IR confinement problem is the single analytic input to which Paper 40
closed the center-sign route:

```math
\mathsf H_{\mathrm{3sec}}(R,\zeta_R):\qquad
\liminf_{a\to0}\, q^{\zeta}_{R,a} \;>\; 0
\qquad\text{(three-sector nonconcentration at fixed physical }R\text{)} .
```

Papers 40–44 established a chain of *equivalences* (not analogies) that
identifies its invariant core. Each link is proved or located in the corpus:

```math
\boxed{
\begin{array}{rl}
\mathsf H_{\mathrm{3sec}}(R,\zeta_R)
&\overset{\text{P40 §35}}{\Longleftrightarrow}\ \text{single-collar charged ratio / center-sign certificate}\\[1mm]
&\overset{\text{P41 §19}}{\Longleftrightarrow}\ \liminf_{a\to0}\inf_\eta\big(1-|m(\eta)|\big)\ge\delta_R>0
\quad(\text{center-flux area law at fixed }R)\\[1mm]
&\overset{\text{P41 §32}}{\Longleftrightarrow}\ \text{the }SO(3)\text{ dressing }\mathcal D\text{ places the induced }Z_2\text{ theory}\\
&\qquad\qquad\ \text{in its disordered phase at fixed }R\text{, uniformly in }a\\[1mm]
&\overset{\text{P41 §34.7b, §37}}{\Longleftrightarrow}\ \text{Gap 2: the }t\leftrightarrow\beta\text{ placement, uniform in }a\\[1mm]
&\overset{\text{P41 §45}}{\Longleftrightarrow}\ \langle\operatorname{tr}\Omega\rangle=0\ \forall L\ \text{(no center breaking in }L\text{, deformed }\mathbb R^3\times S^1)\\[1mm]
&\Longleftrightarrow\ \textbf{crossing a finite intermediate-coupling window with no small parameter.}
\end{array}}
```

The last line is the form this paper works with, and it deserves one paragraph
of justification because the entire program rests on it. **[EXACT, assembled
from the corpus]**

*The window is finite and `a`-independent.* On the UV side, Balaban's
small-field RG (with the §27/§28 decrement) rigorously carries the flow from
the bare coupling `g_0^2 = 4/β_0` down to any fixed small `g_*^2`, in
`K_{\max}\sim 4β_0` blocking steps; the physical scale at the window's entry is
`ξ_{\rm in} \sim \Lambda^{-1}\cdot O(1)` — a *fixed physical scale* (P41 §28.3).
On the IR side, the strong-coupling cluster expansion (Osterwalder–Seiler)
controls every effective coupling beyond some fixed `g_{**}^2`, and the
disordered phase of the induced `Z_2` theory begins at the *exact* Wegner point
`β^* = \tfrac12\log(1+\sqrt2)` (P41 §31). The gap between the two is the
window `[g_*^2,\, g_{**}^2]`: a **fixed, `a`-independent coupling interval**,
crossed by the block flow in `N(R) = O(1)` steps — a number that does **not**
grow as `a\to0`. All of the `a→0` quantifier lives *before* the window (in how
the flowed action arrives at `ξ_{\rm in}`); none of it lives inside. What makes
the window hard is not asymptotics but the absence of any expansion parameter
inside it.

### Non-claims

This paper does not prove: `H_3sec`; any 4D string tension or mass gap; the
entry-compactness extraction (Target 45.E); a certified one-step 4D RG map
(the engineering core of Target 45.T); confinement on the hypercubic lattice
at any coupling outside known regimes. The executed demonstration (§4) is a
theorem-grade computation about the *hierarchical* model only, with one
explicitly flagged classical-difficulty gap (Target 45.D, entry for
arbitrarily weak bare coupling).

---

## 1. The Constraint Inventory: What Any Solution Must Respect

Collected from the corpus; a proposed solution violating any line is dead on
arrival. **[EXACT, citations]**

```math
\boxed{
\begin{array}{ll}
\textbf{C1 (fixed-IR, uniform in }a\textbf{).} & \text{Constants depend on }R\text{ only (P41 §32.7 R1–R2).}\\[1mm]
\textbf{C2 (intermediate coupling).} & \text{The decisive estimate lives at }g\sim O(1)\text{; weak coupling is}\\
& \text{ordered, strong coupling never reaches the continuum (R3, P41 §28.4–28.5).}\\[1mm]
\textbf{C3 (no dilute-gas shortcut).} & \text{Fugacity expansions break exactly at condensation (R4).}\\[1mm]
\textbf{C4 (non-circularity).} & \text{No assumed gap, clustering, }\sigma>0\text{, center dominance (R5).}\\[1mm]
\textbf{C5 (no uniform truncation).} & \text{Any fixed-resolution method is blind below its spacing —}\\
& \text{exponential cost at the transmuted scale (P44 §10–11, proved in the lab).}\\[1mm]
\textbf{C6 (no modular protection).} & \text{Coupling-variable modularity needs Montonen–Olive; refuted}\\
& \text{for pure YM (P43 §7.2). No SUSY index exists to evaluate.}\\[1mm]
\textbf{C7 (no eighth disguise).} & \text{Seven reformulations collapsed to one bedrock core; further}\\
& \text{reformulation is not progress (P41 §37.3).}\\[1mm]
\textbf{C8 (alignment).} & \text{No measure tilt, no hidden Markov dynamics; ISP records expose}\\
& \text{variables only (P40 §16.4–16.5, P41 §1).}
\end{array}}
```

---

## 2. The Decision-Theoretic Step: Only One Technology Class Survives

`V4P45-TECHNOLOGY-CLASSIFICATION`. **[NEW as an explicit classification;
individual entries are corpus results or classical facts]**

A "finite window with no small parameter" is not a new kind of problem in
mathematical physics. The known epistemic technologies for it are exactly
four. We audit each against §1.

**(a) Exact solution / integrability.** Absent in 4D YM; 2D solvability
anchors nothing dynamical (P43 §4.1 caveat). *Dead.*

**(b) Protected rigidity (SUSY, index theorems, modularity of the coupling).**
This was the Paper 42/43 bet: a holomorphic modular object whose finitely many
cusp data pin the answer — the Viazovska move. Refuted: modular `S`-covariance
in the coupling *is* a strong–weak duality, which pure YM lacks (P43 §7.2;
violates nothing — it simply does not exist here). *Dead, with a precise
reason.*

**(c) Monotonicity / correlation inequalities.** The audit is short but worth
recording because each entry fails for a *structural* reason:

- *Griffiths–FKG on the `Z_2` sector:* all-ferromagnetic couplings give
  **lower** bounds on order, i.e. **upper** bounds on disorder — the wrong
  side. Confinement is a disorder *lower* bound. **[EXACT, classical]**
- *Wegner duality:* maps disorder to dual order, where Peierls/Griffiths could
  give the right-side bound — but the dual couplings of the *dressed* theory
  are again dynamical unknowns; the placement question returns unchanged.
  (This is the §29/P41 induced-`Z_2` loop, already closed by §29.7.)
- *Bond-moving (Migdal) inequalities:* reflection positivity gives one-sided
  free-energy comparisons for moved bonds, but the Wilson-loop comparison runs
  the wrong way for confinement lower bounds; this is precisely the gap that
  has kept the decimation program (Tomboulis's claimed interpolation proof)
  from closing. **[EST; literature flag, §7]**
- *Tomboulis–Yaffe / vortex free-energy inequalities:* convert between flux
  ensembles but do not place the coupling (P40 §50 audit).

No known inequality *places* the effective coupling; they all *transport*
information between formulations at the same unknown location. *Dead as a
standalone; alive as glue.*

**(d) Certified finite computation.** Verify a finite, open-condition
statement about a compact family by a rigorously error-bounded computation
(interval arithmetic / validated numerics), as in the Koch–Wittwer
computer-assisted proof of the Feigenbaum conjectures — the standing precedent
for a *renormalization* statement with no small parameter settled by certified
computation. Audit against §1: it needs no small parameter (C2, C3); its
resolution refines per RG step, so it is not a uniform truncation (C5); it
assumes nothing about the IR (C4); it requires no protected structure (C6);
it is a tool, not a reformulation — the statement being verified remains
P41 §32(ii) verbatim (C7); it is an analytic device outside the measure (C8).
The `a`-uniformity (C1) is the one constraint a computation cannot absorb —
it must be *quarantined* into a weak-coupling statement first. That
quarantine is exactly interface (E) below.

```math
\boxed{
\begin{array}{l}
\textbf{Conclusion of the classification.}\ \text{Every constraint-compatible route to the fixed-IR}\\
\text{problem factors through a certified finite computation; and this is the unique class the}\\
\text{corpus has never deployed. The way to \emph{actually solve} the fixed-IR problem is therefore}\\
\text{not another estimate or another disguise, but: (1) quarantine the }a\to0\text{ quantifier into}\\
\text{a weak-coupling compactness statement; (2) cross the window by finitely many}\\
\text{error-certified RG steps; (3) land in an open, classically-controlled basin. The rigidity}\\
\text{that Paper 43 sought from modularity (a finite check) is manufactured by compactness.}
\end{array}}
```

---

## 3. The E/T/X Architecture

`V4P45-ETX-ARCHITECTURE`. **[NEW]**

Fix the physical scale `R` of `H_3sec`. Choose window endpoints
`0 < g_*^2 < g_{**}^2 < \infty` (fixed once, `R`-dependent only). Let
`\mathcal A_a(k)` denote the flowed center-sector effective action of 4D
`SU(2)` at blocking level `k` from lattice spacing `a` — concretely, in the
maximal localization of P41 §32: the induced `Z_2` gauge action
`S^{\rm eff}_{Z_2} = S^{\rm bare}_{Z_2} + \mathcal D` together with the
residual `SO(3)` remainder data, represented as a polymer-activity vector in a
weighted Banach space `\mathcal B_\kappa` whose norm enforces
Prop.-41.38-grade tail decay (super-exponential band/range decay is what makes
balls of `\mathcal B_\kappa` *totally bounded* in the weaker verification
norm — this is where the corpus's structural theorem does real work).

### 3.1. Target 45.E (Entry compactness) — [OPEN, weak-coupling technology]

```math
\boxed{
\begin{array}{l}
\textbf{45.E:}\ \exists\,\mathcal K\subset\mathcal B_\kappa\ \text{compact, }\exists\,a_0>0:\ \text{for all }a<a_0\text{, at the level }k_{\rm in}(a)\\
\text{where the running coupling first reaches }g_*^2,\ \text{the flowed action satisfies }\mathcal A_a(k_{\rm in})\in\mathcal K.
\end{array}}
```

This is the *entire* `a→0` content of the problem, and it lives only at weak
effective coupling, where the rigorous tool exists (Balaban's small-field RG;
the large-field sectors are exponentially suppressed there, P41 §28.1). It
asserts no IR physics whatsoever — no gap, no clustering, no disorder (C4
respected): only that asymptotic freedom funnels all bare couplings into one
compact family of effective theories at the fixed physical scale
`ξ_{\rm in}\sim\Lambda^{-1}`. It is the precise mathematical form of
"universality of the window entry," and it is an *extraction* from
known-technology territory rather than new physics: Balaban's UV-stability
bounds control exactly these effective actions, but were never packaged as a
compactness statement in a norm strong enough for (T). This is hard,
multi-year, expert work — but it is *weak-coupling* work.

### 3.2. Target 45.T (Certified traversal) — [OPEN, finite engineering core]

```math
\boxed{
\begin{array}{l}
\textbf{45.T:}\ \text{construct a one-step blocked RG map }\mathcal R:\mathcal B_\kappa\to\mathcal B_\kappa\ \text{valid at }O(1)\\
\text{coupling, with \emph{certified two-sided error}: an implementable }\widehat{\mathcal R}\text{ and a bound}\\
\|\mathcal R(A)-\widehat{\mathcal R}(A)\|\le\epsilon(A)\ \text{computable from finitely many activity norms; then verify,}\\
\text{on a finite }\varepsilon\text{-net of }\mathcal K\ \text{(compactness + uniform continuity of }\mathcal R\text{), that}\\
\mathcal R^{N}(\mathcal K)\subset\mathcal X\quad\text{for some explicit }N=N(R)=O(1).
\end{array}}
```

Notes. (i) The number of steps `N` is `a`-independent (§0), so this is a
*single finite computation*, not a family of them. (ii) The state space is the
**dressed-`Z_2` localization**, not full `SU(2)` — discrete center variables
plus a quantitatively tail-bounded coupling tower; this is the smallest state
space the corpus's exact reductions permit, and the reason 45.T is plausible
at all. The `SO(3)` coset enters only through the per-step remainder bound
`\epsilon(A)` — bounding one blocking step of the coset at `O(1)` coupling on
a *fixed block* is a finite-dimensional integration problem with compact
group fibers, not an iterated thermodynamic estimate; it must be done with
two-sided rigor, which is exactly what R6 (gauge/section control) demands and
permits. (iii) The verification condition `\mathcal R^N(\mathcal K)\subset
\mathcal X` is **open** in `\mathcal B_\kappa`, so it is decidable on a finite
net at finite precision — false margins fail loudly rather than silently.

### 3.3. Target 45.X (Exit basin) — [partly EXACT already]

```math
\boxed{
\begin{array}{l}
\textbf{45.X:}\ \text{exhibit an open set }\mathcal X\subset\mathcal B_\kappa\ \text{of effective actions for which center disorder}\\
\text{at the fixed block scale is a \emph{theorem}: the strong-coupling/Peierls–cluster domain of the}\\
\text{dressed }Z_2\text{ theory (all couplings summable below an explicit threshold), within which}\\
1-|m(\eta)|\ge\delta>0\ \text{holds with }\delta\ \text{explicit; then P40's closure theorem}\\
(\mathsf H_{\mathrm{3sec}}\Rightarrow(18.20))\ \text{converts basin membership into the fixed-IR certificate.}
\end{array}}
```

The cluster-expansion side of 45.X is classical technology (the corpus's
strong-coupling theorems 40.2/40.3 and P41 §17.2 are its prototypes at bare
strong coupling; 45.X needs the *effective-action* version with extended,
tail-bounded couplings — a quantitative but standard extension). One point is
load-bearing and must be built in from the start: `H_3sec` carries an
`\inf_\eta` over *collar conditionings*, so the basin theorem must hold
**uniformly in boundary conditions** — which is precisely the uniformity a
convergent cluster expansion in the disordered phase supplies (boundary terms
enter only through surface-order corrections), and is why an expansion-domain
basin, rather than a bare order-parameter inequality, is the right exit
interface. The conversion step is then Paper 40's already-proved conditional
closure. **[EST]**

### 3.4. Theorem 45.1 (conditional reduction) — [proof: assembly]

```math
\boxed{
\textbf{45.E}\ \wedge\ \textbf{45.T}\ \wedge\ \textbf{45.X}
\;\Longrightarrow\;
\mathsf H_{\mathrm{3sec}}(R,\zeta_R)
\;\overset{\text{P40 §35}}{\Longrightarrow}\;
\text{fixed-IR center-sign certificate.}
}
```

*Proof.* For `a<a_0`, 45.E puts `\mathcal A_a(k_{\rm in})\in\mathcal K`. 45.T
gives `\mathcal A_a(k_{\rm in}+N)=\mathcal R^N(\mathcal A_a(k_{\rm in}))\in
\mathcal X` with constants uniform over `\mathcal K`, hence uniform in `a`.
45.X gives `1-|m(\eta)|\ge\delta` at the fixed block scale, uniformly in `a`,
which is P41 §32.6(iii) = `H_3sec` (P41 §19/P40 §35 equivalences). ∎

**Quantifier audit** (where each hard quantifier is consumed):

```math
\boxed{
\begin{array}{lll}
\text{quantifier / obstruction} & \text{consumed by} & \text{with what tool}\\\hline
\forall a\to0\ \text{(C1)} & \text{45.E only} & \text{weak-coupling RG (Balaban)}\\
g\sim O(1),\ \text{no parameter (C2,C3)} & \text{45.T} & \text{certified computation (no expansion)}\\
\text{IR asymptotics} & \text{45.X + P40 closure} & \text{open basin + cluster expansion}\\
\text{exponentially small scale (C5)} & \text{the architecture} & N\ \text{steps of per-decade refinement}
\end{array}}
```

### 3.5. Compliance audit against §1 — [check]

C1: quarantined in 45.E. C2/C3: 45.T uses no expansion — error bars replace
small parameters. C4: 45.E asserts weak-coupling compactness only; 45.X
*concludes* (never assumes) disorder. C5: resolution refines by a fixed factor
per step; total cost polynomial in window depth (demonstrated in §4 — see the
precision accounting). C6: no protected structure invoked. C7: the statement
verified is P41 §32(ii) unchanged; the architecture changes the *tool*, not
the formulation. C8: `\mathcal R` is an analytic device; the YM measure is
never tilted; in Barandes-aligned terms the certified flow is bookkeeping on
the deterministic `SU(2)` pushforward law, exposing center variables only.

---

## 4. Executed Demonstration: Certified Window Crossing With Dimensional Transmutation

`V4P45-HIERARCHICAL-CERTIFIED-DEMONSTRATION`. Code:
`code/certified_window_crossing.py` (durable, dependency-light: `mpmath`,
`numpy` for the float diagnostic only).

The architecture stands or falls on one question: **can a certified
computation actually traverse a dimensional-transmutation window** — the exact
regime where Paper 44 §10 proved uniform methods fail — at sub-exponential
cost? This is testable *now*, in the one model that is (i) exactly
renormalizable so that (E) is trivial and (T) needs no remainder bound, yet
(ii) still has genuine transmutation: `SU(2)` lattice gauge theory on the
Berker–Ostlund hierarchical lattice, whose exact RG step is the
Migdal–Kadanoff recursion the corpus already used as a *float diagnostic*
(P41 §23, §25, §27). What was a diagnostic becomes here a certified theorem-
grade computation.

Crucially, confinement in this model is a **known analytic theorem**: K. R.
Ito proved permanent quark confinement for 4D hierarchical lattice gauge
theories of Migdal–Kadanoff type (PRL **55**, 558 (1985); `SU(N)` and
`U(N)`). The demonstration therefore claims no new physics statement; its
value is *calibration*: the certified-computation methodology is run against
a window whose answer has an independent analytic proof, and is shown to
cross it with explicit constants, machine-checked enclosures, and a
polynomial cost law — exactly the validation one wants before deploying the
method where no analytic proof exists. **[EST for the statement (Ito);
NEW for the certified method and cost law]**

### 4.1. The model and the exact step — [EXACT]

State: a positive class function `f=\sum_{n\ge1}c_n\chi_n` (`n=2j+1`,
`c_n\ge0`). One step (`b=2`, `d=4`):

```math
\text{bond moving } g=f^4\ (\text{pointwise; fusion in characters}),\qquad
\text{decimation } c'_n = n\,\Big(\frac{g_n}{n\,g_1}\Big)^{4}.
```

On the hierarchical lattice this recursion is **exact** (it is the model's
definition), positivity of `\{c_n\}` is preserved by both operations, and the
fundamental Wilson loop at level `k` obeys `\langle W\rangle\sim
(r_2^{(k)})^{A}` with `r_2=c_2/(2c_1)`, `A` the area in level-`k` plaquettes
(`4^k` bare plaquettes each). Initial data: the heat-kernel weight
`c_n=n\,e^{-t_0(n^2-1)/4}`, `t_0\approx 2/\beta_0`. Asymptotic freedom holds
on this line: the corpus proved the positive per-step decrement
(P41 §25 Proposition; `Δβ_{\rm MK}\to 1/4` per scale-2 step), so the flow
drifts logarithmically slowly through the window and the transmuted scale is
`e^{-O(\beta_0)}` — an essential singularity in `g^2`, present in the lab.

### 4.2. Lemma 45.X-h (exit basin with explicit constants) — [EXACT, proved here]

Let `\varepsilon=\big(\sum_{n\ge2}n\,c_n\big)/c_1` (normalized nontrivial
mass; tail included). Then one MK step gives

```math
\varepsilon'\;\le\;(\zeta(6)-1)\,(4\varepsilon)^4(1+\varepsilon)^{12}
\;=\;4.4398\,\varepsilon^4(1+\varepsilon)^{12},
```

and consequently, for `\varepsilon\le\tfrac15`:
`\varepsilon'\le 39.6\,\varepsilon^4\le 0.317\,\varepsilon` (the basin is
invariant and collapsing), `L_k=-\log\varepsilon_k` obeys
`L_{k+1}\ge4L_k-\log 39.6`, and the bare-unit string tension satisfies

```math
\boxed{\ \sigma_{\rm phys}\;=\;\liminf_k 4^{-k}\,\sigma_k\;\ge\;4^{-K}\Big(L_K-\tfrac{\log 39.6}{3}\Big)\;>\;0
\quad\text{whenever }\varepsilon_K\le\tfrac15\ \text{at some level }K. }
```

*Proof.* (1) Fusion positivity gives `(f^4)_1\ge c_1^4` (the all-trivial
channel) and the identity-mass factorization `(f^4)(\mathbb 1)=f(\mathbb 1)^4`
gives for the nontrivial mass `M_{\rm nt}(f^4)\le c_1^4\big[(1+\varepsilon)^4-1\big]
\le c_1^4\,4\varepsilon(1+\varepsilon)^3`. (2) For `g=f^4` and `m\ge2`,
`g_m\le M_{\rm nt}(g)/m`; decimation gives `m\,c'_m=g_m^4/m^2\le M_{\rm nt}(g)^4/m^6`
and `c'_1=g_1^4\ge c_1^{16}`, so
`\varepsilon'\le(\zeta(6)-1)\,(M_{\rm nt}(g)/g_1)^4\le(\zeta(6)-1)\,4^4\varepsilon^4(1+\varepsilon)^{12}`,
with `\zeta(6)-1=\pi^6/945-1=0.017343`. (3) At `\varepsilon\le1/5`:
`4.4398\cdot(1.2)^{12}=39.59`, so `\varepsilon'\le39.6\varepsilon^4\le0.317\varepsilon`.
(4) Telescoping `L_{k+1}\ge4L_k-\log39.6` from level `K`:
`4^{-k}L_k\ \ge\ 4^{-K}(L_K-\tfrac{\log39.6}{3})` for all `k\ge K`. Since
`2c_2\le M_{\rm nt}` gives `r_2\le\varepsilon/4`, `\sigma_k=-\log r_2^{(k)}\ge L_k`,
and a level-`k` plaquette is `4^k` bare plaquettes. With
`L_K\ge\log5=1.609>\tfrac{\log39.6}{3}=1.226`, the bound is positive. ∎

The basin `\{\varepsilon\le1/5\}` is **open**, and membership is decidable
from finitely many certified digits — exactly the (X) interface.

### 4.3. The certified engine — [EXACT by construction; implementation-grade]

Because both RG operations preserve coefficient positivity, the entire flow
can be certified in pure coefficient arithmetic with **no quadrature**:

- kept coefficients `n\le N` are outward-rounded intervals (`mpmath` interval
  context at working precision set per run);
- the tail `T\ge\sum_{n>N}n\,c_n` is an interval controlled by three exact
  facts: the mass balance `(fg)(\mathbb 1)=f(\mathbb 1)g(\mathbb 1)` for
  pointwise products; the bound `c_n\le T/n` (`n>N`) which inflates kept
  coefficients two-sidedly (undercount control); and the decimation tail bound
  `\sum_{m>N}g_m^4/m^2\le T^4/(5N^5)`;
- the initial heat-kernel tail has a closed-form rigorous bound.

So every printed digit of `\varepsilon_k` is a theorem-grade enclosure modulo
only the correctness of `mpmath`'s directed rounding and the implementation
(flagged honestly as implementation-grade; the algorithm is fully rigorous).

**The cost law (the demonstration's second finding — measured, including one
instructive failure).** Two distinct resources must scale with window depth,
and both were measured rather than assumed:

1. *Precision.* The step map is expansive (arithmetic sensitivity
   `\sim\times16` per step from `f\mapsto f^4` twice; measured enclosure-width
   growth `\approx2.0`–`2.4` digits/step including tail effects), so certified
   traversal of a `K`-step window needs `\Theta(K)` working digits.
2. *State-space size.* A first run with `N` sized to the weight's physical
   support **failed for `β₀\ge24`** — not from precision: the truncation-edge
   coefficients (`n\approx N`) necessarily carry `O(1)` *relative* enclosure
   widths (the tail bound is, by construction, the same size as the edge
   coefficients), and this edge contamination dilutes into the certified
   `\varepsilon` as a structural width seed `\sim10^{-0.078\,t_0N^2}` that no
   amount of precision removes, then amplifies per step until, past
   `O(1)`, the quartic decimation tail bound compounds double-exponentially.
   Diagnosing this (the certified mean still tracked the true flow to all
   digits; only the *enclosure* died) gave the requirement
   `0.078\,t_0N^2\gtrsim2K+{\rm margin}`, i.e. `N=\Theta(\beta_0)`. With `N`
   resized, the same rows certify with `\sim70` digits of recovered margin,
   exactly as the seed model predicts.

Since `K\approx7.9/t_0\approx4\beta_0`, total cost is **polynomial in `β₀`**
(steps `\times` state `\times` precision), while the scale being certified is
`e^{-c\beta_0}`. This is the log-refinement (Kondo) principle of P44 §10–11 in
its sharpest form: a per-decade-refining method pays *polynomially* per decade
where every uniform method pays *exponentially* — realized here as an actual
rigorous computation through an essential singularity, not as an analogy. The
edge-seed phenomenon is itself a portable lesson for Target 45.T: in any
certified RG, truncation boundaries inject width floors set by the *retained
state's* tail mass, so the state space must grow with the planned number of
steps — a quantitative design rule, not a surprise to be rediscovered in 4D.

### 4.4. Certified results — [EXACT modulo implementation]

`python3 code/certified_window_crossing.py` (float diagnostic agrees step-for-
step; certified table, basin `\varepsilon\le1/5`, Lemma 45.X-h bound):

```text
 t0      beta0   N    digits  K(cert)  eps_K(hi)   width(eps)  log4 sigma_phys >=   secs
 1       2       51   89      6        6.5805e-02  1.04e-72    -5.710                  1.0
 0.5     4       66   112     14       3.1631e-02  6.62e-77    -13.422                 3.0
 0.25    8       87   158     30       1.2655e-02  1.85e-81    -29.174                15.7
 0.125   16      141  248     61       1.8559e-01  1.95e-85    -61.563                67.4
 0.0833  24      206  341     93       1.6117e-01  1.60e-89    -93.369               317.2
 0.0625  32      271  434     125      1.2472e-01  1.02e-92    -125.113              646.8
 0.05    40      336  526     157      1.0762e-01  8.74e-92    -156.998             1385.8

transmutation fit (all 7 rows):  ln sigma_phys >= -11.06/t0 + 3.4
  1/t0 ~ beta0/2  =>  d ln sigma / d beta0 ~= -5.53
```

Every certified `K` equals the float-diagnostic `K` exactly, and every final
`\varepsilon_K` enclosure brackets the float value; the enclosure margins at
the basin are 72–92 digits.

Readings. (i) **The window is crossed, certifiedly, at every depth tried**:
from `β₀=2` (6 steps) to `β₀=40` (157 steps), the flow provably enters the
basin and Lemma 45.X-h converts basin entry into `\sigma_{\rm phys}>0` with an
explicit lower bound. (ii) **Transmutation is certified, not assumed**: the
certified `\ln\sigma_{\rm phys}` is linear in `β₀` with slope `≈-5.53` per
unit `β₀` (the hypercubic one-loop value is `-6\pi^2/11=-5.39`; the closeness
is the known MK scheme coincidence and is *not* claimed as a quantitative 4D
statement). The certified bounds span **~91 orders of magnitude** in
`\sigma_{\rm phys}`. (iii) Steps (`157`), state size (`336`), digits (`526`),
and runtime (`23` min for the deepest row) all scale linearly-to-polynomially
in `β₀`, confirming §4.3's cost law empirically — against an exponentially
shrinking target scale.

### 4.5. What the demonstration does and does not establish

```math
\boxed{
\begin{array}{l}
\textbf{DOES:}\ \text{(1) the (T)+(X) interfaces close end-to-end in a model with genuine}\\
\text{dimensional transmutation — finitely many certified steps + an open-basin lemma yield}\\
\sigma_{\rm phys}>0\ \text{through an essential singularity; (2) the cost is polynomial in window}\\
\text{depth (the certified Kondo principle); (3) the fixed-IR reading holds: at the fixed}\\
\text{physical block where the flow exits, the certified order parameter }r_2\ \text{is pinned in}\\
(0,\rho_*]\text{ uniformly along the trajectory — the hierarchical analogue of }1-|m(\eta)|\ge\delta_R.\\[2mm]
\textbf{DOES NOT:}\ \text{(1) say anything about the hypercubic lattice (bond moving is exact}\\
\text{only hierarchically); (2) cover }\beta_0=\infty\text{: the table reaches }\beta_0\le40\text{, and ``all }\beta_0\text{''}\\
\text{needs the weak-coupling entry lemma (Target 45.D below) — though each additional unit}\\
\text{of }\beta_0\ \text{costs only }\sim4\ \text{steps, }O(10)\ \text{digits, and }O(10)\ \text{retained characters, so any}\\
\text{finite depth is reachable; (3) replace 45.E/45.T for 4D, where the one-step map is not exact and the}\\
\text{remainder bound is the genuine engineering core.}
\end{array}}
```

**Target 45.D (hierarchical entry lemma) — [OPEN here; covered in substance
by Ito's analytic proof].** Prove an invariant weak-coupling neighborhood for
the MK map: for `t` below some `t_w`, the flow stays in a quantified
heat-kernel-like cone and `t` increases monotonically into the certified
range. The corpus's §25 decrement proposition is the on-the-line version;
what is missing in *this* framework is off-line stability — ordinary
perturbative RG work, no transmutation obstruction (the window *ends* where
the certification *begins*). The completed statement (hierarchical 4D
`SU(2)` confines for all `β₀`) is Ito's 1985 theorem; reproving its entry
lemma in certified form matters only as methodology practice for 45.E.

---

## 5. The 4D Program: Three Targets, One Order Of Attack

`V4P45-4D-PROGRAM`.

```math
\boxed{
\begin{array}{llll}
\text{target} & \text{content} & \text{technology} & \text{difficulty}\\\hline
\textbf{45.X} & \text{dressed-}Z_2\text{ Peierls/cluster basin + P40 closure} & \text{classical} & \text{paper-sized}\\
\textbf{45.T} & \text{certified one-step map on }\mathcal B_\kappa\text{ at }O(1)\text{ coupling} & \text{new engineering} & \text{the core}\\
\textbf{45.E} & \text{Balaban extraction to a compact }\mathcal K & \text{known-technology, expert} & \text{multi-year}\\
\end{array}}
```

Order of attack (and why):

1. **45.X first** (it is the cheapest and it *shapes* `\mathcal B_\kappa`):
   write the dressed-`Z_2` cluster expansion with extended tail-bounded
   couplings, extract the explicit basin threshold, and verify P40's closure
   consumes it. Deliverable: the open set `\mathcal X` with explicit
   constants.
2. **45.T on the dimensional ladder** (P41 §38 ordering, now with a sharper
   purpose): build the certified one-step map first for **3D `SU(2)`**, where
   super-renormalizability makes the entry interface elementary (polynomial
   running, no essential singularity in the UV handover) and the same
   dressed-`Z_2` localization applies (3D `Z_2` = Ising dual; P41 §40). A
   certified 3D crossing would already be a genuine new continuum confinement
   theorem and would debug every component of (T) — the activity
   representation, the remainder bounds, the `\varepsilon`-net — before the
   4D assault. The hierarchical demonstration (§4) is rung 0; 3D `SU(2)` is
   rung 1; 4D is rung 2.
3. **45.E last and in parallel** (it is independent of (T)/(X) details except
   for the norm): the precise demand on the Balaban corpus is not new physics
   but a *re-packaging theorem* — UV stability bounds imply total boundedness
   of the flowed action family in `\mathcal B_\kappa` at the window entry.
   This is where collaboration with constructive-QFT expertise is decisive.

**Relation to the `R^3\times S^1` frontier (P44).** Adiabatic continuity
(Step E there) is the *same* window in the `L` direction (P41 §45.3). The
E/T/X architecture applies verbatim with `L`-doubling as the step map; the
small-`L` semiclassical regime supplies the entry compactness (with a genuine
small parameter — the bion fugacity), which is *easier* than Balaban
extraction. A certified `L`-window crossing for the center-stabilized theory
is therefore a legitimate alternative instantiation of 45.E/45.T and the two
should be developed against the same (X) interface. **[NEW routing; OPEN]**

---

## 6. Falsification Ledger

- **(F1) Entry compactness fails:** if the flowed actions at fixed weak
  `g_*^2` do *not* remain in any compact `\mathcal K` as `a\to0`
  (delocalization of relevant directions), 45.E is false and the architecture
  dies at the handover. This is checkable in stages (norm growth of flowed
  activities in Balaban's bounds).
- **(F2) The window is dynamically deep:** if `\mathcal R^N(\mathcal K)`
  fails the basin check for all affordable `N` *and* the failure persists
  under net refinement, either the window endpoints were mischosen (move
  `g_{**}^2`, enlarge `N`) or — the genuine falsifier — the flow has an
  intermediate-coupling fixed point that blocks disorder, i.e. 4D `SU(2)`
  center order survives: confinement by this route is false. The
  architecture would then have produced *evidence against* center-route
  confinement, which is also decisive output (P41 §32.8).
- **(F3) Certified-step impossibility:** if the one-step remainder
  `\epsilon(A)` cannot be made smaller than the contraction margin at `O(1)`
  coupling for any blocking scheme (error bars exceed signal), 45.T is dead
  as engineering; the demonstration's margin accounting (§4.4: enclosure
  widths `10^{-72}`–`10^{-92}` against thresholds `O(10^{-1})`) is the
  existence proof that such margins are not intrinsically unreachable in
  transmutation windows.
- **(F4) Demonstration-level falsifiers:** an error in Lemma 45.X-h's
  constants, or a certified trajectory that fails to enter the basin at some
  deeper `β₀` (none found through `β₀=40`).

---

## 7. Honest Status, Novelty Flags, And Alignment

**Status ledger.**

```math
\boxed{
\begin{array}{ll}
\textbf{Proved here (unconditional):} & \text{Lemma 45.X-h (exit basin, explicit constants);}\\
& \text{Theorem 45.1 (conditional reduction, assembly).}\\[1mm]
\textbf{Computed here (certified, implementation-grade):} & \text{window crossing + }\sigma_{\rm phys}>0\\
& \text{bounds, hierarchical 4D }SU(2),\ \beta_0\in[2,40]\text{ (§4.4).}\\[1mm]
\textbf{Located, not proved:} & \text{45.E (Balaban extraction); 45.T (certified 4D step);}\\
& \text{45.X (dressed-}Z_2\text{ basin); 45.D (hierarchical entry).}\\[1mm]
\textbf{NOT proved:} & \mathsf H_{\mathrm{3sec}},\ \text{4D confinement, mass gap, }\sigma_{\rm phys}>0\ \text{(hypercubic).}
\end{array}}
```

**Novelty flags (web-checked, June 2026).**
(i) Hierarchical confinement is **known**: K. R. Ito, *Permanent quark
confinement in four-dimensional hierarchical lattice gauge theories of
Migdal–Kadanoff type*, PRL **55**, 558 (1985) — the §4 statement is his; the
certified-computation method, explicit basin constants, and cost law are this
paper's. (ii) Tomboulis's decimation program (arXiv:0707.2179) claimed a 4D
`SU(2)` confinement proof via MK-style interpolation between upper/lower
decimation bounds; published critiques (Ito–Seiler, arXiv:0711.4930; further
discussion arXiv:0803.3019) locate the gap in the interpolation step. The
E/T/X architecture replaces exactly that uncontrolled step with certified
computation — this is the clearest statement of what is new here. (iii)
Computer-assisted RG proofs (Koch–Wittwer for Feigenbaum; validated-numerics
proofs in dynamics and PDE) are the precedent class; their application to a
lattice-gauge transmutation window appears unstated in the literature.
**[(i)–(ii) verified; (iii) flagged, not exhaustively checked]**

**Why this is not an eighth disguise (C7).** The statement being targeted is
P41 §32(ii) verbatim; nothing is reformulated. What changes is the *standard
of evidence* inside the window: from "find a small parameter" (impossible
there, proved repeatedly) to "verify an open condition on a compact family at
finite precision" (possible in principle, demonstrated in the exact cousin).
The corpus's own meta-conclusion — stop reformulating, the core is bedrock —
is *accepted as input* and is precisely why a verification technology, rather
than another estimate, is the unique remaining move.

**Barandes/ISP alignment.** The certified RG is an analytic device on the
deterministic `SU(2)` pushforward law: no measure tilt, no hidden Markov
dynamics, no postselection (C8). ISP record structure enters only where it
always has in this corpus: the center variables that the certified flow
tracks are the ones the ISP boundary-record law exposes as primitive
(P40 §3); the architecture neither needs nor smuggles any further ISP
assumption.

**Capstone.**

```math
\boxed{
\begin{array}{l}
\text{The fixed-IR problem is a finite window with no small parameter. Every expansion}\\
\text{dies there; every protection is absent there; every inequality merely transports it.}\\
\text{What survives is verification: quarantine }a\to0\text{ into weak-coupling compactness (E),}\\
\text{cross the window by finitely many error-certified steps (T), land in an open basin}\\
\text{where disorder is classical (X). The demonstration shows the crossing is \emph{actually}}\\
\text{performable through a genuine essential singularity at polynomial cost. What remains}\\
\text{is engineering of a hard, finite, well-posed kind — not another search for a miracle.}
\end{array}}
```
