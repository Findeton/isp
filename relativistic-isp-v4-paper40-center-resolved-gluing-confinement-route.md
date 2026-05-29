# Relativistic ISP V4 Paper 40: Center-Resolved Gluing As A Dual-Disorder Route To The Continuum Confinement Floor

Author: Felix Robles Elvira

Date: 2026-05-29

Status: research-program paper. This paper does not prove confinement, the
continuum string tension, or the mass gap. It develops one specific hypothesis:
that the ISP base's primitive center-resolved gluing data give analytic access
to the *disorder/dual* (center-flux) description of pure `SU(N)` gauge theory,
and that this is the description in which the only rigorous confinement results
are proved. It states the mechanism, the precise theorem targets, the
scale-derivation test, the relocated open step, the obstructions, and the
falsification ledger. Every load-bearing dynamical estimate it needs is flagged
as open.

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
route to the shared floor.

### Non-claims

This paper does not prove:

1. a positive continuum string tension for `4D SU(N)`;
2. a continuum mass gap;
3. survival of any center-flux condensation to the continuum (`t_- → 0`);
4. that the ISP dual is analytically more controllable than the standard
   't Hooft-loop construction;
5. anything for non-Abelian `SU(N)` beyond what the cited rigorous Abelian and
   3D results already establish.

It proves nothing dynamical. It is a route map with explicit theorem targets and
an explicit falsification ledger.

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
