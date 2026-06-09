# Relativistic ISP V4 Paper 42: A Research Program For The Lattice Yang–Mills Bootstrap And A Viazovska-Style Modular Certificate

Author: Felix Robles Elvira

Date: 2026-06-01

Status: **research PLAN, not a proof.** This paper does not prove confinement, a
mass gap, or a string-tension lower bound. It is a careful, staged program for two
open targets identified at the honest terminus of Paper 41 (§§46–50):

- **Target I** — implement the 4D lattice **Makeenko–Migdal loop-equation SDP**
  (the "constrain, don't expand" bootstrap, native to order-one coupling);
- **Target II** — construct a **Viazovska-style modular certificate** that closes a
  string-tension lower bound and survives the continuum limit.

Neither target is solved here. Both are genuine research, with no guarantee of
success; Target II in particular contains a creative step of Fields-Medal
difficulty (Viazovska's analogous certificate for the far simpler sphere-packing
problem). The value of this paper is a *staged, self-checking* plan: every stage is
validated against a case with a known answer, so progress is verifiable and
failures are localized, and the genuinely-open step is isolated from the doable
engineering.

`V4P42-BOOTSTRAP-MODULAR-CERTIFICATE-PROGRAM`.

## Abstract

Paper 41 isolated continuum SU(2) confinement to one bedrock estimate
(self-generation of the scale = dimensional transmutation), showed it is invisible
to both weak- and strong-coupling expansions (the "wall"), and identified a *third*
tool — the loop-equation/positivity **bootstrap** — that operates at order-one
coupling without any expansion (§46). The bootstrap was validated on solvable cases
(one-plaquette to `10^{-10}`, 2D area law, 3D U(1) Jacobi-`\vartheta` structure;
§§47–49), its one novel claim — that the certifying object is **modular** — was
confirmed in the solved 3D U(1) case (§48), and a reproducible code base plus the
external recipe were recorded (§50, `code/`). This paper turns that recipe into a
concrete program: Part I, the lattice Makeenko–Migdal SDP and its staged
implementation and validation; Part II, the construction of a modular dual
certificate, staged from the solved 3D U(1) proof-of-concept to the open 4D goal.
A milestone ledger defines what counts as genuine partial progress independent of
the full (open) target.

## 0. Foundation (Paper 41, §§46–50)

The bootstrap brackets Wilson-loop observables using only exact relations and
positivity — no expansion, hence valid where the wall sits (`g^2\sim1`). Paper 41
established: the engine works (validated SDP, `code/lattice_bootstrap_scaffold.py`);
the convergence is governed by the *truncation order* (number of loop relations),
which in the continuum must grow with `1/a` (§49); and the dual certificate that
would make a bound continuum-stable is, in the one solved confining case (3D U(1)),
a modular `\vartheta` object (§48). This paper builds directly on that.

---

# PART I — THE 4D LATTICE MAKEENKO–MIGDAL LOOP-EQUATION SDP

`V4P42-PART-I-LATTICE-MM-SDP`.

## 1. Objective

Bracket the lattice string tension `\sigma_{\rm lat}(\beta)` for `SU(2)` from exact
loop equations plus positivity, and study its continuum behaviour
`\sigma_{\rm lat}/a^2` as `\beta\to\infty`. The make-or-break is a uniform-in-`a`
lower bound `\liminf_{\beta\to\infty}\sigma_{\rm lat}/a^2>0` (Paper 41, Phase 2).

## 2. Observables

- Single loops `W(C)=\langle\tfrac1N\operatorname{tr}\textstyle\prod_{\ell\in C}U_\ell\rangle`
  for a family `\{C\}` up to a size cutoff `L_{\max}`.
- The multi-loop moments needed for the positivity (Gram) blocks. Two regimes:
  - **large `N`** (master field): factorization `\langle W_iW_j\rangle=\langle W_i\rangle\langle W_j\rangle`
    makes the Gram matrix quadratic in single loops (Anderson–Kruczenski;
    Kazakov–Zheng) — a polynomial-matrix bootstrap;
  - **finite `N=2`** (the physical SU(2) case): multi-trace moments are independent
    variables, *and* SU(2) trace identities (`\chi_j` are polynomials in
    `\chi_{1/2}`, `\operatorname{tr}(AB)+\operatorname{tr}(AB^{-1})=\operatorname{tr}A\,\operatorname{tr}B`,
    etc.) give *extra* linear constraints — more constraints, tighter bounds.

## 3. The Lattice Makeenko–Migdal Loop Equations (Exact)

From invariance of the Haar integral under a left variation `U_\ell\to e^{i\epsilon T^a}U_\ell`
at a link `\ell\in C`, `\int\prod dU\,\mathcal L^a_\ell\big[W(C)e^{-S}\big]=0`, hence
`\langle\mathcal L^a_\ell W(C)\rangle=\langle W(C)\,\mathcal L^a_\ell S\rangle`. Using
the `SU(N)` completeness (Fierz) relation

```math
(T^a)_{ij}(T^a)_{kl}=\tfrac12\delta_{il}\delta_{kj}-\tfrac1{2N}\delta_{ij}\delta_{kl},
```

the result is the exact lattice loop equation, schematically

```math
\boxed{
\beta\!\!\sum_{p\,\ni\,\ell}\!\big[W(C\!\cup\!\partial p)-W(C\!\cup\!\partial \bar p)\big]
=\!\!\sum_{\substack{\text{self-intersections}\\ \text{of }C\text{ at }\ell}}\!\!
\Big[W(C_1)\,W(C_2)-\tfrac1N\,W(C)\Big],
}
```

the left side being deformation of `C` by the plaquettes touching `\ell` (the
lattice loop-space Laplacian / staples), the right side the **splitting** of `C`
into sub-loops `C_1,C_2` at points where it revisits `\ell` (the `\tfrac12\delta\delta`
Fierz term) minus the `\tfrac1N` trace term. This is an exact, *closed-as-a-hierarchy*
set of linear (large `N`: bilinear) relations. The precise lattice form and a
working `SU(2)/SU(3)` implementation are in **Kazakov–Zheng, "Bootstrap for lattice
Yang–Mills theory" (2024)**; the continuum origin is Makeenko–Migdal (1979).

## 4. Positivity

- **Reflection positivity** (Osterwalder–Seiler): for operators `O_i` supported on
  one side of a lattice reflection plane `\Pi`, `\langle\theta(O_i)\,O_j\rangle\succeq0`,
  where `\theta` is reflection. Loop operators crossing `\Pi` give a reflection-positive
  Gram block.
- **Moment positivity**: `\langle O_i^\dagger O_j\rangle\succeq0` for any loop-operator
  list. (Generalizes the one-plaquette moment + localizing matrices of §47.)

## 5. The SDP And Its Truncation

Variables: `\{W(C)\}` and the multi-loop moments, up to `L_{\max}`. Constraints:
the loop equations (§3) as equalities; the Gram blocks (§4) as `\succeq0`. Objective:
maximize/minimize the string-tension proxy `\sigma_{\rm lat}\approx-\tfrac1A\log W(\text{area }A)`
(or the torelon/Polyakov form). Truncation: keep loops up to `L_{\max}` and loop
equations up to a matching order; per §49 the *bracket tightens with the truncation
order*, so `L_{\max}` is the convergence control.

## 6. Staged Milestones (Dimensional Ladder, Each Validated)

```math
\boxed{
\begin{array}{ll}
\textbf{M1}& \text{2D }SU(2)\!: \text{reproduce the exact area law }\sigma=3/2\beta. \ \text{(self-check; cvxpy)}\\
\textbf{M2}& \text{3D }U(1)\!: \text{reproduce Göpfert–Mack confinement }(\sigma>0). \ \text{(cvxpy)}\\
\textbf{M3}& \text{3D }SU(2)\!: \text{bracket }\sigma\text{ vs Monte-Carlo (first non-abelian/no-Higgs).}\\
\textbf{M4}& \text{4D }SU(2)\text{ at fixed }\beta\!: \text{bracket }\sigma_{\rm lat}\text{ vs MC (reproduce/extend Kazakov–Zheng).}\\
\textbf{M5}& \textbf{Phase 2}\!: \text{scan }\beta\to\infty;\ \text{test }\liminf\sigma_{\rm lat}/a^2>0\ \text{uniformly.}
\end{array}}
```

M1–M2 are self-checks against known answers; M3–M4 are genuine computations with
external validation (lattice MC); M5 is the make-or-break.

## 7. Tooling

`cvxpy`+SCS/CLARABEL (open source) for M1–M3 (moderate precision suffices). For the
tight bounds of M4–M5, the arbitrary-precision **SDPB** (Simmons–Duffin) is required
— available via its official Docker image; `cvxpy` is interfaced for setup, SDPB for
the final solve. (Paper 41, `code/` holds the validated engine and the M1–M2 inputs.)

## 8. Risks And The Continuum (Phase 2, Make-Or-Break)

- **Infinite hierarchy / truncation**: the loop equations never close; one truncates
  at `L_{\max}`. Rigor of the truncated bound is standard (any feasible dual is a
  valid bound), but tightness requires growing `L_{\max}`.
- **The continuum race (the wall, in bootstrap form)**: as `a\to0` the relevant
  loops swell, so holding the lower bound on `\sigma_{\rm lat}/a^2` requires
  `L_{\max}\to\infty` with `1/a`. Whether a *fixed-rate* growth suffices is the open
  question; if it does not, no finite-truncation bootstrap closes Phase 2 — and the
  certificate of Part II is then the only route (a modular certificate is an
  *infinite* resummation by construction).
- **Precision**: near the PSD boundary the SDP is delicate; moderate-precision SCS
  fails already at `\beta=5` (§49), hence SDPB for M4–M5.

---

# PART II — A VIAZOVSKA-STYLE MODULAR CERTIFICATE

`V4P42-PART-II-MODULAR-CERTIFICATE`.

## 9. The Certificate Concept (Construct, Don't Search)

The dual of "minimize `\sigma` subject to loop equations (equalities) + positivity
(PSD)" is a **certificate**: dual multipliers `\lambda` for the loop equations and a
dual PSD matrix `Y\succeq0` for the positivity, such that a single inequality —
*dual feasibility* — implies `\sigma\ge\sigma_\star`. Numerically, SDPB finds an
approximate certificate. The Viazovska strategy is to **construct it exactly** from
modular data, so the bound is closed-form and, crucially, **continuum-stable** (a
finite-truncation numerical certificate degrades as `a\to0`; a modular one does
not, because modularity is exactly the continuum/scale symmetry).

## 10. The Viazovska Analogy, Made Precise

Sphere packing (Cohn–Elkies LP bound): a radial `f` with `f(0)>0`, `\hat f(0)>0`,
`f(x)\le0` for `|x|\ge r`, `\hat f\ge0` everywhere bounds the density; Viazovska
*constructed* the optimal `f` in `d=8,24` from weakly-holomorphic quasimodular forms
(Laplace transforms engineered so `f,\hat f` have the required sign pattern and
double zeros on the lattice). The Yang–Mills analog:

```math
\boxed{
\begin{array}{l}
\text{Construct a dual functional }\mathcal F=(\lambda,Y)\text{ on loop space, built from modular/}\vartheta\\
\text{forms, such that (i) it satisfies the bootstrap dual-feasibility inequality (Part I, §9),}\\
\text{(ii) it certifies }\sigma>0,\text{ and (iii) its modular transformation enforces continuum-}\\
\text{stable scaling so the bound survives }a\to0.
\end{array}}
```

The roles: Cohn–Elkies sign/zero conditions `\leftrightarrow` bootstrap dual
feasibility; Fourier self-duality `\leftrightarrow` the heat-kernel/`\vartheta`
modular transform (§30); lattice double zeros `\leftrightarrow` the loop-equation
kernel.

## 11. The Modular Structure To Exploit

From §§30, 48: the heat-kernel/Villain weight is a Jacobi `\vartheta_3` with
spectral coefficients `e^{-k^2/2\beta}`; Poisson summation is its modular transform;
the continuum limit is the modular cusp. The certificate ansatz is therefore a
combination of `\vartheta`-functions (and their quasimodular derivatives) in the
loop/area variable, whose modular weight is fixed by the dimension and whose `q`-
expansion matches the loop-equation hierarchy.

## 12. Staged Milestones

```math
\boxed{
\begin{array}{ll}
\textbf{A}&\text{3D }U(1)\!: \text{construct the certificate explicitly — re-express Göpfert–Mack's}\\
 &\text{monopole/sine-Gordon proof as a modular dual certificate. PROOF-OF-CONCEPT + template. (analytic)}\\
\textbf{B}&\text{2D }SU(2)\!: \text{the certificate is the heat-kernel }\vartheta;\text{ verify it certifies }\sigma=3/2\beta.\\
\textbf{C}&\text{Derive the exact dual-feasibility conditions the 4D certificate must satisfy}\\
 &\text{(from Part I §§3–5), and pose them as conditions on a modular form (Viazovska's "eigen-conditions").}\\
\textbf{D}&\textbf{Construct a modular form meeting condition C}\ —\ \textbf{the open, creative step.}
\end{array}}
```

Milestones A and B are genuinely achievable analytically (the answers are known;
the task is to *exhibit* the modular certificate). C is concrete derivation. **D is
the open bet** (§13).

## 13. The Open Creative Step (Milestone D) And Its Honest Risk

Milestone D — finding the modular form that satisfies the 4D dual-feasibility
conditions — is the genuine research, of the difficulty of Viazovska's original
construction (which solved a *simpler, known-answer* problem after years of effort).
Honest risks:

```math
\boxed{
\begin{array}{l}
\text{(i) Existence is not guaranteed: there may be no modular certificate that closes the 4D}\\
\quad\text{bound (the bootstrap bound itself might not reach }\sigma>0\text{ uniformly).}\\
\text{(ii) Non-abelian complexity: the loop-equation kernel is richer than Cohn–Elkies' Fourier}\\
\quad\text{condition; the required modular object may be vector-valued / higher-depth quasimodular.}\\
\text{(iii) Milestone D solving = proving 4D confinement = the Clay problem. No shortcut is implied.}
\end{array}}
```

## 14. Integration Of Parts I And II

Part I builds the SDP and, at each milestone, *outputs the numerical dual certificate*
(as in §49). Part II reads those numerical certificates (M2/M3) for their modular
structure (§48 confirmed it in 3D U(1)) and *constructs* the analytic modular
certificate (A,B) to be generalized (C,D). The two parts are complementary: the SDP
locates the bound and supplies the dual-feasibility target; the modular construction
supplies the continuum-stable closure the finite SDP cannot.

## 15. Milestone Ledger — What Counts As Progress

```math
\boxed{
\begin{array}{ll}
\text{M1, M2, B}&\text{self-checks (reproduce known 2D / 3D-U(1) results) — validate the program.}\\
\text{M3}&\text{3D }SU(2)\text{ bracket — a genuine new result (first non-abelian/no-Higgs bootstrap).}\\
\text{M4}&\text{tight 4D }SU(2)\text{ bracket at fixed }\beta\text{ — extends Kazakov–Zheng; publishable.}\\
\text{A}&\text{modular certificate for 3D }U(1)\text{ confinement — confirms the construction works.}\\
\text{M5 + D}&\text{the OPEN target: uniform-in-}a\ \sigma>0\text{ via a 4D modular certificate = confinement.}
\end{array}}
```

Each of M1–M4, A, B, C is a concrete, checkable deliverable worth completing on its
own; M5+D is the Clay-level goal and is not promised.

## 16. Honest Status And Non-Claims

This paper is a plan. It proves nothing about confinement and modifies no measure.
The bootstrap is a tool (constrain-don't-expand), validated in Paper 41; this
program would scale it (Part I) and attempt to close it continuum-stably (Part II).
Targets I and II are open research; Milestone D is of Viazovska/Clay difficulty and
may have no solution. The plan's worth is that it is **staged and self-checking** —
every step is validated against a known answer before the next — so that genuine
partial progress (M1–M4, A–C) is verifiable and the single open step (D) is
isolated, named, and not disguised as done.

## 17. Implementation Architecture For Target I (Committed Choices)

`V4P42-TARGET-I-IMPLEMENTATION-ARCHITECTURE`.

Concrete, committed engineering choices, optimized for a fast iteration loop
(LLM- or human-driven), easy access to the right libraries, exact/arbitrary
precision, and efficient solving — with the heavy specialized solver kept as a
swappable, pre-built backend so no compilation ever sits in the inner loop.

### 17.1. The Committed Stack

| layer | choice | why (fast-feedback / capability) |
|------|--------|----------------------------------|
| frontend language | **Python 3.10+** | no compile step → instant edit-run-inspect loop; largest, best-documented ecosystem for these tools; native unbounded `int` (BigInt by default) |
| exact coefficients | **`gmpy2`** (`mpq`, GMP-backed) | MM coefficients are rational (`½`, `1/N`, `β`); keep them exact through assembly → enables a later *rigorous* bound; far faster than `sympy.Rational` in bulk |
| arbitrary-precision floats | **`mpmath`** (frontend), **MPFR inside SDPB** (solve) | theta/heat-kernel checks and high-precision input generation (cf. Paper 41 §48 used `mpmath`) |
| dense/sparse linear algebra | **`numpy` + `scipy.sparse`** | vectorized assembly of the (sparse) loop-equation constraint matrix |
| combinatorial hotspots | **pure Python first; `numba` JIT only if profiled hot** | `numba` adds speed *without* a separate compile step, preserving the feedback loop; avoid C++/Rust in the inner loop |
| dev/validation solver | **`cvxpy` ≥1.5 + SCS / CLARABEL** | open source, `pip install`, moderate precision — instant iteration for M1–M3 (already validated, Paper 41 `code/`) |
| production solver | **SDPB** via its **Docker image** (`pmp2sdp`/`sdp2input` input) | arbitrary precision (GMP/MPFR), MPI-parallel — required for tight M4–M5; Docker means *no local C++ build* |
| optional pure-no-C++ solver | **`Hypatia.jl`** (Julia, arbitrary-precision conic) | fallback if a Docker-free arbitrary-precision path is wanted |
| tests | **`pytest`** | small modules, automated validation gates (M1/M2) → fast, localized correctness feedback |
| reproducibility | **venv + `requirements.txt`** (frontend), **Docker/Singularity** (SDPB) | matches Paper 41 `code/`; the only compiled artifact is a *pre-built* container |

### 17.2. Why Python, Not Julia/C++/Rust, For The Frontend

The inner development loop is *edit → run → inspect → fix*, repeated thousands of
times; the binding cost is **time-to-feedback**, not raw runtime of the frontend
(the runtime cost is the SDP solve, which is a separate pre-built binary). Python
wins decisively on time-to-feedback: no compilation, no JIT warm-up, the richest
library coverage, and BigInt built in. Julia is faster at steady state but pays a
JIT "time-to-first-result" tax on every fresh process and has thinner library/LLM
coverage; C++/Rust pay a full compile per change. Reserve compiled code for the
*solver only* (SDPB, which already exists — never rewrite it).

### 17.3. Arbitrary Precision — Fully Covered, No Custom Code

```math
\boxed{
\begin{array}{l}
\text{integers / counts / indices: native Python }\texttt{int}\ (\text{unbounded}).\\
\text{exact rational coefficients (MM, Fierz, }\beta)\!: \texttt{gmpy2.mpq}\ (\text{exact, GMP-fast}).\\
\text{arbitrary-precision floats (input gen, }\vartheta\text{ checks})\!: \texttt{mpmath}.\\
\text{the high-precision SDP solve}\!: \text{SDPB's internal GMP/MPFR (hundreds of bits).}
\end{array}}
```

Exact rationals are carried symbolically through assembly and converted to
high-precision floats only when writing the SDPB input — this is what keeps a
*rigorous* (not merely numerical) bound on the table.

### 17.4. Is A GPU Needed? — No (and why)

```math
\boxed{
\begin{array}{l}
\textbf{No GPU.}\ \text{The two costs are (a) the combinatorial frontend (loop enumeration,}\\
\text{canonicalization, sparse assembly) — irregular, integer/exact, \emph{not} a GPU workload;}\\
\text{and (b) the SDP solve — \emph{arbitrary-precision} (GMP/MPFR), which GPUs do not}\\
\text{accelerate (GPU BLAS is double precision; SDPB is CPU/MPI by design).}\\[1mm]
\text{The parallelism that matters is CPU: SDPB's MPI across cores, and the}\\
\text{embarrassingly-parallel }\beta\times L_{\max}\text{ scan as a Slurm job array across nodes.}
\end{array}}
```

A GPU would help only a hypothetical *double-precision* reformulation — which is
the wrong precision for tight bootstrap bounds. So GPU is overkill/irrelevant here.

### 17.5. Module Layout (Small, Independently Testable)

```text
loops.py         lattice loop = cyclic word of steps; canonicalization under the
                 hypercubic point group + translation + orientation; self-intersection.
mm_equations.py  the Makeenko-Migdal generator (the hard module): exact rational
                 (gmpy2.mpq) loop equations; unit-tested vs hand cases; THE correctness risk.
gram.py          moment/Gram + reflection-positivity blocks  M_k(x) = sum_i x_i B_{k,i}.
sdp.py           assemble variables + linear constraints (scipy.sparse) + PSD blocks +
                 objective; emit cvxpy model (dev) or SDPB input via pmp2sdp (prod).
solve.py         backend switch: cvxpy/SCS (dev)  |  SDPB-in-Docker (prod); read bound + dual.
scan.py          beta x L_max sweep (Slurm job array); post-process bounds + dual certificate
                 (the handoff to Part II).
tests/           pytest; gate on M1 (2D, sigma=3/2beta) and M2 (3D U(1)) before scaling.
```

### 17.6. Build Order And Gates

Prototype (Python+cvxpy, one-plaquette) is done (Paper 41 `code/`). Then: build
`loops.py` + `mm_equations.py`, **gate on M1/M2** (must reproduce known answers);
add `gram.py`/`sdp.py`, reproduce Kazakov–Zheng at fixed `β` (**M4 gate**); switch
`solve.py` to SDPB-in-Docker and run the `scan.py` continuum sweep (M5). Build the
large-`N` (master-field, polynomial) engine first (simpler), then specialize to the
physical finite `N=2` (more variables, but bonus SU(2) trace-identity constraints).

```math
\boxed{
\textbf{Committed:}\ \text{Python 3.10+ frontend (gmpy2 / mpmath / numpy / scipy / numba-if-hot)};\\
\text{cvxpy+SCS for dev, SDPB-in-Docker for production; pytest gates on M1/M2/M4; no GPU;}\\
\text{CPU parallelism (SDPB MPI + Slurm scan). Only pre-built compiled artifact: the SDPB container.}
```

## 18. Milestone Log (Results)

`V4P42-MILESTONE-LOG`.

### 18.1. M1 — 2D SU(2) Area Law: **PASS**

Executed (`code/milestone_M1_2d.py`, on the committed Python+cvxpy stack of §17).
2D structure (Migdal): a simple planar loop factorizes, `\langle W(A)\rangle=W_1^A`
with `W_1=\langle\tfrac12\operatorname{tr}U\rangle_{\rm plaq}=I_2(\beta)/I_1(\beta)`, so
`\sigma_{\rm lat}=-\log W_1`. The loop-equation + positivity SDP bootstrap brackets
`W_1`, and the area law follows:

```text
bootstrap W_1 (CLARABEL, J=2) vs exact I_2/I_1:
  beta=1:  W_1 = 0.240194  (exact 0.240194)   sigma_lat = 1.426309
  beta=2:  W_1 = 0.433127  (exact 0.433127)   sigma_lat = 0.836723
  beta=3:  W_1 in [0.567924,0.567929] (exact 0.567924)  sigma_lat ~ 0.56576
continuum trend  sigma_lat = -log(I_2/I_1) -> 3/(2 beta):
  beta: 2, 4, 8, 16, 32  ->  ratio sigma_lat/(3/2beta) = 1.116, 1.116, 1.063, 1.032, 1.016 -> 1
area law  <W(A)> = W_1^A  (beta=8):  -log<W(A)>/A = 0.199367 = sigma_lat for all A.
```

```math
\boxed{
\textbf{M1 PASS.}\ \text{The bootstrap reproduces the exact 2D }SU(2)\text{ area law:}\ \sigma_{\rm lat}=-\log W_1>0,\\
\text{matching }-\log(I_2/I_1)\text{ and }\to 3/(2\beta)\ \text{in the continuum. Machinery validated where}\\
\text{an area law provably exists; tight bounds at larger }\beta\text{ would need SDPB (§17).}
}
```

This is a self-check (2D is solvable), passed: it confirms the bootstrap yields an
area law of the correct value, and exercises the §17 stack end-to-end. Next gate:
M2 (3D `U(1)`, Göpfert–Mack confinement).

### 18.2. M2 — 3D `U(1)` (Göpfert–Mack): **REFERENCE ESTABLISHED; BOOTSTRAP RUN GATED**

Executed (`code/milestone_M2_3du1.py`). M2 is the first *genuinely* confining case —
unlike 2D, the area law is not a trivial factorization — and the honest verdict is
that it splits into an easy part (done) and the distinctive hard part (gated).

```text
(A) STRONG coupling, exact leading area law sigma_lat = -log(I_1/I_0) > 0:
      beta=0.5,1,2,5  ->  sigma_lat = 1.417, 0.807, 0.360, 0.113   (confining)
(B) WEAK coupling, the DISTINCTIVE part: monopole plasma (Polyakov/GM), sigma~exp(-c*beta):
      beta=2,4,8,16  ->  fugacity z~ 4.6e-5, 2.2e-9, 4.7e-18, 2.2e-35  => sigma>0 but exp. small
(C) contrast: 3D U(1) confines for ALL beta (monopoles); 4D U(1) DEconfines for beta>beta_c.
(D) the Villain weight is a Jacobi theta_3 (sec.48); the monopole/sine-Gordon dual is its
    modular transform -- the modular object a certificate would use (Part II, Milestone A).
```

```math
\boxed{
\begin{array}{l}
\textbf{M2 status (honest).}\ \textbf{Confinement reference established:}\ \text{3D }U(1)\text{ confines for all}\\
\beta\ (\sigma>0)\text{ — strong-coupling exact, weak-coupling monopole (GM) — distinct from 4D }U(1).\\[1mm]
\text{The EASY part (strong coupling, }\sigma\sim O(1)\text{) a bootstrap captures as in M1. The GENUINE}\\
\text{part — weak-coupling monopole }\sigma\text{ (exponentially small) — is the M2 \textbf{gate}: reproducing}\\
\text{it by bootstrap needs the abelian Makeenko–Migdal loop-equation module (Target I, module 2,}\\
\text{not yet built) and SDPB precision (to resolve an exp.-small }\sigma).\\[1mm]
\textbf{So M2 = reference + structure + modular connection DONE; the bootstrap run that}\\
\textbf{reproduces weak-coupling GM is the gated next implementation step.}\ \text{Not a clean PASS (unlike M1).}
\end{array}}
```

The honest lesson: 3D `U(1)` already shows, in miniature, why the program is hard —
the *interesting* confinement is non-perturbative (monopoles) with an exponentially
small `\sigma`, so even this "easier" abelian rung needs the real loop-equation
machinery + arbitrary precision to bootstrap, exactly the tools §17 commits to. The
modular structure (D) is why Part II's certificate is the natural closer here.

### 18.3. `mm_equations.py` — The Loop-Equation Generator: **BUILT + VALIDATED (abelian U(1))**

The Target-I module 2 (§17.5), flagged as *the* correctness risk, is built for the
abelian case and passes a hard correctness gate. Modules `code/loops.py` (lattice
geometry, 1-chain cycles, translation+orientation canonicalization, exact 2D fill)
and `code/mm_equations.py` (the U(1) Schwinger–Dyson generator of §3 plus cycle
enumeration and system assembly).

**Correctness gate (`code/test_mm.py`):** the generated U(1) loop equations must be
satisfied by the *exact* 2D solution `W(C)=\prod_p I_{w_p}(\beta)/I_0(\beta)`.
Result — for cycles {1×1, 1×2 (h/v), 2×2}, every link (including off-loop
deformation links), and `\beta=0.7,1.7,3.0`:

```text
GLOBAL max |residual| = 4.4e-16   ->   PASS
full system (Lmax=2, 2D): 39 distinct cycles, 310 equations, 285 loop variables,
max |residual| under the exact 2D solution = 4.4e-16  (consistent).
```

```math
\boxed{
\begin{array}{l}
\textbf{mm\_equations.py (U(1)): built and validated.}\ \text{The generated lattice loop equations}\\
\text{are satisfied by the exact 2D }U(1)\text{ solution to machine precision }(\sim\!10^{-16}).\\[1mm]
\text{This unblocks the \emph{genuine} M2 bootstrap run (abelian loop equations + positivity into the}\\
\text{SDP) and is the foundation for the non-abelian extension. \textbf{Honest scope:} only the abelian}\\
\text{U(1) generator is built; the SU(2) case adds the Fierz \emph{splitting} terms (§3), the documented}\\
\text{next step (needed for M3/M4).}
\end{array}}
```

The hard combinatorial module now exists and is correct (abelian); the remaining
implementation risk is concentrated in the non-abelian splitting terms, which the
same exact-solution gate (2D SU(2), M1) will validate.

### 18.4. Wiring `mm_equations` Into The SDP: **DONE + CORRECT; TIGHTNESS IS A SCALE PROBLEM**

`code/bootstrap_lattice.py` wires the validated loop equations into a genuine U(1)
SDP: variables `W(D)`; constraint `W(\varnothing)=1`; the loop equations as linear
equalities; and the abelian Gram positivity `M[i,j]=W(C_j-C_i)\succeq0` over a set
of test cycles (since `\langle O_{C_i}^\dagger O_{C_j}\rangle = W(C_j-C_i)`).

Run in 2D `U(1)` (exact answer `W(1\times1)=I_1/I_0` known), bracketing the plaquette:

```text
loop eqs (657-776) + Gram positivity, Gram windows 1,2,3, beta=0.7,1.5,3.0:
   W(1x1) bracket = [-1.000, 1.000]  (width 2.000) for ALL windows/beta;
   exact value (0.330, 0.596, 0.810) is ALWAYS contained (no violation);
   variable set capped at 900.
```

```math
\boxed{
\begin{array}{l}
\textbf{Wiring: done and correct.}\ \text{mm\_equations feeds the SDP; loop equations + Gram}\\
\text{positivity are active; the exact value is always contained (no violation), so nothing is wrong.}\\[1mm]
\textbf{But the bracket is trivial }([-1,1])\ \text{and does NOT tighten with the Gram size.}\ \text{Reason: the}\\
\text{loop equations couple }W(1\times1)\text{ to \emph{larger} loops that are not positivity-constrained in this}\\
\text{small/capped truncation, so the constraint does not propagate. Tightening requires a coherent,}\\
\text{large positivity structure (many loops) + arbitrary-precision SDPB — exactly the §17/§49/§50}\\
\text{scale-and-precision conclusion, here made concrete: a small }cvxpy\text{ bootstrap saturates at }|W|\le1.}
\end{array}}
```

So "wire `mm_equations` into the SDP" is **complete and correct**; obtaining a
*tight* bracket (the genuine M2 confinement test, and a fortiori 3D) is a
scale/precision problem — the moderate-precision, few-hundred-variable `cvxpy`
build is provably too weak, and the path to tightness is the SDPB-scale lattice
bootstrap of §17 (and Kazakov–Zheng). This is the honest state: the machine is
assembled end-to-end and correct; making it *tight* needs the HPC backend, not more
wiring.

### 18.5. Tightening Diagnostic: **The Positivity Propagates — Coverage, Not Structure**

Before committing to the SDPB backend, a cheap decisive test (`code/tighten_test.py`):
does a *coherent, point-group-reduced* variable set with a *richer* Gram (a
charge-power block `{0,P,2P,3P}` plus a spatial block of adjacent plaquettes)
tighten `W(1\times1)` below the trivial `|W|\le1` in 2D `U(1)`? Two ingredients
were added: full **point-group canonicalization** (`loops.canonical_full`,
hyperoctahedral group + translation + reversal — re-validated against the exact
2D solution, residual `4.4\times10^{-16}`), and **two Gram blocks** whose pairwise
differences stay in the variable set.

```text
2D U(1), point-group reduced, charge+spatial Gram (blocks 4x4, 6x6), ~279 vars, 205 eqs:
  beta=0.7: W(1x1) in [-0.515, 0.705]  width 1.22  (was 2.0)   exact 0.330
  beta=1.0: W(1x1) in [-0.618, 0.781]  width 1.40              exact 0.446
  beta=2.0: W(1x1) in [-0.781, 0.883]  width 1.66              exact 0.698
```

```math
\boxed{
\begin{array}{l}
\textbf{Diagnostic result: the positivity PROPAGATES.}\ \text{With a coherent point-group-reduced}\\
\text{variable set and charge+spatial Gram blocks, the bracket drops from the trivial width 2 to}\\
\text{1.2--1.7 (exact value contained, tighter at strong coupling). So the earlier trivial bracket was}\\
\text{a \textbf{coverage} problem (positivity not reaching the loops the equations touch), \textbf{not} a}\\
\text{structural gap — Wilson loops + positivity \emph{do} constrain }W\text{; no disorder operators needed to tighten.}\\[1mm]
\textbf{Consequence:}\ \text{the bootstrap demonstrably tightens; full tightness (toward the exact value) is}\\
\text{now a pure scale+precision push — more loops + arbitrary-precision SDPB — i.e. the SDPB-Docker}\\
\text{backend (§17) is the validated, de-risked next investment. (The bracket here is modest, not tight:}\\
\text{the lower bound is weak, wanting localizing-type blocks as in the one-plaquette case §47.)}
\end{array}}
```

This de-risks the whole Target-I program: the constrain-don't-expand machinery is
not only correct (§18.4) but *demonstrably tightening* (§18.5), so scaling it
(loops + SDPB) is worthwhile rather than speculative.

### 18.6. Gram Scaling Saturates: Tightness Needs Careful Setup + SDPB, Not Just More Loops

Pushing the Gram larger (`code/tighten_test.py`) gave a sobering, honest correction
to the naive "more loops ⇒ tighter" reading:

```text
2D U(1), W(1x1) bracket at beta=1.0 (exact 0.4464) vs Gram size:
  K=3, spw=1, Lcap=14:  width 1.3988   (279 vars)
  K=4, spw=2, Lcap=18:  width 1.3988   (1500 vars, capped)
  K=5, spw=2, Lcap=22:  width 1.3988   (1500 vars, capped)
```

The width is **identical to 5 digits** across a 5x growth in variables — the
Wilson-loop *moment* bootstrap **saturates** at width `~1.4`; adding more loops of
the same kind does not tighten it. (No bug: the loop-equation gate passed at
`10^{-16}`, the Gram is correctly PSD, the exact value is contained.)

```math
\boxed{
\begin{array}{l}
\textbf{Honest correction to §18.5.}\ \text{The bracket tightens from trivial (2.0) to }{\sim}1.4\ \text{once the}\\
\text{positivity covers the right loops — but then \textbf{saturates}: more Wilson-loop moment}\\
\text{positivity does not tighten further. So a \emph{tight} bound is \textbf{not} a casual scale-up; it needs}\\
\text{(i) a carefully engineered, coherent operator basis and loop-equation closure (the}\\
\text{Kazakov–Zheng-grade setup, which provably reaches tight bounds), plausibly (ii) localizing}\\
\text{blocks (the one-plaquette §47 ingredient), and (iii) arbitrary-precision SDPB. The "just add}\\
\text{loops" gain is exhausted at }{\sim}1.4.}
\end{array}}
```

Two further honest facts from this turn: the **Docker daemon was not running**, so
the SDPB backend could not be stood up here (it needs Docker Desktop started); and
the variable-set cap (1500) was being hit, so part of the saturation may also be
incoherent truncation — disentangling "needs better-engineered coherent basis" from
"needs SDPB precision/scale" from "needs new (disorder) operators" is the next real
diagnostic. The clean takeaway: **the simple bootstrap is correct and tightens
below trivial, but reaching a *tight* bound is genuine Kazakov–Zheng-grade
engineering + SDPB, not a one-parameter scale-up** — which is exactly the honest
boundary between what this exploration establishes and what the external-scale
program (§17, §50) must carry out.

### 18.7. SDPB Stood Up + Validated; The 1.4 Saturation Is **Structural, Not Precision**

With Docker started, the arbitrary-precision backend was stood up and the open
question of §18.6 — "is the `~1.4` saturation a precision wall (⇒ SDPB fixes it) or
a structural/operator-basis limit (⇒ SDPB cannot)?" — was settled **empirically**.

**Backend validated.** `bootstrapcollaboration/sdpb:master` (SDPB v3.1.0) pulled and
run. The PMP-JSON input format was reverse-engineered (no examples ship in the image)
and validated on a trivial SDP `max y s.t. [[1,y],[y,1]]⪰0`: SDPB returned
`y = 1.000…` to **78 digits** (`found primal-dual optimal`, gap `~10^{-30}`). The
format, now encoded in `code/sdpb_bootstrap.py`: all numbers are **strings**
(BigFloat); `polynomials[row][col][n]` is the coeff-list of entry `(row,col)` of the
`n`-th matrix; the solver maximizes `objective·y` s.t. `normalization·y = 1` and
`Σ_n y_n M_n ⪰ 0`.

**The decisive test.** The *same* 2D `U(1)` bootstrap SDP that cvxpy/SCS bracketed at
width 1.3988 (279 vars) was solved at **256-bit precision**. SDPB requires a
*non-degenerate* SDP (SCS regularizes through rank-deficiency; SDPB's exact
`Cholesky(Q)` refuses free or redundant dual directions — first a zero-diagonal `Q`
from unconstrained variables, then a non-HPD `Q` from redundant loop equations). The
SDPB-native fix is to **eliminate the linear constraints**: the loop equations
`A c = 0` and `c_empty = 1` cut the feasible set to an affine space, and the objective
+ Gram depend only on the relevant variables `S`, whose achievable values are an
affine hull `c_S = p_S + U w`. Feeding SDPB the reduced, non-degenerate SDP in the
**6 free variables** `w` (one PSD block per operator block, no equality blocks):

```text
2D U(1), beta=1, K=3,spw=1,Lcap=14  (full 279 vars, 205 loop eqs, Gram blocks [4,6]
  -> reduced to 6 free w)   exact W(1x1)=0.446390
SDPB(256-bit), found primal-dual optimal (gap ~1e-30):
  max W(1x1) =  0.78077641
  min W(1x1) = -0.61803399
  bracket width = 1.3988      (cvxpy/SCS on the same program: 1.3988)
```

The arbitrary-precision optimum is the **same bracket to 5 digits** as the
double-precision SCS one — and both endpoints are now *certified optima*
(primal–dual optimal, gap `10^{-30}`), not solver-tolerance artifacts. (Curiously the
lower endpoint is `-(\sqrt5-1)/2 = -0.6180339887…`, an exact algebraic number fixed by
the 6-variable reduced SDP.)

**Verdict (empirical): the Wilson-loop moment bootstrap's width-~1.4 saturation is
structural (operator-basis), not precision-limited.** SDPB at 256 bits, returning a
certified primal–dual optimum, reproduces 1.3988 exactly. A fixed convex program has a
solver-independent optimum, so arbitrary precision cannot shrink it. The tightening lever
is therefore the **operator basis / coherence + new (disorder) operators**, not the solver.
SDPB is validated infrastructure for the eventual *large coherent* system (its precision
**and** scale will matter there), with the `eliminate-then-positivity` reduction in
`code/sdpb_bootstrap.py` as the reusable (Kazakov–Zheng-style) scaffold.

This closes the §18.6 open question honestly: the SCS result was not loose, the
backend is not the bottleneck, and "just add loops / just add precision" is exhausted
at `~1.4`. The genuine next scientific step is the engineered coherent basis (and the
SU(2) Fierz extension, M3) — exactly the external-scale work (§17, §50).

### 18.8. M3 — SU(2) Fierz-Splitting Loop Equation **(DERIVED + VALIDATED to 1e-16)** + Coherent 2-Loop Block Design

**The non-abelian loop equation.** The Schwinger–Dyson identity from Haar-invariance,
`0 = (1/N) Σ_a ∫ L^a_{ℓ₀}[ tr(T^a U_{ℓ₀} M) e^{-S} ]` (weight `∝ exp[(β/N)Σ_p Re tr U_p]`,
`W=(1/N)tr`), produces three pieces for SU(2):

The SU(2) lattice Makeenko–Migdal equation (multiplied by 4N to clear fractions, giving
integer coefficients), with `contact`, `deformation`, and `Fierz split` terms:

```math
\boxed{\;
\underbrace{2(N^2-1)\,W(C)}_{\text{contact}} \;+\;
\underbrace{\beta\sum_{p\ni\ell_0} s_{p}\,[\,W(C+\partial p)-W(C-\partial p)\,]}_{\text{deformation}}
\;+\;
\underbrace{\sum_{\text{repeat }\ell_0}\big[\,2N^2\,\langle W(C_1)W(C_2)\rangle - 2\,W(C)\,\big]}_{\text{Fierz split}}
\;=\;0\;}
```

- **Contact** `= i C_F W(C)`, `C_F=(N^2-1)/2N`; the `−1/N` Fierz piece of the deformation
  **vanishes for SU(2)** because `tr U_p` is real (`tr U_p = tr U_p^†`).
- **Split**: at every *repeated* traversal of `ℓ₀`, `C` cleaves into the two arcs `C_1,C_2`
  between the two traversals — `⟨W(C_1)W(C_2)⟩` is a **two-loop correlator**, a new kind of
  variable. Which sub-loops result depends on the loop's **path ordering**, which the
  winding chain forgets, so loops are now ordered closed **walks** (`code/su2_loops.py`);
  `W`-values and deformations still reduce to chains.

**Validation (the correctness gate, `code/test_mm_su2.py`).** Against the exact 2D SU(2)
solution `⟨W(C)⟩=∏_p c_{|w_p|}`, `c_n=⟨½tr V^n⟩=[I_n-½(I_{n+2}+I_{|n-2|})]/((2/β)I_1)`:

```text
simple loops (contact+deformation, 17 loop/fwd-link pairs, beta=0.5..4):  |resid| <= 4e-16
doubled 1x1 (split -> identical plaquette, <W^2>=(1+c2)/2):               |resid| <= 9e-16
figure-8    (split -> two DISJOINT plaquettes, <WW>=c1^2):                |resid| <= 8e-16
```

So the contact coefficient `2(N²−1)=6`, the deformation β-coefficient, and the **bilinear
split coefficient `2N²=8`** are all correct. (Only forward-anchored, forward–forward splits
are emitted; forward–backward splits are documented, not yet emitted.)

**Coherent / localizing block design (`code/su2_bootstrap.py`).** The abelian saturation
(§18.7) is structural because the U(1) Gram `M[i,j]=⟨O_i^†O_j⟩=W(C_j−C_i)` collapses to
*single* loops. SU(2) is richer: loops do **not** add, so the Gram of loop operators is built
from genuine **two-loop correlators** `M[i,j]=⟨W(C_i)W(C_j)⟩` (position-dependent — canonicalized
as a **joint** pair, `canonical_pair`), and the split terms couple those `⟨WW⟩` back to single
loops. Two ingredients U(1) lacks:
1. **2-loop Gram block** — the coherent moment matrix in `⟨WW⟩`, fed by the splits.
2. **Pointwise localizing bound** — for SU(2) the fundamental character `W=½tr U ∈[−1,1]`, so
   every single and 2-loop variable lies in `[−1,1]` (a free localizing constraint).

A 2D probe (5 seed walks, Gram over `{1, W(1×1), W(1×2), W(1×1@(1,0))}`), brackets `W(1×1)`,
with a no-Gram control isolating the coherent block:

```text
beta   with-Gram bracket            width   no-Gram width   exact     Gram tightens by
0.5    [ 0.0105, 0.2083]            0.198   0.250           0.124     0.052
1.0    [-0.1070, 0.5000]            0.607   0.667           0.240     0.060
2.0    [-0.4078, 1.0000]            1.408   1.600           0.433     0.192
4.0    [-0.6891, 1.0000]            1.689   2.000           0.658     0.311
```

**Honest M3 status.** The SU(2) Fierz-splitting loop equation is *derived and validated to*
1e-16 (the correctness-critical core). The coherent 2-loop block *demonstrably tightens* the
bracket beyond the pointwise |W|≤1 bound (the "Gram tightens by" column, growing with β) —
the lever U(1) structurally lacks. At strong coupling the bracket is already tight (width 0.20
at β=0.5, vs the abelian 1.4); at weak coupling the small system still saturates near the
trivial +1, so *absolute* tightness needs the large coherent system + SDPB (§17/§50). The
⟨WWW⟩-weighted localizing block and forward–backward splits are the documented next pieces.
Still **not** a proof of confinement.

New durable code: `su2_loops.py` (walk representation + SU(2) loop equation + joint-pair
canonicalization), `test_mm_su2.py` (the M3 gate, PASS), `su2_bootstrap.py` (coherent 2-loop
assembler + no-Gram control).

### 18.9. Next Work (Prioritized)

Ordered by leverage; "engineering" = bounded + validatable, "research" = the open core.

1. **Walk-based closure (the decisive test; engineering). — DONE, see §18.10.** The §18.8
   probe *truncated* — it dropped every loop equation referencing a loop outside the seed set,
   which is why the weak-coupling bracket did not tighten. Close the loop/variable set: generate
   equations for the deformation loops too (deformations and splits realized directly as
   **walks**, so the self-intersection structure is unambiguous), iterating to a fixed order.
   Decisively answers: *does the coherent SU(2) design break the ~1.4 saturation?* **Result
   (§18.10): yes — the bracket tightens monotonically with depth, the opposite of the abelian
   flat saturation.**
2. **Wire the SU(2) bootstrap to SDPB (engineering).** Generalize the validated
   `eliminate-then-positivity` reduction (`sdpb_bootstrap.py`, §18.7) to the bilinear `⟨WW⟩`
   variables + the 2-loop Gram block — arbitrary precision + scale for the large coherent system.
3. **The ⟨WWW⟩-weighted localizing block (engineering).** The genuine localizing matrix — a
   positive loop operator (`1±W_p`, or a reflection-positivity sandwich) inside the Gram, needing
   three-loop correlators. The standard bootstrap sharpening ingredient.
4. **Forward–backward splits (engineering).** Currently only forward–forward splits are emitted;
   FB splits (a link traversed forward *and* backward in one loop) are needed for general loops.
   Derive like FF, validate against a backtracking 2D loop.
5. **Move to 4D (external scale).** The loop equation and block design are dimension-agnostic
   (`d` is a parameter); the real probe is whether the SU(2) coherent bootstrap exhibits an area
   law (`σ>0`) as the system scales. Compute + SDPB at scale.
6. **The continuum limit — the open core (research, NOT engineering).** A tight lattice bound at
   fixed `β` must have `σ>0` *survive* `β→∞` (dimensional transmutation — "the wall"). This is
   where Target II (the Viazovska-style modular certificate) must enter: a dual certificate stable
   under the continuum limit. Remains the open Clay-level problem; nothing in 1–5 closes it.

### 18.10. Walk-Based Closure: the SU(2) Coherent Bootstrap **Breaks the 1.4 Saturation**

> **Correction (see §18.11).** The numbers in this subsection use two provisional measures
> later found to be either incomplete or 2D-specific: (i) an **FB guard** that *skipped*
> forward–backward anchors (the FB split was not yet implemented), and (ii) keying variables by
> their **winding chain**, which silently assumes `⟨W⟩` is determined by the chain — true in 2D
> for the loops reached here, but **false in general** (self-overlapping loops have order-dependent
> holonomy). §18.11 implements the FB split (MC-validated) and switches to holonomy-faithful
> **walk keying**; the corrected, general-`d` bootstrap still breaks 1.4 and tightens monotonically
> but **more modestly** than the chain-keyed figures below — the sharp 2D numbers here partly
> reflect 2D-only loop-value coincidences. Read §18.11 for the corrected result.

Step 1 of §18.9, implemented in `code/su2_bootstrap.py`. A BFS over ordered **walks** closes
the system: the loop equation is generated for each loop *and* for the deformation/split loops
it produces, to a fixed depth + length cap. Two corrections were essential for correctness:

- **Loop-word reduction** (`reduce_walk`): the deformation surgery creates walks with adjacent
  backtracks `U_ℓ U_ℓ^{-1}`; removing them (chain-invariant, leaves `W` unchanged) eliminates
  degenerate walks (some reduce to the identity, `W=1`).
- **FB guard**: the forward-anchored equation (contact + deformation + FF split) is a valid
  identity *only* if the anchor link has no backward occurrence; forward–backward anchors need
  the unimplemented FB split, so they are **skipped** — every emitted equation stays a true SD
  identity. (Verified: the exact `c_1` is **contained** in every bracket below — the operational
  correctness check, since the equations are identities. NB: the naive `∏ c_{|w_p|}` evaluator is
  only valid for contiguous windings, so it cannot itself certify complex walks; containment can.)

**Result (2D, exact `W(1×1)=c_1`).** Closure (depth 3, Gram over `{1, W(1×1), W(1×2),
W(1×1@(1,0)), W(1×1@(0,1))}`), with a no-Gram control isolating the coherent block:

```text
beta   with-Gram bracket       width   no-Gram width   exact     contains exact?   Gram tightens
0.5    [+0.069, +0.169]        0.100   0.172           0.124     yes               0.072
1.0    [+0.086, +0.357]        0.272   0.383           0.240     yes               0.111
2.0    [-0.154, +0.819]        0.972   1.159           0.433     yes               0.187
4.0    [-0.531, +1.000]        1.531   2.000           0.658     yes               0.469
```

**Depth-scaling at beta=2 — the decisive contrast with the abelian flat saturation:**

```text
depth   singles   pairs   W(1x1) width
2       45        7       1.263
3       203       49      0.972
4       964       253     0.478     (CLARABEL hits its numerical limit just past here)
```

The bracket **tightens monotonically with depth** (1.26 → 0.97 → 0.48), whereas the abelian
moment bootstrap was *flat* at ~1.40 across a 5× variable growth (§18.6/18.7). So the coherent
SU(2) design — the genuine two-loop Gram fed by the Fierz splits, plus the pointwise `|W|≤1`
localizing bound — supplies a **scaling lever U(1) structurally lacked**, and it breaks the
saturation: at `β≤2` the bracket is already far below 1.40 and contains the exact value. Around
depth 4 / `β=4` the system (≈1000 singles, ≈250 pairs, ≈1500 equations) exceeds CLARABEL's
numerical reach — precisely the point where **step 2 (wire to SDPB)** becomes necessary for
arbitrary precision + scale. Still NOT a proof of confinement; this is the lattice, fixed-`β`,
2D validation that the coherent SU(2) bootstrap scales — the property the program needs before
4D and the continuum limit.

New durable code in `su2_loops.py`: `reduce_walk`, `has_backward_partner`, `canonical_walk`,
`su2_eq_walks`, `plaq_walks_through`; closure assembler + controls in `su2_bootstrap.py`.

### 18.11. FB Splits (MC-validated), the Walk-Keying Correction, and the SDPB Bridge

Steps 4 and 2 of §18.9. Two things here also force the honest correction flagged atop §18.10.

**Step 4 — the forward–backward (FB) split.** When the anchor link `ℓ₀` is traversed forward
and the *same* link is also traversed backward at `j`, the holonomy is `𝒪 = U_{ℓ₀} A U_{ℓ₀}^† B`
and the Fierz identity on `L^a(U_{ℓ₀}^†) = −i U_{ℓ₀}^† T^a` gives a term with the **opposite
signs** to FF (×4N): `−2N²⟨W(A)W(B)⟩ + 2 W(C)`, where `A`, `B` are the two arcs strictly between
the traversals (based at `x+μ` and `x`). Validated by a purpose-built **SU(2) Monte Carlo**
(`code/su2_mc.py`, quaternion links, Metropolis) — the gold standard, no analytic assumptions:

```text
loop                                   |residual| beta=1   beta=2     (MC noise floor ~ 0.01-0.04)
simple 1x1 (baseline, no split)            0.007       0.003
doubled 1x1 (FF split)                     0.041       0.005
lollipop x1 (FB, arc B empty)              0.016       0.025
lollipop x2 (FB, arcs = two disjoint plaq) 0.013       0.032
```

All residuals sit at the noise floor; a wrong FB sign would shift `lollipop x2` by
`16⟨W(A)W(B)⟩ ≈ 16 c_1²` (~0.9 at beta=1, ~3 at beta=2), vastly above what is seen. FB confirmed.

**The walk-keying correction (a real bug).** With FB added, the exact `c_1` was suddenly
**not contained** at small beta — a wrong (non-identity) constraint. Cause: variables were keyed
by their **winding chain**, but for a self-overlapping loop `⟨W⟩` is *not* a function of the chain
(holonomy is order-dependent: e.g. `tr(V_0 V_1 V_0 V_1) ≠ tr(V_0² V_1²)`). Chain-keying therefore
merged physically distinct loops into one variable, forcing a false equality that excluded the
true solution. FB produces exactly such loops, exposing it. **Fix:** key by canonical **walk**
(holonomy-faithful) — `skey`/`canonical_walk` for single loops, `pkey`/`canonical_walk_pair`
(shared translation + point group, each loop cyclic/reversal-folded) for the two-loop variables.
This is correct in **any** `d` (in 4D those loops genuinely differ). With walk-keying the exact
`c_1` is contained at every `beta`, and the corrected depth-scaling at `beta=2` is:

```text
depth   singles   pairs   W(1x1) width (walk-keyed, FF+FB, CLARABEL)
2       50        7       1.321
3       296       51      1.198
4       1908      285     1.112
```

Still **monotone tightening** below the abelian flat ~1.40, and the 2-loop Gram still tightens
beyond the pointwise bound — so the qualitative §18.10 conclusion (the coherent design supplies a
scaling lever U(1) lacks) **survives**. But the tightening is far **more modest** than the
chain-keyed figures of §18.10 (0.97→0.48): those leaned on 2D-only loop-value coincidences and are
not `d`-faithful. Honest net: the lever is real but, with this small operator set, weak — sharper
bounds need a larger coherent basis + localizing blocks (§18.9 step 3), not just depth.

**Step 2 — the SDPB bridge (`code/su2_sdpb.py`).** The validated eliminate-then-positivity
reduction (18.7) is generalized to the combined singles+pairs vector `z=(x;y)`: eliminate the
linear loop equations (`z = p + V w`, `w` free), and carry the 2-loop Gram and the pointwise
`1 ± z_k ≥ 0` bounds as PSD blocks in `w`. Two wiring fixes were needed (stale-checkpoint cleanup;
negate the `min` sense). Validated against CLARABEL at depth 2, `beta=2`:

```text
depth 2 (57 vars -> 32 free w)        bracket                width
  CLARABEL                            [-0.3546, +0.9662]     1.321
  SDPB 256b                           [-0.3361, +0.9662]     1.302   (certified, gap ~1e-30)
depth 3 (347 vars -> 136 free w)      bracket                width
  CLARABEL                            [-0.290 , +0.907 ]     1.198
  SDPB 256b                           [-0.2904, +0.9075]     1.198   (certified, gap ~1e-30)
```

At depth 2 the upper bound agrees to 5 digits and SDPB's certified `min = -0.336` corrects
CLARABEL's looser `-0.355` (the precision payoff); at depth 3 the two agree to ~3 digits. The
bridge is the validated path to push depth/`beta` past CLARABEL's numerical reach (≈1000+
variables). Still NOT a proof of confinement.

New durable code: `su2_mc.py` (SU(2) Monte Carlo), `test_mc_validate.py` (FF+FB MC gate),
`su2_sdpb.py` (SU(2) bilinear bootstrap → SDPB); `canonical_walk_pair`/`skey`/`pkey` and the FB
branch in `su2_loops.py`; `run_sdpb` checkpoint cleanup in `sdpb_bootstrap.py`.

### 18.12. Plan: Localizing Blocks → a String-Tension Bound (the decisive, non-circular push)

The bare 2-loop Gram is the *weak* form of the bootstrap and tightens only modestly (§18.11). The
decisive move is to add the one ingredient the method actually lacks and aim it at the real
observable, in the real regime — not to keep refining `W(1×1)` in 2D (a solved validation toy).

1. **Localizing blocks (the core missing ingredient).** Add localizing matrices
   `M^{\pm}_p[i,j] = ⟨W(C_i)(1 \pm W_p) W(C_j)⟩ \succeq 0` (positivity of the measure weighted by the
   pointwise-positive operator `1 \pm W_p`). Their entries are **two- and three-loop** correlators.
   The new capability this requires is the **product (2-loop) Schwinger–Dyson equation** — differentiate
   `⟨W(C)W(C')⟩` w.r.t. a link of `C`: it yields contact/deformation/split of `C` **times** the spectator
   `W(C')` (giving three-loop correlators `⟨W(C_1)W(C_2)W(C')⟩`) plus, when `C'` shares the link, a
   cross/merge term. That equation **constrains** the three-loop correlators the localizing blocks
   introduce. (First pass: `C'` not sharing the anchor link → no cross term; valid subset, already
   generates the three-loop structure.) MC-validate it like FF/FB before trusting it.
2. **String-tension objective.** Confinement is `⟨W(R×R)⟩ \lesssim e^{-σR²}`, so a rigorous *upper*
   bound on large Wilson loops is a *lower* bound on `σ` — the actual order parameter. Switch the
   objective from one loop to bounding the loop-size decay / a Creutz-ratio proxy.
3. **Target regime + go/no-go.** Code is dimension-agnostic. 2D is the **fast go/no-go**: with
   localizing blocks, does the machine drive the 2D bound to the *known exact* `σ`? If yes, the method
   demonstrably yields sharp confinement bounds and **4D SU(2)** is the genuinely new target (a rigorous,
   truncation-controlled lower bound on `σ`). If localizing blocks do **not** tighten 2D to exact, that
   is a decisive negative result about the relaxation — and we pivot rather than circle.

Honest scope: this yields a **fixed-`β` lattice** bound; the **continuum limit** (the wall) remains the
Clay-level core, untouched by any lattice bound, and is where Target II (the modular certificate) must
ultimately carry the program's novelty.

### 18.13. Result of §18.12 Step 1: the Naive 3-Loop Enrichment Is **Inert** (a decisive NO-GO)

Implemented and tested (`code/su2_products.py`, `code/su2_localizing.py`). The product (2-loop)
Schwinger–Dyson equation was derived — differentiating `⟨W(C)W(C')⟩` gives `⟨[single-eq(C)]·W(C')⟩=0`,
relating two- and three-loop correlators — and **MC-validated** (`su2_mc.py`, residual at the noise
floor, same as FF/FB). The localizing blocks `M^{\pm}_p[i,j]=⟨W(C_i)(1\pm W_p)W(C_j)⟩\succeq0` were
assembled on top. The 2D go/no-go (`W(1×1)` bracket, with vs without the 3-loop level):

```text
                  single-loop only    + product eqs + localizing block
depth 2, beta=1   width 0.471         0.471      (identical; exact 0.240, contained)
depth 2, beta=2   width 1.321         1.321
depth 3, beta=1   width 0.324         0.324
depth 3, beta=2   width 1.198         1.198
```

**The three-loop level changes nothing.** Two structural reasons, both real:
- The product equation is a *spectator-multiplied* single equation, so it only constrains three-loop
  correlators **among themselves and the two-loop**; it cannot feed back to the one-loop objective
  except through a positivity block.
- The localizing block is that positivity coupling, but its triples `⟨W(C_i)W_p W(C_j)⟩` are generated
  by a product equation only when a closure loop **splits** into `C_i` and `C_j` — possible only for
  *glueable* (link-sharing) operator pairs, never for disjoint ones. So the block stays largely free
  and imposes nothing.

```math
\boxed{
\begin{array}{l}
\textbf{NO-GO (naive form).}\ \text{Adding the next moment level (product SD equations + localizing}\\
\text{blocks) the obvious way does \emph{not} tighten the lattice Wilson-loop bound. Sharp bootstrap}\\
\text{bounds are not a casual "add the next level" — they need a fully \textbf{co-designed} operator set}\\
\text{whose loop equations cover \emph{every} positivity-block correlator (Kazakov--Zheng-grade), which}\\
\text{is a major build, not a quick win. The honest strategic read: the lattice-bootstrap line can}\\
\text{tighten only with heavy co-design, and even a sharp lattice bound never touches the continuum}\\
\text{limit (the wall). The program's leverage is more likely in \textbf{Target II} (the modular certificate}\\
\text{for the continuum limit) than in pushing lattice bracket widths down.}
\end{array}}
```

This is exactly the decisive fork §18.12 step 3 promised: localizing blocks did **not** drive the 2D
bound to exact, so — per the plan — we do **not** pour effort into 4D bracket-chasing. New durable code
(all MC-validated where applicable): `su2_products.py` (product equation + triple canonicalization),
`su2_localizing.py` (localizing-block assembler), general `products` interface in `su2_mc.py`.

## 19. Target II — The Modular Continuum Certificate

The §18 line establishes that lattice-bootstrap bounds, even sharp ones, never touch the continuum
limit (the "wall": dimensional transmutation, the essential singularity `e^{-c/g²}`). Target II is the
program's distinctive claim: a **dual certificate** of the loop-equation SDP that is a **modular form**,
hence continuum-stable. The object must be defined, not sloganeered; the steps:

- **Define the object.** The loop-equation SDP has a dual; a dual-feasible point — multipliers on the
  loop equations + PSD weights on the positivity blocks — is an explicit certificate proving an upper
  bound on a Wilson loop (a lower bound on `σ`). A *modular* certificate carries its coupling/spacing
  dependence in a modular form, so the modular `S`-transform (which swaps `a→0` and `a→∞`) makes the
  bound's positivity manifest in both limits — the exact Viazovska move (Fourier self-duality = the
  modular `S`-transform), giving a certificate that tracks the transmutation scale through the cusp.
- **Step 1 (DONE, §19.1):** construct the certificate explicitly in the solvable confining case
  (3D U(1), with the exact 2D anchor) and check it is modular — the go/no-go for the whole premise.
- **Step 2:** make the cusp = continuum-limit mechanism precise — how the modular form's `q→0` behavior
  produces the `e^{-c/g²}` essential singularity and tracks `Λ` (3D U(1) is the clean nontrivial test).
- **Step 3 (the frontier):** the non-abelian object — affine SU(2) (WZW) characters are modular forms
  (Kac–Peterson) and 2D YM / heat-kernel sums are q-deformations of them; determine whether an SU(2)
  certificate is built from affine characters and where the modular `S`-duality breaks (or does not).

### 19.1. Step 1 — the U(1) Confinement Certificate **IS Modular** (verified; `code/u1_modular_certificate.py`)

Constructed (not searched — Viazovska-style) and verified to machine precision:

```text
A. Villain weight  V_beta(phi)=sum_n e^{-(beta/2)(phi-2pi n)^2}  =  magnetic theta
   (1/sqrt(2 pi beta)) sum_m e^{-m^2/(2 beta)} e^{i m phi}      [Poisson = modular S-transform]
   max |electric - magnetic|                      = 2.2e-16     (EXACT)
   Jacobi:  theta3(e^{-1/(2 beta)}) = sqrt(2 pi beta) theta3(e^{-2 pi^2 beta})  [tau<->-1/tau]
   max relative mismatch                          = 4.1e-16     (EXACT)

B. 2D U(1) Villain -- EXACT certificate:  <W>(electric integral) = e^{-1/(2 beta)} (magnetic m=-1
   term), matched to 2e-16 at beta=0.5..5.  The area law is certified TERM-BY-TERM by the magnetic
   theta; sigma_2D = 1/(2 beta) (power law -- 2D confinement is "trivial").

C. 3D U(1) (Polyakov / Gopfert-Mack):  the SAME theta / S-duality sends the electric theory to a
   monopole Coulomb gas; sigma(beta) > 0 for ALL beta (rigorous, Gopfert-Mack), with an ESSENTIAL
   SINGULARITY.  The monopole fugacity  e^{-S0} = e^{-2 pi^2 v0 beta}  equals  q^{v0}  with
   q = e^{-2 pi^2 beta} the ELECTRIC NOME and v0 = 0.25273 the lattice Coulomb self-energy:
       beta    fugacity zeta      q^{v0} (cusp term)    |zeta - q^v0|/q^v0
       1       6.81e-03           6.81e-03              4e-16
       4       2.16e-09           2.16e-09              1e-15
   => the nonperturbative confinement scale IS the leading CUSP TERM of the electric theta.
```

```math
\boxed{
\begin{array}{l}
\textbf{Step 1 verdict: GO.}\ \text{The U(1) confinement certificate is a modular object (a theta}\\
\text{function). The modular }S\text{-transform IS the electric-magnetic (Poisson) duality; the area law is}\\
\text{certified term-by-term by the magnetic theta (exact in 2D); and the nonperturbative scale (the}\\
\text{essential singularity }e^{-c/g^2}\text{ in 3D) is the theta's CUSP term }q^{v_0}\text{. So a modular dual}\\
\text{certificate for confinement EXISTS and is constructed, not searched — the Viazovska principle is}\\
\text{realized for U(1). The continuum-stability handle is concrete: a modular form is fixed by its cusp}\\
\text{data, which is exactly the transmutation scale.}
\end{array}}
```

**Honest ledger.** EXACT/rigorous: the Villain–theta identity and Jacobi `S`-transform; the 2D
area-law certificate (`σ=1/(2β)`); `σ_3D>0 ∀β` (Göpfert–Mack, cited); the algebraic identity
`fugacity = q^{v₀}`. STANDARD-but-heuristic: the 3D dilute-gas prefactors for `σ(β)` (Polyakov values;
the *form* — `σ>0`, essential singularity — is the rigorous content). NOT yet done: Step 2 (the cusp
expansion as a continuum-limit *bound*, not just a scale match) and Step 3 (the non-abelian/affine
certificate — where literal Poisson summation is replaced by representation-theoretic modularity, and
the real obstruction lives). New durable code: `u1_modular_certificate.py`.

### 19.2. Step 3 — SU(2) **Is** Modular, but the Cusp-Confinement Link Does **Not** Transfer (the frontier, localized)

The non-abelian analog of the Villain theta is the SU(2) **heat kernel** on the group (= the 2D YM
heat-kernel weight), a class function of the angle `θ` with two representations related by Poisson
summation (`code/su2_modular.py`, verified to machine precision):

```text
spectral (irreps j, dim 2j+1, Casimir j(j+1);  n = 2j+1):
   K_t(theta) = (e^{t/4}/sin theta) sum_{n>=1} n sin(n theta) e^{-t n^2/4}
image / winding (geodesics on S^3 = SU(2), the coweight-lattice Poisson dual):
   K_t(theta) = (e^{t/4} sqrt(4 pi/t)/(t sin theta)) sum_{m in Z} (theta+2 pi m) e^{-(theta+2 pi m)^2/t}

   max |spectral - image| over (theta,t) = 1.8e-15      (EXACT non-abelian Villain/theta identity)
   underlying S-transform  vartheta(theta,t)=sqrt(4 pi/t) sum_m e^{-(theta+2 pi m)^2/t},  mismatch 4e-16
```

So **SU(2) IS modular**: its heat kernel is a Jacobi-theta-derived object and spectral↔winding is the
modular `S`-transform (`t ↔ (2π)²/t`) — the rep-theoretic version being the affine SU(2)`_k`
Kac–Peterson `S`-matrix. The 2D area law (`σ_fund = C₂(fund)/2 = 3/8` per unit coupling) is certified
by the spectral side — but, as in 2D U(1), this is the *trivial* (power-law, no essential singularity)
case.

```math
\boxed{
\begin{array}{l}
\textbf{Step 3 verdict: the modular object EXISTS for SU(2), but the U(1) cusp-confinement}\\
\textbf{mechanism does not transfer — and we can now say exactly why.}\ \text{(i) The U(1) magnetic}\\
\text{/monopole sum (whose cusp gave the 3D essential singularity) is here a \emph{geodesic-winding}}\\
\text{sum — geometric, not a charge/vortex gas. (ii) Genuine non-abelian confinement is 4D and}\\
\text{asymptotic-freedom-driven, }\Lambda\sim e^{-1/(2b_0 g^2)}\text{; whether that scale is a \emph{cusp term} of}\\
\text{the affine-character object is open. (iii) The Kac--Peterson }S\text{-matrix \emph{mixes} irreps}\\
\text{(Verlinde fusion), not a simple electric}\leftrightarrow\text{magnetic swap — the non-abelian magnetic}\\
\text{(center-vortex) side has \textbf{no literal Poisson dual}. Constructing that dual, and exhibiting}\\
\Lambda\text{ as its cusp datum, is the precise open problem Target II reduces to.}
\end{array}}
```

**Net of Target II so far.** The program's distinctive idea is now *defined and tested*, not a slogan:
a modular dual certificate for confinement **exists and is exact for U(1)** (Step 1), the essential
singularity literally **is** the theta cusp there, and **SU(2) carries the same modular `S`-structure**
(Step 3). What is genuinely open — and now sharply localized — is the **non-abelian magnetic dual**:
U(1) confinement rides on Poisson self-duality (electric↔monopole), but SU(2) has no literal Poisson
dual, so the center-vortex/`Λ`-scale sector needs its own modular description before a continuum-stable
non-abelian certificate can be constructed. That is the honest frontier, and it is a representation-
theory / number-theory problem (affine characters, Verlinde fusion, cusp data) — not another lattice
computation. New durable code: `su2_modular.py`. Still NOT a proof of confinement.

### 19.3. The Non-Abelian Magnetic Dual — Modular Data Verified, Open Core Made Precise (`su2_affine.py`)

Attacking the §19.2 frontier (the missing non-abelian magnetic dual). Two pieces, sharply separated
into *verified* and *open*.

**(1) The non-abelian modular DATA is concrete and exact.** Affine SU(2)`_k` characters carry an
`SL(2,ℤ)` representation via the Kac–Peterson matrices `S_{ab}=√(2/(k+2)) sin(πab/(k+2))`
(`a=2j+1`) and `T=diag e^{2πi(h_j-c/24)}`, `h_j=j(j+1)/(k+2)`, `c=3k/(k+2)`. Verified (`su2_affine.py`,
`k=1…16`): `S` symmetric + unitary, `S²=C=I` (SU(2) self-conjugate), `(ST)³=S²` up to the `c/24`
framing phase — all to `≤3e-15`. This is the rep-theoretic non-abelian `S`-transform, and it **mixes
irreps** (Verlinde fusion) — confirming it is *not* a simple electric↔magnetic swap.

**(2) The right magnetic dual is ’t Hooft's flux theta — exact in structure, open in dynamics.**
On `T⁴`, `SU(2)/ℤ₂` partition functions split into ’t Hooft fluxes `(e,m) ∈ ℤ₂×ℤ₂` (electric,
magnetic); the modular `S` of an embedded 2-torus swaps `e↔m`, and the flux sum is a finite `ℤ₂`
theta. This is the genuine non-abelian electric–magnetic modular duality (’t Hooft 1979) — the proper
analog of U(1) Poisson self-duality. It is **kinematic and exact**. Confinement is governed by the
*electric-flux free energy*, but those free energies are **4D dynamical** — no closed form.

```math
\boxed{
\begin{array}{l}
\textbf{Status: the modular machinery is in hand; the open core is now a precise conjecture.}\\
\text{The non-abelian }S\text{-transform exists (affine }S\text{-matrix, verified) and the magnetic dual is the}\\
\textbf{'t Hooft }\mathbb{Z}_2\text{ flux theta}\ \text{(exact). The remaining, genuinely open statement is:}\\[3pt]
\quad\textbf{Conjecture.}\ \text{the SU(2) string tension / electric-flux free energy is the \emph{cusp}}\\
\quad\textbf{datum}\ \text{of the flux theta, with }\Lambda\sim e^{-1/(2 b_0 g^2)}\text{ the cusp scale — exactly as the}\\
\quad\text{3D U(1) monopole fugacity was the cusp term }q^{v_0}\text{ in §19.1.}\\[3pt]
\text{This is 4D dynamics, unsolvable in closed form. It is NOT proved here and is NOT faked.}
\end{array}}
```

**Honest endpoint of Target II.** The program's distinctive idea has been carried as far as
construction and verification allow without solving an open problem: (a) the modular dual certificate
**exists and is exact for U(1)**, with the confinement scale = the theta cusp (§19.1, verified);
(b) **SU(2) carries the same modular `S`-structure** and the affine modular data is exact (§19.2–19.3,
verified); (c) the magnetic dual for 4D is identified (’t Hooft `ℤ₂` flux theta) and the open problem
is reduced to a **single precise conjecture** — `Λ` as its cusp datum. That conjecture is the genuine
research frontier: it requires the 4D non-abelian dynamics (the twisted free energies), which no
lattice or modular manipulation here resolves. We stop at the honest boundary rather than manufacture
a proof. New durable code: `su2_affine.py`.

### 19.4. Testing the Conjecture — the 't Hooft `ℤ₂` Flux Free Energy on the Lattice (`su2_thooft.py`)

The observable behind the §19.3 conjecture is the 't Hooft flux free energy. Measured directly by a
purpose-built SU(2) Monte Carlo (quaternion links; `d`-dimensional) with a `ℤ₂` twist (sign-flip on a
coclosed sheet of `(0,1)`-plaquettes), via **thermodynamic integration** (no reweighting overlap
problem): interpolate the sheet coupling `β→β(1−2λ)` and integrate
`F_m = ∫₀¹ β⟨Σ_sheet tr U_p⟩_λ dλ`. MC validated: `⟨½tr U_p⟩` reproduces the strong-coupling `β/4`
to ~1% (`0.097` vs `0.100` at `β=0.4`). The electric-flux free energy follows by `ℤ₂` Fourier,
`F_e = −log tanh(F_m/2)` — the genuine confinement order parameter (`F_e ≈ σ·area`).

```text
3D SU(2), L=4 (proof-of-concept):
   beta   F_m (magnetic twist)   F_e (electric flux)   't Hooft signal
   1.0    0.183                  2.393                 CONFINED  (F_e >> F_m)
   1.6    0.431                  1.550                 CONFINED
   2.2    2.739                  0.129                 ordered / deconfined-like (finite-V crossover)
```

The 't Hooft electric–magnetic **duality and confinement signal come out exactly right**: in the
confined (strong-coupling) regime the magnetic flux is nearly free (`F_m` small) while the electric
flux is costly (`F_e` large, a squeezed string); the roles invert at weak coupling (the `L=4`
finite-volume bulk crossover). The observable and the method work.

```math
\boxed{
\begin{array}{l}
\textbf{What this does and does not show.}\ \text{DOES: the 't Hooft }\mathbb{Z}_2\text{ flux free energy is}\\
\text{measured (validated MC + thermodynamic integration) and behaves as a proper confinement order}\\
\text{parameter (}F_e\text{ large / }F_m\text{ small when confined).}\ \textbf{DOES NOT: test the conjecture.}\\
\text{It is a small-lattice (3D, }L{=}4\text{) proof-of-concept; the crossover is finite-volume, 3D SU(2) is}\\
\text{super-renormalizable (no asymptotic-freedom }\Lambda\text{), and nothing here probes the \emph{modular/cusp}}\\
\text{structure. The §19.3 conjecture (}\Lambda=\text{cusp datum of the flux theta) remains OPEN -- neither}\\
\text{proved nor disproved. A real test needs large \textbf{4D} lattices, weak coupling, continuum scaling}\\
\text{of }F_e/\sigma\text{, and the modular analysis of the twisted free energies. The tooling now exists.}
\end{array}}
```

**Honest endpoint.** We have built and validated the genuine observable (`su2_thooft.py`: `d`-dim SU(2)
MC + 't Hooft twist + thermodynamic integration), shown it reproduces the 't Hooft confinement signal,
and thereby made the conjecture *operationally testable* — but the decisive test (4D, continuum,
modular cusp) is a real lattice campaign plus the open modular analysis, not a one-session computation.
The conjecture stands precisely stated and now equipped with its measurement apparatus. New durable
code: `su2_thooft.py`.
