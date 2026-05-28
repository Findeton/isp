# Relativistic ISP V3 Paper 24: Full-Object RPF Dual Certificate Campaign For Adaptive Branch A

Author: Felix Robles Elvira

Status: completed certificate-body verdict.  The full-object finite-dual
certificate over the closed Paper-23 body \({\mathcal M}_{56}\) is not the
missing positive source unless the live RPF mixed direction is already zero;
in the nontrivial live case, \({\mathcal M}_{56}\) contains same-law witnesses
against every closing pair.  The next positive theorem must therefore add new
actual-law scalar information, not another certificate over the old closed
body.

Paper 23 froze the adaptive Branch-A reduction.  After all closed surface,
activity, RP/Cov, exact-entry, local, endpoint, canonical-label, bridge,
Peter-Weyl, and full-object bookkeeping is spent, the most direct remaining
positive theorem is:

```math
\mathrm{P23\text{-}RPF\text{-}MIN\text{-}SIGNED\text{-}FULL}
(\Theta,\omega)
```

or the finite-dual proof format

```math
\mathrm{P23\text{-}RPF\text{-}MIN\text{-}SIGNED\text{-}FULL\text{-}DUAL}
(\Theta,\omega),
```

with

```math
\sinh((\Theta+\omega^2/4)/2)<B_*^{edge}.
```

Paper 24 executes the binary task: either print a finite same-law certificate
for such a closing pair \((\Theta,\omega)\), or print a same-law witness
showing that the closed Paper-23 constraints cannot certify such a pair.

## 0. Barandes-Aligned Boundary

The primitive object is still the whole-process pushed-forward finite scalar
law.  Paper 24 does not introduce:

1. a continuum Yang-Mills measure with confinement already built in;
2. a Wilson-loop area law;
3. a mass gap;
4. an off-record heat-kernel subprocess;
5. a gauge-fixed Markov kernel;
6. an ontic flux-tube or sheet picture.

Every variable in the certificate body is a finite scalar record variable
already licensed by Papers 20--23.  Gauge, group, Peter-Weyl, and polymer
language is bookkeeping for scalar inequalities on that law.

## 1. Paper-23 Import Contract

### Definition 1.1: Imported Closed Scalar Body

For each adaptive row \((N,j)\), import the compact scalar record body
\({\mathcal M}_{56}^{N,j}\) from Paper 23 Section 56.  It consists of all
finite pushed-forward scalar laws satisfying:

1. normalization and positivity;
2. declared centrality, covariance, conjugation, quotient, and reflection
   equalities;
3. exact `BC/CE` and central-entry identities retained on the branch;
4. local, endpoint-blind, and endpoint-additive removals already proved in
   Paper 23;
5. closed surface/activity and RP/Cov ledgers assigned outside the live RPF
   source;
6. the exact finite row formula for the full normalized minimal-edge
   Hamiltonian \(C_0^{m,N,j}\);
7. no Peter-Weyl truncation source and no full signed-range bound as an input.

The actual adaptive pushed-forward scalar law is an element of
\({\mathcal M}_{56}^{N,j}\).  A Paper-24 certificate must hold on this whole
body or on a justified cofinal subbody defined by additional same-law scalar
equalities.

### Definition 1.2: Full-Object Gate Functional

For constants \(\Theta,\omega\ge0\), define the full-object gate

```math
{\mathcal G}_{full}(\Theta,\omega)
:=
\sinh((\Theta+\omega^2/4)/2).
```

The closing region is

```math
{\mathcal G}_{full}(\Theta,\omega)<B_*^{edge}.
```

### Definition 1.3: `P24-RPF-FULL-DUAL-CERT(Theta,omega)`

`P24-RPF-FULL-DUAL-CERT(Theta,omega)` asserts that, cofinally, every
universal full-object signed inequality over \({\mathcal M}_{56}^{N,j}\) has
a finite same-law certificate.  Equivalently, it supplies

```math
\mathrm{P23\text{-}RPF\text{-}MIN\text{-}SIGNED\text{-}FULL\text{-}DUAL}
(\Theta,\omega).
```

The certificate may use closed Paper-23 equalities and inequalities, but it
may not use the target full signed-range inequality as an input.

### Theorem 1.4: Certificate Closure Import

If `P24-RPF-FULL-DUAL-CERT(Theta,omega)` holds and

```math
{\mathcal G}_{full}(\Theta,\omega)<B_*^{edge},
```

then `P23-RPF-TRANS0` holds.

Proof.

By Definition 1.3, the Paper-24 certificate is exactly the Paper-23
full-object finite-dual source.  Paper 23 Corollary 56.5 then closes
`P23-RPF-TRANS0`. `square`

## 2. Witness Alternative

### Definition 2.1: Rowwise Full-Dual Witness

For a proposed pair \((\Theta,\omega)\),
`P24-RPF-FULL-DUAL-WIT(Theta,omega)` asserts that, cofinally, there is a law
\(\mu_{N,j}\in{\mathcal M}_{56}^{N,j}\) and endpoint/environment records for
which at least one target inequality fails:

```math
(C_0^m)^{dc}(u,v;\zeta)-(C_0^m)^{dc}(u',v';\zeta)>\Theta,
```

or one of the one-line inequalities has oscillation \(>\omega\).

The witness is same-law in the certification sense: it lives in the same
closed scalar record body.  It is not claimed to be the actual adaptive law
unless explicitly proved.

### Lemma 2.2: Witness Refutes A Universal Certificate

If `P24-RPF-FULL-DUAL-WIT(Theta,omega)` holds, then
`P24-RPF-FULL-DUAL-CERT(Theta,omega)` cannot be derived from the closed
constraints defining \({\mathcal M}_{56}^{N,j}\).

Proof.

A universal certificate over \({\mathcal M}_{56}^{N,j}\) would prove the
target inequalities for every law in that body.  The witness supplies a law
in the body violating one of the inequalities. `square`

### Definition 2.3: Closing-Region Witness Program

`P24-RPF-FULL-DUAL-WIT-CLOSE` asserts that every pair
\((\Theta,\omega)\) in the closing region
\({\mathcal G}_{full}(\Theta,\omega)<B_*^{edge}\) is refuted by a rowwise
full-dual witness or by a cofinal lower-floor theorem for the actual
adaptive law.

This is the negative terminal theorem for the full-object certificate route.
It is stronger than Paper 23's current-corpus no-go, because it rules out
not just the printed corpus but the entire closed scalar body for every
closing pair.

## 3. Finite Certificate Worksheet

### Definition 3.1: Target Inequality Rows

For each finite adaptive row, define the target family
\({\mathcal I}_{full}^{N,j}(\Theta,\omega)\) as the finite list consisting of:

1. all doubly centered endpoint differences

   ```math
   (C_0^m)^{dc}(u,v;\zeta)-(C_0^m)^{dc}(u',v';\zeta)\le\Theta;
   ```

2. their reversed inequalities;
3. all one-line endpoint oscillation inequalities in \(u\) and in \(v\),
   bounded by \(\omega\).

The list is finite for each row because all endpoint and environment records
are finite scalar records after the Paper-23 reductions.

### Definition 3.2: Admissible Certificate Form

An admissible certificate for a target inequality \(I\le0\) is a finite
identity or dual inequality of the form

```math
-I
=
\sum_a \lambda_a E_a
+
\sum_b \gamma_b P_b
+
R,
```

where:

1. \(E_a=0\) are closed same-law scalar equalities;
2. \(P_b\ge0\) are closed same-law scalar inequalities, with
   \(\gamma_b\ge0\);
3. \(R\ge0\) is a finite analytic remainder proved nonnegative on
   \({\mathcal M}_{56}^{N,j}\);
4. all coefficients are finite scalar functions of the row data;
5. no term is the target inequality or an unsourced RPF range bound.

This format is deliberately broad enough to include linear programming,
semialgebraic, convex-dual, and analytic multiplier certificates.

### Proposition 3.3: Certificate Soundness

Every admissible certificate proves its target inequality on
\({\mathcal M}_{56}^{N,j}\).

Proof.

On \({\mathcal M}_{56}^{N,j}\), each equality term \(E_a\) vanishes, each
\(\gamma_bP_b\) is nonnegative, and \(R\) is nonnegative.  Hence \(-I\ge0\),
so \(I\le0\). `square`

### Definition 3.4: Paper-24 Primary Search Problem

For a chosen closing pair \((\Theta,\omega)\), the primary search problem is:

```math
\forall I\in{\mathcal I}_{full}^{N,j}(\Theta,\omega),
\quad
\text{print an admissible certificate for } I\le0
```

cofinally in the adaptive row.

If this succeeds, Theorem 1.4 closes adaptive Branch A's RPF source.  If it
fails by a witness in the sense of Section 2, the full-object route is
falsified for that pair.

## 4. Work Packages

The campaign is organized in this order; Sections 6--12 execute these items.

1. **Freeze the certificate alphabet.** List the exact equality and
   inequality rows admitted from Paper 23 into \({\mathcal M}_{56}\).
2. **Choose the first gate pair.** Start with the strongest plausible
   full-object pair, then relax only while staying inside
   \({\mathcal G}_{full}<B_*^{edge}\).
3. **Build the finite row dual.** Translate each target row in
   \({\mathcal I}_{full}\) into the admissible certificate form.
4. **Search for a certificate.** Try equality reductions first, then
   RP/positivity multipliers, then analytic finite remainders.
5. **If the certificate fails, print the witness.** A witness must live in
   \({\mathcal M}_{56}\) and must identify which target inequality fails.
6. **Export the verdict.** A certificate closes adaptive Branch A's RPF
   source; a closing-region witness theorem falsifies the full-object route
   and sends the program back to tail sourcing, bridge damping, or upstream
   screened conditional influence.

## 5. Initial Verdict

Paper 24 begins from a precise finite problem, not from a new physical
assumption.  The live question is:

```math
\boxed{
\mathrm{P24\text{-}RPF\text{-}FULL\text{-}DUAL\text{-}CERT}
(\Theta,\omega)
\quad\text{for some}\quad
{\mathcal G}_{full}(\Theta,\omega)<B_*^{edge}
}
```

or else a same-law witness theorem showing why such a certificate cannot be
obtained from \({\mathcal M}_{56}\).  Sections 6--12 settle that obstruction
as a negative certificate-body theorem in the nontrivial live RPF case.

## 6. Certificate Alphabet Freeze

The first work package is to decide exactly what a Paper-24 certificate may
use.  The answer is deliberately conservative: it may use all closed
Paper-23 scalar information, and nothing that is equivalent to the target
full signed-range estimate.

### Definition 6.1: Equality Alphabet

Let \({\mathsf E}_{56}^{N,j}\) be the finite list of equality rows in
\({\mathcal M}_{56}^{N,j}\).  It consists of:

1. normalization of the finite scalar law;
2. centrality, covariance, conjugation, reflection, and quotient equalities;
3. exact `BC/CE` identities retained on the branch;
4. central-entry/readout equalities already fixed before RPF;
5. deterministic anchor-gauge equalities removing endpoint-additive parts;
6. the exact finite formula defining \(C_0^{m,N,j}\) from the scalar records.

No equality row may assert a value bound on \(C_0^m\), on a bridge amplitude,
or on a Peter-Weyl tail.

### Definition 6.2: Inequality Alphabet

Let \({\mathsf P}_{56}^{N,j}\) be the finite list of inequality rows in
\({\mathcal M}_{56}^{N,j}\).  It consists of:

1. positivity of probabilities and finite densities;
2. printed RP/positivity inequalities imported from the closed RP/Cov ledger;
3. closed surface/activity inequalities already assigned outside the RPF
   source;
4. no-double-charge local, endpoint-blind, and endpoint-additive removals;
5. finite row-admissibility constraints defining the adaptive branch.

No inequality row may be a full signed-range bound, a bridge-damping bound,
a `MIN-KTAIL` bound, a screened conditional influence bound, or a Dobrushin
row bound.

### Lemma 6.3: Alphabet Soundness

Every certificate built from \({\mathsf E}_{56}^{N,j}\) and
\({\mathsf P}_{56}^{N,j}\) in the admissible form of Definition 3.2 is a
same-law certificate over \({\mathcal M}_{56}^{N,j}\).

Proof.

This is Proposition 3.3 with the alphabet now fixed.  Each equality is true
on \({\mathcal M}_{56}^{N,j}\), each inequality is nonnegative there, and no
target RPF range statement is smuggled into the certificate. `square`

### Proposition 6.4: Alphabet Completeness For The Closed Body

The alphabet \({\mathsf E}_{56}^{N,j}\cup{\mathsf P}_{56}^{N,j}\) contains
all current-corpus information licensed for a full-object Paper-24
certificate over \({\mathcal M}_{56}^{N,j}\).

Proof.

Paper 23 Section 57 proves that endpoint/corner geometry, activity counting,
RP/Cov transport, local and endpoint removals, central-entry exactness,
declared covariance/quotient equalities, finite labels, Paper-16 clean KP,
Peter-Weyl truncation, and heat-kernel/Casimir estimates have all either been
spent in the closed body or identified as new sources.  Definitions 6.1 and
6.2 include the spent parts and exclude the new sources.  Therefore any
further certificate over the same closed body must be built from this
alphabet. `square`

## 7. Full-Object Gate Geometry

Before searching for certificates, the scalar gate should be put in its
sharpest form.

### Definition 7.1: Full Signed Radius

Define

```math
R_*^{full}:=2\,\operatorname{arsinh}(B_*^{edge}).
```

The closing region is

```math
\Theta+\omega^2/4<R_*^{full}.
```

### Lemma 7.2: Equivalent Gate

For \(\Theta,\omega\ge0\),

```math
\sinh((\Theta+\omega^2/4)/2)<B_*^{edge}
```

is equivalent to

```math
\Theta+\omega^2/4<R_*^{full}.
```

Proof.

The hyperbolic sine is strictly increasing on \([0,\infty)\).  Apply
\(\operatorname{arsinh}\) and multiply by \(2\). `square`

### Corollary 7.3: Every Closing Pair Has A Finite Cap

Every closing pair satisfies

```math
\Theta<R_*^{full},
\qquad
\omega<2\sqrt{R_*^{full}}.
```

Thus a witness with arbitrarily large doubly centered range or one-line
width refutes every possible closing pair at once.

## 8. Residual-Tail Directions Inside The Closed Body

The crucial question is whether \({\mathcal M}_{56}\) still contains a live
direction that changes the full mixed range while preserving all closed
constraints.  Paper 23's residual-tail no-go arguments say yes in the
nontrivial live RPF case.

### Definition 8.1: Admissible Full-Mixed Direction

An admissible full-mixed direction is a finite scalar perturbation
\(H^{N,j}\) of the residual log-density such that:

1. \(H^{N,j}\) preserves all equality rows in \({\mathsf E}_{56}^{N,j}\);
2. for every finite \(t\) in a nonempty interval, the tilted scalar law
   obtained by replacing the residual factor by \(e^{tH^{N,j}}\) and
   renormalizing still satisfies \({\mathsf P}_{56}^{N,j}\);
3. \(H^{N,j}\) is local/endpoint-additive-free after the Paper-23 anchor
   gauge;
4. either \((H^{N,j})^{dc}\) has nonzero endpoint oscillation or \(H^{N,j}\)
   has nonzero one-line endpoint width.

If the interval of admissible \(t\)'s is unbounded above, call the direction
unbounded.  If it is merely nontrivial but bounded, call it bounded-live.

### Lemma 8.2: Paper-23 Residual-Tail Import

In the nontrivial live RPF case, Paper 23 imports an admissible full-mixed
direction not fixed by the closed non-RPF ledgers.

Proof.

Paper 23 Sections 28--33 construct arbitrary-order residual-tail completions
that preserve the already closed non-RPF source package.  Sections 47--56
reuse the same family after the minimal-edge and true-bridge reductions:
finite labels, endpoint-additive removals, equality quotients, RP/Cov
carries, and surface/activity ledgers remain fixed while a surviving
true-bridge mixed mode changes.  That is exactly an admissible full-mixed
direction in the sense of Definition 8.1. `square`

### Lemma 8.3: Zero Direction Alternative

If no admissible full-mixed direction exists cofinally, then the live RPF
mixed source is already zero on the closed body, and
`P23-RPF-MIN-SIGNED-FULL(0,0)` holds.

Proof.

The only rows left after Paper 23's local, endpoint-blind, and
endpoint-additive removals are the true mixed RPF rows.  If the closed body
admits no direction changing the full mixed conditional Hamiltonian, then
the full doubly centered and one-line endpoint variations are identically
zero on that body.  This is precisely `SIGNED-FULL(0,0)`. `square`

## 9. Witness Construction

### Lemma 9.1: Unbounded Direction Witnesses Every Closing Pair

Assume an unbounded admissible full-mixed direction \(H^{N,j}\) exists
cofinally.  Then for every \((\Theta,\omega)\) in the closing region,
`P24-RPF-FULL-DUAL-WIT(Theta,omega)` holds.

Proof.

By Definition 8.1, either the doubly centered oscillation of \(H^{N,j}\) is
positive or a one-line oscillation is positive.  Along the tilted family
\(e^{tH^{N,j}}\), the corresponding full-object Hamiltonian difference grows
linearly in \(t\), while all closed constraints remain satisfied by
admissibility.  Since \(t\) is unbounded above, choose \(t\) so the relevant
oscillation exceeds the finite cap from Corollary 7.3.  The resulting law is
in \({\mathcal M}_{56}^{N,j}\) and violates one target inequality. `square`

### Lemma 9.2: Bounded-Live Direction Still Blocks Universal Small Gates

Assume a bounded-live admissible full-mixed direction exists with attainable
full-object oscillation floor \(r_{live}^{N,j}>0\).  Then every proposed
closing pair satisfying

```math
\Theta<r_{live}^{N,j}
```

or

```math
\omega<r_{live}^{N,j}
```

on the corresponding active endpoint line is refuted by a rowwise witness.

Proof.

Use the endpoint records supplied by Definition 8.1 and choose an admissible
tilt attaining the floor.  The target inequality with a smaller proposed
constant fails inside \({\mathcal M}_{56}^{N,j}\). `square`

### Definition 9.3: Closing-Region Witness Body

`P24-RPF-FULL-WIT-CLOSE` asserts that the unbounded direction of Lemma 9.1
exists cofinally, or that the bounded-live floors of Lemma 9.2 exceed the
whole closing cap \(R_*^{full}\) in the relevant endpoint channel.

### Theorem 9.4: Witness-Body No-Certificate Theorem

If `P24-RPF-FULL-WIT-CLOSE` holds, then no
`P24-RPF-FULL-DUAL-CERT(Theta,omega)` exists for any pair in the closing
region.

Proof.

For every closing pair, Definition 9.3 supplies a rowwise witness in
\({\mathcal M}_{56}^{N,j}\).  Lemma 2.2 says such a witness refutes any
universal certificate over that body. `square`

## 10. The Closed-Body Dichotomy

The certificate campaign has therefore become a dichotomy.

### Theorem 10.1: Full-Object Closed-Body Dichotomy

Exactly one of the following is needed for the closed Paper-23 body:

1. the zero-direction alternative holds cofinally, in which case
   `P23-RPF-MIN-SIGNED-FULL(0,0)` closes adaptive Branch A;
2. a same-law source narrows \({\mathcal M}_{56}\) by adding genuine
   numerical information about the actual adaptive law;
3. the residual-tail witness body holds, in which case no full-object finite
   dual certificate over \({\mathcal M}_{56}\) can close the branch.

Proof.

If no admissible mixed direction exists, Lemma 8.3 gives alternative 1.  If
the actual law is further constrained by a new same-law scalar theorem, then
the certificate body is no longer \({\mathcal M}_{56}\), giving alternative
2.  If the Paper-23 residual-tail freedom remains present inside
\({\mathcal M}_{56}\), Lemmas 9.1--9.2 and Theorem 9.4 give alternative 3.
These exhaust the possibilities for a universal certificate over the closed
body. `square`

### Corollary 10.2: Current Paper-24 Verdict

On the nontrivial live RPF branch studied by Papers 23--24, the full-object
dual certificate over \({\mathcal M}_{56}\) does not close adaptive Branch A.

Proof.

The nontrivial live branch is precisely the branch in which the zero-direction
alternative has not already closed RPF.  Paper 23's residual-tail import
then gives a live admissible full-mixed direction by Lemma 8.2.  Without a
new same-law scalar theorem narrowing \({\mathcal M}_{56}\), the certificate
body remains too large.  Hence a universal full-object certificate over that
body is refuted by the witness dichotomy. `square`

## 11. Projection/Tail Split As A Diagnostic Only

The user-facing temptation is to project the full object and estimate a tail.
This is useful as a scout but cannot be the completed full-object proof.

### Definition 11.1: Projected Full-Object Scout

For a cutoff \(L\), define projected full-object values

```math
\Theta_L^{full}
:=
\operatorname{osc}_{dc}(\Pi_{\le L}^{xy}C_0^m),
\qquad
\omega_L^{full}
:=
\operatorname{osc}_{line}(\Pi_{\le L}^{xy}C_0^m),
```

and tail size

```math
\kappa_L^{full}
:=
\|(I-\Pi_{\le L}^{xy})C_0^m\|_{\mathrm{edge}}.
```

### Lemma 11.2: Projection Scout Reintroduces `MIN-KTAIL`

Any proof based on
\(\Pi_{\le L}^{xy}C_0^m+(I-\Pi_{\le L}^{xy})C_0^m\) closes only if it also
supplies a cofinal bound on \(\kappa_L^{full}\).

Proof.

The projected term can be handled by finite spectral algebra for fixed \(L\).
The unprojected remainder is exactly a Peter-Weyl tail of the same full
Hamiltonian.  A cofinal bound on that remainder is `MIN-KTAIL` in the
minimal-edge normalization. `square`

### Corollary 11.3: Projection Scout Verdict

Projection/tail splitting is useful for estimating how much slack a future
tail theorem would need.  It is not a proof of
`P24-RPF-FULL-DUAL-CERT` over \({\mathcal M}_{56}\).  If pursued, it returns
the program to the Paper-23 Section-55 alternatives:

1. exact finite-band support;
2. uniform Peter-Weyl decay;
3. an explicit cofinal numerical tail table.

## 12. Paper-24 Terminal Verdict

### Theorem 12.1: Paper-24 Completion Theorem

Paper 24 settles the full-object finite-dual certificate campaign over the
closed Paper-23 body \({\mathcal M}_{56}\):

1. the certificate format is sound;
2. a closing certificate would close adaptive Branch A's RPF source;
3. in the nontrivial live RPF case, the closed body still contains residual
   full-mixed freedom;
4. therefore \({\mathcal M}_{56}\) is too large for a closing universal
   full-object certificate unless a new same-law scalar theorem narrows it.

Proof.

Items 1 and 2 are Proposition 3.3 and Theorem 1.4.  Item 3 is the Paper-23
residual-tail import, formalized in Lemma 8.2.  Item 4 is the closed-body
dichotomy of Theorem 10.1 and the current Paper-24 verdict of Corollary
10.2. `square`

### Corollary 12.2: Export After Paper 24

The next positive proof cannot be another certificate over
\({\mathcal M}_{56}\).  It must do at least one of the following:

1. add new actual-law scalar information narrowing the certificate body;
2. prove a cofinal Peter-Weyl tail source (`PWBAND`, `PWDECAY`, or a tail
   table);
3. prove a bridge-damping theorem on the actual law;
4. prove screened conditional influence or a direct Dobrushin row;
5. return to the parked Branch-B or Branch-C alternatives from Paper 22.

Thus Paper 24 is finished as a negative certificate-body theorem: it does not
prove confinement, but it prevents the program from spending more effort on
the wrong universal dual body.
