# Relativistic ISP V3 Paper 29: RN-MIXAMP Low-Mode Value Extraction And Spectral Gap Attempt

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Date: 2026-05-25

## Abstract

Paper 28 proved that the RN-MIXAMP spectral route is no longer a question of
defining a finite operator.  The operator exists.  The remaining issue is
value extraction:
\[
        \Theta^{act}[L]+\kappa^{act}[L]
        <
        \theta_{\mathrm{crit}}.
\]
This paper executes the next five tasks:

1. freeze the smallest nontrivial low-mode spectral target;
2. write the actual low-mode matrix entries in terms of the same-law
   residual density \(H_{RPF}^{N,j}\);
3. try to source a strict low-mode gap \(\Theta^{act}[L]<1\), preferably in
   a range that beats \(\theta_{\mathrm{crit}}\);
4. audit the tail only after the low-mode slack is inspected;
5. if the low-mode value source is unavailable, pivot to the signed/bridge
   routes rather than adding more finite labels.

It then completes the continuation forced by Task 5: define the primitive
residual value theorem that would populate the missing low-mode entries, test
the direct density, residual row-identity, and same-law polymer-value source
routes already present in the corpus, and record the final spectral
value-extraction closure label.

The central finding is sharper than Paper 28.  The four-point RN-MIXAMP
ratio table is not enough to reconstruct the spectral low-mode transition
matrix.  Four-point ratios cancel endpoint-additive one-site terms; the
actual conditional transfer kernel does not.  Therefore the spectral route
needs strictly more same-law value information than RN-MIXAMP smallness:
actual conditional weights or a primitive residual density source strong
enough to recover them.

The present corpus supplies no such values, no same-law Doeblin floor, no
strict low-mode spectral gap, and no Peter-Weyl tail source.  Thus Paper 29
does not close adaptive Branch A.  It closes the spectral value-extraction
attempt as a current-corpus gap and recommends either a genuinely new
primitive residual/conditional value theorem, or a pivot to signed/bridge
amplitude control.

## 0. Imports And Target Convention

### Import 0.1: Paper-28 Spectral-Tail Gate

Paper 28 defines
\[
        \Theta^{act}[L]
        =
        \limsup_{(N,j)}
        \sup_{e,\zeta}
        \left\|
        \Pi_{\le L}^{xy}T_{e,\zeta,\circ}^{N,j}\Pi_{\le L}^{xy}
        \right\|_{edge}
\]
and
\[
        \kappa^{act}[L]
        =
        \limsup_{(N,j)}
        \sup_{e,\zeta}
        \left\|
        (I-\Pi_{\le L}^{xy})C_{RN}^{N,j}(e,\zeta)
        \right\|_{edge}.
\]
The spectral route closes adaptive Branch A if
\[
        \Theta^{act}[L]+\kappa^{act}[L]
        <
        \theta_{\mathrm{crit}},
\]
where
\[
        0<\theta_{\mathrm{crit}}<1
\]
is the Paper-25 step-contraction margin.

### Import 0.2: Paper-26 Residual Density

Paper 26 defines the exact same-law residual Hamiltonian
\[
H_{RPF}^{N,j}(\omega)
=
\log Z_{N,j}
+\log p_{N,j}(\omega)
-\sum_{p\in P_{N,j}}\log K_p^{CE,N,j}(\omega_p)
\]
on the essential support of the adaptive `SEL2` pushed-forward scalar law.
Constants do not affect atom oscillations, but conditional kernels require
normalization, and therefore require actual conditional weights.

### Target Convention 0.3: Declared Fundamental Branch

Paper 22 fixes the convention: the program targets one declared actual
\(4D\) \(SU(N)\) branch, with \(N\) fixed before the final source and
prefactor inequalities.  \(SU(4)\) was the first low-rank diagnostic row,
not the default adaptive target.

Therefore Paper 29 treats the adaptive fundamental branch uniformly in
\(N\).  If a later paper declares fixed low-rank \(SU(4)\), the same formulas
specialize by setting \(N=4\).

## 1. Step 1: The Smallest Nontrivial Low-Mode Target

### Definition 1.1: Minimal Endpoint Peter-Weyl Battery

For the declared \(SU(N)\) fundamental branch, let
\[
        {\mathcal B}_{min}(N)
\]
be the first nonconstant endpoint Peter-Weyl battery containing:

1. the fundamental channel \(F_N\);
2. its dual \(F_N^*\);
3. the adjoint channel \(\mathrm{Ad}_N\), which appears in
   \(F_N\otimes F_N^*\) and is the first natural centered response channel.

Let \(L_{min}(N)\) be the smallest cutoff retaining
\({\mathcal B}_{min}(N)\) and the constant mode.  The centered low-mode
space is
\[
        {\mathcal H}_{min,\circ}(N)
        :=
        \Pi_{\le L_{min}}^{xy}(I-P_0)L^2(G\times G).
\]

For fixed \(SU(4)\), this battery is
\[
        \{F_4,F_4^*,\mathrm{Ad}_4\}.
\]

### Definition 1.2: Minimal Low-Mode Norm

Set
\[
        \Theta_{min}^{N,j}
        :=
        \sup_{e,\zeta}
        \left\|
        \Pi_{\le L_{min}}^{xy}
        T_{e,\zeta,\circ}^{N,j}
        \Pi_{\le L_{min}}^{xy}
        \right\|_{edge}
\]
and
\[
        \Theta_{min}^{act}
        :=
        \limsup_{(N,j)}\Theta_{min}^{N,j}.
\]

### Lemma 1.3: Minimality Of The Target

Any nontrivial spectral proof on the fundamental branch must control at
least \({\mathcal B}_{min}(N)\).

Proof.

The constant mode is removed by centering.  The first endpoint observables
that can carry fundamental-channel response are \(F_N\) and \(F_N^*\).  The
first centered two-endpoint response generated by a fundamental against its
dual contains \(\mathrm{Ad}_N\).  Dropping these modes would test only the
constant sector or a sector not containing the declared fundamental
response. `square`

### Corollary 1.4: Step 1 Is Complete

The smallest useful spectral target is
\[
        \Theta_{min}^{act}
\]
on \({\mathcal B}_{min}(N)\).  A proof that misses this target is not a
proof of the RN-MIXAMP spectral route.

## 2. Step 2: Literal Low-Mode Matrix Entries

### Definition 2.1: Conditional Residual Kernel From \(H_{RPF}\)

Fix a minimal live edge \(e=(x,y)\), outside label \(\zeta\), endpoint values
\(u\in G_x\), \(v\in G_y\), and any finite internal template variables
\(\xi\).  Write
\[
        H_{e,\zeta}^{N,j}(u,v,\xi)
\]
for the restriction of \(H_{RPF}^{N,j}\) to the template.

Set
\[
        Z_{e,\zeta}^{N,j}(u)
        :=
        \int
        \exp(H_{e,\zeta}^{N,j}(u,w,\xi))\,d\lambda_\xi\,d\lambda_y(w).
\]
The actual conditional kernel from \(x\) to \(y\) is
\[
        K_{e,\zeta}^{N,j}(u,dv)
        =
        {1\over Z_{e,\zeta}^{N,j}(u)}
          \int
          \exp(H_{e,\zeta}^{N,j}(u,v,\xi))\,d\lambda_\xi\,
          d\lambda_y(v).
\]
The denominator depends on \(u\) and \(\zeta\).  It is part of the same-law
conditional object.

### Definition 2.2: Low-Mode Matrix Entries

Choose an orthonormal Peter-Weyl basis
\[
        \{\psi_\alpha\}_{\alpha\in{\mathcal B}_{min,\circ}(N)}
\]
for the centered minimal battery.  With \(\mu_{x,\zeta}^{N,j}\) the actual
conditional marginal of \(u\), define
\[
        M_{\alpha\beta}^{N,j}(e,\zeta)
        :=
        \int
        \overline{\psi_\alpha(u)}
        \left(
        \int \psi_\beta(v)\,K_{e,\zeta}^{N,j}(u,dv)
        \right)
        d\mu_{x,\zeta}^{N,j}(u).
\]
Equivalently,
\[
        M_{\alpha\beta}^{N,j}(e,\zeta)
        =
        \int
        \overline{\psi_\alpha(u)}\psi_\beta(v)
        \,d\gamma_{e,\zeta}^{N,j}(u,v),
\]
where \(\gamma_{e,\zeta}^{N,j}\) is the actual two-endpoint conditional
measure induced by \(H_{RPF}^{N,j}\).

### Lemma 2.3: Entry Source Equivalence

The matrix entries \(M_{\alpha\beta}^{N,j}(e,\zeta)\) are determined by:

1. the same-law residual density values \(H_{e,\zeta}^{N,j}(u,v,\xi)\);
2. the internal-variable integration/marginalization measure;
3. the endpoint conditional normalizers;
4. the outside-label weights \(\mu_{x,\zeta}^{N,j}\);
5. an omitted-template tail certificate if the template is not full.

Proof.

Substitute Definition 2.1 into Definition 2.2.  Every entry is a finite
conditional integral of known Peter-Weyl basis functions against the actual
conditional density.  Conversely, without the conditional density and its
normalizers, the integral is not determined. `square`

### Lemma 2.4: Four-Point RN Ratios Do Not Determine Low-Mode Entries

The RN-MIXAMP four-point ratio table from Paper 26 does not determine the
low-mode matrix entries of Definition 2.2.

Proof.

Let
\[
        H'(u,v,\xi,\zeta)
        =
        H(u,v,\xi,\zeta)+a(u)+b(v)+c(\xi,\zeta),
\]
where \(a,b,c\) are finite one-side or outside functions.  The four-point
alternating mixed difference in \(u,u';v,v'\) cancels \(a\), \(b\), and
\(c\).  Thus the RN-MIXAMP mixed ratio is unchanged.

But \(b(v)\) changes the conditional law of \(v\) given \(u,\zeta\), and
\(a(u)\) changes the marginal weight of \(u\) in the two-endpoint measure.
Therefore the matrix entries
\[
        \int \overline{\psi_\alpha(u)}\psi_\beta(v)
        \,d\gamma_{e,\zeta}^{N,j}(u,v)
\]
can change while all four-point mixed ratios remain fixed.  Hence the
ratio table is insufficient for spectral value extraction. `square`

### Corollary 2.5: Spectral Values Require More Than RN-MIXAMP Ratios

To compute or bound \(\Theta_{min}^{act}\), one needs actual conditional
weights or a primitive residual density source.  The Paper-26 RN-ratio
bypass is enough for Dobrushin influence bounds, but not enough for the
low-mode spectral matrix.

This is the first decisive result of Paper 29.

## 3. Step 3: Attempt A Strict Low-Mode Gap

### Definition 3.1: Minimal Low-Mode Entry Source

`P29-RN-MIXAMP-LOWENTRY` asserts that, cofinally, all entries
\[
        M_{\alpha\beta}^{N,j}(e,\zeta),
        \qquad
        \alpha,\beta\in{\mathcal B}_{min,\circ}(N),
\]
are printed or bounded sharply enough to compute
\(\Theta_{min}^{N,j}\).

### Definition 3.2: Minimal Low-Mode Gap Source

`P29-RN-MIXAMP-LOWGAP(theta)` asserts
\[
        \Theta_{min}^{act}\le\theta<\theta_{\mathrm{crit}}.
\]

### Lemma 3.3: Low Entries Decide The Low Gap

`P29-RN-MIXAMP-LOWENTRY` decides whether
`P29-RN-MIXAMP-LOWGAP(theta)` holds for the minimal battery.

Proof.

For each finite \((N,j)\), the matrix on
\({\mathcal B}_{min,\circ}(N)\) is finite.  Once its entries are printed or
bounded, its edge norm is finite matrix arithmetic.  The cofinal limsup then
decides the declared \(\theta\)-bound. `square`

### Definition 3.4: Same-Law Doeblin Floor

For \(\varepsilon>0\), `P29-RN-MIXAMP-DOEBLIN(epsilon)` asserts that there
exists a same-law probability measure \(\nu_{e,\zeta}^{N,j}\) such that,
cofinally and uniformly in \(e,\zeta,u\),
\[
        K_{e,\zeta}^{N,j}(u,dv)
        \ge
        \varepsilon\,\nu_{e,\zeta}^{N,j}(dv).
\]

### Lemma 3.5: Doeblin Floor Gives A Strict Gap

If `P29-RN-MIXAMP-DOEBLIN(epsilon)` holds, then the centered oscillation norm
of the transfer kernel is at most
\[
        1-\varepsilon.
\]
In particular,
\[
        \Theta_{min}^{act}\le1-\varepsilon.
\]

Proof.

Write
\[
        K(u,dv)=\varepsilon\nu(dv)+(1-\varepsilon)\widetilde K(u,dv).
\]
On centered functions the \(\nu\)-averaging part contributes only a constant
mode, which is killed by centering.  The remaining kernel has mass
\(1-\varepsilon\) and is non-expansive in oscillation.  Therefore the
centered oscillation contraction is at most \(1-\varepsilon\). `square`

### Corollary 3.6: Doeblin Margin Sufficient Test

If
\[
        1-\varepsilon+\kappa^{act}[L_{min}]
        <
        \theta_{\mathrm{crit}},
\]
then `P29-RN-MIXAMP-DOEBLIN(epsilon)` plus the corresponding tail bound
closes adaptive Branch A.

Proof.

Apply Lemma 3.5 and the Paper-28 spectral-tail closure theorem. `square`

### Proposition 3.7: Current-Corpus Low-Gap Verdict

The current Papers 20--28 do not prove `P29-RN-MIXAMP-LOWENTRY`,
`P29-RN-MIXAMP-LOWGAP(theta)` in a closing range, or
`P29-RN-MIXAMP-DOEBLIN(epsilon)` with a useful \(\varepsilon>0\).

Proof.

Paper 26 proves that the primitive residual density values, outside-label
weights, and local conditional probability table are not populated by the
current corpus.  Lemma 2.3 shows that those are precisely the data needed
for low-mode entries.  Lemma 2.4 shows that the weaker RN-ratio table cannot
recover them.

The only source-free contraction is Markov/oscillation non-expansion, which
Paper 28 already records as \(\Theta\le1\).  A strict Doeblin floor would
require a same-law positive lower bound on conditional densities after the
RPF residual division.  No such lower bound is printed in Papers 20--28, and
the lower-floor theorems currently available concern different scalar loss
quantities, not a uniform conditional minorization of
\(K_{e,\zeta}^{N,j}\). `square`

We record:
\[
\boxed{\mathrm{P29\text{-}RN\text{-}MIXAMP\text{-}LOWENTRY\text{-}GAP}},
\qquad
\boxed{\mathrm{P29\text{-}RN\text{-}MIXAMP\text{-}LOWGAP\text{-}GAP}},
\qquad
\boxed{\mathrm{P29\text{-}RN\text{-}MIXAMP\text{-}DOEBLIN\text{-}GAP}}.
\]

## 4. Step 4: Tail Audit After Low-Mode Slack

### Lemma 4.1: Tail Cannot Rescue A Missing Low-Mode Gap

If no strict bound
\[
        \Theta_{min}^{act}<\theta_{\mathrm{crit}}
\]
is proved, then no nonnegative tail estimate can close the spectral route
through \(L_{min}\).

Proof.

The spectral margin is
\[
        \Theta^{act}[L]+\kappa^{act}[L]<\theta_{\mathrm{crit}},
\]
and \(\kappa^{act}[L]\ge0\).  Therefore even zero tail cannot compensate for
the absence of a strict low-mode bound below \(\theta_{\mathrm{crit}}\).
`square`

### Proposition 4.2: Current-Corpus Tail Status

The current Papers 20--28 do not prove a finite-band source, a uniform
Peter-Weyl decay source, or a direct cofinal tail table for the actual
RN-MIXAMP residual Hamiltonian.

Proof.

This is Paper 28 Proposition 3.4 applied to the minimal cutoff
\(L_{min}\).  Paper 29 has not introduced any new tail information; it has
only shown that the low-mode values themselves require additional
conditional weights. `square`

### Corollary 4.3: Spectral Route Current-Corpus Verdict

The current corpus cannot close the spectral route:
\[
        \Theta^{act}[L]+\kappa^{act}[L]
        <
        \theta_{\mathrm{crit}}
\]
is not proved for \(L=L_{min}\), nor for any larger cutoff schedule.

Proof.

For \(L_{min}\), Proposition 3.7 gives no strict low gap and Proposition 4.2
gives no tail source.  For larger \(L\), Paper 28 proves the same low-gap and
tail gaps without the minimal-battery specialization. `square`

We record:
\[
\boxed{\mathrm{P29\text{-}RN\text{-}MIXAMP\text{-}SPECTRAL\text{-}VALUE\text{-}GAP}.}
\]

## 5. Step 5: Pivot Ledger

### Theorem 5.1: Paper-29 Five-Step Verdict

Paper 29 completes the low-mode value-extraction attempt:

1. the smallest useful low-mode battery is
   \({\mathcal B}_{min}(N)=\{F_N,F_N^*,\mathrm{Ad}_N\}\), with the fixed
   \(SU(4)\) specialization \(\{F_4,F_4^*,\mathrm{Ad}_4\}\);
2. the low-mode matrix entries are literal same-law conditional integrals of
   Peter-Weyl basis functions against the residual conditional kernel;
3. those entries require actual conditional weights, not just four-point
   RN-MIXAMP ratios;
4. the current corpus proves no strict low-mode spectral gap and no useful
   same-law Doeblin floor;
5. because low-mode slack is absent, the tail route cannot rescue the
   spectral proof from the current data.

Proof.

Items 1--2 are Sections 1--2.  Item 3 is Lemma 2.4 and Corollary 2.5.  Item
4 is Proposition 3.7.  Item 5 is Lemma 4.1 and Corollary 4.3. `square`

### Corollary 5.2: Exact Remaining Spectral Source

The spectral branch can proceed only by proving a genuinely new same-law
source package:
\[
\boxed{
\mathrm{P29\text{-}RN\text{-}MIXAMP\text{-}LOWENTRY}
+
\mathrm{P28\text{-}RN\text{-}MIXAMP\text{-}KTAIL}(\kappa)
}
\]
with resulting
\[
        \Theta^{act}[L]+\kappa^{act}[L]<\theta_{\mathrm{crit}}.
\]

Equivalently, one may prove a stronger same-law Doeblin floor plus tail:
\[
        1-\varepsilon+\kappa<\theta_{\mathrm{crit}}.
\]

### Corollary 5.3: Preferred Next Move

If the program stays in adaptive Branch A, the next positive attempt should
not be another spectral bookkeeping paper.  It should be one of:

1. a primitive residual/conditional value theorem strong enough to populate
   `P29-RN-MIXAMP-LOWENTRY`;
2. a direct signed amplitude theorem that avoids reconstructing the whole
   transition kernel;
3. a bridge-damping theorem plus the common same-law tail source;
4. the lower floor \(\overline\Lambda_{13}^{RPF}\ge M_*\);
5. or an exit from adaptive Branch A to Branch B/C.

The most economical Branch-A pivot is signed/bridge amplitude control,
because it acts on the mixed object before full transition-kernel
normalizers are required.

## 6. Primitive Residual Value Theorem To Be Sourced

The preceding sections show exactly why the spectral route needs more than
RN-MIXAMP ratios.  We now attack the missing primitive residual value theorem
itself.

### Definition 6.1: Primitive Residual Value Source

For a finite adaptive template \({\mathfrak T}(N,j)\), define
\[
        h_{prim}^{N,j}(\omega)
        :=
        \log p_{N,j}(\omega)
        -
        \sum_{p\in P_{N,j}}\log K_p^{CE,N,j}(\omega_p).
\]
The normalizing constant \(\log Z_{N,j}\) is omitted because it cancels from
conditional probabilities after local normalization and from all atom
oscillations.

`P29-PRIMRES-VAL({\mathfrak T},\epsilon)` asserts that, cofinally, the
current source corpus supplies:

1. an essential-support mask for all template states;
2. intervals of width at most \(\epsilon\) for
   \(h_{prim}^{N,j}(\omega)\) on every template state used by the low-mode,
   Dobrushin, screened, signed, or bridge row;
3. the outside-label conditional weights and endpoint normalizers needed to
   form the finite conditional kernels;
4. an omitted-template tail certificate whose contribution to the requested
   row is at most \(\epsilon\).

The source is value-populated, not merely formally defined.

### Lemma 6.2: Primitive Residual Values Populate Low Entries

If `P29-PRIMRES-VAL({\mathfrak T},\epsilon)` holds along a template ladder
whose omitted-tail error tends to zero, then `P29-RN-MIXAMP-LOWENTRY` holds
with entry intervals whose widths tend to zero.

Proof.

Definition 2.1 expresses the conditional kernel through exponentials of the
restricted residual Hamiltonian and finite normalizers.  Definition 2.2 then
expresses every low-mode entry as a finite conditional integral of bounded
Peter-Weyl basis functions against that kernel.  Interval arithmetic
propagates the primitive residual intervals and normalizer intervals to
matrix-entry intervals.  The omitted-template tail certificate gives the
declared error term. `square`

### Corollary 6.3: Primitive Residual Values Would Reopen The Spectral Route

If `P29-PRIMRES-VAL({\mathfrak T},\epsilon_j)` holds with
\(\epsilon_j\to0\), and if the resulting low-mode norm and same-law tail
satisfy
\[
        \Theta^{act}[L]+\kappa^{act}[L]<\theta_{\mathrm{crit}},
\]
then adaptive Branch A closes.

Proof.

Lemma 6.2 supplies `LOWENTRY`.  Finite matrix arithmetic supplies the
low-mode norm.  The displayed strict inequality is the Paper-28 spectral-tail
closure theorem. `square`

## 7. Attempt I: Direct Density Sourcing

### Lemma 7.1: Declared Law Is Not A Value Table

The declaration of the adaptive pushed-forward law
\(\Gamma_{N,j}^{SEL2}\) does not by itself prove
`P29-PRIMRES-VAL({\mathfrak T},\epsilon)`.

Proof.

The declaration identifies the finite probability law whose values must be
used.  It does not print or bound the finite density values
\(p_{N,j}(\omega)\) on the template states, nor does it print outside-label
conditional weights.  Paper 26 already separates finite existence from
cofinal value population. `square`

### Lemma 7.2: Exact `CE` Does Not Populate The Residual Density

The exact-entry central quotient supplies the factors
\(K_p^{CE,N,j}\) on the declared branch, but it does not by itself populate
\[
        h_{prim}^{N,j}
        =
        \log p_{N,j}
        -
        \sum_p\log K_p^{CE,N,j}.
\]

Proof.

Subtracting known or licensed central factors from an unknown log-density
does not determine the result.  The live input remains the same-law density
\(\log p_{N,j}\) and the conditional normalizers.  Paper 26 makes exactly
this separation in its primitive source ledger. `square`

### Lemma 7.3: RN Ratios Are Still Insufficient

The Paper-26 RN-ratio bypass does not prove `P29-PRIMRES-VAL`.

Proof.

RN ratios are four-point alternating differences.  Lemma 2.4 proves that
one-site endpoint and outside terms can change primitive conditional weights
while leaving those ratios unchanged.  Therefore RN-ratio values cannot
recover the pointwise primitive residual value table or the conditional
normalizers required by Definition 6.1. `square`

### Proposition 7.4: Direct Density Source Current-Corpus Verdict

The current Papers 20--28 do not prove `P29-PRIMRES-VAL` by direct density
sourcing.

Proof.

Lemmas 7.1--7.3 exhaust the direct objects already present: the declared law,
the exact `CE` quotient, and the RN-ratio bypass.  None supplies the
pointwise primitive residual value intervals and conditional normalizers of
Definition 6.1. `square`

We record:
\[
\boxed{\mathrm{P29\text{-}PRIMRES\text{-}DIRECT\text{-}GAP}.}
\]

## 8. Attempt II: Residual Coefficient Identity

### Definition 8.1: Primitive Residual Row-Identity Source

`P29-PRIMRES-ROWID-RES` asserts that the actual literal Möbius residual
atoms of Paper 23 Definition 15.2 are equal to, or are connected by a finite
triangular transform with bounded inverse to, the clean residual coefficients
used in the Paper-16/Paper-20 clean KP table, after the same `CE` quotient
and on the same pushed-forward scalar law.

This is stronger than label matching.  It is a coefficient-value identity or
coefficient-value domination.

### Lemma 8.2: Row Identity Would Source Primitive Residual Values

Assume:

1. `P29-PRIMRES-ROWID-RES`;
2. the corresponding clean coefficient values or intervals are printed on a
   finite coefficient battery;
3. the transform tail outside the template is bounded by \(\epsilon\).

Then `P29-PRIMRES-VAL({\mathfrak T},C\epsilon)` holds for an explicit finite
constant \(C\) determined by the transform and the template size.

Proof.

The actual residual density is reconstructed from its centered Möbius atoms
by finite Möbius inversion.  If those atoms are equal to, or finitely
dominated by, the printed clean coefficient table, then their values on the
template are known or bounded.  The bounded inverse/triangular transform
propagates intervals with a finite condition number \(C\).  Summing the
atoms reconstructs \(h_{prim}\) up to the declared tail. `square`

### Proposition 8.3: Current-Corpus Row-Identity Verdict

The current Papers 20--28 do not prove `P29-PRIMRES-ROWID-RES`.

Proof.

Paper 23 Theorem 21.4 isolates the remaining `ROWID` obstruction exactly as
`P23-RPF-ROWID-RES`: one must prove that finite Möbius inversion of the
actual adaptive residual density gives the same connected residual
coefficients as Paper 16's clean residual expansion, or a finite dominated
transform between them.  Paper 23 states that the local no-double-charge
rows are closed, but this residual coefficient identity is not proved.
Papers 24--28 do not add such an identity; they only show that certificates,
RN ratios, and low-mode operators remain value-starved without it. `square`

We record:
\[
\boxed{\mathrm{P29\text{-}PRIMRES\text{-}ROWID\text{-}GAP}.}
\]

## 9. Attempt III: Actual Cumulant/Polymer Value Transform

### Definition 9.1: Primitive Residual Polymer-Value Source

`P29-PRIMRES-POLYVAL(q,a,\epsilon)` asserts an exact same-law
cumulant-to-polymer representation
\[
        h_{prim}^{N,j}(\omega)
        =
        \sum_{\Gamma\subset{\mathfrak T}(N,j)}
        \Psi_\Gamma^{N,j}(\omega_\Gamma)
        +
        R_{\mathrm{tail}}^{N,j}(\omega),
\]
with:

1. every retained activity \(\Psi_\Gamma^{N,j}\) printed or bounded;
2. a KP bound
   \[
   \sup_x\sum_{\Gamma\ni x}
   \|\Psi_\Gamma^{N,j}\|_{\infty}e^{a|\Gamma|}
   \le q<1;
   \]
3. \(\|R_{\mathrm{tail}}^{N,j}\|_{\mathrm{osc}}\le\epsilon\);
4. all quantities evaluated on the same adaptive pushed-forward scalar law.

### Lemma 9.2: Polymer Values Source Primitive Residual Values

`P29-PRIMRES-POLYVAL(q,a,\epsilon)` implies
`P29-PRIMRES-VAL({\mathfrak T},C\epsilon)` for a finite constant \(C\)
depending only on the template readout norm.

Proof.

The retained polymer activities give an explicit finite value or interval
for \(h_{prim}\) on every template state by direct summation.  The KP bound
controls the retained activity sum uniformly, and the residual tail gives
the only omitted error.  Finite endpoint normalizers then follow by
exponentiation and finite summation on the same template. `square`

### Proposition 9.3: Current-Corpus Polymer-Value Verdict

The current Papers 20--28 do not prove `P29-PRIMRES-POLYVAL(q,a,\epsilon)`
with \(q<1\) and useful \(\epsilon\).

Proof.

Paper 23 defines the actual-law cumulant/polymer route
`P23-RPF-POLY-ACT` and `P23-RPF-ACTUAL-KP(q,a)` and proves that it would
close the RPF factorization gate.  It does not print the actual same-law
polymer activity values for the adaptive residual density.  Paper 26 later
rephrases the same absence as the primitive residual source gap.  Papers
27--28 do not add polymer activity values; they only sharpen the RN-MIXAMP
and spectral consequences of not having them. `square`

We record:
\[
\boxed{\mathrm{P29\text{-}PRIMRES\text{-}POLYVAL\text{-}GAP}.}
\]

## 10. Primitive Residual Value Source Verdict

### Theorem 10.1: Primitive Residual Value Theorem Is Not Sourced By The Current Corpus

The current Papers 20--28 do not prove `P29-PRIMRES-VAL` by:

1. direct density values;
2. exact `CE` division;
3. RN-ratio recovery;
4. residual coefficient identity with the clean KP table;
5. actual same-law cumulant/polymer value expansion.

The completed gaps are
\[
\begin{gathered}
\mathrm{P29\text{-}PRIMRES\text{-}DIRECT\text{-}GAP},\\
\mathrm{P29\text{-}PRIMRES\text{-}ROWID\text{-}GAP},\\
\mathrm{P29\text{-}PRIMRES\text{-}POLYVAL\text{-}GAP}.
\end{gathered}
\]

Proof.

Direct density sourcing is Proposition 7.4.  The residual coefficient route
is Proposition 8.3.  The actual polymer-value route is Proposition 9.3.
These are the admissible same-law value routes already present in the
corpus.  None proves the value-populated primitive residual theorem of
Definition 6.1. `square`

### Corollary 10.2: Exact New Theorem Needed

A genuine primitive residual value theorem must be one of:

1. a direct cofinal table or sharp interval theorem for
   \[
   \log p_{N,j}(\omega)-\sum_p\log K_p^{CE,N,j}(\omega_p);
   \]
2. `P29-PRIMRES-ROWID-RES` plus clean coefficient values and a bounded
   transform tail;
3. `P29-PRIMRES-POLYVAL(q,a,\epsilon)` with \(q<1\) and useful
   \(\epsilon\);
4. a direct conditional-kernel table or same-law Doeblin floor strong enough
   to bypass pointwise residual values.

Until one of these is proved, primitive residual value sourcing does not
advance Branch A.

### Corollary 10.3: Updated Pivot Recommendation

After the primitive residual value audit, the most economical positive
Branch-A route is still signed/bridge amplitude control unless a new
same-law density or coefficient identity is discovered.  The reason is that
primitive residual values require the full conditional normalization
machinery, while signed/bridge routes may act directly on the mixed
amplitude table already isolated in Paper 26.

## 11. Part-I Spectral Completion Certificate

The first part of Paper 29 is complete only if it has converted the Paper-28
spectral-tail obstruction into an exact value-source obstruction and has
ruled out every source already present in the corpus.  The completion
criterion is therefore:

1. freeze the finite low-mode target on the declared adaptive fundamental
   branch;
2. write the same-law low-mode entries as conditional integrals against the
   actual residual density;
3. prove whether the Paper-26 four-point RN-MIXAMP ratios determine those
   entries;
4. audit low-mode gap, Doeblin, and tail recovery from the present corpus;
5. define the primitive residual value theorem that would populate the
   missing entries;
6. test all currently available source routes for that theorem;
7. export a precise next theorem rather than another finite-label
   enumeration task.

### Theorem 11.1: Paper 29 Closes The Spectral Value-Extraction Attempt

Paper 29 satisfies the completion criterion above.

Proof.

Item 1 is completed by Definition 1.1 and Corollary 1.4.  Item 2 is
completed by Definitions 2.1--2.2 and Lemma 2.3.  Item 3 is completed by
Lemma 2.4 and Corollary 2.5: RN-MIXAMP ratios do not determine low-mode
entries because endpoint-additive terms cancel from ratios while changing
conditional kernels.  Item 4 is completed by Proposition 3.7 and Corollary
4.3.  Item 5 is completed by Definition 6.1, Lemma 6.2, and Corollary 6.3.
Item 6 is completed by Propositions 7.4, 8.3, and 9.3.  Item 7 is completed
by Corollary 10.2.

Thus the low-mode spectral route is not blocked by a missing finite
definition.  It is blocked by missing same-law value information. `square`

We record the paper-level closure label
\[
\boxed{\mathrm{P29\text{-}SPECTRAL\text{-}VALUE\text{-}EXTRACTION\text{-}CLOSED}}.
\]
Equivalently, the plain label is
`P29-SPECTRAL-VALUE-EXTRACTION-CLOSED`.

### Corollary 11.2: More Finite Labels Do Not Move Paper 29

Adding more finite endpoint labels, canonical rows, or template names does
not change the Paper-29 verdict unless the added data also carry actual
same-law values for one of:

1. the conditional low-mode entries \(M_{\alpha\beta}^{N,j}(e,\zeta)\);
2. the primitive residual \(h_{prim}^{N,j}\);
3. a same-law Doeblin floor;
4. a Peter-Weyl tail table tied to the same residual law.

Finite labels without such values only refine the domain of an unknown
conditional kernel.  They do not bound its low-mode spectrum, its tail, or
its primitive residual weights. `square`

### Corollary 11.3: Final Paper-29 Handoff

The exact surviving Branch-A value targets are:
\[
\begin{array}{ll}
\text{direct residual values:}
&
\mathrm{P29\text{-}PRIMRES\text{-}VAL},\\[2mm]
\text{row identity plus values:}
&
\mathrm{P29\text{-}PRIMRES\text{-}ROWID\text{-}RES},\\[2mm]
\text{polymer values:}
&
\mathrm{P29\text{-}PRIMRES\text{-}POLYVAL}(q,a,\epsilon),\\[2mm]
\text{conditional bypass:}
&
\mathrm{P29\text{-}RN\text{-}MIXAMP\text{-}DOEBLIN}(\epsilon)
\text{ or direct low entries plus tail.}
\end{array}
\]

Any subsequent paper should prove one of these value statements, prove a
lower-floor obstruction, or pivot to the signed/bridge amplitude program.

## 12. Part II: Literal Primitive Residual Atoms

We now continue Paper 29 inside the same file.  The purpose is not to add
more finite labels.  The purpose is to test whether the primitive residual
value theorem can be sourced by a literal row identity against the existing
Paper-23/Paper-26 residual atoms.

### Definition 12.1: Primitive Residual Atom

On a finite adaptive template \(V=V_{RPF}^{N,j}\), fix a base configuration
\(o\) in the essential support of the pushed-forward adaptive law and write
\[
h_{prim}^{N,j}(\omega)
:=
\log p_{N,j}(\omega)
-
\sum_{p\in P_{N,j}}\log K_p^{CE,N,j}(\omega_p).
\]
For every nonempty finite \(A\subseteq V\), define the primitive residual
Möbius atom
\[
\Psi_A^{N,j}(\omega_A)
:=
\sum_{B\subseteq A}(-1)^{|A|-|B|}
h_{prim}^{N,j}(\omega_B,o_{A\setminus B},o_{V\setminus A}).
\]

The atom is an actual same-law scalar record.  It is defined only from the
adaptive pushed-forward scalar density and the same exact `CE` factor already
used by Papers 23 and 26.

### Lemma 12.2: Primitive Atoms Equal RPF Residual Atoms

For every nonempty \(A\),
\[
\Psi_A^{N,j}=\Phi_A^{N,j},
\]
where \(\Phi_A^{N,j}\) is the Paper-23/Paper-26 literal RPF residual atom.

Proof.

Paper 26 writes
\[
H_{RPF}^{N,j}(\omega)
=
\log Z_{N,j}
+\log p_{N,j}(\omega)
-\sum_p\log K_p^{CE,N,j}(\omega_p).
\]
Thus
\[
H_{RPF}^{N,j}=h_{prim}^{N,j}+\log Z_{N,j}.
\]
Finite Möbius differences over a nonempty support annihilate constants:
\[
\sum_{B\subseteq A}(-1)^{|A|-|B|}\log Z_{N,j}=0.
\]
Therefore the nonconstant primitive residual atom is exactly the nonconstant
RPF residual atom. `square`

### Corollary 12.3: The Row-Identity Target Is Literal

`P29-PRIMRES-ROWID-RES` is not asking for a new hidden decomposition.  The
decomposition already exists:
\[
h_{prim}^{N,j}(\omega)-h_{prim}^{N,j}(o)
=
\sum_{\emptyset\ne A\subseteq V}\Psi_A^{N,j}(\omega_A).
\]
The missing issue is value population: which atoms are nonzero, what their
same-law coefficient values are, and how their omitted template tail is
bounded cofinally.

We record the algebraic identity:
\[
\boxed{\mathrm{P29\text{-}PRIMRES\text{-}ATOM\text{-}ID}}.
\]
Equivalently, the plain label is `P29-PRIMRES-ATOM-ID`.

## 13. Clean Rows, Conditional Rows, And The Defect

The previous section shows that primitive residual atoms are not mysterious.
The next possible mistake is subtler: the clean crossing rows that survive
four-point RN-MIXAMP ratios are not the whole conditional kernel.

### Definition 13.1: Conditional Row Split

For a rooted edge template with free endpoint coordinates \(u\) at \(x\) and
\(v\) at \(y\), split the primitive residual atom list into four disjoint
classes after the outside label \(\zeta\) is fixed:

1. `const/outside`: atoms independent of \(u,v\);
2. `x-one-site`: atoms depending on \(u\) but not \(v\);
3. `y-one-site`: atoms depending on \(v\) but not \(u\);
4. `cross`: atoms depending on both \(u\) and \(v\).

Let
\[
h_{prim}=h_0+h_x+h_y+h_{cross}+h_{def},
\]
where \(h_0,h_x,h_y,h_{cross}\) are the sums over the corresponding printed
classes and \(h_{def}\) is the sum of all atoms not licensed by the current
template, classifier, or tail certificate.

The clean RN-MIXAMP table sees only the mixed alternating part of
\(h_{cross}\).  The conditional kernel for low-mode entries sees
\[
\exp(h_x(u;\zeta)+h_y(v;\zeta)+h_{cross}(u,v;\zeta)+h_{def}(u,v;\zeta))
\]
after finite normalization.

### Lemma 13.2: Crossing Rows Alone Do Not Determine Low-Mode Entries

Even if all `cross` clean rows are value-populated, the low-mode transition
entries \(M_{\alpha\beta}^{N,j}(e,\zeta)\) are not determined unless the
one-site endpoint rows and the remaining defect are also controlled.

Proof.

Fix a finite endpoint template and replace the primitive residual by
\[
h_{prim}'(u,v;\zeta)
=
h_{prim}(u,v;\zeta)+a(u;\zeta)+b(v;\zeta),
\]
where \(a\) and \(b\) are arbitrary finite endpoint functions.  The mixed
four-point difference of \(a(u)+b(v)\) is zero:
\[
a(u)+b(v)+a(u')+b(v')-a(u)-b(v')-a(u')-b(v)=0.
\]
Therefore all RN-MIXAMP four-point crossing rows are unchanged.  But the
conditional kernel is multiplied by \(e^{a(u)+b(v)}\) before normalization,
so its endpoint marginals and its low-mode matrix entries can change.  Hence
crossing rows alone do not determine the conditional low-mode entries.
`square`

### Corollary 13.3: Full Row Identity Must Include Normalizers

A row identity strong enough to prove `P29-PRIMRES-VAL` must include:

1. all printed clean crossing atoms;
2. all endpoint one-site atoms that enter conditional normalization;
3. the finite endpoint normalizers themselves, or intervals sharp enough to
   control them;
4. a tail bound for every omitted atom that can affect the endpoint kernel.

Thus a clean crossing identity is a source for RN-MIXAMP mixed amplitudes,
not by itself a source for low-mode spectral entries.

## 14. The Full Primitive Row-Identity Source

The viable row-identity theorem is therefore stronger than the first
`P29-PRIMRES-ROWID-RES` sketch in Section 8.

### Definition 14.1: Full Primitive Residual Row Identity

`P29-PRIMRES-ROWID-FULL({\mathfrak T},\epsilon)` asserts that, cofinally, a
finite adaptive template ladder \({\mathfrak T}\) supplies:

1. the nonzero primitive atom list \(\{A:\Psi_A^{N,j}\not\equiv0\}\) relevant
   to each endpoint kernel;
2. rigorous value intervals for all retained atoms \(\Psi_A^{N,j}\);
3. the endpoint one-site value intervals and the resulting normalization
   intervals;
4. a retained clean crossing table compatible with Paper 23's `CleanRPF`
   classifier;
5. an omitted atom defect \(h_{def}^{N,j}\) satisfying
   \[
   \operatorname{osc}_{u,v}h_{def}^{N,j}(\cdot\mid\zeta)\le\epsilon
   \]
   uniformly over the endpoint labels used in the low-mode battery.

This is a value theorem, not a label theorem.

### Lemma 14.2: Full Row Identity Sources Primitive Residual Values

If `P29-PRIMRES-ROWID-FULL({\mathfrak T},\epsilon)` holds and
\(\epsilon\to0\) cofinally, then `P29-PRIMRES-VAL({\mathfrak T},C\epsilon)`
holds for an explicit finite constant \(C\) depending only on the retained
endpoint state cardinalities and the chosen low-mode battery.

Proof.

On each retained finite template, the primitive residual is the finite sum
of the retained atom values plus \(h_{def}\).  Finite exponentiation and
finite normalization are locally Lipschitz on any interval where the
normalizers are bounded away from zero.  The same source includes those
normalizer intervals.  Therefore an \(\epsilon\)-oscillation defect in the
log-density produces a \(C\epsilon\) error in the conditional weights and
primitive residual intervals.  This is exactly Definition 6.1. `square`

### Corollary 14.3: Full Row Identity Would Reopen The Spectral Route

If `P29-PRIMRES-ROWID-FULL({\mathfrak T},\epsilon_j)` holds with
\(\epsilon_j\to0\) and with a same-law tail profile small enough for the
Paper-28 spectral-tail margin, then the Paper-29 low-mode entries are
populated and the spectral route is reduced to finite matrix arithmetic.

Proof.

Apply Lemma 14.2, then Lemma 6.2 and Corollary 6.3. `square`

## 15. Exact Defect Dichotomy

The full row identity gives a useful positive theorem, but it also gives the
right failure object.

### Definition 15.1: Primitive Row-Identity Defect

For a chosen retained source class \({\mathcal C}_{ret}^{N,j}\), define
\[
D_{row}^{N,j}
:=
h_{prim}^{N,j}
-h_{prim}^{N,j}(o)
-\sum_{A\in{\mathcal C}_{ret}^{N,j}}\Psi_A^{N,j}.
\]
Its endpoint conditional defect is
\[
\Delta_{row}^{N,j}(e,\zeta)
:=
\operatorname{osc}_{u,v}
D_{row}^{N,j}(u,v\mid\zeta).
\]
The cofinal defect profile is
\[
\Delta_{row}^{cof}
:=
\limsup_{(N,j)}\sup_{e,\zeta}\Delta_{row}^{N,j}(e,\zeta).
\]

### Theorem 15.2: Row-Identity Dichotomy

For every retained template ladder, exactly one of the following holds:

1. \(\Delta_{row}^{cof}=0\), in which case the retained rows are a complete
   primitive residual value source up to the printed normalizer intervals;
2. \(\Delta_{row}^{cof}>0\), in which case the retained rows do not source
   `P29-PRIMRES-VAL` without an additional defect theorem.

Proof.

The finite Möbius expansion of Corollary 12.3 is exact.  After the retained
class is chosen, the difference between the true primitive residual and the
retained sum is exactly \(D_{row}^{N,j}\).  If the cofinal endpoint
oscillation of this difference is zero, then all conditional kernels agree
cofinally after the printed normalizer intervals.  If it is positive, there
is a cofinal subsequence and endpoint label on which the omitted defect
changes the conditional log-density by a nonzero amount.  That change cannot
be recovered from the retained rows alone. `square`

### Corollary 15.3: Defect Becomes The Polymer-Value Target

If \(\Delta_{row}^{cof}>0\), then the correct polymer-value target is not the
whole primitive residual again.  It is the defect \(D_{row}^{N,j}\).  A
positive continuation should prove a KP/polymer value bound for \(D_{row}\):
\[
\mathrm{P29\text{-}PRIMRES\text{-}DEFECT\text{-}POLYVAL}(q,a,\epsilon),
\]
meaning an exact same-law polymer expansion for \(D_{row}\), with
\(q<1\), useful activity \(a\), and endpoint conditional error \(\epsilon\).

This is strictly sharper than the original `P29-PRIMRES-POLYVAL`: retained
rows are not charged twice.

We record the exported defect target:
\[
\boxed{\mathrm{P29\text{-}PRIMRES\text{-}DEFECT\text{-}EXPORTED}}.
\]
Equivalently, the plain label is `P29-PRIMRES-DEFECT-EXPORTED`.

## 16. Part-II Verdict

### Theorem 16.1: Current Corpus Does Not Prove Full Primitive Row Identity

The current Papers 20--28 do not prove
`P29-PRIMRES-ROWID-FULL({\mathfrak T},\epsilon)` with \(\epsilon\to0\).

Proof.

Papers 23 and 26 prove formal Möbius existence for the actual residual atoms.
Lemma 12.2 identifies those atoms with the primitive residual atoms.  But
Paper 26 Lemma 12.6 already proves that Möbius inversion is not numerical
population: it does not print the values of \(H_{RPF}^{N,j}\), hence does
not print the values of the atoms.  Paper 26 Proposition 23.3 identifies the
minimal RN ratio with the mixed `CleanRPF` table plus tail, but Lemma 13.2
above proves that mixed crossing data do not determine endpoint one-site
weights or conditional normalizers.  Papers 27 and 28 sharpen consequences
of this absence; they do not add endpoint one-site values, atom values,
normalizer intervals, or a defect tail.

Therefore the full primitive row identity remains unsourced by the current
corpus. `square`

We record:
\[
\boxed{\mathrm{P29\text{-}PRIMRES\text{-}ROWID\text{-}FULL\text{-}GAP}}.
\]
Equivalently, the plain label is `P29-PRIMRES-ROWID-FULL-GAP`.

### Corollary 16.2: What Part II Adds

Part II does prove something new and useful:

1. primitive residual atoms and literal RPF atoms are the same nonconstant
   Möbius atoms;
2. clean crossing rows alone are insufficient because endpoint one-site
   terms affect normalization;
3. the correct positive row theorem is `P29-PRIMRES-ROWID-FULL`;
4. failure of that theorem exports the sharper defect target
   `P29-PRIMRES-DEFECT-POLYVAL`.

Thus Paper 29 has now sourced the algebraic primitive residual identity and
isolated the exact value defect.  It has not sourced the missing values
themselves.

## 17. Part III: Maximal Retention And The Defect-Value Fork

Part II exported the defect
\[
D_{row}^{N,j}
=
h_{prim}^{N,j}
-h_{prim}^{N,j}(o)
-\sum_{A\in{\mathcal C}_{ret}^{N,j}}\Psi_A^{N,j}.
\]
We now sharpen the fork.  To avoid double charging, the retained class should
be chosen as large as the current finite ledger permits.  Whatever remains is
the only legitimate target for a new polymer-value theorem.

### Definition 17.1: Maximal Licensed Retained Class

For each finite endpoint template, let
\({\mathcal C}_{ret,max}^{N,j}\) be the union of the following atom classes:

1. atoms already proved identically zero by structural endpoint
   classification;
2. exact `BC/CE` and central-entry rows already divided out or licensed
   before the RPF slot;
3. endpoint one-site atoms, but only when their same-law value intervals and
   normalizer contribution are printed;
4. clean crossing atoms, but only when their same-law value intervals are
   printed;
5. any finite atom row whose contribution is supplied with a rigorous
   interval under the actual adaptive `SEL2` pushed-forward scalar law.

The word "licensed" is essential.  A finite label belongs to
\({\mathcal C}_{ret,max}^{N,j}\) only when the corresponding same-law value
or interval is available.  A merely named row remains outside the retained
value class.

Define the maximal primitive defect
\[
D_{max}^{N,j}
:=
h_{prim}^{N,j}
-h_{prim}^{N,j}(o)
-\sum_{A\in{\mathcal C}_{ret,max}^{N,j}}\Psi_A^{N,j}.
\]

### Lemma 17.2: Maximal Retention Is No-Double-Charge

Any positive source theorem for \(D_{max}^{N,j}\) can be combined with the
retained finite rows without double charging a contribution already licensed
by Papers 23--29.

Proof.

The retained class is defined by set subtraction from the exact Möbius atom
identity of Corollary 12.3.  Each atom is either retained with a value
certificate or left inside \(D_{max}\).  The two classes are disjoint, and
their sum reconstructs the primitive residual.  Hence a later estimate on
\(D_{max}\) charges only unretained terms. `square`

### Corollary 17.3: The Real New Positive Target

The strongest Paper-29 continuation is not a value theorem for the whole
primitive residual.  It is the defect theorem
\[
\mathrm{P29\text{-}PRIMRES\text{-}DEFECT\text{-}POLYVAL}
(q,a,\epsilon;{\mathcal C}_{ret,max}).
\]

If this fails, the only honest alternatives are a defect lower-floor theorem,
a signed/bridge theorem, or leaving adaptive Branch A.

## 18. Defect Polymer-Value Source

### Definition 18.1: Same-Law Defect Polymer Value Theorem

`P29-PRIMRES-DEFECT-POLYVAL(q,a,epsilon;Cret)` asserts that, cofinally, the
defect \(D_{row}^{N,j}\) associated to the retained class \(Cret\) admits an
exact same-law connected polymer expansion
\[
D_{row}^{N,j}(\omega)
=
\sum_{\Gamma\ {\rm conn}} W_\Gamma^{N,j}(\omega_\Gamma)
+R_{\rm def}^{N,j}(\omega),
\]
where:

1. every activity \(W_\Gamma^{N,j}\) is a finite scalar function of the
   actual adaptive pushed-forward records;
2. the weighted activity norm satisfies
   \[
   \sup_x\sum_{\Gamma\ni x}
   \|W_\Gamma^{N,j}\|_{\rm osc}e^{a|\Gamma|}
   \le q<1;
   \]
3. the endpoint conditional oscillation of the remainder obeys
   \[
   \sup_{e,\zeta}\operatorname{osc}_{u,v}
   R_{\rm def}^{N,j}(u,v\mid\zeta)\le\epsilon;
   \]
4. the retained class \(Cret\) includes its printed value intervals and
   normalizer intervals.

This theorem is same-law.  It does not import a heat-kernel law, a continuum
Yang-Mills measure, a Wilson-loop area law, or a hidden Markov subprocess.

### Lemma 18.2: Defect Polymer Values Source Full Primitive Values

Assume:

1. \(Cret={\mathcal C}_{ret,max}\) is value-populated;
2. `P29-PRIMRES-DEFECT-POLYVAL(q,a,epsilon;Cret)` holds with \(q<1\);
3. \(\epsilon\to0\) cofinally;
4. the endpoint normalizer intervals are bounded away from zero.

Then `P29-PRIMRES-VAL({\mathfrak T},C\epsilon)` holds after possibly
enlarging \(C\) by the finite KP constant determined by \(q,a\) and the
template degree.

Proof.

The primitive residual splits exactly into the retained valued rows plus the
defect.  The retained rows are finite intervals.  The polymer theorem gives
an absolutely convergent connected expansion for the defect and a uniform
oscillation remainder.  The KP bound controls the sum of all defect
activities touching a finite endpoint battery by a finite constant depending
only on \(q,a\) and the local graph degree.  Finite exponentiation and
normalization are locally Lipschitz once normalizers are bounded away from
zero.  Thus the conditional primitive residual values are populated with an
error \(C\epsilon\). `square`

### Corollary 18.3: Defect Polymer Values Reopen Low-Mode Spectral Closure

If the hypotheses of Lemma 18.2 hold and the resulting same-law Peter-Weyl
tail is small enough for the Paper-28 spectral-tail margin, then the
Paper-29 low-mode spectral route is reduced to finite arithmetic.

Proof.

Lemma 18.2 gives `P29-PRIMRES-VAL`.  Lemma 6.2 populates low-mode entries,
and Corollary 6.3 gives the spectral-tail comparison. `square`

## 19. Current-Corpus Defect-KP Audit

### Proposition 19.1: Current Corpus Does Not Prove Defect Polymer Values

The current Papers 20--28 do not prove
`P29-PRIMRES-DEFECT-POLYVAL(q,a,epsilon;Cret)` in a closing range for any
retained class strong enough to populate the Paper-29 low-mode entries.

Proof.

Paper 23 defines the actual-law polymer/KP route
`P23-RPF-POLY-ACT` and `P23-RPF-ACTUAL-KP(q,a)` and proves the positive
implication from a same-law KP certificate.  It does not print the actual
activity values.  Paper 26 imports the formal Möbius atom identity and proves
that atom existence is not value population.  Paper 27 proves the
RN-MIXAMP smallness/floor trichotomy but supplies neither the smallness
values nor the lower floor.  Paper 28 defines the spectral-tail operator but
does not supply a strict low-mode gap or tail.  Sections 12--18 of the
present paper identify the defect precisely, but do not create its same-law
cumulants, activity values, Dobrushin influence matrix, or KP norm.

Therefore the defect-polymer route is a valid positive route, but it is not
proved by the current corpus. `square`

We record:
\[
\boxed{\mathrm{P29\text{-}PRIMRES\text{-}DEFECT\text{-}POLYVAL\text{-}GAP}}.
\]
Equivalently, the plain label is
`P29-PRIMRES-DEFECT-POLYVAL-GAP`.

### Corollary 19.2: Dobrushin Is The Sharpest Finite Sufficient Test

A finite sufficient test for the defect-polymer theorem is the same-law
defect Dobrushin certificate
\[
\mathrm{P29\text{-}PRIMRES\text{-}DEFECT\text{-}DOB}(q,a),
\]
defined by the weighted conditional influence matrix of the defect records
inside the actual adaptive pushed-forward law.  If this influence norm is
\(<1\), the finite Dobrushin-Shlosman implication used in Paper 23 sources
the defect KP theorem.

The current corpus does not print this matrix.

## 20. Lower-Floor Alternative

If defect smallness fails, the productive opposite target is not merely
"large defect."  It must be a lower floor strong enough to falsify adaptive
Branch A.

### Definition 20.1: Defect Lower-Floor Source

`P29-PRIMRES-DEFECT-FLOOR(M_*)` asserts that the same-law defect contribution
forces the actual RPF predebit to satisfy
\[
\overline\Lambda_{13}^{RPF}\ge M_*,
\]
where \(M_*\) is the loss threshold isolated in Papers 23, 26, and 27.

Equivalently, the defect cannot be absorbed by any retained finite row,
defect-polymer smallness theorem, signed/bridge damping theorem, or
same-law tail certificate in the closing range.

### Lemma 20.2: Defect Floor Falsifies Adaptive Branch A After Route Failure

If all positive Branch-A routes retained in Papers 25--29 fail and
`P29-PRIMRES-DEFECT-FLOOR(M_*)` holds, then adaptive Branch A is falsified.

Proof.

The positive routes are sufficient routes for driving the actual RPF
predebit below the loss threshold.  A same-law lower floor at or above
\(M_*\) gives the opposite inequality for the same predebit.  Once the
positive routes fail, the lower floor is exactly the Paper-27 falsification
format applied to the sharper defect object. `square`

### Proposition 20.3: Current Corpus Does Not Prove The Defect Floor

The current Papers 20--28 do not prove
`P29-PRIMRES-DEFECT-FLOOR(M_*)`.

Proof.

Paper 27 proves that the existing corpus does not prove the broader lower
floor \(\overline\Lambda_{13}^{RPF}\ge M_*\).  The present defect object is
more specific, not easier: it requires showing that the unretained part of
the primitive residual alone forces the threshold after all licensed retained
rows are removed.  No paper prints such a same-law lower bound, no paper
prints the defect distribution, and no paper proves that the defect survives
all signed/bridge or normalization cancellations. `square`

We record:
\[
\boxed{\mathrm{P29\text{-}PRIMRES\text{-}DEFECT\text{-}FLOOR\text{-}GAP}}.
\]
Equivalently, the plain label is
`P29-PRIMRES-DEFECT-FLOOR-GAP`.

## 21. Part-III Five-Step Verdict

### Theorem 21.1: The Defect Fork Is Fully Reduced

The five-step continuation after Part II is completed:

1. maximal retained rows are defined by value licensing, not by labels;
2. the primitive defect \(D_{max}\) is the no-double-charge remainder;
3. defect polymer values would source primitive residual values and reopen
   low-mode spectral closure, conditional on the common same-law tail;
4. the current corpus does not prove the defect-polymer theorem;
5. the current corpus also does not prove the opposite defect lower floor.

Proof.

Items 1--2 are Definitions 17.1 and Lemma 17.2.  Item 3 is Lemma 18.2 and
Corollary 18.3.  Item 4 is Proposition 19.1.  Item 5 is Proposition 20.3.
`square`

The completed Part-III labels are
\[
\begin{gathered}
\mathrm{P29\text{-}PRIMRES\text{-}DEFECT\text{-}POLYVAL\text{-}GAP},\\
\mathrm{P29\text{-}PRIMRES\text{-}DEFECT\text{-}FLOOR\text{-}GAP}.
\end{gathered}
\]

### Corollary 21.2: Exact Next Theorem After Paper 29

After Part III, the next theorem must be one of:

1. `P29-PRIMRES-DEFECT-DOB(q,a)` or another proof of
   `P29-PRIMRES-DEFECT-POLYVAL(q,a,epsilon;Cret)`;
2. `P29-PRIMRES-DEFECT-FLOOR(M_*)`;
3. a direct signed/bridge amplitude theorem on the actual same-law mixed
   object;
4. a same-law Peter-Weyl tail theorem plus populated low-mode values;
5. exit from adaptive Branch A.

More finite labels remain irrelevant unless they carry one of those value
theorems.

## 22. Part IV: Defect Dobrushin Records

We now execute the first option in Corollary 21.2 while keeping the work
inside Paper 29.  The goal is to decide how far the finite Dobrushin route
can go on the defect object itself.

### Definition 22.1: Defect Record Battery

Let \({\mathcal C}_{ret,max}^{N,j}\) be the maximal value-licensed retained
class of Definition 17.1, and let
\[
D_{max}^{N,j}
=
h_{prim}^{N,j}
-h_{prim}^{N,j}(o)
-\sum_{A\in{\mathcal C}_{ret,max}^{N,j}}\Psi_A^{N,j}.
\]

The defect record battery \(V_{def}^{N,j}\) is the finite set of adaptive
record coordinates that appear in at least one unretained atom of
\(D_{max}^{N,j}\), together with any endpoint and blanket coordinates needed
to define the corresponding finite conditional laws.  The defect graph
\[
G_{def}^{N,j}=(V_{def}^{N,j},E_{def}^{N,j})
\]
uses the inherited RPF block/collar adjacency.

This is not a new process.  It is a finite sub-battery of the actual adaptive
`SEL2` pushed-forward scalar law after value-licensed rows have been
subtracted.

### Definition 22.2: Defect Conditional Specification

For \(x\in V_{def}^{N,j}\), boundary label \(\zeta_{V_{def}\setminus x}\),
and local value \(s\) in the essential support of the \(x\)-record, define
\[
\mu_{x}^{def,N,j}(s\mid \zeta)
:=
{ \exp D_{max}^{N,j}(s,\zeta)
  \,d\lambda_x(s)
\over
\int \exp D_{max}^{N,j}(s',\zeta)\,d\lambda_x(s') }.
\]
The definition is used only on boundaries for which the denominator is
positive and bounded away from zero by the same essential-support convention
used in Sections 6 and 14.

All objects are finite conditional distributions derived from the same
pushed-forward scalar law.  No hidden Markov subprocess is being composed.

### Definition 22.3: Defect Dobrushin Matrix

For \(x,y\in V_{def}^{N,j}\), define the defect influence
\[
I_{xy}^{def,N,j}
:=
\sup_{\zeta,\zeta':\,\zeta_{V\setminus y}=\zeta'_{V\setminus y}}
\left\|
\mu_x^{def,N,j}(\cdot\mid\zeta)
-
\mu_x^{def,N,j}(\cdot\mid\zeta')
\right\|_{\rm TV}.
\]
Let
\[
\mathfrak D_{def}^{N,j}(a)
:=
\sup_x\sum_y e^{a d_{def}(x,y)}I_{xy}^{def,N,j}.
\]

`P29-PRIMRES-DEFECT-DOB(q,a)` asserts that, cofinally,
\[
\mathfrak D_{def}^{N,j}(a)\le q<1.
\]

This is the sharp finite row test for the defect route.

## 23. Defect Dobrushin Implies Defect KP

### Theorem 23.1: Defect Dobrushin Sources Defect Polymer Values

If `P29-PRIMRES-DEFECT-DOB(q,a)` holds for some \(q<1\), then there exist
\(q'<1\), \(a'>0\), and \(\epsilon_j\to0\) such that
\[
\mathrm{P29\text{-}PRIMRES\text{-}DEFECT\text{-}POLYVAL}
(q',a',\epsilon_j;{\mathcal C}_{ret,max})
\]
holds.

Proof.

For each finite \((N,j)\), the defect specification of Definition 22.2 is a
finite Gibbs specification with log-density \(D_{max}^{N,j}\).  The weighted
Dobrushin bound in Definition 22.3 is exactly the finite same-record
influence criterion used in Paper 23 Theorem 14.5.  A uniform cofinal bound
strictly below one gives exponential decay of connected defect cumulants in
the defect graph metric and an absolutely convergent connected polymer
expansion for the defect logarithmic generating function.  The constants
weaken from \((q,a)\) to \((q',a')\), but strictness is preserved.  Any
finite template truncation error is the remainder \(\epsilon_j\), which tends
to zero along the cofinal battery by the hypothesis that the defect battery
has been enlarged before the selector is evaluated. `square`

### Corollary 23.2: Defect Dobrushin Reopens The Paper-29 Spectral Route

Assume `P29-PRIMRES-DEFECT-DOB(q,a)` and the same normalizer/tail hypotheses
of Lemma 18.2 and Corollary 18.3.  Then the Paper-29 low-mode entries are
populated and the spectral route is reduced to finite arithmetic.

Proof.

Theorem 23.1 gives the defect-polymer theorem.  Lemma 18.2 gives
`P29-PRIMRES-VAL`.  Lemma 6.2 gives low-mode entries.  The final comparison
is Corollary 6.3. `square`

We record the positive implication:
\[
\boxed{
\mathrm{P29\text{-}PRIMRES\text{-}DEFECT\text{-}DOB}
\Longrightarrow
\mathrm{P29\text{-}PRIMRES\text{-}DEFECT\text{-}POLYVAL}
}.
\]

## 24. Current-Corpus Defect Dobrushin Audit

### Proposition 24.1: Current Corpus Does Not Prove Defect Dobrushin

The current Papers 20--28, together with Sections 0--23 of the present
paper, do not prove `P29-PRIMRES-DEFECT-DOB(q,a)` for any \(q<1\).

Proof.

The defect Dobrushin matrix requires the actual finite conditional
distributions \(\mu_x^{def,N,j}(\cdot\mid\zeta)\).  To print those
conditionals one needs the same-law values of \(D_{max}^{N,j}\) or an
equivalent conditional-kernel table.  Papers 23 and 26 provide the formal
Möbius atom identity and the finite worksheet format, but not the values of
the unretained atoms.  Paper 25 proves that a direct actual-law Dobrushin row
would close adaptive Branch A, but also proves that the current corpus does
not supply the row.  Papers 27--28 sharpen the RN-MIXAMP and spectral
consequences, but do not print the defect conditional distributions.
Sections 17--23 define \(D_{max}\) and its Dobrushin test, but definitions do
not supply the numerical influence matrix.

Therefore the defect Dobrushin route is valid but unsourced. `square`

We record:
\[
\boxed{\mathrm{P29\text{-}PRIMRES\text{-}DEFECT\text{-}DOB\text{-}GAP}}.
\]
Equivalently, the plain label is `P29-PRIMRES-DEFECT-DOB-GAP`.

### Corollary 24.2: Failure Of Dobrushin Is Not A Lower Floor

The negation of `P29-PRIMRES-DEFECT-DOB(q,a)` does not by itself prove
`P29-PRIMRES-DEFECT-FLOOR(M_*)`.

Proof.

A Dobrushin norm \(\ge1\) says that this sufficient contraction certificate
fails.  It does not determine the sign, spectral direction, or accumulated
predebit of the defect.  Conditional dependence may be too large for this
criterion while still being cancelled by signed/bridge structure, absorbed by
normalization, or controlled by a different spectral/tail theorem.  A lower
floor requires a same-law witness for the actual RPF predebit, not merely
failure of a sufficient upper-bound test. `square`

## 25. Defect Witness Route

### Definition 25.1: Defect Dobrushin Witness

`P29-PRIMRES-DEFECT-DOBWIT(M_*)` asserts that the defect influence matrix
comes with an oriented cofinal witness chain whose accumulated same-law
predebit contribution is at least \(M_*\).  Concretely, it supplies:

1. a cofinal sequence of defect sites and boundary variations realizing a
   noncontractive influence row;
2. a sign/coherence certificate showing that the variations add rather than
   cancel in the RPF predebit;
3. normalization and tail bounds showing that retained rows, signed/bridge
   cancellations, and Peter-Weyl truncation cannot remove the contribution;
4. the inequality
   \[
   \overline\Lambda_{13}^{RPF}\ge M_*.
   \]

### Lemma 25.2: Defect Witness Implies Defect Floor

`P29-PRIMRES-DEFECT-DOBWIT(M_*)` implies
`P29-PRIMRES-DEFECT-FLOOR(M_*)`.

Proof.

The witness is defined to supply the missing implication from large defect
influence to an actual lower bound on the same-law RPF predebit.  Items 2
and 3 rule out cancellation or absorption by retained rows and tails.  Item
4 is exactly the lower-floor inequality. `square`

### Proposition 25.3: Current Corpus Does Not Prove The Defect Witness

The current Papers 20--28 and the present Paper-29 Sections 0--24 do not
prove `P29-PRIMRES-DEFECT-DOBWIT(M_*)`.

Proof.

Proposition 24.1 proves that the current corpus does not even print the
defect Dobrushin matrix.  A witness requires strictly more data: a realizing
row, sign coherence, normalization survival, and a lower-floor comparison.
Paper 27 proves that the broader lower floor is not supplied by the current
corpus.  Therefore the sharper defect witness is also unsourced. `square`

We record:
\[
\boxed{\mathrm{P29\text{-}PRIMRES\text{-}DEFECT\text{-}DOBWIT\text{-}GAP}}.
\]
Equivalently, the plain label is `P29-PRIMRES-DEFECT-DOBWIT-GAP`.

## 26. Part-IV Verdict

### Theorem 26.1: Defect Dobrushin Campaign Is Settled For The Current Corpus

The defect Dobrushin continuation has the following exact status:

1. `P29-PRIMRES-DEFECT-DOB(q,a)` is a valid same-law finite sufficient test;
2. if it holds with \(q<1\), then the defect-polymer route and hence
   primitive residual value route reopen;
3. the current corpus does not prove it;
4. failure of the Dobrushin test does not imply a lower floor;
5. the stronger defect witness that would imply a lower floor is also not
   proved by the current corpus.

Proof.

Items 1--2 are Definitions 22.2--22.3, Theorem 23.1, and Corollary 23.2.
Item 3 is Proposition 24.1.  Item 4 is Corollary 24.2.  Item 5 is
Proposition 25.3. `square`

The completed Part-IV labels are
\[
\begin{gathered}
\mathrm{P29\text{-}PRIMRES\text{-}DEFECT\text{-}DOB\text{-}GAP},\\
\mathrm{P29\text{-}PRIMRES\text{-}DEFECT\text{-}DOBWIT\text{-}GAP}.
\end{gathered}
\]

### Corollary 26.2: Final Paper-29 Next-Step Ledger

After Part IV, the exact surviving next steps are:

1. print the defect conditional influence matrix and prove
   `P29-PRIMRES-DEFECT-DOB(q,a)` with \(q<1\);
2. print a coherent defect witness proving
   `P29-PRIMRES-DEFECT-DOBWIT(M_*)`, hence the defect floor;
3. bypass the defect route with a direct signed/bridge amplitude theorem;
4. bypass it with direct low-mode entries plus a same-law Peter-Weyl tail;
5. leave adaptive Branch A.

Nothing weaker than same-law values, conditionals, witnesses, or tails moves
the proof.

This completes Paper 29.
