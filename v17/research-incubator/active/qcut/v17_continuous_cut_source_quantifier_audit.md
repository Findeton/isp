# ISP v17 — source and quantifier audit for the continuous cut theorem

**Status:** ACTIVE INCUBATOR / AUTHOR-SIDE AUDIT / NOT INDEPENDENT REVIEW

**Date:** 2026-08-23

**Scientific result awarded:** none
**Authority created:** none

This note attacks the reductions in
`v17_continuous_cut_information_theorem_candidate.md`. The exact primary-source
derivation and retrieved-byte receipts are in
`v17_qcut_primary_source_reconstruction.md`. It does not
freeze a pin, open an official unit, reopen Paper 04B, or authorize any
downstream clock, chronology, spacetime, or gravity work.

---

## 1. Audit decision

The candidate theorem survives, with four binding corrections:

1. the exact message-compression source is Harsha--Jain--McAllester--
   Radhakrishnan (HJMR), not Jain--Radhakrishnan--Sen;
2. the hard ensemble should be the explicit natural distribution used in the
   original \(\alpha\)-Partial Matching proof, not an unnamed Yao witness;
3. the proof must print why the HJMR information cost
   \(I(X,Y:Q)\) reduces to \(I(X:Q)\) despite correlated promised inputs; and
4. admissible sizes must satisfy \(\alpha n\in\mathbb N\), with all error
   margins fixed independently of \(n\).

The exact source reconstruction additionally verifies that HJMR's information
cost is the external quantity \(I(XY;Q)\), not the receiver-conditioned
internal quantity \(I(X;Q\mid Y)\), and that Section 3.3 of the Partial
Matching source fixes the natural ensemble itself. After these repairs, no
counterexample was found to the following restricted
claim:

> Under the natural hard \(\alpha\)-Partial Matching ensemble, every
> standard-Borel ordinary-positive intermediate variable that is prepared
> independently of the later reader choice, approximately screens the
> preparation from every registered reader, and retains a fixed bounded-error
> advantage must carry
> \(I(X:\Lambda\mid S)=\Omega(\sqrt{n/\alpha})\).

This is not yet an accepted theorem. It remains an author-side reconstruction
requiring independent mathematical review.

---

## 2. Primary-source chain

### 2.1 Natural hard task

Gavinsky, Kempe, Kerenidis, Raz, and de Wolf define the
\(\alpha\)-Partial Matching task for \(0<\alpha\le1/4\):

- \(X\) is uniform on \(\{0,1\}^n\);
- \(\mathsf M\) is uniform on \(\alpha n\)-edge matchings;
- \(B\) is a fair independent bit;
- \(W=\mathsf M X\oplus B^{\alpha n}\);
- Bob receives \(Y=(\mathsf M,W)\) and must output \(B\).

Their Section 3.3 proves the classical distributional lower bound on this
specific ensemble, not merely the existence of some hard distribution. For
every fixed error threshold \(\delta_*<1/2\), the proof yields

$$
D^{\pi^{\rm nat}_{n,\alpha}}_{\delta_*}(f_{n,\alpha})
=
\Omega_{\delta_*}\!\left(\sqrt{\frac n\alpha}\right).
$$

The same paper constructs a quantum one-way protocol using
\(O(1/\alpha)\) copies of an \(n\)-dimensional phase state, hence
\(O(\log(n)/\alpha)\) qubits.

Versioned primary source:
<https://arxiv.org/abs/quant-ph/0611209v3>.

### 2.2 Exact message-compression lemma

HJMR Definition V.1 defines

$$
IC^\pi(\Pi)=I(XY;T_\Pi).
$$

HJMR Lemma V.3 then states, for any possibly correlated distribution \(\pi\) on
\((X,Y)\), any \(k\)-round private-coin protocol, and any \(\Delta>0\),

$$
D^\pi_{e+\Delta}(f)
\le
\frac{2\,IC^{\pi,k}_{e}(f)+O(k)}{\Delta}.
$$

At one round, a particular finite-message protocol of error at most \(e\) is
one competitor in the defining minimum, so

$$
IC^{\pi,1}_e(f)\le I(XY;Q).
$$

Consequently there is a universal constant \(C_{\rm H}\ge0\) such that

$$
D^\pi_{e+\Delta}(f)
\le
\frac{2I(X,Y:Q)+C_{\rm H}}{\Delta}.
$$

The route is exact where needed:

1. their Result 1 remotely simulates the message distribution using public
   randomness with expected communication controlled by mutual information;
2. Markov's inequality truncates long messages at probability cost
   \(\Delta\); and
3. fixing the random strings gives a deterministic distributional protocol
   with worst-case message length and average error at most \(e+\Delta\).

HJMR explicitly state that the same proof applies to relations. The partial
matching promise can therefore be treated directly as a relation, or as any
arbitrary total extension with \(\pi^{\rm nat}\) supported on promised inputs.
No off-promise accuracy is used.

Primary source:
<https://doi.org/10.1109/TIT.2009.2034824>.

The exact retrieved-source hashes, source total-variation convention, and
constant-error derivation are recorded in
`v17_qcut_primary_source_reconstruction.md`. No secondary application is a
load-bearing premise.

---

## 3. Correlated-input identity

The natural promise makes \(X\) and \(Y\) correlated. It would therefore be
wrong to replace \(I(X,Y:Q)\) by \(I(X:Q)\) without a protocol identity.

In the induced protocol, Alice samples

$$
S\sim\nu,
\qquad
\Lambda\sim\mu_{X,S},
\qquad
Q=q(S,\Lambda),
$$

with \(S\perp(X,Y)\). Neither sampling kernel depends on Bob's input. Hence

$$
Q\perp Y\mid X.
$$

The chain rule then gives

$$
I(X,Y:Q)
=I(X:Q)+I(Y:Q\mid X)
=I(X:Q).
$$

This identity fails if preparation depends on the later reader setting. Such a
model is a separately charged retrocausal, measurement-dependent, or
whole-program branch; it is not covered by the theorem.

---

## 4. Quantifier reconstruction

The theorem requires the order

$$
\forall n\in\mathcal N_\alpha
\quad
\exists\pi^{\rm nat}_{n,\alpha}
\quad
\forall\mathcal R\in\mathfrak R^+_{n,\alpha},
$$

where \(\mathcal N_\alpha=\{n:\alpha n\in\mathbb N\}\), the distribution is
the explicit natural ensemble above, and \(\mathfrak R^+_{n,\alpha}\) is the
frozen positive-cut class. Because \(\pi^{\rm nat}\) depends only on the task,
the same distribution tests every realizer.

The following weaker, post-hoc order is prohibited:

$$
\forall\mathcal R\;\exists\pi_{\mathcal R}.
$$

The constants \(\alpha,\delta,\varepsilon_{\rm fac},\eta,\delta_*\), and the
compression slack \(\Delta\) are frozen independently of \(n\), with

$$
e:=\delta+\varepsilon_{\rm fac}+\eta,
\qquad
0<\Delta<\delta_*-e.
$$

No asymptotic lower bound survives if the remaining gap is allowed to vanish
without its dependence being tracked.

---

## 5. Continuous-carrier reduction

Let \(\mathcal E\) be a standard-Borel total carrier with Borel projection
\(p:\mathcal E\to\mathcal S\), let \(\Lambda\in\mathcal E\) obey
\(p(\Lambda)=S\), and require every binary response probability

$$
e\longmapsto\xi_y(1\mid e)
$$

to be Borel measurable. Bob's registered input set is finite at each \(n\).
The complete response map into the finite product

$$
r:\mathcal E
\longrightarrow
[0,1]^{|\mathcal Y_n|}
$$

is therefore Borel. Coordinatewise finite-grid quantization produces a finite
Borel label \(Q_\eta\) and changes every registered binary response by at most
\(\eta\). No topological compactness, density, or finite ontic cardinality is
used.

Since \(Q_\eta\) is a deterministic measurable function of \((S,\Lambda)\),

$$
I(X:Q_\eta)
\le I(X:S,\Lambda)
=I(X:\Lambda\mid S),
$$

where the last equality uses \(S\perp X\). This remains valid for an
uncountable carrier and extended-valued mutual information.

---

## 6. Error reconstruction

For a promised input, let the actual model have task error at most \(\delta\),
let the screened prediction differ from the actual binary output law by at
most \(\varepsilon_{\rm fac}\) in total variation, and let quantization change
the response probability by at most \(\eta\). The induced protocol then has
average and worst-case task error at most

$$
e=\delta+\varepsilon_{\rm fac}+\eta.
$$

HJMR compression at slack \(\Delta\) gives a deterministic protocol at error
\(e+\Delta<\delta_*\). Error monotonicity yields

$$
D^{\pi^{\rm nat}}_{e+\Delta}
\ge D^{\pi^{\rm nat}}_{\delta_*}
=\Omega(\sqrt{n/\alpha}).
$$

Combining this with the HJMR upper bound forces

$$
I(X:Q_\eta)=\Omega(\sqrt{n/\alpha}),
$$

and data processing transfers the bound to
\(I(X:\Lambda\mid S)\).

---

## 7. Attempted countermodels

### C1 — one exact real

Encode all of \(X\) into one real coordinate. This defeats coordinate counting
but not mutual information. If the coordinate remains sufficient for every
reader, its information under the hard ensemble is charged.

**Outcome:** does not defeat the theorem.

### C2 — arbitrarily large independent public randomness

Let response power reside mostly in \(S\), with \(S\perp(X,Y)\). Alice samples
\(S\) privately and sends the quantized complete response label. HJMR
compression removes input-independent entropy from the information charge.

**Outcome:** does not defeat the theorem; computational and law-description
cost remain unbounded and unclaimed.

### C3 — correlate the public seed with Bob's setting

Let \(S\) help choose \(Y\). The internalization and free-setting premise no
longer hold.

**Outcome:** genuine premise escape; classify as measurement dependence or a
common-boundary mechanism.

### C4 — future-dependent preparation

Use \(\mu_{x,y}\) rather than \(\mu_x\). Then \(Q\not\perp Y\mid X\), so the
one-way reduction fails.

**Outcome:** genuine premise escape; classify as retrocausal or whole-program
dependence.

### C5 — nonmeasurable response assignment

Choose a nonmeasurable response table so no Borel response-vector map exists.

**Outcome:** not an admitted stochastic law; probabilities and conditional
mutual information are not operationally defined.

### C6 — vanishing success margin

Let \(\delta_*-(\delta+\varepsilon_{\rm fac}+\eta)\to0\) with \(n\).

**Outcome:** fixed-constant theorem does not apply. Any varying-margin result
must retain the explicit \(\Delta\) dependence.

### C7 — genuinely indivisible whole-history law

Supply no positive future-sufficient cut variable at all.

**Outcome:** outside the theorem and scientifically live. This is the intended
input to the later uniform indivisible-law classification gate.

### C8 — nonpositive or noncommutative boundary

Retain amplitudes, operators, signed data, or quasiprobability structure at
the cut.

**Outcome:** outside the ordinary-positive screening class. The result locates
the classical information burden; it does not rule out compact phase-complete
boundaries.

---

## 8. Remaining independent-review duties

An independent review must still reconstruct:

1. the author reconstruction of the constant-error natural-distribution lower
   bound, including the source's unnormalized total-variation convention;
2. the exact one-round specialization of HJMR Lemma V.3, including its
   external information definition, additive \(O(1)\), and truncation
   convention;
3. standard-Borel measurability for a bundled carrier rather than a fixed
   product carrier;
4. the conditional-independence identity for every admitted preparation
   kernel;
5. uniform versus average error transfer; and
6. whether Paper 01's accepted positive-history interface ever asserts this
   positive screening property, or merely a whole-history representation.

The final item is a scope firewall: failure of a screened cut cannot be
reported as failure of positive histories or of Barandes-style indivisibility.

---

## 9. Root disposition

```text
SOURCE CHAIN:                         RECONSTRUCTED / AUTHOR-SIDE PASS
NATURAL HARD DISTRIBUTION:            EXPLICIT / MODEL-INDEPENDENT
CORRELATED-INPUT INFORMATION IDENTITY: PROVED UNDER ONE-WAY PREPARATION
CONTINUOUS RESPONSE QUANTIZATION:      PROVISIONALLY PASS
APPROXIMATE ERROR ACCOUNTING:          PROVISIONALLY PASS
COMPUTATIONAL EFFICIENCY:              NOT CLAIMED
PHYSICAL MEMORY / ENERGY COST:         NOT CLAIMED
INDIVISIBLE-HISTORY NO-GO:             NOT CLAIMED
ONTOLOGY SELECTION:                    NOT CLAIMED
OFFICIAL PIN READINESS:                PENDING ACTIVE-PIN HASH AND ROOT REAUDIT
```

The active candidate pin already fixes \(\alpha=1/4\), the natural hard
ensemble, the positive-cut class, fixed error slack, and all premise-escape
branches. It must be rehashed only after the active theorem, this audit, and
the source reconstruction pass the final author-side consistency audit. Later
review can be independent verification but not blind discovery.
