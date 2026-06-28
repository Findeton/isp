# The record click-law, XX: deterministic record machines and the click-law without primitive stochasticity

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-22. Twentieth paper of the v7 program. This paper investigates whether the record click-law can be read as the shadow of deterministic hidden machines rather than as a primitive stochastic process. Tags: **[FORCED]** = required by existing v7/v6 constraints; **[REALIZATION]** = an explicit deterministic representation of an already-forced record law; **[CONSTRAINED]** = narrowed but not unique; **[NO-GO]** = impossible within the stated scope; **[OPEN]** = a disclosed unsolved obligation. All new numerical checks are receipted in `v7/code/p20_deterministic_machines.py` at mpmath `dps = 140`; inherited receipts were rerun in the project venv.

## Abstract

The sealed-record corpus has been written in the language of stochastic processes: survival probabilities, Markov collars, Poisson evidence clocks, positive kernels, and hidden-process realizations. This paper asks whether that language is fundamental. The answer is a sharp **yes-but**. Primitive stochastic ontology can be demoted, but the record-facing **measure** cannot be removed. A deterministic hidden substrate is admissible only as a **measure-preserving sealed transducer**: a deterministic update on a hidden measure space, a record partition, an orthogonal seal projection, and an additive evidence cocycle. Without the measure there is no KL content, Fisher capacity, Born weight, moment matrix, or survival law.

The core construction is a deterministic realization of Paper I's evidence clock. Take a two-sided Bernoulli tape `(...,U_-1,U_0,U_1,...)`, the invertible shift, and roof times `I_n = -log U_n`. The special flow under this roof is deterministic, invertible, and measure-preserving. From the post-seal section,

$$
\Pr_\mu(I_n>I)=e^{-I},
$$

and because the roof is exponential, the stationary residual survival is also `exp(-I)`. Thus the dense record-facing law is exactly `S(chi)=exp(-kappa chi)`. Nothing random happens once the hidden tape is fixed; the randomness is the invariant measure over hidden states. In the sparse regime, for any chosen lattice/mode spacing `d`, a Bernoulli skeleton with no-click probability `s` gives exactly `S(nd)=s^n`; choosing `s=exp(-kappa d)` samples the dense exponential on that chosen seal lattice.

This does **not** loosen the v7 constraints. Multiplicativity is not automatic for arbitrary hidden sections; it is the deterministic-machine version of Paper I's dense-refinement, single-channel, stationarity hypotheses. Under those hypotheses, the Cauchy equation still forces the exponential. On a sparse lattice it still forces only the geometric skeleton, leaving the inter-seal coherent profile free. A closed finite deterministic automaton cannot realize the exact unbounded dense clock without a non-atomic hidden measure, an infinite symbolic reservoir, or an external tape. A fixed-grid nearest-neighbor CA fails as a fundamental relativistic substrate by importing a preferred frame; a Lorentzian sprinkling machine cannot select a finite-valency collar by a Lorentz-invariant rule, by the BHS obstruction. Such machines may still serve as gauge-fixed approximations or emergent simulators; they are not fundamental record substrates.

The Bell bookkeeping must also be sharpened. With a complete deterministic hidden state, outcome-independence is automatic for local outcome functions. Therefore a Bell-violating deterministic record machine cannot be Bell-local. Assuming measurement independence/free settings and a complete hidden state, it must fail local factorization: there is no representation of the readout by local response functions `A_x(lambda), B_y(lambda)`, even with an arbitrary shared hidden measure `mu(lambda)`. Operational no-signaling is kept only after pushing forward by the invariant measure. This is the deterministic version of the v7 Bell guardrail; it does not license a superdeterministic loophole, and it does not prove a no-go for theories that explicitly abandon measurement independence.

The payoff is conceptual: the click record law becomes a deterministic **realization** problem, not a new law. The record-facing law is unique under Paper I's hypotheses; the hidden partition realizing it is highly nonunique. The deterministic substrate also cannot derive the record-blind inputs already classified by Paper XVII: the tensor/local-tomography bit is the clean structural wall, the canonical mode is the weaker/import-fixed mode wall, and the scale/`G` leg is conditional on the Jacobson-Clausius route. A deterministic machine may import those structures; it cannot get them from the record constraints alone.

---

## 1. The replacement: deterministic ontology plus invariant measure

The viable move is not:

`probability disappears`.

That would erase the objects the program has already forced: `chi = D(P_AB || P_BA)`, Fisher capacity, survival, Born weights, moment matrices, and the positive-cone realization criterion. The viable move is:

`primitive stochastic process -> deterministic hidden dynamics + invariant record measure`.

Call a candidate deterministic substrate a **sealed record machine**

$$
M=(X,\Sigma,\mu,T,\Pi_{\mathrm{rec}},E,\rho).
$$

Here `(X, Sigma, mu)` is a hidden measurable state space; `T` is a deterministic update or flow preserving `mu`; `Pi_rec` is the record partition/sigma-algebra; `E` is the seal readout; and `rho` is the evidence increment whose accumulated sum

$$
\chi_n(x)=\sum_{k=0}^{n-1}\rho(T^k x)
$$

is the record odometer in discrete commit order, with the analogous integral for a flow. The stochastic law observed by records is the pushforward of `mu` through `(Pi_rec, E, chi)`. If `mu` is removed, the record probabilities disappear. If `E` is not an orthogonal projection, the q=2/Born seal is lost. If `chi` is not additive and nonnegative, Paper I's odometer is lost. [CONSTRAINED]

The deterministic substrate may be ontic. The record law remains measure-theoretic.

---

## 2. Dense clock realization by a reversible Bernoulli suspension

Paper I's dense click law is `S(chi)=exp(-kappa chi)`. A deterministic hidden realization is obtained from a two-sided Bernoulli suspension.

Let

`Omega = (0,1)^Z`, `mu = Lebesgue^Z`, `theta((U_i)_{i in Z}) = (U_{i+1})_{i in Z}`.

The base update `theta` is deterministic, invertible, and measure-preserving. Define the roof/inter-seal evidence length

$$
I(\omega)=-\log U_0.
$$

Build the suspension space

$$
Y=\{(\omega,a):0\le a<I(\omega)\}
$$

with normalized measure `dnu = dmu(omega) da / E_mu[I]`. The deterministic flow `Phi_t` increases the age `a` by `t`; when `a` reaches `I(omega)`, the seal section is crossed, `a` resets to `0`, and the base point shifts by `theta`. Up to the standard identification of roof endpoints, this is an invertible measure-preserving special flow. The record sigma-algebra of completed seals is generated by the crossed roof sections; the seal projection is conditional expectation onto that committed-record sigma-algebra in `L^2(Y,nu)`. [REALIZATION]

The evidence cocycle is the flow time in evidence units, `rho=1`, so between two seals `chi_t=t`; at a roof crossing the completed interval contributes exactly the roof evidence `I(omega)` to the committed record and the age resets for the next interval.

From the post-seal section `a=0`, the next evidence length satisfies

$$
\mu(I>t)=\mu(U_0<e^{-t})=e^{-t}.
$$

From a stationary point inside the suspension, the residual evidence length has the same survival because the roof is exponential:

$$
\nu(\mathrm{residual}>t)=\frac{\mathbb{E}_\mu[(I-t)_+]}{\mathbb{E}_\mu[I]}=e^{-t}.
$$

Therefore the record-facing dense survival is

$$
S(\chi)=e^{-\kappa\chi}.
$$

Nothing random happens after the hidden tape is fixed. The exponential clock is the record shadow of the invariant non-atomic hidden measure.

The new receipt `p20_deterministic_machines.py` verifies at `dps = 140`: `E[I]=1`, `Var[I]=1`, post-seal survival `mu(I>t)=exp(-t)`, and stationary residual survival `E[(I-t)_+]/E[I]=exp(-t)`, with maximum residual `6.56e-142` on the sampled test points.

---

## 3. Sparse skeleton realization for a chosen lattice

The sparse/indivisible law is deterministic once a sparse lattice is chosen. Papers II-III do **not** derive a canonical scalar `d`: the committed content is mode-dependent and bound-only, every admissible mode sits below `W_*`, and the firing axis carries the evidence clock. So the construction below is conditional on a chosen lattice/mode spacing `L={nd}`.

Let the hidden tape carry symbols `B_i in {0,1}` under the two-sided shift, with invariant product measure

`mu(B_i=0)=s`, `mu(B_i=1)=1-s`.

Read `B_i=0` as no seal at the `i`-th lattice opportunity and `B_i=1` as a seal. Then

$$
S(nd)=s^n=S(d)^n.
$$

Choosing `s=exp(-kappa d)` gives

$$
S(nd)=e^{-\kappa nd},
$$

the dense law sampled on that lattice. This realizes only the sparse skeleton. The inter-seal coherent profile remains the free functional degree of freedom of Paper I. [REALIZATION]

The `p20` receipt verifies the identity for the illustrative values `kappa=0.83`, `d=0.125`; the maximum residual for `0 <= n <= 24` is `6.56e-142`. This is an arithmetic check of the skeleton, not a claim that the chosen `d` is canonical.

---

## 4. Finite deterministic automata: exact dense clocks are impossible

A closed finite deterministic automaton cannot realize the exact dense exponential law for unbounded evidence. Scope: finite state set, deterministic update, stationary initial measure, no external input tape, no non-atomic hidden reservoir, and a seal/target set `A`.

For a first hit of `A`, any trajectory either hits `A` before any non-target state repeats, or never hits. Hence the first-hitting time has support contained in `{0,1,...,N-|A|}` plus a possible atom at `infinity`. It cannot equal a continuum `Exp(1)` law, and it cannot give an exact unbounded geometric renewal law across repeated intervals. Repeated inter-seal intervals in a closed finite deterministic orbit are eventually periodic unless fresh hidden data are supplied. [NO-GO]

The point is not that finite machines are useless. They can approximate finite horizons and can simulate finite experiments. The point is that exact dense sealing needs one of:

- a non-atomic hidden measure;
- an infinite symbolic reservoir;
- an external tape/input stream;
- a continuum or large-state limit;
- or an explicitly stochastic coarse-graining.

The `p20` receipt includes a finite-cycle witness: on a deterministic `97`-cycle with a `12`-state target block, the two-step survival differs from the memoryless square by `0.0980975661600595...`.

---

## 5. What a deterministic machine must preserve

### 5.1 Orthogonal sealing [FORCED]

The record seal remains an orthogonal projection. In a deterministic measure model, the natural representative is conditional expectation onto the sealed record sigma-algebra:

$$
\mathbb{E}_\mu[\cdot\mid \Sigma_{\mathrm{seal}}]:
L^2(X,\mu)\to L^2(\Sigma_{\mathrm{seal}},\mu).
$$

Conditional expectation is an orthogonal projection. This is the deterministic-measure version of Paper I's `E=E*=E^2`. An oblique readout or hidden many-to-one erasure is not a seal unless the erased information is itself ledgered.

### 5.2 Additive evidence [FORCED]

The evidence must be a cocycle/odometer:

`chi(seg1 then seg2) = chi(seg1) + chi(seg2)`, `dchi >= 0`.

The rerun `f3c_sequential_odometer.py` receipt verifies the trajectory entropy-production telescope, the sequential gap `7.745e-121`, and arrow-positivity. In the deterministic machine, this means the evidence function is a genuine additive cocycle, not a side channel chosen after the fact.

### 5.3 Survival-section multiplicativity [FORCED under Paper I hypotheses]

Let `R_chi` be the hidden survival section: the set of hidden states whose current seal has not fired after accumulated evidence `chi`. Multiplicativity is not automatic for arbitrary hidden sections. It is the deterministic-machine restatement of Paper I's dense-regime premises:

- dense refinement points;
- one scalar survival channel;
- stationarity of the channel along the commit order.

Under those hypotheses, refinement consistency gives

$$
\mu(R_{\chi+\psi})=\mu(R_\chi)\mu(R_\psi).
$$

With `S(0)=1`, `0<S<=1`, monotonicity, measurability, and nontriviality, the Cauchy equation forces

$$
S(\chi)=\mu(R_\chi)=e^{-\kappa\chi}.
$$

On a chosen sparse lattice it forces only

$$
S(nd)=S(d)^n.
$$

The self-accounting identity `-log S(chi)=kappa chi` is the conclusion, not an input.

### 5.4 Positive realization at the finite record interface [FORCED in scope]

At the sealed record level, a **stationary finite-valued finite** record law is equivalent to a finite invariant positive cone. This is v6 Paper 16's Heller characterization: the ledger is the cone and its rays are the sealed states. Therefore a hidden deterministic machine may be complicated underneath, but any finite-valued observed process claimed to be a finite sealed law still needs a positive-cone certificate. Finite rank alone is not enough.

This criterion is not being applied to the continuous dense `Exp(1)` clock itself; that clock uses a non-atomic hidden realization. It applies to finite observed record languages, finite sparse skeletons, and finite-valued factors of the hidden machine. The `p20` receipt gives the trivial one-ray cone for the iid sparse Bernoulli skeleton.

---

## 6. Bell-safe deterministic hidden variables

The deterministic-machine picture must not become a Bell-local hidden-variable theory. Assume measurement independence/free settings. A complete deterministic hidden state with local response functions

`a = A_x(lambda)`, `b = B_y(lambda)`

gives outcome-independence automatically and satisfies Bell-local factorization:

$$
P(a,b\mid x,y,\lambda)=P(a\mid x,\lambda)P(b\mid y,\lambda).
$$

That structure is forbidden. It cannot reproduce the record correlations.

Therefore the deterministic record machine must fail **local factorization**, not rely on the old record-level shorthand. Shared hidden randomness is not enough: even an arbitrary global measure `mu(lambda)` is Bell-local if the outcomes are generated by local response functions `A_x(lambda)` and `B_y(lambda)`. The Bell-safe deterministic condition is stronger:

> under measurement independence and a complete hidden state `lambda`, there is no representation of the record readout by local response functions `A_x(lambda), B_y(lambda)`.

Equivalently, the deterministic readout must be genuinely joint/contextual/nonlocal at the ontic readout level, for example a joint setting-dependent map `F_{xy}(lambda)=(a,b)` not decomposable as `(A_x(lambda),B_y(lambda))`. The operational record law must still satisfy no-signaling after pushing forward by `mu`:

`P_mu(a | x,y) = P_mu(a | x)`, `P_mu(b | x,y) = P_mu(b | y)`.

This is the deterministic version of the v7 Bell address. It keeps operational parameter-independence/no-signaling, rejects Bell-local factorization at the ontic readout level, and leaves the entangling complement inside the `Qtilde` envelope. It does not license a superdeterministic loophole, and it is not a no-go theorem for models that explicitly abandon measurement independence.

---

## 7. Cellular automata and computers: scoped constraints

The phrase "cellular automaton" hides several distinct cases.

**Fixed-grid finite-neighbor CA. [NO-GO as fundamental substrate]** A fixed lattice with nearest-neighbor update imports a preferred frame/foliation. It can be a gauge-fixed simulator or an emergent approximation, but it is not an exact fundamental relativistic record substrate.

**Lorentzian sprinkling / causal-set automaton. [NO-GO for finite-valency collar from discreteness alone]** A Poisson/Lorentz-invariant sprinkling preserves the causal order, but BHS blocks a Lorentz-invariant finite-neighbor graph rule. Any finite-valency "nearest collar" rule is frame-dependent. This is the C2 note's point-locality obstruction.

**Order-based non-finite-valency transducer. [CONSTRAINED]** An order-only machine avoids the preferred-grid problem, but it still must pass the point-local scalar premise of Paper VII, the C2 collar gate, and the manifoldlikeness gate of Paper XI. It is covariance-eligible, not automatically covariant.

**Universal computer. [CONSTRAINED]** A universal computer can simulate an exponential clock, a Bell experiment, or a causal set. Simulation is too weak. The record partition must satisfy the SHARD constraints internally: orthogonal seal, additive KL odometer, survival-section multiplicativity, finite positive cone where finite-valued, Bell-safe nonfactorized joint readout, covariance-eligible order, and manifoldlikeness.

Thus the closest acceptable target is a **covariance-eligible deterministic record transducer**:

- deterministic hidden dynamics with invariant measure;
- reversible or fully ledgered hidden update;
- record partition and orthogonal conditional-expectation seal;
- additive RN/KL evidence cocycle;
- Bernoulli/Poisson survival section in evidence units;
- causal order generated by committed seals;
- no preferred finite-valency collar;
- finite positive cone for finite-valued record laws;
- Bell-safe nonfactorized joint readout;
- manifoldlikeness not assumed away.

---

## 8. Deterministic seal-machine law

A valid hidden substrate for one record chain is a deterministic measure-preserving system `(X,mu,T)` or flow with an additive evidence cocycle, a sealed record partition, and nested survival sections `R_chi` such that:

1. `chi` is the record odometer;
2. the seal is the orthogonal projection onto the committed record sigma-algebra;
3. `S(chi):=mu(R_chi)` obeys `S(0)=1`, `0<S<=1`, measurability, monotonicity, and nontriviality;
4. in the dense regime, dense refinement plus single-channel stationarity gives `S(chi+psi)=S(chi)S(psi)`;
5. on a chosen sparse lattice `L={nd}`, the same law is required only on `L`;
6. stationary finite-valued observed laws admit a finite invariant positive cone.

Then:

- in the dense regime, `S(chi)=exp(-kappa chi)` is forced;
- in the sparse regime, `S(nd)=S(d)^n` is forced and the inter-seal profile remains free;
- deterministic hidden realization is possible by the Bernoulli suspension clock / threshold tape;
- the hidden realization does not fix `kappa`, `d`, the inter-seal profile, the tensor product, the canonical mode, or manifoldlikeness.

The click record law is therefore not replaced. It is realized. The uniqueness is law-level only: many hidden partitions and deterministic machines can have the same record-facing survival.

---

## 9. What remains open

1. **Origin of the invariant measure. [OPEN]** The deterministic realization uses an invariant measure. This paper does not derive why the hidden substrate carries that measure rather than another.

2. **Canonical hidden partition. [OPEN]** The Bernoulli suspension realizes the law but does not prove uniqueness of the hidden partition. The record-facing law is unique under Paper I's hypotheses; the hidden realization is not.

3. **Sparse placement and inter-seal profile. [OPEN]** The deterministic machine does not fix the spacing `d`, the inter-seal coherent profile, or whether gravitational sealing is dense or sparse.

4. **Manifoldlikeness. [OPEN]** A deterministic order machine still has to beat the Kleitman-Rothschild dominance problem. Nothing here supplies that selection rule.

5. **Record-blind inputs. [NO-GO/CONSTRAINED]** The deterministic substrate does not derive the composite-state-space bit, the canonical matter mode, or the absolute scale. Paper XVII grades these unevenly: tensor/local-tomography is the clean structural wall; mode is the weaker/import-fixed mode wall; scale/`G` is conditional on the Jacobson-Clausius route. A deterministic machine may import them as hidden structure, but the record constraints do not force them.

6. **Reservoir size versus cone capacity. [OPEN]** A hidden Bernoulli tape can realize the law, while finite-valued record processes need positive-cone certificates. The relation between minimal hidden deterministic reservoir and minimal sealed cone capacity remains open.

---

## 10. What this paper claims and does not claim

It **claims** that primitive stochastic ontology is not required for the click law: a deterministic measure-preserving hidden machine can realize the dense exponential clock and the sparse geometric skeleton exactly. It also claims that this does **not** weaken the existing record constraints: the seal remains an orthogonal projection, evidence remains an additive nonnegative odometer, dense-refinement/single-channel/stationarity still force the exponential law, sparse lattice composition still forces the geometric skeleton, stationary finite-valued record laws still require positive cones, Bell-local deterministic hidden variables remain excluded under measurement independence, fixed-grid finite-neighbor CAs remain nonviable as exact fundamental relativistic substrates, and the Paper XVII record-blind inputs remain unforced.

It **does not** claim that probabilities disappear, that an arbitrary CA is viable, that local hidden variables are restored, that superdeterministic models are ruled out, that the tensor product/local tomography bit is derived, that `kappa` or `d` is fixed, that the invariant measure is uniquely selected, that the hidden realization is unique, or that manifoldlikeness is solved.

The one-line summary:

> the stochastic click process can be re-read as the record shadow of a deterministic measure-preserving hidden machine, but the record law and its no-go constraints are unchanged.

---

## 11. Precision and receipt discipline

New receipt:

- `v7/code/p20_deterministic_machines.py` passed 8/8 at `dps = 140`: Bernoulli roof `E[I]=1`, `Var[I]=1`; post-seal survival `mu(I>t)=exp(-t)`; stationary residual survival `E[(I-t)_+]/E[I]=exp(-t)` with max residual `6.56e-142`; sparse skeleton `S(nd)=S(d)^n` with max residual `6.56e-142`; finite-cycle memoryless obstruction gap `0.0980975661600595...`; and one-ray positive-cone certificate for the iid sparse skeleton.

Inherited receipts rerun in the project venv:

- `v7/code/f3_self_consistency.py` passed: `eta_A`, `theta_A`, `W_*`, Cauchy multiplicativity, `p=1`, no-revival, and Tier-B reparametrization checks; residuals at `~1e-121`.
- `v7/code/f3b_sparse_seal_shape.py` passed: sparse skeleton `S(nd)=S(d)^n`, free inter-seal profile, dense-limit squeeze; maximum lattice residual `1.21e-122`.
- `v7/code/f3c_sequential_odometer.py` passed: sequential entropy-production telescope, odometer additivity, and arrow-positivity; concatenation gap `7.745e-121`.
- `v7/code/f3d_foundational_supports.py` passed: seal/composition bridge, CK gap equals interference cross-term, collar Markov-presentability split; identity gap `6.56e-142`.
- `v7/code/f3e_history_independence.py` passed: single-channel and stationarity premises; multi-channel gap `0.3168`, nonstationary gap `0.18`.
- `v7/code/p2a_content_supply.py` and `v7/code/p3_d_nogo.py` passed: `W_*` ceiling, sub-capacity/mode-dependent content, evidence clock `E[I]=Var[I]=1`, and the scale-bridge no-go.
- `v7/code/p6_transverse_nogo.py` passed: capacity blindness, field blindness, and the almost-quantum envelope; SDP digits are solver-tolerance only, as in the source paper.
- `v7/code/p17_classification.py` passed: Paper XVII's uneven classification of scale/tensor/mode record-blind inputs.

No float64 was used for cancellation-sensitive quantities.

---

## References

**Companion (this program).**

- *The record click-law, I* (`v7/relativistic-isp-v7-paper1-record-click-law`) - orthogonal seal, forced odometer, dense exponential, sparse skeleton, no-revival, one free scale.
- *The record click-law, II-III* (`v7/relativistic-isp-v7-paper2-content-supply`, `v7/relativistic-isp-v7-paper3-seal-spacing-no-go`) - content coboundary, `W_*` ceiling, sub-capacity/mode-dependent firing, evidence clock.
- *The record click-law, IV / VI / XII / XIII* - joint click-law, free entangling complement, almost-quantum envelope, tensor-product/local-tomography no-go.
- *The record click-law, VII* and *Note C2* - conditional covariance, point-local scalar premise, BHS finite-valency collar obstruction.
- *The record click-law, XI* - order + number = geometry up to `l_step`, and the manifoldlikeness gate.
- *The record click-law, XVII* - the three record-blind inputs as one quotient-by-internal-symmetry shape, with uneven epistemic grading.
- v6 Paper 16, *Process-O6 - The Separation Theorem* - finite record laws iff finite invariant positive cone; finite rank is not record realizability.

**External.**

- G. D. Heller / positive-realization theory - finite stochastic/positive realizations by invariant cones.
- Bombelli, Henson, Sorkin - Lorentz-invariant discreteness and the no finite-valency Lorentz-invariant graph obstruction.
- Bell / Jarrett / Tsirelson / Navascues-Pironio-Acin / Navascues-Guryanova-Hoban-Acin - the PI/OI line, Tsirelson envelope, and almost-quantum boundary.
- Rokhlin / Bernoulli shifts / special flows / deterministic dilations of random processes - the measure-preserving background behind deterministic threshold realizations.
