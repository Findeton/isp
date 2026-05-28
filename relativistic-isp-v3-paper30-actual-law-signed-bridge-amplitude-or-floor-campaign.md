# Relativistic ISP V3 Paper 30: Actual-Law Signed/Bridge Amplitude Or Floor Campaign

Author: Felix Robles Elvira

Date: 2026-05-25

## Abstract

Paper 29 closed the RN-MIXAMP low-mode value-extraction attempt at the
current-corpus level.  The remaining spectral route needs new same-law
residual values, direct low-mode entries, a Doeblin floor, a defect
Dobrushin/value theorem, or a same-law Peter-Weyl tail table.  This paper
executes the most economical non-spectral continuation left by that ledger:
the signed/bridge amplitude route.

The rule is unchanged.  Everything below is evaluated on the actual adaptive
`SEL2` pushed-forward scalar law.  We do not introduce a heat-kernel
surrogate, a hidden Markov bridge process, a cleaner comparison law, or a
continuum Yang-Mills measure.  The only admissible stochastic object is the
finite record law already selected by Papers 20--29, together with its
literal same-law conditionals.

The result is a sharp current-corpus closure:

1. a same-law signed bridge value theorem would close adaptive Branch A by
   the Paper-23 scalar gate;
2. a same-law finite dual certificate for the signed bridge inequalities
   would close the same route;
3. a same-law bridge damping theorem plus the common Peter-Weyl tail source
   would close the triangle-sum route;
4. a same-law full-object signed range theorem would close the no-tail route;
5. a same-law lower-floor theorem would falsify adaptive Branch A after the
   closing routes fail;
6. the present corpus supplies none of these five value sources.

The paper then goes one step further.  It does not try to unblock the proof
by adding more labels.  Instead it isolates the first genuinely analytic
unblock route: push the actual scalar obstruction back to the finite parent
gauge law, use the exact finite-volume DLR conditional, and ask whether
tree-gauge heat-kernel convolution gives real bridge damping after the RPF
residual tilt is paid.  The parent-law pushforward domination and finite DLR
identity are proved below.  The remaining hard theorem is then localized to
two cofinal quantities: the effective bridge heat time and the residual tilt.

Thus Paper 30 does not prove confinement.  It also does not leave a vague
task behind.  It settles the signed/bridge branch as far as Papers 20--29
permit and exports the next real theorem: print actual signed bridge values,
print a valid finite dual certificate over a narrowed actual-law body, print
actual bridge damping plus tail, print full-object signed range control,
print a lower floor, or leave adaptive Branch A.

## 0. Imports And Same-Law Convention

### Import 0.1: Paper-23 Signed Gate

Paper 23 defines the signed minimal bridge source
`P23-RPF-MIN-SIGNED(Theta,omega,kappa)`.  It asserts that cofinally
$$
        \Theta_{br,0}^{N,j}\le\Theta,\qquad
        \omega_{br,0}^{N,j}\le\omega,\qquad
        \mathrm{P23\text{-}RPF\text{-}MIN\text{-}KTAIL}(\kappa).
$$
Paper 23 Proposition 51.4 proves the scalar closure theorem:
$$
        \sinh\left({\Theta+\omega^2/4\over2}\right)+\kappa
        <
        B_*^{edge}
        \quad\Longrightarrow\quad
        \mathrm{P23\text{-}RPF\text{-}TRANS0}.
$$
Equivalently, for
$$
        M_{\mathrm{sgn}}(\kappa)
        :=
        2\,\operatorname{arsinh}(B_*^{edge}-\kappa),
        \qquad 0\le\kappa<B_*^{edge},
$$
the signed route closes when
$$
        \Theta+\omega^2/4<M_{\mathrm{sgn}}(\kappa).
$$

### Import 0.2: Paper-23 Bridge Damping Gate

Paper 23 defines `P23-RPF-MIN-BRIDGEDAMP(D)` and proves:
$$
\mathrm{P23\text{-}RPF\text{-}MIN\text{-}BRIDGEDAMP}(D)
+
\mathrm{P23\text{-}RPF\text{-}MIN\text{-}KTAIL}(\kappa)
$$
closes `P23-RPF-TRANS0` whenever
$$
        \kappa<B_*^{edge},
        \qquad
        D<D_{\mathrm{crit}}(\kappa).
$$
The constants are the Paper-23 edge budget constants.  This paper does not
renormalize them.

### Import 0.3: Paper-24 Full-Object Certificate Verdict

Paper 24 proves that the full-object finite-dual certificate format is sound,
but the closed Paper-23 scalar body \({\mathcal M}_{56}\) is too wide in the
nontrivial live RPF case.  Residual full-mixed directions remain inside the
closed ledgers and vary the signed range while preserving the already proved
finite constraints.

Therefore a future dual certificate must either use genuinely new same-law
numerical information about the actual adaptive law or work over a narrowed
body.  A certificate over the already closed body is not enough.

### Import 0.4: Paper-27 And Paper-29 Handoff

Paper 27 proves that the current corpus does not supply:
$$
\begin{gathered}
\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}SIGN\text{-}GAP},\\
\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}SPEC\text{-}GAP},\\
\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}SMALL\text{-}GAP},\\
\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}FLOOR\text{-}GAP}.
\end{gathered}
$$
Paper 29 then closes the spectral value-extraction attempt at
`P29-SPECTRAL-VALUE-EXTRACTION-CLOSED` and exports the surviving next steps:
defect influence/value information, a signed/bridge theorem, direct low-mode
entries plus tail, a lower-floor theorem, or exit from adaptive Branch A.

### Convention 0.5: Barandes-Aligned Same-Law Discipline

In this paper, "same-law" means:

1. the pushed-forward scalar record law is the actual adaptive `SEL2` law;
2. all conditionals are conditionals of that law;
3. any quotient, anchor, central-entry division, or Peter-Weyl projection is
   deterministic record processing;
4. no unrecorded subprocess is inserted to make the proof easier;
5. every proposed stochastic equality, domination, or dual certificate must
   be an equality, domination, or certificate on the actual finite record
   body.

This is the operational alignment used throughout Papers 20--29.

## 1. The Actual Signed Bridge Object

### Definition 1.1: True Bridge Carrier

For a selected adaptive row \((N,j)\), and an active minimal edge pair
\((x,y)\), let
$$
        {\mathcal U}_{br,0}^{N,j}(x,y)
$$
be the Paper-23 true-bridge carrier: the finite set of anchored residual
atoms with nonzero four-point mixed debit after endpoint-blind and
endpoint-additive rows have been removed.

For each \(A\in{\mathcal U}_{br,0}^{N,j}(x,y)\), let
$$
        G_A^{anc}(u,v;\zeta)
$$
be its anchored same-law two-endpoint interaction, with \(u,v\) the two
endpoint variables and \(\zeta\) the outside scalar record.

### Definition 1.2: Actual Signed Bridge Hamiltonian

The actual signed bridge Hamiltonian is
$$
        W_{br,0}^{anc,N,j}(u,v;\zeta)
        :=
        \sum_{A\in{\mathcal U}_{br,0}^{N,j}(x,y)}
        G_A^{anc}(u,v;\zeta).
$$
The sum is signed.  No absolute value is taken before summation.

The doubly centered part is
$$
        (W_{br,0}^{anc})^{dc}
        :=
        W_{br,0}^{anc}
        - E_u W_{br,0}^{anc}
        - E_v W_{br,0}^{anc}
        + E_{u,v} W_{br,0}^{anc},
$$
where the conditional averages are same-law conditional expectations over
the two endpoint variables in the selected row.

### Definition 1.3: Signed Range And One-Line Width

Define
$$
        \Theta_{br,0}^{N,j}
        :=
        \operatorname*{ess\,sup}_{x,y,\zeta}
        \operatorname{osc}_{u,v}
        \left[(W_{br,0}^{anc,N,j})^{dc}(u,v;\zeta)\right],
$$
and
$$
        \omega_{br,0}^{N,j}
        :=
        \operatorname*{ess\,sup}_{x,y,\zeta}
        \max\left\{
        \sup_u\operatorname{osc}_v W_{br,0}^{anc,N,j}(u,v;\zeta),
        \sup_v\operatorname{osc}_u W_{br,0}^{anc,N,j}(u,v;\zeta)
        \right\}.
$$

These are literal value quantities, not carrier-size quantities.

### Definition 1.4: Paper-30 Signed Bridge Value Source

`P30-SIGNED-BRIDGE-VALUE(Theta,omega,kappa)` asserts:
$$
        \limsup_{(N,j)}\Theta_{br,0}^{N,j}\le\Theta,
        \qquad
        \limsup_{(N,j)}\omega_{br,0}^{N,j}\le\omega,
$$
and the common same-law tail source
$$
        \mathrm{P23\text{-}RPF\text{-}MIN\text{-}KTAIL}(\kappa)
$$
holds on the same cofinal selector.

### Lemma 1.5: Signed Bridge Value Is Exactly The Paper-23 Signed Source

`P30-SIGNED-BRIDGE-VALUE(Theta,omega,kappa)` implies
`P23-RPF-MIN-SIGNED(Theta,omega,kappa)`.

Proof.

Definitions 1.2--1.4 are the Paper-23 definitions of the signed true-bridge
range and one-line width, restated with the actual-law convention explicit.
The tail source is the same `MIN-KTAIL(kappa)`.  Therefore the three
inequalities in Paper-23 Definition 51.3 hold. `square`

### Theorem 1.6: Positive Signed Bridge Closure

Assume `P30-SIGNED-BRIDGE-VALUE(Theta,omega,kappa)`.  If
$$
        \sinh\left({\Theta+\omega^2/4\over2}\right)+\kappa
        <
        B_*^{edge},
$$
then adaptive Branch A closes at `P23-RPF-TRANS0`.

Proof.

By Lemma 1.5, the Paper-23 signed source holds with the same constants.
Paper 23 Proposition 51.4 gives `P23-RPF-TRANS0`. `square`

### Corollary 1.7: The Signed Value Target Is Sharp

For fixed \(\kappa<B_*^{edge}\), Paper 30 needs only
$$
        \Theta+\omega^2/4<M_{\mathrm{sgn}}(\kappa).
$$
It does not need an unsigned bridge triangle-sum bound.

Proof.

This is the scalar gate equivalence imported from Paper 23.  The signed route
uses cancellation before taking the two-endpoint range, while the unsigned
bridge route pays every true bridge separately. `square`

## 2. Direct Signed Values

### Definition 2.1: Direct Signed Value Theorem

`P30-SIGNED-BRIDGE-DIRECT(Theta,omega,kappa)` asserts that the actual
same-law finite table of values of
$$
        W_{br,0}^{anc,N,j}(u,v;\zeta)
$$
is printed or analytically dominated cofinally strongly enough to prove
`P30-SIGNED-BRIDGE-VALUE(Theta,omega,kappa)`.

The theorem may be proved by:

1. literal row-by-row evaluation;
2. a same-law analytic identity reducing the signed sum;
3. a same-law cancellation theorem pairing bridge rows before oscillation;
4. a verified finite extremal computation over the actual law.

It may not be proved by replacing the adaptive law with a cleaner law.

### Lemma 2.2: Direct Values Close The Signed Route

If `P30-SIGNED-BRIDGE-DIRECT(Theta,omega,kappa)` holds and
$$
        \Theta+\omega^2/4<M_{\mathrm{sgn}}(\kappa),
$$
then `P23-RPF-TRANS0` holds.

Proof.

The direct theorem is defined to imply `P30-SIGNED-BRIDGE-VALUE`.  Apply
Theorem 1.6. `square`

### Proposition 2.3: Current Corpus Does Not Supply Direct Signed Values

The present Papers 20--29 do not prove
`P30-SIGNED-BRIDGE-DIRECT(Theta,omega,kappa)` in a closing range.

Proof.

Paper 23 defines the true bridge table and proves the structural zeroes:
endpoint-blind and endpoint-additive rows do not contribute to the doubly
centered mixed part.  It also defines the signed bridge range.  But it does
not print cofinal numerical values of the signed range or one-line width.

Paper 26 identifies the minimal mixed RN ratio with the true mixed
`CleanRPF`/bridge amplitude table, but Paper 29 proves that such mixed ratios
do not determine the conditional spectral entries or the missing residual
values.  In particular, endpoint-additive one-site terms can cancel from
four-point ratios while changing conditional weights.

Paper 29 further proves that the primitive residual value theorem,
full residual row identity, defect polymer-value theorem, and defect
Dobrushin witness are all unsourced by the current corpus.  Those are exactly
the currently available mechanisms that could populate the signed bridge
values without importing a new law.

Therefore direct signed bridge values are a valid future source theorem, but
not a theorem already proved in Papers 20--29. `square`

We record:
$$
\boxed{\mathrm{P30\text{-}SIGNED\text{-}BRIDGE\text{-}DIRECT\text{-}GAP}.}
$$
Equivalently, the plain label is
`P30-SIGNED-BRIDGE-DIRECT-GAP`.

## 3. Finite Dual Certificate Route

### Definition 3.1: Actual Signed Bridge Record Body

Let
$$
        {\mathcal M}_{30}^{N,j}
$$
be the finite scalar record body consisting of:

1. the actual adaptive `SEL2` scalar record variables;
2. normalization and positivity constraints;
3. declared centrality, covariance, conjugation, quotient, and reflection
   constraints already closed in Papers 20--29;
4. the deterministic `BC/CE`, anchor, and endpoint-additive removals;
5. the literal true-bridge signed Hamiltonian \(W_{br,0}^{anc,N,j}\);
6. any additional same-law value information explicitly proved before the
   certificate is applied.

If item 6 is empty, \({\mathcal M}_{30}^{N,j}\) is just the already closed
Paper-23/Paper-24 certificate body restricted to the signed bridge target.

### Definition 3.2: Signed Bridge Dual Certificate

`P30-SIGNED-BRIDGE-DUAL(Theta,omega)` asserts that, cofinally, the universal
inequalities
$$
        -\Theta
        \le
        (W_{br,0}^{anc})^{dc}(u,v;\zeta)
        -
        (W_{br,0}^{anc})^{dc}(u',v';\zeta)
        \le
        \Theta
$$
and the two one-line width inequalities bounded by \(\omega\) have finite
same-law certificates over \({\mathcal M}_{30}^{N,j}\).

The certificate may use equality multipliers, positivity/RP/covariance
inequality multipliers, compact finite-record convex or semialgebraic dual
terms, and any new value constraints listed in Definition 3.1(6).  It may not
use the target signed range inequality as an input.

### Lemma 3.3: Dual Certificate Implies Signed Value

If `P30-SIGNED-BRIDGE-DUAL(Theta,omega)` holds and
`P23-RPF-MIN-KTAIL(kappa)` holds on the same cofinal selector, then
`P30-SIGNED-BRIDGE-VALUE(Theta,omega,kappa)` holds.

Proof.

The dual certificate proves the signed range and one-line width inequalities
uniformly on the finite record body containing the actual adaptive law.  The
tail source supplies the third component of Definition 1.4. `square`

### Corollary 3.4: Dual Certificate Closure

Assume
$$
\mathrm{P30\text{-}SIGNED\text{-}BRIDGE\text{-}DUAL}(\Theta,\omega)
+
\mathrm{P23\text{-}RPF\text{-}MIN\text{-}KTAIL}(\kappa).
$$
If
$$
        \Theta+\omega^2/4<M_{\mathrm{sgn}}(\kappa),
$$
then `P23-RPF-TRANS0` holds.

Proof.

Apply Lemma 3.3 and Theorem 1.6. `square`

### Proposition 3.5: Closed-Body Duals Still Do Not Close

If Definition 3.1(6) is empty, the present corpus does not prove
`P30-SIGNED-BRIDGE-DUAL(Theta,omega)` in a closing range.

Proof.

This is the Paper-24 obstruction in signed-bridge language.  The closed
constraint body contains normalization, positivity, quotient, covariance,
central-entry, local removal, and endpoint-additive removal data.  Those
constraints identify zero rows and quotient symmetries, but they do not
bound the magnitude of surviving true-bridge mixed modes.

Paper 23 Sections 51--56 prove that equality-only and RP/positivity-only
arguments cannot certify a nontrivial signed range without a genuine
extremal or value theorem.  Paper 24 then proves that the full-object
closed body retains residual mixed directions which vary the signed range
while preserving the closed ledgers.

Therefore a certificate over the already closed body is not available in the
closing region.  A future certificate must narrow the body by adding new
same-law value information, or explicitly print a certificate not derivable
from the old ledgers alone. `square`

We record:
$$
\boxed{\mathrm{P30\text{-}SIGNED\text{-}BRIDGE\text{-}DUAL\text{-}GAP}.}
$$
Equivalently, the plain label is
`P30-SIGNED-BRIDGE-DUAL-GAP`.

### Corollary 3.6: What A Future Dual Must Add

A future positive dual certificate must include at least one of:

1. literal same-law signed bridge values;
2. a same-law cancellation identity among true bridges;
3. same-law conditional influence or defect Dobrushin data;
4. a same-law tail/low-mode theorem strong enough to shrink the live range;
5. a new finite extremal theorem over a narrowed actual-law body.

Proof.

Proposition 3.5 excludes the old closed body.  The listed mechanisms are the
ways to shrink that body or directly bound the target functional without
changing the law. `square`

## 4. Bridge Damping Plus Tail

### Definition 4.1: Paper-30 Bridge Damping Source

`P30-BRIDGEDAMP(D,kappa)` asserts:

1. the actual same-law bridge damping source
   `P23-RPF-MIN-BRIDGEDAMP(D)` holds;
2. the common tail source
   `P23-RPF-MIN-KTAIL(kappa)` holds;
3. both are proved on the same cofinal adaptive selector.

### Theorem 4.2: Positive Bridge-Damping Closure

If `P30-BRIDGEDAMP(D,kappa)` holds and
$$
        \kappa<B_*^{edge},
        \qquad
        D<D_{\mathrm{crit}}(\kappa),
$$
then `P23-RPF-TRANS0` holds.

Proof.

This is Paper 23 Proposition 50.5 with the same-law cofinality requirement
made explicit. `square`

### Proposition 4.3: Current Corpus Does Not Prove Bridge Damping Plus Tail

The present Papers 20--29 do not prove `P30-BRIDGEDAMP(D,kappa)` in a
closing range.

Proof.

Paper 23 proves that the true-bridge carrier is finite and that bridge
damping plus tail would close the branch.  It also proves that finite
cardinality and canonical row labels do not imply useful damping, because
they do not bound the actual mixed oscillation of surviving bridge rows.

Paper 25 repeats this as an actual-law source audit: bridge damping plus tail
is a valid positive Branch-A route, but the bridge amplitudes and the common
tail budget are not supplied by the current papers.

Paper 28 and Paper 29 then attack the spectral/tail side more sharply.
They prove that the current corpus supplies no strict low-mode spectral gap,
no cofinal Peter-Weyl tail table, no finite-band support theorem for the
actual residual minimal-edge Hamiltonian, and no primitive residual values
from which such a tail could be recovered.

Thus neither component of `P30-BRIDGEDAMP(D,kappa)` is available in the
closing range. `square`

We record:
$$
\boxed{\mathrm{P30\text{-}BRIDGEDAMP\text{-}TAIL\text{-}GAP}.}
$$
Equivalently, the plain label is `P30-BRIDGEDAMP-TAIL-GAP`.

## 5. Full-Object No-Tail Signed Route

### Definition 5.1: Full Signed Object

Let
$$
        C_0^{m,N,j}(u,v;\zeta)
$$
be the exact normalized minimal-edge conditional Hamiltonian after `BC/CE`,
anchoring, and deterministic endpoint processing, with no Peter-Weyl
projection.

Define
$$
        \Theta_{\mathrm{full}}^{N,j}
        :=
        \operatorname*{ess\,sup}_{x,y,\zeta}
        \operatorname{osc}_{u,v}
        \left[(C_0^{m,N,j})^{dc}(u,v;\zeta)\right],
$$
and
$$
        \omega_{\mathrm{full}}^{N,j}
        :=
        \operatorname*{ess\,sup}_{x,y,\zeta}
        \max\left\{
        \sup_u\operatorname{osc}_v C_0^{m,N,j}(u,v;\zeta),
        \sup_v\operatorname{osc}_u C_0^{m,N,j}(u,v;\zeta)
        \right\}.
$$

`P30-SIGNED-FULL(Theta,omega)` asserts cofinal bounds
$$
        \Theta_{\mathrm{full}}^{N,j}\le\Theta,
        \qquad
        \omega_{\mathrm{full}}^{N,j}\le\omega.
$$

### Lemma 5.2: Full Object Avoids Ktail

If `P30-SIGNED-FULL(Theta,omega)` holds and
$$
        \sinh\left({\Theta+\omega^2/4\over2}\right)
        <
        B_*^{edge},
$$
then `P23-RPF-TRANS0` holds.

Proof.

This is Paper 23 Proposition 56.2.  Since no projection is applied, there is
no Peter-Weyl tail debit. `square`

### Proposition 5.3: Current Corpus Does Not Prove The Full No-Tail Source

The present Papers 20--29 do not prove `P30-SIGNED-FULL(Theta,omega)` in a
closing range.

Proof.

Paper 23 proves the full-object no-tail theorem as a valid route.  Paper 24
then proves the obstacle: the closed finite record body admits live residual
mixed directions which vary the full signed range.  Avoiding the tail debit
therefore makes the value theorem stronger, not easier.  The uncontrolled
tail modes no longer appear as \(\kappa\); they appear directly in
\(\Theta_{\mathrm{full}}\) and \(\omega_{\mathrm{full}}\).

Papers 25--29 supply no new same-law full-object range values, no full-object
finite dual certificate, no strict spectral contraction plus tail theorem,
and no primitive residual value theorem.  Therefore the full no-tail source
remains unsourced. `square`

We record:
$$
\boxed{\mathrm{P30\text{-}SIGNED\text{-}FULL\text{-}GAP}.}
$$
Equivalently, the plain label is `P30-SIGNED-FULL-GAP`.

## 6. Lower-Floor Exit

### Definition 6.1: Signed/Bridge Lower Floor

`P30-SIGNED-BRIDGE-FLOOR(M_*)` asserts a same-law lower floor strong enough
to force
$$
        \overline\Lambda_{13}^{RPF}\ge M_*,
$$
or an equivalent lower bound on the actual minimal RPF predebit after all
closed reductions are applied.

This is not a failure of a sufficient test.  It is a positive lower-bound
theorem on the actual adaptive law.

### Lemma 6.2: Lower Floor Falsifies Adaptive Branch A After Route Failure

If all closing routes available in adaptive Branch A fail and
`P30-SIGNED-BRIDGE-FLOOR(M_*)` holds, then adaptive Branch A is falsified.

Proof.

The adaptive Branch-A theorem needs the actual RPF predebit below the
threshold \(M_*\).  If the lower floor forces
\(\overline\Lambda_{13}^{RPF}\ge M_*\), then the branch cannot meet its
strict loss budget.  Route failure alone is not enough; the lower floor is
the separate falsifying theorem. `square`

### Proposition 6.3: Current Corpus Does Not Prove The Lower Floor

The present Papers 20--29 do not prove `P30-SIGNED-BRIDGE-FLOOR(M_*)`.

Proof.

Paper 25 and Paper 27 explicitly separate current-corpus nonclosure from a
lower-floor theorem.  They prove that the existing route failures do not
decide the actual truth value of adaptive Branch A and do not imply
\(\overline\Lambda_{13}^{RPF}\ge M_*\).

Paper 29 sharpens the issue for the residual-value route: even failure of
defect Dobrushin does not itself imply a floor.  A coherent defect witness
with sign coherence, normalization survival, and a lower-floor comparison is
needed, and that witness is unsourced.

Therefore no lower-floor theorem is presently available. `square`

We record:
$$
\boxed{\mathrm{P30\text{-}SIGNED\text{-}BRIDGE\text{-}FLOOR\text{-}GAP}.}
$$
Equivalently, the plain label is
`P30-SIGNED-BRIDGE-FLOOR-GAP`.

## 7. No More Finite-Label Escape

### Proposition 7.1: Finite Labels Do Not Determine Signed Bridge Values

Finite true-bridge labels, canonical selector labels, and quotient labels do
not determine the cofinal signed bridge range
\((\Theta_{br,0}^{N,j},\omega_{br,0}^{N,j})\).

Proof.

Finite labels determine which rows exist, which rows are structurally zero,
and which rows are equivalent under already declared symmetries.  They do
not determine the actual same-law scalar values of surviving mixed rows.

Paper 23 proves that live true-bridge rows remain after endpoint-blind and
endpoint-additive removals.  Paper 24 proves that the closed finite record
body leaves residual mixed directions.  Paper 29 proves that the missing
primitive residual values are not recovered from the existing row identities
or RN-MIXAMP ratios.  Hence labels alone cannot compute or bound the signed
range in a closing interval. `square`

### Corollary 7.2: Paper-30 Label No-Go

Any future Branch-A proof that stays in the signed/bridge channel must add
actual same-law values, not merely more labels.

Proof.

All finite carriers relevant to this channel have already been named:
true bridges, signed bridge sums, full-object signed ranges, tail profiles,
finite dual bodies, and lower-floor witnesses.  The unresolved quantities are
their values. `square`

We record:
$$
\boxed{\mathrm{P30\text{-}SIGNED\text{-}BRIDGE\text{-}LABEL\text{-}NOGO}.}
$$
Equivalently, the plain label is
`P30-SIGNED-BRIDGE-LABEL-NOGO`.

## 8. Paper-30 Completion Theorem

### Theorem 8.1: Signed/Bridge Current-Corpus Verdict

The signed/bridge campaign has the following exact status:

1. `P30-SIGNED-BRIDGE-VALUE(Theta,omega,kappa)` is a valid positive source.
   It closes adaptive Branch A whenever
   $$
   \Theta+\omega^2/4<M_{\mathrm{sgn}}(\kappa).
   $$
2. `P30-SIGNED-BRIDGE-DIRECT(Theta,omega,kappa)` is a valid way to source
   the signed value theorem.
3. `P30-SIGNED-BRIDGE-DUAL(Theta,omega)` plus `MIN-KTAIL(kappa)` is a valid
   way to source the signed value theorem.
4. `P30-BRIDGEDAMP(D,kappa)` is a valid positive bridge route when
   $$
   \kappa<B_*^{edge},\qquad D<D_{\mathrm{crit}}(\kappa).
   $$
5. `P30-SIGNED-FULL(Theta,omega)` is a valid no-tail route when
   $$
   \sinh((\Theta+\omega^2/4)/2)<B_*^{edge}.
   $$
6. `P30-SIGNED-BRIDGE-FLOOR(M_*)` is a valid falsifying lower-floor route
   after the positive routes fail.
7. The present Papers 20--29 prove none of these source theorems in a
   closing or falsifying range.
8. More finite labels alone cannot change this verdict.

Proof.

Items 1--6 are Theorem 1.6, Lemma 2.2, Corollary 3.4, Theorem 4.2, Lemma
5.2, and Lemma 6.2.  Item 7 is the collection of current-corpus gap
propositions:
$$
\begin{gathered}
\mathrm{P30\text{-}SIGNED\text{-}BRIDGE\text{-}DIRECT\text{-}GAP},\\
\mathrm{P30\text{-}SIGNED\text{-}BRIDGE\text{-}DUAL\text{-}GAP},\\
\mathrm{P30\text{-}BRIDGEDAMP\text{-}TAIL\text{-}GAP},\\
\mathrm{P30\text{-}SIGNED\text{-}FULL\text{-}GAP},\\
\mathrm{P30\text{-}SIGNED\text{-}BRIDGE\text{-}FLOOR\text{-}GAP}.
\end{gathered}
$$
Item 8 is Corollary 7.2. `square`

### Corollary 8.2: Next Real Theorem After Paper 30

After Paper 30, the next Branch-A theorem must be one of:

1. direct same-law signed bridge values;
2. a narrowed-body finite dual certificate for the signed bridge range;
3. actual bridge damping plus the common same-law Peter-Weyl tail;
4. full-object signed range control with no tail debit;
5. a lower-floor theorem
   $$
   \overline\Lambda_{13}^{RPF}\ge M_*;
   $$
6. a return to the defect value/influence routes of Paper 29;
7. an exit from adaptive Branch A to Branch B or Branch C.

No finite-template, canonical-label, quotient, or carrier refinement is a
substitute for these same-law value theorems.

### Corollary 8.3: Continuum YM Confinement Status After Paper 30

The continuum Yang-Mills confinement proof remains open.  Adaptive Branch A
has not been proved and has not been falsified.  Paper 30 completes the
signed/bridge current-corpus audit: the route is mathematically sound, but
the actual same-law signed/bridge value source is not yet present.

## 9. Part II: Analytic Unblock Rather Than More Labels

The current-corpus verdict of Sections 1--8 is not a request for a larger
finite table.  It is a request for value information.  The feedback diagnosed
the danger correctly: if the only way to obtain the missing values is to
solve the full infinite-volume Yang-Mills conditional law, then adaptive
Branch A has merely re-encoded the Clay difficulty.

The goal of Part II is therefore narrower and more surgical.  We try to
avoid reconstructing the full scalar conditional law by proving that the
specific signed/bridge obstruction is dominated by a finite parent-law
conditional estimate already visible before the scalar pushforward.

The proposed route is:
$$
\boxed{
\mathrm{parent\ finite\ gauge\ law}
\longrightarrow
\mathrm{finite\ DLR\ conditional}
\longrightarrow
\mathrm{tree\text{-}gauge\ heat\text{-}kernel\ bridge\ damping}
\longrightarrow
\mathrm{P30\text{-}BRIDGEDAMP}(D,\kappa).
}
$$

This is still hard.  But it is not the same as asking for the whole
infinite-volume measure.  It asks for a targeted upper bound on the finite
same-law bridge amplitude after deterministic scalar pushforward.

## 10. Parent-Law Pushforward Domination

### Definition 10.1: Parent Law And Scalar Pushforward

Let
$$
        (\Omega_{N,j}^{par},\nu_{N,j}^{par})
$$
be the finite parent lattice gauge row used before the adaptive `SEL2`
scalar pushforward.  Its coordinates are compact-group link or plaquette
variables, with the finite gauge action, boundary convention, `BC/CE`
normalization, and adaptive selector already fixed.

Let
$$
        S_{N,j}:\Omega_{N,j}^{par}\to\Omega_{N,j}^{SEL2}
$$
be the deterministic scalar record map.  The actual adaptive scalar law is
$$
        \nu_{N,j}^{SEL2}:=(S_{N,j})_\#\nu_{N,j}^{par}.
$$

For a finite scalar region \(R\), write \(S_R\) for the restricted scalar
map and \(S_{\partial R}\) for the boundary scalar map.

### Definition 10.2: Parent And Scalar Conditional Kernels

For a parent boundary configuration \(\eta\), let
$$
        K_R^{par}(\eta)
$$
be the parent conditional law of the parent variables in \(R\) given
\(\eta\).  Its scalar pushforward is
$$
        \widehat K_R^{par}(\eta):=(S_R)_\# K_R^{par}(\eta).
$$

For a scalar boundary record \(\zeta\), let
$$
        K_R^{SEL2}(\zeta)
$$
be the actual scalar conditional law of \(S_R\) given
$$
        S_{\partial R}=\zeta.
$$

All objects are finite regular conditional probabilities.  No Markov
subprocess is introduced.

### Lemma 10.3: Scalar Conditionals Are Mixtures Of Parent Conditionals

For every scalar boundary \(\zeta\), there exists a probability measure
\(\Pi_\zeta\) on parent boundaries satisfying \(S_{\partial R}(\eta)=\zeta\)
such that
$$
        K_R^{SEL2}(\zeta)
        =
        \int \widehat K_R^{par}(\eta)\,d\Pi_\zeta(\eta).
$$

Proof.

This is disintegration on a finite measure space.  Conditioning the parent
law on the scalar event \(S_{\partial R}=\zeta\) gives a probability measure
on the parent boundary fiber.  Conditional on each parent boundary point
\(\eta\), the scalar interior law is exactly the pushforward
\(\widehat K_R^{par}(\eta)\).  Integrating over the parent boundary fiber
gives the scalar conditional law. `square`

### Theorem 10.4: Parent-Law Pushforward Domination

For any two scalar boundary records \(\zeta,\zeta'\),
$$
\left\|
K_R^{SEL2}(\zeta)-K_R^{SEL2}(\zeta')
\right\|_{\rm TV}
\le
\sup_{\substack{
S_{\partial R}(\eta)=\zeta\\
S_{\partial R}(\eta')=\zeta'}}
\left\|
K_R^{par}(\eta)-K_R^{par}(\eta')
\right\|_{\rm TV}.
$$
Consequently every scalar Dobrushin or bridge-influence coefficient is
bounded by the corresponding parent coefficient after taking the same
boundary variation and then pushing forward.

Proof.

By Lemma 10.3,
$$
K_R^{SEL2}(\zeta)-K_R^{SEL2}(\zeta')
=
\int \widehat K_R^{par}(\eta)\,d\Pi_\zeta(\eta)
-
\int \widehat K_R^{par}(\eta')\,d\Pi_{\zeta'}(\eta').
$$
Couple the two mixing measures arbitrarily.  Convexity of total variation
gives
$$
\left\|
K_R^{SEL2}(\zeta)-K_R^{SEL2}(\zeta')
\right\|_{\rm TV}
\le
\iint
\left\|
\widehat K_R^{par}(\eta)-\widehat K_R^{par}(\eta')
\right\|_{\rm TV}
d\Pi_\zeta d\Pi_{\zeta'}.
$$
Pushforward contracts total variation:
$$
\left\|
\widehat K_R^{par}(\eta)-\widehat K_R^{par}(\eta')
\right\|_{\rm TV}
\le
\left\|
K_R^{par}(\eta)-K_R^{par}(\eta')
\right\|_{\rm TV}.
$$
Taking the supremum over the two boundary fibers proves the claim. `square`

We record the exact theorem:
$$
\boxed{\mathrm{P30\text{-}PARENT\text{-}PUSH\text{-}DOM}}.
$$
Equivalently, the plain label is `P30-PARENT-PUSH-DOM`.

### Lemma 10.5: Log-Oscillation Pushforward Domination

Let \(p_\eta(x)\) and \(p_{\eta'}(x)\) be two positive parent conditional
densities on a finite parent fiber, and let \(S_R(x)=s\) be a deterministic
scalar readout.  Define pushed densities
$$
        q_\eta(s):=\int_{S_R^{-1}(s)}p_\eta(x)\,dx,\qquad
        q_{\eta'}(s):=\int_{S_R^{-1}(s)}p_{\eta'}(x)\,dx.
$$
If for all \(x\in S_R^{-1}(s)\) and \(x'\in S_R^{-1}(s')\),
$$
        \left|
        \log {p_\eta(x)p_{\eta'}(x')\over p_\eta(x')p_{\eta'}(x)}
        \right|
        \le D,
$$
then
$$
        \left|
        \log {q_\eta(s)q_{\eta'}(s')\over q_\eta(s')q_{\eta'}(s)}
        \right|
        \le D.
$$
Consequently parent pointwise log-cross-ratio bounds descend to scalar
log-Hamiltonian mixed oscillation bounds under deterministic pushforward.

Proof.

The hypothesis is equivalent to
$$
        e^{-D}
        \le
        {p_\eta(x)p_{\eta'}(x')\over p_\eta(x')p_{\eta'}(x)}
        \le
        e^D
$$
for every pair of parent representatives in the two scalar fibers.  Multiply
by the positive measures on the two fibers and integrate in \((x,x')\).  The
left side becomes
$$
        e^{-D}q_\eta(s')q_{\eta'}(s)
        \le
        q_\eta(s)q_{\eta'}(s')
        \le
        e^Dq_\eta(s')q_{\eta'}(s),
$$
which is the desired logarithmic cross-ratio bound. `square`

We record:
$$
\boxed{\mathrm{P30\text{-}PARENT\text{-}LOGOSC\text{-}DOM}}.
$$
Equivalently, the plain label is `P30-PARENT-LOGOSC-DOM`.

### Corollary 10.6: Why This Is Barandes-Aligned

`P30-PARENT-PUSH-DOM` does not compose an undeclared subprocess.  It uses:

1. the actual parent finite gauge law;
2. the deterministic scalar readout \(S_{N,j}\);
3. finite disintegration;
4. total-variation contraction under pushforward;
5. the log-sum-exp monotonicity in Lemma 10.5 for Hamiltonian oscillations.

Thus it is a permitted way to import parent-law estimates into the scalar
record law.  It does not by itself prove any parent estimate.

## 11. Exact Finite-Volume DLR Conditional

### Definition 11.1: Parent DLR Bridge Region

Let \(R_{br}\) be a finite parent bridge region whose scalar readout contains
one active true bridge in \({\mathcal U}_{br,0}^{N,j}(x,y)\).  Let
\(\partial R_{br}\) be its parent boundary.  After gauge fixing on a tree
inside \(R_{br}\), write the remaining parent variables as
$$
        g=(g_1,\ldots,g_m)\in G^m,\qquad G=SU(N).
$$

### Definition 11.2: Finite DLR Density

For parent boundary \(\eta\), the finite parent DLR conditional has the form
$$
dK_{R_{br}}^{par}(g\mid\eta)
=
{1\over Z(\eta)}
\left[
\prod_{p\cap R_{br}\ne\varnothing}
H_{t_p}\!\left(h_p(g,\eta)\right)
\right]
\exp\!\left(-V_{RPF}(g,\eta)\right)
J_{tree}(g,\eta)\,dg.
$$
Here:

1. \(H_{t_p}\) is the compact-group heat-kernel plaquette density in the
   declared finite row;
2. \(h_p(g,\eta)\) is the plaquette holonomy after tree gauge;
3. \(V_{RPF}\) is the finite residual potential left after the licensed
   `BC/CE` and retained-row removals;
4. \(J_{tree}\) is the finite gauge-fixing/Haar Jacobian, including any
   deterministic readout Jacobian that remains on the chart;
5. \(Z(\eta)\) is the conditional normalizer.

This formula is finite-row exact whenever the parent row is the finite
heat-kernel lattice row declared in Papers 20--23.

### Lemma 11.3: Finite DLR Exactness

The scalar bridge conditional \(K_{R_{br}}^{SEL2}\) is the pushforward under
\(S_{R_{br}}\) of the mixture of the exact DLR conditionals in Definition
11.2 over the parent boundary fiber.

Proof.

Definition 11.2 is the ordinary finite-volume conditional density of the
parent finite gauge law after gauge fixing.  Lemma 10.3 then pushes this
conditional through the scalar readout and mixes over the parent boundaries
with the same scalar boundary. `square`

We record:
$$
\boxed{\mathrm{P30\text{-}FV\text{-}DLR\text{-}EXACT}}.
$$
Equivalently, the plain label is `P30-FV-DLR-EXACT`.

### Corollary 11.4: The New Analytic Work Is Localized

After `P30-PARENT-PUSH-DOM` and `P30-FV-DLR-EXACT`, the missing bridge
damping theorem is no longer mysterious.  It is the task of bounding the
variation of the finite DLR density in Definition 11.2 under bridge boundary
changes.

The only nontrivial terms are:

1. heat-kernel convolution along gauge-fixed bridge paths;
2. the residual tilt \(V_{RPF}\);
3. the chart/Jacobian oscillation \(J_{tree}\);
4. the normalizer ratio \(Z(\eta)/Z(\eta')\).

## 12. Tree-Gauge Heat-Kernel Bridge Damping

### Definition 12.1: Effective Bridge Heat Time

For a true bridge atom \(A\), let \(\ell(A)\) be the Paper-23 bridge
separation statistic.  In the tree-gauge DLR chart, define
$$
        T_{br}(A)
$$
to be the smallest total heat-kernel convolution time that any nontrivial
endpoint representation must cross in order to transmit the boundary
variation from one side of the bridge to the other.

Define the cofinal effective heat-time slope
$$
        \tau_{br}^{cof}
        :=
        \liminf_{(N,j)}
        \inf_{A\in{\mathcal U}_{br,0}^{N,j}}
        {T_{br}(A)\over \ell(A)}.
$$

### Definition 12.2: Residual Tilt Cost

Let
$$
        \chi_{tilt}^{N,j}(A)
$$
be the worst bridge-normalized oscillation cost coming from
$$
        V_{RPF},\quad J_{tree},\quad Z(\eta)/Z(\eta')
$$
in Definition 11.2, after subtracting all retained licensed rows.  The
cofinal tilt slope is
$$
        \chi_{tilt}^{cof}
        :=
        \limsup_{(N,j)}
        \sup_{A\in{\mathcal U}_{br,0}^{N,j}}
        {\chi_{tilt}^{N,j}(A)\over \ell(A)}.
$$

### Definition 12.3: Parent Heat-Kernel Bridge Damping Source

`P30-TREE-HK-BRIDGEDAMP(A0,m)` asserts that cofinally every true bridge
amplitude satisfies
$$
        d_A^{br}(x,y)
        \le
        A_0\,e^{-m\ell(A)}.
$$

The heat-kernel proof mechanism is the strict inequality
$$
        m
        <
        {1\over2}C_{min}^{br}\tau_{br}^{cof}
        -
        \chi_{tilt}^{cof},
$$
where \(C_{min}^{br}\) is the smallest nonzero Casimir among the endpoint
representations that can carry the bridge variation.

### Lemma 12.4: Heat-Kernel Convolution Gives Representation Damping

In the parent DLR chart, a bridge transmission in representation \(\rho\)
across total heat time \(T\) is multiplied by
$$
        \exp\!\left(-{1\over2}C_2(\rho)T\right).
$$
Therefore the smallest nontrivial bridge channel is damped by at least
$$
        \exp\!\left(-{1\over2}C_{min}^{br}T_{br}(A)\right).
$$

Proof.

This is the compact-group heat-kernel semigroup identity in Peter-Weyl
coordinates:
$$
        H_T(g)=\sum_\rho d_\rho
        e^{-C_2(\rho)T/2}\chi_\rho(g).
$$
Tree gauge reduces bridge transmission to convolution along the bridge
path.  Convolution adds heat times, so the nontrivial representation
coefficient is multiplied by the displayed factor. `square`

### Proposition 12.5: Heat-Kernel Damping With Tilt Control

Assume:

1. `P30-PARENT-PUSH-DOM`;
2. `P30-PARENT-LOGOSC-DOM`;
3. `P30-FV-DLR-EXACT`;
4. \(\tau_{br}^{cof}>0\);
5. \(\chi_{tilt}^{cof}<\frac12 C_{min}^{br}\tau_{br}^{cof}\).

Then `P30-TREE-HK-BRIDGEDAMP(A0,m)` holds for every
$$
        0<m<
        {1\over2}C_{min}^{br}\tau_{br}^{cof}
        -
        \chi_{tilt}^{cof},
$$
with some finite \(A_0\).

Proof.

Lemma 12.4 gives the heat-kernel factor
$$
\exp\!\left(-{1\over2}C_{min}^{br}T_{br}(A)\right).
$$
By Definitions 12.1--12.2, the remaining residual, Jacobian, and normalizer
terms contribute at most
$$
        \exp(\chi_{tilt}^{N,j}(A)+o(\ell(A))).
$$
Combining the two bounds gives
$$
d_A^{br}(x,y)
\le
A_0
\exp\!\left[
-\left({1\over2}C_{min}^{br}\tau_{br}^{cof}
-\chi_{tilt}^{cof}-o(1)\right)\ell(A)
\right].
$$
Absorb finite short bridges and the \(o(1)\) slack into \(A_0\), then choose
any strict \(m\) below the displayed exponent.  Lemma 10.5 pushes the parent
log-cross-ratio bound to the scalar bridge Hamiltonian without increasing
the mixed oscillation. `square`

### Corollary 12.6: Bridge-Damping Sum Test

Let \(N_{br}(\ell)\) be the number of true bridge atoms of length \(\ell\)
incident to a fixed active edge, and assume
$$
        N_{br}(\ell)\le C_{br}e^{g_{br}\ell}.
$$
If
$$
        m>g_{br},
$$
then
$$
        D
        :=
        \sum_{\ell\ge1} C_{br}A_0e^{-(m-g_{br})\ell}
$$
is finite, and `P23-RPF-MIN-BRIDGEDAMP(D)` holds.  If moreover
$$
        D<D_{\mathrm{crit}}(\kappa)
$$
and `P23-RPF-MIN-KTAIL(kappa)` holds with \(\kappa<B_*^{edge}\), then
adaptive Branch A closes.

Proof.

The first statement is the bridge amplitude sum using
`P30-TREE-HK-BRIDGEDAMP(A0,m)`.  The last statement is Theorem 4.2. `square`

We record the complete positive route:
$$
\boxed{
\begin{array}{c}
\mathrm{P30\text{-}PARENT\text{-}PUSH\text{-}DOM}
+\mathrm{P30\text{-}PARENT\text{-}LOGOSC\text{-}DOM}
+\mathrm{P30\text{-}FV\text{-}DLR\text{-}EXACT}\\
+\left[
{1\over2}C_{min}^{br}\tau_{br}^{cof}
-\chi_{tilt}^{cof}
>g_{br}
\right]
+\mathrm{P23\text{-}RPF\text{-}MIN\text{-}KTAIL}(\kappa)
\Longrightarrow
\mathrm{P23\text{-}RPF\text{-}TRANS0}
\end{array}}
$$
provided the resulting \(D\) lies below \(D_{\mathrm{crit}}(\kappa)\).

## 13. Current Status Of The Heat-Kernel Bridge Route

### Proposition 13.1: What Is Proved Now

The present Paper 30 proves:
$$
\mathrm{P30\text{-}PARENT\text{-}PUSH\text{-}DOM}
\quad
\mathrm{P30\text{-}PARENT\text{-}LOGOSC\text{-}DOM}
\quad\text{and}\quad
\mathrm{P30\text{-}FV\text{-}DLR\text{-}EXACT}.
$$

Proof.

These are Theorem 10.4, Lemma 10.5, and Lemma 11.3. `square`

### Proposition 13.2: What Is Not Proved Now

The present Papers 20--30 do not prove the strict bridge exponent inequality
$$
        {1\over2}C_{min}^{br}\tau_{br}^{cof}
        -
        \chi_{tilt}^{cof}
        >
        g_{br},
$$
nor do they prove the common tail source
$$
        \mathrm{P23\text{-}RPF\text{-}MIN\text{-}KTAIL}(\kappa)
$$
in the closing range.

Proof.

Papers 20--23 contain real finite heat-kernel diagnostics, axial-tree
convolution formulas, and character-tail estimates for declared heat-kernel
rows.  But Paper 23 already separates those clean heat-kernel rows from the
actual adaptive residual law after `BC/CE` and RPF division.  Papers 26--29
then prove that the missing residual values, conditional normalizers, defect
values, and tail profiles are not populated by the current corpus.

The two quantities
$$
        \tau_{br}^{cof},
        \qquad
        \chi_{tilt}^{cof}
$$
have now been isolated, but not computed or bounded.  In particular, no
paper proves that residual tilt grows more slowly than the heat-kernel
convolution damping, and no paper proves that the remaining Peter-Weyl tail
budget is small enough for the bridge gate. `square`

We record:
$$
\boxed{\mathrm{P30\text{-}TREE\text{-}HK\text{-}BRIDGEDAMP\text{-}GAP}.}
$$
Equivalently, the plain label is `P30-TREE-HK-BRIDGEDAMP-GAP`.

### Corollary 13.3: The Sharp Computation To Try Next

The route is now reduced to the following finite/cofinal computation:
$$
        \boxed{
        m_{HK}^{eff}
        :=
        {1\over2}C_{min}^{br}\tau_{br}^{cof}
        -
        \chi_{tilt}^{cof}
        }
$$
and the test
$$
        m_{HK}^{eff}>g_{br},
        \qquad
        D(m_{HK}^{eff})<D_{\mathrm{crit}}(\kappa),
        \qquad
        \kappa<B_*^{edge}.
$$

This is the first genuinely analytic Paper-30 unblock target.  It is not
another label theorem.

## 14. Signed Heat-Kernel Variant

The unsigned bridge route may fail because it pays every true bridge
amplitude absolutely.  The signed route should be tested in the same parent
DLR chart before absolute values are taken.

### Definition 14.1: Tree-Gauge Signed Heat-Kernel Source

`P30-TREE-HK-SIGNED(Theta,omega,kappa)` asserts that the tree-gauge DLR
character expansion of the signed bridge sum satisfies
$$
        \Theta_{br,0}^{N,j}\le\Theta,\qquad
        \omega_{br,0}^{N,j}\le\omega
$$
cofinally, with the same tail source `MIN-KTAIL(kappa)`.

The proof mechanism may use orientation, representation duality, reflection
symmetry, or heat-kernel character signs, but only after each identity is
proved as an identity of the actual parent finite law and then pushed
through the scalar record map.

### Lemma 14.2: Signed Heat-Kernel Source Closes The Signed Route

If `P30-TREE-HK-SIGNED(Theta,omega,kappa)` holds and
$$
        \Theta+\omega^2/4<M_{\mathrm{sgn}}(\kappa),
$$
then `P23-RPF-TRANS0` holds.

Proof.

`P30-TREE-HK-SIGNED` is a proof mechanism for
`P30-SIGNED-BRIDGE-VALUE`.  Apply Theorem 1.6. `square`

### Proposition 14.3: Current Corpus Does Not Prove Signed Heat-Kernel Cancellation

The present Papers 20--30 do not prove
`P30-TREE-HK-SIGNED(Theta,omega,kappa)` in a closing range.

Proof.

Papers 20--23 contain heat-kernel character calculations on declared rows,
but the signed bridge target is the residual minimal-edge object after
division, anchoring, retained-row removal, and adaptive scalar pushforward.
Paper 24 proves that the closed finite body still allows live mixed
directions.  Paper 29 proves that the primitive residual values needed to
evaluate those directions are not supplied.  The signed heat-kernel route
therefore needs a new identity showing that the actual residual bridge
characters cancel in the signed sum.  No such identity is printed. `square`

We record:
$$
\boxed{\mathrm{P30\text{-}TREE\text{-}HK\text{-}SIGNED\text{-}GAP}.}
$$
Equivalently, the plain label is `P30-TREE-HK-SIGNED-GAP`.

## 15. Why A Blanket Dobrushin Theorem Is Too Strong

### Proposition 15.1: Full-Law Dobrushin Is Mass-Gap-Strength Input

A cofinal uniform Dobrushin contraction for the full actual adaptive
Yang-Mills scalar law would imply exponential decay of finite-volume
conditional influence for local scalar observables.  Such a theorem is
mass-gap-strength information and should not be treated as a cheap source
lemma.

Proof.

Finite Dobrushin contraction gives uniqueness of the finite-volume Gibbs
specification and exponential decay of boundary influence in the graph metric
for the controlled observables.  Passing this uniformly along the cofinal
tower gives exponential clustering for the corresponding scalar record
observables.  This is exactly the kind of quantitative mixing information
that the mass-gap/confinement program is trying to prove, not a bookkeeping
fact already present in the finite labels. `square`

### Corollary 15.2: Why The Bridge Route Is Still Worth Trying

The bridge damping target is narrower than a full-law Dobrushin theorem.  It
asks only for damping of the true-bridge channel that contributes to the
minimal RPF predebit, after licensed local and endpoint-additive rows have
been removed.  Therefore it may be easier than proving full exponential
mixing, but it still requires genuine quantitative law information.

## 16. Part-II Analytic Verdict

### Theorem 16.1: Paper-30 Analytic Unblock Status

Paper 30 now proves three exact, usable analytic reductions:

1. `P30-PARENT-PUSH-DOM`;
2. `P30-PARENT-LOGOSC-DOM`;
3. `P30-FV-DLR-EXACT`.

It also proves the conditional positive route:
$$
\begin{gathered}
{1\over2}C_{min}^{br}\tau_{br}^{cof}
-\chi_{tilt}^{cof}>g_{br},\\
D(m_{HK}^{eff})<D_{\mathrm{crit}}(\kappa),\qquad
\kappa<B_*^{edge},\\
\mathrm{P23\text{-}RPF\text{-}MIN\text{-}KTAIL}(\kappa)
\end{gathered}
$$
imply adaptive Branch-A closure through bridge damping.

The present corpus does not prove the strict heat-kernel bridge exponent,
the signed heat-kernel cancellation theorem, or the common tail source in a
closing range.

Proof.

The exact reductions are Theorem 10.4, Lemma 10.5, and Lemma 11.3.  The
conditional positive route is Proposition 12.5 and Corollary 12.6 combined
with Theorem 4.2.  The current-corpus gaps are Propositions 13.2 and 14.3,
together with the tail gap already proved in Section 4. `square`

The new labels are
$$
\begin{gathered}
\mathrm{P30\text{-}PARENT\text{-}PUSH\text{-}DOM},\\
\mathrm{P30\text{-}PARENT\text{-}LOGOSC\text{-}DOM},\\
\mathrm{P30\text{-}FV\text{-}DLR\text{-}EXACT},\\
\mathrm{P30\text{-}TREE\text{-}HK\text{-}BRIDGEDAMP\text{-}GAP},\\
\mathrm{P30\text{-}TREE\text{-}HK\text{-}SIGNED\text{-}GAP}.
\end{gathered}
$$

### Corollary 16.2: Concrete Next Computation

The next attempt to unblock adaptive Branch A should compute or sharply
bound:
$$
        \tau_{br}^{cof},\qquad
        \chi_{tilt}^{cof},\qquad
        g_{br},\qquad
        \kappa.
$$

The decisive inequality is
$$
        {1\over2}C_{min}^{br}\tau_{br}^{cof}
        -
        \chi_{tilt}^{cof}
        >
        g_{br},
$$
followed by the Paper-23 bridge margin
$$
        D<D_{\mathrm{crit}}(\kappa).
$$
If this inequality fails for structural reasons, adaptive Branch A should be
de-prioritized in favor of the Paper-29 defect witness route or Branch C.

### Corollary 16.3: Updated Continuum YM Status

The continuum Yang-Mills confinement proof remains open.  Paper 30 now
contains a genuine analytic unblock plan rather than just a gap ledger:
parent-law domination, log-oscillation domination, and finite DLR exactness
are proved, while the actual unproved theorem is the heat-kernel/tree-gauge
bridge exponent after residual tilt and tail are paid.

## 17. Part III: Bridge Exponent Worksheet

Part II reduces the most economical positive continuation to the strict
bridge-exponent inequality
$$
        {1\over2}C_{min}^{br}\tau_{br}^{cof}
        -
        \chi_{tilt}^{cof}
        >
        g_{br}.
$$
This section freezes the worksheet needed to evaluate that inequality.
The point is deliberately narrow.  We do not introduce a new scalar law, a
new bridge process, or a new hidden heat-kernel comparison.  We only isolate
the finite and analytic quantities that the actual adaptive `SEL2` law has
to provide.

### Definition 17.1: Four Bridge-Exponent Accounts

For the actual same-law bridge family of Section 12, define four accounts:

1. the effective bridge heat-time slope
   $$
   \tau_{br}^{cof};
   $$
2. the least nontrivial bridge Casimir
   $$
   C_{min}^{br};
   $$
3. the exponential bridge route entropy
   $$
   g_{br};
   $$
4. the residual tilt slope
   $$
   \chi_{tilt}^{cof}.
   $$

The bridge route is positive only if the heat-kernel damping account beats
the entropy and residual-tilt accounts:
$$
        m_{HK}^{eff}
        :=
        {1\over2}C_{min}^{br}\tau_{br}^{cof}
        -
        \chi_{tilt}^{cof}
        >
        g_{br}.
$$

The tail account \(\kappa\) is separate.  It enters only after a positive
bridge exponent has produced a candidate damping value \(D(m_{HK}^{eff})\).

### Principle 17.2: What Counts As Same-Law Progress

The following inputs count as same-law progress:

1. a theorem about the finite-volume Yang-Mills DLR law before the scalar
   pushforward;
2. a deterministic pushforward inequality from that parent law to the
   scalar record law;
3. an exact tree-gauge heat-kernel identity for a parent sheet factor;
4. an exact residual Radon-Nikodym tilt bound for the real 4D measure;
5. a finite bridge-route census on the already printed adaptive carrier.

The following inputs do not count:

1. replacing the actual 4D conditional law by an independent sheet law;
2. assuming \(\mathcal R_j=1\) outside the two-dimensional axial-gauge
   model;
3. using an off-law heat-kernel tail as though it were the adaptive
   `SEL2` tail;
4. adding more labels without a bound on their actual values.

This is the Barandes-aligned rule for Part III: the law is the record; the
calculation may refine the record, but it may not smuggle in a different
one.

## 18. Effective Bridge Heat-Time Slope

Paper 20 gives the correct starting point.  Its real 4D convolution-defect
ledger writes the pushed `SEL2` law as an independent sheet heat-kernel
reference multiplied by an exact residual Radon-Nikodym factor
\(\mathcal R_j\).  The two-dimensional axial-gauge sheet has
\(\mathcal R_j=1\), but the real 4D law does not.  Therefore the bridge
heat-time account must be defined before the residual tilt is removed.

### Definition 18.1: Sheet Bridge Time

Let \(A\) be a live bridge object in the actual adaptive bridge carrier.
Let \(\Gamma_A^{sheet}(j)\) be the set of sheet plaquette factors that the
tree-gauge parent conditional uses to transmit the nontrivial representation
carried by \(A\).  Define
$$
        T_{br,j}^{sheet}(A)
        :=
        \sum_{b\in\Gamma_A^{sheet}(j)} \tau_{b,j},
$$
where \(\tau_{b,j}\) is the heat-kernel time of the corresponding sheet
factor in the Paper-20 normalization.

The cofinal bridge heat-time slope is
$$
        \tau_{br}^{cof}
        :=
        \liminf_{N\to\infty}
        \liminf_{j\to\infty}
        \inf_{A\in{\mathcal U}_{br,0}^{N,j}}
        {T_{br,j}^{sheet}(A)\over \ell(A)}.
$$
Here \(\ell(A)\) is the bridge length used in Paper 23's
`MIN-BRIDGEDAMP` route.

### Lemma 18.2: Heat-Time Slope Is The Only Honest Time Input

If the parent bridge channel carries representation \(\rho_A\) along
\(\Gamma_A^{sheet}(j)\), then the independent sheet heat-kernel reference
contributes at most
$$
        \exp\!\left(
        -{1\over2}C_2(\rho_A)T_{br,j}^{sheet}(A)
        \right)
$$
to the magnitude of that channel, in the Paper-20 heat-kernel normalization.

Proof.

For a compact-group heat kernel, the Peter-Weyl coefficient of the irreducible
channel \(\rho\) at time \(t\) is
\(\exp(-C_2(\rho)t/2)\) in the normalization used throughout the Paper-20
heat-kernel ledger.  Multiplying sheet factors adds heat times in the same
irreducible channel before the residual RN factor is applied.  Thus the
independent sheet reference contributes the displayed exponential. `square`

### Definition 18.3: Positive Time-Slope Source

The plain source label
$$
\boxed{\mathrm{P30\text{-}BRIDGE\text{-}TIME\text{-}SLOPE}(\tau_0)}
$$
means:
$$
        \tau_{br}^{cof}\ge \tau_0>0
$$
on the actual adaptive `SEL2` bridge family.

### Proposition 18.4: Current-Corpus Time-Slope Status

Papers 20--29 do not prove `P30-BRIDGE-TIME-SLOPE(tau_0)` for any explicit
\(\tau_0>0\) in the real 4D bridge family.

Proof.

Paper 20 proves the correct heat-kernel sheet ledger and the exact
two-dimensional axial-gauge identity.  It also explicitly separates the real
4D law from the independent sheet reference by the RN correction
\(\mathcal R_j\).  The standard sheet-time scaling controls the bulk sheet
time in the reference law, but it does not by itself prove that every live
true bridge in the adaptive `SEL2` carrier must pay a positive amount of
reference heat time per Paper-23 bridge length after the real 4D residual
tilt and cofinal selector are fixed.

Paper 23 defines the bridge length and proves that bridge damping plus tail
would close the scalar gate.  It does not print a positive lower bound for
\(T_{br,j}^{sheet}(A)/\ell(A)\) on the live bridge population.  Papers
24--29 keep returning to the same same-law value obstruction; none of them
prints the missing time-slope lower bound. `square`

Thus the current gap is
$$
\boxed{\mathrm{P30\text{-}BRIDGE\text{-}TIME\text{-}SLOPE\text{-}GAP}.}
$$

## 19. Least Bridge Casimir

The Casimir account is the least mysterious part of the worksheet.  It is
representation theory, provided the normalization is carried honestly.

### Definition 19.1: Live Bridge Representation Set

Let \({\mathcal R}_{br}^{live}(N,j)\) be the set of nontrivial irreducible
\(SU(N)\) representations that appear in the parent tree-gauge channel of a
live bridge object \(A\in{\mathcal U}_{br,0}^{N,j}\).  Define
$$
        C_{min}^{br}(N,j)
        :=
        \inf_{\rho\in{\mathcal R}_{br}^{live}(N,j)} C_2^{P20}(\rho)
$$
and
$$
        C_{min}^{br}
        :=
        \liminf_{N\to\infty}\liminf_{j\to\infty} C_{min}^{br}(N,j).
$$

### Lemma 19.2: Nontrivial Bridge Channels Have Fundamental Casimir Floor

Assume the Paper-20 heat-kernel normalization is
$$
        C_2^{P20}(\rho)=\lambda_{HK}\,C_2^{std}(\rho)
$$
with \(\lambda_{HK}>0\), where \(C_2^{std}(F_N)=(N^2-1)/(2N)\) for the
fundamental representation.  If every live bridge channel is nontrivial,
then
$$
        C_{min}^{br}(N,j)
        \ge
        \lambda_{HK}{N^2-1\over2N}.
$$
If the live bridge carrier is adjoint-only, then the stronger bound
$$
        C_{min}^{br}(N,j)\ge \lambda_{HK}N
$$
holds.

Proof.

For \(SU(N)\), the least positive quadratic Casimir among nontrivial
irreducible representations is attained by the fundamental and its dual in
the standard normalization.  The adjoint Casimir is \(N\).  Multiplication
by the fixed heat-kernel normalization factor \(\lambda_{HK}\) gives the
displayed bounds. `square`

### Definition 19.3: Casimir Normalization Source

The label
$$
\boxed{\mathrm{P30\text{-}CASIMIR\text{-}NORM}(\lambda_{HK})}
$$
means that Paper-20's heat-kernel convention has been fixed so that
$$
        C_2^{P20}=\lambda_{HK}C_2^{std}.
$$

This is not a conceptual gap.  It is a normalization pin.  Once the pin is
printed, the Casimir account is finite-dimensional representation theory.

## 20. Bridge Entropy

The entropy account is finite and combinatorial.  It cannot by itself prove
decay, but it can say exactly how much heat-kernel decay has to beat.

### Definition 20.1: Bridge Route Growth

Let
$$
        N_{br}^{N,j}(\ell)
        :=
        \#\{A\in{\mathcal U}_{br,0}^{N,j}:\ell(A)=\ell\}.
$$
Define
$$
        g_{br}
        :=
        \limsup_{N\to\infty}
        \limsup_{j\to\infty}
        \limsup_{\ell\to\infty}
        {1\over \ell}\log N_{br}^{N,j}(\ell).
$$

### Lemma 20.2: Finite Carrier Gives Exponential Entropy

Suppose the bridge carrier has at most \(M_{type}\) local bridge types and
each bridge extension has at most \(\Delta_{br}\) admissible next moves.
Then
$$
        N_{br}^{N,j}(\ell)
        \le
        C_{br}\,(M_{type}\Delta_{br})^\ell
$$
for a finite collar constant \(C_{br}\), and therefore
$$
        g_{br}\le \log(M_{type}\Delta_{br}).
$$

Proof.

Choose the initial collar root in at most \(C_{br}\) ways.  At each length
increment, choose a local bridge type and an admissible next move.  The
finite adaptive carrier forbids any additional continuous choice at the
label level.  This gives the displayed word-count bound. `square`

### Definition 20.3: Sharp Entropy Table

The label
$$
\boxed{\mathrm{P30\text{-}BRIDGE\text{-}ENTROPY\text{-}TABLE}
       (M_{type},\Delta_{br})}
$$
means that the actual Paper-23/Paper-26 bridge carrier has been printed
with its sharp local type count and sharp next-move count.

### Proposition 20.4: Entropy Is Not The Analytic Core

The current corpus proves finiteness of \(g_{br}\) at the level of a finite
carrier, but does not print the sharp pair
\((M_{type},\Delta_{br})\) needed for a numerical exponent test.

Proof.

Papers 23--26 print finite bridge and RPF carriers sufficient to state row
maps, label covers, and finite template obstructions.  The carrier finiteness
is enough for Lemma 20.2.  But the sharp local bridge type table and sharp
next-move count are not printed as a completed bridge-entropy table in the
current corpus.  This is a finite task, unlike the residual value theorem.
`square`

The finite-table gap is
$$
\boxed{\mathrm{P30\text{-}BRIDGE\text{-}ENTROPY\text{-}TABLE\text{-}GAP}.}
$$

## 21. Residual Tilt Split

The real 4D measure differs from the independent sheet heat-kernel reference
by a residual RN factor and by chart/normalizer effects.  This is the place
where the hard value theorem can re-enter.  We therefore split the tilt
account instead of hiding it.

### Definition 21.1: Tilt Decomposition

For a live bridge object \(A\), write the parent bridge conditional in the
form
$$
        d\mu_{br}^{act}
        =
        {1\over Z_{br}}\,
        e^{-H_{HK}^{sheet}}\,
        e^{-\Delta H_{RPF}}\,
        J_{tree}\,
        d\lambda_{tree}.
$$
Here \(H_{HK}^{sheet}\) is the independent sheet heat-kernel Hamiltonian,
\(\Delta H_{RPF}\) is the exact real-4D residual RN correction relative to
that reference, and \(J_{tree}\) is the tree-gauge/chart Jacobian factor on
the finite template.

Define
$$
        \chi_{tilt}^{cof}
        :=
        \chi_{RPF}^{cof}
        +
        \chi_{Jac}^{cof}
        +
        \chi_Z^{cof},
$$
where the three terms are the cofinal per-bridge-length log-oscillation
slopes of \(\Delta H_{RPF}\), \(J_{tree}\), and \(Z_{br}\), respectively.

### Lemma 21.2: Normalizers Do Not Create New Oscillation

Let two boundary conditions produce finite-template potentials \(V_0,V_1\)
on the same finite internal state space, and assume
$$
        \operatorname{osc}(V_1-V_0)\le \chi.
$$
Let
$$
        Z_i=\int e^{-V_i}\,d\lambda.
$$
Then
$$
        \operatorname{osc}\!\left[
        (V_1+\log Z_1)-(V_0+\log Z_0)
        \right]\le \chi.
$$
If an anchored representative is chosen so that
\(\inf(V_1-V_0)=0\), then additionally
$$
        0\le \log Z_0-\log Z_1\le \chi.
$$

Proof.

Let \(m=\inf(V_1-V_0)\) and \(M=\sup(V_1-V_0)\).  Then
$$
        e^{-M}Z_0\le Z_1\le e^{-m}Z_0.
$$
Taking logs gives
$$
        -M\le \log Z_1-\log Z_0\le -m,
$$
after anchoring.  More importantly, \(\log Z_1-\log Z_0\) is a constant on
the internal state space.  Adding a constant cannot change oscillation.
Therefore the normalized Hamiltonian difference has the same oscillation as
\(V_1-V_0\), bounded by \(M-m\le\chi\). `square`

### Corollary 21.3: Tilt Can Be Charged To Primitive Oscillation Sources

If
$$
        \chi_{pot}^{cof}
        :=
        \chi_{RPF}^{cof}+\chi_{Jac}^{cof},
$$
then
$$
        \chi_{tilt}^{cof}
        \le
        2\chi_{pot}^{cof}.
$$
More sharply, if the bridge amplitude is already written in doubly centered
form, or if only mixed oscillation is being charged, then
$$
        \chi_{tilt}^{cof}
        \le
        \chi_{pot}^{cof}.
$$

Proof.

For anchored uncentered absolute-density bookkeeping, Lemma 21.2 charges the
log normalizer by at most the same primitive potential oscillation, giving
the conservative factor \(2\).  For mixed oscillation, the normalizer is an
additive constant and does not create new oscillation.  In the doubly centered
bridge amplitude, additive row and column normalizers cancel by construction,
so only the primitive potential oscillation remains. `square`

### Proposition 21.4: Current-Corpus Tilt Status

The Jacobian/interior sheet part is structurally controlled by the Paper-20
axial-tree heat-kernel Schwinger-Dyson audits, up to boundary/collar and
large-field terms.  The residual RPF part
\(\chi_{RPF}^{cof}\) is not bounded in a closing range by Papers 20--29.

Proof.

Paper 20's rootwise heat-kernel Schwinger-Dyson and finite-template
axial-tree audits show that the interior heat-kernel generator identities
are compatible with the strict normalized `SEL2` row.  They do not set the
real 4D residual RN factor \(\mathcal R_j\) equal to one.  The same Paper-20
convolution-defect ledger explicitly names the residual 4D correction as the
unproved comparison input.  Papers 23--29 repeatedly show that the RPF/RN
MIXAMP values, Dobrushin rows, low-mode entries, and lower floors are not
printed by the finite label corpus.  Hence the residual tilt slope is the
same missing actual-law value information in another notation. `square`

The current tilt gap is
$$
\boxed{\mathrm{P30\text{-}TILT\text{-}RPF\text{-}GAP}.}
$$

## 22. Bridge-Exponent Closure Theorem

### Theorem 22.1: Four Accounts Close The Bridge-Damping Route

Assume the following same-law sources:

1. `P30-BRIDGE-TIME-SLOPE(tau_0)`;
2. `P30-CASIMIR-NORM(lambda_HK)` and the live bridge nontriviality floor
   $$
   C_{min}^{br}\ge C_0;
   $$
3. `P30-BRIDGE-ENTROPY-TABLE(M_type,Delta_br)` with
   $$
   g_0:=\log(M_{type}\Delta_{br});
   $$
4. a tilt bound
   $$
   \chi_{tilt}^{cof}\le \chi_0;
   $$
5. the strict exponent inequality
   $$
   {1\over2}C_0\tau_0-\chi_0>g_0.
   $$

Then there is \(m>0\) such that
$$
        d_A^{br}\le a_{\tau(A)}e^{-m\ell(A)}
$$
for the actual same-law bridge family, with
$$
        m\le {1\over2}C_0\tau_0-\chi_0-g_0.
$$
Consequently `P30-BRIDGEDAMP(D,kappa)` is sourced after the Paper-23 tail
budget is supplied in a range satisfying
$$
        D(m)<D_{\mathrm{crit}}(\kappa),
        \qquad
        \kappa<B_*^{edge}.
$$

Proof.

The heat-kernel sheet factor supplies the channel decay
$$
        \exp[-C_0 T_{br,j}^{sheet}(A)/2].
$$
The time-slope source gives
$$
        T_{br,j}^{sheet}(A)\ge (\tau_0-o(1))\ell(A)
$$
cofinally.  The tilt bound costs at most
$$
        \exp[(\chi_0+o(1))\ell(A)].
$$
The entropy table costs at most
$$
        \exp[(g_0+o(1))\ell(A)]
$$
when summing all bridge objects of length \(\ell(A)\).  The strict inequality
leaves a positive exponent
$$
        {1\over2}C_0\tau_0-\chi_0-g_0>0.
$$
This is precisely the Paper-23 bridge-damping hypothesis, and the final
tail and margin assumptions are the previously proved Paper-23 scalar
closure gate. `square`

### Corollary 22.2: What Would Actually Unblock Branch A

Adaptive Branch A is unblocked by the following concrete package:
$$
\boxed{
\begin{gathered}
\mathrm{P30\text{-}BRIDGE\text{-}TIME\text{-}SLOPE}(\tau_0),\\
\mathrm{P30\text{-}TILT\text{-}UPPER}(\chi_0),\\
\mathrm{P30\text{-}BRIDGE\text{-}ENTROPY\text{-}TABLE}(M_{type},\Delta_{br}),\\
{1\over2}C_0\tau_0-\chi_0>\log(M_{type}\Delta_{br}),\\
\mathrm{P23\text{-}RPF\text{-}MIN\text{-}KTAIL}(\kappa)
\ \text{with}\ 
D<D_{\mathrm{crit}}(\kappa).
\end{gathered}}
$$

The new essential analytic input is not another finite label cover.  It is
actual same-law value information: a positive bridge heat-time slope and a
residual tilt bound on the real 4D adaptive law.

## 23. Part-III Verdict

### Theorem 23.1: Bridge-Exponent Worksheet Status

Part III proves the following:

1. the heat-kernel part of bridge damping is controlled by the single
   cofinal slope \(\tau_{br}^{cof}\);
2. the Casimir account is a representation-theoretic floor once the
   Paper-20 normalization is pinned;
3. the bridge entropy account is finite and reduces to a sharp finite
   carrier table;
4. normalizer tilt is controlled by potential oscillation;
5. the full bridge-damping route closes if the four accounts satisfy the
   strict exponent inequality.

It also proves that the present corpus does not yet supply:
$$
\begin{gathered}
\mathrm{P30\text{-}BRIDGE\text{-}TIME\text{-}SLOPE}(\tau_0),\\
\mathrm{P30\text{-}TILT\text{-}UPPER}(\chi_0),\\
\mathrm{P30\text{-}BRIDGE\text{-}ENTROPY\text{-}TABLE}
(M_{type},\Delta_{br})
\end{gathered}
$$
in a numerical closing range.

Proof.

The positive reductions are Lemma 18.2, Lemma 19.2, Lemma 20.2, Lemma 21.2,
Corollary 21.3, and Theorem 22.1.  The current-corpus non-sourcing results
are Proposition 18.4, Proposition 20.4, and Proposition 21.4. `square`

The active Paper-30 front is therefore:
$$
\boxed{
\mathrm{P30\text{-}BRIDGE\text{-}TIME\text{-}SLOPE\text{-}GAP}
\quad+\quad
\mathrm{P30\text{-}TILT\text{-}RPF\text{-}GAP}
\quad+\quad
\mathrm{P30\text{-}BRIDGE\text{-}ENTROPY\text{-}TABLE\text{-}GAP}.
}
$$

The first two are analytic same-law value problems.  The third is a finite
table problem.  The finite table is worth printing because it tells us the
exact entropy price, but it cannot by itself unblock confinement if the
bridge time slope or residual tilt remains unknown.

## 24. Finite Account Pass: Casimir And Coarse Entropy

This section executes the finite part of the Part-III worksheet as far as the
existing corpus permits.  It closes the heat-kernel Casimir normalization and
prints a conservative over-refined bridge entropy bound.  The result is
useful, but it is not a hidden confinement proof: the entropy bound is far too
coarse to be expected to beat the analytic residual tilt without a genuinely
new same-law value theorem.

### Lemma 24.1: Paper-20 Heat-Kernel Normalization Gives \(\lambda_{HK}=1\)

In the Paper-20 standard heat-kernel normalization,
$$
        H_T(U)
        =
        \sum_{\lambda\in\widehat{SU(N)}}
        d_\lambda e^{-T C_2(\lambda)/2}\chi_\lambda(U).
$$
Therefore Paper 30's normalization pin is
$$
\boxed{\mathrm{P30\text{-}CASIMIR\text{-}NORM}(1)}.
$$

Proof.

Paper 20 writes the heat-kernel coefficient of the irreducible channel
\(\lambda\) as \(e^{-T C_2(\lambda)/2}\) after dimension-normalization.  That
is exactly the convention used in Lemma 18.2 and Lemma 19.2.  Hence
\(C_2^{P20}=C_2^{std}\) in the standard heat-kernel convention carried here,
so \(\lambda_{HK}=1\). `square`

### Lemma 24.2: True Bridges Pay A Nontrivial Casimir

Every true bridge charged by
\({\mathcal U}_{br,0}^{N,j}(x,y)\) carries at least one nontrivial
\(SU(N)\) channel across the endpoint pair.  Consequently
$$
        C_{min}^{br}(N,j)
        \ge
        {N^2-1\over2N}.
$$
If the selected bridge carrier is proved adjoint-only, then
$$
        C_{min}^{br}(N,j)\ge N.
$$

Proof.

By Paper 23 Lemma 49.3, true bridges are exactly the rows with nonzero mixed
endpoint oscillation \(\delta_\square(A;x,y)>0\).  A purely trivial
representation channel is constant in the endpoint holonomy it crosses and
therefore has zero mixed endpoint oscillation.  Thus every true bridge has a
nontrivial channel.  Lemma 19.2 and Lemma 24.1 give the fundamental Casimir
floor, with the adjoint improvement when the carrier is adjoint-only.
`square`

### Definition 24.3: Coarse Over-Refined Bridge Entropy

Use the complete over-refined Paper-21/Paper-23 carrier
\({\mathfrak T}_{99}^{edge}\).  Paper 23's canonical entropy worksheet imports
Paper 21 Definition 102.3--102.5 and Lemma 111.2 and gives the conservative
same-record vertex bound
$$
        v_{RPF}^{can}\le v_{99}^{+},
        \qquad
        \log v_{99}^{+}\le157.39.
$$
It then proves the coarse canonical support entropy
$$
        L_{can}^{N,j}(n)\le 2^{v_{99}^{+}n}.
$$

For the bridge route, take the printed bridge length \(\ell(A)\) to be the
connected carrier-size length of the true bridge support.  Define
$$
        g_{br}^{99}
        :=
        v_{99}^{+}\log 2.
$$
Equivalently,
$$
        \log g_{br}^{99}\le157.02.
$$

### Proposition 24.4: Coarse Entropy Certificate

The current corpus proves the coarse bridge entropy bound
$$
\boxed{
        g_{br}\le g_{br}^{99}
        :=
        v_{99}^{+}\log2,
        \qquad
        \log g_{br}^{99}\le157.02.
}
$$

Proof.

Paper 23 Sections 49--50 identify the true-bridge rows with the active mixed
rows and prove that the rowwise true-bridge table is finite.  Paper 23
Section 24 imports the complete over-refined Paper-21 carrier and proves that
a connected support of carrier-size \(n\) has at most
\(2^{v_{99}^{+}n}\) canonical support choices.  Since true bridges are a
subfamily of those canonical supports, the same bound applies to the number
of true bridges of carrier-size length \(\ell=n\).  Taking
\(\ell^{-1}\log\) and then the cofinal limsup gives
\(g_{br}\le v_{99}^{+}\log2\).  The numerical logarithmic bound is the Paper
23 bound \(\log h_{can}^{coarse}\le157.02\). `square`

### Corollary 24.5: The Coarse Entropy Bound Is Finite But Not A Closing
Certificate

Using only the over-refined carrier, the bridge exponent test becomes
$$
        {1\over2}C_0\tau_0-\chi_0
        >
        g_{br}^{99},
        \qquad
        \log g_{br}^{99}\le157.02.
$$
This is a valid same-law finite reduction, but it is not a plausible closing
certificate unless a new analytic theorem supplies an enormous positive
margin or a much sharper physical selector reduces the entropy.

Proof.

Proposition 24.4 supplies a legitimate finite upper bound on \(g_{br}\).  But
the bound is the Paper-21/Paper-23 over-refined carrier entropy, not the
entropy of a physically sharp bridge selector.  Its logarithm is already
about \(157\), so the entropy itself is astronomically large.  No current
Paper-20--29 source theorem supplies a bridge heat-time slope and residual
tilt margin of that size.  Therefore the coarse finite certificate is useful
as an upper-bound ledger, not as a closing estimate. `square`

### Theorem 24.6: Finite Account Status After The Pass

After this finite pass:

1. the Casimir normalization is closed:
   $$
   \mathrm{P30\text{-}CASIMIR\text{-}NORM}(1);
   $$
2. true bridges have at least the fundamental Casimir floor:
   $$
   C_{min}^{br}(N,j)\ge {N^2-1\over2N};
   $$
3. the coarse over-refined entropy certificate is closed:
   $$
   g_{br}\le g_{br}^{99},
   \qquad
   \log g_{br}^{99}\le157.02;
   $$
4. a sharp useful bridge entropy table remains open:
   $$
   \mathrm{P30\text{-}BRIDGE\text{-}ENTROPY\text{-}SHARP\text{-}GAP};
   $$
5. the real analytic blockers remain:
   $$
   \mathrm{P30\text{-}BRIDGE\text{-}TIME\text{-}SLOPE\text{-}GAP}
   \quad+\quad
   \mathrm{P30\text{-}TILT\text{-}RPF\text{-}GAP}.
   $$

Proof.

Items 1 and 2 are Lemmas 24.1 and 24.2.  Item 3 is Proposition 24.4.  Item 4
is Corollary 24.5: the over-refined entropy is valid but not sharp enough to
serve as a serious closing certificate.  Item 5 is unchanged by finite
entropy bookkeeping; it is exactly Proposition 18.4 plus Proposition 21.4.
`square`

### Corollary 24.7: What Paper 30 Should Do Next

Paper 30 should not spend more effort on larger finite carriers.  The finite
account pass already used the complete over-refined carrier and found the
coarse entropy too expensive.  The next meaningful theorem must be one of:

1. a physical bridge selector/automaton proving
   `P30-BRIDGE-ENTROPY-SHARP` with a much smaller \(g_{br}\);
2. a positive bridge time-slope theorem strong enough to survive the entropy
   actually paid;
3. a residual RPF tilt theorem strong enough to leave positive exponent;
4. a lower-floor theorem falsifying adaptive Branch A;
5. an exit from adaptive Branch A.

The most conservative next attack is step 2 or 3.  A sharper entropy table is
helpful only if it is paired with one of those analytic same-law value
theorems.

## 25. Time-Slope Unit Audit

The finite pass used a carrier-size bridge length because that is the length
for which the over-refined entropy bound is available.  This section checks
whether the heat-time slope can be positive in that same unit.  The answer is
negative unless the bridge length is cofinally bounded or the length unit is
changed and the entropy is recomputed in the new unit.

This is an important obstruction.  It means the heat-kernel bridge route
cannot mix a carrier-size entropy count with a bounded total sheet heat time
and then expect a positive damping rate per carrier step.

### Lemma 25.1: Total Sheet Time Is Cofinally Bounded

On the standard `SEL2` AF-area selector of Paper 20, the independent sheet
reference has a finite block-time window
$$
        0<T_-^{SEL2}
        \le
        T_j^{SEL2,conv}
        \le
        T_+^{SEL2}
        <\infty
$$
on a cofinal tail.

Proof.

Paper 20's standard sheet-time scaling gives
\(n_j=S_j+B_j^{sheet}\), \(S_j=L_j^2\), \(B_j^{sheet}=O(L_j)\), and
\(\tau_{b,j}/t_{i(j)}\to1\) uniformly over the sheet list.  On the AF-area
selector, \(S_jt_{i(j)}\) remains in the finite positive window fixed by the
selected area parameter, while \(B_j^{sheet}t_{i(j)}\to0\).  Paper 20 records
this as the finite block-time window for \(T_j^{SEL2,conv}\). `square`

### Lemma 25.2: Carrier-Size Length Forces Zero Time Slope

Suppose the bridge length \(\ell_{car}(A)\) is a carrier-size length: it
counts connected carrier steps, plaquette slots, or over-refined support
vertices, so that an unbounded bridge family contains objects
\(A_k\) with \(\ell_{car}(A_k)\to\infty\).  Suppose also that
\(\Gamma_A^{sheet}(j)\subseteq\mathscr S_j^{SEL2}\), so that
$$
        0\le T_{br,j}^{sheet}(A)\le T_j^{SEL2,conv}.
$$
Then
$$
        \liminf_{N\to\infty}
        \liminf_{j\to\infty}
        \inf_{A}
        {T_{br,j}^{sheet}(A)\over \ell_{car}(A)}
        =
        0
$$
whenever the true-bridge family has unbounded carrier-size length cofinally.

Proof.

By Lemma 25.1, \(T_{br,j}^{sheet}(A)\le T_+^{SEL2}\) on a cofinal tail.
For any \(L\), choose a live true bridge with \(\ell_{car}(A)\ge L\).  Then
$$
        {T_{br,j}^{sheet}(A)\over \ell_{car}(A)}
        \le
        {T_+^{SEL2}\over L}.
$$
Taking the infimum over bridges and then \(L\to\infty\) gives zero. `square`

### Corollary 25.3: The Coarse Entropy Unit Cannot Carry Positive
Heat-Time Slope

The coarse entropy certificate of Proposition 24.4 uses carrier-size support
length.  If true bridges occur with unbounded carrier-size length, then
$$
\boxed{
\tau_{br}^{cof}(\ell_{car})=0.
}
$$
Consequently the strict exponent inequality
$$
        {1\over2}C_0\tau_{br}^{cof}(\ell_{car})-\chi_0
        >
        g_{br}
$$
cannot hold with any nonnegative residual tilt \(\chi_0\).

Proof.

Apply Lemma 25.2.  The left-hand side is at most \(-\chi_0\), while
\(g_{br}\ge0\). `square`

### Definition 25.4: Time-Compatible Bridge Length

A bridge length \(\ell_{time}(A)\) is time-compatible if there are constants
\(c_-,c_+>0\) such that cofinally
$$
        c_-\ell_{time}(A)
        \le
        T_{br,j}^{sheet}(A)
        \le
        c_+\ell_{time}(A)
$$
for every live true bridge \(A\).

The natural heat-time choice is
$$
        \ell_{time}(A):=T_{br,j}^{sheet}(A).
$$
For that choice the time slope is tautologically \(1\), but the bridge
entropy must be recomputed per unit \(\ell_{time}\), not per carrier-size
step.

### Definition 25.5: Time-Compatible Entropy Source

The source
$$
\boxed{\mathrm{P30\text{-}BRIDGE\text{-}TIMEENT}(g_{time})}
$$
means that the actual true-bridge family satisfies
$$
        \limsup
        {1\over \ell_{time}}
        \log
        \#\{A:\ell_{time}(A)\le \ell_{time}\}
        \le
        g_{time}
$$
in a cofinal same-law schedule, for a time-compatible bridge length.

This source is not supplied by the over-refined carrier entropy table.  The
over-refined table counts carrier support choices; it does not control how
many carrier choices fit into a small heat-time budget.

### Proposition 25.6: Time-Entropy Compatibility Is A New Source

The current corpus does not prove `P30-BRIDGE-TIMEENT(g_time)` in a useful
range.

Proof.

Paper 23 proves finite carrier entropy in carrier-size units.  Paper 20
proves that the total sheet heat time of an entire `SEL2` block remains
finite.  Neither statement bounds the number of bridge carrier choices per
unit accumulated heat time.  Indeed, because the microscopic heat time per
sheet factor is of order \(t_{i(j)}\to0\), many carrier steps can fit into a
bounded total heat-time interval unless a new selector, geometric
self-avoidance theorem, or physical bridge automaton forbids them.  No such
time-compatible entropy theorem is printed in Papers 20--29. `square`

Thus the new gap is
$$
\boxed{\mathrm{P30\text{-}BRIDGE\text{-}TIMEENT\text{-}GAP}.}
$$

### Theorem 25.7: Time-Slope Verdict

The bridge heat-kernel route has the following exact status.

1. With carrier-size length, the coarse entropy table is available, but the
   heat-time slope is zero if bridge lengths are unbounded:
   $$
   \tau_{br}^{cof}(\ell_{car})=0.
   $$
2. With heat-time-compatible length, the time slope can be positive, even
   tautologically positive for \(\ell_{time}=T_{br}^{sheet}\), but the
   entropy account must be rebuilt as `P30-BRIDGE-TIMEENT(g_time)`.
3. Therefore the actual positive heat-kernel bridge route now requires the
   compatible pair
   $$
   \mathrm{P30\text{-}BRIDGE\text{-}TIMEENT}(g_{time})
   \quad+\quad
   \mathrm{P30\text{-}TILT\text{-}UPPER}(\chi_0)
   $$
   together with
   $$
   {1\over2}C_0-\chi_0>g_{time}
   $$
   in the natural choice \(\ell_{time}=T_{br}^{sheet}\).

Proof.

Item 1 is Corollary 25.3.  Item 2 is Definition 25.4 together with the
requirement that entropy be measured in the same length variable as damping.
Item 3 is Theorem 22.1 rewritten with \(\tau_0=1\) in the heat-time length
unit. `square`

### Corollary 25.8: Honest Next Target After The Time Audit

The previous target
`P30-BRIDGE-TIME-SLOPE(tau_0)` was too coarse: by itself it does not specify
which length unit pays entropy.  The corrected target is the compatible
pair
$$
\boxed{
\mathrm{P30\text{-}BRIDGE\text{-}TIMEENT}(g_{time})
\quad+\quad
\mathrm{P30\text{-}TILT\text{-}UPPER}(\chi_0).
}
$$

If this pair cannot be proved without a full quantitative theorem for the
actual 4D Yang-Mills conditional law, then the prior external review is
right: the bridge route has faithfully re-encoded the hard analytic core
rather than bypassed it.

## 26. Casimir-Time Salvage Audit

Section 25 showed that carrier-size length has zero heat-time slope when
true bridge lengths are unbounded.  A possible loophole remains: the actual
heat-kernel damping is not \(T/2\), but \(C_2(\rho)T/2\).  This section asks
whether the Casimir factor can rescue carrier-size damping.

The answer is precise.  For any fixed declared \(SU(N_0)\) row, including the
fixed \(N_0=4096\) row used earlier in the Branch-A ledger, Casimir does not
rescue carrier-size damping in the continuum limit.  A rescue would require
a joint large-\(N\)-with-cutoff declaration in which \(N(j)\) grows on the
order of the inverse microscopic heat time.  That is a different target from
fixed-\(N\) continuum Yang-Mills.

### Definition 26.1: Carrier Casimir-Time Slope

For carrier-size length \(\ell_{car}\), define the carrier Casimir-time
slope
$$
        \mu_{car}^{cof}
        :=
        \liminf
        \inf_A
        {C_2(\rho_A)T_{br,j}^{sheet}(A)\over \ell_{car}(A)},
$$
where \(\rho_A\) is the least nontrivial representation channel carried by
the bridge \(A\), and the liminf is taken in the declared cofinal schedule.

If \(\mu_{car}^{cof}>0\), then the carrier-size damping exponent could be
rewritten as
$$
        \exp\!\left[-{1\over2}\mu_{car}^{cof}\ell_{car}(A)\right].
$$

### Lemma 26.2: Fixed \(N\) Gives Zero Carrier Casimir-Time Slope

Fix a declared gauge group \(SU(N_0)\).  If the true-bridge family has
unbounded carrier-size length cofinally, then
$$
        \mu_{car}^{cof}(N_0)=0.
$$

Proof.

For fixed \(N_0\), the least live Casimir is bounded above by a finite
constant depending only on \(N_0\); for the fundamental floor,
\(C_2(F_{N_0})=(N_0^2-1)/(2N_0)\).  Lemma 25.1 gives
\(T_{br,j}^{sheet}(A)\le T_+^{SEL2}\) cofinally.  Therefore, for bridges with
\(\ell_{car}(A)\ge L\),
$$
        {C_2(\rho_A)T_{br,j}^{sheet}(A)\over \ell_{car}(A)}
        \le
        {C_{max}(N_0)T_+^{SEL2}\over L}.
$$
Letting \(L\to\infty\) gives zero. `square`

### Corollary 26.3: Fixed \(N=4096\) Does Not Rescue Carrier-Length
Damping

The fixed \(N=4096\) row has a large Casimir,
$$
        C_2(F_{4096})={4096^2-1\over2\cdot4096},
$$
but it is still fixed before the continuum limit.  Hence
$$
        \mu_{car}^{cof}(4096)=0
$$
whenever carrier-size bridge lengths are unbounded.

Proof.

Apply Lemma 26.2 with \(N_0=4096\).  The number \(C_2(F_{4096})\) is large
but finite; it cannot compensate an unbounded carrier length in the
continuum row. `square`

### Lemma 26.4: Microscopic Per-Step Salvage Requires Joint Large \(N(j)\)

Suppose a live bridge uses \(\ell_{car}(A)\) sheet steps and each used sheet
step has time comparable to the microscopic heat time \(t_{i(j)}\).  On the
standard `SEL2` selector,
$$
        t_{i(j)}\asymp g_{i(j)}^2=H_j^{-1}.
$$
For the fundamental channel,
$$
        C_2(F_N)={N^2-1\over2N}\sim {N\over2}.
$$
Therefore a positive per-carrier-step Casimir-time slope requires
$$
        \liminf_j {N(j)\over H_j}>0
$$
on a joint \(N(j)\)-with-cutoff schedule.

Proof.

The per-step heat-kernel exponent is
\(C_2(F_{N(j)})t_{i(j)}/2\).  Since \(t_{i(j)}\asymp H_j^{-1}\) and
\(C_2(F_N)\sim N/2\), this quantity is bounded away from zero only if
\(N(j)/H_j\) is bounded below by a positive constant. `square`

### Corollary 26.5: Joint Large \(N(j)\) Is Not A Fixed-Gauge-Group
Continuum Theorem

A schedule with \(N(j)\asymp H_j\) may define a legitimate large-\(N\)
diagnostic branch, but it does not prove confinement for a fixed gauge group
\(SU(N_0)\).  It also changes the representation dimension, scalar record
range, entropy, and residual RN tilt accounts simultaneously.

Proof.

Fixed-gauge-group Yang-Mills keeps \(N_0\) fixed while the continuum
refinement \(j\to\infty\) is taken.  Lemma 26.4 instead ties the gauge rank
to the cutoff.  That changes the target law itself, so any positive result
must be declared as a large-\(N(j)\) cutoff-coupled theorem and cannot be
reported as a fixed-\(N_0\) confinement proof. `square`

### Theorem 26.6: Casimir-Time Salvage Verdict

The Casimir-time audit has the following status.

1. Fixed \(SU(N_0)\) rows do not salvage carrier-size bridge damping:
   $$
   \mu_{car}^{cof}(N_0)=0
   $$
   whenever true-bridge carrier lengths are unbounded.
2. The declared fixed \(N=4096\) row does not evade this verdict.
3. A positive carrier-step Casimir-time exponent requires a joint
   \(N(j)\)-with-cutoff branch satisfying
   $$
   \liminf_j {N(j)\over H_j}>0.
   $$
4. Such a branch is not the fixed-gauge-group continuum Yang-Mills target
   unless it is explicitly declared as a different large-\(N\) diagnostic.

Proof.

Items 1 and 2 are Lemma 26.2 and Corollary 26.3.  Item 3 is Lemma 26.4.
Item 4 is Corollary 26.5. `square`

The fixed-\(N\) heat-kernel carrier-damping route is therefore structurally
closed unless one of the following happens:

1. true-bridge carrier lengths are proved cofinally bounded, reducing the
   problem to a finite same-law amplitude table rather than exponential
   damping;
2. a time-compatible entropy theorem `P30-BRIDGE-TIMEENT(g_time)` is proved;
3. a residual signed/tilt theorem closes the bridge route without carrier
   heat-kernel damping;
4. a lower-floor theorem falsifies adaptive Branch A;
5. the program explicitly changes target to a joint large-\(N(j)\) branch.

### Corollary 26.7: Positive Continuation After Casimir-Time

For fixed declared \(SU(N_0)\), including \(N_0=4096\), the next positive
Paper-30 theorem should not be another carrier-length heat-kernel estimate.
It should be one of:
$$
\boxed{
\mathrm{P30\text{-}BRIDGE\text{-}TIMEENT}(g_{time})
\quad+\quad
\mathrm{P30\text{-}TILT\text{-}UPPER}(\chi_0)
}
$$
in a time-compatible unit, or a direct same-law signed/bridge value theorem,
or a lower-floor theorem.

This is the honest endpoint of the heat-kernel bridge salvage attempt.

## 27. Residual Tilt Localization Audit

The remaining positive fixed-\(N\) route asks whether the residual
Radon-Nikodym tilt can be localized or made small on the true-bridge mixed
part.  This section performs the honest split.  The conclusion is again
sharp: the current corpus cancels local and endpoint-additive pieces, and it
proves rootwise heat-kernel Schwinger-Dyson cancellations for interior
second-order tangents, but it does not bound the doubly centered mixed
oscillation of the real four-dimensional residual RN correction.

### Definition 27.1: Residual Tilt Pieces After Anchoring

Work in the same finite parent tree-gauge chart as Sections 11 and 21.  After
endpoint anchoring and subtracting one-site/constant terms, decompose the
bridge residual tilt symbolically as
$$
        \Delta H_{RPF}^{anc}
        =
        \Delta H_{time}
        +
        \Delta H_{norm}
        +
        \Delta H_{ea}
        +
        \Delta H_{HKSD}
        +
        \Delta H_{4Dmix}.
$$
The terms mean:

1. \(\Delta H_{time}\): heat-time tangent terms absorbed into
   \(T_j^{SEL2,conv}\);
2. \(\Delta H_{norm}\): scalar normalization and row/column normalizer terms;
3. \(\Delta H_{ea}\): endpoint-blind or endpoint-additive local/collar terms;
4. \(\Delta H_{HKSD}\): interior root second-order heat-kernel/Yang-Mills
   Taylor terms covered by the Paper-20 rootwise HKSD audit;
5. \(\Delta H_{4Dmix}\): the remaining real 4D off-sheet/Bianchi/RN mixed
   correction, equivalently the doubly centered part of the residual factor
   \(\mathcal R_j\) not absorbed by the previous four ledgers.

This is a ledger decomposition, not a claim that the real 4D law factorizes.
The last term is exactly where factorization can fail.

### Lemma 27.2: The First Three Pieces Do Not Charge The Doubly Centered
Bridge Tilt

After deterministic anchoring:
$$
        (\Delta H_{time}
        +
        \Delta H_{norm}
        +
        \Delta H_{ea})^{dc}=0
$$
in the true-bridge mixed source, except for constants already charged to the
heat-time account or to finite one-site normalizers.

Proof.

The heat-time tangent is already part of the heat-kernel account
\(T_{br}^{sheet}\), not a residual mixed tilt.  Scalar normalization and
finite row/column normalizers are additive in the endpoint variables and
therefore disappear under double centering by Lemma 21.2 and Paper 23's
anchored mixed calculus.  Endpoint-blind and endpoint-additive rows have zero
mixed finite difference by Paper 23 Lemma 49.2, and Section 51 identifies the
remaining doubly centered minimal marginal with the signed true-bridge sum.
`square`

### Lemma 27.3: Paper-20 HKSD Cancels Interior Tangents, Not The Full
Residual RN Tilt

Paper 20's `P20-SEL2-HKSD-TPL` and rootwise `GENMATCH/FOC` audits imply that
the interior heat-kernel/Yang-Mills second-order tangent terms cancel in the
strict normalized `SEL2` coefficient ledger.  They do not imply
$$
        (\Delta H_{4Dmix})^{dc}=0
$$
or a useful cofinal bound on its mixed oscillation.

Proof.

Paper 20's HKSD audit is a finite root-template statement.  It separates
heat-time tangent and scalar normalization terms, classifies the remaining
interior second-order root labels, and uses compact-group integration by
parts to cancel the interior divergence contribution.  Paper 20 also states
separately that the real 4D convolution defect is the RN factor
\(\mathcal R_j\), and that \(\mathcal R_j=1\) is exact for the two-dimensional
axial sheet but is not automatic in the real four-dimensional block/collar
law.  Thus HKSD controls the local tangent expansion; it does not prove that
the off-sheet/Bianchi residual factor has zero doubly centered endpoint
oscillation. `square`

### Definition 27.4: Bridge-Local Tilt Source

Fix the time-compatible length used in the bridge exponent.  The source
$$
\boxed{
\mathrm{P30\text{-}TILT\text{-}LOCAL\text{-}BRIDGE}(\chi_0)
}
$$
means that cofinally
$$
        \operatorname*{ess\,sup}_{x,y,\zeta}
        \operatorname{osc}_{u,v}
        \left[
        (\Delta H_{4Dmix}^{anc})^{dc}(u,v;\zeta)
        \right]
        \le
        (\chi_0+o(1))\,\ell_{time}.
$$

If the residual mixed term is actually bounded-collar-only, then the same
definition holds with \(\chi_0=0\) whenever the relevant bridge length tends
to infinity.  If the bridge length is bounded, the problem is no longer an
exponential damping problem; it is a finite same-law signed/amplitude table.

### Lemma 27.5: Bridge-Local Tilt Sources `P30-TILT-UPPER`

If `P30-TILT-LOCAL-BRIDGE(chi_0)` holds, then
`P30-TILT-UPPER(chi_0)` holds for the doubly centered bridge exponent
worksheet.

Proof.

By Lemma 27.2, time tangent, scalar normalization, and endpoint-additive
pieces do not charge the doubly centered residual bridge tilt.  By Lemma
27.3, the HKSD-controlled interior tangent is already removed from the
residual account.  The only remaining doubly centered residual contribution
is \(\Delta H_{4Dmix}^{dc}\).  Definition 27.4 bounds exactly its
cofinal oscillation per bridge length. `square`

### Proposition 27.6: Current-Corpus Tilt-Localization Verdict

The current corpus does not prove
`P30-TILT-LOCAL-BRIDGE(chi_0)` in any closing range.

Proof.

The positive cancellations available in the corpus are real but limited:
Paper 23 removes endpoint-additive and endpoint-blind rows from the doubly
centered mixed source, and Paper 20 removes heat-time, normalization, and
rootwise interior tangent terms from the strict coefficient ledger.  What
remains is the real 4D residual RN factor \(\mathcal R_j\), namely the
off-sheet/Bianchi/nonproduct correction measured in Paper 20 by
`P20-SEL2-4DCONV-CLOSE`.  Paper 20 explicitly states that the useful
four-dimensional convolution close estimate is not proved by the current
imports.  Papers 26--29 likewise show that the actual residual density
values, mixed amplitudes, Dobrushin rows, low-mode entries, and lower floors
are not populated by finite labels.  Therefore the bridge-local residual
tilt source remains a genuinely new same-law value theorem. `square`

Thus the current gap is
$$
\boxed{\mathrm{P30\text{-}TILT\text{-}LOCAL\text{-}BRIDGE\text{-}GAP}.}
$$

### Corollary 27.7: Residual Tilt Has Been Reduced To One Primitive Mixed
Object

For fixed declared \(SU(N_0)\), the positive heat-kernel bridge route now
requires
$$
\boxed{
\mathrm{P30\text{-}BRIDGE\text{-}TIMEENT}(g_{time})
\quad+\quad
\mathrm{P30\text{-}TILT\text{-}LOCAL\text{-}BRIDGE}(\chi_0)
}
$$
and the strict margin
$$
        {1\over2}C_0-\chi_0>g_{time}.
$$

All other local, endpoint-additive, normalizer, and interior tangent ledgers
have already been removed or assigned.  The only remaining positive theorem
inside this route is actual same-law control of the real 4D doubly centered
mixed residual RN tilt, together with a compatible bridge entropy theorem.

### Theorem 27.8: Fixed-\(N\) Heat-Kernel Bridge Route Status

After the entropy, time-slope, Casimir-time, and residual-tilt audits, the
fixed-\(N\) heat-kernel bridge route has the following status:

1. carrier-size heat-kernel damping is structurally blocked for unbounded
   bridge lengths;
2. fixed \(N\), including fixed \(N=4096\), cannot be rescued by the Casimir
   factor in carrier-size units;
3. time-compatible damping remains logically possible, but only if
   `P30-BRIDGE-TIMEENT(g_time)` is proved;
4. residual tilt is reduced to the primitive source
   `P30-TILT-LOCAL-BRIDGE(chi_0)`;
5. the current corpus does not prove either primitive source.

Proof.

Items 1 and 2 are Theorems 25.7 and 26.6.  Item 3 is Definition 25.5 and
Proposition 25.6.  Item 4 is Lemma 27.5.  Item 5 is Proposition 25.6 and
Proposition 27.6. `square`

This is a useful positive reduction, but it is not a proof of confinement.
It says exactly what would now have to be proved without changing the law.

## 28. Positive Theorem Search And The No-Free-Locality Verdict

The previous section leaves a narrow opening.  The positive theorem, if it
exists inside Paper 30, cannot be another finite-label theorem.  It must be a
same-law quantitative statement about the actual four-dimensional residual
Radon-Nikodym factor on the true bridge rows.  This section records the
smallest theorem that would unblock the fixed-\(N\) bridge route, and proves
that the current corpus does not imply it by locality alone.

### Definition 28.1: Mixed RN Screening

For fixed declared \(SU(N_0)\), let
$$
        C_0={N_0^2-1\over 2N_0}
$$
in the Paper-20 heat-kernel normalization.  The source
$$
\boxed{
\mathrm{P30\text{-}MIXED\text{-}RN\text{-}SCREEN}(g_{time},\chi_0)
}
$$
means the following two same-law assertions hold cofinally on the actual
adaptive `SEL2` pushed-forward scalar law:

1. **Time-compatible bridge entropy.**  If
   \(N_{br}^{time}(\ell)\) denotes the number of true bridge atoms of
   time-compatible length \(\ell_{time}=\ell\), then
   $$
        \limsup_{\ell\to\infty}{1\over \ell}
        \log N_{br}^{time}(\ell)
        \le g_{time}.
   $$
2. **Screened residual mixed tilt.**  The real four-dimensional residual
   mixed term from Definition 27.1 satisfies
   $$
        \operatorname*{ess\,sup}_{x,y,\zeta}
        \operatorname{osc}_{u,v}
        \left[
        (\Delta H_{4Dmix}^{anc})^{dc}(u,v;\zeta)
        \right]
        \le
        (\chi_0+o(1))\,\ell_{time}.
   $$

The theorem is called **closing** if, after the finite prefactor already paid
in the bridge worksheet and after the common Paper-23 tail budget
\(\kappa\), the induced bridge amplitude sum lies below the Paper-23 critical
threshold:
$$
        D_{screen}(g_{time},\chi_0)
        <
        D_{\mathrm{crit}}(\kappa),
        \qquad
        \kappa<B_*^{edge},
$$
where the exponential rate in \(D_{screen}\) is
$$
        m_{screen}
        =
        {1\over2}C_0-\chi_0-g_{time}.
$$
In particular, a necessary strict-rate condition is
$$
        {1\over2}C_0-\chi_0>g_{time}.
$$

### Theorem 28.2: Mixed RN Screening Is The Positive Fixed-\(N\) Theorem

Assume a closing instance of
`P30-MIXED-RN-SCREEN(g_time,chi_0)` and the Paper-23 common tail source
`P23-RPF-MIN-KTAIL(kappa)` with \(\kappa<B_*^{edge}\).  Then the
same-law bridge route sources `P23-RPF-TRANS0`.

Proof.

The time-compatible bridge entropy gives at most
\(\exp((g_{time}+o(1))\ell)\) true bridge atoms at length \(\ell\).  The
fundamental heat-kernel bridge account supplies the decay
\(\exp(-{1\over2}C_0\ell)\).  The screened residual mixed tilt can increase
the true bridge amplitude by at most
\(\exp((\chi_0+o(1))\ell)\).  Hence the length-\(\ell\) bridge contribution
is bounded by a finite prefactor times
$$
        \exp\left(
        -\left({1\over2}C_0-\chi_0-g_{time}+o(1)\right)\ell
        \right).
$$
The closing hypothesis says that the resulting summed bridge amplitude is
below \(D_{\mathrm{crit}}(\kappa)\).  Paper 23 Proposition 50.5 then turns
bridge damping plus `MIN-KTAIL(kappa)` into `P23-RPF-TRANS0`. `square`

Thus the positive theorem has been found in the precise sense needed by the
reduction: it is `P30-MIXED-RN-SCREEN` in a closing range.  What remains is
whether it is true for the actual four-dimensional law.

### Proposition 28.3: Current Corpus Does Not Prove Mixed RN Screening

Papers 20--29 do not prove `P30-MIXED-RN-SCREEN(g_time,chi_0)` in any
closing range.

Proof.

The entropy half is not supplied by the over-refined finite carrier: Section
24 proves only the coarse finite certificate
\(\log g_{br}^{99}\le157.02\), and Sections 25--26 prove that carrier-size
length does not provide a positive fixed-\(N\) heat-time slope.  Therefore
the required time-compatible entropy theorem is a new selector theorem, not
an existing finite-label theorem.

The tilt half is also not supplied.  Section 27 removes heat-time,
normalizer, endpoint-additive, endpoint-blind, and Paper-20 HKSD interior
tangent pieces.  The surviving object is
\((\Delta H_{4Dmix}^{anc})^{dc}\), equivalently the mixed part of the real
four-dimensional residual RN factor \(\mathcal R_j\).  Paper 20 separates
this factor from the two-dimensional axial sheet law and names
`P20-SEL2-4DCONV-CLOSE` as the missing four-dimensional content.  Papers
26--29 then show, in several equivalent languages, that the current corpus
does not print actual conditional probabilities, primitive residual atom
values, low-mode transition entries, Doeblin floors, or defect-polymer values
for the actual adaptive law.

Therefore neither half of `MIXED-RN-SCREEN` is present in the corpus. `square`

### Theorem 28.4: No Locality-Only Proof Of Mixed RN Screening

No proof using only the already closed endpoint-additive, endpoint-blind,
local/collar, HKSD tangent, finite carrier, canonical-label, RP/Cov, and
finite-battery ledgers can establish `P30-MIXED-RN-SCREEN(g_time,chi_0)`.

Proof.

Paper 23 constructs same-record residual-tail completions that preserve the
closed non-RPF source package while changing arbitrary high-order anchored
RPF residual coefficients.  Sections 49--53 of Paper 23 refine this
obstruction to the true-bridge sector: endpoint-additive and endpoint-blind
rows vanish, but surviving true bridge rows may still carry genuine mixed
four-point variation, and that variation is not determined by the finite
row labels.

The ledgers listed in the statement see exactly the data preserved by those
countermodels: local removals, endpoint zeroes, finite template labels,
canonical support classes, and HKSD tangent cancellation.  They do not see
the actual value of the residual mixed RN term on a surviving true bridge
row.  If those ledgers implied `MIXED-RN-SCREEN`, the residual-tail
countermodels would inherit the same bound, contradicting their freedom to
place \(O(1)\), and at arbitrary order nonlocal, mixed variation on the
surviving residual bridge sector while keeping the closed ledgers fixed.

Thus locality and finite bookkeeping are insufficient.  The proof of
`MIXED-RN-SCREEN`, if true, must use new same-law quantitative information
about the actual four-dimensional Yang-Mills conditional distribution.
`square`

### Corollary 28.5: The Honest Positive Continuation

The Paper-30 positive theorem is now isolated:
$$
\boxed{
\mathrm{P30\text{-}MIXED\text{-}RN\text{-}SCREEN}(g_{time},\chi_0)
\quad\text{in a closing range.}
}
$$
It is narrower than a full Dobrushin theorem for the entire infinite-volume
measure, because it asks only for time-compatible bridge entropy and screened
doubly centered residual RN tilt on the true bridge sector.  But it is still
genuine Yang-Mills value information.  It cannot be obtained by adding more
finite labels, replaying HKSD, or reusing endpoint/local cancellations.

The next positive paper-level move must therefore be one of:

1. prove `P30-MIXED-RN-SCREEN` directly from a new same-law bridge screening
   estimate;
2. prove a stronger same-law signed bridge cancellation theorem that bypasses
   the unsigned bridge entropy;
3. prove a lower floor that falsifies adaptive Branch A and forces exit to
   Branch B/C;
4. leave the fixed-\(N\) bridge route and open the declared joint
   \(N(j)\)-with-cutoff diagnostic branch.

This is the Barandes-aligned endpoint: the law is not changed, no cleaner
surrogate measure is substituted, and the remaining theorem is named exactly
where the actual conditional probabilities enter.

## 29. Executing The Screening Campaign Inside Paper 30

The previous section found the positive theorem in slope form.  We now execute
the promised split inside this same paper.  The first-principles issue is that
the `SEL2` heat-time window is bounded on the AF-area selector.  Hence a
fixed-\(N\) heat-kernel bridge proof cannot rely on an unbounded heat-time
length unless a new selector changes the effective time coordinate.  In the
actual Paper-20 scaling, the right fixed-\(N\) theorem is therefore a
time-window bridge partition-sum theorem.

### Definition 29.1: Window Bridge Partition Sum

For a true bridge \(A\), let
$$
        T_A:=T_{br,j}^{sheet}(A),
        \qquad
        0\le T_A\le T_+^{SEL2}
$$
on the cofinal AF-area tail of Lemma 25.1.  Let
$$
        \Xi_A^{4Dmix}
        :=
        \operatorname{osc}_{u,v}
        \left[
        (\Delta H_{4Dmix,A}^{anc})^{dc}(u,v;\zeta)
        \right]
$$
be the true-bridge residual mixed tilt carried by \(A\).  Define the
same-law window bridge partition sum
$$
        D_{win}^{N,j}(x,y;\zeta)
        :=
        \sum_{A\in{\mathcal U}_{br,0}^{N,j}(x,y)}
        a_A
        \exp\left(
        -{1\over2}C_0 T_A+\Xi_A^{4Dmix}
        \right),
$$
where \(a_A\) is the finite local prefactor already isolated in Sections
12--13.  The cofinal window bound is
$$
        D_{win}^{cof}
        :=
        \limsup_{(N,j)}
        \operatorname*{ess\,sup}_{x,y,\zeta}
        D_{win}^{N,j}(x,y;\zeta).
$$

### Definition 29.2: Window Mixed RN Screening

The source
$$
\boxed{
\mathrm{P30\text{-}MIXED\text{-}RN\text{-}WINDOW}(D)
}
$$
means
$$
        D_{win}^{cof}\le D
$$
on the actual adaptive `SEL2` pushed-forward scalar law.

This is not a new law.  It is the literal same-law bridge partition sum after
the tree-gauge heat-kernel factor, deterministic anchoring, and the residual
mixed RN tilt are all kept in the same conditional density.

### Theorem 29.3: Window Screening Closes The Bridge Route

Assume
$$
\mathrm{P30\text{-}MIXED\text{-}RN\text{-}WINDOW}(D)
+
\mathrm{P23\text{-}RPF\text{-}MIN\text{-}KTAIL}(\kappa).
$$
If
$$
        D<D_{\mathrm{crit}}(\kappa),
        \qquad
        \kappa<B_*^{edge},
$$
then `P23-RPF-TRANS0` holds.

Proof.

The summand in Definition 29.1 is exactly the same-law heat-kernel bridge
amplitude bound after the residual mixed RN tilt is paid.  Therefore
`MIXED-RN-WINDOW(D)` implies the Paper-23 bridge-amplitude source
`P23-RPF-MIN-BRIDGE(D)`, equivalently `MIN-BRIDGEAMP(D)`.  Paper 23
Proposition 50.5 then turns this bridge source plus `MIN-KTAIL(kappa)` into
`P23-RPF-TRANS0` whenever the displayed inequalities hold. `square`

### Lemma 29.4: Slope Screening Implies Window Screening Only With A Real
Time-Window Count

Assume `P30-MIXED-RN-SCREEN(g_time,chi_0)` in the slope sense of Definition
28.1.  It implies `P30-MIXED-RN-WINDOW(D)` only after one also proves a
cofinal finite time-window count or partition estimate:
$$
        \operatorname*{ess\,sup}_{x,y,\zeta}
        \sum_{A\in{\mathcal U}_{br,0}^{N,j}(x,y)}
        a_A e^{-(m_{screen}+o(1))T_A}
        \le D.
$$

Proof.

The slope theorem controls a rate per time-compatible unit.  But Lemma 25.1
puts every \(T_A\) inside a bounded interval.  Therefore the sum is not
controlled by sending \(T_A\to\infty\); it is controlled only by the actual
number and prefactor weight of true bridges inside the finite heat-time
window.  A rate estimate without a window partition estimate does not bound
the total bridge amplitude. `square`

### Corollary 29.5: The Correct Fixed-\(N\) Positive Theorem

For fixed declared \(SU(N_0)\), the most precise positive bridge theorem is
$$
\boxed{
\mathrm{P30\text{-}MIXED\text{-}RN\text{-}WINDOW}(D)
+
\mathrm{P23\text{-}RPF\text{-}MIN\text{-}KTAIL}(\kappa)
}
$$
with
$$
        D<D_{\mathrm{crit}}(\kappa),
        \qquad
        \kappa<B_*^{edge}.
$$
The slope theorem `P30-MIXED-RN-SCREEN(g_time,chi_0)` remains a useful way
to source this, but only if it is accompanied by a true time-window bridge
partition estimate.  This is the fixed-\(N\) correction forced by the bounded
AF-area heat-time window.

## 30. The Time-Entropy Half

We now test the first half of the screening theorem: can the current corpus
prove the required time-window bridge count or entropy estimate?

### Definition 30.1: Time-Window Bridge Entropy

Define
$$
        G_{time}^{win}(N,j)
        :=
        \operatorname*{ess\,sup}_{x,y,\zeta}
        \log
        \sum_{A\in{\mathcal U}_{br,0}^{N,j}(x,y)}
        a_A
$$
where the sum is restricted to the true bridges inside the bounded heat-time
window \(0\le T_A\le T_+^{SEL2}\).  The source
$$
\boxed{
\mathrm{P30\text{-}BRIDGE\text{-}TIMEWIN}(G)
}
$$
means
$$
        \limsup_{(N,j)}G_{time}^{win}(N,j)\le G.
$$

This is the bounded-window replacement for a naive asymptotic entropy slope.

### Lemma 30.2: Carrier Entropy Does Not Bound Time-Window Entropy

The over-refined carrier entropy certificate
$$
        g_{br}\le g_{br}^{99},
        \qquad
        \log g_{br}^{99}\le157.02,
$$
does not imply `P30-BRIDGE-TIMEWIN(G)` for any useful finite \(G\).

Proof.

The carrier certificate counts supports by carrier-size length.  The
heat-time window counts all true bridge supports whose accumulated sheet time
fits inside \(T_+^{SEL2}\).  On the AF-area selector, the microscopic sheet
time per elementary factor tends to zero, while the total block time remains
bounded.  Therefore carrier-size can grow inside a bounded time window.  A
bound per carrier step gives no uniform bound on the total number or prefactor
weight of carrier supports that fit into that window. `square`

### Proposition 30.3: Current-Corpus Time-Entropy Verdict

The current corpus does not prove `P30-BRIDGE-TIMEWIN(G)` in a closing range.

Proof.

Papers 20--23 prove finite carrier tables, canonical labels, and the
over-refined support entropy in carrier units.  Sections 25--26 of this paper
prove that those carrier units are not heat-time units for fixed \(N\).
No previous paper prints a physical true-bridge selector, a time-window
self-avoidance theorem, or a finite automaton whose accepted bridge count is
uniformly bounded inside \(0\le T_A\le T_+^{SEL2}\).  Lemma 30.2 shows that
the existing carrier entropy cannot be converted into such a theorem.
Therefore the time-entropy half remains a genuine new source:
$$
\boxed{\mathrm{P30\text{-}BRIDGE\text{-}TIMEWIN\text{-}GAP}.}
$$
`square`

### Corollary 30.4: What Would Close The Entropy Half

The entropy half can be closed only by proving one of the following same-law
statements:

1. a physical true-bridge selector with uniformly bounded accepted
   time-window partition sum;
2. a cancellation theorem allowing signed summation before the bridge count
   is paid;
3. a stronger heat-time selector in which bridge time grows with the relevant
   support complexity;
4. the window theorem `P30-MIXED-RN-WINDOW(D)` directly, bypassing a separate
   entropy count.

No item is currently in Papers 20--30.

## 31. The Residual RN Mixed-Tilt Half

We now test the second half: can the current corpus prove that the real
four-dimensional residual RN mixed tilt is screened on the true bridge rows?

### Definition 31.1: Residual Mixed-Tilt Window Source

For \(\chi\ge0\), define
$$
\boxed{
\mathrm{P30\text{-}RN\text{-}MIXED\text{-}TILTWIN}(\chi)
}
$$
to mean
$$
        \limsup_{(N,j)}
        \operatorname*{ess\,sup}_{x,y,\zeta}
        \sup_{A\in{\mathcal U}_{br,0}^{N,j}(x,y)}
        \left(
        \Xi_A^{4Dmix}-\chi T_A
        \right)
        \le0.
$$

This is the bounded-window version of
`P30-TILT-LOCAL-BRIDGE(chi)`.  It is still evaluated on the actual pushed
forward scalar law and on the literal residual RN factor.

### Lemma 31.2: Local And HKSD Ledgers Do Not Prove Tilt Screening

The already closed local/endpoint/HKSD ledgers imply only that the residual
mixed tilt has been reduced to \(\Delta H_{4Dmix}^{dc}\).  They do not prove
`P30-RN-MIXED-TILTWIN(chi)` for any closing \(\chi\).

Proof.

Section 27 proves the reduction.  Endpoint-additive and endpoint-blind rows
have zero mixed debit; scalar normalizers and heat-time tangents are already
charged; Paper 20's HKSD audit cancels the interior tangent expansion.  None
of these statements evaluates the actual residual factor \(\mathcal R_j\).
The remaining term is precisely the real four-dimensional off-sheet/Bianchi
RN correction.  Thus the closed ledgers identify what must be bounded, but
do not bound it. `square`

### Proposition 31.3: Residual-Tail Obstruction To Tilt Screening From The
Current Corpus

The current corpus cannot derive `P30-RN-MIXED-TILTWIN(chi)` from the already
closed ledgers.

Proof.

Use the Paper-23 residual-tail countermodel family.  It preserves the closed
non-RPF source package, including local removals, endpoint-additive zeroes,
finite carrier labels, canonical support labels, RP/Cov transport, and the
HKSD tangent audit.  But it can place genuine mixed variation on surviving
true bridge rows.  Since \(T_A\le T_+^{SEL2}\), increasing the residual mixed
variation on a surviving row can violate any proposed closing bound
\(\Xi_A^{4Dmix}\le\chi T_A+o(1)\) while leaving the closed ledgers unchanged.

Therefore tilt screening is not a current-corpus theorem.  It must be proved
from new same-law quantitative information about the actual residual RN
factor. `square`

### Corollary 31.4: Residual-Tilt Verdict

The residual half remains open exactly at
$$
\boxed{\mathrm{P30\text{-}RN\text{-}MIXED\text{-}TILTWIN\text{-}GAP}.}
$$
The viable positive mechanisms are:

1. a direct bound on the actual residual density ratio;
2. a same-law signed cancellation identity on true bridges;
3. a defect-polymer value theorem of the kind exported by Paper 29;
4. a narrow conditional influence theorem only for the true-bridge residual
   sector;
5. a lower-floor theorem that exits adaptive Branch A instead of closing it.

## 32. Paper-30 In-Paper Screening Verdict

We have now executed the proposed Paper-31 campaign inside Paper 30.  The
result is sharper than the original plan.

### Theorem 32.1: Exact Positive Fixed-\(N\) Bridge Theorem

For fixed declared \(SU(N_0)\), the exact positive theorem that would close
the Paper-30 bridge route is
$$
\boxed{
\mathrm{P30\text{-}MIXED\text{-}RN\text{-}WINDOW}(D)
+
\mathrm{P23\text{-}RPF\text{-}MIN\text{-}KTAIL}(\kappa)
}
$$
with
$$
        D<D_{\mathrm{crit}}(\kappa),
        \qquad
        \kappa<B_*^{edge}.
$$
It is implied by a successful time-window bridge partition theorem plus a
successful residual mixed-tilt screening theorem, but those two subtheorems
are not supplied by the current corpus.

Proof.

The closure implication is Theorem 29.3.  The time-window subtheorem is
unsourced by Proposition 30.3.  The residual mixed-tilt subtheorem is
unsourced by Proposition 31.3. `square`

### Corollary 32.2: Fixed-\(N\) Bridge Route Is Fully Audited At The
Current-Corpus Level

Inside fixed declared \(SU(N_0)\), including the \(N_0=4096\) diagnostic row,
Paper 30 has now exhausted the bridge route as far as Papers 20--29 permit:

1. direct signed bridge values are unsourced;
2. closed-body finite dual certificates do not close;
3. unsigned bridge damping requires `MIXED-RN-WINDOW`;
4. carrier entropy is in the wrong unit;
5. time-window entropy is unsourced;
6. residual mixed RN tilt screening is unsourced;
7. the lower-floor exit remains unsourced.

Thus the next real theorem cannot be a larger finite carrier table.  It must
be new same-law value information: `MIXED-RN-WINDOW`, direct signed bridge
values, a true-bridge cancellation identity, a defect-polymer value/influence
theorem, or the lower floor.

### Corollary 32.3: Barandes Alignment Of The Remaining Target

The remaining target is Barandes-aligned precisely because it stays with the
actual finite record law:

1. all conditionals are conditionals of the adaptive `SEL2` scalar law;
2. the parent tree-gauge chart is used only through deterministic
   disintegration and pushforward;
3. the residual RN factor is not replaced by a heat-kernel surrogate;
4. no hidden Markov bridge process is inserted;
5. every proposed bound is a bound on a literal same-law finite quantity.

The price of that alignment is that the theorem is hard.  It asks for actual
quantitative information about the four-dimensional Yang-Mills residual
conditional distribution.  Paper 30 has now isolated that price without
smuggling it into the notation.

## 33. Signed Bridge Involution Test

The remaining plausible positive move is signed cancellation before the
unsigned window sum is paid.  This section tests the cleanest possible
mechanism: pair true bridge rows by an actual same-law involution and ask
whether the paired orbit sums are small.

### Definition 33.1: Admissible True-Bridge Involution

An admissible signed bridge involution is a deterministic map
$$
        \iota:
        {\mathcal U}_{br,0}^{N,j}(x,y)
        \longrightarrow
        {\mathcal U}_{br,0}^{N,j}(x,y)
$$
such that:

1. \(\iota^2=\mathrm{id}\);
2. \(\iota\) is generated only by recorded symmetries: orientation reversal,
   representation duality, endpoint exchange, conjugation, reflection, or an
   already declared quotient/covariance map;
3. \(\iota\) preserves the outside scalar record \(\zeta\) up to the same
   deterministic record processing already licensed in Papers 20--29;
4. no probabilistic resampling, hidden Markov bridge, or cleaner comparison
   law is introduced.

Let \({\mathcal O}_\iota\) be the finite set of \(\iota\)-orbits.

### Definition 33.2: Orbit-Signed Bridge Defect

For an orbit \(O\in{\mathcal O}_\iota\), define
$$
        B_O^{\iota}(u,v;\zeta)
        :=
        \sum_{A\in O}G_A^{anc}(u,v;\zeta).
$$
The total involution defect is
$$
        W_{\iota\text{-}def}^{anc}
        :=
        \sum_{O\in{\mathcal O}_\iota}
        B_O^{\iota}.
$$
This is not an approximation:
$$
        W_{\iota\text{-}def}^{anc}=W_{br,0}^{anc}.
$$
The point of the notation is to force every proposed cancellation to occur
orbit by orbit before oscillations are estimated.

### Definition 33.3: Involution Defect Value Source

`P30-BRIDGE-INV-DEFECT(Theta,omega,kappa)` asserts that, cofinally,
$$
        \operatorname*{ess\,sup}_{x,y,\zeta}
        \operatorname{osc}_{u,v}
        \left[
        (W_{\iota\text{-}def}^{anc})^{dc}(u,v;\zeta)
        \right]\le\Theta,
$$
$$
        \operatorname*{ess\,sup}_{x,y,\zeta}
        \max\left\{
        \sup_u\operatorname{osc}_v W_{\iota\text{-}def}^{anc},
        \sup_v\operatorname{osc}_u W_{\iota\text{-}def}^{anc}
        \right\}\le\omega,
$$
and the common tail source `P23-RPF-MIN-KTAIL(kappa)` holds.

### Lemma 33.4: Involution Defect Values Close The Signed Route

If `P30-BRIDGE-INV-DEFECT(Theta,omega,kappa)` holds and
$$
        \Theta+\omega^2/4<M_{\mathrm{sgn}}(\kappa),
$$
then `P23-RPF-TRANS0` holds.

Proof.

By Definition 33.2, \(W_{\iota\text{-}def}^{anc}=W_{br,0}^{anc}\) exactly.
Thus Definition 33.3 is just `P30-SIGNED-BRIDGE-VALUE(Theta,omega,kappa)`
written in orbit-sum form.  Theorem 1.6 applies. `square`

## 34. Heat-Kernel Symmetric Cancellation Versus Actual Residual Defect

The involution route is useful only if a large part of each orbit sum cancels
for structural reasons.  The most optimistic structural part is the
tree-gauge heat-kernel character contribution.  The dangerous part is the
actual four-dimensional residual RN asymmetry.

### Definition 34.1: HK-Symmetric Orbit Split

For a chosen admissible involution \(\iota\), an HK-symmetric split is a
finite same-law algebraic decomposition
$$
        G_A^{anc}
        =
        H_A^{HK,\iota}
        +
        R_A^{\iota}
$$
on every true bridge row, where \(H_A^{HK,\iota}\) is the part transformed
by the recorded heat-kernel orientation/duality/reflection rule and
\(R_A^{\iota}\) is the remaining actual residual asymmetry.  The split is
admissible only if both terms are deterministic functions of the same finite
record and their sum is the actual \(G_A^{anc}\).

The HK cancellation source
$$
\boxed{\mathrm{P30\text{-}BRIDGE\text{-}INV\text{-}HKCANCEL}(\iota)}
$$
means that for every orbit \(O\),
$$
        \left(
        \sum_{A\in O}H_A^{HK,\iota}
        \right)^{dc}=0.
$$

The residual involution defect is
$$
        R_{\iota}^{anc}
        :=
        \sum_{O\in{\mathcal O}_\iota}
        \sum_{A\in O}R_A^{\iota}.
$$

### Lemma 34.2: HK Cancellation Reduces The Signed Sum To Residual Defect

Assume `P30-BRIDGE-INV-HKCANCEL(iota)` for an admissible split.  Then
$$
        (W_{br,0}^{anc})^{dc}
        =
        (R_{\iota}^{anc})^{dc}.
$$

Proof.

Sum the decomposition \(G_A^{anc}=H_A^{HK,\iota}+R_A^\iota\) over every
orbit.  The double-centered HK orbit sums vanish by Definition 34.1.  The
remaining double-centered signed bridge Hamiltonian is exactly the
double-centered residual defect. `square`

### Definition 34.3: Residual Involution Defect Source

`P30-BRIDGE-INV-RESDEF(Theta,omega,kappa)` asserts that after an admissible
HK-symmetric split satisfying `P30-BRIDGE-INV-HKCANCEL(iota)`, the residual
defect \(R_\iota^{anc}\) satisfies
$$
        \operatorname*{ess\,sup}_{x,y,\zeta}
        \operatorname{osc}_{u,v}
        \left[
        (R_\iota^{anc})^{dc}(u,v;\zeta)
        \right]\le\Theta,
$$
$$
        \operatorname*{ess\,sup}_{x,y,\zeta}
        \max\left\{
        \sup_u\operatorname{osc}_v R_\iota^{anc},
        \sup_v\operatorname{osc}_u R_\iota^{anc}
        \right\}\le\omega,
$$
and `P23-RPF-MIN-KTAIL(kappa)` holds on the same cofinal selector.

### Theorem 34.4: Residual Defect Smallness Closes The Signed Route

Assume `P30-BRIDGE-INV-RESDEF(Theta,omega,kappa)`.  If
$$
        \Theta+\omega^2/4<M_{\mathrm{sgn}}(\kappa),
$$
then `P23-RPF-TRANS0` holds.

Proof.

By Lemma 34.2, the signed bridge range and one-line width are bounded by the
corresponding residual defect bounds.  Thus `P30-SIGNED-BRIDGE-VALUE` holds
with \((\Theta,\omega,\kappa)\).  Apply Theorem 1.6. `square`

## 35. Exhausting The Current Involution Sources

We now check the actual sources available in the current corpus.

### Lemma 35.1: Recorded Symmetries Do Not Supply A Negative Pairing By
Themselves

Orientation reversal, representation duality, endpoint exchange, conjugation,
reflection, covariance, and quotient equalities do not by themselves prove
`P30-BRIDGE-INV-RESDEF(Theta,omega,kappa)` in a closing range.

Proof.

Paper 23 Table 53.7 and Table 54.6 already isolate the issue.  These
symmetries reduce or identify record labels.  They do not provide a negative
coefficient, a small amplitude, or a pointwise conditional Hamiltonian range
bound for surviving true bridge rows.  RP/positivity supplies inequalities
on reflected moment bodies, not a saturation theorem for the pointwise signed
bridge Hamiltonian.  Therefore the symmetries may define an admissible
involution, but they do not evaluate the orbit sums. `square`

### Lemma 35.2: Ideal Heat-Kernel Cancellation Does Not Control The Actual
Residual RN Asymmetry

Even if `P30-BRIDGE-INV-HKCANCEL(iota)` holds for the heat-kernel symmetric
part of an admissible split, the current corpus does not bound
\((R_\iota^{anc})^{dc}\) in a closing range.

Proof.

The heat-kernel part is the part transformed by the recorded
orientation/duality/reflection rule.  The actual signed bridge row, however,
is the residual minimal-edge object after `BC/CE`, anchoring, central-entry
processing, retained-row removal, scalar pushforward, and the real
four-dimensional RN correction.  Papers 26--29 prove that the needed
residual values, conditional normalizers, defect polymer values, and defect
influence matrix are not printed.  Section 31 of this paper proves the same
gap in bounded-window tilt language.  Thus heat-kernel symmetry can cancel
only the ideal symmetric component; it does not bound the actual residual
asymmetry defect. `square`

### Proposition 35.3: Residual-Tail No-Go For Current Involution Closure

The current corpus cannot prove
`P30-BRIDGE-INV-RESDEF(Theta,omega,kappa)` in the signed closing range.

Proof.

Assume such a proof were derivable from the already closed ledgers:
finite carriers, canonical labels, endpoint-additive removals, covariance,
conjugation, reflection, RP/Cov transport, and HKSD/heat-kernel tangent
audits.  The residual-tail countermodels of Paper 23 preserve exactly those
ledgers while changing surviving true-bridge mixed modes.  In orbit language,
they can change one residual asymmetry orbit sum
\(\sum_{A\in O}R_A^\iota\), or a fixed-point orbit, without changing the
declared symmetry labels or the already closed zero rows.

Changing such an orbit changes
\((R_\iota^{anc})^{dc}\), hence changes the signed range and one-line width,
while preserving the closed current-corpus data.  Therefore no closing bound
on the residual involution defect follows from the current corpus. `square`

We record:
$$
\boxed{
\mathrm{P30\text{-}BRIDGE\text{-}INV\text{-}RESDEF\text{-}GAP}.
}
$$

## 36. Lower-Floor Pivot After Signed-Defect Failure

Failure to prove signed defect smallness is not itself a falsification of
adaptive Branch A.  The opposite theorem must be a same-law lower floor.

### Definition 36.1: Involution-Defect Lower Floor

`P30-BRIDGE-INV-DEFECT-FLOOR(M_*)` asserts that, after all retained
heat-kernel symmetric cancellations and licensed local/endpoint removals are
applied, the residual involution defect forces
$$
        \overline\Lambda_{13}^{RPF}\ge M_*.
$$

This is a lower bound on the actual adaptive predebit, not merely the
absence of a smallness proof.

### Lemma 36.2: Defect Floor Falsifies Adaptive Branch A

If all positive Branch-A closing routes retained in Papers 25--30 fail and
`P30-BRIDGE-INV-DEFECT-FLOOR(M_*)` holds, then adaptive Branch A is
falsified.

Proof.

Adaptive Branch A requires the actual RPF predebit to fall strictly below
the threshold \(M_*\).  The displayed lower floor gives the opposite
inequality for the same actual law after the same licensed reductions.
Therefore the branch cannot close. `square`

### Proposition 36.3: Current Corpus Does Not Prove The Involution-Defect
Floor

The current corpus does not prove `P30-BRIDGE-INV-DEFECT-FLOOR(M_*)`.

Proof.

Paper 27 proves that failure of RN-MIXAMP smallness is not a lower floor.
Paper 29 proves the analogous statement for the primitive residual defect:
failure of defect Dobrushin or defect polymer smallness is not a floor unless
a coherent same-law witness survives normalizers, signs, retained-row
subtractions, and cancellations.  Proposition 35.3 shows that the signed
involution residual defect is likewise not bounded above by the current
corpus, but it does not give a sign-coherent lower bound.  No paper prints
the needed witness. `square`

We record:
$$
\boxed{
\mathrm{P30\text{-}BRIDGE\text{-}INV\text{-}DEFECT\text{-}FLOOR\text{-}GAP}.
}
$$

## 37. Signed-Involution Campaign Verdict

The five-step signed-involution push is now complete.

### Theorem 37.1: Signed-Involution Route Status

Inside Paper 30:

1. the admissible true-bridge involution format is defined;
2. an orbit-signed defect value theorem is proved sufficient for the signed
   route;
3. an HK-symmetric cancellation theorem is proved sufficient to reduce the
   signed object to a residual involution defect;
4. the current corpus is shown not to bound that residual defect in a
   closing range;
5. the correct negative pivot is shown to be an involution-defect lower
   floor, which is also unsourced by the current corpus.

Proof.

Items 1 and 2 are Definitions 33.1--33.3 and Lemma 33.4.  Item 3 is Lemma
34.2 and Theorem 34.4.  Item 4 is Proposition 35.3.  Item 5 is Lemma 36.2
and Proposition 36.3. `square`

### Corollary 37.2: The Remaining Positive Options After The Signed Push

The signed-involution route does not produce a current-corpus positive proof.
It does sharpen the next real options:

1. print an actual residual involution-defect value theorem
   `P30-BRIDGE-INV-RESDEF`;
2. print the unsigned window partition source `P30-MIXED-RN-WINDOW`;
3. print the Paper-29 defect value/influence theorem;
4. print a same-law lower floor;
5. exit adaptive Branch A.

Every option is same-law.  None is a finite-label refinement.

## 38. The Residual-Defect Bound We Actually Need

The previous sections locate the obstruction.  This section makes the
needed residual-defect estimate explicit enough that it can be attacked by
finite conditional data, by a defect KP theorem, or by a signed lower-floor
witness.  The point is to avoid a vague phrase such as "control the residual":
we need a concrete mixed cross-ratio and one-line bound on the same adaptive
`SEL2` pushed-forward scalar law.

### Definition 38.1: Anchored Mixed Cross-Ratio

For a two-endpoint bridge residual \(F(u,v;\zeta)\), define
$$
\nabla_{u,u';v,v'}F(\zeta)
:=
F(u,v;\zeta)-F(u',v;\zeta)-F(u,v';\zeta)+F(u',v';\zeta).
$$

Let \(U_{br}^{N,j}\) and \(V_{br}^{N,j}\) be the two endpoint record sets of
the true-bridge edge under consideration, and let \(\zeta\) denote the
remaining finite blanket records.  For an admissible involution split
\(G_A^{anc}=H_A^{HK,\iota}+R_A^\iota\), define the residual mixed
cross-ratio size
$$
{\mathcal C}_{\iota}^{N,j}
:=
\operatorname*{ess\,sup}_{\zeta}
\sup_{u,u'\in U_{br}^{N,j}}
\sup_{v,v'\in V_{br}^{N,j}}
\left|
\nabla_{u,u';v,v'} R_\iota^{anc}(\zeta)
\right|.
$$

Define the residual one-line size
$$
{\mathcal O}_{\iota}^{N,j}
:=
\operatorname*{ess\,sup}_{\zeta}
\max\left\{
\sup_{u\in U_{br}^{N,j}}\operatorname{osc}_{v\in V_{br}^{N,j}}
R_\iota^{anc}(u,v;\zeta),
\sup_{v\in V_{br}^{N,j}}\operatorname{osc}_{u\in U_{br}^{N,j}}
R_\iota^{anc}(u,v;\zeta)
\right\}.
$$

The cofinal versions are
$$
{\mathcal C}_{\iota}^{cof}:=\limsup_{(N,j)\to\infty}{\mathcal C}_{\iota}^{N,j},
\qquad
{\mathcal O}_{\iota}^{cof}:=\limsup_{(N,j)\to\infty}{\mathcal O}_{\iota}^{N,j}.
$$

### Lemma 38.2: Cross-Ratio Controls The Double-Centered Defect

For the anchored double center used in the Paper-23 signed gate,
$$
\operatorname{osc}_{u,v}(R_\iota^{anc})^{dc}(u,v;\zeta)
\le
2
\sup_{u,u',v,v'}
\left|
\nabla_{u,u';v,v'}R_\iota^{anc}(\zeta)
\right|.
$$

Proof.

Fix an anchor \((u_0,v_0)\).  The anchored double center is
$$
F^{dc}(u,v)
=
F(u,v)-F(u,v_0)-F(u_0,v)+F(u_0,v_0).
$$
For two endpoint pairs \((u,v)\) and \((u',v')\),
$$
F^{dc}(u,v)-F^{dc}(u',v')
=
\nabla_{u,u';v,v_0}F+\nabla_{u',u_0;v,v'}F.
$$
Taking absolute values and then the supremum gives the factor \(2\). `square`

### Definition 38.3: Residual Cross-Ratio Source

`P30-BRIDGE-INV-XRATIO(C,Omega,kappa)` asserts that an admissible
HK-symmetric split satisfies `P30-BRIDGE-INV-HKCANCEL(iota)`,
`P23-RPF-MIN-KTAIL(kappa)`, and cofinally
$$
{\mathcal C}_{\iota}^{cof}\le C,
\qquad
{\mathcal O}_{\iota}^{cof}\le\Omega.
$$

This is the sharp residual-defect bound.  It is stronger than merely naming
the residual defect and weaker than reconstructing the whole conditional
law: it asks only for the mixed cross-ratio and the one-line oscillation
that the signed scalar gate actually uses.

### Theorem 38.4: The Required Residual-Defect Inequality

Assume `P30-BRIDGE-INV-XRATIO(C,Omega,kappa)`.  If
$$
2C+\Omega^2/4<M_{\mathrm{sgn}}(\kappa),
$$
then `P23-RPF-TRANS0` holds.

Proof.

By Lemma 38.2, the double-centered residual defect range is at most \(2C\),
and the one-line width is at most \(\Omega\).  Hence
`P30-BRIDGE-INV-RESDEF(2C,Omega,kappa)` holds.  Theorem 34.4 then gives
`P23-RPF-TRANS0` under the displayed inequality. `square`

We record the exact target:
$$
\boxed{
\mathrm{P30\text{-}BRIDGE\text{-}INV\text{-}XRATIO}(C,\Omega,\kappa)
\quad\text{with}\quad
2C+\Omega^2/4<M_{\mathrm{sgn}}(\kappa).
}
$$

This is the residual-defect bound to find.

## 39. Maximal Retention For The Involution Defect

The next question is how one could source
`P30-BRIDGE-INV-XRATIO(C,Omega,kappa)` without reconstructing the whole
four-dimensional measure.  The least wasteful route is to remove every row
whose value is already licensed, leaving only the genuine same-law defect.

### Definition 39.1: Maximal Involution-Retained Class

Let \({\mathcal C}_{\iota,ret,max}^{N,j}\) be the largest class of anchored
rows satisfying all of the following:

1. the row is zero by a previously closed finite table, endpoint-additive
   removal, BC/CE cancellation, covariance, conjugation, reflection,
   quotient equality, or HKSD tangent cancellation;
2. or the row belongs to an admissible HK-symmetric involution orbit whose
   double-centered orbit sum is zero by `P30-BRIDGE-INV-HKCANCEL(iota)`;
3. or the row has an actual same-law value table already printed in Papers
   20--30 and may therefore be subtracted without changing the adaptive law;
4. or the row is endpoint-only after anchoring and hence does not charge the
   bridge mixed cross-ratio.

Define the maximal involution defect
$$
D_{\iota,max}^{N,j}
:=
R_\iota^{anc,N,j}
-
\sum_{A\in{\mathcal C}_{\iota,ret,max}^{N,j}}\Psi_A^{N,j}.
$$

This is a same-law residual.  It is not a new model and not a replacement
heat-kernel process.

### Lemma 39.2: Maximal Retention Does Not Hide The Signed Charge

The signed bridge quantity controlled by `P30-BRIDGE-INV-XRATIO` is unchanged
if \(R_\iota^{anc}\) is replaced by \(D_{\iota,max}\), except for rows whose
same-law values have explicitly been subtracted into the retained account.

Proof.

The retained rows are exactly rows whose bridge mixed cross-ratio is zero, or
rows whose same-law value has been printed and charged in the scalar ledger.
Endpoint-only rows vanish under the mixed cross-ratio.  HK-symmetric
involution orbits vanish by the cancellation source.  Therefore the only
unaccounted signed charge is the maximal defect \(D_{\iota,max}\). `square`

### Definition 39.3: Involution-Defect KP Source

`P30-BRIDGE-INV-DEFECT-KP(B,a,epsilon)` asserts that the same-law maximal
defect \(D_{\iota,max}^{N,j}\) admits, cofinally, a connected polymer
expansion
$$
D_{\iota,max}^{N,j}
=
\sum_{\Gamma} w_{\Gamma}^{\iota,N,j}
$$
on the finite defect graph, with
$$
\sup_x
\sum_{\Gamma\ni x}
e^{a\,{\rm diam}(\Gamma)}
|w_{\Gamma}^{\iota,N,j}|
\le B+\epsilon_j,
\qquad
\epsilon_j\to0.
$$
The expansion is required to be the actual pushed-forward scalar law after
the retained rows of Definition 39.1 have been subtracted.

### Lemma 39.4: Defect KP Gives A Residual Cross-Ratio Bound

Assume `P30-BRIDGE-INV-DEFECT-KP(B,a,epsilon)`.  Let \(d_{br}\) be the
defect-graph distance between the two endpoint record sets of the true
bridge after all retained rows have been removed.  Then cofinally
$$
{\mathcal C}_{\iota}^{cof}
\le
2B e^{-a d_{br}},
$$
up to the vanishing \(\epsilon_j\) remainder, and
$$
{\mathcal O}_{\iota}^{cof}
\le
2B
$$
up to the same vanishing remainder.

Proof.

A polymer that meets neither endpoint set cancels from the mixed cross-ratio.
A polymer that meets only one endpoint set is endpoint-only for the mixed
operation and also cancels from the mixed cross-ratio.  Thus only polymers
meeting both endpoint sets contribute to
\({\mathcal C}_{\iota}^{N,j}\).  Such polymers have diameter at least
\(d_{br}\), so the weighted KP bound gives the exponential factor
\(e^{-a d_{br}}\).  The factor \(2\) absorbs the two endpoint sums and the
limsup remainder.  For one-line oscillation, polymers meeting the varied
endpoint side may contribute without crossing to the other side, and the
weighted sum gives \(2B\). `square`

### Corollary 39.5: KP Form Of The Required Bound

If
$$
4B e^{-a d_{br}}+B^2<M_{\mathrm{sgn}}(\kappa),
$$
after the vanishing cofinal remainder is absorbed, then
`P23-RPF-TRANS0` holds.

Proof.

Lemma 39.4 gives \(C=2B e^{-a d_{br}}\) and \(\Omega=2B\).  Theorem 38.4
then gives the displayed condition. `square`

The useful lesson is severe: a KP theorem is valuable only if it controls
the actual maximal involution defect with enough amplitude slack.  A label
table that merely increases \(d_{br}\) without bounding \(B\) does not close
the route.

## 40. Defect Influence Route To The Bound

The Dobrushin route is the most direct finite conditional route to the KP
source of Section 39, but it must be applied to the actual maximal defect,
not to a heat-kernel surrogate.

### Definition 40.1: Involution-Defect Conditional Specification

Let \(V_{\iota,def}^{N,j}\) be the finite record battery consisting of every
record coordinate appearing in an unretained atom of \(D_{\iota,max}^{N,j}\),
together with the endpoint and blanket coordinates needed to define finite
conditional laws.  For \(x\in V_{\iota,def}^{N,j}\), define
$$
\mu_x^{\iota,def,N,j}(s\mid\zeta)
:=
{
\exp D_{\iota,max}^{N,j}(s,\zeta)\,d\lambda_x(s)
\over
\int \exp D_{\iota,max}^{N,j}(s',\zeta)\,d\lambda_x(s')
}.
$$
The denominator is understood in the same essential-support sense used in
Papers 23 and 29.

Define the influence matrix
$$
I_{xy}^{\iota,def,N,j}
:=
\sup_{\zeta,\zeta':\,\zeta_{V\setminus y}=\zeta'_{V\setminus y}}
\left\|
\mu_x^{\iota,def,N,j}(\cdot\mid\zeta)
-
\mu_x^{\iota,def,N,j}(\cdot\mid\zeta')
\right\|_{\rm TV},
$$
and the weighted row norm
$$
{\mathfrak D}_{\iota,def}^{N,j}(a)
:=
\sup_x\sum_y e^{a d_{\iota,def}(x,y)}
I_{xy}^{\iota,def,N,j}.
$$

### Definition 40.2: Involution-Defect Dobrushin Source

`P30-BRIDGE-INV-DEFECT-DOB(q,a,B)` asserts that, cofinally,
$$
{\mathfrak D}_{\iota,def}^{N,j}(a)\le q<1,
$$
and that the local defect activity normalization used in the induced
finite-volume cluster expansion is bounded by \(B\) after the maximal
retained class has been subtracted.

The \(B\)-clause is necessary.  A strict influence row gives decay of
conditional dependence, but the signed bridge margin also needs the size of
the local defect activity.

### Theorem 40.3: Defect Dobrushin Sources The Residual Bound

If `P30-BRIDGE-INV-DEFECT-DOB(q,a,B)` holds, then there are
\(a'<a\), \(B'=B'(q,a,B)\), and \(\epsilon_j\to0\) such that
`P30-BRIDGE-INV-DEFECT-KP(B',a',epsilon)` holds.  Consequently, if
$$
4B'e^{-a'd_{br}}+(B')^2<M_{\mathrm{sgn}}(\kappa),
$$
then `P23-RPF-TRANS0` holds.

Proof.

The finite specification of Definition 40.1 is a finite Gibbs specification
on the same pushed-forward scalar record battery.  The weighted strict
Dobrushin row bound gives the finite Dobrushin-Shlosman connected-expansion
estimate used in Paper 23 and Paper 29, with weakened constants
\((q,a,B)\mapsto(B',a')\).  The activity normalization gives the local
amplitude scale.  This proves the KP source.  Corollary 39.5 then gives the
signed route. `square`

### Proposition 40.4: Current Corpus Does Not Prove The Defect Influence
Bound

The current corpus does not prove
`P30-BRIDGE-INV-DEFECT-DOB(q,a,B)` in a closing range.

Proof.

Definition 40.1 requires the actual conditional distributions of
\(D_{\iota,max}^{N,j}\).  Papers 26--29 repeatedly prove that the current
corpus supplies the formal residual atom identities, finite worksheets, and
ratio identities, but not the unretained actual conditional values or
influence matrix.  Proposition 35.3 gives the signed-involution version of
the same obstruction: residual-tail completions can preserve all closed
finite labels and symmetries while changing a surviving true-bridge residual
orbit.  Such completions change the influence row and the activity scale.
Therefore the Dobrushin/KP route is valid but unsourced by the current
corpus. `square`

We record:
$$
\boxed{
\mathrm{P30\text{-}BRIDGE\text{-}INV\text{-}DEFECT\text{-}DOB\text{-}GAP}.
}
$$

## 41. Projected Low-Mode Plus Tail Route

If the Dobrushin row is too strong, one can try to bound only the signed
bridge functional directly by a projected Peter-Weyl calculation and a tail.
This is narrower than proving full conditional mixing.

### Definition 41.1: Projected Involution-Defect Bound

Let \(\Pi_{\le L}\) be the finite Peter-Weyl projection on the endpoint and
blanket records used by the signed bridge functional.  Define
$$
D_{\iota,L}^{N,j}:=\Pi_{\le L}D_{\iota,max}^{N,j}\Pi_{\le L}.
$$
`P30-BRIDGE-INV-LOWTAIL(L,C_L,Omega_L,r_L,kappa)` asserts that
`P23-RPF-MIN-KTAIL(kappa)` holds, that
$$
{\mathcal C}_{\iota,L}^{cof}\le C_L,
\qquad
{\mathcal O}_{\iota,L}^{cof}\le\Omega_L,
$$
for the projected defect, and that the omitted tail contributes at most
\(r_L\) to the mixed cross-ratio and at most \(r_L\) to the one-line
oscillation.

### Theorem 41.2: Low-Mode Plus Tail Closes The Residual Bound

Assume `P30-BRIDGE-INV-LOWTAIL(L,C_L,Omega_L,r_L,kappa)`.  If
$$
2(C_L+r_L)+(\Omega_L+r_L)^2/4<M_{\mathrm{sgn}}(\kappa),
$$
then `P23-RPF-TRANS0` holds.

Proof.

The projected estimate plus the tail estimate gives
`P30-BRIDGE-INV-XRATIO(C_L+r_L,Omega_L+r_L,kappa)`.  Apply Theorem 38.4.
`square`

### Proposition 41.3: Current Corpus Does Not Prove The Projected Route

The current corpus does not prove
`P30-BRIDGE-INV-LOWTAIL(L,C_L,Omega_L,r_L,kappa)` in a closing range.

Proof.

Paper 28 proves that projected low-mode operators are legitimate finite
objects but that the current corpus supplies no strict low-mode spectral
value and no same-law Peter-Weyl tail.  Paper 29 strengthens this by showing
that the Paper-26 RN-MIXAMP ratios do not determine the low-mode transition
matrix: endpoint-additive terms cancel from mixed ratios while changing
conditional weights.  The present projected involution defect is a narrower
functional, but it is still a finite conditional value of the same unretained
actual residual.  No paper prints the projected matrix entries or the tail
needed in Definition 41.1. `square`

We record:
$$
\boxed{
\mathrm{P30\text{-}BRIDGE\text{-}INV\text{-}LOWTAIL\text{-}GAP}.
}
$$

## 42. Lower-Floor Witness For The Same Defect

A failed upper-bound route is not a falsification.  To close the negative
side one must print a witness showing that the actual residual defect forces
the RPF predebit above the Branch-A threshold.

### Definition 42.1: Involution-Defect Witness

`P30-BRIDGE-INV-DEFECT-WIT(M_*)` asserts that the maximal involution defect
comes with a cofinal witness consisting of:

1. a finite sequence of endpoint and blanket variations realizing a nonzero
   residual involution orbit;
2. a sign-coherence certificate showing that the realized defect adds to the
   RPF predebit rather than cancelling in the signed bridge ledger;
3. normalizer, retained-row, HK-symmetric, and Peter-Weyl tail survival
   bounds;
4. the same-law lower bound
   $$
   \overline\Lambda_{13}^{RPF}\ge M_*.
   $$

### Lemma 42.2: Witness Implies Lower Floor

`P30-BRIDGE-INV-DEFECT-WIT(M_*)` implies
`P30-BRIDGE-INV-DEFECT-FLOOR(M_*)`.

Proof.

The witness is defined to include exactly the missing data that converts a
surviving residual involution defect into a same-law lower bound on the RPF
predebit.  Items 2 and 3 rule out cancellation and absorption by already
retained accounts; item 4 is the desired floor. `square`

### Proposition 42.3: Current Corpus Does Not Prove The Witness

The current corpus does not prove `P30-BRIDGE-INV-DEFECT-WIT(M_*)`.

Proof.

Proposition 36.3 proves that the lower floor itself is unsourced.  The
witness is stronger: it must identify the realizing residual orbit, prove
sign coherence, and prove survival through normalizers and tails.  None of
those values is printed by Papers 20--30. `square`

We record:
$$
\boxed{
\mathrm{P30\text{-}BRIDGE\text{-}INV\text{-}DEFECT\text{-}WIT\text{-}GAP}.
}
$$

## 43. Residual-Defect Bound Campaign Verdict

### Theorem 43.1: The Residual-Defect Bound Is Now Sharp

The exact residual-defect bound needed by Paper 30 is
`P30-BRIDGE-INV-XRATIO(C,Omega,kappa)` with
$$
2C+\Omega^2/4<M_{\mathrm{sgn}}(\kappa).
$$
It can be sourced by any of the following same-law inputs:

1. a maximal-defect KP theorem satisfying Corollary 39.5;
2. an involution-defect Dobrushin/activity theorem satisfying Theorem 40.3;
3. a projected low-mode plus tail theorem satisfying Theorem 41.2.

The opposite falsification route is the witness theorem
`P30-BRIDGE-INV-DEFECT-WIT(M_*)`, hence the lower floor.

Proof.

Theorem 38.4 proves the sharp cross-ratio closure theorem.  Corollary 39.5,
Theorem 40.3, and Theorem 41.2 are the three positive sourcing routes.
Lemma 42.2 is the negative floor route. `square`

### Corollary 43.2: Current-Corpus Status

Papers 20--30 do not prove any of the closing residual-defect sources above
and do not prove the lower-floor witness.  The active Paper-30 frontier is
therefore
$$
\boxed{
\begin{gathered}
\mathrm{P30\text{-}BRIDGE\text{-}INV\text{-}XRATIO}
\quad\text{or}\quad
\mathrm{P30\text{-}BRIDGE\text{-}INV\text{-}DEFECT\text{-}DOB}\\
\quad\text{or}\quad
\mathrm{P30\text{-}BRIDGE\text{-}INV\text{-}LOWTAIL}
\quad\text{or}\quad
\mathrm{P30\text{-}BRIDGE\text{-}INV\text{-}DEFECT\text{-}WIT}.
\end{gathered}
}
$$

This is not a request for more canonical labels.  It is a request for
same-law value information about the actual adaptive `SEL2` residual defect:
mixed cross-ratios, defect influence/activity, projected low-mode entries
with a tail, or a sign-coherent lower-floor witness.

## 44. What Counts As Proving Or Falsifying A Source Route

The three sourcing mechanisms in Theorem 43.1 are sufficient routes, not
definitions of the physical law.  We therefore separate three statuses.

### Definition 44.1: Route Status

For a Paper-30 source route \({\mathfrak R}\):

1. \({\mathfrak R}\) is **proved by the current corpus** if Papers 20--30
   prove its hypotheses on the actual adaptive `SEL2` law in a closing
   numerical range.
2. \({\mathfrak R}\) is **falsified as a current-corpus derivation** if the
   already closed ledgers admit same-record completions preserving all
   printed finite tables, symmetries, cancellations, and scalar bookkeeping
   while making \({\mathfrak R}\) fail.
3. \({\mathfrak R}\) is **globally falsified** only if one proves that the
   actual adaptive `SEL2` Yang-Mills law cannot satisfy \({\mathfrak R}\).

Only the first status would prove confinement through Paper 30.  The second
status says the route cannot be extracted from the existing work.  The third
would require new information about the actual measure or a lower-floor
witness; absence of a proof is not enough.

### Lemma 44.2: Residual-Tail Completions Are Legitimate Derivation Tests

The residual-tail countermodel family used in Papers 23, 26, 29, and the
present paper is a legitimate test for current-corpus derivability.

Proof.

The family preserves exactly the data already closed by the corpus: finite
record labels, canonical representatives, local and endpoint-additive
removals, BC/CE rows, covariance, conjugation/reflection/duality labels,
HKSD tangent zeroes, quotient rows, and already printed value intervals.  It
changes only unretained same-record RPF residual values.  Therefore any
theorem derived solely from the closed ledgers must hold uniformly across
this family.  If a proposed route can be made to fail inside the family, the
route is not a consequence of the current corpus. `square`

This lemma does not assert that the countermodel is the physical Yang-Mills
law.  It asserts the Barandes-aligned no-smuggling point: the current
stochastic record data do not determine the missing actual residual values.

## 45. Route I: Maximal-Defect KP

The first route is the maximal involution-defect KP theorem
`P30-BRIDGE-INV-DEFECT-KP(B,a,epsilon)`.

### Proposition 45.1: KP Is Not Proved By The Current Corpus

Papers 20--30 do not prove `P30-BRIDGE-INV-DEFECT-KP(B,a,epsilon)` in a
closing range.

Proof.

The proof is the signed-involution specialization of Paper 29 Proposition
19.1.  Paper 29 shows that the maximal retained class and the formal defect
identity do not populate the connected defect activities or their KP norm.
Sections 38--39 of this paper define the sharper involution defect, but the
definition does not print the activity values \(w_\Gamma^{\iota,N,j}\).  The
closed finite tables identify which rows are removed; they do not evaluate
the unretained actual residual cumulants.  Hence no bound
$$
\sup_x
\sum_{\Gamma\ni x}
e^{a\,{\rm diam}(\Gamma)}
|w_\Gamma^{\iota,N,j}|
\le B+\epsilon_j
$$
is proved. `square`

### Proposition 45.2: KP Is Falsified As A Current-Corpus Derivation

For every proposed closing KP datum \((B,a)\), the current closed ledgers
admit same-record residual-tail completions preserving all printed Paper
20--30 data while violating
`P30-BRIDGE-INV-DEFECT-KP(B,a,epsilon)`.

Proof.

Choose an unretained connected residual support \(\Gamma_m\) in the maximal
involution defect, with diameter and size larger than the finite supports
seen by the closed row tables.  Add a same-record term
$$
\delta_m\,\prod_{z\in\Gamma_m} \xi_z
$$
to the unretained residual defect, with the sign chosen so that it is not
cancelled by the chosen involution orbit.  The coefficient can be chosen
small enough to preserve every already printed bounded finite row interval
and all local/endpoint/BC/CE/HKSD zero ledgers, because those ledgers do not
evaluate this unretained connected cumulant.  But for any fixed proposed
\((B,a)\), choose \(\Gamma_m\) and \(\delta_m\) so that
$$
e^{a\,{\rm diam}(\Gamma_m)}|\delta_m|>B+1.
$$
Then the weighted KP activity norm exceeds the proposed bound.  Therefore
the KP source is not derivable from the current corpus. `square`

### Corollary 45.3: KP Is Not Globally Falsified

The current corpus does not globally falsify the maximal-defect KP route.

Proof.

Proposition 45.2 falsifies only derivability from the already printed data.
It does not compute the actual adaptive `SEL2` law.  The true law could still
satisfy a KP theorem by an unprinted same-law analytic estimate, just as it
could fail and instead supply a lower-floor witness.  The present corpus
proves neither. `square`

Route-I verdict:
$$
\boxed{
\begin{gathered}
\text{maximal-defect KP is not proved by Papers 20--30;}\\
\text{it is falsified as a current-corpus derivation;}\\
\text{it is not globally falsified as a possible future same-law theorem.}
\end{gathered}
}
$$

## 46. Route II: Involution-Defect Dobrushin And Activity

The second route is
`P30-BRIDGE-INV-DEFECT-DOB(q,a,B)`.

### Proposition 46.1: Dobrushin/Activity Is Not Proved By The Current Corpus

Papers 20--30 do not prove
`P30-BRIDGE-INV-DEFECT-DOB(q,a,B)` in a closing range.

Proof.

The route requires the finite conditional kernels
\(\mu_x^{\iota,def,N,j}(\cdot\mid\zeta)\), the influence matrix
\(I_{xy}^{\iota,def,N,j}\), and the local activity normalization \(B\).
Paper 29 Proposition 24.1 proves the corresponding defect Dobrushin matrix is
not printed for the primitive defect.  Section 40 of this paper narrows the
object to the involution defect, but again does not print the conditional
probabilities.  A Dobrushin row is a value theorem about the actual finite
conditional law, not a consequence of knowing the row labels. `square`

### Proposition 46.2: Dobrushin/Activity Is Falsified As A Current-Corpus
Derivation

For every proposed closing datum \((q,a,B)\) with \(q<1\), the current closed
ledgers admit same-record completions preserving all printed Paper 20--30
data while violating `P30-BRIDGE-INV-DEFECT-DOB(q,a,B)`.

Proof.

Use the residual-tail completion of Lemma 44.2 on a chain of unretained
defect records \(x=z_0,z_1,\ldots,z_m=y\), or on a distant family connected
through one unretained bridge interaction.  Add a bounded same-record
interaction
$$
\delta\,\xi_x\xi_y
$$
or its finite-chain analogue to the maximal involution defect, supported
outside every already printed value table.  The closed ledgers do not
evaluate this interaction.  It changes the conditional law at \(x\) when the
boundary at \(y\) is flipped by a total-variation amount bounded below by a
positive finite-state constant \(c|\delta|\) on an essential-support event.
Thus the weighted row sum contains
$$
c|\delta|\,e^{a d_{\iota,def}(x,y)}.
$$
Choose the distance or multiplicity so that this term exceeds \(q\), and
choose \(\delta\) within the residual-tail freedom left by the closed
ledgers.  Hence the strict Dobrushin row is not derivable.  The same
completion can also make the local activity normalization exceed a proposed
closing \(B\), so the full Dobrushin/activity route is not derivable either.
`square`

### Corollary 46.3: Dobrushin/Activity Is Not Globally Falsified

The current corpus does not globally falsify the involution-defect
Dobrushin/activity route.

Proof.

The countercompletion proves non-derivability from current data.  It does not
show that the actual adaptive Yang-Mills law has no strict influence row.
Nor does failure of a Dobrushin sufficient criterion imply the lower floor;
Paper 29 Corollary 24.2 proves the analogous point for the primitive defect.
Therefore the true law remains undecided without new conditional values or a
floor witness. `square`

Route-II verdict:
$$
\boxed{
\begin{gathered}
\text{involution-defect Dobrushin/activity is not proved by Papers 20--30;}\\
\text{it is falsified as a current-corpus derivation;}\\
\text{it is not globally falsified as a possible future same-law theorem.}
\end{gathered}
}
$$

## 47. Route III: Projected Low-Mode Plus Tail

The third route is
`P30-BRIDGE-INV-LOWTAIL(L,C_L,Omega_L,r_L,kappa)`.

### Proposition 47.1: Low-Mode Plus Tail Is Not Proved By The Current Corpus

Papers 20--30 do not prove
`P30-BRIDGE-INV-LOWTAIL(L,C_L,Omega_L,r_L,kappa)` in a closing range.

Proof.

The route requires the projected defect matrix entries and a same-law tail
bound for the omitted Peter-Weyl complement.  Paper 28 proves that projected
low-mode operators are finite but that the current corpus proves only the
trivial non-expansion estimate and no same-law Peter-Weyl tail table.  Paper
29 proves that RN-MIXAMP ratios do not determine low-mode matrix entries,
because endpoint-additive terms cancel from mixed ratios while changing
conditional weights.  Section 41 of this paper applies the same issue to the
involution defect.  No paper prints \(C_L\), \(\Omega_L\), or \(r_L\) in a
closing range. `square`

### Proposition 47.2: Low-Mode Plus Tail Is Falsified As A Current-Corpus
Derivation

For every proposed closing datum \((L,C_L,\Omega_L,r_L)\), the current closed
ledgers admit same-record residual-tail completions preserving all printed
Paper 20--30 data while violating
`P30-BRIDGE-INV-LOWTAIL(L,C_L,Omega_L,r_L,kappa)`.

Proof.

There are two independent completions.

First, place the unretained residual defect in a Peter-Weyl mode above
cutoff \(L\).  This leaves the projected low-mode table unchanged while
making the omitted tail contribution larger than the proposed \(r_L\).  This
is the same high-mode freedom isolated in Paper 23 Section 55 and Paper 28
Section 3.

Second, place the unretained residual defect inside a nontrivial low-mode
channel that is not evaluated by any already printed value table.  This can
increase the projected mixed cross-ratio or one-line oscillation above the
proposed \(C_L\) or \(\Omega_L\), while preserving the closed finite labels,
symmetries, and endpoint-additive cancellations.  Paper 29's low-entry
non-recovery theorem supplies the key point: the existing RN-ratio and
finite label data do not determine the projected conditional weights.

Therefore the projected low-mode plus tail source is not derivable from the
current corpus. `square`

### Corollary 47.3: Low-Mode Plus Tail Is Not Globally Falsified

The current corpus does not globally falsify the projected low-mode plus tail
route.

Proof.

The actual adaptive law might have a strict low-mode bound and a same-law
Peter-Weyl tail not yet proved in Papers 20--30.  Conversely, it might fail
the projected route and still close through KP, Dobrushin, a direct
cross-ratio estimate, or a signed lower-floor witness.  The current corpus
does not decide which occurs. `square`

Route-III verdict:
$$
\boxed{
\begin{gathered}
\text{projected low-mode plus tail is not proved by Papers 20--30;}\\
\text{it is falsified as a current-corpus derivation;}\\
\text{it is not globally falsified as a possible future same-law theorem.}
\end{gathered}
}
$$

## 48. Three-Route Completion Theorem

### Theorem 48.1: The Three Residual-Defect Source Routes Are Settled For
Paper 30

The three ways to source the residual-defect bound have the following
definite Paper-30 status:

1. maximal-defect KP is conditionally sufficient, not proved by the current
   corpus, and falsified as a current-corpus derivation;
2. involution-defect Dobrushin/activity is conditionally sufficient, not
   proved by the current corpus, and falsified as a current-corpus derivation;
3. projected low-mode plus tail is conditionally sufficient, not proved by
   the current corpus, and falsified as a current-corpus derivation.

None of the three is globally falsified as a possible future theorem about
the actual adaptive `SEL2` law.

Proof.

Conditional sufficiency is Corollary 39.5, Theorem 40.3, and Theorem 41.2.
Non-proof by the current corpus is Propositions 45.1, 46.1, and 47.1.
Falsification as current-corpus derivations is Propositions 45.2, 46.2, and
47.2.  Non-global-falsification is Corollaries 45.3, 46.3, and 47.3.
`square`

### Corollary 48.2: What Remains After The Three-Route Test

Paper 30 has now exhausted the three residual-defect sourcing mechanisms
available from the present corpus.  The only positive continuation inside
adaptive Branch A is one of the following genuinely new same-law inputs:

1. a direct proof of `P30-BRIDGE-INV-XRATIO(C,Omega,kappa)` not passing
   through the three routes above;
2. a new actual conditional value theorem strong enough to prove one of the
   three routes as a theorem about the physical adaptive law;
3. a sign-coherent witness proving `P30-BRIDGE-INV-DEFECT-WIT(M_*)`, hence
   the lower floor;
4. exit from adaptive Branch A to a different branch of the Paper-22
   trichotomy.

More canonical labels, more finite row names, or another quotient table do
not move this obstruction.

## 49. Branch-A-Only Overcoming Principle

We now keep the work inside adaptive Branch A and ask how the three
current-corpus derivation failures can be overcome.  The answer is not to
add labels.  The answer is to add same-law value anchors that make the
residual-tail completions of Lemma 44.2 inadmissible.

### Definition 49.1: Actual-Law Anchor

An actual-law anchor for a residual-defect route is a cofinal finite data
package extracted from the same adaptive `SEL2` pushed-forward scalar law
which prints enough numerical intervals to determine the route quantity:

1. for KP, the connected defect activities and their weighted norm;
2. for Dobrushin/activity, the defect conditional kernels or influence
   matrix and the local activity normalization;
3. for low-mode plus tail, the projected defect matrix/cross-ratio values
   and the same-law Peter-Weyl complement.

The anchor is required to be law-preserving: it is computed from the actual
finite-volume `SEL2` scalar distribution after the same retained rows,
involutions, BC/CE divisions, normalizers, and endpoint removals have been
applied.  It is not a comparison heat-kernel law, not an independent Markov
bridge, and not a continuum substitute.

### Lemma 49.2: Anchors Defeat Current-Corpus Countercompletions

If an actual-law anchor determines the route quantity in a closing interval,
then the residual-tail completions used in Propositions 45.2, 46.2, and 47.2
are no longer admissible countercompletions for that route.

Proof.

The completions of Lemma 44.2 were admissible only because the closed corpus
did not evaluate the unretained residual values.  An actual-law anchor prints
exactly those values, or a certified interval containing them, for the route
quantity.  Any completion changing the route quantity outside the interval
would contradict the new same-law anchor and is therefore not a completion
of the enlarged corpus.  This is the precise sense in which the
current-corpus derivation failure is overcome. `square`

### Lemma 49.3: Branch-A Admissibility Of Anchors

Actual-law anchors are Barandes-aligned and remain inside adaptive Branch A.

Proof.

They add stochastic record data for the same pushed-forward scalar law.
They do not posit hidden ontic states, replace the law by a heat-kernel
surrogate, introduce an external continuum Yang-Mills measure, or change the
Branch-A selector.  They merely evaluate finite conditional quantities of
the already declared law. `square`

## 50. Overcoming Route I: KP Activity Anchor

### Definition 50.1: KP Activity Anchor

`P30-BRANCHA-KP-ANCHOR(B,a,epsilon)` asserts that, cofinally, the maximal
involution defect \(D_{\iota,max}^{N,j}\) has its actual connected
same-law activities printed in interval form:
$$
w_\Gamma^{\iota,N,j}\in{\mathfrak I}_\Gamma^{N,j},
$$
with interval widths summing to at most \(\epsilon_j\to0\), and with the
certified weighted activity bound
$$
\sup_x
\sum_{\Gamma\ni x}
e^{a\,{\rm diam}(\Gamma)}
\sup_{w\in{\mathfrak I}_\Gamma^{N,j}}|w|
\le B+\epsilon_j.
$$
The intervals are obtained from the actual finite-volume adaptive `SEL2`
conditional law after the maximal retained class of Definition 39.1 has
been subtracted.

### Lemma 50.2: KP Anchor Implies Defect KP

`P30-BRANCHA-KP-ANCHOR(B,a,epsilon)` implies
`P30-BRIDGE-INV-DEFECT-KP(B,a,epsilon)`.

Proof.

Definition 50.1 prints the same activities required in Definition 39.3 and
certifies the same weighted activity norm.  The interval-width sum is the
cofinal error term \(\epsilon_j\). `square`

### Theorem 50.3: KP Anchor Overcomes Route-I Non-Derivability

Assume `P30-BRANCHA-KP-ANCHOR(B,a,epsilon)`.  Then the Route-I
current-corpus derivation failure of Proposition 45.2 is overcome.  If,
after absorbing the cofinal error,
$$
4B e^{-a d_{br}}+B^2<M_{\mathrm{sgn}}(\kappa),
$$
then `P23-RPF-TRANS0` holds.

Proof.

By Lemma 50.2 the KP route is now proved by the enlarged same-law corpus, so
the residual-tail completions that changed \(w_\Gamma^{\iota,N,j}\) are
excluded by Lemma 49.2.  Corollary 39.5 then closes the signed route under
the displayed inequality. `square`

We record the Branch-A KP overcoming package:
$$
\boxed{
\mathrm{P30\text{-}BRANCHA\text{-}KP\text{-}ANCHOR}
(B,a,\epsilon)
\quad+\quad
4B e^{-a d_{br}}+B^2<M_{\mathrm{sgn}}(\kappa).
}
$$

## 51. Overcoming Route II: Dobrushin/Activity Anchor

### Definition 51.1: Dobrushin/Activity Anchor

`P30-BRANCHA-DOB-ANCHOR(q,a,B)` asserts that, cofinally, the actual
involution-defect conditional kernels of Definition 40.1 are printed, or
printed to certified intervals, in a form that yields interval upper bounds
\({\mathfrak J}_{xy}^{N,j}\) for the influences:
$$
I_{xy}^{\iota,def,N,j}\le {\mathfrak J}_{xy}^{N,j},
$$
with
$$
\sup_x\sum_y e^{a d_{\iota,def}(x,y)}
{\mathfrak J}_{xy}^{N,j}
\le q<1,
$$
and with the local defect activity normalization bounded by \(B\).  All
kernels and normalizers are computed from the same actual adaptive `SEL2`
law after the same retained rows and involution split are applied.

### Lemma 51.2: Dobrushin Anchor Implies The Dobrushin Source

`P30-BRANCHA-DOB-ANCHOR(q,a,B)` implies
`P30-BRIDGE-INV-DEFECT-DOB(q,a,B)`.

Proof.

Definition 51.1 directly supplies the weighted influence row bound and the
activity normalization required by Definition 40.2. `square`

### Theorem 51.3: Dobrushin Anchor Overcomes Route-II Non-Derivability

Assume `P30-BRANCHA-DOB-ANCHOR(q,a,B)`.  Then the Route-II current-corpus
derivation failure of Proposition 46.2 is overcome.  If the induced
Dobrushin-Shlosman constants \((B',a')=(B'(q,a,B),a'(q,a,B))\) satisfy
$$
4B'e^{-a'd_{br}}+(B')^2<M_{\mathrm{sgn}}(\kappa),
$$
then `P23-RPF-TRANS0` holds.

Proof.

The influence and activity intervals exclude the residual-tail completions
that changed the conditional kernels or the activity normalization in
Proposition 46.2.  Thus the route is no longer merely an unsupported
derivation; it is an anchored same-law theorem.  Lemma 51.2 gives
`P30-BRIDGE-INV-DEFECT-DOB(q,a,B)`, Theorem 40.3 gives the KP constants, and
Corollary 39.5 closes the signed route under the displayed inequality.
`square`

We record the Branch-A Dobrushin overcoming package:
$$
\boxed{
\mathrm{P30\text{-}BRANCHA\text{-}DOB\text{-}ANCHOR}(q,a,B)
\quad+\quad
4B'e^{-a'd_{br}}+(B')^2<M_{\mathrm{sgn}}(\kappa).
}
$$

## 52. Overcoming Route III: Low-Mode/Tail Anchor

### Definition 52.1: Low-Mode/Tail Anchor

`P30-BRANCHA-LOWTAIL-ANCHOR(L,C_L,Omega_L,r_L,kappa)` asserts that,
cofinally, the actual projected involution defect
$$
D_{\iota,L}^{N,j}=\Pi_{\le L}D_{\iota,max}^{N,j}\Pi_{\le L}
$$
is printed in interval form on the endpoint and blanket records needed for
the signed bridge functional, with certified bounds
$$
{\mathcal C}_{\iota,L}^{cof}\le C_L,
\qquad
{\mathcal O}_{\iota,L}^{cof}\le\Omega_L,
$$
and that the same actual law supplies a Peter-Weyl complement estimate
$$
\|(1-\Pi_{\le L})D_{\iota,max}^{N,j}\|_{br}\le r_L
$$
in the mixed-cross-ratio and one-line norm used by Definition 41.1.  The
common minimal-edge tail `P23-RPF-MIN-KTAIL(kappa)` is also included.

### Lemma 52.2: Low-Mode Anchor Implies Low-Tail Source

`P30-BRANCHA-LOWTAIL-ANCHOR(L,C_L,Omega_L,r_L,kappa)` implies
`P30-BRIDGE-INV-LOWTAIL(L,C_L,Omega_L,r_L,kappa)`.

Proof.

Definition 52.1 prints exactly the projected bounds and complement estimate
required in Definition 41.1. `square`

### Theorem 52.3: Low-Mode/Tail Anchor Overcomes Route-III
Non-Derivability

Assume `P30-BRANCHA-LOWTAIL-ANCHOR(L,C_L,Omega_L,r_L,kappa)`.  Then the
Route-III current-corpus derivation failure of Proposition 47.2 is overcome.
If
$$
2(C_L+r_L)+(\Omega_L+r_L)^2/4<M_{\mathrm{sgn}}(\kappa),
$$
then `P23-RPF-TRANS0` holds.

Proof.

The projected intervals exclude the low-mode completion of Proposition 47.2,
and the complement bound excludes the high-mode tail completion.  Lemma 52.2
gives the low-tail source, and Theorem 41.2 closes the signed route under
the displayed inequality. `square`

We record the Branch-A low-mode/tail overcoming package:
$$
\boxed{
\mathrm{P30\text{-}BRANCHA\text{-}LOWTAIL\text{-}ANCHOR}
(L,C_L,\Omega_L,r_L,\kappa)
\quad+\quad
2(C_L+r_L)+(\Omega_L+r_L)^2/4<M_{\mathrm{sgn}}(\kappa).
}
$$

## 53. Branch-A Overcoming Theorem For The Three Cases

### Theorem 53.1: The Three Current-Corpus Failures Can Be Overcome Without
Leaving Branch A

Each of the three route failures can be overcome inside adaptive Branch A by
adding the corresponding actual-law anchor:

1. `P30-BRANCHA-KP-ANCHOR` overcomes the maximal-defect KP failure;
2. `P30-BRANCHA-DOB-ANCHOR` overcomes the involution-defect
   Dobrushin/activity failure;
3. `P30-BRANCHA-LOWTAIL-ANCHOR` overcomes the projected low-mode/tail
   failure.

If any one of the three anchors satisfies its displayed closing inequality,
then `P23-RPF-TRANS0` holds.

Proof.

The overcoming statements are Theorems 50.3, 51.3, and 52.3.  The closure
statements are the last sentences of those theorems.  Each anchor is
law-preserving by Definition 49.1 and Branch-A admissible by Lemma 49.3.
`square`

### Corollary 53.2: What Paper 30 Has And Has Not Done

Paper 30 has now converted the non-derivability obstruction into three
precise Branch-A same-law data tasks.  It has not pretended that Papers
20--30 already contain those data.  The next positive work, still inside
Branch A, is therefore to print at least one of:
$$
\boxed{
\begin{gathered}
\mathrm{P30\text{-}BRANCHA\text{-}KP\text{-}ANCHOR},\\
\mathrm{P30\text{-}BRANCHA\text{-}DOB\text{-}ANCHOR},\\
\mathrm{P30\text{-}BRANCHA\text{-}LOWTAIL\text{-}ANCHOR}.
\end{gathered}
}
$$

The residual-tail countermodels no longer block these enlarged tasks,
because the tasks explicitly print the same-law values that the
countermodels were free to vary.

## 54. Actual Anchor Value Audit

We now remove a possible ambiguity in Sections 49--53.  The Branch-A anchors
are not values.  They are value tasks.  This section asks whether Paper 30
can actually prove or falsify those values.

### Definition 54.1: Actual Anchor Scalars

For the KP route, define the actual cofinal KP scalar
$$
{\mathcal K}_{\iota}(a)
:=
\limsup_{(N,j)}
\sup_x
\sum_{\Gamma\ni x}
e^{a\,{\rm diam}(\Gamma)}
|w_\Gamma^{\iota,N,j}|.
$$

For the Dobrushin route, define the actual cofinal influence scalar
$$
{\mathcal D}_{\iota}(a)
:=
\limsup_{(N,j)}
\sup_x\sum_y e^{a d_{\iota,def}(x,y)}
I_{xy}^{\iota,def,N,j},
$$
and let \({\mathcal B}_{\iota}\) denote the corresponding cofinal local
defect activity normalization.

For the low-mode/tail route, define
$$
{\mathcal L}_{\iota}(L)
:=
\limsup_{(N,j)}
{\mathcal C}_{\iota,L}^{N,j},
\qquad
{\mathcal W}_{\iota}(L)
:=
\limsup_{(N,j)}
{\mathcal O}_{\iota,L}^{N,j},
\qquad
{\mathcal R}_{\iota}(L)
:=
\limsup_{(N,j)}
r_L^{N,j}.
$$

These are the values the anchors would have to bound.  They are not
introduced as assumptions; they name the actual quantities whose values are
missing.

### Proposition 54.2: Paper 30 Does Not Prove The Anchor Values

Papers 20--30 do not prove closing numerical bounds for
\({\mathcal K}_{\iota}(a)\), \({\mathcal D}_{\iota}(a)\) together with
\({\mathcal B}_{\iota}\), or
\(({\mathcal L}_{\iota}(L),{\mathcal W}_{\iota}(L),{\mathcal R}_{\iota}(L))\).

Proof.

For KP, Proposition 45.1 proves that the connected activities are not
printed.  For Dobrushin/activity, Proposition 46.1 proves that the defect
conditional kernels, influence row, and activity normalization are not
printed.  For low-mode/tail, Proposition 47.1 proves that neither the
projected entries nor the Peter-Weyl complement are printed.  Definitions
50.1, 51.1, and 52.1 specify what would have to be printed, but do not print
it. `square`

### Proposition 54.3: Paper 30 Does Not Falsify The Anchor Values

Papers 20--30 do not prove that the actual anchor values fail every closing
range.

Proof.

To falsify KP one would need a same-law lower bound showing that
\({\mathcal K}_{\iota}(a)\) exceeds every closing \(B\), or that no \(a\)
can make the KP margin close.  No such lower bound is printed.  To falsify
Dobrushin/activity one would need a same-law proof that
\({\mathcal D}_{\iota}(a)\ge1\) for every admissible \(a\), or that the
activity normalization necessarily violates every closing margin.  Paper 29
Corollary 24.2 already warns that failure of a Dobrushin sufficient test is
not a lower floor, and the present paper has not even proved such failure
for the actual law.  To falsify low-mode/tail one would need a same-law
lower bound on every projected mixed range or on the Peter-Weyl complement
large enough to violate the signed margin.  No such lower bound is printed.

Thus the current corpus does not prove the anchors, but it also does not
falsify them as statements about the actual adaptive law. `square`

### Theorem 54.4: Anchor Values Are Undecided By The Current Corpus

The current corpus neither proves nor falsifies the three anchor value
packages.  More precisely, the closed ledgers are compatible with same-record
residual completions in which the anchor quantities are small enough to pass
their route and also with same-record residual completions in which they are
large enough to fail.

Proof.

The failure completions are those used in Propositions 45.2, 46.2, and 47.2:
add unretained connected activities, long-range influence, or high/low
Peter-Weyl residual pieces while preserving all printed finite labels,
symmetries, removals, and value intervals.

For pass completions, set the unretained maximal involution defect to zero,
or to an arbitrarily small same-record residual supported only in already
admissible unretained rows.  This preserves the same closed ledgers because
the closed corpus never printed those unretained values.  The KP activity
norm, Dobrushin influence contribution, and projected/tail contribution can
therefore be made arbitrarily small inside the completion family.

Since both pass-like and fail-like completions preserve the already printed
data, the current corpus cannot decide the actual anchor values.  This is a
non-identifiability theorem for the existing records, not a statement that
the physical adaptive Yang-Mills law is arbitrary. `square`

### Corollary 54.5: Specific Task Verdict

The request "prove or falsify the anchor values" has the following honest
Paper-30 resolution:

1. the anchor values are not proven;
2. the anchor values are not falsified;
3. their decidability from Papers 20--30 is falsified;
4. proving or falsifying them requires new same-law quantitative information
   about the actual adaptive `SEL2` residual law.

In symbols, Paper 30 proves
$$
\boxed{
\begin{gathered}
\mathrm{NOT\ PROVED:}\quad
\mathrm{P30\text{-}BRANCHA\text{-}KP\text{-}ANCHOR},
\ \mathrm{P30\text{-}BRANCHA\text{-}DOB\text{-}ANCHOR},
\ \mathrm{P30\text{-}BRANCHA\text{-}LOWTAIL\text{-}ANCHOR},\\
\mathrm{NOT\ FALSIFIED:}\quad
\mathrm{P30\text{-}BRANCHA\text{-}KP\text{-}ANCHOR},
\ \mathrm{P30\text{-}BRANCHA\text{-}DOB\text{-}ANCHOR},
\ \mathrm{P30\text{-}BRANCHA\text{-}LOWTAIL\text{-}ANCHOR},\\
\mathrm{FALSIFIED:}\quad
\text{their derivability or refutability from the current closed corpus.}
\end{gathered}
}
$$

This is the strongest rigorous conclusion available inside Paper 30 without
printing new actual finite-volume conditional data.

## 55. First New Same-Law Quantitative Information: Finite-DLR Ranges

We now extract the first actual quantitative information that is genuinely
same-law.  It is not yet a closing estimate, but it is not invented: it is
computed from the exact finite DLR density of Section 11.

### Definition 55.1: Heat-Kernel Range Profile

For \(G=SU(N)\) and heat time \(t>0\), define
$$
\mathsf r_{HK}^{N}(t)
:=
\log
{ \sup_{U\in G} H_t(U)\over \inf_{U\in G} H_t(U) }.
$$
For a finite parent region \(B\), define
$$
\mathsf R_{HK}^{N,j}(B)
:=
\sum_{p\cap B\ne\varnothing}\mathsf r_{HK}^{N}(t_p).
$$
Define also
$$
\mathsf R_{Jac}^{N,j}(B)
:=
\operatorname{osc}_{B}\log J_{tree},
\qquad
\mathsf R_{RPF}^{N,j}(B)
:=
\operatorname{osc}_{B}V_{RPF},
$$
and the finite DLR range envelope
$$
\mathsf R_{DLR}^{N,j}(B)
:=
\mathsf R_{HK}^{N,j}(B)
\,+\,
\mathsf R_{Jac}^{N,j}(B)
\,+\,
\mathsf R_{RPF}^{N,j}(B).
$$

All oscillations are taken on the actual finite parent DLR chart used in
Definition 11.2, after the same `BC/CE`, retained-row, and tree-gauge
conventions have been applied.

### Lemma 55.2: The Range Profile Is Same-Law And Finite At Fixed
\((N,j)\)

For every fixed finite \((N,j)\), \(\mathsf R_{DLR}^{N,j}(B)<\infty\) on
every finite parent region \(B\).

Proof.

The compact group \(SU(N)\) is compact.  For \(t>0\), the heat kernel
\(H_t\) is continuous and strictly positive, so its supremum and infimum are
finite and positive.  The tree-gauge Jacobian and the finite residual
potential are finite functions on the finite chart on every admissible
essential-support cell.  Thus each range term is finite.  All terms are
computed from the actual finite DLR density, not from a comparison law.
`square`

### Definition 55.3: Boundary Log-Ratio Envelope

For two parent boundary conditions \(\eta,\eta'\), define
$$
\Delta_{DLR}^{N,j}(B;\eta,\eta')
:=
\operatorname{osc}_{g\in B}
\log
{dK_{B}^{par}(g\mid\eta)\over dK_{B}^{par}(g\mid\eta')}.
$$
By Lemma 21.2, the normalizer does not increase this oscillation.  Hence
\(\Delta_{DLR}^{N,j}\) is bounded by the oscillation of the unnormalized
finite DLR Hamiltonian difference.

### Lemma 55.4: DLR Range Gives Conditional Influence

Let \(\mu\) and \(\nu\) be two finite conditionals whose log-density ratio
has oscillation at most \(\Delta\).  Then
$$
\|\mu-\nu\|_{\rm TV}\le \tanh(\Delta/4).
$$
Consequently, for every defect coordinate pair \(x,y\),
$$
I_{xy}^{\iota,def,N,j}
\le
\tanh\left({\Delta_{xy}^{DLR,N,j}\over4}\right),
$$
where \(\Delta_{xy}^{DLR,N,j}\) is the worst DLR boundary log-ratio
oscillation caused at \(x\) by changing the \(y\)-record boundary.

Proof.

If \(d\mu/d\nu=e^F/Z\) and \(\operatorname{osc}F\le\Delta\), then the
likelihood ratio \(d\mu/d\nu\) lies in an interval of multiplicative width
at most \(e^\Delta\).  The maximal total variation over such likelihood
ratios is attained by a two-level ratio and equals
\((e^{\Delta/2}-1)/(e^{\Delta/2}+1)=\tanh(\Delta/4)\).  Apply this to the
two defect conditionals. `square`

This is the first hard quantitative object actually found in Paper 30:
the Dobrushin row has a same-law finite-DLR upper envelope
$$
\boxed{
{\mathcal D}_{\iota}(a)
\le
\limsup_{(N,j)}
\sup_x\sum_y e^{a d_{\iota,def}(x,y)}
\tanh\left({\Delta_{xy}^{DLR,N,j}\over4}\right).
}
$$

## 56. DLR Range Envelopes For The Three Anchors

The finite-DLR range profile also gives explicit same-law envelopes for the
KP and projected low-mode routes.

### Definition 56.1: Möbius Range Envelope

For an unretained residual atom \(A\), let \(B(A)\) be its finite parent DLR
support.  Define
$$
\mathsf M_A^{N,j}
:=
2^{|A|}\mathsf R_{DLR}^{N,j}(B(A)).
$$

The factor \(2^{|A|}\) is the cost of the finite alternating Möbius
projection over the coordinates of \(A\).

### Lemma 56.2: Möbius Range Bounds The Literal Defect Activity

For every unretained residual atom \(A\),
$$
|\Phi_A^{\iota,N,j}|\le \mathsf M_A^{N,j}
$$
in oscillation norm.

Proof.

The atom \(\Phi_A^{\iota,N,j}\) is an alternating sum of at most \(2^{|A|}\)
restrictions of the same finite DLR log-density contribution.  Each
restriction has oscillation bounded by \(\mathsf R_{DLR}^{N,j}(B(A))\).
The triangle inequality gives the displayed envelope. `square`

### Corollary 56.3: Same-Law KP Envelope

The actual KP scalar satisfies the same-law upper envelope
$$
{\mathcal K}_{\iota}(a)
\le
\limsup_{(N,j)}
\sup_x
\sum_{A\ni x}
e^{a\,{\rm diam}(A)}
\mathsf M_A^{N,j},
$$
provided the connected activity model is taken to be the literal finite
Möbius interaction expansion of the maximal defect.

Proof.

Use Lemma 56.2 in the weighted activity norm. `square`

### Definition 56.4: Projected DLR Coefficient Tail

Let \(\widehat D_{\iota,max}^{N,j}(\lambda,\mu)\) denote the finite
Peter-Weyl coefficients of \(D_{\iota,max}^{N,j}\) in the endpoint and
blanket variables used by the signed bridge functional.  Define the exact
same-law projected/tail quantities
$$
\mathsf C_{\iota,L}^{DLR}
:=
\limsup_{(N,j)}{\mathcal C}_{\iota,L}^{N,j},
\qquad
\mathsf W_{\iota,L}^{DLR}
:=
\limsup_{(N,j)}{\mathcal O}_{\iota,L}^{N,j},
$$
and
$$
\mathsf T_{\iota,L}^{DLR}
:=
\limsup_{(N,j)}
\left\|
\sum_{\max(\lambda,\mu)>L}
\widehat D_{\iota,max}^{N,j}(\lambda,\mu)
\right\|_{br}.
$$

The norm is the mixed-cross-ratio and one-line bridge norm of Definition
41.1.

### Lemma 56.5: DLR Coefficients Give The Low-Mode/Tail Anchor Values

If the finite DLR coefficient table in Definition 56.4 is printed with
certified intervals, then
`P30-BRANCHA-LOWTAIL-ANCHOR` holds with
$$
C_L=\mathsf C_{\iota,L}^{DLR},
\qquad
\Omega_L=\mathsf W_{\iota,L}^{DLR},
\qquad
r_L=\mathsf T_{\iota,L}^{DLR}.
$$

Proof.

These are exactly the projected bridge range, one-line width, and omitted
Peter-Weyl complement of Definition 52.1. `square`

## 57. Why The Found Quantitative Information Does Not Yet Close

The finite-DLR envelopes are real same-law quantitative information.  The
coarse version is nevertheless too weak to close the continuum Branch-A
gate without additional cancellation, derivative, or coefficient decay.

### Lemma 57.1: Heat-Kernel Range Diverges In The Small-Time Limit

For nontrivial compact connected \(SU(N)\),
$$
\mathsf r_{HK}^{N}(t)\to\infty
\qquad\text{as }t\downarrow0.
$$

Proof.

The heat kernel \(H_t(e)\) has the usual small-time on-diagonal blowup, while
for any fixed \(U\ne e\) away from the identity cut locus contribution,
\(H_t(U)\to0\).  Hence the ratio between the maximum and the minimum over
the compact group diverges. `square`

### Proposition 57.2: Crude DLR Range Does Not Prove A Closing Anchor

The envelopes of Sections 55--56 do not, by themselves, prove any of
`P30-BRANCHA-KP-ANCHOR`, `P30-BRANCHA-DOB-ANCHOR`, or
`P30-BRANCHA-LOWTAIL-ANCHOR` in a closing range.

Proof.

For KP, the Möbius envelope contains the heat-kernel range
\(\mathsf r_{HK}^{N}(t_p)\) and the residual/Jacobian ranges.  Lemma 57.1
shows that the heat-kernel range has no small-time cofinal boundedness from
range control alone.  Thus the weighted KP bound obtained from
\(\mathsf M_A^{N,j}\) is a finite upper bound at fixed \((N,j)\), but not a
closing cofinal bound.

For Dobrushin, Lemma 55.4 gives
\(\tanh(\Delta/4)\).  When the crude DLR oscillation \(\Delta\) is large,
this upper bound saturates at \(1\), and the weighted row sum cannot be
forced below one by this estimate alone.

For low-mode/tail, Definition 56.4 gives exact coefficients if computed,
but the range envelope alone gives no decay of the Peter-Weyl complement.
Uniform tail decay requires a derivative, band-limit, heat-kernel smoothing,
or actual coefficient theorem for the residual defect.  None is supplied by
the crude range estimate. `square`

### Corollary 57.3: The New Quantitative Target Is Now Concrete

Paper 30 has found the first same-law quantitative extractor:
finite-DLR ranges, boundary log-ratio envelopes, Möbius activity envelopes,
and exact projected coefficient tails.  The remaining positive task is to
sharpen one of these from a finite but coarse envelope into a closing bound:

1. prove cancellation or connected-cluster improvement in the Möbius envelope
   so that \({\mathcal K}_{\iota}(a)\) satisfies the KP margin;
2. prove a small boundary log-ratio envelope
   \(\sum_y e^{ad}\tanh(\Delta_{xy}^{DLR}/4)<1\);
3. prove same-law Peter-Weyl coefficient decay for
   \(D_{\iota,max}^{N,j}\), so that \(\mathsf T_{\iota,L}^{DLR}\to0\) with
   enough margin.

These are quantitative Branch-A tasks.  They no longer ask for unnamed
"new information"; they identify the finite same-law quantities that must be
estimated.

## 58. Radical Same-Law Search Ledger

The range extractor is real but too crude.  The next pass must therefore
look for same-law information that is weaker than full range but stronger
than pure label bookkeeping.  The following six routes are the live radical
search directions, ordered by expected value:

1. score/covariance response instead of pointwise log-density range;
2. connected Möbius/cumulant cancellation instead of the
   \(2^{|A|}\)-triangle bound;
3. Peter-Weyl heat-flow smoothing plus residual-tail control;
4. finite Schwinger-Dyson/Ward identities for the signed bridge object;
5. transport or entropic contraction instead of total-variation Dobrushin;
6. a sign-coherent lower-floor theorem if positive Branch-A smallness fails.

All six are same-law routes.  None changes the adaptive `SEL2` pushed-forward
scalar law, none replaces the parent finite DLR density by an auxiliary
process, and none imports a continuum Yang-Mills measure as an external
black box.

## 59. Route I: Score/Covariance Response

The first attempt is to replace sup-range by an actual response identity.
Range sees rare heat-kernel spikes.  Conditional influence sees how the
scalar observable responds to a boundary perturbation.

### Definition 59.1: Boundary Score

Fix a finite parent DLR conditional \(K_B^{par}(\cdot\mid\eta)\).  Let
\(\eta_y(s)\) be a smooth one-parameter boundary perturbation supported on
the boundary record \(y\), with \(\eta_y(0)=\eta\).  The centered boundary
score is
$$
\mathcal S_y^{N,j}(g;\eta)
:=
\partial_s\log {dK_B^{par}(g\mid\eta_y(s))\over dg}\Big|_{s=0}
-
E_{K_B^{par}(\cdot\mid\eta)}
\partial_s\log {dK_B^{par}(g\mid\eta_y(s))\over dg}\Big|_{s=0}.
$$

For a scalar defect observable \(F_x\), define the response row
$$
\mathcal I_{xy}^{score,N,j}
:=
\sup_{\eta}
\sup_{\eta_y}
\left|
E_{K_B^{par}(\cdot\mid\eta)}
\left[
\bigl(F_x-EF_x\bigr)\mathcal S_y^{N,j}
\right]
\right|.
$$

### Lemma 59.2: Exact Score/Covariance Identity

For every smooth finite boundary path \(\eta_y(s)\),
$$
\partial_s E_{K_B^{par}(\cdot\mid\eta_y(s))}F_x\Big|_{s=0}
=
\operatorname{Cov}_{K_B^{par}(\cdot\mid\eta)}
\left(F_x,\partial_s\log {dK_B^{par}(g\mid\eta_y(s))\over dg}\Big|_{s=0}
\right).
$$

Proof.

Differentiate the finite density under the integral.  The derivative of the
normalizer subtracts the mean score, leaving the covariance.  All integrals
are finite because the parent region and group are finite and compact.
`square`

### Definition 59.3: Score/Covariance Closing Source

`P30-SCORE-COV-ROW(q,a)` asserts that, on the actual cofinal adaptive law,
$$
\limsup_{(N,j)}
\sup_x
\sum_y e^{a d(x,y)}\mathcal I_{xy}^{score,N,j}
\le q<1.
$$

### Theorem 59.4: Score/Covariance Closes The Dobrushin Anchor

If `P30-SCORE-COV-ROW(q,a)` holds and the boundary perturbation family spans
the retained scalar boundary records used in the defect conditional, then
`P30-BRANCHA-DOB-ANCHOR` holds with Dobrushin row at most \(q\).

Proof.

The scalar conditional variation between two boundary records is obtained by
integrating the infinitesimal response along a boundary path.  Lemma 59.2
identifies the response with the score covariance.  The row bound in
Definition 59.3 gives the weighted Dobrushin row. `square`

### Proposition 59.5: Score/Covariance Is Not Supplied By The Current Corpus

Papers 20--30 do not prove `P30-SCORE-COV-ROW(q,a)` for any closing
\(q<1\).

Proof.

The corpus prints finite DLR densities, retained-row identities, heat-kernel
Schwinger-Dyson cancellations, and the range/log-ratio extractor.  It does
not print a covariance decay theorem, a uniform Poincare/Helffer-Sjostrand
inverse for the conditioned residual law, or a score-energy estimate for the
off-sheet residual RN term.  The range extractor of Section 55 is compatible
with both small and large covariances because it controls only oscillation,
not covariance cancellation. `square`

### Corollary 59.6: Route I Verdict

Route I proves a real same-law identity and a valid closing theorem, but it
does not close from Papers 20--30.  It is falsified as a current-corpus
derivation, not as a possible future theorem about the actual adaptive law.

## 60. Route II: Connected Möbius/Cumulant Cancellation

The second attempt attacks the worst overcount in Section 56: the factor
\(2^{|A|}\) from the triangle inequality.  Möbius atoms are alternating
objects.  They should be bounded by connected mixed derivatives, not by the
full range of every face of the cube.

### Definition 60.1: Interpolation Cube For A Defect Atom

For an atom \(A=\{a_1,\ldots,a_m\}\), choose a reference boundary
\(\eta^{0}\) and an activated boundary \(\eta^{1}\).  Let
\(\eta(\mathbf s)\), \(\mathbf s\in[0,1]^m\), be the finite DLR boundary
interpolation that activates coordinate \(a_i\) when \(s_i\) is increased.
Let \(H_A^{N,j}(\mathbf s)\) be the corresponding centered residual
Hamiltonian contribution.

### Lemma 60.2: Möbius Atom Equals A Mixed-Derivative Integral

For every finite atom \(A\),
$$
\Phi_A^{N,j}
=
\int_{[0,1]^{|A|}}
\partial_{s_1}\cdots\partial_{s_{|A|}}
H_A^{N,j}(\mathbf s)\,d\mathbf s.
$$

Proof.

This is the finite multivariate fundamental theorem of calculus applied to
the alternating cube difference defining the Möbius atom.  The finite DLR
chart is smooth on each admissible essential-support cell; if a cell boundary
is crossed, apply the identity cellwise and sum the finitely many pieces.
`square`

### Definition 60.3: Connected Mixed-Derivative Source

`P30-CONN-MOBIUS(\alpha,a)` asserts that the actual mixed derivatives admit
a connected-tree majorant
$$
\left\|
\partial_{s_1}\cdots\partial_{s_m}H_A^{N,j}(\mathbf s)
\right\|
\le
\sum_{T\text{ tree on }A}
\prod_{\{u,v\}\in T}\alpha_{uv}^{N,j}
$$
with
$$
\limsup_{(N,j)}
\sup_x
\sum_{A\ni x}
e^{a\,{\rm diam}(A)}
\sum_{T\text{ tree on }A}
\prod_{\{u,v\}\in T}\alpha_{uv}^{N,j}
<1.
$$

### Theorem 60.4: Connected Möbius Closes The KP Anchor

`P30-CONN-MOBIUS(\alpha,a)` implies `P30-BRANCHA-KP-ANCHOR`.

Proof.

Insert Lemma 60.2 into the literal connected activity norm.  The tree
majorant in Definition 60.3 bounds every atom by a connected product rather
than by the full cube range.  The displayed weighted sum is exactly the KP
activity bound. `square`

### Proposition 60.5: Connected Möbius Is Not Supplied By The Current Corpus

Papers 20--30 do not prove `P30-CONN-MOBIUS(\alpha,a)` in a closing range.

Proof.

The corpus contains finite support, canonical labels, retained-row
subtractions, and local cancellation ledgers.  It does not contain a
tree-graph inequality for the actual residual mixed derivatives, a
Battle-Brydges-Federbush/Brydges-Kennedy forest formula applied to the
adaptive residual Hamiltonian, or a same-law bound on the mixed derivative
kernel \(\alpha_{uv}^{N,j}\).  Section 56 therefore remains at the triangle
bound until this new connected derivative theorem is supplied. `square`

### Corollary 60.6: Route II Verdict

Route II is the most promising positive route because it targets the exact
lost cancellation.  It is nevertheless not proved by the present corpus.  It
is settled here as a valid but currently unsourced Branch-A theorem.

## 61. Route III: Peter-Weyl Smoothing Plus Residual Tail

The third attempt asks whether heat-kernel smoothing can source the
low-mode/tail anchor without reconstructing the full conditional law.

### Lemma 61.1: Pure Heat-Kernel Factors Dampen Peter-Weyl Modes

For a compact-group heat-kernel factor on \(SU(N)\),
$$
\widehat H_t(\lambda)=e^{-tC_2(\lambda)}
$$
on the irreducible representation \(\lambda\).

Proof.

This is the Peter-Weyl diagonalization of the compact-group heat semigroup.
`square`

### Definition 61.2: Residual Smoothing Defect

Let \(D_{\iota,max}^{N,j}\) be the actual bridge defect of Definition 56.4.
After factoring the tree-gauge heat-kernel channels, define the residual
smoothing defect by
$$
\mathcal E_{PW}^{N,j}(L)
:=
\left\|
\Pi_{>L}
\left(D_{\iota,max}^{N,j}
-D_{\iota,max}^{HK,N,j}\right)
\right\|_{br},
$$
where \(D_{\iota,max}^{HK,N,j}\) is the part controlled only by the
heat-kernel convolution channels.

### Definition 61.3: Heat-Residual Tail Source

`P30-HK-RESID-PWTAIL(A,c,L_0)` asserts that for all \(L\ge L_0\),
$$
\mathsf T_{\iota,L}^{DLR}
\le
A e^{-c C_2(L)t_{\rm eff}}
+\mathcal E_{PW}^{N,j}(L),
$$
and that cofinally the right side is below the Paper-30 low-mode/tail
margin.

### Theorem 61.4: Heat-Residual Tail Sources The Low-Mode/Tail Anchor

If `P30-HK-RESID-PWTAIL(A,c,L_0)` holds and the projected low-mode matrix
entries satisfy the margin in Lemma 56.5, then
`P30-BRANCHA-LOWTAIL-ANCHOR` holds.

Proof.

The heat-kernel part is damped by Lemma 61.1.  The residual smoothing defect
pays the part not controlled by pure heat flow.  The projected matrix plus
the tail bound is precisely the low-mode/tail anchor of Lemma 56.5.
`square`

### Proposition 61.5: Pure Heat-Kernel Smoothing Does Not Prove The Actual
Tail

The pure heat-kernel estimate alone does not prove
`P30-HK-RESID-PWTAIL(A,c,L_0)` for the actual adaptive residual defect.

Proof.

Conditioning, central-entry division, retained-row subtraction, and the RPF
residual potential can introduce high Peter-Weyl coefficients after the
heat-kernel factors are divided or multiplied by noncentral residual terms.
Papers 28 and 29 already isolate this as the same-law tail gap.  Therefore
Lemma 61.1 is correct but insufficient unless the residual smoothing defect
\(\mathcal E_{PW}^{N,j}(L)\) is itself bounded. `square`

### Corollary 61.6: Route III Verdict

Route III proves the admissible heat-flow component and identifies the exact
missing residual tail.  It is falsified as a pure heat-kernel derivation of
the actual adaptive tail, but remains open as a same-law residual-smoothing
theorem.

## 62. Route IV: Schwinger-Dyson/Ward Signed Bridge Identity

The fourth attempt uses gauge-invariant integration by parts.  The hope is
not positivity but cancellation: the signed bridge object might be a
finite-dimensional divergence plus a controlled boundary defect.

### Lemma 62.1: Finite Compact-Lie Integration By Parts

Let \(X_\ell\) be a left-invariant vector field on an internal parent edge
\(\ell\), and let \(F\) be a smooth finite DLR observable.  Then
$$
E_{K_B^{par}}\left[X_\ell F\right]
=
-
E_{K_B^{par}}\left[
F\,X_\ell\log {dK_B^{par}\over dg}
\right].
$$

Proof.

Haar measure is invariant and \(X_\ell\) has zero Haar divergence.  Integrate
\(X_\ell(F\rho)\) over the compact group chart, where
\(\rho=dK_B^{par}/dg\). `square`

### Definition 62.2: Signed Ward Residual

For the signed bridge functional \(\mathcal B_{sgn}\), define
$$
\mathcal W_{br}^{N,j}
:=
E_{K_B^{par}}\left[
\mathcal B_{sgn}\,
X_\ell\log {dK_B^{par}\over dg}
\right]
$$
after all retained-row, endpoint-additive, HKSD tangent, and
HK-symmetric pieces have been removed.

### Definition 62.3: Ward Closing Source

`P30-WARD-BRIDGE(Theta,omega)` asserts that the finite signed Ward residual
satisfies the Paper-30 signed bridge margin
$$
\Theta+\omega^2/4<M_{\rm sgn}(\kappa)
$$
with \(\Theta,\omega\) computed from \(\mathcal W_{br}^{N,j}\).

### Theorem 62.4: Ward Bridge Source Closes The Signed Route

`P30-WARD-BRIDGE(Theta,omega)` implies the signed bridge value source
`P30-SIGNED-BRIDGE-VALUE(Theta,omega,kappa)`.

Proof.

Lemma 62.1 rewrites the signed bridge amplitude as a Ward residual plus
already removed retained and heat-kernel tangent pieces.  The retained pieces
have been licensed earlier in Paper 30; the remaining signed range and
one-line width are exactly \(\Theta,\omega\).  The Paper-30 signed scalar
gate then applies. `square`

### Proposition 62.5: Ward Identities Do Not Currently Give A Vanishing
Residual

Papers 20--30 do not prove that \(\mathcal W_{br}^{N,j}=0\), nor that it is
small enough for `P30-WARD-BRIDGE(Theta,omega)`.

Proof.

The earlier HKSD audits remove heat-kernel tangent and endpoint-local
pieces.  The remaining object is the off-sheet/Bianchi/RN residual term.
Gauge invariance gives the integration-by-parts identity, but it does not
force the residual term to vanish unless the signed bridge functional is an
exact divergence with no boundary/collar defect.  That exact-divergence
theorem is not printed in the corpus. `square`

### Corollary 62.6: Route IV Verdict

Route IV proves the finite same-law Ward identity but does not prove the
signed residual cancellation.  It is settled as an unsourced but potentially
valuable signed-cancellation theorem.

## 63. Route V: Transport Or Entropic Contraction

The fifth attempt weakens the metric.  Total variation is often too harsh;
the scalar gate may only need contraction of the actual record observable.

### Definition 63.1: Record-Compatible Transport Influence

Let \(d_{rec}\) be the scalar record metric used by the adaptive defect
coordinate.  Define
$$
\mathcal T_{xy}^{N,j}
:=
\sup_{\eta,\eta' \text{ differing at }y}
W_{1,d_{rec}}
\left(
K_x^{par}(\cdot\mid\eta),
K_x^{par}(\cdot\mid\eta')
\right).
$$

### Lemma 63.2: Transport Influence Bounds Scalar Lipschitz Observables

For every scalar observable \(F_x\) with
\(\operatorname{Lip}_{d_{rec}}(F_x)\le1\),
$$
\left|
E_{\eta}F_x-E_{\eta'}F_x
\right|
\le
\mathcal T_{xy}^{N,j}.
$$

Proof.

This is Kantorovich duality for \(W_1\). `square`

### Definition 63.3: Transport Closing Source

`P30-TRANSPORT-ROW(q,a)` asserts
$$
\limsup_{(N,j)}
\sup_x
\sum_y e^{a d(x,y)}\mathcal T_{xy}^{N,j}
\le q<1
$$
for the scalar defect observables entering Branch A.

### Theorem 63.4: Transport Row Closes The Observable Dobrushin Gate

If the Branch-A scalar defect observables are \(1\)-Lipschitz in
\(d_{rec}\) and `P30-TRANSPORT-ROW(q,a)` holds, then the corresponding
observable-level Dobrushin gate closes.

Proof.

Apply Lemma 63.2 to each row entry and sum with the Branch-A weight.
`square`

### Proposition 63.5: Transport Contraction Is Not Supplied By The Current
Corpus

The current corpus does not prove `P30-TRANSPORT-ROW(q,a)`.

Proof.

A useful transport row would follow from a same-law log-Sobolev,
Talagrand, coarse Ricci, or synchronous-coupling contraction estimate for
the conditioned residual law.  Papers 20--30 do not prove any of these for
the actual adaptive residual DLR conditional.  Heat-kernel factors alone are
not enough because the residual tilt and conditioning can destroy a uniform
transport constant in the required scalar coordinates. `square`

### Corollary 63.6: Route V Verdict

Route V is a legitimate weakening of Dobrushin and may be analytically
easier than total variation.  It is not proved by the current corpus and is
settled here as a new same-law transport theorem to be proved, not as a
bookkeeping task.

## 64. Route VI: Lower-Floor Exit

The sixth route is the negative theorem.  If the positive smallness routes
are false, the honest way to close Branch A is to prove a same-law lower
floor rather than continue to search for labels.

### Definition 64.1: Radical Lower-Floor Source

`P30-RADICAL-FLOOR(M_*)` asserts a same-law sign-coherent lower floor
$$
\overline\Lambda_{13}^{RPF}\ge M_*
$$
in the exact adaptive residual object, after all retained rows and licensed
subtractions have been applied.

### Theorem 64.2: Lower Floor Falsifies Adaptive Branch A

`P30-RADICAL-FLOOR(M_*)` falsifies adaptive Branch A whenever \(M_*\) exceeds
the maximal Branch-A loss budget allowed by the Paper-23/Paper-30 scalar
gates.

Proof.

This is the lower-floor alternative already isolated in Papers 24, 27, 29,
and the earlier signed route of Paper 30.  A floor above the admissible
smallness threshold rules out every positive Branch-A smallness theorem.
`square`

### Proposition 64.3: The Lower Floor Is Not Supplied By The Current Corpus

Papers 20--30 do not prove `P30-RADICAL-FLOOR(M_*)`.

Proof.

The corpus proves that failure of KP, Dobrushin, spectral, transport, or
signed estimates does not itself imply a lower floor.  A floor requires a
sign-coherent witness surviving normalization, retained-row subtraction,
RP/Cov transport, and scalar pushforward.  No such witness is printed.
`square`

### Corollary 64.4: Route VI Verdict

The lower-floor route is valid and remains the honest negative closure of
Branch A.  It is unsourced by the current corpus.  Thus it is not a positive
proof, but it is the right theorem if the actual adaptive law refuses all
smallness routes.

## 65. Completion Of The Radical Search Pass

The six radical routes have now been explored to the limit of the current
corpus:

1. score/covariance response: exact identity proved; closing row unsourced;
2. connected Möbius/cumulant cancellation: mixed-derivative identity proved;
   connected derivative bound unsourced;
3. Peter-Weyl smoothing: pure heat-kernel damping proved; residual tail
   unsourced;
4. Ward/signed bridge identity: finite integration-by-parts identity proved;
   signed residual cancellation unsourced;
5. transport contraction: observable transport implication proved; same-law
   transport row unsourced;
6. lower-floor exit: falsifying implication proved; sign-coherent floor
   witness unsourced.

Therefore the radical search does not close Branch A from Papers 20--30, but
it does sharpen the next real theorem.  The most valuable positive target is
not another finite label table.  It is one of the following actual-law
analytic estimates:

$$
\boxed{
\mathrm{P30\text{-}CONN\text{-}MOBIUS}
\quad\text{or}\quad
\mathrm{P30\text{-}SCORE\text{-}COV\text{-}ROW}
\quad\text{or}\quad
\mathrm{P30\text{-}HK\text{-}RESID\text{-}PWTAIL}
}
$$

with the signed alternatives
$$
\boxed{
\mathrm{P30\text{-}WARD\text{-}BRIDGE}
\quad\text{or}\quad
\mathrm{P30\text{-}RADICAL\text{-}FLOOR}.
}
$$

This is Barandes-aligned: every theorem is stated on the actual finite
conditional law and its scalar pushforward, and every failure is reported as
a current-corpus non-sourcing result rather than hidden as a comparison-law
substitution.

## 66. A More Feynman Move: Same-Law Representation Histories

The previous six routes still phrase the obstruction as an estimate on the
finite DLR density.  A more path-integral move is to stop staring at the
density itself.  Rewrite the same finite law as a sum over representation
histories.  This is not a comparison law.  It is the Peter-Weyl expansion of
the same compact-group heat-kernel DLR measure.

The point is conceptual.  Range estimates see pointwise spikes.  A
representation-history expansion sees flux conservation, Casimir weights,
and the exact boundary charges that can contribute to a signed bridge
coefficient.

### Definition 66.1: Residual Insertion

On a finite parent DLR region \(B\), write
$$
\mathcal R_B^{N,j}(g,\eta)
:=
e^{-V_{RPF}(g,\eta)}J_{tree}(g,\eta)
$$
on each admissible tree-gauge chart and essential-support cell.  The exact
finite parent conditional has unnormalized density
$$
\mathcal U_B^{N,j}(g,\eta)
=
\left(\prod_{p\cap B\ne\varnothing}H_{t_p}(h_p(g,\eta))\right)
\mathcal R_B^{N,j}(g,\eta).
$$

### Lemma 66.2: Heat-Kernel Character Expansion Is Same-Law

For each plaquette heat-kernel factor,
$$
H_{t_p}(U)
=
\sum_{\lambda\in\widehat{SU(N)}}
d_\lambda e^{-t_p C_2(\lambda)}
\chi_\lambda(U)
$$
in the Paper-20 heat-kernel normalization.

Proof.

This is the Peter-Weyl spectral decomposition of the compact-group heat
semigroup.  The expansion is the heat kernel itself, not a replacement
measure. `square`

### Definition 66.3: Finite Spin-Foam Amplitude With Residual Insertion

Expand all plaquette heat kernels by Lemma 66.2 and expand the residual
insertion \(\mathcal R_B^{N,j}\) in Peter-Weyl matrix coefficients on the
finite chart.  After integrating internal link variables, obtain a
representation-history amplitude
$$
\mathcal A_{B}^{N,j}(\mathfrak f;\eta)
$$
where \(\mathfrak f\) consists of:

1. plaquette representation labels \(\lambda_p\);
2. edge intertwiners enforcing Haar flux conservation;
3. residual insertion labels carried by \(\mathcal R_B^{N,j}\);
4. the boundary spin-network data induced by \(\eta\).

Let \(\mathfrak F_B(\eta)\) be the set of all such finite-region
representation histories.

### Theorem 66.4: Exact Same-Law Spin-Foam DLR Formula

For every finite parent region \(B\),
$$
Z_B^{N,j}(\eta)
=
\sum_{\mathfrak f\in\mathfrak F_B(\eta)}
\mathcal A_B^{N,j}(\mathfrak f;\eta),
$$
and every scalar bridge coefficient computed from
\(K_B^{par}(\cdot\mid\eta)\) is the corresponding normalized sum of the same
amplitudes with the scalar observable inserted.

Proof.

Insert the Peter-Weyl expansion of each heat-kernel factor and the
Peter-Weyl expansion of the finite residual insertion into the exact finite
DLR integral.  Orthogonality of matrix coefficients performs the internal
link integrations and produces edge intertwiners.  Because the region is
finite and the heat kernels are smooth for \(t_p>0\), the heat-kernel part is
absolutely summable; the residual insertion is the actual finite function or
finite \(L^2\) limit on the admissible cell.  Truncated expansions converge
to the finite DLR integral. `square`

This is the Feynman-style object that was missing: the actual same-law
conditional has been rewritten as a sum over histories with explicit Casimir
weights and exact conservation rules.

## 67. Flux Selection For Bridge Coefficients

The representation-history formula gives information not visible in the
range extractor: many coefficients are zero unless a compatible flux history
exists.

### Definition 67.1: Bridge Boundary Charge

For a projected signed bridge coefficient
\(\widehat D_{\iota,max}^{N,j}(\lambda,\mu)\), define its boundary charge
class \(Q(\lambda,\mu)\) to be the endpoint/blanket spin-network charge that
must be supplied by the finite parent DLR representation history.

### Definition 67.2: Admissible Flux History

A history \(\mathfrak f\in\mathfrak F_B(\eta)\) is
\((\lambda,\mu)\)-admissible if its plaquette labels, edge intertwiners, and
residual insertion labels fuse to the boundary charge \(Q(\lambda,\mu)\)
after all retained rows and licensed endpoint-additive pieces are removed.

### Proposition 67.3: Same-Law Flux Selection Rule

If no \((\lambda,\mu)\)-admissible representation history exists, then
$$
\widehat D_{\iota,max}^{N,j}(\lambda,\mu)=0.
$$

Proof.

By Theorem 66.4 the coefficient is a normalized sum over representation
histories with boundary charge \(Q(\lambda,\mu)\).  Haar integration at each
internal edge enforces the intertwiner constraint.  If the charge cannot be
fused through the plaquette and residual insertion labels to the boundary,
every internal link integral vanishes by Peter-Weyl orthogonality. `square`

### Definition 67.4: Foam Tail Enumerator

For a cutoff \(L\), define the actual same-law foam tail numerator
$$
\mathfrak T_{B,L}^{N,j}
:=
\sum_{\mathfrak f\in\mathfrak F_B(\eta):\,Q(\mathfrak f)>L}
\left|\mathcal A_B^{N,j}(\mathfrak f;\eta)\right|,
$$
where \(Q(\mathfrak f)>L\) means that \(\mathfrak f\) carries at least one
endpoint/blanket boundary charge above the Peter-Weyl cutoff required by
Definition 56.4.  Define also the positive absolute partition
$$
\mathfrak Z_{B}^{abs,N,j}
:=
\sum_{\mathfrak f\in\mathfrak F_B(\eta)}
\left|\mathcal A_B^{N,j}(\mathfrak f;\eta)\right|.
$$

### Lemma 67.5: Foam Tail Controls The Projected Tail

For the bridge norm of Definition 41.1,
$$
\mathsf T_{\iota,L}^{DLR}
\le
\limsup_{(N,j)}
\sup_B
{\mathfrak T_{B,L}^{N,j}\over Z_B^{N,j}(\eta)}
$$
whenever the signed bridge observable has bridge norm at most one on the
tail sector.  More conservatively,
$$
\mathsf T_{\iota,L}^{DLR}
\le
\limsup_{(N,j)}
\sup_B
{\mathfrak T_{B,L}^{N,j}\over
\left|Z_B^{N,j}(\eta)\right|}
$$
with the same normalization cell.

Proof.

The projected tail is a normalized sum of amplitudes whose boundary charge
lies above \(L\).  Taking absolute values before summing gives the displayed
upper bound. `square`

### Definition 67.6: Spin-Foam Tail Source

`P30-SPINFOAM-TAIL(r_L)` asserts that the actual adaptive cofinal family
satisfies
$$
\limsup_{(N,j)}
\sup_B
{\mathfrak T_{B,L}^{N,j}\over Z_B^{N,j}(\eta)}
\le r_L
$$
with \(r_L\) below the Paper-30 low-mode/tail margin.

### Theorem 67.7: Spin-Foam Tail Sources The Low-Mode/Tail Anchor

If the projected low-mode bridge matrix is printed in the same
representation-history normalization and `P30-SPINFOAM-TAIL(r_L)` holds in a
closing range, then `P30-BRANCHA-LOWTAIL-ANCHOR` holds.

Proof.

The low-mode entries are the normalized history sums with
\(Q(\mathfrak f)\le L\).  Lemma 67.5 pays the omitted histories.  This is
exactly Lemma 56.5 with the tail now represented by a same-law path-sum
quantity. `square`

## 68. What The Path-Sum Move Actually Buys

The spin-foam expansion is not a proof of confinement.  It is a new
same-law quantitative representation of the missing values.  It buys three
things that range control did not:

1. **zero tests**: Proposition 67.3 can prove actual coefficient vanishing
   from representation fusion constraints;
2. **tail bookkeeping**: Lemma 67.5 converts the Peter-Weyl tail into a
   weighted sum over high-charge histories;
3. **Casimir pressure**: every plaquette face in a high-charge history pays
   explicit heat-kernel weight \(e^{-t_pC_2(\lambda_p)}\).

The remaining hard estimate is now a concrete surface/foam competition:
Casimir damping plus signed/intertwiner cancellation against the entropy of
admissible high-charge histories and the residual insertion coefficients.

### Proposition 68.1: The Pure Foam Bound Still Does Not Close Automatically

The identity of Theorem 66.4 and the selection rule of Proposition 67.3 do
not by themselves prove `P30-SPINFOAM-TAIL(r_L)` in a closing cofinal range.

Proof.

The expansion contains explicit Casimir weights, but the number of
admissible high-charge histories, the size of residual insertion
coefficients, and possible cancellations after normalization are not bounded
by the identity alone.  In the small-time cofinal regime the factor
\(e^{-t_pC_2(\lambda_p)}\) may be too weak unless high-charge histories are
forced to carry enough area, enough repeated heat-time, or enough signed
cancellation.  These are new quantitative statements about the same
representation-history law. `square`

### Corollary 68.2: The New Most Concrete Positive Target

The most concrete next theorem is no longer an abstract "tail estimate".
It is the spin-foam tail theorem
$$
\boxed{
\mathrm{P30\text{-}SPINFOAM\text{-}TAIL}(r_L)
}
$$
possibly strengthened by one of:

1. a high-charge area lower bound for admissible bridge histories;
2. a residual-insertion Peter-Weyl decay theorem;
3. an intertwiner/signed cancellation theorem for paired high-charge foams;
4. a denominator lower bound preventing normalization blowup.

This is the closest analogue, inside the present same-law program, of a
Feynman path-integral leap: exchange a hard density estimate for a sum over
histories whose weights and conservation laws are explicit.

## 69. Updated Endpoint After The Path-Integral Push

The radical search has now been pushed one step further than the
"not sourced" ledger.  A new constructive same-law object has been printed:
the representation-history expansion of the actual finite parent DLR law.

What is proved:

1. the exact same-law spin-foam DLR formula;
2. the flux-selection rule for projected bridge coefficients;
3. the foam-tail upper bound for the projected Peter-Weyl complement;
4. the closure implication from a passing foam-tail theorem to
   `P30-BRANCHA-LOWTAIL-ANCHOR`.

What remains unproved:

1. a cofinal high-charge area lower bound;
2. residual insertion coefficient decay;
3. signed/intertwiner cancellation in the high-charge tail;
4. a denominator lower bound strong enough to prevent normalization loss.

Thus the next genuinely positive theorem to attack is
`P30-SPINFOAM-TAIL(r_L)`, not another label table.  The best first subgate is
the high-charge area lower bound, because it would convert the explicit
Casimir weights in Lemma 66.2 into actual tail decay.

## 70. Nonabelian Switching: The Real Feynman-Style Target

The path-sum formulation still asks for a tail estimate.  The more radical
move is to search for a **switching identity**, analogous in role to the
random-current switching lemma but adapted to nonabelian representation
histories.

The abelian/Ising switching idea cannot be copied literally.  There is no
single mod-2 current.  A nonabelian history carries oriented irreducible
representations and intertwiners.  Switching is therefore not symmetric
difference of currents; it is a recoupling move along a corridor that moves
a boundary charge through the spin network.

### Definition 70.1: Signed History Observable

Let \(\mathfrak F_B(\eta)\) be the representation-history set of
Definition 66.3.  Write a projected signed bridge coefficient in the form
$$
\mathcal B_B^{N,j}
=
{1\over Z_B^{N,j}(\eta)}
\sum_{\mathfrak f\in\mathfrak F_B(\eta)}
\mathcal A_B^{N,j}(\mathfrak f;\eta)\,
\sigma_B(\mathfrak f),
$$
where \(\sigma_B(\mathfrak f)\) is the signed bridge insertion after all
retained, endpoint-additive, and licensed rows have been removed.

### Definition 70.2: Switching Corridor

A switching corridor \(\Gamma\) is a connected chain of plaquette/intertwiner
incidences joining the two bridge endpoint charge sites.  A corridor switch
\(S_\Gamma\) is a partial map on \(\mathfrak F_B(\eta)\) that:

1. tensors the local charge along \(\Gamma\) by the fundamental/dual charge
   required by the signed bridge insertion;
2. recouples each intermediate edge by finite \(SU(N)\) \(F\)-moves;
3. preserves the Haar intertwiner constraints at all internal links;
4. returns a history with the same external retained scalar record.

The map is defined only on histories for which all required fusion channels
and recoupling coefficients are nonzero.

### Lemma 70.3: Local Recoupling Preserves The Same-Law History Space

Whenever \(S_\Gamma\mathfrak f\) is defined, it is again an element of the
same representation-history space \(\mathfrak F_B(\eta)\).

Proof.

The move changes labels only by legal tensor product decompositions and
finite \(F\)-moves.  These are identities in the representation category of
\(SU(N)\).  The internal Haar integrations require exactly invariant
intertwiners; recoupling replaces one basis of the same invariant tensor
space by another.  Boundary retained scalar data are declared fixed by item
4 of Definition 70.2. `square`

### Definition 70.4: Switching Defects

For a defined corridor switch, set
$$
\Delta_\Gamma(\mathfrak f)
:=
\log
\left|
{\mathcal A_B^{N,j}(S_\Gamma\mathfrak f;\eta)
\over
\mathcal A_B^{N,j}(\mathfrak f;\eta)}
\right|.
$$
Decompose it as
$$
\Delta_\Gamma
=
\Delta_\Gamma^{HK}
+\Delta_\Gamma^{F}
+\Delta_\Gamma^{RPF},
$$
where the terms are respectively the heat-kernel Casimir weight change, the
recoupling/intertwiner coefficient change, and the residual insertion
coefficient change.

Also define the actual complex amplitude-mismatch defect
$$
\mathfrak d_\Gamma(\mathfrak f)
:=
{\left|
\mathcal A_B^{N,j}(S_\Gamma\mathfrak f;\eta)
-
\mathcal A_B^{N,j}(\mathfrak f;\eta)
\right|
\over
\left|\mathcal A_B^{N,j}(\mathfrak f;\eta)\right|}
$$
whenever the denominator is nonzero.  Histories with zero denominator are
placed in the unpaired sector.  This second defect is the one that controls
signed cancellation; \(\Delta_\Gamma\) only controls magnitudes and must be
supplemented by phase information.

### Lemma 70.5: Explicit Heat-Kernel Part Of The Switching Defect

For every defined switch,
$$
\Delta_\Gamma^{HK}(\mathfrak f)
=
-
\sum_{p\in \Gamma}
t_p\left[
C_2(\lambda_p(S_\Gamma\mathfrak f))
-C_2(\lambda_p(\mathfrak f))
\right]
+
\sum_{p\in\Gamma}
\log {d_{\lambda_p(S_\Gamma\mathfrak f)}\over d_{\lambda_p(\mathfrak f)}}.
$$

Proof.

Use Lemma 66.2.  The heat-kernel factor attached to plaquette \(p\) is
\(d_\lambda e^{-t_pC_2(\lambda)}\).  Taking the logarithm of the ratio after
the switch gives the displayed expression. `square`

### Definition 70.6: Nonabelian Switching Source

`P30-NONABELIAN-SWITCHING(delta,u)` asserts that for the high-charge bridge
tail there is a finite family of corridor switches whose orbits satisfy:

1. except for an unpaired set \(\mathfrak U\), every high-charge history is
   paired with exactly one switched history;
2. the signed insertion reverses on paired histories:
   \(\sigma_B(S\mathfrak f)=-\sigma_B(\mathfrak f)\);
3. the amplitude-mismatch switching defect obeys
   \(\mathfrak d_S(\mathfrak f)\le\delta\);
4. the normalized unpaired absolute mass satisfies
   $$
   {1\over Z_B^{N,j}(\eta)}
   \sum_{\mathfrak f\in\mathfrak U}
   |\mathcal A_B^{N,j}(\mathfrak f;\eta)|
   \le u.
   $$

### Theorem 70.7: Switching Bound For The Signed High-Charge Tail

If `P30-NONABELIAN-SWITCHING(delta,u)` holds, then the signed high-charge
tail obeys
$$
|\mathcal B_{tail}^{N,j}|
\le
\delta
{\mathfrak Z_{tail}^{abs,N,j}\over Z_B^{N,j}(\eta)}
+u.
$$
In particular, if the right side is below the Paper-30 low-mode/tail margin,
then the signed low-mode/tail route closes.

Proof.

On a paired orbit \(\{\mathfrak f,S\mathfrak f\}\),
\(\sigma(S\mathfrak f)=-\sigma(\mathfrak f)\).  Hence the paired signed
contribution is
$$
\sigma(\mathfrak f)
\left(
\mathcal A(\mathfrak f)-\mathcal A(S\mathfrak f)
\right).
$$
The defect bound gives
\(|\mathcal A(S\mathfrak f)-\mathcal A(\mathfrak f)|
\le\delta|\mathcal A(\mathfrak f)|\).  Summing over paired orbits and then
adding the unpaired mass gives the result. `square`

This is the nonabelian switching analogue of the random-current miracle: the
large absolute tail may exist, but only the failure of the local switch to be
amplitude-preserving, plus the unpaired sector, survives in the signed
observable.

## 71. Can The Switching Source Be Proved From The Current Corpus?

The switching theorem is constructive enough to test.  Its four hypotheses
map to four concrete subproblems.

### Proposition 71.1: The Current Corpus Proves The Category Part

Papers 20--30, together with standard finite \(SU(N)\) representation
theory already used in the Peter-Weyl expansions, prove the categorical
legality part of corridor switching: legal recouplings preserve the internal
Haar constraints.

Proof.

This is Lemma 70.3.  The corpus already uses Peter-Weyl orthogonality,
dualities, conjugation, and finite representation batteries.  Corridor
switching adds no new measure; it only changes basis inside finite invariant
tensor spaces. `square`

### Proposition 71.2: Exact Ising-Style Switching Is False As A Free
Inference

The current corpus does not imply an exact amplitude-preserving nonabelian
switching involution with \(\delta=0\) and \(u=0\).

Proof.

Even if the heat-kernel part were paired, the amplitude also contains
recoupling coefficients and the residual insertion
\(\mathcal R_B^{N,j}=e^{-V_{RPF}}J_{tree}\).  A local recoupling generally
changes the \(F\)-move coefficient and the residual Peter-Weyl coefficient.
No theorem in Papers 20--30 states that
\(\Delta_\Gamma^{F}+\Delta_\Gamma^{RPF}\) cancels the heat-kernel change or
vanishes on every paired orbit.  Therefore the Ising random-current miracle
does not transfer for free to the actual nonabelian adaptive law. `square`

### Definition 71.3: Residual Quasi-Invariance Source

`P30-SWITCH-RESID-QI(epsilon)` asserts that for the corridor switches used
in Definition 70.6,
$$
\left|
\Delta_\Gamma^{F}(\mathfrak f)
+\Delta_\Gamma^{RPF}(\mathfrak f)
\right|
\le \epsilon
$$
outside an unpaired set whose normalized mass is already counted in \(u\).
It also asserts the corresponding phase/quasi-invariance control needed to
convert this magnitude estimate into an amplitude-mismatch estimate.

### Definition 71.4: Switch Neutrality And Unpaired Sources

`P30-SWITCH-NEUTRAL(nu)` asserts that the heat-kernel, dimension, and
recoupling parts of the corridor switch are amplitude-neutral up to
\(\nu\), after the residual quasi-invariance source has been applied:
$$
\mathfrak d_\Gamma(\mathfrak f)\le \nu
$$
on the paired favorable sector.

`P30-SWITCH-UNPAIRED(u)` asserts that the normalized absolute mass of
histories on which the switch is not defined, not sign-reversing, or not
neutral is at most \(u\).

Separately, `P30-SWITCH-AREA(A_0)` asserts that every unpaired high-charge
history, or every history for which one abandons cancellation and uses
absolute damping instead, carries at least \(A_0\) plaquette heat-kernel cost
in the relevant switched charge sector:
$$
\sum_{p\in\Gamma}
t_p
\left[
C_2(\lambda_p(S_\Gamma\mathfrak f))
-C_2(\lambda_p(\mathfrak f))
\right]
\ge A_0.
$$

Switch neutrality is the cancellation source.  Switch area is the absolute
tail source for the histories that cannot be cancelled.

### Theorem 71.5: Residual Quasi-Invariance Plus Neutrality Sources
Nonabelian Switching

If `P30-SWITCH-RESID-QI(epsilon)`, `P30-SWITCH-NEUTRAL(nu)`, and
`P30-SWITCH-UNPAIRED(u)` hold, then
`P30-NONABELIAN-SWITCHING(delta,u)` holds with
$$
\delta\le \nu.
$$

Proof.

Residual quasi-invariance is the statement that the actual RPF/Jacobian
insertion does not spoil the corridor switch.  Switch neutrality supplies
the amplitude-mismatch bound on the paired favorable sector.  The unpaired
source pays all histories not covered by the sign-reversing neutral switch.
These are exactly the hypotheses of Definition 70.6. `square`

### Theorem 71.6: Switch Area Sources The Unpaired Tail Debit

If `P30-SWITCH-AREA(A_0)` holds with representation-history entropy debit
\(g_{sw}\), residual insertion coefficient debit \(\epsilon_{res}\), and
denominator lower debit \(d_Z\), then the unpaired absolute tail satisfies
$$
u
\le
\exp\left(g_{sw}+\epsilon_{res}+d_Z-A_0\right).
$$

Proof.

The unpaired sector is bounded absolutely.  Each such history pays at least
the heat-kernel Casimir cost \(A_0\).  The number and recoupling size of such
histories is charged to \(g_{sw}\), the residual insertion coefficients to
\(\epsilon_{res}\), and the normalization denominator to \(d_Z\).  Summing
the resulting majorant gives the displayed bound. `square`

### Proposition 71.7: Current-Corpus Status Of Nonabelian Switching

The current corpus proves the switching framework and the heat-kernel
defect formula, but it does not prove `P30-SWITCH-RESID-QI(epsilon)`,
`P30-SWITCH-NEUTRAL(nu)`, `P30-SWITCH-AREA(A_0)`, or a useful unpaired-mass
bound.

Proof.

`P30-SWITCH-RESID-QI` is a new theorem about the actual residual insertion
coefficients under local nonabelian recoupling.  `P30-SWITCH-NEUTRAL` is a
new theorem that the paired histories have nearly equal complex amplitudes,
not merely comparable magnitudes.  `P30-SWITCH-AREA` is a new geometric
theorem about which high-charge bridge histories must cross enough
heat-kernel area when cancellation fails.  Papers 20--30 contain
bridge/carrier finite tables and rooted-tree overcounts, but not this
representation-history area lower bound.  Finally, the unpaired sector is
precisely where fusion channels vanish or residual coefficients obstruct the
switch; no current theorem bounds its normalized mass. `square`

## 72. What The Switching Push Really Changes

The nonabelian switching route is stronger than the spin-foam tail route in
one crucial way.  It does not require the absolute high-charge tail to be
small.  It only requires paired high-charge histories to have nearly equal
amplitudes with opposite signed insertion.

Thus the live positive theorem is now sharper:
$$
\boxed{
\mathrm{P30\text{-}NONABELIAN\text{-}SWITCHING}(\delta,u)
}
$$
or, more primitively,
$$
\boxed{
\mathrm{P30\text{-}SWITCH\text{-}RESID\text{-}QI}(\epsilon)
\quad+\quad
\mathrm{P30\text{-}SWITCH\text{-}NEUTRAL}(\nu)
\quad+\quad
\mathrm{P30\text{-}SWITCH\text{-}UNPAIRED}(u).
}
$$
The unpaired source can itself be attacked by
$$
\boxed{
\mathrm{P30\text{-}SWITCH\text{-}AREA}(A_0)
}
$$
plus entropy, residual-coefficient, and denominator debits.

This is the best genuinely creative Branch-A target produced so far.  It is
Barandes-aligned because it operates entirely inside the actual finite DLR
history expansion.  It is Feynman-like in the relevant sense: it changes the
variables so that cancellation, not smallness, becomes the central object.

What is settled:

1. the nonabelian switching format is mathematically valid;
2. exact Ising-style switching is not available as a free inference;
3. the heat-kernel part of the switching defect is explicit;
4. residual quasi-invariance plus switch-neutrality would source signed
   cancellation without paying the full absolute tail;
5. switch-area would pay the sector where cancellation is unavailable.

What remains:

1. prove residual quasi-invariance of the actual RPF/Jacobian insertion under
   local recoupling;
2. prove complex amplitude neutrality for paired corridor switches;
3. prove a high-charge switch-area lower bound;
4. bound the unpaired fusion-obstruction sector;
5. then insert the resulting \(\delta,u\) into Theorem 70.7.

This does not close Branch A yet.  It does, however, replace "find a value
bound" by a more structural theorem: prove a same-law nonabelian switching
principle for the residual bridge histories.

## 73. Minimal Corridor Amplitude-Ratio Test

We now test the switching idea on the smallest local corridor.  This is the
right next diagnostic: if the minimal corridor already cannot be neutral,
then termwise switching is the wrong formulation.

### Definition 73.1: Minimal Corridor Cell

A minimal corridor cell \(\Gamma_1\) consists of:

1. one live plaquette heat-kernel face \(p\);
2. the two adjacent Haar-intertwiner vertices through which the bridge
   endpoint charge is transported;
3. one residual insertion coefficient from
   \(\mathcal R_B^{N,j}=e^{-V_{RPF}}J_{tree}\);
4. the signed bridge endpoint charge \(q\), taken first in the declared
   fundamental/dual battery.

Let the local history data be
$$
h=(\lambda,i_L,i_R,\rho),
$$
where \(\lambda\) is the plaquette irrep, \(i_L,i_R\) are local intertwiner
labels, and \(\rho\) is the residual-insertion Peter-Weyl label touching the
cell.  A minimal switch sends
$$
h\mapsto h'=(\lambda',i_L',i_R',\rho')
$$
through an allowed fusion channel in \(\lambda\otimes q\).

### Definition 73.2: Local Amplitude Factors

Write the local contribution to the representation-history amplitude as
$$
\mathcal A_{\Gamma_1}(h)
=
H_{\Gamma_1}(\lambda)\,
F_{\Gamma_1}(\lambda,i_L,i_R;q)\,
R_{\Gamma_1}(\rho;\lambda,i_L,i_R),
$$
where
$$
H_{\Gamma_1}(\lambda)
=
d_\lambda e^{-t_pC_2(\lambda)}
$$
is the heat-kernel factor, \(F_{\Gamma_1}\) is the product of the finite
recoupling/intertwiner coefficients in the chosen orthonormal convention,
and \(R_{\Gamma_1}\) is the actual residual insertion coefficient.

### Lemma 73.3: Exact Minimal Corridor Ratio

For every defined minimal corridor switch with nonzero denominator,
$$
{\mathcal A_{\Gamma_1}(h')\over\mathcal A_{\Gamma_1}(h)}
=
R_{HK}(h,h')\,R_F(h,h')\,R_{RPF}(h,h'),
$$
where
$$
R_{HK}(h,h')
=
{d_{\lambda'}\over d_\lambda}
\exp\{-t_p(C_2(\lambda')-C_2(\lambda))\},
$$
$$
R_F(h,h')
=
{F_{\Gamma_1}(\lambda',i_L',i_R';q)
\over
F_{\Gamma_1}(\lambda,i_L,i_R;q)},
$$
and
$$
R_{RPF}(h,h')
=
{R_{\Gamma_1}(\rho';\lambda',i_L',i_R')
\over
R_{\Gamma_1}(\rho;\lambda,i_L,i_R)}.
$$

Proof.

This is the factorization of Definition 73.2 applied before and after the
switch. `square`

### Proposition 73.4: Termwise Switch Neutrality Is Not Generic

The current corpus does not prove, and finite \(SU(N)\) representation
theory does not generically imply,
$$
R_{HK}(h,h')R_F(h,h')R_{RPF}(h,h')=1
$$
for all defined minimal corridor switches.

Proof.

If \(\lambda'\ne\lambda\), the heat-kernel ratio contains the nontrivial
factor
\((d_{\lambda'}/d_\lambda)\exp\{-t_p(C_2(\lambda')-C_2(\lambda))\}\).
This is not identically one over allowed fusion channels.  Even when
Casimir and dimension accidentally match, the recoupling coefficient ratio
need not be one term by term.  Finally, \(R_{RPF}\) is an actual residual
coefficient ratio and Papers 20--30 do not prove its invariance under local
recoupling.  Hence termwise `P30-SWITCH-NEUTRAL` is too strong unless the
switch is restricted to a special neutral sector or a new residual
quasi-invariance theorem is proved. `square`

This is not a failure of the switching idea.  It says that the nonabelian
analogue of random-current switching should not pair individual histories.
Nonabelian recoupling is linear algebra on an intertwiner space.  The right
object is a block.

## 74. Block Switching: The Correct Nonabelian Replacement

Termwise switching fails for structural reasons.  The unitary nature of
finite recoupling suggests a better formulation: group histories into a
finite local intertwiner block and switch the block by a unitary recoupling
matrix.

### Definition 74.1: Minimal Recoupling Block

Fix the external plaquette labels, boundary charge, retained scalar record,
and residual support cell of a minimal corridor.  Let
$$
\mathcal H_{\Gamma_1}^{block}
$$
be the finite-dimensional local invariant tensor space spanned by all
intertwiner labels compatible with those external data.  Let
\(U_{\Gamma_1}\) be the unitary \(F\)-move/recoupling matrix between the two
corridor bracketings.

The local signed bridge insertion is represented by a finite matrix
\(\Sigma_{\Gamma_1}\) on \(\mathcal H_{\Gamma_1}^{block}\).  The local
residual insertion is represented by a finite matrix
\(\mathcal R_{\Gamma_1}\), and the heat-kernel plaquette weights by a positive
diagonal matrix \(D_{\Gamma_1}^{HK}\).

### Definition 74.2: Block Switching Defect

Define
$$
\mathcal E_{\Gamma_1}^{block}
:=
D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}
+
U_{\Gamma_1}^{*}
D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}
U_{\Gamma_1}.
$$
This is the failure of the signed insertion to cancel after the recoupling
switch.  Exact block switching is the condition
\(\mathcal E_{\Gamma_1}^{block}=0\).

### Lemma 74.3: Block Switching Bound

The signed contribution of the minimal corridor block is bounded by
$$
\left|
\operatorname{Tr}_{\mathcal H_{\Gamma_1}^{block}}
\left(D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}\right)
\right|
\le
{1\over2}
\left\|
\mathcal E_{\Gamma_1}^{block}
\right\|_1.
$$

Proof.

The trace is invariant under unitary conjugation:
$$
\operatorname{Tr}(A)
=
\operatorname{Tr}(U^*AU).
$$
If \(A=D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}\), then
$$
2\operatorname{Tr}(A)
=
\operatorname{Tr}(A+U^*AU)
=
\operatorname{Tr}(\mathcal E_{\Gamma_1}^{block}).
$$
Taking absolute values and using \(|\operatorname{Tr}X|\le\|X\|_1\) gives
the result. `square`

### Definition 74.4: Block-Switching Source

`P30-BLOCK-SWITCH(theta,u)` asserts that the high-charge bridge tail can be
partitioned into finite recoupling blocks plus an unblocked sector of
normalized absolute mass \(u\), and that the normalized sum of block defects
satisfies
$$
{1\over Z_B^{N,j}(\eta)}
\sum_{\Gamma_1\text{ blocks}}
{1\over2}
\left\|
\mathcal E_{\Gamma_1}^{block}
\right\|_1
\le \theta.
$$

### Theorem 74.5: Block Switching Sources The Signed Tail Bound

If `P30-BLOCK-SWITCH(theta,u)` holds and
\(\theta+u\) is below the Paper-30 low-mode/tail margin, then the signed
low-mode/tail route closes.

Proof.

Apply Lemma 74.3 block by block.  The unblocked sector is paid absolutely by
\(u\).  The sum bounds the signed high-charge tail that enters the
low-mode/tail anchor. `square`

## 75. Minimal Block Audit

Block switching is a stronger and more plausible formulation than termwise
switching, but it still has an exact obstruction.

### Proposition 75.1: Exact Block Cancellation Requires Anticommutation

If \(D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\) is invertible on the block,
then exact block switching
\(\mathcal E_{\Gamma_1}^{block}=0\) is equivalent to
$$
U_{\Gamma_1}^{*}
D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}
U_{\Gamma_1}
=
-
D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}.
$$
In particular, if \(D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\) is scalar on
the block, exact cancellation reduces to
$$
U_{\Gamma_1}^{*}\Sigma_{\Gamma_1}U_{\Gamma_1}
=
-
\Sigma_{\Gamma_1}.
$$

Proof.

This is the definition of \(\mathcal E_{\Gamma_1}^{block}=0\), followed by
division by a scalar positive block weight in the scalar case. `square`

### Proposition 75.2: Current-Corpus Status Of Block Neutrality

Papers 20--30 do not prove `P30-BLOCK-SWITCH(theta,u)` in a closing range.

Proof.

The corpus proves that \(U_{\Gamma_1}\) is a legitimate finite recoupling
matrix, but it does not print:

1. the local signed insertion matrix \(\Sigma_{\Gamma_1}\) in a recoupling
   basis;
2. an anticommutation identity
   \(U_{\Gamma_1}^{*}\Sigma_{\Gamma_1}U_{\Gamma_1}=-\Sigma_{\Gamma_1}\);
3. scalarity or controlled commutator bounds for
   \(D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\) on the block;
4. a normalized trace-norm sum of block defects;
5. a bound on the unblocked sector.

Therefore block switching is not closed by the current corpus. `square`

### Corollary 75.3: The Switching Route Has Improved, But Not Closed

The minimal-corridor audit proves that termwise neutrality is generally the
wrong target.  The correct nonabelian replacement is block switching.  The
new live theorem is
$$
\boxed{
\mathrm{P30\text{-}BLOCK\text{-}SWITCH}(\theta,u)
}
$$
or, more primitively,
$$
\boxed{
U^*\Sigma U\approx-\Sigma
\quad\text{and}\quad
\left[D^{HK}\mathcal R,\Sigma\right]\ \text{small on high-charge blocks}.
}
$$

This is more concrete than `P30-SWITCH-NEUTRAL`: it asks for a finite matrix
anticommutation/commutator theorem on the actual same-law recoupling blocks.

## 76. Updated Switching Endpoint

After the minimal-corridor pass, the status is sharper:

1. the exact termwise amplitude ratio is
   \(R_{HK}R_F R_{RPF}\);
2. termwise neutrality is not generic and should not be the primary target;
3. block switching gives a same-law finite matrix inequality;
4. exact block cancellation would follow from an anticommutation identity;
5. the actual obstruction is now finite and algebraic plus residual:
   print \(\Sigma\), \(U\), \(D^{HK}\mathcal R\), then bound
   \(\|D^{HK}\mathcal R\Sigma+U^*D^{HK}\mathcal R\Sigma U\|_1\).

The next practical computation is therefore not another global source audit.
It is the minimal block table:
$$
\boxed{
\Sigma_{\Gamma_1},
\quad
U_{\Gamma_1},
\quad
D_{\Gamma_1}^{HK},
\quad
\mathcal R_{\Gamma_1}
}
$$
for the declared fundamental/dual bridge battery.

## 77. The Universal \(F\otimes F^*\) Minimal Block Table

We now print the part of the minimal block table that is fixed by
representation theory alone.  This is the first real matrix computation in
the switching route.

### Definition 77.1: Singlet/Adjoint Channel Basis

For the declared fundamental/dual battery, use the orthonormal channel basis
$$
|0\rangle:=\text{singlet channel in }F_N\otimes F_N^*,
\qquad
|A\rangle:=\text{adjoint channel in }F_N\otimes F_N^*.
$$
The minimal block space is
$$
\mathcal H_{\Gamma_1}^{block}
=
\operatorname{span}\{|0\rangle,|A\rangle\}.
$$

Set
$$
a_N={1\over N},
\qquad
b_N={\sqrt{N^2-1}\over N}.
$$

### Lemma 77.2: Universal Recoupling Matrix

In the singlet/adjoint channel basis, the fundamental/dual recoupling matrix
is
$$
U_N
=
\begin{pmatrix}
a_N & b_N\\
b_N & -a_N
\end{pmatrix}.
$$
It is real unitary and involutive:
$$
U_N^*=U_N,\qquad U_N^2=I.
$$

Proof.

This is the normalized \(SU(N)\) Fierz recoupling between the two pairings of
four fundamental/dual legs.  The coefficient \(1/N\) is the singlet overlap,
and \(\sqrt{N^2-1}/N\) is the normalized adjoint complement.  Since
\(a_N^2+b_N^2=1\), the displayed matrix is orthogonal and squares to the
identity. `square`

### Definition 77.3: Universal Heat-Kernel Diagonal

In the Paper-20 heat-kernel normalization
\(C_2^{P20}=\lambda_{HK}C_2^{std}\), the universal two-channel heat diagonal
for the minimal block is
$$
D_{\Gamma_1}^{HK}
=
\begin{pmatrix}
h_0 & 0\\
0 & h_A
\end{pmatrix},
$$
with
$$
h_0=1,
\qquad
h_A=(N^2-1)\exp\{-t_p\lambda_{HK}N\}.
$$

Here \(C_2^{std}(\mathbf 1)=0\), \(C_2^{std}(\mathrm{Ad}_N)=N\), and
\(d_{\mathrm{Ad}}=N^2-1\).

### Definition 77.4: Actual Residual And Signed Matrices

The universal table does not determine the residual insertion or the signed
observable.  Write them as actual same-law \(2\times2\) matrices
$$
\mathcal R_{\Gamma_1}
=
\begin{pmatrix}
r_{00} & r_{0A}\\
r_{A0} & r_{AA}
\end{pmatrix},
\qquad
\Sigma_{\Gamma_1}
=
\begin{pmatrix}
s_{00} & s_{0A}\\
s_{A0} & s_{AA}
\end{pmatrix}.
$$
The entries are finite DLR/Peter-Weyl coefficients of the actual residual
insertion and actual signed bridge observable in this block.  They are not
free parameters in the law, but Papers 20--30 have not printed their
numerical or symbolic values.

### Corollary 77.5: Minimal Block Table

The minimal block table is
$$
\boxed{
U_N=
\begin{pmatrix}
1/N & \sqrt{N^2-1}/N\\
\sqrt{N^2-1}/N & -1/N
\end{pmatrix},
\quad
D_{\Gamma_1}^{HK}
=
\begin{pmatrix}
1&0\\
0&(N^2-1)e^{-t_p\lambda_{HK}N}
\end{pmatrix},
\quad
\mathcal R_{\Gamma_1},
\quad
\Sigma_{\Gamma_1}.
}
$$

Only the first two matrices are universal.  The last two are the actual-law
data that must be computed or bounded.

## 78. Exact Block Defect In Projection Form

The block defect becomes especially transparent if the unitary recoupling is
viewed as an involution.

### Definition 78.1: \(U_N\)-Even Projection

For any \(2\times2\) matrix \(X\), define
$$
\Pi_{+}^{U}(X)
:=
{1\over2}(X+U_N^*XU_N),
\qquad
\Pi_{-}^{U}(X)
:=
{1\over2}(X-U_N^*XU_N).
$$

Let
$$
A_{\Gamma_1}
:=
D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}.
$$

### Lemma 78.2: Block Defect Is The \(U_N\)-Even Part

The minimal block defect satisfies
$$
\mathcal E_{\Gamma_1}^{block}
=
2\Pi_{+}^{U}(A_{\Gamma_1}).
$$
Consequently
$$
{1\over2}
\left\|
\mathcal E_{\Gamma_1}^{block}
\right\|_1
=
\left\|
\Pi_{+}^{U}
\left(
D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}
\right)
\right\|_1.
$$

Proof.

This is Definition 74.2 and Definition 78.1. `square`

### Corollary 78.3: Exact Minimal Block-Switch Criterion

Exact cancellation on the minimal block is equivalent to
$$
\Pi_{+}^{U}
\left(
D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}
\right)=0.
$$
Thus the correct target is not that \(\Sigma_{\Gamma_1}\) itself is odd.  The
weighted signed matrix \(D^{HK}\mathcal R\Sigma\) must be odd under
conjugation by \(U_N\).

## 79. The Optimistic Switch-Odd Test

There is one natural real switch-odd matrix in the singlet/adjoint block:
$$
\Sigma_{odd}
=
\begin{pmatrix}
b_N&-a_N\\
-a_N&-b_N
\end{pmatrix}.
$$
It satisfies
$$
U_N^*\Sigma_{odd}U_N=-\Sigma_{odd}.
$$

This is the most favorable possible real signed insertion if the heat and
residual weights were scalar on the block.

### Lemma 79.1: Heat Splitting Alone Produces Leakage

Assume \(\mathcal R_{\Gamma_1}=I\) and
\(\Sigma_{\Gamma_1}=\Sigma_{odd}\).  Then
$$
\mathcal E_{\Gamma_1}^{block}
=
(h_0-h_A)b_N\,I_2.
$$
Hence
$$
{1\over2}
\left\|
\mathcal E_{\Gamma_1}^{block}
\right\|_1
=
|h_0-h_A|\,b_N
$$
in the two-dimensional trace norm.

Proof.

Using
$$
D^{HK}\Sigma_{odd}
=
\begin{pmatrix}
h_0b_N&-h_0a_N\\
-h_Aa_N&-h_Ab_N
\end{pmatrix}
$$
and
$$
U_N^*D^{HK}\Sigma_{odd}U_N
=
\begin{pmatrix}
-h_Ab_N&h_0a_N\\
h_Aa_N&h_0b_N
\end{pmatrix},
$$
their sum is \((h_0-h_A)b_NI_2\).  The trace norm of a scalar multiple of
\(I_2\) is twice the absolute scalar. `square`

### Proposition 79.2: The Universal Minimal Block Does Not Close By Pure
Oddness

The universal singlet/adjoint block does not prove
`P30-BLOCK-SWITCH(theta,u)` by the pure switch-odd insertion alone unless
\(|h_0-h_A|b_N\) is already below the signed tail margin.

Proof.

Lemma 79.1 gives the exact defect even in the optimistic case
\(\mathcal R=I\).  In the small-time or large-\(N\) regimes, \(h_0\) and
\(h_A\) need not be close.  Therefore switch-oddness of the signed insertion
is insufficient; the actual residual matrix must either compensate the heat
splitting, remove the singlet leakage, or the block must be restricted to a
sector where \(D^{HK}\mathcal R\) is effectively scalar/odd-compatible.
`square`

## 80. The New Exact Subgate

The minimal block table gives a precise next theorem:
$$
\boxed{
\mathrm{P30\text{-}BLOCK\text{-}EVEN\text{-}SMALL}(\theta)
}
$$
asserting
$$
\limsup_{(N,j)}
{1\over Z_B^{N,j}(\eta)}
\sum_{\Gamma_1\text{ blocks}}
\left\|
\Pi_+^U
\left(D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}\right)
\right\|_1
\le\theta.
$$

`P30-BLOCK-EVEN-SMALL(theta)` plus the unblocked-sector debit \(u\) is
exactly `P30-BLOCK-SWITCH(theta,u)`.

This is the sharpest current form of the nonabelian switching program:
compute or bound the \(U_N\)-even part of the actual weighted signed block.
No Markovian hidden process is introduced; this is a finite matrix question
inside the same Peter-Weyl expansion of the actual DLR law.

## 81. Algebraic Normal Form Of The Block-Even Projection

We now expand the exact \(2\times2\) obstruction.  This is the first place
where the block-switching route becomes genuinely sharper than the previous
signed-bridge abstractions: the four entries of the actual weighted signed
block reduce to two scalar defects.

### Definition 81.1: Weighted Signed Block Entries

Write
$$
C_{\Gamma_1}:=\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}
=
\begin{pmatrix}
c_{00}&c_{0A}\\
c_{A0}&c_{AA}
\end{pmatrix}
$$
and
$$
A_{\Gamma_1}:=D_{\Gamma_1}^{HK}C_{\Gamma_1}
=
\begin{pmatrix}
p&q\\
r&s
\end{pmatrix},
$$
where
$$
p=h_0c_{00},\qquad
q=h_0c_{0A},\qquad
r=h_Ac_{A0},\qquad
s=h_Ac_{AA}.
$$

The entries may be complex.  They are finite same-law Peter-Weyl
coefficients of the actual adaptive `SEL2` residual/signed insertion; no
probabilistic hidden trajectory is being introduced.

### Definition 81.2: The Two Block Defects

Define
$$
\delta_1:=p+s,
$$
and
$$
\delta_2:=b_N(q+r)+a_N(p-s).
$$

Equivalently, in the original residual/signed entries,
$$
\delta_1
=h_0c_{00}+h_Ac_{AA},
$$
and
$$
\delta_2
=b_N(h_0c_{0A}+h_Ac_{A0})
+a_N(h_0c_{00}-h_Ac_{AA}).
$$

### Lemma 81.3: Exact Two-Defect Formula

For every \(2\times2\) weighted signed block,
$$
\Pi_+^U(A_{\Gamma_1})
=
{1\over2}
\begin{pmatrix}
\delta_1+a_N\delta_2&b_N\delta_2\\
b_N\delta_2&\delta_1-a_N\delta_2
\end{pmatrix}
=
{1\over2}\left(\delta_1 I+\delta_2 U_N\right).
$$

Proof.

For
$$
A=
\begin{pmatrix}
p&q\\
r&s
\end{pmatrix}
$$
and
$$
U_N=
\begin{pmatrix}
a_N&b_N\\
b_N&-a_N
\end{pmatrix},
$$
direct multiplication gives
$$
U_NAU_N
=
\begin{pmatrix}
a_N^2p+a_Nb_N(q+r)+b_N^2s&
a_Nb_N(p-s)+b_N^2r-a_N^2q\\
a_Nb_N(p-s)+b_N^2q-a_N^2r&
b_N^2p-a_Nb_N(q+r)+a_N^2s
\end{pmatrix}.
$$
Adding \(A\), using \(a_N^2+b_N^2=1\), and dividing by two gives the
displayed expression. `square`

### Corollary 81.4: Exact Cancellation Criterion

Exact block cancellation,
$$
\Pi_+^U(A_{\Gamma_1})=0,
$$
is equivalent to the two scalar conditions
$$
\delta_1=0,
\qquad
\delta_2=0.
$$
That is,
$$
h_0c_{00}+h_Ac_{AA}=0
$$
and
$$
b_N(h_0c_{0A}+h_Ac_{A0})
+a_N(h_0c_{00}-h_Ac_{AA})=0.
$$

Equivalently, if \(b_N\ne0\),
$$
h_Ac_{AA}=-h_0c_{00},
$$
and
$$
h_0c_{0A}+h_Ac_{A0}
=
-{2a_N\over b_N}\,h_0c_{00}.
$$

These are the heat-compensated block-oddness equations.  They are stronger
and more accurate than asking \(\Sigma_{\Gamma_1}\) alone to be switch-odd.

### Corollary 81.5: Exact Trace-Norm Formula

The singular values of \(\Pi_+^U(A_{\Gamma_1})\) are
$$
{1\over2}\left|\delta_1+\delta_2\right|,
\qquad
{1\over2}\left|\delta_1-\delta_2\right|.
$$
Hence
$$
\left\|\Pi_+^U(A_{\Gamma_1})\right\|_1
=
{1\over2}
\left(
\left|\delta_1+\delta_2\right|
+
\left|\delta_1-\delta_2\right|
\right).
$$
In the real-entry case this simplifies to
$$
\left\|\Pi_+^U(A_{\Gamma_1})\right\|_1
=
\max\{|\delta_1|,|\delta_2|\}.
$$

Proof.

Lemma 81.3 diagonalizes in the \(U_N\)-eigenbasis, with eigenvalues
\((\delta_1+\delta_2)/2\) and \((\delta_1-\delta_2)/2\).  Because this matrix
is normal even for complex \(\delta_1,\delta_2\), its singular values are the
absolute values of these eigenvalues. `square`

## 82. Current-Corpus No-Go For A Purely Universal Proof

The two-defect formula lets us state the honest negative result sharply.  The
universal \(F\otimes F^*\) data decide \(U_N\), \(h_0\), and \(h_A\).  They do
not decide \(\delta_1\) or \(\delta_2\).

### Proposition 82.1: Universal Data And Norm Envelopes Do Not Force
Block-Even Smallness

No proof of `P30-BLOCK-EVEN-SMALL(theta)` can use only:

1. the universal recoupling matrix \(U_N\);
2. the heat-kernel diagonal \(D^{HK}\);
3. support on the singlet/adjoint block;
4. a scalar magnitude envelope on the entries of the weighted block
   \(A_{\Gamma_1}=D^{HK}\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}\);
5. finite-label admissibility data.

Proof.

Fix any \(m>0\).  Consider two same-label \(2\times2\) assignments for the
weighted signed block \(A=D^{HK}C\).

First, the exact-cancelling assignment
$$
p=m,\qquad
s=-m,\qquad
q+r=-{2a_N\over b_N}m
$$
has \(\delta_1=\delta_2=0\), so its block-even defect is zero.

Second, the even assignment
$$
p=m,\qquad
s=m,\qquad
q=r=0
$$
has
$$
\delta_1=2m,\qquad
\delta_2=0,
$$
so
$$
\left\|\Pi_+^U(A)\right\|_1=m
$$
in the real trace-norm formula of Corollary 81.5.

Both assignments have the same universal \(U_N\), the same heat diagonal, the
same block support, and comparable scalar entry size.  For any scalar
envelope that allows entries of size \(m\), both assignments are permitted by
the listed data.  If an envelope itself forced \(m\le\theta\), that envelope
would already be the missing quantitative same-law value theorem, not a
consequence of universal recoupling or finite labels.  Therefore the listed
data do not logically imply small block-even defect.  Any closing proof must
use additional same-law value information about the actual entries of
\(D^{HK}\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}\). `square`

### Corollary 82.2: More Finite Labels Still Do Not Move This Obstruction

Refining the canonical labels can locate which \(\Gamma_1\) block is being
used, but it cannot decide whether \(\delta_1\) and \(\delta_2\) vanish or
are small.  The missing datum is not the identity of the block.  It is the
same-law value of the weighted signed residual matrix on that block.

This is the block-switching analogue of the Paper-26 and Paper-29 verdicts:
finite labels can expose the live entry, but they do not evaluate the actual
conditional amplitude.

## 83. The Positive Theorem Now Needed

The exact algebra suggests the only plausible positive theorem inside this
route.

### Definition 83.1: Heat-Compensated Block-Oddness Source

For \(\theta\ge0\), `P30-HKCOMP-BLOCK-ODD(theta)` asserts that cofinally
$$
\limsup_{(N,j)}
{1\over Z_B^{N,j}(\eta)}
\sum_{\Gamma_1\text{ blocks}}
{1\over2}
\left(
\left|\delta_1(\Gamma_1)+\delta_2(\Gamma_1)\right|
+
\left|\delta_1(\Gamma_1)-\delta_2(\Gamma_1)\right|
\right)
\le\theta,
$$
where \(\delta_1,\delta_2\) are the actual same-law defects from Definition
81.2.

Equivalently, this says the actual weighted signed matrix
$$
D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}
$$
is \(U_N\)-odd up to total normalized defect \(\theta\).

### Lemma 83.2: Heat-Compensated Block-Oddness Is Exactly The Block-Even
Subgate

`P30-HKCOMP-BLOCK-ODD(theta)` is equivalent to
`P30-BLOCK-EVEN-SMALL(theta)`.

Proof.

This is Corollary 81.5 inserted into the definition of
`P30-BLOCK-EVEN-SMALL(theta)` from Section 80. `square`

### Theorem 83.3: Positive Closure From The Heat-Compensated Source

If `P30-HKCOMP-BLOCK-ODD(theta)` holds and the unblocked-sector debit is
bounded by \(u\), then
$$
\mathrm{P30\text{-}BLOCK\text{-}SWITCH}(\theta,u)
$$
holds.  Consequently the nonabelian switching route closes whenever the
previous Paper-30 signed-tail margin admits the total debit \(\theta+u\).

Proof.

Lemma 83.2 gives `P30-BLOCK-EVEN-SMALL(theta)`.  Section 80 proves that this
plus the unblocked-sector debit \(u\) is exactly
`P30-BLOCK-SWITCH(theta,u)`.  The earlier switching theorem then feeds this
block switch into the signed high-charge tail estimate. `square`

### Remark 83.4: Why This Is Barandes-Aligned

`P30-HKCOMP-BLOCK-ODD(theta)` is not a hidden Markovian mechanism.  It does
not introduce a stochastic trajectory beneath the finite DLR law.  It is an
identity or inequality among Peter-Weyl coefficients of the same actual
finite parent law after pushing forward to the adaptive `SEL2` scalar
records.  The only admissible sources for it are same-law sources: exact
recoupling identities, finite Schwinger-Dyson/Ward identities, controlled
Peter-Weyl tails, or an explicit evaluation of the finite residual/signed
matrix.

## 84. The Floor Alternative Is Not Automatic

The no-go in Section 82 is not a lower-floor theorem.  It only says current
universal data are insufficient.

### Definition 84.1: Block-Even Floor Witness

`P30-BLOCK-EVEN-FLOOR-WIT(M_*)` asserts that the surviving block-even defect
is sign-coherent with the actual RPF predebit ledger and forces
$$
\overline\Lambda_{13}^{RPF}\ge M_*.
$$
Concretely, it must supply a same-law inequality converting the normalized
block-even mass
$$
{1\over Z_B^{N,j}(\eta)}
\sum_{\Gamma_1\text{ blocks}}
\left\|
\Pi_+^U
\left(D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}\right)
\right\|_1
$$
into a positive retained RPF debit rather than allowing it to cancel in the
signed bridge ledger.

### Lemma 84.2: Floor Witness Falsifies Adaptive Branch A

If `P30-BLOCK-EVEN-FLOOR-WIT(M_*)` holds, then adaptive Branch A is falsified.

Proof.

Adaptive Branch A requires the actual RPF predebit to remain strictly below
the Paper-22/Paper-23 threshold \(M_*\).  The witness gives the opposite
same-law lower bound. `square`

### Proposition 84.3: Failure Of Block-Even Smallness Does Not By Itself
Prove The Floor

The negation of `P30-BLOCK-EVEN-SMALL(theta)` does not imply
`P30-BLOCK-EVEN-FLOOR-WIT(M_*)`.

Proof.

Failure of block-even smallness gives only a large signed or complex
block-even residual in the switching ledger.  A lower floor requires the
same residual to contribute with the correct sign to the RPF predebit ledger
and to survive all retained cancellations.  Sections 36, 42, and 64 already
prove this distinction for the previous signed-defect routes; the
two-defect block algebra does not change it.  One can have a large
\(\delta_1\) or \(\delta_2\) in the signed block while its contribution to
the predebit ledger cancels or lies outside the retained floor account.
Therefore a separate sign-coherent witness is required. `square`

## 85. Paper-30 Endpoint After The Block Algebra

The live theorem has now been reduced to the following exact fork:
$$
\boxed{
\mathrm{P30\text{-}HKCOMP\text{-}BLOCK\text{-}ODD}(\theta)
\quad\text{or}\quad
\mathrm{P30\text{-}BLOCK\text{-}EVEN\text{-}FLOOR\text{-}WIT}(M_*).
}
$$

The first is the positive Branch-A route: prove that the two same-law defects
$$
\delta_1=h_0c_{00}+h_Ac_{AA},
$$
and
$$
\delta_2=b_N(h_0c_{0A}+h_Ac_{A0})
+a_N(h_0c_{00}-h_Ac_{AA})
$$
are small in normalized signed-tail average.

The second is the honest negative closure: prove that the surviving
block-even defect is not merely large but sign-coherently contributes to the
RPF predebit floor.

What is closed:

1. the universal \(F\otimes F^*\) block table;
2. the exact \(U_N\)-even projection formula;
3. the exact trace-norm formula for the block defect;
4. the current-corpus no-go for a proof using only universal data, finite
   labels, or scalar envelopes;
5. the precise Barandes-aligned positive source now needed.

What remains open:

1. a same-law source for the two defects \(\delta_1,\delta_2\);
2. or a sign-coherent floor witness.

This is progress, but it is not an unconditional confinement proof.  Paper
30 has narrowed the obstruction to two explicit same-law scalar combinations
inside the actual adaptive `SEL2` Peter-Weyl block.

## 86. Exact Finite-DLR Formulas For The Two Defects

The next step is to remove the last notational ambiguity from \(p,q,r,s\).
They are not adjustable matrix entries.  They are exact finite-DLR
Peter-Weyl coefficients of the same parent law from Definition 11.2.

### Definition 86.1: Minimal-Block Matrix Coefficient Insertions

Fix a parent finite bridge region \(B\), a parent boundary \(\eta\), and one
minimal fundamental/dual bridge block \(\Gamma_1\).  Let
$$
\alpha,\beta\in\{0,A\}
$$
denote the singlet and adjoint channel labels from Section 77.

Let
$$
\Phi_{\alpha\beta}^{\Gamma_1}(g,\eta)
$$
be the finite spin-network matrix coefficient obtained by:

1. projecting the chosen minimal bridge block to input channel \(\beta\) and
   output channel \(\alpha\);
2. inserting the signed bridge observable after the retained-row,
   endpoint-additive, and HK-symmetric removals already licensed in Paper 30;
3. leaving the actual residual insertion
   \(\mathcal R_B^{N,j}=e^{-V_{RPF}}J_{tree}\) and all heat-kernel factors in
   the same finite DLR density.

The weighted signed block entries are the exact unnormalized finite-DLR
coefficients
$$
a_{\alpha\beta}^{N,j}(\eta;\Gamma_1)
:=
\int_{G^m}
\Phi_{\alpha\beta}^{\Gamma_1}(g,\eta)
\left(
\prod_{p\cap B\ne\varnothing}
H_{t_p}(h_p(g,\eta))
\right)
e^{-V_{RPF}(g,\eta)}
J_{tree}(g,\eta)\,dg.
$$

Equivalently,
$$
A_{\Gamma_1}
=
\begin{pmatrix}
a_{00}&a_{0A}\\
a_{A0}&a_{AA}
\end{pmatrix}
=
D_{\Gamma_1}^{HK}\mathcal R_{\Gamma_1}\Sigma_{\Gamma_1}.
$$
Thus
$$
p=a_{00},\qquad q=a_{0A},\qquad r=a_{A0},\qquad s=a_{AA}.
$$

This definition is deliberately parent-law exact.  The scalar adaptive
`SEL2` law sees these numbers only after the deterministic pushforward, but
the computation is performed inside the same finite DLR law whose
pushforward defines the scalar law.  The normalizing factor
\(Z_B^{N,j}(\eta)\) is applied only when the block sum is inserted into
`P30-BLOCK-EVEN-SMALL(theta)`, as in Section 80.

### Definition 86.2: Defect Insertions

Define the two defect insertions
$$
\Phi_1^{\Gamma_1}
:=
\Phi_{00}^{\Gamma_1}+\Phi_{AA}^{\Gamma_1},
$$
and
$$
\Phi_2^{\Gamma_1}
:=
b_N(\Phi_{0A}^{\Gamma_1}+\Phi_{A0}^{\Gamma_1})
+a_N(\Phi_{00}^{\Gamma_1}-\Phi_{AA}^{\Gamma_1}).
$$

### Lemma 86.3: The Defects Are Exact Expectations

For every finite row and every admissible parent boundary,
$$
{\delta_1(\Gamma_1)\over Z_B^{N,j}(\eta)}
=
E_{K_B^{par}(\cdot\mid\eta)}
\left[\Phi_1^{\Gamma_1}\right],
$$
and
$$
{\delta_2(\Gamma_1)\over Z_B^{N,j}(\eta)}
=
E_{K_B^{par}(\cdot\mid\eta)}
\left[\Phi_2^{\Gamma_1}\right].
$$

Proof.

Insert Definition 86.1 into Definition 81.2 and divide the resulting
unnormalized coefficient by \(Z_B^{N,j}(\eta)\).  The two linear combinations
in Definition 86.2 are exactly
$$
p+s
$$
and
$$
b_N(q+r)+a_N(p-s).
$$
`square`

### Corollary 86.4: Trace Interpretation

Equivalently,
$$
\delta_1=\operatorname{Tr}(A_{\Gamma_1}),
\qquad
\delta_2=\operatorname{Tr}(U_NA_{\Gamma_1}).
$$

Thus the obstruction is the pair of \(U_N\)-even trace coordinates of the
actual weighted signed block.  This is why finite label refinement cannot
remove the obstruction: it can identify \(A_{\Gamma_1}\), but it cannot
evaluate its two trace coordinates.

## 87. The Targeted Defect-Ward Identity

We now specialize the finite Ward identity from Section 62 to the two defect
insertions \(\Phi_1,\Phi_2\).

### Definition 87.1: Defect Ward Decomposition

Let \(\Psi\) be either \(\Phi_1^{\Gamma_1}\) or \(\Phi_2^{\Gamma_1}\).  A
finite defect Ward decomposition of \(\Psi\) consists of:

1. internal parent edges \(\ell\) and Lie algebra basis directions \(a\);
2. smooth finite DLR observables \(F_{\ell,a}^{\Psi}\);
3. a controlled cohomological/collar remainder \(R_{\Psi}\);

such that on the same chart and essential-support cell,
$$
\Psi
=
\sum_{\ell,a} X_{\ell,a}F_{\ell,a}^{\Psi}
+R_{\Psi}.
$$
Here \(X_{\ell,a}\) is the left-invariant vector field on edge \(\ell\) in
direction \(a\).

### Lemma 87.2: Exact Defect Ward Formula

For \(\Psi\in\{\Phi_1^{\Gamma_1},\Phi_2^{\Gamma_1}\}\), any finite defect
Ward decomposition gives
$$
E_{K_B^{par}}[\Psi]
=
E_{K_B^{par}}[R_{\Psi}]
-
\sum_{\ell,a}
E_{K_B^{par}}
\left[
F_{\ell,a}^{\Psi}
X_{\ell,a}\log {dK_B^{par}\over dg}
\right].
$$

Moreover,
$$
X_{\ell,a}\log {dK_B^{par}\over dg}
=
\sum_{p\cap B\ne\varnothing}
X_{\ell,a}\log H_{t_p}(h_p)
-
X_{\ell,a}V_{RPF}
+
X_{\ell,a}\log J_{tree}.
$$

Proof.

Apply Lemma 62.1 to each \(F_{\ell,a}^{\Psi}\) and sum.  The second display
is Definition 11.2 differentiated in the finite chart; the normalizer
\(Z_B^{N,j}(\eta)\) is independent of the integration variable \(g\).
`square`

### Definition 87.3: Defect Ward Residuals

After the already licensed heat-kernel Schwinger-Dyson, retained-row,
endpoint-additive, and HK-symmetric removals, define the unnormalized
residuals
$$
\mathcal W_i^{\Gamma_1}
$$
for \(i=1,2\) to be \(Z_B^{N,j}(\eta)\) times the remaining right-hand side
in Lemma 87.2 when \(\Psi=\Phi_i^{\Gamma_1}\).  Explicitly, it is the
unnormalized expectation of the collar remainder plus the residual/Jacobian
score terms
$$
X_{\ell,a}V_{RPF},
\qquad
X_{\ell,a}\log J_{tree},
$$
and any unremoved off-sheet/Bianchi defect terms.

The equality
$$
\delta_i(\Gamma_1)=\mathcal W_i^{\Gamma_1}
$$
is exact once the decomposition and removals are fixed.

## 88. The Defect-Ward Closing Source

The targeted Ward identity gives a precise positive theorem, but it does not
make the residual small for free.

### Definition 88.1: Defect-Ward Smallness Source

For \(\theta\ge0\), `P30-DEFECT-WARD(theta)` asserts that finite defect Ward
decompositions exist for the two defect insertions on the declared cofinal
selector and that
$$
\limsup_{(N,j)}
{1\over Z_B^{N,j}(\eta)}
\sum_{\Gamma_1\text{ blocks}}
{1\over2}
\left(
\left|\mathcal W_1^{\Gamma_1}+\mathcal W_2^{\Gamma_1}\right|
+
\left|\mathcal W_1^{\Gamma_1}-\mathcal W_2^{\Gamma_1}\right|
\right)
\le\theta.
$$

### Theorem 88.2: Defect-Ward Smallness Closes The Block-Even Subgate

`P30-DEFECT-WARD(theta)` implies
`P30-HKCOMP-BLOCK-ODD(theta)`, hence
`P30-BLOCK-EVEN-SMALL(theta)`.

Proof.

By Definition 87.3,
$$
\delta_i(\Gamma_1)=\mathcal W_i^{\Gamma_1}
\qquad (i=1,2).
$$
Insert this into the trace-norm formula of Corollary 81.5 and sum over the
blocks.  This is exactly Definition 83.1. `square`

### Corollary 88.3: Ward Route To Nonabelian Switching

If `P30-DEFECT-WARD(theta)` holds and the unblocked-sector debit is \(u\),
then
$$
\mathrm{P30\text{-}BLOCK\text{-}SWITCH}(\theta,u)
$$
holds.  If the earlier signed-tail margin admits \(\theta+u\), the
nonabelian switching route closes.

Proof.

Theorem 88.2 gives the block-even subgate.  Apply Theorem 83.3. `square`

## 89. Why The Targeted Ward Route Is Still A New Theorem

The targeted Ward pass is valuable because it names the exact residual that
must be small.  It does not, by itself, prove smallness.

### Proposition 89.1: Current Corpus Does Not Prove `P30-DEFECT-WARD(theta)`
In A Closing Range

Papers 20--30 do not prove `P30-DEFECT-WARD(theta)` for a \(\theta\) small
enough to close the signed-tail margin.

Proof.

Section 62 proves the finite compact-Lie integration-by-parts identity.
Sections 20--21 and the earlier Paper-30 audits remove heat-kernel tangent,
retained-row, endpoint-additive, and HK-symmetric pieces.  What remains in
Definition 87.3 is the actual residual/Jacobian score contribution:
$$
X_{\ell,a}V_{RPF},
\qquad
X_{\ell,a}\log J_{tree},
$$
together with collar/off-sheet terms.  No current paper proves that these
terms have the sign, cancellation, or small norm required by Definition
88.1.

Equivalently, the two defect insertions \(\Phi_1,\Phi_2\) are the trace
coordinates of the actual weighted signed block.  A Ward identity can control
them only after one prints either:

1. exact divergence primitives with controlled collar remainders;
2. score-orthogonality of those primitives against the actual residual
   score;
3. a Peter-Weyl tail theorem for the residual score;
4. or a sign-coherent floor witness.

None of these four value theorems is printed in the present corpus.
`square`

### Corollary 89.2: The Ward Route Is Barandes-Aligned But Not Smuggled

`P30-DEFECT-WARD(theta)` is Barandes-aligned because it is an exact identity
inside the same finite DLR law and its deterministic `SEL2` pushforward.  It
does not introduce a hidden stochastic process or a Markovian subdynamics.
But it is also not a magic cancellation principle: the residual score must be
bounded or shown to cancel by a same-law theorem.

## 90. Paper-30 Endpoint After The Defect-Ward Pass

Paper 30 has now pushed the nonabelian switching idea as far as the present
corpus permits.

The positive route is the chain
$$
\boxed{
\mathrm{P30\text{-}DEFECT\text{-}WARD}(\theta)
\Longrightarrow
\mathrm{P30\text{-}HKCOMP\text{-}BLOCK\text{-}ODD}(\theta)
\Longleftrightarrow
\mathrm{P30\text{-}BLOCK\text{-}EVEN\text{-}SMALL}(\theta).
}
$$

The negative route is the independent same-law floor witness
$$
\boxed{
\mathrm{P30\text{-}BLOCK\text{-}EVEN\text{-}FLOOR\text{-}WIT}(M_*).
}
$$

What was gained in this pass:

1. \(p,q,r,s\) are now exact finite-DLR/Peter-Weyl integrals, not placeholders;
2. \(\delta_1,\delta_2\) are exact expectations of two explicit defect
   insertions \(\Phi_1,\Phi_2\);
3. the Ward identity has been targeted at precisely those two insertions;
4. the exact residual Ward terms are isolated;
5. the route is shown to remain Barandes-aligned and non-Markovian.

What is still not proved:

1. smallness of the residual/Jacobian score terms in Definition 87.3;
2. exact divergence primitives with vanishing collar remainder;
3. a residual-score Peter-Weyl tail theorem;
4. or a sign-coherent lower-floor witness.

Thus the next genuinely new theorem cannot be another structural reduction.
It must be one of:

$$
\boxed{
\mathrm{P30\text{-}DEFECT\text{-}WARD}(\theta),
\quad
\mathrm{P30\text{-}RESID\text{-}SCORE\text{-}TAIL},
\quad
\mathrm{P30\text{-}BLOCK\text{-}EVEN\text{-}FLOOR\text{-}WIT}(M_*).
}
$$

This is still not an unconditional confinement proof, but the remaining
Branch-A obstruction is now a concrete same-law score/value theorem for the
two block defects, not a bookkeeping ambiguity.

## 91. Residual-Score Object

The defect-Ward pass reduces the positive route to the residual/Jacobian
score terms.  We now isolate that object exactly.

### Definition 91.1: Residual Score

For an internal parent edge \(\ell\) and Lie algebra direction \(a\), define
the residual score
$$
S_{\ell,a}^{RPF}(g,\eta)
:=
-X_{\ell,a}V_{RPF}(g,\eta)
+X_{\ell,a}\log J_{tree}(g,\eta).
$$

The heat-kernel score
$$
\sum_{p\cap B\ne\varnothing}X_{\ell,a}\log H_{t_p}(h_p)
$$
is not included in \(S_{\ell,a}^{RPF}\), because the heat-kernel tangent
terms are precisely the pieces already removed by the HKSD and
HK-symmetric audits.  Collar/off-sheet terms are recorded separately.

### Definition 91.2: Score Pairings For The Two Defects

For \(i\in\{1,2\}\), let \(F_{\ell,a}^{i,\Gamma_1}\) be a defect-Ward
primitive for \(\Phi_i^{\Gamma_1}\), as in Definition 87.1.  Define the
unnormalized residual-score pairing
$$
\mathcal P_{i,\ell,a}^{\Gamma_1}
:=
\int_{G^m}
F_{\ell,a}^{i,\Gamma_1}(g,\eta)
S_{\ell,a}^{RPF}(g,\eta)
\left(
\prod_{p\cap B\ne\varnothing}
H_{t_p}(h_p(g,\eta))
\right)
e^{-V_{RPF}(g,\eta)}
J_{tree}(g,\eta)\,dg.
$$

Let \(\mathcal C_i^{\Gamma_1}\) denote the unnormalized collar/off-sheet
remainder after the licensed removals.  Then
$$
\mathcal W_i^{\Gamma_1}
=
\mathcal C_i^{\Gamma_1}
+
\sum_{\ell,a}\mathcal P_{i,\ell,a}^{\Gamma_1}.
$$

### Lemma 91.3: Residual Score Is The Exact Remaining Ward Source

After the licensed heat-kernel, retained-row, endpoint-additive, and
HK-symmetric removals, the only bulk score left in the two-defect Ward
identity is \(S_{\ell,a}^{RPF}\).

Proof.

Lemma 87.2 decomposes the finite DLR score as
$$
\sum_{p\cap B\ne\varnothing}X_{\ell,a}\log H_{t_p}(h_p)
-
X_{\ell,a}V_{RPF}
+
X_{\ell,a}\log J_{tree}.
$$
The first term is the heat-kernel score and is removed by the licensed HKSD
and HK-symmetric audits.  The remaining two bulk terms are exactly Definition
91.1.  All non-bulk defects are, by definition, placed in the collar
remainders \(\mathcal C_i^{\Gamma_1}\). `square`

## 92. Peter-Weyl Low-Mode Plus Tail Split For The Score Pairing

The score-tail theorem must be same-law.  Therefore the projection is a
projection of the actual finite integrand, not of a comparison process.

### Definition 92.1: Weighted Pairing Functions

Let
$$
\rho_B^{N,j}(g,\eta)
:=
\left(
\prod_{p\cap B\ne\varnothing}
H_{t_p}(h_p(g,\eta))
\right)
e^{-V_{RPF}(g,\eta)}
J_{tree}(g,\eta).
$$

On \(L^2(G^m,dg)\), set
$$
G_{i,\ell,a}^{\Gamma_1}
:=
F_{\ell,a}^{i,\Gamma_1}\sqrt{\rho_B^{N,j}},
\qquad
T_{\ell,a}^{RPF}
:=
S_{\ell,a}^{RPF}\sqrt{\rho_B^{N,j}}.
$$
Then
$$
\mathcal P_{i,\ell,a}^{\Gamma_1}
=
\left\langle
G_{i,\ell,a}^{\Gamma_1},
T_{\ell,a}^{RPF}
\right\rangle_{L^2(dg)}
$$
with the convention that complex conjugation is carried by the Hilbert-space
inner product.

### Definition 92.2: Peter-Weyl Projection

Let \(\Pi_{\le L}\) be the finite Peter-Weyl projection on the \(G^m\) chart,
retaining all irreducible tensor modes with declared cutoff at most \(L\).
Define
$$
\mathcal P_{i,\ell,a}^{\Gamma_1,\le L}
:=
\left\langle
\Pi_{\le L}G_{i,\ell,a}^{\Gamma_1},
\Pi_{\le L}T_{\ell,a}^{RPF}
\right\rangle,
$$
and
$$
\mathcal P_{i,\ell,a}^{\Gamma_1,>L}
:=
\mathcal P_{i,\ell,a}^{\Gamma_1}
-
\mathcal P_{i,\ell,a}^{\Gamma_1,\le L}.
$$

The low-mode term is a finite matrix entry.  The tail term is the omitted
same-law Peter-Weyl complement.

### Lemma 92.3: Cauchy-Schwarz Score Tail Bound

For every \(\Gamma_1,i,\ell,a\),
$$
\left|
\mathcal P_{i,\ell,a}^{\Gamma_1,>L}
\right|
\le
\left\|(I-\Pi_{\le L})G_{i,\ell,a}^{\Gamma_1}\right\|_2
\left\|T_{\ell,a}^{RPF}\right\|_2
+
\left\|\Pi_{\le L}G_{i,\ell,a}^{\Gamma_1}\right\|_2
\left\|(I-\Pi_{\le L})T_{\ell,a}^{RPF}\right\|_2.
$$

Proof.

Write
$$
G=\Pi_{\le L}G+(I-\Pi_{\le L})G,
\qquad
T=\Pi_{\le L}T+(I-\Pi_{\le L})T.
$$
Because \(\Pi_{\le L}\) is an orthogonal projection, the cross pairing
between \(\Pi_{\le L}G\) and \((I-\Pi_{\le L})T\) vanishes if both functions
are projected in the same Peter-Weyl basis.  The displayed bound is the
slightly more conservative two-tail estimate and follows by Cauchy-Schwarz.
`square`

### Remark 92.4: Why This Split Is Barandes-Aligned

This is not a hidden Markov chain, a comparison dynamics, or an auxiliary
measure.  It is the Peter-Weyl decomposition of the actual finite DLR
integrand \(\rho_B^{N,j}\), exactly as in Sections 66 and 86.  The only new
input requested is quantitative decay of the actual residual-score
coefficients.

## 93. The Residual-Score Tail Source

We can now state the next positive theorem in a form that can be proved,
falsified, or numerically audited on a finite row.

### Definition 93.1: Low-Mode Defect-Ward Table

For a cutoff \(L\), define
$$
\mathcal W_i^{\Gamma_1,\le L}
:=
\mathcal C_i^{\Gamma_1,\le L}
+
\sum_{\ell,a}
\mathcal P_{i,\ell,a}^{\Gamma_1,\le L},
$$
where \(\mathcal C_i^{\Gamma_1,\le L}\) is the retained low-mode collar
contribution.

Define the normalized low-mode defect size
$$
\Theta_L^{score}
:=
\limsup_{(N,j)}
{1\over Z_B^{N,j}(\eta)}
\sum_{\Gamma_1\text{ blocks}}
{1\over2}
\left(
\left|
\mathcal W_1^{\Gamma_1,\le L}
+
\mathcal W_2^{\Gamma_1,\le L}
\right|
+
\left|
\mathcal W_1^{\Gamma_1,\le L}
-
\mathcal W_2^{\Gamma_1,\le L}
\right|
\right).
$$

### Definition 93.2: Residual-Score Tail Source

`P30-RESID-SCORE-TAIL(L,Theta_L,r_L)` asserts:

1. the low-mode table of Definition 93.1 is printed or bounded by
   \(\Theta_L^{score}\le\Theta_L\);
2. the omitted collar and residual-score Peter-Weyl complement contributes
   at most \(r_L\), namely
   $$
   \limsup_{(N,j)}
   {1\over Z_B^{N,j}(\eta)}
   \sum_{\Gamma_1\text{ blocks}}
   {1\over2}
   \left(
   \left|
   \mathcal W_1^{\Gamma_1,>L}
   +
   \mathcal W_2^{\Gamma_1,>L}
   \right|
   +
   \left|
   \mathcal W_1^{\Gamma_1,>L}
   -
   \mathcal W_2^{\Gamma_1,>L}
   \right|
   \right)
   \le r_L.
   $$

Here
$$
\mathcal W_i^{\Gamma_1,>L}
:=
\mathcal W_i^{\Gamma_1}
-
\mathcal W_i^{\Gamma_1,\le L}.
$$

### Theorem 93.3: Score-Tail Source Implies Defect-Ward Smallness

If `P30-RESID-SCORE-TAIL(L,Theta_L,r_L)` holds, then
$$
\mathrm{P30\text{-}DEFECT\text{-}WARD}(\Theta_L+r_L)
$$
holds.

Proof.

For each block,
$$
\mathcal W_i^{\Gamma_1}
=
\mathcal W_i^{\Gamma_1,\le L}
+
\mathcal W_i^{\Gamma_1,>L}.
$$
Apply the triangle inequality to the two combinations
\(\mathcal W_1+\mathcal W_2\) and \(\mathcal W_1-\mathcal W_2\), then sum
over blocks and divide by \(Z_B^{N,j}(\eta)\).  Definition 93.2 gives the
bound \(\Theta_L+r_L\). `square`

### Corollary 93.4: Score-Tail Route To Block Switching

If `P30-RESID-SCORE-TAIL(L,Theta_L,r_L)` holds and the unblocked-sector debit
is \(u\), then
$$
\mathrm{P30\text{-}BLOCK\text{-}SWITCH}(\Theta_L+r_L,u)
$$
holds.  The signed high-charge route closes whenever the earlier Paper-30
signed-tail margin admits the total debit \(\Theta_L+r_L+u\).

Proof.

Theorem 93.3 gives `P30-DEFECT-WARD(Theta_L+r_L)`.  Apply Corollary 88.3.
`square`

## 94. Current-Corpus Verdict For The Score-Tail Route

The score-tail theorem is now exact.  The current corpus still does not prove
it in a closing range.

### Proposition 94.1: `P30-RESID-SCORE-TAIL` Is Not Sourced By Papers 20--30

Papers 20--30 do not prove `P30-RESID-SCORE-TAIL(L,Theta_L,r_L)` with
\(\Theta_L+r_L\) inside the signed-tail margin.

Proof.

Paper 28 defines the same-law Peter-Weyl tail problem for actual residual
RN-MIXAMP objects and proves that the present corpus supplies neither
finite-band support nor coefficient decay nor a cofinal numerical tail
schedule.  Paper 29 shows that even low-mode entries of the actual residual
law are not determined by the RN-MIXAMP ratios alone.

The present score object is at least as demanding: it contains derivatives of
the residual potential and Jacobian,
$$
-X_{\ell,a}V_{RPF},
\qquad
X_{\ell,a}\log J_{tree},
$$
weighted by the same finite DLR density and paired against the defect-Ward
primitives.  Differentiating the residual insertion can increase high
Peter-Weyl modes rather than damp them.  Therefore the existing residual-tail
gaps from Papers 28--29 do not automatically improve for the score object.

The low-mode table \(\Theta_L^{score}\) is also not printed.  It is a finite
same-law table, but it requires actual values of the finite integrals in
Definition 92.2.  No current paper evaluates those integrals or bounds them
strictly enough for the signed-tail margin. `square`

### Corollary 94.2: What Would Actually Prove The Score-Tail Source

To prove `P30-RESID-SCORE-TAIL`, one must supply at least one of:

1. a finite low-mode table for the score pairings plus a cofinal
   Peter-Weyl tail bound;
2. a residual-score coefficient decay theorem strong enough to make
   \(r_L\to0\) while \(\Theta_L\) stays below the signed-tail margin;
3. an exact score-orthogonality theorem making the low-mode pairings vanish
   or cancel in the two defect combinations;
4. a direct finite-row computation of the two defect Ward residuals with
   certified interval bounds.

These are genuine same-law quantitative value theorems.  They are not more
finite labels.

## 95. Floor Route From A Large Residual Score

A failed score-tail bound does not automatically falsify adaptive Branch A.
It must be converted into a lower-floor witness.

### Definition 95.1: Residual-Score Floor Witness

`P30-RESID-SCORE-FLOOR-WIT(M_*)` asserts that the residual-score contribution
surviving in Definition 91.2 is sign-coherent with the actual RPF predebit
ledger and forces
$$
\overline\Lambda_{13}^{RPF}\ge M_*.
$$

Equivalently, it supplies a same-law inequality converting the large
residual-score mass into retained RPF predebit rather than allowing it to
cancel in the signed bridge or Ward ledger.

### Lemma 95.2: Score Floor Witness Implies The Block-Even Floor Witness

`P30-RESID-SCORE-FLOOR-WIT(M_*)` implies
`P30-BLOCK-EVEN-FLOOR-WIT(M_*)`.

Proof.

The block-even defect is exactly the normalized Ward defect by Sections
86--88.  If the score part of that Ward defect is sign-coherent with the RPF
predebit and forces the threshold \(M_*\), then the block-even defect itself
has the floor witness required in Definition 84.1. `square`

### Proposition 95.3: Failure Of `P30-RESID-SCORE-TAIL` Is Not A Floor

The negation of `P30-RESID-SCORE-TAIL(L,Theta_L,r_L)` does not imply
`P30-RESID-SCORE-FLOOR-WIT(M_*)`.

Proof.

Failure of a low-mode-plus-tail sufficient condition may occur because the
chosen cutoff is too small, the Cauchy-Schwarz tail bound is crude, or the
score pairings are large but sign-cancelling in the RPF predebit ledger.
None of those alternatives gives the sign-coherent lower bound required by
Definition 95.1.  This is the same logical distinction already isolated for
RN-MIXAMP, primitive residual values, and block-even defects. `square`

## 96. Paper-30 Endpoint After The Score-Tail Pass

The positive score route is now the explicit chain
$$
\boxed{
\mathrm{P30\text{-}RESID\text{-}SCORE\text{-}TAIL}(L,\Theta_L,r_L)
\Longrightarrow
\mathrm{P30\text{-}DEFECT\text{-}WARD}(\Theta_L+r_L)
\Longrightarrow
\mathrm{P30\text{-}HKCOMP\text{-}BLOCK\text{-}ODD}(\Theta_L+r_L).
}
$$

The negative score route is
$$
\boxed{
\mathrm{P30\text{-}RESID\text{-}SCORE\text{-}FLOOR\text{-}WIT}(M_*)
\Longrightarrow
\mathrm{P30\text{-}BLOCK\text{-}EVEN\text{-}FLOOR\text{-}WIT}(M_*).
}
$$

What is now closed:

1. the exact residual score \(S_{\ell,a}^{RPF}\);
2. the exact bilinear score pairings with the two defect-Ward primitives;
3. the Peter-Weyl low-mode-plus-tail split for those pairings;
4. the conditional theorem from score-tail bounds to defect-Ward smallness;
5. the logical separation between score-tail failure and a lower floor.

What remains open:

1. a printed finite low-mode score table;
2. a residual-score Peter-Weyl decay/tail theorem;
3. score-orthogonality against the two defect primitives;
4. or a sign-coherent residual-score floor witness.

This is the most concrete form of the Paper-30 obstruction.  The next
positive theorem must bound actual residual-score pairings on the same
finite DLR law.

## 97. Finite Heat-Kernel Stein Operator

The score-tail route asks for raw Peter-Weyl decay of the residual score.
That may be too strong: differentiating \(V_{RPF}\) can increase high modes.
The more targeted route is a finite Stein/Ward identity.  It tests whether
the two defect insertions are transverse to the residual score.

This is still same-law and Barandes-aligned.  The heat-kernel operator below
is an analytic inverse on the same finite compact chart.  It is not a hidden
Markov process and it does not replace the actual finite DLR law.

### Definition 97.1: Heat-Kernel Reference Density

On the same tree-gauge chart \(G^m\) and parent boundary \(\eta\), define
the heat-kernel reference density
$$
d\nu_{HK,B}^{N,j}(g\mid\eta)
:=
{1\over Z_{HK,B}^{N,j}(\eta)}
\left(
\prod_{p\cap B\ne\varnothing}
H_{t_p}(h_p(g,\eta))
\right)dg.
$$

The actual finite DLR law from Definition 11.2 is absolutely continuous with
respect to this reference law:
$$
dK_B^{par}(g\mid\eta)
=
{R_B^{N,j}(g,\eta)\over
E_{\nu_{HK,B}^{N,j}}[R_B^{N,j}(\cdot,\eta)]}
d\nu_{HK,B}^{N,j}(g\mid\eta),
$$
where
$$
R_B^{N,j}(g,\eta)
:=
e^{-V_{RPF}(g,\eta)}J_{tree}(g,\eta).
$$

### Definition 97.2: Heat-Kernel Dirichlet Operator

Let
$$
\mathcal E_{HK}(f,g)
:=
\sum_{\ell,a}
E_{\nu_{HK,B}^{N,j}}
\left[
X_{\ell,a}f\,
X_{\ell,a}g
\right]
$$
on smooth functions modulo constants.  Let
$$
\mathcal A_{HK,B}^{N,j}
$$
be the nonnegative self-adjoint operator satisfying
$$
E_{\nu_{HK,B}^{N,j}}
\left[
f\,\mathcal A_{HK,B}^{N,j}g
\right]
=
\mathcal E_{HK}(f,g).
$$

Because \(B\) is finite and the heat-kernel density is smooth and strictly
positive on the compact group chart, \(\mathcal A_{HK,B}^{N,j}\) has constants
as its kernel and is invertible on the finite-energy mean-zero subspace.

### Definition 97.3: Stein Potentials For The Defect Insertions

For each minimal block \(\Gamma_1\) and each defect insertion
\(\Phi_i^{\Gamma_1}\), \(i=1,2\), define the heat-reference mean
$$
m_i^{\Gamma_1}
:=
E_{\nu_{HK,B}^{N,j}}
\left[
\Phi_i^{\Gamma_1}
\right],
$$
and choose the mean-zero Stein potential \(U_i^{\Gamma_1}\) solving
$$
\mathcal A_{HK,B}^{N,j}U_i^{\Gamma_1}
=
\Phi_i^{\Gamma_1}-m_i^{\Gamma_1}.
$$

This equation is finite-row exact.  It is a compact-group Poisson equation,
not an added dynamics.

### Lemma 97.4: Finite Stein Identity For Each Defect

For every block \(\Gamma_1\) and \(i=1,2\),
$$
{ \delta_i(\Gamma_1)\over Z_B^{N,j}(\eta)}
=
m_i^{\Gamma_1}
+
E_{K_B^{par}(\cdot\mid\eta)}
\left[
\sum_{\ell,a}
X_{\ell,a}U_i^{\Gamma_1}\,
S_{\ell,a}^{RPF}
\right].
$$

Proof.

By Lemma 86.3,
$$
{\delta_i(\Gamma_1)\over Z_B^{N,j}(\eta)}
=
E_{K_B^{par}}\left[\Phi_i^{\Gamma_1}\right].
$$
Use Definition 97.3:
$$
\Phi_i^{\Gamma_1}
=
m_i^{\Gamma_1}
+
\mathcal A_{HK,B}^{N,j}U_i^{\Gamma_1}.
$$
Let
$$
R=
R_B^{N,j},
\qquad
dK_B^{par}={R\over E_{\nu_{HK}}R}d\nu_{HK}.
$$
Then, by the defining integration-by-parts identity for
\(\mathcal A_{HK}\),
$$
E_{K_B^{par}}
\left[
\mathcal A_{HK}U_i
\right]
=
{1\over E_{\nu_{HK}}R}
E_{\nu_{HK}}
\left[
R\,\mathcal A_{HK}U_i
\right]
=
{1\over E_{\nu_{HK}}R}
\sum_{\ell,a}
E_{\nu_{HK}}
\left[
X_{\ell,a}R\,X_{\ell,a}U_i
\right].
$$
Since
$$
X_{\ell,a}\log R
=
-X_{\ell,a}V_{RPF}
+
X_{\ell,a}\log J_{tree}
=
S_{\ell,a}^{RPF},
$$
the last display equals the \(K_B^{par}\)-expectation of
\(\sum_{\ell,a}X_{\ell,a}U_iS_{\ell,a}^{RPF}\). `square`

## 98. Score-Orthogonality Source

The Stein identity separates the problem into a heat-reference neutrality
term and an actual residual-score transversality term.

### Definition 98.1: Heat-Reference Defect Debit

Define
$$
\Xi_{HK}^{N,j}
:=
\sum_{\Gamma_1\text{ blocks}}
{1\over2}
\left(
\left|m_1^{\Gamma_1}+m_2^{\Gamma_1}\right|
+
\left|m_1^{\Gamma_1}-m_2^{\Gamma_1}\right|
\right).
$$

`P30-HKREF-DEFECT-NEUTRAL(epsilon_0)` asserts
$$
\limsup_{(N,j)}
\Xi_{HK}^{N,j}
\le\epsilon_0.
$$

### Definition 98.2: Defect-Score Orthogonality Debit

Define the score pairings
$$
O_i^{\Gamma_1}
:=
E_{K_B^{par}(\cdot\mid\eta)}
\left[
\sum_{\ell,a}
X_{\ell,a}U_i^{\Gamma_1}\,
S_{\ell,a}^{RPF}
\right],
\qquad i=1,2.
$$

Then set
$$
\Xi_{score}^{N,j}
:=
\sum_{\Gamma_1\text{ blocks}}
{1\over2}
\left(
\left|O_1^{\Gamma_1}+O_2^{\Gamma_1}\right|
+
\left|O_1^{\Gamma_1}-O_2^{\Gamma_1}\right|
\right).
$$

`P30-DEFECT-SCORE-ORTHO(epsilon_s)` asserts
$$
\limsup_{(N,j)}
\Xi_{score}^{N,j}
\le\epsilon_s.
$$

### Theorem 98.3: Score-Orthogonality Implies Defect-Ward Smallness

If `P30-HKREF-DEFECT-NEUTRAL(epsilon_0)` and
`P30-DEFECT-SCORE-ORTHO(epsilon_s)` hold, then
$$
\mathrm{P30\text{-}DEFECT\text{-}WARD}(\epsilon_0+\epsilon_s)
$$
holds.

Proof.

By Lemma 97.4,
$$
{\delta_i(\Gamma_1)\over Z_B^{N,j}(\eta)}
=
m_i^{\Gamma_1}+O_i^{\Gamma_1}.
$$
Insert this into the two-combination norm
$$
{1\over2}
\left(
\left|\delta_1/Z_B+\delta_2/Z_B\right|
+
\left|\delta_1/Z_B-\delta_2/Z_B\right|
\right)
$$
and apply the triangle inequality, first to the \(m\)-part and then to the
\(O\)-part.  The two hypotheses give the cofinal bound
\(\epsilon_0+\epsilon_s\). `square`

### Corollary 98.4: Score-Orthogonality Route To Block Switching

If the hypotheses of Theorem 98.3 hold and the unblocked-sector debit is
\(u\), then
$$
\mathrm{P30\text{-}BLOCK\text{-}SWITCH}(\epsilon_0+\epsilon_s,u)
$$
holds.  The signed high-charge route closes whenever the earlier Paper-30
signed-tail margin admits \(\epsilon_0+\epsilon_s+u\).

Proof.

Apply Theorem 98.3 and Corollary 88.3. `square`

## 99. Transversality Audit

We now test what the current corpus can say about the two new debits.

### Lemma 99.1: Heat-Reference Neutrality Is A Concrete Finite Test

`P30-HKREF-DEFECT-NEUTRAL(epsilon_0)` is decided by the heat-kernel reference
finite integrals
$$
m_i^{\Gamma_1}
=
E_{\nu_{HK,B}^{N,j}}
\left[
\Phi_i^{\Gamma_1}
\right].
$$

If the defect insertions are exactly odd under a heat-reference involution
preserving \(\nu_{HK,B}^{N,j}\), then \(\epsilon_0=0\).

Proof.

The first statement is Definition 98.1.  For the second, pair every
configuration with its involutive image.  The reference density is invariant
and the insertion changes sign, so the integral cancels. `square`

### Proposition 99.2: Current Corpus Does Not Print The Needed
Heat-Reference Involution

Papers 20--30 do not prove `P30-HKREF-DEFECT-NEUTRAL(0)` for the two
Stein defect insertions.

Proof.

Earlier Paper-30 sections remove heat-kernel tangent, HK-symmetric, retained
row, and endpoint-additive pieces, and Section 79 proves that pure
switch-oddness of \(\Sigma\) is not enough once the heat diagonal is
present.  The current defect insertions \(\Phi_1,\Phi_2\) include the
heat-compensated block combinations from Section 81.  No printed theorem
identifies an involution preserving \(\nu_{HK,B}^{N,j}\) and making those
two insertions odd after all collar and boundary choices are fixed. `square`

### Proposition 99.3: Current Corpus Does Not Prove Score Orthogonality

Papers 20--30 do not prove `P30-DEFECT-SCORE-ORTHO(epsilon_s)` in a closing
range.

Proof.

The score pairing
$$
O_i^{\Gamma_1}
=
E_{K_B^{par}}
\left[
\sum_{\ell,a}
X_{\ell,a}U_i^{\Gamma_1}S_{\ell,a}^{RPF}
\right]
$$
depends on the actual residual/Jacobian score and the Stein potential of the
defect insertion.  Papers 28--29 already show that the current corpus does
not print low-mode values or same-law Peter-Weyl tails for the actual
residual law.  Section 94 strengthens this for the residual score.  The
Stein potential narrows the test but does not evaluate the pairing.  No
current result proves orthogonality, transversality, or sign cancellation of
\(S_{\ell,a}^{RPF}\) against \(X_{\ell,a}U_i^{\Gamma_1}\). `square`

### Corollary 99.4: What A Positive Transversality Theorem Must Say

A genuine positive theorem must provide at least one of:

1. a heat-reference involution proving \(\epsilon_0=0\);
2. explicit finite values for \(m_i^{\Gamma_1}\) and \(O_i^{\Gamma_1}\);
3. a score-orthogonality identity
   \(E_K[\sum XU_i\,S^{RPF}]=0\) or a small bound;
4. a Stein-Peter-Weyl tail theorem for \(XU_i\) and \(S^{RPF}\);
5. a sign-coherent floor witness if the score is not transverse.

These are same-law quantitative theorems, not label refinements.

## 100. Floor Alternative From Non-Transversality

If score-orthogonality fails, the failure is useful only if it has the right
sign in the RPF predebit ledger.

### Definition 100.1: Stein-Score Floor Witness

`P30-STEIN-SCORE-FLOOR-WIT(M_*)` asserts that the Stein score pairings
\(O_i^{\Gamma_1}\), after the heat-reference debit and licensed removals,
contribute sign-coherently to the retained RPF predebit and force
$$
\overline\Lambda_{13}^{RPF}\ge M_*.
$$

### Lemma 100.2: Stein-Score Floor Witness Implies The Previous Floor

`P30-STEIN-SCORE-FLOOR-WIT(M_*)` implies
`P30-RESID-SCORE-FLOOR-WIT(M_*)`, hence
`P30-BLOCK-EVEN-FLOOR-WIT(M_*)`.

Proof.

The Stein score pairings are a refined decomposition of the residual-score
contribution from Definition 91.2.  If this refined contribution is already
sign-coherent and reaches the RPF predebit threshold, then the coarser
residual-score floor witness and the block-even floor witness follow.
`square`

### Proposition 100.3: Non-Orthogonality Is Not A Floor

The failure of `P30-DEFECT-SCORE-ORTHO(epsilon_s)` does not imply
`P30-STEIN-SCORE-FLOOR-WIT(M_*)`.

Proof.

Large score pairings can occur with cancellations between \(i=1\) and
\(i=2\), between blocks, or between the signed Ward ledger and the RPF
predebit ledger.  A lower floor requires sign coherence and survival in the
retained RPF account.  Non-orthogonality alone is only a failed sufficient
positive estimate. `square`

## 101. Peter-Weyl Tails As Support For Orthogonality

Peter-Weyl tails are now a supporting tool rather than the first bet.

### Definition 101.1: Stein-Projected Score Pairing

Let
$$
\Pi_{\le L}
$$
be the same finite Peter-Weyl projection used in Section 92.  Define
$$
O_i^{\Gamma_1,\le L}
:=
E_{K_B^{par}}
\left[
\sum_{\ell,a}
\Pi_{\le L}(X_{\ell,a}U_i^{\Gamma_1})\,
\Pi_{\le L}(S_{\ell,a}^{RPF})
\right],
$$
and set
$$
O_i^{\Gamma_1,>L}:=
O_i^{\Gamma_1}-O_i^{\Gamma_1,\le L}.
$$

### Definition 101.2: Stein-Peter-Weyl Orthogonality Source

`P30-STEIN-PW-ORTHO(L,epsilon_L,r_L)` asserts:

1. the low-mode Stein score combinations obey
   $$
   \limsup_{(N,j)}
   \sum_{\Gamma_1\text{ blocks}}
   {1\over2}
   \left(
   \left|O_1^{\Gamma_1,\le L}+O_2^{\Gamma_1,\le L}\right|
   +
   \left|O_1^{\Gamma_1,\le L}-O_2^{\Gamma_1,\le L}\right|
   \right)
   \le\epsilon_L;
   $$
2. the omitted complement obeys the analogous bound with \(r_L\).

### Lemma 101.3: Stein-Peter-Weyl Orthogonality Implies Score Orthogonality

`P30-STEIN-PW-ORTHO(L,epsilon_L,r_L)` implies
`P30-DEFECT-SCORE-ORTHO(epsilon_L+r_L)`.

Proof.

Use
$$
O_i^{\Gamma_1}
=
O_i^{\Gamma_1,\le L}
+
O_i^{\Gamma_1,>L}
$$
and apply the triangle inequality to the two combinations
\(O_1+O_2\) and \(O_1-O_2\). `square`

### Proposition 101.4: Current Corpus Does Not Prove The Stein-Peter-Weyl
Source

Papers 20--30 do not prove
`P30-STEIN-PW-ORTHO(L,epsilon_L,r_L)` in a closing range.

Proof.

This source requires the low-mode values of the Stein score pairings and a
tail for both \(XU_i\) and \(S^{RPF}\) on the actual finite DLR law.  Section
94 proves that the residual-score tail is not printed.  Sections 97--99 add
the Stein potential \(U_i\), but they do not print its low-mode table or
tail after multiplication by the actual residual score.  Thus the source is
well-defined and narrower than raw score-tail, but still unsourced by the
current corpus. `square`

## 102. Paper-30 Endpoint After The Stein/Ward Orthogonality Pass

The positive route inside Paper 30 is now:
$$
\boxed{
\mathrm{P30\text{-}HKREF\text{-}DEFECT\text{-}NEUTRAL}(\epsilon_0)
+
\mathrm{P30\text{-}DEFECT\text{-}SCORE\text{-}ORTHO}(\epsilon_s)
\Longrightarrow
\mathrm{P30\text{-}DEFECT\text{-}WARD}(\epsilon_0+\epsilon_s).
}
$$

A Peter-Weyl route can support the score-orthogonality term:
$$
\boxed{
\mathrm{P30\text{-}STEIN\text{-}PW\text{-}ORTHO}(L,\epsilon_L,r_L)
\Longrightarrow
\mathrm{P30\text{-}DEFECT\text{-}SCORE\text{-}ORTHO}(\epsilon_L+r_L).
}
$$

The negative route is:
$$
\boxed{
\mathrm{P30\text{-}STEIN\text{-}SCORE\text{-}FLOOR\text{-}WIT}(M_*)
\Longrightarrow
\mathrm{P30\text{-}BLOCK\text{-}EVEN\text{-}FLOOR\text{-}WIT}(M_*).
}
$$

What this pass closes:

1. a finite compact-group Stein operator on the heat-kernel reference chart;
2. the Poisson equation for the two defect insertions;
3. the exact Stein identity expressing the actual defect as heat-reference
   mean plus residual-score pairing;
4. the sufficient score-orthogonality theorem;
5. the floor alternative from non-transversality;
6. the Peter-Weyl support route for the orthogonality term.

What remains open:

1. heat-reference defect neutrality or a printed heat-reference defect
   table;
2. score-orthogonality against \(S_{\ell,a}^{RPF}\);
3. Stein-Peter-Weyl low-mode values and tails;
4. or a Stein-score lower-floor witness.

This is still not an unconditional confinement proof.  But Paper 30 has now
turned the remaining Branch-A obstruction into the most surgical same-law
question currently visible:
$$
\boxed{
\text{Are the two defect Stein gradients orthogonal, in the actual finite
DLR law, to the residual/Jacobian score?}
}
$$

## 103. Heat-Reference Neutrality: Exact Minimal-Block Test

Before attacking the residual score, we test the heat-reference debit
\(\epsilon_0\).  This is the cleanest possible subproblem because it removes
the actual residual/Jacobian factor and asks only what the heat-kernel
reference law says about the two defect insertions.

### Definition 103.1: Heat-Reference Block Mean Matrix

For each minimal block \(\Gamma_1\), define
$$
M_{\Gamma_1}^{HK}
:=
\begin{pmatrix}
\mu_{00}&\mu_{0A}\\
\mu_{A0}&\mu_{AA}
\end{pmatrix},
$$
where
$$
\mu_{\alpha\beta}
:=
E_{\nu_{HK,B}^{N,j}}
\left[
\Phi_{\alpha\beta}^{\Gamma_1}
\right],
\qquad
\alpha,\beta\in\{0,A\}.
$$
Then the heat-reference defect means are
$$
m_1^{\Gamma_1}
=
\operatorname{Tr}(M_{\Gamma_1}^{HK})
=
\mu_{00}+\mu_{AA},
$$
and
$$
m_2^{\Gamma_1}
=
\operatorname{Tr}(U_NM_{\Gamma_1}^{HK})
=
a_N(\mu_{00}-\mu_{AA})
+b_N(\mu_{0A}+\mu_{A0}).
$$

Proof.

This is Definition 86.2 and Corollary 86.4 with the actual finite DLR
expectation replaced by the heat-reference expectation of Definition 97.3.
`square`

### Corollary 103.2: Heat-Reference Neutrality Is A Two-Trace Test

Exact heat-reference neutrality on the minimal block is equivalent to
$$
\operatorname{Tr}(M_{\Gamma_1}^{HK})=0,
\qquad
\operatorname{Tr}(U_NM_{\Gamma_1}^{HK})=0.
$$
Equivalently,
$$
\mu_{00}+\mu_{AA}=0,
\qquad
a_N(\mu_{00}-\mu_{AA})
+b_N(\mu_{0A}+\mu_{A0})=0.
$$

Thus the heat-reference problem is finite and explicit.  It is not a
question of more labels.

## 104. Candidate Heat-Reference Involutions

There are two natural candidate symmetries on the minimal block:

1. the recoupling involution \(U_N\);
2. the diagonal phase involution
   $$
   P:=
   \begin{pmatrix}
   1&0\\
   0&-1
   \end{pmatrix}.
   $$

We now check both.

### Lemma 104.1: The Recoupling Involution Is Not A Heat-Reference Symmetry
Unless \(h_0=h_A\)

The heat-reference two-channel weight
$$
D^{HK}
=
\begin{pmatrix}
h_0&0\\
0&h_A
\end{pmatrix}
$$
is invariant under conjugation by \(U_N\) if and only if \(h_0=h_A\).

Proof.

Direct multiplication gives
$$
U_ND^{HK}U_N
=
\begin{pmatrix}
a_N^2h_0+b_N^2h_A&a_Nb_N(h_0-h_A)\\
a_Nb_N(h_0-h_A)&b_N^2h_0+a_N^2h_A
\end{pmatrix}.
$$
This equals \(D^{HK}\) only if the off-diagonal entry vanishes and the
diagonal entries match.  Since \(a_Nb_N\ne0\) for \(N>1\), this requires
\(h_0=h_A\).  The converse is immediate. `square`

### Corollary 104.2: Universal \(U_N\)-Oddness Cannot Prove
`P30-HKREF-DEFECT-NEUTRAL(0)`

A proof of heat-reference neutrality cannot rely only on \(U_N\)-oddness of
the defect insertion, because the heat-reference weight is not generally
\(U_N\)-invariant.

Proof.

If a measure or weighted finite block is not invariant under the proposed
involution, pairing an insertion with its \(U_N\)-image does not cancel its
expectation.  Lemma 104.1 shows that the minimal heat-reference weight fails
this invariance unless \(h_0=h_A\).  In the actual rows,
$$
h_0=1,
\qquad
h_A=(N^2-1)e^{-t_p\lambda_{HK}N},
$$
and equality is not a structural identity. `square`

### Lemma 104.3: The Phase Involution Preserves The Heat Diagonal But Does
Not Force The Two Defects To Vanish

The phase involution \(P=\operatorname{diag}(1,-1)\) commutes with
\(D^{HK}\), hence preserves the two-channel heat diagonal.  If the
heat-reference block mean is covariant under this phase convention, namely
\(M_{\Gamma_1}^{HK}=PM_{\Gamma_1}^{HK}P\), then its off-diagonal block means
are forced to vanish:
$$
\mu_{0A}=\mu_{A0}=0.
$$
The diagonal means \(\mu_{00},\mu_{AA}\) are not forced to vanish.

Proof.

Since \(P D^{HK}P=D^{HK}\), \(P\) is compatible with the diagonal heat
weights.  But conjugation by \(P\) sends
$$
\begin{pmatrix}
\mu_{00}&\mu_{0A}\\
\mu_{A0}&\mu_{AA}
\end{pmatrix}
\mapsto
\begin{pmatrix}
\mu_{00}&-\mu_{0A}\\
-\mu_{A0}&\mu_{AA}
\end{pmatrix}.
$$
Covariance \(M_{\Gamma_1}^{HK}=PM_{\Gamma_1}^{HK}P\) therefore gives
\(\mu_{0A}=-\mu_{0A}\) and \(\mu_{A0}=-\mu_{A0}\), hence the off-diagonal
means vanish.  The diagonal entries are unchanged by \(P\).  Since the
heat-reference defect combinations contain the diagonal traces from
Corollary 103.2, a phase symmetry that merely removes off-diagonal terms does
not prove both heat-reference defects vanish.
`square`

### Corollary 104.4: The Only Universal Symmetry Tests Are Insufficient

The two obvious universal symmetries do not close
`P30-HKREF-DEFECT-NEUTRAL(0)`:

1. \(U_N\) would give the right cancellation but does not preserve the heat
   diagonal unless \(h_0=h_A\);
2. \(P\) preserves the heat diagonal but does not force the diagonal trace
   defects to vanish.

Therefore heat-reference neutrality requires either an actual finite
heat-reference table \(M_{\Gamma_1}^{HK}\) or a more refined same-law
involution involving the full parent heat-kernel graph, not just the
universal two-channel block.

## 105. Optimistic Switch-Odd Heat-Reference Debit

The failure above is not merely qualitative.  In the most favorable
switch-odd two-channel insertion from Section 79, the heat-reference debit is
exactly the heat-splitting leakage already seen in the block-switching
defect.

### Lemma 105.1: Switch-Odd Heat-Reference Means

Assume the heat-reference signed insertion on the minimal block is the
optimistic switch-odd matrix
$$
\Sigma_{odd}
=
\begin{pmatrix}
b_N&-a_N\\
-a_N&-b_N
\end{pmatrix}.
$$
With no residual/Jacobian factor, the weighted heat-reference block is
$$
M_{odd}^{HK}=D^{HK}\Sigma_{odd}.
$$
Then
$$
m_1=(h_0-h_A)b_N,
\qquad
m_2=0.
$$

Proof.

Here
$$
M_{odd}^{HK}
=
\begin{pmatrix}
h_0b_N&-h_0a_N\\
-h_Aa_N&-h_Ab_N
\end{pmatrix}.
$$
Therefore
$$
m_1=\operatorname{Tr}(M_{odd}^{HK})=(h_0-h_A)b_N.
$$
Also
$$
m_2=\operatorname{Tr}(U_NM_{odd}^{HK})
=
b_N(-h_0a_N-h_Aa_N)
+a_N(h_0b_N+h_Ab_N)=0.
$$
`square`

### Corollary 105.2: The Optimistic Heat-Reference Debit

For the optimistic switch-odd insertion,
$$
{1\over2}
\left(
|m_1+m_2|+|m_1-m_2|
\right)
=
|h_0-h_A|\,b_N.
$$

This is exactly the leakage from Lemma 79.1.  Hence pure switch-oddness
cannot supply \(\epsilon_0=0\) unless the singlet/adjoint heat weights are
equal, or unless a non-universal parent-graph cancellation removes the
diagonal heat-splitting term.

## 106. Heat-Reference Neutrality Verdict

The heat-reference neutrality test is now settled as far as universal
two-channel representation theory can take it.

### Theorem 106.1: Universal Minimal-Block Heat-Reference Neutrality Fails

The current universal minimal-block data do not prove
`P30-HKREF-DEFECT-NEUTRAL(0)`.  More strongly, for the most favorable
switch-odd local insertion, the heat-reference debit is
$$
|h_0-h_A|\,b_N.
$$

Proof.

Corollary 104.4 proves that the two universal candidate symmetries are
insufficient.  Corollary 105.2 computes the debit in the optimistic
switch-odd case and gives a nonzero value whenever \(h_0\ne h_A\). `square`

### Corollary 106.2: What Can Still Rescue Heat-Reference Neutrality

The remaining options for the heat-reference term are exactly:

1. print the finite heat-reference table \(M_{\Gamma_1}^{HK}\) and show the
   two trace combinations are small;
2. find a parent-graph heat-reference involution, beyond the local
   two-channel \(U_N\) and \(P\), that cancels the diagonal leakage;
3. show the leakage is within the signed-tail margin for the declared
   cofinal selector;
4. abandon \(\epsilon_0=0\) and absorb the explicit heat-reference debit into
   the score-orthogonality budget;
5. if the heat-reference debit is large and sign-coherent in the retained RPF
   predebit ledger, try the floor route.

### Proposition 106.3: Current Corpus Does Not Prove Any Rescue Option

Papers 20--30 do not currently print a closing proof of any of the five
rescue options in Corollary 106.2.

Proof.

The finite table \(M_{\Gamma_1}^{HK}\) has not been printed beyond the
universal two-channel heat diagonal and the optimistic switch-odd probe.  No
parent-graph heat-reference involution cancelling the diagonal leakage is
printed.  The paper has not compared \(|h_0-h_A|b_N\), summed over the
cofinal block family, to the final signed-tail margin in a closing range.
Nor has it proved sign coherence of this heat-reference debit in the RPF
predebit ledger. `square`

## 107. Updated Paper-30 Endpoint After The Heat-Reference Test

The first subgate of the positive Stein route has been attacked.  Universal
heat-reference neutrality does not close.  The route now has the sharper
form:
$$
\boxed{
\epsilon_0^{HK}
=
\limsup
\sum_{\Gamma_1}
{1\over2}
\left(
|m_1^{\Gamma_1}+m_2^{\Gamma_1}|
+
|m_1^{\Gamma_1}-m_2^{\Gamma_1}|
\right),
}
$$
where \(m_i\) are computed from the actual heat-reference table
\(M_{\Gamma_1}^{HK}\).

The positive branch must prove
$$
\boxed{
\epsilon_0^{HK}
+
\epsilon_s^{score}
\quad\text{fits inside the signed-tail margin.}
}
$$

The universal optimistic switch-odd probe already contains the heat-splitting
debit
$$
|h_0-h_A|\,b_N.
$$

Thus the next useful attack is not another universal local involution.  It is
one of:

1. print the actual heat-reference block table and margin-test
   \(\epsilon_0^{HK}\);
2. find a nonlocal parent-graph heat-reference cancellation;
3. compute/bound the score-orthogonality debit \(\epsilon_s^{score}\) tightly
   enough to absorb the heat debit;
4. or prove a floor witness if the heat debit is sign-coherent and too large.

This completes the first attack on the three routes: the heat-reference
neutrality route is not universally closed, but it has been reduced to an
explicit finite table plus margin test.

## 108. Heat-Debit Margin Test

We now attack the third rescue option in Corollary 106.2: perhaps the
heat-reference debit is nonzero but small enough to fit inside the signed
tail margin.

### Definition 108.1: Available Signed-Tail Margin

Fix the common minimal-edge tail debit \(\kappa\), the unblocked-sector debit
\(u\), and a proposed score-orthogonality debit \(\epsilon_s\).  Define the
available heat-reference budget
$$
\mathfrak M_{HK}(\kappa,u,\epsilon_s)
:=
M_{\mathrm{sgn}}(\kappa)-u-\epsilon_s,
$$
where
$$
M_{\mathrm{sgn}}(\kappa)
=
2\,\operatorname{arsinh}(B_*^{edge}-\kappa).
$$

The heat-reference debit can be absorbed only if
$$
\epsilon_0^{HK}<\mathfrak M_{HK}(\kappa,u,\epsilon_s).
$$

### Lemma 108.2: Universal Optimistic Absorption Condition

For the optimistic switch-odd two-channel probe, absorption of the
heat-reference debit requires
$$
|1-(N^2-1)e^{-t_p\lambda_{HK}N}|\,
{\sqrt{N^2-1}\over N}
<
\mathfrak M_{HK}(\kappa,u,\epsilon_s).
$$

Proof.

Corollary 105.2 gives the optimistic heat-reference debit
$$
|h_0-h_A|b_N.
$$
Section 77 gives
$$
h_0=1,
\qquad
h_A=(N^2-1)e^{-t_p\lambda_{HK}N},
\qquad
b_N={\sqrt{N^2-1}\over N}.
$$
Insert these in the budget condition from Definition 108.1. `square`

### Definition 108.3: Adjoint-Balance Window

Set
$$
\Delta_{HK}(N,\kappa,u,\epsilon_s)
:=
{N\over\sqrt{N^2-1}}\,
\mathfrak M_{HK}(\kappa,u,\epsilon_s).
$$

The adjoint-balance window is the interval of heat times \(t_p\) satisfying
$$
\left|
1-(N^2-1)e^{-t_p\lambda_{HK}N}
\right|
<
\Delta_{HK}.
$$

When \(0<\Delta_{HK}<1\), this is equivalently
$$
{\log(N^2-1)-\log(1+\Delta_{HK})
\over
\lambda_{HK}N}
<
t_p
<
{\log(N^2-1)-\log(1-\Delta_{HK})
\over
\lambda_{HK}N}.
$$

Proof.

The inequality
$$
|1-(N^2-1)e^{-t_p\lambda_{HK}N}|<\Delta_{HK}
$$
is equivalent to
$$
1-\Delta_{HK}
<
(N^2-1)e^{-t_p\lambda_{HK}N}
<
1+\Delta_{HK}.
$$
If \(0<\Delta_{HK}<1\), divide by \(N^2-1\), take logarithms, and reverse
signs after multiplying by \(-1\). `square`

### Corollary 108.4: The Window Is Narrow At Large \(N\)

For \(0<\Delta_{HK}<1\), the center of the adjoint-balance window is
$$
t_{bal}(N)
:=
{\log(N^2-1)\over\lambda_{HK}N},
$$
and its width is
$$
{1\over\lambda_{HK}N}
\log{1+\Delta_{HK}\over1-\Delta_{HK}}
=
{2\Delta_{HK}+O(\Delta_{HK}^3)\over\lambda_{HK}N}.
$$

Thus, unless the cofinal selector places \(t_p\) in an
\(O(\mathfrak M_{HK}/N)\) window around \(t_{bal}(N)\), the universal
optimistic heat debit cannot be absorbed.

### Corollary 108.5: Fixed Non-Balanced Heat Times Do Not Absorb The Debit

If along a cofinal subsequence
$$
\left|
1-(N^2-1)e^{-t_p\lambda_{HK}N}
\right|
\ge c_0>0,
$$
then the optimistic heat-reference debit is bounded below by
$$
c_0\,{\sqrt{N^2-1}\over N}.
$$
Consequently it cannot fit inside any signed-tail budget whose available
margin is eventually below that lower bound.

Proof.

This is Lemma 108.2 with the inequality reversed.  Since
\(\sqrt{N^2-1}/N\to1\), any fixed nonzero imbalance gives an order-one heat
debit. `square`

## 109. Current-Corpus Verdict For Margin Absorption

The margin test is exact, but the current corpus does not prove it in a
closing range.

### Proposition 109.1: Papers 20--30 Do Not Prove The Adjoint-Balance Window

Papers 20--30 do not prove that the declared cofinal selector places every
live optimistic heat-reference block in the adjoint-balance window of
Definition 108.3.

Proof.

The earlier TREE-TIME and heat-kernel audits choose cofinal rows to meet
separate scalar loss, activity, and carrier constraints.  They do not impose
the new equation
$$
t_p
\approx
{\log(N^2-1)\over\lambda_{HK}N}
$$
to within the narrow width from Corollary 108.4.  No paper proves that this
adjoint-balance condition is compatible with all previously closed finite
tables, the `SEL2` pushed-forward law, and the signed-tail margin. `square`

### Proposition 109.2: Margin Absorption Is Not Falsified Either

The current corpus also does not prove that the adjoint-balance window is
impossible.

Proof.

No printed theorem forbids choosing or extracting a cofinal subsequence with
heat times near \(t_{bal}(N)\).  The obstruction is not a contradiction; it
is an unsourced compatibility theorem.  One would need to check the balanced
heat-time selector against the previous scalar law, TREE-TIME gate,
finite-table closures, and the residual-score/floor accounts. `square`

### Definition 109.3: Balanced Heat-Time Compatibility Source

`P30-HK-BALANCE-COMPAT(Delta)` asserts that there is a cofinal selector
preserving the same adaptive `SEL2` scalar law and all previously closed
finite-table results, such that every live optimistic minimal block satisfies
$$
\left|
1-(N^2-1)e^{-t_p\lambda_{HK}N}
\right|
\le\Delta_N,
$$
with
$$
\Delta_N
{\sqrt{N^2-1}\over N}
+\epsilon_s+u
<
M_{\mathrm{sgn}}(\kappa)
$$
cofinally.

### Theorem 109.4: Balanced Heat-Time Compatibility Would Absorb The Heat
Debit

If `P30-HK-BALANCE-COMPAT(Delta)` holds and the score-orthogonality debit is
\(\epsilon_s\), then the optimistic heat-reference debit can be absorbed
inside the signed-tail margin.

Proof.

The displayed inequality in Definition 109.3 is exactly Lemma 108.2 plus the
score and unblocked-sector debits. `square`

### Corollary 109.5: New Live Subgate After The Margin Test

The heat-reference margin route is now reduced to
$$
\boxed{
\mathrm{P30\text{-}HK\text{-}BALANCE\text{-}COMPAT}(\Delta).
}
$$

Without this compatibility source, or a stronger nonlocal heat-reference
cancellation, universal local heat-reference neutrality remains open and
cannot be counted as closed.

## 110. Updated Paper-30 Endpoint After The Margin Test

The heat-reference branch has now been attacked in three ways:

1. exact local \(U_N\)-neutrality fails unless \(h_0=h_A\);
2. phase symmetry does not kill the diagonal trace defects;
3. margin absorption requires the adjoint-balance window
   $$
   t_p
   =
   {\log(N^2-1)\over\lambda_{HK}N}
   +O\!\left({\mathfrak M_{HK}\over N}\right).
   $$

The positive heat-reference route is therefore:
$$
\boxed{
\mathrm{P30\text{-}HK\text{-}BALANCE\text{-}COMPAT}(\Delta)
\quad\text{or}\quad
\text{a nonlocal parent-graph cancellation}
\quad\text{or}\quad
\text{a printed }M_{\Gamma_1}^{HK}\text{ table below margin.}
}
$$

The negative route is still:
$$
\boxed{
\text{a sign-coherent heat-reference or Stein-score floor witness.}
}
$$

What is closed:

1. the exact heat-debit inequality;
2. the adjoint-balance window;
3. the large-\(N\) narrow-window asymptotic;
4. the current-corpus verdict: compatibility is neither proved nor
   forbidden.

What remains open at this pre-attack endpoint:

1. balanced heat-time compatibility with the earlier `SEL2` scalar law;
2. a nonlocal heat-reference cancellation;
3. a printed heat-reference table;
4. or a floor witness.

## 111. Direct Attack On `P30-HK-BALANCE-COMPAT`

The balance obstruction has two different meanings, depending on whether the
target gauge group rank is fixed or the active Branch-A row is the large-rank
cofinal family already used by Papers 22--23.  We separate them explicitly.
This matters: a fixed-rank AF row drives the microscopic heat time to zero,
whereas the balance window is centered at a positive fixed heat time.  A
large-rank diagonal row can instead let the balance center tend to zero with
the AF heat time.

### Proposition 111.1: Fixed-Rank Balance Fails On The AF Tail

Fix \(N\ge2\).  On the standard AF heat-kernel tail,
$$
t_{i(j)}\to0,
$$
and therefore
$$
(N^2-1)e^{-t_{i(j)}\lambda_{HK}N}\to N^2-1.
$$
Consequently
$$
\left|
1-(N^2-1)e^{-t_{i(j)}\lambda_{HK}N}
\right|
\to N^2-2.
$$
In particular, for any fixed-rank branch and any balance tolerance
\(\Delta_N<N^2-2\), `P30-HK-BALANCE-COMPAT(Delta)` fails cofinally.

Proof.

The Paper-16/Paper-20 AF heat-kernel scheme has \(t_i\sim g_i^2\to0\).
The displayed limit follows by continuity of the exponential.  Since
\(N^2-2>0\), the adjoint-balance inequality cannot hold for any smaller
tolerance after passing to a tail. `square`

### Definition 111.2: Large-Rank Balance Function

For \(x>1\), define the balance time
$$
f_{\lambda}(x)
:=
{\log(x^2-1)\over\lambda_{HK}x}.
$$
Thus
$$
t_{bal}(N)=f_{\lambda}(N).
$$
For large \(x\),
$$
f_{\lambda}(x)
=
{2\log x+O(x^{-2})\over\lambda_{HK}x}
\to0.
$$

### Lemma 111.3: Integer-Rank Balance Tracking

There are constants \(N_0\) and \(C_{bal}\) such that for every
\(0<t<f_{\lambda}(N_0)\) one can choose an integer
\(N(t)\ge N_0\) with
$$
f_{\lambda}(N(t)+1)<t\le f_{\lambda}(N(t))
$$
and
$$
\left|
1-(N(t)^2-1)e^{-t\lambda_{HK}N(t)}
\right|
\le
C_{bal}{\log N(t)\over N(t)}.
$$

Proof.

For large \(x\),
$$
f_{\lambda}'(x)
=
{1\over\lambda_{HK}x^2}
\left(
{2x^2\over x^2-1}
-\log(x^2-1)
\right)
<0,
$$
so \(f_{\lambda}\) is eventually strictly decreasing to zero.  Given small
\(t\), choose the unique integer \(N=N(t)\) with
\(f_{\lambda}(N+1)<t\le f_{\lambda}(N)\).  By the mean-value theorem and the
large-\(x\) derivative estimate,
$$
0\le f_{\lambda}(N)-t
<
f_{\lambda}(N)-f_{\lambda}(N+1)
\le
C{\log N\over N^2}.
$$
Set
$$
\theta_N
:=
\lambda_{HK}N\bigl(f_{\lambda}(N)-t\bigr).
$$
Then
$$
0\le\theta_N\le C'{\log N\over N}.
$$
Since
$$
(N^2-1)e^{-t\lambda_{HK}N}
=
\exp\!\left(\lambda_{HK}N(f_{\lambda}(N)-t)\right)
=e^{\theta_N},
$$
we get
$$
\left|
1-(N^2-1)e^{-t\lambda_{HK}N}
\right|
=e^{\theta_N}-1
\le
C_{bal}{\log N\over N}
$$
after increasing \(C_{bal}\) and passing to \(N\ge N_0\). `square`

## 112. The Rank-Diagonal Balance Selector

The preceding lemma gives a genuine way to source balance, but only for the
large-rank cofinal family.  It is not a proof for fixed \(SU(N_0)\).

### Definition 112.1: `P30-HK-BALANCE-DIAG`

`P30-HK-BALANCE-DIAG` is the following structural selector.

Start with the same Paper-16/Paper-20 AF heat-kernel trajectory
\((g_i,t_i)\), \(t_i\to0\).  For each sufficiently large \(i\), choose the
integer rank
$$
N_i:=N(t_i)
$$
from Lemma 111.3.  Then use the same `SEL2` square selector
$$
H_i=g_i^{-2},
\qquad
L_i=\lfloor\sqrt{sH_i}\rfloor,
\qquad
S_i=L_i^2,
$$
with the same fixed \(s,\epsilon_A,\chi\) tail-slack convention as Paper 22.

This is a diagonal row in the already declared large-\(N\) Branch-A family:
the finite parent law at row \(i\) is the actual \(SU(N_i)\) finite DLR law,
and the scalar law is its deterministic adaptive `SEL2` pushforward.

### Lemma 112.2: The Diagonal Selector Preserves The Block-Time Ledger

On `P30-HK-BALANCE-DIAG`,
$$
T_i^{SEL2,conv}=S_i t_i+o(1)=s+o(1)
$$
after the same slack tightening used in Paper 22.  In particular, for every
fixed \(0<\epsilon_A,\chi<1\),
$$
s(1-\epsilon_A)(1-\chi)
\le
\liminf_i T_i^{SEL2,conv}
\le
\limsup_i T_i^{SEL2,conv}
\le
s(1+\epsilon_A)(1+\chi).
$$

Proof.

This is exactly Paper 20 Theorem 4.3A.160BB and Paper 22 Lemmas 19.2--19.4
read on the diagonal subsequence.  The rank \(N_i\) is not used in the
identity
$$
T_i^{SEL2,conv}=S_i t_i+o(1),
$$
which follows from the sheet-time audit, \(S_i/H_i\to s\), and
\(t_i/g_i^2\to1\).  Passing to a diagonal cofinal subsequence preserves the
finite row tables by Paper 22 Lemma 19.4. `square`

### Lemma 112.3: The Diagonal Selector Preserves `TREE-TIME`

Assume the Paper-22 activity gate
$$
\widehat\eta_{*,20}\le\eta_{\log2}.
$$
Then for any fixed \(s>0\) and fixed slack tail
\(\epsilon_A,\chi<1\), `P20-SEL2-TREE-TIME(F_{N_i})` holds cofinally on
`P30-HK-BALANCE-DIAG`.

Proof.

For the fundamental channel,
$$
C_2(F_N)={N^2-1\over2N}.
$$
The Paper-20/Paper-22 tree-time threshold is
$$
\Theta_T^{tree}(F_N)
=
{2\over C_2(F_N)}
\left(
1+\log19+{20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right)
=O(N^{-1})
$$
under the displayed activity ceiling.  Since \(N_i\to\infty\), while
Lemma 112.2 gives a positive lower endpoint
\(s(1-\epsilon_A)(1-\chi)\), the strict tree-time inequality holds
cofinally. `square`

### Lemma 112.4: The Diagonal Selector Sources The Balance Inequality

On `P30-HK-BALANCE-DIAG`,
$$
\left|
1-(N_i^2-1)e^{-t_i\lambda_{HK}N_i}
\right|
\le
C_{bal}{\log N_i\over N_i}
$$
cofinally.

Proof.

This is Lemma 111.3 with \(t=t_i\). `square`

## 113. Closing The Balance Compatibility Subgate On The Large-Rank Branch

### Theorem 113.1: Large-Rank Diagonal Balance Compatibility

Assume:

1. adaptive Branch A is being evaluated on the large-rank fundamental-channel
   family \(F_N\), not on a fixed \(SU(N_0)\) theory;
2. the previous finite-table closures are the uniform symbolic closures of
   Papers 21--23, hence are preserved by cofinal diagonal subsequences;
3. the signed residual budget after the score and unblocked-sector debits is
   strictly positive:
   $$
   \mathfrak m
   :=
   M_{\mathrm{sgn}}(\kappa)-u-\epsilon_s
   >0.
   $$

Then `P30-HK-BALANCE-DIAG` proves
$$
\mathrm{P30\text{-}HK\text{-}BALANCE\text{-}COMPAT}(\Delta)
$$
with
$$
\Delta_{N_i}
=
C_{bal}{\log N_i\over N_i}.
$$
Consequently the optimistic heat-reference debit is absorbed cofinally:
$$
\Delta_{N_i}{\sqrt{N_i^2-1}\over N_i}
+\epsilon_s+u
<
M_{\mathrm{sgn}}(\kappa).
$$

Proof.

Lemma 112.4 gives the balance tolerance.  Since
\(\Delta_{N_i}\to0\) and \(\sqrt{N_i^2-1}/N_i\to1\), the heat-reference debit
term tends to zero.  The strict positive residual budget \(\mathfrak m>0\)
therefore absorbs it after passing to a cofinal tail.

The law has not been replaced by a comparison process: each row is still the
finite \(SU(N_i)\) parent DLR law and its deterministic adaptive `SEL2`
pushforward.  The only change is the diagonal scheduling of the already
allowed large-rank family.  Exact finite identities, zero rows, admissibility
tags, finite row maps, and limsup upper bounds survive by cofinal
restriction, as in Paper 22 Lemma 19.4. `square`

### Corollary 113.2: What This Does And Does Not Prove

The balance obstruction is now settled in the following precise sense.

1. On fixed \(SU(N_0)\), the AF microscopic heat time forces balance failure
   by Proposition 111.1.
2. On the large-rank Branch-A diagonal family, balance is compatible and the
   optimistic heat-reference debit is \(O(\log N/N)\).
3. This does not close adaptive Branch A by itself.  It spends only the local
   heat-reference debit.  The remaining same-law quantitative input is still
   the score-orthogonality or residual signed-value theorem needed to make
   $$
   M_{\mathrm{sgn}}(\kappa)-u-\epsilon_s>0
   $$
   on the actual adaptive pushed-forward law.
4. The result is Barandes-aligned: it uses no hidden Markov bridge process,
   no auxiliary heat-kernel scalar law, and no continuum Yang-Mills measure.
   It is a deterministic cofinal scheduling of finite actual laws.

Therefore the next live positive theorem is no longer the balance
compatibility source.  It is the same-law residual score/signed-value source
that supplies a positive residual budget \(\mathfrak m\), or else a lower
floor witness showing that no such budget exists.

## 114. Residual Budget Ledger

We now attack the new live obstruction directly.  The large-rank balance
selector makes the heat-reference debit cofinally negligible, so the remaining
question is whether the non-heat debits fit inside the Paper-23 signed gate.

### Definition 114.1: Residual Signed Budget

For a declared minimal-edge Peter-Weyl tail debit \(\kappa\), unblocked-sector
debit \(u\), and score-orthogonality debit \(\epsilon_s\), define
$$
\mathfrak B_{\mathrm{res}}(\kappa,u,\epsilon_s)
:=
M_{\mathrm{sgn}}(\kappa)-u-\epsilon_s,
$$
where
$$
M_{\mathrm{sgn}}(\kappa)
=
2\,\operatorname{arsinh}(B_*^{edge}-\kappa),
\qquad
0\le\kappa<B_*^{edge}.
$$

If a separate one-line width debit \(\omega\) is retained rather than absorbed
into the block-switching norm, replace this by the stricter budget
$$
\mathfrak B_{\mathrm{res}}(\kappa,u,\epsilon_s,\omega)
:=
M_{\mathrm{sgn}}(\kappa)-{\omega^2\over4}-u-\epsilon_s.
$$
The minimal block-switching ledger below uses the \(\omega=0\) form.  Any
future route that reintroduces line width must spend the \(\omega^2/4\) term.

### Lemma 114.2: Budget Positivity Is The Exact Remaining Positive
Condition After Balance

Assume the large-rank diagonal balance selector of Theorem 113.1.  Suppose
the same cofinal adaptive law supplies:
$$
\mathrm{P23\text{-}RPF\text{-}MIN\text{-}KTAIL}(\kappa),
$$
the unblocked-sector bound \(u\), and
$$
\mathrm{P30\text{-}DEFECT\text{-}SCORE\text{-}ORTHO}(\epsilon_s).
$$
If
$$
\mathfrak B_{\mathrm{res}}(\kappa,u,\epsilon_s)>0,
$$
then the optimistic heat-reference branch passes the signed-tail margin.

Proof.

Theorem 113.1 makes the heat-reference debit
\(\Delta_{N_i}\sqrt{N_i^2-1}/N_i=O(\log N_i/N_i)\), hence it is eventually
smaller than any fixed positive residual budget.  The remaining debits are
exactly \(u\) and \(\epsilon_s\), while \(\kappa\) has already been spent in
\(M_{\mathrm{sgn}}(\kappa)\) by Paper 23 Definition 52.1.  Therefore the
Paper-23 signed gate is strict after passing to a cofinal tail. `square`

### Table 114.3: Residual Budget Ledger

| debit | same-law meaning | current Paper-30 status | needed theorem |
|---|---|---|---|
| \(\kappa\) | minimal-edge Peter-Weyl tail of the normalized RPF Hamiltonian | not sourced by finite labels or heat-kernel reference alone | `P23-RPF-MIN-KTAIL(kappa)` in a useful range, or a full-object no-tail theorem |
| \(u\) | normalized absolute mass of the high-charge sector not paired into admissible switching blocks | named but not bounded in a closing range | complete block cover \(u=0\), or same-law unblocked-mass bound |
| \(\epsilon_s\) | Stein residual-score pairing debit \(\Xi_{score}\) | defined exactly, not evaluated | score orthogonality, finite Stein low-mode table plus tail, or a sign-coherent floor witness |

The table is deliberately short.  Every remaining positive proof must lower
one of these three entries or prove that the total is already below
\(M_{\mathrm{sgn}}(\kappa)\).  More canonical labels do not help unless they
change one of the three numerical debits.

## 115. Tail Debit \(\kappa\)

### Definition 115.1: Imported Minimal Ktail Object

Paper 23 Section 55 defines
$$
\kappa_{PW}^{N,j}(L)
:=
\left\|
(I-\Pi_{\le L}^{xy})C_0^{m,N,j}
\right\|_{\mathrm{edge}},
$$
where \(C_0^{m,N,j}\) is the normalized minimal-edge Hamiltonian after
`BC/CE`, anchoring, and the adaptive `SEL2` pushforward.  The source
`P23-RPF-MIN-KTAIL(kappa)` asserts that for a declared cofinal cutoff schedule
\(L=L(N,j)\),
$$
\limsup_{(N,j)}\kappa_{PW}^{N,j}(L(N,j))\le\kappa.
$$

### Proposition 115.2: Current Corpus Does Not Source A Useful \(\kappa\)

Papers 20--30 do not prove `P23-RPF-MIN-KTAIL(kappa)` for any useful
\(\kappa\) in the residual budget.

Proof.

Paper 23 Proposition 55.4 proves that finite scalar records do not imply
finite Peter-Weyl band support after conditioning, central-entry division,
normalization, anchoring, and logarithms.  Paper 23 Table 55.7 records that
heat-kernel/Casimir smoothing is available for declared heat-kernel rows, not
for the actual adaptive residual Hamiltonian \(C_0^{m,N,j}\).  Paper 28
Proposition 3.4 repeats the same verdict for the RN-MIXAMP tail, and Paper 29
uses it in the low-mode value-extraction closure.  Paper 30 has not added a
new tail theorem for \(C_0^{m,N,j}\); it has only moved the heat-reference
debit. `square`

### Corollary 115.3: The Only Positive \(\kappa\) Routes

The tail debit can be closed only by one of:

1. `P23-RPF-MIN-PWBAND(L0)`, exact finite Peter-Weyl support;
2. `P23-RPF-MIN-PWDECAY(A,t)`, uniform same-law Peter-Weyl decay;
3. a printed cofinal numerical table for
   \(\kappa_{PW}^{N,j}(L(N,j))\);
4. a full-object signed theorem that avoids truncation and therefore pays no
   \(\kappa\).

The first three are tail theorems.  The fourth changes the route but remains
inside Branch A if it is proved on the same actual pushed-forward law.

## 116. Unblocked-Sector Debit \(u\)

### Definition 116.1: Unblocked-Mass Source

Let \({\mathcal Q}_{unblk}^{N,j}\) be the part of the signed high-charge
bridge tail not assigned to an admissible \(U_N\)-switching block in the
finite block partition of Definition 74.4.  Define
$$
u_{unblk}^{N,j}
:=
{1\over Z_B^{N,j}(\eta)}
\left\|
\sum_{Q\in{\mathcal Q}_{unblk}^{N,j}} W_Q^{N,j}
\right\|_{\mathrm{abs}},
$$
where \(W_Q^{N,j}\) denotes the actual same-law signed contribution and the
absolute norm is the same normalized absolute mass used in Definition 74.4.

`P30-UNBLOCKED-SMALL(u)` asserts
$$
\limsup_{(N,j)}u_{unblk}^{N,j}\le u.
$$

The exact-cover case is
$$
\mathrm{P30\text{-}UNBLOCKED\text{-}COVER}
\quad\Longrightarrow\quad
\mathrm{P30\text{-}UNBLOCKED\text{-}SMALL}(0).
$$

### Proposition 116.2: Current Corpus Does Not Bound \(u\)

Papers 20--30 do not prove `P30-UNBLOCKED-SMALL(u)` in a closing range.

Proof.

Section 74 introduces \(u\) as the normalized absolute mass of the part not
covered by the switching blocks.  Section 75 explicitly lists a bound on the
unblocked sector as one of the missing ingredients for
`P30-BLOCK-SWITCH(theta,u)`.  Later sections reduce the block-even part to
two defect combinations and then to heat-reference plus score terms, but they
do not print either a complete block cover or an absolute mass estimate for
the complement.  Therefore \(u\) is not a solved finite-label term; it remains
a same-law coverage/value source. `square`

### Corollary 116.3: Productive \(u\)-Attack

The next useful \(u\)-work is finite but sharp:

1. print the literal switching-block cover and prove
   `P30-UNBLOCKED-COVER`, giving \(u=0\); or
2. prove an actual-law absolute mass bound `P30-UNBLOCKED-SMALL(u)` small
   enough to fit the residual budget; or
3. if neither is true, extract the unblocked sector as part of a floor
   witness.

This is a finite partition problem only in the exact-cover case.  If a
nonempty complement remains, its mass is actual-law quantitative information.

## 117. Score-Orthogonality Debit \(\epsilon_s\)

### Definition 117.1: Exact Score Debit

Paper 30 Definition 98.2 defines
$$
\Xi_{score}^{N,j}
:=
\sum_{\Gamma_1\text{ blocks}}
{1\over2}
\left(
\left|O_1^{\Gamma_1}+O_2^{\Gamma_1}\right|
+
\left|O_1^{\Gamma_1}-O_2^{\Gamma_1}\right|
\right),
$$
where
$$
O_i^{\Gamma_1}
=
E_{K_B^{par}}
\left[
\sum_{\ell,a}
X_{\ell,a}U_i^{\Gamma_1}\,
S_{\ell,a}^{RPF}
\right].
$$
The source `P30-DEFECT-SCORE-ORTHO(epsilon_s)` is exactly
$$
\limsup_{(N,j)}\Xi_{score}^{N,j}\le\epsilon_s.
$$

### Definition 117.2: Low-Mode Plus Tail Score Source

For a Peter-Weyl cutoff \(L\), define the low-mode debit
$$
\Xi_{score,\le L}^{N,j}
:=
\sum_{\Gamma_1\text{ blocks}}
{1\over2}
\left(
\left|O_1^{\Gamma_1,\le L}+O_2^{\Gamma_1,\le L}\right|
+
\left|O_1^{\Gamma_1,\le L}-O_2^{\Gamma_1,\le L}\right|
\right),
$$
using Definition 101.1, and define the complementary tail
\(\Xi_{score,>L}^{N,j}\) analogously.

`P30-STEIN-LOWTAB(L,epsilon_L)` asserts
$$
\limsup_{(N,j)}\Xi_{score,\le L}^{N,j}\le\epsilon_L.
$$
`P30-STEIN-SCORE-KTAIL(L,r_L)` asserts
$$
\limsup_{(N,j)}\Xi_{score,>L}^{N,j}\le r_L.
$$

### Lemma 117.3: Low-Mode Plus Tail Gives Score Orthogonality

If `P30-STEIN-LOWTAB(L,epsilon_L)` and
`P30-STEIN-SCORE-KTAIL(L,r_L)` hold, then
$$
\mathrm{P30\text{-}DEFECT\text{-}SCORE\text{-}ORTHO}(\epsilon_L+r_L)
$$
holds.

Proof.

This is Definition 101.1 and Lemma 101.3 with the low-mode and tail parts
named separately.  Apply the triangle inequality to the two combinations
\(O_1+O_2\) and \(O_1-O_2\), then sum over blocks and take the cofinal
limsup. `square`

### Proposition 117.4: Current Corpus Does Not Source \(\epsilon_s\)

Papers 20--30 do not prove `P30-DEFECT-SCORE-ORTHO(epsilon_s)` for a
budget-closing \(\epsilon_s\).

Proof.

Paper 30 Proposition 99.3 already proves that the current corpus does not
print score orthogonality in a closing range.  Proposition 101.4 proves that
the Stein-Peter-Weyl low-mode-plus-tail source is also unsourced: the
low-mode score table is not printed, and the actual residual-score tail is
not bounded.  Papers 28--29 provide the parallel negative verdict for
RN-MIXAMP low-mode values and tails.  Therefore \(\epsilon_s\) is the main
same-law value theorem still needed after the balance compatibility split.
`square`

## 118. Residual Budget Status After The Direct Attack

### Theorem 118.1: Exact Conditional Positive Closure

On the large-rank diagonal Branch-A selector, the following package closes
the Paper-30 optimistic signed/heat-reference route:
$$
\boxed{
\begin{gathered}
\mathrm{P23\text{-}RPF\text{-}MIN\text{-}KTAIL}(\kappa),\\
\mathrm{P30\text{-}UNBLOCKED\text{-}SMALL}(u),\\
\mathrm{P30\text{-}DEFECT\text{-}SCORE\text{-}ORTHO}(\epsilon_s),\\
M_{\mathrm{sgn}}(\kappa)-u-\epsilon_s>0.
\end{gathered}
}
$$

If the proof uses Peter-Weyl truncation for the score term, it is enough to
replace the third line by
$$
\mathrm{P30\text{-}STEIN\text{-}LOWTAB}(L,\epsilon_L)
+
\mathrm{P30\text{-}STEIN\text{-}SCORE\text{-}KTAIL}(L,r_L)
$$
and require
$$
M_{\mathrm{sgn}}(\kappa)-u-\epsilon_L-r_L>0.
$$

Proof.

Theorem 113.1 spends the heat-reference debit on the diagonal balance
selector.  Lemma 114.2 then reduces the remaining margin to the residual
budget.  Lemma 117.3 supplies the optional low-mode-plus-tail replacement for
the score term. `square`

### Theorem 118.2: Current-Corpus Verdict

The current corpus does not prove the residual budget positivity
$$
M_{\mathrm{sgn}}(\kappa)-u-\epsilon_s>0.
$$

Proof.

Proposition 115.2 says that a useful \(\kappa\) is not sourced.  Proposition
116.2 says that \(u\) is not bounded or removed.  Proposition 117.4 says that
\(\epsilon_s\) is not sourced.  Any one of these gaps can block the displayed
strict inequality; all three are presently open. `square`

### Corollary 118.3: Next Positive And Negative Targets

After the balance split, Paper 30 has narrowed the obstruction to three
primitive same-law value tasks:

1. close \(\kappa\) by finite-band support, Peter-Weyl decay, a printed
   cofinal tail table, or a full-object no-tail theorem;
2. close \(u\) by a complete switching-block cover or a same-law unblocked
   mass bound;
3. close \(\epsilon_s\) by a Stein low-mode table plus tail, exact score
   orthogonality, or direct residual-score cancellation.

The negative/floor route is equally sharp:
$$
\boxed{
\text{if the same objects force }
\overline\Lambda_{13}^{RPF}\ge M_*,
\text{ adaptive Branch A is falsified.}
}
$$

This is the new endpoint.  The obstruction is no longer heat-time balance and
not finite labeling.  It is literal quantitative information about the
actual adaptive pushed-forward residual law.

## 119. Direct Attack On The Unblocked-Sector Debit

The debit \(u\) is the only entry in the residual budget that might still be
removed by a finite cover theorem.  This section makes that possibility exact
and separates it from the genuinely quantitative alternatives.

### Definition 119.1: Blockable High-Charge Bridge Row

Let \(Q\) be a high-charge signed bridge history or true-bridge atom in the
Paper-30 tail ledger.  Say that \(Q\) is \(U_N\)-blockable if all of the
following finite same-law conditions hold.

1. **Minimal corridor localization.**  \(Q\) contains a declared minimal
   corridor cell \(\Gamma_1\) in the sense of Definition 73.1.
2. **Two-channel switch space.**  The local endpoint transport through
   \(\Gamma_1\) lands in the singlet/adjoint \(F\otimes F^*\) block, or in a
   declared finite block whose recoupling matrix has been printed and plays
   the same role as \(U_N\).
3. **Defined recoupling.**  The corridor switch has nonzero denominator and
   preserves the internal Haar/intertwiner constraints.
4. **No double charge.**  The row has not already been paid by endpoint-blind,
   endpoint-additive, local, CE/retraction, retained finite, or Peter-Weyl
   tail ledgers.
5. **Unique assignment.**  A deterministic priority rule assigns \(Q\) to one
   and only one block \(\Gamma_1(Q)\).

Let
$$
{\mathcal Q}_{blk}^{N,j}
:=
\{Q:Q\text{ is }U_N\text{-blockable}\},
\qquad
{\mathcal Q}_{unblk}^{N,j}
:=
{\mathcal Q}_{tail}^{N,j}\setminus{\mathcal Q}_{blk}^{N,j}.
$$

### Lemma 119.2: Exact Cover Is Exactly \(u=0\)

If
$$
{\mathcal Q}_{unblk}^{N,j}=\varnothing
$$
cofinally, then `P30-UNBLOCKED-SMALL(0)` holds.  Conversely, an exact
finite-cover proof of \(u=0\) through the block-switching route must show
that every non-tail-paid high-charge bridge row is \(U_N\)-blockable, up to
zero actual signed mass.

Proof.

The unblocked debit \(u\) is by Definition 116.1 the normalized absolute mass
of the complement of the block partition.  If the complement is empty, that
mass is zero.  Conversely, a block-switching proof cannot make an uncovered
row disappear by notation: an uncovered row is either assigned to another
already licensed ledger, has zero actual signed mass, or contributes to the
unblocked absolute mass. `square`

### Proposition 119.3: The Current Corpus Does Not Prove Exact Cover

Papers 20--30 do not prove `P30-UNBLOCKED-COVER`.

Proof.

Paper 23 Lemma 49.3 proves that true bridges are exactly active mixed rows:
they are rows with nonzero mixed endpoint variation.  That definition does
not assert the existence of a minimal corridor cell, a two-channel
singlet/adjoint switch, a nonzero recoupling denominator, or a unique
switching assignment.  Paper 30 Proposition 71.7 explicitly leaves the
unpaired sector and switch-area source open, and Section 75 lists a bound on
the unblocked sector as a missing ingredient for `P30-BLOCK-SWITCH`.

Thus the current corpus proves finite true-bridge classification, not
complete \(U_N\)-blockability of every high-charge row.  Exact cover remains
a new finite corridor-completeness theorem. `square`

## 120. Classification Of The Unblocked Complement

The complement of the blockable sector is not a single mystery.  It splits
into finite flags.  This lets us decide what kind of theorem could remove
each part.

### Definition 120.1: Unblocked Flags

For a row \(Q\in{\mathcal Q}_{unblk}^{N,j}\), assign the first applicable
flag in the following priority order.

| flag | condition | possible payment |
|---|---|---|
| `TAIL` | \(Q\) lies outside the retained Peter-Weyl cutoff | \(\kappa\) |
| `NOCELL` | no declared minimal corridor cell \(\Gamma_1\) is printed | corridor-completeness theorem or floor |
| `NON2CH` | the local transport is not in a printed \(U_N\)-type two-channel block | enlarged recoupling block or floor |
| `DEN0` | the switch denominator/recoupling coefficient vanishes | switch-unpaired debit \(u\) or switch-area |
| `NOSIGN` | the switch is defined but does not reverse the signed insertion | switch-neutrality theorem or floor |
| `RNFAIL` | the residual/Jacobian factor is not quasi-invariant enough | `P30-SWITCH-RESID-QI` or floor |
| `DUP` | the row would double-charge a previously licensed ledger | keep in the previous ledger, not in \(u\) |
| `VALUE` | the row is blockable structurally but its actual mass is unknown | `P30-UNBLOCKED-SMALL(u)` or floor |

This priority rule is deterministic.  It is only a finite scalar-record
classification; it does not change the actual law.

### Lemma 120.2: `TAIL` And `DUP` Are Not New \(u\)-Mass

Rows flagged `TAIL` are paid by the declared \(\kappa\) tail source.  Rows
flagged `DUP` are removed from the unblocked sector and returned to the
previously licensed ledger that already charges them.

Proof.

`TAIL` rows are, by definition, outside the retained projection and hence are
not part of the retained block-switching mass.  They are charged to
`P23-RPF-MIN-KTAIL(kappa)`.  `DUP` rows violate the no-double-charge
condition in Definition 119.1, so they may not be charged again as unblocked
mass; they remain in the earlier finite ledger that licensed them. `square`

### Lemma 120.3: The Live Unblocked Classes

After removing `TAIL` and `DUP`, the genuinely live unblocked classes are
$$
\mathrm{NOCELL},\quad
\mathrm{NON2CH},\quad
\mathrm{DEN0},\quad
\mathrm{NOSIGN},\quad
\mathrm{RNFAIL},\quad
\mathrm{VALUE}.
$$
The first two are finite corridor-completeness defects.  The next three are
nonabelian switching-source defects.  The last is pure actual-law mass.

Proof.

This is the priority classification of Definition 120.1 after deleting rows
already assigned to \(\kappa\) or to a previous ledger.  Each remaining flag
names exactly one missing assertion: a printed cell, a printed block, a
defined switch, a sign reversal, residual quasi-invariance, or numerical
mass. `square`

## 121. Source Theorems That Remove \(u\)

### Definition 121.1: Corridor Completeness Source

`P30-CORRIDOR-COMPLETE` asserts that, cofinally, every retained high-charge
true-bridge row that is not already tail-paid or previously licensed has:

1. a declared minimal corridor cell;
2. a printed finite recoupling block;
3. a nonzero switch denominator;
4. a deterministic unique block assignment.

Equivalently, after removing `TAIL` and `DUP`, no row has flag `NOCELL`,
`NON2CH`, or `DEN0`.

### Definition 121.2: Signed Switching Completeness Source

`P30-SWITCH-SIGNED-COMPLETE(delta,u)` asserts that, on the rows supplied by
`P30-CORRIDOR-COMPLETE`, the switch sign and residual/Jacobian controls hold
with:
$$
\mathrm{P30\text{-}SWITCH\text{-}NEUTRAL}(\delta)
\quad\text{and}\quad
\mathrm{P30\text{-}SWITCH\text{-}RESID\text{-}QI}(\delta),
$$
outside a residual unpaired sector of normalized absolute mass at most \(u\).

### Lemma 121.3: Completeness Plus Switching Bounds \(u\)

If `P30-CORRIDOR-COMPLETE` and
`P30-SWITCH-SIGNED-COMPLETE(delta,u)` hold, then
`P30-UNBLOCKED-SMALL(u)` holds.  If the residual unpaired sector is empty,
then `P30-UNBLOCKED-SMALL(0)` holds.

Proof.

Corridor completeness removes the finite structural flags `NOCELL`,
`NON2CH`, and `DEN0`.  Signed switching completeness removes `NOSIGN` and
`RNFAIL` except for the declared unpaired sector.  The remaining normalized
absolute mass is at most \(u\), which is exactly Definition 116.1. `square`

### Lemma 121.4: Switch-Area Bound For The Residual Unpaired Sector

Assume the residual unpaired sector satisfies `P30-SWITCH-AREA(A0)` with
representation-history entropy debit \(g_{sw}\), residual insertion
coefficient debit \(\epsilon_{res}\), and denominator lower debit \(d_Z\).
Then
$$
\mathrm{P30\text{-}UNBLOCKED\text{-}SMALL}
\left(
\exp(g_{sw}+\epsilon_{res}+d_Z-A_0)
\right)
$$
holds.

Proof.

This is Theorem 71.6 applied to the residual unpaired sector after the
blockable rows have been removed by corridor completeness. `square`

## 122. \(u\)-Attack Verdict

### Theorem 122.1: Exact Conditional \(u=0\) Route

The finite cover route proves that the unblocked debit vanishes exactly when
the retained high-charge bridge tail admits a complete corridor/switch cover,
up to rows of zero actual signed mass:
$$
\boxed{
\mathrm{P30\text{-}CORRIDOR\text{-}COMPLETE}
+
\mathrm{P30\text{-}SWITCH\text{-}SIGNED\text{-}COMPLETE}(\delta,0)
\Longrightarrow
\mathrm{P30\text{-}UNBLOCKED\text{-}SMALL}(0).
}
$$

Proof.

Apply Lemma 121.3 with \(u=0\).  Conversely, within the finite cover proof
format, Lemma 119.2 says that any row not covered, not tail-paid, not
previously licensed, and not zero-mass contributes to the unblocked absolute
mass.  A proof that uncovered rows have zero actual mass would be a separate
same-law value theorem, not an exact-cover theorem. `square`

### Theorem 122.2: Exact Conditional Small-\(u\) Route

If exact cover fails but the unpaired sector satisfies the switch-area bound,
then
$$
\boxed{
\mathrm{P30\text{-}UNBLOCKED\text{-}SMALL}
\left(
\exp(g_{sw}+\epsilon_{res}+d_Z-A_0)
\right).
}
$$
This closes the \(u\)-entry of the residual budget whenever
$$
M_{\mathrm{sgn}}(\kappa)
-
\epsilon_s
-
\exp(g_{sw}+\epsilon_{res}+d_Z-A_0)
>0.
$$

Proof.

Lemma 121.4 supplies the bound on \(u\).  Substitute it into the residual
budget inequality of Definition 114.1. `square`

### Proposition 122.3: Current-Corpus Verdict For \(u\)

The current corpus does not prove `P30-UNBLOCKED-SMALL(u)` in a useful range,
but it has now reduced \(u\) to three explicit source theorems:
$$
\boxed{
\mathrm{P30\text{-}CORRIDOR\text{-}COMPLETE}
\quad+\quad
\mathrm{P30\text{-}SWITCH\text{-}SIGNED\text{-}COMPLETE}
\quad+\quad
\mathrm{P30\text{-}SWITCH\text{-}AREA}.
}
$$

Proof.

Proposition 119.3 rules out exact cover as a current-corpus consequence.
Proposition 71.7 states that residual quasi-invariance, switch-neutrality,
switch-area, and useful unpaired-mass bounds are not currently proved.
Lemmas 121.3 and 121.4 show that these are precisely the missing sources
needed to control \(u\). `square`

### Corollary 122.4: Updated Residual Budget After The \(u\)-Attack

The \(u\)-entry is no longer a vague leftover.  It is one of:

1. zero, if a complete corridor/switch cover is proved;
2. explicitly bounded by switch-area:
   $$
   u\le\exp(g_{sw}+\epsilon_{res}+d_Z-A_0);
   $$
3. a floor-witness candidate, if unblocked mass is sign-coherent and cannot
   fit in the residual budget;
4. an open actual-law mass source.

Thus the next best finite move is to attempt
`P30-CORRIDOR-COMPLETE`.  If it fails, the work should immediately attack
`P30-SWITCH-AREA` or promote the leftover sector to the floor route.

## 123. Full-Block Corridor Selector

The previous section left `P30-CORRIDOR-COMPLETE` as the next finite
question.  The important correction is that the minimal \(2\times2\)
singlet/adjoint \(U_N\) block is only the first diagnostic block.  It is not
the right structural cover for the whole high-charge tail.  The full
Peter-Weyl history expansion of Section 66 gives a broader finite block at
each corridor cell: the complete local invariant tensor space compatible
with the labels present in the actual history.

This section proves the corridor part of the cover in that full-block sense.
It does not prove signed cancellation, residual quasi-invariance, or
smallness.

### Definition 123.1: History-Level Bridge Atom

Let \(Q\) be a retained high-charge bridge contribution after the
Peter-Weyl expansion of Theorem 66.4.  Thus
$$
Q=(A,\mathfrak f)
$$
where \(A\) is a surviving true-bridge atom and \(\mathfrak f\) is a
representation history contributing to the same actual adaptive finite DLR
coefficient.  The contribution is retained only if it is not already paid by
the Peter-Weyl tail \(\kappa\) and not already licensed by an older
endpoint-blind, endpoint-additive, local, CE, RP/Cov, or finite-template
ledger.

The history-level refinement is not a new process.  It is the same
Peter-Weyl expansion of the same compact-group DLR integral used in
Theorem 66.4.

### Definition 123.2: Connected Flux Component

For a history \(Q=(A,\mathfrak f)\), let
\(\operatorname{Flux}(Q)\) be the subgraph of the finite parent region
consisting of plaquette faces, edge intertwiners, and residual insertion
legs carrying nontrivial representation charge in \(\mathfrak f\).

A component \(C\subset \operatorname{Flux}(Q)\) is endpoint-mixed if it
meets both endpoint charge sites \(x\) and \(y\), or meets the two endpoint
ports after the deterministic anchor gauge of Paper 23 Section 45.

### Lemma 123.3: True-Bridge Histories Have Endpoint-Mixed Flux

Every retained history-level contribution \(Q=(A,\mathfrak f)\) of a
true-bridge atom has an endpoint-mixed flux component.

Proof.

If no flux component meets both endpoint ports, then the internal Haar
constraints split the representation history into an \(x\)-side factor, a
\(y\)-side factor, and an outside factor.  After the deterministic anchor
gauge, the corresponding scalar contribution is endpoint-additive:
$$
G_A^{anc}(u,v;\zeta)
=
G_x(u;\zeta)+G_y(v;\zeta)+G_0(\zeta)
$$
at the level of the mixed finite difference.  Paper 23 Lemma 49.2 removes
endpoint-blind and endpoint-additive rows from the true-bridge sector, and
Paper 23 Lemma 49.3 identifies true bridges exactly with active mixed rows.
Therefore a retained true-bridge history must contain at least one flux
component connecting the two endpoint ports. `square`

### Definition 123.4: Canonical Corridor Selector

For a retained history-level bridge contribution \(Q\), choose the canonical
corridor \(\gamma(Q)\) as follows.

1. Among endpoint-mixed flux components, choose the one whose rooted
   over-refined Paper-21/Paper-23 carrier code is lexicographically first.
2. Inside that component, choose the lexicographically first simple path of
   plaquette/intertwiner incidences from the \(x\)-port to the \(y\)-port.
3. Let \(\Gamma_1(Q)\) be the first plaquette/intertwiner cell on that path
   after leaving the \(x\)-port.

This selector is deterministic, same-record, and same-law: it uses only the
literal representation-history labels and the already fixed over-refined
carrier ordering.

### Lemma 123.5: The Selector Eliminates `NOCELL`

Every retained history-level true-bridge contribution has a declared minimal
corridor cell \(\Gamma_1(Q)\).  Hence the `NOCELL` class is empty on the
history-level retained high-charge bridge sector.

Proof.

Lemma 123.3 gives an endpoint-mixed flux component.  A finite connected
component contains a finite simple path between the two endpoint ports.  The
canonical order in Definition 123.4 chooses one such path and hence its first
plaquette/intertwiner cell.  That cell is exactly the required
\(\Gamma_1(Q)\). `square`

## 124. Full Finite Recoupling Blocks

The second possible corridor failure was `NON2CH`: a local transport need not
land in the \(F\otimes F^*\) singlet/adjoint \(2\times2\) diagnostic block.
That objection is real against the minimal diagnostic block, but it is not a
structural obstruction to corridor completeness.  The right object is the
full finite invariant tensor block for the labels actually present in the
history.

### Definition 124.1: Full Corridor Block

Fix a selected cell \(\Gamma_1(Q)\).  Freeze:

1. the external plaquette labels adjacent to the cell;
2. the endpoint charge \(q\) transported through the cell;
3. the residual insertion support labels touching the cell;
4. the retained scalar record and outside boundary data.

Let
$$
\mathcal H_{\Gamma_1(Q)}^{full}
$$
be the finite-dimensional invariant tensor space spanned by all local
intertwiner/fusion channels compatible with these frozen data.

Let
$$
U_{\Gamma_1(Q)}^{full}
:
\mathcal H_{\Gamma_1(Q)}^{full}
\to
\mathcal H_{\Gamma_1(Q)}^{full}
$$
be the \(SU(N)\) recoupling \(F\)-move between the two bracketings that move
the endpoint charge through the corridor cell.

In an orthonormal intertwiner convention, \(U_{\Gamma_1(Q)}^{full}\) is a
unitary matrix of finite size.  The \(2\times2\) matrix \(U_N\) of
Lemma 77.2 is the special fundamental/dual singlet-adjoint instance of this
definition.

### Lemma 124.2: Full Blocks Eliminate `NON2CH`

Every retained history-level true-bridge contribution belongs to a printed
finite recoupling block \(\mathcal H_{\Gamma_1(Q)}^{full}\).  Hence
`NON2CH` is empty after replacing the minimal diagnostic block by the full
corridor block.

Proof.

The selected cell \(\Gamma_1(Q)\) carries finitely many representation labels
in the finite parent history \(\mathfrak f\).  The representation category of
compact \(SU(N)\) is semisimple, and all local Haar constraints are finite
invariant tensor constraints.  Therefore the space of compatible local
intertwiners is finite-dimensional.  The recoupling between two bracketings
of the same invariant tensor space is the standard unitary \(F\)-move.  This
prints the finite block symbolically and exactly, with entries given by the
ordinary \(SU(N)\) recoupling coefficients. `square`

### Lemma 124.3: Full Blocks Eliminate The Structural `DEN0` Failure

For the full block \(U_{\Gamma_1(Q)}^{full}\), there is no structural
zero-denominator obstruction.  Histories for which the local invariant
tensor space is zero-dimensional do not occur, and on a nonzero finite
invariant tensor space the recoupling matrix is unitary.

Proof.

If \(\mathcal H_{\Gamma_1(Q)}^{full}=\{0\}\), then no local invariant tensor
with the frozen labels exists, so the history \(\mathfrak f\) is not an
admissible representation history in \(\mathfrak F_B(\eta)\).  If the space
is nonzero, the two bracketings are two orthonormal bases of the same finite
Hilbert space, and the change-of-basis matrix is unitary.  Its determinant
has modulus one.  Individual matrix entries may vanish, but that is not a
denominator failure for block switching; the whole block is the object being
switched. `square`

### Definition 124.4: Full-Block Corridor Completeness

`P30-CORRIDOR-COMPLETE-full` asserts that, cofinally, every retained
history-level high-charge true-bridge contribution that is not tail-paid and
not previously licensed has:

1. the canonical corridor cell \(\Gamma_1(Q)\);
2. the full finite recoupling block
   \(\mathcal H_{\Gamma_1(Q)}^{full}\);
3. a unitary recoupling matrix \(U_{\Gamma_1(Q)}^{full}\);
4. a deterministic unique assignment to that first selected cell and block.

### Theorem 124.5: Full-Block Corridor Completeness Holds

The current corpus proves `P30-CORRIDOR-COMPLETE-full`.

Proof.

Theorem 66.4 supplies the same-law representation-history expansion.
Lemma 123.3 supplies endpoint-mixed flux for retained true-bridge histories.
Definition 123.4 supplies the deterministic first-cell selector, proving the
cell and uniqueness clauses.  Lemma 124.2 supplies the full finite
recoupling block, and Lemma 124.3 supplies the nonzero block-level
recoupling denominator.  The no-double-charge restriction is inherited from
Definition 123.1, which removes tail-paid and previously licensed rows
before the selector is applied. `square`

## 125. Corridor-Completeness Verdict

The corridor-completeness attack has a positive structural close, but only
after making explicit that the block is the full finite invariant tensor
block, not just the \(2\times2\) diagnostic table.

### Corollary 125.1: Original Corridor Gate With Full Blocks

Under the "declared finite block" clause of Definition 119.1,
`P30-CORRIDOR-COMPLETE-full` supplies `P30-CORRIDOR-COMPLETE`.
Consequently, after the full-block refinement, the live unblocked flags are
not
$$
\mathrm{NOCELL},\quad \mathrm{NON2CH},\quad \mathrm{DEN0}.
$$
They are only
$$
\mathrm{NOSIGN},\quad \mathrm{RNFAIL},\quad \mathrm{VALUE},
$$
plus any sector deliberately abandoned to `P30-SWITCH-AREA`.

Proof.

Definition 119.1 allowed either the singlet/adjoint \(U_N\) block or a
declared finite block playing the same recoupling role.  Definition 124.1
declares exactly that full finite block.  Theorem 124.5 proves the four
corridor-completeness clauses for every retained history-level bridge
contribution.  The removed flags are precisely the structural flags listed
in Lemma 120.3. `square`

### Corollary 125.2: What This Does And Does Not Buy

The residual budget now improves from
$$
\mathrm{P30\text{-}CORRIDOR\text{-}COMPLETE}
+
\mathrm{P30\text{-}SWITCH\text{-}SIGNED\text{-}COMPLETE}
$$
to the sharper statement that the first factor is closed by full finite
recoupling:
$$
\boxed{
\mathrm{P30\text{-}CORRIDOR\text{-}COMPLETE}
\quad\text{is closed in the full-block sense.}
}
$$
The remaining positive \(u=0\) route is therefore exactly
$$
\boxed{
\mathrm{P30\text{-}SWITCH\text{-}SIGNED\text{-}COMPLETE}(\delta,0).
}
$$
Equivalently, one must still prove signed reversal/neutrality and residual
quasi-invariance on the full blocks:
$$
\mathrm{P30\text{-}SWITCH\text{-}NEUTRAL}(\delta)
\quad+\quad
\mathrm{P30\text{-}SWITCH\text{-}RESID\text{-}QI}(\delta),
$$
with no residual unpaired mass, or else prove `P30-SWITCH-AREA` for the
leftover sector.

This is a real gain: \(u\) is no longer allowed to hide a missing corridor,
missing finite block, or zero denominator.  It can only hide actual signed
amplitude failure or actual-law residual failure.

### Proposition 125.3: Barandes-Alignment Check

The full-block corridor close is Barandes-aligned.

Proof.

No auxiliary stochastic process is introduced.  The histories are the
Peter-Weyl expansion of the same compact-group finite DLR conditional
already present in Theorem 66.4.  The selector uses only deterministic
finite labels inside the same record.  The recoupling matrices are
change-of-basis matrices inside finite \(SU(N)\) invariant tensor spaces;
they do not replace the law, alter the pushed-forward scalar record, or
insert a Markovian hidden dynamics. `square`

### Corollary 125.4: Updated Next Target

The next theorem is no longer `P30-CORRIDOR-COMPLETE`.  It is
$$
\boxed{
\mathrm{P30\text{-}SWITCH\text{-}SIGNED\text{-}COMPLETE}(\delta,u)
}
$$
on the full finite corridor blocks, with the two primitive same-law value
subgates
$$
\boxed{
\mathrm{P30\text{-}SWITCH\text{-}NEUTRAL}(\delta)
\quad+\quad
\mathrm{P30\text{-}SWITCH\text{-}RESID\text{-}QI}(\delta).
}
$$
If these fail with an unpaired sector, the only positive Branch-A fallback is
the switch-area estimate
$$
\boxed{
\mathrm{P30\text{-}SWITCH\text{-}AREA}(A_0)
}
$$
strong enough to make
$$
M_{\mathrm{sgn}}(\kappa)
-
\epsilon_s
-
\exp(g_{sw}+\epsilon_{res}+d_Z-A_0)
>0.
$$

## 126. Full-Block Signed Defect

With corridor completeness closed in the full-block sense, the remaining
question is no longer whether a corridor block exists.  It is whether the
actual signed contribution of that block cancels, or is small, under the
recoupling switch.

### Definition 126.1: Full-Block Weighted Signed Matrix

For a selected full corridor block \(\Gamma\), abbreviate
$$
U=U_{\Gamma}^{full},
\qquad
D=D_{\Gamma}^{HK},
\qquad
R=\mathcal R_{\Gamma},
\qquad
\Sigma=\Sigma_{\Gamma}.
$$
Here:

1. \(U\) is the finite unitary recoupling matrix of Definition 124.1;
2. \(D\) is the positive diagonal heat-kernel matrix in the chosen local
   channel basis;
3. \(R\) is the actual residual/Jacobian insertion matrix on the full block;
4. \(\Sigma\) is the actual signed bridge insertion matrix on the full block.

Define
$$
A_{\Gamma}^{full}:=DR\Sigma.
$$

All four matrices are finite same-law objects attached to the actual
Peter-Weyl expansion of the finite DLR conditional.  None is an auxiliary
transition kernel.

### Definition 126.2: Full-Block Switching Defect

Define the full-block switching defect by
$$
\mathcal E_{\Gamma}^{full}
:=
A_{\Gamma}^{full}
+
U^*A_{\Gamma}^{full}U
=
DR\Sigma+U^*DR\Sigma U.
$$
The normalized full-block signed defect is
$$
\Theta_{full}^{sw}
:=
\limsup_{(N,j)}
{1\over Z_B^{N,j}(\eta)}
\sum_{\Gamma\text{ full blocks}}
{1\over2}
\left\|
\mathcal E_{\Gamma}^{full}
\right\|_1.
$$

`P30-FULLBLOCK-SWDEF(theta)` asserts
\(\Theta_{full}^{sw}\le\theta\).

### Lemma 126.3: Exact Full-Block Oddness Criterion

For a full block \(\Gamma\),
$$
\mathcal E_{\Gamma}^{full}=0
$$
if and only if the actual weighted signed matrix is odd under the recoupling
conjugation:
$$
U^*A_{\Gamma}^{full}U=-A_{\Gamma}^{full}.
$$
Equivalently,
$$
U^*DR\Sigma U=-DR\Sigma.
$$

Proof.

This is Definition 126.2.  The defect is the sum of the matrix and its
recoupled image.  The sum vanishes exactly when the recoupled image is the
negative of the original matrix. `square`

### Lemma 126.4: Full-Block Defect Bounds The Signed Contribution

For each full block,
$$
\left|
\operatorname{Tr}(A_{\Gamma}^{full})
\right|
\le
{1\over2}
\left\|
\mathcal E_{\Gamma}^{full}
\right\|_1.
$$

Proof.

Trace is invariant under unitary conjugation, so
$$
2\operatorname{Tr}(A_{\Gamma}^{full})
=
\operatorname{Tr}
\left(
A_{\Gamma}^{full}+U^*A_{\Gamma}^{full}U
\right)
=
\operatorname{Tr}(\mathcal E_{\Gamma}^{full}).
$$
Use \(|\operatorname{Tr}X|\le\|X\|_1\). `square`

### Theorem 126.5: Full-Block Defect Sources Signed Switching

If `P30-FULLBLOCK-SWDEF(theta)` holds and the residual unpaired or
deliberately abandoned sector has normalized absolute mass at most \(u\),
then the full-block version of `P30-SWITCH-SIGNED-COMPLETE(theta,u)` holds.
Consequently the signed high-charge contribution is bounded by
\(\theta+u\).

Proof.

By Theorem 124.5 every retained history-level true-bridge contribution is
assigned to a unique full block unless it is intentionally placed in the
unpaired/abandoned sector.  Lemma 126.4 bounds each block's signed
contribution by half the trace norm of its defect.  Summing over blocks,
dividing by \(Z_B^{N,j}(\eta)\), and adding the unpaired mass \(u\) gives
the claim. `square`

## 127. Exact Decomposition Of The Full-Block Defect

The full-block defect separates into three logically distinct failures:
signed parity failure, heat-kernel non-invariance, and residual
quasi-invariance failure.

### Lemma 127.1: Three-Term Defect Identity

For every full block,
$$
\mathcal E_{\Gamma}^{full}
=
DR(\Sigma+U^*\Sigma U)
+
(U^*DU-D)(U^*RU)(U^*\Sigma U)
+
D(U^*RU-R)(U^*\Sigma U).
$$

Proof.

Start from
$$
\mathcal E_{\Gamma}^{full}
=
DR\Sigma+U^*DR\Sigma U.
$$
Insert \(UU^*=I\) in the second term:
$$
U^*DR\Sigma U
=
(U^*DRU)(U^*\Sigma U).
$$
Add and subtract \(DR(U^*\Sigma U)\):
$$
\mathcal E_{\Gamma}^{full}
=
DR(\Sigma+U^*\Sigma U)
+
(U^*DRU-DR)(U^*\Sigma U).
$$
Finally,
$$
U^*DRU
=
(U^*DU)(U^*RU),
$$
so
$$
U^*DRU-DR
=
(U^*DU-D)(U^*RU)+D(U^*RU-R).
$$
Substitute this into the previous display. `square`

### Definition 127.2: The Three Full-Block Debits

Define the normalized signed-parity debit \(\eta_\Sigma\), heat recoupling
debit \(\eta_{HK}\), and residual quasi-invariance debit \(\eta_R\) by the
following three cofinal bounds:
$$
\limsup_{(N,j)}
{1\over Z_B^{N,j}(\eta)}
\sum_{\Gamma}
{1\over2}
\left\|
DR(\Sigma+U^*\Sigma U)
\right\|_1
\le \eta_\Sigma,
$$
$$
\limsup_{(N,j)}
{1\over Z_B^{N,j}(\eta)}
\sum_{\Gamma}
{1\over2}
\left\|
(U^*DU-D)(U^*RU)(U^*\Sigma U)
\right\|_1
\le \eta_{HK},
$$
and
$$
\limsup_{(N,j)}
{1\over Z_B^{N,j}(\eta)}
\sum_{\Gamma}
{1\over2}
\left\|
D(U^*RU-R)(U^*\Sigma U)
\right\|_1
\le \eta_R.
$$

Name these sources:
$$
\mathrm{P30\text{-}FULL\text{-}SIGPAR}(\eta_\Sigma),
\qquad
\mathrm{P30\text{-}FULL\text{-}HKCOMM}(\eta_{HK}),
\qquad
\mathrm{P30\text{-}FULL\text{-}RPFQI}(\eta_R).
$$

### Theorem 127.3: Three Debits Source Full-Block Switching

If
$$
\mathrm{P30\text{-}FULL\text{-}SIGPAR}(\eta_\Sigma)
+
\mathrm{P30\text{-}FULL\text{-}HKCOMM}(\eta_{HK})
+
\mathrm{P30\text{-}FULL\text{-}RPFQI}(\eta_R)
$$
hold, then
$$
\mathrm{P30\text{-}FULLBLOCK\text{-}SWDEF}
(\eta_\Sigma+\eta_{HK}+\eta_R)
$$
holds.

Proof.

Apply the trace-norm triangle inequality to Lemma 127.1, then sum over
blocks and divide by \(Z_B^{N,j}(\eta)\). `square`

### Corollary 127.4: Exact Positive Budget After Corridor Closure

After full-block corridor completeness, the positive signed-switching route
closes whenever
$$
M_{\mathrm{sgn}}(\kappa)
-
\epsilon_s
-
u
-
(\eta_\Sigma+\eta_{HK}+\eta_R)
>0.
$$
If \(u=0\), the condition is
$$
M_{\mathrm{sgn}}(\kappa)
>
\epsilon_s+\eta_\Sigma+\eta_{HK}+\eta_R.
$$

Proof.

Theorem 127.3 gives the full-block defect.  Theorem 126.5 inserts it into
the signed high-charge contribution.  The remaining debits are exactly the
residual budget of Definition 114.1. `square`

## 128. Current-Corpus Audit Of The Three Debits

The decomposition is useful only if at least one of its terms is structurally
small.  The current corpus gives a partial answer.

### Proposition 128.1: Signed Parity Is Not Automatic

The current corpus does not prove
`P30-FULL-SIGPAR(eta_Sigma)` in a closing range.

Proof.

The signed insertion \(\Sigma\) is the actual bridge observable restricted
to the full local invariant tensor block.  The switch sign rule would require
the weighted block sector to satisfy
$$
\Sigma+U^*\Sigma U
\quad\text{small}
$$
after the retained-row, endpoint-additive, and licensed removals.  Paper 30
Sections 70--75 prove that termwise switching is not generically
sign-reversing, and Sections 80--85 show that even the minimal \(2\times2\)
block requires actual same-law values of the weighted signed entries.  The
full block contains the minimal block as a subcase, so finite recoupling
legality alone cannot prove the signed-parity bound. `square`

### Proposition 128.2: Heat Recoupling Commutation Is Not Automatic

The current corpus does not prove
`P30-FULL-HKCOMM(eta_HK)` in a closing range.

Proof.

The heat matrix \(D\) is diagonal in plaquette representation labels with
entries of the form
$$
d_\lambda e^{-t_pC_2(\lambda)}.
$$
The full recoupling matrix \(U\) generally mixes different fusion channels.
Unless the recoupled channels have matched heat weights, or the block is
restricted to a heat-balanced sector, \(U^*DU-D\) need not be small.

Paper 30 Sections 108--113 prove a rank-diagonal balance only for the
declared adjoint/singlet diagnostic mismatch.  That balance does not
automatically extend to every high-charge full-block channel, whose Casimir
and dimension factors vary across the full invariant tensor space.  Hence
`P30-FULL-HKCOMM` is a new full-block heat-balance theorem, not a consequence
of the current balance selector. `square`

### Proposition 128.3: Residual Quasi-Invariance Is Not Automatic

The current corpus does not prove
`P30-FULL-RPFQI(eta_R)` in a closing range.

Proof.

The debit is controlled by
$$
U^*RU-R,
$$
where \(R\) is the actual residual/Jacobian insertion matrix on the full
block.  This is exactly the full-block version of
`P30-SWITCH-RESID-QI`.  Papers 28--30 repeatedly isolate the same missing
value theorem: the actual residual coefficients and residual-score
pairings are not determined by finite labels, universal recoupling, or the
heat-kernel reference law.  Therefore no current theorem implies small
\(U^*RU-R\) on the actual adaptive pushed-forward law. `square`

### Corollary 128.4: The Three-Term Route Is Sharp But Not Closed

The exact decomposition
$$
\eta_\Sigma+\eta_{HK}+\eta_R
$$
is now the sharp full-block form of
`P30-SWITCH-SIGNED-COMPLETE`.  It is Barandes-aligned and same-law, but the
current corpus does not prove the needed numerical bounds.

This is not a failure of the corridor-completeness pass.  It means the
structural cover is closed, and the remaining obstruction is actual signed
amplitude/residual value information.

## 129. Full-Block Ward/Stein Lift

The existing Ward/Stein machinery of Sections 86--101 was written for the
minimal \(2\times2\) diagnostic block.  The same mechanism lifts to full
blocks, but the lift makes the remaining source larger rather than
automatic.

### Definition 129.1: Full-Block Defect Coordinates

For a full block \(\Gamma\), let
$$
\mathcal L_{\Gamma}(A):=A+U^*AU
$$
on the finite matrix space of the block.  Choose a finite trace-dual basis
\(\{B_{\Gamma,\alpha}\}_{\alpha\in I_\Gamma}\) for the range of
\(\mathcal L_{\Gamma}\), normalized so that the trace norm of
\(\mathcal L_{\Gamma}(A)\) is controlled by a finite constant
\(C_\Gamma^{dual}\) times the coordinate sum:
$$
\left\|\mathcal L_{\Gamma}(A)\right\|_1
\le
C_\Gamma^{dual}
\sum_{\alpha\in I_\Gamma}
\left|
\operatorname{Tr}
\left(
B_{\Gamma,\alpha}^*\mathcal L_{\Gamma}(A)
\right)
\right|.
$$

Each coordinate
$$
\Psi_{\Gamma,\alpha}
$$
is the finite DLR insertion whose expectation gives
\(\operatorname{Tr}(B_{\Gamma,\alpha}^*\mathcal L_{\Gamma}(A_{\Gamma}^{full}))\).

### Definition 129.2: Full-Block Defect-Ward Source

`P30-FULLDEF-WARD(theta)` asserts that finite Ward/Stein decompositions exist
for all coordinates \(\Psi_{\Gamma,\alpha}\), with total normalized residual
after heat-reference and licensed removals at most \(\theta\):
$$
\limsup_{(N,j)}
{1\over Z_B^{N,j}(\eta)}
\sum_{\Gamma}
{C_\Gamma^{dual}\over2}
\sum_{\alpha\in I_\Gamma}
\left|
\mathcal W_{\Gamma,\alpha}
\right|
\le \theta.
$$

Here \(\mathcal W_{\Gamma,\alpha}\) is the corresponding full-block
Ward/Stein residual: heat-reference mean, collar remainder, and residual
score pairing, exactly as in Sections 87--98.

### Theorem 129.3: Full-Block Ward Source Implies Signed Switching

`P30-FULLDEF-WARD(theta)` implies
`P30-FULLBLOCK-SWDEF(theta)`.  Consequently, with unpaired mass \(u\), it
implies the full-block version of
`P30-SWITCH-SIGNED-COMPLETE(theta,u)`.

Proof.

The coordinate insertions of Definition 129.1 reconstruct the full-block
defect norm up to the finite trace-dual constant \(C_\Gamma^{dual}\).  The
Ward/Stein residual bound of Definition 129.2 controls the normalized sum of
those coordinates.  This is exactly the norm in Definition 126.2.  Apply
Theorem 126.5 for the last statement. `square`

### Proposition 129.4: Full-Block Ward Is Not Yet Sourced

The current corpus does not prove `P30-FULLDEF-WARD(theta)` in a closing
range.

Proof.

The minimal \(2\times2\) Ward/Stein route already requires
`P30-HKREF-DEFECT-NEUTRAL` and `P30-DEFECT-SCORE-ORTHO`, neither of which is
proved in a closing range by Sections 99--101.  The full-block lift adds:

1. more defect coordinates \(\alpha\);
2. the trace-dual constants \(C_\Gamma^{dual}\);
3. possible growth of block dimension in high-charge sectors;
4. the same actual residual-score pairings, now against a larger family of
Stein potentials.

Therefore the full-block Ward lift is a valid same-law route, but it is not
closed by the existing corpus. `square`

## 130. Signed-Switching Verdict

The attack on `P30-SWITCH-SIGNED-COMPLETE` has now settled what can be
settled structurally.

### Theorem 130.1: Exact Full-Block Signed-Switching Reduction

After `P30-CORRIDOR-COMPLETE-full`, the positive Branch-A signed-switching
gate is equivalent to sourcing one of the following same-law quantitative
packages:
$$
\boxed{
\mathrm{P30\text{-}FULLBLOCK\text{-}SWDEF}(\theta)
}
$$
directly, or the sufficient three-debit package
$$
\boxed{
\mathrm{P30\text{-}FULL\text{-}SIGPAR}(\eta_\Sigma)
+
\mathrm{P30\text{-}FULL\text{-}HKCOMM}(\eta_{HK})
+
\mathrm{P30\text{-}FULL\text{-}RPFQI}(\eta_R),
}
$$
or the Ward/Stein package
$$
\boxed{
\mathrm{P30\text{-}FULLDEF\text{-}WARD}(\theta).
}
$$
Together with unpaired mass \(u\), the residual budget closes if
$$
M_{\mathrm{sgn}}(\kappa)-\epsilon_s-u-\theta>0,
$$
or, for the three-debit package,
$$
M_{\mathrm{sgn}}(\kappa)
-
\epsilon_s
-
u
-
(\eta_\Sigma+\eta_{HK}+\eta_R)
>0.
$$

Proof.

Theorem 126.5 gives the direct full-block defect route.  Theorem 127.3 gives
the three-debit sufficient package.  Theorem 129.3 gives the Ward/Stein
route.  Substitution into the residual budget gives the displayed closing
conditions. `square`

### Proposition 130.2: Current-Corpus Verdict

The current corpus does not prove `P30-SWITCH-SIGNED-COMPLETE` in a closing
range, but it has reduced it to exact full-block same-law value sources.

Proof.

Propositions 128.1--128.3 show that the three natural algebraic debits are
not sourced by existing finite labels, heat balance, or universal recoupling.
Proposition 129.4 shows that the full-block Ward/Stein route is not sourced
by the existing score-orthogonality machinery.  The reduction itself is exact
by Theorem 130.1. `square`

### Corollary 130.3: What To Attack Next

The next positive move should not be another corridor or label table.  The
best-ranked same-law targets are:

1. `P30-FULL-HKCOMM`: try to extend the rank-diagonal heat balance from the
   \(2\times2\) diagnostic block to the full recoupling blocks, or prove a
   no-go for that extension;
2. `P30-FULL-SIGPAR`: test whether the actual signed bridge insertion is
   anti-invariant under the full recoupling after the licensed removals;
3. `P30-FULL-RPFQI`: test residual/Jacobian quasi-invariance under the full
   recoupling;
4. `P30-FULLDEF-WARD`: attempt a full-block Stein orthogonality theorem;
5. if all fail, attack `P30-SWITCH-AREA(A_0)` or promote the surviving
   block defect to a sign-coherent floor witness.

The honest priority is `P30-FULL-HKCOMM`, because it is the only term that
might still be controlled by the existing balance selector rather than by a
new theorem about the actual residual law.

Proof.

The ranking follows from Theorem 130.1 and Propositions 128.1--128.3.
`P30-FULL-HKCOMM` is the only listed debit whose leading matrices are
universal heat-kernel data plus recoupling; it may be attacked by extending
the Paper-30 balance selector.  `P30-FULL-SIGPAR` and `P30-FULL-RPFQI`
depend directly on the actual signed insertion and actual residual/Jacobian
matrix.  `P30-FULLDEF-WARD` is a valid same-law lift but inherits the
unsourced score-orthogonality problem from Sections 99--101.  If none of
these positive bounds is sourced, Lemma 121.4 and Definition 84.1 give the
remaining alternatives: switch-area payment or a sign-coherent floor
witness. `square`

## 131. Attack On `P30-FULL-HKCOMM`

The next target is the heat recoupling debit
$$
\mathrm{P30\text{-}FULL\text{-}HKCOMM}(\eta_{HK}).
$$
This is the only remaining signed-switching debit that might still be
controlled by the already built rank-diagonal heat balance, because it
contains only heat-kernel weights, recoupling, and the already present
signed/residual block factor.

The first question is purely algebraic: when does a full recoupling block
commute with the heat diagonal?

### Definition 131.1: Full-Block Heat Weights

Let \(\mathcal H_\Gamma^{full}\) have an orthonormal channel basis
\(\{e_\alpha\}_{\alpha\in I_\Gamma}\) in which the heat-kernel factor is
diagonal:
$$
D_\Gamma e_\alpha
=
w_\alpha(t,N)e_\alpha.
$$
For a channel carrying plaquette irrep \(\lambda_\alpha\),
$$
w_\alpha(t,N)
=
d_{\lambda_\alpha}
\exp\{-t\,\lambda_{HK}C_2^{std}(\lambda_\alpha)\}.
$$

Define the recoupling mixing graph
$$
\mathcal G_\Gamma^U
$$
on \(I_\Gamma\) by joining \(\alpha\) to \(\beta\) whenever
\((U_\Gamma)_{\alpha\beta}\ne0\).

### Lemma 131.2: Exact Heat-Commutation Criterion

For a full block,
$$
U_\Gamma^*D_\Gamma U_\Gamma=D_\Gamma
$$
if and only if the heat weight \(w_\alpha(t,N)\) is constant on every
connected component of \(\mathcal G_\Gamma^U\).

Equivalently,
$$
(w_\alpha-w_\beta)(U_\Gamma)_{\alpha\beta}=0
$$
for every pair of channel indices \(\alpha,\beta\).

Proof.

Since \(U_\Gamma\) is unitary, \(U_\Gamma^*D_\Gamma U_\Gamma=D_\Gamma\) is
equivalent to \(D_\Gamma U_\Gamma=U_\Gamma D_\Gamma\).  In the diagonal
basis for \(D_\Gamma\), the \((\alpha,\beta)\)-entry of the commutator is
$$
(w_\alpha-w_\beta)(U_\Gamma)_{\alpha\beta}.
$$
Thus all nonzero recoupling entries can connect only equal heat weights.
This is exactly constancy on the connected components of the mixing graph.
`square`

### Definition 131.3: Pair Balance Time

For two channels \(\alpha,\beta\) with distinct standard Casimir values, set
$$
t_{\alpha\beta}(N)
:=
{\log d_{\lambda_\alpha}-\log d_{\lambda_\beta}
\over
\lambda_{HK}
\left(C_2^{std}(\lambda_\alpha)-C_2^{std}(\lambda_\beta)\right)}.
$$
This is the unique heat time at which
$$
w_\alpha(t,N)=w_\beta(t,N).
$$

If \(C_2^{std}(\lambda_\alpha)=C_2^{std}(\lambda_\beta)\), equality of heat
weights is either automatic when the dimensions also match, or impossible
for all \(t\) when the dimensions differ.

### Corollary 131.4: One Heat Time Cannot Balance An Arbitrary Full Block

A full block can be exactly heat-balanced by one scalar plaquette time \(t\)
only if all edges in every connected component of \(\mathcal G_\Gamma^U\)
have the same pair-balance time.  Equivalently, for every cycle of mixed
channels, the pair-balance equations are consistent.

Thus full-block heat commutation is a finite compatibility theorem, not a
formal consequence of unitarity of recoupling.

Proof.

By Lemma 131.2, all channels in a connected mixing component must have the
same heat weight.  Equality along each edge imposes the pair-balance equation
of Definition 131.3.  A common scalar \(t\) exists exactly when these finite
equations are consistent. `square`

## 132. The Two-Index Obstruction To Universal Full Balance

The rank-diagonal selector of Section 112 balances the singlet and adjoint
weights:
$$
1
\sim
(N^2-1)e^{-t\lambda_{HK}N}.
$$
That is enough for the \(2\times2\) diagnostic block.  It is not enough for
full blocks containing additional \(SU(N)\) channels.

### Lemma 132.1: Two-Index Channel Weights At Adjoint Balance

Let \(S_2\) denote the two-index symmetric representation of \(SU(N)\).  For
\(N\ge3\),
$$
d_{S_2}={N(N+1)\over2},
\qquad
C_2^{std}(S_2)={(N-1)(N+2)\over N}.
$$
At the adjoint-balance heat time
$$
t_A(N):={\log(N^2-1)\over \lambda_{HK}N},
$$
the symmetric two-index heat weight satisfies
$$
d_{S_2}
\exp\{-t_A(N)\lambda_{HK}C_2^{std}(S_2)\}
\longrightarrow {1\over2}.
$$

The same limit holds for the two-index antisymmetric representation
\(\Lambda_2\), with
$$
d_{\Lambda_2}={N(N-1)\over2},
\qquad
C_2^{std}(\Lambda_2)={(N+1)(N-2)\over N}.
$$

Proof.

For \(S_2\),
$$
\log w_{S_2}(t_A,N)
=
\log {N(N+1)\over2}
-
{(N-1)(N+2)\over N^2}
\log(N^2-1).
$$
Since
$$
{(N-1)(N+2)\over N^2}
=
1+{1\over N}-{2\over N^2},
$$
the right-hand side tends to \(-\log2\).  Hence
\(w_{S_2}(t_A,N)\to1/2\).

For \(\Lambda_2\), the same calculation uses
$$
{(N+1)(N-2)\over N^2}
=
1-{1\over N}-{2\over N^2}
$$
and again gives limit \(-\log2\). `square`

### Lemma 132.2: Three-Channel Balance Has A Fixed Asymptotic Gap

Consider any heat time of the form
$$
t_N={2\log N+x_N\over \lambda_{HK}N}
$$
with \(x_N\) bounded.  Then
$$
w_{\mathrm{Ad}}(t_N,N)\to e^{-x}
$$
and
$$
w_{S_2}(t_N,N)\to {1\over2}e^{-x}
$$
along any subsequence \(x_N\to x\).  Consequently
$$
\liminf_N
\inf_t
\max\{
|w_{\mathrm{Ad}}(t,N)-1|,
|w_{S_2}(t,N)-1|
\}
\ge {1\over3}.
$$

Proof.

The displayed limits follow from the same logarithmic estimates as
Lemma 132.1.  Put \(y=e^{-x}>0\).  The limiting optimization is
$$
\inf_{y>0}\max\{|y-1|,|y/2-1|\}.
$$
For \(1\le y\le2\), the two terms are \(y-1\) and \(1-y/2\), and they are
equal at \(y=4/3\), with common value \(1/3\).  Outside this interval the
maximum is larger.  If a sequence of heat times is not of the displayed
form with bounded \(x_N\), then either the adjoint weight tends to \(0\),
diverges, or has a subsequence covered by the displayed form; in the first
two cases the maximum is at least \(1\) in the limit, and in the third the
previous optimization applies. `square`

### Theorem 132.3: Universal Full-Block Heat Balance Fails

No cofinal scalar heat-time selector can make the singlet, adjoint, and
two-index symmetric channels all heat-balanced with error \(o(1)\).

In particular, the rank-diagonal adjoint-balance selector of Theorem 113.1
does not, by itself, prove `P30-FULL-HKCOMM(eta_HK)` on full blocks whose
recoupling mixing graph connects the adjoint sector to a two-index sector
that is not annihilated by the signed/residual factor.

Proof.

Lemma 132.2 gives a fixed asymptotic lower gap for simultaneously balancing
the adjoint and two-index symmetric weights against the singlet weight.
Lemma 131.2 says exact heat commutation on a connected full block requires
equal heat weights on all channels connected by nonzero recoupling entries.
Thus a full block containing such a connected three-channel component cannot
be made heat-commuting by the scalar adjoint-balance selector.

The final clause is careful: `P30-FULL-HKCOMM` contains the product
$$
(U^*DU-D)(U^*RU)(U^*\Sigma U).
$$
Even if \(U^*DU-D\) is order one on a nonbalanced channel, the product may
vanish if the actual residual/signed factor annihilates that channel or if
the actual law gives it zero normalized mass.  Such annihilation is a new
same-law value/support theorem.  It is not supplied by heat balance alone.
`square`

## 133. Exact Replacement For `P30-FULL-HKCOMM`

The heat-commutation route is therefore not dead, but its correct statement
is not "balance the adjoint block."  It is a support-sensitive theorem:
nonbalanced heat channels must either be absent, annihilated, or paid.

### Definition 133.1: Full Heat-Balanced Support Source

For \(\delta_{HK},u_{HK}\ge0\),
`P30-FULL-HKBAL-SUPPORT(delta_HK,u_HK)` asserts that, cofinally, the full
blocks can be partitioned into:

1. a heat-balanced sector \(\mathcal B_{bal}\), on which
   $$
   \left\|
   U_\Gamma^*D_\Gamma U_\Gamma-D_\Gamma
   \right\|_{op}
   \le \delta_{HK};
   $$
2. a heat-unbalanced sector \(\mathcal B_{unbal}\), whose normalized
   signed/residual absolute contribution is at most \(u_{HK}\):
   $$
   \limsup_{(N,j)}
   {1\over Z_B^{N,j}(\eta)}
   \sum_{\Gamma\in\mathcal B_{unbal}}
   {1\over2}
   \left\|
   (U^*D_\Gamma U-D_\Gamma)
   (U^*R_\Gamma U)(U^*\Sigma_\Gamma U)
   \right\|_1
   \le u_{HK}.
   $$

The first clause is finite representation/heat data.  The second clause is a
same-law support or value theorem for the part of the actual block matrix
that lives on unbalanced channels.

### Lemma 133.2: Heat-Balanced Support Sources `FULL-HKCOMM`

Assume `P30-FULL-HKBAL-SUPPORT(delta_HK,u_HK)`.  Let
$$
B_{R\Sigma}
$$
be a cofinal normalized bound for
$$
{1\over Z_B^{N,j}(\eta)}
\sum_{\Gamma\in\mathcal B_{bal}}
{1\over2}
\left\|
(U^*R_\Gamma U)(U^*\Sigma_\Gamma U)
\right\|_1.
$$
Then
$$
\mathrm{P30\text{-}FULL\text{-}HKCOMM}
(\delta_{HK}B_{R\Sigma}+u_{HK})
$$
holds.

Proof.

On \(\mathcal B_{bal}\), use
$$
\|(U^*DU-D)(U^*RU)(U^*\Sigma U)\|_1
\le
\|U^*DU-D\|_{op}\,
\|(U^*RU)(U^*\Sigma U)\|_1.
$$
The heat-balanced support source bounds the operator norm by
\(\delta_{HK}\), and the normalized sum of the second factor is
\(B_{R\Sigma}\).  The unbalanced sector is paid by \(u_{HK}\). `square`

### Proposition 133.3: Current-Corpus Status Of Full Heat-Balanced Support

The current corpus does not prove
`P30-FULL-HKBAL-SUPPORT(delta_HK,u_HK)` in a closing range.

Proof.

Theorem 113.1 proves adjoint/singlet rank-diagonal balance only for the
minimal diagnostic mismatch.  Theorem 132.3 proves that this cannot be
extended universally to full blocks containing two-index channels.  Therefore
a full heat-balanced support theorem must additionally prove that the actual
high-charge signed/residual block avoids or annihilates all nonbalanced
channels, or that their normalized contribution is small.  That is exactly
the second clause of Definition 133.1, and no previous paper prints such a
same-law support/value theorem. `square`

## 134. `P30-FULL-HKCOMM` Verdict

### Theorem 134.1: Full Heat Commutation Is Settled As A Structural Route

The current corpus proves the following sharp status.

1. Exact full-block heat commutation is equivalent to heat-weight constancy
   on the connected components of the recoupling mixing graph.
2. The rank-diagonal balance selector closes only the singlet/adjoint
   diagnostic mismatch.
3. Universal extension of that balance to full blocks is impossible: the
   two-index channel gives an asymptotic gap of at least \(1/3\) in the
   three-channel balance test.
4. `P30-FULL-HKCOMM` remains possible only through the support-sensitive
   source
   $$
   \mathrm{P30\text{-}FULL\text{-}HKBAL\text{-}SUPPORT}
   (\delta_{HK},u_{HK}),
   $$
   or through a direct actual-law cancellation of
   $$
   (U^*DU-D)(U^*RU)(U^*\Sigma U).
   $$

Proof.

Item 1 is Lemma 131.2.  Item 2 is Theorem 113.1.  Item 3 is Theorem 132.3.
Item 4 is Lemma 133.2 together with Proposition 133.3. `square`

### Corollary 134.2: Updated Priority After The Heat-Commutation Attack

The best remaining positive moves are now:

1. prove `P30-FULL-HKBAL-SUPPORT(delta_HK,u_HK)` by showing that actual
   signed/residual mass lives only on heat-balanced full-block components;
2. if that fails, attack `P30-FULL-SIGPAR`, because signed anti-invariance
   could cancel even heat-unbalanced channels;
3. then attack `P30-FULL-RPFQI`, the actual residual/Jacobian
   quasi-invariance theorem;
4. in parallel, keep `P30-SWITCH-AREA(A_0)` as the absolute-payment fallback;
5. if the nonbalanced heat sector is sign-coherent in the predebit ledger,
   promote it to a floor witness.

This is a genuine pruning of the search tree: the naive hope that the
rank-diagonal adjoint balance automatically controls full recoupling blocks
is falsified.  What remains is a sharper support/cancellation problem on the
same adaptive pushed-forward law.

## 135. The Heat-Bad Full-Block Classifier

The next step is to make the heat-unbalanced part literal.  Once it is a
finite component set, there is no more ambiguity about what must be bounded
by a same-law value theorem.

### Definition 135.1: Component Heat Oscillation

For a full block \(\Gamma\), let
$$
\mathcal C(\Gamma)
$$
be the connected components of the recoupling mixing graph
\(\mathcal G_\Gamma^U\) from Definition 131.1.

For \(C\in\mathcal C(\Gamma)\), define the heat oscillation
$$
\omega_{HK}(C;t,N)
:=
\max_{\alpha,\beta\in C}
|w_\alpha(t,N)-w_\beta(t,N)|.
$$

For a tolerance \(\delta\ge0\), call \(C\)

1. `HK-good(delta)` if \(\omega_{HK}(C;t,N)\le\delta\);
2. `HK-bad(delta)` if \(\omega_{HK}(C;t,N)>\delta\).

Let
$$
P_C
$$
denote the orthogonal projection onto the channel span of \(C\).  Since the
components are components of the support graph of \(U_\Gamma\), both
\(U_\Gamma\) and \(D_\Gamma\) are block-diagonal with respect to
$$
\mathcal H_\Gamma^{full}
=
\bigoplus_{C\in\mathcal C(\Gamma)}
P_C\mathcal H_\Gamma^{full}.
$$

### Table 135.2: Universal Low-Channel Heat Diagnostics

At the adjoint balance time
$$
t_A(N)={\log(N^2-1)\over \lambda_{HK}N},
$$
the low channels relevant to the first obstruction have:

| channel \(\lambda\) | \(d_\lambda\) | \(C_2^{std}(\lambda)\) | \(w_\lambda(t_A,N)\) as \(N\to\infty\) |
|---|---:|---:|---:|
| \(1\) | \(1\) | \(0\) | \(1\) |
| \(\mathrm{Ad}\) | \(N^2-1\) | \(N\) | \(1\) |
| \(S_2\) | \(N(N+1)/2\) | \((N-1)(N+2)/N\) | \(1/2\) |
| \(\Lambda_2\) | \(N(N-1)/2\) | \((N+1)(N-2)/N\) | \(1/2\) |

Thus a component that mixes \(\{1,\mathrm{Ad}\}\) with \(S_2\) or
\(\Lambda_2\) is asymptotically `HK-bad(delta)` for every
\(\delta<1/2\), and it is uniformly bad for the three-channel simultaneous
balance problem at the sharper obstruction level of Lemma 132.2.

### Lemma 135.3: The Classifier Is A Finite Same-Law Selector

For each finite \((N,j)\), tolerance \(\delta\), and full corridor block
\(\Gamma\), the predicate
$$
C\in\mathcal C(\Gamma)
\quad\mapsto\quad
\mathbf 1_{\mathrm{HK\text{-}bad}(\delta)}(C)
$$
is determined by:

1. the finite list of irreducible channel labels in \(\Gamma\);
2. their dimensions and standard Casimirs;
3. the zero/nonzero support pattern of the recoupling matrix \(U_\Gamma\);
4. the chosen same-law heat time \(t(N,j)\).

It does not depend on any auxiliary probability law.

Proof.

The component relation is the connected-component relation in the finite
support graph of \(U_\Gamma\).  The heat weights are the deterministic
functions
$$
w_\alpha(t,N)
=
d_{\lambda_\alpha}
\exp\{-t\lambda_{HK}C_2^{std}(\lambda_\alpha)\}.
$$
Therefore \(\omega_{HK}(C;t,N)\) is a finite deterministic number once the
same-law cofinal selector has chosen \(t(N,j)\).  No conditional transition
kernel, comparison process, or hidden Markov state is being introduced.
`square`

### Lemma 135.4: Two-Index Bad Components Cannot Be Moved Into The Good Set

Fix any \(\delta<1/3\).  Cofinally, every connected full-block component
that mixes the singlet or adjoint channel with a two-index channel
\(S_2\) or \(\Lambda_2\) is `HK-bad(delta)` for every heat-time selector
that keeps the singlet/adjoint diagnostic in the rank-diagonal closing
window.

Proof.

If the heat time does not keep the singlet/adjoint diagnostic in the
rank-diagonal closing window, the minimal diagnostic already leaves the
Paper-30 positive route.  Along selectors that do keep that diagnostic in
range, the adjoint and singlet weights are asymptotically comparable to
one.  Lemma 132.2 shows that adding a connected two-index channel forces a
liminf heat mismatch at least \(1/3\) in the simultaneous three-channel
test.  Hence for every fixed \(\delta<1/3\), the component is eventually
classified as heat-bad. `square`

### Corollary 135.5: What The Classifier Has Settled

The heat-bad set is not a matter of taste.  It is a finite, same-law,
representation-theoretic row set.  What is unknown is not which rows are
heat-bad; what is unknown is the actual signed/residual mass carried by
those rows.

Equivalently, after Section 135 the live problem is no longer:
$$
\text{Can the full block be made universally heat-balanced?}
$$
That answer is no.  The live problem is:
$$
\text{Does the actual adaptive law charge the heat-bad full-block sector?}
$$

## 136. The Exact Heat-Bad Debit

We now name the actual quantity that must be small.  This is deliberately
not a new law.  It is the same finite DLR/Peter-Weyl matrix already present
in the full-block switching ledger, projected onto the heat-bad components.

### Definition 136.1: Heat-Bad Projection

For a tolerance \(\delta\), define
$$
P_{\Gamma,bad}^{HK}(\delta)
:=
\sum_{\substack{C\in\mathcal C(\Gamma)\\
C\ \mathrm{HK\text{-}bad}(\delta)}}
P_C,
$$
and
$$
P_{\Gamma,good}^{HK}(\delta)
:=
I-P_{\Gamma,bad}^{HK}(\delta).
$$

The corresponding heat-commutator defect is
$$
\mathcal K_\Gamma^{HK}
:=
(U_\Gamma^*D_\Gamma U_\Gamma-D_\Gamma)
(U_\Gamma^*R_\Gamma U_\Gamma)
(U_\Gamma^*\Sigma_\Gamma U_\Gamma).
$$

Define the normalized heat-bad debit
$$
\mathfrak u_{HK}^{N,j}(\delta)
:=
{1\over Z_B^{N,j}(\eta)}
\sum_{\Gamma}
{1\over2}
\left\|
P_{\Gamma,bad}^{HK}(\delta)
\mathcal K_\Gamma^{HK}
\right\|_1.
$$

Define also the normalized heat-good residual size
$$
B_{R\Sigma}^{N,j}(\delta)
:=
{1\over Z_B^{N,j}(\eta)}
\sum_{\Gamma}
{1\over2}
\left\|
P_{\Gamma,good}^{HK}(\delta)
(U_\Gamma^*R_\Gamma U_\Gamma)
(U_\Gamma^*\Sigma_\Gamma U_\Gamma)
\right\|_1.
$$

All sums are over the same full corridor block family already used in
Sections 126--134.

### Lemma 136.2: The Heat-Bad Debit Is Exactly The Missing Support Source

Assume cofinally that
$$
\limsup_{(N,j)}\mathfrak u_{HK}^{N,j}(\delta)\le u_{HK}
$$
and
$$
\limsup_{(N,j)}B_{R\Sigma}^{N,j}(\delta)\le B_{R\Sigma}.
$$
Then
$$
\mathrm{P30\text{-}FULL\text{-}HKCOMM}
(\delta B_{R\Sigma}+u_{HK})
$$
holds.

Proof.

Decompose the heat-commutator term into its good and bad projections:
$$
\mathcal K_\Gamma^{HK}
=
P_{\Gamma,good}^{HK}(\delta)\mathcal K_\Gamma^{HK}
+
P_{\Gamma,bad}^{HK}(\delta)\mathcal K_\Gamma^{HK}.
$$
On the good projection,
$$
\left\|
P_{\Gamma,good}^{HK}(\delta)
(U_\Gamma^*D_\Gamma U_\Gamma-D_\Gamma)
\right\|_{op}
\le \delta
$$
by the definition of `HK-good(delta)` and Lemma 131.2: on each good
component the diagonal heat weights have range at most \(\delta\), and
unitary conjugation inside that component changes the diagonal operator by
operator norm at most that range.  Therefore
$$
\left\|
P_{\Gamma,good}^{HK}(\delta)\mathcal K_\Gamma^{HK}
\right\|_1
\le
\delta
\left\|
P_{\Gamma,good}^{HK}(\delta)
(U_\Gamma^*R_\Gamma U_\Gamma)
(U_\Gamma^*\Sigma_\Gamma U_\Gamma)
\right\|_1.
$$
After normalization and limsup, the good part contributes at most
\(\delta B_{R\Sigma}\).  The bad part is exactly
\(\mathfrak u_{HK}^{N,j}(\delta)\), hence contributes at most \(u_{HK}\).
`square`

### Definition 136.3: The Sharp Same-Law Heat-Bad Mass Gate

For \(\delta<1/3\) and \(\mu\ge0\),
`P30-HKBAD-MASS(delta,mu)` asserts
$$
\limsup_{(N,j)}
\mathfrak u_{HK}^{N,j}(\delta)
\le \mu.
$$

`P30-HKBAD-ZERO(delta)` is the special case \(\mu=0\).

This is the precise positive theorem that would source the heat-commutator
part of the full-block signed-switching route.

### Corollary 136.4: Closing Inequality For The Heat-Bad Route

Assume:

1. `P30-HKBAD-MASS(delta,mu)`;
2. \(B_{R\Sigma}^{N,j}(\delta)\le B_{R\Sigma}\) cofinally;
3. `P30-FULL-SIGPAR(eta_Sigma)`;
4. `P30-FULL-RPFQI(eta_R)`.

Then the full-block signed-switching positive route closes whenever
$$
M_{\mathrm{sgn}}(\kappa)
-
\epsilon_s
-
u
-
\eta_\Sigma
-
\eta_R
-
\delta B_{R\Sigma}
-
\mu
>
0.
$$

Proof.

Lemma 136.2 supplies
$$
\eta_{HK}=\delta B_{R\Sigma}+\mu.
$$
Substitute this into the debit inequality from Theorem 130.1. `square`

## 137. Current-Corpus Verdict On `P30-HKBAD-MASS`

The heat-bad classifier is finite and explicit.  The mass gate is not yet
closed.

### Proposition 137.1: Representation Data Alone Cannot Prove Heat-Bad Mass Smallness

The current representation-theoretic corpus proves the existence and
classification of heat-bad components, but it does not prove
`P30-HKBAD-MASS(delta,mu)` in a closing range.

Proof.

Sections 131--135 determine the operator
$$
P_{\Gamma,bad}^{HK}(\delta)(U_\Gamma^*D_\Gamma U_\Gamma-D_\Gamma)
$$
from finite channel data.  They do not determine the actual same-law matrix
factor
$$
(U_\Gamma^*R_\Gamma U_\Gamma)(U_\Gamma^*\Sigma_\Gamma U_\Gamma)
$$
on the same projection.  The latter contains the actual residual/Jacobian
and signed insertion of the adaptive finite DLR law.  Papers 26--29 proved
that these actual residual values are not recovered from scalar labels or
finite template enumeration alone.  Therefore representation data alone can
classify the bad sector but cannot bound its same-law signed/residual mass.
`square`

### Proposition 137.2: The Five Current Ways To Source The Gate

Within adaptive Branch A, `P30-HKBAD-MASS(delta,mu)` can be sourced only by
one of the following same-law inputs:

1. **support zero:** prove \(P_{\Gamma,bad}^{HK}(\delta)
(U_\Gamma^*R_\Gamma U_\Gamma)(U_\Gamma^*\Sigma_\Gamma U_\Gamma)=0\)
cofinally;
2. **signed cancellation:** prove that the heat-bad contribution is
antisymmetric or nearly antisymmetric in trace norm, giving
`P30-FULL-SIGPAR(eta_Sigma)` on the bad projection;
3. **residual quasi-invariance:** prove that the residual/Jacobian factor is
approximately invariant under the full recoupling switch on the bad
projection, giving `P30-FULL-RPFQI(eta_R)` there;
4. **absolute smallness:** prove an actual-law bound on
\(\mathfrak u_{HK}^{N,j}(\delta)\) directly;
5. **floor exit:** if the heat-bad contribution is sign-coherent and exceeds
the Branch-A budget, promote it to the lower-floor route instead of trying
to absorb it.

Proof.

The heat-bad debit is the normalized trace norm of the heat-bad projection
of the exact full-block defect.  To make it small without leaving Branch A,
one must either remove the support, cancel it by the sign, make the residual
factor invariant enough that the commutator product is harmless, or bound
the absolute same-law value directly.  If the opposite sign-coherent lower
bound is proved, the same object becomes a floor witness and adaptive
Branch A is falsified rather than closed.  These are exhaustive for the
decomposition in Definition 136.1. `square`

### Theorem 137.3: `P30-FULL-HKBAL-SUPPORT` Is Reduced To A Primitive Same-Law Value Gate

For every fixed \(\delta<1/3\), the present corpus proves:

1. the finite heat-bad component classifier;
2. the exact heat-bad debit \(\mathfrak u_{HK}^{N,j}(\delta)\);
3. the implication
   $$
   \mathrm{P30\text{-}HKBAD\text{-}MASS}(\delta,\mu)
   \Rightarrow
   \mathrm{P30\text{-}FULL\text{-}HKCOMM}
   (\delta B_{R\Sigma}+\mu);
   $$
4. the current-corpus non-derivation of the mass bound from representation
   data alone.

Thus the remaining heat route is a single primitive same-law value theorem:
bound the actual adaptive signed/residual mass on the heat-bad full-block
projection.

Proof.

Items 1 and 2 are Definitions 135.1 and 136.1 plus Lemma 135.3.  Item 3 is
Lemma 136.2.  Item 4 is Proposition 137.1. `square`

### Corollary 137.4: Next Action After The Heat-Bad Reduction

The next positive attack should not add more canonical labels.  It should
work on the heat-bad projection itself:
$$
P_{\Gamma,bad}^{HK}(\delta)
(U_\Gamma^*R_\Gamma U_\Gamma)
(U_\Gamma^*\Sigma_\Gamma U_\Gamma).
$$

The most promising order is:

1. prove exact support zero on the bad projection;
2. if support is nonzero, prove signed antisymmetry there;
3. if signed antisymmetry fails, prove residual quasi-invariance there;
4. if all three fail, test whether the same bad projection gives a
   sign-coherent floor witness.

This keeps the work Barandes-aligned: no hidden Markovian dynamics is
inserted, no cleaner comparison law replaces the actual law, and the object
being bounded is the exact same-law finite DLR/Peter-Weyl block already in
the corridor ledger.

## 138. Support-Zero Audit On The Heat-Bad Projection

The cleanest possible positive outcome would be that the heat-bad projection
is simply absent from the actual signed/residual block.  We now isolate that
as a theorem and test what the present corpus can prove.

### Definition 138.1: Heat-Bad Actual Support-Zero Gate

For \(\delta<1/3\), `P30-HKBAD-ACTZERO(delta)` asserts that cofinally
$$
P_{\Gamma,bad}^{HK}(\delta)
(U_\Gamma^*R_\Gamma U_\Gamma)
(U_\Gamma^*\Sigma_\Gamma U_\Gamma)
=0
$$
for every retained full corridor block \(\Gamma\).

Equivalently,
$$
\mathfrak u_{HK}^{N,j}(\delta)=0
$$
cofinally.

### Lemma 138.2: Actual Support-Zero Immediately Closes The Heat-Bad Debit

If `P30-HKBAD-ACTZERO(delta)` holds, then
$$
\mathrm{P30\text{-}HKBAD\text{-}MASS}(\delta,0)
$$
holds.

Consequently,
$$
\mathrm{P30\text{-}FULL\text{-}HKCOMM}
(\delta B_{R\Sigma})
$$
holds whenever the good-sector size \(B_{R\Sigma}\) is cofinally bounded.

Proof.

The first assertion is Definition 136.1 with the heat-bad projected matrix
set to zero.  The final assertion is Lemma 136.2 with \(u_{HK}=0\).
`square`

### Proposition 138.3: Pure Representation Theory Does Not Prove Support-Zero

`P30-HKBAD-ACTZERO(delta)` is not a consequence of the finite recoupling
labels, Littlewood-Richardson support, or heat weights alone.

Proof.

The full-block carrier contains all invariant tensor channels licensed by
the finite corridor template.  In particular, whenever a local pair of
fundamental-type legs is present, the standard decomposition contains
$$
F\otimes F
\cong
S_2\oplus\Lambda_2,
$$
with nonzero Littlewood-Richardson multiplicity for both summands.  These
are precisely the two-index channels that Lemma 135.4 classifies as
heat-bad when connected to the singlet/adjoint diagnostic component.

The representation data therefore identify the bad channels; they do not
annihilate them.  To see the logical point sharply, set the residual and
signed factors formally to the identity on a finite block that contains the
two-index channel.  Then the bad projection is nonzero.  Thus no theorem
using only channel existence, dimensions, Casimirs, and recoupling support
can imply
$$
P_{\Gamma,bad}^{HK}(\delta)
(U_\Gamma^*R_\Gamma U_\Gamma)
(U_\Gamma^*\Sigma_\Gamma U_\Gamma)
=0.
$$
Any true proof of `P30-HKBAD-ACTZERO(delta)` must use actual same-law
information about \(R_\Gamma\), \(\Sigma_\Gamma\), or their product.
`square`

### Corollary 138.4: Support-Zero Is A Real Same-Law Theorem, Not A Label Theorem

The support-zero subroute is now settled at the current-corpus level:

1. it is a valid positive source if proved for the actual adaptive law;
2. it would close `P30-HKBAD-MASS(delta,0)`;
3. it is not derivable from representation labels or heat balance alone;
4. it can still be true only through actual signed/residual annihilation.

Therefore the next nontrivial positive move is not another support
classifier.  It is either:
$$
\mathrm{P30\text{-}HKBAD\text{-}ACTZERO}(\delta)
$$
from actual signed/residual annihilation, or the weaker cancellation route
$$
\mathrm{P30\text{-}FULL\text{-}SIGPAR}(\eta_\Sigma)
$$
restricted to the heat-bad projection.

## 139. Signed Cancellation On The Heat-Bad Projection

The support-zero route has been reduced to actual signed/residual
annihilation.  The next possibility is signed cancellation.  On a heat-bad
component, however, one must be careful: bare switch-oddness of
\(\Sigma\) is not the right theorem.  The heat weights themselves are the
obstruction, so cancellation must be cancellation of the weighted object.

### Definition 139.1: Heat-Bad Weighted Oddness

For \(\delta<1/3\), define the heat-bad weighted signed defect
$$
\Theta_{bad}^{WODD,N,j}(\delta)
:=
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma
{1\over2}
\left\|
P_{\Gamma,bad}^{HK}(\delta)
\left(
D_\Gamma R_\Gamma\Sigma_\Gamma
+
U_\Gamma^*D_\Gamma R_\Gamma\Sigma_\Gamma U_\Gamma
\right)
\right\|_1.
$$

`P30-HKBAD-WODD(delta,theta)` asserts
$$
\limsup_{(N,j)}
\Theta_{bad}^{WODD,N,j}(\delta)
\le \theta.
$$

This is the direct signed-cancellation theorem on the heat-bad sector.  It
does not ask the bad sector to vanish.  It asks the actual weighted signed
contribution of that sector to be odd enough under the full recoupling
switch.

### Lemma 139.2: Heat-Bad Weighted Oddness Pays The Bad Sector Directly

Let
$$
\Theta_{good}^{sw,N,j}(\delta)
:=
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma
{1\over2}
\left\|
P_{\Gamma,good}^{HK}(\delta)
\left(
D_\Gamma R_\Gamma\Sigma_\Gamma
+
U_\Gamma^*D_\Gamma R_\Gamma\Sigma_\Gamma U_\Gamma
\right)
\right\|_1.
$$

If
$$
\limsup_{(N,j)}
\Theta_{good}^{sw,N,j}(\delta)\le\theta_{good}
$$
and `P30-HKBAD-WODD(delta,theta_bad)` holds, then
$$
\mathrm{P30\text{-}FULLBLOCK\text{-}SWDEF}
(\theta_{good}+\theta_{bad})
$$
holds.

Proof.

For each block,
$$
\mathcal E_\Gamma^{full}
=
P_{\Gamma,good}^{HK}(\delta)\mathcal E_\Gamma^{full}
+
P_{\Gamma,bad}^{HK}(\delta)\mathcal E_\Gamma^{full}.
$$
The trace norm triangle inequality gives the sum of the good and bad
projected norms.  The good part is bounded by \(\theta_{good}\), and the
bad part is exactly `P30-HKBAD-WODD(delta,theta_bad)`. `square`

### Corollary 139.3: Positive Budget For The Weighted-Odd Route

If the good sector is controlled with debit \(\theta_{good}\), the heat-bad
sector is controlled by `P30-HKBAD-WODD(delta,theta_bad)`, and the abandoned
or unpaired sector has normalized mass \(u\), then adaptive Branch A closes
whenever
$$
M_{\mathrm{sgn}}(\kappa)
-
\epsilon_s
-
u
-
\theta_{good}
-
\theta_{bad}
>
0.
$$

Proof.

Lemma 139.2 gives the full-block switching defect.  The signed high-charge
bound is then Theorem 126.5, with the usual residual budget
\(\epsilon_s\). `square`

## 140. Bare Signed Parity Is Not Enough On Heat-Bad Components

The phrase "signed cancellation" can be misleading.  If it means only
\(\Sigma+U^*\Sigma U=0\), it does not by itself solve the heat-bad problem.

### Lemma 140.1: Two-Channel Counterexample To Bare Parity

There are finite matrices \(U,D,\Sigma\) such that
$$
U^*\Sigma U=-\Sigma
$$
but
$$
D\Sigma+U^*D\Sigma U\ne0.
$$

Proof.

Let
$$
U=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
\Sigma=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix},
\qquad
D=
\begin{pmatrix}
d_1&0\\
0&d_2
\end{pmatrix},
$$
with \(d_1\ne d_2\).  Then \(U^*\Sigma U=-\Sigma\).  But
$$
D\Sigma+U^*D\Sigma U
=
\begin{pmatrix}
d_1-d_2&0\\
0&d_1-d_2
\end{pmatrix},
$$
which is nonzero. `square`

### Corollary 140.2: `P30-FULL-SIGPAR` Must Be Weighted Or Accompanied By Heat/Residual Control

On heat-bad components, bare switch-oddness of the signed insertion
\(\Sigma\) does not imply heat-bad weighted oddness.  A useful signed route
must prove one of the following:

1. the actual weighted statement `P30-HKBAD-WODD(delta,theta)`;
2. bare signed parity plus separate heat commutator control;
3. bare signed parity plus residual quasi-invariance and a compensating
   identity for the heat mismatch;
4. a direct cancellation in the full product \(DR\Sigma+U^*DR\Sigma U\).

Proof.

Lemma 140.1 is already a heat-bad finite block with \(R=I\).  Thus
\(\Sigma\)-oddness alone is not enough once \(D\) is nonconstant on the
recoupling component.  The four listed options are exactly the ways to
restore cancellation after the heat mismatch is included. `square`

## 141. Current-Corpus Verdict On Heat-Bad Signed Cancellation

### Proposition 141.1: The Current Corpus Does Not Prove Heat-Bad Weighted Oddness

The current corpus does not prove
`P30-HKBAD-WODD(delta,theta)` in a closing range.

Proof.

`P30-HKBAD-WODD(delta,theta)` is a bound on the actual same-law finite
matrix
$$
P_{\Gamma,bad}^{HK}(\delta)
\left(
D_\Gamma R_\Gamma\Sigma_\Gamma
+
U_\Gamma^*D_\Gamma R_\Gamma\Sigma_\Gamma U_\Gamma
\right).
$$
Sections 135--138 print the heat-bad projection and prove that support-zero
is not forced by representation theory.  Lemma 140.1 proves that even exact
bare sign oddness of \(\Sigma\) would not force weighted oddness when the
heat weights differ.  Therefore a proof of `P30-HKBAD-WODD` must use actual
same-law information about the product \(R_\Gamma\Sigma_\Gamma\), not just
recoupling labels, Casimirs, dimensions, or the sign character of the
bridge observable.  Papers 26--29 do not provide that product value on the
heat-bad full-block projection. `square`

### Theorem 141.2: Signed Cancellation Route Is Settled To A Weighted Primitive Gate

The signed-cancellation subroute on the heat-bad sector has the following
sharp status.

1. The valid positive theorem is not bare signed parity; it is
   `P30-HKBAD-WODD(delta,theta)`.
2. If this theorem holds with a closing \(\theta\), it directly pays the
   heat-bad sector in the full-block switching defect.
3. Bare switch-oddness of \(\Sigma\) is insufficient on heat-bad components.
4. The current corpus does not prove the weighted theorem in a closing
   range.

Thus the next remaining positive option is residual/Jacobian
quasi-invariance on the heat-bad projection, or else a direct absolute
smallness/floor analysis of the same projected weighted matrix.

Proof.

Item 1 is Definition 139.1.  Item 2 is Lemma 139.2 and Corollary 139.3.
Item 3 is Lemma 140.1 and Corollary 140.2.  Item 4 is Proposition 141.1.
`square`

### Corollary 141.3: Updated Live Target

After support-zero and signed cancellation have both been audited, the live
heat-bad front is:
$$
\boxed{
\mathrm{P30\text{-}HKBAD\text{-}RPFQI}(\eta_R)
\quad\text{or}\quad
\mathrm{P30\text{-}HKBAD\text{-}ABS}(\mu)
\quad\text{or}\quad
\mathrm{P30\text{-}HKBAD\text{-}FLOOR}(M_*).
}
$$

Here `P30-HKBAD-RPFQI` means residual/Jacobian quasi-invariance restricted
to \(P_{\Gamma,bad}^{HK}(\delta)\), `P30-HKBAD-ABS` means a direct absolute
same-law bound on the weighted bad defect, and `P30-HKBAD-FLOOR` is the
sign-coherent lower-floor alternative.

## 142. Residual Quasi-Invariance On The Heat-Bad Projection

The next possible escape is that the actual residual/Jacobian insertion
\(R_\Gamma\) is almost invariant under the full recoupling switch on the
heat-bad sector.  This is a meaningful same-law theorem, but it must be
kept in its correct place: it pays the residual term in the decomposition,
not the whole heat-bad weighted defect by itself.

### Definition 142.1: Heat-Bad Residual Quasi-Invariance

For \(\delta<1/3\), define
$$
\Theta_{bad}^{RPFQI,N,j}(\delta)
:=
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma
{1\over2}
\left\|
P_{\Gamma,bad}^{HK}(\delta)
D_\Gamma
(U_\Gamma^*R_\Gamma U_\Gamma-R_\Gamma)
(U_\Gamma^*\Sigma_\Gamma U_\Gamma)
\right\|_1.
$$

`P30-HKBAD-RPFQI(delta,eta_R)` asserts
$$
\limsup_{(N,j)}
\Theta_{bad}^{RPFQI,N,j}(\delta)
\le \eta_R.
$$

This is the heat-bad restriction of `P30-FULL-RPFQI`.

### Lemma 142.2: Projected Three-Term Identity

On the heat-bad projection,
$$
P_{\Gamma,bad}^{HK}(\delta)\mathcal E_\Gamma^{full}
=
P_{\Gamma,bad}^{HK}(\delta)
D_\Gamma R_\Gamma
(\Sigma_\Gamma+U_\Gamma^*\Sigma_\Gamma U_\Gamma)
$$
$$
\quad+
P_{\Gamma,bad}^{HK}(\delta)
(U_\Gamma^*D_\Gamma U_\Gamma-D_\Gamma)
(U_\Gamma^*R_\Gamma U_\Gamma)
(U_\Gamma^*\Sigma_\Gamma U_\Gamma)
$$
$$
\quad+
P_{\Gamma,bad}^{HK}(\delta)
D_\Gamma
(U_\Gamma^*R_\Gamma U_\Gamma-R_\Gamma)
(U_\Gamma^*\Sigma_\Gamma U_\Gamma).
$$

Proof.

Apply the full-block decomposition of Lemma 127.1 and left-multiply by the
finite projection \(P_{\Gamma,bad}^{HK}(\delta)\). `square`

### Lemma 142.3: Heat-Bad RPFQI Pays Only The Residual Term

If `P30-HKBAD-RPFQI(delta,eta_R)` holds, then the third term in the
projected identity of Lemma 142.2 contributes at most \(\eta_R\) to the
normalized heat-bad switching defect.

Proof.

This is exactly Definition 142.1. `square`

### Proposition 142.4: RPFQI Alone Does Not Close The Heat-Bad Sector

Even exact residual quasi-invariance on the heat-bad projection does not
imply heat-bad weighted oddness.

Proof.

Take the two-channel example of Lemma 140.1 and set \(R=I\).  Then
$$
U^*RU-R=0,
$$
so residual quasi-invariance is exact.  But Lemma 140.1 gives
$$
D\Sigma+U^*D\Sigma U\ne0
$$
whenever \(d_1\ne d_2\).  Thus the heat-bad weighted defect can remain
nonzero even when the residual/Jacobian factor is perfectly invariant.
`square`

### Proposition 142.5: The Current Corpus Does Not Prove Heat-Bad RPFQI

The current corpus does not prove
`P30-HKBAD-RPFQI(delta,eta_R)` in a closing range.

Proof.

The gate is a bound on the actual same-law matrix
$$
P_{\Gamma,bad}^{HK}(\delta)
D_\Gamma
(U_\Gamma^*R_\Gamma U_\Gamma-R_\Gamma)
(U_\Gamma^*\Sigma_\Gamma U_\Gamma).
$$
The finite recoupling graph and heat weights determine
\(P_{\Gamma,bad}^{HK}(\delta)\) and \(D_\Gamma\), but not
\(U_\Gamma^*R_\Gamma U_\Gamma-R_\Gamma\).  Proposition 128.3 already proves
that the full-block residual quasi-invariance theorem is not supplied by
the current corpus.  Restricting to a heat-bad projection does not create
new information about the actual residual/Jacobian entries.  Therefore the
projected gate remains a primitive same-law value theorem. `square`

### Theorem 142.6: Heat-Bad RPFQI Is Valid But Not A Standalone Escape

The residual quasi-invariance route on the heat-bad sector has the following
status.

1. `P30-HKBAD-RPFQI(delta,eta_R)` is a valid same-law projected debit.
2. It pays exactly the residual term in the projected three-term identity.
3. It does not by itself imply weighted oddness or heat-bad smallness.
4. The current corpus does not prove it in a closing range.

Thus residual quasi-invariance is useful only if paired with either weighted
signed cancellation, heat-bad absolute smallness, or a floor analysis of the
remaining heat-bad product.

Proof.

Items 1 and 2 are Definitions 142.1 and Lemma 142.3.  Item 3 is
Proposition 142.4.  Item 4 is Proposition 142.5. `square`

## 143. Direct Absolute Smallness And The Floor Alternative

After support-zero, weighted signed cancellation, and projected RPFQI have
been audited, the remaining positive theorem is simply a direct bound on
the same heat-bad weighted defect.  If the opposite sign-coherent lower
bound holds, the same object becomes a floor witness instead.

### Definition 143.1: Direct Heat-Bad Absolute Bound

For \(\mu\ge0\), `P30-HKBAD-ABS(delta,mu)` asserts
$$
\limsup_{(N,j)}
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma
{1\over2}
\left\|
P_{\Gamma,bad}^{HK}(\delta)
\left(
D_\Gamma R_\Gamma\Sigma_\Gamma
+
U_\Gamma^*D_\Gamma R_\Gamma\Sigma_\Gamma U_\Gamma
\right)
\right\|_1
\le \mu.
$$

This is the direct version of `P30-HKBAD-WODD(delta,mu)`: no mechanism is
specified, only the actual same-law smallness of the weighted bad defect.

### Definition 143.2: Heat-Bad Floor Witness

For \(M_*>0\), `P30-HKBAD-FLOOR(M_*)` asserts that, after the same retained
row restrictions used in the Branch-A ledger, the heat-bad projected signed
contribution has a sign-coherent real lower bound
$$
\liminf_{(N,j)}
\left|
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma
{1\over2}
\operatorname{Re}\operatorname{Tr}
\left[
P_{\Gamma,bad}^{HK}(\delta)
\left(
D_\Gamma R_\Gamma\Sigma_\Gamma
+
U_\Gamma^*D_\Gamma R_\Gamma\Sigma_\Gamma U_\Gamma
\right)
\right]
\right|
\ge M_*.
$$

The phrase sign-coherent means that the lower bound survives the same
orientation, endpoint-additive, retained-row, and normalization conventions
used in the predebit ledger.  Without that coherence, a large norm is not a
floor.

### Lemma 143.3: Direct Absolute Smallness Closes The Heat-Bad Defect

If `P30-HKBAD-ABS(delta,mu)` holds and the heat-good sector has normalized
switching defect at most \(\theta_{good}\), then
$$
\mathrm{P30\text{-}FULLBLOCK\text{-}SWDEF}
(\theta_{good}+\mu)
$$
holds.

Proof.

This is Lemma 139.2 with `P30-HKBAD-WODD(delta,mu)` renamed as direct
absolute smallness. `square`

### Lemma 143.4: A Heat-Bad Floor Falsifies Adaptive Branch A Above Budget

If `P30-HKBAD-FLOOR(M_*)` holds and
$$
M_*>
M_{\mathrm{sgn}}(\kappa)-\epsilon_s-u,
$$
then the current adaptive Branch-A signed-switching budget cannot close.

Proof.

The Branch-A positive route requires the retained signed heat-bad
contribution to be absorbed into the available margin
\(M_{\mathrm{sgn}}(\kappa)-\epsilon_s-u\).  A sign-coherent lower bound
strictly above that margin contradicts absorbability in the same retained
ledger. `square`

### Proposition 143.5: The Current Corpus Proves Neither ABS Nor FLOOR

The current corpus proves neither `P30-HKBAD-ABS(delta,mu)` in a closing
range nor `P30-HKBAD-FLOOR(M_*)` above the Branch-A budget.

Proof.

Both assertions are quantitative statements about the actual same-law matrix
$$
P_{\Gamma,bad}^{HK}(\delta)
\left(
D_\Gamma R_\Gamma\Sigma_\Gamma
+
U_\Gamma^*D_\Gamma R_\Gamma\Sigma_\Gamma U_\Gamma
\right).
$$
Sections 135--142 determine the projection, the heat weights, the recoupling
support, and several exact implications.  They do not determine the actual
matrix values of \(R_\Gamma\Sigma_\Gamma\) on this projection.  A small
upper bound and a sign-coherent lower floor are opposite value theorems for
the same actual object.  Neither follows from the current representation,
selector, or finite-template corpus. `square`

## 144. Heat-Bad Sector Verdict

### Theorem 144.1: The Heat-Bad Branch Is Fully Reduced To One Actual Same-Law Object

Let
$$
\mathcal W_{\Gamma,bad}^{N,j}(\delta)
:=
P_{\Gamma,bad}^{HK}(\delta)
\left(
D_\Gamma R_\Gamma\Sigma_\Gamma
+
U_\Gamma^*D_\Gamma R_\Gamma\Sigma_\Gamma U_\Gamma
\right).
$$

The present corpus proves:

1. the heat-bad projection \(P_{\Gamma,bad}^{HK}(\delta)\) is finite and
   explicitly classifiable;
2. support-zero would close the heat-bad debit, but is not forced by
   representation theory;
3. bare signed parity is insufficient on heat-bad components;
4. the valid signed theorem is weighted oddness of
   \(\mathcal W_{\Gamma,bad}^{N,j}(\delta)\), but it is not sourced;
5. projected residual quasi-invariance is a valid debit, but not a
   standalone escape and not sourced;
6. direct absolute smallness or a sign-coherent floor are the remaining
   value alternatives, and neither is sourced by the current corpus.

Therefore no further finite-label refinement of the heat-bad branch can
close adaptive Branch A.  The next theorem must be new actual same-law
quantitative information about
$$
\mathcal W_{\Gamma,bad}^{N,j}(\delta).
$$

Proof.

Item 1 is Section 135.  Item 2 is Section 138.  Items 3 and 4 are
Sections 139--141.  Item 5 is Section 142.  Item 6 is Section 143. `square`

### Corollary 144.2: What Would Count As Positive Progress Now

Positive progress on Paper 30 now means proving exactly one of:
$$
\mathrm{P30\text{-}HKBAD\text{-}ACTZERO}(\delta),
$$
$$
\mathrm{P30\text{-}HKBAD\text{-}WODD}(\delta,\theta),
$$
$$
\mathrm{P30\text{-}HKBAD\text{-}ABS}(\delta,\mu),
$$
or a closing package combining
$$
\mathrm{P30\text{-}HKBAD\text{-}RPFQI}(\delta,\eta_R)
$$
with independent bounds for the remaining projected sign and heat terms.

Negative progress, equally valuable, means proving
$$
\mathrm{P30\text{-}HKBAD\text{-}FLOOR}(M_*)
$$
above the Branch-A budget.

Everything else is now bookkeeping.

## 145. Source-Response Reframing Of The Heat-Bad Object

The preceding verdict says that the missing object is the actual same-law
matrix
$$
\mathcal W_{\Gamma,bad}^{N,j}(\delta).
$$
The change of viewpoint is to stop asking for its entries directly.  Instead
we regard its trace norm as the support function of a finite source-response
body.  The impossible row value becomes the first derivative of a same-law
source functional.

This is not a path integral replacement and not a hidden dynamics.  It is a
finite deterministic source insertion into the same finite DLR law, followed
by differentiation at source strength zero.

### Definition 145.1: Heat-Bad Dual Tests

For each retained full block \(\Gamma\), let \(Q_\Gamma\) be a finite matrix
on the same full-block channel space such that
$$
\|Q_\Gamma\|_{op}\le1
$$
and
$$
Q_\Gamma=P_{\Gamma,bad}^{HK}(\delta)Q_\Gamma P_{\Gamma,bad}^{HK}(\delta).
$$

A heat-bad dual test is a finite family
$$
Q=\{Q_\Gamma\}_\Gamma
$$
of such matrices, chosen deterministically from the same retained
finite-record data.

Define the linear response functional
$$
\Lambda_{bad}^{N,j}(Q;\delta)
:=
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma
{1\over2}
\operatorname{Re}\operatorname{Tr}
\left(
Q_\Gamma^*
\mathcal W_{\Gamma,bad}^{N,j}(\delta)
\right).
$$

### Lemma 145.2: Trace-Norm Debit Is A Dual Response Supremum

The direct heat-bad absolute debit satisfies
$$
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma
{1\over2}
\left\|
\mathcal W_{\Gamma,bad}^{N,j}(\delta)
\right\|_1
=
\sup_Q
\Lambda_{bad}^{N,j}(Q;\delta),
$$
where the supremum is over all heat-bad dual tests \(Q\).

Proof.

For a finite matrix \(M\),
$$
\|M\|_1
=
\sup_{\|Q\|_{op}\le1}
\operatorname{Re}\operatorname{Tr}(Q^*M),
$$
with the supremum attained by the polar dual of \(M\).  Apply this
block-by-block to \(M=\mathcal W_{\Gamma,bad}^{N,j}(\delta)\), observing
that \(M\) is already supported on the heat-bad projection.  Sum and divide
by \(Z_B^{N,j}(\eta)\). `square`

### Definition 145.3: Same-Law Heat-Bad Source Functional

Let \(Q\) be a heat-bad dual test.  On the underlying finite DLR probability
space for \((N,j)\), let
$$
V_Q^{N,j}(\omega;\delta)
$$
be the deterministic real observable whose actual expectation is
$$
\mathbf E_{N,j}^{act}
\left[
V_Q^{N,j}(\cdot;\delta)
\right]
=
\Lambda_{bad}^{N,j}(Q;\delta).
$$
Concretely, \(V_Q\) is the blockwise trace-dual pairing with the heat-bad
weighted signed insertion before the final retained-block summation.  It is
the same finite DLR/Peter-Weyl integrand as in the corridor ledger, with a
deterministic source matrix \(Q_\Gamma\) inserted.

Define the source pressure
$$
\Psi_Q^{N,j}(s;\delta)
:=
\log
\mathbf E_{N,j}^{act}
\left[
\exp\left(sV_Q^{N,j}(\cdot;\delta)\right)
\right].
$$

This is a same-law source functional: the expectation is taken under the
actual adaptive finite DLR law.  For \(s\ne0\), \(\Psi_Q(s)\) is only a
generating function.  The physical debit is the derivative at \(s=0\), and
that derivative is evaluated under the actual law.

### Lemma 145.4: First Response Identity

For every heat-bad dual test \(Q\),
$$
{\partial\over\partial s}
\Psi_Q^{N,j}(0;\delta)
=
\Lambda_{bad}^{N,j}(Q;\delta).
$$

Consequently,
$$
\mathrm{P30\text{-}HKBAD\text{-}ABS}(\delta,\mu)
$$
is equivalent to the cofinal response bound
$$
\limsup_{(N,j)}
\sup_Q
{\partial\over\partial s}
\Psi_Q^{N,j}(0;\delta)
\le\mu.
$$

Proof.

Since the finite DLR space is finite-dimensional after the retained
regularization and the source is finite, differentiation under the finite
sum/integral is legitimate.  At \(s=0\),
$$
\Psi'_Q(0)
=
{\mathbf E[V_Q e^{0}]\over \mathbf E[e^0]}
=
\mathbf E[V_Q]
=
\Lambda_{bad}^{N,j}(Q;\delta).
$$
The equivalence with `P30-HKBAD-ABS` is Lemma 145.2. `square`

## 146. Source Neutrality Plus Curvature

The source-response identity by itself is only a rewrite.  Its value is that
first derivatives can sometimes be bounded by symmetry and curvature of the
source pressure.  This is the finite-law analogue of replacing an unknown
coefficient by a susceptibility.

### Definition 146.1: Heat-Bad Source Neutrality And Curvature

Fix \(a>0\), \(\rho\ge0\), and \(\chi\ge0\).

`P30-HKBAD-SRC-NEUT(a,rho)` asserts that cofinally, for every heat-bad dual
test \(Q\),
$$
\left|
\Psi_Q^{N,j}(a;\delta)
-
\Psi_Q^{N,j}(-a;\delta)
\right|
\le 2\rho.
$$

`P30-HKBAD-SRC-CURV(a,chi)` asserts that cofinally, for every heat-bad dual
test \(Q\) and every \(|s|\le a\),
$$
\left|
{\partial^2\over\partial s^2}
\Psi_Q^{N,j}(s;\delta)
\right|
\le \chi.
$$

The neutrality condition is a same-law near-evenness statement for the
source pressure.  The curvature condition is a same-law susceptibility bound
for the same source family.

### Lemma 146.2: Neutrality-Curvature Bound On The First Response

If `P30-HKBAD-SRC-NEUT(a,rho)` and
`P30-HKBAD-SRC-CURV(a,chi)` hold, then
$$
\mathrm{P30\text{-}HKBAD\text{-}ABS}
\left(\delta,{\rho\over a}+{\chi a\over2}\right)
$$
holds.

Proof.

For any fixed \(Q\), write \(\Psi=\Psi_Q^{N,j}\).  Then
$$
\Psi(a)-\Psi(-a)
=
\int_{-a}^{a}\Psi'(t)\,dt
=
2a\Psi'(0)
+
\int_{-a}^{a}(\Psi'(t)-\Psi'(0))\,dt.
$$
The curvature bound gives
$$
\left|
\int_{-a}^{a}(\Psi'(t)-\Psi'(0))\,dt
\right|
\le
\int_{-a}^{a}\chi |t|\,dt
=
\chi a^2.
$$
Therefore
$$
|\Psi'(0)|
\le
{|\Psi(a)-\Psi(-a)|\over2a}
+
{\chi a\over2}
\le
{\rho\over a}+{\chi a\over2}.
$$
Take the supremum over \(Q\), then use Lemma 145.4. `square`

### Corollary 146.3: Optimized Source-Curvature Debit

If the same \(\rho,\chi\) bounds are available over a range of \(a\), the
best debit supplied by the source-curvature route is
$$
\inf_{a>0}
\left(
{\rho(a)\over a}+{\chi(a)a\over2}
\right).
$$

In the model case of constant \(\rho,\chi\), this gives
$$
\sqrt{2\rho\chi}
$$
at
$$
a=\sqrt{2\rho/\chi}.
$$

## 147. How The Source Viewpoint Could Source The Missing Value

The new live theorem is not a conditional row table.  It is one of the
following source-response statements:
$$
\mathrm{P30\text{-}HKBAD\text{-}SRC\text{-}NEUT}(a,\rho),
$$
$$
\mathrm{P30\text{-}HKBAD\text{-}SRC\text{-}CURV}(a,\chi),
$$
or the stronger direct response bound
$$
\sup_Q
{\partial\over\partial s}
\Psi_Q^{N,j}(0;\delta)
\le\mu.
$$

The potentially useful sources for these statements are different from a
row-value computation:

1. reflection or orientation symmetry of the source pressure;
2. a Ward identity for the source derivative;
3. a convexity or log-Sobolev bound for the source pressure;
4. a Peter-Weyl tail bound for the source observable \(V_Q\);
5. a floor theorem from a sign-coherent nonzero source slope.

These are still hard, but they are not the same question as evaluating a
conditional transition kernel.  They ask whether all heat-bad probes have
small same-law response.

### Proposition 147.1: Current-Corpus Status Of The Source Route

The source-response identity is proved by the current paper, but the
neutrality and curvature estimates are not yet sourced by the current
corpus.

Proof.

Lemma 145.4 proves the exact first-response identity.  Lemma 146.2 proves
the calculus implication from source neutrality and curvature to
`P30-HKBAD-ABS`.  However, no previous section proves the required
near-evenness of \(\Psi_Q(a)-\Psi_Q(-a)\) uniformly over all heat-bad dual
tests, and no previous section proves the uniform second-derivative bound
for the actual adaptive source family.  These are new same-law quantitative
theorems. `square`

### Corollary 147.2: The New Viewpoint Has Changed The Shape Of The Problem

The original obstruction was:
$$
\text{evaluate the actual heat-bad residual/signed matrix.}
$$

The source-response obstruction is:
$$
\text{bound the first source response of all heat-bad dual probes.}
$$

This is a genuine change of viewpoint.  It does not solve the problem by
itself, but it makes the impossible quantity natural: it is the derivative
at zero of a same-law finite pressure.  The next constructive attack should
try to prove source neutrality or source curvature, rather than print more
finite labels.

### Corollary 147.3: Barandes Alignment Of The Source Viewpoint

The source-response viewpoint is Barandes-aligned.

It does not introduce:

1. a hidden Markov bridge process;
2. an auxiliary heat-kernel comparison law;
3. a replacement Yang-Mills measure;
4. an assumed stochastic dynamics inside the block.

It introduces only deterministic trace-dual probes \(Q_\Gamma\) and a
finite generating function whose derivative at zero is an actual-law
expectation.  Therefore any eventual proof of
`P30-HKBAD-SRC-NEUT` or `P30-HKBAD-SRC-CURV` would remain inside adaptive
Branch A.
