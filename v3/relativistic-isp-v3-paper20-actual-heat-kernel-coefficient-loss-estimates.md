# Relativistic ISP V3 Paper 20: Actual Heat-Kernel Coefficient And Loss Estimates For 4D `SU(N)` Direct-Witness Confinement

Author: Felix Robles Elvira

## Abstract

Paper 19 reduced the AF-matched direct-witness confinement branch to two
strict scalar estimates on one frozen whole-process tower:

```text
R_H^opt < R_H^crit,
L_AFM^sharp < Sig_AFM.
```

Paper 20 is the actual-estimate paper. It freezes the selector, tower,
representation channel, block windows, character cutoff, counterterm
convention, and pushed-forward scalar record law before any estimate is made.
It then attacks the two remaining source estimates directly. If both pass,
Paper 20 imports the Paper-19/Paper-18 conditional theorem and closes the
declared direct-witness branch on that selector. If either fails, Paper 20
records the exact scalar obstruction. Paper 20 does not treat the frozen
selector itself as an area-law or continuum-Yang-Mills existence theorem.

## 0. Honest Boundary

The primitive object remains a whole-process law of records. Heat-kernel
links, gauge charts, counterterm coordinates, block plaquettes, surfaces,
polymers, and RG flows are proof coordinates only. Every estimate in this
paper must end as an inequality for scalar records on the same pushed-forward
law.

Paper 20 permits:

1. the Paper-16 heat-kernel AF trajectory and its pushed-forward record laws;
2. the Paper-19 frozen selector and direct-witness ledgers;
3. finite character batteries and cofinal Weyl-Casimir cutoffs already used
   by `P19-T13-DEC`;
4. coefficient, decoration, transport, and surface-entry constants when they
   are evaluated on the same record tower;
5. exact pass/fail statements for scalar limsup and liminf quantities.

Paper 20 does not permit:

1. changing `rho`, the block scale, the character cutoff, or the window
   schedule after a favorable estimate is found;
2. adding a second hidden representation cutoff to control the
   non-leading tail;
3. charging the same projective, regulator, loop-readout, volume, or
   decoration loss in more than one bucket;
4. treating gauge-fixed fields, sheets, or local polymers as ontology.

### Post-Paper-11/12 Source Audit Rule

The Paper-10 and Paper-11 audits are now part of the Paper-20 boundary.
Paper 20 may use Paper 11 for conditional RG residual ledgers, AF locality
margin forms, perturbative trajectory bookkeeping, and a smeared Wilson-loop
nontriviality benchmark. Paper 20 may use Paper 12 for calibrated
perimeter/cusp renormalized Wilson-loop records and smearing-removal ledgers.

Paper 20 may not use Papers 11 or 12 to import:

```text
T_-^{SEL2}>0 above the tree-rate threshold;
the SEL2 block-plaquette heat-kernel coefficient comparison;
P20-SEL2-TREE-RATE-GATE;
Wilson-loop area law;
mass gap;
confinement.
```

Those are same-record source estimates for this paper. If they are not proved
inside the active Paper-20 coefficient ledger, they must be parked as
obstructions rather than imported from the earlier RG or loop-renormalization
papers.

### Paper 20 Does / Does Not Prove

Paper 20 aims to prove the conditional implication

```text
P20-FROZEN-SEL
+ P20-NOSMUGGLE
+ P20-COEFF-PASS
+ P20-LOSS-PASS
=> Paper-19 direct-witness closure
=> Paper-18 confinement closure.
```

Paper 20 does not begin by assuming actual `4D SU(N)` confinement, a mass
gap, or an area law. Those are downstream consequences only if the two
source estimates pass on the same frozen selector.

### Anti-Circularity Rule

The frozen selector and tower data in this paper are bookkeeping and target
selection data only. They may declare:

```text
finite restrictions,
readout maps,
AF trajectory,
block/window schedule,
character channel,
counterterm convention,
debit register.
```

They may not declare, hide, or import:

```text
R_H^opt < R_H^crit,
L_AFM^sharp < Sig_AFM,
positive string tension,
Wilson-loop area law,
mass gap,
or existence of continuum 4D SU(N) Yang-Mills with those properties.
```

If either headline inequality is used before it is proved from the declared
source constants, the Paper-20 closure is circular and invalid. If the
available estimates only prove a strong-coupling finite-regulator area law,
or a fixed-battery Wilson-loop bound with no cofinal continuum control, then
Paper 20 must record a route failure rather than a confinement proof.

## 0A. Imports From Paper 19

Paper 19 exports the following exact theorem:

```text
R_H^opt < R_H^crit
+ L_AFM^sharp < Sig_AFM
=> c_15^tail > 0
=> AYM-CONF-CLOSE(m_*)
=> MGAP(m_*).
```

Here

```math
R_H^{opt}
:=
\limsup_j g_{i(j)}^{-2}\delta_j e^{a_j},
```

where `delta_j` is the same-record leading coefficient defect and
`a_j` is the selected heat-kernel reference exponent. The coefficient
threshold is

```math
R_H^{crit}(\epsilon_A,\chi,\rho)
=
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho)\over2}
```

on the tight AF-area selector.

The loss envelope is

```math
L_{AFM}^{sharp}
:=
\limsup_j
\left(\Delta_{dec,j}^{bd}+T_{loss,j}^{bd}\right),
```

and the signal floor is

```math
Sig_{AFM}
=
\exp(-n_+A_{AFM}^*)
\left(1-\exp(-q_-B_{AFM}^*)\right),
```

with

```math
A_{AFM}^*
=
{(1+\chi)s_+C_2(\rho)\over2}
 + {s_+R_H\over1-r_*},
\qquad
B_{AFM}^*
=
{(1-\chi)s_-C_2(\rho)\over2}
 - s_+R_H.
```

The signal floor is meaningful only when `B_AFM^*>0`, equivalently when the
coefficient-error reserve is strict.

### Theorem 0A.1: Paper-19 Import Theorem

Assume a frozen selector satisfying `P20-FROZEN-SEL` and
`P20-NOSMUGGLE`, and assume

```text
P20-COEFF-PASS,
P20-LOSS-PASS.
```

Then the Paper-19 AF-matched direct-witness branch closes. Consequently the
Paper-18 confinement closure and the Paper-17 mass-gap consequence close on
the same whole-process tower.

Proof.

`P20-COEFF-PASS` is exactly `R_H^opt<R_H^crit` on the frozen selector.
`P20-LOSS-PASS` is exactly `L_AFM^sharp<Sig_AFM` on that same selector.
Paper 19 Theorem 8K.3 and the final status theorem import these two strict
inequalities to prove the direct-witness Creutz reserve. Paper 18 then
imports that reserve into `AYM-CONF-CLOSE(m_*)`, and Paper 17 imports the
confinement closure into the mass-gap consequence. `square`

## 1. Common Tower And Selector Freeze

### Definition 1.1: Frozen Paper-20 Selector `P20-FROZEN-SEL`

`P20-FROZEN-SEL` consists of the following data, fixed before Sections 2--6
are evaluated:

1. one Paper-16 heat-kernel AF trajectory with cutoff index `i`;
2. one cofinal subsequence `j -> i(j)`;
3. one AF-area schedule with

   ```math
   s(1-\epsilon_A)
   \le
   {S_j\over H_j}
   \le
   s(1+\epsilon_A),
   \qquad
   H_j:=g_{i(j)}^{-2};
   ```

4. one scheme-slack tail with

   ```math
   1-\chi
   \le
   {t_{i(j)}\over g_{i(j)}^2}
   \le
   1+\chi;
   ```

5. one representation channel `rho` in the Paper-19 admissible selector
   class;
6. one thick/co-scaling Creutz window family, including the block scale,
   square or rectangular template, and decrement schedule;
7. one character cutoff schedule, the same one used by the
   `P19-CHTAIL-AUDIT` and `P19-T13-DEC` ledgers;
8. one counterterm convention, one block/collar geometry, and one scalar
   block-plaquette readout;
9. one pushed-forward whole-process scalar record law carrying all
   coefficient, decoration, loop, transport, and surface-entry records.

No section of Paper 20 may change these data after estimating a constant.

### Definition 1.2: Same-Record Estimate

An estimate is same-record when its input and output are functions of the
single pushed-forward law fixed in `P20-FROZEN-SEL`. In particular:

1. a coefficient estimate must use the same block plaquette marginal
   `K_{p,j}` as `P19-T13-LEAD`;
2. a decoration estimate must use the same character cutoff and residual
   decoration gas as `P19-T13-DEC`;
3. a transport estimate must use the same debit register as the Paper-19
   `T_11`, `T_12`, `T_13`, and `T_14` buckets;
4. a surface-entry estimate must use the same `rho`, block scale, Creutz
   battery, and scalar exact-entry comparison as Paper 19.

### Definition 1.2A: No-Smuggling Audit `P20-NOSMUGGLE`

`P20-NOSMUGGLE` is the anti-circularity audit for the frozen selector. It
holds when all clauses of `P20-FROZEN-SEL` are sourced only from structural
record-law data:

```text
finite restrictions,
readout maps,
AF trajectory and row labels,
block/window schedules,
representation and cutoff choices,
counterterm convention,
debit register,
pushed-forward scalar record law.
```

The audit fails if the selector, its imported tower, or its proof of
admissibility uses any of the following as an input:

```text
R_H^opt < R_H^crit,
L_AFM^sharp < Sig_AFM,
positive string tension,
Wilson-loop area law,
mass gap,
confinement,
or continuum 4D SU(N) Yang-Mills existence with those properties.
```

It also fails if a component estimate is evaluated on a different
representation channel, character cutoff, block/window family, counterterm
scheme, pushed-forward law, or debit register from the one fixed by
`P20-FROZEN-SEL`.

### Theorem 1.2B: `P20-NOSMUGGLE` Makes The Source Estimates Genuine

Assume `P20-FROZEN-SEL` and `P20-NOSMUGGLE`. Then `P20-COEFF-PASS` and
`P20-LOSS-PASS` cannot be imported from the selector itself. They must be
proved or falsified by the coefficient and loss estimates of Sections 2--5.

Proof.

By Definition 1.2A, the frozen selector contains only structural data and
explicitly excludes the two headline inequalities and their area-law or
mass-gap consequences. Therefore the selector can define the quantities
`R_H^opt`, `R_H^crit`, `L_AFM^sharp`, and `Sig_AFM`, but it cannot decide the
strict comparisons between them. Those comparisons are exactly
`P20-COEFF-PASS` and `P20-LOSS-PASS`, so they must be supplied by the later
source estimates or recorded as failures. `square`

### Lemma 1.3: The Frozen Selector Prevents Hidden Optimization

Under `P20-FROZEN-SEL`, proving a strict inequality for one component cannot
be combined with a strict inequality proved after changing another component
of the selector.

Proof.

All constants in Paper 19's final worksheet are functions of the same
pushed-forward scalar record law and the same finite/cofinal batteries. If a
coefficient estimate is proved for one representation channel, while a loss
estimate is proved after changing the channel or cutoff schedule, the two
estimates do not live on the same record law and cannot be inserted into the
Paper-19 theorem. Therefore all estimates must be evaluated after the
selector is frozen. `square`

### Definition 1.4: First Frozen Candidate `P20-SEL0`

`P20-SEL0` is the first selector Paper 20 will test. It imports the `SEL_0`
branch isolated in Paper 19, but freezes it here as an independent Paper-20
worksheet. The data are:

1. **AF row and subsequence.** Use one Paper-16 heat-kernel AF trajectory
   with cutoff index `i`, coupling `g_i`, heat-kernel scheme time `t_i`, and
   cofinal subsequence `j -> i(j)`. Set

   ```math
   H_j:=g_{i(j)}^{-2}.
   ```

2. **Representation channel.** Use `rho_0`, the lowest nontrivial controlled
   `SU(N)` channel in the declared record battery: the fundamental channel,
   or the paired fundamental real-character channel when the battery stores
   real paired characters. Write

   ```math
   C_0:=C_2(\rho_0).
   ```

3. **Selector tolerances.** Fix once and for all

   ```math
   0<\alpha<1,\qquad s>0,\qquad
   0<\epsilon_A<1,\qquad 0<\chi<1.
   ```

4. **Centered square thick windows.** Use the centered square schedule

   ```math
   R_j=T_j=L_j,
   \qquad
   L_j:=\left\lfloor\sqrt{sH_j}\right\rfloor,
   \qquad
   \sigma_j:=\left\lfloor\alpha L_j\right\rfloor,
   ```

   after passing to a tail with `L_j>=1` and `sigma_j>=1`. Let

   ```math
   S_j:=L_j^2.
   ```

5. **AF-area and scheme slack.** Work only on tails on which

   ```math
   s(1-\epsilon_A)
   \le {S_j\over H_j}
   \le s(1+\epsilon_A),
   \qquad
   1-\chi
   \le {t_{i(j)}\over g_{i(j)}^2}
   \le 1+\chi.
   ```

6. **Coefficient target.** Use the same block-plaquette scalar marginal
   `K_{p,j}` and same leading coefficient

   ```math
   k_{\rho_0,j}
   =
   {\langle K_{p,j},\chi_{\rho_0}\rangle
    \over
    \langle\chi_{\rho_0},\chi_{\rho_0}\rangle}
   ```

   as Paper 19 `P19-T13-COEFF-FRZ`. The heat-kernel reference exponent is
   the same branch-selected `a_j` used in Paper 19 Section 8J. On the
   fixed-time branch, `a_j=t_{i(j)}C_0/2`. On an admissible matched-time
   branch, `a_j=\tau_j^{match}C_0/2`. The branch must be declared before
   any coefficient constants are evaluated.

7. **Coefficient threshold.** The first-row threshold is

   ```math
   R_0^{crit}
   =
   {(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
   {C_0\over2}.
   ```

8. **Character-tail schedule.** Use the same cofinal character cutoff as
   `P19-CHTAIL-AUDIT` and `P19-T13-DEC`; on the canonical half-margin branch
   choose

   ```math
   \eta_{ch}^*
   =
   {1-\eta_{19}^{res}\over2}.
   ```

9. **Decoration template.** Use the centered square finite template with
   constants `C_\xi^{SEL0}` and `C_{\xi'}^{SEL0}` from Paper 19
   Lemma 8L.9A.1--Corollary 8L.9C.1.

10. **Analytic residual import.** Use only the clean Paper-16 analytic import
    exported by Paper 19 Theorem 0A.6 and Corollary 0A.7:

    ```text
    P19-AN-AUDIT(m) => P19-AN-IMPORT(m).
    ```

    This import supplies analytic residual decay constants, not confinement
    or area-law constants.

11. **Transport debit register.** Use the Paper-19 disjoint debit register:

    ```text
    T_11: local-RG/RP/covariance/gauge reconstruction,
    T_12: perimeter/cusp/smearing/loop approximation,
    T_13: surface-polymer/exact-entry/exact scalar comparison,
    T_14: Paper-14 whole-process finite-block transport.
    ```

12. **Pushed-forward record law.** All coefficient, decoration, loop,
    transport, and surface-entry quantities are evaluated on the same
    pushed-forward scalar record law fixed by the preceding clauses.

No later section may change `rho_0`, `alpha`, `s`, `epsilon_A`, `chi`, the
window schedule, the character cutoff, the counterterm convention, the
coefficient marginal `K_{p,j}`, or the debit register.

### Lemma 1.5: `P20-SEL0` Instantiates The Frozen Selector

If the Paper-19 `SEL_0` branch data exist on a common Paper-16 heat-kernel
AF trajectory, then `P20-SEL0` satisfies `P20-FROZEN-SEL`.

Proof.

Clauses 1--5 give the Paper-16 AF trajectory, cofinal subsequence, AF-area
schedule, scheme slack, representation channel, and thick/co-scaling window
family required by Definition 1.1. Clauses 6--10 fix the coefficient target,
character cutoff, decoration template, and analytic residual import on the
same Paper-19 `SEL_0` row. Clause 11 is the disjoint transport debit
register, and clause 12 is the required pushed-forward scalar record law.
These are exactly the nine data classes of `P20-FROZEN-SEL`, with additional
first-row constants made explicit. `square`

### Theorem 1.6: `P20-SEL0-NOSMUGGLE`

If `P20-SEL0` holds and the cited Paper-19 `SEL_0` imports are used only in
the roles listed in Definition 1.4, then `P20-NOSMUGGLE` holds for the first
selector.

Proof.

Check the exclusions in Definition 1.2A.

Clauses 1--5 of `P20-SEL0` are structural selector data: AF row labels,
coupling and time labels, cofinal subsequence, square window schedule,
representation channel, and tolerances. They define the quantities entering
`R_0^{crit}` and the AF-matched window geometry, but they do not assert
`R_H^opt<R_H^crit`.

Clause 6 defines the coefficient target `K_{p,j}` and `k_{\rho_0,j}`. It
defines the defect to be estimated; it does not bound that defect. Clause 7
defines the threshold `R_0^{crit}`; defining a threshold is not proving that
the source error lies below it.

Clauses 8--9 choose the same character cutoff and finite decoration template
used in Paper 19. They supply cutoff and combinatorial bookkeeping. They do
not assert `L_AFM^sharp<Sig_AFM`, because the transport ceilings and final
loss comparison remain later Paper-20 estimates.

Clause 10 imports `P19-AN-IMPORT(m)` only as the Paper-16 analytic residual
package proved by Paper 19 Theorem 0A.6 and Corollary 0A.7. That package
provides residual decay and row-compatibility constants. It is not an
area-law, confinement, mass-gap, or continuum-Yang-Mills-existence theorem.

Clause 11 fixes the debit partition, and clause 12 fixes the pushed-forward
record law. These prevent hidden optimization and double charging, but they
do not supply positivity of a string tension, Wilson-loop area law, mass gap,
or either headline scalar inequality.

Thus every `P20-SEL0` clause is structural, readout, selector, analytic
residual, or debit data, and none imports any forbidden conclusion in
Definition 1.2A. Therefore `P20-NOSMUGGLE` holds for `P20-SEL0`. `square`

### Definition 1.7: Second Frozen Candidate `P20-SEL1`

`P20-SEL1` is the first replacement selector after the standard unit-collar
`SEL0` branch. It keeps the same coefficient and AF data as `P20-SEL0`, but
changes the loss-side collar bookkeeping before any source inequality is tested.
The data are:

1. **Shared coefficient selector.** Clauses 1--8, 10, and 12 of
   Definition 1.4 are unchanged: same Paper-16 AF row and cofinal subsequence,
   same `rho_0`, same centered square windows, same AF-area and scheme slack,
   same coefficient target, same coefficient threshold, same character-tail
   schedule, same analytic residual import, and same pushed-forward scalar
   record law. Therefore the coefficient-side closure and the AF signal floor
   are inherited as scalar formulas:

   ```math
   K_0^{src,SEL1}=K_0^{src,SEL0}=0,
   \qquad
   Sig_{AFM}^{SEL1}=Sig_{AFM}^{SEL0},
   ```

   unless a later section explicitly declares a different frozen selector.

2. **Corner-separated decoration template.** Replace the standard unit-collar
   decoration template of Definition 1.4 clause 9 by a corner-separated finite
   template with constants

   ```math
   C_\xi^{SEL1}<\infty,
   \qquad
   E_{corn}^{SEL1}<\infty.
   ```

   The area-charged collar multiplicity per unit excess area is bounded by
   `C_xi^{SEL1}`. Endpoint and corner collars are not charged to the
   multiplicative Paper-15 decoration constant; they are placed in the finite
   endpoint/corner transport debit `E_corn^{SEL1}`.

3. **Decoration debit.** The multiplicative decoration constant for the
   `SEL1` loss worksheet is

   ```math
   C_{dec}^{SEL1}:=C_\xi^{SEL1}.
   ```

   Equivalently, `C_{\xi'}^{SEL1}=0` only as a debit-assignment convention:
   endpoint/corner collar effects are not erased; they are moved to
   `E_corn^{SEL1}`.

4. **Transport debit register.** Use the same four Paper-19 buckets, but charge
   the endpoint/corner collar debit inside the loop-readout bucket:

   ```text
   T_12^{SEL1}
   :=
   A_12^per + A_12^cusp + A_12^smear + A_12^app + E_corn^{SEL1}.
   ```

   The term `E_corn^{SEL1}` may not also be charged in `D_dec`, `T_11`,
   `T_13`, or `T_14`.

No later section may use a `SEL0` unit-collar decoration estimate together with
the `SEL1` coefficient or transport estimates. `SEL1` is a new frozen branch,
not a patch to `SEL0`.

### Lemma 1.8: `P20-SEL1` Instantiates The Frozen Selector

If the shared Paper-19 `SEL_0` coefficient data and the corner-separated finite
collar template exist on a common Paper-16 heat-kernel AF trajectory, then
`P20-SEL1` satisfies `P20-FROZEN-SEL`.

Proof.

The shared clauses give the same AF trajectory, cofinal subsequence,
representation channel, window family, coefficient target, character cutoff,
analytic residual import, and pushed-forward scalar record law already checked
in Lemma 1.5. The new decoration clause is still finite structural
block/collar bookkeeping on the same finite record law. The new transport
clause is a disjoint debit-register declaration: the endpoint/corner collar
term is charged once, in `T_12^{SEL1}`. These are exactly the data required by
Definition 1.1. `square`

### Theorem 1.9: `P20-SEL1-NOSMUGGLE`

If `P20-SEL1` holds and its imports are used only in the roles listed in
Definition 1.7, then `P20-NOSMUGGLE` holds for the second selector.

Proof.

The shared clauses have already been audited in Theorem 1.6. The only new data
are the corner-separated finite template and the assignment of
`E_corn^{SEL1}` to `T_12`. This changes where a finite endpoint/corner debit is
paid; it does not assert that the debit is small, that `L_AFM^sharp<Sig_AFM`,
that `R_H^opt<R_H^crit`, or that an area law, mass gap, or continuum Yang-Mills
measure exists. Since every endpoint/corner contribution remains on the same
pushed-forward scalar record law and is charged exactly once, the new selector
does not import a forbidden conclusion. `square`

### Definition 1.10: Activity-Optimized Third Candidate `P20-SEL2(eta_ch,C_area)`

`P20-SEL2(eta_ch,C_area)` is a parametric family of replacement selectors.
It is not a single frozen branch until the two displayed parameters are fixed.
The point of the family is to keep the same coefficient-side construction while
testing whether the loss-side decoration activity can be made small enough by a
strict character-tail budget and a finite same-record area-collar enumeration.

The data are:

1. **Shared coefficient selector.** Clauses 1--7, 10, and 12 of Definition 1.4
   are unchanged: same Paper-16 AF row and cofinal subsequence, same `rho_0`,
   same centered square windows, same AF-area and scheme slack, same
   coefficient target, same coefficient threshold, same analytic residual
   import, and same pushed-forward scalar record law. Thus the clean
   matched-time coefficient closure remains

   ```math
   K_0^{src,SEL2}=K_0^{src,SEL0}=0,
   \qquad
   Sig_{AFM}^{SEL2}=Sig_{AFM}^{SEL0},
   ```

   unless a later definition explicitly declares a different frozen selector.

2. **Variable character-tail budget.** Replace the canonical half-margin
   character-tail choice of Definition 1.4 clause 8 by a strict declared
   number

   ```math
   0<\eta_{ch}^{SEL2}<1-\eta_{19}^{res},
   ```

   together with the same-record audit

   ```math
   P19\text{-}CHTAIL\text{-}AUDIT(\eta_{ch}^{SEL2}).
   ```

   The value of `eta_ch^{SEL2}` must be fixed before the selector is used as a
   frozen branch. Existence of a possible value may be proved first as a scalar
   theorem; the branch is frozen only after choosing one such value.

3. **Area-collar multiplicative template.** Use the corner-separated template
   convention of `SEL1`: endpoint and corner collars remain outside the
   multiplicative decoration constant and are paid in the disjoint loop-readout
   transport register. The multiplicative decoration register contains only the
   area-charged plaquette-collar templates. Its actual constant is

   ```math
   C_{dec,act}^{SEL2}
   :=
   \limsup_j c_{\xi,j}^{*,SEL2}.
   ```

4. **Finite area-collar ceiling.** The parameter `C_area` is an audited finite
   same-record upper bound for the multiplicative area-collar register:

   ```math
   1\le C_{dec,act}^{SEL2}\le C_{area}<\infty.
   ```

   The lower bound records the standard nonempty unit area-collar contribution.
   The upper bound must be proved by a finite template enumeration; it is not a
   choice of notation.

5. **Disjoint debit register.** Use the same four Paper-19 buckets. The
   endpoint/corner collar debit is charged in `T_12`, area-collar
   multiplicative growth is charged only in `D_dec`, surface-polymer
   decoration growth is charged only through the later `T_13` formula, and
   projective/regulator/volume terms remain outside the loop-readout bucket.

Once `eta_ch^{SEL2}` and `C_area` are fixed and the audits in clauses 2 and 4
are proved, this selector is a candidate `P20-FROZEN-SEL` branch. Until then it
is only a parametric worksheet.

### Lemma 1.11: `P20-SEL2(eta_ch,C_area)` Instantiates The Frozen Selector

Assume the shared Paper-19 coefficient data, the same-record character-tail
audit for `eta_ch^{SEL2}`, and the finite area-collar ceiling `C_area` exist
on a common Paper-16 heat-kernel AF trajectory. Then the frozen instance of
`P20-SEL2(eta_ch,C_area)` satisfies `P20-FROZEN-SEL`.

Proof.

The shared clauses give the same AF trajectory, cofinal subsequence,
representation channel, window family, coefficient target, analytic residual
import, and pushed-forward scalar record law already checked in Lemma 1.5.
Clause 2 supplies a fixed character cutoff and same-record character-tail
budget. Clauses 3--4 supply a finite multiplicative decoration template and
its scalar ceiling. Clause 5 declares the disjoint debit register. These are
exactly the data required by Definition 1.1. `square`

### Theorem 1.12: `P20-SEL2-NOSMUGGLE`

If a frozen instance of `P20-SEL2(eta_ch,C_area)` holds and its imports are
used only in the roles listed in Definition 1.10, then `P20-NOSMUGGLE` holds
for that selector.

Proof.

The shared coefficient and analytic residual clauses were already audited in
Theorem 1.6. The new character-tail clause asks only for the same
`P19-CHTAIL-AUDIT` estimate with a stricter declared budget; it is a cutoff
tail estimate, not an area law, mass gap, coefficient pass, or loss pass. The
new decoration clause gives a finite upper bound on a local area-collar
template count. It does not assert that the bound is below the available
signal floor. Finally, the disjoint debit register records where each loss is
paid; it does not prove any loss is small.

Thus the selector supplies structural, cutoff, finite-template, and debit data
only. None of these data imports `R_H^opt<R_H^crit`,
`L_AFM^sharp<Sig_AFM`, a Wilson-loop area law, a mass gap, or continuum
Yang-Mills existence. `square`

## 2. Heat-Kernel Coefficient Error

### Definition 2.1: Coefficient Source Decomposition `P20-COEFF-SRC`

On a frozen selector, let

```math
\delta_j
=
\left|k_{\rho,j}-e^{-a_j}\right|
```

be the same-record leading coefficient defect of the block plaquette
marginal. The coefficient source decomposition holds when

```math
\limsup_j {\delta_j\over g_{i(j)}^2}
\le
K_{HK}+K_{proj}+K_{chart}+K_{ct}+K_{vol}+K_{tail}
<\infty.
```

The six constants mean:

1. `K_HK`: finite heat-kernel reference defect after block plaquette readout;
2. `K_proj`: projective/block projection defect;
3. `K_chart`: chart and scalar extraction defect;
4. `K_ct`: counterterm convention defect;
5. `K_vol`: finite-volume and boundary passage defect;
6. `K_tail`: RG drift and cofinal tail defect.

Each constant must be evaluated on the same `K_{p,j}` and the same
heat-kernel reference exponent `a_j`.

### Definition 2.2: Coefficient Pass Gate `P20-COEFF-PASS`

`P20-COEFF-PASS` holds when

```math
R_H^{opt}<R_H^{crit},
```

where

```math
R_H^{opt}
=
\limsup_j g_{i(j)}^{-2}\delta_j e^{a_j}.
```

A sufficient source form is

```math
K_{HK}+K_{proj}+K_{chart}+K_{ct}+K_{vol}+K_{tail}
<
R_H^{crit},
```

provided `e^{a_j}` stays cofinally within the Paper-19 coefficient-error
normalization. On the AF-matched branch this normalization is already part
of the Paper-19 selector.

### Theorem 2.3: Source Decomposition Proves The Coefficient Pass

Assume `P20-FROZEN-SEL`, `P20-NOSMUGGLE`, and `P20-COEFF-SRC`. If

```math
K_{HK}+K_{proj}+K_{chart}+K_{ct}+K_{vol}+K_{tail}
<
R_H^{crit},
```

then `P20-COEFF-PASS` holds.

Proof.

By `P20-COEFF-SRC`,

```math
R_H^{opt}
=
\limsup_j g_{i(j)}^{-2}\delta_j e^{a_j}
```

is bounded by the same six source constants, with the harmless exponential
normalization already included in the definitions of those constants on the
frozen selector. The displayed strict inequality therefore gives
`R_H^opt<R_H^crit`. `square`

### Obstruction 2.4: Coefficient Failure

If a lower estimate on the same frozen selector proves

```math
R_H^{opt}\ge R_H^{crit},
```

then this Paper-20 coefficient route fails. This does not by itself falsify
Yang-Mills confinement; it falsifies the AF-matched direct-witness branch
with the selected tower, representation channel, and record battery.

## 2A. First-Selector Coefficient Estimate On `P20-SEL0`

### Definition 2A.1: `SEL0` Coefficient Defect Ledger

On `P20-SEL0`, define the exact leading defect

```math
\delta_j^{(0)}
:=
\left|k_{\rho_0,j}-e^{-a_j}\right|.
```

A `SEL0` coefficient defect ledger is a same-record decomposition

```math
\delta_j^{(0)}
\le
\delta_{HK,j}^{(0)}
+\delta_{proj,j}^{(0)}
+\delta_{chart,j}^{(0)}
+\delta_{ct,j}^{(0)}
+\delta_{vol,j}^{(0)}
+\delta_{tail,j}^{(0)}
```

where every summand is evaluated on the same pushed-forward `P20-SEL0`
scalar record law, the same block-plaquette marginal `K_{p,j}`, the same
reference exponent `a_j`, and the same debit register.

The six Paper-20 first-selector constants are defined with the
`R_H^{opt}` normalization built in:

```math
K_{HK}^{(0)}
:=
\limsup_j
g_{i(j)}^{-2}e^{a_j}\delta_{HK,j}^{(0)},
\qquad
K_{proj}^{(0)}
:=
\limsup_j
g_{i(j)}^{-2}e^{a_j}\delta_{proj,j}^{(0)},
```

```math
K_{chart}^{(0)}
:=
\limsup_j
g_{i(j)}^{-2}e^{a_j}\delta_{chart,j}^{(0)},
\qquad
K_{ct}^{(0)}
:=
\limsup_j
g_{i(j)}^{-2}e^{a_j}\delta_{ct,j}^{(0)},
```

```math
K_{vol}^{(0)}
:=
\limsup_j
g_{i(j)}^{-2}e^{a_j}\delta_{vol,j}^{(0)},
\qquad
K_{tail}^{(0)}
:=
\limsup_j
g_{i(j)}^{-2}e^{a_j}\delta_{tail,j}^{(0)}.
```

This is the Paper-20 version of Paper 19 Definition 8J.10D. Paper 19 writes
the same ledger before the final `e^{a_j}` normalization; Paper 20 absorbs
that bounded AF-matched factor into the six constants so that comparison with
`R_H^{opt}` is exact.

### Definition 2A.2: First-Selector Coefficient Source `P20-SEL0-COEFF-SRC`

`P20-SEL0-COEFF-SRC` holds when:

1. `P20-SEL0` and `P20-SEL0-NOSMUGGLE` hold;
2. the same-record decomposition of Definition 2A.1 holds;
3. all six constants in Definition 2A.1 are finite.

Define

```math
K_0^{src}
:=
K_{HK}^{(0)}
+K_{proj}^{(0)}
+K_{chart}^{(0)}
+K_{ct}^{(0)}
+K_{vol}^{(0)}
+K_{tail}^{(0)}
```

and the first-selector coefficient margin

```math
M_{CE}^{(0)}
:=
R_0^{crit}-K_0^{src}.
```

The six buckets have the following disjoint meanings:

```text
K_HK^(0):    heat-kernel reference defect after block-plaquette readout;
K_proj^(0):  finite-battery projection and block/readout drift;
K_chart^(0): chart and scalar extraction drift;
K_ct^(0):    counterterm convention drift;
K_vol^(0):   finite-volume and boundary passage drift;
K_tail^(0):  RG drift, cofinal tail, and untested-character leakage.
```

No term may be charged to two buckets. In particular, a chart/counterterm
choice used to define `K_HK^(0)` cannot be charged again in `K_chart^(0)` or
`K_ct^(0)`.

### Theorem 2A.3: `SEL0` Coefficient Source Proves The Coefficient Pass

Assume `P20-SEL0-COEFF-SRC`. If

```math
M_{CE}^{(0)}>0,
```

then `P20-COEFF-PASS` holds on the `P20-SEL0` selector.

Proof.

By Definition 2A.1,

```math
\delta_j^{(0)}
\le
\sum_{b\in\{HK,proj,chart,ct,vol,tail\}}\delta_{b,j}^{(0)}.
```

Multiplying by `g_{i(j)}^{-2}e^{a_j}` and taking the limsup gives

```math
R_H^{opt}
=
\limsup_j g_{i(j)}^{-2}e^{a_j}\delta_j^{(0)}
\le
K_0^{src}.
```

The strict margin says `K_0^{src}<R_0^{crit}`. Since `R_0^{crit}` is the
Paper-20 value of `R_H^{crit}` on `P20-SEL0`, this gives
`R_H^{opt}<R_H^{crit}`, i.e. `P20-COEFF-PASS`. `square`

### Theorem 2A.4: Exact First-Selector Coefficient Fork

On `P20-SEL0`, the first-selector coefficient route has the following exact
status.

1. If `P20-SEL0-COEFF-SRC` holds and `M_{CE}^{(0)}>0`, then
   `P20-COEFF-PASS` holds.
2. If one of the six constants is infinite or undefined on the same record
   law, then the `SEL0` coefficient source is not available.
3. If the sharp same-record source evaluation gives `K_0^{src}\ge R_0^{crit}`,
   then this `SEL0` coefficient route fails. This does not falsify every
   possible selector and does not falsify confinement; it falsifies the
   first frozen direct-witness coefficient route.

Proof.

The first clause is Theorem 2A.3. The second is the negation of
Definition 2A.2. The third is the negation of the strict first-selector
margin, with all constants evaluated on the same frozen selector. `square`

## 2B. Heat-Kernel Bucket `K_HK^(0)` On `P20-SEL0`

The first coefficient bucket is the heat-kernel reference defect. This
section attacks only that bucket. It does not charge projection, chart,
counterterm, volume, or tail errors, and it does not prove the full
coefficient pass unless the other five buckets later fit below the same
margin.

### Definition 2B.1: Normalized Heat-Kernel Subledger

On `P20-SEL0`, a heat-kernel subledger is a same-record coefficient chain

```math
u_{0,j}^{bare}
\to
u_{0,j}^{time}
\to
u_{0,j}^{block}
\to
u_{0,j}^{res}
\to
u_{0,j}^{act},
```

where:

```text
u_bare  = fixed Paper-16 heat-kernel coefficient for rho_0;
u_time  = coefficient after the local time/scheme shift only;
u_block = coefficient after same-block local interaction corrections;
u_res   = coefficient after cross-block residual-polymer corrections;
u_act   = actual extracted P20-SEL0 block-plaquette coefficient.
```

The four nonnegative debits are

```math
\delta_{time,j}^{(0)}
:=
\left|u_{0,j}^{time}-u_{0,j}^{bare}\right|,
\qquad
\delta_{block,j}^{(0)}
:=
\left|u_{0,j}^{block}-u_{0,j}^{time}\right|,
```

```math
\delta_{cross,j}^{(0)}
:=
\left|u_{0,j}^{res}-u_{0,j}^{block}\right|,
\qquad
\delta_{extract,j}^{(0)}
:=
\left|u_{0,j}^{act}-u_{0,j}^{res}\right|.
```

Paper 20 uses the same `R_H^{opt}` normalization as Definition 2A.1:

```math
\widehat K_{time}^{(0)}
:=
\limsup_j g_{i(j)}^{-2}e^{a_j}\delta_{time,j}^{(0)},
\qquad
\widehat K_{block}^{(0)}
:=
\limsup_j g_{i(j)}^{-2}e^{a_j}\delta_{block,j}^{(0)},
```

```math
\widehat K_{cross}^{(0)}
:=
\limsup_j g_{i(j)}^{-2}e^{a_j}\delta_{cross,j}^{(0)},
\qquad
\widehat K_{extract}^{(0)}
:=
\limsup_j g_{i(j)}^{-2}e^{a_j}\delta_{extract,j}^{(0)}.
```

The hats mark that these are the Paper-20 normalized versions of Paper 19's
`K_time,K_block,K_cross,K_extract` constants. The subledger is admissible
only after every proof-coordinate object has been pushed forward to the
same scalar `P20-SEL0` record law.

### Theorem 2B.2: Decomposition Bound For `K_HK^(0)`

Every admissible heat-kernel subledger satisfies

```math
K_{HK}^{(0)}
\le
\widehat K_{time}^{(0)}
+\widehat K_{block}^{(0)}
+\widehat K_{cross}^{(0)}
+\widehat K_{extract}^{(0)}.
```

Proof.

The triangle inequality gives

```math
\left|u_{0,j}^{act}-u_{0,j}^{bare}\right|
\le
\delta_{time,j}^{(0)}
+\delta_{block,j}^{(0)}
+\delta_{cross,j}^{(0)}
+\delta_{extract,j}^{(0)}.
```

Multiply by `g_{i(j)}^{-2}e^{a_j}` and take the limsup. This is Paper 19
Theorem 8J.11B with the Paper-20 exponential normalization included.
`square`

### Definition 2B.3: Four Source Envelopes For `P20-SEL0`

Define the bounded AF exponential factor

```math
E_a^{(0)}
:=
\limsup_j e^{a_j}.
```

On `P20-SEL0`, this is finite because Definition 1.4 freezes
`a_j=(C_0/2)\,t_j^{sel}` with
`t_j^{sel}/g_{i(j)}^2` in the declared AF scheme window.

The fixed-time four-source envelopes are:

```math
T_0
:=
\limsup_j {|\tau_j^{time}-t_{i(j)}|\over g_{i(j)}^2},
```

```math
B_0
:=
\limsup_j e^{a_j}{{\mathcal B}_{0,j}\over g_{i(j)}^2},
\qquad
C_0^{res}
:=
\limsup_j e^{a_j}{{\mathcal C}_{0,j}\over g_{i(j)}^2},
\qquad
X_0
:=
\limsup_j e^{a_j}{{\mathcal X}_{0,j}\over g_{i(j)}^2}.
```

Here `mathcal B`, `mathcal C`, and `mathcal X` are exactly the same-block,
cross-block residual, and extraction/readout scalar coefficient differences
of Paper 19 Definition 8J.12A, evaluated on the same `P20-SEL0` record law.
In this Paper-20 ledger, `mathcal X` is charged to the heat-kernel bucket
only on the exact coefficient-readout route. If loop approximation, finite
precision, representation truncation, or projective finite-battery errors
remain, those errors belong to `K_proj^(0)` or `K_tail^(0)` and may not be
charged again here.

The fixed-time heat-kernel source gate `P20-SEL0-HK-FIX-SRC(T_0,B_0,C_0^{res},X_0)`
holds when these four envelopes are finite and the four debits of Definition
2B.1 are bounded by them:

```math
\widehat K_{time}^{(0)}
\le
E_a^{(0)}{C_0\over2}T_0,
\qquad
\widehat K_{block}^{(0)}\le B_0,
\qquad
\widehat K_{cross}^{(0)}\le C_0^{res},
\qquad
\widehat K_{extract}^{(0)}\le X_0.
```

The factor `E_a^{(0)}` appears only in the time debit because Paper 19's
time envelope is written before Paper 20's final `e^{a_j}` normalization.
The other three envelopes are defined here after that normalization.

### Theorem 2B.4: Fixed-Time Heat-Kernel Bound

If `P20-SEL0-HK-FIX-SRC(T_0,B_0,C_0^{res},X_0)` holds, then

```math
K_{HK}^{(0)}
\le
E_a^{(0)}{C_0\over2}T_0
+B_0+C_0^{res}+X_0.
```

Consequently, the fixed-time heat-kernel bucket passes its own first-selector
test if

```math
E_a^{(0)}{C_0\over2}T_0
+B_0+C_0^{res}+X_0
<
R_0^{crit}.
```

Proof.

Use Definition 2B.3 in Theorem 2B.2. The final strict inequality is only the
single-bucket test; the full coefficient pass still requires the other five
coefficient buckets of Definition 2A.1. `square`

### Definition 2B.5: Matched-Time Heat-Kernel Source

Suppose the same heat-kernel subledger has `0<u_{0,j}^{time}<1` cofinally.
Define

```math
\tau_j^{match}
:=
-{2\over C_0}\log u_{0,j}^{time}.
```

The matched-time branch is admissible when:

```math
1-\chi
\le
{\tau_j^{match}\over g_{i(j)}^2}
\le
1+\chi
```

cofinally, and every tested character, tail, decoration, transport, and
first-excess ledger is evaluated on the same matched-time record family.

The gate `P20-SEL0-HK-MATCH-SRC(B_0,C_0^{res},X_0)` holds when the matched
time is admissible and

```math
\widehat K_{block}^{(0)}\le B_0,
\qquad
\widehat K_{cross}^{(0)}\le C_0^{res},
\qquad
\widehat K_{extract}^{(0)}\le X_0.
```

It is not admissible to choose

```math
\tau_j^{act}:=-{2\over C_0}\log u_{0,j}^{act}
```

unless a separate source theorem proves that the block, cross, and
extraction debits are pure time/scheme shifts. Otherwise the refit would
hide non-time record-law errors inside a proof coordinate.

### Theorem 2B.6: Matched-Time Heat-Kernel Bound

If `P20-SEL0-HK-MATCH-SRC(B_0,C_0^{res},X_0)` holds, then the matched-time
heat-kernel bucket satisfies

```math
K_{HK,match}^{(0)}
\le
B_0+C_0^{res}+X_0.
```

Proof.

By definition of `tau_j^{match}`,

```math
u_{0,j}^{time}
=
\exp(-\tau_j^{match}C_0/2).
```

Thus the time/scheme debit is zero in the matched reference coordinate. The
triangle inequality leaves only the block, cross, and extraction debits.
Multiplying by `g_{i(j)}^{-2}e^{a_j}` and taking the limsup gives the
displayed bound. The admissibility clauses ensure that this has not changed
the record law or hidden other debits. `square`

### Theorem 2B.7: Clean `SEL0` Matched-Time Import Closes `K_HK`

Assume `P20-SEL0`, `P20-SEL0-NOSMUGGLE`, and the clean Paper-19 local import
used in Definition 1.4:

```text
coefficient-only MIN-SEL_0,
exact normalized rho_0 coefficient readout,
Paper-16 HK-SF-YM2 on the same pushed-forward record law,
local large-field import,
pure-gauge counterterm ledger,
time-only matched scheme branch,
P19-AN-IMPORT(m),
centered square fractional SEL_0 collar geometry.
```

Then, on the matched-time `P20-SEL0` branch,

```math
B_0=0,
\qquad
C_0^{res}=0,
\qquad
X_0=0,
```

and therefore

```math
K_{HK,match}^{(0)}=0.
```

This proves only the heat-kernel bucket on the clean matched-time selector.
It does not prove the fixed-time `K_HK^(0)=0`, and it does not prove the
full coefficient estimate until `K_proj^(0),K_chart^(0),K_ct^(0),K_vol^(0)`,
and `K_tail^(0)` are evaluated on the same record law.

Proof.

Paper 19 Theorem 8J.24E gives, on the same coefficient-only `SEL_0` row,

```math
HK\text{-}BLOCK\text{-}COEFF_0(0),
\qquad
HK\text{-}CROSS\text{-}COEFF_0(0),
\qquad
HK\text{-}EXTRACT\text{-}COEFF_0(0).
```

Corollary 8J.24F states the same result as a pushed-forward scalar record
identity, not as a hidden gauge-fixed field statement. These are exactly the
matched-time source bounds `B_0=C_0^{res}=X_0=0` in Definition 2B.5, after
Paper 20's harmless `e^{a_j}` normalization. Theorem 2B.6 then gives
`K_HK,match^(0)=0`.

The no-smuggling condition is preserved because the imported clauses are
local analytic, finite-record, and selector-geometry statements. They do not
assert `R_H^{opt}<R_H^{crit}`, `L_AFM^{sharp}<Sig_AFM`, an area law, a mass
gap, or existence of the continuum Yang-Mills measure. `square`

For the rest of Paper 20, the notation `K_HK^(0)` means the heat-kernel
bucket for the declared branch. If the fixed-time branch is declared, it is
the fixed-time bucket of Theorem 2B.4. If the matched-time branch is declared,
it is the matched-time bucket of Theorem 2B.6 with
`a_j=\tau_j^{match}C_0/2`. Switching branches after seeing the other source
constants is not allowed; that would violate the frozen-selector ledger.

### Obstruction 2B.8: Heat-Kernel Bucket Failure Modes

The heat-kernel bucket remains open or fails in exactly the following ways:

1. the fixed-time defect is not `O(g_i^2)` after the Paper-20 normalization;
2. the fixed-time lower floor already consumes `R_0^{crit}`;
3. the matched time leaves the AF scheme window
   `(1-\chi)g_i^2 <= tau_j^{match} <= (1+\chi)g_i^2`;
4. the matched-time branch is obtained by fitting `tau_j^{act}` and thereby
   hiding block, cross, or extraction errors;
5. one of the clean local imports used in Theorem 2B.7 fails on the same
   pushed-forward record law.

These are heat-kernel bucket obstructions only. They do not by themselves
decide the remaining coefficient buckets or the loss estimate.

## 2C. Remaining Coefficient Buckets On The Matched-Time `P20-SEL0` Branch

The clean matched-time branch of Section 2B leaves five coefficient buckets:

```text
K_proj^(0), K_chart^(0), K_ct^(0), K_vol^(0), K_tail^(0).
```

This section evaluates them on the same frozen branch. The evaluation is
not a new physical estimate. It is a debit audit: if the coefficient target
is the exact pushed-forward scalar record already frozen in Definition 1.4,
then these five buckets are not additional analytic errors. If any
approximating projection, chart, counterterm conversion, volume passage, or
character truncation is inserted, the corresponding bucket reopens.

### Definition 2C.1: Exact Remaining-Bucket Clauses

On the matched-time `P20-SEL0` branch, define the exact remaining-bucket
clauses as follows.

1. `P20-SEL0-PROJ0`: the block plaquette marginal `K_{p,j}` is already the
   pushed-forward post-projection scalar record used in the coefficient
   target. No further projection, block approximation, or finite-battery
   surrogate is inserted when computing `k_{\rho_0,j}`.
2. `P20-SEL0-CHART0`: the coefficient is the Haar projection of the central
   scalar marginal `K_{p,j}`. Gauge charts, axial trees, collar extensions,
   and local fields are used only to prove source estimates and are eliminated
   before the scalar coefficient is read.
3. `P20-SEL0-CT0`: the clean counterterm convention is the same convention
   used in Section 2B. The pure-gauge relevant/marginal counterterms are
   time-tangent or normalization-fixed, and no additional non-time
   counterterm conversion is applied to the leading coefficient.
4. `P20-SEL0-VOL0`: the coefficient source is evaluated on the declared
   finite cofinal row. No infinite-volume passage or boundary-buffer limit is
   inserted into `R_H^{opt}`. Whole-process finite-block transport belongs to
   the later loss bucket `T_14`, not to this leading-coefficient debit.
5. `P20-SEL0-TAIL0`: the selected leading coefficient is read exactly in the
   `rho_0` channel. Non-leading character tails are assigned to
   `P20-DEC-SRC` and `T_13`, not to the leading coefficient defect. No
   truncated-character surrogate is used for `k_{\rho_0,j}`.

These clauses are the Paper-20 form of the no-double-charge rule. They do
not say that non-leading character tails, volume transport, or loop-readout
losses vanish in the whole proof. They say only that those effects are not
part of the leading coefficient error once the exact scalar coefficient
target has been frozen.

### Lemma 2C.2: Exact Clauses Give Zero Remaining Debits

On the matched-time `P20-SEL0` branch:

```math
P20\text{-}SEL0\text{-}PROJ0
\Rightarrow
K_{proj}^{(0)}=0,
```

```math
P20\text{-}SEL0\text{-}CHART0
\Rightarrow
K_{chart}^{(0)}=0,
```

```math
P20\text{-}SEL0\text{-}CT0
\Rightarrow
K_{ct}^{(0)}=0,
```

```math
P20\text{-}SEL0\text{-}VOL0
\Rightarrow
K_{vol}^{(0)}=0,
```

and

```math
P20\text{-}SEL0\text{-}TAIL0
\Rightarrow
K_{tail}^{(0)}=0.
```

Proof.

Each implication is an identity of the corresponding debit in Definition
2A.1.

`P20-SEL0-PROJ0` says the coefficient is computed from the exact
post-projection scalar marginal already named `K_{p,j}`. Therefore there is
no second projection map whose error could contribute to
`\delta_{proj,j}^{(0)}`.

`P20-SEL0-CHART0` says all gauge-chart and local-field coordinates have
already been pushed forward to the central scalar record before the Haar
projection is taken. Therefore the chart-transport difference in the leading
coefficient ledger is zero.

`P20-SEL0-CT0` says the clean counterterm convention is the same convention
used by the matched-time heat-kernel row, and any relevant/marginal
counterterm freedom has been absorbed into the declared time coordinate or
normalization. Therefore no additional counterterm convention difference
remains in `\delta_{ct,j}^{(0)}`.

`P20-SEL0-VOL0` says the coefficient estimate is a finite-row same-record
statement. Since no infinite-volume or boundary-buffer comparison is made in
the coefficient defect, `\delta_{vol,j}^{(0)}=0`. This does not remove
finite-block whole-process transport from the proof; that loss is assigned
to `T_14`.

`P20-SEL0-TAIL0` says the leading coefficient is not approximated by a
finite character surrogate: it is the exact Haar projection onto the
selected `rho_0` record. Thus untested-character leakage is absent from the
leading coefficient error. The non-leading character tail is still charged
later through `P20-DEC-SRC` and `T_13`.

In all five cases the corresponding pointwise debit is zero, so after
multiplication by `g_{i(j)}^{-2}e^{a_j}` and taking `limsup`, the normalized
constant is zero. `square`

### Theorem 2C.3: Clean Matched-Time `P20-SEL0` Closes The Coefficient Source

Assume:

```text
P20-SEL0,
P20-SEL0-NOSMUGGLE,
P20-SEL0-HK-MATCH-SRC(0,0,0),
P20-SEL0-PROJ0,
P20-SEL0-CHART0,
P20-SEL0-CT0,
P20-SEL0-VOL0,
P20-SEL0-TAIL0.
```

Then the first-selector coefficient source has

```math
K_{HK}^{(0)}=0,
\qquad
K_{proj}^{(0)}=0,
\qquad
K_{chart}^{(0)}=0,
```

```math
K_{ct}^{(0)}=0,
\qquad
K_{vol}^{(0)}=0,
\qquad
K_{tail}^{(0)}=0.
```

Consequently

```math
K_0^{src}=0,
\qquad
M_{CE}^{(0)}=R_0^{crit}>0,
```

and `P20-COEFF-PASS` holds on this declared matched-time selector.

Proof.

The heat-kernel bucket is zero by Theorem 2B.7. The other five buckets are
zero by Lemma 2C.2. Therefore the sum `K_0^{src}` in Definition 2A.2 is
zero. Since `rho_0` is nontrivial and `0<\chi,\epsilon_A<1`,

```math
R_0^{crit}
=
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}{C_0\over2}
>0.
```

Thus `M_CE^(0)>0`, and Theorem 2A.3 gives `P20-COEFF-PASS`.
`square`

### Corollary 2C.4: What This Does And Does Not Prove

Theorem 2C.3 proves the Paper-20 coefficient inequality

```math
R_H^{opt}<R_H^{crit}
```

for the clean matched-time `P20-SEL0` coefficient selector.

It does not prove:

```text
fixed-time K_HK^(0)=0;
positive leading sheet rate kappa_13^CE>0;
T_13 subcriticality q_13^act<1;
the loss inequality L_AFM^sharp<Sig_AFM;
an unconditional 4D SU(N) continuum Yang-Mills measure;
an area law or mass gap.
```

The reason is simple: the coefficient pass is a relative same-record
heat-kernel reference estimate. In the matched-time branch, it is allowed to
choose the heat-kernel time as an admissible scheme coordinate for the
leading coefficient. The dynamical confinement content still lives in the
loss-side source estimates, especially the `T_13` leading-rate and
surface-polymer audits.

### Obstruction 2C.5: Reopening The Remaining Buckets

If any exact clause in Definition 2C.1 is replaced by an approximation, the
corresponding bucket must be evaluated rather than set to zero:

```text
nonexact finite battery or block projection        -> K_proj^(0);
exported gauge-chart or scalar-extraction drift    -> K_chart^(0);
changed counterterm convention outside time        -> K_ct^(0);
infinite-volume/boundary passage inside R_H        -> K_vol^(0);
truncated leading coefficient or hidden char tail  -> K_tail^(0).
```

Such a reopened bucket must be bounded on the same pushed-forward
`P20-SEL0` record law with the same `e^{a_j}` normalization before
Theorem 2C.3 can be used.

## 3. Loss Worksheet, Signal Floor, And Decoration Constants

### 3A. `P20-SEL0` Loss Worksheet And Signal Floor

The coefficient side is now closed on one specific branch: the clean
matched-time exact-record `P20-SEL0` selector. The loss side must use the
same selector. This section freezes the loss worksheet and evaluates the
signal floor before any decoration or transport losses are compared to it.

#### Definition 3A.1: Loss Worksheet `P20-SEL0-LOSS`

`P20-SEL0-LOSS` is the loss-side worksheet attached to the same selector as
Theorem 2C.3. It consists of:

1. the same cofinal heat-kernel row and subsequence `j -> i(j)`;
2. the same representation `rho_0`, Casimir `C_0`, and matched-time
   coefficient branch;
3. the same centered square windows

   ```math
   R_j=T_j=L_j,\qquad
   L_j=\lfloor\sqrt{sH_j}\rfloor,\qquad
   \sigma_j=\lfloor\alpha L_j\rfloor;
   ```

4. the same AF-area bounds

   ```math
   s_-:=s(1-\epsilon_A),
   \qquad
   s_+:=s(1+\epsilon_A);
   ```

5. a fixed geometry tolerance

   ```math
   0<\epsilon_G<\min\{\alpha^2,2(1-\alpha)\};
   ```

6. the same character cutoff, decoration template, analytic residual import,
   and transport debit register as Definition 1.4.

No later loss estimate may change these data. In particular, the loss side
may not switch from the matched-time exact-record coefficient selector to a
different coefficient branch.

#### Lemma 3A.2: Thick-Window Constants For `P20-SEL0`

On `P20-SEL0-LOSS`, after passing to a cofinal tail,

```math
q_-^{SEL0}:=\alpha^2-\epsilon_G
\le
{Q_{\sigma,j}\over S_j},
```

and

```math
{N_{0,j}\over S_j}
\le
n_+^{SEL0}:=2(1-\alpha)+\epsilon_G.
```

Proof.

Paper 19 Lemma 8J.10B proves, for the same integer-rounded square schedule,

```math
{Q_{\sigma,j}\over S_j}\to\alpha^2,
\qquad
{N_{0,j}\over S_j}\to2(1-\alpha).
```

The chosen `epsilon_G` is strictly smaller than both limiting positive
quantities needed here, so the displayed one-sided estimates hold on a
cofinal tail. `square`

#### Definition 3A.3: Evaluated `SEL0` Signal Floor

On the clean matched-time exact-record coefficient branch, Theorem 2C.3
gives a zero coefficient source debit:

```math
R_H^{SEL0}:=K_0^{src}=0.
```

Therefore the Paper-19 AF-matched signal exponents reduce to

```math
A_{AFM}^{SEL0}
:=
{(1+\chi)s_+C_0\over2},
```

and

```math
B_{AFM}^{SEL0}
:=
{(1-\chi)s_-C_0\over2}.
```

Since `rho_0` is nontrivial and
`s>0`, `0<epsilon_A<1`, `0<chi<1`, we have

```math
B_{AFM}^{SEL0}>0.
```

The evaluated signal floor for the frozen selector is

```math
Sig_{AFM}^{SEL0}
:=
\exp\left(-n_+^{SEL0}A_{AFM}^{SEL0}\right)
\left(
1-\exp\left(-q_-^{SEL0}B_{AFM}^{SEL0}\right)
\right).
```

Equivalently,

```math
Sig_{AFM}^{SEL0}
=
\exp\left(
-\left[2(1-\alpha)+\epsilon_G\right]
{(1+\chi)s(1+\epsilon_A)C_0\over2}
\right)
\left[
1-\exp\left(
-\left[\alpha^2-\epsilon_G\right]
{(1-\chi)s(1-\epsilon_A)C_0\over2}
\right)
\right].
```

This is strictly positive. It is the right-hand side for the remaining
loss comparison on the declared branch.

#### Theorem 3A.4: `P20-SEL0-LOSS` Supplies The Paper-19 Signal Floor

Assume `P20-SEL0-LOSS` and the clean matched-time coefficient closure of
Theorem 2C.3. Then the Paper-19 signal floor `Sig_AFM` specialized to this
selector is exactly `Sig_AFM^{SEL0}`.

Proof.

Paper 19 Definition 8K.1 defines

```math
Sig_{AFM}
=
\exp(-n_+A_{AFM}^*)\left(1-\exp(-q_-B_{AFM}^*)\right),
```

with

```math
A_{AFM}^*
=
{(1+\chi)s_+C_2(\rho)\over2}
+ {s_+R_H\over1-r_*},
\qquad
B_{AFM}^*
=
{(1-\chi)s_-C_2(\rho)\over2}
-s_+R_H.
```

On `P20-SEL0`, `rho=rho_0`, `C_2(\rho_0)=C_0`, and Theorem 2C.3 gives
`R_H=0` for the clean matched-time coefficient source. Lemma 3A.2 supplies
`q_-=q_-^{SEL0}` and `n_+=n_+^{SEL0}`. Substitution gives the displayed
`Sig_AFM^{SEL0}`. `square`

The remaining Paper-20 loss task is therefore the scalar inequality

```math
L_{AFM}^{sharp}<Sig_{AFM}^{SEL0}.
```

### Definition 3.1: Decoration Source Gate `P20-DEC-SRC`

`P20-DEC-SRC(eta_res^*,eta_ch^*,c_Delta^*)` holds when, on the frozen
selector,

```math
\limsup_j\eta_{res,j}^{bd}\le\eta_{res}^*,
\qquad
\limsup_j C_{ch,j}Tail_{CE,j}\le\eta_{ch}^*,
\qquad
\limsup_j c_{\Delta,j}^*\le c_\Delta^*,
```

with

```math
\eta_*:=\eta_res^*+\eta_ch^*<1.
```

This is exactly the Paper-19 decoration ledger, evaluated again on the
selector frozen in Section 1.

### Theorem 3.2: Decoration Source Gate Bounds The Decoration Debit

If `P20-DEC-SRC(eta_res^*,eta_ch^*,c_Delta^*)` holds, then

```math
\limsup_j\Delta_{dec,j}^{bd}
\le
D_{dec}^*
:=
\exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1.
```

Moreover the non-leading `CE` tail satisfies

```math
\epsilon_{13}^{CE}\le\eta_ch^*<\infty
```

on the same character/decorrelation ledger.

Proof.

The first inequality is Paper 19 Theorem 8L.10 on the frozen selector. The
second is Paper 19 Theorem 8L.11A.22G.4D.22, which identifies the
non-leading `CE` tail with the same `Tail_CE` envelope used by
`P19-T13-DEC`. No additional cutoff is introduced. `square`

### Definition 3.3: Canonical `SEL0` Decoration Constants

On `P20-SEL0-LOSS`, use the clean Paper-19 analytic import and centered
square finite-template decoration geometry:

```math
\eta_{res}^{SEL0}:=\eta_{19}^{res},
```

```math
\eta_{ch}^{SEL0}:={1-\eta_{19}^{res}\over2},
```

```math
c_\Delta^{SEL0}
:=
C_\xi^{SEL0}+C_{\xi'}^{SEL0}.
```

Set

```math
\eta_{SEL0}
:=
\eta_{res}^{SEL0}+\eta_{ch}^{SEL0}
=
{1+\eta_{19}^{res}\over2}.
```

Since the clean analytic import gives `0<=eta_19^res<1`,

```math
0\le\eta_{SEL0}<1.
```

The associated decoration debit is

```math
D_{dec}^{SEL0}
:=
\exp\left(
{c_\Delta^{SEL0}\eta_{SEL0}
\over
1-\eta_{SEL0}}
\right)-1.
```

### Theorem 3.4: Canonical `SEL0` Branch Closes `P20-DEC-SRC`

Assume `P20-SEL0-LOSS` and the clean Paper-19 imports fixed in Definition
1.4:

```text
P19-AN-AUDIT(m),
P19-CHTAIL-AUDIT((1-eta_19^res)/2),
P19-FBTPL-DEC(C_xi^SEL0,C_xip^SEL0).
```

Then

```text
P20-DEC-SRC(eta_res^SEL0, eta_ch^SEL0, c_Delta^SEL0)
```

holds, and

```math
\limsup_j\Delta_{dec,j}^{bd}
\le
D_{dec}^{SEL0}.
```

Moreover the non-leading coefficient-entry tail satisfies

```math
\epsilon_{13}^{CE}
\le
\eta_{ch}^{SEL0}
<
\infty.
```

Proof.

Paper 19 Theorem 0A.6 proves `P19-AN-AUDIT(m)` for the clean `SEL_0`
branch, and Corollary 0A.7 gives

```math
\limsup_j\eta_{res,j}^{bd}\le\eta_{19}^{res}<1.
```

Paper 19 Corollary 8L.8B proves
`P19-CHTAIL-AUDIT((1-eta_19^res)/2)`, hence

```math
\limsup_j C_{ch,j}Tail_{CE,j}
\le
{1-\eta_{19}^{res}\over2}
=\eta_{ch}^{SEL0}.
```

Paper 19 Lemma 8L.9A.1 gives the centered square finite-template decoration
geometry, and Theorem 8L.9B gives

```math
\limsup_j c_{\Delta,j}^*
\le
C_\xi^{SEL0}+C_{\xi'}^{SEL0}
=c_\Delta^{SEL0}.
```

These are exactly the three clauses of Definition 3.1, and
`eta_SEL0<1` was checked in Definition 3.3. The decoration debit bound is
Theorem 3.2 with these constants. The non-leading tail bound is the second
part of Theorem 3.2, equivalently Paper 19 Theorem 8L.11A.22G.4D.22, on
the same character/decorrelation ledger. `square`

### Corollary 3.5: First Loss Comparison After Decoration Closure

After Theorem 3.4, the remaining `P20-SEL0` loss comparison is

```math
D_{dec}^{SEL0}
+T_{11}^*+T_{12}^*+T_{13}^*+T_{14}^*
<
Sig_{AFM}^{SEL0}.
```

Equivalently, the transport budget must fit under the residual scalar
margin

```math
M_{loss}^{SEL0}
:=
Sig_{AFM}^{SEL0}-D_{dec}^{SEL0}.
```

If `M_loss^SEL0<=0`, then the component-source route of Paper 20 cannot
close the loss inequality, even before transport losses are charged. If
`M_loss^SEL0>0`, the next task is to prove

```math
T_{11}^*+T_{12}^*+T_{13}^*+T_{14}^*
<
M_{loss}^{SEL0}.
```

### Definition 3.6: Computed Residual Transport Margin

For the canonical `SEL0` decoration constants, set

```math
C_{dec}^{SEL0}
:=
C_\xi^{SEL0}+C_{\xi'}^{SEL0}.
```

Since

```math
\eta_{SEL0}={1+\eta_{19}^{res}\over2},
\qquad
1-\eta_{SEL0}={1-\eta_{19}^{res}\over2},
```

the decoration debit simplifies to

```math
D_{dec}^{SEL0}
=
\exp\left(
C_{dec}^{SEL0}
{1+\eta_{19}^{res}\over1-\eta_{19}^{res}}
\right)-1.
```

Therefore the residual transport margin is the explicit scalar

```math
M_{loss}^{SEL0}
=
\exp\left(
-\left[2(1-\alpha)+\epsilon_G\right]
{(1+\chi)s(1+\epsilon_A)C_0\over2}
\right)
\left[
1-\exp\left(
-\left[\alpha^2-\epsilon_G\right]
{(1-\chi)s(1-\epsilon_A)C_0\over2}
\right)
\right]
+1
-
\exp\left(
C_{dec}^{SEL0}
{1+\eta_{19}^{res}\over1-\eta_{19}^{res}}
\right).
```

Equivalently,

```math
M_{loss}^{SEL0}>0
```

holds exactly when

```math
C_{dec}^{SEL0}
<
{1-\eta_{19}^{res}\over1+\eta_{19}^{res}}
\log\left(1+Sig_{AFM}^{SEL0}\right).
```

This is the decoration-only bottleneck before any transport debit is
charged.

### Theorem 3.7: Exact Transport-Margin Fork

On the clean matched-time `P20-SEL0` branch:

1. if `M_loss^SEL0>0`, then the remaining loss problem is exactly

   ```math
   T_{11}^*+T_{12}^*+T_{13}^*+T_{14}^*
   <
   M_{loss}^{SEL0};
   ```

2. if `M_loss^SEL0<=0`, then the component-source route cannot prove
   `P20-LOSS-PASS` on this selector, regardless of how small the transport
   ceilings are.

Proof.

By Corollary 3.5, the loss inequality is

```math
D_{dec}^{SEL0}
+T_{11}^*+T_{12}^*+T_{13}^*+T_{14}^*
<
Sig_{AFM}^{SEL0}.
```

Subtracting `D_dec^SEL0` gives clause 1. Since the transport ceilings are
nonnegative debits, if `Sig_AFM^SEL0-D_dec^SEL0<=0`, then even the zero
transport budget cannot make the strict inequality true. The displayed
closed-form threshold follows from

```math
D_{dec}^{SEL0}<Sig_{AFM}^{SEL0}
```

and monotonicity of the exponential. `square`

## 4. Transport And Surface-Entry Ceilings

### Definition 4.0A: `SEL0` Common-Record Transport Audit

`P20-SEL0-TR-COMMON` is the Paper-20 instantiation of Paper 19
`P19-TR-COMMON` on the clean matched-time `SEL0` selector. It holds when the
following data are fixed and identified before any transport ceiling is
estimated:

1. **One whole-process record tower.** The finite laws are the restrictions
   of the same frozen scalar record law:

   ```text
   Gamma_j^{SEL0} = rho_j(Law_*^{SEL0})
   ```

   on the finite record algebras `F_j^{SEL0}` of Definition 1.4 and the loss
   worksheet of Definition 3A.1.

2. **One Paper-16 heat-kernel tower after pushforward.** The Paper-16 common
   tower `T_HK` is identified with the same scalar laws, not with an
   independent gauge-fixed or local-field process:

   ```text
   B_j^{HK} = F_j^{SEL0} or the declared common refinement,
   Gamma_j^{HK} = Gamma_j^{SEL0},
   Pi_{j->k}^{HK} = Pi_{j->k}^{SEL0}.
   ```

3. **One certificate family.** The Paper-16 certificates feeding projectivity,
   regulator/chart comparison, reflection positivity, Euclidean covariance,
   loop continuity, nontriviality, and the `X_15`/surface-entry ledgers use the
   same finite batteries, loop approximants, counterterm branches, comparison
   maps, and scalar readouts as `P20-SEL0-LOSS`.

4. **One Paper-14 export chain.** The Paper-14 finite-block transport vector
   `E_14(eta_j)` is read on this same cofinal battery family. Its entries are
   assigned to `T_14`, except when the debit register declares a shared scalar
   value that is counted exactly once.

5. **One disjoint debit register.** Every source defect has one scalar value
   and one ledger home among

   ```text
   Delta_dec, T_11, T_12, T_13, T_14.
   ```

   In particular, projective, regulator/chart, and finite-volume loop
   transport are not charged to `T_12` if they are already assigned to `T_11`
   or `T_14`; decoration activity is not charged again through `T_13`.

6. **No hidden dynamical subprocess.** Gauge charts, axial trees, local fields,
   heat-kernel coordinates, and polymer expansions may be used only as proof
   coordinates. Every exported quantity must be a scalar inequality for the
   pushed-forward record laws `Gamma_j^{SEL0}`.

This audit is a compatibility statement. It does not assert a positive
transport margin, a surface subcriticality bound, a continuum Yang-Mills
measure, or an area law.

### Theorem 4.0B: `SEL0` Instantiates Paper 19 `P19-TR-COMMON`

Assume:

```text
P20-SEL0,
P20-SEL0-LOSS,
HK-WP-CLOSE on the identified Paper-16 tower,
same-battery Paper-14 export chain eta_j,
the disjoint debit assignment of Definition 4.0A.
```

Then `P20-SEL0-TR-COMMON` holds. Consequently the Paper-19 common-record
transport audit `P19-TR-COMMON` holds on the `SEL0` selector.

Proof.

`P20-SEL0` fixes the cofinal AF row, finite scalar record laws, restriction
maps, representation channel, loop/window batteries, character cutoff,
decoration template, analytic import, and transport debit register. The loss
worksheet `P20-SEL0-LOSS` reuses exactly those data on the loss side. The
assumed `HK-WP-CLOSE` identifies the Paper-16 heat-kernel tower with these
same pushed-forward laws and requires the projective, regulator, RP/covariance,
loop-continuity, nontriviality, and `X_15` certificates to share batteries,
maps, counterterms, loop approximants, and constants. The same-battery Paper-14
export attaches `E_14(eta_j)` to this same finite family.

The disjoint debit assignment gives each source defect one scalar value and one
ledger home among `Delta_dec,T_11,T_12,T_13,T_14`. The final clause of
Definition 4.0A eliminates proof-coordinate subprocesses by requiring every
quantity to be pushed forward to the scalar record laws `Gamma_j^{SEL0}`.
These are exactly the six clauses of Paper 19 `P19-TR-COMMON`. `square`

### Definition 4.1: Transport Source Gate `P20-TLOSS-SRC`

`P20-TLOSS-SRC(T_11^*,T_12^*,T_13^*,T_14^*)` holds when the common-record
transport audit has been instantiated and the four Paper-19 transport buckets
satisfy

```math
\limsup_j T_{11,j}\le T_{11}^*,
\qquad
\limsup_j T_{12,j}\le T_{12}^*,
\qquad
\limsup_j T_{13,j}\le T_{13}^*,
\qquad
\limsup_j T_{14,j}\le T_{14}^*.
```

The buckets are disjoint:

```text
T_11: local-RG/RP/covariance/gauge reconstruction,
T_12: perimeter/cusp/smearing/loop approximation,
T_13: surface-polymer/exact-entry/exact scalar comparison,
T_14: Paper-14 whole-process finite-block transport.
```

### Definition 4.2: Surface-Entry Source Gate `P20-T13-SRC`

The `T_13` source gate is the hardest component of `P20-TLOSS-SRC`. It holds
when the frozen selector supplies:

```text
P20-T13-SUB(q_13^*) with q_13^*<1,
P20-T13-SURF(A_13^surf),
P20-T13-ENTRY(A_13^entry),
P20-T13-EXACT(A_13^exact),
```

and

```math
T_{13}^*
=
A_{13}^{surf}+A_{13}^{entry}+A_{13}^{exact}.
```

The subcriticality part is the real confinement-pressure test:

```math
q_{13}^{act}
:=
\limsup_j\max_C D_{C,j}E_{C,j}^{surf}u_{\rho,s_0,j}
<1.
```

### Definition 4.3: `SEL0` Transport Ceiling Evaluation

Assume `P20-SEL0-TR-COMMON`. On the clean matched-time `P20-SEL0` selector,
the four transport ceilings are the following Paper-19 same-record source
constants, evaluated on the `SEL0` record tower and debit register.

First,

```math
T_{11}^{SEL0}
:=
A_{11}^{loc,SEL0}
+A_{11}^{RP,SEL0}
+A_{11}^{Cov,SEL0}
+A_{11}^{gauge,SEL0}.
```

These are the reduced local-RG, reflection-positivity, Euclidean-covariance,
and scalar gauge/chart reconstruction tails of Paper 19 Definition 8L.11A.5.
On `SEL0`, the evaluated components are

```math
A_{11}^{loc,SEL0}
:=
\limsup_j
\sum_{k\ge j}
L_j^{rec}
\left(
\eta_{locRG,k}^{B_j}
+\eta_{prec,j,k}^{(11)}
\right),
```

```math
A_{11}^{RP,SEL0}
:=
\limsup_j
\sum_{k\ge j}
\left(
\eta_{binRP,j,k}^{(11)}
+\eta_{projRP,j,k}^{(11)}
+\eta_{regRP,j,k}^{(11)}
+\eta_{volRP,j,k}^{(11)}
+\eta_{ctRP,j,k}^{(11,red)}
\right),
```

```math
A_{11}^{Cov,SEL0}
:=
\limsup_j
\sup_{g\in Euc_{adm}(B_j)}
\sum_{k\ge j}
\left(
\eta_{exactCov,j,k}(g)
+\eta_{appCov,j,k}^{(11)}(g)
+\eta_{binCov,j,k}^{(11)}(g)
+\eta_{blockCov,j,k}^{(11)}(g)
+\eta_{projCov,j,k}^{(11)}(g)
+\eta_{regCov,j,k}^{(11)}(g)
+\eta_{volCov,j,k}^{(11)}(g)
+\eta_{ctCov,j,k}^{(11,red)}(g)
\right),
```

and

```math
A_{11}^{gauge,SEL0}
:=
\limsup_j
\sum_{k\ge j}
\left(
\eta_{chart,j,k}^{(11)}
+\eta_{gauge-rec,j,k}^{(11)}
\right),
```

whenever these four limsups are finite. If all four vanish, then
`T_11^{SEL0}=0`; otherwise the displayed sum is the evaluated reduced
`T_11` ceiling.

Second,

```math
T_{12}^{SEL0}
:=
A_{12}^{per,SEL0}
+A_{12}^{cusp,SEL0}
+A_{12}^{smear,SEL0}
+A_{12}^{app,SEL0},
```

where the four entries are exactly the reduced loop-continuity limsups

```math
A_{12}^{per,SEL0}
=
\limsup_j\sum_{k\ge j}\eta_{perLC,j,k},
\qquad
A_{12}^{cusp,SEL0}
=
\limsup_j\sum_{k\ge j}\eta_{cuspLC,j,k},
```

```math
A_{12}^{smear,SEL0}
=
\limsup_j\sum_{k\ge j}\eta_{smearLC,j,k},
```

and

```math
A_{12}^{app,SEL0}
=
\limsup_j\sum_{k\ge j}
\left(
\eta_{P12,j,k}
+\eta_{appLC,j,k}^{(12)}
+\eta_{binLC,j,k}^{(12)}
\right).
```

Projective, regulator, and finite-volume loop-continuity terms are not in
`T_12`; they remain charged to `T_11` or `T_14`.

Third, the Paper-14 whole-process finite-block ceiling is

```math
T_{14}^{SEL0}:=E_{14}^{SEL0},
\qquad
E_{14}^{SEL0}
:=
\limsup_j\|E_{14}(\eta_j)\|_{tr},
```

provided the Paper-14 export chain is evaluated on the same `SEL0` batteries
and the displayed limsup is finite.

Finally, define the `SEL0` surface-entry constants

```math
h_{13}^{SEL0}:=3+\log 20,
\qquad
d_{13}^{SEL0}
:=
C_\xi^{SEL0}{1+\eta_{19}^{res}\over1-\eta_{19}^{res}},
```

using the reduced 4D hypercubic surface template and the area-charged
decoration constant. If the orientation-doubled fallback is used, replace
`3+\log 20` by `3+\log 40`.

For a proposed leading central-character rate `kappa_13^*`, set

```math
\mu_{13}^{SEL0}(\kappa_{13}^*)
:=
\kappa_{13}^*
-d_{13}^{SEL0}
-h_{13}^{SEL0}.
```

If `mu_13^SEL0(kappa_13^*)>0`, the Paper-19 surface-polymer source gives, for
every

```math
q_{13}^*\in
\left(
\exp[-\mu_{13}^{SEL0}(\kappa_{13}^*)],
1
\right),
```

the certified ceiling

```math
T_{13}^{SEL0}(q_{13}^*)
:=
M_{13}^{surf,SEL0}{q_{13}^*\over1-q_{13}^*}
+A_{13}^{entry,SEL0}
+A_{13}^{exact,SEL0}.
```

Thus the infimal surface-entry ceiling available from this route is

```math
T_{13}^{SEL0,opt}(\kappa_{13}^*)
:=
M_{13}^{surf,SEL0}
{\exp[-\mu_{13}^{SEL0}(\kappa_{13}^*)]
\over
1-\exp[-\mu_{13}^{SEL0}(\kappa_{13}^*)]}
+A_{13}^{entry,SEL0}
+A_{13}^{exact,SEL0}.
```

The word `infimal` matters: Paper 19 certifies any slightly larger value by
choosing `q_13^*` strictly above `exp[-mu_13^SEL0]`. Because the final
comparison is strict, this infimal form is the sharp pass/fail threshold for
the component route.

### Definition 4.3A: Signed Margin Tests For `SEL0`

The residual transport margin has already been computed in Definition 3.6.
For the purpose of checking signs after the linear transport ceilings are
evaluated, define the non-surface debit

```math
L_{pre13}^{SEL0}
:=
T_{11}^{SEL0}
+T_{12}^{SEL0}
+T_{14}^{SEL0}
+A_{13}^{entry,SEL0}
+A_{13}^{exact,SEL0}.
```

Then

```math
M_{pre13}^{SEL0}
=
M_{loss}^{SEL0}-L_{pre13}^{SEL0}.
```

Let

```math
\Lambda_{dec}^{SEL0}
:=
{1+\eta_{19}^{res}\over1-\eta_{19}^{res}}.
```

The exact sign tests are:

1. `M_loss^SEL0>0` if and only if

   ```math
   C_{dec}^{SEL0}
   <
   {1\over\Lambda_{dec}^{SEL0}}
   \log(1+Sig_{AFM}^{SEL0}).
   ```

2. `M_pre13^SEL0>0` if and only if both

   ```math
   L_{pre13}^{SEL0}<Sig_{AFM}^{SEL0}
   ```

   and

   ```math
   C_{dec}^{SEL0}
   <
   {1\over\Lambda_{dec}^{SEL0}}
   \log(1+Sig_{AFM}^{SEL0}-L_{pre13}^{SEL0})
   ```

   hold.

Therefore the current branch is numerically signed only after the source
papers supply finite values for `C_dec^SEL0`, `eta_19^res`, the three linear
ceilings, and the entry/exact `T_13` debits. Until then the sign is reduced to
the two displayed scalar inequalities.

### Theorem 4.3A.1: Sharp Source-Bound Sign Decision

Let

```math
0\le \underline\eta\le \eta_{19}^{res}\le \overline\eta<1,
\qquad
0\le \underline C\le C_{dec}^{SEL0}\le \overline C,
```

and

```math
0\le \underline L\le L_{pre13}^{SEL0}\le \overline L.
```

Define

```math
\Theta(S,\eta,L)
:=
{1-\eta\over1+\eta}\log(1+S-L),
```

for `0<=L<S`. Then:

1. `M_loss^SEL0>0` is certified by the source upper bounds if

   ```math
   \overline C
   <
   \Theta(Sig_{AFM}^{SEL0},\overline\eta,0).
   ```

2. `M_loss^SEL0<=0` is certified by source lower bounds if

   ```math
   \underline C
   \ge
   \Theta(Sig_{AFM}^{SEL0},\underline\eta,0).
   ```

3. `M_pre13^SEL0>0` is certified by the source upper bounds if

   ```math
   \overline L<Sig_{AFM}^{SEL0}
   ```

   and

   ```math
   \overline C
   <
   \Theta(Sig_{AFM}^{SEL0},\overline\eta,\overline L).
   ```

4. `M_pre13^SEL0<=0` is certified by source lower bounds if either

   ```math
   \underline L\ge Sig_{AFM}^{SEL0}
   ```

   or, when `\underline L<Sig_AFM^{SEL0}`,

   ```math
   \underline C
   \ge
   \Theta(Sig_{AFM}^{SEL0},\underline\eta,\underline L).
   ```

Proof.

The function `Theta(S,eta,L)` is decreasing in `eta` and decreasing in `L` on
`0<=eta<1`, `0<=L<S`. The sign tests in Definition 4.3A are exactly

```math
C_{dec}^{SEL0}<\Theta(Sig_{AFM}^{SEL0},\eta_{19}^{res},0)
```

for `M_loss^SEL0>0`, and

```math
L_{pre13}^{SEL0}<Sig_{AFM}^{SEL0},
\qquad
C_{dec}^{SEL0}
<
\Theta(Sig_{AFM}^{SEL0},\eta_{19}^{res},L_{pre13}^{SEL0})
```

for `M_pre13^SEL0>0`. Monotonicity gives the upper-bound certification
clauses and the lower-bound obstruction clauses. `square`

### Corollary 4.3A.2: Universal `log 2` Decoration Obstruction

On `P20-SEL0-LOSS`,

```math
0<Sig_{AFM}^{SEL0}<1.
```

Consequently, a necessary condition for `M_loss^SEL0>0` is

```math
C_{dec}^{SEL0}
<
\log 2.
```

More sharply,

```math
C_{dec}^{SEL0}
<
{1-\eta_{19}^{res}\over1+\eta_{19}^{res}}
\log(1+Sig_{AFM}^{SEL0}).
```

Likewise, a necessary condition for `M_pre13^SEL0>0` is

```math
L_{pre13}^{SEL0}<Sig_{AFM}^{SEL0},
```

and

```math
C_{dec}^{SEL0}
<
{1-\eta_{19}^{res}\over1+\eta_{19}^{res}}
\log(1+Sig_{AFM}^{SEL0}-L_{pre13}^{SEL0})
<
\log 2.
```

Therefore, if the finite-template decoration audit on the chosen normalization
proves `C_dec^SEL0>=log 2`, this `SEL0` component route fails before the
surface-polymer rate is tested.

Proof.

Definition 3A.3 gives `Sig_AFM^SEL0>0`; both factors in its formula are
strictly below one, so `Sig_AFM^SEL0<1`. The displayed necessary conditions are
Definition 4.3A and the inequalities

```math
{1-\eta_{19}^{res}\over1+\eta_{19}^{res}}\le1,
\qquad
\log(1+Sig_{AFM}^{SEL0})<\log2,
```

and similarly after subtracting `L_pre13^SEL0`. `square`

### Corollary 4.3A.3: Current Paper-20 Sign Status

Using only the constants already exported by Papers 16--19, the sharpest
available upper-bound certification is obtained by setting

```math
\overline\eta
:=
\eta_{19}^{res}
=
{C_{KP}A_{res}e^{-\Delta_{19}^{an}r_{res}}
\over
1-e^{-\Delta_{19}^{an}}},
\qquad
\Delta_{19}^{an}=\mu_{res}-h_{KP}-m>0,
```

```math
\overline C
:=
C_\xi^{SEL0}+C_{\xi'}^{SEL0},
```

and

```math
\overline L
:=
T_{11}^{SEL0}
+T_{12}^{SEL0}
+T_{14}^{SEL0}
+A_{13}^{entry,SEL0}
+A_{13}^{exact,SEL0}.
```

The current source papers therefore decide the signs exactly when these
quantities satisfy the inequalities of Theorem 4.3A.1. If the inequalities do
not pass and no matching lower bounds are supplied, the status is undecided,
not falsified.

At the present level of the written source papers, `eta_19^res` is formulaic,
`C_xi^SEL0+C_xip^SEL0` is finite-template but not numerically minimized, and
`\overline L` is a sum of same-record limsup transport constants. Thus the
papers have reduced the sign decision to explicit scalar constants, but they
have not yet numerically certified `M_loss^SEL0>0` or `M_pre13^SEL0>0`.

Proof.

The formula for `eta_19^res` is the Paper-19 import of Paper-16 Theorem
9N.2A. The value of `overline C` is Corollary 8L.9C.1 of Paper 19 on the
centered square branch. The value of `overline L` is Definition 4.3A. Applying
Theorem 4.3A.1 gives the exact decision criterion. The final statement is an
inventory claim: the cited papers provide these formulaic ceilings, not
numerical values or lower bounds sharp enough to force either sign. `square`

### Theorem 4.3A.4: Exhausted Sharp Source-Constant Bound

For the clean matched-time `SEL0` branch, define the two exact thresholds

```math
U_{loss}^{SEL0}
:=
{1-\eta_{19}^{res}\over1+\eta_{19}^{res}}
\log(1+Sig_{AFM}^{SEL0}),
```

and, whenever `L_pre13^SEL0<Sig_AFM^SEL0`,

```math
U_{pre13}^{SEL0}
:=
{1-\eta_{19}^{res}\over1+\eta_{19}^{res}}
\log(1+Sig_{AFM}^{SEL0}-L_{pre13}^{SEL0}).
```

Then the sharp source-constant decisions are:

1. `M_loss^SEL0>0` if and only if

   ```math
   C_\xi^{SEL0}+C_{\xi'}^{SEL0}<U_{loss}^{SEL0}.
   ```

2. `M_loss^SEL0<=0` if and only if

   ```math
   C_\xi^{SEL0}+C_{\xi'}^{SEL0}\ge U_{loss}^{SEL0}.
   ```

3. `M_pre13^SEL0>0` if and only if

   ```math
   L_{pre13}^{SEL0}<Sig_{AFM}^{SEL0}
   ```

   and

   ```math
   C_\xi^{SEL0}+C_{\xi'}^{SEL0}<U_{pre13}^{SEL0}.
   ```

4. `M_pre13^SEL0<=0` if and only if either

   ```math
   L_{pre13}^{SEL0}\ge Sig_{AFM}^{SEL0}
   ```

   or

   ```math
   C_\xi^{SEL0}+C_{\xi'}^{SEL0}\ge U_{pre13}^{SEL0}.
   ```

Consequently the current written source papers do not yet decide either sign.
They prove the analytic form of `eta_19^res`, finite-template existence of
`C_xi^SEL0+C_xip^SEL0`, and same-record limsup formulas for
`L_pre13^SEL0`; they do not provide a numerical finite-template upper bound
below `U_loss^SEL0` or `U_pre13^SEL0`, nor a lower bound above those thresholds.
The sharp universal warning remains:

```math
C_\xi^{SEL0}+C_{\xi'}^{SEL0}\ge\log2
\quad\Longrightarrow\quad
M_{loss}^{SEL0}\le0
\quad\Longrightarrow\quad
M_{pre13}^{SEL0}\le0.
```

Proof.

The identities are Definition 4.3A with
`C_dec^SEL0=C_xi^SEL0+C_xip^SEL0`. Corollary 4.3A.2 gives the `log2`
obstruction because `U_loss^SEL0<log2` and
`U_pre13^SEL0<log2` whenever the latter is defined. The last paragraph is a
source inventory: Paper 19 Lemma 8L.9A.1 supplies only finite template
constants, and Paper 19/Paper 16 supply only the displayed residual and
transport formulas unless additional numerical source estimates are proved.
`square`

### Theorem 4.3A.5: Decoration Bottleneck Decision Attempt

For the frozen `P20-SEL0` selector, let

```math
C_{dec,act}^{SEL0}
:=
\limsup_j\left(c_{\xi,j}^*+c_{\xi',j}^*\right)
```

be the actual Paper-15 decoration constant of the declared centered-square
finite template, evaluated on the same pushed-forward record law and same
cofinal battery. Paper 19 currently proves only

```math
C_{dec,act}^{SEL0}
\le
C_\xi^{SEL0}+C_{\xi'}^{SEL0}
<\infty.
```

Thus the decoration bottleneck is decided exactly as follows:

1. the frozen `SEL0` decoration route passes the pre-transport bottleneck iff

   ```math
   C_{dec,act}^{SEL0}<U_{loss}^{SEL0};
   ```

2. it fails before transport iff

   ```math
   C_{dec,act}^{SEL0}\ge U_{loss}^{SEL0};
   ```

3. the current written source papers do not compute `C_dec,act^SEL0`, because
   Paper 19 Lemma 8L.9A.1 names the finite local template types but does not
   give their exact unit-cell collar counts.

Consequently, the strongest unconditional statement available from the present
text is an undecided exact scalar bottleneck:

```math
C_{dec,act}^{SEL0}
\ ?\
{1-\eta_{19}^{res}\over1+\eta_{19}^{res}}
\log(1+Sig_{AFM}^{SEL0}).
```

There is, however, an immediate conditional failure test. If the fixed
block/collar convention is normalized so that every nonempty area-charged
collar cell or endpoint/corner collar cell contributes at least one unit to the
Paper-15 constants, and if the centered-square Creutz template contains such a
nonempty collar cofinally, then

```math
C_{dec,act}^{SEL0}\ge1>\log2>U_{loss}^{SEL0},
```

so `M_loss^SEL0<=0`; this `SEL0` route is dead before any transport or
surface-polymer estimate is tested.

Proof.

Paper 15 Definition 9A.1 gives
`c_Delta,j^*=c_xi,j^*+c_xip,j^*`. Paper 19 Definition 8L.9A and Lemma 8L.9A.1
prove only a uniform finite-template ceiling for the centered-square branch.
Substituting the actual limsup in Definition 3.6 gives the exact iff
conditions. The conditional failure test follows from Corollary 4.3A.2, since
`U_loss^SEL0<log2<1`. The nonempty-collar premise is a genuine extra
finite-template enumeration, not a consequence of the current written source
papers. `square`

### Definition 4.3A.6: Unit-Collar Template Enumeration

`P20-SEL0-UCOL` is the finite collar enumeration for the centered-square
`SEL0` Creutz template under the standard Paper-15 unit-counting convention.
It consists of the following clauses.

1. On a cofinal tail,

   ```math
   R_j=T_j=L_j,
   \qquad
   1\le\sigma_j<L_j.
   ```

2. The four Creutz slots are

   ```math
   C_{++}=(L_j,L_j),
   \quad
   C_{--}=(L_j-\sigma_j,L_j-\sigma_j),
   ```

   ```math
   C_{-+}=(L_j-\sigma_j,L_j),
   \quad
   C_{+-}=(L_j,L_j-\sigma_j).
   ```

3. Each slot is a nondegenerate lattice rectangle and therefore has four
   convex corner collar templates. Across the four slots there are sixteen
   convex corner occurrences before quotienting by translation, reflection,
   or record-label symmetries.

4. After quotienting by those symmetries, the local template list is

   ```text
   straight edge,
   interior plaquette collar,
   convex corner,
   Creutz-overlap concave corner,
   endpoint/corner collar.
   ```

5. The unit-counting convention means that each nonempty endpoint/corner
   collar template contributes at least one unit to the Paper-15 `c'_{C,j}`
   constant, and each nonempty area-charged collar template contributes at
   least one unit to the Paper-15 `c_{C,j}` constant. No geometric surface is
   being exported as ontology; these are finite proof-coordinate labels for
   the pushed-forward scalar record battery.

### Lemma 4.3A.7: Centered-Square Creutz Slots Have Nonempty Unit Collars

Assume `P20-SEL0-UCOL`. Then, on a cofinal tail,

```math
c_{\xi',j}^*\ge1,
\qquad
c_{\xi,j}^*+c_{\xi',j}^*\ge1.
```

Consequently

```math
C_{dec,act}^{SEL0}
=
\limsup_j(c_{\xi,j}^*+c_{\xi',j}^*)
\ge1.
```

Proof.

For `j` on the cofinal tail, `1<=sigma_j<L_j`, so all four slots in Definition
4.3A.6 are nondegenerate rectangles. In particular, the slot
`C_{++}=(L_j,L_j)` has four convex corners. The unit-counting convention
assigns at least one endpoint/corner collar unit to a nonempty corner template.
Therefore `c'_{C_{++},j}>=1`. Since Paper 15 Definition 9A.1 defines
`c_xip,j^*` as the maximum of `c'_{C,j}` over the finite Creutz battery,
`c_xip,j^*>=1`. The constants are nonnegative, so
`c_xi,j^*+c_xip,j^*>=1`. Taking the limsup proves the final claim. `square`

### Theorem 4.3A.8: Unit-Collar Enumeration Falsifies The `SEL0` Decoration Bottleneck

Assume `P20-SEL0-UCOL`. Then

```math
C_{dec,act}^{SEL0}\ge1>\log2>U_{loss}^{SEL0}.
```

Hence

```math
M_{loss}^{SEL0}\le0.
```

Therefore the clean matched-time centered-square `SEL0` component route cannot
prove `P20-LOSS-PASS`; it fails before any `T_11`, `T_12`, `T_13`, or `T_14`
transport debit is charged.

Proof.

Lemma 4.3A.7 gives `C_dec,act^SEL0>=1`. Corollary 4.3A.2 gives
`U_loss^SEL0<log2`, and `log2<1`. Therefore
`C_dec,act^SEL0>U_loss^SEL0`. The exact decision theorem, Theorem 4.3A.5,
then gives `M_loss^SEL0<=0`. The final statement is Theorem 3.7: if the
decoration-only margin is nonpositive, the component-source route cannot close
the loss inequality even with zero transport debit. `square`

### Corollary 4.3A.9: Retiring The Standard Unit-Collar `SEL0` Branch

Under the standard Paper-15 unit-counting collar convention `P20-SEL0-UCOL`,
the clean matched-time centered-square `SEL0` branch is retired:

```text
P20-SEL0-UCOL
=> M_loss^SEL0<=0
=> no P20-LOSS-PASS proof on this frozen branch.
```

Therefore no later Paper-20 closure argument may continue to use
`T_11^{SEL0}`, `T_12^{SEL0}`, `T_13^{SEL0}`, or `T_14^{SEL0}` as though they
could still fit under a positive residual margin. The already-defined `SEL0`
transport ceilings may remain as diagnostic records for the failed branch, but
any continuation toward closure must declare a new frozen selector, re-run
`P20-NOSMUGGLE`, and recompute the same-record source constants.

Proof.

This is Theorem 4.3A.8 plus Theorem 3.7. The last sentence is the frozen
selector rule of Definition 1.3. `square`

### Theorem 4.3A.10: Exact `SEL1` Decoration Bottleneck

For the replacement selector `P20-SEL1`, set

```math
U_{loss}^{SEL1}
:=
{1-\eta_{19}^{res}\over1+\eta_{19}^{res}}
\log(1+Sig_{AFM}^{SEL1}),
```

and define the actual area-charged finite-template constant

```math
C_{dec,act}^{SEL1}
:=
\limsup_j c_{\xi,j}^{*,SEL1}.
```

With the canonical half-margin character-tail choice, define

```math
D_{dec}^{SEL1}
:=
\exp\left(
C_{dec,act}^{SEL1}
{1+\eta_{19}^{res}\over1-\eta_{19}^{res}}
\right)-1,
\qquad
M_{loss}^{SEL1}
:=
Sig_{AFM}^{SEL1}-D_{dec}^{SEL1}.
```

Then

```math
M_{loss}^{SEL1}>0
\quad\Longleftrightarrow\quad
C_{dec,act}^{SEL1}<U_{loss}^{SEL1}.
```

Moreover

```math
U_{loss}^{SEL1}=U_{loss}^{SEL0}<\log2<1.
```

Proof.

Definition 1.7 keeps the same AF row, coefficient closure, character
half-margin, and signal floor as `SEL0`, so
`Sig_AFM^SEL1=Sig_AFM^SEL0` and `eta_*=(1+eta_19^res)/2`. It changes only the
decoration bookkeeping:

```math
C_{dec}^{SEL1}=C_\xi^{SEL1},
\qquad
C_{\xi'}^{SEL1}=0
```

as a debit-assignment convention, with endpoint/corner collars moved to
`E_corn^{SEL1}`. Therefore the same algebra as Theorem 4.3A.4 gives the exact
iff with `C_dec,act^SEL1` in place of
`C_xi^SEL0+C_xip^SEL0`. The equality of thresholds follows from
`Sig_AFM^SEL1=Sig_AFM^SEL0`, and the strict bound
`U_loss^SEL0<log2<1` is Corollary 4.3A.2. `square`

### Definition 4.3A.11: `SEL1` Area-Collar Enumeration

`P20-SEL1-ACOL` is the finite area-collar enumeration for the
corner-separated `SEL1` template. It consists of:

1. the `P20-SEL1` centered-square schedule

   ```math
   R_j=T_j=L_j,
   \qquad
   \sigma_j=\lfloor\alpha L_j\rfloor,
   \qquad
   0<\alpha<1;
   ```

2. the four Creutz slots of Definition 4.3A.6;
3. the same local template list as Definition 4.3A.6, but with endpoint/corner
   templates excluded from the multiplicative decoration register and charged
   instead to `E_corn^{SEL1}`;
4. the standard Paper-15 unit area-collar convention: every nonempty
   area-charged plaquette-collar template contributes at least one unit to
   `c_{C,j}` and hence to the maximum `c_{\xi,j}^{*,SEL1}`;
5. the finite Creutz battery includes the standard unit interior-plaquette
   nonminimal deformation whenever a slot contains an interior plaquette. This
   is the ordinary Paper-13/Paper-15 area-collar source; omitting it would be a
   different frozen selector and would require a new no-smuggling audit.

### Lemma 4.3A.12: `SEL1` Has A Nonempty Area-Charged Collar Cofinally

Assume `P20-SEL1-ACOL`. Then, on a cofinal tail,

```math
c_{\xi,j}^{*,SEL1}\ge1,
\qquad
C_{dec,act}^{SEL1}\ge1.
```

Proof.

Since `0<alpha<1`, both `L_j` and `L_j-\sigma_j` tend to infinity along the
cofinal tail. After passing to a tail, the slot

```math
C_{--}=(L_j-\sigma_j,L_j-\sigma_j)
```

contains an interior plaquette. By Definition 4.3A.11 clause 5, the finite
Creutz battery contains the local one-plaquette nonminimal deformation at such
an interior plaquette. Its collar is an area-charged plaquette-collar template:
it is not an endpoint or corner term, and its count is per excess plaquette.
By Definition 4.3A.11 clause 4, this nonempty area-charged template contributes
at least one unit to `c_{C_{--},j}`. Taking the maximum over the finite Creutz
battery gives `c_{\xi,j}^{*,SEL1}\ge1`. The limsup gives
`C_dec,act^SEL1>=1`. `square`

### Theorem 4.3A.13: Standard Area-Collar `SEL1` Falsifies The Decoration Inequality

Assume `P20-SEL1-ACOL`. Then the `SEL1` decoration inequality is false:

```math
C_{dec,act}^{SEL1}
\ge
1
>
\log2
>
U_{loss}^{SEL1}.
```

Consequently

```math
M_{loss}^{SEL1}\le0.
```

Thus the corner-separated `SEL1` branch with the standard Paper-15 unit
area-collar convention cannot prove `P20-LOSS-PASS`; it fails before
endpoint/corner transport `E_corn^{SEL1}`, before the linear transport buckets,
and before the `T_13` surface-rate test.

Proof.

Lemma 4.3A.12 gives `C_dec,act^SEL1>=1`. Theorem 4.3A.10 gives
`U_loss^SEL1<log2<1`. Therefore
`C_dec,act^SEL1>U_loss^SEL1`, so the exact iff in Theorem 4.3A.10 gives
`M_loss^SEL1<=0`. Since all later transport ceilings are nonnegative debits,
the same argument as Theorem 3.7 shows that no later `T_11`, `T_12`, `T_13`, or
`T_14` estimate can restore the strict loss inequality on this frozen selector.
`square`

### Corollary 4.3A.14: Standard-Selector Failure Ledger

The two standard finite-template branches tested so far fail at the
decoration-only loss gate:

```text
SEL0 + standard unit endpoint/corner collar counting:
  C_dec,act^SEL0 >= 1 > log 2 > U_loss^SEL0
  => M_loss^SEL0 <= 0.

SEL1 + standard unit area-collar counting:
  C_dec,act^SEL1 >= 1 > log 2 > U_loss^SEL1
  => M_loss^SEL1 <= 0.
```

Thus neither standard branch can prove `P20-LOSS-PASS`, regardless of the later
transport or surface-rate estimates. This is not a contradiction with Paper 19
and is not a falsification of confinement. It is a falsification of the
standard unit-counted finite-template direct-witness loss route on these frozen
selectors.

Proof.

The first implication is Theorem 4.3A.8. The second is Theorem 4.3A.13. Both
failures occur before any transport debit is charged, so later nonnegative
transport estimates cannot restore the strict scalar loss inequality. `square`

### Definition 4.3A.15: Viable Replacement Selector Test `P20-SEL2-ADMISS`

A further replacement selector `P20-SEL2` is admissible only if it is declared
before any favorable inequality is used and satisfies the following clauses.

1. **Frozen tower.** It supplies a full `P20-FROZEN-SEL` instance: one AF row,
   one cofinal subsequence, one representation channel, one window schedule, one
   character cutoff, one counterterm convention, and one pushed-forward scalar
   record law.
2. **No-smuggling.** It proves `P20-NOSMUGGLE`: the selector may not assume
   `R_H^opt<R_H^crit`, `L_AFM^sharp<Sig_AFM`, a Wilson-loop area law, a mass
   gap, or continuum `4D SU(N)` Yang-Mills existence.
3. **Coefficient accountability.** If it changes the coefficient branch, it must
   re-prove `P20-COEFF-PASS`; if it keeps the clean matched-time coefficient
   branch, it must explicitly import the same coefficient closure without
   changing the loss-side record law.
4. **Decoration accountability.** It must define an actual same-record
   multiplicative decoration constant

   ```math
   C_{dec,act}^{SEL2}
   ```

   from the finite-battery decoration partition functions. This constant may be
   smaller than the unit-counted collar constant only if a genuine scalar
   estimate, cancellation, normalization, or improved KP bound proves it.
   Renaming a unit-counted collar as transport is not enough.
5. **Disjoint debit register.** Every endpoint/corner, area-collar,
   projective/regulator, loop-readout, volume, and surface-entry effect is
   charged exactly once.
6. **Activity choice.** It must declare a character-tail budget
   `eta_{ch}^{SEL2}>0`, prove `P19-CHTAIL-AUDIT(eta_ch^{SEL2})` on the same
   record law, and set

   ```math
   \eta_*^{SEL2}:=\eta_{19}^{res}+\eta_{ch}^{SEL2}<1.
   ```

   The canonical half-margin is optional, not mandatory.
7. **Strict pre-transport pass test.** It must prove

   ```math
   C_{dec,act}^{SEL2}
   <
   U_{loss}^{SEL2}
   :=
   {1-\eta_*^{SEL2}\over\eta_*^{SEL2}}
   \log(1+Sig_{AFM}^{SEL2}).
   ```

If clause 7 fails, the selector is dead before transport.

### Theorem 4.3A.16: Variable-Activity Decoration Gate For `SEL2`

Assume `P20-SEL2-ADMISS`. Set

```math
L_{sig}^{SEL2}:=\log(1+Sig_{AFM}^{SEL2}),
\qquad
\eta_*:=\eta_*^{SEL2},
\qquad
C:=C_{dec,act}^{SEL2}.
```

Then the decoration-only margin is positive exactly when

```math
C
<
{1-\eta_*\over\eta_*}
L_{sig}^{SEL2},
```

equivalently

```math
\eta_*
<
{L_{sig}^{SEL2}\over C+L_{sig}^{SEL2}}.
```

Consequently, if the selector retains a nonempty unit-counted multiplicative
collar contribution `C>=1`, then a necessary condition for the route not to die
before transport is

```math
\eta_{19}^{res}
<
{L_{sig}^{SEL2}\over1+L_{sig}^{SEL2}}.
```

If instead

```math
\eta_{19}^{res}
\ge
{L_{sig}^{SEL2}\over1+L_{sig}^{SEL2}},
```

then every unit-counted finite-template `SEL2` branch fails before transport,
regardless of how sharply the non-leading character cutoff is chosen.

Proof.

The decoration debit on the declared selector is

```math
D_{dec}^{SEL2}
=
\exp\left({C\eta_*\over1-\eta_*}\right)-1.
```

The pre-transport loss margin is positive exactly when
`D_dec^SEL2<Sig_AFM^SEL2`, i.e.

```math
{C\eta_*\over1-\eta_*}
<
\log(1+Sig_{AFM}^{SEL2})=L_{sig}^{SEL2}.
```

Solving first for `C` and then for `eta_*` gives the two equivalent displayed
criteria. Since `eta_* = eta_19^res+eta_ch^SEL2` and
`eta_ch^SEL2>0`, any branch with `C>=1` requires
`eta_19^res<L_sig/(1+L_sig)`. If the residual activity is at least that
threshold, no positive character-tail choice can make `eta_*` small enough.
`square`

### Corollary 4.3A.17: Character-Tail Optimization Is Available Once The Residual Gate Passes

Assume the clean Paper-19 character-tail theorem, Theorem 8L.8A, on the same
pushed-forward record law. If

```math
\eta_{19}^{res}
<
{L_{sig}^{SEL2}\over C_{dec,act}^{SEL2}+L_{sig}^{SEL2}},
```

then there exists a strict character-tail budget `eta_ch^{SEL2}>0` such that

```math
P19\text{-}CHTAIL\text{-}AUDIT(\eta_{ch}^{SEL2})
```

holds and the decoration-only inequality for `SEL2` passes:

```math
C_{dec,act}^{SEL2}
<
{1-\eta_*^{SEL2}\over\eta_*^{SEL2}}
L_{sig}^{SEL2}.
```

Conversely, if

```math
\eta_{19}^{res}
\ge
{L_{sig}^{SEL2}\over C_{dec,act}^{SEL2}+L_{sig}^{SEL2}},
```

then no positive character-tail budget can make the decoration-only inequality
strict for that same `C_dec,act^SEL2` and signal floor.

Proof.

The first displayed strict inequality leaves a positive gap between
`eta_19^res` and `L_sig/(C_dec,act^SEL2+L_sig)`. Choose
`eta_ch^SEL2>0` smaller than that gap and also smaller than
`1-eta_19^res`. Theorem 8L.8A supplies `P19-CHTAIL-AUDIT` for that budget on
the same pushed-forward record law. Theorem 4.3A.16 then gives the strict
decoration pass. The converse is the contrapositive of the same exact
inequality, using `eta_*^SEL2>=eta_19^res`. `square`

### Definition 4.3A.18: Actual Residual-Activity Target For `SEL2`

Let `P20-SEL2-ADMISS` be fixed and set

```math
L:=L_{sig}^{SEL2}=\log(1+Sig_{AFM}^{SEL2}),
\qquad
C:=C_{dec,act}^{SEL2}.
```

The exact residual activity imported from Paper 19 is

```math
\eta_{19}^{res}
=
{C_{KP}A_{res}\exp(-\Delta r_{res})\over1-\exp(-\Delta)},
\qquad
\Delta:=\mu_{res}-h_{KP}-m>0,
```

where all constants are the same-record constants exported by Paper 16 through
`P19-AN-AUDIT(m)`. The residual side of the `SEL2` decoration gate is therefore
the scalar inequality

```math
{C_{KP}A_{res}\exp(-\Delta r_{res})\over1-\exp(-\Delta)}
<
{L\over C+L}.
```

Equivalently, if the logarithm is positive, it is enough and necessary to have

```math
r_{res}
>
{1\over\Delta}
\log\left(
{C_{KP}A_{res}(C+L)\over L(1-\exp(-\Delta))}
\right).
```

If the logarithm is nonpositive, every positive residual starting range passes
this residual-only gate.

For an available upper bound `C_dec,act^SEL2<=C_U`, define

```math
\tau_U^{SEL2}
:=
{L\over C_U+L}.
```

Then the stronger source inequality

```math
\eta_{19}^{res}<\tau_U^{SEL2}
```

is sufficient for every `SEL2` decoration template whose actual same-record
constant is at most `C_U`.

### Theorem 4.3A.19: Paper-16 Clean Residual Bound For The `SEL2` Gate

Assume the Paper-19 analytic import is sourced by the clean finite-range
Paper-16 branch of Theorem 9N.1Q.1 on the same pushed-forward record law. Fix
an admissible upper bound `C_dec,act^SEL2<=C_U<\infty`, and put

```math
\tau_U^{SEL2}:={L_{sig}^{SEL2}\over C_U+L_{sig}^{SEL2}}.
```

If there is a finite-range margin `delta>0` such that the large-field source
is available with

```math
\sigma_{lf}^{sharp}\ge h_{KP}+m+\delta
```

and

```math
2C_{KP}{\exp(-\delta r_{res}^{clean})\over1-\exp(-\delta)}
<
\tau_U^{SEL2},
```

then, after restricting to a sufficiently fine AF tail, the imported residual
activity satisfies

```math
\eta_{19}^{res}
\le
2C_{KP}{\exp(-\delta r_{res}^{clean})\over1-\exp(-\delta)}
<
\tau_U^{SEL2}.
```

Consequently the residual side of the `SEL2` variable-activity decoration gate
passes for every selector with `C_dec,act^SEL2<=C_U`.

Proof.

Paper 16 Theorem 9N.1Q.1 evaluates the clean residual activity as

```math
\eta_\delta(g_*)
=
C_{KP}A_\delta(g_*)
{\exp(-\delta r_{res}^{clean})\over1-\exp(-\delta)}
```

with

```math
A_\delta(g_*)
=
1+
{C_v^{row}C_0\exp(2R_G(h_{KP}+m+\delta))C_{ent}g_*^2
\over
1-\theta_\delta(g_*)}.
```

The same theorem gives an AF-tail restriction for which
`\theta_\delta(g_*)<=1/2` and `A_delta(g_*)<=2`. Substitution gives the
displayed upper bound for `eta_19^res`, because this is exactly the Paper-19
name for the same-record residual activity after `P19-AN-AUDIT(m)`.
The final implication is Definition 4.3A.18. `square`

### Definition 4.3A.20: Same-Record Decoration-Constant Audit `P20-SEL2-CDEC-BOUND(C_U,C_L)`

For a declared `SEL2`, `P20-SEL2-CDEC-BOUND(C_U,C_L)` is the finite-template
audit which proves, on the same pushed-forward record law,

```math
0\le C_L\le C_{dec,act}^{SEL2}\le C_U<\infty.
```

The audit must exhibit a finite list of multiplicative decoration template
types `\mathcal D_{SEL2}` and nonnegative template weights `w_\tau` such that
the rowwise decoration constant is bounded by

```math
C_{dec,j}^{SEL2}
\le
\sum_{\tau\in\mathcal D_{SEL2}}N_{\tau,j}w_\tau,
```

and

```math
C_U
\ge
\limsup_j
\sum_{\tau\in\mathcal D_{SEL2}}N_{\tau,j}w_\tau.
```

Every template in `\mathcal D_{SEL2}` must be disjoint from the effects already
charged to `T_11`, `T_12`, `T_13`, or `T_14`. If a nonempty unit-counted
collar remains in the multiplicative decoration register, the audit must also
record the lower bound `C_L>=1`.

This definition is deliberately finite and combinatorial. It does not allow a
smaller `C_U` merely by changing names; a smaller upper bound must come from an
actual scalar estimate, cancellation, normalization, or improved KP activity
bound on the declared record law.

### Theorem 4.3A.21: Combined `SEL2` Residual-Decoration Pass/Falsifier

Assume `P20-SEL2-ADMISS` and `P20-SEL2-CDEC-BOUND(C_U,C_L)`.

If

```math
\eta_{19}^{res}
<
{L_{sig}^{SEL2}\over C_U+L_{sig}^{SEL2}},
```

then there exists a strict character-tail budget `eta_ch^{SEL2}>0` such that
`P19-CHTAIL-AUDIT(eta_ch^{SEL2})` holds and the `SEL2` decoration-only gate
passes.

If instead

```math
\eta_{19}^{res}
\ge
{L_{sig}^{SEL2}\over C_L+L_{sig}^{SEL2}},
```

then every `SEL2` branch satisfying the lower bound
`C_dec,act^SEL2>=C_L` fails the decoration-only gate, regardless of how sharply
the character tail is cut.

Proof.

The upper-bound statement follows because

```math
{L_{sig}^{SEL2}\over C_U+L_{sig}^{SEL2}}
\le
{L_{sig}^{SEL2}\over C_{dec,act}^{SEL2}+L_{sig}^{SEL2}},
```

so Corollary 4.3A.17 applies. The lower-bound statement follows from

```math
{L_{sig}^{SEL2}\over C_{dec,act}^{SEL2}+L_{sig}^{SEL2}}
\le
{L_{sig}^{SEL2}\over C_L+L_{sig}^{SEL2}},
```

and the converse clause of Corollary 4.3A.17. `square`

### Corollary 4.3A.22: Unit-Template `SEL2` Scalar Target

Suppose a later selector proves

```math
P20\text{-}SEL2\text{-}CDEC\text{-}BOUND(1,1).
```

Then the decoration-only route is alive exactly on the residual side when

```math
\eta_{19}^{res}
<
{L_{sig}^{SEL2}\over1+L_{sig}^{SEL2}}.
```

On the clean Paper-16 residual branch, a sufficient same-record source test is
the existence of `delta>0` with the large-field source available at
`h_KP+m+delta` and

```math
2C_{KP}{\exp(-\delta r_{res}^{clean})\over1-\exp(-\delta)}
<
{L_{sig}^{SEL2}\over1+L_{sig}^{SEL2}}.
```

Proof.

The exact unit-template threshold is Theorem 4.3A.21 with `C_U=C_L=1`.
The clean sufficient test is Theorem 4.3A.19 with the same upper bound. `square`

### Definition 4.3A.23: `SEL2` Area-Collar Enumeration `P20-SEL2-ACOL(C_area)`

`P20-SEL2-ACOL(C_area)` is the finite same-record enumeration of the
multiplicative area-collar register for the activity-optimized selector of
Definition 1.10. It consists of the following clauses.

1. The geometric window schedule is the centered square schedule

   ```math
   R_j=T_j=L_j,
   \qquad
   \sigma_j=\lfloor\alpha L_j\rfloor,
   \qquad
   0<\alpha<1.
   ```

2. The four Creutz slots are the same four slots listed in Definition 4.3A.6.

3. Endpoint and corner templates are excluded from the multiplicative
   decoration register and charged only in the loop-readout transport debit.

4. The multiplicative decoration register contains exactly the area-charged
   plaquette-collar template types attached to nonminimal excess plaquette
   insertions in the finite Paper-15 battery. Let this finite list be
   `\mathcal D_{area}^{SEL2}`.

5. For each template `tau in \mathcal D_{area}^{SEL2}`, let `w_tau>=0` be the
   scalar Paper-15 activity weight assigned to one occurrence of that template,
   after pushforward to the same scalar record law. Let `N_{\tau,j}(q)` be the
   maximum number of occurrences of that template created by an excess surface
   with `q` excess plaquettes, divided by `q`.

6. The finite area-collar ceiling is

   ```math
   C_{area}
   \ge
   \limsup_j
   \sum_{\tau\in\mathcal D_{area}^{SEL2}}
   \sup_{q\ge1}N_{\tau,j}(q)w_\tau
   <\infty.
   ```

7. The ordinary unit interior-plaquette nonminimal deformation remains in the
   finite Creutz battery. Thus at least one area-charged plaquette-collar
   occurrence is present cofinally.

This is a finite proof-coordinate enumeration, not an ontic surface
decomposition. It is valid only on the pushed-forward scalar record law fixed
by the selector.

### Lemma 4.3A.24: `SEL2` Area-Collar Enumeration Bounds The Decoration Constant

Assume `P20-SEL2-ACOL(C_area)`. Then

```math
P20\text{-}SEL2\text{-}CDEC\text{-}BOUND(C_{area},1)
```

holds. In particular,

```math
1\le C_{dec,act}^{SEL2}\le C_{area}<\infty.
```

Proof.

By Definition 4.3A.23 clauses 4--6, every multiplicative decoration occurrence
charged to `C_dec,act^SEL2` is one of the finitely many templates in
`\mathcal D_{area}^{SEL2}`, and the per-excess-plaquette limsup of the weighted
template count is bounded by `C_area`. Endpoint and corner terms are excluded
by clause 3, so no endpoint/corner debit is double counted in the
multiplicative constant.

Clause 7 gives a nonempty unit area-collar occurrence cofinally, hence the
standard Paper-15 unit-counting lower bound is `C_dec,act^SEL2>=1`. These are
exactly the upper and lower bounds required by Definition 4.3A.20 with
`C_U=C_area` and `C_L=1`. `square`

### Theorem 4.3A.25: Concrete `SEL2` Decoration Decision With `C_area`

Assume the parametric selector family `P20-SEL2(eta_ch,C_area)` and
`P20-SEL2-ACOL(C_area)` are available on the same record law.

If

```math
\eta_{19}^{res}
<
{L_{sig}^{SEL2}\over C_{area}+L_{sig}^{SEL2}},
```

then a strict character-tail budget can be chosen so that the `SEL2`
decoration-only gate passes on the corresponding frozen instance.

If instead

```math
\eta_{19}^{res}
\ge
{L_{sig}^{SEL2}\over1+L_{sig}^{SEL2}},
```

then the whole `SEL2` family with the standard nonempty unit area-collar lower
bound fails before transport, regardless of the character-tail cutoff.

On the clean Paper-16 residual branch, the first condition is implied by the
existence of `delta>0` with large-field rate at least `h_KP+m+delta` and

```math
2C_{KP}{\exp(-\delta r_{res}^{clean})\over1-\exp(-\delta)}
<
{L_{sig}^{SEL2}\over C_{area}+L_{sig}^{SEL2}}.
```

Proof.

Lemma 4.3A.24 supplies
`P20-SEL2-CDEC-BOUND(C_area,1)`. The first two conclusions are Theorem
4.3A.21 with `C_U=C_area` and `C_L=1`. The clean residual sufficient condition
is Theorem 4.3A.19 with `C_U=C_area`. `square`

### Definition 4.3A.26: Four-Dimensional Area-Collar Weight `w_area^max`

For the `SEL2` finite template list, define the maximal scalar weight of one
area-charged plaquette-collar occurrence by

```math
w_{area}^{max}
:=
\max_{\tau\in\mathcal D_{area}^{SEL2}}w_\tau.
```

Under the standard unit-counted Paper-15 area-collar normalization,
`w_area^max=1`. If a different scalar normalization is used, that normalization
must be declared in the frozen selector and the same-record value of
`w_area^max` must be audited before any pass theorem uses it.

### Lemma 4.3A.27: Sharp 4D Hypercubic Area-Collar Count

In the four-dimensional hypercubic plaquette complex, one plaquette has at most
twenty edge-adjacent plaquette-collar cells. This bound is sharp for an isolated
interior plaquette.

Proof.

Fix an interior plaquette in the coordinate plane `(mu,nu)`. It has four
edges. Consider one of its edges, say an edge parallel to `mu`. In four
dimensions, the plaquettes containing that edge are obtained by choosing one
of the three transverse coordinate directions and one of the two sides in that
direction. Thus there are `2(4-1)=6` plaquettes containing the edge. One of
these six is the original plaquette, leaving five distinct edge-neighbor
plaquettes along that edge. The same count holds for each of the four edges,
so the total number of edge-adjacent plaquette-collar cells is at most
`4*5=20`.

For an isolated interior plaquette all twenty of these edge-neighbor cells are
available as collar cells in the unreduced local template. Hence the upper
bound is sharp before boundary, overlap, or symmetry quotient reductions.
`square`

### Theorem 4.3A.28: Sharp `SEL2` Area-Collar Upper Bound

For the activity-optimized `SEL2` area-collar template of Definition 4.3A.23,
the actual multiplicative decoration constant satisfies

```math
1\le C_{dec,act}^{SEL2}\le 20\,w_{area}^{max}.
```

Equivalently,

```math
P20\text{-}SEL2\text{-}CDEC\text{-}BOUND(20w_{area}^{max},1)
```

holds. Under the standard unit-counted area-collar normalization, this becomes

```math
P20\text{-}SEL2\text{-}CDEC\text{-}BOUND(20,1).
```

Proof.

Definition 4.3A.23 restricts the multiplicative decoration register to
area-charged plaquette-collar cells attached to nonminimal excess plaquettes.
By Lemma 4.3A.27, each added excess plaquette creates at most twenty such
edge-adjacent collar cells in the unreduced four-dimensional hypercubic
template. Boundary contact, sharing between neighboring excess plaquettes, and
record-label quotienting can only reduce this number. Therefore for every
template `tau`,

```math
\sup_{q\ge1}N_{\tau,j}(q)
```

contributes to a total bounded by `20`, and weighting each occurrence by at
most `w_area^max` gives

```math
\limsup_j
\sum_{\tau\in\mathcal D_{area}^{SEL2}}
\sup_{q\ge1}N_{\tau,j}(q)w_\tau
\le
20w_{area}^{max}.
```

Clause 7 of Definition 4.3A.23 gives the lower bound `C_dec,act^SEL2>=1`.
Definition 4.3A.20 then gives the displayed `CDEC` audit. The final statement
is the specialization `w_area^max=1`. `square`

### Corollary 4.3A.29: Concrete Unit-Normalized `SEL2` Residual Test

On the standard unit-counted area-collar branch, the `SEL2` decoration gate is
alive if

```math
\eta_{19}^{res}
<
{L_{sig}^{SEL2}\over20+L_{sig}^{SEL2}}.
```

On the clean Paper-16 residual branch, it is enough to find `delta>0` with
large-field rate at least `h_KP+m+delta` and

```math
2C_{KP}{\exp(-\delta r_{res}^{clean})\over1-\exp(-\delta)}
<
{L_{sig}^{SEL2}\over20+L_{sig}^{SEL2}}.
```

If instead

```math
\eta_{19}^{res}
\ge
{L_{sig}^{SEL2}\over1+L_{sig}^{SEL2}},
```

then even the most favorable standard nonempty unit area-collar branch fails
before transport.

Proof.

Apply Theorem 4.3A.25 with the upper bound `C_area=20` supplied by Theorem
4.3A.28 and the lower bound `1`. `square`

### Definition 4.3A.30: The `C_area=20` Residual Threshold `delta_20`

For the unit-normalized `SEL2` area-collar branch, set

```math
L_{20}:=L_{sig}^{SEL2}=\log(1+Sig_{AFM}^{SEL2})>0,
\qquad
\tau_{20}:={L_{20}\over20+L_{20}}.
```

For the clean Paper-16 residual source with KP counting constant `C_KP` and
starting range `r_res^clean>=1`, define

```math
\delta_{20}^{suff}
:=
\log\left(1+{2C_{KP}\over\tau_{20}}\right)
=
\log\left(1+{2C_{KP}(20+L_{20})\over L_{20}}\right).
```

In the finite-template counting normalization of Paper 16 Corollary 9N.1Q.2,
where `C_KP=1`, this is

```math
\delta_{20}^{suff}
=
\log\left(3+{40\over L_{20}}\right).
```

### Theorem 4.3A.31: The `C_area=20` Residual Inequality Passes Under The Clean Adjustable-Rate Branch

Assume the unit-normalized `SEL2` branch, so `C_area=20`, and assume the clean
Paper-16 residual source hypotheses of Theorem 9N.1Q.1 on the same
pushed-forward record law. If the large-field source is available with

```math
\sigma_{lf}^{sharp}\ge h_{KP}+m+\delta
```

for some

```math
\delta>\delta_{20}^{suff},
```

and the AF tail is restricted as in Paper 16 Theorem 9N.1Q.1 so that
`A_delta(g_*)<=2`, then

```math
2C_{KP}{\exp(-\delta r_{res}^{clean})\over1-\exp(-\delta)}
<
{L_{20}\over20+L_{20}}.
```

Consequently

```math
\eta_{19}^{res}
<
{L_{sig}^{SEL2}\over20+L_{sig}^{SEL2}},
```

so the residual side of the unit-normalized `SEL2` decoration gate passes.

Proof.

Since `r_res^clean>=1`,

```math
{\exp(-\delta r_{res}^{clean})\over1-\exp(-\delta)}
\le
{\exp(-\delta)\over1-\exp(-\delta)}.
```

Let `x=exp(-delta)`. The sufficient inequality

```math
2C_{KP}{x\over1-x}<\tau_{20}
```

is equivalent to

```math
x<{\tau_{20}\over2C_{KP}+\tau_{20}},
```

or

```math
\delta>\log\left(1+{2C_{KP}\over\tau_{20}}\right)
=\delta_{20}^{suff}.
```

Thus every `delta>delta_20^suff` gives the displayed residual estimate. Paper
16 Theorem 9N.1Q.1 then supplies the AF-tail restriction making
`A_delta(g_*)<=2`, so the Paper-19 residual activity obeys the same bound.
Corollary 4.3A.29 gives the final unit-normalized `SEL2` residual gate. `square`

### Corollary 4.3A.32: Exact Status Of The `C_area=20` Residual Test

The scalar residual inequality with `C_area=20` is not an obstruction under
the clean adjustable-rate hypotheses of Paper 16 Theorem 9N.1Q.1: choose any

```math
\delta>\delta_{20}^{suff}
```

and then choose the cofinal AF tail small enough to keep
`theta_delta(g_*)<=1/2` and `A_delta(g_*)<=2`.

If a branch cannot supply the large-field rate

```math
\sigma_{lf}^{sharp}\ge h_{KP}+m+\delta_{20}^{suff}
```

on the same record law, then the failure is not a decoration-counting failure.
It is a failure of the clean Paper-16 large-field/residual source import at the
specific margin required by the unit-normalized `SEL2` loss gate.

Proof.

The pass statement is Theorem 4.3A.31. The obstruction statement is its only
unsupplied source hypothesis after `L_20>0`, `C_KP<infinity`, and
`r_res^clean>=1` are fixed by the clean finite-template row. `square`

### Theorem 4.3A.33: Paper-16 Large-Field Source Supplies The `delta_20` Margin

Assume the following Paper-16 large-field source clauses hold on the same
pushed-forward record law as the `SEL2` decoration ledger:

1. the first five clauses of `HK-LF-SRC(delta_lf,t_L)` from Paper 16 Definition
   9J.1A hold for the selected finite block/collar template and for some fixed
   large-field threshold `0<delta_lf<delta_0`;
2. the collar-adapted finite-energy margin is strict, `c_H>a_ad`;
3. the AF tail may be restricted so that the chosen `t_L` applies cofinally.

Then, for every `epsilon_lf>0`, the large-field source can be run with

```math
\sigma_{lf}^{sharp}
\ge
h_{KP}+m+\delta_{20}^{suff}+\epsilon_{lf}.
```

Consequently the large-field hypothesis of Theorem 4.3A.31 holds with

```math
\delta=\delta_{20}^{suff}+\epsilon_{lf}.
```

Proof.

Set

```math
\delta_{20}(\epsilon_{lf})
:=
\delta_{20}^{suff}+\epsilon_{lf},
```

and choose the desired Paper-16 large-field excess

```math
\xi_{lf}
>
\max\{0,\ h_{KP}+m+\delta_{20}(\epsilon_{lf})-h_{poly}\}.
```

Paper 16 Theorem 9J.1C says that, once the first five clauses of
`HK-LF-SRC` and `c_H>a_ad` are available on the same record law, one may choose
`t_L` small enough that

```math
\sigma_{lf}^{sharp}\ge h_{poly}+\xi_{lf}.
```

By the strict choice of `xi_lf`, this is at least
`h_KP+m+delta_20(epsilon_lf)`. The cofinal AF-tail clause keeps the same
finite-template source valid on the selected tail. Thus Theorem 4.3A.31 applies
with the displayed `delta`. `square`

If any of the three source clauses above fails, Paper 20 has not proved the
large-field input. The failure is a same-record `HK-CAD`/`HK-LF-REP`/AF-tail
source failure, not a failure of the scalar `C_area=20` decoration algebra.

### Definition 4.3A.34: The Actual `SEL2` Character-Tail Budget

Assume the hypotheses of Theorem 4.3A.33 and fix `epsilon_lf>0`. Put

```math
\delta_{20}(\epsilon_{lf})
:=
\delta_{20}^{suff}+\epsilon_{lf},
```

and define the certified residual upper bound

```math
\bar\eta_{res,20}
:=
2C_{KP}
{\exp(-\delta_{20}(\epsilon_{lf})r_{res}^{clean})
\over
1-\exp(-\delta_{20}(\epsilon_{lf}))}.
```

Let

```math
\tau_{20}:={L_{20}\over20+L_{20}}.
```

The `C_area=20` character-tail budget is

```math
\eta_{ch,20}^{SEL2}
:=
{1\over2}\left(\tau_{20}-\bar\eta_{res,20}\right).
```

By Theorems 4.3A.31 and 4.3A.33, `0<eta_ch,20^SEL2`.

### Theorem 4.3A.35: Full `SEL2` Decoration Debit Passes For `C_area=20`

Assume the hypotheses of Theorem 4.3A.33 for some `epsilon_lf>0`, and freeze
the unit-normalized activity-optimized selector

```math
P20\text{-}SEL2(\eta_{ch,20}^{SEL2},20).
```

Assume also the Paper-19 heat-kernel character-tail theorem, Theorem 8L.8A, on
the same pushed-forward record law. Then:

```math
P19\text{-}CHTAIL\text{-}AUDIT(\eta_{ch,20}^{SEL2})
```

holds, and the full pre-transport multiplicative decoration debit satisfies

```math
D_{dec}^{SEL2,20}
:=
\exp\left(
{20\eta_*^{SEL2}\over1-\eta_*^{SEL2}}
\right)-1
<
Sig_{AFM}^{SEL2},
```

where

```math
\eta_*^{SEL2}
:=
\eta_{19}^{res}+\eta_{ch,20}^{SEL2}.
```

Thus the unit-normalized `SEL2` branch passes the full decoration-only gate
before transport.

Proof.

Theorem 4.3A.33 supplies the large-field hypothesis of Theorem 4.3A.31 with
`delta=delta_20(epsilon_lf)`. Hence

```math
\eta_{19}^{res}
\le
\bar\eta_{res,20}
<
\tau_{20}.
```

Therefore

```math
0<\eta_{ch,20}^{SEL2}
={1\over2}(\tau_{20}-\bar\eta_{res,20})
<1-\eta_{19}^{res},
```

because `tau_20<1`. Paper 19 Theorem 8L.8A then gives
`P19-CHTAIL-AUDIT(eta_ch,20^SEL2)` on the same record law.

For the total activity,

```math
\eta_*^{SEL2}
\le
\bar\eta_{res,20}
 + {1\over2}(\tau_{20}-\bar\eta_{res,20})
=
{1\over2}(\tau_{20}+\bar\eta_{res,20})
<
\tau_{20}.
```

Since `x/(1-x)` is strictly increasing on `(0,1)`,

```math
{20\eta_*^{SEL2}\over1-\eta_*^{SEL2}}
<
{20\tau_{20}\over1-\tau_{20}}
=
L_{20}.
```

The last equality is the definition `tau_20=L_20/(20+L_20)`. Exponentiating
gives

```math
D_{dec}^{SEL2,20}
<
\exp(L_{20})-1
=
Sig_{AFM}^{SEL2}.
```

This is exactly the full decoration-only inequality with `C_area=20`. `square`

### Definition 4.3A.36: `SEL2` Transport Common-Record Audit

`P20-SEL2-TR-COMMON` holds for the frozen branch

```math
P20\text{-}SEL2(\eta_{ch,20}^{SEL2},20)
```

when the Paper-19 transport ledger is instantiated on exactly the same
pushed-forward record law and with the following disjoint debit assignment.

1. The finite laws are the restrictions of the same frozen scalar record law
   used in Theorem 4.3A.35:

   ```math
   \Gamma_j^{SEL2}=\rho_j(Law_*^{SEL2}).
   ```

2. The Paper-16 heat-kernel tower, the Paper-19 direct-witness tower, and the
   Paper-14 finite-block export are identified after pushforward. There is no
   independent gauge-fixed, local-field, or polymer subprocess.

3. The multiplicative area-collar decoration debit is charged only to
   `D_dec^{SEL2,20}`. Endpoint/corner loop-readout debits are charged only to
   `T_12`; projective, regulator, RP/covariance, and finite-volume terms are
   charged only to their declared `T_11` or `T_14` homes.

4. The surface-polymer terms are charged only to `T_13`; the character-tail
   activity used there is the same `P19-CHTAIL-AUDIT(eta_ch,20^SEL2)` activity
   already fixed in Theorem 4.3A.35, not a second cutoff.

5. Every exported quantity is a scalar inequality for the same finite record
   laws `Gamma_j^{SEL2}`.

This is a compatibility audit. It does not assert that any transport ceiling
is small, or that the final loss inequality holds.

### Theorem 4.3A.37: `SEL2` Instantiates Paper-19 Transport Compatibility

Assume:

```text
P20-SEL2(eta_{ch,20}^{SEL2},20),
Theorem 4.3A.35 decoration closure,
HK-WP-CLOSE on the identified Paper-16 tower,
same-battery Paper-14 export chain eta_j,
the disjoint debit assignment of Definition 4.3A.36.
```

Then `P20-SEL2-TR-COMMON` holds. Consequently the Paper-19 common-record
transport audit `P19-TR-COMMON` holds on the frozen `SEL2` selector.

Proof.

The frozen `SEL2` selector fixes the AF row, finite scalar record laws,
restriction maps, representation channel, loop/window batteries, character-tail
budget, area-collar decoration constant, analytic import, and transport debit
register. Theorem 4.3A.35 fixes the decoration activity and its character-tail
cutoff on that same record law. The assumed `HK-WP-CLOSE` identifies the
Paper-16 certificates with this pushed-forward scalar tower, and the Paper-14
export attaches its finite-block error vector to the same cofinal family.
Definition 4.3A.36 gives each source defect one scalar value and one ledger
home. These are exactly the Paper-19 `P19-TR-COMMON` clauses with `SEL2`
replacing `SEL0`. `square`

### Definition 4.3A.38: `SEL2` Post-Decoration Margin And Transport Ceilings

On the frozen unit-normalized `SEL2` branch of Theorem 4.3A.35, define the
certified total activity ceiling

```math
\widehat\eta_{*,20}
:=
{1\over2}(\tau_{20}+\bar\eta_{res,20}),
```

so that `eta_*^{SEL2}<=widehat eta_{*,20}<tau_20`. The certified
post-decoration margin is

```math
\underline M_{loss}^{SEL2,20}
:=
\exp(L_{20})
-
\exp\left(
{20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right)
>0.
```

The strict positivity is exactly the slack proved in Theorem 4.3A.35.

Assume `P20-SEL2-TR-COMMON`. Define the linear transport ceilings by the same
Paper-19 component ledgers as Definition 4.3, but evaluated on the frozen
`SEL2` record law and disjoint debit register:

```math
T_{11}^{SEL2}
:=
A_{11}^{loc,SEL2}
+A_{11}^{RP,SEL2}
+A_{11}^{Cov,SEL2}
+A_{11}^{gauge,SEL2},
```

```math
T_{12}^{SEL2}
:=
A_{12}^{per,SEL2}
+A_{12}^{cusp,SEL2}
+A_{12}^{smear,SEL2}
+A_{12}^{app,SEL2}
+E_{corn}^{SEL2},
```

```math
T_{14}^{SEL2}:=E_{14}^{SEL2}.
```

Here `E_corn^SEL2` is included only when endpoint/corner loop-readout effects
were moved out of the multiplicative decoration register; it may not also be
charged to `D_dec`, `T_11`, `T_13`, or `T_14`.

Let

```math
L_{pre13}^{SEL2}
:=
T_{11}^{SEL2}
+T_{12}^{SEL2}
+T_{14}^{SEL2}
+A_{13}^{entry,SEL2}
+A_{13}^{exact,SEL2},
```

and define the certified pre-surface margin

```math
\underline M_{pre13}^{SEL2,20}
:=
\underline M_{loss}^{SEL2,20}
-L_{pre13}^{SEL2}.
```

Finally set

```math
h_{13}^{SEL2}:=3+\log 20,
\qquad
d_{13}^{SEL2,20}
:=
20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}.
```

The number `d_13^{SEL2,20}` is an upper bound on the surface-decoration
exponent because the same unit-counted area-collar constant `20` and the same
activity ceiling `widehat eta_{*,20}` are used in the surface-collar ledger.
This is not a second multiplicative decoration debit: `D_dec^{SEL2,20}` has
already paid the finite-battery decoration loss, while `d_13^{SEL2,20}` is the
Paper-19 rate degradation inside the disjoint `T_13` surface-polymer estimate.
For a proposed leading central-character rate `kappa_13^*`, define

```math
\mu_{13}^{SEL2}(\kappa_{13}^*)
:=
\kappa_{13}^*
-h_{13}^{SEL2}
-d_{13}^{SEL2,20}.
```

### Theorem 4.3A.39: `SEL2` Loss Closure Reduces To One Leading-Rate Inequality

Assume:

```text
P20-SEL2-TR-COMMON,
the finite component ceilings of Definition 4.3A.38,
Theorem 4.3A.35 decoration closure.
```

If

```math
\underline M_{pre13}^{SEL2,20}>0
```

and the sharp same-record leading coefficient rate satisfies

```math
\kappa_{13}^{CE}
>
h_{13}^{SEL2}
+d_{13}^{SEL2,20}
+\log\left(
1+{M_{13}^{surf,SEL2}\over\underline M_{pre13}^{SEL2,20}}
\right),
```

then the frozen `SEL2` branch proves `P20-LOSS-PASS`.

Conversely, if `underline M_pre13^{SEL2,20}<=0`, this `SEL2` source route fails
before the surface-polymer leading-rate test, because all remaining debits are
nonnegative.

Proof.

Theorem 4.3A.35 gives

```math
D_{dec}^{SEL2,20}
\le
Sig_{AFM}^{SEL2}
-\underline M_{loss}^{SEL2,20}.
```

The component ceilings in Definition 4.3A.38 give the linear and exact-entry
debits bounded by `L_pre13^SEL2`, leaving
`underline M_pre13^{SEL2,20}` for the surface-polymer tail. Choose
`kappa_13^*` strictly between the displayed threshold and `kappa_13^CE`. Then
`mu_13^SEL2(kappa_13^*)>0` and

```math
\mu_{13}^{SEL2}(\kappa_{13}^*)
>
\log\left(
1+{M_{13}^{surf,SEL2}\over\underline M_{pre13}^{SEL2,20}}
\right).
```

Equivalently,

```math
M_{13}^{surf,SEL2}
{\exp[-\mu_{13}^{SEL2}(\kappa_{13}^*)]
\over
1-\exp[-\mu_{13}^{SEL2}(\kappa_{13}^*)]}
<
\underline M_{pre13}^{SEL2,20}.
```

Paper 19's `T_13` surface-polymer theorem then permits a strict admissible
`q_13^*` above `exp[-mu_13^SEL2(kappa_13^*)]` with surface debit still below
the displayed margin. Adding back `D_dec`, `T_11`, `T_12`, `T_14`, entry, and
exact-comparison debits gives total loss strictly below `Sig_AFM^SEL2`, which
is `P20-LOSS-PASS`. If the certified pre-surface margin is nonpositive, no
nonnegative surface estimate can restore strict loss domination. `square`

### Definition 4.3A.40: `SEL2` Large-Field Source Audit `P20-SEL2-LFSRC`

`P20-SEL2-LFSRC(delta_lf,t_L,xi_lf)` holds when the finite block/collar
heat-kernel source data used by the frozen `SEL2` branch satisfy the following
clauses on the same pushed-forward scalar record law.

1. The standard finite block/collar template ledger `HK-LF-TPL` is fixed, with
   the same block graph, collars, axial-tree charts, large-field record events,
   and finite residual battery as the `SEL2` decoration and transport ledgers.
2. The heat-kernel plaquette tail constants `C_H,c_H,t_H` and the local lower
   constants are evaluated with one declared bi-invariant metric on `SU(N)`.
3. The collar-adapted denominator source `HK-CAD(C_ad,a_ad,e_col,delta_lf,b,t_ad)`
   holds, and its finite-energy margin is strict:

   ```math
   c_H-a_ad>0.
   ```

4. Bad collars are assigned to the adjacent large-field polymer record event.
   They are not discarded and are not charged again to `T_11`, `T_12`, `T_13`,
   `T_14`, or `D_dec`.
5. The finite source ledger `HK-LF-REP-SRC(N_lab,J_blk,R_blk,E_blk)` holds for
   the residual extractor used by the same finite battery.
6. Connected block polymers through a fixed block obey the same entropy bound

   ```math
   N_{conn}(n;x)\le C_{ent}\exp(h_{poly}n)
   ```

   used in the clean residual KP worksheet.
7. The AF heat-kernel tail satisfies `t_i<=t_L` cofinally.
8. With

   ```math
   K_L:=C_ad P_b C_H N_lab J_blk R_blk E_blk,
   ```

   the chosen time cutoff satisfies

   ```math
   0<t_L<\min(t_H,t_ad)
   ```

   and

   ```math
   {(c_H-a_ad)\delta_{lf}^2\over t_L}
   \ge
   h_{poly}+\log K_L+\xi_{lf}.
   ```

The audit is a source statement. It is allowed to use axial-tree coordinates
and local field variables in the proof, but its conclusion is only the scalar
large-field record estimate exported to the pushed-forward `SEL2` law.

### Theorem 4.3A.41: `P20-SEL2-LFSRC` Closes Step 1

Assume `P20-SEL2-LFSRC(delta_lf,t_L,xi_lf)` with `0<delta_lf<delta_0`.
Then the Paper-16 source certificate `HK-LF-SRC(delta_lf,t_L)` holds on the
frozen `SEL2` record law, and

```math
\sigma_{lf}^{sharp}\ge h_{poly}+\xi_{lf}.
```

Consequently, if

```math
\xi_{lf}>
h_{KP}+m+\delta_{20}^{suff}+\epsilon_{lf}-h_{poly},
```

then the large-field input of Theorem 4.3A.33 holds with
`delta=delta_20(epsilon_lf)`.

Proof.

Clauses 1--6 of `P20-SEL2-LFSRC` are exactly the first five source clauses of
Paper 16 Definition 9J.1A, together with the shared entropy ledger. Clause 3
gives the strict collar margin `c_H>a_ad`. Clause 8 is the entropy-margin
choice in Paper 16 Theorem 9J.1C:

```math
\sigma_{lf}^{sharp}
=
{(c_H-a_ad)\delta_{lf}^2\over t_L}
-\log K_L
\ge h_{poly}+\xi_{lf}.
```

Clause 7 restricts the AF tail so the same finite certificate applies
cofinally. Therefore `HK-LF-SRC(delta_lf,t_L)` holds and exports the displayed
rate. The final implication is the displayed strict lower bound on `xi_lf`.
`square`

### Corollary 4.3A.42: Standard Finite Templates Supply `P20-SEL2-LFSRC`

Assume the Paper-16 standard heat-kernel source hypotheses:

```text
HK-LF-TPL,
one common bi-invariant heat-kernel metric,
t_i -> 0 along the AF tail.
```

Then, for every required finite excess `xi_lf>0`, there are
`delta_lf,t_L` with `0<delta_lf<delta_0` such that

```text
P20-SEL2-LFSRC(delta_lf,t_L,xi_lf)
```

holds on the pushed-forward `SEL2` record law.

Proof.

Paper 16 Theorem 9J.6 gives `HK-CAD` on the standard finite template with a
strict margin, in fact `c_H-a_ad=c_H/4` after its canonical choice of
parameters. Paper 16 Theorem 9J.7 gives `HK-LF-REP-SRC` with finite
template constants. The trigger count, bad-collar assignment, and connected
polymer entropy are part of `HK-LF-TPL`. Paper 16 Theorem 9J.8 then chooses
`t_L` below `min(t_H,t_ad)` so that the inequality in Definition 4.3A.40 holds,
and the AF condition `t_i->0` gives `t_i<=t_L` cofinally. The pushforward
clause is the same common-record requirement as Definition 4.3A.36. `square`

If any source hypothesis in this corollary is unavailable on the selected
whole-process tower, Step 1 is not closed for that tower. The obstruction is
local: finite block/collar template failure, metric mismatch, denominator
failure, finite-battery extractor failure, entropy failure, or lack of a
cofinal heat-kernel tail.

### Definition 4.3A.43: Frozen `SEL2` Branch Worksheet

After Step 1 is closed, choose `epsilon_lf>0` and set

```math
\delta_{20}:=\delta_{20}(\epsilon_{lf})
=\delta_{20}^{suff}+\epsilon_{lf}.
```

The frozen unit-normalized `SEL2` worksheet is the scalar list

```math
\bar\eta_{res,20}
=
2C_{KP}{\exp(-\delta_{20}r_{res}^{clean})
\over1-\exp(-\delta_{20})},
```

```math
\tau_{20}={L_{20}\over20+L_{20}},
\qquad
\eta_{ch,20}^{SEL2}
={1\over2}(\tau_{20}-\bar\eta_{res,20}),
```

```math
\widehat\eta_{*,20}
={1\over2}(\tau_{20}+\bar\eta_{res,20}),
```

and

```math
\underline M_{loss}^{SEL2,20}
=
\exp(L_{20})
-
\exp\left(
{20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right).
```

The branch is declared frozen only if

```math
0<\bar\eta_{res,20}<\tau_{20}.
```

When this holds, `eta_ch,20^SEL2>0`,
`widehat eta_{*,20}<tau_20`, and `underline M_loss^{SEL2,20}>0`.

### Theorem 4.3A.44: Step 2 Freezes A Genuine `SEL2` Selector

Assume Step 1 has been closed by Theorem 4.3A.41 or Corollary 4.3A.42, and
assume the worksheet inequality

```math
\bar\eta_{res,20}<\tau_{20}
```

holds. Then the selector

```math
P20\text{-}SEL2(\eta_{ch,20}^{SEL2},20)
```

is a genuine frozen selector in the sense of Definition 1.10, its character
budget is strict, and its pre-transport decoration debit satisfies

```math
D_{dec}^{SEL2,20}<Sig_{AFM}^{SEL2}.
```

Proof.

The strict worksheet inequality gives the hypotheses of Definition 4.3A.34.
Theorem 4.3A.35 then imports the same-record character-tail audit and proves
the displayed decoration inequality with `C_area=20`. Definition 1.10 and
Lemma 1.11 are satisfied because the branch has now fixed the AF row, the
analytic source, the character-tail budget, and the finite area-collar
constant before any transport comparison is invoked. `square`

### Definition 4.3A.45: `SEL2` Linear Transport Evaluation Audit

On the frozen selector of Theorem 4.3A.44, `P20-SEL2-LIN-EVAL` holds when the
following same-record Paper-19 source attacks are available:

```text
P19-T11-LEDGER(A_{11}^{loc,SEL2},A_{11}^{RP,SEL2},A_{11}^{Cov,SEL2},A_{11}^{gauge,SEL2}),
P19-T12-LEDGER(A_{12}^{per,SEL2},A_{12}^{cusp,SEL2},A_{12}^{smear,SEL2},A_{12}^{app,SEL2}),
P19-T13-ENTRY(A_{13}^{entry,SEL2}),
P19-T13-EXACT(A_{13}^{exact,SEL2}),
P19-P14-EXPORT(E_{14}^{SEL2}).
```

The audit additionally requires the disjoint assignment of Definition 4.3A.36:
projective/regulator/volume and RP/covariance/gauge terms are not charged to
`T_12` or `T_13`; perimeter/cusp/smearing/readout terms are not charged to
`T_11`; exact-entry and cutoff-to-exact scalar terms are not charged to
`D_dec`.

The evaluated nonsurface transport debit is

```math
L_{pre13}^{SEL2}
:=
T_{11}^{SEL2}
+T_{12}^{SEL2}
+T_{14}^{SEL2}
+A_{13}^{entry,SEL2}
+A_{13}^{exact,SEL2},
```

with `T_11^SEL2`, `T_12^SEL2`, and `T_14^SEL2` as in Definition 4.3A.38.

### Theorem 4.3A.46: Step 3 Evaluates The Linear Transport Ceilings

Assume `P20-SEL2-TR-COMMON` and `P20-SEL2-LIN-EVAL`. Then

```math
\limsup_jT_{11,j}^{SEL2}\le T_{11}^{SEL2},
\qquad
\limsup_jT_{12,j}^{SEL2}\le T_{12}^{SEL2},
\qquad
\limsup_jT_{14,j}^{SEL2}\le T_{14}^{SEL2},
```

and the non-surface part of `T_13` obeys

```math
\limsup_j
\left(
R_{13,j}^{entry,SEL2}+R_{13,j}^{exact,SEL2}
\right)
\le
A_{13}^{entry,SEL2}+A_{13}^{exact,SEL2}.
```

Consequently the total pre-surface debit is bounded by
`L_pre13^SEL2`.

Proof.

The `T_11` conclusion is Paper 19 Theorem 8L.11A.6 applied to the reduced
`SEL2` ledger. The `T_12` conclusion is Paper 19 Theorem 8L.11A.8. The
`T_14` conclusion is Paper 19 Theorem 8L.11A.4. The entry and exact scalar
comparison bounds are the two nonsurface components isolated in Paper 19
Definitions 8L.11A.24 and 8L.11A.25, with the same common-record audit
preventing double charge. Adding the finite limsup bounds gives the displayed
`L_pre13^SEL2` ceiling. `square`

### Theorem 4.3A.47: Step 4 Certifies Or Localizes The Pre-`T_13` Margin

Assume the frozen worksheet of Definition 4.3A.43 and the linear evaluation
audit of Definition 4.3A.45. The `SEL2` branch is certified to pass the
pre-surface transport test whenever

```math
L_{pre13}^{SEL2}
<
\underline M_{loss}^{SEL2,20}.
```

Equivalently, the certified upper-margin

```math
\underline M_{pre13}^{SEL2,20}
=
\underline M_{loss}^{SEL2,20}-L_{pre13}^{SEL2}
>0.
```

For a genuine failure certificate, suppose in addition that the same record law
supplies a lower floor `L_{pre13}^{SEL2,-}` for the actual nonsurface
transport debit:

```math
0\le L_{pre13}^{SEL2,-}
\le
\liminf_j
\left(
T_{11,j}^{SEL2}
+T_{12,j}^{SEL2}
+T_{14,j}^{SEL2}
+R_{13,j}^{entry,SEL2}
+R_{13,j}^{exact,SEL2}
\right).
```

If

```math
L_{pre13}^{SEL2,-}
\ge
\underline M_{loss}^{SEL2,20},
```

then this frozen `SEL2` route fails before the surface-polymer leading-rate
test. If neither the upper-margin strict inequality nor such a lower-floor
failure inequality is known, Step 4 is undecided rather than falsified.

Proof.

Theorem 4.3A.44 leaves the strict post-decoration margin
`underline M_loss^{SEL2,20}` for all transport losses. Theorem 4.3A.46 bounds
the nonsurface transport debit by `L_pre13^SEL2`. Therefore a positive margin
remains for the surface-polymer debit exactly when the first displayed strict
inequality holds.

For the failure statement, the lower floor says that the actual nonsurface
debit alone already consumes the full post-decoration margin. Since the
remaining surface-polymer debit is nonnegative, no later `T_13` leading-rate
estimate can make the total loss strictly less than `Sig_AFM^SEL2`. Without a
lower floor, a large upper ceiling is only a weak estimate, not a mathematical
failure of the branch. `square`

### Definition 4.3A.48: Canonical `SEL2` Source Parameters

Fix `epsilon_lf>0` and set

```math
\delta_{20}:=\delta_{20}^{suff}+\epsilon_{lf}.
```

Define the canonical large-field excess requested from Paper 16 by

```math
\xi_{lf}^{20}(\epsilon_{lf})
:=
1+\max\{0,\ h_{KP}+m+\delta_{20}-h_{poly}\}.
```

Thus

```math
h_{poly}+\xi_{lf}^{20}(\epsilon_{lf})
>
h_{KP}+m+\delta_{20}.
```

Given a standard Paper-16 finite block/collar source instance, choose
`delta_lf` with

```math
0<\delta_{lf}<\min(\delta_0,\delta_{col}),
```

and define

```math
K_L:=C_adP_bC_HN_labJ_blkR_blkE_blk.
```

The canonical `SEL2` heat-kernel time cutoff is any number `t_L^{20}`
satisfying

```math
0<t_L^{20}<\min(t_H,t_ad)
```

and

```math
{(c_H-a_ad)\delta_{lf}^2\over t_L^{20}}
\ge
h_{poly}+\log K_L+\xi_{lf}^{20}(\epsilon_{lf}).
```

Such a `t_L^{20}` exists whenever `c_H>a_ad` and all constants in `K_L` are
finite.

### Theorem 4.3A.49: Step 1 Source Pass For The Standard `SEL2` Template

Assume the standard Paper-16 finite-template hypotheses of Corollary 4.3A.42
on the same pushed-forward record law:

```text
HK-LF-TPL,
one common bi-invariant heat-kernel metric,
t_i -> 0 along the AF tail.
```

Then for every `epsilon_lf>0` the canonical parameters of Definition 4.3A.48
give

```text
P20-SEL2-LFSRC(delta_lf,t_L^{20},xi_lf^{20}(epsilon_lf)).
```

Consequently Step 1 is closed for the standard `SEL2` template, and

```math
\sigma_{lf}^{sharp}
>
h_{KP}+m+\delta_{20}^{suff}+\epsilon_{lf}.
```

Proof.

Paper 16 Theorem 9J.6 supplies `HK-CAD` with strict margin
`c_H-a_ad>0`; Paper 16 Theorem 9J.7 supplies finite
`HK-LF-REP-SRC` constants; Paper 16 Theorem 9J.8 chooses a cofinal
heat-kernel time cutoff below `min(t_H,t_ad)` for any prescribed finite
`xi_lf`. Applying it to `xi_lf=xi_lf^{20}(epsilon_lf)` proves
`P20-SEL2-LFSRC`. The strict rate inequality follows from Definition
4.3A.48 and Theorem 4.3A.41. `square`

This theorem does not construct a continuum Yang-Mills measure. It only says
that, conditional on the same finite heat-kernel template tower used by Paper
16, the large-field source margin needed by the `SEL2` scalar worksheet is
available without importing an area law.

### Lemma 4.3A.50: Step 2 Worksheet Strictness

Assume `epsilon_lf>0`, `C_KP<infinity`, `r_res^clean>=1`, and
`L_20>0`. With the definitions

```math
\tau_{20}:={L_{20}\over20+L_{20}},
```

```math
\delta_{20}^{suff}
:=
\log\left(1+{2C_{KP}\over\tau_{20}}\right)
=
\log\left(1+{2C_{KP}(20+L_{20})\over L_{20}}\right),
```

and

```math
\delta_{20}:=\delta_{20}^{suff}+\epsilon_{lf},
```

the residual worksheet bound of Definition 4.3A.43 satisfies

```math
\bar\eta_{res,20}<\tau_{20}.
```

Hence the character budget and post-decoration margin are strictly positive:

```math
\eta_{ch,20}^{SEL2}>0,
\qquad
\underline M_{loss}^{SEL2,20}>0.
```

Proof.

Let `x=exp(-delta_20)`. Since `epsilon_lf>0`,

```math
x<\exp(-\delta_{20}^{suff})
={\tau_{20}\over2C_{KP}+\tau_{20}}.
```

Because `r_res^clean>=1`,

```math
\bar\eta_{res,20}
=
2C_{KP}{x^{r_res^{clean}}\over1-x}
\le
2C_{KP}{x\over1-x}.
```

The inequality `x<tau_20/(2C_KP+tau_20)` is equivalent to

```math
2C_{KP}{x\over1-x}<\tau_{20}.
```

Therefore `bar eta_res,20<tau_20`. The definitions of
`eta_ch,20^SEL2` and `widehat eta_*,20` then give
`eta_ch,20^SEL2>0` and `widehat eta_*,20<tau_20`. The formula for
`underline M_loss^SEL2,20` is strictly positive because
`x/(1-x)` is strictly increasing and
`20 tau_20/(1-tau_20)=L_20`. `square`

### Theorem 4.3A.51: Step 2 Freezes The Standard `SEL2` Branch

Assume Step 1 is closed by Theorem 4.3A.49, and fix any
`epsilon_lf>0`. Then the canonical worksheet of Definition 4.3A.43 freezes a
genuine selector

```math
P20\text{-}SEL2(\eta_{ch,20}^{SEL2},20)
```

and proves the full pre-transport decoration inequality

```math
D_{dec}^{SEL2,20}<Sig_{AFM}^{SEL2}.
```

Proof.

Theorem 4.3A.49 supplies the source hypothesis needed by Theorem 4.3A.33.
Lemma 4.3A.50 proves the strict worksheet inequality
`bar eta_res,20<tau_20`. Theorem 4.3A.44 then freezes the selector and
imports the decoration pass from Theorem 4.3A.35. `square`

### Definition 4.3A.52: `SEL2` Transport Source Package

`P20-SEL2-TRANSPORT-SRC` holds when the following Paper-19 source attacks are
available on the same frozen selector of Theorem 4.3A.51:

```text
P19-T11-LOC-AF(A_{11}^{loc,SEL2}),
P19-T11-RP(A_{11}^{RP,SEL2}),
P19-T11-COV(A_{11}^{Cov,SEL2}),
P19-T11-GAUGE(A_{11}^{gauge,SEL2}),
P19-T12-PC(A_{12}^{per,SEL2},A_{12}^{cusp,SEL2}),
P19-T12-SMEAR(A_{12}^{smear,SEL2}),
P19-T12-APP(A_{12}^{app,SEL2}),
P19-T13-ENTRY(A_{13}^{entry,SEL2}),
P19-T13-EXACT(A_{13}^{exact,SEL2}),
P19-P14-EXPORT(E_{14}^{SEL2}).
```

It also requires the Paper-19 reduced `T_12` evaluation worksheet on the same
loop-readout record law:

```text
P19-T12-EVAL.
```

The source package is deliberately missing the surface-polymer leading-rate
slot. It evaluates only the nonsurface terms needed before `T_13`:

```math
T_{11}^{SEL2},
\quad
T_{12}^{SEL2},
\quad
T_{14}^{SEL2},
\quad
A_{13}^{entry,SEL2},
\quad
A_{13}^{exact,SEL2}.
```

### Theorem 4.3A.53: Step 3 Source Package Proves `P20-SEL2-LIN-EVAL`

Assume `P20-SEL2-TR-COMMON` and `P20-SEL2-TRANSPORT-SRC`. Then
`P20-SEL2-LIN-EVAL` holds with the component values declared in Definition
4.3A.52. Consequently the evaluated nonsurface debit is

```math
L_{pre13}^{SEL2}
=
A_{11}^{loc,SEL2}+A_{11}^{RP,SEL2}+A_{11}^{Cov,SEL2}+A_{11}^{gauge,SEL2}
+A_{12}^{per,SEL2}+A_{12}^{cusp,SEL2}
+A_{12}^{smear,SEL2}+A_{12}^{app,SEL2}+E_{corn}^{SEL2}
+E_{14}^{SEL2}
+A_{13}^{entry,SEL2}+A_{13}^{exact,SEL2}.
```

If the reduced loop-readout branch assigns no endpoint/corner term outside
the multiplicative decoration register, set `E_corn^{SEL2}=0`; otherwise it
is the uniquely declared `T_12` endpoint/corner debit.

Proof.

Paper 19 Theorem 8L.11A.15D turns the four `T_11` source attacks into
`P19-T11-LEDGER` and hence the `T_11` bound. Paper 19 Theorem 8L.11A.21E
turns the reduced `T_12` source attacks and `P19-T12-EVAL` into the evaluated
`T_12` constants. Paper 19 Theorem 8L.11A.4 supplies the `T_14` bound from
`P19-P14-EXPORT`. Paper 19 Definitions 8L.11A.24 and 8L.11A.25 supply the
entry and exact-comparison nonsurface `T_13` bounds.

The common-record audit and the disjoint debit assignment in
`P20-SEL2-TR-COMMON` ensure these source attacks are evaluated on one scalar
record law and do not double-charge decoration, projective/regulator/volume,
loop-readout, or surface-polymer terms. Therefore the hypotheses of
Definition 4.3A.45 hold, which is `P20-SEL2-LIN-EVAL`; expanding
Definitions 4.3A.38 and 4.3A.45 gives the displayed `L_pre13^SEL2`. `square`

### Theorem 4.3A.54: Step 4 Scalar Decision After The Source Package

Assume Theorem 4.3A.51 freezes the standard `SEL2` selector, and assume
`P20-SEL2-TRANSPORT-SRC` with `P20-SEL2-TR-COMMON`. Define

```math
\mathcal M_{pre13}^{SEL2}
:=
\underline M_{loss}^{SEL2,20}
-L_{pre13}^{SEL2},
```

with `L_pre13^SEL2` expanded in Theorem 4.3A.53. If

```math
\mathcal M_{pre13}^{SEL2}>0,
```

then Steps 1--4 pass and the only remaining loss question is the surface
leading-rate inequality of Theorem 4.3A.39:

```math
\kappa_{13}^{CE}
>
h_{13}^{SEL2}
+d_{13}^{SEL2,20}
+\log\left(
1+{M_{13}^{surf,SEL2}\over\mathcal M_{pre13}^{SEL2}}
\right).
```

If a same-record lower floor `L_{pre13}^{SEL2,-}` is proved and

```math
L_{pre13}^{SEL2,-}
\ge
\underline M_{loss}^{SEL2,20},
```

then the standard `SEL2` branch fails before the surface-leading-rate test.
If neither inequality is known, Step 4 remains undecided.

Proof.

Theorem 4.3A.51 gives the frozen branch and strict post-decoration margin.
Theorem 4.3A.53 gives the evaluated nonsurface transport ceiling, so
`\mathcal M_{pre13}^{SEL2}` is exactly the certified pre-surface margin of
Definition 4.3A.38. The positive case is Theorem 4.3A.47 followed by Theorem
4.3A.39. The lower-floor failure and undecided cases are exactly the two
remaining alternatives in Theorem 4.3A.47. `square`

### Definition 4.3A.55: Fully Expanded `SEL2` Pre-`T_13` Scoreboard

On the standard frozen `SEL2` branch of Theorem 4.3A.51, fix
`epsilon_lf>0` and write

```math
L_{20}:=\log(1+Sig_{AFM}^{SEL2}),
\qquad
\tau_{20}:={L_{20}\over20+L_{20}},
```

```math
\delta_{20}
:=
\log\left(1+{2C_{KP}\over\tau_{20}}\right)+\epsilon_{lf},
```

and

```math
\bar\eta_{res,20}
:=
2C_{KP}
{\exp(-\delta_{20}r_{res}^{clean})
\over
1-\exp(-\delta_{20})}.
```

The certified activity ceiling is

```math
\widehat\eta_{*,20}
:=
{1\over2}(\tau_{20}+\bar\eta_{res,20}),
```

and the post-decoration margin is

```math
\underline M_{loss}^{SEL2,20}
=
\exp(L_{20})
-
\exp\left(
{20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right).
```

The fully expanded nonsurface debit is

```math
L_{pre13}^{SEL2}
=
A_{11}^{loc,SEL2}
+A_{11}^{RP,SEL2}
+A_{11}^{Cov,SEL2}
+A_{11}^{gauge,SEL2}
+A_{12}^{per,SEL2}
+A_{12}^{cusp,SEL2}
+A_{12}^{smear,SEL2}
+A_{12}^{app,SEL2}
+E_{corn}^{SEL2}
+E_{14}^{SEL2}
+A_{13}^{entry,SEL2}
+A_{13}^{exact,SEL2}.
```

The `SEL2` pre-surface scoreboard is

```math
\mathcal M_{pre13}^{SEL2}
=
\exp(L_{20})
-
\exp\left(
{20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right)
-
\Big(
A_{11}^{loc,SEL2}
+A_{11}^{RP,SEL2}
+A_{11}^{Cov,SEL2}
+A_{11}^{gauge,SEL2}
+A_{12}^{per,SEL2}
+A_{12}^{cusp,SEL2}
+A_{12}^{smear,SEL2}
+A_{12}^{app,SEL2}
+E_{corn}^{SEL2}
+E_{14}^{SEL2}
+A_{13}^{entry,SEL2}
+A_{13}^{exact,SEL2}
\Big).
```

This is the single scalar quantity that decides whether the branch reaches the
surface-leading-rate problem. It contains no `T_13` surface-polymer debit and
no leading-sheet coefficient assumption.

### Theorem 4.3A.56: The Scoreboard Is Exactly The Step-4 Margin

Assume Theorem 4.3A.51 and `P20-SEL2-TRANSPORT-SRC`. Then the expanded
scoreboard of Definition 4.3A.55 equals the certified pre-surface margin of
Theorem 4.3A.54:

```math
\mathcal M_{pre13}^{SEL2}
=
\underline M_{loss}^{SEL2,20}-L_{pre13}^{SEL2}.
```

Consequently the standard `SEL2` branch is certified through Steps 1--4 if
and only if this displayed expanded expression is strictly positive.

Proof.

Definition 4.3A.55 substitutes the explicit formulas for
`underline M_loss^{SEL2,20}` and `L_pre13^SEL2` from Definitions 4.3A.38 and
4.3A.43, with the component expansion proved by Theorem 4.3A.53. Therefore it
is algebraically identical to the Step-4 margin in Theorem 4.3A.54. `square`

### Definition 4.3A.57: Nonsurface Transport Upper-Bound Package

`P20-SEL2-NS-UPPER(U_{pre13}^{SEL2})` holds when the same frozen `SEL2` record
law supplies finite upper bounds

```math
A_{11}^{loc,SEL2}\le U_{11}^{loc},
\quad
A_{11}^{RP,SEL2}\le U_{11}^{RP},
\quad
A_{11}^{Cov,SEL2}\le U_{11}^{Cov},
\quad
A_{11}^{gauge,SEL2}\le U_{11}^{gauge},
```

```math
A_{12}^{per,SEL2}\le U_{12}^{per},
\quad
A_{12}^{cusp,SEL2}\le U_{12}^{cusp},
\quad
A_{12}^{smear,SEL2}\le U_{12}^{smear},
\quad
A_{12}^{app,SEL2}\le U_{12}^{app},
```

```math
E_{corn}^{SEL2}\le U_{corn},
\quad
E_{14}^{SEL2}\le U_{14},
\quad
A_{13}^{entry,SEL2}\le U_{13}^{entry},
\quad
A_{13}^{exact,SEL2}\le U_{13}^{exact},
```

all obtained from the source attacks in Definition 4.3A.52, and

```math
U_{pre13}^{SEL2}
:=
U_{11}^{loc}+U_{11}^{RP}+U_{11}^{Cov}+U_{11}^{gauge}
+U_{12}^{per}+U_{12}^{cusp}+U_{12}^{smear}+U_{12}^{app}
+U_{corn}+U_{14}+U_{13}^{entry}+U_{13}^{exact}.
```

This package is an upper-bound certificate only. It proves a pass when small
enough, but a large value does not falsify the branch unless accompanied by a
same-record lower floor as in Theorem 4.3A.47.

### Theorem 4.3A.58: Nonsurface Bounds Decide Step 2 Of The Remaining Work

Assume the standard `SEL2` branch is frozen by Theorem 4.3A.51 and assume
`P20-SEL2-NS-UPPER(U_{pre13}^{SEL2})`. If

```math
U_{pre13}^{SEL2}
<
\underline M_{loss}^{SEL2,20},
```

then

```math
\mathcal M_{pre13}^{SEL2}
>
0,
```

so Steps 1--4 pass and the paper may proceed to the leading-rate test
`kappa_13^{CE}`.

In particular, if all nonsurface source attacks close with zero debit,

```math
U_{pre13}^{SEL2}=0,
```

then the pre-surface margin is strictly positive:

```math
\mathcal M_{pre13}^{SEL2}
=
\underline M_{loss}^{SEL2,20}
>0.
```

Proof.

The upper-bound package gives

```math
L_{pre13}^{SEL2}\le U_{pre13}^{SEL2}.
```

If `U_pre13^SEL2<underline M_loss^{SEL2,20}`, then
`L_pre13^SEL2<underline M_loss^{SEL2,20}`. Theorem 4.3A.56 gives
`\mathcal M_{pre13}^{SEL2}>0`. The zero-debit case is the same argument with
`U_pre13^SEL2=0`, using the strict positivity of
`underline M_loss^{SEL2,20}` from Lemma 4.3A.50. `square`

### Corollary 4.3A.59: Ordered Nonsurface Transport Attack

The ordered attack on `U_pre13^SEL2` is:

1. close or bound the reduced `T_12` slots:
   `A_12^{per,SEL2}`, `A_12^{cusp,SEL2}`, `A_12^{smear,SEL2}`,
   `A_12^{app,SEL2}`, and the optional `E_corn^{SEL2}`;
2. close or bound the exact-comparison slot `A_13^{exact,SEL2}`;
3. close or bound the whole-process export `E_14^{SEL2}`;
4. close or bound the reduced `T_11` slots:
   `A_11^{loc,SEL2}`, `A_11^{RP,SEL2}`, `A_11^{Cov,SEL2}`,
   `A_11^{gauge,SEL2}`;
5. close or bound the nonsurface exact-entry slot `A_13^{entry,SEL2}`;
6. compare the resulting sum to `underline M_loss^{SEL2,20}`.

Only after this sum is strictly below the margin does it make sense to spend
effort on the nonlinear surface-leading-rate inequality. This ordering avoids
using a hard `T_13` character estimate to compensate for an already failed
nonsurface ledger.

### Theorem 4.3A.60: Reduced `T_12` Component Attack

Assume `P20-SEL2-TR-COMMON`, `P19-T12-EVAL`, and the three reduced loop
source attacks on the frozen `SEL2` record law:

```text
P19-T12-PC(A_{12}^{per,SEL2},A_{12}^{cusp,SEL2}),
P19-T12-SMEAR(A_{12}^{smear,SEL2}),
P19-T12-APP(A_{12}^{app,SEL2}).
```

Then the `T_12` part of `P20-SEL2-NS-UPPER` may be taken to be

```math
U_{12}^{per}=A_{12}^{per,eval,SEL2},
\qquad
U_{12}^{cusp}=A_{12}^{cusp,eval,SEL2},
```

```math
U_{12}^{smear}=A_{12}^{smear,eval,SEL2},
\qquad
U_{12}^{app}=A_{12}^{app,eval,SEL2},
```

where the evaluated constants are the four limsups in Paper 19 Definition
8L.11A.21A, computed on the same `SEL2` loop-readout record law.

If the calibrated perimeter/cusp tails, smearing-removal tail, and reduced
loop-approximant/readout tails vanish cofinally,

```math
\sum_{k\ge j}\eta_{perLC,j,k}\to0,
\quad
\sum_{k\ge j}\eta_{cuspLC,j,k}\to0,
\quad
\sum_{k\ge j}\eta_{smearLC,j,k}\to0,
```

and

```math
\sum_{k\ge j}
\left(
\eta_{P12,j,k}
+\eta_{appLC,j,k}^{(12)}
+\eta_{binLC,j,k}^{(12)}
\right)
\to0,
```

then the reduced loop-readout contribution is zero:

```math
U_{12}^{per}=U_{12}^{cusp}=U_{12}^{smear}=U_{12}^{app}=0.
```

The optional endpoint/corner debit is

```math
U_{corn}:=E_{corn}^{SEL2},
```

with `U_corn=0` whenever the frozen `SEL2` branch does not move
endpoint/corner terms out of the multiplicative decoration register.

Proof.

Paper 19 Theorems 8L.11A.21B--8L.11A.21E identify the four reduced `T_12`
constants with exactly these four evaluated limsups, after projective,
regulator, and finite-volume terms have been removed from `T_12`. The
vanishing statement is Paper 19 Corollary 8L.11A.21 specialized to the same
`SEL2` finite row. The endpoint/corner term is not part of Paper 19's reduced
`T_12` evaluation; it is the extra Paper-20 reassignment variable introduced
for selector bookkeeping, and it is paid here only if the disjoint debit
register declares it. `square`

### Theorem 4.3A.61: Exact-Comparison Component Attack

Assume `P20-SEL2-TR-COMMON` and the Paper-19 exact-comparison source attack

```text
P19-T13-EXACT(A_{13}^{exact,SEL2}).
```

Let

```math
X_{13,j}^{exact,SEL2}
:=
\sup_{F\in B_{13,j}^{exact,SEL2}}
\left|
E_{\mu_{a_j,s_0}^{blk}}F
-
E_{\mu_{s_0}^{blk}}F
\right|
+\epsilon_{read,j}^{(13,SEL2)}.
```

If

```math
\limsup_jX_{13,j}^{exact,SEL2}\le U_{13}^{exact}<\infty,
```

then the exact-comparison component of `P20-SEL2-NS-UPPER` is closed with

```math
A_{13}^{exact,SEL2}\le U_{13}^{exact}.
```

If block convergence is exact on every fixed `SEL2` finite battery and
`epsilon_{read,j}^{(13,SEL2)}\to0`, then

```math
U_{13}^{exact}=0.
```

Proof.

This is Paper 19 Definition 8L.11A.25 with the `SEL2` record law substituted.
The projective, regulator/chart, finite-volume, and Paper-14 whole-process
terms are not included in `X_{13,j}^{exact,SEL2}` because
`P20-SEL2-TR-COMMON` assigns them to `T_11` or `T_14`. Therefore the displayed
limsup is a legitimate upper bound for `A_13^{exact,SEL2}`. The zero branch is
the final sentence of Paper 19 Definition 8L.11A.25. `square`

### Theorem 4.3A.62: Paper-14 Export Component Attack

Assume `P20-SEL2-TR-COMMON` and the same-battery Paper-14 export

```text
P19-P14-EXPORT(E_{14}^{SEL2}).
```

Then the whole-process transport component of `P20-SEL2-NS-UPPER` is closed
with

```math
U_{14}=E_{14}^{SEL2}.
```

If the Paper-14 export chain is exact on the frozen `SEL2` battery, or if its
transport norm satisfies

```math
\|E_{14}(\eta_j)\|_{tr}\to0,
```

then the zero branch is available:

```math
U_{14}=0.
```

Proof.

Paper 19 Theorem 8L.11A.4 proves
`\limsup_jT_{14,j}\le E_14^{SEL2}` from `P19-P14-EXPORT(E_14^{SEL2})`.
When the exported Paper-14 defect vector is exact or its transport norm tends
to zero, the same theorem applies with `E_14^{SEL2}=0`. `square`

### Theorem 4.3A.63: Reduced `T_11` Component Attack

Assume `P20-SEL2-TR-COMMON` and the four reduced `T_11` source attacks

```text
P19-T11-LOC-AF(A_{11}^{loc,SEL2}),
P19-T11-RP(A_{11}^{RP,SEL2}),
P19-T11-COV(A_{11}^{Cov,SEL2}),
P19-T11-GAUGE(A_{11}^{gauge,SEL2}).
```

Suppose finite bounds are proved:

```math
A_{11}^{loc,SEL2}\le U_{11}^{loc},
\quad
A_{11}^{RP,SEL2}\le U_{11}^{RP},
\quad
A_{11}^{Cov,SEL2}\le U_{11}^{Cov},
\quad
A_{11}^{gauge,SEL2}\le U_{11}^{gauge}.
```

Then the reduced `T_11` component of `P20-SEL2-NS-UPPER` is closed.

A zero reduced `T_11` branch is available if all four reduced source tails
vanish on the same finite record law:

```math
U_{11}^{loc}=U_{11}^{RP}=U_{11}^{Cov}=U_{11}^{gauge}=0.
```

Concretely, the local-RG part is zero under Paper 19 Corollary 8L.11A.15,
and the RP, covariance, and gauge/chart parts are zero when their respective
reduced Paper-16 transport tails have vanishing cofinal sums after the
perimeter/cusp, loop-readout, surface-entry, and Paper-14 terms have been
removed.

Proof.

Paper 19 Theorem 8L.11A.15D says that the four source attacks close
`P19-T11-LEDGER` and give

```math
\limsup_jT_{11,j}^{SEL2}
\le
A_{11}^{loc,SEL2}
+A_{11}^{RP,SEL2}
+A_{11}^{Cov,SEL2}
+A_{11}^{gauge,SEL2}.
```

The displayed finite upper bounds are therefore exactly the `T_11` entries
required by Definition 4.3A.57. The zero statement is the same inequality
with all four limsups equal to zero. `square`

### Theorem 4.3A.64: Exact-Entry Component Attack

Assume `P20-SEL2-TR-COMMON` and the Paper-19 exact-entry source attack

```text
P19-T13-ENTRY(A_{13}^{entry,SEL2}).
```

For the frozen `SEL2` row set

```math
E_{13,j}^{entry,SEL2}
:=
\epsilon_{BC,j}^{SEL2}
+\epsilon_{CE,j}^{SEL2}
+\epsilon_{RPF,j}^{SEL2}
+\epsilon_{KPdec,j}^{SEL2}
+\epsilon_{SUB,j}^{SEL2}
+\epsilon_{WP,j}^{SEL2}.
```

If

```math
\limsup_jE_{13,j}^{entry,SEL2}\le U_{13}^{entry}<\infty,
```

then the entry component of `P20-SEL2-NS-UPPER` is closed with

```math
A_{13}^{entry,SEL2}\le U_{13}^{entry}.
```

If all six entry residuals vanish cofinally on the same record law, then

```math
U_{13}^{entry}=0.
```

The term `epsilon_CE^{SEL2}` here is only the finite-entry transport residual
of Paper 13's actual-entry chain. It is not the later leading coefficient
rate `kappa_13^{CE}`. The term `epsilon_SUB^{SEL2}` may be counted here only
if surface subcriticality is not already charged through the reduced
`P19-T13-SUB` surface bucket.

Proof.

Paper 19 Definition 8L.11A.24 defines `E_{13,j}^{entry}` as the sum of the
six actual-entry residuals and proves that its cofinal limsup bounds
`A_13^{entry}`. Substituting the frozen `SEL2` record law gives the displayed
upper bound. If each of the six residuals tends to zero, the limsup is zero.
The final two cautions are the disjoint-debit clauses in Paper 19 Definition
8L.11A.24 and `P20-SEL2-TR-COMMON`. `square`

### Theorem 4.3A.65: Componentwise `U_pre13^SEL2` Assembly

Assume the component attacks of Theorems 4.3A.60--4.3A.64. Define

```math
U_{pre13}^{SEL2}
:=
U_{11}^{loc}+U_{11}^{RP}+U_{11}^{Cov}+U_{11}^{gauge}
+U_{12}^{per}+U_{12}^{cusp}+U_{12}^{smear}+U_{12}^{app}
+U_{corn}+U_{14}+U_{13}^{entry}+U_{13}^{exact}.
```

Then

```text
P20-SEL2-NS-UPPER(U_{pre13}^{SEL2})
```

holds. Hence, if

```math
U_{pre13}^{SEL2}<\underline M_{loss}^{SEL2,20},
```

then

```math
\mathcal M_{pre13}^{SEL2}>0,
```

and the standard `SEL2` branch reaches the leading-rate test.

If all component attacks close with zero debit, then

```math
U_{pre13}^{SEL2}=0
```

and the branch automatically passes the pre-`T_13` margin.

Proof.

Theorems 4.3A.60--4.3A.64 supply exactly the finite upper bounds required in
Definition 4.3A.57. Therefore `P20-SEL2-NS-UPPER(U_pre13^SEL2)` holds, and
Theorem 4.3A.58 gives the strict pre-surface margin whenever the aggregate
bound is below `underline M_loss^{SEL2,20}`. The zero-debit statement is the
zero case of Theorem 4.3A.58. `square`

### Corollary 4.3A.66: Easy-Zero Reduced Branch For `T_12`, `A_13^{exact}`, And `E_14`

Assume `P20-SEL2-TR-COMMON`. Suppose the reduced `SEL2` source audits satisfy
the following cofinal vanishing clauses:

```math
\sum_{k\ge j}\eta_{perLC,j,k}\to0,\qquad
\sum_{k\ge j}\eta_{cuspLC,j,k}\to0,\qquad
\sum_{k\ge j}\eta_{smearLC,j,k}\to0,
```

```math
\sum_{k\ge j}
\big(
\eta_{P12,j,k}
+\eta_{appLC,j,k}^{(12)}
+\eta_{binLC,j,k}^{(12)}
\big)\to0,
```

the exact-comparison discrepancy satisfies

```math
X_{13,j}^{exact,SEL2}\to0,
```

and the Paper-14 export is exact on the frozen `SEL2` battery, or else has
vanishing trace-norm export defect:

```math
\|E_{14}(\eta_j)\|_{tr}\to0.
```

Then the reduced easy-zero transport ceilings are

```math
U_{12}^{per}=U_{12}^{cusp}=U_{12}^{smear}=U_{12}^{app}
=U_{13}^{exact}=U_{14}=0.
```

If the selected branch also keeps endpoint/corner normalization inside the
decoration ledger, then

```math
U_{corn}=0.
```

Therefore the nonsurface pre-`T_13` upper bound reduces to

```math
U_{pre13}^{SEL2}
=
U_{11}^{loc}+U_{11}^{RP}+U_{11}^{Cov}+U_{11}^{gauge}
+U_{13}^{entry}
```

in the no-corner branch, and to the same expression plus `U_corn` otherwise.

Proof.

The first four displayed vanishing assumptions are exactly the zero branch of
Theorem 4.3A.60, hence they force the four reduced `T_12` ceilings to vanish.
The convergence `X_{13,j}^{exact,SEL2}->0` is the zero branch of Theorem
4.3A.61, hence `U_13^{exact}=0`. The exact or trace-norm-vanishing Paper-14
export assumption is the zero branch of Theorem 4.3A.62, hence `U_14=0`.
Substituting these identities into Theorem 4.3A.65 gives the reduced expression
for `U_pre13^SEL2`; the endpoint/corner clause is precisely the final optional
zero clause in Theorem 4.3A.60. `square`

### Corollary 4.3A.67: Easy-Zero Pre-Surface Pass Test

Assume the hypotheses of Corollary 4.3A.66. If

```math
U_{11}^{loc}+U_{11}^{RP}+U_{11}^{Cov}+U_{11}^{gauge}
+U_{13}^{entry}
<
\underline M_{loss}^{SEL2,20}
```

in the no-corner branch, then

```math
\mathcal M_{pre13}^{SEL2}>0.
```

In the branch with a separate endpoint/corner debit, replace the left side by

```math
U_{11}^{loc}+U_{11}^{RP}+U_{11}^{Cov}+U_{11}^{gauge}
+U_{corn}+U_{13}^{entry}.
```

Proof.

Corollary 4.3A.66 identifies the easy-zero ceilings and reduces
`U_pre13^SEL2` to the displayed residual sum. Theorem 4.3A.65 then gives
`P20-SEL2-NS-UPPER(U_pre13^SEL2)`, and Theorem 4.3A.58 converts the strict
aggregate inequality into the positive pre-surface margin. `square`

### Corollary 4.3A.68: Aggregate Pre-Surface Bound Computation

Assume the component bounds in Definition 4.3A.57 have been declared on the
same frozen `SEL2` record law. Set

```math
U_{11}^{\Sigma}
:=
U_{11}^{loc}+U_{11}^{RP}+U_{11}^{Cov}+U_{11}^{gauge},
```

```math
U_{12}^{\Sigma}
:=
U_{12}^{per}+U_{12}^{cusp}+U_{12}^{smear}+U_{12}^{app}.
```

Then the aggregate nonsurface upper bound is

```math
U_{pre13}^{SEL2}
=
U_{11}^{\Sigma}
+U_{12}^{\Sigma}
+U_{corn}
+U_{14}
+U_{13}^{entry}
+U_{13}^{exact}.
```

Equivalently, expanded without abbreviations,

```math
U_{pre13}^{SEL2}
=
U_{11}^{loc}+U_{11}^{RP}+U_{11}^{Cov}+U_{11}^{gauge}
+U_{12}^{per}+U_{12}^{cusp}+U_{12}^{smear}+U_{12}^{app}
+U_{corn}+U_{14}+U_{13}^{entry}+U_{13}^{exact}.
```

Define the computed aggregate surplus

```math
\Pi_{pre13}^{SEL2}
:=
\underline M_{loss}^{SEL2,20}
-U_{pre13}^{SEL2}.
```

Using the frozen worksheet of Definition 4.3A.43, this is the explicit scalar

```math
\Pi_{pre13}^{SEL2}
=
\exp(L_{20})
-\exp\!\left({20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}\right)
-U_{pre13}^{SEL2}.
```

Therefore:

1. if `Pi_pre13^SEL2>0`, then the pre-surface margin is positive;
2. if `Pi_pre13^SEL2<=0`, the current upper-bound package does not certify the
   branch, but does not by itself falsify it;
3. genuine pre-surface falsification still requires a same-record lower floor
   `L_pre13^{SEL2,-}>=underline M_loss^{SEL2,20}` as in Theorem 4.3A.47.

In the easy-zero branch of Corollary 4.3A.66,

```math
U_{pre13}^{SEL2}
=
U_{11}^{\Sigma}+U_{13}^{entry}
```

if endpoint/corner normalization remains inside decoration, and

```math
U_{pre13}^{SEL2}
=
U_{11}^{\Sigma}+U_{corn}+U_{13}^{entry}
```

if endpoint/corner normalization is charged separately.

Proof.

The first displayed identity is Theorem 4.3A.65 with the four `T_11` entries
collected into `U_11^Sigma` and the four reduced `T_12` entries collected into
`U_12^Sigma`. Definition 4.3A.38 gives

```math
\underline M_{loss}^{SEL2,20}
=
\exp(L_{20})
-\exp\!\left({20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}\right),
```

so subtracting `U_pre13^SEL2` gives the formula for
`Pi_pre13^SEL2`. The pass implication is Theorem 4.3A.58. The non-falsification
clause is Theorem 4.3A.47: an insufficient upper ceiling is not a lower-bound
obstruction. The easy-zero identities substitute
`U_12^Sigma=U_14=U_13^{exact}=0` from Corollary 4.3A.66, with the optional
corner convention handled by that same corollary. `square`

### Theorem 4.3A.69: Easy-Zero Attempt And Honest Decision

Assume the standard frozen unit-normalized `SEL2` branch of Theorem 4.3A.51,
the common-record audit `P20-SEL2-TR-COMMON`, and the source package
`P20-SEL2-TRANSPORT-SRC`. Then the following are the exact zero tests for the
easy-zero components.

1. The reduced perimeter and cusp debits vanish exactly under the evaluated
   calibrated-tail test

   ```math
   \limsup_j\sum_{k\ge j}\eta_{perLC,j,k}=0,
   \qquad
   \limsup_j\sum_{k\ge j}\eta_{cuspLC,j,k}=0.
   ```

   In particular, cofinal stationarity of the calibrated perimeter/cusp
   counterterm branches on every finite loop battery is sufficient.

2. The reduced smearing debit vanishes exactly under the evaluated
   smearing-tail test

   ```math
   \limsup_j\sum_{k\ge j}\eta_{smearLC,j,k}=0,
   ```

   with the Paper-12 local subtraction schedule kept inside the same loop
   collar.

3. The reduced loop-approximant/readout debit vanishes exactly under

   ```math
   \limsup_j\sum_{k\ge j}
   \left(
   \eta_{P12,j,k}
   +\eta_{appLC,j,k}^{(12)}
   +\eta_{binLC,j,k}^{(12)}
   \right)=0.
   ```

4. The exact-comparison debit vanishes exactly under

   ```math
   X_{13,j}^{exact,SEL2}\to0,
   ```

   equivalently: the cutoff block records converge exactly on every finite
   scalar `SEL2` battery used by the row-`j` surface-entry proof and
   `epsilon_{read,j}^{(13,SEL2)}->0`.

5. The Paper-14 export debit vanishes exactly under

   ```math
   \|E_{14}(\eta_j)\|_{tr}\to0.
   ```

   A finite Paper-14 ceiling alone, `limsup_j||E_14(eta_j)||_tr<infinity`,
   is not enough to set `U_14=0`.

Consequently, on the standard `SEL2` branch, the current papers prove the
easy-zero identities

```math
U_{12}^{per}=U_{12}^{cusp}=U_{12}^{smear}=U_{12}^{app}
=U_{13}^{exact}=U_{14}=0
```

if and only if the five displayed cofinal zero tests hold on the same pushed-
forward scalar record law. The existing common-record and transport source
audits reduce the question to these tests; they do not by themselves prove the
tests.

For the endpoint/corner term, the standard `SEL2` branch is corner-separated:
endpoint/corner loop-readout effects are moved out of the multiplicative
decoration register and charged only to `T_12`. Therefore the standard branch
may set

```math
U_{corn}=E_{corn}^{SEL2},
```

but may set `U_corn=0` only if either

```math
E_{corn}^{SEL2}=0
```

is proved on the same scalar record law, or a different no-corner selector is
declared and its decoration constant is re-audited with endpoint/corner
normalization kept inside decoration.

Thus the honest outcome of the easy-zero attempt is:

```text
Easy-zero is conditionally available, but not unconditionally proved by the
current Paper-12/14/16/19 imports.
```

The next non-formal work is to prove or falsify the five displayed cofinal
zero tests, plus the endpoint/corner zero test if the standard corner-separated
`SEL2` branch is retained.

Proof.

The first three zero tests are exactly Paper 19 Definition 8L.11A.21A and
Theorems 8L.11A.21B--8L.11A.21E, pulled back to the frozen `SEL2` record law
by `P20-SEL2-TR-COMMON`. The fourth test is Paper 19 Definition 8L.11A.25
and Theorem 4.3A.61. The fifth test is Paper 19 Definition 8L.11A.3 and
Theorem 4.3A.62. Each displayed quantity is nonnegative, so a zero limsup is
both the natural sufficient condition and, for the evaluated ceilings chosen
in this paper, the exact way the declared ceiling becomes zero.

The endpoint/corner statement is Definition 1.10 clause 3 together with
Definition 4.3A.36 clause 3 and Definition 4.3A.38: the standard `SEL2`
selector deliberately keeps endpoint/corner collars outside the multiplicative
decoration register and assigns them to the loop-readout debit. Setting
`U_corn=0` without one of the two stated additional facts would either erase a
declared debit or move it into decoration without redoing the decoration
constant audit. `square`

### Definition 4.3A.70: Evaluated Reduced `T_11` Ceilings On `SEL2`

Assume `P20-SEL2-TR-COMMON`. The evaluated reduced `T_11` ceilings on the
frozen `SEL2` scalar record law are the four limsup tails

```math
U_{11}^{loc,eval}
:=
\limsup_j
\sum_{k\ge j}
L_j^{rec}
\left(
\eta_{locRG,k}^{B_j}
+\eta_{prec,j,k}^{(11)}
\right),
```

```math
U_{11}^{RP,eval}
:=
\limsup_j
\sum_{k\ge j}
\left(
\eta_{binRP,j,k}^{(11)}
+\eta_{projRP,j,k}^{(11)}
+\eta_{regRP,j,k}^{(11)}
+\eta_{volRP,j,k}^{(11)}
+\eta_{ctRP,j,k}^{(11,red)}
\right),
```

```math
U_{11}^{Cov,eval}
:=
\limsup_j
\sup_{g\in Euc_{adm}(B_j)}
\sum_{k\ge j}
\left(
\eta_{exactCov,j,k}(g)
+\eta_{appCov,j,k}^{(11)}(g)
+\eta_{binCov,j,k}^{(11)}(g)
+\eta_{blockCov,j,k}^{(11)}(g)
+\eta_{projCov,j,k}^{(11)}(g)
+\eta_{regCov,j,k}^{(11)}(g)
+\eta_{volCov,j,k}^{(11)}(g)
+\eta_{ctCov,j,k}^{(11,red)}(g)
\right),
```

and

```math
U_{11}^{gauge,eval}
:=
\limsup_j
\sum_{k\ge j}
\left(
\eta_{chart,j,k}^{(11)}
+\eta_{gauge-rec,j,k}^{(11)}
\right).
```

The reduced-label convention is part of the definition:

1. `eta_ctRP^{(11,red)}` and `eta_ctCov^{(11,red)}` have already had the
   perimeter/cusp singular transports removed; those transports belong only to
   reduced `T_12`.
2. `eta_appCov^{(11)}` is an admissible Euclidean-motion approximant defect,
   not the loop-readout approximant defect `eta_appLC^{(12)}`.
3. projective, regulator/chart, finite-volume, block/collar, and precision
   terms appearing here are not also charged to reduced `T_12`, reduced
   `T_13`, `T_14`, or the decoration debit.
4. no Paper-14 whole-process export term is included here; that term is
   exactly `U_14`.

If all four right-hand sides are finite, set

```math
U_{11}^{loc}:=U_{11}^{loc,eval},
\quad
U_{11}^{RP}:=U_{11}^{RP,eval},
\quad
U_{11}^{Cov}:=U_{11}^{Cov,eval},
\quad
U_{11}^{gauge}:=U_{11}^{gauge,eval}.
```

If any right-hand side is infinite, the reduced `T_11` source route does not
certify the frozen `SEL2` branch.

### Theorem 4.3A.71: Reduced `T_11` Block Bound And Zero Decision

Assume `P20-SEL2-TR-COMMON`, `P20-SEL2-TRANSPORT-SRC`, and the evaluated
finite ceilings of Definition 4.3A.70. Then the surviving reduced `T_11`
block is bounded by

```math
U_{11}^{\Sigma}
\le
U_{11}^{loc,eval}
+U_{11}^{RP,eval}
+U_{11}^{Cov,eval}
+U_{11}^{gauge,eval}.
```

With the evaluated choice in Definition 4.3A.70, equality holds in the
declared upper-bound package:

```math
U_{11}^{\Sigma}
=
U_{11}^{loc,eval}
+U_{11}^{RP,eval}
+U_{11}^{Cov,eval}
+U_{11}^{gauge,eval}.
```

The reduced `T_11` block vanishes on the frozen `SEL2` record law if and only
if the following four evaluated zero tests hold:

```math
\sum_{k\ge j}
L_j^{rec}
\left(
\eta_{locRG,k}^{B_j}
+\eta_{prec,j,k}^{(11)}
\right)
\to0,
```

```math
\sum_{k\ge j}
\left(
\eta_{binRP,j,k}^{(11)}
+\eta_{projRP,j,k}^{(11)}
+\eta_{regRP,j,k}^{(11)}
+\eta_{volRP,j,k}^{(11)}
+\eta_{ctRP,j,k}^{(11,red)}
\right)
\to0,
```

```math
\sup_{g\in Euc_{adm}(B_j)}
\sum_{k\ge j}
\left(
\eta_{exactCov,j,k}(g)
+\eta_{appCov,j,k}^{(11)}(g)
+\eta_{binCov,j,k}^{(11)}(g)
+\eta_{blockCov,j,k}^{(11)}(g)
+\eta_{projCov,j,k}^{(11)}(g)
+\eta_{regCov,j,k}^{(11)}(g)
+\eta_{volCov,j,k}^{(11)}(g)
+\eta_{ctCov,j,k}^{(11,red)}(g)
\right)
\to0,
```

and

```math
\sum_{k\ge j}
\left(
\eta_{chart,j,k}^{(11)}
+\eta_{gauge-rec,j,k}^{(11)}
\right)
\to0.
```

Under these four tests,

```math
U_{11}^{loc}=U_{11}^{RP}=U_{11}^{Cov}=U_{11}^{gauge}=0,
\qquad
U_{11}^{\Sigma}=0.
```

The current Paper-16/Paper-19 imports prove the reduction to these four tests.
They do not automatically prove the tests unless the corresponding
record-sensitivity weighted local-RG tail, RP transport tail, uniform
Euclidean-covariance transport tail, and scalar gauge/chart reconstruction
tail are shown to vanish on the same frozen `SEL2` record law.

Proof.

Paper 19 Definition 8L.11A.5 defines the four reduced `T_11` tails
`R_11^loc`, `R_11^RP`, `R_11^Cov`, and `R_11^gauge`. Paper 19 Definitions
8L.11A.13, 8L.11A.15A, 8L.11A.15B, and 8L.11A.15C identify those tails with
the Paper-11/Paper-16 local-RG, RP, covariance, and gauge/chart source
attacks, after the debit register removes perimeter/cusp, loop-readout,
surface-entry, decoration, and Paper-14 terms. Paper 19 Theorem 8L.11A.15D
then gives

```math
\limsup_jT_{11,j}^{SEL2}
\le
A_{11}^{loc,SEL2}
+A_{11}^{RP,SEL2}
+A_{11}^{Cov,SEL2}
+A_{11}^{gauge,SEL2}.
```

Substituting the evaluated `SEL2` limsups of Definition 4.3A.70 gives the
displayed bound and the evaluated equality in the declared upper-bound
package. Since each summand is nonnegative, all four evaluated ceilings vanish
exactly when the four displayed cofinal tails vanish. The final sentence is
the no-smuggling boundary: common-record compatibility identifies the tests,
but only the actual vanishing estimates make the debits zero. `square`

### Definition 4.3A.72: Evaluated Exact-Entry Ceiling On `SEL2`

Assume `P20-SEL2-TR-COMMON`. The evaluated exact-entry residuals on the frozen
`SEL2` scalar record law are

```math
U_{13}^{BC,eval}
:=
\limsup_j\epsilon_{BC,j}^{SEL2},
\qquad
U_{13}^{CE,eval}
:=
\limsup_j\epsilon_{CE,j}^{SEL2},
```

```math
U_{13}^{RPF,eval}
:=
\limsup_j\epsilon_{RPF,j}^{SEL2},
\qquad
U_{13}^{KPdec,eval}
:=
\limsup_j\epsilon_{KPdec,j}^{SEL2},
```

and

```math
U_{13}^{SUB,eval}
:=
\limsup_j\epsilon_{SUB,j}^{SEL2},
\qquad
U_{13}^{WP,eval}
:=
\limsup_j\epsilon_{WP,j}^{SEL2}.
```

The evaluated aggregate exact-entry ceiling is

```math
U_{13}^{entry,eval}
:=
U_{13}^{BC,eval}
+U_{13}^{CE,eval}
+U_{13}^{RPF,eval}
+U_{13}^{KPdec,eval}
+U_{13}^{SUB,eval}
+U_{13}^{WP,eval}.
```

When all six component limsups are finite, set

```math
U_{13}^{entry}:=U_{13}^{entry,eval}.
```

The six entries have the following ledger meanings.

1. `BC` is block convergence on the actual finite `SEL2` block records.
2. `CE` is central-character extraction for the exact-entry chain. It is not
   the later leading-rate constant `kappa_13^CE`.
3. `RPF` is residual factorization for the same pushed-forward scalar records.
4. `KPdec` is the exact-entry decoration/KP comparison residual. It is not the
   already-paid multiplicative decoration debit `D_dec^{SEL2,20}` and may not
   recharge character-tail activity.
5. `SUB` is surface-subcriticality transport. On the preferred reduced route,
   where subcriticality is charged only through `P19-T13-SUB` and the later
   leading-rate threshold, set `epsilon_{SUB,j}^{SEL2}=0` in this entry bucket.
   If a branch instead pays a finite `SUB` comparison here, the same term may
   not also be charged in the surface bucket.
6. `WP` is whole-process compatibility for the Paper-13 actual-entry chain.
   It is not the Paper-14 export norm `E_14`.

If any component limsup is infinite, the exact-entry source route does not
certify the frozen `SEL2` branch.

### Theorem 4.3A.73: Exact-Entry Bound And Zero Decision

Assume `P20-SEL2-TR-COMMON`, `P20-SEL2-TRANSPORT-SRC`, and the finite
evaluated residuals of Definition 4.3A.72. Then the exact-entry component of
`P20-SEL2-NS-UPPER` is closed with

```math
A_{13}^{entry,SEL2}
\le
U_{13}^{entry}
=
U_{13}^{BC,eval}
+U_{13}^{CE,eval}
+U_{13}^{RPF,eval}
+U_{13}^{KPdec,eval}
+U_{13}^{SUB,eval}
+U_{13}^{WP,eval}.
```

Equivalently, by limsup subadditivity,

```math
A_{13}^{entry,SEL2}
\le
\limsup_j\epsilon_{BC,j}^{SEL2}
+\limsup_j\epsilon_{CE,j}^{SEL2}
+\limsup_j\epsilon_{RPF,j}^{SEL2}
+\limsup_j\epsilon_{KPdec,j}^{SEL2}
+\limsup_j\epsilon_{SUB,j}^{SEL2}
+\limsup_j\epsilon_{WP,j}^{SEL2}.
```

The exact-entry debit vanishes on the frozen `SEL2` record law if the six
entry residuals vanish cofinally:

```math
\epsilon_{BC,j}^{SEL2}\to0,\quad
\epsilon_{CE,j}^{SEL2}\to0,\quad
\epsilon_{RPF,j}^{SEL2}\to0,\quad
\epsilon_{KPdec,j}^{SEL2}\to0,\quad
\epsilon_{SUB,j}^{SEL2}\to0,\quad
\epsilon_{WP,j}^{SEL2}\to0.
```

In the preferred reduced route, the fifth condition is replaced by the
disjoint-debit convention

```math
\epsilon_{SUB,j}^{SEL2}=0
```

inside the entry bucket, because subcriticality is handled by the surface
leading-rate test. Under these clauses,

```math
U_{13}^{entry}=0.
```

The current Paper-13/Paper-19 imports prove the reduction to these component
residuals. They do not automatically prove that the residuals vanish or are
small enough; that requires same-record estimates for block convergence,
central extraction, residual factorization, entry-level KP/decorrelation,
subcriticality placement, and whole-process compatibility on the frozen
`SEL2` tower.

Proof.

Paper 19 Definition 8L.11A.24 defines

```math
E_{13,j}^{entry}
=
\epsilon_{BC,j}
+\epsilon_{CE,j}
+\epsilon_{RPF,j}
+\epsilon_{KPdec,j}
+\epsilon_{SUB,j}
+\epsilon_{WP,j}
```

and proves `R_{13,j}^{entry}<=E_{13,j}^{entry}` after all losses assigned to
`T_11`, reduced `T_12`, `T_14`, and the decoration ledger have been removed.
Substituting the frozen `SEL2` record law gives the six displayed residuals.
Taking limsup and using subadditivity gives the aggregate upper bound. If all
component residuals vanish cofinally, the aggregate limsup is zero. The
`SUB`, `KPdec`, and `WP` conventions are exactly the disjoint-debit clauses in
Paper 19 Definition 8L.11A.24 and `P20-SEL2-TR-COMMON`: subcriticality,
decoration activity, and Paper-14 export may each have only one ledger home.
`square`

### Corollary 4.3A.74: Easy-Zero Tail Decision On The Standard `SEL2` Branch

Assume the standard frozen unit-normalized branch
`P20-SEL2(eta_{ch,20}^{SEL2},20)`, `P20-SEL2-TR-COMMON`, and
`P20-SEL2-TRANSPORT-SRC`. With only the source estimates currently imported
from Papers 12, 14, 16, and 19, the easy-zero tails are decided as follows.

| Slot | Current standard-branch decision | Extra estimate that would make it zero |
| --- | --- | --- |
| `U_12^{per}` | carry as `A_12^{per,eval,SEL2}` | `limsup_j sum_{k>=j} eta_{perLC,j,k}=0` |
| `U_12^{cusp}` | carry as `A_12^{cusp,eval,SEL2}` | `limsup_j sum_{k>=j} eta_{cuspLC,j,k}=0` |
| `U_12^{smear}` | carry as `A_12^{smear,eval,SEL2}` | `limsup_j sum_{k>=j} eta_{smearLC,j,k}=0` |
| `U_12^{app}` | carry as `A_12^{app,eval,SEL2}` | `limsup_j sum_{k>=j}(eta_{P12,j,k}+eta_{appLC,j,k}^{(12)}+eta_{binLC,j,k}^{(12)})=0` |
| `U_13^{exact}` | carry as `limsup_j X_{13,j}^{exact,SEL2}` | `X_{13,j}^{exact,SEL2}->0` |
| `U_14` | carry as `E_14^{SEL2}` | `||E_14(eta_j)||_{tr}->0` or exact Paper-14 export |
| `U_corn` | carry as `E_corn^{SEL2}` | `E_corn^{SEL2}=0`, or a new no-corner selector with a re-audited decoration constant |

Thus the standard `SEL2` branch cannot presently use

```math
U_{12}^{per}=U_{12}^{cusp}=U_{12}^{smear}=U_{12}^{app}
=U_{13}^{exact}=U_{14}=U_{corn}=0
```

as proved input. The correct aggregate bound for the standard branch remains

```math
U_{pre13}^{SEL2}
=
U_{11}^{\Sigma}
+A_{12}^{per,eval,SEL2}
+A_{12}^{cusp,eval,SEL2}
+A_{12}^{smear,eval,SEL2}
+A_{12}^{app,eval,SEL2}
+E_{corn}^{SEL2}
+E_{14}^{SEL2}
+U_{13}^{entry}
+\limsup_jX_{13,j}^{exact,SEL2},
```

with any term replaced by zero only after the corresponding estimate in the
right column of the table has been proved on the same pushed-forward scalar
record law.

This is a rejection of the unconditional easy-zero shortcut for the standard
`SEL2` branch. It is not a falsification of the actual zero estimates
themselves; those estimates remain independent source problems.

Proof.

The four `U_12` rows are Paper 19 Definition 8L.11A.21A and Theorems
8L.11A.21B--8L.11A.21E, imported in Theorem 4.3A.60. Those results evaluate
the four reduced loop-readout tails, and they set them to zero only under the
displayed cofinal vanishing tests. The current `P20-SEL2-TRANSPORT-SRC`
imports `P19-T12-EVAL` and the three `T_12` attacks, but it does not include
those zero tests.

The `U_13^{exact}` row is Theorem 4.3A.61: the current import gives the
finite ceiling `limsup_j X_{13,j}^{exact,SEL2}`, and zero requires actual
convergence of that discrepancy to zero. The `U_14` row is Theorem 4.3A.62:
`P19-P14-EXPORT(E_14^{SEL2})` gives a finite Paper-14 transport ceiling, and
zero requires exact export or vanishing transport norm. The `U_corn` row is
Definition 1.10 clause 3, Definition 4.3A.36 clause 3, and Definition
4.3A.38: the standard `SEL2` branch is corner-separated and charges the
endpoint/corner debit in `T_12`. Therefore `U_corn` must remain unless its
declared scalar value is proved zero or the selector is changed and the
decoration audit is redone. `square`

### Corollary 4.3A.75: Computed Standard `SEL2` Pre-Surface Surplus

Assume the standard frozen unit-normalized branch
`P20-SEL2(eta_{ch,20}^{SEL2},20)`, `P20-SEL2-TR-COMMON`,
`P20-SEL2-TRANSPORT-SRC`, and the evaluated component ceilings of Definitions
4.3A.70 and 4.3A.72. Use the standard-branch easy-zero decision of Corollary
4.3A.74, so the easy-zero terms are carried unless their separate zero
estimates have been proved.

Define the standard carried nonsurface ceiling

```math
U_{pre13,std}^{SEL2}
:=
U_{11}^{loc,eval}
+U_{11}^{RP,eval}
+U_{11}^{Cov,eval}
+U_{11}^{gauge,eval}
+A_{12}^{per,eval,SEL2}
+A_{12}^{cusp,eval,SEL2}
+A_{12}^{smear,eval,SEL2}
+A_{12}^{app,eval,SEL2}
+E_{corn}^{SEL2}
+E_{14}^{SEL2}
+U_{13}^{BC,eval}
+U_{13}^{CE,eval}
+U_{13}^{RPF,eval}
+U_{13}^{KPdec,eval}
+U_{13}^{SUB,eval}
+U_{13}^{WP,eval}
+\limsup_jX_{13,j}^{exact,SEL2}.
```

On the preferred reduced route, where subcriticality is charged only through
the surface leading-rate test, replace `U_13^{SUB,eval}` by `0`.

The computed standard pre-surface surplus is

```math
\Pi_{pre13,std}^{SEL2}
:=
\exp(L_{20})
-\exp\!\left({20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}\right)
-U_{pre13,std}^{SEL2}.
```

If

```math
\Pi_{pre13,std}^{SEL2}>0,
```

then the standard `SEL2` branch is certified past the pre-surface stage:

```math
\mathcal M_{pre13}^{SEL2}
\ge
\Pi_{pre13,std}^{SEL2}
>0.
```

Consequently the branch reaches the final `T_13` leading-rate test. A
sufficient final leading-rate condition is then

```math
\kappa_{13}^{CE}
>
h_{13}^{SEL2}
+d_{13}^{SEL2,20}
+\log\!\left(
1+{M_{13}^{surf,SEL2}\over\Pi_{pre13,std}^{SEL2}}
\right).
```

If

```math
\Pi_{pre13,std}^{SEL2}\le0,
```

then the present standard-branch upper package does not certify the
pre-surface margin. This is not a falsification unless a same-record lower
floor proves

```math
L_{pre13}^{SEL2,-}
\ge
\underline M_{loss}^{SEL2,20}.
```

Proof.

Corollary 4.3A.74 supplies the carried standard-branch values for the reduced
`T_12`, endpoint/corner, Paper-14, and exact-comparison terms. Definition
4.3A.70 and Theorem 4.3A.71 supply the evaluated reduced `T_11` block.
Definition 4.3A.72 and Theorem 4.3A.73 supply the evaluated exact-entry
ceiling. Substituting these values into Corollary 4.3A.68 gives
`U_pre13,std^SEL2`.

The post-decoration margin is Definition 4.3A.38:

```math
\underline M_{loss}^{SEL2,20}
=
\exp(L_{20})
-\exp\!\left({20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}\right).
```

Subtracting the carried nonsurface ceiling gives the displayed
`Pi_pre13,std^SEL2`. Since the actual nonsurface debit is bounded above by
`U_pre13,std^SEL2`, the actual pre-surface margin is bounded below by
`Pi_pre13,std^SEL2`. Positivity therefore certifies the branch through the
pre-surface stage. The leading-rate threshold is Theorem 4.3A.39 with the
certified lower margin `Pi_pre13,std^SEL2` substituted for the available
pre-surface margin. The non-falsification clause is Theorem 4.3A.47. `square`

### Definition 4.3A.76: Frozen Standard Reduced `SEL2` Branch

`P20-SEL2-STDRED` is the following branch convention.

1. The frozen selector is the unit-normalized activity-optimized selector

   ```math
   P20\text{-}SEL2(\eta_{ch,20}^{SEL2},20).
   ```

   Thus the area-collar constant is the audited finite-template value
   `C_area=20`, and the decoration debit is exactly

   ```math
   D_{dec}^{SEL2,20}
   =
   \exp\!\left({20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}\right)-1.
   ```

2. The branch uses `P20-SEL2-TR-COMMON`, so all coefficient, decoration,
   reduced loop-readout, Paper-14 export, `T_11`, exact-entry, and
   cutoff-to-exact scalar records are evaluated on the same pushed-forward
   scalar record law.

3. Endpoint and corner collars are corner-separated. They are not hidden in
   the multiplicative decoration constant. Their standard debit is
   `E_corn^{SEL2}` in the reduced loop-readout side of the nonsurface
   transport ledger.

4. The easy-zero tails of Corollary 4.3A.74 are carried unless their separate
   same-record zero tests are proved. In particular the standard branch
   carries

   ```math
   A_{12}^{per,eval,SEL2},\quad
   A_{12}^{cusp,eval,SEL2},\quad
   A_{12}^{smear,eval,SEL2},\quad
   A_{12}^{app,eval,SEL2},\quad
   E_{corn}^{SEL2},\quad
   E_{14}^{SEL2},\quad
   \limsup_jX_{13,j}^{exact,SEL2}.
   ```

5. On the reduced route, the exact-entry subcriticality residual is not
   charged in the entry bucket:

   ```math
   U_{13}^{SUB,eval}=0.
   ```

   This is allowed only because the surface subcriticality cost is paid later
   in the final `T_13` leading-rate inequality. If that later payment is not
   used, then `U_13^{SUB,eval}` must be restored in the entry bucket.

This convention is a ledger assignment, not a physical assumption. It contains
no Wilson-loop area law, no continuum Yang-Mills measure, no positivity of
`kappa_13^{CE}`, and no assertion that any carried tail vanishes.

### Definition 4.3A.77: Five-Bucket Pre-Surface Ceiling On `P20-SEL2-STDRED`

On `P20-SEL2-STDRED`, define the carried easy-zero bucket

```math
U_{EZ}^{SEL2}
:=
A_{12}^{per,eval,SEL2}
+A_{12}^{cusp,eval,SEL2}
+A_{12}^{smear,eval,SEL2}
+A_{12}^{app,eval,SEL2}
+E_{corn}^{SEL2}
+E_{14}^{SEL2}
+\limsup_jX_{13,j}^{exact,SEL2}.
```

Define the reduced `T_11` bucket

```math
U_{11}^{red,SEL2}
:=
U_{11}^{loc,eval}
+U_{11}^{RP,eval}
+U_{11}^{Cov,eval}
+U_{11}^{gauge,eval}.
```

Define the reduced exact-entry bucket

```math
U_{13}^{entry,red,SEL2}
:=
U_{13}^{BC,eval}
+U_{13}^{CE,eval}
+U_{13}^{RPF,eval}
+U_{13}^{KPdec,eval}
+U_{13}^{WP,eval}.
```

The unreduced entry variant is obtained by replacing
`U_13^{entry,red,SEL2}` with

```math
U_{13}^{entry,full,SEL2}
:=
U_{13}^{entry,red,SEL2}+U_{13}^{SUB,eval}.
```

The standard reduced nonsurface ceiling is

```math
U_{pre13,std,red}^{SEL2}
:=
U_{EZ}^{SEL2}
+U_{11}^{red,SEL2}
+U_{13}^{entry,red,SEL2}.
```

The corresponding post-decoration scalar surplus is

```math
\Pi_{pre13,std,red}^{SEL2}
:=
\exp(L_{20})
-\exp\!\left({20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}\right)
-U_{pre13,std,red}^{SEL2}.
```

Equivalently,

```math
\Pi_{pre13,std,red}^{SEL2}
=
\underline M_{loss}^{SEL2,20}
-U_{EZ}^{SEL2}
-U_{11}^{red,SEL2}
-U_{13}^{entry,red,SEL2}.
```

### Theorem 4.3A.78: Five-Step Pre-Surface Computation

Assume `P20-SEL2-STDRED`, the source imports of
`P20-SEL2-TRANSPORT-SRC`, and the evaluated ceilings of Definitions 4.3A.70
and 4.3A.72. Then the five-step pre-surface computation is as follows.

1. **Branch fixed.** The only active branch is
   `P20-SEL2(eta_ch,20^SEL2,20)` with the corner-separated standard reduced
   ledger of Definition 4.3A.76.

2. **Easy-zero survivors evaluated.** The easy-zero survivors are exactly the
   bucket `U_EZ^{SEL2}` of Definition 4.3A.77. Current imports do not prove
   `U_EZ^{SEL2}=0`; they prove only the carried finite ceiling and the
   separate zero tests of Corollary 4.3A.74.

3. **Reduced `T_11` evaluated.** The surviving `T_11` contribution is exactly
   `U_11^{red,SEL2}`. Current imports do not prove this bucket is zero; they
   reduce zero to the four cofinal vanishing tests of Theorem 4.3A.71.

4. **Reduced exact-entry evaluated.** The entry contribution on the reduced
   route is exactly `U_13^{entry,red,SEL2}`. Current imports do not prove this
   bucket is zero; they reduce zero to the `BC`, `CE`, `RPF`, `KPdec`, and
   `WP` cofinal residual tests in Theorem 4.3A.73. The `SUB` residual is
   absent only because the branch pays subcriticality in the final
   leading-rate test.

5. **Scalar sign test.** The branch is certified through the pre-surface
   stage if and only if the available upper package proves

   ```math
   U_{EZ}^{SEL2}
   +U_{11}^{red,SEL2}
   +U_{13}^{entry,red,SEL2}
   <
   \exp(L_{20})
   -\exp\!\left({20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}\right).
   ```

   Equivalently,

   ```math
   \Pi_{pre13,std,red}^{SEL2}>0.
   ```

If this strict inequality holds, the final remaining confinement-side source
test is the `T_13` leading-rate inequality

```math
\kappa_{13}^{CE}
>
h_{13}^{SEL2}
+d_{13}^{SEL2,20}
+\log\!\left(
1+{M_{13}^{surf,SEL2}\over\Pi_{pre13,std,red}^{SEL2}}
\right).
```

If the strict inequality is not proved, the standard reduced `SEL2` branch is
not certified past the pre-surface stage by the present upper package. This is
not a falsification of the route unless same-record lower bounds prove that
the actual nonsurface debit consumes the whole post-decoration margin.

Proof.

Step 1 is Definition 4.3A.76. Step 2 is Corollary 4.3A.74 with the surviving
terms grouped as `U_EZ^{SEL2}`. Step 3 is Definition 4.3A.70 and Theorem
4.3A.71. Step 4 is Definition 4.3A.72 and Theorem 4.3A.73, with the
subcriticality convention specified in Definition 4.3A.76 clause 5. Adding
the three nonnegative buckets gives `U_pre13,std,red^SEL2`. Subtracting that
ceiling from the post-decoration margin `underline M_loss^{SEL2,20}` gives
`Pi_pre13,std,red^SEL2`. The positive-margin implication is Theorem 4.3A.39
with the certified lower margin substituted into the surface-tail threshold.
The non-falsification clause is Theorem 4.3A.47. `square`

### Corollary 4.3A.79: Present Decision Of Steps 1--5

Steps 1--4 are now complete as reductions on the standard reduced `SEL2`
branch: every nonsurface term has a unique same-record bucket and no debit is
charged twice. Step 5 is not numerically or symbolically decided by the
current imports, because the following strict aggregate inequality remains an
external source estimate:

```math
U_{EZ}^{SEL2}
+U_{11}^{red,SEL2}
+U_{13}^{entry,red,SEL2}
<
\underline M_{loss}^{SEL2,20}.
```

Thus Paper 20 may proceed in exactly one of two honest ways.

1. Prove sharper same-record upper bounds for the three buckets on the left
   until the inequality is strict.
2. Prove a same-record lower floor for the actual nonsurface debit at or above
   `underline M_loss^{SEL2,20}`, thereby falsifying this standard reduced
   `SEL2` branch.

Without one of those two additional estimates, the branch remains
pre-surface-undecided and cannot honestly be advanced to an unconditional
confinement theorem.

### Definition 4.3A.80: Priority-Ordered `U_EZ^{SEL2}` Attack Worksheet

On `P20-SEL2-STDRED`, split the easy-zero bucket into the requested priority
order:

```math
U_{EZ}^{SEL2}
=
U_{EZ,014}^{SEL2}
+U_{EZ,12}^{SEL2},
```

where the first block contains the Paper-14, endpoint/corner, and
cutoff-to-exact scalar terms

```math
U_{EZ,014}^{SEL2}
:=
E_{14}^{SEL2}
+E_{corn}^{SEL2}
+X_{13}^{exact,SEL2},
\qquad
X_{13}^{exact,SEL2}:=\limsup_jX_{13,j}^{exact,SEL2},
```

and the second block contains the four reduced loop-readout tails

```math
U_{EZ,12}^{SEL2}
:=
A_{12}^{per,eval,SEL2}
+A_{12}^{cusp,eval,SEL2}
+A_{12}^{smear,eval,SEL2}
+A_{12}^{app,eval,SEL2}.
```

The evaluated `T_12` subconstants are

```math
A_{12}^{per,eval,SEL2}
:=
\limsup_j\sum_{k\ge j}\eta_{perLC,j,k}^{SEL2},
\qquad
A_{12}^{cusp,eval,SEL2}
:=
\limsup_j\sum_{k\ge j}\eta_{cuspLC,j,k}^{SEL2},
```

```math
A_{12}^{smear,eval,SEL2}
:=
\limsup_j\sum_{k\ge j}\eta_{smearLC,j,k}^{SEL2},
```

and

```math
A_{12}^{app,eval,SEL2}
:=
\limsup_j\sum_{k\ge j}
\left(
\eta_{P12,j,k}^{SEL2}
+\eta_{appLC,j,k}^{(12),SEL2}
+\eta_{binLC,j,k}^{(12),SEL2}
\right).
```

These are the Paper-19 `P19-T12-EVAL` constants pushed forward to the frozen
`SEL2` scalar record law. They do not include projective, regulator,
finite-volume, covariance, or Paper-14 export terms.

### Theorem 4.3A.81: First Three `U_EZ` Terms, Honest Zero Tests

Assume `P20-SEL2-STDRED` and `P20-SEL2-TR-COMMON`. Then:

1. **Paper-14 export term.** The sharp same-record value available from
   Paper 19 is

   ```math
   E_{14}^{SEL2}
   =
   \limsup_j\|E_{14}(\eta_j^{SEL2})\|_{tr}
   ```

   when the limsup exists as an evaluated source constant, or any finite
   declared upper bound for this limsup otherwise. It can be replaced by zero
   only under the actual zero-export clause

   ```math
   \|E_{14}(\eta_j^{SEL2})\|_{tr}\to0,
   ```

   or under an exact same-battery Paper-14 export on the frozen `SEL2`
   battery.

2. **Endpoint/corner term.** The standard corner-separated branch carries
   `E_corn^{SEL2}` as a `T_12` endpoint/corner debit. It can be replaced by
   zero only if one proves, on the same scalar record law, either

   ```math
   E_{corn}^{SEL2}=0,
   ```

   or a new no-corner selector is declared and its decoration audit is redone.
   The current finite-template enumeration proves only disjointness and
   finiteness of the endpoint/corner register; it does not prove that the
   register is empty or that its scalar debit vanishes.

3. **Cutoff-to-exact scalar term.** The sharp carried value is

   ```math
   X_{13}^{exact,SEL2}
   =
   \limsup_jX_{13,j}^{exact,SEL2}.
   ```

   It can be replaced by zero only if the Paper-13/Paper-19 exact-entry
   battery satisfies

   ```math
   X_{13,j}^{exact,SEL2}\to0.
   ```

   Equivalently, the cutoff block records used in the row-`j` surface-entry
   proof converge to the exact whole-process scalar entry records on every
   finite record in `B_{13,j}^{exact}`, and the readout tolerance
   `epsilon_{read,j}^{(13),SEL2}` tends to zero.

Consequently the first-priority block satisfies the exact carried bound

```math
U_{EZ,014}^{SEL2}
=
E_{14}^{SEL2}
+E_{corn}^{SEL2}
+X_{13}^{exact,SEL2},
```

with any summand set to zero only after its displayed same-record zero test is
proved.

Proof.

For `E_14`, Paper 19 Definition 8L.11A.3 defines `P19-P14-EXPORT` by the
same-battery transport norm
`\limsup_j||E_14(eta_j)||_tr`, and Theorem 8L.11A.4 proves that this is the
`T_14` source package. Zero therefore requires the norm itself to vanish
cofinally, or the stronger exact export statement.

For `E_corn`, Definition 1.10 and Definition 4.3A.36 of this paper put
endpoint/corner collars outside `D_dec^{SEL2,20}` and inside the reduced
loop-readout transport register. This is a debit-register decision, not a
vanishing estimate. Erasing the term would either double-use the decoration
audit or silently discard endpoint/corner records unless a same-record zero
audit or a new selector is supplied.

For `X_13`, Paper 19 Definition 8L.11A.25 defines the cutoff-to-exact scalar
comparison as the supremum over the finite exact-entry scalar battery plus
the finite readout tolerance. It explicitly excludes projective, regulator,
chart, volume, and Paper-14 whole-process terms, because those are already
charged elsewhere. Hence zero is exactly convergence of this scalar
comparison and readout tolerance on the declared battery. `square`

### Theorem 4.3A.82: Four Reduced `T_12` Loop-Readout Tails

Assume `P20-SEL2-STDRED`, `P20-SEL2-TR-COMMON`, and the Paper-19 reduced
loop-readout source package `P19-T12-EVAL` on the frozen `SEL2` record law.
Then the reduced loop-readout block is exactly

```math
U_{EZ,12}^{SEL2}
=
A_{12}^{per,eval,SEL2}
+A_{12}^{cusp,eval,SEL2}
+A_{12}^{smear,eval,SEL2}
+A_{12}^{app,eval,SEL2},
```

with the four evaluated limsups of Definition 4.3A.80. More explicitly:

1. `A_12^{per,eval,SEL2}=A_12^{cusp,eval,SEL2}=0` if and only if the
   calibrated perimeter and cusp transport tails vanish on the cofinal
   battery:

   ```math
   \sum_{k\ge j}\eta_{perLC,j,k}^{SEL2}\to0,
   \qquad
   \sum_{k\ge j}\eta_{cuspLC,j,k}^{SEL2}\to0.
   ```

2. `A_12^{smear,eval,SEL2}=0` if the smearing-removal schedule stays inside
   the finite loop collars and

   ```math
   \sum_{k\ge j}\eta_{smearLC,j,k}^{SEL2}\to0.
   ```

3. `A_12^{app,eval,SEL2}=0` if the residual Paper-12 loop modulus, loop
   representative replacement, and finite record binning tails all vanish:

   ```math
   \sum_{k\ge j}\eta_{P12,j,k}^{SEL2}\to0,
   \quad
   \sum_{k\ge j}\eta_{appLC,j,k}^{(12),SEL2}\to0,
   \quad
   \sum_{k\ge j}\eta_{binLC,j,k}^{(12),SEL2}\to0.
   ```

If any displayed limsup is finite but nonzero, its value remains in
`U_EZ,12^SEL2`. If any displayed limsup is infinite, the standard reduced
`SEL2` branch fails before the surface leading-rate test.

Proof.

This is Paper 19 Definition 8L.11A.21A and Theorems
8L.11A.21B--8L.11A.21E, evaluated after the `P20-SEL2-TR-COMMON`
pushforward. The perimeter/cusp, smearing, and approximant/readout terms are
exactly the reduced `HK-LC-TRANSPORT` subtails kept in `T_12`. Paper 19
explicitly excludes projective, regulator, and finite-volume losses from
these four limsups; those losses are paid by the reduced `T_11`/`T_14`
ledgers. Nonnegativity and limsup subadditivity give the finite upper bounds,
and vanishing of the displayed cofinal sums gives zero. `square`

### Corollary 4.3A.83: `U_EZ^{SEL2}` Attack Decision

On the current standard reduced `SEL2` branch, the easy-zero bucket has been
attacked down to seven source tests:

```math
U_{EZ}^{SEL2}
=
E_{14}^{SEL2}
+E_{corn}^{SEL2}
+X_{13}^{exact,SEL2}
+A_{12}^{per,eval,SEL2}
+A_{12}^{cusp,eval,SEL2}
+A_{12}^{smear,eval,SEL2}
+A_{12}^{app,eval,SEL2}.
```

The current imports prove this decomposition and prove finite-source
conditions when the corresponding limsups are finite. They do not prove
unconditional zero of any of the seven terms. Therefore the honest
pre-surface surplus after the `U_EZ` attack is

```math
\Pi_{pre13,std,red}^{SEL2}
=
\underline M_{loss}^{SEL2,20}
-U_{EZ}^{SEL2}
-U_{11}^{red,SEL2}
-U_{13}^{entry,red,SEL2},
```

with `U_EZ^SEL2` expanded as above. The next mathematical target is not the
formal decomposition of `U_EZ`; it is one of the seven displayed same-record
estimates, preferably in the priority order

```text
E_14^SEL2, E_corn^SEL2, X_13^exact,SEL2,
A_12^per, A_12^cusp, A_12^smear, A_12^app.
```

Proof.

The first-priority block is Theorem 4.3A.81. The four loop-readout tails are
Theorem 4.3A.82. Adding the two blocks gives Definition 4.3A.80, hence the
displayed expansion of `U_EZ`. Substitution into Definition 4.3A.77 gives the
updated surplus formula. The nonzero decision follows because none of the
seven zero tests is included among the current imported hypotheses. `square`

### Definition 4.3A.84: Paper-14 Export-Zero Audit On `SEL2`

`P20-SEL2-P14-ZERO` is the same-record audit that the Paper-14 export chain
used in `P20-SEL2-TR-COMMON` is a tail-normalized rate-certificate chain.
It consists of the following clauses.

1. The Paper-14 cutoff tuples `eta_n=(a_n,V_n,q_n,ct_n)` form a standard
   Paper-14 continuum chain on the same finite battery family as the frozen
   `SEL2` record laws `Gamma_j^{SEL2}`.

2. The Paper-14 defect vector is exactly the one in Paper 14 Definition 14.1:

   ```text
   E_14(eta_n)
   =
   (E_ID,E_proj,E_CE,E_tail,E_chart,E_ct,E_vol,E_cov,E_RP)(eta_n),
   ```

   with the transport norm of Paper 14 Definition 14.2.

3. The `SEL2` rows read the remaining tail of the Paper-14 rate certificate:
   there is a cofinal map `n=n(j)` such that

   ```math
   \mathfrak E_{14,j}^{tail}
   :=
   \sum_{m\ge n(j)}
   \|E_{14}(\eta_m)\|_{tr}
   ```

   is the exported Paper-14 `T_14` debit for row `j`.

4. The rate-certificate tail vanishes:

   ```math
   \mathfrak E_{14,j}^{tail}\to0.
   ```

This audit is stronger than merely importing `P19-P14-EXPORT(E_14^{SEL2})`.
The latter gives a finite same-record ceiling; `P20-SEL2-P14-ZERO` gives a
vanishing rowwise remaining export debit.

### Theorem 4.3A.85: Paper-14 Export-Zero Criterion

Assume `P20-SEL2-STDRED`, `P20-SEL2-TR-COMMON`, and
`P20-SEL2-P14-ZERO`. Then the Paper-14 term in the easy-zero bucket vanishes:

```math
E_{14}^{SEL2}=0.
```

More precisely,

```math
\limsup_j\|E_{14}(\eta_j^{SEL2})\|_{tr}=0,
```

where `E_14(eta_j^{SEL2})` denotes the row-`j` remaining export vector read by
the `SEL2` common-record ledger.

Proof.

Paper 14 Theorem 14.3 proves whole-process certificate independence when the
transport defects along a standard chain are summable and the remaining tail
from scale `n` onward tends to zero. Paper 14 Theorem 20.3 gives a concrete
rate-certificate route to that hypothesis. Definition 4.3A.84 requires the
frozen `SEL2` row `j` to read exactly that remaining tail after the cofinal
index `n(j)`.

By Definition 4.3A.84,

```math
0\le
\|E_{14}(\eta_j^{SEL2})\|_{tr}
\le
\mathfrak E_{14,j}^{tail}
\to0.
```

Therefore the limsup defining the Paper-19 export ceiling is zero. Paper 19
Theorem 8L.11A.4 then closes the `T_14` source package with
`E_14^{SEL2}=0`. `square`

### Corollary 4.3A.86: Current Decision For `E_14^{SEL2}`

The current `SEL2` imports prove the following exact fork.

1. If the Paper-14 export is only the finite package

   ```math
   P19\text{-}P14\text{-}EXPORT(E_{14}^{SEL2}),
   \qquad
   \limsup_j\|E_{14}(\eta_j^{SEL2})\|_{tr}\le E_{14}^{SEL2}<\infty,
   ```

   then Paper 20 must carry `E_14^{SEL2}` in `U_EZ^{SEL2}`.

2. If the stronger audit `P20-SEL2-P14-ZERO` is proved on the same frozen
   record law, then Theorem 4.3A.85 permits the replacement

   ```math
   E_{14}^{SEL2}=0.
   ```

3. Finite total Paper-14 transport is not enough by itself to set
   `E_14^{SEL2}=0`. The zero conclusion requires either exact same-battery
   export or a tail-normalized rate certificate whose remaining rowwise
   transport norm tends to zero.

Thus step 1 is reduced to a precise Paper-14 source import: prove
`P20-SEL2-P14-ZERO`, or carry the finite value `E_14^{SEL2}` in the
pre-surface surplus.

### Definition 4.3A.87: Component Audit For `P20-SEL2-P14-ZERO`

`P20-SEL2-P14-COMP` is the componentwise version of
`P20-SEL2-P14-ZERO`. It holds when the Paper-14 standard continuum chain and
the `SEL2` cofinal row map `n=n(j)` satisfy all of the following on the same
finite scalar record law.

1. **Row-tail reading.** The `SEL2` row does not read the total accumulated
   Paper-14 transport budget. It reads only the remaining tail after `n(j)`:

   ```math
   E_{14,j}^{SEL2}
   \le
   \sum_{m\ge n(j)}
   \big(
   \alpha_{ID}\epsilon_{ID,m}
   +\alpha_{proj}\epsilon_{proj,m}
   +\alpha_{CE}\epsilon_{CE,m}
   +\alpha_{tail}\epsilon_{tail,m}
   +\alpha_{chart}\epsilon_{chart,m}
   +\alpha_{ct}\epsilon_{ct,m}
   +\alpha_{vol}\epsilon_{vol,m}
   +\alpha_{cov}\epsilon_{cov,m}
   +\alpha_{RP}\epsilon_{RP,m}
   \big).
   ```

2. **Cofinality.** The row map satisfies `n(j)->infinity`.

3. **Component domination.** For every `m`, the nine Paper-14 defect-vector
   components are dominated by the displayed nonnegative source sequences:

   ```math
   E_{ID}(\eta_m)\le\epsilon_{ID,m},
   \quad
   E_{proj}(\eta_m)\le\epsilon_{proj,m},
   \quad
   E_{CE}(\eta_m)\le\epsilon_{CE,m},
   \quad
   E_{tail}(\eta_m)\le\epsilon_{tail,m},
   ```

   ```math
   E_{chart}(\eta_m)\le\epsilon_{chart,m},
   \quad
   E_{ct}(\eta_m)\le\epsilon_{ct,m},
   \quad
   E_{vol}(\eta_m)\le\epsilon_{vol,m},
   \quad
   E_{cov}(\eta_m)\le\epsilon_{cov,m},
   \quad
   E_{RP}(\eta_m)\le\epsilon_{RP,m}.
   ```

4. **Summability.** The weighted component series is summable:

   ```math
   \sum_m
   \big(
   \alpha_{ID}\epsilon_{ID,m}
   +\alpha_{proj}\epsilon_{proj,m}
   +\alpha_{CE}\epsilon_{CE,m}
   +\alpha_{tail}\epsilon_{tail,m}
   +\alpha_{chart}\epsilon_{chart,m}
   +\alpha_{ct}\epsilon_{ct,m}
   +\alpha_{vol}\epsilon_{vol,m}
   +\alpha_{cov}\epsilon_{cov,m}
   +\alpha_{RP}\epsilon_{RP,m}
   \big)
   <\infty.
   ```

The component names are exactly those of Paper 14 Definitions 14.1, 14.2,
and 20.2. The audit does not permit substituting unweighted or different
record-law estimates for these nine pushed-forward whole-process defects.

### Theorem 4.3A.88: Component Audit Closes `P20-SEL2-P14-ZERO`

Assume `P20-SEL2-P14-COMP`. Then `P20-SEL2-P14-ZERO` holds. Consequently
Theorem 4.3A.85 applies and

```math
E_{14}^{SEL2}=0.
```

Proof.

By component domination and the definition of the Paper-14 transport norm,

```math
\|E_{14}(\eta_m)\|_{tr}
\le
\alpha_{ID}\epsilon_{ID,m}
+\alpha_{proj}\epsilon_{proj,m}
+\alpha_{CE}\epsilon_{CE,m}
+\alpha_{tail}\epsilon_{tail,m}
+\alpha_{chart}\epsilon_{chart,m}
+\alpha_{ct}\epsilon_{ct,m}
+\alpha_{vol}\epsilon_{vol,m}
+\alpha_{cov}\epsilon_{cov,m}
+\alpha_{RP}\epsilon_{RP,m}.
```

The weighted component series is summable, so its tails tend to zero. Since
`n(j)->infinity`, the tail read by row `j` tends to zero:

```math
\sum_{m\ge n(j)}
\|E_{14}(\eta_m)\|_{tr}
\to0.
```

This is exactly Definition 4.3A.84 clauses 3--4, with clauses 1--2 supplied
by the same `SEL2` row-tail reading and Paper-14 standard-chain hypotheses.
Thus `P20-SEL2-P14-ZERO` holds, and Theorem 4.3A.85 gives
`E_14^{SEL2}=0`. `square`

### Corollary 4.3A.89: Admissible Paper-14 Rate Classes Are Sufficient

Assume the Paper-14 rate classes of Paper 14 Definition 31.1 on the same
standard chain:

```math
\epsilon_{ID,m}\le C_{ID}m^{-1-p_{ID}},
\quad
\epsilon_{proj,m}\le C_{proj}e^{-m_{proj}D_m},
\quad
\epsilon_{CE,m}\le C_{CE}m^{-1-p_{CE}},
```

```math
\epsilon_{tail,m}\le C_{tail}e^{-m_{tail}C_2(\Lambda_m)},
\quad
\epsilon_{chart,m}\le C_{chart}m^{-1-p_{chart}},
\quad
\epsilon_{ct,m}\le C_{ct}m^{-1-p_{ct}},
```

```math
\epsilon_{vol,m}\le C_{vol}e^{-m_{vol}b_m},
\quad
\epsilon_{cov,m}\le C_{cov}m^{-1-p_{cov}},
\quad
\epsilon_{RP,m}\le C_{RP}m^{-1-p_{RP}},
```

with all polynomial exponents and exponential rate constants positive, and
with `D_m`, `C_2(\Lambda_m)`, and `b_m` increasing so the exponential tails
are summable. If the `SEL2` row map satisfies `n(j)->infinity` and reads the
remaining tail, then `P20-SEL2-P14-COMP` holds, hence

```math
E_{14}^{SEL2}=0.
```

Proof.

Paper 14 Proposition 20.4 and Theorem 31.2 state that these polynomial and
exponential rate classes give a summable Paper-14 rate certificate. With the
same weights `alpha_*`, finite weighted sums of these summable sequences are
summable. Definition 4.3A.87 then holds, and Theorem 4.3A.88 gives the
conclusion. `square`

### Corollary 4.3A.90: Result Of The Further `E_14` Investigation

The further investigation does not prove `E_14^{SEL2}=0` unconditionally from
the currently imported sources. It proves the exact decision:

1. if the actual Paper-14 standard chain is equipped with the component rate
   certificate of Definition 4.3A.87, or with the admissible rate classes of
   Corollary 4.3A.89, and if `SEL2` reads the remaining tail along a cofinal
   row map, then `E_14^{SEL2}=0`;
2. if Paper 20 imports only `P19-P14-EXPORT(E_14^{SEL2})`, then the branch
   must carry finite `E_14^{SEL2}`;
3. Paper 14 currently names the needed actual estimates. It does not, by
   itself, prove that four-dimensional `SU(N)` satisfies the nine component
   rate bounds on the relevant whole-process tower.

Thus the honest next step after this investigation is either to prove the
nine Paper-14 component rate estimates on the same `SEL2` tower, or to stop
spending Paper-20 effort on this term and carry `E_14^{SEL2}` into the
pre-surface surplus.

### Corollary 4.3A.91: Parked Paper-14 Export Convention

For the current standard reduced `SEL2` branch, Paper 20 adopts the parked
Paper-14 convention:

```math
E_{14}^{SEL2,park}:=E_{14}^{SEL2}<\infty,
```

where the finite value is the value imported by
`P19-P14-EXPORT(E_14^{SEL2})`. The zero replacement

```math
E_{14}^{SEL2}=0
```

is not used in the active pre-surface surplus unless
`P20-SEL2-P14-COMP` is later proved on the same frozen record law.

Thus the active easy-zero bucket for the current branch is

```math
U_{EZ}^{SEL2,park}
:=
E_{14}^{SEL2}
+E_{corn}^{SEL2}
+X_{13}^{exact,SEL2}
+A_{12}^{per,eval,SEL2}
+A_{12}^{cusp,eval,SEL2}
+A_{12}^{smear,eval,SEL2}
+A_{12}^{app,eval,SEL2}.
```

The active pre-surface surplus is therefore

```math
\Pi_{pre13,std,red}^{SEL2,park}
:=
\underline M_{loss}^{SEL2,20}
-U_{EZ}^{SEL2,park}
-U_{11}^{red,SEL2}
-U_{13}^{entry,red,SEL2}.
```

The parked convention is a bookkeeping decision, not a falsification of the
Paper-14 zero route. It prevents Paper 20 from spending the unproved
component rate certificate while allowing the `SEL2` branch to continue with
the finite Paper-14 debit carried honestly.

### Definition 4.3A.92: Endpoint/Corner Template Audit On `SEL2`

`P20-SEL2-ECORN(C_{corn}^{SEL2})` is the same-record finite-template audit
for the endpoint/corner transport debit of the standard corner-separated
`SEL2` branch. It consists of the following data.

1. The geometric slots are the four centered-square Creutz slots of
   Definition 4.3A.6:

   ```math
   (L_j,L_j),\quad
   (L_j-\sigma_j,L_j-\sigma_j),\quad
   (L_j-\sigma_j,L_j),\quad
   (L_j,L_j-\sigma_j).
   ```

2. Endpoint/corner templates are excluded from
   `D_dec^{SEL2,20}` and charged only to the reduced loop-readout side of the
   nonsurface transport ledger.

3. Let `\mathcal D_{corn}^{SEL2}` be the finite list of endpoint/corner
   template types appearing in these four slots after quotienting by the
   declared record symmetries. For each `upsilon in \mathcal D_{corn}^{SEL2}`,
   let `v_upsilon>=0` be the scalar transport weight of one occurrence on the
   pushed-forward `SEL2` scalar record law.

4. Let `M_{\upsilon,j}` be the number of occurrences of template `upsilon` in
   the row-`j` four-slot Creutz battery. The audited corner ceiling satisfies

   ```math
   C_{corn}^{SEL2}
   \ge
   \limsup_j
   \sum_{\upsilon\in\mathcal D_{corn}^{SEL2}}
   M_{\upsilon,j}v_\upsilon
   <\infty.
   ```

The audit is purely finite-template bookkeeping. It is not a new decoration
constant and may not also be charged in `D_dec`, `T_11`, `T_13`, or `T_14`.

### Lemma 4.3A.93: Four-Slot Corner Count

On the standard centered-square `SEL2` branch, after passing to a cofinal tail
all four Creutz slots are nondegenerate rectangles. Hence the unreduced
four-slot battery has exactly sixteen convex endpoint/corner occurrences:

```math
N_{corn}^{rect}=4\cdot4=16.
```

If the selected endpoint/corner transport convention also counts
Creutz-overlap concave subtraction corners as separate endpoint/corner
templates, let `N_{conc}^{SEL2}` denote their finite four-slot count. Then

```math
N_{corn}^{templ,SEL2}
:=
16+N_{conc}^{SEL2}
<\infty
```

is the total endpoint/corner occurrence count before quotienting by record
symmetries.

Proof.

The centered-square schedule has `0<alpha<1` and
`\sigma_j=\lfloor\alpha L_j\rfloor`, so along a cofinal tail both `L_j` and
`L_j-\sigma_j` are positive. Each of the four Creutz slots is therefore a
nondegenerate lattice rectangle. A nondegenerate rectangle has four convex
corners, giving `4*4=16` convex endpoint/corner occurrences.

The local template list of Definition 4.3A.6 is finite and includes the
possible Creutz-overlap concave corner type. If the transport convention
treats those concave subtraction corners as endpoint/corner debits, their
number is bounded by a finite template count depending only on the four-slot
Creutz pattern, not on `j`. This gives finite `N_conc^{SEL2}` and hence the
displayed total. Quotienting by symmetries can only reduce the number of
distinct weighted occurrences. `square`

### Theorem 4.3A.94: Explicit Finite Bound For `E_corn^{SEL2}`

Assume `P20-SEL2-STDRED` and `P20-SEL2-ECORN(C_{corn}^{SEL2})`. Then

```math
0\le E_{corn}^{SEL2}\le C_{corn}^{SEL2}<\infty.
```

In particular, if

```math
v_{corn}^{max}
:=
\max_{\upsilon\in\mathcal D_{corn}^{SEL2}}v_\upsilon,
```

then the standard four-slot template gives the explicit finite bound

```math
E_{corn}^{SEL2}
\le
N_{corn}^{templ,SEL2}\,v_{corn}^{max}
=
(16+N_{conc}^{SEL2})v_{corn}^{max}.
```

On the pure rectangular-corner convention, where no Creutz-overlap concave
corner is charged separately to endpoint/corner transport,
`N_conc^{SEL2}=0`, so

```math
E_{corn}^{SEL2}\le16\,v_{corn}^{max}.
```

Under the standard unit-counted endpoint/corner normalization
`v_corn^max=1`, this becomes

```math
E_{corn}^{SEL2}\le16
```

on the pure rectangular-corner convention, and

```math
E_{corn}^{SEL2}\le16+N_{conc}^{SEL2}
```

under the convention that also counts concave subtraction corners.

Proof.

By Definition 4.3A.92, the endpoint/corner debit is the limsup of a finite
weighted count of endpoint/corner templates on the same pushed-forward scalar
record law. This gives `E_corn^{SEL2}<=C_corn^{SEL2}`. Lemma 4.3A.93 bounds
the number of endpoint/corner occurrences before quotienting by
`N_corn^{templ,SEL2}`. Bounding each occurrence by `v_corn^max` gives the
displayed estimate. The unit-counted specialization is the case
`v_corn^max=1`. `square`

### Theorem 4.3A.95: Zero Decision For `E_corn^{SEL2}`

On the standard corner-separated `SEL2` branch with the four nondegenerate
Creutz slots of Definition 4.3A.6, the endpoint/corner debit cannot be set to
zero merely by bookkeeping. The zero replacement

```math
E_{corn}^{SEL2}=0
```

is allowed only under one of the following stronger clauses.

1. **Zero-weight audit:** every endpoint/corner transport weight vanishes on
   the same scalar record law:

   ```math
   v_\upsilon=0
   \qquad
   \text{for all }\upsilon\in\mathcal D_{corn}^{SEL2}.
   ```

2. **Empty-template audit:** the selected finite battery has no
   endpoint/corner templates cofinally:

   ```math
   M_{\upsilon,j}=0
   \qquad
   \text{for all }\upsilon
   \text{ on a cofinal tail}.
   ```

3. **New no-corner selector:** endpoint/corner normalization is moved back
   into the multiplicative decoration ledger or removed by a different finite
   readout convention, and the full selector, no-smuggling audit, decoration
   constant, and transport ledger are recomputed.

In the present standard branch none of these clauses is part of the imported
source package. Therefore `E_corn^{SEL2}` is carried with the finite bound of
Theorem 4.3A.94.

Proof.

Definition 4.3A.76 fixes the standard branch as corner-separated:
endpoint/corner collars are outside `D_dec^{SEL2,20}` and charged to the
reduced loop-readout side. Lemma 4.3A.93 shows that the four-slot
centered-square battery has nonempty endpoint/corner occurrences on a cofinal
tail. Therefore the only ways for the scalar debit to vanish on this branch
are that all corresponding scalar weights vanish, or that the finite battery
is changed so those templates are not present. The latter is a different
selector or readout convention and must be re-audited. Without one of the
three displayed clauses, setting `E_corn^{SEL2}=0` would discard a declared
finite record-law debit. `square`

### Corollary 4.3A.96: Active `E_corn` Decision

For the active parked Paper-14 branch of Corollary 4.3A.91, the easy-zero
bucket becomes

```math
U_{EZ}^{SEL2,park}
=
E_{14}^{SEL2}
+E_{corn}^{SEL2}
+X_{13}^{exact,SEL2}
+A_{12}^{per,eval,SEL2}
+A_{12}^{cusp,eval,SEL2}
+A_{12}^{smear,eval,SEL2}
+A_{12}^{app,eval,SEL2},
```

with

```math
0\le E_{corn}^{SEL2}
\le
(16+N_{conc}^{SEL2})v_{corn}^{max}.
```

Thus the current standard reduced `SEL2` branch carries `E_corn^{SEL2}` as a
finite endpoint/corner transport debit. It cannot use `E_corn^{SEL2}=0`
unless the zero-weight, empty-template, or new-selector audit of Theorem
4.3A.95 is later supplied.

### Definition 4.3A.97: Cutoff-To-Exact Scalar Audit On `SEL2`

`P20-SEL2-X13EXACT(A_X^{SEL2})` is the same-record version of Paper 19's
`P19-T13-EXACT` comparison on the frozen standard reduced `SEL2` branch. Let
`B_{13,j}^{exact,SEL2}` be the finite scalar battery required by the row-`j`
surface-entry proof: the four Creutz loop records, the finite connected-entry
products, and the scalar block records used to read
`u_{\rho,s_0,j}`, `A_{C,j}`, `B_{C,j}`, `xi_{C,j}`, `xi'_{C,j}`, and
`N_j(C)`.

Define the rowwise cutoff-to-exact scalar discrepancy by

```math
D_{13,j}^{cut\to exact,SEL2}
:=
\sup_{F\in B_{13,j}^{exact,SEL2}}
\left|
\mathbb E_{\mu_{a_j,s_0}^{blk,SEL2}}F
-
\mathbb E_{\mu_{s_0}^{blk,SEL2}}F
\right|,
```

and

```math
X_{13,j}^{exact,SEL2}
:=
D_{13,j}^{cut\to exact,SEL2}
+
\epsilon_{read,j}^{(13),SEL2}.
```

The audit `P20-SEL2-X13EXACT(A_X^{SEL2})` asserts

```math
\limsup_jX_{13,j}^{exact,SEL2}
\le A_X^{SEL2}<\infty.
```

The zero-strength version, `P20-SEL2-X13EXACT-ZERO`, asserts the two stronger
limits

```math
D_{13,j}^{cut\to exact,SEL2}\to0,
\qquad
\epsilon_{read,j}^{(13),SEL2}\to0.
```

The cutoff-to-exact audit is reduced: it contains no projective, chart,
counterterm, finite-volume, covariance, reflection-positivity, Paper-14
export, perimeter, cusp, smearing, or loop-approximant debit. Those terms
remain in the other parked buckets.

### Lemma 4.3A.98: Diagonal Finite-Battery Criterion For `X_13`

Assume `P20-SEL2-STDRED` and `P20-SEL2-TR-COMMON`. Suppose that:

1. For every fixed finite scalar battery `B` contained in the `SEL2`
   block-record algebra,

   ```math
   \sup_{F\in B}
   \left|
   \mathbb E_{\mu_{a,s_0}^{blk,SEL2}}F
   -
   \mathbb E_{\mu_{s_0}^{blk,SEL2}}F
   \right|
   \to0
   \qquad(a\to\infty).
   ```

2. The rowwise batteries `B_{13,j}^{exact,SEL2}` are finite and are declared
   before choosing the cutoff row `a_j`.

3. The cutoff family is directed enough that `a_j` may be chosen
   nondecreasing and cofinal after the row battery is fixed.

Then there is a cofinal cutoff schedule and a numerical sequence `r_j downarrow
0` such that

```math
D_{13,j}^{cut\to exact,SEL2}\le r_j.
```

Consequently, if also `epsilon_{read,j}^{(13),SEL2}\to0`, then
`P20-SEL2-X13EXACT-ZERO` holds.

Proof.

For each fixed row `j`, the battery `B_{13,j}^{exact,SEL2}` is finite. The
fixed-battery convergence clause therefore gives a cutoff threshold
`a(j)` such that the displayed supremum over that row's battery is at most
`r_j`, for any prechosen sequence `r_j downarrow0`. Recursively replace
`a(j)` by a larger directed cutoff if needed so that the sequence is
nondecreasing and cofinal. This proves
`D_{13,j}^{cut->exact,SEL2}<=r_j`. Adding the readout convergence gives
`X_{13,j}^{exact,SEL2}->0`. `square`

### Theorem 4.3A.99: `X_13^{exact,SEL2}` Zero And Carry Decision

Assume `P20-SEL2-STDRED` and `P20-SEL2-TR-COMMON`.

1. If `P20-SEL2-X13EXACT-ZERO` holds, then the cutoff-to-exact scalar term in
   the easy-zero bucket vanishes:

   ```math
   X_{13}^{exact,SEL2}:=\limsup_jX_{13,j}^{exact,SEL2}=0.
   ```

2. If only `P20-SEL2-X13EXACT(A_X^{SEL2})` holds, then the active branch must
   carry the finite debit

   ```math
   0\le X_{13}^{exact,SEL2}\le A_X^{SEL2}.
   ```

3. Fixed-battery convergence alone does not justify setting
   `X_{13}^{exact,SEL2}=0` when the batteries
   `B_{13,j}^{exact,SEL2}` move with `j`. One needs the diagonal row schedule
   of Lemma 4.3A.98, or an equivalent uniform moving-battery estimate.

Proof.

The first statement is immediate from the definition of the limsup. The
second is the finite-source audit of Definition 4.3A.97. For the third,
pointwise convergence on each fixed battery controls any battery held fixed
while the cutoff is sent to infinity; it does not by itself control the
supremum over a row-dependent battery. Lemma 4.3A.98 supplies the missing
diagonal choice. Without that diagonal or uniform moving-battery clause,
erasing `X_13^{exact,SEL2}` would hide an exact-entry transport estimate in
the surface ledger. `square`

### Corollary 4.3A.100: Active `U_EZ` Decision After Steps 1--2

After parking the Paper-14 zero route, bounding the endpoint/corner register,
and attacking the cutoff-to-exact scalar comparison, the active standard
reduced `SEL2` branch uses

```math
U_{EZ}^{SEL2,park}
=
E_{14}^{SEL2}
+E_{corn}^{SEL2}
+X_{13}^{exact,SEL2}
+A_{12}^{per,eval,SEL2}
+A_{12}^{cusp,eval,SEL2}
+A_{12}^{smear,eval,SEL2}
+A_{12}^{app,eval,SEL2},
```

with

```math
0\le E_{corn}^{SEL2}
\le(16+N_{conc}^{SEL2})v_{corn}^{max},
```

and either

```math
X_{13}^{exact,SEL2}=0
\quad\text{under }P20\text{-}SEL2\text{-}X13EXACT\text{-}ZERO,
```

or

```math
0\le X_{13}^{exact,SEL2}\le A_X^{SEL2}
\quad\text{under }P20\text{-}SEL2\text{-}X13EXACT(A_X^{SEL2}).
```

Thus steps 1--2 of the `U_EZ^{SEL2}` attack are complete as an honest
decision tree. The next terms in execution order are
`A_12^{per,eval,SEL2}` and `A_12^{cusp,eval,SEL2}`.

### Definition 4.3A.101: Perimeter/Cusp Residuals For The `SEL2` Creutz Row

For the standard `SEL2` centered-square Creutz row, let the four loop slots be

```math
C_{++}=C(L_j,L_j),\quad
C_{--}=C(L_j-\sigma_j,L_j-\sigma_j),\quad
C_{+-}=C(L_j,L_j-\sigma_j),\quad
C_{-+}=C(L_j-\sigma_j,L_j),
```

with signed Creutz coefficients

```math
s_{++}=s_{--}=+1,\qquad s_{+-}=s_{-+}=-1.
```

The scalar perimeter residual is

```math
\Pi_j^{per}
:=
\left|
\sum_{\alpha\in\{++,--,+-,-+\}}s_\alpha\,{\rm Per}(C_\alpha)
\right|.
```

For each cusp angle `theta`, let `n_\alpha(theta)` be the number of cusps of
angle `theta` in `C_\alpha`. The scalar cusp residual is

```math
\Pi_j^{cusp}
:=
\sum_{\theta}
\left|
\sum_{\alpha\in\{++,--,+-,-+\}}s_\alpha\,n_\alpha(\theta)
\right|.
```

The exact perimeter/cusp cancellation audit `P20-SEL2-PC-CANCEL` asserts:

1. the four slots use the same representation and the same calibrated
   Paper-12 perimeter/cusp counterterm branches;
2. the perimeter/cusp part of `T_12` is the signed Creutz scalar record, while
   loop-approximant, endpoint/corner-collar, projective, regulator, volume,
   and Paper-14 terms remain in their assigned buckets;
3. `Pi_j^{per}=Pi_j^{cusp}=0` on a cofinal tail.

This audit concerns only the scalar perimeter/cusp counterterm transport
tails. It does not set the endpoint/corner finite-template debit
`E_corn^{SEL2}` to zero.

### Lemma 4.3A.102: Four-Slot Creutz Cancellation

For the actual rectangular four-slot `SEL2` geometry of Definition 4.3A.101,
the geometric residuals vanish:

```math
\Pi_j^{per}=0,
\qquad
\Pi_j^{cusp}=0.
```

Proof.

For a rectangle with side lengths `(R,S)`,

```math
{\rm Per}(R,S)=2R+2S.
```

Therefore

```math
\begin{aligned}
&{\rm Per}(L_j,L_j)
+{\rm Per}(L_j-\sigma_j,L_j-\sigma_j)\\
&\quad
-{\rm Per}(L_j,L_j-\sigma_j)
-{\rm Per}(L_j-\sigma_j,L_j)
=0.
\end{aligned}
```

Each of the four rectangular slots has exactly four right-angle cusps and no
other cusp angle in the scalar perimeter/cusp counterterm ledger. Thus the
signed right-angle cusp count is

```math
4+4-4-4=0,
```

and every other angle has count zero in every slot. Hence
`Pi_j^{cusp}=0`. `square`

### Definition 4.3A.103: Perimeter/Cusp Tail Bound Audit On `SEL2`

`P20-SEL2-T12-PC-BOUND(U_{12}^{per,SEL2},U_{12}^{cusp,SEL2})` is the finite
same-record bound for the calibrated perimeter/cusp loop-continuity tails. It
asserts that there are nonnegative row-shell bounds
`b_{per,j,k}^{SEL2}` and `b_{cusp,j,k}^{SEL2}` such that, for all `k>=j`,

```math
\eta_{perLC,j,k}^{SEL2}\le b_{per,j,k}^{SEL2},
\qquad
\eta_{cuspLC,j,k}^{SEL2}\le b_{cusp,j,k}^{SEL2},
```

and

```math
\limsup_j\sum_{k\ge j}b_{per,j,k}^{SEL2}
\le U_{12}^{per,SEL2}<\infty,
\qquad
\limsup_j\sum_{k\ge j}b_{cusp,j,k}^{SEL2}
\le U_{12}^{cusp,SEL2}<\infty.
```

A source-realized choice is obtained from Paper 12's scalar counterterm
ledger by bounding the one-shell calibration variation:

```math
b_{per,j,k}^{SEL2}
=
\Pi_j^{per}\,v_{per,j,k}^{SEL2}+r_{per,j,k}^{SEL2},
```

```math
b_{cusp,j,k}^{SEL2}
=
\Pi_j^{cusp}\,v_{cusp,j,k}^{SEL2}+r_{cusp,j,k}^{SEL2},
```

where `v_per` and `v_cusp` are the scalar changes of the calibrated
perimeter and cusp branches between shell `k` and shell `k+1`, and the
residuals `r_per`, `r_cusp` are allowed only for explicitly declared
perimeter/cusp mismatch not already assigned to `A_12^{app}`, `E_corn`,
`T_11`, or `T_14`.

The zero-strength audit `P20-SEL2-T12-PC-ZERO` is the stronger condition

```math
\sum_{k\ge j}b_{per,j,k}^{SEL2}\to0,
\qquad
\sum_{k\ge j}b_{cusp,j,k}^{SEL2}\to0.
```

The exact Creutz branch `P20-SEL2-PC-CANCEL`, together with
`r_{per,j,k}^{SEL2}=r_{cusp,j,k}^{SEL2}=0` on a cofinal tail, implies
`P20-SEL2-T12-PC-ZERO`.

### Theorem 4.3A.104: Perimeter/Cusp Tail Decision

Assume `P20-SEL2-STDRED`, `P20-SEL2-TR-COMMON`, and the reduced Paper-19
perimeter/cusp source attack `P19-T12-PC` evaluated on the frozen `SEL2`
record law.

1. If `P20-SEL2-T12-PC-BOUND(U_{12}^{per,SEL2},U_{12}^{cusp,SEL2})` holds,
   then

   ```math
   A_{12}^{per,eval,SEL2}\le U_{12}^{per,SEL2},
   \qquad
   A_{12}^{cusp,eval,SEL2}\le U_{12}^{cusp,SEL2}.
   ```

2. If `P20-SEL2-T12-PC-ZERO` holds, then

   ```math
   A_{12}^{per,eval,SEL2}
   =
   A_{12}^{cusp,eval,SEL2}
   =
   0.
   ```

3. In particular, the exact signed Creutz cancellation audit
   `P20-SEL2-PC-CANCEL`, with no residual perimeter/cusp mismatch outside the
   assigned `A_12^{app}` and `E_corn` buckets, gives

   ```math
   \sum_{k\ge j}\eta_{perLC,j,k}^{SEL2}\to0,
   \qquad
   \sum_{k\ge j}\eta_{cuspLC,j,k}^{SEL2}\to0.
   ```

Proof.

Paper 19 Definition 8L.11A.21A identifies
`A_12^{per,eval,SEL2}` and `A_12^{cusp,eval,SEL2}` with the limsups of the
two displayed `HK-LC-TRANSPORT` tails. The row-shell domination in Definition
4.3A.103 gives the finite upper bounds by monotonicity of limsup.

If the row-shell bound tails tend to zero, those limsups are zero. For the
exact Creutz branch, Lemma 4.3A.102 gives `Pi_j^{per}=Pi_j^{cusp}=0`. With
the same Paper-12 calibration branches on all four slots and no unassigned
perimeter/cusp residuals, the source-realized bounds have zero tails, so the
two calibrated perimeter/cusp transport sums vanish. `square`

### Corollary 4.3A.105: Active `U_EZ` Decision After Perimeter/Cusp Attack

After the perimeter/cusp attack, the active easy-zero bucket may be sharpened
to

```math
U_{EZ}^{SEL2,park,pc}
=
E_{14}^{SEL2}
+E_{corn}^{SEL2}
+X_{13}^{exact,SEL2}
+U_{12}^{per,SEL2}
+U_{12}^{cusp,SEL2}
+A_{12}^{smear,eval,SEL2}
+A_{12}^{app,eval,SEL2},
```

under `P20-SEL2-T12-PC-BOUND`. Under the stronger exact cancellation branch
`P20-SEL2-T12-PC-ZERO`, this reduces to

```math
U_{EZ}^{SEL2,park,pc0}
=
E_{14}^{SEL2}
+E_{corn}^{SEL2}
+X_{13}^{exact,SEL2}
+A_{12}^{smear,eval,SEL2}
+A_{12}^{app,eval,SEL2}.
```

Thus `A_12^{per}` and `A_12^{cusp}` are now decided in the honest sense:
they vanish on the same-record signed Creutz cancellation branch, and
otherwise they remain as the explicit finite carried bounds
`U_{12}^{per,SEL2}` and `U_{12}^{cusp,SEL2}`. The next terms in execution
order are `A_12^{smear,eval,SEL2}` and then `A_12^{app,eval,SEL2}`.

### Definition 4.3A.106: Smearing Collar Window Audit On `SEL2`

For each row `j`, let `B_{12,j}^{smear,SEL2}` be the finite loop battery on
which the reduced smearing-removal comparison is used. Define
`r_{min,j}^{SEL2}>0` to be the minimum admissible separation in that battery:
the minimum of the separation between distinct nonadjacent arcs, distinct
loops in any tested product, and the physical distance from cusp collars to
nonincident arcs. Let `c_{sm}` be the fixed support constant of the
gauge-covariant smearing kernel, so the kernel of radius `tau` is supported
inside distance `c_{sm}tau`.

`P20-SEL2-SMEAR-COL` is the collar-window audit asserting that there are
smearing radii `tau_{j,k}^{SEL2}` for `k>=j` such that:

```math
a_k\ll \tau_{j,k}^{SEL2},
\qquad
c_{sm}\tau_{j,k}^{SEL2}
\le {1\over4}r_{min,j}^{SEL2},
\qquad
\tau_{j,k}^{SEL2}\to0
\quad(k\to\infty),
```

and all comparisons use the same Paper-12 perimeter/cusp calibration branches
already fixed in the perimeter/cusp attack. Equivalently, the smearing
support remains inside the declared loop collars and never mixes distinct
nonadjacent arcs, distinct loops, or nonincident cusp collars.

For the rectangular `SEL2` Creutz row, the nondegenerate cofinal condition
`L_j-\sigma_j>0` gives `r_{min,j}^{SEL2}>0` for each finite row. The audit is
not the numerical assertion that the tail is small; it is the geometric
precondition that allows Paper 12 Lemma 3.13 and Theorem 3.12 to be applied
on that row.

### Definition 4.3A.107: Smearing-Removal Tail Audit On `SEL2`

Assume `P20-SEL2-SMEAR-COL`. For each row-shell pair `k>=j`, define the
finite-row Paper-12 smearing modulus

```math
\Delta_{sm,j,k}^{SEL2}
:=
\max_{\alpha\in B_{12,j}^{smear,SEL2}}
\left(
\epsilon_{\alpha}^{cal}(\tau_{j,k}^{SEL2})
+\Omega_{\alpha}(\tau_{j,k}^{SEL2})
\right).
```

`P20-SEL2-T12-SMEAR-BOUND(U_{12}^{smear,SEL2})` asserts that there are
nonnegative row-shell bounds `b_{smear,j,k}^{SEL2}` with

```math
\eta_{smearLC,j,k}^{SEL2}
\le b_{smear,j,k}^{SEL2},
```

and

```math
\limsup_j\sum_{k\ge j}b_{smear,j,k}^{SEL2}
\le U_{12}^{smear,SEL2}<\infty.
```

A source-realized bound has the form

```math
b_{smear,j,k}^{SEL2}
=
w_{sm,j,k}^{SEL2}\Delta_{sm,j,k}^{SEL2}
+r_{sm,j,k}^{SEL2},
```

where `w_{sm,j,k}^{SEL2}` is the finite product/cumulant multiplicity from
the row battery and `r_{sm,j,k}^{SEL2}` is allowed only for explicitly
declared smearing-readout mismatch not assigned to `A_12^{app}`, `E_corn`,
`T_11`, or `T_14`.

The zero-strength audit `P20-SEL2-T12-SMEAR-ZERO` asserts

```math
\sum_{k\ge j}b_{smear,j,k}^{SEL2}\to0.
```

A sufficient diagonal version is: after fixing the finite row battery, choose
the cofinal smearing radii inside the collar window so that

```math
w_{sm,j,k}^{SEL2}\Delta_{sm,j,k}^{SEL2}
+r_{sm,j,k}^{SEL2}
\le 2^{-(j+k)}
```

for all `k>=j` on a cofinal tail. Then

```math
\sum_{k\ge j}b_{smear,j,k}^{SEL2}
\le 2^{-j+1}\to0.
```

This diagonal schedule is the moving-row analogue of Paper 12's fixed finite
battery smearing-removal convergence.

### Theorem 4.3A.108: Smearing-Removal Tail Decision

Assume `P20-SEL2-STDRED`, `P20-SEL2-TR-COMMON`,
`P19-T12-SMEAR(A_{12}^{smear,SEL2})`, and `P19-T12-EVAL` on the frozen
`SEL2` record law.

1. If `P20-SEL2-T12-SMEAR-BOUND(U_{12}^{smear,SEL2})` holds, then

   ```math
   A_{12}^{smear,eval,SEL2}
   \le U_{12}^{smear,SEL2}.
   ```

2. If `P20-SEL2-T12-SMEAR-ZERO` holds, then

   ```math
   A_{12}^{smear,eval,SEL2}=0.
   ```

3. The geometric collar audit `P20-SEL2-SMEAR-COL`, together with the
   diagonal source-realized bound of Definition 4.3A.107 and
   `r_{sm,j,k}^{SEL2}=0` cofinally, proves

   ```math
   \sum_{k\ge j}\eta_{smearLC,j,k}^{SEL2}\to0.
   ```

Proof.

Paper 19 Definition 8L.11A.21A identifies
`A_{12}^{smear,eval,SEL2}` with
`\limsup_j sum_{k>=j}eta_{smearLC,j,k}^{SEL2}`. The bound audit therefore
gives clause 1 by domination and limsup monotonicity. Clause 2 is the same
statement when the dominating tail tends to zero.

For clause 3, `P20-SEL2-SMEAR-COL` gives the scale window
`a_k<<tau_{j,k}^{SEL2}<<r_{min,j}^{SEL2}` required by Paper 12 Lemma 3.13.
Paper 12 Definition 3.11 and Theorem 3.12 then bound the finite-row
smeared-to-unsmeared difference by
`epsilon_alpha^{cal}(tau)+Omega_alpha(tau)`, with uniform connected
domination on the finite row. The diagonal choice in Definition 4.3A.107
makes the transported row-shell sum summable with vanishing tail. Paper 16
`HK-LC-TRANSPORT` assigns exactly this replacement to `eta_smearLC`; all
projective, regulator, finite-volume, perimeter/cusp, endpoint/corner, and
readout losses remain outside this bucket. `square`

### Corollary 4.3A.109: Active `U_EZ` Decision After Smearing Attack

After the smearing-removal attack, the active easy-zero bucket may be written

```math
U_{EZ}^{SEL2,park,pcs}
=
E_{14}^{SEL2}
+E_{corn}^{SEL2}
+X_{13}^{exact,SEL2}
+U_{12}^{per,SEL2}
+U_{12}^{cusp,SEL2}
+U_{12}^{smear,SEL2}
+A_{12}^{app,eval,SEL2},
```

under the finite perimeter/cusp and smearing bound audits. Under the stronger
same-record zero audits for perimeter/cusp and smearing,

```math
A_{12}^{per,eval,SEL2}
=A_{12}^{cusp,eval,SEL2}
=A_{12}^{smear,eval,SEL2}
=0,
```

and the bucket reduces to

```math
U_{EZ}^{SEL2,park,pcs0}
=
E_{14}^{SEL2}
+E_{corn}^{SEL2}
+X_{13}^{exact,SEL2}
+A_{12}^{app,eval,SEL2}.
```

Thus `A_12^{smear}` is now decided in the honest sense: it vanishes when the
smearing schedule stays inside collars and the transported smearing-removal
tail is diagonally summable with vanishing row tail; otherwise it remains as
the explicit finite carried bound `U_{12}^{smear,SEL2}`. The next `U_EZ`
term in execution order is `A_12^{app,eval,SEL2}`.

### Definition 4.3A.110: Three-Term `A_12^{app}` Split On `SEL2`

On the frozen `SEL2` scalar record law, define the three reduced app/readout
subtails

```math
L_{12}^{P12,SEL2}
:=
\limsup_j\sum_{k\ge j}\eta_{P12,j,k}^{SEL2},
```

```math
L_{12}^{appLC,SEL2}
:=
\limsup_j\sum_{k\ge j}\eta_{appLC,j,k}^{(12),SEL2},
```

and

```math
L_{12}^{binLC,SEL2}
:=
\limsup_j\sum_{k\ge j}\eta_{binLC,j,k}^{(12),SEL2}.
```

These are the only three terms in `A_12^{app,eval,SEL2}`:

```math
A_{12}^{app,eval,SEL2}
\le
L_{12}^{P12,SEL2}
+L_{12}^{appLC,SEL2}
+L_{12}^{binLC,SEL2}.
```

They mean, respectively:

1. residual Paper-12 AF loop-variation and connected-tail loss after the row
   loop modulus has been extracted;
2. lattice/block loop-representative replacement loss;
3. finite scalar record binning and battery-restriction loss.

The split is reduced. It excludes perimeter/cusp, smearing, endpoint/corner,
projective, regulator/chart, finite-volume, reflection-positivity,
covariance, and Paper-14 export terms.

### Definition 4.3A.111: Paper-12 Residual Modulus Tail Audit

`P20-SEL2-T12-P12-BOUND(U_{12}^{P12,SEL2})` asserts that there are
nonnegative row-shell bounds `b_{P12,j,k}^{SEL2}` such that

```math
\eta_{P12,j,k}^{SEL2}\le b_{P12,j,k}^{SEL2},
```

and

```math
\limsup_j\sum_{k\ge j}b_{P12,j,k}^{SEL2}
\le U_{12}^{P12,SEL2}<\infty.
```

A source-realized bound has the form

```math
b_{P12,j,k}^{SEL2}
=
\theta_{P12,j,k}^{tail,SEL2}
+\theta_{P12,j,k}^{conn,SEL2},
```

where `theta_P12^tail` is the omitted Paper-12 AF loop-variation tail after
the finite-battery modulus `omega_j` is extracted, and `theta_P12^conn` is
the remaining connected-polymer tail from the same admissible loop stratum.

The zero-strength audit `P20-SEL2-T12-P12-ZERO` asserts

```math
\sum_{k\ge j}b_{P12,j,k}^{SEL2}\to0.
```

A sufficient diagonal form is to choose the row-tail truncation after the
finite `SEL2` row battery is fixed so that

```math
b_{P12,j,k}^{SEL2}\le2^{-(j+k)}
\qquad(k\ge j)
```

on a cofinal tail.

### Definition 4.3A.112: Loop-Representative Tail Audit

Let `ell_{j,k}^{SEL2}` be the declared level-`k` lattice/block representative
map for loops in the finite row battery, and set

```math
\delta_{app,j,k}^{SEL2}
:=
\sup_{\alpha\in B_{12,j}^{app,SEL2}}
d_{loop}^{(m)}(\alpha,\ell_{j,k}^{SEL2}\alpha).
```

`P20-SEL2-T12-APPLC-BOUND(U_{12}^{appLC,SEL2})` asserts that there are
nonnegative bounds `b_{appLC,j,k}^{SEL2}` such that

```math
\eta_{appLC,j,k}^{(12),SEL2}
\le b_{appLC,j,k}^{SEL2},
```

and

```math
\limsup_j\sum_{k\ge j}b_{appLC,j,k}^{SEL2}
\le U_{12}^{appLC,SEL2}<\infty.
```

A source-realized bound is

```math
b_{appLC,j,k}^{SEL2}
=
\omega_j(\delta_{app,j,k}^{SEL2})
+\epsilon_{app,j,k}^{(12),SEL2},
```

where `omega_j` is the Paper-16/Paper-12 finite-row loop modulus and
`epsilon_app^{(12)}` is the declared representative equivariance defect
inside the reduced `T_12` app/readout slot.

The zero-strength audit `P20-SEL2-T12-APPLC-ZERO` asserts

```math
\sum_{k\ge j}b_{appLC,j,k}^{SEL2}\to0.
```

This is a genuine schedule condition: `delta_app,j,k->0` for each fixed row
is not enough unless the resulting moduli and equivariance defects have a
vanishing cofinal row tail.

### Definition 4.3A.113: Finite Record Binning Tail Audit

Let `Q_{j,k}^{SEL2}` be the scalar finite-record binning map used for the
row-`j` loop-readout battery at shell `k`, and let

```math
\beta_{bin,j,k}^{SEL2}
:=
\sup_{F\in B_{12,j}^{app,SEL2}}
\|F-Q_{j,k}^{SEL2}F\|_{\infty}
```

be the rowwise binning mesh. `P20-SEL2-T12-BINLC-BOUND(U_{12}^{binLC,SEL2})`
asserts that there are nonnegative bounds `b_{binLC,j,k}^{SEL2}` such that

```math
\eta_{binLC,j,k}^{(12),SEL2}
\le b_{binLC,j,k}^{SEL2},
```

and

```math
\limsup_j\sum_{k\ge j}b_{binLC,j,k}^{SEL2}
\le U_{12}^{binLC,SEL2}<\infty.
```

A source-realized bound is

```math
b_{binLC,j,k}^{SEL2}
=
\nu_j(\beta_{bin,j,k}^{SEL2})
+\epsilon_{bin,j,k}^{(12),SEL2},
```

where `nu_j` is the finite-row scalar readout modulus and `epsilon_bin^{(12)}`
is the declared battery-restriction defect. The zero-strength audit
`P20-SEL2-T12-BINLC-ZERO` asserts

```math
\sum_{k\ge j}b_{binLC,j,k}^{SEL2}\to0.
```

Again, pointwise bin refinement on each fixed row is not enough without a
cofinal row-tail estimate.

### Theorem 4.3A.114: Loop-App/Readout Tail Decision

Assume `P20-SEL2-STDRED`, `P20-SEL2-TR-COMMON`,
`P19-T12-APP(A_{12}^{app,SEL2})`, and `P19-T12-EVAL` on the frozen `SEL2`
record law.

1. If the three finite bound audits

   ```text
   P20-SEL2-T12-P12-BOUND(U_12^P12,SEL2),
   P20-SEL2-T12-APPLC-BOUND(U_12^appLC,SEL2),
   P20-SEL2-T12-BINLC-BOUND(U_12^binLC,SEL2)
   ```

   hold, then

   ```math
   A_{12}^{app,eval,SEL2}
   \le
   U_{12}^{P12,SEL2}
   +U_{12}^{appLC,SEL2}
   +U_{12}^{binLC,SEL2}.
   ```

2. If the three zero-strength audits

   ```text
   P20-SEL2-T12-P12-ZERO,
   P20-SEL2-T12-APPLC-ZERO,
   P20-SEL2-T12-BINLC-ZERO
   ```

   hold, then

   ```math
   A_{12}^{app,eval,SEL2}=0.
   ```

3. Equivalently, the requested tail test

   ```math
   \sum_{k\ge j}
   \left(
   \eta_{P12,j,k}^{SEL2}
   +\eta_{appLC,j,k}^{(12),SEL2}
   +\eta_{binLC,j,k}^{(12),SEL2}
   \right)
   \to0
   ```

   is proved by proving the three component zero audits.

Proof.

Paper 19 Definition 8L.11A.21A defines `A_12^{app,eval}` as the limsup of
exactly these three nonnegative reduced tails. Definition 4.3A.110 records
the same split after the `SEL2` pushforward. The three component bound audits
therefore give clause 1 by limsup subadditivity. If all three component
tails tend to zero, their sum tends to zero, proving clause 2 and the
displayed requested tail test.

The definitions of the three component bounds match Paper 16 Definition
9X.1C: `eta_P12` is the residual Paper-12 modulus/connected-tail loss,
`eta_appLC` is the loop representative replacement loss, and `eta_binLC` is
the scalar record binning/battery-restriction loss. No term from `T_11`,
`T_14`, perimeter/cusp, smearing, endpoint/corner, or Paper-14 export is used
in this proof. `square`

### Corollary 4.3A.115: Reduced `T_12` Bucket Decision On `SEL2`

After the app/readout attack, the active easy-zero bucket may be written

```math
U_{EZ}^{SEL2,park,pcsa}
=
E_{14}^{SEL2}
+E_{corn}^{SEL2}
+X_{13}^{exact,SEL2}
+U_{12}^{per,SEL2}
+U_{12}^{cusp,SEL2}
+U_{12}^{smear,SEL2}
+U_{12}^{P12,SEL2}
+U_{12}^{appLC,SEL2}
+U_{12}^{binLC,SEL2},
```

under the finite component audits. Under the stronger same-record zero audits
for perimeter/cusp, smearing, and all three app/readout subtails,

```math
A_{12}^{per,eval,SEL2}
=A_{12}^{cusp,eval,SEL2}
=A_{12}^{smear,eval,SEL2}
=A_{12}^{app,eval,SEL2}
=0,
```

so the reduced `T_12` loop-readout contribution vanishes and the easy-zero
bucket reduces to

```math
U_{EZ}^{SEL2,park,T12zero}
=
E_{14}^{SEL2}
+E_{corn}^{SEL2}
+X_{13}^{exact,SEL2}.
```

Thus the reduced `T_12` bucket is now completely split and decided: it either
vanishes by six same-record cofinal zero audits, or it is carried as the
explicit finite sum of the six displayed component bounds. The next
pre-surface terms are the remaining carried `E_14`, `E_corn`,
`X_13^{exact}`, `U_11^{red}`, and `U_13^{entry,red}` in the scalar surplus
test.

### Definition 4.3A.116: Assembled Reduced `T_12` Package On `SEL2`

`P20-SEL2-T12-BOUND(U_{12}^{red,SEL2})` is the assembled finite bound audit
for the reduced loop-readout bucket. It is the conjunction of the finite
component audits

```text
P20-SEL2-T12-PC-BOUND(U_12^per,SEL2,U_12^cusp,SEL2),
P20-SEL2-T12-SMEAR-BOUND(U_12^smear,SEL2),
P20-SEL2-T12-P12-BOUND(U_12^P12,SEL2),
P20-SEL2-T12-APPLC-BOUND(U_12^appLC,SEL2),
P20-SEL2-T12-BINLC-BOUND(U_12^binLC,SEL2),
```

with

```math
U_{12}^{red,SEL2}
:=
U_{12}^{per,SEL2}
+U_{12}^{cusp,SEL2}
+U_{12}^{smear,SEL2}
+U_{12}^{P12,SEL2}
+U_{12}^{appLC,SEL2}
+U_{12}^{binLC,SEL2}.
```

`P20-SEL2-T12-ZERO` is the assembled zero audit. It is the conjunction of:

```text
P20-SEL2-T12-PC-ZERO,
P20-SEL2-T12-SMEAR-ZERO,
P20-SEL2-T12-P12-ZERO,
P20-SEL2-T12-APPLC-ZERO,
P20-SEL2-T12-BINLC-ZERO.
```

Equivalently, it asserts the six scalar cofinal tail tests

```math
\sum_{k\ge j}\eta_{perLC,j,k}^{SEL2}\to0,
\qquad
\sum_{k\ge j}\eta_{cuspLC,j,k}^{SEL2}\to0,
```

```math
\sum_{k\ge j}\eta_{smearLC,j,k}^{SEL2}\to0,
```

and

```math
\sum_{k\ge j}\eta_{P12,j,k}^{SEL2}\to0,
\qquad
\sum_{k\ge j}\eta_{appLC,j,k}^{(12),SEL2}\to0,
\qquad
\sum_{k\ge j}\eta_{binLC,j,k}^{(12),SEL2}\to0.
```

The endpoint/corner debit `E_corn^{SEL2}` is not part of
`P20-SEL2-T12-ZERO`; it remains the separate finite-template term already
decided in Corollary 4.3A.96.

### Theorem 4.3A.117: Step 1 Assembly Of The Reduced `T_12` Decision

Assume `P20-SEL2-STDRED`, `P20-SEL2-TR-COMMON`, `P19-T12-EVAL`, and the
reduced Paper-19 `T_12` source attacks on the frozen `SEL2` record law. Define

```math
R_{12}^{red,SEL2}
:=
A_{12}^{per,eval,SEL2}
+A_{12}^{cusp,eval,SEL2}
+A_{12}^{smear,eval,SEL2}
+A_{12}^{app,eval,SEL2}.
```

Then:

1. If `P20-SEL2-T12-BOUND(U_{12}^{red,SEL2})` holds, then

   ```math
   R_{12}^{red,SEL2}\le U_{12}^{red,SEL2}.
   ```

2. If `P20-SEL2-T12-ZERO` holds, then

   ```math
   R_{12}^{red,SEL2}=0.
   ```

3. The active easy-zero bucket after step 1 is therefore either the carried
   finite-bound package

   ```math
   U_{EZ}^{SEL2,step1}
   :=
   E_{14}^{SEL2}
   +E_{corn}^{SEL2}
   +X_{13}^{exact,SEL2}
   +U_{12}^{red,SEL2},
   ```

   or, under `P20-SEL2-T12-ZERO`, the reduced package

   ```math
   U_{EZ}^{SEL2,step1zero}
   :=
   E_{14}^{SEL2}
   +E_{corn}^{SEL2}
   +X_{13}^{exact,SEL2}.
   ```

Proof.

The perimeter/cusp assembly is Theorem 4.3A.104, the smearing assembly is
Theorem 4.3A.108, and the residual Paper-12/modulus, loop-representative, and
binning assembly is Theorem 4.3A.114. Adding the finite upper bounds gives
clause 1. If all six scalar cofinal tail tests vanish, each evaluated
`T_12` subconstant is zero, giving clause 2. Clause 3 is just the
substitution of `R_12^{red,SEL2}` into the parked `U_EZ` formula, keeping
`E_14`, `E_corn`, and `X_13^{exact}` separate because their zero tests are
not part of the reduced loop-readout package. `square`

### Definition 4.3A.118: Post-Step-1 `U_EZ` And Surplus Branches

After the reduced `T_12` assembly, define the conservative post-step-1
easy-zero ceiling by

```math
U_{EZ}^{SEL2,step1}
:=
E_{14}^{SEL2}
+E_{corn}^{SEL2}
+X_{13}^{exact,SEL2}
+U_{12}^{red,SEL2}.
```

Define the corresponding post-step-1 pre-surface ceiling and surplus:

```math
U_{pre13,std,red}^{SEL2,step1}
:=
U_{EZ}^{SEL2,step1}
+U_{11}^{red,SEL2}
+U_{13}^{entry,red,SEL2},
```

```math
\Pi_{pre13,std,red}^{SEL2,step1}
:=
\underline M_{loss}^{SEL2,20}
-U_{EZ}^{SEL2,step1}
-U_{11}^{red,SEL2}
-U_{13}^{entry,red,SEL2}.
```

If the assembled zero audit `P20-SEL2-T12-ZERO` is proved, define the
zero-`T_12` branch by

```math
U_{EZ}^{SEL2,step1zero}
:=
E_{14}^{SEL2}
+E_{corn}^{SEL2}
+X_{13}^{exact,SEL2},
```

```math
U_{pre13,std,red}^{SEL2,step1zero}
:=
U_{EZ}^{SEL2,step1zero}
+U_{11}^{red,SEL2}
+U_{13}^{entry,red,SEL2},
```

and

```math
\Pi_{pre13,std,red}^{SEL2,step1zero}
:=
\underline M_{loss}^{SEL2,20}
-U_{EZ}^{SEL2,step1zero}
-U_{11}^{red,SEL2}
-U_{13}^{entry,red,SEL2}.
```

These are bookkeeping consequences of step 1. They do not assert
`E_14^{SEL2}=0`, `E_corn^{SEL2}=0`, or `X_13^{exact,SEL2}=0`.

### Theorem 4.3A.119: Step 2 Recomputed `U_EZ` Pass Test

Assume `P20-SEL2-STDRED`, `P20-SEL2-TR-COMMON`, the reduced `T_12` source
attacks, and the finite post-decoration margin
`\underline M_{loss}^{SEL2,20}>0`.

1. On the conservative carried-`T_12` branch, the standard reduced `SEL2`
   route reaches the final surface-leading-rate test only if the available
   upper package proves

   ```math
   \Pi_{pre13,std,red}^{SEL2,step1}>0.
   ```

   Equivalently,

   ```math
   E_{14}^{SEL2}
   +E_{corn}^{SEL2}
   +X_{13}^{exact,SEL2}
   +U_{12}^{red,SEL2}
   +U_{11}^{red,SEL2}
   +U_{13}^{entry,red,SEL2}
   <
   \underline M_{loss}^{SEL2,20}.
   ```

2. On the stronger zero-`T_12` branch, the corresponding test is

   ```math
   \Pi_{pre13,std,red}^{SEL2,step1zero}>0,
   ```

   equivalently

   ```math
   E_{14}^{SEL2}
   +E_{corn}^{SEL2}
   +X_{13}^{exact,SEL2}
   +U_{11}^{red,SEL2}
   +U_{13}^{entry,red,SEL2}
   <
   \underline M_{loss}^{SEL2,20}.
   ```

3. Using the active endpoint/corner bound from Corollary 4.3A.96, the
   conservative sufficient inequality may be written as

   ```math
   E_{14}^{SEL2}
   +(16+N_{conc}^{SEL2})v_{corn}^{max}
   +X_{13}^{exact,SEL2}
   +U_{12}^{red,SEL2}
   +U_{11}^{red,SEL2}
   +U_{13}^{entry,red,SEL2}
   <
   \underline M_{loss}^{SEL2,20}.
   ```

   On the zero-`T_12` branch, delete `U_12^{red,SEL2}` from this display.

If either strict inequality is proved, the certified margin to use in the
surface-leading-rate theorem is the corresponding `Pi` from Definition
4.3A.118. If neither is proved, this upper-bound package has not certified
the branch past the pre-surface stage.

Proof.

Theorem 4.3A.117 replaces the four reduced `T_12` evaluated constants by
either the assembled finite ceiling `U_12^{red,SEL2}` or zero. Definition
4.3A.118 substitutes that result into the parked `U_EZ` bucket and then into
the standard reduced pre-surface surplus. Positivity of the resulting surplus
is exactly Theorem 4.3A.78's scalar sign test with the refined `U_EZ`
ceiling. The endpoint/corner inequality is Theorem 4.3A.94. As before,
failure to prove the strict upper inequality is not a falsification unless a
same-record lower-loss estimate proves the actual nonsurface debit consumes
the margin. `square`

### Definition 4.3A.120: Sharp `X_13^{exact}` Split On `SEL2`

For the row-`j` exact-entry battery `B_{13,j}^{exact,SEL2}` of Definition
4.3A.97, write

```math
B_{13,j}^{exact,SEL2}
=
B_{13,j}^{Creutz}
\cup B_{13,j}^{conn}
\cup B_{13,j}^{const},
```

where `B_Creutz` contains the four Creutz loop records, `B_conn` contains the
finite connected-entry products used by the surface-entry proof, and
`B_const` contains the finite scalar block records used to read
`u_{\rho,s_0,j}`, `A_{C,j}`, `B_{C,j}`, `xi_{C,j}`, `xi'_{C,j}`, and
`N_j(C)`.

Define the two exact-comparison components

```math
D_{13,j}^{cut,SEL2}
:=
\sup_{F\in B_{13,j}^{exact,SEL2}}
\left|
\mathbb E_{\mu_{a_j,s_0}^{blk,SEL2}}F
-
\mathbb E_{\mu_{s_0}^{blk,SEL2}}F
\right|,
```

and

```math
R_{13,j}^{read,SEL2}:=\epsilon_{read,j}^{(13),SEL2}.
```

Thus

```math
X_{13,j}^{exact,SEL2}
=
D_{13,j}^{cut,SEL2}
+R_{13,j}^{read,SEL2}.
```

The sharp carried value is

```math
X_{13}^{sharp,SEL2}
:=
\limsup_j
\left(
D_{13,j}^{cut,SEL2}
+R_{13,j}^{read,SEL2}
\right).
```

The component carried bounds are

```math
U_{13}^{cut,SEL2}:=\limsup_jD_{13,j}^{cut,SEL2},
\qquad
U_{13}^{read,SEL2}:=\limsup_jR_{13,j}^{read,SEL2},
```

when the two limsups are finite. Then

```math
X_{13}^{exact,SEL2}
\le
X_{13}^{sharp,SEL2}
\le
U_{13}^{cut,SEL2}+U_{13}^{read,SEL2}.
```

The first inequality is equality if `X_13^{exact,SEL2}` is defined as the
sharp limsup of the displayed rowwise discrepancies. The second inequality is
the separated carried-bound version used when the two component audits are
proved independently.

### Definition 4.3A.121: Exact-Entry Block-Convergence Audit For `X_13`

`P20-SEL2-X13-BC0` is the zero-strength cutoff-to-exact block-convergence
audit. It asserts:

1. the exact whole-process block pushforward `mu_{s_0}^{blk,SEL2}` is the
   same scalar law used by `P20-SEL2-TR-COMMON`;
2. for each row `j`, the battery `B_{13,j}^{exact,SEL2}` is finite and
   declared before choosing the cutoff `a_j`;
3. Paper 13's block-convergence/uniqueness gate holds on that finite battery,
   equivalently every subsequential block limit gives the same values on all
   records in `B_{13,j}^{exact,SEL2}`;
4. the cutoffs can be chosen diagonally so that

   ```math
   D_{13,j}^{cut,SEL2}\to0.
   ```

This is exactly the moving-battery strengthening of Paper 13 Definition
7.30F clause 1 and Theorem 7.30AC, restricted to the finite scalar records
used by the Paper-19 exact-entry comparison. It is not an area-law assumption
and does not assert a surface-polymer leading coefficient. It only asserts
convergence of the finite block-record expectations being compared.

The finite-bound version `P20-SEL2-X13-BCBOUND(U_{13}^{cut,SEL2})` asserts

```math
\limsup_jD_{13,j}^{cut,SEL2}
\le U_{13}^{cut,SEL2}<\infty.
```

### Definition 4.3A.122: Exact Scalar Readout Audit For `X_13`

`P20-SEL2-X13-READ0` is the zero-strength exact scalar readout audit. It
asserts that the row battery contains the exact scalar records needed by the
surface-entry proof and that their readout maps are not finite-precision
approximations. Equivalently,

```math
R_{13,j}^{read,SEL2}
=\epsilon_{read,j}^{(13),SEL2}
=0
```

on a cofinal tail.

The finite-bound version `P20-SEL2-X13-READBOUND(U_{13}^{read,SEL2})`
asserts

```math
\limsup_jR_{13,j}^{read,SEL2}
\le U_{13}^{read,SEL2}<\infty.
```

For an operational finite-readout route, a sufficient source form is

```math
R_{13,j}^{read,SEL2}
\le
\nu_{13,j}^{SEL2}(\beta_{13,j}^{SEL2})
+\epsilon_{13,j}^{prec,SEL2},
```

where `beta_13,j` is the scalar readout mesh on
`B_{13,j}^{exact,SEL2}`, `nu_13,j` is the finite-row readout modulus, and
`epsilon_13,j^prec` is the declared precision defect. The readout-zero route
requires the right-hand side to tend to zero cofinally.

### Theorem 4.3A.123: `X_13^{exact,SEL2}` Zero Or Sharp Carried Bound

Assume `P20-SEL2-STDRED` and `P20-SEL2-TR-COMMON`.

1. If `P20-SEL2-X13-BC0` and `P20-SEL2-X13-READ0` hold, then

   ```math
   X_{13}^{exact,SEL2}=0.
   ```

2. If instead the finite component bounds

   ```text
   P20-SEL2-X13-BCBOUND(U_13^cut,SEL2),
   P20-SEL2-X13-READBOUND(U_13^read,SEL2)
   ```

   hold, then

   ```math
   X_{13}^{exact,SEL2}
   \le
   X_{13}^{sharp,SEL2}
   \le
   U_{13}^{cut,SEL2}+U_{13}^{read,SEL2}.
   ```

3. The strongest honest carried value is `X_13^{sharp,SEL2}` itself. The
   separated sum `U_13^{cut,SEL2}+U_13^{read,SEL2}` is used only when the
   cutoff-convergence and readout estimates are sourced separately.

Proof.

Definition 4.3A.120 gives the exact rowwise identity
`X_{13,j}^{exact,SEL2}=D_{13,j}^{cut,SEL2}+R_{13,j}^{read,SEL2}`. If
`D_{13,j}^{cut,SEL2}->0` and `R_{13,j}^{read,SEL2}->0`, then the limsup is
zero. This proves clause 1.

For clause 2, take limsup in the same rowwise identity and use limsup
subadditivity. Clause 3 is just the observation that a limsup of a sum can be
strictly smaller than the sum of the component limsups; therefore the direct
quantity `X_13^{sharp,SEL2}` is the sharper carried value whenever it is
available. `square`

### Corollary 4.3A.124: Post-`X_13` Surplus Branches

After the `X_13` attack, the conservative post-step-1 surplus can be sharpened
to

```math
\Pi_{pre13,std,red}^{SEL2,step1X}
:=
\underline M_{loss}^{SEL2,20}
-E_{14}^{SEL2}
-E_{corn}^{SEL2}
-X_{13}^{sharp,SEL2}
-U_{12}^{red,SEL2}
-U_{11}^{red,SEL2}
-U_{13}^{entry,red,SEL2},
```

or, using only separated component bounds,

```math
\Pi_{pre13,std,red}^{SEL2,step1Xbd}
:=
\underline M_{loss}^{SEL2,20}
-E_{14}^{SEL2}
-E_{corn}^{SEL2}
-U_{13}^{cut,SEL2}
-U_{13}^{read,SEL2}
-U_{12}^{red,SEL2}
-U_{11}^{red,SEL2}
-U_{13}^{entry,red,SEL2}.
```

On the zero-`T_12` branch delete `U_12^{red,SEL2}`. On the exact
`X_13`-zero branch delete `X_13^{sharp,SEL2}` or the two separated `U_13`
component bounds. Thus the next live scalar terms, after `T_12` and
`X_13`, are still `E_14^{SEL2}`, `E_corn^{SEL2}`, `U_11^{red,SEL2}`, and
`U_13^{entry,red,SEL2}`.

### Corollary 4.3A.125: Honest Decision Of The `X_13` Attack

Current Paper-13/Paper-19 imports reduce `X_13^{exact,SEL2}` to a precise
finite-record question. They do not, by themselves, prove
`P20-SEL2-X13-BC0` on the moving `SEL2` exact-entry batteries. That requires
the Paper-13 block-limit uniqueness/convergence gate on those scalar records,
plus a diagonal cutoff schedule. Therefore the present honest status is:

1. `X_13^{exact,SEL2}=0` is available only under
   `P20-SEL2-X13-BC0 + P20-SEL2-X13-READ0`;
2. otherwise carry the sharp value `X_13^{sharp,SEL2}` if directly evaluated;
3. if only component estimates are available, carry
   `U_13^{cut,SEL2}+U_13^{read,SEL2}`.

This is a real source estimate, not a formal ledger identity. In particular,
the cutoff-to-exact block-convergence clause cannot be replaced by the
surface area-law conclusion that Paper 20 is trying to reach.

### Definition 4.3A.126: Active Carried `X_13` Value On `SEL2`

For the current standard reduced `SEL2` branch, define the active carried
exact-comparison debit `X_{13}^{car,SEL2}` by the following priority rule.

1. If `P20-SEL2-X13-BC0` and `P20-SEL2-X13-READ0` are both proved, set

   ```math
   X_{13}^{car,SEL2}:=0.
   ```

2. If the sharp rowwise value is directly evaluated, set

   ```math
   X_{13}^{car,SEL2}:=X_{13}^{sharp,SEL2}.
   ```

3. If only separated component estimates are available, set

   ```math
   X_{13}^{car,SEL2}
   :=
   U_{13}^{cut,SEL2}+U_{13}^{read,SEL2}.
   ```

The branch is admissible only if the chosen value is finite and satisfies

```math
0\le X_{13}^{exact,SEL2}\le X_{13}^{car,SEL2}<\infty.
```

This convention freezes the `X_13` term before any later transport work. In
particular, no later `T_11`, `T_12`, `T_14`, endpoint/corner, or surface-entry
estimate may reabsorb this cutoff-to-exact/readout debit.

### Definition 4.3A.127: Active Finite `E_14` And `E_corn` Debits

For the same current standard reduced `SEL2` branch, define

```math
E_{14}^{car,SEL2}:=E_{14}^{SEL2},
```

where `E_14^{SEL2}` is the finite Paper-14 export debit imported by
`P19-P14-EXPORT(E_14^{SEL2})`. The replacement `E_14^{car,SEL2}=0` is allowed
only if `P20-SEL2-P14-COMP`, or an equivalent same-record Paper-14
tail-normalized component audit, is proved.

For the endpoint/corner debit, set

```math
E_{corn}^{car,SEL2}:=E_{corn}^{SEL2},
```

with the active finite bound

```math
0\le E_{corn}^{car,SEL2}
\le
(16+N_{conc}^{SEL2})v_{corn}^{max}.
```

The replacement `E_corn^{car,SEL2}=0` is allowed only under one of the
zero-weight, empty-template, or new-selector audits of Theorem 4.3A.95. On
the current corner-separated branch this zero replacement is not used.

Thus the active easy-zero block after the reduced `T_12` attack and the
`X_13` attack is

```math
U_{EZ}^{car,SEL2}
:=
E_{14}^{car,SEL2}
+E_{corn}^{car,SEL2}
+X_{13}^{car,SEL2}
+U_{12}^{red,SEL2}.
```

On the proved `P20-SEL2-T12-ZERO` branch the final term is deleted.

### Definition 4.3A.128: Active Reduced `T_11` Source Package

`P20-SEL2-T11-ACT(U_{11}^{loc},U_{11}^{RP},U_{11}^{Cov},U_{11}^{gauge})`
is the active same-record reduced `T_11` source package. It consists of:

1. the evaluated local-RG tail of Definition 4.3A.70,

   ```math
   U_{11}^{loc}=U_{11}^{loc,eval};
   ```

2. the evaluated reflection-positivity/projective residual tail,

   ```math
   U_{11}^{RP}=U_{11}^{RP,eval};
   ```

3. the evaluated Euclidean-covariance transport tail,

   ```math
   U_{11}^{Cov}=U_{11}^{Cov,eval};
   ```

4. the evaluated scalar gauge/chart reconstruction tail,

   ```math
   U_{11}^{gauge}=U_{11}^{gauge,eval};
   ```

5. the same debit-exclusion convention used by `P20-SEL2-TR-COMMON`: perimeter,
   cusp, smearing, loop-approximant/readout, Paper-14 export,
   endpoint/corner, `X_13`, and exact-entry surface terms are not charged in
   this package.

The active reduced `T_11` ceiling is

```math
U_{11}^{act,SEL2}
:=
U_{11}^{loc,eval}
+U_{11}^{RP,eval}
+U_{11}^{Cov,eval}
+U_{11}^{gauge,eval}.
```

This is the same mathematical object as `U_{11}^{red,SEL2}`, now frozen after
the `E_14`, `E_corn`, `X_13`, and reduced `T_12` branches have been fixed.

### Theorem 4.3A.129: Active Reduced `T_11` Bound And Zero Test

Assume `P20-SEL2-STDRED`, `P20-SEL2-TR-COMMON`, and the active source package
`P20-SEL2-T11-ACT`. Then the active reduced `T_11` contribution satisfies

```math
0\le T_{11}^{red,SEL2}\le U_{11}^{act,SEL2}.
```

Moreover,

```math
U_{11}^{act,SEL2}=0
```

if and only if all four evaluated tails vanish:

```math
U_{11}^{loc,eval}
=U_{11}^{RP,eval}
=U_{11}^{Cov,eval}
=U_{11}^{gauge,eval}
=0.
```

Proof.

Definition 4.3A.70 evaluates the four reduced `T_11` limsup tails on the
frozen `SEL2` scalar record law, and Theorem 4.3A.71 proves the corresponding
block bound and zero decision. Definition 4.3A.128 does not introduce a new
estimate; it fixes the active branch after the earlier parked debits have
been assigned and explicitly excludes all terms already paid by `E_14`,
`E_corn`, `X_13`, reduced `T_12`, or exact-entry transport. Therefore
Theorem 4.3A.71 gives the displayed bound and zero criterion without double
charging. `square`

### Corollary 4.3A.130: Active Steps 1--3 Pre-Surface Surplus

After freezing the active `X_13` value, carrying the finite `E_14` and
`E_corn` debits, and applying the reduced `T_11` attack, the current standard
reduced `SEL2` branch reaches the final surface-rate test if

```math
\Pi_{pre13,std,red}^{SEL2,1\text{--}3}
:=
\underline M_{loss}^{SEL2,20}
-E_{14}^{car,SEL2}
-E_{corn}^{car,SEL2}
-X_{13}^{car,SEL2}
-U_{12}^{red,SEL2}
-U_{11}^{act,SEL2}
-U_{13}^{entry,red,SEL2}
>0.
```

On the proved `P20-SEL2-T12-ZERO` branch, delete `U_12^{red,SEL2}`. If the
strict inequality is not proved, the `SEL2` branch has not reached the final
`T_13` leading-rate comparison. This is an undecided loss-budget failure, not
by itself a falsification, unless a matching lower estimate proves the left
side is nonpositive.

### Corollary 4.3A.131: Honest Status After Steps 1--3

Steps 1--3 are now complete as a same-record reduction:

1. `X_13` is frozen as `X_13^{car,SEL2}`;
2. `E_14` and `E_corn` are finite carried debits on the current branch;
3. the reduced `T_11` bucket is bounded by `U_11^{act,SEL2}` and is zero only
   under the four cofinal vanishing tests of Theorem 4.3A.129.

No unconditional `SEL2` pass follows from these reductions alone. The next
unpaid nonsurface term is the exact-entry residual bucket
`U_{13}^{entry,red,SEL2}`. Once that is evaluated on the same frozen scalar
record law, Corollary 4.3A.130 gives the scalar pre-surface pass/fail test.

### Definition 4.3A.132: Active Exact-Entry Component Audits On `SEL2`

On the frozen standard reduced `SEL2` branch, define the active component
audits for the exact-entry residuals as follows.

1. `P20-SEL2-ENTRY-BC(U_{13}^{BC,car})` holds when the rowwise block
   convergence defect for the Paper-13 actual-entry battery obeys

   ```math
   \limsup_j\epsilon_{BC,j}^{SEL2}
   \le U_{13}^{BC,car}<\infty.
   ```

   The zero version, `P20-SEL2-ENTRY-BC0`, asserts
   `epsilon_{BC,j}^{SEL2}->0`. By Paper 13 Theorem 7.30AC, this is sourced by
   block-limit uniqueness on the finite block record algebra generated by the
   row battery. It is stronger than compactness and is not supplied by
   asymptotic freedom alone.

2. `P20-SEL2-ENTRY-CE(U_{13}^{CE,car})` holds when the exact-entry central
   extraction residual obeys

   ```math
   \limsup_j\epsilon_{CE,j}^{SEL2}
   \le U_{13}^{CE,car}<\infty.
   ```

   The zero version, `P20-SEL2-ENTRY-CE0`, asserts
   `epsilon_{CE,j}^{SEL2}->0`. This is the Paper-13 `CE` gate on the same
   pushed-forward block law: Peter-Weyl regularity, a positive subunit
   `rho` coefficient, and a finite non-leading character tail. It is not the
   later positive-rate inequality for `kappa_13^{CE}`.

3. `P20-SEL2-ENTRY-RPF(U_{13}^{RPF,car})` holds when

   ```math
   \limsup_j\epsilon_{RPF,j}^{SEL2}
   \le U_{13}^{RPF,car}<\infty,
   ```

   with zero version `epsilon_{RPF,j}^{SEL2}->0`. Its source is the Paper-13
   residual factorization gate: the exact block density, after extracting the
   central plaquette factors, must have a local compatible polymer
   representation. This is an exact pushed-forward record statement, not a
   gauge-fixed field ontology.

4. `P20-SEL2-ENTRY-KPDEC(U_{13}^{KPdec,car})` holds when

   ```math
   \limsup_j\epsilon_{KPdec,j}^{SEL2}
   \le U_{13}^{KPdec,car}<\infty,
   ```

   with zero version `epsilon_{KPdec,j}^{SEL2}->0`. This is the entry-level
   Paper-13 `KP_dec` comparison: non-leading character insertions and
   residual polymers must be controlled by one compatible KP decoration gas.
   It is not the global decoration debit already paid through
   `D_dec^{SEL2,20}`.

5. `P20-SEL2-ENTRY-SUB-RED` is the reduced-branch placement convention

   ```math
   \epsilon_{SUB,j}^{SEL2}=0
   ```

   inside the entry bucket. This is allowed only because the branch pays
   surface subcriticality later through the `T_13` leading-rate inequality. If
   a branch pays `SUB` here, it must instead declare
   `P20-SEL2-ENTRY-SUB(U_{13}^{SUB,car})` with
   `limsup_j epsilon_{SUB,j}^{SEL2}<=U_{13}^{SUB,car}` and remove the same
   debit from the later surface bucket.

6. `P20-SEL2-ENTRY-WP(U_{13}^{WP,car})` holds when

   ```math
   \limsup_j\epsilon_{WP,j}^{SEL2}
   \le U_{13}^{WP,car}<\infty,
   ```

   with zero version `epsilon_{WP,j}^{SEL2}->0`. This is whole-process
   compatibility of the certificate under the regulator/chart ledgers. It is
   not the Paper-14 export norm and does not assert Lorentz covariance or a
   Markovian subprocess.

The reduced active entry ceiling is

```math
U_{13}^{entry,act,SEL2}
:=
U_{13}^{BC,car}
+U_{13}^{CE,car}
+U_{13}^{RPF,car}
+U_{13}^{KPdec,car}
+U_{13}^{WP,car},
```

with `SUB` absent only under `P20-SEL2-ENTRY-SUB-RED`. The unreduced variant is

```math
U_{13}^{entry,full,act,SEL2}
:=
U_{13}^{entry,act,SEL2}+U_{13}^{SUB,car}.
```

### Lemma 4.3A.133: Paper-13 Source Routes For The Six Entry Residuals

The component audits of Definition 4.3A.132 have the following source routes.

1. `BC` is sourced by `BLU(s_0,L)` on the active row batteries, by Paper 13
   Theorem 7.30AC.
2. `CE` is sourced by the Paper-13 character extraction gate, equivalently by
   Peter-Weyl regularity plus the coefficient sign/subunit/tail inequalities
   of Paper 13 Proposition 7.30AF, on the same block plaquette marginal.
3. `RPF` and `KPdec` are jointly sourced by the connected-cumulant KP
   criterion of Paper 13 Theorem 7.30AS, after central extraction has fixed
   the product plaquette factors.
4. `SUB` is sourced either by Paper 13 Proposition 7.30AI / Paper 19
   `P19-T13-SUB`, or is absent from the entry bucket under the reduced
   placement convention.
5. `WP` is sourced by the whole-process certificate clause of Paper 13
   Definition 7.30Y, on the same pushed-forward scalar record law used by
   `P20-SEL2-TR-COMMON`.

None of these source routes is an area-law conclusion. The dangerous points
are exactly `BC`, `CE`, `RPF`, `KPdec`, and `WP`: they must be proved as
record-law estimates before the surface-leading-rate theorem is invoked.

Proof.

The source identifications are the clauses of Paper 13 Definition 7.30Y.
Theorem 7.30Z proves that those six gates imply `ACSB`; Theorem 7.30V
transports `ACSB` to strong-block entry; Theorem 7.30M gives exact RG entry;
and Theorem 7.30G gives the resulting `RSB` entry. Paper 19 Definition
8L.11A.24 records the same six defects as the entry transport debit. The
reduced `SUB` convention is a ledger placement: the same subcriticality
defect cannot be charged both in entry and in the later surface-rate
inequality. `square`

### Theorem 4.3A.134: Active Exact-Entry Bound And Zero Decision

Assume `P20-SEL2-STDRED`, `P20-SEL2-TR-COMMON`, the active component audits
`P20-SEL2-ENTRY-BC`, `P20-SEL2-ENTRY-CE`,
`P20-SEL2-ENTRY-RPF`, `P20-SEL2-ENTRY-KPDEC`,
`P20-SEL2-ENTRY-WP`, and the reduced placement convention
`P20-SEL2-ENTRY-SUB-RED`. Then

```math
0\le A_{13}^{entry,SEL2}
\le
U_{13}^{entry,act,SEL2}.
```

Moreover, the reduced entry bucket vanishes if

```math
\epsilon_{BC,j}^{SEL2}\to0,\quad
\epsilon_{CE,j}^{SEL2}\to0,\quad
\epsilon_{RPF,j}^{SEL2}\to0,\quad
\epsilon_{KPdec,j}^{SEL2}\to0,\quad
\epsilon_{WP,j}^{SEL2}\to0,
```

and `SUB` is placed only in the later surface-rate test. Under those clauses,

```math
U_{13}^{entry,act,SEL2}=0.
```

If the branch does not use the reduced placement convention, the bound becomes

```math
A_{13}^{entry,SEL2}
\le
U_{13}^{entry,full,act,SEL2}
=U_{13}^{entry,act,SEL2}+U_{13}^{SUB,car}.
```

Proof.

Paper 19 Definition 8L.11A.24 gives the rowwise estimate

```math
R_{13,j}^{entry}
\le
\epsilon_{BC,j}
+\epsilon_{CE,j}
+\epsilon_{RPF,j}
+\epsilon_{KPdec,j}
+\epsilon_{SUB,j}
+\epsilon_{WP,j}.
```

Restrict this estimate to the frozen `SEL2` scalar record law. Under the
reduced convention, `epsilon_SUB` is not part of the entry ledger. Taking
limsups and using subadditivity gives the displayed active bound. If each
remaining component tends to zero, every component limsup is zero and hence
the reduced entry ceiling vanishes. The unreduced formula is the same
calculation with `SUB` restored. `square`

### Corollary 4.3A.135: Post-Entry Active Surplus

After the exact-entry attack, the active standard reduced `SEL2` branch has
the scalar pre-surface surplus

```math
\Pi_{pre13,std,red}^{SEL2,entry}
:=
\underline M_{loss}^{SEL2,20}
-E_{14}^{car,SEL2}
-E_{corn}^{car,SEL2}
-X_{13}^{car,SEL2}
-U_{12}^{red,SEL2}
-U_{11}^{act,SEL2}
-U_{13}^{entry,act,SEL2}.
```

On the zero reduced `T_12` branch delete `U_12^{red,SEL2}`. On the unreduced
entry branch replace `U_13^{entry,act,SEL2}` by
`U_13^{entry,full,act,SEL2}`.

If

```math
\Pi_{pre13,std,red}^{SEL2,entry}>0,
```

the branch reaches the final surface-leading-rate comparison. If this strict
inequality is not proved, Paper 20 has not closed the loss headline on the
current branch.

### Corollary 4.3A.136: Honest Status Of The Entry Attack

The exact-entry attack is now expanded into its real dynamical components:

```math
\epsilon_{BC}
+\epsilon_{CE}
+\epsilon_{RPF}
+\epsilon_{KPdec}
+\epsilon_{SUB}
+\epsilon_{WP}.
```

On the preferred reduced branch, `epsilon_SUB` is placed in the later surface
subcriticality/leading-rate test and is not charged in
`U_13^{entry,act,SEL2}`. The remaining five terms are not formalities:

1. `BC` requires block-limit uniqueness for the pushed-forward block records;
2. `CE` requires the actual central coefficient extraction window;
3. `RPF` requires exact local residual factorization;
4. `KPdec` requires a compatible KP decoration gas for residuals plus
   non-leading characters;
5. `WP` requires the whole-process certificate to be independent of the
   regulator/chart bookkeeping.

Current source papers reduce these five estimates to the named Paper-13
gates. They do not prove them unconditionally for four-dimensional `SU(N)`.
Thus Paper 20 has sharpened the obstruction: the remaining nonsurface problem
is no longer an unnamed `U_13^{entry}` bucket, but the five same-record
source estimates above, plus the final surface-rate test.

### Definition 4.3A.137: Post-Entry Debit Worksheet On `SEL2`

On the active standard reduced branch, define the post-entry nonsurface debit
ceiling

```math
\mathcal U_{post}^{SEL2,entry}
:=
E_{14}^{car,SEL2}
+E_{corn}^{car,SEL2}
+X_{13}^{car,SEL2}
+U_{12}^{red,SEL2}
+U_{11}^{act,SEL2}
+U_{13}^{entry,act,SEL2}.
```

On the zero reduced-loop-readout branch, define

```math
\mathcal U_{post,0T12}^{SEL2,entry}
:=
E_{14}^{car,SEL2}
+E_{corn}^{car,SEL2}
+X_{13}^{car,SEL2}
+U_{11}^{act,SEL2}
+U_{13}^{entry,act,SEL2}.
```

The certified post-decoration margin from the `C_area=20` `SEL2` worksheet is

```math
\underline M_{loss}^{SEL2,20}
=
\exp(L_{20})
-
\exp\!\left(
{20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right),
```

where

```math
L_{20}=\log(1+Sig_{AFM}^{SEL2}),
\qquad
\widehat\eta_{*,20}
={1\over2}(\tau_{20}+\bar\eta_{res,20}),
\qquad
\tau_{20}={L_{20}\over20+L_{20}}.
```

Equivalently,

```math
\underline M_{loss}^{SEL2,20}
=
Sig_{AFM}^{SEL2}
-
\left[
\exp\!\left(
{20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right)-1
\right].
```

Thus the bracketed term is exactly the certified `C_area=20` decoration debit.

### Theorem 4.3A.138: Computed Post-Entry Surplus

Assume the frozen `SEL2` worksheet of Theorem 4.3A.51, the active carried
branches of Definitions 4.3A.126--4.3A.128, and the active exact-entry audits
of Definition 4.3A.132. Then the computed post-entry surplus is

```math
\Pi_{pre13,std,red}^{SEL2,entry}
=
\underline M_{loss}^{SEL2,20}
-
\mathcal U_{post}^{SEL2,entry}.
```

Expanding every active term,

```math
\Pi_{pre13,std,red}^{SEL2,entry}
=
\exp(L_{20})
-
\exp\!\left(
{20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right)
-E_{14}^{car,SEL2}
-E_{corn}^{car,SEL2}
-X_{13}^{car,SEL2}
-U_{12}^{red,SEL2}
-U_{11}^{act,SEL2}
-U_{13}^{entry,act,SEL2}.
```

Equivalently,

```math
\Pi_{pre13,std,red}^{SEL2,entry}
=
Sig_{AFM}^{SEL2}
-D_{dec}^{SEL2,20}
-E_{14}^{car,SEL2}
-E_{corn}^{car,SEL2}
-X_{13}^{car,SEL2}
-U_{12}^{red,SEL2}
-U_{11}^{act,SEL2}
-U_{13}^{entry,act,SEL2},
```

where

```math
D_{dec}^{SEL2,20}
:=
\exp\!\left(
{20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right)-1.
```

On the zero reduced-loop-readout branch,

```math
\Pi_{pre13,std,red,0T12}^{SEL2,entry}
=
\underline M_{loss}^{SEL2,20}
-
\mathcal U_{post,0T12}^{SEL2,entry}.
```

Proof.

Definition 4.3A.137 is the active debit sum after the decoration debit has
already been subtracted into `underline M_loss^{SEL2,20}`. Corollary 4.3A.135
gives the same expression term by term. The equality with the signal floor
uses `exp(L_20)=1+Sig_AFM^{SEL2}`. The zero-`T_12` formula is the same sum
after deleting the reduced loop-readout debit, which is allowed only under
`P20-SEL2-T12-ZERO`. `square`

### Corollary 4.3A.139: Post-Entry Decision

The active standard reduced `SEL2` branch reaches the final surface-leading
comparison if and only if the available upper package proves

```math
\mathcal U_{post}^{SEL2,entry}
<
\underline M_{loss}^{SEL2,20}.
```

Equivalently,

```math
\Pi_{pre13,std,red}^{SEL2,entry}>0.
```

Using the currently proved endpoint/corner bound, a sufficient explicit
condition is

```math
E_{14}^{car,SEL2}
+(16+N_{conc}^{SEL2})v_{corn}^{max}
+X_{13}^{car,SEL2}
+U_{12}^{red,SEL2}
+U_{11}^{act,SEL2}
+U_{13}^{entry,act,SEL2}
<
\underline M_{loss}^{SEL2,20}.
```

On the zero reduced-loop-readout branch, delete `U_12^{red,SEL2}` from the
left-hand side. On an exact `X_13`-zero branch, delete `X_13^{car,SEL2}`. On
an exact Paper-14 export branch, delete `E_14^{car,SEL2}`. On a no-corner or
zero-corner branch, delete the endpoint/corner term only after re-auditing the
selector's decoration register.

With the current source imports, this scalar inequality is not decided
numerically: the active carried constants

```math
E_{14}^{car,SEL2},\quad
X_{13}^{car,SEL2},\quad
U_{12}^{red,SEL2},\quad
U_{11}^{act,SEL2},\quad
U_{13}^{entry,act,SEL2}
```

are finite source ceilings but are not supplied with values sharp enough to
prove the strict inequality. Therefore Paper 20 has computed the post-entry
surplus as an exact symbolic scalar test; it has not proved that the test is
positive.

### Definition 4.3A.140: Active `BC` Battery And Oscillation On `SEL2`

Let `\mathcal B_{BC,j}^{SEL2}` be the finite scalar block-record battery used
by the row-`j` exact-entry proof. It contains the active Creutz loop records,
the finite connected products used in the entry chain, and the scalar
block-plaquette/coefficient records needed by `CE`, `RPF`, `KPdec`, and `WP`.
It is declared before choosing any cutoff subsequence.

For fixed row `j`, let `\mathfrak C_{BC,j}^{SEL2}` be the set of subsequential
weak limits of the cutoff block pushforwards
`\mu_{a,s_0}^{blk,SEL2}` restricted to the finite record algebra generated by
`\mathcal B_{BC,j}^{SEL2}`. By Paper 13 Lemma 7.30AA this cluster set is
nonempty and compact.

Define the block-limit oscillation

```math
\omega_{BC,j}^{SEL2}
:=
\sup_{F\in\mathcal B_{BC,j}^{SEL2}}
\sup_{\mu,\nu\in\mathfrak C_{BC,j}^{SEL2}}
\left|
\mathbb E_\mu F-\mathbb E_\nu F
\right|.
```

Define also the row battery norm

```math
B_{BC,j}^{SEL2}
:=
\max_{F\in\mathcal B_{BC,j}^{SEL2}}\|F\|_\infty,
\qquad
B_{BC}^{SEL2}:=\limsup_j B_{BC,j}^{SEL2}.
```

For normalized Wilson/character scalar records, `B_BC^SEL2<=1`. If an
unnormalized character convention is used, `B_BC^SEL2` must be audited on the
same row battery before this branch uses the bound below.

### Lemma 4.3A.141: Compactness Gives Only A Finite `BC` Ceiling

Assume `P20-SEL2-STDRED` and `P20-SEL2-TR-COMMON`, and assume
`B_{BC}^{SEL2}<\infty`. Then the active `BC` residual has the finite fallback
bound

```math
0\le U_{13}^{BC,car}\le 2B_{BC}^{SEL2}.
```

In particular, under normalized scalar records,

```math
U_{13}^{BC,car}\le2.
```

Proof.

For every bounded scalar record `F` and every pair of probability laws
`\mu,\nu`,

```math
\left|\mathbb E_\mu F-\mathbb E_\nu F\right|
\le2\|F\|_\infty.
```

Taking the supremum over the finite row battery and then `limsup_j` gives the
bound. Compactness supplies subsequential limits, so the oscillation is
well-defined, but the estimate is only a boundedness statement. It does not
prove convergence or uniqueness of the block limit. `square`

### Definition 4.3A.142: `SEL2` Block-Limit Uniqueness Audit

`P20-SEL2-BC-BLU` is the active block-limit uniqueness audit. It asserts:

1. for each row `j`, every pair of subsequential cutoff block limits gives
   the same values on every record in `\mathcal B_{BC,j}^{SEL2}`;
2. the exact block law `\mu_{s_0}^{blk,SEL2}` used by the later `CE`, `RPF`,
   `KPdec`, `WP`, `X_13`, and surface-rate records is this unique row limit;
3. the cutoff schedule can be chosen diagonally over the moving row batteries
   so that

   ```math
   \epsilon_{BC,j}^{SEL2}\to0.
   ```

Equivalently,

```math
\omega_{BC,j}^{SEL2}\to0
```

and the selected exact law is the corresponding unique block-record limit on
the active row battery.

### Theorem 4.3A.143: `BC` Zero Is Exactly Moving-Battery `BLU`

Assume `P20-SEL2-STDRED`, `P20-SEL2-TR-COMMON`, and the active finite batteries
of Definition 4.3A.140.

1. If `P20-SEL2-BC-BLU` holds, then

   ```math
   P20\text{-}SEL2\text{-}ENTRY\text{-}BC0
   ```

   holds, hence

   ```math
   U_{13}^{BC,car}=0.
   ```

2. Conversely, if `P20-SEL2-ENTRY-BC0` holds for the active row batteries and
   the exact law used downstream is the cutoff limit read by those batteries,
   then `P20-SEL2-BC-BLU` holds.

3. Without `P20-SEL2-BC-BLU`, Paper 20 may carry the finite bound of Lemma
   4.3A.141, but it may not erase the `BC` debit.

Proof.

Paper 13 Theorem 7.30AC proves that, on a finite block-record algebra,
block convergence is equivalent to block-limit uniqueness. Clause 1 is that
the same equivalence holds rowwise and diagonally for the active moving
`SEL2` batteries: uniqueness makes every subsequential limit agree on the
row battery, so the cutoff expectations converge to the selected exact block
law and `epsilon_BC,j^{SEL2}->0`.

For clause 2, if the rowwise cutoff expectations converge to the selected
exact law on the active battery, then any two subsequential limits have the
same expectations on that battery. This is exactly rowwise block-limit
uniqueness. Clause 3 is Lemma 4.3A.141 plus the observation that boundedness
of a family of expectations is not uniqueness of its cluster point. `square`

### Corollary 4.3A.144: Determining-Identity Route To Active `BC`

The named noncircular route to `P20-SEL2-BC-BLU` is the Paper-13 determining
identity route. It is enough to prove, on the same active row batteries, that:

1. the finite-block identity ledger of Paper 13 Definition 7.30AM is
   determining on the finite algebra generated by `\mathcal B_{BC,j}^{SEL2}`;
2. the cutoff trajectory satisfies that ledger with defects tending to zero
   uniformly along the chosen cofinal row schedule.

Then Paper 13 Theorem 7.30AN gives `BLU`, and Theorem 4.3A.143 gives
`U_13^{BC,car}=0`.

With the current source imports, these determining identities have not been
proved for four-dimensional `SU(N)` on the active `SEL2` whole-process tower.
Therefore the honest current `BC` status is:

```math
0\le U_{13}^{BC,car}\le2B_{BC}^{SEL2},
```

with zero available only after `P20-SEL2-BC-BLU`, or the determining-identity
route above, is supplied. This is a genuine continuum-construction gap, not a
finite-template bookkeeping gap and not a Wilson-loop area-law assumption.

### Definition 4.3A.145: Active `CE-REG` Target On `SEL2`

Let `\nu_{p,j}^{SEL2}` be the active block-plaquette marginal on `SU(N)` read
from the same row law as `P20-SEL2-TR-COMMON`, using the block plaquette
readout fixed by the `SEL2` coefficient target. The regularity part of the
central-extraction gate, `P20-SEL2-CE-REG`, asserts that, on a cofinal row
tail, `\nu_{p,j}^{SEL2}` has a central Haar density

```math
K_{p,j}^{SEL2}\in L^1(SU(N),dHaar),
\qquad
K_{p,j}^{SEL2}\ge0,
\qquad
\int K_{p,j}^{SEL2}\,dHaar=1,
```

with character coefficients

```math
k_{\lambda,j}^{SEL2}
:=
{\langle K_{p,j}^{SEL2},\chi_\lambda\rangle
\over
\langle\chi_\lambda,\chi_\lambda\rangle}
```

and heat-regularized Peter-Weyl expansion

```math
K_{p,j}^{SEL2}*H_\tau
=
\sum_{\lambda\in\widehat{SU(N)}}
e^{-\tau C_2(\lambda)/2}k_{\lambda,j}^{SEL2}\chi_\lambda
\longrightarrow
K_{p,j}^{SEL2}
\quad\text{in }L^1
\quad(\tau\downarrow0).
```

The strengthened finite-row version, `P20-SEL2-CE-REG^+`, additionally asserts
the rowwise finite weighted character tail

```math
W_{CE,j}^{SEL2}
:=
\sum_{\lambda\ne0}
d_\lambda |k_{\lambda,j}^{SEL2}|
<\infty
```

for every cofinal row. This is not yet the uniform coefficient-tail budget
needed by `CE-TAIL`; that later budget asks for a cofinal limsup bound with
the leading `rho` channel separated.

### Lemma 4.3A.146: Smooth Central Densities Have Finite Weighted Character Tail

Let `G=SU(N)` and let `K` be a central `C^\infty` probability density on `G`.
Then

```math
K(U)=1+\sum_{\lambda\ne0}k_\lambda\chi_\lambda(U)
```

in the heat-regularized Peter-Weyl sense, and

```math
\sum_{\lambda\ne0}d_\lambda |k_\lambda|<\infty.
```

Proof.

Since `K` is central and smooth on the compact group, its character
coefficients are defined by Haar projection and its heat-regularized
Peter-Weyl expansion converges to `K` in `C^\infty`, hence in `L^1`.

For the weighted tail, choose `s>dim(G)/2`. By Cauchy-Schwarz,

```math
\sum_\lambda d_\lambda |k_\lambda|
\le
\left(\sum_\lambda d_\lambda^2(1+C_2(\lambda))^{-s}\right)^{1/2}
\left(\sum_\lambda (1+C_2(\lambda))^s |k_\lambda|^2\right)^{1/2}.
```

The first factor is finite by the compact-group Weyl law, equivalently by the
small-time heat-kernel trace asymptotic
`\sum_\lambda d_\lambda^2e^{-tC_2(\lambda)}=O(t^{-dim(G)/2})`. The second
factor is a Sobolev norm of the smooth central function `K`, hence finite.
Thus the weighted tail is finite. `square`

### Lemma 4.3A.146A: The `SEL2` Plaquette Readout Is A Submersion

For the active four-dimensional hypercubic `SEL2` block template, the block
plaquette holonomy readout

```math
P_j:G^{E_j}\to G
```

is a smooth submersion on the finite row link space.

Proof.

The block plaquette readout is a finite word in link variables and inverses
around the declared plaquette boundary, possibly with fixed block transport
segments already included in the word. Choose one boundary link variable
`U_e` that appears nontrivially in the word. Holding all other links fixed,
the readout has the form

```math
P_j(U)=A\,U_e^{\pm1}\,B
```

for fixed group elements `A` and `B` depending on the other link variables.
The differential in the `U_e` direction is left/right translation, composed
possibly with inversion, on the Lie algebra `\mathfrak{su}(N)`. This map is a
linear isomorphism onto `T_{P_j(U)}G`. Hence the full differential of `P_j`
is surjective at every point. Smoothness is immediate because multiplication
and inversion are smooth on `SU(N)`. `square`

### Theorem 4.3A.147: Finite Heat-Kernel Rows Prove Active `CE-REG^+`

Assume the active `SEL2` block-plaquette marginal is evaluated on the
Paper-16 finite heat-kernel row before taking any weak continuum subsequence,
with the same block/counterterm/projective readout and the same scalar law
used by `P20-SEL2-TR-COMMON`. Then `P20-SEL2-CE-REG^+` holds.

Proof.

Fix a cofinal row `j`. The finite row link space is a compact finite product
`G^{E_j}`, `G=SU(N)`. The Paper-16 heat-kernel row has a smooth nonnegative
density

```math
F_j(U)=Z_j^{-1}\prod_p K_{t_j}(U_p(U))
```

with respect to product Haar, after the declared finite counterterm and
projective readout conventions are folded into the same scalar row law. The
block-plaquette readout

```math
P_j:G^{E_j}\to G
```

is a smooth submersion by Lemma 4.3A.146A. Therefore the pushforward
`(P_j)_*(F_j\,dHaar^{E_j})` has a smooth density with respect to Haar on `G`;
locally this is the fiber-integration formula for densities under a
submersion, and compactness patches the local formulas globally.

Gauge invariance of the finite heat-kernel action, Haar measure, and closed
scalar readout implies conjugation invariance of the plaquette marginal. Thus
the density has a central representative `K_{p,j}^{SEL2}` with
`K_{p,j}^{SEL2}\ge0` and integral one. Lemma 4.3A.146 then gives the
heat-regularized Peter-Weyl expansion and the rowwise finite weighted
character tail. This is precisely `P20-SEL2-CE-REG^+`. `square`

### Corollary 4.3A.148: `CE-REG` Removes Only The Regularity Part Of `CE`

Assume the hypotheses of Theorem 4.3A.147. Then the active exact-entry
central-extraction residual can be split as

```math
\epsilon_{CE,j}^{SEL2}
\le
\epsilon_{CE\text{-}reg,j}^{SEL2}
+\epsilon_{CE\text{-}win,j}^{SEL2},
```

with

```math
\epsilon_{CE\text{-}reg,j}^{SEL2}=0
```

on the finite heat-kernel row branch. The remaining term
`\epsilon_{CE-win,j}^{SEL2}` contains the actual coefficient-window content:

```math
0<k_{\rho,j}^{SEL2}<1,
\qquad
\liminf_j-\log k_{\rho,j}^{SEL2}>0,
\qquad
\limsup_j\sum_{\lambda\ne0,\rho}d_\lambda|k_{\lambda,j}^{SEL2}|<\infty.
```

Thus `CE-REG^+` does not by itself prove `P20-SEL2-ENTRY-CE0`; it only makes
the Haar projections and the rowwise weighted sums legitimate.

### Honest Boundary 4.3A.149: `CE-REG` For Exact Weak Limits

Theorem 4.3A.147 is a finite-row heat-kernel theorem. If
`\nu_{p,j}^{SEL2}` is instead interpreted as an already-taken weak continuum
block-plaquette marginal, then `CE-REG` does not follow from compactness,
positivity, or centrality alone: weak limits of absolutely continuous measures
can be singular.

For an exact weak-limit interpretation, Paper 20 must add a same-record
regularity source such as uniform integrability, total-variation convergence
of the plaquette marginal, or a uniform Sobolev bound strong enough to pass
the `L^1` density and finite weighted tail to the limit. Without such a
source, `CE-REG` is a genuine analytic regularity gap. On the active
finite-row source branch, however, Theorem 4.3A.147 closes the regularity
subgate, leaving `CE-SIGN/UNIT/RATE` and `CE-TAIL` as the next coefficient
problems.

### Definition 4.3A.150: Heat-Regularized Weak-Limit `CE` Branch

Let `G=SU(N)` with normalized Haar measure `dU`. Let `H_\tau` denote the
central heat-kernel density on `G` at heat time `\tau>0`, normalized by

```math
\int_G H_\tau(U)\,dU=1.
```

For any central probability measure `\nu_{p,j}^{SEL2}` on the active block
plaquette record, finite-row or weak-limit, define the heat-regularized
plaquette density

```math
K_{p,j}^{SEL2,\tau}(U)
:=
\int_G H_\tau(V^{-1}U)\,d\nu_{p,j}^{SEL2}(V).
```

Equivalently, the regularized plaquette law is

```math
d\nu_{p,j}^{SEL2,\tau}(U)
=K_{p,j}^{SEL2,\tau}(U)\,dU
=d(\nu_{p,j}^{SEL2}*H_\tau)(U).
```

The audit `P20-SEL2-CE-REG-HSM(\tau)` asserts that
`K_{p,j}^{SEL2,\tau}` is a smooth central probability density with
Peter-Weyl coefficients

```math
k_{\lambda,j}^{SEL2,\tau}
=
\langle K_{p,j}^{SEL2,\tau},\chi_\lambda\rangle_{L^2(dU)}
```

and finite weighted character tail

```math
W_{CE,j}^{SEL2,\tau}
:=
\sum_{\lambda\ne0}d_\lambda |k_{\lambda,j}^{SEL2,\tau}|
<\infty.
```

For the selected leading channel `\rho`, all sign and order statements use
the same real-paired scalar central record convention as Paper 19 Definition
8L.11A.22G.1A: if `\rho` is not self-conjugate, `\chi_\rho` is replaced once
by the real paired central record `\Phi_\rho`. Thus `k_{\rho}` is a real
scalar sheet coefficient, not an arbitrary complex Fourier coefficient.

This is not a spacetime loop-smearing operation and it is not the same as the
Paper-12 smearing-removal tail. It is a group-character heat regularization
of the one-plaquette marginal. Therefore it may be used for regularity and
coefficient diagnostics without double-charging `T_12`, but any replacement
of the exact unsmoothed coefficient gate by this regularized gate must be
paid by the de-smearing audit below.

### Theorem 4.3A.151: Heat Regularization Proves `CE-REG` For Every Central Weak Limit

For every central probability measure `\nu_{p,j}^{SEL2}` on `SU(N)` and every
`\tau>0`, `P20-SEL2-CE-REG-HSM(\tau)` holds. More explicitly,
`K_{p,j}^{SEL2,\tau}` is smooth, nonnegative, central, has integral one, and
admits the Peter-Weyl expansion

```math
K_{p,j}^{SEL2,\tau}(U)
=
1+\sum_{\lambda\ne0}
e^{-\tau C_2(\lambda)/2}
\widehat\nu_{\lambda,j}^{SEL2}
\chi_\lambda(U),
```

where

```math
\widehat\nu_{\lambda,j}^{SEL2}
:=
\int_G\overline{\chi_\lambda(V)}\,d\nu_{p,j}^{SEL2}(V).
```

Consequently

```math
k_{\lambda,j}^{SEL2,\tau}
=
e^{-\tau C_2(\lambda)/2}
\widehat\nu_{\lambda,j}^{SEL2}.
```

Furthermore,

```math
W_{CE,j}^{SEL2,\tau}
\le
\sum_{\lambda\ne0}d_\lambda^2e^{-\tau C_2(\lambda)/2}
<\infty.
```

Proof.

Since `H_\tau` is a smooth positive central heat-kernel density on the compact
Lie group `G`, convolution against any finite measure gives the smooth
function

```math
U\mapsto\int_GH_\tau(V^{-1}U)\,d\nu(V).
```

Differentiation under the integral is justified by compactness and smoothness
of `H_\tau`. Positivity and total mass one follow from positivity and
normalization of `H_\tau`. If `\nu` is central, then for every `g\in G`,

```math
K^\tau(gUg^{-1})
=
\int_G H_\tau(V^{-1}gUg^{-1})\,d\nu(V)
=
\int_G H_\tau((g^{-1}Vg)^{-1}U)\,d\nu(V)
=K^\tau(U),
```

using centrality of `H_\tau` and conjugation invariance of `\nu`.

The distributional Peter-Weyl coefficient of `\nu` in the character
`\chi_\lambda` is `\widehat\nu_\lambda`. The heat semigroup multiplies the
`\lambda` coefficient by `e^{-\tau C_2(\lambda)/2}`, giving the displayed
coefficient formula. Finally,

```math
|\widehat\nu_{\lambda,j}^{SEL2}|
\le
\|\chi_\lambda\|_\infty
=d_\lambda,
```

so

```math
\sum_{\lambda\ne0}d_\lambda|k_{\lambda,j}^{SEL2,\tau}|
\le
\sum_{\lambda\ne0}d_\lambda^2e^{-\tau C_2(\lambda)/2}.
```

The final sum is finite because it is the nontrivial part of the heat trace
at the identity on the compact group. `square`

### Definition 4.3A.152: `CE` De-Smearing Audit

Let `\tau_j>0` be a cofinal heat-character regularization schedule. Define
the extended de-smearing discrepancy

```math
\Delta_{CE\text{-}sm,j}^{SEL2}(\tau_j)
:=
|1-e^{-\tau_j C_2(\rho)/2}|\,
|\widehat\nu_{\rho,j}^{SEL2}|
+
\sum_{\lambda\ne0,\rho}
d_\lambda
|1-e^{-\tau_j C_2(\lambda)/2}|\,
|\widehat\nu_{\lambda,j}^{SEL2}|.
```

The sum is allowed to take the value `+\infty`. The audit
`P20-SEL2-CE-DESMEAR(U_{CE\text{-}sm}^{SEL2})` asserts

```math
\limsup_j
\Delta_{CE\text{-}sm,j}^{SEL2}(\tau_j)
\le
U_{CE\text{-}sm}^{SEL2}.
```

The zero de-smearing audit is the special case
`U_{CE\text{-}sm}^{SEL2}=0`. A sufficient same-record route to zero is:

1. `\tau_j\downarrow0`;
2. a cofinal uniform weighted character-tail tightness bound

```math
\lim_{R\to\infty}
\limsup_j
\sum_{\lambda\ne0,\rho:\ C_2(\lambda)>R}
d_\lambda|\widehat\nu_{\lambda,j}^{SEL2}|
=0;
```

3. finite-window coefficient boundedness along the active row battery.

The tail-tightness clause is stronger than a uniform finite weighted norm. It
rules out drifting character mass at `C_2(\lambda)\sim\tau_j^{-1}`, where
`1-e^{-\tau_jC_2(\lambda)/2}` is order one. Under these hypotheses,
finite-window convergence of the heat multiplier plus the tight tail gives
`\Delta_{CE-sm,j}^{SEL2}(\tau_j)\to0` after the usual diagonal choice of
`\tau_j`. If tail tightness is absent, heat regularization still proves
`CE-REG-HSM(\tau)`, but the exact unsmoothed coefficient gate must carry the
finite or infinite de-smearing debit.

### Theorem 4.3A.153: Regularized `CE` Tail And Coefficient Fork

Fix `\tau>0`. On the heat-regularized branch, the non-leading character tail
has the explicit universal bound

```math
\sum_{\lambda\ne0,\rho}
d_\lambda |k_{\lambda,j}^{SEL2,\tau}|
\le
\Theta_G(\tau)-1-d_\rho^2e^{-\tau C_2(\rho)/2},
```

where

```math
\Theta_G(\tau):=
\sum_\lambda d_\lambda^2e^{-\tau C_2(\lambda)/2}
=H_\tau(e).
```

The leading coefficient satisfies

```math
k_{\rho,j}^{SEL2,\tau}
=
e^{-\tau C_2(\rho)/2}
\widehat\nu_{\rho,j}^{SEL2}.
```

Thus heat regularization automatically closes the regularity and finite-tail
parts of `CE` at fixed `\tau`, but it does not by itself prove leading
coefficient positivity: the sign of `k_{\rho,j}^{SEL2,\tau}` is exactly the
sign of the real-paired scalar coefficient `\widehat\nu_{\rho,j}^{SEL2}`. If
the active source proves
`\widehat\nu_{\rho,j}^{SEL2}>0` cofinally, then choosing

```math
\tau>
\frac{2\log d_\rho}{C_2(\rho)}
```

also gives the universal strict upper bound

```math
0<k_{\rho,j}^{SEL2,\tau}<1
```

cofinally. However, using that bound for the exact unsmoothed theorem is
legitimate only after paying `P20-SEL2-CE-DESMEAR`.

Proof.

The tail bound is Theorem 4.3A.151 with the `\rho` term removed. The leading
coefficient formula is the same heat-semigroup multiplier identity. Since the
heat multiplier is strictly positive, it preserves the sign of the unsmoothed
character coefficient. Finally,

```math
|\widehat\nu_{\rho,j}^{SEL2}|
\le d_\rho,
```

so if `\widehat\nu_{\rho,j}^{SEL2}>0` and
`e^{-\tau C_2(\rho)/2}d_\rho<1`, then
`0<k_{\rho,j}^{SEL2,\tau}<1`. `square`

### Corollary 4.3A.154: What The Creative `CE` Extension Does And Does Not Prove

The active `CE` regularity status is now:

1. finite heat-kernel rows prove unregularized rowwise `CE-REG^+` by Theorem
   4.3A.147;
2. arbitrary central weak plaquette limits prove heat-regularized
   `CE-REG-HSM(\tau)` for every `\tau>0` by Theorem 4.3A.151;
3. fixed positive `\tau` gives an explicit finite non-leading tail bound by
   Theorem 4.3A.153;
4. exact unsmoothed weak-limit `CE-REG^+` still requires either a direct
   uniform regularity source or the de-smearing audit
   `P20-SEL2-CE-DESMEAR`;
5. neither regularity route proves the real dynamical sign/rate statement
   `\widehat\nu_{\rho,j}^{SEL2}>0` with a positive cofinal rate.

Therefore the proof has genuinely advanced: the possible singularity of the
weak block-plaquette law is no longer a fatal obstruction for a regularized
coefficient attack. But Paper 20 still cannot convert this into exact
unconditional confinement unless the de-smearing debit and the leading
coefficient sign/rate are closed without importing an area law.

### Audit 4.3A.154A: Coefficient Normalization Source Audit

The active Paper-20 `CE` coefficient must follow the source convention in
Paper 13 and Paper 19. That convention is the **raw Haar-projection
coefficient**, not a dimension-normalized coefficient.

Paper 13 Definition 7.30AE writes the one-plaquette central factor as

```math
K_p(U)=1+\sum_{\lambda\ne0}k_\lambda(p)\chi_\lambda(U),
\qquad
u_{\rho,s_0}:=k_\rho(p)\in(0,1),
```

and Paper 13 Definition 7.30AP computes

```math
k_\lambda(p)
=
{\langle K_p,\chi_\lambda\rangle_{L^2(G)}
\over
\langle\chi_\lambda,\chi_\lambda\rangle_{L^2(G)}}.
```

Paper 19 Definition 8L.11A.22G and Definition 8L.11A.22G.2 then set

```math
u_{\rho,s_0,j}=k_{\rho,j}
```

for the `T_13` leading-sheet factor. No division by `d_\rho` appears in the
active source chain.

Therefore the Paper-20 active branch is source-aligned only if it keeps

```math
u_{\rho,j}^{SEL2}=a_{\rho,j}^{SEL2}=k_{\rho,j}^{SEL2}
```

as the raw scalar coefficient. Introducing

```math
\widetilde u_{\rho,j}^{SEL2}:=
{k_{\rho,j}^{SEL2}\over d_\rho}
```

would be mathematically natural for heat-kernel diagnostics, but it would be
a different surface-expansion theorem unless the Paper-13/Paper-19 surface
ledger is rebuilt.

The heat-kernel diagnostic makes the issue visible. For the central heat
kernel

```math
H_t(U)=\sum_\lambda d_\lambda e^{-tC_2(\lambda)/2}\chi_\lambda(U),
```

the raw coefficient is

```math
k_\rho^{HK}(t)=d_\rho e^{-tC_2(\rho)/2},
```

whereas the dimension-normalized coefficient is

```math
\widetilde u_\rho^{HK}(t)=e^{-tC_2(\rho)/2}.
```

Thus `CE-UNIT` for the raw coefficient can fail at small heat time even
though the normalized heat-kernel coefficient lies in `(0,1)`. This is not a
formatting issue in Paper 20; it is a genuine normalization choice in the
source surface theorem.

### Corollary 4.3A.154B: The Dimension-Normalized Fork Is A Different Route

Define the normalized coefficient

```math
\widetilde a_{\rho,j}^{SEL2}:={a_{\rho,j}^{SEL2}\over d_\rho}.
```

Then heat-kernel rows satisfy the natural unit window

```math
0<\widetilde a_{\rho,j}^{HK}<1
```

for every positive heat time. However, Paper 20 may replace the active raw
coefficient by `\widetilde a_{\rho,j}^{SEL2}` only after proving a new
normalization-compatibility audit `P20-SEL2-NORM-SURF`:

1. the Paper-13 surface representation is rewritten with
   `\widetilde a_{\rho,j}^{|\Sigma|}` as the leading sheet weight;
2. all `d_\rho` factors created by Peter-Weyl link integrations are either
   exactly canceled by the Wilson-loop normalization or assigned once to the
   finite decoration/surface constants `D_C,E_C,\xi_C,\xi'_C`;
3. the `SUB` threshold and Paper-19 `T_13` surface-tail inequality are
   rederived with the normalized sheet weight;
4. the non-leading character tail and decoration ledger are reweighted
   consistently, with no double charge against `T_11`, `T_12`, or `T_14`.

Until `P20-SEL2-NORM-SURF` is proved, the active exact Paper-20 branch remains
the raw-coefficient branch of Audit 4.3A.154A. The normalized fork is useful
as a diagnostic and may be the better route for a future revision of the
surface theorem, but it cannot be silently substituted into the present
Paper-13/Paper-19 chain. Definitions 4.3A.160M--4.3A.160P carry out this
fork explicitly: a pure algebraic rewrite gives no gain, and a genuine
normalized route requires a new same-record surface theorem with a
dimension-surcharge strictly below `log d_\rho`. Audit 4.3A.160Q and Lemma
4.3A.160R then freeze the normalized Wilson-loop convention and prove the
one-link Schur gluing factor; Corollary 4.3A.160S gives the local
one-plaquette normalized sheet weight `k_\rho/d_\rho`, Theorem 4.3A.160V
lifts it to every clean rho-monochromatic disk surface, Corollaries
4.3A.160W--4.3A.160X isolate the remaining non-clean/corner/decoration
surface-collar extension, and Definition 4.3A.160Y--Corollary 4.3A.160AE
close the dimension-surcharge part of that extension on the active reduced
`SEL2` convention.

### Definition 4.3A.155: Frozen Leading Scalar Convention For `CE-SIGN/UNIT/RATE`

For the active `SEL2` coefficient attack, freeze once and for all:

1. a nontrivial irreducible channel `\rho`;
2. the scalar central record

   ```math
   \Phi_\rho=
   \begin{cases}
   \chi_\rho, & \rho\simeq\bar\rho,\\
   \operatorname{Re}(\chi_\rho), & \rho\not\simeq\bar\rho,
   \end{cases}
   ```

   with the non-self-conjugate case understood in the Paper-19 real-paired
   convention and normalized exactly as in Paper 19 Definition
   8L.11A.22G.1A;
3. the exact unsmoothed scalar coefficient

   ```math
   a_{\rho,j}^{SEL2}
   :=
   \int_G\Phi_\rho(U)\,d\nu_{p,j}^{SEL2}(U);
   ```

4. the heat-smoothed scalar coefficient

   ```math
   a_{\rho,j}^{SEL2,\tau}
   :=
   e^{-\tau C_2(\rho)/2}a_{\rho,j}^{SEL2};
   ```

5. the sheet weight used by the `T_13` surface ledger

   ```math
   u_{\rho,j}^{SEL2}:=a_{\rho,j}^{SEL2}.
   ```

By Audit 4.3A.154A this is the raw Paper-13/Paper-19 Haar-projection
coefficient. The dimension-normalized fork
`\widetilde a_{\rho,j}^{SEL2}=a_{\rho,j}^{SEL2}/d_\rho` is not used in this
active branch unless `P20-SEL2-NORM-SURF` is separately proved.

All inequalities in `CE-SIGN`, `CE-UNIT`, and `CE-RATE` are inequalities for
this real scalar coefficient. No complex Fourier sign is used. This keeps the
attack Barandes-aligned: the object is a pushed-forward scalar record
coefficient, not a hidden gauge-fixed field or amplitude phase.

### Lemma 4.3A.156: Regularity Alone Does Not Prove The Leading Window

Central `L^1` density, smoothness, and finite weighted character tail do not
imply any of the following:

```math
a_{\rho,j}^{SEL2}>0,
\qquad
0<a_{\rho,j}^{SEL2}<1,
\qquad
\liminf_j-\log a_{\rho,j}^{SEL2}>0.
```

Proof.

For sign, choose any nonzero real scalar central record `\Phi_\rho` and take

```math
K_\epsilon(U)=1-\epsilon\Phi_\rho(U)
```

with `0<\epsilon<\|\Phi_\rho\|_\infty^{-1}`. Then `K_\epsilon` is a smooth
central probability density for sufficiently small `\epsilon` because
`\int_G\Phi_\rho\,dU=0`, while its `\Phi_\rho` coefficient is negative.

For the subunit bound, take the heat kernel based at the identity. Its
`\rho` coefficient is

```math
d_\rho e^{-\tau C_2(\rho)/2}
```

in the unpaired self-conjugate convention, with the corresponding positive
real-paired scalar coefficient in the paired convention. For sufficiently
small positive `\tau`, this coefficient is larger than one whenever the
chosen nontrivial sheet has `d_\rho>1`; for `SU(N)`, every nontrivial
irreducible has this property. Thus regularity does not impose a universal
strict subunit ceiling.

For positive rate, choose heat times

```math
\tau_j={2\log d_\rho\over C_2(\rho)}+{1\over j}
```

in the self-conjugate convention. Then the heat-kernel coefficient is
positive and strictly below one, but tends to one, so
`-\log a_{\rho,j}\to0`. Thus a positive cofinal rate is a genuine dynamical
source estimate, not a consequence of regularity. `square`

### Definition 4.3A.157: `CE-SIGN` Witnesses On The Exact `SEL2` Branch

The exact sign audit `P20-SEL2-CE-SIGN(s_\rho)` asserts

```math
\liminf_j a_{\rho,j}^{SEL2}\ge s_\rho>0.
```

A concrete finite-template sufficient witness is the identity-collar
inequality. Choose a central neighborhood `\mathcal U_\rho` of the identity
and constants `c_+(\rho),c_-(\rho)>0` such that

```math
\Phi_\rho(U)\ge c_+(\rho)
\quad (U\in\mathcal U_\rho),
\qquad
\Phi_\rho(U)\ge -c_-(\rho)
\quad (U\notin\mathcal U_\rho).
```

Then the collar witness `P20-SEL2-CE-SIGN-COL(m_\rho)` asserts

```math
\liminf_j\nu_{p,j}^{SEL2}(\mathcal U_\rho)\ge m_\rho
```

with

```math
m_\rho>
{c_-(\rho)\over c_+(\rho)+c_-(\rho)}.
```

The resulting sign margin is

```math
s_\rho
=
(c_+(\rho)+c_-(\rho))m_\rho-c_-(\rho)>0.
```

This is not an area-law input. It is a local one-plaquette central-sheet bias
statement on the frozen scalar record law.

### Theorem 4.3A.158: The Sign Audit Is Exactly The First Live Coefficient Gate

If `P20-SEL2-CE-SIGN(s_\rho)` holds, then the exact leading coefficient is
positive cofinally. If the collar witness `P20-SEL2-CE-SIGN-COL(m_\rho)`
holds with the displayed strict inequality, then
`P20-SEL2-CE-SIGN(s_\rho)` holds with the displayed `s_\rho`.

Conversely, without some positive scalar-sheet witness of this kind, the
current regularity results cannot prove sign, by Lemma 4.3A.156.

Proof.

The first assertion is the definition of the sign audit. For the collar
witness,

```math
a_{\rho,j}^{SEL2}
=
\int_{\mathcal U_\rho}\Phi_\rho\,d\nu_{p,j}^{SEL2}
+
\int_{G\setminus\mathcal U_\rho}\Phi_\rho\,d\nu_{p,j}^{SEL2}
\ge
c_+(\rho)\nu_{p,j}^{SEL2}(\mathcal U_\rho)
-c_-(\rho)(1-\nu_{p,j}^{SEL2}(\mathcal U_\rho)).
```

Taking `liminf` gives `s_\rho`. The counterexample in Lemma 4.3A.156 proves
that regularity alone is insufficient. `square`

### Definition 4.3A.159: `CE-UNIT` Sheet Ceiling On `SEL2`

The exact subunit audit `P20-SEL2-CE-UNIT(b_\rho)` asserts

```math
\limsup_j a_{\rho,j}^{SEL2}\le b_\rho<1.
```

Together with `P20-SEL2-CE-SIGN(s_\rho)`, this gives the cofinal exact
window

```math
0<a_{\rho,j}^{SEL2}<1.
```

A finite-template sufficient route is a non-identity escape witness: find a
central set `\mathcal V_\rho` and constants `M_\rho>m_\rho^{out}` such that

```math
\Phi_\rho(U)\le M_\rho\quad(U\in G),
\qquad
\Phi_\rho(U)\le m_\rho^{out}\quad(U\in\mathcal V_\rho),
```

and

```math
\liminf_j\nu_{p,j}^{SEL2}(\mathcal V_\rho)\ge q_\rho>0,
\qquad
M_\rho-q_\rho(M_\rho-m_\rho^{out})<1.
```

Then `b_\rho:=M_\rho-q_\rho(M_\rho-m_\rho^{out})` is an admissible subunit
ceiling. This is again a one-plaquette scalar-record spread estimate, not a
Wilson-loop area-law estimate.

### Theorem 4.3A.160: Exact `CE-SIGN/UNIT` Window Decision

If `P20-SEL2-CE-SIGN(s_\rho)` and `P20-SEL2-CE-UNIT(b_\rho)` hold, then

```math
0<a_{\rho,j}^{SEL2}<1
```

cofinally. If the escape witness in Definition 4.3A.159 holds, then
`P20-SEL2-CE-UNIT(b_\rho)` holds.

Proof.

The first claim follows from the definitions and the strict inequalities
`s_\rho>0`, `b_\rho<1`. For the escape witness,

```math
a_{\rho,j}^{SEL2}
\le
m_\rho^{out}\nu_{p,j}^{SEL2}(\mathcal V_\rho)
+M_\rho(1-\nu_{p,j}^{SEL2}(\mathcal V_\rho))
=
M_\rho-\nu_{p,j}^{SEL2}(\mathcal V_\rho)(M_\rho-m_\rho^{out}).
```

Taking `limsup` gives the displayed `b_\rho`. `square`

### Definition 4.3A.160A: Raw Heat-Time Unit Threshold

For the raw Paper-13/Paper-19 coefficient convention of Audit 4.3A.154A,
define the representation threshold

```math
\theta_\rho
:=
{2\log d_\rho\over C_2(\rho)}.
```

On a heat-kernel reference marginal

```math
H_t(U)=\sum_\lambda d_\lambda e^{-tC_2(\lambda)/2}\chi_\lambda(U),
```

the raw leading coefficient is

```math
k_\rho^{HK}(t)=d_\rho e^{-tC_2(\rho)/2}.
```

Therefore the exact raw heat-kernel unit condition is

```math
0<k_\rho^{HK}(t)<1
\quad\Longleftrightarrow\quad
t>\theta_\rho.
```

For the active `SEL2` branch, define the raw heat-time comparison audit
`P20-SEL2-RAW-HKTIME(t_{eff,j},\varepsilon_{\rho,j})` by

```math
\left|
a_{\rho,j}^{SEL2}
-d_\rho e^{-t_{eff,j}C_2(\rho)/2}
\right|
\le
\varepsilon_{\rho,j}.
```

Here `t_{eff,j}` is the effective one-block central-character heat time of
the pushed-forward plaquette marginal. It is not automatically the
microscopic AF heat-kernel time. If the block scale is held at a fixed
physical size while the cutoff is refined, `t_{eff,j}` must be proved from
the block pushforward, not read off from the bare plaquette action.

### Theorem 4.3A.160B: Honest Raw `CE-UNIT` Pass Criterion

Assume `P20-SEL2-RAW-HKTIME(t_{eff,j},\varepsilon_{\rho,j})`. If there is
`\Delta_\rho>0` such that

```math
\liminf_j t_{eff,j}\ge\theta_\rho+\Delta_\rho,
```

and

```math
\limsup_j\varepsilon_{\rho,j}
<
1-e^{-\Delta_\rho C_2(\rho)/2},
```

then `P20-SEL2-CE-UNIT(b_\rho)` holds with any strict

```math
b_\rho>
e^{-\Delta_\rho C_2(\rho)/2}
+\limsup_j\varepsilon_{\rho,j},
\qquad
b_\rho<1.
```

If, in addition,

```math
\limsup_j t_{eff,j}<\infty,
\qquad
\limsup_j\varepsilon_{\rho,j}
<
d_\rho e^{-(\limsup_j t_{eff,j})C_2(\rho)/2},
```

then the same heat-time comparison also gives cofinal positivity of the raw
coefficient.

Proof.

For all sufficiently large `j`,

```math
d_\rho e^{-t_{eff,j}C_2(\rho)/2}
\le
d_\rho e^{-(\theta_\rho+\Delta_\rho)C_2(\rho)/2}
=
e^{-\Delta_\rho C_2(\rho)/2}.
```

The comparison error then gives

```math
\limsup_j a_{\rho,j}^{SEL2}
\le
e^{-\Delta_\rho C_2(\rho)/2}
+\limsup_j\varepsilon_{\rho,j}
<1.
```

This is `CE-UNIT`. The positivity addendum follows from the lower comparison

```math
a_{\rho,j}^{SEL2}
\ge
d_\rho e^{-t_{eff,j}C_2(\rho)/2}-\varepsilon_{\rho,j},
```

together with the displayed strict lower margin. `square`

### Theorem 4.3A.160C: Honest Raw `CE-UNIT` Failure Criterion

Assume `P20-SEL2-RAW-HKTIME(t_{eff,j},\varepsilon_{\rho,j})`. If there is
`\Delta_\rho>0` such that

```math
\limsup_j t_{eff,j}\le\theta_\rho-\Delta_\rho,
```

and

```math
\limsup_j\varepsilon_{\rho,j}
<
e^{\Delta_\rho C_2(\rho)/2}-1,
```

then the raw coefficient is eventually larger than one, hence the active raw
`CE-UNIT` route fails:

```math
a_{\rho,j}^{SEL2}>1
```

cofinally.

In particular, if the active comparison identifies `t_{eff,j}` with a
microscopic AF heat time satisfying `t_{eff,j}\to0`, and if
`\varepsilon_{\rho,j}\to0`, then raw `CE-UNIT` fails for every nontrivial
irreducible `\rho` of `SU(N)`.

Proof.

For all sufficiently large `j`,

```math
d_\rho e^{-t_{eff,j}C_2(\rho)/2}
\ge
d_\rho e^{-(\theta_\rho-\Delta_\rho)C_2(\rho)/2}
=
e^{\Delta_\rho C_2(\rho)/2}.
```

The lower comparison gives

```math
\liminf_j a_{\rho,j}^{SEL2}
\ge
e^{\Delta_\rho C_2(\rho)/2}
-\limsup_j\varepsilon_{\rho,j}
>1.
```

Thus `0<a_{\rho,j}^{SEL2}<1` cannot hold cofinally. If `t_{eff,j}\to0`,
choose any `0<\Delta_\rho<\theta_\rho`; since `SU(N)` has
`d_\rho>1` for every nontrivial irreducible, `\theta_\rho>0`, and the same
argument applies. `square`

### Corollary 4.3A.160D: Current Status Of Raw `CE-UNIT` On `SEL2`

The raw `CE-UNIT` problem is now an explicit scalar heat-time decision.

1. If the active `SEL2` block pushforward has an effective coefficient time
   staying uniformly above `\theta_\rho`, with comparison error below the
   margin in Theorem 4.3A.160B, then raw `CE-UNIT` closes.
2. If the active branch is controlled only by the microscopic AF
   heat-kernel time `t_i\to0`, with no nonperturbative block-time
   renormalization lifting the effective time above `\theta_\rho`, then raw
   `CE-UNIT` fails by Theorem 4.3A.160C.
3. The critical regime `t_{eff,j}\to\theta_\rho`, or a regime where the
   comparison error is comparable to the unit margin, is undecided by this
   scalar test and must be handled by sharper coefficient estimates.

Thus the next source task is not merely to bound a coefficient. It is to
prove a genuine block-time statement:

```math
\liminf_j t_{eff,j}>\theta_\rho
```

on the same frozen `SEL2` scalar record law, or to prove that the active raw
route is dead and move deliberately to the normalized surface fork
`P20-SEL2-NORM-SURF`.

### Definition 4.3A.160E: Intrinsic Effective Block Time

On the raw positive branch `a_{\rho,j}^{SEL2}>0`, define the intrinsic
effective block character time by

```math
t_{\rho,j}^{blk}
:=
{2\over C_2(\rho)}
\log\left({d_\rho\over a_{\rho,j}^{SEL2}}\right).
```

Then

```math
a_{\rho,j}^{SEL2}
=d_\rho e^{-t_{\rho,j}^{blk}C_2(\rho)/2}.
```

Therefore the raw unit and rate tests are exactly

```math
a_{\rho,j}^{SEL2}<1
\quad\Longleftrightarrow\quad
t_{\rho,j}^{blk}>\theta_\rho,
```

and

```math
\liminf_j-\log a_{\rho,j}^{SEL2}>0
\quad\Longleftrightarrow\quad
\liminf_j(t_{\rho,j}^{blk}-\theta_\rho)>0.
```

This definition is diagnostic, not a proof of heat-kernel form. It simply
rewrites the scalar coefficient as a heat-time coordinate for the selected
representation. A source theorem must still prove a lower bound for
`t_{\rho,j}^{blk}` from the block pushforward.

### Definition 4.3A.160F: Block-Time Lift And Collapse Audits

The block-time lift audit `P20-SEL2-BTIME-LIFT(\Delta_\rho)` asserts

```math
\liminf_j t_{\rho,j}^{blk}
\ge
\theta_\rho+\Delta_\rho,
\qquad
\Delta_\rho>0.
```

The microscopic-collapse audit `P20-SEL2-BTIME-COLLAPSE` asserts that, for
some finite `C_{mic}` and some `r_j\to0`,

```math
t_{\rho,j}^{blk}
\le
C_{mic}t_i+r_j,
```

where `t_i` is the microscopic AF heat-kernel time of the underlying
Paper-16 row.

The additive block-time audit `P20-SEL2-BTIME-ADD(A_j,r_j)` asserts

```math
t_{\rho,j}^{blk}
\ge
A_jt_i-r_j,
\qquad
r_j\to0.
```

Here `A_j` is an effective block-area/time-amplification factor for the
selected block plaquette record. This audit is deliberately not assumed from
microscopic heat-kernel locality; it is a same-record estimate for the
pushed-forward block plaquette marginal.

### Theorem 4.3A.160G: Block-Time Lift Closes Raw `CE-UNIT/RATE`

If `P20-SEL2-BTIME-LIFT(\Delta_\rho)` holds, then the active raw coefficient
window and positive rate hold:

```math
0<a_{\rho,j}^{SEL2}<1
```

cofinally, and

```math
\liminf_j-\log a_{\rho,j}^{SEL2}
\ge
{C_2(\rho)\Delta_\rho\over2}
>0.
```

If `P20-SEL2-BTIME-ADD(A_j,r_j)` holds and

```math
\liminf_j(A_jt_i-r_j)
>
\theta_\rho,
```

then `P20-SEL2-BTIME-LIFT(\Delta_\rho)` holds for every strict

```math
0<\Delta_\rho
<
\liminf_j(A_jt_i-r_j)-\theta_\rho.
```

Proof.

The first part is Definition 4.3A.160E. Indeed,

```math
-\log a_{\rho,j}^{SEL2}
=
{C_2(\rho)\over2}
(t_{\rho,j}^{blk}-\theta_\rho).
```

The additive audit gives a lower bound for `t_{\rho,j}^{blk}`. If the lower
bound is strictly above `\theta_\rho`, any smaller strict gap is an admissible
`\Delta_\rho`. `square`

### Theorem 4.3A.160H: Microscopic Collapse Kills The Raw Route

Assume the microscopic AF heat-kernel time satisfies `t_i\to0`. If
`P20-SEL2-BTIME-COLLAPSE` holds, then

```math
t_{\rho,j}^{blk}\to0.
```

Since `\theta_\rho>0` for every nontrivial irreducible representation of
`SU(N)`, raw `CE-UNIT` fails cofinally:

```math
a_{\rho,j}^{SEL2}>1
```

for all sufficiently large `j`.

Proof.

The collapse audit and `t_i\to0` give `t_{\rho,j}^{blk}\to0`. For large `j`,
`t_{\rho,j}^{blk}<\theta_\rho`, and Definition 4.3A.160E gives
`a_{\rho,j}^{SEL2}>1`. `square`

### Corollary 4.3A.160I: Does `SEL2` Create A Block Time Above Threshold?

With the current source imports, Paper 20 has **not** proved either side of
the fork.

1. Paper 16 proves that the microscopic heat-kernel time satisfies
   `t_i\to0` along the AF tail for the local analytic estimates.
2. Paper 13 explicitly treats `u_{\rho,s_0}` as a renormalized block-scale
   coefficient produced by exact whole-process blocking at physical scale
   `s_0`; it is not declared to be the microscopic heat-kernel coefficient.
3. Therefore `t_i\to0` alone does not prove collapse of
   `t_{\rho,j}^{blk}`.
4. Conversely, the present Paper-16/Paper-19 imports do not prove the
   additive or renormalized block-time lift

   ```math
   \liminf_j t_{\rho,j}^{blk}>\theta_\rho.
   ```

Thus the honest status is:

```text
SEL2 raw CE-UNIT/RATE is undecided.
It passes if P20-SEL2-BTIME-LIFT is proved.
It fails if P20-SEL2-BTIME-COLLAPSE is proved.
Current imports prove neither.
```

The next noncircular mathematical task is to prove a same-record block-time
lift from the finite block pushforward, for example through a strong-block
character-domain estimate, a determining finite-block identity ledger, or a
constructive RG coefficient-flow theorem. If that lift cannot be supplied,
the raw branch should be parked and the normalized surface fork
`P20-SEL2-NORM-SURF` should be developed explicitly.

### Lemma 4.3A.160J: Finite Pushforward Alone Does Not Decide Block Time

The finite pushed-forward `SEL2` block-record hypotheses used so far do not
imply either `P20-SEL2-BTIME-LIFT` or `P20-SEL2-BTIME-COLLAPSE`.

More precisely, if the only retained data are:

1. a finite block/collar template with a scalar plaquette readout
   `U_p\in SU(N)`;
2. centrality of the pushed-forward plaquette law;
3. rowwise `L^1` Peter-Weyl regularity, or heat-smoothed regularity as in
   `CE-REG-HSM`;
4. the same-record bookkeeping convention, with no area-law or confinement
   input;

then there are comparison rows satisfying these data and realizing both
block-time behaviors.

Proof.

Fix a nontrivial irreducible representation `rho` and write

```math
\theta_\rho={2\log d_\rho\over C_2(\rho)}.
```

First choose a constant `\Delta_\rho>0` and let the scalar plaquette marginal
be the central heat-kernel density `H_{\theta_\rho+2\Delta_\rho}` on `SU(N)`.
Its raw Haar coefficient is

```math
a_\rho
=d_\rho e^{-(\theta_\rho+2\Delta_\rho)C_2(\rho)/2}
=e^{-\Delta_\rho C_2(\rho)}.
```

Therefore the intrinsic block time of Definition 4.3A.160E is exactly

```math
t_\rho^{blk}=\theta_\rho+2\Delta_\rho,
```

so the lift audit holds, with room.

Second let `t_i\downarrow0` and choose the scalar plaquette marginal
`H_{t_i}`. Then

```math
a_{\rho,i}
=d_\rho e^{-t_iC_2(\rho)/2},
\qquad
t_{\rho,i}^{blk}=t_i\to0.
```

This is the microscopic-collapse behavior, and for all sufficiently large
`i` the raw coefficient is larger than one because `t_i<\theta_\rho`.

Both rows are central probability densities, smooth for each positive time,
and have rowwise finite Peter-Weyl tails. They can be realized on the same
finite block template by taking one block plaquette variable with the stated
law and adjoining dummy Haar-distributed collar variables, then pushing
forward to the scalar plaquette readout. This construction is not asserted to
be the actual Yang-Mills row. It proves only the logical point needed here:
the finite pushforward, centrality, regularity, and same-record bookkeeping
axioms do not decide the effective block time. `square`

### Definition 4.3A.160K: Active Raw-Branch Parking Convention

The active raw branch is said to be parked, written
`P20-SEL2-RAWBTIME-PARK`, when the source ledger contains neither
`P20-SEL2-BTIME-LIFT(\Delta_\rho)` for some `\Delta_\rho>0` nor
`P20-SEL2-BTIME-COLLAPSE`.

On this parked branch:

1. Paper 20 may not spend raw `CE-UNIT/RATE` in the surface-polymer closure
   theorem.
2. The undecided block-time fork is an obstruction gate, not a finite
   transport debit. It is therefore not added to `U_pre13`, `U_EZ`, or
   `U_13^{entry}`.
3. If a later source theorem proves `P20-SEL2-BTIME-LIFT`, the raw branch
   reopens and Theorem 4.3A.160G supplies the rate.
4. If a later source theorem proves `P20-SEL2-BTIME-COLLAPSE` while the
   microscopic AF time satisfies `t_i\to0`, the raw branch closes negatively
   by Theorem 4.3A.160H, and any continuation must use a rebuilt branch such
   as `P20-SEL2-NORM-SURF`.

### Theorem 4.3A.160L: Exhausted Decision For Current Sources

With the current Paper-13, Paper-16, Paper-19, and Paper-20 imports, the
honest decision is

```text
P20-SEL2-RAWBTIME-PARK.
```

In particular, Paper 20 has not proved `P20-SEL2-BTIME-LIFT`; it has also not
proved `P20-SEL2-BTIME-COLLAPSE`.

Proof.

Corollary 4.3A.160I identifies the two available source facts. Paper 16 gives
microscopic AF heat-kernel times tending to zero for local analytic rows.
Paper 13 treats `u_{\rho,s_0}` as a renormalized block-scale coefficient
produced by exact whole-process blocking at physical scale `s_0`, not as the
bare microscopic heat-kernel coefficient. Hence the current imports do not
prove collapse.

The same imports also do not supply a determining block coefficient-flow
estimate, strong-character-domain estimate, or same-record identity ledger
forcing

```math
\liminf_j t_{\rho,j}^{blk}>\theta_\rho.
```

Hence they do not prove lift.

Lemma 4.3A.160J shows that this is not a presentational gap: finite
pushforward plus centrality, rowwise regularity, and same-record bookkeeping
is logically compatible with both a lifted block time and microscopic
collapse. Therefore no proof of either branch can be extracted from the
current hypotheses alone. By Definition 4.3A.160K, the active raw branch is
parked. `square`

### Definition 4.3A.160M: Normalized-Surface Fork

On the same `SEL2` scalar plaquette record, define the dimension-normalized
coefficient

```math
\widetilde a_{\rho,j}^{SEL2}
:=
{a_{\rho,j}^{SEL2}\over d_\rho}.
```

The normalized-surface fork `P20-SEL2-NORM-SURF` is not the statement that
`\widetilde a_{\rho,j}^{SEL2}` exists. It is the stronger statement that the
Paper-13 surface-polymer expansion can be rederived in the form

```math
\mu_j(W_\rho(C))
=
\sum_{\Sigma:\partial\Sigma=C}
\left(\widetilde a_{\rho,j}^{SEL2}\right)^{|\Sigma|}
\widetilde Z_j(\Sigma),
```

on the same pushed-forward scalar record law, with the same minimal sheets
and with a normalized excess bound

```math
|\widetilde Z_j(\Sigma)|
\le
e^{\widetilde\xi'_{C,j}}
\left(\widetilde D_{C,j}\right)^q,
\qquad
q=|\Sigma|-N(C).
```

Let `\widetilde E_{C,j}^{surf}` be the corresponding normalized surface
entropy factor and set

```math
\widetilde B_{C,j}:=
\widetilde D_{C,j}\widetilde E_{C,j}^{surf},
\qquad
\Delta_{dim,C,j}:=
\log\widetilde B_{C,j}-\log B_{C,j},
```

where `B_{C,j}=D_{C,j}E_{C,j}^{surf}` is the raw Paper-13/Paper-19 surface
factor. The cofinal dimension-surcharge envelope is

```math
\Delta_{dim}^{SEL2}
:=
\limsup_j\max_{C\in B_{CR,j}}\Delta_{dim,C,j}.
```

Thus `P20-SEL2-NORM-SURF(\Delta_{dim}^{SEL2})` is a new surface theorem, not
a change of notation. It must prove the normalized expansion and the
displayed finite surcharge on the same record law and same disjoint debit
register.

### Lemma 4.3A.160N: Pure Algebra Gives No Normalized Gain

Assume only the raw Paper-13 surface expansion

```math
\mu_j(W_\rho(C))
=
\sum_{\Sigma:\partial\Sigma=C}
\left(a_{\rho,j}^{SEL2}\right)^{|\Sigma|}Z_j(\Sigma).
```

If one rewrites this expansion by the identity
`a_{\rho,j}^{SEL2}=d_\rho\widetilde a_{\rho,j}^{SEL2}` and makes no new
surface cancellation estimate, then the nonminimal surface ratio is
unchanged:

```math
B_{C,j}a_{\rho,j}^{SEL2}
=
\left(d_\rho B_{C,j}\right)\widetilde a_{\rho,j}^{SEL2}.
```

Equivalently, the algebraic normalized fork has

```math
\Delta_{dim}^{SEL2}=\log d_\rho
```

and gives exactly the same subcriticality margin as the raw fork.

Proof.

For a surface `\Sigma` with `|\Sigma|=N(C)+q`,

```math
\left(a_{\rho,j}^{SEL2}\right)^{|\Sigma|}Z_j(\Sigma)
=
\left(\widetilde a_{\rho,j}^{SEL2}\right)^{N(C)}
\left(d_\rho\widetilde a_{\rho,j}^{SEL2}\right)^q
d_\rho^{N(C)}Z_j(\Sigma).
```

The common minimal factor `d_\rho^{N(C)}` belongs to the minimal-sheet
normalization and does not improve the excess-`q` tail. Every excess plaquette
still carries one factor `d_\rho`. Thus the automatic normalized excess
factor is `\widetilde B_{C,j}=d_\rho B_{C,j}`. Hence

```math
\log\widetilde B_{C,j}-\log B_{C,j}=\log d_\rho,
```

and

```math
\widetilde B_{C,j}\widetilde a_{\rho,j}^{SEL2}
=
d_\rho B_{C,j}{a_{\rho,j}^{SEL2}\over d_\rho}
=
B_{C,j}a_{\rho,j}^{SEL2}.
```

So the algebraic rewrite neither improves nor worsens the actual
surface-tail ratio. `square`

### Theorem 4.3A.160O: Normalized Surface Threshold

Assume `P20-SEL2-NORM-SURF(\Delta_{dim}^{SEL2})` and define the normalized
rate

```math
\widetilde\kappa_{13}^{CE}
:=
\liminf_j-\log\widetilde a_{\rho,j}^{SEL2}.
```

Let

```math
G_{13}^{raw}
:=
\limsup_j\max_{C\in B_{CR,j}}\log B_{C,j},
\qquad
G_{13}^{norm}
:=
G_{13}^{raw}+\Delta_{dim}^{SEL2}.
```

Then the normalized surface-polymer subcriticality test is

```math
\widetilde\kappa_{13}^{CE}>G_{13}^{norm}.
```

Here `G_{13}^{raw}` is the combined raw nonminimal-sheet growth
`log(D_C E_C^{surf})`; in the split Paper-20 ledger it is bounded by the
surface-entropy term plus the nonminimal decoration term. With the Paper-20
nonsurface reserve included, the normalized analogue of the final
surface-rate condition is

```math
\widetilde\kappa_{13}^{CE}
>
G_{13}^{norm}
+
\log\left(
1+
{M_{13}^{surf,SEL2}\over
\underline M_{pre13}^{SEL2,20}}
\right).
```

The normalized fork is genuinely better than the raw fork only to the extent
that

```math
\Delta_{dim}^{SEL2}<\log d_\rho.
```

If the only available normalized expansion is the algebraic rewrite of Lemma
4.3A.160N, then this theorem reduces exactly to the raw threshold and gives
no new route around `P20-SEL2-RAWBTIME-PARK`.

Proof.

The normalized expansion has the same form as Paper 13 Definition 7.30L,
with `\widetilde a_{\rho,j}^{SEL2}` in place of the raw sheet coefficient
and `\widetilde B_{C,j}` in place of `B_{C,j}`. Therefore the nonminimal
surface series is dominated by a geometric tail with ratio

```math
\widetilde B_{C,j}\widetilde a_{\rho,j}^{SEL2}.
```

It is subcritical cofinally exactly when

```math
\limsup_j
\max_C
\left(
\log\widetilde B_{C,j}
+
\log\widetilde a_{\rho,j}^{SEL2}
\right)<0,
```

which is the first displayed threshold. Adding the already-separated
nonsurface reserve term gives the second displayed inequality by the same
algebra as Theorem 4.3A.39, with `G_{13}^{norm}` replacing the split
surface-plus-decoration growth.

Finally,

```math
\widetilde\kappa_{13}^{CE}
=
\liminf_j-\log a_{\rho,j}^{SEL2}+\log d_\rho
=
\kappa_{13}^{CE,raw}+\log d_\rho,
```

while

```math
G_{13}^{norm}=G_{13}^{raw}+\Delta_{dim}^{SEL2}.
```

Thus the normalized threshold improves the raw margin by
`\log d_\rho-\Delta_{dim}^{SEL2}`. Lemma 4.3A.160N is the special case
`\Delta_{dim}^{SEL2}=\log d_\rho`, where the improvement is zero. `square`

### Corollary 4.3A.160P: The Next Required Source Estimate

After the normalized-surface audit, the decision tree is sharp.

1. If `P20-SEL2-NORM-SURF(\Delta_{dim}^{SEL2})` is proved with
   `\Delta_{dim}^{SEL2}<\log d_\rho`, then the normalized route is a real new
   branch. It still needs a positive normalized rate strong enough to satisfy
   Theorem 4.3A.160O; microscopic AF time tending to zero is not enough if it
   makes `\widetilde\kappa_{13}^{CE}\to0`.
2. If the only normalized relation is the algebraic rewrite of Lemma
   4.3A.160N, the normalized route gives no advantage and the active raw
   branch remains parked.
3. The only noncircular way to reopen the raw branch is a new same-record
   source theorem proving `P20-SEL2-BTIME-LIFT`. Such a theorem must be one of
   the following, or something mathematically equivalent:

   ```text
   P20-SEL2-STRONG-BLOCK-CE:
     a strong-block character-domain estimate with
     liminf_j t_{rho,j}^{blk} > theta_rho;

   P20-SEL2-COEFF-FLOW:
     a constructive RG coefficient-flow theorem proving a cofinal
     block coefficient below exp(-kappa) with kappa>0;

   P20-SEL2-DETERM-ID-CE:
     a determining finite block identity ledger that fixes the plaquette
     coefficient in a subcritical central-character domain.
   ```

These are new mathematical inputs. They cannot be derived from finite
pushforward, centrality, regularity, or same-record bookkeeping alone by
Lemma 4.3A.160J.

### Audit 4.3A.160Q: Exact Normalization Freeze For Gluing

For the dimension-cancellation audit, freeze the following conventions.

1. Haar measure on `SU(N)` is normalized to total mass one.
2. For an irreducible unitary representation `rho`, write

   ```math
   \chi_\rho(U)=\operatorname{Tr}\rho(U),
   \qquad
   d_\rho=\chi_\rho(1).
   ```

   In the non-self-conjugate case the real paired scalar record is used, as
   in Paper 13 and Paper 19; the following formulas are written for the
   self-conjugate notation and then applied componentwise to the paired
   record.
3. The normalized Wilson/character loop record is

   ```math
   w_\rho(C):={1\over d_\rho}\chi_\rho(U_C).
   ```

   This is the bounded scalar loop record compatible with Paper 13's
   normalized Wilson-loop convention.
4. The central one-plaquette marginal is expanded in raw Peter-Weyl
   coefficients:

   ```math
   K_p(U)=1+\sum_{\lambda\ne0}k_\lambda(p)\chi_\lambda(U),
   \qquad
   k_\lambda(p)
   =
   {\langle K_p,\chi_\lambda\rangle\over
   \langle\chi_\lambda,\chi_\lambda\rangle}.
   ```

   Thus the normalized coefficient attached to a normalized loop record is

   ```math
   \widetilde k_\rho(p):={k_\rho(p)\over d_\rho}.
   ```

5. Paper 19's active `P19-T13-LEAD` route sets
   `u_{\rho,s_0,j}=k_{\rho,j}`. That is the raw branch audited in
   4.3A.154A--4.3A.160L. The normalized-surface fork does not alter that
   source convention; it asks for a rederived surface theorem for the
   normalized loop record `w_\rho(C)`.

This freezes the object to be proved. Dimension cancellation is not the
formal replacement `k_\rho -> k_\rho/d_\rho` inside an already-declared raw
surface expansion. It is the Schur-orthogonality statement that the exact
normalized Wilson-loop gluing computation produces `k_\rho/d_\rho` per
plaquette before the non-leading/decorated surface estimates are added.

### Lemma 4.3A.160R: One-Link Schur Gluing Identity

Let `A` and `B` be fixed path holonomies in the representation `rho`, and
let `U` be the link variable along a shared oriented edge. Then

```math
\int_{SU(N)}
\chi_\rho(AU)\chi_\rho(U^{-1}B)\,dU
=
{1\over d_\rho}\chi_\rho(AB).
```

With the conjugate-orientation convention, the inverse-edge factor is the
corresponding matrix coefficient of `rho(U^{-1})`; for a non-self-conjugate
real paired record the identity is applied componentwise to the `rho` and
`\bar\rho` channels. Thus gluing one plaquette to an existing sheet along one
shared edge contributes exactly one Schur factor `d_\rho^{-1}`.

Proof.

Write matrix entries in the representation `rho`. Since `rho` is unitary,
the normalized Schur orthogonality relation is

```math
\int_G
\rho(U)_{ab}\rho(U^{-1})_{cd}\,dU
=
{1\over d_\rho}\delta_{ad}\delta_{bc}.
```

Now expand the characters:

```math
\chi_\rho(AU)=A_{ia}\rho(U)_{ai},
\qquad
\chi_\rho(U^{-1}B)=\rho(U^{-1})_{bc}B_{cb},
```

with repeated indices summed. Therefore

```math
\int
A_{ia}\rho(U)_{ai}\rho(U^{-1})_{bc}B_{cb}\,dU
=
{1\over d_\rho}
A_{ia}\delta_{ac}\delta_{ib}B_{cb}
=
{1\over d_\rho}A_{ib}B_{bi}
=
{1\over d_\rho}\chi_\rho(AB).
```

The conjugate-orientation formula is the same identity written with
`\rho(U^{-1})=\rho(U)^*`. `square`

### Corollary 4.3A.160S: One-Plaquette Normalized Gluing Weight

Consider a single plaquette factor on the `rho` channel

```math
k_\rho\chi_\rho(U_p^{-1})
```

and the normalized Wilson plaquette record

```math
w_\rho(\partial p)={1\over d_\rho}\chi_\rho(U_p).
```

Then the one-plaquette sheet contribution is exactly

```math
\int w_\rho(\partial p)\,k_\rho\chi_\rho(U_p^{-1})\,dU
=
{k_\rho\over d_\rho}
=
\widetilde k_\rho.
```

Moreover, adding one further plaquette to a normalized open sheet along one
shared edge multiplies the sheet amplitude by `k_\rho/d_\rho` before
non-leading channels and decoration polymers are inserted.

Proof.

For the single plaquette, the product-link Haar integral is equivalent, by a
change of variables to the plaquette holonomy, to

```math
{k_\rho\over d_\rho}
\int_G\chi_\rho(U)\chi_\rho(U^{-1})\,dU
=
{k_\rho\over d_\rho},
```

because irreducible characters are orthonormal in `L^2(SU(N))`.

For the gluing step, isolate the shared edge. The new plaquette contributes
the raw factor `k_\rho\chi_\rho(U^{-1}B)`, while the current open sheet
contains the adjacent character factor `\chi_\rho(AU)` along that edge.
Lemma 4.3A.160R integrates the shared edge and replaces the two factors by
`d_\rho^{-1}\chi_\rho(AB)`. Hence the local multiplier contributed by the
new plaquette is `k_\rho/d_\rho`. `square`

### Corollary 4.3A.160T: What The Gluing Identity Proves And Does Not Prove

The one-plaquette gluing identity proves the local spin-network core of
dimension cancellation:

```math
\text{normalized one-plaquette sheet weight}
=
\widetilde k_\rho={k_\rho\over d_\rho}.
```

It also proves that the naive algebraic no-gain result of Lemma 4.3A.160N is
not the final word: Lemma 4.3A.160N rewrites an already-assumed raw expansion
with `k_\rho^{|\Sigma|}`. Corollary 4.3A.160S instead derives the sheet
factor from the normalized Wilson-loop gluing calculation itself.

However, Corollary 4.3A.160S is not yet the full
`P20-SEL2-NORM-SURF(0)` theorem. To close that theorem one still has to lift
the one-plaquette identity to the entire moving `SEL2` surface/collar
template and prove that the following effects do not reintroduce a per-excess
dimension surcharge:

1. non-leading representation insertions in the same character-tail ledger;
2. tensor recoupling at corners, backtracking reductions, and possible
   self-touching local replacements;
3. decoration polymer activities and their KP regrouping;
4. the real paired convention for non-self-conjugate `rho`;
5. the exact block/collar pushforward and scalar readout used by the moving
   `SEL2` row battery.

Thus the next normalized-surface task is no longer vague. It is the global
extension

```text
P20-SEL2-NORM-SURF-EXT:
  the local Schur factor k_rho/d_rho survives the full surface/collar
  expansion with Delta_dim^{SEL2}=0, or with a proved strict bound
  Delta_dim^{SEL2}<log d_rho.
```

### Lemma 4.3A.160U: Clean Disk Plaquette Coordinates

Let `\Sigma` be a finite oriented block-plaquette surface with one boundary
loop `C`, no self-touching, no branch lines, and disk topology. Let
`A=|\Sigma|`. On the finite sheet/collar link set, fix an axial tree in the
one-skeleton of `\Sigma`. After gauge-fixing along this tree, the remaining
Haar integral can be written in plaquette coordinates

```math
(P_1,\ldots,P_A)\in SU(N)^A
```

with product Haar measure, and the boundary holonomy is an ordered product

```math
U_C=P_1P_2\cdots P_A
```

up to simultaneous conjugation, which is invisible to `\chi_\rho`.

Proof.

This is the finite axial-tree coordinate construction on a simply connected
plaquette disk. Choose a root vertex and a maximal tree in the sheet
one-skeleton. Gauge transformations set all tree links to the identity. Each
remaining link is the last unfixed edge of a unique plaquette in an ordering
compatible with the tree. The map from the unfixed links to plaquette
holonomies is triangular: at each step, the next plaquette holonomy is the
next unfixed link multiplied by already-fixed or already-processed links.
Left and right invariance of Haar measure gives product Haar measure in the
new plaquette variables. Because the sheet is a disk, the ordered product of
oriented plaquette boundaries cancels every internal edge once in each
orientation and leaves precisely the boundary holonomy. Residual root
conjugation does not change the character. `square`

### Theorem 4.3A.160V: Whole-Surface Normalized Gluing Identity

Let `\Sigma` be a clean disk surface as in Lemma 4.3A.160U, with boundary
`C` and area `A=|\Sigma|`. Consider the rho-monochromatic leading-channel
sheet integral

```math
I_\Sigma^\rho(k_\rho)
:=
\int
{1\over d_\rho}\chi_\rho(U_C)
\prod_{p\in\Sigma}k_\rho\chi_\rho(P_p^{-1})
\prod_{p\in\Sigma}dP_p.
```

Then

```math
I_\Sigma^\rho(k_\rho)
=
\left({k_\rho\over d_\rho}\right)^A.
```

Therefore every plaquette in a clean rho-monochromatic normalized sheet
contributes the normalized sheet weight `k_\rho/d_\rho`, with no residual
per-area `d_\rho` surcharge.

Proof.

By Lemma 4.3A.160U, after axial-tree gauge fixing the normalized boundary
record and the plaquette factors give

```math
I_\Sigma^\rho(k_\rho)
=
{k_\rho^A\over d_\rho}
\int_{G^A}
\chi_\rho(P_1\cdots P_A)
\prod_{r=1}^A\chi_\rho(P_r^{-1})
\prod_{r=1}^A dP_r.
```

Use the Schur convolution identity, which is Lemma 4.3A.160R with
`B=1`:

```math
\int_G \chi_\rho(XP)\chi_\rho(P^{-1})\,dP
=
{1\over d_\rho}\chi_\rho(X).
```

Integrating successively in `P_A,P_{A-1},\ldots,P_1` gives

```math
\int_{G^A}
\chi_\rho(P_1\cdots P_A)
\prod_{r=1}^A\chi_\rho(P_r^{-1})
\prod_{r=1}^A dP_r
=
d_\rho^{1-A}.
```

Indeed, after `A` integrations the remaining character is `\chi_\rho(1)=d_\rho`
and the convolution has supplied `A` factors of `d_\rho^{-1}`. Thus

```math
I_\Sigma^\rho(k_\rho)
=
{k_\rho^A\over d_\rho}d_\rho^{1-A}
=
\left({k_\rho\over d_\rho}\right)^A.
```

This proves the whole-surface identity. `square`

### Corollary 4.3A.160W: Clean-Surface Dimension Surcharge Is Zero

On the clean rho-monochromatic disk-surface branch of Theorem 4.3A.160V,

```math
\Delta_{dim}^{clean}=0.
```

In particular, the unique planar rectangular minimal sheets of Paper 13
Lemma 7.30P have normalized leading factor

```math
\left({k_\rho\over d_\rho}\right)^{N(C)}.
```

The same conclusion holds for any nonminimal admissible surface whose
rho-channel leading contribution can be decomposed into clean disk
components with normalized boundary records and no extra tensor-recouping
vertex. Such surfaces pay no per-excess dimension surcharge beyond the
normalized coefficient itself.

Proof.

Theorem 4.3A.160V gives the exact factor `(k_\rho/d_\rho)^{|\Sigma|}` for
each clean disk surface. Comparing this with Definition 4.3A.160M shows that
the normalized excess factor is not multiplied by any additional power of
`d_\rho`; hence `\widetilde B_C=B_C` for the clean leading channel and
`\Delta_{dim}^{clean}=0`. Paper 13 Lemma 7.30P says the rectangular minimal
sheet is the planar disk, so it is included in the clean class. `square`

### Corollary 4.3A.160X: Updated Boundary Of `NORM-SURF-EXT`

The normalized-surface fork has now been lifted from one plaquette to every
clean rho-monochromatic disk sheet. The remaining `P20-SEL2-NORM-SURF-EXT`
work is exactly the passage from clean leading sheets to the full moving
`SEL2` surface/collar expansion. The only places where a positive
dimension-surcharge can still enter are:

1. tensor recoupling at singular vertices, self-touching sheets, or
   non-disk local replacements;
2. non-leading representation insertions and their weighted character-tail
   conversion;
3. decoration polymers and KP regrouping on the sheet collar;
4. the real paired non-self-conjugate convention when the two channels mix
   through a decoration or corner;
5. the exact moving block/collar pushforward from the whole-process `SEL2`
   row law.

Thus the next pass/fail target is sharper:

```text
P20-SEL2-NORM-SURF-EXT-REM(Delta_rem):
  all non-clean leading, non-leading, corner, and decoration effects
  together have cofinal dimension surcharge Delta_rem.
```

If `Delta_rem<log d_rho`, the normalized route is a real improvement over the
parked raw branch by Theorem 4.3A.160O. If the best available bound is
`Delta_rem>=log d_rho`, the normalized route gives no useful advantage.

### Definition 4.3A.160Y: Remainder Surcharge Audit

The normalized-surface remainder audit
`P20-SEL2-NORM-SURF-EXT-REM(\Delta_{rem})` is decomposed into five possible
sources:

```math
\Delta_{rem}
=
\Delta_{corner}
+\Delta_{rec}
+\Delta_{ch}
+\Delta_{dec}
+\Delta_{pair/push}.
```

These are **dimension-surcharge** constants only. They do not count ordinary
surface entropy, decoration growth, character-tail activity, endpoint/corner
transport, or exact-entry loss already assigned to the disjoint Paper-19 and
Paper-20 ledgers.

The components mean:

1. `\Delta_{corner}`: surcharge from ordinary boundary corners and endpoint
   normalizations;
2. `\Delta_{rec}`: surcharge from singular tensor recoupling, self-touching
   sheets, branch vertices, or non-clean local replacements;
3. `\Delta_{ch}`: surcharge from non-leading representation insertions after
   they are moved to the declared character-tail ledger;
4. `\Delta_{dec}`: surcharge from residual decoration polymers after KP
   regrouping;
5. `\Delta_{pair/push}`: surcharge from the real paired convention and the
   exact block/collar pushforward.

If a component is paid as an ordinary finite debit in `E_corn`, `eta_ch`,
`d_{13}`, `U_13^{entry}`, or another already declared bucket, it is not also
counted as a dimension surcharge here.

### Lemma 4.3A.160Z: Corners Do Not Reintroduce Per-Excess Dimension

On the normalized Wilson-loop convention of Audit 4.3A.160Q, ordinary
rectangular boundary corners and endpoint normalizations do not create a
per-excess factor of `d_\rho`. Hence

```math
\Delta_{corner}=0.
```

Any finite endpoint/corner collar cost remains the already declared
`E_corn^{SEL2}` or corner-decoration debit; it is not a per-excess dimension
surcharge.

Proof.

The normalized boundary record is the single scalar
`d_\rho^{-1}\chi_\rho(U_C)`, independently of the number of corners in the
polygonal representative of `C`. Changing direction at a boundary corner
changes only the order and orientation of adjacent matrix factors inside the
same trace. It does not introduce an additional free representation trace.
Thus no factor `d_\rho` is created per added plaquette or per unit excess
area. The finite corner collars counted earlier are local record/collar
bookkeeping costs and stay in their disjoint debit register. `square`

### Lemma 4.3A.160AA: Non-Leading Channels And Decorations Carry Activity,
Not Dimension Surcharge

Assume the same-record character-tail and decoration audits already used by
`P19-T13-DEC`:

```text
P19-CHTAIL-AUDIT(eta_ch),
P19-T13-DEC(d_13).
```

Then non-leading representation insertions and residual decoration polymers
do not reintroduce an additional per-excess `d_\rho` surcharge in the
normalized leading sheet. In the notation of Definition 4.3A.160Y,

```math
\Delta_{ch}=0,
\qquad
\Delta_{dec}=0.
```

Their cost remains the finite activity/decorrelation debit already measured
by `eta_ch` and `d_13`.

Proof.

Paper 19 assigns the non-leading coefficient tail to the same representation
cutoff and decoration ledger as `P19-T13-DEC`. Its norm is measured as a
weighted character activity, schematically

```math
\sum_{\lambda\ne0,\rho}d_\lambda |k_{\lambda,j}|,
```

and then inserted into the KP decoration gas. This is an activity bound, not
a modification of the leading `rho`-sheet Schur convolution. Once a
non-leading insertion appears, the term is no longer part of the clean
rho-monochromatic leading sheet of Theorem 4.3A.160V; it is a decoration or
tail term. Charging it again as a `d_\rho` surcharge would double-count the
same object.

The same reasoning applies to residual decoration polymers. The KP regrouping
controls scalar activities in the sheet collar and contributes to the
ordinary growth factor `D_C` or to the finite decoration debit. It does not
change the Schur identity which gives the leading normalized factor
`k_\rho/d_\rho` on each clean plaquette. `square`

### Lemma 4.3A.160AB: Real Pairing And Pushforward Add No Surcharge Once Frozen

Under Audit 4.3A.160Q, the real paired convention for non-self-conjugate
representations and the exact scalar block/collar pushforward do not add a
per-excess dimension surcharge:

```math
\Delta_{pair/push}=0.
```

Proof.

The real paired record is the direct real scalar combination of the `rho` and
`\bar\rho` character channels. Schur orthogonality applies to each channel
with the same dimension `d_\rho=d_{\bar\rho}`. Cross-channel terms are either
absent by the frozen scalar projection or are non-leading mixed terms and
therefore belong to the character-tail/decorrelation ledger of Lemma
4.3A.160AA.

The block/collar pushforward is a map from the finite whole-process row law
to the declared scalar record law. Once the scalar readout and Haar
projection are frozen, the pushforward changes the values of the coefficients
`k_{\lambda,j}` but not the Schur normalization of the subsequent
finite-dimensional gluing computation. Thus it cannot by itself create a
new per-excess `d_\rho` factor. Any failure of convergence or exact-entry
transport remains in the `BC`, `CE`, `RPF`, `KPdec`, or `WP` source gates,
not in `\Delta_{pair/push}`. `square`

### Lemma 4.3A.160AC: Recoupling Is The Only Possible Dimension Surcharge

After Lemmas 4.3A.160Z--4.3A.160AB, the only remaining possible
dimension-surcharge source is singular recoupling:

```math
\Delta_{rem}=\Delta_{rec}.
```

Moreover, on any unreduced admissible-surface convention with at most
`r_{rec}q+O(1)` singular recoupling sites for excess area `q`, and with a
uniform local recoupling norm bound `C_{rec}`, one has the finite fallback

```math
\Delta_{rec}\le r_{rec}\log C_{rec}.
```

If the reduced surface-support convention is used, in which backtracking
pairs are removed, orientation/sign bookkeeping is absorbed into the scalar
loop record or decorations, and local replacements are counted only as
finite-degree support entropy, then

```math
\Delta_{rec}=0.
```

Proof.

The first statement is Definition 4.3A.160Y together with Lemmas
4.3A.160Z--4.3A.160AB. For the finite fallback, each singular recoupling site
is a finite-dimensional intertwiner contraction for the fixed representation
channel and the finite local replacement template. Compactness of the
finite-dimensional intertwiner space gives a finite operator norm
`C_{rec}`. If there are at most `r_{rec}q+O(1)` such sites on an excess-`q`
surface, their contribution is bounded by

```math
C_{rec}^{r_{rec}q+O(1)}
=
O(1)\exp(q\,r_{rec}\log C_{rec}).
```

The coefficient of `q` is the displayed surcharge.

Under the reduced support convention, such recoupling vertices are not part
of the leading rho-monochromatic sheet. Backtracking pairs have been removed,
orientation labels are not separate surface states, and local replacements
are counted in the finite-degree entropy factor rather than by tensoring
additional open representation legs into the leading sheet. The remaining
leading components are clean disk components covered by Theorem 4.3A.160V,
so no recoupling surcharge remains. `square`

### Theorem 4.3A.160AD: Decision For The Remainder Buckets

On the active reduced `SEL2` surface-support convention used for the
four-dimensional hypercubic template, corners, self-touching/local
replacements, non-leading channels, and decoration regrouping do **not**
reintroduce a per-excess dimension surcharge into the normalized leading
sheet:

```math
P20\text{-}SEL2\text{-}NORM\text{-}SURF\text{-}EXT\text{-}REM(0).
```

Equivalently,

```math
\Delta_{rem}=0.
```

If an unreduced surface convention is used instead, the theorem becomes the
finite carried-bound statement

```math
\Delta_{rem}\le r_{rec}\log C_{rec},
```

and the normalized route improves the raw route only if this bound is
strictly smaller than `\log d_\rho`.

Proof.

For the reduced `SEL2` convention, Lemma 4.3A.160Z gives
`\Delta_{corner}=0`; Lemma 4.3A.160AA gives
`\Delta_{ch}=\Delta_{dec}=0`; Lemma 4.3A.160AB gives
`\Delta_{pair/push}=0`; and Lemma 4.3A.160AC gives `\Delta_{rec}=0` because
the reduced convention removes singular recoupling from the leading sheet and
places local replacements in finite-degree entropy or decoration ledgers.
Substituting into Definition 4.3A.160Y gives `\Delta_{rem}=0`.

For an unreduced convention, only Lemma 4.3A.160AC changes: it gives the
finite fallback `r_{rec}\log C_{rec}`. The comparison with `\log d_\rho` is
exactly the improvement criterion of Theorem 4.3A.160O. `square`

### Corollary 4.3A.160AE: Normalized Route After The Surcharge Audit

On the active reduced `SEL2` surface convention, the dimension part of
`P20-SEL2-NORM-SURF` is closed with

```math
\Delta_{dim}^{SEL2}=0.
```

Consequently the normalized surface threshold in Theorem 4.3A.160O becomes

```math
\widetilde\kappa_{13}^{CE}
>
G_{13}^{raw}
+
\log\left(
1+
{M_{13}^{surf,SEL2}\over
\underline M_{pre13}^{SEL2,20}}
\right),
```

with the already-declared surface entropy, decoration, character-tail, and
nonsurface debits still present in `G_{13}^{raw}` and the pre-surface
margin. This does not prove confinement by itself. It proves only that the
normalized fork is a real route rather than an algebraic mirage: the missing
source estimate is now the positive normalized leading rate
`\widetilde\kappa_{13}^{CE}`, not another hidden dimension factor.

### Definition 4.3A.160AF: Normalized Positive-Rate Audit

On the active reduced normalized branch of Corollary 4.3A.160AE, define

```math
\widetilde a_{\rho,j}^{SEL2}
:=
{a_{\rho,j}^{SEL2}\over d_\rho}.
```

The normalized positive-rate audit
`P20-SEL2-CE-NORM-RATE(\widetilde\kappa_\rho)` asserts

```math
\liminf_j-\log \widetilde a_{\rho,j}^{SEL2}
\ge
\widetilde\kappa_\rho>0,
```

on the positive normalized branch. Equivalently, there is a strict normalized
subunit gap `\widetilde\sigma_\rho>0` such that

```math
\limsup_j\widetilde a_{\rho,j}^{SEL2}
\le
1-\widetilde\sigma_\rho.
```

In raw coefficient notation this is

```math
\limsup_j a_{\rho,j}^{SEL2}
\le
d_\rho(1-\widetilde\sigma_\rho),
```

not the stronger raw condition `a_{\rho,j}^{SEL2}<1`. Thus the normalized
branch has a different dynamical target: it must keep the normalized
coefficient away from its maximal value `1`, but it need not force the raw
coefficient below one.

The exact source estimate needed for the normalized surface theorem is the
strict inequality

```math
\widetilde\kappa_\rho
>
G_{13}^{raw}
+
\log\left(
1+
{M_{13}^{surf,SEL2}\over
\underline M_{pre13}^{SEL2,20}}
\right).
```

### Theorem 4.3A.160AG: Normalized Rate Is A Positive Block-Time Statement

Define the normalized heat-time comparison audit
`P20-SEL2-NORM-HKTIME(t_{eff,j},\widetilde\varepsilon_{\rho,j})` by

```math
\left|
\widetilde a_{\rho,j}^{SEL2}
-
e^{-t_{eff,j}C_2(\rho)/2}
\right|
\le
\widetilde\varepsilon_{\rho,j}.
```

This is the normalized form of the raw comparison in Definition 4.3A.160A,
with `\widetilde\varepsilon_{\rho,j}=\varepsilon_{\rho,j}/d_\rho` whenever the
raw comparison is available.

Assume cofinal positivity of `\widetilde a_{\rho,j}^{SEL2}`; for example, this
follows from `P20-SEL2-CE-SIGN(s_\rho)` because `d_\rho>0`. If
`P20-SEL2-NORM-HKTIME(t_{eff,j},\widetilde\varepsilon_{\rho,j})` holds and
there are constants `\delta_\rho>0` and `\eta_\rho\ge0` such that

```math
\liminf_j t_{eff,j}\ge\delta_\rho,
\qquad
\limsup_j\widetilde\varepsilon_{\rho,j}\le\eta_\rho,
```

with

```math
e^{-\delta_\rho C_2(\rho)/2}+\eta_\rho<1,
```

then the normalized rate audit holds with any strict

```math
0<
\widetilde\kappa_\rho
<
-\log\left(
e^{-\delta_\rho C_2(\rho)/2}+\eta_\rho
\right).
```

Conversely, if

```math
t_{eff,j}\to0,
\qquad
\widetilde\varepsilon_{\rho,j}\to0,
```

then

```math
\widetilde a_{\rho,j}^{SEL2}\to1
```

and `P20-SEL2-CE-NORM-RATE(\widetilde\kappa_\rho)` fails for every
`\widetilde\kappa_\rho>0`.

Proof.

Under the lower block-time bound,

```math
e^{-t_{eff,j}C_2(\rho)/2}
\le
e^{-\delta_\rho C_2(\rho)/2}
```

cofinally. The comparison audit gives

```math
\limsup_j\widetilde a_{\rho,j}^{SEL2}
\le
e^{-\delta_\rho C_2(\rho)/2}+\eta_\rho
<1.
```

On the positive branch, `-\log x` is decreasing and continuous on `(0,1)`, so
the displayed strict rate follows. If `t_{eff,j}\to0` and
`\widetilde\varepsilon_{\rho,j}\to0`, then the comparison gives
`\widetilde a_{\rho,j}^{SEL2}\to1`; hence the liminf of
`-\log\widetilde a_{\rho,j}^{SEL2}` is zero. `square`

### Corollary 4.3A.160AH: Current Status Of Normalized Positive Rate

The dimension-surcharge audit is closed on the active reduced `SEL2` branch,
but the normalized leading rate is not closed by the current imports.

More precisely:

1. finite pushforward, centrality, Peter-Weyl regularity, and the same-record
   scalar convention do not imply a positive lower bound on `t_{eff,j}`;
2. microscopic AF heat time tending to zero would falsify normalized positive
   rate if it is also the effective block character time;
3. Paper 13's surface coefficient is a renormalized block coefficient, so the
   current sources also do not prove that the effective time collapses to the
   microscopic AF time.

Thus Paper 20 has reduced the normalized route to the source audit

```text
P20-SEL2-NORM-BTIME-LIFT(delta_rho,eta_rho):
  prove the normalized heat-time comparison with
  liminf t_eff,j >= delta_rho > 0 and
  exp(-delta_rho C_2(rho)/2)+eta_rho < 1.
```

If this audit is proved, Theorem 4.3A.160AG supplies
`P20-SEL2-CE-NORM-RATE`. If instead the effective normalized time collapses to
zero with vanishing comparison error, the normalized route fails. The current
Paper-13/Paper-16/Paper-19 source set proves neither alternative.

Proof.

The positive-lift implication and collapse failure are exactly Theorem
4.3A.160AG. Lemma 4.3A.160J already proves that finite pushforward, centrality,
rowwise regularity, and same-record bookkeeping underdetermine the effective
block time: comparison rows can be built with either lifted time or microscopic
collapse. Paper 16 supplies microscopic AF time for local estimates, while
Paper 13 uses a renormalized block coefficient; without an additional source
identifying these two, neither lift nor collapse follows. `square`

### Lemma 4.3A.160AI: Normalized Character Ceiling And Escape Sets

Let

```math
\psi_\rho(U):={\Phi_\rho(U)\over d_\rho}.
```

Then `\psi_\rho` is a real central continuous function and

```math
-1\le\psi_\rho(U)\le1
\qquad(U\in SU(N)).
```

Let

```math
\mathcal E_\rho:=\{U:\psi_\rho(U)=1\}.
```

For every closed central set `V\subset SU(N)` disjoint from
`\mathcal E_\rho`, the gap

```math
\gamma_\rho(V):=
1-\sup_{U\in V}\psi_\rho(U)
```

is strictly positive.

Proof.

For the self-conjugate convention, `\Phi_\rho=\chi_\rho`; for the paired
convention, `\Phi_\rho=\operatorname{Re}\chi_\rho`. In either case,
`|\chi_\rho(U)|\le d_\rho` because `\rho(U)` is unitary and the character is a
trace of `d_\rho` unit-modulus eigenvalues. Hence
`\operatorname{Re}\chi_\rho(U)/d_\rho\in[-1,1]`, and the self-conjugate scalar
record satisfies the same two-sided bound. Continuity and centrality are
inherited from the character. If `V` is closed and disjoint from the closed
maximizing set `\mathcal E_\rho`, compactness gives
`\sup_V\psi_\rho<1`, which is the claimed positive gap. `square`

### Definition 4.3A.160AJ: Normalized Non-Identity Escape Witness

Fix a central measurable escape set `V_\rho` and constants
`\gamma_\rho,q_\rho>0` such that

```math
\psi_\rho(U)\le1-\gamma_\rho
\qquad(U\in V_\rho).
```

The normalized escape audit
`P20-SEL2-NORM-ESC(V_\rho,\gamma_\rho,q_\rho)` asserts

```math
\liminf_j \nu_{p,j}^{SEL2}(V_\rho)\ge q_\rho.
```

This is a one-block scalar-record spread statement. It says that the active
`SEL2` block plaquette marginal keeps a cofinal positive amount of mass away
from the normalized-character maximizer set. It is not a Wilson-loop area-law
statement and it does not assert a continuum Yang-Mills measure.

On the positive normalized branch define the intrinsic normalized block
character time

```math
\widetilde t_{\rho,j}^{blk}
:=
{2\over C_2(\rho)}
\log {1\over \widetilde a_{\rho,j}^{SEL2}}.
```

### Theorem 4.3A.160AK: Escape Witness Closes Normalized Rate

Assume cofinal positivity of `\widetilde a_{\rho,j}^{SEL2}` and
`P20-SEL2-NORM-ESC(V_\rho,\gamma_\rho,q_\rho)`. Then

```math
\limsup_j \widetilde a_{\rho,j}^{SEL2}
\le
1-q_\rho\gamma_\rho.
```

Consequently `P20-SEL2-CE-NORM-RATE(\widetilde\kappa_\rho)` holds for every
strict

```math
0<\widetilde\kappa_\rho<-\log(1-q_\rho\gamma_\rho),
```

and the intrinsic zero-error normalized block-time lift holds with every strict

```math
0<\delta_\rho
<
{2\over C_2(\rho)}
\left[-\log(1-q_\rho\gamma_\rho)\right].
```

In particular, the normalized surface-rate inequality of Definition
4.3A.160AF is certified by this escape witness whenever

```math
-\log(1-q_\rho\gamma_\rho)
>
G_{13}^{raw}
+
\log\left(
1+
{M_{13}^{surf,SEL2}\over
\underline M_{pre13}^{SEL2,20}}
\right).
```

Proof.

Since `\psi_\rho\le1` everywhere and `\psi_\rho\le1-\gamma_\rho` on
`V_\rho`,

```math
\widetilde a_{\rho,j}^{SEL2}
=
\int\psi_\rho\,d\nu_{p,j}^{SEL2}
\le
(1-\gamma_\rho)\nu_{p,j}^{SEL2}(V_\rho)
+1\cdot(1-\nu_{p,j}^{SEL2}(V_\rho))
=
1-\gamma_\rho\nu_{p,j}^{SEL2}(V_\rho).
```

Taking `limsup` and using the escape audit gives the first displayed bound.
The normalized rate conclusion follows from continuity and monotonicity of
`-\log x` on `(0,1)`. The intrinsic block-time statement is just the definition
of `\widetilde t_{\rho,j}^{blk}`. The final displayed condition is the
normalized surface threshold of Corollary 4.3A.160AE with the escape lower
bound substituted for `\widetilde\kappa_\rho`. For the block-time statement,
choose `t_{eff,j}=\widetilde t_{\rho,j}^{blk}` and
`\widetilde\varepsilon_{\rho,j}=0` in the normalized comparison audit.
`square`

### Theorem 4.3A.160AL: Escape Versus Normalized Collapse

For `0<\gamma<2`, set

```math
V_{\rho,\gamma}:=\{U:\psi_\rho(U)\le1-\gamma\}.
```

If

```math
\widetilde a_{\rho,j}^{SEL2}\to1,
```

then

```math
\nu_{p,j}^{SEL2}(V_{\rho,\gamma})\to0
\qquad(0<\gamma<2).
```

Conversely, if

```math
\nu_{p,j}^{SEL2}(V_{\rho,\gamma})\to0
\qquad(0<\gamma<2),
```

for every fixed `\gamma`, then

```math
\widetilde a_{\rho,j}^{SEL2}\to1.
```

Thus a cofinal normalized escape witness is exactly the obstruction to
collapse of the normalized leading coefficient to its maximal value, up to the
usual liminf/limsup distinction.

Proof.

The first implication follows from

```math
1-\widetilde a_{\rho,j}^{SEL2}
=
\int(1-\psi_\rho)\,d\nu_{p,j}^{SEL2}
\ge
\gamma\,\nu_{p,j}^{SEL2}(V_{\rho,\gamma}).
```

For the converse, fix `\epsilon>0` and choose `0<\gamma<\epsilon/2`. Since
`-1\le\psi_\rho\le1`, the integrand `1-\psi_\rho` is bounded by `2`. Split
the integral into `V_{\rho,\gamma}` and its complement:

```math
0\le
1-\widetilde a_{\rho,j}^{SEL2}
\le
2\nu_{p,j}^{SEL2}(V_{\rho,\gamma})
+\gamma.
```

The first term tends to zero and `\gamma<\epsilon/2`; letting `j` be large and
then `\epsilon\downarrow0` proves `\widetilde a_{\rho,j}^{SEL2}\to1`.
`square`

### Corollary 4.3A.160AM: Current Status After The Escape Reduction

The normalized branch is now reduced to a concrete one-block source:

```text
P20-SEL2-NORM-ESC(V_rho,gamma_rho,q_rho)
```

together with cofinal positivity. If this escape source is supplied and the
scalar inequality in Theorem 4.3A.160AK beats the surface threshold, the
normalized leading-rate gate closes. If the active `SEL2` block plaquette laws
collapse onto the normalized-character maximizer set in the sense of Theorem
4.3A.160AL, the normalized route fails.

The current Paper-13/Paper-16/Paper-19 imports do not prove either the cofinal
escape mass or the collapse alternative. The remaining mathematical source
problem is therefore no longer a dimension-normalization issue: it is the
one-block scalar spread problem for the pushed-forward `SEL2` plaquette
marginal.

### Theorem 4.3A.160AN: Existing Large-Field Sources Do Not Prove Escape

The current Paper-16/Paper-19 large-field and residual source imports do not
imply `P20-SEL2-NORM-ESC(V_\rho,\gamma_\rho,q_\rho)` for any fixed
`q_\rho>0`.

More precisely, the following data are insufficient:

1. central `L^1`/Peter-Weyl regularity of the pushed-forward plaquette marginal;
2. the common-record and no-smuggling audits;
3. `P20-SEL2-LFSRC`, hence the Paper-16 chain
   `HK-LF-SRC => HK-LF-CLOSE => HK-LFS`;
4. residual-polymer, decoration, and non-leading character-tail upper bounds.

Proof.

Each imported large-field or residual theorem has an upper-bound form. In the
notation of Paper 16 it bounds activities or coefficients supported on declared
large-field/bad-collar/polymer events, schematically as

```math
\sum_{Y\ni B} e^{m|Y|}|K_Y^{lf}|
\le \eta_{lf},
\qquad
\sum_{Y\ni B} e^{m|Y|}|K_Y^{res}|
\le \eta_{res},
```

or as a finite weighted upper bound on non-leading character coefficients. Such
statements control how much bad or residual material may be charged after the
finite block/collar decomposition. They are monotone in the direction of making
those bad/residual events smaller.

`P20-SEL2-NORM-ESC` has the opposite logical shape. It is a lower-bound
statement

```math
\liminf_j\nu_{p,j}^{SEL2}(V_\rho)\ge q_\rho>0
```

for a fixed set away from the maximizer set of `\psi_\rho`. No displayed
large-field, residual, decoration, or tail estimate contains such a lower
bound.

This is not just a missing line in the proof. At the level of the stated source
conclusions, the upper-bound hypotheses are compatible with approximate
identity central laws. For example, take a central smooth approximate identity
`h_{\epsilon_j}` on `SU(N)` with `\epsilon_j\downarrow0`, and set all residual
activities not forced by the one-block marginal to zero in the comparison row.
Then the regularity and all upper-envelope inequalities can be satisfied
abstractly, while for every closed central `V` disjoint from
`\mathcal E_\rho`,

```math
\int_V h_{\epsilon_j}(U)\,dU\to0,
\qquad
\int\psi_\rho(U)h_{\epsilon_j}(U)\,dU\to1.
```

Thus the current source conclusions are logically compatible with failure of
every positive escape lower bound. Therefore `P20-SEL2-NORM-ESC` cannot be
deduced from the existing large-field/residual imports alone. This comparison
row is not being claimed as an actual continuum Yang-Mills construction; it is a
counterexample to the formal implication from the currently stated source
conclusions to the escape lower bound. `square`

### Definition 4.3A.160AO: Normalized Microscopic-Collapse Source

The normalized same-target collapse audit `P20-SEL2-NCOLL-SRC` asserts that
there is an audited same-record heat time `s_j\downarrow0` such that the active
normalized block coefficient is same-target asymptotic to the heat-kernel
coefficient at that time:

```math
\left|
\widetilde a_{\rho,j}^{SEL2}
-\exp\{-s_jC_2(\rho)/2\}
\right|
\to0.
```

The microscopic AF collapse branch is the special case `s_j=t_{i(j)}`, where
`t_{i(j)}` is the bare Paper-16 AF heat-kernel time. The convolution-collapse
branch below is the special case `s_j=T_j^{SEL2,conv}`.

This is an exact coefficient-comparison assertion for the active `SEL2`
plaquette marginal. It is not supplied by the finite pushforward formalism or by
large-field upper-tail estimates.

### Theorem 4.3A.160AP: Microscopic Same-Target Comparison Proves Collapse

If `P20-SEL2-NCOLL-SRC` holds, then

```math
\widetilde a_{\rho,j}^{SEL2}\to1,
```

and hence, for every `0<\gamma<2`,

```math
\nu_{p,j}^{SEL2}(V_{\rho,\gamma})\to0,
\qquad
V_{\rho,\gamma}=\{U:\psi_\rho(U)\le1-\gamma\}.
```

Consequently no positive normalized escape witness can hold on the same target.

Proof.

Since `s_j\downarrow0`,

```math
\exp\{-s_jC_2(\rho)/2\}\to1.
```

The same-target comparison in `P20-SEL2-NCOLL-SRC` then gives
`\widetilde a_{\rho,j}^{SEL2}\to1`. The vanishing of every fixed escape set is
exactly the first implication of Theorem 4.3A.160AL. `square`

### Corollary 4.3A.160AQ: Decision Status For `P20-SEL2-NORM-ESC`

With the current Paper-13/Paper-16/Paper-19 imports, `P20-SEL2-NORM-ESC` is
neither proved nor falsified.

Theorem 4.3A.160AN proves that the existing large-field/residual source chain
does not imply a cofinal positive escape mass. Theorem 4.3A.160AP proves the
collapse alternative only under the additional same-target collapse comparison
`P20-SEL2-NCOLL-SRC`, which is also not supplied by the current imports.

Thus the honest fork is:

```text
P20-SEL2-NESC-SRC:
  prove a fixed non-identity escape lower mass for the actual SEL2 block
  plaquette marginal;

or

P20-SEL2-NCOLL-SRC:
  prove same-target comparison to an audited heat-kernel coefficient whose
  time tends to 0, which collapses the normalized branch.
```

Until one of these two source statements is proved on the active `SEL2` law, the
normalized leading-rate gate remains open. This is a genuine one-block
coefficient problem, not a Wilson-loop area-law input.

### Definition 4.3A.160AQ.1: Exact Normalized Escape Observable

Freeze the exact escape observable for the active normalized `SEL2` branch as

```math
\mathfrak e_\rho(U):=1-\psi_\rho(U),
\qquad
\psi_\rho(U)={\Phi_\rho(U)\over d_\rho}.
```

Thus `0\le\mathfrak e_\rho\le2`, and the normalized-character maximizer set is

```math
\mathcal E_\rho=\{U:\mathfrak e_\rho(U)=0\}
=\{U:\psi_\rho(U)=1\}.
```

For `0<\gamma<\gamma_\rho^{max}`, where

```math
\gamma_\rho^{max}:=\max_{U\in SU(N)}\mathfrak e_\rho(U)>0
```

for every nontrivial channel `\rho`, define the closed central escape window

```math
V_{\rho,\gamma}
:=
\{U\in SU(N):\mathfrak e_\rho(U)\ge\gamma\}
=
\{U:\psi_\rho(U)\le1-\gamma\}.
```

The exact cofinal escape mass for this window is

```math
Q_{\rho,\gamma}^{SEL2}
:=
\liminf_j\nu_{p,j}^{SEL2}(V_{\rho,\gamma}).
```

The exact escape-mass audit `P20-SEL2-NESC-EXACT(\gamma,q)` asserts

```math
Q_{\rho,\gamma}^{SEL2}\ge q>0.
```

This observable is intrinsic to the pushed-forward scalar plaquette record.
It uses no gauge chart, axial tree, continuum measure, or Wilson-loop area
law.

### Lemma 4.3A.160AQ.2: Escape Mass Is Equivalent To A Coefficient Gap

For every `0<\gamma<\gamma_\rho^{max}`:

1. if `P20-SEL2-NESC-EXACT(\gamma,q)` holds, then

   ```math
   \limsup_j\widetilde a_{\rho,j}^{SEL2}\le1-\gamma q;
   ```

2. if for some `\sigma>0`,

   ```math
   \limsup_j\widetilde a_{\rho,j}^{SEL2}\le1-\sigma,
   ```

   then for every `0<\gamma<\sigma`,

   ```math
   Q_{\rho,\gamma}^{SEL2}
   \ge
   {\sigma-\gamma\over2}.
   ```

Proof.

For the first clause, use `\psi_\rho\le1-\gamma` on `V_{\rho,\gamma}` and
`\psi_\rho\le1` everywhere:

```math
\widetilde a_{\rho,j}^{SEL2}
=
\int\psi_\rho\,d\nu_{p,j}^{SEL2}
\le
1-\gamma\nu_{p,j}^{SEL2}(V_{\rho,\gamma}).
```

Taking `limsup` gives
`\limsup_j\widetilde a_{\rho,j}^{SEL2}\le1-\gamma q`.

For the second clause,

```math
1-\widetilde a_{\rho,j}^{SEL2}
=
\int\mathfrak e_\rho\,d\nu_{p,j}^{SEL2}.
```

On `G\setminus V_{\rho,\gamma}`, `\mathfrak e_\rho<\gamma`; on
`V_{\rho,\gamma}`, `\mathfrak e_\rho\le2`. Therefore

```math
1-\widetilde a_{\rho,j}^{SEL2}
\le
\gamma+2\nu_{p,j}^{SEL2}(V_{\rho,\gamma}).
```

Taking `liminf` and using
`\liminf_j(1-\widetilde a_{\rho,j}^{SEL2})\ge\sigma` gives the displayed
lower bound. `square`

### Corollary 4.3A.160AQ.2A: Character-Gap Form Of The Escape Bound

Let `V_\rho\subset SU(N)` be a central measurable set. Suppose that, for some
`\gamma_\rho>0`,

```math
1-{\Phi_\rho(U)\over d_\rho}\ge\gamma_\rho
\qquad(U\in V_\rho),
```

and that the active `SEL2` block plaquette marginal has cofinal escape mass

```math
\liminf_j\nu_{p,j}^{SEL2}(V_\rho)\ge q_\rho>0.
```

Then

```math
\limsup_j {a_{\rho,j}^{SEL2}\over d_\rho}
\le
1-q_\rho\gamma_\rho.
```

Equivalently, on a cofinal tail and up to an arbitrary `o(1)` slack,

```math
{a_{\rho,j}^{SEL2}\over d_\rho}
\le
1-q_\rho\gamma_\rho+o(1).
```

Proof.

By definition,

```math
{a_{\rho,j}^{SEL2}\over d_\rho}
=
\int_{SU(N)}{\Phi_\rho(U)\over d_\rho}\,
d\nu_{p,j}^{SEL2}(U)
=
\int_{SU(N)}\psi_\rho(U)\,d\nu_{p,j}^{SEL2}(U).
```

On `V_\rho`, the character-gap assumption gives
`\psi_\rho(U)\le1-\gamma_\rho`; on the complement, the character bound gives
`\psi_\rho(U)\le1`. Therefore

```math
{a_{\rho,j}^{SEL2}\over d_\rho}
\le
(1-\gamma_\rho)\nu_{p,j}^{SEL2}(V_\rho)
+1\cdot(1-\nu_{p,j}^{SEL2}(V_\rho))
=
1-\gamma_\rho\nu_{p,j}^{SEL2}(V_\rho).
```

Taking `limsup` and using
`\liminf_j\nu_{p,j}^{SEL2}(V_\rho)\ge q_\rho` gives the displayed
coefficient gap. `square`

### Definition 4.3A.160AQ.2B: Normalized Lower-Bias Audit

The normalized lower-bias audit
`P20-SEL2-NORM-POS(s_\rho^{norm})` asserts

```math
\liminf_j {a_{\rho,j}^{SEL2}\over d_\rho}
\ge
s_\rho^{norm}>0.
```

This is the normalized version of the sign source. It is logically separate
from the escape audit: escape controls how far the normalized coefficient is
from its maximal value `1`; it does not prevent the coefficient from being
zero or negative.

### Theorem 4.3A.160AQ.2C: Positivity Plus Escape Gives The Normalized Window And Rate

Assume:

1. `P20-SEL2-NORM-POS(s_\rho^{norm})`;
2. a central escape set `V_\rho` with character gap

   ```math
   1-{\Phi_\rho(U)\over d_\rho}\ge\gamma_\rho>0
   \qquad(U\in V_\rho);
   ```

3. cofinal escape mass

   ```math
   \liminf_j\nu_{p,j}^{SEL2}(V_\rho)\ge q_\rho>0.
   ```

Then the normalized coefficient has the cofinal window

```math
0<s_\rho^{norm}
\le
\liminf_j {a_{\rho,j}^{SEL2}\over d_\rho}
\le
\limsup_j {a_{\rho,j}^{SEL2}\over d_\rho}
\le
1-q_\rho\gamma_\rho
<1.
```

Consequently the normalized leading sheet has positive rate. More precisely,
for every strict

```math
0<\widetilde\kappa_\rho
<
-\log(1-q_\rho\gamma_\rho),
```

one has

```math
\liminf_j
-\log\left({a_{\rho,j}^{SEL2}\over d_\rho}\right)
\ge
\widetilde\kappa_\rho.
```

Equivalently, the optimal lower bound delivered by these two source inputs is

```math
\liminf_j
-\log\left({a_{\rho,j}^{SEL2}\over d_\rho}\right)
\ge
-\log(1-q_\rho\gamma_\rho)>0.
```

Proof.

The lower bound is exactly `P20-SEL2-NORM-POS`. The upper bound is Corollary
4.3A.160AQ.2A. Since `q_\rho\gamma_\rho>0`, the upper endpoint is strictly
below one. On the cofinal positive branch, the function `-\log x` is
continuous and decreasing on `(0,1)`, so the displayed upper bound on
`a_{\rho,j}^{SEL2}/d_\rho` gives the displayed lower bound on the normalized
rate. `square`

### Theorem 4.3A.160AQ.3: Cofinal Escape Mass On The Strict Clean Scalar-Source Branch

Assume:

1. the standard `SEL2` sheet-time scaling audit holds, with

   ```math
   \liminf_jT_j^{SEL2,conv}\ge\delta_T>0;
   ```

2. the strict clean scalar-source assembly of Corollary 4.3A.165D holds, so
   `P20-SEL2-4DCOEFF-CLOSE(\epsilon_{\rho,j})` holds with
   `\epsilon_{\rho,j}\to0`.

Then the exact escape-mass audit holds. More precisely, set

```math
\sigma_\rho^{ref}
:=
1-\exp\{-\delta_TC_2(\rho)/2\}>0.
```

For every

```math
0<\gamma<\min\{\gamma_\rho^{max},\sigma_\rho^{ref}\},
```

one has

```math
Q_{\rho,\gamma}^{SEL2}
\ge
{\sigma_\rho^{ref}-\gamma\over2},
```

and hence `P20-SEL2-NESC-EXACT(\gamma,q)` holds for every strict

```math
0<q<{\sigma_\rho^{ref}-\gamma\over2}.
```

Proof.

The scalar coefficient source gives

```math
\left|
\widetilde a_{\rho,j}^{SEL2}
-
\exp\{-T_j^{SEL2,conv}C_2(\rho)/2\}
\right|
\le\epsilon_{\rho,j}
```

on a cofinal tail. Since `\liminf_jT_j^{SEL2,conv}\ge\delta_T`,

```math
\limsup_j\widetilde a_{\rho,j}^{SEL2}
\le
\exp\{-\delta_TC_2(\rho)/2\}
=1-\sigma_\rho^{ref}.
```

Lemma 4.3A.160AQ.2 with `\sigma=\sigma_\rho^{ref}` proves the displayed
escape-mass lower bound. `square`

### Theorem 4.3A.160AQ.4: Collapse Falsifies Every Fixed Exact Escape Window

If the same-target collapse source `P20-SEL2-NCOLL-SRC` holds, then for every
`0<\gamma<\gamma_\rho^{max}`,

```math
Q_{\rho,\gamma}^{SEL2}=0.
```

Consequently every fixed exact escape-mass audit
`P20-SEL2-NESC-EXACT(\gamma,q)` with `q>0` is false on that same target.

Proof.

Theorem 4.3A.160AP gives `\widetilde a_{\rho,j}^{SEL2}\to1`. The first
implication of Theorem 4.3A.160AL gives
`\nu_{p,j}^{SEL2}(V_{\rho,\gamma})\to0` for each fixed `\gamma`, hence
`Q_{\rho,\gamma}^{SEL2}=0`. `square`

### Corollary 4.3A.160AQ.5: Verdict For The Exact Escape Mass

The exact escape observable is now frozen:

```math
\mathfrak e_\rho=1-\psi_\rho,
\qquad
V_{\rho,\gamma}=\{\mathfrak e_\rho\ge\gamma\}.
```

The cofinal escape mass is:

```math
Q_{\rho,\gamma}^{SEL2}
=
\liminf_j\nu_{p,j}^{SEL2}(V_{\rho,\gamma}).
```

The result is a genuine fork.

1. On the strict clean scalar-source branch with positive convolution block
   time, Theorem 4.3A.160AQ.3 proves
   `P20-SEL2-NESC-EXACT(\gamma,q)` for every sufficiently small fixed
   `\gamma>0` and some `q>0`.
2. On a same-target normalized collapse branch, Theorem 4.3A.160AQ.4 proves
   `Q_{\rho,\gamma}^{SEL2}=0` for every fixed escape window.
3. With only rowwise regularity, large-field upper bounds, residual upper
   bounds, or finite pushforward formalism, the exact escape mass is neither
   proved nor falsified. Those inputs do not contain a lower anti-concentration
   estimate for `\nu_{p,j}^{SEL2}` away from `\mathcal E_\rho`.

This is Barandes-aligned: the escape mass is an operational statement about a
finite pushed-forward scalar record. It does not identify gauge coordinates
with ontology and it does not import confinement or an area law.

### Definition 4.3A.160AR: `SEL2` Effective Block-Time Worksheet

Freeze the following finite-row worksheet for the active `SEL2` block plaquette.
At row `j`, let `i=i(j)` be the underlying Paper-16 heat-kernel cutoff row and
let

```math
\mathscr S_j^{SEL2}
=\{b_1,\ldots,b_{n_j}\}
```

be the ordered finite sheet/collar list of microscopic plaquette increments
which the axial-tree `SEL2` block readout uses before residual and
off-sheet-bath corrections are applied. Each increment has a heat-kernel time
`\tau_{b,j}>0` and an orientation `\epsilon_b\in\{+1,-1\}`. The exact
heat-kernel convolution reference is the law

```math
\nu_{conv,j}^{SEL2}
:=
\operatorname{Law}
\left(
X_{b_1,j}^{\epsilon_{b_1}}\cdots
X_{b_{n_j},j}^{\epsilon_{b_{n_j}}}
\right),
```

where the `X_{b,j}` are independent `SU(N)` variables with densities
`H_{\tau_{b,j}}`. Its representation-independent block time is

```math
T_{j}^{SEL2,conv}
:=
\sum_{b\in\mathscr S_j^{SEL2}}\tau_{b,j}.
```

If all sheet increments use the same microscopic heat-kernel time `t_{i(j)}`,
then

```math
T_{j}^{SEL2,conv}
=
n_jt_{i(j)}.
```

More generally, write

```math
T_{j}^{SEL2,conv}
=
n_jt_{i(j)}+R_{j}^{time},
\qquad
R_{j}^{time}:=
\sum_{b\in\mathscr S_j^{SEL2}}(\tau_{b,j}-t_{i(j)}).
```

This is the frozen `SEL2` block-time scaling object. It is a finite-record
quantity built from the declared block readout. It is not a continuum
Yang-Mills measure, and it is not a Wilson-loop area-law assumption.

### Definition 4.3A.160AS: Same-Target Convolution Defect

Use the total-variation convention

```math
\|\mu-\nu\|_{TV}
:=
\sup_{\|f\|_\infty\le1}
\left|\int f\,d\mu-\int f\,d\nu\right|.
```

The same-target convolution defect for the active `SEL2` plaquette marginal is

```math
\varepsilon_{conv,j}^{SEL2}
:=
\left\|
\nu_{p,j}^{SEL2}-\nu_{conv,j}^{SEL2}
\right\|_{TV}.
```

The audit `P20-SEL2-CONV-CMP(\varepsilon_j)` asserts

```math
\varepsilon_{conv,j}^{SEL2}\le\varepsilon_j
```

on a cofinal row tail. When `\varepsilon_j\to0`, the actual pushed-forward
plaquette marginal and the exact convolution reference are same-target
asymptotic for every bounded scalar record.

### Lemma 4.3A.160AT: Heat-Kernel Convolution Computes The Reference Coefficient

For the convolution reference of Definition 4.3A.160AR,

```math
\nu_{conv,j}^{SEL2}=H_{T_j^{SEL2,conv}}(U)\,dU,
```

and therefore

```math
\int_{SU(N)}\psi_\rho(U)\,d\nu_{conv,j}^{SEL2}(U)
=
\exp\{-T_j^{SEL2,conv}C_2(\rho)/2\}.
```

Equivalently, in raw scalar normalization,

```math
\int_{SU(N)}\Phi_\rho(U)\,d\nu_{conv,j}^{SEL2}(U)
=
d_\rho\exp\{-T_j^{SEL2,conv}C_2(\rho)/2\}.
```

Proof.

The heat kernel on compact `SU(N)` is central, inversion-invariant, and obeys
the convolution semigroup law

```math
H_s*H_t=H_{s+t}.
```

Orientation signs do not change the law because `H_t(U^{-1})=H_t(U)`. Hence the
law of the ordered product of the independent increments is the iterated
convolution

```math
H_{\tau_{b_1,j}}*\cdots*H_{\tau_{b_{n_j},j}}
=
H_{\sum_b\tau_{b,j}}
=
H_{T_j^{SEL2,conv}}.
```

The Peter-Weyl expansion of `H_T` is

```math
H_T(U)
=
\sum_{\lambda\in\widehat{SU(N)}}
d_\lambda e^{-TC_2(\lambda)/2}\chi_\lambda(U),
```

in the standard heat-kernel normalization. Orthogonality of characters gives
the displayed raw coefficient. Dividing by `d_\rho` gives the normalized
coefficient. In the non-self-conjugate paired convention the same identity
holds after taking real parts, because the heat-kernel coefficient of `\rho`
and `\bar\rho` is the same. `square`

### Theorem 4.3A.160AU: Same-Target Coefficient Comparison On `SEL2`

If `P20-SEL2-CONV-CMP(\varepsilon_j)` holds, then

```math
\left|
\widetilde a_{\rho,j}^{SEL2}
-
\exp\{-T_j^{SEL2,conv}C_2(\rho)/2\}
\right|
\le
\varepsilon_j.
```

Consequently the normalized heat-time comparison audit
`P20-SEL2-NORM-HKTIME(t_{eff,j},\widetilde\varepsilon_{\rho,j})` holds with

```math
t_{eff,j}=T_j^{SEL2,conv},
\qquad
\widetilde\varepsilon_{\rho,j}=\varepsilon_j.
```

Proof.

By Definition 4.3A.160AJ,

```math
\widetilde a_{\rho,j}^{SEL2}
=
\int\psi_\rho\,d\nu_{p,j}^{SEL2},
\qquad
\|\psi_\rho\|_\infty\le1.
```

Lemma 4.3A.160AT computes the same integral against the convolution reference.
The total-variation definition gives

```math
\left|
\int\psi_\rho\,d\nu_{p,j}^{SEL2}
-
\int\psi_\rho\,d\nu_{conv,j}^{SEL2}
\right|
\le
\varepsilon_{conv,j}^{SEL2}
\le
\varepsilon_j.
```

This is exactly the displayed coefficient comparison. `square`

### Corollary 4.3A.160AV: The Scaling Fork Decides Escape Or Collapse

Assume `P20-SEL2-CONV-CMP(\varepsilon_j)` with `\varepsilon_j\to0`.

1. If

   ```math
   T_j^{SEL2,conv}\to0,
   ```

   then `P20-SEL2-NCOLL-SRC` holds and the normalized branch collapses:

   ```math
   \widetilde a_{\rho,j}^{SEL2}\to1.
   ```

2. If there is `\delta_T>0` such that

   ```math
   \liminf_jT_j^{SEL2,conv}\ge\delta_T,
   ```

   then the normalized positive-rate audit holds with every strict

   ```math
   0<\widetilde\kappa_\rho
   <
   {\delta_T C_2(\rho)\over2}.
   ```

   Moreover `P20-SEL2-NORM-ESC(V_\rho,\gamma_\rho,q_\rho)` holds for some
   central escape set `V_\rho` disjoint from `\mathcal E_\rho` and some
   `\gamma_\rho,q_\rho>0`.

Proof.

The first part follows immediately from Theorem 4.3A.160AU and
`T_j^{SEL2,conv}\to0`, which gives the same-target collapse source of
Definition 4.3A.160AO with `s_j=T_j^{SEL2,conv}`.

For the second part, Theorem 4.3A.160AU gives
`P20-SEL2-NORM-HKTIME(T_j^{SEL2,conv},\varepsilon_j)`. Apply Theorem
4.3A.160AG with any strict lower bound below `\delta_T` and with vanishing
error.

It remains to record the escape statement. Choose a closed central set
`V_\rho` with positive Haar measure and disjoint from `\mathcal E_\rho`; for
example, take the complement of a sufficiently small conjugation-invariant
neighborhood of `\mathcal E_\rho`. Lemma 4.3A.160AI gives a gap
`\gamma_\rho>0` on `V_\rho`. The heat-kernel density is strictly positive and
continuous on `(0,\infty)\times SU(N)`, and `H_T\to1` uniformly as
`T\to\infty`; hence

```math
q_0:=
\inf_{T\ge\delta_T/2}\int_{V_\rho}H_T(U)\,dU
>0.
```

For all sufficiently large `j`, `T_j^{SEL2,conv}\ge\delta_T/2`. Total-variation
comparison gives

```math
\nu_{p,j}^{SEL2}(V_\rho)
\ge
\nu_{conv,j}^{SEL2}(V_\rho)-\varepsilon_j
\ge
q_0-\varepsilon_j.
```

Thus `\liminf_j\nu_{p,j}^{SEL2}(V_\rho)\ge q_0`; taking any
`0<q_\rho<q_0` proves `P20-SEL2-NORM-ESC`. `square`

### Corollary 4.3A.160AW: What The Coefficient-Comparison Step Has Proved

The coefficient-normalization obstruction is now reduced to two explicit
finite-row questions:

```text
1. Prove the same-target convolution defect:
   epsilon_conv,j^SEL2 -> 0.

2. Evaluate the frozen block time:
   T_j^SEL2,conv = sum_{b in S_j^SEL2} tau_b,j.
```

If the defect vanishes, the sign of the route is decided by the scaling of
`T_j^{SEL2,conv}`:

```text
T_j^SEL2,conv -> 0
  => normalized collapse;

liminf_j T_j^SEL2,conv > 0
  => normalized escape and positive rate.
```

Theorem 4.3A.160AU is the rigorous same-target coefficient comparison on the
exact convolution branch. What remains open is not a character-normalization
issue and not an area-law input; it is the analytic comparison between the
actual four-dimensional `SEL2` block pushforward and the independent
heat-kernel convolution reference.

### Definition 4.3A.160AX: Real Four-Dimensional Convolution Defect Ledger

On the real four-dimensional `SEL2` heat-kernel row, fix the same axial-tree
block/collar chart used in the Paper-16/Paper-19 local estimates. Let
`\mathcal Y_j` denote the finite collection of sheet plaquette coordinates
entering `\mathscr S_j^{SEL2}` and let `\mathcal Z_j` denote all remaining
finite row variables in the same block/collar battery: off-sheet plaquettes,
collar plaquettes, Bianchi variables, local counterterm/scheme records, and
finite projective readout records.

After axial-tree gauge fixing and centralization, the real pushed-forward
plaquette marginal may be written abstractly as

```math
d\nu_{p,j}^{SEL2}
=
(P_j)_*
\left[
\mathcal R_j(Y,Z)\,
d\nu_{conv,j}^{sheet}(Y)\,d\lambda_j(Z)
\right],
```

where:

1. `d\nu_{conv,j}^{sheet}` is the independent sheet heat-kernel product whose
   product readout is `\nu_{conv,j}^{SEL2}`;
2. `d\lambda_j` is a finite reference law for the off-sheet/collar variables;
3. `\mathcal R_j` is the exact Radon-Nikodym correction coming from the
   four-dimensional link sharing, nonabelian cube/Bianchi relations,
   off-sheet plaquette action, counterterm/scheme insertions, and finite
   projective readout.

Define the four-dimensional convolution defect by

```math
\Delta_{4Dconv,j}^{SEL2}
:=
\left\|
(P_j)_*
\left[
(\mathcal R_j-1)\,
d\nu_{conv,j}^{sheet}d\lambda_j
\right]
\right\|_{TV}.
```

With this exact representation,

```math
\varepsilon_{conv,j}^{SEL2}
=
\Delta_{4Dconv,j}^{SEL2}.
```

The audit `P20-SEL2-4DCONV-CLOSE(\epsilon_j)` asserts

```math
\Delta_{4Dconv,j}^{SEL2}\le\epsilon_j,
\qquad
\epsilon_j\to0.
```

This is the real four-dimensional content of `P20-SEL2-CONV-CMP`; it is not a
notation choice.

### Lemma 4.3A.160AY: Why The 4D Defect Is Not Automatically Zero

For a two-dimensional axial-gauge heat-kernel sheet with no off-sheet plaquette
variables, `\mathcal R_j=1` and `P20-SEL2-CONV-CMP(0)` holds exactly.

For the real four-dimensional `SEL2` block/collar row, `\mathcal R_j=1` is not a
consequence of the finite heat-kernel action, axial-tree gauge fixing,
centrality, or Peter-Weyl regularity.

Proof.

In two dimensions, after axial-tree gauge fixing on a simply connected sheet,
the remaining plaquette variables may be chosen as independent coordinates and
the heat-kernel action is a product of one-plaquette heat kernels. The boundary
or block readout is then exactly the ordered product of independent heat-kernel
increments, so Definition 4.3A.160AR applies with zero defect.

In four dimensions, each sheet plaquette shares links with transverse plaquettes
and participates in nonabelian cube/Bianchi relations. In axial-tree
coordinates these constraints and off-sheet action terms appear precisely in
`\mathcal R_j`. The Paper-16 large-field, small-field, counterterm, and residual
ledgers bound selected activities and tails; they do not assert

```math
\mathcal R_j\to1
\quad\text{in the pushed-forward }L^1/TV\text{ sense}.
```

Centrality and Peter-Weyl regularity only identify the available scalar
coefficients after the law is known. They do not factor a four-dimensional
plaquette law into independent sheet increments. Therefore the zero-defect
convolution comparison is exact in the two-dimensional sheet model, but is a
new same-record analytic estimate in the real four-dimensional `SEL2` row.
`square`

### Theorem 4.3A.160AZ: Current Status Of `P20-SEL2-CONV-CMP`

With the current Paper-16/Paper-19/Paper-20 imports, the useful form

```math
P20\text{-}SEL2\text{-}CONV\text{-}CMP(\epsilon_j),
\qquad
\epsilon_j\to0,
```

is not proved for the real four-dimensional `SEL2` block pushforward.

What is proved is the exact reduction:

```math
P20\text{-}SEL2\text{-}4DCONV\text{-}CLOSE(\epsilon_j)
\Longrightarrow
P20\text{-}SEL2\text{-}CONV\text{-}CMP(\epsilon_j).
```

The trivial bound `P20-SEL2-CONV-CMP(2)` always holds under the total-variation
normalization of Definition 4.3A.160AS, but it is useless for the normalized
rate test.

Proof.

The implication is immediate from Definition 4.3A.160AX. The total-variation
distance between two probability measures is at most `2` under the convention
`\sup_{\|f\|_\infty\le1}`.

No current source theorem bounds `\Delta_{4Dconv,j}^{SEL2}` by a sequence
tending to zero. The existing sources supply finite-row regularity, character
tail controls, large-field suppression, counterterm/scheme residual estimates,
and finite transport ledgers. None of these is the pushed-forward
total-variation factorization estimate

```math
\left\|
(P_j)_*
\left[
(\mathcal R_j-1)\,
d\nu_{conv,j}^{sheet}d\lambda_j
\right]
\right\|_{TV}
\to0.
```

Setting this term to zero would replace the four-dimensional `SEL2` row by the
two-dimensional independent sheet reference, which is a process switch unless
the displayed estimate is proved on the same record law. `square`

### Definition 4.3A.160BA: Standard `SEL2` Sheet-Time Scaling Audit

The standard `SEL2` sheet-time scaling audit asserts that the finite sheet list
has area-plus-collar size

```math
n_j=S_j+B_j^{sheet},
\qquad
S_j=L_j^2,
\qquad
B_j^{sheet}=O(L_j),
```

and that the sheet heat-kernel times satisfy

```math
\max_{b\in\mathscr S_j^{SEL2}}
\left|{\tau_{b,j}\over t_{i(j)}}-1\right|
\to0.
```

The `O(L_j)` collar term is the usual finite-width boundary/collar correction.
It is allowed because `L_j/H_j\to0` on the AF-area selector.

### Theorem 4.3A.160BB: Evaluation Of `T_j^{SEL2,conv}` On The AF-Area Selector

Assume `P20-FROZEN-SEL` on the `SEL2` branch and the standard sheet-time scaling
audit of Definition 4.3A.160BA. Then

```math
s(1-\epsilon_A)(1-\chi)
\le
\liminf_j T_j^{SEL2,conv}
\le
\limsup_j T_j^{SEL2,conv}
\le
s(1+\epsilon_A)(1+\chi).
```

In particular,

```math
\liminf_jT_j^{SEL2,conv}>0.
```

Proof.

By Definition 1.1 and the `SEL2` shared coefficient selector,

```math
s(1-\epsilon_A)
\le
{S_j\over H_j}
\le
s(1+\epsilon_A),
\qquad
H_j=g_{i(j)}^{-2},
```

and

```math
1-\chi
\le
{t_{i(j)}\over g_{i(j)}^2}
\le
1+\chi.
```

Hence

```math
S_jt_{i(j)}
=
{S_j\over H_j}\,{t_{i(j)}\over g_{i(j)}^2}
```

has liminf at least `s(1-\epsilon_A)(1-\chi)` and limsup at most
`s(1+\epsilon_A)(1+\chi)`.

The collar correction is lower order. Since `L_j=\lfloor\sqrt{sH_j}\rfloor`,

```math
B_j^{sheet}t_{i(j)}=O(L_jg_{i(j)}^2)
=O(H_j^{1/2}H_j^{-1})
=O(H_j^{-1/2})\to0.
```

The relative time perturbation in Definition 4.3A.160BA gives

```math
\sum_{b\in\mathscr S_j^{SEL2}}\tau_{b,j}
=
n_jt_{i(j)}(1+o(1))
=
S_jt_{i(j)}+o(1).
```

This is exactly the displayed estimate for `T_j^{SEL2,conv}`. `square`

### Corollary 4.3A.160BB.1: Frozen `SEL2` Block-Time Window

Under the hypotheses of Theorem 4.3A.160BB, fix any strict constants

```math
0<T_-^{SEL2}<s(1-\epsilon_A)(1-\chi),
\qquad
T_+^{SEL2}>s(1+\epsilon_A)(1+\chi).
```

Then, on a cofinal tail,

```math
0<T_-^{SEL2}
\le
T_j^{SEL2,conv}
\le
T_+^{SEL2}
<\infty.
```

This is the finite-record block-time window used by the normalized coefficient
branch. The lower endpoint is the no-collapse input for the escape/subunit
half of the coefficient window. The upper endpoint is the no-blowup input for
the positivity/lower-bias half.

Proof.

This is the cofinal form of the liminf/limsup bounds in Theorem 4.3A.160BB,
with strict slack in the named constants. No continuum Yang-Mills measure,
Wilson-loop area law, or limiting process law is used; the input is only the
finite `SEL2` block selector and its sheet-time ledger. `square`

### Corollary 4.3A.160BC: Conditional `SEL2` Escape From The Real 4D Comparison

Assume:

1. `P20-SEL2-4DCONV-CLOSE(\epsilon_j)` with `\epsilon_j\to0`;
2. the standard `SEL2` sheet-time scaling audit of Definition 4.3A.160BA.

Then the normalized branch does not collapse. It satisfies
`P20-SEL2-NORM-ESC(V_\rho,\gamma_\rho,q_\rho)` for some fixed escape data and
has normalized positive rate with every strict

```math
0<\widetilde\kappa_\rho
<
{s(1-\epsilon_A)(1-\chi)C_2(\rho)\over2}.
```

Proof.

Theorem 4.3A.160AZ turns `P20-SEL2-4DCONV-CLOSE(\epsilon_j)` into
`P20-SEL2-CONV-CMP(\epsilon_j)`. Theorem 4.3A.160BB gives
`\liminf_jT_j^{SEL2,conv}\ge s(1-\epsilon_A)(1-\chi)>0`. Apply Corollary
4.3A.160AV. `square`

### Corollary 4.3A.160BD: Decision After Attempting The Real 4D Comparison

The scaling of the independent-convolution reference has now been evaluated:
on the standard `SEL2` AF-area selector, `T_j^{SEL2,conv}` stays bounded away
from zero. Therefore the convolution route would give normalized escape and
positive rate if the real four-dimensional pushforward were asymptotic in
total variation to that convolution reference.

But that comparison is exactly the new unsupplied source

```text
P20-SEL2-4DCONV-CLOSE(epsilon_j), epsilon_j -> 0.
```

The current corpus proves neither this estimate nor its failure. Thus the
independent-convolution route is conditionally favorable in scaling, but not
closed for actual four-dimensional `SU(N)`.

### Definition 4.3A.160BE: Scalar Convolution Coefficient Defect

The total-variation comparison in Definition 4.3A.160AS is stronger than the
surface-rate argument needs. The normalized leading sheet spends only the single
central scalar observable `\psi_\rho`. Define the scalar convolution coefficient
defect

```math
\delta_{\rho,conv,j}^{SEL2}
:=
\left|
\int\psi_\rho\,d\nu_{p,j}^{SEL2}
-
\int\psi_\rho\,d\nu_{conv,j}^{SEL2}
\right|.
```

By Lemma 4.3A.160AT this is equivalently

```math
\delta_{\rho,conv,j}^{SEL2}
=
\left|
\widetilde a_{\rho,j}^{SEL2}
-
\exp\{-T_j^{SEL2,conv}C_2(\rho)/2\}
\right|.
```

The scalar audit `P20-SEL2-SCONV-CLOSE(\epsilon_{\rho,j})` asserts

```math
\delta_{\rho,conv,j}^{SEL2}\le\epsilon_{\rho,j},
\qquad
\epsilon_{\rho,j}\to0.
```

Since `\|\psi_\rho\|_\infty\le1`,

```math
\delta_{\rho,conv,j}^{SEL2}
\le
\varepsilon_{conv,j}^{SEL2}
=
\Delta_{4Dconv,j}^{SEL2}.
```

Thus `P20-SEL2-4DCONV-CLOSE` implies the scalar audit, but the scalar audit is
strictly weaker: it permits four-dimensional corrections in directions
orthogonal to the one character coefficient actually used by the normalized
leading sheet.

### Lemma 4.3A.160BF: A Subunit Normalized Coefficient Forces Escape

Assume that for some `\sigma_\rho>0`,

```math
\limsup_j\widetilde a_{\rho,j}^{SEL2}\le1-\sigma_\rho.
```

Then, for every `0<\gamma<\sigma_\rho`, the closed central set

```math
V_{\rho,\gamma}:=\{U:\psi_\rho(U)\le1-\gamma\}
```

satisfies the normalized escape audit with any strict

```math
0<q_\rho<{\,\sigma_\rho-\gamma\,\over2}.
```

Proof.

Because `-1\le\psi_\rho\le1`,

```math
0\le1-\psi_\rho\le2.
```

On the complement of `V_{\rho,\gamma}`, one has `1-\psi_\rho<\gamma`. Hence

```math
1-\widetilde a_{\rho,j}^{SEL2}
=
\int(1-\psi_\rho)\,d\nu_{p,j}^{SEL2}
\le
\gamma
+2\nu_{p,j}^{SEL2}(V_{\rho,\gamma}).
```

The assumed limsup bound gives
`\liminf_j(1-\widetilde a_{\rho,j}^{SEL2})\ge\sigma_\rho`. Therefore

```math
\liminf_j\nu_{p,j}^{SEL2}(V_{\rho,\gamma})
\ge
{\sigma_\rho-\gamma\over2}.
```

Taking any strict smaller `q_\rho` proves
`P20-SEL2-NORM-ESC(V_{\rho,\gamma},\gamma,q_\rho)`. `square`

### Theorem 4.3A.160BG: Scalar Coefficient Comparison Is Enough On `SEL2`

Assume:

1. `P20-SEL2-SCONV-CLOSE(\epsilon_{\rho,j})`;
2. the standard `SEL2` sheet-time scaling audit of Definition 4.3A.160BA.

Then the normalized leading coefficient has positive rate. More precisely,
`P20-SEL2-CE-NORM-RATE(\widetilde\kappa_\rho)` holds for every strict

```math
0<\widetilde\kappa_\rho
<
{s(1-\epsilon_A)(1-\chi)C_2(\rho)\over2}.
```

Moreover `P20-SEL2-NORM-ESC(V_\rho,\gamma_\rho,q_\rho)` holds for some fixed
central escape data.

Proof.

The scalar audit gives the same normalized heat-time comparison as Theorem
4.3A.160AU, but only for the observable `\psi_\rho`:

```math
\left|
\widetilde a_{\rho,j}^{SEL2}
-
\exp\{-T_j^{SEL2,conv}C_2(\rho)/2\}
\right|
\le\epsilon_{\rho,j}.
```

By Theorem 4.3A.160BB,

```math
\liminf_jT_j^{SEL2,conv}
\ge
s(1-\epsilon_A)(1-\chi)>0.
```

The same theorem also gives a finite upper limsup for `T_j^{SEL2,conv}`, so the
heat-kernel coefficient on the right is bounded away from zero on a cofinal
tail. Since `\epsilon_{\rho,j}\to0`, the actual normalized coefficient is
cofinally positive. Theorem 4.3A.160AG therefore gives the displayed positive
normalized rate.
Equivalently, for every strict

```math
0<\sigma_\rho
<
1-
\exp\{-s(1-\epsilon_A)(1-\chi)C_2(\rho)/2\},
```

the scalar comparison gives
`\limsup_j\widetilde a_{\rho,j}^{SEL2}\le1-\sigma_\rho`. Lemma
4.3A.160BF then supplies a fixed escape set and fixed positive escape mass.
`square`

### Lemma 4.3A.160BG.1: Scalar Comparison Supplies Normalized Lower Bias

Assume:

1. `P20-SEL2-SCONV-CLOSE(\epsilon_{\rho,j})`, with
   `\epsilon_{\rho,j}\to0`;
2. the `SEL2` block-time upper window

   ```math
   T_j^{SEL2,conv}\le T_+^{SEL2}<\infty
   ```

   holds cofinally.

Then `P20-SEL2-NORM-POS(s_\rho^{norm})` holds for every strict

```math
0<s_\rho^{norm}
<
\exp\{-T_+^{SEL2}C_2(\rho)/2\}.
```

In particular one may choose the explicit safe value

```math
s_\rho^{norm}
=
{1\over2}\exp\{-T_+^{SEL2}C_2(\rho)/2\}
```

after moving to a sufficiently far cofinal tail.

Proof.

The scalar comparison gives

```math
\left|
\widetilde a_{\rho,j}^{SEL2}
-
\exp\{-T_j^{SEL2,conv}C_2(\rho)/2\}
\right|
\le
\epsilon_{\rho,j}.
```

The finite upper block-time bound gives the uniform heat-kernel lower bound

```math
\exp\{-T_j^{SEL2,conv}C_2(\rho)/2\}
\ge
\exp\{-T_+^{SEL2}C_2(\rho)/2\}
>0
```

cofinally. Since `\epsilon_{\rho,j}\to0`, for all sufficiently large `j`,

```math
\widetilde a_{\rho,j}^{SEL2}
\ge
{1\over2}\exp\{-T_+^{SEL2}C_2(\rho)/2\}.
```

This is exactly the normalized lower-bias audit. `square`

### Corollary 4.3A.160BG.2: Coefficient-Normalization Audit On The `SEL2` Branch

The coefficient used by the normalized surface expansion is

```math
\widetilde a_{\rho,j}^{SEL2}
=
{a_{\rho,j}^{SEL2}\over d_\rho}
=
\int_{SU(N)}{\Phi_\rho(U)\over d_\rho}\,
d\nu_{p,j}^{SEL2}(U).
```

Therefore:

1. positivity/lower bias means

   ```math
   \liminf_j\widetilde a_{\rho,j}^{SEL2}>0,
   ```

   not merely positivity of the raw Haar coefficient;
2. subunit rate means

   ```math
   \limsup_j\widetilde a_{\rho,j}^{SEL2}<1,
   ```

   not the stronger and generally false condition
   `\limsup_j a_{\rho,j}^{SEL2}<1`;
3. the normalized leading rate is always

   ```math
   \liminf_j-\log\widetilde a_{\rho,j}^{SEL2};
   ```

4. the raw coefficient may be larger than one when `d_\rho>1`, with no
   contradiction, because the exact whole-surface gluing identity has already
   moved the representation-dimension factor into the normalization.

This audit is the Barandes-aligned convention for the finite scalar record:
all claims are statements about the pushed-forward probability law of the
single normalized character observable `\psi_\rho=\Phi_\rho/d_\rho`.

Proof.

The identity is Definition 4.3A.160AF together with the scalar plaquette
readout convention. Items 1--3 are just the definitions of
`P20-SEL2-NORM-POS`, `P20-SEL2-CE-NORM-RATE`, and the escape audit. Item 4 is
Corollary 4.3A.160S and Theorem 4.3A.160V: after gluing the clean surface, the
local sheet weight is `a_{\rho,j}^{SEL2}/d_\rho`. `square`

### Corollary 4.3A.160BG.3: Full Normalized Window From Scalar Source Plus Escape

Assume:

1. `P20-SEL2-SCONV-CLOSE(\epsilon_{\rho,j})`, with
   `\epsilon_{\rho,j}\to0`;
2. the frozen `SEL2` block-time window

   ```math
   0<T_-^{SEL2}\le T_j^{SEL2,conv}\le T_+^{SEL2}<\infty
   ```

   holds cofinally;
3. a central escape set `V_\rho` has character gap

   ```math
   1-{\Phi_\rho(U)\over d_\rho}\ge\gamma_\rho>0
   \qquad(U\in V_\rho)
   ```

   and cofinal mass

   ```math
   \liminf_j\nu_{p,j}^{SEL2}(V_\rho)\ge q_\rho>0.
   ```

Then the normalized coefficient window closes:

```math
0<
s_\rho^{norm}
\le
\liminf_j\widetilde a_{\rho,j}^{SEL2}
\le
\limsup_j\widetilde a_{\rho,j}^{SEL2}
\le
1-q_\rho\gamma_\rho
<1,
```

where any strict

```math
0<s_\rho^{norm}
<
\exp\{-T_+^{SEL2}C_2(\rho)/2\}
```

is admissible after passing to a cofinal tail. Consequently

```math
\liminf_j-\log\widetilde a_{\rho,j}^{SEL2}
\ge
-\log(1-q_\rho\gamma_\rho)>0.
```

Equivalently, the named normalized rate may be taken as every strict

```math
0<\widetilde\kappa_\rho
<
-\log(1-q_\rho\gamma_\rho).
```

Proof.

The upper block-time bound and scalar comparison give
`P20-SEL2-NORM-POS(s_\rho^{norm})` by Lemma 4.3A.160BG.1. The escape set gives
the subunit upper bound by Corollary 4.3A.160AQ.2A. Theorem
4.3A.160AQ.2C combines the two estimates and gives the displayed rate. `square`

### Corollary 4.3A.160BG.4: `4DCOEFF-CLOSE` Version Of The Normalized Window

Assume:

1. `P20-SEL2-4DCOEFF-CLOSE(\epsilon_{\rho,j})`, with
   `\epsilon_{\rho,j}\to0`;
2. the standard `SEL2` sheet-time scaling audit of Definition 4.3A.160BA;
3. the exact escape data of Corollary 4.3A.160AQ.3 are chosen with
   `0<q_\rho` and `0<\gamma_\rho`.

Then the hypotheses of Corollary 4.3A.160BG.3 hold. Hence the active strict
`SEL2` branch has both:

```math
\liminf_j {a_{\rho,j}^{SEL2}\over d_\rho}>0,
\qquad
\limsup_j {a_{\rho,j}^{SEL2}\over d_\rho}\le1-q_\rho\gamma_\rho<1,
```

and

```math
\liminf_j
-\log\left({a_{\rho,j}^{SEL2}\over d_\rho}\right)
\ge
-\log(1-q_\rho\gamma_\rho)>0.
```

Proof.

`P20-SEL2-4DCOEFF-CLOSE` implies the scalar convolution comparison by
Definition 4.3A.160BH. The sheet-time audit gives the finite block-time window
by Corollary 4.3A.160BB.1. Corollary 4.3A.160AQ.3 supplies cofinal escape mass
on the same scalar record. Apply Corollary 4.3A.160BG.3. `square`

### Definition 4.3A.160BH: Scalar Four-Dimensional Coefficient Source

Using the exact four-dimensional representation of Definition 4.3A.160AX,
define the scalar four-dimensional convolution correction by

```math
\delta_{\rho,4Dconv,j}^{SEL2}
:=
\left|
\int
\psi_\rho(P_j(Y,Z))(\mathcal R_j(Y,Z)-1)\,
d\nu_{conv,j}^{sheet}(Y)\,d\lambda_j(Z)
\right|.
```

With the same record law and the same pushed-forward block readout,

```math
\delta_{\rho,conv,j}^{SEL2}
=
\delta_{\rho,4Dconv,j}^{SEL2}.
```

The scalar source audit `P20-SEL2-4DCOEFF-CLOSE(\epsilon_{\rho,j})` asserts

```math
\delta_{\rho,4Dconv,j}^{SEL2}\le\epsilon_{\rho,j},
\qquad
\epsilon_{\rho,j}\to0.
```

This is the correct weakened replacement for `P20-SEL2-4DCONV-CLOSE` if the
goal is only the normalized leading sheet rate. A natural source decomposition
is

```math
\delta_{\rho,4Dconv,j}^{SEL2}
\le
E_{\rho,Bianchi,j}^{SEL2}
+E_{\rho,off,j}^{SEL2}
+E_{\rho,col,j}^{SEL2}
+E_{\rho,ct,j}^{SEL2}
+E_{\rho,proj,j}^{SEL2},
```

where the five terms isolate, respectively, cube/Bianchi constraints,
off-sheet plaquette action, collar replacement, counterterm/scheme insertion,
and finite projective/readout effects. Each term is a scalar cumulant against
`\psi_\rho\circ P_j`, not a total-variation norm of the whole law.

### Definition 4.3A.160BH.1: Telescoped Scalar Correction Ledger

To make the five scalar terms unambiguous, choose on the same finite
block/collar battery an ordered interpolation

```math
\mathcal R_j^{(0)}=1,\qquad
\mathcal R_j^{(5)}=\mathcal R_j,
```

where the successive increments insert, in order,

```text
Bianchi, off-sheet, collar, counterterm/scheme, projective/readout.
```

Thus `\mathcal R_j^{(m)}` is the same finite-row Radon-Nikodym correction as
`\mathcal R_j`, but with only the first `m` declared correction classes
activated. The interpolation is a proof-coordinate device on the finite record
law; it is not a second process.

For `f_j(Y,Z):=\psi_\rho(P_j(Y,Z))`, define

```math
E_{\rho,m,j}^{SEL2}
:=
\left|
\int f_j(Y,Z)
\left(\mathcal R_j^{(m)}-\mathcal R_j^{(m-1)}\right)
d\nu_{conv,j}^{sheet}(Y)d\lambda_j(Z)
\right|,
```

and set

```math
E_{\rho,Bianchi,j}^{SEL2}:=E_{\rho,1,j}^{SEL2},\quad
E_{\rho,off,j}^{SEL2}:=E_{\rho,2,j}^{SEL2},\quad
E_{\rho,col,j}^{SEL2}:=E_{\rho,3,j}^{SEL2},
```

```math
E_{\rho,ct,j}^{SEL2}:=E_{\rho,4,j}^{SEL2},\quad
E_{\rho,proj,j}^{SEL2}:=E_{\rho,5,j}^{SEL2}.
```

Then

```math
\delta_{\rho,4Dconv,j}^{SEL2}
\le
E_{\rho,Bianchi,j}^{SEL2}
+E_{\rho,off,j}^{SEL2}
+E_{\rho,col,j}^{SEL2}
+E_{\rho,ct,j}^{SEL2}
+E_{\rho,proj,j}^{SEL2}.
```

Proof.

The identity

```math
\mathcal R_j-1
=
\sum_{m=1}^5
\left(\mathcal R_j^{(m)}-\mathcal R_j^{(m-1)}\right)
```

is telescopic. Multiply by `f_j`, integrate, and apply the triangle
inequality. `square`

### Definition 4.3A.160BH.1A: Actual Finite `SEL2` Row Freeze For `4DCOEFF`

The actual finite-row freeze `P20-SEL2-ACTROW` consists of the following
same-record data, all at the fixed cofinal row `j`.

```math
\mathfrak R_j^{SEL2}
:=
\left(
i(j),H_j,L_j,S_j,B_j^{sheet},
\mathscr S_j^{SEL2},\mathscr C_j^{SEL2},
Y_j,Z_j,\nu_{conv,j}^{sheet},\lambda_j,
\mathcal R_j,P_j,\psi_\rho
\right).
```

Here:

1. `Y_j` is the finite list of sheet plaquette variables in the `SEL2`
   block;
2. `Z_j` is the finite list of off-sheet, collar, Bianchi, counterterm/scheme,
   and readout variables retained in the same block/collar battery;
3. `\nu_{conv,j}^{sheet}` is the independent sheet heat-kernel reference with
   total time `T_j^{SEL2,conv}`;
4. `\lambda_j` is the finite reference law for `Z_j`;
5. `\mathcal R_j\ge0` is the rowwise Radon-Nikodym correction satisfying

   ```math
   \int \mathcal R_j\,d\nu_{conv,j}^{sheet}d\lambda_j=1;
   ```

6. `P_j(Y,Z)\in SU(N)` is the exact pushed-forward block plaquette readout;
7. `\psi_\rho=\Phi_\rho/d_\rho` is the normalized central character observable.

The freeze is finite-row and operational. It is not a continuum process axiom:
all objects live on a compact finite product of copies of `SU(N)` and finite
auxiliary records. The only comparison being attempted is the scalar
expectation of `\psi_\rho\circ P_j`.

### Lemma 4.3A.160BH.1B: `ACTROW` Gives The Exact Scalar Target

Assume `P20-SEL2-ACTROW`. Then

```math
\widetilde a_{\rho,j}^{SEL2}
=
\int \psi_\rho(P_j(Y,Z))\,
\mathcal R_j(Y,Z)\,
d\nu_{conv,j}^{sheet}(Y)d\lambda_j(Z),
```

and

```math
\exp\{-T_j^{SEL2,conv}C_2(\rho)/2\}
=
\int \psi_\rho(P_j(Y,Z))\,
d\nu_{conv,j}^{sheet}(Y)d\lambda_j(Z)
```

on the independent sheet reference. Consequently

```math
\left|
\widetilde a_{\rho,j}^{SEL2}
-
\exp\{-T_j^{SEL2,conv}C_2(\rho)/2\}
\right|
=
\delta_{\rho,4Dconv,j}^{SEL2}.
```

Proof.

The first identity is the definition of the pushed-forward actual finite row
under the rowwise density `\mathcal R_j`. The second identity is the
convolution heat-kernel character formula for the same normalized scalar
readout: multiplying independent sheet heat-kernel plaquettes and gluing them
through the clean normalized scalar record gives heat time
`T_j^{SEL2,conv}` and character coefficient
`e^{-T_j^{SEL2,conv}C_2(\rho)/2}`. Subtracting the two identities is exactly
Definition 4.3A.160BH. `square`

### Corollary 4.3A.160BH.1C: Five-Term Ledger Is The Complete Step-2 Target

Under `P20-SEL2-ACTROW`, the proof of `P20-SEL2-4DCOEFF-CLOSE` is reduced to
the five scalar quantities

```math
E_{\rho,Bianchi,j}^{SEL2},
E_{\rho,off,j}^{SEL2},
E_{\rho,col,j}^{SEL2},
E_{\rho,ct,j}^{SEL2},
E_{\rho,proj,j}^{SEL2}.
```

More precisely, if their sum tends to zero, then
`P20-SEL2-4DCOEFF-CLOSE(\epsilon_{\rho,j})` holds with

```math
\epsilon_{\rho,j}
:=
E_{\rho,Bianchi,j}^{SEL2}
+E_{\rho,off,j}^{SEL2}
+E_{\rho,col,j}^{SEL2}
+E_{\rho,ct,j}^{SEL2}
+E_{\rho,proj,j}^{SEL2}
\to0.
```

No total-variation convergence of the full actual row to the convolution row is
needed. Conversely, any proof that bypasses these five scalar ledgers must
still produce the same scalar bound on
`\delta_{\rho,4Dconv,j}^{SEL2}`; otherwise it has not proved the coefficient
source used by the normalized surface expansion.

Proof.

The first statement is the telescoped scalar correction bound in Definition
4.3A.160BH.1. The second statement is Lemma 4.3A.160BH.1B. The final sentence
is just the definition of
`P20-SEL2-4DCOEFF-CLOSE`: it is a scalar coefficient audit, not a law-level
metric audit. `square`

### Lemma 4.3A.160BH.2: Finite-Template Bounds For The Nonbulk Scalar Terms

Let `\omega_\rho(r)` be the uniform modulus of continuity of `\psi_\rho` on
`SU(N)` with respect to the fixed bi-invariant group metric. On the standard
`SEL2` finite block/collar template, the following same-record bounds hold.

1. **Projective/readout.** If the finite projective readout differs from the
   ideal scalar block product by a group-distance error at most `r_{proj,j}`
   outside an event of probability `p_{proj,j}`, and the remaining scalar
   projective law-transport debit is `\eta_{proj,j}^{sc}`, then

   ```math
   E_{\rho,proj,j}^{SEL2}
   \le
   \omega_\rho(r_{proj,j})+2p_{proj,j}+\eta_{proj,j}^{sc}.
   ```

2. **Counterterm/scheme.** If the clean local counterterm convention has
   absorbed all relevant/marginal pure-gauge counterterms into heat time,
   normalization, or boundary scalar factors, and the remaining irrelevant or
   scheme tail has scalar `L^1` size `\eta_{ct,j}^{sc}`, then

   ```math
   E_{\rho,ct,j}^{SEL2}\le\eta_{ct,j}^{sc}.
   ```

   On the clean minimal counterterm row of Paper 16, the strictly local
   relevant/marginal part contributes zero to this term; only the declared
   irrelevant/scheme tail can remain.

3. **Collar replacement.** Suppose the collar part changes the block product by
   group-distance at most `C_{col}B_j^{sheet}t_{i(j)}` outside the declared bad
   collar/residual event of scalar size `\eta_{col,j}^{bad}`. Then

   ```math
   E_{\rho,col,j}^{SEL2}
   \le
   \omega_\rho(C_{col}B_j^{sheet}t_{i(j)})
   +2\eta_{col,j}^{bad}.
   ```

Consequently, if `r_{proj,j}\to0`, `p_{proj,j}\to0`,
`\eta_{proj,j}^{sc}\to0`, `\eta_{ct,j}^{sc}\to0`,
`\eta_{col,j}^{bad}\to0`, and the standard `SEL2` sheet-time scaling audit
holds, then

```math
E_{\rho,proj,j}^{SEL2}
+E_{\rho,ct,j}^{SEL2}
+E_{\rho,col,j}^{SEL2}
\to0.
```

Proof.

For the projective/readout term, on the good event the scalar observable changes
by at most `\omega_\rho(r_{proj,j})`; on the bad event it changes by at most
`2`, because `-1\le\psi_\rho\le1`. The residual scalar law-transport debit is
by definition `\eta_{proj,j}^{sc}`.

The counterterm/scheme statement is exactly the scalar `L^1` bound against a
test function of sup norm at most one. The clean row removes the local
time-tangent and normalization pieces before this transverse scalar ledger is
formed, so they do not contribute.

For collars, use the same modulus-of-continuity argument on the good collar
event and the trivial oscillation bound `2` on the bad collar/residual event.
Finally, Definition 4.3A.160BA gives `B_j^{sheet}=O(L_j)` and
`t_{i(j)}=O(g_{i(j)}^2)=O(H_j^{-1})`, while
`L_j=O(H_j^{1/2})`; hence
`B_j^{sheet}t_{i(j)}=O(H_j^{-1/2})\to0`. Since `\omega_\rho(r)\to0` as
`r\downarrow0`, the displayed convergence follows. `square`

### Definition 4.3A.160BH.2A: Clean Nonbulk Scalar Audits

The clean nonbulk branch for the active normalized `SEL2` coefficient uses the
following four same-record audits.

1. `P20-SEL2-COL-CLEAN` asserts that the good-collar replacement has a finite
   template constant `C_{col}<\infty` with

   ```math
   d_G(P_j^{col},P_j^{ideal})
   \le C_{col}B_j^{sheet}t_{i(j)}
   ```

   on the good collar event, and that the scalar bad-collar transition size
   satisfies

   ```math
   \eta_{col,j}^{bad}\to0.
   ```

   Bad-collar events are the union of collar-cutoff transitions, collar
   partition derivatives, and residual collar replacements not already assigned
   to the large-field ledger.
2. `P20-SEL2-CT-CLEAN` asserts that the matched heat-time convention has
   absorbed every relevant or marginal local pure-gauge counterterm into the
   heat-time tangent, scalar normalization, or finite boundary scalar factor,
   and that the remaining irrelevant/scheme scalar tail obeys

   ```math
   \eta_{ct,j}^{sc}\to0.
   ```

3. `P20-SEL2-PROJ-CLEAN` asserts that the coefficient is read from the exact
   pushed-forward scalar block record, or from a projective readout with

   ```math
   r_{proj,j}\to0,\qquad
   p_{proj,j}\to0,\qquad
   \eta_{proj,j}^{sc}\to0.
   ```

4. `P20-SEL2-NONBULK-COMMON` asserts that the three audits above are evaluated
   on the same finite row law, with the same scalar record `\psi_\rho`, the
   same block/collar stencil, and the same debit partition as
   Definition 4.3A.160BH.1. In particular, no perimeter/cusp/readout,
   projective, counterterm, or collar transition term is charged twice.

The finite fallback audit `P20-SEL2-NONBULK-FIN(E_{\rho,nonbulk})` asserts

```math
\limsup_j
\left(
E_{\rho,col,j}^{SEL2}
+E_{\rho,ct,j}^{SEL2}
+E_{\rho,proj,j}^{SEL2}
\right)
\le E_{\rho,nonbulk}<\infty.
```

### Theorem 4.3A.160BH.2B: Clean Nonbulk Scalar Closure

Assume the standard `SEL2` sheet-time scaling audit and
`P20-SEL2-NONBULK-COMMON`.

1. If `P20-SEL2-COL-CLEAN`, `P20-SEL2-CT-CLEAN`, and
   `P20-SEL2-PROJ-CLEAN` hold, then

   ```math
   E_{\rho,col,j}^{SEL2}
   +E_{\rho,ct,j}^{SEL2}
   +E_{\rho,proj,j}^{SEL2}
   \to0.
   ```

2. If only `P20-SEL2-NONBULK-FIN(E_{\rho,nonbulk})` holds, then the nonbulk
   scalar correction contributes at most the carried finite debit
   `E_{\rho,nonbulk}` to the finite-gap scalar comparison.

Proof.

Clause 1 is Lemma 4.3A.160BH.2 with the clean audit hypotheses inserted. The
collar good-event displacement satisfies

```math
C_{col}B_j^{sheet}t_{i(j)}=O(H_j^{-1/2})\to0,
```

and `\eta_{col,j}^{bad}\to0`, so the collar term vanishes. The counterterm and
projective/readout terms vanish by their declared scalar tails and modulus
bounds. The common-record audit guarantees these are disjoint scalar ledgers.

Clause 2 is the definition of `P20-SEL2-NONBULK-FIN` together with the
telescopic scalar correction bound of Lemma 4.3A.160BH.1. `square`

### Corollary 4.3A.160BH.2C: Status Of Collar, Counterterm, And Projective Readout

The collar replacement/bad-collar transition, counterterm/scheme, and
projective/readout parts are now closed on the strict clean branch in the
precise sense needed for the vanishing scalar source:

```math
E_{\rho,col,j}^{SEL2}
+E_{\rho,ct,j}^{SEL2}
+E_{\rho,proj,j}^{SEL2}
\to0.
```

On any branch that keeps a nonvanishing bad-collar event, an irrelevant/scheme
tail, or a projective/readout mismatch, the proof does not erase that term.
It must be carried as `E_{\rho,nonbulk}` and tested in the finite-gap
inequality of Theorem 4.3A.160BH.5.

### Definition 4.3A.160BH.2D: Clean-Branch Source Audit

`P20-SEL2-CLEAN-SRC` is the audit that the clean nonbulk assumptions are not
new process axioms. It consists of the following source identifications.

1. **Common record.** The `SEL2` coefficient row, block/collar template,
   scalar record `\psi_\rho`, counterterm convention, and projective readout
   convention are the same pushed-forward finite record data used by the
   Paper-16 heat-kernel analytic branch and by the Paper-19 source constants.
2. **Counterterm source.** The row uses the clean minimal Paper-16
   counterterm convention: all relevant/marginal pure-gauge counterterms are
   absorbed into the heat-time tangent, scalar normalization, or finite
   boundary scalar factor, and no nonlocal irrelevant/scheme tail remains in
   the coefficient ledger.
3. **Collar source.** The row uses the Paper-16 collar-refined large-field
   assignment: collar-cutoff transitions and bad collars are assigned to the
   adjacent large-field/bad-collar polymer event. On the clean scalar-source
   branch, the residual scalar size of that event satisfies
   `\eta_{col,j}^{bad}\to0` on the selected `SEL2` battery.
4. **Readout source.** Either the coefficient is computed from the exact finite
   pushed-forward scalar block record, or a separate projective/readout source
   proves
   `r_{proj,j},p_{proj,j},\eta_{proj,j}^{sc}\to0`.
5. **No double charge.** If a term is assigned to the large-field ledger,
   counterterm ledger, projective/readout ledger, boundary/collar debit, or
   loop-readout transport ledger, it is not also assigned to another one of
   these ledgers.

### Theorem 4.3A.160BH.2E: Source Verdict For The Clean Nonbulk Audits

On the current Paper-16/Paper-20 source base, `P20-SEL2-CLEAN-SRC` has the
following exact verdict.

1. The common-record clause is proved by the `SEL2` no-smuggling/common-record
   convention: all quantities are finite pushed-forward scalar records on the
   same heat-kernel row.
2. The counterterm source is proved on the clean minimal row by Paper 16
   Theorem 9K.2G, which gives

   ```text
   HK-CT-RATE => HK-CT-SRC => HK-CT-CLOSE
   ```

   with zero nonlocal counterterm and scheme amplitudes. Hence
   `P20-SEL2-CT-CLEAN` holds on that branch.
3. The collar source is proved only on the branch that uses the Paper-16
   collar-refined large-field assignment and imports the corresponding
   large-field/bad-collar scalar decay on the selected `SEL2` battery. On that
   branch, `P20-SEL2-COL-CLEAN` holds. If the bad-collar event is not assigned
   to the large-field ledger or its scalar size is not shown to vanish, then
   `P20-SEL2-COL-CLEAN` is not proved and the term must be carried inside
   `E_{\rho,nonbulk}` or `E_{\rho,col,*}^{SEL2,bd}`.
4. The readout source is proved on the exact finite scalar-record branch, where
   `r_{proj,j}=p_{proj,j}=\eta_{proj,j}^{sc}=0`. On a genuine projective or
   finite-precision readout branch, `P20-SEL2-PROJ-CLEAN` is not proved by
   rowwise regularity; it requires the projective/readout ledger exported from
   Paper 16's `HK-PROJ-CLOSE` or an equivalent same-record source.

Consequently, on the strict exact-record, clean-minimal-counterterm,
collar-refined large-field branch, `P20-SEL2-CLEAN-SRC` proves
`P20-SEL2-NONBULK-COMMON`, `P20-SEL2-COL-CLEAN`,
`P20-SEL2-CT-CLEAN`, and `P20-SEL2-PROJ-CLEAN`. On every other branch the
unproved pieces are explicitly parked as carried nonbulk debits.

Proof.

Clause 1 is the declared `SEL2` branch convention and contains no continuum
limit assumption. Clause 2 is exactly the clean minimal-row conclusion of
Paper 16 Theorem 9K.2G; strictly local terms are time/normalization/boundary
coordinates, not residual scalar counterterm tails. Clause 3 is the
large-field/collar assignment of Paper 16 applied to the same finite
block/collar record; if the bad-collar scalar event tends to zero, Lemma
4.3A.160BH.2 turns it into a vanishing collar correction. Clause 4 is
immediate for the exact finite scalar record. If one replaces that exact
record by a projective or finite-precision record, the displayed error
parameters are additional same-record source data and cannot be inferred from
regularity. Clause 5 is precisely the debit partition in
`P20-SEL2-NONBULK-COMMON`. `square`

### Corollary 4.3A.160BH.2F: Clean Nonbulk Assumption Status

The clean nonbulk assumptions are now audited as source theorems rather than
left as free hypotheses.

```text
CT-CLEAN:    proved on the Paper-16 clean minimal row.
COL-CLEAN:   proved only with the Paper-16 collar-refined large-field
             assignment and vanishing bad-collar scalar event.
PROJ-CLEAN:  proved on the exact finite scalar-record branch; otherwise
             parked pending HK-PROJ-CLOSE/projective readout estimates.
COMMON:      proved by the SEL2 same-record/no-smuggling convention.
```

This is the Barandes-aligned reading: the proof coordinates and readout maps
are finite operational records. No continuum Yang-Mills measure, area law, or
unmentioned projective limit is inserted here.

### Corollary 4.3A.160BH.2G: Step-3 Actual Nonbulk Closure

Assume:

1. `P20-SEL2-ACTROW`;
2. the standard `SEL2` sheet-time scaling audit;
3. `P20-SEL2-CLEAN-SRC` on the strict exact-record, clean-minimal-counterterm,
   collar-refined large-field branch.

Then the actual finite `SEL2` row satisfies

```math
E_{\rho,col,j}^{SEL2}
+E_{\rho,ct,j}^{SEL2}
+E_{\rho,proj,j}^{SEL2}
\to0.
```

Equivalently, Steps 1--3 of the scalar coefficient source are closed on the
strict branch: the actual row is frozen, the five-term scalar ledger is the
active ledger, and the three nonbulk ledgers vanish.

On any non-strict branch, the exact replacement is

```math
\limsup_j
\left(
E_{\rho,col,j}^{SEL2}
+E_{\rho,ct,j}^{SEL2}
+E_{\rho,proj,j}^{SEL2}
\right)
\le
E_{\rho,nonbulk},
```

with `E_{\rho,nonbulk}` carried into the finite-gap scalar comparison.

Proof.

`P20-SEL2-ACTROW` fixes the finite row and scalar readout used in
Definitions 4.3A.160BH--4.3A.160BH.1C. The clean-source verdict of Theorem
4.3A.160BH.2E supplies `P20-SEL2-NONBULK-COMMON`,
`P20-SEL2-COL-CLEAN`, `P20-SEL2-CT-CLEAN`, and
`P20-SEL2-PROJ-CLEAN` on the strict branch. Theorem 4.3A.160BH.2B then gives
the displayed convergence. The fallback statement is exactly
`P20-SEL2-NONBULK-FIN(E_{\rho,nonbulk})`. `square`

### Definition 4.3A.160BH.3: Bulk Bianchi/Off-Sheet Scalar Envelope

The bulk part is different from the finite-template collar/counterterm/readout
pieces: it can touch every interior plaquette of the `SEL2` sheet. Define the
rowwise scalar bulk activity envelope by the smallest numbers
`\zeta_{\rho,bulk,j}^{SEL2}` and `\zeta_{\rho,bd,j}^{SEL2}` for which the
connected scalar cumulant expansion of the Bianchi and off-sheet correction
satisfies

```math
E_{\rho,Bianchi,j}^{SEL2}+E_{\rho,off,j}^{SEL2}
\le
S_j\zeta_{\rho,bulk,j}^{SEL2}
+B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2}.
```

Equivalently, `\zeta_{\rho,bulk,j}^{SEL2}` is the supremum, over an interior
sheet plaquette, of the rooted sum of absolute connected scalar cumulants that
touch that plaquette and at least one Bianchi cube or off-sheet plaquette; the
boundary version is the analogous rooted sum for sheet-collar plaquettes. This
is the scalar analogue of the Paper-16 connected-polymer activity norm, with
the test observable fixed to `\psi_\rho\circ P_j`.

The zero-bulk audit `P20-SEL2-BULKSC-ZERO` asserts

```math
S_j\zeta_{\rho,bulk,j}^{SEL2}\to0,
\qquad
B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2}\to0.
```

The finite-bulk audit `P20-SEL2-BULKSC-FIN(\Xi_\rho)` asserts

```math
\limsup_j
\left(
S_j\zeta_{\rho,bulk,j}^{SEL2}
+B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2}
\right)
\le\Xi_\rho<\infty.
```

### Lemma 4.3A.160BH.4: Bulk Envelope Bound

The envelope of Definition 4.3A.160BH.3 gives the exact scalar estimate

```math
E_{\rho,Bianchi,j}^{SEL2}+E_{\rho,off,j}^{SEL2}
\le
S_j\zeta_{\rho,bulk,j}^{SEL2}
+B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2}.
```

In particular, `P20-SEL2-BULKSC-ZERO` makes the Bianchi/off-sheet contribution
vanish, while `P20-SEL2-BULKSC-FIN(\Xi_\rho)` leaves at most the finite carried
scalar debit `\Xi_\rho`.

Proof.

Root every connected scalar cumulant contributing to the Bianchi/off-sheet
correction at the first sheet plaquette it touches, using the fixed ordering of
the `SEL2` sheet/collar list. Interior roots contribute at most
`\zeta_{\rho,bulk,j}^{SEL2}` each, and there are `S_j` such roots. Boundary
roots contribute at most `\zeta_{\rho,bd,j}^{SEL2}` each, and there are
`B_j^{sheet}` of them. Summing the rooted absolute values gives the displayed
bound. This is the standard connected-polymer root-counting estimate, now
applied to the scalar observable `\psi_\rho\circ P_j`. `square`

### Theorem 4.3A.160BH.5: Scalar Correction Pass Tests

Let

```math
\delta_{\rho,*}^{SEL2}
:=
\limsup_j
\delta_{\rho,4Dconv,j}^{SEL2}.
```

The following pass tests hold.

1. If the three nonbulk terms in Lemma 4.3A.160BH.2 vanish and
   `P20-SEL2-BULKSC-ZERO` holds, then
   `P20-SEL2-4DCOEFF-CLOSE(\epsilon_{\rho,j})` holds for some
   `\epsilon_{\rho,j}\to0`.

2. More generally, suppose the standard `SEL2` sheet-time scaling audit holds,
   the normalized leading coefficient is cofinally positive, and

   ```math
   \delta_{\rho,*}^{SEL2}
   <
   1-\exp\{-s(1-\epsilon_A)(1-\chi)C_2(\rho)/2\}.
   ```

   Then the normalized leading coefficient still has a positive subunit gap,
   with every strict

   ```math
   0<\widetilde\kappa_\rho
   <
   -\log\left(
   \exp\{-s(1-\epsilon_A)(1-\chi)C_2(\rho)/2\}
   +\delta_{\rho,*}^{SEL2}
   \right).
   ```

   Consequently the normalized branch reaches the same escape/rate conclusion
   as Theorem 4.3A.160BG, with the reduced rate displayed above.

Proof.

The first clause follows by combining Definition 4.3A.160BH.1, Lemma
4.3A.160BH.2, and Lemma 4.3A.160BH.4.

For the second clause, Definition 4.3A.160BH gives

```math
\widetilde a_{\rho,j}^{SEL2}
\le
\exp\{-T_j^{SEL2,conv}C_2(\rho)/2\}
+\delta_{\rho,4Dconv,j}^{SEL2}.
```

Theorem 4.3A.160BB gives
`\liminf_jT_j^{SEL2,conv}\ge s(1-\epsilon_A)(1-\chi)`. Taking limsup yields

```math
\limsup_j\widetilde a_{\rho,j}^{SEL2}
\le
\exp\{-s(1-\epsilon_A)(1-\chi)C_2(\rho)/2\}
+\delta_{\rho,*}^{SEL2}
<1.
```

The cofinal positivity assumption puts the normalized coefficient in `(0,1)`
on a cofinal tail, so continuity of `-\log` gives the displayed rate. Lemma
4.3A.160BF then supplies a fixed escape witness. `square`

### Corollary 4.3A.160BH.6: Current Bound Status For The Five Scalar Terms

On the present source base, the nonbulk terms are sharply reduced but the bulk
term is not closed.

1. `E_{\rho,ct,j}^{SEL2}` is zero for the strictly local clean
   counterterm/time-tangent part and is reduced to the Paper-16 irrelevant or
   scheme-tail scalar ledger for any remaining tail.
2. `E_{\rho,proj,j}^{SEL2}` is reduced to the finite projective/readout
   modulus and scalar projective transport debit.
3. `E_{\rho,col,j}^{SEL2}` is reduced to the boundary estimate
   `B_j^{sheet}t_{i(j)}\to0` plus the declared bad-collar/residual scalar
   event.
4. The combined Bianchi/off-sheet term is reduced to the bulk envelope
   `S_j\zeta_{\rho,bulk,j}^{SEL2}+B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2}`.

The last item is the real remaining obstruction. Since `S_j\sim H_j` on the
AF-area selector, a merely pointwise small bulk correction
`\zeta_{\rho,bulk,j}^{SEL2}=O(g_{i(j)}^2)=O(H_j^{-1})` gives an order-one
carried debit, not a vanishing scalar comparison. To close
`P20-SEL2-4DCOEFF-CLOSE` one needs the stronger cancellation

```math
\zeta_{\rho,bulk,j}^{SEL2}=o(H_j^{-1}),
```

or, for the finite-gap route in Theorem 4.3A.160BH.5, an explicit finite value
of the limsup small enough to stay below the normalized reference gap. This is
a scalar coefficient problem on the same `SEL2` record law, not an area-law
assumption.

The refinement in Definitions 4.3A.160BH.7--4.3A.160BH.10 and Theorem
4.3A.160BH.11 sharpens this statement: the boundary bulk term is harmless under
the natural rooted estimate `\zeta_{\rho,bd,j}^{SEL2}=O(g_{i(j)}^2)`, so the
remaining scalar number is

```math
\Xi_{\rho,int}^{SEL2}
=
\limsup_jS_j\zeta_{\rho,bulk,j}^{SEL2}.
```

### Definition 4.3A.160BH.7: Frozen Bulk Scalar Target For `SEL2`

Freeze the exact same-record bulk target as follows. On the standard `SEL2`
branch use:

1. the same cofinal row map `j -> i(j)`;
2. the same AF-area selector
   `H_j=g_{i(j)}^{-2}`, `L_j=\lfloor\sqrt{sH_j}\rfloor`, and
   `S_j=L_j^2`;
3. the same sheet/collar count `B_j^{sheet}=O(L_j)`;
4. the same axial-tree block/collar chart and the same interpolation
   `\mathcal R_j^{(m)}` from Definition 4.3A.160BH.1;
5. the same normalized central observable `\psi_\rho`.

Define the boundary and interior bulk scalar debits

```math
D_{\rho,bd,j}^{SEL2}
:=
B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2},
\qquad
D_{\rho,int,j}^{SEL2}
:=
S_j\zeta_{\rho,bulk,j}^{SEL2},
```

and the total bulk scalar debit

```math
D_{\rho,bulk,j}^{SEL2}
:=
D_{\rho,int,j}^{SEL2}
+D_{\rho,bd,j}^{SEL2}.
```

The bulk target is therefore exactly

```math
\limsup_jD_{\rho,bulk,j}^{SEL2}.
```

This is the only bulk quantity that may be used in the scalar coefficient
comparison. It is a pushed-forward finite-record scalar cumulant envelope; it
does not assert a continuum Yang-Mills measure and it does not assert a
Wilson-loop area law.

### Definition 4.3A.160BH.8: Boundary Root Estimate

The boundary-root audit `P20-SEL2-BDROOT(C_{\rho,bd})` asserts that for some
finite constant `C_{\rho,bd}`,

```math
\zeta_{\rho,bd,j}^{SEL2}
\le
C_{\rho,bd}g_{i(j)}^2
+o(g_{i(j)}^2)
```

on a cofinal row tail. The stronger zero-boundary audit
`P20-SEL2-BDROOT0` asserts simply

```math
B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2}\to0.
```

`P20-SEL2-BDROOT(C_{\rho,bd})` is the natural boundary estimate expected from
one finite collar layer: a rooted boundary cumulant has one local heat-kernel
scale factor, and there are only `O(L_j)` boundary roots.

### Definition 4.3A.160BH.8A: Actual `SEL2` Boundary/Collar Root Census

For the active normalized `SEL2` coefficient branch, a boundary root is a
sheet plaquette whose finite root battery intersects the declared
surface-collar layer. The actual boundary/collar root template is the following
same-record object.

1. **Root variables.** Use the same axial-tree logarithmic coordinates as in
   the interior census, but restrict the root battery to the finite
   boundary/collar stencil attached to the sheet plaquette. Exterior collar
   variables, endpoint/corner records, projective readout variables, and
   counterterm/scheme records are parameters unless they are explicitly in the
   local root stencil.
2. **Good collar event.** On the clean branch, the collar cutoff is flat on
   the root stencil and the small-field partition is identically one there.
   Derivatives of collar cutoffs or small-field partitions are supported only
   in the declared bad-collar/large-field transition event and are charged to
   `E_{\rho,col,j}^{SEL2}` or the large-field ledger, not to
   `\zeta_{\rho,bd,j}^{SEL2}`.
3. **Boundary action through order `g_i^2`.** After extracting the same
   quadratic Gaussian and heat-time tangent as in the interior root census, the
   good-collar boundary expansion through order `g_i^2` contains only finitely
   many local labels:

   ```text
   boundary restrictions of 4, 33, J2;
   finite missing-neighbor/Bianchi truncation labels bd2;
   finite off-sheet/collar replacement labels col2.
   ```

   The labels `bd2` and `col2` are boundary versions of the same local
   heat-kernel Taylor/Wick expansion. They are not new interior area labels;
   they occur only in the fixed-width collar stencil.
4. **No zeroth or first order boundary scalar term.** The boundary correction
   is a centered scalar cumulant of `\mathcal R_j-1` against the neutral
   pushed-forward record `\psi_\rho`. The zeroth-order term cancels by
   centering. The order-`g_i` terms are odd/root-cubic or one-leg
   Bianchi/off-sheet insertions and vanish after neutral scalar pushforward on
   the good collar event. Any order-`g_i` term created by a cutoff derivative
   is, by item 2, outside the boundary-root ledger.
5. **Finite template uniformity.** The number of boundary/collar root stencils
   is finite and independent of `j`; the stencil diameter and collar width are
   fixed by `SEL2`.

This is the boundary analogue of Definition 4.3A.160BH.37. It is again a
finite template statement, not a continuum measure hypothesis.

### Lemma 4.3A.160BH.8A.1: Boundary One-Leg Cancellation

On the clean good-collar branch of Definition 4.3A.160BH.8A, the
order-`g_i` boundary root contribution vanishes after pushforward to the
neutral scalar record.

Proof.

Work on one finite boundary/collar root stencil. After axial-tree gauge fixing
and extraction of the quadratic heat-kernel reference, the order-`g_i` terms
are finite sums of one Lie-algebra leg against the scalar test
`\psi_\rho\circ P_j` and the centered Bianchi/off-sheet root insertion.

The reference root law is centered and invariant under the local root
inversion/adjoint symmetry inherited from Haar measure and the central
heat-kernel density. The pushed-forward test is neutral: it is central and
depends only on the closed scalar record, not on an oriented open root leg.
Thus every one-leg term is odd under the centered root inversion while the
remaining factors are even. Its root integral is therefore zero.

Equivalently, before normal-coordinate expansion, the same statement is the
compact-group integration-by-parts identity applied to a left- or
right-invariant derivative of a central closed-record test. Since `SU(N)` has
traceless generators and no boundary in the compact group integral, a single
unpaired Lie-algebra leg has zero scalar coefficient.

The only possible order-`g_i` terms not covered by this symmetry are
cutoff-derivative terms. By Definition 4.3A.160BH.8A item 2 those are not in
the clean boundary-root ledger; they are charged to the collar or large-field
ledger. `square`

### Lemma 4.3A.160BH.8B: Rooted Boundary Cumulants Start At Order `g_i^2`

On the clean good-collar branch of Definition 4.3A.160BH.8A, each rooted
boundary scalar cumulant satisfies

```math
\left|\mathfrak K_{\rho,r,j}^{bd}\right|
\le
C_{\rho,bd,r}\,g_{i(j)}^2
+o(g_{i(j)}^2),
```

where `C_{\rho,bd,r}<\infty` depends only on the finite boundary/collar root
template, the representation `\rho`, and the fixed `SEL2` collar stencil.

Proof.

Work on one boundary/collar root stencil. The stencil is finite, so the
compact-group heat-kernel density, Haar/log-chart Jacobian, local
Bianchi/off-sheet insertion, and scalar readout have finite Taylor/Wick
expansions in the axial-tree root coordinates through order `g_i^2`.

The zeroth-order term is absent because the boundary root contribution is a
connected centered scalar coefficient of the telescopic correction
`\mathcal R_j-1`. Lemma 4.3A.160BH.8A.1 proves that all good-collar
order-`g_i` one-leg terms vanish after neutral scalar pushforward.
Cutoff-derivative terms are not hidden here: Definition 4.3A.160BH.8A item 2
assigns them to the collar or large-field ledger.

The first possible nonzero good-collar boundary labels are therefore the
finite second-order labels listed in item 3. For each label the scalar test is
bounded and smooth on a compact finite-dimensional group stencil, and the
block-conditioned covariance is finite on the same stencil. Hence each label
has a finite projected constant. Summing the finitely many label constants
gives `C_{\rho,bd,r}`, and the uniform Taylor remainder on the finite stencil
is `o(g_i^2)`. `square`

### Definition 4.3A.160BH.8C: Boundary Template Constant

Let `\mathcal T_{bd}^{SEL2}` be the finite set of good-collar boundary root
templates from Definition 4.3A.160BH.8A. Define

```math
C_{\rho,bd}^{SEL2}
:=
\max_{r\in\mathcal T_{bd}^{SEL2}} C_{\rho,bd,r}.
```

This maximum is finite because `\mathcal T_{bd}^{SEL2}` is finite.

If an unreduced branch keeps collar-cutoff transition terms in the same
boundary-root ledger, define the carried boundary/collar remainder

```math
E_{\rho,col,*}^{SEL2,bd}
:=
\limsup_j
\left(
B_j^{sheet}\zeta_{\rho,bd,j}^{trans}
+E_{\rho,col,j}^{SEL2}
\right),
```

where `\zeta_{\rho,bd,j}^{trans}` is the rooted scalar envelope of the
transition terms not assigned to the clean collar ledger. This quantity is a
finite usable debit only if the displayed limsup is finite; if it is infinite,
that unreduced collar branch fails the scalar-source test.

On the clean branch used below, `\zeta_{\rho,bd,j}^{trans}=0`, so no additional
boundary/collar constant is carried beyond the already declared
`E_{\rho,col,j}^{SEL2}`.

### Theorem 4.3A.160BH.8D: Verification Of `P20-SEL2-BDROOT`

On the actual strict reduced normalized `SEL2` branch with the clean
good-collar convention of Definition 4.3A.160BH.8A,

```math
P20\text{-}SEL2\text{-}BDROOT(C_{\rho,bd}^{SEL2})
```

holds.

Proof.

By Lemma 4.3A.160BH.8B, every boundary root template `r` has

```math
\left|\mathfrak K_{\rho,r,j}^{bd}\right|
\le
C_{\rho,bd,r}g_{i(j)}^2+o(g_{i(j)}^2).
```

Taking the maximum over the finite template set gives the uniform estimate

```math
\zeta_{\rho,bd,j}^{SEL2}
\le
C_{\rho,bd}^{SEL2}g_{i(j)}^2+o(g_{i(j)}^2).
```

This is exactly `P20-SEL2-BDROOT(C_{\rho,bd}^{SEL2})`. `square`

### Corollary 4.3A.160BH.8E: Boundary Contribution Vanishes On `SEL2`

Assume the standard `SEL2` sheet-time scaling audit of Definition
4.3A.160BA and the clean good-collar branch of Definition 4.3A.160BH.8A. Then

```math
B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2}\to0.
```

Equivalently, the boundary/collar-root part of the Bianchi/off-sheet scalar
bulk envelope is `o(1)`.

Proof.

Theorem 4.3A.160BH.8D gives

```math
\zeta_{\rho,bd,j}^{SEL2}
\le
C_{\rho,bd}^{SEL2}g_{i(j)}^2+o(g_{i(j)}^2).
```

By the standard `SEL2` sheet-time scaling,
`B_j^{sheet}=O(L_j)=O(H_j^{1/2})` and
`g_{i(j)}^2=H_j^{-1}`. Therefore

```math
B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2}
\le
O(H_j^{1/2})\left(C_{\rho,bd}^{SEL2}H_j^{-1}
+o(H_j^{-1})\right)
=o(1).
```

This proves `P20-SEL2-BDROOT0`. In particular the boundary contribution is
not merely `o(H_j)` relative to the area scale; it vanishes absolutely in the
scalar coefficient comparison. `square`

### Corollary 4.3A.160BH.8F: Honest Boundary/Collar Fork

The boundary/collar-root census has the following exact fork.

1. On the strict reduced clean-collar `SEL2` branch,

   ```math
   D_{\rho,bd,j}^{SEL2}
   =
   B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2}
   \to0.
   ```

   Thus the boundary Bianchi/off-sheet roots do not contribute to the final
   scalar coefficient defect.
2. On an unreduced branch with collar-transition terms retained in the
   boundary-root ledger, one must carry the explicit debit
   `E_{\rho,col,*}^{SEL2,bd}` from Definition 4.3A.160BH.8C. No proof below
   may set this debit to zero unless the transition envelope is moved back into
   the declared collar/large-field ledger or is separately shown to satisfy
   `B_j^{sheet}\zeta_{\rho,bd,j}^{trans}\to0`.

This closes `P20-SEL2-BDROOT` for the clean branch and gives the precise
carried constant for the nonclean branch.

### Lemma 4.3A.160BH.9: Boundary Bulk Term Is Harmless Under `BDROOT`

Assume the standard `SEL2` sheet-time scaling audit of Definition
4.3A.160BA. If `P20-SEL2-BDROOT(C_{\rho,bd})` holds, then
`P20-SEL2-BDROOT0` holds:

```math
D_{\rho,bd,j}^{SEL2}
=
B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2}
\to0.
```

Proof.

By Definition 4.3A.160BA and Theorem 4.3A.160BB,
`B_j^{sheet}=O(L_j)` and `L_j=O(H_j^{1/2})`, while
`g_{i(j)}^2=H_j^{-1}`. The boundary-root audit gives

```math
B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2}
\le
O(H_j^{1/2})\left(C_{\rho,bd}H_j^{-1}+o(H_j^{-1})\right)
=
O(H_j^{-1/2})+o(H_j^{-1/2})
\to0.
```

This proves the claim. `square`

### Corollary 4.3A.160BH.9A: Step-4 Actual Boundary/Collar Bianchi Closure

Assume:

1. `P20-SEL2-ACTROW`;
2. the standard `SEL2` sheet-time scaling audit;
3. the strict reduced clean-collar convention of Definition 4.3A.160BH.8A.

Then the actual boundary/collar Bianchi/off-sheet contribution to the scalar
coefficient defect vanishes:

```math
D_{\rho,bd,j}^{SEL2}
=
B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2}
\to0.
```

Thus Steps 1--4 reduce `P20-SEL2-4DCOEFF-CLOSE` to the interior
Bianchi/off-sheet scalar envelope alone:

```math
\delta_{\rho,4Dconv,j}^{SEL2}
\le
S_j\zeta_{\rho,bulk,j}^{SEL2}
+\epsilon_{\rho,1-4,j}^{SEL2},
\qquad
\epsilon_{\rho,1-4,j}^{SEL2}\to0,
```

on the strict branch. On a nonclean collar branch, replace the vanishing
`\epsilon_{\rho,1-4,j}^{SEL2}` contribution by the carried boundary/collar
debit `E_{\rho,col,*}^{SEL2,bd}` and the nonbulk debit `E_{\rho,nonbulk}`.

Proof.

The actual finite row and the five-term ledger are fixed by
`P20-SEL2-ACTROW` and Corollary 4.3A.160BH.1C. Step 3 removes the nonbulk
terms by Corollary 4.3A.160BH.2G. The clean-collar boundary census proves
`P20-SEL2-BDROOT(C_{\rho,bd}^{SEL2})` by Theorem 4.3A.160BH.8D, and Lemma
4.3A.160BH.9 turns this into
`B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2}\to0`. The only remaining term in the
bulk envelope of Lemma 4.3A.160BH.4 is therefore the interior area-rooted
quantity `S_j\zeta_{\rho,bulk,j}^{SEL2}`. The nonclean fallback is the
explicit fork of Corollary 4.3A.160BH.8F together with
`P20-SEL2-NONBULK-FIN`. `square`

### Definition 4.3A.160BH.10: Interior Bulk Cumulant Audits

The remaining interior scalar target is

```math
D_{\rho,int,j}^{SEL2}
=
S_j\zeta_{\rho,bulk,j}^{SEL2}.
```

Define the interior limsup value

```math
\Xi_{\rho,int}^{SEL2}
:=
\limsup_jD_{\rho,int,j}^{SEL2}
=
\limsup_jS_j\zeta_{\rho,bulk,j}^{SEL2}.
```

The zero-interior audit `P20-SEL2-INTBULK-ZERO` asserts

```math
S_j\zeta_{\rho,bulk,j}^{SEL2}\to0.
```

The finite-interior audit `P20-SEL2-INTBULK-FIN(\Xi_{\rho,int})` asserts

```math
\Xi_{\rho,int}^{SEL2}\le\Xi_{\rho,int}<\infty.
```

The first-order-cancellation audit, reserved for the next step, is

```text
P20-SEL2-INTBULK-FOC:
  zeta_{rho,bulk,j}^{SEL2}=o(H_j^{-1}).
```

Since `S_j\sim H_j`, `P20-SEL2-INTBULK-FOC` implies
`P20-SEL2-INTBULK-ZERO`. A mere estimate
`\zeta_{\rho,bulk,j}^{SEL2}=O(H_j^{-1})` proves only
`P20-SEL2-INTBULK-FIN`, with an order-one carried scalar debit.

### Theorem 4.3A.160BH.11: Steps 1--4 Reduce The Bulk Problem To Interior Cumulants

Assume:

1. `P20-SEL2-ACTROW`;
2. the three nonbulk terms in Lemma 4.3A.160BH.2 vanish;
3. the standard `SEL2` sheet-time scaling audit holds;
4. `P20-SEL2-BDROOT(C_{\rho,bd})` holds.

Then:

1. if `P20-SEL2-INTBULK-ZERO` holds, then
   `P20-SEL2-4DCOEFF-CLOSE(\epsilon_{\rho,j})` holds for some
   `\epsilon_{\rho,j}\to0`;
2. if `P20-SEL2-INTBULK-FIN(\Xi_{\rho,int})` holds, then

   ```math
   \delta_{\rho,*}^{SEL2}\le\Xi_{\rho,int}.
   ```

   Consequently, on the cofinal positive-sign branch, the normalized route
   still passes whenever

   ```math
   \Xi_{\rho,int}
   <
   1-\exp\{-s(1-\epsilon_A)(1-\chi)C_2(\rho)/2\}.
   ```

Proof.

By Lemma 4.3A.160BH.9, the boundary debit
`D_{\rho,bd,j}^{SEL2}` tends to zero. By hypothesis, the nonbulk scalar
corrections also tend to zero. Therefore Definition 4.3A.160BH.1 and Lemma
4.3A.160BH.4 give

```math
\delta_{\rho,4Dconv,j}^{SEL2}
\le
S_j\zeta_{\rho,bulk,j}^{SEL2}+o(1).
```

If the interior zero audit holds, the right-hand side tends to zero, proving
`P20-SEL2-4DCOEFF-CLOSE`.

If the finite-interior audit holds, taking limsup gives
`\delta_{\rho,*}^{SEL2}\le\Xi_{\rho,int}`. The finite-gap pass condition is then
exactly clause 2 of Theorem 4.3A.160BH.5 with this sharper bound inserted.
`square`

### Corollary 4.3A.160BH.12: Step-3 Status Before First-Order Cancellation

Steps 1--3 now leave one precise live problem:

```text
Evaluate Xi_{rho,int}^{SEL2}
= limsup_j S_j zeta_{rho,bulk,j}^{SEL2}.
```

The boundary Bianchi/off-sheet term is harmless on the clean good-collar
branch: Theorem 4.3A.160BH.8D proves `P20-SEL2-BDROOT`, and Corollary
4.3A.160BH.8E gives

```math
B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2}\to0.
```

On a nonclean collar branch, Corollary 4.3A.160BH.8F requires carrying the
explicit debit `E_{\rho,col,*}^{SEL2,bd}`. The next real question for the
clean branch is therefore the interior first-order coefficient:

```text
Does the O(H_j^{-1}) rooted interior Bianchi/off-sheet term cancel?
```

If yes, `INTBULK-ZERO` follows and the scalar convolution source closes. If no,
one must compute the finite constant `Xi_{rho,int}^{SEL2}` and compare it with
the normalized heat-kernel reference gap. This is exactly the step-4
first-order cancellation problem.

### Definition 4.3A.160BH.13: Grouped First-Order Interior Coefficient

First-order cancellation is a signed local statement. It cannot be tested after
splitting every local label and taking absolute values term by term. Therefore
freeze the following grouped scalar convention for the interior
Bianchi/off-sheet cumulant.

For each interior sheet root `r`, let
`\mathcal I_{\rho,int}^{(2)}` be the finite list of second-order local labels
from the Paper-16 `HK-SF-YM2` ledger that actually touch the root and at least
one Bianchi cube or off-sheet plaquette. This list is a sublist of

```text
{4, 33, J2, gf2, cov2, rec2, norm2},
```

after time-tangent and pure-normalization labels have been removed. The grouped
interior scalar expansion is

```math
\mathfrak K_{\rho,r,j}^{bulk}
=
g_{i(j)}^2
\Gamma_{\rho,r}^{(2),bulk}
+R_{\rho,r,j}^{bulk},
```

with

```math
\sup_{r\in int}|R_{\rho,r,j}^{bulk}|=o(g_{i(j)}^2).
```

Here `\mathfrak K_{\rho,r,j}^{bulk}` is the signed rooted scalar cumulant after
all local Bianchi/off-sheet labels at the same root have been grouped on the
same pushed-forward scalar record. Define

```math
\Gamma_{\rho,int}^{SEL2}
:=
\sup_{r\in int}
\left|
\Gamma_{\rho,r}^{(2),bulk}
\right|.
```

For the cancellation and interior audits below, `\zeta_{\rho,bulk,j}^{SEL2}`
is understood as the corresponding grouped rooted envelope: take the absolute
value after forming `\mathfrak K_{\rho,r,j}^{bulk}` at each root and after
including the uniformly smaller higher-order remainder. The earlier ungrouped
termwise absolute envelope remains a valid upper bound, but it cannot witness
signed first-order cancellation.

The first-order cancellation audit `P20-SEL2-INTBULK-FOC` asserts

```math
\Gamma_{\rho,int}^{SEL2}=0
```

with the displayed uniform `o(g_i^2)` remainder. The finite grouped constant
audit `P20-SEL2-INTBULK-GAMMA(\Gamma_{\rho,int})` asserts

```math
\Gamma_{\rho,int}^{SEL2}\le\Gamma_{\rho,int}<\infty.
```

If one does not compute the signed grouped coefficients, a safe but usually
larger upper bound is

```math
\Gamma_{\rho,int}^{abs}
:=
\sum_{a\in\mathcal I_{\rho,int}^{(2)}} C_{\rho,int,a}^{SEL2},
```

where `C_{\rho,int,a}^{SEL2}` is the absolute local projected constant of label
`a` against `\psi_\rho\circ P_j`. This absolute bound cannot prove
first-order cancellation; it can only feed the finite-gap comparison.

### Lemma 4.3A.160BH.14: What `HK-SF-YM2` Proves And Does Not Prove

On the active `SEL2` interior bulk record, the existing `HK-SF-YM2` source
proves the following and no more:

1. all order-`g_i` odd/cubic contributions vanish after neutral scalar
   pushforward;
2. the order-`g_i^2` time-tangent component is absorbed into the declared
   heat-kernel time coordinate;
3. every remaining nonabsorbed local label begins at order `g_i^2` and belongs
   to the finite second-order list.

Consequently the current source base proves

```math
\zeta_{\rho,bulk,j}^{SEL2}=O(H_j^{-1})
```

provided the grouped interior constants are finite, but it does not prove

```math
\zeta_{\rho,bulk,j}^{SEL2}=o(H_j^{-1})
```

unless the additional signed cancellation audit
`P20-SEL2-INTBULK-FOC` is verified.

Proof.

Items 1--3 are exactly the `HK-SF-YM2` clauses imported in Paper 16: odd
order-`g_i` labels vanish, time-tangent quadratic labels are absorbed, and the
remaining nonabsorbed labels are second order. Since `H_j=g_{i(j)}^{-2}`, a
second-order rooted local label has size `O(g_{i(j)}^2)=O(H_j^{-1})`.

However, `HK-SF-YM2` only says that the remaining second-order label list is
finite and starts at order `g_i^2`. It does not assert that the signed sum of
the Bianchi/off-sheet labels in Definition 4.3A.160BH.13 vanishes for the
specific observable `\psi_\rho\circ P_j`. Therefore it supplies the finite
order-one route, not the zero route. `square`

### Theorem 4.3A.160BH.15: First-Order Cancellation Criterion

Assume:

1. the hypotheses of Theorem 4.3A.160BH.11;
2. the grouped scalar expansion of Definition 4.3A.160BH.13;
3. `P20-SEL2-INTBULK-FOC`.

Then

```math
\zeta_{\rho,bulk,j}^{SEL2}=o(H_j^{-1}),
```

so `P20-SEL2-INTBULK-ZERO` holds. Consequently
`P20-SEL2-4DCOEFF-CLOSE(\epsilon_{\rho,j})` holds for some
`\epsilon_{\rho,j}\to0`, and the normalized route closes by Theorem
4.3A.160BI.

Proof.

By the grouped expansion,

```math
\mathfrak K_{\rho,r,j}^{bulk}
=
g_{i(j)}^2\Gamma_{\rho,r}^{(2),bulk}
+R_{\rho,r,j}^{bulk}.
```

The first-order cancellation audit says
`\Gamma_{\rho,r}^{(2),bulk}=0` for every interior root. The remainder is
uniformly `o(g_i^2)`, hence the rooted interior envelope is
`o(g_i^2)=o(H_j^{-1})`. Since `S_j\sim H_j`, this gives
`S_j\zeta_{\rho,bulk,j}^{SEL2}\to0`. Theorem 4.3A.160BH.11 then gives
`P20-SEL2-4DCOEFF-CLOSE`, and Theorem 4.3A.160BI closes the normalized route.
`square`

### Theorem 4.3A.160BH.16: Finite Constant And Gap Comparison

Assume the hypotheses of Theorem 4.3A.160BH.11 and
`P20-SEL2-INTBULK-GAMMA(\Gamma_{\rho,int})`. Then

```math
\Xi_{\rho,int}^{SEL2}
\le
s(1+\epsilon_A)\Gamma_{\rho,int}.
```

In particular, on the cofinal positive-sign branch, the normalized route
passes by the finite-gap test if

```math
s(1+\epsilon_A)\Gamma_{\rho,int}
<
1-\exp\{-s(1-\epsilon_A)(1-\chi)C_2(\rho)/2\}.
```

If the signed grouped coefficient is not evaluated but the absolute local
constants are, the sufficient but weaker test is

```math
s(1+\epsilon_A)\Gamma_{\rho,int}^{abs}
<
1-\exp\{-s(1-\epsilon_A)(1-\chi)C_2(\rho)/2\}.
```

Proof.

The grouped gamma audit gives

```math
\zeta_{\rho,bulk,j}^{SEL2}
\le
\Gamma_{\rho,int}g_{i(j)}^2+o(g_{i(j)}^2).
```

Since `g_{i(j)}^2=H_j^{-1}` and `S_j/H_j\le s(1+\epsilon_A)` on the standard
AF-area selector,

```math
\limsup_jS_j\zeta_{\rho,bulk,j}^{SEL2}
\le
s(1+\epsilon_A)\Gamma_{\rho,int}.
```

The finite-gap pass condition is then Theorem 4.3A.160BH.11 followed by
Theorem 4.3A.160BH.5. The absolute-constant version follows from
`\Gamma_{\rho,int}\le\Gamma_{\rho,int}^{abs}`. `square`

### Corollary 4.3A.160BH.17: Current Decision On Interior First Order

The current Paper-16/Paper-19/Paper-20 source base does not prove
`P20-SEL2-INTBULK-FOC`. It proves the structural prerequisites for a finite
second-order calculation:

```text
odd order-g_i cancellation
+ time-tangent absorption
+ finite second-order label list.
```

Thus the interior bulk target is now reduced to the finite signed coefficient

```math
\Gamma_{\rho,int}^{SEL2}
=
\sup_{r\in int}
\left|
\sum_{a\in\mathcal I_{\rho,int}^{(2)}}
\Gamma_{\rho,r,a}^{(2),bulk}
\right|.
```

There are two honest exits:

1. prove the signed sum is zero for every interior root; then
   `INTBULK-ZERO` and `4DCOEFF-CLOSE` follow;
2. compute or sharply bound `\Gamma_{\rho,int}^{SEL2}` and test

   ```math
   s(1+\epsilon_A)\Gamma_{\rho,int}^{SEL2}
   <
   1-\exp\{-s(1-\epsilon_A)(1-\chi)C_2(\rho)/2\}.
   ```

Without one of these two finite local evaluations, Paper 20 cannot honestly
declare the normalized `SEL2` coefficient route closed. This is not an area-law
gap; it is the remaining same-record local second-order scalar coefficient
calculation.

### Definition 4.3A.160BH.18: Active Normalized `SEL2` Branch Freeze

For the rest of the `SEL2` coefficient analysis, the active branch is the
normalized same-record branch, not the raw coefficient branch. Concretely:

1. the raw branch remains parked by `P20-SEL2-RAWBTIME-PARK`;
2. the surface-normalization audit has reduced the dimension surcharge to the
   active reduced-support value

   ```math
   \Delta_{dim}^{SEL2}=0;
   ```

3. the coefficient that enters the leading surface sheet is the normalized
   scalar central coefficient

   ```math
   \widetilde a_{\rho,j}^{SEL2}:=
   {a_{\rho,j}^{SEL2}\over d_\rho};
   ```

4. the only remaining comparison source is the scalar four-dimensional defect
   of Definition 4.3A.160BH, or its finite-gap replacement in Theorem
   4.3A.160BH.5;
5. all terms below are evaluated on the same finite pushed-forward `SEL2`
   scalar record law used by `P20-SEL2-TR-COMMON`, `NORM-SURF`, and
   `4DCOEFF`.

This branch freeze is a bookkeeping theorem, not a new physical assumption:
proof-coordinate data such as axial-tree charts, covariance coordinates, and
local vertex labels are allowed only through their pushed-forward scalar
record coefficients. In particular, the next calculation is not a continuum
Yang-Mills measure construction and not an area-law input. It is the finite
rooted coefficient calculation for `\Gamma_{\rho,int}^{SEL2}`.

### Definition 4.3A.160BH.19: Seven-Label Interior `Gamma` Worksheet

Fix an interior sheet root `r` on the active normalized `SEL2` branch. Let
`\mathcal B_{r,j}^{bulk}` denote the signed, centered local
Bianchi/off-sheet correction at that root after the convolution sheet
reference has been subtracted. Let `V_{a,j}` denote the pushed-forward
Paper-16/Paper-19 second-order local vertex label, with

```math
a\in I_{\rho,int}^{(2)}
\subseteq
\{4,33,J2,gf2,cov2,rec2,norm2\}.
```

After odd terms have vanished and the time tangent has been absorbed, define
the signed rooted coefficient by the cofinal limit, when it exists,

```math
\Gamma_{\rho,r,a}^{(2),bulk}
:=
\lim_{j\to\infty}
g_{i(j)}^{-2}
\,
\left\langle
\psi_\rho\circ P_j,\,
\mathcal B_{r,j}^{bulk}V_{a,j}
\right\rangle_{c,j}^{SEL2}.
```

Here `\langle\cdot,\cdot\rangle_{c,j}^{SEL2}` is the connected scalar
coefficient in the frozen pushed-forward `SEL2` record law. If the limit has
not been proved, replace it by the corresponding cofinal limsup coefficient;
the exact-cancellation audit below requires the signed limits, while the
finite-gap audit may use signed limsups or absolute constants.

The seven entries are:

```math
\Gamma_{\rho,r,4}^{(2),bulk}
\quad\text{quartic Yang--Mills insertion,}
```

```math
\Gamma_{\rho,r,33}^{(2),bulk}
\quad\text{connected double-cubic insertion,}
```

```math
\Gamma_{\rho,r,J2}^{(2),bulk}
\quad\text{quadratic Haar/log-chart Jacobian insertion,}
```

```math
\Gamma_{\rho,r,gf2}^{(2),bulk}
\quad\text{quadratic gauge-slice insertion,}
```

```math
\Gamma_{\rho,r,cov2}^{(2),bulk}
\quad\text{block-conditioned covariance-drift insertion,}
```

```math
\Gamma_{\rho,r,rec2}^{(2),bulk}
\quad\text{second-order scalar record/readout insertion,}
```

```math
\Gamma_{\rho,r,norm2}^{(2),bulk}
\quad\text{connected normalization subtraction.}
```

The worksheet value is the signed sum

```math
\Gamma_{\rho,r}^{YM2,bulk}
:=
\Gamma_{\rho,r,4}^{(2),bulk}
+\Gamma_{\rho,r,33}^{(2),bulk}
+\Gamma_{\rho,r,J2}^{(2),bulk}
+\Gamma_{\rho,r,gf2}^{(2),bulk}
+\Gamma_{\rho,r,cov2}^{(2),bulk}
+\Gamma_{\rho,r,rec2}^{(2),bulk}
+\Gamma_{\rho,r,norm2}^{(2),bulk},
```

and

```math
\Gamma_{\rho,int}^{SEL2}
=
\sup_{r\in int}
\left|
\Gamma_{\rho,r}^{YM2,bulk}
\right|.
```

The absolute fallback worksheet is

```math
\Gamma_{\rho,int}^{abs,SEL2}
:=
\sup_{r\in int}
\sum_{a\in I_{\rho,int}^{(2)}}
\left|
\Gamma_{\rho,r,a}^{(2),bulk}
\right|.
```

The strict ordering is important. Cancellation must be tested on
`\Gamma_{\rho,r}^{YM2,bulk}` before absolute values are taken. The absolute
worksheet is only a finite-gap fallback.

### Lemma 4.3A.160BH.20: Immediate Same-Record Reductions Of The Worksheet

On the active normalized `SEL2` branch, the seven-label worksheet reduces as
follows.

1. If the chart is the strict axial-tree chart with unit gauge-slice
   determinant, then

   ```math
   \Gamma_{\rho,r,gf2}^{(2),bulk}=0.
   ```

2. If the scalar record is the minimal normalized coefficient readout and the
   time tangent has been absorbed as in `HK-SF-YM2`, then

   ```math
   \Gamma_{\rho,r,rec2}^{(2),bulk}=0.
   ```

3. If connected/cumulant normalization is used for the pushed-forward scalar
   law, then

   ```math
   \Gamma_{\rho,r,norm2}^{(2),bulk}=0.
   ```

4. If the reference Gaussian covariance is chosen to be the exact
   block-conditioned covariance for the tested root, then

   ```math
   \Gamma_{\rho,r,cov2}^{(2),bulk}=0.
   ```

   Otherwise it remains as a finite carried coefficient bounded by a local
   covariance-drift constant:

   ```math
   |\Gamma_{\rho,r,cov2}^{(2),bulk}|
   \le
   M_{\rho,cov}^{int}K_{\rho,cov}^{int}.
   ```

Consequently, on the strict axial-tree, exact-covariance,
connected/cumulant, minimal-readout subbranch, exact first-order cancellation
is equivalent to the finite universal identity

```math
\Gamma_{\rho,r,4}^{(2),bulk}
+\Gamma_{\rho,r,33}^{(2),bulk}
+\Gamma_{\rho,r,J2}^{(2),bulk}
=0
\qquad(r\in int).
```

Proof.

The first three reductions are the same finite pushed-forward reductions used
in Paper 19's `SEL_0` small-field worksheet and in Paper 16's strict
`HK-SF-YM2` minimal branch, now applied to the active `SEL2` scalar record:
strict axial-tree removes the gauge-slice insertion, minimal coefficient
readout makes the record drift time-tangent after absorption, and connected
normalization removes the local denominator subtraction. These are statements
about the pushed-forward scalar record coefficients, not about a different
gauge-fixed ontology.

For `cov2`, exact covariance matching makes the covariance-drift insertion
zero by definition. Without that choice, the same finite operator-norm
argument as in the `SEL_0` worksheet gives the displayed bound. Substituting
the four reductions into Definition 4.3A.160BH.19 gives the final identity.
`square`

### Definition 4.3A.160BH.21: Interior Universal Cancellation Audit

The exact universal cancellation audit
`P20-SEL2-INTBULK-YM2-CANCEL` asserts that, on the strict reduced subbranch of
Lemma 4.3A.160BH.20,

```math
\Gamma_{\rho,r,4}^{(2),bulk}
+\Gamma_{\rho,r,33}^{(2),bulk}
+\Gamma_{\rho,r,J2}^{(2),bulk}
=0
\qquad
\text{for every interior root }r.
```

The finite carried version `P20-SEL2-INTBULK-YM2-GAP(\Gamma_{\rho,YM2})`
asserts

```math
\sup_{r\in int}
\left|
\Gamma_{\rho,r,4}^{(2),bulk}
+\Gamma_{\rho,r,33}^{(2),bulk}
+\Gamma_{\rho,r,J2}^{(2),bulk}
\right|
\le
\Gamma_{\rho,YM2}<\infty.
```

If exact covariance matching is not used, replace the right-hand side by
`\Gamma_{\rho,YM2}+M_{\rho,cov}^{int}K_{\rho,cov}^{int}`.

### Theorem 4.3A.160BH.22: Exact Cancellation Attempt And Current Verdict

On the active normalized `SEL2` branch:

1. `P20-SEL2-INTBULK-YM2-CANCEL` implies
   `P20-SEL2-INTBULK-FOC`.
2. `P20-SEL2-INTBULK-YM2-GAP(\Gamma_{\rho,YM2})` implies
   `P20-SEL2-INTBULK-GAMMA(\Gamma_{\rho,YM2})` on the strict exact-covariance
   subbranch, and

   ```math
   P20\text{-}SEL2\text{-}INTBULK\text{-}GAMMA
   \left(
   \Gamma_{\rho,YM2}+M_{\rho,cov}^{int}K_{\rho,cov}^{int}
   \right)
   ```

   on the non-exact-covariance subbranch.
3. The current Paper-16/Paper-19/Paper-20 source base does not prove
   `P20-SEL2-INTBULK-YM2-CANCEL`. It proves the reductions of Lemma
   4.3A.160BH.20 and reduces the cancellation question to the displayed
   three-term universal finite identity.

Proof.

For clause 1, Lemma 4.3A.160BH.20 sets the optional worksheet entries to zero
on the strict reduced subbranch. The universal cancellation audit then gives
`\Gamma_{\rho,r}^{YM2,bulk}=0` for every interior root, hence
`\Gamma_{\rho,int}^{SEL2}=0`, which is precisely
`P20-SEL2-INTBULK-FOC`.

For clause 2, the same reduction leaves only the displayed three universal
terms, plus the covariance-drift term if exact covariance matching is not
used. Taking the supremum over roots gives the stated `Gamma` audit.

For clause 3, `HK-SF-YM2` supplies odd cancellation, time-tangent absorption,
and the finite second-order label list. The `SEL_0` worksheet supplies the
same-record zero reductions for `gf2`, `rec2`, and `norm2` under the strict
minimal conventions, and the covariance term is zero only under exact
same-root covariance matching. None of these source statements computes the
signed Wick/root contraction

```math
\Gamma_{\rho,r,4}^{(2),bulk}
+\Gamma_{\rho,r,33}^{(2),bulk}
+\Gamma_{\rho,r,J2}^{(2),bulk}.
```

Therefore exact first-order cancellation has not been proved. The honest
output of steps 1--3 is a finite same-record decision problem: either prove
the three-term universal identity above, or carry
`\Gamma_{\rho,YM2}` into the finite-gap scalar comparison of Theorem
4.3A.160BH.16. `square`

### Definition 4.3A.160BH.23: Wick Evaluation Of The Three Universal Terms

Fix an interior root `r` on the strict reduced normalized `SEL2` subbranch.
Let `\gamma_{r,j}` be the centered block-conditioned Gaussian reference law in
the local axial-tree coordinates, and let

```math
F_{\rho,r,j}:=\psi_\rho\circ P_j
```

be the selected scalar record observable restricted to the root battery. Let
`\mathcal B_{r,j}^{bulk}` be the centered bulk Bianchi/off-sheet insertion
from Definition 4.3A.160BH.19. Write the universal local expansion through
order `g_i^2` as

```math
\mathcal V_{r,j}^{YM2}
:=
V_{4,r,j}
 + V_{33,r,j}
 + V_{J2,r,j},
```

where `V_{33}` is the connected second cumulant of the cubic insertion,
including its `1/2` cumulant factor and its sign from the exponential
expansion. Define the finite Wick functional

```math
\mathsf W_{\rho,r,j}^{YM2}
:=
g_{i(j)}^{-2}
\left\langle
F_{\rho,r,j},\,
\mathcal B_{r,j}^{bulk}
\mathcal V_{r,j}^{YM2}
\right\rangle_{c,j}^{SEL2}.
```

Equivalently, by the finite-dimensional Wick formula, there is a finite
differential operator `\mathcal D_{r,j}^{YM2}` with coefficients determined by
the same covariance, Taylor, and Haar/Jacobian data such that

```math
\mathsf W_{\rho,r,j}^{YM2}
=
\left[
\mathcal D_{r,j}^{YM2}
\left(
F_{\rho,r,j}\mathcal B_{r,j}^{bulk}
\right)
\right]_{A=0}.
```

The evaluated three-term coefficient is

```math
\Gamma_{\rho,r}^{YM2,bulk}
=
\lim_j \mathsf W_{\rho,r,j}^{YM2}
```

when the signed limit exists, and otherwise is represented by its cofinal
limsup interval. In expanded notation,

```math
\Gamma_{\rho,r}^{YM2,bulk}
=
\Gamma_{\rho,r,4}^{(2),bulk}
+\Gamma_{\rho,r,33}^{(2),bulk}
+\Gamma_{\rho,r,J2}^{(2),bulk}.
```

Thus the three-term local identity is no longer an informal cancellation
claim. It is the finite Wick statement

```math
\left[
\mathcal D_{r}^{YM2}
\left(
F_{\rho,r}\mathcal B_{r}^{bulk}
\right)
\right]_{A=0}=0
```

on every interior root after the heat-time tangent has been removed.

### Definition 4.3A.160BH.24: Heat-Time Split And Local Generator Mismatch

Let `\Phi_{\rho,r}` be the local heat-time tangent for the normalized scalar
coefficient and let `\ell_{\rho,r}^{time}` be the finite dual time functional
used in the time-tangent absorption. Decompose the Wick operator of Definition
4.3A.160BH.23 into its time-tangent and transverse parts on the finite local
test space generated by `F_{\rho,r}\mathcal B_r^{bulk}`:

```math
\mathcal D_{r}^{YM2}
=
\alpha_{\rho,r}^{YM2}\mathcal L_{\rho,r}^{HK}
+\mathcal R_{\rho,r}^{YM2,\perp}.
```

Here `\mathcal L_{\rho,r}^{HK}` is the local heat-kernel coefficient
generator, normalized so that its action is precisely the time displacement
already absorbed in the declared convolution time, and
`\mathcal R_{\rho,r}^{YM2,\perp}` has zero time component:

```math
\ell_{\rho,r}^{time}
\left(
\mathcal R_{\rho,r}^{YM2,\perp}
\right)=0.
```

Define the local generator mismatch

```math
\Xi_{\rho,r}^{YM2}
:=
\left[
\mathcal R_{\rho,r}^{YM2,\perp}
\left(
F_{\rho,r}\mathcal B_{r}^{bulk}
\right)
\right]_{A=0}.
```

The finite root supremum is

```math
\Xi_{\rho,YM2}^{SEL2}
:=
\sup_{r\in int}
|\Xi_{\rho,r}^{YM2}|.
```

The local generator matching audit
`P20-SEL2-INTBULK-GENMATCH` asserts

```math
\Xi_{\rho,YM2}^{SEL2}=0.
```

The finite mismatch audit `P20-SEL2-INTBULK-GENBOUND(\Xi_{\rho,YM2})` asserts

```math
\Xi_{\rho,YM2}^{SEL2}\le \Xi_{\rho,YM2}<\infty.
```

This is the correct formulation of the hoped-for cancellation: quartic,
double-cubic, and Haar/log-Jacobian terms may cancel only after their common
heat-time tangent is removed, and only on the same pushed-forward scalar
record.

### Lemma 4.3A.160BH.25: Evaluation Of The Three-Term Identity

On the strict reduced normalized `SEL2` subbranch,

```math
\Gamma_{\rho,r,4}^{(2),bulk}
+\Gamma_{\rho,r,33}^{(2),bulk}
+\Gamma_{\rho,r,J2}^{(2),bulk}
=
\Xi_{\rho,r}^{YM2}.
```

Consequently:

1. `P20-SEL2-INTBULK-GENMATCH` implies
   `P20-SEL2-INTBULK-YM2-CANCEL`;
2. `P20-SEL2-INTBULK-GENBOUND(\Xi_{\rho,YM2})` implies
   `P20-SEL2-INTBULK-YM2-GAP(\Xi_{\rho,YM2})`;
3. without `GENMATCH`, the absolute same-record source bound is

   ```math
   \Xi_{\rho,YM2}^{SEL2}
   \le
   24M_{\rho,4}^{int}C_4C_{\rm cov}^2
   +18M_{\rho,33}^{int}C_3^2C_{\rm cov}^3
   +M_{\rho,J}^{int}C_JC_{\rm cov}.
   ```

Proof.

Definition 4.3A.160BH.23 rewrites the signed sum of the three universal local
labels as the Wick operator `\mathcal D_r^{YM2}` applied to the finite test
`F_{\rho,r}\mathcal B_r^{bulk}`. Definition 4.3A.160BH.24 then splits this
operator into the heat-time generator and a transverse remainder. The
heat-time part is exactly the component already absorbed into the declared
convolution time by the `HK-SF-YM2` time-tangent clause, so it does not
contribute to the transverse scalar defect. The surviving three-term
coefficient is therefore the local generator mismatch `\Xi_{\rho,r}^{YM2}`.

Clauses 1 and 2 are immediate by taking the supremum over roots. For clause
3, apply the Paper-11/Paper-16 local Wick bounds to the same pushed-forward
root observable. One quartic insertion is bounded by
`24C_4C_{\rm cov}^2`; the connected double-cubic cumulant is bounded by
`18C_3^2C_{\rm cov}^3`; and the quadratic Haar/log-Jacobian insertion is
bounded by `C_JC_{\rm cov}`. The finite constants
`M_{\rho,4}^{int}`, `M_{\rho,33}^{int}`, and `M_{\rho,J}^{int}` are the
operator norms of the same scalar root projection against
`F_{\rho,r}\mathcal B_r^{bulk}`. `square`

### Corollary 4.3A.160BH.26: Honest Verdict On The Three-Term Evaluation

The three-term local identity has been evaluated to the local generator
mismatch:

```math
\Gamma_{\rho,r,4}^{(2),bulk}
+\Gamma_{\rho,r,33}^{(2),bulk}
+\Gamma_{\rho,r,J2}^{(2),bulk}
=
\Xi_{\rho,r}^{YM2}.
```

The current source base does not prove
`P20-SEL2-INTBULK-GENMATCH`, because Papers 11 and 16 provide uniform Wick
source bounds for `4`, `33`, and `J2`, not the signed rootwise equality of the
second-order local Yang--Mills/Haar operator with the heat-kernel generator on
the Bianchi/off-sheet scalar test.

Thus the exact cancellation route is not closed. The branch has two remaining
honest exits:

1. prove the local generator matching identity

   ```math
   \mathcal R_{\rho,r}^{YM2,\perp}
   \left(F_{\rho,r}\mathcal B_r^{bulk}\right)(0)=0
   \quad(r\in int);
   ```

2. carry the finite constant

   ```math
   \Xi_{\rho,YM2}^{SEL2}
   \le
   24M_{\rho,4}^{int}C_4C_{\rm cov}^2
   +18M_{\rho,33}^{int}C_3^2C_{\rm cov}^3
   +M_{\rho,J}^{int}C_JC_{\rm cov}
   ```

   plus `M_{\rho,cov}^{int}K_{\rho,cov}^{int}` if exact covariance matching
   is not used, and test it in the finite-gap inequality of Theorem
   4.3A.160BH.16.

This is a genuine finite local calculation. It is not a hidden area-law
assumption, but it is also not proved by the existing absolute vertex ledger.
The next definition gives the noncircular route to proving it: the three-term
operator must be recognized as the finite heat-kernel Schwinger-Dyson
divergence after the time tangent is removed.

### Definition 4.3A.160BH.27: Rootwise Heat-Kernel Schwinger-Dyson Ledger

The finite route to `GENMATCH` is not to estimate the three universal terms
separately. It is to identify their signed sum as a finite heat-kernel
Schwinger-Dyson divergence before any absolute values are taken.

`P20-SEL2-ROOT-HKSD` holds when, for every interior root `r`, the following
same-record finite identities hold on the root battery.

1. **Exact group-level identity before chart truncation.** The root variables
   are evaluated under the finite heat-kernel row on the compact group, with
   Haar measure and the declared heat-kernel plaquette density. For every
   smooth finite cylinder test `G` in the root battery,

   ```math
   \int
   \left(
   {1\over2}\Delta_rG
   +{1\over2}\nabla_rG\cdot\nabla_r\log K_{t_i}
   \right)
   K_{t_i}\,dHaar_r
   =0.
   ```

   Here `\Delta_r` is the root Laplace-Beltrami operator in the fixed
   bi-invariant metric, and the displayed identity is simply integration by
   parts on the compact group.

2. **Second-order normal-coordinate expansion.** In the axial-tree chart used
   by the `SEL2` small-field ledger, the second-order expansion of the
   group-level identity has the form

   ```math
   \mathcal D_r^{YM2}
   =
   \alpha_{\rho,r}^{YM2}\mathcal L_{\rho,r}^{HK}
   +{\rm div}_{\gamma_r}{\mathcal Q}_{\rho,r}
   ```

   on the finite test space generated by
   `F_{\rho,r}\mathcal B_r^{bulk}`, modulo terms already assigned to the
   collar, boundary, counterterm, projective/readout, or large-field ledgers.
   The three non-time entries of `\mathcal D_r^{YM2}` are exactly the
   quartic, connected double-cubic, and Haar/log-Jacobian labels
   `{4,33,J2}`.

3. **No interior boundary residue.** The divergence term has zero scalar
   connected coefficient against the rooted bulk test:

   ```math
   \left[
   {\rm div}_{\gamma_r}{\mathcal Q}_{\rho,r}
   \left(F_{\rho,r}\mathcal B_r^{bulk}\right)
   \right]_{A=0}=0.
   ```

   Any cutoff, collar, or small-field partition boundary term is not hidden in
   this clause; it must already be charged to the nonbulk ledgers or to the
   boundary-root term.

This ledger is finite and local. It is a statement about the pushed-forward
root record law, not about continuum Yang-Mills existence and not about an
area law.

### Lemma 4.3A.160BH.28: Divergence Form Kills The Root Mismatch

Assume `P20-SEL2-ROOT-HKSD` at an interior root `r`. Then

```math
\Xi_{\rho,r}^{YM2}=0.
```

Proof.

By Definition 4.3A.160BH.27, the second-order Wick operator on the root test
splits as

```math
\mathcal D_r^{YM2}
=
\alpha_{\rho,r}^{YM2}\mathcal L_{\rho,r}^{HK}
+{\rm div}_{\gamma_r}{\mathcal Q}_{\rho,r}.
```

The first term is the local heat-kernel time tangent. It is precisely the
part removed in Definition 4.3A.160BH.24 when
`\mathcal R_{\rho,r}^{YM2,\perp}` is formed. The remaining term is the
Gaussian/heat-kernel divergence. Clause 3 of `P20-SEL2-ROOT-HKSD` says its
scalar connected coefficient against
`F_{\rho,r}\mathcal B_r^{bulk}` is zero, with all boundary/cutoff residues
paid outside the interior bulk ledger. Therefore

```math
\left[
\mathcal R_{\rho,r}^{YM2,\perp}
\left(F_{\rho,r}\mathcal B_r^{bulk}\right)
\right]_{A=0}=0,
```

which is the definition of `\Xi_{\rho,r}^{YM2}=0`. `square`

### Theorem 4.3A.160BH.29: Rootwise `GENMATCH` From `ROOT-HKSD`

If `P20-SEL2-ROOT-HKSD` holds for every interior root of the active normalized
`SEL2` sheet, then

```math
P20\text{-}SEL2\text{-}INTBULK\text{-}GENMATCH
```

holds. Consequently,

```math
P20\text{-}SEL2\text{-}INTBULK\text{-}YM2\text{-}CANCEL
```

and, on the strict exact-covariance reduced branch,

```math
P20\text{-}SEL2\text{-}INTBULK\text{-}FOC
```

hold.

Proof.

Lemma 4.3A.160BH.28 gives `\Xi_{\rho,r}^{YM2}=0` for each interior root.
Taking the supremum over interior roots gives
`\Xi_{\rho,YM2}^{SEL2}=0`, which is exactly `GENMATCH`. Lemma
4.3A.160BH.25 turns `GENMATCH` into `YM2-CANCEL`, and Theorem
4.3A.160BH.22 turns `YM2-CANCEL` into `INTBULK-FOC` on the strict reduced
subbranch. `square`

### Corollary 4.3A.160BH.30: How To Prove `GENMATCH` Rootwise

The rootwise proof strategy is now sharp:

```text
finite compact-group heat-kernel integration by parts
-> second-order axial-tree normal-coordinate expansion
-> heat-time tangent plus divergence
-> no interior divergence residue
-> GENMATCH.
```

This is the first plausible noncircular proof route for the three-term
identity. It uses only finite heat-kernel rows and local pushed-forward scalar
records. It does not use a continuum Yang-Mills measure and does not assume
confinement.

The remaining work is also precise. One must verify clause 2 of
`P20-SEL2-ROOT-HKSD` on the actual `SEL2` axial-tree root template: the signed
normal-coordinate expansion of the compact-group Schwinger-Dyson identity must
produce exactly the `{4,33,J2}` Wick operator, with every cutoff/collar
residue charged outside the interior bulk ledger. If that finite template
calculation is completed, `GENMATCH` is proved rootwise and the interior
bulk obstruction disappears.

### Lemma 4.3A.160BH.31: Compact-Group Root Integration By Parts

For each finite `SEL2` interior root battery, clause 1 of
`P20-SEL2-ROOT-HKSD` holds.

Proof.

The root variables live on a finite product of compact Lie groups with
normalized Haar measure. Let `K_{t_i}` denote the product of the heat-kernel
densities assigned to the root plaquette variables in the fixed bi-invariant
metric, after all variables outside the root battery are held fixed. For every
smooth finite cylinder test `G`, left and right invariance of Haar measure and
compactness give

```math
0
=
\int {\rm div}_r\!\left(K_{t_i}\nabla_rG\right)dHaar_r.
```

Expanding the divergence gives

```math
0
=
\int
\left(
\Delta_rG+\nabla_rG\cdot\nabla_r\log K_{t_i}
\right)
K_{t_i}\,dHaar_r.
```

Multiplying by `1/2` gives the clause in Definition 4.3A.160BH.27. No chart
boundary term appears because the identity is proved on the compact group
before any small-field coordinate partition is introduced. `square`

### Definition 4.3A.160BH.32: Normal-Coordinate Template Audit

`P20-SEL2-HKSD-TPL` is the finite-template statement that the actual `SEL2`
axial-tree root chart is used with the following conventions.

1. **One root chart.** The chart, covariance, scalar readout, and
   Bianchi/off-sheet insertion are the same objects as in the active
   `SEL2` `HK-SF-YM2` worksheet.
2. **Exact heat-kernel parametrix convention.** The local heat-kernel density
   is expanded in these coordinates through order `g_i^2`; the scalar
   normalization and heat-time tangent are separated before the transverse
   projection is applied.
3. **Label completeness.** Every second-order interior term in that expansion
   which is not heat-time, scalar normalization, counterterm/scheme, collar,
   boundary, large-field, or projective/readout belongs to exactly one of the
   three labels `{4,33,J2}`:

   ```text
   4   : one quartic term from the BCH/Taylor expansion of the local YM action;
   33  : connected second cumulant of two cubic terms, with the exponential
         sign and 1/2 factor included;
   J2  : the quadratic Haar/log-chart/heat-parametrix Jacobian term.
   ```

4. **Flat interior partition.** The small-field partition and collar cutoff
   are constant on the interior root chart to second order. Derivatives of
   the partition, if any, are supported only in the already charged
   collar/boundary or large-field ledgers.
5. **Closed scalar test.** The finite scalar test
   `F_{\rho,r}\mathcal B_r^{bulk}` is gauge-invariant and depends only on the
   pushed-forward closed root record, so integration-by-parts divergence terms
   with no collar support have zero scalar connected coefficient.

The audit is deliberately finite. It is verified or falsified by expanding
one of the finitely many `SEL2` root templates; it is not a continuum
existence hypothesis.

### Lemma 4.3A.160BH.33: Template Audit Supplies The Second-Order Expansion

Assume `P20-SEL2-HKSD-TPL`. Then clause 2 of `P20-SEL2-ROOT-HKSD` holds.

Proof.

By Lemma 4.3A.160BH.31 the exact root identity is first available on the
compact group. Pull it back to the finite axial-tree chart. The coordinate
expression of the group Laplacian, the gradient of the heat-kernel density,
and the Haar density is a finite smooth differential expression on the root
chart. Expanding it through order `g_i^2` gives a finite list of local
Taylor/Wick labels.

By clause 2 of `P20-SEL2-HKSD-TPL`, the scalar normalization and heat-time
tangent have already been separated. By clause 3, every remaining interior
second-order term belongs to exactly one of `{4,33,J2}` with the same sign and
cumulant convention used in Definition 4.3A.160BH.23. Terms generated by
counterterms, collars, boundaries, large-field partitions, or projective
readout are excluded precisely because they have their own ledgers in the
telescoped scalar correction. Therefore, on the finite test space generated by
`F_{\rho,r}\mathcal B_r^{bulk}`,

```math
\mathcal D_r^{YM2}
=
\alpha_{\rho,r}^{YM2}\mathcal L_{\rho,r}^{HK}
+{\rm div}_{\gamma_r}{\mathcal Q}_{\rho,r},
```

where the non-time part of `\mathcal D_r^{YM2}` is exactly the signed
`{4,33,J2}` Wick operator. This is clause 2 of
`P20-SEL2-ROOT-HKSD`. `square`

### Lemma 4.3A.160BH.34: No Interior Divergence Residue

Assume `P20-SEL2-HKSD-TPL`. Then clause 3 of
`P20-SEL2-ROOT-HKSD` holds.

Proof.

By clause 4 of the template audit, partition or cutoff derivatives are not
supported in the interior root calculation; any such term is already outside
the interior bulk ledger. Thus the divergence term left by Lemma
4.3A.160BH.33 is a true compact-group or centered-Gaussian divergence on the
finite interior root variables.

By clause 5, the test `F_{\rho,r}\mathcal B_r^{bulk}` is a closed
pushed-forward scalar record. Applying the compact-group integration by parts
identity before chart truncation, or equivalently its centered finite
Gaussian Wick form after the normal-coordinate expansion, gives zero
connected scalar coefficient for this pure interior divergence. Hence

```math
\left[
{\rm div}_{\gamma_r}{\mathcal Q}_{\rho,r}
\left(F_{\rho,r}\mathcal B_r^{bulk}\right)
\right]_{A=0}=0.
```

This is clause 3 of `P20-SEL2-ROOT-HKSD`. `square`

### Theorem 4.3A.160BH.35: Rootwise `GENMATCH` Proof Under The Template Audit

Assume `P20-SEL2-HKSD-TPL` for every interior root template used by the active
normalized `SEL2` branch. Then

```math
P20\text{-}SEL2\text{-}INTBULK\text{-}GENMATCH
```

holds. Consequently the strict exact-covariance normalized `SEL2` branch has

```math
P20\text{-}SEL2\text{-}INTBULK\text{-}FOC.
```

Proof.

Lemma 4.3A.160BH.31 proves clause 1 of `P20-SEL2-ROOT-HKSD`. Lemma
4.3A.160BH.33 proves clause 2, and Lemma 4.3A.160BH.34 proves clause 3. Thus
`P20-SEL2-ROOT-HKSD` holds at every interior root. Theorem
4.3A.160BH.29 then gives `GENMATCH`, `YM2-CANCEL`, and, on the strict
exact-covariance reduced branch, `INTBULK-FOC`. `square`

### Corollary 4.3A.160BH.36: Intermediate Proof Status Of `GENMATCH`

`GENMATCH` is now proved modulo the finite normal-coordinate template audit
`P20-SEL2-HKSD-TPL`. The proof uses only compact-group heat-kernel
integration by parts, the finite `SEL2` axial-tree chart, and same-record
projection of closed scalar records.

The only remaining item is not conceptual: expand the finite `SEL2` root
template and check clauses 2--4 of Definition 4.3A.160BH.32. If a term appears
in that expansion which is neither `{4,33,J2}` nor an already charged
nonbulk/counterterm/projective/large-field label, then `HKSD-TPL` fails and
that term must be added to the carried finite `\Xi` budget. If no such term
appears, `GENMATCH` is fully proved rootwise.

The next definition performs this finite root-template census for the strict
reduced `SEL2` branch.

### Definition 4.3A.160BH.37: Actual `SEL2` Interior Root Term Census

For the active normalized `SEL2` coefficient branch, the finite interior root
template is the following same-record object.

1. **Root variables.** Use the axial-tree logarithmic coordinates for the
   interior non-tree links in the finite root battery. Collar links,
   endpoint/corner collars, projective readout variables, and off-root
   residual variables are parameters or external records, not interior root
   variables.
2. **Root Gaussian.** Use the exact block-conditioned covariance on the root
   for the strict reduced branch. If a reference covariance different from
   the exact block-conditioned covariance is used, the difference is the
   already isolated `cov2` term and is not part of `HKSD-TPL`.
3. **Root action through order `g_i^2`.** After extracting the quadratic
   Gaussian and the declared heat-kernel time coordinate, the only interior
   action/Jacobian terms through order `g_i^2` are

   ```text
   cubic YM vertex,
   quartic YM vertex,
   quadratic Haar/log-chart Jacobian.
   ```

   The cubic vertex enters the second-order scalar ledger only through its
   connected double insertion.
4. **Excluded ledgers.** The following possible second-order terms are not
   interior `HKSD-TPL` terms:

   ```text
   heat-time tangent        -> absorbed in T_j^{SEL2,conv};
   scalar normalization     -> connected/cumulant normalization;
   gauge-slice/Faddeev term -> zero in the strict axial-tree chart;
   covariance drift         -> zero under exact root covariance, otherwise cov2;
   record/readout drift     -> time-tangent/minimal readout or projective ledger;
   counterterm/scheme       -> E_{rho,ct}^{SEL2};
   collar/boundary cutoff   -> E_{rho,col}^{SEL2} or boundary-root ledger;
   large-field partition    -> large-field ledger;
   projective/readout       -> E_{rho,proj}^{SEL2}.
   ```

5. **Interior flatness.** The small-field partition is chosen to be identically
   one on the strict interior root chart. Its derivatives are supported only
   in the collar/boundary transition region and are therefore outside the
   interior root ledger.

This term census is finite because there are only finitely many root
templates in the declared `SEL2` hypercubic block/collar list.

### Lemma 4.3A.160BH.38: No Extra Second-Order Interior Label

On the actual strict reduced `SEL2` root template of Definition
4.3A.160BH.37, every nonabsorbed second-order interior term belongs to exactly
one of `{4,33,J2}`.

Proof.

Work in the finite axial-tree root chart. The compact-group heat-kernel
identity of Lemma 4.3A.160BH.31 is pulled back to this chart and expanded
through order `g_i^2`.

The quadratic part of the heat-kernel action defines the root Gaussian and the
heat-time tangent. By the branch convention, that tangent is separated before
the transverse scalar projection. The first nonquadratic action terms are the
cubic and quartic Yang-Mills/BCH Taylor terms. Odd cubic terms do not enter
linearly after the neutral pushforward; at order `g_i^2` the cubic vertex
appears only as the connected double-cubic cumulant, which is label `33`.
The quartic Taylor term is label `4`.

The pullback of Haar measure, together with the logarithmic chart and the
small-time heat-kernel parametrix Jacobian, has no linear interior term in the
centered axial-tree coordinates. Its quadratic interior part is exactly label
`J2`.

The remaining possible second-order terms are exhausted by the exclusion list
in Definition 4.3A.160BH.37. Gauge-slice terms vanish in the strict axial-tree
chart; covariance drift is absent because the root covariance is exact;
record/readout drift is either the already absorbed coefficient time tangent
or belongs to the projective/readout ledger; counterterm/scheme, collar,
boundary, large-field, and projective terms are explicitly assigned to their
own ledgers in the telescoped scalar correction. Since the root template is
finite, this is an exhaustive term census. Therefore no extra second-order
interior label appears. `square`

### Theorem 4.3A.160BH.39: Verification Of `P20-SEL2-HKSD-TPL`

On the actual strict reduced normalized `SEL2` coefficient branch of
Definition 4.3A.160BH.37,

```math
P20\text{-}SEL2\text{-}HKSD\text{-}TPL
```

holds for every interior root template.

Proof.

Clause 1 of `HKSD-TPL` is the branch convention of Definition
4.3A.160BH.37: the chart, covariance, scalar readout, and
Bianchi/off-sheet insertion are the same pushed-forward root objects used in
the active `HK-SF-YM2` worksheet.

Clause 2 holds because the heat-kernel density is expanded in the same finite
normal coordinates and the heat-time tangent is separated before transverse
projection by the active normalized coefficient convention.

Clause 3 is Lemma 4.3A.160BH.38: after exclusions for already charged ledgers,
the only nonabsorbed second-order interior labels are `{4,33,J2}`.

Clause 4 is Definition 4.3A.160BH.37 item 5: the interior small-field
partition is flat on the root chart, with transition derivatives supported
only in collar/boundary or large-field regions.

Clause 5 is the closed-record convention of the normalized coefficient branch:
`F_{\rho,r}` is a scalar central record observable and
`\mathcal B_r^{bulk}` is the centered Bianchi/off-sheet scalar root insertion
on the same pushed-forward closed record. Hence pure interior divergence
terms have zero connected scalar coefficient by compact-group integration by
parts.

Thus all clauses of `P20-SEL2-HKSD-TPL` hold for the finite actual `SEL2`
interior root template. `square`

### Corollary 4.3A.160BH.40: `GENMATCH` Is Rootwise Closed On The Strict `SEL2` Branch

On the actual strict reduced normalized `SEL2` branch,

```math
P20\text{-}SEL2\text{-}INTBULK\text{-}GENMATCH
```

holds. Consequently,

```math
P20\text{-}SEL2\text{-}INTBULK\text{-}FOC
```

holds on the strict exact-covariance branch, and the interior bulk part of the
scalar four-dimensional coefficient defect vanishes.

Proof.

Theorem 4.3A.160BH.39 verifies `P20-SEL2-HKSD-TPL` for every actual interior
root template. Theorem 4.3A.160BH.35 then gives `GENMATCH` and
`INTBULK-FOC`. The final statement is Theorem 4.3A.160BH.15. `square`

### Theorem 4.3A.160BH.40A: Actual Interior Bianchi/Off-Sheet Roots Are Closed

Assume the actual strict reduced normalized `SEL2` branch of Definition
4.3A.160BH.37 and the standard `SEL2` sheet-time scaling audit. Then the
interior Bianchi/off-sheet scalar root envelope satisfies

```math
\zeta_{\rho,bulk,j}^{SEL2}=o(H_j^{-1}),
```

and therefore

```math
D_{\rho,int,j}^{SEL2}
=
S_j\zeta_{\rho,bulk,j}^{SEL2}
\to0.
```

Equivalently,

```math
P20\text{-}SEL2\text{-}INTBULK\text{-}ZERO
```

holds on the actual strict reduced branch.

Proof.

Corollary 4.3A.160BH.40 proves `P20-SEL2-INTBULK-FOC` on the strict
exact-covariance branch. By Definition 4.3A.160BH.10,
`INTBULK-FOC` is exactly the rooted estimate
`\zeta_{\rho,bulk,j}^{SEL2}=o(H_j^{-1})`.

The standard `SEL2` AF-area selector gives `S_j=L_j^2` and
`S_j/H_j=O(1)`. Hence

```math
S_j\zeta_{\rho,bulk,j}^{SEL2}
=
O(H_j)\,o(H_j^{-1})
=o(1).
```

Thus the area-rooted interior Bianchi/off-sheet contribution vanishes
absolutely in the scalar coefficient comparison. `square`

### Corollary 4.3A.160BH.40B: Steps 1--5 Close The Scalar Coefficient Source On The Strict Branch

Assume:

1. `P20-SEL2-ACTROW`;
2. the standard `SEL2` sheet-time scaling audit;
3. the strict exact-record, clean-minimal-counterterm, collar-refined
   large-field branch of `P20-SEL2-CLEAN-SRC`;
4. the strict reduced clean-collar convention of Definition 4.3A.160BH.8A;
5. the actual strict reduced normalized interior root branch of Definition
   4.3A.160BH.37.

Then the five scalar terms in the telescoped coefficient ledger vanish:

```math
E_{\rho,Bianchi,j}^{SEL2}
+E_{\rho,off,j}^{SEL2}
+E_{\rho,col,j}^{SEL2}
+E_{\rho,ct,j}^{SEL2}
+E_{\rho,proj,j}^{SEL2}
\to0.
```

Consequently

```math
P20\text{-}SEL2\text{-}4DCOEFF\text{-}CLOSE(\epsilon_{\rho,j})
```

holds for some `\epsilon_{\rho,j}\to0`, before any optional
heat-character smoothing is introduced.

Proof.

`P20-SEL2-ACTROW` and Corollary 4.3A.160BH.1C identify the exact scalar target
and the complete five-term coefficient ledger. Corollary 4.3A.160BH.2G
removes the nonbulk terms
`E_{\rho,col,j}^{SEL2}+E_{\rho,ct,j}^{SEL2}+E_{\rho,proj,j}^{SEL2}` on the
strict clean branch. Corollary 4.3A.160BH.9A removes the boundary/collar part
of the Bianchi/off-sheet bulk envelope. Theorem 4.3A.160BH.40A removes the
interior part:

```math
S_j\zeta_{\rho,bulk,j}^{SEL2}\to0.
```

Lemma 4.3A.160BH.4 therefore gives

```math
E_{\rho,Bianchi,j}^{SEL2}
+E_{\rho,off,j}^{SEL2}
\to0.
```

All five scalar ledgers vanish, and Corollary 4.3A.160BH.1C gives
`P20-SEL2-4DCOEFF-CLOSE(\epsilon_{\rho,j})` with
`\epsilon_{\rho,j}\to0`. Since the proof stayed on the exact scalar observable
`\psi_\rho`, no de-smearing debit is created in this strict branch. `square`

### Theorem 4.3A.160BH.40C: Strict-Branch Normalized Coefficient Window

Assume the strict exact finite-row `SEL2` coefficient branch:

1. `P20-SEL2-ACTROW`;
2. the standard `SEL2` sheet-time scaling audit;
3. the strict exact-record, clean-minimal-counterterm, collar-refined
   large-field branch of `P20-SEL2-CLEAN-SRC`;
4. the strict reduced clean-collar convention of Definition 4.3A.160BH.8A;
5. the actual strict reduced normalized interior root branch of Definition
   4.3A.160BH.37.

Let `T_-^{SEL2}` and `T_+^{SEL2}` be strict block-time window constants from
Corollary 4.3A.160BB.1, and let `V_\rho` be a central escape set with

```math
1-{\Phi_\rho(U)\over d_\rho}\ge\gamma_\rho>0
\qquad(U\in V_\rho),
```

and

```math
\liminf_j\nu_{p,j}^{SEL2}(V_\rho)\ge q_\rho>0.
```

Then the normalized coefficient has the cofinal strict window

```math
0<s_\rho^{norm}
\le
\liminf_j {a_{\rho,j}^{SEL2}\over d_\rho}
\le
\limsup_j {a_{\rho,j}^{SEL2}\over d_\rho}
\le
1-q_\rho\gamma_\rho
<1,
```

where every strict

```math
0<s_\rho^{norm}
<
\exp\{-T_+^{SEL2}C_2(\rho)/2\}
```

is admissible after passing to a cofinal tail.

Proof.

Corollary 4.3A.160BH.40B proves
`P20-SEL2-4DCOEFF-CLOSE(\epsilon_{\rho,j})` with
`\epsilon_{\rho,j}\to0` on the strict branch. Corollary 4.3A.160BB.1 gives
the finite block-time window. Corollary 4.3A.160BG.3 then combines the scalar
comparison, the upper block-time bound, and the declared escape mass to give
the displayed coefficient window. Equivalently, if the escape set is chosen by
Corollary 4.3A.160AQ.3, the cofinal mass hypothesis is supplied by the same
strict scalar-source branch. `square`

### Definition 4.3A.160BH.40D: Certified Strict-Branch Surface Rate

On the strict exact finite-row `SEL2` coefficient branch, define the two
available normalized rate floors

```math
\widetilde\kappa_{\rho,time}^{SEL2}
:=
{T_-^{SEL2}C_2(\rho)\over2},
```

and

```math
\widetilde\kappa_{\rho,esc}^{SEL2}
:=
-\log(1-q_\rho\gamma_\rho),
```

where `T_-^{SEL2}` is any strict lower block-time constant from Corollary
4.3A.160BB.1 and `(q_\rho,\gamma_\rho)` are any strict escape data accepted in
Theorem 4.3A.160BH.40C. The conservative certified surface rate is

```math
\widetilde\kappa_{\rho,cert}^{SEL2}
:=
\min\left\{
\widetilde\kappa_{\rho,time}^{SEL2},
\widetilde\kappa_{\rho,esc}^{SEL2}
\right\}
>0.
```

The named rate audit `P20-SEL2-CERT-RATE(\widetilde\kappa_\rho)` is allowed
to use every strict

```math
0<\widetilde\kappa_\rho
<
\widetilde\kappa_{\rho,cert}^{SEL2}.
```

This is the rate that should be inserted into the surface-polymer pass test.
It is intentionally conservative: if both floors are used simultaneously, the
larger of the two lower bounds is also available, but the minimum is the
branch-stable number that remains valid under either citation route.

### Corollary 4.3A.160BH.40E: Certified Rate From The Strict Coefficient Window

Under the hypotheses of Theorem 4.3A.160BH.40C,

```math
\liminf_j
-\log\left({a_{\rho,j}^{SEL2}\over d_\rho}\right)
\ge
\widetilde\kappa_{\rho,cert}^{SEL2}.
```

Equivalently, `P20-SEL2-CERT-RATE(\widetilde\kappa_\rho)` holds for every
strict

```math
0<\widetilde\kappa_\rho
<
\widetilde\kappa_{\rho,cert}^{SEL2}.
```

Proof.

The scalar comparison from Corollary 4.3A.160BH.40B and the lower block-time
bound give

```math
\limsup_j {a_{\rho,j}^{SEL2}\over d_\rho}
\le
\exp\{-T_-^{SEL2}C_2(\rho)/2\},
```

hence

```math
\liminf_j
-\log\left({a_{\rho,j}^{SEL2}\over d_\rho}\right)
\ge
\widetilde\kappa_{\rho,time}^{SEL2}.
```

The escape side of Theorem 4.3A.160BH.40C gives

```math
\limsup_j {a_{\rho,j}^{SEL2}\over d_\rho}
\le
1-q_\rho\gamma_\rho,
```

hence

```math
\liminf_j
-\log\left({a_{\rho,j}^{SEL2}\over d_\rho}\right)
\ge
\widetilde\kappa_{\rho,esc}^{SEL2}.
```

Therefore the liminf is at least the conservative minimum of the two displayed
positive floors, and every strict smaller named rate is certified. `square`

### Corollary 4.3A.160BH.40F: Strict Surface-Polymer Pass Test

Assume the strict exact finite-row `SEL2` coefficient branch of Theorem
4.3A.160BH.40C and the certified rate convention of Definition
4.3A.160BH.40D. Assume also that the Paper-20 pre-surface margin is already
positive,

```math
\underline M_{pre13}^{SEL2,20}>0.
```

Define the strict `T13` surface-polymer threshold

```math
P_{13}^{surf,SEL2}
:=
G_{13}^{raw}
+
\log\left(
1+
{M_{13}^{surf,SEL2}\over
\underline M_{pre13}^{SEL2,20}}
\right).
```

If

```math
\widetilde\kappa_{\rho,cert}^{SEL2}
>
P_{13}^{surf,SEL2},
```

then the active `SEL2` branch passes the Paper-13/Paper-19 `T13`
surface-polymer condition.

Equivalently, the certified surface surplus

```math
\Pi_{13}^{surf,SEL2}
:=
\widetilde\kappa_{\rho,cert}^{SEL2}
-
G_{13}^{raw}
-
\log\left(
1+
{M_{13}^{surf,SEL2}\over
\underline M_{pre13}^{SEL2,20}}
\right)
```

is a valid pass certificate exactly when it is strictly positive.

Proof.

If `\Pi_{13}^{surf,SEL2}>0`, choose a strict named rate
`\widetilde\kappa_\rho` satisfying

```math
P_{13}^{surf,SEL2}
<
\widetilde\kappa_\rho
<
\widetilde\kappa_{\rho,cert}^{SEL2}.
```

Corollary 4.3A.160BH.40E certifies
`P20-SEL2-CERT-RATE(\widetilde\kappa_\rho)`. Corollary 4.3A.160AE is the
normalized surface theorem after the dimension-surcharge audit, with
`G_{13}^{norm}=G_{13}^{raw}` on the strict branch. Therefore the displayed
strict inequality is exactly the required Paper-13/Paper-19 surface-polymer
pass condition. If the displayed surplus is zero or negative, this certified
route is not closed; the failure is a failure of this scalar certificate, not
by itself a proof that no sharper same-record estimate can close the branch.
`square`

### Definition 4.3A.160BH.40G: Strict-Branch Carried Debit Ledger

For the strict exact finite-row branch used in Corollary 4.3A.160BH.40F, the
following source debits are zero by the cited strict conventions:

```math
E_{\rho,nonbulk}^{SEL2}=0,
```

because the clean nonbulk row is handled by Corollary 4.3A.160BH.2G;

```math
E_{\rho,col,bd}^{SEL2}=0,
```

because the good-collar boundary/root census is handled by Corollary
4.3A.160BH.9A;

```math
U_{CE\text{-}sm}^{SEL2}=0,
```

provided the proof uses the exact scalar observable `\psi_\rho` directly and
does not introduce an additional smoothing, de-smearing, or heat-character
cutoff transfer.

The remaining zero entries are conditional on exact operational conventions,
not automatic consequences of the finite row:

```math
U_{\rho,cov}^{SEL2}=0
```

only under exact block-conditioned covariance matching;

```math
U_{\rho,read}^{SEL2}=U_{\rho,proj}^{SEL2}=0
```

only under exact finite scalar readout and no projective/regulator mismatch;

```math
U_{\rho,ct}^{SEL2}=U_{\rho,sch}^{SEL2}=0
```

only under the clean minimal counterterm convention in which the time-tangent
part is absorbed into `T_j^{SEL2,conv}` and no residual scheme debit is
introduced.

Any branch that does not satisfy one of these strict hypotheses must carry the
corresponding finite debit. In that case the surface-polymer certificate is not
Corollary 4.3A.160BH.40F as written; one must replace the strict pre-surface
margin and/or the strict certified rate by the finite-gap ledger with the
carried sum

```math
U_{carry}^{SEL2}
=
E_{\rho,nonbulk}^{SEL2}
+E_{\rho,col,bd}^{SEL2}
+U_{CE\text{-}sm}^{SEL2}
+U_{\rho,cov}^{SEL2}
+U_{\rho,read}^{SEL2}
+U_{\rho,proj}^{SEL2}
+U_{\rho,ct}^{SEL2}
+U_{\rho,sch}^{SEL2}
+\cdots .
```

The ellipsis is not a hidden allowance: it denotes only named same-record
debits already introduced elsewhere in the paper, such as a nonzero
recoupling/local-replacement surcharge or a parked Paper-14 export debit. No
new continuum-law, area-law, or whole-process assumption may be inserted at
this stage.

### Definition 4.3A.160BH.40H: Evaluated Strict `SEL2` Surface Surplus

On the strict exact finite-row branch, use the frozen `SEL2` surface-growth
worksheet of Definition 4.3A.38:

```math
G_{13}^{raw,SEL2,cert}
:=
h_{13}^{SEL2}+d_{13}^{SEL2,20}
=
3+\log 20
+
20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}.
```

This is the certified same-record upper value for the raw nonminimal-sheet
growth `G_{13}^{raw}`. If a sharper Paper-13 surface-entropy/decorrelation
bound is proved on the same frozen `SEL2` record, it may replace
`G_{13}^{raw,SEL2,cert}`. Without such a sharper proof, this is the value that
must be used.

The four scalar inputs to the strict surface test are therefore frozen as

```math
\widetilde\kappa_{\rho,cert}^{SEL2}
=
\min\left\{
{T_-^{SEL2}C_2(\rho)\over2},
-\log(1-q_\rho\gamma_\rho)
\right\},
```

```math
G_{13}^{raw}
\le
G_{13}^{raw,SEL2,cert},
```

```math
\underline M_{pre13}^{SEL2,20}
=
\exp(L_{20})
-
\exp\left(
{20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right)
-
L_{pre13}^{SEL2},
```

and the same-record Paper-13 surface prefactor `M_{13}^{surf,SEL2}`.

The certified strict surface surplus is

```math
\Pi_{13,cert}^{surf,SEL2}
:=
\min\left\{
{T_-^{SEL2}C_2(\rho)\over2},
-\log(1-q_\rho\gamma_\rho)
\right\}
-
\left(
3+\log 20
+
20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right)
-
\log\left(
1+
{M_{13}^{surf,SEL2}\over
\exp(L_{20})
-
\exp\left(
{20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right)
-
L_{pre13}^{SEL2}}
\right).
```

This expression is meaningful only on branches for which
`\underline M_{pre13}^{SEL2,20}>0`. If the denominator in the last logarithm is
nonpositive, the branch has already failed or remains undecided at the
pre-surface stage, exactly as in Theorem 4.3A.47.

### Corollary 4.3A.160BH.40I: Closure From The Evaluated Surface Surplus

Assume the strict exact finite-row coefficient branch, the strict carried-debit
ledger of Definition 4.3A.160BH.40G, and the frozen `SEL2` decoration and
pre-surface transport worksheet of Definition 4.3A.38. If

```math
\underline M_{pre13}^{SEL2,20}>0
```

and

```math
\Pi_{13,cert}^{surf,SEL2}>0,
```

then the strict `SEL2` branch proves the named pass

```text
P20-SEL2-T13-PASS.
```

Together with the decoration closure and linear transport closure already
used to define `\underline M_{pre13}^{SEL2,20}`, this proves

```text
P20-LOSS-PASS
```

for the strict exact finite-row `SEL2` branch.

Proof.

The first displayed hypothesis makes the logarithm in Definition
4.3A.160BH.40H admissible and leaves a positive reserve for the surface-polymer
tail. The second displayed hypothesis is stronger than the threshold in
Corollary 4.3A.160BH.40F, because
`G_{13}^{raw}\le G_{13}^{raw,SEL2,cert}`. Therefore the strict branch passes
the Paper-13/Paper-19 `T13` surface-polymer condition. The zero-debit ledger
in Definition 4.3A.160BH.40G ensures that no hidden nonbulk, boundary,
de-smearing, covariance, readout, projective, counterterm, or scheme debit is
being spent outside the frozen `L_pre13^SEL2` register. Theorem 4.3A.39 then
adds the decoration, linear transport, exact-entry, exact-comparison, and
surface-polymer debits and gives strict total loss below `Sig_AFM^{SEL2}`.
`square`

### Definition 4.3A.160BH.40J: Two-Gate Form Of The Surface Surplus

Define the certified rate, certified surface growth, and rate-growth gap by

```math
R_{13,cert}^{SEL2}
:=
\min\left\{
{T_-^{SEL2}C_2(\rho)\over2},
-\log(1-q_\rho\gamma_\rho)
\right\},
```

```math
G_{13,cert}^{SEL2}
:=
3+\log 20
+
20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}},
```

and

```math
\Delta_{13,cert}^{SEL2}
:=
R_{13,cert}^{SEL2}
-
G_{13,cert}^{SEL2}.
```

When `\underline M_{pre13}^{SEL2,20}>0`, the evaluated surplus of Definition
4.3A.160BH.40H can be written as

```math
\Pi_{13,cert}^{surf,SEL2}
=
\Delta_{13,cert}^{SEL2}
-
\log\left(
1+
{M_{13}^{surf,SEL2}\over\underline M_{pre13}^{SEL2,20}}
\right).
```

The strict pass test therefore separates into:

```math
\Delta_{13,cert}^{SEL2}>0,
```

and

```math
M_{13}^{surf,SEL2}
<
\underline M_{pre13}^{SEL2,20}
\left(
\exp(\Delta_{13,cert}^{SEL2})-1
\right).
```

The first inequality is the certified rate-over-growth gate. The second
inequality is the exact admissible surface-prefactor gate.

### Corollary 4.3A.160BH.40K: Rate And Prefactor Gates Are Necessary And Sufficient

On any strict branch with `\underline M_{pre13}^{SEL2,20}>0` and
`M_{13}^{surf,SEL2}\ge0`,

```math
\Pi_{13,cert}^{surf,SEL2}>0
```

if and only if both gates in Definition 4.3A.160BH.40J hold.

Equivalently, the rate-over-growth gate itself is the pair of scalar lower
bounds

```math
T_-^{SEL2}
>
{2G_{13,cert}^{SEL2}\over C_2(\rho)}
```

and

```math
q_\rho\gamma_\rho
>
1-\exp(-G_{13,cert}^{SEL2}).
```

Thus the certified escape mass must be strong enough to beat the full
same-record surface-growth constant, and the certified block-time lower bound
must beat the same constant after division by `C_2(\rho)/2`.

Proof.

For the first claim, exponentiate the inequality

```math
\Delta_{13,cert}^{SEL2}
>
\log\left(
1+
{M_{13}^{surf,SEL2}\over\underline M_{pre13}^{SEL2,20}}
\right).
```

Since the logarithm is nonnegative, the left side must be positive. Because
`\underline M_{pre13}^{SEL2,20}>0`, the exponentiated inequality is exactly

```math
M_{13}^{surf,SEL2}
<
\underline M_{pre13}^{SEL2,20}
\left(
\exp(\Delta_{13,cert}^{SEL2})-1
\right).
```

Conversely, the two displayed gates imply the logarithmic inequality by
monotonicity of `log`.

For the rate-over-growth gate, the minimum
`R_{13,cert}^{SEL2}` is larger than `G_{13,cert}^{SEL2}` exactly when both
entries in the minimum are larger than `G_{13,cert}^{SEL2}`. The first entry
gives the displayed lower bound on `T_-^{SEL2}`. The second entry is

```math
-\log(1-q_\rho\gamma_\rho)>G_{13,cert}^{SEL2},
```

which is equivalent to
`q_\rho\gamma_\rho>1-\exp(-G_{13,cert}^{SEL2})`. `square`

### Corollary 4.3A.160BH.40L: Step-1--4 Scalar Verdict For Strict `SEL2`

The first four surface-pass tasks for the strict branch have the following
complete scalar form.

1. The scalar surplus is decided by `\Pi_{13,cert}^{surf,SEL2}>0`.
2. The certified-rate bottleneck is exactly the pair
   `T_-^{SEL2}>2G_{13,cert}^{SEL2}/C_2(\rho)` and
   `q_\rho\gamma_\rho>1-\exp(-G_{13,cert}^{SEL2})`.
3. The current frozen surface-growth side is

   ```math
   G_{13,cert}^{SEL2}
   =
   3+\log 20
   +
   20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}},
   ```

   and may be replaced only by a sharper same-record Paper-13 surface-growth
   proof.
4. The prefactor penalty is exactly the admissible inequality

   ```math
   M_{13}^{surf,SEL2}
   <
   \underline M_{pre13}^{SEL2,20}
   \left(
   \exp(\Delta_{13,cert}^{SEL2})-1
   \right).
   ```

If any strict-zero convention from Definition 4.3A.160BH.40G is dropped, the
same four clauses remain valid only after replacing the pre-surface margin by
the carried margin

```math
\underline M_{pre13,carry}^{SEL2,20}
:=
\underline M_{pre13}^{SEL2,20}-U_{carry}^{SEL2}.
```

In particular, a negative or zero carried margin stops the route before the
surface-polymer leading-rate test.

### Corollary 4.3A.160BH.40M: Rate-Gate Plausibility Diagnostic

Let

```math
E_{20}^{dec}
:=
20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}},
\qquad
G_0:=3+\log 20,
```

so that

```math
G_{13,cert}^{SEL2}=G_0+E_{20}^{dec}.
```

Since `\widehat\eta_{*,20}\ge0`,

```math
G_{13,cert}^{SEL2}\ge G_0=3+\log 20\approx5.995732.
```

Therefore the escape half of the rate-over-growth gate requires

```math
q_\rho\gamma_\rho
>
1-\exp(-G_{13,cert}^{SEL2})
=
1-{e^{-E_{20}^{dec}}\over20e^3}
\ge
1-{1\over20e^3}
\approx
0.9975106.
```

Equivalently,

```math
1-q_\rho\gamma_\rho
<
{e^{-E_{20}^{dec}}\over20e^3}
\le
{1\over20e^3}
\approx
0.0024894.
```

The block-time half requires

```math
T_-^{SEL2}
>
{2(G_0+E_{20}^{dec})\over C_2(\rho)}
\ge
{6+2\log 20\over C_2(\rho)}.
```

For the fundamental representation of `SU(N)`, where
`C_2(F)=(N^2-1)/(2N)`, the decoration-free lower threshold is

```math
T_-^{SEL2}
>
{4N(3+\log 20)\over N^2-1}.
```

In particular, before any positive decoration term is added, this gives the
benchmarks

```text
SU(2), F:  T_-^{SEL2} > 15.9886...
SU(3), F:  T_-^{SEL2} >  8.9936...
SU(4), F:  T_-^{SEL2} >  6.3954...
```

Thus the current certified surface-growth bound makes the rate gate severe:
the escape witness must force an almost maximal normalized coefficient gap,
and the block-time lower bound must be very large unless `C_2(\rho)` is large
or a sharper same-record surface-growth estimate replaces `G_{13,cert}^{SEL2}`.

This is a plausibility diagnostic, not a falsification. The gate is falsified
only if the same frozen `SEL2` record also supplies either

```math
q_\rho\gamma_\rho
\le
1-\exp(-G_{13,cert}^{SEL2})
```

or

```math
T_-^{SEL2}
\le
{2G_{13,cert}^{SEL2}\over C_2(\rho)}.
```

Absent such upper information, the honest conclusion is that the strict `SEL2`
certificate is currently bottlenecked at the rate-over-growth gate.

### Definition 4.3A.160BH.40N: Surface-Growth Decomposition Audit

The certified surface-growth constant used above splits as

```math
G_{13,cert}^{SEL2}
=
h_{13,geom}^{SEL2}
+
d_{13,dec}^{SEL2,20},
```

where the decoration part is

```math
d_{13,dec}^{SEL2,20}
:=
20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}},
```

and the currently imported Paper-19 geometry part is

```math
h_{13,geom}^{SEL2,old}
:=
3+\log 20.
```

The geometry audit separates four possible sources of surface growth:

1. plaquette adjacency: the maximum number of edge-sharing neighboring block
   plaquettes;
2. local replacement types: additional non-backtracking replacement labels per
   added plaquette;
3. orientation/sign bookkeeping: whether oriented plaquette sheets are counted
   as separate supports;
4. disconnected component/partition bookkeeping: how several local deviations
   are ordered and rooted.

On the strict reduced `SEL2` support convention, orientation/sign bookkeeping
is part of the scalar loop record and not a support count, and local
backtracking pairs are removed before the entropy count. Thus only the
unoriented plaquette-adjacency animal count contributes to the per-excess
geometry exponent; component partitions and root placements are assigned to
the surface prefactor `M_{13}^{surf,SEL2}` unless they grow exponentially in
the excess area.

### Lemma 4.3A.160BH.40O: Actual `4D` Reduced Surface Template Counts

On the strict reduced four-dimensional hypercubic block-surface template:

```math
\Delta_{plaq}^{4D}=20,
\qquad
R_{loc}^{4D}=1.
```

The value `20` is sharp for the edge-sharing plaquette graph, but it is a
degree bound, not itself the connective constant of rooted excess surfaces.
The value `R_loc^{4D}=1` holds because the strict branch counts reduced
unoriented supports: orientation, scalar sign, and representation trace data
are already in the finite loop record, while local backtracking pairs are
cancelled before the surface-support enumeration.

Proof.

Each plaquette has four boundary block edges. Along any fixed edge in four
dimensions, the edge direction can be paired with three transverse coordinate
directions and two sides, giving six incident plaquettes, one of which is the
original plaquette. Thus at most five other plaquettes share that edge.
Summing over the four edges gives at most `4*5=20` edge-sharing neighbors, and
interior plaquettes in the infinite hypercubic block lattice attain the bound.

The strict reduced support convention removes backtracking pairs and does not
double supports by orientation. Once the added neighboring plaquette is chosen,
there is no further replacement label to count in the support entropy.
Boundary and collar restrictions can only lower the degree. `square`

### Theorem 4.3A.160BH.40P: Rooted Animal Sharpening Of The Geometry Constant

Under the strict reduced `SEL2` support convention of Definition
4.3A.160BH.40N, the geometry exponent may be sharpened from

```math
h_{13,geom}^{SEL2,old}=3+\log 20
```

to the rooted tree-graph bound

```math
h_{13,geom}^{SEL2,tree}
:=
1+\log 19.
```

Equivalently, the same-record surface-growth constant may be replaced by

```math
G_{13,tree}^{SEL2}
:=
1+\log 19
+
20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}.
```

This replacement is valid only for the same reduced support branch: if
orientation-doubled supports, independent local replacement labels, or
exponentially many collar-root choices are restored, their exponents must be
added back.

Proof.

Let `A_q(r)` be the number of connected reduced excess plaquette animals of
size `q` containing a fixed root plaquette `r` in the block plaquette
adjacency graph. For a graph of maximum degree `Delta`, the standard
tree-graph bound gives

```math
A_q(r)\le [e(\Delta-1)]^{q-1}.
```

Indeed, every connected animal has a spanning tree rooted at `r`; during a
depth-first tree exposure, after the first plaquette every newly exposed
plaquette has at most `Delta-1` forward choices, and the number of rooted tree
shapes with `q` vertices is bounded by `e^{q-1}`. This overcounts animals, but
it is uniform and depends only on the local degree.

For the actual strict `4D` reduced template, Lemma 4.3A.160BH.40O gives
`Delta=20`, hence the connected rooted exponent is at most

```math
\log(e(20-1))=1+\log 19.
```

Disconnected deviations are finite collections of connected components with
total excess `q`. The integer partition factor is subexponential:

```math
\lim_{q\to\infty}{1\over q}\log p(q)=0.
```

For each fixed Creutz battery row, root placements and the finite number of
boundary/collar attachment choices multiply the surface prefactor
`M_{13}^{surf,SEL2}`; they do not change the per-excess limsup exponent. Thus
the per-excess geometry growth is bounded by `1+log 19`. `square`

### Corollary 4.3A.160BH.40Q: Sharpened Rate-Gate Plausibility Diagnostic

With the rooted tree-graph surface-growth constant,

```math
G_{13,tree}^{SEL2}
=
1+\log 19
+
20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}},
```

the decoration-free floor becomes

```math
1+\log 19\approx3.944439.
```

The escape half of the rate gate now requires

```math
q_\rho\gamma_\rho
>
1-\exp(-G_{13,tree}^{SEL2})
\ge
1-{1\over19e}
\approx
0.980632.
```

The block-time half requires, before adding the positive decoration
correction,

```math
T_-^{SEL2}
>
{2(1+\log 19)\over C_2(\rho)}.
```

For the fundamental representation of `SU(N)` this gives the benchmark

```math
T_-^{SEL2}>
{4N(1+\log 19)\over N^2-1},
```

namely

```text
SU(2), F:  T_-^{SEL2} > 10.5185...
SU(3), F:  T_-^{SEL2} >  5.9167...
SU(4), F:  T_-^{SEL2} >  4.2074...
```

This is a real improvement over the `3+log 20` envelope, but the gate remains
strong: the strict branch still needs a very large normalized escape product
or a large block-time lower bound. The next possible improvement would have to
come from an actual lattice-surface connective constant below `e(19)`, not
from the already-audited plaquette degree or local replacement count.

### Corollary 4.3A.160BH.40R: Sharpened Surface Surplus On Reduced `SEL2`

On the strict reduced `SEL2` support branch, every occurrence of
`G_{13,cert}^{SEL2}` in Definitions 4.3A.160BH.40J--4.3A.160BH.40L may be
replaced by

```math
G_{13,tree}^{SEL2}
=
1+\log 19
+
20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}.
```

Thus the sharpened rate-growth gap is

```math
\Delta_{13,tree}^{SEL2}
:=
\min\left\{
{T_-^{SEL2}C_2(\rho)\over2},
-\log(1-q_\rho\gamma_\rho)
\right\}
-
G_{13,tree}^{SEL2},
```

and the strict surface pass follows from

```math
\Delta_{13,tree}^{SEL2}>0
```

and

```math
M_{13}^{surf,SEL2}
<
\underline M_{pre13}^{SEL2,20}
\left(
\exp(\Delta_{13,tree}^{SEL2})-1
\right).
```

If the branch leaves the strict reduced support convention, this replacement
is not licensed; the abandoned orientation, replacement, or collar-root
exponents must be restored before applying the surface pass.

### Definition 4.3A.160BH.40S: Tree-Rate Threshold Functions

For the strict reduced `SEL2` branch, freeze the decoration contribution

```math
D_{13,dec}^{SEL2,20}
:=
20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}.
```

The sharpened tree-growth constant is

```math
G_{13,tree}^{SEL2}
=
1+\log 19+D_{13,dec}^{SEL2,20}.
```

The exact escape threshold is

```math
\Theta_{esc}^{tree}(\widehat\eta_{*,20})
:=
1-\exp(-G_{13,tree}^{SEL2})
=
1-
{1\over19e}
\exp\left(
-20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right).
```

Equivalently,

```math
\Theta_{esc}^{tree}(\widehat\eta_{*,20})
=
1-
{1\over19e}
\exp\left(
-D_{13,dec}^{SEL2,20}
\right).
```

The exact block-time threshold is

```math
\Theta_T^{tree}(\rho;\widehat\eta_{*,20})
:=
{2G_{13,tree}^{SEL2}\over C_2(\rho)}
=
{2\over C_2(\rho)}
\left(
1+\log 19
+20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right).
```

The sharpened rate-over-growth gate is therefore exactly

```math
q_\rho\gamma_\rho
>
\Theta_{esc}^{tree}(\widehat\eta_{*,20}),
\qquad
T_-^{SEL2}
>
\Theta_T^{tree}(\rho;\widehat\eta_{*,20}).
```

Both threshold functions are increasing in `\widehat\eta_{*,20}`. Thus the
decoration budget is not a harmless afterthought: every increase in the
character/residual activity simultaneously drives the required escape product
closer to one and raises the required block-time lower bound.

### Lemma 4.3A.160BH.40T: Source Comparison For The Tree-Rate Gate

The current strict `SEL2` source chain supplies:

1. a positive block-time lower bound `T_-^{SEL2}` from Corollary
   4.3A.160BB.1;
2. positive escape data `(q_\rho,\gamma_\rho)` from the strict escape audit
   used in Theorem 4.3A.160BH.40C;
3. the symbolic activity ceiling `\widehat\eta_{*,20}` from Definition
   4.3A.38.

It does not, by itself, supply the two numerical strict comparisons

```math
T_-^{SEL2}
>
\Theta_T^{tree}(\rho;\widehat\eta_{*,20})
```

and

```math
q_\rho\gamma_\rho
>
\Theta_{esc}^{tree}(\widehat\eta_{*,20}).
```

Consequently the sharpened geometry audit improves the surface-growth constant
but does not close the rate gate. The remaining missing source is exactly the
same-record scalar gate

```text
P20-SEL2-TREE-RATE-GATE.
```

`P20-SEL2-TREE-RATE-GATE` means the two displayed strict inequalities hold for
the same frozen `SEL2` branch, the same representation channel `\rho`, and the
same activity ceiling `\widehat\eta_{*,20}`.

Proof.

Corollary 4.3A.160BB.1 gives positivity and finiteness of the block-time
window, not a lower bound larger than the explicit tree threshold. The escape
audit gives `q_\rho>0` and `\gamma_\rho>0`, and Theorem 4.3A.160BH.40C turns
their product into a subunit coefficient gap, but it does not prove that the
product lies above the near-one threshold in Definition 4.3A.160BH.40S.
Definition 4.3A.38 fixes `\widehat\eta_{*,20}` symbolically from the residual
and character-tail worksheet; unless that worksheet is numerically
instantiated, the threshold itself remains symbolic. Hence the exact missing
assertion is the named two-inequality gate. `square`

### Definition 4.3A.160BH.40T.1: Two-Subgate Form Of The Tree-Rate Gate

The parked gate is split into two independent same-record source subgates.
Both use the same frozen `SEL2` selector, the same representation channel
`\rho`, and the same activity ceiling `\widehat\eta_{*,20}` as Definition
4.3A.160BH.40S.

The escape-mass subgate
`P20-SEL2-ESC-MASS(V_\rho,\gamma_\rho,q_\rho)` holds when:

1. `V_\rho\subset SU(N)` is a central measurable set in the active
   block-plaquette scalar record;
2. it has character gap

   ```math
   1-{\Phi_\rho(U)\over d_\rho}\ge\gamma_\rho>0
   \qquad(U\in V_\rho);
   ```

3. the frozen `SEL2` plaquette marginal has cofinal escape mass

   ```math
   \liminf_j\nu_{p,j}^{SEL2}(V_\rho)\ge q_\rho>0;
   ```

4. the resulting escape product beats the rooted tree threshold:

   ```math
   q_\rho\gamma_\rho>\Theta_{esc}^{tree}.
   ```

The tree-time subgate `P20-SEL2-TREE-TIME(\rho)` holds when

```math
T_-^{SEL2}>\Theta_T^{tree}(\rho).
```

The full gate is the conjunction

```text
P20-SEL2-TREE-RATE-GATE
:=
P20-SEL2-ESC-MASS(V_rho,gamma_rho,q_rho)
+ P20-SEL2-TREE-TIME(rho)
```

for one declared channel and one declared escape set on the frozen record law.

This split is only notation. It does not introduce a new ontology: both
subgates are scalar statements about the same pushed-forward plaquette record.

### Lemma 4.3A.160BH.40T.2: `ESC-MASS` Is Exactly The Escape Half

Assume `P20-SEL2-ESC-MASS(V_\rho,\gamma_\rho,q_\rho)`. Then the normalized
coefficient satisfies

```math
\limsup_j {a_{\rho,j}^{SEL2}\over d_\rho}
\le
1-q_\rho\gamma_\rho
<
\exp(-G_{13,tree}^{SEL2}),
```

and hence

```math
\liminf_j
-\log\left({a_{\rho,j}^{SEL2}\over d_\rho}\right)
>
G_{13,tree}^{SEL2}.
```

Conversely, if the certified rate proof is forced to use only a single
central escape set `V_\rho` with gap `\gamma_\rho` and cofinal mass
`q_\rho`, then the strict tree escape side cannot pass unless
`q_\rho\gamma_\rho>\Theta_{esc}^{tree}`.

Proof.

Corollary 4.3A.160AQ.2A gives

```math
\limsup_j {a_{\rho,j}^{SEL2}\over d_\rho}
\le
1-q_\rho\gamma_\rho.
```

By Definition 4.3A.160BH.40S,

```math
\Theta_{esc}^{tree}
=1-\exp(-G_{13,tree}^{SEL2}).
```

Thus `q_\rho\gamma_\rho>\Theta_{esc}^{tree}` is equivalent to
`1-q_\rho\gamma_\rho<\exp(-G_{13,tree}^{SEL2})`, and the logarithmic rate
bound follows. The converse is the same algebra read backwards when the only
available certified subunit gap is the product `q_\rho\gamma_\rho`. `square`

### Theorem 4.3A.160BH.40T.3: First `ESC-MASS` Pass/Fail Reduction

The exact escape-mass audit of Section 4.3A.160AQ starts the attack but does
not by itself close the tree escape side.

1. If a central set `V_\rho` satisfies the character-gap condition, the exact
   mass lower bound

   ```math
   \liminf_j\nu_{p,j}^{SEL2}(V_\rho)\ge q_\rho>0,
   ```

   and the scalar inequality

   ```math
   q_\rho\gamma_\rho>\Theta_{esc}^{tree},
   ```

   then `P20-SEL2-ESC-MASS(V_\rho,\gamma_\rho,q_\rho)` holds.

2. If the same-target normalized collapse source `P20-SEL2-NCOLL-SRC` holds,
   then `P20-SEL2-ESC-MASS(V_\rho,\gamma_\rho,q_\rho)` fails for every fixed
   central set with `\gamma_\rho>0` and `q_\rho>0`.

3. With only rowwise regularity, finite pushforward bookkeeping,
   large-field upper bounds, residual upper bounds, and representation-tail
   upper bounds, `P20-SEL2-ESC-MASS` is neither proved nor falsified.

Proof.

Clause 1 is exactly Definition 4.3A.160BH.40T.1. Clause 2 follows from
Theorem 4.3A.160AQ.4: same-target collapse gives zero cofinal mass for every
fixed positive escape window, and every fixed central set with character gap
`\gamma_\rho>0` is contained in such a window. Clause 3 is Theorem
4.3A.160AN and Corollary 4.3A.160AQ.5: the existing imported estimates are
upper-envelope estimates or regularity statements, not lower
anti-concentration estimates away from the maximizer set of `\psi_\rho`.
`square`

### Theorem 4.3A.160BH.40T.4: The Existing Positive-Escape Bound Is Too Weak

Let the strict clean scalar-source branch of Theorem 4.3A.160AQ.3 hold with

```math
\sigma_\rho^{ref}
:=
1-\exp\{-\delta_TC_2(\rho)/2\}.
```

The escape lower bound supplied there cannot close `P20-SEL2-ESC-MASS` for
the rooted tree threshold. More precisely, the product certified by that
argument is at most

```math
{\left(\sigma_\rho^{ref}\right)^2\over8}
<
{1\over8},
```

whereas

```math
\Theta_{esc}^{tree}
\ge
1-{1\over19e}
>
0.98.
```

Thus the already-proved positive escape mass is a genuine noncollapse
statement, but it is far below the nearly maximal escape product demanded by
the current rooted tree surface-growth bound.

The strict scalar-source branch can still close the escape side if it proves
the stronger direct coefficient gap

```math
1-\exp\{-\delta_TC_2(\rho)/2\}
>
\Theta_{esc}^{tree},
```

equivalently

```math
\delta_T>\Theta_T^{tree}(\rho).
```

But that is exactly the tree-time threshold in another form; it does not
provide an independent `ESC-MASS` source.

Proof.

Theorem 4.3A.160AQ.3 gives, for every
`0<\gamma<\sigma_\rho^{ref}`, the lower mass

```math
q<{\sigma_\rho^{ref}-\gamma\over2}.
```

Therefore the certified product is bounded above by

```math
\gamma q
<
{\gamma(\sigma_\rho^{ref}-\gamma)\over2}
\le
{\left(\sigma_\rho^{ref}\right)^2\over8},
```

with equality only at the formal optimizer
`\gamma=\sigma_\rho^{ref}/2`. Since `0<\sigma_\rho^{ref}<1`, this upper bound
is less than `1/8`. On the other hand
`D_{13,dec}^{SEL2,20}\ge0`, so Definition 4.3A.160BH.40S gives

```math
\Theta_{esc}^{tree}
=1-{1\over19e}\exp(-D_{13,dec}^{SEL2,20})
\ge
1-{1\over19e}
>0.98.
```

Hence the positive-escape lower bound from Theorem 4.3A.160AQ.3 cannot prove
`q_\rho\gamma_\rho>\Theta_{esc}^{tree}`.

For the last claim, the direct coefficient gap gives

```math
\limsup_j {a_{\rho,j}^{SEL2}\over d_\rho}
\le
\exp\{-\delta_TC_2(\rho)/2\}.
```

This beats the tree surface exponent precisely when

```math
\exp\{-\delta_TC_2(\rho)/2\}<\exp(-G_{13,tree}^{SEL2}),
```

or `\delta_TC_2(\rho)/2>G_{13,tree}^{SEL2}`. By Definition
4.3A.160BH.40S this is
`\delta_T>\Theta_T^{tree}(\rho)`. `square`

### Definition 4.3A.160BH.40T.5: `TREE-TIME` Evaluation Window

On the standard frozen `SEL2` AF-area selector, define the clean certified
time window

```math
T_{clean,-}^{SEL2}
:=
s(1-\epsilon_A)(1-\chi),
```

and

```math
T_{clean,+}^{SEL2}
:=
s(1+\epsilon_A)(1+\chi).
```

These are not new source constants. They are the lower and upper endpoints
computed in Theorem 4.3A.160BB from the finite block-time identity

```math
T_j^{SEL2,conv}
=
\sum_{b\in\mathscr S_j^{SEL2}}\tau_{b,j}
=
S_jt_{i(j)}+o(1),
```

with

```math
{S_j\over H_j}\in[s(1-\epsilon_A),s(1+\epsilon_A)],
\qquad
{t_{i(j)}\over g_{i(j)}^2}\in[1-\chi,1+\chi].
```

The `TREE-TIME` source is evaluated against the threshold

```math
\Theta_T^{tree}(\rho)
=
{2\over C_2(\rho)}
\left(
1+\log 19
+20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right).
```

This is a scalar finite-template audit. It does not mention a continuum field,
a hidden flux tube, or a Wilson-loop area-law input.

### Theorem 4.3A.160BH.40T.6: Exact `TREE-TIME` Pass/Falsification Test

Assume the standard `SEL2` sheet-time scaling audit of Definition
4.3A.160BA.

1. If

   ```math
   T_{clean,-}^{SEL2}>\Theta_T^{tree}(\rho),
   ```

   then `P20-SEL2-TREE-TIME(\rho)` holds.

2. If

   ```math
   T_{clean,+}^{SEL2}\le\Theta_T^{tree}(\rho),
   ```

   then `P20-SEL2-TREE-TIME(\rho)` fails for the standard frozen `SEL2`
   template.

3. If

   ```math
   T_{clean,-}^{SEL2}
   \le
   \Theta_T^{tree}(\rho)
   <
   T_{clean,+}^{SEL2},
   ```

   then the current window audit is inconclusive. The subgate can be decided
   only by sharpening the actual liminf of `T_j^{SEL2,conv}`, tightening the
   AF-area/scheme slack, or changing the frozen selector.

Proof.

By Theorem 4.3A.160BB,

```math
T_{clean,-}^{SEL2}
\le
\liminf_jT_j^{SEL2,conv}
\le
\limsup_jT_j^{SEL2,conv}
\le
T_{clean,+}^{SEL2}.
```

For clause 1, choose a strict lower endpoint `T_-^{SEL2}` with

```math
\Theta_T^{tree}(\rho)<T_-^{SEL2}<T_{clean,-}^{SEL2}.
```

Corollary 4.3A.160BB.1 then gives
`T_-^{SEL2}\le T_j^{SEL2,conv}` on a cofinal tail, and the chosen inequality
is exactly `P20-SEL2-TREE-TIME(\rho)`.

For clause 2, suppose a valid tree-time endpoint existed. Then there would be
a cofinal lower bound `T_-^{SEL2}\le T_j^{SEL2,conv}` and
`T_-^{SEL2}>\Theta_T^{tree}(\rho)`. This would imply

```math
\limsup_jT_j^{SEL2,conv}\ge T_-^{SEL2}>\Theta_T^{tree}(\rho),
```

contradicting
`\limsup_jT_j^{SEL2,conv}\le T_{clean,+}^{SEL2}\le\Theta_T^{tree}(\rho)`.

Clause 3 is the remaining case: the coarse certified window straddles the
threshold, so neither a strict cofinal lower pass nor a strict cofinal upper
falsifier follows from the present data. `square`

### Corollary 4.3A.160BH.40T.7: Selector-Parameter Form Of `TREE-TIME`

For the standard `SEL2` selector, `TREE-TIME` is guaranteed if

```math
s
>
{2\left(
1+\log 19
+20\widehat\eta_{*,20}/(1-\widehat\eta_{*,20})
\right)
\over
C_2(\rho)(1-\epsilon_A)(1-\chi)}.
```

It is falsified by the clean finite-template window if

```math
s
\le
{2\left(
1+\log 19
+20\widehat\eta_{*,20}/(1-\widehat\eta_{*,20})
\right)
\over
C_2(\rho)(1+\epsilon_A)(1+\chi)}.
```

Between these two inequalities, the currently stated `SEL2` window leaves
`P20-SEL2-TREE-TIME` parked.

In the decoration-free and zero-slack diagnostic limit
`\widehat\eta_{*,20}=\epsilon_A=\chi=0`, the pass threshold is

```math
s>{2(1+\log 19)\over C_2(\rho)}.
```

For the fundamental channel of `SU(N)`,
`C_2(F)=(N^2-1)/(2N)`, this becomes

```math
s>{4N(1+\log 19)\over N^2-1}.
```

Numerically, the decoration-free zero-slack thresholds are exactly the
benchmarks already obtained for `T_-^{SEL2}`:

```text
SU(2), F:  s > 10.5185...
SU(3), F:  s >  5.9167...
SU(4), F:  s >  4.2074...
```

Adding decoration activity or selector slack only raises the pass threshold.

Proof.

Substitute the definition of `Theta_T^{tree}` into the pass and falsification
conditions of Theorem 4.3A.160BH.40T.6, then solve for `s`. The numerical
values use the standard fundamental Casimir. `square`

### Corollary 4.3A.160BH.40T.8: Current Verdict On `TREE-TIME`

The finite block pushforward has now evaluated the relevant clean convolution
time:

```math
T_j^{SEL2,conv}=S_jt_{i(j)}+o(1),
```

so the `TREE-TIME` question is no longer vague. It is the scalar inequality

```math
s(1-\epsilon_A)(1-\chi)
>
\Theta_T^{tree}(\rho)
```

for the frozen selector, or the corresponding falsifier

```math
s(1+\epsilon_A)(1+\chi)
\le
\Theta_T^{tree}(\rho).
```

With the current corpus, `P20-SEL2-TREE-TIME` is not unconditionally proved
or falsified because the active selector has not fixed numerical values of
`s`, `\epsilon_A`, `\chi`, `\widehat\eta_{*,20}`, and `\rho` satisfying one
side of the trichotomy.

The audit does show something important: the finite `SEL2` block pushforward
does not create hidden extra time beyond the declared sheet list. Collar
increments are `o(1)`, counterterm/scheme changes are already absorbed into
`T_j^{SEL2,conv}` only when explicitly declared, and off-sheet/collar/Bianchi
corrections are scalar coefficient defects rather than additional positive
heat time. Thus any proof of `TREE-TIME` must either choose and freeze a large
enough AF-area parameter `s`, prove a sharper lower bound for the actual
liminf of `T_j^{SEL2,conv}`, or lower the surface-growth threshold. It cannot
be obtained merely from finite pushforward bookkeeping.

### Corollary 4.3A.160BH.40U: Tree-Rate Gate Closes The Rate Side

Assume the strict reduced `SEL2` support branch and
`P20-SEL2-TREE-RATE-GATE`. Then

```math
\Delta_{13,tree}^{SEL2}>0.
```

The remaining surface-polymer task is only the prefactor cap

```math
M_{13}^{surf,SEL2}
<
\underline M_{pre13}^{SEL2,20}
\left(
\exp(\Delta_{13,tree}^{SEL2})-1
\right).
```

If either inequality in `P20-SEL2-TREE-RATE-GATE` fails on the same frozen
record, then the strict reduced `SEL2` certificate cannot pass the
surface-polymer test with the current rooted tree-graph growth bound,
regardless of how small `M_{13}^{surf,SEL2}` is.

Proof.

By Definition 4.3A.160BH.40S, the two inequalities in
`P20-SEL2-TREE-RATE-GATE` are exactly

```math
\min\left\{
{T_-^{SEL2}C_2(\rho)\over2},
-\log(1-q_\rho\gamma_\rho)
\right\}
>
G_{13,tree}^{SEL2}.
```

This is the statement `\Delta_{13,tree}^{SEL2}>0`. Corollary
4.3A.160BH.40R then leaves only the displayed prefactor cap. If one of the two
rate inequalities fails, the minimum is not strictly above
`G_{13,tree}^{SEL2}`, so `\Delta_{13,tree}^{SEL2}\le0`; the admissible
prefactor cap is then nonpositive and no nonnegative surface prefactor can
restore the strict pass. `square`

### Theorem 4.3A.160BH.40V: Paper-11/12 Audit Parks The Tree-Rate Gate

After the Paper-11 RG-closure audit and the Paper-12 loop-renormalization
audit, the current corpus does not supply a stronger source theorem for
`P20-SEL2-TREE-RATE-GATE`.

More precisely:

1. Paper 11 supplies conditional `CYM-RG` residual bookkeeping,
   one-block/multiscale AF locality-margin forms, perturbative inverse-coupling
   tracking, and a smeared Wilson-loop nontriviality anchor. It does not prove
   the actual `SEL2` block-plaquette coefficient-time lower bound
   `T_-^{SEL2}>\Theta_T^{tree}` and does not prove the same-record escape
   product `q_\rho\gamma_\rho>\Theta_{esc}^{tree}`.
2. Paper 12 supplies calibrated perimeter/cusp renormalized Wilson-loop
   records, smearing-removal schedules, and nontriviality transfer for
   admissible Wilson-loop batteries. It does not compute the active
   block-plaquette central character coefficient and does not provide a
   heat-kernel coefficient comparison for the `SEL2` scalar sheet observable.
3. Therefore the present Paper-20 strict reduced branch cannot strengthen
   `P20-SEL2-TREE-RATE-GATE` by citation to Papers 11--12.

The active status is:

```text
P20-SEL2-TREE-RATE-GATE is parked as the remaining SEL2 source obstruction.
```

It is reopened only by a same-record source theorem proving the two strict
inequalities

```math
q_\rho\gamma_\rho>\Theta_{esc}^{tree}(\widehat\eta_{*,20}),
\qquad
T_-^{SEL2}>\Theta_T^{tree}(\rho;\widehat\eta_{*,20}),
```

or by a new surface-growth theorem lowering the thresholds and re-running the
same comparison on the frozen record law.

### Proof

The Paper-11 audit identifies the missing Paper-20 source data as the actual
central coefficient window, the positive coefficient-time lower bound, and the
same-record heat-kernel comparison. Its positive outputs are residual ledgers
and perturbative smeared-loop anchors, not the `SEL2` block-plaquette sheet
rate. Paper 12 changes the Wilson-loop readout side by renormalizing perimeter,
cusp, and smearing effects; it does not change the block-plaquette coefficient
source. Consequently neither paper proves either inequality in
`P20-SEL2-TREE-RATE-GATE`. Corollary 4.3A.160BH.40U says those inequalities
are exactly the remaining rate-side pass condition, so absent a new
same-record source theorem the gate is parked. `square`

### Corollary 4.3A.160BH.40W: Current Paper-20 Closure Status

On the strict reduced `SEL2` branch, Paper 20 has reduced the coefficient and
loss problem to explicit same-record scalar source data, but the branch is not
an unconditional proof of actual four-dimensional confinement. The currently
parked obstruction is:

```text
P20-SEL2-TREE-RATE-GATE
```

together with any carried finite debit that is restored when the strict exact
branch conventions are relaxed. If `P20-SEL2-TREE-RATE-GATE` is later proved
on the frozen record law and the prefactor cap of Corollary
4.3A.160BH.40U is satisfied, the strict reduced `SEL2` branch reaches
`P20-LOSS-PASS`. If it is falsified, this `SEL2` surface-polymer route fails
without falsifying every possible confinement strategy.

### Theorem 4.3A.160BI: Scalar Four-Dimensional Source Closes The Normalized Route

Assume:

1. `P20-SEL2-4DCOEFF-CLOSE(\epsilon_{\rho,j})`;
2. the standard `SEL2` sheet-time scaling audit of Definition 4.3A.160BA.

Then the conclusions of Theorem 4.3A.160BG hold. In particular the normalized
leading sheet has positive rate and a fixed non-identity escape witness, with
every strict

```math
0<\widetilde\kappa_\rho
<
{s(1-\epsilon_A)(1-\chi)C_2(\rho)\over2}.
```

Proof.

Definition 4.3A.160BH identifies
`\delta_{\rho,conv,j}^{SEL2}` with the scalar four-dimensional correction.
Thus `P20-SEL2-4DCOEFF-CLOSE` implies
`P20-SEL2-SCONV-CLOSE`. Apply Theorem 4.3A.160BG. `square`

### Corollary 4.3A.160BJ: Step-3 Verdict

The real four-dimensional comparison no longer has to be proved in total
variation in order to close the normalized leading-rate branch. It is enough to
prove either the vanishing scalar source

```text
P20-SEL2-4DCOEFF-CLOSE(epsilon_rho,j), epsilon_rho,j -> 0.
```

or, on the cofinal positive-sign branch, the finite-gap scalar inequality in
Theorem 4.3A.160BH.5:

```math
\delta_{\rho,*}^{SEL2}
<
1-\exp\{-s(1-\epsilon_A)(1-\chi)C_2(\rho)/2\}.
```

Together with the already evaluated `SEL2` AF-area scaling of
`T_j^{SEL2,conv}`, either scalar source gives both positive normalized rate and
a cofinal non-identity escape witness.

This is a real improvement over Corollary 4.3A.160BD, but it is not yet an
unconditional proof. Lemma 4.3A.160BH.2 and Theorem 4.3A.160BH.2B reduce the
counterterm, projective, and collar terms to a precise fork: they vanish on
the strict clean nonbulk branch and otherwise remain as the carried debit
`E_{\rho,nonbulk}`. The boundary Bianchi/off-sheet roots are also no longer
open on the clean branch: Theorem 4.3A.160BH.8D and Corollary
4.3A.160BH.8E prove `BDROOT` and `BDROOT0`. The interior bulk obstruction has
now been closed on the strict reduced normalized `SEL2` branch: Corollary
4.3A.160BH.40 proves rootwise `GENMATCH`, hence `INTBULK-FOC`, by verifying
the finite normal-coordinate template audit.

Thus the clean scalar-source route is assembled except for the exact
unsmoothed transfer:

```text
exact de-smearing/tail-tightness if the unsmoothed coefficient is used.
```

If the strict exact-covariance/minimal-readout branch is not used, then the
finite carried terms identified above, especially
`M_{rho,cov}^{int}K_{rho,cov}^{int}`, must be restored and tested in the
finite-gap inequality. If the clean collar branch is not used, the carried
boundary/collar debit `E_{\rho,col,*}^{SEL2,bd}` from Definition
4.3A.160BH.8C must also be restored. If the clean nonbulk branch is not used,
restore `E_{\rho,nonbulk}`. If tail-tightness is not used, restore
`U_{CE-sm}^{SEL2}`. The interior, boundary, and nonbulk scalar pieces are
closed only on the strict reduced clean branch.

### Definition 4.3A.161: Raw Positive-Rate Audit For The Leading Sheet

The exact raw positive-rate audit `P20-SEL2-CE-RATE(kappa_\rho)` asserts

```math
\liminf_j-\log a_{\rho,j}^{SEL2}\ge\kappa_\rho>0.
```

It is equivalent, on the sign branch, to the existence of a strict subunit
gap `\sigma_\rho>0` such that

```math
\limsup_j a_{\rho,j}^{SEL2}\le1-\sigma_\rho,
\qquad
\kappa_\rho=-\log(1-\sigma_\rho).
```

The rate required by the raw surface bucket is not merely `CE-UNIT`; it must
dominate the surface entropy and decoration terms in Theorem 4.3A.39. On the
active reduced normalized branch, the corresponding rate is instead
`P20-SEL2-CE-NORM-RATE` from Definition 4.3A.160AF.

### Theorem 4.3A.162: Raw `CE-RATE` Is The Dynamical Part Of The Window

Assume `P20-SEL2-CE-SIGN(s_\rho)`. Then
`P20-SEL2-CE-RATE(kappa_\rho)` holds for some `kappa_\rho>0` if and only if
there is `\sigma_\rho>0` with

```math
\limsup_j a_{\rho,j}^{SEL2}\le1-\sigma_\rho.
```

In that case one may take `kappa_\rho=-\log(1-\sigma_\rho)`. If
`a_{\rho,j}^{SEL2}\to1`, then `CE-SIGN/UNIT` may hold pointwise but
`CE-RATE` fails.

Proof.

On the positive branch, `-\log x` is continuous and decreasing on `(0,1)`.
The equivalence follows from elementary calculus. The last statement follows
because `-\log a_{\rho,j}^{SEL2}\to0` when
`a_{\rho,j}^{SEL2}\to1`. `square`

### Theorem 4.3A.163: Zero De-Smearing From Representation-Tail Tightness

Assume the de-smearing setup of Definition 4.3A.152. If

```math
\lim_{R\to\infty}
\limsup_j
\sum_{\lambda\ne0,\rho:\ C_2(\lambda)>R}
d_\lambda|\widehat\nu_{\lambda,j}^{SEL2}|
=0
```

then one can choose a diagonal schedule `\tau_j\downarrow0` for which

```math
\Delta_{CE\text{-}sm,j}^{SEL2}(\tau_j)\to0.
```

Hence `P20-SEL2-CE-DESMEAR(0)` holds.

Proof.

Fix `\epsilon>0`. The leading term is finite because
`|a_{\rho,j}^{SEL2}|\le\|\Phi_\rho\|_\infty`, so its heat-multiplier error
tends to zero as `\tau_j\downarrow0`. Choose `R` so that the non-leading
high-character tail has `limsup` less than `\epsilon`. On the finite set
`C_2(\lambda)\le R`, the heat multiplier error

```math
|1-e^{-\tau C_2(\lambda)/2}|
```

converges uniformly to zero as `\tau\downarrow0`. Choose the diagonal
schedule `\tau_j` so that the finite-window contribution is eventually below
`\epsilon`. The high-character contribution is bounded by the tight tail.
Thus the `limsup` of the de-smearing discrepancy is at most `2\epsilon`;
letting `\epsilon\downarrow0` proves the result. `square`

### Definition 4.3A.164: Exact Non-Leading Character-Tail Audit

The exact tail audit `P20-SEL2-CE-TAIL(E_\rho)` asserts

```math
\limsup_j
\sum_{\lambda\ne0,\rho}
d_\lambda|\widehat\nu_{\lambda,j}^{SEL2}|
\le E_\rho<\infty.
```

The stronger tight-tail audit `P20-SEL2-CE-TAIL-TIGHT` asserts

```math
\lim_{R\to\infty}
\limsup_j
\sum_{\lambda\ne0,\rho:\ C_2(\lambda)>R}
d_\lambda|\widehat\nu_{\lambda,j}^{SEL2}|
=0.
```

`CE-TAIL` is enough to make the non-leading debit finite. `CE-TAIL-TIGHT` is
the natural exact de-smearing source.

### Theorem 4.3A.165: Sobolev Source For `CE-TAIL`

Suppose the exact `SEL2` plaquette marginals have central densities
`K_{p,j}^{SEL2}` and, for some `s>dim(SU(N))/2`,

```math
\sup_j
\sum_\lambda
(1+C_2(\lambda))^s
|\widehat\nu_{\lambda,j}^{SEL2}|^2
<\infty.
```

Then `P20-SEL2-CE-TAIL(E_\rho)` holds for some finite `E_\rho`.

Moreover, the same Sobolev bound implies `P20-SEL2-CE-TAIL-TIGHT`, hence
Theorem 4.3A.163 gives zero de-smearing.

Proof.

By Cauchy-Schwarz,

```math
\sum_{\lambda\ne0,\rho}d_\lambda|\widehat\nu_{\lambda,j}^{SEL2}|
\le
\left(
\sum_{\lambda\ne0,\rho}d_\lambda^2(1+C_2(\lambda))^{-s}
\right)^{1/2}
\left(
\sum_{\lambda\ne0,\rho}
(1+C_2(\lambda))^s
|\widehat\nu_{\lambda,j}^{SEL2}|^2
\right)^{1/2}.
```

The first factor is finite for `s>dim(SU(N))/2` by the Weyl law. The second
factor is uniformly bounded by hypothesis. Applying the same estimate after
restricting to `C_2(\lambda)>R` gives a first factor tending to zero as
`R\to\infty`; the second factor remains uniformly bounded. This proves
`CE-TAIL-TIGHT`. `square`

### Definition 4.3A.165A: Exact De-Smearing Closure Fork

The active exact coefficient branch distinguishes two de-smearing outcomes.

1. `P20-SEL2-CE-DESMEAR-ZERO` means that there is a diagonal character-heat
   schedule `\tau_j\downarrow0` such that

   ```math
   \Delta_{CE\text{-}sm,j}^{SEL2}(\tau_j)\to0.
   ```

2. `P20-SEL2-CE-DESMEAR-FIN(U_{CE\text{-}sm}^{SEL2})` means

   ```math
   \limsup_j
   \Delta_{CE\text{-}sm,j}^{SEL2}(\tau_j)
   \le U_{CE\text{-}sm}^{SEL2}<\infty.
   ```

The first branch lets any heat-regularized coefficient estimate pass to the
exact unsmoothed coefficient without loss. The second branch is allowed only
in a finite-gap theorem, where `U_{CE-sm}^{SEL2}` is added to the scalar
defect. If neither branch is proved, the exact unsmoothed coefficient theorem
is not closed.

### Theorem 4.3A.165B: Exact De-Smearing From Tail Tightness

If `P20-SEL2-CE-TAIL-TIGHT` holds, then

```math
P20\text{-}SEL2\text{-}CE\text{-}DESMEAR\text{-}ZERO
```

holds. In particular the exact unsmoothed coefficient branch pays no
additional de-smearing debit.

If only `P20-SEL2-CE-TAIL(E_\rho)` holds, then a fixed positive
regularization proves finite regularized tails, but it does not imply
`P20-SEL2-CE-DESMEAR-ZERO`; an explicit
`P20-SEL2-CE-DESMEAR-FIN(U_{CE-sm}^{SEL2})` must be supplied separately.

Proof.

The zero statement is Theorem 4.3A.163 with the exact tight-tail audit of
Definition 4.3A.164. The final statement follows from the definition of
`\Delta_{CE-sm,j}^{SEL2}`: a finite weighted tail controls the size of the
non-leading debit at a fixed row, but without tightness it does not rule out
character mass drifting to `C_2(\lambda)\sim\tau_j^{-1}` as
`\tau_j\downarrow0`. Such drifting mass can leave
`|1-e^{-\tau_jC_2(\lambda)/2}|` bounded away from zero. Therefore finite tail
alone is not enough for exact de-smearing. `square`

### Corollary 4.3A.165C: Sobolev-Tight Exact Branch

The uniform Sobolev source of Theorem 4.3A.165 implies both
`P20-SEL2-CE-TAIL(E_\rho)` and `P20-SEL2-CE-DESMEAR-ZERO`. Thus, on a branch
where the exact `SEL2` plaquette marginals have the stated uniform Sobolev
bound, the non-leading character tail is finite and the heat-regularized
coefficient estimates pass to the exact unsmoothed coefficient with zero
de-smearing loss.

### Lemma 4.3A.165C.1: Rowwise Regularity Does Not Prove Tail Tightness

The current rowwise regularity source

```text
finite row central L^1 density + rowwise finite weighted tail
```

does not imply `P20-SEL2-CE-TAIL-TIGHT`.

Proof.

Consider the central heat-kernel densities `H_{t_j}` on `SU(N)` with
`t_j\downarrow0`. Each row is smooth, central, positive, has integral one,
and has Peter-Weyl coefficients

```math
\widehat\nu_{\lambda,j}=d_\lambda e^{-t_jC_2(\lambda)/2}
```

in the unnormalized character expansion convention used here. Therefore every
fixed row has a finite heat-trace weighted tail.

However, for any fixed cutoff `R`, the tail

```math
\sum_{\lambda:\ C_2(\lambda)>R}
d_\lambda|\widehat\nu_{\lambda,j}|
```

does not have a cofinal bound tending to zero as `R\to\infty`; as
`t_j\downarrow0`, representation mass moves through arbitrarily high
Casimir levels. In fact the full weighted heat trace grows like the compact
group heat trace as `t_j\downarrow0`, so the `limsup_j` of the high-character
tail is not controlled by any fixed `R`.

Thus smoothness and rowwise finite tails are compatible with failure of the
cofinal tight-tail audit. This example is not used as a new physical branch;
it only proves the logical non-implication from the currently available
regularity sources. `square`

### Theorem 4.3A.165C.2: Exact Tail-Tightness Is Parked Unless A Uniform Source Is Supplied

For the exact unsmoothed `SEL2` coefficient branch, the current source base
does not prove `P20-SEL2-CE-TAIL-TIGHT` from rowwise regularity,
heat-regularized `CE-REG`, or the scalar leading-coefficient comparison alone.

The exact branch is therefore parked in the following precise sense.

1. If a uniform Sobolev source as in Theorem 4.3A.165 is supplied on the exact
   `SEL2` plaquette marginals, then `P20-SEL2-CE-TAIL-TIGHT` and
   `P20-SEL2-CE-DESMEAR-ZERO` hold.
2. If another same-record representation-tail theorem proves
   `P20-SEL2-CE-TAIL-TIGHT`, then exact de-smearing is again zero by Theorem
   4.3A.165B.
3. If only a finite de-smearing audit
   `P20-SEL2-CE-DESMEAR-FIN(U_{CE-sm}^{SEL2})` is supplied, then the exact
   branch may continue only through the finite-gap inequality with
   `U_{CE-sm}^{SEL2}` added to the scalar defect.
4. If neither tail-tightness nor a finite de-smearing debit is supplied, Paper
   20 may state only the heat-regularized coefficient theorem, not the exact
   unsmoothed coefficient theorem.

Proof.

Theorem 4.3A.165 proves the positive Sobolev route. Theorem 4.3A.165B proves
that any tight-tail source gives zero de-smearing. Lemma 4.3A.165C.1 proves
that rowwise regularity and rowwise finite tails alone are insufficient. The
definition of `P20-SEL2-CE-DESMEAR-FIN` gives the finite-gap alternative. If no
such source is supplied, there is no bound connecting the heat-regularized
coefficient to the exact unsmoothed coefficient as `\tau_j\downarrow0`, so the
exact theorem is not closed. `square`

### Corollary 4.3A.165C.3: Tail-Tightness Verdict

`P20-SEL2-CE-TAIL-TIGHT` is not closed unconditionally in Paper 20. It is
closed under the explicit uniform Sobolev source of Theorem 4.3A.165, or under
any equivalent same-record representation-tail theorem. Otherwise the exact
unsmoothed branch must carry `U_{CE-sm}^{SEL2}` or remain parked at the
heat-regularized coefficient theorem.

This parking is not a continuum-measure assumption and not an area-law
assumption. It is a representation-tail regularity requirement for one finite
pushed-forward plaquette record family.

### Corollary 4.3A.165D: Clean Exact Scalar-Source Assembly

Assume the strict reduced clean `SEL2` branch:

1. the standard `SEL2` sheet-time scaling audit holds;
2. `P20-SEL2-NONBULK-COMMON`, `P20-SEL2-COL-CLEAN`,
   `P20-SEL2-CT-CLEAN`, and `P20-SEL2-PROJ-CLEAN` hold;
3. the clean good-collar boundary branch of Definition 4.3A.160BH.8A is used;
4. the strict exact-covariance interior branch of Definition 4.3A.160BH.37 is
   used;
5. `P20-SEL2-CE-TAIL-TIGHT` holds if the final theorem uses the exact
   unsmoothed coefficient.

Then the nonbulk scalar terms vanish, the boundary bulk term vanishes, the
interior bulk term vanishes, and exact de-smearing carries zero debit. Hence
the exact clean branch has

```math
P20\text{-}SEL2\text{-}4DCOEFF\text{-}CLOSE(\epsilon_{\rho,j}),
\qquad
\epsilon_{\rho,j}\to0,
```

with no additional de-smearing loss.

If any of clauses 2 or 5 is weakened to a finite carried audit, the same
argument gives the finite-gap branch with the corresponding additive debit:

```math
\delta_{\rho,*}^{SEL2}
\le
E_{\rho,nonbulk}
+E_{\rho,col,*}^{SEL2,bd}
+U_{CE\text{-}sm}^{SEL2},
```

plus any restored covariance, uncharged-template, or recoupling debit from
the chosen nonstrict branch.

Proof.

Theorem 4.3A.160BH.2B gives vanishing of
`E_{\rho,col,j}^{SEL2}+E_{\rho,ct,j}^{SEL2}+E_{\rho,proj,j}^{SEL2}` under
clause 2. Corollary 4.3A.160BH.8E gives the boundary bulk vanishing under
clause 3. Corollary 4.3A.160BH.40 gives `INTBULK-FOC`, hence
`P20-SEL2-INTBULK-ZERO`, under clause 4. Theorem 4.3A.160BH.11 then gives
`P20-SEL2-4DCOEFF-CLOSE`. Finally, Theorem 4.3A.165B gives zero de-smearing
from the tail-tightness clause. The finite-gap inequality follows by replacing
each vanishing input by its limsup debit in the telescopic bound. `square`

### Corollary 4.3A.166: Six-Step `CE` Decision On `SEL2`

The requested six-step coefficient attack has the following status.

1. **Frozen convention.** Closed by Definition 4.3A.155: the coefficient is
   the real scalar central record coefficient `a_{\rho,j}^{SEL2}`.
2. **Sign.** Reduced to `P20-SEL2-CE-SIGN(s_\rho)`; the identity-collar
   witness of Definition 4.3A.157 is a concrete non-area-law sufficient
   source, and Lemma 4.3A.156 proves regularity alone cannot supply it.
3. **Unit.** Reduced to `P20-SEL2-CE-UNIT(b_\rho)`; the escape witness of
   Definition 4.3A.159 is a concrete sufficient source, and Lemma 4.3A.156
   proves regularity alone cannot supply it. On the active raw-coefficient
   route, Theorems 4.3A.160G--4.3A.160L further reduce this to the block-time
   fork and park the route until `BTIME-LIFT` or `BTIME-COLLAPSE` is proved.
4. **Rate.** Split into two distinct audits. The raw rate is reduced to a
   strict raw subunit gap by Theorem 4.3A.162 and may not be spent while
   `P20-SEL2-RAWBTIME-PARK` is active. The active reduced normalized branch is
   governed instead by `P20-SEL2-CE-NORM-RATE` from Definition 4.3A.160AF; by
   Theorem 4.3A.160AG it passes if the normalized effective block time is
   bounded below by a positive `delta_rho` with controlled comparison error,
   and fails if that effective time collapses to zero. Lemma
   4.3A.160AI--Corollary 4.3A.160BJ reduce the positive normalized block-time
   source to the one-block escape audit `P20-SEL2-NORM-ESC`, prove that the
   current large-field/residual imports neither prove escape nor prove collapse,
   evaluate the exact heat-kernel convolution reference time on the standard
   `SEL2` AF-area scaling, and sharpen the remaining four-dimensional source
   from the overstrong total-variation audit `P20-SEL2-4DCONV-CLOSE` to the
   scalar coefficient audit `P20-SEL2-4DCOEFF-CLOSE`, with a finite-gap variant
   controlled by the bulk Bianchi/off-sheet envelope.
5. **De-smearing.** Closed if `CE-TAIL-TIGHT` holds, by Theorem
   4.3A.165B. Lemma 4.3A.165C.1 shows rowwise regularity and rowwise finite
   tails do not prove this; Theorem 4.3A.165C.2 parks the exact unsmoothed
   branch unless a uniform Sobolev/tight-tail source or a finite
   `U_{CE-sm}^{SEL2}` debit is supplied.
6. **Non-leading tail.** Closed by the Sobolev source of Theorem 4.3A.165, or
   left as the exact source audit `P20-SEL2-CE-TAIL(E_\rho)`.

Therefore Paper 20 has not proved unconditional `CE-SIGN/UNIT/RATE`; it has
made the obstruction sharp. The missing input is no longer regularity of the
plaquette law. On the raw branch it is a same-record scalar-sheet bias and
spread estimate strong enough to give

```math
0<s_\rho
\le
\liminf_j a_{\rho,j}^{SEL2}
\le
\limsup_j a_{\rho,j}^{SEL2}
\le
1-\sigma_\rho<1,
```

On the active reduced normalized branch, the corresponding missing source is

```math
0<\widetilde s_\rho
\le
\liminf_j {a_{\rho,j}^{SEL2}\over d_\rho}
\le
\limsup_j {a_{\rho,j}^{SEL2}\over d_\rho}
\le
1-\widetilde\sigma_\rho<1,
```

with the stronger numerical domination required in Definition 4.3A.160AF.
Equivalently, it is the positive normalized block-time lift
`P20-SEL2-NORM-BTIME-LIFT(delta_rho,eta_rho)`, and Theorem 4.3A.160AK gives the
concrete sufficient source `P20-SEL2-NORM-ESC(V_rho,gamma_rho,q_rho)`.
Corollary 4.3A.160BJ is sharpened by the later closure lemmas. The standard
`SEL2` AF-area scaling keeps `T_j^{SEL2,conv}` bounded away from zero, and full
total-variation convergence is not necessary for the normalized leading sheet.
The scalar four-dimensional coefficient comparison is closed on the strict
clean branch by Corollary 4.3A.165D: nonbulk collar/counterterm/projective
terms vanish, the boundary bulk term vanishes, and the interior bulk term
vanishes. Exact tail tightness is still needed if the final theorem uses the
unsmoothed coefficient; otherwise the finite de-smearing debit
`U_{CE-sm}^{SEL2}` must be added to the finite-gap scalar comparison.

### Theorem 4.3B: Linear Transport Ceilings On `SEL0`

Assume `P20-SEL0-TR-COMMON` and the finite evaluated limsups in Definition
4.3. Then the linear transport components satisfy

```math
\limsup_jT_{11,j}
\le
T_{11}^{SEL0},
\qquad
\limsup_jT_{12,j}
\le
T_{12}^{SEL0},
\qquad
\limsup_jT_{14,j}
\le
T_{14}^{SEL0}.
```

Moreover, if the four `T_11` limsups vanish, the four reduced `T_12` limsups
vanish, and `E_14^{SEL0}=0`, then the whole linear transport ceiling vanishes:

```math
T_{11}^{SEL0}+T_{12}^{SEL0}+T_{14}^{SEL0}=0.
```

Proof.

For `T_11`, Paper 19 Definition 8L.11A.5 gives the rowwise domination by the
four reduced tails

```math
R_{11,j}^{loc}+R_{11,j}^{RP}+R_{11,j}^{Cov}+R_{11,j}^{gauge}.
```

The four evaluated `SEL0` constants are exactly the limsups of these tails, so
limsup subadditivity gives the displayed `T_11` bound.

For `T_12`, Paper 19 Definition 8L.11A.21A evaluates the reduced
loop-continuity terms as the four limsups retained in Definition 4.3; the
projective, regulator, and finite-volume loop losses are excluded from `T_12`
and paid elsewhere by `P20-SEL0-TR-COMMON`. Limsup subadditivity gives the
displayed `T_12` bound.

For `T_14`, the same-battery Paper-14 export gives

```math
T_{14,j}\le \|E_{14}(\eta_j)\|_{tr},
```

and taking the limsup gives the displayed `T_14` bound. The vanishing statement
is immediate from nonnegativity of all source tails. `square`

### Theorem 4.4: Four Transport Ceilings Against The Residual Margin

Assume `P20-SEL0-TR-COMMON` and the `SEL0` transport source packages of
Definition 4.3. Define the pre-surface transport margin

```math
M_{pre13}^{SEL0}
:=
M_{loss}^{SEL0}
-T_{11}^{SEL0}
-T_{12}^{SEL0}
-T_{14}^{SEL0}
-A_{13}^{entry,SEL0}
-A_{13}^{exact,SEL0}.
```

Then the four-ceiling route has the following exact scalar fork.

1. If

   ```math
   M_{pre13}^{SEL0}\le0,
   ```

   the route cannot prove `P20-LOSS-PASS`, regardless of the surface-polymer
   tail, because all remaining debits are nonnegative.

2. If

   ```math
   M_{pre13}^{SEL0}>0
   ```

   and there is a leading rate `kappa_13^*` with

   ```math
   \mu_{13}^{SEL0}(\kappa_{13}^*)>0
   ```

   such that

   ```math
   M_{13}^{surf,SEL0}
   {\exp[-\mu_{13}^{SEL0}(\kappa_{13}^*)]
   \over
   1-\exp[-\mu_{13}^{SEL0}(\kappa_{13}^*)]}
   <
   M_{pre13}^{SEL0},
   ```

   then one can choose `q_13^*` close enough to
   `exp[-mu_13^SEL0(kappa_13^*)]` so that

   ```math
   T_{11}^{SEL0}+T_{12}^{SEL0}+T_{13}^{SEL0}(q_{13}^*)+T_{14}^{SEL0}
   <
   M_{loss}^{SEL0}.
   ```

   Hence `P20-TLOSS-SRC` fits under the residual transport margin.

3. Equivalently, when `M_{13}^{surf,SEL0}>0`, clause 2 is the leading-rate
   threshold

   ```math
   \mu_{13}^{SEL0}(\kappa_{13}^*)
   >
   \log\left(
   1+{M_{13}^{surf,SEL0}\over M_{pre13}^{SEL0}}
   \right),
   ```

   or, expanded,

   ```math
   \kappa_{13}^*
   >
   h_{13}^{SEL0}
   +d_{13}^{SEL0}
   +\log\left(
   1+{M_{13}^{surf,SEL0}\over M_{pre13}^{SEL0}}
   \right).
   ```

If the sharp same-record coefficient rate from Paper 19 is
`kappa_13^{CE}`, then the sufficient source condition is therefore

```math
\kappa_{13}^{CE}
>
h_{13}^{SEL0}
+d_{13}^{SEL0}
+\log\left(
1+{M_{13}^{surf,SEL0}\over M_{pre13}^{SEL0}}
\right),
```

because one may choose a strict `kappa_13^*` below `kappa_13^{CE}` and above
the displayed threshold.

Proof.

Definition 4.3 and the Paper-19 component ledgers give

```math
\limsup_jT_{11,j}\le T_{11}^{SEL0},
\quad
\limsup_jT_{12,j}\le T_{12}^{SEL0},
\quad
\limsup_jT_{14,j}\le T_{14}^{SEL0}.
```

For `T_13`, Paper 19 Theorem 8L.11A.22H gives subcriticality whenever
`mu_13^SEL0(kappa_13^*)>0`, and Theorem 8L.11A.23 gives the surface-tail
ceiling

```math
M_{13}^{surf,SEL0}{q_{13}^*\over1-q_{13}^*}
```

for every admissible `q_13^*` strictly above
`exp[-mu_13^SEL0(kappa_13^*)]`. Adding the entry and exact-comparison debits
gives `T_13^SEL0(q_13^*)`.

After subtracting the already-paid `T_11`, `T_12`, `T_14`, entry, and exact
comparison terms from `M_loss^SEL0`, the only remaining inequality is the
surface-tail inequality in clause 2. The function `q -> q/(1-q)` is increasing
on `(0,1)`, so strict domination by the infimal value lets us choose an
admissible `q_13^*` close enough to the endpoint. Solving

```math
M_{13}^{surf,SEL0}{x\over1-x}<M_{pre13}^{SEL0},
\qquad x=e^{-\mu},
```

gives

```math
e^{-\mu}<{M_{pre13}^{SEL0}\over M_{pre13}^{SEL0}+M_{13}^{surf,SEL0}},
```

which is equivalent to the logarithmic threshold in clause 3. The final
statement follows because Paper 19 permits any strict
`0<kappa_13^*<kappa_13^{CE}` once the same-record coefficient window is
proved. `square`

## 5. Final Loss And Source Comparison

### Definition 5.1: Loss Pass Gate `P20-LOSS-PASS`

`P20-LOSS-PASS` holds when the frozen selector supplies
`P20-DEC-SRC` and `P20-TLOSS-SRC`, and the strict scalar comparison

```math
D_{dec}^*
 + T_{11}^*+T_{12}^*+T_{13}^*+T_{14}^*
<
Sig_{AFM}
```

holds.

Equivalently,

```math
L_{AFM}^{sharp}<Sig_{AFM}.
```

### Theorem 5.2: Component Sources Prove The Loss Pass

Assume `P20-FROZEN-SEL`, `P20-NOSMUGGLE`, `P20-DEC-SRC`, and
`P20-TLOSS-SRC`. If the strict comparison in Definition 5.1 holds, then
`P20-LOSS-PASS` holds.

Proof.

Theorem 3.2 bounds the decoration debit by `D_dec^*`. Definition 4.1 bounds
the transport debit by the sum of the four component ceilings. Therefore

```math
L_{AFM}^{sharp}
\le
D_{dec}^*+T_{11}^*+T_{12}^*+T_{13}^*+T_{14}^*
<
Sig_{AFM}.
```

This is exactly `P20-LOSS-PASS`. `square`

### Obstruction 5.3: Loss Dominance

If the sharp loss limsup satisfies

```math
L_{AFM}^{sharp}\ge Sig_{AFM},
```

then the Paper-19 sufficient loss gate cannot close on the frozen selector.
An actual falsification of the direct-witness branch requires the sharper
lower-loss and upper-signal comparison named in Paper 19; failure of the
sufficient estimate alone is a route failure, not a proof that confinement is
false.

## 6. Main Paper-20 Theorem

### Theorem 6.1: Paper 20 Closure Theorem

Assume:

```text
P20-FROZEN-SEL,
P20-NOSMUGGLE,
P20-COEFF-PASS,
P20-LOSS-PASS.
```

Then the Paper-19 AF-matched direct-witness source constants pass on the
same whole-process tower. Consequently Paper 18 proves `AYM-CONF-CLOSE(m_*)`
and Paper 17 supplies the corresponding mass-gap consequence on that tower.
This is a branch closure on the declared selector. It is not an unconditional
construction of continuum `4D SU(N)` Yang-Mills unless the frozen selector
itself has also been constructed as the actual continuum Yang-Mills record law
without assuming an area law or mass gap.

Proof.

This is Theorem 0A.1. `square`

### Theorem 6.2: Paper 20 Exact Obstruction Ledger

On a frozen selector, Paper 20 fails to close the Paper-19 branch exactly at
one or more of the following scalar obstruction classes:

1. `P20-FROZEN-SEL` is inadmissible;
2. `P20-NOSMUGGLE` fails, so the selector or source estimates already import
   the conclusion;
3. `R_H^opt>=R_H^crit`, or the source decomposition cannot bound
   `R_H^opt`;
4. `eta_res^*+eta_ch^*>=1`, or `c_Delta^*` is not finite;
5. the selector's transport common-record audit, such as `P20-SEL0-TR-COMMON`
   or the corresponding audit for a replacement selector, fails, so the
   transport constants are not evaluated on one pushed-forward record law and
   one disjoint debit register;
6. one of `T_11^*`, `T_12^*`, `T_13^*`, `T_14^*` is not finite on the frozen
   selector;
7. the selector's decoration-only margin or pre-`T_13` margin is nonpositive;
   for the standard unit-collar `SEL0` branch this is `M_loss^SEL0<=0` or
   `M_pre13^SEL0<=0`, and the finite-template enumeration already proves
   `M_loss^SEL0<=0`; for the corner-separated `SEL1` branch with the standard
   unit area-collar convention, Theorem 4.3A.13 proves `M_loss^SEL1<=0`;
   for any later `SEL2`, Theorem 4.3A.16 requires the exact variable-activity
   inequality
   `C_dec,act^SEL2 < ((1-eta_*^SEL2)/eta_*^SEL2) log(1+Sig_AFM^SEL2)`, and
   Theorem 4.3A.21 reduces the actual source test to
   `P20-SEL2-CDEC-BOUND(C_U,C_L)` plus
   `eta_19^res < L_sig^SEL2/(C_U+L_sig^SEL2)`; for the concrete
   activity-optimized area-collar family, Theorem 4.3A.25 specializes this to
   `P20-SEL2-ACOL(C_area)` plus
   `eta_19^res < L_sig^SEL2/(C_area+L_sig^SEL2)`, and Theorem 4.3A.28 gives
   the sharp 4D bound `C_area<=20w_area^max` (`C_area=20` on the standard
   unit-counted normalization); Definition 4.3A.40 and Theorem 4.3A.41 name
   the exact `P20-SEL2-LFSRC` source audit needed for the required
   `delta_20^suff` large-field margin, Corollary 4.3A.42 imports it from the
   standard Paper-16 finite heat-kernel templates when their source hypotheses
   hold, Theorem 4.3A.49 closes Step 1 for the canonical `SEL2` source
   parameters, Lemma 4.3A.50 proves the strict worksheet inequality
   `bar_eta_res,20<tau_20`, and Theorem 4.3A.51 freezes the resulting
   `P20-SEL2(eta_ch,20^SEL2,20)` branch with full `C_area=20` decoration
   debit below `Sig_AFM^SEL2`;
8. `q_13^act>=1`, the leading-rate threshold fails, exact-entry transport
   fails, or exact scalar comparison fails; on the frozen unit-counted `SEL2`
   branch, Definition 4.3A.52 imports the concrete Paper-19 nonsurface
   transport source attacks, Theorem 4.3A.53 evaluates the nonsurface
   transport debit, Definition 4.3A.55 expands the full pre-surface scoreboard,
   Theorems 4.3A.56--4.3A.58 certify Steps 1--4 when the nonsurface upper
   package lies below the post-decoration margin, Theorems 4.3A.60--4.3A.65
   attack the package component by component, Corollaries 4.3A.66--4.3A.68
   isolate the easy-zero branch and compute the aggregate surplus, Theorem
   4.3A.69 records that the current imports reduce but do not automatically
   prove the required zero tail tests, Definition 4.3A.70 and Theorem 4.3A.71
   evaluate the surviving reduced `T_11` block on the same `SEL2` record law,
   Definition 4.3A.72 and Theorem 4.3A.73 evaluate the exact-entry transport
   residual as the six Paper-13 actual-entry gate defects on that same record
   law, Corollary 4.3A.74 rejects the unconditional easy-zero shortcut for the
   standard `SEL2` branch and gives the carried-forward aggregate bound,
   Corollary 4.3A.75 computes the resulting standard pre-surface surplus
   `Pi_pre13,std^SEL2`,
   Definitions 4.3A.76--4.3A.77 freeze the exact standard reduced branch and
   regroup the surviving nonsurface terms into the three buckets
   `U_EZ^SEL2`, `U_11^red,SEL2`, and `U_13^entry,red,SEL2`,
   Theorem 4.3A.78 performs the five-step computation and reduces the pass to
   `Pi_pre13,std,red^SEL2>0`, and Corollary 4.3A.79 records that this final
   sign is not decided by the current imports,
   Definition 4.3A.80 then splits `U_EZ^SEL2` into the priority block
   `E_14^SEL2+E_corn^SEL2+X_13^exact,SEL2` and the four reduced `T_12`
   tails, Theorems 4.3A.81--4.3A.82 give the exact zero tests for those seven
   easy-zero components, and Corollary 4.3A.83 records that the present
   imports decompose but do not annihilate this bucket,
   Definition 4.3A.84 isolates the stronger Paper-14 tail-normalized export
   audit `P20-SEL2-P14-ZERO`, Theorem 4.3A.85 proves that audit would set
   `E_14^SEL2=0`, and Corollary 4.3A.86 decides the present branch: carry
   finite `E_14^SEL2` unless that stronger audit is supplied,
   Definition 4.3A.87 expands that audit into the nine Paper-14 component
   rate estimates plus the cofinal tail-reading map, Theorem 4.3A.88 proves
   the component audit closes `P20-SEL2-P14-ZERO`, Corollary 4.3A.89 imports
   Paper 14's admissible rate-class sufficient condition, and Corollary
   4.3A.90 records that the present source papers still do not prove those
   actual component rates for four-dimensional `SU(N)`, while Corollary
   4.3A.91 parks this zero route and fixes the active branch to carry finite
   `E_14^SEL2` in `U_EZ^SEL2`,
   Definition 4.3A.92 audits the endpoint/corner finite-template register,
   Lemma 4.3A.93 gives the four-slot corner count, Theorem 4.3A.94 proves
   `E_corn^SEL2 <= (16+N_conc^SEL2)v_corn^max`, Theorem 4.3A.95 rejects
   zero on the standard corner-separated branch absent a zero-weight,
   empty-template, or new-selector audit, and Corollary 4.3A.96 records the
   active carried finite `E_corn^SEL2` debit,
   Definition 4.3A.97 defines the same-record cutoff-to-exact scalar audit
   for `X_13^exact,SEL2`, Lemma 4.3A.98 supplies the required diagonal
   finite-battery criterion for moving row batteries, Theorem 4.3A.99 proves
   the zero/carry decision, and Corollary 4.3A.100 records the active
   `U_EZ^SEL2` decision after steps 1--2,
   Definition 4.3A.101 defines the signed `SEL2` perimeter/cusp residuals,
   Lemma 4.3A.102 proves the four-slot Creutz perimeter and right-angle cusp
   residuals vanish, Definition 4.3A.103 names the finite perimeter/cusp tail
   bound audit, Theorem 4.3A.104 proves the zero-or-bound decision for
   `A_12^per` and `A_12^cusp`, and Corollary 4.3A.105 records the sharpened
   active `U_EZ` bucket after the perimeter/cusp attack,
   Definition 4.3A.106 states the `SEL2` smearing collar-window audit,
   Definition 4.3A.107 gives the finite and zero smearing-tail audits,
   Theorem 4.3A.108 proves that a collar-safe diagonal smearing-removal
   schedule gives `A_12^smear=0`, and Corollary 4.3A.109 records the active
   bucket after the smearing attack,
   Definitions 4.3A.110--4.3A.113 split `A_12^app` into the Paper-12
   residual modulus tail, the loop-representative tail, and the scalar
   binning tail, Theorem 4.3A.114 proves the component zero-or-bound decision,
   and Corollary 4.3A.115 records the fully split reduced `T_12` bucket,
   Definition 4.3A.116 assembles those six subtails into one
   `U_12^{red,SEL2}` package and one zero gate `P20-SEL2-T12-ZERO`, while
   Theorem 4.3A.117 closes step 1 by reducing the active `U_EZ` bucket to
   either `E_14+E_corn+X_13+U_12^{red}` or, on the zero branch,
   `E_14+E_corn+X_13`,
   Definition 4.3A.118 defines the corresponding post-step-1 surplus branches
   `Pi_pre13,std,red^{SEL2,step1}` and
   `Pi_pre13,std,red^{SEL2,step1zero}`, and Theorem 4.3A.119 gives the
   recomputed scalar pass tests, including the active corner bound
   `(16+N_conc^{SEL2})v_corn^max`,
   Definition 4.3A.120 splits `X_13^exact,SEL2` into its cutoff-to-exact
   block-convergence debit and its scalar readout debit, Definitions
   4.3A.121--4.3A.122 name the corresponding zero and carried-bound audits,
   Theorem 4.3A.123 proves the exact zero-or-sharp-bound decision, and
   Corollaries 4.3A.124--4.3A.125 update the post-`X_13` surplus branches
   and record the honest status: the current imports do not prove the moving
   SEL2 exact-entry battery convergence, so the active branch must carry
   either `X_13^{sharp,SEL2}` or the separated bound
   `U_13^{cut,SEL2}+U_13^{read,SEL2}` unless the new audits are supplied,
   Definition 4.3A.126 freezes that choice as the active carried value
   `X_13^{car,SEL2}`, Definition 4.3A.127 freezes the active finite
   `E_14^{car,SEL2}` and `E_corn^{car,SEL2}` debits, Definition 4.3A.128 and
   Theorem 4.3A.129 import the already evaluated reduced `T_11` source package
   into this active branch without double charging, and Corollaries
   4.3A.130--4.3A.131 give the active steps-1--3 surplus
   `Pi_pre13,std,red^{SEL2,1--3}` and record that the next unpaid nonsurface
   term is `U_13^{entry,red,SEL2}`,
   Definition 4.3A.132 expands that exact-entry term into the six Paper-13
   residuals `BC`, `CE`, `RPF`, `KPdec`, `SUB`, and `WP`, Lemma 4.3A.133
   identifies the corresponding Paper-13 source routes, Theorem 4.3A.134
   proves the active reduced entry bound with `SUB` deferred to the final
   surface-rate test, and Corollaries 4.3A.135--4.3A.136 give the post-entry
   surplus `Pi_pre13,std,red^{SEL2,entry}` and record that the remaining
   nonsurface obstruction is now the five same-record gates
   `BC`, `CE`, `RPF`, `KPdec`, and `WP`,
   Definition 4.3A.137 and Theorem 4.3A.138 compute this post-entry surplus
   explicitly as
   `underline M_loss^{SEL2,20}-U_post^{SEL2,entry}`, equivalently
   `Sig_AFM^{SEL2}-D_dec^{SEL2,20}` minus the active carried nonsurface
   debits, and Corollary 4.3A.139 gives the exact scalar decision: the branch
   reaches the final surface-rate comparison only if the active carried debit
   is strictly below `underline M_loss^{SEL2,20}`,
   Definition 4.3A.140 isolates the active `BC` row battery and its
   block-limit oscillation, Lemma 4.3A.141 proves compactness gives only the
   finite fallback bound `U_13^{BC,car}<=2B_BC^{SEL2}`, Definition 4.3A.142
   names the moving-battery block-limit uniqueness audit
   `P20-SEL2-BC-BLU`, Theorem 4.3A.143 proves `BC` zero is exactly this
   moving-battery `BLU`, and Corollary 4.3A.144 records the determining
   identity route and the honest status: current source imports do not prove
   `BLU` for four-dimensional `SU(N)` on the active `SEL2` tower,
   Definition 4.3A.145 isolates the active `CE-REG` target, Lemma 4.3A.146
   proves smooth central densities have finite weighted character tails,
   Lemma 4.3A.146A proves the hypercubic `SEL2` plaquette readout is a
   submersion, Theorem 4.3A.147 proves the finite heat-kernel rows give
   central `L^1` Peter-Weyl regularity with rowwise finite weighted tail,
   Corollaries 4.3A.148--4.3A.149 record the exact weak-limit boundary,
   Definition 4.3A.150 and Theorem 4.3A.151 add the heat-regularized weak
   limit route `CE-REG-HSM(\tau)`, Definition 4.3A.152 isolates the required
   de-smearing debit, and Theorem 4.3A.153 gives the explicit heat-trace tail
   bound and the coefficient fork: regularity and finite tail can be proved
   for every central weak plaquette law after heat-character smoothing, but
   exact unsmoothed closure still needs de-smearing plus the real
   coefficient sign/subunit/rate estimate; Audit 4.3A.154A proves that the
   active source chain uses the raw Haar coefficient `k_\rho`, Corollary
   4.3A.154B isolates the dimension-normalized fork as a different route
   requiring `P20-SEL2-NORM-SURF`, and Definitions 4.3A.155--4.3A.164,
   Theorems 4.3A.158--4.3A.165, and Corollary 4.3A.166 then execute the
   six-step `CE-SIGN/UNIT/RATE/DESMEAR/TAIL` attack: regularity alone is
   shown insufficient by explicit central-density counterexamples, sign is
   reduced to a same-record scalar-sheet witness, raw unit is reduced by
   Definition 4.3A.160A and Theorems 4.3A.160B--4.3A.160C to the effective
   block-time threshold
   `liminf t_eff > 2 log(d_rho)/C_2(rho)`, Definitions 4.3A.160E--4.3A.160F
   and Theorems 4.3A.160G--4.3A.160H sharpen this into the intrinsic
   block-time fork: raw `CE-UNIT/RATE` passes under `BTIME-LIFT` and fails
   under `BTIME-COLLAPSE`, while Corollary 4.3A.160I records that current
   source imports prove neither side; Lemma 4.3A.160J proves finite
   pushforward plus centrality/regularity/same-record bookkeeping cannot
   decide the fork, Definition 4.3A.160K names the active parking convention,
   Theorem 4.3A.160L parks the raw branch for the current sources, and
   Definitions 4.3A.160M--4.3A.160P open the normalized-surface fork, proving
   that a pure algebraic `k_\rho/d_\rho` rewrite gives no gain and that a real
   normalized route requires a same-record surface theorem with dimension
   surcharge strictly below `log d_\rho`; Audit 4.3A.160Q, Lemma
   4.3A.160R, and Corollaries 4.3A.160S--4.3A.160T then freeze the exact
   normalized Wilson-loop convention and prove the one-plaquette Schur
   gluing identity, Theorem 4.3A.160V and Corollary 4.3A.160W lift this to
   clean rho-monochromatic disk surfaces with zero dimension surcharge,
   Corollary 4.3A.160X reduces the normalized route to the non-clean
   remainder audit `P20-SEL2-NORM-SURF-EXT-REM`, and Definition
   4.3A.160Y--Corollary 4.3A.160AE decide that audit: corners,
   non-leading channels, decoration regrouping, real pairing, and pushforward
   add no dimension surcharge, while self-touching/local replacement
   recoupling is zero on the active reduced `SEL2` support convention and is
   otherwise carried by the finite fallback `r_rec log C_rec`; Definition
   4.3A.160AF and Theorem 4.3A.160AG then split the normalized leading-rate
   audit from the raw one and prove the exact pass/fail fork: a positive
   normalized effective block time gives `P20-SEL2-CE-NORM-RATE`, while
   collapse of that effective time to zero falsifies it, and Corollary
   4.3A.160AH records that the current source imports prove neither branch;
   Lemma 4.3A.160AI--Corollary 4.3A.160BJ then reduce that normalized
   block-time source to the one-block non-identity escape audit
   `P20-SEL2-NORM-ESC`, prove that escape closes normalized rate, and prove
   that collapse of all escape sets is equivalent to
   `\widetilde a_{\rho,j}^{SEL2}->1`; the same passage proves that the current
   large-field/residual imports neither supply the escape lower bound nor the
   same-target collapse comparison needed to prove collapse, then freezes the
   convolution reference time `T_j^{SEL2,conv}` and proves exact same-target
   coefficient comparison from the defect audit `P20-SEL2-CONV-CMP`, evaluates
   `T_j^{SEL2,conv}` as positive on the standard AF-area selector, and then
   replaces the overstrong real four-dimensional total-variation target by the
   scalar source `P20-SEL2-4DCOEFF-CLOSE`; the scalar correction is then
   split into nonbulk finite-template terms and the bulk Bianchi/off-sheet
   envelope, with a finite-gap pass test if the bulk envelope is small enough;
   de-smearing is proved from representation-tail tightness, and the exact
   non-leading tail is proved from a uniform Sobolev source or left as a
   named source audit,
   and Theorem 4.3A.39 then reduces the surviving surface bucket to
   `kappa_13^CE >
   h_13^SEL2+d_13^{SEL2,20}
   +log(1+M_13^{surf,SEL2}/underline M_pre13^{SEL2,20})`;
9. `L_AFM^sharp>=Sig_AFM`, or the component source bound is too large to
   prove a strict loss margin.

Proof.

These are precisely the negations of the pass gates in Sections 1--5,
written with the Paper-19 disjoint debit register. `square`

## 7. Work Plan

The execution order is:

1. freeze `P20-FROZEN-SEL`;
2. instantiate the first worksheet `P20-SEL0`;
3. prove or fail `P20-NOSMUGGLE`: verify that the frozen selector is
   structural only and does not already contain `R_H^opt<R_H^crit`,
   `L_AFM^sharp<Sig_AFM`, or area-law input;
4. start the first-selector coefficient estimate by fixing
   `P20-SEL0-COEFF-SRC`, `K_0^src`, and the margin `M_CE^(0)`;
5. attack `K_HK^(0)` first by choosing fixed-time or matched-time before
   any source constants are summed;
6. evaluate `K_proj^(0),K_chart^(0),K_ct^(0),K_vol^(0),K_tail^(0)` on the
   same branch and test `R_H^opt<R_H^crit`;
7. freeze the `P20-SEL0` loss worksheet and evaluate `Sig_AFM^{SEL0}`;
8. close `P20-DEC-SRC` by re-evaluating
   `eta_res^*,eta_ch^*,c_Delta^*` on that selector;
9. compute the residual transport margin `M_loss^SEL0`;
10. instantiate `P20-SEL0-TR-COMMON`;
11. evaluate `T_11^SEL0`, `T_12^SEL0`, and `T_14^SEL0`;
12. run the finite collar enumeration for the standard unit-collar `SEL0`
    template;
13. if `P20-SEL0-UCOL` holds, retire the standard `SEL0` branch by Corollary
    4.3A.9;
14. instantiate the replacement corner-separated selector `P20-SEL1`;
15. prove `P20-SEL1-NOSMUGGLE`;
16. recompute the `SEL1` decoration bottleneck using
    `C_dec^SEL1=C_xi^SEL1` and the added endpoint/corner debit
    `E_corn^SEL1` in `T_12`;
17. if the standard unit area-collar enumeration `P20-SEL1-ACOL` holds, retire
    `SEL1` by Theorem 4.3A.13;
18. record the standard-selector failure ledger and the admissibility test for
    any viable `SEL2`;
19. freeze the activity-optimized selector family
    `P20-SEL2(eta_ch,C_area)` and prove `P20-SEL2-NOSMUGGLE`;
20. run the finite same-record area-collar audit
    `P20-SEL2-ACOL(C_area)`, hence
    `P20-SEL2-CDEC-BOUND(C_area,1)`;
21. test the actual residual source inequality; for the unit-normalized branch
    this is closed by Theorem 4.3A.31 if the clean large-field source is
    available at
    `delta_20^suff=log(1+2C_KP(20+L_sig)/L_sig)`;
22. instantiate the same-record `P20-SEL2-LFSRC` audit; Theorem 4.3A.49 closes
    Step 1 for the canonical Paper-16 finite-template source parameters;
23. freeze the explicit worksheet
    `delta_20,bar_eta_res,20,tau_20,eta_ch,20^SEL2,widehat eta_*,20` by
    Definition 4.3A.43, with Lemma 4.3A.50 proving
    `bar_eta_res,20<tau_20` for every `epsilon_lf>0`;
24. freeze the resulting actual `P20-SEL2(eta_{ch,20}^{SEL2},20)` branch;
    Theorem 4.3A.51 imports Theorem 4.3A.44 and proves
    `exp(20 eta_*^SEL2/(1-eta_*^SEL2))-1<Sig_AFM^SEL2`;
25. instantiate `P20-SEL2-TR-COMMON` and `P20-SEL2-TRANSPORT-SRC`; Theorem
    4.3A.53 evaluates
    `T_11^SEL2,T_12^SEL2,T_14^SEL2,A_13^entry,SEL2,A_13^exact,SEL2`, and
    Definition 4.3A.55 expands the full `\mathcal M_{pre13}^{SEL2}` scoreboard;
26. attack `U_pre13^SEL2` component by component using Theorems
    4.3A.60--4.3A.65: reduced `T_12`, exact comparison, Paper-14 export,
    reduced `T_11`, and exact-entry transport; Theorem 4.3A.58 gives the
    aggregate upper-bound pass test, Corollary 4.3A.68 computes the resulting
    scalar surplus `Pi_pre13^SEL2`, Theorem 4.3A.69 decides the easy-zero
    attempt by reducing it to five explicit cofinal zero tests plus the
    endpoint/corner convention, Definition 4.3A.70 and Theorem 4.3A.71
    evaluate the surviving reduced `T_11` block and its zero tests, and
    Definition 4.3A.72 and Theorem 4.3A.73 evaluate `U_13^entry` as the six
    actual-entry residuals
    `BC,CE,RPF,KPdec,SUB,WP`, and Corollary 4.3A.74 decides that the
    standard `SEL2` branch must carry the evaluated `T_12`, `A_13^exact`,
    `E_14`, and `E_corn` terms unless their separate zero estimates are
    proved, and Corollary 4.3A.75 computes the resulting standard surplus
    `Pi_pre13,std^SEL2`; Definitions 4.3A.76--4.3A.77 freeze the standard
    reduced branch and regroup the surviving terms, Theorem 4.3A.78 executes
    the requested five-step computation, and Corollary 4.3A.79 records the
    honest decision: Steps 1--4 are closed as reductions, while Step 5 is
    exactly the unresolved strict sign test
    `U_EZ^SEL2+U_11^red,SEL2+U_13^entry,red,SEL2
    < underline M_loss^{SEL2,20}`; Definition 4.3A.80 and Theorems
    4.3A.81--4.3A.82 attack `U_EZ^SEL2` first, in the order
    `E_14`, `E_corn`, `X_13^exact`, then the four reduced `T_12` tails, and
    Corollary 4.3A.83 records the resulting seven same-record source tests;
    Definition 4.3A.84, Theorem 4.3A.85, and Corollary 4.3A.86 complete step
    1 of that attack by proving `E_14^SEL2=0` from the stronger
    `P20-SEL2-P14-ZERO` audit and otherwise requiring the finite Paper-14
    debit to be carried; Definition 4.3A.87, Theorem 4.3A.88, and
    Corollaries 4.3A.89--4.3A.90 make the further investigation componentwise:
    nine Paper-14 defect rates plus a cofinal row-tail map are sufficient, but
    not currently proved by the imported source papers; Corollary 4.3A.91
    parks the zero route and defines the active carried-debit surplus
    `Pi_pre13,std,red^SEL2,park`; Definition 4.3A.92, Lemma 4.3A.93,
    Theorems 4.3A.94--4.3A.95, and Corollary 4.3A.96 attack `E_corn^SEL2`,
    give the explicit finite bound
    `E_corn^SEL2 <= (16+N_conc^SEL2)v_corn^max`, and decide that zero is not
    available on the standard corner-separated branch without an additional
    zero-weight, empty-template, or new-selector audit; Definition 4.3A.97,
    Lemma 4.3A.98, Theorem 4.3A.99, and Corollary 4.3A.100 then complete
    step 2 of the `U_EZ` attack by reducing `X_13^exact,SEL2` to a diagonal
    finite-battery cutoff-to-exact audit plus vanishing readout tolerance, or
    else to a finite carried debit `A_X^SEL2`; Definition 4.3A.101, Lemma
    4.3A.102, Definition 4.3A.103, Theorem 4.3A.104, and Corollary
    4.3A.105 then attack the calibrated perimeter/cusp tails: the rectangular
    four-slot Creutz geometry cancels the scalar perimeter and right-angle
    cusp residuals exactly, so `A_12^per=A_12^cusp=0` on the same-branch
    cancellation audit, while the fallback route carries explicit finite
    bounds `U_12^{per,SEL2}` and `U_12^{cusp,SEL2}`; Definition 4.3A.106,
    Definition 4.3A.107, Theorem 4.3A.108, and Corollary 4.3A.109 then
    attack `A_12^smear`: the smearing radius must stay in the Paper-12
    collar window `a<<tau<<r_min`, and a diagonal finite-row schedule makes
    `sum_{k>=j} eta_smearLC,j,k^SEL2 -> 0`, otherwise a finite
    `U_12^{smear,SEL2}` debit is carried; Definitions 4.3A.110--4.3A.113,
    Theorem 4.3A.114, and Corollary 4.3A.115 finish the reduced `T_12`
    bucket by splitting `A_12^app` into
    `eta_P12+eta_appLC^(12)+eta_binLC^(12)`, proving the aggregate tail is
    zero when those three component tails vanish, and otherwise carrying the
    explicit finite bounds `U_12^{P12,SEL2}`, `U_12^{appLC,SEL2}`, and
    `U_12^{binLC,SEL2}`; Definition 4.3A.116 and Theorem 4.3A.117 assemble
    step 1 into the reusable package
    `U_12^{red,SEL2}=U_12^{per}+U_12^{cusp}+U_12^{smear}
    +U_12^{P12}+U_12^{appLC}+U_12^{binLC}`, with the zero branch named
    `P20-SEL2-T12-ZERO`; Definition 4.3A.118 and Theorem 4.3A.119 then
    complete step 2 by recomputing the active `U_EZ` and the two post-step-1
    surplus branches, with the conservative test
    `E_14+E_corn+X_13+U_12^red+U_11^red+U_13^entry < underline M_loss`
    and the zero-`T_12` test obtained by deleting `U_12^red`;
    Definitions 4.3A.120--4.3A.122 and Theorem 4.3A.123 then attack
    `X_13^exact,SEL2` itself: zero is available exactly from the same-record
    moving-battery cutoff-to-exact audit plus exact scalar readout, while the
    fallback branch carries the sharp debit `X_13^{sharp,SEL2}` or the
    separated upper bound `U_13^{cut,SEL2}+U_13^{read,SEL2}`; Corollaries
    4.3A.124--4.3A.125 recompute the post-`X_13` surplus and make explicit
    that the current source papers have reduced, not proved, this zero audit;
    Definitions 4.3A.126--4.3A.128 then freeze the active carried `X_13`,
    finite `E_14`/`E_corn`, and reduced `T_11` branches, Theorem 4.3A.129
    proves the active reduced `T_11` zero-or-bound test from Theorem 4.3A.71,
    and Corollaries 4.3A.130--4.3A.131 complete steps 1--3 by reducing the
    active pre-surface pass to
    `Pi_pre13,std,red^{SEL2,1--3}>0`, with
    `U_13^{entry,red,SEL2}` the next unpaid nonsurface bucket;
    Definition 4.3A.132, Lemma 4.3A.133, Theorem 4.3A.134, and Corollaries
    4.3A.135--4.3A.136 then attack that exact-entry bucket by expanding
    `epsilon_BC+epsilon_CE+epsilon_RPF+epsilon_KPdec+epsilon_SUB+epsilon_WP`,
    deferring `SUB` to the later surface-leading-rate test on the reduced
    branch, and reducing the active post-entry pass to
    `Pi_pre13,std,red^{SEL2,entry}>0`;
    Definition 4.3A.137, Theorem 4.3A.138, and Corollary 4.3A.139 compute
    that post-entry surplus explicitly and decide the scalar pass condition:
    the active carried nonsurface debit must be strictly less than
    `underline M_loss^{SEL2,20}`;
    Definition 4.3A.140, Lemma 4.3A.141, Definition 4.3A.142, Theorem
    4.3A.143, and Corollary 4.3A.144 then attack the first live entry gate
    `BC`: compactness gives a finite carry, but zero is equivalent to
    moving-battery block-limit uniqueness on the active `SEL2` row records;
    the named noncircular route is the Paper-13 determining-identity audit,
    which is not currently proved by the source papers;
    Definition 4.3A.145, Lemma 4.3A.146, Lemma 4.3A.146A, Theorem 4.3A.147,
    and Corollaries 4.3A.148--4.3A.149 then close `CE-REG` on the finite
    heat-kernel row branch and mark the exact weak-limit boundary; Definition
    4.3A.150, Theorem 4.3A.151, Definition 4.3A.152, Theorem 4.3A.153, and
    Corollary 4.3A.154 then extend the attack creatively: every central weak
    plaquette law has a heat-regularized smooth central density with explicit
    finite heat-trace character tail, while the exact theorem must still pay
    `CE-DESMEAR` and prove the leading coefficient sign/subunit/rate without
    area-law input; Audit 4.3A.154A and Corollary 4.3A.154B perform the
    coefficient-normalization audit, proving that the active source chain
    uses the raw Haar coefficient and that the dimension-normalized
    coefficient is a separate `NORM-SURF` route, not a silent substitution;
    Definitions 4.3A.155--4.3A.164, Theorems
    4.3A.158--4.3A.165, and Corollary 4.3A.166 then do that attack in order:
    freeze the real scalar coefficient convention, prove regularity alone
    cannot imply sign/unit/rate, give concrete non-area-law sign and spread
    witnesses, reduce raw `CE-UNIT` to the effective block heat-time
    threshold `t_eff>2 log(d_rho)/C_2(rho)`, introduce the intrinsic
    block-time fork `BTIME-LIFT` versus `BTIME-COLLAPSE`, prove that finite
    pushforward alone does not decide that fork, park the active raw branch
    until a new lift or collapse source is supplied, open the normalized
    surface fork and show that it helps only if the per-excess
    dimension-surcharge is strictly below `log d_rho`, freeze the normalized
    Wilson-loop convention, prove the one-plaquette Schur gluing identity
    giving local sheet weight `k_rho/d_rho`, lift that identity to clean
    rho-monochromatic disk surfaces, reduce the remaining normalized work to
    the non-clean/corner/decoration remainder audit, close that audit with
    zero dimension surcharge on the active reduced `SEL2` convention and a
    finite `r_rec log C_rec` fallback on the unreduced convention, split the
    raw and normalized positive-rate audits, reduce normalized rate first to
    `P20-SEL2-NORM-BTIME-LIFT(delta_rho,eta_rho)` and then to the one-block
    escape source `P20-SEL2-NORM-ESC`, prove zero de-smearing from
    representation-tail tightness, and close the exact non-leading tail from a
    uniform Sobolev source;
    Theorem 4.3A.47 gives the lower-floor failure test and the honest
    undecided region;
    if the certified margin is positive, apply Theorem 4.3A.39 to reduce
    `T_13` to the leading-rate threshold for `kappa_13^CE`;
27. close by Theorem 6.1 or record the exact obstruction by Theorem 6.2.

## 8. Current Status

Paper 20 has frozen the proof architecture and has closed the coefficient
headline on the clean matched-time exact-record `P20-SEL0` branch. It has
not yet closed the loss headline. Steps 1--3 of the work plan are complete
for the first selector. Definition 1.4 freezes the full `P20-SEL0` worksheet:
AF row, cofinal subsequence, `rho_0`, tolerances, centered square windows,
coefficient target, coefficient threshold, character cutoff, decoration
template, analytic residual import, transport debit register, and
pushed-forward scalar record law. Lemma 1.5 proves that this worksheet
instantiates `P20-FROZEN-SEL`, and Theorem 1.6 proves
`P20-SEL0-NOSMUGGLE`. Step 4 has also started: Definitions 2A.1--2A.2 now
fix the first-selector coefficient defect ledger, absorb the exact
`e^{a_j}` normalization into the six source constants, and define
`K_0^src` and `M_CE^(0)`. Theorems 2A.3--2A.4 prove the exact first-selector
coefficient fork:

```text
P20-SEL0-COEFF-SRC + M_CE^(0)>0
=> P20-COEFF-PASS,

K_0^src>=R_0^crit
=> this SEL0 coefficient route fails.
```

Step 5 has now started and the heat-kernel bucket is split into honest
branches. Definitions 2B.1--2B.3 define the Paper-20 normalized
decomposition

```text
K_HK^(0)
<= K_time^(0)+K_block^(0)+K_cross^(0)+K_extract^(0)
```

with the `e^{a_j}` normalization already included. Theorems 2B.4 and 2B.6
give the fixed-time and matched-time tests, respectively. The clean
Paper-19 local import proves the matched-time branch has

```text
B_0=C_0^res=X_0=0
=> K_HK,match^(0)=0.
```

This closes the heat-kernel bucket only on the declared matched-time clean
selector. It does not prove fixed-time `K_HK^(0)=0` and does not prove the
full coefficient pass by itself.

Step 6 has now been evaluated on the same matched-time exact-record branch.
Definition 2C.1 isolates the five exact remaining-bucket clauses:

```text
P20-SEL0-PROJ0, P20-SEL0-CHART0, P20-SEL0-CT0,
P20-SEL0-VOL0, P20-SEL0-TAIL0.
```

Lemma 2C.2 proves that these clauses give

```text
K_proj^(0)=K_chart^(0)=K_ct^(0)=K_vol^(0)=K_tail^(0)=0.
```

Together with the matched-time heat-kernel result, Theorem 2C.3 gives

```text
K_0^src=0,
M_CE^(0)=R_0^crit>0,
P20-COEFF-PASS.
```

This is not the full Paper-20 closure. The coefficient gate is now closed on
the clean matched-time exact-record selector.

Steps 7--8 have now also been completed on the same selector. Definition
3A.1 freezes the loss worksheet `P20-SEL0-LOSS`, Lemma 3A.2 evaluates the
thick-window geometry, and Definition 3A.3 gives the explicit positive
signal floor

```text
Sig_AFM^SEL0 =
exp(-n_+^SEL0 A_AFM^SEL0)
  [1-exp(-q_-^SEL0 B_AFM^SEL0)].
```

Theorem 3A.4 proves this is the Paper-19 signal floor specialized to the
clean matched-time selector. Theorem 3.4 then closes the decoration source:

```text
eta_res^SEL0 = eta_19^res,
eta_ch^SEL0 = (1-eta_19^res)/2,
c_Delta^SEL0 = C_xi^SEL0 + C_xip^SEL0,
P20-DEC-SRC(eta_res^SEL0, eta_ch^SEL0, c_Delta^SEL0).
```

Step 9 has now computed the residual transport margin. Definition 3.6 gives

```text
M_loss^SEL0 = Sig_AFM^SEL0 - D_dec^SEL0
```

and expands it entirely in the frozen constants
`alpha,epsilon_G,s,epsilon_A,chi,C_0,eta_19^res,C_xi^SEL0,C_xip^SEL0`.
The exact decoration-only positivity test is

```text
C_dec^SEL0
< [(1-eta_19^res)/(1+eta_19^res)] log(1+Sig_AFM^SEL0).
```

Thus the remaining work is the transport side and final scalar comparison:

```text
T_11^*, T_12^*, T_13^*, T_14^*,
T_11^* + T_12^* + T_13^* + T_14^* < M_loss^SEL0.
```

Step 10 has now instantiated the transport common-record audit for `SEL0`.
Definition 4.0A defines `P20-SEL0-TR-COMMON` as the Paper-20 version of
Paper 19 `P19-TR-COMMON`: one whole-process scalar record tower, one
Paper-16 heat-kernel tower after pushforward, one certificate family, one
same-battery Paper-14 export chain, one disjoint debit register, and no hidden
gauge-fixed or local-field subprocess. Theorem 4.0B proves that

```text
P20-SEL0
+ P20-SEL0-LOSS
+ HK-WP-CLOSE on the identified Paper-16 tower
+ same-battery Paper-14 export
+ declared disjoint debit assignment
=> P20-SEL0-TR-COMMON
=> P19-TR-COMMON on SEL0.
```

This is only a same-record compatibility audit; it does not assert a transport
margin, a surface subcriticality estimate, or an area law.

Step 11 has now evaluated the linear transport ceilings on the common `SEL0`
record law. Definition 4.3 and Theorem 4.3B give

```text
T_11^SEL0 =
 A_11^loc,SEL0+A_11^RP,SEL0+A_11^Cov,SEL0+A_11^gauge,SEL0,

T_12^SEL0 =
 A_12^per,SEL0+A_12^cusp,SEL0+A_12^smear,SEL0+A_12^app,SEL0,

T_14^SEL0 = E_14^SEL0.
```

Here the four `A_11` terms are the reduced local-RG/RP/covariance/gauge
limsups, the four `A_12` terms are the reduced Paper-12/Paper-16
loop-continuity limsups, and `E_14^SEL0=limsup_j||E_14(eta_j)||_tr`.
Projective, regulator, and volume terms are not double charged into `T_12`.

Definition 4.3A now signs the two margins as exact scalar tests. The residual
margin satisfies

```text
M_loss^SEL0>0
iff
C_dec^SEL0 < [(1-eta_19^res)/(1+eta_19^res)] log(1+Sig_AFM^SEL0).
```

After the linear ceilings and the non-surface `T_13` debits are charged,
define

```text
M_pre13^SEL0 =
M_loss^SEL0
-T_11^SEL0-T_12^SEL0-T_14^SEL0
-A_13^entry,SEL0-A_13^exact,SEL0.
```

Then

```text
M_pre13^SEL0>0
iff
L_pre13^SEL0<Sig_AFM^SEL0
and
C_dec^SEL0
< [(1-eta_19^res)/(1+eta_19^res)]
  log(1+Sig_AFM^SEL0-L_pre13^SEL0).
```

Thus the current source papers do not numerically sign the margins yet; they
reduce the sign decision to these two inequalities. Theorem 4.3A.4 records the
exhausted sharp source-constant bound:

```text
M_loss^SEL0>0
iff
C_xi^SEL0+C_xip^SEL0
  < [(1-eta_19^res)/(1+eta_19^res)] log(1+Sig_AFM^SEL0),
```

and the same test with `Sig_AFM^SEL0-L_pre13^SEL0` decides
`M_pre13^SEL0`. In particular, `C_xi^SEL0+C_xip^SEL0>=log 2` would already
kill the `SEL0` component route before the surface-polymer rate is tested.
Theorem 4.3A.5 then attacks this decoration bottleneck directly. It introduces
the actual template limsup

```text
C_dec,act^SEL0 = limsup_j(c_xi,j^*+c_xip,j^*)
```

and proves the exact pass/fail test

```text
C_dec,act^SEL0 < U_loss^SEL0       passes the pre-transport bottleneck,
C_dec,act^SEL0 >= U_loss^SEL0      fails before transport.
```

The current papers do not yet enumerate the exact centered-square collar cell
counts needed to decide this value. Under the standard unit-collar
normalization, any cofinal nonempty collar gives `C_dec,act^SEL0>=1`, hence
failure because `U_loss^SEL0<log 2<1`; but that unit-cell enumeration must be
proved as a finite-template statement before it is recorded as an unconditional
failure of the frozen `SEL0` route.

The finite-template enumeration is now explicit. Definition 4.3A.6 lists the
four centered-square Creutz slots and the five local collar template types.
Lemma 4.3A.7 proves that, under the standard Paper-15 unit-counting convention,
the nondegenerate rectangle `C_{++}` already contributes a nonempty
endpoint/corner collar unit. Hence

```text
C_dec,act^SEL0 >= 1.
```

Theorem 4.3A.8 therefore proves that the unit-collar `SEL0` route fails before
transport:

```text
C_dec,act^SEL0 >= 1 > log 2 > U_loss^SEL0
=> M_loss^SEL0 <= 0.
```

This is a failure of this frozen selector and collar normalization, not a
falsification of confinement. A different selector, or a different explicitly
declared collar normalization, could still be tested, but it must be declared as
a new frozen branch with its own no-smuggling audit and same-record source
constants.

Steps 13--15 have now been carried out at the structural level. Corollary
4.3A.9 retires the standard unit-collar `SEL0` branch as a closure route.
Definition 1.7 declares the replacement corner-separated selector `P20-SEL1`:
it keeps the clean matched-time coefficient data but moves finite
endpoint/corner collar effects out of the multiplicative decoration constant
and into the loop-readout transport debit `E_corn^{SEL1}`. Lemma 1.8 proves
that `P20-SEL1` instantiates `P20-FROZEN-SEL`, and Theorem 1.9 proves
`P20-SEL1-NOSMUGGLE`.

Step 16 is now decided for the standard area-collar normalization. The exact
`SEL1` scalar test is

```text
C_dec,act^SEL1 = limsup_j c_xi,j^{*,SEL1}
?<
U_loss^SEL1,
```

where

```text
U_loss^SEL1 =
[(1-eta_19^res)/(1+eta_19^res)] log(1+Sig_AFM^SEL1)
= U_loss^SEL0 < log 2 < 1.
```

Theorem 4.3A.10 proves this exact iff. Definition 4.3A.11 then freezes the
standard Paper-15 unit area-collar enumeration for `SEL1`, and Lemma 4.3A.12
proves the cofinal lower bound

```text
C_dec,act^SEL1 >= 1.
```

Therefore Theorem 4.3A.13 falsifies the `SEL1` decoration inequality under the
standard unit area-collar convention:

```text
C_dec,act^SEL1 >= 1 > log 2 > U_loss^SEL1
=> M_loss^SEL1 <= 0.
```

This means the endpoint/corner reassignment was not enough. It removes
`C_xip` from the multiplicative decoration debit, but the area-charged
plaquette-collar constant `C_xi` alone already exceeds the available loss
threshold when it is counted in unit Paper-15 cells. This is a failure of the
standard `SEL1` route, not a falsification of confinement.

Step 18 is now also recorded. Corollary 4.3A.14 gives the compact branch
ledger:

```text
standard SEL0 fails by endpoint/corner unit decoration,
standard SEL1 fails by area-collar unit decoration.
```

Definition 4.3A.15 then states what a viable activity-optimized `SEL2` must
prove. The canonical half-margin is no longer mandatory: `SEL2` may choose any
strict character-tail budget supplied by Paper 19 Theorem 8L.8A. The exact
variable-activity gate is now Theorem 4.3A.16:

```text
C_dec,act^SEL2
<
[(1-eta_*^SEL2)/eta_*^SEL2] log(1+Sig_AFM^SEL2),

eta_*^SEL2 = eta_19^res + eta_ch^SEL2.
```

Equivalently, with `L_sig^SEL2=log(1+Sig_AFM^SEL2)`,

```text
eta_*^SEL2 < L_sig^SEL2/(C_dec,act^SEL2+L_sig^SEL2).
```

Corollary 4.3A.17 imports the character-tail optimization theorem: if the
residual activity already satisfies

```text
eta_19^res < L_sig^SEL2/(C_dec,act^SEL2+L_sig^SEL2),
```

then one can choose `eta_ch^SEL2>0` small enough that the decoration-only gate
passes, provided the declared `C_dec,act^SEL2` is a genuine same-record scalar
constant. Conversely, if the residual activity is at or above that threshold,
no character-tail cutoff can save the branch.

The actual residual side has now been unfolded. Definition 4.3A.18 substitutes
the Paper-19/Paper-16 residual activity

```text
eta_19^res =
C_KP A_res exp(-Delta r_res)/(1-exp(-Delta))
```

and proves the exact scalar target

```text
C_KP A_res exp(-Delta r_res)/(1-exp(-Delta))
< L_sig^SEL2/(C_dec,act^SEL2+L_sig^SEL2).
```

Theorem 4.3A.19 gives the clean Paper-16 sufficient source bound: if
`C_dec,act^SEL2<=C_U`, it is enough to find a finite-range margin `delta>0`
with the large-field source available at `h_KP+m+delta` and

```text
2C_KP exp(-delta r_res^clean)/(1-exp(-delta))
< L_sig^SEL2/(C_U+L_sig^SEL2).
```

Definition 1.10 now freezes the activity-optimized selector family
`P20-SEL2(eta_ch,C_area)`, Lemma 1.11 proves that each audited instance is a
frozen selector, and Theorem 1.12 proves the no-smuggling audit. Definition
4.3A.20 names the finite-template audit `P20-SEL2-CDEC-BOUND(C_U,C_L)`.
Definition 4.3A.23 specializes it to the concrete area-collar enumeration
`P20-SEL2-ACOL(C_area)`, and Lemma 4.3A.24 proves

```text
P20-SEL2-CDEC-BOUND(C_area,1).
```

Theorem 4.3A.25 combines this with the residual source bound. Thus the
remaining non-dead path is now an explicit two-scalar task:

```text
audit w_area^max on the same record law,
prove eta_19^res < L_sig^SEL2/(20w_area^max+L_sig^SEL2).
```

Theorem 4.3A.28 now supplies the sharp hypercubic finite-template upper bound
`C_area<=20w_area^max`, and the standard unit-counted branch may take
`C_area=20`. Corollary 4.3A.29 therefore reduces the unit-counted residual gate
to

```text
eta_19^res < L_sig^SEL2/(20+L_sig^SEL2),
```

or, on the clean Paper-16 residual branch,

```text
2C_KP exp(-delta r_res^clean)/(1-exp(-delta))
< L_sig^SEL2/(20+L_sig^SEL2).
```

The residual inequality has now been tested symbolically. Definition 4.3A.30
defines

```text
delta_20^suff
= log(1+2C_KP(20+L_sig^SEL2)/L_sig^SEL2).
```

Theorem 4.3A.31 proves that, if the clean large-field source is available at
`h_KP+m+delta` for some `delta>delta_20^suff` and the AF tail is restricted as
in Paper 16 Theorem 9N.1Q.1, then

```text
eta_19^res < L_sig^SEL2/(20+L_sig^SEL2).
```

Thus the `C_area=20` residual gate is not a remaining scalar obstruction under
the clean adjustable-rate Paper-16 hypotheses. The next obstruction, if any, is
the availability of that large-field rate on the same record law, or else the
later full decoration debit after choosing `eta_ch^SEL2`.

The large-field source has now been audited at the correct level of honesty.
Theorem 4.3A.33 proves that Paper 16 supplies the required

```text
sigma_lf^sharp >= h_KP+m+delta
with delta>delta_20^suff
```

whenever the same-record finite `HK-LF-SRC` source clauses hold: the
collar-adapted denominator source, the finite large-field coefficient
representation source, the block-polymer entropy bound, and the cofinal
AF-tail choice. The theorem does not hide these clauses; if one of them fails,
the failure is now localized to the Paper-16 large-field source import.

Assuming those same-record clauses hold, Definition 4.3A.34 chooses the actual
character-tail budget

```text
eta_ch,20^SEL2=(tau_20-bar_eta_res,20)/2,
```

where

```text
bar_eta_res,20
=2C_KP exp(-delta_20(epsilon_lf) r_res^clean)
 /(1-exp(-delta_20(epsilon_lf))).
```

Theorem 4.3A.35 then freezes `P20-SEL2(eta_{ch,20}^{SEL2},20)`, imports
`P19-CHTAIL-AUDIT(eta_ch,20^SEL2)` from Paper 19 Theorem 8L.8A, and proves the
full pre-transport decoration pass

```text
exp(20 eta_*^SEL2/(1-eta_*^SEL2))-1 < Sig_AFM^SEL2.
```

So, under the finite same-record `HK-LF-SRC` source clauses, the `SEL2`
decoration bottleneck is closed. The remaining work is no longer the
decoration algebra; it is the transport side and the nonlinear `T_13`
leading-rate comparison on the frozen `SEL2` branch.

That transport side has now been pushed to the same scalar form as the
decoration side. Definition 4.3A.36 defines `P20-SEL2-TR-COMMON`, and Theorem
4.3A.37 shows that it instantiates the Paper-19 transport common-record audit
whenever the Paper-16 and Paper-14 exports are read on the same frozen `SEL2`
record law with the declared disjoint debit assignment.

Definition 4.3A.38 then defines the certified post-decoration margin

```text
underline M_loss^SEL2,20
= exp(L_20)-exp(20 widehat_eta_*,20/(1-widehat_eta_*,20)) > 0,
```

the linear transport ceilings `T_11^SEL2,T_12^SEL2,T_14^SEL2`, the non-surface
debit `L_pre13^SEL2`, and the certified pre-surface margin

```text
underline M_pre13^SEL2,20
= underline M_loss^SEL2,20 - L_pre13^SEL2.
```

Theorem 4.3A.39 gives the next scalar fork once the pre-surface margin is
certified positive. If the upper-bound margin
`underline M_pre13^SEL2,20` is positive, the only remaining nonlinear loss
condition is the leading-rate inequality

```text
kappa_13^CE
>
h_13^SEL2+d_13^SEL2,20
+ log(1+M_13^surf,SEL2/underline M_pre13^SEL2,20).
```

If the certified upper-margin is nonpositive, the current source ceiling does
not pass. Theorem 4.3A.47 records the sharper logic: genuine failure before
`T_13` requires a same-record lower floor consuming the post-decoration margin;
without such a lower floor, the route is only undecided at this stage.

For any future branch that does pass the decoration and pre-`T_13` margins, the
only nonlinear remaining bucket is `T_13`. Theorem 4.4 shows that if
`M_pre13>0` on that branch, the surface-polymer comparison is equivalent to the
leading-rate threshold

```text
kappa_13^CE
>
h_13
+ d_13
+ log(1+M_13^surf/M_pre13),
```

with

```text
h_13 = 3+log 20,
d_13 = C_xi eta_*/(1-eta_*).
```

Thus the four transport ceilings have been evaluated against the residual
margin as far as the current source constants permit. For the standard `SEL0`
and `SEL1` branches, the decoration enumeration already blocks the route before
this threshold is relevant. For a genuinely new branch, the same theorem
isolates which actual same-record constants must be made small enough, and
exactly how much `kappa_13^CE` must exceed the entropy-decoration threshold.

The first four `SEL2` execution steps are now written as source theorems rather
than informal next steps. Definition 4.3A.40 names the exact large-field source
audit `P20-SEL2-LFSRC`; Theorem 4.3A.41 proves that it supplies the Paper-16
large-field rate needed for the residual decoration gate; Corollary 4.3A.42
imports that audit from the standard finite heat-kernel template theorem when
the common metric, finite template ledger, and AF time tail are available; and
Theorem 4.3A.49 closes Step 1 for the canonical `SEL2` source parameters.

Definition 4.3A.43 then freezes the actual `SEL2` worksheet:

```text
delta_20,
bar_eta_res,20,
tau_20,
eta_ch,20^SEL2,
widehat eta_*,20,
underline M_loss^SEL2,20.
```

Lemma 4.3A.50 proves the strict scalar inequality
`bar_eta_res,20<tau_20` for every `epsilon_lf>0`, and Theorem 4.3A.51 freezes
the branch as a genuine `P20-SEL2(eta_ch,20^SEL2,20)` selector with full
decoration debit below `Sig_AFM^SEL2`.

Definition 4.3A.52 names the concrete nonsurface transport source package:
the four `T_11` attacks, the three reduced `T_12` attacks plus
`P19-T12-EVAL`, `P19-T13-ENTRY`, `P19-T13-EXACT`, and the Paper-14 export.
Theorem 4.3A.53 proves that this source package evaluates the same-branch
nonsurface ceilings:

```text
T_11^SEL2,
T_12^SEL2,
T_14^SEL2,
A_13^entry,SEL2,
A_13^exact,SEL2.
```

Finally, Theorem 4.3A.54 gives the rigorous Step-4 fork. The branch is
certified past the pre-`T_13` stage when

```text
\mathcal M_{pre13}^{SEL2}
= underline M_loss^SEL2,20 - L_pre13^SEL2
> 0.
```

It is genuinely failed at this stage only if a same-record lower floor
`L_pre13^SEL2,-` is proved with

```text
L_pre13^SEL2,- >= underline M_loss^SEL2,20.
```

If the upper ceiling is too weak but no lower floor is known, the status is
undecided, not falsified. That is the honest boundary before attacking the
final `kappa_13^CE` leading-rate inequality.

Steps 1--2 of the remaining post-SEL2 work are now also explicit. Definition
4.3A.55 expands the whole pre-surface scoreboard into one scalar expression:

```text
\mathcal M_{pre13}^{SEL2}
= exp(L_20)-exp(20 widehat_eta_*,20/(1-widehat_eta_*,20))
  - (T_11^SEL2 + T_12^SEL2 + T_14^SEL2
     + A_13^entry,SEL2 + A_13^exact,SEL2).
```

Theorem 4.3A.56 proves that this is exactly the Step-4 margin. Definition
4.3A.57 then names the nonsurface upper-bound package
`P20-SEL2-NS-UPPER(U_pre13^SEL2)`, and Theorem 4.3A.58 proves the clean pass
criterion:

```text
U_pre13^SEL2 < underline M_loss^SEL2,20
=> \mathcal M_{pre13}^{SEL2} > 0.
```

Corollary 4.3A.59 orders the remaining nonsurface work: reduced `T_12`,
`A_13^exact`, Paper-14 export, reduced `T_11`, then `A_13^entry`. Only after
this aggregate bound is below the margin should the paper spend the hard
effort on the leading central-character rate.

The component attack is now explicit. Theorem 4.3A.60 handles the reduced
`T_12` bucket and records its zero branch when the perimeter/cusp,
smearing-removal, and loop-approximant/readout tails vanish. Theorem 4.3A.61
handles `A_13^exact` and records the exact finite-battery/readout-zero route.
Theorem 4.3A.62 handles the Paper-14 export `E_14`. Theorem 4.3A.63 handles
the reduced `T_11` slots. Theorem 4.3A.64 handles the exact-entry transport
residuals, with the explicit warning that its finite `CE` residual is not the
later leading-rate constant `kappa_13^CE`. Theorem 4.3A.65 assembles these
component bounds into `P20-SEL2-NS-UPPER(U_pre13^SEL2)`.

The requested vanishing route is now isolated as an easy-zero package.
Corollary 4.3A.66 proves that cofinal vanishing of the reduced perimeter/cusp,
smearing, loop-approximant/readout, exact-comparison, and Paper-14 export
defects gives

```text
U_12^per = U_12^cusp = U_12^smear = U_12^app
          = U_13^exact = U_14 = 0,
```

with `U_corn=0` when endpoint/corner normalization remains inside the
decoration ledger. Corollary 4.3A.67 then reduces the pre-surface pass test to
the genuinely remaining terms:

```text
U_11^loc + U_11^RP + U_11^Cov + U_11^gauge
+ U_13^entry
< underline M_loss^SEL2,20
```

in the no-corner branch, with `+ U_corn` added only if the selector separates
endpoint/corner normalization from decoration.

The aggregate computation has also been frozen. Corollary 4.3A.68 defines

```text
U_11^Sigma = U_11^loc+U_11^RP+U_11^Cov+U_11^gauge,
U_12^Sigma = U_12^per+U_12^cusp+U_12^smear+U_12^app,
```

and computes

```text
U_pre13^SEL2
= U_11^Sigma+U_12^Sigma+U_corn+U_14+U_13^entry+U_13^exact.
```

The actual scalar pass quantity is now

```text
Pi_pre13^SEL2
= exp(L_20)-exp(20 widehat_eta_*,20/(1-widehat_eta_*,20))
 - U_pre13^SEL2.
```

Thus `Pi_pre13^SEL2>0` certifies the branch past the pre-surface stage; if
`Pi_pre13^SEL2<=0`, the upper package has failed to certify but the route is
not falsified unless a same-record lower floor consumes the margin.

The easy-zero attempt has now been made and logged honestly. Theorem 4.3A.69
shows that the current Paper-12/14/16/19 imports do not by themselves prove

```text
U_12^per = U_12^cusp = U_12^smear = U_12^app
          = U_13^exact = U_14 = 0.
```

They reduce the claim to five concrete cofinal zero tests: perimeter/cusp
tail zero, smearing tail zero, loop-approximant/readout tail zero,
`X_13,j^{exact,SEL2}->0`, and `||E_14(eta_j)||_tr->0`. On the standard
corner-separated `SEL2` branch, `U_corn` also cannot be erased: it is
`E_corn^SEL2` unless that term is proved zero on the same record law or a
different no-corner selector is declared and its decoration constant is
re-audited.

Corollary 4.3A.74 makes this decision operational for the standard `SEL2`
branch: the unconditional easy-zero shortcut is rejected. The branch must
carry

```text
A_12^per,eval,SEL2 + A_12^cusp,eval,SEL2
+ A_12^smear,eval,SEL2 + A_12^app,eval,SEL2
+ E_corn^SEL2 + E_14^SEL2
+ limsup_j X_13,j^exact,SEL2
```

unless the corresponding right-column zero estimate in that corollary is
proved on the same pushed-forward scalar record law.

The surviving reduced `T_11` block has now been attacked in the same style.
Definition 4.3A.70 evaluates

```text
U_11^loc, U_11^RP, U_11^Cov, U_11^gauge
```

as the exact local-RG/precision, RP, covariance, and gauge/chart limsup tails
on the frozen `SEL2` scalar record law. Theorem 4.3A.71 proves

```text
U_11^Sigma
= U_11^loc,eval + U_11^RP,eval + U_11^Cov,eval + U_11^gauge,eval,
```

and shows that `U_11^Sigma=0` exactly when the four evaluated cofinal tails
vanish. Perimeter/cusp, loop-readout, Paper-14, surface-entry, and decoration
terms are explicitly excluded from these `T_11` tails, so there is no
double-charge.

The exact-entry term has now been expanded too. Definition 4.3A.72 evaluates

```text
U_13^entry
= U_13^BC,eval + U_13^CE,eval + U_13^RPF,eval
 + U_13^KPdec,eval + U_13^SUB,eval + U_13^WP,eval.
```

Theorem 4.3A.73 proves this bounds `A_13^entry,SEL2` on the same frozen
record law. The `CE` residual here is finite-entry central extraction, not
`kappa_13^CE`; `KPdec` is an entry-level comparison residual, not a second
decoration debit; `SUB` is set to zero in the entry bucket on the preferred
route where subcriticality is paid only through the surface leading-rate
test; and `WP` is not the Paper-14 export norm.

The standard pre-surface surplus has now been computed by direct substitution.
Corollary 4.3A.75 defines

```text
U_pre13,std^SEL2
= U_11^loc,eval+U_11^RP,eval+U_11^Cov,eval+U_11^gauge,eval
 + A_12^per,eval,SEL2+A_12^cusp,eval,SEL2
 + A_12^smear,eval,SEL2+A_12^app,eval,SEL2
 + E_corn^SEL2+E_14^SEL2
 + U_13^BC,eval+U_13^CE,eval+U_13^RPF,eval
 + U_13^KPdec,eval+U_13^SUB,eval+U_13^WP,eval
 + limsup_j X_13,j^exact,SEL2,
```

with `U_13^SUB,eval=0` on the preferred reduced route. The operative scalar is

```text
Pi_pre13,std^SEL2
= exp(L_20)-exp(20 widehat_eta_*,20/(1-widehat_eta_*,20))
 - U_pre13,std^SEL2.
```

If `Pi_pre13,std^SEL2>0`, the standard branch reaches the final `T_13`
leading-rate test with certified margin `Pi_pre13,std^SEL2`. If
`Pi_pre13,std^SEL2<=0`, the present upper package does not certify the branch,
but it is not falsified without a same-record lower floor.

The requested five-step computation has also been isolated as its own
standard reduced branch. Definition 4.3A.76 freezes `P20-SEL2-STDRED`: full
`C_area=20` decoration, corner-separated endpoint/corner debit, carried
easy-zero survivors, and `U_13^SUB,eval=0` only because subcriticality is paid
later in the surface leading-rate inequality. Definition 4.3A.77 regroups the
surviving terms into

```text
U_EZ^SEL2,
U_11^red,SEL2,
U_13^entry,red,SEL2.
```

Theorem 4.3A.78 then performs the five-step pass:

```text
Pi_pre13,std,red^SEL2
= exp(L_20)-exp(20 widehat_eta_*,20/(1-widehat_eta_*,20))
 - U_EZ^SEL2 - U_11^red,SEL2 - U_13^entry,red,SEL2.
```

Corollary 4.3A.79 is the current honest decision. Steps 1--4 are complete as
same-record reductions with unique ledger homes. Step 5 is still undecided:
the present imports do not prove

```text
U_EZ^SEL2+U_11^red,SEL2+U_13^entry,red,SEL2
< underline M_loss^SEL2,20.
```

So the branch cannot yet be advanced to an unconditional proof. The next
actual mathematical work is to sharpen one of those three bucket estimates, or
to prove a matching lower floor showing that the standard reduced `SEL2`
branch fails before `T_13`.

The first such bucket, `U_EZ^SEL2`, has now been attacked in the requested
order. Definition 4.3A.80 splits it as

```text
U_EZ^SEL2
= E_14^SEL2+E_corn^SEL2+X_13^exact,SEL2
 + A_12^per,eval,SEL2+A_12^cusp,eval,SEL2
 + A_12^smear,eval,SEL2+A_12^app,eval,SEL2.
```

Theorem 4.3A.81 handles the first three terms. `E_14^SEL2` is zero only under
vanishing Paper-14 transport norm or exact same-battery export;
`E_corn^SEL2` is zero only under a same-record corner-zero audit or a new
no-corner selector with its decoration ledger redone; and
`X_13^exact,SEL2` is zero only under cutoff-to-exact scalar convergence plus
vanishing readout tolerance. Theorem 4.3A.82 handles the four reduced
loop-readout tails as the exact Paper-19 `P19-T12-EVAL` limsups. Corollary
4.3A.83 is the current decision: `U_EZ^SEL2` is decomposed into seven precise
same-record source tests, but the present imports do not prove that any of
the seven terms vanishes unconditionally.

Step 1 inside this bucket has also been sharpened. Definition 4.3A.84 names
the stronger `P20-SEL2-P14-ZERO` audit: the `SEL2` rows must read the
remaining tail of a Paper-14 rate certificate, not merely a finite total
export budget. Theorem 4.3A.85 proves that this stronger audit gives
`E_14^SEL2=0`. Corollary 4.3A.86 records the current fork: prove
`P20-SEL2-P14-ZERO`, or carry the finite `E_14^SEL2` term in `U_EZ^SEL2`.

The extra investigation of that fork has also been logged. Definition
4.3A.87 decomposes `P20-SEL2-P14-ZERO` into nine Paper-14 component rates:
identity, projection, coefficient-window, representation-tail, chart,
counterterm, volume, covariance, and reflection-positivity defects, plus the
cofinal row-tail map `n(j)->infinity`. Theorem 4.3A.88 proves those component
estimates imply `P20-SEL2-P14-ZERO`, and Corollary 4.3A.89 shows Paper 14's
admissible polynomial/exponential rate classes would be sufficient. Corollary
4.3A.90 is the honest verdict: those rate classes are named as targets, but
the current source papers do not prove the actual nine estimates for
four-dimensional `SU(N)` on the relevant whole-process tower. So `E_14^SEL2`
is zero only conditionally; otherwise it remains a carried finite debit.

The active branch now carries it. Corollary 4.3A.91 parks the Paper-14 zero
route behind `P20-SEL2-P14-COMP` and defines

```text
E_14^SEL2,park := E_14^SEL2 < infinity.
```

The active easy-zero bucket is therefore

```text
U_EZ^SEL2,park
= E_14^SEL2
 + E_corn^SEL2 + X_13^exact,SEL2
 + A_12^per,eval,SEL2 + A_12^cusp,eval,SEL2
 + A_12^smear,eval,SEL2 + A_12^app,eval,SEL2,
```

and the active pre-surface surplus is

```text
Pi_pre13,std,red^SEL2,park
= underline M_loss^SEL2,20
 - U_EZ^SEL2,park
 - U_11^red,SEL2
 - U_13^entry,red,SEL2.
```

Thus later `SEL2` work should not spend `E_14^SEL2=0` unless the parked
Paper-14 component audit is explicitly reopened and proved.

The endpoint/corner debit has now been attacked too. Definition 4.3A.92
defines the same-record finite-template audit `P20-SEL2-ECORN`; Lemma
4.3A.93 proves the standard four-slot centered-square branch has sixteen
convex endpoint/corner occurrences, plus a finite optional count
`N_conc^SEL2` if the convention separately charges Creutz-overlap concave
corners. Theorem 4.3A.94 gives the explicit bound

```text
E_corn^SEL2 <= (16+N_conc^SEL2) v_corn^max,
```

and, under pure rectangular-corner unit counting,

```text
E_corn^SEL2 <= 16.
```

Theorem 4.3A.95 is the zero decision: the standard corner-separated `SEL2`
branch cannot set `E_corn^SEL2=0` merely by bookkeeping. Zero requires a
same-record zero-weight audit, an empty-template audit, or a new no-corner
selector with the decoration and transport ledgers redone. Corollary
4.3A.96 records the active decision: carry finite `E_corn^SEL2` with the
displayed bound.

Step 2 has now been attacked as well. Definition 4.3A.97 defines
`P20-SEL2-X13EXACT(A_X^SEL2)` on the same frozen scalar record law:

```text
X_13,j^exact,SEL2
= sup_{F in B_13,j^exact,SEL2}
  |E_{mu_{a_j,s0}^{blk,SEL2}}F-E_{mu_{s0}^{blk,SEL2}}F|
  + epsilon_read,j^(13),SEL2.
```

Lemma 4.3A.98 is the important rigor point: because the row batteries move
with `j`, fixed-battery convergence alone is not enough. One needs a
diagonal cofinal cutoff schedule, or a uniform moving-battery estimate, to
make the supremum vanish. Theorem 4.3A.99 is the decision:
`X_13^exact,SEL2=0` only under that diagonal cutoff-to-exact audit plus
vanishing readout tolerance; otherwise the active branch carries the finite
debit `0<=X_13^exact,SEL2<=A_X^SEL2`. Corollary 4.3A.100 records the active
`U_EZ^SEL2,park` decision after steps 1--2.

The perimeter/cusp tails have now been attacked. Definition 4.3A.101 isolates
the signed scalar perimeter and cusp residuals of the four `SEL2` Creutz
slots, and Lemma 4.3A.102 proves the actual rectangular geometry has

```text
Pi_j^per = 0,
Pi_j^cusp = 0.
```

Theorem 4.3A.104 is the zero-or-bound decision. If the same calibrated
Paper-12 perimeter/cusp branch is used on the four signed Creutz slots and
no perimeter/cusp mismatch is hidden outside the assigned `A_12^app` and
`E_corn` buckets, then

```text
sum_{k>=j} eta_perLC,j,k^SEL2 -> 0,
sum_{k>=j} eta_cuspLC,j,k^SEL2 -> 0,
```

so

```text
A_12^per,eval,SEL2 = A_12^cusp,eval,SEL2 = 0.
```

If that same-branch cancellation audit is not supplied, Definition 4.3A.103
keeps the honest carried bounds
`U_12^{per,SEL2}` and `U_12^{cusp,SEL2}`. Corollary 4.3A.105 updates the
active `U_EZ` bucket accordingly. The next `U_EZ` terms in execution order
are `A_12^smear,eval,SEL2` and `A_12^app,eval,SEL2`.

The smearing-removal tail has now been attacked too. Definition 4.3A.106
states the geometric collar audit: for the finite row battery,

```text
a_k << tau_{j,k}^SEL2,
c_sm tau_{j,k}^SEL2 <= r_min,j^SEL2/4,
tau_{j,k}^SEL2 -> 0,
```

so the smearing support stays inside the declared loop collars and does not
mix nonadjacent arcs, distinct loops, or nonincident cusp collars. Definition
4.3A.107 then translates Paper 12's local subtraction estimate into the
row-shell bound

```text
eta_smearLC,j,k^SEL2
 <= w_sm,j,k^SEL2 max_alpha(epsilon_alpha^cal(tau_{j,k})
    + Omega_alpha(tau_{j,k}))
    + r_sm,j,k^SEL2.
```

Theorem 4.3A.108 gives the decision: a collar-safe diagonal schedule with
vanishing transported row tail proves

```text
sum_{k>=j} eta_smearLC,j,k^SEL2 -> 0,
```

hence `A_12^smear,eval,SEL2=0`; otherwise the branch carries a finite
`U_12^{smear,SEL2}` debit. Corollary 4.3A.109 updates `U_EZ` after this
attack. The remaining reduced `T_12` term is `A_12^app,eval,SEL2`.

The final reduced `T_12` term has now been split. Definition 4.3A.110 writes

```text
A_12^app,eval,SEL2
<= L_12^P12,SEL2 + L_12^appLC,SEL2 + L_12^binLC,SEL2,
```

where the three pieces are exactly the residual Paper-12 loop-modulus tail,
the loop-representative replacement tail, and the finite scalar binning tail.
Definitions 4.3A.111--4.3A.113 give component audits:

```text
eta_P12        <= b_P12,
eta_appLC^(12) <= omega_j(delta_app) + epsilon_app^(12),
eta_binLC^(12) <= nu_j(beta_bin) + epsilon_bin^(12).
```

Theorem 4.3A.114 proves the decision: if the three component row tails vanish,
then

```text
sum_{k>=j}(eta_P12,j,k^SEL2
 + eta_appLC,j,k^(12),SEL2
 + eta_binLC,j,k^(12),SEL2) -> 0,
```

hence `A_12^app,eval,SEL2=0`; otherwise the branch carries the finite
component bounds. Corollary 4.3A.115 records the reduced `T_12` result: the
whole loop-readout bucket vanishes only under six same-record zero audits
for perimeter, cusp, smearing, residual Paper-12 modulus, representative
replacement, and binning; otherwise it is an explicit finite carried sum.

Step 1 is now assembled. Definition 4.3A.116 names the complete reduced
loop-readout package

```text
U_12^red,SEL2
= U_12^per,SEL2 + U_12^cusp,SEL2 + U_12^smear,SEL2
 + U_12^P12,SEL2 + U_12^appLC,SEL2 + U_12^binLC,SEL2,
```

and names the zero gate `P20-SEL2-T12-ZERO`. Theorem 4.3A.117 proves the
assembled decision:

```text
R_12^red,SEL2 <= U_12^red,SEL2
```

on the carried-bound branch, while

```text
R_12^red,SEL2 = 0
```

on the zero branch. Thus the active easy-zero bucket after step 1 is either

```text
U_EZ^SEL2,step1
= E_14^SEL2 + E_corn^SEL2 + X_13^exact,SEL2 + U_12^red,SEL2,
```

or, if `P20-SEL2-T12-ZERO` is proved,

```text
U_EZ^SEL2,step1zero
= E_14^SEL2 + E_corn^SEL2 + X_13^exact,SEL2.
```

Step 2 has also been recomputed. Definition 4.3A.118 defines the two live
post-step-1 surplus branches:

```text
Pi_pre13,std,red^SEL2,step1
= underline M_loss^SEL2,20
 - E_14^SEL2 - E_corn^SEL2 - X_13^exact,SEL2
 - U_12^red,SEL2 - U_11^red,SEL2 - U_13^entry,red,SEL2,
```

and, on `P20-SEL2-T12-ZERO`,

```text
Pi_pre13,std,red^SEL2,step1zero
= underline M_loss^SEL2,20
 - E_14^SEL2 - E_corn^SEL2 - X_13^exact,SEL2
 - U_11^red,SEL2 - U_13^entry,red,SEL2.
```

Theorem 4.3A.119 is the scalar decision: either corresponding `Pi` must be
strictly positive to reach the final surface-leading-rate test. With the
current corner audit, the conservative sufficient inequality may use

```text
E_corn^SEL2 <= (16+N_conc^SEL2)v_corn^max.
```

The `X_13^exact,SEL2` attack has now been pushed to its honest endpoint.
Definition 4.3A.120 splits it into the cutoff-to-exact block-convergence
debit and the scalar readout debit:

```text
X_13^sharp,SEL2
= limsup_j(D_13,j^cut,SEL2 + R_13,j^read,SEL2).
```

Theorem 4.3A.123 proves the exact decision:

```text
X_13^exact,SEL2 = 0
```

only if `P20-SEL2-X13-BC0` and `P20-SEL2-X13-READ0` are both supplied.
Otherwise the branch carries either the sharp value `X_13^sharp,SEL2`, if
directly evaluated, or the separated finite bound

```text
U_13^cut,SEL2 + U_13^read,SEL2.
```

This is a reduction, not an annihilation: the current Paper-13/Paper-19
imports do not prove the moving SEL2 exact-entry battery convergence needed
for `P20-SEL2-X13-BC0`.

Steps 1--3 after the `T_12` assembly are now frozen. Definition 4.3A.126
chooses the active carried value `X_13^car,SEL2`; Definition 4.3A.127 carries
finite `E_14^car,SEL2` and `E_corn^car,SEL2`; Definition 4.3A.128 and
Theorem 4.3A.129 import the reduced `T_11` attack as

```text
U_11^act,SEL2
= U_11^loc,eval+U_11^RP,eval+U_11^Cov,eval+U_11^gauge,eval.
```

The active scalar surplus is therefore

```text
Pi_pre13,std,red^SEL2,1--3
= underline M_loss^SEL2,20
 - E_14^car,SEL2 - E_corn^car,SEL2 - X_13^car,SEL2
 - U_12^red,SEL2 - U_11^act,SEL2 - U_13^entry,red,SEL2.
```

The exact-entry bucket has now also been expanded. Definition 4.3A.132 names
the active component audits

```text
BC, CE, RPF, KPdec, SUB, WP.
```

On the reduced branch, `SUB` is not charged in entry; it is deferred to the
final surface-leading-rate test. The active entry ceiling is therefore

```text
U_13^entry,act,SEL2
= U_13^BC,car+U_13^CE,car+U_13^RPF,car
 + U_13^KPdec,car+U_13^WP,car.
```

The post-entry scalar surplus is

```text
Pi_pre13,std,red^SEL2,entry
= underline M_loss^SEL2,20
 - E_14^car,SEL2 - E_corn^car,SEL2 - X_13^car,SEL2
 - U_12^red,SEL2 - U_11^act,SEL2 - U_13^entry,act,SEL2.
```

This is the current nonsurface decision point. If the displayed quantity is
positive, the branch reaches the final surface-leading-rate comparison. If it
is not proved positive, Paper 20 has isolated the remaining nonsurface
obstruction to the five same-record gates `BC`, `CE`, `RPF`, `KPdec`, and
`WP`, together with the already carried finite debits.

The post-entry surplus has now been computed explicitly. Theorem 4.3A.138
rewrites the same scalar as

```text
Pi_pre13,std,red^SEL2,entry
= Sig_AFM^SEL2 - D_dec^SEL2,20
 - E_14^car,SEL2 - E_corn^car,SEL2 - X_13^car,SEL2
 - U_12^red,SEL2 - U_11^act,SEL2 - U_13^entry,act,SEL2.
```

Corollary 4.3A.139 gives the decision criterion:

```text
E_14^car,SEL2 + E_corn^car,SEL2 + X_13^car,SEL2
+ U_12^red,SEL2 + U_11^act,SEL2 + U_13^entry,act,SEL2
< underline M_loss^SEL2,20.
```

Using the finite corner audit, it is enough to replace
`E_corn^car,SEL2` by `(16+N_conc^SEL2)v_corn^max`. The inequality is not
currently proved numerically because the active carried source ceilings have
not been sharpened enough. Thus the post-entry computation is complete as an
exact scalar worksheet, but the branch remains undecided before the final
surface-rate test.

The first largest live term, `BC`, has now been attacked. Definition 4.3A.140
defines the active row battery and block-limit oscillation; Lemma 4.3A.141
shows compactness gives only

```text
0 <= U_13^BC,car <= 2 B_BC^SEL2
```

and hence `U_13^BC,car<=2` under normalized records. Theorem 4.3A.143 proves
that `U_13^BC,car=0` is equivalent to the moving-battery block-limit
uniqueness audit `P20-SEL2-BC-BLU`. Corollary 4.3A.144 identifies the
noncircular route: a determining finite-block identity ledger with vanishing
cutoff defects, as in Paper 13 Theorem 7.30AN.

Current status: `BC` is not closed unconditionally. It is reduced to a true
continuum-construction uniqueness problem on the active `SEL2` whole-process
record tower. The next largest live entry term is `CE`.

The regularity part of `CE` has now been closed on the finite heat-kernel row
branch and extended to an honest heat-regularized weak-limit route.
Definition 4.3A.145 states the active `CE-REG` target; Lemma 4.3A.146 proves
that smooth central densities have finite weighted character tails; Lemma
4.3A.146A proves the active hypercubic block plaquette readout is a
submersion; and Theorem 4.3A.147 proves

```text
K_p,j^SEL2 in L^1(SU(N)),
K_p,j^SEL2 = 1 + sum_{lambda != 0} k_lambda,j^SEL2 chi_lambda
```

for every cofinal finite heat-kernel row, with

```text
sum_{lambda != 0} d_lambda |k_lambda,j^SEL2| < infinity
```

rowwise. Theorem 4.3A.151 then proves the creative extension: for any central
weak plaquette law, even a singular one, the heat-character smoothed law
`\nu_p*H_\tau` has a smooth central `L^1` density and an explicit finite
heat-trace weighted tail. Theorem 4.3A.153 gives the bound

```text
sum_{lambda != 0,rho} d_lambda |k_lambda^tau|
<= Theta_G(tau)-1-d_rho^2 exp(-tau C_2(rho)/2).
```

This does not decide the exact coefficient window. The leading sign is still
the sign of the unsmoothed coefficient `hat nu_rho`; the positive rate is
still a real dynamical estimate; and returning from the heat-smoothed branch
to the exact unsmoothed theorem requires the de-smearing audit
`P20-SEL2-CE-DESMEAR`.

The requested `CE-SIGN/UNIT` pass has now been carried out as a sharp
decision ledger. Audit 4.3A.154A checks the normalization against Paper 13
Definition 7.30AE/AP and Paper 19 Definition 8L.11A.22G: the active source
chain uses the raw Haar-projection coefficient `k_\rho`, not
`k_\rho/d_\rho`. Corollary 4.3A.154B records that the dimension-normalized
coefficient is a possible future fork, but it requires a rebuilt
surface-normalization audit `P20-SEL2-NORM-SURF`; it cannot be silently
substituted into the present Paper-13/Paper-19 chain. Definition 4.3A.155
therefore freezes the raw real scalar central coefficient convention. Lemma
4.3A.156 proves, by explicit smooth central density examples, that regularity
alone does not imply sign, subunit size, or positive rate. Definitions
4.3A.157 and 4.3A.159 give concrete non-area-law one-plaquette witnesses for
sign and unit: an identity-collar lower bias and a non-identity escape/spread
estimate. Theorems 4.3A.158--4.3A.162 prove that these witnesses give the
exact coefficient window and that positive rate is exactly a strict subunit
gap. Theorems 4.3A.163--4.3A.165C.3 then handle the remaining transfer work:
representation-tail tightness gives zero de-smearing, a uniform Sobolev
coefficient source gives the exact non-leading tail, and rowwise regularity
alone is proved insufficient. Thus exact tail-tightness is parked unless a
uniform same-record representation-tail source is supplied.

The raw `CE-UNIT` part has also been attacked in the heat-kernel model rather
than left as an opaque inequality. Definition 4.3A.160A defines

```text
theta_rho = 2 log(d_rho)/C_2(rho)
```

and the same-record comparison audit

```text
|a_rho,j^SEL2 - d_rho exp(-t_eff,j C_2(rho)/2)| <= epsilon_rho,j.
```

Theorem 4.3A.160B proves raw `CE-UNIT` if the effective block time stays
uniformly above `theta_rho` with enough error margin. Theorem 4.3A.160C
proves the complementary failure statement: if the effective time is
uniformly below `theta_rho`, and in particular if it is just the microscopic
AF heat time tending to zero with vanishing comparison error, then the raw
coefficient is eventually larger than one and the active raw route fails.
Definitions 4.3A.160E--4.3A.160F then remove the model ambiguity by defining
the intrinsic block time

```text
t_rho,j^blk = (2/C_2(rho)) log(d_rho/a_rho,j^SEL2).
```

Theorems 4.3A.160G--4.3A.160H prove the exact fork. If
`P20-SEL2-BTIME-LIFT(Delta_rho)` holds, raw `CE-UNIT/RATE` closes with rate
at least `C_2(rho) Delta_rho/2`. If `P20-SEL2-BTIME-COLLAPSE` holds and
`t_i->0`, raw `CE-UNIT` fails. Corollary 4.3A.160I is the current decision:
Paper 16 supplies `t_i->0` for microscopic local estimates, while Paper 13
declares `u_{rho,s0}` to be a renormalized block-scale coefficient, so the
current imports prove neither lift nor collapse. Lemma 4.3A.160J then proves
that the finite block pushforward itself underdetermines the fork: comparison
rows satisfying centrality, rowwise regularity, and same-record bookkeeping
can realize either lifted block time or microscopic collapse. Definition
4.3A.160K and Theorem 4.3A.160L therefore park the active raw branch for the
current sources. Definitions 4.3A.160M--4.3A.160P then open the normalized
surface fork. The result is critical: simply replacing `k_\rho` by
`k_\rho/d_\rho` is algebraically neutral, because each excess plaquette
returns a `d_\rho` surcharge. The normalized route helps only if a new
same-record surface theorem proves a genuine cancellation with
`\Delta_dim^{SEL2}<log d_\rho`. Audit 4.3A.160Q freezes the exact
normalization convention, Lemma 4.3A.160R proves the one-link Schur gluing
identity, and Corollary 4.3A.160S proves the local one-plaquette normalized
sheet weight `k_\rho/d_\rho`. Corollary 4.3A.160T records the boundary: this
proves the local spin-network core of dimension cancellation. Lemma
4.3A.160U and Theorem 4.3A.160V then lift the identity to any clean
rho-monochromatic disk surface, giving exact whole-surface weight
`(k_\rho/d_\rho)^{|\Sigma|}`. Corollary 4.3A.160W proves zero dimension
surcharge for the clean leading channel, Corollary 4.3A.160X narrows the
remaining `P20-SEL2-NORM-SURF` work to the non-clean/corner/decoration
remainder, and Definition 4.3A.160Y--Corollary 4.3A.160AE decide that
remainder: corners, non-leading channels, decoration regrouping, real pairing,
and pushforward add no per-excess dimension surcharge; recoupling from
self-touching/local replacements is the only possible source, is zero on the
active reduced `SEL2` support convention, and is otherwise carried as the
finite fallback `r_rec log C_rec`. Definition 4.3A.160AF and Theorem
4.3A.160AG then split the normalized rate from the raw rate: normalized
closure needs a positive effective block character time, not the raw
`theta_rho` threshold. Lemma 4.3A.160AI--Corollary 4.3A.160BJ sharpen this
again: a cofinal one-block non-identity escape mass closes normalized rate,
while disappearance of every fixed escape set is equivalent to normalized
coefficient collapse; the current large-field/residual imports prove neither
alternative. The new convolution worksheet then freezes the only legitimate
finite-row reference time `T_j^{SEL2,conv}` and proves the same-target
coefficient comparison from the explicit defect `P20-SEL2-CONV-CMP`; the
standard `SEL2` AF-area scaling gives the cofinal block-time window
`0<T_-^{SEL2}<=T_j^{SEL2,conv}<=T_+^{SEL2}<infty`, and the active remaining
four-dimensional target is weakened to the scalar coefficient source
`P20-SEL2-4DCOEFF-CLOSE` or the finite-gap scalar inequality. The
new Definitions 4.3A.160BH.1A--4.3A.160BH.1C now freeze the actual finite
`SEL2` row and prove that the five-term scalar ledger is the complete Step-2
target for this coefficient. The
counterterm, projective, and collar pieces are split by Definitions
4.3A.160BH.2A--4.3A.160BH.2C: they vanish on the strict clean nonbulk branch
and otherwise contribute the carried debit `E_{rho,nonbulk}`; Corollary
4.3A.160BH.2G packages this as the Step-3 actual nonbulk closure. Definitions
4.3A.160BH.8A--4.3A.160BH.9A now verify `BDROOT` on the clean good-collar
branch, prove the Step-4 actual boundary/collar closure, and give the explicit
carried boundary/collar debit
`E_{rho,col,*}^{SEL2,bd}` for nonclean branches; and the surviving coefficient
problem is the signed grouped interior constant
`Gamma_{rho,int}^{SEL2}`. Definitions 4.3A.160BH.18--4.3A.160BH.26 now freeze
the active normalized branch, expand that constant into the seven
`HK-SF-YM2` labels, and evaluate the strict axial-tree, exact-covariance,
connected/cumulant, minimal-readout subbranch as the local generator mismatch

```text
Xi_{rho,r}^{YM2}
= Gamma_4 + Gamma_33 + Gamma_J2
```

at every interior root, after the heat-time tangent has been removed.
Definitions 4.3A.160BH.27--4.3A.160BH.36 then give the actual rootwise proof
route: compact-group heat-kernel Schwinger-Dyson is exact, the divergence has
no interior scalar residue, and `GENMATCH` follows once the finite
normal-coordinate template audit `P20-SEL2-HKSD-TPL` verifies that the only
interior second-order non-time labels are `{4,33,J2}`. Definitions
4.3A.160BH.37--4.3A.160BH.40 perform that finite template census on the actual
strict reduced `SEL2` root branch and close `GENMATCH` rootwise. Theorems
4.3A.160BH.40A--4.3A.160BH.40B then convert this into actual interior-root
closure:

```text
S_j zeta_{rho,bulk,j}^{SEL2} -> 0
```

and assemble Steps 1--5 into `P20-SEL2-4DCOEFF-CLOSE` on the strict exact
finite-row branch.
Definitions 4.3A.165A--4.3A.165C close the exact de-smearing fork:
tail-tightness gives zero de-smearing, while a merely finite tail requires the
carried debit `U_{CE-sm}^{SEL2}`. Corollary 4.3A.165D assembles the clean
exact scalar source: strict clean nonbulk, clean boundary, strict interior
`GENMATCH`, and tail-tightness give `P20-SEL2-4DCOEFF-CLOSE` with
`\epsilon_{\rho,j}->0`.

Current honest status: the six-step `CE` attack is fully reduced and partially
proved at the abstract source level, but it is not an unconditional closure
for four-dimensional `SU(N)`. On the raw branch, the remaining source inputs
are the scalar-sheet bias/spread estimates

```text
0<s_rho <= liminf a_rho,j <= limsup a_rho,j <= 1-sigma_rho < 1
```

and either a new `BTIME-LIFT` source or a collapse proof that kills the raw
route. On the active reduced normalized route, the dimension-surcharge value is
now `Delta_dim^{SEL2}=0`; the coefficient window is

```text
0<s_tilde_rho
 <= liminf a_rho,j/d_rho
 <= limsup a_rho,j/d_rho
 <= 1-sigma_tilde_rho < 1.
```

The lower side is the separate audit `P20-SEL2-NORM-POS` in general, but
Lemma 4.3A.160BG.1 proves it on the strict scalar-comparison branch from the
finite upper block-time bound. Corollary 4.3A.160BG.2 fixes the normalization:
the object is always `a_rho,j/d_rho`, never the raw coefficient. The upper side
is the escape audit, equivalently a normalized block-time lift together with
cofinal positivity. The exact escape observable has now been frozen as

```text
e_rho=1-psi_rho,
V_{rho,gamma}={e_rho>=gamma}.
```

Theorems 4.3A.160AQ.3--4.3A.160AQ.4 decide its mass: strict clean scalar
source plus positive convolution block time proves a cofinal escape lower
bound, while same-target collapse falsifies every fixed escape window.
Corollaries 4.3A.160BG.3--4.3A.160BG.4 then combine lower bias,
normalization, and escape into the final normalized rate:

```text
kappa_tilde_rho >= -log(1-q_rho gamma_rho) > 0
```

with the usual strict-inequality convention for named lower-bound constants.
Theorem 4.3A.160BH.40C consolidates this into one strict-branch coefficient
window theorem, and Definition 4.3A.160BH.40D freezes the rate that should be
used by the surface-polymer pass test:

```text
kappa_tilde_{rho,cert}^{SEL2}
= min{
    T_-^{SEL2} C_2(rho)/2,
    -log(1-q_rho gamma_rho)
  }.
```

Corollary 4.3A.160BH.40F plugs this certified rate into the actual
Paper-13/Paper-19 surface-polymer test. On the strict branch the remaining
T13 pass condition is exactly the scalar inequality

```text
kappa_tilde_{rho,cert}^{SEL2}
>
G_13^raw
+ log(1+M_13^{surf,SEL2}/underline M_pre13^{SEL2,20}).
```

Equivalently the branch has a positive surface surplus

```text
Pi_13^{surf,SEL2}
= kappa_tilde_{rho,cert}^{SEL2}
  - G_13^raw
  - log(1+M_13^{surf,SEL2}/underline M_pre13^{SEL2,20})
> 0.
```

Definition 4.3A.160BH.40H then plugs in the frozen `SEL2` worksheet value

```text
G_13^{raw,SEL2,cert}
=3+log 20+20 widehat_eta_*,20/(1-widehat_eta_*,20),
```

and gives the evaluated surplus

```text
Pi_13,cert^{surf,SEL2}
= min{T_-^{SEL2}C_2(rho)/2, -log(1-q_rho gamma_rho)}
  - G_13^{raw,SEL2,cert}
  - log(1+M_13^{surf,SEL2}/underline M_pre13^{SEL2,20}).
```

Corollary 4.3A.160BH.40I is the strict closure test:
`P20-SEL2-T13-PASS`, and hence `P20-LOSS-PASS` for this frozen branch, follows
if

```text
underline M_pre13^{SEL2,20}>0
and
Pi_13,cert^{surf,SEL2}>0.
```

Corollaries 4.3A.160BH.40J--4.3A.160BH.40L turn this into the two scalar
gates that must now be checked:

```text
T_-^{SEL2} > 2G_13,cert^{SEL2}/C_2(rho),
q_rho gamma_rho > 1-exp(-G_13,cert^{SEL2}),
```

and, after defining

```text
Delta_13,cert^{SEL2}
= min{T_-^{SEL2}C_2(rho)/2, -log(1-q_rho gamma_rho)}
  - G_13,cert^{SEL2},
```

the exact prefactor cap

```text
M_13^{surf,SEL2}
<
underline M_pre13^{SEL2,20}
(exp(Delta_13,cert^{SEL2})-1).
```

This is the current sharp decision form. If the rate-over-growth gate fails,
the certified strict branch cannot pass with the present surface-growth bound.
If it passes, the only remaining surface question is whether the Paper-13
surface prefactor fits under the displayed cap.

Corollary 4.3A.160BH.40M evaluates the plausibility of the unsharpened rate
gate. Because the current imported surface-growth constant has the
decoration-free floor

```text
G_13,cert^{SEL2} >= 3+log 20 approx 5.995732,
```

the escape side requires

```text
q_rho gamma_rho > 1-exp(-G_13,cert^{SEL2})
                 >= 0.9975106...
```

and the block-time side requires

```text
T_-^{SEL2} > (6+2 log 20)/C_2(rho)
```

before adding the positive decoration correction. For the fundamental channel
this already means approximately `T_->15.99` for `SU(2)`, `T_->8.99` for
`SU(3)`, and `T_->6.40` for `SU(4)`. So the present rate gate is severe. It is
not formally falsified, but it is plausible only if the same-record escape mass
is nearly maximal, the block-time lower bound is genuinely large, or the
surface-growth constant is sharpened below the current `3+log 20+decoration`
ceiling.

Definitions 4.3A.160BH.40N--4.3A.160BH.40R perform that sharpening on the
actual reduced `SEL2` surface template. The audit keeps
`Delta_plaq^{4D}=20` and `R_loc^{4D}=1`: the adjacency degree is already sharp,
and orientation/local replacement labels are not additional support entropy on
the strict branch. The improvement comes from replacing the crude
`e^3 Delta` animal envelope by a rooted tree-graph bound `e(Delta-1)`.
Therefore the strict reduced branch may use

```text
G_13,tree^{SEL2}
=1+log 19+20 widehat_eta_*,20/(1-widehat_eta_*,20).
```

Before decoration this lowers the escape threshold to

```text
q_rho gamma_rho > 1-1/(19e) approx 0.980632
```

and the fundamental-channel time thresholds to approximately `T_->10.52` for
`SU(2)`, `T_->5.92` for `SU(3)`, and `T_->4.21` for `SU(4)`. This is a real
improvement, but still a strong source requirement. Any non-reduced branch
must restore the dropped orientation/replacement/collar-root exponents before
claiming the sharpened surplus.

Definitions 4.3A.160BH.40S--4.3A.160BH.40U now freeze the exact missing source
gate. The decoration contribution is

```text
D_13,dec^{SEL2,20}=20 widehat_eta_*,20/(1-widehat_eta_*,20),
```

and the sharpened thresholds are

```text
Theta_esc^tree
=1-(1/(19e)) exp(-D_13,dec^{SEL2,20}),
```

```text
Theta_T^tree(rho)
=2(1+log 19+D_13,dec^{SEL2,20})/C_2(rho).
```

The current source chain supplies positive symbolic data
`T_-^{SEL2}`, `q_rho`, `gamma_rho`, and `widehat_eta_*,20`; it does not by
itself prove the strict comparisons

```text
q_rho gamma_rho > Theta_esc^tree,
T_-^{SEL2} > Theta_T^tree(rho).
```

Those two comparisons are now named
`P20-SEL2-TREE-RATE-GATE`. If they hold, the rate side is closed and the only
remaining T13 surface task is the prefactor cap. If either fails on the same
record, the strict reduced `SEL2` certificate cannot pass with the current
tree-graph surface-growth bound.

Definition 4.3A.160BH.40T.1 now splits this parked gate into the two exact
source subgates:

```text
P20-SEL2-ESC-MASS(V_rho,gamma_rho,q_rho)
and
P20-SEL2-TREE-TIME(rho).
```

The first asks for a same-record escape product
`q_rho gamma_rho>Theta_esc^tree`; the second asks for
`T_-^{SEL2}>Theta_T^tree(rho)`. Lemma 4.3A.160BH.40T.2 proves that
`ESC-MASS` is exactly the escape half of the surface-rate gate. Theorem
4.3A.160BH.40T.3 gives the first pass/fail reduction: a sufficiently large
cofinal escape mass proves the subgate, same-target normalized collapse
falsifies it, and the existing rowwise regularity/large-field/residual upper
bounds decide neither. Theorem 4.3A.160BH.40T.4 adds the important scalar
diagnostic: the positive escape mass already obtained from the clean
coefficient-gap route is real, but its certified product is at most
`(sigma_rho^{ref})^2/8<1/8`, while the rooted tree threshold is at least
`1-1/(19e)>0.98`. Thus the current positive-escape theorem is far too weak
to close `ESC-MASS`; a new near-maximal escape source, a much sharper
surface-growth theorem, or the independent tree-time inequality is still
needed.

The `TREE-TIME` half is now equally explicit. Definition
4.3A.160BH.40T.5 freezes the clean finite-template time window

```text
T_clean,-^SEL2=s(1-epsilon_A)(1-chi),
T_clean,+^SEL2=s(1+epsilon_A)(1+chi),
```

coming from

```text
T_j^SEL2,conv=sum_b tau_b,j=S_j t_i(j)+o(1).
```

Theorem 4.3A.160BH.40T.6 proves the exact trichotomy:

```text
T_clean,-^SEL2 > Theta_T^tree(rho)
  => TREE-TIME passes;

T_clean,+^SEL2 <= Theta_T^tree(rho)
  => TREE-TIME fails for the frozen standard template;

otherwise the current finite-template window is inconclusive.
```

Corollary 4.3A.160BH.40T.7 rewrites this as a selector-parameter threshold
for `s`; before decoration and slack the fundamental-channel thresholds are
`s>10.5185...` for `SU(2)`, `s>5.9167...` for `SU(3)`, and `s>4.2074...`
for `SU(4)`. Thus the finite block pushforward does not create hidden extra
time; it computes a window. Passing `TREE-TIME` requires freezing a large
enough AF-area parameter, proving a sharper actual lower liminf for
`T_j^SEL2,conv`, or lowering the surface-growth threshold.

Definition 4.3A.160BH.40G records the carried-debit convention for the same
test. On the strict exact branch,

```text
E_nonbulk = 0,
E_col,bd = 0,
U_CE-sm = 0
```

where the last equality uses the exact scalar observable `psi_rho` without an
extra smoothing/de-smearing transfer. The covariance, readout/projective, and
counterterm/scheme debits are also zero only under their strict exact
conventions: exact block-conditioned covariance, exact finite scalar readout,
no projective/regulator mismatch, and clean minimal counterterm absorption
into `T_j^{SEL2,conv}`. Any missing strict convention restores the named
finite carried debit before the surface surplus may be claimed.

Corollary 4.3A.160BJ was the scalar-source reduction point:
the independent-convolution reference has favorable scaling, and it is enough
to compare the actual four-dimensional `SEL2` block pushforward to that
reference on the single observable `\psi_\rho`; full
`P20-SEL2-4DCONV-CLOSE` is stronger than necessary. The strict exact finite-row
branch now supplies the vanishing scalar source by Corollary 4.3A.160BH.40B.
The former hard interior term has been closed on the strict reduced branch:
`P20-SEL2-HKSD-TPL` is verified by the finite root term census, so

```text
Xi_{rho,r}^{YM2}=0
```

for every interior root, `INTBULK-FOC` follows, and Theorem
4.3A.160BH.40A gives `S_j zeta_{rho,bulk,j}^{SEL2}->0`. The nonbulk scalar
terms are closed on the strict clean branch by Corollary 4.3A.160BH.2G, and
the boundary/collar Bianchi roots are closed by Corollary 4.3A.160BH.9A. If
exact covariance matching, exact finite scalar readout, clean collar support,
or the strict reduced root census is not used, add the carried covariance,
uncharged-template, nonclean collar, counterterm/scheme, or projective/readout
debits back into the finite `Xi`/scalar budget. Uniform Sobolev/tail-tight
control closes the exact de-smearing branch by Theorem 4.3A.165B; without it,
restore `U_{CE-sm}^{SEL2}` before any finite-gap comparison. Thus the scalar
source, normalized lower bias, and exact escape mass are cleanly assembled on
the strict branch. The overall confinement route now depends on whether that
strict exact finite-row branch is accepted as the actual `SEL2` source branch;
off it, the carried finite debits listed above must still be tested.

After the Paper-11 and Paper-12 audits, the tree-rate gate is not strengthened
by earlier-paper imports. Paper 11 gives the RG residual/trajectory scaffold
and a smeared Wilson-loop anchor; Paper 12 gives renormalized Wilson-loop
readout control. Neither supplies the same-record `SEL2` block-plaquette
coefficient-time lower bound or the escape product above the rooted tree
threshold. Therefore the current final obstruction is parked exactly as
`P20-SEL2-TREE-RATE-GATE`, plus the prefactor cap if that gate is later
proved. Paper 20 should not claim unconditional actual `4D SU(N)` confinement
until that parked source gate is either proved on the frozen record law or
replaced by a strictly stronger same-record surface theorem.

## Final Obstruction Ledger

| Item | Status | Reader-facing meaning |
| --- | --- | --- |
| `P20-NOSMUGGLE` | proved/audited | The frozen selector is structural bookkeeping, not an imported area law, mass gap, or continuum-YM existence theorem. |
| Clean matched-time coefficient branch | proved on its declared exact-record row | The first coefficient debit can be made zero on the frozen clean selector; this is not yet the surface-rate source. |
| `SEL2` decoration gate with `C_area=20` | proved under the same-record residual/character-tail audits | The decoration debit fits below the signal floor on the unit-normalized `SEL2` worksheet. |
| Strict nonbulk/collar/interior scalar source | proved on the strict exact reduced branch | The finite root/collar census removes the local scalar source obstruction when exact conventions are used. |
| Exact de-smearing/tail-tightness | conditional | Zero de-smearing requires the uniform tail-tightness/Sobolev source; otherwise carry `U_CE-sm^{SEL2}`. |
| Easy-zero transport and Paper-14 export debits | partly parked | Terms such as `E_14`, `E_corn`, and `X_13^exact` are zero only under their same-record component audits; otherwise they remain finite carried debits. |
| `P20-SEL2-TREE-RATE-GATE` | parked open source obstruction | Papers 11--12 do not prove the required same-record inequalities `q_rho gamma_rho>Theta_esc^tree` and `T_-^{SEL2}>Theta_T^tree`. |
| Surface prefactor cap | conditional after tree-rate pass | Once the tree-rate gate passes, `M_13^{surf,SEL2}` must fit below the explicit cap. |
| Actual unconditional `4D SU(N)` confinement | not proved | The strict reduced branch remains a conditional/reduction route until the parked tree-rate source and any carried debits are closed. |

The next legitimate fork is therefore exactly one of:

1. prove `P20-SEL2-TREE-RATE-GATE` on the frozen `SEL2` record law;
2. prove a stronger same-record surface-growth theorem that lowers
   `Theta_esc^tree` and `Theta_T^tree`, then rerun the gate;
3. close Paper 20 as a conditional reduction paper and open a new source paper
   dedicated to the block-plaquette coefficient-time/escape estimates.

## Handoff To Paper 21

Paper 20 stops here. Its result is a completed same-record reduction and
obstruction ledger, not an unconditional confinement proof. Continuing to add
source estimates inside this file would blur the boundary between a reduction
paper and a new analytic source campaign.

The next paper should therefore be:

```text
Paper 21:
SEL2 Tree-Rate Source Or Falsification For 4D SU(N) Direct-Witness Confinement.
```

Paper 21 inherits exactly the frozen objects already declared here:

```text
P20-SEL2(eta_ch,20^SEL2,20),
P20-SEL2-TR-COMMON,
P20-SEL2-NOSMUGGLE,
T_j^SEL2,conv,
Theta_esc^tree,
Theta_T^tree(rho),
underline M_pre13^SEL2,20,
M_13^surf,SEL2.
```

It has three permitted tasks, in order.

1. Decide the time half:

   ```text
   P20-SEL2-TREE-TIME(rho):
   T_-^SEL2 > Theta_T^tree(rho).
   ```

   The pass/fail trichotomy is already Theorem 4.3A.160BH.40T.6. Paper 21
   must either freeze selector parameters satisfying the pass inequality,
   freeze parameters satisfying the falsifier, or show that a sharper
   same-record lower liminf for `T_j^SEL2,conv` is available.

2. Decide the escape half:

   ```text
   P20-SEL2-ESC-MASS(V_rho,gamma_rho,q_rho):
   q_rho gamma_rho > Theta_esc^tree.
   ```

   Paper 20 proved that the existing positive-escape theorem is far too weak.
   Paper 21 must supply a genuinely stronger anti-concentration source, prove
   same-target collapse and falsify the branch, or lower the surface-growth
   threshold enough that the existing escape product becomes relevant.

3. If both halves pass, evaluate the remaining surface prefactor cap:

   ```text
   M_13^surf,SEL2
   <
   underline M_pre13^SEL2,20
   (exp(Delta_13,tree^SEL2)-1).
   ```

Anything outside these three tasks belongs to a later synthesis and global
audit paper. In particular, Paper 21 must not import a Wilson-loop area law,
mass gap, or continuum Yang-Mills measure as a premise for the tree-rate
source; it must remain a scalar same-record source or falsification paper.
