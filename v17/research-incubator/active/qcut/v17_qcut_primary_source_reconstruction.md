# ISP v17 — Q-Cut primary-source reconstruction

**Status:** ACTIVE INCUBATOR / AUTHOR-SIDE SOURCE RECONSTRUCTION / NOT INDEPENDENT REVIEW  
**Date:** 2026-08-23  
**Scientific result awarded:** none  
**Pin frozen:** no

This note reconstructs the two external mathematical inputs used by the Q-Cut
candidate. It exists because an asymptotic separation is only as sound as the
information quantity, hard distribution, error convention, and quantifier
order imported from its sources.

The reconstruction changes one author-side diagnosis: the candidate's use of
external information (I(XY;Q)) is correct. Harsha--Jain--McAllester--
Radhakrishnan (HJMR) do not use (I(X;Q\mid Y)) in their Definition V.1. They
define the information cost of the transcript (M) to be (I(XY;M)), and
their Lemma V.3 compresses exactly that quantity.

---

## 1. Exact source receipts

### S1 — message compression

Prahladh Harsha, Rahul Jain, David McAllester, and Jaikumar
Radhakrishnan, *The Communication Complexity of Correlation*, IEEE
Transactions on Information Theory **56**(1), 438--449 (2010),
DOI `10.1109/TIT.2009.2034824`.

- Author-hosted PDF:
  <https://www.tcs.tifr.res.in/~prahladh/papers/HJMR/HJMR2010.pdf>
- Retrieved: 2026-08-23
- PDF size: 328165 bytes
- SHA-256:
  `f049e5c2ee3c16f3096ccc6b9bf4a28f27ac1fe0acd44da411eb7c081ab05222`
- Bound locations: Definition V.1, Proposition V.2, Lemma V.3 and its
  proof.

### S2 — natural hard Partial Matching distribution

Dmytro Gavinsky, Julia Kempe, Iordanis Kerenidis, Ran Raz, and Ronald
de Wolf, *Exponential separations for one-way quantum communication
complexity, with applications to cryptography*, arXiv
`quant-ph/0611209v3`, subsequently STOC 2007.

- Versioned PDF:
  <https://arxiv.org/pdf/quant-ph/0611209v3>
- Version landing page:
  <https://arxiv.org/abs/quant-ph/0611209v3>
- Retrieved: 2026-08-23
- PDF size: 229425 bytes
- Retrieved-PDF SHA-256:
  `6e623c66dae1406308d28edfdc16693f8c0e760196a17ff91a30901e15a0c783`
- Bound locations: Theorem 1, Section 3.3, and the quantum upper-bound
  construction. The journal-layout copy numbers the headline results
  Theorems 1.1 and 1.2; the arXiv v3 text numbers them Theorems 1 and 2.

The PDFs themselves are not copied into the repository. The receipts bind the
exact retrieved bytes without republishing the papers.

---

## 2. The pinned operational task

For (0<\alpha\le 1/4) with (\alpha n\in\mathbb N), let

$$
X\sim\operatorname{Unif}(\{0,1\}^n),
$$

let (M) be independent and uniform over all matchings with (\alpha n)
disjoint edges, and define the edge-parity vector

$$
Z=MX\in\{0,1\}^{\alpha n}.
$$

Let (B\sim\operatorname{Bernoulli}(1/2)) independently and set

$$
W=Z\oplus B^{\alpha n}.
$$

Alice receives (X). Bob receives

$$
Y=(M,W)
$$

and must output (B). Write (\pi_{n,\alpha}^{\rm nat}) for this joint
distribution. It is supported entirely on the promise set of
(\alpha\)-Partial Matching.

This is not a Yao distribution inferred after looking at a candidate model.
Section 3.3 of S2 explicitly chooses uniform (X), uniform (M), and the fair
choice between (W=Z) and (W=\bar Z). The same distribution therefore tests
every Q-Cut realizer.

---

## 3. Reconstruction of the classical lower bound

### 3.1 Source convention

S2 writes

$$
\|p-q\|_{\rm tvd}=\sum_z |p(z)-q(z)|,
$$

which is twice the modern normalized total-variation distance. Under this
source convention, the optimal success probability for distinguishing equally
likely (p) and (q) from one sample is

$$
\frac12+\frac14\|p-q\|_{\rm tvd}.
$$

All constants below use the source convention until the final communication
statement. No factor of two is silently transferred to the Q-Cut screening
error.

### 3.2 Source theorem

S2 proves that there is a universal (\gamma>0) such that, for any set
(A\subseteq\{0,1\}^n) satisfying

$$
|A|\ge 2^{n-c}
$$

and for (X) uniform on (A), the distribution (p_M) of (MX) obeys

$$
\mathbb E_M\|p_M-U\|_{\rm tvd}\le \varepsilon_s
$$

whenever

$$
c\le \gamma\varepsilon_s\sqrt{\frac n\alpha}.
$$

Here (\varepsilon_s) is a source proof parameter, not a protocol error.

### 3.3 Deterministic protocol under the natural distribution

Let a deterministic one-way protocol send at most

$$
C=\gamma\varepsilon_s\sqrt{\frac n\alpha}
  -\log_2(1/\varepsilon_s)
$$

bits. Its message partitions (\{0,1\}^n) into cells. Under uniform (X),
the probability that the occupied cell has size smaller than

$$
2^{n-\gamma\varepsilon_s\sqrt{n/\alpha}}
$$

is at most (\varepsilon_s). Conditional on a larger cell, the source theorem
and Markov's inequality imply that, except for a
(\sqrt{\varepsilon_s}) fraction of matchings,

$$
\|p_M-U\|_{\rm tvd}\le\sqrt{\varepsilon_s}.
$$

Complementing every parity string preserves the uniform law, so on this good
event

$$
\|p_M-\bar p_M\|_{\rm tvd}
\le 2\sqrt{\varepsilon_s}.
$$

The protocol's total advantage over a fair guess is consequently at most

$$
a(\varepsilon_s)
=
\varepsilon_s
+\sqrt{\varepsilon_s}
+\frac12\sqrt{\varepsilon_s}
=
\varepsilon_s+\frac32\sqrt{\varepsilon_s}.
$$

This reproduces the Section 3.3 ledger rather than quoting only its headline
worst-case theorem.

### 3.4 Every fixed error below one half

Fix any target distributional error (\delta_*<1/2). Choose a constant
(\varepsilon_s>0), independently of (n), such that

$$
a(\varepsilon_s)<\frac12-\delta_*.
$$

Then every deterministic protocol with communication at most (C) has error
strictly larger than (\delta_*) under the single natural distribution. Hence

$$
D^{\pi_{n,\alpha}^{\rm nat}}_{\delta_*}(f_{n,\alpha})
\ge
\gamma\varepsilon_s\sqrt{\frac n\alpha}
-\log_2(1/\varepsilon_s),
$$

up to the harmless integer rounding of a message length. For sufficiently
large (n),

$$
D^{\pi_{n,\alpha}^{\rm nat}}_{\delta_*}(f_{n,\alpha})
=
\Omega_{\delta_*}\!\left(\sqrt{\frac n\alpha}\right).
$$

For the Q-Cut constants, take (\alpha=1/4), (\delta_*=1/3), and the
source's displayed choice (\varepsilon_s=1/1000). Indeed,

$$
\frac1{1000}+\frac32\sqrt{\frac1{1000}}
<\frac16.
$$

Thus there are (c_{\rm PM}>0) and (n_{\rm PM}) such that

$$
D^{\pi_n^{\rm nat}}_{1/3}(f_n)
\ge c_{\rm PM}\sqrt n
\qquad(n\ge n_{\rm PM}).
$$

No candidate-dependent hard distribution has entered.

---

## 4. Reconstruction of HJMR message compression

### 4.1 The information quantity is external

For a private-coin protocol (\Pi) with input pair ((X,Y)\sim\mu) and
message transcript (T), HJMR Definition V.1 sets

$$
IC^\mu(\Pi)=I(XY;T).
$$

It then minimizes this quantity over (k)-round protocols of distributional
error at most (e):

$$
IC^{\mu,k}_e(f)
=
\min_{\Pi:\,\operatorname{err}_\mu(\Pi)\le e} I(XY;T_\Pi).
$$

This is not the receiver-conditioned internal information
(I(X;T\mid Y)). Replacing HJMR's printed quantity by that different notion
would be a source error.

### 4.2 Lemma V.3

For every finite input distribution (\mu), not necessarily a product, every
(e,\Delta>0), and every (k), HJMR prove

$$
D^{\mu,k}_{e+\Delta}(f)
\le
\frac{2IC^{\mu,k}_e(f)+O(k)}{\Delta}.
$$

Their proof remotely generates each message with its exact distribution,
obtaining expected communication (2I(XY;T)+O(k)); truncates by Markov's
inequality at additional error (\Delta); and fixes the random strings to
obtain a deterministic distributional protocol. They also state that the
argument applies to relations.

For a particular one-way message (Q) whose induced protocol has error at
most (e), minimization gives

$$
IC^{\mu,1}_e(f)\le I(XY;Q).
$$

Therefore a universal constant (C_{\rm H}\) exists such that

$$
D^{\mu,1}_{e+\Delta}(f)
\le
\frac{2I(XY;Q)+C_{\rm H}}{\Delta}.
$$

The unknown numerical value of (C_{\rm H}) affects only the eventual
finite-(n) threshold, not the asymptotic exponent. It must not be reported as
zero or as an explicit source constant.

### 4.3 Promise handling

The natural distribution is supported on valid Partial Matching inputs. One
may either use HJMR's stated relation extension or choose an arbitrary total
function extension off the promise. Distributional error and information cost
under (\pi^{\rm nat}) never inspect the off-promise values. No worst-case
off-promise correctness is imported.

---

## 5. The correlated-input identity

In Q-Cut, Alice samples the finite quantized message (Q_\eta) from (X) and
Alice-side randomness only. Bob's full input (Y=(M,W)) is correlated with
(X), but the preparation kernel satisfies

$$
P(Q_\eta=q\mid X=x,Y=y)
=
P(Q_\eta=q\mid X=x).
$$

Equivalently,

$$
Q_\eta\perp Y\mid X.
$$

The chain rule now gives the exact identity

$$
I(XY;Q_\eta)
=
I(X;Q_\eta)+I(Y;Q_\eta\mid X)
=
I(X;Q_\eta).
$$

This identity would fail for future-dependent preparation, measurement
dependence, a whole-program compiler, or any protocol in which the message
kernel actually depends on (Y). Those are named outside branches, not hidden
exceptions.

---

## 6. Complete Q-Cut inequality with pinned constants

The candidate freezes

$$
\delta_{\rm act}=\frac1{10},
\qquad
\varepsilon_{\rm fac}=\frac1{40},
\qquad
\eta=\frac1{40}.
$$

The finite response-vector protocol therefore has error at most

$$
e
=
\delta_{\rm act}+\varepsilon_{\rm fac}+\eta
=
\frac3{20}.
$$

Choose the HJMR truncation slack

$$
\Delta=\frac1{20}.
$$

Then (e+\Delta=1/5), and Sections 4--5 give

$$
D^{\pi_n^{\rm nat}}_{1/5}(f_n)
\le
40I(X;Q_\eta)+20C_{\rm H}.
$$

Error monotonicity and Section 3 give, for (n\ge n_{\rm PM}),

$$
D^{\pi_n^{\rm nat}}_{1/5}(f_n)
\ge
D^{\pi_n^{\rm nat}}_{1/3}(f_n)
\ge
c_{\rm PM}\sqrt n.
$$

Hence

$$
I(X;Q_\eta)
\ge
\frac{c_{\rm PM}}{40}\sqrt n-\frac{C_{\rm H}}2.
$$

After increasing the threshold (n_0),

$$
I(X;Q_\eta)
\ge
\frac{c_{\rm PM}}{80}\sqrt n.
$$

If (Q_\eta) is a deterministic finite quantization of ((S,\Lambda)) and
(S\perp X), data processing yields

$$
I(X;Q_\eta)
\le
I(X;S,\Lambda)
=
I(X;\Lambda\mid S).
$$

Therefore

$$
I(X;\Lambda\mid S)=\Omega(\sqrt n).
$$

The source chain proves this only after the candidate's Borel response-vector
quantization and screening-error lemmas are established. Those are internal
Q-Cut obligations, not results imported from S1 or S2.

---

## 7. Quantum comparator check

S2 uses the state

$$
|\psi_x\rangle
=
\frac1{\sqrt n}\sum_{i=1}^n(-1)^{x_i}|i\rangle.
$$

For a matching with (\alpha n) edges, one copy yields a parity on an input
edge with heralded probability (2\alpha). At (\alpha=1/4), three
independent copies all fail with probability (1/8). Guessing (B) fairly
only on that heralded-failure branch gives error

$$
\frac12\cdot\frac18=\frac1{16}<\frac1{10}.
$$

The joint carrier has Hilbert dimension (n^3), so for its cq preparation
ensemble

$$
I(X;Q_{\rm quantum})\le 3\log_2 n.
$$

This is a comparison of a positive future-sufficient cut with a
noncommutative phase-complete carrier on one operational task. It is not a
comparison of total apparatus memory, energy, spacetime volume, precision,
law-description length, or preparation cost.

---

## 8. Novelty boundary

S2 already supplies the Partial Matching quantum/classical separation and its
natural hard distribution. S1 already supplies the message-compression bridge
from external transcript information to bounded communication. Q-Cut does not
claim either ingredient as new, nor does it claim a new empirical prediction.

The candidate contribution, if independently proved and judged worthwhile,
is the foundations-level quantifier transfer:

> every admitted standard-Borel ordinary-positive variable that is prepared
> independently of the later reader choice and approximately screens the
> registered future responses can be reduced to the published one-way task
> and must therefore retain the stated preparation mutual information.

Its additional content is the typed physical interface, continuous-carrier
quantization, and explicit escape ledger for genuinely indivisible
whole-history laws. The asymptotic communication lower bound remains credited
to S2 and the compression theorem to S1.

---

## 9. Source-level verdict

```text
HJMR INFORMATION QUANTITY:          EXTERNAL I(XY;T) / VERIFIED
HJMR NONPRODUCT DISTRIBUTIONS:       ALLOWED / VERIFIED
HJMR PARTICULAR-PROTOCOL USE:       VALID VIA IC MINIMIZATION
HJMR ADDITIVE TERM:                 O(1) AT ONE ROUND / RETAINED
GKKRW NATURAL DISTRIBUTION:          EXPLICIT / VERIFIED
GKKRW CONSTANT-ERROR EXTENSION:      DERIVED WITH SOURCE PARAMETER PRINTED
TOTAL-VARIATION CONVENTION:          TRANSLATED / NO SILENT FACTOR TWO
PROMISE HANDLING:                    DISTRIBUTIONAL SUPPORT / VERIFIED
QUANTUM THREE-COPY ERROR:            1/16 / VERIFIED
INDEPENDENT REVIEW:                  NOT PERFORMED
SCIENTIFIC RESULT:                   NONE
```

The primary-source bridge survives reconstruction. The remaining possible
defeaters are internal: bundled standard-Borel measurability, response-vector
quantization, uniform error transfer, the typing of any proposed physical
realizer into the screening class, and the interpretation of mutual
information as an explanatory rather than automatically material resource.
