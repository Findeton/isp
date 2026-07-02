# Relativistic ISP v7 Paper XLV: Reusable-Residue Description Length, Falsified Geometric Dominance, and Carrier Selection

**Status:** analytic campaign note, not peer reviewed, version 2026-06-30.

## 0. Question

Paper XLIV reduced forced spacetime onset to a precise hinge:

$$
\boxed{
\text{target-relative geometric dominance.}
}
$$

The question is:

$$
\boxed{
\text{when is geometry the shortest stable non-reconstructive explanation of
recurrent record residues?}
}
$$

If geometry wins, forced finite spacetime onset becomes derivable for a serious
class of large pre-geometric seeds.  If a non-geometric code wins, spacetime is
not forced for that target family.

This paper attacks that hinge directly.

## 1. Executive Result

The first part of the campaign proves a scoped dominance theorem conditional
on a sharing inequality.  The directive campaign later falsifies that sharing
inequality for the current physical admissibility gates.  The final result of
the paper is therefore not "geometry always wins."

The final result is:

$$
\boxed{
\text{physical admissibility}
\Rightarrow
\text{minimal bounded-history carrier selection},
}
$$

and:

$$
\boxed{
\text{spacetime}
=
\text{the geometry-irreducible phase of that selector.}
}
$$

Geometry is not universally dominant.  In this paper's conditional route, it
can dominate only when the target family requires all five residue functions:

$$
\boxed{
\text{interval}
+\text{overlap/transport}
+\text{cycle/curvature}
+\text{Ward/source}
+\text{history drift}.
}
$$

The conditional finite theorem from the first half of the campaign is:

$$
\boxed{
\begin{gathered}
\text{modular recurrent residue graph}\\
+\text{bounded overlap degree}\\
+\text{cycle consistency}\\
+\text{Ward/source coupling}\\
+\text{summable drift}\\
+\text{subraw nonlookup constraint}\\
+\text{sharing inequality or geometry-irreducible carrier phase}\\
\\
\Longrightarrow
\text{the geometric packet is code-risk minimal among target-preserving
admissible compressions.}
\end{gathered}
}
$$

The strongest honest negation is also proved:

$$
\boxed{
\text{if the target family omits geometric residue functions, non-geometric
codes can win.}
}
$$

Thus geometric dominance is not metaphysical inevitability.  It is a finite
minimum-description theorem for a sufficiently rich target family.

## 2. Recurrent Residue Graph

Let `S_0` be a large pre-geometric seed.  Its recurrent residue graph is:

$$
\boxed{
\mathcal RGraph(S_0,\mathcal Y)
=
(V_R,E_R,\ell_R,w_R).
}
$$

Here:

- `V_R` is the finite set of recurrent residue channels relevant to target
  family `\mathcal Y`;
- `E_R` is the hyperedge set recording joint recurrence, overlap, or shared
  carrier use;
- `\ell_R(v)` is the residue type label of vertex `v`;
- `w_R(v)` is the committed work weight of the residue.

The target family is:

$$
\boxed{
\mathcal Y
=
(Y^{click},Y^{I},Y^{O},Y^{F},Y^{W},Y^{\Delta}).
}
$$

where:

- `Y^{click}` are click predictions;
- `Y^I` are interval/interior profiles;
- `Y^O` are overlap/transport responses;
- `Y^F` are loop/curvature-like responses;
- `Y^W` are Ward/source residues;
- `Y^\Delta` are history-drift responses.

If `\mathcal Y` contains only `Y^{click}`, geometry need not dominate.

## 3. Codes And Code Risk

A compression code `K` assigns a finite dictionary and carrier map:

$$
\boxed{
K=(\mathcal D_K,\pi_K,\rho_K).
}
$$

where:

- `\mathcal D_K` is the dictionary of carriers;
- `\pi_K:V_R\to\mathcal D_K` assigns residues to carriers;
- `\rho_K` gives projective/deletion/refinement behavior.

The code risk is:

$$
\boxed{
\mathfrak R_K(\mathcal Y)
=
C_{\rm dict}(K)
+C_{\rm assign}(K)
+C_{\rm drift}(K)
+C_{\rm defect}(K)
+C_{\rm nonlookup}(K)
+\lambda\,\ell_K(\mathcal Y).
}
$$

The loss term is:

$$
\boxed{
\ell_K(\mathcal Y)
=
d_{\mathcal Y}
\left(
\widehat{\mathcal Y}_K,
\mathcal Y
\right).
}
$$

Only admissible codes are allowed:

$$
\boxed{
C_{\rm nonlookup}(K)<C_{\rm raw}(S_0),
\qquad
\sum_j C_{\rm drift,j}(K)<\infty.
}
$$

## 4. The Geometric Code

The geometric code is:

$$
\boxed{
K_{GR}
=
(\mathsf A,\mathsf Q,\mathsf U,\mathsf F,\mathsf W,\mathsf\Theta,\mathsf r).
}
$$

with:

- `\mathsf A`: atlas/diamond cover;
- `\mathsf Q`: interval, shell, volume, and center summaries;
- `\mathsf U`: overlap transport;
- `\mathsf F`: loop/curvature defects;
- `\mathsf W`: Ward/Bianchi residues;
- `\mathsf\Theta`: typed source dictionary;
- `\mathsf r`: refinement maps.

The geometric code risk is:

$$
\boxed{
\mathfrak R_{GR}
=
C_{\mathsf A}+C_{\mathsf Q}+C_{\mathsf U}+C_{\mathsf F}
+C_{\mathsf W}+C_{\mathsf\Theta}+C_{\mathsf r}
+C_{\rm drift}+C_{\rm defect}.
}
$$

## 5. Non-Geometric Competitors

The adversarial competitors are:

1. `K_{\rm lookup}`: raw lookup;
2. `K_{\rm stage}`: staged or layer code;
3. `K_{\rm exp}`: expander-like symbolic code;
4. `K_{\rm rand}`: random dense compressor;
5. `K_{\rm ent}`: entanglement-only hyperedge code;
6. `K_{\rm sym}`: high-symmetry quotient code;
7. `K_{\rm blackbox}`: arbitrary learned predictor;
8. `K_{\rm click}`: target-click-only code.

A fair competitor must preserve `\mathcal Y` below tolerance and remain
subraw/projective.

## 6. Dominance Margin

Define the target-relative dominance margin:

$$
\boxed{
\Delta_{\rm dom}(\mathcal Y)
=
\inf_{K\not\simeq K_{GR}}
\mathfrak R_K(\mathcal Y)
-
\mathfrak R_{GR}(\mathcal Y).
}
$$

Geometry dominates when:

$$
\boxed{
\Delta_{\rm dom}(\mathcal Y)>\epsilon_K.
}
$$

It ties when:

$$
\boxed{
|\Delta_{\rm dom}(\mathcal Y)|\le\epsilon_K.
}
$$

It loses when:

$$
\boxed{
\Delta_{\rm dom}(\mathcal Y)<-\epsilon_K.
}
$$

## 7. Structural Assumptions

The dominance theorem needs finite structural hypotheses.

### 7.1 Modular Atlas Decomposition

The recurrent residue graph has a cover:

$$
\boxed{
\mathcal U=\{U_a\}_{a\in A}
}
$$

with bounded local overlap:

$$
\boxed{
\deg_{\mathcal U}(v)\le D.
}
$$

### 7.2 Local Reuse

Each geometric carrier is reused at least:

$$
\boxed{
m_a\ge m_{\min}
}
$$

times across the target family.

### 7.3 Cycle Consistency

Transport around overlap cycles has stable finite residue:

$$
\boxed{
\sum_{\gamma\in\Gamma_{\rm cyc}}
\|F_\gamma-\widehat F_\gamma\|<\epsilon_F.
}
$$

### 7.4 Ward/Source Coupling

Source residues are coupled to interval/transport residues:

$$
\boxed{
I\leftrightarrow W,\qquad U\leftrightarrow W.
}
$$

### 7.5 Drift Summability

The code must be stable under history depth:

$$
\boxed{
\sum_{j\ge k}
d_K(K_{j+1},\rho_{j+1\to j}^{*}K_j)<\infty.
}
$$

## 8. Theorem 1: Raw Lookup Is Disqualified

`K_lookup` cannot beat geometry inside the admissible bounded law.

**Proof.**

Raw lookup has:

$$
\boxed{
C_{\rm nonlookup}(K_{\rm lookup})\ge C_{\rm raw}(S_0).
}
$$

Admissibility requires strict subrawness.  Therefore raw lookup is outside the
competitor class. `\square`

## 9. Theorem 2: Click-Only Codes Win Only For Click-Only Targets

If the target family contains only click predictions and those clicks are
determined by non-geometric typed residues, then a click-only code can beat
geometry.

**Proof.**

For `\mathcal Y=(Y^{click})`, the loss term does not charge interval,
overlap, cycle, Ward, or GR drift failure.  A smaller typed click dictionary
can preserve the target at lower code risk than the geometric packet. `\square`

### 9.1 Consequence

Spacetime is not forced by successful click prediction alone.  The target
family must include spacetime-relevant residues.

## 10. Theorem 3: Staged Codes Fail Rich Targets

If `\mathcal Y` includes overlap transport, cycle consistency, and
history-drift responses, then a staged/layer code that matches only interval
or dimension profiles has above-tolerance loss.

**Proof.**

Layer statistics do not determine overlap transport maps, loop residues, or
projective deletion/refinement drift.  Therefore there exist two histories
with the same staged profile and different `Y^O`, `Y^F`, or `Y^\Delta`.
Any code that identifies them has target loss above tolerance. `\square`

## 11. Theorem 4: Expander Codes Lose Local Overlap Targets

An expander-like non-geometric code can compress global adjacency, but if the
target family requires bounded local overlap and transport locality, it must
pay either high assignment cost or high defect cost.

**Proof.**

Expander codes spread dependencies globally.  Local overlap targets require
residue changes to be carried by bounded neighborhoods and stable refinement
maps.  Encoding those local neighborhoods inside an expander code requires
extra assignment data comparable to an atlas, or else the local-overlap loss is
above tolerance. `\square`

## 12. Theorem 5: Entanglement-Only Codes Do Not Preserve Geometry Targets

An entanglement-only hyperedge code can preserve shared click correlations,
but it cannot preserve interval, overlap, cycle, and Ward/source targets
unless it reconstructs equivalent geometric carriers.

**Proof.**

Shared hyperedges encode correlation carriers.  The rich target family also
requires interval interiors, local overlap transport, loop defects, and source
coupling.  If the hyperedge code does not encode these, target loss is high.
If it does encode them, it has reconstructed an equivalent geometric carrier
dictionary and is no longer a strict non-geometric competitor. `\square`

## 13. Theorem 6: Black-Box Predictors Fail Projective Nonlookup

A black-box predictor can beat geometric code risk only if its internal state
is subraw, projectively stable, and interpretable as finite carriers for the
target residues.

**Proof.**

If the black box is raw, it is inadmissible.  If it is unstable across
deletion/refinement, it fails projectivity.  If it is stable and subraw while
preserving the rich target family, its internal state defines a finite carrier
dictionary.  The carrier dictionary is then subject to the same comparison as
any other code. `\square`

## 14. Lower Bound Lemma

A non-geometric code preserving the rich target family must encode five
independent reusable structures:

$$
\boxed{
I,\quad O,\quad F,\quad W,\quad \Delta.
}
$$

Define their independent work masses:

$$
\boxed{
M_I,\ M_O,\ M_F,\ M_W,\ M_\Delta.
}
$$

If the structures are independent modulo same-actual quotient, then any
target-preserving code has lower bound:

$$
\boxed{
\mathfrak R_K(\mathcal Y)
\ge
c_I M_I+c_O M_O+c_F M_F+c_W M_W+c_\Delta M_\Delta
-C_{\rm share}(K).
}
$$

Here `C_share(K)` is the legitimate saving from shared carriers.

## 15. Theorem 7: Shared-Carrying Geometry Wins Under Modular Reuse

Assume:

1. the rich target family includes `I,O,F,W,\Delta`;
2. the recurrent residue graph has a bounded-overlap modular atlas cover;
3. geometric carriers share the five structures with reuse factor at least
   `m_min`;
4. every non-geometric code has sharing saving no larger than the geometric
   overlap saving plus tolerance:

$$
\boxed{
C_{\rm share}(K)
\le
C_{\rm share}(K_{GR})+\epsilon_{\rm share};
}
$$

5. the geometric dictionary is subraw and projectively stable.

Then:

$$
\boxed{
\Delta_{\rm dom}(\mathcal Y)>-\epsilon_{\rm share}.
}
$$

If the sharing inequality is strict by margin `\eta`, then:

$$
\boxed{
\Delta_{\rm dom}(\mathcal Y)>\eta-\epsilon_{\rm share}.
}
$$

**Proof.**

Any target-preserving code must represent all five independent structures.
The geometric code represents them with shared atlas/overlap carriers.  By the
sharing assumption, no non-geometric code can save more description length
than the geometric carriers except within tolerance.  Therefore the geometric
code is risk-minimal up to tolerance, and strictly dominant under a strict
sharing gap. `\square`

## 16. Opening: Prove The Sharing Inequality

The real opening is now:

$$
\boxed{
C_{\rm share}(K)
\le
C_{\rm share}(K_{GR})+\epsilon_{\rm share}.
}
$$

This says geometric carriers are at least as good as any other admissible
carrier at sharing interval, overlap, loop, Ward, and drift information.

This is the finite mathematical core of geometric dominance.

## 17. Follow-Up A: When Sharing Inequality Fails

The sharing inequality can fail.

### 17.1 Symbolic Compression Failure

If residues are generated by a short non-geometric symbolic rule, then:

$$
\boxed{
C_{\rm share}(K_{\rm sym})<C_{\rm share}(K_{GR}).
}
$$

Spacetime is not forced.

### 17.2 Global Expander Failure

If the target family ignores local overlap but preserves global adjacency,
expander-like code can win.

### 17.3 Entanglement-Dominant Failure

If hyperedges explain the selected targets without interval/transport residue,
entanglement code can win.

### Theorem 8: Sharing Failure Blocks Forced Geometry

If an admissible non-geometric code has strictly better sharing for the
selected target family, then geometric dominance fails and spacetime onset is
not forced by that target family.

**Proof.**

The non-geometric code has lower code risk while preserving targets.  By
least-work selection, at least one minimizer is non-geometric. `\square`

## 18. Follow-Up B: Enriching The Target Family

If non-geometric code wins because the target is too weak, enrich the target
family.

Define target closure:

$$
\boxed{
\overline{\mathcal Y}
=
\operatorname{NoSilentClosure}(\mathcal Y).
}
$$

It adds every above-tolerance residue that changes the target under bounded
history projection.

### Theorem 9: No-Silent Target Closure Restores Fair Competition

If a non-geometric code wins only by ignoring an above-tolerance residue that
changes the target under bounded history projection, then no-silent target
closure adds that residue and invalidates the win.

**Proof.**

By definition, no-silent closure appends all above-tolerance target-changing
residues.  A code that ignored the residue no longer preserves
`\overline{\mathcal Y}`. `\square`

### 18.1 Limit

If the non-geometric code still wins after no-silent target closure, the
failure is real.  Geometry is not forced for that bounded problem.

## 19. Follow-Up C: Entropy Principle

Maybe geometric dominance follows from entropy: geometry is the maximum-reuse,
minimum-surprise code for local residues.

Define residual surprise under code `K`:

$$
\boxed{
S_K
=
-\sum_{v\in V_R}w_R(v)\log p_K(v\mid \pi_K(v)).
}
$$

The entropy-regularized risk is:

$$
\boxed{
\mathfrak R_K^{ent}
=
\mathfrak R_K+\theta S_K.
}
$$

### Theorem 10: Entropy Helps Geometry Only With Locality

Entropy regularization favors geometry only when the residue distribution is
locally reusable in atlas/overlap neighborhoods.  If the residue distribution
is non-geometric but simple, entropy can favor a non-geometric code.

**Proof.**

Entropy rewards predictive carrier assignments.  If local geometric carriers
predict residues well, entropy lowers geometric risk.  If a symbolic or
non-geometric carrier predicts them better, entropy lowers that code instead.
`\square`

## 20. Follow-Up D: Symmetry Principle

Maybe geometry wins because it is the most symmetric compression compatible
with the target family.

Let:

$$
\boxed{
\operatorname{Aut}_{\mathcal Y}(K)
}
$$

be target-preserving automorphisms of code `K`.  Add:

$$
\boxed{
C_{\rm sym}(K)
=
-\sigma\log|\operatorname{Aut}_{\mathcal Y}(K)|.
}
$$

### Theorem 11: Symmetry Alone Does Not Force Geometry

Symmetry can select non-geometric highly symmetric codes unless the target
family includes local overlap, transport, cycle, and Ward/source residues.

**Proof.**

Large automorphism groups occur in antichains, chains, staged orders, and
expander-like structures.  Without rich geometric targets, symmetry does not
distinguish them from geometry.  With rich targets, non-geometric symmetries
that collapse transport or Ward/source data incur target loss. `\square`

## 21. Full Dominance Theorem

#### Theorem 12: Target-Relative Geometric Dominance

Let `S_0` be a large pre-geometric seed.  Let `\overline{\mathcal Y}` be the
no-silent target closure of the selected click/source/GR target family.  Assume:

1. `\overline{\mathcal Y}` includes interval, overlap/transport, cycle,
   Ward/source, and history-drift residues;
2. the recurrent residue graph has bounded-overlap modular atlas
   decomposition;
3. geometric carriers are subraw and projectively stable;
4. non-geometric competitors are required to be subraw, projective, and
   target-preserving;
5. the sharing inequality holds, or holds strictly by margin `\eta`.

Then:

$$
\boxed{
\Delta_{\rm dom}(\overline{\mathcal Y})\ge-\epsilon_{\rm share}.
}
$$

If the sharing inequality is strict by `\eta>\epsilon_{\rm share}`, then:

$$
\boxed{
\Delta_{\rm dom}(\overline{\mathcal Y})>0.
}
$$

Thus geometry is forced by least-work selection for that target family.

**Proof.**

No-silent closure prevents competitors from ignoring target-changing residues.
The rich target family requires all five reusable structures.  The lower-bound
lemma applies to every admissible competitor.  The geometric code carries the
same structures through shared atlas/overlap carriers.  The sharing inequality
gives risk minimality, strict if the margin is strict. `\square`

## 22. Hostile Review Round I

### Review 1: "The sharing inequality is still an assumption."

Accepted.  The paper has reduced dominance to one exact inequality.  That is a
substantial narrowing but not total closure.

### Review 2: "The theorem is target-relative."

Accepted.  It must be.  Geometry cannot be forced for a target family that
does not ask geometric questions.

### Review 3: "A symbolic law could beat geometry."

Accepted.  If it is subraw, projective, and target-preserving after no-silent
closure, then geometry is not forced.  That would be a genuine counterexample.

### Review 4: "The target closure could grow raw."

Accepted.  If no-silent target closure becomes raw, the bounded problem is not
closed at that tolerance.  The boundary must expand or the target must be
weakened.

### Review 5: "Entropy and symmetry do not solve it."

Accepted.  They help only when local geometric reuse is already present.

## 23. Opening Follow-Up: Can The Sharing Inequality Be Audited?

The inequality is auditable if every code is represented by a finite carrier
hypergraph:

$$
\boxed{
\mathcal C_K=(D_K,E_K)
}
$$

and sharing is:

$$
\boxed{
C_{\rm share}(K)
=
\sum_{e\in E_K}(\operatorname{reuse}(e)-1)c(e).
}
$$

The geometric carrier hypergraph has edges from atlas overlaps, loops, and
source couplings.

### Theorem 13: Finite Sharing Audit

At finite tolerance, target-relative geometric dominance can be audited by
comparing carrier hypergraph sharing scores over the finite admissible
dictionary class.

**Proof.**

The admissible dictionary class is finite after subraw quotienting and target
closure.  Each dictionary has finite carrier edges and reuse counts.  Therefore
the sharing scores and code risks are finite and comparable. `\square`

### 23.1 Meaning

This gives an actual finite test:

$$
\boxed{
\text{build finite carrier competitors and compute code risk.}
}
$$

It is not brute-force over all histories.  It is finite model selection over
subraw residue dictionaries.

## 24. Opening Follow-Up: Does This Close Forced Onset?

Combine Paper XLIV with Theorem 12.

#### Theorem 14: Dominance Closes Forced Onset For Rich Seeds

If a large pre-geometric seed satisfies Paper XLIV's structural rank,
recurrence, subraw carrier, finite-floor, no-silent pressure, and least-work
conditions, and if Theorem 12 gives strict geometric dominance for its
no-silent target closure, then finite spacetime onset is forced.

**Proof.**

Paper XLIV's forced-onset theorem requires target-relative geometric
dominance.  Theorem 12 supplies it.  All other hypotheses are the Paper XLIV
seed conditions. `\square`

## 25. Final Hostile Review Round II

### Review 6: "This is still conditional on rich seeds."

Yes.  Richness is necessary.  Small or click-only seeds do not force
spacetime.

### Review 7: "A real counterexample may exist."

Yes.  A subraw, projective, target-closed symbolic compressor with lower risk
would falsify forced geometric onset for that target family.

### Review 8: "This suggests a computational program."

Correct.  The next empirical/mathematical step is to enumerate finite carrier
dictionaries for small but rich residue graphs and test the code-risk
inequality.

### Review 9: "This still does not prove continuum GR."

Correct.  It proves finite geometric dominance, which is upstream of finite
spacetime onset.  Continuum representation and Einstein limits remain later.

## 26. Interim Campaign State Before The Directive Counterexample

Before Section 27, the paper had reduced the question to the clean theorem:

$$
\boxed{
\text{prove or falsify the sharing inequality for physically admissible
recurrent residue graphs.}
}
$$

At that point, if true, then:

$$
\boxed{
\text{large pre-geometric rich seeds}
\Longrightarrow
\text{target-relative geometric dominance}
\Longrightarrow
\text{forced finite spacetime onset}.
}
$$

If false, then the counterexample tells us what replaces geometry:

$$
\boxed{
\text{the winning non-geometric subraw projective compressor.}
}
$$

Section 27 resolves this fork by giving the counterexample.  Therefore this
section is preserved only as the pre-resolution state of the campaign.

## 27. Directive Campaign: Prove Or Falsify The Sharing Inequality

The directive is to decide the universal claim:

$$
\boxed{
C_{\rm share}(K)
\le
C_{\rm share}(K_{GR})+\epsilon_{\rm share}
}
$$

for physically admissible recurrent residue graphs, using the admissibility
conditions already developed in Papers XL--XLIV:

1. finite bounded record-history cylinder;
2. record-intrinsic channels;
3. no-silent residue accounting;
4. same-actual quotienting;
5. subraw/nonlookup description;
6. projective deletion/refinement compatibility;
7. finite channel floors;
8. bounded-history, non-Markovian recurrence.

No additional locality, manifoldlikeness, or "already geometric" premise is
allowed in this decision.

### 27.1 The Counterexample Family

Fix a finitely presented residually finite group `\Gamma` with a fixed finite
generating set `S` and fixed finite relator set `\mathcal R_\Gamma`.  For
definiteness take a congruence tower:

$$
\boxed{
G_m=\mathrm{SL}(3,\mathbb Z/p^m\mathbb Z),
\qquad
\pi_{m+1,m}:G_{m+1}\to G_m.
}
$$

Only the following properties are used:

$$
\boxed{
|S|<\infty,\qquad
|\mathcal R_\Gamma|<\infty,\qquad
\pi_{m+1,m}(gs)=\pi_{m+1,m}(g)s.
}
$$

For each `m`, build a bounded record diamond `B_m` with records:

$$
\boxed{
R_m
=
X_m^-
\sqcup
E_m
\sqcup
P_m
\sqcup
X_m^+.
}
$$

Here:

- `X_m^-=\{x_g^-:g\in G_m\}` are lower boundary records;
- `X_m^+=\{x_g^+:g\in G_m\}` are upper boundary records;
- `E_m=\{e_{g,s}:g\in G_m,s\in S\}` are typed generator-edge records;
- `P_m=\{p_{g,r}:g\in G_m,r\in\mathcal R_\Gamma\}` are typed relator or
  plaquette records.

The order relation is the height-three relation generated by:

$$
\boxed{
x_g^-\prec e_{g,s}\prec x_{gs}^+,
}
$$

and by the analogous incidence relations attaching each relator record
`p_{g,r}` to the finite loop of generator-edge records determined by `r`.

This is a record diamond construction.  It is not a continuum manifold and
does not assume a coordinate metric.

### 27.2 Its Rich Target Channels

The recurrent residue target family is:

$$
\boxed{
\mathcal Y_m=(Y^I_m,Y^O_m,Y^F_m,Y^W_m,Y^\Delta_m).
}
$$

The channels are:

1. `Y^I_m`: interval/incidence profiles of generator intervals
   `[x_g^-,x_{gs}^+]`;
2. `Y^O_m`: overlap/transport responses given by generator composition
   `g\mapsto gs`;
3. `Y^F_m`: loop/curvature-like residues given by relator closure
   `gr=g`;
4. `Y^W_m`: Ward/source balance residues saying each record has the fixed
   finite incoming/outgoing generator and relator incidence prescribed by
   `(S,\mathcal R_\Gamma)`;
5. `Y^\Delta_m`: history-drift residues given by the projective maps
   `\pi_{m+1,m}`.

All five target functions from Section 1 are present.  Their channel floors
are positive because every generator and relator channel is printed with
positive finite incidence mass.

### 27.3 Physical Admissibility Check

This family satisfies the current physical admissibility gates.

**Finite.**  For each `m`, `R_m` is finite.

**Record-intrinsic.**  The channels are incidence, interval, overlap,
relator-loop, and deletion/refinement responses of the record diamond.  No
external continuum geometry is used.

**No-silent.**  Every above-tolerance target-changing residue is printed by
one of the generator, relator, balance, or projection channels.

**Same-actual quotient.**  Automorphisms of the Cayley-residue presentation are
quotiented.  They are presentation symmetries, not hidden physical residue.

**Subraw.**  Raw lookup of all incidences costs at least:

$$
\boxed{
C_{\rm raw}(B_m)\ge c\,|G_m|\,|S|
}
$$

and, if all pair incidences are treated as hidden presentation data, at least
quadratic in `|G_m|`.  The algebraic carrier below costs only:

$$
\boxed{
O(\log |G_m|)+O(1).
}
$$

**Projective.**  The quotient maps `\pi_{m+1,m}` preserve generator edges and
relator loops, so deletion/refinement drift is exactly controlled:

$$
\boxed{
\Delta_m=0
}
$$

for the printed target channels, up to the chosen same-actual quotient.

**Bounded-history recurrence.**  The tower

$$
\boxed{
B_1\leftarrow B_2\leftarrow\cdots\leftarrow B_m
}
$$

is a non-Markovian bounded-history cylinder: the target residues at depth `m`
are not determined by a one-step state alone but by the compatible projective
history of quotient maps.

Therefore this is a physically admissible recurrent residue graph under the
conditions already on the table.

### 27.4 The Winning Non-Geometric Code

Define the algebraic code:

$$
\boxed{
K_{\rm alg}
=
(\Gamma,S,\mathcal R_\Gamma,p,m,\pi_{m+1,m}).
}
$$

It stores:

1. the fixed finite presentation of `\Gamma`;
2. the finite generator labels `S`;
3. the finite relator labels `\mathcal R_\Gamma`;
4. the modulus parameter `p^m`;
5. the projective quotient rule.

From these data it reconstructs every target residue in
`\mathcal Y_m`:

$$
\boxed{
\widehat{\mathcal Y}_{K_{\rm alg}}=\mathcal Y_m.
}
$$

The code is not raw lookup.  It does not list all records or all incidences.
It prints them by a finite algebraic rule.

Its carrier sharing is maximal in the following precise sense.  One carrier
rule:

$$
\boxed{
(g,s)\mapsto gs
}
$$

is reused by all generator intervals, overlap transports, relator loops,
balance residues, and projective drift tests.  Hence:

$$
\boxed{
C_{\rm share}(K_{\rm alg})
\ge
(|G_m||S|-1)c_{\rm mult}
+(|G_m||\mathcal R_\Gamma|-1)c_{\rm rel}
}
$$

up to fixed dictionary constants.

### 27.5 Why The Geometric Carrier Cannot Match It

The geometric packet carrier:

$$
\boxed{
K_{GR}=(\mathsf A,\mathsf Q,\mathsf U,\mathsf F,\mathsf W,\mathsf\Theta,\mathsf r)
}
$$

has only two options on this family.

**Option 1: treat the Cayley-residue structure as non-geometric.**  Then the
finite GR packet does not preserve the target family.  Its loss is
above-tolerance:

$$
\boxed{
\ell_{K_{GR}}(\mathcal Y_m)>\epsilon.
}
$$

It is not a competitor to `K_{\rm alg}`.

**Option 2: encode the Cayley-residue structure inside atlas/overlap
carriers.**  Then the geometric packet must reproduce the finite multiplication
and relator data.  But this is exactly the algebraic rule, or else it must pay
local assignment cost for the incidences:

$$
\boxed{
C_{\rm assign}(K_{GR})
\ge
c'|G_m||S|.
}
$$

In Option 2, either:

$$
\boxed{
K_{GR}\simeq K_{\rm alg}
}
$$

after carrier equivalence, in which case the algebraic code is not beaten by
a distinct geometric code, or:

$$
\boxed{
\mathfrak R_{K_{GR}}(\mathcal Y_m)
-
\mathfrak R_{K_{\rm alg}}(\mathcal Y_m)
\to+\infty
\quad(m\to\infty).
}
$$

Thus there is no strict geometric sharing advantage on this physically
admissible recurrent residue graph.

### 27.6 The Falsification

For large `m`:

$$
\boxed{
C_{\rm share}(K_{\rm alg})
>
C_{\rm share}(K_{GR})+\epsilon_{\rm share}
}
$$

unless `K_{GR}` is declared equivalent to the algebraic carrier itself.

Therefore the universal sharing inequality is false as stated:

$$
\boxed{
\forall K\quad
C_{\rm share}(K)
\le
C_{\rm share}(K_{GR})+\epsilon_{\rm share}
\quad
\text{is false.}
}
$$

This is not a conditional narrowing.  It is a counterexample inside the
existing admissibility gates.

## 28. Hostile Review Of The Falsification

### Review 1: "The Cayley family is not spacetime-like."

Correct, and that is exactly why it falsifies the universal sharing
inequality.  The directive was about physically admissible recurrent residue
graphs, not already-spacetime-like graphs.  Current admissibility permits
pre-geometric physical record histories.

### Review 2: "Maybe `K_{\rm alg}` is hidden raw lookup."

Rejected.  `K_{\rm alg}` stores a finite presentation and a modulus.  It does
not list `|G_m||S|` edge incidences or all target records.  Its description
length is subraw.

### Review 3: "Maybe no-silent closure would add geometry."

Rejected for this family.  No-silent closure adds the target-changing
residues.  The algebraic code already prints interval, overlap, loop,
Ward/balance, and projective-drift residues.  Adding geometry would be an
extra interpretation, not a no-silent necessity.

### Review 4: "Maybe the algebraic code is secretly geometric."

Only if "geometric" is broadened to mean any stable finite carrier algebra.
But then `K_{GR}` no longer means manifoldlike atlas/overlap geometry; it
means generic algebraic compression.  Under the paper's distinction between
geometric atlas carriers and non-geometric symbolic carriers, `K_{\rm alg}` is
a non-geometric admissible compressor.

### Review 5: "Maybe bounded degree or bounded overlap fails."

Generator degree is fixed by `|S|`.  Relator arity is fixed by the finite
presentation.  Projective drift is fixed by the quotient maps.  The family is
bounded-degree in the residue interfaces even as `|G_m|` grows.

### Review 6: "Maybe this only blocks universal dominance, not spacetime
onset for actually geometric seeds."

Correct.  But that is not a defect in the falsification.  It means the
universal sharing inequality is false, while a separate theorem may still hold
for a narrower class of already-geometric or geometry-irreducible physical
residue graphs.

The directive asked for proof or falsification of the universal physical
admissible claim.  The result is falsification.

## 29. Final Verdict

The sharing inequality is not a theorem of the current axioms.

The current axioms allow physically admissible recurrent residue graphs whose
shortest nonreconstructive explanation is algebraic rather than geometric.
Therefore:

$$
\boxed{
\text{the universal sharing inequality is false.}
}
$$

The exact failure mode is:

$$
\boxed{
\text{finite algebraic recurrence can share the printed target residues more
efficiently than manifoldlike atlas carriers.}
}
$$

Consequently, forced spacetime onset cannot be obtained from physical
admissibility alone.  Geometry is forced only after one proves or assumes that
the actual physical residue graph is not merely admissible but
geometry-irreducible: its interval, overlap, loop, Ward/source, and drift
residues cannot all be generated by a cheaper non-geometric algebraic carrier.

That statement is not a new narrowing of the result.  It is the conclusion of
the falsification: the old universal target is false.

## 30. Replacement Campaign: Carrier-Selection Click Law

The falsification does not kill the click-law program.  It kills the stronger
claim that geometry must always be the best carrier.

The replacement law is:

$$
\boxed{
\text{clicks are governed by minimal admissible bounded-history carriers.}
}
$$

Geometry is then not the universal carrier.  It is one phase of the carrier
selector.

### 30.1 Primitive Object: Bounded History Cylinder

For a bounded problem `B`, the primitive object is not a present state.  It is
a compatible bounded history cylinder:

$$
\boxed{
H_{B,k}
=
(W_{N-k},W_{N-k+1},\ldots,W_N;\partial B).
}
$$

Here:

- `W_j` is the record object at click depth `j`;
- `k` is the bounded history depth used by the problem;
- `\partial B` is the record boundary, including the instrument/source records
  needed at the requested tolerance.

The law is therefore non-Markovian in the Barandes sense:

$$
\boxed{
H_{B,k}\not\equiv W_N,
\qquad
\Pr(W_{N+1}\mid W_N)\text{ is not primitive.}
}
$$

### 30.2 Admissible Carrier

A carrier `K` for target family `\mathcal Y_B` is:

$$
\boxed{
K=(\mathcal D_K,\pi_K,\rho_K,\mathcal P_K).
}
$$

where:

- `\mathcal D_K` is a finite record-intrinsic dictionary;
- `\pi_K` assigns printed residues to dictionary carriers;
- `\rho_K` gives deletion/insertion/refinement behavior across the history;
- `\mathcal P_K` is the finite panel of readings produced by the carrier.

The admissibility gates are exactly the gates already used in Papers XL--XLIV:

1. **history first:** `K` acts on `H_{B,k}`, not merely on `W_N`;
2. **record intrinsic:** no continuum coordinates or hidden presentation labels;
3. **no-silent complete:** every above-tolerance target-changing residue is
   printed or explicitly charged;
4. **same-actual quotient:** presentation duplicates with zero residue are
   quotiented;
5. **subraw:** `K` is strictly cheaper than raw bounded-history lookup;
6. **projective:** deletion/refinement drift is controlled across depths;
7. **finite floors:** printed channels used in ratios have positive floors;
8. **deterministic sufficiency:** panel cells have below-tolerance target
   diameter.

Write the admissible class as:

$$
\boxed{
\operatorname{Adm}_B(\mathcal Y_B,\epsilon).
}
$$

If this class is empty, the bounded problem is not closed at that tolerance.

## 31. The Selector

For a history `H` and carrier `K`, define:

$$
\boxed{
\mathcal A^{sel}_B(H,K;\mathcal Y_B)
=
\mathcal A^{hist}_B(H;K)
+\mathfrak R_B(K;\mathcal Y_B).
}
$$

Here:

- `\mathcal A^{hist}_B(H;K)` is the no-silent bounded-history work from Paper
  XL, evaluated through carrier `K`;
- `\mathfrak R_B(K;\mathcal Y_B)` is the carrier risk from this paper:
  dictionary cost, assignment cost, drift cost, defect cost, nonlookup cost,
  and target loss.

The selected carrier set is:

$$
\boxed{
K_B^\star(H;\mathcal Y_B,\epsilon)
=
\operatorname*{Argmin}_{K\in\operatorname{Adm}_B(\mathcal Y_B,\epsilon)}
\mathcal A^{sel}_B(H,K;\mathcal Y_B).
}
$$

The carrier-reduced history action is:

$$
\boxed{
\mathcal A^{click}_B(H;\mathcal Y_B)
=
\inf_{K\in\operatorname{Adm}_B(\mathcal Y_B,\epsilon)}
\mathcal A^{sel}_B(H,K;\mathcal Y_B).
}
$$

and the bounded-history weight is:

$$
\boxed{
h_B(H;\mathcal Y_B)
=
\exp[-\mathcal A^{click}_B(H;\mathcal Y_B)].
}
$$

This is the replacement click law.

### 31.1 Effective Probability Is Projection

Let `O` be the observed finite panel and `Y` the target observable.  Then:

$$
\boxed{
\Pr_B(Y=y\mid O=o)
=
\frac{
\sum_{H:\ O(H)=o,\ Y(H)=y}
\exp[-\mathcal A^{click}_B(H;\mathcal Y_B)]
}{
\sum_{H:\ O(H)=o}
\exp[-\mathcal A^{click}_B(H;\mathcal Y_B)]
}.
}
$$

This is not a fundamental transition probability.  It is the calibrated
residual after projecting indivisible bounded histories onto the panel that is
actually computed.

### Theorem 15: Barandes-Aligned Carrier Selection

The selector above is aligned with indivisible-history dynamics: it does not
assign primitive probabilities to one-step transitions, and it treats
probability as a projection of weighted compatible histories.

**Proof.**

The primitive argument of the action is `H_{B,k}`, not `W_N`.  The carrier is
selected by minimizing no-silent work over the bounded history cylinder.
Probabilities appear only after conditioning on a finite observed panel and
summing over compatible full bounded histories.  Thus the law is history-first
and non-Markovian. `\square`

## 32. Carrier Phases

The selector can land in different phases.

### 32.1 Algebraic Phase

`K_B^\star` is algebraic when a finite symbolic or algebraic rule carries the
target residues at lower work than atlas-like geometry.

The Cayley-residue counterexample is in this phase.

### 32.2 Entanglement/Source Phase

`K_B^\star` is source-dominated when typed shared residues or long-range
hyperedges carry the target more cheaply than local overlap geometry.

This is admissible only if the source sector is printed inside the bounded
history panel and has controlled unresolved tail.

### 32.3 Staged/Layer Phase

`K_B^\star` is staged when layer or rank data carries the target.  This phase
is sufficient for some click targets but fails rich geometry targets when
overlap, loop, and drift residues are above tolerance.

### 32.4 Geometric Phase

`K_B^\star` is geometric when every selected minimizer is equivalent, up to
same-actual quotient, to a finite packet:

$$
\boxed{
K_{geo}
=
(\mathsf A,\mathsf Q,\mathsf U,\mathsf F,\mathsf W,\mathsf\Theta,\mathsf r)
}
$$

that passes the finite spacetime readout tests.

### Theorem 16: Carrier Phase Classification

For a finite bounded problem with nonempty admissible carrier class, every
least-work solution belongs to at least one carrier phase: algebraic,
entanglement/source, staged/layer, geometric, or a tie of these phases.

**Proof.**

At finite tolerance, admissible carriers are finite dictionaries modulo
same-actual equivalence.  The minimizer set is finite after subraw quotienting.
Classify each minimizer by the kind of dictionary that carries the target
residues with least work.  Ties are possible and are recorded as mixed phases.
`\square`

## 33. Geometry-Irreducibility Gate

The falsification shows that physical admissibility alone is too weak.  The
spacetime question is:

$$
\boxed{
\text{when is the selected carrier genuinely geometric rather than merely
algebraic?}
}
$$

Define `K` to be geometry-irreducible at tolerance `\epsilon_{GR}` when it
passes all of the following record-intrinsic tests.

### 33.1 Multiscale Interval Growth

There exists a dimension `d` such that interval volumes obey stable polynomial
scaling across the bounded history window:

$$
\boxed{
|I_r(x,y)|
\asymp
r^d
}
$$

within tolerance, after same-actual quotienting.

### 33.2 Local Atlas Overlap

Diamond neighborhoods admit overlaps whose transition defects are bounded:

$$
\boxed{
\sum_{\alpha\beta}
\|U_{\alpha\beta}U_{\beta\gamma}U_{\gamma\alpha}-1\|
\le
\epsilon_U.
}
$$

### 33.3 Finite Propagation Boundary

Unresolved response must decay from the printed boundary/source panel:

$$
\boxed{
\operatorname{tail}_K(R)
\le
C_K\theta_K^R,
\qquad
\theta_K<1.
}
$$

### 33.4 Approximate Isotropy

The local residue law cannot depend on a privileged generator presentation
after quotienting:

$$
\boxed{
\operatorname{anis}_K(B)
\le
\epsilon_{\rm iso}.
}
$$

### 33.5 Density Regularity

Interval counts cannot be explained by clustered density modulation alone:

$$
\boxed{
\operatorname{densdef}_K(B)
\le
\epsilon_{\rm dens}.
}
$$

### 33.6 Ward/Source Stability

Source and loop residues satisfy the finite Ward/Bianchi balance:

$$
\boxed{
\Delta^{Ward}_K+\Delta^{Bianchi}_K
\le
\epsilon_W.
}
$$

### 33.7 Robustness Under Target Closure

Adding no-silent nearby target residues must not switch the minimizer to a
non-geometric phase:

$$
\boxed{
K_B^\star(\operatorname{NoSilentClosure}(\mathcal Y_B))
\simeq
K_B^\star(\mathcal Y_B)
}
$$

up to same-actual geometric equivalence.

### Theorem 17: Geometry-Irreducibility Is A Phase Test, Not A Click-Law Axiom

The carrier-selection click law does not require geometry-irreducibility.
Geometry-irreducibility is exactly the additional condition for spacetime
onset.

**Proof.**

The selector is defined for every nonempty admissible carrier class.  It may
select algebraic, staged, source, or geometric carriers.  Spacetime readout is
licensed only when the selected carrier also satisfies the finite geometric
tests above.  Thus geometry-irreducibility is not needed to compute clicks; it
is needed to interpret the selected carrier as spacetime. `\square`

## 34. Re-Reading The Cayley Counterexample Under The New Law

The Cayley-residue family does not refute the click law.  It becomes an
example of a non-geometric carrier phase.

### 34.1 It Passes Click Carrier Selection

The selected carrier is:

$$
\boxed{
K_B^\star=K_{\rm alg}.
}
$$

The click law is well defined because the algebraic carrier is finite,
projective, no-silent, and subraw.

### 34.2 It Fails Generic Spacetime Onset

For expander-like finite quotients such as `SL(3,Z/p^mZ)`, the carrier fails
the geometric gate:

1. volume growth is not stable polynomial manifold growth at all scales;
2. local residue depends on chosen generator structure;
3. overlap cycles are relator constraints, not small curvature defects on a
   local atlas;
4. projective quotient maps are algebraic, not geometric refinements of a
   manifold patch;
5. approximate isotropy and density regularity are not forced.

Therefore:

$$
\boxed{
K_{\rm alg}\in\text{algebraic phase},
\qquad
K_{\rm alg}\notin\text{geometric phase}.
}
$$

### 34.3 Flat Torus Exception

If the algebraic code is a finite torus-like group, for example
`\mathbb Z_n^d` with nearest-neighbor generators, it may pass the geometric
gate.  Then the algebraic description and the geometric description are two
codes for the same carrier phase:

$$
\boxed{
K_{\rm alg}\simeq K_{geo}.
}
$$

This is healthy.  Algebraic syntax is allowed to describe geometric content.
The relevant question is not whether the code is written algebraically, but
whether the selected carrier has the record-intrinsic spacetime properties.

## 35. Replacement Theorem

### Theorem 18: Bounded-History Carrier-Selection Click Law

Let `B` be a bounded record problem, `\mathcal Y_B` a no-silent target family,
and `\epsilon` a tolerance.  If
`\operatorname{Adm}_B(\mathcal Y_B,\epsilon)` is nonempty and finite modulo
same-actual quotienting, then:

1. the carrier selector `K_B^\star` exists;
2. the carrier-reduced history action `\mathcal A_B^{click}` is defined;
3. the positive bounded-history weight
   `h_B=\exp[-\mathcal A_B^{click}]` is defined;
4. effective probabilities are normalized projections of `h_B` over
   compatible histories;
5. spacetime is licensed exactly when the selected carrier phase passes the
   geometry-irreducibility gate.

**Proof.**

Finiteness modulo same-actual quotienting gives existence of minimizers.
Admissibility gives no-silent completeness, subrawness, and projective
compatibility.  The infimum over carriers defines
`\mathcal A_B^{click}`.  Exponentiating gives a positive bounded-history
weight.  Conditioning on a finite observed panel gives normalized projected
probabilities.  The geometric phase tests are independent readout tests on the
selected minimizers, so spacetime is licensed exactly when those tests pass.
`\square`

### 35.1 What This Replaces

The old false target was:

$$
\boxed{
\text{physical admissibility}\Rightarrow\text{geometry wins}.
}
$$

The replacement is:

$$
\boxed{
\text{physical admissibility}
\Rightarrow
\text{minimal carrier selection}.
}
$$

and:

$$
\boxed{
\text{minimal carrier selection}
+\text{geometry-irreducible selected phase}
\Rightarrow
\text{spacetime onset}.
}
$$

This is the click-law/spacetime split we needed.

## 36. Hostile Review Of The Replacement Law

### Review 1: "You replaced a theorem about geometry with a definition."

Rejected.  The carrier selector is an operational law: minimize a specified
finite action over a specified admissible class and project the resulting
history weights.  Geometry is no longer assumed as the minimizer.

### Review 2: "The target family still matters."

Accepted.  It must.  No bounded experiment computes the entire universe.  The
target family is the finite question plus its no-silent closure at tolerance.

### Review 3: "This still allows algebraic universes."

Accepted.  That is the point.  The click law should not falsely forbid
non-geometric but physically admissible record histories.  It should classify
them as non-spacetime phases.

### Review 4: "Probability is still present."

Only after projection.  The full bounded history cylinder is the primitive.
Probability measures our loss of history information when we compute only a
finite panel.

### Review 5: "Geometry-irreducibility adds new tests."

It adds tests for spacetime, not for clicks.  The Cayley falsification proved
that click admissibility is broader than spacetime admissibility.

### Review 6: "Could a clever non-geometric carrier pass all geometric tests?"

If it passes all record-intrinsic geometric tests, then it is not a
counterexample to spacetime onset.  It is an alternative syntax for the
geometric phase, like a torus described by a group presentation.

### Review 7: "Could the admissible carrier class be empty?"

Yes.  Then the bounded problem is not closed at the requested tolerance.  The
boundary must expand, the history depth must expand, or the target must be
weakened.

## 37. Campaign Result

The corrected law is:

$$
\boxed{
\text{bounded histories}
\to
\text{minimal admissible carrier}
\to
\text{finite panel}
\to
\text{projected effective probabilities}.
}
$$

and spacetime is:

$$
\boxed{
\text{the geometry-irreducible phase of the same carrier selector.}
}
$$

This preserves Barandes alignment:

$$
\boxed{
\text{history first, probability second, Markov transition never primitive.}
}
$$

It also absorbs the falsification instead of hiding it:

$$
\boxed{
\text{the Cayley counterexample is an algebraic carrier phase, not a failure
of the click law.}
}
$$

The old project "prove geometry always wins" is dead.  The new project is
cleaner:

$$
\boxed{
\text{derive the admissible carrier selector, then classify when its minimizer
is geometric.}
}
$$
