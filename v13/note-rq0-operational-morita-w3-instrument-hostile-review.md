# Independent hostile review — categorical quantum mechanics and instruments

## Review provenance

- Governing pin: `35a487877d357bbeb60e11df31e1c8b6f37e1b6e`
- Immutable paper: `a1fa2c9cdd7f04189328c17357575abc72af54b4`
- Dispatch: `5e9fac08ff144dc44dab83bbe7cbeda65657164f`
- Verified paper SHA-256: `cb36418645f845fc35b9e1c77e71a37f1c5a9d6779cae8526a2dfba2ff138537`
- Verified pin SHA-256: `d7f83221c706e420d6c77e25fe645085cb7cb43cea2e75f629850623f2c99dac`

I reviewed the frozen blobs rather than later repository state. No repository artifact was edited, staged, or committed. Scratch calculations were confined to `/private/tmp`.

## Executive verdict

\[
\boxed{\texttt{HEADLINE-DOWNGRADE}}
\]

The first registered obstruction is

\[
\boxed{\texttt{RQ0-L0-BLOCKED-AT-COMPLETE-INSTRUMENT-W3}.}
\]

The paper substantially repairs the old candidate-selected probe defect. Its universal operator-system block condition, law-relative \(Z\)-versus-\(ZX\) control, full-effect negative, classical action transport, two-dephasing arrow, and nine-object branch benchmark are valuable.

It does not, however, construct the pinned complete-instrument W3 object. Two independent defects occur at the first rung:

1. The W3 tuple forgets the source and output CP-instrument witnesses above their state/POVM shadows.
2. The proposed eraser “scalar” can be nonzero even though no admitted complete readout probability distinguishes the written coherent state from its dephased state.

Thus the strongest supported description is:

\[
\boxed{
\text{a source-relative, complete-effect-marked W3 candidate theory
with algebraic cross-block erasure,}
}
\]

not a complete-instrument operational W3 theory.

The previously adjudicated terminal result remains:

\[
\boxed{\texttt{RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM}}
\]

with its prior law-relative, admitted-repeatable-coarse-graining scope. The antecedent adjudication preserves that result explicitly at commit `0623334`, lines 52–59 and 334–355.

---

## 1. Physical completeness

### What succeeds

Definition 2.2 fixes all admitted preparation instruments, readouts, processes, comparisons, and scalar contexts before a candidate is examined (paper lines 186–214). The output operator system

\[
\mathcal E_D(x)
=
\operatorname{span}_{\mathbb C}
\{I,e_j:e_j\text{ is an admitted outcome effect}\}
\]

is therefore candidate-independent. This correctly implements the pin’s prohibition on favorable effect subsets (pin lines 63–95).

Preparation completeness also correctly quantifies over every nonzero branch of the chosen source instrument (paper lines 216–230 and 559–578). An omitted branch of that same instrument cannot be ignored.

### Exact source-relative scope

A W3 object nevertheless selects one complete admitted source instrument:

\[
S=(\rho_\alpha)_{\alpha\in A}
\]

at paper lines 535–557. The construction ranges over all admitted source instruments, but it does not require a candidate to work for every source instrument simultaneously.

Hence:

- write correlation is relative to one selected complete source instrument;
- universal preservation is relative to the whole admitted output effect law;
- sharp readability is existential in an admitted output instrument;
- erasure is existential in a source branch, effect, and eraser continuation.

That asymmetry is permitted by pin lines 80–83, but it must remain engraved. “Complete” does not mean source-independent or law-wide over preparations.

### Exact preparation-postselection analogue

Let \(q_0,q_1\) lie in one coarse sector and suppose an existing favorable source passes write correlation. For a unitary write \(U\), add

\[
|\eta_{\mathrm{bad}}\rangle
=
U^\dagger\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad
\rho_{\mathrm{bad}}
=
|\eta_{\mathrm{bad}}\rangle\langle\eta_{\mathrm{bad}}|.
\]

Then

\[
w_{\mathrm{bad},0}
=
\rho_{\mathrm{bad}}(U^*q_0)
=
\frac12,
\qquad
w_{\mathrm{bad},1}
=
\frac12,
\]

and therefore

\[
w_{\mathrm{bad},0}w_{\mathrm{bad},1}
=
\frac14\ne0.
\]

If this is an omitted branch of the chosen complete source instrument, Definition 5.2 catches it. If it is instead a separately admitted complete one-outcome source instrument, the original favorable W3 object remains. That is the precise preparation-source relativity.

### Instrument data are dropped

Definition 2.3 says that a preparation instrument supplies normalized postselected states together with nonzero occurrence weights (paper lines 216–227). But Definition 5.1 records only \((\rho_\alpha)\).

For a preparation from a trivial input, the actual CP branches are

\[
\mathcal P_\alpha(1)=p_\alpha\rho_\alpha.
\]

Two instruments with the same normalized states and different nonzero weights \(p_\alpha\ne p'_\alpha\) yield the same \(S\). For a nontrivial preparation input, still more of the CP branch dynamics is lost.

This contradicts the pin’s requirement that the candidate object contain actual branches of a complete source preparation instrument (pin lines 269–285). Ambient membership of the full marking, asserted at paper lines 667–668, does not make the omitted witness part of the W3 datum.

---

## 2. Instrument versus effect

The ambient marked Morita equivalence does transport instrument branches outcome by outcome (paper lines 335–367 and 797–799). That part is correctly typed.

The W3 object does not retain those branches.

Sharp readable availability, paper lines 612–631, uses only:

- the output POVM effects \((e_j)\);
- their coarse map \(\ell\); and
- the equation
  \[
  V^*\!\left(\sum_{\ell(j)=r}e_j\right)=p_r.
  \]

Neither the output CP branches nor even the chosen output instrument and \(\ell\) appear as fields of

\[
s=(\omega,C_\Omega\xrightarrow{q^*}C_K,\lambda_F)
\]

at paper lines 651–668. They occur only as existential witnesses.

### Same POVM, different disturbance

Let \(P_A,P_B\) be rank-two projections. Compare the nondemolition Lüders instrument

\[
\mathcal L_r(\rho)=P_r\rho P_r
\]

with the measure-and-reprepare instrument

\[
\mathcal J_r(\rho)
=
\operatorname{Tr}(P_r\rho)\tau_r,
\]

where \(\tau_r\) is a fixed normalized state in sector \(r\). Both are complete instruments and

\[
\mathcal L_r^*(I)
=
P_r
=
\mathcal J_r^*(I).
\]

They therefore have the same POVM and induce exactly the same Definition 5.5 equations.

They have different dynamics. For example, with \(P_A=Q_0+Q_1\), \(\tau_A=Q_0\), and input \(Q_1\),

\[
\mathcal L_A(Q_1)=Q_1,
\qquad
\mathcal J_A(Q_1)=Q_0.
\]

The W3 object cannot distinguish them.

### Terminal destructive versus nondemolition

A terminal readout branch can be written

\[
\mathcal T_r(\rho)
=
\operatorname{Tr}(P_r\rho)\,|r\rangle\langle r|
\]

with classical target, while a nondemolition branch is \(P_r\rho P_r\) with quantum target. Their outcome effects agree, but their codomains and continuation possibilities do not.

The branch benchmark explicitly chooses the terminal case and excludes cut-boundary nondemolition pinching (paper lines 1355–1361). Therefore its narrow sharp-question claim is honest. It does not establish instrument-level availability or repeatability.

The correct surviving statement is “sharp POVM-effect availability,” not “complete-instrument W3.”

---

## 3. Universal availability

The universal block condition itself is correct at its declared effect-law scope:

\[
\mathcal D_RV^*(a)=V^*(a)
\quad
\forall a\in\mathcal E_D(x_2).
\]

The equivalences at paper lines 674–702 are elementary and valid:

\[
\mathcal D_RV^*(a)=V^*(a)
\iff
p_rV^*(a)p_s=0\ (r\ne s)
\iff
V^*(\mathcal E_D)\subseteq C_R'.
\]

There is a minor statement-level typing error: Theorem 6.1 writes both \(\mathcal E\subseteq B\) and \(T:\mathcal E\to B\), whereas the application has an output operator system in one algebra and a cut PVM in another. The proof only requires an operator system in the domain and a linear map into the PVM algebra. This is repairable and does not invalidate the block calculation.

### Favorable \(Z\)-only law

For

\[
p_0=|0\rangle\langle0|,
\qquad
p_1=|1\rangle\langle1|,
\qquad
\mathcal E_Z=\operatorname{span}\{I,p_0,p_1\},
\qquad
V^*=\operatorname{id},
\]

every effect is block diagonal. The record passes at this restricted admitted scope.

The identity is harmless:

\[
\mathcal D_R(I)=p_0+p_1=I.
\]

Declared coarse-grainings are sums of outcome effects and likewise remain block diagonal.

### Same algebra with an admitted \(X\) readout

Adding

\[
p_+=|+\rangle\langle+|
\]

gives

\[
p_0p_+p_1
=
\frac12|0\rangle\langle1|
\ne0.
\]

The same candidate therefore fails in the \(ZX\) law. Paper lines 1235–1267 and 1296–1302 reproduce this correctly.

### Full effect access and a unitary continuation

If

\[
\mathcal E=B(H_2)
\]

and \(V^*\) is a *-isomorphism onto \(B(H_1)\), universal preservation would imply

\[
B(H_1)\subseteq C_R'.
\]

For a nontrivial PVM, choose \(u\in p_rH_1\), \(v\in p_sH_1\), \(r\ne s\). Then

\[
p_r|u\rangle\langle v|p_s
=
|u\rangle\langle v|
\ne0.
\]

Thus no nontrivial record decomposition survives. Proposition 6.4, paper lines 729–741, is correct.

The block condition is therefore neither impossibly strong nor candidate-relative. It is the correct complete-effect replacement for the old singleton-probe test. It says nothing about disturbance branches.

---

## 4. Exact hostile reconstruction

For the four-level control, let

\[
P_A=Q_0+Q_1,
\qquad
P_B=Q_2+Q_3,
\]

and let \(V\) rotate \(\operatorname{span}\{|1\rangle,|2\rangle\}\) by an angle \(0<\theta<\pi/2\). The favorable effect \(Q_0\) is fixed.

Writing \(c=\cos\theta\), \(s=\sin\theta\),

\[
V^*Q_1
=
c^2Q_1+s^2Q_2
-cs\bigl(|1\rangle\langle2|+|2\rangle\langle1|\bigr)
\]

up to the irrelevant rotation-sign convention. Hence

\[
P_AV^*(Q_1)P_B
=
-cs\,|1\rangle\langle2|
\ne0.
\]

A singleton test using \(Q_0\) passes; the complete output effect system rejects \(V\). Paper lines 1188–1233 correctly close the old false-positive mechanism.

The preparation analogue behaves differently: branch completeness catches an omitted branch of the selected source instrument, but a separately admitted bad source does not invalidate a favorable source-relative object. The paper’s rule is therefore branch-complete but source-existential.

---

## 5. W3 dynamics and the eraser obstruction

Write correlation and matched no-write failure are legitimate probability conditions for states and UCP maps. Universal preservation is legitimate effect-level dynamics. Sharp readability is a legitimate POVM pullback, though not instrument-disturbance-sensitive.

The eraser condition is not generally an operational scalar.

Paper lines 633–649 require

\[
z=
\rho_\alpha\!\left(
U^*(q_kE^*(a)q_\ell)
\right)
\ne0.
\]

For \(k\ne\ell\), \(q_kE^*(a)q_\ell\) is generally nonself-adjoint and nonpositive. A state evaluates it as a complex linear functional, but it is not the effect of a closed CP experiment. In a CP/CPM operational theory, closed preparation-effect circuits yield nonnegative real probabilities. The paper explicitly chooses the individual cross term because its sum with the conjugate can cancel (lines 648–649); that is exactly the point at which operationality is lost.

### Exact complete-law false positive

Let \(H=\mathbb C^4\), with

\[
q_i=|i\rangle\langle i|,
\qquad
p_A=q_0+q_1,
\qquad
p_B=q_2+q_3.
\]

Use the complete four-outcome computational source instrument. Define unitaries by

\[
\begin{aligned}
U|0\rangle&=\frac{|0\rangle+|2\rangle}{\sqrt2},&
U|1\rangle&=\frac{|1\rangle+|3\rangle}{\sqrt2},\\
U|2\rangle&=\frac{|0\rangle-|2\rangle}{\sqrt2},&
U|3\rangle&=\frac{|1\rangle-|3\rangle}{\sqrt2},
\end{aligned}
\]

and

\[
\begin{aligned}
N|0\rangle&=\frac{|0\rangle+|1\rangle}{\sqrt2},&
N|1\rangle&=\frac{|0\rangle-|1\rangle}{\sqrt2},\\
N|2\rangle&=\frac{|2\rangle+|3\rangle}{\sqrt2},&
N|3\rangle&=\frac{|2\rangle-|3\rangle}{\sqrt2}.
\end{aligned}
\]

Every \(U|j\rangle\) has at most one fine component in each coarse sector, so write correlation holds for every source branch. The \(N|0\rangle\) branch gives

\[
n_{0,0}=n_{0,1}=\frac12,
\]

so matched no-write failure holds.

Admit two complete output readouts:

\[
(p_A,p_B)
\]

and

\[
(a,I-a),
\qquad
a=|\chi\rangle\langle\chi|,
\qquad
|\chi\rangle=\frac{|0\rangle+i|2\rangle}{\sqrt2}.
\]

Let

\[
V^*=\mathcal D_R,
\qquad
\mathcal D_R(x)=p_Axp_A+p_Bxp_B.
\]

Then for the whole admitted output effect system,

\[
\mathcal D_RV^*(x)=V^*(x),
\]

and

\[
V^*(p_A)=p_A,\qquad V^*(p_B)=p_B.
\]

Thus universal preservation and sharp readable availability hold.

Set

\[
E^*=\operatorname{id}.
\]

For source branch \(0\),

\[
|\psi\rangle=U|0\rangle
=
\frac{|0\rangle+|2\rangle}{\sqrt2}.
\]

The paper’s individual cross term is

\[
\begin{aligned}
z
&=
\langle\psi|q_0aq_2|\psi\rangle\\
&=
-\frac{i}{4}
\ne0.
\end{aligned}
\]

Definition 5.6 therefore calls \(E\) a coherent eraser.

But the actual complete-readout probability contrast is zero:

\[
\begin{aligned}
\langle\psi|a|\psi\rangle
-
\langle\psi|\mathcal D_R(a)|\psi\rangle
&=
z+\bar z\\
&=0.
\end{aligned}
\]

Indeed,

\[
\langle\psi|a|\psi\rangle
=
\langle\psi|\mathcal D_R(a)|\psi\rangle
=
\frac12.
\]

The same is true for \(I-a\), \(p_A\), and \(p_B\), and therefore for the entire admitted output operator system. No admitted output outcome probability distinguishes the written coherent state from its dephased state.

This is a full W3 object under Definitions 5.1–5.7, not merely an isolated matrix objection. It passes write, no-write, universal preservation, sharp readability, and the stated eraser test while failing operational coherence recovery.

Proposition 6.5 remains algebraically true: \(E^*(a)\) has a nonzero cross block. What fails is the promotion of an individual complex matrix coefficient to an admitted operational scalar connected to the written state and a complete experiment, required by pin lines 150–161 and 283–293.

The fixed branch-memory benchmark is not destroyed by this counterexample: its displayed eraser terms are positive real numbers \(|B||C|/16\), so their conjugate sums do not cancel. The general theorem and registered first rung nevertheless fail.

---

## 6. Classical interface

The categorical language is mathematically sound but does not add a new physical referent beyond the action.

A unital *-homomorphism

\[
\lambda:\mathbb C^\Omega\to\mathcal L_A(M)
\]

is equivalent to the PVM

\[
p_r=\lambda(\delta_r)
\]

by paper lines 434–468. The Frobenius structure packages finite classical copying/deleting intrinsically, while the physical embedding remains precisely the action \(\lambda\).

The fine-to-coarse map is correct:

\[
q^*:C_\Omega\to C_K,
\qquad
(q^*f)(k)=f(q(k)),
\]

and

\[
p_r=\sum_{q(k)=r}q_k
\]

at paper lines 470–500.

This removes dependence on coordinates of an already chosen PVM under Morita transport. It does not derive or uniquely select a PVM. The paper correctly retains nine branch actions and does not claim otherwise.

Two abstract copies of \(\mathbb C^2\) are isomorphic, but their actions can remain physically inequivalent when the conjugating unitary is not an admitted marked symmetry. Control 12.8 states this correctly.

---

## 7. Law-relative ontology

The ontology section is appropriately restrained.

The exact distinctions are:

- a stable proposition is a classical action/PVM satisfying the preservation predicate;
- a readable record is such a proposition with a sharp admitted POVM pullback;
- evidence would require an actual registered outcome in an experiment;
- an actual outcome requires a truth valuation selecting an atom in one run;
- fact co-reference requires identifying actual facts across descriptions;
- an event token requires individuation of occurrences;
- spatial locality requires independent localization and overlap structure.

The paper constructs only the first two, and even readability is effect-level. It explicitly denies actualization, fact co-reference, event tokens, and locality at lines 1737–1752. The exclusions at lines 1756–1778 are correct.

No coarse-graining, Morita equivalence, or addressability idempotent is silently promoted to spatial support.

---

## 8. Spectators and marking

### Inaccessible amplification

For the displayed \(\mathbb C\)-\(M_n\) imprimitivity module,

\[
H^X=H\otimes_{\mathbb C}\mathbb C^{1\times n},
\qquad
\mathcal L_{M_n}(H^X)\cong B(H).
\]

If the marking is defined by transporting the original marking and no additional spectator-resolving operation is admitted, Theorem 8.1 follows directly. This is a valid presentation-invariance theorem.

It is also close to tautological: \(D^{(n)}\) is defined to contain exactly the transported operational data. It does not discover from black-box experiments that an arbitrary tensor factor is inaccessible. The paper acknowledges the correct ontology at lines 908–913: this is a different module presentation, not a hidden system subsequently ignored.

The displayed construction explicitly proves the scalar-coefficient \(\mathbb C\leftrightarrow M_n\) case. The pin requested the general \(A\leftrightarrow A\otimes M_n\) amplification (pin lines 309–324). The standard generalization is available, but it is not actually written out in the frozen paper. I treat this as a scope omission, not a counterexample to the displayed theorem.

### Independently controlled spectator

Replace the induced right-\(M_n\) module presentation by the ordinary Hilbert-space system

\[
H\otimes\mathbb C^n
\]

over \(\mathbb C\), and admit, for example,

\[
I_H\otimes|0\rangle\langle0|,
\qquad
I_H\otimes X,
\]

together with an independently selectable spectator preparation. The observable algebra is now

\[
B(H)\otimes M_n,
\]

and the added effect/control has no preimage under the transported \(B(H)\) marking. Definition 3.4’s marking bijection fails. Proposition 8.2 and Control 12.3 correctly distinguish this physical spectator.

Thus the paper operationally distinguishes extra marked access. What remains definitional is the initial decision that no extra spectator operation belongs to the inaccessible marking.

### Q8 support smuggling

Control 12.6 correctly states that a separately supplied two-level W3 witness cannot become an internal quaternion seam merely through an `access_operations` label.

Its “if declared inaccessible” branch is a typing convention, not an independent experiment. If the witness source, effects, and controls are in the marking, the factor is physical by Proposition 8.2; if they are absent, it cannot supply the W3 witness. The control blocks support smuggling but does not rebuild a quaternion measurement.

---

## 9. Exact controls

| Control | Independent disposition | Nature |
|---|---|---|
| Singleton versus complete effect system | Correct. \(Q_0\) passes while the admitted \(Q_1\) exposes \(P_AV^*(Q_1)P_B\ne0\). | Exact matrix counterexample. |
| Favorable \(Z\) versus admitted \(X\) | Correct. \(p_0p_+p_1=\frac12|0\rangle\langle1|\ne0\). | Genuine law-relative measurement distinction. |
| Omitted source branch | Correctly caught within one source instrument; not across separately admitted sources. | Exact postselection counterexample and scope fact. |
| Same POVM, different disturbance | Not distinguished by W3. | Fatal instrument-shadow countermodel. |
| Terminal versus nondemolition | Benchmark honestly postulates terminal readout and excludes pinching. The general W3 predicate cannot distinguish the instruments. | Frozen-law postulate, not instrument theorem. |
| Full matrix effects plus unitary | Correctly excludes every nontrivial PVM. | Exact theorem. |
| Equivalent grammars | Correct conditional on equality of represented operational images. | Congruence/definition, not measurement. |
| Same algebra, different marked law | Correctly separated by the complete effect marking. | Genuine operational discriminator. |
| Inaccessible spectator | Correct for an induced marking. | Presentation-invariance definition/theorem. |
| Physical spectator | Correctly fails marking bijection when a new effect/control is admitted. | Genuine operational discriminator. |
| Q8 support smuggling | Correct typing conclusion, but no independent quaternion W3 experiment is reconstructed. | Definition/control. |
| Two dephasings | Correct. \(h=e_me_n\) satisfies \(e_mhe_n=h\) and is noninvertible for nonparallel, nonorthogonal axes. | Exact CP/Karoubi calculation, conditional on admitted maps. |
| Classical-object/PVM equivalence | Correct. | Structural theorem. |
| Branch-memory law | Source, readout, atomic actions, and identity-only idempotents are explicit law postulates; the finite enumeration is then exact. | Exact conditional classification. |

---

## 10. Nine seams, symmetry, and addressability

### Nine-object count

The branch-memory count survives at its frozen effect-level law.

The 15 partitions of four availability rays have types

\[
4,\quad 3+1,\quad 2+2,\quad 2+1+1,\quad 1+1+1+1.
\]

- The one-block partition has no nontrivial record.
- The four \(3+1\) partitions fail write correlation.
- The all-singleton partition cannot satisfy matched no-write failure.
- The three \(2+2\) and six \(2+1+1\) partitions pass.

Therefore

\[
\boxed{3+6=9}
\]

candidate seams remain. Paper lines 1408–1491 give the correct combinatorial argument. Because the benchmark’s eraser terms are positive real, the general phase-cancellation countermodel does not change this particular count.

They should be called nine W3 effect-level candidate seams unless instrument witnesses are added to the objects.

### Error in the printed \(S_4\) lift

Lemma 13.5 claims that for every output permutation matrix \(P\),

\[
T_2=P,\qquad
T_1=V^*PV,\qquad
T_0=U^*T_1U
\]

satisfy all four intertwining equations (paper lines 1501–1545). This explicit construction is false.

Use the paper’s basis and let \(P=P_{01}\), swapping output indices \(0\) and \(1\). With \(V=N\),

\[
T_1=NP_{01}N
=
\operatorname{diag}(1,-1,1,1),
\]

while

\[
T_0=U^*T_1U=P_{23}.
\]

Then

\[
\sqrt2\,(T_1N-NT_0)
=
\begin{pmatrix}
0&0&0&0\\
-2&2&0&0\\
0&0&0&0\\
0&0&2&-2
\end{pmatrix}
\ne0.
\]

So the second named-role intertwining equation fails.

The abstract conclusion is recoverable, but not by the printed proof. Exact enumeration of all

\[
24\cdot2^4=384
\]

signed monomial matrices found 48 matrices commuting with the displayed Hadamard matrix \(A\): exactly two signs over each underlying permutation. The central pair is \(\{\pm I\}\), and a 24-element complement exists. For example, a corrected lift of the transposition \((01)\) is

\[
\widetilde P_{01}
=
\begin{pmatrix}
0&1&0&0\\
1&0&0&0\\
0&0&-1&0\\
0&0&0&-1
\end{pmatrix},
\]

not the unsigned \(P_{01}\). Corrected signed lifts of adjacent transpositions satisfy the Coxeter relations and generate a subgroup isomorphic to \(S_4\).

Thus the \(S_4\) action and its two partition-type orbits are supported, but Lemma 13.5 has a genuine proof error. It cannot be accepted as written.

### Identity-only addressability

The benchmark explicitly admits terminal readout and no corresponding cut-boundary pinching (paper lines 1355–1361), then freezes its admitted idempotent grammar to identity only (lines 1574–1585). This is an honest frozen-law postulate; it does not delete a measurement channel that the same law had admitted.

It also does not establish that every \(\mathsf{Addr}(s)\) is an identity-only category.

Definition 10.2 says that a morphism between identity-idempotent objects is every admitted CP map \(h\) satisfying

\[
h=\operatorname{id}\,h\,\operatorname{id}=h
\]

and the record-interface compatibility. Restricting idempotent objects to identities does not remove nonidentity CP morphisms.

Moreover, “carrying the typed seam observability maps” at paper line 1055 is not given an equation or diagram. Proposition 10.3 merely says that this unspecified compatibility composes. Consequently:

- the fiber morphism sets are not completely defined;
- the branch benchmark does not inventory which admitted \(U,N,V,E\) or other CP processes are compatible;
- the claimed addressability categories in Theorem 13.7 are not classified.

The two-dephasing example at lines 1136–1182 is exact and correctly demonstrates the required noninvertible arrow. The general formal Grothendieck theorem is valid conditional on a genuinely defined pseudofunctor. The frozen paper has not supplied that full datum.

---

## Theorem-programme audit

| Pin theorem | Disposition |
|---|---|
| T1 — complete-instrument W3 | **Fails.** Universal block/readability distinction succeeds, but instrument witnesses are discarded and coherent erasure admits a complete-law false positive. |
| T2 — internal classical object | **Passes at the stated finite sharp-action scope.** It is categorified PVM data, not a derived unique referent. |
| T3 — marked Morita transport | **Conditionally passes for the algebraic state/effect predicates.** Conjugation by the boundary *-isomorphisms preserves the equations and full ambient marking. It cannot promote the deficient W3 object to instrument semantics. |
| T4 — spectator stability | **Passes for the displayed induced \(\mathbb C\)-\(M_n\) marking; general \(A\)-amplification is not written.** Physical marked spectators are correctly separated. |
| T5 — effective rigidification | **Formally passes conditional on well-defined W3 and addressability data.** The benchmark \(S_4\) proof contains the explicit lift error above. |
| T6 — full addressability fibration | **Not proved.** Record-interface compatibility is undefined, and the benchmark fiber morphisms are not classified. |
| T7 — branch-memory classification | **Partially passes.** The nine effect-level candidates and two partition-type symmetry orbits survive; complete instrument and full addressability classification do not. |

---

## Registered rung dispositions

| Registered outcome | Disposition | Exact reason |
|---|---|---|
| `RQ0-L0-COMPLETE-INSTRUMENT-W3` | **NOT EARNED** | The source tuple drops preparation branch weights/maps; output and eraser instruments are existential POVM shadows rather than retained branches; the individual eraser cross term is not generally an admitted operational scalar and has the explicit complete-law false positive above. |
| `RQ0-L0-MORITA-INVARIANT-W3-SEAMS` | **NOT EARNED** | Cumulative on the failed first rung. Classical actions and marked *-isomorphism transport survive conditionally, as does the displayed induced spectator equivalence. |
| `RQ0-L0-EFFECTIVE-W3-SEAM-STACK` | **NOT EARNED** | Cumulative failure. The finite normal-kernel quotient is sound conditionally, but the benchmark’s printed \(S_4\) lift proof is false and requires corrected signed lifts. |
| `RQ0-L0-FULL-ADDRESSABILITY-FIBRATION` | **NOT EARNED** | Cumulative failure, plus an independent defect: the record-interface compatibility defining fiber morphisms is unspecified and the branch categories are not actually classified. |
| `RQ0-L0-BLOCKED-AT-COMPLETE-INSTRUMENT-W3` | **REGISTERED CYCLE DISPOSITION** | This is the first exact obstruction in the pin’s cumulative ladder. |
| Prior `RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM` | **PRESERVED** | Nothing in this review reopens or weakens its law-relative repeatable-UCP-idempotent coarse-graining result. |

The later precise blocked labels are not selected because the first obstruction already occurs at complete-instrument W3.

## Final assessment

The paper succeeds in replacing favorable singleton probes with a genuine law-relative complete output operator system. It gives a useful finite classical-action formalism, exact negative controls, a correct nine-candidate benchmark at its frozen readout law, and a strong conditional Morita-transport architecture.

It does not yet carry complete quantum instruments through the W3 object itself, and its general eraser predicate is algebraic rather than operational. Those are semantic failures at the first registered rung, not editorial defects.

Therefore:

\[
\boxed{
\begin{gathered}
\texttt{HEADLINE-DOWNGRADE},\\
\texttt{RQ0-L0-BLOCKED-AT-COMPLETE-INSTRUMENT-W3},\\
\text{no new cumulative registered rung earned.}
\end{gathered}
}
\]
