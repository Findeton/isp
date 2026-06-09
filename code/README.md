# Bootstrap code for paper 41 (§§46–49)

Computational artifacts for the loop-equation / positivity **bootstrap** line of
`relativistic-isp-v4-paper41-fixed-ir-response-screening-continuation.md`.
These are the scripts that produced the numbers recorded in §§47–49. They are a
*new tool* (constrain-don't-expand), native to order-one coupling, with no
expansion around any configuration.

## Setup

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r code/requirements.txt   # cvxpy, numpy, scipy, mpmath
```
(In this workspace the env already exists at `../.bootstrap_venv`.)

## Scripts

| file | what it does | paper |
|------|--------------|-------|
| `oneplaquette_sdp_bootstrap.py` | genuine SDP one-plaquette SU(2) bootstrap: loop eqs + moment/localizing positivity; validation, truncation-convergence study, dual-certificate extraction | §47, §49 |
| `phase0_exact_checks.py` | 2D SU(2) exact area law `σ=3/(2β)`; 3D U(1) Villain weight = Jacobi `θ₃` (the Phase-1 modularity test, answered YES) | §48 |
| `lattice_bootstrap_scaffold.py` | general, correct SDP bootstrap **engine** (observables + linear loop-equation constraints + PSD Gram blocks), validated on the one-plaquette instance; the lattice case is the documented extension point | §49, §50 |
| `milestone_M1_2d.py` | **Milestone M1 (paper 42): 2D SU(2) area law — PASS.** bootstraps `W₁`, forms `σ_lat=−log W₁`, matches exact `−log(I₂/I₁)→3/(2β)`, exhibits `⟨W(A)⟩=W₁^A` | p42 §6, §18.1 |
| `milestone_M2_3du1.py` | **Milestone M2 (paper 42): 3D U(1) Göpfert–Mack — reference established, bootstrap run gated.** strong-coupling `σ=−log(I₁/I₀)>0`; weak-coupling monopole `σ~e^{−cβ}>0`; 3D-vs-4D contrast; theta/modular connection | p42 §6, §18.2 |
| `loops.py` | lattice geometry: 1-chain cycles, plaquette boundaries, translation+orientation canonicalization, exact 2D fill `W=∏I_{w_p}/I₀` | p42 §17.5 |
| `mm_equations.py` | **the loop-equation generator (Target I, module 2): abelian U(1) Schwinger–Dyson + cycle enumeration + system assembly.** validated | p42 §3, §18.3 |
| `test_mm.py` | **correctness gate: U(1) loop equations satisfied by exact 2D solution to ~1e-16 (PASS).** | p42 §18.3 |
| `bootstrap_lattice.py` | **mm_equations wired into a genuine U(1) SDP** (loop eqs + abelian Gram positivity `W(Cⱼ−Cᵢ)⪰0`). Wiring correct (exact value always contained); bracket trivial at small scale — tightness needs SDPB-scale | p42 §18.4 |
| `tighten_test.py` | **tightening diagnostic: point-group-reduced + charge+spatial Gram tightens `W(1×1)` below `|W|≤1` (width 2→1.2–1.7).** positivity propagates; obstacle is coverage, not structure → SDPB worthwhile | p42 §18.5 |

Expected key outputs (reproducible):
- one-plaquette SDP brackets the exact `m_{1/2}` to `~1e-10` at cutoff `J=2`;
- truncated-loop study: bracket width `0.65 → 0.095 → 0.014` as loop-order `K=2,3,4`;
- 3D U(1) weight matches `θ₃` to `~1e-18`.

## The external-scale step (Phase 2): what remains and how

The engine is correct and runs; the genuine *lattice* bootstrap needs two things
this environment does not have, and one piece of real research:

1. **An arbitrary-precision SDP solver — SDPB** (Simmons-Duffin), the standard
   bootstrap workhorse. It is **not** a pip package: it is a C++ build (GMP, Boost,
   Elemental, MPI), installed from source or via the official Docker/Singularity
   image. (Open-source moderate-precision SCS/CLARABEL, used here, suffice for
   validation but not tight 4D bounds — e.g. SCS already fails at `β=5`.)

2. **The lattice Makeenko–Migdal loop equations** (the research piece). Supply, to
   `lattice_bootstrap_scaffold.BootstrapProblem`:
   - observables = Wilson loops `W(C)` for a loop family (plus the independent
     multi-loop moments the Gram blocks need at finite `N`);
   - linear constraints = the lattice MM equations (Schwinger–Dyson on the links:
     deforming a link relates a loop to plaquette-appended loops and, at
     self-intersections, to products of sub-loops). See Makeenko–Migdal; and
     **Kazakov–Zheng, "Bootstrap for lattice Yang–Mills theory" (2024)** for the
     precise lattice form and a working SU(2)/SU(3) implementation;
   - Gram blocks = reflection-positive loop-correlation moment matrices;
   - objective = the string-tension proxy `σ_lat ≈ −log W(area)/area`.

3. **Phase 2 (make-or-break):** scan `β → ∞` and test whether the lower bracket on
   `σ_lat / a(β)²` stays positive *uniformly*. Per §49, the truncation **order**
   (number of loop equations / loop sizes) must grow with `1/a`; that growth, at
   the precision SDPB provides, is the truncation-vs-continuum race.

4. **Phase 3 (the bet):** rather than search for the certificate, *construct* the
   dual certificate from modular/`θ` data (Viazovska-style; §§30, 48), so it
   survives the continuum limit.

No 4D confinement is proved by any of this. The machinery is validated; the
remaining gap is scale (full lattice loop equations) and precision (SDPB), not the
existence of the method.
