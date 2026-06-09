# Relativistic ISP V3 Paper 18: Confinement, Uniform Marked KP, And 4D Gauge-Theory Completion Gates

Author: Felix Robles Elvira

## Abstract

Paper 17 completed a conditional mass-gap reduction:

```text
CYM_WL
+ MG-OS-CLOSE
+ cofinal MG-OBS
+ G_j-2PT-KP for every j
+ MG-UNIF(m_*)
+ MG-WP
=> MG-EXP-CLOSE(m_*)
=> MGAP(m_*).
```

Paper 18 asks whether independently proved confinement or area-law estimates
can supply the two remaining dynamical gates:

```text
G_j-2PT-KP for every cofinal mass-gap battery,
MG-UNIF(m_*).
```

The paper is deliberately operational. Wilson loops, Creutz ratios,
Polyakov-loop correlators, and static-potential records are scalar records
of the whole process. Colored charged objects are typed instruments or
boundary probes, not standalone scalar Gamma records. The goal is not to
declare confinement as a slogan, but to build a certificate strong enough to
feed the Paper-17 marked two-point KP and uniform reserve gates.

## 0. Compact Theorem Summary

The target chain is:

```text
CYM_WL
+ confinement record domain CONF-REC
+ renormalized area-law certificate CONF-AL(sigma)
+ marked area-to-surface bridge CONF-MARK_j(sigma)
+ marked surface-polymer stability MS-KP_j for every j
+ cofinal confinement pass CONF-COFINAL-PASS(m_*)
+ whole-process loss ledger CONF-WP
=> G_j-2PT-KP for every j
+ MG-UNIF(m_*)
=> Paper-17 MGAP(m_*).
```

The candidate ISP definition interface is:

```text
4D pure quantum gauge theory in ISP, as a record-law target
:= a whole-process Wilson-loop record law satisfying
   CYM_WL + MG-OS-CLOSE + cofinal MG-OBS + MG-WP.
```

This is a definition interface and reduction target, not an existence theorem
for continuum `4D SU(N)` Yang-Mills.

**Continuum-floor pointer (external review, 2026-05).** The area-law certificate
`CONF-AL(sigma)` that feeds Paper 17's clustering gate is itself reduced (Papers
19-21) to a strict source inequality — the block-plaquette sheet rate must beat
the rooted surface-polymer entropy. That positive source floor is the genuine
content (it is the string tension), and the v3 corpus left it **undecided**
("the current corpus does not prove this… remains open"). The v4 consolidation
(paper 39, Section 11, `TOK-BESSEL`) proves the floor only at *fixed* heat-kernel
collar time `t_- > 0`; uniform survival as `t_- → 0` (a positive continuum string
tension) is the open infrared step and coincides with the open part of the Clay
problem. The ISP suppositions used are existence-type only, so the reduction is
non-circular: the gap is reduced to the floor, not assumed.

The completion target is:

```text
4D mass-gapped confining gauge theory in ISP
:= the above plus CONF-REC + CONF-AL or CONF-CR
   + CONF-MARK_j + MS-KP_j + CONF-COFINAL-PASS + CONF-WP,
   hence Paper-17 MGAP(m_*).
```

### Post-Paper-20 Source Boundary

Paper 18 is a conditional confinement-to-mass-gap bridge. It may be cited
for the formal implication from scalar confinement records, marked-surface
stability, and a same-ledger cofinal pass to Paper 17's mass-gap gates. It
may not be cited as a source theorem for the later Paper-20 SEL2 tree-rate
gate.

In particular, Paper 18 does not prove the Paper-20 same-record coefficient
source

```text
P20-SEL2-TREE-RATE-GATE:
q_rho gamma_rho > Theta_esc^tree
and
T_-^{SEL2} > Theta_T^tree(rho).
```

Nor does it prove the SEL2 block-plaquette coefficient-time lower bound,
the SEL2 heat-kernel coefficient comparison, or any actual area-law input
needed by Paper 20. If a later proof uses those estimates, they must be
proved as separate scalar source theorems on the frozen pushed-forward record
law, not imported from the conditional architecture of this paper.

## 0A. Barandes-Aligned Ontology

The primitive object is still the whole-process law of records. A Wilson loop
is an operational record. A Polyakov loop or static-charge insertion is a
typed boundary instrument. A flux tube is not introduced as a hidden object;
it is shorthand for a stable pattern in scalar loop-record correlations and
surface-polymer expansions.

Paper 18 therefore avoids:

1. treating colored charges as isolated scalar observables;
2. treating gauge-fixed fields as primitive variables;
3. composing unrecorded partial kernels as though the process were
   Markovian;
4. importing a Hilbert-space particle interpretation before OS
   reconstruction.

### Ontology Guardrail

Every object in the confinement proof must pass the following elimination
test before it may enter a final theorem.

1. A surface, sheet, flux-tube, polymer, or hull is an auxiliary estimate for
   closed-loop or marked-loop records.
2. A static charged endpoint is a typed boundary instrument whose scalar
   consequences are Wilson-loop, Polyakov-loop, or marked-loop records.
3. A gauge chart, axial tree, plaquette field, or small-field coordinate is a
   computational chart for record estimates.
4. Any auxiliary object must be eliminated into inequalities among scalar
   records before applying Paper 17's OS and mass-gap theorems.

The final observable content of Paper 18 is therefore only:

```text
scalar loop records
+ typed boundary protocols
+ whole-process limiting laws
+ debited constants.
```

No flux tube, sheet, polymer, gauge-fixed field, or partial transition kernel
is added to the ontology.

## 0B. Honest Boundary

Paper 18 does not yet prove confinement or the Clay mass-gap theorem. It
starts the confinement program by defining exact ISP certificates and proving
the reduction:

```text
confinement certificate strong enough for marked two-point polymers
=> Paper-17 G_j-2PT-KP + MG-UNIF
=> Paper-17 mass gap.
```

The remaining hard work is proving the confinement certificate on the actual
four-dimensional `SU(N)` continuum trajectory.

## 0C. Paper 18 Does / Does Not Prove

| Paper 18 does prove | Paper 18 does not prove |
| --- | --- |
| A candidate ISP record-law definition interface for a four-dimensional pure gauge theory: `CYM_WL + MG-OS-CLOSE + cofinal MG-OBS + MG-WP`. | An unconditional construction or existence theorem for actual continuum `4D SU(N)` Yang-Mills. |
| A conditional confinement-to-mass-gap bridge: sufficiently strong scalar confinement records imply the Paper-17 marked two-point KP gates and `MG-UNIF(m_*)`, hence `MGAP(m_*)`. | The Clay Yang-Mills mass-gap theorem. |
| A finite-battery confinement bridge from clean area-law or Creutz inputs to marked KP and finite-battery exponential clustering. | A proof that actual continuum `4D SU(N)` Wilson loops obey the needed area-law or Creutz lower bounds. |
| A cofinal actual-continuum workbench `AYM-CONF-CLOSE(m_*)`, split into law, window, reserve, loop-modulus, marked-bridge, Gamma-rate, and whole-process audit certificates. | A proof that all those certificates hold on the actual continuum trajectory. |
| Real-constant tail reductions for reserve, loop-modulus, marked KP, and Gamma-rate gates, including explicit pass/fail criteria. | A guarantee that the raw absolute tail routes pass; some raw tail routes are shown to fail unless normalized or finite-window records are used. |
| A Barandes-aligned ontology: scalar loop records, typed boundary instruments, and one whole-process ledger. | Hidden flux tubes, gauge-fixed fields, colored particles, or partial Markov kernels as primitives. |

So the paper is complete as a rigorous conditional architecture and
obstruction map. It is not complete as an unconditional proof of
confinement, mass gap, or actual continuum `4D SU(N)` Yang-Mills.

## 0D. Paper 18 Final Bottleneck

After the Gamma-rate worksheet reductions, the remaining actual-confinement
problem is no longer diffuse. For every cofinal window `j`, define

```text
S_j^RLD =
gamma_15,j underline M_j
- overline epsilon_15,j
- 2 max{overline E_j, 4 overline omega_j / underline kappa_j}.
```

This is the reserve left after the minimal legal loop-modulus debit. Then
define the Gamma pressure surplus

```text
Pi_j =
underline alpha_j S_j^RLD
- (overline epsilon_j + overline h_j + overline lambda_j + overline D_j)
- 2 ell_j overline Delta_j
- 4 ell_j m_*.
```

The finite-window Gamma route closes if, on one frozen whole-process tower,

```text
S_j^RLD > 0
and
Pi_j > 0
for every cofinal j.
```

Equivalently, Paper 18's remaining source problem is:

```text
retained minimal-debit reserve
>
marked/KP pressure + Paper-17 pressure + target-rate pressure
cofinally.
```

This is not a new ontology. It is a scalar record inequality among debited
constants. Proving it on the actual continuum `4D SU(N)` trajectory would
close the Paper-18 confinement-rate source. Failing it names the obstruction:
reserve collapse, loop-modulus overpayment, retained-area collapse,
marked/KP pressure growth, Paper-17 debit growth, target-rate overreach, or
same-ledger mismatch.

## 0E. Source Constants To Prove

The remaining proof obligations are the following constants. Every row must
be certified on the same whole-process tower; otherwise the failure is a
ledger failure rather than a confinement estimate.

| Constant | Source | Needed bound | Current status | Obstruction if failed |
| --- | --- | --- | --- | --- |
| `gamma_15,j` | Paper-15/Paper-16 Creutz readout calibration | positive and same-ledger | named in `AYM-CONF-RES-ATTACK`; actual cofinal lower control open | reserve calibration collapse |
| `underline M_j` | transported Paper-15/Paper-16 reserve after battery, regulator, volume, and shape losses | positive enough after extraction losses | named in `AYM-CONF-RES-ATTACK`; actual source estimate open | no positive finite-window reserve |
| `overline epsilon_15,j` | reserve readout, counterterm, projection, and window errors | smaller than `gamma_15,j underline M_j` after loop debit | named and debited; actual size open | reserve consumed before loop-modulus step |
| `overline E_j` | loop-modulus readout error | contributes through `2 overline E_j`; must not consume reserve | named in `AYM-CONF-LMOD-CONST-ATTACK`; actual bound open | readout overpayment |
| `overline omega_j` | loop-continuity modulus | contributes through `8 overline omega_j / underline kappa_j`; must not consume reserve | named in `AYM-CONF-LMOD-CONST-ATTACK`; actual bound open | loop-continuity error too large |
| `underline kappa_j` | Creutz-slot denominator lower bound | positive on each finite window; tail uniformity only if using tail route | finite-window route declared; raw absolute tail can fail | denominator collapse |
| `underline alpha_j` | marked retained-area conversion | strictly positive; large enough that `underline alpha_j S_j^RLD` beats debits | named in marked geometry; actual cofinal behavior open | retained-area collapse |
| `overline epsilon_j` | marked local endpoint/collar/counterterm/projection loss | finite and small per window | named in `AYM-CONF-MARK-CONST-ATTACK`; actual bound open | marked local loss consumes reserve |
| `overline h_j` | endpoint-enlarged KP height loss | finite and small per window | named in marked KP ledger; actual bound open | marked polymer height pressure |
| `overline lambda_j` | endpoint-enlarged marked activity loss | finite and small per window | named in marked KP ledger; actual bound open | marked activity pressure |
| `overline D_j` | marked KP threshold debit | finite and small per window | named in marked KP ledger; actual bound open | KP threshold pressure |
| `overline Delta_j` | Paper-17 selected-rate debit | finite and small enough that `2 ell_j overline Delta_j` fits the surplus | named in Paper-17 debit ledger; actual cofinal bound open | selected-rate debit consumes physical rate |
| `ell_j` | cofinal battery/window schedule | compatible with all constants and target `m_*` | schedule exists formally; optimal scaling open | target-rate pressure `4 ell_j m_*` overreaches |

The two quantities to prove or falsify are therefore:

```text
S_j^RLD > 0,
Pi_j > 0.
```

The first has now been reduced to the source-import gate
`AYM-CONF-SRLD-SRC_j`, which proves

```text
gamma_15,j underline M_j - overline epsilon_15,j
>
2 max{overline E_j, 4 overline omega_j / underline kappa_j}
=> S_j^RLD > 0.
```

The second has now been reduced to the pressure-import gate
`AYM-CONF-PI-SRC_j(m_*)`, which proves

```text
underline alpha_j S_j^RLD
>
overline epsilon_j + overline h_j + overline lambda_j + overline D_j
+ 2 ell_j overline Delta_j + 4 ell_j m_*
=> Pi_j > 0.
```

Everything else in Paper 18 is now either an input to these inequalities or a
theorem showing what follows from them.

The next proof layer is therefore four concrete actual-constant tasks:

```text
1. AYM-CONF-ACT-RLD_j:
   prove the reserve-loop surplus S_j^RLD>0 from actual 4D SU(N) constants;

2. AYM-CONF-ACT-PI_j(m_*):
   prove the pressure surplus Pi_j>0 after the reserve-loop surplus;

3. AYM-CONF-ACT-LEDGER_j:
   prove all constants are restrictions of one frozen whole-process law;

4. AYM-CONF-ACT-COF(m_*):
   prove the preceding certificates survive on a cofinal sequence.
```

Theorem 4.6I.47z.2e.16 proves that these four certificates close the
minimal-debit Gamma route.

Steps 1 and 2 have now been pushed to worksheet form. The
generic worksheet `AYM-CONF-ACT-WORK_j` lists every constant entering
`S_j^{RLD}` and `Pi_j`, while `AYM-CONF-ACT-RLD-WORK_j` reduces the
reserve-loop attack to the explicit positive margin
`Sigma_j^RLD>0`, and `AYM-CONF-ACT-PI-WORK_j(m_*)` reduces the pressure
attack to the explicit positive margin `Sigma_j^PI(m_*)>0`.
The cofinal worksheet `AYM-CONF-ACT-COF-WORK(m_*)` then states exactly when
those two local margins survive on a tail or on a reindexed cofinal
subsequence.
The reserve-loop bottleneck has now been attacked directly: uniform tail
positivity follows from a strict tail gap `R_R-B_R>=s_R>0`, while weaker
asymptotic or reindexed positivity follows from a positive scaled gap
`r_R>b_R`. If upper reserve and lower debit bounds satisfy `R_j^+<=B_j^-`,
the declared reserve-loop instruments are falsified for that window.
The first concrete asymptotic tail check is now isolated as
`AYM-CONF-ACT-RNUM-TAIL + AYM-CONF-ACT-BDEB-TAIL`: lower-bound the reserve
numerator by `R_R`, upper-bound the loop debit by `B_R`, and test
`R_R-B_R>=s_R>0`.
Step 1 has now been attacked at the source level as
`AYM-CONF-ACT-RLD-SRC-ATTACK`: lower-bound the transported raw reserve by
`C_R`, debit the four extraction losses into `L_R`, and compare
`gamma_R(C_R-L_R)-e_R` against
`2 max{E_R, 4 omega_R/kappa_R}`. The alternative
`AYM-CONF-ACT-RLD-SRC-FALS` records the same-ledger obstruction when that
absolute-tail route cannot pass.
The same attack now has a threshold form:
`C_R >= C_R^crit(s_R)`, where
`C_R^crit(s_R)=L_R+(e_R+2 max{E_R,4 omega_R/kappa_R}+s_R)/gamma_R`.
This identifies `C_R` and `kappa_R` as the fragile actual-dynamics
constants in the absolute-tail route.
The focused `C_R/kappa_R` refinement now splits the denominator attack into
two routes: a separated bound `kappa_j^- >= k_R >0`, or the weaker and often
more realistic quotient bound `omega_j^+ / kappa_j^- <= W_R`. Either route
reduces step 1 to a raw-reserve lower bound against the corresponding
critical threshold.
The quotient bound is now derived from the existing loop-modulus machinery:
`AYM-CONF-ACT-KQ-LMOD(W_R)` asks Paper 16's loop-continuity selector to make
the combined error budget `Omega_j(alpha_Q(j))` no larger than
`W_R kappa_j^-`. This proves `AYM-CONF-ACT-KAPPA-QUOT(W_R)`.
The selector itself has a rate-form sufficient condition
`AYM-CONF-ACT-KQ-RATE(W_R)`: a denominator profile `d_j`, a Paper-16 error
gauge `Xi_j(alpha)`, and the first cutoff with
`Xi_j(alpha_Q(j)) <= W_R d_j`.
The raw-reserve side is now connected back to Paper 16 by
`AYM-CONF-ACT-CRES-P16(c_R)`: import the surface reserve
`M_SUB^{bd}` before paying the Paper-18 extraction losses, or else import
the already-debited Creutz reserve only with the Paper-18 extraction debit
set to zero. This prevents the same battery, regulator, volume, and shape
losses from being charged twice.
Thus step 1 is fully closed as a conditional reduction:

```text
AYM-CONF-ACT-CRES-P16(c_R)
+ AYM-CONF-ACT-KQ-RATE(W_R)
+ c_R >= C_quot^crit(s_R,W_R)
=> AYM-CONF-ACT-RLD-TAIL.
```

What remains outside the formal Paper-18 algebra is the actual source
estimate that the `4D SU(N)` continuum tower supplies the declared
`c_R`, denominator profile, cutoff selector, and threshold inequality.
The pressure bottleneck is parallel: uniform tail positivity follows from
`alpha_P s_R-K_P-T_P>=s_P>0`, while weaker asymptotic or reindexed
positivity follows from a positive scaled pressure gap `a_P>b_P`. If upper
retained-reserve and lower pressure-debit bounds satisfy `A_j^+<=P_j^-`,
the declared pressure instruments and target rate are falsified for that
window.
The concrete pressure tail check is now isolated as
`AYM-CONF-ACT-PNUM-TAIL + AYM-CONF-ACT-PDEB-TAIL(m_*)`: lower-bound the
retained reserve by `A_P=alpha_P s_R`, upper-bound the pressure debit by
`K_P+T_P(m_*)`, and test
`A_P-K_P-T_P(m_*)>=s_P>0`.
Step 2 has now also been closed as a conditional source reduction:

```text
AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)
+ AYM-CONF-ACT-PI-THRESH(s_P,m_*)
=> AYM-CONF-ACT-PI-TAIL(m_*).
```

The import gate says that the same tower supplies the step-1 retained
reserve margin, the marked retained-area and endpoint/KP debit bounds, and
the Paper-17 selected-rate debit bounds. The threshold gate says that the
retained scalar reserve beats those scalar debits by `s_P>0`.
Step 3 is now closed as a same-ledger conditional reduction:

```text
AYM-CONF-ACT-LEDGER-SRC
=> AYM-CONF-ACT-LEDGER-TAIL.
```

This says the step-1 and step-2 constants are restrictions of one frozen
whole-process law, with one disjoint debit register and typed endpoint
instruments eliminated into scalar records.
Step 4 is now closed as a cofinal-survival conditional reduction:

```text
AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)
=> AYM-CONF-ACT-COF(m_*).
```

Combining steps 1--4 gives the minimal-debit source closure:

```text
AYM-CONF-ACT-RLD-TAIL
+ AYM-CONF-ACT-PI-TAIL(m_*)
+ AYM-CONF-ACT-LEDGER-TAIL
+ AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)
=> AYM-CONF-GAMMA-FW-DIRECT(m_*).
```

## 0F. Final Source-Gate Checklist And Handoff

Paper 18's final route is the finite-window minimal-debit route. Earlier
reserve, loop-modulus, marked-bridge, and compact-tail routes remain as
diagnostic reductions, but they are not the canonical endpoint. The canonical
endpoint is:

```text
P16-LAW-IMPORT
+ AYM-CONF-WIN-SCHED
+ AYM-CONF-ACT-CRES-P16(c_R)
+ AYM-CONF-ACT-KQ-RATE(W_R)
+ c_R >= C_quot^crit(s_R,W_R)
+ AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)
+ AYM-CONF-ACT-PI-THRESH(s_P,m_*)
+ AYM-CONF-ACT-LEDGER-SRC
+ AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)
=> AYM-CONF-GAMMA-FW-DIRECT(m_*)
=> AYM-CONF-CLOSE(m_*)
=> MGAP(m_*).
```

The exact source gates that remain outside Paper 18 are therefore:

| Gate | What must be proved on the actual `4D SU(N)` tower | If it fails |
| --- | --- | --- |
| `AYM-CONF-ACT-CRES-P16(c_R)` | Paper 16/Paper 15 exports a same-ledger raw surface reserve, or an already-debited reserve without double-counting Paper-18 extraction losses. | no usable scalar reserve source |
| `AYM-CONF-ACT-KQ-RATE(W_R)` | the Paper-16 loop-continuity selector drives loop/readout error below the moving Creutz-denominator scale. | loop-modulus overpayment or denominator collapse |
| `c_R >= C_quot^crit(s_R,W_R)` | the raw reserve beats the quotient-modulus threshold with positive retained margin `s_R`. | reserve-loop surplus `S_j^RLD` is not positive cofinally |
| `AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)` | the retained reserve, marked retained-area factor, endpoint/KP debits, and Paper-17 selected-rate debits are all exported on the same tower. | pressure constants are not jointly admissible |
| `AYM-CONF-ACT-PI-THRESH(s_P,m_*)` | the retained scalar reserve beats marked/KP/Paper-17/target-rate pressure by positive margin `s_P`. | the physical Gamma rate cannot be certified |
| `AYM-CONF-ACT-LEDGER-SRC` | the reserve and pressure constants are restrictions of one frozen whole-process law with one disjoint debit register. | ledger mismatch or double counting |
| `AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)` | the passing windows form a cofinal scheduled family with the same margins and ledger. | finite-window successes do not become a continuum theorem |

This is the intended boundary of Paper 18. The paper finishes the
Barandes-aligned conditional closure and obstruction ledger. Paper 19 should
attack the actual source estimates, beginning with
`AYM-CONF-ACT-CRES-P16(c_R)`, `AYM-CONF-ACT-KQ-RATE(W_R)`, and the scalar
threshold `c_R >= C_quot^crit(s_R,W_R)`.

## 1. Imports

### 1.1 Paper 16

Paper 16 supplies `CYM_WL`: the continuum Wilson-loop record functional with
reflection positivity, Euclidean covariance, gauge invariance, loop
continuity, nontriviality, and whole-process compatibility.

### 1.2 Paper 17

Paper 17 supplies:

1. cofinal mass-gap batteries `G_j`;
2. `MG-OS-CLOSE`;
3. the marked two-point KP gate `G_j-2PT-KP`;
4. the uniform reserve gate `MG-UNIF(m_*)`;
5. the final theorem:

   ```text
   G_j-2PT-KP for every j + MG-UNIF(m_*) => MGAP(m_*).
   ```

Paper 18 may not assume `G_j-2PT-KP` or `MG-UNIF`; it must attempt to prove
them from confinement data.

### 1.3 Papers 12--15

Papers 12--15 supply:

1. renormalized unsmeared Wilson-loop records;
2. finite-battery loop continuity;
3. finite-block entry data;
4. connected-polymer KP machinery;
5. Creutz and surface-polymer reserves.

Paper 18 uses those tools only as operational record-law estimates.

## 2. Confinement Records

### Definition 2.1: Rectangular Wilson-Loop Record

For a representation `rho` and rectangle `R x T`, define the normalized
scalar Wilson-loop record

```math
W_\rho(R,T)
=
{\rm Re}\,{1\over d_\rho}
\chi_\rho(U_{\partial\Box_{R,T}}).
```

The continuum expectation is

```math
\mathcal W_\rho(R,T)
=
W_\infty(W_\rho(R,T)).
```

All perimeter and cusp counterterms are the Paper-12 renormalized
counterterms. The symbol `W_rho(R,T)` is a scalar loop record, not a
gauge-fixed field observable.

### Definition 2.2: Creutz Ratio Record

At physical increment `s_0`, define the renormalized Creutz-ratio record by

```math
\chi_\rho(R,T;s_0)
=
-\log
{ \mathcal W_\rho(R,T)\mathcal W_\rho(R-s_0,T-s_0)
\over
\mathcal W_\rho(R-s_0,T)\mathcal W_\rho(R,T-s_0) }.
```

The expression is used only on a declared domain where the four loop
expectations are positive and separated from zero by the Paper-13/Paper-15
nontriviality and reserve ledgers.

### Definition 2.3: Polyakov And Static-Potential Records

A Polyakov-loop pair is a boundary-condition record for a typed static
charge-anticharge instrument. Its scalar record is written
`P_rho(x)P_rho(y)^*` only after the boundary instrument has been declared.

The static potential record is the large-time rate

```math
V_\rho(R)
=
-\lim_{T\to\infty}{1\over T}
\log \mathcal W_\rho(R,T),
```

when the limit exists after the same perimeter/cusp and volume ledgers used
for Wilson loops. This is an operational rate extracted from records, not a
primitive force law.

## 3. Area-Law And Confinement Certificates

### Definition 3.1: Renormalized Area-Law Certificate `CONF-AL(sigma)`

For `sigma>0`, `CONF-AL(sigma)` holds on a declared rectangle class if
there are finite constants `K_per`, `K_corner`, and an error modulus
`E_AL(R,T)` with `E_AL(R,T)=o(RT)` such that

```math
-\log |\mathcal W_\rho(R,T)|
\ge
\sigma RT
-K_{\rm per}(R+T)
-K_{\rm corner}
-E_{\rm AL}(R,T)
```

for all sufficiently large rectangles in the class.

The certificate is continuum-facing only if all terms are computed after
Paper-12 renormalization and along the same Paper-16 whole-process tower.

### Definition 3.2: Creutz-Margin Certificate `CONF-CR(sigma)`

`CONF-CR(sigma)` holds if, for a cofinal set of rectangles and increments
`s_0`,

```math
\chi_\rho(R,T;s_0)
\ge
\sigma s_0^2-\epsilon_{\rm CR}(R,T,s_0),
```

where `epsilon_CR` tends to zero along the declared large-rectangle limit and
all finite-volume, smearing, counterterm, and projection losses are debited.

`CONF-CR` is often easier to compare with the Paper-13 and Paper-15 Creutz
ledgers than the raw area law, because perimeter terms cancel to first
order.

### Definition 3.3: Confinement Record Domain `CONF-REC`

`CONF-REC` holds when the confinement records used in the paper live inside
one declared operational domain:

1. all rectangular Wilson-loop records belong to the Paper-16 `CYM_WL`
   closed-loop record algebra after Paper-12 perimeter and cusp
   renormalization;
2. every Creutz ratio is evaluated only where the four loop expectations are
   positive and separated from zero by an explicit nontriviality ledger;
3. static charged records are typed boundary instruments, not standalone
   gauge-invariant scalar records;
4. large-rectangle, large-time, finite-volume, and cutoff limits are taken
   only along the declared whole-process tower.

This is a domain condition, not a confinement estimate. It says exactly
which records the later estimates are allowed to control.

### Definition 3.4: Creutz Domain And Boundary-Protocol Gates

Creutz ratios are logarithms of Wilson-loop expectations. On an unbounded
area-law rectangle class, those expectations usually decay toward zero, so
one should not demand one positive lower bound for all rectangle sizes.
Paper 18 therefore uses finite-window Creutz domains and then passes to a
cofinal sequence of such windows.

For a finite rectangle window `D_CR,J`, the finite-stage Creutz-domain gate
`CR-FIN(alpha,J,kappa_CR,J)` holds on a finite regulator stage `alpha` if:

1. `D_CR,J` is finite and closed under the four rectangles used in the
   Creutz ratio:
   `(R,T)`, `(R-s_0,T)`, `(R,T-s_0)`, and `(R-s_0,T-s_0)`;
2. after Paper-12 perimeter/cusp renormalization, every loop expectation
   appearing in those four slots is real and satisfies

```math
\mathcal W_{\rho,\alpha}(R,T)\ge 2\kappa_{{\rm CR},J}
```

3. the counterterm factors used to define the four expectations are
   positive and belong to the same Paper-16/Paper-17 tower;
4. the same physical increment `s_0` is used for every rectangle in the
   declared finite-stage domain.

The finite-window Creutz continuity gate `CR-CONT(J,kappa_CR,J)` holds if
the finite-stage renormalized loop expectations converge to the continuum
expectations on `D_CR,J` with error smaller than `kappa_CR,J`:

```math
\sup_{(R,T)\in D_{{\rm CR},J}}
|\mathcal W_{\rho,\alpha}(R,T)-\mathcal W_\rho(R,T)|
<\kappa_{{\rm CR},J}
```

eventually along the declared tower.

The finite-window continuum Creutz-domain gate `CR-DOM(J,kappa_CR,J)` holds
on `D_CR,J` if every continuum loop expectation appearing in the four Creutz
slots is real and satisfies

```math
\mathcal W_\rho(R,T)\ge\kappa_{{\rm CR},J}.
```

The strict positivity is needed because Definition 2.2 uses an ordinary real
logarithm of a quotient, not a logarithm of an absolute value.

The cofinal Creutz-domain gate `CR-DOM^cof` holds if there is an increasing
sequence of finite windows `D_CR,J` whose union contains every Creutz
rectangle used later, and each window satisfies `CR-DOM(J,kappa_CR,J)` for
some `kappa_CR,J>0`. No positive lower bound uniform in `J` is required for
domain legality. Uniform lower bounds enter only through later rate
reserves.

### Lemma 3.4A: Finite Positivity Plus Continuity Gives Finite `CR-DOM`

Assume `CR-FIN(alpha,J,kappa_CR,J)` eventually along the tower and
`CR-CONT(J,kappa_CR,J)`. Then `CR-DOM(J,kappa_CR,J)` holds on the declared
finite continuum rectangle window.

Proof.

For every rectangle in the four Creutz slots, finite-stage positivity gives
`W_{rho,alpha}(R,T)>=2 kappa_CR,J`. Continuity transports the expectation by
less than `kappa_CR,J`, so the continuum expectation is at least
`kappa_CR,J`. The same tower and counterterm clauses in `CR-FIN` and
`CR-CONT` ensure this is a statement about the Paper-16 record law, not a
separate regulator object. `square`

### Lemma 3.4B: Cofinal Creutz Domain From Finite Windows

Assume an increasing family of finite windows `D_CR,J` covers the Creutz
rectangles used in the confinement proof. If for each `J` there is
`kappa_CR,J>0` such that `CR-FIN(alpha,J,kappa_CR,J)` holds eventually and
`CR-CONT(J,kappa_CR,J)` holds, then `CR-DOM^cof` holds.

Proof.

Apply Lemma 3.4A to each finite window. The union of the windows covers all
Creutz records used later, so every later Creutz ratio is evaluated in some
finite window where the ordinary real logarithm is legal. `square`

### Definition 3.4C: Finite-Window Creutz Positivity Certificate `CR-POS(J)`

For a finite window `D_CR,J`, let `L_J` be the finite set of all rectangular
loop records appearing in the four Creutz slots over `D_CR,J`. The
finite-window positivity certificate `CR-POS(J,kappa_CR,J)` holds at a
finite regulator stage `alpha` if every `L in L_J` admits a real
decomposition

```math
\mathcal W_{\rho,\alpha}(L)
=
M_{\alpha,J}(L)+E_{\alpha,J}(L),
```

with

```math
M_{\alpha,J}(L)\ge 3\kappa_{{\rm CR},J},
```

and

```math
|E_{\alpha,J}(L)|\le\kappa_{{\rm CR},J}.
```

The intended sources of `M` are a minimal-sheet term, a positive
heat-kernel character coefficient, or another explicitly positive finite
record contribution. The error `E` contains all nonminimal sheets,
finite-volume residues, cutoff mismatch, and counterterm comparison losses.

### Definition 3.4C.1: Positive-Main-Term Dominance Ledger `CR-MTD(J)`

For a finite window `D_CR,J`, `CR-MTD(J,kappa_CR,J)` is a concrete way to
prove `CR-POS(J,kappa_CR,J)`. It consists of:

1. a declared positive source for each loop `L in L_J`, written
   `P_alpha,J(L)`;
2. a decomposition of all remaining contributions into signed or complex
   errors:

   ```math
   E_{\alpha,J}(L)
   =
   E_{{\rm sheet},\alpha,J}(L)
   +E_{{\rm vol},\alpha,J}(L)
   +E_{{\rm cut},\alpha,J}(L)
   +E_{{\rm ctr},\alpha,J}(L)
   +E_{{\rm reg},\alpha,J}(L)
   +E_{{\rm proj},\alpha,J}(L);
   ```

3. a finite-window lower bound

   ```math
   p_{{\rm min},J}(\alpha)
   =
   \inf_{L\in L_J} P_{\alpha,J}(L);
   ```

4. a finite-window error budget

   ```math
   e_{{\rm pos},J}(\alpha)
   =
   \sup_{L\in L_J}
   \left(
   |E_{{\rm sheet},\alpha,J}(L)|
   +|E_{{\rm vol},\alpha,J}(L)|
   +|E_{{\rm cut},\alpha,J}(L)|
   +|E_{{\rm ctr},\alpha,J}(L)|
   +|E_{{\rm reg},\alpha,J}(L)|
   +|E_{{\rm proj},\alpha,J}(L)|
   \right);
   ```

5. the dominance inequalities

   ```math
   p_{{\rm min},J}(\alpha)\ge 3\kappa_{{\rm CR},J},
   ```

   and

   ```math
   e_{{\rm pos},J}(\alpha)\le\kappa_{{\rm CR},J}.
   ```

The positive source `P_alpha,J` may be a minimal-sheet term, a positive
heat-kernel character coefficient, or an imported positive finite-window
Creutz reserve from Papers 13--16. The ontology is unchanged: the source is
only a term in a scalar loop-record estimate.

### Lemma 3.4C.2: `CR-MTD` Proves `CR-POS`

Assume `CR-MTD(J,kappa_CR,J)` holds at a finite regulator stage. Set

```math
M_{\alpha,J}(L)=P_{\alpha,J}(L).
```

Then `CR-POS(J,kappa_CR,J)` holds at that stage.

Proof.

The lower bound in `CR-MTD` gives
`M_alpha,J(L)>=3 kappa_CR,J` for every `L in L_J`. The error decomposition
and budget give `|E_alpha,J(L)|<=kappa_CR,J`. These are precisely the two
inequalities in Definition 3.4C. `square`

### Definition 3.4D: Finite-Window Loop-Continuity Certificate `CR-LCONT(J)`

`CR-LCONT(J,kappa_CR,J)` holds if the Paper-16 loop-continuity and
Paper-12 renormalization ledgers give a finite-window modulus
`omega_CR,J(alpha)` such that

```math
\sup_{L\in L_J}
|\mathcal W_{\rho,\alpha}(L)-\mathcal W_\rho(L)|
\le
\omega_{{\rm CR},J}(\alpha),
```

with

```math
\omega_{{\rm CR},J}(\alpha)<\kappa_{{\rm CR},J}
```

eventually along the declared tower.

### Definition 3.4D.1: Loop-Continuity Modulus Ledger `CR-LMOD(J)`

For a finite window `D_CR,J`, `CR-LMOD(J,kappa_CR,J)` is a concrete way to
prove `CR-LCONT(J,kappa_CR,J)`. It consists of finite-window moduli

```math
\omega_{{\rm CR},J}(\alpha)
=
\omega_{{\rm loop},J}(\alpha)
+\omega_{{\rm ren},J}(\alpha)
+\omega_{{\rm vol},J}(\alpha)
+\omega_{{\rm reg},J}(\alpha)
+\omega_{{\rm proj},J}(\alpha),
```

where:

| Modulus | Source | Meaning |
| --- | --- | --- |
| `omega_loop,J` | Paper 16 | loop-record continuity on the finite window |
| `omega_ren,J` | Paper 12 | perimeter/cusp counterterm convergence |
| `omega_vol,J` | volume ledger | finite-volume exhaustion on the finite window |
| `omega_reg,J` | regulator/chart ledger | regulator and gauge-chart comparison |
| `omega_proj,J` | Paper 17 `MG-WP` | projective finite-record restriction error |

The required inequality is

```math
\omega_{{\rm CR},J}(\alpha)<\kappa_{{\rm CR},J}
```

eventually along the declared tower.

### Lemma 3.4D.2: `CR-LMOD` Proves `CR-LCONT`

Assume `CR-LMOD(J,kappa_CR,J)` holds. Then
`CR-LCONT(J,kappa_CR,J)` holds.

Proof.

For every `L in L_J`, telescope the finite-stage expectation to the
continuum expectation through the loop-continuity, renormalization, volume,
regulator, and projective comparison steps. The five moduli bound the five
increments, so the supremum over the finite set `L_J` is bounded by
`omega_CR,J(alpha)`. The final inequality in `CR-LMOD` is exactly the
strict `CR-LCONT` bound. `square`

### Theorem 3.4E: Finite-Window Creutz Legalization

Assume for a fixed finite window `D_CR,J`:

1. `CR-POS(J,kappa_CR,J)` holds eventually along the regulator tower;
2. all counterterm factors in the four Creutz slots are positive and use the
   Paper-12/Paper-16 normalization;
3. `CR-LCONT(J,kappa_CR,J)` holds.

Then `CR-FIN(alpha,J,kappa_CR,J)` holds eventually,
`CR-CONT(J,kappa_CR,J)` holds, and therefore `CR-DOM(J,kappa_CR,J)` holds.

Proof.

The decomposition in `CR-POS` gives, for every finite-stage loop in the
finite window,

```math
\mathcal W_{\rho,\alpha}(L)
\ge
3\kappa_{{\rm CR},J}-\kappa_{{\rm CR},J}
=
2\kappa_{{\rm CR},J}.
```

Together with positive counterterms and closure of `D_CR,J` under the four
Creutz slots, this is exactly `CR-FIN(alpha,J,kappa_CR,J)`. The modulus in
`CR-LCONT` is exactly `CR-CONT(J,kappa_CR,J)`. Lemma 3.4A then gives
`CR-DOM(J,kappa_CR,J)`. `square`

### Corollary 3.4E.1: Dominance And Modulus Legalize A Finite Window

Assume for a fixed finite window `D_CR,J`:

1. `CR-MTD(J,kappa_CR,J)` holds eventually;
2. `CR-LMOD(J,kappa_CR,J)` holds;
3. all counterterm factors in the four Creutz slots are positive and use the
   Paper-12/Paper-16 normalization.

Then `CR-DOM(J,kappa_CR,J)` holds.

Proof.

Lemma 3.4C.2 gives `CR-POS(J,kappa_CR,J)`. Lemma 3.4D.2 gives
`CR-LCONT(J,kappa_CR,J)`. Theorem 3.4E then gives
`CR-DOM(J,kappa_CR,J)`. `square`

### Corollary 3.4F: Cofinal Creutz Legalization

Assume an increasing finite-window family `D_CR,J` covers every Creutz
rectangle used later. If `CR-POS(J,kappa_CR,J)` and
`CR-LCONT(J,kappa_CR,J)` hold for every `J`, with positive counterterm
factors on each window, then `CR-DOM^cof` holds.

Proof.

Apply Theorem 3.4E to each `J`, then Lemma 3.4B. `square`

### Corollary 3.4F.1: Cofinal Creutz Legalization From Ledgers

Assume an increasing finite-window family `D_CR,J` covers every Creutz
rectangle used later. If `CR-MTD(J,kappa_CR,J)` and
`CR-LMOD(J,kappa_CR,J)` hold for every `J`, with positive counterterm
factors on each window, then `CR-DOM^cof` holds.

Proof.

Apply Corollary 3.4E.1 to each finite window, then Lemma 3.4B. `square`

### Definition 3.4H: First-Battery Creutz Window `D_CR,box`

The first-battery Creutz window `D_CR,box` is the finite set of rectangular
loop records needed to tile the retained block faces in the first
plaquette-clover hull convention of Proposition 4.2A.2a. It is required to
be closed under the four slots of the Creutz ratio:

```text
(R,T), (R-s_0,T), (R,T-s_0), (R-s_0,T-s_0).
```

Let `C_box` be the corresponding finite set of Creutz cells
`C=(rho,R,T;s_0)` in the representation channels used by `G_box`.
When the paper writes `CR-MTD(D_CR,box,kappa_CR,box)` or
`CR-LMOD(D_CR,box,kappa_CR,box)`, it means the finite-window ledgers of
Definitions 3.4C.1 and 3.4D.1 applied to this named window.

The effective first-battery Creutz certificate `CONF-CR_box(sigma)` holds
when:

1. `CR-DOM(D_CR,box,kappa_CR,box)` holds for some `kappa_CR,box>0`;
2. all loop records in `D_CR,box` use the Paper-12 perimeter/cusp
   counterterms and the Paper-16 whole-process tower;
3. for every `C=(rho,R,T;s_0) in C_box`,

   ```math
   \chi_\rho(R,T;s_0)\ge\sigma s_0^2.
   ```

This is the first-battery specialization of `CONF-CR(sigma)`. The symbol
`sigma` is already the effective post-debit Creutz coefficient; any
finite-window transport loss has been consumed before this certificate is
exported to `BOX-RESERVE-PASS(Creutz)`.

### Definition 3.4I: First-Battery Creutz Main-Term Ledger `CR-MTD_box`

For target `sigma>0`, margin `delta_box>0`, and domain constant
`kappa_CR,box>0`, the ledger
`CR-MTD_box(sigma,delta_box,kappa_CR,box)` holds when:

1. the generic positivity ledger `CR-MTD(D_CR,box,kappa_CR,box)` holds
   eventually along the finite-regulator tower;
2. for every finite-stage Creutz cell `C in C_box`, the finite-stage Creutz
   ratio has a main-term decomposition

   ```math
   \chi_{\rho,\alpha}(C)
   =
   Q_{\alpha,box}(C)+E_{\chi,\alpha,box}(C);
   ```

3. the main term has the strict first-battery reserve

   ```math
   \inf_{C\in C_{box}} Q_{\alpha,box}(C)
   \ge
   (\sigma+2\delta_{box})s_0^2;
   ```

4. the signed remainder obeys

   ```math
   \sup_{C\in C_{box}} |E_{\chi,\alpha,box}(C)|
   \le
   \delta_{box}s_0^2.
   ```

Consequently the finite-stage Creutz ratio satisfies

```math
\chi_{\rho,\alpha}(C)
\ge
(\sigma+\delta_{box})s_0^2
```

for every `C in C_box`.

The main term `Q_alpha,box` is not a new physical sheet. It is a declared
positive contribution inside the scalar loop-record estimate, such as a
minimal heat-kernel character term or an imported positive finite-window
Creutz reserve.

### Definition 3.4I.1: Paper-15 First-Battery Creutz Reserve Import `P15-CR-RES_box`

`P15-CR-RES_box` is the import package that lets Paper 18 use the positive
Paper-15 Creutz reserve inside the first-battery Creutz main-term ledger. It
holds when the following data are available on one whole-process tower.

1. Paper 15 has a positive numerical certificate `nCPSC` on a finite battery
   whose Creutz sector contains the first-battery cells `C_box`.
2. The Paper-15 explicit Creutz reserve

   ```text
   M_15^{bd}
   =
   u_-^{N_0}(1-u_+^{Q_sigma})
   - Delta_dec^{bd}
   - T_loss^{bd}
   ```

   is strictly positive.
3. The Paper-15 Creutz anchor and the Paper-18 first-battery Creutz ratio
   are expressed in the same Paper-12/Paper-16 normalization, up to a finite
   calibration constant `gamma_15,box>0`.
4. Any mismatch between the Paper-15 Creutz battery and the first-battery
   cells is bounded by an alignment loss `epsilon_15_to_box>=0`.
5. For every finite-stage first-battery Creutz cell `C in C_box`, there is
   a decomposition

   ```math
   \chi_{\rho,\alpha}(C)
   =
   Q_{15,\alpha,box}(C)
   +E_{{\rm extra},\alpha,box}(C),
   ```

   where the imported Paper-15 part satisfies

   ```math
   \inf_{C\in C_{box}}Q_{15,\alpha,box}(C)
   \ge
   \gamma_{15,box}M_{15}^{bd}
   -\epsilon_{15\to box}
   ```

   eventually along the declared tower.

The exported Paper-15 first-battery reserve is

```math
S_{15,box}
=
\gamma_{15,box}M_{15}^{bd}
-\epsilon_{15\to box}.
```

This definition does not identify a physical sheet. It only says that the
positive Paper-15 Creutz record reserve has been transported into the
finite first-battery Creutz-ratio normalization with a declared loss.

### Definition 3.4I.2: First-Battery Creutz Error Budget `CR-ERR_box`

`CR-ERR_box(delta_box)` holds when the extra first-battery error in
Definition 3.4I.1 has a decomposition

```math
E_{{\rm extra},\alpha,box}(C)
=
E_{{\rm sheet},\alpha,box}(C)
+E_{{\rm vol},\alpha,box}(C)
+E_{{\rm cut},\alpha,box}(C)
+E_{{\rm ctr},\alpha,box}(C)
+E_{{\rm reg},\alpha,box}(C)
+E_{{\rm proj},\alpha,box}(C)
+E_{{\rm bat},\alpha,box}(C)
+E_{{\rm lognorm},\alpha,box}(C),
```

with finite sup-norm bounds:

```math
e_{*,box}(\alpha)
\ge
\sup_{C\in C_{box}}|E_{*,\alpha,box}(C)|.
```

Let

```math
E_{{\rm box}}^{bd}(\alpha)
=
e_{{\rm sheet},box}(\alpha)
+e_{{\rm vol},box}(\alpha)
+e_{{\rm cut},box}(\alpha)
+e_{{\rm ctr},box}(\alpha)
+e_{{\rm reg},box}(\alpha)
+e_{{\rm proj},box}(\alpha)
+e_{{\rm bat},box}(\alpha)
+e_{{\rm lognorm},box}(\alpha).
```

The budget passes if eventually

```math
E_{{\rm box}}^{bd}(\alpha)
\le
\delta_{box}s_0^2.
```

The entries have the following roles.

| Error | Meaning |
| --- | --- |
| `E_sheet` | residual mismatch between the Paper-15 sheet/character expansion and the first-battery Creutz cell |
| `E_vol` | finite-volume exhaustion error |
| `E_cut` | cutoff-removal error at fixed first-battery window |
| `E_ctr` | perimeter, cusp, and local counterterm comparison error not already in `M_15^{bd}` |
| `E_reg` | regulator or gauge-chart comparison error |
| `E_proj` | finite-record projective restriction error |
| `E_bat` | battery-enlargement or first-battery selection error |
| `E_lognorm` | mismatch between Paper-15 anchor normalization and Paper-18 log-Creutz normalization |

No error may be counted here if it has already been debited inside
`Delta_dec^{bd}` or `T_loss^{bd}`. This is the no-double-counting clause.

### Theorem 3.4I.3: Paper-15 Reserve Plus Error Budget Proves `CR-MTD_box`

Assume, for some `sigma>0`, `delta_box>0`, and `kappa_CR,box>0`:

1. the generic positivity ledger `CR-MTD(D_CR,box,kappa_CR,box)` holds
   eventually;
2. `P15-CR-RES_box` holds and exports `S_15,box`;
3. `CR-ERR_box(delta_box)` holds;
4. the Paper-15 imported reserve beats the first-battery target:

   ```math
   S_{15,box}
   \ge
   (\sigma+2\delta_{box})s_0^2.
   ```

Then `CR-MTD_box(sigma,delta_box,kappa_CR,box)` holds.

Proof.

Clause 1 is exactly the generic positivity clause required in
Definition 3.4I. Use the decomposition from `P15-CR-RES_box` and set

```math
Q_{\alpha,box}(C)=Q_{15,\alpha,box}(C),
```

and

```math
E_{\chi,\alpha,box}(C)=E_{{\rm extra},\alpha,box}(C).
```

The Paper-15 import and the reserve comparison give

```math
\inf_{C\in C_{box}}Q_{\alpha,box}(C)
\ge
S_{15,box}
\ge
(\sigma+2\delta_{box})s_0^2.
```

The explicit error budget gives

```math
\sup_{C\in C_{box}}|E_{\chi,\alpha,box}(C)|
\le
E_{{\rm box}}^{bd}(\alpha)
\le
\delta_{box}s_0^2.
```

These are precisely clauses 2--4 of `CR-MTD_box`. `square`

### Corollary 3.4I.4: Paper-15 Reserve Route To `CONF-CR_box`

Assume the hypotheses of Theorem 3.4I.3, `CR-LMOD_box(delta_box,kappa_CR,box)`,
and positive Paper-12/Paper-16 counterterms in the four Creutz slots. Then
`CONF-CR_box(sigma)` holds.

Proof.

Theorem 3.4I.3 gives `CR-MTD_box(sigma,delta_box,kappa_CR,box)`. Theorem
3.4L then gives `CONF-CR_box(sigma)`. `square`

### Definition 3.4I.5: Paper-15 First-Battery Creutz Pass `P15-CREUTZ-PASS_box`

For `sigma>0`, `delta_box>0`, and `kappa_CR,box>0`,
`P15-CREUTZ-PASS_box(sigma,delta_box,kappa_CR,box)` holds when all of the
following are available on one whole-process tower:

1. the generic positivity ledger `CR-MTD(D_CR,box,kappa_CR,box)` holds
   eventually;
2. `P15-CR-RES_box` holds and exports

   ```math
   S_{15,box}
   =
   \gamma_{15,box}M_{15}^{bd}
   -\epsilon_{15\to box};
   ```

3. `CR-ERR_box(delta_box)` holds;
4. `CR-LMOD_box(delta_box,kappa_CR,box)` holds;
5. all counterterm factors in the four Creutz slots of `D_CR,box` are
   positive and use the Paper-12/Paper-16 normalization;
6. the imported Paper-15 surplus beats the first-battery target:

   ```math
   \gamma_{15,box}M_{15}^{bd}
   -\epsilon_{15\to box}
   \ge
   (\sigma+2\delta_{box})s_0^2.
   ```

This certificate is deliberately first-battery. It says that the Paper-15
positive Creutz reserve has been calibrated into the first plaquette-clover
Creutz window and still has enough surplus after the explicitly declared
extra errors.

### Theorem 3.4I.6: `P15-CREUTZ-PASS_box` Proves `CONF-CR_box`

If `P15-CREUTZ-PASS_box(sigma,delta_box,kappa_CR,box)` holds, then
`CONF-CR_box(sigma)` holds.

Proof.

Clauses 1--3 and 6 are exactly the hypotheses of Theorem 3.4I.3, so
`CR-MTD_box(sigma,delta_box,kappa_CR,box)` holds. Clauses 4 and 5 are the
remaining hypotheses needed by Corollary 3.4I.4. Hence
`CONF-CR_box(sigma)` holds. `square`

### Definition 3.4I.7: Upstream First-Battery Creutz Positivity Window

The upstream Paper-15-to-Paper-18 pass has a nonempty positivity window when
the following finite first-battery constants are available on one
whole-process tower:

| Constant | Meaning | Required bound |
| --- | --- | --- |
| `S_15,box` | imported Paper-15 Creutz surplus | `S_15,box>0` |
| `E_box^*` | eventual upper bound for `E_box^bd(alpha)` | finite |
| `omega_box^*` | eventual upper bound for `omega_CR,box(alpha)` | finite |
| `kappa_CR,box` | lower bound for the four Creutz-slot loop expectations | `>0` |

Define the required upstream debit

```math
\delta_{{\rm req},box}
=
\max\left\{
{E_{\rm box}^*\over s_0^2},
{4\omega_{\rm box}^*\over \kappa_{{\rm CR},box}s_0^2}
\right\}.
```

The first-battery Creutz positivity window is nonempty when

```math
S_{15,box}
>
2\delta_{{\rm req},box}s_0^2.
```

When this holds, any choice of `delta_box` and `sigma` satisfying

```math
\delta_{{\rm req},box}
\le
\delta_{box}
<
{S_{15,box}\over 2s_0^2}
```

and

```math
0<\sigma
\le
{S_{15,box}\over s_0^2}
-2\delta_{box}
```

is upstream-admissible.

This is the exact numerical place where the first-battery Creutz route can
fail before the marked-KP bridge is even considered: the Paper-15 surplus
may be positive but too small after the first-battery error and log-modulus
debits.

### Theorem 3.4I.8: Positivity Window Proves `P15-CREUTZ-PASS_box`

Assume:

1. the generic positivity ledger `CR-MTD(D_CR,box,kappa_CR,box)` holds
   eventually;
2. `P15-CR-RES_box` holds and exports `S_15,box`;
3. `CR-ERR_box(delta_box)` holds because eventually
   `E_box^bd(alpha)<=E_box^*<=delta_box s_0^2`;
4. the hypotheses of Corollary 3.4J.2 hold and
   `omega_CR,box(alpha)<=omega_box^*` eventually, with
   `4 omega_box^*/kappa_CR,box <= delta_box s_0^2`;
5. the four Creutz-slot counterterm factors are positive and use the
   Paper-12/Paper-16 normalization;
6. `delta_box` and `sigma` are upstream-admissible in the sense of
   Definition 3.4I.7.

Then `P15-CREUTZ-PASS_box(sigma,delta_box,kappa_CR,box)` holds.

Proof.

Clauses 1 and 2 are clauses 1 and 2 of `P15-CREUTZ-PASS_box`. Clause 3 is
clause 3. Clause 4 gives `CR-LMOD_box(delta_box,kappa_CR,box)` by
Corollary 3.4J.2, which is clause 4. Clause 5 is clause 5.

It remains only to check the surplus inequality. By upstream admissibility,

```math
\sigma+2\delta_{box}
\le
{S_{15,box}\over s_0^2}.
```

Multiplying by `s_0^2` gives

```math
S_{15,box}
\ge
(\sigma+2\delta_{box})s_0^2.
```

Since `S_15,box=gamma_15,box M_15^{bd}-epsilon_15_to_box`, this is exactly
clause 6 of `P15-CREUTZ-PASS_box`. `square`

### Definition 3.4J: First-Battery Creutz Log-Modulus Ledger `CR-LMOD_box`

For `delta_box>0` and `kappa_CR,box>0`,
`CR-LMOD_box(delta_box,kappa_CR,box)` holds when:

1. the generic loop-continuity ledger `CR-LMOD(D_CR,box,kappa_CR,box)` holds;
2. the induced finite-window log-ratio modulus satisfies

   ```math
   \Omega_{{\rm CR},box}(\alpha)
   =
   \sup_{C\in C_{box}}
   |\chi_{\rho,\alpha}(C)-\chi_\rho(C)|
   \le
   \delta_{box}s_0^2
   ```

   eventually along the declared tower.

A sufficient explicit modulus is obtained from the loop-expectation modulus:
if the four loop expectations in every Creutz cell are bounded below by
`kappa_CR,box` in the continuum domain and the finite-stage-to-continuum
loop error is at most `omega_CR,box(alpha)`, then

```math
\Omega_{{\rm CR},box}(\alpha)
\le
{4\omega_{{\rm CR},box}(\alpha)\over\kappa_{{\rm CR},box}}.
```

Thus the displayed `CR-LMOD_box` inequality follows whenever

```math
{4\omega_{{\rm CR},box}(\alpha)\over\kappa_{{\rm CR},box}}
\le
\delta_{box}s_0^2.
```

### Lemma 3.4J.1: First-Battery Creutz Log-Lipschitz Bound

Fix a finite-stage index `alpha`. Assume that for every loop slot `L`
appearing in a first-battery Creutz cell:

1. the finite-stage and continuum loop expectations are real and positive;
2. both are bounded below by the same constant:

   ```math
   \mathcal W_{\rho,\alpha}(L)\ge\kappa_{{\rm CR},box}
   ```

   and

   ```math
   \mathcal W_\rho(L)\ge\kappa_{{\rm CR},box};
   ```

3. the finite-stage-to-continuum loop modulus obeys

   ```math
   \sup_L
   |\mathcal W_{\rho,\alpha}(L)-\mathcal W_\rho(L)|
   \le
   \omega_{{\rm CR},box}(\alpha).
   ```

Then

```math
\Omega_{{\rm CR},box}(\alpha)
\le
{4\omega_{{\rm CR},box}(\alpha)\over\kappa_{{\rm CR},box}}.
```

Proof.

Write a Creutz cell as the four loop slots
`L_1=(R,T)`, `L_2=(R-s_0,T-s_0)`, `L_3=(R-s_0,T)`, and
`L_4=(R,T-s_0)`. Then

```math
\chi_{\rho,\alpha}(C)-\chi_\rho(C)
=
-\log{\mathcal W_{\rho,\alpha}(L_1)\over \mathcal W_\rho(L_1)}
-\log{\mathcal W_{\rho,\alpha}(L_2)\over \mathcal W_\rho(L_2)}
+\log{\mathcal W_{\rho,\alpha}(L_3)\over \mathcal W_\rho(L_3)}
+\log{\mathcal W_{\rho,\alpha}(L_4)\over \mathcal W_\rho(L_4)}.
```

For positive `a,b>=kappa_CR,box`, the mean-value theorem gives

```math
|\log a-\log b|
\le
{|a-b|\over\kappa_{{\rm CR},box}}.
```

Applying this to the four loop slots and summing gives

```math
|\chi_{\rho,\alpha}(C)-\chi_\rho(C)|
\le
{4\omega_{{\rm CR},box}(\alpha)\over\kappa_{{\rm CR},box}}.
```

Taking the supremum over the finite set `C_box` gives the claim. `square`

### Corollary 3.4J.2: Loop-Expectation Modulus Proves `CR-LMOD_box`

Assume:

1. the generic loop-continuity ledger `CR-LMOD(D_CR,box,kappa_CR,box)` holds
   with loop-expectation modulus `omega_CR,box(alpha)`;
2. `CR-DOM(D_CR,box,kappa_CR,box)` holds;
3. the finite-stage loop expectations in the four slots of every
   first-battery Creutz cell satisfy

   ```math
   \mathcal W_{\rho,\alpha}(L)\ge\kappa_{{\rm CR},box}
   ```

   eventually;
4. the small-log-modulus inequality

   ```math
   {4\omega_{{\rm CR},box}(\alpha)\over\kappa_{{\rm CR},box}}
   \le
   \delta_{box}s_0^2
   ```

   holds eventually.

Then `CR-LMOD_box(delta_box,kappa_CR,box)` holds.

Proof.

The generic `CR-LMOD` ledger supplies clause 1 of Definition 3.4J and the
loop-expectation modulus in clause 1 above. `CR-DOM` supplies the continuum
lower bound `W_rho(L)>=kappa_CR,box` on the finite first-battery window.
Clause 3 supplies the matching finite-stage lower bound. Lemma 3.4J.1 gives

```math
\Omega_{{\rm CR},box}(\alpha)
\le
{4\omega_{{\rm CR},box}(\alpha)\over\kappa_{{\rm CR},box}}
\le
\delta_{box}s_0^2.
```

This is clause 2 of Definition 3.4J, so `CR-LMOD_box` holds. `square`

### Corollary 3.4J.3: Practical Reduction Of `CR-LMOD_box`

Assume:

1. the generic positivity ledger `CR-MTD(D_CR,box,kappa_CR,box)` holds
   eventually;
2. the generic loop-continuity ledger `CR-LMOD(D_CR,box,kappa_CR,box)` holds
   with loop-expectation modulus `omega_CR,box(alpha)`;
3. all counterterm factors in the four Creutz slots are positive and use the
   Paper-12/Paper-16 normalization;
4. the small-log-modulus inequality

   ```math
   {4\omega_{{\rm CR},box}(\alpha)\over\kappa_{{\rm CR},box}}
   \le
   \delta_{box}s_0^2
   ```

   holds eventually.

Then `CR-LMOD_box(delta_box,kappa_CR,box)` holds.

Proof.

By Lemma 3.4C.2, the generic `CR-MTD` ledger gives
`CR-POS(D_CR,box,kappa_CR,box)`. By Lemma 3.4D.2, the generic `CR-LMOD`
ledger gives `CR-LCONT(D_CR,box,kappa_CR,box)`. With positive
counterterms, Theorem 3.4E gives both the finite-stage lower bound
`W_{rho,alpha}(L)>=2 kappa_CR,box` and the continuum domain
`CR-DOM(D_CR,box,kappa_CR,box)`. In particular, the finite-stage lower
bound required by Corollary 3.4J.2 holds. Corollary 3.4J.2 then gives
`CR-LMOD_box(delta_box,kappa_CR,box)`. `square`

### Definition 3.4J.4: Quantitative Loop-Modulus Pass `CR-LMOD-QUANT_box`

`CR-LMOD-QUANT_box(delta_box,kappa_CR,box)` holds when the following
finite-window facts are proved on the same whole-process tower:

1. Paper 16 supplies the loop-continuity closure gate `HK-LC-CLOSE`, hence
   an admissible finite-battery loop modulus for every loop slot appearing
   in `D_CR,box`;
2. the Paper-12/Paper-16 normalization and counterterm choices keep the four
   loop expectations in every first-battery Creutz cell positive;
3. the continuum Creutz-slot lower bound holds:

   ```math
   \inf_{L\in{\rm Slot}(D_{{\rm CR},box})}
   \mathcal W_\rho(L)
   \ge
   \kappa_{{\rm CR},box};
   ```

4. the finite-stage lower bound holds eventually:

   ```math
   \inf_{L\in{\rm Slot}(D_{{\rm CR},box})}
   \mathcal W_{\rho,\alpha}(L)
   \ge
   \kappa_{{\rm CR},box};
   ```

5. the transported finite-window loop error satisfies eventually

   ```math
   \omega_{{\rm CR},box}(\alpha)
   \le
   {\delta_{box}\kappa_{{\rm CR},box}s_0^2\over 4}.
   ```

The finite slot set `Slot(D_CR,box)` contains exactly the four Wilson-loop
records for each first-battery Creutz ratio. This is a scalar record-domain
condition; it does not introduce gauge-fixed fields as new observables.

### Theorem 3.4J.5: `CR-LMOD-QUANT_box` Proves `CR-LMOD_box`

If `CR-LMOD-QUANT_box(delta_box,kappa_CR,box)` holds, then
`CR-LMOD_box(delta_box,kappa_CR,box)` holds.

Proof.

Clause 1 of `CR-LMOD-QUANT_box` gives the generic loop-continuity ledger
`CR-LMOD(D_CR,box,kappa_CR,box)` with modulus `omega_CR,box(alpha)`.
Clauses 2--4 give the positivity and lower-bound hypotheses in Lemma
3.4J.1 for every loop slot in the first-battery Creutz window. Clause 5 is
exactly the small-log-modulus inequality:

```math
{4\omega_{{\rm CR},box}(\alpha)\over\kappa_{{\rm CR},box}}
\le
\delta_{box}s_0^2.
```

Corollary 3.4J.2 therefore applies and gives
`CR-LMOD_box(delta_box,kappa_CR,box)`. `square`

### Corollary 3.4J.6: Quantitative First-Battery Paper-15 Pass

Assume the hypotheses of Theorem 3.4I.8, replacing its clause 4 by the
single hypothesis `CR-LMOD-QUANT_box(delta_box,kappa_CR,box)`. Then
`P15-CREUTZ-PASS_box(sigma,delta_box,kappa_CR,box)` holds.

Proof.

Theorem 3.4J.5 converts `CR-LMOD-QUANT_box` into
`CR-LMOD_box(delta_box,kappa_CR,box)`. Theorem 3.4I.8 then applies.
`square`

### Lemma 3.4K: `CR-LMOD_box` Transports Finite-Stage Creutz Margins

Assume `CR-DOM(D_CR,box,kappa_CR,box)` and
`CR-LMOD_box(delta_box,kappa_CR,box)`. If, eventually,

```math
\chi_{\rho,\alpha}(C)
\ge
(\sigma+\delta_{box})s_0^2
```

for every `C in C_box`, then

```math
\chi_\rho(C)\ge\sigma s_0^2
```

for every `C in C_box`.

Proof.

By `CR-LMOD_box`,

```math
|\chi_{\rho,\alpha}(C)-\chi_\rho(C)|
\le
\delta_{box}s_0^2
```

uniformly on the finite set `C_box`. Therefore

```math
\chi_\rho(C)
\ge
\chi_{\rho,\alpha}(C)-\delta_{box}s_0^2
\ge
\sigma s_0^2.
```

`square`

### Theorem 3.4L: `CR-MTD_box + CR-LMOD_box` Proves `CONF-CR_box`

Assume, for some `sigma>0`, `delta_box>0`, and `kappa_CR,box>0`:

1. `CR-MTD_box(sigma,delta_box,kappa_CR,box)`;
2. `CR-LMOD_box(delta_box,kappa_CR,box)`;
3. the counterterm factors in all four Creutz slots of `D_CR,box` are
   positive and use the Paper-12/Paper-16 normalization.

Then `CONF-CR_box(sigma)` holds.

Proof.

The generic part of `CR-MTD_box` gives `CR-MTD(D_CR,box,kappa_CR,box)`.
The generic part of `CR-LMOD_box` gives
`CR-LMOD(D_CR,box,kappa_CR,box)`. With the positive counterterm factors,
Corollary 3.4E.1 gives `CR-DOM(D_CR,box,kappa_CR,box)`.

The main-term and remainder inequalities in `CR-MTD_box` give the
finite-stage lower bound

```math
\chi_{\rho,\alpha}(C)
\ge
(\sigma+\delta_{box})s_0^2
```

for every `C in C_box`. Lemma 3.4K transports this lower bound through the
log-ratio modulus and gives

```math
\chi_\rho(C)\ge\sigma s_0^2
```

on the continuum first-battery window. These are exactly the three clauses
of `CONF-CR_box(sigma)`. `square`

The charged-boundary protocol gate `CH-BDY-PROT` holds for a static
charge-anticharge instrument when the following data are specified at each
finite regulator stage:

1. its representation `rho`;
2. two finite-regulator boundary worldlines, Polyakov lines, or static
   timelike paths `gamma_x` and `gamma_y`;
3. a closure prescription `C_alpha` that turns the pair into either a closed
   Wilson-loop record or a paired Polyakov-loop scalar record;
4. a positive normalization and counterterm factor
   `Z_{rho,alpha}^{bd}` built from the same perimeter, cusp, and boundary
   ledgers as Papers 12 and 16;
5. a scalar record

   ```math
   B_{\rho,\alpha}^{x,y,T}
   =
   (Z_{\rho,\alpha}^{\rm bd})^{-1}
   {\rm Re}\,{1\over d_\rho}
   \chi_\rho(U_{C_\alpha(\gamma_x,\gamma_y)}),
   ```

   or the corresponding paired Polyakov scalar when the time direction is
   periodic;
6. a projective compatibility map showing that restriction to a smaller
   finite record battery produces the same scalar record as first restricting
   the boundary protocol and then scalarizing;
7. a declared limit or rate extraction, such as

   ```math
   V_\rho(R)
   =
   -\lim_{T\to\infty}{1\over T}
   \log W_\infty(B_{\rho}^{x,y,T}),
   ```

   whenever the static-potential record is used.

The charged-boundary gate `CH-BDY` holds for a family of static or charged
instruments if `CH-BDY-PROT` holds for every member of the family and every
scalarized record belongs to the Paper-16 Wilson-loop or marked-loop record
tower.

### Lemma 3.4G: Boundary Protocols Give `CH-BDY`

Assume `CH-BDY-PROT` holds for every charged instrument used in the
confinement proof, and the scalarized records belong to the common
Paper-16/Paper-17 tower. Then `CH-BDY` holds.

Proof.

Each charged instrument is specified at finite regulator, closed or paired
into a scalar record, normalized by the same counterterm ledgers as the
Wilson-loop tower, and transported through a projectively compatible limit.
No open colored line is treated as an observable. Therefore the family is a
typed boundary protocol for generating scalar records, which is exactly
`CH-BDY`. `square`

`CH-BDY` is deliberately not a colored observable gate. It is only a typed
protocol for generating scalar records.

### Proposition 3.5: Imported Reduction For `CONF-REC`

Assume:

1. Paper 16 `CYM_WL`;
2. Paper 12 perimeter/cusp renormalization for rectangular loop records;
3. Paper 17 `MG-WP` for the cofinal mass-gap batteries;
4. `CR-DOM^cof` on the rectangle windows used for Creutz ratios;
5. `CH-BDY` for every static or charged boundary instrument used in the
   confinement proof.

Then `CONF-REC` holds.

Proof.

Paper 16 puts the renormalized closed-loop records in one continuum
whole-process Wilson-loop functional. Paper 12 supplies the perimeter and
cusp counterterms for rectangular records, so the records used in
`CONF-AL` and `CONF-CR` belong to that functional. `CR-DOM^cof` is exactly
the positivity and nonzero-domain condition needed for every logarithm in
the Creutz-ratio records used later. `CH-BDY` converts static charged
instruments into scalar closed-loop or marked-loop records before they enter
any estimate.
Paper 17 `MG-WP` identifies the mass-gap batteries with restrictions of the
same tower. These five clauses are precisely the four clauses of
Definition 3.3. `square`

### Corollary 3.5A: Fully Reduced `CONF-REC` Gate

Assume:

1. Paper 16 `CYM_WL`;
2. Paper 12 perimeter/cusp renormalization for rectangular loop records;
3. Paper 17 `MG-WP` for the cofinal mass-gap batteries;
4. an increasing finite-window family `D_CR,J` covering the Creutz
   rectangles used later, with `CR-MTD(J,kappa_CR,J)`,
   `CR-LMOD(J,kappa_CR,J)`, and positive counterterm factors for every `J`;
5. `CH-BDY-PROT` for every static or charged boundary instrument used in the
   confinement proof, with scalarized records in the common tower.

Then `CONF-REC` holds.

Proof.

Corollary 3.4F.1 gives `CR-DOM^cof`. Lemma 3.4G gives `CH-BDY`.
Proposition 3.5 then gives `CONF-REC`. `square`

This corollary closes the definitional side of steps 1--2. The remaining
mathematical content is not the meaning of the gates, but proving their
finite-window estimates on the actual four-dimensional `SU(N)` continuum
trajectory: `CR-MTD`, `CR-LMOD`, positive counterterm factors, and the
inclusion of all scalarized boundary records in the common tower.

### Definition 3.6: Confinement Whole-Process Ledger `CONF-WP`

`CONF-WP` holds when:

1. the Wilson-loop, Creutz, Polyakov, static-potential, marked-polymer, and
   mass-gap batteries are all restrictions of the same Paper-16
   whole-process law;
2. perimeter, cusp, smearing, regulator, gauge-chart, and projection
   counterterms are the same counterterms used in Papers 12--17;
3. every comparison between two record batteries is made by projective
   restriction or by an explicitly debited extension of the common tower;
4. no proof step composes unrecorded partial transition kernels as though
   the process were Markovian or divisible;
5. all gauge-fixed fields, surfaces, sheets, and flux-tube language are
   auxiliary encodings of scalar record estimates;
6. charged or colored endpoints appear only through declared boundary
   protocols whose scalar consequences are closed-loop or marked-loop
   records;
7. every artifact loss is entered once in the confinement loss ledger and
   once in the Paper-17 mass-gap ledger, with a named comparison map between
   the two entries.

This is the Barandes-aligned audit. The primitive object remains the
whole-process record law; the confinement proof is a way of estimating that
law, not a replacement ontology.

### Definition 3.7: Confinement Completion Certificate `CONF-COMP`

`CONF-COMP(sigma,m_*)` holds if:

1. `CONF-REC` holds;
2. `CONF-WP` holds;
3. `CONF-AL(sigma)` or `CONF-CR(sigma)` holds on the declared continuum
   rectangle class;
4. for every Paper-17 battery `G_j`, the marked bridge gate
   `CONF-MARK_j(sigma)` holds;
5. marked surface-polymer stability `MS-KP_j` holds for every `G_j`;
6. the residual and decorated smallness tests in `G_j-CONF-PASS` hold for
   every `G_j`;
7. the confinement-to-KP rate ledger leaves the cofinal positive reserve
   `CONF-COFINAL-PASS(m_*)`.

Thus `CONF-COMP` is not a single black-box area-law claim. It is a checklist
whose entries can fail independently.

## 4. Marked Surface-Polymer Bridge

### Definition 4.1: Marked Surface-Polymer Stability `MS-KP_j`

For a Paper-17 battery `G_j`, `MS-KP_j` holds if every marked two-point
correlator generated by endpoint records `O,P in G_j` admits a connected
surface-polymer expansion whose activities obey a KP bound with constants

```text
A_j^S, mu_j^S, h_j^S, lambda_mark,j^S.
```

The marked surface polymers must be compatible with the Paper-13/Paper-15
residual polymer gas and with the Paper-17 endpoint marking ledger.

### Definition 4.2: Marked Area-To-Surface Bridge `CONF-MARK_j(sigma)`

For a Paper-17 battery `G_j`, `CONF-MARK_j(sigma)` holds when the declared
area-law or Creutz certificate controls the marked surface polymers entering
`MS-KP_j` in the following quantitative sense.

For each centered endpoint pair `O,P in G_j`, and for each admissible marked
surface hull `S` joining their endpoint collars, there are constants
`B_j(O,P)`, `epsilon_area,j>=0`, and `c_geom,j>0` such that the renormalized
activity satisfies

```math
|z_j(S;O,P)|
\le
B_j(O,P)\exp[-\mu_j^S |S|],
```

with the block-distance decay lower bound

```math
\mu_j^S
\ge
c_{{\rm geom},j}\sigma\ell_j
-\epsilon_{{\rm area},j}.
```

Here `ell_j` is the Paper-17 physical block scale, and `c_geom,j` includes
the minimal transverse surface width and any fixed representation-dependent
normalization. The point of this definition is surgical: it converts an
area-law statement about loop records into a decay statement for the marked
two-point hulls needed by the mass-gap batteries.

### Definition 4.2A: Area-To-Marked-Hull Transfer `AL2MARK_j`

`AL2MARK_j(sigma)` is the concrete transfer package used to prove
`CONF-MARK_j(sigma)`. It consists of the following finite-battery data.

1. **Endpoint closure:** for every endpoint pair `O,P in G_j`, each marked
   hull `S` can be closed by a finite collar protocol into a finite family of
   scalar loop records `L_a(S;O,P)`.
2. **Area comparison:** there are constants `c_geom,j>0` and
   `b_area,j>=0` such that the total renormalized loop area obeys

   ```math
   \sum_a {\rm Area}(L_a(S;O,P))
   \ge
   c_{{\rm geom},j}\ell_j |S|
   -b_{{\rm area},j}.
   ```

3. **Counterterm cancellation:** perimeter and cusp terms from the closure
   protocol are either absorbed into the amplitude `B_j(O,P)` or debited
   through `epsilon_area,j`.
4. **Creutz fallback:** if `CONF-CR(sigma)` rather than `CONF-AL(sigma)` is
   used, the hull is tiled by Creutz cells of physical size `s_0`, and the
   finite-cell boundary remainder is included in `epsilon_area,j`.
5. **Endpoint locality:** the closure collars have diameter bounded in units
   of the support diameter of `O` and `P`; their growth is independent of the
   large separation.
6. **Record compatibility:** every loop created by the closure protocol is a
   record allowed by `CONF-REC` and the same whole-process tower required by
   `CONF-WP`.

The transfer loss is recorded as

```math
\epsilon_{{\rm area},j}
=
\epsilon_{{\rm area0},j}
+\epsilon_{{\rm tile},j}
+\epsilon_{{\rm ctr},j}
+\epsilon_{{\rm collar},j},
```

where `epsilon_area0,j` is the rate loss left after bounded endpoint-area
terms have been moved into the amplitude `B_j(O,P)`.

### Definition 4.2A.1: Marked Closure Geometry `MARK-GEOM_j`

For a Paper-17 battery `G_j`, `MARK-GEOM_j` holds when the following
geometric closure data are available for every endpoint pair `O,P in G_j`.

1. **Closure map.** Each admissible marked hull `S` has a finite closure
   family

   ```math
   {\rm Cl}_j(S;O,P)=\{L_a(S;O,P)\}_{a=1}^{N_j(S;O,P)}
   ```

   of scalar closed-loop records.
2. **Uniform local multiplicity.** There is `N_cl,j<infty` such that every
   plaquette or block face of `S` is covered by at most `N_cl,j` closure
   loops away from the endpoint collars.
3. **Area comparison.** There are constants `c_geom,j>0` and
   `b_area,j>=0` such that

   ```math
   \sum_{a=1}^{N_j(S;O,P)}
   {\rm Area}(L_a(S;O,P))
   \ge
   c_{{\rm geom},j}\ell_j |S|
   -b_{{\rm area},j}.
   ```

4. **Endpoint locality.** The collar loops used to close the endpoints have
   diameter bounded by a constant depending only on the support diameters of
   `O` and `P`, not on the separation between endpoints.
5. **Record compatibility.** Every loop in `Cl_j(S;O,P)` belongs to the
   `CONF-REC` record domain and to the same whole-process tower audited by
   `CONF-WP`.

This is a geometric statement about how to estimate scalar record
correlations. It does not introduce a physical sheet as an additional
object.

### Lemma 4.2A.2: `MARK-GEOM_j` Supplies The Closure And Area Clauses

Assume `MARK-GEOM_j`. Then the endpoint closure, area comparison, endpoint
locality, and record-compatibility clauses of `AL2MARK_j` hold.

Proof.

The closure map is exactly the endpoint closure clause. The displayed
inequality is exactly the area comparison clause. Endpoint locality and
record compatibility are clauses 4 and 5 of `MARK-GEOM_j`. `square`

### Proposition 4.2A.2a: First-Battery Plaquette-Clover Geometry Proves `MARK-GEOM_box`

Use Paper 17's first plaquette-clover battery `G_box`, with block scale
`ell_box=s_0`, finite representation set `Rep_box`, finite orientation set
of plaquette planes, and endpoint records generated by centered plaquette
loops, clover averages, and products of at most two such records.

Assume the standard Paper-13--15 block-face hull convention for this first
battery:

1. a marked hull `S` is a finite connected set of oriented block faces in
   the `s_0` cellulation whose support intersects the fixed endpoint collars
   of `O` and `P`;
2. `|S|` counts the block faces in the admissible hull, while at most a
   finite endpoint-collar number of faces may be omitted from the
   long-distance retained-face count;
3. each retained block face has a scalar plaquette Wilson-loop record in one
   of the representation channels of `Rep_box`;
4. clover endpoint records are treated as their four plaquette components
   before estimating areas, since the clover is only a finite real average
   of closed scalar loop records.

Then `MARK-GEOM_box` holds.

Proof.

The closure map is explicit. For every retained face `f in S`, let
`L_f` be the scalar plaquette loop around the boundary of `f`, in the
representation channel paired with the endpoint record being estimated. Let
`E_box(O,P)` be the finite set of plaquette and clover-component loops in
the one-block endpoint collars needed to match the local endpoint supports
of `O` and `P`. Define

```math
{\rm Cl}_{box}(S;O,P)
=
\{L_f:f\in S\}\cup E_{box}(O,P).
```

This is a finite family of closed scalar loop records. Away from the
endpoint collars each retained block face is used exactly once, so one may
take

```math
N_{{\rm cl},box}=1
```

for the local multiplicity clause. Endpoint collar multiplicities are not
part of the large-distance local multiplicity; they are finite endpoint
data.

Let `alpha_box` be the minimal retained area fraction of a block face under
the chosen plaquette/clover convention. In the unreduced plaquette-face
normalization, `alpha_box=1`. In a convention that subdivides a clover into
finite plaquette components, `alpha_box` is the positive minimum over that
finite subdivision. Let `N_skip,box(O,P)` be the maximum number of block
faces hidden inside the two endpoint collars. Since `G_box` is finite, set

```math
N_{{\rm skip},box}
=
\max_{O,P\in G_{box}} N_{{\rm skip},box}(O,P).
```

Then every retained face contributes at least
`alpha_box s_0^2` of renormalized loop area, so

```math
\sum_{L\in{\rm Cl}_{box}(S;O,P)}
{\rm Area}(L)
\ge
\alpha_{box}s_0^2(|S|-N_{{\rm skip},box}).
```

Equivalently, the `MARK-GEOM_box` area constants may be chosen as

```math
c_{{\rm geom},box}=\alpha_{box}s_0,
```

and

```math
b_{{\rm area},box}=\alpha_{box}s_0^2N_{{\rm skip},box},
```

so that

```math
\sum_{L\in{\rm Cl}_{box}(S;O,P)}
{\rm Area}(L)
\ge
c_{{\rm geom},box}s_0|S|
-b_{{\rm area},box}.
```

Endpoint locality holds because `E_box(O,P)` is contained in the fixed
one-block collars of the finite endpoint supports of `O` and `P`; its
diameter depends only on the endpoint records, not on the separation of the
two insertions. Record compatibility holds because every loop in
`Cl_box(S;O,P)` is a closed scalar Wilson-loop record in `Rep_box`, and
clover records have already been expanded into finite scalar loop
components on the same whole-process tower. Thus all five clauses of
`MARK-GEOM_box` hold. `square`

This proposition is deliberately finite-battery. If a later cofinal hull
convention uses larger loops, nonrectangular cells, or charged boundary
probes, the corresponding `MARK-GEOM_j` must be proved again with its own
closure constants.

### Definition 4.2A.3: Marked Collar And Counterterm Ledger `MARK-LOSS_j`

For a Paper-17 battery `G_j`, `MARK-LOSS_j` holds when the closure protocol
has finite endpoint amplitudes and rate losses with the following form.

For each endpoint pair `O,P in G_j`, there is `B_j(O,P)<infty` such that
all endpoint collars, bounded area defects, local normalization factors, and
finite closure multiplicities contribute at most this amplitude times a
rate-loss exponential. The rate loss is decomposed as

```math
\epsilon_{{\rm area},j}
=
\epsilon_{{\rm area0},j}
+\epsilon_{{\rm tile},j}
+\epsilon_{{\rm ctr},j}
+\epsilon_{{\rm collar},j},
```

where:

| Loss | Meaning | Finite-battery requirement |
| --- | --- | --- |
| `epsilon_area0,j` | residual area defect not absorbed into `B_j(O,P)` | finite |
| `epsilon_tile,j` | Creutz-cell tiling boundary remainder | zero on the direct area-law branch or finite |
| `epsilon_ctr,j` | perimeter, cusp, and counterterm mismatch | finite and compatible with Papers 12--16 |
| `epsilon_collar,j` | endpoint collar and local closure growth | amplitude-only or finite in rate |

The ledger condition is that, after applying the area-law or Creutz estimate
to the closure loops, the non-area factors obey

```math
F_j(S;O,P)
\le
B_j(O,P)
\exp[\epsilon_{{\rm area},j}|S|],
```

where `F_j(S;O,P)` denotes the product of collar, tiling, counterterm,
finite-volume, and closure-comparison factors not already included in the
area cost.

### Lemma 4.2A.4: `MARK-LOSS_j` Controls Endpoint And Counterterm Losses

Assume `MARK-LOSS_j`. Then endpoint collar and counterterm losses are either
absorbed into the finite amplitude `B_j(O,P)` or debited through
`epsilon_area,j`. In particular, these losses cannot be used again in the
Paper-17 rate ledger except through the named artifact terms in
`Delta_conf,j`.

Proof.

The displayed ledger inequality bounds all non-area factors by one finite
amplitude and one rate-loss exponential. The amplitude is independent of the
large endpoint separation and therefore affects only prefactors in
two-point estimates. The rate-loss exponential is precisely the named
`epsilon_area,j` debit. `CONF-WP` prevents the same artifact from being
counted a second time under a different name. `square`

### Proposition 4.2A.4a: First-Battery Loss Ledger Proves `MARK-LOSS_box`

Assume the first-battery block-face hull convention of Proposition 4.2A.2a,
`CONF-WP`, and the Paper-12/Paper-16 same-ledger renormalized loop record
package on the plaquette, clover-component, and endpoint-collar loops
appearing in `Cl_box(S;O,P)`.

Assume also the following finite local loss bounds.

1. **Endpoint collars.** For every `O,P in G_box`, all endpoint collar
   scalarization, clover expansion, centering, and finite product
   normalizations are bounded by a finite constant `C_collar,box(O,P)`.
2. **Bounded area defect.** The bounded endpoint area defect
   `b_area,box` from Proposition 4.2A.2a is absorbed into the amplitude.
3. **Counterterm comparison.** The counterterms used in the marked closure
   loops and in the area-law or Creutz estimate are the same Paper-12
   symmetric-positive scalar counterterms, up to a finite local per-face
   comparison factor. Let

   ```math
   M_{{\rm ctr},box}
   =
   \max\left(1,\max_{t\in{\mathcal T}_{box}} M_{{\rm ctr},box}(t)\right),
   ```

   where `T_box` is the finite set of local plaquette/clover face types and
   each `M_ctr,box(t)` bounds the corresponding counterterm comparison
   factor on the common Paper-16 tower.
4. **Tiling branch.** On the direct area-law branch set
   `M_tile,box=1`. On the Creutz branch, assume each retained block face is
   tiled by a uniformly bounded number of declared Creutz cells and let
   `M_tile,box>=1` be the finite maximal local tiling-remainder factor per
   retained face, again taking the maximum with `1`.

Then `MARK-LOSS_box` holds. One may choose

```math
\epsilon_{{\rm area0},box}=0,
```

```math
\epsilon_{{\rm collar},box}=0,
```

```math
\epsilon_{{\rm ctr},box}=\log M_{{\rm ctr},box},
```

and

```math
\epsilon_{{\rm tile},box}=\log M_{{\rm tile},box}.
```

Thus

```math
\epsilon_{{\rm area},box}
=
\log M_{{\rm ctr},box}
+\log M_{{\rm tile},box}.
```

For each endpoint pair define the finite amplitude

```math
B_{box}(O,P)
=
C_{{\rm collar},box}(O,P)
\exp[\sigma b_{{\rm area},box}].
```

If the Creutz branch uses a finite additive endpoint remainder instead of
the direct `sigma b_area,box` area-defect term, replace the exponential
factor above by the corresponding finite endpoint-remainder exponential.

Proof.

By Proposition 4.2A.2a, the closure protocol uses one retained scalar
plaquette loop per retained block face and finitely many endpoint-collar
loops. The endpoint-collar loops, clover-component expansions, centering
constants, and product normalizations depend only on the finite endpoint
records `O,P in G_box`, so they contribute the finite amplitude
`C_collar,box(O,P)` and no large-distance rate loss.

The bounded endpoint area defect enters the area estimate as a constant
`b_area,box`. Applying an area-law cost with coefficient `sigma` turns this
bounded defect into the finite factor `exp[sigma b_area,box]`, again with
no rate loss in `|S|`. Hence `epsilon_area0,box=0`.

For the counterterm part, `CONF-WP` forces the marked closure loops and the
confinement estimate to use the same Paper-12 counterterm branch on the same
Paper-16 whole-process tower. Any remaining mismatch is therefore a declared
local comparison factor attached to one of finitely many plaquette/clover
face types. Since each retained face appears once away from endpoint
collars,

```math
F_{{\rm ctr},box}(S;O,P)
\le
M_{{\rm ctr},box}^{|S|}.
```

The same argument applies to the Creutz tiling branch. In the direct
area-law branch there is no tiling factor. In the Creutz branch the
uniformly bounded local tiling protocol assigns at most the finite local
factor `M_tile,box` per retained face, so

```math
F_{{\rm tile},box}(S;O,P)
\le
M_{{\rm tile},box}^{|S|}.
```

Multiplying the endpoint amplitude, bounded area-defect amplitude,
counterterm comparison, and tiling comparison gives

```math
F_{box}(S;O,P)
\le
B_{box}(O,P)
\exp[
(\log M_{{\rm ctr},box}+\log M_{{\rm tile},box})|S|
].
```

This is exactly the `MARK-LOSS_box` ledger inequality with the displayed
choices of `epsilon_area0,box`, `epsilon_collar,box`, `epsilon_ctr,box`,
and `epsilon_tile,box`. `square`

In the cleanest first-battery branch, the closure loops are the same
renormalized plaquette records used by the area-law certificate and no
Creutz tiling fallback is invoked. Then `M_ctr,box=M_tile,box=1`, so the
entire first-battery loss ledger is amplitude-only:

```math
\epsilon_{{\rm area},box}=0.
```

The nonzero-loss branch is still useful because it records exactly how much
margin is consumed when the proof uses Creutz tiling, counterterm
transport, or a slightly different scalarization of the endpoint collars.

### Theorem 4.2A.5: Geometry Plus Losses Prove `AL2MARK_j`

Assume `MARK-GEOM_j` and `MARK-LOSS_j`. Then the structural clauses of
`AL2MARK_j(sigma)` hold. If, in addition, either `CONF-AL(sigma)` or
`CONF-CR(sigma)` supplies the scalar loop-record area cost on the closure
loops, then the transfer loss and marked decay exported by `AL2MARK_j` are:

```math
\epsilon_{{\rm area},j}
=
\epsilon_{{\rm area0},j}
+\epsilon_{{\rm tile},j}
+\epsilon_{{\rm ctr},j}
+\epsilon_{{\rm collar},j},
```

and

```math
\mu_j^S
\ge
c_{{\rm geom},j}\sigma\ell_j
-\epsilon_{{\rm area},j}.
```

Proof.

Lemma 4.2A.2 gives the closure, area comparison, endpoint locality, and
record-compatibility clauses. Lemma 4.2A.4 gives the counterterm,
collar, tiling, and bounded-defect loss clauses. Applying `CONF-AL` to the
closed loop family gives the area cost directly. If `CONF-CR` is used, tile
the hull by the declared Creutz cells and debit the finite-cell boundary
remainder through `epsilon_tile,j`. Combining the area comparison with the
loss ledger yields the displayed lower bound for `mu_j^S`. `square`

### Proposition 4.2B: `AL2MARK_j` Proves `CONF-MARK_j`

Assume `CONF-REC`, `CONF-WP`, either `CONF-AL(sigma)` or
`CONF-CR(sigma)`, and `AL2MARK_j(sigma)`. Then `CONF-MARK_j(sigma)` holds.

Proof.

The endpoint closure writes every marked hull contribution as a finite
combination of scalar loop records, with finite endpoint factors. By
`CONF-REC`, those records lie in the declared domain; by `CONF-WP`, the
closure comparison is made inside the same whole-process tower. The
area-law branch applies `CONF-AL(sigma)` to the closed loop family. The
Creutz branch tiles the same hull by Creutz cells and uses
`CONF-CR(sigma)`, debiting the cell boundary remainder. In either branch,
counterterms and collar terms are absorbed into `B_j(O,P)` or into
`epsilon_area,j`. The area comparison then gives

```math
|z_j(S;O,P)|
\le
B_j(O,P)
\exp[-(c_{{\rm geom},j}\sigma\ell_j
-\epsilon_{{\rm area},j})|S|],
```

which is exactly Definition 4.2 with

```math
\mu_j^S
\ge
c_{{\rm geom},j}\sigma\ell_j
-\epsilon_{{\rm area},j}.
```

`square`

### Corollary 4.2C: First-Battery Marked Bridge

Assume:

1. `CONF-REC` and `CONF-WP`;
2. either `CONF-AL(sigma)` or `CONF-CR(sigma)` on the first-battery
   rectangle class;
3. `MARK-GEOM_box`;
4. `MARK-LOSS_box`.

Then `AL2MARK_box(sigma)` holds and therefore `CONF-MARK_box(sigma)` holds.
Under the standard first-battery block-face hull convention, assumption 3 is
discharged by Proposition 4.2A.2a. Under the same-ledger finite local loss
bounds of Proposition 4.2A.4a, assumption 4 is discharged as well.
The exported first-battery constants are those listed in Definition 4.3A:

| Constant | Role |
| --- | --- |
| `c_geom,box` | first-battery area-to-hull conversion |
| `b_area,box` | bounded closure-area defect |
| `epsilon_area0,box` | residual area defect not absorbed into amplitude |
| `epsilon_tile,box` | Creutz tiling boundary loss |
| `epsilon_ctr,box` | perimeter, cusp, and counterterm mismatch |
| `epsilon_collar,box` | endpoint collar and closure growth loss |

with

```math
\epsilon_{{\rm area},box}
=
\epsilon_{{\rm area0},box}
+\epsilon_{{\rm tile},box}
+\epsilon_{{\rm ctr},box}
+\epsilon_{{\rm collar},box},
```

and

```math
\mu_{\rm box}^S
\ge
c_{{\rm geom},box}\sigma s_0
-\epsilon_{{\rm area},box}.
```

Proof.

Theorem 4.2A.5 gives `AL2MARK_box(sigma)` after setting `G_j=G_box` and
`ell_box=s_0`. Proposition 4.2B then gives `CONF-MARK_box(sigma)`. `square`

### Corollary 4.2D: First-Battery Input To `BOX-CONF-PASS`

Assume the hypotheses of Corollary 4.2C and `MS-KP_box`. If the finite
visible margin

```math
c_{{\rm geom},box}\sigma s_0
-\epsilon_{{\rm area},box}
-h_{\rm box}^S
-\lambda_{{\rm mark},box}^S
>0
```

holds and the residual/decorated smallness tests in Definition 4.3B hold for
some `m_box`, then `BOX-CONF-PASS` holds.

Proof.

Corollary 4.2C supplies `AL2MARK_box` and `CONF-MARK_box`. The assumption
`MS-KP_box` supplies the marked surface stability data. The displayed
positive margin and the residual/decorated tests are the remaining clauses
of Definition 4.3B. `square`

### Definition 4.3: Confinement-To-KP Rate Ledger

For each `j`, define the raw confinement-to-KP rate

```math
m_j^{\rm conf}
=
\mu_j^S
-h_j^S
-\lambda_{{\rm mark},j}^S,
```

where `h_j^S` is the surface-polymer entropy loss and
`lambda_mark,j^S` is the endpoint-marking loss. Under `CONF-MARK_j(sigma)`,
the visible lower bound is

```math
m_j^{\rm conf}
\ge
c_{{\rm geom},j}\sigma\ell_j
-\epsilon_{{\rm area},j}
-h_j^S
-\lambda_{{\rm mark},j}^S.
```

The debited rate is

```math
m_{{\rm conf,phys},j}
=
{m_j^{\rm conf}\over \ell_j}
-\Delta_{{\rm conf},j},
```

with

```math
\Delta_{{\rm conf},j}
=
\Delta_{{\rm cut},j}
+\Delta_{{\rm vol},j}
+\Delta_{{\rm smear},j}
+\Delta_{{\rm block},j}
+\Delta_{{\rm bat},j}
+\Delta_{{\rm reg},j}
+\Delta_{{\rm proj},j}.
```

The terms have the following confinement-specific meanings.

| Loss | Meaning | Required behavior for completion |
| --- | --- | --- |
| `epsilon_area,j/ell_j` | area-law or Creutz-to-surface bridge loss | bounded below the string-tension reserve |
| `Delta_cut,j` | cutoff-removal loss | tends to zero or is uniformly reserved |
| `Delta_vol,j` | finite-volume exhaustion loss | uniform on the local loop batteries |
| `Delta_smear,j` | smearing and unsmearing loss | controlled by Paper-12/Paper-16 loop continuity |
| `Delta_block,j` | block-to-physical conversion and collar loss | amplitude-only or rate-bounded |
| `Delta_bat,j` | battery enlargement loss | controlled along the cofinal `G_j` sequence |
| `Delta_reg,j` | regulator, chart, or counterterm comparison loss | compatible with `CONF-WP` |
| `Delta_proj,j` | finite-record projective restriction loss | vanishes or is summably bounded on the common tower |

The `CONF-MARK_j` constants ledger must publish the following constants
before the confinement bridge can be used by Paper 17.

| Constant | Source | Meaning | Required bound |
| --- | --- | --- | --- |
| `sigma` | `CONF-AL` or `CONF-CR` | string-tension or Creutz area coefficient | positive on the declared continuum class |
| `kappa_CR,J` | `CR-DOM^cof` | finite-window lower bound keeping Creutz logs inside their domain | positive for each finite window |
| `s_0` | Creutz tiling branch | physical cell size for area extraction | fixed before large-rectangle limits |
| `c_geom,j` | `AL2MARK_j` | conversion from area cost to marked hull separation | strictly positive |
| `b_area,j` | `AL2MARK_j` | bounded area defect from endpoint closure | amplitude-only or rate-debited |
| `epsilon_area0,j` | `AL2MARK_j` | residual rate loss after bounded area defects are moved to amplitude | uniformly controlled |
| `epsilon_tile,j` | Creutz fallback | tiling boundary remainder | uniformly controlled |
| `epsilon_ctr,j` | Papers 12--16 | perimeter, cusp, and counterterm mismatch | compatible with `CONF-WP` |
| `epsilon_collar,j` | endpoint protocol | collar and local endpoint closure loss | amplitude-only or rate-bounded |
| `epsilon_area,j` | bridge sum | total area-to-marked-hull loss | smaller than the raw area reserve |
| `mu_j^S` | `CONF-MARK_j` | marked surface activity decay | at least `c_geom,j sigma ell_j - epsilon_area,j` |
| `h_j^S` | `MS-KP_j` | surface-polymer entropy | below the decay margin |
| `lambda_mark,j^S` | endpoint marking | insertion and generator enlargement loss | below the decay margin |
| `ell_j` | Paper 17 | physical block scale | controlled along the cofinal sequence |
| `Delta_conf,j` | loss ledger | transport loss to physical rate | below the debited margin |
| `B_j(O,P)` | endpoint closure | finite pair amplitude | finite for every pair in `G_j` |

The finite-battery pass inequality is

```math
c_{{\rm geom},j}\sigma\ell_j
-\epsilon_{{\rm area},j}
-h_j^S
-\lambda_{{\rm mark},j}^S
>0.
```

The cofinal pass inequality is

```math
\inf_j
\left[
{c_{{\rm geom},j}\sigma\ell_j
-\epsilon_{{\rm area},j}
-h_j^S
-\lambda_{{\rm mark},j}^S
\over \ell_j}
-\Delta_{{\rm conf},j}
\right]
>0.
```

This ledger is the main work surface for the rest of Paper 18: every future
confinement argument must fill this table, not merely assert a qualitative
area law.

The confinement uniform reserve `CONF-UNIF(m_*)` holds when

```math
\inf_j m_{{\rm conf,phys},j}\ge m_*>0.
```

Equivalently, every cofinal battery must satisfy the visible inequality

```math
{\mu_j^S-h_j^S-\lambda_{{\rm mark},j}^S\over \ell_j}
\ge
m_*+\Delta_{{\rm conf},j}.
```

A simple sufficient test is:

```math
\inf_j
\left[
{c_{{\rm geom},j}\sigma\ell_j
-\epsilon_{{\rm area},j}
-h_j^S
-\lambda_{{\rm mark},j}^S
\over \ell_j}
-\Delta_{{\rm conf},j}
\right]
>0.
```

### Definition 4.3A: First-Battery `AL2MARK_box` Constants

Specialize the marked bridge to Paper 17's first plaquette-clover battery
`G_box`. The physical block scale is

```math
\ell_{\rm box}=s_0.
```

`AL2MARK_box(sigma)` is `AL2MARK_j(sigma)` with `G_j=G_box`; it must publish
the following finite constants.

| Constant | Meaning | Finite-battery requirement |
| --- | --- | --- |
| `alpha_box` | minimal retained area fraction per block face in the plaquette/clover convention | strictly positive |
| `N_cl,box` | first-battery local closure multiplicity away from endpoint collars | equal to `1` in the block-face convention |
| `N_skip,box` | maximum number of endpoint-collar faces not counted in the retained hull size | finite because `G_box` is finite |
| `C_collar,box(O,P)` | finite endpoint collar, clover expansion, centering, and product normalization factor | finite for all endpoint pairs |
| `M_ctr,box` | maximal local counterterm comparison factor per retained block face | finite; equal to `1` on the same-counterterm branch |
| `M_tile,box` | maximal local tiling-remainder factor per retained block face | `1` on the direct area-law branch; finite on the Creutz branch |
| `c_geom,box` | minimal area-to-hull conversion for the plaquette-clover endpoint collars | `c_geom,box>0` |
| `b_area,box` | bounded endpoint area defect from closing marked hulls | absorbed into `B_box(O,P)` or debited |
| `epsilon_area0,box` | residual rate loss from endpoint area defects | finite |
| `epsilon_tile,box` | Creutz-cell tiling remainder, zero on the direct area-law branch | finite |
| `epsilon_ctr,box` | perimeter, cusp, and counterterm mismatch | finite and compatible with `CONF-WP` |
| `epsilon_collar,box` | local endpoint collar loss | amplitude-only or finite in rate |
| `epsilon_area,box` | total bridge loss | the sum below |
| `A_box^S` | Paper-15 marked activity prefactor after endpoint enlargement | finite |
| `C_cum,box^S` | Paper-15 connected-cumulant combinatorial constant on marked hulls | finite |
| `h_box^S` | marked surface-polymer entropy loss | finite and below the decay margin |
| `r_box^S` | marked residual-polymer range or collar radius | finite |
| `eta_ch,box` | Paper-15 character-tail/decorated-record bound on the enlarged battery | strictly less than `1` |
| `lambda_mark,box^S` | endpoint-marking generator loss | zero on the generator-normalized branch or finite |
| `R_clean,box` | clean first-battery reserve `alpha_box sigma s_0^2-h_box^S-lambda_mark,box^S` | must beat `D_KP,box` |
| `R_Creutz,box` | Creutz-fallback reserve `alpha_box sigma s_0^2-log M_ctr,box-log M_tile,box-h_box^S-lambda_mark,box^S` | must beat `D_KP,box` |
| `D_KP,box` | residual/decorated KP threshold from Theorems 4.3B.1--4.3B.2 | finite when `eta_ch,box<1` |
| `c_box^S(O,P)` | endpoint collar constant exported to Paper 17 | finite for all pairs |
| `B_box(O,P)` | finite endpoint amplitude for `O,P in G_box` | finite for all pairs |

The bridge loss is

```math
\epsilon_{{\rm area},box}
=
\epsilon_{{\rm area0},box}
+\epsilon_{{\rm tile},box}
+\epsilon_{{\rm ctr},box}
+\epsilon_{{\rm collar},box}.
```

The first-battery marked decay exported by `AL2MARK_box` is

```math
\mu_{\rm box}^S
\ge
c_{{\rm geom},box}\sigma s_0
-\epsilon_{{\rm area},box}.
```

These constants are finite-battery data. They do not require cofinal
uniformity.

### Definition 4.3A.1: First-Battery Pass/Fail Worksheet

For the first battery, define the residual/decorated KP threshold

```math
D_{{\rm box}}^{{\rm KP}}
=
\log
{C_{{\rm cum},box}^S A_{\rm box}^S+1-\eta_{{\rm ch},box}
\over
1-\eta_{{\rm ch},box}},
```

whenever `eta_ch,box<1`. The two first-battery branch reserves are:

```math
R_{{\rm box}}^{{\rm clean}}
=
\alpha_{box}\sigma s_0^2
-h_{\rm box}^S
-\lambda_{{\rm mark},box}^S,
```

and

```math
R_{{\rm box}}^{{\rm Creutz}}
=
\alpha_{box}\sigma s_0^2
-\log M_{{\rm ctr},box}
-\log M_{{\rm tile},box}
-h_{\rm box}^S
-\lambda_{{\rm mark},box}^S.
```

The first-battery worksheet is:

| Quantity | Clean branch | Creutz branch |
| --- | --- | --- |
| confinement input | direct `CONF-AL(sigma)` | `CONF-CR(sigma)` |
| geometry input | `MARK-GEOM_box` from Proposition 4.2A.2a | same |
| loss input | `M_ctr,box=M_tile,box=1` | finite `M_ctr,box,M_tile,box>=1` |
| bridge loss | `epsilon_area,box=0` | `epsilon_area,box=log M_ctr,box+log M_tile,box` |
| reserve | `R_box^clean` | `R_box^Creutz` |
| pass test | `R_box^clean>D_box^KP` | `R_box^Creutz>D_box^KP` |

Let `A_box^{branch}` be the set of available branches: it contains `clean`
only when the direct area-law branch hypotheses of Theorem 4.3B.1 hold, and
it contains `Creutz` only when the Creutz-fallback hypotheses of Theorem
4.3B.2 hold. Define

```math
R_{{\rm box}}^{{\rm best}}
=
\max_{\beta\in A_{{\rm box}}^{{\rm branch}}}
R_{{\rm box}}^\beta,
```

when the available branch set is nonempty. The first-battery pass/fail test
is:

```math
R_{{\rm box}}^{{\rm best}}
>
D_{{\rm box}}^{{\rm KP}}.
```

This is only a worksheet over available record-law certificates. It does not
allow a proof to take the numerical maximum over a branch whose confinement
input has not been proved on the same whole-process tower.

### Definition 4.3A.2: First-Battery Paper-14/15 Import Package `BOX-MSKP-IMPORT`

`BOX-MSKP-IMPORT` is the finite import package used to prove `MS-KP_box`.
It consists of the following data, all computed for the same pushed-forward
block record law and the same whole-process tower as the confinement
records.

1. Paper 14 proves `FBE(s_0,rho,L_box)` and exports the finite-block package
   `X_14,box`.
2. Paper 15 has a positive numerical certificate
   `nCPSC(s_0,rho,L_box)` after enlarging the finite generator battery to
   include:
   - all endpoint records in `G_box`;
   - the scalar plaquette and clover-component records used in
     `MARK-GEOM_box`;
   - the endpoint-collar records used in `MARK-LOSS_box`.
3. The Paper-15 connected-polymer constants are valid on marked hulls with
   two endpoint insertions from `G_box`, not only on the unmarked Creutz
   battery.
4. The Paper-17 endpoint-marking ledger is finite: for every
   `O,P in G_box`, the endpoint collar constant `c_box^S(O,P)`, the
   amplitude `B_box(O,P)`, and the marking loss `lambda_mark,box^S` are
   finite.
5. The character-tail/decorated-record bound imported from Paper 15 obeys
   `eta_ch,box<1`.

The imported constants are identified as follows.

| Paper-18 constant | Imported source | Meaning |
| --- | --- | --- |
| `A_box^S` | Paper-15 `A_AF` after endpoint enlargement | marked surface-polymer activity prefactor |
| `C_cum,box^S` | Paper-15 `C_cum` after endpoint enlargement | connected-cumulant combinatorial constant |
| `h_box^S` | Paper-15 surface entropy constant on the marked battery | lattice-animal or marked-hull entropy loss |
| `r_box^S` | Paper-15 `r_*` on the marked battery | finite residual range or collar radius |
| `eta_ch,box` | Paper-15 `eta_ch^{bd}` on the marked battery | character-tail/decorated-record bound |
| `lambda_mark,box^S` | Paper-17 endpoint-marking ledger | exponential loss from inserting endpoint records |
| `c_box^S(O,P)` | Paper-17 endpoint-collar ledger | finite block-distance collar correction |
| `B_box(O,P)` | Paper-17 endpoint amplitude ledger | finite pair amplitude |

This package is an import of record-law estimates, not an import of
additional ontology. The marked polymers are bookkeeping for connected
cumulants of declared records.

### Theorem 4.3A.3: `BOX-MSKP-IMPORT` Proves `MS-KP_box`

Assume `BOX-MSKP-IMPORT`. Then `MS-KP_box` holds with constants

```text
A_box^S, C_cum,box^S, h_box^S, r_box^S,
eta_ch,box, lambda_mark,box^S, c_box^S(O,P), B_box(O,P).
```

Proof.

Paper 14's `FBE(s_0,rho,L_box)` supplies the finite block entry package:
the block cumulant expansion, the connected expansion, and the
whole-process compatibility ledger for the exact pushed-forward block
record law. Paper 15's positive `nCPSC` supplies the connected-polymer KP
control on the same record law: a finite activity prefactor, connected
cumulant constant, surface-entropy loss, residual range, and character-tail
bound.

The endpoint enlargement clause ensures that these Paper-15 estimates apply
to the marked hulls generated by the first plaquette-clover records
`O,P in G_box`. Thus the estimates control the actual marked two-point
cumulants used by the first-battery confinement bridge, not merely an
unmarked Creutz sub-battery.

The Paper-17 endpoint-marking ledger records the only additional cost of
marking the two endpoints. Endpoint collars and scalarization constants
enter the finite amplitudes `B_box(O,P)` and the finite collar constants
`c_box^S(O,P)`. If endpoint marking creates exponential generator growth,
that growth is debited once through `lambda_mark,box^S`; on the
generator-normalized branch this loss is zero.

Combining these imports gives a connected surface-polymer expansion for
every marked two-point correlator generated by endpoints in `G_box`, with
KP constants exactly as required by Definition 4.1. Therefore `MS-KP_box`
holds. `square`

### Corollary 4.3A.4: Imported First-Battery KP Threshold

Assume `BOX-MSKP-IMPORT`. Then the first-battery residual/decorated KP
threshold in Definition 4.3A.1 is a finite imported constant:

```math
D_{{\rm box}}^{{\rm KP}}
=
\log
{C_{{\rm cum},box}^S A_{\rm box}^S+1-\eta_{{\rm ch},box}
\over
1-\eta_{{\rm ch},box}}.
```

Proof.

Theorem 4.3A.3 supplies `A_box^S`, `C_cum,box^S`, and `eta_ch,box`. The
definition of `BOX-MSKP-IMPORT` includes `eta_ch,box<1`, so the displayed
logarithm is finite. `square`

### Definition 4.3A.5: Compact First-Battery Constants Ledger

The first-battery pass calculation is controlled by the following compact
ledger. All entries are finite-battery quantities computed on the same
whole-process tower.

| Constant | Source | Formula or constraint | Used for |
| --- | --- | --- | --- |
| `alpha_box` | `MARK-GEOM_box` | `alpha_box>0` | retained face area fraction |
| `s_0` | Paper-17 block scale | fixed physical block size | converts area to block hull cost |
| `sigma` | `CONF-AL` or `CONF-CR` | `sigma>0` | scalar loop area coefficient |
| `M_ctr,box` | `MARK-LOSS_box` | `M_ctr,box>=1` | counterterm comparison debit |
| `M_tile,box` | `MARK-LOSS_box` | `M_tile,box>=1` | Creutz tiling debit |
| `A_box^S` | `BOX-MSKP-IMPORT` | finite | marked activity prefactor |
| `C_cum,box^S` | `BOX-MSKP-IMPORT` | finite | connected-cumulant combinatorics |
| `eta_ch,box` | `BOX-MSKP-IMPORT` | `0<=eta_ch,box<1` | decorated/character-tail debit |
| `h_box^S` | `BOX-MSKP-IMPORT` | finite | marked surface entropy loss |
| `lambda_mark,box^S` | `BOX-MSKP-IMPORT` | finite, possibly `0` | endpoint-marking loss |
| `D_KP,box` | Corollary 4.3A.4 | `log((C_cum,box^S A_box^S+1-eta_ch,box)/(1-eta_ch,box))` | KP threshold |
| `R_clean,box` | clean branch | `alpha_box sigma s_0^2-h_box^S-lambda_mark,box^S` | direct area-law reserve |
| `R_Creutz,box` | Creutz branch | `alpha_box sigma s_0^2-log M_ctr,box-log M_tile,box-h_box^S-lambda_mark,box^S` | Creutz fallback reserve |

The ledger is deliberately algebraic. It does not assert a positive
confinement estimate; it says exactly which numerical reserve must be
positive once the corresponding branch has been proved on the record law.

### Definition 4.3A.6: Branch Reserve Certificate `BOX-RESERVE-PASS(beta)`

Let `beta` be either `clean` or `Creutz`.

`BOX-RESERVE-PASS(clean)` holds when:

1. `BOX-MSKP-IMPORT` holds;
2. `CONF-REC` and `CONF-WP` hold;
3. direct first-battery `CONF-AL(sigma)` holds on the closure-loop class;
4. `MARK-GEOM_box` holds;
5. `MARK-LOSS_box` holds with the clean same-counterterm choices
   `M_ctr,box=1` and `M_tile,box=1`, so that the first-battery constants
   satisfy `c_geom,box=alpha_box s_0` and `epsilon_area,box=0`;
6. the clean reserve beats the imported KP threshold:

   ```math
   R_{{\rm box}}^{{\rm clean}}
   >
   D_{{\rm box}}^{{\rm KP}}.
   ```

`BOX-RESERVE-PASS(Creutz)` holds when:

1. `BOX-MSKP-IMPORT` holds;
2. `CONF-REC` and `CONF-WP` hold;
3. first-battery `CONF-CR_box(sigma)` holds on the declared Creutz-cell
   class, equivalently the `CONF-CR(sigma)` hypothesis is available on the
   first-battery class used by Theorem 4.3B.2;
4. `MARK-GEOM_box` holds;
5. `MARK-LOSS_box` holds with finite local loss factors
   `M_ctr,box>=1` and `M_tile,box>=1`, so that the first-battery constants
   satisfy `c_geom,box=alpha_box s_0` and
   `epsilon_area,box=log M_ctr,box+log M_tile,box`;
6. the Creutz reserve beats the imported KP threshold:

   ```math
   R_{{\rm box}}^{{\rm Creutz}}
   >
   D_{{\rm box}}^{{\rm KP}}.
   ```

In either branch, an admissible selected Paper-17 rate is any

```math
0<m_{\rm box}<R_{{\rm box}}^\beta-D_{{\rm box}}^{{\rm KP}}.
```

This certificate prevents a proof from mixing the clean reserve, the Creutz
loss ledger, and an imported KP threshold from different towers.

### Definition 4.3A.7: Paper-15 Creutz Route Final Inequality Ledger

The Paper-15 Creutz route for the first battery has two independent reserve
inequalities.

The upstream Creutz extraction inequality is:

```math
\gamma_{15,box}M_{15}^{bd}
-\epsilon_{15\to box}
\ge
(\sigma+2\delta_{box})s_0^2.
```

Equivalently,

```math
S_{15,box}\ge(\sigma+2\delta_{box})s_0^2.
```

This is the inequality needed by `P15-CREUTZ-PASS_box` to export
`CONF-CR_box(sigma)`.

The downstream marked-KP reserve inequality is:

```math
\alpha_{box}\sigma s_0^2
-\log M_{{\rm ctr},box}
-\log M_{{\rm tile},box}
-h_{\rm box}^S
-\lambda_{{\rm mark},box}^S
>
D_{{\rm box}}^{{\rm KP}}.
```

Equivalently,

```math
R_{{\rm box}}^{{\rm Creutz}}
>
D_{{\rm box}}^{{\rm KP}}.
```

This is the inequality needed by `BOX-RESERVE-PASS(Creutz)` to export
`BOX-CONF-PASS`. The strictness is required at the downstream stage because
Paper 17 needs a nonempty interval of rates `m_box`.

The two inequalities must be proved on the same whole-process tower. The
first one produces the effective `sigma`; the second checks that this
`sigma` still has enough reserve after marked-surface entropy, endpoint
marking, and local Creutz/counterterm losses.

### Definition 4.3A.8: Single-Window Creutz Closing Inequality

For the Paper-15 Creutz route define the downstream loss

```math
L_{{\rm Creutz},box}
=
\log M_{{\rm ctr},box}
+\log M_{{\rm tile},box}
+h_{\rm box}^S
+\lambda_{{\rm mark},box}^S.
```

For a chosen upstream error margin `delta_box`, the first-battery Creutz
window has a strict combined reserve when

```math
\alpha_{box}
\left(
S_{15,box}-2\delta_{box}s_0^2
\right)
>
L_{{\rm Creutz},box}
+D_{{\rm box}}^{{\rm KP}}.
```

Equivalently, the interval

```math
{L_{{\rm Creutz},box}+D_{{\rm box}}^{{\rm KP}}
\over
\alpha_{box}s_0^2}
<
\sigma
\le
{S_{15,box}\over s_0^2}
-2\delta_{box}
```

is nonempty. Any `sigma` in this interval simultaneously satisfies the
upstream Paper-15 Creutz extraction inequality and the downstream marked-KP
reserve inequality.

The inequality is intentionally strict. A zero-width interval gives no
admissible Paper-17 rate `m_box`.

### Theorem 4.3A.9: Combined Creutz Closing Inequality Gives Both Reserves

Assume:

1. `P15-CR-RES_box` exports `S_15,box`;
2. `BOX-MSKP-IMPORT` exports `D_KP,box`;
3. `MARK-GEOM_box` exports `alpha_box>0`;
4. `MARK-LOSS_box` exports finite `M_ctr,box>=1` and `M_tile,box>=1`;
5. the single-window Creutz closing inequality of Definition 4.3A.8 holds
   for some `delta_box>0`.

Then there exists `sigma>0` such that both reserve checks in
Definition 4.3A.7 hold:

```math
S_{15,box}\ge(\sigma+2\delta_{box})s_0^2
```

and

```math
R_{{\rm box}}^{{\rm Creutz}}
>
D_{{\rm box}}^{{\rm KP}}.
```

Proof.

By Definition 4.3A.8 the displayed interval for `sigma` is nonempty. Choose
any `sigma` in it. The upper bound on `sigma` gives

```math
(\sigma+2\delta_{box})s_0^2
\le
S_{15,box},
```

which is the upstream reserve.

The strict lower bound on `sigma` gives

```math
\alpha_{box}\sigma s_0^2
>
L_{{\rm Creutz},box}
+D_{{\rm box}}^{{\rm KP}}.
```

Substituting the definition of `L_Creutz,box` and moving the loss terms to
the left gives

```math
R_{{\rm box}}^{{\rm Creutz}}
>
D_{{\rm box}}^{{\rm KP}}.
```

Thus the same `sigma` passes both stages. `square`

### Definition 4.3B: First-Battery Confinement Pass Gate `BOX-CONF-PASS`

`BOX-CONF-PASS` holds when:

1. `CONF-REC` and `CONF-WP` hold;
2. either `CONF-AL(sigma)` or `CONF-CR(sigma)` holds on the rectangle class
   needed by the first battery;
3. `AL2MARK_box(sigma)` holds;
4. the first-battery marked surface stability gate `MS-KP_box` holds,
   including the Paper-14 `FBE` import, the Paper-15 positive `nCPSC`
   import after endpoint enlargement to `G_box`, marked connected-cumulant
   constants `A_box^S`, `C_cum,box^S`, `h_box^S`, `r_box^S`, and a
   character-tail bound `eta_ch,box`, plus endpoint collar constants
   `c_box^S(O,P)` and amplitudes `B_box(O,P)`. Equivalently, this clause is
   discharged by Theorem 4.3A.3 from `BOX-MSKP-IMPORT`;
5. the finite-battery raw margin is positive:

   ```math
   m_{\rm box}^{\rm conf}
   =
   c_{{\rm geom},box}\sigma s_0
   -\epsilon_{{\rm area},box}
   -h_{\rm box}^S
   -\lambda_{{\rm mark},box}^S
   >0;
   ```

6. the Paper-17 residual and decoration smallness tests hold for some
   choice of `m_box` with `0<m_box<m_box^{conf}`:

   ```math
   \delta_{\rm box}^{\rm conf}
   =
   \mu_{\rm box}^S
   -m_{\rm box}
   -h_{\rm box}^S
   -\lambda_{{\rm mark},box}^S
   >0,
   ```

   ```math
   C_{{\rm cum},box}^S A_{\rm box}^S
   {e^{-\delta_{\rm box}^{\rm conf}}
   \over
   1-e^{-\delta_{\rm box}^{\rm conf}}}
   <1,
   ```

   and

   ```math
   C_{{\rm cum},box}^S A_{\rm box}^S
   {e^{-\delta_{\rm box}^{\rm conf}}
   \over
   1-e^{-\delta_{\rm box}^{\rm conf}}}
   +\eta_{{\rm ch},box}
   <1.
   ```

The visible sufficient inequality in clause 5 is the promised finite-battery
confinement pass condition:

```math
c_{{\rm geom},box}\sigma s_0
-\epsilon_{{\rm area},box}
-h_{\rm box}^S
-\lambda_{{\rm mark},box}^S
>0.
```

It is the box-level version of the cofinal reserve test, without the
cofinal infimum.

### Theorem 4.3B.1: Clean-Branch `BOX-CONF-PASS`

Assume:

1. `CONF-REC` and `CONF-WP`;
2. direct first-battery `CONF-AL(sigma)` on the closure-loop class used by
   the standard block-face hull convention;
3. the first-battery block-face hull convention of Proposition 4.2A.2a;
4. the same-ledger local loss bounds of Proposition 4.2A.4a with
   `M_ctr,box=1` and `M_tile,box=1`;
5. `BOX-MSKP-IMPORT`.

Define the clean first-battery reserve

```math
R_{{\rm box}}^{{\rm clean}}
=
\alpha_{box}\sigma s_0^2
-h_{\rm box}^S
-\lambda_{{\rm mark},box}^S.
```

If `eta_ch,box<1`, define the residual/decorated KP threshold

```math
D_{{\rm box}}^{{\rm KP}}
=
\log
{C_{{\rm cum},box}^S A_{\rm box}^S+1-\eta_{{\rm ch},box}
\over
1-\eta_{{\rm ch},box}}.
```

If

```math
R_{{\rm box}}^{{\rm clean}}
>
D_{{\rm box}}^{{\rm KP}},
```

then `BOX-CONF-PASS` holds for every choice of `m_box` satisfying

```math
0<m_{\rm box}<R_{{\rm box}}^{{\rm clean}}-D_{{\rm box}}^{{\rm KP}}.
```

Proof.

Theorem 4.3A.3 gives `MS-KP_box`, and Corollary 4.3A.4 gives the finite
threshold `D_KP,box`.

Proposition 4.2A.2a gives `MARK-GEOM_box`. Proposition 4.2A.4a, with
`M_ctr,box=M_tile,box=1`, gives `MARK-LOSS_box` and

```math
\epsilon_{{\rm area},box}=0.
```

Corollary 4.2C therefore gives `AL2MARK_box(sigma)` and
`CONF-MARK_box(sigma)`. With
`c_geom,box=alpha_box s_0`, the marked decay lower bound is

```math
\mu_{\rm box}^S
\ge
\alpha_{box}\sigma s_0^2.
```

Hence, for any displayed choice of `m_box`,

```math
\delta_{\rm box}^{\rm conf}
=
\mu_{\rm box}^S
-m_{\rm box}
-h_{\rm box}^S
-\lambda_{{\rm mark},box}^S
>
D_{{\rm box}}^{{\rm KP}}.
```

Let `q=exp[-delta_box^conf]`. The inequality
`delta_box^conf>D_box^KP` is equivalent to

```math
q
<
{1-\eta_{{\rm ch},box}
\over
C_{{\rm cum},box}^S A_{\rm box}^S+1-\eta_{{\rm ch},box}}.
```

Therefore

```math
C_{{\rm cum},box}^S A_{\rm box}^S
{q\over 1-q}
+\eta_{{\rm ch},box}
<1.
```

This is the combined decoration smallness test in Definition 4.3B, and it
also implies the residual smallness test without `eta_ch,box`. The clean
reserve inequality gives the positive raw margin. Thus every clause of
`BOX-CONF-PASS` is satisfied. `square`

This theorem is the first fully explicit finite-battery confinement pass in
Paper 18. Its hard inputs are not hidden: the direct area-law coefficient
`sigma`, the finite Paper-14/Paper-15 marked KP constants, and the condition
that the first-battery closure uses the same Paper-12 counterterm branch with
no Creutz tiling loss.

### Theorem 4.3B.2: Creutz-Fallback `BOX-CONF-PASS`

Assume:

1. `CONF-REC` and `CONF-WP`;
2. first-battery `CONF-CR_box(sigma)`, hence `CONF-CR(sigma)` on the
   declared Creutz-cell class used by the standard block-face hull
   convention;
3. the first-battery block-face hull convention of Proposition 4.2A.2a;
4. the same-ledger local loss bounds of Proposition 4.2A.4a, with finite
   `M_ctr,box>=1` and `M_tile,box>=1`;
5. `BOX-MSKP-IMPORT`.

Define the Creutz-fallback first-battery reserve

```math
R_{{\rm box}}^{{\rm Creutz}}
=
\alpha_{box}\sigma s_0^2
-\log M_{{\rm ctr},box}
-\log M_{{\rm tile},box}
-h_{\rm box}^S
-\lambda_{{\rm mark},box}^S.
```

If `eta_ch,box<1`, let `D_box^KP` be the threshold from Theorem 4.3B.1:

```math
D_{{\rm box}}^{{\rm KP}}
=
\log
{C_{{\rm cum},box}^S A_{\rm box}^S+1-\eta_{{\rm ch},box}
\over
1-\eta_{{\rm ch},box}}.
```

If

```math
R_{{\rm box}}^{{\rm Creutz}}
>
D_{{\rm box}}^{{\rm KP}},
```

then `BOX-CONF-PASS` holds for every choice of `m_box` satisfying

```math
0<m_{\rm box}<R_{{\rm box}}^{{\rm Creutz}}-D_{{\rm box}}^{{\rm KP}}.
```

Proof.

Theorem 4.3A.3 gives `MS-KP_box`, and Corollary 4.3A.4 gives the finite
threshold `D_KP,box`.

Proposition 4.2A.2a gives `MARK-GEOM_box`. Proposition 4.2A.4a gives
`MARK-LOSS_box` with

```math
\epsilon_{{\rm area},box}
=
\log M_{{\rm ctr},box}
+\log M_{{\rm tile},box}.
```

Corollary 4.2C, using `CONF-CR(sigma)` rather than `CONF-AL(sigma)`, gives
`AL2MARK_box(sigma)` and `CONF-MARK_box(sigma)`. With
`c_geom,box=alpha_box s_0`, the marked decay lower bound is

```math
\mu_{\rm box}^S
\ge
\alpha_{box}\sigma s_0^2
-\log M_{{\rm ctr},box}
-\log M_{{\rm tile},box}.
```

Hence, for any displayed choice of `m_box`,

```math
\delta_{\rm box}^{\rm conf}
=
\mu_{\rm box}^S
-m_{\rm box}
-h_{\rm box}^S
-\lambda_{{\rm mark},box}^S
>
D_{{\rm box}}^{{\rm KP}}.
```

Let `q=exp[-delta_box^conf]`. Since
`delta_box^conf>D_box^KP`, the definition of `D_box^KP` gives

```math
q
<
{1-\eta_{{\rm ch},box}
\over
C_{{\rm cum},box}^S A_{\rm box}^S+1-\eta_{{\rm ch},box}}.
```

Therefore

```math
C_{{\rm cum},box}^S A_{\rm box}^S
{e^{-\delta_{\rm box}^{\rm conf}}
\over
1-e^{-\delta_{\rm box}^{\rm conf}}}
+\eta_{{\rm ch},box}
<1,
```

and therefore also the residual smallness test without `eta_ch,box`. The
Creutz reserve inequality gives the positive raw margin in Definition 4.3B.
Thus every clause of `BOX-CONF-PASS` is satisfied. `square`

This theorem is the operational fallback branch. It keeps the ISP ontology
clean: the Creutz cells and marked hulls are only estimate devices for
scalar loop records on the same whole-process law, and every loss appears as
one of the explicit local debits in `R_box^Creutz`.

### Theorem 4.3B.2a: Branch Reserve Certificate Proves `BOX-CONF-PASS`

If `BOX-RESERVE-PASS(beta)` holds for `beta=clean` or `beta=Creutz`, then
`BOX-CONF-PASS` holds. Moreover, for every

```math
0<m_{\rm box}<R_{{\rm box}}^\beta-D_{{\rm box}}^{{\rm KP}},
```

the residual and decorated KP inequalities in Definition 4.3B hold.

Proof.

The certificate includes `BOX-MSKP-IMPORT`; hence Theorem 4.3A.3 supplies
`MS-KP_box`, and Corollary 4.3A.4 supplies the finite threshold
`D_KP,box`. It also includes `CONF-REC`, `CONF-WP`, `MARK-GEOM_box`, and
`MARK-LOSS_box`, together with the branch-appropriate scalar confinement
input.

Corollary 4.2C gives `AL2MARK_box(sigma)` and `CONF-MARK_box(sigma)`.
The branch-specific constants in Definition 4.3A.6 give:

```math
\mu_{\rm box}^S-h_{\rm box}^S-\lambda_{{\rm mark},box}^S
\ge
R_{{\rm box}}^\beta.
```

For any selected `m_box` in the displayed interval,

```math
\delta_{\rm box}^{\rm conf}
>
D_{{\rm box}}^{{\rm KP}}.
```

The same algebra used in Theorems 4.3B.1 and 4.3B.2 then gives

```math
C_{{\rm cum},box}^S A_{\rm box}^S
{e^{-\delta_{\rm box}^{\rm conf}}
\over
1-e^{-\delta_{\rm box}^{\rm conf}}}
+\eta_{{\rm ch},box}
<1,
```

and hence also the residual test without `eta_ch,box`. The branch reserve
inequality gives the positive raw margin. Therefore every clause of
`BOX-CONF-PASS` holds. `square`

### Theorem 4.3B.2b: Paper-15 Creutz Pass Proves `BOX-RESERVE-PASS(Creutz)`

Assume:

1. `P15-CREUTZ-PASS_box(sigma,delta_box,kappa_CR,box)`;
2. `BOX-MSKP-IMPORT`;
3. `CONF-REC` and `CONF-WP`;
4. `MARK-GEOM_box`;
5. `MARK-LOSS_box` holds with finite local Creutz-branch factors
   `M_ctr,box>=1` and `M_tile,box>=1`, and exports
   `c_geom,box=alpha_box s_0` and
   `epsilon_area,box=log M_ctr,box+log M_tile,box`;
6. the downstream Creutz reserve inequality holds:

   ```math
   R_{{\rm box}}^{{\rm Creutz}}
   >
   D_{{\rm box}}^{{\rm KP}}.
   ```

Then `BOX-RESERVE-PASS(Creutz)` holds.

Proof.

Theorem 3.4I.6 applies to the first hypothesis and gives
`CONF-CR_box(sigma)`. This is precisely the scalar confinement input
required by clause 3 of `BOX-RESERVE-PASS(Creutz)`.

The second hypothesis supplies clause 1 of `BOX-RESERVE-PASS(Creutz)`.
The third supplies clause 2. The fourth supplies clause 4. The fifth
supplies clause 5 with exactly the Creutz-branch loss ledger used in
Definition 4.3A.6. The sixth is clause 6. Hence every clause in
Definition 4.3A.6 for the Creutz branch is satisfied, so
`BOX-RESERVE-PASS(Creutz)` holds. `square`

This theorem is the point where the Paper-15 Creutz signal becomes an
operational first-battery confinement input. The ontology is unchanged:
Paper 15 exports a scalar loop-record reserve; Paper 18 only checks that
the same whole-process tower has enough remaining marked-KP reserve after
local counterterm and tiling debits.

### Theorem 4.3B.3: First-Battery Branch Pass/Fail Criterion

Assume `BOX-MSKP-IMPORT` and
`A_box^{branch}` is the available branch set from Definition 4.3A.1.

If `A_box^{branch}` is nonempty and

```math
R_{{\rm box}}^{{\rm best}}
>
D_{{\rm box}}^{{\rm KP}},
```

then `BOX-CONF-PASS` holds. Moreover, for any branch
`beta in A_box^{branch}` satisfying

```math
R_{{\rm box}}^\beta
>
D_{{\rm box}}^{{\rm KP}},
```

one may choose

```math
0<m_{\rm box}
<
R_{{\rm box}}^\beta-D_{{\rm box}}^{{\rm KP}},
```

and the residual and decorated KP tests in Definition 4.3B hold.

Proof.

The definition of `A_box^{branch}` ensures that only branches with their
own confinement input, geometry, loss, and whole-process hypotheses are
eligible. If the maximizing branch is `clean`, then
`BOX-RESERVE-PASS(clean)` holds; if it is `Creutz`, then
`BOX-RESERVE-PASS(Creutz)` holds. Theorem 4.3B.2a gives
`BOX-CONF-PASS`.

For the moreover clause, apply Theorem 4.3B.2a to the particular branch
`beta` satisfying `R_box^beta>D_KP,box`; this gives the displayed interval
for `m_box` and the residual/decorated KP tests. Thus the maximum cannot
mix a clean-branch reserve with a Creutz-branch proof or use an unavailable
estimate. `square`

### Definition 4.3C: Cofinal Confinement Pass Gate `G_j-CONF-PASS`

For a cofinal Paper-17 battery `G_j`, `G_j-CONF-PASS` holds when:

1. `CONF-REC` and `CONF-WP` hold;
2. either `CONF-AL(sigma)` or `CONF-CR(sigma)` holds on the rectangle class
   needed by `G_j`;
3. `AL2MARK_j(sigma)` holds;
4. the marked surface stability gate `MS-KP_j` holds, including the
   Paper-14 `FBE` import, the Paper-15 positive `nCPSC` import after
   endpoint enlargement to `G_j`, marked connected-cumulant constants
   `A_j^S`, `C_cum,j^S`, `h_j^S`, `r_j^S`, endpoint collar amplitudes, and
   a character-tail bound `eta_ch,j`;
5. the visible confinement margin is positive:

   ```math
   M_j^{\rm conf}
   =
   c_{{\rm geom},j}\sigma\ell_j
   -\epsilon_{{\rm area},j}
   -h_j^S
   -\lambda_{{\rm mark},j}^S
   >0;
   ```

6. there is an exported Paper-17 KP rate `m_j` satisfying
   `0<m_j<M_j^{conf}` and the residual/decorated smallness tests:

   ```math
   \delta_j^{\rm conf}
   =
   \mu_j^S
   -m_j
   -h_j^S
   -\lambda_{{\rm mark},j}^S
   >0,
   ```

   ```math
   C_{{\rm cum},j}^S A_j^S
   {e^{-\delta_j^{\rm conf}}\over 1-e^{-\delta_j^{\rm conf}}}
   <1,
   ```

   and

   ```math
   C_{{\rm cum},j}^S A_j^S
   {e^{-\delta_j^{\rm conf}}\over 1-e^{-\delta_j^{\rm conf}}}
   +\eta_{{\rm ch},j}
   <1.
   ```

The visible per-battery pass inequality is:

```math
c_{{\rm geom},j}\sigma\ell_j
-\epsilon_{{\rm area},j}
-h_j^S
-\lambda_{{\rm mark},j}^S
>0.
```

This is the cofinal version of `BOX-CONF-PASS`, still finite in `j`.

### Definition 4.3D: Cofinal Uniform Confinement Pass `CONF-COFINAL-PASS(m_*)`

`CONF-COFINAL-PASS(m_*)` holds when:

1. `G_j-CONF-PASS` holds for every cofinal battery `G_j`;
2. the selected exported rates `m_j` obey the Paper-17 loss reserve

   ```math
   \inf_j
   \left[
   {m_j\over \ell_j}
   -\Delta_{{\rm conf},j}
   \right]
   \ge
   m_*
   >
   0.
   ```

The gross visible reserve screen is

```math
\inf_j
\left[
{c_{{\rm geom},j}\sigma\ell_j
-\epsilon_{{\rm area},j}
-h_j^S
-\lambda_{{\rm mark},j}^S
\over \ell_j}
-\Delta_{{\rm conf},j}
\right]
>0.
```

The exported theorem uses the selected-rate reserve, not merely the gross
screen. A convenient canonical branch sets `m_j=theta M_j^{conf}` for one
fixed `0<theta<1` and proves

```math
\inf_j
\left[
{\theta M_j^{\rm conf}\over \ell_j}
-\Delta_{{\rm conf},j}
\right]
\ge m_*>0,
```

while keeping the residual and decoration tests in Definition 4.3C valid.

### Lemma 4.4: Area Law To Marked Surface Cost

Assume `CONF-REC`, `CONF-WP`, either `CONF-AL(sigma)` or
`CONF-CR(sigma)`, and `CONF-MARK_j(sigma)` for a fixed `j`. Then the marked
surface activities entering `MS-KP_j` have block-distance decay at least

```math
c_{{\rm geom},j}\sigma\ell_j-\epsilon_{{\rm area},j}.
```

Proof.

`CONF-AL` or `CONF-CR` supplies the scalar loop-record area cost. `CONF-REC`
fixes the domain on which this cost may be read. `CONF-WP` ensures that the
marked hulls are estimates inside the same record tower rather than new
hidden variables. `CONF-MARK_j` is exactly the geometric comparison from the
loop-record area cost to the endpoint-marked surface hulls. Combining these
clauses gives the displayed decay. `square`

### Lemma 4.5: Marked Surface Cost Gives `G_j-2PT-KP`

Assume `MS-KP_j` and the positive raw margin

```math
m_j^{\rm conf}
=
\mu_j^S-h_j^S-\lambda_{{\rm mark},j}^S
>0.
```

Then Paper 17's finite marked two-point certificate `G_j-2PT-KP` holds for
the battery `G_j`, with the marked connected-polymer rate chosen below
`m_j^{conf}`.

Proof.

Paper 17's `G_j-2PT-KP` asks for a finite marked connected-polymer expansion
for endpoint records in `G_j`, with a strictly positive residual KP margin
after entropy and endpoint marking are debited. `MS-KP_j` supplies that
expansion. The displayed inequality is precisely the strict residual margin.
Choosing the Paper-17 rate `m_j` with `0<m_j<m_j^{conf}` gives the required
finite certificate. `square`

### Theorem 4.5A: Cofinal Per-Battery Confinement Bridge `G_j-CONF-KP`

For any fixed cofinal battery `G_j`, assume `G_j-CONF-PASS`. Then Paper 17's
certificate `G_j-2PT-KP` holds for that battery.

Proof.

`G_j-CONF-PASS` includes `CONF-REC`, `CONF-WP`, either `CONF-AL(sigma)` or
`CONF-CR(sigma)`, and `AL2MARK_j(sigma)`. Proposition 4.2B gives
`CONF-MARK_j(sigma)`, hence the marked surface decay lower bound for
`mu_j^S`. Since `M_j^conf>0`, this lower bound leaves
`mu_j^S-h_j^S-lambda_mark,j^S>0`. The `MS-KP_j` clause supplies the finite
marked connected-polymer expansion and the Paper-14/Paper-15 imports needed
by Paper 17. The selected rate `m_j` in Definition 4.3C satisfies the
positive residual margin and the residual/decorated smallness tests. Lemma
4.5 therefore gives `G_j-2PT-KP`. `square`

### Theorem 4.5B: First-Battery Confinement Bridge `BOX-CONF-KP`

Assume `BOX-CONF-PASS`. Then Paper 17's first-battery certificate
`BOX-2PT-KP` holds.

More explicitly, the Paper-17 constants may be chosen as:

```math
A_{\rm box}=A_{\rm box}^S,
```

```math
\mu_{\rm box}=\mu_{\rm box}^S,
```

```math
h_{\rm box}=h_{\rm box}^S,
```

```math
C_{{\rm cum},box}=C_{{\rm cum},box}^S,
```

```math
\lambda_{{\rm mark},box}
=
\lambda_{{\rm mark},box}^S,
```

```math
c_{\rm box}(O,P)=c_{\rm box}^S(O,P),
```

with `B_box(O,P)` supplied by the finite endpoint closure and `m_box` chosen
in the interval

```math
0<m_{\rm box}<m_{\rm box}^{\rm conf}.
```

Proof.

By `BOX-CONF-PASS`, the record-domain and whole-process gates hold, and
either `CONF-AL(sigma)` or `CONF-CR(sigma)` holds on the first-battery
rectangle class. `AL2MARK_box(sigma)` and Proposition 4.2B give
`CONF-MARK_box(sigma)`, hence marked surface activity decay
`mu_box^S >= c_geom,box sigma s_0 - epsilon_area,box`.

The `MS-KP_box` clause supplies exactly the Paper-14 `FBE`, Paper-15
positive `nCPSC`, marked connected-cumulant constants, endpoint marking
data, and character-tail data required by Paper 17's Definition
`BOX-2PT-KP`. The positive pass inequality gives a nonempty interval for
`m_box`. The two smallness inequalities in `BOX-CONF-PASS` are Paper 17's
residual and combined decoration tests after substituting the surface
constants listed above. The finite endpoint closure supplies the amplitude
`B_box(O,P)` and collar constants for every endpoint pair in `G_box`.

Thus every clause of Paper 17's `BOX-2PT-KP` certificate is satisfied.
`square`

### Corollary 4.5C: First-Battery Confinement Clustering

Assume:

1. Paper 16 `CYM_WL`;
2. finite-battery `MG-OBS` for `G_box`;
3. Paper 17 `MG-WP`;
4. `BOX-CONF-PASS`;
5. Paper 17 `BOX-MASS`.

Then Paper 17's finite-battery clustering conclusion
`MG-EXP-CLOSE(m_phys,box)` holds on `G_box`.

Proof.

Theorem 4.5B gives `BOX-2PT-KP`. Paper 17, Theorem 5.12 then gives
`MG-EXP-CLOSE(m_phys,box)` on the first plaquette-clover battery. `square`

### Corollary 4.5D: Explicit Branch Reserve Gives First-Battery Clustering

Assume:

1. Paper 16 `CYM_WL`;
2. finite-battery `MG-OBS` for `G_box`;
3. Paper 17 `MG-WP`;
4. `BOX-MSKP-IMPORT`;
5. the first-battery branch set `A_box^{branch}` is nonempty and

   ```math
   R_{{\rm box}}^{{\rm best}}
   >
   D_{{\rm box}}^{{\rm KP}};
   ```

6. Paper 17 `BOX-MASS` holds for a selected rate `m_box` satisfying, for
   some passing branch `beta in A_box^{branch}`,

   ```math
   0<m_{\rm box}
   <
   R_{{\rm box}}^\beta-D_{{\rm box}}^{{\rm KP}}.
   ```

Then

```text
MG-EXP-CLOSE(m_phys,box)
```

holds on `G_box`.

Proof.

The branch reserve assumption, together with `BOX-MSKP-IMPORT`, lets
Theorem 4.3B.3 give `BOX-CONF-PASS` with the selected `m_box`. Corollary
4.5C then applies and gives
`MG-EXP-CLOSE(m_phys,box)` on `G_box`. `square`

In particular, the clean direct branch proves first-battery clustering if

```math
R_{{\rm box}}^{{\rm clean}}
>
D_{{\rm box}}^{{\rm KP}}
```

and `BOX-MASS` holds for some
`0<m_box<R_box^clean-D_box^KP`. The Creutz branch proves the same conclusion
with `R_box^Creutz` in place of `R_box^clean`.

### Corollary 4.5E: Paper-15 Creutz Route Gives First-Battery Clustering

Assume:

1. Paper 16 `CYM_WL`;
2. finite-battery `MG-OBS` for `G_box`;
3. Paper 17 `MG-WP`;
4. `CONF-REC` and `CONF-WP`;
5. `P15-CREUTZ-PASS_box(sigma,delta_box,kappa_CR,box)`;
6. `BOX-MSKP-IMPORT`;
7. `MARK-GEOM_box`;
8. `MARK-LOSS_box` holds with finite local Creutz-branch factors
   `M_ctr,box>=1` and `M_tile,box>=1`, and exports
   `c_geom,box=alpha_box s_0` and
   `epsilon_area,box=log M_ctr,box+log M_tile,box`;
9. the downstream Creutz reserve inequality holds:

   ```math
   R_{{\rm box}}^{{\rm Creutz}}
   >
   D_{{\rm box}}^{{\rm KP}};
   ```

10. Paper 17 `BOX-MASS` holds for a selected rate satisfying

    ```math
    0<m_{\rm box}
    <
    R_{{\rm box}}^{{\rm Creutz}}
    -
    D_{{\rm box}}^{{\rm KP}}.
    ```

Then

```text
MG-EXP-CLOSE(m_phys,box)
```

holds on `G_box`.

Proof.

Theorem 4.3B.2b gives `BOX-RESERVE-PASS(Creutz)` from the Paper-15
Creutz pass, the marked geometry/loss ledgers, and the downstream strict
reserve. Theorem 4.3B.2a then gives `BOX-CONF-PASS` for every selected
rate in the displayed interval. Corollary 4.5C applies with the stated
Paper 16 and Paper 17 hypotheses, so `MG-EXP-CLOSE(m_phys,box)` holds on
`G_box`. `square`

This is the fully wired first-battery Creutz route:

```text
P15-CREUTZ-PASS_box
+ MARK-GEOM_box
+ MARK-LOSS_box
+ BOX-MSKP-IMPORT
+ R_Creutz,box > D_KP,box
+ BOX-MASS
=> MG-EXP-CLOSE(m_phys,box) on G_box.
```

### Definition 4.5F: First-Battery Paper-17 Rate Compatibility

For a passing branch `beta`, define its first-battery surplus above the
marked-KP threshold:

```math
G_{{\rm box}}^\beta
=
R_{{\rm box}}^\beta
-D_{{\rm box}}^{{\rm KP}}.
```

Let `Delta_tot,box` be the Paper-17 first-battery rate-loss ledger from
`BOX-MASS`. The branch is compatible with Paper 17 when

```math
G_{{\rm box}}^\beta
>
s_0\Delta_{{\rm tot},box}.
```

In that case the canonical compatible selected rate is

```math
m_{{\rm box},can}^\beta
=
{G_{{\rm box}}^\beta+s_0\Delta_{{\rm tot},box}\over 2}.
```

The corresponding debited physical rate is

```math
m_{{\rm phys},box}^\beta
=
{G_{{\rm box}}^\beta-s_0\Delta_{{\rm tot},box}\over 2s_0}.
```

This definition separates two questions that were previously easy to blur:
the confinement/KP branch must first leave a positive box surplus
`G_box^beta`; Paper 17 then asks that this surplus beat the independent
transport-loss ledger `s_0 Delta_tot,box`.

### Theorem 4.5G: Rate Compatibility Proves `BOX-MASS`

Assume a branch `beta` satisfies `BOX-RESERVE-PASS(beta)` and

```math
G_{{\rm box}}^\beta
>
s_0\Delta_{{\rm tot},box}.
```

Choose `m_box=m_box,can^beta` as in Definition 4.5F. Then:

1. `0<m_box<R_box^beta-D_KP,box`;
2. Paper 17 `BOX-MASS` holds;
3. the debited first-battery rate is

   ```math
   m_{{\rm phys},box}
   =
   m_{{\rm phys},box}^\beta
   >
   0.
   ```

Proof.

Since `G_box^beta>0`, the canonical rate is positive. Since
`s_0 Delta_tot,box<G_box^beta`,

```math
m_{{\rm box},can}^\beta
=
{G_{{\rm box}}^\beta+s_0\Delta_{{\rm tot},box}\over 2}
<
G_{{\rm box}}^\beta
=
R_{{\rm box}}^\beta-D_{{\rm box}}^{{\rm KP}}.
```

Thus clause 1 holds. Also

```math
{m_{{\rm box},can}^\beta\over s_0}
-\Delta_{{\rm tot},box}
=
{G_{{\rm box}}^\beta-s_0\Delta_{{\rm tot},box}\over 2s_0}
>
0.
```

This is exactly Paper 17 `BOX-MASS`, and it identifies the exported
physical rate. `square`

### Corollary 4.5H: Paper-15 Creutz Route With Explicit `BOX-MASS`

Assume the hypotheses of Theorem 4.3B.2b, and define

```math
G_{{\rm box}}^{{\rm Creutz}}
=
R_{{\rm box}}^{{\rm Creutz}}
-D_{{\rm box}}^{{\rm KP}}.
```

If

```math
G_{{\rm box}}^{{\rm Creutz}}
>
s_0\Delta_{{\rm tot},box},
```

then, with the canonical rate

```math
m_{{\rm box},can}^{{\rm Creutz}}
=
{G_{{\rm box}}^{{\rm Creutz}}
+s_0\Delta_{{\rm tot},box}\over 2},
```

the Paper-15 Creutz route satisfies `BOX-MASS` and exports

```math
m_{{\rm phys},box}^{{\rm Creutz}}
=
{G_{{\rm box}}^{{\rm Creutz}}
-s_0\Delta_{{\rm tot},box}\over 2s_0}
>
0.
```

Consequently, with Paper 16 `CYM_WL`, finite-battery `MG-OBS` for `G_box`,
and Paper 17 `MG-WP`, the conclusion
`MG-EXP-CLOSE(m_phys,box)` holds on `G_box`.

Proof.

Theorem 4.3B.2b gives `BOX-RESERVE-PASS(Creutz)`. Theorem 4.5G, applied
with `beta=Creutz`, gives `BOX-MASS` with the displayed positive physical
rate. Corollary 4.5E then gives first-battery clustering. `square`

### Lemma 4.6: `CONF-UNIF` Gives Paper-17 `MG-UNIF`

Assume `CONF-UNIF(m_*)` and `CONF-WP`. Then the Paper-17 cofinal uniform
reserve `MG-UNIF(m_*)` holds for the rates exported by Lemma 4.5.

Proof.

`CONF-UNIF(m_*)` says that the debited confinement rates
`m_conf,phys,j` have a cofinal lower bound `m_*`. `CONF-WP` identifies the
confinement losses with the cutoff, volume, smearing, block, battery,
regulator, and projective losses debited in Paper 17. Therefore the
Paper-17 debited rates satisfy the same lower bound. `square`

### Theorem 4.6A: Cofinal Confinement Pass Closes Paper-17 Dynamical Gates

Assume `CONF-COFINAL-PASS(m_*)`. Then:

```text
G_j-2PT-KP for every j,
MG-UNIF(m_*).
```

Proof.

For each `j`, `CONF-COFINAL-PASS(m_*)` includes `G_j-CONF-PASS`. Theorem
4.5A gives `G_j-2PT-KP`. The selected-rate reserve in Definition 4.3D is
exactly the Paper-17 cofinal debited-rate condition, with
`Delta_conf,j` identified with the Paper-17 transport-loss ledger by
`CONF-WP`. Hence `MG-UNIF(m_*)` holds. `square`

### Corollary 4.6B: Cofinal Confinement Pass Gives Paper-17 Mass Gap

Assume:

1. Paper 16 `CYM_WL`;
2. Paper 17 `MG-OS-CLOSE`, cofinal `MG-OBS`, and `MG-WP`;
3. `CONF-COFINAL-PASS(m_*)`.

Then `MGAP(m_*)` holds in the declared gauge-invariant OS sector.

Proof.

Theorem 4.6A gives `G_j-2PT-KP` for every `j` and `MG-UNIF(m_*)`. Paper 17,
Theorem 9.3 then gives `MGAP(m_*)`. `square`

### Definition 4.6C: Cofinal Branch Surplus Ledger

For each cofinal battery `G_j`, suppose a branch `beta_j` has been proved
on the same whole-process tower and exports a finite marked-KP threshold
`D_KP,j` and a branch reserve `R_j^{beta_j}`. Define the battery surplus

```math
G_j^{\beta_j}
=
R_j^{\beta_j}
-D_{{\rm KP},j}.
```

The cofinal branch surplus ledger `COF-BRANCH-SURP(m_*)` holds when:

1. `G_j-CONF-PASS` is available for every `j` from the selected branch
   `beta_j`;
2. the Paper-17 transport-loss ledger `Delta_conf,j` is the same ledger used
   in `CONF-WP`;
3. the normalized surplus stays strictly above the transport losses:

   ```math
   \inf_j
   \left[
   {G_j^{\beta_j}\over \ell_j}
   -\Delta_{{\rm conf},j}
   \right]
   \ge
   2m_*
   >
   0.
   ```

When the inequality holds, choose the canonical cofinal rates

```math
m_j^{can}
=
{G_j^{\beta_j}
+\ell_j\Delta_{{\rm conf},j}\over 2}.
```

This is the cofinal analogue of Definition 4.5F. It prevents a proof from
using many positive finite-battery margins whose normalized infimum is zero.

### Theorem 4.6D: Cofinal Branch Surplus Proves `CONF-COFINAL-PASS`

Assume `COF-BRANCH-SURP(m_*)`. Then `CONF-COFINAL-PASS(m_*)` holds.

Proof.

Clause 1 of `COF-BRANCH-SURP(m_*)` gives `G_j-CONF-PASS` for every cofinal
battery, which is clause 1 of `CONF-COFINAL-PASS(m_*)`.

For each `j`, the strict surplus inequality implies

```math
G_j^{\beta_j}
>
\ell_j\Delta_{{\rm conf},j}.
```

Hence the canonical rate satisfies

```math
0<m_j^{can}<G_j^{\beta_j}.
```

It is therefore an admissible selected rate for the branch pass. Moreover,

```math
{m_j^{can}\over\ell_j}
-\Delta_{{\rm conf},j}
=
{1\over 2}
\left[
{G_j^{\beta_j}\over\ell_j}
+\Delta_{{\rm conf},j}
\right]
-\Delta_{{\rm conf},j}
=
{1\over 2}
\left[
{G_j^{\beta_j}\over\ell_j}
-\Delta_{{\rm conf},j}
\right]
\ge
m_*.
```

Taking the infimum over `j` gives the selected-rate reserve in
Definition 4.3D. Thus both clauses of `CONF-COFINAL-PASS(m_*)` hold.
`square`

### Corollary 4.6E: Cofinal Branch Surplus Gives The Paper-17 Mass Gap

Assume:

1. Paper 16 `CYM_WL`;
2. Paper 17 `MG-OS-CLOSE`, cofinal `MG-OBS`, and `MG-WP`;
3. `COF-BRANCH-SURP(m_*)`.

Then `MGAP(m_*)` holds in the declared gauge-invariant OS sector.

Proof.

Theorem 4.6D gives `CONF-COFINAL-PASS(m_*)`. Corollary 4.6B then gives
`MGAP(m_*)`. `square`

### Definition 4.6F: Cofinal Paper-15 Creutz Program

`COF-P15-CREUTZ(m_*)` holds when, for every cofinal battery `G_j`, there is
a finite Creutz window `D_CR,j` and constants
`sigma_j>0`, `delta_j>0`, and `kappa_CR,j>0` such that the box-level
Paper-15 Creutz machinery has a `j`-level analogue on the same
whole-process tower:

1. `P15-CREUTZ-PASS_j(sigma_j,delta_j,kappa_CR,j)` holds, meaning the
   clauses of Definition 3.4I.5 hold with `box` replaced by `j`;
2. `MARK-GEOM_j` and `MARK-LOSS_j` hold for the endpoint records in `G_j`;
3. `MS-KP_j` holds, either directly or through the `j`-level analogue of
   `BOX-MSKP-IMPORT`;
4. the Creutz branch reserve

   ```math
   R_j^{{\rm Creutz}}
   =
   c_{{\rm geom},j}\sigma_j\ell_j
   -\epsilon_{{\rm area},j}
   -h_j^S
   -\lambda_{{\rm mark},j}^S
   ```

   and the `j`-level threshold `D_KP,j` obey

   ```math
   G_j^{{\rm Creutz}}
   =
   R_j^{{\rm Creutz}}
   -D_{{\rm KP},j}
   >
   0;
   ```

5. the normalized surplus has the uniform reserve

   ```math
   \inf_j
   \left[
   {G_j^{{\rm Creutz}}\over\ell_j}
   -\Delta_{{\rm conf},j}
   \right]
   \ge
   2m_*
   >
   0.
   ```

This program is the cofinal version of the first-battery Paper-15 Creutz
route. It is not a new ontology: each item is a scalar record-law estimate
or a finite connected-cumulant estimate for declared endpoint records.

### Theorem 4.6G: Cofinal Paper-15 Creutz Program Proves `CONF-COFINAL-PASS`

Assume `COF-P15-CREUTZ(m_*)`. Then `CONF-COFINAL-PASS(m_*)` holds.

Proof.

For each `j`, `P15-CREUTZ-PASS_j` gives `CONF-CR_j(sigma_j)` by the same
finite-window proof as Theorem 3.4I.6. Together with `MARK-GEOM_j`,
`MARK-LOSS_j`, and `MS-KP_j`, this gives `G_j-CONF-PASS` by the same
argument as Theorem 4.3B.2a, with `box` replaced by `j`.

The fourth and fifth clauses of `COF-P15-CREUTZ(m_*)` are exactly the
cofinal branch surplus ledger `COF-BRANCH-SURP(m_*)`, with
`beta_j=Creutz`. Theorem 4.6D therefore gives
`CONF-COFINAL-PASS(m_*)`. `square`

### Corollary 4.6H: Cofinal Paper-15 Creutz Program Gives The Mass Gap

Assume:

1. Paper 16 `CYM_WL`;
2. Paper 17 `MG-OS-CLOSE`, cofinal `MG-OBS`, and `MG-WP`;
3. `COF-P15-CREUTZ(m_*)`.

Then `MGAP(m_*)` holds in the declared gauge-invariant OS sector.

Proof.

Theorem 4.6G gives `CONF-COFINAL-PASS(m_*)`. Corollary 4.6B gives
`MGAP(m_*)`. `square`

### Definition 4.6I: Actual-Trajectory Confinement Certificate `AYM-CONF-CLOSE`

For pure `4D SU(N)` on the declared heat-kernel or Wilson-comparison
continuum trajectory, `AYM-CONF-CLOSE(m_*)` is the assertion that the
cofinal Paper-15 Creutz program is verified from the actual continuum
record law, with no imported confinement theorem.

It consists of the following same-tower data:

1. Paper 16 supplies `CYM_WL`, hence one reflection-positive,
   Euclidean-covariant, gauge-invariant, loop-continuous whole-process
   Wilson-loop record law.
2. For every cofinal mass-gap probe battery `G_j`, there is a finite
   Creutz window `D_CR,j` and a corresponding Paper-15 finite battery whose
   Creutz sector contains the window after the declared scalar readout.
   This inclusion includes the structural `j`-level Paper-15 pass data:
   declared Creutz cells, scalar normalization, positive counterterm choices,
   and no unledgered readout losses. The numerical reserve and smallness
   estimates are clauses 3--5.
3. The actual trajectory proves the `j`-level Paper-15 reserve:

   ```math
   S_{15,j}
   =
   \gamma_{15,j}M_{15,j}^{bd}
   -\epsilon_{15\to j}
   >
   0.
   ```

4. The actual trajectory proves quantitative loop-modulus and denominator
   control:

   ```math
   \delta_{{\rm req},j}
   =
   \max\left\{
   {E_j^*\over\ell_j^2},
   {4\omega_j^*\over\kappa_{{\rm CR},j}\ell_j^2}
   \right\}
   <
   {S_{15,j}\over 2\ell_j^2}.
   ```

5. The actual trajectory proves the single-window closing inequality:

   ```math
   \alpha_j
   \left(S_{15,j}-2\delta_j\ell_j^2\right)
   >
   L_{{\rm Creutz},j}
   +D_{{\rm KP},j}
   ```

   for some `delta_j>=delta_req,j`.
6. The actual trajectory proves the Paper-17 rate surplus uniformly:

   ```math
   \inf_j
   \left[
   {G_j^{{\rm Creutz}}\over\ell_j}
   -\Delta_{{\rm conf},j}
   \right]
   \ge
   2m_*
   >
   0.
   ```

7. The marked geometry, marked loss, marked KP, regulator/chart,
   projectivity, loop-continuity, and whole-process ledgers used in clauses
   1--6 are the same ledgers as Paper 16 and Paper 17.

This certificate is deliberately stronger than `AYM-CLOSE`. `AYM-CLOSE`
constructs the continuum Wilson-loop record law. `AYM-CONF-CLOSE` proves
that this particular record law has enough positive Creutz/marked-surface
reserve to imply confinement and a mass gap.

### Definition 4.6I.1: `AYM-CONF-CLOSE` Workbench

To work on `AYM-CONF-CLOSE(m_*)` without hiding the actual `4D SU(N)`
burden, split it into eight same-tower subcertificates.

| Name | Content | Strongest current source | Remaining actual-trajectory burden |
| --- | --- | --- | --- |
| `AYM-CONF-LAW` | the actual trajectory supplies `CYM_WL` as one whole-process Wilson-loop record law | Paper 16: `HK-CYC-CLOSE => AYM-CLOSE => CYM_WL` | prove all `HK-CYC-CLOSE` subcertificates on one heat-kernel or comparison tower |
| `AYM-CONF-WIN` | every cofinal `G_j` has a finite Creutz window `D_CR,j`, Paper-15 battery inclusion, and structural Paper-15 pass data after scalar readout | Paper 16: `HK-X15-CLOSE` and Paper 17: cofinal `MG-OBS` | build the cofinal window/battery inclusion maps and keep representation schedules compatible |
| `AYM-CONF-RES` | the transported Paper-15 reserve satisfies `S_15,j=gamma_15,j M_15,j^bd-epsilon_15_to_j>0` | Paper 16: `HK-CREUTZ-CLOSE => AYM-CREUTZ`; Paper 15: `M_15^bd>0` | prove cofinal lower bounds for `gamma_15,j M_15,j^bd-epsilon_15_to_j` |
| `AYM-CONF-LMOD` | denominator and loop-modulus control give `delta_req,j<S_15,j/(2 ell_j^2)` | Paper 16: `HK-LC-CLOSE => AYM-LC`; Paper 18: `CR-LMOD-QUANT_j => CR-LMOD_j` | prove positive Creutz-slot denominators `kappa_CR,j` and small enough transported `omega_j^*` |
| `AYM-CONF-SWIN` | the single-window Creutz closing inequality holds for every `j` | Paper 18: Definition 4.3A.8 and Theorem 4.3A.9 | compute `alpha_j`, `L_Creutz,j`, `D_KP,j`, and choose `delta_j` so the inequality is strict |
| `AYM-CONF-MARK` | `MARK-GEOM_j`, `MARK-LOSS_j`, and `MS-KP_j` hold for every cofinal marked endpoint battery | Paper 18: Sections 4.2A--4.3C; Paper 14/15 imports for finite batteries | prove the marked closure, loss, and connected-polymer constants on the actual cofinal tower |
| `AYM-CONF-RATE` | the cofinal rate surplus leaves `inf_j[G_j^Creutz/ell_j-Delta_conf,j]>=2m_*>0` | Paper 17: `MG-UNIF`; Paper 18: `COF-BRANCH-SURP` | prove the normalized surplus does not collapse to zero as batteries become cofinal |
| `AYM-CONF-WP` | all confinement, Paper-15, Paper-16, and Paper-17 constants use one pushed-forward law and one debit ledger | Paper 16: `HK-WP-CLOSE => AYM-WP`; Paper 17: `MG-WP`; Paper 18: `CONF-WP` | audit that no partial-kernel composition, hidden gauge chart, or duplicated loss appears |

These names are only a workbench. They do not add new ontology. Every entry
is a scalar closed-loop record statement, a marked endpoint-record cumulant
statement, or a same-ledger audit.

### Theorem 4.6I.2: Workbench Closure For Actual Confinement

If the eight workbench subcertificates in Definition 4.6I.1 hold on one
actual `4D SU(N)` whole-process trajectory, then `AYM-CONF-CLOSE(m_*)`
holds.

Proof.

`AYM-CONF-LAW` is clause 1 of `AYM-CONF-CLOSE`. `AYM-CONF-WIN` is clause 2.
`AYM-CONF-RES` is clause 3. `AYM-CONF-LMOD` is clause 4.
`AYM-CONF-SWIN` is clause 5. `AYM-CONF-RATE` is clause 6.
`AYM-CONF-MARK` supplies the marked geometry, marked loss, and marked KP part
of clause 7, while `AYM-CONF-WP` supplies the same-ledger part of clause 7.
Since all eight are assumed on the same whole-process trajectory, every
clause of Definition 4.6I is satisfied.
`square`

### Status After The `AYM-CONF-CLOSE` Workbench Split

| Subcertificate | Current status |
| --- | --- |
| `AYM-CONF-LAW` | reduced to Paper 16 `HK-CYC-CLOSE`; not yet an unconditional actual-continuum construction |
| `AYM-CONF-WIN` | reduced to the explicit map certificate `AYM-CONF-WIN-MAP` |
| `AYM-CONF-RES` | reduced to `P15-RES-CAL_j`, and sharpened by `AYM-CONF-RES-NC` to explicit lower bounds `underline S_15,j>0` |
| `AYM-CONF-LMOD` | reduced to `AYM-CONF-LMOD-EST`: explicit bounds `underline kappa_j`, `overline E_j`, and `overline omega_j` beat `S_15,j` |
| `AYM-CONF-SWIN` | reduced to `AYM-CONF-SWIN-CALC`: the computable margin `Gamma_j>0` |
| `AYM-CONF-MARK` | reduced to `AYM-CONF-MARK-UNIF`: one cofinal marked protocol with explicit geometry, loss, and KP bounds |
| `AYM-CONF-RATE` | reduced to `AYM-CONF-RATE-CALC`, and further to termwise `AYM-CONF-GAMMA-LB`: `inf_j[underline Gamma_j/(2 ell_j)-overline Delta_j]>=2m_*>0` |
| `AYM-CONF-WP` | reduced to Paper 16 `HK-WP-CLOSE`, Paper 17 `MG-WP`, and Paper 18 `CONF-WP` |

The first row is the continuum Wilson-loop construction problem. The middle
rows are the actual confinement problem. The rate row is the step that turns
cofinal confinement into a Paper-17 mass-gap input.

After the seven-step source push below, each row has a named source
certificate:

| Subcertificate | Source-level sufficient certificate |
| --- | --- |
| `AYM-CONF-LAW` | `P16-LAW-IMPORT => AYM-CONF-LAW-SRC` |
| `AYM-CONF-WIN` | `AYM-CONF-WIN-SCHED => AYM-CONF-WIN-SRC => AYM-CONF-WIN-MAP` |
| `AYM-CONF-RES` | `AYM-CONF-RES-SYM` or `AYM-CONF-RES-TAIL` proves `AYM-CONF-RES-CALC => AYM-CONF-RES-SRC => AYM-CONF-RES-NC` |
| `AYM-CONF-LMOD` | `AYM-CONF-LMOD-SYM` or `AYM-CONF-LMOD-TAIL` proves `AYM-CONF-LMOD-CALC => AYM-CONF-LMOD-SRC` |
| `AYM-CONF-MARK` | `AYM-CONF-MARK-SYM` or `AYM-CONF-MARK-TAIL` proves `AYM-CONF-MARK-CALC => AYM-CONF-MARK-SRC` |
| `AYM-CONF-SWIN` and `AYM-CONF-RATE` | `AYM-CONF-GAMMA-CONST-ATTACK(m_*)` decides finite-window Gamma success, compact-tail Gamma success, smaller-rate survival, or Gamma obstruction; success gives `AYM-CONF-GAMMA-SYM(m_*)` or `AYM-CONF-GAMMA-TAIL(m_*)`, hence `AYM-CONF-GAMMA-CALC(m_*) => AYM-CONF-GAMMA-LB(m_*)` |
| `AYM-CONF-WP` | `CONF-IMPORT-WP => AYM-CONF-LEDGER-AUDIT` |

### Definition 4.6I.3: Cofinal Paper-15 Reserve Calibration `P15-RES-CAL_j`

For a cofinal probe battery `G_j`, `P15-RES-CAL_j` is the finite calibration
package that transports Paper 16's `AYM-CREUTZ` reserve into the Paper 18
quantity `S_15,j`.

It consists of:

1. a finite Creutz window `D_CR,j` whose cells are represented inside the
   Paper-15 Creutz-character battery used by Paper 16;
2. a Paper-16 Creutz reserve certificate `HK-CREUTZ-CLOSE_j`, or an
   equivalent `AYM-CREUTZ_j`, exporting a positive reserve

   ```math
   M_{15,j}^{bd}>0;
   ```

3. a scalar readout calibration constant `gamma_15,j>0` comparing the
   Paper-15 Creutz anchor normalization with the Paper-18 log-Creutz
   normalization on `D_CR,j`;
4. a finite alignment loss `epsilon_15_to_j>=0`, including only losses not
   already counted in `M_15,j^bd`;
5. the strict calibration inequality

   ```math
   \epsilon_{15\to j}
   <
   \gamma_{15,j}M_{15,j}^{bd}.
   ```

When these clauses hold, define

```math
S_{15,j}
=
\gamma_{15,j}M_{15,j}^{bd}
-\epsilon_{15\to j}.
```

This is a calibration of scalar records, not a physical identification of a
surface. The factors `gamma_15,j` and `epsilon_15_to_j` must be computed on
the same whole-process tower as the Wilson-loop record law.

### Lemma 4.6I.4: Calibration Gives Positive `S_15,j`

If `P15-RES-CAL_j` holds, then

```math
S_{15,j}>0.
```

Proof.

By definition,

```math
S_{15,j}
=
\gamma_{15,j}M_{15,j}^{bd}
-\epsilon_{15\to j}.
```

The reserve certificate gives `M_15,j^bd>0`, the calibration gives
`gamma_15,j>0`, and the strict calibration inequality gives

```math
\gamma_{15,j}M_{15,j}^{bd}
-\epsilon_{15\to j}
>
0.
```

Thus `S_15,j>0`. `square`

### Definition 4.6I.5: Cofinal Paper-15 Reserve Positivity `AYM-CONF-RES`

`AYM-CONF-RES` holds when, for every cofinal probe battery `G_j`, the
calibration package `P15-RES-CAL_j` holds on the same actual
whole-process trajectory, and the finite windows `D_CR,j` are compatible
with the cofinal battery/window inclusion maps from `AYM-CONF-WIN`.

Equivalently, the actual trajectory exports a sequence of positive scalar
Creutz surpluses:

```math
S_{15,j}>0
```

for every cofinal `j`.

No uniform lower bound is included in this definition. Uniformity enters
later through `AYM-CONF-LMOD`, `AYM-CONF-SWIN`, and `AYM-CONF-RATE`.

### Theorem 4.6I.6: `P15-RES-CAL_j` For All `j` Proves `AYM-CONF-RES`

Assume:

1. `AYM-CONF-WIN` supplies the cofinal Creutz windows and inclusion maps;
2. for every cofinal `j`, `P15-RES-CAL_j` holds on the same whole-process
   trajectory.

Then `AYM-CONF-RES` holds.

Proof.

For each `j`, Lemma 4.6I.4 gives `S_15,j>0`. The first hypothesis ensures
that the calibrated reserve is attached to the Creutz window actually used
by the cofinal battery `G_j`. The second hypothesis ensures the reserve,
calibration, and alignment loss are evaluated on the common actual tower.
These are precisely the clauses of Definition 4.6I.5. `square`

### Corollary 4.6I.7: Paper-16 Creutz Reserve Imports Cofinal `S_15,j`

Assume:

1. `AYM-CONF-WIN`;
2. for every cofinal `j`, Paper 16 proves `HK-CREUTZ-CLOSE_j`, hence
   `AYM-CREUTZ_j`, with reserve `M_15,j^bd>0`;
3. for every cofinal `j`, the scalar readout calibration constants satisfy
   `gamma_15,j>0` and

   ```math
   \epsilon_{15\to j}
   <
   \gamma_{15,j}M_{15,j}^{bd}.
   ```

Then `AYM-CONF-RES` holds.

Proof.

Clauses 2 and 3 are exactly the non-window clauses of `P15-RES-CAL_j`.
Clause 1 supplies the compatible windows. Therefore `P15-RES-CAL_j` holds
for every cofinal `j`, and Theorem 4.6I.6 gives `AYM-CONF-RES`. `square`

This is the requested import of cofinal `S_15,j` positivity. It is still
not the confinement theorem: `S_15,j>0` must later beat the loop-modulus
debit, the marked-KP losses, and the cofinal Paper-17 rate losses.

### Definition 4.6I.8: Cofinal Quantitative Loop-Modulus Certificate `AYM-CONF-LMOD`

`AYM-CONF-LMOD` holds when, for every cofinal battery `G_j`, the actual
whole-process trajectory supplies the following quantitative data on the
same finite Creutz window `D_CR,j`.

1. `AYM-CONF-RES` exports the positive scalar reserve `S_15,j>0`.
2. The Paper-12/Paper-16 scalar normalization and counterterm choices keep
   every loop record in `Slot(D_CR,j)` positive on the declared stages.
3. There is a Creutz-slot denominator `kappa_CR,j>0` such that

   ```math
   \inf_{L\in{\rm Slot}(D_{{\rm CR},j})}
   \mathcal W_\rho(L)
   \ge
   \kappa_{{\rm CR},j}
   ```

   and, eventually along the finite regulator stages,

   ```math
   \inf_{L\in{\rm Slot}(D_{{\rm CR},j})}
   \mathcal W_{\rho,\alpha}(L)
   \ge
   \kappa_{{\rm CR},j}.
   ```

4. Paper 16 loop continuity, through `HK-LC-CLOSE` or an equivalent
   `AYM-LC` ledger, supplies a finite-window loop modulus
   `omega_CR,j(alpha)` satisfying eventually

   ```math
   \omega_{{\rm CR},j}(\alpha)
   \le
   \omega_j^*.
   ```

5. The extra cofinal Creutz readout error not already debited in Paper 15
   satisfies eventually

   ```math
   E_j^{bd}(\alpha)
   \le
   E_j^*.
   ```

6. With

   ```math
   \delta_{{\rm req},j}
   =
   \max\left\{
   {E_j^*\over\ell_j^2},
   {4\omega_j^*\over\kappa_{{\rm CR},j}\ell_j^2}
   \right\},
   ```

   the strict reserve inequality holds:

   ```math
   \delta_{{\rm req},j}
   <
   {S_{15,j}\over 2\ell_j^2}.
   ```

When these clauses hold, choose once and for all a number `delta_j` satisfying

```math
\delta_{{\rm req},j}
\le
\delta_j
<
{S_{15,j}\over 2\ell_j^2}.
```

This certificate is a scalar loop-record statement. The denominator lower
bound is a lower bound on declared Wilson-loop records in a finite Creutz
slot set, not a gauge-fixed statement about an underlying field.

### Theorem 4.6I.9: `AYM-CONF-LMOD` Gives The Cofinal Admissible Delta Window

Assume `AYM-CONF-LMOD`. Then for every cofinal battery `G_j` the chosen
`delta_j` has the following consequences:

1. `CR-ERR_j(delta_j)` holds, meaning the cofinal Creutz readout error is
   eventually at most `delta_j ell_j^2`;
2. the `j`-level quantitative loop-modulus pass
   `CR-LMOD-QUANT_j(delta_j,kappa_CR,j)` holds, hence
   `CR-LMOD_j(delta_j,kappa_CR,j)`;
3. the upstream Paper-15 reserve still has positive room:

   ```math
   S_{15,j}
   -2\delta_j\ell_j^2
   >
   0.
   ```

Proof.

The choice `delta_j>=delta_req,j` and the definition of `delta_req,j` give

```math
E_j^*
\le
\delta_j\ell_j^2.
```

Together with `E_j^{bd}(alpha)<=E_j^*` eventually, this is exactly the
`j`-level `CR-ERR` bound.

The same choice gives

```math
{4\omega_j^*\over\kappa_{{\rm CR},j}}
\le
\delta_j\ell_j^2.
```

Since `omega_CR,j(alpha)<=omega_j^*` eventually, the small-log-modulus
condition required by the `j`-level analogue of Theorem 3.4J.5 holds:

```math
{4\omega_{{\rm CR},j}(\alpha)\over\kappa_{{\rm CR},j}}
\le
\delta_j\ell_j^2.
```

The positive counterterm clause, continuum denominator lower bound, and
finite-stage denominator lower bound are exactly the positivity and
lower-bound clauses of `CR-LMOD-QUANT_j`; Paper 16 loop continuity supplies
its loop-modulus ledger. Thus `CR-LMOD-QUANT_j` holds, and Theorem 3.4J.5,
with `box` replaced by `j`, gives `CR-LMOD_j`.

Finally, the strict upper bound on `delta_j` gives

```math
2\delta_j\ell_j^2
<
S_{15,j},
```

which is the displayed positive room. `square`

### Definition 4.6I.10: Cofinal Single-Window Closing Certificate `AYM-CONF-SWIN`

`AYM-CONF-SWIN` holds when, for every cofinal battery `G_j`, the following
constants are available on the same tower as `AYM-CONF-RES` and
`AYM-CONF-LMOD`:

1. `MARK-GEOM_j` exports a retained-area constant `alpha_j>0` through

   ```math
   c_{{\rm geom},j}
   =
   \alpha_j\ell_j;
   ```

2. `MARK-LOSS_j` and `MS-KP_j` export finite marked Creutz losses collected as

   ```math
   L_{{\rm Creutz},j}
   =
   \epsilon_{{\rm area},j}
   +h_j^S
   +\lambda_{{\rm mark},j}^S;
   ```

3. the marked KP threshold `D_KP,j` is finite;
4. with the `delta_j` selected by `AYM-CONF-LMOD`, the strict closing
   inequality holds:

   ```math
   \alpha_j
   \left(
   S_{15,j}-2\delta_j\ell_j^2
   \right)
   >
   L_{{\rm Creutz},j}
   +D_{{\rm KP},j}.
   ```

This is the cofinal version of Definition 4.3A.8. Its role is to choose one
`sigma_j` that works both upstream, where Paper 15 exports a Creutz area
coefficient, and downstream, where the marked endpoint-polymer bridge debits
entropy and local losses.

### Theorem 4.6I.11: `AYM-CONF-SWIN` Gives One `sigma_j` Passing Both Creutz Reserves

Assume `AYM-CONF-LMOD` and `AYM-CONF-SWIN`. Then for every cofinal battery
`G_j` there exists `sigma_j>0` such that

```math
S_{15,j}
\ge
(\sigma_j+2\delta_j)\ell_j^2
```

and

```math
R_j^{{\rm Creutz}}
>
D_{{\rm KP},j},
```

where

```math
R_j^{{\rm Creutz}}
=
c_{{\rm geom},j}\sigma_j\ell_j
-\epsilon_{{\rm area},j}
-h_j^S
-\lambda_{{\rm mark},j}^S.
```

Proof.

By `AYM-CONF-SWIN`,

```math
{L_{{\rm Creutz},j}+D_{{\rm KP},j}
\over
\alpha_j\ell_j^2}
<
{S_{15,j}\over\ell_j^2}
-2\delta_j.
```

Choose `sigma_j` in this nonempty interval:

```math
{L_{{\rm Creutz},j}+D_{{\rm KP},j}
\over
\alpha_j\ell_j^2}
<
\sigma_j
\le
{S_{15,j}\over\ell_j^2}
-2\delta_j.
```

The upper bound gives

```math
(\sigma_j+2\delta_j)\ell_j^2
\le
S_{15,j},
```

which is the upstream Paper-15 Creutz reserve inequality.

The strict lower bound gives

```math
\alpha_j\sigma_j\ell_j^2
>
L_{{\rm Creutz},j}
+D_{{\rm KP},j}.
```

Using `c_geom,j=alpha_j ell_j` and the definition of `L_Creutz,j`, this is
equivalent to

```math
c_{{\rm geom},j}\sigma_j\ell_j
-\epsilon_{{\rm area},j}
-h_j^S
-\lambda_{{\rm mark},j}^S
>
D_{{\rm KP},j}.
```

That is `R_j^Creutz>D_KP,j`. `square`

### Definition 4.6I.12: Cofinal Marked Bridge Stability `AYM-CONF-MARK`

`AYM-CONF-MARK` holds when every cofinal battery `G_j` carries one marked
endpoint protocol satisfying the following three gates on the same
whole-process tower.

1. `MARK-GEOM_j` holds, exporting `alpha_j>0`, `c_geom,j=alpha_j ell_j`,
   endpoint locality, record compatibility, a finite closure multiplicity
   `N_cl,j`, and a finite boundary-area loss `b_area,j`.
2. `MARK-LOSS_j` holds, exporting one finite local loss ledger
   `epsilon_area,j`, including endpoint collars, tiling remainders,
   perimeter/cusp/counterterm losses, and no loss already counted in
   `S_15,j`.
3. `MS-KP_j` holds, either directly or through the `j`-level analogue of
   `BOX-MSKP-IMPORT`, with finite constants `A_j^S`, `C_cum,j^S`,
   `h_j^S`, `lambda_mark,j^S`, and a character-tail constant
   `eta_ch,j` satisfying

   ```math
   0\le\eta_{{\rm ch},j}<1.
   ```

For such a battery define

```math
D_{{\rm KP},j}
=
\log
{C_{{\rm cum},j}^S A_j^S+1-\eta_{{\rm ch},j}
\over
1-\eta_{{\rm ch},j}}.
```

This bridge is Barandes-aligned in the same sense as the earlier papers: the
marked endpoints are typed instruments used to define scalar record
cumulants. They are not hidden colored beables and they are not extra
configuration variables added to the ontology.

### Theorem 4.6I.13: `AYM-CONF-MARK` Supplies The Marked Cofinal Clauses

Assume `AYM-CONF-MARK`. Then, for every cofinal battery `G_j`:

1. `MARK-GEOM_j`, `MARK-LOSS_j`, and `MS-KP_j` hold;
2. `D_KP,j` is finite;
3. whenever a scalar confinement input `CONF-CR_j(sigma_j)` or
   `CONF-AL_j(sigma_j)` is supplied on the declared closure-loop class,
   `CONF-MARK_j(sigma_j)` follows through `AL2MARK_j(sigma_j)`.

Proof.

Clause 1 is part of the definition of `AYM-CONF-MARK`. Since
`eta_ch,j<1` and `A_j^S`, `C_cum,j^S` are finite, the logarithm defining
`D_KP,j` is finite. The structural bridge

```text
MARK-GEOM_j + MARK-LOSS_j + scalar area or Creutz input
=> AL2MARK_j
=> CONF-MARK_j
```

is Proposition 4.2B and its preceding `AL2MARK_j` theorem with `j` fixed.
Thus the marked cofinal clauses needed by `COF-P15-CREUTZ` are supplied on
the same tower. `square`

### Corollary 4.6I.14: Steps 3--5 Close The Cofinal Finite-Battery Pass Up To Rate

Assume `AYM-CONF-WIN`, `AYM-CONF-RES`, `AYM-CONF-LMOD`,
`AYM-CONF-SWIN`, `AYM-CONF-MARK`, and `AYM-CONF-WP` on one actual
whole-process trajectory. Then every cofinal battery `G_j` has constants
`sigma_j`, `delta_j`, and `kappa_CR,j` such that the first four clauses of
`COF-P15-CREUTZ(m_*)` hold:

1. the `j`-level Paper-15 Creutz pass holds;
2. `MARK-GEOM_j` and `MARK-LOSS_j` hold;
3. `MS-KP_j` holds;
4. `R_j^Creutz>D_KP,j`.

The only remaining `COF-P15-CREUTZ` clause not supplied by these steps is the
uniform normalized rate surplus

```math
\inf_j
\left[
{G_j^{{\rm Creutz}}\over\ell_j}
-\Delta_{{\rm conf},j}
\right]
\ge
2m_*
>
0.
```

Proof.

`AYM-CONF-WIN` supplies the cofinal Creutz windows and Paper-15 battery
alignments. `AYM-CONF-RES` supplies `S_15,j>0`. Theorem 4.6I.9 supplies
`CR-ERR_j(delta_j)`, `CR-LMOD_j(delta_j,kappa_CR,j)`, and positive upstream
room. Theorem 4.6I.11 chooses `sigma_j` so that the upstream Paper-15 reserve
inequality and the downstream Creutz reserve inequality both hold. With the
standard `j`-level Paper-15 pass hypotheses already included in the window
and reserve alignment, the `j`-level analogue of Corollary 3.4J.6 gives
`P15-CREUTZ-PASS_j(sigma_j,delta_j,kappa_CR,j)`. Theorem 4.6I.13 supplies
`MARK-GEOM_j`, `MARK-LOSS_j`, `MS-KP_j`, and finite `D_KP,j`. `AYM-CONF-WP`
ensures these constants are not assembled from different towers.

Thus clauses 1--4 of `COF-P15-CREUTZ(m_*)` hold for every cofinal `j`. The
displayed infimum is exactly clause 5, which is `AYM-CONF-RATE`. `square`

### Definition 4.6I.15: Cofinal Window And Inclusion Maps `AYM-CONF-WIN-MAP`

`AYM-CONF-WIN-MAP` is the explicit map-level version of `AYM-CONF-WIN`. For
each cofinal Paper-17 probe battery `G_j` it consists of the following
finite data, all evaluated on the same whole-process tower.

1. A finite Creutz window `D_CR,j`, including its four-slot loop set
   `Slot(D_CR,j)`.
2. A finite Paper-15 battery `B_15,j` and a scalar readout map

   ```math
   \iota_j:D_{{\rm CR},j}\to B_{15,j}.
   ```

3. A structural pass map

   ```math
   \pi_j:G_j\to{\mathcal P}_{\rm fin}(D_{{\rm CR},j})
   ```

   assigning each mass-gap probe record to the finite set of Creutz cells and
   closure loops used to test it.
4. The Paper-15 structural hypotheses for the image of `iota_j`: declared
   Creutz cells, scalar normalization, positive Paper-12/Paper-16
   counterterm choices, and no readout loss except the one recorded in
   `epsilon_15_to_j` and `E_j^{bd}`.
5. A compatibility clause: every closure loop used by `MARK-GEOM_j` and every
   loop slot used by `CR-LMOD_j` is either in `Slot(D_CR,j)` or is assigned a
   named local loss in `MARK-LOSS_j`.
6. A cofinality clause: for every finite gauge-invariant Paper-17 loop-record
   test battery `F`, there is `j_F` such that for all `j>=j_F`, the records
   in `F` are represented by the maps above after the declared scalar readout.
7. A projective ledger clause: if `j<=k`, the two ways of reading a record
   through `G_j` and through `G_k` agree up to losses already recorded in the
   Paper-16/Paper-18 whole-process ledger.

This is deliberately only a map of scalar records. It is not a choice of
gauge-fixed field representatives and it does not add local hidden variables.

### Theorem 4.6I.16: `AYM-CONF-WIN-MAP` Proves `AYM-CONF-WIN`

If `AYM-CONF-WIN-MAP` holds, then `AYM-CONF-WIN` holds.

Proof.

The first three clauses supply, for every cofinal `G_j`, a finite Creutz
window `D_CR,j`, a finite Paper-15 battery containing that window after
scalar readout, and a map from the Paper-17 probes to the Creutz records used
to test them. Clause 4 supplies the structural Paper-15 pass data. Clauses 5
and 7 ensure that no loop or loss is used outside the declared record and
whole-process ledger. Clause 6 is exactly cofinality. These are precisely the
map-level contents of `AYM-CONF-WIN`. `square`

### Definition 4.6I.17: Actual Loop-Modulus Estimate Ledger `AYM-CONF-LMOD-EST`

`AYM-CONF-LMOD-EST` is a computable sufficient condition for
`AYM-CONF-LMOD`. It holds when `AYM-CONF-WIN-MAP` and `AYM-CONF-RES` hold and,
for every cofinal `j`, there are explicit nonnegative bounds

```math
\underline{\kappa}_j>0,
\quad
\overline{E}_j\ge0,
\quad
\overline{\omega}_j\ge0
```

such that:

1. the continuum and finite-stage Creutz-slot denominator bounds satisfy

   ```math
   \inf_{L\in{\rm Slot}(D_{{\rm CR},j})}
   \mathcal W_\rho(L)
   \ge
   \kappa_{{\rm CR},j}
   \ge
   \underline{\kappa}_j
   ```

   and, eventually,

   ```math
   \inf_{L\in{\rm Slot}(D_{{\rm CR},j})}
   \mathcal W_{\rho,\alpha}(L)
   \ge
   \kappa_{{\rm CR},j}
   \ge
   \underline{\kappa}_j;
   ```

2. the cofinal readout error satisfies eventually

   ```math
   E_j^{bd}(\alpha)
   \le
   \overline{E}_j;
   ```

3. the finite-window loop modulus satisfies eventually

   ```math
   \omega_{{\rm CR},j}(\alpha)
   \le
   \overline{\omega}_j;
   ```

4. the actual estimate margin is strict:

   ```math
   \max\left\{
   {\overline{E}_j\over\ell_j^2},
   {4\overline{\omega}_j\over\underline{\kappa}_j\ell_j^2}
   \right\}
   <
   {S_{15,j}\over 2\ell_j^2}.
   ```

The ledger is allowed to use heat-kernel, Wilson-comparison, or
finite-range-covariance estimates, but only after they are pushed into these
three scalar record bounds.

### Theorem 4.6I.18: `AYM-CONF-LMOD-EST` Proves `AYM-CONF-LMOD`

If `AYM-CONF-LMOD-EST` holds, then `AYM-CONF-LMOD` holds.

Proof.

Set

```math
E_j^*=\overline{E}_j,
\quad
\omega_j^*=\overline{\omega}_j,
\quad
\kappa_{{\rm CR},j}=\underline{\kappa}_j.
```

The denominator, readout-error, and loop-modulus clauses of
`AYM-CONF-LMOD` are then exactly clauses 1--3 of
`AYM-CONF-LMOD-EST`, with the structural positivity supplied by
`AYM-CONF-WIN-MAP`. Clause 4 of `AYM-CONF-LMOD-EST` is the strict
`delta_req,j<S_15,j/(2 ell_j^2)` inequality. Therefore every clause of
`AYM-CONF-LMOD` holds. `square`

### Definition 4.6I.19: Cofinal Single-Window Constants Ledger `AYM-CONF-SWIN-CALC`

Assume `AYM-CONF-RES`, `AYM-CONF-LMOD`, and `AYM-CONF-MARK`. For every
cofinal `j`, define the computable single-window margin

```math
\Gamma_j
=
\alpha_j
\left(
S_{15,j}-2\delta_j\ell_j^2
\right)
-L_{{\rm Creutz},j}
-D_{{\rm KP},j}.
```

`AYM-CONF-SWIN-CALC` holds when these quantities are computed from the same
tower and

```math
\Gamma_j>0
```

for every cofinal `j`.

When `AYM-CONF-SWIN-CALC` holds, define the canonical midpoint choice

```math
\sigma_j^{can}
=
{1\over2}
\left[
{L_{{\rm Creutz},j}+D_{{\rm KP},j}
\over
\alpha_j\ell_j^2}
+
{S_{15,j}\over\ell_j^2}
-2\delta_j
\right].
```

This midpoint is not an added physical parameter. It is a bookkeeping choice
inside the finite scalar-record interval.

### Theorem 4.6I.20: The Single-Window Ledger Gives A Canonical Creutz Reserve

If `AYM-CONF-SWIN-CALC` holds, then `AYM-CONF-SWIN` holds. Moreover, using
`sigma_j=sigma_j^can`,

```math
G_j^{{\rm Creutz}}
=
R_j^{{\rm Creutz}}
-D_{{\rm KP},j}
=
{\Gamma_j\over2}.
```

Proof.

The inequality `Gamma_j>0` is exactly

```math
\alpha_j
\left(
S_{15,j}-2\delta_j\ell_j^2
\right)
>
L_{{\rm Creutz},j}
+D_{{\rm KP},j},
```

so `AYM-CONF-SWIN` holds by Definition 4.6I.10. The midpoint choice lies in
the nonempty interval of Theorem 4.6I.11.

By definition of the interval's lower endpoint,

```math
{L_{{\rm Creutz},j}+D_{{\rm KP},j}
\over
\alpha_j\ell_j^2}
<
\sigma_j^{can}.
```

The distance from the lower endpoint to the midpoint is

```math
{\Gamma_j\over 2\alpha_j\ell_j^2}.
```

Multiplying by `alpha_j ell_j^2` gives

```math
\alpha_j\sigma_j^{can}\ell_j^2
-L_{{\rm Creutz},j}
-D_{{\rm KP},j}
=
{\Gamma_j\over2}.
```

Since `c_geom,j=alpha_j ell_j` and
`L_Creutz,j=epsilon_area,j+h_j^S+lambda_mark,j^S`, the left-hand side is
`R_j^Creutz-D_KP,j`. Therefore `G_j^Creutz=Gamma_j/2`. `square`

### Definition 4.6I.21: Uniform Cofinal Marked Bridge `AYM-CONF-MARK-UNIF`

`AYM-CONF-MARK-UNIF` holds when `AYM-CONF-WIN-MAP` supplies one cofinal
family of marked endpoint protocols and the following uniform construction
data.

1. `MARK-GEOM_j` holds for every `j` with one declared closure rule and
   constants satisfying

   ```math
   \alpha_j\ge\alpha_*>0,
   \quad
   N_{{\rm cl},j}\le N_*<\infty.
   ```

2. `MARK-LOSS_j` holds for every `j` with one local loss rule and explicit
   bounds

   ```math
   \epsilon_{{\rm area},j}
   \le
   \overline{\epsilon}_j.
   ```

3. `MS-KP_j` holds for every `j` with one marked connected-polymer rule and
   constants bounded by explicit sequences

   ```math
   h_j^S\le\overline{h}_j,
   \quad
   \lambda_{{\rm mark},j}^S\le\overline{\lambda}_j,
   \quad
   D_{{\rm KP},j}\le\overline{D}_j.
   ```

4. The character-tail margins are uniformly away from the KP singularity:

   ```math
   \sup_j\eta_{{\rm ch},j}<1.
   ```

Uniform here does not mean every loss is bounded independently of `j`; a
cofinal battery may grow. It means the same finite record protocol, with
explicit bounding sequences, works for the whole tower.

### Theorem 4.6I.22: Uniform Marked Bridge Proves `AYM-CONF-MARK`

If `AYM-CONF-MARK-UNIF` holds, then `AYM-CONF-MARK` holds. In addition,

```math
L_{{\rm Creutz},j}
\le
\overline{\epsilon}_j
+\overline{h}_j
+\overline{\lambda}_j
```

and

```math
D_{{\rm KP},j}\le\overline{D}_j.
```

Proof.

Clauses 1--3 of `AYM-CONF-MARK-UNIF` are the three gates required by
`AYM-CONF-MARK`, with one cofinal rule instead of unrelated
battery-by-battery choices. Clause 4 keeps the logarithmic KP threshold
finite throughout the tower. The two displayed inequalities follow from the
definitions of `L_Creutz,j` and `D_KP,j`. `square`

### Definition 4.6I.23: Computable Rate Certificate `AYM-CONF-RATE-CALC(m_*)`

Assume `AYM-CONF-SWIN-CALC` and use the canonical choices
`sigma_j=sigma_j^can`. `AYM-CONF-RATE-CALC(m_*)` holds when

```math
\inf_j
\left[
{\Gamma_j\over 2\ell_j}
-\Delta_{{\rm conf},j}
\right]
\ge
2m_*
>
0.
```

This is the sharp rate test left by the current reduction. It says that the
single-window margin per physical block length survives every Paper-17
cofinal debit with positive room.

### Theorem 4.6I.24: `AYM-CONF-RATE-CALC` Proves `AYM-CONF-RATE`

If `AYM-CONF-RATE-CALC(m_*)` holds, then `AYM-CONF-RATE` holds for the
canonical single-window choices.

Proof.

By Theorem 4.6I.20, the canonical choices satisfy

```math
G_j^{{\rm Creutz}}
=
{\Gamma_j\over2}.
```

Substituting this identity into the defining inequality of
`AYM-CONF-RATE-CALC(m_*)` gives

```math
\inf_j
\left[
{G_j^{{\rm Creutz}}\over\ell_j}
-\Delta_{{\rm conf},j}
\right]
\ge
2m_*
>
0,
```

which is exactly `AYM-CONF-RATE`. `square`

### Corollary 4.6I.25: Sharp Actual-Confinement Reduction

Assume, on one actual `4D SU(N)` whole-process trajectory:

1. `AYM-CONF-LAW`;
2. `AYM-CONF-WIN-MAP`;
3. `AYM-CONF-RES`;
4. `AYM-CONF-LMOD-EST`;
5. `AYM-CONF-MARK-UNIF`;
6. `AYM-CONF-SWIN-CALC`;
7. `AYM-CONF-RATE-CALC(m_*)`;
8. `AYM-CONF-WP`.

Then `AYM-CONF-CLOSE(m_*)` holds.

Proof.

Theorem 4.6I.16 gives `AYM-CONF-WIN`. Theorem 4.6I.18 gives
`AYM-CONF-LMOD`. Theorem 4.6I.22 gives `AYM-CONF-MARK`. Theorem 4.6I.20
gives `AYM-CONF-SWIN`, and Theorem 4.6I.24 gives `AYM-CONF-RATE`. Together
with the assumed `AYM-CONF-LAW`, `AYM-CONF-RES`, and `AYM-CONF-WP`, all eight
workbench subcertificates hold. Theorem 4.6I.2 gives
`AYM-CONF-CLOSE(m_*)`. `square`

### Definition 4.6I.26: Strengthened Cofinal Reserve Noncollapse `AYM-CONF-RES-NC`

`AYM-CONF-RES-NC` is the termwise lower-bound version of `AYM-CONF-RES`. It
holds when `P15-RES-CAL_j` holds for every cofinal `j` and there are explicit
sequences

```math
\underline{\gamma}_j>0,
\quad
\underline{M}_j>0,
\quad
\overline{\epsilon}_{15,j}\ge0
```

such that

```math
\gamma_{15,j}\ge\underline{\gamma}_j,
\quad
M_{15,j}^{bd}\ge\underline{M}_j,
\quad
\epsilon_{15\to j}\le\overline{\epsilon}_{15,j}.
```

Define the computable reserve lower bound

```math
\underline{S}_{15,j}
=
\underline{\gamma}_j\underline{M}_j
-\overline{\epsilon}_{15,j}.
```

The noncollapse condition is

```math
\underline{S}_{15,j}>0
```

for every cofinal `j`.

This gate is where Paper 15's positive finite-battery reserve is forced to
survive the actual cofinal scalar readout. It remains purely operational:
`gamma_15,j`, `M_15,j^bd`, and `epsilon_15_to_j` are scalar record
calibration constants.

### Lemma 4.6I.27: `AYM-CONF-RES-NC` Gives A Reserve Lower Bound

If `AYM-CONF-RES-NC` holds, then `AYM-CONF-RES` holds and

```math
S_{15,j}\ge\underline{S}_{15,j}>0
```

for every cofinal `j`.

Proof.

By definition,

```math
S_{15,j}
=
\gamma_{15,j}M_{15,j}^{bd}
-\epsilon_{15\to j}.
```

The three displayed bounds in Definition 4.6I.26 give

```math
S_{15,j}
\ge
\underline{\gamma}_j\underline{M}_j
-\overline{\epsilon}_{15,j}
=
\underline{S}_{15,j}.
```

Since `underline S_15,j>0`, `P15-RES-CAL_j` holds with positive surplus for
every cofinal `j`, hence `AYM-CONF-RES` holds by Theorem 4.6I.6. `square`

### Definition 4.6I.28: Actual Loop-Modulus Source Certificate `AYM-CONF-LMOD-SRC`

`AYM-CONF-LMOD-SRC` is a source-level way to prove `AYM-CONF-LMOD-EST` from
the actual heat-kernel or Wilson-comparison trajectory. For every cofinal
window `D_CR,j`, it supplies explicit quantities

```math
\underline{\kappa}_j>0,
\quad
\rho_j>0,
\quad
\varepsilon_{{\rm slot},j}(\alpha),
\quad
\varepsilon_{{\rm loop},j}(\alpha),
\quad
\varepsilon_{{\rm read},j}(\alpha)
```

with the following properties.

1. Continuum slot positivity has a margin:

   ```math
   \inf_{L\in{\rm Slot}(D_{{\rm CR},j})}
   \mathcal W_\rho(L)
   \ge
   \underline{\kappa}_j+\rho_j.
   ```

2. Finite-stage slot transport is eventually bounded by
   `epsilon_slot,j(alpha)` and smaller than the margin:

   ```math
   \sup_{L\in{\rm Slot}(D_{{\rm CR},j})}
   \left|
   \mathcal W_{\rho,\alpha}(L)-\mathcal W_\rho(L)
   \right|
   \le
   \varepsilon_{{\rm slot},j}(\alpha)
   \le
   \rho_j.
   ```

3. Loop-continuity and readout errors satisfy eventually

   ```math
   \omega_{{\rm CR},j}(\alpha)
   \le
   \varepsilon_{{\rm slot},j}(\alpha)
   +
   \varepsilon_{{\rm loop},j}(\alpha),
   \quad
   E_j^{bd}(\alpha)
   \le
   \varepsilon_{{\rm read},j}(\alpha).
   ```

4. There are finite eventual bounds

   ```math
   \varepsilon_{{\rm slot},j}(\alpha)
   +
   \varepsilon_{{\rm loop},j}(\alpha)
   \le
   \overline{\omega}_j,
   \quad
   \varepsilon_{{\rm read},j}(\alpha)
   \le
   \overline{E}_j.
   ```

5. The strict scalar margin holds:

   ```math
   \max\left\{
   {\overline{E}_j\over\ell_j^2},
   {4\overline{\omega}_j\over\underline{\kappa}_j\ell_j^2}
   \right\}
   <
   {S_{15,j}\over2\ell_j^2}.
   ```

The source certificate may be proved by small-field/large-field heat-kernel
analysis, by a Wilson-comparison trajectory, or by imported constructive
estimates. In every case, the output is only the displayed scalar record
bounds.

### Theorem 4.6I.29: `AYM-CONF-LMOD-SRC` Proves `AYM-CONF-LMOD-EST`

Assume `AYM-CONF-WIN-MAP`, `AYM-CONF-RES`, and `AYM-CONF-LMOD-SRC`. Then
`AYM-CONF-LMOD-EST` holds.

Proof.

The continuum slot positivity clause gives the continuum denominator bound
with lower constant `underline kappa_j`. The finite-stage transport estimate
and the margin inequality imply eventually

```math
\inf_{L\in{\rm Slot}(D_{{\rm CR},j})}
\mathcal W_{\rho,\alpha}(L)
\ge
\underline{\kappa}_j.
```

The loop-continuity and readout clauses give the eventual bounds
`omega_CR,j(alpha)<=overline omega_j` and
`E_j^{bd}(alpha)<=overline E_j`. The final strict scalar margin is exactly
clause 4 of `AYM-CONF-LMOD-EST`. `square`

### Definition 4.6I.30: Uniform Marked Source Certificate `AYM-CONF-MARK-SRC`

`AYM-CONF-MARK-SRC` proves `AYM-CONF-MARK-UNIF` from explicit construction
data. It consists of:

1. a single cofinal endpoint-closure rule for the maps in
   `AYM-CONF-WIN-MAP`;
2. constants `alpha_*>0` and finite `N_*` such that the closure rule gives
   `alpha_j>=alpha_*` and `N_cl,j<=N_*`;
3. a single local loss rule exporting bounds
   `epsilon_area,j<=overline epsilon_j`;
4. a marked connected-polymer import or proof exporting
   `h_j^S<=overline h_j`, `lambda_mark,j^S<=overline lambda_j`, and
   `D_KP,j<=overline D_j`;
5. a uniform character-tail margin `sup_j eta_ch,j<1`;
6. a same-ledger clause saying all closure, loss, and KP constants are
   computed from the same pushed-forward law as `AYM-CONF-LAW`.

The source certificate is stronger than `AYM-CONF-MARK-UNIF` only because it
specifies the construction rules generating the uniform bounds.

### Theorem 4.6I.31: `AYM-CONF-MARK-SRC` Proves `AYM-CONF-MARK-UNIF`

If `AYM-CONF-MARK-SRC` holds, then `AYM-CONF-MARK-UNIF` holds.

Proof.

Clauses 1 and 2 are the uniform `MARK-GEOM_j` clauses of
`AYM-CONF-MARK-UNIF`. Clause 3 is the uniform `MARK-LOSS_j` clause. Clauses
4 and 5 are the uniform `MS-KP_j` and finite `D_KP,j` clauses. Clause 6
ensures these are not separate finite-battery constructions glued together
after the fact. Hence all clauses of `AYM-CONF-MARK-UNIF` hold. `square`

### Definition 4.6I.32: Termwise Gamma Lower-Bound Ledger `AYM-CONF-GAMMA-LB(m_*)`

Assume `AYM-CONF-RES-NC`, `AYM-CONF-LMOD-EST`,
`AYM-CONF-MARK-UNIF`, and `AYM-CONF-WP`. A termwise Gamma lower-bound ledger
consists of explicit sequences

```math
\overline{\delta}_j,
\quad
\underline{\alpha}_j,
\quad
\overline{L}_j,
\quad
\overline{D}_j,
\quad
\overline{\Delta}_j
```

such that, for every cofinal `j`,

```math
\delta_j\le\overline{\delta}_j,
\quad
\alpha_j\ge\underline{\alpha}_j>0,
\quad
L_{{\rm Creutz},j}\le\overline{L}_j,
\quad
D_{{\rm KP},j}\le\overline{D}_j,
\quad
\Delta_{{\rm conf},j}\le\overline{\Delta}_j.
```

Define

```math
\underline{\Gamma}_j
=
\underline{\alpha}_j
\left(
\underline{S}_{15,j}-2\overline{\delta}_j\ell_j^2
\right)
-\overline{L}_j
-\overline{D}_j.
```

`AYM-CONF-GAMMA-LB(m_*)` holds when

```math
\underline{\Gamma}_j>0
```

for every cofinal `j` and

```math
\inf_j
\left[
{\underline{\Gamma}_j\over2\ell_j}
-\overline{\Delta}_j
\right]
\ge
2m_*
>
0.
```

This is the most compressed quantitative target in Paper 18: every term in
the actual confinement margin is bounded separately before the cofinal
infimum is taken.

### Theorem 4.6I.33: Termwise Gamma Bounds Prove The Rate Certificate

Assume `AYM-CONF-GAMMA-LB(m_*)`. Then `AYM-CONF-SWIN-CALC` and
`AYM-CONF-RATE-CALC(m_*)` hold.

Proof.

The assumptions built into `AYM-CONF-GAMMA-LB` include `AYM-CONF-RES-NC`,
`AYM-CONF-LMOD-EST`, and `AYM-CONF-MARK-UNIF`. Lemma 4.6I.27 gives
`AYM-CONF-RES` and `S_15,j>=underline S_15,j`; Theorems 4.6I.18 and 4.6I.22
give `AYM-CONF-LMOD` and `AYM-CONF-MARK`. Thus the quantities entering
`Gamma_j` are the legitimate same-tower quantities of Definition 4.6I.19.
By the termwise bounds,

```math
\Gamma_j
=
\alpha_j(S_{15,j}-2\delta_j\ell_j^2)
-L_{{\rm Creutz},j}
-D_{{\rm KP},j}
\ge
\underline{\Gamma}_j.
```

Thus `underline Gamma_j>0` implies `Gamma_j>0`, which is
`AYM-CONF-SWIN-CALC`. Also

```math
{\Gamma_j\over2\ell_j}
-\Delta_{{\rm conf},j}
\ge
{\underline{\Gamma}_j\over2\ell_j}
-\overline{\Delta}_j.
```

Taking the infimum over `j` and using the second inequality in
`AYM-CONF-GAMMA-LB(m_*)` gives `AYM-CONF-RATE-CALC(m_*)`. `square`

### Corollary 4.6I.34: Fully Termwise Actual-Confinement Reduction

Assume, on one actual `4D SU(N)` whole-process trajectory:

1. `AYM-CONF-LAW`;
2. `AYM-CONF-WIN-MAP`;
3. `AYM-CONF-RES-NC`;
4. `AYM-CONF-LMOD-SRC`;
5. `AYM-CONF-MARK-SRC`;
6. `AYM-CONF-GAMMA-LB(m_*)`;
7. `AYM-CONF-WP`.

Then `AYM-CONF-CLOSE(m_*)` holds.

Proof.

Lemma 4.6I.27 gives `AYM-CONF-RES`. Theorem 4.6I.29 gives
`AYM-CONF-LMOD-EST`, hence Theorem 4.6I.18 gives `AYM-CONF-LMOD`. Theorem
4.6I.31 gives `AYM-CONF-MARK-UNIF`, hence Theorem 4.6I.22 gives
`AYM-CONF-MARK`. Theorem 4.6I.33 gives `AYM-CONF-SWIN-CALC` and
`AYM-CONF-RATE-CALC(m_*)`, so Theorem 4.6I.20 gives `AYM-CONF-SWIN` and
Theorem 4.6I.24 gives `AYM-CONF-RATE`. Together with `AYM-CONF-LAW`,
`AYM-CONF-WIN-MAP`, and `AYM-CONF-WP`, Corollary 4.6I.25 gives
`AYM-CONF-CLOSE(m_*)`. `square`

### Theorem 4.6I.35: Remaining Obstruction Theorem For The Paper-18 Route

Fix an actual `4D SU(N)` whole-process trajectory satisfying `AYM-CONF-LAW`
and `AYM-CONF-WP`. If the Paper-18 route does not prove
`AYM-CONF-CLOSE(m_*)` through Corollary 4.6I.34, then at least one of the
following explicit failures occurs:

1. **Window-map failure:** `AYM-CONF-WIN-MAP` fails.
2. **Reserve noncollapse failure:** `AYM-CONF-RES-NC` fails, so the cofinal
   Paper-15 reserve cannot be bounded below by positive `underline S_15,j`.
3. **Loop-modulus source failure:** `AYM-CONF-LMOD-SRC` fails, through a
   denominator collapse, a readout error, or a loop-modulus error too large
   for the available reserve.
4. **Marked source failure:** `AYM-CONF-MARK-SRC` fails, through closure
   geometry, local loss, marked KP, or character-tail instability.
5. **Gamma lower-bound failure:** `AYM-CONF-GAMMA-LB(m_*)` fails; equivalently,
   the termwise lower margin `underline Gamma_j` is nonpositive for some
   cofinal battery or its normalized infimum is zero after Paper-17 debits.
6. **Whole-process mismatch:** one of the preceding certificates is proved on
   a different tower, gauge chart, partial kernel, or charged-record protocol
   than the actual scalar Wilson-loop law.

Proof.

This is the contrapositive of Corollary 4.6I.34. If none of the six failures
occurs, then all seven hypotheses of that corollary hold on the same
whole-process trajectory. Hence `AYM-CONF-CLOSE(m_*)` follows. Therefore, if
the route does not close, at least one listed obstruction must be present.
`square`

### Definition 4.6I.35A: Frozen Actual Source Tower `AYM-CONF-TOWER-FRZ`

`AYM-CONF-TOWER-FRZ` is the tower-freezing step for the source-constant
campaign. It holds when one directed set `I_frz` and one cofinal selector

```math
j\mapsto i(j)\in I_{{\rm frz}}
```

have been fixed once and for all, and the following data are all restrictions
or finite enlargements along that same selector.

1. The Paper-16 continuum Wilson-loop tower: cutoff, volume, heat-kernel or
   Wilson-comparison regulator, smearing, gauge-reconstruction data, and
   pushed-forward finite-stage record laws.
2. The Paper-12 perimeter, cusp, and unsmeared-loop counterterm ledger.
3. The Paper-17 cofinal probe batteries `G_j`, time slabs, representation
   schedules, endpoint instruments, and selected-rate debits
   `overline Delta_j`.
4. The Paper-18 block scales `ell_j`, Creutz-window candidates `D_CR,j`,
   Paper-15 battery candidates `B_15,j`, endpoint collars, marked hulls, and
   loop-modulus readouts.
5. One debit ledger with disjoint buckets:

   ```text
   reserve S
   loop modulus delta
   marked local loss L
   KP/decorated smallness D
   Paper-17 rate Delta
   audit-only zero loss.
   ```

6. Monotone finite enlargement: if `j<=k`, every scalar loop record,
   boundary instrument, representation label, and finite battery used at
   level `j` is represented at level `k` or is compared to it by a named
   projective or loop-modulus debit.
7. No later source certificate may switch to a different regulator,
   counterterm convention, gauge chart, Paper-17 observable family, endpoint
   protocol, or partial subprocess law.

Thus all constants

```text
underline gamma_j, underline M_j, overline epsilon_15,j,
underline kappa_j, overline E_j, overline omega_j,
overline h_j, overline lambda_j, overline D_j, overline Delta_j
```

are functions of the same frozen whole-process record tower.

### Lemma 4.6I.35B: Freezing Prevents Source Mixing

Assume `AYM-CONF-TOWER-FRZ`. If `P16-LAW-IMPORT`,
`AYM-CONF-WIN-SCHED`, and a reserve certificate are all proved relative to
the frozen selector `i(j)`, then the law, window, and reserve constants have
no whole-process mismatch in the sense of Theorem 4.6I.35.

Proof.

By clause 1, all Wilson-loop records are restrictions of one Paper-16
pushed-forward law. By clause 2, every perimeter and cusp counterterm comes
from the same Paper-12 ledger. By clause 3, the Paper-17 probes and selected
rate debits are fixed before the confinement windows are built. By clauses
4 and 6, all Creutz windows and Paper-15 batteries are finite enlargements
or named comparisons inside the same directed family. Clause 5 assigns every
loss label to one bucket, and clause 7 forbids changing the tower after a
constant has been certified. Therefore no law/window/reserve term can be
imported from a different whole-process law or charged-record protocol.
`square`

### Definition 4.6I.35C: Law/Window Source Audit `AYM-CONF-LAWWIN-AUDIT`

`AYM-CONF-LAWWIN-AUDIT` is the combined execution of steps 1 and 2 of the
source-constant campaign. It holds when:

1. `AYM-CONF-TOWER-FRZ` holds;
2. `P16-LAW-IMPORT` holds on the frozen Paper-16 tower;
3. every Paper-18 loop family used by the scheduler is an admissible finite
   restriction of the frozen Paper-16 loop class;
4. `AYM-CONF-WIN-SCHED` is run using the frozen Paper-17 batteries `G_j`,
   frozen block scales `ell_j`, frozen representation schedule, and frozen
   endpoint protocols;
5. the resulting `D_CR,j`, `B_15,j`, `iota_j`, and `pi_j` are entered into
   the frozen debit ledger before any reserve constant is evaluated.

### Theorem 4.6I.35D: Law/Window Audit Proves The First Two Source Gates

If `AYM-CONF-LAWWIN-AUDIT` holds, then

```text
AYM-CONF-LAW-SRC
+ AYM-CONF-WIN-SRC
```

hold on the frozen tower.

Proof.

Clause 2 is exactly the hypothesis of Theorem 4.6I.36b, so it imports
`AYM-CONF-LAW-SRC`. Clauses 3 and 4 are exactly the admissibility and
construction hypotheses of `AYM-CONF-WIN-SCHED`. Theorem 4.6I.38c then gives
`AYM-CONF-WIN-SRC`. Clause 5 and Lemma 4.6I.35B record that both outputs live
on the same frozen whole-process tower. `square`

### Definition 4.6I.35E: First Reserve Constant Attack `AYM-CONF-RES-ATTACK`

`AYM-CONF-RES-ATTACK` is the step-3 calculation performed after
`AYM-CONF-LAWWIN-AUDIT`. For every cofinal `j`, it computes, on the frozen
tower, the transported Paper-15/Paper-16 reserve components

```math
M_{{\rm SUB},j}^{bd},
\quad
L_{{\rm bat},j},
\quad
L_{{\rm reg},j},
\quad
L_{{\rm vol},j},
\quad
L_{{\rm shape},j},
```

the scalar readout calibration

```math
\gamma_{15,j},
\quad
\epsilon_{{\rm norm},j},
\quad
\epsilon_{{\rm ct},j},
\quad
\epsilon_{{\rm proj},j},
\quad
\epsilon_{{\rm win},j},
```

and then sets

```math
\underline{M}_j
=
M_{{\rm SUB},j}^{bd}
-L_{{\rm bat},j}
-L_{{\rm reg},j}
-L_{{\rm vol},j}
-L_{{\rm shape},j},
```

```math
\overline{\epsilon}_{15,j}
=
\epsilon_{{\rm norm},j}
+\epsilon_{{\rm ct},j}
+\epsilon_{{\rm proj},j}
+\epsilon_{{\rm win},j},
```

```math
\underline{S}_{15,j}
=
\gamma_{15,j}\underline{M}_j
-\overline{\epsilon}_{15,j}.
```

For later use in the Gamma ledger, it also records the normalized reserve
densities

```math
s_j^{{\rm area}}
:=
\frac{\underline{S}_{15,j}}{\ell_j^2},
\quad
s_j^{{\rm rate}}
:=
\frac{\underline{S}_{15,j}}{\ell_j}.
```

The attack has four possible outcomes.

1. **Finite-window success:** `gamma_15,j>0`, `underline M_j>0`, and
   `underline S_15,j>0` for every cofinal `j`, with all five extraction
   losses and four readout losses finite and debited once.
2. **Absolute-tail success:** there are constants
   `gamma_R>0`, `M_R>0`, `epsilon_R>=0`, and `s_R>0` such that

   ```math
   \gamma_{15,j}\ge\gamma_R,
   \quad
   \underline{M}_j\ge M_R,
   \quad
   \overline{\epsilon}_{15,j}\le\epsilon_R,
   \quad
   \gamma_RM_R-\epsilon_R\ge s_R>0
   ```

   on a cofinal tail, with the finite prefix checked by finite-window
   success.
3. **Normalized-tail survival:** absolute-tail success is not available, but
   the finite prefix is checked directly and, for the loop-modulus choices
   later used by the Gamma ledger,

   ```math
   q_j^{{\rm loop}}
   :=
   \frac{\underline{S}_{15,j}
   -2\overline{\delta}_j\ell_j^2}{\ell_j}
   ```

   has a positive cofinal lower bound.
4. **Reserve failure:** either some required finite-window
   `underline S_15,j` is nonpositive, or every admissible cofinal
   normalization has `inf_j q_j^{loop}<=0` after the loop-modulus debit.

### Theorem 4.6I.35F: Reserve Attack Trichotomy

Assume `AYM-CONF-LAWWIN-AUDIT` and perform `AYM-CONF-RES-ATTACK`.

1. Finite-window success proves `AYM-CONF-RES-SRC`.
2. Absolute-tail success proves `AYM-CONF-RES-ACT-TAIL`, hence
   `AYM-CONF-RES-SRC`.
3. Normalized-tail survival does not by itself prove
   `AYM-CONF-RES-ACT-TAIL`, but it supplies the reserve part of the later
   `AYM-CONF-GAMMA-RC-TAIL(m_*)` computation through a positive lower bound
   for `q_G`.
4. Reserve failure blocks the Paper-18 confinement proof at the reserve
   source unless the window schedule, normalization, or source estimates are
   changed.

Proof.

For finite-window success, choose

```math
\underline{\gamma}_j=\gamma_{15,j},
\quad
\overline{\epsilon}_{15,j}
\text{ as computed above},
```

and use the computed `underline M_j`. The strict inequality
`underline S_15,j>0` is exactly the reserve positivity clause in
`AYM-CONF-RES-SRC`, while `AYM-CONF-LAWWIN-AUDIT` supplies the law and
window source. Thus `AYM-CONF-RES-SRC` holds.

For absolute-tail success, the displayed constants are exactly clauses 2--4
of `AYM-CONF-RES-ACT-TAIL`, with the finite prefix checked by the
finite-window branch. Theorem 4.6I.40i gives `AYM-CONF-RES-TAIL`, and
Theorem 4.6I.40g gives `AYM-CONF-RES-CALC`; Theorem 4.6I.40c then gives
`AYM-CONF-RES-SRC`.

For normalized-tail survival, the raw lower bound `M_R>0` may fail, so the
absolute reserve theorem is not available. Nevertheless the Gamma-tail
definition only needs a lower bound for

```math
q_j
=
\frac{\underline{S}_{15,j}
-2\overline{\delta}_j\ell_j^2}{\ell_j}.
```

Thus a positive cofinal lower bound for `q_j^{loop}` is exactly the reserve
input `q_G>0` used later by `AYM-CONF-GAMMA-RC-TAIL(m_*)`.

For reserve failure, either a finite scheduled battery lacks positive
reserve, or the normalized loop-debited reserve collapses on every admissible
tail. Then neither the finite-window reserve source nor the compact
Gamma-tail reserve input has been proved. The obstruction is therefore a
genuine reserve-source obstruction, not a bookkeeping issue. `square`

### Definition 4.6I.36: Actual Wilson-Loop Law Source `AYM-CONF-LAW-SRC`

`AYM-CONF-LAW-SRC` is the source-level version of step 1. It holds when the
declared actual `4D SU(N)` trajectory supplies one continuum Wilson-loop
record law by the Paper-16 construction, with the following explicit data.

1. A single heat-kernel or Wilson-comparison tower indexed by cutoff,
   volume, smoothing, block scale, and battery.
2. Finite-stage scalar Wilson-loop records
   `W_alpha(L)` for every loop in every `Slot(D_CR,j)` and in every
   Paper-17 loop test battery.
3. A continuum functional `W(L)` on the cofinal loop algebra such that, for
   every finite loop family `F`,

   ```math
   \sup_{L\in F}|W_\alpha(L)-W(L)|
   \to0.
   ```

4. Reflection positivity, Euclidean covariance, gauge invariance, and loop
   continuity in the sense used by Paper 16.
5. Same-tower compatibility with the Paper-12 perimeter/cusp counterterm
   ledger, the Paper-16 gauge-reconstruction ledger, and the Paper-17
   mass-gap observable ledger.
6. No gauge-fixed field, local sheet, or partial transition kernel is used as
   primitive data; those objects may only witness the scalar record estimates
   above.

This is a Barandes-aligned law certificate: the primitive object is the
whole-process record law and its scalar finite-window restrictions.

### Definition 4.6I.36a: Paper-16 Law Import `P16-LAW-IMPORT`

`P16-LAW-IMPORT` is the exact Paper-16 package needed to prove
`AYM-CONF-LAW-SRC`. It holds when the following data are available on one
declared heat-kernel or Wilson-comparison trajectory.

1. Paper 16 `HK-CYC-CLOSE` holds on a single cofinal closure tower
   `T_HK`. Equivalently, the seven Paper-16 heat-kernel closure gates
   `HK-X15-CLOSE`, `HK-PROJ-CLOSE`, `HK-REG-CLOSE`, `HK-RPCOV-CLOSE`,
   `HK-LC-CLOSE`, `HK-NT-CLOSE`, and `HK-WP-CLOSE` hold on that tower.
2. The Paper-18 loop families are admissible restrictions of the Paper-16
   loop class: for every finite family `F` formed from a Creutz slot,
   rectangular Wilson loop, marked closure loop, Polyakov/static-potential
   loop, or Paper-17 mass-gap test loop, there is a finite Paper-16 loop
   battery containing `F` after the declared scalar readout.
3. The finite-stage laws used by Paper 18 are the restrictions of the
   Paper-16 pushed-forward laws `Gamma_i` to those finite loop batteries.
4. The Paper-12 perimeter/cusp counterterms, the Paper-16 gauge
   reconstruction/counterterm choices, and the Paper-17 mass-gap observable
   restrictions are the same choices used in the Paper-16 whole-process
   ledger `HK-WP-CLOSE`.
5. Gauge-fixed fields, local sheets, flux-tube pictures, and partial
   transition kernels are not primitive objects in the import. They may only
   be used as witnesses for the scalar Wilson-loop estimates already
   present in Paper 16.

The import is intentionally stronger than merely citing `CYM_WL`: it also
states that the loop records later used by confinement are restrictions of
the same Paper-16 whole-process law.

### Theorem 4.6I.36b: Paper 16 Imports `AYM-CONF-LAW-SRC`

If `P16-LAW-IMPORT` holds, then `AYM-CONF-LAW-SRC` holds.

Proof.

By Paper 16 Theorem 9AA.2, `HK-CYC-CLOSE` implies `AYM-CLOSE` and strong
`CYC`. By Paper 16 Corollary 9AA.3 and Theorem 10.1, this gives `CYM_WL`.
By Paper 16 Definition 10.0, `CYM_WL` is a nontrivial, gauge-invariant,
reflection-positive, Euclidean-covariant, loop-continuous continuum
Wilson-loop functional on the declared pure `SU(N)` loop class.

Clause 1 of `P16-LAW-IMPORT` supplies the single cofinal tower. Clause 3
supplies the finite-stage scalar Wilson-loop records by restriction of the
Paper-16 pushed-forward laws. Clause 2 says that every finite loop family
needed by Paper 18 belongs to the declared Paper-16 loop class after scalar
readout; hence the Paper-16 convergence statement applies to each such
finite family. Therefore, for every finite family `F` used by Paper 18,

```math
\sup_{L\in F}|W_\alpha(L)-W(L)|
\to0.
```

The reflection-positivity, Euclidean-covariance, gauge-invariance, and
loop-continuity clauses of `AYM-CONF-LAW-SRC` are exactly the corresponding
clauses of `CYM_WL`, imported through `HK-RPCOV-CLOSE`, `HK-LC-CLOSE`, and
the strong-closure theorem in Paper 16. Clause 4 of `P16-LAW-IMPORT`
provides same-tower compatibility with the Paper-12, Paper-16, and Paper-17
ledgers. Clause 5 supplies the Barandes-aligned ontology restriction: the
primitive object is the whole-process record law, not a hidden gauge-fixed
field process or an unrecorded Markovian subdynamics.

Thus every clause of `AYM-CONF-LAW-SRC` holds. `square`

### Theorem 4.6I.37: `AYM-CONF-LAW-SRC` Proves `AYM-CONF-LAW`

If `AYM-CONF-LAW-SRC` holds, then `AYM-CONF-LAW` holds.

Proof.

Clauses 1--4 give exactly the Paper-16 output `CYM_WL`: a continuum,
reflection-positive, Euclidean-covariant, gauge-invariant Wilson-loop record
law. Clause 5 says that this is the same law used by the confinement and
mass-gap ledgers. Clause 6 excludes a hidden gauge-chart ontology. This is
clause 1 of `AYM-CONF-CLOSE`, which is `AYM-CONF-LAW`. `square`

### Definition 4.6I.38: Cofinal Window Source `AYM-CONF-WIN-SRC`

`AYM-CONF-WIN-SRC` is the source-level version of step 2. It consists of a
cofinal scheduling rule which, for every Paper-17 probe battery `G_j`,
constructs:

1. a finite Creutz window `D_CR,j`;
2. a finite Paper-15 battery `B_15,j`;
3. scalar maps

   ```math
   \iota_j:D_{{\rm CR},j}\to B_{15,j},
   \quad
   \pi_j:G_j\to{\mathcal P}_{\rm fin}(D_{{\rm CR},j});
   ```

4. a representation schedule ensuring that all representations, loop slots,
   endpoint closures, and scalar normalizations used by `G_j` occur inside
   the image of the scheduled finite batteries;
5. a finite-window cofinality function `J(F)` such that every finite
   gauge-invariant loop test family `F` is represented for all `j>=J(F)`;
6. a projective compatibility estimate: if `j<=k`, then reading a scalar
   record through the `j`-window or through the `k`-window differs only by a
   named projective or loop-modulus loss already entered in the ledger;
7. a structural Paper-15 pass clause for each `B_15,j`.

### Definition 4.6I.38a: Canonical Creutz-Window Scheduler `AYM-CONF-WIN-SCHED`

`AYM-CONF-WIN-SCHED` is the explicit combinatorial construction of
`AYM-CONF-WIN-SRC`. It assumes:

1. the Paper-17 cofinal plaquette-clover sequence `G_j` of Definition 2.7;
2. `P16-LAW-IMPORT`, so every loop used below is a restriction of the
   Paper-16 whole-process Wilson-loop law;
3. the Paper-15 finite-battery envelope rule: every finite block graph,
   finite representation set, and finite Creutz-loop family determines a
   finite Paper-15 generator battery containing the corresponding scalar
   Wilson-loop, central-character, and Creutz-character records.

For each `j`, construct the following finite objects.

1. Let `Raw_j` be the finite set of loop records appearing in `G_j`: the
   loops in the Paper-17 skeleton set `D_j`, their declared time translates,
   the plaquette/clover averages, and every loop appearing in products of
   degree at most `p_j`.
2. Let `Hull_j` be the finite set of rational rectangular hulls, block-face
   rectangles, endpoint-collar loops, and closure paths required to support
   the records in `Raw_j` inside the chosen spatial box and time slab.
3. For every rectangle or rational polygonal loop `R in Hull_j`, choose a
   finite Creutz completion `Crt(R)`: the four rectangular loop slots used by
   the Creutz comparison at the same block scale and representation labels.
4. Define the finite Creutz window by cumulative closure:

   ```math
   D_{{\rm CR},j}
   =
   \bigcup_{n\le j}
   \bigcup_{R\in Hull_n}
   {\rm Crt}(R).
   ```

   Then `D_CR,j` is finite, nested in `j`, and closed under the four-slot
   Creutz operation.
5. Define `B_15,j` to be the finite Paper-15 generator battery determined by
   the finite block graph supporting `D_CR,j`, the representation set
   `Rep_j`, and the finite central-character and Creutz-character records
   needed by the Paper-15 reserve theorem.
6. Define

   ```math
   \iota_j:D_{{\rm CR},j}\to B_{15,j}
   ```

   by sending each Creutz cell to its corresponding Paper-15 scalar
   Wilson-loop/character generator tuple.
7. Define

   ```math
   \pi_j: G_j\to{\mathcal P}_{\rm fin}(D_{{\rm CR},j})
   ```

   by sending a centered generator, plaquette/clover average, or finite
   product in `G_j` to the finite union of Creutz completions of the hulls of
   all loop records appearing in that expression.
8. If `j<=k`, use the inclusion `D_CR,j subset D_CR,k` and the Paper-16
   projective comparison map to compare readings through the two windows.
   The difference is assigned to the named projective or loop-modulus debit
   already used by `CONF-DEBIT-REG`.

No step chooses gauge-fixed field representatives. The construction only
enlarges finite scalar loop-record sets.

### Lemma 4.6I.38b: The Scheduler Is Finite, Nested, And Cofinal

Assume `AYM-CONF-WIN-SCHED`. Then:

1. every `D_CR,j` and `B_15,j` is finite;
2. `D_CR,j subset D_CR,k` and `B_15,j` embeds in `B_15,k` for `j<=k`;
3. for every finite gauge-invariant Paper-17 loop-record test family `F`,
   there is `J(F)` such that `F` is represented by the scheduler for all
   `j>=J(F)`.

Proof.

For fixed `j`, `G_j` is finite by Paper 17 Definition 2.7: it uses a finite
box, finite time slab, finite representation set, finite loop skeleton set,
finite product degree, and finite block-scale set. Hence `Raw_j` is finite.
Each record has finitely many hulls and finitely many declared endpoint
closures, so `Hull_j` is finite. Each `Crt(R)` has four slots, so the finite
union defining `D_CR,j` is finite. The Paper-15 envelope rule then gives a
finite `B_15,j`.

The cumulative definition using `n<=j` makes the windows nested. Since the
Paper-15 envelope rule is monotone under finite battery enlargement, the
`B_15,j` embed in the later batteries.

For cofinality, let `F` be a finite gauge-invariant loop-record test family.
Paper 17 cofinal `MG-OBS`, ultimately from Definition 2.7 and Theorem 2.8,
gives `J(F)` such that the loop records in `F` occur in the finite skeleton
and product battery for all `j>=J(F)`. The scheduler takes hulls and Creutz
completions of all those records, so `F` is represented by the corresponding
`D_CR,j` and `B_15,j`. `square`

### Theorem 4.6I.38c: The Scheduler Constructs `AYM-CONF-WIN-SRC`

If `AYM-CONF-WIN-SCHED` holds, then `AYM-CONF-WIN-SRC` holds.

Proof.

Definition 4.6I.38a explicitly constructs `D_CR,j`, `B_15,j`, `iota_j`, and
`pi_j` for every cofinal `j`. Lemma 4.6I.38b gives finiteness, nesting, and
the cofinality function `J(F)`. The construction includes the representation
schedule through `Rep_j`, the closure loops through `Hull_j`, and scalar
normalization through the Paper-15 envelope rule. The projective comparison
for `j<=k` is clause 8 of the scheduler, with all differences assigned to
named debits in the whole-process ledger. The Paper-15 structural pass
clause is built into `B_15,j` by the finite-battery envelope rule.

Thus all seven clauses of `AYM-CONF-WIN-SRC` hold. `square`

### Theorem 4.6I.39: `AYM-CONF-WIN-SRC` Proves `AYM-CONF-WIN-MAP`

If `AYM-CONF-WIN-SRC` holds, then `AYM-CONF-WIN-MAP` holds.

Proof.

Clauses 1--3 provide the finite Creutz windows, Paper-15 batteries, scalar
readout maps, and probe-to-window maps required by Definition 4.6I.15.
Clause 4 gives representation compatibility; clause 5 gives cofinality;
clause 6 gives projective agreement; clause 7 gives the structural Paper-15
pass data. These are precisely the seven clauses of `AYM-CONF-WIN-MAP`.
`square`

### Definition 4.6I.40: Reserve Source `AYM-CONF-RES-SRC`

`AYM-CONF-RES-SRC` is the source-level version of step 3. It holds when
`AYM-CONF-WIN-SRC` supplies the windows and, for every cofinal `j`, the
actual trajectory exports explicit finite-stage-to-continuum bounds

```math
\gamma_{15,j}\ge\underline{\gamma}_j>0,
\quad
M_{15,j}^{bd}\ge\underline{M}_j>0,
\quad
\epsilon_{15\to j}\le\overline{\epsilon}_{15,j}
```

with

```math
\underline{\gamma}_j\underline{M}_j
-\overline{\epsilon}_{15,j}
>
0.
```

The three constants must be computed from the same scalar record law as
`AYM-CONF-LAW-SRC`, with Paper-15 finite-battery reserve, Paper-16
counterterms, and Paper-18 window readout losses entered once.

### Definition 4.6I.40a: Cofinal Reserve Calculation `AYM-CONF-RES-CALC`

`AYM-CONF-RES-CALC` is the explicit calculation layer for
`AYM-CONF-RES-SRC`. It assumes `AYM-CONF-WIN-SCHED`, so the finite windows
`D_CR,j` and Paper-15 batteries `B_15,j` have already been constructed. For
every cofinal `j`, it supplies the following scalar constants on the same
whole-process tower.

1. Paper-16/Paper-15 Creutz reserve data:

   ```math
   M_{{\rm SUB},j}^{bd},
   \quad
   L_{{\rm bat},j},
   \quad
   L_{{\rm reg},j},
   \quad
   L_{{\rm vol},j},
   \quad
   L_{{\rm shape},j}.
   ```

   These are the `j`-level versions of Paper 16 Definition 9R.1.
2. Explicit lower/upper bounds

   ```math
   M_{{\rm SUB},j}^{bd}\ge\underline{M}_{{\rm SUB},j},
   \quad
   L_{{\rm bat},j}\le\overline{L}_{{\rm bat},j},
   \quad
   L_{{\rm reg},j}\le\overline{L}_{{\rm reg},j},
   \quad
   L_{{\rm vol},j}\le\overline{L}_{{\rm vol},j},
   \quad
   L_{{\rm shape},j}\le\overline{L}_{{\rm shape},j}.
   ```

3. The computed Paper-16 reserve lower bound

   ```math
   \underline{M}_j
   =
   \underline{M}_{{\rm SUB},j}
   -\overline{L}_{{\rm bat},j}
   -\overline{L}_{{\rm reg},j}
   -\overline{L}_{{\rm vol},j}
   -\overline{L}_{{\rm shape},j}
   >
   0.
   ```

4. A scalar normalization lower bound

   ```math
   \gamma_{15,j}\ge\underline{\gamma}_j>0.
   ```

   Operationally, `underline gamma_j` is the minimum finite-window
   comparison factor between the Paper-15 Creutz-character anchor
   normalization and the Paper-18 log-Creutz normalization over the finite
   cells in `D_CR,j`.
5. A residual alignment-loss decomposition

   ```math
   \epsilon_{15\to j}
   =
   \epsilon_{{\rm norm},j}
   +\epsilon_{{\rm ct},j}
   +\epsilon_{{\rm proj},j}
   +\epsilon_{{\rm win},j},
   ```

   where none of these four terms is already counted in
   `L_bat,j`, `L_reg,j`, `L_vol,j`, or `L_shape,j`, and

   ```math
   \epsilon_{15\to j}
   \le
   \overline{\epsilon}_{15,j}.
   ```

6. The strict reserve inequality

   ```math
   \underline{S}_{15,j}
   =
   \underline{\gamma}_j\underline{M}_j
   -\overline{\epsilon}_{15,j}
   >
   0.
   ```

This is the first genuinely nontrivial actual-confinement reserve target.
It does not say "there is confinement"; it says that the Paper-15 finite
Creutz reserve, after actual Paper-16 transport and Paper-18 scalar readout,
still leaves a positive scalar surplus on every cofinal window.

### Lemma 4.6I.40b: Reserve Calculation Bounds `M_15,j^bd`

Assume `AYM-CONF-RES-CALC`. Then, for every cofinal `j`, Paper 16
`HK-CREUTZ-CLOSE_j` exports a positive reserve satisfying

```math
M_{15,j}^{bd}\ge\underline{M}_j>0.
```

Proof.

By Paper 16 Definition 9R.1, the transported Creutz reserve is

```math
M_{15,j}^{bd}
=
M_{{\rm SUB},j}^{bd}
-L_{{\rm bat},j}
-L_{{\rm reg},j}
-L_{{\rm vol},j}
-L_{{\rm shape},j}.
```

Using the lower bound for `M_SUB,j^bd` and the upper bounds for the four
losses gives

```math
M_{15,j}^{bd}
\ge
\underline{M}_{{\rm SUB},j}
-\overline{L}_{{\rm bat},j}
-\overline{L}_{{\rm reg},j}
-\overline{L}_{{\rm vol},j}
-\overline{L}_{{\rm shape},j}
=
\underline{M}_j.
```

Clause 3 of `AYM-CONF-RES-CALC` gives `underline M_j>0`. `square`

### Theorem 4.6I.40c: `AYM-CONF-RES-CALC` Proves `AYM-CONF-RES-SRC`

If `AYM-CONF-RES-CALC` holds, then `AYM-CONF-RES-SRC` holds.

Proof.

`AYM-CONF-WIN-SCHED` constructs the windows and Paper-15 batteries, and
Theorem 4.6I.38c gives `AYM-CONF-WIN-SRC`. Lemma 4.6I.40b gives
`M_15,j^bd>=underline M_j>0`. Clause 4 of `AYM-CONF-RES-CALC` gives
`gamma_15,j>=underline gamma_j>0`. Clause 5 gives
`epsilon_15_to_j<=overline epsilon_15,j` with no double counting against the
Paper-16 reserve losses. Clause 6 is precisely

```math
\underline{\gamma}_j\underline{M}_j
-\overline{\epsilon}_{15,j}
>
0.
```

These are exactly the bounds and positivity condition required by
`AYM-CONF-RES-SRC`. `square`

### Definition 4.6I.40d: Symbolic/Numeric Reserve Verifier `AYM-CONF-RES-SYM`

`AYM-CONF-RES-SYM` is the symbolic or interval-arithmetic verifier for
`AYM-CONF-RES-CALC`. It assumes `AYM-CONF-WIN-SCHED`. For every cofinal
window `D_CR,j`, it supplies the following explicit certified quantities.

1. A Paper-15 leading-character interval and sheet data:

   ```math
   0<\underline{u}_j\le u_{-,j}\le u_{+,j}\le\overline{u}_j<1,
   \quad
   N_{0,j}\ge1,
   \quad
   Q_{\sigma,j}\ge1.
   ```

2. A decoration bound:

   ```math
   \eta_{{\rm dec},j}\le\overline{\eta}_j<1,
   \quad
   c_{\Delta,j}\le\overline{c}_{\Delta,j},
   ```

   and

   ```math
   \overline{\Delta}_{{\rm dec},j}
   =
   \exp\left(
   {\overline{c}_{\Delta,j}\overline{\eta}_j
   \over
   1-\overline{\eta}_j}
   \right)-1.
   ```

3. A prior Paper-11--Paper-14 transport bound:

   ```math
   T_{{\rm loss},j}^{bd}\le\overline{T}_{{\rm pre},j}.
   ```

4. The symbolic surface/Creutz lower reserve:

   ```math
   \underline{M}_{{\rm SUB},j}
   =
   \underline{u}_j^{N_{0,j}}
   \left(1-\overline{u}_j^{Q_{\sigma,j}}\right)
   -\overline{\Delta}_{{\rm dec},j}
   -\overline{T}_{{\rm pre},j}.
   ```

5. Paper-16 extraction-loss upper bounds
   `overline L_bat,j`, `overline L_reg,j`, `overline L_vol,j`, and
   `overline L_shape,j`, and the resulting transported reserve lower bound

   ```math
   \underline{M}_j
   =
   \underline{M}_{{\rm SUB},j}
   -\overline{L}_{{\rm bat},j}
   -\overline{L}_{{\rm reg},j}
   -\overline{L}_{{\rm vol},j}
   -\overline{L}_{{\rm shape},j}.
   ```

6. A normalization interval lower bound and residual alignment-loss upper
   bounds:

   ```math
   \gamma_{15,j}\ge\underline{\gamma}_j>0,
   \quad
   \epsilon_{{\rm norm},j}\le\overline{\epsilon}_{{\rm norm},j},
   \quad
   \epsilon_{{\rm ct},j}\le\overline{\epsilon}_{{\rm ct},j},
   \quad
   \epsilon_{{\rm proj},j}\le\overline{\epsilon}_{{\rm proj},j},
   \quad
   \epsilon_{{\rm win},j}\le\overline{\epsilon}_{{\rm win},j}.
   ```

   Define

   ```math
   \overline{\epsilon}_{15,j}
   =
   \overline{\epsilon}_{{\rm norm},j}
   +\overline{\epsilon}_{{\rm ct},j}
   +\overline{\epsilon}_{{\rm proj},j}
   +\overline{\epsilon}_{{\rm win},j}.
   ```

7. The certified reserve test:

   ```math
   \underline{\gamma}_j\underline{M}_j
   >
   \overline{\epsilon}_{15,j}.
   ```

All quantities are scalar record quantities. If the verifier is numerical,
each inequality is interpreted as an interval-arithmetic certificate with
outward-rounded endpoints. If it is symbolic, the displayed inequalities are
proved in the declared parameter domain.

### Theorem 4.6I.40e: `AYM-CONF-RES-SYM` Proves `AYM-CONF-RES-CALC`

If `AYM-CONF-RES-SYM` holds, then `AYM-CONF-RES-CALC` holds.

Proof.

By Paper 15 Definition 11.1 and Definition 11A.2, the block-scale Creutz
reserve is bounded below by

```math
u_{-,j}^{N_{0,j}}
\left(1-u_{+,j}^{Q_{\sigma,j}}\right)
-\Delta_{{\rm dec},j}
-T_{{\rm loss},j}^{bd}.
```

The monotonicities used here are elementary on the declared domain:
`u^N` is increasing for `0<u<1`, `1-u^Q` is decreasing in `u`, and
`exp(c eta/(1-eta))-1` is increasing in both `c>=0` and `0<=eta<1`.
Therefore clauses 1--4 of `AYM-CONF-RES-SYM` give

```math
M_{{\rm SUB},j}^{bd}
\ge
\underline{M}_{{\rm SUB},j}.
```

Clause 5 gives the Paper-16 extraction-loss upper bounds and defines
`underline M_j`. Clause 6 gives the scalar normalization lower bound and
the residual alignment-loss upper bound. Clause 7 is exactly

```math
\underline{\gamma}_j\underline{M}_j
-\overline{\epsilon}_{15,j}
>
0.
```

These are all clauses of `AYM-CONF-RES-CALC`. `square`

### Definition 4.6I.40f: Finite-Prefix And Tail Reserve Test `AYM-CONF-RES-TAIL`

`AYM-CONF-RES-TAIL` is a practical cofinal verifier for
`AYM-CONF-RES-SYM`. It holds when there is a cofinal index `J_*` and a
positive margin `s_*>0` such that:

1. `AYM-CONF-RES-SYM` is verified directly for every `j<J_*`;
2. for every `j>=J_*`, the symbolic/numeric data satisfy

   ```math
   \underline{\gamma}_j\ge\gamma_*,
   \quad
   \underline{M}_j\ge M_*,
   \quad
   \overline{\epsilon}_{15,j}\le\epsilon_*,
   ```

   with

   ```math
   \gamma_*M_*-\epsilon_*\ge s_*>0.
   ```

This is useful when the early cofinal windows must be checked one by one,
but the large-window regime has uniform asymptotic bounds.

### Theorem 4.6I.40g: `AYM-CONF-RES-TAIL` Proves `AYM-CONF-RES-CALC`

If `AYM-CONF-RES-TAIL` holds, then `AYM-CONF-RES-CALC` holds for every
cofinal `j`.

Proof.

For `j<J_*`, the first clause verifies `AYM-CONF-RES-SYM`, hence
`AYM-CONF-RES-CALC` by Theorem 4.6I.40e. For `j>=J_*`, the tail bounds give

```math
\underline{\gamma}_j\underline{M}_j
-\overline{\epsilon}_{15,j}
\ge
\gamma_*M_*-\epsilon_*
\ge
s_*
>
0.
```

The remaining clauses of `AYM-CONF-RES-CALC` are the same symbolic/numeric
bounds used to define the tail data. Hence `AYM-CONF-RES-CALC` holds for
every cofinal `j`. `square`

### Definition 4.6I.40h: Actual Cofinal Reserve Tail Export `AYM-CONF-RES-ACT-TAIL`

`AYM-CONF-RES-ACT-TAIL` is the actual-trajectory source package intended to
prove `AYM-CONF-RES-TAIL` from Paper 15 and Paper 16, without adding a
flux-tube or gauge-fixed ontology. It holds when there are a cofinal index
`J_R` and positive constants

```math
\gamma_R>0,
\quad
M_R>0,
\quad
\epsilon_R\ge0,
\quad
s_R>0
```

such that:

1. the finite prefix is verified directly:

   ```text
   AYM-CONF-RES-SYM holds for every cofinal j<J_R;
   ```

2. for every cofinal `j>=J_R`, Paper 16 supplies a same-tower transported
   Creutz reserve package

   ```text
   HK-CREUTZ-CLOSE_j
   ```

   equivalently `AYM-CREUTZ_j`, with Paper-15/Paper-16 constants

   ```math
   M_{{\rm SUB},j}^{bd},
   L_{{\rm bat},j},
   L_{{\rm reg},j},
   L_{{\rm vol},j},
   L_{{\rm shape},j}
   ```

   satisfying

   ```math
   M_{{\rm SUB},j}^{bd}
   -L_{{\rm bat},j}
   -L_{{\rm reg},j}
   -L_{{\rm vol},j}
   -L_{{\rm shape},j}
   \ge
   M_R;
   ```

3. for every cofinal `j>=J_R`, the Paper-18 scalar readout and normalization
   calibration obeys

   ```math
   \gamma_{15,j}\ge\gamma_R
   ```

   and

   ```math
   \epsilon_{15\to j}
   =
   \epsilon_{{\rm norm},j}
   +\epsilon_{{\rm ct},j}
   +\epsilon_{{\rm proj},j}
   +\epsilon_{{\rm win},j}
   \le
   \epsilon_R,
   ```

   with none of these four alignment losses already included in the five
   `HK-CREUTZ-CLOSE_j` losses;
4. the cofinal reserve margin is strictly positive:

   ```math
   \gamma_RM_R-\epsilon_R
   \ge
   s_R
   >
   0.
   ```

This is the honest actual-trajectory reserve target. Clauses 2 and 3 are
not formalities: they are where the actual continuum `4D SU(N)` tower must
export a transported Creutz reserve and a compatible scalar readout
normalization with enough margin left.

### Theorem 4.6I.40i: `AYM-CONF-RES-ACT-TAIL` Proves `AYM-CONF-RES-TAIL`

If `AYM-CONF-RES-ACT-TAIL` holds, then `AYM-CONF-RES-TAIL` holds. In
particular, the actual cofinal reserve inequality

```math
\underline{\gamma}_j\underline{M}_j
-\overline{\epsilon}_{15,j}
>
0
```

holds for every cofinal `j`.

Proof.

The finite-prefix clause of `AYM-CONF-RES-ACT-TAIL` is exactly clause 1 of
`AYM-CONF-RES-TAIL`.

For `j>=J_R`, define the tail lower and upper bounds used by
`AYM-CONF-RES-TAIL` as

```math
\gamma_*=\gamma_R,
\quad
M_*=M_R,
\quad
\epsilon_*=\epsilon_R.
```

Clause 2 gives the actual transported Creutz reserve lower bound. In the
notation of `AYM-CONF-RES-SYM` and `AYM-CONF-RES-CALC`, this says

```math
\underline{M}_j:=M_R
```

is a valid lower-bound choice for the tail. Clause 3 makes

```math
\underline{\gamma}_j:=\gamma_R,
\quad
\overline{\epsilon}_{15,j}:=\epsilon_R
```

valid calibration choices. Therefore the tail bounds read

```math
\underline{\gamma}_j\ge\gamma_*,
\quad
\underline{M}_j\ge M_*,
\quad
\overline{\epsilon}_{15,j}\le\epsilon_*.
```

Clause 4 gives the strict tail margin

```math
\gamma_*M_*-\epsilon_*
=
\gamma_RM_R-\epsilon_R
\ge
s_R
>
0.
```

These are exactly the tail bounds required by Definition 4.6I.40f. Hence
`AYM-CONF-RES-TAIL` holds. Moreover, Theorem 4.6I.40g then gives
`AYM-CONF-RES-CALC`, whose clause 6 is precisely

```math
\underline{\gamma}_j\underline{M}_j
-\overline{\epsilon}_{15,j}
>
0
```

for every cofinal `j`. `square`

### Corollary 4.6I.40j: Actual Reserve Closure

If `AYM-CONF-RES-ACT-TAIL` holds, then

```text
AYM-CONF-RES-ACT-TAIL
=> AYM-CONF-RES-TAIL
=> AYM-CONF-RES-CALC
=> AYM-CONF-RES-SRC
=> AYM-CONF-RES-NC.
```

Thus the actual positive cofinal reserve is reduced to the four explicit
tail constants `gamma_R`, `M_R`, `epsilon_R`, and `s_R`, with
`gamma_R M_R - epsilon_R >= s_R > 0`.

### Definition 4.6I.40k: Real-Constant Reserve Tail Ledger `AYM-CONF-RES-RC-TAIL`

`AYM-CONF-RES-RC-TAIL` is the explicit real-constant attempt to prove
`AYM-CONF-RES-ACT-TAIL`. It holds when there is a cofinal index `J_R` and
real constants

```math
0<u_R^-\le u_R^+<1,
\quad
N_R<\infty,
\quad
Q_R\ge1,
\quad
0\le\eta_R<1,
\quad
c_{\Delta,R}\ge0,
\quad
T_R\ge0,
```

transport-loss constants

```math
L_{{\rm bat},R},
L_{{\rm reg},R},
L_{{\rm vol},R},
L_{{\rm shape},R}
\ge0,
```

and calibration constants

```math
\gamma_R>0,
\quad
\epsilon_{{\rm norm},R},
\epsilon_{{\rm ct},R},
\epsilon_{{\rm proj},R},
\epsilon_{{\rm win},R}
\ge0
```

such that the following statements hold.

1. The finite prefix is checked directly: `AYM-CONF-RES-SYM` holds for every
   cofinal `j<J_R`.
2. For every cofinal `j>=J_R`, the Paper-15 leading and decoration data obey

   ```math
   u_{-,j}\ge u_R^-,
   \quad
   u_{+,j}\le u_R^+,
   \quad
   N_{0,j}\le N_R,
   \quad
   Q_{\sigma,j}\ge Q_R,
   ```

   and

   ```math
   \eta_{{\rm dec},j}\le\eta_R,
   \quad
   c_{\Delta,j}\le c_{\Delta,R},
   \quad
   T_{{\rm loss},j}^{bd}\le T_R.
   ```

3. For every cofinal `j>=J_R`, the Paper-16 extraction losses obey

   ```math
   L_{{\rm bat},j}\le L_{{\rm bat},R},
   \quad
   L_{{\rm reg},j}\le L_{{\rm reg},R},
   \quad
   L_{{\rm vol},j}\le L_{{\rm vol},R},
   \quad
   L_{{\rm shape},j}\le L_{{\rm shape},R}.
   ```

4. For every cofinal `j>=J_R`, the Paper-18 scalar readout calibration obeys

   ```math
   \gamma_{15,j}\ge\gamma_R
   ```

   and

   ```math
   \epsilon_{{\rm norm},j}\le\epsilon_{{\rm norm},R},
   \quad
   \epsilon_{{\rm ct},j}\le\epsilon_{{\rm ct},R},
   \quad
   \epsilon_{{\rm proj},j}\le\epsilon_{{\rm proj},R},
   \quad
   \epsilon_{{\rm win},j}\le\epsilon_{{\rm win},R}.
   ```

Define

```math
\Delta_R
=
\exp\left(
{c_{\Delta,R}\eta_R\over1-\eta_R}
\right)-1,
```

```math
M_{{\rm SUB},R}
=
(u_R^-)^{N_R}
\left(1-(u_R^+)^{Q_R}\right)
-\Delta_R
-T_R,
```

```math
M_R
=
M_{{\rm SUB},R}
-L_{{\rm bat},R}
-L_{{\rm reg},R}
-L_{{\rm vol},R}
-L_{{\rm shape},R},
```

and

```math
\epsilon_R
=
\epsilon_{{\rm norm},R}
+\epsilon_{{\rm ct},R}
+\epsilon_{{\rm proj},R}
+\epsilon_{{\rm win},R}.
```

The real-constant ledger closes when

```math
M_R>0,
\quad
\gamma_RM_R-\epsilon_R
=
s_R
>
0.
```

The bounded `N_R` clause is not cosmetic. Since `0<u_R^-<1`, a uniform lower
bound on the raw Paper-15 leading sheet requires a uniform upper bound on
the raw minimal-sheet count, or else a different normalized reserve must be
used.

### Theorem 4.6I.40l: Real-Constant Reserve Tail Proves `AYM-CONF-RES-ACT-TAIL`

If `AYM-CONF-RES-RC-TAIL` holds, then `AYM-CONF-RES-ACT-TAIL` holds with
the constants `gamma_R`, `M_R`, `epsilon_R`, and `s_R` defined above.

Proof.

The finite-prefix clause of `AYM-CONF-RES-RC-TAIL` is clause 1 of
`AYM-CONF-RES-ACT-TAIL`.

For `j>=J_R`, the monotonicities are elementary on the declared domain. The
map `u -> u^N` is increasing for `u>0`, and for `0<u<1` it is decreasing in
`N`. Hence `u_{-,j}\ge u_R^-` and `N_{0,j}\le N_R` give

```math
u_{-,j}^{N_{0,j}}
\ge
(u_R^-)^{N_R}.
```

Similarly, `u -> u^Q` is increasing in `u` and decreasing in `Q` on
`0<u<1`, so `u_{+,j}\le u_R^+` and `Q_{\sigma,j}\ge Q_R` give

```math
1-u_{+,j}^{Q_{\sigma,j}}
\ge
1-(u_R^+)^{Q_R}.
```

The decoration bound is monotone in both variables:

```math
\exp\left(
{c_{\Delta,j}\eta_{{\rm dec},j}\over1-\eta_{{\rm dec},j}}
\right)-1
\le
\Delta_R.
```

Together with `T_loss,j^bd<=T_R`, this gives

```math
M_{{\rm SUB},j}^{bd}
\ge
M_{{\rm SUB},R}.
```

Subtracting the four Paper-16 extraction-loss bounds gives

```math
M_{{\rm SUB},j}^{bd}
-L_{{\rm bat},j}
-L_{{\rm reg},j}
-L_{{\rm vol},j}
-L_{{\rm shape},j}
\ge
M_R
>
0.
```

Clause 4 supplies `gamma_15,j>=gamma_R` and
`epsilon_15_to_j<=epsilon_R`. The closing inequality is

```math
\gamma_RM_R-\epsilon_R=s_R>0.
```

These are exactly clauses 2--4 of `AYM-CONF-RES-ACT-TAIL`. `square`

### Theorem 4.6I.40m: Raw Growing-Sheet Tail Falsifies Absolute `AYM-CONF-RES-ACT-TAIL`

Consider the raw Paper-15 leading-sheet branch in which the cofinal window
schedule has unbounded minimal-sheet counts

```math
N_{0,j}\to\infty,
```

and there is a constant `u_{\max}<1` such that, on the cofinal tail,

```math
0<u_{-,j}\le u_{\max}<1.
```

Assume the losses in the transported reserve are nonnegative and the raw
upper estimate

```math
M_{15,j}^{bd}
\le
u_{-,j}^{N_{0,j}}
\left(1-u_{+,j}^{Q_{\sigma,j}}\right)
```

is the only available leading-sheet lower-bound scale for the absolute
reserve. Then no positive constant `M_R>0` can satisfy clause 2 of
`AYM-CONF-RES-ACT-TAIL` on that raw branch. Consequently the raw absolute
tail version of `AYM-CONF-RES-ACT-TAIL` is falsified for such a schedule.

Proof.

Since `0<u_{\max}<1` and `N_{0,j}->infinity`,

```math
u_{\max}^{N_{0,j}}\to0.
```

For every `M_R>0`, choose `j` on the cofinal tail such that
`u_{\max}^{N_{0,j}}<M_R`. Since
`1-u_{+,j}^{Q_{\sigma,j}}\le1` and `u_{-,j}\le u_{\max}`,

```math
u_{-,j}^{N_{0,j}}
\left(1-u_{+,j}^{Q_{\sigma,j}}\right)
\le
u_{\max}^{N_{0,j}}
<
M_R.
```

The transported reserve is no larger than this raw leading scale after
nonnegative losses are subtracted. Thus

```math
M_{15,j}^{bd}<M_R
```

for that tail index, contradicting the required uniform lower bound
`M_15,j^bd>=M_R`. Hence no positive absolute `M_R` exists on the raw
growing-sheet branch. `square`

### Corollary 4.6I.40n: Reserve-Tail Status

The real-constant proof route for `AYM-CONF-RES-ACT-TAIL` is therefore:

```text
uniform local geometry or bounded raw N_0,j
+ real constants u_R^-, u_R^+, N_R, Q_R, eta_R, c_Delta,R, T_R
+ uniform Paper-16 extraction-loss bounds
+ gamma_R>0 and epsilon_R finite
+ gamma_R M_R - epsilon_R = s_R > 0
=> AYM-CONF-RES-RC-TAIL
=> AYM-CONF-RES-ACT-TAIL.
```

The raw growing-sheet branch gives the opposite result:

```text
N_0,j -> infinity with u_{-,j} <= u_max < 1
=> no positive absolute M_R
=> raw absolute AYM-CONF-RES-ACT-TAIL fails.
```

Thus Paper 18 may use `AYM-CONF-RES-ACT-TAIL` only on a genuinely local or
renormalized reserve branch. For raw cofinal growing surfaces, the correct
target is not an absolute `M_R>0`; it is a normalized/rate reserve that feeds
the later Gamma inequality directly.

### Theorem 4.6I.41: `AYM-CONF-RES-SRC` Proves `AYM-CONF-RES-NC`

If `AYM-CONF-RES-SRC` holds, then `AYM-CONF-RES-NC` holds.

Proof.

`AYM-CONF-RES-SRC` includes the Paper-15 reserve calibration for every
scheduled battery and the three lower/upper bounds used in Definition
4.6I.26. The displayed positivity is exactly
`underline S_15,j>0`. Hence all clauses of `AYM-CONF-RES-NC` hold. `square`

### Definition 4.6I.42: Loop-Modulus Calculation `AYM-CONF-LMOD-CALC`

`AYM-CONF-LMOD-CALC` is the sharpened version of step 4. For every cofinal
`j`, it supplies explicit error functions and bounds

```math
\varepsilon_{{\rm slot},j}(\alpha),
\quad
\varepsilon_{{\rm loop},j}(\alpha),
\quad
\varepsilon_{{\rm read},j}(\alpha),
\quad
\underline{\kappa}_j,
\quad
\rho_j,
\quad
\overline{\omega}_j,
\quad
\overline{E}_j
```

such that the five clauses of `AYM-CONF-LMOD-SRC` hold and, additionally,
the eventual bounds are witnessed by a cofinal cutoff selector
`alpha_L(j)`. Thus for all `alpha>=alpha_L(j)`,

```math
\varepsilon_{{\rm slot},j}(\alpha)
+\varepsilon_{{\rm loop},j}(\alpha)
\le
\overline{\omega}_j,
\quad
\varepsilon_{{\rm read},j}(\alpha)
\le
\overline{E}_j.
```

The selector is part of the data because the actual continuum proof must
show not just convergence but convergence fast enough for the reserve
ledger.

### Theorem 4.6I.43: `AYM-CONF-LMOD-CALC` Proves `AYM-CONF-LMOD-SRC`

If `AYM-CONF-LMOD-CALC` holds, then `AYM-CONF-LMOD-SRC` holds.

Proof.

The calculation certificate repeats the slot positivity, finite-stage
transport, loop-continuity, readout, and strict scalar margin clauses of
Definition 4.6I.28, with the extra cutoff selector identifying where the
eventual bounds begin. Forgetting the selector leaves exactly
`AYM-CONF-LMOD-SRC`. `square`

### Definition 4.6I.43a: Symbolic/Numeric Loop-Modulus Verifier `AYM-CONF-LMOD-SYM`

`AYM-CONF-LMOD-SYM` is the symbolic or interval-arithmetic verifier for
`AYM-CONF-LMOD-CALC`. It is read relative to the constructed cofinal windows
of `AYM-CONF-WIN-SCHED` and the reserve lower bounds of
`AYM-CONF-RES-NC`. For every cofinal window `D_CR,j`, it supplies the
following scalar data.

1. A continuum slot-denominator certificate:

   ```math
   \underline{\kappa}_j>0,
   \quad
   \rho_j>0,
   \quad
   p_{{\rm slot},j}>0,
   \quad
   \overline e_{{\rm den},j}\ge0,
   ```

   with

   ```math
   p_{{\rm slot},j}-\overline e_{{\rm den},j}
   \ge
   \underline{\kappa}_j+\rho_j
   ```

   and

   ```math
   \inf_{L\in{\rm Slot}(D_{{\rm CR},j})}
   \mathcal W_\rho(L)
   \ge
   p_{{\rm slot},j}-\overline e_{{\rm den},j}.
   ```

2. A finite-stage denominator transport selector `alpha_den(j)` such that,
   for all `alpha>=alpha_den(j)`,

   ```math
   \sup_{L\in{\rm Slot}(D_{{\rm CR},j})}
   \left|
   \mathcal W_{\rho,\alpha}(L)-\mathcal W_\rho(L)
   \right|
   \le
   \varepsilon_{{\rm slot},j}(\alpha)
   \le
   \rho_j.
   ```

3. A loop-modulus decomposition and selector `alpha_loop(j)`:

   ```math
   \varepsilon_{{\rm loop},j}(\alpha)
   =
   \varepsilon_{{\rm shape},j}(\alpha)
   +\varepsilon_{{\rm ren},j}(\alpha)
   +\varepsilon_{{\rm vol},j}(\alpha)
   +\varepsilon_{{\rm reg},j}(\alpha)
   +\varepsilon_{{\rm proj},j}(\alpha),
   ```

   with all summands nonnegative and, for all `alpha>=alpha_loop(j)`,

   ```math
   \omega_{{\rm CR},j}(\alpha)
   \le
   \varepsilon_{{\rm slot},j}(\alpha)
   +
   \varepsilon_{{\rm loop},j}(\alpha)
   \le
   \overline{\omega}_j.
   ```

4. A readout-error decomposition and selector `alpha_read(j)`:

   ```math
   \varepsilon_{{\rm read},j}(\alpha)
   =
   \varepsilon_{{\rm norm},j}^{E}(\alpha)
   +\varepsilon_{{\rm ct},j}^{E}(\alpha)
   +\varepsilon_{{\rm proj},j}^{E}(\alpha)
   +\varepsilon_{{\rm win},j}^{E}(\alpha),
   ```

   with all summands nonnegative and, for all `alpha>=alpha_read(j)`,

   ```math
   E_j^{bd}(\alpha)
   \le
   \varepsilon_{{\rm read},j}(\alpha)
   \le
   \overline{E}_j.
   ```

5. The cutoff selector and strict reserve comparison:

   ```math
   \alpha_L(j)
   =
   \max\{\alpha_{{\rm den}}(j),\alpha_{{\rm loop}}(j),
   \alpha_{{\rm read}}(j)\}
   ```

   and

   ```math
   \max\left\{
   {\overline{E}_j\over\ell_j^2},
   {4\overline{\omega}_j\over\underline{\kappa}_j\ell_j^2}
   \right\}
   <
   {\underline{S}_{15,j}\over2\ell_j^2}.
   ```

All estimates in this verifier are scalar closed-loop estimates. A numerical
implementation must certify the inequalities by outward-rounded intervals;
a symbolic implementation must prove them uniformly on the declared
parameter domain.

### Theorem 4.6I.43b: `AYM-CONF-LMOD-SYM` Proves `AYM-CONF-LMOD-CALC`

If `AYM-CONF-LMOD-SYM` holds, then `AYM-CONF-LMOD-CALC` holds.

Proof.

Clause 1 gives the continuum slot positivity clause of
`AYM-CONF-LMOD-SRC` because

```math
\inf_{L\in{\rm Slot}(D_{{\rm CR},j})}
\mathcal W_\rho(L)
\ge
p_{{\rm slot},j}-\overline e_{{\rm den},j}
\ge
\underline{\kappa}_j+\rho_j.
```

Clause 2 is exactly the finite-stage slot-transport clause. Clause 3 gives
the required loop-modulus bound, and clause 4 gives the required readout
bound. Let `alpha>=alpha_L(j)`. Then clauses 2--4 are all simultaneously
valid, so the eventual bounds in Definition 4.6I.42 hold.

It remains only to compare the margin with the actual reserve `S_15,j`.
Since `AYM-CONF-LMOD-SYM` is read relative to `AYM-CONF-RES-NC`, Lemma
4.6I.27 gives

```math
S_{15,j}\ge\underline{S}_{15,j}>0.
```

Therefore the strict inequality in clause 5 implies

```math
\max\left\{
{\overline{E}_j\over\ell_j^2},
{4\overline{\omega}_j\over\underline{\kappa}_j\ell_j^2}
\right\}
<
{S_{15,j}\over2\ell_j^2}.
```

Thus the five source clauses and the explicit cutoff selector required by
`AYM-CONF-LMOD-CALC` all hold. `square`

### Definition 4.6I.43c: Finite-Prefix And Tail Loop-Modulus Test `AYM-CONF-LMOD-TAIL`

`AYM-CONF-LMOD-TAIL` is a practical cofinal verifier for
`AYM-CONF-LMOD-SYM`. It holds when there is an index `J_L` and positive tail
constants

```math
s_L>0,
\quad
\kappa_L>0,
\quad
e_L\ge0,
\quad
w_L\ge0
```

such that:

1. `AYM-CONF-LMOD-SYM` is verified directly for every cofinal `j<J_L`;
2. for every cofinal `j>=J_L`, clauses 1--4 of
   `AYM-CONF-LMOD-SYM` hold with one declared tail rule and explicit
   selectors `alpha_den(j)`, `alpha_loop(j)`, and `alpha_read(j)`;
3. for every cofinal `j>=J_L`, the normalized reserve and loop-modulus
   quantities obey

   ```math
   {\underline{S}_{15,j}\over\ell_j^2}
   \ge
   s_L,
   \quad
   \underline{\kappa}_j\ge\kappa_L,
   \quad
   {\overline{E}_j\over\ell_j^2}
   \le
   e_L,
   \quad
   {4\overline{\omega}_j
   \over
   \underline{\kappa}_j\ell_j^2}
   \le
   w_L;
   ```

4. the tail margin is strict:

   ```math
   \max\{e_L,w_L\}
   <
   {s_L\over2}.
   ```

The tail test separates the finite arithmetic problem from the asymptotic
one. Early windows can be checked one by one; the large-window regime only
needs a uniform normalized reserve lower bound and uniform normalized error
upper bounds.

### Theorem 4.6I.43d: `AYM-CONF-LMOD-TAIL` Proves `AYM-CONF-LMOD-CALC`

If `AYM-CONF-LMOD-TAIL` holds, then `AYM-CONF-LMOD-CALC` holds for every
cofinal `j`.

Proof.

For `j<J_L`, clause 1 gives `AYM-CONF-LMOD-SYM`, so Theorem 4.6I.43b gives
`AYM-CONF-LMOD-CALC`.

For `j>=J_L`, clauses 2 and 3 supply the denominator, loop-modulus, readout,
and selector data required by `AYM-CONF-LMOD-SYM`. The strict tail margin
gives

```math
\max\left\{
{\overline{E}_j\over\ell_j^2},
{4\overline{\omega}_j\over\underline{\kappa}_j\ell_j^2}
\right\}
\le
\max\{e_L,w_L\}
<
{s_L\over2}
\le
{\underline{S}_{15,j}\over2\ell_j^2}.
```

Thus clause 5 of `AYM-CONF-LMOD-SYM` also holds on the tail. Theorem
4.6I.43b then gives `AYM-CONF-LMOD-CALC` for every cofinal tail index.
Together with the finite-prefix verification, `AYM-CONF-LMOD-CALC` holds
cofinally. `square`

### Definition 4.6I.43e: Actual Loop-Modulus Source Export `AYM-CONF-LMOD-ACT-SYM`

`AYM-CONF-LMOD-ACT-SYM` is the actual-trajectory source package intended to
prove `AYM-CONF-LMOD-SYM` from the Paper-16 Wilson-loop law, loop-continuity
ledger, and finite-window nontriviality/positivity estimates. For every
cofinal window `D_CR,j`, it supplies the following same-tower data.

1. A finite-window Creutz-slot denominator export:

   ```math
   p_{{\rm slot},j}>0,
   \quad
   \overline e_{{\rm den},j}\ge0,
   \quad
   \underline{\kappa}_j>0,
   \quad
   \rho_j>0,
   ```

   with

   ```math
   \inf_{L\in{\rm Slot}(D_{{\rm CR},j})}
   \mathcal W_\rho(L)
   \ge
   p_{{\rm slot},j}-\overline e_{{\rm den},j}
   \ge
   \underline{\kappa}_j+\rho_j.
   ```

   This may be proved by a Paper-13/15 finite-window nontriviality anchor,
   by a Paper-16 transported Creutz-slot positivity certificate, or by a
   direct Wilson-loop lower-bound ledger on the finite window. The output is
   only the displayed scalar lower bound.

2. A finite-stage slot-transport export from the same tower. There is
   `alpha_den(j)` such that, for all `alpha>=alpha_den(j)`,

   ```math
   \sup_{L\in{\rm Slot}(D_{{\rm CR},j})}
   \left|
   \mathcal W_{\rho,\alpha}(L)-\mathcal W_\rho(L)
   \right|
   \le
   \varepsilon_{{\rm slot},j}(\alpha)
   \le
   \rho_j.
   ```

3. A Paper-16/Paper-12 loop-continuity export. There is `alpha_loop(j)` and
   a nonnegative decomposition

   ```math
   \varepsilon_{{\rm loop},j}(\alpha)
   =
   \varepsilon_{{\rm shape},j}(\alpha)
   +\varepsilon_{{\rm ren},j}(\alpha)
   +\varepsilon_{{\rm vol},j}(\alpha)
   +\varepsilon_{{\rm reg},j}(\alpha)
   +\varepsilon_{{\rm proj},j}(\alpha)
   ```

   such that, for all `alpha>=alpha_loop(j)`,

   ```math
   \omega_{{\rm CR},j}(\alpha)
   \le
   \varepsilon_{{\rm slot},j}(\alpha)
   +
   \varepsilon_{{\rm loop},j}(\alpha)
   \le
   \overline{\omega}_j.
   ```

4. A finite-window readout-error export. There is `alpha_read(j)` and a
   nonnegative decomposition

   ```math
   \varepsilon_{{\rm read},j}(\alpha)
   =
   \varepsilon_{{\rm norm},j}^{E}(\alpha)
   +\varepsilon_{{\rm ct},j}^{E}(\alpha)
   +\varepsilon_{{\rm proj},j}^{E}(\alpha)
   +\varepsilon_{{\rm win},j}^{E}(\alpha)
   ```

   such that, for all `alpha>=alpha_read(j)`,

   ```math
   E_j^{bd}(\alpha)
   \le
   \varepsilon_{{\rm read},j}(\alpha)
   \le
   \overline{E}_j.
   ```

5. The loop-modulus debit is small compared with the already established
   reserve lower bound:

   ```math
   \max\left\{
   {\overline{E}_j\over\ell_j^2},
   {4\overline{\omega}_j\over\underline{\kappa}_j\ell_j^2}
   \right\}
   <
   {\underline{S}_{15,j}\over2\ell_j^2}.
   ```

This certificate is deliberately finite-window and scalar. It does not
require a uniform positive denominator over all growing windows; if
denominators decay with loop area, the fifth clause is the correct place to
ask whether loop/readout errors decay fast enough relative to that
denominator and to the physical reserve.

### Theorem 4.6I.43f: `AYM-CONF-LMOD-ACT-SYM` Proves `AYM-CONF-LMOD-SYM`

If `AYM-CONF-LMOD-ACT-SYM` holds, then `AYM-CONF-LMOD-SYM` holds.

Proof.

Clause 1 is exactly the continuum slot-denominator certificate required by
clause 1 of `AYM-CONF-LMOD-SYM`. Clause 2 is the finite-stage denominator
transport certificate. In particular, for all `alpha>=alpha_den(j)` and all
`L in Slot(D_CR,j)`,

```math
\mathcal W_{\rho,\alpha}(L)
\ge
\mathcal W_\rho(L)-\varepsilon_{{\rm slot},j}(\alpha)
\ge
\underline{\kappa}_j+\rho_j-\rho_j
=
\underline{\kappa}_j
>
0.
```

Thus every finite-stage Creutz-slot denominator used by the logarithmic
readout is positive and separated from zero by the declared scalar margin.
Clause 3 is the loop-modulus decomposition and eventual upper bound. Clause
4 is the readout-error decomposition and eventual upper bound. Define

```math
\alpha_L(j)
=
\max\{\alpha_{{\rm den}}(j),\alpha_{{\rm loop}}(j),
\alpha_{{\rm read}}(j)\}.
```

Clause 5 is the strict reserve comparison required by
`AYM-CONF-LMOD-SYM`. Therefore every clause of `AYM-CONF-LMOD-SYM` holds.
`square`

### Definition 4.6I.43g: Actual Loop-Modulus Tail Export `AYM-CONF-LMOD-ACT-TAIL`

`AYM-CONF-LMOD-ACT-TAIL` is the stronger actual-tail package that proves
`AYM-CONF-LMOD-TAIL`. It holds when there is an index `J_L^{act}` and
constants

```math
s_L>0,
\quad
\kappa_L>0,
\quad
e_L\ge0,
\quad
w_L\ge0
```

such that:

1. `AYM-CONF-LMOD-ACT-SYM` is verified directly for every cofinal
   `j<J_L^{act}`;
2. for every cofinal `j>=J_L^{act}`, clauses 1--4 of
   `AYM-CONF-LMOD-ACT-SYM` hold with one declared tail rule and selectors
   `alpha_den(j)`, `alpha_loop(j)`, and `alpha_read(j)`;
3. for every cofinal `j>=J_L^{act}`,

   ```math
   {\underline{S}_{15,j}\over\ell_j^2}
   \ge
   s_L,
   \quad
   \underline{\kappa}_j\ge\kappa_L,
   \quad
   {\overline{E}_j\over\ell_j^2}\le e_L,
   \quad
   {4\overline{\omega}_j
   \over
   \underline{\kappa}_j\ell_j^2}
   \le
   w_L;
   ```

4. the actual tail margin is strict:

   ```math
   \max\{e_L,w_L\}
   <
   {s_L\over2}.
   ```

This tail export is intentionally stronger than the finite-window source.
It is appropriate only if the actual tower supplies a uniform positive
Creutz-slot denominator on the cofinal tail, or if the chosen normalized
records have been renormalized so that such a denominator is available.

### Theorem 4.6I.43h: `AYM-CONF-LMOD-ACT-TAIL` Proves `AYM-CONF-LMOD-TAIL`

If `AYM-CONF-LMOD-ACT-TAIL` holds, then `AYM-CONF-LMOD-TAIL` holds.

Proof.

For `j<J_L^{act}`, clause 1 gives `AYM-CONF-LMOD-ACT-SYM`; Theorem
4.6I.43f gives `AYM-CONF-LMOD-SYM`, which is the finite-prefix clause of
`AYM-CONF-LMOD-TAIL`.

For `j>=J_L^{act}`, clauses 2 and 3 supply the source clauses 1--4 of
`AYM-CONF-LMOD-SYM` and the normalized reserve, denominator, readout, and
loop-modulus bounds required by `AYM-CONF-LMOD-TAIL`. Clause 4 is exactly
the strict tail margin

```math
\max\{e_L,w_L\}
<
{s_L\over2}.
```

Thus every clause of `AYM-CONF-LMOD-TAIL` holds. `square`

### Corollary 4.6I.43i: Actual Loop-Modulus Closure

If `AYM-CONF-LMOD-ACT-SYM` holds, then

```text
AYM-CONF-LMOD-ACT-SYM
=> AYM-CONF-LMOD-SYM
=> AYM-CONF-LMOD-CALC
=> AYM-CONF-LMOD-SRC
=> AYM-CONF-LMOD.
```

If the stronger `AYM-CONF-LMOD-ACT-TAIL` holds, then

```text
AYM-CONF-LMOD-ACT-TAIL
=> AYM-CONF-LMOD-TAIL
=> AYM-CONF-LMOD-CALC
=> AYM-CONF-LMOD-SRC
=> AYM-CONF-LMOD.
```

Thus positive Creutz-slot denominators and small loop/readout errors are
reduced to the actual scalar estimates in Definitions 4.6I.43e and
4.6I.43g.

### Definition 4.6I.43j: Real-Constant Loop-Modulus Tail Ledger `AYM-CONF-LMOD-RC-TAIL`

`AYM-CONF-LMOD-RC-TAIL` is the explicit real-constant attempt to prove
`AYM-CONF-LMOD-ACT-TAIL`. It holds when there is a cofinal index
`J_L^{rc}` and constants

```math
s_L>0,
\quad
p_L>0,
\quad
e_{{\rm den},L}\ge0,
\quad
\rho_L>0,
\quad
\kappa_L>0,
\quad
e_L\ge0,
\quad
\omega_L\ge0,
\quad
w_L\ge0
```

such that the following statements hold.

1. The finite prefix is checked directly: `AYM-CONF-LMOD-ACT-SYM` holds for
   every cofinal `j<J_L^{rc}`.
2. For every cofinal `j>=J_L^{rc}`, the normalized reserve satisfies

   ```math
   {\underline{S}_{15,j}\over\ell_j^2}\ge s_L.
   ```

3. For every cofinal `j>=J_L^{rc}` and every slot loop
   `L in Slot(D_CR,j)`, the continuum denominator satisfies

   ```math
   \mathcal W_\rho(L)
   \ge
   p_L-e_{{\rm den},L}
   \ge
   \kappa_L+\rho_L.
   ```

4. For every cofinal `j>=J_L^{rc}`, the finite-stage denominator transport
   has a selector `alpha_den(j)` such that, for all `alpha>=alpha_den(j)`,

   ```math
   \sup_{L\in{\rm Slot}(D_{{\rm CR},j})}
   \left|
   \mathcal W_{\rho,\alpha}(L)-\mathcal W_\rho(L)
   \right|
   \le
   \varepsilon_{{\rm slot},j}(\alpha)
   \le
   \rho_L.
   ```

5. For every cofinal `j>=J_L^{rc}`, Paper-16/Paper-12 loop-continuity and
   readout estimates export selectors `alpha_loop(j)` and `alpha_read(j)`
   with

   ```math
   \overline{E}_j\le e_L\ell_j^2,
   \quad
   \overline{\omega}_j\le \omega_L\ell_j^2,
   \quad
   {4\omega_L\over\kappa_L}\le w_L.
   ```

6. The tail loop-modulus margin is strict:

   ```math
   \max\{e_L,w_L\}< {s_L\over2}.
   ```

The constants are raw denominator constants unless the record has been
explicitly normalized or renormalized before entering the slot family. A
positive `kappa_L` is therefore a substantive physical or record-design
input, not a consequence of pointwise finite-window positivity.

### Theorem 4.6I.43k: Real-Constant Loop-Modulus Tail Proves `AYM-CONF-LMOD-ACT-TAIL`

If `AYM-CONF-LMOD-RC-TAIL` holds, then `AYM-CONF-LMOD-ACT-TAIL` holds.

Proof.

The finite-prefix clause of `AYM-CONF-LMOD-RC-TAIL` is clause 1 of
`AYM-CONF-LMOD-ACT-TAIL`.

For `j>=J_L^{rc}`, define the tail constants for
`AYM-CONF-LMOD-ACT-TAIL` to be the constants in Definition 4.6I.43j.
Clause 2 gives the normalized reserve lower bound. Clause 3 gives the
continuum slot-denominator export with

```math
\underline{\kappa}_j:=\kappa_L,
\quad
\rho_j:=\rho_L,
\quad
p_{{\rm slot},j}:=p_L,
\quad
\overline e_{{\rm den},j}:=e_{{\rm den},L}.
```

Clause 4 gives the finite-stage denominator transport. In particular, for
`alpha>=alpha_den(j)` and every `L in Slot(D_CR,j)`,

```math
\mathcal W_{\rho,\alpha}(L)
\ge
\mathcal W_\rho(L)-\varepsilon_{{\rm slot},j}(\alpha)
\ge
\kappa_L+\rho_L-\rho_L
=
\kappa_L
>
0.
```

Clause 5 supplies the loop-modulus and readout tail bounds:

```math
{\overline{E}_j\over\ell_j^2}\le e_L,
\quad
{4\overline{\omega}_j\over\underline{\kappa}_j\ell_j^2}
\le
{4\omega_L\over\kappa_L}
\le
w_L.
```

Clause 6 is the strict tail margin. Therefore every clause of
`AYM-CONF-LMOD-ACT-TAIL` holds. `square`

### Theorem 4.6I.43l: Raw Denominator Collapse Falsifies `AYM-CONF-LMOD-ACT-TAIL`

Suppose that the cofinal slot schedule contains a raw Wilson-loop slot
`L_j in Slot(D_CR,j)` with continuum expectation bounded above by a sequence
`U_j` satisfying

```math
0\le \mathcal W_\rho(L_j)\le U_j,
\quad
U_j\to0.
```

Then no positive constant `kappa_L>0` can satisfy clause 3 of
`AYM-CONF-LMOD-ACT-TAIL` on that raw slot schedule. Consequently the raw
absolute tail version of `AYM-CONF-LMOD-ACT-TAIL` is falsified.

Proof.

If `AYM-CONF-LMOD-ACT-TAIL` held, then for every sufficiently large cofinal
`j`,

```math
\mathcal W_\rho(L_j)
\ge
\underline{\kappa}_j+\rho_j
\ge
\kappa_L
>
0.
```

But `U_j->0`, so for that same positive `kappa_L` there is a cofinal
`j` with `U_j<kappa_L`. Hence

```math
\mathcal W_\rho(L_j)\le U_j<\kappa_L,
```

contradicting the required lower bound. Thus no positive cofinal
denominator constant can exist on the raw schedule. `square`

### Corollary 4.6I.43m: Area-Decaying Raw Wilson Loops Force Finite-Window Or Normalized LMOD

Assume the raw slot schedule contains loops with area `A_j` and perimeter
`P_j` such that `A_j->infinity` and a same-ledger upper area envelope holds:

```math
0\le \mathcal W_\rho(L_j)
\le
C\exp[-\sigma A_j+K P_j+K_0],
\quad
\sigma>0.
```

If `sigma A_j-KP_j-K_0-log C -> infinity`, then
`AYM-CONF-LMOD-ACT-TAIL` fails on the raw slot schedule.

Proof.

The displayed upper envelope has right-hand side tending to zero. Apply
Theorem 4.6I.43l with

```math
U_j=C\exp[-\sigma A_j+K P_j+K_0].
```

`square`

### Corollary 4.6I.43n: Loop-Modulus Tail Status

The real-constant proof route for `AYM-CONF-LMOD-ACT-TAIL` is:

```text
uniform positive raw or normalized slot denominator kappa_L>0
+ normalized reserve S_15,j/ell_j^2 >= s_L
+ finite-stage slot transport <= rho_L
+ normalized readout and loop-modulus errors <= e_L,w_L
+ max{e_L,w_L}<s_L/2
=> AYM-CONF-LMOD-RC-TAIL
=> AYM-CONF-LMOD-ACT-TAIL.
```

The raw growing-loop branch gives the opposite result:

```text
some slot Wilson loop W(L_j) -> 0
=> no positive cofinal kappa_L
=> raw absolute AYM-CONF-LMOD-ACT-TAIL fails.
```

Therefore the honest default route for raw cofinal Wilson-loop slots is
finite-window `AYM-CONF-LMOD-ACT-SYM`. The tail route is available only for
local slot schedules, denominator-renormalized records, or normalized Creutz
readouts whose denominators are proved uniformly positive after
renormalization.

### Definition 4.6I.43o: Loop-Modulus Constant Attack `AYM-CONF-LMOD-CONST-ATTACK`

`AYM-CONF-LMOD-CONST-ATTACK` is the concrete step-4 computation after
`AYM-CONF-TOWER-FRZ`, `AYM-CONF-LAWWIN-AUDIT`, and
`AYM-CONF-RES-ATTACK`. For each cofinal window `D_CR,j`, let

```math
{\rm Slot}_j:={\rm Slot}(D_{{\rm CR},j})
```

be the finite set of Wilson-loop records appearing in the four Creutz slots.
The attack computes the following scalar constants on the frozen tower.

1. A certified continuum slot lower bound

   ```math
   K_j^{{\rm slot}}
   :=
   p_{{\rm slot},j}
   -\overline e_{{\rm den},j}
   \le
   \inf_{L\in{\rm Slot}_j}\mathcal W_\rho(L).
   ```

2. A finite-stage denominator transport allowance `rho_j` and denominator
   lower bound

   ```math
   0<\rho_j<K_j^{{\rm slot}},
   \quad
   \underline{\kappa}_j
   :=
   K_j^{{\rm slot}}-\rho_j
   >
   0,
   ```

   with selector `alpha_den(j)` such that, for all
   `alpha>=alpha_den(j)`,

   ```math
   \sup_{L\in{\rm Slot}_j}
   |\mathcal W_{\rho,\alpha}(L)-\mathcal W_\rho(L)|
   \le
   \rho_j.
   ```

3. A loop-continuity bound `overline omega_j` and selector
   `alpha_loop(j)` such that, eventually,

   ```math
   \omega_{{\rm CR},j}(\alpha)
   \le
   \overline{\omega}_j.
   ```

4. A readout-error bound `overline E_j` and selector `alpha_read(j)` such
   that, eventually,

   ```math
   E_j^{bd}(\alpha)
   \le
   \overline{E}_j.
   ```

5. The required normalized loop-modulus debit

   ```math
   \delta_{{\rm req},j}
   :=
   \max\left\{
   \frac{\overline{E}_j}{\ell_j^2},
   \frac{4\overline{\omega}_j}
   {\underline{\kappa}_j\ell_j^2}
   \right\},
   ```

   and the reserve allowance

   ```math
   \delta_{{\rm max},j}
   :=
   \frac{\underline{S}_{15,j}}{2\ell_j^2}.
   ```

The finite-window loop-modulus constants pass at `j` when

```math
K_j^{{\rm slot}}>0,
\quad
\delta_{{\rm req},j}<\delta_{{\rm max},j}.
```

In that case choose any certified

```math
\overline{\delta}_j
\quad
\text{with}
\quad
\delta_{{\rm req},j}
\le
\overline{\delta}_j
<
\delta_{{\rm max},j}.
```

The attack also records the loop-debited rate reserve

```math
q_j^{{\rm LMOD}}
:=
\frac{\underline{S}_{15,j}
-2\overline{\delta}_j\ell_j^2}{\ell_j}.
```

### Theorem 4.6I.43p: Finite-Window Loop-Modulus Constants Prove `AYM-CONF-LMOD-ACT-SYM`

Assume `AYM-CONF-LMOD-CONST-ATTACK` and suppose the finite-window
loop-modulus constants pass at a cofinal `j`. Then
`AYM-CONF-LMOD-ACT-SYM` holds at that `j`.

Proof.

The certified lower bound `K_j^{slot}` gives

```math
\inf_{L\in{\rm Slot}_j}\mathcal W_\rho(L)
\ge
K_j^{{\rm slot}}
=
\underline{\kappa}_j+\rho_j.
```

This is the continuum slot-denominator export in clause 1 of
`AYM-CONF-LMOD-ACT-SYM`. The selector `alpha_den(j)` and the transport
bound by `rho_j` give clause 2. The loop-continuity and readout selectors
give clauses 3 and 4.

Finally, `delta_req,j<delta_max,j` means

```math
\max\left\{
\frac{\overline{E}_j}{\ell_j^2},
\frac{4\overline{\omega}_j}
{\underline{\kappa}_j\ell_j^2}
\right\}
<
\frac{\underline{S}_{15,j}}{2\ell_j^2},
```

which is clause 5. Therefore `AYM-CONF-LMOD-ACT-SYM` holds at the window.
`square`

### Definition 4.6I.43q: Loop-Modulus Constant Outcomes

Running `AYM-CONF-LMOD-CONST-ATTACK` on the frozen tower has four possible
outcomes.

1. **Finite-window LMOD success:** every cofinal `j` has
   `K_j^{slot}>0` and `delta_req,j<delta_max,j`. Then
   `AYM-CONF-LMOD-ACT-SYM` holds for every cofinal `j`.
2. **Uniform-tail LMOD success:** there are constants

   ```math
   s_L>0,
   \quad
   \kappa_L>0,
   \quad
   e_L\ge0,
   \quad
   w_L\ge0
   ```

   such that, on a cofinal tail,

   ```math
   \frac{\underline{S}_{15,j}}{\ell_j^2}\ge s_L,
   \quad
   \underline{\kappa}_j\ge\kappa_L,
   \quad
   \frac{\overline{E}_j}{\ell_j^2}\le e_L,
   \quad
   \frac{4\overline{\omega}_j}
   {\underline{\kappa}_j\ell_j^2}
   \le w_L,
   ```

   with

   ```math
   \max\{e_L,w_L\}<\frac{s_L}{2}.
   ```

   Then `AYM-CONF-LMOD-RC-TAIL` holds, hence
   `AYM-CONF-LMOD-ACT-TAIL`.
3. **Normalized Gamma survival:** raw tail denominators may collapse, so no
   uniform `kappa_L>0` exists, but finite-window selectors still give
   `overline delta_j` and

   ```math
   \inf_j q_j^{{\rm LMOD}}>0
   ```

   on the intended cofinal tail. This does not prove the raw absolute
   loop-modulus tail, but it supplies the loop-debited reserve `q_G>0` needed
   by `AYM-CONF-GAMMA-RC-TAIL(m_*)`.
4. **LMOD obstruction:** either some required finite-window
   `K_j^{slot}` is nonpositive, or every admissible choice of
   `overline delta_j` makes `q_j^{LMOD}` collapse to zero or become
   nonpositive on the cofinal tail.

### Theorem 4.6I.43r: Loop-Modulus Constant Attack Trichotomy

Assume the tower is frozen and the law/window and reserve attacks have been
run. Then:

1. finite-window LMOD success proves `AYM-CONF-LMOD-SRC`;
2. uniform-tail LMOD success proves `AYM-CONF-LMOD-ACT-TAIL`, hence
   `AYM-CONF-LMOD-SRC`;
3. normalized Gamma survival supplies the loop-modulus part of
   `AYM-CONF-GAMMA-RC-TAIL(m_*)`;
4. LMOD obstruction blocks the Paper-18 confinement proof at the
   loop-modulus source unless the slot schedule, normalization, or estimates
   are changed.

Proof.

Finite-window success gives `AYM-CONF-LMOD-ACT-SYM` for every cofinal `j` by
Theorem 4.6I.43p. Corollary 4.6I.43i then gives
`AYM-CONF-LMOD-SRC`.

Uniform-tail success is exactly the real-constant tail ledger of Definition
4.6I.43j, with finite prefix supplied by the finite-window branch. Theorem
4.6I.43k gives `AYM-CONF-LMOD-ACT-TAIL`, and Corollary 4.6I.43i gives
`AYM-CONF-LMOD-SRC`.

For normalized Gamma survival, the raw denominator tail may be impossible
by Theorem 4.6I.43l, but the Gamma tail only uses

```math
q_j
=
\frac{\underline{S}_{15,j}
-2\overline{\delta}_j\ell_j^2}{\ell_j}.
```

Thus a positive cofinal lower bound for `q_j^{LMOD}` supplies the `q_G>0`
input in `AYM-CONF-GAMMA-RC-TAIL(m_*)`.

For LMOD obstruction, either a finite scheduled window lacks positive
denominators, or the loop/readout debit consumes the reserve after every
admissible normalization. Then neither the finite-window source nor the
compact Gamma-tail input has been proved. This is a real loop-modulus
obstruction. `square`

### Definition 4.6I.44: Marked-Bridge Calculation `AYM-CONF-MARK-CALC`

`AYM-CONF-MARK-CALC` is the sharpened version of step 5. It consists of:

1. an explicit endpoint-closure algorithm generated from
   `AYM-CONF-WIN-SRC`;
2. constants `alpha_*>0` and finite `N_*` with
   `alpha_j>=alpha_*` and `N_cl,j<=N_*`;
3. local loss formulae for endpoint collars, tiling remainders,
   perimeter/cusp/counterterm transport, and projection losses, producing
   `epsilon_area,j<=overline epsilon_j`;
4. a marked connected-polymer import or proof on the enlarged endpoint
   battery giving `h_j^S<=overline h_j`,
   `lambda_mark,j^S<=overline lambda_j`, and
   `D_KP,j<=overline D_j`;
5. a character-tail estimate `sup_j eta_ch,j<1`;
6. an endpoint-record typing clause: charged or colored endpoint records are
   instruments used to define marked scalar loop records, not autonomous
   scalar Gamma observables, and all closure, loss, and KP constants are
   computed from the same pushed-forward law as `AYM-CONF-LAW`.

### Theorem 4.6I.45: `AYM-CONF-MARK-CALC` Proves `AYM-CONF-MARK-SRC`

If `AYM-CONF-MARK-CALC` holds, then `AYM-CONF-MARK-SRC` holds.

Proof.

Clauses 1--5 are the construction, geometry, local loss, marked KP, and
character-tail clauses required by Definition 4.6I.30. Clause 6 is the
same-ledger charged-record typing required for Barandes-aligned use of
colored endpoints. Thus `AYM-CONF-MARK-SRC` holds. `square`

### Definition 4.6I.45a: Symbolic/Numeric Marked-Bridge Verifier `AYM-CONF-MARK-SYM`

`AYM-CONF-MARK-SYM` is the symbolic or interval-arithmetic verifier for
`AYM-CONF-MARK-CALC`. It is read relative to the cofinal window scheduler
`AYM-CONF-WIN-SCHED` and the same whole-process ledger used by
`AYM-CONF-LAW-SRC`. For every cofinal battery `G_j`, it supplies the
following scalar and finite-record data.

1. A finite endpoint-closure rule

   ```math
   {\rm Cl}_j(S;O,P)
   =
   \{L_a(S;O,P)\}_{a=1}^{N_j(S;O,P)}
   ```

   such that every loop `L_a(S;O,P)` is either in the scheduled Creutz-slot
   record family or is assigned a named local loss in `MARK-LOSS_j`. The rule
   has local multiplicity

   ```math
   N_{{\rm cl},j}\le N_*<\infty.
   ```

2. A retained-area lower bound. There are constants `alpha_*>0`,
   `b_area,j>=0`, and `alpha_j>=alpha_*` such that

   ```math
   \sum_{a=1}^{N_j(S;O,P)}
   {\rm Area}(L_a(S;O,P))
   \ge
   \alpha_j\ell_j^2 |S|-b_{{\rm area},j}.
   ```

   Equivalently, `c_geom,j=alpha_j ell_j`. Endpoint collar diameters are
   bounded by a declared function of the finite endpoint supports of `O` and
   `P`, and all closure loops are declared `CONF-REC` records on the same
   tower.

3. A local marked-loss budget. The non-area factors satisfy

   ```math
   F_j(S;O,P)
   \le
   B_j(O,P)\exp[\epsilon_{{\rm area},j}|S|],
   ```

   with finite amplitudes `B_j(O,P)` and

   ```math
   \epsilon_{{\rm area},j}
   =
   \epsilon_{{\rm area0},j}
   +\epsilon_{{\rm tile},j}
   +\epsilon_{{\rm ctr},j}
   +\epsilon_{{\rm collar},j}
   +\epsilon_{{\rm proj},j}
   \le
   \overline{\epsilon}_j.
   ```

   Here `epsilon_proj,j` is allowed only for the finite-record projection
   loss not already counted in `epsilon_15_to_j`, `E_j^{bd}`, or
   `Delta_conf,j`.

4. A marked connected-polymer certificate on the endpoint-enlarged battery.
   It supplies finite constants

   ```math
   A_j^S,
   \quad
   C_{{\rm cum},j}^S,
   \quad
   h_j^S,
   \quad
   \lambda_{{\rm mark},j}^S,
   \quad
   0\le\eta_{{\rm ch},j}<1
   ```

   with

   ```math
   h_j^S\le\overline{h}_j,
   \quad
   \lambda_{{\rm mark},j}^S\le\overline{\lambda}_j,
   ```

   and

   ```math
   D_{{\rm KP},j}
   =
   \log
   {C_{{\rm cum},j}^S A_j^S+1-\eta_{{\rm ch},j}
   \over
   1-\eta_{{\rm ch},j}}
   \le
   \overline{D}_j.
   ```

5. A uniform character-tail margin:

   ```math
   \eta_{{\rm ch},j}\le\eta_*<1
   ```

   for all cofinal `j`.

6. A same-ledger and endpoint-typing certificate. All constants above are
   computed from the same pushed-forward law as `AYM-CONF-LAW-SRC`, and
   charged or colored endpoint records appear only as typed boundary
   instruments used to define marked scalar loop records.

All six clauses are operational. The marked hulls, endpoint collars, and
surface polymers are estimate devices for scalar records, not additional
configuration variables.

### Theorem 4.6I.45a.1: `AYM-CONF-MARK-SYM` Proves `AYM-CONF-MARK-CALC`

If `AYM-CONF-MARK-SYM` holds, then `AYM-CONF-MARK-CALC` holds.

Proof.

Clauses 1 and 2 give the explicit endpoint-closure algorithm, the positive
retained-area constant `alpha_j>=alpha_*>0`, and the finite multiplicity
bound `N_cl,j<=N_*`. They are the geometry clauses required by
`AYM-CONF-MARK-CALC`, and they also prove the corresponding `MARK-GEOM_j`
data.

Clause 3 gives the local loss formulae for endpoint collars, tiling
remainders, counterterm transport, and projection loss, with the bound
`epsilon_area,j<=overline epsilon_j`. Clause 4 gives the marked
connected-polymer import or proof and the bounds
`h_j^S<=overline h_j`, `lambda_mark,j^S<=overline lambda_j`, and
`D_KP,j<=overline D_j`. Clause 5 gives the required uniform
character-tail estimate. Clause 6 is exactly the endpoint-record typing and
same-ledger condition.

Therefore all six clauses of `AYM-CONF-MARK-CALC` hold. `square`

### Definition 4.6I.45b: Finite-Prefix And Tail Marked-Bridge Test `AYM-CONF-MARK-TAIL`

`AYM-CONF-MARK-TAIL` is a practical cofinal verifier for
`AYM-CONF-MARK-SYM`. It holds when there is an index `J_M` and tail
constants

```math
\alpha_M>0,
\quad
N_M<\infty,
\quad
\eta_M<1
```

such that:

1. `AYM-CONF-MARK-SYM` is verified directly for every cofinal `j<J_M`;
2. for every cofinal `j>=J_M`, the same endpoint-closure rule supplies
   `MARK-GEOM_j` with

   ```math
   \alpha_j\ge\alpha_M>0,
   \quad
   N_{{\rm cl},j}\le N_M<\infty;
   ```

3. for every cofinal `j>=J_M`, the same local loss rule supplies finite
   amplitudes and explicit bounds

   ```math
   \epsilon_{{\rm area},j}\le\overline{\epsilon}_j<\infty;
   ```

4. for every cofinal `j>=J_M`, the endpoint-enlarged marked KP proof or
   import supplies finite bounds

   ```math
   h_j^S\le\overline{h}_j,
   \quad
   \lambda_{{\rm mark},j}^S\le\overline{\lambda}_j,
   \quad
   D_{{\rm KP},j}\le\overline{D}_j<\infty;
   ```

5. for every cofinal `j>=J_M`,

   ```math
   \eta_{{\rm ch},j}\le\eta_M<1;
   ```

6. the tail rule uses one same-ledger endpoint typing convention: endpoint
   records are typed boundary instruments and all loop, loss, and KP
   constants are computed from the same pushed-forward law.

Unlike `AYM-CONF-LMOD-TAIL`, this tail test does not require a positive
rate margin. Its job is to prove finiteness and uniform protocol control for
the marked bridge. The rate margin is paid later by `AYM-CONF-GAMMA-CALC`.

### Theorem 4.6I.45b.1: `AYM-CONF-MARK-TAIL` Proves `AYM-CONF-MARK-CALC`

If `AYM-CONF-MARK-TAIL` holds, then `AYM-CONF-MARK-CALC` holds for every
cofinal `j`.

Proof.

For `j<J_M`, clause 1 gives `AYM-CONF-MARK-SYM`, hence
`AYM-CONF-MARK-CALC` by Theorem 4.6I.45a.1.

For `j>=J_M`, clauses 2--6 are exactly the six clauses of
`AYM-CONF-MARK-SYM`, with `alpha_*` replaced by the tail lower bound
`alpha_M`, `N_*` by `N_M`, and `eta_*` by `eta_M`. The required amplitudes
and bounds are finite by clauses 3 and 4. Therefore
`AYM-CONF-MARK-SYM` holds on the tail, and Theorem 4.6I.45a.1 gives
`AYM-CONF-MARK-CALC`. Thus the marked-bridge calculation holds for every
cofinal `j`. `square`

### Definition 4.6I.45c: Endpoint-Enlarged Marked KP Source Export `AYM-CONF-MARK-ACT-SYM`

`AYM-CONF-MARK-ACT-SYM` is the actual-trajectory source package intended to
prove `AYM-CONF-MARK-SYM`. For every cofinal endpoint battery `G_j`, it
supplies the following data on the same whole-process Wilson-loop law.

1. A finite endpoint-enlarged battery `B_j^S`. It contains:
   - the scheduled Creutz-window records touching `G_j`;
   - every endpoint record `O,P in G_j`;
   - every closure loop in `Cl_j(S;O,P)`;
   - every endpoint-collar, scalarization, counterterm, and projection record
     used by the local loss ledger;
   - the marked hull generators used in the endpoint-enlarged polymer proof.

   The battery is finite for each `j`, consists only of declared `CONF-REC`
   scalar records and typed endpoint instruments, and is obtained by pushing
   the same whole-process law used by `AYM-CONF-LAW-SRC`.

2. An endpoint closure and retained-area export. There are constants

   ```math
   \alpha_*>0,
   \quad
   N_*<\infty
   ```

   such that, for every cofinal `j`, every endpoint pair `O,P in G_j`, and
   every marked hull `S`,

   ```math
   {\rm Cl}_j(S;O,P)
   =
   \{L_a(S;O,P)\}_{a=1}^{N_j(S;O,P)},
   \quad
   N_{{\rm cl},j}\le N_*,
   ```

   and

   ```math
   \sum_{a=1}^{N_j(S;O,P)}
   {\rm Area}(L_a(S;O,P))
   \ge
   \alpha_j\ell_j^2 |S|-b_{{\rm area},j},
   \quad
   \alpha_j\ge\alpha_*.
   ```

   Endpoint collars have diameters bounded by declared functions of the
   finite endpoint supports of `O` and `P`.

3. A same-ledger local loss export. The non-area endpoint and closure factors
   obey

   ```math
   F_j(S;O,P)
   \le
   B_j(O,P)\exp[\epsilon_{{\rm area},j}|S|],
   ```

   where `B_j(O,P)<infinity` and

   ```math
   \epsilon_{{\rm area},j}
   =
   \epsilon_{{\rm area0},j}
   +\epsilon_{{\rm tile},j}
   +\epsilon_{{\rm ctr},j}
   +\epsilon_{{\rm collar},j}
   +\epsilon_{{\rm proj},j}
   \le
   \overline{\epsilon}_j.
   ```

   Every term is entered once in the confinement debit ledger.

4. An endpoint-enlarged Paper-14/Paper-15 KP import. On `B_j^S`, Paper 14
   supplies the finite-block entry package `FBE_j^S`, and Paper 15 supplies
   a positive endpoint-enlarged numerical certificate `nCPSC_j^S`. The
   endpoint enlargement means that the Paper-15 generator battery already
   includes the endpoint records, closure loops, and collar records listed in
   clause 1. The import exports finite constants

   ```math
   A_j^S,
   \quad
   C_{{\rm cum},j}^S,
   \quad
   h_j^S,
   \quad
   r_j^S,
   \quad
   \eta_{{\rm ch},j},
   \quad
   \lambda_{{\rm mark},j}^S
   ```

   with

   ```math
   h_j^S\le\overline{h}_j,
   \quad
   \lambda_{{\rm mark},j}^S\le\overline{\lambda}_j.
   ```

   The marked KP threshold is then

   ```math
   D_{{\rm KP},j}
   =
   \log
   {C_{{\rm cum},j}^S A_j^S+1-\eta_{{\rm ch},j}
   \over
   1-\eta_{{\rm ch},j}}
   \le
   \overline{D}_j
   <
   \infty.
   ```

5. A uniform character-tail margin:

   ```math
   \eta_{{\rm ch},j}\le\eta_*<1
   ```

   for all cofinal `j`.

6. A clean endpoint ontology clause. Colored endpoint records are typed
   boundary instruments used to generate marked scalar records. They are not
   autonomous scalar Gamma observables, and no gauge-fixed endpoint field or
   flux-tube object is added to the ontology.

This is the source-level endpoint-enlarged KP stability statement. It does
not assert a new Markov property for endpoint histories; it asserts that the
declared endpoint-enlarged finite record batteries have the same
connected-polymer estimates as the unmarked Paper-15 batteries, with the
endpoint marking loss debited once.

### Theorem 4.6I.45d: `AYM-CONF-MARK-ACT-SYM` Proves `AYM-CONF-MARK-SYM`

If `AYM-CONF-MARK-ACT-SYM` holds, then `AYM-CONF-MARK-SYM` holds.

Proof.

Clause 1 makes all records used by the endpoint bridge part of one finite
same-ledger battery. Clauses 2 and 3 give the endpoint-closure rule,
retained-area bound, finite local multiplicity, finite endpoint amplitudes,
and local marked-loss budget required by clauses 1--3 of
`AYM-CONF-MARK-SYM`.

Clause 4 imports the endpoint-enlarged connected-polymer estimate. Paper
14's `FBE_j^S` gives the exact finite-block pushed-forward record law on
`B_j^S`. Positive Paper-15 `nCPSC_j^S` gives connected-polymer KP control on
that same battery. Because `B_j^S` already includes the endpoint records,
closure loops, and collar records, the KP estimate applies to the marked
endpoint hulls rather than only to the unmarked Creutz sub-battery.

The endpoint marking ledger contributes only the displayed
`lambda_mark,j^S` term. The character-tail denominator is separated from
zero by clause 5:

```math
1-\eta_{{\rm ch},j}
\ge
1-\eta_*
>
0.
```

Hence the logarithmic threshold `D_KP,j` is finite and is bounded by
`overline D_j`. This is exactly clause 4 of `AYM-CONF-MARK-SYM`, while
clause 5 gives the uniform character-tail margin and clause 6 gives the
same-ledger endpoint typing. Therefore `AYM-CONF-MARK-SYM` holds. `square`

### Definition 4.6I.45e: Actual Endpoint-Enlarged Marked KP Tail Export `AYM-CONF-MARK-ACT-TAIL`

`AYM-CONF-MARK-ACT-TAIL` is the stronger actual-tail source package that
proves `AYM-CONF-MARK-TAIL`. It holds when there is an index `J_M^{act}`
and constants

```math
\alpha_M>0,
\quad
N_M<\infty,
\quad
\eta_M<1
```

such that:

1. `AYM-CONF-MARK-ACT-SYM` is verified directly for every cofinal
   `j<J_M^{act}`;
2. for every cofinal `j>=J_M^{act}`, clauses 1--3 of
   `AYM-CONF-MARK-ACT-SYM` hold with one tail endpoint-closure and loss
   rule, with

   ```math
   \alpha_j\ge\alpha_M,
   \quad
   N_{{\rm cl},j}\le N_M;
   ```

3. for every cofinal `j>=J_M^{act}`, the endpoint-enlarged Paper-14/Paper-15
   import of clause 4 of `AYM-CONF-MARK-ACT-SYM` holds and exports finite
   bounds

   ```math
   h_j^S\le\overline{h}_j,
   \quad
   \lambda_{{\rm mark},j}^S\le\overline{\lambda}_j,
   \quad
   D_{{\rm KP},j}\le\overline{D}_j<\infty;
   ```

4. for every cofinal `j>=J_M^{act}`,

   ```math
   \eta_{{\rm ch},j}\le\eta_M<1;
   ```

5. the tail uses one same-ledger endpoint typing convention and debits every
   endpoint, counterterm, projection, and character-tail loss exactly once.

This tail export is weaker than a mass-gap or confinement estimate. It asks
only for stable endpoint-enlarged KP inputs and finite protocol constants
on the cofinal tail.

### Theorem 4.6I.45f: `AYM-CONF-MARK-ACT-TAIL` Proves `AYM-CONF-MARK-TAIL`

If `AYM-CONF-MARK-ACT-TAIL` holds, then `AYM-CONF-MARK-TAIL` holds.

Proof.

For `j<J_M^{act}`, clause 1 gives `AYM-CONF-MARK-ACT-SYM`; Theorem
4.6I.45d gives `AYM-CONF-MARK-SYM`, which is the finite-prefix clause of
`AYM-CONF-MARK-TAIL`.

For `j>=J_M^{act}`, clause 2 gives the tail `MARK-GEOM_j` and local loss
rules with `alpha_M` and `N_M`. Clause 3 gives the endpoint-enlarged marked
KP bounds and finite `D_KP,j`. Clause 4 gives the uniform character-tail
margin. Clause 5 gives the required same-ledger endpoint typing. These are
exactly clauses 2--6 of `AYM-CONF-MARK-TAIL`. Therefore
`AYM-CONF-MARK-TAIL` holds. `square`

### Corollary 4.6I.45g: Actual Marked-Bridge Closure

If `AYM-CONF-MARK-ACT-SYM` holds, then

```text
AYM-CONF-MARK-ACT-SYM
=> AYM-CONF-MARK-SYM
=> AYM-CONF-MARK-CALC
=> AYM-CONF-MARK-SRC
=> AYM-CONF-MARK.
```

If the stronger `AYM-CONF-MARK-ACT-TAIL` holds, then

```text
AYM-CONF-MARK-ACT-TAIL
=> AYM-CONF-MARK-TAIL
=> AYM-CONF-MARK-CALC
=> AYM-CONF-MARK-SRC
=> AYM-CONF-MARK.
```

Thus endpoint-enlarged marked KP stability is reduced to finite
endpoint-enlarged `FBE_j^S`, positive `nCPSC_j^S`, a finite endpoint-marking
ledger, and a uniform character-tail margin below one.

### Definition 4.6I.45h: Real-Constant Endpoint-Marked Tail Ledger `AYM-CONF-MARK-RC-TAIL`

`AYM-CONF-MARK-RC-TAIL` is the explicit real-constant attempt to prove
`AYM-CONF-MARK-ACT-TAIL`. It holds when there is a cofinal index
`J_M^{rc}` and constants

```math
\alpha_M>0,
\quad
N_M<\infty,
\quad
\eta_M<1
```

such that the following statements hold.

1. The finite prefix is checked directly: `AYM-CONF-MARK-ACT-SYM` holds for
   every cofinal `j<J_M^{rc}`.
2. For every cofinal `j>=J_M^{rc}`, a single endpoint-enlarged battery
   builder produces a finite same-ledger battery `B_j^S` containing:
   - the scheduled Creutz-window records touching `G_j`;
   - every endpoint record `O,P in G_j`;
   - every closure loop in `Cl_j(S;O,P)`;
   - every endpoint-collar, scalarization, counterterm, and projection record
     used by the local loss ledger;
   - the marked hull generators used in the endpoint-enlarged polymer proof.
3. For every cofinal `j>=J_M^{rc}`, the same endpoint-closure rule gives

   ```math
   \alpha_j\ge\alpha_M,
   \quad
   N_{{\rm cl},j}\le N_M,
   ```

   and the same local loss rule gives finite amplitudes `B_j(O,P)` and finite
   bounds

   ```math
   \epsilon_{{\rm area},j}\le\overline{\epsilon}_j<\infty.
   ```

4. For every cofinal `j>=J_M^{rc}`, Paper 14 proves the endpoint-enlarged
   finite-block entry package

   ```text
   FBE_j^S
   ```

   on `B_j^S`.
5. For every cofinal `j>=J_M^{rc}`, Paper 15 proves a positive
   endpoint-enlarged numerical certificate

   ```text
   nCPSC_j^S
   ```

   on the same finite battery `B_j^S`. The exported constants are finite:

   ```math
   A_j^S<\infty,
   \quad
   C_{{\rm cum},j}^S<\infty,
   \quad
   h_j^S<\infty,
   \quad
   r_j^S<\infty,
   \quad
   0\le\eta_{{\rm ch},j}<1.
   ```

6. The character-tail margin is uniform on the cofinal tail:

   ```math
   \eta_{{\rm ch},j}\le\eta_M<1.
   ```

7. The endpoint-marking ledger is finite and same-ledger:

   ```math
   \lambda_{{\rm mark},j}^S\le\overline{\lambda}_j<\infty,
   ```

   every endpoint collar amplitude is finite, every endpoint/counterterm/
   projection loss is debited once, and colored endpoints are typed boundary
   instruments used only to define marked scalar records.

Define

```math
\overline{h}_j:=h_j^S,
\quad
\overline{D}_j
:=
\log
\frac{C_{{\rm cum},j}^S A_j^S+1-\eta_{{\rm ch},j}}
{1-\eta_{{\rm ch},j}}.
```

Since `eta_ch,j<=eta_M<1`, the denominator is uniformly separated from
zero and each `overline D_j` is finite.

### Theorem 4.6I.45i: `AYM-CONF-MARK-RC-TAIL` Proves `AYM-CONF-MARK-ACT-TAIL`

If `AYM-CONF-MARK-RC-TAIL` holds, then `AYM-CONF-MARK-ACT-TAIL` holds.

Proof.

The finite-prefix clause of `AYM-CONF-MARK-RC-TAIL` is clause 1 of
`AYM-CONF-MARK-ACT-TAIL`.

For `j>=J_M^{rc}`, clauses 2 and 3 give clauses 1--3 of
`AYM-CONF-MARK-ACT-SYM` with one tail endpoint-closure and loss rule, and
with the uniform bounds `alpha_j>=alpha_M` and `N_cl,j<=N_M`.

Clause 4 gives the endpoint-enlarged Paper-14 `FBE_j^S` package on the
same finite battery. Clause 5 gives positive endpoint-enlarged Paper-15
`nCPSC_j^S`. By Paper 15 Theorem 12.1B, positive `nCPSC_j^S` gives the
connected-polymer surface certificate on `B_j^S`; because `B_j^S` includes
the endpoint records, closure loops, collar records, and marked hull
generators, the certificate applies to the endpoint-enlarged marked polymer
family used by Paper 18.

The exported constants `A_j^S`, `C_cum,j^S`, `h_j^S`, `r_j^S`, and
`eta_ch,j` are finite by clause 5. Clause 6 gives

```math
1-\eta_{{\rm ch},j}
\ge
1-\eta_M
>
0.
```

Therefore

```math
D_{{\rm KP},j}
=
\log
\frac{C_{{\rm cum},j}^S A_j^S+1-\eta_{{\rm ch},j}}
{1-\eta_{{\rm ch},j}}
\le
\overline{D}_j
<
\infty.
```

Clause 7 supplies finite endpoint marking and same-ledger endpoint typing.
These are exactly clauses 2--5 of `AYM-CONF-MARK-ACT-TAIL`. Hence
`AYM-CONF-MARK-ACT-TAIL` holds. `square`

### Theorem 4.6I.45j: Pointwise Character-Tail Positivity Does Not Prove The Tail

Assume that endpoint-enlarged `FBE_j^S` and positive `nCPSC_j^S` hold for
every cofinal `j`, and that

```math
0\le\eta_{{\rm ch},j}<1
```

for every cofinal `j`, but

```math
\sup_j\eta_{{\rm ch},j}=1.
```

Then these pointwise hypotheses do not prove `AYM-CONF-MARK-ACT-TAIL`.
Indeed, if a subsequence has `eta_ch,j_k -> 1`, clause 4 of
`AYM-CONF-MARK-ACT-TAIL` fails for every proposed `eta_M<1`.

Proof.

`AYM-CONF-MARK-ACT-TAIL` requires a single constant `eta_M<1` such that

```math
\eta_{{\rm ch},j}\le\eta_M
```

for every cofinal tail index. If `sup_j eta_ch,j=1`, then for every
`eta_M<1` there is a cofinal index `j` with `eta_ch,j>eta_M`. Thus no such
tail constant exists. The pointwise inequalities `eta_ch,j<1` give finite
battery estimates, but they do not give the cofinal tail theorem. `square`

### Corollary 4.6I.45k: Marked-Tail Status

The real-constant proof route for `AYM-CONF-MARK-ACT-TAIL` is:

```text
same-ledger endpoint-enlarged batteries B_j^S
+ one endpoint closure/loss rule with alpha_j>=alpha_M and N_cl,j<=N_M
+ Paper-14 FBE_j^S on B_j^S
+ positive Paper-15 nCPSC_j^S on B_j^S
+ finite endpoint marking
+ eta_ch,j<=eta_M<1
=> AYM-CONF-MARK-RC-TAIL
=> AYM-CONF-MARK-ACT-TAIL.
```

The obstruction is equally sharp:

```text
eta_ch,j<1 pointwise but sup_j eta_ch,j=1
=> no uniform eta_M<1
=> AYM-CONF-MARK-ACT-TAIL is not proved.
```

Thus the endpoint-enlarged marked KP tail is a genuine cofinal stability
condition. Finite batteries remain legal one by one, but a Paper-18 tail
proof needs a uniform character-tail gap and one cofinal endpoint protocol.

### Definition 4.6I.45l: Marked-Bridge Constant Attack `AYM-CONF-MARK-CONST-ATTACK`

`AYM-CONF-MARK-CONST-ATTACK` is the concrete step-5 computation after the
tower, law/window, reserve, and loop-modulus attacks. For every cofinal
endpoint battery `G_j`, it computes the following finite-record data on the
frozen whole-process tower.

1. The endpoint-enlarged battery

   ```text
   B_j^S
   ```

   containing the scheduled Creutz-window records touching `G_j`, every
   endpoint record `O,P in G_j`, every closure loop in `Cl_j(S;O,P)`, every
   endpoint collar, scalarization, counterterm, projection record, and every
   marked hull generator used by the endpoint-enlarged polymer proof.

2. The finite geometry constants

   ```math
   \alpha_j>0,
   \quad
   N_{{\rm cl},j}<\infty,
   \quad
   b_{{\rm area},j}<\infty,
   ```

   where `alpha_j` is the retained-area conversion and `N_cl,j` is the
   endpoint-closure multiplicity.

3. The local marked-loss constants

   ```math
   \epsilon_{{\rm area},j}\le\overline{\epsilon}_j<\infty,
   \quad
   B_j(O,P)<\infty,
   ```

   with every endpoint, collar, counterterm, projection, and tiling loss
   debited exactly once.

4. The Paper-14/Paper-15 endpoint-enlarged KP inputs on the same battery:

   ```text
   FBE_j^S,
   positive nCPSC_j^S.
   ```

   The positive `nCPSC_j^S` exports finite constants

   ```math
   A_j^S,
   \quad
   C_{{\rm cum},j}^S,
   \quad
   h_j^S,
   \quad
   r_j^S,
   \quad
   \eta_{{\rm ch},j},
   \quad
   \lambda_{{\rm mark},j}^S.
   ```

5. The marked thresholds

   ```math
   0\le\eta_{{\rm ch},j}<1,
   ```

   ```math
   D_{{\rm KP},j}
   :=
   \log
   \frac{C_{{\rm cum},j}^S A_j^S+1-\eta_{{\rm ch},j}}
   {1-\eta_{{\rm ch},j}},
   ```

   and explicit upper bounds

   ```math
   h_j^S\le\overline{h}_j,
   \quad
   \lambda_{{\rm mark},j}^S\le\overline{\lambda}_j,
   \quad
   D_{{\rm KP},j}\le\overline{D}_j<\infty.
   ```

6. The marked debit entering the Gamma ledger:

   ```math
   \overline{L}_j^{{\rm mark}}
   :=
   \overline{\epsilon}_j
   +\overline{h}_j
   +\overline{\lambda}_j,
   ```

   ```math
   b_j^{{\rm MARK}}
   :=
   \frac{\overline{L}_j^{{\rm mark}}+\overline{D}_j}{2\ell_j}.
   ```

7. The endpoint ontology certificate: all endpoint records are typed
   boundary instruments used only to define marked scalar records, and all
   constants above are computed from the same pushed-forward law as
   `AYM-CONF-LAW-SRC`.

The finite-window marked constants pass at `j` when clauses 1--7 hold.

### Theorem 4.6I.45m: Finite-Window Marked Constants Prove `AYM-CONF-MARK-ACT-SYM`

Assume `AYM-CONF-MARK-CONST-ATTACK` and suppose the finite-window marked
constants pass at a cofinal `j`. Then `AYM-CONF-MARK-ACT-SYM` holds at
that `j`.

Proof.

Clause 1 is exactly the endpoint-enlarged finite battery required by clause
1 of `AYM-CONF-MARK-ACT-SYM`. Clause 2 gives the endpoint closure and
retained-area export. Clause 3 gives the same-ledger local loss export.
Clause 4 gives the endpoint-enlarged Paper-14 `FBE_j^S` package and positive
Paper-15 `nCPSC_j^S` on the same battery. Clause 5 gives the finite marked
KP threshold and the bounds `h_j^S<=overline h_j`,
`lambda_mark,j^S<=overline lambda_j`, and `D_KP,j<=overline D_j`.
Clause 7 is the endpoint ontology clause. Therefore every clause of
`AYM-CONF-MARK-ACT-SYM` holds at `j`. `square`

### Definition 4.6I.45n: Marked-Bridge Constant Outcomes

Running `AYM-CONF-MARK-CONST-ATTACK` on the frozen tower has four possible
outcomes.

1. **Finite-window MARK success:** every cofinal `j` passes the finite-window
   marked constants. Then `AYM-CONF-MARK-ACT-SYM` holds for every cofinal
   `j`.
2. **Uniform-tail MARK success:** there are constants

   ```math
   \alpha_M>0,
   \quad
   N_M<\infty,
   \quad
   \eta_M<1
   ```

   such that, on a cofinal tail,

   ```math
   \alpha_j\ge\alpha_M,
   \quad
   N_{{\rm cl},j}\le N_M,
   \quad
   \eta_{{\rm ch},j}\le\eta_M<1,
   ```

   and the same endpoint-closure/loss convention gives finite
   `overline epsilon_j`, `overline h_j`, `overline lambda_j`, and
   `overline D_j`. Then `AYM-CONF-MARK-RC-TAIL` holds, hence
   `AYM-CONF-MARK-ACT-TAIL`.
3. **Normalized Gamma survival:** finite-window marked constants pass, but
   no uniform tail constant `eta_M<1` is available. If nevertheless

   ```math
   \sup_j b_j^{{\rm MARK}}<\infty
   ```

   on the intended cofinal tail, then the marked bridge does not prove the
   raw marked tail theorem, but it supplies the marked debit part of
   `AYM-CONF-GAMMA-RC-TAIL(m_*)`.
4. **MARK obstruction:** some cofinal finite window lacks endpoint-enlarged
   `FBE_j^S`, positive `nCPSC_j^S`, finite endpoint marking, finite
   `D_KP,j`, or clean endpoint typing; or every admissible cofinal
   normalization has `b_j^{MARK}` unbounded.

### Theorem 4.6I.45o: Marked-Bridge Constant Attack Trichotomy

Assume the tower is frozen and the law/window, reserve, and loop-modulus
attacks have been run. Then:

1. finite-window MARK success proves `AYM-CONF-MARK-SRC`;
2. uniform-tail MARK success proves `AYM-CONF-MARK-ACT-TAIL`, hence
   `AYM-CONF-MARK-SRC`;
3. normalized Gamma survival supplies the marked/KP debit part of
   `AYM-CONF-GAMMA-RC-TAIL(m_*)`;
4. MARK obstruction blocks the Paper-18 confinement proof at the
   marked-bridge source unless the endpoint battery, endpoint protocol,
   polymer certificate, or normalization is changed.

Proof.

Finite-window MARK success gives `AYM-CONF-MARK-ACT-SYM` for every cofinal
`j` by Theorem 4.6I.45m. Corollary 4.6I.45g then gives
`AYM-CONF-MARK-SRC`.

Uniform-tail MARK success is exactly the real-constant marked tail ledger of
Definition 4.6I.45h, with finite prefix supplied by the finite-window
branch. Theorem 4.6I.45i gives `AYM-CONF-MARK-ACT-TAIL`, and Corollary
4.6I.45g gives `AYM-CONF-MARK-SRC`.

For normalized Gamma survival, the raw marked tail may be impossible by
Theorem 4.6I.45j if `sup_j eta_ch,j=1`. But the Gamma tail uses only the
normalized debit

```math
b_j
=
\frac{\overline{L}_j+\overline{D}_j}{2\ell_j}.
```

The computed `b_j^{MARK}` is exactly this marked/KP part of the debit.
Hence a finite cofinal upper bound for `b_j^{MARK}` supplies the marked
input `b_G<infty` used later by `AYM-CONF-GAMMA-RC-TAIL(m_*)`.

For MARK obstruction, either a finite endpoint-enlarged battery lacks one of
the legal marked KP inputs, or the marked/KP debit cannot be bounded in the
normalized Gamma ledger. Then neither the finite-window marked source nor
the compact Gamma-tail input has been proved. This is a real marked-bridge
obstruction. `square`

### Definition 4.6I.46: Gamma Calculation `AYM-CONF-GAMMA-CALC(m_*)`

`AYM-CONF-GAMMA-CALC(m_*)` is the explicit version of step 6. Assume
`AYM-CONF-RES-SRC`, `AYM-CONF-LMOD-CALC`, and
`AYM-CONF-MARK-CALC`. Define

```math
\overline{L}_j
=
\overline{\epsilon}_j
+\overline{h}_j
+\overline{\lambda}_j.
```

Choose explicit `overline delta_j` satisfying

```math
\overline{\delta}_j
\ge
\max\left\{
{\overline{E}_j\over\ell_j^2},
{4\overline{\omega}_j\over\underline{\kappa}_j\ell_j^2}
\right\}
```

and explicit `underline alpha_j`, `overline D_j`, and `overline Delta_j`
with

```math
\underline{\alpha}_j\le\alpha_j,
\quad
D_{{\rm KP},j}\le\overline{D}_j,
\quad
\Delta_{{\rm conf},j}\le\overline{\Delta}_j.
```

Set

```math
\underline{\Gamma}_j
=
\underline{\alpha}_j
\left(
\underline{S}_{15,j}
-2\overline{\delta}_j\ell_j^2
\right)
-\overline{L}_j
-\overline{D}_j.
```

The calculation closes when

```math
\underline{\Gamma}_j>0
```

for every cofinal `j` and

```math
\inf_j
\left[
{\underline{\Gamma}_j\over2\ell_j}
-\overline{\Delta}_j
\right]
\ge
2m_*
>
0.
```

This is the exact quantitative place where a cofinal tower of positive
finite batteries either becomes a physical confinement rate or degenerates
to zero.

### Theorem 4.6I.47: `AYM-CONF-GAMMA-CALC` Proves `AYM-CONF-GAMMA-LB`

If `AYM-CONF-GAMMA-CALC(m_*)` holds, then
`AYM-CONF-GAMMA-LB(m_*)` holds.

Proof.

The bounds on `overline delta_j`, `underline alpha_j`, `overline L_j`,
`overline D_j`, and `overline Delta_j` are exactly the termwise bounds
required by Definition 4.6I.32. The displayed definition of
`underline Gamma_j` is the same definition, and the two final inequalities
are the positivity and cofinal rate clauses of `AYM-CONF-GAMMA-LB(m_*)`.
`square`

### Definition 4.6I.47a: Symbolic/Numeric Gamma-Rate Verifier `AYM-CONF-GAMMA-SYM(m_*)`

`AYM-CONF-GAMMA-SYM(m_*)` is the symbolic or interval-arithmetic verifier
for `AYM-CONF-GAMMA-CALC(m_*)`. It assumes the reserve, loop-modulus, and
marked-bridge calculation data are already available on one common
whole-process ledger. For every cofinal `j`, it supplies the following
certified scalar quantities.

1. The marked local-loss bound is assembled as

   ```math
   \overline{L}_j
   =
   \overline{\epsilon}_j
   +\overline{h}_j
   +\overline{\lambda}_j.
   ```

2. The loop-modulus choice satisfies

   ```math
   \overline{\delta}_j
   \ge
   \max\left\{
   {\overline{E}_j\over\ell_j^2},
   {4\overline{\omega}_j\over\underline{\kappa}_j\ell_j^2}
   \right\}.
   ```

3. The retained-area, KP, and Paper-17 rate bounds satisfy

   ```math
   0<\underline{\alpha}_j\le\alpha_j,
   \quad
   0\le D_{{\rm KP},j}\le\overline{D}_j,
   \quad
   0\le\Delta_{{\rm conf},j}\le\overline{\Delta}_j.
   ```

4. Define the assembled lower margin

   ```math
   \underline{\Gamma}_j
   =
   \underline{\alpha}_j
   \left(
   \underline{S}_{15,j}
   -2\overline{\delta}_j\ell_j^2
   \right)
   -\overline{L}_j
   -\overline{D}_j
   ```

   and the normalized rate certificate

   ```math
   r_j
   =
   {\underline{\Gamma}_j\over2\ell_j}
   -\overline{\Delta}_j.
   ```

5. The final rate inequality is certified:

   ```math
   r_j\ge 2m_*
   ```

   for every cofinal `j`, with

   ```math
   m_*>0.
   ```

All inequalities are scalar record inequalities. A numerical implementation
must certify them by outward-rounded interval arithmetic; a symbolic
implementation must prove them on the declared parameter domain.

### Theorem 4.6I.47a.1: `AYM-CONF-GAMMA-SYM` Proves `AYM-CONF-GAMMA-CALC`

If `AYM-CONF-GAMMA-SYM(m_*)` holds, then
`AYM-CONF-GAMMA-CALC(m_*)` holds.

Proof.

Clauses 1--3 are exactly the assembly and termwise bounds required by
Definition 4.6I.46. Clause 4 defines the same `underline Gamma_j` as
`AYM-CONF-GAMMA-CALC`. Clause 5 gives

```math
{\underline{\Gamma}_j\over2\ell_j}
-\overline{\Delta}_j
\ge
2m_*
>
0
```

for every cofinal `j`. Since `overline Delta_j>=0` and `ell_j>0`, this also
implies `underline Gamma_j>0`. Taking the infimum over `j` gives

```math
\inf_j
\left[
{\underline{\Gamma}_j\over2\ell_j}
-\overline{\Delta}_j
\right]
\ge
2m_*
>
0.
```

Thus both closing inequalities in `AYM-CONF-GAMMA-CALC(m_*)` hold. `square`

### Definition 4.6I.47b: Finite-Prefix And Tail Gamma-Rate Test `AYM-CONF-GAMMA-TAIL(m_*)`

`AYM-CONF-GAMMA-TAIL(m_*)` is a practical verifier for the final cofinal
infimum. It holds when there is an index `J_G` and tail constants

```math
\alpha_G>0,
\quad
q_G>0,
\quad
b_G\ge0,
\quad
\Delta_G\ge0
```

such that:

1. `AYM-CONF-GAMMA-SYM(m_*)` is verified directly for every cofinal
   `j<J_G`;
2. for every cofinal `j>=J_G`, clauses 1--4 of
   `AYM-CONF-GAMMA-SYM(m_*)` hold with one declared tail rule;
3. for every cofinal `j>=J_G`, the normalized tail bounds satisfy

   ```math
   \underline{\alpha}_j\ge\alpha_G,
   ```

   ```math
   {\underline{S}_{15,j}
   -2\overline{\delta}_j\ell_j^2
   \over
   \ell_j}
   \ge
   q_G,
   ```

   ```math
   {\overline{L}_j+\overline{D}_j\over2\ell_j}
   \le
   b_G,
   \quad
   \overline{\Delta}_j\le\Delta_G;
   ```

4. the tail rate margin is positive:

   ```math
   {\alpha_Gq_G\over2}
   -b_G
   -\Delta_G
   \ge
   2m_*
   >
   0.
   ```

The quantity `q_G` is the surviving reserve per physical block length after
the loop-modulus debit. The constants `b_G` and `Delta_G` are, respectively,
the normalized marked/KP debit and the Paper-17 selected-rate debit. This
tail test is the exact place where cofinal positivity becomes a physical
nonzero rate rather than a family of finite positive batteries.

### Theorem 4.6I.47b.1: `AYM-CONF-GAMMA-TAIL` Proves `AYM-CONF-GAMMA-CALC`

If `AYM-CONF-GAMMA-TAIL(m_*)` holds, then
`AYM-CONF-GAMMA-CALC(m_*)` holds for every cofinal `j`.

Proof.

For `j<J_G`, clause 1 gives `AYM-CONF-GAMMA-SYM(m_*)`, hence
`AYM-CONF-GAMMA-CALC(m_*)` by Theorem 4.6I.47a.1.

For `j>=J_G`, clauses 2 and 3 give

```math
{\underline{\Gamma}_j\over2\ell_j}
-\overline{\Delta}_j
=
{\underline{\alpha}_j\over2}
{\underline{S}_{15,j}
-2\overline{\delta}_j\ell_j^2
\over
\ell_j}
-
{\overline{L}_j+\overline{D}_j\over2\ell_j}
-
\overline{\Delta}_j.
```

Using the tail lower and upper bounds,

```math
{\underline{\Gamma}_j\over2\ell_j}
-\overline{\Delta}_j
\ge
{\alpha_Gq_G\over2}
-b_G
-\Delta_G
\ge
2m_*
>
0.
```

Thus `underline Gamma_j>0` and the normalized rate inequality hold on the
tail. Combining the finite-prefix and tail estimates gives

```math
\inf_j
\left[
{\underline{\Gamma}_j\over2\ell_j}
-\overline{\Delta}_j
\right]
\ge
2m_*
>
0.
```

Therefore `AYM-CONF-GAMMA-CALC(m_*)` holds cofinally. `square`

### Definition 4.6I.47c: Actual Gamma-Rate Source Export `AYM-CONF-GAMMA-ACT-SYM(m_*)`

`AYM-CONF-GAMMA-ACT-SYM(m_*)` is the actual-trajectory source package that
proves `AYM-CONF-GAMMA-SYM(m_*)`. It is read after the actual reserve,
loop-modulus, and marked-bridge source packages have exported their scalar
constants on one whole-process ledger. For every cofinal `j`, it supplies
the following certified data.

1. The actual scalar inputs are available on the same ledger:

   ```math
   \underline{S}_{15,j},
   \quad
   \overline{E}_j,
   \quad
   \overline{\omega}_j,
   \quad
   \underline{\kappa}_j,
   \quad
   \overline{\epsilon}_j,
   \quad
   \overline{h}_j,
   \quad
   \overline{\lambda}_j,
   \quad
   \overline{D}_j,
   \quad
   \overline{\Delta}_j,
   \quad
   \ell_j.
   ```

   These are the outputs of the reserve, loop-modulus, marked-bridge, and
   Paper-17 physical-rate debit ledgers. No term may be imported from a
   different pushed-forward law.

2. The marked loss and loop-modulus debit are assembled as

   ```math
   \overline{L}_j
   =
   \overline{\epsilon}_j
   +\overline{h}_j
   +\overline{\lambda}_j,
   ```

   and

   ```math
   \overline{\delta}_j
   \ge
   \max\left\{
   {\overline{E}_j\over\ell_j^2},
   {4\overline{\omega}_j\over\underline{\kappa}_j\ell_j^2}
   \right\}.
   ```

3. The retained-area and downstream debits are bounded by actual source
   estimates:

   ```math
   0<\underline{\alpha}_j\le\alpha_j,
   \quad
   D_{{\rm KP},j}\le\overline{D}_j,
   \quad
   \Delta_{{\rm conf},j}\le\overline{\Delta}_j.
   ```

4. The loop-debited scalar branch reserve is positive:

   ```math
   Q_j
   =
   \underline{S}_{15,j}
   -2\overline{\delta}_j\ell_j^2
   >
   0.
   ```

5. The actual physical-rate lower bound is certified:

   ```math
   \underline{\Gamma}_j
   =
   \underline{\alpha}_j Q_j
   -\overline{L}_j
   -\overline{D}_j,
   \quad
   r_j
   =
   {\underline{\Gamma}_j\over2\ell_j}
   -\overline{\Delta}_j
   \ge
   2m_*
   >
   0.
   ```

The certificate is intentionally scalar. It says that the actual finite
record estimates leave a physical rate after all declared debits; it does
not introduce flux tubes, endpoint trajectories, or a hidden gauge-fixed
field ontology.

### Theorem 4.6I.47d: `AYM-CONF-GAMMA-ACT-SYM` Proves `AYM-CONF-GAMMA-SYM`

If `AYM-CONF-GAMMA-ACT-SYM(m_*)` holds, then
`AYM-CONF-GAMMA-SYM(m_*)` holds.

Proof.

Clause 1 declares that all scalar inputs come from the same actual
whole-process ledger. Clause 2 is exactly the marked-loss and loop-modulus
assembly required by clauses 1 and 2 of `AYM-CONF-GAMMA-SYM`. Clause 3 gives
the retained-area, KP, and physical-rate debit bounds of clause 3 of
`AYM-CONF-GAMMA-SYM`.

Clause 4 identifies the positive loop-debited branch reserve. Clause 5
defines the same `underline Gamma_j` and normalized rate `r_j` as
`AYM-CONF-GAMMA-SYM`, and it certifies `r_j>=2m_*>0` for every cofinal `j`.
Therefore every clause of `AYM-CONF-GAMMA-SYM(m_*)` holds. `square`

### Definition 4.6I.47e: Actual Gamma-Rate Tail Export `AYM-CONF-GAMMA-ACT-TAIL(m_*)`

`AYM-CONF-GAMMA-ACT-TAIL(m_*)` is the actual-tail source package that proves
`AYM-CONF-GAMMA-TAIL(m_*)`. It holds when there is an index `J_G^{act}` and
constants

```math
\alpha_G>0,
\quad
q_G>0,
\quad
b_G\ge0,
\quad
\Delta_G\ge0
```

such that:

1. `AYM-CONF-GAMMA-ACT-SYM(m_*)` is verified directly for every cofinal
   `j<J_G^{act}`;
2. for every cofinal `j>=J_G^{act}`, clauses 1--3 of
   `AYM-CONF-GAMMA-ACT-SYM(m_*)` hold with one declared tail assembly rule;
3. for every cofinal `j>=J_G^{act}`,

   ```math
   \underline{\alpha}_j\ge\alpha_G,
   ```

   ```math
   {\underline{S}_{15,j}
   -2\overline{\delta}_j\ell_j^2
   \over
   \ell_j}
   \ge
   q_G,
   ```

   ```math
   {\overline{L}_j+\overline{D}_j\over2\ell_j}
   \le
   b_G,
   \quad
   \overline{\Delta}_j\le\Delta_G;
   ```

4. the tail physical-rate margin is positive:

   ```math
   {\alpha_Gq_G\over2}
   -b_G
   -\Delta_G
   \ge
   2m_*
   >
   0.
   ```

This is the strongest compact rate certificate in the paper. It says that
the normalized loop-debited reserve stays positive and beats the normalized
marked/KP and Paper-17 debits on the cofinal tail.

### Theorem 4.6I.47f: `AYM-CONF-GAMMA-ACT-TAIL` Proves `AYM-CONF-GAMMA-TAIL`

If `AYM-CONF-GAMMA-ACT-TAIL(m_*)` holds, then
`AYM-CONF-GAMMA-TAIL(m_*)` holds.

Proof.

For `j<J_G^{act}`, clause 1 gives `AYM-CONF-GAMMA-ACT-SYM(m_*)`, hence
Theorem 4.6I.47d gives `AYM-CONF-GAMMA-SYM(m_*)`; this is the finite-prefix
clause of `AYM-CONF-GAMMA-TAIL(m_*)`.

For `j>=J_G^{act}`, clause 2 gives the tail assembly clauses required by
`AYM-CONF-GAMMA-SYM(m_*)`, and clause 3 gives the normalized tail bounds
with constants `alpha_G`, `q_G`, `b_G`, and `Delta_G`. Clause 4 is exactly
the tail rate margin of `AYM-CONF-GAMMA-TAIL(m_*)`. Therefore
`AYM-CONF-GAMMA-TAIL(m_*)` holds. `square`

### Corollary 4.6I.47g: Actual Gamma-Rate Closure

If `AYM-CONF-GAMMA-ACT-SYM(m_*)` holds, then

```text
AYM-CONF-GAMMA-ACT-SYM(m_*)
=> AYM-CONF-GAMMA-SYM(m_*)
=> AYM-CONF-GAMMA-CALC(m_*)
=> AYM-CONF-GAMMA-LB(m_*).
```

If the stronger `AYM-CONF-GAMMA-ACT-TAIL(m_*)` holds, then

```text
AYM-CONF-GAMMA-ACT-TAIL(m_*)
=> AYM-CONF-GAMMA-TAIL(m_*)
=> AYM-CONF-GAMMA-CALC(m_*)
=> AYM-CONF-GAMMA-LB(m_*).
```

Thus the final positive physical rate is reduced to one scalar inequality:

```math
{\alpha_Gq_G\over2}
-b_G
-\Delta_G
\ge
2m_*
>
0
```

on the cofinal tail, plus finite-prefix verification.

### Definition 4.6I.47h: Real-Constant Gamma Tail Computation `AYM-CONF-GAMMA-RC-TAIL(m_*)`

`AYM-CONF-GAMMA-RC-TAIL(m_*)` is the computable real-constant version of
`AYM-CONF-GAMMA-ACT-TAIL(m_*)`. It is the place where the symbols
`q_G`, `b_G`, and `Delta_G` are no longer names but certified tail numbers.

Fix a proposed cofinal tail start `J_G^{rc}`. For every cofinal
`j>=J_G^{rc}`, assemble on the same whole-process ledger

```math
\overline{L}_j
=
\overline{\epsilon}_j+\overline{h}_j+\overline{\lambda}_j,
\quad
Q_j
=
\underline{S}_{15,j}
-2\overline{\delta}_j\ell_j^2,
```

and define the normalized tail observables

```math
q_j
:=
\frac{Q_j}{\ell_j},
\quad
b_j
:=
\frac{\overline{L}_j+\overline{D}_j}{2\ell_j},
\quad
d_j
:=
\overline{\Delta}_j.
```

The optimal tail constants at `J_G^{rc}` are

```math
\alpha_G^{{\rm opt}}(J_G^{rc})
:=
\inf_{j\ge J_G^{rc}}\underline{\alpha}_j,
```

```math
q_G^{{\rm opt}}(J_G^{rc})
:=
\inf_{j\ge J_G^{rc}}q_j,
```

```math
b_G^{{\rm opt}}(J_G^{rc})
:=
\sup_{j\ge J_G^{rc}}b_j,
\quad
\Delta_G^{{\rm opt}}(J_G^{rc})
:=
\sup_{j\ge J_G^{rc}}d_j.
```

The ledger holds when the following finite list is certified.

1. `AYM-CONF-GAMMA-ACT-SYM(m_*)` is verified directly for every cofinal
   `j<J_G^{rc}`.
2. For every cofinal `j>=J_G^{rc}`, clauses 1--3 of
   `AYM-CONF-GAMMA-ACT-SYM(m_*)` hold with one declared tail assembly rule.
3. The computed tail constants are certified by outward-rounded interval
   arithmetic or by symbolic inequalities:

   ```math
   0<\alpha_G\le\alpha_G^{{\rm opt}}(J_G^{rc}),
   \quad
   0<q_G\le q_G^{{\rm opt}}(J_G^{rc}),
   ```

   ```math
   b_G\ge b_G^{{\rm opt}}(J_G^{rc}),
   \quad
   \Delta_G\ge\Delta_G^{{\rm opt}}(J_G^{rc}),
   ```

   with `b_G<infinity` and `Delta_G<infinity`.
4. The computed tail reserve

   ```math
   R_G
   :=
   \frac{\alpha_Gq_G}{2}
   -b_G
   -\Delta_G
   ```

   satisfies

   ```math
   R_G\ge 2m_*>0.
   ```

Equivalently, for a fixed computed tail the largest certified rate parameter
available from this compact gate is

```math
m_*^{{\rm tail}}
=
\frac{1}{2}
\left(
\frac{\alpha_Gq_G}{2}
-b_G
-\Delta_G
\right),
```

and the gate proves any `m_*` with `0<m_*<=m_*^{tail}`.

All quantities in this definition are scalar record quantities exported by
the reserve, loop-modulus, marked-bridge, and Paper-17 debit ledgers. The
test uses no flux-tube primitive, no gauge-fixed field primitive, and no
unobserved subprocess kernel.

### Theorem 4.6I.47i: `AYM-CONF-GAMMA-RC-TAIL` Proves `AYM-CONF-GAMMA-ACT-TAIL`

If `AYM-CONF-GAMMA-RC-TAIL(m_*)` holds, then
`AYM-CONF-GAMMA-ACT-TAIL(m_*)` holds.

Proof.

Clause 1 of `AYM-CONF-GAMMA-RC-TAIL` is the finite-prefix clause of
`AYM-CONF-GAMMA-ACT-TAIL`. Clause 2 supplies the common actual tail assembly
rule required by `AYM-CONF-GAMMA-ACT-TAIL`.

For `j>=J_G^{rc}`, clause 3 implies

```math
\underline{\alpha}_j\ge\alpha_G,
\quad
\frac{\underline{S}_{15,j}
-2\overline{\delta}_j\ell_j^2}{\ell_j}
=q_j
\ge q_G,
```

and

```math
\frac{\overline{L}_j+\overline{D}_j}{2\ell_j}
=b_j
\le b_G,
\quad
\overline{\Delta}_j=d_j\le\Delta_G.
```

These are exactly the normalized tail bounds of
`AYM-CONF-GAMMA-ACT-TAIL`. Clause 4 is exactly the tail physical-rate
margin. Therefore `AYM-CONF-GAMMA-ACT-TAIL(m_*)` holds. `square`

### Theorem 4.6I.47j: Gamma Tail Pass/Fail Test

Fix a cofinal tail start `J`. Define the optimal constants
`alpha_G^{opt}(J)`, `q_G^{opt}(J)`, `b_G^{opt}(J)`, and
`Delta_G^{opt}(J)` as in Definition 4.6I.47h. Set

```math
R_G^{{\rm opt}}(J)
:=
\frac{\alpha_G^{{\rm opt}}(J)q_G^{{\rm opt}}(J)}{2}
-b_G^{{\rm opt}}(J)
-\Delta_G^{{\rm opt}}(J),
```

when the right-hand side is well-defined.

If, for some cofinal `J`, one has

```math
\alpha_G^{{\rm opt}}(J)>0,
\quad
q_G^{{\rm opt}}(J)>0,
\quad
b_G^{{\rm opt}}(J)<\infty,
\quad
\Delta_G^{{\rm opt}}(J)<\infty,
```

and

```math
R_G^{{\rm opt}}(J)>0,
```

then the compact tail route succeeds for every

```math
0<m_*<\frac{R_G^{{\rm opt}}(J)}{2},
```

after choosing rational or interval constants
`alpha_G`, `q_G`, `b_G`, and `Delta_G` strictly inside those bounds.
For a declared target `m_*`, the robust tail test is therefore:

```math
R_G^{{\rm opt}}(J)>2m_*.
```

If exact symbolic constants certify the non-strict inequality
`R_G^{opt}(J)>=2m_*`, the tail also passes at that target. If only interval
data are available, one should keep strict slack.

Conversely, if for every cofinal `J` at least one of the following occurs:

```text
alpha_G^{opt}(J)<=0,
q_G^{opt}(J)<=0,
b_G^{opt}(J)=infinity,
Delta_G^{opt}(J)=infinity,
R_G^{opt}(J)<=0,
```

then this compact Gamma-tail route does not prove
`AYM-CONF-GAMMA-ACT-TAIL(m_*)` for any `m_*>0`.
More generally, for a fixed target `m_*`, if every cofinal `J` has
well-defined constants but `R_G^{opt}(J)<2m_*`, then the compact tail route
does not prove that target. The borderline case `R_G^{opt}(J)=2m_*` requires
an exact symbolic certificate; outward-rounded numerics alone leave it
undecided.

Proof.

The positive case is just Definition 4.6I.47h with a small slack. Since
`R_G^{opt}(J)>0`, choose `alpha_G` and `q_G` below the two infima and choose
`b_G` and `Delta_G` above the two suprema so that

```math
\frac{\alpha_Gq_G}{2}-b_G-\Delta_G>0.
```

Then any `m_*` less than half this margin satisfies the tail inequality, so
Theorem 4.6I.47i gives `AYM-CONF-GAMMA-ACT-TAIL(m_*)`.

For the converse, `AYM-CONF-GAMMA-ACT-TAIL(m_*)` requires a tail with
positive `alpha_G`, positive `q_G`, finite `b_G`, finite `Delta_G`, and
positive margin at least `2m_*`. If every possible tail fails one of these
necessary conditions, no compact tail certificate exists. This does not
falsify confinement; it says that the proof must use finite-window
verification, stronger source estimates, or a refined normalization of the
debit ledger. `square`

### Corollary 4.6I.47k: Gamma Tail Status

The actual Gamma-rate tail has been reduced to a single scalar computation:

```text
compute q_j=(underline S_15,j-2 overline delta_j ell_j^2)/ell_j
compute b_j=(overline L_j+overline D_j)/(2 ell_j)
compute d_j=overline Delta_j
take alpha_G=tail inf underline alpha_j
take q_G=tail inf q_j
take b_G=tail sup b_j
take Delta_G=tail sup d_j
test alpha_G q_G/2 - b_G - Delta_G >= 2m_* > 0.
```

If the test passes on some cofinal tail, then

```text
AYM-CONF-GAMMA-RC-TAIL(m_*)
=> AYM-CONF-GAMMA-ACT-TAIL(m_*)
=> AYM-CONF-GAMMA-TAIL(m_*)
=> AYM-CONF-GAMMA-CALC(m_*).
```

For a fixed target `m_*`, failure means that every cofinal tail either has
`q_G<=0`, divergent `b_G` or `Delta_G`, or a final margin below `2m_*`.
Then the compact tail route is not enough. The honest alternatives are
finite-window `AYM-CONF-GAMMA-ACT-SYM(m_*)`, stronger actual estimates for
reserve and debits, or a better normalized rate ledger.

### Definition 4.6I.47l: Gamma-Rate Constant Attack `AYM-CONF-GAMMA-CONST-ATTACK(m_*)`

`AYM-CONF-GAMMA-CONST-ATTACK(m_*)` is the concrete step-6 calculation after
`AYM-CONF-RES-ATTACK`, `AYM-CONF-LMOD-CONST-ATTACK`, and
`AYM-CONF-MARK-CONST-ATTACK`. It does not introduce a new confinement
ontology. It only assembles the scalar record constants already exported by
the reserve, loop-modulus, marked-bridge, and Paper-17 rate-debit ledgers,
then tests whether the remaining physical Gamma-rate margin is positive.

For each cofinal window `j`, use the same frozen whole-process tower and
define

```math
\overline{L}_j
:=
\overline{\epsilon}_j
+\overline{h}_j
+\overline{\lambda}_j,
```

```math
Q_j
:=
\underline{S}_{15,j}
-2\overline{\delta}_j\ell_j^2,
```

```math
\underline{\Gamma}_j
:=
\underline{\alpha}_jQ_j
-\overline{L}_j
-\overline{D}_j,
```

and

```math
r_j
:=
\frac{\underline{\Gamma}_j}{2\ell_j}
-\overline{\Delta}_j.
```

The normalized Gamma bookkeeping constants are

```math
q_j^{\Gamma}
:=
\frac{Q_j}{\ell_j},
\quad
b_j^{\Gamma}
:=
\frac{\overline{L}_j+\overline{D}_j}{2\ell_j},
\quad
d_j^{\Gamma}
:=
\overline{\Delta}_j.
```

A finite-window Gamma pass at `j` is the certificate

```math
Q_j>0,
\quad
\underline{\Gamma}_j>0,
\quad
r_j\ge2m_*>0.
```

A compact-tail Gamma pass from a cofinal start `J_G` is the certificate that
there are explicit constants

```math
\alpha_G>0,
\quad
q_G>0,
\quad
b_G<\infty,
\quad
\Delta_G<\infty
```

with, for every `j>=J_G`,

```math
\underline{\alpha}_j\ge\alpha_G,
\quad
q_j^{\Gamma}\ge q_G,
\quad
b_j^{\Gamma}\le b_G,
\quad
d_j^{\Gamma}\le\Delta_G,
```

and

```math
R_G
:=
\frac{\alpha_Gq_G}{2}
-b_G
-\Delta_G
\ge
2m_*
>
0.
```

The attack therefore computes or bounds

```text
Q_j, overline L_j, underline Gamma_j, r_j,
q_j^Gamma, b_j^Gamma, d_j^Gamma,
alpha_G, q_G, b_G, Delta_G, R_G.
```

Every number must be certified by symbolic inequalities or outward-rounded
interval arithmetic on the declared parameter domain. Imported estimates
must be tagged by their source ledger: reserve, loop-modulus, marked-bridge,
or Paper-17 debit. Untagged constants do not count.

### Theorem 4.6I.47m: Gamma-Rate Constant Attack Trichotomy

Run `AYM-CONF-GAMMA-CONST-ATTACK(m_*)` on the frozen confinement tower and
record the first applicable outcome in the following priority order. The
priority order makes the audit unambiguous even when, for example, a
finite-window proof and a compact-tail proof both happen to be available.

1. **Finite-window Gamma success:** every cofinal window has a finite-window
   Gamma pass. Then `AYM-CONF-GAMMA-ACT-SYM(m_*)` holds, hence
   `AYM-CONF-GAMMA-CALC(m_*)` holds.
2. **Compact-tail Gamma success:** a finite prefix has finite-window Gamma
   passes and a cofinal tail has a compact-tail Gamma pass. Then
   `AYM-CONF-GAMMA-RC-TAIL(m_*)` holds, hence
   `AYM-CONF-GAMMA-ACT-TAIL(m_*)` and `AYM-CONF-GAMMA-CALC(m_*)` hold.
3. **Smaller-rate survival:** the same computation gives a positive
   certified finite-window margin

   ```math
   \rho_{{\rm fin}}
   :=
   \inf_j r_j
   >
   0
   ```

   or a positive compact-tail margin

   ```math
   \rho_{{\rm tail}}
   :=
   R_G
   >
   0,
   ```

   but the certified margin is below the declared target `2m_*`. Then the
   present constants do not prove the requested `m_*`, but they prove any
   smaller rate satisfying

   ```math
   0<m'_*\le\frac{\rho}{2},
   ```

   where `rho` is any certified positive value no larger than the available
   `rho_fin` or `rho_tail`.
4. **Gamma-rate obstruction:** no finite-window or compact-tail pass is
   available, and no positive smaller-rate margin is certified. Then the
   Paper-18 route has not proved confinement at the Gamma-rate step. The
   obstruction is one of:

   ```text
   Q_j<=0 on a required window,
   underline alpha_j collapses to zero,
   q_j^Gamma collapses to zero on every tail,
   b_j^Gamma is unbounded on every tail,
   d_j^Gamma is unbounded on every tail,
   the final rate margin stays below the target,
   the constants cannot be certified on one same-ledger tower.
   ```

Proof.

If every cofinal `j` has the finite-window Gamma pass, then the data in
Definition 4.6I.47l are precisely clauses 1--5 of
`AYM-CONF-GAMMA-ACT-SYM(m_*)`: same-ledger scalar inputs, marked-loss
assembly, loop-modulus debit, downstream debits, positive `Q_j`, and
`r_j>=2m_*>0`. Theorem 4.6I.47d gives `AYM-CONF-GAMMA-SYM(m_*)`, and
Theorem 4.6I.47a.1 gives `AYM-CONF-GAMMA-CALC(m_*)`.

If a finite prefix passes and a compact tail passes, then the finite prefix
is clause 1 of `AYM-CONF-GAMMA-RC-TAIL(m_*)`. The common assembly rule and
the tail bounds on `underline alpha_j`, `q_j^Gamma`, `b_j^Gamma`, and
`d_j^Gamma` are clauses 2 and 3. The inequality
`R_G>=2m_*>0` is clause 4. Therefore
`AYM-CONF-GAMMA-RC-TAIL(m_*)` holds, and Theorem 4.6I.47i gives
`AYM-CONF-GAMMA-ACT-TAIL(m_*)`.

If the same formulas certify a positive margin smaller than the declared
target, the preceding two arguments apply with `m_*` replaced by any
`m'_*` satisfying the displayed bound. This is not a proof of the requested
rate; it is a proof that the present record tower still contains a positive
rate at a weaker target.

If none of those alternatives is certified, then the attack has exhausted
the Gamma-rate proof routes available from the current scalar constants.
The listed obstructions are exactly the negations of the finite-window and
compact-tail hypotheses. This does not falsify confinement; it localizes the
remaining work to the source constants or to the normalization of the
Gamma-rate ledger. `square`

### Corollary 4.6I.47n: Gamma Constant Attack Status

`AYM-CONF-GAMMA-CONST-ATTACK(m_*)` turns the last confinement-rate question
into a bounded scalar ledger audit:

```text
reserve output       -> underline S_15,j,
loop-modulus output  -> overline delta_j and Q_j,
marked output        -> overline L_j and overline D_j,
Paper-17 output      -> overline Delta_j,
area-retention output -> underline alpha_j,
Gamma assembly       -> r_j or R_G.
```

If the attack passes, Paper 18 has a final positive confinement rate on the
declared record domain. If it only gives smaller-rate survival, Paper 18 has
a weaker positive rate but not the requested `m_*`. If it obstructs, the
honest next move is not to add a flux-tube postulate; it is to improve or
falsify one of the scalar source estimates on the same whole-process
continuum tower.

### Definition 4.6I.47o: Source-Populated Gamma Ledger `AYM-CONF-GAMMA-SRC-POP`

`AYM-CONF-GAMMA-SRC-POP` is the step-1 population of
`AYM-CONF-GAMMA-CONST-ATTACK(m_*)` by actual source constants from the
preceding Paper-18 ledgers. For every cofinal window `j`, all quantities
must be read from the same frozen whole-process tower:

| Gamma input | Source ledger | Concrete population |
| --- | --- | --- |
| `underline S_15,j` | `AYM-CONF-RES-ATTACK` | `gamma_15,j underline M_j - overline epsilon_15,j` |
| `overline delta_j` | `AYM-CONF-LMOD-CONST-ATTACK` | any certified value with `delta_req,j<=overline delta_j<underline S_15,j/(2 ell_j^2)` on finite-window pass |
| `Q_j` | reserve plus loop-modulus | `underline S_15,j - 2 overline delta_j ell_j^2` |
| `underline alpha_j` | marked retained-area ledger | any certified lower bound with `0<underline alpha_j<=alpha_j` |
| `overline epsilon_j` | marked local-loss ledger | finite endpoint/collar/counterterm/projection loss |
| `overline h_j` | endpoint-enlarged KP ledger | finite polymer height loss with `h_j^S<=overline h_j` |
| `overline lambda_j` | endpoint-enlarged KP ledger | finite marked polymer activity loss with `lambda_mark,j^S<=overline lambda_j` |
| `overline D_j` | marked KP threshold ledger | finite bound for `D_KP,j` |
| `overline Delta_j` | Paper-17 rate-debit ledger | finite selected-rate comparison debit |
| `ell_j` | cofinal battery schedule | physical length scale of the scheduled confinement window |

The populated local loss is

```math
\overline{L}_j
=
\overline{\epsilon}_j
+\overline{h}_j
+\overline{\lambda}_j.
```

The populated Gamma reserve and physical rate are

```math
\underline{\Gamma}_j
=
\underline{\alpha}_j
\left(
\gamma_{15,j}\underline{M}_j
-\overline{\epsilon}_{15,j}
-2\overline{\delta}_j\ell_j^2
\right)
-\overline{\epsilon}_j
-\overline{h}_j
-\overline{\lambda}_j
-\overline{D}_j,
```

```math
r_j
=
\frac{\underline{\Gamma}_j}{2\ell_j}
-\overline{\Delta}_j.
```

This is the fully populated direct inequality. Written without
abbreviations, the finite-window target is

```math
\frac{
\underline{\alpha}_j
\left(
\gamma_{15,j}\underline{M}_j
-\overline{\epsilon}_{15,j}
-2\overline{\delta}_j\ell_j^2
\right)
-\overline{\epsilon}_j
-\overline{h}_j
-\overline{\lambda}_j
-\overline{D}_j
}{2\ell_j}
-\overline{\Delta}_j
\ge
2m_*
>
0.
```

The source population passes at `j` when every table entry is finite,
same-ledger tagged, and the inequalities

```math
\gamma_{15,j}\underline{M}_j-\overline{\epsilon}_{15,j}>0,
```

```math
Q_j
=
\gamma_{15,j}\underline{M}_j
-\overline{\epsilon}_{15,j}
-2\overline{\delta}_j\ell_j^2
>
0
```

are both certified.

### Definition 4.6I.47p: Gamma Route Decision `AYM-CONF-GAMMA-ROUTE`

`AYM-CONF-GAMMA-ROUTE` is the step-2 decision between the finite-window
route and the compact-tail route.

The finite-window route is selected when `AYM-CONF-GAMMA-SRC-POP` passes for
every cofinal `j` and the direct inequalities for the individual `r_j` are
available. This route allows slot denominators, endpoint constants, and
marked KP thresholds to vary with `j`, provided every finite window is
certified on the same whole-process tower.

The compact-tail route is selected only after the normalized tail constants

```math
\alpha_G,
\quad
q_G,
\quad
b_G,
\quad
\Delta_G
```

are certified with

```math
\alpha_G>0,
\quad
q_G>0,
\quad
b_G<\infty,
\quad
\Delta_G<\infty,
\quad
\frac{\alpha_Gq_G}{2}-b_G-\Delta_G\ge2m_*>0.
```

The route decision for raw Wilson-loop slots is therefore:

```text
use finite-window Gamma direct by default;
use compact-tail Gamma only after normalized tail constants are certified;
do not use raw absolute loop denominators as a tail assumption.
```

This is the Barandes-aligned choice because it keeps every claim tied to
finite scalar records and their projective restrictions. A cofinal tail is
allowed only when it is itself a scalar record theorem, not a hidden
large-distance picture.

### Theorem 4.6I.47q: Direct Finite-Window Gamma Rate Test `AYM-CONF-GAMMA-FW-DIRECT(m_*)`

Assume `AYM-CONF-GAMMA-SRC-POP`. Suppose that for every cofinal window `j`
the populated constants satisfy

```math
\frac{
\underline{\alpha}_j
\left(
\gamma_{15,j}\underline{M}_j
-\overline{\epsilon}_{15,j}
-2\overline{\delta}_j\ell_j^2
\right)
-\overline{\epsilon}_j
-\overline{h}_j
-\overline{\lambda}_j
-\overline{D}_j
}{2\ell_j}
-\overline{\Delta}_j
\ge
2m_*
>
0.
```

Then `AYM-CONF-GAMMA-ACT-SYM(m_*)` holds. Consequently
`AYM-CONF-GAMMA-CALC(m_*)` and `AYM-CONF-GAMMA-LB(m_*)` hold.

Proof.

By `AYM-CONF-GAMMA-SRC-POP`, every term in the displayed inequality is a
finite scalar record constant on the same frozen whole-process tower. The
reserve and loop-modulus part gives

```math
Q_j
=
\gamma_{15,j}\underline{M}_j
-\overline{\epsilon}_{15,j}
-2\overline{\delta}_j\ell_j^2
>
0.
```

The marked-loss and KP terms assemble to

```math
\overline{L}_j
=
\overline{\epsilon}_j
+\overline{h}_j
+\overline{\lambda}_j.
```

Thus the displayed inequality is exactly

```math
r_j
=
\frac{
\underline{\alpha}_jQ_j
-\overline{L}_j
-\overline{D}_j
}{2\ell_j}
-\overline{\Delta}_j
\ge
2m_*
>
0.
```

This is clause 5 of `AYM-CONF-GAMMA-ACT-SYM(m_*)`, while the source
population supplies clauses 1--4: same-ledger inputs, marked-loss assembly,
loop-modulus debit, downstream debits, retained-area lower bound, and
positive `Q_j`. Therefore `AYM-CONF-GAMMA-ACT-SYM(m_*)` holds. Corollary
4.6I.47g gives `AYM-CONF-GAMMA-LB(m_*)` through
`AYM-CONF-GAMMA-CALC(m_*)`. `square`

### Corollary 4.6I.47r: Steps 1--3 Status

The first three post-attack steps are now explicit inside Paper 18:

```text
1. populate Gamma constants:
   AYM-CONF-GAMMA-SRC-POP;

2. decide route:
   AYM-CONF-GAMMA-ROUTE selects finite-window direct by default,
   compact-tail only after normalized tail constants pass;

3. test the final rate directly:
   AYM-CONF-GAMMA-FW-DIRECT(m_*)
   => AYM-CONF-GAMMA-ACT-SYM(m_*)
   => AYM-CONF-GAMMA-CALC(m_*).
```

What has not been proved is that actual continuum `4D SU(N)` supplies the
numerical or symbolic inequalities in `AYM-CONF-GAMMA-FW-DIRECT(m_*)`. The
paper has reduced that question to a single populated scalar inequality
with all debits named.

### Definition 4.6I.47s: Gamma Constant Worksheet `AYM-CONF-GAMMA-WORK_j`

For a fixed cofinal window `j`, `AYM-CONF-GAMMA-WORK_j` is the finite
worksheet used to attack the populated Gamma inequality. It consists of the
following scalar entries, all on the same frozen whole-process tower:

```math
R_j^{{\rm res}}
:=
\gamma_{15,j}\underline{M}_j
-\overline{\epsilon}_{15,j},
```

```math
Q_j
:=
R_j^{{\rm res}}
-2\overline{\delta}_j\ell_j^2,
```

```math
A_j^{{\rm ret}}
:=
\frac{\underline{\alpha}_jQ_j}{2\ell_j},
```

```math
B_j^{{\rm mark}}
:=
\frac{
\overline{\epsilon}_j
+\overline{h}_j
+\overline{\lambda}_j
+\overline{D}_j
}{2\ell_j},
```

```math
C_j^{{\rm P17}}
:=
\overline{\Delta}_j,
```

and

```math
r_j
:=
A_j^{{\rm ret}}
-B_j^{{\rm mark}}
-C_j^{{\rm P17}}.
```

The worksheet is complete when each entry has a source tag:

```text
RES  -> R_j^res and underline S_15,j,
LMOD -> overline delta_j and Q_j,
AREA -> underline alpha_j,
MARK -> overline epsilon_j, overline h_j, overline lambda_j, overline D_j,
P17  -> overline Delta_j,
WP   -> same frozen whole-process tower.
```

`AYM-CONF-GAMMA-WORK_j` is not itself a pass condition. It is the finite
ledger on which the next five tests are evaluated.

### Definition 4.6I.47t: Reserve-Loop-Debit Pass `AYM-CONF-GAMMA-RLD_j`

`AYM-CONF-GAMMA-RLD_j` holds when the reserve survives the loop-modulus
debit on window `j`:

```math
R_j^{{\rm res}}>0,
\quad
Q_j
=
R_j^{{\rm res}}
-2\overline{\delta}_j\ell_j^2
>
0.
```

Equivalently, with the finite-window normalized reserve

```math
q_j^{{\rm RLD}}
:=
\frac{Q_j}{\ell_j},
```

the condition is

```math
q_j^{{\rm RLD}}>0.
```

If `AYM-CONF-RES-ATTACK` has finite-window reserve success and
`AYM-CONF-LMOD-CONST-ATTACK` has finite-window loop-modulus success at `j`,
then `AYM-CONF-GAMMA-RLD_j` holds for every admissible
`overline delta_j<underline S_15,j/(2 ell_j^2)`.

Proof.

Finite-window reserve success gives

```math
R_j^{{\rm res}}
=
\underline{S}_{15,j}
>
0.
```

Finite-window loop-modulus success chooses `overline delta_j` strictly below
`underline S_15,j/(2 ell_j^2)`. Hence

```math
Q_j
=
\underline{S}_{15,j}
-2\overline{\delta}_j\ell_j^2
>
0.
```

Dividing by `ell_j>0` gives `q_j^{RLD}>0`. `square`

### Definition 4.6I.47u: Retained-Area Pass `AYM-CONF-GAMMA-AREA_j`

`AYM-CONF-GAMMA-AREA_j` holds when the marked-geometry ledger exports a
strict retained-area lower bound

```math
0<\underline{\alpha}_j\le\alpha_j.
```

For the finite-window route no uniform lower bound in `j` is required. For a
compact-tail route one must additionally certify

```math
\inf_{j\ge J}\underline{\alpha}_j>0
```

on the declared tail.

If `AYM-CONF-MARK-CONST-ATTACK` has finite-window marked success at `j`,
then `AYM-CONF-GAMMA-AREA_j` holds.

Proof.

Finite-window marked success includes the retained-area export `alpha_j>0`
from the endpoint closure and marked hull geometry. Choose any certified
lower bound `underline alpha_j` with `0<underline alpha_j<=alpha_j`. This is
exactly `AYM-CONF-GAMMA-AREA_j`. `square`

### Definition 4.6I.47v: Marked/KP Debit Pass `AYM-CONF-GAMMA-MKPD_j`

`AYM-CONF-GAMMA-MKPD_j` holds when the marked endpoint and KP ledgers export
finite same-ledger debits

```math
\overline{\epsilon}_j<\infty,
\quad
\overline{h}_j<\infty,
\quad
\overline{\lambda}_j<\infty,
\quad
\overline{D}_j<\infty,
```

and therefore

```math
B_j^{{\rm mark}}
=
\frac{
\overline{\epsilon}_j
+\overline{h}_j
+\overline{\lambda}_j
+\overline{D}_j
}{2\ell_j}
<
\infty.
```

If `AYM-CONF-MARK-CONST-ATTACK` has finite-window marked success at `j`,
then `AYM-CONF-GAMMA-MKPD_j` holds.

Proof.

Finite-window marked success gives finite local marked loss, finite
endpoint-enlarged KP height and activity losses, and a finite bound for
`D_KP,j`. These are respectively bounded by `overline epsilon_j`,
`overline h_j`, `overline lambda_j`, and `overline D_j`. Since `ell_j>0`,
`B_j^{mark}` is finite. `square`

### Definition 4.6I.47w: Paper-17 Selected-Rate Debit Pass `AYM-CONF-GAMMA-P17D_j`

`AYM-CONF-GAMMA-P17D_j` holds when the Paper-17 mass-gap comparison ledger
exports a finite selected-rate debit on the same window:

```math
0\le
\Delta_{{\rm conf},j}
\le
\overline{\Delta}_j
<
\infty.
```

The debit is admissible only when it is restricted from the same
whole-process tower as the Wilson-loop law and the marked endpoint battery.
If the selected-rate comparison uses a different cutoff path, endpoint
protocol, or projection convention, `AYM-CONF-GAMMA-P17D_j` fails by
same-ledger mismatch.

### Theorem 4.6I.47x: Six-Step Finite-Window Gamma Pass

Assume that for every cofinal `j` the following six statements hold:

1. `AYM-CONF-GAMMA-WORK_j`;
2. `AYM-CONF-GAMMA-RLD_j`;
3. `AYM-CONF-GAMMA-AREA_j`;
4. `AYM-CONF-GAMMA-MKPD_j`;
5. `AYM-CONF-GAMMA-P17D_j`;
6. the worksheet rate inequality

   ```math
   A_j^{{\rm ret}}
   -B_j^{{\rm mark}}
   -C_j^{{\rm P17}}
   \ge
   2m_*
   >
   0.
   ```

Then `AYM-CONF-GAMMA-FW-DIRECT(m_*)` holds, hence
`AYM-CONF-GAMMA-CALC(m_*)` holds.

Proof.

By the worksheet definitions,

```math
A_j^{{\rm ret}}
-B_j^{{\rm mark}}
-C_j^{{\rm P17}}
=
\frac{
\underline{\alpha}_jQ_j
-\overline{\epsilon}_j
-\overline{h}_j
-\overline{\lambda}_j
-\overline{D}_j
}{2\ell_j}
-\overline{\Delta}_j.
```

Using

```math
Q_j
=
\gamma_{15,j}\underline{M}_j
-\overline{\epsilon}_{15,j}
-2\overline{\delta}_j\ell_j^2,
```

the displayed rate inequality is exactly the hypothesis of
`AYM-CONF-GAMMA-FW-DIRECT(m_*)`. The first five statements ensure that all
constants are finite, positive where needed, and same-ledger tagged.
Theorem 4.6I.47q gives `AYM-CONF-GAMMA-ACT-SYM(m_*)`, and Corollary
4.6I.47g gives `AYM-CONF-GAMMA-CALC(m_*)`. `square`

### Corollary 4.6I.47y: Six-Step Gamma Obstruction Classifier

If Theorem 4.6I.47x cannot be applied, the finite-window Gamma route fails
at one of the following named locations:

| Step | Gate | Failure meaning |
| --- | --- | --- |
| 1 | `AYM-CONF-GAMMA-WORK_j` | some constant is missing, untagged, or not on the common tower |
| 2 | `AYM-CONF-GAMMA-RLD_j` | reserve does not survive loop-modulus debit: `Q_j<=0` |
| 3 | `AYM-CONF-GAMMA-AREA_j` | retained-area lower bound collapses or is not certified |
| 4 | `AYM-CONF-GAMMA-MKPD_j` | marked/KP losses are not finite on the endpoint-enlarged battery |
| 5 | `AYM-CONF-GAMMA-P17D_j` | Paper-17 selected-rate debit is missing, infinite, or off-ledger |
| 6 | worksheet rate inequality | all constants exist, but `r_j<2m_*` somewhere cofinal |

The last case is the most informative failure: it says the ontology and
ledger are clean, but the current constants do not prove the requested
physical rate. Then the honest options are a smaller certified `m_*`, sharper
source constants, a different finite-window schedule, or a normalized
compact-tail proof.

### Definition 4.6I.47z: First Gamma Worksheet `AYM-CONF-FIRST-GAMMA-WORK_{j_0}`

Let `j_0` be the first nontrivial cofinal window after the tower, law/window,
reserve, loop-modulus, and marked-bridge ledgers have all been frozen. The
first Gamma worksheet is the specialization of `AYM-CONF-GAMMA-WORK_j` to
that window.

Use the shorthand

```math
\ell_0:=\ell_{j_0},
\quad
\gamma_0:=\gamma_{15,j_0},
\quad
\underline{M}_0:=\underline{M}_{j_0},
\quad
e_{15,0}:=\overline{\epsilon}_{15,j_0},
```

```math
\delta_0:=\overline{\delta}_{j_0},
\quad
\alpha_0:=\underline{\alpha}_{j_0},
\quad
e_0:=\overline{\epsilon}_{j_0},
\quad
h_0:=\overline{h}_{j_0},
```

```math
\lambda_0:=\overline{\lambda}_{j_0},
\quad
D_0:=\overline{D}_{j_0},
\quad
\Delta_0:=\overline{\Delta}_{j_0}.
```

Define the first-window reserve, loop-debited reserve, and normalized
loop-debited reserve:

```math
R_0^{{\rm res}}
:=
\gamma_0\underline{M}_0-e_{15,0},
```

```math
Q_0
:=
R_0^{{\rm res}}-2\delta_0\ell_0^2,
```

```math
q_0
:=
\frac{Q_0}{\ell_0}.
```

Define the three rate terms:

```math
A_0^{{\rm ret}}
:=
\frac{\alpha_0Q_0}{2\ell_0},
```

```math
B_0^{{\rm mark}}
:=
\frac{e_0+h_0+\lambda_0+D_0}{2\ell_0},
```

```math
C_0^{{\rm P17}}
:=
\Delta_0.
```

The first-window Gamma rate is

```math
r_0
:=
A_0^{{\rm ret}}
-B_0^{{\rm mark}}
-C_0^{{\rm P17}}.
```

The first-window target is

```math
r_0\ge2m_*>0.
```

This worksheet proves nothing cofinal by itself. It is the first diagnostic
place where the actual constants must either produce a positive rate or
identify a concrete obstruction.

### Lemma 4.6I.47z.1: First Worksheet Symbolic Pass Criterion

Assume that the first worksheet has certified constants

```math
q_0^{{\rm min}}>0,
\quad
a_0>0,
\quad
b_0\ge0,
\quad
c_0\ge0
```

such that

```math
Q_0\ge q_0^{{\rm min}}\ell_0,
\quad
\alpha_0\ge a_0,
```

```math
B_0^{{\rm mark}}\le b_0,
\quad
C_0^{{\rm P17}}\le c_0,
```

and

```math
\frac{a_0q_0^{{\rm min}}}{2}
-b_0
-c_0
\ge
2m_*
>
0.
```

Then the first window passes the Gamma rate test:

```math
r_0\ge2m_*>0.
```

Proof.

The first two bounds give

```math
A_0^{{\rm ret}}
=
\frac{\alpha_0Q_0}{2\ell_0}
\ge
\frac{a_0q_0^{{\rm min}}}{2}.
```

The debit bounds give

```math
B_0^{{\rm mark}}+C_0^{{\rm P17}}
\le
b_0+c_0.
```

Therefore

```math
r_0
=
A_0^{{\rm ret}}
-B_0^{{\rm mark}}
-C_0^{{\rm P17}}
\ge
\frac{a_0q_0^{{\rm min}}}{2}
-b_0
-c_0
\ge
2m_*
>
0.
```

`square`

### Lemma 4.6I.47z.2: First Reserve-Loop Bottleneck

The first-window reserve after loop debit is

```math
Q_0
=
\gamma_0\underline{M}_0
-e_{15,0}
-2\delta_0\ell_0^2.
```

Thus the first reserve-loop pass condition is exactly

```math
\gamma_0\underline{M}_0
-e_{15,0}
>
2\delta_0\ell_0^2.
```

Equivalently, the normalized reserve is

```math
q_0
=
\frac{\gamma_0\underline{M}_0-e_{15,0}}{\ell_0}
-2\delta_0\ell_0.
```

This exposes the first genuine bottleneck: even a positive Paper-15 reserve
does not help the Gamma rate if the loop-modulus debit grows faster than the
reserve when measured in the selected physical length `ell_0`.

### Lemma 4.6I.47z.2a: First Loop-Modulus Substitution

On the first window, set

```math
E_0:=\overline{E}_{j_0},
\quad
\omega_0:=\overline{\omega}_{j_0},
\quad
\kappa_0:=\underline{\kappa}_{j_0}.
```

The loop-modulus worksheet gives the minimal legal debit

```math
\delta_{{\rm req},0}
=
\max\left\{
\frac{E_0}{\ell_0^2},
\frac{4\omega_0}{\kappa_0\ell_0^2}
\right\}.
```

Equivalently, define the unnormalized loop-modulus cost

```math
\Lambda_0^{{\rm LMOD}}
:=
\max\left\{
E_0,
\frac{4\omega_0}{\kappa_0}
\right\}.
```

Then

```math
\delta_{{\rm req},0}\ell_0^2
=
\Lambda_0^{{\rm LMOD}}.
```

Consequently, the first reserve-loop bottleneck admits some legal
`delta_0>=delta_req,0` with `Q_0>0` exactly when

```math
\gamma_0\underline{M}_0-e_{15,0}
>
2\Lambda_0^{{\rm LMOD}}
=
2\max\left\{
E_0,
\frac{4\omega_0}{\kappa_0}
\right\}.
```

Proof.

If a legal `delta_0>=delta_req,0` gives `Q_0>0`, then

```math
\gamma_0\underline{M}_0-e_{15,0}
>
2\delta_0\ell_0^2
\ge
2\delta_{{\rm req},0}\ell_0^2
=
2\Lambda_0^{{\rm LMOD}}.
```

Conversely, if the displayed strict inequality holds, define the reserve-loop
slack

```math
s_0^{{\rm RLD}}
:=
\gamma_0\underline{M}_0-e_{15,0}
-2\Lambda_0^{{\rm LMOD}}
>
0.
```

Choose any certified `theta_0` with

```math
0<\theta_0<s_0^{{\rm RLD}}
```

and set

```math
\delta_0
=
\delta_{{\rm req},0}
+\frac{\theta_0}{2\ell_0^2}.
```

Then `delta_0>=delta_req,0`, and

```math
Q_0
=
\gamma_0\underline{M}_0-e_{15,0}
-2\delta_0\ell_0^2
=
s_0^{{\rm RLD}}-\theta_0
>
0.
```

Thus the legal loop-modulus choice leaves positive first-window reserve.
`square`

### Corollary 4.6I.47z.2b: Minimal-Debit First Bottleneck

With the minimal loop-modulus debit, the first bottleneck is no longer

```text
gamma_0 M_0 - e_15,0 > 2 delta_0 ell_0^2.
```

It is the source-constant inequality

```math
\gamma_0\underline{M}_0-e_{15,0}
>
2\max\left\{
E_0,
\frac{4\omega_0}{\kappa_0}
\right\}.
```

Failure of this inequality has an exact interpretation: the transported
Paper-15 reserve on the first window is already consumed by readout error
`E_0`, loop-continuity error `omega_0`, or slot-denominator weakness
`kappa_0`. No later marked/KP or Paper-17 estimate can repair this
first-window reserve-loop failure.

### Theorem 4.6I.47z.2c: Minimal-Debit Full First-Window Pass

Define the minimal-debit leftover reserve

```math
S_0^{{\rm RLD}}
:=
\gamma_0\underline{M}_0
-e_{15,0}
-2\Lambda_0^{{\rm LMOD}},
```

where

```math
\Lambda_0^{{\rm LMOD}}
=
\max\left\{
E_0,
\frac{4\omega_0}{\kappa_0}
\right\}.
```

Assume

```math
S_0^{{\rm RLD}}>0,
\quad
\alpha_0>0.
```

If the pressure-balance inequality

```math
\alpha_0S_0^{{\rm RLD}}
>
e_0+h_0+\lambda_0+D_0
+2\ell_0(\Delta_0+2m_*)
```

holds, then the first window passes the Gamma rate test for any legal
loop-modulus debit `delta_0` sufficiently close to `delta_req,0`.

More explicitly, define the pressure surplus

```math
\Pi_0
:=
\alpha_0S_0^{{\rm RLD}}
-e_0-h_0-\lambda_0-D_0
-2\ell_0(\Delta_0+2m_*).
```

If `Pi_0>0`, then every certified choice

```math
\delta_0
=
\delta_{{\rm req},0}
+\frac{\theta_0}{2\ell_0^2}
```

with

```math
0<\theta_0<
\min\left\{
S_0^{{\rm RLD}},
\frac{\Pi_0}{\alpha_0}
\right\}
```

gives

```math
r_0\ge2m_*>0.
```

Proof.

For the displayed choice of `delta_0`, Lemma 4.6I.47z.2a gives

```math
Q_0
=
S_0^{{\rm RLD}}-\theta_0.
```

The first-window rate is therefore

```math
r_0
=
\frac{\alpha_0(S_0^{{\rm RLD}}-\theta_0)
-e_0-h_0-\lambda_0-D_0}{2\ell_0}
-\Delta_0.
```

The condition `r_0>=2m_*` is equivalent to

```math
\alpha_0(S_0^{{\rm RLD}}-\theta_0)
\ge
e_0+h_0+\lambda_0+D_0
+2\ell_0(\Delta_0+2m_*).
```

By definition of `Pi_0`, this is equivalent to

```math
\Pi_0-\alpha_0\theta_0\ge0.
```

The strict upper bound `theta_0<Pi_0/alpha_0` gives the desired inequality
with positive slack. The additional bound `theta_0<S_0^{RLD}` keeps
`Q_0>0`. Hence the first window passes. `square`

### Corollary 4.6I.47z.2d: First-Window Pressure Balance

The minimal-debit first-window pass is exactly the comparison

```text
retained reserve pressure
>
marked/KP pressure + Paper-17 pressure + target-rate pressure,
```

where

```math
P_0^{{\rm res}}
:=
\alpha_0
\left(
\gamma_0\underline{M}_0-e_{15,0}
-2\max\left\{
E_0,
\frac{4\omega_0}{\kappa_0}
\right\}
\right),
```

```math
P_0^{{\rm mark}}
:=
e_0+h_0+\lambda_0+D_0,
```

```math
P_0^{{\rm P17}}
:=
2\ell_0\Delta_0,
\quad
P_0^{{\rm target}}
:=
4\ell_0m_*.
```

Thus the pass condition is

```math
P_0^{{\rm res}}
>
P_0^{{\rm mark}}
+P_0^{{\rm P17}}
+P_0^{{\rm target}}.
```

If this fails after `S_0^{RLD}>0` has been proved, the first-window
obstruction is no longer the reserve-loop bottleneck. It is one of:
retained-area weakness, marked/KP pressure, Paper-17 selected-rate pressure,
or an over-large target rate.

### Definition 4.6I.47z.2e: Cofinal Minimal-Debit Gamma Worksheet `AYM-CONF-GAMMA-MD-WORK_j`

For an arbitrary cofinal window `j`, define the loop-modulus source constants

```math
E_j:=\overline{E}_j,
\quad
\omega_j:=\overline{\omega}_j,
\quad
\kappa_j:=\underline{\kappa}_j,
```

and the unnormalized minimal loop-modulus debit

```math
\Lambda_j^{{\rm LMOD}}
:=
\max\left\{
E_j,
\frac{4\omega_j}{\kappa_j}
\right\}.
```

Then

```math
\delta_{{\rm req},j}\ell_j^2
=
\Lambda_j^{{\rm LMOD}}.
```

Define the cofinal minimal-debit leftover reserve

```math
S_j^{{\rm RLD}}
:=
\gamma_{15,j}\underline{M}_j
-\overline{\epsilon}_{15,j}
-2\Lambda_j^{{\rm LMOD}}.
```

Define the four pressure terms

```math
P_j^{{\rm res}}
:=
\underline{\alpha}_jS_j^{{\rm RLD}},
```

```math
P_j^{{\rm mark}}
:=
\overline{\epsilon}_j
+\overline{h}_j
+\overline{\lambda}_j
+\overline{D}_j,
```

```math
P_j^{{\rm P17}}
:=
2\ell_j\overline{\Delta}_j,
\quad
P_j^{{\rm target}}
:=
4\ell_jm_*,
```

and the pressure surplus

```math
\Pi_j
:=
P_j^{{\rm res}}
-P_j^{{\rm mark}}
-P_j^{{\rm P17}}
-P_j^{{\rm target}}.
```

`AYM-CONF-GAMMA-MD-WORK_j` holds when all these constants are finite,
same-ledger tagged, and

```math
\kappa_j>0,
\quad
\underline{\alpha}_j>0.
```

This is the arbitrary-window version of the first Gamma worksheet. The only
difference is that it does not privilege `j_0`; every cofinal window must
carry its own finite record constants.

### Theorem 4.6I.47z.2e.0: Exact Pressure Criterion For `Pi_j>0`

Assume `AYM-CONF-GAMMA-MD-WORK_j`. If

```math
\underline{\alpha}_jS_j^{{\rm RLD}}
>
\overline{\epsilon}_j
+\overline{h}_j
+\overline{\lambda}_j
+\overline{D}_j
+2\ell_j\overline{\Delta}_j
+4\ell_jm_*,
```

then

```math
\Pi_j>0.
```

Proof.

By definition of the pressure surplus,

```math
\Pi_j
=
\underline{\alpha}_jS_j^{{\rm RLD}}
-\left(
\overline{\epsilon}_j
+\overline{h}_j
+\overline{\lambda}_j
+\overline{D}_j
+2\ell_j\overline{\Delta}_j
+4\ell_jm_*
\right).
```

The displayed strict pressure inequality says exactly that the right-hand
side is strictly positive. Hence `Pi_j>0`. `square`

### Definition 4.6I.47z.2e.1: Reserve-Loop Source Import `AYM-CONF-SRLD-SRC_j`

`AYM-CONF-SRLD-SRC_j` is the finite-window source certificate for
`S_j^{RLD}>0`. It imports lower reserve data and upper loop-modulus data on
the same frozen whole-process tower. It consists of certified constants

```math
\gamma_j^- >0,
\quad
M_j^- >0,
\quad
e_{15,j}^+\ge0,
```

```math
E_j^+\ge0,
\quad
\omega_j^+\ge0,
\quad
\kappa_j^- >0,
```

such that

```math
\gamma_{15,j}\ge\gamma_j^-,
\quad
\underline{M}_j\ge M_j^-,
\quad
\overline{\epsilon}_{15,j}\le e_{15,j}^+,
```

```math
E_j\le E_j^+,
\quad
\omega_j\le\omega_j^+,
\quad
\kappa_j\ge\kappa_j^-,
```

and the strict source inequality

```math
\gamma_j^- M_j^- - e_{15,j}^+
>
2\max\left\{
E_j^+,
\frac{4\omega_j^+}{\kappa_j^-}
\right\}.
```

The source certificate is admissible only when the six bounds come from the
same law/window/reserve/loop-modulus ledger as `AYM-CONF-GAMMA-MD-WORK_j`.

### Theorem 4.6I.47z.2e.2: `AYM-CONF-SRLD-SRC_j` Proves `S_j^{RLD}>0`

Assume `AYM-CONF-GAMMA-MD-WORK_j` and `AYM-CONF-SRLD-SRC_j`. Then

```math
S_j^{{\rm RLD}}>0.
```

Proof.

By the reserve lower bounds,

```math
\gamma_{15,j}\underline{M}_j
-\overline{\epsilon}_{15,j}
\ge
\gamma_j^- M_j^- - e_{15,j}^+.
```

By the loop-modulus upper and denominator lower bounds,

```math
\Lambda_j^{{\rm LMOD}}
=
\max\left\{
E_j,
\frac{4\omega_j}{\kappa_j}
\right\}
\le
\max\left\{
E_j^+,
\frac{4\omega_j^+}{\kappa_j^-}
\right\}.
```

Therefore

```math
S_j^{{\rm RLD}}
=
\gamma_{15,j}\underline{M}_j
-\overline{\epsilon}_{15,j}
-2\Lambda_j^{{\rm LMOD}}
```

satisfies

```math
S_j^{{\rm RLD}}
\ge
\gamma_j^- M_j^- - e_{15,j}^+
-2\max\left\{
E_j^+,
\frac{4\omega_j^+}{\kappa_j^-}
\right\}
>
0.
```

`square`

### Corollary 4.6I.47z.2e.3: Cofinal Reserve-Loop Source Import

If `AYM-CONF-SRLD-SRC_j` holds for every cofinal `j`, then
`S_j^{RLD}>0` holds for every cofinal `j`.

More compactly, on a cofinal tail `j>=J_R`, suppose there are tail constants

```math
\gamma_R>0,
\quad
M_R>0,
\quad
e_R\ge0,
\quad
E_R\ge0,
\quad
\omega_R\ge0,
\quad
\kappa_R>0
```

such that, for all `j>=J_R`,

```math
\gamma_{15,j}\ge\gamma_R,
\quad
\underline{M}_j\ge M_R,
\quad
\overline{\epsilon}_{15,j}\le e_R,
```

```math
E_j\le E_R,
\quad
\omega_j\le\omega_R,
\quad
\kappa_j\ge\kappa_R,
```

and

```math
\gamma_RM_R-e_R
>
2\max\left\{
E_R,
\frac{4\omega_R}{\kappa_R}
\right\}.
```

Then `S_j^{RLD}>0` on that cofinal tail, with finite-prefix windows checked
by the finite-window source certificate.

Proof.

Apply Theorem 4.6I.47z.2e.2 pointwise using the tail constants for
`j>=J_R`. For `j<J_R`, use the finite-window certificates. `square`

### Corollary 4.6I.47z.2e.4: First Real Reserve-Loop Obstruction

The first actual-confinement attack has now been reduced to proving or
falsifying the scalar inequality

```math
\gamma_{15,j}\underline{M}_j-\overline{\epsilon}_{15,j}
>
2\max\left\{
E_j,
\frac{4\omega_j}{\kappa_j}
\right\}.
```

If the imported lower and upper bounds fail to make this inequality strict,
then the obstruction is already before marked endpoints, KP thresholds, and
Paper-17 selected-rate debits. It is one of:

```text
reserve calibration gamma_15,j too small,
transported reserve underline M_j too small,
reserve readout error overline epsilon_15,j too large,
loop readout error E_j too large,
loop-continuity modulus omega_j too large,
Creutz-slot denominator kappa_j too small,
or same-ledger mismatch.
```

This is a genuine scalar-record obstruction. It does not falsify
confinement, but it says the current Paper-18 route has not yet produced the
minimal reserve needed for the Gamma-rate worksheet.

### Definition 4.6I.47z.2e.5: Pressure-Surplus Source Import `AYM-CONF-PI-SRC_j(m_*)`

`AYM-CONF-PI-SRC_j(m_*)` is the finite-window source certificate for
`Pi_j>0` after `S_j^{RLD}>0` has been imported. It consists of certified
constants

```math
s_j^- >0,
\quad
a_j^- >0,
```

```math
e_j^+\ge0,
\quad
h_j^+\ge0,
\quad
\lambda_j^+\ge0,
\quad
D_j^+\ge0,
\quad
\Delta_j^+\ge0
```

such that

```math
S_j^{{\rm RLD}}\ge s_j^-,
\quad
\underline{\alpha}_j\ge a_j^-,
```

```math
\overline{\epsilon}_j\le e_j^+,
\quad
\overline{h}_j\le h_j^+,
\quad
\overline{\lambda}_j\le\lambda_j^+,
\quad
\overline{D}_j\le D_j^+,
\quad
\overline{\Delta}_j\le\Delta_j^+,
```

and the strict pressure inequality

```math
a_j^-s_j^-
>
e_j^+ + h_j^+ + \lambda_j^+ + D_j^+
+2\ell_j\Delta_j^+
+4\ell_jm_*.
```

The source certificate is admissible only when the retained-area lower bound,
marked/KP upper bounds, and Paper-17 selected-rate debit are restrictions of
the same whole-process tower used to prove `S_j^{RLD}>0`.

### Theorem 4.6I.47z.2e.6: `AYM-CONF-PI-SRC_j` Proves `Pi_j>0`

Assume `AYM-CONF-GAMMA-MD-WORK_j` and
`AYM-CONF-PI-SRC_j(m_*)`. Then

```math
\Pi_j>0.
```

Proof.

By definition,

```math
\Pi_j
=
\underline{\alpha}_jS_j^{{\rm RLD}}
-\overline{\epsilon}_j
-\overline{h}_j
-\overline{\lambda}_j
-\overline{D}_j
-2\ell_j\overline{\Delta}_j
-4\ell_jm_*.
```

The imported lower bounds give

```math
\underline{\alpha}_jS_j^{{\rm RLD}}
\ge
a_j^-s_j^-,
```

because both factors are nonnegative and the lower bounds are positive. The
imported upper bounds give

```math
\overline{\epsilon}_j+\overline{h}_j+\overline{\lambda}_j+\overline{D}_j
+2\ell_j\overline{\Delta}_j
+4\ell_jm_*
\le
e_j^+ + h_j^+ + \lambda_j^+ + D_j^+
+2\ell_j\Delta_j^+
+4\ell_jm_*.
```

The strict pressure inequality therefore implies `Pi_j>0`. `square`

### Corollary 4.6I.47z.2e.7: Combined `S_j^{RLD}` And `Pi_j` Import

Assume `AYM-CONF-SRLD-SRC_j` and `AYM-CONF-PI-SRC_j(m_*)` hold on the same
finite window and the same frozen whole-process tower. Then

```math
S_j^{{\rm RLD}}>0,
\quad
\Pi_j>0.
```

Consequently, the arbitrary-window minimal-debit Gamma pass theorem applies
at `j`.

Proof.

Theorem 4.6I.47z.2e.2 gives `S_j^{RLD}>0`. Theorem 4.6I.47z.2e.6 gives
`Pi_j>0`. Theorem 4.6I.47z.2f then applies. `square`

### Corollary 4.6I.47z.2e.8: Cofinal Pressure-Surplus Source Import

If `AYM-CONF-PI-SRC_j(m_*)` holds for every cofinal `j`, then `Pi_j>0`
holds for every cofinal `j`.

A compact tail version is available when there are constants `J_P`,
`a_P>0`, `s_P>0`, `b_P>=0`, and `Delta_P>=0` such that, for all `j>=J_P`,

```math
\underline{\alpha}_j\ge a_P,
\quad
\frac{S_j^{{\rm RLD}}}{\ell_j}\ge s_P,
```

```math
\frac{\overline{\epsilon}_j+\overline{h}_j+\overline{\lambda}_j+\overline{D}_j}
{2\ell_j}
\le b_P,
\quad
\overline{\Delta}_j\le\Delta_P,
```

and

```math
\frac{a_Ps_P}{2}
-b_P
-\Delta_P
>
2m_*
>
0.
```

Then `Pi_j>0` on the cofinal tail, with finite-prefix windows checked by
the finite-window source certificate.

Proof.

For `j>=J_P`, the tail bounds imply

```math
\frac{\Pi_j}{2\ell_j}
=
\frac{\underline{\alpha}_jS_j^{{\rm RLD}}}{2\ell_j}
-\frac{\overline{\epsilon}_j+\overline{h}_j+\overline{\lambda}_j+\overline{D}_j}
{2\ell_j}
-\overline{\Delta}_j
-2m_*
```

and therefore

```math
\frac{\Pi_j}{2\ell_j}
\ge
\frac{a_Ps_P}{2}
-b_P
-\Delta_P
-2m_*
>
0.
```

Since `ell_j>0`, this gives `Pi_j>0`. The finite prefix is handled by the
pointwise `AYM-CONF-PI-SRC_j(m_*)` certificates. `square`

### Corollary 4.6I.47z.2e.9: First Real Pressure-Surplus Obstruction

After `S_j^{RLD}>0` has been proved, the second actual-confinement attack is
the strict scalar inequality

```math
\underline{\alpha}_jS_j^{{\rm RLD}}
>
\overline{\epsilon}_j
+\overline{h}_j
+\overline{\lambda}_j
+\overline{D}_j
+2\ell_j\overline{\Delta}_j
+4\ell_jm_*.
```

If the imported bounds do not make this strict, then the obstruction is no
longer reserve survival. It is one of:

```text
retained-area lower bound underline alpha_j too small,
minimal-debit reserve S_j^RLD too small after multiplication by alpha_j,
marked local loss overline epsilon_j too large,
marked KP height overline h_j too large,
marked activity overline lambda_j too large,
KP threshold overline D_j too large,
Paper-17 selected-rate debit overline Delta_j too large,
target rate m_* too large for the chosen ell_j,
or same-ledger mismatch.
```

This is the exact pressure-surplus obstruction for Paper 18's finite-window
Gamma route.

### Definition 4.6I.47z.2e.10: Actual Reserve-Loop Certificate `AYM-CONF-ACT-RLD_j`

For a cofinal window `j`, `AYM-CONF-ACT-RLD_j` is the exact same-ledger
reserve-loop certificate

```math
\gamma_{15,j}\underline{M}_j-\overline{\epsilon}_{15,j}
>
2\max\left\{
\overline{E}_j,
\frac{4\overline{\omega}_j}{\underline{\kappa}_j}
\right\}.
```

It is admissible only when every quantity in the display is computed from
the actual continuum `4D SU(N)` whole-process Wilson-loop law restricted to
the same finite window, the same Paper-15/Paper-16 reserve readout, and the
same loop-modulus readout.

### Theorem 4.6I.47z.2e.11: Actual Reserve-Loop Certificate Proves `S_j^{RLD}>0`

Assume `AYM-CONF-GAMMA-MD-WORK_j` and `AYM-CONF-ACT-RLD_j`. Then

```math
S_j^{{\rm RLD}}>0.
```

Proof.

In `AYM-CONF-GAMMA-MD-WORK_j`,

```math
S_j^{{\rm RLD}}
=
\gamma_{15,j}\underline{M}_j
-\overline{\epsilon}_{15,j}
-2\max\left\{
\overline{E}_j,
\frac{4\overline{\omega}_j}{\underline{\kappa}_j}
\right\}.
```

The strict inequality in `AYM-CONF-ACT-RLD_j` says exactly that the
right-hand side is positive. `square`

### Definition 4.6I.47z.2e.12: Actual Pressure Certificate `AYM-CONF-ACT-PI_j(m_*)`

After `AYM-CONF-ACT-RLD_j` has supplied `S_j^{RLD}>0`,
`AYM-CONF-ACT-PI_j(m_*)` is the exact pressure certificate

```math
\underline{\alpha}_jS_j^{{\rm RLD}}
>
\overline{\epsilon}_j
+\overline{h}_j
+\overline{\lambda}_j
+\overline{D}_j
+2\ell_j\overline{\Delta}_j
+4\ell_jm_*.
```

The certificate is admissible only when the retained-area lower bound,
marked/KP loss bounds, Paper-17 selected-rate debit, and target scale
`ell_j` are all read from the same frozen actual continuum tower as
`AYM-CONF-ACT-RLD_j`.

### Theorem 4.6I.47z.2e.13: Actual Pressure Certificate Proves `Pi_j>0`

Assume `AYM-CONF-GAMMA-MD-WORK_j` and
`AYM-CONF-ACT-PI_j(m_*)`. Then

```math
\Pi_j>0.
```

Proof.

This is Theorem 4.6I.47z.2e.0 applied to the actual pressure certificate.
`square`

### Definition 4.6I.47z.2e.14: Actual Same-Ledger Certificate `AYM-CONF-ACT-LEDGER_j`

`AYM-CONF-ACT-LEDGER_j` holds when the two actual scalar inequalities above
are not assembled from incompatible estimates. Concretely, for the cofinal
window `j` there is one frozen whole-process law `Law_*`, one finite
record algebra `F_j`, and one restriction map

```math
\rho_j:\mathsf{Law}_*\to F_j
```

such that:

1. `gamma_15,j`, `underline M_j`, `overline epsilon_15,j`,
   `overline E_j`, `overline omega_j`, and `underline kappa_j` are all
   functions of `rho_j(Law_*)` and the declared Paper-15/Paper-16 reserve
   and loop-modulus instruments;
2. `underline alpha_j`, `overline epsilon_j`, `overline h_j`,
   `overline lambda_j`, `overline D_j`, and `overline Delta_j` are functions
   of the same `rho_j(Law_*)`, the declared marked endpoint protocol, and
   the Paper-17 selected-rate battery;
3. every loss term is included exactly once in the debit ledger and no loss
   term is imported from a different regulator, gauge chart, volume
   sequence, or smearing family;
4. the loop family used in the Creutz readout is the same finite loop family
   used in the marked endpoint bridge after the declared boundary
   restriction maps.

This is the Barandes-aligned compatibility clause: the primitive object is
the scalar whole-process record law. Gauge charts, heat-kernel coordinates,
strong-coupling expansions, endpoint labels, and RG transport devices are
admissible only as calculations that export these scalar records.

### Definition 4.6I.47z.2e.15: Actual Cofinal Constant Certificate `AYM-CONF-ACT-COF(m_*)`

`AYM-CONF-ACT-COF(m_*)` holds when there is a cofinal subsequence of windows
`j` such that, for every window in the subsequence,

```text
AYM-CONF-GAMMA-MD-WORK_j,
AYM-CONF-ACT-LEDGER_j,
AYM-CONF-ACT-RLD_j,
AYM-CONF-ACT-PI_j(m_*)
```

all hold.

Equivalently, finite-prefix exceptions are allowed only when the declared
cofinal subsequence starts after them and the omitted finite prefix is not
used to prove the physical infimum. If the proof uses every sufficiently
large scale, the certificate may be recorded as a tail certificate
`AYM-CONF-ACT-TAIL(J_*,m_*)`.

### Theorem 4.6I.47z.2e.16: Four Actual Constants Close The Minimal-Debit Gamma Route

Assume `AYM-CONF-ACT-COF(m_*)`. Then, on the declared cofinal subsequence,

```math
S_j^{{\rm RLD}}>0,
\quad
\Pi_j>0,
```

and therefore

```text
AYM-CONF-GAMMA-FW-DIRECT(m_*).
```

Consequently, the Paper-18 Gamma-rate source closes on that cofinal
subsequence, reindexed as the declared cofinal window family.

Proof.

Fix a cofinal window `j` in the declared subsequence. The same-ledger
certificate makes the constants in `AYM-CONF-ACT-RLD_j` and
`AYM-CONF-ACT-PI_j(m_*)` admissible inputs to
`AYM-CONF-GAMMA-MD-WORK_j`. Theorem 4.6I.47z.2e.11 gives
`S_j^{RLD}>0`. Theorem 4.6I.47z.2e.13 gives `Pi_j>0`. The arbitrary-window
minimal-debit Gamma pass, Theorem 4.6I.47z.2f, then supplies a legal
loop-modulus debit and the rate inequality `r_j>=2m_*>0` for this window.
Since the subsequence is cofinal, it may be used as the declared cofinal
window family. The pointwise certificates therefore assemble into
`AYM-CONF-GAMMA-FW-DIRECT(m_*)` on that reindexed family. `square`

### Corollary 4.6I.47z.2e.17: Actual Constant Obstruction

At this stage the remaining actual `4D SU(N)` problem is exactly one of the
following four failures:

| Step | Certificate | Failure meaning |
| --- | --- | --- |
| 1 | `AYM-CONF-ACT-RLD_j` | the reserve left after minimal loop-modulus debit is not positive |
| 2 | `AYM-CONF-ACT-PI_j(m_*)` | the retained reserve is positive but too small to pay marked/KP, Paper-17, and target-rate debits |
| 3 | `AYM-CONF-ACT-LEDGER_j` | the constants do not come from one frozen whole-process record law |
| 4 | `AYM-CONF-ACT-COF(m_*)` | finite-window successes do not survive along a cofinal sequence |

This corollary is deliberately narrow. It does not claim an unconditional
proof of confinement. It says that Paper 18 has reduced the remaining
confinement-rate source to four scalar record-law tasks on the actual
continuum trajectory.

### Definition 4.6I.47z.2e.18: Actual Constant Worksheet `AYM-CONF-ACT-WORK_j`

For one generic cofinal window `j`, the actual-constant worksheet is the
finite table of scalar record constants needed to evaluate `S_j^{RLD}` and
`Pi_j`. It is not a new assumption; it is the bookkeeping format in which an
actual `4D SU(N)` proof must deliver its estimates.

| Block | Constant | Certified direction | Source instrument |
| --- | --- | --- | --- |
| reserve calibration | `gamma_15,j` | lower bound | Paper-15/Paper-16 Creutz normalization readout |
| raw transported reserve | `M_SUB,j` | lower bound | actual Wilson-loop law restricted to the Paper-15 battery |
| battery loss | `L_bat,j` | upper bound | finite-battery projection/embedding ledger |
| regulator loss | `L_reg,j` | upper bound | regulator and heat-kernel transport ledger |
| volume loss | `L_vol,j` | upper bound | finite-volume to selected-window restriction |
| shape loss | `L_shape,j` | upper bound | rectangular/block-face and endpoint-closure replacement |
| reserve readout loss | `epsilon_15,j` | upper bound | counterterm/projection/window readout ledger |
| loop readout error | `E_j` | upper bound | loop-modulus readout ledger |
| loop-continuity modulus | `omega_j` | upper bound | Paper-16 loop-continuity export |
| Creutz denominator | `kappa_j` | lower bound | positive slot denominator in the same finite window |
| retained-area conversion | `alpha_j` | lower bound | marked endpoint geometry |
| marked local loss | `epsilon_j` | upper bound | endpoint/collar/counterterm/projection ledger |
| marked KP height | `h_j` | upper bound | endpoint-enlarged KP ledger |
| marked activity | `lambda_j` | upper bound | endpoint-enlarged polymer activity ledger |
| KP threshold debit | `D_j` | upper bound | marked KP threshold |
| Paper-17 selected-rate debit | `Delta_j` | upper bound | Paper-17 mass-gap battery |
| scale | `ell_j` | exact positive value | cofinal window schedule |

The reserve part of the worksheet is evaluated by

```math
\underline{M}_j
:=
\underline{M}_{{\rm SUB},j}
-\overline{L}_{{\rm bat},j}
-\overline{L}_{{\rm reg},j}
-\overline{L}_{{\rm vol},j}
-\overline{L}_{{\rm shape},j}.
```

The worksheet is admissible only if all rows are same-ledger tagged in the
sense of `AYM-CONF-ACT-LEDGER_j`.

### Definition 4.6I.47z.2e.19: Reserve-Loop Worksheet Margin `AYM-CONF-ACT-RLD-WORK_j`

`AYM-CONF-ACT-RLD-WORK_j` is the reserve-loop part of
`AYM-CONF-ACT-WORK_j`. It supplies certified bounds

```math
\gamma_{15,j}\ge\gamma_j^- >0,
\quad
\underline{M}_{{\rm SUB},j}\ge M_{{\rm SUB},j}^-,
\quad
\overline{L}_{{\rm bat},j}\le L_{{\rm bat},j}^+,
```

```math
\overline{L}_{{\rm reg},j}\le L_{{\rm reg},j}^+,
\quad
\overline{L}_{{\rm vol},j}\le L_{{\rm vol},j}^+,
\quad
\overline{L}_{{\rm shape},j}\le L_{{\rm shape},j}^+,
```

```math
\overline{\epsilon}_{15,j}\le e_{15,j}^+,
\quad
\overline{E}_j\le E_j^+,
\quad
\overline{\omega}_j\le\omega_j^+,
\quad
\underline{\kappa}_j\ge\kappa_j^- >0.
```

All upper-bound constants in this display are required to be finite and
nonnegative.

Define the certified reserve lower bound

```math
M_j^-
:=
M_{{\rm SUB},j}^-
-L_{{\rm bat},j}^+
-L_{{\rm reg},j}^+
-L_{{\rm vol},j}^+
-L_{{\rm shape},j}^+,
```

the certified reserve numerator

```math
R_j^-
:=
\gamma_j^-M_j^- - e_{15,j}^+,
```

the certified minimal loop debit

```math
B_j^+
:=
2\max\left\{
E_j^+,
\frac{4\omega_j^+}{\kappa_j^-}
\right\},
```

and the reserve-loop worksheet margin

```math
\Sigma_j^{{\rm RLD}}
:=
R_j^- - B_j^+.
```

The worksheet passes at `j` when

```math
M_j^- >0,
\quad
\Sigma_j^{{\rm RLD}}>0.
```

### Theorem 4.6I.47z.2e.20: Reserve-Loop Worksheet Proves `AYM-CONF-ACT-RLD_j`

Assume `AYM-CONF-GAMMA-MD-WORK_j`, `AYM-CONF-ACT-LEDGER_j`, and
`AYM-CONF-ACT-RLD-WORK_j`. If

```math
M_j^- >0,
\quad
\Sigma_j^{{\rm RLD}}>0,
```

then `AYM-CONF-ACT-RLD_j` holds and, more quantitatively,

```math
S_j^{{\rm RLD}}\ge\Sigma_j^{{\rm RLD}}>0.
```

Proof.

The loss bounds give

```math
\underline{M}_j
\ge
M_j^-.
```

The reserve bounds therefore give

```math
\gamma_{15,j}\underline{M}_j-\overline{\epsilon}_{15,j}
\ge
\gamma_j^-M_j^- - e_{15,j}^+
=
R_j^-.
```

The loop bounds and `kappa_j^- >0` give

```math
2\max\left\{
\overline{E}_j,
\frac{4\overline{\omega}_j}{\underline{\kappa}_j}
\right\}
\le
2\max\left\{
E_j^+,
\frac{4\omega_j^+}{\kappa_j^-}
\right\}
=
B_j^+.
```

Subtracting the second estimate from the first gives

```math
S_j^{{\rm RLD}}
\ge
R_j^- - B_j^+
=
\Sigma_j^{{\rm RLD}}
>
0.
```

Thus the exact reserve-loop inequality `AYM-CONF-ACT-RLD_j` holds. `square`

### Corollary 4.6I.47z.2e.21: Reserve-Loop Attack Outcome

For a fixed cofinal window `j`, the reserve-loop attack has three honest
outcomes:

1. **Pass:** `Sigma_j^{RLD}>0`. Then Theorem 4.6I.47z.2e.20 proves
   `AYM-CONF-ACT-RLD_j` and gives the explicit lower bound
   `S_j^{RLD}>=Sigma_j^{RLD}`.
2. **Undecided:** the available bounds give `Sigma_j^{RLD}<=0`, but no
   upper-bound calculation proves the exact reserve-loop surplus impossible.
   Then the current estimates are too weak.
3. **Instrument falsification:** a same-ledger upper reserve bound
   `R_j^+` and lower loop debit `B_j^-` prove `R_j^+<=B_j^-`. Then the
   chosen window, readout, and debit instruments cannot prove
   `AYM-CONF-ACT-RLD_j`; the proof must change instruments, windows, or
   target subsequence.

This is the first real mathematical attack on the actual `4D SU(N)`
constants. It is deliberately local in `j`; cofinal confinement requires
the same pass, or a reindexed cofinal pass, along an unbounded window family.

### Definition 4.6I.47z.2e.21a: Tail Reserve-Loop Positivity `AYM-CONF-ACT-RLD-TAIL`

`AYM-CONF-ACT-RLD-TAIL` is the tail version of the reserve-loop attack. It
holds when there is a tail start `J_R` such that `AYM-CONF-ACT-RLD-WORK_j`
is available for every declared window `j>=J_R` and

```math
\Sigma_j^{{\rm RLD}}>0
```

for every such `j`.

A uniform tail pass is the stronger certificate that there is an `s_R>0`
such that

```math
\Sigma_j^{{\rm RLD}}\ge s_R
```

for every `j>=J_R`. A reindexed cofinal pass is the weaker certificate that
there is a cofinal subsequence `j_n` with

```math
\Sigma_{j_n}^{{\rm RLD}}>0
```

for every `n`.

### Theorem 4.6I.47z.2e.21b: Uniform Reserve-Debit Gap Proves Tail Positivity

Assume that, for all `j>=J_R`, `AYM-CONF-ACT-RLD-WORK_j` holds and there
are constants `R_R`, `B_R`, and `s_R>0` such that

```math
R_j^-\ge R_R,
\quad
B_j^+\le B_R,
\quad
R_R-B_R\ge s_R>0.
```

Then `AYM-CONF-ACT-RLD-TAIL` holds, and in fact

```math
\Sigma_j^{{\rm RLD}}\ge s_R
```

for every `j>=J_R`.

Proof.

For `j>=J_R`,

```math
\Sigma_j^{{\rm RLD}}
=
R_j^- - B_j^+
\ge
R_R-B_R
\ge
s_R
>
0.
```

This is the uniform tail pass. `square`

### Theorem 4.6I.47z.2e.21c: Asymptotic Dominance Proves Cofinal Reserve-Loop Positivity

Suppose there are a positive scale `c_j>0`, a tail start `J_R`, and constants
`r_R>b_R` such that, for all `j>=J_R`,

```math
R_j^-\ge c_j r_R,
\quad
B_j^+\le c_j b_R.
```

Then `AYM-CONF-ACT-RLD-TAIL` holds on that tail:

```math
\Sigma_j^{{\rm RLD}}
\ge
c_j(r_R-b_R)
>
0.
```

If the two inequalities hold only on a cofinal subsequence `j_n`, then the
same conclusion holds after reindexing that subsequence as the declared
cofinal reserve-loop family.

Proof.

The first statement follows by subtraction:

```math
\Sigma_j^{{\rm RLD}}
=
R_j^- - B_j^+
\ge
c_j(r_R-b_R).
```

Since `c_j>0` and `r_R>b_R`, the right-hand side is positive. The
subsequence statement is identical after replacing `j` by `j_n`. `square`

### Definition 4.6I.47z.2e.21d: Reserve-Loop Falsification Ledger `AYM-CONF-ACT-RLD-FALS_j`

For a fixed window `j`, `AYM-CONF-ACT-RLD-FALS_j` is the same-ledger
certificate that the chosen reserve-loop instruments cannot pass. It
consists of an upper reserve numerator `R_j^+` and a lower loop debit
`B_j^-` such that

```math
\gamma_{15,j}\underline{M}_j-\overline{\epsilon}_{15,j}\le R_j^+,
```

```math
2\max\left\{
\overline{E}_j,
\frac{4\overline{\omega}_j}{\underline{\kappa}_j}
\right\}
\ge B_j^-,
```

and

```math
R_j^+\le B_j^-.
```

The certificate falsifies this instrument choice, not confinement itself.
It says that the declared window, reserve readout, loop-modulus readout, and
denominator estimate cannot produce `AYM-CONF-ACT-RLD_j`.

### Theorem 4.6I.47z.2e.21e: Reserve-Loop Falsification

If `AYM-CONF-ACT-RLD-FALS_j` holds, then `AYM-CONF-ACT-RLD_j` is false for
the declared instruments at window `j`.

Proof.

The falsification bounds give

```math
\gamma_{15,j}\underline{M}_j-\overline{\epsilon}_{15,j}
\le
R_j^+
\le
B_j^-
\le
2\max\left\{
\overline{E}_j,
\frac{4\overline{\omega}_j}{\underline{\kappa}_j}
\right\}.
```

This is the negation of the strict reserve-loop inequality required by
`AYM-CONF-ACT-RLD_j`. `square`

### Corollary 4.6I.47z.2e.21f: Reserve-Loop Tail Trichotomy

For the declared actual `4D SU(N)` reserve-loop instruments, the proof
status should be recorded in one of the following forms:

1. **Uniform tail pass:** Theorem 4.6I.47z.2e.21b supplies
   `Sigma_j^{RLD}>=s_R>0` eventually.
2. **Asymptotic or reindexed pass:** Theorem 4.6I.47z.2e.21c supplies
   `Sigma_j^{RLD}>0` eventually or on a cofinal subsequence.
3. **Instrument falsification:** Theorem 4.6I.47z.2e.21e proves that the
   declared instruments cannot pass on a tail or on infinitely many required
   windows.
4. **Undecided:** neither lower-bound positivity nor upper-bound
   falsification has been proved. Then the remaining work is to sharpen
   actual same-ledger estimates for `R_j^-` and `B_j^+`.

Thus the first bottleneck has been reduced to a genuine asymptotic
comparison:

```text
certified reserve numerator R_j^-
versus
certified loop-modulus debit B_j^+.
```

The next non-formal input is an actual continuum estimate showing which side
wins along the declared cofinal window family.

### Definition 4.6I.47z.2e.21g: Actual RLD Asymptotic Constants Ledger `AYM-CONF-ACT-RLD-ASYM`

`AYM-CONF-ACT-RLD-ASYM` is the asymptotic constants ledger for the first
reserve-loop bottleneck. It records the actual tail estimates needed to
decide whether `R_j^-` beats `B_j^+`.

| Quantity | Formula role | Required tail estimate | Source to prove/import | Failure mode |
| --- | --- | --- | --- | --- |
| `gamma_j^-` | reserve calibration multiplier | `gamma_j^- >= gamma_R >0` or a scaled product estimate for `gamma_j^- M_j^-` | Paper-15/Paper-16 Creutz normalization on same window | calibration collapse |
| `M_SUB,j^-` | raw transported reserve before losses | lower bound `M_SUB,j^- >= M_SUB,R` or scaled `>= c_j M_SUB,R` | actual Wilson-loop reserve export | no raw reserve |
| `L_bat,j^+` | finite-battery loss | upper bound `<= L_bat,R` or scaled `<= c_j l_bat` | finite-battery embedding/projection ledger | battery loss eats reserve |
| `L_reg,j^+` | regulator/heat-kernel transport loss | upper bound `<= L_reg,R` or scaled `<= c_j l_reg` | Paper-16 regulator transport ledger | regulator loss eats reserve |
| `L_vol,j^+` | finite-volume/window restriction loss | upper bound `<= L_vol,R` or scaled `<= c_j l_vol` | volume restriction ledger | volume loss eats reserve |
| `L_shape,j^+` | shape and endpoint-closure replacement loss | upper bound `<= L_shape,R` or scaled `<= c_j l_shape` | loop-window scheduler | shape loss eats reserve |
| `e_15,j^+` | reserve readout loss | upper bound `<= e_R` or scaled `<= c_j e_R` | counterterm/projection/window readout ledger | readout loss eats reserve |
| `E_j^+` | loop readout error | upper bound `<= E_R` or scaled `<= c_j E_R` | loop-modulus readout ledger | direct loop debit too large |
| `omega_j^+` | loop-continuity modulus | upper bound `<= omega_R` or scaled `<= c_j omega_R` | Paper-16 loop-continuity export | continuity debit too large |
| `kappa_j^-` | Creutz-slot denominator | lower bound `>= kappa_R>0` or scaled denominator control | positive slot denominator ledger | denominator collapse |

The ledger has not proved the actual constants. It states exactly what an
actual continuum `4D SU(N)` estimate must supply to decide the first
bottleneck.

### Definition 4.6I.47z.2e.21h: Reserve Numerator Lower-Bound Attack `AYM-CONF-ACT-RNUM-TAIL`

`AYM-CONF-ACT-RNUM-TAIL` holds on a tail `j>=J_R` when there are constants

```math
\gamma_R>0,
\quad
M_{{\rm SUB},R},
\quad
L_{{\rm bat},R}\ge0,
\quad
L_{{\rm reg},R}\ge0,
```

```math
L_{{\rm vol},R}\ge0,
\quad
L_{{\rm shape},R}\ge0,
\quad
e_R\ge0
```

such that, for all `j>=J_R`,

```math
\gamma_j^-\ge\gamma_R,
\quad
M_{{\rm SUB},j}^-\ge M_{{\rm SUB},R},
```

```math
L_{{\rm bat},j}^+\le L_{{\rm bat},R},
\quad
L_{{\rm reg},j}^+\le L_{{\rm reg},R},
```

```math
L_{{\rm vol},j}^+\le L_{{\rm vol},R},
\quad
L_{{\rm shape},j}^+\le L_{{\rm shape},R},
\quad
e_{15,j}^+\le e_R.
```

Define

```math
M_R
:=
M_{{\rm SUB},R}
-L_{{\rm bat},R}
-L_{{\rm reg},R}
-L_{{\rm vol},R}
-L_{{\rm shape},R},
```

and

```math
R_R
:=
\gamma_RM_R-e_R.
```

### Theorem 4.6I.47z.2e.21i: Reserve Numerator Tail Lower Bound

Assume `AYM-CONF-ACT-RNUM-TAIL`. If

```math
M_R>0,
```

then, for every `j>=J_R`,

```math
M_j^-\ge M_R,
\quad
R_j^-\ge R_R.
```

If also `R_R>0`, then the certified reserve numerator is uniformly
positive on the tail.

Proof.

The loss estimates give

```math
M_j^-
=
M_{{\rm SUB},j}^-
-L_{{\rm bat},j}^+
-L_{{\rm reg},j}^+
-L_{{\rm vol},j}^+
-L_{{\rm shape},j}^+
\ge
M_R.
```

Since `gamma_j^- >= gamma_R >0`, `M_j^- >= M_R>0`, and
`e_{15,j}^+<=e_R`,

```math
R_j^-
=
\gamma_j^-M_j^- - e_{15,j}^+
\ge
\gamma_RM_R-e_R
=
R_R.
```

The final statement is immediate. `square`

### Definition 4.6I.47z.2e.21j: Loop-Debit Upper-Bound Attack `AYM-CONF-ACT-BDEB-TAIL`

`AYM-CONF-ACT-BDEB-TAIL` holds on a tail `j>=J_B` when there are constants

```math
E_R\ge0,
\quad
\omega_R\ge0,
\quad
\kappa_R>0
```

such that, for all `j>=J_B`,

```math
E_j^+\le E_R,
\quad
\omega_j^+\le\omega_R,
\quad
\kappa_j^-\ge\kappa_R.
```

Define the tail loop debit

```math
B_R
:=
2\max\left\{
E_R,
\frac{4\omega_R}{\kappa_R}
\right\}.
```

### Theorem 4.6I.47z.2e.21k: Loop-Debit Tail Upper Bound

Assume `AYM-CONF-ACT-BDEB-TAIL`. Then, for every `j>=J_B`,

```math
B_j^+\le B_R.
```

Proof.

By definition,

```math
B_j^+
=
2\max\left\{
E_j^+,
\frac{4\omega_j^+}{\kappa_j^-}
\right\}.
```

The tail bounds give `E_j^+<=E_R` and

```math
\frac{4\omega_j^+}{\kappa_j^-}
\le
\frac{4\omega_R}{\kappa_R}.
```

Taking the maximum and multiplying by `2` gives the claim. `square`

### Theorem 4.6I.47z.2e.21l: First Tail Reserve-Loop Inequality

Assume `AYM-CONF-ACT-RNUM-TAIL` and `AYM-CONF-ACT-BDEB-TAIL`. Let

```math
J_*:=\max\{J_R,J_B\}.
```

If

```math
M_R>0,
\quad
R_R-B_R\ge s_R>0,
```

then `AYM-CONF-ACT-RLD-TAIL` holds on the tail `j>=J_*`, with

```math
\Sigma_j^{{\rm RLD}}\ge s_R>0.
```

Proof.

For `j>=J_*`, Theorem 4.6I.47z.2e.21i gives `R_j^- >= R_R`, and Theorem
4.6I.47z.2e.21k gives `B_j^+ <= B_R`. Therefore

```math
\Sigma_j^{{\rm RLD}}
=
R_j^- - B_j^+
\ge
R_R-B_R
\ge
s_R
>
0.
```

This is exactly the uniform tail reserve-loop pass. `square`

### Corollary 4.6I.47z.2e.21m: First Tail RLD Decision

The first tail inequality is now the single scalar comparison

```math
\gamma_R
\left(
M_{{\rm SUB},R}
-L_{{\rm bat},R}
-L_{{\rm reg},R}
-L_{{\rm vol},R}
-L_{{\rm shape},R}
\right)
-e_R
>
2\max\left\{
E_R,
\frac{4\omega_R}{\kappa_R}
\right\}.
```

If this strict inequality is proved, the reserve-loop tail passes. If it is
falsified by same-ledger upper reserve and lower debit bounds, the declared
reserve-loop instruments fail. If neither direction is proved, the first
actual asymptotic bottleneck remains open.

### Definition 4.6I.47z.2e.21n: Actual Step-1 Source Attack `AYM-CONF-ACT-RLD-SRC-ATTACK`

`AYM-CONF-ACT-RLD-SRC-ATTACK` is the source-level version of the first
reserve-loop bottleneck. It does not merely name the worksheet constants;
it asks whether the actual continuum tower supplies constants that make the
tail gap positive.

It holds on a tail `j>=J_S` when the same frozen whole-process tower
supplies constants

```math
\gamma_R>0,
\quad
C_R\ge0,
\quad
L_{{\rm bat},R},L_{{\rm reg},R},L_{{\rm vol},R},L_{{\rm shape},R}\ge0,
```

```math
e_R,E_R,\omega_R\ge0,
\quad
\kappa_R>0
```

such that, for every `j>=J_S`,

```math
\gamma_j^-\ge\gamma_R,
\quad
M_{{\rm SUB},j}^-\ge C_R,
```

```math
L_{{\rm bat},j}^+\le L_{{\rm bat},R},
\quad
L_{{\rm reg},j}^+\le L_{{\rm reg},R},
```

```math
L_{{\rm vol},j}^+\le L_{{\rm vol},R},
\quad
L_{{\rm shape},j}^+\le L_{{\rm shape},R},
\quad
e_{15,j}^+\le e_R,
```

and

```math
E_j^+\le E_R,
\quad
\omega_j^+\le\omega_R,
\quad
\kappa_j^-\ge\kappa_R.
```

Define the total extraction loss

```math
L_R
:=
L_{{\rm bat},R}
+L_{{\rm reg},R}
+L_{{\rm vol},R}
+L_{{\rm shape},R},
```

the source reserve after extraction

```math
N_R:=C_R-L_R,
```

the source reserve numerator

```math
R_R^{{\rm src}}
:=
\gamma_RN_R-e_R,
```

the source loop debit

```math
B_R^{{\rm src}}
:=
2\max\left\{
E_R,
\frac{4\omega_R}{\kappa_R}
\right\},
```

and the source reserve-loop margin

```math
S_R^{{\rm src}}
:=
R_R^{{\rm src}}-B_R^{{\rm src}}.
```

This is the sharp place where actual four-dimensional Yang-Mills enters
step 1. The constant `C_R` is the transported raw Wilson-loop reserve. The
four `L` constants are the finite-battery, regulator, volume, and shape
losses needed to read that reserve in the Paper-18 window. The constants
`E_R`, `omega_R`, and `kappa_R` are the loop-modulus debit data. All of them
must be measured on the same record law.

### Theorem 4.6I.47z.2e.21o: Source Step-1 Gap Proves Tail RLD

Assume `AYM-CONF-ACT-RLD-SRC-ATTACK`. If

```math
N_R>0,
\quad
S_R^{{\rm src}}\ge s_R>0,
```

then `AYM-CONF-ACT-RLD-TAIL` holds on the tail `j>=J_S`, with

```math
\Sigma_j^{{\rm RLD}}\ge s_R>0.
```

Proof.

The source estimates imply `AYM-CONF-ACT-RNUM-TAIL` with
`M_SUB,R=C_R` and the four displayed loss bounds. Therefore

```math
M_R=C_R-L_R=N_R,
\quad
R_R=\gamma_RN_R-e_R=R_R^{{\rm src}}.
```

They also imply `AYM-CONF-ACT-BDEB-TAIL`, with

```math
B_R=B_R^{{\rm src}}.
```

Thus

```math
R_R-B_R
=
R_R^{{\rm src}}-B_R^{{\rm src}}
=
S_R^{{\rm src}}
\ge
s_R
>
0.
```

Theorem 4.6I.47z.2e.21l applies and proves the tail reserve-loop pass.
`square`

### Definition 4.6I.47z.2e.21p: Actual Step-1 Source Falsification `AYM-CONF-ACT-RLD-SRC-FALS`

`AYM-CONF-ACT-RLD-SRC-FALS` is the same-ledger certificate that the chosen
absolute-tail step-1 route cannot work. It consists of tail constants

```math
\gamma_R^+ >0,
\quad
C_R^+\ge0,
\quad
L_R^-\ge0,
\quad
e_R^-\ge0,
```

```math
E_R^-\ge0,
\quad
\omega_R^-\ge0,
\quad
\kappa_R^+ >0
```

such that, on a tail, the exact reserve numerator is bounded above by

```math
\gamma_{15,j}\underline{M}_j-\overline{\epsilon}_{15,j}
\le
\gamma_R^+\max\{C_R^+-L_R^-,0\}-e_R^-,
```

and the loop debit is bounded below by

```math
2\max\left\{
\overline{E}_j,
\frac{4\overline{\omega}_j}{\underline{\kappa}_j}
\right\}
\ge
2\max\left\{
E_R^-,
\frac{4\omega_R^-}{\kappa_R^+}
\right\}.
```

Define

```math
R_R^+
:=
\gamma_R^+\max\{C_R^+-L_R^-,0\}-e_R^-,
```

and

```math
B_R^-
:=
2\max\left\{
E_R^-,
\frac{4\omega_R^-}{\kappa_R^+}
\right\}.
```

The falsification condition is

```math
R_R^+\le B_R^-.
```

This falsifies only the declared absolute-tail reserve-loop route. It does
not rule out a finite-window route, a reindexed route, or a different
normalization.

### Theorem 4.6I.47z.2e.21q: Source Step-1 Falsification

If `AYM-CONF-ACT-RLD-SRC-FALS` holds, then the declared absolute-tail
source constants cannot prove `AYM-CONF-ACT-RLD-TAIL`.

Proof.

On the falsified tail,

```math
\gamma_{15,j}\underline{M}_j-\overline{\epsilon}_{15,j}
\le
R_R^+
\le
B_R^-
\le
2\max\left\{
\overline{E}_j,
\frac{4\overline{\omega}_j}{\underline{\kappa}_j}
\right\}.
```

Therefore the strict reserve-loop inequality required by
`AYM-CONF-ACT-RLD_j` cannot hold on that tail for the declared instruments.
Consequently the absolute-tail version of `AYM-CONF-ACT-RLD-TAIL` is
blocked. `square`

### Corollary 4.6I.47z.2e.21r: Step-1 Attack Reduction

The first actual bottleneck has now been reduced to one scalar source
comparison:

```math
\gamma_R
\left(
C_R
-L_{{\rm bat},R}
-L_{{\rm reg},R}
-L_{{\rm vol},R}
-L_{{\rm shape},R}
\right)
-e_R
>
2\max\left\{
E_R,
\frac{4\omega_R}{\kappa_R}
\right\}.
```

If this inequality is proved on the frozen continuum tower, step 1 passes.
If `AYM-CONF-ACT-RLD-SRC-FALS` is proved, the absolute-tail step-1 route
fails and Paper 18 must use a finite-window, reindexed, or normalized Gamma
route. If neither side is proved, the obstruction is now completely
localized: actual continuum estimates for raw reserve, extraction losses,
loop readout, loop continuity, and Creutz-slot denominators are still too
weak to decide step 1.

### Definition 4.6I.47z.2e.21s: Step-1 Threshold Form `AYM-CONF-ACT-RLD-THRESH`

For the source constants in `AYM-CONF-ACT-RLD-SRC-ATTACK`, define the total
loop-modulus debit

```math
D_R^{{\rm loop}}
:=
2\max\left\{
E_R,
\frac{4\omega_R}{\kappa_R}
\right\},
```

the total non-raw-reserve debit

```math
D_R^{{\rm tot}}
:=
e_R+D_R^{{\rm loop}},
```

and, for a demanded step-1 margin `s_R>0`, the critical raw reserve

```math
C_R^{{\rm crit}}(s_R)
:=
L_R+\frac{D_R^{{\rm tot}}+s_R}{\gamma_R}.
```

`AYM-CONF-ACT-RLD-THRESH(s_R)` is the certificate that

```math
C_R\ge C_R^{{\rm crit}}(s_R).
```

This is not a new assumption. It is the step-1 inequality solved for the
actual raw reserve `C_R`.

### Theorem 4.6I.47z.2e.21t: Threshold Form Is Equivalent To Source Step-1 Pass

Assume `AYM-CONF-ACT-RLD-SRC-ATTACK`, with `gamma_R>0`. Then, for a fixed
`s_R>0`, the inequality

```math
S_R^{{\rm src}}\ge s_R
```

is algebraically equivalent, for the declared constants, to

```math
C_R\ge C_R^{{\rm crit}}(s_R).
```

Consequently, if `AYM-CONF-ACT-RLD-THRESH(s_R)` holds and

```math
C_R>L_R,
```

then `AYM-CONF-ACT-RLD-TAIL` holds with margin `s_R`.

Proof.

By definition,

```math
S_R^{{\rm src}}
=
\gamma_R(C_R-L_R)-e_R-D_R^{{\rm loop}}
=
\gamma_R(C_R-L_R)-D_R^{{\rm tot}}.
```

Thus

```math
S_R^{{\rm src}}\ge s_R
```

is equivalent, since `gamma_R>0`, to

```math
C_R
\ge
L_R+\frac{D_R^{{\rm tot}}+s_R}{\gamma_R}
=
C_R^{{\rm crit}}(s_R).
```

If this holds and `C_R>L_R`, then `N_R=C_R-L_R>0`. Theorem
4.6I.47z.2e.21o applies. `square`

### Corollary 4.6I.47z.2e.21u: Step-1 Constants Decision Table

The source attack has the following concrete decision table. Each row is a
same-ledger estimate on the frozen continuum tower, not a new physical
object.

| Constant | Enters through | Current proof status in Paper 18 | What would prove it | What would falsify absolute-tail step 1 |
| --- | --- | --- | --- | --- |
| `gamma_R` | divides the critical reserve threshold | reducible, conditional | Paper-15/Paper-16 readout normalization gives a tail lower bound away from zero | calibration lower bound decays to zero on every admissible tail |
| `C_R` | raw transported reserve | genuinely open, decisive | an actual continuum Wilson-loop or Creutz reserve lower bound on the declared windows | upper reserve bound below `C_R^crit(s_R)` |
| `L_bat,R` | raises `L_R` | mostly reducible | finite-battery embedding/projection losses are uniformly bounded or scaled below the reserve | battery loss grows as fast as, or faster than, raw reserve |
| `L_reg,R` | raises `L_R` | reducible to Paper-16 transport, but uniform constants are conditional | regulator/heat-kernel transport has bounded same-ledger loss on the chosen tail | regulator transport loss consumes the reserve |
| `L_vol,R` | raises `L_R` | conditional | finite-volume restriction loss is uniformly bounded for the selected local window family | volume restriction loss is not controlled on any cofinal tail |
| `L_shape,R` | raises `L_R` | mostly scheduler/combinatorial | rectangle/block-face and endpoint-closure replacements have bounded shape loss | shape replacement loss grows with the cofinal windows |
| `e_R` | raises `D_R^tot` | reducible but delicate | counterterm, projection, and window readout errors have a common upper bound | readout error alone exceeds available calibrated reserve |
| `E_R` | raises direct loop debit | reducible by loop readout control | loop readout approximants make `E_R` small on the same tower | direct loop readout error remains comparable to reserve |
| `omega_R` | raises continuity debit | imported only if Paper-16 loop-continuity modulus is uniform enough | loop-continuity export gives a small same-ledger upper bound | continuity modulus stays too large on every tail |
| `kappa_R` | denominator in continuity debit | finite-window positive; tail lower bound is a real risk | Creutz-slot denominators stay bounded away from zero on the chosen tail | denominator collapses, making `4 omega_R/kappa_R` unpayable |

Therefore the first raw target is not merely `C_R>0`; it is

```math
C_R
\ge
L_R
+\frac{
e_R
+2\max\left\{
E_R,
\frac{4\omega_R}{\kappa_R}
\right\}
+s_R
}{\gamma_R}.
```

This table makes the honest status sharper. The finite-battery and
bookkeeping losses are mostly reducible. The genuinely dynamical content is
the competition between the raw reserve `C_R` and the critical threshold.
The most fragile absolute-tail constants are `C_R` itself and the denominator
lower bound `kappa_R`.

### Definition 4.6I.47z.2e.21v: Focused `C_R` And `kappa_R` Attack `AYM-CONF-ACT-CRK-FOCUS`

`AYM-CONF-ACT-CRK-FOCUS` is the narrowed step-1 campaign. It separates the
raw reserve question from the denominator question.

The raw reserve lower-bound certificate `AYM-CONF-ACT-CRES-LOW(c_R)` holds
on a tail `j>=J_C` when the frozen continuum tower proves

```math
M_{{\rm SUB},j}^-\ge c_R
```

for every `j>=J_C`.

The separated denominator certificate `AYM-CONF-ACT-KAPPA-SEP(k_R)` holds
on a tail `j>=J_K` when

```math
\kappa_j^-\ge k_R>0
```

for every `j>=J_K`.

The quotient denominator certificate `AYM-CONF-ACT-KAPPA-QUOT(W_R)` holds
on a tail `j>=J_W` when

```math
\frac{\omega_j^+}{\kappa_j^-}\le W_R
```

for every `j>=J_W`.

The quotient certificate is weaker in ontology and stronger in usefulness:
it does not assert that raw Creutz-slot denominators are uniformly separated
from zero. It asserts only that the loop-continuity debit actually entering
the scalar record inequality is bounded.

### Theorem 4.6I.47z.2e.21w: Separated Denominator Route

Assume the non-fragile constants in `AYM-CONF-ACT-RLD-SRC-ATTACK` are
available with

```math
\gamma_R>0,
\quad
L_R<\infty,
\quad
e_R<\infty,
\quad
E_R<\infty,
\quad
\omega_R<\infty.
```

Assume also `AYM-CONF-ACT-CRES-LOW(c_R)` and
`AYM-CONF-ACT-KAPPA-SEP(k_R)`. Define

```math
C_{{\rm sep}}^{{\rm crit}}(s_R,k_R)
:=
L_R+\frac{
e_R
+2\max\left\{
E_R,
\frac{4\omega_R}{k_R}
\right\}
+s_R
}{\gamma_R}.
```

If

```math
c_R\ge C_{{\rm sep}}^{{\rm crit}}(s_R,k_R),
```

then `AYM-CONF-ACT-RLD-TAIL` holds on the common tail with margin `s_R`.

Proof.

The lower bound `kappa_j^- >= k_R` and the loop-continuity upper bound
`omega_j^+ <= omega_R` imply

```math
\frac{\omega_j^+}{\kappa_j^-}
\le
\frac{\omega_R}{k_R}.
```

Thus the loop debit is bounded by the maximum appearing in
`C_sep^crit`. The raw reserve lower bound gives `C_R>=c_R`; the displayed
threshold then gives `C_R>=C_R^crit(s_R)`. Theorem 4.6I.47z.2e.21t gives
the source step-1 pass, and Theorem 4.6I.47z.2e.21o gives
`AYM-CONF-ACT-RLD-TAIL`. `square`

### Theorem 4.6I.47z.2e.21x: Quotient Denominator Route

Assume the non-fragile constants in `AYM-CONF-ACT-RLD-SRC-ATTACK` are
available with

```math
\gamma_R>0,
\quad
L_R<\infty,
\quad
e_R<\infty,
\quad
E_R<\infty.
```

Assume also `AYM-CONF-ACT-CRES-LOW(c_R)` and
`AYM-CONF-ACT-KAPPA-QUOT(W_R)`. Define

```math
C_{{\rm quot}}^{{\rm crit}}(s_R,W_R)
:=
L_R+\frac{
e_R
+2\max\left\{
E_R,
4W_R
\right\}
+s_R
}{\gamma_R}.
```

If

```math
c_R\ge C_{{\rm quot}}^{{\rm crit}}(s_R,W_R),
```

then `AYM-CONF-ACT-RLD-TAIL` holds on the common tail with margin `s_R`.

Proof.

The quotient certificate gives

```math
\frac{4\omega_j^+}{\kappa_j^-}
\le
4W_R.
```

Therefore the loop debit is bounded by

```math
2\max\left\{
E_R,
4W_R
\right\}.
```

The raw reserve lower bound and the displayed threshold give
`C_R>=C_R^crit(s_R)` with the quotient debit in place of the separated
`omega_R/kappa_R` debit. The same algebra as Theorem 4.6I.47z.2e.21t
proves `S_R^{src}>=s_R`, and Theorem 4.6I.47z.2e.21o gives
`AYM-CONF-ACT-RLD-TAIL`. `square`

### Corollary 4.6I.47z.2e.21y: Denominator Collapse Diagnostic

Suppose no positive separated denominator tail exists: for every `k_R>0`
and every tail start, some declared window has `kappa_j^-<k_R`. Then the
separated route `AYM-CONF-ACT-KAPPA-SEP(k_R)` fails.

The step-1 route is not automatically dead. It splits into two honest
options:

1. prove the quotient route `AYM-CONF-ACT-KAPPA-QUOT(W_R)` and then test
   `C_R>=C_quot^crit(s_R,W_R)`;
2. abandon the absolute-tail route and use finite-window, reindexed, or
   normalized Gamma records.

If neither a separated lower bound nor a quotient bound exists, then the
absolute-tail loop-modulus debit cannot be bounded by the current
instruments.

### Corollary 4.6I.47z.2e.21z: Narrow Step-1 Decision

After all reducible debits are fixed, the first actual decision is:

```text
Does the actual continuum tower prove either

1. kappa_j^- >= k_R > 0 and
   c_R >= C_sep^crit(s_R,k_R),

or

2. omega_j^+ / kappa_j^- <= W_R and
   c_R >= C_quot^crit(s_R,W_R)?
```

If yes, step 1 passes. If no, the absolute-tail route does not currently
close. The next honest move is then not to add more bookkeeping, but to
change the route: finite-window pass, reindexed cofinal pass, or normalized
record pass.

### Definition 4.6I.47z.2e.21aa: Quotient Control From Loop-Modulus Machinery `AYM-CONF-ACT-KQ-LMOD(W_R)`

`AYM-CONF-ACT-KQ-LMOD(W_R)` is the explicit derivation of
`AYM-CONF-ACT-KAPPA-QUOT(W_R)` from the existing Paper-16 loop-continuity
and Paper-18 loop-modulus ledgers. It holds on a tail `j>=J_Q` when the
following data live on the same frozen whole-process tower.

1. The Paper-18 slot lower-bound ledger supplies

   ```math
   K_j^{{\rm slot}}>0,
   \quad
   0<\rho_j<K_j^{{\rm slot}},
   \quad
   \kappa_j^-:=K_j^{{\rm slot}}-\rho_j.
   ```

2. The Paper-16/Paper-12 loop-continuity and transport ledger supplies a
   cutoff selector `alpha_Q(j)` and a nonnegative error budget

   ```math
   \Omega_j(\alpha_Q(j))
   =
   \varepsilon_{{\rm slot},j}(\alpha_Q(j))
   +\varepsilon_{{\rm shape},j}(\alpha_Q(j))
   +\varepsilon_{{\rm ren},j}(\alpha_Q(j))
   +\varepsilon_{{\rm vol},j}(\alpha_Q(j))
   +\varepsilon_{{\rm reg},j}(\alpha_Q(j))
   +\varepsilon_{{\rm proj},j}(\alpha_Q(j))
   ```

   with

   ```math
   \omega_j^+\le \Omega_j(\alpha_Q(j)).
   ```

3. The quotient-control inequality holds:

   ```math
   \Omega_j(\alpha_Q(j))
   \le
   W_R\left(K_j^{{\rm slot}}-\rho_j\right).
   ```

The selector `alpha_Q(j)` may depend on the finite window. This is allowed:
the quotient route asks for one whole-process tower with a declared cofinal
cutoff selector, not for a window-independent finite cutoff.

### Theorem 4.6I.47z.2e.21ab: Loop-Modulus Quotient Criterion Proves `AYM-CONF-ACT-KAPPA-QUOT(W_R)`

If `AYM-CONF-ACT-KQ-LMOD(W_R)` holds, then
`AYM-CONF-ACT-KAPPA-QUOT(W_R)` holds on the same tail.

Proof.

For every `j>=J_Q`, clause 1 gives

```math
\kappa_j^-=K_j^{{\rm slot}}-\rho_j>0.
```

Clauses 2 and 3 give

```math
\omega_j^+
\le
\Omega_j(\alpha_Q(j))
\le
W_R\left(K_j^{{\rm slot}}-\rho_j\right)
=
W_R\kappa_j^-.
```

Dividing by `kappa_j^- >0` gives

```math
\frac{\omega_j^+}{\kappa_j^-}\le W_R.
```

This is exactly `AYM-CONF-ACT-KAPPA-QUOT(W_R)`. `square`

### Corollary 4.6I.47z.2e.21ac: Adaptive Paper-16 Selector Criterion

Assume the Paper-18 slot ledger gives a positive finite-window denominator

```math
\kappa_j^-=K_j^{{\rm slot}}-\rho_j>0
```

for every declared tail window. Assume Paper 16 loop-continuity gives
cutoff-dependent budgets `Omega_j(alpha)` with

```math
\Omega_j(\alpha)\to0
```

as `alpha` advances along the frozen tower, for each fixed `j`. If there is
a cofinal selector `alpha_Q(j)` such that

```math
\Omega_j(\alpha_Q(j))\le W_R\kappa_j^-,
```

then `AYM-CONF-ACT-KAPPA-QUOT(W_R)` holds.

This criterion is the practical use of Paper 16. Even if raw denominators
shrink with the window, the quotient route can survive if the cutoff
selector drives loop-continuity errors down at least proportionally to the
declared denominator.

### Corollary 4.6I.47z.2e.21ad: Quotient-Control Failure

For the declared slot schedule and frozen tower, the quotient route fails
if, for every finite `W_R` and every cofinal cutoff selector, there are
arbitrarily large declared windows with

```math
\Omega_j(\alpha_Q(j))
>
W_R\left(K_j^{{\rm slot}}-\rho_j\right).
```

In that case `AYM-CONF-ACT-KAPPA-QUOT(W_R)` cannot be proved from the
current Paper-16/Paper-18 loop-modulus machinery. The remaining options are
finite-window verification, reindexed cofinal windows, normalized records,
or a stronger loop-continuity theorem.

### Corollary 4.6I.47z.2e.21ae: Step-1 Quotient-Control Target

Combining Theorem 4.6I.47z.2e.21ab with Theorem 4.6I.47z.2e.21x, the
quotient route closes step 1 if the same frozen tower supplies

```text
AYM-CONF-ACT-CRES-LOW(c_R)
+ AYM-CONF-ACT-KQ-LMOD(W_R)
+ c_R >= C_quot^crit(s_R,W_R).
```

Thus the next actual estimate is not a free-standing denominator lower
bound. It is the proportional loop-continuity target

```math
\Omega_j(\alpha_Q(j))
\le
W_R\kappa_j^-,
```

followed by the raw-reserve comparison against `C_quot^crit`.

### Definition 4.6I.47z.2e.21af: Rate Selector Export `AYM-CONF-ACT-KQ-RATE(W_R)`

`AYM-CONF-ACT-KQ-RATE(W_R)` is the rate-form sufficient condition for
`AYM-CONF-ACT-KQ-LMOD(W_R)`. It holds on a tail `j>=J_\Xi` when the frozen
Paper-16/Paper-18 tower exports:

1. a denominator profile `d_j>0` with

   ```math
   \kappa_j^-\ge d_j;
   ```

2. a monotone cutoff error gauge `Xi_j(\alpha)` with

   ```math
   \Omega_j(\alpha)\le \Xi_j(\alpha),
   \quad
   \Xi_j(\alpha)\to0
   ```

   as `alpha` advances along the tower for each fixed `j`;

3. a cofinal cutoff selector

   ```math
   \alpha_Q(j)
   :=
   \inf\{\alpha:\Xi_j(\alpha)\le W_R d_j\}
   ```

   that is finite and belongs to the same directed tower for every
   `j>=J_\Xi`.

The profile `d_j` may decay with `j`. The content is not uniform raw
denominator positivity; it is that Paper 16's convergence can be driven
below the moving denominator scale on the same whole-process tower.

### Theorem 4.6I.47z.2e.21ag: Rate Selector Proves Quotient Control

If `AYM-CONF-ACT-KQ-RATE(W_R)` holds, then
`AYM-CONF-ACT-KQ-LMOD(W_R)` holds, hence
`AYM-CONF-ACT-KAPPA-QUOT(W_R)` holds.

Proof.

For `j>=J_\Xi`, the selector is finite, so

```math
\Xi_j(\alpha_Q(j))\le W_Rd_j.
```

Using `Omega_j(alpha)<=Xi_j(alpha)` and `d_j<=kappa_j^-` gives

```math
\Omega_j(\alpha_Q(j))
\le
\Xi_j(\alpha_Q(j))
\le
W_Rd_j
\le
W_R\kappa_j^-.
```

This is the quotient-control inequality in
`AYM-CONF-ACT-KQ-LMOD(W_R)`. Theorem 4.6I.47z.2e.21ab then gives
`AYM-CONF-ACT-KAPPA-QUOT(W_R)`. `square`

### Corollary 4.6I.47z.2e.21ah: Uniform Paper-16 Gauge Special Case

If Paper 16 exports a window-independent monotone gauge `Xi(alpha)` such
that

```math
\Omega_j(\alpha)\le A_j\Xi(\alpha),
```

and the slot ledger exports `kappa_j^- >= d_j>0`, then the rate selector
exists whenever the directed cutoff tower contains, for every `j`, a cutoff
`alpha_Q(j)` satisfying

```math
\Xi(\alpha_Q(j))
\le
\frac{W_Rd_j}{A_j}.
```

This is often the usable form: `A_j` is the finite combinatorial or shape
amplification of the loop family, while `d_j` is the finite slot lower
profile. The quotient route passes if the cutoff convergence can outrun the
ratio `A_j/d_j`.

### Corollary 4.6I.47z.2e.21ai: Rate Selector Obstruction

The quotient route fails for the declared gauge and slot profile if there is
a positive lower obstruction `q_*>0` such that, for every cofinal selector,

```math
\limsup_j
\frac{\Omega_j(\alpha_Q(j))}{\kappa_j^-}
\ge q_*,
```

and the desired `W_R` is smaller than `q_*`. More strongly, if the limsup is
infinite for every cofinal selector, no finite `W_R` can be proved by the
current Paper-16/Paper-18 machinery.

This obstruction is a rate obstruction, not an ontology objection. It says
that the loop-continuity convergence available on the frozen tower is too
slow relative to the denominator profile selected by the confinement
windows.

### Corollary 4.6I.47z.2e.21aj: Step-1 Selector-To-Reserve Chain

The current narrow step-1 route is now:

```text
Paper-16/Paper-18 rate selector:
AYM-CONF-ACT-KQ-RATE(W_R)
=> AYM-CONF-ACT-KAPPA-QUOT(W_R)

raw reserve:
AYM-CONF-ACT-CRES-LOW(c_R)

threshold:
c_R >= C_quot^crit(s_R,W_R)

therefore:
AYM-CONF-ACT-RLD-TAIL.
```

The only remaining non-formal step in this chain is to provide either the
rate selector data `(d_j, Xi_j, alpha_Q(j))` and the raw reserve lower bound
`c_R`, or a same-ledger obstruction showing one of them cannot hold.

### Definition 4.6I.47z.2e.21ak: Paper-16 Raw Reserve Import `AYM-CONF-ACT-CRES-P16(c_R)`

`AYM-CONF-ACT-CRES-P16(c_R)` is the same-ledger import of the raw reserve
needed by `AYM-CONF-ACT-CRES-LOW(c_R)`. It holds on a tail `j>=J_C` when the
Paper-16/Paper-15 surface and Creutz ledgers supply one of the following two
compatible exports.

1. **Raw surface-reserve export.** Paper 16 `HK-SURF-CLOSE` holds on the
   declared block units, and the surface reserve

   ```math
   M_{{\rm SUB},j}^{{\rm bd}}
   =
   \kappa_{{\rm sheet},j}
   -h_{{\rm surf},j}
   -L_{{\rm dec},j}\eta_{{\rm dec},j}^{{\rm bd}}
   -R_{{\rm surf},j}
   ```

   satisfies

   ```math
   M_{{\rm SUB},j}^{{\rm bd}}\ge c_R>0
   ```

   for every `j>=J_C`.

2. **Already-debited Creutz-reserve export.** Paper 16 `HK-CREUTZ-CLOSE`
   exports

   ```math
   M_{{15},j}^{{\rm bd}}
   =
   M_{{\rm SUB},j}^{{\rm bd}}
   -L_{{\rm bat},j}
   -L_{{\rm reg},j}
   -L_{{\rm vol},j}
   -L_{{\rm shape},j}
   \ge c_R>0,
   ```

   and the Paper-18 threshold calculation is explicitly switched to the
   already-debited convention `L_R=0` for those four losses.

The first convention is the default in Paper 18 because
`C_quot^crit(s_R,W_R)` already contains `L_R`. The second convention is
allowed only as a bookkeeping rewrite. It is not allowed to import
`M_15^{bd}` and also subtract `L_bat,R+L_reg,R+L_vol,R+L_shape,R`.

### Lemma 4.6I.47z.2e.21al: Paper-16 Raw Reserve Import Proves `CRES-LOW`

If `AYM-CONF-ACT-CRES-P16(c_R)` holds, then
`AYM-CONF-ACT-CRES-LOW(c_R)` holds on the same tail, with no additional
ontology and no extra reserve assumption.

Proof.

In the raw surface-reserve convention, clause 1 gives directly

```math
M_{{\rm SUB},j}^-\ge M_{{\rm SUB},j}^{{\rm bd}}\ge c_R
```

after identifying Paper 18's raw reserve lower envelope with Paper 16's
surface reserve in the same block-area units. This is exactly
`AYM-CONF-ACT-CRES-LOW(c_R)`.

In the already-debited convention, the imported reserve is
`M_15^{bd}`. Setting the Paper-18 extraction debit `L_R` to zero for the
same four losses makes the threshold algebra use the already-debited reserve
as its raw input. Thus the effective lower envelope is again at least
`c_R`, and no loss is paid twice. `square`

### Theorem 4.6I.47z.2e.21am: Full Conditional Closure Of Step 1

Assume the non-fragile constants in `AYM-CONF-ACT-RLD-SRC-ATTACK` are
available with

```math
\gamma_R>0,
\quad
L_R<\infty,
\quad
e_R<\infty,
\quad
E_R<\infty.
```

Assume also that, on one frozen whole-process tower,

```text
AYM-CONF-ACT-CRES-P16(c_R),
AYM-CONF-ACT-KQ-RATE(W_R),
c_R >= C_quot^crit(s_R,W_R)
```

hold for some `c_R>0`, `W_R<infinity`, and `s_R>0`. Then step 1 is proved:

```text
AYM-CONF-ACT-RLD-TAIL
```

holds with reserve-loop margin at least `s_R` on the common tail.

Proof.

Lemma 4.6I.47z.2e.21al turns `AYM-CONF-ACT-CRES-P16(c_R)` into
`AYM-CONF-ACT-CRES-LOW(c_R)`. Theorem 4.6I.47z.2e.21ag turns
`AYM-CONF-ACT-KQ-RATE(W_R)` into `AYM-CONF-ACT-KAPPA-QUOT(W_R)`. The
threshold inequality `c_R>=C_quot^crit(s_R,W_R)` is therefore exactly the
hypothesis of the quotient denominator route, Theorem 4.6I.47z.2e.21x. That
theorem gives `AYM-CONF-ACT-RLD-TAIL` with margin `s_R`. `square`

### Corollary 4.6I.47z.2e.21an: Step-1 Endpoint

Step 1 is now fully reduced inside Paper 18. There are only three remaining
actual-source questions:

```text
1. Does Paper 16/Paper 15 give AYM-CONF-ACT-CRES-P16(c_R)?
2. Does Paper 16 loop continuity give AYM-CONF-ACT-KQ-RATE(W_R)?
3. Does the scalar inequality c_R >= C_quot^crit(s_R,W_R) hold?
```

If all three answers are yes on one frozen tower, Theorem
4.6I.47z.2e.21am proves `AYM-CONF-ACT-RLD-TAIL`. If any answer is no, then
the obstruction is no longer a bookkeeping ambiguity. It is one of:
surface-reserve collapse, loop-continuity rate failure relative to the slot
denominator, or insufficient reserve after the declared extraction and
loop-modulus debits.

### Definition 4.6I.47z.2e.22: Pressure Worksheet Margin `AYM-CONF-ACT-PI-WORK_j(m_*)`

`AYM-CONF-ACT-PI-WORK_j(m_*)` is the pressure part of
`AYM-CONF-ACT-WORK_j`, evaluated after the reserve-loop worksheet has
produced a certified lower bound

```math
S_j^{{\rm RLD}}\ge\Sigma_j^{{\rm RLD}}>0.
```

It supplies certified bounds

```math
\underline{\alpha}_j\ge\alpha_j^- >0,
\quad
\overline{\epsilon}_j\le e_j^+,
\quad
\overline{h}_j\le h_j^+,
```

```math
\overline{\lambda}_j\le\lambda_j^+,
\quad
\overline{D}_j\le D_j^+,
\quad
\overline{\Delta}_j\le\Delta_j^+,
```

with all upper-bound constants finite and nonnegative. Define the marked/KP
debit

```math
K_j^+
:=
e_j^+ + h_j^+ + \lambda_j^+ + D_j^+,
```

the Paper-17 and target-rate debit

```math
T_j^+(m_*)
:=
2\ell_j\Delta_j^+
+4\ell_jm_*,
```

and the pressure worksheet margin

```math
\Sigma_j^{{\rm PI}}(m_*)
:=
\alpha_j^-\Sigma_j^{{\rm RLD}}
-K_j^+
-T_j^+(m_*).
```

The pressure worksheet passes at `j` when

```math
\Sigma_j^{{\rm PI}}(m_*)>0.
```

### Theorem 4.6I.47z.2e.23: Pressure Worksheet Proves `AYM-CONF-ACT-PI_j(m_*)`

Assume `AYM-CONF-GAMMA-MD-WORK_j`, `AYM-CONF-ACT-LEDGER_j`,
`AYM-CONF-ACT-RLD-WORK_j`, and `AYM-CONF-ACT-PI-WORK_j(m_*)`. If

```math
\Sigma_j^{{\rm RLD}}>0,
\quad
\Sigma_j^{{\rm PI}}(m_*)>0,
```

then `AYM-CONF-ACT-PI_j(m_*)` holds and, more quantitatively,

```math
\Pi_j\ge\Sigma_j^{{\rm PI}}(m_*)>0.
```

Proof.

The reserve-loop worksheet gives

```math
S_j^{{\rm RLD}}\ge\Sigma_j^{{\rm RLD}}>0.
```

Since `alpha_j^- >0` and `underline alpha_j>=alpha_j^-`, the retained
reserve satisfies

```math
\underline{\alpha}_jS_j^{{\rm RLD}}
\ge
\alpha_j^-\Sigma_j^{{\rm RLD}}.
```

The pressure upper bounds give

```math
\overline{\epsilon}_j+\overline{h}_j+\overline{\lambda}_j+\overline{D}_j
\le
K_j^+,
```

and

```math
2\ell_j\overline{\Delta}_j+4\ell_jm_*
\le
T_j^+(m_*).
```

Therefore

```math
\Pi_j
\ge
\alpha_j^-\Sigma_j^{{\rm RLD}}
-K_j^+
-T_j^+(m_*)
=
\Sigma_j^{{\rm PI}}(m_*)
>
0.
```

Hence the exact pressure certificate `AYM-CONF-ACT-PI_j(m_*)` holds.
`square`

### Corollary 4.6I.47z.2e.24: Pressure Attack Outcome

For a fixed cofinal window `j`, after the reserve-loop pass
`Sigma_j^{RLD}>0`, the pressure attack has three honest outcomes:

1. **Pass:** `Sigma_j^{PI}(m_*)>0`. Then Theorem 4.6I.47z.2e.23 proves
   `AYM-CONF-ACT-PI_j(m_*)` and gives the explicit lower bound
   `Pi_j>=Sigma_j^{PI}(m_*)`.
2. **Undecided:** the available bounds give `Sigma_j^{PI}(m_*)<=0`, but no
   same-ledger upper/lower calculation proves that the exact pressure
   surplus is impossible. Then the current marked/KP, Paper-17, or target
   estimates are too weak.
3. **Instrument or target falsification:** a same-ledger upper retained
   reserve bound `A_j^+` and lower pressure debit `P_j^-` prove
   `A_j^+<=P_j^-`. Then the chosen endpoint protocol, KP battery,
   selected-rate debit, target rate `m_*`, or window schedule cannot prove
   `AYM-CONF-ACT-PI_j(m_*)`.

This is the second real mathematical attack on the actual `4D SU(N)`
constants. It does not ask for a field ontology or a hidden flux tube; it
asks whether the scalar retained reserve beats all declared scalar debits on
the same whole-process record law.

### Definition 4.6I.47z.2e.24a: Tail Pressure Positivity `AYM-CONF-ACT-PI-TAIL(m_*)`

`AYM-CONF-ACT-PI-TAIL(m_*)` is the tail version of the pressure attack. It
holds when there is a tail start `J_P` such that
`AYM-CONF-ACT-PI-WORK_j(m_*)` is available for every declared window
`j>=J_P` and

```math
\Sigma_j^{{\rm PI}}(m_*)>0
```

for every such `j`.

A uniform pressure-tail pass is the stronger certificate that there is an
`s_P>0` such that

```math
\Sigma_j^{{\rm PI}}(m_*)\ge s_P
```

for every `j>=J_P`. A reindexed pressure pass is the weaker certificate
that there is a cofinal subsequence `j_n` with

```math
\Sigma_{j_n}^{{\rm PI}}(m_*)>0
```

for every `n`.

### Theorem 4.6I.47z.2e.24b: Uniform Pressure-Debit Gap Proves Tail Positivity

Assume that, for all `j>=J_P`, `AYM-CONF-ACT-PI-WORK_j(m_*)` holds and
there are constants

```math
s_R>0,
\quad
\alpha_P>0,
\quad
K_P\ge0,
\quad
T_P\ge0,
\quad
s_P>0
```

such that

```math
\Sigma_j^{{\rm RLD}}\ge s_R,
\quad
\alpha_j^-\ge\alpha_P,
\quad
K_j^+\le K_P,
\quad
T_j^+(m_*)\le T_P,
```

and

```math
\alpha_Ps_R-K_P-T_P\ge s_P>0.
```

Then `AYM-CONF-ACT-PI-TAIL(m_*)` holds, and in fact

```math
\Sigma_j^{{\rm PI}}(m_*)\ge s_P
```

for every `j>=J_P`.

Proof.

For `j>=J_P`,

```math
\Sigma_j^{{\rm PI}}(m_*)
=
\alpha_j^-\Sigma_j^{{\rm RLD}}
-K_j^+
-T_j^+(m_*)
\ge
\alpha_Ps_R-K_P-T_P
\ge
s_P
>
0.
```

This is the uniform pressure-tail pass. `square`

### Theorem 4.6I.47z.2e.24c: Asymptotic Dominance Proves Cofinal Pressure Positivity

Suppose there are a positive scale `c_j>0`, a tail start `J_P`, and constants
`a_P>b_P` such that, for all `j>=J_P`,

```math
\alpha_j^-\Sigma_j^{{\rm RLD}}\ge c_j a_P,
\quad
K_j^+ + T_j^+(m_*)\le c_j b_P.
```

Then `AYM-CONF-ACT-PI-TAIL(m_*)` holds on that tail:

```math
\Sigma_j^{{\rm PI}}(m_*)
\ge
c_j(a_P-b_P)
>
0.
```

If the two inequalities hold only on a cofinal subsequence `j_n`, then the
same conclusion holds after reindexing that subsequence as the declared
cofinal pressure family.

Proof.

Subtract the pressure debit from the retained-reserve lower bound:

```math
\Sigma_j^{{\rm PI}}(m_*)
=
\alpha_j^-\Sigma_j^{{\rm RLD}}
-K_j^+
-T_j^+(m_*)
\ge
c_j(a_P-b_P).
```

Since `c_j>0` and `a_P>b_P`, the margin is positive. The subsequence version
is the same calculation with `j` replaced by `j_n`. `square`

### Definition 4.6I.47z.2e.24d: Pressure Falsification Ledger `AYM-CONF-ACT-PI-FALS_j(m_*)`

For a fixed window `j`, `AYM-CONF-ACT-PI-FALS_j(m_*)` is the same-ledger
certificate that the chosen pressure instruments and target rate cannot
pass. It consists of an upper retained-reserve bound `A_j^+` and a lower
pressure-debit bound `P_j^-` such that

```math
\underline{\alpha}_jS_j^{{\rm RLD}}\le A_j^+,
```

```math
\overline{\epsilon}_j+\overline{h}_j+\overline{\lambda}_j+\overline{D}_j
+2\ell_j\overline{\Delta}_j
+4\ell_jm_*
\ge P_j^-,
```

and

```math
A_j^+\le P_j^-.
```

This certificate falsifies the declared endpoint/KP/rate instruments for
the chosen target `m_*`; it does not falsify confinement at another target
rate or with another cofinal window family.

### Theorem 4.6I.47z.2e.24e: Pressure Falsification

If `AYM-CONF-ACT-PI-FALS_j(m_*)` holds, then `AYM-CONF-ACT-PI_j(m_*)` is
false for the declared instruments at window `j`.

Proof.

The falsification bounds give

```math
\underline{\alpha}_jS_j^{{\rm RLD}}
\le
A_j^+
\le
P_j^-
\le
\overline{\epsilon}_j+\overline{h}_j+\overline{\lambda}_j+\overline{D}_j
+2\ell_j\overline{\Delta}_j
+4\ell_jm_*.
```

This is the negation of the strict pressure inequality required by
`AYM-CONF-ACT-PI_j(m_*)`. `square`

### Corollary 4.6I.47z.2e.24f: Pressure Tail Trichotomy

For the declared actual `4D SU(N)` pressure instruments and target `m_*`,
the proof status should be recorded in one of the following forms:

1. **Uniform tail pass:** Theorem 4.6I.47z.2e.24b supplies
   `Sigma_j^{PI}(m_*)>=s_P>0` eventually.
2. **Asymptotic or reindexed pass:** Theorem 4.6I.47z.2e.24c supplies
   `Sigma_j^{PI}(m_*)>0` eventually or on a cofinal subsequence.
3. **Instrument or target falsification:** Theorem 4.6I.47z.2e.24e proves
   that the declared pressure instruments cannot pass for the chosen
   `m_*` on a tail or on infinitely many required windows.
4. **Undecided:** neither lower-bound positivity nor upper-bound
   falsification has been proved. Then the remaining work is to sharpen
   actual same-ledger estimates for `alpha_j^- Sigma_j^{RLD}` and
   `K_j^+ + T_j^+(m_*)`.

Thus the second bottleneck has been reduced to a genuine asymptotic
comparison:

```text
certified retained reserve alpha_j^- Sigma_j^RLD
versus
certified pressure debit K_j^+ + T_j^+(m_*).
```

### Theorem 4.6I.47z.2e.24g: Tail RLD And Tail PI Combine To Cofinal Survival

Assume the declared window family has tail starts `J_R` and `J_P` such that:

1. `AYM-CONF-ACT-RLD-TAIL` holds on all declared windows `j>=J_R`;
2. `AYM-CONF-ACT-PI-TAIL(m_*)` holds on all declared windows `j>=J_P`;
3. for all `j>=max{J_R,J_P}`, the same-ledger certificates

   ```text
   AYM-CONF-GAMMA-MD-WORK_j,
   AYM-CONF-ACT-LEDGER_j,
   AYM-CONF-ACT-WORK_j,
   AYM-CONF-ACT-RLD-WORK_j,
   AYM-CONF-ACT-PI-WORK_j(m_*)
   ```

   hold on one frozen whole-process law.

Then `AYM-CONF-ACT-COF(m_*)` holds on the tail family.

Proof.

Let `J_*:=max{J_R,J_P}`. For every declared window `j>=J_*`, the RLD-tail
certificate gives `Sigma_j^{RLD}>0` and the PI-tail certificate gives
`Sigma_j^{PI}(m_*)>0`. The same-ledger certificates supply the remaining
worksheet hypotheses. Therefore the tail windows satisfy
`AYM-CONF-ACT-COF-WORK(m_*)`. Theorem 4.6I.47z.2e.26 gives
`AYM-CONF-ACT-COF(m_*)`. `square`

### Definition 4.6I.47z.2e.24h: Actual PI Asymptotic Constants Ledger `AYM-CONF-ACT-PI-ASYM`

`AYM-CONF-ACT-PI-ASYM` is the asymptotic constants ledger for the second
actual bottleneck. It records the estimates needed to decide whether the
retained reserve after the reserve-loop pass beats the marked/KP,
Paper-17, and target-rate pressure.

| Quantity | Formula role | Required tail estimate | Source to prove/import | Failure mode |
| --- | --- | --- | --- | --- |
| `Sigma_j^RLD` | retained reserve available after minimal loop-modulus debit | lower bound `>=s_R>0` or a scaled positive reserve | `AYM-CONF-ACT-RLD-TAIL`, reindexed RLD pass, or direct window proof | no reserve left to retain |
| `alpha_j^-` | marked retained-area conversion | lower bound `>=alpha_P>0` or scaled product control for `alpha_j^- Sigma_j^RLD` | marked geometry and endpoint bridge ledger | retained-area collapse |
| `e_j^+` | local marked readout/collar/counterterm loss | upper bound `<=e_P` or scaled debit control | marked local readout ledger | local endpoint loss eats reserve |
| `h_j^+` | endpoint-enlarged KP height loss | upper bound `<=h_P` or scaled debit control | marked KP import from Papers 14 and 15 | KP height pressure eats reserve |
| `lambda_j^+` | endpoint-enlarged activity loss | upper bound `<=lambda_P` or scaled debit control | marked activity ledger | marked activity pressure eats reserve |
| `D_j^+` | KP threshold debit | upper bound `<=D_P` or scaled debit control | finite marked KP threshold estimate | threshold pressure eats reserve |
| `ell_j Delta_j^+` | Paper-17 selected-rate debit at window scale | upper bound `<=Q_P` or scaled debit control | Paper-17 rate-loss ledger | selected-rate loss eats reserve |
| `ell_j` | target-rate multiplier | upper bound `<=ell_P` for a fixed target route, or reduced target `m_*` | cofinal scheduler and target-rate choice | `4 ell_j m_*` overreaches |

The ledger is deliberately scalar. It does not introduce endpoint particles,
flux tubes, gauge-fixed fields, or partial kernels. It asks whether one
whole-process tower supplies enough retained scalar loop reserve to pay the
declared scalar debits.

### Definition 4.6I.47z.2e.24i: Pressure Numerator Lower-Bound Attack `AYM-CONF-ACT-PNUM-TAIL`

Fix `m_*>0`. `AYM-CONF-ACT-PNUM-TAIL` holds on a tail `j>=J_A` when
`AYM-CONF-ACT-PI-WORK_j(m_*)` is available on that tail and there are
constants

```math
s_R>0,
\quad
\alpha_P>0
```

such that, for all `j>=J_A`,

```math
\Sigma_j^{{\rm RLD}}\ge s_R,
\quad
\alpha_j^-\ge\alpha_P.
```

Define the retained-reserve numerator lower bound

```math
A_P:=\alpha_Ps_R.
```

### Theorem 4.6I.47z.2e.24j: Pressure Numerator Tail Lower Bound

Assume `AYM-CONF-ACT-PNUM-TAIL`. Then, for every `j>=J_A`,

```math
\alpha_j^-\Sigma_j^{{\rm RLD}}\ge A_P.
```

Proof.

The two defining lower bounds give

```math
\alpha_j^-\Sigma_j^{{\rm RLD}}
\ge
\alpha_Ps_R
=
A_P.
```

Since `alpha_P>0` and `s_R>0`, the retained-reserve numerator is strictly
positive on the tail. `square`

### Definition 4.6I.47z.2e.24k: Pressure-Debit Upper-Bound Attack `AYM-CONF-ACT-PDEB-TAIL(m_*)`

Fix `m_*>0`. `AYM-CONF-ACT-PDEB-TAIL(m_*)` holds on a tail `j>=J_D` when
`AYM-CONF-ACT-PI-WORK_j(m_*)` is available on that tail and there are
finite constants

```math
e_P,h_P,\lambda_P,D_P,Q_P,\ell_P\ge0
```

such that, for all `j>=J_D`,

```math
e_j^+\le e_P,
\quad
h_j^+\le h_P,
\quad
\lambda_j^+\le\lambda_P,
\quad
D_j^+\le D_P,
```

and

```math
\ell_j\Delta_j^+\le Q_P,
\quad
\ell_j\le\ell_P.
```

Define

```math
K_P:=e_P+h_P+\lambda_P+D_P,
```

and

```math
T_P(m_*):=2Q_P+4\ell_Pm_*.
```

The product bound on `ell_j Delta_j^+` is intentional: the Paper-17 debit
enters only through that product. Bounding `Delta_j^+` and `ell_j`
separately is stronger than necessary and may falsely reject a good
cofinal scheduler.

### Theorem 4.6I.47z.2e.24l: Pressure-Debit Tail Upper Bound

Assume `AYM-CONF-ACT-PDEB-TAIL(m_*)`. Then, for every `j>=J_D`,

```math
K_j^+ + T_j^+(m_*)\le K_P+T_P(m_*).
```

Proof.

The local debit bounds give

```math
K_j^+
=
e_j^+ + h_j^+ + \lambda_j^+ + D_j^+
\le
K_P.
```

The selected-rate and target-rate bounds give

```math
T_j^+(m_*)
=
2\ell_j\Delta_j^+
+4\ell_jm_*
\le
2Q_P+4\ell_Pm_*
=
T_P(m_*).
```

Adding the two estimates proves the claim. `square`

### Theorem 4.6I.47z.2e.24m: First Tail Pressure Inequality

Assume `AYM-CONF-ACT-PNUM-TAIL` and
`AYM-CONF-ACT-PDEB-TAIL(m_*)`. Let

```math
J_*:=\max\{J_A,J_D\}.
```

If

```math
A_P-K_P-T_P(m_*)\ge s_P>0,
```

then `AYM-CONF-ACT-PI-TAIL(m_*)` holds on the tail `j>=J_*`, with

```math
\Sigma_j^{{\rm PI}}(m_*)\ge s_P>0.
```

Proof.

For `j>=J_*`, Theorem 4.6I.47z.2e.24j gives

```math
\alpha_j^-\Sigma_j^{{\rm RLD}}\ge A_P,
```

and Theorem 4.6I.47z.2e.24l gives

```math
K_j^+ + T_j^+(m_*)\le K_P+T_P(m_*).
```

Therefore

```math
\Sigma_j^{{\rm PI}}(m_*)
=
\alpha_j^-\Sigma_j^{{\rm RLD}}
-K_j^+
-T_j^+(m_*)
\ge
A_P-K_P-T_P(m_*)
\ge
s_P
>
0.
```

This is exactly the uniform tail pressure pass. `square`

### Corollary 4.6I.47z.2e.24n: First Tail PI Decision

The first tail pressure inequality is now the single scalar comparison

```math
\alpha_Ps_R
>
e_P+h_P+\lambda_P+D_P
+2Q_P
+4\ell_Pm_*.
```

If this strict inequality is proved, the pressure tail passes. If it is
falsified by same-ledger upper retained-reserve and lower pressure-debit
bounds, the declared pressure instruments or target rate fail. If neither
direction is proved, the remaining work is to sharpen actual estimates for
`alpha_j^- Sigma_j^RLD`, local marked/KP pressure, the Paper-17 product
debit `ell_j Delta_j^+`, and the target-rate schedule `ell_j m_*`.

### Definition 4.6I.47z.2e.24o: Step-2 Source Import `AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)`

`AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)` is the source-import package for the
second actual bottleneck. It is read on the same frozen whole-process tower
as the step-1 closure. It holds on a tail `j>=J_{PI}` when the following
data are exported by the already declared Paper-18 and Paper-17 ledgers.

1. **Retained reserve from step 1.** `AYM-CONF-ACT-RLD-TAIL` holds with a
   tail margin `s_R>0`, so the pressure worksheet may use

   ```math
   \Sigma_j^{{\rm RLD}}\ge s_R
   ```

   for every `j>=J_{PI}`.

2. **Marked retained-area and endpoint/KP source.** The marked source
   package, through `AYM-CONF-MARK-ACT-TAIL` or a stronger same-ledger
   finite-window verification, exports constants

   ```math
   \alpha_P>0,
   \quad
   e_P,h_P,\lambda_P,D_P\ge0
   ```

   such that

   ```math
   \alpha_j^-\ge\alpha_P,
   \quad
   e_j^+\le e_P,
   \quad
   h_j^+\le h_P,
   \quad
   \lambda_j^+\le\lambda_P,
   \quad
   D_j^+\le D_P
   ```

   for every `j>=J_{PI}`. Here `alpha_P` is the retained-area conversion
   from `MARK-GEOM_j`, while `e_P,h_P,lambda_P,D_P` are the local endpoint,
   marked height, marked activity, and KP-threshold debits from
   `MARK-LOSS_j` and `MS-KP_j`.

3. **Paper-17 selected-rate source.** Paper 17's selected-rate and
   whole-process ledgers export constants `Q_P>=0` and `ell_P>0` such that

   ```math
   \ell_j\Delta_j^+\le Q_P,
   \quad
   \ell_j\le\ell_P
   ```

   for every `j>=J_{PI}`.

4. **Worksheet population.** For every `j>=J_{PI}`, the imported constants
   populate `AYM-CONF-ACT-PI-WORK_j(m_*)` with

   ```text
   alpha_j^-,
   e_j^+,
   h_j^+,
   lambda_j^+,
   D_j^+,
   Delta_j^+,
   ell_j.
   ```

5. **One ledger.** The estimates above are restrictions or explicitly
   debited extensions of the same whole-process law used in
   `AYM-CONF-ACT-CRES-P16(c_R)` and `AYM-CONF-ACT-KQ-RATE(W_R)`.

The import is intentionally operational. It imports scalar record constants
and typed endpoint-protocol debits; it does not introduce colored particles,
hidden flux tubes, gauge-fixed fields, or partial transition kernels as
new primitives.

### Lemma 4.6I.47z.2e.24p: Step-2 Source Import Populates `PNUM` And `PDEB`

If `AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)` holds, then
`AYM-CONF-ACT-PNUM-TAIL` and `AYM-CONF-ACT-PDEB-TAIL(m_*)` hold on the same
tail, with

```math
A_P=\alpha_Ps_R,
```

```math
K_P=e_P+h_P+\lambda_P+D_P,
```

and

```math
T_P(m_*)=2Q_P+4\ell_Pm_*.
```

Proof.

Clause 1 gives the reserve lower bound
`Sigma_j^{RLD}>=s_R`, and clause 2 gives `alpha_j^- >= alpha_P`. These are
exactly the hypotheses of `AYM-CONF-ACT-PNUM-TAIL`, with
`A_P=alpha_P s_R`.

The remaining bounds in clause 2 give the local debit estimates

```math
e_j^+\le e_P,
\quad
h_j^+\le h_P,
\quad
\lambda_j^+\le\lambda_P,
\quad
D_j^+\le D_P.
```

Clause 3 gives the selected-rate and target-scale estimates

```math
\ell_j\Delta_j^+\le Q_P,
\quad
\ell_j\le\ell_P.
```

These are exactly the hypotheses of `AYM-CONF-ACT-PDEB-TAIL(m_*)`. `square`

### Definition 4.6I.47z.2e.24q: Step-2 Threshold `AYM-CONF-ACT-PI-THRESH(s_P,m_*)`

Given the source-import constants of
`AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)`, define

```math
K_P:=e_P+h_P+\lambda_P+D_P,
```

```math
T_P(m_*):=2Q_P+4\ell_Pm_*,
```

and

```math
A_P:=\alpha_Ps_R.
```

For a demanded pressure margin `s_P>0`,
`AYM-CONF-ACT-PI-THRESH(s_P,m_*)` is the scalar inequality

```math
A_P-K_P-T_P(m_*)\ge s_P.
```

Equivalently, the target rate must obey

```math
m_*
\le
\frac{\alpha_Ps_R-e_P-h_P-\lambda_P-D_P-2Q_P-s_P}
{4\ell_P}
```

when `ell_P>0`. This is a rate ceiling, not a new physics assumption.

### Theorem 4.6I.47z.2e.24r: Full Conditional Closure Of Step 2

Assume, on one frozen whole-process tower,

```text
AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*),
AYM-CONF-ACT-PI-THRESH(s_P,m_*).
```

Then step 2 is proved:

```text
AYM-CONF-ACT-PI-TAIL(m_*)
```

holds with pressure margin at least `s_P` on the common tail.

Proof.

Lemma 4.6I.47z.2e.24p gives `AYM-CONF-ACT-PNUM-TAIL` and
`AYM-CONF-ACT-PDEB-TAIL(m_*)` with the displayed constants. The threshold
condition is exactly

```math
A_P-K_P-T_P(m_*)\ge s_P>0.
```

Theorem 4.6I.47z.2e.24m therefore gives
`AYM-CONF-ACT-PI-TAIL(m_*)` with

```math
\Sigma_j^{{\rm PI}}(m_*)\ge s_P
```

on the common tail. `square`

### Corollary 4.6I.47z.2e.24s: Step-2 Endpoint

Step 2 is now fully reduced inside Paper 18. There are only three remaining
actual-source questions:

```text
1. Does step 1 supply Sigma_j^RLD >= s_R on the same tail?
2. Do the marked and Paper-17 ledgers supply PI-SRC-IMPORT(s_R,m_*)?
3. Does the scalar threshold A_P-K_P-T_P(m_*) >= s_P > 0 hold?
```

If all three answers are yes on one frozen tower, Theorem
4.6I.47z.2e.24r proves `AYM-CONF-ACT-PI-TAIL(m_*)`. If any answer is no,
then the pressure obstruction is one of: retained-area collapse,
endpoint/KP pressure growth, Paper-17 selected-rate overpayment,
target-rate overreach, or same-ledger mismatch.

### Definition 4.6I.47z.2e.24t: Step-3 Ledger Source Import `AYM-CONF-ACT-LEDGER-SRC`

`AYM-CONF-ACT-LEDGER-SRC` is the source-import package for the third actual
bottleneck: proving that the step-1 and step-2 constants are all read from
one whole-process record law with one debit register. It holds on a tail
`j>=J_{LED}` when the following data are available.

1. **Common law and restrictions.** There is one frozen whole-process law
   `Law_*`, one finite record algebra `F_j`, and one restriction map

   ```math
   \rho_j:\mathsf{Law}_*\to F_j
   ```

   for every `j>=J_{LED}`. The maps are the same maps used by
   `P16-LAW-IMPORT`, `AYM-CONF-WIN-SCHED`, the Paper-15 battery inclusion,
   and the Paper-17 probe-battery restriction.

2. **Step-1 source binding.** The constants in
   `AYM-CONF-ACT-CRES-P16(c_R)`, `AYM-CONF-ACT-KQ-RATE(W_R)`, and the
   threshold calculation for `AYM-CONF-ACT-RLD-TAIL` are functions of
   `rho_j(Law_*)` and the declared Paper-15/Paper-16 reserve and
   loop-modulus instruments.

3. **Step-2 source binding.** The constants in
   `AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)` and
   `AYM-CONF-ACT-PI-THRESH(s_P,m_*)` are functions of the same
   `rho_j(Law_*)`, the declared marked endpoint protocol, and the Paper-17
   selected-rate battery.

4. **Disjoint debit register.** For every `j>=J_{LED}`,
   `CONF-DEBIT-REG` holds after restriction to `F_j`. In particular:

   ```text
   reserve extraction and readout losses are paid once,
   loop-modulus losses are paid once,
   marked endpoint and KP losses are paid once,
   Paper-17 selected-rate losses are paid once.
   ```

   No loss may be both absorbed into the Paper-15/Paper-16 reserve and
   subtracted again in the Paper-18 marked/KP or Paper-17 rate debit.

5. **Typed endpoint ontology.** Endpoint labels are typed boundary
   instruments. Their admissible scalar consequences are the marked-loop,
   Wilson-loop, Polyakov-loop, or connected-record estimates appearing in
   the finite record algebra. No colored endpoint, gauge-fixed field,
   surface, or partial transition kernel is used as a primitive state.

### Lemma 4.6I.47z.2e.24u: Ledger Source Import Proves `ACT-LEDGER_j`

If `AYM-CONF-ACT-LEDGER-SRC` holds, then `AYM-CONF-ACT-LEDGER_j` holds for
every `j>=J_{LED}`.

Proof.

Clause 1 supplies the law, finite record algebra, and restriction map
required by Definition 4.6I.47z.2e.14. Clause 2 says that all reserve,
readout, loop-modulus, and denominator constants entering
`AYM-CONF-ACT-RLD_j` are functions of that restricted law and its declared
Paper-15/Paper-16 instruments. This is clause 1 of
`AYM-CONF-ACT-LEDGER_j`.

Clause 3 says that all retained-area, marked endpoint, marked KP, and
Paper-17 selected-rate constants entering `AYM-CONF-ACT-PI_j(m_*)` are
functions of the same restricted law. This is clause 2 of
`AYM-CONF-ACT-LEDGER_j`.

Clause 4 is exactly the no-double-debit and no-foreign-ledger condition in
clause 3 of `AYM-CONF-ACT-LEDGER_j`. Clause 5 identifies the endpoint
protocol and loop family as typed scalar-record constructions, which gives
the compatibility clause between the Creutz readout and marked endpoint
bridge. Therefore every clause of `AYM-CONF-ACT-LEDGER_j` holds. `square`

### Definition 4.6I.47z.2e.24v: Step-3 Tail Ledger `AYM-CONF-ACT-LEDGER-TAIL`

`AYM-CONF-ACT-LEDGER-TAIL` holds when there is a tail start `J_{LED}` such
that `AYM-CONF-ACT-LEDGER_j` holds for every declared window `j>=J_{LED}`.

The certificate is allowed to use a finite-prefix check if the proof keeps
finite-prefix windows in the declared family. It is not allowed to stitch
together different regulator towers or endpoint protocols across the tail.

### Theorem 4.6I.47z.2e.24w: Full Conditional Closure Of Step 3

If `AYM-CONF-ACT-LEDGER-SRC` holds, then
`AYM-CONF-ACT-LEDGER-TAIL` holds.

Proof.

Lemma 4.6I.47z.2e.24u proves `AYM-CONF-ACT-LEDGER_j` for every
`j>=J_{LED}`. This is exactly `AYM-CONF-ACT-LEDGER-TAIL`. `square`

### Corollary 4.6I.47z.2e.24x: Step-3 Endpoint

Step 3 is now fully reduced inside Paper 18. There are only three remaining
actual-source questions:

```text
1. Is there one frozen whole-process law Law_* for the RLD and PI constants?
2. Does CONF-DEBIT-REG assign every loss to exactly one bucket?
3. Are endpoint instruments eliminated into scalar records before use?
```

If all three answers are yes on the declared tower, Theorem
4.6I.47z.2e.24w proves `AYM-CONF-ACT-LEDGER-TAIL`. If any answer is no, the
obstruction is ledger drift, double debit, foreign-regulator import, or
ontology failure.

### Definition 4.6I.47z.2e.24y: Step-4 Cofinal Source Import `AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)`

`AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)` is the source-import package for the
fourth actual bottleneck: proving that the local positive windows survive
cofinally. It holds when the following data are available on one frozen
whole-process tower.

1. **Cofinal scheduler.** There is a schedule `n -> j_n` such that for every
   declared base window `J` there is an `n` with `j_n>=J`. The schedule is
   the one produced by `AYM-CONF-WIN-SCHED` or an explicitly declared
   cofinal subsequence of it.

2. **Local worksheets.** For every `n`, the following certificates are
   available on the same restricted law:

   ```text
   AYM-CONF-GAMMA-MD-WORK_j_n,
   AYM-CONF-ACT-WORK_j_n,
   AYM-CONF-ACT-RLD-WORK_j_n,
   AYM-CONF-ACT-PI-WORK_j_n(m_*).
   ```

3. **Step-1 and step-2 tails.** The schedule is contained in the common tail
   on which

   ```math
   \Sigma_{j_n}^{{\rm RLD}}\ge s_R>0,
   \quad
   \Sigma_{j_n}^{{\rm PI}}(m_*)\ge s_P>0.
   ```

4. **Step-3 ledger.** `AYM-CONF-ACT-LEDGER-TAIL` holds on the same schedule.

This is a cofinality certificate, not a new dynamical estimate. It says the
already proved local scalar inequalities occur along an unbounded directed
family compatible with the Paper-17 and Paper-15 batteries.

### Lemma 4.6I.47z.2e.24z: Cofinal Source Import Populates `COF-WORK`

If `AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)` holds, then
`AYM-CONF-ACT-COF-WORK(m_*)` holds on the scheduled family `j_n`.

Proof.

Clause 1 is the cofinal schedule required by
`AYM-CONF-ACT-COF-WORK(m_*)`. Clause 2 supplies the local Gamma,
actual-constant, reserve-loop, and pressure worksheets. Clause 4 supplies
`AYM-CONF-ACT-LEDGER_j_n` for every scheduled window. Clause 3 supplies the
two positive worksheet margins. These are exactly the clauses of
`AYM-CONF-ACT-COF-WORK(m_*)`. `square`

### Theorem 4.6I.47z.2e.24aa: Full Conditional Closure Of Step 4

If `AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)` holds, then
`AYM-CONF-ACT-COF(m_*)` holds.

Proof.

Lemma 4.6I.47z.2e.24z gives `AYM-CONF-ACT-COF-WORK(m_*)` on the scheduled
cofinal family. Theorem 4.6I.47z.2e.26 then gives
`AYM-CONF-ACT-COF(m_*)`. `square`

### Corollary 4.6I.47z.2e.24ab: Step-4 Endpoint

Step 4 is now fully reduced inside Paper 18. There are only three remaining
actual-source questions:

```text
1. Do the positive windows form a cofinal scheduled family?
2. Do RLD-tail, PI-tail, and LEDGER-tail overlap on that family?
3. Do the local worksheets remain available on every scheduled window?
```

If all three answers are yes, Theorem 4.6I.47z.2e.24aa proves
`AYM-CONF-ACT-COF(m_*)`. If any answer is no, the obstruction is scheduler
failure, tail-overlap failure, ledger drift, or loss of worksheet data on
the cofinal family.

### Theorem 4.6I.47z.2e.24ac: Steps 1--4 Close The Minimal-Debit Source

Assume, on one frozen whole-process tower:

```text
AYM-CONF-ACT-RLD-TAIL,
AYM-CONF-ACT-PI-TAIL(m_*),
AYM-CONF-ACT-LEDGER-TAIL,
AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*).
```

Then:

```text
AYM-CONF-ACT-COF(m_*),
AYM-CONF-GAMMA-FW-DIRECT(m_*).
```

Proof.

Theorem 4.6I.47z.2e.24aa gives `AYM-CONF-ACT-COF(m_*)`. The four-constant
closure theorem, Theorem 4.6I.47z.2e.16, then gives
`AYM-CONF-GAMMA-FW-DIRECT(m_*)` on the declared cofinal family. `square`

### Definition 4.6I.47z.2e.25: Cofinal Actual Worksheet `AYM-CONF-ACT-COF-WORK(m_*)`

`AYM-CONF-ACT-COF-WORK(m_*)` is the local-to-cofinal worksheet. It consists
of:

1. a cofinal schedule of windows `n -> j_n`, meaning that for every declared
   base window `J` there is an `n` with `j_n>=J`;
2. for every `n`, the certificates

   ```text
   AYM-CONF-GAMMA-MD-WORK_j_n,
   AYM-CONF-ACT-LEDGER_j_n,
   AYM-CONF-ACT-WORK_j_n,
   AYM-CONF-ACT-RLD-WORK_j_n,
   AYM-CONF-ACT-PI-WORK_j_n(m_*)
   ```

   on the same frozen whole-process law;
3. the two local worksheet margins

   ```math
   \Sigma_{j_n}^{{\rm RLD}}>0,
   \quad
   \Sigma_{j_n}^{{\rm PI}}(m_*)>0
   ```

   for every `n`.

The worksheet is a certificate of cofinal survival, not a new physical
postulate. It says that the same scalar whole-process estimates keep passing
along an unbounded family of finite record windows.

### Theorem 4.6I.47z.2e.26: Cofinal Actual Worksheet Proves `AYM-CONF-ACT-COF(m_*)`

Assume `AYM-CONF-ACT-COF-WORK(m_*)`. Then `AYM-CONF-ACT-COF(m_*)` holds.

Proof.

Fix `n`. The reserve-loop worksheet and positive margin give
`AYM-CONF-ACT-RLD_j_n` by Theorem 4.6I.47z.2e.20. The pressure worksheet
and positive margin give `AYM-CONF-ACT-PI_j_n(m_*)` by Theorem
4.6I.47z.2e.23. The cofinal worksheet also includes
`AYM-CONF-GAMMA-MD-WORK_j_n` and `AYM-CONF-ACT-LEDGER_j_n`.

Thus every window in the schedule has exactly the four certificates required
by Definition 4.6I.47z.2e.15. Since the schedule is cofinal,
`AYM-CONF-ACT-COF(m_*)` holds. `square`

### Theorem 4.6I.47z.2e.27: Finite-Prefix And Tail Cofinal Survival

Suppose the declared window family has a tail start `J_*`. Assume:

1. every finite-prefix window used by the proof, if any, is checked directly
   by the local worksheet pass
   `AYM-CONF-ACT-RLD-WORK_j + AYM-CONF-ACT-PI-WORK_j(m_*)` with both
   margins positive;
2. for every declared tail window `j>=J_*`, the same-ledger worksheet
   certificates

   ```text
   AYM-CONF-GAMMA-MD-WORK_j,
   AYM-CONF-ACT-LEDGER_j,
   AYM-CONF-ACT-WORK_j,
   AYM-CONF-ACT-RLD-WORK_j,
   AYM-CONF-ACT-PI-WORK_j(m_*)
   ```

   hold;
3. there are tail constants `s_R>0` and `s_P>0` such that, for all `j>=J_*`,

   ```math
   \Sigma_j^{{\rm RLD}}\ge s_R,
   \quad
   \Sigma_j^{{\rm PI}}(m_*)\ge s_P.
   ```

Then the tail windows define `AYM-CONF-ACT-COF(m_*)`. If the proof keeps the
finite-prefix windows in the declared family, the direct finite-prefix
checks supply those windows as well.

Proof.

For each tail window `j>=J_*`, the lower bounds imply both worksheet margins
are strictly positive. The tail windows are cofinal, so they define a
cofinal schedule. Applying Theorem 4.6I.47z.2e.26 to that schedule gives
`AYM-CONF-ACT-COF(m_*)`. Finite-prefix checks are not needed for cofinality,
but they certify any finite windows retained in the declared family. `square`

### Theorem 4.6I.47z.2e.28: Reindexed Cofinal Survival

Suppose full-tail uniformity is unavailable, but there exists a cofinal
subsequence `j_n` such that, for every `n`,

```text
AYM-CONF-GAMMA-MD-WORK_j_n,
AYM-CONF-ACT-LEDGER_j_n,
AYM-CONF-ACT-WORK_j_n,
AYM-CONF-ACT-RLD-WORK_j_n,
AYM-CONF-ACT-PI-WORK_j_n(m_*)
```

hold and

```math
\Sigma_{j_n}^{{\rm RLD}}>0,
\quad
\Sigma_{j_n}^{{\rm PI}}(m_*)>0.
```

Then the subsequence can be reindexed as the declared cofinal window family,
and `AYM-CONF-ACT-COF(m_*)` holds for that family.

Proof.

The displayed data are precisely `AYM-CONF-ACT-COF-WORK(m_*)` on the
subsequence. Theorem 4.6I.47z.2e.26 gives `AYM-CONF-ACT-COF(m_*)` after
reindexing the subsequence as the declared cofinal family. `square`

### Corollary 4.6I.47z.2e.29: Cofinal Survival Obstruction Classifier

If the local worksheets exist but `AYM-CONF-ACT-COF(m_*)` cannot be proved,
then the obstruction is one of the following scalar failures:

| Obstruction | Meaning |
| --- | --- |
| no cofinal scheduler | the positive windows do not form an unbounded directed family |
| reserve-loop tail failure | `Sigma_j^{RLD}` is nonpositive eventually, or no cofinal positive subsequence is available |
| pressure tail failure | `Sigma_j^{PI}(m_*)` is nonpositive eventually, or no cofinal positive subsequence is available |
| ledger drift | the constants pass locally but not on one frozen whole-process law across the declared cofinal family |
| sparse incompatible positives | positive windows exist but cannot be embedded into the Paper-17/Paper-15 cofinal scheduler |
| target-rate overreach | lowering `m_*` could restore `Sigma_j^{PI}(m_*)>0`, so the chosen target rate is too aggressive |
| estimate weakness | the current bounds fail, but no same-ledger upper/lower calculation falsifies the exact margins |

This classifier is the final local-to-cofinal boundary. Beyond it, the work
is no longer formal reduction. It is the actual asymptotic estimate problem
for the `4D SU(N)` whole-process constants.

### Theorem 4.6I.47z.2f: Arbitrary-Window Minimal-Debit Gamma Pass

Fix a cofinal window `j`. Assume `AYM-CONF-GAMMA-MD-WORK_j` and

```math
S_j^{{\rm RLD}}>0,
\quad
\Pi_j>0.
```

Then there is a legal loop-modulus debit `overline delta_j` for which the
finite-window Gamma rate at `j` satisfies

```math
r_j\ge2m_*>0.
```

More explicitly, choose any certified `theta_j` with

```math
0<\theta_j<
\min\left\{
S_j^{{\rm RLD}},
\frac{\Pi_j}{\underline{\alpha}_j}
\right\}
```

and set

```math
\overline{\delta}_j
=
\delta_{{\rm req},j}
+\frac{\theta_j}{2\ell_j^2}.
```

Then

```math
Q_j=S_j^{{\rm RLD}}-\theta_j>0
```

and `r_j>=2m_*>0`.

Proof.

The equality `delta_req,j ell_j^2=Lambda_j^{LMOD}` gives

```math
Q_j
=
\gamma_{15,j}\underline{M}_j
-\overline{\epsilon}_{15,j}
-2\overline{\delta}_j\ell_j^2
=
S_j^{{\rm RLD}}-\theta_j.
```

The bound `theta_j<S_j^{RLD}` gives `Q_j>0`. The Gamma rate is

```math
r_j
=
\frac{
\underline{\alpha}_j(S_j^{{\rm RLD}}-\theta_j)
-P_j^{{\rm mark}}
}{2\ell_j}
-\overline{\Delta}_j.
```

Therefore `r_j>=2m_*` is equivalent to

```math
\underline{\alpha}_j(S_j^{{\rm RLD}}-\theta_j)
\ge
P_j^{{\rm mark}}
+2\ell_j\overline{\Delta}_j
+4\ell_jm_*.
```

Using the definitions of `P_j^{P17}` and `P_j^{target}`, this is

```math
\Pi_j-\underline{\alpha}_j\theta_j\ge0.
```

The bound `theta_j<Pi_j/underline alpha_j` gives the desired positive slack.
Thus the arbitrary window passes. `square`

### Theorem 4.6I.47z.2g: Cofinal Minimal-Debit Gamma Pass

Assume `AYM-CONF-GAMMA-MD-WORK_j` holds for every cofinal window `j`, and
assume

```math
S_j^{{\rm RLD}}>0,
\quad
\Pi_j>0
```

for every cofinal `j`. Choose `overline delta_j` by Theorem
4.6I.47z.2f for each `j`. Then

```text
AYM-CONF-GAMMA-FW-DIRECT(m_*)
```

holds, hence `AYM-CONF-GAMMA-CALC(m_*)` holds.

Proof.

For each cofinal `j`, Theorem 4.6I.47z.2f gives a legal loop-modulus debit,
positive `Q_j`, and the finite-window rate inequality `r_j>=2m_*>0`.
Together with the source tags in `AYM-CONF-GAMMA-MD-WORK_j`, these are
exactly the hypotheses of `AYM-CONF-GAMMA-FW-DIRECT(m_*)` on every cofinal
window. Theorem 4.6I.47q then gives `AYM-CONF-GAMMA-ACT-SYM(m_*)`, and
Corollary 4.6I.47g gives `AYM-CONF-GAMMA-CALC(m_*)`. `square`

### Corollary 4.6I.47z.2h: Cofinal Minimal-Debit Obstruction Classifier

If the cofinal minimal-debit Gamma pass fails, then at least one cofinal
subsequence hits a named obstruction:

| Obstruction | Scalar failure |
| --- | --- |
| minimal-debit reserve collapse | `S_j^{RLD}<=0` infinitely often or along the intended tail |
| retained-area collapse | `underline alpha_j` is zero, unproved, or too small for positive `Pi_j` |
| marked/KP pressure growth | `P_j^{mark}` prevents `Pi_j>0` |
| Paper-17 pressure growth | `P_j^{P17}` prevents `Pi_j>0` |
| target overreach | `P_j^{target}=4 ell_j m_*` prevents `Pi_j>0` |
| ledger failure | the constants are not restrictions of one frozen whole-process tower |

This is the arbitrary-window version of the first-window diagnostic. It is
the point at which Paper 18 can distinguish a real confinement-rate failure
from a bookkeeping failure.

### Proposition 4.6I.47z.3: First Window Fully Expanded Rate Inequality

The first-window Gamma rate can be written as

```math
r_0
=
\frac{
\alpha_0
\left(
\gamma_0\underline{M}_0-e_{15,0}-2\delta_0\ell_0^2
\right)
-e_0-h_0-\lambda_0-D_0
}{2\ell_0}
-\Delta_0.
```

Therefore the first window passes at target `m_*` whenever

```math
\alpha_0
\left(
\gamma_0\underline{M}_0-e_{15,0}-2\delta_0\ell_0^2
\right)
>
e_0+h_0+\lambda_0+D_0
+2\ell_0(\Delta_0+2m_*).
```

When `alpha_0>0`, this may also be read as the required lower bound on the
raw transported reserve:

```math
\gamma_0\underline{M}_0
>
e_{15,0}
+2\delta_0\ell_0^2
+\frac{e_0+h_0+\lambda_0+D_0+2\ell_0(\Delta_0+2m_*)}{\alpha_0}.
```

Proof.

Substitute the definitions of `A_0^{ret}`, `B_0^{mark}`, `C_0^{P17}`, and
`Q_0` into

```math
r_0
=
A_0^{{\rm ret}}
-B_0^{{\rm mark}}
-C_0^{{\rm P17}}.
```

This gives the first displayed expression. The condition `r_0>=2m_*>0`
is obtained by moving the marked/KP debit and Paper-17 debit to the right
side. If `alpha_0>0`, divide by `alpha_0` to obtain the final reserve lower
bound. `square`

### Corollary 4.6I.47z.4: First Window Diagnostic Outcome

The first worksheet has three honest outcomes.

1. **First-window pass:** the inequality in Proposition 4.6I.47z.3 is
   certified. Then the first window satisfies the finite-window Gamma
   inequality required by `AYM-CONF-GAMMA-FW-DIRECT(m_*)`.
2. **First-window smaller-rate pass:** the same inequality holds with
   `m_*` replaced by a smaller positive `m'_0`. Then the first window has a
   positive rate, but not the declared target.
3. **First-window obstruction:** one of the following quantities is
   unavailable or too small:

   ```text
   gamma_0 underline M_0 - e_15,0 - 2 delta_0 ell_0^2,
   E_0 or 4 omega_0/kappa_0 consuming the reserve,
   alpha_0,
   e_0+h_0+lambda_0+D_0,
   Delta_0,
   same-ledger compatibility.
   ```

The first-window pass is only a local diagnostic. Paper 18 still needs the
same calculation cofinally, or a normalized compact-tail theorem, before it
can claim the full `AYM-CONF-GAMMA-CALC(m_*)` source.

### Definition 4.6I.48: Whole-Process Ledger Audit `AYM-CONF-LEDGER-AUDIT`

`AYM-CONF-LEDGER-AUDIT` is step 7. It holds when all source certificates
above are organized over one common directed index of cutoff, volume,
smearing, block scale, probe battery, representation schedule, and endpoint
protocol, and when:

1. every finite record is a restriction or explicitly debited extension of
   the same Paper-16 whole-process law;
2. every perimeter, cusp, regulator, chart, projection, readout, loop
   modulus, marked-closure, charged-boundary, and Paper-17 mass-gap loss has
   one name and one debit entry;
3. no loss is both absorbed into `S_15,j` and subtracted again in
   `overline L_j`, `overline D_j`, or `overline Delta_j`;
4. no proof step composes unrecorded partial transition kernels;
5. all gauge-fixed fields and surfaces are auxiliary estimates for scalar
   records;
6. the final constants entering `underline Gamma_j` are computed from the
   same pushed-forward law as `AYM-CONF-LAW-SRC`.

### Definition 4.6I.48a: Canonical Confinement Debit Register `CONF-DEBIT-REG`

`CONF-DEBIT-REG` is the explicit loss register for
`AYM-CONF-LEDGER-AUDIT`. For every cofinal battery `G_j`, let `Loss_j` be
the finite set of artifact labels used in the Paper-18 proof. These labels
include only declared regulator, chart, projection, loop-modulus, readout,
counterterm, perimeter, cusp, marked-closure, charged-boundary, KP,
projective, and Paper-17 comparison artifacts.

The register consists of a disjoint partition

```math
Loss_j
=
Loss_j^S
\sqcup
Loss_j^\delta
\sqcup
Loss_j^L
\sqcup
Loss_j^D
\sqcup
Loss_j^\Delta
\sqcup
Loss_j^0
```

and nonnegative debits `d_j(x)` for `x in Loss_j`, with the following
interpretation.

1. `Loss_j^S` is the reserve-readout bucket. Its total is bounded by the
   Paper-15 transport error:

   ```math
   \sum_{x\in Loss_j^S}d_j(x)
   \le
   \overline{\epsilon}_{15,j}.
   ```

2. `Loss_j^delta` is the loop-modulus/readout bucket. Its total is bounded
   by the chosen loop-modulus scale:

   ```math
   \sum_{x\in Loss_j^\delta}d_j(x)
   \le
   \overline{\delta}_j\ell_j^2.
   ```

3. `Loss_j^L` is the marked local-loss bucket:

   ```math
   \sum_{x\in Loss_j^L}d_j(x)
   \le
   \overline{L}_j.
   ```

4. `Loss_j^D` is the connected-polymer and decorated-smallness bucket:

   ```math
   \sum_{x\in Loss_j^D}d_j(x)
   \le
   \overline{D}_j.
   ```

5. `Loss_j^\Delta` is the Paper-17 selected-rate comparison bucket:

   ```math
   \sum_{x\in Loss_j^\Delta}d_j(x)
   \le
   \overline{\Delta}_j.
   ```

6. `Loss_j^0` contains audit-only compatibility labels whose numerical
   effect is already zero after projective restriction or exact
   counterterm matching.

The disjointness is the no-double-debit rule. A counterterm mismatch, for
example, may be placed in `Loss_j^S` if it is absorbed into
`epsilon_15_to_j`, or in `Loss_j^L` if it is paid as marked local loss, but
not in both. A character-tail loss paid through `D_KP,j` may not also be
placed in `overline L_j` or `overline Delta_j`.

### Definition 4.6I.48b: Imported Whole-Process Ledger Package `CONF-IMPORT-WP`

`CONF-IMPORT-WP` holds when the following imported ledgers are available on
one common refinement of the directed towers:

1. Paper 16 `HK-WP-CLOSE`, hence `AYM-WP`;
2. Paper 17 `MG-WP`;
3. Paper 18 `CONF-WP`;
4. all source certificates from `AYM-CONF-LAW-SRC` through
   `AYM-CONF-GAMMA-CALC(m_*)` use the same finite-stage laws, comparison
   maps, counterterm branches, loop approximants, representation schedules,
   and endpoint protocols after that common refinement;
5. `CONF-DEBIT-REG` holds for every cofinal `j`;
6. if a finite object is introduced by a gauge chart, surface, sheet,
   flux-tube picture, or endpoint-color protocol, its only use is to produce
   one of the scalar record debits in `CONF-DEBIT-REG` or a scalar record
   estimate in the source certificates.

### Theorem 4.6I.48c: `CONF-IMPORT-WP` Proves `AYM-CONF-LEDGER-AUDIT`

If `CONF-IMPORT-WP` holds, then `AYM-CONF-LEDGER-AUDIT` holds.

Proof.

Paper 16 `HK-WP-CLOSE` fixes the common heat-kernel or comparison tower,
the pushed-forward laws, and the no-hidden-divisibility clause. Paper 17
`MG-WP` says that the mass-gap batteries, OS reconstruction, clustering
estimates, and selected-rate losses are restrictions of that same tower.
Paper 18 `CONF-WP` says that the Wilson-loop, Creutz, marked-polymer,
charged-boundary, and confinement batteries are also restrictions or
explicitly debited extensions of the same tower.

Clause 4 of `CONF-IMPORT-WP` puts the new source certificates on the common
refinement. Therefore every finite record used by Paper 18 is either a
restriction of the Paper-16 whole-process law or an explicitly debited
extension of it. This proves clause 1 of `AYM-CONF-LEDGER-AUDIT`.

`CONF-DEBIT-REG` gives one finite label set `Loss_j`, one disjoint bucket
assignment, and one nonnegative debit for every artifact. Thus every
perimeter, cusp, regulator, chart, projection, readout, loop-modulus,
marked-closure, charged-boundary, and Paper-17 mass-gap loss has a single
name and a single location in the ledger. This proves clause 2.

The disjoint partition in `CONF-DEBIT-REG` proves clause 3: a loss used in
the reserve bucket `Loss_j^S` cannot also appear in the loop-modulus bucket,
the marked-loss bucket, the KP bucket, or the Paper-17 rate bucket. In
particular the quantities entering

```math
\underline{\Gamma}_j
=
\underline{\alpha}_j
(\underline{S}_{15,j}-2\overline{\delta}_j\ell_j^2)
-\overline{L}_j
-\overline{D}_j
```

and the final subtraction `overline Delta_j` are non-overlapping debits.

The no-hidden-divisibility clauses of `HK-WP-CLOSE`, `MG-WP`, and `CONF-WP`
prove clause 4. Clause 6 of `CONF-IMPORT-WP` proves clause 5: all gauge-fixed
fields, surfaces, sheets, flux-tube pictures, and colored endpoint protocols
are auxiliary ways of estimating scalar records, not primitive ontology.

Finally, the common-refinement clause and the debit register ensure that
the constants entering `underline Gamma_j` are computed from the same
pushed-forward law as `AYM-CONF-LAW-SRC`; this is clause 6. Hence all clauses
of `AYM-CONF-LEDGER-AUDIT` hold. `square`

### Theorem 4.6I.49: `AYM-CONF-LEDGER-AUDIT` Proves `AYM-CONF-WP`

If `AYM-CONF-LEDGER-AUDIT` holds, then `AYM-CONF-WP` holds.

Proof.

The six audit clauses are the confinement whole-process ledger `CONF-WP`
together with the Paper-16/Paper-17 same-ledger compatibility required by
the `AYM-CONF-WP` row of Definition 4.6I.1. Therefore `AYM-CONF-WP` holds.
`square`

### Theorem 4.6I.50: Coarse Seven-Step Diagnostic Closure

This theorem is the older coarse closure route. It is retained as a
diagnostic wrapper because many earlier sections feed its seven gates
directly. The canonical endpoint of Paper 18 is the sharper minimal-debit
source closure in Theorem 4.6I.50l below.

Assume, on one actual `4D SU(N)` whole-process trajectory:

1. `AYM-CONF-LAW-SRC`;
2. `AYM-CONF-WIN-SRC`;
3. `AYM-CONF-RES-SRC`;
4. `AYM-CONF-LMOD-CALC`;
5. `AYM-CONF-MARK-CALC`;
6. `AYM-CONF-GAMMA-CALC(m_*)`;
7. `AYM-CONF-LEDGER-AUDIT`.

Then `AYM-CONF-CLOSE(m_*)` holds.

Proof.

Theorem 4.6I.37 gives `AYM-CONF-LAW`. Theorem 4.6I.39 gives
`AYM-CONF-WIN-MAP`. Theorem 4.6I.41 gives `AYM-CONF-RES-NC`. Theorems
4.6I.43 and 4.6I.29 give `AYM-CONF-LMOD-EST`. Theorems 4.6I.45 and
4.6I.31 give `AYM-CONF-MARK-UNIF`. Theorem 4.6I.47 gives
`AYM-CONF-GAMMA-LB(m_*)`. Theorem 4.6I.49 gives `AYM-CONF-WP`.
Corollary 4.6I.34 then gives `AYM-CONF-CLOSE(m_*)`. `square`

### Corollary 4.6I.50a: Paper-16 Imported Source Closure

Assume the seven hypotheses of Theorem 4.6I.50, except replace
`AYM-CONF-LAW-SRC` by `P16-LAW-IMPORT`. Then `AYM-CONF-CLOSE(m_*)` holds.

Proof.

Theorem 4.6I.36b imports `AYM-CONF-LAW-SRC` from `P16-LAW-IMPORT`. Theorem
4.6I.50 then applies. `square`

### Corollary 4.6I.50b: Imported-Law And Constructed-Window Closure

Assume the seven hypotheses of Theorem 4.6I.50, except replace
`AYM-CONF-LAW-SRC` by `P16-LAW-IMPORT` and replace
`AYM-CONF-WIN-SRC` by `AYM-CONF-WIN-SCHED`. Then
`AYM-CONF-CLOSE(m_*)` holds.

Proof.

Theorem 4.6I.36b imports `AYM-CONF-LAW-SRC` from `P16-LAW-IMPORT`. Theorem
4.6I.38c constructs `AYM-CONF-WIN-SRC` from `AYM-CONF-WIN-SCHED`. Theorem
4.6I.50 then applies. `square`

### Corollary 4.6I.50c: Imported-Law, Constructed-Window, And Calculated-Reserve Closure

Assume the seven hypotheses of Theorem 4.6I.50, except replace
`AYM-CONF-LAW-SRC` by `P16-LAW-IMPORT`, replace `AYM-CONF-WIN-SRC` by
`AYM-CONF-WIN-SCHED`, and replace `AYM-CONF-RES-SRC` by
`AYM-CONF-RES-CALC`. Then `AYM-CONF-CLOSE(m_*)` holds.

Proof.

Theorem 4.6I.36b imports `AYM-CONF-LAW-SRC`. Theorem 4.6I.38c constructs
`AYM-CONF-WIN-SRC`. Theorem 4.6I.40c proves `AYM-CONF-RES-SRC` from
`AYM-CONF-RES-CALC`. Theorem 4.6I.50 then applies. `square`

### Corollary 4.6I.50d: Symbolic/Numeric Reserve Closure

Assume the seven hypotheses of Theorem 4.6I.50, except replace
`AYM-CONF-LAW-SRC` by `P16-LAW-IMPORT`, replace `AYM-CONF-WIN-SRC` by
`AYM-CONF-WIN-SCHED`, and replace `AYM-CONF-RES-SRC` by either
`AYM-CONF-RES-SYM` or `AYM-CONF-RES-TAIL`. Then `AYM-CONF-CLOSE(m_*)`
holds.

Proof.

Theorem 4.6I.36b imports the law source. Theorem 4.6I.38c constructs the
window source. If `AYM-CONF-RES-SYM` holds, Theorem 4.6I.40e gives
`AYM-CONF-RES-CALC`; if `AYM-CONF-RES-TAIL` holds, Theorem 4.6I.40g gives
`AYM-CONF-RES-CALC`. Theorem 4.6I.40c gives `AYM-CONF-RES-SRC`, and Theorem
4.6I.50 applies. `square`

### Corollary 4.6I.50e: Symbolic/Numeric Reserve And Loop-Modulus Closure

Assume the seven hypotheses of Theorem 4.6I.50, except replace
`AYM-CONF-LAW-SRC` by `P16-LAW-IMPORT`, replace `AYM-CONF-WIN-SRC` by
`AYM-CONF-WIN-SCHED`, replace `AYM-CONF-RES-SRC` by either
`AYM-CONF-RES-SYM` or `AYM-CONF-RES-TAIL`, and replace
`AYM-CONF-LMOD-CALC` by either `AYM-CONF-LMOD-SYM` or
`AYM-CONF-LMOD-TAIL`. Then `AYM-CONF-CLOSE(m_*)` holds.

Proof.

Theorem 4.6I.36b imports the law source, and Theorem 4.6I.38c constructs
the window source. The reserve verifier gives `AYM-CONF-RES-CALC` by
Theorem 4.6I.40e or 4.6I.40g, and then `AYM-CONF-RES-SRC` by Theorem
4.6I.40c. The loop-modulus verifier gives `AYM-CONF-LMOD-CALC` by Theorem
4.6I.43b or 4.6I.43d. Theorem 4.6I.50 then applies. `square`

### Corollary 4.6I.50f: Symbolic/Numeric Reserve, Loop-Modulus, And Marked-Bridge Closure

Assume the seven hypotheses of Theorem 4.6I.50, except replace
`AYM-CONF-LAW-SRC` by `P16-LAW-IMPORT`, replace `AYM-CONF-WIN-SRC` by
`AYM-CONF-WIN-SCHED`, replace `AYM-CONF-RES-SRC` by either
`AYM-CONF-RES-SYM` or `AYM-CONF-RES-TAIL`, replace
`AYM-CONF-LMOD-CALC` by either `AYM-CONF-LMOD-SYM` or
`AYM-CONF-LMOD-TAIL`, and replace `AYM-CONF-MARK-CALC` by either
`AYM-CONF-MARK-SYM` or `AYM-CONF-MARK-TAIL`. Then
`AYM-CONF-CLOSE(m_*)` holds.

Proof.

Theorem 4.6I.36b imports the law source, and Theorem 4.6I.38c constructs
the window source. The reserve verifier gives `AYM-CONF-RES-CALC` by
Theorem 4.6I.40e or 4.6I.40g, and then `AYM-CONF-RES-SRC` by Theorem
4.6I.40c. The loop-modulus verifier gives `AYM-CONF-LMOD-CALC` by Theorem
4.6I.43b or 4.6I.43d. If `AYM-CONF-MARK-SYM` holds, Theorem 4.6I.45a.1
gives `AYM-CONF-MARK-CALC`; if `AYM-CONF-MARK-TAIL` holds, Theorem
4.6I.45b.1 gives `AYM-CONF-MARK-CALC`. Theorem 4.6I.50 then applies.
`square`

### Corollary 4.6I.50g: Fully Assembled Symbolic/Numeric Source Closure

Assume the seven hypotheses of Theorem 4.6I.50, except replace
`AYM-CONF-LAW-SRC` by `P16-LAW-IMPORT`, replace `AYM-CONF-WIN-SRC` by
`AYM-CONF-WIN-SCHED`, replace `AYM-CONF-RES-SRC` by either
`AYM-CONF-RES-SYM` or `AYM-CONF-RES-TAIL`, replace
`AYM-CONF-LMOD-CALC` by either `AYM-CONF-LMOD-SYM` or
`AYM-CONF-LMOD-TAIL`, replace `AYM-CONF-MARK-CALC` by either
`AYM-CONF-MARK-SYM` or `AYM-CONF-MARK-TAIL`, and replace
`AYM-CONF-GAMMA-CALC(m_*)` by either `AYM-CONF-GAMMA-SYM(m_*)` or
`AYM-CONF-GAMMA-TAIL(m_*)`. Then `AYM-CONF-CLOSE(m_*)` holds.

Proof.

Theorem 4.6I.36b imports the law source, and Theorem 4.6I.38c constructs
the window source. The reserve verifier gives `AYM-CONF-RES-CALC` by
Theorem 4.6I.40e or 4.6I.40g, and then `AYM-CONF-RES-SRC` by Theorem
4.6I.40c. The loop-modulus verifier gives `AYM-CONF-LMOD-CALC` by Theorem
4.6I.43b or 4.6I.43d. The marked-bridge verifier gives
`AYM-CONF-MARK-CALC` by Theorem 4.6I.45a.1 or 4.6I.45b.1. Finally, the
Gamma-rate verifier gives `AYM-CONF-GAMMA-CALC(m_*)` by Theorem
4.6I.47a.1 or 4.6I.47b.1. Theorem 4.6I.50 then applies. `square`

### Corollary 4.6I.50h: Actual-Reserve Tail Source Closure

Assume the seven hypotheses of Theorem 4.6I.50, except replace
`AYM-CONF-LAW-SRC` by `P16-LAW-IMPORT`, replace `AYM-CONF-WIN-SRC` by
`AYM-CONF-WIN-SCHED`, replace `AYM-CONF-RES-SRC` by
`AYM-CONF-RES-ACT-TAIL`, replace `AYM-CONF-LMOD-CALC` by either
`AYM-CONF-LMOD-SYM` or `AYM-CONF-LMOD-TAIL`, replace
`AYM-CONF-MARK-CALC` by either `AYM-CONF-MARK-SYM` or
`AYM-CONF-MARK-TAIL`, and replace `AYM-CONF-GAMMA-CALC(m_*)` by either
`AYM-CONF-GAMMA-SYM(m_*)` or `AYM-CONF-GAMMA-TAIL(m_*)`. Then
`AYM-CONF-CLOSE(m_*)` holds.

Proof.

Theorem 4.6I.40i gives `AYM-CONF-RES-TAIL` from
`AYM-CONF-RES-ACT-TAIL`. The rest of the proof is identical to Corollary
4.6I.50g: the law is imported by Theorem 4.6I.36b, the window source is
constructed by Theorem 4.6I.38c, the loop-modulus, marked-bridge, and
Gamma-rate calculations are supplied by their symbolic or tail verifiers,
and Theorem 4.6I.50 applies. `square`

### Corollary 4.6I.50i: Actual Reserve And Actual Loop-Modulus Source Closure

Assume the seven hypotheses of Theorem 4.6I.50, except replace
`AYM-CONF-LAW-SRC` by `P16-LAW-IMPORT`, replace `AYM-CONF-WIN-SRC` by
`AYM-CONF-WIN-SCHED`, replace `AYM-CONF-RES-SRC` by
`AYM-CONF-RES-ACT-TAIL`, replace `AYM-CONF-LMOD-CALC` by either
`AYM-CONF-LMOD-ACT-SYM` or `AYM-CONF-LMOD-ACT-TAIL`, replace
`AYM-CONF-MARK-CALC` by either `AYM-CONF-MARK-SYM` or
`AYM-CONF-MARK-TAIL`, and replace `AYM-CONF-GAMMA-CALC(m_*)` by either
`AYM-CONF-GAMMA-SYM(m_*)` or `AYM-CONF-GAMMA-TAIL(m_*)`. Then
`AYM-CONF-CLOSE(m_*)` holds.

Proof.

Theorem 4.6I.40i gives `AYM-CONF-RES-TAIL` from
`AYM-CONF-RES-ACT-TAIL`, hence Theorem 4.6I.40g gives
`AYM-CONF-RES-CALC` and Theorem 4.6I.40c gives `AYM-CONF-RES-SRC`.

If `AYM-CONF-LMOD-ACT-SYM` holds, Corollary 4.6I.43i gives
`AYM-CONF-LMOD-CALC`. If `AYM-CONF-LMOD-ACT-TAIL` holds, the same corollary
again gives `AYM-CONF-LMOD-CALC`. The law is imported by Theorem 4.6I.36b,
the window source is constructed by Theorem 4.6I.38c, the marked-bridge and
Gamma-rate calculations are supplied by their symbolic or tail verifiers, and
Theorem 4.6I.50 applies. `square`

### Corollary 4.6I.50j: Actual Reserve, Loop-Modulus, And Marked-Bridge Source Closure

Assume the seven hypotheses of Theorem 4.6I.50, except replace
`AYM-CONF-LAW-SRC` by `P16-LAW-IMPORT`, replace `AYM-CONF-WIN-SRC` by
`AYM-CONF-WIN-SCHED`, replace `AYM-CONF-RES-SRC` by
`AYM-CONF-RES-ACT-TAIL`, replace `AYM-CONF-LMOD-CALC` by either
`AYM-CONF-LMOD-ACT-SYM` or `AYM-CONF-LMOD-ACT-TAIL`, replace
`AYM-CONF-MARK-CALC` by either `AYM-CONF-MARK-ACT-SYM` or
`AYM-CONF-MARK-ACT-TAIL`, and replace `AYM-CONF-GAMMA-CALC(m_*)` by either
`AYM-CONF-GAMMA-SYM(m_*)` or `AYM-CONF-GAMMA-TAIL(m_*)`. Then
`AYM-CONF-CLOSE(m_*)` holds.

Proof.

Corollary 4.6I.43i turns either actual loop-modulus source into
`AYM-CONF-LMOD-CALC`. Corollary 4.6I.45g turns either actual marked-bridge
source into `AYM-CONF-MARK-CALC`. The reserve source is handled by Theorem
4.6I.40i, Theorem 4.6I.40g, and Theorem 4.6I.40c as in Corollary
4.6I.50i. The law is imported by Theorem 4.6I.36b, the window source is
constructed by Theorem 4.6I.38c, the Gamma-rate calculation is supplied by
its symbolic or tail verifier, and Theorem 4.6I.50 applies. `square`

### Corollary 4.6I.50k: Actual Source Closure Through The Physical Gamma Rate

Assume the seven hypotheses of Theorem 4.6I.50, except replace
`AYM-CONF-LAW-SRC` by `P16-LAW-IMPORT`, replace `AYM-CONF-WIN-SRC` by
`AYM-CONF-WIN-SCHED`, replace `AYM-CONF-RES-SRC` by
`AYM-CONF-RES-ACT-TAIL`, replace `AYM-CONF-LMOD-CALC` by either
`AYM-CONF-LMOD-ACT-SYM` or `AYM-CONF-LMOD-ACT-TAIL`, replace
`AYM-CONF-MARK-CALC` by either `AYM-CONF-MARK-ACT-SYM` or
`AYM-CONF-MARK-ACT-TAIL`, and replace `AYM-CONF-GAMMA-CALC(m_*)` by either
`AYM-CONF-GAMMA-ACT-SYM(m_*)` or `AYM-CONF-GAMMA-ACT-TAIL(m_*)`. Then
`AYM-CONF-CLOSE(m_*)` holds.

Proof.

The law, window, reserve, loop-modulus, and marked-bridge source reductions
are exactly those used in Corollary 4.6I.50j. Corollary 4.6I.47g turns
either actual Gamma-rate source into `AYM-CONF-GAMMA-CALC(m_*)`. Therefore
all seven hypotheses of Theorem 4.6I.50 are restored, and
`AYM-CONF-CLOSE(m_*)` follows. `square`

The corollaries above are coarse diagnostic variants. They should not be
read as the final proof route, because the finite-window minimal-debit
analysis has since localized the real source problem more sharply.

### Theorem 4.6I.50l: Final Minimal-Debit Conditional Completion

Assume, on one actual `4D SU(N)` whole-process trajectory:

1. `P16-LAW-IMPORT`;
2. `AYM-CONF-WIN-SCHED`;
3. `AYM-CONF-ACT-CRES-P16(c_R)`;
4. `AYM-CONF-ACT-KQ-RATE(W_R)`;
5. `c_R >= C_quot^crit(s_R,W_R)` for some `s_R>0`;
6. `AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)`;
7. `AYM-CONF-ACT-PI-THRESH(s_P,m_*)` for some `s_P>0`;
8. `AYM-CONF-ACT-LEDGER-SRC`;
9. `AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)`.

Then the finite-window Gamma route closes:

```text
AYM-CONF-GAMMA-FW-DIRECT(m_*).
```

Moreover the actual-confinement certificate closes:

```text
AYM-CONF-CLOSE(m_*)
=> MGAP(m_*).
```

Proof.

Theorem 4.6I.36b imports `AYM-CONF-LAW-SRC` from `P16-LAW-IMPORT`.
Theorem 4.6I.38c constructs `AYM-CONF-WIN-SRC` from
`AYM-CONF-WIN-SCHED`. Theorem 4.6I.47z.2e.24i, applied to clauses 3--5,
gives `AYM-CONF-ACT-RLD-TAIL`. Theorem 4.6I.47z.2e.24r, applied to
clauses 6 and 7, gives `AYM-CONF-ACT-PI-TAIL(m_*)`. Theorem
4.6I.47z.2e.24w, applied to clause 8, gives
`AYM-CONF-ACT-LEDGER-TAIL`. Theorem 4.6I.47z.2e.24aa, applied to clause 9,
gives `AYM-CONF-ACT-COF(m_*)`.

Theorem 4.6I.47z.2e.24ac then gives
`AYM-CONF-GAMMA-FW-DIRECT(m_*)`.

The same clauses also populate Definition 4.6I directly. Clauses 1 and 2
give the Wilson-loop law and finite Creutz windows. The reserve-loop
closure gives the positive reserve and admissible loop-modulus debit in
clauses 3 and 4. The pressure closure gives the single-window closing
inequality and selected-rate surplus in clauses 5 and 6. The ledger and
cofinal-source clauses give the same-tower and cofinal-survival requirement
in clause 7. Hence `AYM-CONF-CLOSE(m_*)` holds. Corollary 4.6K then gives
`MGAP(m_*)`. `square`

This is as far as Paper 18 can honestly push the proof without importing
new nonperturbative source estimates for actual `4D SU(N)` confinement. The
remaining task is no longer conceptual: prove or falsify the source gates in
the checklist of Section 0F on the actual continuum trajectory.

### Theorem 4.6J: `AYM-CONF-CLOSE` Proves Actual `COF-P15-CREUTZ`

If `AYM-CONF-CLOSE(m_*)` holds for the declared actual `4D SU(N)` trajectory,
then `COF-P15-CREUTZ(m_*)` holds for that trajectory.

Proof.

Unpack `AYM-CONF-CLOSE(m_*)` through the workbench of Definition 4.6I.1.
The subcertificates `AYM-CONF-WIN`, `AYM-CONF-RES`, `AYM-CONF-LMOD`,
`AYM-CONF-SWIN`, `AYM-CONF-MARK`, and `AYM-CONF-WP` are exactly the
hypotheses of Corollary 4.6I.14. Hence, for every cofinal battery `G_j`,
clauses 1--4 of `COF-P15-CREUTZ(m_*)` hold: the `j`-level Paper-15 Creutz
pass, marked geometry/loss, marked KP stability, and the strict Creutz branch
reserve `R_j^Creutz>D_KP,j`.

The remaining clause of `COF-P15-CREUTZ(m_*)` is the uniform normalized rate
surplus. This is precisely `AYM-CONF-RATE`, the sixth subcertificate of
`AYM-CONF-CLOSE(m_*)`:

```math
\inf_j
\left[
{G_j^{{\rm Creutz}}\over\ell_j}
-\Delta_{{\rm conf},j}
\right]
\ge
2m_*
>
0.
```

The subcertificates `AYM-CONF-LAW` and `AYM-CONF-WP` ensure that these
estimates are attached to the same continuum closed-loop record law and the
same debit ledger required by `CONF-REC` and `CONF-WP`. Therefore every clause
of `COF-P15-CREUTZ(m_*)` holds. `square`

### Corollary 4.6K: Actual-Trajectory Confinement Closure Gives Mass Gap

Assume:

1. Paper 17 `MG-OS-CLOSE`, cofinal `MG-OBS`, and `MG-WP`;
2. `AYM-CONF-CLOSE(m_*)` for the actual `4D SU(N)` trajectory.

Then `MGAP(m_*)` holds in the declared gauge-invariant OS sector.

Proof.

Theorem 4.6J gives `COF-P15-CREUTZ(m_*)`. Corollary 4.6H gives
`MGAP(m_*)`. `square`

### Lemma 4.6L: Strong-Coupling Area Law Alone Does Not Close The Actual Trajectory

Suppose a finite-lattice strong-coupling expansion proves an area law for
bare couplings in a compact interval away from the asymptotically-free
continuum trajectory. This fact alone does not prove
`AYM-CONF-CLOSE(m_*)`.

Proof.

The actual `4D SU(N)` continuum trajectory used in Paper 16 is an
asymptotically-free trajectory: the cutoff is removed while the running
coupling approaches the continuum scaling regime. A strong-coupling area
law at fixed coarse bare coupling proves an estimate on a different part of
the lattice parameter space. To use it here, one must prove a transport
theorem that carries a positive renormalized area or Creutz reserve from
the strong-coupling regime to the declared continuum trajectory, while
debiting regulator, volume, block, loop-shape, projective, and counterterm
losses on the same whole-process ledger.

That missing transport theorem is precisely the kind of estimate recorded
in `AYM-CONF-CLOSE`: the cofinal inequalities for `S_15,j`,
`CR-LMOD-QUANT_j`, the single-window Creutz closing inequality, and the
uniform rate surplus. Without those estimates, the strong-coupling theorem
is a useful model calculation but not an actual-continuum confinement proof.
`square`

### Lemma 4.6M: No-Smuggling Principle For Actual Confinement

Within the ISP/Barandes-aligned ontology of this paper, actual confinement
may enter the mass-gap proof only through scalar record-law inequalities:
`CONF-AL`, `CONF-CR`, `COF-P15-CREUTZ`, `CONF-COFINAL-PASS`, or the explicit
actual-trajectory certificate `AYM-CONF-CLOSE`. It may not be inferred from
field pictures, gauge-fixed sheets, flux-tube language, or a partially
specified Markov kernel.

Proof.

Definitions 3.6 and 3.7 require all confinement estimates to be evaluated
on one whole-process record law and one loss ledger. Theorems 4.6B, 4.6E,
4.6H, and 4.6K use only scalar loop-record estimates, marked record
cumulants, and selected-rate inequalities. The auxiliary objects in the
proof, such as surfaces, sheets, polymers, and gauge charts, are eliminated
into those scalar inequalities before Paper 17 is invoked. Therefore any
argument that does not export one of the named scalar certificates has not
provided an admissible input to the mass-gap proof. `square`

### Theorem 4.7: `CONF-COMP` Gives Paper-17 Marked KP And Uniform Reserve

Assume `CONF-COMP(sigma,m_*)`. Then:

```text
G_j-2PT-KP for every j,
MG-UNIF(m_*).
```

Proof.

`CONF-COMP(sigma,m_*)` includes the cofinal pass gate
`CONF-COFINAL-PASS(m_*)`. Theorem 4.6A gives `G_j-2PT-KP` for every `j` and
`MG-UNIF(m_*)`. `square`

### Corollary 4.8: Confinement Completion Gives Paper-17 Mass Gap

Assume:

1. Paper 16 `CYM_WL`;
2. Paper 17 `MG-OS-CLOSE`, cofinal `MG-OBS`, and `MG-WP`;
3. `CONF-COMP(sigma,m_*)`.

Then `MGAP(m_*)` holds in the declared gauge-invariant OS sector.

Proof.

Theorem 4.7 gives `G_j-2PT-KP` for every `j` and `MG-UNIF(m_*)`. Paper 17,
Theorem 9.3 then gives `MGAP(m_*)`. `square`

## 5. ISP Definition Of 4D Pure Quantum Gauge Theory

### Definition 5.1: Four-Dimensional Pure Gauge Theory In ISP

A four-dimensional pure quantum gauge theory in the ISP sense is a
whole-process law of scalar closed-loop records satisfying:

1. `CYM_WL`: a continuum Wilson-loop functional with reflection positivity,
   Euclidean covariance, gauge invariance, loop continuity, nontriviality,
   and whole-process compatibility;
2. `MG-OS-CLOSE`: OS reconstruction with strongly continuous Euclidean time
   semigroup on the declared gauge-invariant OS sector;
3. cofinal `MG-OBS`: a dense operational gauge-invariant loop-record probe
   family;
4. `MG-WP`: all constructions use one whole-process tower and one ledger.

This is a precise definition of the record-theoretic object. It does not by
itself assert confinement or a mass gap.

### Definition 5.2: Completed Mass-Gapped Confining 4D Gauge Theory

The theory is completed as a mass-gapped confining 4D gauge theory when, in
addition to Definition 5.1, it satisfies `CONF-COMP(sigma,m_*)` for some
`sigma>0` and `m_*>0`.

Then Corollary 4.8 supplies the positive mass gap.

## 6. Obstruction Ledger

At the current endpoint, Paper 18 has eliminated many vague failure modes.
Assuming the Paper-16 continuum Wilson-loop law exists, failure of the
actual-continuum confinement proof must now occur in one of the following
typed places.

1. **Law-source failure:** `P16-LAW-IMPORT` fails to provide the required
   reflection-positive, Euclidean-covariant, gauge-invariant, loop-continuous,
   nontrivial, same-ledger Wilson-loop law for the Paper-18 loop families.
2. **Window-source failure:** `AYM-CONF-WIN-SCHED` fails to map the Paper-17
   cofinal probe batteries into finite Creutz windows and Paper-15 batteries
   on the same directed tower.
3. **Reserve-source failure:** the actual trajectory does not prove
   `AYM-CONF-RES-SRC`. In the narrowed step-1 route this is the failure of
   `AYM-CONF-ACT-CRES-P16(c_R)`: Paper 16 does not provide either a raw
   surface reserve `M_SUB^{bd}>=c_R>0` in the same block units, or an
   already-debited Creutz reserve with the Paper-18 extraction losses set to
   zero. Equivalently, after the Paper-15/Paper-16 extraction debits, the
   scalar reserve

   ```text
   underline S_15,j = underline gamma_j underline M_j - overline epsilon_15,j
   ```

   is not positive on the needed finite windows or has no usable cofinal
   normalized lower bound.
4. **Loop-modulus failure:** `AYM-CONF-LMOD-SRC` fails. Typical causes are
   collapsed raw Wilson-loop denominators, loop/readout errors larger than
   the normalized reserve, or failure of `AYM-CONF-ACT-KQ-RATE(W_R)`: the
   Paper-16 loop-continuity selector cannot drive the error gauge below the
   moving denominator scale `W_R d_j` on the same cofinal tower.
5. **Marked-bridge failure:** `AYM-CONF-MARK-SRC` fails. This can occur
   because endpoint-enlarged `FBE_j^S` is unavailable, positive
   `nCPSC_j^S` is not proved on the same battery, endpoint marking is not
   finite, or the character-tail margin satisfies only pointwise
   `eta_ch,j<1` with no uniform `eta_ch,j<=eta_M<1` on a cofinal tail.
   In the narrowed step-2 route this appears as failure of
   `AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)` to export a positive retained-area
   lower bound and finite endpoint/KP debits on the same tower.
6. **Gamma-rate failure:** `AYM-CONF-GAMMA-CALC(m_*)` fails. In the compact
   tail route this is exactly the failure of

   ```text
   alpha_G q_G/2 - b_G - Delta_G >= 2m_* > 0.
   ```

   Thus either `q_G` collapses, `b_G` or `Delta_G` diverges, or the final
   normalized margin is nonpositive for the target rate.
   In the finite-window minimal-debit route, this has now been sharpened to
   the four actual-constant failures:

   ```text
   AYM-CONF-ACT-RLD_j fails,
   AYM-CONF-ACT-PI_j(m_*) fails,
   AYM-CONF-ACT-LEDGER_j fails,
   or AYM-CONF-ACT-COF(m_*) fails.
   ```

   These are respectively reserve-loop surplus failure, pressure-surplus
   failure, same-ledger failure, and cofinal-survival failure.
   The pressure-surplus failure has now been sharpened further:

   ```text
   AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*) fails,
   AYM-CONF-ACT-PI-THRESH(s_P,m_*) fails,
   or the target rate m_* must be lowered.
   ```
7. **Debit-ledger failure:** `AYM-CONF-LEDGER-AUDIT` fails because some
   counterterm, projection, endpoint, character-tail, regulator, volume, or
   smearing loss is omitted, paid twice, or imported from a different
   whole-process tower.
   In the narrowed step-3 route this appears as failure of
   `AYM-CONF-ACT-LEDGER-SRC`: there is no single `Law_*`, no disjoint debit
   register, or no typed endpoint scalarization that makes the step-1 and
   step-2 constants admissible together.
8. **Cofinal-survival failure:** `AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)` fails.
   The local windows may pass one by one, but they do not form a cofinal
   scheduled family on which RLD-tail, PI-tail, ledger-tail, and the local
   worksheets all overlap.
9. **Ontology failure:** the argument uses a flux tube, colored endpoint,
   gauge-fixed field, or partial transition kernel as a primitive rather than
   eliminating it into scalar loop records and typed boundary protocols.
10. **Transport failure:** a strong-coupling, model-regime, gauge-chart, or
   finite-regulator area law is proved, but no same-ledger transport theorem
   carries a positive scalar reserve to the declared continuum
   asymptotically-free trajectory.

These are not philosophical objections. They are the exact places where the
current proof ledger can be checked, improved, or falsified.

## 7. Honest Status And Paper 19 Handoff

The canonical Paper-18 endpoint is now the minimal-debit finite-window
closure, not the older coarse seven-step route. Paper 18 proves the
conditional implication

```text
P16-LAW-IMPORT
+ AYM-CONF-WIN-SCHED
+ AYM-CONF-ACT-CRES-P16(c_R)
+ AYM-CONF-ACT-KQ-RATE(W_R)
+ c_R >= C_quot^crit(s_R,W_R)
+ AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)
+ AYM-CONF-ACT-PI-THRESH(s_P,m_*)
+ AYM-CONF-ACT-LEDGER-SRC
+ AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)
=> AYM-CONF-GAMMA-FW-DIRECT(m_*)
=> AYM-CONF-CLOSE(m_*)
=> MGAP(m_*).
```

This is a completed conditional architecture and obstruction ledger. It is
not an unconditional proof of actual `4D SU(N)` confinement, the Clay
mass-gap theorem, or an unconditional construction of continuum Yang-Mills.
The unresolved work has been reduced to the source gates in Section 0F.

Paper 18 should stop here. Paper 19 should begin with the actual source
estimates, in this order:

1. prove or falsify `AYM-CONF-ACT-CRES-P16(c_R)`;
2. prove or falsify `AYM-CONF-ACT-KQ-RATE(W_R)`;
3. test the scalar reserve-loop threshold `c_R >= C_quot^crit(s_R,W_R)`;
4. only after step 3 passes, prove or falsify
   `AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)` and
   `AYM-CONF-ACT-PI-THRESH(s_P,m_*)`;
5. audit `AYM-CONF-ACT-LEDGER-SRC` and
   `AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)` on the same frozen tower.

The detailed audit trail below is retained to show how the paper reached
this endpoint. The source-gate checklist in Section 0F is the operative
handoff to Paper 19.

### Detailed Audit Trail

Paper 18 is now a rigorous conditional bridge from Paper 17's mass-gap
theorem to a possible actual four-dimensional gauge-theory example. Its
formal architecture is complete:

```text
P16-LAW-IMPORT
+ AYM-CONF-WIN-SRC
+ AYM-CONF-RES-SRC
+ AYM-CONF-LMOD-SRC
+ AYM-CONF-MARK-SRC
+ AYM-CONF-GAMMA-CALC(m_*)
+ AYM-CONF-LEDGER-AUDIT
=> AYM-CONF-CLOSE(m_*)
=> MGAP(m_*).
```

The paper also makes the strongest compact tail route explicit:

```text
AYM-CONF-RES-RC-TAIL
+ AYM-CONF-LMOD-RC-TAIL
+ AYM-CONF-MARK-RC-TAIL
+ AYM-CONF-GAMMA-RC-TAIL(m_*)
=> AYM-CONF-CLOSE(m_*)
```

provided all gates are supplied on the same whole-process tower and the
Gamma margin

```text
alpha_G q_G/2 - b_G - Delta_G >= 2m_* > 0
```

passes. This is a conditional theorem, not an unconditional proof that the
actual continuum `4D SU(N)` trajectory has those constants.

The finite-window route has now been sharpened further. The actual source
work has four named constants tasks, with worksheet margins feeding them:

```text
AYM-CONF-ACT-WORK_j
+ AYM-CONF-ACT-RLD-WORK_j with Sigma_j^RLD>0
+ AYM-CONF-ACT-RLD-ASYM
+ AYM-CONF-ACT-RLD-SRC-ATTACK or AYM-CONF-ACT-RLD-SRC-FALS
+ AYM-CONF-ACT-RLD-THRESH(s_R)
+ AYM-CONF-ACT-CRES-P16(c_R) => AYM-CONF-ACT-CRES-LOW(c_R)
+ AYM-CONF-ACT-CRES-LOW(c_R)
+ AYM-CONF-ACT-KAPPA-SEP(k_R) or AYM-CONF-ACT-KAPPA-QUOT(W_R)
+ AYM-CONF-ACT-KQ-LMOD(W_R) => AYM-CONF-ACT-KAPPA-QUOT(W_R)
+ AYM-CONF-ACT-KQ-RATE(W_R) => AYM-CONF-ACT-KQ-LMOD(W_R)
+ [AYM-CONF-ACT-CRES-P16(c_R)
+  AYM-CONF-ACT-KQ-RATE(W_R)
+  c_R >= C_quot^crit(s_R,W_R)]
+ => AYM-CONF-ACT-RLD-TAIL
+ AYM-CONF-ACT-RNUM-TAIL + AYM-CONF-ACT-BDEB-TAIL
+ first tail RLD inequality R_R-B_R>=s_R>0
+ AYM-CONF-ACT-RLD-TAIL or reindexed RLD pass
+ AYM-CONF-ACT-PI-WORK_j(m_*) with Sigma_j^PI(m_*)>0
+ AYM-CONF-ACT-PI-ASYM
+ AYM-CONF-ACT-PNUM-TAIL + AYM-CONF-ACT-PDEB-TAIL(m_*)
+ first tail PI inequality A_P-K_P-T_P(m_*)>=s_P>0
+ AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*) => AYM-CONF-ACT-PNUM-TAIL + AYM-CONF-ACT-PDEB-TAIL(m_*)
+ AYM-CONF-ACT-PI-THRESH(s_P,m_*)
+ [AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)
+  AYM-CONF-ACT-PI-THRESH(s_P,m_*)]
+ => AYM-CONF-ACT-PI-TAIL(m_*)
+ AYM-CONF-ACT-PI-TAIL(m_*) or reindexed PI pass
+ AYM-CONF-ACT-LEDGER-SRC => AYM-CONF-ACT-LEDGER-TAIL
+ AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*) => AYM-CONF-ACT-COF-WORK(m_*) => AYM-CONF-ACT-COF(m_*)
+ [AYM-CONF-ACT-RLD-TAIL
+  AYM-CONF-ACT-PI-TAIL(m_*)
+  AYM-CONF-ACT-LEDGER-TAIL
+  AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)]
+ => AYM-CONF-GAMMA-FW-DIRECT(m_*)
+ AYM-CONF-ACT-COF-WORK(m_*)
=>
AYM-CONF-ACT-RLD_j
+ AYM-CONF-ACT-PI_j(m_*)
+ AYM-CONF-ACT-LEDGER_j
+ AYM-CONF-ACT-COF(m_*)
=> AYM-CONF-GAMMA-FW-DIRECT(m_*).
```

So the remaining open mathematical question is not whether the bookkeeping
can close. It can. The open question is whether the actual continuum
`4D SU(N)` record law supplies those four scalar certificates with positive
cofinal margin.

For step 1 specifically, Paper 18 has reached its formal endpoint:

```text
AYM-CONF-ACT-CRES-P16(c_R)
+ AYM-CONF-ACT-KQ-RATE(W_R)
+ c_R >= C_quot^crit(s_R,W_R)
=> AYM-CONF-ACT-RLD-TAIL.
```

This is a completed conditional proof of the reserve-loop gate, not an
unconditional proof of actual confinement. The unproved source content is
now exactly the Paper-16/Paper-15 raw reserve, the loop-continuity rate
selector, and the final scalar threshold comparison.

For step 2, Paper 18 has now reached the parallel formal endpoint:

```text
AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)
+ AYM-CONF-ACT-PI-THRESH(s_P,m_*)
=> AYM-CONF-ACT-PI-TAIL(m_*).
```

This is a completed conditional proof of the pressure-surplus gate. The
unproved source content is exactly the retained-area export, endpoint/KP
debit bounds, Paper-17 selected-rate product bound, and final scalar
pressure threshold on the same tower.

For step 3, Paper 18 has reached the same formal endpoint:

```text
AYM-CONF-ACT-LEDGER-SRC
=> AYM-CONF-ACT-LEDGER-TAIL.
```

This is a completed conditional proof of same-ledger compatibility. The
unproved source content is exactly the existence of one frozen law, one
restriction family, one disjoint debit register, and typed endpoint
scalarization for the RLD and PI constants.

For step 4, Paper 18 has reached the cofinal-survival endpoint:

```text
AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)
=> AYM-CONF-ACT-COF(m_*).
```

Together, steps 1--4 now give:

```text
AYM-CONF-ACT-RLD-TAIL
+ AYM-CONF-ACT-PI-TAIL(m_*)
+ AYM-CONF-ACT-LEDGER-TAIL
+ AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)
=> AYM-CONF-GAMMA-FW-DIRECT(m_*).
```

This is the completed conditional finite-window Gamma route. It remains
conditional because the actual `4D SU(N)` constants must still satisfy the
source imports and scalar thresholds.

The draft still proves only reductions:

```text
CONF-COMP(sigma,m_*)
=> G_j-2PT-KP for all j + MG-UNIF(m_*)
=> Paper-17 MGAP(m_*).
```

The reduction is now split into named gates:

```text
CONF-REC
+ CONF-WP
+ [CR-MTD + CR-LMOD => CR-DOM^cof]
+ [CH-BDY-PROT => CH-BDY]
+ CONF-AL or CONF-CR
+ [MARK-GEOM_j + MARK-LOSS_j => AL2MARK_j]
+ [AL2MARK_j => CONF-MARK_j]
+ MS-KP_j
+ G_j-CONF-PASS for every j
+ CONF-COFINAL-PASS(m_*)
=> G_j-2PT-KP for all j + MG-UNIF(m_*).
```

The record-domain side is now reduced: finite-window `CR-DOM` follows from
positive-main-term dominance `CR-MTD` plus loop-continuity modulus
`CR-LMOD`, cofinal legality follows by covering the Creutz records with
finite windows, and `CH-BDY` follows from finite-regulator scalarized
charged-boundary protocols. These reductions do not prove confinement; they
make the charged and Creutz records legal inputs for a confinement proof.

The first-battery Creutz confinement input has now been reduced as well:

```text
CR-MTD_box(sigma,delta_box,kappa_CR,box)
+ CR-LMOD_box(delta_box,kappa_CR,box)
+ positive Paper-12/Paper-16 counterterms
=> CONF-CR_box(sigma).
```

This is stronger than Creutz-domain legalization. `CR-MTD_box` must provide
a finite-stage lower bound for the Creutz ratio itself, with a positive
main term beating its signed remainder. `CR-LMOD_box` must then transport
that lower bound through the finite-window log-ratio modulus. The theorem is
a clean reduction; the actual four-dimensional `SU(N)` problem is to prove
these two first-battery ledgers on the continuum trajectory.

The log-ratio side is no longer a black box. The paper now proves that
finite-window loop-expectation continuity gives `CR-LMOD_box` once the four
Creutz-slot expectations are bounded below:

```text
loop lower bound kappa_CR,box
+ 4 omega_CR,box(alpha)/kappa_CR,box <= delta_box s_0^2
=> CR-LMOD_box(delta_box,kappa_CR,box).
```

The practical reduction uses generic `CR-MTD` and `CR-LMOD` to provide the
finite-stage lower bound, continuum Creutz domain, and loop modulus.
The positive main-term side is now reduced to the Paper-15 reserve route:

```text
P15-CR-RES_box
+ CR-ERR_box(delta_box)
+ S_15,box >= (sigma+2 delta_box)s_0^2
=> CR-MTD_box(sigma,delta_box,kappa_CR,box).
```

Here `S_15,box=gamma_15,box M_15^{bd}-epsilon_15_to_box`. The explicit
`CR-ERR_box` budget records only first-battery errors not already debited in
Paper 15's `Delta_dec^{bd}` or `T_loss^{bd}`. Thus the remaining hard
first-battery Creutz input is now sharply localized: prove the Paper-15
reserve applies to the first-battery cells with positive calibrated surplus
after the extra error budget.

This has now been packaged into the stronger first-battery pass certificate:

```text
P15-CREUTZ-PASS_box(sigma,delta_box,kappa_CR,box)
=> CONF-CR_box(sigma).
```

That certificate bundles the generic Creutz positivity ledger,
`P15-CR-RES_box`, `CR-ERR_box`, `CR-LMOD_box`, positive Paper-12/Paper-16
counterterms, and the upstream surplus inequality
`S_15,box >= (sigma+2 delta_box)s_0^2` on a single whole-process tower.

The marked bridge side is now reduced as well:

```text
MARK-GEOM_j + MARK-LOSS_j + CONF-AL or CONF-CR
=> AL2MARK_j
=> CONF-MARK_j.
```

Here `MARK-GEOM_j` supplies the closure map, positive area-to-hull
comparison, endpoint locality, and record compatibility. `MARK-LOSS_j`
keeps endpoint collars, tiling remainders, and perimeter/cusp/counterterm
losses in a single debit ledger. This is still conditional on proving those
geometry and loss ledgers for the actual continuum trajectory.

For the first plaquette-clover battery, both finite-battery halves have now
been proved under the standard block-face hull convention and same-ledger
local loss bounds:

```text
G_box block-face hulls
=> MARK-GEOM_box
```

The proof constructs one closed scalar plaquette loop for each retained
block face and finitely many endpoint-collar loops. It exports
`N_cl,box=1`, `c_geom,box=alpha_box s_0`, and a finite
`b_area,box`.

```text
same-ledger local collar/counterterm/tiling bounds
=> MARK-LOSS_box.
```

The loss theorem exports
`epsilon_area0,box=epsilon_collar,box=0`,
`epsilon_ctr,box=log M_ctr,box`, and
`epsilon_tile,box=log M_tile,box`. In the clean direct area-law branch with
identical Paper-12 counterterms and no Creutz tiling fallback, this gives
`epsilon_area,box=0`. In the transport branch, the nonzero loss is explicit
and must be beaten by the first-battery margin.

The first-battery marked KP gate has also been reduced to earlier-paper
imports:

```text
Paper-14 FBE_box
+ Paper-15 positive nCPSC_box after endpoint enlargement to G_box
+ Paper-17 endpoint-marking ledger
=> BOX-MSKP-IMPORT
=> MS-KP_box.
```

This imports the finite constants
`A_box^S`, `C_cum,box^S`, `h_box^S`, `r_box^S`,
`eta_ch,box`, `lambda_mark,box^S`, `c_box^S(O,P)`, and `B_box(O,P)`.
The step is a reduction, not a new proof of positive `nCPSC` on the actual
continuum trajectory.

The compact first-battery constants ledger is now explicit. It isolates the
only reserve comparison used by the branch proof:

```text
D_KP,box
= log((C_cum,box^S A_box^S + 1 - eta_ch,box)/(1 - eta_ch,box)),
R_clean,box = alpha_box sigma s_0^2 - h_box^S - lambda_mark,box^S,
R_Creutz,box
= alpha_box sigma s_0^2 - log M_ctr,box - log M_tile,box
  - h_box^S - lambda_mark,box^S.
```

The branch pass is now packaged as a named certificate:

```text
BOX-RESERVE-PASS(beta)
=> BOX-CONF-PASS.
```

This certificate requires the matching branch input, `BOX-MSKP-IMPORT`,
`MARK-GEOM_box`, `MARK-LOSS_box`, and the strict reserve inequality
`R_beta,box>D_KP,box` on one tower.

The Paper-15 Creutz route now has its own explicit pass-through theorem:

```text
P15-CREUTZ-PASS_box
+ BOX-MSKP-IMPORT
+ MARK-GEOM_box
+ MARK-LOSS_box
+ R_Creutz,box > D_KP,box
=> BOX-RESERVE-PASS(Creutz)
=> BOX-CONF-PASS.
```

The final Paper-15 Creutz route has exactly two numerical reserve checks:

```text
S_15,box >= (sigma+2 delta_box)s_0^2,
R_Creutz,box > D_KP,box.
```

The first check produces the effective Creutz coefficient `sigma`; the
second checks that this coefficient survives the marked-surface entropy,
endpoint marking, counterterm, and tiling losses.

The paper now also states the exact nonempty-interval test for choosing
such a `sigma`. With

```text
delta_req,box = max(E_box^*/s_0^2,
                   4 omega_box^*/(kappa_CR,box s_0^2)),
L_Creutz,box = log M_ctr,box + log M_tile,box
               + h_box^S + lambda_mark,box^S,
```

the first-battery Paper-15 Creutz route has room only if one can choose
`delta_box>=delta_req,box` such that

```text
alpha_box(S_15,box - 2 delta_box s_0^2)
> L_Creutz,box + D_KP,box.
```

This single inequality is the current sharp first-battery target. It
simultaneously checks the upstream Creutz extraction and the downstream
marked-KP reserve.

The clean first-battery pass theorem is now explicit:

```text
CONF-AL(sigma)
+ G_box block-face hulls
+ same-counterterm direct branch
+ BOX-RESERVE-PASS(clean)
=> BOX-CONF-PASS.
```

The reserve is
`R_clean,box=alpha_box sigma s_0^2-h_box^S-lambda_mark,box^S`. The KP
threshold `D_KP,box` is the explicit logarithmic residual/decorated
smallness threshold from Theorem 4.3B.1. This is a genuine finite-battery
positive statement, not merely a relabeling of the `BOX-CONF-PASS`
definition.

The Creutz fallback pass theorem is explicit as well:

```text
CONF-CR(sigma)
+ G_box block-face hulls
+ same-ledger local loss bounds
+ BOX-RESERVE-PASS(Creutz)
=> BOX-CONF-PASS.
```

Here
`R_Creutz,box=alpha_box sigma s_0^2-log M_ctr,box-log M_tile,box-h_box^S-lambda_mark,box^S`.
This is the more operational branch: Creutz cells are finite record
comparisons, not physical sheets, and every extra cost is visible in the
reserve.

These two branches are now packaged into a first-battery worksheet:

```text
A_box^branch = available clean/Creutz branches,
R_best,box = max_{beta in A_box^branch} R_beta,box,
R_best,box > D_KP,box
=> BOX-RESERVE-PASS(beta_best)
=> BOX-CONF-PASS.
```

With Paper 17 `BOX-MASS` for a selected rate below the winning branch's
reserve surplus, Corollary 4.5D gives the explicit finite-battery clustering
conclusion:

```text
R_beta,box > D_KP,box
+ BOX-MASS
=> MG-EXP-CLOSE(m_phys,box) on G_box.
```

The Paper-15 Creutz specialization is now explicit as well:

```text
P15-CREUTZ-PASS_box
+ BOX-MSKP-IMPORT
+ MARK-GEOM_box
+ MARK-LOSS_box
+ R_Creutz,box > D_KP,box
+ BOX-MASS
=> MG-EXP-CLOSE(m_phys,box) on G_box.
```

The `BOX-MASS` compatibility is now explicit rather than implicit. If

```text
G_box^Creutz = R_Creutz,box - D_KP,box
```

and

```text
G_box^Creutz > s_0 Delta_tot,box,
```

then the canonical choice

```text
m_box = (G_box^Creutz + s_0 Delta_tot,box)/2
```

exports the positive physical rate

```text
m_phys,box = (G_box^Creutz - s_0 Delta_tot,box)/(2s_0).
```

The finite-battery confinement bridge is also now explicit:

```text
BOX-CONF-PASS
=> BOX-2PT-KP
```

and, with Paper 17 `BOX-MASS`,

```text
BOX-CONF-PASS + BOX-MASS
=> MG-EXP-CLOSE(m_phys,box) on G_box.
```

This is still not the full mass gap. It is the first-battery version of the
confinement-to-KP bridge.

The cofinal conditional bridge is now explicit as well:

```text
G_j-CONF-PASS for every j
+ selected-rate reserve
=> G_j-2PT-KP for every j + MG-UNIF(m_*).
```

The cofinal Paper-15 Creutz program is now isolated:

```text
COF-P15-CREUTZ(m_*)
=> CONF-COFINAL-PASS(m_*)
=> MGAP(m_*).
```

Its hard uniform inequality is:

```text
inf_j [G_j^Creutz/ell_j - Delta_conf,j] >= 2m_* > 0.
```

This is the exact step where a tower of finite positive Creutz results
would become a genuine mass-gap theorem rather than a collection of
finite-battery clustering statements.

The actual-continuum endpoint is now named separately:

```text
AYM-CONF-CLOSE(m_*)
=> COF-P15-CREUTZ(m_*)
=> MGAP(m_*).
```

`AYM-CONF-CLOSE` is the desired actual `4D SU(N)` confinement theorem in
this architecture. It requires the actual continuum whole-process law to
verify the cofinal Paper-15 Creutz windows, the quantitative loop-modulus
and denominator bounds, the single-window closing inequalities, the cofinal
marked bridge stability, and the uniform Paper-17 rate surplus.
Strong-coupling area laws, flux-tube
language, gauge-fixed sheets, or partial Markov kernels do not count unless
they export these scalar record-law inequalities on the same tower.

Steps 3--5 of the actual-continuum workbench are now explicit reductions:

```text
AYM-CONF-LMOD
=> CR-ERR_j(delta_j) + CR-LMOD_j(delta_j,kappa_CR,j)
   + S_15,j - 2 delta_j ell_j^2 > 0,

AYM-CONF-SWIN
=> choose sigma_j so that
   S_15,j >= (sigma_j+2 delta_j)ell_j^2
   and R_j^Creutz > D_KP,j,

AYM-CONF-MARK
=> MARK-GEOM_j + MARK-LOSS_j + MS-KP_j
   with finite D_KP,j on the same tower.
```

Together with `AYM-CONF-RES`, these steps close every cofinal finite-battery
Creutz pass except the uniform normalized rate reserve. That remaining
reserve is not cosmetic: it is the step that prevents a tower of positive
finite batteries from degenerating into zero physical mass scale.

The latest sharp reduction makes all six actual-continuum workbench tasks
explicit:

```text
AYM-CONF-WIN-MAP
=> AYM-CONF-WIN,

AYM-CONF-LMOD-EST
=> AYM-CONF-LMOD,

AYM-CONF-MARK-UNIF
=> AYM-CONF-MARK,

AYM-CONF-SWIN-CALC
=> AYM-CONF-SWIN
   and G_j^Creutz = Gamma_j/2 for canonical sigma_j,

AYM-CONF-RATE-CALC(m_*)
=> AYM-CONF-RATE,

AYM-CONF-LAW + AYM-CONF-WP + the preceding gates
=> AYM-CONF-CLOSE(m_*).
```

The single number now carrying the remaining cofinal confinement burden is

```text
Gamma_j
= alpha_j(S_15,j-2 delta_j ell_j^2)-L_Creutz,j-D_KP,j.
```

The sharp rate condition is:

```text
inf_j [Gamma_j/(2 ell_j)-Delta_conf,j] >= 2m_* > 0.
```

This is a stricter and more computable target than merely saying "prove
confinement": it asks for a positive same-ledger Creutz reserve per physical
block length after all loop-modulus, marked-bridge, KP, and Paper-17 debits.

The route has now also been pushed to termwise lower bounds:

```text
AYM-CONF-RES-NC
+ AYM-CONF-LMOD-SRC
+ AYM-CONF-MARK-SRC
+ AYM-CONF-GAMMA-LB(m_*)
=> AYM-CONF-CLOSE(m_*).
```

Here

```text
underline Gamma_j
= underline alpha_j(underline S_15,j - 2 overline delta_j ell_j^2)
  - overline L_j - overline D_j
```

and the remaining termwise rate target is:

```text
inf_j [underline Gamma_j/(2 ell_j)-overline Delta_j] >= 2m_* > 0.
```

The obstruction theorem says that failure of the Paper-18 route, assuming the
actual Wilson-loop law and whole-process ledger exist, must be localized in
one of six places: window maps, reserve noncollapse, source loop-modulus
control, source marked-bridge control, termwise Gamma lower bound, or
same-ledger compatibility.

The seven-step source closure now makes those places constructive:

```text
AYM-CONF-TOWER-FRZ
+ AYM-CONF-LAWWIN-AUDIT
+ AYM-CONF-RES-ATTACK
+ AYM-CONF-LMOD-CONST-ATTACK
+ AYM-CONF-MARK-CONST-ATTACK
P16-LAW-IMPORT => AYM-CONF-LAW-SRC
+ AYM-CONF-WIN-SCHED => AYM-CONF-WIN-SRC
+ AYM-CONF-RES-RC-TAIL => AYM-CONF-RES-ACT-TAIL
+ AYM-CONF-RES-ACT-TAIL => AYM-CONF-RES-TAIL
+ AYM-CONF-RES-SYM or AYM-CONF-RES-TAIL => AYM-CONF-RES-CALC => AYM-CONF-RES-SRC
+ AYM-CONF-LMOD-RC-TAIL => AYM-CONF-LMOD-ACT-TAIL
+ AYM-CONF-LMOD-ACT-SYM => AYM-CONF-LMOD-SYM
  or AYM-CONF-LMOD-ACT-TAIL => AYM-CONF-LMOD-TAIL
+ AYM-CONF-LMOD-SYM or AYM-CONF-LMOD-TAIL => AYM-CONF-LMOD-CALC => AYM-CONF-LMOD-SRC
+ AYM-CONF-MARK-RC-TAIL => AYM-CONF-MARK-ACT-TAIL
+ AYM-CONF-MARK-ACT-SYM => AYM-CONF-MARK-SYM
  or AYM-CONF-MARK-ACT-TAIL => AYM-CONF-MARK-TAIL
+ AYM-CONF-MARK-SYM or AYM-CONF-MARK-TAIL => AYM-CONF-MARK-CALC => AYM-CONF-MARK-SRC
+ AYM-CONF-GAMMA-CONST-ATTACK(m_*)
+ AYM-CONF-GAMMA-SRC-POP
+ AYM-CONF-GAMMA-ROUTE
+ AYM-CONF-GAMMA-WORK_j
+ AYM-CONF-GAMMA-RLD_j
+ AYM-CONF-GAMMA-AREA_j
+ AYM-CONF-GAMMA-MKPD_j
+ AYM-CONF-GAMMA-P17D_j
+ AYM-CONF-GAMMA-MD-WORK_j
+ AYM-CONF-SRLD-SRC_j => S_j^RLD>0
+ AYM-CONF-PI-SRC_j(m_*) => Pi_j>0
+ AYM-CONF-ACT-WORK_j
+ AYM-CONF-ACT-RLD-WORK_j => Sigma_j^RLD>0 => AYM-CONF-ACT-RLD_j
+ AYM-CONF-ACT-RLD-ASYM
+ AYM-CONF-ACT-RLD-SRC-ATTACK or AYM-CONF-ACT-RLD-SRC-FALS
+ AYM-CONF-ACT-RLD-THRESH(s_R)
+ AYM-CONF-ACT-CRES-P16(c_R) => AYM-CONF-ACT-CRES-LOW(c_R)
+ AYM-CONF-ACT-CRES-LOW(c_R)
+ AYM-CONF-ACT-KAPPA-SEP(k_R) or AYM-CONF-ACT-KAPPA-QUOT(W_R)
+ AYM-CONF-ACT-KQ-LMOD(W_R) => AYM-CONF-ACT-KAPPA-QUOT(W_R)
+ AYM-CONF-ACT-KQ-RATE(W_R) => AYM-CONF-ACT-KQ-LMOD(W_R)
+ [AYM-CONF-ACT-CRES-P16(c_R)
+  AYM-CONF-ACT-KQ-RATE(W_R)
+  c_R >= C_quot^crit(s_R,W_R)]
+ => AYM-CONF-ACT-RLD-TAIL
+ AYM-CONF-ACT-RNUM-TAIL + AYM-CONF-ACT-BDEB-TAIL
+ first tail RLD inequality R_R-B_R>=s_R>0
+ AYM-CONF-ACT-RLD-TAIL or reindexed RLD pass
+ AYM-CONF-ACT-PI-WORK_j(m_*) => Sigma_j^PI(m_*)>0 => AYM-CONF-ACT-PI_j(m_*)
+ AYM-CONF-ACT-PI-ASYM
+ AYM-CONF-ACT-PNUM-TAIL + AYM-CONF-ACT-PDEB-TAIL(m_*)
+ first tail PI inequality A_P-K_P-T_P(m_*)>=s_P>0
+ AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*) => AYM-CONF-ACT-PNUM-TAIL + AYM-CONF-ACT-PDEB-TAIL(m_*)
+ AYM-CONF-ACT-PI-THRESH(s_P,m_*)
+ [AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)
+  AYM-CONF-ACT-PI-THRESH(s_P,m_*)]
+ => AYM-CONF-ACT-PI-TAIL(m_*)
+ AYM-CONF-ACT-PI-TAIL(m_*) or reindexed PI pass
+ AYM-CONF-ACT-LEDGER-SRC => AYM-CONF-ACT-LEDGER-TAIL
+ AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*) => AYM-CONF-ACT-COF-WORK(m_*) => AYM-CONF-ACT-COF(m_*)
+ [AYM-CONF-ACT-RLD-TAIL
+  AYM-CONF-ACT-PI-TAIL(m_*)
+  AYM-CONF-ACT-LEDGER-TAIL
+  AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)]
+ => AYM-CONF-GAMMA-FW-DIRECT(m_*)
+ AYM-CONF-ACT-COF-WORK(m_*) => AYM-CONF-ACT-COF(m_*)
+ AYM-CONF-ACT-RLD_j
+ AYM-CONF-ACT-PI_j(m_*)
+ AYM-CONF-ACT-LEDGER_j
+ AYM-CONF-ACT-COF(m_*)
+ cofinal AYM-CONF-GAMMA-MD-WORK_j with S_j^RLD>0 and Pi_j>0
+ AYM-CONF-GAMMA-FW-DIRECT(m_*) => AYM-CONF-GAMMA-ACT-SYM(m_*)
+ AYM-CONF-GAMMA-RC-TAIL(m_*) => AYM-CONF-GAMMA-ACT-TAIL(m_*)
+ AYM-CONF-GAMMA-ACT-SYM(m_*) => AYM-CONF-GAMMA-SYM(m_*)
  or AYM-CONF-GAMMA-ACT-TAIL(m_*) => AYM-CONF-GAMMA-TAIL(m_*)
+ AYM-CONF-GAMMA-SYM(m_*) or AYM-CONF-GAMMA-TAIL(m_*) => AYM-CONF-GAMMA-CALC(m_*)
+ AYM-CONF-LEDGER-AUDIT
=> AYM-CONF-CLOSE(m_*).
```

This is the most explicit Paper-18 endpoint. Each item is a scalar
whole-process record certificate. None is a flux-tube ontology, gauge-fixed
field ontology, or partial Markov-kernel assumption. The remaining
mathematical problem is to prove those seven certificates on the actual
continuum `4D SU(N)` tower.

The six source-constant campaign steps are no longer informal:

```text
AYM-CONF-TOWER-FRZ
=> all constants live on one frozen whole-process tower,

AYM-CONF-LAWWIN-AUDIT
=> AYM-CONF-LAW-SRC + AYM-CONF-WIN-SRC,

AYM-CONF-RES-ATTACK
=> finite-window reserve success
   or absolute-tail reserve success
   or normalized-tail reserve survival
   or a real reserve-source obstruction,

AYM-CONF-LMOD-CONST-ATTACK
=> finite-window loop-modulus success
   or uniform-tail loop-modulus success
   or normalized Gamma survival
   or a real loop-modulus obstruction,

AYM-CONF-MARK-CONST-ATTACK
=> finite-window marked-bridge success
   or uniform-tail marked-bridge success
   or normalized Gamma survival
   or a real marked-bridge obstruction,

AYM-CONF-GAMMA-CONST-ATTACK(m_*)
=> finite-window Gamma success
   or compact-tail Gamma success
   or smaller-rate survival
   or a real Gamma-rate obstruction,

AYM-CONF-GAMMA-SRC-POP
+ AYM-CONF-GAMMA-ROUTE
+ AYM-CONF-GAMMA-WORK_j
+ AYM-CONF-GAMMA-RLD_j
+ AYM-CONF-GAMMA-AREA_j
+ AYM-CONF-GAMMA-MKPD_j
+ AYM-CONF-GAMMA-P17D_j
+ AYM-CONF-GAMMA-MD-WORK_j
+ AYM-CONF-SRLD-SRC_j => S_j^RLD>0
+ AYM-CONF-PI-SRC_j(m_*) => Pi_j>0
+ AYM-CONF-ACT-WORK_j
+ AYM-CONF-ACT-RLD-WORK_j => Sigma_j^RLD>0 => AYM-CONF-ACT-RLD_j
+ AYM-CONF-ACT-RLD-ASYM
+ AYM-CONF-ACT-RLD-SRC-ATTACK or AYM-CONF-ACT-RLD-SRC-FALS
+ AYM-CONF-ACT-RLD-THRESH(s_R)
+ AYM-CONF-ACT-CRES-P16(c_R) => AYM-CONF-ACT-CRES-LOW(c_R)
+ AYM-CONF-ACT-CRES-LOW(c_R)
+ AYM-CONF-ACT-KAPPA-SEP(k_R) or AYM-CONF-ACT-KAPPA-QUOT(W_R)
+ AYM-CONF-ACT-KQ-LMOD(W_R) => AYM-CONF-ACT-KAPPA-QUOT(W_R)
+ AYM-CONF-ACT-KQ-RATE(W_R) => AYM-CONF-ACT-KQ-LMOD(W_R)
+ [AYM-CONF-ACT-CRES-P16(c_R)
+  AYM-CONF-ACT-KQ-RATE(W_R)
+  c_R >= C_quot^crit(s_R,W_R)]
+ => AYM-CONF-ACT-RLD-TAIL
+ AYM-CONF-ACT-RNUM-TAIL + AYM-CONF-ACT-BDEB-TAIL
+ first tail RLD inequality R_R-B_R>=s_R>0
+ AYM-CONF-ACT-RLD-TAIL or reindexed RLD pass
+ AYM-CONF-ACT-PI-WORK_j(m_*) => Sigma_j^PI(m_*)>0 => AYM-CONF-ACT-PI_j(m_*)
+ AYM-CONF-ACT-PI-ASYM
+ AYM-CONF-ACT-PNUM-TAIL + AYM-CONF-ACT-PDEB-TAIL(m_*)
+ first tail PI inequality A_P-K_P-T_P(m_*)>=s_P>0
+ AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*) => AYM-CONF-ACT-PNUM-TAIL + AYM-CONF-ACT-PDEB-TAIL(m_*)
+ AYM-CONF-ACT-PI-THRESH(s_P,m_*)
+ [AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)
+  AYM-CONF-ACT-PI-THRESH(s_P,m_*)]
+ => AYM-CONF-ACT-PI-TAIL(m_*)
+ AYM-CONF-ACT-PI-TAIL(m_*) or reindexed PI pass
+ AYM-CONF-ACT-LEDGER-SRC => AYM-CONF-ACT-LEDGER-TAIL
+ AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*) => AYM-CONF-ACT-COF-WORK(m_*) => AYM-CONF-ACT-COF(m_*)
+ [AYM-CONF-ACT-RLD-TAIL
+  AYM-CONF-ACT-PI-TAIL(m_*)
+  AYM-CONF-ACT-LEDGER-TAIL
+  AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)]
+ => AYM-CONF-GAMMA-FW-DIRECT(m_*)
+ AYM-CONF-ACT-COF-WORK(m_*) => AYM-CONF-ACT-COF(m_*)
+ AYM-CONF-ACT-RLD_j
+ AYM-CONF-ACT-PI_j(m_*)
+ AYM-CONF-ACT-LEDGER_j
+ AYM-CONF-ACT-COF(m_*)
+ cofinal S_j^RLD>0 and Pi_j>0
+ AYM-CONF-GAMMA-FW-DIRECT(m_*)
=> populated finite-window Gamma direct source
   or a named failure of the populated scalar inequality.
```

The first source certificate is now imported from Paper 16:

```text
HK-CYC-CLOSE
+ Paper-18 loop-family admissibility
+ Paper-16 whole-process restrictions
=> P16-LAW-IMPORT
=> AYM-CONF-LAW-SRC
=> AYM-CONF-LAW.
```

This imports the actual continuum Wilson-loop law: reflection positivity,
Euclidean covariance, gauge invariance, loop continuity, nontriviality, and
same-ledger compatibility. It does not import confinement.

The second source certificate is now constructed combinatorially:

```text
Paper-17 cofinal G_j
+ P16-LAW-IMPORT
+ Paper-15 finite-battery envelope rule
=> AYM-CONF-WIN-SCHED
=> AYM-CONF-WIN-SRC
=> AYM-CONF-WIN-MAP.
```

For each `G_j`, the scheduler forms a finite raw loop set, takes finite
rectangular/block-face hulls and endpoint closures, closes those hulls under
the four-slot Creutz operation, defines the finite window `D_CR,j`, embeds it
into a finite Paper-15 battery `B_15,j`, and maps each probe to the finite
set of Creutz cells supporting its scalar record. This is a projective
finite-record construction, not a gauge-field construction.

The third source certificate has now been reduced to the explicit reserve
calculation:

```text
AYM-CONF-WIN-SCHED
+ AYM-CONF-RES-SYM or AYM-CONF-RES-TAIL
+ Paper-16 HK-CREUTZ-CLOSE_j loss ledger
+ scalar normalization lower bound underline gamma_j
+ residual alignment-loss bound overline epsilon_15,j
+ underline gamma_j underline M_j - overline epsilon_15,j > 0
=> AYM-CONF-RES-CALC
=> AYM-CONF-RES-SRC
=> AYM-CONF-RES-NC.
```

Here

```text
underline M_j
= underline M_SUB,j
  - overline L_bat,j
  - overline L_reg,j
  - overline L_vol,j
  - overline L_shape,j.
```

So the first real confinement-reserve problem has been isolated to one
positive scalar inequality on every cofinal window:

```text
underline S_15,j
= underline gamma_j underline M_j - overline epsilon_15,j
> 0.
```

The symbolic/numeric verifier expands `underline M_j` further into Paper-15
and Paper-16 quantities:

```text
underline M_SUB,j
= underline u_j^N0,j (1-overline u_j^Qsigma,j)
  - overline Delta_dec,j
  - overline T_pre,j,

underline M_j
= underline M_SUB,j
  - overline L_bat,j
  - overline L_reg,j
  - overline L_vol,j
  - overline L_shape,j.
```

Thus the reserve gate can now be checked either window by window with
interval arithmetic, or by a finite-prefix plus uniform-tail test
`AYM-CONF-RES-TAIL`.

The actual-tail reserve source has also been isolated:

```text
Paper-16 HK-CREUTZ-CLOSE_j on the tail
+ gamma_15,j >= gamma_R > 0
+ epsilon_15_to_j <= epsilon_R
+ M_SUB,j^bd - L_bat,j - L_reg,j - L_vol,j - L_shape,j >= M_R > 0
+ gamma_R M_R - epsilon_R >= s_R > 0
=> AYM-CONF-RES-ACT-TAIL
=> AYM-CONF-RES-TAIL.
```

This proves the actual positive cofinal reserve once the four displayed
tail constants are supplied by the actual continuum trajectory. It is not an
unconditional proof of those constants.

The real-constant attempt has now been sharpened:

```text
uniform local geometry or bounded raw N_0,j
+ u_R^-, u_R^+, N_R, Q_R, eta_R, c_Delta,R, T_R
+ uniform Paper-16 extraction-loss bounds
+ gamma_R>0 and epsilon_R finite
+ gamma_R M_R - epsilon_R = s_R > 0
=> AYM-CONF-RES-RC-TAIL
=> AYM-CONF-RES-ACT-TAIL.
```

But the raw growing-sheet branch has been falsified as an absolute-tail
route:

```text
N_0,j -> infinity with u_{-,j} <= u_max < 1
=> M_15,j^bd can have no positive absolute cofinal lower bound
=> raw absolute AYM-CONF-RES-ACT-TAIL fails.
```

So the reserve route is now honest in a sharper way. Either the cofinal
reserve is genuinely local/renormalized, or the proof must abandon absolute
`M_R>0` and feed a normalized rate reserve directly into the Gamma tail
inequality.

The fourth source certificate has now been reduced to an explicit
loop-modulus calculation:

```text
AYM-CONF-WIN-SCHED
+ AYM-CONF-RES-NC
+ positive slot denominator underline kappa_j
+ finite-stage slot transport epsilon_slot,j(alpha)
+ loop-modulus bound overline omega_j
+ readout bound overline E_j
+ max{overline E_j/ell_j^2,
       4 overline omega_j/(underline kappa_j ell_j^2)}
   < underline S_15,j/(2 ell_j^2)
=> AYM-CONF-LMOD-SYM
=> AYM-CONF-LMOD-CALC
=> AYM-CONF-LMOD-SRC
=> AYM-CONF-LMOD.
```

The tail version `AYM-CONF-LMOD-TAIL` replaces infinitely many arithmetic
checks by a finite prefix plus uniform normalized tail bounds. This proves
the loop-modulus calculation as a scalar-record theorem. It does not by
itself prove that the actual continuum `4D SU(N)` trajectory satisfies the
needed denominator and error inequalities.

The actual loop-modulus source has now also been isolated:

```text
Paper-16 loop continuity and same-ledger Wilson-loop law
+ finite-window Creutz-slot positivity
+ finite-stage slot transport
+ loop-continuity error decomposition
+ readout-error decomposition
+ max{overline E_j/ell_j^2,
       4 overline omega_j/(underline kappa_j ell_j^2)}
   < underline S_15,j/(2 ell_j^2)
=> AYM-CONF-LMOD-ACT-SYM
=> AYM-CONF-LMOD-SYM.
```

This proves the finite-window actual source route. The stronger tail route

```text
AYM-CONF-LMOD-ACT-TAIL
=> AYM-CONF-LMOD-TAIL
```

requires a uniform normalized tail with `underline kappa_j>=kappa_L>0`,
normalized readout and loop-modulus errors bounded by `e_L` and `w_L`, and
`max{e_L,w_L}<s_L/2`. That is a real asymptotic confinement estimate, not a
formal consequence of loop continuity alone.

The real-constant attempt has now been decided:

```text
uniform positive raw or normalized slot denominator kappa_L>0
+ normalized reserve S_15,j/ell_j^2 >= s_L
+ finite-stage slot transport <= rho_L
+ normalized readout and loop-modulus errors <= e_L,w_L
+ max{e_L,w_L}<s_L/2
=> AYM-CONF-LMOD-RC-TAIL
=> AYM-CONF-LMOD-ACT-TAIL.
```

But raw growing Wilson-loop slots falsify the absolute tail route:

```text
some raw slot Wilson loop W(L_j) -> 0
=> no positive cofinal kappa_L
=> raw absolute AYM-CONF-LMOD-ACT-TAIL fails.
```

In particular, a raw area-decaying envelope
`W(L_j)<=C exp[-sigma A_j+K P_j+K_0]` with
`sigma A_j-KP_j-K_0-log C -> infinity` forces denominator collapse. Thus the
honest default for raw cofinal Wilson-loop slots is finite-window
`AYM-CONF-LMOD-ACT-SYM`; the tail route is available only after proving a
local slot schedule or a denominator-renormalized/normalized readout with
uniform positive denominators.

The fifth source certificate has now been reduced to an explicit
marked-bridge calculation:

```text
AYM-CONF-WIN-SCHED
+ finite endpoint closure rule Cl_j(S;O,P)
+ alpha_j >= alpha_* > 0
+ N_cl,j <= N_* < infinity
+ local marked-loss ledger epsilon_area,j <= overline epsilon_j
+ endpoint-enlarged marked KP bounds
   h_j^S <= overline h_j,
   lambda_mark,j^S <= overline lambda_j,
   D_KP,j <= overline D_j
+ eta_ch,j <= eta_* < 1
+ endpoint records typed only as boundary instruments
=> AYM-CONF-MARK-SYM
=> AYM-CONF-MARK-CALC
=> AYM-CONF-MARK-SRC
=> AYM-CONF-MARK.
```

The tail version `AYM-CONF-MARK-TAIL` replaces infinitely many marked
geometry/loss/KP checks by a finite prefix plus a common tail protocol. This
proves the marked-bridge calculation as a scalar-record theorem. It does not
prove the actual `4D SU(N)` endpoint-enlarged marked KP estimates; those
remain an actual-trajectory input.

The actual marked-bridge source has now been isolated:

```text
same-ledger endpoint-enlarged finite batteries B_j^S
+ Paper-14 FBE_j^S on B_j^S
+ positive Paper-15 nCPSC_j^S on B_j^S
+ finite endpoint-marking ledger
+ eta_ch,j <= eta_* < 1
=> endpoint-enlarged marked KP stability
=> AYM-CONF-MARK-ACT-SYM
=> AYM-CONF-MARK-SYM.
```

The stronger tail source

```text
AYM-CONF-MARK-RC-TAIL
=> AYM-CONF-MARK-ACT-TAIL
=> AYM-CONF-MARK-TAIL
```

is now reduced to the real-constant endpoint-marked tail ledger:

```text
same-ledger endpoint-enlarged batteries B_j^S
+ one cofinal endpoint closure/loss convention
+ Paper-14 FBE_j^S on B_j^S
+ positive Paper-15 nCPSC_j^S on B_j^S
+ finite endpoint marking
+ eta_ch,j <= eta_M < 1 on the cofinal tail
=> AYM-CONF-MARK-RC-TAIL.
```

Pointwise `eta_ch,j<1` is not enough: if `sup_j eta_ch,j=1`, the
endpoint-enlarged marked KP estimates stay finite one by one, but the
cofinal tail theorem is not proved.

The older shorthand

```text
AYM-CONF-MARK-ACT-TAIL
=> AYM-CONF-MARK-TAIL
```

should therefore be read through `AYM-CONF-MARK-RC-TAIL`: it requires one
cofinal endpoint-closure/loss convention, uniform tail bounds
`alpha_j>=alpha_M>0`, `N_cl,j<=N_M<infinity`, `eta_ch,j<=eta_M<1`, and finite
endpoint-enlarged KP thresholds. This is not a mass-gap estimate; it is the
stability needed before the Gamma-rate ledger can ask for positive physical
decay.

The sixth source certificate has now been assembled into the final
Gamma-rate calculation:

```text
overline L_j
= overline epsilon_j + overline h_j + overline lambda_j,

overline delta_j
>= max{overline E_j/ell_j^2,
       4 overline omega_j/(underline kappa_j ell_j^2)},

underline Gamma_j
= underline alpha_j(underline S_15,j-2 overline delta_j ell_j^2)
  - overline L_j
  - overline D_j,

r_j
= underline Gamma_j/(2 ell_j)-overline Delta_j.
```

The direct verifier `AYM-CONF-GAMMA-SYM(m_*)` proves `r_j>=2m_*>0` for
every cofinal `j`. The tail verifier `AYM-CONF-GAMMA-TAIL(m_*)` proves the
same infimum from a finite prefix and the asymptotic bound

```text
alpha_G q_G/2 - b_G - Delta_G >= 2m_* > 0.
```

This is the exact point where the finite positive Creutz reserves become a
nonzero physical rate. If this inequality fails, the tower may still contain
positive finite batteries, but it does not yet prove confinement or the
Paper-17 uniform mass-gap input.

The actual Gamma-rate source has now been isolated:

```text
same-ledger reserve, loop-modulus, marked-bridge, and Paper-17 debit bounds
+ Q_j = underline S_15,j - 2 overline delta_j ell_j^2 > 0
+ r_j = underline Gamma_j/(2 ell_j)-overline Delta_j >= 2m_* > 0
=> AYM-CONF-GAMMA-ACT-SYM(m_*)
=> AYM-CONF-GAMMA-SYM(m_*).
```

The stronger tail source

```text
AYM-CONF-GAMMA-RC-TAIL(m_*)
=> AYM-CONF-GAMMA-ACT-TAIL(m_*)
=> AYM-CONF-GAMMA-TAIL(m_*)
```

is now a computable tail test. On a proposed cofinal tail one computes

```text
q_j = (underline S_15,j - 2 overline delta_j ell_j^2)/ell_j,
b_j = (overline L_j + overline D_j)/(2 ell_j),
d_j = overline Delta_j,
```

then certifies

```text
alpha_G = tail inf underline alpha_j,
q_G = tail inf q_j,
b_G = tail sup b_j,
Delta_G = tail sup d_j,
```

with outward-rounded or symbolic slack. The final test is

```text
alpha_G q_G/2 - b_G - Delta_G >= 2m_* > 0.
```

If this passes, the compact Gamma tail closes. If `q_G` collapses to zero,
or if `b_G` or `Delta_G` diverges, or if the final margin is nonpositive on
every cofinal tail, then the compact tail route does not prove the physical
rate and the paper must use finite-window verification or sharper source
estimates.

The older shorthand

```text
AYM-CONF-GAMMA-ACT-TAIL(m_*)
=> AYM-CONF-GAMMA-TAIL(m_*)
```

should therefore be read through `AYM-CONF-GAMMA-RC-TAIL(m_*)`: it reduces
the infinite cofinal rate problem to a finite prefix plus the single tail
inequality

```text
alpha_G q_G/2 - b_G - Delta_G >= 2m_* > 0.
```

Thus the last remaining numerical burden is clear: the normalized
loop-debited reserve per physical block length must beat the normalized
marked/KP and Paper-17 rate debits by a positive amount.

The whole-process source certificate has now been discharged as an audit
theorem:

```text
HK-WP-CLOSE
+ MG-WP
+ CONF-WP
+ CONF-DEBIT-REG
+ common-refinement source compatibility
=> CONF-IMPORT-WP
=> AYM-CONF-LEDGER-AUDIT
=> AYM-CONF-WP.
```

The new content is `CONF-DEBIT-REG`: every loss label belongs to exactly one
bucket, reserve `S`, loop-modulus `delta`, marked local loss `L`, KP/decorated
smallness `D`, Paper-17 rate `Delta`, or audit-only zero loss. This prevents
the same counterterm, projection, endpoint, or character-tail error from
being paid twice in `underline Gamma_j`.

Thus the conditional architecture of Paper 18 is complete. What remains open
is not the formal route from confinement estimates to the Paper-17 mass-gap
gates, but the actual proof of the `4D SU(N)` estimates entering
`AYM-CONF-CLOSE(m_*)`, equivalently `CONF-COFINAL-PASS(m_*)` on the actual
trajectory.

It also states a candidate ISP record-law definition interface for a
four-dimensional pure quantum gauge theory:

```text
CYM_WL + MG-OS-CLOSE + cofinal MG-OBS + MG-WP.
```

The remaining hard mathematical problem is to prove the actual
four-dimensional `SU(N)` estimates entering `AYM-CONF-CLOSE(m_*)`:
finite-window Creutz dominance `CR-MTD`, quantitative loop-continuity
`CR-LMOD-QUANT`, marked area-to-hull transfer, marked KP stability,
single-window Creutz closing, and a positive cofinal selected-rate reserve.

Bottom line: Paper 18 currently counts as a complete Barandes-aligned
conditional confinement architecture and obstruction ledger. It does not yet
count as a proof of actual `4D SU(N)` confinement, a proof of the Clay
mass-gap theorem, or an unconditional construction of continuum Yang-Mills.
The next mathematical task is no longer to invent the route; it is to prove
or falsify the actual source constants in the obstruction ledger above.
