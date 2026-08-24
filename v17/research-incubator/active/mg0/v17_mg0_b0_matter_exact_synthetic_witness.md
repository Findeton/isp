# ISP v17 — MG0 B0-Matter exact synthetic complete-record witness

**Status:** ACTIVE AUTHOR-SIDE EXACT CONTROL / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-24
**Scientific result awarded:** none
**Empirical or apparatus claim:** none

---

## 0. Purpose

This finite witness tests the mathematical interfaces proposed by the
B0-Matter readiness audit. It is deliberately too small to be a laboratory
model. In particular, it tests:

1. coherent source phase versus an incoherent mixture;
2. a reversible temporary path marker and coherent eraser;
3. a retained-register proxy, explicitly short of physical stable-record
   certification;
4. complete noisy reader normalization, including a correlated null-inclusive
   joint kernel;
5. an independently supplied fixed-background probe phase; and
6. a shared-nuisance countermodel with unchanged marginals but changed joint
   records.

It does not model a massive material, support, trap, Casimir force, gravity
source, reciprocal backreaction, or emergent spacetime. It cannot discharge
`P-B0-1`.

---

## 1. Effective finite carrier

Use two-dimensional source, marker, retained-register, and probe roles together
with a four-dimensional auxiliary role

$$
\mathcal H_{\rm syn}
=
\mathcal H_S\otimes
\mathcal H_M\otimes
\mathcal H_R\otimes
\mathcal H_P\otimes
\mathcal H_W,
\qquad
\mathcal H_W=\mathcal H_{W_D}\otimes\mathcal H_{W_X}.
$$

Here:

- `S` is a source path bit with basis `|L⟩,|R⟩`;
- `M` is a reversible path-marker bit;
- `R` is a retained-register bit used only as a finite proxy for a later
  amplified record;
- `P` is a probe path bit;
- `W_D` retains the finite dephasing/randomizer branch; and
- `W_X` is an uninterpreted external tag used to test whether two identical
  reduced operations are being silently identified.

These are operational test roles. They are not discrete ontology.

Take `|L⟩=|0⟩`, `|R⟩=|1⟩`. The common seed is

$$
|\Omega_0\rangle
=
|0\rangle_S|0\rangle_M|0\rangle_R|+\rangle_P
|0\rangle_{W_D}|0\rangle_{W_X}.
$$

Define

$$
|+_\varphi\rangle_S
=
\frac{|0\rangle+e^{i\varphi}|1\rangle}{\sqrt2}.
$$

After the coherent preparation map defined below, the joint state is

$$
|\Omega_\varphi\rangle
=
|+_\varphi\rangle_S|0\rangle_M|0\rangle_R|+\rangle_P
|0\rangle_{W_D}|0\rangle_{W_X}.
$$

---

## 2. Preparation family

The synthetic family is generated from the same `S,W_D` seed by the maps

$$
\begin{aligned}
\mathcal P_L &: I_S,\\
\mathcal P_R &: X_S,\\
\mathcal P_\varphi &: R_z(\varphi)H_S,\\
\mathcal P_{\rm mix} &:
\operatorname{CNOT}_{S\rightarrow W_D}H_S,
\end{aligned}
$$

where `R_z(varphi)=exp(-i varphi Z/2)` and the irrelevant global phase in
`R_z(varphi) H |0>` is discarded; products act rightmost first. Their reduced
source outputs are

$$
\begin{aligned}
E_L &: |0\rangle\langle0|_S,\\
E_R &: |1\rangle\langle1|_S,\\
E_\varphi &: |+_\varphi\rangle\langle+_\varphi|_S,\\
E_{\rm mix} &:
\frac12\left(|0\rangle\langle0|+|1\rangle\langle1|\right)_S.
\end{aligned}
$$

For `E_mix`, the untraced output is

$$
|\Psi_{\rm mix}\rangle_{S W_D}
=
\frac{|0,0\rangle+|1,1\rangle}{\sqrt2},
$$

so the mixture arises only after `W_D` is retained and ignored by the source
reader. The complete synthetic law can still read `W_D`; it does not destroy
the branch to manufacture a mixed state.

These are exact finite gate branches, not physical massive preparation
devices. A future empirical B0 model must generate the corresponding source
states from its apparatus dynamics; this file earns no such source credit.

For an ideal source read in the `X` basis,

$$
p_X(+\mid E_\varphi)=\frac{1+\cos\varphi}{2},
\qquad
p_X(-\mid E_\varphi)=\frac{1-\cos\varphi}{2}.
$$

For a `Y`-basis quadrature with the registered sign convention,

$$
p_Y(+\mid E_\varphi)=\frac{1+\sin\varphi}{2}.
$$

Thus `X` alone cannot distinguish `varphi=pi/2` from a mixture, while the
second quadrature can. This is why one fringe or one visibility is not a
complete coherence witness.

For `E_mix`, both `X` and `Y` outcomes are uniform.

---

## 3. Matched diagonal and coherence witness

For every diagonal source observable

$$
A=a_0|0\rangle\langle0|+a_1|1\rangle\langle1|,
$$

one has

$$
\operatorname{Tr}(A E_\varphi)
=
\operatorname{Tr}(A E_{\rm mix})
=
\frac{a_0+a_1}{2}.
$$

But with

$$
X_\varphi
=
e^{-i\varphi}|0\rangle\langle1|
+e^{i\varphi}|1\rangle\langle0|,
$$

the expectations are

$$
\operatorname{Tr}(X_\varphi E_\varphi)=1,
\qquad
\operatorname{Tr}(X_\varphi E_{\rm mix})=0.
$$

The witness therefore realizes the exact matched-algebra ceiling: the two
preparations match on the declared diagonal algebra, not on all observables.

---

## 4. Temporary marker and coherent eraser

Let

$$
U_{\rm mark}=\operatorname{CNOT}_{S\rightarrow M}.
$$

Marking gives

$$
U_{\rm mark}|\Omega_\varphi\rangle
=
\frac{|0,0\rangle_{SM}
+e^{i\varphi}|1,1\rangle_{SM}}{\sqrt2}
|0\rangle_R|+\rangle_P|0\rangle_{W_D}|0\rangle_{W_X}.
$$

If `M` is ignored, the source fringe is absent. The coherent eraser is the
same controlled operation applied again:

$$
U_{\rm mark}^{-1}=U_{\rm mark},
\qquad
U_{\rm mark}^{-1}U_{\rm mark}|\Omega_\varphi\rangle
=
|\Omega_\varphi\rangle.
$$

Therefore `E_erase` restores the ideal `X/Y` phase law before a stable record
forms.

This is a typed reversible marker, not a claim that an amplified material
record can be erased locally.

---

## 5. Retained-register proxy

The finite retention proxy copies the marker into the register:

$$
U_{\rm retain}=\operatorname{CNOT}_{M\rightarrow R}.
$$

After marking and retention,

$$
|\Psi_{\rm retain}\rangle
=
\frac{|0,0,0\rangle_{SMR}
+e^{i\varphi}|1,1,1\rangle_{SMR}}{\sqrt2}|+\rangle_P
|0\rangle_{W_D}|0\rangle_{W_X}.
$$

When `M,R` are inaccessible to a source-only operation,

$$
\rho_S
=
\operatorname{Tr}_{MR}
|\Psi_{\rm retain}\rangle\langle\Psi_{\rm retain}|
=
E_{\rm mix}.
$$

The complete ideal joint record under a path read of `R` and an `X` read of
`S` is

$$
p(r=0,x=+)=p(r=0,x=-)
=p(r=1,x=+)=p(r=1,x=-)=\frac14.
$$

Resetting the visible value of `R` without recovering `M` leaves the source
reduced state mixed. The witness thereby separates visible reset from coherent
uncomputation at this finite interface.

This construction does **not** certify a stable physical record. It has no
amplifying material, redundant environmental copies, durability interval, or
licensed future grammar under which the record sectors are proved invariant.
`R` is a retained-register proxy showing the typing distinction that a future
B0-E apparatus must realize physically. Calling this qubit itself an
amplified stable record would exceed the witness.

---

## 6. Fixed-background probe control

Apply to the probe the supplied external phase

$$
U_P(\alpha)=e^{-i\alpha Z_P/2}.
$$

With the probe initialized in `|+⟩`, its ideal `X` read is

$$
p_P(+\mid\alpha)=\cos^2\frac\alpha2,
\qquad
p_P(-\mid\alpha)=\sin^2\frac\alpha2.
$$

The phase `alpha` is a fixed-background input in this witness. It is not
generated from `S`, so the witness contains no matter-to-gravity arrow and no
reciprocity.

### 6.1 External-tag nonidentifiability control

Let `V_S` be any one-qubit source operation used by a synthetic context. The
two global unitaries

$$
U^{(0)}=V_S\otimes I_{W_X},
\qquad
U^{(1)}=V_S\otimes X_{W_X}
$$

induce the same reduced source channel from `|0⟩_{W_X}`:

$$
\operatorname{Tr}_{W_X}
\left[
U^{(j)}(\rho_S\otimes|0\rangle\langle0|)U^{(j)\dagger}
\right]
=V_S\rho_SV_S^\dagger,
\qquad j\in\{0,1\}.
$$

But their complete external-tag records differ deterministically:

$$
p(w_X=0\mid U^{(0)})=1,
\qquad
p(w_X=1\mid U^{(1)})=1.
$$

Thus the reduced target gate does not determine every external record.
`W_X` is deliberately the idle-tag limit of that nonidentifiability statement:
it is not coupled source dynamics and has no assigned energy, momentum, work,
or heat. The control proves only that a reduced gate cannot exclude an
unseen external change. It is not a positive realization of the physical
controller/exchange ledger required by Proposition B0-D, and it earns no
conservation coordinate.

---

## 7. Complete noisy reader

The ideal readers are contextual instruments, not one global probability law
over incompatible observables. A licensed context chooses at most one basis
for each role. The witness uses `Z` path/bit reads on `S,M,R,W_D,W_X` where
registered, `X` or `Y` as alternative coherence reads on `S`, and `X` as the
displayed probe read. Projectors on different tensor factors may be combined
inside one context.

For context `c`, with one chosen projector family on each read role, the
complete ideal law is

$$
p_{\rm ideal}(z\mid b,c)
=
\operatorname{Tr}
\left[
\left(
\bigotimes_{j\in J_c}\Pi_{z_j}^{(j,c)}
\right)
\rho_{b,c}
\right],
\qquad
\sum_{z\in\mathcal Z_c}p_{\rm ideal}(z\mid b,c)=1.
$$

There is no licensed joint context containing both `X` and `Y` on the same
source instance. "Complete" means every outcome field, including null and
failure, for one declared context—not a hidden joint distribution across
incompatible contexts.

Use the same three-outcome reader form for each binary ideal record. Let

$$
\eta=\frac34,
\qquad
\epsilon=\frac1{10},
$$

where `eta` is the registration probability and `epsilon` is the conditional
binary misclassification probability. If the ideal plus probability is `p`,
the registered law is

$$
\begin{aligned}
q(+\mid p)&=\frac34\left(\frac9{10}p+\frac1{10}(1-p)\right)
=\frac3{40}+\frac35p,\\
q(-\mid p)&=\frac34\left(\frac1{10}p+\frac9{10}(1-p)\right)
=\frac{27}{40}-\frac35p,\\
q(\varnothing\mid p)&=\frac14.
\end{aligned}
$$

All three probabilities are nonnegative and sum to one for `0 <= p <= 1`.

For the coherent source `X` read,

$$
q_X(+\mid E_\varphi)=\frac38+\frac3{10}\cos\varphi,
\qquad
q_X(-\mid E_\varphi)=\frac38-\frac3{10}\cos\varphi.
$$

The exact cases are:

| preparation | `q(+)` | `q(-)` | `q(null)` |
|---|---:|---:|---:|
| `E_+`, `varphi=0` | `27/40` | `3/40` | `1/4` |
| `E_-`, `varphi=pi` | `3/40` | `27/40` | `1/4` |
| `E_mix` | `3/8` | `3/8` | `1/4` |
| retained source, source-only read | `3/8` | `3/8` | `1/4` |
| `E_varphi`, `varphi=pi/2`, X read | `3/8` | `3/8` | `1/4` |

The `Y` read separates the held-out `pi/2` coherent preparation from the
mixture and remains separated after the same reader noise, using the formula
above with `cos(varphi)` replaced by `sin(varphi)`.

For independently read source and probe roles, the registered joint law is the
product of their complete three-outcome laws only if the nuisance parent
certifies their independence.

### 7.1 General complete joint reader

For a joint context, let `z` be the complete ideal record, `n` a retained or
integrated nuisance value with normalized law `mu`, and `y` the complete
registered record including null fields. A correlated reader is a stochastic
kernel

$$
K_n(y\mid z)\ge0,
\qquad
\sum_y K_n(y\mid z)=1.
$$

The registered law is

$$
p_{\rm reg}(y\mid b,c)
=
\sum_{z,n}
K_n(y\mid z)\,\mu(n\mid b,c)\,p_{\rm ideal}(z\mid n,b,c),
$$

where the conditional ideal law is normalized for every admitted `n`.

Consequently

$$
\sum_y p_{\rm reg}(y\mid b,c)=1
$$

without assuming that different record fields are independent. The product of
the one-field `q` kernels is one allowed special case, not the general law.

---

## 8. Complete shared-nuisance countermodel

Take ideal source and probe reads that would both return `+`. Let the source
and probe registration bits be independent with registration probability
`eta=3/4`. Conditional on registration, let one common unobserved nuisance bit
`N` flip both signs with probability

$$
p(N=1)=\frac14.
$$

Conditional on **both** roles registering, the true sign law is

$$
p(++ )=\frac34,
\quad
p(+-)=0,
\quad
p(-+)=0,
\quad
p(--)=\frac14.
$$

Each conditional sign marginal has flip probability `1/4`. A falsely
factorized model with two independent flip bits and the same marginals predicts

$$
p_{\rm fact}(++ )=\frac9{16},
\quad
p_{\rm fact}(+-)=p_{\rm fact}(-+)=\frac3{16},
\quad
p_{\rm fact}(--)=\frac1{16}.
$$

The earlier two-by-two display is therefore a conditional table, not a
complete reader. Including null records gives the common-nuisance law

| source / probe | `+` | `-` | `null` |
|---|---:|---:|---:|
| `+` | `27/64` | `0` | `9/64` |
| `-` | `0` | `9/64` | `3/64` |
| `null` | `9/64` | `3/64` | `1/16` |

and the falsely factorized law

| source / probe | `+` | `-` | `null` |
|---|---:|---:|---:|
| `+` | `81/256` | `27/256` | `36/256` |
| `-` | `27/256` | `9/256` | `12/256` |
| `null` | `36/256` | `12/256` | `16/256` |

Both complete tables are normalized. Both have the same one-role marginals

$$
p(+)=\frac9{16},
\qquad
p(-)=\frac3{16},
\qquad
p(\varnothing)=\frac14,
$$

while their correlations differ. The nuisance flip probability `1/4` is a
separate hostile control, not the single-reader misclassification parameter
`epsilon=1/10` used in Section 7. A shared
laser, support, field supply, shield vibration, or acquisition error can
therefore imitate or hide a joint source--probe signature without changing
the separate calibration marginals.

---

## 9. Normalization audit

Every ideal branch is generated from the common seed by a unitary. Every
registered binary reader is completed by the null outcome. Every correlated
joint reader is required to satisfy the stochastic-kernel normalization in
Section 7.1. Hence for every preparation, marker context, probe phase, and
readout context,

$$
\sum_{r_S,r_M,r_R,r_P,r_{W_D},r_{W_X}}
p_{\rm syn}
(r_S,r_M,r_R,r_P,r_{W_D},r_{W_X}\mid b,c)=1.
$$

Each record symbol in this sum denotes the single basis licensed for that role
by `c`; the equation does not combine incompatible source reads.

The complete shared-nuisance table sums to one because it combines normalized
registration bits with a normalized common-flip mixture. The factorized mutant
is also normalized. Normalization alone cannot detect false independence;
joint held-outs are required.

---

## 10. Attacks passed by construction

The witness distinguishes:

1. coherent phase from a diagonal mixture using two quadratures;
2. a reversible mark from a retained-register proxy, without claiming
   physical record stability;
3. coherent uncomputation from visible reset;
4. complete records from accepted-only records;
5. a fixed external probe phase from a reciprocal source response;
6. a common nuisance parent from factorized marginals; and
7. identical reduced source operations with distinct uninterpreted external
   tags, without claiming a physical exchange ledger.

It also demonstrates that these are independent gates: normalization does not
prove physical source descent, correct marginals do not prove a correct joint
law, and a restored fringe before amplification does not prove that a stable
record can be reversed.

---

## 11. Deliberate failures and ceilings

This witness deliberately fails the real B0 requirements:

1. its source, marker, probe, and record are abstract qubits;
2. it has no mass distribution, trap, support, actuator, or material reader;
3. `R` is only a retained-register proxy, not an amplified durable record with
   a proved stable-future grammar;
4. `W_D,W_X` are abstract finite tags, not calibrated energy, momentum, heat,
   recoil, or boundary-flux carriers, so it has no physical conservation
   closure;
5. it has no electromagnetic, Casimir, thermal, collisional, seismic, or
   backaction physics;
6. it is handed the preparation family and external probe phase;
7. it has no no-refit transfer to another apparatus;
8. it has no dynamical gravity or reciprocal response; and
9. it has no microscopic actuality claim.

Therefore its maximum status is author-side `B0-L2` evidence if independently
rebuilt under a future pin. No level is awarded here.

---

## 12. Maximum legitimate claim

> One exact finite standard-quantum witness realizes the B0 matched-diagonal,
> coherence, temporary-marker, coherent-eraser, retained-register,
> fixed-background phase, complete-reader, and correlated-nuisance interface
> types. Its complete null-inclusive record laws are positive and normalized,
> and exact countermodels show why a second quadrature, physical stable-record
> certification, null outcomes, and a common nuisance parent are necessary.
> The retained qubit and external tag are deliberately not a durable material
> record or physical exchange ledger. The witness is an abstract interface
> test, not a massive apparatus, gravity law, ontology, experiment, or
> discharge of `P-B0-1`.
