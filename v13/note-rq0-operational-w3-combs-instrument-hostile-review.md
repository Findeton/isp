# Independent hostile review — categorical operational instruments

**Target:** pin `3c958da`, paper `fa02148`  
**Mode:** repository read-only; exact scratch work only in `/private/tmp`  
**Overall verdict:** `HEADLINE-DOWNGRADE`  
**First registered obstruction:** `RQ0-L0-BLOCKED-AT-TESTER-DESCENT`

The first two rungs survive at the paper’s finite, definite-order, candidate-independent admitted-tester scope. The third does not: the proved sheaf is an ambient product of unconstrained probability coordinates, while conversion coherence and common-comb physical realizability are imposed only at the terminal master context. The paper therefore has a sound chart-complete W3 locus and a sound raw coordinate sheaf, but not a physical tester-evaluation descent construction satisfying the pin.

## Registered-rung verdicts

| Registered rung | Verdict | Decision |
|---|---|---|
| `RQ0-L0-COMB-COMPLETE-W3` | **ACCEPT-WITH-FIXES** | Narrowly earned. The flagged construction retains branch weights, CP maps, classical outcomes and quantum outputs. The explicit controls instantiate complete closed experiments. Output/tail wiring and the fine/coarse instrument relationship need corrections, but no counterexample defeats the finite comb construction. |
| `RQ0-L0-TESTER-SEPARATED-W3` | **ACCEPT-WITH-FIXES** | Earned at fixed law-relative tester scope. Preservation and recovery factor through admitted complete-tester probabilities; the imaginary false eraser is rejected and the real contrast passes. Effects are not substituted for disturbance in the decisive controls. |
| `RQ0-L0-W3-TEST-SHEAF` | **NOT EARNED** | The physical evaluation image is not shown to satisfy descent, tester-conversion equations are omitted from the sheaf, general control insertion is mistyped as an affine map of old outcome probabilities, and active physical-symmetry arrows are asserted but not constructed. |
| First exact blocked outcome | **SELECTED** | `RQ0-L0-BLOCKED-AT-TESTER-DESCENT`. |

## Independent reconstruction

The standard comb and interactive-discrimination foundations are appropriately attributed to the quantum-network and strategy literature: [Chiribella–D’Ariano–Perinotti](https://arxiv.org/abs/0904.4483), [Gutoski–Watrous](https://arxiv.org/abs/quant-ph/0611234), and [Gutoski](https://arxiv.org/abs/1008.4636). I found no outsourced programme-specific W3 theorem.

The paper’s exact numerical claims independently survive:

| Quantity | Paper | Independent result |
|---|---:|---:|
| \(A^\*A\) | \(4I\) | \(4I\) |
| Set partitions of four candidate rays | implicit 15 | 15 |
| Eligible \(2+1+1\) candidates | 6 | 6 |
| Eligible \(2+2\) candidates | 3 | 3 |
| Total eligible candidates | 9 | 9 |
| \(\mathcal C_R\), \(2+1+1\) | \(5/4\) | \(5/4\) |
| \(\mathcal C_R\), \(2+2\) | \(1\) | \(1\) |
| Imaginary-cross tester distance | \(0\) | \(0\) |
| Real probability-visible distance | \(1/2\) | \(1/2\) |
| Lüders/reprepare tester distance | \(2\) | \(2\) |

For a two-element block \(B=\{i,j\}\), the omitted fine PVM can be reconstructed as the rays

\[
Q_{B,\pm}
=
\left|\frac{v_i\pm v_j}{\sqrt2}\right\rangle
\left\langle\frac{v_i\pm v_j}{\sqrt2}\right|.
\]

Every written column occupies one of these rays inside \(B\), while a no-write state \(v_i\) has support on both. Three-element blocks contain nonorthogonal, noncollinear restricted write rays and cannot satisfy the required fine-ray condition. This independently produces precisely the six \(2+1+1\) and three \(2+2\) cases.

The recovery formula is also correct:

\[
p_{\rm return}(\pi)
=
\frac1{16}\sum_{B\in\pi}|B|^2,
\qquad
\mathcal C_R
=
2\left(1-p_{\rm return}\right).
\]

The prior operational-Morita counterexample is genuinely repaired. The imaginary term remains \(-i/4\), but its conjugate cancels it in every admitted probability, so tester distance is zero. With the real-phase tester, two source branches contribute weighted \(\ell^1\) distance \(1/4\) each, giving \(1/2\).

## Findings

### F1 FATAL TO THE THIRD RUNG — the sheaf descends arbitrary coordinates, not physical tester evaluations

Paper §§11.1–11.3 defines

\[
\mathcal E(U)
=
\prod_{s,a,\Xi}X_{s,a,\Xi}.
\]

No tester-conversion equation and no common-comb realizability condition is imposed in this product. Its sheaf proof is consequently correct but tautological: coordinatewise data glue because covers are set-theoretic unions.

An exact countermodel shows why this is not physical descent. Let \(A=\{T,T'\}\), where \(T'\) is the same complete binary tester as \(T\) with its outcome handles swapped. Physical evaluations obey

\[
p_{T'}=Kp_T
\]

for the swap matrix \(K\). On singleton contexts choose

\[
p_T=(1,0),
\qquad
p_{T'}=(1,0).
\]

Each singleton datum is separately realizable—by opposite eigenstates—and they agree on the empty overlap. The paper’s union coverage therefore glues them to a global section of \(\mathcal E(A)\). No comb realizes that section, because conversion coherence requires \(p_{T'}=(0,1)\) when \(p_T=(1,0)\).

The same failure occurs without presentation duplicates: deterministic \(Z\)- and \(X\)-test data are separately realizable on singleton contexts but cannot be jointly realized by one qubit state.

The paper explicitly admits that arbitrary sections need not be physical, then defines \(\operatorname{Real}_D(A)\) only at the terminal context. That honesty preserves the raw-sheaf theorem, but it leaves the physical image without a presheaf, fibration, or descent theorem. Membership in a globally defined image is a global acceptance condition, not a construction of tester descent.

**Required replacement sentence:**

> \(\mathcal E\) is an ambient coordinate sheaf whose sections need not respect tester conversions or arise from a common comb. This paper defines a physically realized W3 locus at \(A_D\), but does not prove descent for the realized evaluation image and therefore does not earn `RQ0-L0-W3-TEST-SHEAF`.

### F2 MAJOR — the tester conversion category mistypes quantum control insertion

Paper §10.1 requires every tester conversion, including insertion of a fixed admitted control, to carry an affine map

\[
p_{\mathbf T'}(C)=K_f p_{\mathbf T}(C).
\]

That equation is appropriate for classical postprocessing and for refinement in the forgetful direction. It is false for a general inserted quantum control.

Let \(T\) be computational-basis measurement and let \(T'\) insert a Hadamard before that measurement. States \(|+\rangle\) and \(|-\rangle\) have the same \(T\)-distribution \((1/2,1/2)\) but opposite deterministic \(T'\)-distributions. No affine \(K_f\) acting only on \(p_T\) can produce both.

The correct relation is tester pullback or process pushforward:

\[
T'=S^\*T,
\qquad
p_{T'}(C)=p_T(S(C)),
\]

not generally \(K_fp_T(C)\). Moreover, the later site discards the tester-category arrows altogether and retains only inclusions among subsets of its object set.

**Required replacement sentence:**

> Classical postprocessings act by stochastic affine maps on outcome distributions. Quantum control insertion instead acts by tester pullback \(T\mapsto S^\*T\), with \(p_{S^\*T}(C)=p_T(S(C))\); no affine map from \(p_T(C)\) alone is assumed.

### F3 MAJOR — active physical symmetries are not retained by the displayed stack

Paper §11.1 defines \(\mathfrak S\) with presentation-gauge arrows and says physical symmetries “may” be retained separately. No separate action is defined. Nevertheless, §11.2 says physical-symmetry arrows are retained in

\[
\operatorname{Real}_D(A)//\mathfrak S.
\]

That conclusion does not follow. The quotient only contains arrows actually placed in \(\mathfrak S\). The stackification likewise glues the stated presentation isomorphisms, not an absent active-symmetry action.

This matters because the pin requires physical symmetries to remain as groupoid arrows. Keeping all nine objects without choosing one prevents lexical selection, but it does not construct the required physical-symmetry groupoid.

**Required replacement sentence:**

> The displayed quotient retains presentation-gauge arrows only. No active physical-symmetry action or quotient is constructed here; such an action must be supplied explicitly before physical-symmetry stabilizers can be claimed.

### F4 MAJOR — coarse and fine Lüders instruments are not instrument refinements

Paper §4.2 writes \(\mathbf R\subseteq\mathbf F\) and calls \(\mathbf R\) a coarse record action, but

\[
\mathcal R_r(\rho)=P_r\rho P_r
\]

is not the classical coarse-graining of the fine Lüders branches. The latter is

\[
\sum_{k\in K_r}Q_k\rho Q_k.
\]

For \(P=Q_0+Q_1\) and \(\rho=|+\rangle\langle+|\) inside that block,

\[
P\rho P=\rho,
\qquad
Q_0\rho Q_0+Q_1\rho Q_1
=
\frac12(Q_0+Q_1).
\]

A later \(X\)-basis tester distinguishes these with probabilities \(1\) and \(1/2\). Thus the PVM/effect algebras are nested, but the instruments have different disturbance. This is precisely the effect-versus-instrument distinction the paper otherwise handles correctly.

The W3 calculations survive if the two Lüders instruments are treated as separately admitted counterfactual interventions.

**Required replacement sentence:**

> \(\mathbf R\) coarsens \(\mathbf F\) at the PVM and commutative-algebra level only. Their Lüders instruments are separately admitted interventions and are generally not related by classical outcome coarse-graining.

### F5 MAJOR — the output instrument must be explicitly wired into the tester law

The typed list includes

\[
\mathcal M_j:H_2\to K_j
\]

and says a tail tester acts on \(K_j\), but the decisive norms are written only on \(\boldsymbol{\mathcal V}\star W\) or \(\boldsymbol{\mathcal E}\star W\). The benchmark makes the intended meaning recoverable: the terminal instrument and tail are parts of the complete tester, with source, continuation, output and tail labels jointly retained. The general definition should say this explicitly, otherwise \(\boldsymbol{\mathcal M}\) can appear as an unused field.

A type-safe formulation is to define the induced testers on \(H_2\) by composing every admitted tail tester with the flagged output instrument, retaining the joint \(j,t\) flag. If several output instruments are admitted, that family must be frozen as chart law before the record candidate.

This ambiguity does not defeat the explicit benchmark or the second rung, but it must be fixed before claiming a general complete output-instrument package.

### F6 MINOR — the branch-memory fine actions should be printed

Section 9 states the ray argument but never prints the candidate-dependent fine projectors. The exact reconstruction above proves their existence and leaves all counts unchanged. Printing \(Q_{B,\pm}\) would make the candidate objects determined rather than inferred by the reviewer.

### F7 MINOR — deterministic-comb tensor order is inconsistent as written

The paper declares ascending tensor order \(H_0\otimes\cdots\otimes H_{2N-1}\), but writes

\[
\operatorname{Tr}_{2n-1}C^{(n)}
=
I_{2n-2}\otimes C^{(n-1)}.
\]

Under that declared order, the right side should be

\[
C^{(n-1)}\otimes I_{2n-2},
\]

unless a canonical factor permutation is explicitly inserted. This does not alter the one-step exact controls, but it is a real printed typing defect.

## Mandatory-attack conclusions

- **Completeness of the operational object:** Passes narrowly. Flagged channels retain CP branches, weights, classical flags and quantum outputs. The source-state notation is legitimate because the declared source input is \(I\cong\mathbb C\). No normalized branch is substituted for its weight. The output/tail composite must be made explicit.

- **Record action and support:** The support rule is mathematically sound for positive subnormalized branches. The exact nine-candidate benchmark instantiates it once the omitted fine projectors are reconstructed. The claimed instrument nesting is false and must be replaced by effect-algebra nesting plus separately admitted Lüders interventions.

- **Operational quotient before seams:** Preservation, recovery and \(\mathcal C_R\) genuinely use complete-tester probabilities. The quotient removes the imaginary dormant coefficient. Candidate independence is a declared chart-law postulate, not a derived theorem, and the paper mostly labels it honestly.

- **Effects versus disturbance:** Passes in the load-bearing controls. The Lüders/reprepare example has identical POVM effects but tester distance \(2\), so the paper does not identify effects with instruments. The terminal block theorem is correctly limited to separating one-step effect laws. F4 is a localized relapse in the fine/coarse terminology.

- **Tester category and physical referents:** Every named tester in the exact controls is a normalized closed experiment. Postprocessing is coherent. General control insertion is not typed by the displayed affine \(K_f\), and the sheaf ignores tester-conversion relations.

- **Ontology firewall:** Passes. The paper consistently separates W3 seam, actual outcome, fact co-reference and event-token identity; confines completeness and global sections to one chart; does not call comb order causal order; and uses RQ0-A only with its supplied regions and maps.

## Four-gate audit

| Object | Verdict |
|---|---|
| Complete comb | **PASS WITH FIXES.** Physical network referent, prior instrument-loss necessity and exact disturbance controls are present. Cut, record action and tester grammar remain disclosed law inputs. |
| Tester quotient | **PASS.** Referent is the admitted family of complete closed experiments; the imaginary/real pair is an exact discriminator; candidate independence is explicitly postulated. |
| Recoverable process coherence | **PASS.** It is an admitted operational \(\ell^1\) contrast, not a matrix coefficient, Born-composition defect or record-multiplicativity defect. |
| Tester-context site | **PARTIAL.** Bare tester subsets have a referent, but physical conversion arrows—especially control insertion—are not represented correctly in the site used for descent. |
| Evaluation sheaf | **FAIL AS PHYSICAL DESCENT; PASS AS RAW COORDINATE SHEAF.** Its unrestricted product sections need not satisfy conversion equations or common-comb realizability. |
| Chart-complete W3 locus | **PASS AS A GLOBAL DEFINITION.** Requiring membership in \(\operatorname{Real}_D(A)\) blocks favorable singleton certification. It is not itself a descended sheaf/fibration, and its active symmetry arrows are missing. |

## Preserved narrower results

The following survive independently:

- finite flagged equivalence between complete instruments and classical-output channels;
- the admitted tester seminorm, operational equivalence and contraction under tester-pullback-preserving supermaps;
- exact tester-visible preservation and recovery definitions;
- terminal effect-block equivalence at its separating-source scope;
- multiplicative-domain sharp transport at its inherited scope;
- unequal-weight and same-POVM/different-disturbance controls;
- inaccessible-spectator and nonfaithful-tester controls;
- the imaginary false eraser and real \(1/2\) contrast;
- the exact nine-candidate classification and \(5/4\) versus \(1\) coherence values;
- the universal/existential variance observation;
- the raw coordinate-product sheaf;
- the physically realized chart-complete W3 locus as a global one-chart definition;
- the complete ontology and one-chart firewall.

## Final disposition

The paper successfully repairs the preceding complete-instrument and false-eraser obstruction. Its strongest surviving registered result is therefore

\[
\boxed{\texttt{RQ0-L0-TESTER-SEPARATED-W3}}
\]

at finite-dimensional, definite-order, one-chart, law-relative admitted-tester scope, subject to the listed typing clarifications.

The claimed W3 test sheaf is not earned. The exact registered disposition is

\[
\boxed{\texttt{RQ0-L0-BLOCKED-AT-TESTER-DESCENT}}.
\]

This is not a failure to select an outcome, derive co-reference, or construct an atlas; those were correctly excluded. It is the narrower failure to construct physical, conversion-coherent descent of tester-evaluated W3 data. No intrinsic locality, overlap, topology, causality, fields, or gravity follows.
