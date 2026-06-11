# Free-QFT Matching And Equivalence Benchmarks

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

V2 Paper 8 investigation draft

Date: 2026-05-16

Status: proof-hardened theorem-framework draft. This paper follows V2 Paper 7
and precedes the Lorentz-covariant free-QFT completion now assigned to V2 Paper
9. It proves, conditionally on Paper 7's enriched hypotheses, that the promoted
free Dirac/CAR candidate matches standard massive `1+1D` free QFT on sampled
local field-polynomial observables.

The scope decision is strict:

> Paper 8 is a QFT-matching paper, not a metric or gravity paper. It does not
> try to reconstruct QFT from `Gamma` alone. It tests whether the enriched
> Paper 7 object is equivalent to the standard free Dirac/CAR benchmark on the
> declared sampled sector.

## 1. Why Paper 8 Exists

Paper 7 proved the right kind of mixed result:

```text
Gamma alone -> no unique free QFT
Gamma + lift + polarization + CAR/local net -> conditional free Dirac candidate
```

That is not yet the same as saying:

```text
the candidate matches standard free QFT
```

Paper 8 closes that gap. It should compare every object in the enriched ISP
candidate with the corresponding object in standard massive `1+1D` free
Dirac/CAR QFT.

## 2. Ontological Discipline

Paper 8 keeps five layers separate.

1. **Stochastic data.** Endpoint kernels, exchange curvature, and comparison
   maps. These remain probability-level or algebraic relative-dynamics objects.
2. **Lift data.** The selected Hilbert generator `H_a` and its sampled continuum
   limit.
3. **One-particle QFT data.** The continuum Dirac space, Hamiltonian, spectral
   projections, and time evolution.
4. **Field-theoretic data.** CAR algebra, vacuum, local net, and correlation
   functions.
5. **QFT matching data.** The explicit equivalences between the enriched ISP
   output and the standard free-QFT construction.

The paper's central rule is:

> Matching to standard QFT is a theorem about the enriched representation, not a
> retroactive proof that `Gamma` alone contained the whole QFT.

### 2.1 Barandes Compliance Box

Paper 8 must remain compatible with the indivisible-stochastic-process
standpoint. The following rules are part of the theorem statement, not merely
interpretive commentary.

| Rule | Consequence In Paper 8 |
| --- | --- |
| Whole processes are primary. | Finite kernels and comparison maps describe declared whole slabs, regions, or operational protocols. |
| Division events are physical structure. | No product of unrecorded partial kernels is treated as a Markov decomposition unless the corresponding record/division event is explicitly part of the protocol. |
| Hilbert lifts are representation data. | The selected `H_a`, polarization, CAR functor, and local net are extra enriched inputs, not consequences of `Gamma` alone. |
| Lift phases are not automatically physical gauge. | Schur-Hadamard or unitary lift freedom is quotiented only by the declared unitary/CAR/polarization equivalences. |
| QFT matching is benchmark matching. | Agreement with standard free QFT shows that the enriched ISP representation has the same tested predictions, not that the stochastic ontology has been replaced by fields. |

Thus a successful Paper 8 has the form:

```text
Gamma-level ISP data
+ chosen physically admissible lift data
+ sampled convergence and CAR/local-net enrichment
-> standard free-QFT matching on declared tests.
```

It never has the form:

```text
Gamma alone -> unique standard QFT.
```

## 3. Export Ledger From Paper 7

Paper 8 may use exactly the following.

| Source | Exported To Paper 8 | Not Exported |
| --- | --- | --- |
| Theorem 10.2 | Gamma-only no-go. | A reason to abandon enriched reconstruction. |
| Section 11 | Minimal counterexamples separating phase, Fock/statistics, and local-net data. | Full QFT inequivalence classification. |
| Theorem 12.1 | Sampled one-particle Dirac convergence. | All-mode lattice convergence. |
| Section 12.3 | Explicit doubler policy. | A Wilson theorem or full finite-lattice Fock theorem. |
| Proposition 12.2 | Sampled spectral projection convergence. | Gamma-derived vacuum uniqueness. |
| Proposition 12.3 | CAR vacuum correlation convergence. | All Wightman axioms. |
| Proposition 12.4 | Finite-polynomial stochastic-curvature response. | Closed local-net derivation or full Lorentz covariance. |
| Theorem 12.5 | Conditional free Dirac/CAR promotion theorem. | Standard QFT equivalence without additional matching checks. |

Therefore Paper 8 must not assume:

1. full Lorentz covariance;
2. Reeh-Schlieder or full Haag-Kastler completeness unless explicitly invoked
   from the standard free Dirac theorem;
3. all-mode finite lattice Fock convergence;
4. stress-energy reconstruction;
5. metric extraction;
6. dynamical geometry.

## 4. Standard Free-QFT Target

The target is the standard massive free Dirac/CAR theory in `1+1D`.

One-particle data:

```math
\mathcal H=L^2(\mathbb R,\mathbb C^2),
\qquad
H_D=-i\alpha\partial_x+m\beta,
\qquad
m>0.
```

Spectral projections:

```math
P_\pm=1_{\mathbb R_\pm}(H_D).
```

Field algebra:

```math
\mathrm{CAR}(\mathcal H)
```

with quasifree vacuum `\Omega` determined by the positive-energy polarization.

Equal-time local net:

```math
\mathcal A(I)=C^*\{\psi(f),\psi(f)^*:\operatorname{supp}f\subset I\}.
```

Time evolution:

```math
\alpha_t(\psi(f))=\psi(e^{-itH_D}f).
```

The matching question is whether the enriched ISP construction gives this same
object, up to the declared unitary/CAR/polarization equivalences.

## 5. Matching Table

| Standard QFT Object | Enriched ISP/Paper 7 Object | Matching Condition |
| --- | --- | --- |
| `\mathcal H` | sampled spaces `\mathcal H_a` and maps `\iota_a` | sampled one-particle convergence |
| `H_D` | finite lifts `H_a` | Theorem 12.1 |
| `P_\pm` | finite projections `P_{a,\pm}` | Proposition 12.2 |
| CAR functor | finite CAR algebras `\mathrm{CAR}(\mathcal K_a)` | representation input plus projection convergence |
| vacuum `\Omega` | quasifree vacua `\Omega_a` | two-point and Wick/Pfaffian convergence |
| local net `I\mapsto\mathcal A(I)` | `I\mapsto\mathcal A_a(I)` | support sampling and correlation convergence |
| time evolution `\alpha_t` | lifted finite dynamics | sampled evolution convergence |
| tested curvature response | Paper 1/Paper 7 `K_\parallel[\xi]` response | Proposition 12.4 |

### 5.1 Standing Matching Convention

Let

```math
\mathscr D=C_c^\infty(\mathbb R,\mathbb C^2),
\qquad
\mathscr D(I)=\{f\in\mathscr D:\operatorname{supp}f\subset I\}.
```

All limits in Paper 8 are taken with a fixed finite list of test functions in
`\mathscr D`, fixed adjoint choices, fixed finite field-polynomial degree, and
fixed compact time interval unless a theorem explicitly says otherwise. The
basic convergence topology is the weak local-polynomial topology:

```math
B_a(f_1,\ldots,f_k)\to B(f_1,\ldots,f_k)
```

means convergence of all vacuum matrix elements of the fixed sampled field
polynomial, and in particular convergence of vacuum expectations. This is not
operator-norm convergence of the full quasilocal C*-algebra and not all-mode
finite-lattice Fock convergence.

The continuum local algebra is always the universal CAR algebra over the
one-particle test space, represented in the quasifree GNS/Fock representation
selected by the supplied positive-energy polarization. Two promoted theories
are called matched in Paper 8 when the induced CAR isomorphism identifies:

1. the compactly supported smeared-field generators;
2. the local subalgebras generated by `\mathscr D(I)`;
3. the quasifree vacuum state on all fixed local field polynomials;
4. the time-translation automorphisms on sampled local polynomials;
5. the tested curvature-response derivations on their common polynomial domain.

## 6. Theorem 8.1: Local Correlation Matching

**Theorem 8.1: sampled local correlation matching.** Suppose the hypotheses of
Paper 7 Theorem 12.5 hold. Then for every bounded interval `I`, every finite
list of compactly supported test spinors `f_j` with support in `I`, and every
choice `\#_j\in\{\emptyset,*\}`,

```math
\omega_a\!\left(
\psi_a(\iota_af_1)^{\#_1}\cdots\psi_a(\iota_af_k)^{\#_k}
\right)
\to
\omega_{\rm std}\!\left(
\psi(f_1)^{\#_1}\cdots\psi(f_k)^{\#_k}
\right).
```

Here `\omega_{\rm std}` is the standard massive free Dirac vacuum.

Equivalently, `\omega_a` converges to `\omega_{\rm std}` in the weak
local-polynomial topology of Section 5.1.

**Proof.** Let `Q_a` denote the finite quasifree covariance determined by the
sampled positive-energy projection `P_{a,+}`, and let `Q_{\rm std}` denote the
continuum covariance determined by

```math
P_+=1_{(0,\infty)}(H_D).
```

Paper 7 Proposition 12.2 gives, for every fixed `f,g\in\mathscr D`,

```math
\langle \iota_af,Q_a\iota_ag\rangle_{\ell^2_a}
\to
\langle f,Q_{\rm std}g\rangle_{L^2}.
```

Paper 7 Proposition 12.3 then gives convergence of all finite quasifree CAR
correlations whose entries are sampled compactly supported test fields. The
continuum covariance `Q_{\rm std}` is precisely the covariance of the standard
massive free Dirac vacuum with the supplied positive-energy polarization. For a
fixed number of field insertions, the CAR Wick/Pfaffian formula expresses the
`k`-point function as a finite polynomial in the two-point covariances. Pointwise
two-point convergence therefore implies convergence of the fixed `k`-point
function.

No uniformity in `k`, no operator-norm convergence of local algebras, and no
all-mode finite Fock convergence is used here. The theorem is exactly a fixed
local-field-polynomial vacuum-correlation theorem.

This is the first matching theorem. It says the promoted object has the same
local vacuum field-polynomial statistics as standard free QFT on sampled test
fields.

## 7. Theorem 8.2: Equal-Time Local Net Matching

**Theorem 8.2: equal-time local net matching.** Under the same hypotheses, the
continuum net obtained from the enriched ISP/CAR promotion is the standard
equal-time massive free Dirac local net:

```math
I\mapsto C^*\{\psi(f),\psi(f)^*:\operatorname{supp}f\subset I\}.
```

More explicitly, it has:

1. the same smeared-field generators;
2. the same CAR relations;
3. the same local vacuum polynomial expectations by Theorem 8.1;
4. the same isotony relation;
5. the same equal-time graded locality for disjoint intervals.

**Proof.** The CAR algebra over a complex pre-Hilbert space is universal for
generators satisfying

```math
\{\psi(f),\psi(g)^*\}=\langle f,g\rangle,
\qquad
\{\psi(f),\psi(g)\}=0.
```

Paper 7's enriched construction supplies the same continuum test space
`\mathscr D`, the same `L^2` inner product, the same positive-energy
polarization, and the same support assignment as the standard free Dirac
construction. Therefore the identity map on `\mathscr D` is an isometry and
extends uniquely to a CAR `*`-isomorphism between the enriched continuum CAR
algebra and the standard free Dirac CAR algebra.

For each interval `I`, this isomorphism maps the subalgebra generated by
`\mathscr D(I)` onto

```math
C^*\{\psi(f),\psi(f)^*:\operatorname{supp}f\subset I\}.
```

Thus the equal-time local net is matched as a net of generated CAR subalgebras.
Isotony is the inclusion `\mathscr D(I)\subset\mathscr D(J)` when `I\subset J`.
If `I` and `J` are disjoint, then `\langle f,g\rangle=0` for
`f\in\mathscr D(I)` and `g\in\mathscr D(J)`, so odd generators anticommute and
the even subalgebras commute. The vacuum representation is the GNS/Fock
representation of the same quasifree state identified in Theorem 8.1.

The finite-regulator algebras `\mathcal A_a(I)` converge only in the sampled
vacuum-polynomial sense stated in Section 5.1. The exact C*-net equality is a
continuum enriched-representation statement, not a claim that every finite
lattice algebra is already the continuum local algebra.

## 8. Theorem 8.3: Dynamics And Spectrum Matching

**Theorem 8.3: time-evolution and spectrum matching.** Under the same
hypotheses, for every fixed compact time interval `[-T,T]`:

1. finite sampled dynamics converge to standard Dirac time evolution;
2. the induced CAR automorphisms converge on local field polynomials in vacuum
   matrix elements:
   ```math
   \alpha_{a,t}(\psi_a(\iota_af))
   \to
   \psi(e^{-itH_D}f);
   ```
3. the physical field Hamiltonian is the standard positive-energy
   second-quantized Hamiltonian relative to the supplied Dirac polarization;
4. the vacuum is invariant under `\alpha_t`;
5. the physical spectrum is nonnegative after the standard vacuum-energy
   normalization.

More explicitly, for every `f\in\mathscr D`,

```math
\sup_{|t|\le T}
\left\|
e^{-itH_a}\iota_af-\iota_a e^{-itH_D}f
\right\|_{\ell^2_a}
\to0.
```

Consequently, for every fixed local field polynomial `B`,

```math
\omega_a(\alpha_{a,t}(B_a))\to\omega_{\rm std}(\alpha_t(B)),
```

uniformly for `t` in compact intervals whenever the one-particle convergence is
uniform for the finite list of test functions appearing in `B`.

**Proof.** Paper 7 Theorem 12.1 gives the displayed sampled one-particle
convergence, uniformly for `t` in compact intervals. The CAR functor sends a
one-particle unitary `U` to the automorphism

```math
\psi(f)\mapsto\psi(Uf).
```

Therefore the finite lifted one-particle dynamics induce finite CAR
automorphisms whose action on a fixed sampled field polynomial is obtained by
replacing each test function by its evolved sampled test function. The
one-particle convergence above and the CAR norm bound
`\|\psi(f)\|\le \|f\|` control each fixed word. Applying Theorem 8.1 to the
finite list of time-evolved test functions gives convergence of vacuum matrix
elements.

Paper 7 Proposition 12.2 identifies the positive-energy polarization on sampled
test fields. The standard CAR/Fock construction over this polarization gives the
usual positive-energy second-quantized Hamiltonian, leaves the quasifree vacuum
invariant, and has nonnegative spectrum after subtracting the conventional
vacuum energy. This spectral statement is a statement about the supplied Fock
representation. It is not derived from endpoint `Gamma` data alone.

This theorem is still sampled-sector. It does not say every finite-lattice mode
has matched the standard continuum Fock construction.

## 9. Theorem 8.4: Tested Covariance Matching

Paper 7 gives a tested stochastic-curvature response:

```math
\delta_\xi^{\rm test}(\psi(f))=\psi(K_\parallel[\xi]f).
```

Paper 8 compares this with the standard free Dirac action of the same
one-particle differential operator on field polynomials.

**Theorem 8.4: tested curvature-response matching.** Under the Paper 7
hypotheses, let `\xi\in C_c^\infty(\mathbb R)` and let `B` be a finite local
field polynomial whose test functions lie in the common polynomial domain of
`K_\parallel[\xi]`. Then

```math
\omega_a(\delta_{a,N,M}B)\to
\omega_{\rm std}(\delta_\xi^{\rm std}B),
```

where `\delta_\xi^{\rm std}` is the standard CAR field-polynomial action induced
by `K_\parallel[\xi]`.

Here `\delta_{a,N,M}` and `\delta_\xi^{\rm std}` act by the Leibniz rule on the
fixed polynomial algebra; no closed C*-derivation is claimed.

**Proof.** Paper 7 Proposition 12.4 gives

```math
\omega_a(\delta_{a,N,M}B)\to\omega(\delta_\xi B)
```

for the continuum quasifree CAR state produced by the enriched ISP promotion.
Concretely, if

```math
B=\psi(f_1)^{\#_1}\cdots\psi(f_k)^{\#_k},
```

then `\delta_\xi B` is the finite sum obtained by replacing one entry at a time
by `\psi(K_\parallel[\xi]f_j)^{\#_j}` with the appropriate adjoint convention.
The one-particle stochastic-curvature convergence controls each replacement,
and the CAR norm bound controls each fixed operator word. Theorem 8.1 then
identifies the limiting quasifree state `\omega` with the standard massive free
Dirac vacuum `\omega_{\rm std}` on all field polynomials appearing in this
finite sum. The one-particle operator in both actions is the same
`K_\parallel[\xi]`, so the limiting response is precisely the standard
free-QFT field-polynomial response.

This is not full Lorentz covariance. It is a standard-QFT matching statement for
the specific stochastic-curvature generator that Paper 1 and Paper 7 control.

## 10. Theorem 8.5: Final Free-QFT Matching Theorem

**Theorem 8.5: sampled-sector standard free-QFT matching.** Under the hypotheses
of Paper 7 Theorem 12.5, the enriched relativistic ISP free Dirac/CAR candidate
matches the standard massive `1+1D` free Dirac/CAR QFT on the sampled local
field-polynomial sector.

The matching includes:

1. local vacuum field-polynomial correlations;
2. equal-time CAR local-net structure;
3. time evolution and positive-energy spectrum after the supplied polarization;
4. finite-propagation/locality properties inherited from the free Dirac equation;
5. the tested stochastic-curvature field-polynomial response.

The matching explicitly excludes:

1. QFT reconstruction from `Gamma` alone;
2. all-mode finite lattice Fock convergence;
3. boost covariance or full Lorentz covariance;
4. Wightman/Haag-Kastler completeness beyond the equal-time net plus time
   evolution stated here;
5. stress-energy reconstruction;
6. metric extraction or dynamical geometry.

**Proof.** Use the matching convention of Section 5.1. Theorem 8.1 identifies
the local vacuum field-polynomial statistics. Theorem 8.2 identifies the
equal-time CAR local net through the universal CAR isomorphism and the common
quasifree GNS/Fock state. Theorem 8.3 identifies time translations and the
positive-energy Fock representation on the sampled sector. Theorem 8.4
identifies the controlled stochastic-curvature response on the shared polynomial
domain.

These four statements exhaust the declared equivalence relation. The exclusions
are exactly the structures not supplied by Paper 7 and not proved in Sections
6-9. In particular, the theorem does not convert `Gamma` into a unique QFT; it
shows that the enriched ISP representation, once supplied, has the same tested
free-QFT predictions as the standard massive Dirac/CAR benchmark.

## 11. Boost And Full Lorentz Scope Decision

Paper 8 should explicitly defer boost covariance and full Lorentz covariance.
The reason is not philosophical; it is technical. A boost theorem would require:

1. a common invariant domain for the boost generator;
2. compatibility of boosts with the supplied polarization;
3. covariance of the local net under spacetime transformations, not only
   equal-time support and time evolution;
4. regulator convergence of the corresponding finite transformations.

Paper 7 does not export these. Therefore Paper 8 proves time translations,
positive energy, equal-time graded locality, finite propagation, and tested
curvature response, while marking boost covariance as a later theorem.

## 12. Axiom Audit

Paper 8 includes an explicit audit rather than a vague "QFT recovered" claim.

| QFT Property | Status In Paper 8 |
| --- | --- |
| CAR algebra | matched by construction |
| Equal-time isotony | matched in Theorem 8.2 |
| Equal-time graded locality | matched in Theorem 8.2 |
| Vacuum quasifree correlations | matched on sampled test fields in Theorem 8.1 |
| Positive energy | matched after supplied polarization in Theorem 8.3 |
| Time translations | matched on sampled field polynomials in Theorem 8.3 |
| Finite propagation | inherited from the free Dirac equation |
| Tested stochastic-curvature response | matched in Theorem 8.4 |
| Boost covariance | explicitly deferred |
| Full Wightman reconstruction | not claimed |
| Full Haag-Kastler net in spacetime | only equal-time plus time evolution unless extended |
| Stress-energy tensor | not claimed |
| Metric extraction | deferred to Paper 10 |

Barandes-facing audit:

| Ontological Issue | Status In Paper 8 |
| --- | --- |
| Whole-process stochastic data remain primitive | yes |
| Unrecorded partial-kernel Markov composition avoided | yes, by Section 2.1 and Paper 7 export condition |
| Hilbert lift treated as extra data | yes |
| CAR/Fock treated as extra representation data | yes |
| Gamma-only QFT reconstruction | explicitly denied |
| QFT matching interpreted as operational benchmark equivalence | yes |

## 13. Operational Matching

Paper 8 also translates the algebraic matching into operational language. For
any finite family of detector effects approximating local field-polynomial
expectations, the finite ISP prediction converges to the standard free Dirac
prediction:

```math
\Pr_a(\mathrm{record}\mid \mathrm{setting})
\to
\omega_{\rm std}(E_{\mathrm{setting}}).
```

This statement is conditional on the detector protocol being phase-complete
enough to see the CAR/local algebra data. Endpoint-basis `Gamma` tests alone are
not enough; Paper 7's counterexamples prove that.

## 14. Paper 9 Export Box

Paper 9 may use:

1. Theorem 8.5: the free-QFT candidate matches standard massive `1+1D`
   Dirac/CAR theory on sampled local field-polynomial tests;
2. the stochastic-curvature response matches the corresponding standard
   field-polynomial action;
3. the equal-time CAR local-net and time-translation/positive-energy matching;
4. the explicit list of what is still not matched.

Paper 9's job is to test whether these facts upgrade to a Lorentz-covariant
spacetime free-QFT match: boosts, spacetime local net, microcausality, and a
relativistic axiom audit.

Paper 9 may not use:

1. full Lorentz covariance before it is proved or imported as a standard
   continuum completion;
2. stress-energy reconstruction;
3. a metric coefficient;
4. interacting QFT;
5. all-mode finite lattice Fock convergence;
6. dynamical geometry.

## 15. Initial Work Plan

1. Add the Barandes compliance audit. Done in Sections 2.1 and 12.
2. Prove Theorem 8.1, local correlation matching. Done in Section 6.
3. Prove Theorem 8.2, equal-time local-net matching. Done in Section 7.
4. Prove Theorem 8.3, dynamics and spectrum matching. Done in Section 8.
5. Prove Theorem 8.4, tested curvature-response matching. Done in Section 9.
6. Add the final matching theorem. Done in Section 10.
7. Add the QFT axiom audit table. Done in Section 12.
8. Add the operational matching statement for detector protocols. Done in
   Section 13.
9. Decide whether boosts/full Lorentz covariance are in scope. Deferred in
   Section 11.
10. Export only the matched standard free-QFT facts to Paper 9. Done in
   Section 14.

## 16. Current Verdict

Paper 8 is necessary before the Lorentz-covariant QFT completion, and that
completion is necessary before metric reconstruction. Paper 7 promotes enriched
ISP data to a free Dirac/CAR candidate; Paper 8 now states the conditional
theorem package showing that the candidate matches the standard massive `1+1D`
free Dirac theory on controlled sampled observables.

The strongest honest claim is:

> Enriched relativistic ISP reproduces standard massive `1+1D` free Dirac/CAR
> QFT on sampled local field-polynomial observables, while leaving boost
> covariance, stress-energy, metric data, and dynamical geometry outside scope.
