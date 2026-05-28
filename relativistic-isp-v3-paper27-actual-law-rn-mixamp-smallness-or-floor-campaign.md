# Relativistic ISP V3 Paper 27: Actual-Law RN-MIXAMP Smallness Or Lower-Floor Campaign

Author: Felix Robles Elvira

Date: 2026-05-25

## Abstract

Paper 26 reduced adaptive Branch A to the true mixed RN-amplitude table on
the same adaptive `SEL2` pushed-forward scalar law.  This paper executes the
next four attacks promised by that reduction:

1. freeze the exact RN-MIXAMP norm to be proved;
2. try to prove it by signed cancellation;
3. try to prove it by conditional spectral contraction;
4. if those fail, try to prove the same-law lower floor that would falsify
   adaptive Branch A after route failure.

The result is negative for the present corpus.  The route is not closed by a
missing finite label, quotient, or worksheet entry.  What is missing is
exactly new same-law value information: signed amplitude control, spectral
contraction plus tail, direct RN-MIXAMP domination, bridge damping plus tail,
or the lower-floor theorem
\(\overline\Lambda_{13}^{RPF}\ge M_*\).  None is supplied by Papers 20--26.
More finite labels will not move adaptive Branch A.

This is a Barandes-aligned statement: all conditionals, ratios, residual
Hamiltonians, Peter-Weyl projections, bridge amplitudes, and lower floors are
evaluated only on the actual pushed-forward finite scalar law.  No continuum
Yang-Mills measure, off-law heat kernel, hidden Markov subprocess, or
external area law is introduced.

## 0. Boundary And Imports

### Boundary 0.1: Same-Law Discipline

Throughout this paper, `actual law` means the adaptive `SEL2` finite scalar
law already fixed in Papers 21--26.  A proof may use finite conditional
probabilities, RN ratios, residual densities, Peter-Weyl coefficients, or
bridge amplitudes only if they are computed after pushing the same record law
forward to the declared local template.

The following are not admissible substitutes:

1. heat-kernel coefficients on a comparison law;
2. continuum Yang-Mills Wilson-loop estimates;
3. a Markov factorization not proved for the whole pushed-forward record law;
4. bounds for clean/non-RPF ledgers unless a same-row transfer theorem is
   printed;
5. finite-label decidability without actual numerical or analytic value
   control.

### Import 0.2: Paper-26 Endpoint

Paper 26 exports the true mixed-amplitude table
\[
        \delta_\square^{N,j}(x,y)
\]
on the minimal live `CleanRPF` edge.  Equivalently, it exports the minimal
mixed RN log-oscillation
\[
        D_{RN,0}^{N,j}(x,y)
\]
defined by the same four-point conditional RN-ratio table.  The exact
Dobrushin variation contribution of this pair is
\[
        q_{RN}^{N,j}(x,y)
        :=
        \tanh\!\left({D_{RN,0}^{N,j}(x,y)\over 4}\right).
\]

Paper 26 proves:
\[
 \mathrm{P26\text{-}RN\text{-}MIXAMP\text{-}VALUE\text{-}GAP}.
\]
That is, Papers 20--25 do not populate the cofinal mixed RN-amplitude values,
do not prove a closing smallness estimate, and do not prove the lower floor
needed to falsify adaptive Branch A.

### Import 0.3: Paper-25 Closure Gates

Paper 25 proves exact positive closure implications for adaptive Branch A:

1. a cofinal actual-law Dobrushin row \(<1\);
2. a cofinal screened shell row with enough exponential slack;
3. a same-law Peter-Weyl step contraction beating path entropy;
4. a same-law Peter-Weyl tail/projection theorem plus a passing projected
   table;
5. actual-law bridge damping plus tail control.

Paper 25 also proves that Papers 20--24 do not supply any of these five
sources, and do not supply the lower-floor theorem.

### Import 0.4: Paper-23 Signed And Bridge Budgets

Paper 23 supplies the sharp signed mixed route:
\[
 \mathrm{P23\text{-}RPF\text{-}MIN\text{-}SIGNED}(\Theta,\omega,\kappa)
\]
closes the minimal mixed branch whenever
\[
        \sinh\!\left({\Theta+\omega^2/4\over 2}\right)+\kappa
        <
        B_*^{edge}.
\]
Equivalently,
\[
        \Theta+{\omega^2\over4}
        <
        M_{sgn}(\kappa)
        :=
        2\,\operatorname{asinh}(B_*^{edge}-\kappa).
\]
Paper 23 also proves that the unsigned bridge route closes if a bridge
damping estimate and a same-law Peter-Weyl tail estimate are both supplied.
It does not prove those estimates.

## 1. The Frozen RN-MIXAMP Target Norm

### Definition 1.1: Weighted Mixed RN Row

For \(a>0\), define the weighted mixed RN row
\[
        {\mathfrak D}_{mix}^{N,j}(a)
        :=
        \sup_x
        \sum_{y\ne x}
        e^{a\,d_{RPF}(x,y)}
        q_{RN}^{N,j}(x,y).
\]

Here \(d_{RPF}\) is the same canonical RPF graph distance used in the
Paper-23/Paper-25 adaptive Dobrushin route.

### Definition 1.2: Screened Shell Upper Envelope

For a stronger shell-wise sufficient form, define the shell row
\[
        S_{mix}^{N,j}(r)
        :=
        \sup_x
        \sum_{y:\ d_{RPF}(x,y)=r}
        q_{RN}^{N,j}(x,y),
\]
and its exponential screening transform
\[
        {\mathfrak S}_{mix}^{N,j}(a)
        :=
        \sum_{r\ge1} e^{ar} S_{mix}^{N,j}(r).
\]

### Lemma 1.3: Screened Shells Dominate The Weighted Row

For every \(a>0\),
\[
        {\mathfrak D}_{mix}^{N,j}(a)
        \le
        {\mathfrak S}_{mix}^{N,j}(a).
\]

Proof.

The sum defining \({\mathfrak D}_{mix}^{N,j}(a)\) partitions the same
vertices \(y\ne x\) by the integer distance \(r=d_{RPF}(x,y)\).  For each
fixed \(x\), the \(r\)-shell contribution is bounded by
\(S_{mix}^{N,j}(r)\).  Summing those bounds and then taking the supremum over
\(x\) gives the displayed inequality.  Equality is not asserted, because the
worst shell for different \(r\)'s need not occur at the same root \(x\).
`square`

### Definition 1.4: RN-MIXAMP Smallness Source

`P27-RN-MIXAMP-SMALL(a,q)` asserts that cofinally in \(j\),
\[
        {\mathfrak D}_{mix}^{N,j}(a) \le q < 1.
\]

`P27-RN-MIXAMP-SCR(a,q)` asserts the stronger screened-shell form
\[
        {\mathfrak S}_{mix}^{N,j}(a) \le q < 1.
\]

### Theorem 1.5: Frozen Norm Closure

If `P27-RN-MIXAMP-SMALL(a,q)` holds for some \(a>0\) and \(q<1\), then
adaptive Branch A closes by the Paper-25 direct Dobrushin gate.  If the
screened upper envelope `P27-RN-MIXAMP-SCR(a,q)` holds, the same conclusion
follows.

Proof.

Paper 26 identifies \(q_{RN}^{N,j}(x,y)\) with the exact minimal live-edge
mixed conditional variation contribution.  Definition 1.1 is therefore
precisely the weighted Dobrushin row of Paper 25 for the minimal RPF
conditional kernel.  The strict bound \(q<1\) is the Paper-25 direct
Dobrushin source.  Lemma 1.3 shows that the screened-shell source implies the
same weighted-row bound. `square`

### Corollary 1.6: Entropy Accounting Is Frozen

Any later argument in this paper must prove a bound on
\({\mathfrak D}_{mix}^{N,j}(a)\) or on an explicitly stronger signed,
spectral, or bridge norm that implies it.  No additional canonical-label
entropy may be charged after Definition 1.1.

Proof.

The exponential factor \(e^{a d_{RPF}}\) and the shell sum over all \(y\ne x\)
already include the canonical RPF graph entropy.  Any further label count
would double-count the same neighbors. `square`

## 2. Attack I: Signed Cancellation

### Definition 2.1: Actual Mixed Signed Source

For \(\Theta,\omega,\kappa\ge0\), define
\[
\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}SIGN}(\Theta,\omega,\kappa)
\]
to mean that the actual same-law mixed RN-amplitude table admits a signed
decomposition whose complete two-endpoint contribution satisfies the
Paper-23 signed envelope \((\Theta,\omega)\), with remaining Peter-Weyl tail
\(\kappa\), cofinally in \(j\).

Concretely, this is not an arbitrary sign assignment.  It must be derived
from the actual Möbius/residual Hamiltonian signs of the pushed-forward
adaptive law.

### Lemma 2.2: Signed Source Would Close The Frozen Norm

Assume
\[
\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}SIGN}(\Theta,\omega,\kappa)
\]
and
\[
        \sinh\!\left({\Theta+\omega^2/4\over2}\right)+\kappa
        <
        B_*^{edge}.
\]
Then adaptive Branch A closes.

Proof.

By Definition 2.1, the actual RN-MIXAMP table satisfies the Paper-23 signed
minimal-edge source on the same scalar law.  The displayed strict inequality
is exactly the Paper-23 signed closure budget.  Paper 25 imports that minimal
signed/Dobrushin closure into adaptive Branch A. `square`

### Attempt 2.3: Can Existing Symmetry Prove The Signed Source?

Existing finite quotients, canonical labels, endpoint symmetries, and
bounded-collar reductions do not prove
\[
\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}SIGN}(\Theta,\omega,\kappa)
\]
in any closing range.

Proof.

Paper 23 already audited this route in the minimal signed sections.  The
natural quotient maps identify rows and reduce label entropy, but they do not
produce an anti-involution pairing every positive mixed bridge contribution
with a negative contribution of equal magnitude.  Paper 24 strengthens this
negative verdict at the full-object certificate level: the closed scalar body
still contains residual full-mixed witness directions.  Paper 26 then
identifies the minimal RN ratio with exactly those true mixed bridge
amplitudes.

Therefore existing symmetry supplies structural zeroes and row reductions,
not a cofinal signed value bound on the actual mixed table. `square`

### Attempt 2.4: Can Existing Finite Duality Prove The Signed Source?

The current finite dual certificates do not prove the signed source in a
closing range.

Proof.

Paper 23 prints the finite dual proof format for signed closure, but its
dual constraints are not populated by actual same-law mixed-amplitude values
or a same-law Peter-Weyl tail.  Paper 24 proves that the closed scalar body is
too large for a universal certificate in the live RPF case.  Paper 26 proves
that the missing object is not a label but the value of the true mixed
RN-amplitude table.  Hence finite duality is sound but presently not
decisive. `square`

### Theorem 2.5: Signed Cancellation Current-Corpus Verdict

The present Papers 20--26 do not prove any instance of
\[
\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}SIGN}(\Theta,\omega,\kappa)
\]
whose constants satisfy the Paper-23 signed closure inequality.

Proof.

Attempts 2.3 and 2.4 exhaust the signed mechanisms currently available in
the corpus: quotient/symmetry cancellation and finite dual certificates.
Neither supplies same-law actual mixed-amplitude values or a closing
tail-controlled signed envelope. `square`

We record this as
\[
\boxed{\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}SIGN\text{-}GAP}.}
\]

## 3. Attack II: Conditional Spectral Contraction

### Definition 3.1: Actual Conditional Spectral Source

For a finite Peter-Weyl cutoff \(L\), let
\[
        T_{e,\zeta}^{N,j,L}
        :=
        \Pi_{\le L} T_{e,\zeta}^{N,j}\Pi_{\le L}
\]
be the actual same-law conditional transfer matrix on the declared adaptive
template, as in Papers 25--26.

`P27-RN-MIXAMP-SPEC(L,\theta,\kappa)` asserts that cofinally:

1. the centered projected operator has norm at most \(\theta\);
2. the omitted Peter-Weyl complement contributes at most \(\kappa\);
3. the resulting \(\theta+\kappa\) beats the Paper-25 path-entropy budget.

### Lemma 3.2: Spectral Source Would Close RN-MIXAMP

If `P27-RN-MIXAMP-SPEC(L,\theta,\kappa)` holds with the Paper-25 strict
margin, then adaptive Branch A closes.

Proof.

This is the Paper-25 Peter-Weyl step/tail route applied to the same
conditional RN-MIXAMP kernel isolated in Paper 26.  The finite projected
operator controls the low modes, while the tail term controls the omitted
complement.  The strict path-entropy margin gives the same weighted
Dobrushin contraction as Definition 1.1. `square`

### Attempt 3.3: The Existing Peter-Weyl Tables Are Not Spectral Values

The finite Peter-Weyl row tables in Papers 23--26 do not prove
`P27-RN-MIXAMP-SPEC(L,\theta,\kappa)` in a closing range.

Proof.

Paper 23 proves that Peter-Weyl truncation is legitimate only when paired
with a same-law tail theorem.  It explicitly separates finite projected
matrices from \(KTAIL\), \(PWBAND\), and \(PWDECAY\).  Paper 25 repeats this
at the actual-law level: the projected step route is sound, but the current
corpus has no cofinal spectral gap and no cofinal Peter-Weyl tail estimate
for the actual adaptive residual law.  Paper 26 identifies the minimal live
RN table but does not populate the entries or the projected operator norms.

Thus existing tables are formats for a computation, not a proof of
conditional spectral contraction. `square`

### Attempt 3.4: Can Clean Heat-Kernel Decay Transfer To The Actual Table?

Clean heat-kernel or non-RPF decay estimates do not imply the conditional
spectral source for RN-MIXAMP.

Proof.

The adaptive RN-MIXAMP table is a ratio of actual conditional probabilities
after residual RPF conditioning.  Paper 26 unwinds the residual density as
\[
        H_{RPF}^{N,j}
        =
        \log Z+\log p-\sum_p\log K_p^{CE}.
\]
Without a same-law transfer theorem for this residual density, heat-kernel
decay on a comparison law, clean KP decay, or non-RPF finite ledgers do not
bound the spectral radius of \(T_{e,\zeta}^{N,j,L}\) or its tail.  Importing
those estimates directly would change the law. `square`

### Theorem 3.5: Spectral Contraction Current-Corpus Verdict

The present Papers 20--26 do not prove
`P27-RN-MIXAMP-SPEC(L,\theta,\kappa)` in a range that closes adaptive Branch
A.

Proof.

Attempts 3.3 and 3.4 cover the only spectral information currently available:
finite projected formats and comparison-law heat-kernel/clean estimates.
Neither gives the same-law projected norm plus tail bound required by
Definition 3.1. `square`

We record this as
\[
\boxed{\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}SPEC\text{-}GAP}.}
\]

## 4. Attack III: Direct Smallness

### Definition 4.1: Direct Row Smallness Source

`P27-RN-MIXAMP-DIRECT(a,q)` is the assertion
\[
        \limsup_{j\to\infty}{\mathfrak D}_{mix}^{N,j}(a)\le q<1
\]
for the actual adaptive `SEL2` law and some fixed \(a>0\).

This is the most literal form of `P27-RN-MIXAMP-SMALL`.

### Lemma 4.2: Direct Smallness Is Equivalent To A Populated RN-MIXAMP Row

`P27-RN-MIXAMP-DIRECT(a,q)` can be proved by a cofinal table of the values
\[
        D_{RN,0}^{N,j}(x,y)
\]
or by any same-law analytic upper bound on those values whose weighted row
sum is \(<1\).

Proof.

By Definition 1.1, the row is a finite sum for each fixed local template and
a cofinal supremum in the adaptive limit.  The entries enter only through
\(\tanh(D_{RN,0}^{N,j}(x,y)/4)\).  Therefore actual entries or a same-law
analytic domination of them decides the row. `square`

### Attempt 4.3: Existing Structural Zeroes Are Insufficient

The structural zero table from Papers 23 and 26 does not prove direct
smallness.

Proof.

Paper 26 exhausts the zero classes and identifies the remaining live entries
with true mixed `CleanRPF`/bridge amplitudes.  A zero classification removes
terms but gives no upper bound on nonzero terms.  Since the direct row is a
positive weighted sum, every surviving live entry must be bounded or canceled
by a different signed theorem.  No such value table is supplied. `square`

### Attempt 4.4: Existing Bridge Damping Is Not Available

The bridge route does not presently prove direct smallness.

Proof.

Paper 23 and Paper 25 both prove that bridge damping plus same-law tail
control would close the branch.  They also prove that the current corpus does
not supply actual-law bridge damping in the closing range and does not supply
the needed Peter-Weyl tail.  Paper 26 identifies the RN-MIXAMP entries with
the true bridge amplitudes, but does not bound them.  Thus bridge damping is
an admissible future proof route, not a current proof. `square`

### Theorem 4.5: Direct Smallness Current-Corpus Verdict

The present Papers 20--26 do not prove
`P27-RN-MIXAMP-DIRECT(a,q)` for any closing \(a>0\), \(q<1\).

Proof.

By Lemma 4.2, direct smallness needs cofinal actual values or a same-law
analytic domination of the live mixed RN entries.  Attempts 4.3 and 4.4 show
that the current zero and bridge ledgers supply neither.  The same conclusion
was isolated in Paper 26 as `P26-RN-MIXAMP-VALUE-GAP`. `square`

We record this as
\[
\boxed{\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}SMALL\text{-}GAP}.}
\]

## 5. Attack IV: Same-Law Lower Floor

### Definition 5.1: RN-MIXAMP Lower-Floor Source

`P27-RN-MIXAMP-FLOOR` asserts the same-law lower floor
\[
        \overline\Lambda_{13}^{RPF}\ge M_*,
\]
or an equivalent lower floor strong enough to imply that adaptive Branch A
cannot close after the RN-MIXAMP route fails.

### Lemma 5.2: Lower Floor Would Falsify Adaptive Branch A After Route Failure

If the RN-MIXAMP smallness/signed/spectral/bridge routes fail and
`P27-RN-MIXAMP-FLOOR` holds, then adaptive Branch A is falsified.

Proof.

This is the lower-floor alternative already isolated in Papers 23, 25, and
26.  Route failure alone proves only non-closure of a sufficient test.  The
same-law lower floor is what turns non-closure into a Branch-A falsification
by forcing the actual RPF predebit to reach the loss threshold \(M_*\).
`square`

### Attempt 5.3: Existing Papers Do Not Prove The Lower Floor

The present corpus does not prove `P27-RN-MIXAMP-FLOOR`.

Proof.

Paper 25 explicitly separates truth-status failure of a route from a
lower-floor theorem and proves that Papers 20--24 supply no such floor.
Paper 26 repeats the issue after identifying RN-MIXAMP as the sharp minimal
mixed table: it proves that current values are unpopulated and that neither
smallness nor the floor is decided.  Finite labels, quotient reductions,
structural zeroes, and clean ledgers do not imply a positive lower bound on
the actual residual RPF predebit. `square`

### Theorem 5.4: Lower-Floor Current-Corpus Verdict

The present Papers 20--26 do not prove
\[
        \overline\Lambda_{13}^{RPF}\ge M_*.
\]

Proof.

This is Attempt 5.3 restated in the exact lower-floor notation of Definition
5.1. `square`

We record this as
\[
\boxed{\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}FLOOR\text{-}GAP}.}
\]

## 6. Final Branch-A Attempt Verdict

### Theorem 6.1: Paper-27 Four-Route Verdict

The four requested attacks do not prove adaptive Branch A from the present
corpus:
\[
\begin{gathered}
\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}SIGN\text{-}GAP},\\
\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}SPEC\text{-}GAP},\\
\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}SMALL\text{-}GAP},\\
\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}FLOOR\text{-}GAP}.
\end{gathered}
\]

Consequently, adaptive Branch A is not closed and not falsified by Papers
20--26 plus the four attempted continuations in this paper.

Proof.

Sections 2--5 prove the four gaps.  Each gap is same-law: it concerns the
actual adaptive `SEL2` pushed-forward scalar law and the actual RN-MIXAMP
table identified in Paper 26.  Since neither a closing upper bound nor a
falsifying lower floor is proved, the branch remains undecided by the present
corpus. `square`

### Corollary 6.2: Sharp Next Theorem

The next positive theorem must be one of the following genuinely new same-law
sources:

1. a signed mixed-amplitude theorem in the range
   \[
   \Theta+\omega^2/4 < 2\,\operatorname{asinh}(B_*^{edge}-\kappa);
   \]
2. a conditional spectral contraction plus a same-law Peter-Weyl tail;
3. direct RN-MIXAMP row values or a same-law analytic domination giving
   \({\mathfrak D}_{mix}^{N,j}(a)<1\);
4. actual-law bridge damping plus tail control;
5. the lower floor \(\overline\Lambda_{13}^{RPF}\ge M_*\);
6. or a strategic exit from adaptive Branch A to Branch B or Branch C.

No further finite-label, quotient, or worksheet refinement can substitute
for one of these value theorems.

### Corollary 6.3: No Further Finite-Label Movement

Adaptive Branch A has passed beyond the finite-label stage.  The next real
theorem has to be new same-law value information:
\[
\boxed{
\begin{array}{c}
\text{signed amplitude control,}\\
\text{spectral contraction plus tail,}\\
\text{direct RN-MIXAMP domination,}\\
\text{bridge damping plus tail,}\\
\text{or the lower floor }\overline\Lambda_{13}^{RPF}\ge M_*.
\end{array}}
\]
More finite labels will not move it.

Proof.

Papers 23--26 already print the finite carriers, canonical row maps,
structural zeroes, residual atom formulas, conditional density identities,
and the RN-MIXAMP table to the point where every surviving obstruction is a
value obstruction.  Theorem 6.1 then checks all four Paper-27 continuations:
signed, spectral, direct smallness, and lower floor.  Each fails only because
the actual same-law values are not supplied.  Adding another label, quotient,
or worksheet coordinate would refine the representation of the same
unknowns, not bound them. `square`

### Corollary 6.4: Best Current Recommendation

Within Branch A, the highest-leverage remaining route is the signed or
spectral route, not another structural finite table.  The reason is simple:
direct positive row smallness needs all live mixed amplitudes, whereas a
signed or spectral theorem could exploit cancellations or operator
contraction before absolute values are taken.  But it must still be a theorem
about the same adaptive pushed-forward scalar law.

This completes Paper 27.
