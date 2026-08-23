# ISP v17 — U-Gen G1 relational-holonomy positive parent-law candidate

**Status:** ACTIVE AUTHOR-SIDE COMPILER/CONTROL / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none

---

## 0. Question and bounded answer

N1A is a bounded Nelson hostile control: its existing node-free fields cannot
recover global quantum circulation through a strictly cover-local
exact-germ-preserving repair. G1 does not inherit those fields or succeed N1A.
It independently tests a different compiler class:

> Can one ordinary-positive law on the complete physical experiment carry
> relative holonomy globally, without treating patchwise diffusion restarts
> or a wavefunction as the ontology?

G1 constructs the smallest finite conditional compiler of that type and then
audits its cost.

1. A typed action/holonomy history packet generates a normalized ordinary
   transition law for complete records.
2. The law is indivisible at unrecorded interference seams and becomes
   ordinarily divisible at genuine stable records.
3. A two-port loop gives the exact fringe law

   $$
   Gamma(\theta)=
   \begin{pmatrix}
   \cos^2(\theta/2)&\sin^2(\theta/2)\\
   \sin^2(\theta/2)&\cos^2(\theta/2)
   \end{pmatrix}
   $$

   using only positive output probabilities.
4. The construction lies outside N1A's class because its loop holonomy is
   global input to the whole experiment, not a consequence of local current
   germs. That is an input charge, not a repair or derivation.
5. It does **not** derive that holonomy, the action, magnitude law, record
   partition, or composition carrier. With standard quantum inputs it is a
   zero-gain history compiler.
6. Exact composition exposes the key cost: endpoint-normalized amplitude
   kernels are not closed under coherent concatenation. Closure for all
   coherent boundary data requires an isometric phase-complete carrier, while
   per-program renormalization sacrifices that functorial structure.

G1 is therefore a concrete positive compiler/control and an input-location
candidate theorem. It is not a native ISP unification.

---

## 1. Notation firewall

The Nelson control N1 uses the action-valued scale

$$
\kappa_A=2m\nu,
$$

which equals $\hbar$ at Nelson's quantum calibration. C3 used a coefficient
$\kappa_C$ with inverse-action units in $e^{i\kappa_C S}$. Throughout G1,

$$
\boxed{\chi(S)=e^{iS/\kappa_A}},
\qquad
\kappa_C=\kappa_A^{-1}.
$$

The two symbols must not be identified numerically without this inversion.

---

## 2. Physical parent packet

A finite G1 experiment is

$$
\mathcal E=
(X,R,\mathcal H,f,a,S,\kappa_A,
\mathsf{Div},\mathsf{Erase},\mathsf{Exec}).
$$

Its coordinates are:

1. $X$: registered source configurations at one admitted division boundary;
2. $R$: mutually exclusive stable output records;
3. $\mathcal H(r\leftarrow x)$: physical fine alternatives connecting $x$ to
   $r$, already quotiented by pure presentation relabelings;
4. $f:\mathcal H\to R$: the stable-record map;
5. $a(h)\geq0$: an amplitude-magnitude density, not yet a path probability;
6. $S(h)\in\mathbb R$: an additive action lift when one exists;
7. $\kappa_A>0$: the action scale;
8. $\mathsf{Div}$: physical boundaries at which a positive sufficient restart
   is licensed;
9. $\mathsf{Erase}$: coherent erasers that prevent a merely temporary mark
   from being promoted to a stable division; and
10. $\mathsf{Exec}$: the typed physical composition grammar.

The phase transport is

$$
\chi(h)=e^{iS(h)/\kappa_A}.
$$

More generally, $\chi$ may be a fixed $U(1)$ functor on the reversible part of
the experiment category even when no global real action lift exists.

### 2.1 Composition premises

For an unrecorded composable pair $h_2\circ h_1$, G1 requires

$$
a(h_2\circ h_1)=a(h_2)a(h_1),
\qquad
\chi(h_2\circ h_1)=\chi(h_2)\chi(h_1).
$$

The second equality follows from action additivity when

$$
S(h_2\circ h_1)=S(h_2)+S(h_1).
$$

These are physical premises. Endpoint probabilities do not derive them.

### 2.2 Presentation firewall

Duplicating a label for one physical alternative does not add a member to
$\mathcal H$. A genuine physical refinement must specify how its magnitudes
and phases recombine to the original arrow. G1 does not allow a list
multiplicity to manufacture interference intensity.

---

## 3. The parent law

For each source $x$ and stable record $r$, define the secondary coherent
potential

$$
K_{\mathcal E}(r,x)
=\sum_{h\in\mathcal H(r\leftarrow x)}a(h)\chi(h).
$$

Define

$$
W_{\mathcal E}(r,x)=|K_{\mathcal E}(r,x)|^2,
\qquad
Z_{\mathcal E}(x)=\sum_{r\in R}W_{\mathcal E}(r,x).
$$

For every admitted source column with $0<Z_{\mathcal E}(x)<\infty$, set

$$
\boxed{
\Gamma_{\mathcal E}(r\mid x)
=\frac{W_{\mathcal E}(r,x)}{Z_{\mathcal E}(x)}.}
$$

Then

$$
\Gamma_{\mathcal E}(r\mid x)\geq0,
\qquad
\sum_r\Gamma_{\mathcal E}(r\mid x)=1.
$$

For a contingent source distribution $p_X$, the actual record is sampled from

$$
p_R(r)=\sum_x\Gamma_{\mathcal E}(r\mid x)p_X(x).
$$

The candidate does not sample one member of $\mathcal H$. Fine alternatives
are summation referents in the law. A thick fine-history ontology would need a
separate joint probability law.

### 3.1 Calibrated versus renormalized members

A **calibrated** member has

$$
Z_{\mathcal E}(x)=1
$$

for every admitted $x$. A **renormalized** member uses the displayed quotient
with nonunit raw $Z_{\mathcal E}(x)$.

This distinction is load-bearing. Calibrated members can inherit a linear
composition carrier. Renormalized members always define one positive
whole-program record law, but their normalization can depend on the entire
experiment and need not respect sequential, tensor, or causal composition.

---

## 4. Proposition G1-A — positivity, gauge, and global holonomy

### Positivity

The parent law is column-stochastic by construction whenever every $Z(x)$ is
finite and nonzero.

### Endpoint gauge

For arbitrary $u_X(x),u_R(r)\in U(1)$, transform

$$
\chi(h)\longmapsto
u_R(f(h))\chi(h)u_X(x(h))^{-1}.
$$

Then

$$
K(r,x)\longmapsto u_R(r)K(r,x)u_X(x)^{-1},
$$

so $W$, $Z$, and $\Gamma$ are unchanged. Absolute endpoint phases are gauge.

### Loop holonomy

For a physical closed loop $\ell$ based at $x$,

$$
\operatorname{Hol}(\ell)=\chi(\ell)
$$

is invariant under endpoint gauge. Relative loop holonomy can therefore enter
the complete positive law even though no complex coordinate is ontic.

This is exactly how G1 escapes N1A's local theorem: $\chi(\ell)$ is global
experiment data. G1 has not derived it.

---

## 5. Proposition G1-B — unrecorded gluing and recorded division

### 5.1 Unrecorded seam

Let $\mathcal E_1:X\to Y$ and $\mathcal E_2:Y\to R$ compose through an
unrecorded seam $Y$. If every composite fine alternative factors uniquely and
the magnitude and phase premises of Section 2.1 hold, then

$$
K_{\mathcal E_2\circ\mathcal E_1}=K_{\mathcal E_2}K_{\mathcal E_1}.
$$

The proof is distributivity:

$$
\begin{aligned}
K_{21}(r,x)
&=\sum_y\sum_{h_2:r\leftarrow y}
\sum_{h_1:y\leftarrow x}
a(h_2)a(h_1)\chi(h_2)\chi(h_1)\\
&=\sum_yK_2(r,y)K_1(y,x).
\end{aligned}
$$

The corresponding positive matrices generally do not multiply:

$$
|K_2K_1|^{\odot2}
\neq
|K_2|^{\odot2}|K_1|^{\odot2}.
$$

That failure is interference nondivision, not a failure of positivity of the
complete parent record law.

### 5.2 Stable recorded seam

If $y$ is copied to a stable record, the complete boundary contains every
future-readable memory, and that boundary is independently certified as a
positive sufficient restart, alternatives with different $y$ no longer belong
to one coherent fiber. The licensed conditional law is

$$
\Gamma_{21}^{\rm rec}(r\mid x)
=\sum_y\Gamma_2(r\mid y)\Gamma_1(y\mid x).
$$

This is an ordinary stochastic division. Record stability alone is not enough:
an unresolved environment can retain operational memory even when $y$ is
permanent.

A temporary ancilla mark with a licensed coherent eraser is not automatically
in $\mathsf{Div}$. Otherwise G1 would destroy interference that a later
uncomputation restores.

---

## 6. Proposition G1-C — exact two-port holonomy member

Let the secondary carrier be the real rotation

$$
K(\theta)=
\begin{pmatrix}
\cos(\theta/2)&-\sin(\theta/2)\\
\sin(\theta/2)&\cos(\theta/2)
\end{pmatrix}.
$$

It obeys

$$
K(\theta_2)K(\theta_1)=K(\theta_1+\theta_2),
\qquad
K(\theta)^TK(\theta)=I.
$$

The positive parent law is

$$
\Gamma(\theta)=|K(\theta)|^{\odot2}
=
\begin{pmatrix}
\cos^2(\theta/2)&\sin^2(\theta/2)\\
\sin^2(\theta/2)&\cos^2(\theta/2)
\end{pmatrix}.
$$

Thus the source-port-$0$ record law is

$$
p(0\mid0,\theta)=\frac{1+\cos\theta}{2},
\qquad
p(1\mid0,\theta)=\frac{1-\cos\theta}{2}.
$$

At an unrecorded seam,

$$
\Gamma(\theta_2+\theta_1)
\neq
\Gamma(\theta_2)\Gamma(\theta_1)
$$

in general. For example,

$$
\Gamma(\pi/2)^2
=
\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix}
\neq
\begin{pmatrix}0&1\\1&0\end{pmatrix}
=\Gamma(\pi).
$$

This is a complete finite ordinary-positive indivisible law with a
phase-complete secondary representation. It is mathematically Barandes-like,
but it does not explain why nature chooses this rotation family.

### 6.1 Physical angle

For a two-arm experiment, a possible physical input is

$$
\theta_{\mathcal E}
=\frac{\Delta S_{\rm prop}+q\oint A}{\kappa_A}
+\beta_{\mathcal E},
$$

where $\beta_{\mathcal E}$ is separately calibrated apparatus transport.
This includes dynamical action and electromagnetic holonomy without treating
their gauge representatives as absolute.

Supplying this formula is a candidate source law, not its derivation. In
particular, $A$, $q$, $\kappa_A$, the apparatus term, and the history geometry
remain inputs.

---

## 7. Proposition G1-D — normalization/composition obstruction

Let $K:\mathbb C^X\to\mathbb C^R$ be a finite secondary kernel.

### Classical-column normalization

The raw endpoint weights satisfy

$$
\sum_r|K_{rx}|^2=1
$$

for every configuration source $x$ exactly when

$$
(K^\dagger K)_{xx}=1
$$

for every $x$.

### Coherent-boundary normalization

The stronger condition

$$
\|K\psi\|^2=\|\psi\|^2
$$

for every boundary vector $\psi$ holds exactly when

$$
\boxed{K^\dagger K=I.}
$$

For equal finite input and output dimensions, $K$ is then unitary. A real
carrier is orthogonal.

### Proof

The identity

$$
\|K\psi\|^2=\psi^\dagger K^\dagger K\psi
$$

shows sufficiency. If it equals $\psi^\dagger\psi$ for every complex $\psi$,
the polarization identity gives $K^\dagger K=I$. The column statement is the
same calculation restricted to basis vectors. $\square$

### Endpoint-normalized kernels are not compositionally closed

Let

$$
H=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
L_\alpha=
\begin{pmatrix}
1&\cos\alpha\\
0&\sin\alpha
\end{pmatrix},
$$

with $0<\alpha<\pi/2$. Every column of both matrices has unit norm, so each
defines a normalized positive endpoint matrix. But the two columns of
$L_\alpha H$ have squared norms

$$
1+\cos\alpha,
\qquad
1-\cos\alpha.
$$

Thus their coherent composite is not column-normalized.

G1 has two honest branches.

1. **Isometric branch:** require a phase-complete isometric carrier. This is
   compositionally clean but imports essentially quantum linear structure.
2. **Whole-program renormalized branch:** normalize each complete program
   only after coherent summation. This remains positive and indivisible, but
   its program-level normalization is additional global structure and must
   pass mixture, adaptation, tensor, no-signalling, and refinement tests.

Endpoint stochastic laws alone select neither branch and do not determine the
relative carrier data needed for $L_\alpha H$.

---

## 8. Proposition G1-E — fine-path actuality monotonicity wall

Suppose fine alternatives are mutually exclusive actual paths carrying one
context-independent Kolmogorov measure $\mu$, and a detector event is the
union of the paths that reach it. Then for disjoint path sets $A,B$,

$$
\mu(A\cup B)=\mu(A)+\mu(B)\geq\mu(A).
$$

Opening an additional exclusive path can never lower that detector
probability.

In a balanced two-path interferometer, one open arm gives probability $1/2$
at either output, while two open arms at destructive phase give probability
$0$ at one output. Therefore no context-independent additive fine-path measure
on the same path event algebra reproduces both contexts.

This does not refute:

1. ordinary positive probabilities on complete records;
2. a context-dependent fine-path law for each complete apparatus;
3. a non-Kolmogorov histories law;
4. Bohm/Nelson paths guided by additional global state; or
5. thin Barandes actuality only at licensed target/division events.

G1 adopts the last conservative option: the actual sampled referent is the
stable record. It does not claim one fine alternative occurred.

---

## 9. Proposition G1-F — endpoint positivity does not guarantee no-signalling

The $L_\alpha$ kernel from Proposition G1-D has the positive endpoint law

$$
\Gamma_{L_\alpha}
=
\begin{pmatrix}
1&\cos^2\alpha\\
0&\sin^2\alpha
\end{pmatrix},
$$

whose columns are normalized. Consider the correlated secondary boundary
vector

$$
|\Psi\rangle
=\frac{|0_A0_B\rangle+|1_A1_B\rangle}{\sqrt2}.
$$

If $B$ applies $L_\alpha$, the joint vector becomes

$$
|\Phi_\alpha\rangle
=\frac{
|0_A0_B\rangle
+\cos\alpha|1_A0_B\rangle
+\sin\alpha|1_A1_B\rangle}{\sqrt2}.
$$

It remains normalized, but tracing the $B$ record carrier gives

$$
\rho_A(\alpha)
=\frac12
\begin{pmatrix}
1&\cos\alpha\\
\cos\alpha&1
\end{pmatrix}.
$$

An $A$-side $|+\rangle$ reader therefore has probability

$$
p_A(+\mid\alpha)=\frac{1+\cos\alpha}{2},
$$

whereas the identity choice at $B$ leaves $p_A(+)=1/2$ for the original Bell
boundary state. The remote choice is detectable.

Thus a column-stochastic endpoint shadow does not make a non-isometric
secondary map an admissible local deterministic operation on correlated parent
systems. A no-signalling complete theory must restrict the carrier, add the
correct environment/record dilation, or supply another causal parent-law
mechanism. Endpoint positivity alone does none of those things.

This is not a Bell theorem and does not prove that every renormalized
whole-program law signals. It is an exact hostile member that any proposed G1
composition class must exclude for a physical reason.

---

## 10. The sector-origin ledger

N1A showed that a character cannot be extracted from the local density/current
germs. G1 does not demand that every sector be derived from nothing. It
requires one of four typed origins.

### 10.1 Dynamical connection

A physical gauge or geometric connection is part of the contingent field
state, and

$$
\chi(\ell)=\exp\left(iq\oint_\ell A/\kappa_A\right)
$$

is derived from that field and loop. The field law, coupling, and state remain
owed.

### 10.2 Kinematic or species sector

A fixed bundle/representation encodes statistics or species-level kinematics.
It is stable across the model's state space and must be empirically justified
or derived from deeper field content.

### 10.3 Contingent boundary or cosmological sector

The law admits several sectors and a boundary state selects one or supplies a
distribution over them. This is contingent input, not universal nomology.

### 10.4 Empirically modified sector dynamics

Transitions between sectors or noninteger circulation are new physics. Their
rates and apparatus predictions must freeze before data inspection.

Choosing a different character after seeing each state belongs to none of
these categories. It is post-hoc model selection.

---

## 11. Explanatory input ledger

| Coordinate | G1 status |
|---|---|
| source configurations $X$ | declared physical model input |
| stable records $R$ and $f$ | declared apparatus input |
| physical alternatives $\mathcal H$ | declared history carrier |
| magnitude density $a$ | unexplained generator input |
| action/holonomy $S$ or $\chi$ | calibrated, dynamical, kinematic, or contingent; not derived generally |
| action scale $\kappa_A$ | declared/calibrated |
| composition grammar | declared, with exact unrecorded gluing theorem |
| division versus eraser typing | physical apparatus input |
| normalization branch | isometry or global renormalization; not selected |
| actual stable record | ordinary random sample from $\Gamma_{\mathcal E}$ |
| fine actual path | not asserted |
| complete adaptive compiler | absent |
| empirical deviation | absent |

The standard quantum path/action member supplies every open row and therefore
passes as a zero-gain comparator. G1 earns explanatory credit only if a later
law derives at least one open coordinate from narrower independently physical
premises.

---

## 12. Hostile-control battery

1. **Potential-as-ontology:** call $K$ or $\chi$ a material wave merely because
   it is useful.
2. **Potential-as-explanation:** write $\Gamma=|K|^2$ after importing $K$ and
   claim quantum physics was derived.
3. **Action oracle:** fit a separate $S_{\mathcal E}$ to every target fringe.
4. **Magnitude oracle:** hide the target process in $a(h)$.
5. **Sector after fit:** choose $\chi$ from the observed spectrum.
6. **Endpoint gauge absolutism:** treat $u_R,u_X$ as physical.
7. **Holonomy erasure:** remove the loop character because local forces vanish.
8. **Label cloning:** duplicate a history label and change the intensity.
9. **Bookkeeping split:** split one stable record into two labels and change
   other record probabilities.
10. **Record/eraser conflation:** divide at a mark that a licensed future
    coherently erases.
11. **Hidden isometry:** assume $K^\dagger K=I$ while claiming only endpoint
    positivity.
12. **Renormalization silence:** use $Z_{\mathcal E}$ without testing
    composition and causal marginals.
13. **Fine-path sampling:** normalize $a(h)^2$ and ignore destructive
    interference.
14. **Context-free actuality:** demand one fixed additive path measure across
    open/closed-arm experiments.
15. **Rank-one promotion:** apply the scalar law to mixed boundaries or
    unresolved environments without a Gram-family extension.
16. **Tensor oracle:** receive the interacting parent kernel as an input.
17. **Adaptive oracle:** let future settings enter an earlier source packet.
18. **Classical-wave promotion:** infer single-event ontology from a classical
    wave fringe.
19. **Topology-to-spacetime leap:** identify experiment/configuration holonomy
    with emergent spacetime geometry.
20. **Gravity laundering:** insert a classical metric action and claim quantum
    gravity.

---

## 13. Exact controls still required

The companion control dossier
`v17_ugen_g1_exact_controls_and_native_slot_gate.md` now executes the full
registered battery. The original list is retained so no failed control is
silently deleted:

1. the two-port rotation/nondivision arithmetic;
2. the $L_\alpha H$ normalization obstruction;
3. endpoint-gauge invariance;
4. a label-clone quotient control;
5. retained-record versus coherent-eraser circuits;
6. a twisted-circle or Aharonov--Bohm holonomy member;
7. two independent systems and one interacting parent;
8. an adaptive feed-forward record;
9. a mixed/higher-rank boundary control;
10. the exact $L_\alpha$ no-signalling hostile mutant; and
11. a comparison with the C1 $D_\pm$ relational-orientation witness.

This document executes items 1--3 and 10 algebraically. The companion dossier
executes items 4--9 and 11, repeats the relevant earlier arithmetic, and finds
an exact semantic failure at item 9: scalar G1 is not closed under genuinely
mixed or higher-rank boundaries. The interacting-parent and coherent-adaptive
coordinates also remain conditional or open. G1 is therefore not freeze-ready
as a complete native generator.

---

## 14. QFT, spacetime, and gravity wall

The finite G1 packet presupposes a typed history carrier and action. A QFT
member would still need:

1. fields or variable-particle histories;
2. gauge quotient and anomaly control;
3. statistics sectors;
4. renormalized continuum measures;
5. local observable/record interfaces; and
6. relativistic causal composition.

A gravity member would additionally need:

1. histories containing geometry rather than histories on one fixed metric;
2. diffeomorphism-invariant boundaries and records;
3. constraint closure;
4. internal rather than supplied external time;
5. a measure and contour for Lorentzian geometry; and
6. reciprocal matter--geometry response recovering held-out GR limits.

Replacing the fixed action by the Einstein--Hilbert action would import, not
derive, the gravitational theory. G1 contains no gravity result.

---

## 15. Outcome ladder

| Level | Meaning |
|---|---|
| G1-L0 | positive normalization, gauge, or gluing algebra fails |
| G1-L1 | exact finite two-port indivisible parent law survives |
| G1-L2 | one physical sector source and record/eraser grammar survive |
| G1-L3 | tensor, adaptive, mixed-boundary, and no-signalling controls survive without target import |
| G1-L4 | one input among $a,S,\chi,\kappa_A$, composition, or records is derived from narrower physics |
| G1-L5 | scalable relativistic QFT and prospective empirical wedge survive |
| G1-L6 | internal time and reciprocal quantum matter--geometry dynamics survive |

G1-L1 is the present author-side candidate. The exact connection and
record/eraser controls supply conditional pieces of L2, but no level is
awarded without review. G1-L3 fails for the current scalar class because the
mixed-boundary and complete adaptive coordinates are absent.

---

## 16. Maximum legitimate author-side claim

If its executed controls survive future review, G1 could claim only:

> A global action/holonomy packet can generate an ordinary-positive
> indivisible record law for a finite complete experiment while treating its
> phase-complete carrier as secondary rather than ontic. Exact two-port
> interference and record-relative division follow. Endpoint normalization is
> not closed under coherent composition; uniform phase-complete isometries or
> additional whole-program normalization must be supplied. The construction
> therefore locates rather than derives the missing nomological structure.

It could not claim:

1. derivation of quantum theory from bare probability;
2. selection of a global character;
3. a complete Barandes parent-law compiler;
4. fine-path actuality;
5. a scalable interacting generator;
6. an empirical result;
7. QFT;
8. spacetime; or
9. gravity.

---

## 17. Author verdict

```text
FINITE POSITIVE PARENT LAW:        CONSTRUCTED CONDITIONALLY
TWO-PORT HOLONOMY FRINGE:         EXACT
UNRECORDED SEAM:                  INDIVISIBLE / POTENTIAL COMPOSES
STABLE RECORD SEAM:               POSITIVE DIVISION
GLOBAL HOLONOMY:                  SUPPLIED WITH TYPED ORIGIN / NOT DERIVED
POTENTIAL ONTOLOGY:               NOT ASSERTED
FINE ACTUAL PATH:                 NOT ASSERTED
ENDPOINT-NORMALIZED COMPOSITION:  FAILS IN GENERAL
ISOMETRIC BRANCH:                 CLEAN / PHASE-COMPLETE QUANTUM COST
RENORMALIZED BRANCH:              POSITIVE / COMPOSITION AND CAUSAL DEBT
COMPLETE ADAPTIVE COMPILER:       ABSENT
NATIVE ISP UNIFICATION:           ABSENT
EMPIRICAL WEDGE / QFT / GRAVITY:  NONE
OFFICIAL PIN / REVIEW / RESULT:   NONE
```
