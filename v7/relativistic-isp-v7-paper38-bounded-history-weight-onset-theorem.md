# Relativistic ISP v7 Paper XXXVIII: Bounded History Weight and Spacetime Onset

**Status:** analytic campaign note, not peer reviewed, version 2026-06-30.

Paper XXXVII found the correct fork:

$$
\boxed{
\text{records can click before spacetime exists, and spacetime appears only
when the same bounded history law admits a stable manifoldlike GR packet.}
}
$$

It also found a warning.  The first finite GR-facing packet helps prediction,
but it is too close to raw reconstruction.  Therefore the next campaign cannot
be another brute-force enumeration of larger orders.  It must define the
analytic law:

$$
\boxed{
\text{bounded partial objects}
\longrightarrow
\text{non-Markovian history weight }h_B
\longrightarrow
\text{projected click probabilities and, when stable, spacetime readouts.}
}
$$

This paper carries out that analytic campaign.

No decimal calculation is used in this paper.  All claims are formal finite
theorems, counterexamples, or named irreducible hypotheses.

## 1. Executive Result

The campaign proves the formal part and isolates the physical part.

The formal part is now clean:

$$
\boxed{
h_B\text{ is not a probability.}
\quad
\text{It is a positive history weight.}
}
$$

Probabilities arise only after projecting the bounded history weight onto the
partial record panel actually available to the experiment:

$$
\boxed{
\Pr_B(c\mid O_B=o)
=
\frac{
\sum_{H\in\Gamma_B:\ O_B(H)=o,\ S_B(H)=c} h_B(H)
}{
\sum_{H\in\Gamma_B:\ O_B(H)=o} h_B(H)
}.
}
$$

Here:

- `B` is the bounded record diamond: the experiment, instrument, and relevant
  record boundary, not the whole universe;
- `\Gamma_B` is the finite or effectively finite set of compatible bounded
  record histories for `B`;
- `H` is one compatible bounded history;
- `h_B(H)>0` is the non-probabilistic weight of that history;
- `O_B` is the partial control panel actually computed or observed;
- `o` is the value of that panel;
- `S_B(H)` is the next click/readout determined by the full history `H`.

The non-Markovian correction is also clean:

$$
\boxed{
h_B\text{ lives on bounded histories }H_{B,k},
\text{ not on }q_B(N)\text{ alone.}
}
$$

The law is not:

$$
h_N=K_N h_{N-1}.
$$

The law has the shape:

$$
\boxed{
h_B(H_{B,k})
\sim
\exp[-\mathcal A_B(H_{B,k})],
}
$$

where:

- `H_{B,k}` is a bounded history window of length `k`;
- `\mathcal A_B` is the boundary-work/action cost of that history;
- `k` is selected by a tail/residual principle, not fixed by hand.

Spacetime onset is a second projection of the same bounded histories:

$$
I_{GR}:\Gamma_B^{GR}\to\mathfrak G_B.
$$

Here:

- `\Gamma_B^{GR}` is the subset or phase of histories where a finite GR packet
  is defined;
- `\mathfrak G_B` is the space of finite GR packets;
- `I_GR(H)` is the finite spacetime readout of history `H`.

The onset criterion is:

$$
\boxed{
\mathcal E^{GR}_B(k,O)
=
\mathcal A^{GR}_B(k,O)
+
\mathcal M_B(k)
+
\sum_{j=k}^{\infty}\Delta^{GR}_{B,j}
\le
\epsilon_{GR}.
}
$$

Thus the campaign proves this conditional theorem:

$$
\boxed{
\text{given an intrinsic }h_B,\text{ admissible panels, and an intrinsic }
I_{GR},
\text{ the same bounded-history projection law yields both clicks and
spacetime onset.}
}
$$

It does not prove the final physical law.  The final physical law now reduces
to four irreducible construction problems:

1. derive the boundary-work potential `\psi_B` whose positive minimizer is
   `h_B`;
2. derive the admissible panel class from no-silent diamond centers, excluding
   raw lookup/reconstruction;
3. derive the intrinsic finite GR packet `I_GR` and prove its stability theorem;
4. derive the joint boundary scaling law that makes tolerance-relative
   closure predictive rather than arbitrary.

That is not a slogan. It is the exact remaining theorem boundary.

## 2. Bounded Partial Objects

A bounded object is not the whole world.

For a bounded experiment diamond `B`, define the partial record object:

$$
q_B(N)
=
\left(
\partial B_N,
\mathcal C_B(N),
\mathcal P_B(N),
\mathcal W_B(N),
\mathcal R_B(N)
\right).
$$

The terms are:

- `N` is the current record size inside the bounded problem;
- `\partial B_N` is the lower/upper/collar boundary of the bounded diamond;
- `\mathcal C_B(N)` is the no-silent diamond center;
- `\mathcal P_B(N)` is the selected positive nonreconstructive shadow;
- `\mathcal W_B(N)` is the scalar-work quotient when licensed;
- `\mathcal R_B(N)` is the unresolved residue ledger.

The residue ledger is important.  It prevents the bounded description from
pretending that the outside world does not exist.  Outside influence enters
through:

$$
\partial B_N
\quad\text{and}\quad
\mathcal R_B(N).
$$

This is the record version of experimental closure:

$$
\boxed{
\text{compute inside }B;\quad
\text{account for outside influence through boundary and residue.}
}
$$

### 2.1 Boundary Locality, Not Spatial Locality

Local does not mean "near in an already existing spacetime."  That would be
wrong before spacetime is licensed, and it would mishandle entanglement.

Local means:

$$
\boxed{
\text{local to the bounded record diamond and its admissible boundary
residue.}
}
$$

Therefore a long-range entanglement sector is inside the bounded object if it
has a committed boundary/center effect on the experiment.  It is outside only
if its influence is washed into the boundary residual.

## 3. Predictive Closure Boundary

The word "bounded" is still too weak unless the boundary is selected by a
closure rule.

The boundary must not mean an arbitrary box drawn by an observer.  It must mean
the smallest record diamond whose omission of exterior records changes the
prediction by less than the chosen tolerance.

For click prediction, define:

$$
\mathcal E^{click}_B(k,O)
=
\sum_{j=k}^{\infty}\Delta^{click}_{B,j}
+
A^{click}_{B,k}(O).
$$

Here:

- `\sum_{j=k}^{\infty}\Delta^{click}_{B,j}` is the click-relevant older
  history outside the included depth;
- `A^{click}_{B,k}(O)` is the information lost because the experiment sees only
  the partial panel `O`;
- the pair `(B,k,O)` is click-closed at tolerance `\epsilon_click` if:

  $$
  \mathcal E^{click}_B(k,O)\le\epsilon_{click}.
  $$

Thus the click boundary is:

$$
\boxed{
B^{click}_\epsilon
=
\operatorname*{argmin}_{B,k,O}
C_B(k,O)
\quad\text{subject to}\quad
\mathcal E^{click}_B(k,O)\le\epsilon_{click}.
}
$$

The minimization is over admissible expansions of the experiment diamond:
include more interior records, more collar records, more history depth, or a
richer observation panel only when doing so reduces the residual enough to
justify the added complexity.

In plain language:

> the click boundary is the smallest record boundary that makes the next click
> stable at the requested tolerance.

## 4. Spacetime-Like Closure Boundary

If a spacetime readout is licensed, there is a second closure condition:

$$
\mathcal E^{GR}_B(k,O)
=
\mathcal A^{GR}_{B,k}(O)
+
\mathcal M_B(k)
+
\sum_{j=k}^{\infty}\Delta^{GR}_{B,j}.
$$

The pair `(B,k,O)` is GR-closed at tolerance `\epsilon_GR` if:

$$
\mathcal E^{GR}_B(k,O)\le\epsilon_{GR}.
$$

The unification proposal is:

$$
\boxed{
\text{a spacetime-like experimental region is a record diamond whose same
boundary closes both clicks and GR readout.}
}
$$

Define the joint closure error:

$$
\boxed{
\mathcal E^{joint}_B(k,O)
=
\alpha\,\mathcal E^{click}_B(k,O)
+
\beta\,\mathcal E^{GR}_B(k,O)
+
\gamma\,C_B(k,O).
}
$$

The constants `\alpha,\beta,\gamma` are weights of units/tolerance.  They do not
define the physics; they encode the requested accuracy and complexity tradeoff.

The spacetime-like closure diamond is:

$$
\boxed{
B^{ST}_{\epsilon}
=
\operatorname*{argmin}_{B,k,O}
C_B(k,O)
}
$$

subject to:

$$
\boxed{
\mathcal E^{click}_B(k,O)\le\epsilon_{click},
\qquad
\mathcal E^{GR}_B(k,O)\le\epsilon_{GR}.
}
$$

Equivalently, one can minimize `\mathcal E^{joint}` with hard upper bounds on
the two errors.

This is stronger than Paper XXXVII's onset statement.  It says not merely that
click and GR projections live on the same history weight, but that a
spacetime-like region is precisely a joint closure region:

$$
\boxed{
\text{spacetime regions are predictively closed record diamonds.}
}
$$

## 5. Boundary Ramifications

This section follows the new boundary idea through the main physical cases.

### 5.1 Flat-Lab Regime

An ideal flat-lab approximation is the case where a small collar and short
history depth close both errors:

$$
\mathcal E^{click}_B\le\epsilon_{click},
\qquad
\mathcal E^{GR}_B\le\epsilon_{GR},
$$

with small:

$$
\mathcal M_B,
\qquad
\sum_{j=k}^{\infty}\Delta^{GR}_{B,j},
\qquad
\mathcal R_B.
$$

The flat lab is not assumed. It is a regime where the boundary residue is
regular and cheap.

### 5.2 Massive-Object Regime

Near a massive object, the click boundary may still close locally, but the GR
boundary usually requires a larger collar or richer transport packet.  In
record terms, the boundary shows:

- stronger interval-height distortion;
- stronger transport drift between overlapping diamonds;
- nontrivial closed-loop defect;
- larger Ward/Bianchi source residue;
- possible clock/frame mismatch in the finite packet.

Thus:

$$
B^{ST}_{\epsilon}(\text{near mass})
$$

is expected to be larger or richer than:

$$
B^{ST}_{\epsilon}(\text{flat lab}).
$$

The difference is not inserted as a background metric.  It appears as a higher
joint closure cost.

### 5.3 Horizon or Black-Hole Regime

Near a horizon-like boundary, joint closure may become asymmetric.

Record-intrinsically, this means:

- the incoming boundary `\partial^-B` and outgoing boundary `\partial^+B` do
  not have symmetric deletion/insertion transport;
- some exterior records affect the interior without reciprocal recovery in the
  chosen bounded panel;
- the history tail for GR may decay more slowly than the click tail;
- the same click-stable experiment may fail to be GR-closed at the same collar
  depth.

So the formal signal of a horizon-like situation is not "large gravity" as a
background assumption.  It is:

$$
\boxed{
\mathcal E^{click}_B\le\epsilon_{click}
\quad\text{but}\quad
\mathcal E^{GR}_B>\epsilon_{GR}
}
$$

unless the boundary is enlarged or the panel is enriched.

### 5.4 Entangled Experiment

An entangled setup may require records that are not spatially near after
spacetime onset.  The joint boundary rule handles this because the boundary is
not metric-neighborhood-first.

If a distant record sector changes the click law through the diamond center,
then it belongs inside `B` or in a licensed residue sector:

$$
\text{entangled sector}
\in
B
\quad\text{or}\quad
\mathcal R_B.
$$

The experiment is predictively closed only if the remaining residue is below
tolerance.

### 5.5 Pre-Spacetime Regime

Before spacetime onset, only the click closure condition is required:

$$
\mathcal E^{click}_B\le\epsilon_{click}.
$$

The GR closure condition may be undefined or fail:

$$
I_{GR}\ \text{undefined}
\quad\text{or}\quad
\mathcal E^{GR}_B>\epsilon_{GR}.
$$

Thus pre-spacetime is not "bad spacetime."  It is the phase where click closure
exists without joint spacetime closure.

## 6. Bounded Histories

A bounded history window is:

$$
H_{B,k}
=
\left(
q_B(N-k),
q_B(N-k+1),
\ldots,
q_B(N);
\tau_{N-k+1},\ldots,\tau_N
\right).
$$

Here:

- `k` is the history depth;
- `q_B(j)` is the partial object at record size `j`;
- `\tau_j` is the deletion/insertion/refinement transport from
  `q_B(j-1)` to `q_B(j)`.

The transports matter.  Without them, the same sequence of panel labels could
hide different boundary work.

Let:

$$
\Gamma_{B,k}
$$

be the set of compatible histories of length `k` ending at the current bounded
diamond.

The full bounded history set is the projective union:

$$
\Gamma_B
=
\varprojlim_k \Gamma_{B,k}
$$

when the limit exists, or the finite effective union up to the selected history
range when it does not.

The important point is:

$$
\boxed{
\Gamma_B\text{ is not the whole universe.}
}
$$

It is the compatible history cylinder for the bounded record problem.

## 7. The History Weight

The analytic law begins with a positive weight:

$$
h_B:\Gamma_B\to\mathbb R_{>0}.
$$

This is not a probability.  It is a compatibility/action weight.

The expected physical form is:

$$
h_B(H)
=
\exp[-\mathcal A_B^{hist}(H)].
$$

The history action should decompose as:

$$
\mathcal A_B^{hist}(H)
=
\Psi_B(H)
+
\Lambda_B(H)
+
X_B(H).
$$

The terms mean:

- `\Psi_B(H)` is no-silent boundary work;
- `\Lambda_B(H)` is deletion/insertion/refinement drift work;
- `X_B(H)` is unresolved licensed residue work.

This formula intentionally does not include a hand-made reconstruction penalty.
Reconstruction penalty enters at the panel level, not the history level:

$$
C_B(k,O).
$$

The final missing object from Papers XXXIII-XXXV is:

$$
\boxed{
\psi_B
}
$$

the primitive boundary-work potential whose positive minimizer produces this
`h_B`.

## 8. Projection Gives Probability

Let:

$$
O_B:\Gamma_B\to\mathcal O_B
$$

be an admissible observation/control panel.

The weight of a set of histories is:

$$
h_B(A)
=
\sum_{H\in A}h_B(H).
$$

The projected probability of a future click `c` is:

$$
\boxed{
\Pr_B(S_B=c\mid O_B=o)
=
\frac{
h_B(\{H:O_B(H)=o,\ S_B(H)=c\})
}{
h_B(\{H:O_B(H)=o\})
}.
}
$$

This is the exact place where stochastic language enters.

If the full history `H` were known and `S_B(H)` were deterministic, then:

$$
\Pr_B(S_B=c\mid H)
\in
\{0,1\}.
$$

But the partial panel `O_B=o` usually corresponds to many compatible histories.
The probability is the normalized weight of those histories.

So the law is:

$$
\boxed{
\text{deterministic full-history readout}
\quad+\quad
\text{bounded projection}
\quad=\quad
\text{effective probability.}
}
$$

## 9. The Non-Markovian Tail Bound

For a history depth `k`, define the click kernel:

$$
K_{B,k}(c)
=
\Pr_B(S_B=c\mid H_{B,k}).
$$

This is the prediction if the full bounded history window of length `k` is
known.

Define the history increment:

$$
\Delta^{click}_{B,k}
=
\mathbb E_h\,
TV(K_{B,k+1},K_{B,k}).
$$

Here:

- `TV` is total-variation distance;
- `K_{B,k+1}` uses one more older history layer;
- `K_{B,k}` omits that layer;
- `\mathbb E_h` is expectation with respect to normalized `h_B` on the bounded
  history cylinder.

### Theorem 1: Non-Markovian Tail Bound

For any `L>k`:

$$
\boxed{
\mathbb E_h\,TV(K_{B,L},K_{B,k})
\le
\sum_{j=k}^{L-1}\Delta^{click}_{B,j}.
}
$$

**Proof.**

For each compatible history path, the triangle inequality gives:

$$
TV(K_{B,L},K_{B,k})
\le
\sum_{j=k}^{L-1}
TV(K_{B,j+1},K_{B,j}).
$$

Taking `h_B`-weighted expectation gives the result.  No Markov assumption is
used. `\square`

Thus the sufficient history depth at tolerance `\epsilon` is:

$$
\boxed{
m_B^{click}(\epsilon)
=
\min\left\{
k:
\sum_{j=k}^{\infty}\Delta^{click}_{B,j}
\le
\epsilon
\right\}.
}
$$

This is a formula-level replacement for brute force.  The missing physical
theorem is a record-intrinsic bound on `\Delta^{click}_{B,j}`.

## 10. Partial Observation Bound

Experiments do not see the full `H_{B,k}`.  They see:

$$
O_{B,k}
=
\Phi(H_{B,k}).
$$

Define:

$$
K^O_{B,k}(c)
=
\Pr_B(S_B=c\mid O_{B,k}).
$$

Define the partial-panel residual:

$$
A^{click}_{B,k}(O)
=
\mathbb E_h\,TV(K_{B,k},K^O_{B,k}).
$$

### Theorem 2: History Tail Plus Partial Panel

For any `L>k`:

$$
\boxed{
\mathbb E_h\,TV(K_{B,L},K^O_{B,k})
\le
\sum_{j=k}^{L-1}\Delta^{click}_{B,j}
+
A^{click}_{B,k}(O).
}
$$

**Proof.**

Use:

$$
TV(K_{B,L},K^O_{B,k})
\le
TV(K_{B,L},K_{B,k})
+
TV(K_{B,k},K^O_{B,k}).
$$

The first term is bounded by Theorem 1.  The second term is the definition of
`A^{click}_{B,k}(O)`. `\square`

This theorem is the analytic version of "probability from partial `W_N`."

It says the experimental error has exactly two sources:

$$
\boxed{
\text{uncomputed older history}
\quad+\quad
\text{unobserved part of the included history.}
}
$$

## 11. Pre-Spacetime Click Panel

The pre-spacetime click action is:

$$
\boxed{
\mathcal A_B^{pre}(k,O)
=
\sum_{j=k}^{\infty}\Delta^{click}_{B,j}
+
A^{click}_{B,k}(O)
+
\eta C_B(k,O).
}
$$

The selected pre-spacetime panel is:

$$
\boxed{
(k_B^{pre},O_B^{pre})
=
\operatorname*{argmin}_{k,O\in\mathfrak A_B}
\mathcal A_B^{pre}(k,O).
}
$$

Here:

- `\mathfrak A_B` is the admissible panel class;
- `C_B(k,O)` is the no-hidden-presentation complexity of using history depth
  `k` and panel `O`;
- `\eta>0` is the complexity weight.

This panel is defined even when no spacetime readout exists.

So:

$$
\boxed{
\text{records can click before spacetime.}
}
$$

## 12. Spacetime Packet as a Second Projection

When licensed, define:

$$
I_{GR}:\Gamma_B^{GR}\to\mathfrak G_B.
$$

The finite GR packet should have the form:

$$
I_{GR}(H)
=
\left(
Q_H,
U_H,
F_H,
\nabla F_H,
\Theta_H,
r_H
\right).
$$

The terms mean:

- `Q_H` is the interval/volume/height/layer/center packet;
- `U_H` is finite transport between overlapping diamond frames;
- `F_H` is closed-loop transport defect;
- `\nabla F_H` is finite curvature-difference data;
- `\Theta_H` is typed Ward/Bianchi source residue;
- `r_H` is the refinement/cofinality map.

This packet must be constructed from diamonds, centers, boundaries, and
history transports.  It may not use continuum coordinates.

The conditional GR residual is:

$$
\mathcal A^{GR}_{B,k}(O)
=
\mathbb E_h\,
d_{GR}\!\left(
I_{GR}(H),
\operatorname{Law}_h(I_{GR}\mid O_{B,k})
\right).
$$

Equivalently, for a finite packet label metric, this is the conditional
within-cell spread of `I_GR`.

Define the GR history increment:

$$
\Delta^{GR}_{B,k}
=
\mathbb E_h\,
d_{GR}\!\left(
I_{GR}(H_{B,k+1}),
I_{GR}(H_{B,k})
\right).
$$

Define the manifold/Ward defect:

$$
\mathcal M_B(k)
=
M_{\rm dim}
+
M_{\rm interval}
+
M_{\rm shell}
+
M_{\rm drift}
+
M_{\rm Ward}.
$$

The terms test:

- dimension consistency;
- recursive interval heredity;
- shell/density regularity;
- deletion/insertion stability;
- Ward/Bianchi residue typed as source rather than hidden failure.

The spacetime-onset defect is:

$$
\boxed{
\mathcal E^{GR}_B(k,O)
=
\mathcal A^{GR}_{B,k}(O)
+
\mathcal M_B(k)
+
\sum_{j=k}^{\infty}\Delta^{GR}_{B,j}.
}
$$

## 13. Onset Theorem

Define a stable finite spacetime readout at tolerance `\epsilon` to mean:

there exists an admissible history/panel pair `(k,O)` such that:

1. `I_GR` is defined on the relevant compatible histories up to an
   `h_B`-null or negligible set;
2. conditional GR spread is small:

   $$
   \mathcal A^{GR}_{B,k}(O)\le\epsilon_1;
   $$

3. manifold/Ward defect is small:

   $$
   \mathcal M_B(k)\le\epsilon_2;
   $$

4. older-history GR drift is small:

   $$
   \sum_{j=k}^{\infty}\Delta^{GR}_{B,j}\le\epsilon_3;
   $$

with:

$$
\epsilon_1+\epsilon_2+\epsilon_3\le\epsilon.
$$

### Theorem 3: Spacetime Onset Criterion

Under the definitions above:

$$
\boxed{
\mathcal E^{GR}_B(k,O)\le\epsilon
\quad\Longleftrightarrow\quad
(k,O)\text{ gives a stable finite spacetime readout at tolerance }\epsilon.
}
$$

**Proof.**

The forward implication is immediate by splitting the nonnegative summands of
`\mathcal E^{GR}`.  The reverse implication is exactly the definition of stable
readout with the same three nonnegative error channels. `\square`

This theorem is formal, but useful: it prevents the campaign from confusing
three different failures.

If spacetime does not appear, the failure must be one of:

1. `I_GR` is not defined;
2. `I_GR` is too spread out under the available panel;
3. the order is not manifoldlike/Ward-stable;
4. older history still changes the GR readout.

## 14. Joint Selection Theorem

In the spacetime-licensed phase, define:

$$
\mathcal A_B^{total}(k,O)
=
\mathcal A_B^{pre}(k,O)
+
\mu\mathcal A^{GR}_{B,k}(O)
+
\nu\mathcal M_B(k)
+
\rho\sum_{j=k}^{\infty}\Delta^{GR}_{B,j}.
$$

The admissible minimizer is:

$$
\boxed{
(k_B^*,O_B^*)
=
\operatorname*{argmin}_{k,O\in\mathfrak A_B}
\mathcal A_B^{total}(k,O).
}
$$

### Theorem 4: Least-Complex Sufficient Panel in the Exact Finite Case

Assume:

1. `\Gamma_B` is finite;
2. `h_B(H)>0` for every compatible history;
3. `\mathfrak A_B` is a finite family of panels;
4. `C_B` is strictly increasing under strict refinement;
5. there exists at least one panel in `\mathfrak A_B` that makes both `S_B` and
   `I_GR` measurable.

Then, in the lexicographic limit where zero residual is prioritized over
complexity, every minimizer is a least-complex admissible panel sufficient for
both:

$$
S_B
\quad\text{and}\quad
I_{GR}.
$$

If the sufficient admissible panels contain a unique coarsest element, then
that element is the minimizer.

**Proof.**

For a finite positive weighted space, the residual
`\mathcal A^{click}_{B,k}(O)` is zero iff `S_B` is constant on each positive
weight atom of `O`.  Likewise, `\mathcal A^{GR}_{B,k}(O)` is zero iff `I_GR` is
constant on each positive weight atom of `O`.  Therefore the panels with zero
joint residual are exactly the admissible panels that refine the joint target
partition:

$$
H\mapsto(S_B(H),I_{GR}(H)).
$$

Because `\mathfrak A_B` is finite and at least one zero-residual panel exists,
the zero-residual family has at least one `C_B`-minimizer.  Lexicographic
minimization selects one of those panels.  If a unique coarsest sufficient
admissible panel exists, every other zero-residual panel is a strict refinement
of it or has no lower complexity; strict refinement monotonicity of `C_B` then
makes the coarsest panel the unique least-complex minimizer. `\square`

This theorem proves the formal selection principle.

It does not identify the physical panel.  That requires the admissible class
`\mathfrak A_B` and the physical packet `I_GR`.

## 15. Why One-Step Markov Recurrence Is False

The Markov shortcut would say:

$$
\Pr(S_B\mid H_{B,k})
=
\Pr(S_B\mid q_B(N)).
$$

This is false in general.

### Counterexample

Let histories be pairs:

$$
H=(a,b),
\quad
a,b\in\{0,1\}.
$$

Let the current partial object be:

$$
q_B(N)=b.
$$

Let the next click be:

$$
S_B=a.
$$

Then two histories:

$$
(0,b)
\quad\text{and}\quad
(1,b)
$$

have the same current object but different clicks.  Therefore no function of
`q_B(N)` can determine `S_B`.

If the history weight is positive on both histories, then:

$$
\Pr(S_B=1\mid q_B(N)=b)
$$

is a projection average over unresolved histories, not a deterministic
one-step law.

This is the analytic version of the Paper XXXVI finite finding:

$$
\boxed{
\text{the record law is history-functional, not one-step Markov.}
}
$$

## 16. Why Raw Reconstruction Is Not the Law

The opposite shortcut is to use the full history:

$$
O_B(H)=H.
$$

Then every deterministic target is measurable, so all residuals vanish.

This is also not the law, because it fails no-hidden-presentation discipline.

The admissible class must exclude raw lookup by at least one of:

1. generation from bounded diamond-center operators;
2. covariance under record isomorphism;
3. deletion/insertion drift stability;
4. atom-count or description-complexity bound;
5. no reference to hidden presentation multiplicity.

Thus the real law must live between:

$$
\boxed{
\text{too small: } W_N
\qquad
\text{and}
\qquad
\text{too large: } R_N.
}
$$

Paper XXXVII found exactly this finite warning:

$$
W_N
\preceq
G_N^{coarse}
\prec
R_N.
$$

## 17. Admissible Panels

The campaign needs a concrete admissibility rule.

An observation panel `O` belongs to `\mathfrak A_B` only if it is generated by a
finite list of bounded diamond operators:

$$
O
=
\sigma(\mathcal O_1,\ldots,\mathcal O_m).
$$

Each operator must satisfy:

1. **Record covariance.**
   It is invariant under relabeling/isomorphism of committed records.

2. **Boundary locality.**
   It depends only on the bounded diamond, its collar, its center, and licensed
   residue sectors.

3. **No hidden presentation.**
   It does not use presentation counts, construction labels, coordinates, or
   machine states except through committed record projections.

4. **Deletion/insertion stability.**
   It has controlled drift:

   $$
   d_O(O(q_{j+1}),O(q_j))
   \le
   L_O\,\operatorname{BW}(q_{j+1},q_j)
   +
   r_O(j).
   $$

5. **Nonlookup complexity.**
   Its atom count or description complexity is strictly smaller than raw order
   lookup unless raw lookup is forced by the target.

This gives an analytic version of "local enough in terms of spacetime" without
assuming spacetime.  The locality is causal-diamond/boundary locality first;
spacetime locality is allowed only after onset.

## 18. Candidate Coarse GR Packet

Paper XXXVII's naive packet:

$$
G_N
=
(\#\mathrm{relations},h,w,\mathrm{interval},\mathrm{degree},
\mathrm{matching},\mathrm{layer})
$$

was useful but too reconstructive.

The analytic replacement is:

$$
\boxed{
G_B^{coarse}
=
\sigma(
\operatorname{CenterShell},
\operatorname{BoundaryInterval},
\operatorname{TransportDrift},
\operatorname{WardResidue},
\operatorname{RefinementStability}
).
}
$$

The components are:

- `CenterShell`: histograms of no-silent center residues across nested
  intervals;
- `BoundaryInterval`: interval sizes/heights compressed relative to the
  boundary/collar, not raw global profiles;
- `TransportDrift`: deletion/insertion transport disagreement;
- `WardResidue`: closed-loop defect typed by source class;
- `RefinementStability`: cofinal stability under bounded refinement.

This is still a theorem target, not a finished construction.  The admissibility
test is:

$$
\boxed{
W_B
\preceq
G_B^{coarse}
\prec
R_B,
}
$$

and:

$$
\boxed{
\mathcal A^{GR}(G_B^{coarse})
\ll
\mathcal A^{GR}(W_B),
\qquad
C_B(G_B^{coarse})
\ll
C_B(R_B).
}
$$

## 19. The Full Campaign Attacks

This section follows every opening to its end.  Each attack either proves a
formal result, falsifies a shortcut, or names an irreducible hypothesis.

### Attack 1: "Use `h_N` from `h_{N-1}`."

Falsified.

The counterexample in Section 15 proves that the current partial object need
not determine the future click.  The law must use bounded histories:

$$
H_{B,k}.
$$

Opening followed: perhaps a finite `k` always suffices.

Result: finite `k` suffices only if:

$$
\sum_{j=k}^{\infty}\Delta^{click}_{B,j}
\le
\epsilon.
$$

Thus the next theorem is a decay/bound theorem for `\Delta^{click}`.

### Attack 2: "Use full history."

Falsified as law.

Full history makes every deterministic target measurable, but it is raw
reconstruction.  It violates no-hidden-presentation unless raw detail is forced
by the physical target.

Opening followed: maybe complexity penalty is arbitrary.

Result: if `C_B` is arbitrary, the law is arbitrary.  Therefore `C_B` must be
derived from admissibility: atom count, operator description length,
deletion-drift Lipschitz cost, and no-hidden-presentation.

Irreducible hypothesis:

$$
\boxed{
C_B\text{ must be generated by the diamond-center admissibility class.}
}
$$

### Attack 3: "Use scalar work as spacetime."

Falsified.

Paper XXXVII showed:

$$
\mathcal A^{GR}(W_4)
>
\mathcal A^{GR}(WG_4)
$$

in the exact `N=8` audit, and:

$$
\mathcal A^{GR}(W_1)
>
\mathcal A^{GR}(G_1)
$$

in the exact `N=9` current-panel audit.

Opening followed: add all intrinsic order/count/layer features.

Result: naive `G` approaches raw reconstruction.  Therefore the physical
packet must be coarser:

$$
G_B^{coarse}.
$$

### Attack 4: "Probability is primitive."

Rejected.

The projected probability formula is derived from positive weights:

$$
h_B(H)
$$

by normalization over compatible histories.  The stochastic object is the
observer's projected law on `O_B`, not the primitive full-history law.

Opening followed: maybe complex phases are needed.

Result: complex phases, if real, belong upstream of committed records.  This
paper's `h_B` is the positive record-projected weight after commitment.  A
future complex-amplitude theory must reproduce this positive projected
history weight, not replace the experimental probability formula.

### Attack 5: "Spacetime should exist at the first record."

Rejected.

The pre-spacetime panel:

$$
\mathcal Q_B^{pre}
$$

is selected by:

$$
\mathcal A_B^{pre}.
$$

No `I_GR` is required.  Spacetime is licensed only if:

$$
\mathcal E^{GR}_B\le\epsilon_{GR}.
$$

Opening followed: maybe this merely defines onset.

Result: yes, the formal criterion is definitional unless `I_GR`, `d_GR`,
`\mathcal M`, and `\Delta^{GR}` are derived intrinsically.  That is the second
irreducible hypothesis:

$$
\boxed{
\text{derive the finite GR packet and stability scores from record diamonds.}
}
$$

### Attack 6: "Exact zero drift is required."

Rejected.

Finite records should not require exact zero drift.  The correct requirement is
controlled tail:

$$
\sum_{j=k}^{\infty}\Delta_{B,j}
\le
\epsilon.
$$

Opening followed: maybe the tail never decays.

Result: then the bounded experiment is not closed at tolerance `\epsilon`.
That is a physical failure of isolation, not a mathematical inconsistency.

### Attack 7: "Entanglement violates locality."

Rejected after replacing spatial locality with boundary locality.

Entanglement is inside the bounded object if it crosses the diamond center or
boundary residue.  It is outside only if it leaves no unresolved effect beyond
the residual term.

Thus admissible locality is:

$$
\boxed{
\text{record-boundary locality}
\quad\text{not}\quad
\text{pre-assumed metric locality.}
}
$$

### Attack 8: "The onset theorem is tautological."

Partly sustained.

The formal equivalence in Theorem 3 is a bookkeeping theorem.  It does not
derive physical spacetime.  The physical content lies in deriving:

$$
I_{GR},\quad d_{GR},\quad \mathcal M,\quad \Delta^{GR}
$$

from record diamonds.

Opening followed: can the current paper prove those?

Result: not without adding a new physical axiom or importing the v4 finite GR
reconstruction theorem.  Therefore this campaign ends in a valid decomposition
into irreducible construction axioms, not in an unjustified proof.

### Attack 9: "Click boundary and spacetime boundary should be separate."

Rejected in the spacetime-like phase, sustained in the pre-spacetime phase.

Before spacetime onset, only click closure is meaningful:

$$
\mathcal E^{click}_B\le\epsilon_{click}.
$$

After spacetime is licensed, a region deserves the name spacetime-like only if
the same bounded diamond closes both:

$$
\mathcal E^{click}_B\le\epsilon_{click},
\qquad
\mathcal E^{GR}_B\le\epsilon_{GR}.
$$

Opening followed: maybe the two closures select different diamonds.

Result: then the correct object is the least common closure diamond:

$$
B^{joint}
=
\operatorname{lcc}(B^{click},B^{GR}),
$$

where `lcc` means the least admissible diamond expansion that contains both
closure requirements.  If the least common closure is much larger than either
individual closure, the experiment is click-stable but not locally
spacetime-stable at the smaller boundary.

### Attack 10: "The boundary depends on arbitrary tolerances."

Sustained, but not fatal.

All experimental closure is tolerance-relative.  The physical requirement is
not a tolerance-free boundary.  It is monotone convergence:

$$
\epsilon_1<\epsilon_2
\quad\Longrightarrow\quad
B_{\epsilon_1}
\succeq
B_{\epsilon_2}
$$

up to admissible equivalence.  Tighter tolerance may require a larger boundary
or richer panel.

Opening followed: can this become vacuous?

Result: yes, unless the theory proves scaling laws for boundary growth:

$$
C_B(k_\epsilon,O_\epsilon)
\le
F(\epsilon,\text{environment class}).
$$

Flat labs, massive-object labs, horizon-like labs, and entangled labs should
have different scaling classes.

### Attack 11: "Massive exterior objects are smuggled in through spacetime."

Rejected.

The exterior is not represented by a background metric.  It is represented by
record-boundary data:

$$
\partial B,\quad
\operatorname{Collar}(B),\quad
\mathcal C_B,\quad
\mathcal R_B.
$$

If a massive object matters, it changes interval profiles, center residues,
transport drift, and Ward/source defects.  The difference between flat lab and
near-mass lab is a difference in closure cost, not an assumed geometry.

### Attack 12: "Joint closure ignores entanglement."

Rejected.

The boundary is not a spatial surface. It is a record-diamond boundary.  Any
non-spatial entangled sector that changes the projected click law must either
enter `B` or enter the licensed residue ledger `\mathcal R_B`.  If neither is
possible with small error, the bounded experiment is not closed.

## 20. Hostile Review Round 1

### Review 1: "`h_B` is still magic."

Sustained.

This paper proves what `h_B` does once given.  It does not derive `h_B`.

Opening investigated: derive `h_B` from:

$$
h_B(H)=\exp[-\mathcal A_B^{hist}(H)].
$$

Outcome: this reduces the problem to deriving `\Psi_B`, the primitive
boundary-work potential.  That is exactly the Paper XXXIII-XXXV missing object.

### Review 2: "The admissible panel class can smuggle in the answer."

Sustained.

Opening investigated: define admissibility by diamond operators and drift
control.  Section 17 gives the strongest current analytic rule.  It excludes
hidden labels and raw lookup unless raw detail is physically forced.

Remaining axiom: prove that the actual diamond-center operators generate a
finite or compact-enough admissible class.

### Review 3: "`I_GR` is not constructed."

Sustained.

Opening investigated: replace raw interval/count packet with `G_B^{coarse}`.
Section 18 states the construction target, but not its proof.

Remaining axiom: finite GR-packet construction from center shells, boundary
intervals, transport drift, Ward residue, and refinement stability.

### Review 4: "This is still probabilistic."

Rejected.

The primitive object is `h_B`, a positive weight on histories.  Probability is
the normalized projection of `h_B` onto partial observations.  This is exactly
the intended epistemic/effective role.

### Review 5: "A bounded diamond ignores the universe."

Rejected.

The outside universe is represented by boundary and residue terms.  If those
terms do not decay, the bounded prediction does not close.  The formalism says
when the bounded laboratory approximation is invalid.

## 21. Hostile Review Round 2

### Review 6: "The coarsest sufficient panel theorem assumes exact sufficiency."

Sustained for exact zero-residual claims.

Opening investigated: use approximate sufficiency.

For tolerance `\epsilon`, define:

$$
\mathfrak A_B^\epsilon
=
\left\{
(k,O):
\sum_{j=k}^{\infty}\Delta^{click}_{B,j}
+
A^{click}_{B,k}(O)
\le
\epsilon
\right\}.
$$

Then select:

$$
(k,O)_\epsilon
=
\operatorname*{argmin}_{(k,O)\in\mathfrak A_B^\epsilon}
C_B(k,O).
$$

This gives the approximate theorem:

> among all panels with prediction error below tolerance, choose the
> least-complex admissible one.

No exact zero is required.

### Review 7: "The same panel may not optimize clicks and GR."

Sustained.

The correct statement is not equality of click and GR panels.  It is existence
of a common bounded history object with two projections:

$$
O_B^{click}
\preceq
O_B^*
\quad\text{and}\quad
O_B^{GR}
\preceq
O_B^*.
$$

The shared object is the bounded history weight `h_B`, not necessarily a single
visible scalar panel.

### Review 8: "History weights over `\Gamma_B` may be infinite."

Sustained as a convergence condition.

Opening investigated: require local normalizability:

$$
0
<
\sum_{H:O_B(H)=o}h_B(H)
<
\infty.
$$

If this fails, the bounded prediction is undefined.  This becomes a required
normalization axiom for infinite/effective limits.

### Review 9: "The theorem could be vacuous if no panel satisfies the bounds."

Sustained.

If no admissible panel has small tail and partial-panel residual, then the
bounded experiment has no stable prediction at that tolerance.  This is an
allowed negative result, not a contradiction.

## 22. Hostile Review Round 3: Joint Boundary Review

### Review 10: "The joint boundary is just another arbitrary minimization."

Partly sustained.

The joint boundary is meaningful only if the admissible expansions of `B` are
record-intrinsic and if the closure errors are derived from `h_B` and `I_GR`.
If those are hand-made, the boundary is arbitrary.

Opening investigated: define boundary by tolerated residuals rather than
background geometry.  Sections 3-5 do this.  The remaining work is to derive
the scaling laws of those residuals.

### Review 11: "A black hole example assumes a black hole."

Rejected as interpretation, sustained as proof.

The paper does not prove black-hole physics.  It says what the record-intrinsic
signature of a horizon-like closure failure would be:

$$
\mathcal E^{click}_B\le\epsilon_{click}
\quad\text{while}\quad
\mathcal E^{GR}_B>\epsilon_{GR}
$$

for small collars, plus asymmetric deletion/insertion transport.  Showing that
this converges to the GR black-hole regime remains part of Axiom C.

### Review 12: "Flat-space locality is recovered only after onset."

Sustained and accepted.

The paper intentionally does not use metric balls before spacetime onset.
Metric locality is a derived special case of joint closure after `I_GR` is
stable.

### Review 13: "Do click closure and GR closure really use one boundary?"

Not proven generally.

The campaign defines the stronger spacetime-like condition:

$$
B^{ST}_\epsilon
\text{ closes both.}
$$

It does not prove every click-closed region has such a refinement.  If no such
joint closure exists at finite cost, the region is pre-spacetime, nonlocal, or
not experimentally closed.

## 23. Hostile Review Round 4: Pass/Fail Verdict

The campaign now passes as an analytic reduction, not as the final physical
click law.

### Review 14: "Did the campaign prove the click law?"

No.

It proved the projection/selection theorem that any candidate law must satisfy.
The actual physical law still requires `\psi_B`, `\mathfrak A_B`, and `I_GR`.

### Review 15: "Did the campaign avoid brute force?"

Yes.

The main results are tail inequalities, projection formulas, panel-selection
theorems, and counterexamples.  No larger enumeration is used as evidence for
the theorem.

### Review 16: "Did the campaign stop on a narrowing?"

No.

Every narrowing was followed until it became either:

- a formal theorem;
- a counterexample to a shortcut;
- or an irreducible construction axiom.

The surviving irreducible axioms are named explicitly in Section 24.

### Review 17: "Is the onset theorem physical or definitional?"

The theorem is formal.  Its physical content depends entirely on deriving
`I_GR`, `d_GR`, `\mathcal M`, and `\Delta^{GR}` from record diamonds.  This is
not hidden; it is the named remaining task.

### Verdict

$$
\boxed{
\text{PASS as analytic campaign;}
\qquad
\text{NOT PASS as final physical derivation.}
}
$$

The paper reaches the allowed stopping condition:

$$
\boxed{
\text{the target decomposes into independent irreducible axioms, explicitly
named.}
}
$$

## 24. Final Campaign Outcome

The user requirement for this campaign was:

> do not stop on a sharpening; continue until the idea is proven, falsified, or
> decomposed into independent irreducible axioms.

The campaign reaches the third outcome.

The following analytic results are proven:

1. projected probabilities arise from normalized positive history weights;
2. no one-step Markov recurrence is sufficient in general;
3. history truncation error is bounded by a sum of history increments;
4. partial-observation error adds as a separate residual;
5. pre-spacetime click selection is well-defined without `I_GR`;
6. spacetime onset is the stability of a second projection of the same history
   weight;
7. in the exact finite case, least complexity selects a least-complex
   sufficient admissible panel, and selects the coarsest one when it uniquely
   exists;
8. a spacetime-like region should be a joint closure diamond: the same bounded
   boundary closes both click prediction and GR readout at the requested
   tolerances.

The final law is not yet proven because four independent construction
problems remain:

### Axiom A: Boundary-Work Potential

Derive:

$$
\psi_B
$$

from the no-silent diamond center, and prove:

$$
h_B(H)
=
\exp[-\mathcal A_B^{hist}(H)]
$$

or the correct positive replacement.

### Axiom B: Admissible Non-Reconstructive Panel Class

Derive:

$$
\mathfrak A_B
$$

from bounded diamond operators, no-hidden-presentation, deletion/insertion
stability, and boundary locality.

### Axiom C: Intrinsic Finite GR Packet

Derive:

$$
I_{GR},\quad d_{GR},\quad \mathcal M,\quad \Delta^{GR}
$$

from record diamonds, centers, transport, Ward/Bianchi residue, and refinement
stability.

### Axiom D: Joint Boundary Scaling

Derive the closure-growth law:

$$
C_B(k_\epsilon,O_\epsilon)
\le
F(\epsilon,\mathcal K)
$$

for each environment class `\mathcal K`: flat-lab, massive-object,
horizon-like, entangled, and pre-spacetime regimes.

This is the theorem that makes tolerance-relative boundaries predictive rather
than arbitrary.

These are independent in the following sense:

- Axiom A can hold without a spacetime packet.
- Axiom C can be proposed without a derived `h_B`.
- Axiom B is needed to stop both A and C from becoming raw lookup.
- Axiom D is needed to make the phrase "smallest boundary" scale across
  physical environments instead of depending on a one-off tolerance choice.

Therefore no amount of larger brute-force enumeration can close the law unless
it supplies one of these four constructions.

## 25. Updated Long Campaign Target

Paper XXXVIII changes the target from a finite audit to an analytic theorem:

$$
\boxed{
\text{derive }(\psi_B,\mathfrak A_B,I_{GR},F_{\rm closure})
\text{ from no-silent diamond histories.}
}
$$

Once those are derived, the click law is:

$$
\boxed{
(k_B^{pre},O_B^{pre})
=
\operatorname*{argmin}_{k,O\in\mathfrak A_B}
\left[
\sum_{j=k}^{\infty}\Delta^{click}_{B,j}
+
A^{click}_{B,k}(O)
+
\eta C_B(k,O)
\right],
}
$$

with:

$$
\boxed{
\Pr_B(S_B=c\mid O_B=o)
=
\frac{
\sum_{H:O_B(H)=o,\ S_B(H)=c} h_B(H)
}{
\sum_{H:O_B(H)=o} h_B(H)
}.
}
$$

And spacetime onset is:

$$
\boxed{
\exists(k,O)\in\mathfrak A_B:
\mathcal E^{GR}_B(k,O)\le\epsilon_{GR}.
}
$$

For spacetime-like experimental regions, the stronger joint closure law is:

$$
\boxed{
B^{ST}_{\epsilon}
=
\operatorname*{argmin}_{B,k,O} C_B(k,O)
\quad
\text{subject to}
\quad
\mathcal E^{click}_B\le\epsilon_{click},
\quad
\mathcal E^{GR}_B\le\epsilon_{GR}.
}
$$

In plain language:

> The next click may be deterministic in the full bounded history.  Probability
> appears because the experiment sees only a partial panel.  A spacetime-like
> region appears only when the same bounded boundary closes both the click
> projection and the manifoldlike GR projection.

That is the strongest analytic form of the current SHARD click-law frontier.
