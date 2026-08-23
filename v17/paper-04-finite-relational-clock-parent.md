# Paper 04 — finite relational clocks from one constrained quantum parent

## Exact clock-relative process equivalence, finite stoppage, and the limits of eliminating external time

Date: 2026-08-23

Status: **GREEN-UNREVIEWED MATHEMATICAL/PHYSICAL CONSTRUCTION**

Strongest candidate result:

```text
P04-CLOCK-RELATIVE-EQUIVALENCE-WITH-EXTERNAL-PARAMETER-
OPERATIONALLY-REDUNDANT-ON-ONE-FROZEN-FINITE-DOMAIN
```

Binding qualifications:

```text
THE LABORATORY CAUSAL ORDER AND PATH ARE SUPPLIED
THE PARENT AND COMPARATOR ARE CO-DESIGNED FROM ONE PREFROZEN REPRESENTATION
THE A FRAME EXISTS ONLY ON Q != 6
A READING-ONLY CHANGE OF CLOCK FAILS ON THE COHERENT SOURCE
CLOCK-CHOICE-DEPENDENT DYNAMICS IS PRESENT
NO ONTOLOGY, FUNDAMENTAL TIME, SPACETIME, GRAVITY, OR ACTUAL HISTORY IS SELECTED
```

This is the sole construction authorized by model-pin adjudication #81. No
parameter, source, clock, instrument, comparator, training point, held-out
point, threshold, or interpretation has been changed from the #77 pin.

## Abstract

We construct a finite stationary quantum parent with two internal reference
systems and ask whether an external orbit label can be removed from complete
finite predictions. The parent is the invariant subspace of four
seven-dimensional systems under a fixed $\mathbb Z_7$ constraint. One clock
gives a global coordinate reduction; the other gives an exact reduction only
away from a frozen stopped sector. Bare phase projectors are not physical
Dirac observables. Complete clock packets instead use transforming retained
records, equivalently normalized direct-sum reduction branches.

For nine preregistered sources, the parent reproduces the laboratory orbit
description without a runtime orbit label. Two training readings determine
the affine relation between clocks and two held-out readings pass exactly. A
two-step matter measurement with a record-controlled guard also reproduces
the complete laboratory history law. Both predeclared clock--matter response
arms are nonzero and disappear under the frozen interaction-deletion control.

The full quantum temporal-frame map is unitary on its common sector, but a
scalar reading-only mixture fails for the coherent source: an all-reader
interference test distinguishes the coherent A-relative state from every
mixture over B readings. The clocks therefore provide compatible full quantum
frames while yielding source-dependent scalar dynamics. The $Q=6$ sector
stops clock A, every phase recurs after seven gauge steps, and no winding
record exists.

The external label is operationally redundant only on this co-designed,
finite, supplied-order experiment. This is a structural existence theorem,
not evidence that nature is a seven-state system or fundamentally timeless.
Chronology, geometry, gravity, actuality, and the ontology of the parent
remain unconstructed.

## 0. Immutable corpus and construction chronology

The construction authenticates these exact authorities.

| Artifact | SHA-256 | Role |
|---|---|---|
| `v17/note-paper04-two-clock-parent-construction-pin.md` | `8adb5def4c927dd55eba4c2360782b1b6d9370fcf3f5d5c76f5458b1a0fbca4e` | exact model, sources, tests, attacks, and ceiling |
| `v17/note-paper04-model-pin-audit-mathematics.md` | `a2fd150f75557c992a746e78b1e9b3b209bc7d0adca0ca8cee5bcb192d7a9ce9` | finite-constraint and reduction bindings |
| `v17/note-paper04-model-pin-audit-quantum-clocks.md` | `69c7deae38b115fd60d31006e5b5f79f5167e8e655bf9f3a0c7867ebbd809c1d` | complete-instrument and coherent-record bindings |
| `v17/note-paper04-model-pin-audit-ontology-relativity.md` | `ebd1fa98640accbe036d8097802f27e050875a09771f0d646ed7027e302bf0d6` | ontology and supplied-geometry bindings |
| `v17/note-paper04-model-pin-audit-adjudication.md` | `f0d2ae0142192683192a5e033c572d0c5906feb546d14268f7525f1b9a0a42cc` | terminal authorization and B1--B20 |
| `v17/paper-03v32-complete-boundary-relativistic-adequacy.md` | `469ae61c849573c9fe7c70871ca6b60843a080082d07f6850b48213b86d6f7d6` | complete paired operational interface |
| `v17/note-paper03v32-hostile-review-adjudication.md` | `b42fcf6201e249f03772ae2f1e037c2c945e98e4221c89a629d744de937e6104` | accepted Paper-03 scope |
| `v17/paper-00-reality-first-programme.md` | `a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe` | reality-first and gravity walls |

The model pin was committed before any calculation in this paper. The three
audits and root adjudication also preceded calculation. All values below are
consequences of those bytes; none is a fitted input.

## 1. Finite kinematics and gauge constraint

Let $\mathbb F=\mathbb Z_7$, let $\omega=e^{2\pi i/7}$, and let

$$
\mathcal H_{\rm kin}
=\mathcal H_A\otimes\mathcal H_B\otimes\mathcal H_M\otimes\mathcal H_Q,
\qquad
\mathcal H_J\cong\mathbb C^7.
$$

In each factor, $|k\rangle$ is the charge basis and

$$
|\tau\rangle
=\frac1{\sqrt7}\sum_{k\in\mathbb F}\omega^{k\tau}|k\rangle
$$

is the conjugate phase basis. Define

$$
D(a,b,m,q)=a+2b+m+q+aq\pmod7
$$

and

$$
U_g|a,b,m,q\rangle=\omega^{gD(a,b,m,q)}|a,b,m,q\rangle.
$$

### Theorem 1.1 — representation and projector

The map $g\mapsto U_g$ is a unitary representation of $\mathbb Z_7$, and

$$
P=\frac17\sum_{g\in\mathbb F}U_g
$$

is the orthogonal projector onto the charge-zero subspace.

**Proof.** $D$ is a fixed $\mathbb Z_7$-valued function of the charges, so
$\omega^{gD}\omega^{hD}=\omega^{(g+h)D}$. Hence $U_gU_h=U_{g+h}$ and
$U_g^\dagger=U_{-g}$. Finite character orthogonality gives

$$
\frac17\sum_g\omega^{gD}=\mathbf1_{D=0}.
$$

Thus $P=P^\dagger=P^2$. $\square$

### Theorem 1.2 — physical dimension

The physical Hilbert space $\mathcal H_{\rm phys}=P\mathcal H_{\rm kin}$
has dimension $7^3=343$.

**Proof.** For every $(a,m,q)$ there is exactly one

$$
b(a,m,q)=-4(a+m+q+aq)\pmod7,
$$

because $2^{-1}=4$ in $\mathbb Z_7$. The vectors

$$
|a,m,q\rangle_{\rm phys}
:=|a,b(a,m,q),m,q\rangle
$$

therefore form an orthonormal basis indexed by $7^3$ triples. $\square$

The physical inner product is the inherited finite Hilbert inner product. No
distributional rigging map or gauge-volume normalization occurs.

## 2. Frozen sources and their exact physical states

For each frozen kinematic seed $|\phi_u\rangle$, define

$$
|\Psi_u\rangle
=\frac{P|\phi_u\rangle}{\sqrt{\langle\phi_u|P|\phi_u\rangle}}.
$$

Every seed has a sharp B phase. Its seven orbit images have mutually
orthogonal B phase labels. Consequently

$$
\langle\phi_u|P|\phi_u\rangle=\frac17
$$

for all nine sources, and

$$
|\Psi_u\rangle=\frac1{\sqrt7}\sum_{s\in\mathbb F}U_s|\phi_u\rangle.
$$

No source is postselected away.

### 2.1 Orbit forms

Writing phase labels in the order $(A,B,M)$ gives:

| Source | Exact orbit component at $s$ |
|---|---|
| U0 | $|s,2s,s\rangle|0\rangle_Q^k$ |
| U1 | $|2s,2s,s\rangle|1\rangle_Q^k$ |
| USTOP | $|0,2s,s\rangle|6\rangle_Q^k$ |
| UAO | $|1+s,2s,s\rangle|0\rangle_Q^k$ |
| UBO | $|s,1+2s,s\rangle|0\rangle_Q^k$ |
| USEQ | $|s,2s\rangle_{AB}(|s\rangle_M+|s+1\rangle_M)/\sqrt2\,|0\rangle_Q^k$ |
| UCOH | $(|s,2s,s\rangle|0\rangle_Q^k+|2s,2s,s\rangle|1\rangle_Q^k)/\sqrt2$ |
| UA0 | $|0\rangle_A^k|2s,s,s\rangle_{BMQ}$ |
| UA1 | $|1\rangle_A^k|2s,s,2s\rangle_{BMQ}$ |

All arithmetic in this table is modulo seven. The lab comparator is exactly
the individual orbit component; the physical source is their coherent
invariant sum.

## 3. Exact clock reductions

Define

$$
\mathcal R_B(\beta)=\sqrt7\,{}_B\langle\beta|
$$

on $\mathcal H_{\rm phys}$. On the physical charge basis,

$$
\mathcal R_B(\beta)|a,m,q\rangle_{\rm phys}
=\omega^{-b(a,m,q)\beta}|a,m,q\rangle.
$$

This maps an orthonormal basis to an orthonormal basis and is therefore unitary
onto $\mathcal H_A\otimes\mathcal H_M\otimes\mathcal H_Q$ for every $\beta$.

For $q\ne6$, define

$$
a(b,m,q)=-(1+q)^{-1}(2b+m+q)
$$

and

$$
\mathcal R_A(\alpha)|b,m,q\rangle_{\rm phys,A}
=\omega^{-a(b,m,q)\alpha}|b,m,q\rangle.
$$

This is unitary from the physical $q\ne6$ sector onto
$\mathcal H_B\otimes\mathcal H_M\otimes\mathcal H_Q^{q\ne6}$.

At $q=6$, $1+q=0$ and the constraint becomes

$$
2b+m+6=0,
$$

independent of $a$. The physical sector has dimension $49$: seven allowed
$(b,m)$ pairs times seven A charges. Phase contraction maps it onto only the
seven-dimensional span of those allowed pairs. Thus

$$
\operatorname{rank}\mathcal R_A(\alpha)|_{q=6}=7<49.
$$

Clock A is stopped as a temporal reference in this sector. No pseudoinverse
or deletion is introduced.

### 3.1 Full temporal-frame map

On $q\ne6$,

$$
\mathcal S_{A\leftarrow B}(\alpha,\beta)
=\mathcal R_A(\alpha)\mathcal R_B(\beta)^{-1}
$$

acts on a B-frame charge basis as

$$
|a,m,q\rangle
\longmapsto
\omega^{b(a,m,q)\beta-a\alpha}|b(a,m,q),m,q\rangle.
$$

It is a unitary permutation-phase map. Its inverse is
$\mathcal S_{B\leftarrow A}(\beta,\alpha)$, so the round trip is exactly the
identity on the common sector for every state, observable, and transported
complete instrument. It is undefined as an inverse on USTOP.

## 4. Complete gauge-covariant clock records

The kinematic phase effects are covariant, not Dirac:

$$
P E_B(\beta)P=\frac17P.
$$

A bare Lüders branch also leaves $\mathcal H_{\rm phys}$. The physical clock
packet therefore cannot be the compressed PVM.

### 4.1 B-record instrument

Let the B record transform as

$$
T_g^{R_B}|\beta\rangle=|\beta+2g\rangle.
$$

The recorded kinematic isometry

$$
W_B=\sum_\beta E_B(\beta)\otimes|\beta\rangle_{R_B}
$$

satisfies

$$
(U_g\otimes T_g^{R_B})W_B=W_BU_g.
$$

Its reduced direct-sum form has branches

$$
V^B_\beta=\frac1{\sqrt7}\mathcal R_B(\beta),
\qquad
\sum_\beta(V^B_\beta)^\dagger V^B_\beta=I_{\rm phys}.
$$

Thus the record is complete and normalized, while its numeral remains a
coordinate with transforming lineage.

### 4.2 A-record instrument

For A, the record shift depends coherently on Q charge:

$$
T_g^{R_A}
=\sum_q|q\rangle\langle q|_Q\otimes T_{(1+q)g}^{R_A}.
$$

Then

$$
W_A=\sum_\alpha E_A(\alpha)\otimes|\alpha\rangle_{R_A}
$$

intertwines the complete A--Q--record action. On $q\ne6$, the normalized
reduction branches are

$$
V^A_\alpha=\frac1{\sqrt7}\mathcal R_A(\alpha)\Pi_{q\ne6}.
$$

Their effects sum to $\Pi_{q\ne6}$. The complementary output is a retained
`A-STOPPED` flag carrying $\Pi_{q=6}$. The phase PVM remains readable there,
but it is not an invertible temporal frame.

The A record action is never replaced by a fixed classical permutation. On
UCOH, such replacement would measure or dephase Q and change the source.

### 4.3 Matter records

The M record carries $r\mapsto r+g$. The Q record carries the coherently
A-controlled shift $r\mapsto r+(1+a)g$. Each Lüders instrument is represented
by the same covariant recorded-isometry construction. All future-readable
record and controller memory is retained in the Paper-03 complete boundary.

## 5. Physical independence of the two clocks

Distinct tensor labels do not suffice. On the q=0 controls define the
gauge-invariant relative phase readers

$$
\Delta_A=\tau_A-\tau_M,
\qquad
\Delta_B=\tau_B-2\tau_M.
$$

For UAO their exact values are $(\Delta_A,\Delta_B)=(1,0)$; for UBO they are
$(0,1)$; for U0 they are $(0,0)$. Thus the independently shifted A and B
preparations descend to distinct relational records. Neither is a copy or
affine postprocessing of the other. Shared constraint correlations do not
erase their operational independence.

## 6. The clock-neutral predictor and laboratory bridge

For a source $u$, B reading $\beta$, and a complete B-frame context $c$, let

$$
\sigma^B_u(\beta)
=\mathcal R_B(\beta)\rho_u^{\rm phys}\mathcal R_B(\beta)^\dagger
$$

and let $\{K^c_h\}_h$ be the frozen complete context instrument. Define

$$
p_{\rm P}(h\mid u,\beta,c)
=\operatorname{tr}
\left(K^c_h\sigma^B_u(\beta)(K^c_h)^\dagger\right).
$$

The A-frame formula is identical with $\mathcal R_A$ on its common domain.
This predictor depends on the source, projector, physical state, clock record,
reduction, complete instrument, controller, and reader. It has no runtime
orbit argument $s$ and no lookup table for one.

If a seed has B phase origin $b_0$, set

$$
s_B(\beta)=\frac{\beta-b_0}{2}\pmod7.
$$

Directly from the orbit forms,

$$
\sigma^B_u(\beta)
=\operatorname{tr}_B\rho_u^{\rm lab}(s_B(\beta))
$$

with the named clock factor removed and every other factor retained. The
analogous A identity holds on each good fixed-q component with
$s_A=(\alpha-a_0)/(1+q)$, and coherently through the full A reduction for
UCOH.

This proves the exact bridge from the stationary parent to the supplied lab
orbit on the frozen domain. It is a structural reduction theorem because the
comparator and parent use the same pre-frozen $U$.

## 7. U0 calibration and held-out matter laws

For U0,

$$
(\tau_A,\tau_B,\tau_M)=(s,2s,s).
$$

The training points $s=0,1$ fix uniquely

$$
\tau_B=2\tau_A.
$$

The untouched held-out points give

$$
s=2:(\tau_A,\tau_B)=(2,4),
\qquad
s=3:(\tau_A,\tau_B)=(3,6),
$$

so both pass exactly. Conditional on either valid clock, the complete M phase
reader is the sharp law $\tau_M=s$. Hence the lab, A-frame, and B-frame U0
predictions agree with zero total-variation loss at all four registered
points.

No winding is used: the theorem ends before the first seven-step recurrence.

## 8. Complete two-step adaptive history

The USEQ source in the B frame at $\beta_1=2$ corresponds to $s_1=1$ and
has M state

$$
|\psi_M(\beta_1)\rangle
=\frac{|1\rangle_M^\tau+|2\rangle_M^\tau}{\sqrt2}.
$$

The first retained M phase measurement therefore gives

$$
p(r_1=1)=p(r_1=2)=\frac12.
$$

Let $T_M|r\rangle^\tau=|r+1\rangle^\tau$. The frozen guard applies $T_M$
for even $r_1$ and the identity for odd $r_1$. The B-frame propagation from
$\beta_1=2$ to $\beta_2=6$ corresponds to two gauge steps and maps
$|r\rangle_M^\tau$ to $|r+2\rangle_M^\tau$. Consequently

$$
(r_1,r_2)=
\begin{cases}
(1,3),&p=1/2,\\
(2,5),&p=1/2.
\end{cases}
$$

The complete recorded history is therefore

$$
p(2,1,I,6,3)=\frac12,
\qquad
p(2,2,T_M,6,5)=\frac12,
$$

with all other canonical-slice tuples zero. The branch posterior is the
corresponding sharp M phase state together with both retained records and the
guard record.

### 8.1 No postselection and no invariant numeral

The canonical slice is the $\beta_1=2$ coordinate description of one
covariant complete direct sum. For an arbitrary first B record $b$, let

$$
h=4(b-2),
\qquad
b_2=b+4,
\qquad
\widetilde r_1=r_1-h.
$$

Under a gauge shift by $g$, $(b,r_1)$ changes to $(b+2g,r_1+g)$ and $h$
changes to $h+g$, so $\widetilde r_1$ is invariant. The full controller uses
the translated parity predicate on $\widetilde r_1$ and triggers the second
opportunity at the invariant B-record difference $b_2-b=4$. Every first
record branch is retained. The canonical $b=2$ slice has $h=0$ and gives the
table above.

Thus the controller consumes physical relational records rather than
program position or $s$. The supplied Paper-03 causal frontier still orders
the two operations.

### 8.2 Opposite-guard control

With the opposite parity rule, the same first marginal remains
$p(r_1=1)=p(r_1=2)=1/2$, but both branches reach $r_2=4$:

$$
(r_1,r_2)=(1,4),(2,4)
$$

with probability $1/2$ each. The complete history reader distinguishes the
two instruments. Replacing a complete instrument by its PVM effects, dropping
$r_1$, or reusing the undisturbed orbit state makes the guard or posterior
wrong and fails the target.

The lab comparator at $s=1$ and $s=3$ gives the same canonical history. The
parent derivation uses only the B records and their difference.

## 9. Full frame equivalence and scalar insufficiency

The unitary map $\mathcal S_{A\leftarrow B}$ transports all charge-basis
states and therefore all finite density operators and observables on the
common sector. Conjugation and direct-sum functoriality transport complete
instruments, retained records, posteriors, guards, and later readers. The
inverse gives exact all-context round trips for every registered source after
restriction to $q\ne6$.

This full quantum equivalence does not imply the scalar mixture formula.

### Theorem 9.1 — reading-only sufficiency fails on UCOH

Condition UCOH on A record $\alpha=1$. The two coherent contributions are

$$
|x\rangle=|B=2,M=1,q=0\rangle,
\qquad
|y\rangle=|B=1,M=4,q=1\rangle,
$$

and the normalized A-relative state is

$$
|+\rangle=\frac{|x\rangle+|y\rangle}{\sqrt2}.
$$

The A-relative complete reader $F_+=|+\rangle\langle+|$ has probability one.
Any scalar mixture over the two B reading branches replaces the cross-branch
coherence by

$$
\rho_{\rm mix}=\frac12|x\rangle\langle x|+
                \frac12|y\rangle\langle y|,
$$

for which

$$
\operatorname{tr}(F_+\rho_{\rm mix})=\frac12.
$$

Hence no reading-only kernel $M_{B|A}$ can reproduce every complete reader
for UCOH. $\square$

The full frame map remains unitary. The result is exact information loss in
the scalar description, not failure of the parent or permission to dephase
the source.

## 10. Multiple clock choices

The fixed-charge sources already prove source dependence:

$$
\begin{array}{c|c}
\text{source}&\text{A/B relation}\\
\hline
\mathrm{U0}&\tau_B=2\tau_A,\\
\mathrm{U1}&\tau_B=\tau_A,\\
\mathrm{USTOP}&\tau_A=0\text{ while }\tau_B=2s.
\end{array}
$$

UCOH coherently combines the first two rate sectors. No single
source-independent scalar affine or stochastic clock relation covers all
registered sources. The correct output is

```text
P04-CLOCK-CHOICE-DEPENDENT-DYNAMICS
```

with exact cause: clock--matter interaction, coherent sector dependence, and
finite stopped support. The complete quantum parent and common-sector frame
map remain well defined.

## 11. Reciprocal operational source-response

At B record $\beta=2$, corresponding to $s=1$:

- U0 gives the sharp A record $1$;
- U1 gives the sharp A record $2$.

Their complete-reader total-variation distance is one. When the frozen
interaction term $aq$ is deleted, both sources give A record $1$, so that
distance becomes zero.

For the opposite arm at the same B record:

- UA0 gives the sharp Q phase record $1$;
- UA1 gives the sharp Q phase record $2$.

Their distance is again one. Deleting $aq$ makes both records equal to $1$.
Thus both frozen directions pass without changing a reader or calibration.

This is bidirectional operational source-response in the supplied experiment.
It is not a derived causal arrow, energy flow, or gravitational backreaction.

## 12. Baselines and informative error

### 12.1 No-clock baseline

Replacing either clock record by an independent uniform record leaves the M
phase uniform conditional on that record. The target conditional M law is
sharp. Their total-variation distance is

$$
1-\frac17=\frac67.
$$

The time-sensitive M reader therefore separates the target from the no-clock
baseline.

### 12.2 Mistuned-B baseline

Changing only the comparator B coefficient from two to three gives B reading
$3s$ while the frozen target calibration and held-out interpretation remain
unchanged. At the target held-out records $4$ and $6$, the inferred matter
phases disagree sharply with U0. The maximum complete-reader
total-variation distance is one. No baseline is recalibrated.

### 12.3 Exact target loss

Across the registered U0 calibration/held-out laws and USEQ complete history,
the physical predictor and supplied laboratory comparator agree exactly, so
the target maximum total-variation loss is zero. The positive result does not
use a tolerance.

## 13. Reparameterization covariance

On each declared finite window, both

$$
f_{\rm aff}(x)=3x+1,
\qquad
f_{\rm nl}(x)=x+x^3/100
$$

are strictly increasing bijections to their images. Push forward the outcome
labels, covariant record actions, PVMs, counting/reference measures,
conditionals, calibration points, guard subsets, and all readers. For any
complete event $A$,

$$
(f_*p)(f(A))=p(A).
$$

Therefore every complete prediction and the zero-loss comparison are exactly
unchanged under both nonidentity maps. This is finite outcome-coordinate
covariance, not a continuum diffeomorphism theorem.

## 14. Hidden-time dependency audit

Every parent-relative probability has the dependency chain

```text
model-pin bytes
  -> D and P
  -> frozen seed u and normalized physical state
  -> transforming clock record
  -> R_A or R_B on its exact domain
  -> complete relational instrument and controller
  -> retained history and complete reader
  -> probability.
```

The runtime label $s$ is absent. It appears only in the supplied comparator
used after prediction to state the bridge theorem.

The hidden-record mutant substitutes $s$ for the physical B record. It has no
record isometry, no transforming lineage, and no parent branch; it fails at
the clock-packet and dependency gates even though it reproduces the printed
calibration table. The hidden lookup mutant stores $s\mapsto U_s$ in the
controller. Its bytes lie outside the allowed dependency graph and it fails
the same gate.

Thus $s$ is operationally redundant for the frozen finite predictions. The
causal order, query coordinates, preparation choices, and comparator path are
still supplied physical inputs.

## 15. Finite resource, recurrence, and stoppage ledger

The parent and every operation are finite.

| Resource | Exact value |
|---|---|
| A, B, M, Q dimensions | 7 each |
| kinematic dimension | $7^4=2401$ |
| physical dimension | $7^3=343$ |
| each phase record | 7 values |
| stopped-A flag | 2 values |
| USEQ first M record | 7 values |
| USEQ guard record | 2 values |
| USEQ second M record | 7 values |
| full explicit sequential record space | at most $7^4\cdot2=4802$ tuples |
| each Lüders record dilation | one seven-dimensional pointer |
| charge representatives | $0,\ldots,6$ |
| bare charge bandwidth | 6 declared charge units |
| first recurrence | 7 gauge steps |
| certified primary window | steps $0,1,2,3$ |
| comparison precision | exact finite probabilities; TV threshold 0 |

For a uniform charge distribution, the mean is three and the variance is
four. Every phase-state charge marginal has those values. Fixed charges have
zero variance. UCOH has Q-charge mean $1/2$ and variance $1/4$.

For USEQ, the M-charge probabilities are

$$
p_M(k)=\frac17\left(1+\cos\frac{2\pi k}{7}\right),
$$

so

$$
\mathbb E[K_M]=\frac52,
$$

and, writing $c_j=\cos(2\pi j/7)$,

$$
\operatorname{Var}(K_M)
=\frac{91+37c_1+29c_2+25c_3}{7}-\frac{25}{4}.
$$

The interaction support $aq$ is zero on U0, USEQ, UAO, UBO, and UA0; it
spans all residues on U1, USTOP, UA1, and the q=1 component of UCOH. The
preparation projector, readout pointers, two M measurements, one guard bit,
one controlled phase translation, and retained records are all explicit
resources.

The modular charge is not called positive energy. No continuum, large-clock,
or gravitational limit is taken.

## 16. Four record/division combinations

The accepted Paper-03 complete-boundary semantics supplies finite typed
apparatus registers. Within it the four frozen cases are realized as follows.

1. **Record and division.** Retain the clock record, posterior system, and
   every apparatus/controller register. Restrict later operations to this
   complete packet. Equality of the packet is future sufficient within the
   licensed continuation family.
2. **Record without division.** Retain the readable clock numeral but omit a
   two-valued apparatus memory that later controls an M translation. Equal
   clock records then have different future-reader laws.
3. **Division without record.** Apply a complete reset to a fixed posterior
   and erase the clock register. Every licensed future reads the same packet,
   but no clock outcome remains.
4. **Neither.** Stop after a controlled entangling operation before reading or
   retaining its apparatus memory. No clock record or future-sufficient cut
   exists.

These are representation-level divisions relative to the licensed Paper-03
continuations, not universal Barandes division events. None chooses an actual
outcome.

## 17. Theorem-target ledger M1--M24

| ID | Construction result |
|---|---|
| M1 | PASS — all exact authority and candidate bytes authenticate. |
| M2 | PASS — Theorem 1.1 proves the representation and projector. |
| M3 | PASS — dimension 343 and all nine source denominators $1/7$. |
| M4 | PASS WITH DOMAIN — complete covariant A/B recorded packets; A includes `STOPPED`. |
| M5 | PASS — one finite direct-sum joint law contains every source, record, guard, and context. |
| M6 | PASS WITH STRUCTURAL SCOPE — the lab orbit follows from the same pre-frozen representation. |
| M7 | PASS — B reduction and its complete paired record semantics are global. |
| M8 | PASS — A is unitary on $q\ne6$; q=6 has rank 7 of 49 and is retained. |
| M9 | PASS — U0 held-out M laws agree exactly in lab, A, and B descriptions. |
| M10 | PASS — USEQ complete history is $(1,3)$ or $(2,5)$ with probability $1/2$. |
| M11 | PASS — training fixes $(a,b)=(2,0)$ and both held-out points pass. |
| M12 | PASS ON COMMON DOMAIN — full unitary A/B frame map constructed. |
| M13 | READING-ONLY FAIL / FULL MAP PASS — UCOH reader gives $1$ versus $1/2$. |
| M14 | PASS ON COMMON DOMAIN — exact all-source/context round trip; USTOP excluded explicitly. |
| M15 | PASS — both nonidentity complete-interface pushforwards preserve predictions. |
| M16 | PASS ON FROZEN DOMAIN — parent predictor contains no $s$ or encoded schedule table. |
| M17 | PASS — NO-CLOCK has TV $6/7$ and MISTUNED-B reaches TV $1$. |
| M18 | PASS — complete finite resource, recurrence, and stoppage ledger printed. |
| M19 | PASS WITH LANGUAGE SCOPE — both operational source-response arms have TV $1$ and vanish in the deletion control. |
| M20 | DEPENDENT — U0, U1, USTOP, and UCOH do not share one scalar clock dynamics. |
| M21 | PASS WITH PAPER-03 SCOPE — all four record/division combinations instantiated. |
| M22 | PREFIT CONDITIONAL STRUCTURAL PARENT — above a post-fit wrapper, below empirical or ontological selection. |
| M23 | PASS — generic and model-specific product printed separately below. |
| M24 | PASS — every supplied-order, ontology, spacetime, gravity, time, and actuality wall remains closed. |

The earliest positive rung is the complete two-clock joint law. The strongest
candidate rung is bounded clock-relative equivalence with operational
redundancy of $s$, qualified by scalar-frame failure and supplied order.

## 18. Paired controls C1--C42

Every negative arm below is evaluated with all unmentioned objects fixed.

| ID | Positive-arm result | Negative-arm result |
|---|---|---|
| C1 | A/B are physical factors with relational records. | Scalar path index has no packet; rejected. |
| C2 | Relative-origin readers distinguish A and B. | Rename/copy mutants give one clock. |
| C3 | Recorded Lüders/direct-sum instruments are normalized. | Reading table alone has no posterior. |
| C4 | Every reading writes a retained transforming record. | Ephemeral outcome cannot drive USEQ. |
| C5 | All used finite conditionals have probability $1/7$ or greater. | Zero-support normalization refused. |
| C6 | Diffuse case is untested and not claimed. | Null-point versions earn no coordinate. |
| C7 | One physical source and one direct-sum law contain both clocks. | Separate fitted tables fail M5. |
| C8 | Two fit points and two untouched held-out points. | Fit-on-test mutant rejected. |
| C9 | Same comparator path is explicitly supplied. | Different-path forced agreement refused. |
| C10 | Both registered monotone bijections preserve the full packet. | Nonmonotone/noninjective map is physical change. |
| C11 | No winding claim is made. | Hidden cycle counter rejected. |
| C12 | Window $0,1,2,3$ is injective before recurrence. | Ignoring recurrence fails M18. |
| C13 | q=6 stops A locally. | B/M/Q and the universe remain active. |
| C14 | Seven-outcome resolution is retained. | Perfect-continuous-clock claim refused. |
| C15 | Full finite resource ledger printed. | Cost-free accuracy rejected. |
| C16 | Lüders disturbance appears in USEQ. | Nondisturbing replacement changes the history. |
| C17 | Both source-response arms pass. | Deleting $aq$ removes both. |
| C18 | Full histories and posteriors are retained. | Markovized same-reading histories fail. |
| C19 | One invariant parent yields both frames. | Matching independent tables do not pass. |
| C20 | Constraint froze before every result. | Decorative post-fit constraint refused. |
| C21 | Finite physical inner product normalizes all sources. | Kinematic/formal normalization refused. |
| C22 | Covariant finite phase records are constructed. | Ideal self-adjoint time import rejected. |
| C23 | USEQ supplies exact two-step statistics. | One-time PW conditioning is insufficient. |
| C24 | Full states/instruments/records/readers transform. | Scalar relabel fails on UCOH. |
| C25 | Round trip holds for every common-sector source/context. | One-source test is insufficient. |
| C26 | Scalar information loss is printed exactly. | Lossy mixture is not called equivalence. |
| C27 | $s$ is used only in the comparator bridge. | Predictor reading $s$ fails lineage. |
| C28 | The guard consumes a physical retained record. | External timer/program switch rejected. |
| C29 | Causal frontier remains supplied. | Clock labels derive no arrows. |
| C30 | Pure serialization permutations leave formulas unchanged. | Source order as time is rejected. |
| C31 | A/B and all sources froze before results. | Outcome-selected clock rejected. |
| C32 | One fixed $D$ governs every source/frame. | Clock-indexed retuning rejected. |
| C33 | Four record/division cases are distinct. | Tick-equals-division inference rejected. |
| C34 | No material state selects a foliation. | KMS/fundamental-frame claim rejected. |
| C35 | Both response arms use the same frozen law. | Imported GR correction rejected. |
| C36 | UCOH interference reader completes the quotient test. | Incomplete clock-only readers fail. |
| C37 | Coherent clock--Q correlations are retained. | Forced factorization changes UCOH. |
| C38 | Stop, recurrence, and dependence are printed. | Successful-window-only reporting rejected. |
| C39 | Comparator order/path/geometry are labeled supplied. | Emergence claim rejected. |
| C40 | All coordinates print independently. | One success word is forbidden. |
| C41 | Parent inputs froze at #77. | Target-fitted history wrapper is a different chronology. |
| C42 | Redundancy is finite and operational. | Fundamental timelessness does not follow. |

## 19. Generic hostile attacks 1--68

The registry below records the executed semantic disposition. `KILL` means
the mutant loses its first affected positive coordinate; `REFUSE` means it is
outside the frozen model rather than an alternative result.

| Attacks | Exact construction disposition |
|---|---|
| 1, 2 | `KILL M4/M16`: causal-slot rank and path length have no clock instrument. |
| 3, 4, 5 | `KILL M16`: source order/run counter change under presentation controls; pure serialization does not. |
| 6, 7, 8 | `KILL M4`: rename, copied record, and affine postprocessing fail the two-clock independence readers. |
| 9, 10 | `REFUSE`: fit-on-heldout and post-result window selection violate #77. |
| 11, 12 | `KILL M20/M16`: output- or future-selected clocks reverse lineage. |
| 13, 14, 15 | zero-support and null-version promotions are refused; diffuse coordinates remain untested. |
| 16, 17, 18, 19, 20 | `KILL M10`: lost record/memory, marginal-only comparison, deleted disturbance, or Markovization changes USEQ. |
| 21, 22 | `KILL M5/M12`: separate parent states or system laws are not frame changes. |
| 23, 24, 25 | `REFUSE/FORMAL`: post-fit constraint/factorization or clock-dependent $D$ changes the model. |
| 26, 27 | `KILL M2/M3/M7`: kinematic norm or unsolved PW state supplies no physical parent. |
| 28, 29 | `KILL M10` or theorem-scope refusal: one-time conditioning and out-of-domain Trinity use are insufficient. |
| 30, 31 | incompatible ideal-time or infinite-clock substitution is refused. |
| 32, 33, 34, 35 | `KILL M18`: unlimited runtime, ignored wrap, path winding, and phase reuse violate recurrence. |
| 36 | `KILL M8`: stopped A cannot be used as an inverse; B/M/Q remain available. |
| 37, 38 | lossy or orientation-reversing maps are physical controls, not registered gauge. |
| 39, 40 | `KILL M15`: partial label/PVM pushforward changes the complete interface. |
| 41, 42 | comparator path distinctions remain supplied and cannot be fitted away. |
| 43, 44, 45, 46 | `KILL M24`: reading order, category syntax, one clock, or material state cannot derive/globalize time. |
| 47, 48 | `KILL M19`: full or one-arm interaction deletion removes required reciprocity. |
| 49, 50, 51 | deleted disturbance, compensating retune, or hidden resources fail M10/M19/M18. |
| 52, 53 | `KILL M5/M12`: forced factorization or dephasing changes the quantum parent. |
| 54, 55, 56 | `KILL M13/M14`: loss, one-state tests, and incomplete readers cannot certify equivalence. |
| 57 | `KILL M16/M22`: renaming $s$ as a clock gives no physical lineage. |
| 58, 59, 60 | `KILL M21`: record/division identification or history factorization fails the four cases. |
| 61, 62, 63, 64 | `KILL M24`: ontology, metric, chronology, and GR promotions cross permanent walls. |
| 65, 66, 67, 68 | formal wrapper, encoded schedule, post-fit parent, and notation-to-timelessness mutants are refused. |

Every integer 1--68 occurs exactly once in the registry. No software behavior
is used as scientific evidence.

## 20. Model-specific attacks X1--X24

| ID | Result |
|---|---|
| X1 | Changing 7 is semantic replacement; refused. |
| X2 | Changing the B coefficient alters constraint/calibration; refused. |
| X3 | Deleting $aq$ changes both response arms from TV 1 to 0; detected. |
| X4 | Replacing $aq$ by $cI$ gives no reader response; fails M19. |
| X5 | USTOP has norm denominator $1/7$; deletion is detected. |
| X6 | Dephasing UCOH changes the $F_+$ probability from 1 to $1/2$; detected. |
| X7 | U0 alone leaves reciprocal and multiple-choice coordinates unconstructed. |
| X8 | Identifying A/B records destroys the independent $\Delta_A,\Delta_B$ controls. |
| X9 | Copying A into B gives a channel, not the B subsystem. |
| X10 | Four-point fit consumes the held-out evidence; refused. |
| X11 | Dropping either held-out point removes the overidentification gate. |
| X12 | Positive tolerance is unnecessary and refused. |
| X13 | Replacing B by $s$ fails the record-lineage dependency graph. |
| X14 | Hidden $s\mapsto U_s$ lookup fails the byte dependency audit. |
| X15 | Program-position trigger fails the covariant all-branch controller. |
| X16 | Erasing $r_1$ makes the guard untyped. |
| X17 | PVM effects alone cannot produce the USEQ posterior. |
| X18 | USTOP is positive-support and cannot be omitted. |
| X19 | A winding record changes the physical interface; refused. |
| X20 | Identity-only covariance earns no M15 result. |
| X21 | Label-only pushforward changes records/guards/readers; detected. |
| X22 | Increasing U0 readings do not alter the supplied-order coordinate. |
| X23 | Modular charge is not promoted to positive energy. |
| X24 | Finite success leaves ontology, gravity, and fundamental time unselected. |

## 21. Full product-valued result

### 21.1 Generic Paper-04 product

```text
1  P04-UPSTREAM-P03V32-PRESERVED

2  P04-CLOCK-A-PHYSICAL-PACKET-CONSTRUCTED-WITH-Q6-STOPPED-BRANCH

3  P04-CLOCK-B-PHYSICAL-PACKET-CONSTRUCTED

4  P04-TWO-CLOCK-JOINT-LAW-CONSTRUCTED

5  P04-FINITE-CLOCK-CONDITIONING-CONSTRUCTED

6  P04-DIFFUSE-CLOCK-CONDITIONING-AE-UNTESTED-FINITE-MODEL

7  P04-ORDINARY-CLOCK-RELATIVE-ADEQUACY-ON-FROZEN-DOMAIN

8  P04-SEQUENTIAL-ADAPTIVE-CLOCK-ADEQUACY-CONSTRUCTED

9  P04-SAME-PATH-AFFINE-AGREEMENT-EXACT-ON-TWO-HELDOUT-POINTS

10 P04-CLOCK-FRAME-TRANSFORMATION-CONSTRUCTED-ON-Q-NOT-6

11 P04-CLOCK-ROUNDTRIP-EQUIVALENT-ON-COMMON-SECTOR
   WITH-Q6-DOMAIN-LOSS-PRINTED

12 P04-CLOCK-NEUTRAL-PARENT-CONSTRUCTED

13 P04-LABORATORY-REDUCTION-FROM-PARENT-CONSTRUCTED
   AS-A-CO-DESIGNED-STRUCTURAL-BRIDGE

14 P04-PAGE-WOOTTERS-TRINITY-FINITE-COMPARATOR-CONSTRUCTED-WITH-SCOPE

15 P04-POSITIVE-STOCHASTIC-PARENT-NOT-APPLICABLE
   QUANTUM-CONSTRAINED-PARENT-USED

16 P04-REPARAMETRIZATION-COVARIANCE-CONSTRUCTED
   FOR-TWO-FROZEN-NONIDENTITY-FINITE-WINDOW-MAPS

17 P04-HIDDEN-EXTERNAL-TIME-EXCLUDED-FROM-FROZEN-PARENT-PREDICTOR

18 P04-FINITE-CLOCK-LIMITS-CONSTRUCTED

19 P04-CLOCK-BACKREACTION-CONSTRUCTED
   AS-BIDIRECTIONAL-OPERATIONAL-SOURCE-RESPONSE-ONLY

20 P04-STOPPED-RECURRENT-CLOCKS-CLASSIFIED

21 P04-CLOCK-CHOICE-DEPENDENT-DYNAMICS
   WITH-FULL-QUANTUM-COMMON-PARENT

22 P04-EXTERNAL-PARAMETER-OPERATIONALLY-REDUNDANT
   ON-ONE-FROZEN-FINITE-SUPPLIED-ORDER-DOMAIN
   CO-DESIGNED-STRUCTURAL-RESULT-NOT-ONTOLOGY-SELECTION

23 P04-CAUSAL-ORDER-STILL-SUPPLIED

24 P04-ONTOLOGY-SELECTION-UNCONSTRUCTED

25 P04-SPACETIME-CHRONOLOGY-UNCONSTRUCTED

26 P04-GRAVITY-UNCONSTRUCTED

27 P04-FUNDAMENTAL-TIME-STATUS-UNSELECTED

28 P04-ACTUALIZATION-UNCONSTRUCTED
```

### 21.2 Model-selection product

```text
P04M-MODEL-PIN-AUTHENTIC

P04M-FINITE-GROUP-PARENT-CONSTRUCTED

P04M-PHYSICAL-SOURCE-FAMILY-NONEMPTY

P04M-B-REDUCTION-GLOBAL

P04M-A-REDUCTION-Q-NOT-6

P04M-A-STOPPED-Q-6

P04M-COMPLETE-RELATIONAL-INSTRUMENTS-CONSTRUCTED

P04M-HELDOUT-SEQUENTIAL-LAW-REPRODUCED

P04M-FULL-QUANTUM-FRAME-MAP-CONSTRUCTED

P04M-READING-ONLY-SUFFICIENCY-FAILS-ON-UCOH

P04M-RECIPROCAL-INTERACTION-PASS

P04M-MULTIPLE-CHOICE-DEPENDENT

P04M-HIDDEN-TIME-EXCLUDED-ON-FROZEN-DEPENDENCY-GRAPH

P04M-CONDITIONAL-STRUCTURAL-OPERATIONAL-REDUNDANCY
```

The failure of reading-only sufficiency and the dependent-dynamics coordinate
do not compensate away. They are part of the positive scientific product.

## 22. What has and has not been learned

### 22.1 Positive result

One exact stationary constrained quantum system can carry two distinct
internal clock frames, complete transforming records, retained measurement
history, a nontrivial adaptive continuation, and reciprocal clock--matter
response. On a predeclared finite domain, all registered laboratory
probabilities can be computed from physical clock records without providing
the external orbit label to the parent predictor.

This goes beyond attaching a clock register to an already completed movie:
the parent, factorization, interaction, sources, readers, tests, and failure
sectors froze before the calculation; complete sequential statistics and
hidden-time controls pass; and the scalar frame approximation is permitted to
fail.

### 22.2 Negative result inside the positive construction

The clock relation is not a universal scalar change of variables. Interaction
and coherence produce source-dependent temporal frames. A full quantum map
exists while a reading-only mixture loses an exact interference observable.
Clock A also ceases to be a frame on a positive-support sector. These are
finite manifestations of the multiple-choice and nonideal-clock problems,
not implementation defects.

### 22.3 Why this does not establish timeless reality

The group variable is gauge, not a sequence of occurrences. The lab path and
the order of its interventions are supplied. The parent and comparator were
co-designed from the same representation. An idle hidden temporal sector or
an operationally equivalent different parent would evade every registered
reader. Therefore the result establishes a bounded representational and
operational redundancy, not the absence of fundamental time.

### 22.4 Why this is not a lattice or spacetime model

$\mathbb Z_7$ indexes charges and phase coordinates. It has no spatial
adjacency, localization net, causal relation, dimension estimator, metric,
curvature, continuum limit, or Einstein dynamics. Seven gauge images are not
seven events. The construction supplies no evidence that the universe is
discrete.

## 23. Relation to Barandes, quantum theory, and gravity

The construction is an orthodox finite constrained quantum model with
complete operational records. It does not replace Barandes's indivisible
stochastic ontology or derive his target and conditioning indices. It does,
however, sharpen a requirement any such completion faces: renaming a target
index a clock does nothing; a physical clock needs a subsystem, interaction,
record, complete conditional law, and a proof that the old index is absent
from prediction.

The model also demonstrates why quantum coherence matters to temporal frames.
The full transformation is complex-linear and unitary; probabilities arise
from complete instruments. A classical kernel cannot generally replace the
complex quantum map.

Gravity remains distant in a precise way. Paper 04 has no dynamical geometry,
no equivalence between matter response and metric response, no local Lorentz
structure, and no stress-energy or constraint algebra resembling general
relativity. Later work must first recover operational causal structure from
interventions of the same accepted law. Only after that may a separately
frozen matter--geometry parent be investigated.

## 24. Primary-source scope

The construction uses primary results only within these boundaries.

1. Page and Wootters motivate stationary-parent conditional dynamics, not a
   unique factorization or ontology.
2. Höhn, Smith, and Lock justify equivalence among reduction, relational
   observables, and constrained dynamics only under exact constraint,
   physical-inner-product, and clock-domain hypotheses, all proved here in
   the finite sector.
3. Höhn, Krumm, and Müller supply finite-Abelian quantum-reference-frame
   methods; they do not identify the finite group with time or spacetime.
4. Smith and Ahmadi motivate retaining clock--system interactions and their
   source-dependent effects.
5. Giacomini, Castro-Ruiz, and Brukner motivate transformation of complete
   quantum states, observables, and instruments rather than scalar labels.
6. Woods and collaborators motivate explicit finite-clock resources,
   disturbance, recurrence, and bounded validity.
7. Chataignier and collaborators motivate cycle-relative scope for periodic
   clocks and forbid a free winding label.
8. Fewster--Verch-style operational measurement and the accepted Paper-03
   semantics type the supplied laboratory process; its spacetime remains an
   input.
9. Barandes motivates the distinction between operational records,
   conditioning permissions, and an actual stochastic ontology; this paper
   derives none of his time indices or actual configurations.

No cited source selects $p=7$, the polynomial $D$, this factorization, the
source family, a preferred clock, or a fundamental timeless ontology.

## 25. Review-facing theorem list

The frozen candidate presents the following separately attackable theorems.

1. finite representation and orthogonal projector;
2. physical dimension 343;
3. nine source denominators equal to $1/7$;
4. global B reduction;
5. A reduction exactly on $q\ne6$;
6. q=6 rank loss $7<49$;
7. covariant B recorded instrument;
8. coherently Q-controlled A recorded instrument;
9. relational independence of A/B through $\Delta_A,\Delta_B$;
10. exact parent-to-lab orbit bridge;
11. two-point fit plus two-point held-out affine agreement;
12. exact USEQ complete-history law;
13. exact full-frame round trip on common support;
14. UCOH reading-only insufficiency $1$ versus $1/2$;
15. source-dependent scalar clock dynamics;
16. two reciprocal TV-one response arms and deletion controls;
17. no-clock TV $6/7$ and mistuned-B TV one;
18. two complete nonidentity coordinate pushforwards;
19. absence of $s$ from the parent predictor dependency graph;
20. finite resource, recurrence, and stop ledger;
21. all four record/division combinations;
22. C1--C42 paired controls;
23. attacks 1--68 and X1--X24;
24. full noncompensatory product and permanent walls.

## 26. Candidate disposition

The candidate disposition is:

```text
GREEN-UNREVIEWED

P04-CLOCK-RELATIVE-EQUIVALENCE-WITH-EXTERNAL-PARAMETER-
OPERATIONALLY-REDUNDANT-ON-ONE-FROZEN-FINITE-DOMAIN

P04-CLOCK-CHOICE-DEPENDENT-DYNAMICS

P04-READING-ONLY-FRAME-SUFFICIENCY-FAILS-ON-UCOH

P04-CAUSAL-ORDER-STILL-SUPPLIED
P04-ONTOLOGY-SELECTION-UNCONSTRUCTED
P04-SPACETIME-CHRONOLOGY-UNCONSTRUCTED
P04-GRAVITY-UNCONSTRUCTED
P04-FUNDAMENTAL-TIME-STATUS-UNSELECTED
P04-ACTUALIZATION-UNCONSTRUCTED
```

No downstream paper is opened by this green candidate. It must first pass a
result-neutral construction audit, three mutually blind hostile reviews, and
independent terminal adjudication.

## 27. Authentication

Candidate LF line count: `001197`

Candidate byte count: `045211`

Candidate ordinary SHA-256: reported externally after final bytes freeze;
embedding an ordinary self-hash would be circular.

Candidate normalized self-SHA-256:
`5f5e2aebd8b7382df97e07914ee552a3d95ffebd9103f8da5ffbf7377fabe600`

Normalization rule: replace the six decimal digits on each count line and the
64 hexadecimal characters on the normalized-self line by ASCII zeroes,
preserve every other byte, and compute SHA-256. The file must use LF endings,
end in one LF, and contain no trailing horizontal whitespace.
