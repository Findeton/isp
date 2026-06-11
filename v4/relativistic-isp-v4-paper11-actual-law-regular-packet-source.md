# Relativistic ISP V4 Paper 11: Actual-Law Regular Packet Source Or Floor

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Date: 2026-05-26

Status: Completed actual-law selection framework, primitive route sharpening,
and finite probability-theoretic route exhaustion.

## Abstract

V4 Paper 10 proves that declared smooth compatible source-conditioned
packets lie on the zero side of the residual-minimum problem.  Paper 11 asks
the next and harder question:

$$
\boxed{
\hbox{does the actual finite stochastic matter-geometry law select those
regular smooth-compatible packets and residual-small configurations?}
}
$$

The answer from the current corpus is still not unconditional.  But Paper 11
fully develops the actual-law selection problem and proves the exact finite
transfer theorems needed to move forward.

The central point is that packet minima alone are insufficient.  A packet may
contain residual-small witnesses while the actual conditional law inside that
packet assigns most of its mass to residual-large configurations.  Therefore
the actual target is not merely

$$
a_a^*({\mathfrak D})\to0.
$$

It is actual concentration on regular residual-small configurations:

$$
\boxed{
\mathbb P_a^{act}
\bigl(Q_a\in{\mathsf G}_a(\epsilon_a)\bigr)\to1,
\qquad
\epsilon_a\to0.
}
$$

Paper 11 proves five finite same-law selection routes:

1. two-level packet-plus-conditional-minimizer selection;
2. residual-penalty Gibbs concentration;
3. Radon-Nikodym or relative-entropy transfer from a good reference law;
4. finite Fisher-length source-response transfer;
5. regularity tightness plus residual-moment control.

It also proves the negative route:

$$
\boxed{
\mathrm{V4P11\text{-}ACTUAL\text{-}PACKET\text{-}DUAL\text{-}FLOOR}.
}
$$

If the actual support is dual-separated from residual closure, then the
actual law cannot realize the GR-facing residual-zero sector.

The strongest positive theorem is conditional and exact:

$$
\boxed{
\mathrm{V4P11\text{-}ACTUAL\text{-}GOOD\text{-}CONFIG\text{-}TRANSFER}.
}
$$

Any of the five finite transfer mechanisms proves actual good-configuration
concentration.  The current corpus, however, does not yet source any of the
primitive quantitative inputs: no actual residual-Gibbs identity, no
relative-entropy domination, no short Fisher bridge, no residual-moment
bound, no high-probability residual floor, and no actual-support dual floor
certificate.

The maximal Paper-11 continuation sharpens these possibilities further.  RN
domination is exactly a subcritical log-density or entropy defect relative to
a canonical good reference law.  A short Fisher bridge is exactly
Hellinger/Fisher-Rao closeness.  The moment route is exactly actual
\(L^1\) residual decay plus tail control.  The negative route is best stated
as a high-probability residual floor, with support and convex-dual floors as
stronger certificate variants.

Thus the frontier inside Paper 11 is sharply localized:

$$
\boxed{
\mathrm{V4P11\text{-}PRIMITIVE\text{-}ACTUAL\text{-}PACKET\text{-}ESTIMATE}.
}
$$

## 0. Imports And Discipline

### Import 0.1: Paper-10 Source-Conditioned Packets

Paper 10 defines finite data packets

$$
{\mathfrak D}_a
$$

and conditioned sectors

$$
{\mathcal B}_a({\mathfrak D})
\subset C_a^{tot}.
$$

It proves that declared smooth compatible packets have

$$
a_a^*({\mathfrak D})\to0,
$$

where

$$
a_a^*({\mathfrak D})
:=
\min_{q\in{\mathcal B}_a({\mathfrak D})}{\mathcal A}_a(q).
$$

It also proves a regular compact side decision.

### Import 0.2: Residual Penalty

The residual penalty is

$$
{\mathcal A}_a(q)
:=
\sum_{DD}\|R_{DD,a}^q\|^2
+\sum_{DH}\|R_{DH,a}^q\|^2
+\sum_{HH}\|R_{HH,a}^q\|^2
+\|{\mathcal E}_{cov,a}^q\|^2.
$$

### Barandes Rule 0.3

Paper 11 may use:

1. finite actual probability laws on finite record spaces;
2. finite pushforwards of those laws to packet labels;
3. finite conditional laws inside packets;
4. finite Radon-Nikodym derivatives and relative entropies;
5. finite source-response Fisher lengths;
6. finite dual certificates.

Paper 11 may not use:

1. Einstein equations as primitive selection;
2. continuum action weights unless encoded as finite actual laws;
3. hidden Markov intermediate times inside a whole-slab transition;
4. Hilbert phase as ontology;
5. smooth-packet selection by declaration alone.

The rule is:

$$
\hbox{actual finite probabilities must do the selecting.}
$$

## 1. Actual Law And Packet Pushforward

### Definition 1.1: Actual Total-Record Law

Let

$$
\Omega_a
$$

be the finite total-record space relevant to the Paper-7 residual tests.  It
may be a one-slab, two-slab, or finite whole-process record space, but it is
finite at regulator \(a\).  Let

$$
\mathbb P_a^{act}
$$

be the actual finite probability law on \(\Omega_a\).

### Definition 1.2: Packetization Map

A packetization map is a finite deterministic map

$$
\Pi_a:\Omega_a\to{\mathsf P}_a,
$$

where \({\mathsf P}_a\) is the finite set of source-conditioned packet labels.
For \(Q_a\sim\mathbb P_a^{act}\), define the packet random variable

$$
{\mathfrak D}_a:=\Pi_a(Q_a).
$$

The actual packet law is the pushforward

$$
\nu_a^{act}:=(\Pi_a)_\#\mathbb P_a^{act}.
$$

### Definition 1.3: Actual Conditional Law Inside A Packet

For a packet \(D\in{\mathsf P}_a\) with \(\nu_a^{act}(D)>0\), define

$$
\mathbb P_a^{act}(\,\cdot\,\mid D)
:=
\mathbb P_a^{act}(\,\cdot\,\mid \Pi_a(Q_a)=D).
$$

### Proposition 1.4: Packetization Is Barandes-Aligned

The pushforward \(\nu_a^{act}\) and the conditional laws
\(\mathbb P_a^{act}(\cdot\mid D)\) are Barandes-aligned.

Proof.

They are ordinary finite probability operations on finite record spaces.
They introduce no hidden state, no Hilbert ontology, and no intermediate
Markov factorization.  `square`

## 2. Good Packets Are Not Enough

### Definition 2.1: Packet Residual Minimum

For a packet \(D\in{\mathsf P}_a\), write

$$
m_a(D)
:=
\min_{q\in{\mathcal B}_a(D)}{\mathcal A}_a(q),
$$

where \({\mathcal B}_a(D)\) is the conditioned sector represented by the
packet \(D\).

### Definition 2.2: Good Packet

For \(\epsilon>0\), let

$$
{\mathsf GoodPkt}_a(\epsilon)
:=
\{D\in{\mathsf P}_a:
D\hbox{ is regular smooth-compatible and }m_a(D)\le\epsilon\}.
$$

### Definition 2.3: Good Configuration

Let

$$
{\mathsf G}_a(\epsilon)
:=
\{q\in\Omega_a:
\Pi_a(q)\in{\mathsf GoodPkt}_a(\epsilon)
\hbox{ and }{\mathcal A}_a(q)\le\epsilon\}.
$$

This is the actual event needed for residual-small GR-facing behavior.

### Proposition 2.4: Packet Minima Do Not Imply Actual Residual Smallness

It is possible that

$$
\nu_a^{act}({\mathsf GoodPkt}_a(\epsilon_a))=1
$$

and

$$
m_a(D)\le\epsilon_a
$$

for every actual packet \(D\), while

$$
\mathbb P_a^{act}({\mathcal A}_a(Q_a)>\delta)=1
$$

for some fixed \(\delta>0\).

Proof.

For each packet \(D\), let the sector contain two configurations: a witness
\(q_D^0\) with \({\mathcal A}_a(q_D^0)\le\epsilon_a\), and another
configuration \(q_D^1\) with \({\mathcal A}_a(q_D^1)\ge\delta\).  Define the
actual conditional law inside each packet to put all mass on \(q_D^1\).  Then
every packet has a residual-small minimum, but the actual law never selects a
residual-small configuration.  All objects are finite.  `square`

### Corollary 2.5: Actual Selection Has Two Levels

An actual-law theorem must prove:

1. packet-level concentration on regular smooth-compatible packets;
2. conditional concentration inside those packets on residual-small
   configurations.

Packet-level realizability alone is not enough.

## 3. The Actual-Law Target

### Definition 3.1: Actual Good-Configuration Source

The actual finite matter-geometry law sources regular smooth residual
closure if there exists \(\epsilon_a\to0\) such that

$$
\mathbb P_a^{act}
\bigl(Q_a\in{\mathsf G}_a(\epsilon_a)\bigr)\to1.
$$

Call this statement

$$
\boxed{
\mathrm{V4P11\text{-}ACTUAL\text{-}GOOD\text{-}CONFIG\text{-}SOURCE}.
}
$$

### Theorem 3.2: Actual Good-Configuration Source Closes The Paper-10 Gate

If `V4P11-ACTUAL-GOOD-CONFIG-SOURCE` holds and the good packets satisfy
Paper-10 regular compactness and continuum identification, then the actual
law realizes the Paper-7 residual closure in probability.

Proof.

On \({\mathsf G}_a(\epsilon_a)\), the packet is regular smooth-compatible
and the residual penalty is at most \(\epsilon_a\).  Since
\(\epsilon_a\to0\) and the event has probability tending to one, every
finite residual norm entering \({\mathcal A}_a\) tends to zero in probability.
Paper 10 supplies the regular packet interpretation, and Paper 7 converts
residual closure plus its remaining identification hypotheses into the
GR-like finite dynamics conclusion.  `square`

## 4. Route A: Two-Level Selection

### Definition 4.1: Two-Level Selection Data

Two-level selection consists of:

1. packet concentration:

   $$
   \nu_a^{act}({\mathsf GoodPkt}_a(\epsilon_a))\to1;
   $$

2. conditional minimizer selection:

   $$
   \sup_{D\in{\mathsf GoodPkt}_a(\epsilon_a)}
   \mathbb P_a^{act}
   \bigl({\mathcal A}_a(Q_a)>m_a(D)+\delta_a\mid D\bigr)
   \to0
   $$

   with \(\delta_a\to0\).

### Theorem 4.2: Two-Level Selection Implies Actual Good-Configuration Source

If two-level selection holds, then

$$
\mathbb P_a^{act}
\bigl(Q_a\in{\mathsf G}_a(\epsilon_a+\delta_a)\bigr)\to1.
$$

Proof.

Split the bad event into:

1. packets outside \({\mathsf GoodPkt}_a(\epsilon_a)\);
2. packets inside \({\mathsf GoodPkt}_a(\epsilon_a)\) but configurations with
   residual penalty larger than \(m_a(D)+\delta_a\).

The first probability tends to zero by packet concentration.  The second
tends to zero by conditional minimizer selection.  For good packets,
\(m_a(D)\le\epsilon_a\), so the remaining mass has
\({\mathcal A}_a\le\epsilon_a+\delta_a\).  `square`

### Verdict 4.3

Two-level selection is exact and finite.  The current corpus does not yet
source either packet concentration or conditional minimizer selection for the
actual law.

## 5. Route B: Residual-Penalty Gibbs Selection

### Definition 5.1: Regularized Residual-Penalty Score

Let \(K_a(q)\ge0\) be a finite regularity-defect score such that

$$
K_a(q)=0
$$

on the declared regular packet sector, and \(K_a(q)\ge\kappa_a>0\) on the
irregular sector.  Define

$$
S_a(q):={\mathcal A}_a(q)+\lambda_a K_a(q).
$$

### Definition 5.2: Residual-Penalty Gibbs Law

For a positive finite reference measure \(\mu_a\) and temperature
\(\tau_a>0\), define

$$
\pi_a^{pen}(q)
:=
\frac{\mu_a(q)e^{-S_a(q)/\tau_a}}
{\sum_{r\in\Omega_a}\mu_a(r)e^{-S_a(r)/\tau_a}}.
$$

### Definition 5.3: Score Gap

Let \({\mathsf G}_a(\epsilon_a)\) be the good-configuration event.  A score
gap holds if there exist \(\Delta_a>0\) and \(s_a^0\) such that:

1. some good configuration has \(S_a(q)\le s_a^0\);
2. every bad configuration has \(S_a(q)\ge s_a^0+\Delta_a\).

For a chosen good witness \(q_0\), define the reference-measure cost

$$
\chi_a(q_0)
:=
\log\frac{\max_{q\in\Omega_a}\mu_a(q)}{\mu_a(q_0)}.
$$

### Theorem 5.4: Gibbs Concentration

If a score gap holds with good witness \(q_0\) and

$$
\Delta_a/\tau_a-\log|\Omega_a|-\chi_a(q_0)\to+\infty,
$$

then

$$
\pi_a^{pen}({\mathsf G}_a(\epsilon_a))\to1.
$$

Proof.

Let \(q_0\in{\mathsf G}_a(\epsilon_a)\) have \(S_a(q_0)\le s_a^0\).  The
total Gibbs weight of bad configurations is at most

$$
|\Omega_a|e^{-(s_a^0+\Delta_a)/\tau_a}\max_q\mu_a(q),
$$

while the good configuration contributes at least

$$
e^{-s_a^0/\tau_a}\mu_a(q_0).
$$

The bad-to-good ratio is therefore bounded by

$$
\exp\{\log|\Omega_a|+\chi_a(q_0)-\Delta_a/\tau_a\},
$$

which tends to zero by hypothesis.  `square`

### Corollary 5.5: Actual Law Equals Penalty Law

If

$$
\mathbb P_a^{act}=\pi_a^{pen}
$$

and the score-gap hypotheses hold, then
`V4P11-ACTUAL-GOOD-CONFIG-SOURCE` holds.

### Barandes Audit 5.6

The residual-penalty Gibbs law is Barandes-aligned only if it is the actual
finite law or a declared finite candidate law.  It is not a proof of the
actual law unless the equality or a transfer estimate is sourced.

### Verdict 5.7

Residual-penalty Gibbs selection is a clean positive route, but the current
corpus does not prove that the actual law equals this Gibbs law.

## 6. Route C: Radon-Nikodym And Entropy Transfer

The actual law need not equal a good reference law.  It is enough to be close
to one in a finite same-law sense.

### Definition 6.1: Good Reference Law

A finite law \(\pi_a\) on \(\Omega_a\) is a good reference law if

$$
\pi_a({\mathsf G}_a(\epsilon_a)^c)\le e^{-r_a}
$$

with \(r_a\to+\infty\).

### Theorem 6.2: Supremum RN Transfer

Assume \(\mathbb P_a^{act}\ll\pi_a\) and

$$
\log\left\|\frac{d\mathbb P_a^{act}}{d\pi_a}\right\|_\infty
\le\kappa_a.
$$

If

$$
r_a-\kappa_a\to+\infty,
$$

then

$$
\mathbb P_a^{act}({\mathsf G}_a(\epsilon_a)^c)\to0.
$$

Proof.

For the bad event \(B_a={\mathsf G}_a(\epsilon_a)^c\),

$$
\mathbb P_a^{act}(B_a)
\le
e^{\kappa_a}\pi_a(B_a)
\le
e^{\kappa_a-r_a}\to0.
$$

`square`

### Theorem 6.3: Relative-Entropy Transfer

Assume

$$
H(\mathbb P_a^{act}\mid\pi_a)\le h_a
$$

and \(\pi_a(B_a)\le e^{-r_a}\), where
\(B_a={\mathsf G}_a(\epsilon_a)^c\).  If

$$
h_a/r_a\to0,
$$

then

$$
\mathbb P_a^{act}(B_a)\to0.
$$

Proof.

The binary data-processing inequality gives

$$
H(\mathbb P_a^{act}\mid\pi_a)
\ge
p_a\log\frac{p_a}{\pi_a(B_a)}
-\log 2,
$$

where \(p_a=\mathbb P_a^{act}(B_a)\).  Since
\(\pi_a(B_a)\le e^{-r_a}\), this implies

$$
h_a+\log2
\ge
p_a r_a+p_a\log p_a.
$$

The last term is bounded below by \(-1/e\).  Hence
\(p_a\le (h_a+\log2+1/e)/r_a\to0\).  `square`

### Verdict 6.4

RN or entropy transfer is the most economical actual-law bridge.  The
current corpus does not yet source the needed RN or entropy domination
between \(\mathbb P_a^{act}\) and a good packet/reference law.

## 7. Route D: Finite Fisher Source-Response Bridge

This route is more dynamic.  Instead of directly bounding the RN derivative,
one connects the actual law to a good law by a finite source path and proves
that the path is short in Fisher length.

### Definition 7.1: Finite Source Path

A finite source path is a differentiable family

$$
t\in[0,T_a]\mapsto\mathbb P_{a,t}
$$

of positive finite laws on \(\Omega_a\), with

$$
\mathbb P_{a,0}=\mathbb P_a^{act}.
$$

Let

$$
X_{a,t}(q):=\partial_t\log\mathbb P_{a,t}(q)
$$

and

$$
I_a(t):=\mathbb E_{a,t}[X_{a,t}^2].
$$

The Fisher length is

$$
L_a:=\int_0^{T_a}\sqrt{I_a(t)}\,dt.
$$

### Lemma 7.2: Fisher Length Controls Total Variation

For every event \(E\subset\Omega_a\),

$$
\left|
\mathbb P_{a,T_a}(E)-\mathbb P_{a,0}(E)
\right|
\le
L_a.
$$

Proof.

Differentiate \(\mathbb P_{a,t}(E)\):

$$
\left|\frac{d}{dt}\mathbb P_{a,t}(E)\right|
=
\left|\mathbb E_{a,t}[1_E X_{a,t}]\right|
\le
\sqrt{\mathbb E_{a,t}[1_E^2]}\sqrt{I_a(t)}
\le
\sqrt{I_a(t)}.
$$

Integrating over \(t\) gives the bound.  `square`

### Theorem 7.3: Fisher Bridge Transfer

If

$$
\mathbb P_{a,T_a}({\mathsf G}_a(\epsilon_a)^c)\to0
$$

and

$$
L_a\to0,
$$

then

$$
\mathbb P_a^{act}({\mathsf G}_a(\epsilon_a)^c)\to0.
$$

Proof.

Apply Lemma 7.2 to \(E={\mathsf G}_a(\epsilon_a)^c\).  `square`

### Verdict 7.4

The Fisher bridge is fully same-law if the source path is a family of finite
record laws.  The missing primitive is a short actual-to-good Fisher path.
The current corpus does not provide \(L_a\to0\).

## 8. Route E: Regularity Tightness Plus Residual Moment Control

### Definition 8.1: Irregularity Observable

Let

$$
K_a:\Omega_a\to[0,\infty)
$$

be a finite irregularity observable whose sublevel sets

$$
\{K_a\le R_a\}
$$

imply the Paper-10 regularity collar and projective compactness.

### Theorem 8.2: Moment Route

Assume there exist \(R_a\to\infty\) and \(\epsilon_a\to0\) such that:

1. regularity tightness:

   $$
   \mathbb P_a^{act}(K_a>R_a)\to0;
   $$

2. residual moment control:

   $$
   \mathbb E_a^{act}[{\mathcal A}_a(Q_a)]\to0;
   $$

3. source-conditioned packet compatibility on \(\{K_a\le R_a\}\).

Then `V4P11-ACTUAL-GOOD-CONFIG-SOURCE` holds after possibly replacing
\(\epsilon_a\) by a slower sequence tending to zero.

Proof.

By Markov's inequality, for any \(\epsilon_a\) with
\(\mathbb E[{\mathcal A}_a]/\epsilon_a\to0\),

$$
\mathbb P_a^{act}({\mathcal A}_a>\epsilon_a)\to0.
$$

The regularity event \(\{K_a\le R_a\}\) has probability tending to one by
assumption and supplies the source-conditioned regular packet compatibility.
Intersecting the two high-probability events gives good-configuration
concentration.  `square`

### Corollary 8.3: Exponential Tightness Version

If for some \(\lambda_a>0\),

$$
\mathbb E_a^{act}[e^{\lambda_a K_a}]\le e^{c_a}
$$

and

$$
\lambda_a R_a-c_a\to+\infty,
$$

then regularity tightness follows by Chernoff's bound.

### Verdict 8.4

This route is attractive because it uses ordinary finite random-variable
estimates.  The current corpus does not yet source either
\(\mathbb E[{\mathcal A}_a]\to0\) or the needed regularity tightness.

## 9. Route F: Actual-Support Dual Floor

The negative route is just as important.  If the actual law lives on a sector
that is separated from residual closure, then V4 should know that and stop
or change architecture.

### Definition 9.1: Actual Support Floor

The actual law has a support floor if there exists \(\delta>0\) such that

$$
{\mathcal A}_a(q)\ge\delta
\qquad
\hbox{for all }q\in\mathrm{supp}(\mathbb P_a^{act})
$$

for all sufficiently fine \(a\).

### Theorem 9.2: Actual Support Floor Blocks Residual Closure

If the actual law has a support floor, then

$$
\mathbb P_a^{act}({\mathcal A}_a(Q_a)\ge\delta)=1
$$

for all sufficiently fine \(a\).  Hence actual residual closure is false.

Proof.

Immediate from the definition of support floor.  `square`

### Definition 9.3: Actual-Support Dual Certificate

An actual-support dual certificate is a sequence
\(\Lambda_a\in V_a^*\) and \(\delta>0\) such that:

$$
\|\Lambda_a\|_*\le1,
$$

and

$$
\Lambda_a({\mathcal R}_a(q))\ge\delta
\qquad
\hbox{for all }q\in\mathrm{supp}(\mathbb P_a^{act}).
$$

### Theorem 9.4: Dual Certificate Gives Actual Support Floor

An actual-support dual certificate implies an actual support floor
\({\mathcal A}_a\ge\delta^2\).

Proof.

For \(q\) in the actual support,

$$
\delta
\le
\Lambda_a({\mathcal R}_a(q))
\le
\|{\mathcal R}_a(q)\|.
$$

Thus \({\mathcal A}_a(q)=\|{\mathcal R}_a(q)\|^2\ge\delta^2\).  `square`

This proves the negative route:

$$
\boxed{
\mathrm{V4P11\text{-}ACTUAL\text{-}PACKET\text{-}DUAL\text{-}FLOOR}.
}
$$

### Verdict 9.5

The current corpus does not provide an actual-support dual certificate.
Therefore the negative side is not proved either.

## 10. Exhaustion Table

| Route | Finite theorem proved | Missing primitive |
|---|---|---|
| Two-level selection | packet plus conditional minimizer concentration implies actual good-config source | actual packet concentration and conditional minimizer selection |
| Residual-penalty Gibbs | score gap plus low temperature gives concentration | actual law equals or is close to the Gibbs law |
| RN/entropy transfer | domination from a good reference transfers concentration | RN or entropy bound for actual law |
| Fisher bridge | short finite source path transfers concentration | actual-to-good Fisher length tends to zero |
| Moment/tightness | residual moment plus regularity tightness gives concentration | \(\mathbb E[{\mathcal A}_a]\to0\) and tightness |
| Actual dual floor | support dual certificate blocks residual closure | actual-support separator |

## 11. Current-Corpus Classification

### Theorem 11.1: Paper-11 Actual-Law Classification

The current V4 corpus proves the finite transfer theorems:

$$
\mathrm{V4P11\text{-}ACTUAL\text{-}GOOD\text{-}CONFIG\text{-}TRANSFER}
$$

in each of Routes A through E, and proves the negative finite route

$$
\mathrm{V4P11\text{-}ACTUAL\text{-}PACKET\text{-}DUAL\text{-}FLOOR}
$$

under an actual-support dual certificate.

The current corpus does not prove any of the primitive actual-law estimates:

$$
\boxed{
\mathrm{V4P11\text{-}ACTUAL\text{-}GOOD\text{-}CONFIG\text{-}SOURCE}^{cur}
\quad\hbox{not sourced}.
}
$$

It also does not prove:

$$
\boxed{
\mathrm{V4P11\text{-}ACTUAL\text{-}PACKET\text{-}DUAL\text{-}FLOOR}^{cur}
\quad\hbox{not sourced}.
}
$$

Proof.

Routes A through E are Theorems 4.2, 5.4, 6.2, 6.3, 7.3, and 8.2.  The
negative route is Theorem 9.4.  The missing current-corpus claims would
require one of the primitive same-law estimates listed in the exhaustion
table.  Papers 4 through 10 do not supply those estimates for the actual law.
`square`

### Interpretation 11.2

Paper 11 is not another vague gap statement.  It proves exact finite
bridges.  What remains is a primitive quantitative theorem about the actual
finite law.

## 12. Primitive Estimate Campaign Inside Paper 11

This section attacks the primitive actual-law estimates directly, inside
Paper 11.  The question is whether one of the transfer routes above can be
sourced from the existing V4 corpus, or whether each still requires genuinely
new same-law quantitative information about the actual finite law.

### 12.1 Actual Packet RN Domination

Let \(\pi_a\) be a good reference law:

$$
\pi_a({\mathsf G}_a(\epsilon_a)^c)\le e^{-r_a},
\qquad
r_a\to+\infty.
$$

The RN route asks for:

$$
\log\left\|\frac{d\mathbb P_a^{act}}{d\pi_a}\right\|_\infty=o(r_a),
$$

or

$$
H(\mathbb P_a^{act}\mid\pi_a)=o(r_a).
$$

The most concrete way this could happen is through a finite log-density
defect estimate.

### Definition 12.1: Finite Log-Density Defect

Assume \(\mathbb P_a^{act}\ll\pi_a\).  Define

$$
\Delta_a(q)
:=
\log\frac{d\mathbb P_a^{act}}{d\pi_a}(q).
$$

A uniform defect bound is

$$
\sup_{q\in\Omega_a}\Delta_a(q)\le\kappa_a.
$$

A local defect expansion is an algebraic identity

$$
\Delta_a(q)=\sum_{\alpha\in I_a}\Delta_{a,\alpha}(q)
$$

on the finite record space.  This is allowed only as a finite log-density
identity; it is not a hidden Markov factorization.

### Theorem 12.2: Local Defect Domination

If \(\pi_a\) is good, \(\mathbb P_a^{act}\ll\pi_a\), and

$$
\sum_{\alpha\in I_a}\sup_q\Delta_{a,\alpha}(q)\le\kappa_a
$$

with

$$
r_a-\kappa_a\to+\infty,
$$

then

$$
\mathbb P_a^{act}(Q_a\notin{\mathsf G}_a(\epsilon_a))\to0.
$$

Proof.

The local defect expansion gives
\(\sup_q\Delta_a(q)\le\kappa_a\).  Theorem 6.2 then gives

$$
\mathbb P_a^{act}({\mathsf G}_a(\epsilon_a)^c)
\le
e^{\kappa_a-r_a}\to0.
$$

`square`

### Proposition 12.3: Current-Corpus RN Domination Is Not Sourced

The current V4 corpus does not prove the defect bound of Theorem 12.2.

Proof.

Papers 4 through 10 define finite metric records, curvature records,
geometry packets, residual penalties, and residual-small witnesses.  They do
not give a finite identity for

$$
\log\frac{d\mathbb P_a^{act}}{d\pi_a}
$$

relative to a good reference law, nor a uniform or entropy-scale bound on
that log-density.  Any such estimate would be a new same-law quantitative
input about the actual finite probability law.  `square`

### Verdict 12.4

RN domination is the cleanest positive route, but it is not obtained by the
current corpus.  It should be treated as a primitive actual-law theorem, not
as bookkeeping.

### 12.2 Short Fisher Bridge

The Fisher bridge tries to connect the actual law to a good law by a finite
source path

$$
t\mapsto\mathbb P_{a,t},
\qquad
\mathbb P_{a,0}=\mathbb P_a^{act},
\qquad
\mathbb P_{a,T_a}=\pi_a,
$$

where \(\pi_a\) is good.  It asks for

$$
L_a=\int_0^{T_a}\sqrt{I_a(t)}\,dt\to0.
$$

### Proposition 12.5: Fisher Bridge No-Free-Lunch

For any finite source path,

$$
\|\mathbb P_{a,T_a}-\mathbb P_{a,0}\|_{TV}\le L_a.
$$

Consequently, if \(\pi_a\) is good but

$$
\mathbb P_a^{act}({\mathsf G}_a(\epsilon_a)^c)\ge c>0,
$$

then no source path from \(\mathbb P_a^{act}\) to \(\pi_a\) can have
\(L_a\to0\).

Proof.

The first inequality is Lemma 7.2 optimized over events.  If
\(\pi_a({\mathsf G}_a(\epsilon_a)^c)\to0\) while the actual bad-event mass is
bounded below by \(c\), the total-variation distance is bounded below by
\(c+o(1)\).  Therefore \(L_a\) cannot tend to zero.  `square`

### Corollary 12.6: Fisher Bridge Is A Closeness Theorem

A short Fisher bridge does not create good-packet concentration from
nothing.  It proves that the actual law is already close, in finite
statistical geometry, to a good law.

### Proposition 12.7: Current-Corpus Short Fisher Bridge Is Not Sourced

The current corpus does not provide a finite source path from
\(\mathbb P_a^{act}\) to a good reference law with \(L_a\to0\).

Proof.

The existing finite source-response calculus supplies Fisher positivity and
Cauchy-Schwarz estimates once a source family is declared.  It does not
identify a good endpoint law, nor does it bound the integrated score
variance along an actual-to-good source path.  By Proposition 12.5, such a
bound is a substantive closeness theorem.  `square`

### Verdict 12.8

The Fisher route is Barandes-aligned and useful, but it is not magic.  It is
equivalent to proving that the actual law is already statistically close to a
good packet law.

### 12.3 Residual Moment And Regularity Tightness

The moment route asks for:

$$
\mathbb E_a^{act}[{\mathcal A}_a]\to0
$$

plus a regularity tightness estimate for a finite irregularity observable
\(K_a\).

### Proposition 12.9: Residual Moment Control Is Exactly Actual \(L^1\)
Residual Decay

The estimate

$$
\mathbb E_a^{act}[{\mathcal A}_a]\to0
$$

is equivalent to \(L^1\)-decay of the total Paper-7 residual vector under the
actual law.

Proof.

By definition,

$$
{\mathcal A}_a(Q_a)=\|{\mathcal R}_a(Q_a)\|^2.
$$

Therefore the displayed expectation is exactly the actual-law mean squared
residual.  Since \({\mathcal A}_a\ge0\), it is an \(L^1\) residual-decay
statement.  `square`

### Proposition 12.10: Moment Route Needs A Lyapunov Or Ward Source

The current corpus does not prove

$$
\mathbb E_a^{act}[{\mathcal A}_a]\to0
$$

or regularity tightness for the actual law.

Proof.

Papers 7 through 10 define the residual vector and prove that residual-small
sectors are geometrically meaningful.  They do not supply an actual-law
Lyapunov identity, entropy-production inequality, stationarity condition, or
Ward identity forcing the expectation of \({\mathcal A}_a\) to vanish.  Nor
do they supply exponential tightness for the finite regularity collar.
`square`

### Verdict 12.11

The moment/tightness route is direct and physically legible, but it is just
as hard as actual residual decay unless one finds a new finite Lyapunov,
dissipation, or Ward identity.

### 12.4 Actual Support Dual Floor

The negative route asks whether the actual support is separated from
residual closure.

Let

$$
S_a^{act}:=\mathrm{supp}(\mathbb P_a^{act})
$$

and define

$$
d_a^{supp}:=\inf_{q\in S_a^{act}}\|{\mathcal R}_a(q)\|.
$$

If \(d_a^{supp}\ge\delta>0\), then actual residual closure is false.

### Definition 12.12: Convex Dual Distance

Define

$$
d_a^{conv}
:=
\mathrm{dist}\bigl(0,\mathrm{conv}\{{\mathcal R}_a(q):q\in S_a^{act}\}\bigr).
$$

### Theorem 12.13: Convex Dual Certificate Equivalence

The following are equivalent:

1. \(d_a^{conv}\ge\delta\);
2. there exists \(\Lambda_a\in V_a^*\) such that

   $$
   \|\Lambda_a\|_*\le1
   $$

   and

   $$
   \Lambda_a({\mathcal R}_a(q))\ge\delta
   \qquad
   \hbox{for all }q\in S_a^{act}.
   $$

Proof.

This is the finite-dimensional separating-hyperplane theorem applied to the
closed convex set

$$
\mathrm{conv}\{{\mathcal R}_a(q):q\in S_a^{act}\}.
$$

If the set has distance at least \(\delta\) from zero, finite-dimensional
Hahn-Banach separation gives a norm-one functional that separates the closed
ball of radius \(\delta\) around zero from the convex residual hull.
Conversely, such a functional proves that every point in the convex hull has
norm at least \(\delta\) by duality.  `square`

### Proposition 12.14: Support Floor Does Not Always Give A Single Dual
Functional

It is possible that

$$
d_a^{supp}\ge\delta
$$

but

$$
d_a^{conv}=0.
$$

Proof.

Take a one-dimensional residual space and two actual support residuals
\(+1\) and \(-1\).  Each has norm \(1\), so the support floor is \(1\).  But
their convex hull contains \(0\), so no single linear functional is positive
on both with a fixed positive lower bound.  `square`

### Verdict 12.15

The negative route has two levels:

1. a direct support norm floor blocks actual residual closure;
2. a convex dual floor is a stronger, certificate-friendly way to prove it.

The current corpus proves neither for the actual support.

## 13. Maximal Four-Route Consequences

Section 12 names the four primitive routes.  This section pushes each one as
far as it can go inside finite probability theory alone.  The purpose is to
avoid a vague phrase like "get better actual-law information" and replace it
with exact finite statements.

The four primitive routes are:

$$
\boxed{
\begin{gathered}
\mathrm{V4P11\text{-}ACTUAL\text{-}PACKET\text{-}RN\text{-}DEFECT},\\
\mathrm{V4P11\text{-}SHORT\text{-}FISHER\text{-}PACKET\text{-}BRIDGE},\\
\mathrm{V4P11\text{-}ACTUAL\text{-}MOMENT\text{-}TIGHTNESS},\\
\mathrm{V4P11\text{-}ACTUAL\text{-}FLOOR}.
\end{gathered}
}
$$

The first three are positive routes.  The fourth is the negative route, with
support, high-probability, and convex-dual variants.

### 13.1 Canonical Good Reference Law

The RN and Fisher routes need a good reference law.  To avoid arbitrary
choices, define a canonical finite reference law from the same finite record
space.

### Definition 13.1: Canonical Good Packet Reference

Let \(\mu_a\) be a strictly positive neutral reference mass on
\(\Omega_a\), such as counting mass or the declared finite base law.  Let
\({\mathsf Reg}_a\subset\Omega_a\) be the regular sector, let
\({\mathcal A}_a(q)\) be the residual penalty, and let \(K_a(q)\ge0\) be a
finite regularity-collar penalty that vanishes on the declared regular smooth
witness sector.  For parameters \(\tau_a>0\) and \(\lambda_a\ge0\), define

$$
\pi_a^{good}(q)
:=
\frac{
{\bf 1}_{{\mathsf Reg}_a}(q)\,\mu_a(q)\,
\exp\!\left[-\frac{{\mathcal A}_a(q)+\lambda_a K_a(q)}{\tau_a}\right]
}{
\sum_{r\in{\mathsf Reg}_a}
\mu_a(r)\,
\exp\!\left[-\frac{{\mathcal A}_a(r)+\lambda_a K_a(r)}{\tau_a}\right]
}.
$$

If a hard regularity cut is undesirable, replace
\({\bf 1}_{{\mathsf Reg}_a}\) by a soft factor \(\exp[-K_a/\tau_a]\).  The
law is still finite and same-law-admissible as a comparison object.

### Proposition 13.2: Good Reference Concentration Criterion

Let

$$
{\mathsf G}_a(\epsilon)
:=
\{q:\Pi_a(q)\in{\mathsf GoodPkt}_a(\epsilon)
\hbox{ and }{\mathcal A}_a(q)\le\epsilon\}.
$$

Suppose there is a witness \(q_a^0\in{\mathsf G}_a(\epsilon_a)\) with
\(K_a(q_a^0)=0\), and every \(q\in{\mathsf G}_a(\epsilon_a)^c\cap
{\mathsf Reg}_a\) satisfies

$$
{\mathcal A}_a(q)+\lambda_a K_a(q)
\ge
{\mathcal A}_a(q_a^0)+\Delta_a.
$$

If

$$
\frac{\Delta_a}{\tau_a}
-
\log |{\mathsf Reg}_a|
-
\log\frac{\max_{q\in{\mathsf Reg}_a}\mu_a(q)}
{\mu_a(q_a^0)}
\longrightarrow+\infty,
$$

then

$$
\pi_a^{good}\bigl({\mathsf G}_a(\epsilon_a)^c\bigr)\to0.
$$

Proof.

The denominator of \(\pi_a^{good}\) is at least the single contribution from
\(q_a^0\).  The numerator over the bad regular set is bounded by
\(|{\mathsf Reg}_a|\max\mu_a\) times
\(\exp[-({\mathcal A}_a(q_a^0)+\Delta_a)/\tau_a]\).  Dividing gives exactly
the displayed exponential upper bound, which tends to zero.  `square`

### Verdict 13.3

The canonical good reference law can be made good by an ordinary finite
energy-gap estimate.  This is not the hard part.  The hard part is proving
that the actual law \(\mathbb P_a^{act}\) is close enough to this good
comparison law.

### 13.2 RN Route: Sharp Form

The RN route is often stated as "control the log-density defect."  The sharp
finite content is the following.

### Theorem 13.4: Sharp RN Obstruction

Let \(P_a\) and \(Q_a\) be finite laws on \(\Omega_a\), with \(P_a\ll Q_a\).
Let \(B_a\subset\Omega_a\).  If

$$
Q_a(B_a)\le e^{-r_a}
$$

and

$$
P_a(B_a)\ge c
$$

for some fixed \(c\in(0,1]\), then

$$
\log\left\|\frac{dP_a}{dQ_a}\right\|_{\infty}
\ge
r_a+\log c.
$$

Moreover,

$$
H(P_a\mid Q_a)
\ge
c r_a-\log 2.
$$

Proof.

For the \(L^\infty\) claim,

$$
c\le P_a(B_a)
=\sum_{q\in B_a}\frac{dP_a}{dQ_a}(q)Q_a(q)
\le
\left\|\frac{dP_a}{dQ_a}\right\|_\infty e^{-r_a}.
$$

Taking logarithms gives the first estimate.

For the entropy claim, data processing under the two-cell partition
\(\{B_a,B_a^c\}\) gives

$$
H(P_a\mid Q_a)
\ge
D_{\mathrm{bin}}\bigl(P_a(B_a)\,\|\,Q_a(B_a)\bigr).
$$

The binary divergence is at least
\(c\log(e^{r_a})-\log2\) when \(P_a(B_a)\ge c\) and
\(Q_a(B_a)\le e^{-r_a}\), because the binary entropy is at most \(\log2\).
`square`

### Corollary 13.5: RN Domination Is Exactly Bad-Mass Exclusion

Let \(Q_a=\pi_a^{good}\) and

$$
B_a={\mathsf G}_a(\epsilon_a)^c.
$$

If \(Q_a(B_a)\le e^{-r_a}\), then any RN route proving

$$
\log\left\|\frac{d\mathbb P_a^{act}}{dQ_a}\right\|_\infty=o(r_a)
$$

or

$$
H(\mathbb P_a^{act}\mid Q_a)=o(r_a)
$$

forces

$$
\mathbb P_a^{act}(B_a)\to0.
$$

Conversely, if the actual law keeps a fixed amount of mass on \(B_a\), then
the required RN or entropy defect must be at least order \(r_a\).

Proof.

Apply Theorem 13.4.  `square`

### Proposition 13.6: Current-Corpus RN Maximum

Inside the current corpus, the RN route has been developed to its exact
finite form:

$$
\boxed{
\hbox{good reference concentration}
+
\hbox{subcritical actual/reference density defect}
\Longrightarrow
\hbox{actual good-configuration concentration}.
}
$$

The corpus does not prove the subcritical actual/reference density defect.

Proof.

Proposition 13.2 supplies the good reference concentration.  Corollary 13.5
gives the exact transfer criterion and its obstruction.  No earlier V4 paper
proves a log-density or relative-entropy estimate comparing
\(\mathbb P_a^{act}\) to \(\pi_a^{good}\).  `square`

### 13.3 Fisher Route: Exact Geometric Meaning

The Fisher route is not a heuristic.  On a finite record space it is exactly
the spherical geometry of square-root probability amplitudes.  This is
Barandes-aligned because the square roots are a calculation on finite
probabilities, not a Hilbert-space ontology.

### Definition 13.7: Hellinger Affinity

For finite laws \(P,Q\) on \(\Omega_a\), define

$$
\operatorname{Aff}(P,Q)
:=
\sum_{q\in\Omega_a}\sqrt{P(q)Q(q)}.
$$

### Theorem 13.8: Finite Fisher-Rao Distance Formula

Let \(P_t\), \(t\in[0,1]\), be a smooth positive path of finite laws and let

$$
I(t)
:=
\sum_{q\in\Omega_a}
P_t(q)
\left(\partial_t\log P_t(q)\right)^2.
$$

The shortest Fisher length from \(P\) to \(Q\) is

$$
d_{FR}(P,Q)
=
2\arccos\operatorname{Aff}(P,Q).
$$

Proof.

Write \(u_t(q)=\sqrt{P_t(q)}\).  Then

$$
\sum_q u_t(q)^2=1
$$

and

$$
\partial_t\log P_t(q)
=
2\frac{\dot u_t(q)}{u_t(q)}.
$$

Therefore

$$
I(t)=4\sum_q \dot u_t(q)^2.
$$

The Fisher length is twice the spherical length of \(u_t\) on the positive
orthant of the unit sphere.  The shortest spherical path has angle
\(\arccos\sum_q\sqrt{P(q)Q(q)}\).  `square`

### Corollary 13.9: Short Fisher Bridge Equals Hellinger Closeness

A sequence of finite Fisher bridges from \(\mathbb P_a^{act}\) to
\(\pi_a^{good}\) has length tending to zero if and only if

$$
\operatorname{Aff}(\mathbb P_a^{act},\pi_a^{good})\to1.
$$

Equivalently, the squared Hellinger distance tends to zero.

Proof.

Immediate from Theorem 13.8.  `square`

### Proposition 13.10: Current-Corpus Fisher Maximum

The Fisher route is now completely reduced to a single finite statistical
claim:

$$
\boxed{
\operatorname{Aff}(\mathbb P_a^{act},\pi_a^{good})\to1.
}
$$

The current corpus does not prove this claim.

Proof.

Corollary 13.9 supplies the exact equivalence.  Existing source-response
calculus constructs Fisher metrics and response identities, but it does not
prove Hellinger closeness between the actual law and the good reference law.
`square`

### 13.4 Moment/Tightness Route: Exact Content

The moment route asks for a direct probabilistic residual estimate under the
actual law.  Its exact finite content is \(L^1\) residual decay plus tail
control.

### Definition 13.11: Uniform Residual Integrability

The nonnegative residual penalties \({\mathcal A}_a\) are uniformly
integrable under \(\mathbb P_a^{act}\) if

$$
\lim_{M\to\infty}\sup_a
\mathbb E_a^{act}
\bigl[{\mathcal A}_a\,{\bf 1}_{{\mathcal A}_a>M}\bigr]
=0.
$$

### Theorem 13.12: Moment Concentration Equivalence

Assume regularity tightness:

$$
\mathbb P_a^{act}(Q_a\in{\mathsf Reg}_a)\to1.
$$

Then:

1. if

   $$
   \mathbb E_a^{act}[{\mathcal A}_a]\to0,
   $$

   then there exists \(\epsilon_a\downarrow0\) such that

   $$
   \mathbb P_a^{act}(Q_a\in{\mathsf G}_a(\epsilon_a))\to1;
   $$

2. conversely, if

   $$
   \mathbb P_a^{act}(Q_a\in{\mathsf G}_a(\epsilon_a))\to1
   $$

   for some \(\epsilon_a\downarrow0\), and
   \(\{{\mathcal A}_a\}\) is uniformly integrable under
   \(\mathbb P_a^{act}\), then

   $$
   \mathbb E_a^{act}[{\mathcal A}_a]\to0.
   $$

Proof.

For the first direction, choose \(\epsilon_a\downarrow0\) slowly enough that

$$
\frac{\mathbb E_a^{act}[{\mathcal A}_a]}{\epsilon_a}\to0.
$$

Markov's inequality gives

$$
\mathbb P_a^{act}({\mathcal A}_a>\epsilon_a)\to0.
$$

Together with regularity tightness and packet-goodness for residual-small
regular configurations, this gives good-configuration concentration.

For the converse, split

$$
\mathbb E_a^{act}[{\mathcal A}_a]
=
\mathbb E_a^{act}[{\mathcal A}_a{\bf 1}_{{\mathcal A}_a\le M}]
+
\mathbb E_a^{act}[{\mathcal A}_a{\bf 1}_{{\mathcal A}_a>M}].
$$

On the bounded part, good-event concentration and
\(\epsilon_a\downarrow0\) force the contribution to vanish for fixed \(M\).
Uniform integrability then lets \(M\to\infty\).  `square`

### Proposition 13.13: Current-Corpus Moment Maximum

The moment route is exactly:

$$
\boxed{
\hbox{regularity tightness}
+
\mathbb E_a^{act}[{\mathcal A}_a]\to0
+
\hbox{tail control}.
}
$$

The current corpus does not prove the actual \(L^1\) residual decay or the
needed uniform-integrability tail.

Proof.

Theorem 13.12 gives the exact equivalence.  Earlier papers provide finite
definitions of residuals and regular sectors, but not an actual-law Lyapunov,
Ward, dissipation, or coercive source identity implying
\(\mathbb E_a^{act}[{\mathcal A}_a]\to0\).  `square`

### 13.5 Floor Route: Exact Negative Content

The floor route is the negative twin of the positive route.  It must be
stated carefully, because a literal support floor can be too strong.

### Definition 13.14: High-Probability Residual Floor

The actual law has a high-probability residual floor if there exists
\(\delta>0\) such that

$$
\mathbb P_a^{act}({\mathcal A}_a\ge\delta)\to1.
$$

### Proposition 13.15: Full Support Kills A Strong Support Floor

Suppose that, for infinitely many \(a\), the actual law has full support on a
regular sector containing a residual-small witness \(q_a^0\) with

$$
{\mathcal A}_a(q_a^0)\to0.
$$

Then no uniform direct support floor

$$
\inf_{q\in S_a^{act}}\|{\mathcal R}_a(q)\|\ge\delta>0
$$

can hold along that subsequence.

Proof.

Full support puts \(q_a^0\) in \(S_a^{act}\).  The residual of \(q_a^0\) tends
to zero, contradicting any fixed positive support floor.  `square`

### Proposition 13.16: High-Probability Floor Is The Real Negative Twin

If there exists \(\delta>0\) such that

$$
\mathbb P_a^{act}({\mathcal A}_a\ge\delta)\to1,
$$

then actual good-configuration concentration is impossible for every
\(\epsilon_a<\delta\) eventually.

Conversely, if actual good-configuration concentration holds for some
\(\epsilon_a\downarrow0\), then no such high-probability residual floor can
hold.

Proof.

The good event \({\mathsf G}_a(\epsilon_a)\) is contained in
\(\{{\mathcal A}_a\le\epsilon_a\}\).  If \(\epsilon_a<\delta\), the events
\(\{{\mathcal A}_a\le\epsilon_a\}\) and
\(\{{\mathcal A}_a\ge\delta\}\) are disjoint.  `square`

### Proposition 13.17: Convex Dual Floor Is Certificate-Friendly But Strong

A convex dual floor,

$$
\operatorname{dist}
\left(
0,
\operatorname{conv}\{{\mathcal R}_a(q):q\in S_a^{act}\}
\right)
\ge\delta,
$$

implies a direct support floor and hence blocks residual-small support
witnesses.  But it can fail even when every actual support point has
nonzero residual norm.

Proof.

The implication to direct support floor is immediate because every support
residual lies in the convex hull.  Failure under nonzero support residuals is
Proposition 12.14.  `square`

### Proposition 13.18: Current-Corpus Floor Maximum

Inside the current corpus, the negative route has three exact variants:

$$
\boxed{
\begin{gathered}
\hbox{direct support floor},\\
\hbox{high-probability residual floor},\\
\hbox{convex dual residual floor}.
\end{gathered}
}
$$

The direct support floor is too strong whenever the actual law has full
support on residual-small witnesses.  The high-probability floor is the
correct negative twin of actual good-configuration concentration.  The convex
dual floor is the cleanest certificate when it exists.  The current corpus
proves none of the three for \(\mathbb P_a^{act}\).

Proof.

Propositions 13.15 through 13.17 give the exact relationships.  No previous
paper proves actual concentration on residual-large configurations, actual
exclusion of residual-small support points, or convex separation of the
actual residual support.  `square`

## 14. Paper-11 Primitive Estimate Settlement

### Theorem 14.1: Inside-Paper-11 Primitive Route Exhaustion

Inside Paper 11, the primitive actual-law routes have the following status.

| Primitive route | What would prove it | Current-corpus status |
|---|---|---|
| RN domination | finite log-density defect or entropy \(o(r_a)\) relative to \(\pi_a^{good}\) | not sourced; sharp obstruction if actual bad mass persists |
| Short Fisher bridge | Hellinger affinity \(\operatorname{Aff}(\mathbb P_a^{act},\pi_a^{good})\to1\) | not sourced; exactly Fisher-Rao closeness |
| Moment/tightness | \(\mathbb E_a^{act}[{\mathcal A}_a]\to0\), regularity tightness, and residual-tail control | not sourced; exactly actual residual decay plus tails |
| Direct support floor | norm floor on actual support | not sourced; impossible under full support plus residual-small witnesses |
| High-probability floor | \(\mathbb P_a^{act}({\mathcal A}_a\ge\delta)\to1\) | not sourced; real negative twin of good-configuration concentration |
| Convex dual floor | \(0\) separated from convex residual support | not sourced; strongest certificate variant |

Proof.

The RN route is Theorem 12.2, Proposition 12.3, Theorem 13.4, and
Corollary 13.5.  The Fisher route is Propositions 12.5 and 12.7 plus
Theorem 13.8 and Corollary 13.9.  The moment route is Propositions 12.9 and
12.10 plus Theorem 13.12.  The floor routes are Theorem 12.13, Proposition
12.14, and Propositions 13.15 through 13.18.  `square`

### Corollary 14.2: No Structural Shortcut Remains

The remaining obstruction is no longer finite packet bookkeeping, residual
dichotomy, smooth realizability, or actual-law transfer formalism.  It is a
primitive quantitative estimate on the actual finite stochastic law.

Proof.

Papers 9 through 11 have converted each structural step into a finite theorem
and each transfer route into an exact sufficient condition.  Section 12 shows
that the remaining hypotheses are precisely actual-law quantitative
estimates.  Section 13 sharpens those estimates into exact finite
probability statements.  `square`

## 15. Final Settlement

Paper 11 fully implements the actual-law selection layer.

The exact positive target is:

$$
\boxed{
\mathbb P_a^{act}(Q_a\in{\mathsf G}_a(\epsilon_a))\to1,
\qquad
\epsilon_a\to0.
}
$$

Five finite same-law mechanisms imply it:

1. two-level packet and conditional-minimizer concentration;
2. residual-penalty Gibbs equality;
3. RN or entropy domination from a good reference law;
4. a short finite Fisher source bridge;
5. residual moment control plus regularity tightness.

The exact negative target is:

$$
\boxed{
\mathrm{V4P11\text{-}ACTUAL\text{-}PACKET\text{-}DUAL\text{-}FLOOR}.
}
$$

The current-corpus verdict is:

$$
\boxed{
\mathrm{V4P11\text{-}ACTUAL\text{-}GOOD\text{-}CONFIG\text{-}SOURCE}^{cur}
\quad\hbox{not sourced}
}
$$

and

$$
\boxed{
\mathrm{V4P11\text{-}ACTUAL\text{-}PACKET\text{-}DUAL\text{-}FLOOR}^{cur}
\quad\hbox{not sourced}
}
$$

The inside-Paper-11 primitive campaign further shows:

1. RN domination would solve the positive problem, but requires a new
   finite log-density or entropy estimate relative to the canonical good
   reference law \(\pi_a^{good}\);
2. a short Fisher bridge would solve it, but this is exactly Hellinger or
   Fisher-Rao closeness to \(\pi_a^{good}\);
3. residual moment plus tightness would solve it, but is exactly actual
   \(L^1\) residual decay plus regularity and residual-tail control;
4. a direct support floor is too strong when the actual law has full support
   on residual-small witnesses;
5. the correct negative twin is a high-probability residual floor;
6. a convex dual floor is certificate-friendly but stronger than a support
   norm floor, and is not currently sourced.

Thus V4 has now reached a clean primitive actual-law estimate problem inside
Paper 11 itself.  The next real theorem must be one of:

$$
\boxed{
\mathrm{V4P11\text{-}ACTUAL\text{-}PACKET\text{-}RN\text{-}DEFECT}
\quad\hbox{or}\quad
\mathrm{V4P11\text{-}SHORT\text{-}FISHER\text{-}PACKET\text{-}BRIDGE}
\quad\hbox{or}\quad
\mathrm{V4P11\text{-}ACTUAL\text{-}MOMENT\text{-}TIGHTNESS}
\quad\hbox{or}\quad
\mathrm{V4P11\text{-}ACTUAL\text{-}HIGH\text{-}PROB\text{-}FLOOR}.
}
$$
