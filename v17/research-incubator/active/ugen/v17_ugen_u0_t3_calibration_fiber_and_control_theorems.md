# ISP v17 — U-Gen U0-T3 calibration-fiber and control theorems

**Status:** ACTIVE AUTHOR-SIDE MATHEMATICS / NOT REVIEWED / NO PHYSICAL RESULT
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none
**Native candidate constructed:** no

This document proves that the U0-T3 public calibration schema leaves a genuine
complete-process selection problem. The proofs use only ordinary-positive
record laws. They do not select the law realized by nature.

The comparison mathematics is configuration-neutral. In particular it
inherits no Nelson trajectory, Euclidean carrier, Brownian noise, Markov
division, external time, diffusion scale, phase target, bundle, or holonomy.

---

## 0. Exact question

Let $\mathcal P=\mathcal C\sqcup\mathcal H$ be the registered executable
programs, partitioned into public calibration programs and sealed held-out
programs. Does the public packet determine one complete record process, or do
at least two admissible processes agree on every calibration record and differ
on a held-out record?

Only the latter permits a future law to earn member-selection credit.

---

## 1. Comparison class

### Definition T3.F1 — typed process family

Each program $p\in\mathcal P$ has a measurable complete-transcript space
$(\mathcal R_p,\Sigma_p)$. A typed process family is

$$
\mathbf P=\{P_p\in\mathcal P(\mathcal R_p):p\in\mathcal P\}.
\tag{1}
$$

The same transcript field has the same physical meaning wherever it appears.
Relabeling a field does not create another physical process.

### Definition T3.F2 — prefix maps

If $q$ is a completed stable-record prefix of $p$, let

$$
\pi_{p\to q}:\mathcal R_p\longrightarrow\mathcal R_q
\tag{2}
$$

discard only later records. A process family is prefix-compatible when

$$
(\pi_{q\circ f\to q})_*P_{q\circ f}
=
P_q
=
(\pi_{q\circ f'\to q})_*P_{q\circ f'}
\tag{3}
$$

for all later alternatives $f,f'$ licensed after $q$.

Equation (3) is the fixture's no-backwards-control condition. It is not a
Markov-factorization requirement at unresolved seams.

### Definition T3.F3 — admissible schema class

Let $\mathfrak K$ contain all typed process families satisfying:

1. normalization and nonnegativity;
2. the registered transcript and failure alphabets;
3. prefix compatibility (3);
4. the public calibration constraints and uncertainties;
5. the public independent-product and null constraints;
6. registered no-signalling constraints for the Cell C comparison class;
7. registered continuity only where a public actuator setting is continuous;
8. the frozen record coarse-grainings.

$\mathfrak K$ is defined without reference to a future candidate's image.
Resource-bounded subclasses are reported separately at candidate evaluation;
they are not used to make the public calibration appear complete by fiat. If
a resource-restricted fiber is also reported, its class must freeze before
target opening and each witness must satisfy that same bound.

### Definition T3.F4 — calibration restriction and fiber

The calibration map is

$$
\mathsf R_{\mathcal C}:
\mathfrak K\longrightarrow
\prod_{p\in\mathcal C}\mathcal P(\mathcal R_p),
\qquad
\mathbf P\longmapsto(P_p)_{p\in\mathcal C}.
\tag{4}
$$

For public calibration record $c$, define

$$
\mathcal F(c)=
\mathsf R_{\mathcal C}^{-1}(c).
\tag{5}
$$

At nonzero uncertainty, replace exact equality by the T2 calibration tube.
The held-out diameter is

$$
\Delta_{\mathcal H}(c)
=
\sup_{\mathbf P,\mathbf Q\in\mathcal F(c)}
\sup_{h\in\mathcal H}
\|P_h-Q_h\|_{\rm TV}.
\tag{6}
$$

The schema has a nontrivial calibration fiber when
$\Delta_{\mathcal H}(c)>0$.

---

## 2. Terminal-extension theorem

### Theorem T3.A — positive terminal freedom

Assume:

1. $h=q\circ R$ is a held-out terminal program, no registered program has
   $h$ as a stable-record prefix, and its final reader has binary output
   $b\in\{0,1\}$;
2. the stable prefix $q$ has law $\mu(dz)$ fixed by calibration and (3);
3. one admitted baseline conditional $q_0(b\mid z)$ satisfies

   $$
   \epsilon\le q_0(b\mid z)\le1-\epsilon
   \tag{7}
   $$

   on a measurable set $Z_*$ with $\mu(Z_*)=\alpha>0$;
4. the final conditional at $h$ is not itself in the calibration data; and
5. no additional registered equality fixes that conditional.

Then the calibration fiber contains two normalized prefix-compatible
ordinary-positive processes separated at $h$ by at least

$$
2\epsilon\alpha.
\tag{8}
$$

### Construction

Let $s:Z\to[-1,1]$ be measurable, supported on $Z_*$, and satisfy
$|s|=1$ there. Define

$$
q_\pm(b\mid z)
=
q_0(b\mid z)
\pm\epsilon s(z)(-1)^b.
\tag{9}
$$

Use $q_+$ and $q_-$ only for the terminal reader of $h$ and leave every other
program law equal to the baseline.

### Proof

For each $z$,

$$
\sum_b q_\pm(b\mid z)=1,
\tag{10}
$$

and (7) makes both conditionals nonnegative. Since only a final conditional
changes, the prefix marginal remains $\mu$ and (3) is preserved. Every
calibration program is unchanged. Finally,

$$
\begin{aligned}
\|P_h^+-P_h^-\|_{\rm TV}
&=
\int\mu(dz)\,
\frac12\sum_{b=0}^1
|2\epsilon s(z)(-1)^b|\\
&=
2\epsilon\int|s(z)|\,\mu(dz)
\ge2\epsilon\alpha.
\end{aligned}
\tag{11}
$$

Thus (8) holds. $\square$

### Meaning

The theorem is deliberately modest. It proves that an uncalibrated terminal
continuation cannot be inferred merely from calibrated prefixes,
normalization, positivity, and no-backwards control. It does not say that
nature chooses either constructed member.

---

## 3. Continuous-actuator theorem

### Theorem T3.B — finite calibration does not fix a continuous response

Let $U$ be a compact metric actuator-setting space, let
$C\subsetneq U$ be a closed calibration subset, and choose a held-out
$u_*\notin C$. Then there exist two continuous normalized binary record
kernels that agree for every $u\in C$ and differ at $u_*$.

### Proof

Because compact metric spaces are normal, there is a continuous
$g:U\to[0,1]$ with

$$
g|_C=0,
\qquad
g(u_*)=1.
\tag{12}
$$

For $0<\epsilon<1/2$, define

$$
P_\pm(b\mid u)
=
\frac12
\pm\epsilon(-1)^b g(u).
\tag{13}
$$

Both kernels are continuous, normalized, and positive. They coincide on $C$
and satisfy

$$
\|P_+(\,\cdot\mid u_*)-P_-(\,\cdot\mid u_*)\|_{\rm TV}
=2\epsilon.
\tag{14}
$$

$\square$

### Scope

The theorem concerns the public continuous actuator coordinate, not a
fundamental continuous configuration space. A dense or informationally
complete calibration plus a justified regularity class can collapse this
freedom; if it does, T2 must classify the packet as calibration-complete.

---

## 4. Marker/record separation theorem

### Theorem T3.C — overwrite does not type coherent unmarking

Consider four physical program types with final binary output $r$ and, where
present, stable marker record $y$:

1. $p_0$: unmarked baseline;
2. $p_M$: marker amplified into the shared stable-record prefix $y$;
3. $p_R$: marker amplified and retained;
4. $p_E$: marker amplified into stable record $y$, used, and later overwritten
   with registered overwrite result $o$;
5. $p_U$: marker coupled but coherently unmarked before amplification.

The following two complete ordinary-positive process families agree on
$p_0,p_M,p_R,p_E$ but differ on $p_U$:

$$
\begin{array}{c|cc}
&\mathbf P_{\rm revive}&\mathbf P_{\rm divide}\\
\hline
p_0&r=0\text{ with probability }1&r=0\text{ with probability }1\\
p_M&y\text{ uniform}&y\text{ uniform}\\
p_R&(y,r)\text{ uniform}&(y,r)\text{ uniform}\\
p_E&(y,r)\text{ uniform},\ o=1&(y,r)\text{ uniform},\ o=1\\
p_U&r=0\text{ with probability }1&r\text{ uniform}
\end{array}
\tag{15}
$$

Hence calibration of a stable record and its later overwrite does not
determine the coherent-unmarking continuation.

### Proof

Every row in (15) is normalized and ordinary positive. The overwrite row
retains the earlier stable marker record $y$ in the complete transcript; only
the physical marker medium is overwritten. The retained and overwrite
programs push forward to the same uniform $p_M$ prefix and have identical
complete record laws in both families. In $p_U$ no stable marker prefix
exists, so assigning its held-out terminal law does not change a prior stable
record or violate (3). The held-out total variation distance is

$$
\|\delta_0-\tfrac12(\delta_0+\delta_1)\|_{\rm TV}
=\frac12.
\tag{16}
$$

$\square$

### Physical wall

Equation (15) is a comparison pair, not a model of the apparatus. It proves
only that the type “stable record later overwritten” does not entail the type
“coherent marker reversed before record formation.”

---

## 5. Composite nonsignalling fiber

### Theorem T3.D — local calibration and no-signalling do not select a joint

Let settings and binary outcomes satisfy

$$
x,y,a,b\in\{0,1\}.
$$

For $v\in[-1,1]$, define

$$
P_v(a,b\mid x,y)
=
\frac14
\left[
1+v(-1)^{a\oplus b\oplus xy}
\right].
\tag{17}
$$

Then:

1. every $P_v$ is normalized and ordinary positive;
2. every local marginal is uniform and independent of the remote setting;
3. all members therefore agree on uniform local calibration and
   no-signalling tests;
4. for fixed $x,y$,

   $$
   \|P_v-P_w\|_{\rm TV}
   =\frac{|v-w|}{2};
   \tag{18}
   $$

5. the CHSH correlator of this orientation is $S=4v$.

### Proof

For fixed settings, two outcomes have sign $+1$ and two have sign $-1$ in
(17). Normalization and positivity follow from $|v|\le1$. Summing over either
outcome cancels the signed term and gives marginal $1/2$. Equation (18)
follows by summing four absolute differences of magnitude $|v-w|/4$ and
dividing by two. The four correlators are

$$
E_{xy}=v(-1)^{xy},
\tag{19}
$$

which gives $S=E_{00}+E_{01}+E_{10}-E_{11}=4v$.
$\square$

### Complete-failure lift

Let $\eta\in(0,1]$ be a fixed probability of a valid binary-pair record and
let $F$ be one fixed normalized no-signalling distribution on the disjoint
failure alphabet. Define

$$
\widetilde P_v
=
\eta P_v+(1-\eta)F.
\tag{20}
$$

All members retain identical failure behavior and local marginals, while

$$
\|\widetilde P_v-\widetilde P_w\|_{\rm TV}
=
\eta\frac{|v-w|}{2}.
\tag{21}
$$

Thus retaining no-click and failure outcomes does not collapse the joint
fiber.

### Comparator landmarks

$v=0$ is the uniform independent member; $|v|\le1/2$ lies within the CHSH
local bound for this one-parameter orientation; $v=1/\sqrt2$ has the standard
maximal quantum CHSH value; and $v=1$ is the extremal PR-style
nonsignalling member. These are controls, not candidate inputs and not claims
about the sealed target.

---

## 6. Per-program positivity theorem

### Theorem T3.E — positivity alone never supplies uniform generation

For any finite registered program set and any family of normalized target
record laws $\{T_p\}_{p\in\mathcal P}$, the rule

$$
\mathcal N_{\rm table}(p)=T_p
\tag{22}
$$

is an ordinary-positive complete-program assignment.

### Proof

Each $T_p$ is normalized and positive by hypothesis, so (22) returns an
ordinary-positive law for every program. $\square$

### Why it earns zero native credit

The rule stores the target family itself. At the registered numerical
representation and tolerance, its advice/resource cost includes

$$
\sum_{p\in\mathcal P}L(T_p)
\tag{23}
$$

up to shared compression, and it has no held-out member-selection content.
Equation (22) is a mandatory control against equating whole-program
indivisibility with explanation.

---

## 7. Fiber-collapse theorem

### Theorem T3.F — complete calibration removes the test

If the calibration restriction (4) is injective on $\mathfrak K$ at the
registered tolerance, then every calibration fiber has held-out diameter zero
at that tolerance.

### Proof

Injectivity implies that any two members with the same calibration restriction
are the same member of $\mathfrak K$. Therefore their held-out restrictions
coincide. $\square$

This includes a complete process-tomography packet relative to its stated
comparison class. Such a packet may be useful for conformance, but it cannot
test native member selection.

---

## 8. Representation-neutrality proposition

### Proposition T3.G — the fiber witnesses do not select configurations

Theorems T3.A--T3.F are invariant under:

1. bijective relabeling of settings and records;
2. lossless recoding of complete transcripts;
3. changes of units in public actuator coordinates;
4. gauge changes confined to a sealed quantum comparator; and
5. replacement of any microscopic realization by another with the same
   complete record family.

### Proof

Every hypothesis and conclusion is stated in terms of probability kernels,
restriction/pushforward maps, public setting topology where declared, and
total variation. These structures are preserved by the listed recodings.
$\square$

The propositions therefore select neither a finite carrier nor a continuum,
neither a trajectory nor a field, and neither a Hilbert nor a stochastic
ontology.

---

## 9. Schema-level fiber certificate

### Candidate theorem T3-CF

For the U0-T3 fixture schema, take $\mathfrak K_{\rm schema}$ to be the class
of all normalized complete record families satisfying:

1. the public local/blocked calibrations;
2. the complete transcript and failure types;
3. prefix compatibility;
4. continuity on the public Cell I actuator coordinate;
5. the independent-product/null controls;
6. no-signalling for the Cell C nonsignalling comparison subclass; and
7. no target-complete tomography or quantum comparator in the public packet.

If the implementation split leaves at least one terminal Cell I continuation
as in T3.A, then

$$
\Delta_{\mathcal H}(c)>0.
\tag{24}
$$

The Cell C coordinate is independently nontrivial when its calibrated local
marginals and failure law admit two members of the T3.D family while its
common-source joint table remains uncalibrated.

### Proof

T3.A constructs a positive prefix-compatible pair differing on the terminal
Cell I continuation, which already proves (24). T3.B supplies a continuous
pair if that held-out coordinate is a continuous actuator. Under the printed
additional Cell C hypothesis, T3.D independently supplies a nonsignalling
composite pair with identical local calibration and complete failure lift.
The schema constraints are componentwise except for the printed prefix,
product, and no-signalling equalities; the witness pairs preserve those
equalities while leaving every other program law fixed. Extending each
witness by the same unchanged record coordinates therefore preserves its
positive held-out total-variation distance. $\square$

### Exact scope

T3-CF is a schema theorem. An implementation-bound R4 packet must verify its
own hypotheses and tolerances after its real calibration constraints are
populated. The theorem does not say which fiber member nature realizes.

---

## 10. Control classification

| control | positivity | agrees with weak calibration | held-out role | native credit |
|---|---:|---:|---|---:|
| terminal $P_+$/$P_-$ pair | yes | yes | proves continuation freedom | none |
| continuous $P_+$/$P_-$ pair | yes | yes | proves finite-scan freedom | none |
| revive/divide marker pair | yes | yes | separates unmark from overwrite | none |
| $P_v$ nonsignalling family | yes | yes on local marginals | proves joint freedom | none |
| endpoint Markov composer | yes | often | hostile failure control | none |
| finite hidden-state fit | yes | by fit | resource/scaling control | conditional only |
| continuous predictive state | yes | possible | anti-finite-no-go control | conditional only |
| contextual whole-program law | yes | possible | context/advice control | conditional only |
| target table | yes | yes | complete zero-gain control | none |
| standard quantum evaluator | record-positive | yes | established comparator | none |
| supplied Barandes parent | yes | yes if supplied | representation control | none |

No row is the missing U0 nomology.

---

## 11. Hostile attacks on the fiber proof

1. define $\mathfrak K$ as the candidate's image;
2. omit a real public constraint that would collapse the pair;
3. let the two witnesses differ on calibration data;
4. change a stable prefix marginal using a future setting;
5. modify a failure category that calibration fixed;
6. use a discontinuous witness while claiming a continuous public class;
7. use a label clone rather than a record-law difference;
8. hide target advice in the baseline $q_0$;
9. call schema nonuniqueness evidence for one candidate;
10. infer physical superluminal influence from the PR-style control;
11. discard losses before applying T3.D;
12. identify record overwrite with coherent unmarking;
13. use the quantum landmark $v=1/\sqrt2$ as public target input;
14. call the target table a genuinely indivisible explanation;
15. promote public actuator continuity to continuous ontology;
16. promote a finite record alphabet to discrete ontology;
17. report $\Delta>0$ without an implementation-specific tolerance;
18. let the comparison class change after target opening;
19. treat calibration incompleteness as predictive success; and
20. use an opaque apparatus identity as uncharged response advice; and
21. claim that a nontrivial fiber proves a native law exists.

---

## 12. Author-side disposition

$$
\begin{array}{ll}
\text{NORMALIZED POSITIVE FIBER WITNESSES} & \text{CONSTRUCTED}\\
\text{PREFIX COMPATIBILITY} & \text{PRESERVED}\\
\text{CONTINUOUS-ACTUATOR WITNESS} & \text{CONSTRUCTED}\\
\text{MARKER / STABLE-RECORD SEPARATION} & \text{CONSTRUCTED}\\
\text{NONSIGNALLING COMPOSITE FIBER} & \text{CONSTRUCTED}\\
\text{FAILURE-RECORD LIFT} & \text{CONSTRUCTED}\\
\text{SCHEMA-LEVEL NONTRIVIAL FIBER} & \text{PROVED AUTHOR-SIDE}\\
\text{IMPLEMENTATION-BOUND FIBER} & \text{NOT YET CERTIFIED}\\
\text{NATIVE LAW OR MEMBER SELECTION} & \text{ABSENT}\\
\text{OFFICIAL REVIEW / RESULT} & \text{NONE}
\end{array}
$$

---

## 13. Maximum legitimate claim

> The U0-T3 schema leaves a rigorously nontrivial family of
> ordinary-positive, prefix-compatible complete record processes. Finite
> calibration does not fix a continuous held-out response; stable-record
> overwrite does not determine coherent unmarking; and local marginals plus
> no-signalling do not determine a composite joint law. These theorems make a
> future native-law contest nonvacuous. They neither identify nature's member
> nor construct a native indivisible stochastic nomology.
