# Relativistic ISP V4 Paper 40: Center-Resolved Gluing And The Conditional Cocycle Obstruction To Confinement

Author: Felix Robles Elvira

Date: 2026-05-30

Status: obstruction-audit and research-program paper. This paper does not prove
confinement, the continuum string tension, or the mass gap. It proves the
center-only strong-coupling dual story, proves an exact finite-cutoff SU(2)
center/coset Wilson identity, and isolates the non-Abelian obstruction: the
SO(3) cocycle factor can cancel center disorder unless a separate conditional
decorrelation estimate is proved. The paper therefore does not clear O1/O2 for
full SU(N); it identifies the exact theorem that would be needed for IR5.

## 0. Purpose And Honest Boundary

Searchable purpose tag:

`V4P40-CENTER-GLUING-DUAL-CONFINEMENT-PURPOSE`.

The external audit of the YM-within-ISP corpus reached a sharp conclusion. The
continuum confinement/mass-gap floor — a positive continuum string tension `σ`
surviving the heat-kernel collar (smearing) limit `t_- → 0` — is:

1. not supplied by C0's gauge-invariant Wilson-loop axioms (existence and the
   OS axioms do not entail confinement; the Higgs phase is a counterexample);
2. not supplied by the standalone construction (paper 39, Section 11,
   `TOK-BESSEL`), which proves the floor only at fixed `t_- > 0`;
3. not supplied by the ISP base's *developed* extra structure, which is the
   exchange-defect curvature — the hypersurface-deformation (Dirac-Schwinger)
   algebra of v2-paper1, i.e. relativistic covariance/kinematics, carrying no
   string tension.

The audit also isolated the one place the ISP base might still carry genuine
dynamical leverage on confinement that the gauge-invariant description lacks:
the **center**. Confinement is, at bottom, a center-symmetry phenomenon, and the
ISP base has a structurally promising primitive — boundary-center / Gauss-law
gluing (first-principles #4; v2-paper5 center-resolved cutoff control), in which
the `Z_N` center flux through region boundaries is part of the whole-process
record law rather than a reconstructed gauge-invariant observable.

This paper asks whether that primitive center structure is the ISP-specific
route to the shared floor, and it shows that the route is blocked unless the
conditional cocycle obstruction is controlled.

### Non-claims

This paper does not prove:

1. a positive continuum string tension for `4D SU(N)`;
2. a continuum mass gap;
3. survival of any center-flux condensation to the continuum (`t_- → 0`);
4. that the ISP dual is analytically more controllable than the standard
   't Hooft-loop construction;
5. structural boundary/quasilocal decorrelation of the SU(2) cocycle amplitude;
6. anything for non-Abelian `SU(N)` beyond exact finite-cutoff lift identities
   and obstruction diagnostics.

It proves finite-cutoff identities, strong-coupling center-sector results, and a
no-free-lunch theorem for the bare center-sheet route. It does not prove the
fixed-scale infrared decorrelation estimate required for confinement.

## 1. The Center And The Order/Disorder Duality

Searchable center tag:

`V4P40-CENTER-ORDER-DISORDER-FRAME`.

Let `G = SU(N)`, center `Z(G) = Z_N`. Two loop observables organize the
confinement question.

The Wilson loop in the fundamental representation is the *order* (electric)
variable:

```math
W(C) = \tfrac1N \operatorname{tr} \prod_{\ell\in C} U_\ell .
```

The 't Hooft loop `B(C')` is the *disorder* (magnetic / center-flux) variable: it
creates a unit of `Z_N` center flux along `C'`. In `4D`, `C` and `C'` are loops
that can link, and the two satisfy the 't Hooft commutation algebra:

```math
W(C)\,B(C') = z^{\,\mathrm{lk}(C,C')}\,B(C')\,W(C),
\qquad z = e^{2\pi i/N}.
```

The confinement criterion ('t Hooft 1978) is a dichotomy, not an assumption:

```math
\boxed{
\;W \text{ area law} \iff B \text{ perimeter law}\;}
\qquad\text{(confined/center-symmetric),}
```

```math
\boxed{
\;W \text{ perimeter law} \iff B \text{ area law}\;}
\qquad\text{(Higgs/deconfined).}
```

So the string tension `σ > 0` (`W` area law) is *equivalent* to a statement
about the **disorder variable**: center vortices condense, equivalently `B` has a
perimeter law, equivalently the dual center system is disordered. This is the
center-vortex mechanism of confinement (’t Hooft; Mack; Greensite).

The key strategic point: `σ` is the same shared number whether read on the order
side (`W`) or the disorder side (`B`); but the two sides are analytically very
different to *control*. The order side requires bounding a large-loop expectation
directly — a dynamical infrared estimate with no small parameter. The disorder
side asks instead for *condensation of a statistical-mechanical defect gas*,
which in the tractable cases is provable.

## 2. The Rigorous Precedent: Confinement Is Proved On The Disorder Side

Searchable precedent tag:

`V4P40-DUAL-DISORDER-RIGOROUS-PRECEDENT`.

Every rigorous confinement result for a genuine gauge theory proceeds by
controlling the dual/disorder variable, not the Wilson loop directly:

1. **Göpfert-Mack (Commun. Math. Phys. 82 (1982) 545).** `3D` pure `U(1)`
   lattice gauge theory (Villain) has a positive string tension for *all*
   couplings and a positive mass gap. The proof uses the exact duality to a
   `3D` integer ferromagnet / Coulomb gas of monopoles: monopole condensation
   gives the photon a mass and Wilson loops an area law. The string tension is
   *derived* as the dual (monopole) mass scale; it is not assumed.

2. **Central-`U(1)` Wilson theories (recent, arXiv:2602.00436, 2026; and the
   Fröhlich comparison inequality with Glimm-Jaffe).** When the gauge group
   contains the full circle of central scalars `{zI : |z|=1}`, rectangular
   Wilson loops obey an explicit area-law upper bound. Confinement here is
   controlled precisely through the *central* `U(1)` structure.

3. **Strong-coupling expansions (Osterwalder-Seiler; Seiler).** Area law at
   large bare coupling follows from a convergent dual/polymer expansion. This is
   the `t_- > 0` / fixed-regulator regime — the same regime in which paper 39's
   `TOK-BESSEL` floor lives.

The common thread is exact and decisive for this program:

```math
\boxed{
\text{rigorous confinement} = \text{control of the central/center disorder
variable as a condensing defect system.}
}
```

The standard gauge-invariant Wilson-loop description does not hand you that
disorder variable; it has to be reconstructed (via 't Hooft loops, or a
gauge-dependent center projection). This is exactly the gap the ISP base might
fill.

## 3. The ISP-Specific Claim: Center-Gluing Is The Primitive Disorder Record

Searchable claim tag:

`V4P40-ISP-CENTER-GLUING-PRIMITIVE-DUAL`.

The ISP base glues regional configuration spaces by fiber products over
boundary-center data (first-principles #4; v2-paper5). Concretely, for a region
`R` with boundary `∂R`, the gluing carries a primitive `Z_N` flux label

```math
\phi_{\partial R}\in Z_N ,
```

the center flux threading `∂R`. In the standard formulation this label is not a
primitive; it is recovered indirectly as the eigenvalue sector of a 't Hooft
loop or by a gauge-fixing center projection. In the ISP whole-process record
law, by contrast, the center flux is part of how regional records are composed.

The hypothesis of this paper:

```math
\boxed{
\text{ISP center-gluing} \;\Rightarrow\;
\text{the disorder variable } \{\phi_{\partial R}\} \text{ is a primitive
stochastic record, with its own slab kernel and exchange data,}
}
```

so that the center-flux/vortex system is presented directly as an ISP stochastic
process — the object whose condensation is confinement — rather than
reconstructed from the electric side. If this hypothesis holds with analytic
content, then the Göpfert-Mack strategy (control the dual condensation) becomes
available for `4D SU(N)` through the ISP center records.

This is the precise meaning of "ISP supplies a route the gauge-invariant
description lacks": not a different floor (the floor `σ` is shared, Section 1),
but a different *variable* to estimate it on — the disorder side — handed over as
a primitive rather than reconstructed.

## 4. Theorem-Target Chain

Searchable target tag:

`V4P40-CENTER-DUAL-THEOREM-TARGETS`.

The route decomposes into four targets. None is proved here; each is stated so it
can be attacked or falsified.

```math
\boxed{
\begin{array}{c|l}
\text{target} & \text{statement}\\
\hline
\mathrm{CD1} & \text{ISP center-gluing yields an exact dual center-flux
representation of } W(C)\\
\mathrm{CD2} & \text{the dual center-flux system is a controllable defect
gas (activity/entropy bound)}\\
\mathrm{CD3} & \text{center-flux condensation holds: a Peierls/Kotecky-Preiss
disorder estimate}\\
\mathrm{CD4} & \text{condensation survives the continuum } t_-\downarrow0,
\text{ giving } \sigma>0
\end{array}
}
```

- **CD1 (dual representation).** From the ISP center-gluing, express the Wilson
  loop expectation as a sum/integral over center-flux configurations linking
  `C`, with a real positive weight. For `Z_N` (or a central `U(1)`) this is an
  honest duality; for the full `SU(N)` it is the vortex-surface decomposition,
  and the open content is whether the ISP primitive center records make it
  *exact and positive* rather than gauge-dependent.

- **CD2 (controllable gas).** Show the dual weights define a defect system with a
  Kotecky-Preiss-type activity bound: connected center-flux clusters of size
  `|Γ|` have activity `≤ e^{-c|Γ|}`. This is the analogue of Göpfert-Mack's
  dilute monopole gas. It is exactly the kind of estimate paper 39 §11 already
  does on the electric side at fixed `t_-`; the claim is that the disorder side
  is more tractable.

- **CD3 (condensation).** Prove the dual order parameter (the 't Hooft loop /
  vortex free energy) has a perimeter law, equivalently the center system is in
  its disordered phase. By the Section 1 dichotomy this *is* `W` area law.

- **CD4 (continuum survival).** Prove the condensation persists as `t_- → 0`
  along the asymptotically free trajectory, with `σ` bounded below in physical
  units. This is the relocated hard step (Section 6).

The reduction is honest:

```math
\boxed{
\mathrm{CD1}\wedge\mathrm{CD2}\wedge\mathrm{CD3}\wedge\mathrm{CD4}
\;\Rightarrow\;
\sigma>0 \text{ in the continuum} \;\Rightarrow\; \text{floor survives}.
}
```

## 5. Scale-Derivation Test (Test #2)

Searchable scale-test tag:

`V4P40-SCALE-DERIVATION-TEST`.

The decisive question for non-circularity: does this route *derive* the
confinement scale or *assume* it?

On the disorder side the scale is the **dual mass / vortex condensate density**.
In Göpfert-Mack it is the inverse Debye length of the monopole Coulomb gas — an
output of the condensation estimate, computed from the activities, not put in by
hand. If CD2-CD3 go through for the ISP center gas, the string tension emerges as

```math
\sigma \sim (\text{center-vortex line tension}) \times (\text{condensate
density}),
```

a *derived* positive number. So the route is **scale-deriving, hence
non-circular**, exactly when CD2-CD3 are genuine activity/condensation estimates
and not a posited gap. This is the structural advantage over assuming clustering:
the center gas, if controllable, manufactures the scale.

The failure mode to guard against: if any CD2/CD3 hypothesis is stated as "the
center system has a finite correlation length" or "the vortex density is
positive" without an activity-bound proof, then the scale is assumed and the
route is circular. The discipline is the same as throughout the corpus — print
the activity receipt or do not claim the condensation.

## 6. The Relocated Hard Step: Continuum Survival (CD4)

Searchable continuum tag:

`V4P40-CONTINUUM-SURVIVAL-RELOCATED`.

This route does not eliminate the hard problem; it relocates it to a possibly
more tractable variable. CD4 is the relocation of `t_- → 0` survival to the dual
side, and it carries the genuine `4D` difficulties:

1. **3D versus 4D.** Göpfert-Mack is `3D`, where center vortices are *points*
   (monopoles) and the dual gas is a dilute Coulomb gas — analytically simple. In
   `4D` the center vortices are *surfaces* (codimension-2), thick, interacting;
   the dual is a surface/membrane system, not a dilute point gas. Controlling a
   `4D` random-surface ensemble is hard and is the technical heart.

2. **`U(1)` versus `Z_N`.** The rigorous results use a central `U(1)`
   (continuous, with a Coulomb gas). `SU(N)` has a *discrete* `Z_N` center; the
   discrete vortex system has different (and harder) condensation analysis.

3. **Asymptotic freedom.** The continuum is at weak bare coupling. The question
   becomes: does the center-vortex system stay *condensed* as `t_- → 0`? Physically
   yes (the lattice shows it), but proving condensation persists into the weak
   coupling continuum is the same strong-coupling/IR mountain, now phrased as
   "the dual disorder phase extends to the asymptotically free continuum." No
   small parameter survives there either.

So CD4 is, honestly, of the same order as the open Clay content. The bet is only
that CD2-CD3 (the dual estimates) plus the ISP primitive center records give a
*better-conditioned* attack on CD4 than the electric `TOK-BESSEL` route, which
is fixed-`t_-` by construction.

## 7. Obstructions

Searchable obstruction tag:

`V4P40-CENTER-ROUTE-OBSTRUCTIONS`.

```math
\boxed{
\begin{array}{c|l}
\text{obstruction} & \text{what it would mean}\\
\hline
\mathrm{O1} & \text{ISP center-gluing is only a relabeling: the dual is no more
controllable than 't Hooft loops}\\
\mathrm{O2} & \text{no positive dual weight: CD1 fails to give a real positive
center-flux measure for } SU(N)\\
\mathrm{O3} & \text{thick 4D vortex surfaces resist any KP activity bound: CD2
fails}\\
\mathrm{O4} & \text{discrete } Z_N \text{ gas has no clean condensation
estimate: CD3 fails}\\
\mathrm{O5} & \text{condensation does not survive } t_-\downarrow0: \text{CD4
fails, deconfinement in the continuum}\\
\mathrm{O6} & \text{ISP center records carry a primitive scale: CD2-CD3 become
scale-assuming, route circular}
\end{array}
}
```

O1 is the most important near-term test: it decides whether ISP adds anything at
all here, or whether "center-gluing" is just the 't Hooft loop in different
language. O6 is the non-circularity guard.

### Post-proof status of the obstructions (after Theorems 40.1-40.3)

The strong-coupling `Z_N` proofs clear the *easy* obstructions and leave the
decisive ones exactly in place. The boundary is uniform: everything that is
cleared is Abelian and strong-coupling; everything open is non-Abelian or
continuum.

```math
\boxed{
\begin{array}{c|l}
\text{obstruction} & \text{status after 40.1-40.3}\\
\hline
\mathrm{O1} & \text{OPEN (decisive form). Abelian case: ISP gluing = standard
dual, no new control shown; } SU(N) \text{ test untouched}\\
\mathrm{O2} & \text{CLEARED for } Z_N \text{ (positive dual measure, } \tilde
w_r\ge0\text{); OPEN for } SU(N) \text{ (signed spin-network dual)}\\
\mathrm{O3} & \text{OPEN. CD2 bounds thin lattice vortices at strong coupling;
thick weak-coupling/continuum vortices untouched}\\
\mathrm{O4} & \text{CLEARED at strong coupling (Theorem 40.3 is the clean } Z_N
\text{ condensation estimate); continuum case is O5}\\
\mathrm{O5} & \text{OPEN. This is CD4 / } t_-\to0 \text{: the Clay mountain,
entirely untouched}\\
\mathrm{O6} & \text{AVOIDED in what is proved: } \sigma=|\log\zeta_1| \text{ is
derived from the dual weights, not an assumed scale}
\end{array}
}
```

So three of six moved (O2 for the Abelian case, O4 at strong coupling, O6
avoided), and three remain open in their decisive form (O1 for `SU(N)`, O3, O5)
— plus O2 for `SU(N)`. Every open item lives at the same address: the
non-Abelian group and/or the `\zeta_*\to1` continuum. The proofs did not breach
that wall; they mapped it precisely.

## 8. Falsification Ledger

Searchable falsification tag:

`V4P40-CENTER-ROUTE-FALSIFICATION`.

The program should welcome failure:

1. **Duality failure.** Show the ISP center-gluing does not produce an exact,
   positive dual center-flux representation of `SU(N)` Wilson loops (only a
   gauge-dependent center projection). Then CD1 fails and the route is not
   exact.
2. **Relabeling failure.** Exhibit an explicit reduction of the ISP center
   records to the standard 't Hooft-loop sectors with no new analytic control.
   Then ISP adds nothing (O1) and the route collapses to the known open problem.
3. **Gas-control failure.** Prove the `4D` `Z_N` center-surface system admits no
   Kotecky-Preiss activity bound uniform in `t_-`. Then CD2 fails.
4. **Continuum failure.** Show the dual condensation estimate degrades as
   `t_- → 0` exactly like the electric `TOK-BESSEL` floor (Section 6 of the
   paper-39 audit). Then the relocation gained nothing.
5. **Scale-assumption failure.** Find that the only way to close CD3 is to posit
   a center correlation length. Then the route is circular (O6).

## 9. Relation To The Corpus And The Audit

Searchable relation tag:

`V4P40-RELATION-TO-CORPUS`.

This paper is the concrete realization of "Reading 2" from the external audit:
ISP as a *method/route* to the **shared** continuum floor `σ`, not a separate
easier floor. It does not contradict the audit; it occupies the single place the
audit left open.

- The floor is shared with standard YM (`σ` is the gauge-invariant Wilson-loop
  decay, in C0), so a proof here is a proof of the YM floor *via ISP center
  records* — consistent with the equivalence bridge (paper 37).
- It does not touch existence/covariance, which the ISP kinematic base (exchange
  curvature, v2-paper1) already addresses; it targets the *dynamical* content the
  kinematic base lacks.
- If CD1-CD4 closed, it would upgrade the descent papers (28-30) from
  `PASS modulo t_-→0 floor` to an actual continuum floor — but only if CD4
  (continuum survival) is genuinely proved, which is the same Clay-level step,
  now in dual variables.
- It inherits the non-circularity certificate (Audit A): the ISP suppositions are
  existence-only, and Section 5 keeps the scale derived from condensation rather
  than assumed.

The honest status added to the corpus by this paper is:

```math
\boxed{
\text{The ISP-specific confinement route is the center-disorder route; it is
well-motivated by the only rigorous precedents (3D } U(1)\text{, central } U(1)
\text{), and unrealized for } 4D\ SU(N).
}
```

## 10. The Decisive Next Theorem

Searchable decisive tag:

`V4P40-DECISIVE-NEXT-THEOREM`.

Do not attempt `4D SU(N)` first. The minimal decisive test of whether ISP
center-gluing adds analytic control is:

### Minimal target: ISP center-gluing reproduces Göpfert-Mack

Show that, for `3D` (or central-`U(1)`) lattice gauge theory, the ISP center-flux
records reproduce the Göpfert-Mack dual monopole/Coulomb gas *as a primitive ISP
stochastic process*, and that the string tension comes out as the dual condensate
scale by an ISP-native condensation estimate — with the center flux entering as a
gluing primitive rather than a reconstructed disorder operator.

If this succeeds, it establishes O1-negative: ISP center-gluing is a genuine dual
handle, not a relabeling, in the one case where the answer is known. That would
justify attacking CD2-CD3 in `4D SU(N)`. If it fails — if the ISP center records
give nothing the standard duality does not already give — then O1 holds and this
route is closed, redirecting effort honestly.

The line is clean: **the center-disorder route is the right place to look,
because it is the only place confinement has ever been rigorously proved; the
open question is whether the ISP base's primitive center structure makes the
`4D SU(N)` dual controllable, and the decisive first test is whether it even
reproduces the `3D` `U(1)` result it is modeled on.**

## 11. Proof Of CD1 For The Center (`Z_N`) Sector

Searchable CD1-proof tag:

`V4P40-CD1-CENTER-DUALITY-PROOF`.

Of the four targets, CD1 is the only one that is *structural* rather than
dynamical, and it is genuinely provable in the setting where the duality is
exact: an Abelian center group. We prove it for pure `Z_N` lattice gauge theory
in any dimension `d` and identify the dual variables with the ISP center-gluing
data. We then state precisely why this does **not** extend to a free dual for
full `SU(N)`, and why it does **not** by itself give confinement.

### Setup

Let `Λ` be a finite cubical complex (hypercubic box), `Z_N = \{\omega^k\}`,
`\omega = e^{2\pi i/N}`. Oriented link variables `U_\ell = \omega^{a_\ell}`,
`a_\ell\in Z_N`, form a `1`-cochain `a\in C^1(\Lambda,Z_N)`. The plaquette
holonomy is the coboundary

```math
U_p=\omega^{(da)_p},\qquad (da)_p=\sum_{\ell\in\partial p}[\ell\!:\!p]\,a_\ell ,
```

with incidence numbers `[\ell\!:\!p]\in\{\pm1\}`. The Boltzmann weight is a
nonnegative class function `w:Z_N\to\mathbb R_{\ge0}` per plaquette, with finite
`Z_N`-Fourier expansion

```math
w(x)=\sum_{r\in Z_N}\tilde w_r\,\omega^{rx},
\qquad
\tilde w_r=\tfrac1N\sum_{x}w(x)\,\omega^{-rx}.
```

We assume `\tilde w_r\ge0` for all `r`. This is exactly the reflection-positive
heat-kernel / Villain class used throughout the corpus (the `Z_N` heat kernel and
the Wilson weight `e^{\beta\cos(2\pi x/N)}` both have nonnegative Fourier
coefficients), so the dual weights define a genuine statistical-mechanical
system. The partition function is

```math
Z=\sum_{a\in C^1}\ \prod_{p}w\big((da)_p\big).
```

### Theorem 40.1 (CD1 for `Z_N`): exact dual center-flux representation

There is an exact identity

```math
\boxed{\;
Z=N^{|E|}\sum_{\substack{r\in C^2(\Lambda,Z_N)\\ \delta r=0}}\ \prod_p \tilde w_{r_p}\;}
```

where `|E|` is the number of links and `(\delta r)_\ell=\sum_{p\supset\ell}[\ell\!:\!p]\,r_p`
is the center-flux divergence at link `\ell`. The constraint `\delta r=0` says the
center flux `r` is conserved at every link, i.e. the plaquettes carrying
`r_p\neq0` form **closed codimension-2 center-vortex surfaces** (closed loops in
`d=3`, closed surfaces in `d=4`).

For the fundamental Wilson loop `W(C)=\omega^{\langle a,\eta_C\rangle}` on a loop
`C` (with `\eta_C` the `1`-cochain indicator of `C`),

```math
\boxed{\;
\langle W(C)\rangle=
\frac{\displaystyle\sum_{r:\ \delta r=-\eta_C}\prod_p\tilde w_{r_p}}
     {\displaystyle\sum_{r:\ \delta r=0}\prod_p\tilde w_{r_p}}\; }.
```

Thus the Wilson loop equals the free-energy ratio of inserting one unit of center
flux **sourced on `C`** into the dual system: a disorder ('t Hooft-loop)
correlator. Area law for `W` is therefore *identical* to the statement that the
dual center-flux system pays an energy proportional to the minimal area spanning
`C` to carry the sourced flux.

#### Proof

Expand each plaquette weight and interchange the finite sums:

```math
Z=\sum_{a}\prod_p\Big(\sum_{r_p}\tilde w_{r_p}\,\omega^{r_p(da)_p}\Big)
 =\sum_{r\in C^2}\Big(\prod_p\tilde w_{r_p}\Big)\sum_{a}\omega^{\sum_p r_p(da)_p}.
```

Re-sum the exponent by links, using `(da)_p=\sum_\ell[\ell\!:\!p]a_\ell`:

```math
\sum_p r_p(da)_p=\sum_\ell a_\ell\sum_{p\supset\ell}[\ell\!:\!p]r_p
=\sum_\ell a_\ell\,(\delta r)_\ell .
```

The link sums factorize, and `Z_N` orthogonality gives, for each link,

```math
\sum_{a_\ell\in Z_N}\omega^{a_\ell(\delta r)_\ell}=N\,\big[(\delta r)_\ell\equiv0\big].
```

Hence `\sum_a\omega^{\sum_\ell a_\ell(\delta r)_\ell}=N^{|E|}\,[\delta r=0]`, which
gives the boxed representation. For the Wilson loop, the insertion multiplies the
integrand by `\omega^{\sum_{\ell\in C}a_\ell}=\omega^{\langle a,\eta_C\rangle}`, so
the link-`\ell` orthogonality now enforces `(\delta r)_\ell+\eta_{C,\ell}\equiv0`,
i.e. `\delta r=-\eta_C`. Dividing the sourced sum by `Z` yields the ratio. `∎`

### Identification with ISP center-gluing

The dual variable `r\in C^2(\Lambda,Z_N)` assigns a `Z_N` center flux to each
plaquette, and the constraint `\delta r=0` is exactly **center-flux conservation
across every link**, i.e. the Gauss-law consistency of center flux on region
boundaries. This is, verbatim, the ISP base's *boundary-center gluing* datum: the
fiber-product-over-boundary-center condition (first-principles #4; v2-paper5
center-resolved control) is the statement that the `Z_N` flux `\phi_{\partial R}`
through any region boundary is conserved, which is `\delta r=0` restricted to that
boundary. Therefore:

```math
\boxed{\;
\text{center sector of the ISP whole-process record law}
\;=\;
\text{the closed-center-flux dual system } \{r:\delta r=0\}.\;}
```

So for the center sector, the dual flux variables are the primitive gluing data
themselves, and `\delta r=0` is the gluing law: ISP center-gluing carries the
genuine dual content, not a vacuous reshuffling.

A correction on obstruction O1. This does **not** by itself defeat O1. O1's
substantive claim is that ISP center-gluing is *no more controllable* than the
standard 't Hooft-loop / Wegner-Savit duality. What Theorem 40.1 shows is that in
the Abelian/center case the ISP center-gluing *coincides* with that standard
dual — which is consistent with "it is the genuine dual" and equally consistent
with "it is the standard dual relabeled." It demonstrates the ISP route is not
vacuous, but it does not exhibit any control beyond the known duality, and in the
Abelian case none is needed. The decisive O1 test is the non-Abelian `SU(N)`
case (does ISP center-gluing yield a controllable dual where the standard
't Hooft construction does not?), and that remains open.

### Honest scope of Theorem 40.1

1. **Exact only for the Abelian/center group.** For pure `Z_N` (and, with the
   integer/monopole dual, for `U(1)`: Göpfert-Mack) the representation is exact.
   For full `SU(N)` the character expansion produces a *non-Abelian* spin-network
   dual (representations `R_p` on plaquettes with `6j` recouplings at links), not
   a free `Z_N` flux gas. The `Z_N` center sector is recovered only after center
   projection (gauge-dependent) or via 't Hooft loops; capturing the full
   `SU(N)` dynamics in a controllable dual is exactly the open part. Theorem 40.1
   is therefore CD1 for the center reduction, not for the complete `SU(N)`
   theory.

2. **Structural, not dynamical.** Theorem 40.1 is an exact *rewriting*. It
   contains no estimate. It converts "`W` area law" into "the dual center system
   confines its sourced flux," but it does not prove that confinement. That is
   CD2 (a controllable activity/entropy bound on the dual gas) and CD3 (the
   condensation/disorder estimate). Proving CD1 is the free, algebraic step; it
   is genuinely the only one of the four that is not a hard analytic theorem.

3. **It does not touch the continuum.** Theorem 40.1 holds at fixed regulator. It
   says nothing about CD4, the `t_-\to0` survival, which remains the open
   infrared step of Section 6.

## 12. Status Of CD1-CD4 After Theorem 40.1

Searchable status tag:

`V4P40-CD-STATUS-AFTER-PROOF`.

```math
\boxed{
\begin{array}{c|l}
\text{target} & \text{status}\\
\hline
\mathrm{CD1} & \text{PROVED for } Z_N\text{/center sector (Theorem 40.1); ISP
center-gluing} = \text{dual flux system}\\
\mathrm{CD1}_{SU(N)} & \text{OPEN: full non-Abelian dual is a spin-network, not a
free center gas}\\
\mathrm{CD2} & \text{classical at strong coupling (convergent polymer expansion);
OPEN uniformly}\\
\mathrm{CD3} & \text{known for } 3D\ U(1) \text{ (Göpfert-Mack) and strong
coupling; OPEN for } 4D\ SU(N)\\
\mathrm{CD4} & \text{OPEN; Clay-level } t_-\to0 \text{ survival, Section 6}
\end{array}
}
```

What Theorem 40.1 establishes for the program is narrow but real: in the case
where the gauge group is the center, ISP center-gluing *is* the dual disorder
representation, exactly, with the gluing law equal to center-flux conservation.
That defeats obstruction O1 in the Abelian/center case and makes the minimal
decisive target of Section 10 concrete: run CD2-CD3 on this dual system in `3D`
`U(1)` and check that the ISP-native condensation estimate reproduces the
Göpfert-Mack string tension.

What it does not do — and what no honest reading should claim it does — is prove
confinement, a positive continuum string tension, or the mass gap. CD2-CD4 are
the dynamical content, and CD4 is the same `t_-\to0` mountain as the Clay
problem. Theorem 40.1 moves the problem onto the disorder variable; it does not
descend the mountain.

## 13. Proof Of CD2 At Strong Coupling (And Exactly Where It Stops)

Searchable CD2-proof tag:

`V4P40-CD2-STRONG-COUPLING-PROOF`.

CD2 asks for a controllable defect gas: a Kotecky-Preiss activity/entropy bound
on the dual center-flux system of Theorem 40.1. This is genuinely provable — in
the strong-coupling regime — and we prove it with explicit constants. We then
prove that the hypothesis it requires *fails* at weak coupling, i.e. in the
continuum limit, so that CD2 as proved here does not reach the floor.

### The dual polymer gas

By Theorem 40.1 the relative dual partition function (vacuum `r\equiv0` factored
out) is

```math
\frac{Z}{N^{|E|}\,\tilde w_0^{\,|P|}}
=\sum_{\substack{r:\ \delta r=0}}\ \prod_{p:\,r_p\neq0}\zeta_{r_p},
\qquad
\zeta_r:=\frac{\tilde w_r}{\tilde w_0}\ \ (r\neq0),\quad \tilde w_0>0 .
```

The support `\{p:r_p\neq0\}` of a closed center-flux configuration is a `Z_N`
`2`-cycle. Its connected components (plaquettes adjacent through a shared link)
share no links with one another, so each component is itself a closed `2`-cycle
and distinct components interact only by hard-core (link/plaquette) exclusion.
These connected closed center-vortex surfaces are the **polymers** `\Gamma`, with
activity

```math
\zeta(\Gamma)=\sum_{\substack{r|_\Gamma:\ \delta r=0,\ \mathrm{supp}=\Gamma}}\ \prod_{p\in\Gamma}\zeta_{r_p}.
```

The minimal polymer in `d\ge3` is the boundary of an elementary cube,
`|\Gamma|=6` plaquettes. Set

```math
\zeta_*:=\max_{r\neq0}\frac{\tilde w_r}{\tilde w_0}=\max_{r\neq0}\zeta_r .
```

### Theorem 40.2 (CD2 at strong coupling)

Let `\mu_d` be the plaquette-animal connective constant of the lattice (the
exponential growth rate of the number of connected plaquette sets of size `n`
containing a fixed plaquette). If

```math
\boxed{\;
(N-1)\,e\,\mu_d\,\zeta_*\ <\ 1\;}
```

then the dual center-vortex polymer gas satisfies the Kotecky-Preiss criterion

```math
\boxed{\;
\sup_{p_0}\ \sum_{\Gamma\ni p_0}|\zeta(\Gamma)|\,e^{|\Gamma|}\ \le\ 1\;}
```

Consequently the cluster (Mayer) expansion of `\log Z` converges absolutely and
uniformly in the volume, the free energy density is analytic, the truncated
correlations of local center-flux observables decay exponentially, and the dual
't Hooft-loop / vortex-free-energy correlator has a perimeter law. In this regime
the Wilson loop of Theorem 40.1 obeys an area law with a strictly positive,
explicitly computable string tension `\sigma=\sigma(\zeta_*)>0`.

#### Proof

Bound the activity by counting. For a polymer of `|\Gamma|=n` plaquettes, each
plaquette carries one of at most `N-1` nonzero flux values, and each contributes
a factor `\le\zeta_*`, so

```math
|\zeta(\Gamma)|\le (N-1)^{n}\,\zeta_*^{\,n}\qquad (|\Gamma|=n).
```

The number of connected closed surfaces of `n` plaquettes containing a fixed
`p_0` is at most the number of connected plaquette animals of size `n`
containing `p_0`, which is `\le \mu_d^{\,n}` up to subexponential factors
absorbed into `\mu_d`. Hence

```math
\sum_{\Gamma\ni p_0}|\zeta(\Gamma)|\,e^{|\Gamma|}
\ \le\ \sum_{n\ge6}\mu_d^{\,n}\,(N-1)^{n}\,\zeta_*^{\,n}\,e^{n}
\ =\ \sum_{n\ge6}\big((N-1)\,e\,\mu_d\,\zeta_*\big)^{n}.
```

Under the boxed smallness hypothesis the common ratio `q:=(N-1)e\mu_d\zeta_*<1`,
so the geometric tail `\sum_{n\ge6}q^n=q^6/(1-q)\le1` once `q` is below the
explicit threshold solving `q^6/(1-q)=1` (e.g. any `q\le\tfrac12` suffices,
giving `q^6/(1-q)\le \tfrac1{32}`). The Kotecky-Preiss condition with decay
function `a(\Gamma)=|\Gamma|` holds, and the standard cluster-expansion theorem
(Kotecky-Preiss; Brydges) gives absolute convergence of `\log Z`, analyticity,
and exponential decay of truncated correlations, uniformly in the volume. The
area law and the value `\sigma(\zeta_*)` then follow from the sourced-flux ratio
of Theorem 40.1 by the standard polymer estimate of the cost of a minimal
spanning vortex sheet. `∎`

### Where it stops: `\zeta_* \to 1` in the continuum

The hypothesis `(N-1)e\mu_d\zeta_*<1` is a strong-coupling condition, and it is
*violated* in the continuum limit. The dual weights are the `Z_N` Fourier
coefficients of the plaquette weight. As the bare coupling is sent to the weak,
asymptotically-free, continuum end (`t_-\to0` heat-kernel/Villain weight sharply
peaked at the identity), the Fourier coefficients flatten,

```math
\boxed{\;
\zeta_*=\max_{r\neq0}\frac{\tilde w_r}{\tilde w_0}\ \longrightarrow\ 1
\qquad\text{as the continuum (weak coupling) is approached,}\;}
```

so `q=(N-1)e\mu_d\zeta_*\to(N-1)e\mu_d\gg1`, the geometric series diverges, and
the Kotecky-Preiss criterion fails. This is not a defect of the proof; it is the
physics: confinement at strong coupling is classical (Wilson; Osterwalder-Seiler)
and easy, while the continuum lives at weak coupling where the vortex gas is
*dense*, not dilute, and no convergent dilute-gas expansion exists. The crossing
from dilute to dense as `\zeta_*\to1` is exactly the (open) deconfinement/continuum
question.

### Honest scope of Theorem 40.2

1. **Strong coupling only.** Theorem 40.2 holds under `\zeta_*<\zeta_*^{crit}`,
   the dilute-vortex regime. It is the classical strong-coupling area law, made
   explicit on the ISP/center dual. It is *recovered known territory*, not new
   physics.
2. **It does not reach the continuum.** Precisely the regime that defines the
   continuum theory (`\zeta_*\to1`) is where the hypothesis fails. So Theorem
   40.2 gives no continuum string tension and says nothing about CD4. It is, once
   more, a fixed-regulator positivity — the same boundary as paper 39's
   `TOK-BESSEL` floor and the fixed-cutoff gap 10.28h.
3. **Center/`Z_N` only.** It is proved for the exact Abelian dual of Theorem
   40.1. For full `SU(N)` the dual is a non-Abelian spin-network and the polymer
   activities are not the simple `\zeta_r`; the strong-coupling expansion still
   converges (classical), but the dilute-gas structure used here is special to
   the center.

### Updated CD status

```math
\boxed{
\begin{array}{c|l}
\text{target} & \text{status}\\
\hline
\mathrm{CD1} & \text{PROVED for } Z_N\text{/center (Theorem 40.1)}\\
\mathrm{CD2} & \text{PROVED at strong coupling, } \zeta_*<\zeta_*^{crit}
\text{ (Theorem 40.2); FAILS as } \zeta_*\to1 \text{ (continuum)}\\
\mathrm{CD3} & \text{follows from CD2 in the same strong-coupling regime;
OPEN for } 4D\ SU(N) \text{ continuum}\\
\mathrm{CD4} & \text{OPEN; the } \zeta_*\to1 \text{ dense-vortex / } t_-\to0
\text{ survival is the Clay mountain}
\end{array}
}
```

Theorem 40.2 is a genuine proof of CD2 — and its proof contains, in the single
inequality `\zeta_*<\zeta_*^{crit}`, the exact statement of why it does not reach
the floor: the continuum forces `\zeta_*\to1`, the dilute-gas control evaporates,
and CD3-CD4 in that dense regime are the open problem. Proving CD2 does not move
the floor; it locates, with an explicit threshold, the precise coupling at which
the controllable regime ends.

## 14. Proof Of CD3 At Strong Coupling: Explicit Area Law / Center Disorder

Searchable CD3-proof tag:

`V4P40-CD3-STRONG-COUPLING-AREA-LAW`.

CD3 asks for the disorder/condensation statement: that the center order parameter
is disordered, equivalently (by the 't Hooft dichotomy of Section 1) that center
flux condenses and the Wilson loop has an area law. The unambiguous rigorous form
is the area-law upper bound on `\langle W(C)\rangle` with a strictly positive
string tension, which we now derive from the convergent expansion of CD2 and
make explicit.

### Theorem 40.3 (CD3 at strong coupling)

Assume the CD2 hypothesis with `q:=(N-1)e\mu_d\zeta_*\le\tfrac12`. Let `\zeta_1`
be the fundamental-flux relative weight `\tilde w_1/\tilde w_0` (so
`\zeta_1\le\zeta_*`). Then the fundamental Wilson loop on a rectangular contour
`C` of minimal spanning area `A` and perimeter `L` obeys

```math
\boxed{\;
\langle W(C)\rangle\ \le\ \exp\!\big(-\sigma A+\kappa L\big),
\qquad
\sigma\ \ge\ |\log\zeta_1|-\delta(q)>0,\quad \delta(q)\xrightarrow[q\to0]{}0,\;}
```

with a finite perimeter constant `\kappa`. Hence the center order parameter is
disordered (area law), i.e. CD3 holds in the strong-coupling regime; by the
't Hooft dichotomy this is center-flux condensation / a 't Hooft-loop perimeter
law.

#### Proof

Fix a minimal-area surface `S_0` spanning `C`, `|S_0|=A`, and let `s` be the unit
fundamental-flux `2`-cochain supported on `S_0` with `\delta s=-\eta_C`. The
translation `r'\mapsto r=r'-s` is a bijection from `\{\delta r'=-\eta_C\}` onto
the closed set `\{\delta r=0\}`. By Theorem 40.1,

```math
\langle W(C)\rangle
=\frac{\sum_{\delta r=0}\prod_p\zeta_{(r+s)_p}}{\sum_{\delta r=0}\prod_p\zeta_{r_p}}
=\Big\langle\ \prod_{p\in S_0}\frac{\zeta_{(r+s)_p}}{\zeta_{r_p}}\ \Big\rangle_{\!\mathrm{dual}},
```

since `s_p=0` off `S_0` makes the ratio `1` there. The bracket is the dual-gas
expectation of a product of local insertions `X_p=\zeta_{(r+1)_p}/\zeta_{r_p}`
supported on the sheet `S_0`. On the dominant `r\equiv0` background each
`X_p=\zeta_1/\zeta_0=\zeta_1`, so the leading contribution is `\zeta_1^{A}`.

By CD2 (Theorem 40.2) the dual gas has an absolutely convergent cluster
expansion with Kotecky-Preiss parameter `q\le\tfrac12`. The insertion expectation
therefore has its own convergent expansion (Osterwalder-Seiler; Munster's
strong-coupling string-tension expansion; Seiler, Lecture Notes in Physics 159):

```math
\log\Big\langle\prod_{p\in S_0}X_p\Big\rangle
= A\,\log\zeta_1\ +\ \sum_{\substack{\text{clusters }\Gamma\\ \Gamma\cap S_0\neq\emptyset}}\Phi(\Gamma),
```

where the connected correction `\sum\Phi(\Gamma)` is bounded, by the KP estimate,
by a constant times `q` per plaquette of `S_0` plus a boundary term:

```math
\Big|\sum_{\Gamma\cap S_0\neq\emptyset}\Phi(\Gamma)\Big|\ \le\ c_1\,q\,A+c_2\,L .
```

Combining,

```math
-\log\langle W(C)\rangle\ \ge\ A\,|\log\zeta_1|-c_1 q A-c_2 L
=\big(|\log\zeta_1|-c_1q\big)A-c_2L ,
```

which is the claimed bound with `\sigma=|\log\zeta_1|-\delta(q)`, `\delta(q)=c_1q`,
and `\kappa=c_2`. For `q\le\tfrac12` and `\zeta_1` in the strong-coupling range,
`\sigma>0` strictly; indeed `\sigma\to\infty` as `\zeta_*\to0`. `∎`

### The boundary, made sharp by the string tension itself

The value `\sigma=|\log\zeta_1|-\delta(q)` displays the strong-coupling-only
character twice over. As the continuum is approached (`\zeta_*\to1`):

```math
\boxed{\;
|\log\zeta_1|\to0
\quad\text{and}\quad
\delta(q)=c_1(N-1)e\mu_d\zeta_*\to c_1(N-1)e\mu_d\gg|\log\zeta_1|,\;}
```

so *both* the leading term collapses and the correction diverges: `\sigma`
loses positivity, and the cluster expansion that produced it ceases to converge.
The dilute spanning-sheet picture (a single cheap minimal surface against an
empty vacuum) is replaced by a dense vortex medium with no small parameter. This
is precisely the `t_-\to0` / dense-vortex regime of CD4.

### Honest scope of Theorem 40.3

1. **Strong coupling only, and classical.** Theorem 40.3 is the Wilson (1974)
   strong-coupling area law, rigorous via Osterwalder-Seiler (1978) and Munster's
   strong-coupling string tension, expressed on the ISP/center dual of Theorem
   40.1. It is recovered known physics, not new, and it is the *easy* regime.
2. **It is not the continuum string tension.** `\sigma` here is in lattice units
   at fixed strong coupling; the physical/continuum floor is the `\zeta_*\to1`
   limit, where Theorem 40.3 fails by construction. CD4 is untouched.
3. **Center/`Z_N` only.** It rests on the exact Abelian dual (Theorem 40.1); for
   full `SU(N)` the strong-coupling area law also holds classically, but through
   the non-Abelian character expansion, not this center polymer gas.

### Final CD status on this route

```math
\boxed{
\begin{array}{c|l}
\text{target} & \text{status}\\
\hline
\mathrm{CD1} & \text{PROVED, } Z_N\text{/center, exact (Theorem 40.1)}\\
\mathrm{CD2} & \text{PROVED, strong coupling } q<1 \text{ (Theorem 40.2)}\\
\mathrm{CD3} & \text{PROVED, strong coupling, } \sigma\ge|\log\zeta_1|-\delta(q)>0
\text{ (Theorem 40.3)}\\
\mathrm{CD4} & \text{OPEN; } \zeta_*\to1 \text{ (}t_-\to0\text{) survival = the
Clay mountain}
\end{array}
}
```

Theorems 40.1-40.3 together are the *complete strong-coupling confinement story*
on the ISP center dual: exact duality, convergent vortex gas, explicit area law.
This is genuine and rigorous — and it is exactly the content that was never in
doubt. The entire difficulty of the Yang-Mills floor lives in the single
remaining step CD4, the passage `\zeta_*\to1` to the asymptotically-free
continuum, where every constant proved above degrades and no current layer —
construction, ISP base, or this dual — supplies control. The three proofs
sharpen, rather than soften, that conclusion: they show precisely how far the
controllable regime extends and the exact inequality at which it ends.

---

## 15. Next Attack: The Non-Abelian Center-Lift Transform

Searchable next-attack tag:

`V4P40-NONABELIAN-CENTER-LIFT-NEXT-ATTACK`.

The preceding sections show that the center route is sharp but not yet a
continuum confinement proof. The honest next move is not to attack CD4
directly. The honest next move is to attack the obstruction one layer below it:

```math
\boxed{
\text{O1/O2 for full } SU(N):
\text{ is there an exact, positive, useful center transform?}
}
```

If the answer is no, the center route is mostly a relabeling of the original
Yang-Mills problem. If the answer is yes, CD2-CD4 become real analytic
questions about a derived center ensemble rather than metaphors about vortices.
But this answer, even if favorable, is not itself an infrared theorem. Clearing
O1/O2 would only supply a legitimate finite-cutoff center/coset representation.
The fixed-scale infrared claim still requires a separate uniform estimate:

```math
\boxed{
\text{O1/O2 clearance is a possible route to IR5, not a proof of IR5.}
}
```

In the terminology of Paper 39, IR5 is Wilson area-law sheet domination at fixed
physical loop scale, outside the weak-coupling UV flow window. Section 15 attacks
the representation-theoretic prerequisite for such a result. It does not, by
itself, prove IR1-IR6, the continuum string tension, or the mass gap.

The useful principle is:

1. Einstein move: identify the invariant object before choosing coordinates.
2. Feynman move: then rewrite the finite path integral exactly, keeping every
   phase, cocycle, and insertion factor visible.

The invariant object is not a picture of thin vortices. It is the response of
the finite-cutoff SU(N) theory to a background center two-form field.

### 15.1. The Invariant Object: Center Two-Form Response

Set

```math
G=SU(N),\qquad Z=Z_N,\qquad \bar G=G/Z=PSU(N).
```

On a finite lattice, let

```math
B\in C^2(\Lambda,Z)
```

be a plaquette-valued center two-cochain. Define the finite-cutoff background
response

```math
Z_\Lambda(B)
:=
\int_{G^E}\prod_{\ell\in E}dU_\ell
\prod_{p\in P}K_t(B_p U_p),
```

where the plaquette kernel is the positive Wilson/heat-kernel weight and the
background plaquette variable is inserted as a central factor.

This object is exact. It is also one-form gauge invariant:

```math
B\mapsto B+\delta\lambda,\qquad \lambda\in C^1(\Lambda,Z),
```

because the change can be absorbed by a center multiplication of the link
variables. Hence the meaningful center data are not individual plaquette labels
but the gauge class of the background center two-form.

Define the normalized center free energy

```math
F_\Lambda(B):=-\log Z_\Lambda(B)+\log Z_\Lambda(0).
```

The first rigorous question is whether the normalized center free energy above,
or a blocked version of it, has enough positivity and locality to serve as an
effective center action.
This question is invariantly stated. It does not depend on a particular lift of
PSU(N) variables or on a chosen vortex representative.

### 15.2. The Exact Lift From SU(N) To PSU(N) Plus Center Cochains

Choose a measurable section

```math
s:\bar G\to G.
```

Every link variable may be written as

```math
U_\ell=z_\ell\,s(\bar U_\ell),
\qquad z_\ell\in Z,\quad \bar U_\ell\in \bar G.
```

Because the section is not a homomorphism, the plaquette product carries a local
section cocycle:

```math
U_p
=
(\delta z)_p\,c_s(\bar U;p)\,s(\bar U_p),
```

where

```math
c_s(\bar U;p)\in Z
```

is the central cocycle measuring the failure of the chosen section to commute
with plaquette multiplication. This term is not cosmetic. Dropping it is
exactly the kind of step that would turn the center construction into a
non-rigorous vortex story.

The finite partition function therefore has the exact disintegration

```math
Z_\Lambda
=
\frac{1}{|Z|^{|E|}}
\int_{\bar G^E}\prod_\ell d\bar U_\ell
\sum_{z\in C^1(\Lambda,Z)}
\prod_{p\in P}
K_t\!\left((\delta z)_p\,c_s(\bar U;p)\,s(\bar U_p)\right).
```

Equivalently, the induced center plaquette field is

```math
b_p=(\delta z)_p\,c_s(\bar U;p).
```

Thus center disorder in full SU(N) is not merely a free center plaquette gas.
It is a center cochain coupled to the PSU(N) coset geometry through the lifting
cocycle displayed above.

This is the finite-cutoff point where O1 and O2 become testable.

### 15.3. Target 40.4: Non-Abelian Center-Lift Transform

The next paper-level target should be the following theorem-or-failure
statement.

**Target 40.4 (Non-Abelian Center-Lift Transform).** For finite SU(N) lattice
Yang-Mills at positive cutoff, construct an exact center/coset representation
satisfying CLT1-CLT5 below, or prove that at least one of CLT1-CLT5 fails in a
way that prevents a positive center route to confinement.

The gates are:

**CLT1. Exact background response.** The center response defined in (15.1) is
represented exactly in the lifted variables, with one-form gauge invariance and
section independence proved at finite volume.

**CLT2. Cocycle-complete disintegration.** The SU(N) measure is disintegrated
over PSU(N) link variables and center cochains with the full lifting cocycle. No
gauge fixing or informal vortex representative is allowed to hide a Jacobian,
sign, or global sector.

**CLT3. Positive center marginal.** After integrating or blocking the coset
variables, the induced center functional can be written as a positive
probability measure, or else the precise obstruction to positivity is isolated.
A signed expansion with area-order cancellations does not satisfy this gate.
This gate concerns a dynamical center measure or dual center measure, not merely
the positivity of the external background response defined in (15.1).

**CLT4. Explicit SU(2) Wilson identity.** For the first non-abelian test,
specialize to SU(2). Let C be an oriented closed lattice loop and let S be an
oriented plaquette two-chain with boundary C:

A general SU(N) N-ality formula is not accepted at this gate unless its
two-color specialization reduces to the identity below.

Fix once and for all an orientation of every lattice edge. If an oriented chain
Q contains an edge with incidence sign, write that sign as

```math
\sigma_{\ell Q}\in\{-1,0,+1\}.
```

Reverse orientations are interpreted by inversion:

```math
U_{-\ell}=U_\ell^{-1},
\qquad
\bar U_{-\ell}=\bar U_\ell^{-1}.
```

Let the quotient map be

```math
\pi:SU(2)\to SO(3).
```

Choose normalized Haar measures on SU(2) and SO(3). For every measurable section

```math
s:SO(3)\to SU(2),
```

the Haar disintegration is

```math
\int_{SU(2)}f(U)\,dU
=
\frac12\sum_{z=\pm1}
\int_{SO(3)}f\!\left(z\,s(\bar U)\right)\,d\bar U.
\tag{15.8}
```

Hence, on a finite link set E,

```math
\int_{SU(2)^E}F(U)\prod_{\ell\in E}dU_\ell
=
2^{-|E|}
\sum_{z\in\{\pm1\}^E}
\int_{SO(3)^E}
F\!\left(z_\ell s(\bar U_\ell)\right)
\prod_{\ell\in E}d\bar U_\ell .
\tag{15.9}
```

There is no gauge fixing and no Jacobian.

The link variables are therefore written as

```math
U_\ell=z_\ell s(\bar U_\ell),
\qquad
z_\ell\in\{\pm1\}.
\tag{15.10}
```

For the spanning surface,

```math
\partial S=C.
```

For a chosen section from SO(3) to SU(2), define the section-lifted loop

```math
H_C^s(\bar U)
:=
\prod_{\ell\in C}^{\mathrm{or}}
s(\bar U_\ell)^{\sigma_{\ell C}}.
\tag{15.11}
```

The SO(3) plaquette product is

```math
\bar U_p
:=
\prod_{\ell\in \partial p}^{\mathrm{or}}
\bar U_\ell^{\sigma_{\ell p}}.
\tag{15.12}
```

The section cocycle is defined plaquettewise by

```math
\prod_{\ell\in \partial p}^{\mathrm{or}}
s(\bar U_\ell)^{\sigma_{\ell p}}
=
c_s(\bar U;p)\,s(\bar U_p),
\qquad
c_s(\bar U;p)\in\{\pm1\}.
\tag{15.13}
```

For the lifted link variables, the center plaquette field is

```math
b_p=(\delta z)_p\,c_s(\bar U;p).
\tag{15.14}
```

The cochain identity on the spanning surface is

```math
\prod_{\ell\in C}^{\mathrm{or}}z_\ell^{\sigma_{\ell C}}
=
\prod_{p\in S}(\delta z)_p
=
\prod_{p\in S}b_p\,c_s(\bar U;p)^{-1}.
\tag{15.15}
```

Therefore the normalized fundamental Wilson loop obeys the pointwise identity

```math
W_{1/2}(C;U)
:=
\frac12\operatorname{Tr}
\prod_{\ell\in C}^{\mathrm{or}}U_\ell^{\sigma_{\ell C}}
=
\left(\prod_{p\in S}b_p\right)
\left(\prod_{p\in S}c_s(\bar U;p)^{-1}\right)
\frac12\operatorname{Tr}H_C^s(\bar U).
\tag{15.16}
```

Equivalently, set

```math
\Xi_S(b)
:=
\prod_{p\in S}b_p,
\qquad
A^s_{C,S}(\bar U)
:=
\left(\prod_{p\in S}c_s(\bar U;p)^{-1}\right)
\frac12\operatorname{Tr}H_C^s(\bar U).
\tag{15.17}
```

Then the exact finite-cutoff expectation is

```math
\langle W_{1/2}(C)\rangle
=
\left\langle
\Xi_S(b)\,A^s_{C,S}(\bar U)
\right\rangle_{\mathrm{lift}}.
\tag{15.18}
```

The expectation is taken with respect to the exact positive lifted measure
defined by the center/coset disintegration above.

For any lifted observable F, this means

```math
\langle F\rangle_{\mathrm{lift}}
:=
\frac{1}{Z_\Lambda}\,
2^{-|E|}
\sum_{z\in\{\pm1\}^E}
\int_{SO(3)^E}
F(z,\bar U)
\prod_{p\in P}
K_t\!\left(
(\delta z)_p\,c_s(\bar U;p)\,s(\bar U_p)
\right)
\prod_{\ell\in E}d\bar U_\ell .
```

**Proof.** The Haar formula (15.8) is the pushforward of the product of
normalized counting measure on the two-point fiber and normalized Haar measure
on SO(3). Its
pushforward to SU(2) is left-invariant and normalized, hence equals normalized
SU(2) Haar measure. Taking products over links gives (15.9).

The plaquette lift follows from centrality of the signs:

```math
U_p
:=
\prod_{\ell\in \partial p}^{\mathrm{or}}U_\ell^{\sigma_{\ell p}}
=
(\delta z)_p\,c_s(\bar U;p)\,s(\bar U_p).
\tag{15.19}
```

This is the lifted plaquette formula, with (15.14) naming its central factor.
The lattice Stokes identity for the center one-cochain is

```math
\prod_{p\in S}(\delta z)_p
=
\prod_{\ell\in C}^{\mathrm{or}}z_\ell^{\sigma_{\ell C}},
\tag{15.20}
```

because every interior link of S appears twice with opposite incidence and the
remaining boundary incidence is exactly C. Combining (15.14) and (15.20) gives
(15.15).

For the Wilson loop, centrality gives

```math
\prod_{\ell\in C}^{\mathrm{or}}U_\ell^{\sigma_{\ell C}}
=
\left(
\prod_{\ell\in C}^{\mathrm{or}}z_\ell^{\sigma_{\ell C}}
\right)
H_C^s(\bar U).
\tag{15.21}
```

Taking the normalized fundamental trace and substituting (15.15) proves
(15.16). Integrating (15.16) against the positive lifted measure obtained from
(15.9) proves (15.18).

It remains to check section independence. Let another measurable section be

```math
s'(\bar g)=\varepsilon(\bar g)s(\bar g),
\qquad
\varepsilon(\bar g)\in\{\pm1\}.
\tag{15.22}
```

Write

```math
\varepsilon_\ell:=\varepsilon(\bar U_\ell),
\qquad
\varepsilon_p^{\mathrm{plaq}}:=\varepsilon(\bar U_p),
\qquad
(\delta\varepsilon)_p
:=
\prod_{\ell\in\partial p}^{\mathrm{or}}
\varepsilon_\ell^{\sigma_{\ell p}}.
\tag{15.23}
```

The link-center coordinate changes by

```math
z'_\ell=z_\ell\,\varepsilon_\ell^{-1}.
\tag{15.24}
```

The plaquette cocycle changes by

```math
c_{s'}(\bar U;p)
=
(\delta\varepsilon)_p\,
c_s(\bar U;p)\,
\left(\varepsilon_p^{\mathrm{plaq}}\right)^{-1}.
\tag{15.25}
```

Consequently the center plaquette coordinate changes by

```math
b'_p=b_p\left(\varepsilon_p^{\mathrm{plaq}}\right)^{-1}.
\tag{15.26}
```

The section-lifted loop changes by the boundary sign:

```math
H_C^{s'}(\bar U)
=
\left(
\prod_{\ell\in C}^{\mathrm{or}}
\varepsilon_\ell^{\sigma_{\ell C}}
\right)
H_C^s(\bar U).
\tag{15.27}
```

Finally,

```math
\prod_{p\in S}(\delta\varepsilon)_p
=
\prod_{\ell\in C}^{\mathrm{or}}
\varepsilon_\ell^{\sigma_{\ell C}}.
\tag{15.28}
```

Equations (15.25)-(15.28) show that all section-change factors cancel in the
full product:

```math
\Xi_S(b')\,A^{s'}_{C,S}(\bar U)
=
\Xi_S(b)\,A^s_{C,S}(\bar U).
\tag{15.29}
```

Thus (15.16) and (15.18) are independent of the arbitrary SO(3)-to-SU(2)
section. Notice the important distinction: the center plaquette coordinate in
(15.14) is section-dependent, while the full Wilson product in (15.16) is not.
The lifted measure is also section-independent: the map from the old link signs
to the new link signs is a bijection, and the plaquette element in (15.19) is
the same SU(2) plaquette element in either coordinate system.

This is the hardened CLT4 gate. It includes the SO(3) cocycle product over the
entire spanning surface. The amplitude has absolute value at most one, but that
fact is not enough: it is still area-supported and correlated with the center
sheet. The real O2 question is whether this coset/cocycle factor can be
localized, dominated, mixed, or integrated out without destroying center
disorder.

The expression is independent of the choice of spanning surface only as a full
identity. The center sheet factor alone need not be surface-independent. Any
claim of Wilson sheet domination must therefore control the full surface
dependence of the coset/cocycle factor.

**CLT5. Quasilocal blocked center action.** There exists a positive blocking or
finite-range decomposition under which the center effective action is
quasilocal with estimates uniform enough to attempt the CD2-CD4 program. If the
required estimates deteriorate like an area term or vanish in the continuum
scaling window, this must be recorded as the failure mode.

The target is deliberately binary. It either opens a real center route or
closes the route honestly.

### 15.4. IR Validity Boundary

The Non-Abelian Center-Lift Transform is an IR-valid strategy only in the
following limited sense:

```math
\boxed{
\mathrm{CLT1}\text{-}\mathrm{CLT5}
\quad\Longrightarrow\quad
\text{a possible finite-cutoff mechanism for IR5,}
}
```

not:

```math
\boxed{
\mathrm{CLT1}\text{-}\mathrm{CLT5}
\quad\Longrightarrow\quad
\text{confinement, mass gap, or CD4.}
}
```

To become a genuine IR proof, the transform would still need three additional
uniform estimates.

**1. Surface Independence With Constraints.** In the SU(2) identity, the center
sheet factor is

```math
\Xi_S(b)
=
\prod_{p\in S}b_p.
```

This factor need not be independent of the spanning surface by itself. Surface
independence belongs to the full product in (15.16). One-form gauge covariance
alone is not enough. Either the center field must satisfy the correct
closedness/Bianchi law, or the missing dependence must be exactly cancelled by
the SO(3) cocycle amplitude.

**2. No Area-Order Coset Sabotage.** The dangerous non-center factor is

```math
A^s_{C,S}(\bar U)
=
\left(\prod_{p\in S}c_s(\bar U;p)^{-1}\right)
\frac12\operatorname{Tr}H_C^s(\bar U).
```

It obeys the absolute bound

```math
|A^s_{C,S}(\bar U)|\le1,
```

but that bound is not enough. The factor is supported on the whole spanning
surface through the cocycle product. It must be localized, dominated, mixed, or
integrated out without creating area-order cancellation against the center sheet
factor.

**3. Fixed-Scale Uniformity.** The center disorder estimate must be uniform in
volume and cutoff at fixed physical loop scale as the lattice spacing tends to
zero. A strong-coupling estimate, or an estimate confined to the UV
positive-flow corridor, does not prove IR5.

Thus the correct dependency is:

```math
\boxed{
\begin{array}{c}
\text{exact center/coset transform}\\
+\ \text{surface-independent Wilson sheet formula}\\
+\ \text{no area-order coset loss}\\
+\ \text{uniform fixed-scale center disorder}\\[1mm]
\Longrightarrow\ \mathrm{IR5}.
\end{array}}
```

Even if this succeeds, it primarily attacks IR5. The rest of the Paper 39
fixed-scale bridge remains separate: IR1-IR3 identify the standard fixed-scale
continuum sector, IR4 supplies transfer/correlation-length control, and IR6 is
the positive physical mass gap.

### 15.5. Why This Is The Right Obstruction To Attack Next

The strong-coupling proof in Sections 12-14 proves CD3 for the abelianized
center model at fixed strong coupling. It does not tell us whether full SU(N)
Yang-Mills has a positive center ensemble with a Wilson-loop transform strong
enough to carry confinement.

The center-lift transform attacks exactly this missing bridge.

It attacks O1 because it asks whether center variables provide analytic control
beyond a relabeling of the original gauge field.

It attacks O2 because it tests whether non-abelian character sums and lift
cocycles destroy positivity or introduce area-order cancellations into Wilson
observables.

It also prepares IR5. If the exact identity (15.18) can be converted into Wilson
sheet domination, with the SO(3) cocycle factor localized, dominated, mixed, or
integrated out without area-order cancellation, then the area law may be
transferred to a center surface-disorder estimate. If the cocycle factor remains
area-supported in a way that cancels center disorder, then the center mechanism
cannot by itself prove confinement in full SU(N).

### 15.6. First Concrete Proof Order

The cleanest first target is SU(2). In this case

```math
Z=Z_2,\qquad \bar G=SO(3).
```

The proof should be built in the following order.

1. Prove the exact SU(2)-to-SO(3)-times-Z2 lift identity on an arbitrary finite
   cubical lattice, without gauge fixing.

2. Prove one-form gauge covariance, section independence, and the precise
   transformation law of the lifting cocycle.

3. Derive the exact Wilson-loop identity (15.16)-(15.18) first for the
   fundamental representation, then for half-integer and integer spin
   representations. Separate the pure Z2 sheet factor from the SO(3) cocycle
   amplitude.

4. Test whether the SO(3) cocycle amplitude can be localized, dominated, mixed,
   or integrated out without area-order cancellation. This is the key pass/fail
   calculation. If it fails, O2 is real and must be stated as a theorem.

5. If the cocycle test passes, integrate or block the SO(3) variables to
   produce a positive center marginal and estimate its locality radius.

6. Only after steps 1-5 succeed should one attempt CD2-CD4 by random-surface
   switching, reflection positivity, chessboard estimates, finite-range
   decomposition, or Balaban-style RG with a background center two-form.

This sequence is intentionally finite-cutoff first. The continuum question is
deferred until the exact non-abelian center transform exists.

### 15.7. Expected Failure Modes

The transform should be judged by explicit failure modes, not optimism.

**CLT-F1: section dependence.** If the construction depends on the arbitrary
lift, it is not a physical center transform.

**CLT-F2: hidden sign problem.** If the center marginal is signed, or positive
only after cancellations of area-order size, the route does not provide an
independent confinement proof.

**CLT-F3: area-supported cocycle sabotage.** If the SO(3) cocycle factor in
(15.18) cannot be localized, dominated, mixed, or integrated out without
area-order cancellation, then the center sheet character cannot force an area
law. The absolute bound on this factor does not solve the problem by itself.

**CLT-F4: nonlocal center action.** If integrating out the PSU(N) variables
produces a center action with uncontrolled long-range interactions at the
relevant scales, CD2 is not available.

**CLT-F5: continuum collapse.** If all positive center disorder estimates
require a strong-coupling condition that becomes false as beta tends to infinity,
then the result remains a fixed-scale strong-coupling theorem and does not
reach CD4.

### 15.8. The New Local Problem

The next obstruction can therefore be stated as a compact finite-dimensional
problem:

```math
\boxed{
\begin{array}{c}
\text{For finite }SU(2)\text{ lattice Yang-Mills,}\\[2mm]
\text{derive the exact }SO(3)\times Z_2\text{ lift with cocycle,}\\[2mm]
\text{insert a fundamental Wilson loop,}\\[2mm]
\text{and prove or disprove that the }SO(3)\text{ cocycle factor}\\
\text{can be controlled without area-order cancellation.}
\end{array}}
```

This is the next attack because it is small enough to be honest and large
enough to decide whether the center program has teeth. It is also the point
where the two instincts meet: formulate the invariant background response
first, then do the exact path-integral arithmetic without hiding any term.

If this local problem succeeds, Paper 40 can turn from a center-resolved route
into an actual non-abelian center mechanism. If it fails, the failure is itself
a valuable theorem: it says the continuum Yang-Mills gap cannot be obtained by
this center route without a new idea beyond positive center disorder.

### 15.9. Conditional Cocycle Obstruction

Searchable conditional-obstruction tag:

`V4P40-CONDITIONAL-COCYCLE-OBSTRUCTION`.

The SU(2) identity above exposes the exact obstruction, but it is still mixed
between the section-dependent center coordinate and the SO(3) variables. The
next hardening step is to condition on the center coordinate and ask whether the
remaining SO(3) factor is only boundary/quasilocal noise or whether it carries
area-order cancellation.

Fix a section before making any estimate. Let the section-relative center map be

```math
\mathcal B_s(z,\bar U)_p
:=
(\delta z)_p\,c_s(\bar U;p).
```

The section-relative center marginal is the pushforward of the lifted measure:

```math
\mu^s_{\mathrm{cen}}
:=
(\mathcal B_s)_*\mu^s_{\mathrm{lift}}.
\tag{15.30}
```

For each center configuration in the support of this marginal, define the
conditional cocycle amplitude by conditional expectation:

```math
\alpha^s_{C,S}(b)
:=
\mathbb E_{\mu^s_{\mathrm{lift}}}
\left[
A^s_{C,S}(\bar U)
\mid
\mathcal B_s=b
\right].
\tag{15.31}
```

On center configurations of zero marginal weight, the value of the conditional
amplitude is irrelevant and may be chosen arbitrarily. The Wilson identity
(15.18) becomes the exact center-marginal formula

```math
\langle W_{1/2}(C)\rangle
=
\int
\Xi_S(b)\,\alpha^s_{C,S}(b)\,
d\mu^s_{\mathrm{cen}}(b).
\tag{15.32}
```

This is just the tower property of conditional expectation applied to (15.18).
It is exact at finite volume and positive cutoff.

The object in (15.31) is the obstruction. The center coordinate, center
marginal, and conditional amplitude are all section-relative:

```math
\mathcal B_s,\qquad
\mu^s_{\mathrm{cen}},\qquad
\alpha^s_{C,S}.
```

Their product integral in (15.32) is section-independent because it equals the
physical Wilson expectation. Therefore a proof that uses (15.32) must obey one
of the following two disciplines.

**Admissible-Section Discipline.** Choose the section before the loop, surface,
cutoff sequence, or estimate is selected, and prove constants that do not rely
on post-selecting a favorable lift. Since a global continuous section from
SO(3) to SU(2) does not exist, any locality claim using a section must explicitly
control the discontinuity set or replace the section by a local trivialization
with transition signs.

**Invariant Reformulation Discipline.** Avoid treating the center coordinate as
a physical observable. Formulate the estimate directly for the section-invariant
product in (15.16), or for a blocked object whose definition does not change
under section replacement.

The pass/fail target is now sharp.

**PASS: boundary/quasilocal cocycle.** The conditional amplitude can be written,
uniformly enough for the fixed-scale IR5 problem, as a boundary/quasilocal
correction:

```math
\alpha^s_{C,S}(b)
=
\Gamma^s_C(b)
+R^s_{C,S}(b),
\tag{15.33}
```

where the first term is supported near the loop, or has uniformly summable
tails, and the remainder does not create area-order cancellation against the
center sheet factor. This additive form does not assume positivity or the
existence of a logarithm for the conditional amplitude.

**FAIL: area-supported cocycle.** The conditional amplitude has unavoidable
dependence on the interior of the spanning surface:

```math
\alpha^s_{C,S}(b)
\quad
\hbox{carries area-order dependence on }S.
\tag{15.34}
```

In that case the center sheet factor is not an independent disorder variable.
The SO(3) cocycle has retained the hard Yang-Mills IR problem, and the center
route is only a change of coordinates unless a new idea controls that factor.

Thus the finite-cutoff local problem can be restated as:

```math
\boxed{
\begin{array}{c}
\text{Prove that } \alpha^s_{C,S}\text{ is boundary/quasilocal,}\\[1mm]
\text{or prove that it has irreducible area-supported dependence.}
\end{array}}
\tag{15.35}
```

Only the PASS alternative can feed an IR5 proof. Even then, the estimates must
be expressed in physical units and remain uniform along the continuum scaling
trajectory. Otherwise (15.32) is an exact finite-cutoff diagnostic, not a fixed
physical infrared theorem.

### 15.10. Proved Failure Of The Bare Center-Sheet Route

Searchable no-free-lunch tag:

`V4P40-BARE-CENTER-SHEET-ROUTE-FAILURE`.

The previous subsection defines the true obstruction. We can already prove one
negative statement rigorously: center disorder plus the pointwise bound on the
SO(3) cocycle factor is not enough to prove a Wilson area law. Some additional
decorrelation, locality, mixing, domination, or conditional quasilocality
estimate for the cocycle factor is logically necessary.

This is not a proof that the actual Yang-Mills conditional amplitude is in the
FAIL branch. It is a proof that the bare algebraic center route fails.

**Theorem 40.5 (No-Free-Lunch For The Conditional Cocycle).** Let

```math
X_S(b):=\Xi_S(b)
```

be a center sheet variable taking values in the unit circle, and suppose the
center marginal obeys any desired center-disorder estimate, for example

```math
\left|
\mathbb E_{\mu_{\mathrm{cen}}}
X_S
\right|
\le
e^{-\sigma A+\kappa L}.
\tag{15.36}
```

The estimate (15.36), together with the pointwise amplitude bound

```math
|\alpha_S(b)|\le1,
\tag{15.37}
```

does not imply a Wilson area-law bound for

```math
\mathbb E_{\mu_{\mathrm{cen}}}
\left[
X_S(b)\alpha_S(b)
\right].
\tag{15.38}
```

Indeed, there exists a bounded amplitude satisfying (15.37) for which

```math
\mathbb E_{\mu_{\mathrm{cen}}}
\left[
X_S(b)\alpha_S(b)
\right]
=1.
\tag{15.39}
```

#### Proof

Choose

```math
\alpha_S(b):=\overline{X_S(b)}.
\tag{15.40}
```

Then (15.37) holds. But

```math
X_S(b)\alpha_S(b)
=
X_S(b)\overline{X_S(b)}
=1
```

pointwise. Therefore (15.39) holds for every center marginal, even if the
center sheet expectation in (15.36) is exponentially small in the area. Thus no
area-law conclusion can follow from center disorder and boundedness of the
cocycle amplitude alone. `∎`

The theorem identifies the exact logical gap. In the actual SU(2) lift, the
amplitude is not arbitrary; it is the conditional cocycle amplitude

```math
\alpha^s_{C,S}.
```

Therefore the next theorem cannot be merely a center-disorder theorem. It must
prove that the actual conditional amplitude is not locked to the conjugate
center sheet variable in an area-supported way.

A sufficient PASS criterion is the following.

**Criterion 40.6 (Conditional Decorrelation Sufficient For IR5).** Suppose that,
along a continuum scaling trajectory and at fixed physical loop scale, the
section-relative center marginal and conditional cocycle amplitude obey

```math
\left|
\int
\Xi_S(b)\,\alpha^s_{C,S}(b)\,
d\mu^s_{\mathrm{cen}}(b)
\right|
\le
K
\exp\!\left(
-\sigma_{\mathrm{phys}}\operatorname{Area}_{\mathrm{phys}}(S)
+\kappa\operatorname{Perim}_{\mathrm{phys}}(C)
+o(1)
\right),
\tag{15.41}
```

with constants independent of the cutoff and with

```math
\sigma_{\mathrm{phys}}>0.
\tag{15.42}
```

Then the SU(2) Wilson loop satisfies the fixed-physical-scale area law, hence
the center-lift route supplies the IR5 sheet-domination estimate.

#### Proof

Equation (15.32) identifies the Wilson expectation with the integral on the
left-hand side of (15.41). Substituting (15.41) gives the Wilson area-law bound
in physical units. The strict positivity in (15.42) is exactly the positive
physical string-tension requirement. `∎`

The content has therefore been reduced to one nontrivial estimate:

```math
\boxed{
\text{prove (15.41), or prove that (15.41) fails for the actual }
\alpha^s_{C,S}.
}
\tag{15.43}
```

Theorem 40.5 proves that there is no shortcut through the center marginal alone.
Criterion 40.6 states the exact condition that would turn the section-relative
conditional obstruction into a fixed physical IR result.

### 15.11. Conditional Decorrelation Is Exactly The IR5 Content

Searchable equivalence tag:

`V4P40-CONDITIONAL-DECORRELATION-EQUIVALENT-IR5`.

The request "prove or disprove conditional decorrelation" must be interpreted
carefully. There is a weak form and a strong form.

The weak form is the numerical estimate (15.41). This form is not an auxiliary
lemma: by the exact Wilson identity, it is precisely the fixed-scale Wilson
sheet-domination estimate.

The strong form is structural: show that the conditional amplitude is
boundary/quasilocal, or that it is irreducibly area-supported. That structural
claim would explain why (15.41) holds or fails. The current paper proves neither
structural alternative for the actual Yang-Mills cocycle.

The weak equivalence can be proved now.

**Theorem 40.7 (Conditional Decorrelation Equals IR5 For This Route).** Fix an
admissible section before taking estimates. Let a continuum scaling trajectory
be given, with lattice loops and spanning surfaces converging to fixed physical
objects:

```math
a\downarrow0,\qquad
C_a\to C_{\mathrm{phys}},\qquad
S_a\to S_{\mathrm{phys}}.
```

For the SU(2) center-lift representation, the conditional decorrelation bound

```math
\left|
\int
\Xi_{S_a}(b)\,\alpha^s_{C_a,S_a}(b)\,
d\mu^s_{\mathrm{cen},a}(b)
\right|
\le
K
\exp\!\left(
-\sigma_{\mathrm{phys}}\operatorname{Area}_{\mathrm{phys}}(S_{\mathrm{phys}})
+\kappa\operatorname{Perim}_{\mathrm{phys}}(C_{\mathrm{phys}})
+o(1)
\right)
\tag{15.44}
```

with

```math
\sigma_{\mathrm{phys}}>0
\tag{15.45}
```

is equivalent, along this route, to the IR5 Wilson sheet-domination estimate for
the fundamental Wilson loop:

```math
\left|
\langle W_{1/2}(C_a)\rangle
\right|
\le
K
\exp\!\left(
-\sigma_{\mathrm{phys}}\operatorname{Area}_{\mathrm{phys}}(S_{\mathrm{phys}})
+\kappa\operatorname{Perim}_{\mathrm{phys}}(C_{\mathrm{phys}})
+o(1)
\right).
\tag{15.46}
```

#### Proof

For every finite cutoff, equation (15.32) gives the identity

```math
\langle W_{1/2}(C_a)\rangle
=
\int
\Xi_{S_a}(b)\,\alpha^s_{C_a,S_a}(b)\,
d\mu^s_{\mathrm{cen},a}(b).
\tag{15.47}
```

Substituting (15.47) into (15.44) gives (15.46). Conversely, substituting
(15.47) into (15.46) gives (15.44). The positivity condition (15.45) is the same
positive physical string-tension condition in both statements. Therefore the
conditional decorrelation bound, in the weak numerical sense needed for IR5, is
not a preliminary estimate distinct from IR5; it is IR5 written in the
center/coset variables. `∎`

Thus Paper 40 now proves the following fork:

```math
\boxed{
\begin{array}{c}
\text{Bare center disorder does not imply IR5}
\quad\text{(Theorem 40.5).}\\[1mm]
\text{Conditional decorrelation would imply IR5}
\quad\text{(Criterion 40.6).}\\[1mm]
\text{The numerical decorrelation estimate is exactly IR5}
\quad\text{(Theorem 40.7).}
\end{array}}
\tag{15.48}
```

Consequently the unresolved mathematical problem is the strong structural form:

```math
\boxed{
\begin{array}{c}
\text{prove that the actual }SO(3)\text{ cocycle amplitude is
boundary/quasilocal,}\\[1mm]
\text{or prove that it has irreducible area-supported dependence.}
\end{array}}
\tag{15.49}
```

This is the honest end of the present proof. A proof of the first line of
(15.49) would be a new non-Abelian center mechanism for IR5. A proof of the
second line would close this center route as a relabeling of the hard IR
problem.

### 15.12. Attempting The Conditional Cocycle Route

Searchable conditional-route-attempt tag:

`V4P40-CONDITIONAL-COCYCLE-ROUTE-ATTEMPT`.

The conditional cocycle route can be attacked directly by writing the
conditional amplitude as a ratio of constrained SO(3) fiber integrals. This is
the point at which the problem becomes completely explicit.

For a fixed section, define the solvability indicator

```math
\mathbf 1^s_b(\bar U)
:=
\mathbf 1\!\left[
b\,c_s(\bar U)^{-1}\in\operatorname{im}
\left(\delta:C^1(\Lambda,Z_2)\to C^2(\Lambda,Z_2)\right)
\right].
\tag{15.50}
```

Define the fiber denominator

```math
D^s(b)
:=
\int_{SO(3)^E}
\mathbf 1^s_b(\bar U)
\prod_{p\in P}
K_t\!\left(b_p\,s(\bar U_p)\right)
\prod_{\ell\in E}d\bar U_\ell .
\tag{15.51}
```

Define the fiber numerator

```math
N^s_{C,S}(b)
:=
\int_{SO(3)^E}
\mathbf 1^s_b(\bar U)\,
A^s_{C,S}(\bar U)
\prod_{p\in P}
K_t\!\left(b_p\,s(\bar U_p)\right)
\prod_{\ell\in E}d\bar U_\ell .
\tag{15.52}
```

**Theorem 40.8 (Exact Fiber Formula For The Conditional Cocycle).** For every
center configuration in the support of the section-relative center marginal,

```math
\alpha^s_{C,S}(b)
=
\frac{N^s_{C,S}(b)}{D^s(b)}.
\tag{15.53}
```

#### Proof

Fix the center field. The equation defining the center field is

```math
b
=
(\delta z)c_s(\bar U).
\tag{15.54}
```

For fixed SO(3) links, this equation is solvable in the link signs precisely
when the indicator in (15.50) equals one. When it is solvable, the set of
solutions is an affine translate of the kernel of the coboundary map on center
one-cochains, so the number of link-sign solutions is independent of both the
center field and the SO(3) configuration.

On the fiber defined by (15.54), the plaquette argument in the lifted measure is

```math
(\delta z)_p\,c_s(\bar U;p)\,s(\bar U_p)
=
b_p\,s(\bar U_p).
\tag{15.55}
```

Thus the conditional law of the SO(3) variables given the center field has
density proportional to the integrand in (15.51). The common number of
link-sign solutions cancels between numerator and denominator. Applying the
definition of conditional expectation in (15.31) gives (15.53). `∎`

This proves that the conditional cocycle route is not a vague probabilistic
hope. It is the following explicit SO(3) ratio:

```math
\boxed{
\alpha^s_{C,S}(b)
=
\frac{
\int
\mathbf 1^s_b(\bar U)\,
A^s_{C,S}(\bar U)
\prod_pK_t\!\left(b_p\,s(\bar U_p)\right)
d\bar U
}{
\int
\mathbf 1^s_b(\bar U)
\prod_pK_t\!\left(b_p\,s(\bar U_p)\right)
d\bar U
}.
}
\tag{15.56}
```

The numerator contains the surface insertion

```math
A^s_{C,S}(\bar U)
=
\left(\prod_{p\in S}c_s(\bar U;p)^{-1}\right)
\frac12\operatorname{Tr}H_C^s(\bar U).
\tag{15.57}
```

Therefore the route has a precise target:

```math
\boxed{
\text{show that the ratio in (15.56) is boundary/quasilocal,}
\quad
\text{or show that the surface insertion in (15.57) survives in the bulk.}
}
\tag{15.58}
```

This is a constrained SO(3) mixing problem. The center coordinate has not
removed the non-Abelian dynamics; it has isolated it into the fiber ratio.

The only PASS checkpoint currently available from known theory is the old
fixed-cutoff strong-coupling result.

**Theorem 40.9 (Strong-Coupling Conditional Checkpoint).** Suppose the classical
SU(2) lattice strong-coupling area law holds at fixed cutoff:

```math
\left|
\langle W_{1/2}(C)\rangle
\right|
\le
K_{\mathrm{sc}}
\exp\!\left(
-\sigma_{\mathrm{sc}}A+\kappa_{\mathrm{sc}}L
\right),
\qquad
\sigma_{\mathrm{sc}}>0.
\tag{15.59}
```

Then the conditional cocycle integral obeys the same fixed-cutoff estimate:

```math
\left|
\int
\Xi_S(b)\,\alpha^s_{C,S}(b)\,
d\mu^s_{\mathrm{cen}}(b)
\right|
\le
K_{\mathrm{sc}}
\exp\!\left(
-\sigma_{\mathrm{sc}}A+\kappa_{\mathrm{sc}}L
\right).
\tag{15.60}
```

#### Proof

Equation (15.32) identifies the integral in (15.60) with the Wilson expectation.
The assumed strong-coupling area law (15.59) gives the result. `∎`

This checkpoint is useful but not new. It imports the classical strong-coupling
Wilson theorem and therefore remains fixed-cutoff. It does not prove the
fixed-physical-scale IR5 estimate.

The attempt therefore ends at the following exact boundary:

```math
\boxed{
\begin{array}{c}
\text{The conditional cocycle route is reduced to the fiber ratio (15.56).}\\[1mm]
\text{At strong coupling, the numerical bound follows from known Wilson theory.}\\[1mm]
\text{At fixed physical IR scale, one still needs a new SO(3) fiber-mixing
theorem.}
\end{array}}
\tag{15.61}
```

In concrete terms, the next real theorem would have to prove that the surface
insertion in (15.57), under the constrained fiber measure in (15.51), contributes
only boundary/quasilocal corrections uniformly along the continuum trajectory.
Without such a theorem, the conditional cocycle route has not escaped the shared
4D infrared floor; it has located that floor in the SO(3) fiber.

### 15.13. Local Trivialization And The SO(3) Bad-Block Polymer Test

Searchable local-trivialization tag:

`V4P40-LOCAL-TRIVIALIZATION-BAD-BLOCK-TEST`.

The next non-circular bite is local. The SO(3) cocycle is dangerous only where it
cannot be trivialized into a boundary sign. On such a region the surface product
may carry genuine bulk dependence. On a trivializable region it is a boundary
term.

Fix the admissible section before estimates are made. On a plaquette set Q,
call the SO(3) configuration section-trivializable if there exists a center
one-cochain on the links of Q such that

```math
c_s(\bar U;p)
=
(\delta\varepsilon_Q)_p
\qquad
\text{for every }p\subset Q.
\tag{15.62}
```

Call Q bad when no such cochain exists.

**Theorem 40.10 (Good Blocks Localize The Cocycle To The Boundary).** Let Q be a
section-trivializable plaquette region, and let T be any plaquette two-chain in
Q. Then

```math
\prod_{p\in T}c_s(\bar U;p)^{-1}
=
\prod_{\ell\in\partial T}
\varepsilon_Q(\ell)^{-\sigma_{\ell,\partial T}}.
\tag{15.63}
```

Thus the cocycle product over T depends only on the boundary of T inside Q.

#### Proof

Using (15.62),

```math
\prod_{p\in T}c_s(\bar U;p)^{-1}
=
\prod_{p\in T}(\delta\varepsilon_Q)_p^{-1}.
\tag{15.64}
```

Expanding the coboundary, every interior link of T appears twice with opposite
incidence and cancels. The only remaining signs are the boundary-link signs,
which gives (15.63). `∎`

Consequently the surface insertion in (15.57) has bulk support only where the
surface crosses bad blocks. If the spanning surface is decomposed into good and
bad blocks, then the cocycle factor has the schematic exact form

```math
\prod_{p\in S}c_s(\bar U;p)^{-1}
=
\text{boundary signs near }C
\times
\text{interface signs}
\times
\prod_{p\in S\cap\mathrm{Bad}}c_s(\bar U;p)^{-1}.
\tag{15.65}
```

The first two factors are boundary or block-interface data. The last factor is
the only possible area-supported obstruction.

The good-block condition is not empty. A finite-block small-field criterion gives
one concrete source of good blocks.

**Lemma 40.11 (Small-Field Blocks Are Trivializable).** Fix a block shape of
finite lattice diameter. Choose the global section so that it agrees with the
principal SU(2) lift on a sufficiently small neighborhood of the identity in
SO(3). There exists a small-field radius, depending only on the block shape, such
that if an SO(3) configuration on the block admits an axial/tree gauge in which
all links and all plaquette products lie in that neighborhood, then the block is
section-trivializable.

#### Proof

On the chosen neighborhood, the covering map from SU(2) to SO(3) has a continuous
principal local inverse. In the axial/tree gauge, every link and every plaquette
product lies in the domain of this inverse. The sign

```math
\prod_{\ell\in\partial p}^{\mathrm{or}}
s(\bar U_\ell)^{\sigma_{\ell p}}
s(\bar U_p)^{-1}
\tag{15.66}
```

is a continuous map from the connected small-field domain to the discrete group

```math
\{\pm1\}.
```

At the identity configuration it equals plus one. Hence it equals plus one
throughout the small-field domain for the local principal section. Passing back
to the fixed global section changes the local section by link signs. Therefore
the global-section cocycle is a coboundary on the block, which is (15.62). `∎`

This lemma is a local chart statement. Turning it into a probability estimate
under the fiber measure still requires a controlled block gauge fixing or a
gauge-invariant partition of unity. That extra step is part of the bad-block
subcriticality problem below.

The conditional cocycle route is therefore reduced to a polymer question about
bad blocks.

Let

```math
\mathcal B_{\mathrm{bad}}(\bar U)
\tag{15.67}
```

be the set of bad blocks for the SO(3) fiber configuration. A bad-block polymer
is a connected component of this set. The desired fixed-physical-scale theorem
would be a uniform subcriticality estimate for these polymers under the
constrained fiber measure (15.51).

One sufficient condition is a Kotecky-Preiss-type bound at a physical block
scale:

```math
\sup_{Q_0}
\sum_{\Gamma\ni Q_0}
|w_{\mathrm{bad}}(\Gamma)|\,e^{a|\Gamma|}
\le
1
\tag{15.68}
```

with constants independent of the cutoff along the continuum trajectory.

**Criterion 40.12 (Bad-Block Subcriticality Implies Structural Decorrelation).**
Assume (15.68), with a summable interaction between bad polymers and the loop
boundary. Then the conditional amplitude admits a boundary/quasilocal
decomposition of the form

```math
\alpha^s_{C,S}(b)
=
\Gamma^s_C(b)
+R^s_{C,S}(b),
\tag{15.69}
```

where the first term is supported near the loop, up to uniformly summable tails,
and the remainder is controlled by bad-block polymers intersecting the spanning
surface. In particular, if the polymer estimate is uniform in physical units,
the cocycle factor cannot create an uncontrolled area-order cancellation.

#### Proof

On every good block, Theorem 40.10 turns the cocycle product into a boundary or
interface sign. Thus all bulk dependence of the surface insertion is confined to
connected bad-block components intersecting the surface. Under (15.68), the
cluster expansion over those connected components converges absolutely, and the
sum of clusters reaching distance r from the loop boundary has a summable tail.
The resulting cluster expansion separates the boundary contribution from the
summable bad-block remainder, giving (15.69). `∎`

This is the first real structural PASS criterion. It does not assume a Wilson
area law. It asks instead for a subcritical bad-block gas in the SO(3) fiber.

The fixed-physical-scale obstruction is now precise:

```math
\boxed{
\begin{array}{c}
\text{prove uniform bad-block subcriticality (15.68),}\\[1mm]
\text{or prove that bad blocks percolate or remain area-dense in the
constrained SO(3) fiber.}
\end{array}}
\tag{15.70}
```

At weak bare coupling, small plaquettes make the good-block picture plausible at
ultraviolet scales. At fixed physical infrared scale, however, uniform
subcriticality of bad SO(3) blocks is not currently supplied by the construction.
That is the next theorem required by the Conditional Cocycle Route.

### 15.14. Gauge-Invariant Good Blocks And The Uniform Defect Theorem

Searchable fixed-IR tag:

`V4P40-GAUGE-INVARIANT-GOOD-BLOCKS`.

The previous subsection used a chart-dependent small-field lemma. That lemma is
correct as a local source of good blocks, but it is not the right fixed-IR
definition. For the fixed-physical-scale problem, the good/bad distinction must
be gauge-invariant and must include gluing compatibility between neighboring
local lifts. Otherwise one can hide an area-supported obstruction in the
transition signs between individually good blocks.

Fix a physical block scale R and let the lattice spacing be a. Let the block side
length be

```math
m(a)
=
\left\lceil \frac{R}{a}\right\rceil .
\tag{15.71}
```

Let Q be one such block, enlarged by one neighboring block in every lattice
direction. Choose once and for all a base vertex and a spanning tree in the
one-skeleton of the enlarged block. For each oriented link not in the tree, let
the associated fundamental loop be the closed path obtained by going out along
the tree, crossing that link, and returning along the tree. With a
conjugation-invariant distance on SO(3), define

```math
M_Q(\bar U)
=
\max_{\ell\notin T_Q}
d_{SO(3)}
\left(
\operatorname{Hol}_{\gamma_{Q,\ell}}(\bar U),
1
\right).
\tag{15.72}
```

Because fundamental-loop holonomies transform by conjugation, (15.72) is
gauge-invariant. For a fixed radius rho below the local injectivity radius, call
Q reconstructibly good when

```math
M_Q(\bar U)
\le
\rho .
\tag{15.73}
```

This condition is only a sufficient criterion; failure of (15.73) means bad for
this route, not necessarily physically singular.

**Theorem 40.13 (Gauge-Invariant Small-Field Reconstruction).** For every finite
block shape there is a radius rho, depending only on that shape and on the
chosen section chart, such that every reconstructibly good block is
section-trivializable in the sense of (15.62).

#### Proof

Gauge-transform inside the enlarged block to tree gauge. All tree links become
the identity. Every non-tree link becomes, up to orientation and conjugation at
the base vertex, the fundamental-loop holonomy appearing in (15.72). Hence all
links in tree gauge lie in the SO(3) ball of radius rho.

Choose rho small enough that all elementary plaquette products formed from those
links remain in the principal chart of the covering map from SU(2) to SO(3). In
that chart the local SU(2) lift is continuous. The central plaquette sign is
therefore a continuous map from a connected small-field domain to

```math
\{\pm1\}.
\tag{15.74}
```

At the identity configuration the sign is plus one, so it is plus one throughout
the domain. Undoing the SO(3) gauge transformation changes the chosen SU(2)
lifts by vertex lifts and link-center signs; replacing the local principal
section by the fixed global section changes them by another link-center
one-cochain. These changes multiply the plaquette signs by a coboundary.
Therefore the fixed-section cocycle on Q has the form (15.62). `∎`

Local triviality still has to glue. For two overlapping reconstructibly good
blocks, choose local trivializing cochains on the overlap. Since both cochains
trivialize the same cocycle, their ratio is flat:

```math
\delta
\left(
\varepsilon_Q\varepsilon_{Q'}
\right)
=
1
\qquad
\text{on }Q\cap Q'.
\tag{15.75}
```

A connected family of reconstructibly good blocks is coherently good if these
flat transition cochains have trivial Cech class, equivalently if the local
trivializations can be modified by flat one-cochains so that they glue to a
single cochain on the whole family:

```math
c_s(\bar U;p)
=
(\delta\varepsilon_{\mathcal G})_p
\qquad
\text{for every }p\subset \mathcal G .
\tag{15.76}
```

The condition (15.76) is section-invariant. A section change multiplies the
cocycle by a coboundary, so the vanishing or nonvanishing of the obstruction
class is unchanged.

Now define the actual defect set for a surface S. Work in a fixed block
neighborhood of S. A defect set is any block set D such that the complement of D
is a disjoint union of coherently good components. Let the canonical defect set
be the lexicographically first minimal such D:

```math
\mathfrak D_S(\bar U)
=
\operatorname*{arg\,min}_{D}
\left\{
|D|:
\left(S^{+}\setminus D\right)
\text{ is coherently good componentwise}
\right\}.
\tag{15.77}
```

This definition absorbs both kinds of obstruction:

```math
\begin{array}{ll}
\text{local obstruction:}
& \text{a block is not reconstructibly good,}\\[1mm]
\text{gluing obstruction:}
& \text{good local lifts have nontrivial transition class.}
\end{array}
\tag{15.78}
```

**Theorem 40.14 (Deterministic Defect Localization).** For every finite cutoff,
every spanning surface S, and every SO(3) fiber configuration, the cocycle
surface factor has an exact localization of the form

```math
\prod_{p\in S}
c_s(\bar U;p)^{-1}
=
B_C^s(\bar U)
\prod_{\Gamma\in\pi_0(\mathfrak D_S)}
J_\Gamma^s(\bar U).
\tag{15.79}
```

Here the first factor depends only on a fixed-thickness neighborhood of the loop
C, while each factor indexed by a connected defect component depends only on a
fixed-thickness neighborhood of that component. In particular, when defect
components touching the interior of S are subcritical, the cocycle surface
factor has no autonomous area-supported bulk dependence.

#### Proof

Remove the canonical defect set from the block neighborhood of S. By definition,
each remaining connected component is coherently good. On such a component
there exists a cochain satisfying (15.76). Applying Theorem 40.10 to the part of
S inside that component turns the product of cocycle signs into a product over
the boundary of the component.

Boundaries shared by two coherently good regions cancel after the glued
trivialization is chosen. Boundaries adjacent to the loop contribute to the
factor near C. Boundaries adjacent to removed blocks are assigned to the
corresponding connected defect component. Since the construction uses only a
fixed enlargement of S, each defect contribution depends only on a
fixed-thickness neighborhood of that component. This gives (15.79). `∎`

The probabilistic theorem needed for fixed physical IR is now exact. It is not a
Wilson-area-law assumption; it is a statement about the constrained SO(3) fiber
measure appearing in (15.51).

**Target 40.15 (Uniform Local-Lift Defect Subcriticality).** Along the continuum
trajectory, choose a physical block scale R and a reconstruction radius rho.
For every sufficiently small lattice spacing, every center field in the support
of the center marginal, and every reference block, the connected components of
(15.77) under the constrained fiber measure should obey a uniform
Kotecky-Preiss bound:

```math
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen}}}
\sup_{Q_0}
\sum_{\Gamma\ni Q_0}
\left|
w^s_{a,b}(\Gamma)
\right|
e^{\kappa|\Gamma|}
\le
\eta
<
1 .
\tag{15.80}
```

Here the polymer weights are the connected defect-cluster weights induced by the
fiber ratio (15.56), with the block scale held fixed in physical units. A weaker
annealed variant would also be sufficient if it controls the correlation with
the center sheet:

```math
\left|
\mathbb E_{\mu^s_{\mathrm{cen}}}
\left[
\Xi_S(b)\,
\Delta^s_{C,S}(b)
\right]
\right|
\le
K
\exp
\left(
-m_{\mathrm{def}}\operatorname{dist}(S_{\mathrm{bulk}},C)
\right),
\tag{15.81}
```

where

```math
\Delta^s_{C,S}(b)
=
\alpha^s_{C,S}(b)
-
\Gamma^s_C(b)
\tag{15.82}
```

is the non-boundary part of the conditional amplitude.

**Corollary 40.16 (What 40.15 Would Buy).** If either the quenched bound
(15.80) or the annealed bound (15.81) holds uniformly at fixed physical block
scale, then the conditional cocycle route supplies the missing fixed-IR
decorrelation estimate. Combined with Criterion 40.6, this gives the IR5 Wilson
sheet domination estimate for this center-resolved route.

#### Proof

By Theorem 40.14, all non-boundary dependence of the cocycle surface factor is
carried by connected defect components. The bound (15.80) gives an absolutely
convergent polymer expansion for those components, with summable tails away from
the loop. This yields the decomposition (15.69) with constants independent of
the cutoff in physical units. The annealed estimate (15.81) is precisely the
same conclusion after integration against the center sheet. Criterion 40.6 then
turns the resulting conditional decorrelation estimate into IR5. `∎`

Thus the next obstruction is no longer vague. The route succeeds if the
constrained SO(3) fiber has a subcritical gas of local-lift defects:

```math
\boxed{
\text{local-lift defects are uniformly subcritical at fixed physical block
scale.}
}
\tag{15.83}
```

The route fails in its present form if one can instead find a continuum sequence
for which those defects percolate through typical spanning surfaces:

```math
\boxed{
\text{local-lift defects remain area-dense or percolating in the constrained
SO(3) fiber.}
}
\tag{15.84}
```

This is the cleanest next place to push. It separates a deterministic theorem,
which is now proved, from a genuinely four-dimensional probabilistic theorem,
which is the remaining shared IR floor in the center-resolved variables.

### 15.15. First Attempt At Uniform Defect Subcriticality

Searchable Peierls-attempt tag:

`V4P40-FIRST-DEFECT-PEIERLS-ATTEMPT`.

We now try to prove Target 40.15 directly. The point of this subsection is not
to declare victory, but to push until the exact missing lemma is visible.

For a fixed center field, the constrained SO(3) fiber law is

```math
d\nu^s_{a,b}(\bar U)
=
\frac{1}{D^s(b)}
\mathbf 1^s_b(\bar U)
\prod_{p\in P}
K_{t(a)}
\left(
b_p\,s(\bar U_p)
\right)
\prod_{\ell\in E}d\bar U_\ell .
\tag{15.85}
```

Let the defect indicator for the canonical local-lift defect set be

```math
\eta_Q(\bar U;S)
=
\mathbf 1
\left[
Q\in\mathfrak D_S(\bar U)
\right].
\tag{15.86}
```

A direct route to Target 40.15 is the following polymer Peierls estimate. For
every connected block polymer Gamma, require

```math
\sup_{\omega_{\Gamma^c}}
\nu^s_{a,b}
\left(
\eta_Q=1\text{ for every }Q\in\Gamma
\mid
\omega_{\Gamma^c}
\right)
\le
\exp
\left(
-\tau_R|\Gamma|
\right),
\tag{15.87}
```

uniformly in the cutoff, the admissible exterior block data, and the center field
in the support of the center marginal.

**Criterion 40.17 (Polymer Peierls Bound Implies Target 40.15).** Suppose
(15.87) holds with tau_R larger than the lattice-animal entropy at the chosen
block adjacency scale. Then the Kotecky-Preiss bound (15.80) follows.

#### Proof

Let the number of connected block polymers of size n containing a fixed block be
bounded by

```math
N_n
\le
C_{\mathrm{blk}}^n .
\tag{15.88}
```

Using (15.87) as an absolute polymer majorant gives

```math
\sup_{Q_0}
\sum_{\Gamma\ni Q_0}
|w^s_{a,b}(\Gamma)|\,e^{\kappa|\Gamma|}
\le
\sum_{n\ge1}
\left(
C_{\mathrm{blk}}e^{\kappa-\tau_R}
\right)^n .
\tag{15.89}
```

The right-hand side is smaller than one when tau_R is chosen above the
entropy threshold. This is exactly the form required in (15.80). `∎`

So the task becomes a finite-energy estimate for local-lift defects under the
fiber measure. The natural proof is a repair map. For a connected defect polymer
Gamma, one wants a map

```math
\Phi_\Gamma:
\left\{
\Gamma\subset\mathfrak D_S(\bar U)
\right\}
\longrightarrow
\left\{
\Gamma\cap\mathfrak D_S(\Phi_\Gamma\bar U)=\varnothing
\right\}
\tag{15.90}
```

with four properties:

```math
\begin{array}{ll}
\text{fiber preservation:}
&
\mathbf 1^s_b(\Phi_\Gamma\bar U)
=
\mathbf 1^s_b(\bar U),
\\[1mm]
\text{locality:}
&
\Phi_\Gamma\bar U
=
\bar U
\text{ outside a fixed enlargement of }\Gamma,
\\[1mm]
\text{bounded multiplicity:}
&
\#\Phi_\Gamma^{-1}(\bar V)
\le
\exp(c_{\mathrm{mult}}|\Gamma|),
\\[1mm]
\text{action gain:}
&
\mathcal A^s_{a,b}(\bar U;\Gamma^+)
-
\mathcal A^s_{a,b}(\Phi_\Gamma\bar U;\Gamma^+)
\ge
\varepsilon_R|\Gamma|.
\end{array}
\tag{15.91}
```

Here

```math
\mathcal A^s_{a,b}(\bar U;B)
:=
-
\sum_{p\subset B}
\log
K_{t(a)}
\left(
b_p\,s(\bar U_p)
\right).
\tag{15.92}
```

If (15.91) held with

```math
\varepsilon_R
-
c_{\mathrm{mult}}
>
\log C_{\mathrm{blk}}
+
\kappa ,
\tag{15.93}
```

then (15.87) would follow by comparing every defective configuration with its
repaired image and summing over preimages. This would prove Target 40.15.

The local-curvature part of this repair picture is plausible. In tree gauge on
an enlarged block, a non-reconstructibly-good block satisfies a deterministic
curvature lower bound of the form

```math
M_Q(\bar U)>\rho
\quad\Longrightarrow\quad
\sum_{p\subset Q^+}
d_{SO(3)}
\left(
\bar U_p,
1
\right)^2
\ge
c_R\rho^2 .
\tag{15.94}
```

The heat-kernel weight gives the corresponding action cost, schematically

```math
-
\log
K_{t(a)}
\left(
b_p\,s(\bar U_p)
\right)
\gtrsim
\frac{1}{t(a)}
d_{SO(3)}
\left(
\bar U_p,
1
\right)^2
-
C_{t(a)} .
\tag{15.95}
```

Combining (15.94) and (15.95) suggests a local obstruction cost

```math
\Delta\mathcal A_Q
\gtrsim
\frac{c_R\rho^2}{t(a)}
-
C_R' .
\tag{15.96}
```

This is exactly the kind of estimate one would expect from asymptotic freedom at
small physical block scale. It is also exactly where the present argument stops,
because (15.96) only sees curvature-size defects. It does not control the full
canonical defect set (15.77).

Even the curvature part still needs a continuum-scaled non-Abelian Poincare
estimate behind (15.94), with constants that survive the limit at fixed physical
block scale. That is plausible but not supplied here.

There are two hard failures in the attempted proof.

First, gluing defects can be flat. The transition cochains between locally
trivial blocks obey

```math
\delta\tau_{QQ'}
=
1,
\qquad
[\tau]\in H^1(\mathcal G,Z_2).
\tag{15.97}
```

Such a defect can carry a nontrivial transition class without forcing large
plaquette holonomy on any individual block. Therefore the curvature Peierls
estimate does not price it.

Second, the repair map must stay inside the fixed-center fiber. The fiber
constraint is

```math
b\,c_s(\bar U)^{-1}
\in
\operatorname{im}
\left(
\delta:C^1(\Lambda,Z_2)\to C^2(\Lambda,Z_2)
\right).
\tag{15.98}
```

A local repair changes the section cocycle by some center two-cochain:

```math
c_s(\Phi_\Gamma\bar U)
=
h_\Gamma\,c_s(\bar U).
\tag{15.99}
```

The repaired configuration remains in the same fiber only if the new factor in
(15.99) is compatible with (15.98). Equivalently, it must be absorbable by a
link-sign coboundary, or else the repair has to drag a compensating sheet to the
boundary. That compensating sheet is precisely the kind of area-supported object
the route is trying to rule out.

So the first Peierls attempt gives a sharp partial result:

```math
\boxed{
\begin{array}{c}
\text{local curvature defects are Peierls-plausible,}\\[1mm]
\text{flat gluing defects and fiber-preserving repair are the real obstructions.}
\end{array}}
\tag{15.100}
```

The attempted next theorem is therefore not the whole KP estimate at once. It is
the following repair dichotomy.

**Target 40.18 (Fiber-Preserving Defect Repair Or Boundary Tethering).** For each
connected local-lift defect polymer Gamma in the interior of a spanning surface,
one must prove exactly one of the following:

```math
\begin{array}{ll}
\text{repair case:}
&
\text{there exists a map satisfying (15.91) with a uniform action gain,}
\\[1mm]
\text{tether case:}
&
\text{the defect carries a flat transition class forced to connect to }
C
\text{ or to the center sheet.}
\end{array}
\tag{15.101}
```

In the repair case, Criterion 40.17 gives a subcritical polymer gas. In the
tether case, the defect is not an independent area-bulk cancellation; it is
already tied to the boundary or to the center insertion being measured.

The next subsection audits this target. The conclusion is that Target 40.18 is
too strong as stated: it omits the collar condition needed for any local Peierls
repair.

### 15.16. Falsification Of Target 40.18 As Stated

Searchable falsification tag:

`V4P40-TARGET-4018-FALSIFIED-AS-STATED`.

Target 40.18 is false as stated. The missing hypothesis is a good collar around
the defect polymer. Without such a collar, a defect can be forced by ordinary
SO(3) holonomy in the exterior data. This obstruction is not a flat center
transition class, and a local repair cannot remove it while keeping the exterior
fixed.

**Theorem 40.19 (Bad-Collar Counterexample To Target 40.18).** Fix a connected
block set in the interior of the spanning surface and a local repair range. There
exist admissible exterior SO(3) data, with trivial center pairing, such that a
repair supported in the chosen range cannot remove the obstruction; it can only
move it into the collar. For such data, the two alternatives in Target 40.18 are
not exhaustive.

#### Proof

Choose an annular collar just outside the allowed repair range. In that collar,
fix the SO(3) link variables so that some collar loop has holonomy h satisfying

```math
d_{SO(3)}(h,1)
>
\rho ,
\tag{15.102}
```

while the center pairing around this collar obstruction is trivial:

```math
\prod_{p\in T} b_p
=
1 .
\tag{15.103}
```

Here T is any closed two-chain linking only the collar obstruction. This can be
done with h in the identity component of the chosen local chart but outside the
reconstruction ball. The obstruction is therefore ordinary SO(3) holonomy, not a
center transition class.

Any configuration that agrees with this exterior collar has the same collar
holonomy. If the interior block set and its collar were coherently good after a
local repair, the reconstructed lift on the enlarged region would imply that the
same collar holonomy lies inside the reconstruction ball:

```math
d_{SO(3)}(h,1)
\le
\rho .
\tag{15.104}
```

This contradicts (15.102). Thus a local repair supported inside the prescribed
range cannot remove the defect; it can only move the defect to the collar.

The tether alternative also fails. By (15.103), the obstruction has trivial
center pairing. So the defect is not forced to connect to the loop C or to the
center sheet. It is forced by noncenter SO(3) exterior holonomy. Therefore the
repair/tether dichotomy in Target 40.18 is not exhaustive. `∎`

This does not kill the conditional cocycle route. It says that the Peierls
repair must be formulated for maximal polymers with collars, not for arbitrary
connected defect sets under arbitrary exterior data.

Thus the falsification is precise: Target 40.18 fails when read literally for an
arbitrary connected defect set. If one silently intended a maximal canonical
component with a good collar, that hypothesis has to be written into the theorem.

The correct replacement is:

**Target 40.20 (Good-Collar Repair Or Center Tether).** Enlarge every connected
local-lift defect polymer until one of the following holds:

```math
\begin{array}{ll}
\text{bad-collar case:}
&
\text{the collar is not reconstructibly and coherently good,}
\\[1mm]
\text{good-collar case:}
&
\text{the collar is reconstructibly and coherently good.}
\end{array}
\tag{15.105}
```

In the bad-collar case, absorb the collar into the polymer and iterate. In the
good-collar case, prove the corrected dichotomy:

```math
\begin{array}{ll}
\text{repair case:}
&
\text{there is a fiber-preserving repair with uniform action gain,}
\\[1mm]
\text{center-tether case:}
&
\text{the obstruction pairs nontrivially with the fixed center field.}
\end{array}
\tag{15.106}
```

The topological half of this corrected target is already forced by the fiber
constraint. On every closed two-chain T contained in the good collar complement,
(15.98) gives

```math
\prod_{p\in T} c_s(\bar U;p)
=
\prod_{p\in T} b_p ,
\tag{15.107}
```

because the coboundary term has trivial pairing with closed chains. Therefore a
flat gluing obstruction that cannot be removed inside a good collar is visible
in the fixed center field. It is a center tether, not a free coset cancellation.

The analytic half remains open. One still has to prove that, when the collar is
good and the center pairing in (15.107) is trivial, a fiber-preserving repair
with action gain exists:

```math
\boxed{
\begin{array}{c}
\text{good collar}\\
+\\
\text{trivial center pairing}\\
\Longrightarrow\\
\text{fiber-preserving repair with uniform action gain.}
\end{array}}
\tag{15.108}
```

This is the corrected topological theorem. Target 40.18 failed because it tried
to repair non-isolated polymers. Target 40.20 repairs only isolated polymers,
and it charges non-isolated ones to the larger polymer that contains their bad
collar.

The analytic repair claim in (15.108) still has to be audited. The next
subsection shows that it is false in the identity-good-block variables.

### 15.17. Falsification Of The Identity-Good Action-Gain Repair

Searchable action-gain falsification tag:

`V4P40-IDENTITY-GOOD-ACTION-GAIN-FAILS`.

The good-collar and trivial-center-pairing hypotheses remove the topological
obstruction, but they do not by themselves give a uniform action-gain repair.
The reason is simple: a center field that is cohomologically trivial can still
be locally nontrivial. In the fixed-center fiber, such a local center coboundary
can make the heat-kernel action prefer an SO(3) plaquette outside the identity
reconstruction ball.

**Theorem 40.21 (No Uniform Identity-Good Action Gain).** The implication
(15.108) is false as stated along the small-t continuum side of the heat-kernel
trajectory. There are good-collar, trivial-center-pairing local configurations
for which every repair that makes the defect identity-good increases the
fixed-fiber action on at least one plaquette. Hence no repair map can satisfy the
action-gain line of (15.91) uniformly in the center field.

#### Proof

Work in the principal SU(2) chart near the identity. Let theta_rho be the
corresponding SU(2) angular radius for the SO(3) reconstruction radius:

```math
0<\theta_\rho<\frac{\pi}{2}.
\tag{15.109}
```

Choose a plaquette in the interior of a good collar and choose the fixed center
field to be locally nontrivial on that plaquette:

```math
b_p=-1.
\tag{15.110}
```

This does not contradict trivial center pairing: take the local center field to
be a coboundary in the repair region, so its pairing with every closed two-chain
in the good collar complement is trivial.

It is enough to test the claimed uniform repair theorem on this finite Dirichlet
patch, because the estimate in (15.91) is local and is required uniformly over
admissible exterior data.

Choose the remaining plaquette variables in the repair support already at their
local fixed-center action minima, subject to the good collar data. Then any
possible action gain must come from the plaquette displayed below; there is no
reserve of neighboring excess action available to compensate it.

For the SO(3) plaquette variable, choose a section lift with SU(2) angle theta
satisfying

```math
\theta_\rho
<
\theta
\le
\frac{\pi}{2}.
\tag{15.111}
```

This plaquette is outside the identity-good reconstruction ball. Its contribution
to the fixed-fiber action is

```math
A_{\mathrm{bad}}
=
-
\log
K_t
\left(
-e^{\theta X}
\right),
\tag{15.112}
```

where X is a unit Lie-algebra direction. Any repair that makes the plaquette
identity-good must replace theta by some theta prime with

```math
0
\le
\theta'
\le
\theta_\rho .
\tag{15.113}
```

Its repaired action contribution is therefore bounded below by the best
identity-good value

```math
A_{\mathrm{good}}
\ge
-
\log
K_t
\left(
-e^{\theta_\rho X}
\right).
\tag{15.114}
```

For the SU(2) heat kernel at small t, the logarithmic leading term is the squared
geodesic distance to the identity:

```math
-
\log K_t(g)
=
\frac{d_{SU(2)}(g,1)^2}{4t}
+O(\log t).
\tag{15.115}
```

The distance of the bad plaquette argument to the identity is

```math
d_{SU(2)}
\left(
-e^{\theta X},
1
\right)
=
\pi-\theta,
\tag{15.116}
```

whereas the best identity-good repaired value has distance

```math
d_{SU(2)}
\left(
-e^{\theta_\rho X},
1
\right)
=
\pi-\theta_\rho .
\tag{15.117}
```

Since theta is larger than theta_rho, the bad plaquette has smaller action than
every identity-good repair for sufficiently small t:

```math
A_{\mathrm{bad}}
<
A_{\mathrm{good}}.
\tag{15.118}
```

Thus the action difference in the repair direction has the wrong sign:

```math
\mathcal A^s_{a,b}(\bar U;\Gamma^+)
-
\mathcal A^s_{a,b}(\Phi_\Gamma\bar U;\Gamma^+)
<
0.
\tag{15.119}
```

This contradicts the required positive action gain in (15.91). The obstruction
is not topological: the center field was chosen cohomologically trivial in the
repair region. It is energetic. The identity-good definition is not adapted to
the fixed center field. `∎`

This falsification is important. It means the conditional cocycle route cannot
use identity-good blocks uniformly over the center marginal. A local center
coboundary can be cheapened by spreading its cost into the SO(3) plaquette
variable, and that spreading is precisely an identity-good defect.

The correct next definition must be center-adapted. In a region where the center
field has trivial pairing, choose a local center one-cochain satisfying

```math
b_p
=
(\delta\zeta)_p
\qquad
\text{inside the repair region.}
\tag{15.120}
```

Then define the local action-good condition using the actual SU(2) plaquette
argument

```math
b_p\,s(\bar U_p),
\tag{15.121}
```

not the SO(3) distance of the plaquette to the identity alone. The repaired
state should be close to the local minimizer of the fixed-fiber action:

```math
b_p\,s(\bar U_p)
\approx
1.
\tag{15.122}
```

The corrected analytic target is therefore:

**Target 40.22 (Center-Adapted Good-Collar Repair).** Under a good collar and
trivial center pairing, replace identity-good defects by center-adapted action
defects. Prove that every isolated center-adapted defect admits a
fiber-preserving repair with uniform action gain:

```math
\boxed{
\begin{array}{c}
\text{good collar}\\
+\\
\text{trivial center pairing}\\
+\\
\text{center-adapted badness}\\
\Longrightarrow\\
\text{fiber-preserving action-decreasing repair.}
\end{array}}
\tag{15.123}
```

This is narrower and more honest than (15.108). The repair must lower the
fixed-center heat-kernel action, not force the SO(3) variable back toward the
identity when the fixed center field energetically prefers otherwise.

### 15.18. Falsification Of Target 40.22 As Stated

Searchable center-adapted falsification tag:

`V4P40-CENTER-ADAPTED-REPAIR-FAILS-AS-STATED`.

Target 40.22 fixes the local center-sign mistake, but it still misses one more
obstruction: flat noncenter SO(3) holonomy in the collar. A collar can be locally
good on every contractible block and still carry nontrivial SO(3) holonomy around
the defect. That holonomy is invisible to the center pairing. It can force
interior plaquette action, and if the interior is already the Dirichlet minimizer,
there is no action-decreasing repair.

**Theorem 40.23 (Flat-Coset-Collar Counterexample To Target 40.22).** Target
40.22 is false as stated. Good collar, trivial center pairing, and
center-adapted bad plaquettes do not imply the existence of a fiber-preserving
repair with uniform action gain.

#### Proof

Take a repair region D surrounded by an annular collar A. Choose the center field
to be trivial on the union:

```math
b_p
=
1
\qquad
\text{for }p\subset D\cup A.
\tag{15.124}
```

Thus all center pairings in the collar complement are trivial.

Now choose an SO(3) connection on the collar which is flat on every collar
plaquette:

```math
\bar U_p
=
1
\qquad
\text{for }p\subset A,
\tag{15.125}
```

but has nontrivial holonomy around the hole enclosed by the collar:

```math
\operatorname{Hol}_{\gamma_A}(\bar U)
=
h,
\qquad
h\ne 1.
\tag{15.126}
```

This is possible because the annular collar is not simply connected. Every
contractible block in the collar is reconstructibly good, and the center cocycle
glues coherently there. Hence the collar is good in the sense used in Target
40.22.

Let rho_act be the center-adapted action-good radius. Take the repair disk small
enough, one plaquette if necessary, and choose the collar holonomy so that it
cannot be filled by plaquettes all lying inside that action-good ball. For
example, if n_D is the number of plaquettes in a spanning disk for the hole,
choose h with

```math
d_{SO(3)}(h,1)
>
n_D\,\rho_{\mathrm{act}} .
\tag{15.127}
```

If every interior center-adapted plaquette argument were action-good, the
non-Abelian product estimate along the disk would give

```math
d_{SO(3)}(h,1)
\le
n_D\,\rho_{\mathrm{act}},
\tag{15.128}
```

contradicting (15.127). Therefore every filling of the collar data contains at
least one center-adapted bad plaquette.

Now minimize the fixed-center heat-kernel action over all admissible SO(3) fiber
links in D with the collar data fixed. The finite-dimensional admissible domain
is compact and the action is continuous on this local chart, so a minimizer
exists:

```math
\bar U_\ast
\in
\operatorname*{arg\,min}_{\substack{\bar V|_A=\bar U|_A\\
\mathbf 1^s_b(\bar V)=1}}
\mathcal A^s_{a,b}(\bar V;D).
\tag{15.129}
```

By the preceding paragraph, this minimizer still contains a center-adapted bad
plaquette. It is an isolated center-adapted defect inside a good collar with
trivial center pairing.

But no repair supported in D and preserving the collar data can lower the action,
because the configuration is already a Dirichlet minimizer:

```math
\mathcal A^s_{a,b}(\bar U_\ast;D)
-
\mathcal A^s_{a,b}(\Phi\bar U_\ast;D)
\le
0
\tag{15.130}
```

for every admissible fiber-preserving repair Phi. This contradicts the positive
uniform action gain demanded by Target 40.22. `∎`

This counterexample is not a center-sign artifact. The center field was trivial.
The obstruction is a flat coset collar: a noncenter SO(3) holonomy can force
interior action while all local collar plaquettes remain good.

Thus the correct next target must include the full Dirichlet coset holonomy, not
only the center pairing. The right dichotomy is:

```math
\boxed{
\begin{array}{c}
\text{either the collar carries nontrivial SO(3) Dirichlet holonomy,}\\[1mm]
\text{or defects are measured as excess above the local Dirichlet minimizer.}
\end{array}}
\tag{15.131}
```

Call the first case a coset tether. It is not a center tether, but it is also not
a freely floating bulk cancellation: it is tied to boundary SO(3) data around the
polymer.

The corrected analytic target is therefore:

**Target 40.24 (Dirichlet-Adapted Repair Or Coset Tether).** For each isolated
polymer with a good collar and trivial center pairing, prove one of the following:

```math
\begin{array}{ll}
\text{coset-tether case:}
&
\operatorname{Hol}_{\gamma_A}(\bar U)
\ne
1,
\\[1mm]
\text{Dirichlet-excess case:}
&
\mathcal A^s_{a,b}(\bar U;D)
-
\mathcal A^s_{a,b}(\bar U_\ast;D)
\ge
\varepsilon_R|\Gamma|.
\end{array}
\tag{15.132}
```

In the second case the repair is tautological but valid: replace the interior
configuration by the Dirichlet minimizer. This preserves the collar data and the
fixed center fiber, and gives the action gain displayed in (15.132).

So Target 40.22 is not the right theorem. The real theorem must control two
objects: Dirichlet action excess and flat SO(3) collar holonomy. The latter is
where the center-resolved route meets the ordinary non-Abelian IR mixing problem.

### 15.19. Target 40.24: Exact Repair And The Missing Gap

Searchable Dirichlet-repair tag:

`V4P40-DIRICHLET-REPAIR-EXCESS-GAP`.

Target 40.24 has one part that is a theorem and one part that is not. The
theorem is the repair of Dirichlet excess. The non-theorem is the assumption
that every isolated center-adapted defect automatically carries a uniform
Dirichlet excess gap.

Fix a repair region D, a collar A, the center field b, and the SO(3) collar data
xi. The admissible Dirichlet fiber is

```math
\mathcal F^s_{D,A}(b,\xi)
:=
\left\{
\bar V_D:
\bar V|_A=\xi,\quad
\mathbf 1^s_b(\bar V)=1
\right\}.
\tag{15.133}
```

The local Dirichlet minimizer set is

```math
\mathcal M^s_{D,A}(b,\xi)
:=
\operatorname*{arg\,min}_{\bar V\in\mathcal F^s_{D,A}(b,\xi)}
\mathcal A^s_{a,b}(\bar V;D).
\tag{15.134}
```

For any admissible configuration define its Dirichlet excess by

```math
\mathcal E^s_{D,A}(\bar U\mid b,\xi)
:=
\mathcal A^s_{a,b}(\bar U;D)
-
\inf_{\bar V\in\mathcal F^s_{D,A}(b,\xi)}
\mathcal A^s_{a,b}(\bar V;D).
\tag{15.135}
```

Also let the collar coset holonomy record be the collection of all noncontractible
collar loop holonomies:

```math
\mathfrak H_A(\xi)
:=
\left\{
\operatorname{Hol}_{\gamma}(\xi):
\gamma\in H_1(A)
\right\}.
\tag{15.136}
```

**Theorem 40.25 (Dirichlet-Excess Repair Is Exact).** Suppose the admissible
Dirichlet fiber is nonempty. Choose any minimizer

```math
\bar U_\ast\in\mathcal M^s_{D,A}(b,\xi).
\tag{15.137}
```

The repair map that replaces the interior field by the minimizer and leaves the
collar fixed is fiber-preserving. Its action gain is exactly the Dirichlet
excess:

```math
\mathcal A^s_{a,b}(\bar U;D)
-
\mathcal A^s_{a,b}(\bar U_\ast;D)
=
\mathcal E^s_{D,A}(\bar U\mid b,\xi).
\tag{15.138}
```

Consequently, if a connected polymer Gamma is defined by the superlevel condition

```math
\mathcal E^s_{D,A}(\bar U\mid b,\xi)
\ge
\varepsilon_R|\Gamma|,
\tag{15.139}
```

then the action-gain line in (15.91) holds with the same epsilon_R.

#### Proof

The minimizer lies in the same admissible Dirichlet fiber by definition of
(15.134). Replacing the interior by that minimizer leaves the collar data fixed
and keeps the center constraint in (15.133). Subtracting the minimal action from
the original action gives exactly (15.138). If the superlevel condition (15.139)
is imposed as the polymer definition, the required action gain is immediate. `∎`

This proves the repair half of Target 40.24. But it also exposes the missing
ingredient: one must prove that the defects being counted are actually excess
polymers. That does not follow from good collar and trivial center pairing.

**Theorem 40.26 (No Automatic Dirichlet Gap).** Good collar, trivial center
pairing, and trivial collar coset holonomy do not imply a uniform lower bound on
Dirichlet excess. In any admissible Dirichlet fiber containing a nonconstant
continuous path from a minimizer, for every positive epsilon there are
configurations with

```math
\mathfrak H_A(\xi)=\{1\},
\qquad
0
<
\mathcal E^s_{D,A}(\bar U\mid b,\xi)
<
\varepsilon|\Gamma|.
\tag{15.140}
```

#### Proof

Let

```math
\bar U_\ast\in\mathcal M^s_{D,A}(b,\xi)
\tag{15.141}
```

and let

```math
r\mapsto \bar U_r
\tag{15.142}
```

be a nonconstant continuous path in the same admissible Dirichlet fiber, with
the collar fixed and

```math
\bar U_0=\bar U_\ast .
\tag{15.143}
```

The action is continuous on the finite-dimensional lattice configuration space.
Therefore

```math
\mathcal E^s_{D,A}(\bar U_r\mid b,\xi)
\longrightarrow
0
\qquad
\text{as }r\to0.
\tag{15.144}
```

For nonzero r chosen small enough, the configuration is distinct from the
minimizer but has Dirichlet excess below any prescribed positive threshold. The
collar data have not changed, so trivial collar holonomy and trivial center
pairing persist. This gives (15.140). `∎`

Thus Target 40.24 is not a theorem about the original defect set unless the
defect set is redefined by Dirichlet excess. There is a third sector:

```math
\boxed{
\begin{array}{c}
\mathfrak H_A(\xi)=\{1\},\\[1mm]
0<
\mathcal E^s_{D,A}(\bar U\mid b,\xi)
<
\varepsilon_R|\Gamma|.
\end{array}}
\tag{15.145}
```

These are soft Dirichlet fluctuations. They are not Peierls polymers. They have
to be controlled by a local spectral-gap, Poincare, or Gaussian fluctuation
estimate, not by an action-gain contour repair.

The corrected decomposition is therefore:

```math
\boxed{
\begin{array}{lll}
\text{coset tether}
&:&
\mathfrak H_A(\xi)\ne\{1\},
\\[1mm]
\text{excess polymer}
&:&
\mathcal E^s_{D,A}(\bar U\mid b,\xi)\ge\varepsilon_R|\Gamma|,
\\[1mm]
\text{soft fluctuation}
&:&
\mathfrak H_A(\xi)=\{1\}
\text{ and }
\mathcal E^s_{D,A}(\bar U\mid b,\xi)<\varepsilon_R|\Gamma|.
\end{array}}
\tag{15.146}
```

Only the middle line is repaired by Theorem 40.25. The first line is the
non-Abelian coset-tether problem. The third line is the perturbative fluctuation
problem. The next fixed-IR theorem must prove that the first and third lines
cannot create area-order cancellation of the center sheet.

### 15.20. Dirichlet Response Reformulation

Searchable Dirichlet-response tag:

`V4P40-DIRICHLET-RESPONSE-REFORMULATION`.

The defect language has now done its job. It exposed the wrong local variables.
The invariant object is not a good block, a bad block, or an identity-centered
repair. The invariant object is the normalized Dirichlet response of an interior
region to its collar data, with the center field fixed.

This is the Einstein/Feynman move in this problem: choose the invariant boundary
question first, then compute the conditional kernel around the true Dirichlet
minimizer rather than around the identity.

Fix an interior region D, a collar A, a center field b, and SO(3) collar data xi.
Let

```math
P(D,A)
```

be the set of plaquettes whose kernel depends on at least one interior link and
whose remaining links lie in D together with its collar. For a bounded interior
observable O, define the unnormalized Dirichlet response

```math
Z^s_D(O\mid b,\xi)
:=
\int_{\mathcal F^s_{D,A}(b,\xi)}
O(\bar V_D,\xi)
\prod_{p\in P(D,A)}
K_{t(a)}
\left(
b_p\,s(\bar V_p)
\right)
\prod_{\ell\subset D^\circ}d\bar V_\ell .
\tag{15.147}
```

The normalized Dirichlet response is

```math
\mathcal R^s_D(O\mid b,\xi)
:=
\frac{
Z^s_D(O\mid b,\xi)
}{
Z^s_D(1\mid b,\xi)
},
\tag{15.148}
```

whenever the denominator is nonzero.

For the cocycle route, the relevant local observable is the piece of the
surface-cocycle amplitude inside D:

```math
\mathcal O^s_{D;C,S}(\bar V_D,\xi)
:=
\left(
\prod_{p\in S\cap D}
c_s(\bar V,\xi;p)^{-1}
\right)
L^s_{D;C}(\bar V,\xi).
\tag{15.149}
```

Here the factor

```math
L^s_{D;C}(\bar V,\xi)
\tag{15.150}
```

is the section-lifted loop factor contributed by D if D meets C; for bulk
regions disjoint from C it is equal to one.

**Theorem 40.27 (Exact Dirichlet Response Identity).** Let the fixed-center
fiber law be (15.85), and use its regular conditional distribution with respect
to the exterior SO(3) data. Conditional on the exterior data restricting to xi on
the collar A, every bounded observable O supported in D satisfies

```math
\mathbb E_{\nu^s_{a,b}}
\left[
O
\mid
\bar U|_A=\xi
\right]
=
\mathcal R^s_D(O\mid b,\xi).
\tag{15.151}
```

Consequently the conditional cocycle amplitude can be computed by iterating
Dirichlet response kernels over any finite collar atlas of the spanning surface:

```math
\alpha^s_{C,S}(b)
=
\mathbb E_{\mathrm{collars}}
\left[
\mathcal R^s_{D_1}
\circ
\mathcal R^s_{D_2}
\circ
\cdots
\circ
\mathcal R^s_{D_m}
\left(
A^s_{C,S}
\right)
\right].
\tag{15.152}
```

The composition notation means successive conditional expectations, not
independence of the regions.

#### Proof

Fix the exterior data. In the finite product integral (15.85), all plaquette
factors that depend on an interior link, together with the fiber admissibility
constraint, are exactly the integrand in (15.147). All factors depending only on
the exterior are constant under the conditional integral and cancel between
numerator and denominator. This gives (15.151). Iterating the tower property of
conditional expectation over the chosen collar atlas gives (15.152). `∎`

The three-way split in (15.146) now becomes a split of one exact response kernel.
For fixed collar data:

```math
\mathcal R^s_D(O\mid b,\xi)
=
\lambda_{\mathrm{soft}}\,
\mathcal R^s_{D,\mathrm{soft}}(O\mid b,\xi)
+
\lambda_{\mathrm{ex}}\,
\mathcal R^s_{D,\mathrm{ex}}(O\mid b,\xi),
\tag{15.153}
```

where the soft and excess sectors are defined by the Dirichlet excess threshold,
and the weights sum to one. If

```math
\mathfrak H_A(\xi)\ne\{1\},
\tag{15.154}
```

then the whole response is assigned to a coset-tether sector rather than to a
repair sector.

Theorem 40.25 says exactly what happens in the excess sector: replacing the
interior by the Dirichlet minimizer gives the action decrease equal to the
Dirichlet excess. The remaining work is not another repair lemma. It is a
locality theorem for the response kernel.

**Criterion 40.28 (Dirichlet Response Locality Implies Conditional Decorrelation).**
Suppose that at a fixed physical block scale the following three estimates hold
uniformly along the continuum trajectory.

First, excess sectors are Kotecky-Preiss summable:

```math
\sup_{Q_0}
\sum_{\Gamma\ni Q_0}
|w_{\mathrm{ex}}(\Gamma)|e^{\kappa|\Gamma|}
\le
\eta
<
1.
\tag{15.155}
```

Second, in the soft sector with trivial collar holonomy, the local cocycle
response is boundary/quasilocal:

```math
\left|
\mathcal R^s_{D,\mathrm{soft}}
\left(
\mathcal O^s_{D;C,S}
\mid b,\xi
\right)
-
B^s_{\partial D;C,S}(b,\xi)
\right|
\le
K e^{-m\,\operatorname{dist}(D_{\mathrm{bulk}},\partial D)}.
\tag{15.156}
```

Third, coset-tether sectors are themselves summable as collar polymers:

```math
\sup_{Q_0}
\sum_{\Theta\ni Q_0}
|w_{\mathrm{coset}}(\Theta)|e^{\kappa|\Theta|}
\le
\eta
<
1.
\tag{15.157}
```

Then the conditional amplitude has a boundary/quasilocal decomposition of the
form

```math
\alpha^s_{C,S}(b)
=
\Gamma^s_C(b)
+
R^s_{C,S}(b),
\tag{15.158}
```

with the remainder controlled by summable excess and coset-tether polymers.
When this decomposition is paired with the corresponding center-sheet disorder
estimate, it gives the hypothesis of Criterion 40.6.

#### Proof

Use the exact response identity (15.152). The excess part is controlled by the
polymer estimate (15.155), with Theorem 40.25 supplying the action-gain repair
behind the activities. The soft part is replaced by its boundary/quasilocal
representative using (15.156). The nontrivial collar-holonomy part is controlled
by the coset-tether polymer estimate (15.157). The absolutely summable pieces can
reach the loop boundary only with summable tails, so the iterated response kernel
reduces to a loop-local term plus the remainder in (15.158). With the matching
center-sheet disorder estimate, Criterion 40.6 turns this conditional
decorrelation estimate into the Wilson sheet-domination bound. `∎`

This is now the cleanest fixed-IR formulation of the route. It no longer asks
whether a hand-chosen defect is repairable. It asks whether the exact Dirichlet
response kernel is local.

The remaining theorem is:

**Target 40.29 (Uniform Dirichlet Response Locality).** Prove, or disprove, the
three estimates (15.155)-(15.157) for the actual constrained SO(3) fiber measure
at fixed physical block scale.

Equivalently:

```math
\boxed{
\begin{array}{c}
\text{control excess polymers by Dirichlet action,}\\[1mm]
\text{control soft fluctuations by a uniform local spectral-gap or Poincare
estimate,}\\[1mm]
\text{control flat SO(3) collar holonomy by a coset-tether locality estimate.}
\end{array}}
\tag{15.159}
```

This is where the center-resolved route meets the shared four-dimensional floor
in its sharpest form. The center sheet is explicit. The cocycle is exact. The
remaining problem is the locality of the non-Abelian Dirichlet response.

### 15.21. Target 40.29 As Stated: Exact Holonomy Is The Wrong Split

Searchable Target-40.29 audit tag:

`V4P40-TARGET-4029-EXACT-HOLONOMY-FAILS`.

Target 40.29 is still too sharp in the wrong place. It splits the Dirichlet
response by exact triviality of the collar SO(3) holonomy. That is not a stable
probabilistic event. The identity element is a measure-zero point in a continuous
compact Lie group. Therefore exact nontrivial holonomy is generic, not a rare
polymer event.

**Theorem 40.30 (Exact-Holonomy Coset Tethers Are Not Subcritical).** The
coset-tether estimate (15.157) cannot hold with the split (15.154) under any
nondegenerate heat-kernel Dirichlet response. In particular, classifying every
collar with nonidentity SO(3) holonomy as a coset tether makes the coset-tether
sector occur with probability one for generic collar data.

#### Proof

Fix a collar A with at least one noncontractible loop. Let gamma be such a loop.
Under the positive heat-kernel measure at finite cutoff, the induced distribution
of the collar holonomy

```math
\operatorname{Hol}_{\gamma}(\xi)
\tag{15.160}
```

is absolutely continuous with respect to Haar measure on SO(3), except on
degenerate boundary constraints. Haar measure assigns zero mass to the identity:

```math
\operatorname{Haar}_{SO(3)}(\{1\})
=
0.
\tag{15.161}
```

Therefore

```math
\mathbb P
\left[
\operatorname{Hol}_{\gamma}(\xi)\ne1
\right]
=
1.
\tag{15.162}
```

Thus the condition in (15.154) is not a rare event. If each such collar is treated
as a polymer, then typical configurations contain coset-tether collars
everywhere. A polymer gas that occupies every block almost surely cannot satisfy
a Kotecky-Preiss subcriticality estimate of the form (15.157). `∎`

This is not a physical obstruction. It is a classification error. Small collar
holonomies are soft fluctuations, not tethers. Only holonomies above a fixed
physical threshold should be charged as coset-tether polymers.

Define the collar holonomy size by choosing a finite basis of noncontractible
collar loops and setting

```math
\mathfrak h_A(\xi)
:=
\max_{\gamma\in\mathcal B_A}
d_{SO(3)}
\left(
\operatorname{Hol}_{\gamma}(\xi),
1
\right).
\tag{15.163}
```

Choose a physical holonomy threshold

```math
0<\rho_H<\rho_{\mathrm{chart}}.
\tag{15.164}
```

The corrected decomposition of one Dirichlet response is:

```math
\boxed{
\begin{array}{lll}
\text{large coset tether}
&:&
\mathfrak h_A(\xi)\ge\rho_H,
\\[1mm]
\text{excess polymer}
&:&
\mathfrak h_A(\xi)<\rho_H
\text{ and }
\mathcal E^s_{D,A}(\bar U\mid b,\xi)\ge\varepsilon_R|\Gamma|,
\\[1mm]
\text{soft response}
&:&
\mathfrak h_A(\xi)<\rho_H
\text{ and }
\mathcal E^s_{D,A}(\bar U\mid b,\xi)<\varepsilon_R|\Gamma|.
\end{array}}
\tag{15.165}
```

Now the repair theorem applies only to the middle line, exactly as Theorem 40.25
proved. The large-holonomy line is a genuine polymer candidate. The small-holonomy
line is the perturbative/soft response.

The corrected target replacing Target 40.29 is therefore:

**Target 40.31 (Thresholded Uniform Dirichlet Response Locality).** Prove, or
disprove, the following three estimates at fixed physical block scale.

First, excess polymers are summable:

```math
\sup_{Q_0}
\sum_{\Gamma\ni Q_0}
|w_{\mathrm{ex}}(\Gamma)|e^{\kappa|\Gamma|}
\le
\eta
<
1.
\tag{15.166}
```

Second, large collar-holonomy polymers are summable:

```math
\sup_{Q_0}
\sum_{\Theta\ni Q_0}
|w_{\mathrm{hol}}(\Theta)|e^{\kappa|\Theta|}
\le
\eta
<
1.
\tag{15.167}
```

Third, in the soft sector, where both the holonomy size and Dirichlet excess are
below threshold, the Dirichlet response is boundary/quasilocal:

```math
\left|
\mathcal R^s_{D,\mathrm{soft}}
\left(
\mathcal O^s_{D;C,S}
\mid b,\xi
\right)
-
B^s_{\partial D;C,S}(b,\xi)
\right|
\le
K e^{-m\,\operatorname{dist}(D_{\mathrm{bulk}},\partial D)}.
\tag{15.168}
```

**Criterion 40.32 (Thresholded Response Locality Suffices).** If (15.166),
(15.167), and (15.168) hold uniformly along the continuum trajectory, then the
conclusion of Criterion 40.28 holds.

#### Proof

The proof is the same as Criterion 40.28, but with the corrected split (15.165).
The exact repair theorem controls the excess line. The large-holonomy line is
controlled by (15.167). The soft line is controlled directly by (15.168). These
three contributions exhaust the Dirichlet response, so the iterated response
kernel again reduces to a boundary/quasilocal term plus summable tails. `∎`

This is the real Target 40.29 after audit:

```math
\boxed{
\begin{array}{c}
\text{do not ask whether collar holonomy is exactly trivial;}\\[1mm]
\text{ask whether large collar holonomy is subcritical,}\\[1mm]
\text{and whether small-holonomy soft response has uniform locality.}
\end{array}}
\tag{15.169}
```

This corrected target now has to be audited line by line. The excess line is a
repair/free-energy problem. The large-holonomy line is not automatically a
Peierls problem in four dimensions. The soft line is harmless only if it is
really chart-confined; otherwise it hides an ordinary SO(3) response-locality
problem.

### 15.22. Full Investigation Of Target 40.31

Searchable Target-40.31 audit tag:

`V4P40-TARGET-4031-FULL-AUDIT`.

Target 40.31 is now sharp enough to investigate. Its conclusion is mixed:

```math
\boxed{
\begin{array}{lll}
\text{excess polymers} &:&
\text{conditionally reducible to a free-energy Peierls estimate,}\\[1mm]
\text{large collar holonomy} &:&
\text{not controlled by a uniform bare action gap in four dimensions,}\\[1mm]
\text{soft response} &:&
\text{valid by exact cocycle trivialization only after chart confinement.}
\end{array}}
\tag{15.170}
```

Thus Target 40.31 is not proved by the machinery developed so far. It is also
not simply false as a probabilistic statement. What is false is the most natural
action-Peierls proof of its large-holonomy line.

**Proposition 40.33 (Excess Summability Is Conditional On A Free-Energy
Multiplicity Bound).** Suppose the exact excess-sector activities obey

```math
|w_{\mathrm{ex}}(\Gamma)|
\le
\exp
\left(
-
\left(
\varepsilon_R-c_{\mathrm{fluc}}
\right)
|\Gamma|
\right)
\tag{15.171}
```

with constants independent of the cutoff at the chosen physical block scale.
If

```math
\varepsilon_R-c_{\mathrm{fluc}}
>
\log C_{\mathrm{blk}}+\kappa ,
\tag{15.172}
```

where

```math
N_n\le C_{\mathrm{blk}}^n
\tag{15.173}
```

bounds the number of connected block polymers of size n through a fixed block,
then the excess estimate (15.166) holds.

#### Proof

Using (15.171) and (15.173),

```math
\sup_{Q_0}
\sum_{\Gamma\ni Q_0}
|w_{\mathrm{ex}}(\Gamma)|e^{\kappa|\Gamma|}
\le
\sum_{n\ge1}
\left(
C_{\mathrm{blk}}
e^{\kappa-\varepsilon_R+c_{\mathrm{fluc}}}
\right)^n .
\tag{15.174}
```

The series is smaller than one after decreasing the right side of (15.172) by a
fixed margin. This gives (15.166). `∎`

This proposition explains exactly what Theorem 40.25 bought. It converted
excess into action gain. It did not bound the fluctuation determinant,
continuous multiplicity, or local free-energy loss represented by

```math
c_{\mathrm{fluc}} .
\tag{15.175}
```

At fixed physical block scale that constant is a continuum finite-volume
free-energy problem, not a combinatorial identity.

The large-holonomy line has a sharper obstruction.

**Theorem 40.34 (No Uniform Bare Action Gap For Fixed Physical Collar Holonomy
In Four Dimensions).** Let a collar loop have fixed physical size and bound a
lattice plaquette disk with

```math
N_a\asymp R^2a^{-2}
\tag{15.176}
```

plaquettes. For every sufficiently small threshold below the chart radius there
are trivial-center SO(3) lattice connections whose collar holonomy is above
threshold but whose heat-kernel action excess over the identity satisfies

```math
\Delta\mathcal A_a
\le
\frac{C\rho_H^2}{N_a\,t(a)}
+
o
\left(
\frac{1}{N_a\,t(a)}
\right).
\tag{15.177}
```

Along an asymptotically-free heat-kernel trajectory,

```math
N_a\,t(a)\longrightarrow\infty ,
\tag{15.178}
```

so the right hand side tends to zero. Consequently no cutoff-uniform positive
action gap can imply the large-holonomy polymer estimate (15.167).

#### Proof

Choose a one-parameter subgroup of SO(3), and choose an element X in its Lie
algebra so that

```math
d_{SO(3)}
\left(
\exp X,1
\right)
\ge
\rho_H .
\tag{15.179}
```

On a fixed-thickness lattice slab around the plaquette disk choose an abelian
lattice connection whose tangential disk plaquette holonomy is

```math
\exp
\left(
\frac{X}{N_a}
\right)
\tag{15.180}
```

on each disk plaquette, with only a constant multiple of N_a plaquettes in the
slab differing from the identity. This can be done in axial gauge inside the
chosen abelian subgroup. The ordered product of the tangential plaquettes over
the disk is then

```math
\left(
\exp
\left(
\frac{X}{N_a}
\right)
\right)^{N_a}
=
\exp X .
\tag{15.181}
```

Hence the collar loop has holonomy at least rho_H. Each plaquette remains in the
principal chart for sufficiently small lattice spacing, so the section cocycle
is trivial on the slab and the center field can be chosen trivial.

The small-time heat-kernel action above the identity is quadratic to leading
order:

```math
-
\log K_{t(a)}
\left(
\exp
\left(
\frac{X}{N_a}
\right)
\right)
+
\log K_{t(a)}(1)
\le
\frac{C|X|^2}{N_a^2\,t(a)}
+
o
\left(
\frac{1}{N_a^2\,t(a)}
\right).
\tag{15.182}
```

Summing over a constant multiple of N_a plaquettes gives (15.177), after
absorbing the slab-thickness constant into C. The asymptotically-free scaling
has t(a) going to zero only logarithmically, while N_a grows quadratically in
inverse lattice spacing, so (15.178) holds. `∎`

This theorem does not prove that (15.167) is false as a renormalized
free-energy statement. It proves something narrower and important: the
large-holonomy estimate cannot be obtained from a deterministic local
heat-kernel action gap. A proof of (15.167) would need a genuine marginal
collar-law estimate, or a blocked response estimate, not merely a repair map.

Equivalently, the following tempting implication is false:

```math
\boxed{
\mathfrak h_A(\xi)\ge\rho_H
\quad\Longrightarrow\quad
\mathcal A^s_{a,b}
\left(
\bar U;D\cup A
\right)
-
\mathcal A^s_{a,b}
\left(
\mathbf 1;D\cup A
\right)
\ge
\tau_H
}
\tag{15.183}
```

with tau_H independent of the cutoff.

The soft line needs a different sharpening. Soft continuous fluctuations should
not be asked to generate a mass gap for free. For the cocycle problem, the right
question is whether the soft sector stays inside one coherent lift chart.

Define the chart-confined event by requiring that the block family in

```math
D\cup A
\tag{15.184}
```

is reconstructibly and coherently good in the sense of Section 15.14. Denote it
by

```math
\mathcal C_{\mathrm{chart}}(D,A).
\tag{15.185}
```

**Proposition 40.35 (Chart-Confined Soft Response Is Boundary Exact).** On the
chart-confined event, for every bulk region D disjoint from the loop C, the
surface cocycle observable reduces to a boundary observable:

```math
\mathcal O^s_{D;C,S}
=
B^s_{\partial D;C,S}
\qquad
\text{on }
\mathcal C_{\mathrm{chart}}(D,A).
\tag{15.186}
```

Consequently the soft estimate (15.168) holds on this event with zero bulk
remainder.

#### Proof

On a coherently good block family there is a single center one-cochain
trivializing the section cocycle throughout the family:

```math
c_s(\bar U;p)
=
\left(
\delta\varepsilon
\right)_p .
\tag{15.187}
```

Therefore the product over the portion of S inside D collapses by lattice
Stokes to the boundary of that portion:

```math
\prod_{p\in S\cap D}
c_s(\bar U;p)^{-1}
=
\prod_{\ell\in\partial(S\cap D)}
\varepsilon_\ell^{-1}.
\tag{15.188}
```

If D is disjoint from C, no section-lifted loop factor lives in the interior of
D. The entire local observable is therefore supported on the interface boundary
of D, which is (15.186). `∎`

This proposition is the way around a fake mass-gap demand. Continuous soft
SO(3) modes may have long-range response, but the discrete cocycle cannot see
them while the configuration stays in one coherent lift chart. The dangerous
soft events are therefore not all small-excess configurations. They are
small-excess configurations that escape chart confinement.

Target 40.31 should therefore be replaced by the following fully audited target.

**Target 40.36 (Renormalized Chart-Confined Response Locality).** Prove, or
disprove, a uniform Kotecky-Preiss estimate for the union of three bad
response sectors:

```math
\mathcal P_{\mathrm{bad}}
=
\mathcal P_{\mathrm{ex}}
\cup
\mathcal P_{\mathrm{hol}}
\cup
\mathcal P_{\mathrm{esc}} .
\tag{15.189}
```

Here the sectors are:

```math
\begin{array}{lll}
\mathcal P_{\mathrm{ex}}
&:&
\text{Dirichlet excess above threshold,}\\[1mm]
\mathcal P_{\mathrm{hol}}
&:&
\text{large collar holonomy, controlled by renormalized collar free energy,}\\[1mm]
\mathcal P_{\mathrm{esc}}
&:&
\text{failure of reconstructible coherent chart confinement.}
\end{array}
\tag{15.190}
```

The required estimate is

```math
\sup_{Q_0}
\sum_{\Pi\ni Q_0}
|w_{\mathrm{bad}}(\Pi)|e^{\kappa|\Pi|}
\le
\eta
<
1
\tag{15.191}
```

uniformly along the continuum trajectory at the chosen physical block scale.

On the complement of these bad sectors, the cocycle response is boundary exact:

```math
\alpha^s_{C,S}(b)
=
\Gamma^s_C(b)
+
R^s_{C,S}(b),
\qquad
R^s_{C,S}
\text{ supported by summable bad polymers.}
\tag{15.192}
```

**Criterion 40.37 (What The Full Audit Leaves).** Target 40.36 implies the
conditional decorrelation conclusion of Criterion 40.6. Conversely, the present
paper supplies no proof of Target 40.36, because the large-holonomy sector
requires a renormalized collar-law estimate and not a bare action estimate.

#### Proof

The bad-sector estimate (15.191) gives an absolutely convergent polymer
expansion for every place where the exact cocycle cannot be collapsed to a
boundary term. Outside those polymers, Proposition 40.35 gives exact boundary
localization. The summable bad polymers can reach the interior of the spanning
surface only with exponentially summable tails, yielding (15.192). Criterion
40.6 then gives Wilson sheet domination if the center-sheet disorder estimate is
also present.

The converse statement follows from Theorem 40.34. The heat-kernel action alone
does not assign a cutoff-uniform positive cost to fixed physical collar
holonomy. Hence the missing input is a true marginal or blocked free-energy
estimate for the SO(3) response. `∎`

The final status of Target 40.31 is therefore:

```math
\boxed{
\begin{array}{c}
\text{Target 40.31 is not proved.}\\[1mm]
\text{Its excess line is conditionally Peierls after a free-energy bound.}\\[1mm]
\text{Its large-holonomy action-Peierls reading is false in four dimensions.}\\[1mm]
\text{Its soft line should be replaced by chart-confined exact localization.}\\[1mm]
\text{The remaining open theorem is Target 40.36.}
\end{array}}
\tag{15.193}
```

### 15.23. Full Investigation Of Target 40.36

Searchable Target-40.36 audit tag:

`V4P40-TARGET-4036-FULL-AUDIT`.

Target 40.36 is the correct structural target left by the previous audit, but
it is still not a theorem. It asks for a renormalized subcriticality statement
about the exact SO(3) Dirichlet response. That statement is stronger than any
local action repair and weaker than simply assuming the Wilson area law. Its
status is:

```math
\boxed{
\begin{array}{c}
\text{Target 40.36 is sufficient for the cocycle route.}\\[1mm]
\text{It is implied by a uniform bad-block domination estimate.}\\[1mm]
\text{It is falsified by macroscopic bad-block crossings.}\\[1mm]
\text{It cannot be proved from bare heat-kernel action gaps.}
\end{array}}
\tag{15.194}
```

Fix the physical block atlas used to define the response decomposition in
(15.189). Let

```math
\eta^{\mathrm{bad}}_Q(\bar U;b)
\tag{15.195}
```

be the indicator that block Q belongs to at least one of the three bad response
sectors in (15.190). Let the connected components of this bad set be denoted by

```math
\Pi\in\pi_0
\left(
\left\{
Q:\eta^{\mathrm{bad}}_Q=1
\right\}
\right).
\tag{15.196}
```

The useful sufficient condition is not another repair map. It is a finite-energy
domination estimate for this exact bad-block field.

**Criterion 40.38 (Uniform Bad-Block Domination Implies Target 40.36).** Suppose
the bad-polymer activities are absolutely dominated by the corresponding
conditional bad-event probabilities, and suppose there is a constant tau such
that, uniformly in the cutoff, the center field in the support of the center
marginal, the admissible exterior SO(3) data, and all connected block polymers
Pi,

```math
\nu^s_{a,b}
\left(
\eta^{\mathrm{bad}}_Q=1
\text{ for every }Q\in\Pi
\mid
\omega_{\Pi^c}
\right)
\le
e^{-\tau|\Pi|}.
\tag{15.197}
```

If

```math
\tau>\log C_{\mathrm{blk}}+\kappa ,
\tag{15.198}
```

then the Kotecky-Preiss estimate (15.191) holds.

#### Proof

The number of connected block polymers of size n through a fixed reference
block is bounded by

```math
N_n\le C_{\mathrm{blk}}^n .
\tag{15.199}
```

Using the assumed activity domination and (15.197) gives

```math
\sup_{Q_0}
\sum_{\Pi\ni Q_0}
|w_{\mathrm{bad}}(\Pi)|e^{\kappa|\Pi|}
\le
\sum_{n\ge1}
\left(
C_{\mathrm{blk}}e^{\kappa-\tau}
\right)^n .
\tag{15.200}
```

The right hand side is smaller than one after increasing tau by a fixed margin
above (15.198). This gives (15.191), hence Target 40.36. `∎`

This criterion is the cleanest possible PASS line for the present route. It
also shows exactly what remains unproved: one must dominate the actual
renormalized bad-block field, not just show that bad configurations can be
repaired when they carry excess action.

There is also a clean FAIL diagnostic.

**Criterion 40.39 (Macroscopic Bad Crossings Falsify Target 40.36).** If Target
40.36 holds, then there are constants K and m such that for every reference
block Q and every block distance L,

```math
\nu^s_{a,b}
\left[
\begin{array}{c}
\text{there exists a bad component beginning at }Q\\
\text{and reaching block distance at least }L
\end{array}
\right]
\le
K e^{-mL}.
\tag{15.201}
```

Consequently any continuum sequence for which the left hand side stays bounded
below along macroscopic spanning-surface distances falsifies Target 40.36.

#### Proof

If a bad component beginning at Q reaches distance L, then it contains a
connected block polymer of size at least a constant multiple of L. Summing the
Kotecky-Preiss majorant (15.191) over such polymers gives an exponentially
decaying tail. `∎`

Thus Target 40.36 has a precise empirical and mathematical failure mode:

```math
\boxed{
\text{bad response sectors percolate, or have nondecaying macroscopic
crossing probability.}
}
\tag{15.202}
```

The remaining question is whether (15.197) can be proved from the action. The
answer is no.

**Theorem 40.40 (No Bare-Action Proof Of Bad-Block Domination).** For every
fixed physical block scale R and every connected finite block polymer Pi, there
are trivial-center SO(3) lattice configurations for which every block in Pi is
bad through the large-holonomy or chart-escape sector, while the heat-kernel
action excess satisfies

```math
\Delta\mathcal A_a(\Pi)
\le
|\Pi|\,
\frac{C\rho_H^2}{N_R(a)\,t(a)}
+
|\Pi|\,
o
\left(
\frac{1}{N_R(a)\,t(a)}
\right),
\tag{15.203}
```

where

```math
N_R(a)\asymp R^2a^{-2}.
\tag{15.204}
```

Along an asymptotically-free heat-kernel trajectory,

```math
N_R(a)t(a)\longrightarrow\infty .
\tag{15.205}
```

Therefore the action excess per bad block tends to zero. In particular, no
deterministic lower bound of the form

```math
\Delta\mathcal A_a(\Pi)
\ge
\tau|\Pi|
\tag{15.206}
```

with positive cutoff-independent tau can imply (15.197).

#### Proof

Inside each block of Pi choose a small physical loop and a spanning lattice disk
with order N_R(a) tangential plaquettes. As in Theorem 40.34, choose an abelian
SO(3) subgroup and spread a fixed holonomy above threshold over those
plaquettes, using plaquette holonomy

```math
\exp
\left(
\frac{X}{N_R(a)}
\right).
\tag{15.207}
```

The supports can be chosen inside the interiors of the nonoverlapping physical
blocks, with a fixed-thickness lattice slab around each disk. Each block then
fails chart confinement or has large collar holonomy, while every plaquette
remains inside the principal chart for small enough lattice spacing. Thus the
center field can be chosen trivial.

The heat-kernel action cost of one such block is bounded by the estimate already
proved in (15.177), with N_a replaced by N_R(a). Summing over the blocks of Pi
gives (15.203). Equation (15.205) then makes the right hand side vanish per
block. This contradicts any positive cutoff-uniform lower bound of the form
(15.206). `∎`

Theorem 40.40 is stronger than the earlier large-holonomy audit. It says that
even the corrected target cannot be reached through a bare Peierls action
argument. If Target 40.36 is true, it is true because the renormalized SO(3)
collar law suppresses coherent bad response sectors after all entropic and
gauge-volume effects are included.

This leaves the exact next theorem.

**Target 40.41 (Renormalized Bad-Block Domination Or Percolation).** Fix a
physical block scale R and thresholds for excess, holonomy, and chart escape.
For the exact constrained SO(3) fiber law, prove one of the following two
alternatives.

PASS:

```math
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\omega_{\Pi^c}}
\nu^s_{a,b}
\left(
\eta^{\mathrm{bad}}_Q=1
\text{ for every }Q\in\Pi
\mid
\omega_{\Pi^c}
\right)
\le
e^{-\tau|\Pi|}
\tag{15.208}
```

with tau above the entropy threshold in (15.198).

FAIL:

```math
\limsup_{a\downarrow0}
\nu^s_{a,b_a}
\left[
\begin{array}{c}
\text{there is a bad component crossing a fixed}\\
\text{positive fraction of the spanning surface}
\end{array}
\right]
>
0
\tag{15.209}
```

for some admissible continuum sequence of center fields and loop/surface data.

The PASS line proves Target 40.36 by Criterion 40.38. The FAIL line disproves it
by Criterion 40.39.

There is one final scale warning. Target 40.41 should not be demanded at an
arbitrary large physical block scale. At large physical scale, non-Abelian
holonomies are not expected to remain inside a single lift chart with high
probability. The viable version is a multiscale one:

```math
\boxed{
\begin{array}{c}
\text{choose a sufficiently small but fixed physical block scale R,}\\[1mm]
\text{prove bad-block subcriticality at that scale,}\\[1mm]
\text{then use the polymer expansion to cross macroscopic IR surfaces.}
\end{array}}
\tag{15.210}
```

This is the fully investigated status of Target 40.36:

```math
\boxed{
\begin{array}{c}
\text{Target 40.36 is not proved or falsified by finite-cutoff algebra.}\\[1mm]
\text{It is reduced to Target 40.41, a renormalized bad-block domination
theorem.}\\[1mm]
\text{Bare action cannot prove it, because bad holonomy can be spread over
surfaces with vanishing action cost.}\\[1mm]
\text{A proof would be genuine new SO(3) fiber mixing; a disproof would be
bad-sector percolation.}
\end{array}}
\tag{15.211}
```

### 15.24. Target 40.42: The Fixed-Physical Block-Collar Spectral Alternative

Searchable Target-40.42 tag:

`V4P40-TARGET-4042-BLOCK-COLLAR-SPECTRAL-ALTERNATIVE`.

The next attack on Target 40.41 should not be another microscopic action
estimate. The right object is the exact physical-block response kernel. This is
the Einstein/Feynman move in operational form:

```math
\boxed{
\begin{array}{c}
\text{choose the invariant physical-block boundary question,}\\[1mm]
\text{write its exact finite-cutoff kernel,}\\[1mm]
\text{then test whether cocycle-sensitive bad modes contract under blocking.}
\end{array}}
\tag{15.212}
```

Fix a small physical block scale R, independent of the lattice spacing. Let

```math
B_R(a)
\tag{15.213}
```

be the corresponding lattice block, and let

```math
A_-(a),\qquad A_+(a)
\tag{15.214}
```

be two collar portions through which the block response is read. Boundary gauge
redundancy is removed either by quotienting the collar data by boundary gauge
transformations or by fixing a boundary tree gauge. Write the resulting collar
variables as

```math
\xi_-,\qquad \xi_+ .
\tag{15.215}
```

For a bounded observable F of the interior and outgoing collar, define the
unnormalized block response

```math
Z^s_{R,a}(F\mid b,\xi_-,\xi_+)
:=
\int_{\mathcal F^s_{R,a}(b,\xi_-,\xi_+)}
F(\bar V,\xi_+)
\prod_{p\subset B_R(a)}
K_{t(a)}
\left(
b_p\,s(\bar V_p)
\right)
\prod_{\ell\subset B_R(a)^\circ}d\bar V_\ell .
\tag{15.216}
```

The exact block-collar Markov kernel is

```math
\mathsf K^s_{R,a,b}(d\xi_+\mid\xi_-)
:=
\frac{
Z^s_{R,a}(1\mid b,\xi_-,\xi_+)\,d\lambda_{A_+}(\xi_+)
}{
\int
Z^s_{R,a}(1\mid b,\xi_-,\eta)\,d\lambda_{A_+}(\eta)
}.
\tag{15.217}
```

This kernel is the object whose cutoff-uniform behavior matters. A lattice-scale
estimate for individual plaquettes is not enough. The fixed-physical IR version
of the problem asks whether the family (15.217), with R fixed and the cutoff
removed, suppresses the bad sectors from Target 40.41.

Let the one-block conditional bad probability be

```math
\beta^s_{R,a,b}(\xi_-,\xi_+)
:=
\mathbb E
\left[
\eta^{\mathrm{bad}}_Q
\mid
\xi_-,\xi_+
\right] .
\tag{15.218}
```

Define the bad-transfer operator

```math
\mathsf B^s_{R,a,b}f(\xi_-)
:=
\int
\beta^s_{R,a,b}(\xi_-,\xi_+)
f(\xi_+)
\mathsf K^s_{R,a,b}(d\xi_+\mid\xi_-).
\tag{15.219}
```

This operator is the precise replacement for the failed bare Peierls action
bound. It remembers both ingredients that matter:

```math
\boxed{
\begin{array}{c}
\text{the density of bad blocks,}\\[1mm]
\text{and the propagation of bad boundary correlations.}
\end{array}}
\tag{15.220}
```

Peter-Weyl language enters after this point. Decompose the collar function space
into SO(3) boundary representation modes. The constant mode records the
one-block bad density. The nontrivial modes record propagation of collar
correlations. A useful spectral theorem must control both. Controlling only the
nontrivial Peter-Weyl modes is not enough.

**Target 40.42 (Fixed-Physical Bad-Transfer Spectral Alternative).** At a
sufficiently small but fixed physical block scale R, prove one of the following.

PASS:

```math
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\text{admissible block orderings}}
\left\|
\mathsf B_{Q_n}
\mathsf B_{Q_{n-1}}
\cdots
\mathsf B_{Q_1}
\mathbf 1
\right\|_\infty
\le
e^{-\tau n}
\tag{15.221}
```

with tau above the block-animal entropy threshold.

FAIL:

```math
\limsup_{a\downarrow0}
\nu^s_{a,b_a}
\left[
\begin{array}{c}
\text{a cocycle-sensitive bad component crosses a fixed}\\
\text{positive fraction of the spanning surface}
\end{array}
\right]
>
0
\tag{15.222}
```

for some admissible continuum sequence.

Here an admissible block ordering is any ordering obtained by growing a
connected polymer one neighboring block at a time. The operators in (15.221)
are the corresponding exact bad-transfer operators, with the appropriate
conditioned exterior data at each step.

**Criterion 40.43 (Bad-Transfer Contraction Implies Target 40.41).** The PASS
line of Target 40.42 implies the PASS line of Target 40.41. The FAIL line of
Target 40.42 implies the FAIL line of Target 40.41.

#### Proof

Grow a connected candidate bad polymer by an admissible ordering. At the kth
step, condition on all exterior data already exposed. The probability that the
new block is bad is represented by the kth bad-transfer operator. Iterating the
tower property gives the left hand side of (15.221) as an upper bound for the
probability that all n blocks in the ordered polymer are bad. If (15.221) holds,
then (15.208) follows with the same exponential rate, after absorbing the
exponential number of admissible growth orderings into the block-animal entropy
constant. Criterion 40.38 then gives Target 40.36.

The FAIL implication is immediate: a bad component crossing a fixed positive
fraction of the spanning surface is a macroscopic bad crossing of the type
appearing in (15.209). `∎`

The spectral version is useful only if it includes the constant mode. The next
simple theorem records this no-shortcut rule.

**Theorem 40.44 (Nontrivial Peter-Weyl Contraction Alone Is Insufficient).**
A uniform contraction estimate on nonconstant SO(3) collar modes does not imply
Target 40.41 unless it is accompanied by a one-block bad-density bound.

#### Proof

Consider the comparison case in which consecutive block collars are independent.
Then every nonconstant boundary mode contracts in one step:

```math
\Pi_{\mathrm{nonconst}}
\mathsf K
=
0 .
\tag{15.223}
```

Let the bad-block indicator be independent from block to block with probability
p. Then the bad-transfer operator satisfies

```math
\mathsf B\mathbf 1
=
p .
\tag{15.224}
```

If p is above the relevant lattice-animal or percolation threshold, macroscopic
bad clusters occur despite perfect contraction of nonconstant collar modes.
Thus nontrivial-mode contraction alone misses the constant Peter-Weyl component,
which is exactly the bad-block density. `∎`

Therefore the viable spectral package has two parts:

```math
\boxed{
\begin{array}{ll}
\text{density:}
&
\left\|\mathsf B\mathbf 1\right\|_\infty
\le p
\text{ below the polymer threshold,}\\[1mm]
\text{mixing:}
&
\mathsf B
\text{ contracts centered cocycle-sensitive boundary modes.}
\end{array}}
\tag{15.225}
```

This is fixed-IR valid only with R held fixed in physical units and constants
independent of the cutoff:

```math
\boxed{
\begin{array}{c}
R>0\text{ fixed},\\[1mm]
a\downarrow0,\\[1mm]
\tau,p,\kappa
\text{ independent of }a
\text{ and of the physical volume.}
\end{array}}
\tag{15.226}
```

If (15.225) is proved only at the lattice scale, or only before the physical
block limit, it is a UV statement and does not prove Target 40.41. If it is
proved for the exact block kernel (15.217) at fixed physical R with constants
as in (15.226), then it is a legitimate fixed-physical IR theorem.

The final sharpened target is:

**Target 40.45 (Cocycle-Sensitive Block Spectral Package).** Prove, or disprove,
the following two estimates for the exact kernel (15.217) at some sufficiently
small fixed physical block scale:

```math
\sup_{\xi_-}
\int
\beta^s_{R,a,b}(\xi_-,\xi_+)
\mathsf K^s_{R,a,b}(d\xi_+\mid\xi_-)
\le
p
\tag{15.227}
```

with p below the block-polymer threshold, and

```math
\left\|
\mathsf B^s_{R,a,b}f
-
\Pi_0
\mathsf B^s_{R,a,b}f
\right\|
\le
\theta p\,
\left\|
f-\Pi_0 f
\right\|
\tag{15.228}
```

with

```math
0\le\theta<1
\tag{15.229}
```

uniformly in the cutoff, admissible center field, and admissible exterior data.
Here

```math
\Pi_0
\tag{15.230}
```

denotes projection onto the constant boundary mode in the chosen collar Hilbert
space.

**Criterion 40.46 (The Spectral Package Is Fixed-IR Sufficient).** If (15.227)
holds with

```math
p\,e^{\log C_{\mathrm{blk}}+\kappa}<1,
\tag{15.231}
```

then the PASS line of Target 40.42 holds. The centered estimate (15.228) is not
needed for this strongest uniform-density version, but it is the diagnostic
estimate needed for weaker averaged-density variants and for identifying
whether bad boundary correlations propagate.

#### Proof

The bad-transfer operator is positive and satisfies, for every bounded
nonnegative f,

```math
\left\|
\mathsf B^s_{R,a,b}f
\right\|_\infty
\le
p\left\|f\right\|_\infty .
\tag{15.232}
```

Iterating (15.232) gives

```math
\left\|
\mathsf B_{Q_n}
\cdots
\mathsf B_{Q_1}
\mathbf 1
\right\|_\infty
\le
p^n .
\tag{15.233}
```

Condition (15.231) puts this decay above the polymer entropy threshold, so
Target 40.42 PASS follows. `∎`

This is the version I would actually try to prove next. It is narrower than a
full Yang-Mills mass-gap theorem because it only controls cocycle-sensitive bad
response sectors. But it is still a genuine fixed-physical SO(3) fiber-mixing
statement. If it fails, the center-resolved route has reached the shared
four-dimensional floor in its cleanest form.

### 15.25. Working Target 40.45: The Six-Step Fixed-IR Attack

Searchable Target-40.45 work tag:

`V4P40-TARGET-4045-SIX-STEP-FIXED-IR-ATTACK`.

Target 40.45 has to be attacked in physical units. The block scale is fixed
first; the cutoff is removed second:

```math
0<R<R_0,
\qquad
a\downarrow0,
\qquad
\frac{R}{a}\longrightarrow\infty .
\tag{15.234}
```

The parameter R should be small enough for asymptotic freedom to make local
curvature tightness plausible, but it is still a fixed physical scale. Nothing
below is a lattice-scale UV estimate.

#### Step 1: Fix The Physical Block And Threshold Package

Choose thresholds

```math
0<\rho_{\mathrm{chart}}'<\rho_{\mathrm{chart}},
\qquad
0<\rho_H<\rho_{\mathrm{chart}}',
\qquad
\varepsilon_R>0 .
\tag{15.235}
```

The margin between rho_H and rho_chart is deliberate. It leaves room for
collar perturbations, gluing, and section changes without leaving the coherent
lift chart.

For a block Q at physical scale R, define the gauge-invariant reconstruction
size exactly as in Section 15.14:

```math
M_Q(\bar U)
=
\max_{\ell\notin T_Q}
d_{SO(3)}
\left(
\operatorname{Hol}_{\gamma_{Q,\ell}}(\bar U),
1
\right).
\tag{15.236}
```

#### Step 2: Define Chart Escape In Gauge-Invariant Form

For a block family Y, write

```math
\mathcal G_{\rho}(Y)
\tag{15.237}
```

for the event that every block in Y has reconstruction size at most rho and the
local section trivializations glue coherently on overlaps. The chart-escape
event is

```math
\mathcal E_{\mathrm{esc}}(Y)
:=
\mathcal G_{\rho_{\mathrm{chart}}'}(Y)^c .
\tag{15.238}
```

This is the cocycle-sensitive escape event. It is stronger than saying that a
single plaquette is large, and weaker than requiring all continuous SO(3)
fluctuations to be small. It asks exactly whether the section cocycle can be
collapsed to a boundary term on Y.

There is one correction to Target 40.45. The supremum over incoming collar data
in (15.227) cannot include hostile collars that are already bad. If an incoming
collar already violates chart confinement or already carries large holonomy,
then the next block can be forced to be bad with probability one. Such a collar
belongs to the existing bad component and should be absorbed into the polymer.

Define the frontier-good collar set by

```math
\mathcal A_{\mathrm{good}}
:=
\left\{
\xi_-:
\mathfrak h_{A_-}(\xi_-)<\rho_H
\text{ and }
\mathcal G_{\rho_{\mathrm{chart}}'}(A_-)
\text{ holds}
\right\}.
\tag{15.239}
```

The density estimate must be taken over this set:

```math
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\int
\beta^s_{R,a,b}(\xi_-,\xi_+)
\mathsf K^s_{R,a,b}(d\xi_+\mid\xi_-)
\le
p .
\tag{15.240}
```

**Theorem 40.47 (Unrestricted Collar Supremum Is The Wrong Growth Estimate).**
The estimate (15.227) is not the usable polymer-growth estimate if the supremum
includes arbitrary incoming collar data.

#### Proof

Choose incoming collar data whose collar holonomy already satisfies

```math
\mathfrak h_{A_-}(\xi_-)\ge\rho_H .
\tag{15.241}
```

By the definition of the large-holonomy bad sector, this incoming collar is
already part of a bad component. In a block-growth exploration, the neighboring
block is not a fresh trial across a good frontier; it is adjacent to bad data
that must be absorbed into the current polymer before a new conditional estimate
is applied. If one nevertheless counts this as a fresh step, the conditional
bad probability for the enlarged response block can be one. Thus no
below-threshold estimate over arbitrary incoming collars is the right polymer
input. `∎`

Thus the correct growth algorithm is:

```math
\boxed{
\begin{array}{c}
\text{bad incoming collars are absorbed into the existing polymer;}\\[1mm]
\text{fresh probabilistic estimates are applied only across frontier-good
collars.}
\end{array}}
\tag{15.242}
```

#### Step 3: The Small-Block Chart-Tightness Estimate

The first genuinely analytic estimate is the frontier-good chart-escape bound:

```math
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\mathsf K^s_{R,a,b}
\left[
\mathcal E_{\mathrm{esc}}(Q\cup A_+)
\mid
\xi_-
\right]
\le
p_{\mathrm{esc}}(R).
\tag{15.243}
```

This is the fixed-physical form of the asymptotic-freedom hope. It is not
proved by the current paper. What can be proved now is the implication if it
holds with the other bad-sector estimates.

The reason (15.243) is plausible is that R may be chosen small in physical
units while the number of lattice cells in Q diverges. The reason it is hard is
that the estimate is uniform over the center-conditioned fiber and over all
frontier-good collar data.

#### Step 4: Treat Large Holonomy As A Boundary Response Event

Large holonomy must be measured under the block kernel, not priced by a bare
action gap. Define

```math
\mathcal E_{\mathrm{hol}}(Q,A_+)
:=
\left\{
\mathfrak h_{A_+}(\xi_+)\ge\rho_H
\right\}.
\tag{15.244}
```

The required estimate is the frontier-good boundary response bound:

```math
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\mathsf K^s_{R,a,b}
\left[
\mathcal E_{\mathrm{hol}}(Q,A_+)
\mid
\xi_-
\right]
\le
p_{\mathrm{hol}}(R).
\tag{15.245}
```

This is exactly where Theorem 40.34 and Theorem 40.40 force the change of
method. A proof of (15.245) must use the renormalized collar law, not a
microscopic action gap.

#### Step 5: Split Only The Cocycle-Sensitive Peter-Weyl Modes

Let

```math
\mathcal H_{\mathrm{coc}}(A)
\tag{15.246}
```

be the closed subspace of collar functions generated by finite products of:

```math
\begin{array}{c}
\text{chart-escape indicators,}\\[1mm]
\text{large-holonomy indicators,}\\[1mm]
\text{Dirichlet-excess indicators,}\\[1mm]
\text{boundary cocycle signs produced by coherent-chart trivialization.}
\end{array}
\tag{15.247}
```

Decompose this subspace into its constant and centered pieces:

```math
\mathcal H_{\mathrm{coc}}
=
\Pi_0\mathcal H_{\mathrm{coc}}
\oplus
\mathcal H_{\mathrm{coc}}^0 .
\tag{15.248}
```

The Peter-Weyl contraction target should be imposed only on

```math
\mathcal H_{\mathrm{coc}}^0 ,
\tag{15.249}
```

not on the entire SO(3) collar Hilbert space. This is the narrow version that
does not immediately demand a full Yang-Mills mass gap.

The corresponding centered estimate is:

```math
\left\|
\Pi_{\mathrm{coc}}^0
\mathsf B^s_{R,a,b}
\Pi_{\mathrm{coc}}^0 f
\right\|
\le
\theta\,p_{\mathrm{tot}}(R)
\left\|
\Pi_{\mathrm{coc}}^0 f
\right\|,
\qquad
0\le\theta<1 .
\tag{15.250}
```

Here

```math
p_{\mathrm{tot}}(R)
:=
p_{\mathrm{esc}}(R)+p_{\mathrm{hol}}(R)+p_{\mathrm{ex}}(R).
\tag{15.251}
```

#### Step 6: Prove The Density Bound First

The excess sector is handled by the exact Dirichlet-excess response:

```math
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\mathsf K^s_{R,a,b}
\left[
\mathcal E^s_{D,A}(\bar U\mid b,\xi)
\ge
\varepsilon_R
\mid
\xi_-
\right]
\le
p_{\mathrm{ex}}(R).
\tag{15.252}
```

By the union bound,

```math
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\int
\beta^s_{R,a,b}(\xi_-,\xi_+)
\mathsf K^s_{R,a,b}(d\xi_+\mid\xi_-)
\le
p_{\mathrm{tot}}(R).
\tag{15.253}
```

Therefore the density-first theorem is:

**Criterion 40.48 (Density-First Fixed-IR Route To Target 40.45).** Suppose
(15.243), (15.245), and (15.252) hold at a fixed physical block scale R, with

```math
p_{\mathrm{tot}}(R)\,
e^{\log C_{\mathrm{blk}}+\kappa}
<
1 .
\tag{15.254}
```

Then the corrected frontier-good version of Target 40.45 holds. If the
centered estimate (15.250) also holds, then the full cocycle-sensitive spectral
package holds.

#### Proof

The bad event is contained in the union of chart escape, large outgoing collar
holonomy, and Dirichlet excess. Thus (15.253) follows from (15.243), (15.245),
and (15.252). Condition (15.254) is the polymer entropy threshold from Criterion
40.46, with p replaced by p_tot. This proves the density part of Target 40.45
for frontier-good growth. Estimate (15.250) is exactly the centered
cocycle-sensitive contraction part. `∎`

This completes the six-step attack in a form valid for fixed physical IR
regimes. It also exposes the next honest obstruction:

```math
\boxed{
\begin{array}{c}
\text{prove the three frontier-good one-block estimates}\\[1mm]
\text{(chart escape, large holonomy, excess),}\\[1mm]
\text{or exhibit frontier-good data for which one of them stays large.}
\end{array}}
\tag{15.255}
```

The most likely failure mode is not the centered Peter-Weyl estimate. It is
uniformity over the center-conditioned frontier-good collar law. If adversarial
but still frontier-good collars can force chart escape or large outgoing
holonomy with probability near one, Target 40.45 fails in the form needed for
the center route. If those collars are suppressed by the renormalized block law,
the route remains alive.

### 15.26. Proof Work On The Three One-Block Estimates

Searchable one-block proof tag:

`V4P40-ONE-BLOCK-ESTIMATE-PROOF-WORK`.

The three estimates in Section 15.25 are now explicit enough to attack. The
current paper can prove reduction theorems for all three. What it still cannot
prove from finite-cutoff algebra alone is the analytic input behind those
reductions.

The three proof targets are:

```math
\boxed{
\begin{array}{lll}
\text{chart escape}
&:&
\text{reduce to fundamental-loop holonomy and Cech-tail bounds,}\\[1mm]
\text{large outgoing holonomy}
&:&
\text{reduce to an adjoint-character collar moment,}\\[1mm]
\text{Dirichlet excess}
&:&
\text{reduce to a normalized Laplace lower bound.}
\end{array}}
\tag{15.256}
```

#### 15.26.1. Chart Escape

For a block family Y, split chart escape into local reconstruction failure and
flat gluing failure:

```math
\mathcal E_{\mathrm{esc}}(Y)
\subset
\mathcal E_{\mathrm{loc}}(Y)
\cup
\mathcal E_{\mathrm{Cech}}(Y),
\tag{15.257}
```

where

```math
\mathcal E_{\mathrm{loc}}(Y)
:=
\left\{
\exists Q\subset Y:
M_Q(\bar U)>\rho_{\mathrm{chart}}'
\right\},
\tag{15.258}
```

and

```math
\mathcal E_{\mathrm{Cech}}(Y)
:=
\left\{
\begin{array}{c}
M_Q(\bar U)\le\rho_{\mathrm{chart}}'
\text{ for every }Q\subset Y,\\
\text{but the local section trivializations do not glue coherently}
\end{array}
\right\}.
\tag{15.259}
```

Let

```math
\mathcal L_Y
\tag{15.260}
```

be the finite family of fundamental loops used in the reconstruction tests for
blocks in Y. Define the frontier-good loop-tail quantity

```math
q_{\mathrm{loop}}(R,\rho)
:=
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\sup_{\gamma\in\mathcal L_Y}
\mathsf K^s_{R,a,b}
\left[
d_{SO(3)}
\left(
\operatorname{Hol}_{\gamma},
1
\right)
>
\rho
\mid
\xi_-
\right].
\tag{15.261}
```

Also define the coherent-gluing tail

```math
q_{\mathrm{Cech}}(R,\rho)
:=
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\mathsf K^s_{R,a,b}
\left[
\mathcal E_{\mathrm{Cech}}(Y)
\mid
\xi_-
\right].
\tag{15.262}
```

**Criterion 40.49 (Loop-Tail And Cech-Tail Bounds Prove Chart Tightness).** If

```math
|\mathcal L_Y|\,q_{\mathrm{loop}}(R,\rho_{\mathrm{chart}}')
+
q_{\mathrm{Cech}}(R,\rho_{\mathrm{chart}}')
\le
p_{\mathrm{esc}}(R),
\tag{15.263}
```

then the chart-escape estimate (15.243) holds.

#### Proof

If chart escape occurs, then either some block fails the local reconstruction
test or all local tests pass but the resulting local trivializations fail to
glue. This is (15.257). The local failure event is contained in the union, over
loops in the finite reconstruction family, of the event that the corresponding
loop holonomy leaves the reconstruction ball. A union bound gives

```math
\mathsf K^s_{R,a,b}
\left[
\mathcal E_{\mathrm{loc}}(Y)
\mid
\xi_-
\right]
\le
|\mathcal L_Y|\,q_{\mathrm{loop}}(R,\rho_{\mathrm{chart}}') .
\tag{15.264}
```

Adding the Cech-tail term gives (15.263), uniformly in the cutoff, center field,
and frontier-good incoming collar. `∎`

This is the first proof reduction. It also shows why the estimate is genuinely
fixed-physical: the product in (15.263) must remain small after the cutoff is
removed at fixed R. Since the reconstruction loop family grows as the lattice is
refined, the single-loop tail must beat the loop entropy or else the
reconstruction test is too microscopic.

Thus the chart-escape proof forks:

```math
\boxed{
\begin{array}{c}
\text{either prove a cutoff-uniform loop-tail bound strong enough for
(15.263),}\\[1mm]
\text{or coarsen the reconstruction test to a genuinely physical finite loop
family.}
\end{array}}
\tag{15.265}
```

#### 15.26.2. Large Outgoing Collar Holonomy

The large-holonomy estimate can be reduced to an adjoint-character moment. Let
chi_ad be the SO(3) adjoint character. For every threshold below the chart
radius there is a positive constant c_H such that

```math
d_{SO(3)}(g,1)\ge\rho_H
\quad\Longrightarrow\quad
1-\frac{1}{3}\chi_{\mathrm{ad}}(g)
\ge
c_H(\rho_H).
\tag{15.266}
```

Therefore

```math
\mathbf 1
\left[
d_{SO(3)}(g,1)\ge\rho_H
\right]
\le
\frac{1}{c_H(\rho_H)}
\left(
1-\frac{1}{3}\chi_{\mathrm{ad}}(g)
\right).
\tag{15.267}
```

Let

```math
\mathcal B_{A_+}
\tag{15.268}
```

be the finite basis of outgoing collar loops used in the holonomy-size
definition. Define

```math
\Delta_{\mathrm{ad}}(R,\rho_H)
:=
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\sup_{\gamma\in\mathcal B_{A_+}}
\left[
1
-
\frac{1}{3}
\mathsf K^s_{R,a,b}
\left(
\chi_{\mathrm{ad}}
\left(
\operatorname{Hol}_{\gamma}(\xi_+)
\right)
\mid
\xi_-
\right)
\right].
\tag{15.269}
```

**Criterion 40.50 (Adjoint Moment Proves Large-Holonomy Bound).** If

```math
\frac{|\mathcal B_{A_+}|}{c_H(\rho_H)}
\Delta_{\mathrm{ad}}(R,\rho_H)
\le
p_{\mathrm{hol}}(R),
\tag{15.270}
```

then the large outgoing collar holonomy estimate (15.245) holds.

#### Proof

The event in (15.244) is the union over the outgoing collar basis loops of the
event that the corresponding holonomy is at distance at least rho_H from the
identity. Applying (15.267) to each loop and taking the expectation under the
block kernel gives

```math
\mathsf K^s_{R,a,b}
\left[
\mathcal E_{\mathrm{hol}}(Q,A_+)
\mid
\xi_-
\right]
\le
\frac{|\mathcal B_{A_+}|}{c_H(\rho_H)}
\Delta_{\mathrm{ad}}(R,\rho_H).
\tag{15.271}
```

The assumed bound (15.270) gives (15.245). `∎`

This is the Feynman-computable form of the large-holonomy problem. One does not
try to charge holonomy by bare action. One computes, or bounds, the adjoint
collar character under the exact block kernel.

The corresponding analytic target is:

```math
\boxed{
\Delta_{\mathrm{ad}}(R,\rho_H)
\text{ is small for sufficiently small fixed physical }R,
\text{ uniformly as }a\downarrow0.
}
\tag{15.272}
```

If (15.272) fails for frontier-good incoming collars, then the large-holonomy
part of Target 40.45 fails.

#### 15.26.3. Dirichlet Excess

The Dirichlet-excess estimate is an equilibrium tail estimate around the exact
Dirichlet minimizer, not around the identity. Let

```math
\mathcal E(\bar V)
\tag{15.273}
```

denote the Dirichlet excess in the block response fiber. After subtracting the
minimum action, the normalized excess partition function is

```math
Z_{\mathrm{ex}}(b,\xi_-,\xi_+)
:=
\int_{\mathcal F^s_{R,a}(b,\xi_-,\xi_+)}
e^{-\mathcal E(\bar V)}
d\lambda_{\mathrm{fib}}(\bar V).
\tag{15.274}
```

Here the fiber measure is the induced normalized Haar measure on the admissible
Dirichlet fiber. The exact excess-tail probability satisfies:

**Criterion 40.51 (Laplace Lower Bound Proves Excess Tail).** Suppose there is
a cutoff-uniform fluctuation free-energy bound

```math
Z_{\mathrm{ex}}(b,\xi_-,\xi_+)
\ge
e^{-F_{\mathrm{fluc}}(R)}
\tag{15.275}
```

for all admissible frontier-good data. Then

```math
\mathsf K^s_{R,a,b}
\left[
\mathcal E(\bar V)\ge\varepsilon_R
\mid
\xi_-,\xi_+
\right]
\le
\exp
\left(
F_{\mathrm{fluc}}(R)-\varepsilon_R
\right).
\tag{15.276}
```

Consequently (15.252) holds with

```math
p_{\mathrm{ex}}(R)
=
\exp
\left(
F_{\mathrm{fluc}}(R)-\varepsilon_R
\right).
\tag{15.277}
```

#### Proof

For the numerator of the excess-tail probability,

```math
\int_{\mathcal E\ge\varepsilon_R}
e^{-\mathcal E(\bar V)}
d\lambda_{\mathrm{fib}}(\bar V)
\le
e^{-\varepsilon_R}.
\tag{15.278}
```

Dividing by the denominator and using (15.275) gives (15.276). Taking the
supremum over the outgoing collar data gives (15.252). `∎`

This proves the exact excess-tail reduction. It also displays the real
analytic issue. The constant F_fluc is the finite physical block fluctuation
free energy after the cutoff is removed. If it grows without bound as the
lattice is refined, then a fixed excess threshold cannot prove subcriticality.
If it remains finite and can be beaten by the chosen threshold, then the excess
sector is controlled.

#### 15.26.4. Combined Fixed-IR Criterion

Combining Criteria 40.49, 40.50, and 40.51 gives the sharpest current
proof-ready statement.

**Criterion 40.52 (Three Analytic Inputs Prove The Density Bound).** Suppose
that at a sufficiently small fixed physical block scale R,

```math
|\mathcal L_Y|\,q_{\mathrm{loop}}(R,\rho_{\mathrm{chart}}')
+
q_{\mathrm{Cech}}(R,\rho_{\mathrm{chart}}')
\le
p_{\mathrm{esc}}(R),
\tag{15.279}
```

```math
\frac{|\mathcal B_{A_+}|}{c_H(\rho_H)}
\Delta_{\mathrm{ad}}(R,\rho_H)
\le
p_{\mathrm{hol}}(R),
\tag{15.280}
```

and

```math
\exp
\left(
F_{\mathrm{fluc}}(R)-\varepsilon_R
\right)
\le
p_{\mathrm{ex}}(R).
\tag{15.281}
```

If

```math
\left(
p_{\mathrm{esc}}(R)+p_{\mathrm{hol}}(R)+p_{\mathrm{ex}}(R)
\right)
e^{\log C_{\mathrm{blk}}+\kappa}
<
1 ,
\tag{15.282}
```

then the corrected frontier-good density estimate in Target 40.45 holds at
fixed physical scale.

#### Proof

Criterion 40.49 gives (15.243). Criterion 40.50 gives (15.245). Criterion
40.51 gives (15.252). Criterion 40.48 then gives the corrected density-first
Target 40.45. `∎`

This is as far as the present paper can honestly go without importing a new
constructive four-dimensional block-kernel estimate. The next three actual
proof obligations are:

```math
\boxed{
\begin{array}{ll}
\text{P1:}
&
\text{prove loop-tail and Cech-tail bounds strong enough for (15.279),}\\[1mm]
\text{P2:}
&
\text{prove the adjoint collar moment bound (15.280),}\\[1mm]
\text{P3:}
&
\text{prove the normalized fluctuation free-energy bound (15.281).}
\end{array}}
\tag{15.283}
```

These are fixed-physical IR statements because R is held fixed while the cutoff
is removed. They are not proved by UV plaquette smallness alone. If all three
hold below the polymer threshold, the center-resolved route gets its
cocycle-sensitive bad-block subcriticality theorem. If any one fails for
frontier-good data, the route fails at a precisely identified one-block
response channel.

### 15.27. Attempted Proof Of (15.279)-(15.281): What Actually Survives

Searchable proof-attempt tag:

`V4P40-ATTEMPT-PROVE-15279-15281`.

We now try to prove the three analytic inputs in Criterion 40.52. The result is
not a full proof. One part can be made deterministic under a topology
hypothesis, one part reduces to the expected small-block adjoint Wilson
estimate, and one part is false in its raw microscopic form.

The outcome is:

```math
\boxed{
\begin{array}{lll}
\text{(15.279)}
&:&
\text{provable after Cech triviality, up to a loop-tail estimate,}\\[1mm]
\text{(15.280)}
&:&
\text{equivalent to a fixed-physical adjoint collar moment estimate,}\\[1mm]
\text{(15.281)}
&:&
\text{not useful with a fixed raw microscopic excess threshold.}
\end{array}}
\tag{15.284}
```

#### 15.27.1. The Cech Part Of (15.279)

The gluing part of chart escape has a deterministic resolution when the block
family has no one-dimensional Cech cohomology.

**Theorem 40.53 (Cech Triviality Kills The Gluing Tail).** Suppose the nerve of
the block family Y satisfies

```math
H^1
\left(
\mathcal N(Y),Z_2
\right)
=0 .
\tag{15.285}
```

Then, on the event that every block of Y is reconstructibly good with radius
below the chart radius, the local section trivializations glue coherently.
Consequently

```math
q_{\mathrm{Cech}}(R,\rho_{\mathrm{chart}}')
=
0
\tag{15.286}
```

for such Y.

#### Proof

On each reconstructibly good block, Theorem 40.13 supplies a local center
one-cochain trivializing the section cocycle. On an overlap of two such blocks,
the ratio of the two local trivializations is a flat center one-cochain. These
flat transition cochains form a Cech one-cocycle on the nerve of Y. If
(15.285) holds, that cocycle is a coboundary. Modifying the local
trivializations by the corresponding zero-cochain makes them agree on overlaps.
Thus the local trivializations glue to a single coherent trivialization on Y,
and the Cech escape event is empty. `∎`

Therefore, for Cech-trivial block families, (15.279) reduces to:

```math
|\mathcal L_Y|\,q_{\mathrm{loop}}(R,\rho_{\mathrm{chart}}')
\le
p_{\mathrm{esc}}(R).
\tag{15.287}
```

This is the exact remaining chart estimate. It has two possible proof routes:

```math
\boxed{
\begin{array}{c}
\text{prove an entropy-beating tail for the microscopic reconstruction loops,}\\[1mm]
\text{or replace the reconstruction test by a finite physical loop family.}
\end{array}}
\tag{15.288}
```

If the family of reconstruction loops grows with the cutoff, then the first
line is a real analytic estimate. If one coarsens to a finite physical loop
family, then the price is that reconstructible goodness becomes a physical
coarse event rather than a microscopic tree-gauge event.

Thus (15.279) is not proved outright, but its topological half is proved and
its analytic half is isolated in (15.287).

#### 15.27.2. The Adjoint Moment In (15.280)

The large-holonomy estimate is exactly an adjoint small-loop estimate. The
following criterion is the sharp fixed-physical version.

**Criterion 40.54 (Small-Block Adjoint Moment Proves (15.280)).** Suppose that
for some sufficiently small fixed physical R,

```math
\Delta_{\mathrm{ad}}(R,\rho_H)
\le
C_{\mathrm{ad}}\,g_{\mathrm{eff}}^2(R)
+
o_a(1)
\tag{15.289}
```

uniformly over admissible center fields and frontier-good incoming collars,
where

```math
g_{\mathrm{eff}}^2(R)\longrightarrow0
\qquad
\text{as }R\downarrow0 .
\tag{15.290}
```

If R is chosen so that

```math
\frac{|\mathcal B_{A_+}|}{c_H(\rho_H)}
C_{\mathrm{ad}}\,g_{\mathrm{eff}}^2(R)
<
p_{\mathrm{hol}}(R),
\tag{15.291}
```

then (15.280) holds for all sufficiently small cutoffs.

#### Proof

Substitute (15.289) into the left side of (15.280). The cutoff error tends to
zero uniformly by assumption. Condition (15.291) leaves a positive margin, so
for sufficiently small cutoff the left side is bounded by p_hol. `∎`

This is not a proof of (15.289). It identifies the exact perturbative
fixed-physical block estimate that would prove (15.280). It is narrower than a
mass-gap theorem: it controls only adjoint collar loops of size comparable to
the chosen small physical block scale.

#### 15.27.3. The Raw Dirichlet-Excess Estimate (15.281) Fails As Stated

The raw excess estimate is the place where the previous formulation is too
microscopic. In a fixed physical block, the number of lattice degrees of freedom
goes to infinity. A fixed threshold for total microscopic Dirichlet excess
therefore counts ordinary ultraviolet Gaussian fluctuations as bad.

Let

```math
d_a
\tag{15.292}
```

be the dimension of the admissible Dirichlet fiber after removing gauge and
constraint zero modes in a physical block. At fixed R,

```math
d_a\asymp R^4a^{-4}.
\tag{15.293}
```

**Theorem 40.55 (Raw Fixed-Threshold Excess Is Over-UV-Sensitive).** Suppose
the Dirichlet minimizer is nondegenerate modulo gauge and constraint zero modes,
and the heat-kernel action has a quadratic expansion with cutoff parameter
t(a). Then the normalized excess partition function has Laplace asymptotics of
the form

```math
-\log Z_{\mathrm{ex}}(b,\xi_-,\xi_+)
\ge
c_1d_a\log\frac{1}{t(a)}
-
c_2d_a
+
o(d_a)
\tag{15.294}
```

along any frontier-good data family for which the Hessian is uniformly
nondegenerate. In particular, every F_fluc satisfying (15.275) must diverge
as the cutoff is removed. Hence no fixed excess threshold epsilon_R can make

```math
\exp
\left(
F_{\mathrm{fluc}}(R)-\varepsilon_R
\right)
\tag{15.295}
```

uniformly small.

#### Proof

Near the nondegenerate minimizer, choose local coordinates on the reduced
Dirichlet fiber. The heat-kernel action has the form

```math
\mathcal E(x)
=
\frac{1}{2t(a)}
\langle x,H_ax\rangle
+
O(|x|^3/t(a)),
\tag{15.296}
```

with H_a uniformly positive and bounded on the reduced fiber. The normalized
Haar density is smooth and nonzero in these coordinates. The standard
finite-dimensional Laplace estimate gives

```math
Z_{\mathrm{ex}}(b,\xi_-,\xi_+)
\le
C^{d_a}\,t(a)^{d_a/2},
\tag{15.297}
```

after absorbing determinant bounds into the constant C. Taking minus the
logarithm gives (15.294), with changed constants. Since d_a tends to infinity
and t(a) tends to zero along the continuum trajectory, the lower bound
diverges. Therefore the free-energy constant required in (15.275) diverges, and
a fixed epsilon_R cannot make (15.295) subcritical. `∎`

This does not mean the excess sector is hopeless. It means the bad event was
defined with the wrong microscopic threshold. The ultraviolet Gaussian
fluctuation free energy must be absorbed into the block normalization.

The corrected excess tail is:

```math
\mathcal E(\bar V)
\ge
F_{\mathrm{fluc}}(R,a)+\tau_R .
\tag{15.298}
```

With this renormalized threshold, the same Markov argument gives an exact bound.

**Criterion 40.56 (Renormalized Excess Tail).** Let

```math
F_{\mathrm{fluc}}(R,a)
:=
-\log Z_{\mathrm{ex}}(b,\xi_-,\xi_+).
\tag{15.299}
```

Then

```math
\mathsf K^s_{R,a,b}
\left[
\mathcal E(\bar V)
\ge
F_{\mathrm{fluc}}(R,a)+\tau_R
\mid
\xi_-,\xi_+
\right]
\le
e^{-\tau_R}.
\tag{15.300}
```

#### Proof

The numerator of the probability in (15.300) is bounded by

```math
e^{-F_{\mathrm{fluc}}(R,a)-\tau_R}.
\tag{15.301}
```

The denominator is

```math
Z_{\mathrm{ex}}
=
e^{-F_{\mathrm{fluc}}(R,a)}.
\tag{15.302}
```

Dividing gives (15.300). `∎`

Thus the third requested estimate must be replaced:

```math
\boxed{
\begin{array}{c}
\text{do not classify raw microscopic excess above a fixed threshold as bad;}\\
\text{classify excess above the block fluctuation free energy plus a margin.}
\end{array}
}
\tag{15.303}
```

#### 15.27.4. Corrected Status Of The Three Estimates

The requested proof of (15.279), (15.280), and (15.281) cannot be completed as
stated. The correct fixed-physical replacement is:

```math
\boxed{
\begin{array}{ll}
\text{P1 corrected:}
&
\text{prove (15.287), or coarsen to a finite physical loop test,}\\[1mm]
\text{P2 corrected:}
&
\text{prove the adjoint moment estimate (15.289),}\\[1mm]
\text{P3 corrected:}
&
\text{use the renormalized excess tail (15.300), not raw (15.281).}
\end{array}}
\tag{15.304}
```

This is still aligned with fixed physical IR. The correction is precisely what
fixed physical IR demands: the block has infinitely many microscopic degrees of
freedom as the cutoff is removed, so ordinary UV fluctuation entropy must be
integrated into the block kernel rather than counted as a bad polymer.

### 15.28. Implementing The Three Fixed-IR Repairs

Searchable repair tag:

`V4P40-IMPLEMENT-FIXED-IR-REPAIRS`.

The preceding subsection showed that the raw targets (15.279)-(15.281) are not
the final fixed-physical formulation. This subsection implements the three
repairs:

```math
\boxed{
\begin{array}{lll}
\text{chart escape}
&:&
\text{finite physical loop test plus residual UV-cocycle channel,}\\[1mm]
\text{large holonomy}
&:&
\text{finite physical adjoint collar moment,}\\[1mm]
\text{excess}
&:&
\text{renormalized excess above block fluctuation free energy.}
\end{array}}
\tag{15.305}
```

#### 15.28.1. Finite Physical Chart Test

Choose, for each physical block shape, a finite family of physical loop
representatives

```math
\mathcal L^{\mathrm{phys}}_R(Y)
\tag{15.306}
```

whose cardinality is independent of the cutoff. Define the physical chart-good
event by

```math
\mathcal G^{\mathrm{phys}}_{\rho}(Y)
:=
\left\{
d_{SO(3)}
\left(
\operatorname{Hol}_{\gamma},
1
\right)
\le\rho
\text{ for every }
\gamma\in\mathcal L^{\mathrm{phys}}_R(Y)
\right\}.
\tag{15.307}
```

This event is not the same as microscopic reconstructible goodness. It tests a
fixed physical atlas of holonomies. Therefore define the residual UV-cocycle
escape event:

```math
\mathcal E_{\mathrm{uvcoc}}(Y)
:=
\mathcal E_{\mathrm{esc}}(Y)
\cap
\mathcal G^{\mathrm{phys}}_{\rho_{\mathrm{chart}}'}(Y).
\tag{15.308}
```

The first corrected chart estimate is:

```math
|\mathcal L^{\mathrm{phys}}_R(Y)|
q_{\mathrm{phys}}(R,\rho_{\mathrm{chart}}')
+
q_{\mathrm{uvcoc}}(R,\rho_{\mathrm{chart}}')
\le
p_{\mathrm{chart}}(R),
\tag{15.309}
```

where

```math
q_{\mathrm{phys}}(R,\rho)
:=
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\sup_{\gamma\in\mathcal L^{\mathrm{phys}}_R(Y)}
\mathsf K^s_{R,a,b}
\left[
d_{SO(3)}
\left(
\operatorname{Hol}_{\gamma},
1
\right)
>
\rho
\mid
\xi_-
\right],
\tag{15.310}
```

and

```math
q_{\mathrm{uvcoc}}(R,\rho)
:=
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\mathsf K^s_{R,a,b}
\left[
\mathcal E_{\mathrm{uvcoc}}(Y)
\mid
\xi_-
\right].
\tag{15.311}
```

**Theorem 40.57 (Finite Physical Loops Require A UV-Cocycle Residual).** The
finite physical chart estimate (15.309) implies the chart-escape bound
(15.243), with p_esc replaced by p_chart. But the finite physical loop test
alone does not imply microscopic cocycle triviality.

#### Proof

The chart-escape event decomposes as

```math
\mathcal E_{\mathrm{esc}}(Y)
\subset
\left(
\mathcal G^{\mathrm{phys}}_{\rho_{\mathrm{chart}}'}(Y)
\right)^c
\cup
\mathcal E_{\mathrm{uvcoc}}(Y).
\tag{15.312}
```

The first term is controlled by a union bound over the finite physical loop
family, giving the first summand in (15.309). The second term is exactly
the residual channel in (15.311). This proves the implication.

For insufficiency of finite loops alone, choose a microscopic ball inside the
physical block disjoint from the selected finite loop representatives. Modify
the SO(3) connection inside that ball so that a microscopic reconstruction loop
leaves the section chart, while the holonomies of all loops in the finite
physical family (15.306) are unchanged. The physical loop test still passes, but
microscopic reconstructible goodness fails. Thus the residual UV-cocycle term
cannot be dropped. `∎`

This is the fixed-IR version of chart control. It removes the cutoff-growing
loop entropy from (15.287), but it does not pretend that finitely many physical
loops see every microscopic section event. The new analytic input is the
renormalized residual channel in (15.311).

#### 15.28.2. Finite Physical Adjoint Collar Moment

Likewise, replace the outgoing collar basis by a finite physical collar-loop
family

```math
\mathcal B^{\mathrm{phys}}_{A_+}(R).
\tag{15.313}
```

Define

```math
\Delta^{\mathrm{phys}}_{\mathrm{ad}}(R,\rho_H)
:=
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\sup_{\gamma\in\mathcal B^{\mathrm{phys}}_{A_+}(R)}
\left[
1
-
\frac{1}{3}
\mathsf K^s_{R,a,b}
\left(
\chi_{\mathrm{ad}}
\left(
\operatorname{Hol}_{\gamma}(\xi_+)
\right)
\mid
\xi_-
\right)
\right].
\tag{15.314}
```

The corrected large-holonomy estimate is

```math
\frac{|\mathcal B^{\mathrm{phys}}_{A_+}(R)|}{c_H(\rho_H)}
\Delta^{\mathrm{phys}}_{\mathrm{ad}}(R,\rho_H)
\le
p_{\mathrm{hol}}(R).
\tag{15.315}
```

**Criterion 40.58 (Finite Physical Adjoint Moment Controls Physical Collar
Holonomy).** If (15.315) holds, then the large outgoing holonomy bound holds
for the finite physical collar-loop test.

#### Proof

The proof is the same as Criterion 40.50, with the cutoff-independent loop
family (15.313) replacing the microscopic collar basis. The adjoint-character
inequality (15.267) bounds each large-holonomy indicator, and the finite union
bound gives (15.315). `∎`

The Feynman calculation to attempt is now sharply stated:

```math
\Delta^{\mathrm{phys}}_{\mathrm{ad}}(R,\rho_H)
\le
C_{\mathrm{shape}}\,g_{\mathrm{eff}}^2(R)
+
o_a(1),
\tag{15.316}
```

uniformly over frontier-good incoming collars and admissible center fields. If
this fails, then the failure is not a microscopic action failure; it is a real
failure of the finite physical collar response.

#### 15.28.3. Renormalized Excess Only

Replace the raw excess bad event by the renormalized event

```math
\mathcal E^{\mathrm{ren}}_{\mathrm{ex}}
:=
\left\{
\mathcal E(\bar V)
\ge
F_{\mathrm{fluc}}(R,a;b,\xi_-,\xi_+)+\tau_R
\right\},
\tag{15.317}
```

where

```math
F_{\mathrm{fluc}}(R,a;b,\xi_-,\xi_+)
:=
-\log
Z_{\mathrm{ex}}(b,\xi_-,\xi_+).
\tag{15.318}
```

Then Criterion 40.56 gives the exact bound

```math
p^{\mathrm{ren}}_{\mathrm{ex}}(R)
\le
e^{-\tau_R}.
\tag{15.319}
```

This is now cutoff-uniform by construction. The price is conceptual but
necessary: the block fluctuation free energy is part of the good block kernel,
not part of the bad polymer activity.

#### 15.28.4. Corrected Target 40.45

The corrected density-first target is:

**Target 40.59 (Renormalized Finite-Physical Density Bound).** Prove, or
disprove, that there are fixed physical parameters R, rho_chart, rho_H, and
tau_R such that

```math
p_{\mathrm{chart}}(R)
+
p_{\mathrm{hol}}(R)
+
e^{-\tau_R}
<
e^{-\log C_{\mathrm{blk}}-\kappa}.
\tag{15.320}
```

Here p_chart is controlled by (15.309), p_hol by (15.315), and the excess
contribution by (15.319). If (15.320) holds uniformly as the cutoff is removed,
then the corrected frontier-good Target 40.45 holds at fixed physical scale.

#### Proof

The corrected bad event is contained in the union of finite physical chart
escape, finite physical large outgoing collar holonomy, residual UV-cocycle
escape, and renormalized excess. Equations (15.309), (15.315), and (15.319)
bound these probabilities by the three terms appearing in (15.320). Condition
(15.320) is exactly the polymer entropy threshold. Criterion 40.46 then gives
the density-first bad-transfer bound, and Criterion 40.43 gives Target 40.41.
`∎`

This is the version of the route that remains aligned with fixed physical IR:

```math
\boxed{
\begin{array}{c}
\text{finite physical chart observables,}\\[1mm]
\text{finite physical adjoint collar moments,}\\[1mm]
\text{renormalized excess above block fluctuation free energy,}\\[1mm]
\text{all with constants independent of }a\text{ as }a\downarrow0.
\end{array}}
\tag{15.321}
```

The remaining analytic burden is no longer hidden:

```math
\boxed{
\begin{array}{ll}
\text{A:}
&
\text{control the residual UV-cocycle channel }q_{\mathrm{uvcoc}},\\[1mm]
\text{B:}
&
\text{prove the finite physical adjoint moment estimate (15.316).}
\end{array}}
\tag{15.322}
```

The excess channel is repaired exactly by renormalization. The two live
channels are chart/cocycle residuals and finite physical collar response.

### 15.29. Working Target 40.59: The Budgeted Fixed-IR Proof Plan

Searchable Target-40.59 work tag:

`V4P40-TARGET-4059-BUDGETED-FIXED-IR-PROOF`.

Target 40.59 is now a budget problem. Define the polymer threshold

```math
\Theta_{\mathrm{blk}}
:=
e^{-\log C_{\mathrm{blk}}-\kappa}.
\tag{15.323}
```

The target is to put the corrected one-block bad probability below

```math
\Theta_{\mathrm{blk}}.
\tag{15.324}
```

The renormalized excess term can be handled immediately.

**Lemma 40.60 (The Renormalized Excess Budget Can Always Be Made Small).** For
any number

```math
0<\Theta_{\mathrm{ex}}<\Theta_{\mathrm{blk}},
\tag{15.325}
```

choose

```math
\tau_R\ge \log\frac{1}{\Theta_{\mathrm{ex}}}.
\tag{15.326}
```

Then the renormalized excess contribution satisfies

```math
e^{-\tau_R}\le \Theta_{\mathrm{ex}}.
\tag{15.327}
```

#### Proof

This is immediate from (15.326). The important point is not the inequality
itself, but that it is cutoff-uniform because the UV fluctuation entropy has
already been absorbed into the block free energy in (15.317)-(15.319). `∎`

Thus the hard part of Target 40.59 is the remaining budget

```math
\Theta_{\mathrm{live}}
:=
\Theta_{\mathrm{blk}}-\Theta_{\mathrm{ex}}.
\tag{15.328}
```

It must be spent on two live channels:

```math
\boxed{
\begin{array}{c}
\text{finite physical adjoint holonomy response,}\\[1mm]
\text{residual UV-cocycle escape.}
\end{array}}
\tag{15.329}
```

The finite physical chart part is also an adjoint moment. Define

```math
\Delta^{\mathrm{phys}}_{\mathrm{chart}}(R,\rho)
:=
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\sup_{\gamma\in\mathcal L^{\mathrm{phys}}_R(Y)}
\left[
1
-
\frac{1}{3}
\mathsf K^s_{R,a,b}
\left(
\chi_{\mathrm{ad}}
\left(
\operatorname{Hol}_{\gamma}
\right)
\mid
\xi_-
\right)
\right].
\tag{15.330}
```

Let

```math
c_{\mathrm{chart}}
:=
c_H(\rho_{\mathrm{chart}}').
\tag{15.331}
```

Then the adjoint-character inequality gives:

**Criterion 40.61 (Finite Physical Chart Failure Is An Adjoint Moment).** If

```math
\frac{
|\mathcal L^{\mathrm{phys}}_R(Y)|
}{
c_{\mathrm{chart}}
}
\Delta^{\mathrm{phys}}_{\mathrm{chart}}(R,\rho_{\mathrm{chart}}')
+
q_{\mathrm{uvcoc}}(R,\rho_{\mathrm{chart}}')
\le
p_{\mathrm{chart}}(R),
\tag{15.332}
```

then the corrected chart estimate (15.309) holds.

#### Proof

Apply (15.267), with threshold rho_chart', to every loop in the finite physical
chart family. A union bound gives

```math
|\mathcal L^{\mathrm{phys}}_R(Y)|
q_{\mathrm{phys}}(R,\rho_{\mathrm{chart}}')
\le
\frac{
|\mathcal L^{\mathrm{phys}}_R(Y)|
}{
c_{\mathrm{chart}}
}
\Delta^{\mathrm{phys}}_{\mathrm{chart}}(R,\rho_{\mathrm{chart}}').
\tag{15.333}
```

Adding the residual channel gives (15.332), which is exactly (15.309). `∎`

Combine the chart adjoint moment with the outgoing-collar adjoint moment by
setting

```math
\mathcal A_{\mathrm{adj}}(R)
:=
\frac{
|\mathcal L^{\mathrm{phys}}_R(Y)|
}{
c_{\mathrm{chart}}
}
\Delta^{\mathrm{phys}}_{\mathrm{chart}}(R,\rho_{\mathrm{chart}}')
+
\frac{
|\mathcal B^{\mathrm{phys}}_{A_+}(R)|
}{
c_H(\rho_H)
}
\Delta^{\mathrm{phys}}_{\mathrm{ad}}(R,\rho_H).
\tag{15.334}
```

**Criterion 40.62 (Two-Channel Budget Proves Target 40.59).** Suppose that, at
some fixed physical block scale R,

```math
\mathcal A_{\mathrm{adj}}(R)
+
q_{\mathrm{uvcoc}}(R,\rho_{\mathrm{chart}}')
<
\Theta_{\mathrm{live}}.
\tag{15.335}
```

Then Target 40.59 holds.

#### Proof

Criterion 40.61 controls the finite physical chart part and the residual
UV-cocycle part. Criterion 40.58 controls the outgoing finite physical
large-holonomy part. Lemma 40.60 controls the renormalized excess part. Adding
the three estimates gives

```math
p_{\mathrm{chart}}(R)
+
p_{\mathrm{hol}}(R)
+
e^{-\tau_R}
<
\Theta_{\mathrm{live}}+\Theta_{\mathrm{ex}}
=
\Theta_{\mathrm{blk}} .
\tag{15.336}
```

This is exactly (15.320). `∎`

The remaining two analytic estimates can now be stated without decoration.

First, the finite physical adjoint moment estimate:

```math
\mathcal A_{\mathrm{adj}}(R)
\le
C_{\mathrm{adj}}(R)\,g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.337}
```

Second, residual UV-cocycle irrelevance:

```math
q_{\mathrm{uvcoc}}(R,\rho_{\mathrm{chart}}')
\le
\epsilon_{\mathrm{uv}}(R)
+
o_a(1).
\tag{15.338}
```

If there exists a sufficiently small fixed physical R such that

```math
C_{\mathrm{adj}}(R)\,g_{\mathrm{eff}}^2(R)
+
\epsilon_{\mathrm{uv}}(R)
<
\Theta_{\mathrm{live}},
\tag{15.339}
```

then Target 40.59 follows for all sufficiently small cutoffs.

This gives the honest Feynman calculation:

```math
\boxed{
\begin{array}{c}
\text{compute finite physical adjoint collar moments,}\\[1mm]
\text{compute the residual UV-cocycle probability,}\\[1mm]
\text{check whether their sum beats the polymer threshold.}
\end{array}}
\tag{15.340}
```

It also gives the Einstein invariant form:

```math
\boxed{
\begin{array}{c}
\text{the only bad physical block channels left are}\\[1mm]
\text{finite adjoint boundary response and residual cocycle escape.}
\end{array}}
\tag{15.341}
```

There is one more useful diagnostic for the residual UV-cocycle term. In a
one-cell union-bound model, suppose a microscopic chart-escape event inside a
physical block has a one-cell cost of the form

```math
\exp
\left(
-
\frac{c_{\mathrm{uv}}}{t(a)}
\right)
\tag{15.342}
```

and the number of possible microscopic locations is bounded by

```math
C_Ra^{-4}.
\tag{15.343}
```

Then

```math
q_{\mathrm{uvcoc}}(R,\rho_{\mathrm{chart}}')
\le
C_Ra^{-4}
\exp
\left(
-
\frac{c_{\mathrm{uv}}}{t(a)}
\right).
\tag{15.344}
```

Thus the residual channel vanishes if

```math
\frac{c_{\mathrm{uv}}}{t(a)}
-
4\log\frac{1}{a}
\longrightarrow
+\infty .
\tag{15.345}
```

This is not assumed as a theorem. It is a precise test. If (15.345) fails, then
the residual UV-cocycle channel may survive the continuum limit even though all
finite physical loop tests pass.

The final current target is therefore:

**Target 40.63 (Adjoint Response Plus Residual Cocycle Irrelevance).** Prove, or
disprove, the pair of fixed-physical estimates (15.337) and (15.338), with R
fixed first and constants uniform as the cutoff is removed.

If Target 40.63 holds with the budget condition (15.339), then Target 40.59
holds. If either estimate fails, the center-resolved route fails through a
specific channel: finite adjoint boundary response or residual UV-cocycle
escape.

### 15.30. Target 40.64: Residual Cocycle Effect, Not Residual Probability

Searchable Target-40.64 tag:

`V4P40-TARGET-4064-RESIDUAL-COCYCLE-EFFECT`.

Target 40.63 still asks for a probability bound on residual microscopic
cocycle escape. That is sufficient, but it may be too strong. The Wilson route
does not need every microscopic chart failure to be rare. It needs those
failures not to leave an area-supported contribution after the exact block
response is integrated.

Thus the next correction is:

```math
\boxed{
\begin{array}{c}
\text{replace residual cocycle escape probability}\\[1mm]
\text{by residual cocycle effect in the block response.}
\end{array}}
\tag{15.346}
```

This is the invariant form of the remaining problem. It asks how much the exact
cocycle insertion differs from the finite-physical chart representative after
the interior SO(3) variables have been integrated out.

Let

```math
\widehat{\mathsf K}^s_{R,a,b}
\left(
d\bar V,d\xi_+\mid\xi_-
\right)
\tag{15.347}
```

be the full normalized block law, including both interior SO(3) variables and
the outgoing collar. Its outgoing-collar marginal is the kernel (15.217).

Let

```math
\mathcal C^s_Y(\bar V,\xi_+)
\tag{15.348}
```

be the exact local cocycle factor carried by the portion of the spanning
surface inside the block family Y. Let

```math
\mathcal C^{s,\mathrm{phys}}_Y(\xi_-,\xi_+)
\tag{15.349}
```

be the boundary representative obtained from the finite physical chart test.
On the finite physical chart-good event, this is the boundary term produced by
the chosen physical chart. Outside that event, choose any bounded representative
with absolute value at most one.

Define the residual cocycle-effect norm:

```math
\mathfrak r_{\mathrm{coc}}(R)
:=
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\left|
\int
\left(
\mathcal C^s_Y(\bar V,\xi_+)
-
\mathcal C^{s,\mathrm{phys}}_Y(\xi_-,\xi_+)
\right)
\widehat{\mathsf K}^s_{R,a,b}
\left(
d\bar V,d\xi_+\mid\xi_-
\right)
\right|.
\tag{15.350}
```

This is not a probability. It is the norm of the residual contribution to the
block cocycle response.

**Lemma 40.64 (Residual Probability Implies Residual Effect).** If the exact
cocycle factor and the finite physical chart representative agree outside the
residual event (15.308), then

```math
\mathfrak r_{\mathrm{coc}}(R)
\le
2\,q_{\mathrm{uvcoc}}(R,\rho_{\mathrm{chart}}').
\tag{15.351}
```

#### Proof

The two cocycle factors have absolute value at most one. Their difference is
zero outside the residual event and has absolute value at most two on that
event. Integrating gives (15.351). `∎`

Thus residual probability control remains sufficient. The new point is that it
is not necessary.

**Theorem 40.65 (Residual Effect Is Strictly Weaker Than Residual Probability).**
A small residual-effect norm does not imply a small residual-event probability.

#### Proof

Consider a comparison block law in which the residual event has probability one,
but the residual cocycle difference is a sign taking values plus one and minus
one with equal conditional probability. Then

```math
\mathbb P
\left[
\mathcal E_{\mathrm{uvcoc}}(Y)
\right]
=
1,
\tag{15.352}
```

while

```math
\left|
\mathbb E
\left[
\mathcal C^s_Y
-
\mathcal C^{s,\mathrm{phys}}_Y
\right]
\right|
=
0 .
\tag{15.353}
```

Therefore the effect can vanish even when the residual event is certain. `∎`

This theorem is not a claim that Yang-Mills has such cancellation. It only
records the logical distinction: probability control is a Peierls-type route;
effect control is a response-kernel route.

The effect-level replacement for Target 40.63 is:

**Target 40.66 (Adjoint Response Plus Residual Cocycle Effect).** Prove, or
disprove, the pair of fixed-physical estimates

```math
\mathcal A_{\mathrm{adj}}(R)
\le
C_{\mathrm{adj}}(R)\,g_{\mathrm{eff}}^2(R)
+
o_a(1),
\tag{15.354}
```

and

```math
\mathfrak r_{\mathrm{coc}}(R)
\le
\epsilon_{\mathrm{coc}}(R)
+
o_a(1),
\tag{15.355}
```

with R fixed first and constants uniform as the cutoff is removed.

If there is a choice of physical block scale and excess budget such that

```math
C_{\mathrm{adj}}(R)\,g_{\mathrm{eff}}^2(R)
+
\epsilon_{\mathrm{coc}}(R)
<
\Theta_{\mathrm{live}},
\tag{15.356}
```

then the residual contribution is below the polymer threshold in the response
norm.

**Criterion 40.67 (Effect Budget Gives Cocycle Quasilocality).** Suppose Target
40.66 holds and the budget inequality (15.356) holds. Then the exact block
cocycle response has a boundary/quasilocal decomposition with summable
residual tails. Consequently the conditional cocycle obstruction is controlled
in the structural sense needed by Criterion 40.6.

#### Proof

Use the exact block response decomposition. The finite physical adjoint
response controls failures of the finite physical chart and outgoing collar
holonomy, through the same adjoint-character bounds as Criteria 40.58 and
40.61. The renormalized excess contribution is controlled by Lemma 40.60. The
only remaining term is the residual cocycle difference. By (15.355), its
one-block contribution is bounded in absolute response norm by epsilon_coc,
up to a cutoff error.

The sum of these non-boundary response contributions is below the polymer
threshold by (15.356). Iterating the block response over a connected block
growth gives an absolutely summable expansion for the non-boundary remainder.
On the complement, the finite physical chart representative is a boundary
observable. Therefore the full cocycle response is boundary/quasilocal with
summable residual tails. Criterion 40.6 then supplies the Wilson sheet
domination estimate whenever the matching center-sheet disorder estimate is
present. `∎`

This criterion does not literally prove Target 40.59, because Target 40.59 is a
probability-density statement. It proves the more directly relevant
replacement: the exact residual contribution to the cocycle response is
summable. For the Wilson route, this is the right object.

The final live target is therefore:

```math
\boxed{
\begin{array}{c}
\text{compute finite physical adjoint response,}\\[1mm]
\text{compute residual cocycle effect,}\\[1mm]
\text{and prove their sum is below the block threshold.}
\end{array}}
\tag{15.357}
```

Feynman's calculation is the pair of block integrals in (15.354) and (15.355).
Einstein's invariant reformulation is that microscopic chart failures matter
only through their integrated effect on the block cocycle response.

### 15.31. Working Target 40.66: Fixed-Physical Response Form

Searchable Target-40.66 work tag:

`V4P40-TARGET-4066-FIXED-PHYSICAL-RESPONSE-FORM`.

To avoid a misleading phrase, from this point on the quantity in (15.350) should
be called the renormalized residual cocycle response:

```math
\mathfrak R_{\mathrm{coc}}(R)
:=
\mathfrak r_{\mathrm{coc}}(R).
\tag{15.358}
```

The name matters. This is not a microscopic probability estimate. It is a
fixed-physical block response:

```math
\boxed{
\begin{array}{c}
\text{fix the physical block scale }R,\\[1mm]
\text{integrate all microscopic SO(3) variables in the block,}\\[1mm]
\text{compare the exact cocycle response}\\[1mm]
\text{with its finite-chart boundary representative,}\\[1mm]
\text{then take }a\downarrow0\text{ with constants independent of }a.
\end{array}}
\tag{15.359}
```

This is the fixed-IR aligned version of the residual problem.

#### 15.31.1. The Adjoint Response Estimate

For every loop in the finite physical chart and collar families, set

```math
\mathcal D_{\mathrm{ad}}(\gamma)
:=
1
-
\frac{1}{3}
\mathsf K^s_{R,a,b}
\left(
\chi_{\mathrm{ad}}
\left(
\operatorname{Hol}_{\gamma}
\right)
\mid
\xi_-
\right).
\tag{15.360}
```

The needed finite-physical adjoint estimate is the following.

**Target 40.68 (Finite-Physical Adjoint Character Bound).** Prove, or disprove,
that for every loop in the finite physical chart and outgoing-collar families,

```math
\mathcal D_{\mathrm{ad}}(\gamma)
\le
C_{\gamma}(R)\,g_{\mathrm{eff}}^2(R)
+
o_a(1),
\tag{15.361}
```

uniformly over admissible center fields and frontier-good incoming collars.

**Criterion 40.69 (Adjoint Character Bounds Prove (15.354)).** If Target 40.68
holds and

```math
C_{\mathrm{adj}}(R)
:=
\frac{
|\mathcal L^{\mathrm{phys}}_R(Y)|
}{
c_{\mathrm{chart}}
}
\sup_{\gamma\in\mathcal L^{\mathrm{phys}}_R(Y)}
C_{\gamma}(R)
+
\frac{
|\mathcal B^{\mathrm{phys}}_{A_+}(R)|
}{
c_H(\rho_H)
}
\sup_{\gamma\in\mathcal B^{\mathrm{phys}}_{A_+}(R)}
C_{\gamma}(R),
\tag{15.362}
```

then the adjoint response estimate (15.354) holds.

#### Proof

Insert (15.361) into the two finite sums appearing in (15.334). The chart
family and outgoing-collar family have cutoff-independent cardinality at fixed
physical R. Taking the supremum over each family gives exactly (15.362), and
the remaining cutoff errors are still o_a(1). `∎`

Thus the adjoint half of Target 40.66 is a concrete finite list of character
estimates for the exact block kernel. It is not a full SO(3) mass gap theorem.

#### 15.31.2. The Residual Response Estimate

Define the block residual observable

```math
\mathcal X^s_Y(\bar V,\xi_-,\xi_+)
:=
\mathcal C^s_Y(\bar V,\xi_+)
-
\mathcal C^{s,\mathrm{phys}}_Y(\xi_-,\xi_+).
\tag{15.363}
```

Then

```math
\mathfrak R_{\mathrm{coc}}(R)
=
\sup_{a,b,\xi_-}
\left|
\widehat{\mathsf K}^s_{R,a,b}
\left(
\mathcal X^s_Y
\mid
\xi_-
\right)
\right|.
\tag{15.364}
```

The right attack is not to count all microscopic chart failures. It is to
expand the residual observable after the block variables are integrated.

Suppose the residual response admits a connected residual-cluster expansion
inside the fixed physical block:

```math
\widehat{\mathsf K}^s_{R,a,b}
\left(
\mathcal X^s_Y
\mid
\xi_-
\right)
=
\sum_{\mathcal X\subset Y}
w_{\mathrm{res}}(\mathcal X;b,\xi_-),
\tag{15.365}
```

where the sum is over connected residual clusters in the physical block atlas.

**Criterion 40.70 (Residual Cluster Bound Proves (15.355)).** If

```math
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\sum_{\mathcal X\subset Y}
\left|
w_{\mathrm{res}}(\mathcal X;b,\xi_-)
\right|
\le
\epsilon_{\mathrm{coc}}(R)
+
o_a(1),
\tag{15.366}
```

then the residual response estimate (15.355) holds.

#### Proof

Take absolute values in (15.365), then apply (15.366). This gives

```math
\left|
\widehat{\mathsf K}^s_{R,a,b}
\left(
\mathcal X^s_Y
\mid
\xi_-
\right)
\right|
\le
\epsilon_{\mathrm{coc}}(R)
+
o_a(1)
\tag{15.367}
```

uniformly over the data in the definition of (15.350). Taking the supremum
gives (15.355). `∎`

This criterion is deliberately response-level. It permits microscopic residual
events to occur frequently if their integrated contribution cancels or
renormalizes into local boundary terms.

#### 15.31.3. The Fixed-IR Target After The Reformulation

Combining Criteria 40.69 and 40.70 gives the proof-ready version of Target
40.66:

**Target 40.71 (Finite Adjoint Characters And Residual Clusters).** Prove, or
disprove, both of the following fixed-physical estimates:

```math
\mathcal D_{\mathrm{ad}}(\gamma)
\le
C_{\gamma}(R)\,g_{\mathrm{eff}}^2(R)
+
o_a(1)
\tag{15.368}
```

for every loop in the finite physical chart and collar families, and

```math
\sum_{\mathcal X\subset Y}
\left|
w_{\mathrm{res}}(\mathcal X;b,\xi_-)
\right|
\le
\epsilon_{\mathrm{coc}}(R)
+
o_a(1).
\tag{15.369}
```

If the resulting constants obey

```math
C_{\mathrm{adj}}(R)g_{\mathrm{eff}}^2(R)
+
\epsilon_{\mathrm{coc}}(R)
<
\Theta_{\mathrm{live}},
\tag{15.370}
```

then Target 40.66 holds, hence Criterion 40.67 gives the fixed-physical
boundary/quasilocal cocycle response.

This is the current sharp form of the problem. Feynman's task is to compute the
finite list of adjoint character defects and the residual-cluster expansion.
Einstein's task is to keep the object invariant: a fixed physical block
response, not a microscopic defect probability.

### 15.32. Target 40.72: Adjoint Characters From Curvature-Flux Variance

Searchable Target-40.72 tag:

`V4P40-TARGET-4072-ADJOINT-FLUX-VARIANCE`.

Target 40.68 is the most concrete finite-physical calculation left. It asks for
a small adjoint character defect for each loop in a finite physical atlas. The
right reduction is:

```math
\boxed{
\begin{array}{c}
\text{adjoint character defect}\\[1mm]
\Longleftarrow
\text{finite-loop holonomy second moment}\\[1mm]
\Longleftarrow
\text{curvature-flux variance plus non-Abelian Stokes remainder.}
\end{array}}
\tag{15.371}
```

The order of limits remains:

```math
R\text{ fixed first},
\qquad
a\downarrow0\text{ second}.
\tag{15.372}
```

Only after obtaining cutoff-uniform estimates may R be chosen small.

#### 15.32.1. Character Defect From Holonomy Distance

Use the geodesic distance on SO(3), normalized so that a rotation by angle
theta has distance theta. For the adjoint character,

```math
\chi_{\mathrm{ad}}(g)
=
1+2\cos\theta(g).
\tag{15.373}
```

Therefore

```math
1-\frac{1}{3}\chi_{\mathrm{ad}}(g)
=
\frac{2}{3}
\left(
1-\cos\theta(g)
\right)
\le
\frac{1}{3}
d_{SO(3)}(g,1)^2 .
\tag{15.374}
```

**Criterion 40.72 (Holonomy Second Moment Proves Target 40.68).** Suppose that
for every loop gamma in the finite physical chart and outgoing-collar families,

```math
\mathsf K^s_{R,a,b}
\left[
d_{SO(3)}
\left(
\operatorname{Hol}_{\gamma},
1
\right)^2
\mid
\xi_-
\right]
\le
C^{(2)}_{\gamma}(R)\,g_{\mathrm{eff}}^2(R)
+
o_a(1)
\tag{15.375}
```

uniformly over admissible center fields and frontier-good incoming collars.
Then Target 40.68 holds with

```math
C_{\gamma}(R)
=
\frac{1}{3}C^{(2)}_{\gamma}(R).
\tag{15.376}
```

#### Proof

Apply (15.374) to the outgoing holonomy and take the block-kernel expectation.
The estimate (15.375) gives (15.361) with the constant in (15.376). `∎`

This is already a useful simplification. The adjoint character bound is a
second-moment holonomy bound for finitely many physical loops.

#### 15.32.2. Holonomy Second Moment From Curvature Flux

Fix one finite physical loop gamma and choose a physical spanning disk

```math
\Sigma_{\gamma}\subset B_R .
\tag{15.377}
```

Let

```math
\Sigma_{\gamma,a}
\tag{15.378}
```

be a lattice plaquette approximation. In a disk tree gauge, define the
parallel-transported lattice curvature flux

```math
\Phi_{\gamma,a}(\bar V)
:=
\sum_{p\subset\Sigma_{\gamma,a}}
\operatorname{Ad}_{\tau_p}
\log(\bar V_p),
\tag{15.379}
```

whenever all plaquette holonomies in the disk lie in the principal logarithm
chart. Here tau_p is the tree path transporting the plaquette logarithm to the
base point of gamma. This flux is an auxiliary chart variable; the invariant
quantity being estimated remains the loop holonomy in (15.375). Define the
non-Abelian Stokes remainder by

```math
\mathcal N_{\gamma,a}(\bar V)
:=
d_{SO(3)}
\left(
\operatorname{Hol}_{\gamma},
1
\right)^2
-
C_{\gamma}^{\mathrm{St}}
\left|
\Phi_{\gamma,a}(\bar V)
\right|^2,
\tag{15.380}
```

with C_gamma^St chosen large enough that the positive part of the remainder
controls commutator and chart-error terms.

The analytic estimate one wants is:

```math
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi_{\gamma,a}
\right|^2
\mid
\xi_-
\right]
\le
C^{\Phi}_{\gamma}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1),
\tag{15.381}
```

and

```math
\mathsf K^s_{R,a,b}
\left[
\left(
\mathcal N_{\gamma,a}
\right)_+
\mid
\xi_-
\right]
\le
C^{N}_{\gamma}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.382}
```

**Criterion 40.73 (Curvature-Flux Variance Proves Holonomy Second Moment).** If
(15.381) and (15.382) hold uniformly for gamma, then (15.375) holds with

```math
C^{(2)}_{\gamma}(R)
=
C_{\gamma}^{\mathrm{St}}C^{\Phi}_{\gamma}(R)
+
C^{N}_{\gamma}(R).
\tag{15.383}
```

#### Proof

By the definition of the positive part in (15.380),

```math
d_{SO(3)}
\left(
\operatorname{Hol}_{\gamma},
1
\right)^2
\le
C_{\gamma}^{\mathrm{St}}
\left|
\Phi_{\gamma,a}
\right|^2
+
\left(
\mathcal N_{\gamma,a}
\right)_+ .
\tag{15.384}
```

Taking the block-kernel expectation and applying (15.381)-(15.382) gives
(15.375) with the constant (15.383). `∎`

This criterion is deliberately modest. It does not claim that the continuum
curvature field exists pointwise. It only asks for a finite physical flux
variance for a finite list of loops.

#### 15.32.3. The Fixed-Physical Flux Target

The Feynman calculation is now the following finite list of estimates.

**Target 40.74 (Fixed-Physical Curvature-Flux Variance).** For every loop gamma
in the finite physical chart and outgoing-collar families, prove or disprove
the two cutoff-uniform estimates (15.381) and (15.382), with R fixed first and
with constants uniform over admissible center fields and frontier-good incoming
collars.

If Target 40.74 holds, then Criteria 40.73 and 40.72 imply Target 40.68.

The Einstein invariant reading is:

```math
\boxed{
\begin{array}{c}
\text{Target 40.68 is not a lattice plaquette estimate;}\\[1mm]
\text{it is a fixed physical curvature-flux variance estimate}\\[1mm]
\text{for finitely many physical loops in the exact block response.}
\end{array}}
\tag{15.385}
```

The remaining hard analytic input is therefore:

```math
\boxed{
\begin{array}{c}
\text{under the exact fixed-center SO(3) block kernel,}\\[1mm]
\text{finite physical curvature flux through small disks has variance}\\[1mm]
\text{of order }g_{\mathrm{eff}}^2(R)\text{, uniformly as }a\downarrow0.
\end{array}}
\tag{15.386}
```

This is narrower than a mass-gap theorem. It is also not a UV plaquette-smallness
claim: the disk has fixed physical size R, contains many lattice plaquettes, and
the estimate is made only after integrating the block response.

### 15.33. Target 40.75: Renormalized Finite-Physical Adjoint Holonomy

Searchable Target-40.75 tag:

`V4P40-TARGET-4075-RENORMALIZED-ADJOINT-HOLONOMY`.

Target 40.74 is the right final reduction only if the loop holonomy and disk
flux in (15.375)-(15.382) are already physical observables. If they are raw
thin lattice observables, then perimeter, cusp, and chart noise can survive the
continuum limit. That would turn a fixed-IR argument into a disguised UV
regularity assumption.

The fixed-IR repair is to choose the physical resolution first:

```math
\boxed{
\begin{array}{c}
\text{fix the physical loop scale }R,\\[1mm]
\text{fix a physical smoothing or blocking scale below }R,\\[1mm]
\text{define the finite-loop observable at that physical resolution,}\\[1mm]
\text{then take }a\downarrow0\text{ with constants independent of }a.
\end{array}}
\tag{15.387}
```

Choose a physical smoothing radius and, when useful, an equivalent flow time:

```math
0<\ell_R<c_0R,
\qquad
s_R\asymp \ell_R^2 .
\tag{15.388}
```

Let the smoothing map be a gauge-covariant finite-range block map from the
microscopic outgoing SO(3) field to a physical-resolution SO(3) field:

```math
\mathscr S_R:\bar V\longmapsto \bar V^{(R)} .
\tag{15.389}
```

The renormalized finite-loop holonomy is

```math
H^{\mathrm{ren}}_{\gamma,R}(\bar V)
:=
\operatorname{Hol}_{\gamma}
\left(
\bar V^{(R)}
\right)
\in SO(3).
\tag{15.390}
```

The corresponding adjoint defect is

```math
\mathcal D^{\mathrm{ren}}_{\mathrm{ad}}(\gamma;R)
:=
1
-
\frac{1}{3}
\mathsf K^s_{R,a,b}
\left[
\chi_{\mathrm{ad}}
\left(
H^{\mathrm{ren}}_{\gamma,R}
\right)
\mid
\xi_-
\right].
\tag{15.391}
```

**Target 40.75 (Renormalized Finite-Physical Adjoint Holonomy Bound).** For
every loop gamma in the finite physical chart and outgoing-collar families,
prove or disprove the cutoff-uniform estimate

```math
\mathcal D^{\mathrm{ren}}_{\mathrm{ad}}(\gamma;R)
\le
C^{\mathrm{ren}}_{\gamma}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1),
\tag{15.392}
```

uniformly over admissible center fields and frontier-good incoming collars.

This is the fixed-physical version of Target 40.68. It does not assert that
microscopic plaquette holonomies are close to the identity. It asserts that the
finite physical holonomy seen at resolution (15.388) has small adjoint defect.

#### 15.33.1. Renormalized Holonomy Second Moment

For SO(3), the same elementary character inequality used in (15.374) gives

```math
1-\frac{1}{3}\chi_{\mathrm{ad}}(h)
\le
C_{\mathrm{ad}}\,d_{SO(3)}(h,1)^2 .
\tag{15.393}
```

Therefore Target 40.75 follows from the renormalized second-moment estimate

```math
\mathsf K^s_{R,a,b}
\left[
d_{SO(3)}
\left(
H^{\mathrm{ren}}_{\gamma,R},
1
\right)^2
\mid
\xi_-
\right]
\le
C^{(2),\mathrm{ren}}_{\gamma}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.394}
```

**Criterion 40.76 (Renormalized Holonomy Moment Proves Target 40.75).** If
(15.394) holds uniformly for gamma, then (15.392) holds with

```math
C^{\mathrm{ren}}_{\gamma}(R)
=
C_{\mathrm{ad}}C^{(2),\mathrm{ren}}_{\gamma}(R).
\tag{15.395}
```

#### Proof

Apply (15.393) to (15.391), then use (15.394). `∎`

#### 15.33.2. Renormalized Curvature Flux

Define the physical-resolution curvature flux through the same disk family by
applying the block map before taking the disk response:

```math
\Phi^{\mathrm{ren}}_{\gamma,R}(\bar V)
:=
\Phi_{\gamma,R}
\left(
\mathscr S_R\bar V
\right).
\tag{15.396}
```

This symbol denotes the gauge-covariant disk flux associated with the
physical-resolution field. It is not a sum of unsmoothed microscopic plaquette
logarithms.

Define the renormalized non-Abelian Stokes remainder by

```math
\mathcal N^{\mathrm{ren}}_{\gamma,R}(\bar V)
:=
d_{SO(3)}
\left(
H^{\mathrm{ren}}_{\gamma,R},
1
\right)^2
-
C^{\mathrm{St},\mathrm{ren}}_{\gamma}
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}(\bar V)
\right|^2 .
\tag{15.397}
```

The renormalized replacement for Target 40.74 is the pair of estimates

```math
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|^2
\mid
\xi_-
\right]
\le
C^{\Phi,\mathrm{ren}}_{\gamma}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1),
\tag{15.398}
```

and

```math
\mathsf K^s_{R,a,b}
\left[
\left(
\mathcal N^{\mathrm{ren}}_{\gamma,R}
\right)_+
\mid
\xi_-
\right]
\le
C^{N,\mathrm{ren}}_{\gamma}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.399}
```

**Criterion 40.77 (Renormalized Flux Variance Proves Renormalized Holonomy
Moment).** If (15.398) and (15.399) hold uniformly for gamma, then (15.394)
holds with

```math
C^{(2),\mathrm{ren}}_{\gamma}(R)
=
C^{\mathrm{St},\mathrm{ren}}_{\gamma}
C^{\Phi,\mathrm{ren}}_{\gamma}(R)
+
C^{N,\mathrm{ren}}_{\gamma}(R).
\tag{15.400}
```

#### Proof

By (15.397),

```math
d_{SO(3)}
\left(
H^{\mathrm{ren}}_{\gamma,R},
1
\right)^2
\le
C^{\mathrm{St},\mathrm{ren}}_{\gamma}
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|^2
+
\left(
\mathcal N^{\mathrm{ren}}_{\gamma,R}
\right)_+ .
\tag{15.401}
```

Take the block-kernel expectation and apply (15.398)-(15.399). `∎`

#### 15.33.3. The Bridge Back To The Exact Cocycle Route

Target 40.75 is automatically enough only if the finite physical chart and
collar observables in the cocycle route are defined with the same physical
block map. If the route still uses raw thin holonomies, one more bridge is
required.

Define the raw-to-renormalized adjoint mismatch by

```math
\Delta^{\mathrm{thinren}}_{\gamma,R}
:=
\mathsf K^s_{R,a,b}
\left[
\left|
\chi_{\mathrm{ad}}
\left(
\operatorname{Hol}_{\gamma}
\right)
-
\chi_{\mathrm{ad}}
\left(
H^{\mathrm{ren}}_{\gamma,R}
\right)
\right|
\mid
\xi_-
\right].
\tag{15.402}
```

There are then two valid ways forward:

```math
\boxed{
\begin{array}{c}
\text{either prove that the raw-to-renormalized mismatch is harmless,}\\[1mm]
\text{or rebuild the exact cocycle atlas at physical resolution}\\[1mm]
\text{and charge the leftover difference to the residual response.}
\end{array}}
\tag{15.403}
```

The first option asks for

```math
\Delta^{\mathrm{thinren}}_{\gamma,R}
\le
C^{\Delta}_{\gamma}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.404}
```

The second option asks for the atlas-replacement residual to satisfy the same
kind of response bound as (15.369):

```math
\sum_{\mathcal X\subset Y}
\left|
w^{\mathrm{renatlas}}_{\mathrm{res}}
(\mathcal X;b,\xi_-)
\right|
\le
\epsilon_{\mathrm{ren}}(R)
+
o_a(1).
\tag{15.405}
```

**Criterion 40.78 (Renormalized Route Still Proves The Fixed-IR Cocycle
Bound).** Suppose Target 40.75 holds for the finite physical chart and collar
families. Suppose also that either (15.404) holds for the raw route, or the
renormalized-atlas residual estimate (15.405) holds after rebuilding the
cocycle atlas at physical resolution. Then Target 40.71 is recovered with an
extra budget term:

```math
C_{\mathrm{adj}}^{\mathrm{ren}}(R)g_{\mathrm{eff}}^2(R)
+
\epsilon_{\mathrm{coc}}(R)
+
\epsilon_{\mathrm{bridge}}(R)
<
\Theta_{\mathrm{live}} .
\tag{15.406}
```

Here the bridge term is supplied by either the raw-to-renormalized mismatch or
the renormalized-atlas residual:

```math
\epsilon_{\mathrm{bridge}}(R)
=
\begin{cases}
C_{\Delta}(R)g_{\mathrm{eff}}^2(R),
&
\text{under the mismatch route},\\[1mm]
\epsilon_{\mathrm{ren}}(R),
&
\text{under the atlas-replacement route}.
\end{cases}
\tag{15.407}
```

The conclusion is sharp. Raw Target 40.74 is a useful diagnostic, but the
fixed-physical proof should not depend on unsmoothed thin-loop regularity unless
the bridge estimate (15.404) is actually proved. Otherwise the honest next
object is Target 40.75 together with the atlas-replacement response (15.405).

### 15.34. Working Target 40.75: The Flowed Block Proof Package

Searchable Target-40.75 work tag:

`V4P40-TARGET-4075-FLOWED-BLOCK-PACKAGE`.

The previous section says what Target 40.75 should be. This section records the
proof package I would try first.

The fixed-IR order of operations is non-negotiable:

```math
\boxed{
\begin{array}{c}
R\text{ fixed physically},\\[1mm]
\ell_R\text{ fixed physically with }0<\ell_R<c_0R,\\[1mm]
a\downarrow0\text{ only after the observable is defined at scale }\ell_R.
\end{array}}
\tag{15.408}
```

The proof is not allowed to shrink the smoothing radius with the lattice
spacing.

#### 15.34.1. Canonical Candidate For The Smoothing Map

Use the SO(3) lattice Wilson flow as the canonical candidate for the map in
(15.389). Let

```math
\bar V_t
\tag{15.409}
```

solve the finite-cutoff SO(3) gradient-flow equation

```math
\frac{d}{dt}\bar V_{t,\ell}
=
-
\nabla_{\ell}S_{\mathrm{SO3},a}(\bar V_t)\,
\bar V_{t,\ell},
\qquad
\bar V_{0,\ell}=\bar V_{\ell}.
\tag{15.410}
```

Here the gradient is the left-invariant Lie algebra gradient of the local
SO(3) plaquette action. Define

```math
\mathscr S_R(\bar V)
:=
\bar V_{s_R},
\qquad
s_R=\lambda_R\ell_R^2 .
\tag{15.411}
```

The flow choice is useful because it has the three invariances needed by the
cocycle route:

```math
\boxed{
\begin{array}{c}
\text{gauge covariance,}\\[1mm]
\text{center blindness after passage to }SO(3),\\[1mm]
\text{physical smoothing radius fixed before }a\downarrow0.
\end{array}}
\tag{15.412}
```

For the proof, it is enough to require the following admissible-smoother
properties.

**S1. Gauge covariance.**

```math
\mathscr S_R(g\bar V g^{-1})
=
g\,\mathscr S_R(\bar V)\,g^{-1}.
\tag{15.413}
```

**S2. Physical locality.** There are constants independent of the cutoff such
that the influence kernel of the map obeys

```math
\left\|
\nabla_{\ell'}
\left(
\mathscr S_R(\bar V)
\right)_{\ell}
\right\|
\le
C_R
\exp
\left(
-
c_R
\frac{
d(\ell,\ell')^2
}{
\ell_R^2
}
\right).
\tag{15.414}
```

**S3. Energy dissipation.**

```math
S_{\mathrm{SO3},a}(\bar V_{s_R})
+
\int_0^{s_R}
\left\|
\nabla S_{\mathrm{SO3},a}(\bar V_t)
\right\|^2
dt
\le
S_{\mathrm{SO3},a}(\bar V).
\tag{15.415}
```

**S4. Cutoff-stable response norm.** For every finite physical loop family,
the renormalized holonomies have cutoff-uniform Lipschitz norm:

```math
\sup_{a<a_0}
\sum_{\ell'}
\left\|
\nabla_{\ell'}
H^{\mathrm{ren}}_{\gamma,R}
\right\|^2
<
\infty .
\tag{15.416}
```

The Wilson flow is the preferred candidate because S1 and S3 are structural,
and S2-S4 are the finite-propagation or heat-kernel regularization estimates one
expects at positive physical flow time.

#### 15.34.2. Deterministic Stokes Control At Physical Resolution

After smoothing, the loop holonomy should be controlled by the physical disk
curvature and a true non-Abelian commutator remainder. The deterministic
statement needed is the following.

**Criterion 40.79 (Flowed Stokes Control).** Suppose that for each loop gamma in
the finite physical families there are cutoff-independent constants such that
for every outgoing SO(3) field,

```math
d_{SO(3)}
\left(
H^{\mathrm{ren}}_{\gamma,R},
1
\right)^2
\le
C^{\mathrm{flux}}_{\gamma}(R,\ell_R)
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|^2
+
\mathcal Q^{\mathrm{ren}}_{\gamma,R},
\tag{15.417}
```

where the commutator and chart remainder satisfies

```math
0
\le
\mathcal Q^{\mathrm{ren}}_{\gamma,R}
\le
C^{\mathrm{com}}_{\gamma}(R,\ell_R)
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|^4
+
C^{\mathrm{bad}}_{\gamma}(R,\ell_R)
\mathbf 1_{\mathcal B^{\mathrm{ren}}_{\gamma,R}} .
\tag{15.418}
```

Assume also the fourth-moment and bad-chart estimates

```math
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|^4
\mid
\xi_-
\right]
\le
C^{(4)}_{\gamma}(R)g_{\mathrm{eff}}^4(R)
+
o_a(1),
\tag{15.419}
```

and

```math
\mathsf K^s_{R,a,b}
\left[
\mathbf 1_{\mathcal B^{\mathrm{ren}}_{\gamma,R}}
\mid
\xi_-
\right]
\le
C^{\mathrm{bad}}_{\gamma}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.420}
```

Then the renormalized Stokes remainder estimate (15.399) holds.

#### Proof

Equation (15.417) is exactly (15.397) with a positive remainder after choosing

```math
C^{\mathrm{St},\mathrm{ren}}_{\gamma}
\ge
C^{\mathrm{flux}}_{\gamma}(R,\ell_R).
\tag{15.421}
```

The positive part of the remainder is bounded by the right side of (15.418).
Taking the conditional block expectation and applying (15.419)-(15.420) gives
(15.399), after absorbing the smaller fourth-order contribution into the
second-order budget for fixed small physical coupling. `∎`

This is a deterministic geometry task plus two moment estimates. It is not a
thin-plaquette regularity assumption.

#### 15.34.3. Conditional Poincare Route To The Flux Variance

The hard probabilistic estimate is (15.398). The cleanest route is a conditional
Poincare inequality for the exact fixed-center SO(3) block kernel.

Let

```math
\mathcal E^s_{R,a,b,\xi_-}(F,F)
:=
\mathsf K^s_{R,a,b}
\left[
\sum_{\ell\subset B_R}
\left|
\nabla_{\ell}F
\right|^2
\mid
\xi_-
\right]
\tag{15.422}
```

be the conditional Dirichlet form inside the physical block. The desired
Poincare estimate is

```math
\operatorname{Var}_{\mathsf K^s_{R,a,b}(\cdot\mid\xi_-)}(F)
\le
C_P(R,\ell_R)g_{\mathrm{eff}}^2(R)
\mathcal E^s_{R,a,b,\xi_-}(F,F)
+
o_a(1)
\tag{15.423}
```

for the finite list of observables generated by the renormalized disk fluxes
and their Stokes remainders.

This is the exact place where the center field enters. The estimate must hold
uniformly over admissible center fields and frontier-good incoming collars.

The second ingredient is a mean-flux bound:

```math
\left|
\mathsf K^s_{R,a,b}
\left[
\Phi^{\mathrm{ren}}_{\gamma,R}
\mid
\xi_-
\right]
\right|^2
\le
C^{\mathrm{mean}}_{\gamma}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.424}
```

Finally, the smoother must make the flux observable cutoff-uniformly Lipschitz:

```math
\sup_{a<a_0}
\sup_{b,\xi_-}
\mathcal E^s_{R,a,b,\xi_-}
\left(
\Phi^{\mathrm{ren}}_{\gamma,R},
\Phi^{\mathrm{ren}}_{\gamma,R}
\right)
\le
L_{\gamma}^{\mathrm{ren}}(R,\ell_R).
\tag{15.425}
```

**Criterion 40.80 (Conditional Poincare And Mean Flux Prove The Renormalized
Flux Variance).** If (15.423), (15.424), and (15.425) hold, then (15.398)
holds with

```math
C^{\Phi,\mathrm{ren}}_{\gamma}(R)
=
C_P(R,\ell_R)
L_{\gamma}^{\mathrm{ren}}(R,\ell_R)
+
C^{\mathrm{mean}}_{\gamma}(R).
\tag{15.426}
```

#### Proof

Decompose the second moment:

```math
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|^2
\mid
\xi_-
\right]
=
\operatorname{Var}_{\mathsf K^s_{R,a,b}(\cdot\mid\xi_-)}
\left(
\Phi^{\mathrm{ren}}_{\gamma,R}
\right)
+
\left|
\mathsf K^s_{R,a,b}
\left[
\Phi^{\mathrm{ren}}_{\gamma,R}
\mid
\xi_-
\right]
\right|^2 .
\tag{15.427}
```

Apply (15.423) to the variance term, then use (15.424) and (15.425). This gives
(15.398) with the constant (15.426). `∎`

The mean-flux term is essential. A Poincare inequality alone controls
fluctuations; it does not rule out a center-conditioned classical bias.

#### 15.34.4. The Fixed-IR Proof Package

Combining the deterministic Stokes criterion and the conditional Poincare
criterion gives the proof package for Target 40.75.

**Target 40.81 (Fixed-IR Flowed Block Package For Target 40.75).** Prove or
disprove the following cutoff-uniform estimates at fixed physical R and fixed
physical smoothing radius:

```math
\boxed{
\begin{array}{ll}
\mathrm{P1:}
&
\text{admissible smoother properties S1-S4,}\\[1mm]
\mathrm{P2:}
&
\text{flowed Stokes control }(15.417)\text{ and }(15.418),\\[1mm]
\mathrm{P3:}
&
\text{fourth-moment and bad-chart bounds }(15.419)\text{ and }(15.420),\\[1mm]
\mathrm{P4:}
&
\text{conditional Poincare estimate }(15.423),\\[1mm]
\mathrm{P5:}
&
\text{conditional mean-flux estimate }(15.424),\\[1mm]
\mathrm{P6:}
&
\text{renormalized flux Lipschitz estimate }(15.425).
\end{array}}
\tag{15.428}
```

If P1-P6 hold, then Criteria 40.79, 40.80, 40.77, and 40.76 prove Target
40.75. If, in addition, either bridge estimate (15.404) or (15.405) holds and
the budget (15.406) is below threshold, then the fixed-IR cocycle route remains
open.

The obstruction is now completely localized:

```math
\boxed{
\begin{array}{c}
\text{Can the exact fixed-center SO(3) block kernel satisfy}\\[1mm]
\text{a cutoff-uniform Poincare/mean-flux package}\\[1mm]
\text{for physical-resolution fluxes?}
\end{array}}
\tag{15.429}
```

This is the Feynman calculation: compute the conditional Dirichlet form, the
classical mean flux, and the response of the residual atlas error. It is also
the Einstein constraint: every object in (15.428) is defined at fixed physical
scale before the continuum limit is taken.

### 15.35. Working Target 40.82: Conditional Mean-Flux Bias

Searchable Target-40.82 work tag:

`V4P40-TARGET-4082-CONDITIONAL-MEAN-FLUX-BIAS`.

The estimate (15.424) is not a cosmetic add-on. It is the point at which the
fixed-center conditioning can insert a classical SO(3) bias into the smoothed
flux. Poincare estimates control fluctuations around the conditional mean; they
do not control the mean itself.

For each physical loop gamma, define the conditional mean flux

```math
M^{\mathrm{ren}}_{\gamma,R}(b,\xi_-)
:=
\mathsf K^s_{R,a,b}
\left[
\Phi^{\mathrm{ren}}_{\gamma,R}
\mid
\xi_-
\right].
\tag{15.430}
```

The required estimate is exactly

```math
\left|
M^{\mathrm{ren}}_{\gamma,R}(b,\xi_-)
\right|^2
\le
C^{\mathrm{mean}}_{\gamma}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1),
\tag{15.431}
```

uniformly over admissible center fields and frontier-good incoming collars.

#### 15.35.1. Why Poincare Alone Cannot Prove It

The following comparison theorem is the warning.

**Theorem 40.82 (Poincare Alone Does Not Bound The Conditional Mean).** There
are probability measures with the desired Poincare scaling but with a mean that
is order one.

#### Proof

Let

```math
d\mu_{g,m}(x)
=
\frac{1}{\sqrt{2\pi g^2}}
\exp
\left(
-
\frac{(x-m)^2}{2g^2}
\right)
dx .
\tag{15.432}
```

This measure satisfies the sharp Poincare inequality

```math
\operatorname{Var}_{\mu_{g,m}}(F)
\le
g^2
\int
\left|
F'(x)
\right|^2
d\mu_{g,m}(x).
\tag{15.433}
```

For the observable

```math
F(x)=x,
\tag{15.434}
```

the variance is order g squared, but the mean is

```math
\left|
\int x\,d\mu_{g,m}(x)
\right|^2
=
m^2 .
\tag{15.435}
```

If m is fixed while g tends to zero, (15.435) is not bounded by a constant times
g squared. Thus a Poincare estimate can be perfectly true while the mean-flux
bound fails. `∎`

This is not a Yang-Mills counterexample. It is the finite-dimensional reason
why (15.424) is logically independent from (15.423).

#### 15.35.2. The Symmetry Route

The cleanest way to prove (15.431) is an exact conditional symmetry.

**Lemma 40.83 (Flux-Flip Symmetry Kills The Mean).** Suppose there is a
measurable involution

```math
\mathcal J_{\gamma,R}
\tag{15.436}
```

on the fixed-center conditional block fiber such that

```math
\left(\mathcal J_{\gamma,R}\right)_*
\mathsf K^s_{R,a,b}(\cdot\mid\xi_-)
=
\mathsf K^s_{R,a,b}(\cdot\mid\xi_-),
\tag{15.437}
```

and

```math
\Phi^{\mathrm{ren}}_{\gamma,R}
\left(
\mathcal J_{\gamma,R}\bar V
\right)
=
-
\Phi^{\mathrm{ren}}_{\gamma,R}(\bar V).
\tag{15.438}
```

Then

```math
M^{\mathrm{ren}}_{\gamma,R}(b,\xi_-)
=
0.
\tag{15.439}
```

#### Proof

Use (15.437) to change variables by the involution and then use (15.438). This
gives

```math
M^{\mathrm{ren}}_{\gamma,R}(b,\xi_-)
=
-
M^{\mathrm{ren}}_{\gamma,R}(b,\xi_-).
\tag{15.440}
```

Hence the mean is zero. `∎`

This route is attractive but fragile. Fixed center fields, incoming collar data,
surface orientation, and section choices can all break the flux-flip symmetry.
When that happens, the mean has to be treated as a classical Dirichlet bias.

#### 15.35.3. Classical Bias Decomposition

Let

```math
\mathcal M^s_{R,a,b}(\xi_-)
\tag{15.441}
```

be the set of minimizers of the fixed-center block action over the interior and
outgoing collar variables, with incoming collar fixed to xi minus. Choose a
measurable minimizer

```math
\bar V_*=\bar V_*(b,\xi_-)
\in
\mathcal M^s_{R,a,b}(\xi_-).
\tag{15.442}
```

The classical flux bias is

```math
B^{\mathrm{cl}}_{\gamma,R}(b,\xi_-)
:=
\Phi^{\mathrm{ren}}_{\gamma,R}(\bar V_*).
\tag{15.443}
```

The mean-flux estimate follows from two smaller estimates:

```math
\left|
B^{\mathrm{cl}}_{\gamma,R}(b,\xi_-)
\right|^2
\le
C^{\mathrm{cl}}_{\gamma}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1),
\tag{15.444}
```

and

```math
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
-
B^{\mathrm{cl}}_{\gamma,R}(b,\xi_-)
\right|^2
\mid
\xi_-
\right]
\le
C^{\mathrm{fluc}}_{\gamma}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.445}
```

**Criterion 40.84 (Classical Neutrality Plus Centered Fluctuations Prove
Mean-Flux Control).** If (15.444) and (15.445) hold, then (15.431) holds with

```math
C^{\mathrm{mean}}_{\gamma}(R)
=
2C^{\mathrm{cl}}_{\gamma}(R)
+
2C^{\mathrm{fluc}}_{\gamma}(R).
\tag{15.446}
```

#### Proof

By the triangle inequality and Jensen's inequality,

```math
\left|
M^{\mathrm{ren}}_{\gamma,R}(b,\xi_-)
\right|^2
\le
2
\left|
B^{\mathrm{cl}}_{\gamma,R}(b,\xi_-)
\right|^2
+
2
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
-
B^{\mathrm{cl}}_{\gamma,R}(b,\xi_-)
\right|^2
\mid
\xi_-
\right].
\tag{15.447}
```

Insert (15.444) and (15.445). `∎`

The first estimate is the real neutrality condition. The second is a centered
soft-fluctuation estimate, and is the part that a Poincare or Brascamp-Lieb
argument can plausibly prove.

#### 15.35.4. Mean-Bias Tethering

If (15.444) fails, the route should not pretend that the failure is harmless.
It has found a new bad response sector: a center-conditioned classical SO(3)
flux bias.

For a physical threshold rho mean, define

```math
\mathcal E^{\mathrm{mean}}_{\gamma,R}
:=
\left\{
\left|
B^{\mathrm{cl}}_{\gamma,R}(b,\xi_-)
\right|
>
\rho_{\mathrm{mean}}
\right\}.
\tag{15.448}
```

The honest alternative is:

```math
\boxed{
\begin{array}{ll}
\text{neutrality route:}
&
\text{prove the classical bound }(15.444),\\[1mm]
\text{tether route:}
&
\text{add } \mathcal E^{\mathrm{mean}}_{\gamma,R}
\text{ to the bad response sectors and prove it is summable.}
\end{array}}
\tag{15.449}
```

The summability version is

```math
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\mathsf K^s_{R,a,b}
\left[
\mathcal E^{\mathrm{mean}}_{\gamma,R}
\mid
\xi_-
\right]
\le
p_{\mathrm{mean}}(R),
\tag{15.450}
```

with the polymer budget enlarged by

```math
p_{\mathrm{tot}}(R)
\longmapsto
p_{\mathrm{tot}}(R)+p_{\mathrm{mean}}(R).
\tag{15.451}
```

**Target 40.85 (Mean-Flux Neutrality Or Mean-Bias Tethering).** At fixed
physical R and fixed physical smoothing radius, prove one of the following.

PASS-A:

```math
\text{the symmetry route or the classical neutrality estimate proves }(15.431).
\tag{15.452}
```

PASS-B:

```math
\text{the mean-bias sector obeys }(15.450)
\text{ below the enlarged polymer threshold.}
\tag{15.453}
```

FAIL:

```math
\limsup_{a\downarrow0}
\sup_{b,\xi_-}
\left|
B^{\mathrm{cl}}_{\gamma,R}(b,\xi_-)
\right|
>
0
\tag{15.454}
```

along frontier-good data, while the corresponding mean-bias sectors are not
summable.

This is the exact fixed-IR status of the mean term. It is not solved by
Poincare. It is solved only by symmetry, by classical neutrality of the
fixed-center Dirichlet minimizer, or by proving that biased minimizers form a
summable tether sector.

### 15.36. Working Target 40.85: Source Response And The Bias Audit

Searchable Target-40.85 work tag:

`V4P40-TARGET-4085-SOURCE-RESPONSE-BIAS-AUDIT`.

Target 40.85 should be attacked by turning the mean flux into a derivative of
an exact finite-block free energy. This prevents the proof from hiding a
center-conditioned classical bias inside notation.

The fixed-IR order remains:

```math
R\text{ fixed},
\qquad
\ell_R\text{ fixed},
\qquad
a\downarrow0.
\tag{15.455}
```

#### 15.36.1. Source-Coupled Block Response

Let the source variable be

```math
J\in\mathfrak{so}(3)
\tag{15.456}
```

using the invariant inner product to identify the Lie algebra with its dual.
Define the source-coupled normalized block moment generating function by

```math
Z^{\Phi}_{\gamma,R}(J\mid b,\xi_-)
:=
\mathsf K^s_{R,a,b}
\left[
\exp
\left(
\left\langle
J,
\Phi^{\mathrm{ren}}_{\gamma,R}
\right\rangle
\right)
\mid
\xi_-
\right].
\tag{15.457}
```

Let

```math
\Psi^{\Phi}_{\gamma,R}(J\mid b,\xi_-)
:=
\log
Z^{\Phi}_{\gamma,R}(J\mid b,\xi_-).
\tag{15.458}
```

**Theorem 40.86 (Source Response Identity).** At every finite cutoff,

```math
\nabla_J
\Psi^{\Phi}_{\gamma,R}(0\mid b,\xi_-)
=
M^{\mathrm{ren}}_{\gamma,R}(b,\xi_-),
\tag{15.459}
```

and

```math
\nabla_J^2
\Psi^{\Phi}_{\gamma,R}(0\mid b,\xi_-)
=
\operatorname{Cov}_{\mathsf K^s_{R,a,b}(\cdot\mid\xi_-)}
\left(
\Phi^{\mathrm{ren}}_{\gamma,R},
\Phi^{\mathrm{ren}}_{\gamma,R}
\right).
\tag{15.460}
```

#### Proof

At finite cutoff the block configuration space is compact and the
physical-resolution flux is bounded. Differentiation under the integral in
(15.457) is therefore justified. The first derivative of the logarithm gives
the expectation of the flux. The second derivative gives its covariance. `∎`

Equation (15.460) is the source-response form of the Poincare story: Poincare
controls curvature of the source free energy. Equation (15.459) is the missing
anchor: the mean is the first derivative at the origin.

#### 15.36.2. Source Symmetry Criterion

An exact flux-flip symmetry is stronger than necessary. It is enough to prove
that the source free energy is almost even at the origin.

**Criterion 40.87 (Source Antisymmetry Proves Mean-Flux Control).** Suppose
that for every unit vector X in the Lie algebra,

```math
\limsup_{\lambda\downarrow0}
\frac{
\left|
\Psi^{\Phi}_{\gamma,R}(\lambda X\mid b,\xi_-)
-
\Psi^{\Phi}_{\gamma,R}(-\lambda X\mid b,\xi_-)
\right|
}{
2\lambda
}
\le
C^{\mathrm{sym}}_{\gamma}(R)g_{\mathrm{eff}}(R)
+
o_a(1),
\tag{15.461}
```

uniformly over admissible center fields and frontier-good incoming collars.
Then (15.431) holds with

```math
C^{\mathrm{mean}}_{\gamma}(R)
=
\left(
C^{\mathrm{sym}}_{\gamma}(R)
\right)^2.
\tag{15.462}
```

#### Proof

The directional derivative of (15.458) at the origin in the direction X is

```math
\left\langle
X,
M^{\mathrm{ren}}_{\gamma,R}(b,\xi_-)
\right\rangle .
\tag{15.463}
```

Taking the symmetric difference quotient and applying (15.461) bounds every
unit-direction component of the mean by the right side of (15.461). Taking the
supremum over X gives (15.431). `∎`

Thus one way to prove Target 40.85 is to prove an approximate source-evenness
identity. Exact flux flip gives this with zero right side.

#### 15.36.3. Classical Source Envelope

If source symmetry fails, the next object is the source-deformed classical
Dirichlet problem.

Let

```math
\mathcal F^s_{R,a}(b,\xi_-)
\tag{15.464}
```

be the fixed-center block fiber over the incoming collar, with outgoing collar
variables included. Let

```math
\mathcal A^s_{0,R,a}(\bar V\mid b,\xi_-)
\tag{15.465}
```

be the corresponding unsourced block action. Define

```math
\mathcal A^s_{J,R,a}(\bar V\mid b,\xi_-)
:=
\mathcal A^s_{0,R,a}(\bar V\mid b,\xi_-)
-
\left\langle
J,
\Phi^{\mathrm{ren}}_{\gamma,R}(\bar V)
\right\rangle .
\tag{15.466}
```

The classical source free energy is

```math
F^{\mathrm{cl}}_{\gamma,R}(J\mid b,\xi_-)
:=
\inf_{\bar V\in\mathcal F^s_{R,a}(b,\xi_-)}
\mathcal A^s_{J,R,a}(\bar V\mid b,\xi_-).
\tag{15.467}
```

Let the unsourced minimizer set be

```math
\mathcal M^s_{R,a,b}(\xi_-)
=
\operatorname*{arg\,min}_{\bar V\in\mathcal F^s_{R,a}(b,\xi_-)}
\mathcal A^s_{0,R,a}(\bar V\mid b,\xi_-).
\tag{15.468}
```

and define the minimizer-flux set

```math
\mathfrak B^{\mathrm{cl}}_{\gamma,R}(b,\xi_-)
:=
\left\{
\Phi^{\mathrm{ren}}_{\gamma,R}(\bar V_*):
\bar V_*\in\mathcal M^s_{R,a,b}(\xi_-)
\right\}.
\tag{15.469}
```

**Theorem 40.88 (Classical Envelope Identity).** If the unsourced minimizer is
unique modulo gauge and constraint zero modes, then

```math
\nabla_J
F^{\mathrm{cl}}_{\gamma,R}(0\mid b,\xi_-)
=
-
\Phi^{\mathrm{ren}}_{\gamma,R}(\bar V_*).
\tag{15.470}
```

If the minimizer is not unique, then the subdifferential satisfies

```math
\partial_J
F^{\mathrm{cl}}_{\gamma,R}(0\mid b,\xi_-)
\subset
-
\operatorname{conv}
\mathfrak B^{\mathrm{cl}}_{\gamma,R}(b,\xi_-).
\tag{15.471}
```

#### Proof

For fixed finite cutoff this is the envelope theorem for a compact
finite-dimensional minimization problem. In the unique-minimizer case,
differentiating the source-deformed action at the minimizing field gives
(15.470). In the nonunique case, directional derivatives are obtained by
minimizers that maximize or minimize the source pairing. Their closed convex
hull gives the subdifferential inclusion (15.471). `∎`

Therefore the classical bias is not mysterious. It is the first derivative of
the source-deformed Dirichlet minimum.

#### 15.36.4. Minimized Neutrality Criterion

The selection in (15.442) is a sufficient diagnostic, but the invariant object
is the whole minimizer-flux set. A choice-independent sufficient condition is:

```math
\sup_{u\in\operatorname{conv}\mathfrak B^{\mathrm{cl}}_{\gamma,R}(b,\xi_-)}
\left|u\right|^2
\le
C^{\mathrm{min}}_{\gamma}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.472}
```

**Criterion 40.89 (Minimizer Neutrality Proves Classical Neutrality).** If
(15.472) holds uniformly over admissible center fields and frontier-good
incoming collars, then the classical neutrality estimate (15.444) holds for any
measurable minimizer selection, with

```math
C^{\mathrm{cl}}_{\gamma}(R)
=
C^{\mathrm{min}}_{\gamma}(R).
\tag{15.473}
```

#### Proof

Every selected minimizer flux belongs to the set in (15.469), hence to its
convex hull. Apply (15.472). `∎`

This criterion is intentionally strong. It rules out even hidden minimizer
branches with order-one flux. A weaker route may suffice if the Laplace
weights of different minimizer branches cancel, but then that cancellation must
be proved as a source-free-energy statement using (15.457)-(15.461).

#### 15.36.5. Bias Classification

If minimizer neutrality fails, the next question is whether the bias is
tethered to already visible data. Define the center-tether region of the
physical disk as the event that the fixed center field is not a relative
coboundary in a physical neighborhood of the disk:

```math
\mathcal T^{\mathrm{cen}}_{\gamma,R}
:=
\left\{
b\vert_{\mathcal N_R(\Sigma_\gamma)}
\notin
\operatorname{im}
\left(
\delta:C^1_{\mathrm{rel}}\to C^2_{\mathrm{rel}}
\right)
\right\}.
\tag{15.474}
```

Define the coset-tether event by nontrivial incoming collar holonomy around the
same disk neighborhood:

```math
\mathcal T^{\mathrm{cos}}_{\gamma,R}
:=
\left\{
\mathfrak H_{\mathcal N_R(\Sigma_\gamma)}(\xi_-)
\ne
\{1\}
\right\}.
\tag{15.475}
```

For transfer estimates, expose the outgoing collar and use the two-sided
Dirichlet minimizer-flux set

```math
\mathfrak B^{\mathrm{cl},+}_{\gamma,R}(b,\xi_-,\xi_+)
:=
\left\{
\Phi^{\mathrm{ren}}_{\gamma,R}(\bar V_*):
\bar V_*\in
\mathcal M^s_{R,a,b}(\xi_-,\xi_+)
\right\}.
\tag{15.483}
```

The genuinely dangerous event is order-one classical bias without either
tether:

```math
\mathcal E^{\mathrm{bulkmean}}_{\gamma,R}(\xi_+)
:=
\left\{
\sup_{u\in\operatorname{conv}\mathfrak B^{\mathrm{cl},+}_{\gamma,R}(b,\xi_-,\xi_+)}
\left|u\right|
>
\rho_{\mathrm{mean}}
\right\}
\cap
\left(
\mathcal T^{\mathrm{cen}}_{\gamma,R}
\cup
\mathcal T^{\mathrm{cos}}_{\gamma,R}
\right)^c .
\tag{15.476}
```

The center-tether definition must be read relatively: a local center coboundary
is not a bulk obstruction, because it can be absorbed into the center-adapted
Dirichlet variables. A nontrivial relative class is a tether.

**Criterion 40.90 (Bias Tethering Saves The Mean Route).** Suppose the
center-tether and coset-tether sectors are already included in the bad-response
polymer budget. Suppose also that

```math
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\mathsf K^s_{R,a,b}
\left[
\mathbf 1_{\mathcal E^{\mathrm{bulkmean}}_{\gamma,R}(\xi_+)}
\mid
\xi_-
\right]
\le
p_{\mathrm{bulkmean}}(R),
\tag{15.477}
```

with the enlarged budget

```math
p_{\mathrm{tot}}(R)
\longmapsto
p_{\mathrm{tot}}(R)+p_{\mathrm{bulkmean}}(R)
\tag{15.478}
```

still below the polymer threshold. Then the mean-bias failure is summably
tethered and Target 40.85 satisfies PASS-B.

#### Proof

On the complement of the tether events and the bulk-mean event, the classical
minimizer flux is below the physical threshold by definition. The tether events
are charged to the existing center and coset bad-response sectors. The remaining
bulk-mean event is charged by (15.477). The enlarged budget (15.478) is exactly
the bad-transfer density budget used in Criteria 40.46 and 40.48. `∎`

#### 15.36.6. The Exact Next Test

The next fixed-IR theorem to prove or falsify is now:

**Target 40.91 (Source-Minimizer Test For Mean-Flux Bias).** At fixed physical
R and fixed physical smoothing radius, prove one of the following alternatives.

PASS-A:

```math
\text{source antisymmetry }(15.461)\text{ holds.}
\tag{15.479}
```

PASS-B:

```math
\text{minimizer neutrality }(15.472)\text{ and centered fluctuations hold.}
\tag{15.480}
```

PASS-C:

```math
\text{bulk mean-bias sectors obey }(15.477)
\text{ below the enlarged polymer threshold.}
\tag{15.481}
```

FAIL:

```math
\limsup_{a\downarrow0}
\sup_{\substack{
b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}\\
\xi_-\in\mathcal A_{\mathrm{good}}\\
\left(\mathcal T^{\mathrm{cen}}_{\gamma,R}
\cup
\mathcal T^{\mathrm{cos}}_{\gamma,R}\right)^c}}
\mathsf K^s_{R,a,b}
\left[
\mathbf 1_{\mathcal E^{\mathrm{bulkmean}}_{\gamma,R}(\xi_+)}
\mid
\xi_-
\right]
>
0,
\tag{15.482}
```

and the corresponding bulk mean-bias event is not summable.

This is the precise Feynman calculation for Target 40.85: add a source, compute
the derivative of the exact block free energy, compute the derivative of the
classical Dirichlet minimum, and check whether any order-one minimizer flux is
tethered. It is also the Einstein invariant form: the question is about a
physical-resolution SO(3) flux at fixed physical scale, not about microscopic
plaquette regularity.

### 15.37. Working Target 40.91: Tether-Free Minimizer Neutrality

Searchable Target-40.91 work tag:

`V4P40-TARGET-4091-TETHER-FREE-MINIMIZER-NEUTRALITY`.

We now attack the PASS-B line of Target 40.91. The goal is not to show that
every frontier-good collar produces a small mean flux. That would be too strong.
A collar can be inside the chart but still carry a fixed physical holonomy that
forces a fixed physical curvature response. The correct claim is:

```math
\boxed{
\begin{array}{c}
\text{exactly tether-free data give zero classical mean flux;}\\[1mm]
\text{quantitatively small tether data give small classical mean flux;}\\[1mm]
\text{fixed-size tether data must be charged as a bad response sector.}
\end{array}}
\tag{15.484}
```

This is the fixed-IR version. The threshold for a tolerated mean bias must scale
with the physical coupling target, not merely with the chart radius.

#### 15.37.1. The Tether-Free Dirichlet Sector

Let

```math
\mathcal N_{\gamma,R}
\tag{15.485}
```

be the physical neighborhood of the disk used in the renormalized flux
observable. Say that the two-sided Dirichlet data are exactly mean-neutral if
the following two conditions hold.

First, the center field is a relative coboundary in the disk neighborhood:

```math
b\vert_{\mathcal N_{\gamma,R}}
=
\delta\zeta,
\qquad
\zeta\vert_{\partial\mathcal N_{\gamma,R}}=1.
\tag{15.486}
```

Second, after the center-adapted lift by zeta, the incoming and outgoing collar
SO(3) data admit a source-relevant flat filling. Write

```math
\mathfrak P^s_{\zeta,p}(\bar V)
\tag{15.487}
```

for the SU(2) plaquette argument after the local center coboundary has been
absorbed. The condition is that there exists

```math
\bar V^{\mathrm{flat}}
\in
\mathcal F^s_{R,a}(b,\xi_-,\xi_+),
\qquad
\mathfrak P^s_{\zeta,p}
\left(
\bar V^{\mathrm{flat}}
\right)
=
1
\text{ for every }p\in P_{R,a},
\tag{15.488}
```

and, in particular,

```math
\bar V^{\mathrm{flat}}_p=1
\text{ for every }p\subset\mathcal N_{\gamma,R}.
\tag{15.489}
```

The phrase center-adapted is important. If the local center field is a coboundary,
one first absorbs it into link-center coordinates; the remaining SO(3) plaquette
curvature is the physical coset curvature. The central sign itself is not an
SO(3) curvature.

**Theorem 40.92 (Exact Tether-Free Minimizers Have Zero Renormalized Flux).**
Assume the heat-kernel action is minimized plaquettewise exactly when the
center-adapted SU(2) plaquette argument is the identity. If the two-sided
Dirichlet data satisfy (15.486)-(15.489), then every global Dirichlet minimizer
has zero SO(3) curvature on the disk neighborhood. Consequently

```math
\mathfrak B^{\mathrm{cl},+}_{\gamma,R}(b,\xi_-,\xi_+)
=
\{0\}.
\tag{15.490}
```

#### Proof

The field in (15.488) is admissible in the fixed-center Dirichlet fiber. In the
center-adapted lift, every plaquette in the source-relevant block action has
SU(2) plaquette argument equal to the identity. Therefore it attains the
plaquettewise minimum of the full source-relevant action.

Since the full block action is a sum of nonnegative plaquette contributions
after subtracting the common minimum, no global minimizer can have larger action
on any source-relevant plaquette while still matching the same tether-free
collar data. Thus every global minimizer also attains the plaquettewise minimum
on the disk neighborhood. Its SO(3) plaquette curvature is therefore trivial
there.

The smoothing map is gauge-covariant and center-blind after passage to SO(3).
Applied to a flat SO(3) connection on the disk neighborhood, it leaves the
renormalized disk flux equal to zero. Hence the minimizer-flux set is (15.490).
`∎`

**Corollary 40.93 (Exact Tether-Free PASS-B).** On the exactly mean-neutral
sector (15.486)-(15.489), the minimizer neutrality estimate (15.472) holds with

```math
C^{\mathrm{min}}_{\gamma}(R)=0.
\tag{15.491}
```

#### Proof

Equation (15.490) gives a singleton minimizer-flux set equal to zero, so its
convex hull has norm zero. `∎`

This proves PASS-B only on the exact tether-free sector. The next issue is the
one that matters for fixed physical IR: exact triviality is too rigid, while a
fixed chart threshold is too loose.

#### 15.37.2. Quantitative Tether Size

Define a quantitative mean-tether size by

```math
\tau^{\mathrm{mean}}_{\gamma,R}(b,\xi_-,\xi_+)
:=
\mathbf 1_{\mathcal T^{\mathrm{cen}}_{\gamma,R}}
+
\mathfrak h_{\gamma,R}^{\mathrm{cos}}(\xi_-,\xi_+),
\tag{15.492}
```

where the coset collar size is the maximal SO(3) distance of the relevant collar
loop holonomies from the identity:

```math
\mathfrak h_{\gamma,R}^{\mathrm{cos}}(\xi_-,\xi_+)
:=
\max_{\alpha\in\mathcal B_{\gamma,R}^{\mathrm{collar}}}
d_{SO(3)}
\left(
\operatorname{Hol}_{\alpha}(\xi_-,\xi_+),
1
\right).
\tag{15.493}
```

The fixed-IR neutrality estimate needs the stronger, coupling-scaled good event

```math
\mathcal G^{\mathrm{mean}}_{\gamma,R}
:=
\left\{
\tau^{\mathrm{mean}}_{\gamma,R}(b,\xi_-,\xi_+)
\le
c_{\mathrm{mean}}g_{\mathrm{eff}}(R)
\right\}.
\tag{15.494}
```

This is not a UV condition. It is a physical block condition: the collar
holonomies and relative center obstruction are measured at fixed physical
resolution.

#### 15.37.3. Local Convexity Implies Quantitative Neutrality

The deterministic estimate one wants is a stability theorem for the
center-adapted Dirichlet minimizer.

**Criterion 40.94 (Small Tether Gives Small Classical Bias).** Suppose that in
the sector where the center field is a relative coboundary, the center-adapted
Dirichlet action is uniformly coercive around the flat minimizer modulo gauge
and constraint zero modes. Concretely, suppose there are cutoff-independent
constants such that every two-sided minimizer satisfies

```math
\sup_{u\in\operatorname{conv}\mathfrak B^{\mathrm{cl},+}_{\gamma,R}(b,\xi_-,\xi_+)}
\left|u\right|
\le
C_{\gamma}^{\mathrm{stab}}(R)
\mathfrak h_{\gamma,R}^{\mathrm{cos}}(\xi_-,\xi_+)
+
o_a(1).
\tag{15.495}
```

Then on the event (15.494), the minimizer neutrality estimate holds with

```math
C^{\mathrm{min}}_{\gamma}(R)
=
\left(
C_{\gamma}^{\mathrm{stab}}(R)c_{\mathrm{mean}}
\right)^2.
\tag{15.496}
```

#### Proof

On the event (15.494), the center-tether indicator is zero for all sufficiently
small right side, and the coset collar size is bounded by
c_mean times g_eff(R). Insert this bound into (15.495), square the result, and
absorb the cutoff error. `∎`

The actual proof of (15.495) is a finite-dimensional elliptic estimate for the
source-free Dirichlet Euler equation in a center-adapted chart. In gauge-fixed
coordinates it has the schematic form

```math
L_{R,a}A_*
=
\operatorname{boundary}(\xi_-,\xi_+)
+
\operatorname{higher}(A_*),
\tag{15.497}
```

where the inverse of the reduced operator is required to be bounded at fixed
physical R after the cutoff is removed:

```math
\left\|
L_{R,a}^{-1}
\right\|_{\mathrm{red}}
\le
C_R .
\tag{15.498}
```

Equations (15.497)-(15.498) are the concrete Feynman computation behind
Criterion 40.94.

#### 15.37.4. Fixed Chart Goodness Is Not Enough

The previous criterion also explains why the old frontier-good condition cannot
prove PASS-B by itself.

**Theorem 40.95 (Fixed-Size Collar Holonomy Can Force Fixed Mean Bias).** If the
incoming or outgoing collar is allowed to carry a fixed physical holonomy

```math
d_{SO(3)}
\left(
\operatorname{Hol}_{\alpha}(\xi_-,\xi_+),
1
\right)
=
\rho_0
\tag{15.499}
```

with rho_0 independent of g_eff(R), then minimizer neutrality of order
g_eff(R) need not hold.

#### Proof

Work in an abelian SO(3) subgroup and take a disk whose collar loop alpha is the
boundary of the disk. Choose collar data with holonomy (15.499), and choose the
center field to be a relative coboundary. Any filling of the collar must have
total SO(3) curvature flux equal to the boundary holonomy modulo commutator
terms. In the abelian example there are no commutator terms, so every admissible
Dirichlet minimizer has disk flux of size rho_0. Thus

```math
\sup_{u\in\operatorname{conv}\mathfrak B^{\mathrm{cl},+}_{\gamma,R}}
\left|u\right|^2
\ge
c\,\rho_0^2.
\tag{15.500}
```

If g_eff(R) is chosen small while rho_0 is fixed, (15.500) cannot be bounded by
a constant times g_eff squared. `∎`

This does not falsify the route. It says that fixed-size collar holonomy is a
coset tether and must be charged to the bad-response budget. It cannot be
silently included in the mean-neutral sector.

#### 15.37.5. Corrected PASS-B For Target 40.91

The PASS-B line should therefore be read as the following sharpened target.

**Target 40.96 (Quantitative Tether-Free PASS-B).** At fixed physical R and
fixed physical smoothing radius, prove both estimates below.

First, the small-tether minimizer stability estimate:

```math
\sup_{u\in\operatorname{conv}\mathfrak B^{\mathrm{cl},+}_{\gamma,R}(b,\xi_-,\xi_+)}
\left|u\right|
\le
C_{\gamma}^{\mathrm{stab}}(R)
\mathfrak h_{\gamma,R}^{\mathrm{cos}}(\xi_-,\xi_+)
+
o_a(1)
\tag{15.501}
```

on relative-center-coboundary data.

Second, the complement of the coupling-scaled mean-good event is a summable
bad-response sector:

```math
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\mathsf K^s_{R,a,b}
\left[
\mathbf 1_{\left(\mathcal G^{\mathrm{mean}}_{\gamma,R}\right)^c}
\mid
\xi_-
\right]
\le
p_{\mathrm{meantether}}(R),
\tag{15.502}
```

with the enlarged polymer budget still subcritical.

If (15.501)-(15.502) hold, then Target 40.91 satisfies PASS-B or PASS-C
depending on whether the data lie inside or outside the small-tether event.
If (15.501) fails in the small-tether sector, the mean-bias obstruction is a
genuine untethered SO(3) Dirichlet response and the route fails at Target 40.91.

### 15.38. Working Target 40.96: Center-Routed Mean Tethers

Searchable Target-40.96 refinement tag:

`V4P40-TARGET-4096-CENTER-ROUTED-MEAN-TETHERS`.

Target 40.96 still overcharges one sector. A center tether near the Wilson sheet
is not automatically a bad response. It may be the center disorder that the
Wilson route is supposed to keep. The mean-bias split must therefore be:

```math
\boxed{
\begin{array}{c}
\text{mean-good failure}\\[1mm]
\subset\\[1mm]
\text{center tether routed into the center sheet}\\[1mm]
\cup\ \text{large coset tether}\\[1mm]
\cup\ \text{untethered bulk mean bias.}
\end{array}}
\tag{15.503}
```

Only the last two are charged to the noncenter bad-response budget. The first
one must be carried by the center variable already present in the Wilson-sheet
factor.

#### 15.38.1. Center-Routed Mean-Good Event

Define the coset-only mean-good event

```math
\mathcal G^{\mathrm{cosmean}}_{\gamma,R}
:=
\left\{
\mathfrak h_{\gamma,R}^{\mathrm{cos}}(\xi_-,\xi_+)
\le
c_{\mathrm{mean}}g_{\mathrm{eff}}(R)
\right\}.
\tag{15.504}
```

On the relative-center-coboundary sector, (15.504) is the small-tether event
needed by Criterion 40.94. On the nontrivial relative-center sector, the center
class is routed into the center sheet:

```math
\mathcal T^{\mathrm{cen}}_{\gamma,R}
\quad
\leadsto
\quad
\Xi_S(b)
\text{ and the center-disorder estimate.}
\tag{15.505}
```

The corrected bad event is therefore

```math
\mathcal E^{\mathrm{meancos}}_{\gamma,R}(\xi_+)
:=
\left(
\mathcal G^{\mathrm{cosmean}}_{\gamma,R}
\right)^c
\cap
\left(
\mathcal T^{\mathrm{cen}}_{\gamma,R}
\right)^c ,
\tag{15.506}
```

plus the untethered bulk mean event

```math
\mathcal E^{\mathrm{bulkmean,0}}_{\gamma,R}(\xi_+)
:=
\mathcal E^{\mathrm{bulkmean}}_{\gamma,R}(\xi_+)
\cap
\left(
\mathcal T^{\mathrm{cen}}_{\gamma,R}
\cup
\mathcal T^{\mathrm{cos}}_{\gamma,R}
\right)^c .
\tag{15.507}
```

This is the corrected invariant split: center topology is not suppressed as a
coset defect.

#### 15.38.2. Coset-Tether Probability From Adjoint Moments

The large coset-tether event is controlled by the same finite physical adjoint
collar moments used earlier. For the collar loop family

```math
\mathcal B_{\gamma,R}^{\mathrm{collar}},
\tag{15.508}
```

define

```math
\Delta_{\mathrm{cosmean}}(R)
:=
\sup_{\alpha\in\mathcal B_{\gamma,R}^{\mathrm{collar}}}
\left[
1
-
\frac{1}{3}
\mathsf K^s_{R,a,b}
\left(
\chi_{\mathrm{ad}}
\left(
\operatorname{Hol}_{\alpha}(\xi_-,\xi_+)
\right)
\mid
\xi_-
\right)
\right].
\tag{15.509}
```

For small enough angle rho, the adjoint character defect obeys

```math
d_{SO(3)}(h,1)>\rho
\quad\Longrightarrow\quad
1-\frac{1}{3}\chi_{\mathrm{ad}}(h)
\ge
c_{\mathrm{ad}}\rho^2 .
\tag{15.510}
```

**Criterion 40.97 (Adjoint Collar Moments Control Large Coset Mean Tethers).**
If

```math
\Delta_{\mathrm{cosmean}}(R)
\le
C_{\mathrm{cosmean}}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1),
\tag{15.511}
```

then

```math
\mathsf K^s_{R,a,b}
\left[
\mathbf 1_{\mathcal E^{\mathrm{meancos}}_{\gamma,R}(\xi_+)}
\mid
\xi_-
\right]
\le
\frac{
|\mathcal B_{\gamma,R}^{\mathrm{collar}}|
C_{\mathrm{cosmean}}(R)
}{
c_{\mathrm{ad}}c_{\mathrm{mean}}^2
}
+
o_a(1).
\tag{15.512}
```

#### Proof

If (15.504) fails, then some collar loop alpha has

```math
d_{SO(3)}
\left(
\operatorname{Hol}_{\alpha}(\xi_-,\xi_+),
1
\right)
>
c_{\mathrm{mean}}g_{\mathrm{eff}}(R).
\tag{15.513}
```

Apply (15.510) with rho equal to the right side of (15.513), take the
conditional expectation, and sum over the finite collar loop family. The
relative-center factor can only reduce the event after intersection with the
complement of the center-tether sector, so the same upper bound applies to
(15.506). `∎`

The tradeoff is visible:

```math
\boxed{
\begin{array}{c}
c_{\mathrm{mean}}\text{ large makes large coset tethers rare,}\\[1mm]
c_{\mathrm{mean}}\text{ large also worsens the mean-bound constant}\\[1mm]
C^{\mathrm{min}}_{\gamma}(R)
=
\left(
C_{\gamma}^{\mathrm{stab}}(R)c_{\mathrm{mean}}
\right)^2.
\end{array}}
\tag{15.514}
```

This is acceptable only if R can be chosen small enough that the final
mean-flux contribution remains below the live budget.

#### 15.38.3. Untethered Bulk Mean Bias

The remaining event is the dangerous one. It is not center topology and not
coset boundary holonomy:

```math
\mathcal E^{\mathrm{bulkmean,0}}_{\gamma,R}(\xi_+).
\tag{15.515}
```

The required estimate is

```math
\sup_{a<a_0}
\sup_{b\in\operatorname{supp}\mu^s_{\mathrm{cen},a}}
\sup_{\xi_-\in\mathcal A_{\mathrm{good}}}
\mathsf K^s_{R,a,b}
\left[
\mathbf 1_{\mathcal E^{\mathrm{bulkmean,0}}_{\gamma,R}(\xi_+)}
\mid
\xi_-
\right]
\le
p_{\mathrm{bulkmean,0}}(R).
\tag{15.516}
```

If the deterministic stability estimate (15.501) holds on the relative
center-coboundary sector, then the event in (15.515) is empty for small enough
cutoff and sufficiently small threshold margin:

```math
p_{\mathrm{bulkmean,0}}(R)=0.
\tag{15.517}
```

If (15.516) fails with a positive lower bound, then Target 40.91 fails through a
specific channel: untethered SO(3) Dirichlet minimizers with order-one physical
flux.

#### 15.38.4. Corrected Target 40.96

**Target 40.98 (Center-Routed Quantitative PASS-B/C).** At fixed physical R and
fixed physical smoothing radius, prove the following.

First, prove small-coset-tether minimizer stability on the relative-center
coboundary sector:

```math
\sup_{u\in\operatorname{conv}\mathfrak B^{\mathrm{cl},+}_{\gamma,R}(b,\xi_-,\xi_+)}
\left|u\right|
\le
C_{\gamma}^{\mathrm{stab}}(R)
\mathfrak h_{\gamma,R}^{\mathrm{cos}}(\xi_-,\xi_+)
+
o_a(1).
\tag{15.518}
```

Second, prove the adjoint collar moment estimate (15.511). Third, prove the
untethered bulk mean estimate (15.516), or show it is empty by (15.518).

If these hold and the budget

```math
\frac{
|\mathcal B_{\gamma,R}^{\mathrm{collar}}|
C_{\mathrm{cosmean}}(R)
}{
c_{\mathrm{ad}}c_{\mathrm{mean}}^2
}
+
p_{\mathrm{bulkmean,0}}(R)
<
\Theta_{\mathrm{mean}}
\tag{15.519}
```

is compatible with the live polymer threshold, then Target 40.91 satisfies the
corrected PASS-B/C alternative. Center tethers are not included in (15.519);
they are routed through the center-sheet disorder channel.

The next actual proof is now sharply isolated:

```math
\boxed{
\begin{array}{c}
\text{prove the fixed-IR Dirichlet stability estimate }(15.518),\\[1mm]
\text{prove the adjoint collar moment estimate }(15.511),\\[1mm]
\text{and verify that center tethers are routed into the center sheet}\\[1mm]
\text{rather than counted as coset bad response.}
\end{array}}
\tag{15.520}
```

### 15.39. Working Target 40.98: Fixed-IR Dirichlet Stability

Searchable Target-40.98 stability tag:

`V4P40-TARGET-4098-FIXED-IR-DIRICHLET-STABILITY`.

The first line of Target 40.98 is deterministic. Once the relative center
coboundary has been absorbed, the problem is an SO(3) Dirichlet minimizer with
small coset collar holonomy. The estimate to prove is:

```math
\sup_{u\in\operatorname{conv}\mathfrak B^{\mathrm{cl},+}_{\gamma,R}(b,\xi_-,\xi_+)}
\left|u\right|
\le
C_{\gamma}^{\mathrm{stab}}(R)
\mathfrak h_{\gamma,R}^{\mathrm{cos}}(\xi_-,\xi_+)
+
o_a(1).
\tag{15.521}
```

This section reduces (15.521) to a fixed-physical Dirichlet elliptic estimate.

#### 15.39.1. Homogenized Center-Adapted Variables

Work on the relative-center-coboundary sector:

```math
b\vert_{\mathcal N_{\gamma,R}}
=
\delta\zeta,
\qquad
\zeta\vert_{\partial\mathcal N_{\gamma,R}}=1.
\tag{15.522}
```

Absorb zeta into the center-adapted link coordinates. In a gauge-fixed chart
around the flat filling, write every admissible two-sided Dirichlet field as

```math
A
=
E_{\xi}
+
u,
\qquad
u\vert_{\partial}=0,
\qquad
d^*u=0.
\tag{15.523}
```

Here E_xi is a chosen center-adapted extension of the incoming and outgoing
collar data, and u is the zero-boundary reduced variable. Use a fixed physical
lattice Sobolev norm

```math
\left\|A\right\|_{1,R,a}^2
:=
\sum_{p\subset B_R(a)}
a^4
\left|
d_aA(p)
\right|^2
+
R^{-2}
\sum_{\ell\subset B_R(a)}
a^4
\left|
A_{\ell}
\right|^2 .
\tag{15.524}
```

The first deterministic input is the collar extension estimate:

```math
\left\|E_{\xi}\right\|_{1,R,a}
\le
C_{\mathrm{ext}}(R)
\mathfrak h_{\gamma,R}^{\mathrm{cos}}(\xi_-,\xi_+)
+
o_a(1).
\tag{15.525}
```

This is a fixed-physical statement. The collar loop family is finite at scale R;
the constant is allowed to depend on the block shape and R, but not on the
cutoff.

#### 15.39.2. Reduced Coercivity Package

Let

```math
\mathcal S_{R,a}(A\mid b,\xi_-,\xi_+)
\tag{15.526}
```

be the center-adapted normalized Dirichlet action after subtracting the common
plaquette minimum and removing the irrelevant heat-kernel prefactor. The
minimizer is unchanged by this normalization.

The required fixed-IR coercivity package is:

```math
\left\langle
D\mathcal S_{R,a}(E_{\xi}+u)
-
D\mathcal S_{R,a}(E_{\xi}),
u
\right\rangle
\ge
\lambda_R
\left\|u\right\|_{1,R,a}^2
\tag{15.527}
```

for all reduced zero-boundary u in the small physical chart, and

```math
\left\|
D\mathcal S_{R,a}(E_{\xi})
\right\|_{-1,R,a}
\le
C_{\mathrm{grad}}(R)
\left\|E_{\xi}\right\|_{1,R,a}
+
o_a(1).
\tag{15.528}
```

The dual norm in (15.528) is dual to the norm in (15.524) on the reduced
zero-boundary space. Equation (15.527) is the reduced Dirichlet Poincare or
elliptic estimate. The gauge and constraint zero modes must already be removed.

Finally, the renormalized flux must be Lipschitz in this physical norm:

```math
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}(A)
-
\Phi^{\mathrm{ren}}_{\gamma,R}(0)
\right|
\le
C_{\Phi}(R,\ell_R)
\left\|A\right\|_{1,R,a}
+
o_a(1).
\tag{15.529}
```

Since the flat field has zero renormalized flux,

```math
\Phi^{\mathrm{ren}}_{\gamma,R}(0)=0.
\tag{15.530}
```

#### 15.39.3. Stability Theorem

**Criterion 40.99 (Reduced Dirichlet Coercivity Proves (15.518)).** Suppose
(15.525), (15.527), (15.528), and (15.529) hold uniformly as the cutoff is
removed. Then (15.521) holds with

```math
C_{\gamma}^{\mathrm{stab}}(R)
=
C_{\Phi}(R,\ell_R)
\left(
1+
\frac{C_{\mathrm{grad}}(R)}{\lambda_R}
\right)
C_{\mathrm{ext}}(R).
\tag{15.531}
```

#### Proof

Let

```math
A_*
=
E_{\xi}+u_*
\tag{15.532}
```

be a center-adapted Dirichlet minimizer in the reduced chart. Since u_star is a
valid zero-boundary variation around the minimizer,

```math
\left\langle
D\mathcal S_{R,a}(E_{\xi}+u_*),
u_*
\right\rangle
=
0.
\tag{15.533}
```

Apply (15.527) with u equal to u_star and use (15.533):

```math
\lambda_R
\left\|u_*\right\|_{1,R,a}^2
\le
-
\left\langle
D\mathcal S_{R,a}(E_{\xi}),
u_*
\right\rangle .
\tag{15.534}
```

By duality and (15.528),

```math
\left\|u_*\right\|_{1,R,a}
\le
\frac{C_{\mathrm{grad}}(R)}{\lambda_R}
\left\|E_{\xi}\right\|_{1,R,a}
+
o_a(1).
\tag{15.535}
```

Therefore

```math
\left\|A_*\right\|_{1,R,a}
\le
\left(
1+
\frac{C_{\mathrm{grad}}(R)}{\lambda_R}
\right)
\left\|E_{\xi}\right\|_{1,R,a}
+
o_a(1).
\tag{15.536}
```

Use the extension estimate (15.525), then apply the flux Lipschitz bound
(15.529)-(15.530). This gives (15.521) with the constant (15.531). Since the
argument applies to every minimizer, it also applies to the convex hull of the
minimizer-flux set. `∎`

This is the precise Feynman computation behind (15.518): construct the
center-adapted boundary extension, prove reduced coercivity, and compute the
flux Lipschitz constant after physical smoothing.

#### 15.39.4. Why Coercivity Is Necessary

The reduced coercivity estimate is not decorative. Without it, small coset
collar holonomy can be amplified by a soft SO(3) Dirichlet mode.

Let the linearized reduced Euler equation be written schematically as

```math
L_{R,a}u
=
f_{\xi}
+
\operatorname{higher}(u),
\tag{15.537}
```

where

```math
\left\|f_{\xi}\right\|_{-1,R,a}
\le
C_f(R)
\mathfrak h_{\gamma,R}^{\mathrm{cos}}(\xi_-,\xi_+).
\tag{15.538}
```

The low-mode obstruction is:

```math
\sup_{a<a_0}
\left\|
\Phi^{\mathrm{ren}}_{\gamma,R}
L_{R,a}^{-1}
\right\|_{-1\to\mathfrak{so}(3)}
<
\infty .
\tag{15.539}
```

**Criterion 40.100 (Low-Mode Test For Failure Of Dirichlet Stability).** If
(15.539) fails along a cutoff sequence, then the stability estimate (15.521) is
not available by the Dirichlet-minimizer route. More concretely, if there are
reduced forcing covectors f_a with unit dual norm such that

```math
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
L_{R,a}^{-1}f_a
\right|
\longrightarrow
\infty,
\tag{15.540}
```

then one can choose small coset collar data whose linearized minimizer response
violates any cutoff-uniform constant in (15.521), unless nonlinear effects
remove that response before it reaches the physical chart.

#### Proof

Choose collar data with forcing proportional to f_a and with coset size
epsilon_a. The linearized solution has flux response

```math
\epsilon_a
\Phi^{\mathrm{ren}}_{\gamma,R}
L_{R,a}^{-1}f_a .
\tag{15.541}
```

If the operator norm in (15.540) diverges, choose epsilon_a tending to zero
slowly enough that the solution stays inside the chart but the ratio of flux
response to epsilon_a diverges. This contradicts a cutoff-uniform estimate of
the form (15.521), unless the nonlinear terms invalidate the linearized branch
before that scale. `∎`

Thus the fixed-IR burden is exactly:

```math
\boxed{
\begin{array}{c}
\text{prove a reduced Dirichlet elliptic estimate at fixed physical }R,\\[1mm]
\text{or exhibit a reduced low mode with nonzero renormalized flux response.}
\end{array}}
\tag{15.542}
```

This is narrower than a mass-gap theorem. It is a local two-sided Dirichlet
stability theorem for physical-resolution fluxes in the relative-center
coboundary sector.

### 15.40. Working Target 40.98: Coercivity Or Flux-Visible Low Modes

Searchable Target-40.98 coercivity tag:

`V4P40-TARGET-4098-COERCIVITY-OR-FLUX-LOW-MODES`.

The reduced coercivity estimate (15.527) is the strongest clean route to
Dirichlet stability. It can itself be reduced to three deterministic inputs:

```math
\boxed{
\begin{array}{c}
\text{discrete reduced Hodge control,}\\[1mm]
\text{local convexity of the center-adapted plaquette action,}\\[1mm]
\text{and a small-chart bootstrap for the Dirichlet minimizer.}
\end{array}}
\tag{15.543}
```

This section records that reduction and the exact failure mode.

#### 15.40.1. Reduced Hodge Control

For a plaquette two-cochain F, set

```math
\left\|F\right\|_{0,R,a}^2
:=
\sum_{p\subset B_R(a)}
a^4
\left|
F_p
\right|^2 .
\tag{15.544}
```

The reduced Hodge estimate needed on zero-boundary, gauge-fixed one-cochains is

```math
\left\|u\right\|_{1,R,a}^2
\le
C_{\mathrm{Hdg}}(R)
\left\|
d_a u
\right\|_{0,R,a}^2 .
\tag{15.545}
```

This estimate is false if relative harmonic one-forms remain in the reduced
space. Those modes are precisely coset-tether modes. Thus the strong
coercivity route assumes

```math
H^1_{\mathrm{rel}}(B_R;\mathfrak{so}(3))=0
\tag{15.546}
```

after the collar/tether sectors have been removed.

**Criterion 40.101 (Reduced Hodge Control Is The Topological Part Of
Coercivity).** If the block-with-collar reduced complex has no relative harmonic
one-forms and the lattice discretization is a shape-regular refinement of the
fixed physical block, then the desired fixed-IR Hodge input is exactly the
cutoff-uniform estimate (15.545). If (15.545) fails, the failure mode is a
relative low mode and must be treated as a coset tether or as a flux-visible
low-mode obstruction.

This criterion is deliberately stated as the needed input rather than as a
global theorem about all block shapes. In nontrivial collar topology, (15.546)
is the condition that prevents flat SO(3) holonomy from masquerading as a soft
bulk fluctuation.

#### 15.40.2. Local Plaquette Convexity

In the center-adapted chart, write the normalized plaquette action as

```math
\mathcal S_{R,a}(A)
=
\sum_{p\subset B_R(a)}
\sigma
\left(
\mathfrak P^s_{\zeta,p}(A)
\right),
\tag{15.547}
```

where the plaquette argument equals the identity at the flat filling. The local
convexity input is:

```math
\left\langle
D\mathcal S_{R,a}(E_{\xi}+u)
-
D\mathcal S_{R,a}(E_{\xi}),
u
\right\rangle
\ge
c_{\mathrm{loc}}
\left\|
d_a u
\right\|_{0,R,a}^2
-
C_{\mathrm{nl}}(R)
\rho_{\mathrm{chart}}
\left\|u\right\|_{1,R,a}^2
+
o_a(1),
\tag{15.548}
```

for all reduced u in a fixed physical chart of radius rho chart:

```math
\left\|E_{\xi}\right\|_{1,R,a}
+
\left\|u\right\|_{1,R,a}
\le
\rho_{\mathrm{chart}}.
\tag{15.549}
```

**Criterion 40.102 (Hodge Plus Local Convexity Proves Reduced Coercivity).** If
(15.545) and (15.548) hold and the chart radius is chosen so that

```math
C_{\mathrm{nl}}(R)\rho_{\mathrm{chart}}
<
\frac{c_{\mathrm{loc}}}{2C_{\mathrm{Hdg}}(R)},
\tag{15.550}
```

then (15.527) holds with

```math
\lambda_R
=
\frac{c_{\mathrm{loc}}}{2C_{\mathrm{Hdg}}(R)}.
\tag{15.551}
```

#### Proof

By (15.545),

```math
\left\|
d_a u
\right\|_{0,R,a}^2
\ge
\frac{1}{C_{\mathrm{Hdg}}(R)}
\left\|u\right\|_{1,R,a}^2 .
\tag{15.552}
```

Insert this into (15.548). The smallness condition (15.550) leaves the lower
bound (15.551), up to the cutoff error. This is (15.527). `∎`

#### 15.40.3. Small-Chart Bootstrap

The coercivity estimate is only useful if the minimizer stays in the chart where
local convexity holds. This is a deterministic bootstrap.

Suppose

```math
\left\|
D\mathcal S_{R,a}(E_{\xi})
\right\|_{-1,R,a}
\le
C_{\mathrm{grad}}(R)
\left\|E_{\xi}\right\|_{1,R,a}
+
o_a(1)
\tag{15.553}
```

and suppose (15.527) holds in the ball

```math
\left\|u\right\|_{1,R,a}\le\rho_{\mathrm{chart}}.
\tag{15.554}
```

**Criterion 40.103 (Small Boundary Data Keep The Minimizer In The Chart).** If

```math
\left\|E_{\xi}\right\|_{1,R,a}
\le
\frac{\lambda_R}{4C_{\mathrm{grad}}(R)}
\rho_{\mathrm{chart}},
\tag{15.555}
```

then any Dirichlet minimizer connected to the flat branch satisfies

```math
\left\|u_*\right\|_{1,R,a}
\le
\frac{2C_{\mathrm{grad}}(R)}{\lambda_R}
\left\|E_{\xi}\right\|_{1,R,a}
+
o_a(1),
\tag{15.556}
```

and remains inside the convexity chart.

#### Proof

For u inside the chart, integrate (15.527) along the line from zero to u and use
(15.553). This gives

```math
\mathcal S_{R,a}(E_{\xi}+u)
-
\mathcal S_{R,a}(E_{\xi})
\ge
\frac{\lambda_R}{2}
\left\|u\right\|_{1,R,a}^2
-
C_{\mathrm{grad}}(R)
\left\|E_{\xi}\right\|_{1,R,a}
\left\|u\right\|_{1,R,a}
+
o_a(1).
\tag{15.557}
```

At the chart boundary, condition (15.555) makes the right hand side positive.
Hence the minimizing branch cannot exit the chart before lowering the action.
The Euler equation for the interior minimizer then gives the bound (15.556), as
in the proof of Criterion 40.99. `∎`

#### 15.40.4. Gradient And Flux Inputs

The gradient estimate (15.553) follows from bounded local Hessian in the
center-adapted chart:

```math
\left\|
D\mathcal S_{R,a}(E_{\xi})
-
D\mathcal S_{R,a}(0)
\right\|_{-1,R,a}
\le
C_{\mathrm{Hess}}(R)
\left\|E_{\xi}\right\|_{1,R,a}
+
o_a(1),
\tag{15.558}
```

together with

```math
D\mathcal S_{R,a}(0)=0.
\tag{15.559}
```

Thus one may take

```math
C_{\mathrm{grad}}(R)=C_{\mathrm{Hess}}(R).
\tag{15.560}
```

The flux Lipschitz estimate is the physical smoothing input:

```math
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}(A)
-
\Phi^{\mathrm{ren}}_{\gamma,R}(A')
\right|
\le
C_{\Phi}(R,\ell_R)
\left\|A-A'\right\|_{1,R,a}
+
o_a(1).
\tag{15.561}
```

This is where fixed physical IR enters again. The smoothing scale ell_R is held
fixed before the cutoff is removed; no lattice-scale regularity is being used.

#### 15.40.5. Strong PASS Line For (15.518)

Combining the previous criteria gives:

**Criterion 40.104 (Strong Deterministic PASS For Target 40.98).** Suppose the
following fixed-physical estimates hold uniformly as the cutoff is removed:

```math
\begin{array}{ll}
\mathrm{D1:}
&
\text{collar extension }(15.525),\\[1mm]
\mathrm{D2:}
&
\text{reduced Hodge estimate }(15.545),\\[1mm]
\mathrm{D3:}
&
\text{local plaquette convexity }(15.548),\\[1mm]
\mathrm{D4:}
&
\text{small-chart bootstrap }(15.555),\\[1mm]
\mathrm{D5:}
&
\text{flux Lipschitz estimate }(15.561).
\end{array}
\tag{15.562}
```

Then the Dirichlet stability estimate (15.518) holds. Consequently the
untethered bulk mean-bias event is empty in the relative-center-coboundary,
small-coset-tether sector.

#### Proof

D2-D4 give (15.527) and keep the minimizing branch inside its validity chart.
D1 supplies the boundary size estimate. D5 supplies (15.529). Criterion 40.99
then gives (15.518). `∎`

#### 15.40.6. Flux-Visible Low-Mode Alternative

Full coercivity may fail because of soft reduced modes. Such modes do not
necessarily kill Target 40.98. They kill it only if the renormalized flux sees
them.

Let

```math
L_{R,a}
:=
D^2\mathcal S_{R,a}(0)
\tag{15.563}
```

on the reduced zero-boundary space, and define the flux resolvent norm

```math
\Lambda_{\Phi}(R,a)
:=
\left\|
\Phi^{\mathrm{ren}}_{\gamma,R}
L_{R,a}^{-1}
\right\|_{-1\to\mathfrak{so}(3)} .
\tag{15.564}
```

The narrower alternative to full coercivity is:

```math
\sup_{a<a_0}\Lambda_{\Phi}(R,a)<\infty .
\tag{15.565}
```

If (15.565) holds and the nonlinear remainder in the Euler equation is
quadratic on the small branch, then the flux stability estimate can still hold
even when the full reduced inverse norm is not bounded. If (15.565) fails, then
Criterion 40.100 gives the flux-visible low-mode obstruction.

The final Target 40.98 subproblem is therefore:

**Target 40.105 (Reduced Coercivity Or Flux-Blind Soft Modes).** At fixed
physical R and fixed physical smoothing radius, prove one of the following.

PASS-strong:

```math
\text{D1-D5 in }(15.562)\text{ hold.}
\tag{15.566}
```

PASS-weak:

```math
\text{full coercivity may fail, but }(15.565)\text{ holds}
\text{ and nonlinear remainders are controlled.}
\tag{15.567}
```

FAIL:

```math
\limsup_{a\downarrow0}\Lambda_{\Phi}(R,a)=\infty
\tag{15.568}
```

through a reduced low mode that remains inside the physical chart and has
nonzero renormalized flux response.

This is the real fixed-IR fork. Feynman's calculation is the reduced Hessian and
the flux-resolvent norm. Einstein's invariant demand is that any low mode be
classified by what it does to physical-resolution flux, not by microscopic
plaquette coordinates.

### 15.41. Working Target 40.105: The Reduced Hessian Mode Test

Searchable Target-40.105 mode tag:

`V4P40-TARGET-40105-REDUCED-HESSIAN-MODE-TEST`.

We now carry out the five-step attack on Target 40.105 at the proof-package
level. The order of limits is still:

```math
R\text{ fixed},
\qquad
\ell_R\text{ fixed},
\qquad
a\downarrow0.
\tag{15.569}
```

The object to compute is not the whole microscopic spectrum. It is the reduced
Hessian together with the physical-resolution flux functional.

#### 15.41.1. Step 1: Reduced Hodge Estimate

Let the reduced zero-boundary one-cochain space be

```math
\mathcal H^1_{R,a,\mathrm{red}}
:=
\left\{
u\in C^1_0(B_R(a),\mathfrak{so}(3)):
d_a^*u=0,
\Pi_{\mathrm{harm}}u=0
\right\}.
\tag{15.570}
```

Here the harmonic projection removes relative harmonic one-forms. If those
forms are not removed, they are coset-tether data, not bulk fluctuations.

The discrete compactness input is:

```math
\left\|u\right\|_{1,R,a}^2
\le
C_{\mathrm{Hdg}}(R)
\left\|
d_a u
\right\|_{0,R,a}^2
\qquad
u\in\mathcal H^1_{R,a,\mathrm{red}}.
\tag{15.571}
```

**Criterion 40.106 (Discrete Compactness Proves Reduced Hodge).** Suppose the
fixed physical block has trivial relative first cohomology after coset-tether
modes are removed, and suppose the lattice refinements satisfy the standard
discrete compactness property for the reduced de Rham complex. Then (15.571)
holds with a constant independent of the cutoff.

#### Proof

If (15.571) failed, there would be a cutoff sequence and reduced cochains u_a
such that

```math
\left\|u_a\right\|_{1,R,a}=1,
\qquad
\left\|d_a u_a\right\|_{0,R,a}\longrightarrow0.
\tag{15.572}
```

By discrete compactness, a subsequence of the interpolated one-forms converges
strongly in the physical L2 norm and weakly in the physical H1 norm to a
continuum one-form u. The limits of the equations defining the reduced space
give

```math
du=0,
\qquad
d^*u=0,
\qquad
u\vert_{\partial}=0,
\qquad
\Pi_{\mathrm{harm}}u=0.
\tag{15.573}
```

Trivial relative cohomology then gives

```math
u=0.
\tag{15.574}
```

This contradicts the normalized convergence in (15.572). Therefore (15.571)
holds. `∎`

This is the topological part of the calculation. If relative harmonic modes
remain, they must be routed as coset tethers before applying the reduced Hodge
estimate.

#### 15.41.2. Step 2: Hessian In Center-Adapted Variables

In the center-adapted chart, the plaquette argument has the form

```math
\mathfrak P^s_{\zeta,p}(A)
=
\exp
\left(
(d_aA)_p
+
\mathcal Q_p(A)
\right),
\tag{15.575}
```

with

```math
\left|
\mathcal Q_p(A)-\mathcal Q_p(A')
\right|
\le
C_R
\left(
\left|A\right|+\left|A'\right|
\right)
\left|A-A'\right|
\tag{15.576}
```

inside the fixed physical chart. After normalization, the plaquette action
satisfies

```math
\sigma
\left(
\exp X
\right)
=
\frac{1}{2}
\left\langle
X,
H_tX
\right\rangle
+
O(|X|^3),
\tag{15.577}
```

where the normalized Hessian obeys

```math
m_0|X|^2
\le
\left\langle
X,
H_tX
\right\rangle
\le
M_0|X|^2
\tag{15.578}
```

with constants independent of the cutoff on the small heat-kernel trajectory.
Consequently the reduced Hessian at the flat branch is

```math
L_{R,a}
=
d_a^*H_td_a
+
K_{R,a},
\tag{15.579}
```

where K is a uniformly bounded lower-order chart term which vanishes at the
flat filling in the strictly quadratic approximation.

**Criterion 40.107 (Hessian Ellipticity Gives Local Convexity).** If (15.576)
and (15.578) hold in the fixed physical chart, then the local convexity estimate
(15.548) holds with

```math
c_{\mathrm{loc}}=\frac{m_0}{2}
\tag{15.580}
```

after reducing the chart radius if necessary.

#### Proof

Use the fundamental theorem of calculus:

```math
\left\langle
D\mathcal S(E_{\xi}+u)
-
D\mathcal S(E_{\xi}),
u
\right\rangle
=
\int_0^1
\left\langle
D^2\mathcal S(E_{\xi}+tu)u,
u
\right\rangle
dt.
\tag{15.581}
```

The quadratic part gives the lower bound m_0 times the plaquette curvature norm.
The commutator and chart terms are bounded by (15.576) and the small chart
radius, producing the nonlinear subtraction in (15.548). Reducing the chart
radius leaves the coefficient (15.580). `∎`

Thus the strong PASS line is a standard-looking elliptic estimate, but only
after center adaptation, gauge reduction, and tether removal.

#### 15.41.3. Step 3: Spectral Flux-Resolvent Test

Let

```math
\left\{\psi_{k,a}\right\}_{k=1}^{N_a}
\tag{15.582}
```

be an orthonormal basis of reduced modes for the physical one-cochain inner
product, diagonalizing the reduced Hessian:

```math
L_{R,a}\psi_{k,a}
=
\lambda_{k,a}\psi_{k,a},
\qquad
0<\lambda_{1,a}\le\lambda_{2,a}\le\cdots .
\tag{15.583}
```

Let the linearization of the renormalized flux at the flat branch be

```math
\Phi^{\mathrm{lin}}_{\gamma,R,a}
\tag{15.584}
```

and set

```math
\varphi_{k,a}
:=
\Phi^{\mathrm{lin}}_{\gamma,R,a}(\psi_{k,a}).
\tag{15.585}
```

Then the flux-resolvent norm is bounded by the spectral sum

```math
\Lambda_{\Phi}(R,a)^2
\le
\sum_{k=1}^{N_a}
\frac{
\left|
\varphi_{k,a}
\right|^2
}{
\lambda_{k,a}^2
}.
\tag{15.586}
```

**Criterion 40.108 (Mode Sum Proves Flux-Resolvent Bound).** If

```math
\sup_{a<a_0}
\sum_{k=1}^{N_a}
\frac{
\left|
\varphi_{k,a}
\right|^2
}{
\lambda_{k,a}^2
}
<
\infty,
\tag{15.587}
```

then the flux-resolvent bound (15.565) holds.

#### Proof

For any forcing covector f with dual norm at most one, write

```math
f
=
\sum_k f_{k,a}\psi_{k,a}^{\flat}.
\tag{15.588}
```

Then

```math
\Phi^{\mathrm{lin}}_{\gamma,R,a}
L_{R,a}^{-1}f
=
\sum_k
\frac{f_{k,a}}{\lambda_{k,a}}
\varphi_{k,a}.
\tag{15.589}
```

Cauchy-Schwarz gives (15.586), and (15.587) makes the bound uniform. `∎`

This is the finite-dimensional calculation Feynman would actually do: list the
soft modes and compute their physical flux matrix elements.

#### 15.41.4. Step 4: Physical Smoothing Splits UV And IR Modes

Because the flux is defined after smoothing at physical radius ell_R, high
lattice-frequency modes should not dominate the sum (15.587). The needed
estimate is:

```math
\left|
\varphi_{k,a}
\right|
\le
C_{\Phi,0}(R,\ell_R)
\exp
\left(
-
c_{\Phi}\ell_R^2\mu_{k,a}
\right)
\left\|\psi_{k,a}\right\|_{1,R,a},
\tag{15.590}
```

where mu_{k,a} is the corresponding reduced Hodge-Laplacian frequency. This is
the linearized form of the physical smoothing estimate.

Choose a fixed physical frequency cutoff

```math
\mu_*
\asymp
\ell_R^{-2}.
\tag{15.591}
```

Then the mode sum splits into

```math
\sum_{k}
\frac{
\left|
\varphi_{k,a}
\right|^2
}{
\lambda_{k,a}^2
}
=
\sum_{\mu_{k,a}\le\mu_*}
\frac{
\left|
\varphi_{k,a}
\right|^2
}{
\lambda_{k,a}^2
}
+
\sum_{\mu_{k,a}>\mu_*}
\frac{
\left|
\varphi_{k,a}
\right|^2
}{
\lambda_{k,a}^2
}.
\tag{15.592}
```

**Criterion 40.109 (Smoothing Reduces The Flux-Resolvent Test To Physical Low
Modes).** Suppose (15.590) holds, and suppose the high-frequency Hessian obeys

```math
\lambda_{k,a}
\ge
c_L\mu_{k,a}
\qquad
\text{for }\mu_{k,a}>\mu_*.
\tag{15.593}
```

Then the high-frequency part of (15.592) is uniformly bounded as the cutoff is
removed. Consequently Target 40.105 reduces to a finite physical list of
low-frequency modes with

```math
\mu_{k,a}\le\mu_*.
\tag{15.594}
```

#### Proof

Insert (15.590) and (15.593) into the high-frequency part of (15.592). The
exponential factor from fixed physical smoothing dominates the lattice density
of states as the cutoff is removed. The remaining low-frequency band contains
only cutoff-uniformly many physical modes for fixed R and fixed ell_R. `∎`

This is the fixed-IR point. We are not proving smallness by shrinking the
observable to the lattice scale. We are using a physical smoothing radius chosen
before the cutoff limit.

#### 15.41.5. Step 5: Honest Failure Certificate

The reduced Hessian calculation gives a sharp fail certificate.

**Criterion 40.110 (Flux-Visible Soft Mode Falsifies The Stability Route).**
Suppose there is a cutoff sequence and reduced eigenmodes psi_a such that

```math
L_{R,a}\psi_a
=
\lambda_a\psi_a,
\qquad
\left\|\psi_a\right\|_{1,R,a}=1,
\qquad
\lambda_a\downarrow0,
\tag{15.595}
```

and

```math
\left|
\Phi^{\mathrm{lin}}_{\gamma,R,a}(\psi_a)
\right|
\ge
\eta_R>0.
\tag{15.596}
```

Assume also that the boundary forcing map can excite the corresponding dual
mode with coset collar size proportional to the forcing norm, and that the
nonlinear branch remains in the fixed physical chart. Then the stability
estimate (15.518) fails.

#### Proof

Choose forcing in the dual direction of psi_a with size

```math
\epsilon_a\lambda_a .
\tag{15.597}
```

The linearized minimizer displacement is

```math
\epsilon_a\psi_a.
\tag{15.598}
```

The coset collar size is of order epsilon_a lambda_a, while the renormalized
flux response is at least

```math
\epsilon_a\eta_R.
\tag{15.599}
```

Therefore the ratio of flux response to coset collar size is at least

```math
\frac{\eta_R}{\lambda_a}
\longrightarrow
\infty .
\tag{15.600}
```

Choosing epsilon_a small enough keeps the branch in the chart. This contradicts
any cutoff-uniform stability constant in (15.518). `∎`

This is not a toy-model failure. It is an explicit finite-cutoff spectral
certificate for a fixed-physical SO(3) obstruction.

#### 15.41.6. Completed Five-Step Test

The five steps now combine into the final working version of Target 40.105.

**Target 40.111 (Reduced Hessian And Flux-Resolvent Calculation).** At fixed
physical R and fixed physical smoothing radius, prove one of the following.

PASS-strong:

```math
\text{reduced Hodge }(15.571)
+\text{ Hessian convexity }(15.548)
+\text{ chart bootstrap }(15.555)
\tag{15.601}
```

hold uniformly as the cutoff is removed.

PASS-weak:

```math
\text{the mode sum }(15.587)\text{ is uniformly bounded}
\tag{15.602}
```

even if full coercivity fails.

FAIL:

```math
\text{there is a flux-visible soft mode satisfying }(15.595)\text{ and }(15.596).
\tag{15.603}
```

PASS-strong proves (15.518) through Criterion 40.104. PASS-weak proves the
flux-resolvent part needed for the weaker Target 40.105 route, provided the
nonlinear remainder stays quadratic on the small branch. FAIL falsifies the
Dirichlet-stability route and exposes a genuine fixed-IR SO(3) obstruction.

### 15.42. Working Target 40.111: Finite Physical Low-Mode Criterion

Searchable Target-40.111 low-mode tag:

`V4P40-TARGET-40111-FINITE-PHYSICAL-LOW-MODE-CRITERION`.

Criterion 40.109 reduces the flux-resolvent problem to finitely many physical
low modes. The remaining test is not that every low mode be heavy. The true
test is whether soft low modes are flux-blind at the rate needed by the
resolvent.

Define the fixed physical low-band index set

```math
\mathcal I_{\le}(R,\ell_R,a)
:=
\left\{
k:\mu_{k,a}\le\mu_*
\right\}.
\tag{15.604}
```

For fixed R and fixed smoothing radius, the cardinality is cutoff-uniform:

```math
\sup_{a<a_0}
\left|
\mathcal I_{\le}(R,\ell_R,a)
\right|
<
\infty .
\tag{15.605}
```

The low-band flux-resolvent ratio is

```math
\mathcal R_{\Phi}^{\mathrm{low}}(R,a)^2
:=
\sum_{k\in\mathcal I_{\le}(R,\ell_R,a)}
\frac{
\left|
\varphi_{k,a}
\right|^2
}{
\lambda_{k,a}^2
}.
\tag{15.606}
```

**Criterion 40.112 (Finite Low-Mode Ratio Proves PASS-Weak).** Suppose the
high-frequency estimate of Criterion 40.109 holds. If

```math
\sup_{a<a_0}
\mathcal R_{\Phi}^{\mathrm{low}}(R,a)
<
\infty,
\tag{15.607}
```

then the full mode-sum estimate (15.587) holds, and Target 40.111 satisfies
PASS-weak.

#### Proof

Criterion 40.109 bounds the high-frequency part of (15.592). The remaining
low-frequency part is exactly (15.606). The cutoff-uniform bound (15.607)
therefore proves (15.587). `∎`

This is the exact form of the finite low-mode calculation.

#### 15.42.1. The Elementary Low-Mode Alternative

Because the low band is finite in physical units, the ratio condition can be
checked mode by mode. For each low mode, one needs either a spectral gap or
flux blindness at the resolvent rate:

```math
\boxed{
\begin{array}{c}
\lambda_{k,a}\ge\lambda_0(R,\ell_R)>0\\[1mm]
\text{or}\\[1mm]
\left|
\varphi_{k,a}
\right|
\le
C_{\Phi}^{\mathrm{soft}}(R,\ell_R)\lambda_{k,a}.
\end{array}}
\tag{15.608}
```

**Criterion 40.113 (Gap-Or-Flux-Blindness Proves The Low-Mode Ratio).** If
(15.608) holds for every low-band mode with constants independent of the cutoff,
then (15.607) holds.

#### Proof

For modes satisfying the gap line in (15.608), use the uniform boundedness of
the linearized physical flux on the finite low band:

```math
\left|
\varphi_{k,a}
\right|
\le
C_{\Phi}^{\mathrm{low}}(R,\ell_R).
\tag{15.609}
```

Their contribution is bounded by

```math
\frac{
\left(
C_{\Phi}^{\mathrm{low}}(R,\ell_R)
\right)^2
}{
\lambda_0(R,\ell_R)^2
}.
\tag{15.610}
```

For modes satisfying the flux-blindness line in (15.608), the contribution is
bounded by

```math
\left(
C_{\Phi}^{\mathrm{soft}}(R,\ell_R)
\right)^2.
\tag{15.611}
```

There are only cutoff-uniformly many low-band modes by (15.605), so the sum
(15.606) is uniformly bounded. `∎`

Exact vanishing of the flux matrix element is only the cleanest special case:

```math
\varphi_{k,a}=0.
\tag{15.612}
```

The actual sufficient condition is the weaker rate in (15.608).

#### 15.42.2. Flux Factorization Through The Hessian

There is a coordinate-free way to state flux blindness. On the low band, the
linearized flux should factor through the reduced Hessian.

Let

```math
P_{\le,a}
\tag{15.613}
```

be the spectral projector onto the low band. Suppose there is a uniformly
bounded family of linear maps

```math
B_{R,a}:
\mathcal H^1_{R,a,\mathrm{red}}
\longrightarrow
\mathfrak{so}(3)
\tag{15.614}
```

such that

```math
\Phi^{\mathrm{lin}}_{\gamma,R,a}P_{\le,a}
=
B_{R,a}L_{R,a}P_{\le,a}
+
\mathcal R_{R,a},
\tag{15.615}
```

with

```math
\left\|
\mathcal R_{R,a}L_{R,a}^{-1}P_{\le,a}
\right\|_{-1\to\mathfrak{so}(3)}
\longrightarrow0.
\tag{15.616}
```

**Criterion 40.114 (Low-Band Flux Factorization Proves PASS-Weak).** If
(15.615)-(15.616) hold and the high-frequency estimate of Criterion 40.109
holds, then Target 40.111 satisfies PASS-weak.

#### Proof

On the low band,

```math
\Phi^{\mathrm{lin}}_{\gamma,R,a}
L_{R,a}^{-1}P_{\le,a}
=
B_{R,a}P_{\le,a}
+
\mathcal R_{R,a}L_{R,a}^{-1}P_{\le,a}.
\tag{15.617}
```

The first term is uniformly bounded by assumption on B. The second tends to
zero by (15.616). The high-frequency part is controlled by Criterion 40.109.
Thus the full flux-resolvent norm is bounded. `∎`

This formulation is useful because it says exactly what soft modes are allowed
to do: they may exist, but the physical flux must be a Hessian derivative on
their span. Then the inverse Hessian cancels.

#### 15.42.3. Continuum Low-Mode Reading

If the low-band spectral data converge to a continuum reduced operator

```math
L_R
\tag{15.618}
```

and a continuum physical flux functional

```math
\Phi^{\mathrm{lin}}_{\gamma,R},
\tag{15.619}
```

then the invariant continuum condition is not merely

```math
\operatorname{ker}L_R
\subset
\operatorname{ker}\Phi^{\mathrm{lin}}_{\gamma,R}.
\tag{15.620}
```

That inclusion is necessary, but by itself it may not control the rate at which
near-kernel lattice modes approach the kernel. The fixed-IR condition is the
resolvent form:

```math
\Phi^{\mathrm{lin}}_{\gamma,R}
=
B_RL_R
\quad
\text{on the physical low-mode sector}
\tag{15.621}
```

with B_R bounded. Equation (15.621) is the continuum version of (15.615).

Thus the Einstein form of the low-mode test is:

```math
\boxed{
\begin{array}{c}
\text{Does the physical flux functional descend through}\\[1mm]
\text{the reduced Dirichlet Hessian on the low sector?}
\end{array}}
\tag{15.622}
```

If yes, soft modes are flux-blind. If no, the remaining question is whether the
bad direction is actually excited by collar forcing.

#### 15.42.4. Low-Mode Failure Certificate

The exact fail condition is the negation of the bounded ratio test.

**Criterion 40.115 (Unbounded Low-Mode Ratio Falsifies PASS-Weak).** Suppose
there is a cutoff sequence and low-band modes k(a) such that

```math
\mu_{k(a),a}\le\mu_*,
\qquad
\lambda_{k(a),a}\downarrow0,
\tag{15.623}
```

and

```math
\frac{
\left|
\varphi_{k(a),a}
\right|
}{
\lambda_{k(a),a}
}
\longrightarrow
\infty.
\tag{15.624}
```

If the corresponding dual mode can be excited by admissible small coset collar
forcing and the nonlinear branch remains in the fixed physical chart, then
Target 40.111 satisfies FAIL.

#### Proof

Condition (15.624) is exactly the divergence of the low-band flux-resolvent
ratio in the direction k(a). Exciting the dual mode gives the same instability
construction as Criterion 40.110, with the ratio of physical flux response to
coset collar size diverging. Hence no cutoff-uniform stability estimate can
hold. `∎`

#### 15.42.5. Final Low-Mode Target

The final sharpened form is:

**Target 40.116 (Finite Physical Low-Mode Pass/Fail Test).** At fixed physical R
and fixed physical smoothing radius, prove one of the following.

PASS-gap:

```math
\lambda_{k,a}\ge\lambda_0(R,\ell_R)>0
\quad
\text{for every }k\in\mathcal I_{\le}(R,\ell_R,a).
\tag{15.625}
```

PASS-factor:

```math
\Phi^{\mathrm{lin}}_{\gamma,R,a}P_{\le,a}
=
B_{R,a}L_{R,a}P_{\le,a}
+
\mathcal R_{R,a}
\quad
\text{with }(15.616).
\tag{15.626}
```

FAIL:

```math
\text{there is a low-band mode satisfying }(15.623)\text{ and }(15.624).
\tag{15.627}
```

PASS-gap is the strong finite low-mode version. PASS-factor is the weaker
flux-blind-soft-mode version. FAIL is the fixed-physical SO(3) obstruction.
This is the concrete next computation for the reduced Hessian route.

### 15.43. Target 40.117: PASS-Gap From Reduced Hodge-Hessian Control

Searchable Target-40.117 tag:

`V4P40-TARGET-40117-PASS-GAP-HODGE-HESSIAN`.

The first post-40.116 target is the strong PASS-gap line. It is deterministic:
after center adaptation, tether removal, and gauge reduction, the low-band
eigenvalues are bounded below if the reduced Hodge estimate and the flat
plaquette Hessian are both cutoff-uniform.

Let the reduced Hessian satisfy

```math
\left\langle
L_{R,a}u,
u
\right\rangle
\ge
m_R
\left\|
d_a u
\right\|_{0,R,a}^2
-
r_a
\left\|u\right\|_{1,R,a}^2,
\tag{15.628}
```

where

```math
r_a\longrightarrow0
\tag{15.629}
```

uniformly on the reduced chart. Assume the reduced Hodge estimate

```math
\left\|u\right\|_{1,R,a}^2
\le
C_{\mathrm{Hdg}}(R)
\left\|
d_a u
\right\|_{0,R,a}^2
\tag{15.630}
```

on the tether-removed reduced space.

**Criterion 40.117 (Hodge-Hessian Gap Proves PASS-Gap).** If (15.628)-(15.630)
hold, then for all sufficiently small cutoffs,

```math
\lambda_{k,a}
\ge
\lambda_0(R)
:=
\frac{m_R}{2C_{\mathrm{Hdg}}(R)}
\tag{15.631}
```

for every reduced mode, hence for every low-band mode. Therefore Target 40.116
satisfies PASS-gap.

#### Proof

Use (15.630) to rewrite (15.628):

```math
\left\langle
L_{R,a}u,
u
\right\rangle
\ge
\left(
\frac{m_R}{C_{\mathrm{Hdg}}(R)}
-
r_a
\right)
\left\|u\right\|_{1,R,a}^2 .
\tag{15.632}
```

For small enough cutoff, the parenthesis is at least the constant in (15.631).
The Rayleigh-Ritz characterization of the reduced eigenvalues gives (15.631).
`∎`

Thus the strong pass is available whenever the block topology has no unremoved
relative harmonic one-forms and the center-adapted plaquette action is genuinely
convex near the flat branch.

The matching fail diagnostic is:

```math
\boxed{
\begin{array}{c}
\text{if PASS-gap fails before dynamics enters,}\\[1mm]
\text{then either a relative harmonic/coset-tether mode was not removed,}\\[1mm]
\text{or the center-adapted Hessian is not uniformly elliptic.}
\end{array}}
\tag{15.633}
```

The first failure is a routing error. The second is a genuine local analytic
obstruction.

### 15.44. Target 40.118: Dual Flux Source Equivalence

Searchable Target-40.118 tag:

`V4P40-TARGET-40118-DUAL-FLUX-SOURCE-EQUIVALENCE`.

The PASS-factor line can be made exact by passing to the dual source of the
linearized flux. Let

```math
j_{\gamma,R,a}
\in
\left(
\mathcal H^1_{R,a,\mathrm{red}}
\right)^*
\tag{15.634}
```

be the covector representing the linearized renormalized flux:

```math
\Phi^{\mathrm{lin}}_{\gamma,R,a}(u)
=
\left\langle
j_{\gamma,R,a},
u
\right\rangle .
\tag{15.635}
```

Let

```math
w_{\gamma,R,a}
\tag{15.636}
```

be the reduced dual Green field solving

```math
L_{R,a}w_{\gamma,R,a}
=
j_{\gamma,R,a}
\tag{15.637}
```

on the orthogonal complement of the kernel. If a kernel remains, (15.637) is
interpreted after projecting j onto the range of L.

**Theorem 40.118 (Flux-Resolvent Equals Dual Green Norm).** On the reduced
finite-cutoff space,

```math
\Lambda_{\Phi}(R,a)
=
\left\|
w_{\gamma,R,a}
\right\|_{1,R,a}
\tag{15.638}
```

up to the fixed equivalence between the reduced norm and its dual. Consequently
the PASS-factor condition is equivalent to

```math
\sup_{a<a_0}
\left\|
w_{\gamma,R,a}
\right\|_{1,R,a}
<
\infty .
\tag{15.639}
```

#### Proof

For any forcing covector f,

```math
\Phi^{\mathrm{lin}}_{\gamma,R,a}
L_{R,a}^{-1}f
=
\left\langle
j_{\gamma,R,a},
L_{R,a}^{-1}f
\right\rangle .
\tag{15.640}
```

Since L is self-adjoint on the reduced space,

```math
\left\langle
j_{\gamma,R,a},
L_{R,a}^{-1}f
\right\rangle
=
\left\langle
L_{R,a}^{-1}j_{\gamma,R,a},
f
\right\rangle
=
\left\langle
w_{\gamma,R,a},
f
\right\rangle .
\tag{15.641}
```

Taking the supremum over dual-unit f gives the norm of w. `∎`

This is often the cleanest Feynman calculation. Instead of inspecting every
mode, solve one reduced dual Dirichlet problem.

The kernel compatibility condition is:

```math
j_{\gamma,R,a}
\perp
\ker L_{R,a}.
\tag{15.642}
```

If (15.642) fails, then a zero mode is flux-visible and PASS-factor fails
immediately.

### 15.45. Target 40.119: Continuum Dual Flux Potential

Searchable Target-40.119 tag:

`V4P40-TARGET-40119-CONTINUUM-DUAL-FLUX-POTENTIAL`.

The dual Green formulation has a fixed-IR continuum reading. Because the flux is
smoothed at physical radius, its linear source is not a singular unsmoothed
surface delta. It is a physical-resolution covector.

Assume the discrete sources converge:

```math
j_{\gamma,R,a}
\longrightarrow
j_{\gamma,R}
\tag{15.643}
```

in the continuum dual norm at fixed smoothing radius. Let the continuum reduced
operator be

```math
L_R
\tag{15.644}
```

on the tether-removed reduced Dirichlet space. The continuum dual problem is

```math
L_Rw_{\gamma,R}
=
j_{\gamma,R}.
\tag{15.645}
```

**Criterion 40.119 (Continuum Dual Potential Proves PASS-Factor).** Suppose:

```math
j_{\gamma,R}
\perp
\ker L_R,
\tag{15.646}
```

and the continuum dual problem has a reduced solution satisfying

```math
\left\|
w_{\gamma,R}
\right\|_{1,R}
\le
C_{\mathrm{dual}}(R,\ell_R).
\tag{15.647}
```

Suppose moreover that the discrete reduced operators and sources converge in
the strong resolvent sense on the low physical band:

```math
w_{\gamma,R,a}
\longrightarrow
w_{\gamma,R}
\tag{15.648}
```

in the physical reduced norm. Then (15.639) holds, hence Target 40.116 satisfies
PASS-factor.

#### Proof

The convergence (15.648) and the continuum bound (15.647) give a uniform bound
for the discrete dual Green fields. Theorem 40.118 then gives the
flux-resolvent bound. `∎`

The corresponding fail line is just as sharp:

```math
\boxed{
\begin{array}{c}
\text{if }j_{\gamma,R}\text{ has a component in }\ker L_R,\\[1mm]
\text{then the physical flux sees a continuum soft mode.}
\end{array}}
\tag{15.649}
```

That is the fixed-IR obstruction in invariant form.

**Target 40.120 (Dual Flux Potential Alternative).** At fixed physical R and
fixed physical smoothing radius, prove one of the following.

PASS-dual:

```math
\text{the continuum problem }(15.645)\text{ has the bounded solution }(15.647)
\text{ and discrete convergence }(15.648).
\tag{15.650}
```

FAIL-dual:

```math
j_{\gamma,R}
\not\perp
\ker L_R
\tag{15.651}
```

or the discrete dual Green fields diverge despite kernel orthogonality.

This target is equivalent in force to the low-mode ratio test, but it is often
more computable: solve one dual elliptic problem instead of tracking all
low-band eigenvectors.

### 15.46. Target 40.121: Exhaustion Of The Post-40.116 Branches

Searchable Target-40.121 tag:

`V4P40-TARGET-40121-POST-40116-EXHAUSTION`.

The work after Target 40.116 leaves exactly three branches.

**Branch A: PASS-gap.** Prove the reduced Hodge-Hessian gap:

```math
\lambda_{k,a}\ge\lambda_0(R)>0.
\tag{15.652}
```

This follows from Target 40.117. It closes the finite low-mode test without
needing flux factorization.

**Branch B: PASS-factor.** If full gap fails, prove the dual source bound:

```math
\sup_{a<a_0}
\left\|
L_{R,a}^{-1}j_{\gamma,R,a}
\right\|_{1,R,a}
<
\infty .
\tag{15.653}
```

This is Target 40.118 or Target 40.120.

**Branch C: FAIL.** Exhibit a physical low mode with divergent ratio:

```math
\frac{
\left|
\Phi^{\mathrm{lin}}_{\gamma,R,a}(\psi_{k,a})
\right|
}{
\lambda_{k,a}
}
\longrightarrow
\infty.
\tag{15.654}
```

This is Criterion 40.115. If the mode can be excited by admissible collar data
and remains in the chart, the Dirichlet-stability route fails.

These branches are exhaustive because they are exactly the trichotomy for the
finite low-band resolvent:

```math
\boxed{
\begin{array}{c}
\text{either low modes are gapped,}\\[1mm]
\text{or the flux source is in the range of the reduced Hessian with bounded
potential,}\\[1mm]
\text{or the flux-resolvent norm diverges.}
\end{array}}
\tag{15.655}
```

#### Consequence For Target 40.98

If Branch A or Branch B holds, and the nonlinear small-branch estimates in
Target 40.105 hold, then the deterministic stability estimate (15.518) holds.
Together with the adjoint collar estimate (15.511) and center-tether routing,
Target 40.98 satisfies its corrected PASS-B/C alternative.

If Branch C holds, then Target 40.98 fails through an untethered physical SO(3)
mean-bias obstruction, unless the mode is reclassified as a coset tether or is
not excitable by admissible collar data.

Thus the next target after 40.116 is not another abstract theorem. It is the
computable dichotomy:

```math
\boxed{
\begin{array}{c}
\text{solve the reduced dual flux problem }(15.645),\\[1mm]
\text{or find a flux-visible low mode.}
\end{array}}
\tag{15.656}
```

### 15.47. Target 40.122: Return Map To The Global Wilson Route

Searchable Target-40.122 tag:

`V4P40-TARGET-40122-RETURN-MAP-TO-WILSON-ROUTE`.

For clarity, here is the dependency chain back to the global route.

If Target 40.120 passes, then Target 40.116 passes by PASS-factor. If Target
40.116 passes, then Target 40.111 passes. If Target 40.111 passes, then Target
40.105 passes. If Target 40.105 passes with the nonlinear remainder estimates,
then Target 40.98 gets its deterministic stability input (15.518).

The remaining non-deterministic inputs to Target 40.98 are:

```math
\begin{array}{ll}
\mathrm{R1:}
&
\text{adjoint collar moment estimate }(15.511),\\[1mm]
\mathrm{R2:}
&
\text{center tethers routed into the center-sheet disorder channel},\\[1mm]
\mathrm{R3:}
&
\text{untethered bulk mean-bias event empty or summable}.
\end{array}
\tag{15.657}
```

With (15.518) in hand, R3 is empty in the relative-center-coboundary,
small-coset-tether sector. R1 is the same type of finite physical adjoint
character estimate already reduced to renormalized flux variance in Target
40.75. R2 is a bookkeeping and center-disorder compatibility condition.

Thus, after exhausting Target 40.116, the next live targets are exactly:

```math
\boxed{
\begin{array}{ll}
\text{Next A:}
&
\text{prove the dual flux potential alternative }40.120,\\[1mm]
\text{Next B:}
&
\text{prove the adjoint collar estimate }(15.511),\\[1mm]
\text{Next C:}
&
\text{verify center-tether routing against the center-sheet disorder estimate.}
\end{array}}
\tag{15.658}
```

If all three hold, Target 40.91 supplies the mean-flux part of Target 40.81. If
any fails, the paper has a precise obstruction:

```math
\boxed{
\begin{array}{ll}
\text{A fails:}
&
\text{flux-visible SO(3) low mode},\\[1mm]
\text{B fails:}
&
\text{large coset collar response survives at fixed physical scale},\\[1mm]
\text{C fails:}
&
\text{center-sheet disorder is not compatible with the routed center tethers.}
\end{array}}
\tag{15.659}
```

This exhausts the post-40.116 route. The proof is now reduced to one
deterministic dual elliptic calculation, one finite physical adjoint response
estimate, and one center-sheet routing check.

### 15.48. Target 40.123: Solving Next A By The Fixed-IR Fredholm Alternative

Searchable Target-40.123 tag:

`V4P40-TARGET-40123-NEXT-A-FREDHOLM-DUAL`.

Next A asks for the dual flux potential alternative in Target 40.120. At fixed
physical R, this is not a probabilistic question. It is the Fredholm alternative
for the reduced continuum Hessian, plus discrete convergence.

Let the continuum reduced Dirichlet space be

```math
\mathcal H^1_{R,\mathrm{red}}
\tag{15.660}
```

and let

```math
L_R:
\mathcal H^1_{R,\mathrm{red}}
\longrightarrow
\left(\mathcal H^1_{R,\mathrm{red}}\right)^*
\tag{15.661}
```

be the continuum reduced Hessian. Assume the fixed-IR Fredholm package:

```math
\boxed{
\begin{array}{ll}
\mathrm{F1:}
&
L_R\text{ is self-adjoint and nonnegative},\\[1mm]
\mathrm{F2:}
&
\ker L_R\text{ is finite dimensional and consists only of reduced soft modes},\\[1mm]
\mathrm{F3:}
&
L_R\text{ has closed range on }\left(\ker L_R\right)^\perp,\\[1mm]
\mathrm{F4:}
&
\text{the discrete reduced operators converge to }L_R
\text{ in strong resolvent sense.}
\end{array}}
\tag{15.662}
```

**Criterion 40.123 (Fredholm Alternative Exhausts Next A).** Under (15.662),
exactly one of the following two alternatives holds.

PASS-A:

```math
j_{\gamma,R}
\perp
\ker L_R.
\tag{15.663}
```

Then there is a unique reduced solution

```math
w_{\gamma,R}
\in
\left(\ker L_R\right)^\perp
\tag{15.664}
```

of

```math
L_Rw_{\gamma,R}
=
j_{\gamma,R}
\tag{15.665}
```

and

```math
\left\|
w_{\gamma,R}
\right\|_{1,R}
\le
C_{\mathrm{Fred}}(R)
\left\|
j_{\gamma,R}
\right\|_{-1,R}.
\tag{15.666}
```

With F4, the discrete dual fields obey

```math
\sup_{a<a_0}
\left\|
w_{\gamma,R,a}
\right\|_{1,R,a}
<
\infty.
\tag{15.667}
```

FAIL-A:

```math
P_{\ker L_R}j_{\gamma,R}
\ne
0,
\tag{15.668}
```

or F4 fails for the reduced physical low band.

#### Proof

If (15.663) holds, then j lies in the annihilator of the kernel. By closed range
and self-adjointness, this is the range of L_R. The inverse on the orthogonal
complement of the kernel is bounded, giving (15.664)-(15.666). Strong resolvent
convergence transfers the bounded continuum solution to the discrete dual Green
fields, yielding (15.667).

If (15.668) holds, the continuum flux source has a component along a soft
direction. Then the equation (15.665) has no reduced solution orthogonal to the
kernel, and the flux-resolvent norm diverges in the corresponding near-kernel
discrete directions unless that mode is reclassified as a tether. If F4 fails,
the discrete low-band calculation has not converged to the fixed-IR continuum
problem, so Next A fails as a continuum proof. `∎`

Thus Next A is exhausted:

```math
\boxed{
\begin{array}{c}
\text{prove the reduced Fredholm package and kernel orthogonality,}\\[1mm]
\text{or exhibit a flux-visible reduced soft mode,}\\[1mm]
\text{or identify failure of discrete-to-continuum convergence.}
\end{array}}
\tag{15.669}
```

This is the clean fixed-physical form of the dual route. It does not use UV
smallness. The cutoff enters only through convergence to the fixed physical
operator.

### 15.49. Target 40.124: Solving Next B By Collar-Loop Inclusion

Searchable Target-40.124 tag:

`V4P40-TARGET-40124-NEXT-B-ADJOINT-COLLAR`.

Next B asks for the adjoint collar estimate (15.511). This is not independent
of Target 40.75. If the collar loop family was included among the finite
physical loops controlled by Target 40.75, then Next B is immediate.

Assume the collar loops are physical-resolution observables:

```math
\mathcal B_{\gamma,R}^{\mathrm{collar}}
\subset
\mathcal L_R^{\mathrm{phys}},
\tag{15.670}
```

where the family on the right is the finite loop family to which Target 40.75
is applied. Assume that Target 40.75 holds uniformly on this family:

```math
\sup_{\alpha\in\mathcal B_{\gamma,R}^{\mathrm{collar}}}
\left[
1
-
\frac{1}{3}
\mathsf K^s_{R,a,b}
\left(
\chi_{\mathrm{ad}}
\left(
H^{\mathrm{ren}}_{\alpha,R}
\right)
\mid
\xi_-
\right)
\right]
\le
C_{\mathrm{collar}}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.671}
```

Finally require the route to use the same renormalized collar holonomy in the
coset-tether test:

```math
\operatorname{Hol}_{\alpha}(\xi_-,\xi_+)
\quad
\text{in }(15.509)
\quad
\text{is replaced by}
\quad
H^{\mathrm{ren}}_{\alpha,R}.
\tag{15.672}
```

**Criterion 40.124 (Collar Inclusion Proves The Adjoint Collar Estimate).** If
(15.670)-(15.672) hold, then (15.511) holds with

```math
C_{\mathrm{cosmean}}(R)
=
C_{\mathrm{collar}}(R).
\tag{15.673}
```

#### Proof

Equation (15.511) is exactly the supremum of the adjoint character defect over
the finite collar loop family. Under (15.670) and (15.672), the observable in
(15.511) is the same observable controlled by Target 40.75. Taking the supremum
over the collar subfamily gives (15.671), which is (15.511) with the constant
(15.673). `∎`

If (15.672) is not adopted, then Next B is not solved by Target 40.75. The
remaining bridge is the raw-to-renormalized mismatch estimate:

```math
\sup_{\alpha\in\mathcal B_{\gamma,R}^{\mathrm{collar}}}
\Delta^{\mathrm{thinren}}_{\alpha,R}
\le
C_{\mathrm{collar}}^{\Delta}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.674}
```

Thus Next B is exhausted:

```math
\boxed{
\begin{array}{c}
\text{either the collar loops are included in the renormalized loop family,}\\[1mm]
\text{or the raw-to-renormalized collar mismatch must be proved,}\\[1mm]
\text{or large coset collar response remains as a fixed-IR obstruction.}
\end{array}}
\tag{15.675}
```

### 15.50. Target 40.125: Solving Next C By Relative Center Routing

Searchable Target-40.125 tag:

`V4P40-TARGET-40125-NEXT-C-CENTER-ROUTING`.

Next C asks whether center tethers are charged to the center-sheet disorder
channel rather than to the SO(3) coset response. This is a topological
compatibility check.

Let

```math
\mathcal N_R(\Sigma_\gamma)
\tag{15.676}
```

be the physical neighborhood of the Wilson spanning surface. Let the relative
center class of b in this neighborhood be

```math
[b]_{\gamma,R}
\in
H^2
\left(
\mathcal N_R(\Sigma_\gamma),
\partial\mathcal N_R(\Sigma_\gamma);
Z(SU(2))
\right).
\tag{15.677}
```

Let the center-sheet pairing be

```math
\Theta_{\gamma,R}(b)
:=
\left\langle
[b]_{\gamma,R},
[\Sigma_\gamma]
\right\rangle
\in
Z(SU(2)).
\tag{15.678}
```

The routing condition is:

```math
\Xi_S(b)
=
\chi_{1/2}
\left(
\Theta_{\gamma,R}(b)
\right)
\Xi_S^{\mathrm{out}}(b),
\tag{15.679}
```

where the outer factor is independent of the local center-tether class near the
disk, after the center-adapted coboundary part has been absorbed into link
center coordinates.

**Criterion 40.125 (Relative Center Routing Proves Next C).** Suppose:

```math
\boxed{
\begin{array}{ll}
\mathrm{C1:}
&
\text{local relative center coboundaries are absorbed by the section change},\\[1mm]
\mathrm{C2:}
&
\text{nontrivial relative center classes pair with the Wilson sheet by }(15.678),\\[1mm]
\mathrm{C3:}
&
\text{the cocycle amplitude is section-independent after this absorption},\\[1mm]
\mathrm{C4:}
&
\text{the center-sheet disorder estimate applies to }\Theta_{\gamma,R}(b).
\end{array}}
\tag{15.680}
```

Then center tethers are routed into the center-sheet factor and are not counted
as coset bad response.

#### Proof

C1 says that a local center coboundary changes only the arbitrary section used
to lift SO(3) data to SU(2). By the section-independence of the lift identity,
this change cannot alter the physical Wilson expectation except through the
explicit center factor. C2 identifies the nontrivial relative class with its
intersection pairing against the Wilson sheet. Therefore the local center
tether contributes precisely the factor displayed in (15.679). C3 ensures that
no hidden section-dependent center coordinate remains inside the SO(3) cocycle
amplitude. C4 is then exactly the existing center-disorder estimate for the
sheet variable. Hence the center-tether event is charged to the center channel,
not to the coset response budget. `∎`

The failure event for Next C is:

```math
\mathcal E^{\mathrm{cenroute}}_{\gamma,R}
:=
\left\{
\text{one of C1-C4 in }(15.680)\text{ fails}
\right\}.
\tag{15.681}
```

The required estimate is:

```math
\sup_{a<a_0}
\mu_{\mathrm{cen},a}^s
\left[
\mathcal E^{\mathrm{cenroute}}_{\gamma,R}
\right]
\le
p_{\mathrm{cenroute}}(R),
\tag{15.682}
```

with this routing probability inside the center-sheet polymer budget. If
(15.682) cannot be proved, then the Wilson route has found a genuine
incompatibility between the chosen local center resolution and the global
center-sheet disorder mechanism.

Thus Next C is exhausted:

```math
\boxed{
\begin{array}{c}
\text{prove C1-C4 and charge center tethers to the sheet variable,}\\[1mm]
\text{or prove that routing failures are summable,}\\[1mm]
\text{or accept a center-routing obstruction to the Wilson route.}
\end{array}}
\tag{15.683}
```

### 15.51. Target 40.126: Full Exhaustion After Target 40.116

Searchable Target-40.126 tag:

`V4P40-TARGET-40126-FULL-POST-40116-EXHAUSTION`.

The complete post-40.116 status is now a finite decision tree.

```math
\boxed{
\begin{array}{ll}
\mathrm{A:}
&
\text{Fredholm dual flux alternative }40.123,\\[1mm]
\mathrm{B:}
&
\text{collar-loop inclusion or bridge }40.124,\\[1mm]
\mathrm{C:}
&
\text{relative center routing }40.125.
\end{array}}
\tag{15.684}
```

**Theorem 40.126 (Post-40.116 Exhaustion).** At fixed physical R and fixed
physical smoothing radius, assume the earlier high-frequency smoothing and
nonlinear small-branch estimates used in Targets 40.105 and 40.111. Then the
branch after Target 40.116 is exhausted as follows.

PASS:

```math
\text{A passes, B passes, and C passes.}
\tag{15.685}
```

Then the mean-flux part of the fixed-IR flowed block package is reduced to the
existing conditional Poincare and center-disorder inputs.

FAIL-A:

```math
\text{there is a flux-visible reduced SO(3) soft mode.}
\tag{15.686}
```

FAIL-B:

```math
\text{large adjoint collar response survives at fixed physical scale.}
\tag{15.687}
```

FAIL-C:

```math
\text{relative center tethers cannot be routed into the center-sheet factor.}
\tag{15.688}
```

These alternatives are mutually complete for the post-40.116 branch.

#### Proof

Target 40.121 showed that Target 40.116 has only PASS-gap, PASS-factor, or
FAIL-low-mode outcomes. Target 40.123 resolves the PASS-factor branch by the
fixed-IR Fredholm alternative, or else identifies the flux-visible soft-mode
failure. Target 40.124 shows that the adjoint collar estimate needed by Target
40.98 is already a consequence of Target 40.75, provided the collar loop family
is included at physical resolution; otherwise the raw-to-renormalized bridge is
the exact missing estimate. Target 40.125 shows that center tethers are either
routed into the explicit center-sheet variable or become a routing obstruction.

There is no fourth post-40.116 mechanism: deterministic SO(3) stability is A,
finite physical adjoint collar response is B, and center/coset bookkeeping is C.
All remaining burdens are the already named global inputs: conditional Poincare,
renormalized Stokes control, and center-sheet disorder. `∎`

So the proof has reached the following fixed-IR floor:

```math
\boxed{
\begin{array}{c}
\text{The post-40.116 work no longer depends on microscopic UV smoothing.}\\[1mm]
\text{It depends on a fixed physical Fredholm calculation,}\\[1mm]
\text{a finite physical collar-loop moment bound,}\\[1mm]
\text{and a relative center-sheet routing theorem.}
\end{array}}
\tag{15.689}
```

### 15.52. Working Target 40.125: Relative Center Routing Proof

Searchable Target-40.125 proof tag:

`V4P40-TARGET-40125-RELATIVE-CENTER-ROUTING-PROOF`.

We now carry out the first next move: prove the center-routing statement as far
as topology can prove it. The proof is fixed-IR because the neighborhood of the
Wilson sheet is chosen at physical size before the cutoff is removed.

Let

```math
N_{\gamma,R}
:=
\mathcal N_R(\Sigma_\gamma)
\tag{15.690}
```

and let the local sheet be

```math
\Sigma_{\gamma,R}
:=
\Sigma_\gamma\cap N_{\gamma,R}.
\tag{15.691}
```

The center routing theorem applies on the center-Bianchi sector:

```math
\delta b=1
\quad
\text{on }N_{\gamma,R}.
\tag{15.692}
```

If (15.692) fails, there is a local center endpoint in the physical
neighborhood. That is not a coset response, but it is also not a routable sheet
class. It must be charged to the center defect budget.

Use multiplicative notation for center cochains. For any relative two-chain T,
define the pairing

```math
\left\langle b,T\right\rangle
:=
\prod_{p\in T}b_p.
\tag{15.693}
```

Because of (15.692), the value of (15.693) depends only on the relative
cohomology class of b and the relative homology class of T:

```math
\left\langle b,\partial K\right\rangle=1,
\qquad
\left\langle \delta\eta,T\right\rangle
=
\left\langle \eta,\partial T\right\rangle.
\tag{15.694}
```

For relative center coboundaries,

```math
b=\delta\eta,
\qquad
\eta\vert_{\partial N_{\gamma,R}}=1,
\tag{15.695}
```

the local sheet pairing is trivial:

```math
\left\langle b,\Sigma_{\gamma,R}\right\rangle=1.
\tag{15.696}
```

#### Theorem 40.127 (Local Center Coboundaries Have Trivial Sheet Pairing)

Assume (15.692). If (15.695) holds in the physical sheet neighborhood, then the
center-tether class contributes no independent Wilson sheet sign. Equivalently,
the local center coordinate may be absorbed into the center-adapted block
variables for routing purposes. This is not a claim that the action is invariant
under an arbitrary center one-form change; it is a statement about the Wilson
sheet pairing and the bookkeeping of the center channel.

#### Proof

Choose the link-center change

```math
z_\ell\longmapsto z_\ell\eta_\ell^{-1}
\tag{15.697}
```

inside the physical neighborhood, with eta equal to one on the relative
boundary. The plaquette center coordinate changes by

```math
b_p\longmapsto b_p(\delta\eta)_p^{-1}.
\tag{15.698}
```

Thus the relative coboundary part of b becomes trivial in the local
center-adapted representation. Since eta is one on the relative boundary, the
boundary Wilson sign produced by this local center change is trivial.
Equivalently, (15.694) gives (15.696).

The SO(3) variables are still the variables seen by the coset block problem.
The exact SU(2) lift identity remains valid before and after the
center-adapted rewrite, and the section-independence identity (15.29) ensures
that the full product

```math
\Xi_S(b)\,A^s_{C,S}(\bar U)
\tag{15.699}
```

does not acquire a section-dependent extra factor. Therefore a relative center
coboundary is not a center-sheet tether and should not be charged as a coset bad
response merely because it appears in the section-dependent plaquette
coordinate. Its remaining energetic effect, if any, belongs to the ordinary
center-adapted block kernel. `∎`

For a nontrivial relative class, define

```math
\Theta_{\gamma,R}(b)
:=
\left\langle
[b]_{\gamma,R},
[\Sigma_{\gamma,R}]
\right\rangle.
\tag{15.700}
```

The local center sheet factor splits as

```math
\left\langle b,\Sigma_{\gamma,R}\right\rangle
=
\Theta_{\gamma,R}(b).
\tag{15.701}
```

The full center sheet factor then decomposes into local and exterior parts:

```math
\Xi_S(b)
=
\Theta_{\gamma,R}(b)\,
\Xi^{\mathrm{out}}_{\gamma,R}(b),
\tag{15.702}
```

where

```math
\Xi^{\mathrm{out}}_{\gamma,R}(b)
:=
\prod_{p\in S\setminus\Sigma_{\gamma,R}}b_p
\tag{15.703}
```

after a fixed physical partition of the spanning surface.

#### Theorem 40.128 (Relative Class Routes To The Center Sheet)

Assume the center-Bianchi condition (15.692), the section-independence identity
(15.29), and the fixed physical surface split (15.691). Then the center-tether
event in the sheet neighborhood is routed exactly by (15.702). In particular,
local center coboundaries contribute trivially, and nontrivial relative center
classes contribute only through the center-sheet variable (15.700).

#### Proof

By (15.694), the local factor depends only on the relative class of b. If the
class is zero, Theorem 40.127 gives a trivial local contribution. If the class
is nonzero, its contribution is by definition the relative pairing (15.700).
Multiplying the local factor by the exterior plaquette product gives (15.702).
The section-dependent center coordinate cannot create an additional coset
charge, because (15.29) fixes the full product under all section changes. `∎`

Thus Target 40.125 passes, modulo the already named center-sheet disorder
estimate, on the sector

```math
\mathcal G^{\mathrm{route}}_{\gamma,R}
:=
\left\{
\delta b=1\text{ on }N_{\gamma,R}
\right\}
\cap
\left\{
\text{the center-sheet disorder estimate applies to }\Theta_{\gamma,R}(b)
\right\}.
\tag{15.704}
```

The exact failure event is

```math
\mathcal E^{\mathrm{route}}_{\gamma,R}
:=
\left(
\mathcal G^{\mathrm{route}}_{\gamma,R}
\right)^c.
\tag{15.705}
```

Therefore the completed routing alternative is:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS:}
&
\text{Theorem }40.128\text{ holds and }(15.704)\text{ has center-sheet disorder},\\[1mm]
\mathrm{FAIL:}
&
\text{the event }(15.705)\text{ is not summable in the center budget.}
\end{array}}
\tag{15.706}
```

This proves the invariant bookkeeping part of Next C. It does not by itself
prove center disorder. It proves that center tethers, when the center-Bianchi
law holds, belong to the center-sheet variable rather than to the SO(3) coset
bad-response budget.

### 15.53. Working Target 40.124: Collar-Loop Lock And Bridge

Searchable Target-40.124 proof tag:

`V4P40-TARGET-40124-COLLAR-LOOP-LOCK-BRIDGE`.

We now carry out the second next move. The adjoint collar estimate is solved if
the collar loop family is locked to the same physical-resolution loop family
used in Target 40.75.

Define the renormalized collar defect

```math
\Delta^{\mathrm{ren}}_{\mathrm{collar}}(R)
:=
\sup_{\alpha\in\mathcal B_{\gamma,R}^{\mathrm{collar}}}
\left[
1
-
\frac{1}{3}
\mathsf K^s_{R,a,b}
\left(
\chi_{\mathrm{ad}}
\left(
H^{\mathrm{ren}}_{\alpha,R}
\right)
\mid
\xi_-
\right)
\right].
\tag{15.707}
```

The locked collar convention is:

```math
\Delta_{\mathrm{cosmean}}(R)
:=
\Delta^{\mathrm{ren}}_{\mathrm{collar}}(R).
\tag{15.708}
```

#### Theorem 40.129 (Locked Collar Loops Prove The Adjoint Collar Estimate)

Assume the collar loops are included in the Target-40.75 physical loop family
and the locked convention (15.708) is used. If Target 40.75 gives

```math
\Delta^{\mathrm{ren}}_{\mathrm{collar}}(R)
\le
C_{\mathrm{collar}}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1),
\tag{15.709}
```

then the adjoint collar estimate (15.511) holds with

```math
C_{\mathrm{cosmean}}(R)
=
C_{\mathrm{collar}}(R).
\tag{15.710}
```

#### Proof

With the convention (15.708), the left side of (15.511) is exactly the left side
of (15.709). The constants are therefore identical. `∎`

If the route keeps raw thin collar holonomies, the exact bridge is the character
mismatch

```math
\Delta^{\mathrm{rawren}}_{\mathrm{collar}}(R)
:=
\sup_{\alpha\in\mathcal B_{\gamma,R}^{\mathrm{collar}}}
\mathsf K^s_{R,a,b}
\left[
\left|
\chi_{\mathrm{ad}}
\left(
\operatorname{Hol}_{\alpha}
\right)
-
\chi_{\mathrm{ad}}
\left(
H^{\mathrm{ren}}_{\alpha,R}
\right)
\right|
\mid
\xi_-
\right].
\tag{15.711}
```

#### Theorem 40.130 (Raw Collar Bridge)

Assume Target 40.75 gives (15.709), and suppose the mismatch estimate

```math
\Delta^{\mathrm{rawren}}_{\mathrm{collar}}(R)
\le
C_{\mathrm{rawren}}(R)g_{\mathrm{eff}}^2(R)
+
o_a(1)
\tag{15.712}
```

holds. Then the raw adjoint collar estimate (15.511) holds with

```math
C_{\mathrm{cosmean}}(R)
=
C_{\mathrm{collar}}(R)
+
\frac{1}{3}C_{\mathrm{rawren}}(R).
\tag{15.713}
```

#### Proof

For every collar loop alpha,

```math
\begin{aligned}
1
-
\frac{1}{3}
\mathsf K
\left[
\chi_{\mathrm{ad}}
\left(
\operatorname{Hol}_{\alpha}
\right)
\right]
&\le
1
-
\frac{1}{3}
\mathsf K
\left[
\chi_{\mathrm{ad}}
\left(
H^{\mathrm{ren}}_{\alpha,R}
\right)
\right]\\
&\quad
+
\frac{1}{3}
\mathsf K
\left[
\left|
\chi_{\mathrm{ad}}
\left(
\operatorname{Hol}_{\alpha}
\right)
-
\chi_{\mathrm{ad}}
\left(
H^{\mathrm{ren}}_{\alpha,R}
\right)
\right|
\right].
\end{aligned}
\tag{15.714}
```

Taking the supremum over the finite collar family and applying (15.709) and
(15.712) gives (15.713). `∎`

Thus Next B is now completely decided:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS\ locked:}
&
\text{use renormalized collar loops and Target }40.75,\\[1mm]
\mathrm{PASS\ bridge:}
&
\text{keep raw loops but prove }(15.712),\\[1mm]
\mathrm{FAIL:}
&
\text{neither route controls the collar character defect at fixed physical scale.}
\end{array}}
\tag{15.715}
```

For the fixed-IR paper, the clean choice is the locked route. It avoids asking
thin lattice holonomies to have continuum stability.

### 15.54. Working Target 40.123: Fredholm Kernel And Flux Orthogonality

Searchable Target-40.123 proof tag:

`V4P40-TARGET-40123-FREDHOLM-KERNEL-FLUX`.

We now carry out the third next move: compute what Target 40.123 really asks of
the reduced continuum operator.

At the flat center-adapted branch, the continuum reduced Hessian has the form

```math
L_R
=
d_R^*H_Rd_R
\tag{15.716}
```

on the gauge-fixed, tether-removed Dirichlet space, up to lower-order terms
which vanish at the flat branch or are absorbed into the fixed physical Hessian.
The principal coefficient satisfies

```math
\left\langle H_RF,F\right\rangle
\ge
m_R\left\|F\right\|_{0,R}^2.
\tag{15.717}
```

The geometric kernel condition is:

```math
u\in\ker L_R
\quad\Longrightarrow\quad
d_Ru=0
\quad
\text{in }N_{\gamma,R}.
\tag{15.718}
```

This is automatic if the only continuum kernel modes are flat reduced modes.
Those are either removed as coset tethers or are harmonic modes with no local
curvature.

The physical-resolution flux source factors through curvature:

```math
\Phi^{\mathrm{lin}}_{\gamma,R}(u)
=
\mathcal J_{\gamma,R}(d_Ru),
\tag{15.719}
```

where the linear map on the right is bounded at fixed smoothing radius:

```math
\left|
\mathcal J_{\gamma,R}(F)
\right|
\le
C_{\mathcal J}(R,\ell_R)
\left\|F\right\|_{0,N_{\gamma,R}}.
\tag{15.720}
```

#### Theorem 40.131 (Geometric Kernel Orthogonality Proves Next A)

Assume the Fredholm package (15.662), the geometric kernel condition (15.718),
and the flux factorization (15.719). Then

```math
j_{\gamma,R}
\perp
\ker L_R.
\tag{15.721}
```

Consequently Target 40.123 satisfies PASS-A, provided the discrete reduced
operators converge to the continuum reduced operator on the physical low band.

#### Proof

Let u be in the kernel of L_R. By (15.718), its curvature vanishes in the
physical neighborhood supporting the flux observable. Therefore (15.719) gives

```math
\Phi^{\mathrm{lin}}_{\gamma,R}(u)
=
\mathcal J_{\gamma,R}(0)
=
0.
\tag{15.722}
```

Since j is the covector representing the linearized flux,

```math
\left\langle j_{\gamma,R},u\right\rangle
=
\Phi^{\mathrm{lin}}_{\gamma,R}(u).
\tag{15.723}
```

Equations (15.722)-(15.723) prove (15.721). Criterion 40.123 then gives the
bounded dual solution and the PASS-factor line. `∎`

It remains to make the cutoff passage explicit. Let the discrete quadratic
forms be

```math
Q_{R,a}(u)
:=
\left\langle L_{R,a}u,u\right\rangle,
\qquad
Q_R(u)
:=
\left\langle L_Ru,u\right\rangle.
\tag{15.724}
```

The needed convergence is Mosco convergence on the reduced physical space:

```math
Q_{R,a}
\xrightarrow{\mathrm{Mosco}}
Q_R.
\tag{15.725}
```

Together with convergence of the flux sources,

```math
j_{\gamma,R,a}
\longrightarrow
j_{\gamma,R}
\quad
\text{in the dual physical norm},
\tag{15.726}
```

Mosco convergence gives strong resolvent convergence:

```math
\left(
L_{R,a}+P_{\ker,a}
\right)^{-1}
j_{\gamma,R,a}
\longrightarrow
\left(
L_R+P_{\ker}
\right)^{-1}
j_{\gamma,R}.
\tag{15.727}
```

Here the projections insert the identity on the kernel and do not affect the
orthogonal reduced solution.

#### Criterion 40.132 (Discrete Passage For The Fredholm Route)

If (15.725)-(15.727) hold and the continuum orthogonality (15.721) holds, then

```math
\sup_{a<a_0}
\left\|
L_{R,a}^{-1}j_{\gamma,R,a}
\right\|_{1,R,a}
<
\infty
\tag{15.728}
```

on the reduced orthogonal complement of the kernel. Therefore Target 40.120
satisfies PASS-dual.

#### Proof

The continuum inverse applied to j is bounded by Fredholm. Strong resolvent
convergence in (15.727) transfers that bounded solution to the discrete reduced
solutions. The source convergence (15.726) rules out a hidden discrete forcing
component that vanishes only weakly. This gives (15.728), which is exactly the
dual Green bound (15.639). `∎`

The exact fail mode is also now visible. If there exists

```math
u_0\in\ker L_R
\tag{15.729}
```

such that

```math
\Phi^{\mathrm{lin}}_{\gamma,R}(u_0)
\ne
0,
\tag{15.730}
```

then the flux source is not orthogonal to the kernel:

```math
P_{\ker L_R}j_{\gamma,R}
\ne
0.
\tag{15.731}
```

In that case Target 40.123 fails unless that kernel mode is reclassified as a
tether mode and removed from the reduced bulk space.

Thus Next A is reduced to a concrete fixed-IR computation:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS:}
&
\text{prove }(15.718),(15.719),(15.725),(15.726),\\[1mm]
\mathrm{FAIL:}
&
\text{find a continuum kernel mode with nonzero physical flux }(15.730),\\[1mm]
\mathrm{RECLASSIFY:}
&
\text{show the offending mode is actually a coset tether.}
\end{array}}
\tag{15.732}
```

This is the fixed physical IR version of the Feynman calculation: solve the
continuum reduced Hessian, inspect its kernel, and test the physical flux
source against that kernel before taking the cutoff limit.

### 15.55. Working Target 40.81: P1 And P6 For The Flowed Smoother

Searchable Target-40.81 P1/P6 tag:

`V4P40-TARGET-4081-P1-P6-FLOWED-SMOOTHER-LIPSCHITZ`.

We now return to Target 40.81 and attack P1 plus P6. The order of limits is
still fixed:

```math
R\text{ fixed},
\qquad
\ell_R\text{ fixed},
\qquad
s_R=\lambda_R\ell_R^2,
\qquad
a\downarrow0.
\tag{15.733}
```

The central issue is normalization. The flow must smooth at physical radius
ell R, not at a lattice-scale radius. Thus the lattice flow generator is assumed
to be parabolically normalized so that positive flow time s R corresponds to
physical smoothing radius ell R.

Let

```math
\mathscr S_{R,a}(\bar V)
:=
\bar V_{s_R}
\tag{15.734}
```

be the SO(3) Wilson-flow smoother.

#### 15.55.1. Exact Structural Part Of P1

**Theorem 40.133 (Wilson Flow Gives S1 And S3).** At every finite cutoff, the
SO(3) Wilson-flow smoother satisfies gauge covariance and energy dissipation:

```math
\mathscr S_{R,a}(g\bar Vg^{-1})
=
g\,\mathscr S_{R,a}(\bar V)\,g^{-1},
\tag{15.735}
```

and

```math
S_{\mathrm{SO3},a}(\bar V_{s_R})
+
\int_0^{s_R}
\left\|
\nabla S_{\mathrm{SO3},a}(\bar V_t)
\right\|^2dt
\le
S_{\mathrm{SO3},a}(\bar V).
\tag{15.736}
```

#### Proof

The SO(3) action is gauge invariant, hence its left-invariant gradient vector
field is gauge equivariant. By uniqueness of the finite-dimensional ODE
(15.410), the flow commutes with gauge transformations, proving (15.735).

Along the gradient flow,

```math
\frac{d}{dt}
S_{\mathrm{SO3},a}(\bar V_t)
=
-
\left\|
\nabla S_{\mathrm{SO3},a}(\bar V_t)
\right\|^2.
\tag{15.737}
```

Integrating (15.737) from zero to s R gives (15.736). `∎`

This proves the exact part of P1. The remaining part of P1 is not a symmetry
identity; it is a fixed-IR parabolic response estimate.

#### 15.55.2. Parabolic Locality Input

Let

```math
J_{R,a}(\ell,\ell';\bar V)
:=
\nabla_{\ell'}
\left(
\mathscr S_{R,a}(\bar V)
\right)_\ell
\tag{15.738}
```

be the Jacobian of the smoother. The physical heat-kernel response estimate is:

```math
\left\|
J_{R,a}(\ell,\ell';\bar V)
\right\|
\le
C_{\mathrm{heat}}(R,\ell_R)
\exp
\left(
-
c_{\mathrm{heat}}
\frac{
d(\ell,\ell')^2
}{
\ell_R^2
}
\right)
\omega_a(\ell,\ell'),
\tag{15.739}
```

where the lattice normalization factor omega is the one appropriate to the
chosen physical response norm, and the corresponding Schur bounds are
cutoff-uniform:

```math
\sup_{\ell}
\sum_{\ell'}
\left\|
J_{R,a}(\ell,\ell';\bar V)
\right\|
\le
C_J(R,\ell_R),
\tag{15.740}
```

and

```math
\sup_{\ell'}
\sum_{\ell}
\left\|
J_{R,a}(\ell,\ell';\bar V)
\right\|
\le
C_J(R,\ell_R).
\tag{15.741}
```

Equivalently, the smoother has a cutoff-uniform operator norm on the physical
link-response Hilbert space:

```math
\left\|
D\mathscr S_{R,a}(\bar V)
\right\|_{\ell^2_{\mathrm{phys}}\to\ell^2_{\mathrm{phys}}}
\le
C_J(R,\ell_R).
\tag{15.742}
```

**Criterion 40.134 (Physical Heat-Kernel Response Proves S2 And The Smoother
Part Of S4).** If (15.739)-(15.742) hold, then the Wilson-flow smoother
satisfies the physical locality estimate S2 and has cutoff-stable response in
the physical link-gradient norm.

#### Proof

Equation (15.739) is S2 with the response normalization made explicit. The
Schur bounds (15.740)-(15.741) give the operator norm (15.742). Therefore the
first variation of any physical-resolution observable after smoothing is
bounded by the first variation of that observable with respect to the smoothed
field, multiplied by C_J. This is exactly the response part of S4. `∎`

The failure mode is important:

```math
\boxed{
\begin{array}{c}
\text{if }s_R\text{ is not a physical positive flow time,}\\[1mm]
\text{or if the response norm is the raw unweighted microscopic link norm,}\\[1mm]
\text{then }(15.742)\text{ can fail and P1 is not a fixed-IR statement.}
\end{array}}
\tag{15.743}
```

This is where fixed physical IR enters P1. The smoothing radius is chosen before
the cutoff limit; the proof cannot use a lattice-scale smoothing radius.

The response norm in (15.742) must be the same norm used in the conditional
Dirichlet form. Equivalently, the Poincare Dirichlet form is read as

```math
\mathcal E^s_{R,a,b,\xi_-}(F,F)
=
\mathsf K^s_{R,a,b}
\left[
\left\|
DF
\right\|_{\ell^2_{\mathrm{phys}}}^2
\mid
\xi_-
\right].
```

If the paper keeps the raw unweighted microscopic link-gradient norm instead,
then the constants in P1 and P6 have to be checked in that raw norm. This is a
normalization lock, not a cosmetic choice.

#### 15.55.3. Physical Reconstruction Norms

Let a finite physical loop or disk observable be reconstructed from the smoothed
SO(3) field by a smooth gauge-covariant map

```math
\mathcal O_{\gamma,R,a}.
\tag{15.744}
```

For P1 and P6, the required reconstruction hypothesis is the cutoff-uniform
first-variation bound

```math
\sup_{a<a_0}
\sup_{\bar W}
\left\|
D\mathcal O_{\gamma,R,a}(\bar W)
\right\|_{\ell^2_{\mathrm{phys}}\to E_\gamma}
\le
C_{\mathcal O}(R,\ell_R),
\tag{15.745}
```

where E gamma is the finite-dimensional target space of the observable. For
renormalized holonomy,

```math
\mathcal O_{\gamma,R,a}(\bar W)
=
H^{\mathrm{ren}}_{\gamma,R}(\bar W).
\tag{15.746}
```

For renormalized flux,

```math
\mathcal O_{\gamma,R,a}(\bar W)
=
\Phi^{\mathrm{ren}}_{\gamma,R}(\bar W).
\tag{15.747}
```

The point of (15.745) is that the observable is physical-resolution. It is not
a raw product over an ever-growing unsmoothed lattice loop with uncontrolled
microscopic variation.

#### Theorem 40.135 (P1 Implies The Holonomy Response Bound S4)

Assume (15.742) for the smoother and (15.745) for the renormalized holonomy
reconstruction (15.746). Then

```math
\sup_{a<a_0}
\sum_{\ell'}
\left\|
\nabla_{\ell'}
H^{\mathrm{ren}}_{\gamma,R}
\right\|^2
\le
\left(
C_{\mathcal O}(R,\ell_R)
C_J(R,\ell_R)
\right)^2.
\tag{15.748}
```

Thus S4 holds for the finite physical loop family.

#### Proof

By the chain rule,

```math
DH^{\mathrm{ren}}_{\gamma,R}(\bar V)
=
D\mathcal O_{\gamma,R,a}
\left(
\mathscr S_{R,a}(\bar V)
\right)
\circ
D\mathscr S_{R,a}(\bar V).
\tag{15.749}
```

Taking the physical link-response norm and using (15.742) and (15.745) gives
(15.748). `∎`

This closes P1 subject to the physical heat-kernel response estimate and the
physical reconstruction bound.

#### 15.55.4. P6: Renormalized Flux Lipschitz Estimate

The flux version is the same calculation, but now the target is the conditional
Dirichlet form (15.425).

Assume the renormalized flux reconstruction satisfies

```math
\sup_{a<a_0}
\sup_{\bar W}
\left\|
D\Phi^{\mathrm{ren}}_{\gamma,R}(\bar W)
\right\|_{\ell^2_{\mathrm{phys}}\to\mathfrak{so}(3)}
\le
C_{\Phi}^{\mathrm{rec}}(R,\ell_R).
\tag{15.750}
```

Then the pointwise gradient bound after smoothing is

```math
\sum_{\ell'}
\left\|
\nabla_{\ell'}
\Phi^{\mathrm{ren}}_{\gamma,R}(\bar V)
\right\|^2
\le
\left(
C_{\Phi}^{\mathrm{rec}}(R,\ell_R)
C_J(R,\ell_R)
\right)^2.
\tag{15.751}
```

**Theorem 40.136 (Admissible Smoother Proves P6).** If (15.742) and (15.750)
hold, then the renormalized flux Lipschitz estimate (15.425) holds with

```math
L_{\gamma}^{\mathrm{ren}}(R,\ell_R)
=
\left(
C_{\Phi}^{\mathrm{rec}}(R,\ell_R)
C_J(R,\ell_R)
\right)^2.
\tag{15.752}
```

#### Proof

Apply the chain rule:

```math
D\Phi^{\mathrm{ren}}_{\gamma,R}(\bar V)
=
D\Phi^{\mathrm{ren}}_{\gamma,R}
\left(
\mathscr S_{R,a}(\bar V)
\right)
\circ
D\mathscr S_{R,a}(\bar V).
\tag{15.753}
```

The operator norm bound (15.742) and the reconstruction bound (15.750) give
(15.751). The conditional Dirichlet form in (15.425) is the conditional
expectation of the same squared link-gradient norm. Taking the expectation
therefore gives (15.425) with the constant (15.752). `∎`

#### 15.55.5. Completed P1/P6 Alternative

The P1/P6 part of Target 40.81 is therefore reduced to two concrete fixed-IR
analytic estimates:

```math
\boxed{
\begin{array}{ll}
\mathrm{A1:}
&
\text{physical heat-kernel response for the Wilson-flow smoother }(15.742),\\[1mm]
\mathrm{A2:}
&
\text{physical reconstruction bounds for holonomy and flux }(15.745),(15.750).
\end{array}}
\tag{15.754}
```

If A1 and A2 hold, then P1 and P6 in Target 40.81 hold. If A1 fails, the chosen
flow is not a fixed-IR admissible smoother. If A2 fails, the observable is still
too close to a raw microscopic loop or disk variable.

Thus the pass/fail statement is:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS:}
&
\text{prove }(15.742),(15.745),(15.750),\\[1mm]
\mathrm{FAIL}_{\mathrm{smooth}}
&
\text{positive flow time does not give cutoff-stable physical response},\\[1mm]
\mathrm{FAIL}_{\mathrm{obs}}
&
\text{the loop or flux reconstruction has divergent microscopic variation.}
\end{array}}
\tag{15.755}
```

This is the fixed physical IR content of P1 plus P6. The next target after this
is P2: flowed Stokes control for the same physical-resolution holonomy and flux
observables.

### 15.56. Working Target 40.81: P2 Flowed Stokes Control

Searchable Target-40.81 P2 tag:

`V4P40-TARGET-4081-P2-FLOWED-STOKES-CONTROL`.

We now attack P2. The deterministic goal is to prove (15.417)-(15.418) for the
same physical-resolution holonomy and flux observables used in P1 and P6.

The main caution is non-Abelian: a total disk flux by itself does not control a
loop holonomy unless the commutator and cancellation remainder is controlled.
Therefore P2 must include a Stokes-good chart, and the complement of that chart
is exactly the bad-chart event that P3 must later estimate.

#### 15.56.1. Same-Reconstruction Stokes Data

Use the flowed field from P1:

```math
\bar V^{\mathrm{ren}}
:=
\mathscr S_{R,a}(\bar V).
\tag{15.756}
```

Let a gauge-covariant physical reconstruction map produce a piecewise smooth
SO(3) connection on the physical sheet neighborhood:

```math
A^{\mathrm{ren}}_{R,a}
:=
\mathcal A_{R,a}
\left(
\bar V^{\mathrm{ren}}
\right).
\tag{15.757}
```

The renormalized holonomy is defined from this same reconstructed connection:

```math
H^{\mathrm{ren}}_{\gamma,R}
:=
\operatorname{Hol}_{\gamma}
\left(
A^{\mathrm{ren}}_{R,a}
\right).
\tag{15.758}
```

Let the basepoint-transported curvature density on the physical spanning disk
be

```math
K_{\gamma,R,a}(x)
:=
\operatorname{Ad}_{U_{x\to *}}
\left(
F_{A^{\mathrm{ren}}_{R,a}}(x)
\right).
\tag{15.759}
```

The renormalized Stokes flux is the first transported curvature term:

```math
\Phi^{\mathrm{ren}}_{\gamma,R}
:=
\int_{\Sigma_\gamma}
K_{\gamma,R,a}(x)\,dA_x.
\tag{15.760}
```

The curvature size controlling the non-Abelian remainder is

```math
\mathcal K_{\gamma,R,a}
:=
\int_{\Sigma_\gamma}
\left|
K_{\gamma,R,a}(x)
\right|\,dA_x.
\tag{15.761}
```

The same-reconstruction condition is essential:

```math
\boxed{
\begin{array}{c}
H^{\mathrm{ren}}_{\gamma,R}
\text{ and }
\Phi^{\mathrm{ren}}_{\gamma,R}
\text{ are computed from the same }A^{\mathrm{ren}}_{R,a}.
\end{array}}
\tag{15.762}
```

If (15.762) fails, P2 becomes a bridge problem rather than a Stokes theorem.

#### 15.56.2. Fixed-IR Non-Abelian Stokes Expansion

On the injectivity chart of SO(3), define

```math
\Omega_{\gamma,R,a}
:=
\log H^{\mathrm{ren}}_{\gamma,R}.
\tag{15.763}
```

The surface-ordered Stokes expansion has the form

```math
\Omega_{\gamma,R,a}
=
\Phi^{\mathrm{ren}}_{\gamma,R}
+
\mathcal M_{\gamma,R,a},
\tag{15.764}
```

where the Magnus remainder obeys the fixed-IR bound

```math
\left|
\mathcal M_{\gamma,R,a}
\right|
\le
C_{\mathrm{Mag}}(R,\ell_R)
\exp
\left(
C_{\mathrm{Mag}}(R,\ell_R)
\mathcal K_{\gamma,R,a}
\right)
\mathcal K_{\gamma,R,a}^2.
\tag{15.765}
```

**Theorem 40.137 (Fixed-IR Non-Abelian Stokes Expansion).** Suppose the
physical reconstruction (15.757) is gauge-covariant and has cutoff-uniform
smoothness at scale ell R. Then (15.763)-(15.765) hold on every field for which
the loop holonomy lies in the injectivity chart. The constants depend on the
physical geometry of gamma, the disk family, R, and ell R, but not on the
cutoff.

#### Proof

The non-Abelian Stokes theorem writes the loop holonomy as the surface-ordered
exponential of the transported curvature density (15.759). In the injectivity
chart, the logarithm of a surface-ordered exponential is given by the Magnus
expansion. The first term is the integral (15.760). Every higher term contains
at least two transported curvature insertions. Standard bounds for the Magnus
series on a fixed physical surface give (15.765). The smoothing radius and the
surface geometry are fixed before the cutoff limit, so the constants are
cutoff-independent. `∎`

#### 15.56.3. Stokes-Good Sector

Define the Stokes-good event by three deterministic requirements:

```math
\mathcal G^{\mathrm{St}}_{\gamma,R}
:=
\left\{
H^{\mathrm{ren}}_{\gamma,R}
\text{ lies in the injectivity chart}
\right\}
\cap
\left\{
\mathcal K_{\gamma,R,a}
\le
\rho_{\mathrm{St}}(R,\ell_R)
\right\}
\cap
\left\{
\mathcal K_{\gamma,R,a}
\le
C_{\mathrm{coh}}(R,\ell_R)
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|
\right\}.
\tag{15.766}
```

The corresponding bad-chart event is

```math
\mathcal B^{\mathrm{ren}}_{\gamma,R}
:=
\left(
\mathcal G^{\mathrm{St}}_{\gamma,R}
\right)^c.
\tag{15.767}
```

On the good event, choose rho St small enough that the exponential in (15.765)
is bounded by a fixed physical constant. Then

```math
\left|
\mathcal M_{\gamma,R,a}
\right|
\le
C_{\mathrm{St}}(R,\ell_R)
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|^2.
\tag{15.768}
```

The last condition in (15.766) is the coherence condition. It rules out the
case where the transported curvature has large cancellation in the first flux
while the non-Abelian commutator remainder remains visible.

#### 15.56.4. Deterministic P2 Inequality

Let

```math
D_{SO3}
:=
\sup_{h\in SO(3)}
d_{SO(3)}(h,1).
\tag{15.769}
```

On the injectivity chart there is a fixed constant c log such that

```math
d_{SO(3)}(h,1)^2
\le
c_{\log}
\left|
\log h
\right|^2.
\tag{15.770}
```

Define the Stokes remainder variable by

```math
\mathcal Q^{\mathrm{ren}}_{\gamma,R}
:=
2c_{\log}
\left|
\mathcal M_{\gamma,R,a}
\right|^2
\mathbf 1_{\mathcal G^{\mathrm{St}}_{\gamma,R}}
+
D_{SO3}^2
\mathbf 1_{\mathcal B^{\mathrm{ren}}_{\gamma,R}}.
\tag{15.771}
```

**Theorem 40.138 (Stokes-Good Fields Prove P2).** With the definitions above,
the flowed Stokes estimate (15.417)-(15.418) holds with

```math
C^{\mathrm{flux}}_{\gamma}(R,\ell_R)
=
2c_{\log},
\tag{15.772}
```

and with constants

```math
C^{\mathrm{com}}_{\gamma}(R,\ell_R)
=
2c_{\log}
\left(
C_{\mathrm{St}}(R,\ell_R)
\right)^2,
\qquad
C^{\mathrm{bad}}_{\gamma}(R,\ell_R)
=
D_{SO3}^2.
\tag{15.773}
```

#### Proof

On the good event, combine (15.763)-(15.764) with (15.770):

```math
d_{SO(3)}
\left(
H^{\mathrm{ren}}_{\gamma,R},
1
\right)^2
\le
c_{\log}
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
+
\mathcal M_{\gamma,R,a}
\right|^2.
\tag{15.774}
```

Using the elementary inequality

```math
\left|X+Y\right|^2
\le
2\left|X\right|^2
+
2\left|Y\right|^2
\tag{15.775}
```

gives (15.417) with the first term in (15.771). The good-event remainder is
bounded by (15.768), giving the quartic term in (15.418).

On the bad event, the metric diameter bound gives

```math
d_{SO(3)}
\left(
H^{\mathrm{ren}}_{\gamma,R},
1
\right)^2
\le
D_{SO3}^2.
\tag{15.776}
```

This is the second term in (15.771), and it gives the bad-chart term in
(15.418). `∎`

#### 15.56.5. Why The Bad-Chart Term Is Necessary

The coherence condition in (15.766) cannot be removed from P2. The obstruction
is the group commutator mechanism.

**Theorem 40.139 (Total Flux Alone Does Not Control Non-Abelian Holonomy).**
There are fixed physical transported curvature patterns with zero first flux
and nontrivial loop holonomy.

#### Proof

Choose two noncommuting Lie algebra elements X and Y. A surface-ordered product
with four small constant curvature packets in the order

```math
\exp(\varepsilon X)
\exp(\varepsilon Y)
\exp(-\varepsilon X)
\exp(-\varepsilon Y)
\tag{15.777}
```

has first transported flux zero. Its product is the group commutator:

```math
\exp(\varepsilon X)
\exp(\varepsilon Y)
\exp(-\varepsilon X)
\exp(-\varepsilon Y)
=
\exp
\left(
\varepsilon^2[X,Y]
+
O(\varepsilon^3)
\right).
\tag{15.778}
```

For nonzero commutator, the holonomy is nontrivial while the first flux
vanishes. Therefore an estimate of the form (15.417) with no commutator or
bad-chart remainder is false. `∎`

This theorem is not a separate model assumption. It is the deterministic reason
why the bad-chart term in P2 must include non-Abelian cancellation and
commutator incoherence.

#### 15.56.6. Completed P2 Alternative

The P2 part of Target 40.81 is now reduced to the following deterministic
package:

```math
\boxed{
\begin{array}{ll}
\mathrm{S1:}
&
\text{same-reconstruction condition }(15.762),\\[1mm]
\mathrm{S2:}
&
\text{fixed-IR Stokes/Magnus expansion }(15.763)\text{-}(15.765),\\[1mm]
\mathrm{S3:}
&
\text{Stokes-good coherence split }(15.766)\text{-}(15.767).
\end{array}}
\tag{15.779}
```

If S1-S3 hold, then P2 holds pointwise with constants independent of the
cutoff. The remaining probabilistic task is exactly P3:

```math
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|^4
\mid
\xi_-
\right]
\text{ and }
\mathsf K^s_{R,a,b}
\left[
\mathbf 1_{\mathcal B^{\mathrm{ren}}_{\gamma,R}}
\mid
\xi_-
\right].
\tag{15.780}
```

Thus the P2 pass/fail statement is:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS:}
&
\text{prove }(15.762),(15.765),(15.766),\\[1mm]
\mathrm{FAIL}_{\mathrm{bridge}}
&
\text{holonomy and flux are not built from the same reconstruction},\\[1mm]
\mathrm{FAIL}_{\mathrm{coh}}
&
\text{commutator/cancellation bad charts are not controlled by P3.}
\end{array}}
\tag{15.781}
```

This is fixed-IR aligned: the Stokes expansion is performed after physical
smoothing, on a physical disk, with constants depending on R and ell R but not
on the cutoff.

### 15.57. Working Target 40.81: P3 Fourth Moment And Bad-Chart Bounds

Searchable Target-40.81 P3 tag:

`V4P40-TARGET-4081-P3-FOURTH-MOMENT-BAD-CHART`.

We now attack P3. The target is the pair (15.419)-(15.420), but P2 has made the
meaning sharper: the bad-chart event includes non-Abelian cancellation and
commutator incoherence. This is the first place where the first transported
flux may be too lossy.

#### 15.57.1. Fourth Moment From Conditional Concentration

Let the conditional mean and centered flux be

```math
M_{\gamma,R}
:=
\mathsf K^s_{R,a,b}
\left[
\Phi^{\mathrm{ren}}_{\gamma,R}
\mid
\xi_-
\right],
\tag{15.782}
```

and

```math
X_{\gamma,R}
:=
\Phi^{\mathrm{ren}}_{\gamma,R}
-
M_{\gamma,R}.
\tag{15.783}
```

The fourth-moment estimate follows from a conditional fourth-concentration
input:

```math
\mathsf K^s_{R,a,b}
\left[
\left|
X_{\gamma,R}
\right|^4
\mid
\xi_-
\right]
\le
C^{(4),\mathrm{fluc}}_{\gamma}(R,\ell_R)
g_{\mathrm{eff}}^4(R)
+
o_a(1).
\tag{15.784}
```

Together with the mean-flux estimate

```math
\left|
M_{\gamma,R}
\right|^4
\le
C^{(4),\mathrm{mean}}_{\gamma}(R)
g_{\mathrm{eff}}^4(R)
+
o_a(1),
\tag{15.785}
```

this proves (15.419).

**Criterion 40.140 (Fourth Concentration Plus Mean Proves The Flux Fourth
Moment).** If (15.784)-(15.785) hold, then

```math
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|^4
\mid
\xi_-
\right]
\le
C^{(4)}_{\gamma}(R,\ell_R)
g_{\mathrm{eff}}^4(R)
+
o_a(1).
\tag{15.786}
```

#### Proof

Use

```math
\left|
X+M
\right|^4
\le
8\left|X\right|^4
+
8\left|M\right|^4.
\tag{15.787}
```

Then apply (15.784)-(15.785). `∎`

A sufficient way to prove (15.784) is a conditional sub-Gaussian estimate. For
every unit vector v in the Lie algebra, suppose

```math
\mathsf K^s_{R,a,b}
\left[
\exp
\left(
\lambda
\left\langle
v,
X_{\gamma,R}
\right\rangle
\right)
\mid
\xi_-
\right]
\le
\exp
\left(
\frac{\lambda^2}{2}
\sigma_{\gamma}^2(R,\ell_R)
g_{\mathrm{eff}}^2(R)
\right)
+
o_a(1).
\tag{15.788}
```

Then (15.784) follows with a constant depending only on the finite dimension of
the Lie algebra and on sigma gamma. This is stronger than Poincare. Poincare
alone gives a second moment; it does not by itself give the fourth scaling
needed in (15.419).

#### 15.57.2. Bad-Chart Split From P2

The P2 bad chart is

```math
\mathcal B^{\mathrm{ren}}_{\gamma,R}
=
\left(
\mathcal G^{\mathrm{St}}_{\gamma,R}
\right)^c.
\tag{15.789}
```

Using (15.766), split it into three pieces:

```math
\mathcal B^{\mathrm{ren}}_{\gamma,R}
\subset
\mathcal B^{\mathrm{inj}}_{\gamma,R}
\cup
\mathcal B^{\mathrm{size}}_{\gamma,R}
\cup
\mathcal B^{\mathrm{coh}}_{\gamma,R},
\tag{15.790}
```

where

```math
\mathcal B^{\mathrm{inj}}_{\gamma,R}
:=
\left\{
H^{\mathrm{ren}}_{\gamma,R}
\text{ is outside the injectivity chart}
\right\},
\tag{15.791}
```

```math
\mathcal B^{\mathrm{size}}_{\gamma,R}
:=
\left\{
\mathcal K_{\gamma,R,a}
>
\rho_{\mathrm{St}}(R,\ell_R)
\right\},
\tag{15.792}
```

and

```math
\mathcal B^{\mathrm{coh}}_{\gamma,R}
:=
\left\{
\mathcal K_{\gamma,R,a}
\le
\rho_{\mathrm{St}}(R,\ell_R),
\quad
\mathcal K_{\gamma,R,a}
>
C_{\mathrm{coh}}(R,\ell_R)
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|
\right\}.
\tag{15.793}
```

Choose rho St below the fixed injectivity threshold. Then

```math
\mathcal B^{\mathrm{inj}}_{\gamma,R}
\subset
\mathcal B^{\mathrm{size}}_{\gamma,R}.
\tag{15.794}
```

Thus only size and coherence remain.

#### 15.57.3. Size Tail

The physical curvature-size observable is

```math
\mathcal K_{\gamma,R,a}
=
\int_{\Sigma_\gamma}
\left|
K_{\gamma,R,a}(x)
\right|dA_x.
\tag{15.795}
```

Assume the fourth curvature-size moment

```math
\mathsf K^s_{R,a,b}
\left[
\mathcal K_{\gamma,R,a}^4
\mid
\xi_-
\right]
\le
C^{(4)}_{\mathcal K}(R,\ell_R)
g_{\mathrm{eff}}^4(R)
+
o_a(1).
\tag{15.796}
```

Then Markov gives

```math
\mathsf K^s_{R,a,b}
\left[
\mathbf 1_{\mathcal B^{\mathrm{size}}_{\gamma,R}}
\mid
\xi_-
\right]
\le
\frac{
C^{(4)}_{\mathcal K}(R,\ell_R)
}{
\rho_{\mathrm{St}}(R,\ell_R)^4
}
g_{\mathrm{eff}}^4(R)
+
o_a(1).
\tag{15.797}
```

For small physical effective coupling, this is stronger than the required
order in (15.420).

#### 15.57.4. Coherence Is The Real P3 Obstruction

The coherence event is different. It is not a large-field tail. It is a
first-flux cancellation event.

**Theorem 40.141 (First-Flux Moments Do Not Control Coherence Failure).** The
fourth moments of the first flux and curvature size do not imply a small
probability for (15.793).

#### Proof

Take a fixed physical surface and choose two transported curvature packets with
opposite Lie algebra values:

```math
K_1=\varepsilon X,
\qquad
K_2=-\varepsilon X.
\tag{15.798}
```

Then

```math
\Phi^{\mathrm{ren}}_{\gamma,R}=0,
\qquad
\mathcal K_{\gamma,R,a}=2\varepsilon |X|.
\tag{15.799}
```

For small epsilon, the size moment is of order epsilon to the fourth power, and
the first-flux fourth moment is zero. But the coherence failure event (15.793)
occurs whenever epsilon is nonzero. Therefore moment bounds for the first flux
and curvature size do not by themselves make the coherence-failure probability
small. `∎`

This is the hard lesson of P3. The first transported flux can vanish by
cancellation while the non-Abelian Stokes remainder is still a real physical
effect.

#### 15.57.5. Two Valid P3 Routes

There are now two honest fixed-IR routes.

**Route A: prove coherence rarity.** Add the direct estimate

```math
\mathsf K^s_{R,a,b}
\left[
\mathbf 1_{\mathcal B^{\mathrm{coh}}_{\gamma,R}}
\mid
\xi_-
\right]
\le
C^{\mathrm{coh}}_{\gamma}(R,\ell_R)
g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.800}
```

Together with (15.794) and (15.797), this proves the bad-chart estimate
(15.420).

**Route B: enrich the Stokes observable.** Do not require coherence rarity.
Instead, replace the first-flux-only Stokes control by a physical curvature-size
control. On the small-size event,

```math
d_{SO(3)}
\left(
H^{\mathrm{ren}}_{\gamma,R},
1
\right)^2
\le
C_{\mathcal K}(R,\ell_R)
\mathcal K_{\gamma,R,a}^2.
\tag{15.801}
```

Then Target 40.75 follows from the second moment

```math
\mathsf K^s_{R,a,b}
\left[
\mathcal K_{\gamma,R,a}^2
\mid
\xi_-
\right]
\le
C^{(2)}_{\mathcal K}(R,\ell_R)
g_{\mathrm{eff}}^2(R)
+
o_a(1),
\tag{15.802}
```

plus the size-tail estimate (15.797). This route changes the observable package
from first transported flux alone to the enriched Stokes observable

```math
\mathfrak S_{\gamma,R}^{\mathrm{ren}}
:=
\left(
\Phi^{\mathrm{ren}}_{\gamma,R},
\mathcal K_{\gamma,R,a}
\right).
\tag{15.803}
```

It remains fixed-IR because both entries are built from the same smoothed
physical connection at radius ell R.

#### 15.57.6. Completed P3 Alternative

The P3 part of Target 40.81 is therefore:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS}_{\mathrm{flux}}
&
\text{prove }(15.784),(15.785),(15.796),(15.800),\\[1mm]
\mathrm{PASS}_{\mathrm{enr}}
&
\text{use the enriched observable }(15.803)\text{ and prove }(15.802),(15.797),\\[1mm]
\mathrm{FAIL:}
&
\text{coherence failure has nonsummable probability and no enriched control.}
\end{array}}
\tag{15.804}
```

The first pass preserves the original first-flux formulation. The second pass
is the robust non-Abelian repair. The fail line is now precise: P3 fails only
if commutator/cancellation bad charts survive at fixed physical scale and
cannot be controlled by an enriched physical Stokes observable.

This is the fixed physical IR status of P3. No microscopic chart regularity is
being assumed; the question is whether the physical smoothed curvature field has
Gaussian fourth moments and whether first-flux cancellations are either rare or
explicitly included in the Stokes observable family.

### 15.58. Target 40.142: Enriched Fixed-IR Observable Package For P4/P5

Searchable Target-40.142 tag:

`V4P40-TARGET-40142-ENRICHED-FIXED-IR-P4-P5`.

P3 shows that the first transported flux alone may be too lossy for the
non-Abelian Stokes route. The fixed-IR repair is not to ask for microscopic
regularity. It is to freeze a finite physical observable family before proving
P4 and P5.

Define the enriched Stokes observable family by

```math
\mathfrak S_{\gamma,R}^{\mathrm{ren}}
:=
\left(
\Phi^{\mathrm{ren}}_{\gamma,R},
\mathcal K_{\gamma,R,a}
\right),
\tag{15.805}
```

for the finite physical loop and disk family used in Target 40.81. Both entries
are built from the same flowed reconstruction at physical radius ell R.

The live finite family is

```math
\mathcal O^{\mathrm{live}}_{R}
:=
\left\{
\Phi^{\mathrm{ren}}_{\gamma,R},
\mathcal K_{\gamma,R,a},
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|^2,
\mathcal K_{\gamma,R,a}^2
:
\gamma\in\mathcal L_R^{\mathrm{phys}}
\right\}.
\tag{15.806}
```

The point of (15.806) is discipline: P4 is not a Poincare inequality for an
undefined class of microscopic observables. It is a concentration statement for
a finite fixed physical family.

#### 15.58.1. Enriched P4

The enriched P4 input is the cutoff-uniform conditional concentration estimate:

```math
\operatorname{Var}_{\mathsf K^s_{R,a,b}(\cdot\mid\xi_-)}
\left(
F
\right)
\le
C_P^{\mathrm{enr}}(R,\ell_R)g_{\mathrm{eff}}^2(R)
\mathcal E^s_{R,a,b,\xi_-}(F,F)
+
o_a(1)
\tag{15.807}
```

for every observable

```math
F\in\mathcal O^{\mathrm{live}}_{R}.
\tag{15.808}
```

When F is Lie-algebra valued, (15.807) is applied to each component against a
fixed orthonormal basis, equivalently to each unit directional projection. The
family is still finite because the Lie algebra dimension and the physical loop
family are fixed before the cutoff limit.

For the fourth-moment route, the stronger optional input is the finite-family
sub-Gaussian bound

```math
\mathsf K^s_{R,a,b}
\left[
\exp
\left(
\lambda
\left(
F-\mathsf K^s_{R,a,b}[F\mid\xi_-]
\right)
\right)
\mid
\xi_-
\right]
\le
\exp
\left(
\frac{\lambda^2}{2}
\sigma_F^2(R,\ell_R)
g_{\mathrm{eff}}^2(R)
\right)
+
o_a(1).
\tag{15.809}
```

This stronger form implies the fourth moments required by P3 for the finite
physical family.

#### 15.58.2. Enriched P5

The enriched mean input is deliberately asymmetric. The route needs mean
neutrality for the signed Lie-algebra flux, but only moment control for the
nonnegative curvature-size observable:

```math
\left|
\mathsf K^s_{R,a,b}
\left[
\Phi^{\mathrm{ren}}_{\gamma,R}
\mid
\xi_-
\right]
\right|^2
\le
C_{\Phi}^{\mathrm{mean}}(R,\ell_R)g_{\mathrm{eff}}^2(R)
+
o_a(1),
\tag{15.810}
```

and

```math
\mathsf K^s_{R,a,b}
\left[
\mathcal K_{\gamma,R,a}^2
\mid
\xi_-
\right]
\le
C_{\mathcal K}^{(2)}(R,\ell_R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.811}
```

Equation (15.810) is the old P5 mean-flux burden. Equation (15.811) is the
enriched Stokes replacement for coherence rarity.

#### 15.58.3. Consequence For P3 And P4/P5

**Criterion 40.142 (Enriched P4/P5 Closes The P3-Enriched Route).** Suppose:

```math
\boxed{
\begin{array}{ll}
\mathrm{E1:}
&
\text{P1 and P6 hold for the enriched family }(15.806),\\[1mm]
\mathrm{E2:}
&
\text{P2 holds with the enriched Stokes alternative }(15.801),\\[1mm]
\mathrm{E3:}
&
\text{the concentration estimate }(15.807)\text{ or }(15.809)\text{ holds},\\[1mm]
\mathrm{E4:}
&
\text{the mean and size estimates }(15.810)\text{ and }(15.811)\text{ hold}.
\end{array}}
\tag{15.812}
```

Then the P3-enriched line in (15.804) holds, and the P4/P5 part of Target 40.81
is reduced to the finite physical observable family (15.806).

#### Proof

E1 gives cutoff-stable Dirichlet forms for the finite family. E3 gives
conditional fluctuation control for the same family in the same norm. E4
anchors the conditional mean of the signed flux and the second moment of the
curvature-size observable. The curvature-size second moment is exactly
(15.802), and the size-tail estimate follows from the fourth or sub-Gaussian
control in E3. Therefore the P3-enriched route holds. Since the family is
finite and physical before the cutoff limit, this also gives the P4/P5 package
needed by Target 40.81 for the enriched Stokes route. `∎`

#### 15.58.4. What Remains Hard

The hard remaining estimate is not Stokes geometry. It is the fixed-center
block concentration and mean problem for the finite physical family:

```math
\boxed{
\begin{array}{c}
\text{prove conditional concentration for }(15.806),\\[1mm]
\text{prove mean-flux neutrality for }\Phi^{\mathrm{ren}}_{\gamma,R},\\[1mm]
\text{prove curvature-size moment control for }\mathcal K_{\gamma,R,a}.
\end{array}}
\tag{15.813}
```

This is exactly where Targets 40.91 through 40.123 enter: the mean-flux term is
handled by source-minimizer neutrality, center routing, collar locking, and the
Fredholm kernel test. The curvature-size term is nonnegative and should be
handled by concentration or energy-response estimates, not by a cancellation
argument.

Thus Target 40.142 has the following pass/fail form:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS:}
&
\text{prove }(15.807)\text{ or }(15.809),\text{ plus }(15.810),(15.811),\\[1mm]
\mathrm{FAIL}_{\mathrm{conc}}
&
\text{fixed-center concentration fails for the finite physical family},\\[1mm]
\mathrm{FAIL}_{\mathrm{mean}}
&
\text{center-conditioned mean flux survives at fixed physical scale},\\[1mm]
\mathrm{FAIL}_{\mathrm{size}}
&
\text{physical curvature-size moments are not of order }g_{\mathrm{eff}}^2.
\end{array}}
\tag{15.814}
```

This keeps the proof fixed-IR aligned: all observables in (15.806) are
physical-resolution objects, and the cutoff limit is taken only after that
finite family and its response norm are fixed.

### 15.59. Target 40.143: Finite-Family Source Concentration

Searchable Target-40.143 tag:

`V4P40-TARGET-40143-FINITE-FAMILY-SOURCE-CONCENTRATION`.

Target 40.142 reduces P4/P5 to a finite family of physical observables. We now
attack the concentration part by source free energy. This is narrower than a
global Poincare theorem and is better aligned with the source-response
machinery used for mean flux.

Let

```math
\mathcal F_R^{\mathrm{scal}}
\tag{15.815}
```

be the finite scalar family obtained from (15.806) by taking all scalar
observables, all fixed orthonormal components of Lie-algebra-valued observables,
and all unit directional projections needed in the proof. For a nonsmooth
curvature-size observable, use a fixed physical smooth regularization and remove
the regularization only after the cutoff-uniform estimate is proved.

For

```math
F\in\mathcal F_R^{\mathrm{scal}},
\tag{15.816}
```

define the conditional source partition function

```math
Z_F(\lambda\mid b,\xi_-)
:=
\mathsf K^s_{R,a,b}
\left[
\exp
\left(
\lambda F
\right)
\mid
\xi_-
\right],
\tag{15.817}
```

and the source free energy

```math
\Psi_F(\lambda\mid b,\xi_-)
:=
\log Z_F(\lambda\mid b,\xi_-).
\tag{15.818}
```

At finite cutoff,

```math
\Psi_F'(0\mid b,\xi_-)
=
\mathsf K^s_{R,a,b}
\left[
F\mid\xi_-
\right],
\tag{15.819}
```

and

```math
\Psi_F''(\lambda\mid b,\xi_-)
=
\operatorname{Var}_{\mathsf K^{s,\lambda F}_{R,a,b}(\cdot\mid\xi_-)}
\left(
F
\right),
\tag{15.820}
```

where the tilted conditional kernel is

```math
d\mathsf K^{s,\lambda F}_{R,a,b}
=
\frac{
\exp(\lambda F)
}{
Z_F(\lambda\mid b,\xi_-)
}
d\mathsf K^s_{R,a,b}.
\tag{15.821}
```

#### 15.59.1. Source Hessian Criterion

The finite-family source concentration target is:

```math
\sup_{\substack{
F\in\mathcal F_R^{\mathrm{scal}}\\
|\lambda|\le\lambda_0/g_{\mathrm{eff}}(R)\\
b,\xi_-
}}
\Psi_F''(\lambda\mid b,\xi_-)
\le
\sigma_{\mathrm{src}}^2(R,\ell_R)
g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.822}
```

The supremum is over admissible center fields and frontier-good incoming
collars.

**Criterion 40.143 (Source Hessian Bound Proves Finite-Family Concentration).**
If (15.822) holds, then for every F in the finite scalar family and every
lambda in the same source window,

```math
\mathsf K^s_{R,a,b}
\left[
\exp
\left(
\lambda
\left(
F-\mathsf K^s_{R,a,b}[F\mid\xi_-]
\right)
\right)
\mid
\xi_-
\right]
\le
\exp
\left(
\frac{\lambda^2}{2}
\sigma_{\mathrm{src}}^2(R,\ell_R)
g_{\mathrm{eff}}^2(R)
\right)
+
o_a(1).
\tag{15.823}
```

Consequently the enriched P4 sub-Gaussian input (15.809) holds for the finite
physical family.

#### Proof

For fixed F, write

```math
\Psi_F(\lambda)-\Psi_F(0)-\lambda\Psi_F'(0)
=
\int_0^\lambda
(\lambda-t)
\Psi_F''(t)\,dt.
\tag{15.824}
```

Use (15.822) inside the source window. The left side of (15.824) is the
logarithm of the centered moment generating function. This gives (15.823). `∎`

Thus P4 is reduced to a source-Hessian estimate for a finite physical family.

#### 15.59.2. Tilted Poincare Route

One way to prove (15.822) is a tilted conditional Poincare estimate. Suppose
for every F in the finite scalar family and every source in the window,

```math
\operatorname{Var}_{\mathsf K^{s,\lambda F}_{R,a,b}(\cdot\mid\xi_-)}
(G)
\le
C_P^{\mathrm{tilt}}(R,\ell_R)
g_{\mathrm{eff}}^2(R)
\mathcal E^{s,\lambda F}_{R,a,b,\xi_-}(G,G)
+
o_a(1)
\tag{15.825}
```

for

```math
G=F.
\tag{15.826}
```

Assume also the source-uniform Dirichlet bound

```math
\sup_{\substack{
F\in\mathcal F_R^{\mathrm{scal}}\\
|\lambda|\le\lambda_0/g_{\mathrm{eff}}(R)\\
b,\xi_-
}}
\mathcal E^{s,\lambda F}_{R,a,b,\xi_-}(F,F)
\le
L_{\mathrm{live}}(R,\ell_R)
+
o_a(1).
\tag{15.827}
```

Then (15.822) holds with

```math
\sigma_{\mathrm{src}}^2(R,\ell_R)
=
C_P^{\mathrm{tilt}}(R,\ell_R)
L_{\mathrm{live}}(R,\ell_R).
\tag{15.828}
```

This is the Poincare route, but now it is finite-family and source-local rather
than global.

#### 15.59.3. Brascamp-Lieb Route

A second route is classical convexity of the source-deformed block action. Let

```math
\mathcal A_{F,\lambda}(\bar V\mid b,\xi_-)
:=
\mathcal A_0(\bar V\mid b,\xi_-)
-
\lambda F(\bar V).
\tag{15.829}
```

Suppose the source-deformed Hessian on the reduced block variables satisfies

```math
D^2\mathcal A_{F,\lambda}
\ge
\kappa_{\mathrm{src}}(R)
g_{\mathrm{eff}}^{-2}(R)
I_{\mathrm{phys}}
\tag{15.830}
```

on the physical chart, uniformly for F in the finite family and lambda in the
source window, after gauge and tether modes are removed. Suppose also

```math
\left\|
DF
\right\|_{\mathrm{phys}}^2
\le
L_{\mathrm{live}}(R,\ell_R).
\tag{15.831}
```

Then the Brascamp-Lieb inequality gives

```math
\Psi_F''(\lambda\mid b,\xi_-)
\le
\frac{
L_{\mathrm{live}}(R,\ell_R)
}{
\kappa_{\mathrm{src}}(R)
}
g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.832}
```

Hence (15.822) holds.

This route is strong but fragile: it requires convexity of the tilted action in
the source window. If source tilting pushes the minimizer out of the physical
chart, the route fails and the failure is a fixed-IR response obstruction.

#### 15.59.4. Source-Visible Soft-Mode Failure

The exact failure mode is a source-visible soft direction. If there are reduced
directions u_a with

```math
\left\|u_a\right\|_{\mathrm{phys}}=1,
\qquad
\left\langle
L_{R,a}u_a,u_a
\right\rangle
\longrightarrow0,
\tag{15.833}
```

and some live observable F with

```math
\left|
DF(u_a)
\right|
\ge
\eta_R>0,
\tag{15.834}
```

then the source Hessian cannot satisfy (15.822) unless the direction is
reclassified as a tether or removed from the reduced block space.

#### Proof

In a Gaussian quadratic approximation, the variance of F in the direction u_a
contains the term

```math
\frac{
\left|
DF(u_a)
\right|^2
}{
\left\langle
L_{R,a}u_a,u_a
\right\rangle
}.
\tag{15.835}
```

Equations (15.833)-(15.834) make this term diverge. The same obstruction
appears in the second derivative of the exact source free energy by local
Laplace comparison along the soft direction, unless nonlinear effects remove
the branch from the fixed physical chart. `∎`

#### 15.59.5. Completed Target 40.143

Target 40.143 is therefore:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS}_{\mathrm{src}}
&
\text{prove the source Hessian bound }(15.822),\\[1mm]
\mathrm{PASS}_{\mathrm{tilt}}
&
\text{prove tilted Poincare plus response }(15.825)\text{-}(15.827),\\[1mm]
\mathrm{PASS}_{\mathrm{BL}}
&
\text{prove source convexity and response }(15.830)\text{-}(15.831),\\[1mm]
\mathrm{FAIL}
&
\text{exhibit a live-observable soft mode }(15.833)\text{-}(15.834).
\end{array}}
\tag{15.836}
```

If any pass line holds, then the finite-family concentration input (15.809)
holds, and Target 40.142 reduces the remaining P4/P5 work to the mean-flux and
curvature-size estimates (15.810)-(15.811). If the fail line holds, the enriched
fixed-IR route has found a genuine physical SO(3) response mode.

### 15.60. Target 40.144: Curvature-Size And Mean Anchors

Searchable Target-40.144 tag:

`V4P40-TARGET-40144-CURVATURE-SIZE-MEAN-ANCHORS`.

Target 40.143 controls centered fluctuations for the finite enriched family.
The remaining anchors are:

```math
\left|
\mathsf K^s_{R,a,b}
\left[
\Phi^{\mathrm{ren}}_{\gamma,R}
\mid
\xi_-
\right]
\right|^2
\le
C_{\Phi}^{\mathrm{mean}}(R,\ell_R)g_{\mathrm{eff}}^2(R)
+
o_a(1),
\tag{15.837}
```

and

```math
\mathsf K^s_{R,a,b}
\left[
\mathcal K_{\gamma,R,a}^2
\mid
\xi_-
\right]
\le
C_{\mathcal K}^{(2)}(R,\ell_R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.838}
```

The size anchor is positive and geometric. The mean anchor is signed and uses
the source-minimizer route.

#### 15.60.1. Curvature Size From Flowed Surface Energy

Let the flowed surface curvature energy be

```math
\mathcal E^{\mathrm{surf}}_{\gamma,R,a}
:=
\int_{\Sigma_\gamma}
\left|
K_{\gamma,R,a}(x)
\right|^2dA_x.
\tag{15.839}
```

By Cauchy-Schwarz on the fixed physical disk,

```math
\mathcal K_{\gamma,R,a}^2
=
\left(
\int_{\Sigma_\gamma}
\left|
K_{\gamma,R,a}(x)
\right|dA_x
\right)^2
\le
|\Sigma_\gamma|
\mathcal E^{\mathrm{surf}}_{\gamma,R,a}.
\tag{15.840}
```

Thus the desired size anchor follows from the flowed surface-energy estimate

```math
\mathsf K^s_{R,a,b}
\left[
\mathcal E^{\mathrm{surf}}_{\gamma,R,a}
\mid
\xi_-
\right]
\le
C_{\mathrm{surf}}(R,\ell_R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.841}
```

**Criterion 40.144 (Flowed Surface Energy Proves The Size Anchor).** If
(15.841) holds uniformly over admissible center fields and frontier-good
incoming collars, then (15.838) holds with

```math
C_{\mathcal K}^{(2)}(R,\ell_R)
=
|\Sigma_\gamma|
C_{\mathrm{surf}}(R,\ell_R).
\tag{15.842}
```

#### Proof

Take the conditional expectation of (15.840) and use (15.841). `∎`

The estimate (15.841) is fixed-IR only if the curvature in (15.839) is the
flowed physical curvature from the same reconstruction used in P1-P3. A
microscopic unflowed surface energy would not be a fixed-IR observable.

#### 15.60.2. Flowed Surface Energy From A Physical Trace Bound

There is a standard way to reduce (15.841) to a physical block-energy estimate.
Let

```math
N_{\ell_R}(\Sigma_\gamma)
\tag{15.843}
```

be a physical tube around the disk. The flowed trace estimate is

```math
\mathcal E^{\mathrm{surf}}_{\gamma,R,a}
\le
C_{\mathrm{tr}}(R,\ell_R)
\int_{N_{\ell_R}(\Sigma_\gamma)}
\left|
F_{A^{\mathrm{ren}}_{R,a}}(y)
\right|^2dy.
\tag{15.844}
```

Assume the flowed block-energy estimate

```math
\mathsf K^s_{R,a,b}
\left[
\int_{N_{\ell_R}(\Sigma_\gamma)}
\left|
F_{A^{\mathrm{ren}}_{R,a}}(y)
\right|^2dy
\mid
\xi_-
\right]
\le
C_{\mathrm{blkE}}(R,\ell_R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.845}
```

Then (15.841) holds with

```math
C_{\mathrm{surf}}(R,\ell_R)
=
C_{\mathrm{tr}}(R,\ell_R)
C_{\mathrm{blkE}}(R,\ell_R).
\tag{15.846}
```

This is the clean positive route for the enriched Stokes repair. It asks for
flowed physical curvature energy in a fixed tube, not microscopic plaquette
regularity.

#### 15.60.3. Mean Anchor From The Source-Minimizer Route

The signed flux anchor (15.837) cannot be proved from concentration alone. It
is exactly the mean-flux problem already isolated in Targets 40.91 through
40.123.

Let the exact conditional mean be

```math
M_{\gamma,R}^{\Phi}(b,\xi_-)
:=
\mathsf K^s_{R,a,b}
\left[
\Phi^{\mathrm{ren}}_{\gamma,R}
\mid
\xi_-
\right].
\tag{15.847}
```

The mean anchor follows if the source-minimizer package proves

```math
\left|
M_{\gamma,R}^{\Phi}(b,\xi_-)
\right|
\le
C_{\mathrm{anch}}(R,\ell_R)g_{\mathrm{eff}}(R)
+
o_a(1).
\tag{15.848}
```

The fixed-IR dependency chain is:

```math
\boxed{
\begin{array}{c}
\text{center routing }40.125,\\[1mm]
\text{collar loop lock }40.124,\\[1mm]
\text{Fredholm kernel orthogonality }40.123,\\[1mm]
\text{source-minimizer neutrality }40.91
\end{array}}
\quad
\Longrightarrow
\quad
(15.848).
\tag{15.849}
```

**Criterion 40.145 (Source-Minimizer Package Proves The Mean Anchor).** If the
four ingredients in (15.849) hold for the same physical reconstruction and
smoothing radius used in the enriched observable family, then (15.837) holds
with

```math
C_{\Phi}^{\mathrm{mean}}(R,\ell_R)
=
\left(
C_{\mathrm{anch}}(R,\ell_R)
\right)^2.
\tag{15.850}
```

#### Proof

The source-minimizer package gives the linear bound (15.848). Squaring it gives
(15.837), after absorbing the cutoff error. The same-reconstruction condition
is necessary so that the flux appearing in the mean anchor is the same
physical-resolution flux controlled by the Fredholm and collar estimates. `∎`

#### 15.60.4. Anchor Failure Modes

The curvature-size anchor fails only if the fixed physical flowed curvature
energy is too large:

```math
\limsup_{a\downarrow0}
g_{\mathrm{eff}}^{-2}(R)
\mathsf K^s_{R,a,b}
\left[
\mathcal E^{\mathrm{surf}}_{\gamma,R,a}
\mid
\xi_-
\right]
=
\infty.
\tag{15.851}
```

The mean anchor fails only if there is a source-visible mean response not routed
as a center tether, coset tether, or Fredholm soft-mode obstruction:

```math
\limsup_{a\downarrow0}
g_{\mathrm{eff}}^{-1}(R)
\left|
M_{\gamma,R}^{\Phi}(b,\xi_-)
\right|
=
\infty
\tag{15.852}
```

on frontier-good data outside the charged tether sectors.

#### 15.60.5. Completed Target 40.144

Target 40.144 is:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS}_{\mathrm{size}}
&
\text{prove the flowed surface-energy estimate }(15.841),\\[1mm]
\mathrm{PASS}_{\mathrm{energy}}
&
\text{prove the tube-energy estimate }(15.845),\\[1mm]
\mathrm{PASS}_{\mathrm{mean}}
&
\text{prove the source-minimizer chain }(15.849),\\[1mm]
\mathrm{FAIL}_{\mathrm{size}}
&
\text{the physical curvature-size anchor fails by }(15.851),\\[1mm]
\mathrm{FAIL}_{\mathrm{mean}}
&
\text{the signed mean-flux anchor fails by }(15.852).
\end{array}}
\tag{15.853}
```

If the size and mean pass lines hold, then Target 40.142 has its anchors
(15.810)-(15.811). Together with Target 40.143, this supplies the enriched
P4/P5 package needed by Target 40.81. If either fail line holds, the obstruction
is fixed-IR and physical: excessive flowed curvature energy or a surviving
center-conditioned mean flux.

### 15.61. Target 40.146: Flowed Tube-Energy Estimate

Searchable Target-40.146 tag:

`V4P40-TARGET-40146-FLOWED-TUBE-ENERGY-ESTIMATE`.

We now attack the positive size anchor by proving or reducing (15.845). The
object is the flowed physical tube energy

```math
\mathcal E^{\mathrm{tube}}_{\gamma,R,a}
:=
\int_{N_{\ell_R}(\Sigma_\gamma)}
\left|
F_{A^{\mathrm{ren}}_{R,a}}(y)
\right|^2dy.
\tag{15.854}
```

The target is

```math
\mathsf K^s_{R,a,b}
\left[
\mathcal E^{\mathrm{tube}}_{\gamma,R,a}
\mid
\xi_-
\right]
\le
C_{\mathrm{tube}}(R,\ell_R)g_{\mathrm{eff}}^2(R)
+
o_a(1),
\tag{15.855}
```

uniformly over admissible center fields and frontier-good incoming collars.
This is the same estimate as (15.845), with the tube energy named explicitly.

#### 15.61.1. Flowed Energy-Action Comparison

Let

```math
N_{2\ell_R}(\Sigma_\gamma)
\tag{15.856}
```

be a slightly thicker physical tube. Let

```math
\mathcal A^{\mathrm{loc}}_{2\ell_R}(\bar V\mid b,\xi_-)
\tag{15.857}
```

be the dimensionless local block action contribution in that tube, including
the fixed-center plaquette weights and the collar constraints. The required
comparison is

```math
\mathcal E^{\mathrm{tube}}_{\gamma,R,a}
\le
C_{\mathrm{EA}}(R,\ell_R)
g_{\mathrm{eff}}^2(R)
\mathcal A^{\mathrm{loc}}_{2\ell_R}(\bar V\mid b,\xi_-)
+
\mathcal R^{\mathrm{flow}}_{\gamma,R,a}.
\tag{15.858}
```

Here the residual is the finite-speed or tail contribution from flow locality:

```math
\mathsf K^s_{R,a,b}
\left[
\mathcal R^{\mathrm{flow}}_{\gamma,R,a}
\mid
\xi_-
\right]
\le
r_{\mathrm{flow}}(R,\ell_R,a)g_{\mathrm{eff}}^2(R),
\qquad
r_{\mathrm{flow}}(R,\ell_R,a)\longrightarrow0.
\tag{15.859}
```

The factor g effective squared in (15.858) is not cosmetic. The local action is
dimensionless and contains the inverse-coupling weight; the physical curvature
energy is the corresponding unweighted flowed energy.

#### 15.61.2. Conditional Local Action-Excess Bound

The second input is a fixed-IR local action-excess estimate:

```math
\mathsf K^s_{R,a,b}
\left[
\mathcal A^{\mathrm{loc}}_{2\ell_R}(\bar V\mid b,\xi_-)
\mid
\xi_-
\right]
\le
C_{\mathrm{locA}}(R,\ell_R)
+
o_a(1).
\tag{15.860}
```

This is an ordinary finite physical block estimate. It does not say that
microscopic action density is uniformly bounded pointwise. It says that the
conditional expected dimensionless action in a fixed physical tube is finite
after the block kernel integrates microscopic fluctuations.

**Criterion 40.146 (Energy-Action Comparison Proves The Tube Estimate).** If
(15.858)-(15.860) hold, then (15.855) holds with

```math
C_{\mathrm{tube}}(R,\ell_R)
=
C_{\mathrm{EA}}(R,\ell_R)
C_{\mathrm{locA}}(R,\ell_R)
\tag{15.861}
```

after increasing the constant to absorb the vanishing flow residual.

#### Proof

Take the conditional expectation of (15.858). Use (15.859) and (15.860). This
gives

```math
\mathsf K^s_{R,a,b}
\left[
\mathcal E^{\mathrm{tube}}_{\gamma,R,a}
\mid
\xi_-
\right]
\le
\left(
C_{\mathrm{EA}}(R,\ell_R)
C_{\mathrm{locA}}(R,\ell_R)
+
r_{\mathrm{flow}}(R,\ell_R,a)
\right)
g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.862}
```

Absorb the vanishing residual into the constant. `∎`

#### 15.61.3. Why Flowed Energy Is Essential

The estimate would be false as a fixed-IR statement if the left side were
replaced by an unflowed microscopic tube energy. The number of microscopic
plaquettes in the physical tube diverges as the cutoff is removed, and ordinary
short-distance fluctuations are part of the block measure. The flowed field
removes that UV fluctuation entropy before the physical energy is measured.

The correct locality statement is:

```math
\boxed{
\begin{array}{c}
\text{flow first at physical radius }\ell_R,\\[1mm]
\text{reconstruct the physical curvature},\\[1mm]
\text{then measure energy in a fixed physical tube.}
\end{array}}
\tag{15.863}
```

This is exactly the same fixed-IR order used in P1-P3.

#### 15.61.4. Alternative Source Route For Positive Energy

The tube-energy estimate can also be proved by a positive source bound. Define

```math
Z_{\mathrm{tube}}(\theta\mid b,\xi_-)
:=
\mathsf K^s_{R,a,b}
\left[
\exp
\left(
\theta g_{\mathrm{eff}}^{-2}(R)
\mathcal E^{\mathrm{tube}}_{\gamma,R,a}
\right)
\mid
\xi_-
\right].
\tag{15.864}
```

If there is a positive source window

```math
0\le\theta\le\theta_0(R,\ell_R)
\tag{15.865}
```

such that

```math
\log Z_{\mathrm{tube}}(\theta\mid b,\xi_-)
\le
C_{\mathrm{tube,src}}(R,\ell_R)\theta
+
o_a(1),
\tag{15.866}
```

then differentiating at the origin gives

```math
\mathsf K^s_{R,a,b}
\left[
\mathcal E^{\mathrm{tube}}_{\gamma,R,a}
\mid
\xi_-
\right]
\le
C_{\mathrm{tube,src}}(R,\ell_R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.867}
```

This is equivalent in force to (15.855), but it may be easier to prove by
comparing the source-deformed action with the undeformed local action.

#### 15.61.5. Failure Mode

The fixed-IR failure mode is a center-conditioned tube-energy excitation:

```math
\limsup_{a\downarrow0}
g_{\mathrm{eff}}^{-2}(R)
\mathsf K^s_{R,a,b}
\left[
\mathcal E^{\mathrm{tube}}_{\gamma,R,a}
\mid
\xi_-
\right]
=
\infty.
\tag{15.868}
```

If (15.868) occurs on frontier-good data, then the enriched Stokes route fails
through physical curvature energy, not through a bookkeeping error in the
center/coset split.

#### 15.61.6. Completed Target 40.146

Target 40.146 is:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS}_{\mathrm{EA}}
&
\text{prove energy-action comparison }(15.858)\text{ and local action }(15.860),\\[1mm]
\mathrm{PASS}_{\mathrm{src}}
&
\text{prove the positive tube-energy source bound }(15.866),\\[1mm]
\mathrm{FAIL}
&
\text{exhibit the fixed-IR tube-energy divergence }(15.868).
\end{array}}
\tag{15.869}
```

If either pass line holds, then (15.845) holds, hence Criterion 40.144 proves
the curvature-size anchor (15.838). This closes the positive half of Target
40.144 and leaves the signed mean-flux anchor as the remaining part of the
enriched P4/P5 package.

### 15.62. Target 40.147: Signed Mean-Flux Anchor From Source-Minimizer Neutrality

Searchable Target-40.147 tag:

`V4P40-TARGET-40147-SIGNED-MEAN-FLUX-ANCHOR`.

The remaining anchor is the signed estimate, not the positive energy estimate.
This is the delicate point. A Poincare or source Hessian bound controls
fluctuations around a conditional mean; it does not by itself say that the
conditional mean is small. A center-conditioned classical bias could still
survive unless the mean is tied to the same physical minimizer problem already
studied in Targets 40.91, 40.123, 40.124, and 40.125.

The first requirement is therefore a same-reconstruction condition:

```math
\Phi^{\mathrm{ren}}_{\gamma,R}
=
\Phi^{\mathrm{ren},\mathrm{Stokes}}_{\gamma,R}
=
\Phi^{\mathrm{ren},\mathrm{mean}}_{\gamma,R}.
\tag{15.870}
```

The flux appearing in the enriched Stokes estimate, the finite-family source
estimate, and the mean-flux anchor must be the same flowed physical observable.
No microscopic plaquette flux is allowed to replace it after the estimates have
been proved.

Recall the signed conditional mean:

```math
M^{\Phi}_{\gamma,R}(b,\xi_-)
:=
\mathsf K^s_{R,a,b}
\left[
\Phi^{\mathrm{ren}}_{\gamma,R}
\mid
\xi_-
\right].
\tag{15.871}
```

The target estimate is:

```math
\left|
M^{\Phi}_{\gamma,R}(b,\xi_-)
\right|
\le
C_{\mathrm{anch}}(R,\ell_R)g_{\mathrm{eff}}(R)
+
o_a(1).
\tag{15.872}
```

#### 15.62.1. Two-Sided Minimizer Decomposition

Expose the outgoing collar data by disintegrating the conditional block kernel:

```math
\mathsf K^s_{R,a,b}
\left[
\cdot
\mid
\xi_-
\right]
=
\int
\mathsf K^s_{R,a,b}
\left[
\cdot
\mid
\xi_-,\xi_+
\right]
d\nu^s_{R,a,b}(\xi_+\mid\xi_-).
\tag{15.873}
```

For fixed boundary data let the physical classical minimizer-flux set be:

```math
\mathfrak B^{\mathrm{cl},+}_{\gamma,R}
(b,\xi_-,\xi_+)
\subset
\mathbb R.
\tag{15.874}
```

The convexified classical radius is:

```math
B^{\mathrm{cl},+}_{\gamma,R}
(b,\xi_-,\xi_+)
:=
\sup
\left\{
|u|:
u\in
\operatorname{conv}
\mathfrak B^{\mathrm{cl},+}_{\gamma,R}
(b,\xi_-,\xi_+)
\right\}.
\tag{15.875}
```

The fluctuation distance from the classical minimizer-flux set is:

```math
D_{\gamma,R}
(\bar V;b,\xi_-,\xi_+)
:=
\operatorname{dist}
\left(
\Phi^{\mathrm{ren}}_{\gamma,R}(\bar V),
\operatorname{conv}
\mathfrak B^{\mathrm{cl},+}_{\gamma,R}
(b,\xi_-,\xi_+)
\right).
\tag{15.876}
```

The fixed-IR good event for the signed anchor is:

```math
\mathsf G_{\mathrm{anch}}
:=
\mathsf G_{\mathrm{route}}
\cap
\mathsf G_{\mathrm{collar}}
\cap
\mathsf G_{\mathrm{Fred}}
\cap
\mathsf G_{\mathrm{cos}}.
\tag{15.877}
```

The complement is:

```math
\mathsf B_{\mathrm{anch}}
:=
\mathsf G_{\mathrm{anch}}^{c}.
\tag{15.878}
```

All four good-event factors are physical-resolution conditions. The routing
factor is the relative center routing of Target 40.125. The collar factor is
the loop-lock condition of Target 40.124. The Fredholm factor is the
orthogonality condition of Target 40.123. The coset factor is the
source-minimizer neutrality condition of Target 40.91.

#### 15.62.2. Three Inputs That Locate The Signed Mean

The first input is a classical good-sector radius bound:

```math
B^{\mathrm{cl},+}_{\gamma,R}
(b,\xi_-,\xi_+)
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
\le
C_{\mathrm{good}}(R,\ell_R)g_{\mathrm{eff}}(R)
+
o_a(1).
\tag{15.879}
```

The second input is a thermal fluctuation bound around the minimizer-flux set:

```math
\mathsf K^s_{R,a,b}
\left[
D_{\gamma,R}^2
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
\mid
\xi_-
\right]
\le
C_{\mathrm{fluc}}(R,\ell_R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.880}
```

The third input is a bad-sector first-moment bound:

```math
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|
\mathbf 1_{\mathsf B_{\mathrm{anch}}}
\mid
\xi_-
\right]
\le
C_{\mathrm{bad}}(R,\ell_R)g_{\mathrm{eff}}(R)
+
o_a(1).
\tag{15.881}
```

These are not UV estimates. The observable is flowed at the fixed physical
radius `ell_R`, the loop family is finite at fixed physical `R`, and the
constants may depend on `R` and `ell_R` but not on the cutoff.

**Criterion 40.147 (Good Radius Plus Fluctuations Plus Bad Charge Proves The
Signed Mean Anchor).** Assume the same-reconstruction condition (15.870). If
(15.879), (15.880), and (15.881) hold uniformly as the cutoff is removed, then
the signed mean anchor (15.872) holds with:

```math
C_{\mathrm{anch}}
=
C_{\mathrm{good}}
+
C_{\mathrm{fluc}}^{1/2}
+
C_{\mathrm{bad}}.
\tag{15.882}
```

#### Proof

On the good event, the distance definition gives:

```math
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
\le
\left(
B^{\mathrm{cl},+}_{\gamma,R}
+
D_{\gamma,R}
\right)
\mathbf 1_{\mathsf G_{\mathrm{anch}}}.
\tag{15.883}
```

Take the conditional expectation with respect to the incoming collar:

```math
\left|
M^{\Phi}_{\gamma,R}(b,\xi_-)
\right|
\le
\mathsf K^s_{R,a,b}
\left[
B^{\mathrm{cl},+}_{\gamma,R}
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
\mid
\xi_-
\right]
+
\mathsf K^s_{R,a,b}
\left[
D_{\gamma,R}
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
\mid
\xi_-
\right]
+
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|
\mathbf 1_{\mathsf B_{\mathrm{anch}}}
\mid
\xi_-
\right].
\tag{15.884}
```

Use (15.879) for the first term and (15.881) for the third term. For the
middle term, apply Cauchy-Schwarz:

```math
\mathsf K^s_{R,a,b}
\left[
D_{\gamma,R}
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
\mid
\xi_-
\right]
\le
\left(
\mathsf K^s_{R,a,b}
\left[
D_{\gamma,R}^2
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
\mid
\xi_-
\right]
\right)^{1/2}.
\tag{15.885}
```

Substitute (15.879)-(15.881) into (15.884). This gives (15.872) with
(15.882). `∎`

#### 15.62.3. How The Earlier Targets Supply The Inputs

Target 40.91 supplies the neutral source-minimizer test: without a charged
tether, the classical source response is orthogonal to the physical flux
direction.

Target 40.123 supplies the Fredholm alternative: any remaining source-visible
mode is either killed by the physical flux functional or becomes a named
low-mode obstruction.

Target 40.124 supplies the collar-loop lock: outgoing collar holonomy cannot
create an unrecorded physical flux bias when the corresponding loop observable
has already been included in the physical family.

Target 40.125 supplies relative center routing: local center coboundaries have
trivial sheet pairing, while nontrivial sheet pairings are promoted to charged
sector data instead of being treated as invisible gauge moves.

Together these imply the good-sector radius bound:

```math
\boxed{
40.91+40.123+40.124+40.125
\Longrightarrow
(15.879).
}
\tag{15.886}
```

Target 40.143 supplies the finite-family source Hessian bound. In its
minimizer-centered form it gives:

```math
\boxed{
40.143
\Longrightarrow
(15.880).
}
\tag{15.887}
```

The bad-sector first moment is the remaining bookkeeping estimate. It is not
allowed to discard physically charged sectors. It must charge them explicitly:

```math
\mathsf B_{\mathrm{anch}}
\subset
\mathsf B_{\mathrm{route}}
\cup
\mathsf B_{\mathrm{collar}}
\cup
\mathsf B_{\mathrm{Fred}}
\cup
\mathsf B_{\mathrm{cos}}.
\tag{15.888}
```

The required fixed-IR charge bound is:

```math
\sum_{\mathsf B\in
\{\mathsf B_{\mathrm{route}},
\mathsf B_{\mathrm{collar}},
\mathsf B_{\mathrm{Fred}},
\mathsf B_{\mathrm{cos}}\}}
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|
\mathbf 1_{\mathsf B}
\mid
\xi_-
\right]
\le
C_{\mathrm{bad}}(R,\ell_R)g_{\mathrm{eff}}(R)
+
o_a(1).
\tag{15.889}
```

Then (15.881) follows from (15.888)-(15.889).

#### 15.62.4. Failure Mode

The signed mean anchor fails only if one of the following physical obstructions
survives:

```math
\boxed{
\begin{array}{ll}
\mathrm{F}_{\mathrm{cl}}
&
\limsup_{a\downarrow0}
g_{\mathrm{eff}}^{-1}
B^{\mathrm{cl},+}_{\gamma,R}
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
>0,\\[1mm]
\mathrm{F}_{\mathrm{fluc}}
&
\limsup_{a\downarrow0}
g_{\mathrm{eff}}^{-2}
\mathsf K^s_{R,a,b}
\left[
D_{\gamma,R}^2
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
\mid
\xi_-
\right]
=\infty,\\[1mm]
\mathrm{F}_{\mathrm{bad}}
&
\limsup_{a\downarrow0}
g_{\mathrm{eff}}^{-1}
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|
\mathbf 1_{\mathsf B_{\mathrm{anch}}}
\mid
\xi_-
\right]
>0
\text{ without charged-sector accounting.}
\end{array}}
\tag{15.890}
```

This is the precise fixed-IR diagnostic. The route does not fail because the
center plaquette coordinate was section-dependent. It fails only if, after
passing to physical flowed observables and routing charged center sheets, a
real signed physical flux bias remains.

#### 15.62.5. Completed Target 40.147

Target 40.147 is:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS}_{\mathrm{good}}
&
\text{prove the good-sector classical radius bound }(15.879),\\[1mm]
\mathrm{PASS}_{\mathrm{fluc}}
&
\text{prove the minimizer-centered fluctuation bound }(15.880),\\[1mm]
\mathrm{PASS}_{\mathrm{bad}}
&
\text{prove the charged bad-sector first-moment bound }(15.889),\\[1mm]
\mathrm{FAIL}
&
\text{exhibit one of the fixed-IR obstructions in }(15.890).
\end{array}}
\tag{15.891}
```

If all three pass lines hold, then the signed mean anchor (15.872) holds.
Together with Target 40.146, this closes both anchors in Target 40.144 and
returns the route to the enriched fixed-IR P4/P5 package of Target 40.142.

### 15.63. Target 40.148: Charged Bad-Sector First Moment From Flowed Size

Searchable Target-40.148 tag:

`V4P40-TARGET-40148-BAD-SECTOR-FIRST-MOMENT`.

Target 40.147 made the bad-sector first moment look like an independent
obstruction. It is independent only if the positive flowed-size anchor has not
yet been proved. Once the enriched Stokes size estimate is available, the bad
sectors do not need to be microscopically rare. They only need to be charged by
the same physical flowed flux observable.

The deterministic domination comes directly from the definitions (15.760) and
(15.761):

```math
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|
\le
\mathcal K_{\gamma,R,a}.
\tag{15.892}
```

Therefore the size anchor (15.838) implies the signed-flux second moment:

```math
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|^2
\mid
\xi_-
\right]
\le
C_{\mathcal K}^{(2)}(R,\ell_R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.893}
```

This estimate is fixed-IR aligned because both sides use the flowed physical
surface observable at radius `ell_R`.

#### 15.63.1. Uniform Event Bound

Let `B` be any event measurable in the full conditional block sigma-algebra.
It may depend on center routing, collar loops, Fredholm modes, or coset data.
No rarity assumption is made. Cauchy-Schwarz gives:

```math
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|
\mathbf 1_B
\mid
\xi_-
\right]
\le
\left(
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|^2
\mid
\xi_-
\right]
\right)^{1/2}
\left(
\mathsf K^s_{R,a,b}
\left[
\mathbf 1_B
\mid
\xi_-
\right]
\right)^{1/2}.
\tag{15.894}
```

Since the second factor is at most one, (15.893) gives:

```math
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|
\mathbf 1_B
\mid
\xi_-
\right]
\le
\left(
C_{\mathcal K}^{(2)}(R,\ell_R)
\right)^{1/2}
g_{\mathrm{eff}}(R)
+
o_a(1).
\tag{15.895}
```

The cutoff error is taken at fixed physical `R`; hence taking the square root
of the vanishing residual preserves an `o_a(1)` remainder.

#### 15.63.2. Application To The Four Anchor-Bad Sectors

Apply (15.895) to the four bad-sector events:

```math
\mathfrak B_{\mathrm{anch}}
:=
\left\{
\mathsf B_{\mathrm{route}},
\mathsf B_{\mathrm{collar}},
\mathsf B_{\mathrm{Fred}},
\mathsf B_{\mathrm{cos}}
\right\}.
\tag{15.896}
```

Then:

```math
\sum_{\mathsf B\in\mathfrak B_{\mathrm{anch}}}
\mathsf K^s_{R,a,b}
\left[
\left|
\Phi^{\mathrm{ren}}_{\gamma,R}
\right|
\mathbf 1_{\mathsf B}
\mid
\xi_-
\right]
\le
4
\left(
C_{\mathcal K}^{(2)}(R,\ell_R)
\right)^{1/2}
g_{\mathrm{eff}}(R)
+
o_a(1).
\tag{15.897}
```

Thus (15.889) holds with:

```math
C_{\mathrm{bad}}(R,\ell_R)
=
4
\left(
C_{\mathcal K}^{(2)}(R,\ell_R)
\right)^{1/2}.
\tag{15.898}
```

**Criterion 40.148 (Flowed Size Proves Charged Bad-Sector First Moment).** If
the curvature-size anchor (15.838) holds for the same physical reconstruction
and smoothing radius used in Target 40.147, then the bad-sector first-moment
bound (15.889) holds.

#### Proof

The triangle inequality on the physical surface gives (15.892). Taking the
conditional second moment gives (15.893). Cauchy-Schwarz gives (15.894). Since
conditional probabilities are bounded by one, (15.895) follows. Summing the
four events in (15.896) gives (15.897), which is exactly (15.889) with the
constant (15.898). `∎`

#### 15.63.3. Consequence For Fixed-IR Alignment

This proves that bad-sector first moments are not a separate fixed-IR obstacle
once the positive flowed-size estimate is in place. A bad event may have
order-one conditional probability; that is allowed. What is forbidden is an
order-one physical flowed flux on that event.

Equivalently:

```math
(15.838)
\Longrightarrow
(15.889).
\tag{15.899}
```

Thus:

```math
\neg(15.889)
\Longrightarrow
\neg(15.838).
\tag{15.900}
```

So a failure of the charged bad-sector first moment is not a new kind of
failure. It is a failure of the positive flowed-size anchor already isolated in
Target 40.146.

#### 15.63.4. Completed Target 40.148

Target 40.148 is resolved as:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS}
&
\text{prove the flowed curvature-size anchor }(15.838),\\[1mm]
\mathrm{CONSEQUENCE}
&
\text{the charged bad-sector first moment }(15.889)\text{ follows},\\[1mm]
\mathrm{FAIL}
&
\text{failure of }(15.889)\text{ is reclassified as failure of }(15.838).
\end{array}}
\tag{15.901}
```

Combining Target 40.146 with Target 40.148 removes the bad-sector term from the
signed mean problem. Target 40.147 now has two live burdens: the good-sector
classical radius bound (15.879) and the minimizer-centered fluctuation bound
(15.880).

### 15.64. Target 40.149: Good-Sector Classical Radius Bound

Searchable Target-40.149 tag:

`V4P40-TARGET-40149-GOOD-SECTOR-CLASSICAL-RADIUS`.

We now close the deterministic half of Target 40.147. The point is not that
every frontier-good collar has small classical flux. That is false by Theorem
40.95. The point is that the good sector for the mean anchor is narrower:
center sheets are routed, collar holonomies are small at the physical coupling
scale, and flux-visible Fredholm modes have been removed or charged.

The target is exactly (15.879):

```math
B^{\mathrm{cl},+}_{\gamma,R}
(b,\xi_-,\xi_+)
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
\le
C_{\mathrm{good}}(R,\ell_R)g_{\mathrm{eff}}(R)
+
o_a(1).
\tag{15.902}
```

#### 15.64.1. Sharp Meaning Of The Anchor-Good Sector

The anchor-good event is the intersection of four physical-resolution
conditions:

```math
\mathsf G_{\mathrm{anch}}
=
\mathsf G_{\mathrm{cen}}
\cap
\mathsf G_{\mathrm{coll}}
\cap
\mathsf G_{\mathrm{Fred}}
\cap
\mathsf G_{\mathrm{stab}}.
\tag{15.903}
```

The center condition says that the center sheet is locally routed in the disk
neighborhood:

```math
\mathbf 1_{\mathsf G_{\mathrm{cen}}}
\Longrightarrow
b\vert_{\mathcal N_{\gamma,R}}
=
\delta\zeta,
\qquad
\zeta\vert_{\partial\mathcal N_{\gamma,R}}=1.
\tag{15.904}
```

This is the Target 40.125 input. It says that local center coboundaries have
trivial sheet pairing. It does not say that the action is gauge-invariant under
arbitrary center moves.

The collar condition is the coupling-scaled physical collar-smallness estimate:

```math
\mathfrak h_{\gamma,R}^{\mathrm{cos}}(\xi_-,\xi_+)
\mathbf 1_{\mathsf G_{\mathrm{coll}}}
\le
c_{\mathrm{coll}}(R,\ell_R)g_{\mathrm{eff}}(R)
+
o_a(1).
\tag{15.905}
```

This is the Target 40.124 loop-lock input, but with the important fixed-IR
threshold. A collar holonomy that is merely inside a fixed chart is not enough.

The Fredholm condition is that the flux-visible kernel defect is removed at the
same physical scale. Let:

```math
\eta^{\mathrm{Fred}}_{\gamma,R,a}
:=
\left\|
P^{\ker}_{R,a}j_{\gamma,R,a}
\right\|_{-1,R,a}.
\tag{15.906}
```

The good Fredholm sector obeys:

```math
\eta^{\mathrm{Fred}}_{\gamma,R,a}
\mathbf 1_{\mathsf G_{\mathrm{Fred}}}
\le
c_{\mathrm{Fred}}(R,\ell_R)g_{\mathrm{eff}}(R)
+
o_a(1).
\tag{15.907}
```

In the exact Target 40.123 PASS case, the left side is zero. In a finite
physical low-mode implementation, (15.907) is the condition that the low-mode
component has been charged rather than hidden in the good sector.

Finally, the stability condition is the center-adapted Dirichlet estimate:

```math
B^{\mathrm{cl},+}_{\gamma,R}
(b,\xi_-,\xi_+)
\mathbf 1_{\mathsf G_{\mathrm{stab}}}
\le
C_{\mathrm{stab}}(R,\ell_R)
\left(
\mathfrak h_{\gamma,R}^{\mathrm{cos}}(\xi_-,\xi_+)
+
\eta^{\mathrm{Fred}}_{\gamma,R,a}
\right)
+
o_a(1).
\tag{15.908}
```

This is the fixed-IR analytic content of Target 40.91 after Targets 40.123,
40.124, and 40.125 have removed the three nonclassical ways to fake a mean
bias.

#### 15.64.2. Criterion And Proof

**Criterion 40.149 (Routed Center Plus Small Collar Plus Fredholm Cleanliness
Proves The Good Classical Radius Bound).** If (15.904)-(15.908) hold for the
same flowed physical reconstruction used in (15.870), then (15.902) holds with:

```math
C_{\mathrm{good}}(R,\ell_R)
=
C_{\mathrm{stab}}(R,\ell_R)
\left(
c_{\mathrm{coll}}(R,\ell_R)
+
c_{\mathrm{Fred}}(R,\ell_R)
\right).
\tag{15.909}
```

#### Proof

On the anchor-good event, (15.908) applies. Substituting (15.905) and (15.907)
into (15.908) gives:

```math
B^{\mathrm{cl},+}_{\gamma,R}
(b,\xi_-,\xi_+)
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
\le
C_{\mathrm{stab}}(R,\ell_R)
\left(
c_{\mathrm{coll}}(R,\ell_R)
+
c_{\mathrm{Fred}}(R,\ell_R)
\right)
g_{\mathrm{eff}}(R)
+
o_a(1).
\tag{15.910}
```

This is (15.902) with the constant (15.909). `∎`

#### 15.64.3. Why This Is Still Fixed-IR

The estimate does not ask for microscopic collar flatness, microscopic center
triviality, or cutoff-scale coercivity. Every object in (15.904)-(15.908) is
defined at fixed physical resolution:

```math
\boxed{
\begin{array}{ll}
\mathsf G_{\mathrm{cen}}
&
\text{relative center sheet pairing in }\mathcal N_{\gamma,R},\\[1mm]
\mathsf G_{\mathrm{coll}}
&
\text{finite physical collar-loop holonomies},\\[1mm]
\mathsf G_{\mathrm{Fred}}
&
\text{finite physical reduced kernel modes},\\[1mm]
\mathsf G_{\mathrm{stab}}
&
\text{Dirichlet stability of the center-adapted physical minimizer.}
\end{array}}
\tag{15.911}
```

The cutoff limit is taken only after `R`, `ell_R`, the physical loop family, and
the physical collar-loop family have been fixed.

#### 15.64.4. What Would Falsify The Bound

The good-sector classical radius bound fails only if one of the following
fixed-IR obstructions survives:

```math
\boxed{
\begin{array}{ll}
\mathrm{F}_{\mathrm{cen}}
&
\text{a nontrivial center sheet remains inside }\mathsf G_{\mathrm{cen}},\\[1mm]
\mathrm{F}_{\mathrm{coll}}
&
\mathfrak h_{\gamma,R}^{\mathrm{cos}}
\mathbf 1_{\mathsf G_{\mathrm{coll}}}
\not\le
O(g_{\mathrm{eff}}(R)),\\[1mm]
\mathrm{F}_{\mathrm{Fred}}
&
\eta^{\mathrm{Fred}}_{\gamma,R,a}
\mathbf 1_{\mathsf G_{\mathrm{Fred}}}
\not\le
O(g_{\mathrm{eff}}(R)),\\[1mm]
\mathrm{F}_{\mathrm{stab}}
&
\text{the Dirichlet stability estimate }(15.908)\text{ fails.}
\end{array}}
\tag{15.912}
```

The first three are classification failures: a charged or low-mode sector has
been left in the good set. The fourth is the genuine analytic obstruction: a
tether-free, Fredholm-clean, center-routed physical minimizer has a larger than
linear response to small physical collar data.

#### 15.64.5. Completed Target 40.149

Target 40.149 is resolved as:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS}_{\mathrm{route}}
&
\text{use Target }40.125\text{ to prove }(15.904),\\[1mm]
\mathrm{PASS}_{\mathrm{coll}}
&
\text{use Target }40.124\text{ to prove }(15.905),\\[1mm]
\mathrm{PASS}_{\mathrm{Fred}}
&
\text{use Target }40.123\text{ to prove }(15.907),\\[1mm]
\mathrm{PASS}_{\mathrm{stab}}
&
\text{use Target }40.91\text{ to prove }(15.908),\\[1mm]
\mathrm{CONSEQUENCE}
&
\text{the good-sector classical radius bound }(15.879)\text{ follows},\\[1mm]
\mathrm{FAIL}
&
\text{one of the fixed-IR obstructions in }(15.912)\text{ survives.}
\end{array}}
\tag{15.913}
```

Together with Target 40.148, this reduces the signed mean anchor to the last
remaining burden in Target 40.147: the minimizer-centered fluctuation bound
(15.880).

### 15.65. Target 40.150: Minimizer-Centered Fluctuation Bound

Searchable Target-40.150 tag:

`V4P40-TARGET-40150-MINIMIZER-CENTERED-FLUCTUATION`.

This is the last live input in Target 40.147. It is not a microscopic Hessian
gap. The route only needs the physical flowed flux to concentrate around the
classical minimizer-flux set after the center, collar, and Fredholm sectors have
been routed.

Recall the target:

```math
\mathsf K^s_{R,a,b}
\left[
D_{\gamma,R}^2
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
\mid
\xi_-
\right]
\le
C_{\mathrm{fluc}}(R,\ell_R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.914}
```

The distance is the one defined in (15.876): it is a distance in the finite
physical flux coordinate, not in the full microscopic configuration space.

#### 15.65.1. Two-Sided Reduction

Use the disintegration (15.873). Write the two-sided conditional kernel as:

```math
\mathsf K^{s,+}_{R,a,b}
\left[
\cdot
\mid
\xi_-,\xi_+
\right].
\tag{15.915}
```

For fixed two-sided data define:

```math
\mathcal C^{\mathrm{cl},+}_{\gamma,R}
(b,\xi_-,\xi_+)
:=
\operatorname{conv}
\mathfrak B^{\mathrm{cl},+}_{\gamma,R}
(b,\xi_-,\xi_+).
\tag{15.916}
```

Then:

```math
D_{\gamma,R}(\bar V;b,\xi_-,\xi_+)
=
\operatorname{dist}
\left(
\Phi^{\mathrm{ren}}_{\gamma,R}(\bar V),
\mathcal C^{\mathrm{cl},+}_{\gamma,R}(b,\xi_-,\xi_+)
\right).
\tag{15.917}
```

The two-sided target is:

```math
\mathsf K^{s,+}_{R,a,b}
\left[
D_{\gamma,R}^2
\mid
\xi_-,\xi_+
\right]
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
\le
C_{\mathrm{2s}}(R,\ell_R)g_{\mathrm{eff}}^2(R)
+
o_a(1).
\tag{15.918}
```

**Criterion 40.150A (Two-Sided Fluctuation Proves The One-Sided Bound).** If
(15.918) holds uniformly over admissible two-sided anchor-good data, then
(15.914) holds with:

```math
C_{\mathrm{fluc}}(R,\ell_R)
=
C_{\mathrm{2s}}(R,\ell_R).
\tag{15.919}
```

#### Proof

By disintegration:

```math
\mathsf K^s_{R,a,b}
\left[
D_{\gamma,R}^2
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
\mid
\xi_-
\right]
=
\int
\mathsf K^{s,+}_{R,a,b}
\left[
D_{\gamma,R}^2
\mid
\xi_-,\xi_+
\right]
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
d\nu^s_{R,a,b}(\xi_+\mid\xi_-).
\tag{15.920}
```

Insert (15.918) under the integral and use that the outgoing-collar conditional
law has total mass one. This gives (15.914). `∎`

#### 15.65.2. Flux-Marginal Gaussian Shell Criterion

The clean fixed-IR object is the exact marginal law of the physical flux. Define
the finite-dimensional flux space:

```math
E_{\gamma,R}
:=
\mathfrak{so}(3).
\tag{15.921}
```

Push the two-sided conditional kernel forward by the flowed flux:

```math
\mu^{\Phi,+}_{\gamma,R,a}
(\cdot\mid b,\xi_-,\xi_+)
:=
\left(
\Phi^{\mathrm{ren}}_{\gamma,R}
\right)_{\#}
\mathsf K^{s,+}_{R,a,b}
\left[
\cdot
\mid
\xi_-,\xi_+
\right].
\tag{15.922}
```

The target (15.918) follows from the following physical shell estimate:

```math
\mu^{\Phi,+}_{\gamma,R,a}
\left[
u\in E_{\gamma,R}:
\operatorname{dist}
\left(
u,
\mathcal C^{\mathrm{cl},+}_{\gamma,R}
\right)
\ge
s g_{\mathrm{eff}}(R)
\mid
b,\xi_-,\xi_+
\right]
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
\le
C_{\mathrm{sh}}(R,\ell_R)
\left(
1+s
\right)^{m_{\Phi}}
\exp
\left(
-c_{\mathrm{sh}}(R,\ell_R)s^2
\right)
+
o_a(1)
\tag{15.923}
```

for every:

```math
s\ge0.
\tag{15.924}
```

Here:

```math
m_{\Phi}
=
\dim E_{\gamma,R}.
\tag{15.925}
```

**Criterion 40.150B (Gaussian Shell Bound Proves The Two-Sided Fluctuation
Bound).** If (15.923) holds with constants independent of the cutoff, then
(15.918) holds.

#### Proof

For any nonnegative random variable X:

```math
\mathbb E[X^2]
=
2
\int_0^{\infty}
r
\mathbb P[X\ge r]\,dr.
\tag{15.926}
```

Apply this with:

```math
X
=
D_{\gamma,R}.
\tag{15.927}
```

Set:

```math
r
=
s g_{\mathrm{eff}}(R).
\tag{15.928}
```

Then (15.923) gives:

```math
\mathsf K^{s,+}_{R,a,b}
\left[
D_{\gamma,R}^2
\mid
\xi_-,\xi_+
\right]
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
\le
2
C_{\mathrm{sh}}(R,\ell_R)
g_{\mathrm{eff}}^2(R)
\int_0^{\infty}
s
\left(
1+s
\right)^{m_{\Phi}}
\exp
\left(
-c_{\mathrm{sh}}(R,\ell_R)s^2
\right)
ds
+
o_a(1).
\tag{15.929}
```

The integral is finite because `m_Phi` is fixed before the cutoff limit. Hence
(15.918) holds with:

```math
C_{\mathrm{2s}}(R,\ell_R)
=
2
C_{\mathrm{sh}}(R,\ell_R)
\int_0^{\infty}
s
\left(
1+s
\right)^{m_{\Phi}}
\exp
\left(
-c_{\mathrm{sh}}(R,\ell_R)s^2
\right)
ds.
\tag{15.930}
```

`∎`

#### 15.65.3. How To Prove The Shell Bound

The shell estimate should be proved after integrating out microscopic fibers.
Assume the flux marginal has density:

```math
d\mu^{\Phi,+}_{\gamma,R,a}(u)
=
\frac{
\exp
\left(
-\mathcal I_{\gamma,R,a}(u\mid b,\xi_-,\xi_+)
\right)
}{
Z^{\Phi}_{\gamma,R,a}(b,\xi_-,\xi_+)
}
du.
\tag{15.931}
```

Here the effective potential already includes fiber entropy:

```math
\mathcal I_{\gamma,R,a}(u\mid b,\xi_-,\xi_+)
=
-\log
\int_{\Phi^{\mathrm{ren}}_{\gamma,R}=u}
\exp
\left(
-\mathcal A_0(\bar V\mid b,\xi_-,\xi_+)
\right)
d\sigma_u(\bar V).
\tag{15.932}
```

The fixed-IR Brascamp-Lieb input is a transverse quadratic lower bound for this
exact marginal potential:

```math
\mathcal I_{\gamma,R,a}(u\mid b,\xi_-,\xi_+)
-
\inf_{v\in\mathcal C^{\mathrm{cl},+}_{\gamma,R}}
\mathcal I_{\gamma,R,a}(v\mid b,\xi_-,\xi_+)
\ge
\kappa_{\Phi}(R,\ell_R)
g_{\mathrm{eff}}^{-2}(R)
\operatorname{dist}
\left(
u,
\mathcal C^{\mathrm{cl},+}_{\gamma,R}
\right)^2
-
C_{\mathrm{ent}}(R,\ell_R)
\log
\left(
1+
g_{\mathrm{eff}}^{-1}(R)
\operatorname{dist}
\left(
u,
\mathcal C^{\mathrm{cl},+}_{\gamma,R}
\right)
\right)
-
r_a.
\tag{15.933}
```

The logarithmic term is the allowed finite-dimensional shell entropy. The key
point is that the dimension in the shell entropy is physical and fixed. It does
not grow as the cutoff is removed.

**Criterion 40.150C (Flux-Marginal Brascamp-Lieb Proves The Shell Bound).** If
(15.931)-(15.933) hold on anchor-good data, with a matching local lower
normalization in a physical tube of radius comparable to `g_eff`, then (15.923)
holds.

#### Proof

Work inside the fixed physical flux chart. Tangential volume along the
minimizer-flux set is either compact in that chart or quotiented as an exact
minimizer direction. If it is neither, the broad tangential direction is a
failure of the reduced flux marginal rather than a UV effect.

Under this reduced finite-dimensional convention, the sublevel shells satisfy:

```math
\operatorname{vol}
\left\{
u:
s g_{\mathrm{eff}}(R)
\le
\operatorname{dist}
\left(
u,
\mathcal C^{\mathrm{cl},+}_{\gamma,R}
\right)
\le
\left(
s+1
\right)g_{\mathrm{eff}}(R)
\right\}
\le
C_{\mathrm{vol}}(R,\ell_R)
\left(
1+s
\right)^{m_{\Phi}}
g_{\mathrm{eff}}^{m_{\Phi}}(R).
\tag{15.934}
```

The lower normalization gives the same power of `g_eff` in the denominator.
The quadratic term in (15.933) gives the Gaussian factor:

```math
\exp
\left(
-\kappa_{\Phi}(R,\ell_R)s^2
\right).
\tag{15.935}
```

The logarithmic entropy allowance in (15.933) only changes the polynomial
factor in s. Summing the shells gives (15.923). `∎`

#### 15.65.4. Fixed-IR Failure Mode

The bound fails only if the exact physical flux marginal has a broad transverse
direction:

```math
\limsup_{a\downarrow0}
g_{\mathrm{eff}}^{-2}(R)
\mathsf K^{s,+}_{R,a,b}
\left[
D_{\gamma,R}^2
\mid
\xi_-,\xi_+
\right]
\mathbf 1_{\mathsf G_{\mathrm{anch}}}
=
\infty.
\tag{15.936}
```

Equivalently, there is a flux-visible soft direction that remains after center
routing, collar locking, and Fredholm projection. This is the same kind of
fixed-IR obstruction isolated in Target 40.143, but now centered on the
classical minimizer-flux set instead of the conditional mean.

#### 15.65.5. Completed Target 40.150

Target 40.150 is:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS}_{\mathrm{shell}}
&
\text{prove the physical flux shell estimate }(15.923),\\[1mm]
\mathrm{PASS}_{\mathrm{marg}}
&
\text{prove the flux-marginal Brascamp-Lieb input }(15.931)\text{-}(15.933),\\[1mm]
\mathrm{CONSEQUENCE}
&
\text{the minimizer-centered fluctuation bound }(15.880)\text{ follows},\\[1mm]
\mathrm{FAIL}
&
\text{exhibit the fixed-IR broad marginal }(15.936).
\end{array}}
\tag{15.937}
```

With Targets 40.148, 40.149, and 40.150 in place, Target 40.147 reduces the
signed mean anchor to three fixed-IR statements: positive flowed size, classical
good-sector neutrality, and physical flux-marginal concentration around the
minimizer set.

### 15.66. Target 40.151: Fixed-IR Plug-In Theorem For Paper 40

Searchable Target-40.151 tag:

`V4P40-TARGET-40151-FIXED-IR-PLUGIN-THEOREM`.

We now state exactly what this paper can export to the broader Paper 40
construction theorem. The export is not a bare center-disorder theorem. Theorem
40.5 already showed that bare center disorder is insufficient. The export must
be a fixed-physical-IR Wilson sheet-domination theorem for the actual
center-resolved amplitude.

Fix, before taking the cutoff limit:

```math
R,\qquad
\ell_R,\qquad
\mathcal L_R^{\mathrm{phys}},
\tag{15.938}
```

where the last object is the finite physical loop family. For each:

```math
\gamma\in\mathcal L_R^{\mathrm{phys}},
\tag{15.939}
```

choose a physical spanning surface:

```math
\Sigma_\gamma.
\tag{15.940}
```

Let the lattice representatives along the continuum scaling trajectory be:

```math
C_{\gamma,a}\longrightarrow\gamma,
\qquad
S_{\gamma,a}\longrightarrow\Sigma_\gamma.
\tag{15.941}
```

#### 15.66.1. The Admissible Amplitude Class

Define the fixed-IR admissible amplitude class:

```math
\mathcal Q^{\mathrm{adm}}_{R,\ell_R}
\tag{15.942}
```

as the class of section-relative center amplitudes `Q_a(b)` satisfying the
following requirements.

First, they are produced by the same physical reconstruction used in the
enriched Stokes package:

```math
Q_a
=
\alpha^s_{C_{\gamma,a},S_{\gamma,a}}
\quad
\text{for the reconstruction in }(15.870).
\tag{15.943}
```

Second, the enriched fixed-IR observable package closes:

```math
\mathrm{P1/P6}
\quad+\quad
\mathrm{P2}
\quad+\quad
\mathrm{P3}
\quad+\quad
\mathrm{P4/P5}
\tag{15.944}
```

for the finite physical family (15.806).

Third, the three analytic anchors from the end of Section 15 hold:

```math
\boxed{
\begin{array}{ll}
\mathrm{A1}
&
\text{positive flowed size }(15.838),\\[1mm]
\mathrm{A2}
&
\text{good-sector classical radius }(15.879),\\[1mm]
\mathrm{A3}
&
\text{minimizer-centered fluctuation }(15.880).
\end{array}}
\tag{15.945}
```

By Targets 40.148, 40.149, and 40.150, these imply the full signed mean package
of Target 40.147, provided their stated fixed-IR hypotheses hold.

The class (15.942) is not a class of arbitrary bounded functions. It is the
actual SO(3) cocycle amplitude class after the center sheet has been separated,
the physical smoothing radius has been fixed, and the cutoff has not yet been
sent to zero.

#### 15.66.2. The Remaining Center-Disorder Stability Estimate

The confinement-specific estimate that remains is stability of center disorder
against every admissible amplitude:

```math
\sup_{Q_a\in\mathcal Q^{\mathrm{adm}}_{R,\ell_R}}
\left|
\int
\Xi_{S_{\gamma,a}}(b)
Q_a(b)
d\mu^s_{\mathrm{cen},a}(b)
\right|
\le
K_R
\exp
\left(
-\sigma_R
\operatorname{Area}_{\mathrm{phys}}(\Sigma_\gamma)
+
\kappa_R
\operatorname{Perim}_{\mathrm{phys}}(\gamma)
\right)
+
o_a(1),
\tag{15.946}
```

with:

```math
\sigma_R>0.
\tag{15.947}
```

This is the exact place where the route proves confinement or fails. Equation
(15.946) is stronger than bare center disorder and weaker than simply assuming
the Wilson area law only because the amplitude class has already been reduced
to the fixed-IR admissible class (15.942).

#### 15.66.3. Plug-In Criterion

**Criterion 40.151 (Fixed-IR Plug-In For The Paper 40 Construction Theorem).**
Assume the exact lift identity (15.32), the section discipline of Section 15.9,
and the same-reconstruction condition (15.870). Suppose that for every loop in
the fixed physical family:

```math
\alpha^s_{C_{\gamma,a},S_{\gamma,a}}
\in
\mathcal Q^{\mathrm{adm}}_{R,\ell_R},
\tag{15.948}
```

and that the center-disorder stability estimate (15.946) holds. Then:

```math
\left|
\left\langle
W_{1/2}(C_{\gamma,a})
\right\rangle
\right|
\le
K_R
\exp
\left(
-\sigma_R
\operatorname{Area}_{\mathrm{phys}}(\Sigma_\gamma)
+
\kappa_R
\operatorname{Perim}_{\mathrm{phys}}(\gamma)
\right)
+
o_a(1).
\tag{15.949}
```

Thus this paper supplies the fixed-physical-IR Wilson sheet-domination input
needed by the broader Paper 40 construction theorem at scale `R`.

#### Proof

The exact center-marginal Wilson identity gives:

```math
\left\langle
W_{1/2}(C_{\gamma,a})
\right\rangle
=
\int
\Xi_{S_{\gamma,a}}(b)
\alpha^s_{C_{\gamma,a},S_{\gamma,a}}(b)
d\mu^s_{\mathrm{cen},a}(b).
\tag{15.950}
```

By (15.948), the actual conditional cocycle amplitude belongs to the admissible
class. Apply (15.946) with:

```math
Q_a
=
\alpha^s_{C_{\gamma,a},S_{\gamma,a}}.
\tag{15.951}
```

This gives (15.949). `∎`

#### 15.66.4. What The Plug-In Does And Does Not Claim

The plug-in theorem exports:

```math
\boxed{
\begin{array}{c}
\text{fixed physical loop family}\\
+\\
\text{exact SU(2)/SO(3) center lift}\\
+\\
\text{admissible fixed-IR cocycle amplitude}\\
+\\
\text{center disorder stable against that amplitude}
\end{array}
\Longrightarrow
\text{Wilson area law at fixed physical }R.
}
\tag{15.952}
```

It does not by itself prove the continuum Yang-Mills construction, Osterwalder-
Schrader reconstruction, the mass gap, or large-scale extension beyond the
chosen physical family. Those belong to the surrounding Paper 40 construction
theorem. What it does provide is the missing fixed-IR Wilson sheet-domination
module, provided the remaining estimates are closed.

#### 15.66.5. Completed Target 40.151

Target 40.151 is:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS}_{\mathrm{amp}}
&
\text{prove actual amplitude membership }(15.948),\\[1mm]
\mathrm{PASS}_{\mathrm{cen}}
&
\text{prove center-disorder stability }(15.946),\\[1mm]
\mathrm{CONSEQUENCE}
&
\text{Paper 40 receives the fixed-IR Wilson input }(15.949),\\[1mm]
\mathrm{FAIL}
&
\text{an admissible cocycle amplitude cancels center disorder at area order.}
\end{array}}
\tag{15.953}
```

The next target should therefore be the only remaining confinement-specific
input:

```math
\boxed{
\text{Target 40.152: prove or falsify the center-disorder stability estimate
}(15.946).
}
\tag{15.954}
```

### 15.67. Target 40.152: Center-Sensitivity Norm For Admissible Amplitudes

Searchable Target-40.152 tag:

`V4P40-TARGET-40152-CENTER-SENSITIVITY-NORM`.

Target 40.151 moved the confinement burden to (15.946). The next danger is
conceptual: the SO(3) analytic anchors control the physical coset response, but
they do not automatically control how the conditional amplitude depends on the
center field. A center-sensitive amplitude could still learn the Wilson sheet
sign.

#### 15.67.1. No-Free-Lunch For SO(3)-Only Anchors

Define the SO(3)-shadow admissible class:

```math
\mathcal Q^{\mathrm{SO3}}_{R,\ell_R}
\tag{15.955}
```

to be the class of bounded section-relative amplitudes that satisfy the
SO(3)-side requirements in (15.944)-(15.945), but with no restriction on their
dependence on the center coordinate beyond:

```math
|Q_a(b)|\le1.
\tag{15.956}
```

**Theorem 40.152A (SO(3)-Side Anchors Alone Do Not Prove Center Stability).**
The center-disorder stability estimate (15.946) does not follow from membership
in (15.955).

#### Proof

Choose:

```math
Q_a(b)
:=
\overline{\Xi_{S_{\gamma,a}}(b)}.
\tag{15.957}
```

This amplitude is bounded by one and can be assigned the same SO(3)-observable
shadow data as any other element of (15.955), because (15.955) has no
center-sensitivity constraint. But:

```math
\Xi_{S_{\gamma,a}}(b)Q_a(b)
=
1
\tag{15.958}
```

pointwise. Therefore:

```math
\left|
\int
\Xi_{S_{\gamma,a}}(b)Q_a(b)
d\mu^s_{\mathrm{cen},a}(b)
\right|
=
1.
\tag{15.959}
```

This violates any nontrivial area-law bound for large enough physical surfaces.
Thus the admissible class must include a center-sensitivity condition, not only
SO(3) size, mean, and fluctuation anchors. `∎`

#### 15.67.2. Boundary Sigma Algebra And Sensitivity Norm

Fix a physical boundary thickness:

```math
\rho_R
\asymp
\ell_R.
\tag{15.960}
```

Let:

```math
\mathcal N_{\partial,\rho_R}(\gamma)
\tag{15.961}
```

be the physical collar of the loop boundary inside the chosen sheet
neighborhood. Let:

```math
\mathcal F^{\mathrm{cen}}_{\partial,\rho_R}(\gamma)
\tag{15.962}
```

be the sigma algebra generated by the section-relative center variables in that
physical boundary collar.

For a bounded center amplitude `Q_a`, define its center-sensitivity norm away
from the boundary by:

```math
\|Q_a\|_{\mathrm{censens};S_{\gamma,a},\rho_R}
:=
\inf_{\Gamma_a}
\mathbb E_{\mu^s_{\mathrm{cen},a}}
\left[
\left|
Q_a-\Gamma_a
\right|
\right],
\tag{15.963}
```

where the infimum is over all boundary amplitudes satisfying:

```math
\Gamma_a
\text{ is }
\mathcal F^{\mathrm{cen}}_{\partial,\rho_R}(\gamma)
\text{ measurable},
\qquad
|\Gamma_a|\le1.
\tag{15.964}
```

This norm is deliberately center-facing. It does not measure SO(3) flux size.
It measures whether the amplitude can distinguish center configurations in the
interior of the Wilson sheet after the physical boundary data are fixed.

#### 15.67.3. Boundary-Stable Center Disorder

The center marginal must satisfy a boundary-conditional disorder estimate. The
right fixed-IR form is:

```math
\sup_{\substack{
\Gamma_a\in L^{\infty}(\mathcal F^{\mathrm{cen}}_{\partial,\rho_R}(\gamma))\\
|\Gamma_a|\le1
}}
\left|
\int
\Xi_{S_{\gamma,a}}(b)
\Gamma_a(b)
d\mu^s_{\mathrm{cen},a}(b)
\right|
\le
K_R
\exp
\left(
-\sigma_R
\operatorname{Area}_{\mathrm{phys}}(\Sigma_\gamma)
+
\kappa_R
\operatorname{Perim}_{\mathrm{phys}}(\gamma)
\right)
+
o_a(1).
\tag{15.965}
```

This is stronger than bare disorder and weaker than conditioning on the entire
surface. It says that center disorder survives after the physical boundary
collar has been revealed.

#### 15.67.4. Center-Sensitivity Criterion

The admissible amplitude class should be sharpened to:

```math
\mathcal Q^{\mathrm{adm},\mathrm{sens}}_{R,\ell_R}
\subset
\mathcal Q^{\mathrm{adm}}_{R,\ell_R}.
\tag{15.966}
```

Membership means:

```math
Q_a\in\mathcal Q^{\mathrm{adm}}_{R,\ell_R},
\qquad
|Q_a|\le1,
\tag{15.967}
```

and:

```math
\|Q_a\|_{\mathrm{censens};S_{\gamma,a},\rho_R}
\le
K_R^{\mathrm{sens}}
\exp
\left(
-\sigma_R^{\mathrm{sens}}
\operatorname{Area}_{\mathrm{phys}}(\Sigma_\gamma)
+
\kappa_R^{\mathrm{sens}}
\operatorname{Perim}_{\mathrm{phys}}(\gamma)
\right)
+
o_a(1),
\tag{15.968}
```

with:

```math
\sigma_R^{\mathrm{sens}}>0.
\tag{15.969}
```

**Criterion 40.152B (Boundary Disorder Plus Center Sensitivity Proves
Stability).** If (15.965) and (15.968) hold, then (15.946) holds for
the sharpened admissible amplitude class. More explicitly, for every:

```math
Q_a\in\mathcal Q^{\mathrm{adm},\mathrm{sens}}_{R,\ell_R},
\tag{15.970}
```

one has:

```math
\left|
\int
\Xi_{S_{\gamma,a}}(b)
Q_a(b)
d\mu^s_{\mathrm{cen},a}(b)
\right|
\le
K'_R
\exp
\left(
-\sigma'_R
\operatorname{Area}_{\mathrm{phys}}(\Sigma_\gamma)
+
\kappa'_R
\operatorname{Perim}_{\mathrm{phys}}(\gamma)
\right)
+
o_a(1),
\tag{15.971}
```

for some:

```math
\sigma'_R>0.
\tag{15.972}
```

#### Proof

Choose a boundary amplitude `Gamma_a` with:

```math
\mathbb E_{\mu^s_{\mathrm{cen},a}}
\left[
\left|
Q_a-\Gamma_a
\right|
\right]
\le
\|Q_a\|_{\mathrm{censens};S_{\gamma,a},\rho_R}
+
o_a(1).
\tag{15.973}
```

Then:

```math
\int
\Xi_{S_{\gamma,a}}Q_a
d\mu^s_{\mathrm{cen},a}
=
\int
\Xi_{S_{\gamma,a}}\Gamma_a
d\mu^s_{\mathrm{cen},a}
+
\int
\Xi_{S_{\gamma,a}}
\left(
Q_a-\Gamma_a
\right)
d\mu^s_{\mathrm{cen},a}.
\tag{15.974}
```

Since:

```math
|\Xi_{S_{\gamma,a}}|=1,
\tag{15.975}
```

the second term obeys:

```math
\left|
\int
\Xi_{S_{\gamma,a}}
\left(
Q_a-\Gamma_a
\right)
d\mu^s_{\mathrm{cen},a}
\right|
\le
\mathbb E_{\mu^s_{\mathrm{cen},a}}
\left[
\left|
Q_a-\Gamma_a
\right|
\right].
\tag{15.976}
```

Use (15.965) on the first term and (15.968) on the second term. The sum of two
area-law bounds is again an area-law bound, with:

```math
\sigma'_R
=
\min
\left\{
\sigma_R,
\sigma_R^{\mathrm{sens}}
\right\}
-
\epsilon_R,
\tag{15.977}
```

for any fixed:

```math
0<\epsilon_R<
\min
\left\{
\sigma_R,
\sigma_R^{\mathrm{sens}}
\right\}.
\tag{15.978}
```

Absorb the constants into `K'_R` and the perimeter terms into `kappa'_R`. This
gives (15.971). `∎`

#### 15.67.5. What Must Be Proved For The Actual Cocycle

The remaining actual-amplitude target is now sharper:

```math
\alpha^s_{C_{\gamma,a},S_{\gamma,a}}
\in
\mathcal Q^{\mathrm{adm},\mathrm{sens}}_{R,\ell_R}.
\tag{15.979}
```

Equivalently, prove the boundary approximation:

```math
\alpha^s_{C_{\gamma,a},S_{\gamma,a}}(b)
=
\Gamma^s_{\gamma,a}(b)
+
\mathcal R^s_{\gamma,a}(b),
\tag{15.980}
```

where:

```math
\Gamma^s_{\gamma,a}
\text{ is }
\mathcal F^{\mathrm{cen}}_{\partial,\rho_R}(\gamma)
\text{ measurable},
\qquad
|\Gamma^s_{\gamma,a}|\le1,
\tag{15.981}
```

and:

```math
\mathbb E_{\mu^s_{\mathrm{cen},a}}
\left[
\left|
\mathcal R^s_{\gamma,a}
\right|
\right]
\le
K_R^{\mathrm{sens}}
\exp
\left(
-\sigma_R^{\mathrm{sens}}
\operatorname{Area}_{\mathrm{phys}}(\Sigma_\gamma)
+
\kappa_R^{\mathrm{sens}}
\operatorname{Perim}_{\mathrm{phys}}(\gamma)
\right)
+
o_a(1).
\tag{15.982}
```

This is the normed version of the older boundary/quasilocal target (15.33). It
is exactly what the plug-in theorem needs, because it converts structural
quasilocality into the numerical center-disorder stability estimate (15.946).

#### 15.67.6. Completed Target 40.152

Target 40.152 is:

```math
\boxed{
\begin{array}{ll}
\mathrm{FAIL}_{\mathrm{broad}}
&
\text{SO(3)-side anchors alone fail by Theorem }40.152A,\\[1mm]
\mathrm{PASS}_{\mathrm{bd}}
&
\text{prove boundary-stable center disorder }(15.965),\\[1mm]
\mathrm{PASS}_{\mathrm{sens}}
&
\text{prove actual amplitude sensitivity }(15.979)\text{ or }(15.980)\text{-}(15.982),\\[1mm]
\mathrm{CONSEQUENCE}
&
\text{the center-disorder stability estimate }(15.946)\text{ follows},\\[1mm]
\mathrm{FAIL}
&
\text{the actual cocycle has area-order center sensitivity.}
\end{array}}
\tag{15.983}
```

This is now the precise fixed-IR bottleneck. The remaining work is not another
SO(3) mean or variance estimate. It is a center-sensitivity estimate for the
actual conditional cocycle amplitude.

### 15.68. Target 40.153: From Quasilocal Cocycle Response To Center Sensitivity

Searchable Target-40.153 tag:

`V4P40-TARGET-40153-QUASILOCAL-TO-CENTER-SENSITIVITY`.

The older boundary/quasilocal criteria, such as Criteria 40.12, 40.28, and
40.67, were structural. Target 40.152 now asks for a normed statement:

```math
\left\|
\alpha^s_{C_{\gamma,a},S_{\gamma,a}}
\right\|_{\mathrm{censens};S_{\gamma,a},\rho_R}
\le
\exp
\left(
-\sigma
\operatorname{Area}_{\mathrm{phys}}(\Sigma_\gamma)
+
\kappa
\operatorname{Perim}_{\mathrm{phys}}(\gamma)
\right)
+
o_a(1).
\tag{15.984}
```

This is stronger than merely saying that the cocycle response has summable
tails. The question is whether the structural quasilocal expansion has an
area-barrier against learning the center sheet sign.

#### 15.68.1. Ordinary Bulk Summability Is Not Enough

Let:

```math
\mathcal B_R(\Sigma_\gamma)
\tag{15.985}
```

be a fixed physical block tiling of the sheet neighborhood, chosen after `R` and
`ell_R` are fixed. Suppose a decomposition has independent interior-sensitive
one-block terms with total expected weight:

```math
\sum_{Q\subset\Sigma_\gamma}
\mathbb E
\left[
|w_Q|
\right]
\le
p_R
|\mathcal B_R(\Sigma_\gamma)|.
\tag{15.986}
```

This is a perfectly summable local estimate at fixed physical block scale. It
does not imply (15.984), because the right side of (15.986) is proportional to
area, while (15.984) requires exponential smallness in area.

**Theorem 40.153A (Local Summability Does Not Imply Center Sensitivity).** A
quasilocal expansion with a positive density of interior-sensitive terms cannot
prove the center-sensitivity norm bound (15.984).

#### Proof

If each interior block has a nonzero chance of contributing a center-sensitive
term of size comparable to `p_R`, then the best boundary approximation leaves
an expected interior remainder bounded below by a constant multiple of:

```math
1-
\left(
1-p_R
\right)^{|\mathcal B_R(\Sigma_\gamma)|}.
\tag{15.987}
```

For fixed positive `p_R`, this approaches one as the physical area grows. Even
if the linearized estimate (15.986) is used instead, the remainder is order
area, not exponentially small in area. Therefore ordinary local summability is
too weak for (15.984). `∎`

The phrase physical area grows here means that one compares the fixed-IR
problem across physical loop families or larger choices of `R`; it is not a
cutoff limit. For each such physical problem, `R` and `ell_R` are still fixed
before sending `a` to zero.

This is the new fixed-IR lesson. The cocycle may have local defects, but local
defects must be center-neutral in the sheet interior. Center-sensitive defects
must be forced into an area-order carrier.

#### 15.68.2. Sensitivity Carriers

Define the deep interior block set:

```math
\mathcal B_R^{\mathrm{deep}}(\Sigma_\gamma)
:=
\left\{
Q\in\mathcal B_R(\Sigma_\gamma):
\operatorname{dist}_{\mathrm{phys}}
\left(
Q,
\gamma
\right)
\ge
\rho_R
\right\}.
\tag{15.988}
```

A polymer family:

```math
\mathscr P
\tag{15.989}
```

is called a center-sensitivity carrier family if every polymer collection
`P` in the family has the following property: after deleting `P`, the cocycle
amplitude restricted to the remaining sheet blocks is measurable with respect
to the boundary center sigma algebra:

```math
\mathcal F^{\mathrm{cen}}_{\partial,\rho_R}(\gamma).
\tag{15.990}
```

The carrier family has an area barrier if there are constants:

```math
c_{\mathrm{bar}}(R,\ell_R)>0,
\qquad
C_{\mathrm{bar}}(R,\ell_R)<\infty,
\tag{15.991}
```

such that every center-sensitive carrier satisfies:

```math
|P|
\ge
c_{\mathrm{bar}}(R,\ell_R)
\operatorname{Area}_{\mathrm{phys}}(\Sigma_\gamma)
-
C_{\mathrm{bar}}(R,\ell_R)
\operatorname{Perim}_{\mathrm{phys}}(\gamma).
\tag{15.992}
```

This is the missing topological/combinatorial input. It says that to learn the
Wilson sheet sign from the interior, the cocycle response must carry an
area-order object, not a sparse gas of independent bulk defects.

#### 15.68.3. Area-Barrier Polymer Criterion

Assume the exact conditional cocycle amplitude has the polymer decomposition:

```math
\alpha^s_{C_{\gamma,a},S_{\gamma,a}}(b)
=
\Gamma^s_{\gamma,a}(b)
+
\sum_{P\in\mathscr P_{\mathrm{sens}}}
W_P^s(b)
+
\mathcal R^s_{\mathrm{tail}}(b),
\tag{15.993}
```

where:

```math
\Gamma^s_{\gamma,a}
\text{ is }
\mathcal F^{\mathrm{cen}}_{\partial,\rho_R}(\gamma)
\text{ measurable},
\qquad
\left|
\Gamma^s_{\gamma,a}
\right|
\le1.
\tag{15.994}
```

The sensitivity polymers obey a Kotecky-Preiss bound:

```math
\sum_{\substack{
P\in\mathscr P_{\mathrm{sens}}\\
P\ni Q_0
}}
\mathbb E_{\mu^s_{\mathrm{cen},a}}
\left[
\left|
W_P^s
\right|
\right]
e^{\theta_R |P|}
\le
\eta_R
\tag{15.995}
```

with:

```math
\theta_R>\theta_{\mathrm{ent}}(R,\ell_R),
\qquad
\eta_R<\infty.
\tag{15.996}
```

Here `theta_ent` is the fixed physical entropy rate for connected block
carriers. Finally the nonpolymer tail satisfies:

```math
\mathbb E_{\mu^s_{\mathrm{cen},a}}
\left[
\left|
\mathcal R^s_{\mathrm{tail}}
\right|
\right]
\le
K_R^{\mathrm{tail}}
\exp
\left(
-\sigma_R^{\mathrm{tail}}
\operatorname{Area}_{\mathrm{phys}}(\Sigma_\gamma)
+
\kappa_R^{\mathrm{tail}}
\operatorname{Perim}_{\mathrm{phys}}(\gamma)
\right)
+
o_a(1).
\tag{15.997}
```

**Criterion 40.153B (Area-Barrier Quasilocality Proves Center Sensitivity).**
If (15.992)-(15.997) hold, then the actual cocycle amplitude satisfies
(15.982), hence belongs to:

```math
\mathcal Q^{\mathrm{adm},\mathrm{sens}}_{R,\ell_R}.
\tag{15.998}
```

#### Proof

Use the boundary amplitude in (15.994) as the candidate in the sensitivity norm
(15.963). Then:

```math
\left\|
\alpha^s_{C_{\gamma,a},S_{\gamma,a}}
\right\|_{\mathrm{censens};S_{\gamma,a},\rho_R}
\le
\sum_{P\in\mathscr P_{\mathrm{sens}}}
\mathbb E
\left[
\left|
W_P^s
\right|
\right]
+
\mathbb E
\left[
\left|
\mathcal R^s_{\mathrm{tail}}
\right|
\right].
\tag{15.999}
```

By the connected-carrier entropy bound and (15.995), the sum over carriers of
size at least n is bounded by:

```math
C_R
\exp
\left(
-
\left(
\theta_R-\theta_{\mathrm{ent}}(R,\ell_R)
\right)
n
\right).
\tag{15.1000}
```

Insert the area barrier (15.992). This gives:

```math
\sum_{P\in\mathscr P_{\mathrm{sens}}}
\mathbb E
\left[
\left|
W_P^s
\right|
\right]
\le
K_R^{\mathrm{bar}}
\exp
\left(
-\sigma_R^{\mathrm{bar}}
\operatorname{Area}_{\mathrm{phys}}(\Sigma_\gamma)
+
\kappa_R^{\mathrm{bar}}
\operatorname{Perim}_{\mathrm{phys}}(\gamma)
\right)
+
o_a(1),
\tag{15.1001}
```

where:

```math
\sigma_R^{\mathrm{bar}}
=
\left(
\theta_R-\theta_{\mathrm{ent}}(R,\ell_R)
\right)
c_{\mathrm{bar}}(R,\ell_R).
\tag{15.1002}
```

Combine (15.997), (15.999), and (15.1001). The result is (15.982) with:

```math
\sigma_R^{\mathrm{sens}}
=
\min
\left\{
\sigma_R^{\mathrm{bar}},
\sigma_R^{\mathrm{tail}}
\right\}
-
\epsilon_R,
\tag{15.1003}
```

for any fixed positive epsilon smaller than the displayed minimum. `∎`

#### 15.68.4. Relation To The Older Quasilocal Criteria

Criteria 40.12, 40.28, and 40.67 become sufficient for Target 40.152 only after
they are strengthened in one precise way. The polymer expansion must separate
bulk center-neutral defects from center-sensitive carriers:

```math
\boxed{
\begin{array}{c}
\text{bulk quasilocal defects may occur with positive density,}\\[1mm]
\text{but their contribution must be center-neutral in the sheet interior;}\\[1mm]
\text{center-sensitive carriers must obey the area barrier }(15.992).
\end{array}}
\tag{15.1004}
```

Without (15.1004), the older quasilocal conclusions control locality but not the
center-sensitivity norm. With (15.1004), the older response-locality machinery
feeds directly into Target 40.152.

#### 15.68.5. Completed Target 40.153

Target 40.153 is:

```math
\boxed{
\begin{array}{ll}
\mathrm{FAIL}_{\mathrm{local}}
&
\text{ordinary local summability is insufficient by Theorem }40.153A,\\[1mm]
\mathrm{PASS}_{\mathrm{bar}}
&
\text{prove the area-barrier carrier bound }(15.992),\\[1mm]
\mathrm{PASS}_{\mathrm{KP}}
&
\text{prove the sensitivity-carrier KP estimate }(15.995),\\[1mm]
\mathrm{PASS}_{\mathrm{tail}}
&
\text{prove the residual tail bound }(15.997),\\[1mm]
\mathrm{CONSEQUENCE}
&
\text{actual cocycle center sensitivity }(15.982)\text{ follows},\\[1mm]
\mathrm{FAIL}
&
\text{center-sensitive bulk carriers occur without area-order cost.}
\end{array}}
\tag{15.1005}
```

The next separate target is boundary-stable center disorder (15.965). Target
40.153 handles the amplitude side; Target 40.154 must handle the center marginal
after the physical boundary collar has been revealed.

### 15.69. Target 40.154: Boundary-Stable Center Disorder

Searchable Target-40.154 tag:

`V4P40-TARGET-40154-BOUNDARY-STABLE-CENTER-DISORDER`.

Target 40.152 reduced the center-marginal side of the plug-in theorem to
(15.965). We now rewrite that estimate in the exact form that has to be proved.
The boundary collar may be revealed, but the deep interior center sheet must
still be disordered at area order.

Let:

```math
X_{\gamma,a}(b)
:=
\Xi_{S_{\gamma,a}}(b).
\tag{15.1006}
```

Recall the boundary center sigma algebra:

```math
\mathcal F^{\mathrm{cen}}_{\partial,\rho_R}(\gamma).
\tag{15.1007}
```

Define the boundary-conditioned center sheet mean:

```math
M^{\mathrm{cen}}_{\gamma,a}
:=
\mathbb E_{\mu^s_{\mathrm{cen},a}}
\left[
X_{\gamma,a}
\mid
\mathcal F^{\mathrm{cen}}_{\partial,\rho_R}(\gamma)
\right].
\tag{15.1008}
```

#### 15.69.1. Exact Dual Norm Reformulation

The boundary-stable center disorder estimate (15.965) is equivalent to an
`L1` estimate for (15.1008).

**Lemma 40.154A (Boundary-Amplitude Supremum Equals Conditional Sheet Norm).**
For every finite cutoff:

```math
\sup_{\substack{
\Gamma_a\in L^{\infty}(\mathcal F^{\mathrm{cen}}_{\partial,\rho_R}(\gamma))\\
|\Gamma_a|\le1
}}
\left|
\int
X_{\gamma,a}(b)
\Gamma_a(b)
d\mu^s_{\mathrm{cen},a}(b)
\right|
=
\mathbb E_{\mu^s_{\mathrm{cen},a}}
\left[
\left|
M^{\mathrm{cen}}_{\gamma,a}
\right|
\right].
\tag{15.1009}
```

#### Proof

For any admissible boundary amplitude:

```math
\int
X_{\gamma,a}\Gamma_a
d\mu^s_{\mathrm{cen},a}
=
\int
M^{\mathrm{cen}}_{\gamma,a}\Gamma_a
d\mu^s_{\mathrm{cen},a}.
\tag{15.1010}
```

The absolute value is bounded above by the right side of (15.1009). Equality is
attained up to null sets by choosing the boundary-measurable phase:

```math
\Gamma_a
=
\overline{
\operatorname{phase}
\left(
M^{\mathrm{cen}}_{\gamma,a}
\right)
}.
\tag{15.1011}
```

Thus (15.1009) holds. `∎`

Consequently (15.965) is equivalent to:

```math
\mathbb E_{\mu^s_{\mathrm{cen},a}}
\left[
\left|
M^{\mathrm{cen}}_{\gamma,a}
\right|
\right]
\le
K_R
\exp
\left(
-\sigma_R
\operatorname{Area}_{\mathrm{phys}}(\Sigma_\gamma)
+
\kappa_R
\operatorname{Perim}_{\mathrm{phys}}(\gamma)
\right)
+
o_a(1).
\tag{15.1012}
```

This is the clean center-side target.

#### 15.69.2. Removing The Boundary Collar

Let:

```math
\Sigma_{\gamma}^{\mathrm{deep}}(\rho_R)
:=
\Sigma_\gamma
\setminus
\mathcal N_{\partial,\rho_R}(\gamma).
\tag{15.1013}
```

For fixed physical geometry:

```math
\operatorname{Area}_{\mathrm{phys}}
\left(
\Sigma_{\gamma}^{\mathrm{deep}}(\rho_R)
\right)
\ge
\operatorname{Area}_{\mathrm{phys}}(\Sigma_\gamma)
-
C_{\partial}(R,\ell_R)
\operatorname{Perim}_{\mathrm{phys}}(\gamma).
\tag{15.1014}
```

Thus an area-law bound in the deep interior implies (15.1012), after changing
the perimeter constant. This is why revealing a physical boundary collar is
compatible with fixed-IR confinement.

#### 15.69.3. Conditional Tile Disorder

Choose a fixed physical tiling of the deep sheet by center tiles:

```math
\mathcal T_{\gamma,R}
=
\left\{
T_1,\ldots,T_{N_{\gamma,R}}
\right\}.
\tag{15.1015}
```

The tiling is chosen after `R`, `ell_R`, and `rho_R` are fixed. It satisfies:

```math
N_{\gamma,R}
\ge
c_{\mathrm{tile}}(R,\ell_R)
\operatorname{Area}_{\mathrm{phys}}(\Sigma_\gamma)
-
C_{\mathrm{tile}}(R,\ell_R)
\operatorname{Perim}_{\mathrm{phys}}(\gamma).
\tag{15.1016}
```

Assume the sheet factor decomposes as:

```math
X_{\gamma,a}
=
X^{\partial}_{\gamma,a}
\prod_{j=1}^{N_{\gamma,R}}
\chi_{j,a},
\tag{15.1017}
```

where:

```math
X^{\partial}_{\gamma,a}
\text{ is }
\mathcal F^{\mathrm{cen}}_{\partial,\rho_R}(\gamma)
\text{ measurable},
\qquad
|X^{\partial}_{\gamma,a}|=1,
\qquad
|\chi_{j,a}|=1.
\tag{15.1018}
```

The fixed-IR center disorder input is a charged transfer contraction. Let:

```math
0<q_R<1.
\tag{15.1019}
```

For the ordered tile filtration, write:

```math
\mathcal G_0
:=
\mathcal F^{\mathrm{cen}}_{\partial,\rho_R}(\gamma),
\qquad
\mathcal G_j
:=
\mathcal G_0
\vee
\sigma(\chi_{1,a},\ldots,\chi_{j,a}).
\tag{15.1020}
```

The charged contraction condition is:

```math
\left\|
\mathbb E_{\mu^s_{\mathrm{cen},a}}
\left[
\chi_{j,a}F
\mid
\mathcal G_{j-1}
\right]
\right\|_{\infty}
\le
q_R
\left\|
\mathbb E_{\mu^s_{\mathrm{cen},a}}
\left[
F
\mid
\mathcal G_{j-1}
\right]
\right\|_{\infty}
\tag{15.1021}
```

for every bounded future observable:

```math
F\in L^{\infty}
\left(
\sigma(\chi_{j+1,a},\ldots,\chi_{N_{\gamma,R},a})
\vee
\mathcal G_0
\right).
\tag{15.1022}
```

This is a physical transfer estimate. It is not a plaquette-scale independence
assumption. It says that inserting one more deep center tile contracts the
boundary-conditioned charged transfer by a fixed factor.

**Criterion 40.154B (Charged Tile Transfer Proves Boundary-Stable Center
Disorder).** If (15.1016)-(15.1022) hold uniformly as the cutoff is removed,
then (15.1012) holds with:

```math
\sigma_R
=
-c_{\mathrm{tile}}(R,\ell_R)\log q_R.
\tag{15.1023}
```

#### Proof

Since `X_boundary` has unit modulus and is boundary measurable, it does not
change the conditional norm. Iterating (15.1021) from the last tile to the first
gives:

```math
\left\|
\mathbb E_{\mu^s_{\mathrm{cen},a}}
\left[
\prod_{j=1}^{N_{\gamma,R}}
\chi_{j,a}
\mid
\mathcal G_0
\right]
\right\|_{\infty}
\le
q_R^{N_{\gamma,R}}.
\tag{15.1024}
```

Therefore:

```math
\left|
M^{\mathrm{cen}}_{\gamma,a}
\right|
\le
q_R^{N_{\gamma,R}}
\tag{15.1025}
```

almost surely. Taking expectation and using (15.1016) yields:

```math
\mathbb E
\left[
\left|
M^{\mathrm{cen}}_{\gamma,a}
\right|
\right]
\le
\exp
\left(
-\sigma_R
\operatorname{Area}_{\mathrm{phys}}(\Sigma_\gamma)
+
\kappa_R
\operatorname{Perim}_{\mathrm{phys}}(\gamma)
\right),
\tag{15.1026}
```

with:

```math
\kappa_R
=
-C_{\mathrm{tile}}(R,\ell_R)\log q_R.
\tag{15.1027}
```

This is (15.1012), up to the cutoff error in the uniform transfer estimate. `∎`

#### 15.69.4. Free-Energy Gap Form

A common way to prove (15.1021) is a charged transfer free-energy gap. Let
the neutral and charged center transfer operators across tile `j` be:

```math
\mathcal T^{0}_{j,a},
\qquad
\mathcal T^{\chi}_{j,a}.
\tag{15.1028}
```

The boundary collar and previous interfaces are fixed. The required gap is:

```math
\left\|
\mathcal T^{\chi}_{j,a}
\right\|_{\infty\to\infty}
\le
e^{-m_R}
\left\|
\mathcal T^{0}_{j,a}
\right\|_{\infty\to\infty},
\qquad
m_R>0.
\tag{15.1029}
```

Then (15.1021) holds with:

```math
q_R=e^{-m_R}.
\tag{15.1030}
```

This is the center-disorder analogue of a dual mass or vortex-condensation
estimate. It is the part that is easy in the classical strong-coupling center
dual, and hard at the continuum fixed-IR floor.

#### 15.69.5. Failure Mode

Boundary-stable center disorder fails precisely if:

```math
\limsup_{a\downarrow0}
\exp
\left(
\sigma
\operatorname{Area}_{\mathrm{phys}}(\Sigma_\gamma)
-
\kappa
\operatorname{Perim}_{\mathrm{phys}}(\gamma)
\right)
\mathbb E_{\mu^s_{\mathrm{cen},a}}
\left[
\left|
M^{\mathrm{cen}}_{\gamma,a}
\right|
\right]
=
\infty
\tag{15.1031}
```

for every:

```math
\sigma>0.
\tag{15.1032}
```

Equivalently, after revealing the physical boundary collar, the center marginal
still remembers the deep sheet parity strongly enough to prevent area-order
decay. In transfer language this means:

```math
\limsup_{a\downarrow0}
\sup_j
\left\|
\mathcal T^{\chi}_{j,a}
\right\|_{\infty\to\infty}
\left\|
\mathcal T^{0}_{j,a}
\right\|_{\infty\to\infty}^{-1}
\ge
1.
\tag{15.1033}
```

This is a genuine center-sector obstruction, not an SO(3) cocycle obstruction.

#### 15.69.6. Completed Target 40.154

Target 40.154 is:

```math
\boxed{
\begin{array}{ll}
\mathrm{PASS}_{\mathrm{dual}}
&
\text{rewrite }(15.965)\text{ as the conditional norm }(15.1012),\\[1mm]
\mathrm{PASS}_{\mathrm{tile}}
&
\text{construct the fixed physical deep-sheet tiling }(15.1015)\text{-}(15.1017),\\[1mm]
\mathrm{PASS}_{\mathrm{gap}}
&
\text{prove the charged transfer gap }(15.1029),\\[1mm]
\mathrm{CONSEQUENCE}
&
\text{boundary-stable center disorder }(15.965)\text{ follows},\\[1mm]
\mathrm{FAIL}
&
\text{the boundary-conditioned center sheet has no positive charged gap.}
\end{array}}
\tag{15.1034}
```

Together with Target 40.153, this closes the two final inputs of Target 40.152:
amplitude center sensitivity and boundary-stable center disorder.

### 15.70. Target 40.155: Twisted Tile Free-Energy Gap For The Center Transfer

Searchable Target-40.155 tag:

`V4P40-TARGET-40155-TWISTED-TILE-FREE-ENERGY-GAP`.

Target 40.154 reduced boundary-stable center disorder to the charged transfer
gap (15.1029). We now express that gap as a fixed-IR twisted partition-function
ratio for one physical center tile. This is the most concrete way to attack the
center-side problem.

#### 15.70.1. Induced Center Marginal With SO(3) Fibers Integrated Out

At finite cutoff, for the exact positive SU(2) Gibbs law, the CLT3 positivity
gate is passed by pushforward rather than by a formal expansion. Write:

```math
d\mu^s_{\mathrm{cen},a}(b)
=
\frac{
Z^s_{\mathrm{SO3},a}(b)
}{
Z^s_a
}
d\nu^s_{\mathrm{cen},a}(b).
\tag{15.1035}
```

Here:

```math
Z^s_{\mathrm{SO3},a}(b)
:=
\int_{\mathcal F^s_a(b)}
\exp
\left(
-\mathcal A^s_a(b,\bar U)
\right)
d\lambda^s_a(\bar U).
\tag{15.1036}
```

The reference center measure is:

```math
\nu^s_{\mathrm{cen},a}.
\tag{15.1037}
```

Equation (15.1035) is not an independence assumption. The entire SO(3) fiber
free energy is inside the positive weight (15.1036). A signed or gauge-fixed
alternative representation would still have to pass this positivity test, but
the exact SU(2) pushforward does.

#### 15.70.2. Tile Interface Kernels

Fix one deep physical tile:

```math
T_j\in\mathcal T_{\gamma,R}.
\tag{15.1038}
```

Let:

```math
\omega_-,
\qquad
\omega_+
\tag{15.1039}
```

denote the incoming and outgoing center-interface data for that tile, including
the already revealed physical boundary collar and previous tile interfaces.

The neutral tile partition function is:

```math
Z^0_{j,a}(\omega_-,\omega_+)
:=
\sum_{\substack{
b_{T_j}\\
b_{T_j}\vert_{\partial_-T_j}=\omega_-\\
b_{T_j}\vert_{\partial_+T_j}=\omega_+
}}
Z^s_{\mathrm{SO3},a}
\left(
b_{T_j}\mid\omega_-,\omega_+
\right)
\nu^s_{\mathrm{cen},a}(b_{T_j}\mid\omega_-,\omega_+).
\tag{15.1040}
```

The charged tile partition function inserts the local sheet character:

```math
Z^{\chi}_{j,a}(\omega_-,\omega_+)
:=
\sum_{\substack{
b_{T_j}\\
b_{T_j}\vert_{\partial_-T_j}=\omega_-\\
b_{T_j}\vert_{\partial_+T_j}=\omega_+
}}
\chi_{j,a}(b_{T_j})
Z^s_{\mathrm{SO3},a}
\left(
b_{T_j}\mid\omega_-,\omega_+
\right)
\nu^s_{\mathrm{cen},a}(b_{T_j}\mid\omega_-,\omega_+).
\tag{15.1041}
```

The corresponding transfer kernels are:

```math
\mathcal T^0_{j,a}(\omega_-,\omega_+)
:=
Z^0_{j,a}(\omega_-,\omega_+),
\qquad
\mathcal T^{\chi}_{j,a}(\omega_-,\omega_+)
:=
Z^{\chi}_{j,a}(\omega_-,\omega_+).
\tag{15.1042}
```

The fixed-IR positivity requirement is:

```math
Z^0_{j,a}(\omega_-,\omega_+)>0
\tag{15.1043}
```

on every admissible interface pair in the physical tile atlas.

#### 15.70.3. Twisted Ratio Criterion

The physical twisted ratio is:

```math
\mathfrak r^{\chi}_{j,a}(\omega_-,\omega_+)
:=
\frac{
\left|
Z^{\chi}_{j,a}(\omega_-,\omega_+)
\right|
}{
Z^0_{j,a}(\omega_-,\omega_+)
}.
\tag{15.1044}
```

The desired fixed-IR gap is:

```math
\sup_{\substack{
j\\
\omega_-,\omega_+
}}
\mathfrak r^{\chi}_{j,a}(\omega_-,\omega_+)
\le
e^{-m_R}
+
o_a(1),
\qquad
m_R>0.
\tag{15.1045}
```

Equivalently, the charged free-energy excess obeys:

```math
\Delta F^{\chi}_{j,a}(\omega_-,\omega_+)
:=
-\log
\mathfrak r^{\chi}_{j,a}(\omega_-,\omega_+)
\ge
m_R
-
o_a(1).
\tag{15.1046}
```

**Criterion 40.155A (Twisted Tile Ratio Proves The Charged Transfer Gap).** If
(15.1043)-(15.1045) hold for the fixed physical tile atlas, then the charged
transfer gap (15.1029) holds with any:

```math
0<m'_R<m_R
\tag{15.1047}
```

for all sufficiently small cutoff.

#### Proof

Let `f` be any bounded future-interface observable. By (15.1042):

```math
\left|
\left(
\mathcal T^{\chi}_{j,a}f
\right)(\omega_-)
\right|
\le
\sum_{\omega_+}
\left|
Z^{\chi}_{j,a}(\omega_-,\omega_+)
\right|
\left|
f(\omega_+)
\right|.
\tag{15.1048}
```

Use the ratio bound (15.1045):

```math
\left|
\left(
\mathcal T^{\chi}_{j,a}f
\right)(\omega_-)
\right|
\le
\left(
e^{-m_R}
+
o_a(1)
\right)
\sum_{\omega_+}
Z^0_{j,a}(\omega_-,\omega_+)
\left|
f(\omega_+)
\right|.
\tag{15.1049}
```

Therefore:

```math
\left\|
\mathcal T^{\chi}_{j,a}f
\right\|_{\infty}
\le
\left(
e^{-m_R}
+
o_a(1)
\right)
\left\|
\mathcal T^0_{j,a}|f|
\right\|_{\infty}.
\tag{15.1050}
```

For small enough cutoff, the parenthesis is bounded by `e^{-m'_R}`. Taking the
supremum over bounded `f` gives (15.1029). `∎`

#### 15.70.4. How To Prove The Twisted Ratio

There are two honest routes.

The first is a free-energy route. Prove that the charged tile has a positive
fixed-IR free-energy cost:

```math
\left|
Z^{\chi}_{j,a}(\omega_-,\omega_+)
\right|
\le
e^{-m_R}
Z^0_{j,a}(\omega_-,\omega_+)
+
o_a(1)
\tag{15.1051}
```

uniformly over the physical interface atlas. This is the direct analogue of a
dual mass or vortex-condensation estimate.

The second is a conditional mixing route. Prove that, under the neutral tile law
with fixed interfaces:

```math
\left|
\mathbb E
\left[
\chi_{j,a}
\mid
\omega_-,\omega_+
\right]
\right|
\le
e^{-m_R}
+
o_a(1).
\tag{15.1052}
```

Since the left side is exactly the ratio (15.1044), (15.1052) proves (15.1045).

Both routes are fixed-IR only if the tile, interfaces, and smoothing radius are
physical objects chosen before taking the cutoff limit.

#### 15.70.5. ISP And Ontology-Free Readings

The ISP reading is that primitive center records should retain a nondegenerate
charged channel through each deep physical tile after boundary gluing is fixed.
The mathematical content is the same as (15.1045): the SO(3) fiber free energy
must not make the local center character predictable from the tile interfaces.

The ontology-free reading is purely lattice-theoretic:

```math
\boxed{
\begin{array}{c}
\text{start with the exact finite-cutoff SU(2) center/coset disintegration,}\\[1mm]
\text{integrate out SO(3) fibers to get the positive center marginal,}\\[1mm]
\text{prove the twisted tile ratio }(15.1045).
\end{array}}
\tag{15.1053}
```

No metaphysical premise is needed for the criterion. ISP may explain why these
variables are natural, but the proof obligation is the finite-dimensional
inequality (15.1045), uniform at fixed physical scale.

#### 15.70.6. Failure Mode

The fixed-IR charged gap fails if the SO(3) fiber can absorb the tile twist at
vanishing physical free-energy cost:

```math
\limsup_{a\downarrow0}
\sup_{\substack{
j\\
\omega_-,\omega_+
}}
\mathfrak r^{\chi}_{j,a}(\omega_-,\omega_+)
=
1.
\tag{15.1054}
```

Equivalently:

```math
\liminf_{a\downarrow0}
\inf_{\substack{
j\\
\omega_-,\omega_+
}}
\Delta F^{\chi}_{j,a}(\omega_-,\omega_+)
=
0.
\tag{15.1055}
```

This is the precise center-side obstruction to Target 40.154.

#### 15.70.7. Positive Center Marginal Is A Theorem At Finite Cutoff

The positivity part of Target 40.155 is not an additional physical hypothesis
once the finite-cutoff lifted measure is an honest positive SU(2) Gibbs
measure. It is a pushforward theorem.

Let the finite-cutoff SU(2) link space be:

```math
\Omega^{\mathrm{SU2}}_a
:=
\mathrm{SU2}^{E_a},
\qquad
\lambda^{\mathrm{SU2}}_a(\Omega^{\mathrm{SU2}}_a)=1.
\tag{15.1056}
```

The cutoff Gibbs law is:

```math
d\mu^s_a(U)
=
\frac{1}{Z^s_a}
\exp
\left(
-\mathcal A^s_a(U)
\right)
d\lambda^{\mathrm{SU2}}_a(U).
\tag{15.1057}
```

Fix a section and let the corresponding center-coordinate map be:

```math
\pi^s_{\mathrm{cen},a}
:
\Omega^{\mathrm{SU2}}_a
\longrightarrow
\mathcal B^s_a.
\tag{15.1058}
```

Define the center marginal by pushforward:

```math
\mu^s_{\mathrm{cen},a}
:=
\left(
\pi^s_{\mathrm{cen},a}
\right)_{\#}
\mu^s_a.
\tag{15.1059}
```

Choose the reference measure:

```math
\nu^s_{\mathrm{cen},a}
\tag{15.1060}
```

to have exactly the support allowed by the center constraints. Disintegrating
normalized Haar measure over the fibers of (15.1058) gives:

```math
Z^s_a
=
\int_{\mathcal B^s_a}
Z^s_{\mathrm{SO3},a}(b)
d\nu^s_{\mathrm{cen},a}(b),
\tag{15.1061}
```

with `Z^s_SO3,a` as in (15.1036). Hence:

```math
\frac{
d\mu^s_{\mathrm{cen},a}
}{
d\nu^s_{\mathrm{cen},a}
}
(b)
=
\frac{
Z^s_{\mathrm{SO3},a}(b)
}{
Z^s_a
}.
\tag{15.1062}
```

Because the integrand in (15.1036) is strictly positive on every nonempty
fiber:

```math
Z^s_{\mathrm{SO3},a}(b)>0
\qquad
\text{for every supported center configuration }b.
\tag{15.1063}
```

So (15.1035) is proved at finite cutoff. The only caveat is support: if an
interface pair is not admissible, the neutral tile weight is zero and the ratio
(15.1044) is not the right object. This is exactly why (15.1043) is part of
Target 40.155.

Section changes do not threaten the theorem. If `s` and `s'` are two measurable
sections, the total SU(2) integral is the same integral written in two
coordinate systems:

```math
(b,\bar U)_s
\longleftrightarrow
(b',\bar U)_{s'}.
\tag{15.1064}
```

The bare center coordinate changes, but the pushforward statement (15.1059) and
the fiber formula (15.1062) are repeated in the new coordinates. Thus the
criterion is section-covariant: the transported tile interfaces and transported
sheet insertion give the same numerical SU(2) cylinder integrals. What is not
section-invariant is an untransported statement about one bare coordinate
`b_p`.

#### 15.70.8. The Twisted Ratio Is Exactly Conditional Center Bias

For an admissible tile-interface pair define the neutral conditional tile law:

```math
d\mathbb P^0_{j,a}
\left(
b_{T_j}
\mid
\omega_-,
\omega_+
\right)
:=
\frac{
Z^s_{\mathrm{SO3},a}
\left(
b_{T_j}\mid\omega_-,\omega_+
\right)
d\nu^s_{\mathrm{cen},a}
\left(
b_{T_j}\mid\omega_-,\omega_+
\right)
}{
Z^0_{j,a}(\omega_-,\omega_+)
}.
\tag{15.1065}
```

Then (15.1041) is exactly:

```math
\frac{
Z^{\chi}_{j,a}(\omega_-,\omega_+)
}{
Z^0_{j,a}(\omega_-,\omega_+)
}
=
\mathbb E^0_{j,a}
\left[
\chi_{j,a}
\mid
\omega_-,
\omega_+
\right].
\tag{15.1066}
```

Consequently:

```math
\mathfrak r^{\chi}_{j,a}(\omega_-,\omega_+)
=
\left|
\mathbb E^0_{j,a}
\left[
\chi_{j,a}
\mid
\omega_-,
\omega_+
\right]
\right|.
\tag{15.1067}
```

Since the center character is `Z_2`-valued, set:

```math
p^{\pm}_{j,a}(\omega_-,\omega_+)
:=
\mathbb P^0_{j,a}
\left(
\chi_{j,a}=\pm1
\mid
\omega_-,
\omega_+
\right).
\tag{15.1068}
```

Then:

```math
\mathfrak r^{\chi}_{j,a}(\omega_-,\omega_+)
=
\left|
p^+_{j,a}(\omega_-,\omega_+)
-
p^-_{j,a}(\omega_-,\omega_+)
\right|
=
1
-
2
\min
\left\{
p^+_{j,a}(\omega_-,\omega_+),
p^-_{j,a}(\omega_-,\omega_+)
\right\}.
\tag{15.1069}
```

Therefore the twisted tile ratio (15.1045) is equivalent to the uniform
two-sidedness estimate:

```math
\inf_{\substack{
j\\
\omega_-,\omega_+
}}
\min
\left\{
p^+_{j,a}(\omega_-,\omega_+),
p^-_{j,a}(\omega_-,\omega_+)
\right\}
\ge
\frac{1-e^{-m_R}}{2}
-
o_a(1).
\tag{15.1070}
```

This is the clean fixed-IR form of the center-side problem: after the physical
interfaces are fixed, the center character crossing a deep tile must retain
both signs with a nonvanishing probability. The SO(3) fiber may bias the signs,
but it must not pin one of them.

The corresponding falsifier is equally explicit. If for some admissible
physical tile/interface sequence:

```math
\min
\left\{
p^+_{j,a}(\omega_-,\omega_+),
p^-_{j,a}(\omega_-,\omega_+)
\right\}
=
o_a(1),
\tag{15.1071}
```

then:

```math
\mathfrak r^{\chi}_{j,a}(\omega_-,\omega_+)
=
1-o_a(1),
\tag{15.1072}
```

and the charged transfer gap fails for that fixed physical tile atlas.

#### 15.70.9. Completed Target 40.155

Target 40.155 is now:

```math
\boxed{
\begin{array}{ll}
\mathrm{PROVED}_{\mathrm{pos}}
&
\text{the positive center marginal }(15.1035)\text{ follows from pushforward},\\[1mm]
\mathrm{EQUIV}_{\mathrm{ratio}}
&
\text{the twisted ratio is the conditional bias }(15.1067),\\[1mm]
\mathrm{TARGET}_{\mathrm{two}\text{-}\mathrm{sided}}
&
\text{prove the fixed-IR two-sidedness estimate }(15.1070),\\[1mm]
\mathrm{CONSEQUENCE}
&
\text{the charged transfer gap }(15.1029)\text{ follows},\\[1mm]
\mathrm{FAIL}
&
\text{one center sign is pinned as in }(15.1071).
\end{array}}
\tag{15.1073}
```

Together with Target 40.154, this gives the concrete center-marginal route to
boundary-stable center disorder. The remaining work is no longer formal or
coordinate-theoretic: prove or falsify the physical two-sidedness estimate
(15.1070), uniformly at fixed physical scale.
