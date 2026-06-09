# Relativistic ISP V3 Paper 19: Actual Source Constants For 4D `SU(N)` Confinement

Author: Felix Robles Elvira

## Abstract

Paper 18 gave a conditional reduction of actual `4D SU(N)` confinement to a
finite list of scalar source gates on one frozen whole-process Wilson-loop
record law:

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
=> AYM-CONF-CLOSE(m_*)
=> MGAP(m_*).
```

Paper 19 attacks those source gates directly as a reduction and obstruction
ledger. The aim is ambitious but conditional: close the declared
direct-witness confinement branch if the source constants can be proved on
the actual continuum tower. The paper is equally prepared to falsify the
route: if the reserve, quotient loop-modulus, pressure, ledger, or cofinal
gates cannot hold, the failure must be recorded as a scalar obstruction
rather than hidden behind flux-tube language or gauge-fixed pictures.

## 0. Barandes-Aligned Boundary

The primitive object remains the whole-process law of records. Wilson loops,
Creutz ratios, marked loops, Polyakov lines, and endpoint protocols enter
only as scalar records or typed boundary instruments. A gauge chart, sheet,
surface, polymer, or flux tube is an auxiliary estimate. It must be
eliminated into scalar record inequalities before a final theorem is stated.

Paper 19 therefore permits:

1. finite Wilson-loop and Creutz batteries;
2. endpoint-enlarged marked-loop batteries;
3. source constants exported by Papers 15--18;
4. one frozen whole-process law and one disjoint debit register;
5. finite-window or cofinal-window scalar inequalities.

Paper 19 does not permit:

1. colored endpoints as standalone scalar states;
2. gauge-fixed fields as ontology;
3. partial Markov kernels not declared by the whole-process law;
4. strong-coupling or finite-regulator estimates unless they are transported
   into the declared continuum record tower.

### Post-Paper-20 Source Boundary

Paper 19 names, decomposes, and conditionally audits the source constants
that a direct-witness confinement route would need. After the Paper-20
audit, it must not be read as already supplying the SEL2 tree-rate source.
The leading `T_13` coefficient window, decoration ledger, and same-record
transport bookkeeping remain useful reductions, but they do not prove the
Paper-20 gate

```text
P20-SEL2-TREE-RATE-GATE:
q_rho gamma_rho > Theta_esc^tree
and
T_-^{SEL2} > Theta_T^tree(rho).
```

Equivalently, Paper 19 cannot be cited as an unconditional proof of the
SEL2 block-plaquette coefficient-time lower bound, the SEL2 heat-kernel
coefficient comparison, or the normalized leading-sheet rate needed by
Paper 20. Those must be supplied by a separate source theorem on the same
frozen pushed-forward record law. Until then, Paper 19 remains a rigorous
conditional source-constant ledger and obstruction classifier, not an
unconditional confinement proof.

## 0A. Source Papers Used

Paper 15 exports the numerical connected-polymer surface certificate
`nCPSC`. Its Creutz reserve component is:

```text
M_15^{bd}
 =
 u_-^{N_0}(1-u_+^{Q_sigma})
 - Delta_dec^{bd}
 - T_loss^{bd}.
```

When `M_15^{bd}>0`, Paper 15 proves that the block-scale Creutz anchor
survives decorations and finite transport losses.

Paper 16 exports the actual heat-kernel source gates. The two used first in
Paper 19 are:

```text
HK-CREUTZ-CLOSE(M_SUB^{bd},L_bat,L_reg,L_vol,L_shape)
=> AYM-CREUTZ with reserve
   M_15^{bd}=M_SUB^{bd}-L_bat-L_reg-L_vol-L_shape>0,
```

and

```text
HK-LC-CLOSE
```

from a loop-continuity transport ledger `HK-LC-TRANSPORT`. Paper 16 also
exports the whole-process compatibility needed to keep these constants on
one tower.

Paper 16 now packages the analytic residual branch as one finite-template
certificate:

```text
HK-AN-FINTPL-CLOSE(m)
=> HK-AN-CLOSE(m)
=> AYM-AFRCE + AYM-KP.
```

The finite row-data for that import are

```text
Delta_B,L_ent,L_KP,lambda_D,R_blk,C_v^{row},r_res^clean,m.
```

Paper 19 uses this import through the following scalar constants:

```text
A_19^{an}:=A_res,
mu_19^{an}:=mu_res,
Delta_19^{an}:=mu_res-h_KP-m>0,
K_19^{an}:=C_KP A_res/(1-exp(-Delta_19^{an})),
eta_19^{res}:=
C_KP A_res exp(-Delta_19^{an}r_res)/(1-exp(-Delta_19^{an}))<1.
```

Here `A_res,mu_res,C_KP,h_KP,r_res` are exactly the constants exported by
Paper 16 Theorem 9N.2A after `HK-AN-FINTPL-CLOSE(m)` proves
`HK-AN-CLOSE(m)`. The notation `eta_19^{res}` is the Paper-19 name for the
same residual KP activity when the residual-decoration records are on the
same finite battery.

### Definition 0A.1: Paper-16 Analytic Import `P19-AN-IMPORT(m)`

`P19-AN-IMPORT(m)` holds when:

1. Paper 16 `HK-AN-FINTPL-CLOSE(m)` is verified on the same heat-kernel
   whole-process tower used by Paper 19;
2. the finite row-data

   ```text
   Delta_B,L_ent,L_KP,lambda_D,R_blk,C_v^{row},r_res^clean,m
   ```

   are attached to that same pushed-forward record law;
3. the Paper-19 residual-decoration battery is a subbattery of, or is
   bounded by, the Paper-16 residual KP battery with the same readout ledger.

Under `P19-AN-IMPORT(m)`, Paper 19 may use

```text
eta_res^* := eta_19^{res},
Delta_res^* := Delta_19^{an},
K_res^* := K_19^{an}.
```

This is an import of scalar record-law constants only. It does not import
gauge fields, polymers, sheets, or covariance variables as ontology.

### Definition 0A.2: Same-Record Analytic Import Audit `P19-AN-AUDIT(m)`

`P19-AN-AUDIT(m)` is the finite, checkable audit which proves
`P19-AN-IMPORT(m)`. It holds for a chosen heat-kernel row `T_HK^std` when
all of the following clauses are verified on one and the same pushed-forward
whole-process record law.

1. **Common row.** The Paper-16 analytic row and the Paper-19 direct-witness
   row are the same row: they use the same cutoff tower, same finite
   projection maps, same loop/readout maps, same counterterm convention, and
   same pushed-forward law `Gamma_i`.
2. **Finite counting data.** The block graph has finite maximum degree
   `Delta_B`, the small-field label count `L_ent` is finite, and the residual
   KP label count `L_KP` is finite. These are the constants used in Paper 16
   `HK-FIN-COUNT`.
3. **Finite covariance data.** The block-conditioned covariance source on
   this row has a uniform Dirichlet/Poincare lower bound
   `lambda_D>0` and finite collar-template range `R_blk<infinity`, so
   Paper 16 may use `C_0=lambda_D^{-1}` and `R_G=R_blk`.
4. **Small-field vertex data.** The pushed-forward neutral character record
   satisfies the Paper-16 `HK-SF-YM2` vertex ledger with finite constant
   `C_v^{row}`. Odd or gauge-coordinate-only terms are not exported; only
   the scalar record-law bound is.
5. **Clean analytic conventions.** The row uses the clean counterterm
   convention of Paper 16 Theorem 9K.2G and a finite-template large-field
   source whose margin is large enough for Paper 16 Theorem 9N.1Q.3.
6. **Residual starting radius.** The clean residual starting radius
   `r_res^clean` is finite and is attached to the same residual KP battery.
7. **Weight choice.** The residual weight `m>0` is the same `m` in Paper 16
   `HK-AN-FINTPL-CLOSE(m)` and in the Paper-19 residual-decoration ledger.
8. **Residual battery domination.** The Paper-19 residual-decoration battery
   is a subbattery of, or is activity-dominated by, the Paper-16 residual KP
   battery in the sense of Definition 0A.3 below.

Equivalently, `P19-AN-AUDIT(m)` is the assertion that the eight finite row
data

```text
Delta_B,L_ent,L_KP,lambda_D,R_blk,C_v^{row},r_res^clean,m
```

are not merely named, but are certified on the single record law used by both
papers, and that the Paper-19 residual records are covered by the Paper-16
residual KP ledger.

### Definition 0A.3: Residual-Decoration Subbattery Domination

Let `B_{19,j}^{res}` be the Paper-19 residual-decoration battery at window
`j`, with residual activity `a_{19,j}(b)` and residual weight `w_{19,j}(b)`.
Let `B_{16,j}^{KP}` be the Paper-16 residual KP battery, with activity
`a_{16,j}(c)` and weight `w_{16,j}(c)`.

The Paper-19 battery is dominated by the Paper-16 battery when there are maps

```text
iota_j : B_{19,j}^{res} -> B_{16,j}^{KP}
```

and readout-identifications `rho_{19,j}=rho_{16,j} circ iota_j` such that,
for every Paper-16 residual label `c`,

```math
\sum_{b:\iota_j(b)=c}
a_{19,j}(b)\,e^{m w_{19,j}(b)}
\le
a_{16,j}(c)\,e^{m w_{16,j}(c)}.
```

The same definition also permits a declared scalar domination constant
`D_sub` provided the Paper-16 residual KP activity is run with the
correspondingly debited amplitude. In the clean import used here,
`D_sub=1`.

This is a statement about finite scalar records and their activities. The
maps `iota_j` are not new dynamics and do not introduce a hidden state space.

### Theorem 0A.4: The Audit Proves `P19-AN-IMPORT(m)`

If `P19-AN-AUDIT(m)` holds, then `P19-AN-IMPORT(m)` holds. Consequently
Paper 19 may set

```text
eta_res^* := eta_19^{res},
Delta_res^* := Delta_19^{an},
K_res^* := K_19^{an}.
```

Moreover the residual-decoration activity obeys

```math
\limsup_j\eta_{{res},j}^{bd}
\le
\eta_{19}^{res}.
```

Proof.

Clauses 1--7 of `P19-AN-AUDIT(m)` are exactly the finite-template row data
and clean conventions required by Paper 16 Definition 9N.1Q.4. Hence Paper
16 proves `HK-AN-FINTPL-CLOSE(m)`. Paper 16 Theorem 9N.1Q.5 exports
`HK-AN-CLOSE(m)`, and Paper 16 Theorem 9N.2A exports the analytic residual
constants
`A_res,mu_res,C_KP,h_KP,r_res`.

Clause 8 and Definition 0A.3 give term-by-term domination of the Paper-19
residual-decoration activity by the Paper-16 residual KP activity after the
same exponential weight `m` is applied. Taking finite sums, then the cofinal
limsup, gives the displayed bound. The readout-identification clause ensures
that the comparison is made after pushforward to the same scalar record law.
Thus Definition 0A.1 holds, and the three Paper-19 residual constants may be
identified with the Paper-16 analytic residual constants. `square`

### Theorem 0A.5: Exact Step-1 Obstruction For The Analytic Import

For a fixed candidate row `T_HK^std`, Step 1 fails exactly when at least one
of the audit clauses in Definition 0A.2 fails on the pushed-forward record
law:

```text
common-row mismatch
or infinite Delta_B,L_ent,L_KP
or lambda_D<=0
or R_blk=infinity
or no finite HK-SF-YM2 constant C_v^{row}
or no clean counterterm / large-field margin
or r_res^clean=infinity
or no residual-decoration subbattery domination.
```

If one of these failures is proved for every admissible candidate row in the
declared heat-kernel tower, then `P19-AN-IMPORT(m)` is falsified for that
tower. If none is proved, the honest status is not failure but an unresolved
finite-row audit.

Proof.

The positive direction is Theorem 0A.4. Conversely, Definition 0A.1 imports
Paper 16 only through `HK-AN-FINTPL-CLOSE(m)` on the same row plus the
residual subbattery/readout clause. Paper 16 Definition 9N.1Q.4 lists exactly
the finite row-data needed for `HK-AN-FINTPL-CLOSE(m)`, and Definition 0A.3
is exactly the residual-battery identification needed by Paper 19. Therefore
any listed failure blocks the import for the selected row. Only a proof that
all admissible rows fail upgrades this row obstruction to a tower-level
falsification. `square`

### Theorem 0A.6: Clean `SEL_0` Branch Closes `P19-AN-AUDIT(m)`

On the coefficient-only, time-only, clean finite-template `SEL_0` branch used
in Sections 8J.20--8J.24, `P19-AN-AUDIT(m)` holds.

More explicitly, take the Paper-16 analytic row `T_HK^std` and the Paper-19
direct-witness row to be the same pushed-forward heat-kernel row, with:

```text
same cutoff tower,
same finite block/collar template,
same loop/readout maps,
same clean counterterm convention,
same SEL_0 coefficient readout,
same pushed-forward law Gamma_i.
```

Then the audit clauses of Definition 0A.2 are satisfied with

```text
C_v^{row}=C_v^{YM2,SEL0}
```

and with residual-domination constant `D_sub=1`.

Proof.

Clause 1 is the row choice: throughout Sections 8J.20--8J.24 the finite
records are pushed forward from one heat-kernel whole-process law and the
same `SEL_0` readout. No auxiliary gauge chart or local coordinate is
exported.

Clause 2 is Paper 16 `HK-FIN-COUNT`: the standard finite block/collar
template has finite block-graph degree `Delta_B`, finite small-field label
count `L_ent`, and finite residual KP label count `L_KP`.

Clause 3 is Paper 16 Theorem 9L.1C.2 on the same row. The Paper-11
block-conditioned covariance source supplies the uniform Dirichlet/Poincare
constant `lambda_D>0`, and the finite collar template supplies
`R_blk<infinity`; hence Paper 16 uses `C_0=lambda_D^{-1}` and
`R_G=R_blk`.

Clause 4 is the `SEL_0` small-field verification in Section 8J.20. The
finite local vertex ledger through order `g_i^2`, neutral odd cancellation,
time-tangent absorption, and finite projection constants prove the
Paper-16 `HK-SF-YM2` clauses on the same pushed-forward character record,
with finite constant `C_v^{YM2,SEL0}`.

Clause 5 is the clean analytic convention. The counterterm convention is the
clean minimal convention of Paper 16 Theorem 9K.2G; the finite-template
large-field source is Paper 16 Theorem 9J.8, and the local `SEL_0`
large-field import is closed in Paper 19 by Theorem 8J.15M.1. The large-field
margin can therefore be raised to the value required by Paper 16 Theorem
9N.1Q.3 by passing to the declared AF tail.

Clause 6 holds because the clean starting radius is the finite maximum of
the finite small-field and counterterm starting radii on this row:

```text
r_res^clean=max(r_*,r_ct)<infinity.
```

Clause 7 is by choice of the same residual weight `m` in Paper 16
`HK-AN-FINTPL-CLOSE(m)` and in the Paper-19 residual-decoration ledger.

For clause 8, define `iota_j` as the inclusion of Paper-19 residual
decoration records into the Paper-16 residual KP records with the same
support, residual label, weight, and scalar readout. In the clean
coefficient-only branch, Paper 19 uses no residual decoration outside the
Paper-16 residual KP class. Thus

```text
rho_19,j = rho_16,j circ iota_j,
w_19,j(b)=w_16,j(iota_j(b)),
a_19,j(b)<=a_16,j(iota_j(b)).
```

Each preimage is either empty or a singleton after the shared finite label is
fixed. Therefore, for every Paper-16 residual label `c`,

```math
\sum_{b:\iota_j(b)=c}
a_{19,j}(b)e^{mw_{19,j}(b)}
\le
a_{16,j}(c)e^{mw_{16,j}(c)}.
```

This is Definition 0A.3 with `D_sub=1`. All eight clauses of
`P19-AN-AUDIT(m)` are proved. `square`

### Corollary 0A.7: Clean `SEL_0` Branch Imports The Paper-16 Analytic Constants

On the clean `SEL_0` branch of Theorem 0A.6,

```text
P19-AN-IMPORT(m)
```

holds. Consequently Paper 19 may use

```text
eta_res^* := eta_19^{res},
Delta_res^* := Delta_19^{an},
K_res^* := K_19^{an},
```

and

```math
\limsup_j\eta_{{res},j}^{bd}
\le
\eta_{19}^{res}<1.
```

Proof.

Theorem 0A.6 proves `P19-AN-AUDIT(m)`. Apply Theorem 0A.4. `square`

Paper 17 exports the selected-rate debit ledger:

```text
MG-UNIF(m_*)
```

with visible rate loss `Delta_tot,j` and block scale `ell_j`. Paper 19 uses
that ledger only through the Paper-18 pressure constants
`ell_j Delta_j^+` and `ell_j`.

Paper 18 exports the final conditional completion theorem. Paper 19's job is
not to invent another bridge. Its job is to prove or falsify the source
gates in that theorem.

## 0B. Paper 19 Main Claim Form

The strongest theorem Paper 19 can honestly aim for is:

```text
actual source constants pass
=> Paper 18 final minimal-debit theorem applies
=> AYM-CONF-CLOSE(m_*)
=> MGAP(m_*).
```

The source constants pass exactly when the following are proved on one frozen
whole-process tower:

```text
AYM-CONF-ACT-CRES-P16(c_R),
AYM-CONF-ACT-KQ-RATE(W_R),
c_R >= C_quot^crit(s_R,W_R),
AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*),
AYM-CONF-ACT-PI-THRESH(s_P,m_*),
AYM-CONF-ACT-LEDGER-SRC,
AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*).
```

If any of these fails, Paper 19 does not close confinement. It names the
obstruction.

## 0C. What Paper 19 Does And Does Not Prove

Paper 19 proves the following conditional result:

```text
actual Paper-19 source constants
=> Paper-18 minimal-debit confinement closure
=> AYM-CONF-CLOSE(m_*)
=> MGAP(m_*).
```

It also proves a complete scalar decision ledger for the strongest
direct-witness branch developed here:

```text
thick/co-scaling Creutz windows
+ AF-matched area S_j ~ g_i^{-2}
+ coefficient error R_H^opt < R_H^crit
+ decoration and transport losses below the AF-matched signal floor
=> c_15^tail > 0.
```

Paper 19 does not prove unconditional actual `4D SU(N)` confinement. The
remaining source estimates are explicitly named:

```text
relative character error:
  R_H^opt = limsup_j g_i^{-2} delta_j exp(a_j)
    < R_H^crit;

loss budget:
  L_AFM^sharp
    = limsup_j (Delta_dec,j^bd + T_loss,j^bd)
    < Sig_AFM.
```

If those two estimates are later proved on the same whole-process tower,
Paper 19 supplies the route into Paper 18. If either is falsified, Paper 19
identifies the exact obstruction for this direct-witness confinement branch.

The phrase "same whole-process tower" is structural: it means one finite
restriction family, one readout convention, one scale selector, and one debit
ledger. It does not smuggle in an area law or positive string tension.

## 1. Frozen Whole-Process Source Tower

### Definition 1.1: `P19-TOWER`

`P19-TOWER` is the structural same-record tower for Paper 19. It is not a
confinement axiom, not an area-law axiom, and not by itself an existence
theorem for continuum `4D SU(N)` Yang-Mills.

The tower is deliberately split into four logically different layers.

**Layer A: finite restriction structure.** `P19-TOWER-EXIST` consists of:

1. a whole-process Wilson-loop record law `Law_*`;
2. a cofinal family of finite record algebras `F_j`;
3. restriction maps

   ```math
   \rho_j:\mathsf{Law}_*\to F_j;
   ```

This layer says only that one law and one family of finite restrictions have
been declared. It does not say that the law has an area law, a positive mass
gap, or the correct continuum `SU(N)` scaling.

**Layer B: readout and window compatibility.** `P19-TOWER-READOUT` consists
of:

1. Paper-18 window maps from each Paper-17 probe battery `G_j` to a finite
   Creutz window `D_CR,j` and a finite Paper-15 battery `B_15,j`;
2. Wilson-loop, Creutz, marked-loop, Polyakov-line, and endpoint protocol
   readouts typed as scalar records or boundary instruments on `F_j`;
3. compatibility of those readouts with the restrictions `rho_j`.

This layer supplies the language in which source estimates can be evaluated.
It does not supply positivity of the estimates.

**Layer C: debit bookkeeping.** `P19-TOWER-DEBIT` consists of one debit
register assigning each loss to exactly one bucket:

```text
reserve,
loop-modulus,
marked endpoint/local,
marked KP,
Paper-17 selected-rate,
audit-only zero loss.
```

This layer prevents double counting. It is not a smallness estimate.

**Layer D: scale declaration.** `P19-TOWER-SCALE` records which AF trajectory,
block scale, cofinal windows, character channel, and regulator convention are
being tested. It is a selector declaration. It does not assert that the
selected branch satisfies

```text
R_H^opt < R_H^crit
or
L_AFM^sharp < Sig_AFM.
```

In this paper the shorthand `P19-TOWER` means the conjunction of Layers A--D:

```text
P19-TOWER
:= P19-TOWER-EXIST
 + P19-TOWER-READOUT
 + P19-TOWER-DEBIT
 + P19-TOWER-SCALE.
```

All Paper-19 constants must be functions of `rho_j(Law_*)` and the declared
finite instruments. If a constant is imported from a different regulator
tower, endpoint convention, gauge chart, or debit register, `P19-TOWER`
fails.

The following are explicitly not included in `P19-TOWER` and must be proved
or named separately:

```text
positive Creutz reserve,
quotient loop-modulus smallness,
pressure positivity,
cofinal physical rate,
R_H^opt < R_H^crit,
L_AFM^sharp < Sig_AFM,
area-law confinement,
continuum Yang-Mills existence,
Clay mass gap.
```

This split is the anti-circularity convention for Paper 19.

### Lemma 1.2: `P19-TOWER` Proves The Paper-18 Ledger Source

If `P19-TOWER` holds and all constants in the reserve-loop and pressure
attacks are evaluated by the declared restrictions `rho_j`, then
`AYM-CONF-ACT-LEDGER-SRC` holds.

Proof.

The maps `rho_j` supply one frozen law and one family of finite restrictions.
The readout layer types the endpoint instruments and makes them enter only
through scalar marked-loop, Wilson-loop, Creutz, or Polyakov records. The
debit layer prevents double counting. These are exactly the structural
clauses of Paper 18's `AYM-CONF-ACT-LEDGER-SRC`.

No positivity, area law, continuum construction, or source inequality is used
in this lemma. Those enter only through the later named hypotheses
`P19-CRES-*`, `P19-KQ-SRC`, `P19-PI-*`, `P19-COF`,
`R_H^opt<R_H^crit`, and `L_AFM^sharp<Sig_AFM`. `square`

## 2. Reserve Source Attack

The first real source gate is the raw reserve import
`AYM-CONF-ACT-CRES-P16(c_R)`. This is where actual four-dimensional
dynamics first enters.

### Definition 2.1: Raw Reserve Export `P19-CRES-RAW(c_R)`

`P19-CRES-RAW(c_R)` holds on a tail `j>=J_C` when Paper 16 exports, on
`P19-TOWER`, a raw surface reserve

```math
M_{{\rm SUB},j}^{{\rm bd}}
\ge
c_R
>
0
```

for every `j>=J_C`, in the same block-area normalization used by Paper 18.

The raw reserve may be supplied by `HK-SURF-CLOSE` or by a stronger
same-ledger source theorem. It may not include the Paper-18 extraction
losses if those losses will be charged again in `C_quot^crit`.

### Definition 2.2: Debited Creutz Reserve Export `P19-CRES-DEB(c_R)`

`P19-CRES-DEB(c_R)` holds on a tail `j>=J_C` when Paper 16 exports

```math
HK-CREUTZ-CLOSE(M_{{\rm SUB},j}^{{\rm bd}},
L_{{\rm bat},j},L_{{\rm reg},j},L_{{\rm vol},j},L_{{\rm shape},j})
```

and hence

```math
M_{{15},j}^{{\rm bd}}
=
M_{{\rm SUB},j}^{{\rm bd}}
-L_{{\rm bat},j}
-L_{{\rm reg},j}
-L_{{\rm vol},j}
-L_{{\rm shape},j}
\ge
c_R
>
0
```

for every `j>=J_C`.

In this convention Paper 18's threshold calculation must set the four
extraction losses

```text
L_bat, L_reg, L_vol, L_shape
```

to zero in `L_R`; otherwise the same loss is paid twice.

### Theorem 2.3: Paper-16 Reserve Export Proves `AYM-CONF-ACT-CRES-P16`

If either `P19-CRES-RAW(c_R)` or `P19-CRES-DEB(c_R)` holds on `P19-TOWER`,
then `AYM-CONF-ACT-CRES-P16(c_R)` holds.

Proof.

The raw route is exactly Paper 18's raw surface-reserve export. The debited
route is exactly Paper 18's already-debited Creutz-reserve export, together
with the no-double-debit convention. Thus the imported constant is a
same-ledger lower bound of size `c_R` in one of the two allowed Paper-18
formats. `square`

### Definition 2.4: Reserve Falsification `P19-CRES-FALS(c_R)`

`P19-CRES-FALS(c_R)` holds when a same-ledger upper bound proves that neither
allowed reserve convention can supply `c_R`. Concretely, on every cofinal
tail, either

```math
\liminf_j M_{{\rm SUB},j}^{{\rm bd}}<c_R
```

for the raw convention, or

```math
\liminf_j M_{{15},j}^{{\rm bd}}<c_R
```

for the already-debited convention, after all quantities have been put in
the same block-area units.

This does not falsify confinement. It falsifies the declared Paper-18
minimal-debit source route with that reserve constant.

## 3. Quotient Loop-Modulus Attack

The second real source gate is `AYM-CONF-ACT-KQ-RATE(W_R)`. It does not ask
for a uniform positive raw Wilson-loop denominator. It asks only for the
quotient that enters the Creutz log-ratio debit to be bounded:

```math
{\omega_j^+\over\kappa_j^-}\le W_R.
```

### Definition 3.1: Slot Denominator Profile `P19-SLOT(d_j)`

For every cofinal window `j`, let `Slots_j` be the finite four-slot Creutz
families used by Paper 18. `P19-SLOT(d_j)` holds when the renormalized slot
expectations satisfy

```math
\kappa_j^-
:=
\min_{\alpha\in Slots_j}
\left|
E_{\rho_j(Law_*)}(T_\alpha^{ren})
\right|
\ge
d_j
>
0.
```

The number `d_j` may decay with `j`. Paper 19 does not require an absolute
tail denominator unless a later theorem explicitly says so.

### Definition 3.2: Loop-Continuity Gauge `P19-LC-GAUGE(Xi_j)`

`P19-LC-GAUGE(Xi_j)` holds when Paper 16's `HK-LC-CLOSE` and
`HK-LC-TRANSPORT` export, for the same slots and restrictions, a monotone
cutoff gauge `Xi_j(alpha)` with

```math
\Omega_j(\alpha)\le \Xi_j(\alpha),
```

where `Omega_j(alpha)` is the total loop/readout continuity error entering
Paper 18's quotient estimate, and

```math
\Xi_j(\alpha)\to0
```

along the directed cutoff refinement allowed by `P19-TOWER`.

### Definition 3.3: Quotient Rate Selector `P19-KQ-SRC(W_R)`

`P19-KQ-SRC(W_R)` holds when there are:

1. a slot denominator profile `P19-SLOT(d_j)`;
2. a loop-continuity gauge `P19-LC-GAUGE(Xi_j)`;
3. a cofinal selector `alpha_Q(j)`;

such that, for every sufficiently large `j`,

```math
\Xi_j(\alpha_Q(j))
\le
W_R d_j.
```

### Theorem 3.4: Quotient Source Proves `AYM-CONF-ACT-KQ-RATE`

If `P19-KQ-SRC(W_R)` holds, then `AYM-CONF-ACT-KQ-RATE(W_R)` holds.

Proof.

Paper 18's `AYM-CONF-ACT-KQ-RATE(W_R)` asks for a denominator profile, a
Paper-16 error gauge, and a cutoff selector such that the selected error is
bounded by `W_R` times the denominator profile. These are exactly the three
clauses of `P19-KQ-SRC(W_R)`. `square`

### Definition 3.5: Quotient Falsification `P19-KQ-FALS(W_R)`

`P19-KQ-FALS(W_R)` holds when the declared slot family and Paper-16 loop
continuity cannot make the quotient small enough. A sufficient falsifier is:

```math
\limsup_j
\inf_{\alpha}
{\Omega_j(\alpha)\over\kappa_j^-}
>
W_R.
```

If the limsup is infinite, no finite `W_R` is available for the declared
slot family. The appropriate response is then to change the finite-window
schedule, change the renormalized readout, or accept that the Paper-18
minimal-debit route fails.

## 4. Reserve-Loop Threshold

### Definition 4.1: Paper-19 Reserve-Loop Threshold

Assume the non-fragile constants are finite:

```math
\gamma_R>0,
\quad
L_R<\infty,
\quad
e_R<\infty,
\quad
E_R<\infty.
```

Given `W_R<infinity` and demanded margin `s_R>0`, define

```math
C_{{\rm quot}}^{{\rm crit}}(s_R,W_R)
:=
L_R
+
{e_R+2\max\{E_R,4W_R\}+s_R\over\gamma_R}.
```

The threshold gate `P19-RLD-THRESH(c_R,W_R,s_R)` is:

```math
c_R\ge C_{{\rm quot}}^{{\rm crit}}(s_R,W_R).
```

### Theorem 4.2: First Source Closure

Assume on `P19-TOWER`:

```text
P19-CRES-RAW(c_R) or P19-CRES-DEB(c_R),
P19-KQ-SRC(W_R),
P19-RLD-THRESH(c_R,W_R,s_R).
```

Then Paper 18's first actual gate holds:

```text
AYM-CONF-ACT-RLD-TAIL
```

with reserve-loop margin at least `s_R`.

Proof.

Theorem 2.3 gives `AYM-CONF-ACT-CRES-P16(c_R)`. Theorem 3.4 gives
`AYM-CONF-ACT-KQ-RATE(W_R)`. The threshold gate is exactly Paper 18's
`c_R >= C_quot^crit(s_R,W_R)`. Paper 18, Theorem 4.6I.47z.2e.21am, gives
`AYM-CONF-ACT-RLD-TAIL`. `square`

### Corollary 4.3: First Bottleneck Verdict

The first bottleneck is now completely explicit:

```text
same-ledger raw/debited reserve
versus
extraction + readout + quotient loop-modulus threshold.
```

If Theorem 4.2 passes, Paper 19 may move to the pressure source. If it
fails, the obstruction is one of:

1. reserve collapse: `P19-CRES-FALS(c_R)`;
2. quotient loop-modulus failure: `P19-KQ-FALS(W_R)`;
3. scalar threshold failure: `c_R<C_quot^crit(s_R,W_R)`;
4. ledger failure: the constants were not computed on `P19-TOWER`.

## 5. Pressure Source Attack

After Theorem 4.2, Paper 18 supplies

```math
\Sigma_j^{RLD}\ge s_R>0
```

on the common tail. The remaining question is whether marked geometry,
marked KP, and Paper-17 selected-rate debits consume that retained reserve.

### Definition 5.1: Pressure Source Constants `P19-PI-SRC(s_R,m_*)`

`P19-PI-SRC(s_R,m_*)` holds when, on the same tail and tower as the
reserve-loop pass, the following constants are exported:

```math
\alpha_P>0,
\quad
e_P,h_P,\lambda_P,D_P,Q_P\ge0,
\quad
\ell_P>0,
```

with, for every sufficiently large `j`,

```math
\alpha_j^-\ge\alpha_P,
```

```math
e_j^+\le e_P,\quad
h_j^+\le h_P,\quad
\lambda_j^+\le\lambda_P,\quad
D_j^+\le D_P,
```

and

```math
\ell_j\Delta_j^+\le Q_P,
\quad
\ell_j\le\ell_P.
```

The sources are:

1. `alpha_P,e_P` from Paper-18 marked geometry and marked-loss ledgers;
2. `h_P,lambda_P,D_P` from endpoint-enlarged Paper-14/Paper-15 marked KP
   estimates;
3. `Q_P,ell_P` from Paper 17's selected-rate and block-scale ledger.

### Definition 5.2: Pressure Threshold `P19-PI-THRESH(s_P,m_*)`

Given the constants of `P19-PI-SRC(s_R,m_*)`, define

```math
A_P:=\alpha_Ps_R,
```

```math
K_P:=e_P+h_P+\lambda_P+D_P,
```

and

```math
T_P(m_*):=2Q_P+4\ell_Pm_*.
```

The pressure threshold is:

```math
A_P-K_P-T_P(m_*)\ge s_P>0.
```

Equivalently, for fixed constants and `ell_P>0`, the target rate must obey

```math
m_*
\le
{\alpha_Ps_R-e_P-h_P-\lambda_P-D_P-2Q_P-s_P\over 4\ell_P}.
```

### Theorem 5.3: Pressure Source Closure

Assume `AYM-CONF-ACT-RLD-TAIL` holds with margin `s_R`. If
`P19-PI-SRC(s_R,m_*)` and `P19-PI-THRESH(s_P,m_*)` hold on `P19-TOWER`,
then

```text
AYM-CONF-ACT-PI-TAIL(m_*)
```

holds with pressure margin at least `s_P`.

Proof.

The data of `P19-PI-SRC(s_R,m_*)` are exactly Paper 18's source import
`AYM-CONF-ACT-PI-SRC-IMPORT(s_R,m_*)`. The threshold is exactly
`AYM-CONF-ACT-PI-THRESH(s_P,m_*)`. Paper 18, Theorem
4.6I.47z.2e.24r, gives `AYM-CONF-ACT-PI-TAIL(m_*)`. `square`

## 6. Cofinal Survival

### Definition 6.1: `P19-COF(s_R,s_P,m_*)`

`P19-COF(s_R,s_P,m_*)` holds when the windows on which the reserve-loop and
pressure sources pass form a cofinal scheduled family `j_n`, and on that
family:

```math
\Sigma_{j_n}^{RLD}\ge s_R>0,
\quad
\Sigma_{j_n}^{PI}(m_*)\ge s_P>0.
```

The local Paper-18 worksheets

```text
AYM-CONF-GAMMA-MD-WORK_j_n,
AYM-CONF-ACT-WORK_j_n,
AYM-CONF-ACT-RLD-WORK_j_n,
AYM-CONF-ACT-PI-WORK_j_n(m_*)
```

must remain populated by the same restrictions `rho_j_n(Law_*)`.

### Lemma 6.2: Cofinal Source

If `P19-COF(s_R,s_P,m_*)` and `P19-TOWER` hold, then
`AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)` holds.

Proof.

`P19-COF` supplies the cofinal scheduler, local worksheets, and positive
RLD/PI margins. `P19-TOWER` supplies the same-law and same-debit
requirements. These are exactly the clauses of Paper 18's
`AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)`. `square`

## 7. Main Paper-19 Closure Theorem

### Theorem 7.1: Source Constants Close Paper 18

Assume on one frozen whole-process tower:

1. `P19-TOWER`;
2. `P16-LAW-IMPORT`;
3. `AYM-CONF-WIN-SCHED`;
4. `P19-CRES-RAW(c_R)` or `P19-CRES-DEB(c_R)`;
5. `P19-KQ-SRC(W_R)`;
6. `P19-RLD-THRESH(c_R,W_R,s_R)`;
7. `P19-PI-SRC(s_R,m_*)`;
8. `P19-PI-THRESH(s_P,m_*)`;
9. `P19-COF(s_R,s_P,m_*)`.

Then

```text
AYM-CONF-CLOSE(m_*)
=> MGAP(m_*).
```

Proof.

Lemma 1.2 gives `AYM-CONF-ACT-LEDGER-SRC`. Theorem 2.3 gives
`AYM-CONF-ACT-CRES-P16(c_R)`. Theorem 3.4 gives
`AYM-CONF-ACT-KQ-RATE(W_R)`. The threshold in clause 6 is
`c_R>=C_quot^crit(s_R,W_R)`, so Theorem 4.2 gives
`AYM-CONF-ACT-RLD-TAIL`. Theorem 5.3 gives
`AYM-CONF-ACT-PI-TAIL(m_*)`. Lemma 6.2 gives
`AYM-CONF-ACT-COF-SRC(s_R,s_P,m_*)`.

Now Paper 18, Theorem 4.6I.50l, applies and gives
`AYM-CONF-CLOSE(m_*)=>MGAP(m_*)`. `square`

### Corollary 7.2: What Would Count As Closing `4D SU(N)` Confinement

Paper 19 closes actual `4D SU(N)` confinement only if the nine hypotheses of
Theorem 7.1 are proved from the actual continuum Wilson-loop record law.
The theorem is not closed by naming the constants. It is closed only by
proving their same-ledger bounds.

## 8. First Source-Constant Work Plan

The first source task is the reserve-loop threshold:

```math
c_R
\ge
L_R
+
{e_R+2\max\{E_R,4W_R\}+s_R\over\gamma_R}.
```

This splits into three concrete subproblems.

### 8.1 Prove Or Falsify The Reserve Lower Bound

Use Paper 16's `HK-CREUTZ-CLOSE`:

```math
M_{{15},j}^{{\rm bd}}
=
M_{{\rm SUB},j}^{{\rm bd}}
-L_{{\rm bat},j}
-L_{{\rm reg},j}
-L_{{\rm vol},j}
-L_{{\rm shape},j}.
```

The route passes if either:

```math
\inf_{j\ge J_C}M_{{\rm SUB},j}^{{\rm bd}}\ge c_R>0
```

with extraction losses paid later, or:

```math
\inf_{j\ge J_C}M_{{15},j}^{{\rm bd}}\ge c_R>0
```

with the extraction losses removed from `L_R`.

The route fails in its absolute-tail form if the same-ledger upper bound
forces both infima to vanish on every cofinal tail. In that case the paper
must switch to a finite-window or normalized reserve route; it may not
pretend that an absolute `c_R>0` exists.

### 8.2 Prove Or Falsify The Quotient Bound

Choose a slot profile `d_j` and loop-continuity gauge `Xi_j`. The quotient
route passes if a selector exists with

```math
\Xi_j(\alpha_Q(j))\le W_R d_j
```

cofinally. It fails if

```math
\limsup_j\inf_\alpha{\Omega_j(\alpha)\over\kappa_j^-}>W_R.
```

The point is not to prove denominators stay uniformly away from zero. The
point is to prove that loop-continuity error is small relative to the
denominator actually used by the finite Creutz readout.

### 8.3 Test The Scalar Threshold

Once `c_R` and `W_R` are known, the source route passes only if

```math
s_R
\le
\gamma_R(c_R-L_R)
-e_R
-2\max\{E_R,4W_R\}.
```

Thus the largest available reserve-loop margin is

```math
s_R^{max}
:=
\gamma_R(c_R-L_R)
-e_R
-2\max\{E_R,4W_R\}.
```

The first bottleneck is closed exactly when

```math
s_R^{max}>0.
```

### 8.4 First Reserve-Loop Worksheet

For the first actual calculation, fill the following ledger on one frozen
tower and one declared cofinal window schedule.

| Symbol | Meaning | Source | Needed check |
| --- | --- | --- | --- |
| `c_R` | raw or already-debited reserve lower bound | `P19-CRES-RAW` or `P19-CRES-DEB` | `c_R>0` |
| `gamma_R` | scalar Creutz/readout calibration lower bound | Paper-15/Paper-18 readout ledger | `gamma_R>0` |
| `L_R` | extraction losses not already paid in `c_R` | battery/regulator/volume/shape debit register | finite, no double debit |
| `e_R` | reserve readout and alignment error | Paper-18 reserve error ledger | finite |
| `E_R` | direct loop readout error in the log-modulus debit | Paper-18 loop-modulus worksheet | finite |
| `d_j` | finite slot denominator profile | `P19-SLOT(d_j)` | positive for each window |
| `Xi_j(alpha)` | Paper-16 loop-continuity error gauge | `HK-LC-CLOSE` and `HK-LC-TRANSPORT` | tends to zero under refinement |
| `W_R` | quotient loop-modulus bound | `Xi_j(alpha_Q(j))<=W_R d_j` | finite |
| `s_R^{max}` | available reserve-loop margin | worksheet output | positive |

The worksheet passes when

```math
s_R^{max}
=
\gamma_R(c_R-L_R)
-e_R
-2\max\{E_R,4W_R\}
>0.
```

It fails for the declared route when a same-ledger upper-bound calculation
proves

```math
\gamma_R(c_R-L_R)
-e_R
-2\max\{E_R,4W_R\}
\le0
```

for every cofinal reserve/quotient selector. If the failure comes from a
vanishing raw denominator but the quotient bound still passes, the route has
not failed. If the failure comes from `c_R` itself, the proof must replace
the absolute reserve with a finite-window or normalized reserve route.

### Theorem 8.5: Reserve-Loop Worksheet Proves Step 1

Assume `P19-TOWER`, the worksheet entries in Section 8.4, and

```math
s_R^{max}>0.
```

Choose any

```math
0<s_R\le s_R^{max}.
```

Then `AYM-CONF-ACT-RLD-TAIL` holds.

Proof.

The worksheet gives `c_R>0`, `P19-CRES-RAW(c_R)` or
`P19-CRES-DEB(c_R)`, and `P19-KQ-SRC(W_R)`. The inequality
`s_R<=s_R^{max}` is equivalent to

```math
c_R
\ge
L_R
+
{e_R+2\max\{E_R,4W_R\}+s_R\over\gamma_R}
=
C_{{\rm quot}}^{{\rm crit}}(s_R,W_R).
```

Thus `P19-RLD-THRESH(c_R,W_R,s_R)` holds. Theorem 4.2 gives
`AYM-CONF-ACT-RLD-TAIL`. `square`

## 8A. Step-1 Tail Decision: Prove Or Falsify `c_R`, `W_R`, And `s_R^{max}`

The previous worksheet is useful only after the constants are known. This
section removes the remaining freedom by defining the exact tail envelopes
for the declared tower. Once these envelopes are computed or bounded
sharply, Step 1 has a definite verdict.

### Definition 8A.1: Reserve Branches And Tail Reserve Capacity

Let `b` be one of the two Paper-18 reserve conventions:

```text
b = raw,
b = deb.
```

For the raw branch set

```math
R_{{raw},j}:=M_{{\rm SUB},j}^{{\rm bd}}.
```

For the already-debited branch set

```math
R_{{deb},j}:=M_{{15},j}^{{\rm bd}}
=
M_{{\rm SUB},j}^{{\rm bd}}
-L_{{\rm bat},j}
-L_{{\rm reg},j}
-L_{{\rm vol},j}
-L_{{\rm shape},j}.
```

Let `L_{R,b}` denote the reserve-loop loss still unpaid after choosing branch
`b`. Thus `L_{R,raw}` includes the battery, regulator, volume, and shape
losses if they are not already charged, while `L_{R,deb}` removes exactly
those four losses from the later debit register.

The tail reserve capacity of branch `b` is

```math
c_b^{tail}
:=
\sup_J\inf_{j\ge J}R_{b,j}
=
\liminf_{j\to\infty}R_{b,j}.
```

Branch `b` proves a tail reserve constant `c_R` whenever

```math
0<c_R<c_b^{tail},
```

or whenever `c_R=c_b^{tail}` and the infimum is actually attained on a
cofinal tail. Branch `b` falsifies the declared constant `c_R` whenever

```math
c_R>c_b^{tail}.
```

If `c_R=c_b^{tail}` and no eventual attainment is known, the endpoint is
not a proof-quality constant; one must lower `c_R` by an arbitrary small
slack.

### Lemma 8A.2: Reserve Envelope Is The Sharp `c_R` Test

For a fixed branch `b`, no same-ledger tail proof can export a reserve lower
bound larger than `c_b^{tail}`. Conversely every strict lower constant below
`c_b^{tail}` is exportable on a sufficiently far tail.

Proof.

The first claim is the definition of liminf: if `c_R>c_b^{tail}`, then every
tail contains some `j` with `R_{b,j}<c_R`, so the eventual lower bound fails.
If `c_R<c_b^{tail}`, choose `J` so that `inf_{j>=J}R_{b,j}>=c_R`. This is
exactly `P19-CRES-RAW(c_R)` for `b=raw` or `P19-CRES-DEB(c_R)` for
`b=deb`, with the corresponding no-double-debit convention. `square`

### Definition 8A.3: Quotient Tail Capacity

For each cofinal window `j`, let `A_j` be the declared admissible set of
cutoff refinements, loop approximants, and readout selectors allowed by
`P19-TOWER`. For `alpha in A_j`, write

```math
d_j(\alpha)
:=
\kappa_j^-(\alpha),
```

and let `Xi_j(alpha)` be the Paper-16 loop-continuity gauge from
`P19-LC-GAUGE`. Define the best quotient available in window `j` by

```math
q_j
:=
\inf_{\alpha\in A_j,\ d_j(\alpha)>0}
{\Xi_j(\alpha)\over d_j(\alpha)}.
```

The quotient tail capacity is

```math
W^{tail}
:=
\limsup_{j\to\infty}q_j.
```

If `W^{tail}<infinity`, the quotient source proves `P19-KQ-SRC(W_R)` for
every strict constant

```math
W_R>W^{tail}.
```

It falsifies any declared strict quotient constant

```math
W_R<W^{tail}.
```

If `W^{tail}=infinity`, no finite `W_R` is available for the declared
window schedule and loop-readout family.

### Lemma 8A.4: Quotient Envelope Is The Sharp `W_R` Test

Assume the admissible selector sets `A_j` are exactly the selectors allowed
by the declared tower. Then `W^{tail}` is the sharp cofinal quotient
constant for Step 1.

Proof.

If `W_R>W^{tail}`, the definition of limsup gives a tail on which
`q_j<=W_R`. For each such `j`, choose `alpha_Q(j)` with

```math
{\Xi_j(\alpha_Q(j))\over d_j(\alpha_Q(j))}
\le W_R
```

after an arbitrarily small slack if the infimum is not attained. This is
`P19-KQ-SRC(W_R)`. If `W_R<W^{tail}`, then infinitely many cofinal windows
have `q_j>W_R`, so no admissible selector can satisfy
`Xi_j(alpha_Q(j))<=W_R d_j(alpha_Q(j))` on a cofinal tail. `square`

### Definition 8A.5: Best Possible Step-1 Margin On The Declared Route

For branch `b`, define the sharp reserve-loop tail margin

```math
S_b^{tail}
:=
\gamma_R\left(c_b^{tail}-L_{R,b}\right)
-e_R
-2\max\{E_R,4W^{tail}\}.
```

The declared Paper-18 Step-1 route has best possible tail margin

```math
s_{R,route}^{tail}
:=
\max_{b\in\{raw,deb\}}S_b^{tail},
```

where branches whose debit convention is not populated on `P19-TOWER` are
omitted from the maximum.

### Theorem 8A.6: Step-1 Pass/Fail Decision

Assume:

1. `P19-TOWER` is fixed;
2. at least one reserve branch has a populated same-ledger sequence
   `R_{b,j}`;
3. the admissible quotient selector sets `A_j` are fixed;
4. `gamma_R>0`, `e_R<infinity`, `E_R<infinity`, and `L_{R,b}<infinity`;
5. the envelopes `c_b^{tail}` and `W^{tail}` are sharp, meaning they are
   actual liminf/limsup values for the declared sequences, not merely
   optimistic estimates.

Then:

1. If `s_{R,route}^{tail}>0`, Step 1 is proved. More precisely, there are a
   branch `b`, constants `c_R`, `W_R`, and a margin `s_R>0` such that
   `P19-CRES-RAW(c_R)` or `P19-CRES-DEB(c_R)`, `P19-KQ-SRC(W_R)`, and
   `P19-RLD-THRESH(c_R,W_R,s_R)` all hold.
2. If `s_{R,route}^{tail}<=0`, Step 1 is falsified for the declared
   Paper-18 minimal-debit route, tower, window schedule, and selector
   family: no positive `s_R` can be obtained from any allowed pair
   `(c_R,W_R)`.

Proof.

If `s_{R,route}^{tail}>0`, choose a branch `b` with `S_b^{tail}>0`. Pick
strict constants

```math
0<c_R<c_b^{tail},
\qquad
W_R>W^{tail}
```

so close to their envelopes that

```math
\gamma_R(c_R-L_{R,b})
-e_R
-2\max\{E_R,4W_R\}
>0.
```

This is possible by the strict positivity of `S_b^{tail}` and continuity of
the displayed scalar expression in `c_R` and `W_R`. Lemma 8A.2 proves the
reserve source. Lemma 8A.4 proves the quotient source. Choose

```math
0<s_R\le
\gamma_R(c_R-L_{R,b})
-e_R
-2\max\{E_R,4W_R\}.
```

Then Theorem 8.5 proves `AYM-CONF-ACT-RLD-TAIL`.

Conversely assume `s_{R,route}^{tail}<=0`. Every proof-quality reserve
constant must satisfy `c_R<=c_b^{tail}` up to endpoint attainment, and every
proof-quality quotient constant must satisfy `W_R>=W^{tail}` up to endpoint
attainment. Since the scalar expression is increasing in `c_R` and
nonincreasing in `W_R`, every allowed branch obeys

```math
\gamma_R(c_R-L_{R,b})
-e_R
-2\max\{E_R,4W_R\}
\le
S_b^{tail}
\le
s_{R,route}^{tail}
\le0.
```

Thus no positive `s_R` can satisfy the Paper-18 threshold on the declared
route. `square`

### 8A.7 Actual Source-Paper Verdict For Step 1

The present source papers do not yet give numerical or symbolic sharp values
for `c_b^{tail}` and `W^{tail}` on the actual `4D SU(N)` continuum tower.
They give the following rigorous imports:

1. Paper 15 gives an explicit finite-battery Creutz reserve formula
   `M_15^{bd}` and proves that positivity of that number survives the
   connected-polymer/decorated Creutz extraction.
2. Paper 16 packages the continuum transport as
   `HK-CREUTZ-CLOSE`, with
   `M_15^{bd}=M_SUB^{bd}-L_bat-L_reg-L_vol-L_shape>0`.
3. Paper 16 packages loop continuity as `HK-LC-CLOSE`, with finite-battery
   moduli `omega_j` and summable transport tails.
4. Paper 19 now proves that those imports close Step 1 exactly when the
   sharp envelopes satisfy

   ```math
   \max_b
   \left[
   \gamma_R\left(c_b^{tail}-L_{R,b}\right)
   -e_R
   -2\max\{E_R,4W^{tail}\}
   \right]
   >0.
   ```

Therefore Step 1 is now fully reduced but not unconditionally proved for
actual `4D SU(N)`. It is also not falsified by the current source papers.
The remaining missing data are exactly:

```text
sharp same-ledger tail reserve capacity c_b^{tail},
sharp same-ledger quotient capacity W^{tail},
and the scalar sign of s_{R,route}^{tail}.
```

## 8B. Step 1a: Debited Reserve Envelope `c_{deb}^{tail}`

This section attacks the cleanest reserve branch first: the already-debited
Creutz reserve. The virtue of this branch is ontological and practical. Once
the branch is chosen, battery extraction, regulator transport, finite-volume
exhaustion, and loop-shape/cusp losses are no longer available for later
debits. They have already been paid inside `M_15^{bd}`.

### Definition 8B.1: Debited Reserve Sequence

On `P19-TOWER`, define the Paper-16 debited reserve sequence by

```math
R_{{deb},j}
:=
M_{{15},j}^{{\rm bd}}
:=
M_{{\rm SUB},j}^{{\rm bd}}
-\Lambda_j,
```

where

```math
\Lambda_j
:=
L_{{\rm bat},j}
+L_{{\rm reg},j}
+L_{{\rm vol},j}
+L_{{\rm shape},j}.
```

The Step-1a debited reserve envelope is

```math
c_{{deb}}^{tail}
:=
\liminf_{j\to\infty}M_{{15},j}^{{\rm bd}}
=
\liminf_{j\to\infty}
\left(M_{{\rm SUB},j}^{{\rm bd}}-\Lambda_j\right).
```

The debited reserve branch is proof-positive exactly when

```math
c_{{deb}}^{tail}>0.
```

In that case any strict constant

```math
0<c_R<c_{{deb}}^{tail}
```

is a valid `P19-CRES-DEB(c_R)` export on a sufficiently far tail.

### Lemma 8B.2: Exact Debited-Branch Pass/Falsification Test

For the declared tower and debited reserve sequence:

1. if `c_{deb}^{tail}>0`, then the debited branch proves
   `AYM-CONF-ACT-CRES-P16(c_R)` for every strict
   `0<c_R<c_{deb}^{tail}`;
2. if `c_{deb}^{tail}<=0`, then the debited branch cannot supply any
   positive tail reserve constant `c_R>0`.

Proof.

This is Lemma 8A.2 specialized to `b=deb`. If the liminf is positive, every
strict lower constant below it is eventually below all `M_15,j^{bd}`. If the
liminf is nonpositive, every positive `c_R` is exceeded downward on
arbitrarily far windows, so no eventual bound `M_15,j^{bd}>=c_R` can hold.
`square`

### Definition 8B.3: Component Tail Envelopes

For a component-level attack, define:

```math
m_{{SUB}}^-:=\liminf_{j\to\infty}M_{{\rm SUB},j}^{{\rm bd}},
```

```math
\lambda_{{bat}}^+:=\limsup_{j\to\infty}L_{{\rm bat},j},
\quad
\lambda_{{reg}}^+:=\limsup_{j\to\infty}L_{{\rm reg},j},
```

```math
\lambda_{{vol}}^+:=\limsup_{j\to\infty}L_{{\rm vol},j},
\quad
\lambda_{{shape}}^+:=\limsup_{j\to\infty}L_{{\rm shape},j},
```

and

```math
\Lambda^+
:=
\lambda_{{bat}}^+
+\lambda_{{reg}}^+
+\lambda_{{vol}}^+
+\lambda_{{shape}}^+.
```

The conservative lower envelope is

```math
c_{{deb}}^{low}
:=
m_{{SUB}}^- - \Lambda^+.
```

For falsification, also define:

```math
m_{{SUB}}^+:=\limsup_{j\to\infty}M_{{\rm SUB},j}^{{\rm bd}},
```

```math
\Lambda^-:=\liminf_{j\to\infty}\Lambda_j.
```

The conservative upper envelope is

```math
c_{{deb}}^{up}
:=
m_{{SUB}}^+ - \Lambda^-.
```

### Theorem 8B.4: Component Test For `c_{deb}^{tail}`

The component envelopes imply:

```math
c_{{deb}}^{tail}
\ge
c_{{deb}}^{low}
=
m_{{SUB}}^- - \Lambda^+.
```

Consequently, if

```math
m_{{SUB}}^- > \Lambda^+,
```

then the debited reserve branch passes with every strict

```math
0<c_R<m_{{SUB}}^- - \Lambda^+.
```

Conversely,

```math
c_{{deb}}^{tail}
\le
c_{{deb}}^{up}
=
m_{{SUB}}^+ - \Lambda^-.
```

Therefore, if

```math
m_{{SUB}}^+ \le \Lambda^-,
```

then the debited reserve branch is falsified in its absolute-tail form:
`c_{deb}^{tail}<=0`.

Proof.

The lower bound follows from the elementary liminf inequality

```math
\liminf_j(a_j-b_j)
\ge
\liminf_j a_j-\limsup_j b_j,
```

applied to `a_j=M_SUB,j^{bd}` and `b_j=Lambda_j`, together with

```math
\limsup_j\Lambda_j
\le
\Lambda^+.
```

The positivity claim follows immediately.

For the upper bound, use

```math
\liminf_j(a_j-b_j)
\le
\limsup_j(a_j-b_j)
\le
\limsup_j a_j-\liminf_j b_j.
```

If `m_SUB^+<=Lambda^-`, the right-hand side is nonpositive, so
`c_deb^{tail}<=0`. `square`

### Definition 8B.5: Paper-15 Direct Creutz Witness

Paper 15 also supplies a direct finite-battery Creutz reserve:

```math
M_{{15},j}^{{bd,15}}
=
u_{-,j}^{N_{0,j}}
\left(1-u_{+,j}^{Q_{\sigma,j}}\right)
-\Delta_{{dec},j}^{bd}
-T_{{loss},j}^{bd}.
```

This witness is admissible for the debited branch only if it is computed on
the same `P19-TOWER`, same finite Creutz-character battery, same
representation schedule, and same debit register as the Paper-16
`HK-CREUTZ-CLOSE` witness.

Define its tail capacity by

```math
c_{{15}}^{tail}
:=
\liminf_{j\to\infty}M_{{15},j}^{{bd,15}}.
```

If both the Paper-16 transported witness and the Paper-15 direct witness are
same-ledger admissible, the debited branch may use the better witness:

```math
c_{{deb,avail}}^{tail}
:=
\max\{c_{{deb}}^{tail},c_{{15}}^{tail}\}.
```

If the two witnesses are not on the same tower and debit register, they may
not be mixed; the proof must choose one witness and keep its full ledger.

### Theorem 8B.6: Direct Paper-15 Component Test

Let

```math
A_j
:=
u_{-,j}^{N_{0,j}}
\left(1-u_{+,j}^{Q_{\sigma,j}}\right),
```

and

```math
B_j
:=
\Delta_{{dec},j}^{bd}+T_{{loss},j}^{bd}.
```

Set

```math
A^-:=\liminf_j A_j,
\quad
B^+:=\limsup_j B_j,
```

and

```math
A^+:=\limsup_j A_j,
\quad
B^-:=\liminf_j B_j.
```

Then

```math
c_{{15}}^{tail}\ge A^- - B^+.
```

Thus the direct Paper-15 witness proves a positive debited reserve whenever

```math
A^- > B^+.
```

It is falsified in its absolute-tail form whenever

```math
A^+ \le B^-.
```

Proof.

This is the same liminf/limsup argument as Theorem 8B.4 applied to
`M_15,j^{bd,15}=A_j-B_j`. `square`

### Definition 8B.7: Direct Witness Signal Exponents

Assume the direct Paper-15 witness is same-ledger admissible. For each
cofinal window `j`, define the logarithmic signal exponents

```math
\theta_j^-:=-\log u_{-,j},
\qquad
\theta_j^+:=-\log u_{+,j}.
```

The witness is meaningful on a tail only when

```math
0<u_{-,j}\le u_{+,j}<1,
```

so `theta_j^+<=theta_j^-` and both exponents are nonnegative. Define

```math
\Theta_j:=N_{0,j}\theta_j^-,
\qquad
\Phi_j:=Q_{\sigma,j}\theta_j^+.
```

Then the direct signal satisfies the exact identity

```math
A_j
=
u_{-,j}^{N_{0,j}}
\left(1-u_{+,j}^{Q_{\sigma,j}}\right)
=
e^{-\Theta_j}\left(1-e^{-\Phi_j}\right).
```

The leading-sheet signal gate `P19-DW-SIG(Theta_*,Phi_*)` holds when

```math
\limsup_j\Theta_j\le\Theta_*<\infty,
\qquad
\liminf_j\Phi_j\ge\Phi_*>0.
```

Under this gate, define the certified signal floor

```math
a_*(\Theta_*,\Phi_*)
:=
e^{-\Theta_*}(1-e^{-\Phi_*})>0.
```

### Definition 8B.8: Direct Witness Loss Envelope

The direct Paper-15 loss envelope `P19-DW-LOSS(D_*,T_*)` holds when

```math
\limsup_j\Delta_{{dec},j}^{bd}\le D_*,
\qquad
\limsup_jT_{{loss},j}^{bd}\le T_*.
```

The combined loss ceiling is

```math
B_*:=D_*+T_*.
```

### Theorem 8B.9: Direct Witness Source Estimate Proves `c_{15}^{tail}>0`

Assume:

1. the direct Paper-15 witness is same-ledger admissible on `P19-TOWER`;
2. `P19-DW-SIG(Theta_*,Phi_*)` holds;
3. `P19-DW-LOSS(D_*,T_*)` holds;
4. the strict reserve inequality holds:

   ```math
   e^{-\Theta_*}(1-e^{-\Phi_*})>D_*+T_*.
   ```

Then

```math
c_{{15}}^{tail}
\ge
e^{-\Theta_*}(1-e^{-\Phi_*})-D_*-T_*
>0.
```

Consequently the debited reserve branch passes through the direct Paper-15
witness with every strict

```math
0<c_R<e^{-\Theta_*}(1-e^{-\Phi_*})-D_*-T_*.
```

Proof.

By `P19-DW-SIG`, for every sufficiently far tail and every small slack
`epsilon>0`,

```math
\Theta_j\le\Theta_*+\epsilon,
\qquad
\Phi_j\ge\Phi_*-\epsilon.
```

Since `e^{-x}` is decreasing and `1-e^{-x}` is increasing,

```math
A_j
=e^{-\Theta_j}(1-e^{-\Phi_j})
\ge
e^{-(\Theta_*+\epsilon)}
\left(1-e^{-(\Phi_*-\epsilon)}\right)
```

on that tail. Taking `epsilon` down to zero gives

```math
A^-\ge e^{-\Theta_*}(1-e^{-\Phi_*}).
```

By `P19-DW-LOSS`,

```math
B^+\le D_*+T_*.
```

Theorem 8B.6 gives

```math
c_{{15}}^{tail}
\ge
A^- - B^+
\ge
e^{-\Theta_*}(1-e^{-\Phi_*})-D_*-T_*.
```

The strict inequality makes this positive, so Lemma 8B.2 and the
same-ledger witness convention export a positive debited reserve constant.
`square`

### Theorem 8B.10: Direct Witness Falsification Bound

Assume the direct Paper-15 witness is same-ledger admissible and there are
constants `Theta_0 >= 0`, `Phi^* >= 0`, and `B_- >= 0` such that

```math
\liminf_j\Theta_j\ge\Theta_0,
\qquad
\limsup_j\Phi_j\le\Phi^*,
```

and

```math
\liminf_j
\left(\Delta_{{dec},j}^{bd}+T_{{loss},j}^{bd}\right)
\ge B_-.
```

If

```math
e^{-\Theta_0}(1-e^{-\Phi^*})\le B_-,
```

then the direct Paper-15 witness is falsified in its absolute-tail form:

```math
c_{{15}}^{tail}\le0.
```

Proof.

The exponent hypotheses imply

```math
A^+
\le
e^{-\Theta_0}(1-e^{-\Phi^*}).
```

The loss hypothesis gives `B^- >= B_-`. Hence

```math
A^+\le B^-.
```

Theorem 8B.6 then gives `c_15^{tail}<=0`. `square`

### 8B.11 Step-1a Verdict

Step 1a is now mathematically closed as a decision problem:

```text
prove c_deb^tail > 0
or prove c_deb^tail <= 0
or prove that present source estimates are too weak to decide either sign.
```

From the current source papers, the honest verdict is the third outcome.
Papers 15 and 16 give proof-quality formulas for the debited reserve
candidate, but they do not yet give sharp cofinal estimates for either the
positive lower-envelope test

```text
liminf M_SUB,j^bd,
limsup L_bat,j,
limsup L_reg,j,
limsup L_vol,j,
limsup L_shape,j,
```

or the falsifying upper-envelope test

```text
limsup M_SUB,j^bd,
liminf (L_bat,j+L_reg,j+L_vol,j+L_shape,j).
```

Through the direct Paper-15 witness, they also do not yet give sharp
cofinal estimates for either

```text
liminf u_-,j^{N_0,j}(1-u_+,j^{Q_sigma,j}),
limsup (Delta_dec,j^bd + T_loss,j^bd).
```

or

```text
limsup u_-,j^{N_0,j}(1-u_+,j^{Q_sigma,j}),
liminf (Delta_dec,j^bd + T_loss,j^bd).
```

Therefore Paper 19 does not yet prove `c_deb^{tail}>0`, and it also does not
falsify it. What it has now proved is the exact Step-1a reduction:

```text
m_SUB^- > Lambda^+       => c_deb^tail > 0,
m_SUB^+ <= Lambda^-      => c_deb^tail <= 0,
A^- > B^+                => c_15^tail > 0,
A^+ <= B^-               => c_15^tail <= 0,
P19-DW-SIG + P19-DW-LOSS
  + e^{-Theta_*}(1-e^{-Phi_*})>D_*+T_*
                         => c_15^tail > 0.
```

The next honest mathematical work is to estimate the direct-witness
quantities `Theta_j`, `Phi_j`, `Delta_dec,j^bd`, and `T_loss,j^bd` on the
actual continuum `4D SU(N)` tower. This is now a concrete source-estimate
problem: keep the leading-sheet exponent bounded, keep the first-excess
exponent bounded away from zero, and keep decoration plus transport losses
below the resulting positive signal floor.

## 8C. Step 1a-II: Bounding The Leading-Sheet Exponent `Theta_j`

The first direct-witness signal task is to decide whether

```math
\Theta_j=N_{0,j}(-\log u_{-,j})
```

stays bounded on the declared cofinal window schedule. This is the leading
minimal-sheet signal. If `Theta_j` diverges, the lower signal
`e^{-Theta_j}` vanishes and the direct Paper-15 witness cannot give an
absolute positive reserve on that schedule.

### Definition 8C.1: Leading-Sheet Exponent Gate `P19-DW-THETA(Theta_*)`

`P19-DW-THETA(Theta_*)` holds when

```math
\limsup_{j\to\infty}
N_{0,j}(-\log u_{-,j})
\le
\Theta_*<\infty.
```

Equivalently, the leading sheet has a cofinal lower signal floor

```math
\liminf_j u_{-,j}^{N_{0,j}}
\ge
e^{-\Theta_*}>0.
```

This is a scalar record statement. It is not a statement about a microscopic
surface being real; the sheet is only a certificate for the Wilson-loop
record lower bound.

### Lemma 8C.2: Exponent Gate Is Equivalent To A Leading Signal Floor

`P19-DW-THETA(Theta_*)` holds for some finite `Theta_*` if and only if there
is a number `a_0>0` such that

```math
\liminf_j u_{-,j}^{N_{0,j}}\ge a_0.
```

The constants convert as `a_0=e^{-Theta_*}` and
`Theta_*=-\log a_0`.

Proof.

For `0<u_{-,j}<1`,

```math
u_{-,j}^{N_{0,j}}
=
\exp[-N_{0,j}(-\log u_{-,j})]
=e^{-\Theta_j}.
```

The exponential is continuous and strictly decreasing. A finite limsup bound
on `Theta_j` is therefore exactly a positive liminf bound on
`e^{-Theta_j}`, and conversely. `square`

### Theorem 8C.3: Fixed-Window Sufficient Bound

Assume there are constants `N_*<infinity` and `u_*^->0` such that, on a
cofinal tail,

```math
N_{0,j}\le N_*,
\qquad
u_{-,j}\ge u_*^-.
```

Then `P19-DW-THETA(Theta_*)` holds with

```math
\Theta_*:=N_*(-\log u_*^-).
```

Proof.

Since `-log x` is decreasing on `(0,infinity)`,

```math
-\log u_{-,j}\le-\log u_*^-.
```

Multiplying by `N_{0,j}<=N_*` gives the displayed bound. `square`

### Theorem 8C.4: Heat-Kernel Neighborhood Sufficient Bound

Assume the Paper-14 heat-kernel coefficient window is used on the same
tower, so that

```math
u_{-,j}
\ge
e^{-a_j}(1-\eta_j),
\qquad
a_j:=t_jC_2(\rho_j)/2,
\qquad
0\le\eta_j<1.
```

Assume further that

```math
\limsup_j N_{0,j}a_j\le A_*<\infty,
```

and

```math
\limsup_j N_{0,j}[-\log(1-\eta_j)]\le E_*<\infty.
```

Then `P19-DW-THETA(Theta_*)` holds with

```math
\Theta_*:=A_*+E_*.
```

Proof.

The coefficient lower bound gives

```math
-\log u_{-,j}
\le
a_j-\log(1-\eta_j).
```

Multiplying by `N_{0,j}` and taking limsup gives

```math
\limsup_j\Theta_j
\le
\limsup_j N_{0,j}a_j
+
\limsup_j N_{0,j}[-\log(1-\eta_j)]
\le A_*+E_*.
```

This is `P19-DW-THETA(A_*+E_*)`. `square`

### Corollary 8C.5: Fixed Representation And Fixed Physical Window

If the representation `rho`, heat-kernel neighborhood time `t`, coefficient
error ratio `eta`, and Creutz window are all eventually fixed, with

```math
N_{0,j}=N_0,
\qquad
t_j=t,
\qquad
C_2(\rho_j)=C_2(\rho),
\qquad
\eta_j\le\eta<1,
```

then `P19-DW-THETA(Theta_*)` holds with

```math
\Theta_*
=
N_0
\left(
{tC_2(\rho)\over2}
-\log(1-\eta)
\right).
```

This is the clean finite-window route. It does not prove a growing-window
area law by itself; it proves that the direct witness retains a nonzero
leading signal on the fixed finite Creutz battery.

### Theorem 8C.6: Growing-Window Obstruction

Assume that, on a cofinal tail,

```math
N_{0,j}\to\infty
```

and there is a fixed `u^+<1` such that

```math
u_{-,j}\le u^+.
```

Then

```math
\Theta_j\to\infty,
```

so no finite `Theta_*` can satisfy `P19-DW-THETA(Theta_*)`.

Proof.

Since `u_{-,j}<=u^+<1`,

```math
-\log u_{-,j}\ge-\log u^+>0.
```

Therefore

```math
\Theta_j
=N_{0,j}(-\log u_{-,j})
\ge
N_{0,j}(-\log u^+)
\to\infty.
```

`square`

### Theorem 8C.7: Necessary Scaling For Growing Windows

If `N_{0,j}\to\infty` and `P19-DW-THETA(Theta_*)` holds, then necessarily

```math
-\log u_{-,j}
=
O(N_{0,j}^{-1})
```

on the cofinal tail. Equivalently,

```math
u_{-,j}
\ge
\exp[-(\Theta_*+\epsilon)/N_{0,j}]
```

eventually for every `epsilon>0`.

Proof.

`P19-DW-THETA(Theta_*)` says that for every `epsilon>0`, eventually

```math
N_{0,j}(-\log u_{-,j})\le\Theta_*+\epsilon.
```

Divide by `N_{0,j}` and exponentiate. `square`

### 8C.8 Current Verdict For `Theta_j`

Paper 19 can now bound `Theta_j` in two honest ways:

```text
fixed-window route:
  N_0,j <= N_* and u_-,j >= u_*^- > 0;

heat-kernel scaling route:
  limsup N_0,j t_j C_2(rho_j)/2 < infinity
  and limsup N_0,j[-log(1-eta_j)] < infinity.
```

It can also falsify the direct witness on a declared growing-window schedule:

```text
N_0,j -> infinity and u_-,j <= u^+ < 1
=> Theta_j -> infinity.
```

The current source papers give the formulas and the finite-window route, but
they do not yet prove the heat-kernel scaling route on an actual growing
`4D SU(N)` confinement schedule. Thus the leading-sheet exponent is bounded
for fixed finite Creutz batteries, while a cofinal growing-window area-law
route requires the stronger scaling

```math
-\log u_{-,j}=O(1/N_{0,j}).
```

## 8D. Step 1a-III: Lower-Bounding The First-Excess Exponent `Phi_j`

The second direct-witness signal task is to decide whether

```math
\Phi_j=Q_{\sigma,j}(-\log u_{+,j})
```

stays bounded away from zero. This is the first-excess separation in the
Creutz contrast. If `Phi_j` tends to zero, then
`1-e^{-Phi_j}` tends to zero and the direct Paper-15 witness loses the
Creutz difference even if the leading sheet itself remains visible.

### Definition 8D.1: First-Excess Gate `P19-DW-PHI(Phi_*)`

`P19-DW-PHI(Phi_*)` holds when

```math
\liminf_{j\to\infty}
Q_{\sigma,j}(-\log u_{+,j})
\ge
\Phi_*
>
0.
```

Equivalently, the first-excess suppression has a cofinal positive contrast:

```math
\liminf_j(1-u_{+,j}^{Q_{\sigma,j}})
\ge
1-e^{-\Phi_*}
>
0.
```

### Lemma 8D.2: First-Excess Gate Is Equivalent To A Creutz Contrast Floor

`P19-DW-PHI(Phi_*)` holds for some `Phi_*>0` if and only if there is a
number `b_0>0` such that

```math
\liminf_j(1-u_{+,j}^{Q_{\sigma,j}})\ge b_0.
```

The constants convert as `b_0=1-e^{-Phi_*}` and
`Phi_*=-\log(1-b_0)`.

Proof.

For `0<u_{+,j}<1`,

```math
u_{+,j}^{Q_{\sigma,j}}
=
\exp[-Q_{\sigma,j}(-\log u_{+,j})]
=e^{-\Phi_j}.
```

The function `x -> 1-e^{-x}` is continuous and strictly increasing on
`[0,infinity)`. A positive liminf bound on `Phi_j` is therefore exactly a
positive liminf bound on `1-e^{-Phi_j}`. `square`

### Theorem 8D.3: Fixed-Window Sufficient Bound

Assume there are constants `Q_*>0` and `u^+<1` such that, on a cofinal tail,

```math
Q_{\sigma,j}\ge Q_*,
\qquad
u_{+,j}\le u^+.
```

Then `P19-DW-PHI(Phi_*)` holds with

```math
\Phi_*:=Q_*(-\log u^+)>0.
```

Proof.

Since `-log x` is decreasing and `u_{+,j}<=u^+<1`,

```math
-\log u_{+,j}\ge-\log u^+>0.
```

Multiplying by `Q_{\sigma,j}>=Q_*` gives the bound. `square`

### Theorem 8D.4: Heat-Kernel Neighborhood Sufficient Bound

Assume the Paper-14 heat-kernel coefficient window is used on the same
tower, so that

```math
u_{+,j}
\le
e^{-a_j}(1+\zeta_j),
\qquad
a_j:=t_jC_2(\rho_j)/2,
\qquad
0\le\zeta_j<e^{a_j}-1.
```

Equivalently define the upper-window exponent

```math
b_j:=-\log u_{+,j}.
```

If

```math
\liminf_j Q_{\sigma,j} b_j\ge\Phi_*>0,
```

then `P19-DW-PHI(Phi_*)` holds.

A sufficient explicit condition is:

```math
\liminf_j Q_{\sigma,j}
\left[
a_j-\log(1+\zeta_j)
\right]
\ge\Phi_*>0.
```

Proof.

The definition `b_j=-log u_{+,j}` gives `Phi_j=Q_sigma,j b_j`. The explicit
upper-window bound gives

```math
b_j
\ge
a_j-\log(1+\zeta_j).
```

Multiplying by `Q_sigma,j` and taking liminf proves the claim. `square`

### Theorem 8D.5: Theta/Phi Compatibility Bound

Assume the coefficient window has controlled relative width:

```math
0<u_{-,j}\le u_{+,j}<1,
\qquad
{ -\log u_{+,j}\over -\log u_{-,j}}\ge r_*>0
```

on a cofinal tail. If `P19-DW-THETA(Theta_*)` holds and

```math
\liminf_j {Q_{\sigma,j}\over N_{0,j}}\ge q_*>0,
```

then `P19-DW-PHI(Phi_*)` holds with

```math
\Phi_*:=r_*q_*\Theta_{low},
```

provided the leading exponent also has a positive lower bound

```math
\liminf_j\Theta_j\ge\Theta_{low}>0.
```

Proof.

Write `a_j=-log u_{-,j}` and `b_j=-log u_{+,j}`. The relative-width
hypothesis gives `b_j>=r_*a_j`. Therefore

```math
\Phi_j
=Q_{\sigma,j}b_j
\ge
r_*{Q_{\sigma,j}\over N_{0,j}}N_{0,j}a_j
=
r_*{Q_{\sigma,j}\over N_{0,j}}\Theta_j.
```

Taking liminf gives `Phi_j>=r_*q_*Theta_low` cofinally. `square`

### Theorem 8D.6: Compatibility Obstruction Under Bounded `Theta`

Assume:

1. `P19-DW-THETA(Theta_*)` holds;
2. the upper and lower coefficient exponents are comparable from above:

   ```math
   { -\log u_{+,j}\over -\log u_{-,j}}\le R_*<\infty;
   ```

3. the relative area gap collapses:

   ```math
   {Q_{\sigma,j}\over N_{0,j}}\to0.
   ```

Then

```math
\Phi_j\to0.
```

Thus no positive `P19-DW-PHI(Phi_*)` can hold on that declared schedule.

Proof.

Let `a_j=-log u_{-,j}` and `b_j=-log u_{+,j}`. By the upper comparability
assumption, `b_j<=R_*a_j`. Since `P19-DW-THETA(Theta_*)` gives
`N_{0,j}a_j<=Theta_*+o(1)`,

```math
\Phi_j
=Q_{\sigma,j}b_j
\le
R_*{Q_{\sigma,j}\over N_{0,j}}(N_{0,j}a_j)
\le
R_*{Q_{\sigma,j}\over N_{0,j}}(\Theta_*+o(1)).
```

The right-hand side tends to zero. `square`

### 8D.7 Current Verdict For `Phi_j`

Paper 19 can now lower-bound `Phi_j` in two honest ways:

```text
fixed-window route:
  Q_sigma,j >= Q_* > 0 and u_+,j <= u^+ < 1;

heat-kernel route:
  liminf Q_sigma,j[-log u_+,j] >= Phi_* > 0.
```

The compatibility result says that a growing-window direct witness is not
just a coefficient problem. If `Theta_j` is bounded by tuning `u_-` close to
one, then `Phi_j` remains positive only if the first-excess area gap
`Q_sigma,j` is large enough relative to the minimal-sheet scale `N_0,j`, or
if the coefficient window keeps `u_+` from sitting substantially closer to
one than `u_-`. In exponent language, this means
`(-log u_+)/(-log u_-)` must not collapse to zero.

In the standard comparable-window case, the direct witness needs:

```math
\liminf_j {Q_{\sigma,j}\over N_{0,j}}>0.
```

If instead

```math
Q_{\sigma,j}/N_{0,j}\to0
```

while `Theta_j` is bounded and the upper/lower coefficient exponents are
comparable, then `Phi_j->0` and the direct Paper-15 witness fails on that
growing-window schedule.

## 8E. Step 1a-IV: Direct Witness Loss Estimate

The direct witness now has a scalar signal floor

```math
a_*(\Theta_*,\Phi_*)
=
e^{-\Theta_*}(1-e^{-\Phi_*}).
```

The remaining task is to keep the Paper-15 loss ceiling

```math
\Delta_{{dec},j}^{bd}+T_{{loss},j}^{bd}
```

strictly below this signal floor on the same tower and debit register.

### Definition 8E.1: Decoration Loss Gate `P19-DW-DEC(eta_*,c_\Delta^*)`

Let

```math
\eta_{{dec},j}^{bd}
=
\eta_{{res},j}^{bd}+\eta_{{ch},j}^{bd},
\qquad
\eta_{{ch},j}^{bd}=C_{{ch},j}Tail_{{CE},j},
```

and let `c_{\Delta,j}^*` be the Paper-15 finite-battery constant
`c_xi,j^*+c_xip,j^*`. The decoration gate
`P19-DW-DEC(eta_*,c_\Delta^*)` holds when

```math
\limsup_j\eta_{{dec},j}^{bd}\le\eta_*<1,
\qquad
\limsup_jc_{\Delta,j}^*\le c_\Delta^*<\infty.
```

Define the resulting decoration-loss ceiling

```math
D_{dec}^*(\eta_*,c_\Delta^*)
:=
\exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1.
```

### Theorem 8E.2: Decoration Gate Bounds `Delta_dec^{bd}`

If `P19-DW-DEC(eta_*,c_\Delta^*)` holds, then

```math
\limsup_j\Delta_{{dec},j}^{bd}
\le
D_{dec}^*(\eta_*,c_\Delta^*).
```

Proof.

Paper 15 gives

```math
\Delta_{{dec},j}^{bd}
=
\exp\left(
{c_{\Delta,j}^*\eta_{{dec},j}^{bd}\over1-\eta_{{dec},j}^{bd}}
\right)-1.
```

The functions `x -> x/(1-x)` on `[0,1)` and `y -> exp(y)-1` are increasing.
Taking the limsup bounds in the definition of `P19-DW-DEC` gives the stated
ceiling. `square`

### Definition 8E.3: Component Decoration Gate

The component decoration gate
`P19-DW-DEC-COMP(eta_res^*,eta_ch^*,c_\Delta^*)` holds when

```math
\limsup_j\eta_{{res},j}^{bd}\le\eta_{res}^*,
\qquad
\limsup_j C_{{ch},j}Tail_{{CE},j}\le\eta_{ch}^*,
```

```math
\eta_{res}^*+\eta_{ch}^*<1,
\qquad
\limsup_jc_{\Delta,j}^*\le c_\Delta^*<\infty.
```

Then it implies `P19-DW-DEC(eta_*,c_\Delta^*)` with

```math
\eta_*:=\eta_{res}^*+\eta_{ch}^*.
```

This is the loss-side version of the Paper-15 decoration ledger:
residual-polymer KP plus non-leading character tail must fit inside the
same finite-battery decoration margin.

### Definition 8E.4: Transport Loss Gate `P19-DW-TLOSS(T_*)`

Paper 15 decomposes the finite transport loss as

```math
T_{{loss},j}^{bd}
=
T_{11,j}+T_{12,j}+T_{13,j}+T_{14,j}.
```

The transport loss gate `P19-DW-TLOSS(T_*)` holds when

```math
\limsup_jT_{{loss},j}^{bd}\le T_*<\infty.
```

The component transport gate
`P19-DW-TLOSS-COMP(T_{11}^*,T_{12}^*,T_{13}^*,T_{14}^*)` holds when

```math
\limsup_jT_{k,j}\le T_k^*
\quad
\text{for }k=11,12,13,14.
```

It implies `P19-DW-TLOSS(T_*)` with

```math
T_*:=T_{11}^*+T_{12}^*+T_{13}^*+T_{14}^*.
```

The four terms have the Paper-15 meanings: local-RG/RP/covariance/gauge
reconstruction loss, perimeter-cusp and smearing/loop-approximation loss,
surface-polymer and exact-entry transport loss, and Paper-14 whole-process
finite-block projection loss.

### Theorem 8E.5: Decoration Plus Transport Proves `P19-DW-LOSS`

Assume `P19-DW-DEC(eta_*,c_\Delta^*)` and `P19-DW-TLOSS(T_*)`. Let

```math
D_*:=D_{dec}^*(\eta_*,c_\Delta^*)
=
\exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1.
```

Then `P19-DW-LOSS(D_*,T_*)` holds.

Proof.

Theorem 8E.2 gives `limsup Delta_dec,j^bd<=D_*`. The transport gate gives
`limsup T_loss,j^bd<=T_*`. These are exactly the two clauses of
`P19-DW-LOSS(D_*,T_*)`. `square`

### Theorem 8E.6: Full Direct-Witness Pass Test

Assume on `P19-TOWER`:

1. the direct Paper-15 witness is same-ledger admissible;
2. `P19-DW-THETA(Theta_*)`;
3. `P19-DW-PHI(Phi_*)`;
4. `P19-DW-DEC(eta_*,c_\Delta^*)`;
5. `P19-DW-TLOSS(T_*)`;
6. the strict signal-minus-loss inequality

   ```math
   e^{-\Theta_*}(1-e^{-\Phi_*})
   >
   \exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1
   +T_*.
   ```

Then

```math
c_{{15}}^{tail}>0.
```

Consequently the debited direct-witness branch proves
`AYM-CONF-ACT-CRES-P16(c_R)` for every strict

```math
0<c_R<
e^{-\Theta_*}(1-e^{-\Phi_*})
-
\left[
\exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1
\right]
-T_*.
```

Proof.

The `Theta` and `Phi` gates imply `P19-DW-SIG(Theta_*,Phi_*)`. Theorem 8E.5
implies `P19-DW-LOSS(D_*,T_*)` with the displayed value of `D_*`. The strict
inequality is exactly the hypothesis of Theorem 8B.9, so
`c_15^{tail}>0` and the positive reserve export follows. `square`

### Theorem 8E.7: Loss-Side Falsification Against A Signal Ceiling

Assume the direct Paper-15 witness is same-ledger admissible and there are
signal ceiling constants `Theta_0>=0`, `Phi^*>=0` such that

```math
A^+
\le
e^{-\Theta_0}(1-e^{-\Phi^*}).
```

Assume also a lower loss floor

```math
\liminf_j
\left(\Delta_{{dec},j}^{bd}+T_{{loss},j}^{bd}\right)
\ge B_-.
```

If

```math
e^{-\Theta_0}(1-e^{-\Phi^*})\le B_-,
```

then `c_15^{tail}<=0`; the direct Paper-15 witness is falsified in its
absolute-tail form.

Proof.

The hypotheses give `A^+<=B^-`. Theorem 8B.6 gives `c_15^{tail}<=0`.
`square`

### 8E.8 Current Verdict For The Loss Side

Paper 19 now reduces the loss side to two concrete estimates:

```text
decoration:
  limsup eta_dec,j^bd <= eta_* < 1,
  limsup c_Delta,j^* <= c_Delta^* < infinity;

transport:
  limsup (T_11,j+T_12,j+T_13,j+T_14,j) <= T_* < infinity.
```

The direct witness passes only if the final scalar inequality is strict:

```math
e^{-\Theta_*}(1-e^{-\Phi_*})
>
\exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1
+T_*.
```

The current source papers give the definitions of these quantities and the
finite-battery formulas, but they do not yet prove the cofinal loss ceilings
small enough for the actual `4D SU(N)` tower. After `P19-AN-IMPORT(m)`,
the residual contribution is `eta_19^res`; the next non-algebraic work is
therefore to estimate `Tail_CE`, `c_Delta^*`, and the four transport terms
on the same tower used for `Theta_j` and `Phi_j`.

## 8F. Step 1a-V: Creutz Window Geometry For `Q_sigma/N_0`

Section 8D shows that a growing-window direct witness needs geometric
support:

```math
\liminf_j {Q_{\sigma,j}\over N_{0,j}}>0
```

unless some coefficient exponent is doing extra work. This section computes
that ratio for the standard rectangular Creutz battery. The result is a
hard schedule constraint, not a matter of notation.

### Definition 8F.1: Rectangular Block Window

Fix block-side lengths `R,T` and a Creutz decrement `sigma` with

```math
0<\sigma<\min\{R,T\}.
```

Use the planar block-area model

```math
N_{a,b}=ab
```

for the four Paper-13 Creutz slots:

```math
(R,T),\quad (R-\sigma,T-\sigma),
\quad (R-\sigma,T),\quad (R,T-\sigma).
```

The Paper-13 quantities are

```math
Q_\sigma
=
N_{R,T}+N_{R-\sigma,T-\sigma}
-N_{R-\sigma,T}-N_{R,T-\sigma},
```

and

```math
N_0=N_{R-\sigma,T}+N_{R,T-\sigma}.
```

### Lemma 8F.2: Exact Rectangular Formula

For the rectangular block window of Definition 8F.1,

```math
Q_\sigma=\sigma^2,
```

```math
N_0=2RT-\sigma(R+T),
```

and therefore

```math
{Q_\sigma\over N_0}
=
{\sigma^2\over 2RT-\sigma(R+T)}
=
{(\sigma/R)(\sigma/T)\over 2-\sigma/R-\sigma/T}.
```

Proof.

Expanding the four block areas gives

```math
Q_\sigma
=
RT+(R-\sigma)(T-\sigma)
-(R-\sigma)T-R(T-\sigma)
=
\sigma^2.
```

Similarly,

```math
N_0=(R-\sigma)T+R(T-\sigma)=2RT-\sigma(R+T).
```

Dividing gives the displayed ratio. `square`

### Theorem 8F.3: Thin-Increment Collapse

Let `(R_j,T_j,\sigma_j)` be a cofinal rectangular window schedule with
`0<sigma_j<min{R_j,T_j}`. Suppose

```math
{\sigma_j^2\over R_jT_j}\to0
```

and there is a constant `d_0>0` such that eventually

```math
2-{\sigma_j\over R_j}-{\sigma_j\over T_j}\ge d_0.
```

Then

```math
{Q_{\sigma,j}\over N_{0,j}}\to0.
```

In particular, if `sigma_j` is fixed, or more generally
`sigma_j=o(\sqrt{R_jT_j})`, and the rectangles do not degenerate, then the
relative Creutz area gap collapses.

Proof.

By Lemma 8F.2,

```math
{Q_{\sigma,j}\over N_{0,j}}
=
{(\sigma_j^2/R_jT_j)
\over
2-\sigma_j/R_j-\sigma_j/T_j}
\le
{1\over d_0}{\sigma_j^2\over R_jT_j}.
```

The right-hand side tends to zero. `square`

### Theorem 8F.4: Thick-Increment Geometry Pass

Let `(R_j,T_j,\sigma_j)` be a cofinal rectangular window schedule. Suppose
there are constants `q_0>0` and `d_0>0` such that eventually

```math
{\sigma_j^2\over R_jT_j}\ge q_0,
```

and

```math
2-{\sigma_j\over R_j}-{\sigma_j\over T_j}\ge d_0.
```

Then

```math
\liminf_j {Q_{\sigma,j}\over N_{0,j}}
\ge
{q_0\over 2}.
```

If in addition one has a sharper upper denominator bound `D_0<2`:

```math
2-{\sigma_j\over R_j}-{\sigma_j\over T_j}\le D_0,
```

then

```math
\liminf_j {Q_{\sigma,j}\over N_{0,j}}
\ge
{q_0\over D_0}.
```

Equivalently, the geometry gate passes whenever the decrement is a
macroscopic fraction of both side lengths, while the smaller Creutz slots
remain nondegenerate.

Proof.

Lemma 8F.2 gives

```math
{Q_{\sigma,j}\over N_{0,j}}
=
{(\sigma_j^2/R_jT_j)
\over
2-\sigma_j/R_j-\sigma_j/T_j}.
```

Since `0<sigma_j/R_j<1` and `0<sigma_j/T_j<1`, the denominator is strictly
less than `2`; hence the ratio is at least `q_0/2`. The lower nondegeneracy
bound `d_0` keeps `N_{0,j}/(R_jT_j)` bounded away from zero and rules out a
collapsing smaller slot. If the sharper upper bound `D_0` is available, the
same formula gives the sharper lower bound `q_0/D_0`. `square`

### Corollary 8F.5: Square Thick Windows

If

```math
R_j=T_j=L_j,
\qquad
\sigma_j=\alpha L_j,
\qquad
0<\alpha<1,
```

then

```math
{Q_{\sigma,j}\over N_{0,j}}
=
{\alpha^2\over 2(1-\alpha)}.
```

Thus a square cofinal schedule with a fixed fractional decrement has a
strictly positive `Q_sigma/N_0` geometry constant. A square schedule with
fixed `sigma` has

```math
{Q_{\sigma,j}\over N_{0,j}}
=
{\sigma^2\over 2L_j^2-2\sigma L_j}
\to0.
```

### Corollary 8F.6: Compatibility With The `Theta/Phi` Gate

Assume the coefficient exponents are comparable as in Theorem 8D.6 and
`P19-DW-THETA(Theta_*)` holds.

If the window schedule is thin in the sense of Theorem 8F.3, then

```math
\Phi_j\to0,
```

so the direct Paper-15 witness cannot prove a growing-window reserve on that
schedule.

If the window schedule is thick in the sense of Theorem 8F.4, the geometry
obstruction is removed:

```math
\liminf_j {Q_{\sigma,j}\over N_{0,j}}>0.
```

This does not by itself prove confinement. It only supplies the missing
geometric input needed by Theorem 8D.5. The same schedule must still satisfy
the coefficient lower bound, decoration-loss bound, transport-loss bound, and
same-ledger debit audit from Sections 8C--8E.

### 8F.7 Current Verdict For Window Geometry

For the standard rectangular Creutz battery,

```math
{Q_\sigma\over N_0}
=
{\sigma^2\over 2RT-\sigma(R+T)}.
```

Therefore:

```text
fixed or sub-macroscopic sigma on growing R,T:
  Q_sigma/N_0 -> 0;

fractional sigma, e.g. R=T=L and sigma=alpha L:
  Q_sigma/N_0 = alpha^2/[2(1-alpha)] > 0.
```

The honest conclusion is that the usual adjacent-loop Creutz decrement with
fixed `sigma` is not enough for the growing-window direct-witness route. For
cofinal area-law work, Paper 19 must use one of three routes:

1. stay with fixed finite Creutz batteries and avoid claiming growing-window
   confinement from the direct witness alone;
2. use thick/co-scaling Creutz windows with `Q_sigma/N_0` bounded away from
   zero;
3. abandon the absolute direct-witness branch and prove the reserve through a
   normalized or renormalized source route.

This is Barandes-aligned in the same sense as the rest of Paper 19: the
window schedule is a declared record schedule in the whole-process ledger,
not a hidden field-theoretic object inserted after the fact.

## 8G. Step 1a-VI: Thick-Window Coefficient Scaling

Section 8F makes the growing-window choice unavoidable. If Paper 19 wants a
direct Paper-15 witness on cofinal windows, the main growing-window branch is
now:

```text
use thick/co-scaling Creutz windows,
then prove coefficient exponents at the reciprocal window-area scale.
```

This section states that branch as an explicit gate. It does not assume a
field ontology behind the Wilson-loop records; it only constrains the
declared same-ledger Creutz record schedule and the scalar coefficient
envelope already used in Papers 13--15.

### Definition 8G.1: Thick Direct-Witness Window Branch

A cofinal rectangular Creutz schedule is a thick direct-witness branch when
there is an area scale

```math
S_j:=R_jT_j\to\infty
```

and constants

```math
0<q_- \le q_+<\infty,
\qquad
0<n_- \le n_+<\infty
```

such that, on a cofinal tail,

```math
q_-
\le
{Q_{\sigma,j}\over S_j}
\le q_+,
```

and

```math
n_-
\le
{N_{0,j}\over S_j}
\le n_+.
```

For the square fractional branch

```math
R_j=T_j=L_j,
\qquad
\sigma_j=\alpha L_j,
\qquad
0<\alpha<1,
```

one may take

```math
S_j=L_j^2,
\qquad
q_-=q_+=\alpha^2,
\qquad
n_-=n_+=2(1-\alpha).
```

The ratio required by Section 8D is then

```math
{Q_{\sigma,j}\over N_{0,j}}
=
{q_-\over n_+}
```

in the constant square case, and at least `q_-/n_+` in the general thick
branch.

### Definition 8G.2: Reciprocal-Area Coefficient Gate

Let the same heat-kernel coefficient window as Section 8C and Section 8D be
used:

```math
u_{-,j}
\ge
e^{-a_j}(1-\eta_j),
\qquad
a_j:=t_jC_2(\rho_j)/2,
\qquad
0\le\eta_j<1,
```

and

```math
u_{+,j}
\le
e^{-a_j}(1+\zeta_j),
\qquad
0\le\zeta_j<e^{a_j}-1.
```

Define the lower and upper exponent envelopes

```math
A_j^-:=a_j-\log(1-\eta_j),
```

and

```math
B_j^+:=a_j-\log(1+\zeta_j).
```

The reciprocal-area coefficient gate
`P19-THICK-COEFF(A_*,B_*)` holds on the thick branch when

```math
\limsup_j S_jA_j^-\le A_*<\infty,
```

and

```math
\liminf_j S_jB_j^+\ge B_*>0.
```

The first inequality says the lower coefficient does not kill the leading
sheet faster than reciprocal area. The second says the upper coefficient
still separates the first-excess sheet by a positive reciprocal-area amount.

### Theorem 8G.3: Thick-Window `Theta/Phi` Coefficient Pass

Assume the thick direct-witness branch of Definition 8G.1 and
`P19-THICK-COEFF(A_*,B_*)`. Then

```text
P19-DW-THETA(Theta_*)
```

holds with

```math
\Theta_*:=n_+A_*,
```

and

```text
P19-DW-PHI(Phi_*)
```

holds with

```math
\Phi_*:=q_-B_*.
```

In the square fractional branch these become

```math
\Theta_*=2(1-\alpha)A_*,
\qquad
\Phi_*=\alpha^2B_*.
```

Proof.

The lower coefficient bound gives

```math
-\log u_{-,j}\le A_j^-.
```

Therefore

```math
\Theta_j
=
N_{0,j}(-\log u_{-,j})
\le
{N_{0,j}\over S_j}S_jA_j^-.
```

Taking limsup and using `N_0,j/S_j<=n_+` gives
`limsup Theta_j<=n_+A_*`.

For the first-excess exponent, the upper coefficient bound gives

```math
-\log u_{+,j}\ge B_j^+.
```

Thus

```math
\Phi_j
=
Q_{\sigma,j}(-\log u_{+,j})
\ge
{Q_{\sigma,j}\over S_j}S_jB_j^+.
```

Taking liminf and using `Q_sigma,j/S_j>=q_-` gives
`liminf Phi_j>=q_-B_*>0`. `square`

### Corollary 8G.4: Thick-Window Direct-Witness Reserve Test

Assume:

1. the direct Paper-15 witness is same-ledger admissible;
2. the thick direct-witness branch holds with constants `q_-,n_+`;
3. `P19-THICK-COEFF(A_*,B_*)`;
4. `P19-DW-DEC(eta_*,c_\Delta^*)`;
5. `P19-DW-TLOSS(T_*)`;
6. the strict thick-window signal inequality

   ```math
   \exp(-n_+A_*)\left(1-\exp(-q_-B_*)\right)
   >
   \exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1
   +T_*.
   ```

Then

```math
c_{15}^{tail}>0.
```

Consequently the debited direct-witness branch exports a positive reserve
constant

```math
c_R
<
\exp(-n_+A_*)\left(1-\exp(-q_-B_*)\right)
-
\left[
\exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1
\right]
-T_*.
```

Proof.

Theorem 8G.3 supplies `P19-DW-THETA(n_+A_*)` and
`P19-DW-PHI(q_-B_*)`. The loss hypotheses supply the two loss gates of
Theorem 8E.6. The displayed strict inequality is exactly Theorem 8E.6 with
`Theta_*=n_+A_*` and `Phi_*=q_-B_*`. `square`

### Theorem 8G.5: Thick Branch Still Fails Without Reciprocal-Area Scaling

Assume the thick direct-witness branch and suppose there is a constant
`b^+<\infty` such that

```math
-\log u_{+,j}\le b^+(-\log u_{-,j})
```

on a cofinal tail. If

```math
S_j(-\log u_{-,j})\to0,
```

then

```math
\Phi_j\to0.
```

If instead

```math
S_j(-\log u_{-,j})\to\infty,
```

and `N_{0,j}/S_j>=n_->0`, then

```math
\Theta_j\to\infty.
```

Thus the thick branch does not remove the coefficient bottleneck. It narrows
the only viable growing-window direct-witness scaling to the reciprocal-area
regime:

```math
-\log u_{\pm,j}\asymp {1\over S_j}.
```

Proof.

If `S_j(-log u_-,j)->0`, then by exponent comparability,

```math
\Phi_j
=
Q_{\sigma,j}(-\log u_{+,j})
\le
q_+S_j b^+(-\log u_{-,j})
\to0.
```

If `S_j(-log u_-,j)->infinity`, then

```math
\Theta_j
=
N_{0,j}(-\log u_{-,j})
\ge
n_-S_j(-\log u_{-,j})
\to\infty.
```

The two alternatives show that, under comparable exponents, the only
nontrivial direct-witness window is the reciprocal-area scaling window.
`square`

### 8G.6 Current Verdict For The Thick Branch

Paper 19 now has a declared growing-window direct-witness route:

```text
thick/co-scaling Creutz windows
+ reciprocal-area coefficient scaling
+ decoration and transport losses below the thick signal floor.
```

For square fractional windows this is:

```math
R_j=T_j=L_j,\qquad \sigma_j=\alpha L_j,
```

with coefficient requirements

```math
\limsup_j L_j^2
\left[
{t_jC_2(\rho_j)\over2}
-\log(1-\eta_j)
\right]
\le A_*<\infty,
```

and

```math
\liminf_j L_j^2
\left[
{t_jC_2(\rho_j)\over2}
-\log(1+\zeta_j)
\right]
\ge B_*>0.
```

The resulting signal floor is

```math
\exp[-2(1-\alpha)A_*]
\left(1-\exp[-\alpha^2B_*]\right).
```

This is the strongest direct-witness branch currently available in Paper 19.
It still does not prove actual `4D SU(N)` confinement, because the present
source ledgers have not yet proved the reciprocal-area coefficient scaling
or the loss inequality on the same whole-process tower. But it has eliminated
the fixed-`sigma` growing-window route and replaced it with a precise
cofinal test.

## 8H. Step 1a-VII: Reciprocal-Area Coefficient Source

Step 1 is now focused on one scalar source question:

```text
Can the actual heat-kernel/character coefficient ledger supply
P19-THICK-COEFF(A_*,B_*)?
```

This section separates that question into a clean heat-kernel time schedule
and two coefficient-window error budgets. It proves the exact pass/fail
criteria available from the Paper-14 coefficient window and the Paper-16
heat-kernel source tower.

### Definition 8H.1: Clean Coefficient Scale And Error Widths

On the thick branch let

```math
S_j:=R_jT_j.
```

Recall

```math
a_j={t_jC_2(\rho_j)\over2},
```

and define the clean reciprocal-area coefficient scale

```math
\mathcal A_j:=S_j a_j
=
S_j{t_jC_2(\rho_j)\over2}.
```

Define the lower-window and upper-window error widths

```math
\mathcal E_j^-:=S_j[-\log(1-\eta_j)],
```

and

```math
\mathcal E_j^+:=S_j\log(1+\zeta_j).
```

Then the two thick coefficient quantities of Definition 8G.2 are exactly

```math
S_jA_j^-=\mathcal A_j+\mathcal E_j^-,
```

and

```math
S_jB_j^+=\mathcal A_j-\mathcal E_j^+.
```

Proof.

This is just substitution into

```math
A_j^-:=a_j-\log(1-\eta_j),
\qquad
B_j^+:=a_j-\log(1+\zeta_j).
```

Multiplying by `S_j` gives the two displayed identities. `square`

### Definition 8H.2: Reciprocal-Area Source Envelope `P19-RAC-SRC`

`P19-RAC-SRC(A^-,A^+,E^-,E^+)` holds on the same thick branch and tower when

```math
0<A^-\le A^+<\infty,
```

```math
\liminf_j\mathcal A_j\ge A^-,
\qquad
\limsup_j\mathcal A_j\le A^+,
```

and

```math
\limsup_j\mathcal E_j^-\le E^-<\infty,
\qquad
\limsup_j\mathcal E_j^+\le E^+<\infty.
```

The source envelope is nondegenerate when

```math
A^->E^+.
```

The clean scale `A^-,A^+` is the declared heat-kernel time schedule. The
error widths `E^-,E^+` measure how tightly the actual block coefficient is
kept around the heat-kernel reference inside the same finite character
battery.

### Theorem 8H.3: Source Envelope Proves The Thick Coefficient Gate

Assume `P19-RAC-SRC(A^-,A^+,E^-,E^+)` and

```math
A^->E^+.
```

Then `P19-THICK-COEFF(A_*,B_*)` holds with

```math
A_*:=A^++E^-,
```

and

```math
B_*:=A^--E^+>0.
```

Proof.

By Definition 8H.1,

```math
S_jA_j^-=\mathcal A_j+\mathcal E_j^-.
```

Taking the limsup and using the source-envelope bounds gives

```math
\limsup_j S_jA_j^-
\le
A^++E^-.
```

Similarly,

```math
S_jB_j^+=\mathcal A_j-\mathcal E_j^+,
```

so

```math
\liminf_j S_jB_j^+
\ge
A^--E^+.
```

The strict inequality `A^->E^+` makes `B_*` positive. These are exactly the
two clauses of `P19-THICK-COEFF(A_*,B_*)`. `square`

### Corollary 8H.4: The `t_j=beta_j/S_j` Route

Assume the representation channel is fixed, `rho_j=rho`, with
`C_2(rho)>0`. Suppose the heat-kernel time is scheduled as

```math
t_j={\beta_j\over S_j},
```

with

```math
0<\beta_-\le\liminf_j\beta_j
\le
\limsup_j\beta_j\le\beta_+<\infty.
```

Then

```math
A^-={\beta_-C_2(\rho)\over2},
\qquad
A^+={\beta_+C_2(\rho)\over2}
```

are valid clean-scale bounds. If additionally

```math
\limsup_j S_j[-\log(1-\eta_j)]\le E^-,
```

and

```math
\limsup_j S_j\log(1+\zeta_j)\le E^+,
```

with

```math
{\beta_-C_2(\rho)\over2}>E^+,
```

then `P19-THICK-COEFF(A_*,B_*)` holds with

```math
A_*={\beta_+C_2(\rho)\over2}+E^-,
```

and

```math
B_*={\beta_-C_2(\rho)\over2}-E^+.
```

Proof.

For fixed `rho`,

```math
\mathcal A_j
=
S_j{t_jC_2(\rho)\over2}
=
{\beta_jC_2(\rho)\over2}.
```

The displayed bounds on `beta_j` give `A^-` and `A^+`. The error-width
hypotheses and Theorem 8H.3 give the claimed coefficient gate. `square`

### Corollary 8H.5: Small Additive Character Error Sufficient Condition

Suppose that the Paper-14 heat-kernel neighborhood is represented by an
additive character coefficient error `delta_j`:

```math
u_{-,j}=e^{-a_j}-\delta_j,
\qquad
u_{+,j}=e^{-a_j}+\delta_j,
```

with

```math
0\le\delta_j<e^{-a_j}(1-e^{-a_j})
```

on the tested channel. Define the relative error

```math
r_j:=\delta_je^{a_j}.
```

Then the Section 8G error parameters may be taken as

```math
\eta_j=r_j,
\qquad
\zeta_j=r_j.
```

If the clean route of Corollary 8H.4 holds and

```math
\limsup_j S_j[-\log(1-r_j)]\le E^-,
```

```math
\limsup_j S_j\log(1+r_j)\le E^+,
```

with `beta_-C_2(rho)/2>E^+`, then
`P19-THICK-COEFF(A_*,B_*)` holds with the constants of Corollary 8H.4.

A simple sufficient form is:

```math
\limsup_j S_jr_j\le R_*<\infty,
\qquad
\limsup_j r_j\le r_*<1.
```

Then one may take

```math
E^-={R_*\over1-r_*},
\qquad
E^+=R_*,
```

because `-log(1-r)<=r/(1-r_*)` for `0<=r<=r_*`, and
`log(1+r)<=r`.

Proof.

The additive bounds rewrite as

```math
u_{-,j}=e^{-a_j}(1-r_j),
\qquad
u_{+,j}=e^{-a_j}(1+r_j).
```

This is exactly the Section 8G heat-kernel coefficient window with
`eta_j=zeta_j=r_j`. The remaining claims are Corollary 8H.4 plus the
elementary logarithm inequalities. `square`

### Theorem 8H.6: Exact Coefficient-Source Falsification Tests

On the declared thick branch, the reciprocal-area coefficient gate fails if
either

```math
\limsup_j S_jA_j^-=\infty,
```

or

```math
\liminf_j S_jB_j^+\le0.
```

In the source-envelope variables, a sharp falsification follows if either

```math
\limsup_j(\mathcal A_j+\mathcal E_j^-)=\infty,
```

or

```math
\liminf_j(\mathcal A_j-\mathcal E_j^+)\le0.
```

Proof.

The first condition rules out any finite `A_*`. The second rules out any
positive `B_*`. These are exactly the two clauses of
`P19-THICK-COEFF(A_*,B_*)`. The source-envelope identities are Definition
8H.1. `square`

### 8H.7 Import Verdict From Papers 14 And 16

Paper 14 supplies the coefficient machinery needed for this source attack:

```text
u_ref = exp(-t C_2(rho)/2),
u_- = u_ref - delta_CE,
u_+ = u_ref + delta_CE,
```

and the heat-kernel reference coefficient

```math
u_\rho(t)=\exp[-tC_2(\rho)/2].
```

Paper 16 supplies the heat-kernel actual-trajectory ledger and the
whole-process compatibility requirement. What Papers 14--16 do not yet
prove is the cofinal reciprocal-area estimate itself:

```math
t_j={\beta_j\over S_j},
\qquad
0<\beta_-\le\beta_j\le\beta_+<\infty,
```

with coefficient-window errors satisfying

```math
S_j[-\log(1-\eta_j)]=O(1),
\qquad
S_j\log(1+\zeta_j)=O(1),
```

and the strict nondegeneracy

```math
{\beta_-C_2(\rho)\over2}
>
E^+.
```

Thus Step 1 is now reduced to a precise source decision:

```text
prove P19-RAC-SRC with A^- > E^+
or prove one of the falsification clauses of Theorem 8H.6.
```

This is not yet an unconditional confinement proof. It is the correct next
source-constant target because it decides whether the thick-window
direct-witness branch even has a positive scalar signal before decoration and
transport losses are charged.

## 8I. Step 1a-VIII: Compatibility With The Paper-16 AF Heat-Kernel Trajectory

Section 8H says that the clean thick-window route wants

```math
t_j={\beta_j\over S_j},
\qquad
0<\beta_-\le\beta_j\le\beta_+<\infty.
```

Paper 16 does not let `t_j` float freely. On the heat-kernel actual
trajectory `HK-AYM`, the plaquette heat-kernel time is tied to the
asymptotically-free running coupling:

```math
t_i=g_i^2+O(g_i^4),
```

with

```math
g_i^{-2}
=
2\beta_0\log {1\over a_i\Lambda}
 +{\beta_1\over\beta_0}\log\log {1\over a_i\Lambda}
 +O(1).
```

Thus Step 2 is a compatibility theorem between the Paper-19 window area
`S_j` and the Paper-16 AF scale `g_i^{-2}`.

### Definition 8I.1: AF-Matched Window Area

Let `i=i(j)` be the Paper-16 heat-kernel cutoff node used by the Paper-19
Creutz window `j`. Define

```math
H_j:=g_{i(j)}^{-2}.
```

The thick window schedule is AF-matched when there are constants

```math
0<s_-\le s_+<\infty
```

such that, on a cofinal tail,

```math
s_-\le {S_j\over H_j}\le s_+.
```

Equivalently, using the Paper-16 running coupling formula, the window area
must grow like the inverse coupling:

```math
S_j
\asymp
2\beta_0\log {1\over a_{i(j)}\Lambda}
 +{\beta_1\over\beta_0}\log\log {1\over a_{i(j)}\Lambda}
 +O(1).
```

For square thick windows this means

```math
L_j^2\asymp g_{i(j)}^{-2},
\qquad
L_j\asymp g_{i(j)}^{-1}.
```

In lattice-cutoff language, `L_j` grows only logarithmically:

```math
L_j
\asymp
\sqrt{\log(1/a_{i(j)})}.
```

### Lemma 8I.2: AF-Matched Area Is Equivalent To Bounded `beta_j`

Assume the Paper-16 scheme relation

```math
t_i=g_i^2(1+\epsilon_i),
\qquad
\epsilon_i=O(g_i^2),
```

so that `epsilon_i->0`. Define the Paper-19 clean scale

```math
\beta_j:=S_jt_{i(j)}.
```

Then

```math
\beta_j
=
{S_j\over H_j}(1+\epsilon_{i(j)}).
```

Consequently, the following are equivalent on a cofinal tail:

1. `0<beta_-<=beta_j<=beta_+<infinity`;
2. `0<s_-<=S_j/H_j<=s_+<infinity`.

Proof.

Since `H_j=g_{i(j)}^{-2}`, we have `g_{i(j)}^2=H_j^{-1}`. Therefore

```math
\beta_j
=
S_jt_{i(j)}
=
S_jH_j^{-1}(1+\epsilon_{i(j)})
=
{S_j\over H_j}(1+\epsilon_{i(j)}).
```

Because `epsilon_i->0`, the factor `1+epsilon_i` is eventually bounded
above and below by positive constants. Hence positive finite bounds on
`beta_j` are equivalent to positive finite bounds on `S_j/H_j`. `square`

### Theorem 8I.3: Paper-16 Compatibility Criterion For `t_j=beta_j/S_j`

The clean reciprocal-area route of Corollary 8H.4 is compatible with the
Paper-16 heat-kernel actual trajectory if and only if the Paper-19 thick
window area is AF-matched:

```math
S_j\asymp g_{i(j)}^{-2}.
```

When this holds and the representation channel is fixed, the clean constants
in Corollary 8H.4 may be chosen from the bounds on `S_j/H_j`:

```math
A^-={s_-C_2(\rho)\over2},
\qquad
A^+={s_+C_2(\rho)\over2},
```

up to an arbitrarily small cofinal enlargement of `s_-` and `s_+` accounting
for the `O(g_i^4)` scheme term.

Proof.

By Lemma 8I.2, bounded positive `beta_j=S_jt_{i(j)}` is equivalent to
`S_j/H_j` being bounded above and below by positive constants. Corollary
8H.4 is exactly the clean route with bounded positive `beta_j`. For fixed
`rho`,

```math
\mathcal A_j
=
S_j{t_{i(j)}C_2(\rho)\over2}
=
{\beta_jC_2(\rho)\over2}.
```

Using the cofinal bounds on `beta_j` gives the stated clean constants.
`square`

### Theorem 8I.4: AF Mismatch Falsifies The Clean Thick Branch

Assume fixed `rho` and the Paper-16 heat-kernel scheme relation
`t_i=g_i^2(1+O(g_i^2))`. If

```math
{S_j\over H_j}\to0,
```

then

```math
\mathcal A_j\to0,
```

so no positive `A^-` exists for `P19-RAC-SRC`. The first-excess lower
coefficient source cannot be proved by the clean heat-kernel route.

If instead

```math
{S_j\over H_j}\to\infty,
```

then

```math
\mathcal A_j\to\infty,
```

so no finite `A^+` exists for `P19-RAC-SRC`. The leading-sheet exponent
cannot be bounded by the clean heat-kernel route.

Proof.

Using Lemma 8I.2,

```math
\mathcal A_j
=
{C_2(\rho)\over2}\beta_j
=
{C_2(\rho)\over2}{S_j\over H_j}(1+\epsilon_{i(j)}).
```

Since `1+epsilon_i->1`, the two conclusions follow immediately. `square`

### Corollary 8I.5: Square Fractional Windows Must Grow Like `sqrt(log(1/a))`

For the square fractional branch

```math
R_j=T_j=L_j,
\qquad
\sigma_j=\alpha L_j,
```

the clean Paper-16 compatible growing-window schedule must satisfy

```math
L_j^2\asymp g_{i(j)}^{-2}.
```

Using the Paper-16 running coupling,

```math
L_j^2
\asymp
2\beta_0\log {1\over a_{i(j)}\Lambda}
 +{\beta_1\over\beta_0}\log\log {1\over a_{i(j)}\Lambda}
 +O(1).
```

Thus the legal square thick direct-witness branch is not an arbitrary
large-loop limit. It is an AF-matched logarithmic cofinal window schedule.

### 8I.6 Step-2 Verdict

The schedule

```math
t_j={\beta_j\over S_j}
```

is compatible with Paper 16 only after it is reinterpreted as a restriction
on the cofinal window schedule:

```math
S_j\asymp g_{i(j)}^{-2}.
```

This is a pass for ledger compatibility, not yet a pass for confinement. It
says the thick direct-witness branch is not a formal trick if the record
windows are chosen AF-matched. But it also sharply falsifies two tempting
routes:

```text
S_j << g_i^{-2}:  clean signal scale collapses, Phi source vanishes;
S_j >> g_i^{-2}:  clean signal scale diverges, Theta source blows up.
```

The next source problem is therefore not the clean `t_j` schedule. It is the
coefficient-error budget on this AF-matched window family:

```math
S_j[-\log(1-\eta_j)]=O(1),
\qquad
S_j\log(1+\zeta_j)=O(1),
```

with the strict reserve

```math
{s_-C_2(\rho)\over2}>E^+.
```

## 8J. Step 1a-IX: AF-Matched Coefficient-Error Budget

The clean heat-kernel scale is now ledger-compatible. The remaining
coefficient question is the error width around the heat-kernel reference.
Paper 14 represents this by an additive character coefficient error. On the
AF-matched schedule, that error must be of order `g_i^2`, equivalently of
order `1/S_j`.

### Definition 8J.1: AF-Matched Relative Character Error

Assume:

1. the fixed representation channel `rho`;
2. the AF-matched window area of Definition 8I.1:

   ```math
   s_-\le {S_j\over H_j}\le s_+,
   \qquad
   H_j=g_{i(j)}^{-2};
   ```

3. the Paper-14 additive character window:

   ```math
   u_{-,j}=e^{-a_j}-\delta_j,
   \qquad
   u_{+,j}=e^{-a_j}+\delta_j,
   ```

   with

   ```math
   a_j={t_{i(j)}C_2(\rho)\over2}.
   ```

Define the relative coefficient error

```math
r_j:=\delta_je^{a_j}.
```

The AF-matched coefficient-error gate
`P19-AFM-CEERR(R_H,r_*)` holds when

```math
\limsup_j H_jr_j\le R_H<\infty,
```

and

```math
\limsup_j r_j\le r_*<1.
```

The first clause is the real scale statement: since `H_j~S_j`, it says the
relative coefficient error is `O(g_i^2)`.

### Lemma 8J.2: AF-Matched Error Gate Bounds The Section-8H Widths

Assume the AF-matched schedule and `P19-AFM-CEERR(R_H,r_*)`. Then

```math
\limsup_j S_j\log(1+r_j)\le s_+R_H,
```

and

```math
\limsup_j S_j[-\log(1-r_j)]
\le
{s_+R_H\over1-r_*}.
```

Thus Corollary 8H.5 applies with

```math
E^+=s_+R_H,
\qquad
E^-={s_+R_H\over1-r_*}.
```

Proof.

The AF-matched upper area bound gives

```math
S_jr_j
\le
s_+H_jr_j
```

cofinally in limsup. Since `log(1+r)<=r`, the upper-window estimate follows.
For the lower window, `r_j<=r_*<1` cofinally and

```math
-\log(1-r)\le {r\over1-r_*}
```

for `0<=r<=r_*`. Multiplying by `S_j` and taking limsup gives the second
bound. `square`

### Theorem 8J.3: AF-Matched Coefficient Errors Prove `P19-RAC-SRC`

Assume:

1. the fixed representation channel `rho`;
2. the Paper-16 scheme relation

   ```math
   t_i=g_i^2(1+O(g_i^2));
   ```

3. the AF-matched area bounds

   ```math
   s_-\le {S_j\over H_j}\le s_+;
   ```

4. `P19-AFM-CEERR(R_H,r_*)`;
5. a scheme slack `0<chi<1` chosen so that cofinally

   ```math
   1-\chi\le {t_{i(j)}\over g_{i(j)}^2}\le1+\chi;
   ```

6. the strict reserve inequality

   ```math
   {(1-\chi)s_-C_2(\rho)\over2}>s_+R_H.
   ```

Then `P19-RAC-SRC(A^-,A^+,E^-,E^+)` holds with

```math
A^-={(1-\chi)s_-C_2(\rho)\over2},
\qquad
A^+={(1+\chi)s_+C_2(\rho)\over2},
```

and

```math
E^+=s_+R_H,
\qquad
E^-={s_+R_H\over1-r_*}.
```

Consequently `P19-THICK-COEFF(A_*,B_*)` holds with

```math
A_*={(1+\chi)s_+C_2(\rho)\over2}+{s_+R_H\over1-r_*},
```

and

```math
B_*={(1-\chi)s_-C_2(\rho)\over2}-s_+R_H>0.
```

Proof.

By Section 8I,

```math
\mathcal A_j
=
S_j{t_{i(j)}C_2(\rho)\over2}
=
{C_2(\rho)\over2}{S_j\over H_j}
{t_{i(j)}\over g_{i(j)}^2}.
```

The AF-matched bounds and scheme slack give the displayed `A^-` and `A^+`.
Lemma 8J.2 gives `E^-` and `E^+`. The strict reserve inequality is exactly
`A^->E^+`. Theorem 8H.3 then proves the thick coefficient gate with the
displayed `A_*` and `B_*`. `square`

### Theorem 8J.4: Coefficient-Error Falsification

On an AF-matched branch with fixed `rho`, if

```math
\limsup_j H_jr_j=\infty,
```

then the Paper-14 additive-error route does not supply finite Section-8H
error widths, so it cannot prove `P19-RAC-SRC` by the direct coefficient
window.

If, more sharply,

```math
\liminf_j
\left[
{C_2(\rho)\over2}{S_j\over H_j}{t_{i(j)}\over g_{i(j)}^2}
-S_j\log(1+r_j)
\right]
\le0,
```

then `P19-THICK-COEFF(A_*,B_*)` is false on this branch.

Proof.

The first claim says the available upper error budget `E^+` or lower error
budget `E^-` is infinite under the Paper-14 additive route. The second claim
is exactly

```math
\liminf_j S_jB_j^+\le0,
```

because `S_jB_j^+=\mathcal A_j-\mathcal E_j^+`. Theorem 8H.6 gives the
falsification. `square`

### 8J.5 Coefficient-Error Verdict

Step 1 now has an actual coefficient-error target:

```math
r_j=\delta_je^{a_j}=O(g_i^2),
```

with a constant small enough that

```math
{s_-C_2(\rho)\over2}>s_+R_H
```

after scheme slack. Paper 14 supplies the additive error framework. Paper 16
supplies the AF heat-kernel trajectory. What is not yet proved in the source
papers is this `O(g_i^2)` relative character-error estimate on the same
whole-process tower and the same AF-matched Creutz windows.

### 8J.6 Attempt From The Paper-14 Rate Class

Paper 14 gives an admissible coefficient-error rate class of the form

```math
\delta_j\le C_{CE} n_j^{-1-p_{CE}},
\qquad
p_{CE}>0,
```

on a standard continuum chain. This is a summability statement in the chain
index `n_j`. It proves the AF-matched estimate only if the chain index is
calibrated against the AF coupling.

Let

```math
L_j:=\log {1\over a_{i(j)}\Lambda}.
```

By Paper 16,

```math
g_{i(j)}^{-2}
=
2\beta_0L_j+{\beta_1\over\beta_0}\log L_j+O(1),
```

so

```math
g_{i(j)}^2
\asymp
{1\over L_j}
```

on the cofinal AF tail. Also, on the AF-matched branch,

```math
a_j={t_{i(j)}C_2(\rho)\over2}=O(g_{i(j)}^2),
```

hence `e^{a_j}` is cofinally bounded above and below by positive constants.

### Theorem 8J.6A: Paper-14 Polynomial Rate Proves `r_j=O(g_i^2)` Under Chain Calibration

Assume the Paper-14 coefficient-error rate

```math
\delta_j\le C_{CE}n_j^{-1-p_{CE}},
```

and the chain-calibration bound

```math
L_j\le C_L n_j^{1+p_{CE}}
```

on the same cofinal tower. Then

```math
r_j=\delta_je^{a_j}=O(g_{i(j)}^2).
```

More explicitly, for a cofinal constant `C_a` with `e^{a_j}\le C_a`,

```math
g_{i(j)}^{-2}r_j
\le
C_a C_{CE}\,
{g_{i(j)}^{-2}\over n_j^{1+p_{CE}}}
\le
C_a C_{CE} C_g C_L,
```

where `C_g` is any cofinal constant satisfying `g_i^{-2}\le C_gL_i`.

Proof.

The Paper-16 AF formula implies `g_i^{-2}<=C_gL_i` cofinally. Therefore

```math
g_{i(j)}^{-2}r_j
=
g_{i(j)}^{-2}\delta_je^{a_j}
\le
C_gL_j C_{CE}n_j^{-1-p_{CE}}C_a
\le
C_aC_{CE}C_gC_L.
```

This is exactly `limsup H_jr_j<infinity`, since `H_j=g_{i(j)}^{-2}`.
`square`

### Corollary 8J.6B: Exponential-In-Index Lattice Refinement

If

```math
a_{i(j)}\Lambda\asymp e^{-c n_j^\kappa}
```

with constants `c>0` and `0<\kappa\le1+p_{CE}`, then the Paper-14
polynomial coefficient-error rate proves

```math
r_j=O(g_{i(j)}^2).
```

Proof.

The hypothesis gives `L_j=O(n_j^\kappa)`. Since
`\kappa<=1+p_CE`, the calibration bound of Theorem 8J.6A holds. `square`

### Theorem 8J.6C: What The Present Source Papers Do Not Prove

The present Paper-14 rate class, by itself, does not prove

```math
r_j=O(g_i^2)
```

on an arbitrary continuum chain. It proves the estimate only together with a
chain-calibration bound such as

```math
\log {1\over a_i\Lambda}
\le
C_L n_i^{1+p_{CE}}.
```

If the declared chain has

```math
{\log(1/(a_i\Lambda))\over n_i^{1+p_{CE}}}\to\infty,
```

then the Paper-14 polynomial upper bound is too weak to imply
`r_j=O(g_i^2)`. This is not a falsification of the actual coefficient error;
it is a falsification of the proof from that rate class alone.

Proof.

The estimate needed is `delta_j e^{a_j}<=C g_i^2`. Since `e^{a_j}` is
bounded above and below on the AF tail, this is equivalent at the level of
upper bounds to `delta_j=O(g_i^2)`. Paper 14 supplies only
`delta_j<=C n_j^{-1-p_CE}`. Comparing with `g_i^2~1/L_i`, this proves the
needed estimate only when `L_i=O(n_i^{1+p_CE})`. If that comparison fails,
the displayed Paper-14 upper bound no longer implies the needed AF-scaled
bound. No lower bound on `delta_j` is supplied, so the actual estimate is not
falsified. `square`

### 8J.6D Coefficient-Error Estimate Verdict

The requested coefficient-error estimate is therefore decided as follows.

From the current source papers alone:

```text
not unconditionally proved;
not falsified.
```

From Paper 14 plus a calibrated standard chain satisfying

```math
\log {1\over a_i\Lambda}
\le
C_L n_i^{1+p_{CE}},
```

it is proved:

```math
r_j=O(g_i^2).
```

For chains whose cutoff refinement is too fast compared with the Paper-14
coefficient-error rate, the existing Paper-14 rate ledger is insufficient;
one must either strengthen the coefficient-error rate or slow/reindex the
standard chain. The remaining small-constant condition is separate:

```math
{(1-\chi)s_-C_2(\rho)\over2}>s_+R_H.
```

That condition requires the actual smallness of `R_H`, not merely its
finiteness. The next subsection turns that into a sharp limsup test.

### 8J.7 Resolving The Coefficient-Error Constant `R_H`

The constant `R_H` is not a new physical parameter. It is the scalar debit
assigned to the relative character-coefficient error on the declared
whole-process tower. Thus it is resolved by the tower itself:

```math
R_H^{opt}
:=
\limsup_j H_jr_j
=
\limsup_j g_{i(j)}^{-2}\delta_je^{a_j}.
```

This is the smallest admissible `R_H` for the `P19-AFM-CEERR` route.

### Lemma 8J.7A: Minimality Of `R_H^{opt}`

If `R_H^{opt}<\infty`, then `P19-AFM-CEERR(R_H,r_*)` holds for every
`R_H>=R_H^{opt}` and every fixed `0<r_*<1` after passing to a cofinal tail.
If `R_H<R_H^{opt}`, then `P19-AFM-CEERR(R_H,r_*)` fails for every `r_*`.

Proof.

The first clause of `P19-AFM-CEERR` is exactly

```math
\limsup_j H_jr_j\le R_H.
```

If this limsup is finite, then `r_j=O(H_j^{-1})`. Since `H_j=g_i^{-2}->infty`
on the AF tail, `r_j->0`, so every fixed `0<r_*<1` holds cofinally. If
`R_H<R_H^{opt}`, the limsup inequality is false. `square`

### Definition 8J.7B: Critical Coefficient-Error Threshold

For the AF-matched coefficient theorem with fixed `rho`, area bounds
`s_-<=S_j/H_j<=s_+`, and scheme slack `chi`, define

```math
R_H^{crit}
:=
{(1-\chi)s_-C_2(\rho)\over2s_+}.
```

This is the largest relative-error debit allowed by the Section-8J
coefficient theorem.

### Theorem 8J.7C: Exact `R_H` Pass/Fail Test For The Section-8J Route

The `R_H`-based AF-matched coefficient-error route passes exactly when

```math
R_H^{opt}<R_H^{crit}.
```

If `R_H^{opt}>=R_H^{crit}`, then no admissible `R_H` can satisfy the strict
reserve inequality in Theorem 8J.3. This does not by itself falsify every
possible coefficient argument; it falsifies this `R_H`-based sufficient route.

Proof.

By Lemma 8J.7A, every admissible `R_H` must satisfy
`R_H>=R_H^{opt}`. The strict reserve inequality of Theorem 8J.3 is

```math
R_H<R_H^{crit}.
```

Such an `R_H` exists if and only if `R_H^{opt}<R_H^{crit}`. `square`

### Theorem 8J.7D: Paper-14/Paper-16 Source Bound For `R_H^{opt}`

Let

```math
L_j:=\log {1\over a_{i(j)}\Lambda},
```

and suppose the Paper-14 coefficient-error source has an asymptotic constant

```math
K_{CE}:=
\limsup_j n_j^{1+p_{CE}}\delta_j<\infty,
```

while the declared standard chain has an AF calibration constant

```math
K_L:=
\limsup_j {L_j\over n_j^{1+p_{CE}}}<\infty.
```

Then

```math
R_H^{opt}
\le
2\beta_0 K_{CE} K_L.
```

Consequently the Paper-14/Paper-16 source route proves the `R_H` smallness
condition if

```math
2\beta_0 K_{CE} K_L
<
{(1-\chi)s_-C_2(\rho)\over2s_+}.
```

Proof.

Paper 16 gives

```math
g_{i(j)}^{-2}
=
2\beta_0L_j
 +{\beta_1\over\beta_0}\log L_j
 +O(1),
```

so

```math
{g_{i(j)}^{-2}\over L_j}\to2\beta_0.
```

On the AF tail,

```math
a_j={t_{i(j)}C_2(\rho)\over2}=O(g_{i(j)}^2),
```

hence `e^{a_j}->1`. Therefore

```math
R_H^{opt}
=
\limsup_j
{g_{i(j)}^{-2}\over L_j}
\, e^{a_j}\,
\left(n_j^{1+p_{CE}}\delta_j\right)
\left({L_j\over n_j^{1+p_{CE}}}\right)
\le
2\beta_0 K_{CE} K_L.
```

The last displayed strict inequality puts this source upper bound below
`R_H^crit`, so Theorem 8J.7C closes the `R_H` route. `square`

### Corollary 8J.7E: Polynomial-Rate Constants

If Paper 14 supplies the explicit bound

```math
\delta_j\le C_{CE}n_j^{-1-p_{CE}},
```

and the chain calibration satisfies

```math
L_j\le C_Ln_j^{1+p_{CE}}
```

cofinally, then

```math
R_H^{opt}\le2\beta_0 C_{CE} C_L.
```

The coefficient-error source passes through the Section-8J route if

```math
2\beta_0 C_{CE} C_L
<
{(1-\chi)s_-C_2(\rho)\over2s_+}.
```

### Theorem 8J.7F: Current Verdict On `R_H`

The constant `R_H` is now mathematically resolved as the sharp limsup

```math
R_H^{opt}
=
\limsup_j g_{i(j)}^{-2}\delta_je^{a_j}.
```

The current source papers do not yet give the numerical or symbolic
smallness estimate

```math
R_H^{opt}<R_H^{crit}.
```

They do give a clean sufficient route:

```math
2\beta_0 K_{CE} K_L<R_H^{crit}.
```

What remains missing is an actual same-tower bound on the product
`K_CE K_L` small enough to satisfy this inequality. Without that bound,
`R_H` is finite only conditionally and small only conditionally. Without a
lower bound on `delta_j`, the present papers also do not falsify the actual
smallness of `R_H^{opt}`.

Proof.

The identity defining `R_H^opt` is Lemma 8J.7A. The sufficient route is
Theorem 8J.7D. Papers 14 and 16 provide the rate framework and AF comparison,
but they do not supply a same-tower estimate proving
`2 beta_0 K_CE K_L<R_H^crit`, nor do they supply lower bounds implying
`R_H^opt>=R_H^crit`. `square`

### 8J.8 AF-Normalized Coefficient-Defect Attack

Section 8J.7 resolves `R_H` as a limsup. The next sharper attack is to avoid
chain-index rates as the primary object and prove the coefficient defect
directly in asymptotic-freedom units.

### Definition 8J.8A: AF-Normalized Coefficient Defect

The AF-normalized coefficient-defect certificate
`P19-AFCE(K_AF)` holds when

```math
\limsup_j{\delta_j\over g_{i(j)}^2}\le K_{AF}<\infty.
```

The certificate is same-ledger only if `delta_j` is measured on the same
finite Creutz-character battery, the same block plaquette marginal, and the
same pushed-forward whole-process laws used by Sections 8G--8K.

### Theorem 8J.8B: AF-Normalized Defect Resolves `R_H`

If `P19-AFCE(K_AF)` holds, then

```math
R_H^{opt}\le K_{AF}.
```

Consequently the Section-8J coefficient route passes if

```math
K_{AF}<R_H^{crit}.
```

Proof.

By definition,

```math
R_H^{opt}
=
\limsup_j g_{i(j)}^{-2}\delta_je^{a_j}.
```

On the AF tail, `a_j=O(g_i^2)`, hence `e^{a_j}->1`. Therefore

```math
R_H^{opt}
=
\limsup_j {\delta_j\over g_{i(j)}^2}
\le K_{AF}.
```

If `K_AF<R_H^crit`, then `R_H^opt<R_H^crit`, so Theorem 8J.7C applies.
`square`

### Definition 8J.8C: Source Decomposition Of `delta_j`

The coefficient defect is source-decomposed when there are nonnegative
same-ledger pieces

```math
\delta_{{HK},j},
\delta_{{proj},j},
\delta_{{chart},j},
\delta_{{ct},j},
\delta_{{vol},j},
\delta_{{tail},j}
```

such that

```math
\delta_j
\le
\delta_{{HK},j}
+\delta_{{proj},j}
+\delta_{{chart},j}
+\delta_{{ct},j}
+\delta_{{vol},j}
+\delta_{{tail},j}.
```

Their intended meanings are:

```text
delta_HK    = deviation from the heat-kernel block-plaquette reference;
delta_proj  = finite-battery projection/readout drift;
delta_chart = gauge-chart or regulator-coordinate transport drift;
delta_ct    = running counterterm/local-action transport drift;
delta_vol   = finite-volume and boundary-buffer drift;
delta_tail  = representation-tail and untested-character leakage.
```

Each term is a difference of finite record-law expectations or character
coefficients. None is a hidden field variable.

### Theorem 8J.8D: Source Pieces Prove AF-Normalized Defect

Assume the source decomposition of Definition 8J.8C and constants

```math
K_{HK},K_{proj},K_{chart},K_{ct},K_{vol},K_{tail}
```

such that

```math
\limsup_j{\delta_{{HK},j}\over g_{i(j)}^2}\le K_{HK},
\qquad
\limsup_j{\delta_{{proj},j}\over g_{i(j)}^2}\le K_{proj},
```

```math
\limsup_j{\delta_{{chart},j}\over g_{i(j)}^2}\le K_{chart},
\qquad
\limsup_j{\delta_{{ct},j}\over g_{i(j)}^2}\le K_{ct},
```

```math
\limsup_j{\delta_{{vol},j}\over g_{i(j)}^2}\le K_{vol},
\qquad
\limsup_j{\delta_{{tail},j}\over g_{i(j)}^2}\le K_{tail}.
```

Let

```math
K_{AF}^{src}
:=
K_{HK}+K_{proj}+K_{chart}+K_{ct}+K_{vol}+K_{tail}.
```

Then `P19-AFCE(K_AF^src)` holds. If

```math
K_{AF}^{src}<R_H^{crit},
```

then the coefficient-error source is resolved.

Proof.

Divide the source decomposition by `g_i^2`, take limsups, and use
subadditivity of `limsup` for nonnegative sequences. This gives

```math
\limsup_j{\delta_j\over g_{i(j)}^2}
\le
K_{AF}^{src}.
```

Theorem 8J.8B then gives the coefficient pass whenever
`K_AF^src<R_H^crit`. `square`

### Theorem 8J.8E: Threshold Optimization

For a fixed representation channel `rho`, the Section-8J threshold is

```math
R_H^{crit}(\chi,s_-,s_+,\rho)
=
{(1-\chi)s_-C_2(\rho)\over2s_+}.
```

Within the declared AF-matched branch, the threshold is increased by:

1. shrinking scheme slack `chi`;
2. choosing a tighter area schedule, so `s_-/s_+` is closer to one;
3. choosing a representation channel with larger `C_2(rho)`, provided the
   same Paper-14/Paper-15 batteries still have controlled tails and positive
   first-excess reserve.

More precisely, if a source estimate gives `K_AF^src`, then the admissible
window/channel choices are exactly those satisfying

```math
{s_-\over s_+}
>
{2K_{AF}^{src}\over(1-\chi)C_2(\rho)}.
```

Proof.

The coefficient pass condition is `K_AF^src<R_H^crit`. Substituting the
definition of `R_H^crit` and solving for `s_-/s_+` gives the displayed
inequality. The three monotonicity claims are immediate from the same
formula, subject to the independent same-ledger constraints on tails,
batteries, and first-excess reserve. `square`

### 8J.8F Verdict After The Three Pushes

The coefficient-error problem is now organized into three nested routes:

```text
sharp route:
  R_H^opt < R_H^crit;

AF-normalized route:
  limsup delta_j/g_i^2 <= K_AF < R_H^crit;

source-decomposed route:
  K_HK+K_proj+K_chart+K_ct+K_vol+K_tail < R_H^crit.
```

This is stronger and cleaner than the earlier Paper-14 chain-index route.
It says exactly what must be proved next: each source piece of `delta_j`
must be bounded at order `g_i^2` on the same whole-process tower, and the
sum must fit under the optimized threshold. The current source papers do not
yet provide those six AF-normalized constants, and they do not prove that
their sum is below the optimized threshold.

### 8J.9 Optimized AF-Area, Slack, And Representation Selector

The previous subsection gives the threshold. This subsection turns the
optimization instruction into an explicit selector theorem.

### Definition 8J.9A: Tight AF-Area Schedule

For constants `s>0` and `0<epsilon_A<1`, the AF-area schedule is
`(s,epsilon_A)`-tight when

```math
s(1-\epsilon_A)
\le
{S_j\over H_j}
\le
s(1+\epsilon_A)
```

cofinally. In the notation of Theorem 8J.3 this means

```math
s_-:=s(1-\epsilon_A),
\qquad
s_+:=s(1+\epsilon_A).
```

The coefficient-error threshold becomes

```math
R_H^{crit}(\epsilon_A,\chi,\rho)
=
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho)\over2}.
```

The absolute scale `s` cancels from this threshold. It still matters for the
geometric window and for the eventual signal/loss comparison, but not for
the `R_H` smallness inequality.

### Lemma 8J.9B: Scheme Slack Can Be Made Arbitrarily Small On A Tail

Because Paper 16 gives

```math
{t_i\over g_i^2}\to1,
```

for every `0<chi<1` there is a cofinal tail on which

```math
1-\chi
\le
{t_{i(j)}\over g_{i(j)}^2}
\le
1+\chi.
```

Thus `chi` is a tail-selection tolerance, not an additional ontology or a
new dynamical parameter.

Proof.

This is the definition of convergence of `t_i/g_i^2` to one, restricted to
the declared cofinal tower. `square`

### Definition 8J.9C: Representation-Admissible Selector Class

Fix a tight AF-area tolerance `epsilon_A` and a slack tolerance `chi`.
A representation channel `rho` is selector-admissible when all of the
following are true on the same whole-process tower:

1. `rho` and all forced character records generated by the Paper-14/15
   battery closure are included in the declared finite record battery;
2. the AF-normalized source constants

   ```math
   K_{HK}(\rho),K_{proj}(\rho),K_{chart}(\rho),
   K_{ct}(\rho),K_{vol}(\rho),K_{tail}(\rho)
   ```

   exist as finite limsup bounds for the six pieces of Definition 8J.8C;
3. the representation-tail and decoration conversion ledgers remain finite
   for that same channel, so enlarging `rho` does not silently spend the
   Paper-15 loss budget;
4. the thick-window geometry still has `q_->0` and `n_+<infinity`;
5. the first-excess coefficient reserve is positive after the source debit:

   ```math
   K_{AF}^{src}(\rho)
   <
   R_H^{crit}(\epsilon_A,\chi,\rho),
   ```

   where

   ```math
   K_{AF}^{src}(\rho)
   :=
   K_{HK}(\rho)+K_{proj}(\rho)+K_{chart}(\rho)
   +K_{ct}(\rho)+K_{vol}(\rho)+K_{tail}(\rho).
   ```

Write the resulting selector class as

```math
{\mathcal R}_{adm}(\epsilon_A,\chi).
```

This definition is intentionally conservative: a larger `C_2(rho)` helps
only if the same `rho` keeps the tail, battery, and first-excess records
under control.

### Theorem 8J.9D: Optimized Selector Closure

Assume:

1. a thick direct-witness window branch;
2. an `(s,epsilon_A)`-tight AF-area schedule;
3. the scheme slack tail of Lemma 8J.9B for `chi`;
4. a representation channel

   ```math
   \rho\in{\mathcal R}_{adm}(\epsilon_A,\chi).
   ```

Then the coefficient-error source is resolved:

```math
R_H^{opt}<R_H^{crit}(\epsilon_A,\chi,\rho).
```

Consequently the Section-8J coefficient gate passes.

Proof.

By selector admissibility, the six AF-normalized source constants exist and
their sum satisfies

```math
K_{AF}^{src}(\rho)<R_H^{crit}(\epsilon_A,\chi,\rho).
```

Theorem 8J.8D gives `P19-AFCE(K_AF^src(rho))`, and Theorem 8J.8B gives

```math
R_H^{opt}\le K_{AF}^{src}(\rho).
```

Therefore

```math
R_H^{opt}<R_H^{crit}(\epsilon_A,\chi,\rho),
```

and Theorem 8J.7C closes the coefficient gate. `square`

### Corollary 8J.9E: Near-Optimal Tight-Schedule Limit

Suppose there is a channel `rho` and a source constant `K_{AF}^{src}(rho)`
such that the tail/decorations and thick-window records are controlled and

```math
K_{AF}^{src}(\rho)<{C_2(\rho)\over2}.
```

Then there exist small enough `epsilon_A>0` and `chi>0` such that

```math
\rho\in{\mathcal R}_{adm}(\epsilon_A,\chi).
```

Equivalently, if there is a strict limiting margin below `C_2(rho)/2`, then
one can tighten the AF area schedule and minimize scheme slack enough to make
the `R_H` gate pass.

Proof.

Since

```math
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
\to1
```

as `chi,epsilon_A->0`, the strict inequality
`K_AF^src(rho)<C_2(rho)/2` remains true after multiplying
`C_2(rho)/2` by the displayed factor, provided `chi` and `epsilon_A` are
small enough. The remaining admissibility clauses are exactly the assumed
tail/decorations and thick-window controls. `square`

### Theorem 8J.9F: Selector Obstruction

If, for every channel whose tail, decoration, battery, and first-excess
ledgers are controlled,

```math
K_{AF}^{src}(\rho)
\ge
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho)\over2},
```

then the optimized selector cannot resolve `R_H` at tolerances
`(epsilon_A,chi)`.

If the stronger limiting obstruction holds,

```math
K_{AF}^{src}(\rho)\ge {C_2(\rho)\over2}
```

for every channel with controlled tail/decorations and first-excess ledgers,
then no amount of tightening the AF area schedule or minimizing scheme slack
can close this Section-8J route.

Proof.

The first statement is the negation of the selector-admissible strict
coefficient inequality. The second follows by taking
`epsilon_A,chi` arbitrarily small, for which the threshold tends upward to
`C_2(rho)/2` but never exceeds it. `square`

### 8J.9G Selector Verdict

Paper 19 now has an explicit optimization rule:

```text
1. choose S_j/H_j in [s(1-epsilon_A), s(1+epsilon_A)];
2. pass to a tail where t_i/g_i^2 is in [1-chi,1+chi];
3. choose rho only inside R_adm(epsilon_A,chi);
4. test K_AF^src(rho) < [(1-chi)(1-epsilon_A)/(1+epsilon_A)] C_2(rho)/2.
```

This is the strongest honest coefficient selector currently available. It
pushes the route to the limit allowed by the source estimates while keeping
the ontology clean: the chosen area schedule, slack, and representation
channel are all record-ledger choices, and each is rejected if it breaks the
tail, decoration, battery, or first-excess ledgers.

### 8J.10 First Selector Candidate And Six-Source Ledger

We now freeze the first concrete selector candidate. This is not a claim that
the candidate passes. It is the first same-ledger row on which the six
AF-normalized source constants must be proved or falsified.

### Definition 8J.10A: First Selector Candidate `SEL_0`

Let `rho_0` be the lowest nontrivial controlled `SU(N)` channel in the
declared record battery. Concretely, this is the fundamental channel, or the
paired fundamental real-character channel when the operational battery stores
real paired characters. Its quadratic Casimir is denoted

```math
C_0:=C_2(\rho_0).
```

Fix:

```math
0<\alpha<1,
\qquad
s>0,
\qquad
0<\epsilon_A<1,
\qquad
0<\chi<1.
```

The first selector candidate `SEL_0(s,alpha,epsilon_A,chi)` uses:

```math
R_j=T_j=L_j,
\qquad
L_j:=\left\lfloor \sqrt{sH_j}\right\rfloor,
\qquad
\sigma_j:=\left\lfloor \alpha L_j\right\rfloor,
```

after passing to a tail on which `L_j>=1` and `sigma_j>=1`. The AF-area
scale is

```math
S_j:=L_j^2.
```

The representation channel is `rho_0`, unless `rho_0` fails the tail,
decoration, battery, or first-excess admissibility tests. In that case
`SEL_0` is not admissible; one does not repair it by moving to a larger
Casimir outside the controlled ledger.

### Lemma 8J.10B: `SEL_0` Is A Tight Thick Schedule

For every `epsilon_A>0`, the integer-rounded square schedule in Definition
8J.10A is `(s,epsilon_A)`-tight on a cofinal tail:

```math
s(1-\epsilon_A)
\le
{S_j\over H_j}
\le
s(1+\epsilon_A).
```

Moreover, for every small geometry tolerance `epsilon_G>0`, on a cofinal
tail,

```math
\alpha^2-\epsilon_G
\le
{Q_{\sigma,j}\over S_j}
\le
\alpha^2+\epsilon_G,
```

and

```math
2(1-\alpha)-\epsilon_G
\le
{N_{0,j}\over S_j}
\le
2(1-\alpha)+\epsilon_G.
```

Thus `SEL_0` is a thick direct-witness branch whenever
`0<epsilon_G<min{alpha^2,2(1-alpha)}`.

Proof.

Since `H_j->infinity`, the rounding error in
`L_j=floor(sqrt(sH_j))` is `o(sqrt(H_j))`. Therefore
`L_j^2/H_j->s`, which proves the tight AF-area bounds on a tail. Likewise,
`sigma_j/L_j->alpha`, so the square-window formulas of Definition 8G.1 give
`Q_sigma,j/S_j->alpha^2` and `N_0,j/S_j->2(1-alpha)`. The displayed
two-sided estimates follow by passing to a tail. `square`

### Definition 8J.10C: First-Selector Threshold

For `SEL_0`, the optimized coefficient threshold is

```math
R_{0}^{crit}
:=
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_0\over2}.
```

With geometry tolerance `epsilon_G`, the corresponding direct-witness signal
constants may be taken as

```math
q_{0,-}:=\alpha^2-\epsilon_G,
\qquad
n_{0,+}:=2(1-\alpha)+\epsilon_G.
```

These geometric constants are recorded here because they later enter
`Sig_AFM`; the coefficient-error threshold itself is `R_0^crit`.

### Definition 8J.10D: Six-Source Ledger For `SEL_0`

For the first selector candidate, define the six AF-normalized source
constants:

```math
K_{HK}^{(0)}
:=
\limsup_j{\delta_{{HK},j}^{(0)}\over g_{i(j)}^2},
\qquad
K_{proj}^{(0)}
:=
\limsup_j{\delta_{{proj},j}^{(0)}\over g_{i(j)}^2},
```

```math
K_{chart}^{(0)}
:=
\limsup_j{\delta_{{chart},j}^{(0)}\over g_{i(j)}^2},
\qquad
K_{ct}^{(0)}
:=
\limsup_j{\delta_{{ct},j}^{(0)}\over g_{i(j)}^2},
```

```math
K_{vol}^{(0)}
:=
\limsup_j{\delta_{{vol},j}^{(0)}\over g_{i(j)}^2},
\qquad
K_{tail}^{(0)}
:=
\limsup_j{\delta_{{tail},j}^{(0)}\over g_{i(j)}^2}.
```

The superscript `(0)` means every defect is evaluated on the same
`SEL_0` windows, the same `rho_0` record battery, and the same pushed-forward
whole-process laws. The total first-selector coefficient debit is

```math
K_{0}^{src}
:=
K_{HK}^{(0)}
+K_{proj}^{(0)}
+K_{chart}^{(0)}
+K_{ct}^{(0)}
+K_{vol}^{(0)}
+K_{tail}^{(0)}.
```

The six rows are:

```text
K_HK^(0):
  block-plaquette coefficient deviation from the heat-kernel reference;

K_proj^(0):
  finite-battery projection and readout drift;

K_chart^(0):
  regulator/gauge-chart transport drift;

K_ct^(0):
  running counterterm and local-action transport drift;

K_vol^(0):
  finite-volume, boundary-buffer, and infrared-window drift;

K_tail^(0):
  representation-tail and untested-character leakage.
```

### Definition 8J.10E: First-Selector Ledger Pass/Fail Margin

Define the first-selector coefficient margin

```math
M_{CE}^{(0)}
:=
R_{0}^{crit}-K_{0}^{src}.
```

The first selector passes the coefficient source when

```math
M_{CE}^{(0)}>0.
```

It fails as a first selector when either:

1. one of the six constants is not finite on the same ledger;
2. `rho_0` fails the tail, decoration, battery, or first-excess admissibility
   tests;
3. `M_CE^(0)<=0`.

The third clause only falsifies `SEL_0`, not every possible admissible
channel.

### Theorem 8J.10F: First-Selector Coefficient Closure

Assume `SEL_0` is admissible and

```math
M_{CE}^{(0)}>0.
```

Then the coefficient-error source is resolved for the first selector:

```math
R_H^{opt}<R_{0}^{crit}.
```

Consequently the Section-8J coefficient gate passes with `rho=rho_0` and the
tight AF-area/slack tolerances of `SEL_0`.

Proof.

By Definition 8J.10D, the six source constants define
`K_AF^src(rho_0)=K_0^src`. The strict margin `M_CE^(0)>0` is exactly

```math
K_{AF}^{src}(\rho_0)<R_0^{crit}.
```

Theorem 8J.9D then gives

```math
R_H^{opt}<R_0^{crit}.
```

This is the Section-8J coefficient pass. `square`

### 8J.10G First-Selector Verdict

Steps 1--2 are now frozen:

```text
candidate:
  rho_0 = fundamental or paired fundamental controlled record;
  L_j = floor(sqrt(s H_j));
  sigma_j = floor(alpha L_j);
  S_j/H_j -> s;
  t_i/g_i^2 in [1-chi,1+chi] on a tail.

six-source ledger:
  K_0^src =
    K_HK^(0)+K_proj^(0)+K_chart^(0)
    +K_ct^(0)+K_vol^(0)+K_tail^(0).

coefficient pass:
  K_0^src
  <
  [(1-chi)(1-epsilon_A)/(1+epsilon_A)] C_2(rho_0)/2.
```

The current source papers still do not prove this inequality. They now have
a precise first row to attack: prove or falsify the six constants for
`SEL_0`, starting with `K_HK^(0)`.

### 8J.11 First Attack On `K_HK^(0)`

The first source constant in `SEL_0` is the heat-kernel reference defect.
This is the part of `delta_j` that compares the actual block-plaquette
coefficient in the `rho_0` channel with the heat-kernel coefficient before
projection, chart, counterterm, volume, and tail debits are charged.

The correct order is decomposition first, branch choice second. Fixed-time
and matched-time are proof-coordinate choices made after the record-law
debit has been split into its source pieces.

### Definition 8J.11A: Decomposition-First Heat-Kernel Defect Ledger

Let

```math
u_{0,j}^{bare}
:=
\exp\left(-{t_{i(j)}C_0\over2}\right)
```

be the fixed Paper-16 bare heat-kernel coefficient for `rho_0`. A
decomposition-first heat-kernel defect ledger is a same-tower chain of
coefficient records

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
u_bare  = fixed Paper-16 heat-kernel coefficient;
u_time  = coefficient after the local time/scheme shift only;
u_block = coefficient after same-block local interaction corrections;
u_res   = coefficient after cross-block residual-polymer corrections;
u_act   = actual extracted block-plaquette coefficient.
```

The corresponding nonnegative source debits are

```math
\delta_{{time},j}^{(0)}
:=
\left|u_{0,j}^{time}-u_{0,j}^{bare}\right|,
\qquad
\delta_{{block},j}^{(0)}
:=
\left|u_{0,j}^{block}-u_{0,j}^{time}\right|,
```

```math
\delta_{{cross},j}^{(0)}
:=
\left|u_{0,j}^{res}-u_{0,j}^{block}\right|,
\qquad
\delta_{{extract},j}^{(0)}
:=
\left|u_{0,j}^{act}-u_{0,j}^{res}\right|.
```

Define the AF-normalized constants

```math
K_{time}^{(0)}
:=
\limsup_j{\delta_{{time},j}^{(0)}\over g_{i(j)}^2},
\qquad
K_{block}^{(0)}
:=
\limsup_j{\delta_{{block},j}^{(0)}\over g_{i(j)}^2},
```

```math
K_{cross}^{(0)}
:=
\limsup_j{\delta_{{cross},j}^{(0)}\over g_{i(j)}^2},
\qquad
K_{extract}^{(0)}
:=
\limsup_j{\delta_{{extract},j}^{(0)}\over g_{i(j)}^2}.
```

The decomposition is admissible only if each intermediate coefficient is a
declared finite-record coefficient or a proof-coordinate coefficient pushed
back to the same finite record law. It is not a chain of hidden states.

### Theorem 8J.11B: Decomposition Bounds `K_HK^(0)` And Selects The Branch

For any admissible decomposition-first ledger,

```math
K_{HK}^{(0)}
\le
K_{time}^{(0)}+K_{block}^{(0)}+K_{cross}^{(0)}+K_{extract}^{(0)}.
```

Therefore:

1. the fixed-time branch is viable if

   ```math
   K_{time}^{(0)}+K_{block}^{(0)}
   +K_{cross}^{(0)}+K_{extract}^{(0)}
   <R_0^{crit};
   ```

2. the matched-time branch should be tested if the dominant debit is
   `K_time^(0)` and the time-shift can be absorbed into an admissible
   matched heat-kernel time;
3. the matched-time branch is proved by this decomposition only if the
   non-time residual upper budget

   ```math
   K_{block}^{(0)}+K_{cross}^{(0)}+K_{extract}^{(0)}
   ```

   leaves enough first-selector margin; an actual failure conclusion requires
   the lower-floor test of Theorem 8J.12K.

Proof.

By the triangle inequality,

```math
\left|u_{0,j}^{act}-u_{0,j}^{bare}\right|
\le
\delta_{{time},j}^{(0)}
+\delta_{{block},j}^{(0)}
+\delta_{{cross},j}^{(0)}
+\delta_{{extract},j}^{(0)}.
```

Divide by `g_i^2` and take limsup to obtain the bound on `K_HK^(0)`. The
fixed-time viability statement is the first-selector margin test with this
bound inserted. If the time-shift is the large term, the only way to avoid
charging it to the fixed-time defect is to absorb it into an admissible
matched-time reference; this is exactly the matched branch below. If the
non-time upper budget is too large, the decomposition has not proved the
branch. If the non-time lower floor itself consumes the threshold, Theorem
8J.12K gives the actual failure statement. `square`

### Definition 8J.11C: Fixed-Time Heat-Kernel Coefficient Defect

Let `u_{0,j}^{act}` be the actual normalized `rho_0` block-plaquette
coefficient extracted from the pushed-forward `SEL_0` record law at cutoff
node `i(j)`. Let the fixed Paper-16 heat-kernel reference time be `t_{i(j)}`.
Define

```math
u_{0,j}^{HK}
:=
\exp\left(-{t_{i(j)}C_0\over2}\right),
```

and

```math
\delta_{HK,j}^{(0)}
:=
\left|u_{0,j}^{act}-u_{0,j}^{HK}\right|.
```

Then

```math
K_{HK}^{(0)}
=
\limsup_j{\left|u_{0,j}^{act}
-\exp(-t_{i(j)}C_0/2)\right|\over g_{i(j)}^2}.
```

This is the fixed-time interpretation of `K_HK^(0)`: the Paper-16
heat-kernel time is not refitted to the observed coefficient.

### Theorem 8J.11D: AF-Normalized RGCE Proves `K_HK^(0)`

Assume the fixed-time AF-normalized character-domain estimate
`AF-RGCE_0(K_HK)`:

```math
\left|u_{0,j}^{act}
-\exp(-t_{i(j)}C_0/2)\right|
\le
K_{HK}g_{i(j)}^2+o(g_{i(j)}^2)
```

on the same `SEL_0` tower. Then

```math
K_{HK}^{(0)}\le K_{HK}.
```

If this bound is part of a full first-selector estimate satisfying

```math
K_{HK}+K_{proj}^{(0)}+K_{chart}^{(0)}
+K_{ct}^{(0)}+K_{vol}^{(0)}+K_{tail}^{(0)}
<R_0^{crit},
```

then the fixed-time heat-kernel reference defect is small enough for the
`SEL_0` coefficient route.

Proof.

Divide the displayed `AF-RGCE_0` estimate by `g_i^2` and take limsup. This
gives `K_HK^(0)<=K_HK`. The second claim is Theorem 8J.10F with this value
inserted in the first row of `K_0^src`. `square`

### Corollary 8J.11E: Total-Variation Version

If the actual block-plaquette marginal `nu_{P,j}^{act}` and the fixed-time
heat-kernel marginal `K_{t_{i(j)}}dU` satisfy

```math
\|\nu_{P,j}^{act}-K_{t_{i(j)}}dU\|_{TV}
\le
K_{TV}^{(0)}g_{i(j)}^2+o(g_{i(j)}^2),
```

then

```math
K_{HK}^{(0)}\le K_{TV}^{(0)}.
```

Proof.

The normalized character record `chi_{rho_0}/d_{rho_0}` has absolute value
at most one. Paper 14 Corollary 6.6 therefore bounds the coefficient
difference by the total-variation distance. Apply Theorem 8J.11D. `square`

### Theorem 8J.11F: Fixed-Time Falsification Of `K_HK^(0)`

If

```math
\limsup_j
{\left|u_{0,j}^{act}
-\exp(-t_{i(j)}C_0/2)\right|
\over g_{i(j)}^2}
=\infty,
```

then the fixed-time heat-kernel source row fails:

```math
K_{HK}^{(0)}=\infty.
```

If, more sharply,

```math
\liminf_j
{\left|u_{0,j}^{act}
-\exp(-t_{i(j)}C_0/2)\right|
\over g_{i(j)}^2}
\ge R_0^{crit},
```

then `SEL_0` fails before the other five source debits are even charged.

Proof.

The first statement is the definition of `K_HK^(0)`. For the second, all
other source constants are nonnegative, so

```math
K_0^{src}\ge K_{HK}^{(0)}\ge R_0^{crit}.
```

Thus `M_CE^(0)=R_0^crit-K_0^src<=0`, and Definition 8J.10E declares
`SEL_0` failed. `square`

### Definition 8J.11G: Matched-Time Alternative

Suppose an admissible decomposition-first ledger has been fixed and
`u_{0,j}^{time}` lies in `(0,1)` cofinally. Define the matched heat-kernel
time

```math
\tau_j^{match}
:=
-{2\over C_0}\log u_{0,j}^{time}.
```

Then

```math
u_{0,j}^{time}
=
\exp\left(-{\tau_j^{match}C_0\over2}\right),
```

so the time/scheme component of the leading-channel heat-kernel defect is
zero if the reference time is allowed to be `tau_j^match`.

This is admissible for Paper 19 only if the matched time remains in the same
AF scheme ledger:

```math
1-\chi
\le
{\tau_j^{match}\over g_{i(j)}^2}
\le
1+\chi
```

cofinally, and if all other tested character, tail, decoration, and
first-excess ledgers are still evaluated on the same matched-time
whole-process record family.

Choosing instead

```math
\tau_j^{act}:=-{2\over C_0}\log u_{0,j}^{act}
```

is not an admissible shortcut unless a source theorem proves that the
same-block, cross-block, and extraction terms are themselves pure
time/scheme shifts. Without that theorem, `tau_j^act` would hide
record-law debits inside a refitted proof coordinate.

### Theorem 8J.11H: Matched-Time Residual Branch

If the matched-time admissibility conditions of Definition 8J.11G hold, then
the time/scheme part of the leading heat-kernel defect for `rho_0` is zero:

```math
K_{time,match}^{(0)}=0.
```

The matched heat-kernel source is still bounded by the non-time residual
debits:

```math
K_{HK,match}^{(0)}
\le
K_{block}^{(0)}+K_{cross}^{(0)}+K_{extract}^{(0)}.
```

The coefficient source then passes only if the non-time heat-kernel residuals
and the remaining five source constants fit below the first-selector margin:

```math
K_{block}^{(0)}+K_{cross}^{(0)}+K_{extract}^{(0)}
+K_{proj}^{(0)}+K_{chart}^{(0)}+K_{ct}^{(0)}
+K_{vol}^{(0)}+K_{tail}^{(0)}
<R_0^{crit}.
```

This theorem does not prove the fixed-time `K_HK^(0)` is zero, and it does
not allow block, cross, or extraction errors to disappear. It proves only
that a matched-time proof coordinate can remove the time/scheme debit if the
matching itself is an admissible AF scheme choice.

Proof.

The identity defining `tau_j^match` makes the `rho_0` coefficient of the
matched heat-kernel reference equal to `u_{0,j}^{time}`. Hence the
time/scheme debit is zero. The triangle inequality gives

```math
\left|u_{0,j}^{act}
-\exp(-\tau_j^{match}C_0/2)\right|
\le
\delta_{{block},j}^{(0)}
+\delta_{{cross},j}^{(0)}
+\delta_{{extract},j}^{(0)}.
```

Divide by `g_i^2` and take limsup. The final pass condition is Theorem
8J.10F with the heat-kernel term replaced by this non-time residual bound
and with the admissibility conditions ensuring that no hidden change of
record law or regulator chart has been introduced. `square`

### Theorem 8J.11I: Present Source-Paper Verdict On `K_HK^(0)`

For the fixed Paper-16 heat-kernel time, the current source papers do not
prove and do not falsify `K_HK^(0)`.

They prove the exact alternatives:

```text
decomposition-first ledger       => K_HK^(0) <= K_time^(0)+K_block^(0)+K_cross^(0)+K_extract^(0);
AF-RGCE_0(K_HK)              => K_HK^(0) <= K_HK;
TV distance <= K_TV g_i^2    => K_HK^(0) <= K_TV;
fixed-time defect/g_i^2 -> infinity
                              => K_HK^(0) = infinity;
matched admissible time       => matched time debit is zero, residual debits remain.
```

What is missing is the actual fixed-time AF-normalized estimate

```math
\left|u_{0,j}^{act}
-\exp(-t_{i(j)}C_0/2)\right|
=O(g_{i(j)}^2)
```

with a constant small enough for the first-selector margin. Paper 14's
ordinary `RGCE` gives a heat-kernel neighborhood criterion, but unless its
distance is `O(g_i^2)` on the `SEL_0` tower it does not bound
`K_HK^(0)`. Paper 16 chooses the heat-kernel regulator and proves the finite
cutoff law, but it does not by itself prove that the interacting
block-plaquette marginal has fixed-time coefficient defect `O(g_i^2)` after
all neighboring plaquette and residual-polymer effects are charged.

Proof.

The decomposition implication is Theorem 8J.11B. The positive fixed-time
implications are Theorems 8J.11D and 8J.11E. The matched-time residual
statement is Theorem 8J.11H. The negative implication is Theorem 8J.11F. The
source papers provide neither the fixed-time AF-normalized upper bound nor a
lower bound forcing one of the failure alternatives, and they do not yet prove
that the non-time residual upper budget is strictly below the first-selector
threshold. The lower-floor falsification criterion is separated in Theorem
8J.12K. `square`

### 8J.12 Four-Constant Source Attack For `K_HK^(0)`

Section 8J.11 splits the heat-kernel defect into four debits. This section
attacks those debits directly. The point is to avoid the phrase "prove
`K_HK^(0)`" until every source of coefficient drift has a scalar record-law
bound.

### Definition 8J.12A: Four Source Envelopes

For the `SEL_0` row define four source envelopes:

```math
T_0
:=
\limsup_j
{|\tau_j^{time}-t_{i(j)}|\over g_{i(j)}^2},
```

```math
B_0
:=
\limsup_j
{{\mathcal B}_{0,j}\over g_{i(j)}^2},
\qquad
C_0^{res}
:=
\limsup_j
{{\mathcal C}_{0,j}\over g_{i(j)}^2},
\qquad
X_0
:=
\limsup_j
{{\mathcal X}_{0,j}\over g_{i(j)}^2}.
```

Here:

```text
tau_j^time  = admissible local time/scheme coefficient time;
mathcal_B   = same-block local interaction coefficient drift;
mathcal_C   = cross-block residual-polymer coefficient drift;
mathcal_X   = coefficient extraction/readout drift.
```

The envelopes are admissible only when they are evaluated on the same
finite `SEL_0` record law. A gauge-fixed covariance, local action, polymer
surface, or extraction chart may be used to estimate them, but the displayed
quantities must be scalar coefficient-record differences after pushforward
to the declared finite battery.

### Lemma 8J.12B: Time Constant

If `T_0<infty`, then

```math
K_{time}^{(0)}
\le
{C_0\over2}T_0.
```

In the matched-time branch of Definition 8J.11G, `T_0` is not charged to the
source budget; it is replaced by the admissibility condition

```math
1-\chi
\le
{\tau_j^{time}\over g_{i(j)}^2}
\le
1+\chi.
```

Proof.

For `s,t>=0`,

```math
\left|
e^{-C_0s/2}-e^{-C_0t/2}
\right|
\le
{C_0\over2}|s-t|,
```

because the derivative of `e^{-C_0t/2}` has absolute value at most `C_0/2`.
Apply this with `s=t_{i(j)}` and `t=tau_j^time`, divide by `g_i^2`, and take
limsup. The matched-time statement is just the bookkeeping convention of
Theorem 8J.11H: if the time is an admissible scheme coordinate, it is not a
physical residual debit. `square`

### Definition 8J.12C: Same-Block Coefficient Drift Gate

`HK-BLOCK-COEFF_0(B_0)` holds when the same-block local effective law and the
time-shifted heat-kernel local law obey, on the normalized `rho_0` character
record,

```math
\left|u_{0,j}^{block}-u_{0,j}^{time}\right|
\le
{\mathcal B}_{0,j},
\qquad
\limsup_j{{\mathcal B}_{0,j}\over g_{i(j)}^2}\le B_0.
```

A sufficient Paper-16 route is:

```text
local counterterm normalization fixes the rho_0 coefficient
+ strictly local same-block irrelevant tail is O(g_i^2)
+ finite block coefficient Lipschitz constant is bounded
=> HK-BLOCK-COEFF_0(B_0).
```

This gate is stronger than `HK-CT-CLOSE`. `HK-CT-CLOSE` controls locality of
counterterm tails; `HK-BLOCK-COEFF_0` also demands that the remaining local
same-block coefficient drift is no larger than order `g_i^2` on the selected
record.

### Lemma 8J.12D: Block Constant

If `HK-BLOCK-COEFF_0(B_0)` holds, then

```math
K_{block}^{(0)}\le B_0.
```

Proof.

This is the definition of `K_block^(0)` and the displayed bound in
Definition 8J.12C. `square`

### Definition 8J.12E: Cross-Block Residual Tail Gate

Let `r_j^{col}` be a collar radius around the tested block-plaquette record,
and fix a target constant `C_0^{res}>0`.
`HK-CROSS-COEFF_0(C_0^{res})` holds when all residual polymers touching the
tested record and leaving the collar contribute at most

```math
\left|u_{0,j}^{res}-u_{0,j}^{block}\right|
\le
{\mathcal C}_{0,j},
\qquad
\limsup_j{{\mathcal C}_{0,j}\over g_{i(j)}^2}
\le C_0^{res}.
```

The Paper-16 analytic branch proves this gate if it supplies a size-resolved
residual envelope with constants `A_res,mu_res,C_KP,h_KP,m,r_res` satisfying

```math
\Delta_{res}:=\mu_{res}-h_{KP}-m>0
```

and if the collar schedule obeys

```math
r_j^{col}
\ge
{1\over\Delta_{res}}
\left[
2\log {1\over g_{i(j)}}
+\log\left(
{C_{KP}A_{res}\over(1-e^{-\Delta_{res}})C_0^{res}}
\right)
\right]
```

cofinally, with `r_j^{col}` still smaller than the available block/window
separation and at least the residual-envelope starting radius `r_res`.

### Theorem 8J.12F: Residual Exponential Decay Proves The Cross Constant

Assume the Paper-16 analytic branch gives the residual polymer envelope
used in Definition 8J.12E. If the logarithmic collar schedule displayed
there is admissible, then

```math
K_{cross}^{(0)}\le C_0^{res}.
```

Proof.

The size-resolved residual envelope and the KP label-counting bound give the
standard tail estimate for polymers leaving a collar of radius `r`:

```math
\sum_{n\ge r}
C_{KP}A_{res}e^{-(\mu_{res}-h_{KP}-m)n}
\le
{C_{KP}A_{res}e^{-\Delta_{res}r}
\over
1-e^{-\Delta_{res}}}.
```

With `r=r_j^col`, the chosen schedule makes this tail at most
`C_0^{res} g_i^2`. This tail is exactly the scalar coefficient-record drift
`|u_res-u_block|` after the proof-coordinate polymers are pushed back to the
declared `SEL_0` record law. Dividing by `g_i^2` and taking limsup gives the
claim. `square`

### Definition 8J.12G: Extraction Drift Gate

`HK-EXTRACT-COEFF_0(X_0)` holds when the extraction/readout map from the
residual-corrected coefficient to the actual finite record coefficient
satisfies

```math
\left|u_{0,j}^{act}-u_{0,j}^{res}\right|
\le
{\mathcal X}_{0,j},
\qquad
\limsup_j{{\mathcal X}_{0,j}\over g_{i(j)}^2}\le X_0.
```

There are two important subroutes:

1. **Exact coefficient-readout route.** If the finite battery contains the
   normalized `rho_0` character exactly and the pushforward law is evaluated
   exactly on that record, then `mathcal_X_{0,j}=0` and `X_0=0`.
2. **Operational finite-readout route.** If binning, precision,
   loop-approximant, projective, or representation-tail readout errors
   remain, it is sufficient that their Paper-16 operational ledger has
   total effect at most `X_0 g_i^2+o(g_i^2)` on the normalized `rho_0`
   character.

### Lemma 8J.12H: Extraction Constant

If `HK-EXTRACT-COEFF_0(X_0)` holds, then

```math
K_{extract}^{(0)}\le X_0.
```

In particular, the exact coefficient-readout route gives

```math
K_{extract}^{(0)}=0.
```

Proof.

The first statement is Definition 8J.12G divided by `g_i^2` and passed to a
limsup. The exact-readout statement is the same bound with
`mathcal_X_{0,j}=0`. `square`

### Theorem 8J.12I: Four Constants Prove The Heat-Kernel Source Bound

Assume:

1. `T_0<infty`;
2. `HK-BLOCK-COEFF_0(B_0)`;
3. `HK-CROSS-COEFF_0(C_0^{res})`;
4. `HK-EXTRACT-COEFF_0(X_0)`.

Then the fixed-time heat-kernel source satisfies

```math
K_{HK}^{(0)}
\le
{C_0\over2}T_0+B_0+C_0^{res}+X_0.
```

In the matched-time branch, if Definition 8J.11G is admissible, then

```math
K_{HK,match}^{(0)}
\le
B_0+C_0^{res}+X_0.
```

Proof.

Use Lemma 8J.12B, Lemma 8J.12D, Theorem 8J.12F, and Lemma 8J.12H in the
decomposition bound of Theorem 8J.11B. In the matched-time branch the
time/scheme debit is removed by Theorem 8J.11H, leaving only the non-time
terms. `square`

### Definition 8J.12J: Non-Time Residual Budget And Lower Floor

Define the certified non-time residual upper budget

```math
K_{NT}^{up}
:=
B_0+C_0^{res}+X_0.
```

Define also the actual non-time residual lower floor

```math
K_{NT}^{low}
:=
\liminf_j
{\left|u_{0,j}^{act}-u_{0,j}^{time}\right|
\over g_{i(j)}^2}.
```

`K_NT^up` is a proof budget. `K_NT^low` is a falsification floor. They are
not interchangeable: a large upper budget means the current proof is too
weak, while a large lower floor means the matched-time branch actually fails.

### Theorem 8J.12K: Non-Time Residual Pass/Falsification Criterion

For the heat-kernel source row alone:

1. if

   ```math
   K_{NT}^{up}<R_0^{crit},
   ```

   then the matched-time heat-kernel source fits below the first-selector
   margin before the other five source constants are charged;

2. if

   ```math
   K_{NT}^{low}\ge R_0^{crit},
   ```

   then the matched-time heat-kernel source row cannot pass for `SEL_0`.

For the whole first selector in the matched-time branch, the sufficient pass
condition is the stronger inequality

```math
K_{NT}^{up}
+K_{proj}^{(0)}+K_{chart}^{(0)}+K_{ct}^{(0)}
+K_{vol}^{(0)}+K_{tail}^{(0)}
<R_0^{crit}.
```

Proof.

The first claim is Theorem 8J.12I in the matched-time branch. The second is
the definition of `K_NT^low`: if the actual scalar coefficient discrepancy
between the time-matched reference and the extracted record is already at
least `R_0^crit` in `g_i^2` units, no decomposition or cancellation inside
the proof budget can make the matched-time heat-kernel row pass. The final
claim is Theorem 8J.10F with the heat-kernel source term replaced by
`K_NT^up`. `square`

### Theorem 8J.12L: Present Source-Paper Verdict On The Four Constants

The four-constant attack is now reduced to exact source estimates:

```text
time:
  |tau_time-t_i| = O(g_i^2), or matched-time admissibility;

block:
  HK-BLOCK-COEFF_0(B_0);

cross:
  Paper-16 residual envelope + logarithmic collar schedule
  => HK-CROSS-COEFF_0(C_0^res);

extract:
  exact rho_0 coefficient readout gives X_0=0,
  otherwise operational readout drift must be O(g_i^2).
```

The strongest partial closure from current source papers is the cross term:
Paper 16's `HK-AN-CLOSE`/`HK-KP-TEST` machinery, if verified with compatible
constants and an admissible logarithmic collar, gives
`K_cross^(0)<=C_0^res`.

The remaining non-time source bottleneck is therefore:

```math
B_0+C_0^{res}+X_0<R_0^{crit}
```

for a pass, or

```math
K_{NT}^{low}\ge R_0^{crit}
```

for a falsification of the matched-time heat-kernel row. Current Papers
14--16 do not yet supply the actual `B_0`, `C_0^res`, and `X_0` values in
this `SEL_0` normalization, nor do they supply a lower floor proving failure.

Thus the proof has advanced, but it has not closed actual `K_HK^(0)`:
`K_cross` has a concrete exponential-tail route, `K_extract` can be zero in
the exact coefficient-readout route, and `K_block` is the main remaining
local same-block coefficient source.

### 8J.13 Attack On `HK-BLOCK-COEFF_0(B_0)`

The same-block gate is local, but it is not automatic. Paper 16 proves that
strictly local counterterms can be absorbed into the renormalized local
action and record normalization. For `SEL_0`, we need the sharper statement
that after the heat-kernel time direction has been absorbed into
`tau_j^time`, the remaining local coefficient drift is only order `g_i^2`
on the normalized `rho_0` record.

### Definition 8J.13A: Local Time Tangent And Transverse Block Residual

Let `f_0(U):=chi_{rho_0}(U)/d_{rho_0}` be the normalized first-selector
character record. On the one-block local record algebra, let `Phi_0` denote
the heat-kernel time tangent, defined by

```math
{d\over dt}
\exp(-tC_0/2)
=
-{C_0\over2}\exp(-tC_0/2).
```

The local same-block effective action difference is admissibly split when,
on the finite `SEL_0` battery,

```math
\Delta K_{0,j}^{loc}
=
a_{0,j}\Phi_0+R_{0,j}^{\perp}.
```

The scalar `a_{0,j}` is absorbed into the local time/scheme coefficient
`tau_j^time`. The transverse residual `R_{0,j}^\perp` is the part that is
not allowed to be hidden inside a refitted heat-kernel time.

### Definition 8J.13B: Local Coefficient Lipschitz Constant

`HK-BLOCK-LIP_0(L_0^{blk})` holds when the finite one-block coefficient map
from a local action perturbation to the normalized character coefficient is
Lipschitz on the declared local neighborhood:

```math
\left|
u_{0,j}(\Delta K)-u_{0,j}(0)
\right|
\le
L_0^{blk}\,
\|\Delta K\|_{0,loc}
```

for every local perturbation in the selected neighborhood, after the
one-block law is normalized. The norm `||.||_{0,loc}` is the finite
coefficient norm on the declared `SEL_0` local record battery.

This is a finite-dimensional statement once the local record battery,
normalization convention, and allowed coefficient neighborhood are fixed.

### Lemma 8J.13C: Lipschitz Bound For The Block Drift

If `HK-BLOCK-LIP_0(L_0^{blk})` holds and

```math
\|R_{0,j}^{\perp}\|_{0,loc}
\le
A_{0,j}^{blk},
```

then

```math
\left|u_{0,j}^{block}-u_{0,j}^{time}\right|
\le
L_0^{blk}A_{0,j}^{blk}.
```

Proof.

By Definition 8J.13A, the time-tangent piece `a_{0,j}Phi_0` is already
included in `tau_j^time`. The difference between the block coefficient and
the time-shifted coefficient is therefore caused by the transverse residual
only. Apply the finite local Lipschitz bound of Definition 8J.13B to
`Delta K=R_{0,j}^\perp`. `square`

### Definition 8J.13D: Same-Block Residual Source Ledger

`HK-BLOCK-RES_0(A_0^{blk})` holds when the transverse local residual obeys

```math
\limsup_j
{A_{0,j}^{blk}\over g_{i(j)}^2}
\le
A_0^{blk}.
```

A sufficient Paper-16 analytic source ledger is:

```text
local rho_0 time-tangent counterterm is absorbed into tau_time
+ renormalized small-field local vertices have order g_i^{2p}, p>=1
+ local irrelevant counterterm/scheme residue has order g_i^2
+ local large-field contribution on the tested block has order g_i^2
+ all constants use the same finite SEL_0 local record norm
=> HK-BLOCK-RES_0(A_0^blk).
```

More explicitly, if constants

```math
A_{sf,0},A_{ct,0},A_{sch,0},A_{lf,0}<\infty
```

satisfy

```math
\limsup_j
{A_{0,j}^{sf}+A_{0,j}^{ct}+A_{0,j}^{sch}+A_{0,j}^{lf}
\over g_{i(j)}^2}
\le
A_{sf,0}+A_{ct,0}+A_{sch,0}+A_{lf,0},
```

then one may take

```math
A_0^{blk}
=
A_{sf,0}+A_{ct,0}+A_{sch,0}+A_{lf,0}.
```

The small-field term is supplied by Paper 16's local vertex ledger only when
the selected vertex order has `p>=1`; otherwise it is not an `O(g_i^2)`
source for this coefficient gate. The large-field term is local to the
tested block and is separate from the cross-block residual tail of
Theorem 8J.12F.

### Theorem 8J.13E: Local Residual Ledger Proves `HK-BLOCK-COEFF_0`

Assume:

1. the local time tangent has been absorbed as in Definition 8J.13A;
2. `HK-BLOCK-LIP_0(L_0^{blk})`;
3. `HK-BLOCK-RES_0(A_0^{blk})`.

Then

```math
HK\text{-}BLOCK\text{-}COEFF_0(B_0)
```

holds with

```math
B_0=L_0^{blk}A_0^{blk}.
```

Consequently

```math
K_{block}^{(0)}
\le
L_0^{blk}A_0^{blk}.
```

Proof.

Lemma 8J.13C gives

```math
\left|u_{0,j}^{block}-u_{0,j}^{time}\right|
\le
L_0^{blk}A_{0,j}^{blk}.
```

Divide by `g_i^2` and take the limsup. Definition 8J.13D gives the bound
`L_0^blk A_0^blk`, which is exactly the gate `HK-BLOCK-COEFF_0(B_0)` from
Definition 8J.12C. Lemma 8J.12D then gives the final inequality for
`K_block^(0)`. `square`

### Theorem 8J.13F: Same-Block Contribution To The Non-Time Budget

Assume the hypotheses of Theorem 8J.13E, `HK-CROSS-COEFF_0(C_0^{res})`,
and `HK-EXTRACT-COEFF_0(X_0)`. Then the non-time residual budget may be
taken as

```math
K_{NT}^{up}
=
L_0^{blk}A_0^{blk}+C_0^{res}+X_0.
```

Thus the matched-time heat-kernel source row passes whenever

```math
L_0^{blk}A_0^{blk}+C_0^{res}+X_0
<R_0^{crit}.
```

Proof.

Substitute `B_0=L_0^blk A_0^blk` from Theorem 8J.13E into
Definition 8J.12J and apply Theorem 8J.12K. `square`

### Theorem 8J.13G: Present Verdict On `HK-BLOCK-COEFF_0`

`HK-BLOCK-COEFF_0(B_0)` is now reduced to a finite local renormalized-action
estimate:

```text
time tangent absorbed into tau_time
+ finite local coefficient Lipschitz constant L_0^blk
+ transverse local residual A_0^blk = O(g_i^2)
=> B_0 = L_0^blk A_0^blk.
```

Paper 16 supplies the surrounding analytic ingredients:

```text
HK-CT-CLOSE: local counterterms are absorbed and only tails remain;
HK-SF-CLOSE: local small-field vertices are controlled;
HK-LF-CLOSE: large-field events are controlled;
HK-AN-CLOSE: these constants live on one heat-kernel record tower.
```

At this stage the source papers still do not compute the `SEL_0` transverse
local constant `A_0^blk`, and they do not yet prove the local large-field
piece is `O(g_i^2)` on the tested block. The Lipschitz factor is
finite-dimensional and is closed in Section 8J.14 once the local
sup-domination constant is declared. Therefore this attack does not yet
close `B_0`; it turns it into the explicit local finite-dimensional source
problem:

```math
L_0^{blk}
\left(A_{sf,0}+A_{ct,0}+A_{sch,0}+A_{lf,0}\right)
+C_0^{res}+X_0
<R_0^{crit}.
```

If the left side is proved strictly below `R_0^crit`, the non-time
matched-time heat-kernel row passes. If a lower bound on the actual
transverse residual forces the corresponding `K_NT^low` above
`R_0^crit`, this first-selector branch is falsified.

### 8J.14 Finite-Dimensional Bound For `L_0^blk`

It remains to make `L_0^blk` concrete. This part is genuinely
finite-dimensional: the local block law has already been pushed to the
declared one-block `SEL_0` record battery, and the tested observable is the
bounded normalized character `f_0`.

### Definition 8J.14A: Local Sup-Norm Domination

Let `||.||_{0,loc}` be the finite coefficient norm on the one-block
`SEL_0` local record battery. `SUP_0(C_{sup,0})` holds when every real local
action perturbation `H` in the selected local span satisfies

```math
\|H\|_{\infty}
\le
C_{sup,0}\|H\|_{0,loc}.
```

Since the local span is finite-dimensional, such a finite `C_sup,0` exists
once the local basis, coefficient norm, and compact block configuration
space are fixed. The point of recording it is not existence; it is that the
constant must be in the same `SEL_0` normalization used by the budget
`R_0^crit`.

### Definition 8J.14B: One-Block Exponential-Tilt Coefficient Map

Let `nu_{0,j}^{time}` be the time-shifted one-block reference record law
after the time tangent has been absorbed into `tau_j^time`. For a real local
perturbation `H`, define the tilted one-block law

```math
d\nu_{0,j}^{H}
=
{e^{-H}\over Z_j(H)}\,d\nu_{0,j}^{time},
\qquad
Z_j(H):=\int e^{-H}\,d\nu_{0,j}^{time},
```

and the local coefficient map

```math
u_{0,j}(H):=\int f_0\,d\nu_{0,j}^{H}.
```

This definition is admissible only for real perturbations on the declared
finite record law. If a gauge chart, field split, or formal local action is
used to produce `H`, it must be pushed to this finite scalar record before
the tilt is evaluated.

### Lemma 8J.14C: Covariance Derivative Bound

For `H` real and `f_0` with `|f_0|<=1`,

```math
\left|{d\over ds}u_{0,j}(sH)\right|
\le
2\|H\|_{\infty}
\qquad
(0\le s\le1).
```

Proof.

Let `nu_s` be the tilted law with density proportional to `e^{-sH}`. Then

```math
{d\over ds}u_{0,j}(sH)
=
-\,{\rm Cov}_{\nu_s}(f_0,H).
```

Since `|f_0|<=1`,

```math
|{\rm Cov}_{\nu_s}(f_0,H)|
=
\left|
\int f_0(H-\nu_sH)\,d\nu_s
\right|
\le
\int |H-\nu_sH|\,d\nu_s
\le
2\|H\|_{\infty}.
```

This is a statement about the finite tilted record law, not an unrecorded
subprocess. `square`

### Theorem 8J.14D: Sup-Norm Domination Proves `HK-BLOCK-LIP_0`

If `SUP_0(C_{sup,0})` holds and the local coefficient map is the
exponential-tilt map of Definition 8J.14B, then

```math
HK\text{-}BLOCK\text{-}LIP_0(L_0^{blk})
```

holds with

```math
L_0^{blk}=2C_{sup,0}.
```

Consequently Theorem 8J.13E gives

```math
B_0\le 2C_{sup,0}A_0^{blk}.
```

Proof.

Integrate Lemma 8J.14C from `s=0` to `s=1`:

```math
|u_{0,j}(H)-u_{0,j}(0)|
\le
2\|H\|_\infty.
```

Apply `SUP_0(C_sup,0)` to obtain

```math
|u_{0,j}(H)-u_{0,j}(0)|
\le
2C_{sup,0}\|H\|_{0,loc}.
```

This is Definition 8J.13B with `L_0^blk=2C_sup,0`. The final inequality is
Theorem 8J.13E. `square`

### Corollary 8J.14E: Exact Character-Basis Bound

If the local perturbation norm is chosen so that it directly dominates
sup norm on the declared local basis,

```math
\|H\|_{\infty}\le\|H\|_{0,loc},
```

then one may take

```math
L_0^{blk}\le2,
\qquad
B_0\le2A_0^{blk}.
```

If the declared coefficient norm is the `ell^1` norm of a basis
`G_b` with `||G_b||_\infty<=M_b`, then a computable choice is

```math
C_{sup,0}:=\max_b M_b,
\qquad
L_0^{blk}\le2\max_b M_b.
```

Proof.

The first claim is Theorem 8J.14D with `C_sup,0=1`. For an `ell^1` basis
expansion `H=sum_b c_bG_b`,

```math
\|H\|_\infty
\le
\sum_b |c_b|\,\|G_b\|_\infty
\le
\left(\max_bM_b\right)\sum_b|c_b|.
```

Taking the infimum over declared expansions gives `SUP_0(max_b M_b)`, and
Theorem 8J.14D applies. `square`

### Theorem 8J.14F: Updated Non-Time Budget With Explicit `L_0^blk`

Assume `SUP_0(C_sup,0)`, `HK-BLOCK-RES_0(A_0^blk)`,
`HK-CROSS-COEFF_0(C_0^res)`, and `HK-EXTRACT-COEFF_0(X_0)`. Then the
matched-time non-time heat-kernel budget may be taken as

```math
K_{NT}^{up}
=
2C_{sup,0}A_0^{blk}+C_0^{res}+X_0.
```

Thus the heat-kernel row passes if

```math
2C_{sup,0}A_0^{blk}+C_0^{res}+X_0
<R_0^{crit}.
```

Proof.

Theorem 8J.14D gives `L_0^blk=2C_sup,0`. Substitute this into Theorem
8J.13F. `square`

### Theorem 8J.14G: Present Verdict On `L_0^blk`

`L_0^blk` is no longer an open analytic Yang-Mills constant. It is a
finite-dimensional local record-norm constant. Under the declared
exponential-tilt local law and sup-norm domination,

```text
L_0^blk <= 2 C_sup,0.
```

This closes the Lipschitz part of `HK-BLOCK-COEFF_0`. The remaining local
source is now only the transverse residual size:

```math
A_0^{blk}
=
A_{sf,0}+A_{ct,0}+A_{sch,0}+A_{lf,0}.
```

The next scalar bottleneck is therefore

```math
2C_{sup,0}
\left(A_{sf,0}+A_{ct,0}+A_{sch,0}+A_{lf,0}\right)
+C_0^{res}+X_0
<R_0^{crit}.
```

If the exact character-basis norm is chosen with `C_sup,0=1`, this becomes

```math
2\left(A_{sf,0}+A_{ct,0}+A_{sch,0}+A_{lf,0}\right)
+C_0^{res}+X_0
<R_0^{crit}.
```

The Barandes-aligned boundary is unchanged: the finite tilt and covariance
calculation are proof coordinates for one declared local record law. No
hidden local Markov process has been introduced.

### 8J.15 Local Large-Field Part Of The Transverse Residual

The remaining same-block source is

```math
A_0^{blk}
=
A_{sf,0}+A_{ct,0}+A_{sch,0}+A_{lf,0}.
```

This section isolates the large-field summand. The point is sharper than the
generic `HK-LF-CLOSE` statement of Paper 16: for the first selector row
`SEL_0`, the local large-field residual must be small in the same finite
coefficient norm used in `HK-BLOCK-RES_0`.

### Definition 8J.15A: `SEL_0` Local Large-Field Residual

Let `E_{lf,0,j}` be the record event that the tested `SEL_0` block is
large-field in the collar-refined Paper-16 decomposition, including bad
collars assigned to that block. Let

```math
R_{0,j}^{lf,\perp}
```

be the large-field contribution to the transverse local residual after the
heat-kernel time tangent has been absorbed into `tau_j^time`. Define

```math
A_{0,j}^{lf}:=\|R_{0,j}^{lf,\perp}\|_{0,loc}.
```

The local large-field source gate

```math
HK\text{-}LF\text{-}LOC_0(M_{lf,0})
```

holds when, on the same pushed-forward record law and in the same
`SEL_0` local norm,

```math
A_{0,j}^{lf}
\le
M_{lf,0}\,\mathbf{P}_i(E_{lf,0,j})
```

for all sufficiently fine nodes, with `M_lf,0<infty` independent of the
cutoff node.

This is the one-block specialization of Paper 16's `HK-LF-REP => HK-LF-DOM`:
the local residual coefficient is a bounded finite-battery insertion
supported on the declared large-field record event.

### Definition 8J.15B: Local Bad-Block Finite-Energy Gate

`HK-BFE_0(C_B,c_B,delta,t_B)` holds when the same collar-refined local
large-field event obeys

```math
\mathbf{P}_i(E_{lf,0,j})
\le
C_B\exp\left(-{c_B\delta^2\over t_i}\right)
```

for every sufficiently fine node with `t_i<=t_B`, where

```math
C_B<\infty,\qquad c_B>0,\qquad \delta>0.
```

The event `E_lf,0,j` is a record event. Thus this is not a hidden
configuration-space condition; it is an estimate inside the declared
whole-process law.

### Lemma 8J.15C: Exponential Finite-Energy Beats The `SEL_0` `g_i^2` Scale

Assume `HK-LF-LOC_0(M_lf,0)`, `HK-BFE_0(C_B,c_B,delta,t_B)`, and the
asymptotic-freedom time comparison

```math
t_i\le T_+ g_i^2
```

on a cofinal tail, with `0<T_+<infty` and `g_i\to0`. Then

```math
\limsup_j {A_{0,j}^{lf}\over g_{i(j)}^2}=0.
```

Consequently the local large-field contribution is `o(g_i^2)` in the
`SEL_0` normalization, and in the source ledger one may take

```math
A_{lf,0}=0.
```

Proof.

By the two gates,

```math
A_{0,j}^{lf}
\le
M_{lf,0}C_B
\exp\left(-{c_B\delta^2\over t_i}\right).
```

Using `t_i<=T_+g_i^2`,

```math
{A_{0,j}^{lf}\over g_i^2}
\le
M_{lf,0}C_B\,g_i^{-2}
\exp\left(-{c_B\delta^2\over T_+g_i^2}\right).
```

For every positive `a`,

```math
x^{-2}\exp(-a/x^2)\to0
\qquad (x\downarrow0).
```

Taking `x=g_i` and `a=c_B delta^2/T_+` gives the claim. `square`

### Corollary 8J.15D: Paper-16 Collar-Adapted Route To `A_lf,0=0`

Suppose the Paper-16 collar-adapted large-field branch holds locally on the
`SEL_0` block:

```text
HK-CAD(C_ad,a_ad,e_col,delta,b,t_ad)
+ heat-kernel plaquette tail constants C_H,c_H,t_H
+ size-one bad-collar assignment covered by the same local event estimate
+ local one-block HK-LF-REP constants C_lab,0,C_coef,0,C_rec,0,C_ext,0
+ c_H>a_ad
```

and the AF time comparison `t_i<=T_+g_i^2` holds on the same tower. Then
`HK-LF-LOC_0(M_lf,0)` and `HK-BFE_0(C_B,c_B,delta,t_B)` hold with

```math
M_{lf,0}
=
C_{lab,0}C_{coef,0}C_{rec,0}C_{ext,0},
```

```math
C_B=C_{ad}P_bC_H,\qquad c_B=c_H-a_{ad},
\qquad t_B=\min(t_H,t_{ad}),
```

and hence

```math
A_{lf,0}=0.
```

Proof.

Paper 16 Theorem 9H.6 gives the collar-refined good-collar bad-block
finite-energy estimate with the displayed `C_B` and `c_B`. The size-one
bad-collar assignment hypothesis says that the union event `E_lf,0,j` used
by the `SEL_0` residual is covered by that same local estimate. Thus
`HK-BFE_0` holds. Paper 16 Theorem 9I.4 gives local coefficient dominance
with the displayed one-block `M_lf,0`. Lemma 8J.15C then applies. `square`

### Theorem 8J.15E: Updated Transverse Residual Budget

Assume the hypotheses of Corollary 8J.15D and suppose the remaining local
transverse pieces satisfy

```math
\limsup_j
{A_{0,j}^{sf}\over g_i^2}
\le A_{sf,0},
\qquad
\limsup_j
{A_{0,j}^{ct}\over g_i^2}
\le A_{ct,0},
\qquad
\limsup_j
{A_{0,j}^{sch}\over g_i^2}
\le A_{sch,0}.
```

Then

```math
HK\text{-}BLOCK\text{-}RES_0(A_0^{blk})
```

holds with

```math
A_0^{blk}
\le
A_{sf,0}+A_{ct,0}+A_{sch,0}.
```

Consequently, under `SUP_0(C_sup,0)`,

```math
K_{NT}^{up}
\le
2C_{sup,0}
\left(A_{sf,0}+A_{ct,0}+A_{sch,0}\right)
+C_0^{res}+X_0.
```

The matched-time non-time heat-kernel row passes if

```math
2C_{sup,0}
\left(A_{sf,0}+A_{ct,0}+A_{sch,0}\right)
+C_0^{res}+X_0
<R_0^{crit}.
```

Proof.

Corollary 8J.15D gives `A_lf,0=0`. Add the three displayed limsup bounds
for the small-field, counterterm, and scheme parts to obtain
`HK-BLOCK-RES_0` with the stated `A_0^blk`. The non-time budget is then
Theorem 8J.14F with this sharper value of `A_0^blk`. `square`

### Theorem 8J.15F: Present Verdict On `A_lf,0`

The local large-field piece is no longer the main scalar obstruction once
the Paper-16 collar-adapted large-field branch is imported with uniform
one-block constants. The exact reduction is:

```text
local HK-LF-REP on SEL_0
+ collar-adapted HK-BFE with c_B delta^2>0
+ t_i <= T_+ g_i^2
=> A_lf,0 = 0 in the SEL_0 normalization.
```

What remains unproved by the current source papers is the actual verification
of the local input constants on the frozen `SEL_0` row:

```text
HK-CAD heat constants, finite COL-EXT_0, and 0<e_col<c_H/q_loc,
local one-block HK-LF-REP in the SEL_0 norm,
same-ledger size-one bad-collar assignment covered by HK-BFE_0,
and the AF time comparison on the selected tower.
```

If those source inputs are supplied, the same-block residual bottleneck
reduces to the non-large-field pieces:

```math
2C_{sup,0}
\left(A_{sf,0}+A_{ct,0}+A_{sch,0}\right)
+C_0^{res}+X_0
<R_0^{crit}.
```

This is Barandes-aligned for the same reason as the previous sections: the
bad-block indicator, local coefficient extractor, and collar assignment are
record-law proof coordinates. The only exported object is the normalized
finite `SEL_0` record coefficient.

### 8J.15G Actual `SEL_0` Attack On `HK-CAD`

The first remaining local large-field input is the collar-adapted denominator
margin. Paper 16 reduced it to

```text
q_loc(e_col+L_B alpha^2)<c_H.
```

This subsection makes that inequality a source-constant decision problem on
the frozen `SEL_0` row.

#### Definition 8J.15G.1: Same-Metric Heat-Kernel Constants

`HK-CAD-HEAT_0(C_H,c_H,C_loc,q_loc,t_H,t_loc,delta_0)` holds when the
same bi-invariant group metric `d_G` is used in both of the following
estimates on the pushed-forward `SEL_0` local record law:

1. the one-plaquette heat-kernel tail satisfies, for
   `0<delta<delta_0` and `t_i<=t_H`,

   ```math
   \mathbf P_i(d_G(U_p,1)\ge\delta)
   \le
   C_H\exp\left(-{c_H\delta^2\over t_i}\right);
   ```

2. the local heat-kernel lower bound satisfies, for
   `d_G(U,1)<=delta_0` and `t_i<=t_loc`,

   ```math
   K_{t_i}(U)
   \ge
   C_{loc}t_i^{-d_G/2}
   \exp\left(-{q_{loc}d_G(U,1)^2\over t_i}\right).
   ```

The constants `c_H` and `q_loc` must refer to the same normalization of the
heat-kernel time and the same metric. Otherwise the comparison has no
record-law meaning.

#### Definition 8J.15G.2: `SEL_0` Collar-Minimizer Source

`HK-CAD-MIN_0(e_col,L_B,alpha,v_B,D_B)` holds when, for every
`(e_col,delta)`-good collar of the tested `SEL_0` block, the following
finite-dimensional source data are available:

1. an interior configuration `U_*` with

   ```math
   E_B(U_*;collar)\le e_{col}\delta^2;
   ```

2. a collar-compatible neighborhood `N_alpha(U_*)` of radius `alpha delta`
   on which

   ```math
   E_B(U_{int};collar)
   \le
   (e_{col}+L_B alpha^2)\delta^2;
   ```

3. a Haar-volume lower bound

   ```math
   Vol(N_alpha(U_*))\ge v_B(alpha\delta)^{D_B}.
   ```

This is not a gauge-ontology assumption. The minimizer, chart, and
neighborhood are proof coordinates used to lower-bound a finite conditional
denominator. The exported statement is the resulting bound on the
pushed-forward `SEL_0` record law.

#### Definition 8J.15G.3: `SEL_0` CAD Margin

For a chosen collar source row define

```math
m_{CAD,0}(alpha)
:=
c_H-q_{loc}(e_{col}+L_B alpha^2),
```

and the endpoint margin

```math
m_{CAD,0}^{end}
:=
c_H-q_{loc}e_{col}.
```

The row is CAD-positive when `m_CAD,0(alpha)>0`.

#### Theorem 8J.15G.4: CAD-Positive Source Proves Local `HK-CAD`

Assume `HK-CAD-HEAT_0(C_H,c_H,C_loc,q_loc,t_H,t_loc,delta_0)` and
`HK-CAD-MIN_0(e_col,L_B,alpha,v_B,D_B)` on the same pushed-forward
`SEL_0` record law. If

```math
m_{CAD,0}(alpha)>0,
```

then the local `SEL_0` instance of Paper 16 `HK-CAD` holds. More explicitly,
choose

```math
a_{ad}
=
q_{loc}(e_{col}+L_B alpha^2)
+{1\over2}m_{CAD,0}(alpha).
```

Then

```math
q_{loc}(e_{col}+L_B alpha^2)<a_{ad}<c_H,
```

and

```math
c_H-a_{ad}={1\over2}m_{CAD,0}(alpha)>0.
```

Thus the local large-field estimate of Corollary 8J.15D has positive
finite-energy exponent

```math
c_B=c_H-a_{ad}
={1\over2}m_{CAD,0}(alpha).
```

Proof.

The two source gates are exactly the local hypotheses of Paper 16 Lemma
9H.5, with constants measured in the same heat-kernel metric. That lemma
gives `HK-CAD` for every `a_ad>q_loc(e_col+L_B alpha^2)`. The displayed
choice lies strictly between that lower bound and `c_H` precisely because
`m_CAD,0(alpha)>0`. The stated `c_B` is the Paper 16 collar margin imported
by Corollary 8J.15D. `square`

#### Corollary 8J.15G.5: Endpoint Test And Choice Of `alpha`

If

```math
e_{col}< {c_H\over q_{loc}},
```

then `alpha` can be chosen so that the local `SEL_0` `HK-CAD` margin is
positive. When `L_B>0`, it is enough to choose

```math
0<alpha<
\left({c_H/q_{loc}-e_{col}\over L_B}\right)^{1/2}.
```

When `L_B=0`, every sufficiently small admissible `alpha>0` works.

Proof.

The displayed endpoint inequality is `m_CAD,0^{end}>0`. By continuity of
`m_CAD,0(alpha)` in `alpha`, any sufficiently small positive `alpha`
preserves positivity. The explicit bound is just
`e_col+L_B alpha^2<c_H/q_loc`. `square`

#### Corollary 8J.15G.6: Heat-Kernel Ratio Form

Suppose the `SU(N)` heat-kernel estimates are used with a common Gaussian
rate `kappa_H>0`, in the sense that for any fixed slack `eta>0` and
sufficiently small `delta_0,t_H,t_loc` the same metric gives

```math
c_H=kappa_H-eta,
\qquad
q_{loc}=kappa_H+eta.
```

Then the endpoint CAD test becomes

```math
e_{col}< {kappa_H-eta\over kappa_H+eta}.
```

Consequently, in the sharp heat-kernel limit `eta downarrow 0`, the
collar-minimizer route can only hope to close when the good-collar energy
loss is strictly below one heat-kernel unit:

```math
e_{col}<1
```

in this common normalization.

Proof.

Substitute the displayed values into Corollary 8J.15G.5. The limiting
statement is the ratio limit as `eta downarrow 0`. `square`

#### Theorem 8J.15G.7: CAD Falsifier For The Local-Minimizer Route

The local-minimizer route to `LF-IMP_0` fails on the frozen `SEL_0` row if
every admissible collar-minimizer source satisfies

```math
q_{loc}(e_{col}+L_B alpha^2)\ge c_H.
```

In particular, if the best possible good-collar energy floor obeys

```math
e_{col}^{best}\ge {c_H\over q_{loc}},
```

then no choice of `alpha` in this route can certify `c_H>a_ad`.

Proof.

Paper 16 Lemma 9H.5 requires
`a_ad>q_loc(e_col+L_B alpha^2)`. Under the displayed obstruction every
admissible `a_ad` is at least `c_H` after the strict lower-bound slack is
included. Hence the positive collar margin required in Corollary 8J.15D
cannot be obtained by this route. The endpoint statement follows because
`L_B alpha^2>=0`. `square`

#### Status 8J.15G.8

The `SEL_0` CAD problem is now exact:

```text
prove e_col < c_H/q_loc,
then choose alpha and a_ad;
or prove e_col^best >= c_H/q_loc,
and this local-minimizer CAD route fails.
```

Current Papers 14--16 give the abstract heat-kernel and collar machinery,
but they do not yet compute the actual `SEL_0` collar-extension constant
needed to charge the complement of the chosen good-collar threshold. Thus
this step is not unconditionally closed. The next subsection replaces the
raw `e_col^{best}` language by the correct finite extension/charge problem.

### 8J.15H Collar Floor Versus Bad-Collar Charge

There is one important refinement. Since Paper 16 defines a collar to be
`(e_col,delta)`-good by the inequality

```math
E_B^*(collar)\le e_{col}\delta^2,
```

one should not treat `e_col` as a mysterious global floor over all collars.
The proof is allowed to choose a stricter good-collar threshold, provided
the complement is honestly charged to the large-field record event. Thus the
actual source problem has two coupled pieces:

```text
choose e_col<c_H/q_loc for the good-collar denominator;
prove bad collars are rare enough, on the same record law.
```

This subsection makes that coupling explicit.

#### Definition 8J.15H.1: Collar Energy And Extension Source

Let `P_{\partial B}` be the finite set of collar plaquettes used by the
`SEL_0` block template, and define

```math
E_{\partial B}(collar)
:=
\sum_{p\in P_{\partial B}}d_G(U_p(collar),1)^2.
```

`COL-EXT_0(\Lambda_{\partial},\delta_{\partial})` holds when, in the same
finite axial-tree block/collar chart used for `SEL_0`, every collar with
`E_{\partial B}(collar)\le\delta_{\partial}^2` admits an interior filling
whose block ground energy obeys

```math
E_B^*(collar)\le
\Lambda_{\partial}E_{\partial B}(collar).
```

Here `\Lambda_{\partial}<infty` is a finite block-template constant. It is a
proof-coordinate constant: it depends on the finite chart and block/collar
template, but the event `E_{\partial B}` and the conclusion are statements
about the pushed-forward local record law.

#### Lemma 8J.15H.2: Finite Axial-Tree Fill Reduces `COL-EXT_0`

`COL-EXT_0(\Lambda_{\partial},\delta_{\partial})` follows if the chosen
`SEL_0` axial-tree chart has:

1. a bounded linear right inverse `R_{\partial}` for the linearized
   collar-to-interior curvature map on the finite block template;
2. a BCH remainder bound `B_{\partial}` on the chart ball of radius
   `\delta_{\partial}`;
3. `\delta_{\partial}` small enough that the nonlinear remainder is absorbed
   into the linear fill estimate.

In that case one may take, for example,

```math
\Lambda_{\partial}
=
4\|R_{\partial}\|^2(1+B_{\partial})^2
```

after decreasing `\delta_{\partial}` if necessary.

Proof.

The block/collar template is finite. In axial-tree coordinates the local
plaquette map is smooth near the identity. Its differential is the finite
linearized curvature map. A bounded right inverse gives a linear interior
fill with norm at most `\|R_{\partial}\|` times the collar curvature norm.
The BCH expansion writes the nonlinear plaquette map as this linear map plus
a quadratic remainder bounded by `B_{\partial}` on a sufficiently small
chart ball. Choosing `\delta_{\partial}` small lets the quadratic term be
absorbed by the standard contraction/implicit-function estimate. Squaring
the resulting norm bound gives the displayed `\Lambda_{\partial}`. `square`

#### Lemma 8J.15H.3: Bad-Collar Charge From Extension

Assume `COL-EXT_0(\Lambda_{\partial},\delta_{\partial})`. Fix
`0<e_col<c_H/q_loc` and choose `delta` small enough that

```math
{e_{col}\delta^2\over \Lambda_{\partial}}\le \delta_{\partial}^2.
```

If a collar is not `(e_col,delta)`-good, then

```math
E_{\partial B}(collar)>
{e_{col}\delta^2\over \Lambda_{\partial}}.
```

Consequently, with `P_{\partial}:=|P_{\partial B}|`, the bad-collar event is
contained in the finite union

```math
\bigcup_{p\in P_{\partial B}}
\left\{
d_G(U_p,1)^2
\ge
{e_{col}\delta^2\over \Lambda_{\partial}P_{\partial}}
\right\}.
```

Proof.

If `E_{\partial B}(collar)<=e_col delta^2/Lambda_{\partial}`, then
`COL-EXT_0` gives

```math
E_B^*(collar)\le e_{col}\delta^2,
```

so the collar is `(e_col,delta)`-good. The contrapositive gives the first
claim. The finite-union claim is the elementary implication that if a sum of
`P_{\partial}` nonnegative terms is larger than
`e_col delta^2/Lambda_{\partial}`, at least one term is at least the average.
`square`

#### Theorem 8J.15H.4: `COL-EXT_0` Closes The Bad-Collar Half Of CAD

Assume:

1. `HK-CAD-HEAT_0(C_H,c_H,C_loc,q_loc,t_H,t_loc,delta_0)`;
2. `COL-EXT_0(\Lambda_{\partial},\delta_{\partial})`;
3. `0<e_col<c_H/q_loc`.

Choose `alpha` and `a_ad` as in Corollary 8J.15G.5, so that

```math
c_{good}:=c_H-a_{ad}>0.
```

Then the local large-field event coming from either a good-collar bad block
or a bad collar has a positive finite-energy exponent. More precisely, for
sufficiently small `delta` and all sufficiently fine heat-kernel nodes,

```math
\mathbf P_i(E_{lf,0,j})
\le
C_{lf,0}^{CAD}
\exp\left(
-{c_{lf,0}^{CAD}\delta^2\over t_i}
\right),
```

with

```math
c_{lf,0}^{CAD}
=
\min\left\{
c_{good},
{c_H e_{col}\over \Lambda_{\partial}P_{\partial}}
\right\}
>0.
```

One may take

```math
C_{lf,0}^{CAD}
=
C_{ad}P_bC_H+P_{\partial}C_H
```

after shrinking the common small-distance and time thresholds.

Proof.

For good collars, Paper 16 Theorem 9H.6 gives the good-collar bad-block
estimate with exponent `c_good=c_H-a_ad` and prefactor `C_ad P_b C_H`.
For bad collars, Lemma 8J.15H.3 covers the bad-collar event by
`P_{\partial}` one-plaquette tail events at threshold
`sqrt(e_col/(Lambda_{\partial}P_{\partial})) delta`. The same-metric
heat-kernel tail then gives exponent
`c_H e_col/(Lambda_{\partial}P_{\partial})` and prefactor
`P_{\partial}C_H`. Adding the two estimates and taking the smaller exponent
gives the displayed bound. `square`

#### Corollary 8J.15H.5: Corrected Step-2 Pass Criterion

The local `SEL_0` CAD part of `LF-IMP_0` is proved if the following finite
source data are supplied on the same pushed-forward record law:

```text
HK-CAD-HEAT_0(C_H,c_H,C_loc,q_loc,t_H,t_loc,delta_0)
+ COL-EXT_0(Lambda_partial,delta_partial)
+ choose 0<e_col<c_H/q_loc
+ choose alpha,a_ad with q_loc(e_col+L_B alpha^2)<a_ad<c_H.
```

The resulting local large-field exponent is

```math
c_{lf,0}^{CAD}
=
\min\left\{
c_H-a_{ad},
{c_H e_{col}\over \Lambda_{\partial}P_{\partial}}
\right\}
>0.
```

Thus the raw collar-floor question has been replaced by a sharper and more
honest finite source problem: prove a finite collar extension constant
`\Lambda_{\partial}`, then choose the good-collar threshold below
`c_H/q_loc`.

#### Theorem 8J.15H.6: Corrected Falsifiers

This CAD route fails if either:

1. no same-metric heat-kernel constants can be fixed, so `c_H/q_loc` is not a
   meaningful record-law ratio;
2. the finite axial-tree fill has no bounded right inverse on the declared
   `SEL_0` block/collar template;
3. the nonlinear BCH remainder cannot be controlled on any uniform
   collar-neighborhood chart;
4. every admissible good-collar threshold compatible with the bad-collar
   charge satisfies `e_col>=c_H/q_loc`;
5. the required `alpha` neighborhood is empty after the finite volume lower
   bound and chart-domain constraints are imposed.

These are mathematical falsifiers of the local-minimizer CAD route, not
ontological statements about hidden gauge variables. The only exported
question is whether the pushed-forward finite record law admits the displayed
positive exponent.

#### Status 8J.15H.7

Step 2 is now sharpened. We do not need a mystical global
`e_col^{best}` over all collars. We need:

```text
1. a finite same-metric heat-kernel ratio c_H/q_loc;
2. a finite collar extension constant Lambda_partial;
3. a threshold 0<e_col<c_H/q_loc;
4. small alpha and a_ad with q_loc(e_col+L_B alpha^2)<a_ad<c_H.
```

If these hold, the bad-collar complement is charged with positive exponent
and the local CAD input for `LF-IMP_0` is proved. The remaining large-field
input is then `HK-LF-REP-SRC` on the same `SEL_0` record law.

### 8J.15I Construction Of `COL-EXT_0` For The `SEL_0` Template

We now prove the finite collar-extension input used above for the actual
`SEL_0` block/collar template. The construction is entirely finite
dimensional. The axial-tree chart is a proof coordinate; the resulting
constant is a constant of the pushed-forward local record law.

#### Definition 8J.15I.1: Linearized `SEL_0` Collar Complex

Fix the finite hypercubic `SEL_0` block/collar template and its strict
axial-tree link chart. Let

```math
C_{int}^1,\qquad C_B^2,\qquad C_{\partial B}^2
```

be the finite real Hilbert spaces of Lie-algebra-valued interior link
coordinates, block plaquette coordinates, and collar plaquette coordinates,
with the norms induced by the chosen bi-invariant metric on `SU(N)`.

Let

```math
d_{int}:C_{int}^1\to C_B^2
```

be the linearized plaquette map for interior links, and let

```math
i_{\partial}:C_{\partial B}^2\to C_B^2
```

be the linear injection recording how collar plaquette curvatures enter the
block plaquette list. Let

```math
Z_{\partial}^2\subset C_{\partial B}^2
```

be the finite-dimensional subspace satisfying the linearized collar Bianchi
constraints inherited from the actual block/collar template.

#### Lemma 8J.15I.2: Bounded Axial-Tree Right Inverse

For the finite rectangular `SEL_0` block/collar template there is a bounded
linear map

```math
R_{\partial}:Z_{\partial}^2\to C_{int}^1
```

such that

```math
d_{int}R_{\partial}\omega
=
-i_{\partial}\omega
```

on the block plaquettes affected by the collar source, with no uncancelled
linear interior curvature on the tested block. In particular

```math
C_R:=\|R_{\partial}\|<\infty.
```

Proof.

The `SEL_0` block/collar template is a finite contractible rectangular cell
complex. In strict axial-tree gauge, the remaining link variables are
coordinates on the finite relative one-cochain space. The linearized
plaquette map is the cellular coboundary restricted to this finite
relative complex. Contractibility gives the finite cochain homotopy

```math
d h+h d=I
```

on relative two-cochains. Restricting `h` to the admissible collar subspace
and changing sign gives the required right inverse:

```math
R_{\partial}:=-h\,i_{\partial}.
```

Equivalently, one may order plaquettes by the axial-tree peeling order and
solve the triangular linear system by back-substitution. Since the template
has finitely many links and plaquettes, the operator norm of this
back-substitution map is finite. `square`

#### Lemma 8J.15I.3: BCH Remainder And Linear Bianchi Defect

There are finite constants

```math
C_Z,\qquad B_{BCH},\qquad B_{Bi},\qquad C_{log},\qquad C_E
```

and a radius `delta_BCH>0` with the following properties for every actual
collar record with `E_{\partial B}(collar)<=delta_BCH^2`.

Let `\Omega_{\partial}` be the vector of collar plaquette logarithms in the
axial-tree chart, and let `\Pi_Z` be any fixed orthogonal projection onto
`Z_{\partial}^2`. Then:

1. the logarithmic coordinates are comparable to record energy:

   ```math
   \|\Omega_{\partial}\|^2
   \le
   C_{log}E_{\partial B}(collar);
   ```

2. the exact nonabelian Bianchi identities imply a quadratic linear-Bianchi
   defect:

   ```math
   \|\Omega_{\partial}-\Pi_Z\Omega_{\partial}\|
   \le
   B_{Bi}\|\Omega_{\partial}\|^2;
   ```

3. for the interior fill

   ```math
   A_{int}:=R_{\partial}\Pi_Z\Omega_{\partial},
   ```

   the block plaquette logarithm vector satisfies

   ```math
   \|F_B(A_{int},\Omega_{\partial})\|
   \le
   C_{rem}\|\Omega_{\partial}\|^2,
   ```

   where one may take

   ```math
   C_{rem}
   :=
   B_{Bi}
   +B_{BCH}\left(1+C_R C_Z\right)^2,
   \qquad
   C_Z:=\|\Pi_Z\|.
   ```

4. block energy is bounded by plaquette logarithms:

   ```math
   E_B(A_{int};collar)
   \le
   C_E\|F_B(A_{int},\Omega_{\partial})\|^2.
   ```

Proof.

All maps are smooth maps between finite-dimensional normed spaces on a
fixed chart ball. The logarithm-distance comparison gives item 1 after
shrinking the chart radius. The collar record comes from actual link
variables, hence satisfies the exact nonabelian lattice Bianchi identities.
Expanding these identities by BCH gives the linearized Bianchi identity plus
a quadratic remainder; projecting to the linear Bianchi subspace gives item
2 with a finite constant.

For item 3, write the block plaquette logarithm expansion as

```math
F_B(A,\Omega)
=
d_{int}A+i_{\partial}\Omega+\mathcal R_{BCH}(A,\Omega),
```

with

```math
\|\mathcal R_{BCH}(A,\Omega)\|
\le
B_{BCH}(\|A\|+\|\Omega\|)^2
```

on the chart ball. With `A=R_{\partial}\Pi_Z\Omega`, the linear part equals

```math
d_{int}R_{\partial}\Pi_Z\Omega+i_{\partial}\Omega
=
i_{\partial}(\Omega-\Pi_Z\Omega),
```

which is bounded by item 2 after absorbing the finite norm of
`i_{\partial}` into `B_{Bi}`. The BCH term is bounded by
`B_BCH(1+C_R C_Z)^2\|\Omega\|^2`. This proves item 3. Item 4 is another
finite chart comparison between group distance squared and plaquette
logarithm norm squared. `square`

#### Theorem 8J.15I.4: Actual `SEL_0` Template Proves `COL-EXT_0`

For the strict axial-tree `SEL_0` block/collar template,
`COL-EXT_0(\Lambda_{\partial},\delta_{\partial})` holds for every

```math
0<\delta_{\partial}\le\delta_{BCH}
```

with, for example,

```math
\Lambda_{\partial}
=
C_E C_{rem}^2 C_{log}^2\delta_{\partial}^2.
```

Proof.

Let an actual collar satisfy
`E_{\partial B}(collar)<=\delta_{\partial}^2`. Use the interior fill

```math
A_{int}=R_{\partial}\Pi_Z\Omega_{\partial}
```

from Lemma 8J.15I.3. Then

```math
E_B(A_{int};collar)
\le
C_E C_{rem}^2\|\Omega_{\partial}\|^4.
```

By the logarithmic comparison,

```math
\|\Omega_{\partial}\|^2
\le
C_{log}E_{\partial B}(collar)
\le
C_{log}\delta_{\partial}^2.
```

Therefore

```math
E_B(A_{int};collar)
\le
C_E C_{rem}^2 C_{log}^2\delta_{\partial}^2
E_{\partial B}(collar)
=
\Lambda_{\partial}E_{\partial B}(collar).
```

This is Definition 8J.15H.1. `square`

#### Corollary 8J.15I.5: CAD Source After The Constructed Extension

Combining Theorem 8J.15I.4 with Corollary 8J.15H.5, the local `SEL_0`
CAD input is proved once the same-metric heat-kernel constants are fixed and
one chooses

```math
0<e_{col}< {c_H\over q_{loc}},
```

then `alpha,a_ad` with

```math
q_{loc}(e_{col}+L_B alpha^2)<a_{ad}<c_H.
```

The bad-collar contribution is charged with exponent

```math
{c_H e_{col}\over \Lambda_{\partial}P_{\partial}},
```

where `\Lambda_{\partial}` is the explicit finite constant of Theorem
8J.15I.4. Hence `COL-EXT_0` is no longer an open gate for the actual
`SEL_0` template; the remaining local large-field source gate is the finite
coefficient representation `HK-LF-REP-SRC` on the same record law.

### 8J.15J Complete Local CAD Source Row

We now close the remaining CAD source constants: the same-metric heat-kernel
constants, the good-collar minimizer-neighborhood constants, and the scalar
choice of `e_col,alpha,a_ad`.

#### Lemma 8J.15J.1: Same-Metric Heat Constants Are Imported

For the heat-kernel trajectory used in Paper 16 and the same bi-invariant
metric used in the `SEL_0` record law, `HK-CAD-HEAT_0` holds on a cofinal
tail. More explicitly, for any fixed heat-kernel slack `eta_H>0` below the
Gaussian rate, one may choose finite constants

```math
C_H,\quad c_H>0,\quad C_{loc},\quad q_{loc}<\infty,
\quad t_H,\quad t_{loc},\quad \delta_0>0
```

such that Definition 8J.15G.1 holds.

Proof.

Paper 16 fixes one heat-kernel trajectory and one bi-invariant group metric
for both the one-plaquette tail estimate and the local heat-kernel lower
bound. The small-time heat-kernel parametrix on compact `SU(N)` gives a
Gaussian upper tail and a Gaussian lower bound on a common normal
neighborhood of the identity, with finite prefactors and arbitrarily small
slack in the exponent after shrinking `t_H,t_loc,delta_0`. Pulling these
estimates through the finite `SEL_0` record map does not change the metric
normalization; it only restricts the estimates to the declared finite
record events. Thus `HK-CAD-HEAT_0` holds. `square`

#### Lemma 8J.15J.2: Good-Collar Neighborhood Constants Are Finite

For the strict axial-tree `SEL_0` block/collar template, there are finite
constants

```math
L_B<\infty,\qquad v_B>0,\qquad D_B<\infty
```

such that `HK-CAD-MIN_0(e_col,L_B,alpha,v_B,D_B)` holds for every
`0<e_col<c_H/q_loc` and all sufficiently small `alpha,delta`.

Proof.

Fix a good collar. By definition
`E_B^*(collar)<=e_col delta^2`. The interior link space of the finite block
template is compact, and `E_B(\cdot;collar)` is continuous, so the infimum
is attained by some `U_*` after replacing `e_col` by an arbitrarily small
strict slack if needed.

In the strict axial-tree chart, the plaquette map is smooth on a fixed
finite-dimensional chart ball. Its first derivative is bounded on that ball.
Therefore the energy increase from moving a distance `alpha delta` from
`U_*` is bounded by `L_B alpha^2 delta^2` after shrinking the chart ball.
The constant `L_B` is finite because the template has finitely many links
and plaquettes.

Finally, Haar measure in a finite-dimensional compact Lie group is comparable
to Euclidean volume in normal coordinates on sufficiently small balls. Hence
the neighborhood of radius `alpha delta` has volume at least
`v_B(alpha delta)^{D_B}` for finite `D_B` and positive `v_B`, uniformly over
the finite block/collar chart family. These are exactly the clauses of
`HK-CAD-MIN_0`. `square`

#### Theorem 8J.15J.3: Explicit Local CAD Parameter Choice

Assume the same-metric heat constants of Lemma 8J.15J.1 and the finite
neighborhood constants of Lemma 8J.15J.2. Choose

```math
e_{col}:={c_H\over4q_{loc}}.
```

If `L_B>0`, choose `alpha>0` with

```math
L_B alpha^2\le {c_H\over4q_{loc}}.
```

If `L_B=0`, choose any sufficiently small admissible `alpha>0`. Set

```math
a_{ad}:={3c_H\over4}.
```

Then the local `SEL_0` CAD margin is positive:

```math
q_{loc}(e_{col}+L_B alpha^2)\le {c_H\over2}<a_{ad}<c_H,
```

and

```math
c_{good}:=c_H-a_{ad}={c_H\over4}.
```

After choosing `delta` small enough that

```math
{e_{col}\delta^2\over\Lambda_{\partial}}\le\delta_{\partial}^2
```

and `delta<delta_0`, the full local CAD/bad-collar exponent is

```math
c_{lf,0}^{CAD}
=
\min\left\{
{c_H\over4},
{c_H^2\over4q_{loc}\Lambda_{\partial}P_{\partial}}
\right\}
>0.
```

Proof.

The first displayed choice gives `q_loc e_col=c_H/4`. The choice of `alpha`
gives `q_loc L_B alpha^2<=c_H/4`, hence the denominator exponent from
Lemma 8J.15G.4 is at most `c_H/2`. The chosen `a_ad=3c_H/4` lies strictly
between this value and `c_H`, so `c_good=c_H/4`. The bad-collar exponent is
Theorem 8J.15H.4 with `e_col=c_H/(4q_loc)`. `square`

#### Corollary 8J.15J.4: Local CAD Is Closed For `SEL_0`

On the actual strict axial-tree `SEL_0` block/collar template, the local
CAD part of `LF-IMP_0` is closed with the constants of Theorem 8J.15J.3.
The remaining large-field input is no longer CAD; it is the finite local
coefficient representation and the event-support bookkeeping.

### 8J.15K Local `HK-LF-REP-SRC` On `SEL_0`

We now prove the finite local representation source needed for the local
large-field residual coefficient.

#### Definition 8J.15K.1: `SEL_0` Large-Field Representation Ledger

Let `I_{lf,0}` be the finite list of labels obtained by expanding the local
`SEL_0` block/collar large-field partition, including:

1. the bad interior-plaquette or bad-collar trigger label;
2. the finite chart/collar cell label;
3. the finite local counterterm or normalization label;
4. the finite `rho_0` record insertion label;
5. the finite transverse coefficient-extractor label.

Define

```math
N_{lf,0}:=|I_{lf,0}|.
```

Let `J_{lf,0}` be the maximum absolute scalar chart/Jacobian/partition
coefficient over this finite list, `R_{lf,0}` the maximum sup norm of the
finite record insertions, and `E_{lf,0}` the maximum operator norm of the
transverse coefficient extractors in the `SEL_0` local norm.

`HK-LF-REP-SRC_0(N_{lf,0},J_{lf,0},R_{lf,0},E_{lf,0})` holds when the local
large-field residual has the finite representation

```math
R_{0,j}^{lf,\perp}
=
\sum_{\lambda\in I_{lf,0}}
c_{\lambda,j}\,
L_{\lambda,j}
\left[
\mathbf 1_{E_{lf,0,j}}F_{\lambda,j}
\right],
```

where

```math
|c_{\lambda,j}|\le J_{lf,0},\qquad
\|F_{\lambda,j}\|_{\infty}\le R_{lf,0},\qquad
\|L_{\lambda,j}\|_{0,loc}\le E_{lf,0}.
```

Every object in this display is a function or linear functional of the same
pushed-forward finite `SEL_0` record law.

#### Lemma 8J.15K.2: The Local Ledger Constants Are Finite

For the strict axial-tree `SEL_0` block/collar template,
`N_{lf,0},J_{lf,0},R_{lf,0},E_{lf,0}` are finite.

Proof.

The block template, collar template, chart atlas, local partition, `rho_0`
battery, and transverse readout are all finite by the definition of the
frozen `SEL_0` row. The partition factors are bounded by construction, the
strict axial-tree chart has finite Jacobian bounds on the selected chart
cells, and the local counterterm/normalization labels are finite in the
declared source ledger. The record battery is finite, so every insertion has
finite sup norm. The coefficient space is finite-dimensional, so every
extractor norm is finite. Taking maxima over the finite list gives the four
constants. `square`

#### Theorem 8J.15K.3: Local `HK-LF-REP-SRC` Proves `HK-LF-LOC_0`

If `HK-LF-REP-SRC_0(N_{lf,0},J_{lf,0},R_{lf,0},E_{lf,0})` holds, then
`HK-LF-LOC_0(M_{lf,0})` holds with

```math
M_{lf,0}
=
N_{lf,0}J_{lf,0}R_{lf,0}E_{lf,0}.
```

Proof.

Using the finite representation and positivity of the pushed-forward record
law,

```math
\|R_{0,j}^{lf,\perp}\|_{0,loc}
\le
\sum_{\lambda\in I_{lf,0}}
|c_{\lambda,j}|\,
\|L_{\lambda,j}\|_{0,loc}\,
\|F_{\lambda,j}\|_{\infty}\,
\mathbf P_i(E_{lf,0,j}).
```

The four finite bounds give the displayed `M_lf,0`. This is Definition
8J.15A. `square`

#### Theorem 8J.15K.4: Actual `SEL_0` Template Proves Local `HK-LF-REP-SRC`

The strict axial-tree, finite-battery `SEL_0` block/collar template proves
`HK-LF-REP-SRC_0(N_{lf,0},J_{lf,0},R_{lf,0},E_{lf,0})` with the constants of
Definition 8J.15K.1.

Proof.

Expand the local large-field residual by the declared finite block/collar
partition. Each summand carries a trigger label because the residual is the
large-field part, hence it is multiplied by the local event
`E_{lf,0,j}`. The remaining scalar chart, Jacobian, counterterm,
normalization, record-insertion, and extractor factors are exactly the
finite labels listed in Definition 8J.15K.1. Lemma 8J.15K.2 gives finite
uniform maxima. Therefore the displayed representation and bounds hold.
`square`

### 8J.15L Size-One Bad-Collar Coverage

The last local large-field bookkeeping point is support: the event used in
the coefficient representation must be the same event used in the
finite-energy estimate.

#### Definition 8J.15L.1: Size-One Collar Coverage `BC-COV_0`

`BC-COV_0` holds when every bad collar sharing a boundary plaquette with the
tested `SEL_0` block is assigned by the Paper-16 collar map either to the
tested block itself or to one of the finitely many adjacent size-one local
large-field blocks included in `E_{lf,0,j}`.

#### Lemma 8J.15L.2: The Declared Collar Map Gives `BC-COV_0`

For the `SEL_0` local block/collar template, the declared nearest-block
collar assignment gives `BC-COV_0`.

Proof.

The collar assignment is a deterministic finite map on the block/collar
record. A bad collar touching the tested block has finite graph distance
zero or one from the tested block. The local event `E_lf,0,j` was defined in
Definition 8J.15A to include large-field records in the tested block and bad
collars assigned to that block in the collar-refined Paper-16 decomposition.
Enlarging the size-one local event by the finitely many adjacent assignments
does not change the one-block norm by more than a finite factor, already
absorbed into `N_lf,0`. Hence every such bad collar is supported on the same
event used in the local representation. `square`

### 8J.15M Full Local Large-Field Import Closure

We can now assemble the whole local large-field route.

#### Theorem 8J.15M.1: `LF-IMP_0` Is Proved On The `SEL_0` Row

For the strict axial-tree, finite-battery `SEL_0` row, assume the AF time
comparison

```math
t_i\le T_+g_i^2
```

on the selected cofinal tail. Then `LF-IMP_0` holds. More explicitly,

```math
A_{lf,0}=0.
```

Proof.

Lemma 8J.15J.1 gives the same-metric heat constants. Lemma 8J.15J.2 gives
the good-collar minimizer-neighborhood constants. Theorem 8J.15I.4 gives
`COL-EXT_0`, and Theorem 8J.15J.3 chooses
`e_col,alpha,a_ad` with a positive local CAD/bad-collar exponent. Thus the
local finite-energy estimate `HK-BFE_0` holds with a positive exponent.

Theorem 8J.15K.4 gives the local finite representation source, and Theorem
8J.15K.3 gives `HK-LF-LOC_0(M_lf,0)`. Lemma 8J.15L.2 gives the size-one
bad-collar coverage, so the event used by `HK-LF-LOC_0` is the same event
bounded by the finite-energy estimate. Finally Lemma 8J.15C applies with
`t_i<=T_+g_i^2`, giving `A_lf,0=0`. `square`

#### Corollary 8J.15M.2: Large-Field Is Closed For The Same-Block Budget

In the `SEL_0` same-block residual budget, the large-field source debit is
zero:

```math
A_{0}^{blk}
\le
A_{sf,0}+A_{ct,0}+A_{sch,0}.
```

The next non-large-field work is exactly the scalar budget already isolated
in Theorem 8J.16I.

### 8J.16 Small-Field, Counterterm, And Scheme Parts Of `A_0^blk`

Section 8J.15 removes the local large-field term once the local Paper-16
large-field imports are verified. The same-block problem is therefore:

```math
A_0^{blk}
\le
A_{sf,0}+A_{ct,0}+A_{sch,0}.
```

This section gives the exact local gates for the remaining three terms and
then reassembles the `SEL_0` same-block pass theorem.

### Definition 8J.16A: Local Large-Field Import Certificate `LF-IMP_0`

`LF-IMP_0` holds when all hypotheses of Corollary 8J.15D are verified on the
frozen `SEL_0` row:

```text
local HK-CAD with COL-EXT_0, e_col<c_H/q_loc, and c_H>a_ad
+ local one-block HK-LF-REP in the SEL_0 norm
+ size-one bad-collar event estimate inside HK-BFE_0
+ t_i <= T_+ g_i^2 on the selected AF tail.
```

For the strict axial-tree finite-battery `SEL_0` row, Theorem 8J.15M.1
proves this certificate once the AF time comparison is imposed. By
Corollary 8J.15D,

```math
LF\text{-}IMP_0
\quad\Longrightarrow\quad
A_{lf,0}=0.
```

This is the completed form of step 1 for the same-block residual ledger.

### Definition 8J.16B: Local Small-Field Transverse Expansion `SF-TRANS_0`

Let

```math
R_{0,j}^{sf,\perp}
```

be the small-field contribution to the transverse local residual after the
time tangent has been absorbed. `SF-TRANS_0(I_{sf},C_{sf,a},p_{sf,a})` holds
when there is a finite local expansion on the `SEL_0` battery

```math
R_{0,j}^{sf,\perp}
=
\sum_{a\in I_{sf}} g_i^{2p_{sf,a}}V_{sf,a,j}^{\perp}
+Q_{sf,j},
```

with

```math
\|V_{sf,a,j}^{\perp}\|_{0,loc}\le C_{sf,a},
\qquad
\|Q_{sf,j}\|_{0,loc}=o(g_i^2),
```

and

```math
p_{sf,a}\ge1
\qquad (a\in I_{sf}).
```

The finite set `I_sf` is the `SEL_0` local vertex list after the declared
counterterms and the heat-kernel time tangent have been removed. Gauge-fixed
small-field covariance and local vertices are proof coordinates only; the
displayed norm is a norm of pushed-forward local record coefficients.

Define the small-field debit

```math
A_{sf,0}^{src}
:=
\sum_{a\in I_{sf}:p_{sf,a}=1} C_{sf,a}.
```

Vertices with `p_sf,a>1` are higher order in the `g_i^2` normalization and
do not contribute to `A_sf,0`.

### Lemma 8J.16C: `SF-TRANS_0` Proves The Small-Field Debit

If `SF-TRANS_0` holds, then

```math
\limsup_j
{\|R_{0,j}^{sf,\perp}\|_{0,loc}\over g_i^2}
\le
A_{sf,0}^{src}.
```

Thus one may take

```math
A_{sf,0}=A_{sf,0}^{src}.
```

If any transverse local small-field vertex has `p_sf,a<1`, this `SEL_0`
same-block route fails unless that vertex is reabsorbed into the declared
local time/scheme coordinates or canceled by an explicit counterterm.

Proof.

Divide the expansion in Definition 8J.16B by `g_i^2`. Terms with `p_sf,a=1`
contribute at most `C_sf,a`. Terms with `p_sf,a>1` vanish because `g_i->0`.
The remainder is `o(1)` after division by `g_i^2`. Taking the limsup gives
the displayed bound. A term with `p_sf,a<1` would scale like
`g_i^{2p_sf,a-2}` and therefore would not be bounded in this normalization
unless removed by a separate local normalization. `square`

### Definition 8J.16D: Local Counterterm Transverse Normalization `CT-TRANS_0`

Let

```math
R_{0,j}^{ct,\perp}
```

be the counterterm contribution to the transverse local residual after:

1. all relevant and marginal counterterms declared by Paper 16 are inserted
   into the local renormalized action;
2. the `rho_0` time-tangent part has been absorbed into `tau_j^time`;
3. the remaining local normalization conditions are imposed on the finite
   `SEL_0` battery.

`CT-TRANS_0(C_{ct,0},p_{ct})` holds when

```math
\|R_{0,j}^{ct,\perp}\|_{0,loc}
\le
C_{ct,0}g_i^{2p_{ct}}+o(g_i^2)
```

with

```math
p_{ct}\ge1.
```

A sufficient Paper-16 source route is:

```text
HK-CT-CLOSE for irrelevant and scheme-change tails
+ all strictly local relevant/marginal counterterms lie in tau_time
   or are fixed to zero by the SEL_0 local normalization
+ the remaining irrelevant local projection has order g_i^{2p_ct}, p_ct>=1.
```

If a strictly local relevant or marginal counterterm has a nonzero transverse
projection on `SEL_0`, then this gate fails until that coordinate is either
declared as part of the local record normalization or shown to cancel.

### Lemma 8J.16E: `CT-TRANS_0` Proves The Counterterm Debit

If `CT-TRANS_0(C_{ct,0},p_{ct})` holds, then

```math
\limsup_j
{\|R_{0,j}^{ct,\perp}\|_{0,loc}\over g_i^2}
\le
A_{ct,0}^{src},
```

where

```math
A_{ct,0}^{src}
=
\begin{cases}
C_{ct,0},& p_{ct}=1,\\
0,& p_{ct}>1.
\end{cases}
```

Thus one may take `A_ct,0=A_ct,0^src`.

Proof.

Divide the defining estimate by `g_i^2`. If `p_ct=1`, the limsup is at most
`C_ct,0`. If `p_ct>1`, the term vanishes. The `o(g_i^2)` remainder vanishes
in both cases. `square`

### Definition 8J.16F: Local Scheme Transverse Drift `SCH-TRANS_0`

The matched-time proof coordinate is admissible only when it remains inside
the same AF scheme ledger. Let `lambda` denote the finite-dimensional local
scheme coordinates remaining after the heat-kernel time coordinate has been
separated. Let

```math
K_{0}^{loc}(\lambda)
```

be the local action coordinate map on the finite `SEL_0` battery, and let
`Pi_0^\perp` be the finite projection to the complement of the time tangent
`Phi_0`.

`SCH-TRANS_0(H_{sch,0},K_{sch,0})` holds when:

1. the first local scheme derivative is time-tangent:

   ```math
   \Pi_0^\perp D_\lambda K_0^{loc}(0)=0;
   ```

2. the second transverse derivative is uniformly bounded:

   ```math
   \|\Pi_0^\perp D_\lambda^2K_0^{loc}(\lambda)\|_{0,loc}
   \le H_{sch,0}
   ```

   on the selected local scheme neighborhood;
3. the allowed matched-scheme displacement obeys

   ```math
   \|\lambda_j\|\le K_{sch,0}g_i.
   ```

This is a finite-dimensional statement about the declared local record
normalization. It does not introduce a second physical process; it checks
that the scheme coordinate used to remove the time drift is an admissible
coordinate of the same whole-process ledger.

### Lemma 8J.16G: Quadratic Scheme Drift Is `O(g_i^2)`

If `SCH-TRANS_0(H_{sch,0},K_{sch,0})` holds, then the transverse scheme
residual satisfies

```math
\limsup_j
{\|R_{0,j}^{sch,\perp}\|_{0,loc}\over g_i^2}
\le
{1\over2}H_{sch,0}K_{sch,0}^2.
```

Thus one may take

```math
A_{sch,0}^{src}
=
{1\over2}H_{sch,0}K_{sch,0}^2.
```

If the first scheme derivative has a nonzero transverse component and
`||lambda_j||` is only `O(g_i)`, this same-block route fails: it produces an
`O(g_i)` transverse drift, which is too large in the `g_i^2` normalization.

Proof.

Taylor expand the transverse scheme contribution:

```math
\Pi_0^\perp
\left[
K_0^{loc}(\lambda_j)-K_0^{loc}(0)
\right]
=
\Pi_0^\perp D_\lambda K_0^{loc}(0)\lambda_j
+{1\over2}\Pi_0^\perp D_\lambda^2K_0^{loc}(\lambda_j^*)[\lambda_j,\lambda_j].
```

The first term vanishes by clause 1. Clauses 2 and 3 bound the second term by

```math
{1\over2}H_{sch,0}K_{sch,0}^2g_i^2.
```

Divide by `g_i^2` and take limsup. `square`

### Theorem 8J.16H: Full `SEL_0` Same-Block Residual Closure

Assume:

1. `LF-IMP_0`;
2. `SF-TRANS_0(I_{sf},C_{sf,a},p_{sf,a})`;
3. `CT-TRANS_0(C_{ct,0},p_{ct})`;
4. `SCH-TRANS_0(H_{sch,0},K_{sch,0})`;
5. all four residual pieces are measured in the same `SEL_0` local norm and
   the same pushed-forward record law.

Define

```math
A_{sf,0}^{src}
:=
\sum_{a\in I_{sf}:p_{sf,a}=1}C_{sf,a},
```

```math
A_{ct,0}^{src}
:=
\begin{cases}
C_{ct,0},&p_{ct}=1,\\
0,&p_{ct}>1,
\end{cases}
\qquad
A_{sch,0}^{src}
:=
{1\over2}H_{sch,0}K_{sch,0}^2.
```

Then

```math
HK\text{-}BLOCK\text{-}RES_0(A_0^{blk})
```

holds with

```math
A_0^{blk}
\le
A_{sf,0}^{src}+A_{ct,0}^{src}+A_{sch,0}^{src}.
```

Consequently, using Section 8J.14,

```math
K_{block}^{(0)}
\le
2C_{sup,0}
\left(
A_{sf,0}^{src}+A_{ct,0}^{src}+A_{sch,0}^{src}
\right).
```

Proof.

`LF-IMP_0` gives `A_lf,0=0`. Lemma 8J.16C bounds the small-field part,
Lemma 8J.16E bounds the counterterm part, and Lemma 8J.16G bounds the scheme
part. Adding the four pieces gives `HK-BLOCK-RES_0`. The block coefficient
bound follows from Theorem 8J.14D and Theorem 8J.13E. `square`

### Theorem 8J.16I: Reassembled Same-Block Pass Test

Assume the hypotheses of Theorem 8J.16H, `HK-CROSS-COEFF_0(C_0^res)`, and
`HK-EXTRACT-COEFF_0(X_0)`. Then the matched-time non-time heat-kernel row
passes if

```math
2C_{sup,0}
\left(
A_{sf,0}^{src}+A_{ct,0}^{src}+A_{sch,0}^{src}
\right)
+C_0^{res}+X_0
<R_0^{crit}.
```

In the exact sup-dominating character basis, where `C_sup,0=1`, this becomes

```math
2
\left(
A_{sf,0}^{src}+A_{ct,0}^{src}+A_{sch,0}^{src}
\right)
+C_0^{res}+X_0
<R_0^{crit}.
```

Proof.

Theorem 8J.16H bounds the same-block term. Add the cross and extraction
debits and apply Theorem 8J.12K. `square`

### 8J.16J Present Verdict On Steps 1--5

Steps 1--5 are now closed as a local conditional theorem:

```text
LF-IMP_0
+ SF-TRANS_0
+ CT-TRANS_0
+ SCH-TRANS_0
+ 2 C_sup,0(A_sf,0^src+A_ct,0^src+A_sch,0^src)+C_0^res+X_0<R_0^crit
=> SEL_0 same-block/non-time row passes.
```

What remains actual, rather than formal, is the source verification:

```text
1. prove all transverse small-field local vertices have p>=1;
2. prove relevant/marginal counterterms have no unabsorbed transverse SEL_0
   component;
3. prove the matched-scheme first derivative is time-tangent and the
   residual scheme displacement is O(g_i);
4. insert the resulting constants into the scalar inequality.
```

The local large-field clause is closed by Theorem 8J.15M.1. If any of the
remaining transverse clauses fail, the matched-time heat-kernel row is not merely
unproved: this `SEL_0` route is falsified unless the offending transverse
term is moved into a declared local coordinate and the whole-process ledger
is updated.

### 8J.17 Prove Or Falsify `SF-TRANS_0`

We now attack clause 2. The source question is:

```text
After the heat-kernel time tangent and declared counterterms are removed,
does the local small-field contribution have no transverse term below order
g_i^2?
```

Paper 16's `HK-SF-CLOSE` says that local small-field vertices are bounded by
`C_v g_i^{2p}` after the declared counterterms. Paper 16's later
`HK-SF-YM2` ledger lists the generic second-order Yang-Mills labels; the
present section specializes that generic vertex ledger to the actual
`SEL_0` one-block projection and proves the exact import theorem and the
exact falsifier.

### Definition 8J.17A: `SEL_0` Small-Field Vertex Ledger `SF-VERT_0`

`SF-VERT_0` holds when the gauge-fixed small-field coordinate proof, after
pushforward to the finite `SEL_0` local record law, supplies an expansion
through order `g_i^2`:

```math
R_{0,j}^{sf}
=
g_i\,L_{1,j}
+g_i^2L_{2,j}
+Q_{3,j},
```

with

```math
\|Q_{3,j}\|_{0,loc}=o(g_i^2).
```

The order-two coefficient has a finite split

```math
L_{2,j}
=
b_{2,j}\Phi_0
+\sum_{a\in I_{sf}^{(2)}} c_{a,j}W_{a,j}^{\perp},
```

where `Phi_0` is the time tangent, the `W_a,j^perp` are finite local
transverse records in the `SEL_0` norm, and

```math
\|W_{a,j}^{\perp}\|_{0,loc}\le1,
\qquad
\limsup_j |c_{a,j}|\le C_{sf,a}<\infty.
```

The first coefficient is allowed only if it is killed by the neutrality
selection rule below.

### Definition 8J.17B: Neutral Odd-Vertex Cancellation `SF-ODD_0`

`SF-ODD_0` holds when the first small-field coefficient has no transverse
projection in the pushed-forward `SEL_0` law:

```math
\Pi_0^\perp L_{1,j}=0
```

for all sufficiently fine nodes.

A sufficient local proof is the standard neutral Wick/parity selection:

1. the small-field reference measure is centered and even in the gauge-fixed
   fluctuation coordinates after the axial-tree chart is forgotten;
2. the normalized character record
   `chi_{rho_0}(\exp(g_iA))/d_{rho_0}` has no linear term because
   `tr_{rho_0}(T^a)=0`;
3. the order-`g_i` Yang-Mills cubic or Jacobian insertion is odd in the
   centered Gaussian variables, so its expectation against the `SEL_0`
   neutral record battery vanishes;
4. any surviving order-`g_i` local coordinate is purely a declared gauge/chart
   proof artifact and has zero projection after pushforward to the finite
   record law.

The point is not that the gauge-fixed action has no cubic vertex. It does.
The point is that a single odd vertex cannot contribute to this neutral
one-block character coefficient after the declared record pushforward.

### Lemma 8J.17C: `SF-VERT_0 + SF-ODD_0` Proves `SF-TRANS_0`

Assume `SF-VERT_0` and `SF-ODD_0`. Assume also that the time-tangent part
`b_{2,j}\Phi_0` is absorbed into `tau_j^time`. Then `SF-TRANS_0` holds with

```math
I_{sf}=I_{sf}^{(2)},
\qquad
p_{sf,a}=1,
\qquad
C_{sf,a}=\limsup_j|c_{a,j}|.
```

Consequently

```math
A_{sf,0}^{src}
\le
\sum_{a\in I_{sf}^{(2)}} C_{sf,a}.
```

Proof.

Project the expansion of Definition 8J.17A to the transverse complement of
`Phi_0`. The order-`g_i` term vanishes by `SF-ODD_0`. The time-tangent part
of `L_2,j` is absorbed into `tau_j^time`. What remains is

```math
R_{0,j}^{sf,\perp}
=
g_i^2
\sum_{a\in I_{sf}^{(2)}} c_{a,j}W_{a,j}^{\perp}
+Q_{3,j}^{\perp}.
```

This is Definition 8J.16B with `p_sf,a=1` and with an `o(g_i^2)` remainder.
Lemma 8J.16C gives the displayed debit. `square`

### Theorem 8J.17D: Falsifier For `SF-TRANS_0`

Suppose the local small-field expansion has a transverse coefficient below
order `g_i^2`: there exist `q<2` and a cofinal tail such that

```math
R_{0,j}^{sf,\perp}
=
g_i^q U_j^\perp+\widetilde Q_j,
\qquad
\|U_j^\perp\|_{0,loc}\ge u_->0,
\qquad
\|\widetilde Q_j\|_{0,loc}=o(g_i^q).
```

Then `SF-TRANS_0` is false on this `SEL_0` row. In particular, a surviving
order-`g_i` transverse contribution falsifies the matched-time same-block
route.

Proof.

Divide by `g_i^2`:

```math
{\|R_{0,j}^{sf,\perp}\|_{0,loc}\over g_i^2}
\ge
{u_-\over2}g_i^{q-2}
```

on a cofinal tail. Since `q<2` and `g_i->0`, the right-hand side diverges.
Thus no finite constant `A_sf,0` can satisfy Definition 8J.16B. `square`

### Theorem 8J.17E: Present Decision For `SF-TRANS_0`

From the current source papers alone, `SF-TRANS_0` is not unconditionally
proved and not falsified. What is proved in Paper 19 is the exact decision:

```text
SF-VERT_0 + SF-ODD_0 + time-tangent absorption
=> SF-TRANS_0,
```

whereas

```text
nonzero transverse small-field term of order g_i^q, q<2
=> SF-TRANS_0 is false.
```

The natural Yang-Mills small-field expectation is favorable: the order-`g_i`
cubic term is odd and a single insertion should vanish against the neutral
`SEL_0` character battery, while the first possible transverse corrections
come from quartic, cubic-cubic, Jacobian, covariance, record, and finite local
normalization terms at order `g_i^2`. Section 8J.18 now writes this finite
one-block ledger explicitly. The remaining non-formal source work is not the
list; it is the numerical/symbolic evaluation of the finite constants in that
list from the chosen Paper-11/Paper-16 small-field construction.

Thus the honest status is:

```text
SF-TRANS_0 is conditionally proved by the local parity/vertex ledger.
It is not yet an unconditional theorem of the current source papers.
It would be falsified by any surviving order-g_i transverse SEL_0 vertex.
```

The next actual source task is therefore finite and explicit: evaluate the
constants in the `SEL_0` one-block small-field vertex list of Section 8J.18
and compare the resulting scalar debit with `R_0^crit`.

### 8J.18 Explicit First `SEL_0` Small-Field Vertex Worksheet

This section performs the finite one-block task left by Section 8J.17. It
does not introduce a new physical state space. The gauge-fixed small-field
coordinates are proof coordinates; the output is the pushed-forward neutral
character-record coefficient on the `SEL_0` battery.

Fix one `SEL_0` block collar `B_0`. Let `gamma_{0,j}` denote the centered
Gaussian small-field reference law in the chosen axial-tree block chart, and
let

```math
{\mathcal P}_{0,j}
```

denote pushforward to the finite neutral `SEL_0` character record. Let
`Phi_0` be the heat-kernel time tangent for the selected record
`f_0(U)=chi_{rho_0}(U)/d_{rho_0}`. Let `Pi_0^perp` be the finite projection
to the complement of `span{Phi_0}` in the local record coefficient norm.

#### Definition 8J.18A: Vertices Through Order `g_i^2`

The one-block small-field density, after extracting the Gaussian quadratic
part and the declared counterterms, has the pushed-forward expansion

```math
R_{0,j}^{sf}
=
g_i\,V_{3,j}^{odd}
+g_i^2
\left(
V_{4,j}
+V_{33,j}
+V_{J2,j}
+V_{gf2,j}
+V_{cov2,j}
+V_{rec2,j}
+V_{norm2,j}
\right)
+Q_{3,j},
```

where `||Q_3,j||_{0,loc}=o(g_i^2)`. The terms are:

```text
V_3^odd   : one cubic Yang-Mills insertion, plus any odd chart/gauge-slice
            insertion surviving before neutral pushforward;
V_4       : one quartic Yang-Mills insertion;
V_33      : the connected second cumulant of two cubic insertions;
V_J2      : quadratic Haar/log-chart/Jacobian insertion;
V_gf2     : quadratic gauge-slice or Faddeev-Popov insertion
            (zero in a strict unit-Jacobian axial-tree chart);
V_cov2    : block-conditioning/covariance-drift insertion;
V_rec2    : second-order expansion of the neutral character record itself;
V_norm2   : local normalization subtraction from the ratio/pushforward.
```

The finite second-order index set is

```math
I_{sf}^{(2)}
=
\{4,33,J2,gf2,cov2,rec2,norm2\}.
```

For each `a in I_sf^(2)` set

```math
C_{sf,a}
:=
\limsup_j
\left\|
\Pi_0^\perp V_{a,j}
\right\|_{0,loc}.
```

If a vertex is absent in the chosen chart, its constant is `0`. In
particular, `C_sf,gf2=0` for a strict axial-tree chart whose gauge-slice
determinant is already included in `J2` or is exactly constant.

#### Lemma 8J.18B: Odd Order-`g_i` Cancellation After Neutral Pushforward

Assume the `SEL_0` chart is centered and the Gaussian reference law is even
under the local involution `A -> -A`. Assume also that the selected record is
neutral:

```math
{\rm tr}_{\rho_0}(T^a)=0
```

for every Lie algebra generator `T^a`, and that the local chart/Jacobian has
no unpaired linear term. Then

```math
\Pi_0^\perp{\mathcal P}_{0,j}\!\left[V_{3,j}^{odd}\right]=0.
```

Consequently the order-`g_i` term in the pushed-forward transverse
small-field residual vanishes.

Proof.

The cubic Yang-Mills insertion is odd in the centered fluctuation coordinate.
The Gaussian reference measure is even, so every expectation of an odd local
polynomial against an even local test is zero. The neutral character record
has no linear Lie-algebra coefficient because
`tr_{rho_0}(T^a)=0`; hence its first nontrivial local Taylor coefficient is
even. Any chart/Jacobian contribution at order `g_i` is either absent because
the logarithmic Jacobian starts quadratically, or is an odd gauge-slice
artifact. Such an artifact integrates to zero after the same neutral
pushforward. Therefore the entire pushed-forward order-`g_i` transverse
coefficient vanishes. `square`

#### Lemma 8J.18C: Absorption Of The Order-`g_i^2` Time Tangent

Let

```math
L_{2,j}
:=
V_{4,j}+V_{33,j}+V_{J2,j}+V_{gf2,j}
+V_{cov2,j}+V_{rec2,j}+V_{norm2,j}.
```

Choose the finite dual functional `ell_0^time` with
`ell_0^time(Phi_0)=1` and `ell_0^time` vanishing on the declared transverse
basis. Define

```math
b_{2,j}:=\ell_0^{time}(L_{2,j}),
\qquad
L_{2,j}^{\perp}:=L_{2,j}-b_{2,j}\Phi_0.
```

Then replacing the selected heat-kernel time by

```math
\tau_j^{time,new}
=
\tau_j^{time}+g_i^2 b_{2,j}
```

removes the order-`g_i^2` time-tangent part without changing any neutral
transverse coefficient. In particular,

```math
\Pi_0^\perp L_{2,j}
=
\Pi_0^\perp L_{2,j}^{\perp}.
```

Proof.

The `SEL_0` battery is finite. Thus `span{Phi_0}` has a finite algebraic
complement, and the displayed projection is well-defined. The heat-kernel
coefficient of the selected record satisfies

```math
{d\over dt}\exp(-tC_2(\rho_0)/2)
=
-{C_2(\rho_0)\over2}\exp(-tC_2(\rho_0)/2),
```

so a displacement of the local time parameter changes the record only along
`Phi_0`. Absorbing `g_i^2 b_2,j Phi_0` into the time coordinate therefore
does not alter the transverse pushed-forward coefficient. `square`

#### Theorem 8J.18D: Explicit Small-Field Debit On `SEL_0`

Under the hypotheses of Definition 8J.18A, Lemma 8J.18B, and Lemma 8J.18C,
`SF-TRANS_0` holds with

```math
I_{sf}=I_{sf}^{(2)},
\qquad
p_{sf,a}=1
\quad(a\in I_{sf}^{(2)}),
```

and

```math
A_{sf,0}^{src}
=
\sum_{a\in I_{sf}^{(2)}} C_{sf,a}.
```

Equivalently, in expanded form,

```math
A_{sf,0}^{src}
=
C_{sf,4}
+C_{sf,33}
+C_{sf,J2}
+C_{sf,gf2}
+C_{sf,cov2}
+C_{sf,rec2}
+C_{sf,norm2}.
```

Proof.

Lemma 8J.18B removes the whole order-`g_i` piece after pushforward to the
neutral record. Lemma 8J.18C removes the order-`g_i^2` time-tangent piece.
The remaining transverse coefficient is therefore

```math
R_{0,j}^{sf,\perp}
=
g_i^2
\sum_{a\in I_{sf}^{(2)}}
\Pi_0^\perp V_{a,j}
+Q_{3,j}^{\perp},
\qquad
\|Q_{3,j}^{\perp}\|_{0,loc}=o(g_i^2).
```

Dividing by `g_i^2` and taking `limsup` gives

```math
\limsup_j
{\|R_{0,j}^{sf,\perp}\|_{0,loc}\over g_i^2}
\le
\sum_{a\in I_{sf}^{(2)}}
\limsup_j\|\Pi_0^\perp V_{a,j}\|_{0,loc}.
```

This is precisely the displayed formula for `A_sf,0^src`. `square`

#### Corollary 8J.18E: Paper-11 Source Ceiling

Using the Paper-11 small-field constants on the same block chart, the first
three universal entries admit the coarse source ceilings

```math
C_{sf,4}
\le
M_{4,0}\,24C_4C_{\rm cov}^{2},
\qquad
C_{sf,33}
\le
M_{33,0}\,18C_3^2C_{\rm cov}^{3},
\qquad
C_{sf,J2}
\le
M_{J,0}\,C_JC_{\rm cov},
```

where `M_4,0`, `M_33,0`, and `M_J,0` are finite `SEL_0` pushforward/projection
operator constants for the chosen one-block record norm. Thus a completely
explicit sufficient small-field debit is

```math
A_{sf,0}^{src}
\le
M_{4,0}\,24C_4C_{\rm cov}^{2}
+M_{33,0}\,18C_3^2C_{\rm cov}^{3}
+M_{J,0}\,C_JC_{\rm cov}
+C_{sf,gf2}
+C_{sf,cov2}
+C_{sf,rec2}
+C_{sf,norm2}.
```

Proof.

Paper 11 bounds one cubic small-field insertion by
`6C_3C_cov^{3/2}g_i`, one quartic insertion by
`24C_4C_cov^2g_i^2`, and the quadratic Jacobian correction by
`C_JC_cov g_i^2` in the block-collar norm. The pushed-forward `SEL_0`
projection is a finite linear map, so applying its operator constants gives
the displayed quartic and Jacobian bounds. For the connected double-cubic
entry, the cumulant factor is `1/2`, hence

```math
{1\over2}\left(6C_3C_{\rm cov}^{3/2}\right)^2
=
18C_3^2C_{\rm cov}^{3}.
```

The remaining four terms are already defined as their exact `SEL_0`
projected limsup constants. Summing the seven entries gives the stated
ceiling. `square`

This ceiling is intentionally not claimed to be sharp. It is the finite
constant row that must be inserted into the scalar test

```math
2C_{sup,0}(A_{sf,0}^{src}+A_{ct,0}^{src}+A_{sch,0}^{src})
+C_0^{res}+X_0<R_0^{crit}.
```

The remaining issue is now a source-constant evaluation, not structural:
insert symbolic or numerical values for the finite `SEL_0` chart constants
and test the scalar margin below.

### 8J.19 Symbolic Evaluation Against `R_0^crit`

This section evaluates the seven entries from Section 8J.18 as far as the
current source papers allow. There are no decimal constants in Papers 11 and
16 to insert here. The actual output is therefore a symbolic `SEL_0` row:
every remaining number is a finite one-block operator constant in the
declared record norm.

Use the connected/cumulant normalization of the pushed-forward one-block
law. In that normalization the denominator subtraction is already included
in each connected vertex, so

```math
C_{sf,norm2}=0.
```

Use the chosen block axial-tree chart. Its gauge-slice determinant is either
constant or included in the Haar/log-chart Jacobian term. Thus

```math
C_{sf,gf2}=0.
```

Use the minimal `SEL_0` coefficient readout: the normalized `rho_0`
coefficient and the heat-kernel time tangent `Phi_0`. Then the second-order
record drift in the selected coefficient is time-tangent after the
`tau_j^time` absorption of Lemma 8J.18C. Hence

```math
C_{sf,rec2}=0
```

on the minimal readout. If diagnostic neutral characters are retained in an
enlarged battery, replace this zero by the finite projected constant
`C_{sf,rec2}^{diag}`; the theorem below remains valid with that replacement.

It remains to evaluate the three universal local vertices and the possible
block-conditioned covariance drift. Define the exact covariance-drift source
constant

```math
K_{cov,0}^{blk}
:=
\limsup_j
g_i^{-2}
\left\|
C_{0,j}^{cond}-C_{0,j}^{ref}
\right\|_{op,0},
```

where `C_0,j^cond` is the actual block-conditioned Gaussian covariance in
the `SEL_0` chart, `C_0,j^ref` is the reference covariance used in the local
heat-kernel comparison, and `||.||_{op,0}` is the induced operator norm on
second local record derivatives. Let `M_cov,0` be the finite norm of the
corresponding second-derivative pushforward/projection map. Then

```math
C_{sf,cov2}
\le
M_{cov,0}K_{cov,0}^{blk}.
```

Combining this with Corollary 8J.18E gives the symbolic evaluated
small-field debit

```math
A_{sf,0}^{eval}
:=
24M_{4,0}C_4C_{\rm cov}^{2}
+18M_{33,0}C_3^2C_{\rm cov}^{3}
+M_{J,0}C_JC_{\rm cov}
+M_{cov,0}K_{cov,0}^{blk}.
```

The actual `SEL_0` small-field debit satisfies

```math
A_{sf,0}^{src}
\le
A_{sf,0}^{eval}.
```

If the reference Gaussian is chosen to be the exact block-conditioned
Gaussian on the tested block, then `K_cov,0^blk=0`, and the evaluated
small-field debit reduces to

```math
A_{sf,0}^{eval,exact\ cov}
=
24M_{4,0}C_4C_{\rm cov}^{2}
+18M_{33,0}C_3^2C_{\rm cov}^{3}
+M_{J,0}C_JC_{\rm cov}.
```

#### Theorem 8J.19A: Evaluated Same-Block Pass Margin

Assume the Section 8J.18 hypotheses, the connected normalization above, the
chosen axial-tree chart, the minimal `SEL_0` coefficient readout, and the
covariance-drift bound `K_cov,0^blk<infty`. Define the evaluated local source
margin

```math
M_{loc,0}^{eval}
:=
R_0^{crit}
-C_0^{res}-X_0
-2C_{sup,0}
\left(
A_{sf,0}^{eval}
+A_{ct,0}^{src}
+A_{sch,0}^{src}
\right).
```

Then the matched-time same-block/non-time `SEL_0` row passes whenever

```math
M_{loc,0}^{eval}>0.
```

Equivalently, after inserting the first-selector threshold

```math
R_0^{crit}
=
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho_0)\over2},
```

the explicit symbolic pass inequality is

```math
2C_{sup,0}
\left(
24M_{4,0}C_4C_{\rm cov}^{2}
+18M_{33,0}C_3^2C_{\rm cov}^{3}
+M_{J,0}C_JC_{\rm cov}
+M_{cov,0}K_{cov,0}^{blk}
+A_{ct,0}^{src}
+A_{sch,0}^{src}
\right)
+C_0^{res}+X_0
<
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho_0)\over2}.
```

Proof.

Section 8J.18 gives the exact seven-term `A_sf,0^src`. The connected
normalization, axial-tree choice, and minimal coefficient readout set the
`norm2`, `gf2`, and `rec2` entries to zero. Corollary 8J.18E bounds the
quartic, double-cubic, and Jacobian entries, and the definition of
`K_cov,0^blk` bounds the covariance entry. Thus
`A_sf,0^src<=A_sf,0^eval`. Substitute this bound into Theorem 8J.16I.
The displayed formula for `R_0^crit` is Definition 8J.10C. `square`

#### Corollary 8J.19B: Exact-Readout, Exact-Covariance Minimal Row

In the exact coefficient-readout route `X_0=0`. If, in addition, the local
reference Gaussian is the actual block-conditioned Gaussian on the tested
block, then the sufficient row becomes

```math
2C_{sup,0}
\left(
24M_{4,0}C_4C_{\rm cov}^{2}
+18M_{33,0}C_3^2C_{\rm cov}^{3}
+M_{J,0}C_JC_{\rm cov}
+A_{ct,0}^{src}
+A_{sch,0}^{src}
\right)
+C_0^{res}
<
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho_0)\over2}.
```

If the sup-dominating character basis is also used, `C_sup,0=1`, and the
leading prefactor is exactly `2`.

#### Verdict 8J.19C: What Is Decided

The seven small-field constants have now been evaluated symbolically in the
`SEL_0` normalization:

```text
C_sf,4     <= 24 M_4,0 C_4 C_cov^2,
C_sf,33    <= 18 M_33,0 C_3^2 C_cov^3,
C_sf,J2    <= M_J,0 C_J C_cov,
C_sf,gf2   = 0          on the chosen axial-tree chart,
C_sf,cov2  <= M_cov,0 K_cov,0^blk,
C_sf,rec2  = 0          on the minimal SEL_0 coefficient readout,
C_sf,norm2 = 0          in connected/cumulant normalization.
```

Therefore the remaining same-block question is a single scalar inequality,
`M_loc,0^eval>0`. Current Papers 11 and 16 still do not provide numerical
values for

```text
M_4,0, M_33,0, M_J,0, M_cov,0, K_cov,0^blk,
C_3, C_4, C_J, C_cov, C_sup,0, C_0^res,
A_ct,0^src, A_sch,0^src.
```

So this section does not yet prove a positive pass against `R_0^crit`.
It does prove that there is no longer a hidden seven-constant ambiguity: the
pass/fail decision is exactly the evaluated scalar inequality above.

### 8J.20 Frozen Minimal `SEL_0` Row And Projection Constants

This section performs the two strongest finite-dimensional choices left open
in Section 8J.19.

#### Definition 8J.20A: Minimal Same-Block Normalization `MIN-SEL_0`

`MIN-SEL_0` is the following same-block normalization:

```text
1. connected/cumulant one-block normalization;
2. strict block axial-tree chart, with gauge determinant constant or included
   in the Jacobian term;
3. exact normalized rho_0 coefficient readout;
4. heat-kernel time tangent separated before transverse projection;
5. exact block-conditioned Gaussian used as the same-block reference
   covariance;
6. finite normalized-character basis for any declared transverse diagnostic
   records, with ell^1 coefficient norm.
```

The immediate consequences are

```math
X_0=0,\qquad
C_{sf,norm2}=0,\qquad
C_{sf,gf2}=0,\qquad
C_{sf,rec2}=0,\qquad
K_{cov,0}^{blk}=0.
```

Moreover, because normalized characters satisfy `|chi_lambda/d_lambda|<=1`,
the declared `ell^1` coefficient norm is sup-dominating with

```math
C_{sup,0}=1.
```

Proof.

The first three zeroes are exactly the connected normalization, axial-tree
chart, and minimal coefficient-readout clauses already isolated in Section
8J.19. Clause 5 makes `C_0,j^cond=C_0,j^ref` in the definition of
`K_cov,0^blk`, hence `K_cov,0^blk=0`. For a finite expansion
`H=sum_b h_b chi_b/d_b`,

```math
\|H\|_\infty
\le
\sum_b |h_b|\|\chi_b/d_b\|_\infty
\le
\sum_b |h_b|
=
\|H\|_{0,loc}.
```

Thus `SUP_0(1)` holds. `square`

#### Definition 8J.20B: Finite Character-Basis Projection Constants

Let `B_0^\perp` be the finite list of declared transverse normalized
character records after removing the time tangent `Phi_0`. Write this basis
as

```math
\psi_b(U)={\chi_{\lambda_b}(U)\over d_{\lambda_b}},
\qquad b\in B_0^\perp.
```

For each of the three universal small-field source types, define the
unit-normalized pushed-forward transverse coefficient by

```math
\widehat V_{4,j}
:=
{1\over24C_4C_{\rm cov}^{2}}
\Pi_0^\perp V_{4,j},
```

```math
\widehat V_{33,j}
:=
{1\over18C_3^2C_{\rm cov}^{3}}
\Pi_0^\perp V_{33,j},
```

and

```math
\widehat V_{J,j}
:=
{1\over C_JC_{\rm cov}}
\Pi_0^\perp V_{J2,j}.
```

Expand them in the finite transverse character basis:

```math
\widehat V_{a,j}
=
\sum_{b\in B_0^\perp} m_{a,b,j}\psi_b,
\qquad
a\in\{4,33,J\}.
```

The projection constants are

```math
M_{4,0}:=
\sum_{b\in B_0^\perp}\limsup_j |m_{4,b,j}|,
```

```math
M_{33,0}:=
\sum_{b\in B_0^\perp}\limsup_j |m_{33,b,j}|,
```

and

```math
M_{J,0}:=
\sum_{b\in B_0^\perp}\limsup_j |m_{J,b,j}|.
```

These are not new analytic hypotheses. They are finite sums of coefficients
in the declared record basis. In a fully specified finite battery they are
computed by evaluating the finitely many pushed-forward vertex coefficients
`m_a,b,j` and taking their cofinal limsups.

#### Lemma 8J.20C: Projection Constants Are Computable `ell^1` Upper Norms

Under `MIN-SEL_0`,

```math
\|\Pi_0^\perp V_{4,j}\|_{0,loc}
\le
24C_4C_{\rm cov}^{2}M_{4,0}+o(1),
```

```math
\|\Pi_0^\perp V_{33,j}\|_{0,loc}
\le
18C_3^2C_{\rm cov}^{3}M_{33,0}+o(1),
```

and

```math
\|\Pi_0^\perp V_{J2,j}\|_{0,loc}
\le
C_JC_{\rm cov}M_{J,0}+o(1).
```

If the transverse diagnostic list is empty, `B_0^\perp=\emptyset`, then

```math
M_{4,0}=M_{33,0}=M_{J,0}=0.
```

Proof.

The local norm in `MIN-SEL_0` is the `ell^1` coefficient norm in the basis
`{psi_b}`. Therefore

```math
\left\|
\sum_{b\in B_0^\perp}m_{a,b,j}\psi_b
\right\|_{0,loc}
=
\sum_{b\in B_0^\perp}|m_{a,b,j}|.
```

Multiplying by the corresponding Paper-11 normalization factor and taking
`limsup` gives the displayed bounds; the inequality is the only place where
cofinal oscillation can lose sharpness, since `limsup sum <= sum limsup` for
this finite basis. If the coefficients converge cofinally, the displayed
constants are the exact `ell^1` limits. If `B_0^\perp` is empty, the
projection target is the zero space, so all three sums are zero. `square`

#### Theorem 8J.20D: Minimal-Row Same-Block Test

Under `MIN-SEL_0`, the evaluated small-field debit is

```math
A_{sf,0}^{min}
=
24M_{4,0}C_4C_{\rm cov}^{2}
+18M_{33,0}C_3^2C_{\rm cov}^{3}
+M_{J,0}C_JC_{\rm cov}.
```

The same-block/non-time `SEL_0` row passes whenever

```math
M_{loc,0}^{min}>0,
```

where

```math
M_{loc,0}^{min}
:=
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho_0)\over2}
-C_0^{res}
-2
\left(
A_{sf,0}^{min}
+A_{ct,0}^{src}
+A_{sch,0}^{src}
\right).
```

Equivalently,

```math
2\left(
24M_{4,0}C_4C_{\rm cov}^{2}
+18M_{33,0}C_3^2C_{\rm cov}^{3}
+M_{J,0}C_JC_{\rm cov}
+A_{ct,0}^{src}
+A_{sch,0}^{src}
\right)
+C_0^{res}
<
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho_0)\over2}.
```

Proof.

Definition 8J.20A gives `X_0=0`, `C_sup,0=1`, and `K_cov,0^blk=0`. Lemma
8J.20C computes the three remaining small-field projection constants.
Substitute these values into Theorem 8J.19A. `square`

#### Corollary 8J.20E: Coefficient-Only Minimal Battery

If the same-block coefficient source uses no transverse diagnostic records,
so `B_0^\perp=\emptyset`, then

```math
A_{sf,0}^{min}=0.
```

In that coefficient-only row the same-block/non-time test reduces to

```math
2\left(A_{ct,0}^{src}+A_{sch,0}^{src}\right)
+C_0^{res}
<
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho_0)\over2}.
```

If the counterterm and scheme projections are also purely time-tangent or
fixed to zero on this row, then the local same-block source condition reduces
all the way to

```math
C_0^{res}
<
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho_0)\over2}.
```

This last display is not a claim that the full confinement proof has closed.
It is the sharp coefficient-only same-block row. The remaining Creutz-window,
pressure, cross-residual, and loss ledgers still have to pass on the same
whole-process tower.

#### Definition 8J.20F: Common Pushed-Forward Small-Field Record Law `CRL-SF_0`

`CRL-SF_0` holds when the `SEL_0` small-field calculation uses one and the
same finite pushed-forward record law for all of the following operations:

```text
1. the axial-tree small-field chart and centered Gaussian reference law;
2. the declared local counterterm and heat-kernel time-coordinate split;
3. the neutral character-record pushforward P_{0,j};
4. the time tangent Phi_0 and transverse projection Pi_0^perp;
5. the finite local norm ||.||_{0,loc};
6. the coefficient maps defining M_4,0, M_33,0, M_J,0, and M_cov,0.
```

Equivalently, the objects in Sections 8J.17--8J.20 are all computed from
one finite map

```math
{\mathcal P}_{0,j}:\text{small-field proof coordinates}\longrightarrow
\text{finite neutral }SEL_0\text{ records},
```

followed by the same algebraic projection

```math
\Pi_0^\perp:\text{finite }SEL_0\text{ coefficient space}
\longrightarrow
\text{span}\{\Phi_0\}^{\perp}.
```

No term may be estimated in a gauge-fixed proof coordinate and then combined
with a different projected record estimate. Gauge fixing, covariance
conditioning, time matching, and connected normalization are proof
coordinates only; the ontology is the pushed-forward finite record law.

#### Theorem 8J.20G: Verification Of `HK-SF-YM2` On The `SEL_0` Record Law

Assume:

1. `CRL-SF_0`;
2. the vertex expansion of Definition 8J.18A;
3. the odd cancellation hypotheses of Lemma 8J.18B;
4. the time-tangent absorption of Lemma 8J.18C;
5. the finite projection constants of Definition 8J.20B;
6. the connected/cumulant normalization and strict axial-tree chart of
   `MIN-SEL_0`, except that an enlarged finite diagnostic battery may keep a
   nonzero finite `rec2` entry.

Then the Paper-16 `HK-SF-YM2` clauses are verified on the same pushed-forward
`SEL_0` record law, with projected second-order label set

```math
I_{sf}^{(2)}
=
\{4,33,J2,gf2,cov2,rec2,norm2\}
```

and projected constants

```math
C_{sf,4}
\le
24M_{4,0}C_4C_{\rm cov}^{2},
```

```math
C_{sf,33}
\le
18M_{33,0}C_3^2C_{\rm cov}^{3},
```

```math
C_{sf,J2}
\le
M_{J,0}C_JC_{\rm cov},
```

```math
C_{sf,gf2}=0
\quad\text{in the strict axial-tree chart},
```

```math
C_{sf,cov2}
\le
M_{cov,0}K_{cov,0}^{blk},
```

```math
C_{sf,rec2}=0
\quad\text{for the minimal coefficient readout},
```

and

```math
C_{sf,norm2}=0
\quad\text{in connected/cumulant normalization}.
```

For an enlarged finite diagnostic battery, replace the zero in `rec2` by the
finite projected constant `C_{sf,rec2}^{diag}`. If the gauge slice is not the
strict axial-tree chart, replace the zero in `gf2` by the corresponding
finite projected gauge-slice constant. Thus the projected `SEL_0` vertex
constant is

```math
C_v^{YM2,SEL_0}
:=
24M_{4,0}C_4C_{\rm cov}^{2}
+18M_{33,0}C_3^2C_{\rm cov}^{3}
+M_{J,0}C_JC_{\rm cov}
+C_{sf,gf2}
+M_{cov,0}K_{cov,0}^{blk}
+C_{sf,rec2}
+C_{sf,norm2}
+C_{rem}g_*^{\epsilon_v}.
```

Consequently the `SEL_0` instance of the Paper-16 small-field source bound is

```math
\theta_{sf}^{SEL_0}
\le
e\,C_v^{YM2,SEL_0}C_GC_Eg_*^2.
```

Under the frozen minimal row `MIN-SEL_0`, this reduces to

```math
C_v^{YM2,SEL_0,min}
=
24M_{4,0}C_4C_{\rm cov}^{2}
+18M_{33,0}C_3^2C_{\rm cov}^{3}
+M_{J,0}C_JC_{\rm cov}
+C_{rem}g_*^{\epsilon_v},
```

and therefore

```math
\theta_{sf}^{SEL_0,min}
\le
e\,C_v^{YM2,SEL_0,min}C_GC_Eg_*^2.
```

Proof.

The common-record hypothesis fixes one map `mathcal P_0,j`, one tangent
`Phi_0`, one projection `Pi_0^perp`, and one local norm. Therefore every
coefficient below is a coefficient of the same pushed-forward `SEL_0` record
law.

Clause 1 of Paper-16 `HK-SF-YM2` is Lemma 8J.18B: the order-`g_i` cubic or
odd chart contribution has zero transverse coefficient after neutral
pushforward. The strict axial-tree exception is not a physical term; it is a
proof-coordinate gauge-slice artifact and has zero projection in the
declared record law.

Clause 2 is Lemma 8J.18C: the order-`g_i^2` component along `Phi_0` is
absorbed into the heat-kernel time coordinate, and the transverse projection
is unchanged.

Clause 3 follows by combining the first two clauses with Definition 8J.18A:
after the odd order-`g_i` part and the time tangent are removed, every
nonabsorbed local label begins at order `g_i^2`.

Clause 4 is exactly the finite list in Definition 8J.18A. No additional
local label is allowed unless it is either declared as an absorbed local
coordinate or appended to this finite list with its projected coefficient.

Clause 5 is Corollary 8J.18E plus Definition 8J.20B and Definition 8J.20A:
the quartic, double-cubic, and Jacobian entries are bounded by the displayed
finite projection constants; strict axial-tree, minimal readout, and
connected normalization set `gf2`, `rec2`, and `norm2` to zero; and exact
same-block covariance sets `K_cov,0^blk=0` in the minimal row. If any of
these simplifying choices is not made, the same proof keeps the
corresponding finite projected constant instead of zero.

Thus `HK-SF-YM2` is verified on the pushed-forward `SEL_0` record law with
`q_*=2` and `p=1`. Applying Paper-16 Theorem 9L.1I and Corollary 9L.1J gives
the displayed tree-activity bound. `square`

#### Corollary 8J.20H: Exact Falsifiers For The Common-Record Verification

The verification of Theorem 8J.20G fails, and the `SEL_0` import of
`HK-SF-YM2` is not proved, if any of the following occurs on a cofinal tail:

```text
1. the order-g_i odd/cubic coefficient has a nonzero transverse SEL_0
   projection;
2. an order-g_i^2 component cannot be decomposed into a time tangent plus
   finite transverse records;
3. a nonabsorbed local label appears with power q<2;
4. one of the finite projection constants M_4,0, M_33,0, M_J,0, M_cov,0,
   C_sf,gf2, C_sf,rec2, C_sf,norm2 is infinite;
5. the covariance, vertex, counterterm, time-tangent, or projection estimate
   is evaluated on a different record law.
```

Items 1--4 are mathematical falsifiers for this `SEL_0` small-field route.
Item 5 is a Barandes-alignment failure: it does not create a new
counterexample, but it invalidates the proof because it has mixed
proof-coordinate estimates with operational record estimates.

### 8J.21 Counterterm Debit On The Minimal Row

This section attacks the next local source term:

```math
A_{ct,0}^{src}.
```

The point is to separate three different objects that are easy to conflate:

1. relevant/marginal local counterterms;
2. irrelevant local counterterm remainders;
3. nonlocal counterterm and scheme tails.

Only the first two can enter the same-block debit. The nonlocal tails belong
to the cross/residual ledger, not to `A_ct,0^src`.

#### Definition 8J.21A: Local Counterterm Split `CT-SPLIT_0`

On the finite `SEL_0` one-block record law, write the local counterterm
contribution as

```math
R_{0,j}^{ct}
=
r_{YM,j}\Phi_0
+N_{0,j}
+R_{irr,0,j}^{ct}.
```

Here:

```text
r_YM,j Phi_0:
  the Yang-Mills coupling/time-tangent counterterm;

N_0,j:
  local normalization-fixed terms, including vacuum/identity terms and any
  declared finite-volume or boundary normalization whose SEL_0 coefficient is
  fixed to zero;

R_irr,0,j^ct:
  the irrelevant local counterterm remainder after the declared local action
  and normalization conditions have been imposed.
```

`CT-SPLIT_0` holds when

```math
\Pi_0^\perp(r_{YM,j}\Phi_0+N_{0,j})=0
```

on the pushed-forward `SEL_0` local record battery.

This is the local version of Paper 16's statement that strictly local
relevant/marginal counterterms are not residual errors: they are absorbed
into the declared renormalized local action and record normalization.

#### Lemma 8J.21B: Pure-Gauge Relevant/Marginal Counterterms Are Tangent Or Fixed

Assume the ledger-compatible pure-gauge Yang-Mills counterterm scheme of
Paper 11 and the local counterterm closure convention of Paper 16. Then
`CT-SPLIT_0` holds on the minimal `SEL_0` row.

Proof.

Paper 11's ledger-compatible pure-gauge trajectory has no relevant
gauge-invariant pure-gauge coupling other than the Yang-Mills coupling,
apart from declared finite-volume or boundary terms whose effects are fixed
or vanish in the tested battery. On the one-block `SEL_0` coefficient, a
change of the Yang-Mills coupling is exactly a local heat-kernel time
displacement and hence lies in `span{Phi_0}` after the matched-time
separation. Vacuum/identity terms are removed by connected/cumulant
normalization, and declared local boundary/finite-volume normalizations are
fixed to zero in the finite record battery. Therefore the relevant/marginal
local counterterm projection to the transverse complement vanishes. `square`

#### Definition 8J.21C: Irrelevant Local Counterterm Projection Constant

Let Paper 11's local counterterm/truncation remainder satisfy

```math
|V_{ct}(A;b)|
\le
C_{ct}g_i^{p+1}(1+\|A\|_b^4).
```

Set

```math
B_{ct,0}^{loc}
:=
C_{ct}(1+3C_{\rm cov}^{2})C_{obs,0},
```

where `C_obs,0` is the finite `SEL_0` one-block observable-derivative
conversion constant. Let `M_ct,0` be the finite `ell^1` projection constant
of the unit-normalized irrelevant local counterterm remainder onto
`B_0^\perp`. Equivalently, if

```math
{1\over B_{ct,0}^{loc}g_i^{p+1}}
\Pi_0^\perp R_{irr,0,j}^{ct}
=
\sum_{b\in B_0^\perp}m_{ct,b,j}\psi_b+o(1),
```

then define

```math
M_{ct,0}
:=
\sum_{b\in B_0^\perp}\limsup_j |m_{ct,b,j}|.
```

If `B_0^\perp=\emptyset`, then `M_ct,0=0`.

#### Lemma 8J.21D: Irrelevant Local Counterterm Debit

Assume `CT-SPLIT_0` and the local counterterm remainder bound of Definition
8J.21C. Then

```math
\|R_{0,j}^{ct,\perp}\|_{0,loc}
\le
M_{ct,0}B_{ct,0}^{loc}g_i^{p+1}+o(g_i^{p+1}).
```

Consequently `CT-TRANS_0` holds with

```math
p_{ct}={p+1\over2},
\qquad
C_{ct,0}=M_{ct,0}B_{ct,0}^{loc}.
```

The counterterm debit in the `g_i^2` normalization is therefore

```math
A_{ct,0}^{src}
\le
\begin{cases}
M_{ct,0}B_{ct,0}^{loc},&p=1,\\
0,&p>1.
\end{cases}
```

Proof.

`CT-SPLIT_0` removes the relevant/marginal local part from the transverse
projection. Paper 11's local remainder estimate and the Gaussian fourth
moment bound give the one-block coefficient bound
`B_ct,0^loc g_i^{p+1}` before projection. Applying the finite `ell^1`
projection constant `M_ct,0` gives the first displayed estimate. Since
`CT-TRANS_0` is normalized as `g_i^{2p_ct}`, the exponent is
`2p_ct=p+1`. Dividing by `g_i^2` gives a finite debit exactly when `p=1`,
and gives zero when `p>1`. `square`

#### Theorem 8J.21E: Minimal-Row Counterterm Decision

Under `MIN-SEL_0`, the Paper-11/Paper-16 pure-gauge local counterterm ledger
proves

```math
A_{ct,0}^{src}
\le
\begin{cases}
M_{ct,0}C_{ct}(1+3C_{\rm cov}^{2})C_{obs,0},&p=1,\\
0,&p>1.
\end{cases}
```

In the coefficient-only minimal row `B_0^\perp=\emptyset`, one has

```math
A_{ct,0}^{src}=0.
```

Proof.

Lemma 8J.21B proves `CT-SPLIT_0`. Lemma 8J.21D supplies the irrelevant local
counterterm debit. Under `MIN-SEL_0`, `B_ct,0^loc` is the displayed
Paper-11 constant in the `SEL_0` one-block observable norm. If
`B_0^\perp=\emptyset`, then `M_ct,0=0`, so the debit is zero regardless of
whether `p=1` or `p>1`. `square`

#### Theorem 8J.21F: Counterterm Falsifier

Suppose a relevant or marginal local counterterm has a surviving transverse
projection on the `SEL_0` battery:

```math
\Pi_0^\perp R_{rel/marg,0,j}^{ct}
=
\kappa_j U_0^\perp+\widetilde Q_j,
\qquad
\|U_0^\perp\|_{0,loc}\ge u_->0,
```

with

```math
|\kappa_j|\ge k_- g_i^q,
\qquad
\|\widetilde Q_j\|_{0,loc}=o(g_i^q),
```

for some `q<2` on a cofinal tail. Then `CT-TRANS_0` is false on this
`SEL_0` row. If `q=2`, the same term is not a falsifier, but it must be
charged as an additional debit of at least `k_-u_-`.

Proof.

Divide by `g_i^2`. If `q<2`, the lower bound grows like
`g_i^{q-2}` and no finite `A_ct,0^src` can bound the transverse
counterterm residual. If `q=2`, the term remains finite in the same
normalization and must be included in the debit. `square`

#### Corollary 8J.21G: Updated Minimal Local Margin

Combining Section 8J.20 with Theorem 8J.21E gives the minimal same-block
margin

```math
M_{loc,0}^{min,ct}
:=
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho_0)\over2}
-C_0^{res}
-2
\left(
A_{sf,0}^{min}
+A_{ct,0}^{min}
+A_{sch,0}^{src}
\right),
```

where

```math
A_{ct,0}^{min}
:=
\begin{cases}
M_{ct,0}C_{ct}(1+3C_{\rm cov}^{2})C_{obs,0},&p=1,\\
0,&p>1.
\end{cases}
```

The local row passes if

```math
M_{loc,0}^{min,ct}>0.
```

In the coefficient-only minimal row, `A_sf,0^min=A_ct,0^min=0`, so the
remaining local test is

```math
2A_{sch,0}^{src}+C_0^{res}
<
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho_0)\over2}.
```

Thus the counterterm debit is now closed conditionally on the declared
pure-gauge counterterm ledger. The remaining local source gate is the scheme
debit `A_sch,0^src`, attacked next.

### 8J.22 Scheme Debit On The Minimal Row

Section 8J.16 defined the scheme debit abstractly by the quadratic
`SCH-TRANS_0` gate. This section turns that gate into a finite
source-side decision problem on the frozen `MIN-SEL_0` row.

The word "scheme" here means a finite reparametrization of the local proof
coordinates and record readout inside the same whole-process law. It is not
a second process and it is not an extra physical dynamics. The heat-kernel
time coordinate has already been separated into `tau_j^time`; the remaining
question is whether any non-time local scheme coordinate moves the pushed
record law in a transverse `SEL_0` direction.

#### Definition 8J.22A: Residual Local Scheme Coordinate

Let `Lambda_0` be the finite-dimensional vector space of remaining local
scheme coordinates on the `SEL_0` row after:

1. the heat-kernel time coordinate has been separated;
2. relevant/marginal pure-gauge counterterms have been treated as in
   Section 8J.21;
3. the connected/cumulant normalization and exact `rho_0` coefficient
   readout of `MIN-SEL_0` have been fixed.

Let

```math
K_0^{loc}:\Lambda_0\longrightarrow {\mathcal R}_0^{loc}
```

be the finite local record-coordinate map, and write

```math
R_{0,j}^{sch,\perp}
:=
\Pi_0^\perp
\left[
K_0^{loc}(\lambda_j)-K_0^{loc}(0)
\right].
```

The displacement size is

```math
K_{sch,0}^{min}
:=
\limsup_j{\|\lambda_j\|_{\Lambda_0}\over g_{i(j)}}.
```

If the only scheme movement is the already separated heat-kernel time
coordinate, then `lambda_j=0` and `K_sch,0^min=0`.

#### Definition 8J.22B: Finite Scheme Hessian Constant

Choose a basis `e_alpha` of `Lambda_0` and the normalized-character
transverse basis `B_0^\perp` from Definition 8J.20B. For
`||lambda||_{\Lambda_0}\le r_sch` expand

```math
\Pi_0^\perp
D_\lambda^2K_0^{loc}(\lambda)[e_\alpha,e_\beta]
=
\sum_{b\in B_0^\perp}
h_{\alpha\beta b}(\lambda)\psi_b .
```

Define the finite upper Hessian norm

```math
H_{sch,0}^{min}
:=
\sup_{\|\lambda\|_{\Lambda_0}\le r_{sch}}
\sup_{\|u\|_{\Lambda_0}\le1,\ \|v\|_{\Lambda_0}\le1}
\left\|
\Pi_0^\perp D_\lambda^2K_0^{loc}(\lambda)[u,v]
\right\|_{0,loc}.
```

Equivalently, in the displayed finite basis one may use the computable
upper bound

```math
H_{sch,0}^{min}
\le
\sum_{\alpha,\beta}
\sum_{b\in B_0^\perp}
\sup_{\|\lambda\|\le r_{sch}}
|h_{\alpha\beta b}(\lambda)|.
```

If `B_0^\perp=\emptyset`, then `H_sch,0^min=0`.

#### Definition 8J.22C: Minimal Scheme Split `SCH-SPLIT_0`

`SCH-SPLIT_0` holds on the frozen `MIN-SEL_0` row when the first derivative
of every residual local scheme coordinate is time-tangent or
normalization-fixed:

```math
\Pi_0^\perp D_\lambda K_0^{loc}(0)=0.
```

Equivalently, after the heat-kernel time coordinate is removed, the local
scheme chart has no linear transverse motion on the declared finite record
battery.

This is the Barandes-aligned form of the condition: the finite scheme chart
is a bookkeeping coordinate for the same whole-process law, so a linear
change of coordinates may change the time parameter or the normalization
convention, but it may not secretly change the physical record law in a new
transverse direction.

#### Lemma 8J.22D: `SCH-SPLIT_0` Gives The Quadratic Scheme Debit

Assume `SCH-SPLIT_0`, `K_sch,0^min<infty`, and that the cofinal
displacements lie in the neighborhood `||lambda_j||<=r_sch`. Then
`SCH-TRANS_0` holds with

```math
H_{sch,0}=H_{sch,0}^{min},
\qquad
K_{sch,0}=K_{sch,0}^{min},
```

and therefore

```math
A_{sch,0}^{src}
\le
A_{sch,0}^{min}
:=
{1\over2}H_{sch,0}^{min}(K_{sch,0}^{min})^2.
```

Proof.

Taylor expand in the finite local scheme chart:

```math
\Pi_0^\perp
\left[
K_0^{loc}(\lambda_j)-K_0^{loc}(0)
\right]
=
\Pi_0^\perp D_\lambda K_0^{loc}(0)\lambda_j
+{1\over2}
\Pi_0^\perp
D_\lambda^2K_0^{loc}(\lambda_j^*)[\lambda_j,\lambda_j].
```

The first term is zero by `SCH-SPLIT_0`. The Hessian term is bounded by

```math
{1\over2}H_{sch,0}^{min}\|\lambda_j\|_{\Lambda_0}^2.
```

Divide by `g_i^2` and take the limsup. Definition 8J.22A gives the stated
constant. This is exactly Lemma 8J.16G with source constants now computed
inside the frozen finite scheme chart. `square`

#### Corollary 8J.22E: Time-Only Minimal Scheme Has Zero Debit

If the matched-time branch uses no residual non-time scheme coordinate after
the heat-kernel time has been separated, then

```math
\lambda_j=0,
\qquad
K_{sch,0}^{min}=0,
\qquad
A_{sch,0}^{src}=0.
```

In particular, in the coefficient-only minimal row with
`B_0^\perp=\emptyset`, the scheme debit also vanishes.

Proof.

If `lambda_j=0`, the residual scheme difference is identically zero. If
`B_0^\perp=\emptyset`, the transverse projection is the zero map, so
`H_sch,0^min=0` and the same conclusion follows. `square`

#### Theorem 8J.22F: Scheme-Debit Falsifier

Suppose a residual scheme coordinate has a surviving transverse linear
component:

```math
\Pi_0^\perp D_\lambda K_0^{loc}(0)v
=U_0^\perp,
\qquad
\|U_0^\perp\|_{0,loc}\ge u_->0,
```

and the cofinal displacement contains

```math
\lambda_j=\kappa_j v+\widetilde\lambda_j,
\qquad
|\kappa_j|\ge k_-g_i^q,
\qquad
\|\widetilde\lambda_j\|=o(g_i^q),
```

with `q<2`. Then `SCH-TRANS_0` is false on this row. If `q=2`, the linear
scheme motion is not a falsifier, but it must be charged as an additional
finite debit of at least `k_-u_-`.

Moreover, even if `SCH-SPLIT_0` holds, a quadratic scheme displacement with
`||lambda_j||>=k_-g_i^q` and `q<1` falsifies the quadratic route unless the
corresponding Hessian projection vanishes on that direction.

Proof.

A nonzero transverse linear derivative produces a residual of order
`g_i^q`. Dividing by `g_i^2` diverges when `q<2`; at `q=2` it remains a
finite source debit. Under `SCH-SPLIT_0`, the first nonzero term is
quadratic, hence order `g_i^{2q}`. This is too large in the `g_i^2`
normalization when `q<1` unless the Hessian projection in that direction is
zero. `square`

#### Corollary 8J.22G: Updated Minimal Local Margin After Scheme Debit

Combining Sections 8J.20--8J.22 gives

```math
M_{loc,0}^{min,ct,sch}
:=
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho_0)\over2}
-C_0^{res}
-2
\left(
A_{sf,0}^{min}
+A_{ct,0}^{min}
+A_{sch,0}^{min}
\right),
```

where

```math
A_{sch,0}^{min}
=
{1\over2}H_{sch,0}^{min}(K_{sch,0}^{min})^2.
```

The local `SEL_0` row passes once

```math
M_{loc,0}^{min,ct,sch}>0.
```

In the coefficient-only, time-only minimal branch,

```math
A_{sf,0}^{min}=A_{ct,0}^{min}=A_{sch,0}^{min}=0,
```

so the remaining local test reduces to

```math
C_0^{res}
<
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho_0)\over2}.
```

Thus the scheme debit is no longer a loose placeholder. It is either zero
on the time-only minimal branch, a finite Hessian-times-displacement debit,
or a precise falsifier when a transverse linear scheme motion survives below
order `g_i^2`.

### 8J.23 Cross-Residual Constant From The Paper-16 Tail

Sections 8J.20--8J.22 reduce the coefficient-only, time-only minimal row to
the single residual inequality

```math
C_0^{res}<R_0^{crit},
\qquad
R_0^{crit}
:=
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho_0)\over2}.
```

This section proves the exact Paper-16 reduction of `C_0^res`. It is the
first place where the cross-block residual-polymer tail, rather than a local
one-block source term, is the active bottleneck.

#### Definition 8J.23A: Available Residual Collar

Let `d_j^{av}` be the largest block-graph collar radius around the tested
`SEL_0` block record that can be removed from the cross-block residual sum
while staying inside the declared finite Creutz/window geometry and the same
whole-process record law.

The collar is admissible for the Paper-16 residual envelope when

```math
r_{res}\le r_j^{col}\le d_j^{av}
```

and the collar map is the same block/collar map used by the Paper-16
analytic branch. The number `d_j^{av}` is therefore not a free geometric
parameter; it is fixed by the chosen cofinal window and record battery.

#### Definition 8J.23B: Residual Tail Source Constant

Assume Paper 16 supplies the size-resolved residual envelope

```math
\sum_{\substack{Y\ni B_0\\ |Y|\ge r}}
|\zeta_j(Y)|e^{m|Y|}
\le
{C_{KP}A_{res}e^{-\Delta_{res}r}
\over
1-e^{-\Delta_{res}}},
```

with

```math
\Delta_{res}:=\mu_{res}-h_{KP}-m>0,
```

on the same pushed-forward heat-kernel record tower. Define the best
available residual constant from that envelope by

```math
C_{res}^{env}
:=
\limsup_j
{C_{KP}A_{res}\over1-e^{-\Delta_{res}}}
{e^{-\Delta_{res}d_j^{av}}\over g_{i(j)}^2}.
```

If `d_j^{av}<r_res` infinitely often, set `C_res^env=+\infty`.

#### Lemma 8J.23C: Maximal Collar Gives `HK-CROSS-COEFF_0(C_res^env)`

Under Definition 8J.23B, if `C_res^env<\infty`, then

```math
HK\text{-}CROSS\text{-}COEFF_0(C_{res}^{env})
```

holds. Hence

```math
K_{cross}^{(0)}\le C_{res}^{env}.
```

Proof.

Use the maximal admissible collar `r_j^{col}=d_j^{av}`. The residual
polymers contributing to `u_{0,j}^{res}-u_{0,j}^{block}` are exactly those
touching the tested block record and leaving that collar, after pushforward
from proof-coordinate polymers to the declared `SEL_0` coefficient record.
The Paper-16 envelope gives

```math
|u_{0,j}^{res}-u_{0,j}^{block}|
\le
{C_{KP}A_{res}e^{-\Delta_{res}d_j^{av}}
\over
1-e^{-\Delta_{res}}}.
```

Divide by `g_i^2` and take the limsup. This is Definition 8J.12E with
`C_0^res=C_res^env`, and Theorem 8J.12F gives the final inequality.
`square`

#### Definition 8J.23D: Targeted Collar Schedule

For a chosen target `0<C_0^{res,target}<R_0^{crit}`, define

```math
r_j^{target}
:=
\left\lceil
{1\over\Delta_{res}}
\left[
2\log {1\over g_{i(j)}}
+\log\left(
{C_{KP}A_{res}
\over
(1-e^{-\Delta_{res}})C_0^{res,target}}
\right)
\right]
\right\rceil .
```

The target schedule is admissible if, cofinally,

```math
r_{res}\le r_j^{target}\le d_j^{av}.
```

#### Theorem 8J.23E: Residual Tail Closes The Minimal Local Row

Assume:

1. the Paper-16 residual envelope of Definition 8J.23B holds on the same
   pushed-forward record tower;
2. `Delta_res>0`;
3. for some `0<theta_res<1`, the targeted collar schedule with

   ```math
   C_0^{res,target}:=\theta_{res}R_0^{crit}
   ```

   is admissible.

Then

```math
HK\text{-}CROSS\text{-}COEFF_0(\theta_{res}R_0^{crit})
```

and therefore

```math
C_0^{res}\le\theta_{res}R_0^{crit}<R_0^{crit}.
```

Consequently the coefficient-only, time-only minimal `SEL_0` local row
passes.

Proof.

The chosen schedule is exactly the logarithmic collar bound in Definition
8J.12E with `C_0^res=C_0^{res,target}`. Therefore the residual tail is at
most `C_0^{res,target}g_i^2` cofinally. Theorem 8J.12F proves
`K_cross^(0)<=C_0^{res,target}`. Since `theta_res<1`, this is strictly below
`R_0^crit`. Corollary 8J.22G says that, in the coefficient-only time-only
minimal branch, this strict residual inequality is the entire local row
test. `square`

#### Corollary 8J.23F: Growth-Rate Criterion For `C_0^res`

The targeted residual closure of Theorem 8J.23E is equivalent to the
existence of `theta_res<1` such that, cofinally,

```math
d_j^{av}
\ge
{1\over\Delta_{res}}
\left[
2\log {1\over g_{i(j)}}
+\log\left(
{C_{KP}A_{res}
\over
(1-e^{-\Delta_{res}})\theta_{res}R_0^{crit}}
\right)
\right]
+O(1).
```

In particular, the stronger asymptotic condition

```math
d_j^{av}
-
{2\over\Delta_{res}}\log {1\over g_{i(j)}}
\longrightarrow+\infty
```

implies that `C_res^env=0` and hence the residual tail is negligible in the
`g_i^2` normalization.

Proof.

The first statement is Definition 8J.23D with the ceiling absorbed into
`O(1)`. For the second, substitute the displayed growth into Definition
8J.23B:

```math
{e^{-\Delta_{res}d_j^{av}}\over g_i^2}
\le
\exp\left(
-\Delta_{res}
\left[
d_j^{av}-{2\over\Delta_{res}}\log {1\over g_i}
\right]
\right)
\to0.
```

Thus `C_res^env=0`. `square`

#### Theorem 8J.23G: Residual-Tail Falsification From Available Geometry

The Paper-16 residual envelope cannot prove the minimal local row on the
chosen `SEL_0` geometry if

```math
C_{res}^{env}\ge R_0^{crit}.
```

More sharply, if

```math
\liminf_j
{\left|u_{0,j}^{res}-u_{0,j}^{block}\right|
\over g_{i(j)}^2}
\ge R_0^{crit},
```

then the coefficient-only, time-only minimal row is actually false on that
cofinal branch.

Proof.

The first statement is a proof-limit statement: the best upper bound
available from the declared Paper-16 residual envelope and the maximal
admissible collar is not below the required strict margin. A better envelope
or larger window geometry would be needed. The second statement is an actual
lower-floor obstruction: in the coefficient-only, time-only branch
Corollary 8J.22G requires the residual coefficient drift to be strictly below
`R_0^crit`. A liminf at or above that value violates the row condition.
`square`

#### Status After The Residual-Tail Reduction

The cross-residual obstruction is now reduced to two actual source inputs:

```text
1. P19-AN-IMPORT(m), hence Delta_res^*>0 and K_res^*<infinity;
2. cofinal window geometry with
   d_av - (2/Delta_res^*)log(1/g_i)
   large enough for the desired theta_res<1.
```

If both hold, the minimal local `SEL_0` row closes. If the best available
envelope constant `C_res^env` is at least `R_0^crit`, the current residual
tail proof does not close the row; if an actual lower floor is also at least
`R_0^crit`, the row is falsified.

### 8J.24 Paper-16 Residual Constants And `SEL_0` Collar Geometry

Section 8J.23 leaves two named inputs. This section proves the clean import
from Paper 16 and the cofinal geometry pass for the square fractional
`SEL_0` branch.

#### Theorem 8J.24A: `P19-AN-IMPORT` Imports `Delta_res^*>0`

Assume `P19-AN-IMPORT(m)` on the same heat-kernel record-law tower. Then
Paper 16 `HK-AN-FINTPL-CLOSE(m)` and Theorem 9N.2A export

```text
Delta_res^* := Delta_19^{an} > 0,
K_res^* := K_19^{an} < infinity,
eta_res^* := eta_19^{res} < 1.
```

Consequently the Paper-19 residual envelope of Definition 8J.23B holds with
`Delta_res=Delta_res^*` and `K_res=K_res^*`, and the residual-decoration
component of Definition 8E.3 may use `eta_res^*`.

Proof.

Definition 0A.1 is precisely the same-tower finite-template import of
Paper 16 `HK-AN-FINTPL-CLOSE(m)`. Paper 16 Theorem 9N.2A then exports the
positive residual decay margin and summed geometric tail constant. The
subbattery/readout clause in `P19-AN-IMPORT(m)` identifies the Paper-16
residual KP activity with the Paper-19 residual-decoration component, so
`eta_res^*:=eta_19^{res}` is legitimate. All three constants are scalar
record-law constants on the same tower. `square`

#### Definition 8J.24B: Central-Collar `SEL_0` Placement

The square fractional `SEL_0` window has

```math
R_j=T_j=L_j,
\qquad
\sigma_j=\lfloor\alpha L_j\rfloor,
\qquad
0<\alpha<1.
```

`SEL_0-CENT-COL(c_{av},b_{av})` holds when the tested local block record is
placed in the central retained square slot and the finite endpoint,
plaquette-template, and collar-template losses are bounded by `b_av`, so that
the available residual collar satisfies

```math
d_j^{av}\ge c_{av}L_j-b_{av}
```

cofinally. For the standard centered square placement one may take any

```math
0<c_{av}<{1-\alpha\over2}
```

after increasing `b_av` by a finite amount.

#### Lemma 8J.24C: Square Fractional Windows Have Linear Collar Room

The standard centered `SEL_0` placement satisfies
`SEL_0-CENT-COL(c_av,b_av)` for every
`0<c_av<(1-alpha)/2`.

Proof.

The retained square slot has side length

```math
L_j-\sigma_j
=
(1-\alpha)L_j+O(1).
```

A centered block record in that slot has graph distance at least

```math
{1\over2}(L_j-\sigma_j)+O(1)
=
{1-\alpha\over2}L_j+O(1)
```

from the slot boundary. Subtract the finite endpoint, plaquette-template,
and collar-template losses. For any strict
`c_av<(1-alpha)/2`, the remaining `O(1)` loss is absorbed into a finite
`b_av` on a cofinal tail. `square`

#### Theorem 8J.24D: `SEL_0` Geometry Beats The Logarithmic Collar Demand

Assume:

1. `P19-AN-IMPORT(m)`, so Theorem 8J.24A gives `Delta_res^*>0` and
   `K_res^*<infinity`;
2. the standard centered `SEL_0` placement of Lemma 8J.24C;
3. `H_j=g_{i(j)}^{-2}` and `L_j=floor(sqrt(sH_j))` with `s>0`.

Then for every `0<theta_res<1`,

```math
r_j^{target}
\le d_j^{av}
```

cofinally, where `r_j^target` is the targeted collar of Definition 8J.23D
with `Delta_res=Delta_res^*`, `K_res=K_res^*`, and
`C_0^{res,target}=theta_res R_0^crit`. Hence

```math
C_{res}^{env}=0,
\qquad
HK\text{-}CROSS\text{-}COEFF_0(0),
\qquad
C_0^{res}=0<R_0^{crit}.
```

Consequently the coefficient-only, time-only minimal `SEL_0` local row
passes.

Proof.

By Lemma 8J.24C, for some `c_av>0` and finite `b_av`,

```math
d_j^{av}\ge c_{av}L_j-b_{av}.
```

Since `L_j=floor(sqrt(s)g_i^{-1})`, there is a tail on which

```math
d_j^{av}
\ge
{c_{av}\sqrt{s}\over2}g_i^{-1}.
```

The targeted collar has the form

```math
r_j^{target}
=
{2\over\Delta_{res}^*}\log {1\over g_i}
+O(1),
```

because `Delta_res^*>0`, `K_res^*<infty`, and `R_0^crit>0`. Therefore

```math
d_j^{av}-r_j^{target}
\ge
{c_{av}\sqrt{s}\over2}g_i^{-1}
-{2\over\Delta_{res}^*}\log {1\over g_i}
+O(1)
\longrightarrow+\infty,
```

since `g_i^{-1}` dominates `log(1/g_i)` as `g_i->0`. Thus the targeted
collar fits cofinally for every `theta_res<1`, and Corollary 8J.23F gives
`C_res^env=0`. The residual inequality is then strict because
`R_0^crit>0` for a nontrivial `rho_0` and `0<chi,epsilon_A<1`. Corollary
8J.22G closes the coefficient-only, time-only minimal local row. `square`

#### Theorem 8J.24E: Ordered Clean-Branch Local Closure

Assume the following branch choices and source inputs, in this order:

1. **Coefficient-only frozen row.** Use `MIN-SEL_0` with
   `B_0^\perp=\emptyset`, exact normalized `rho_0` coefficient readout,
   exact same-block covariance, connected/cumulant normalization, and the
   same pushed-forward record law `CRL-SF_0`.
2. **Local large-field import.** Use Theorem 8J.15M.1 on this same strict
   axial-tree finite-battery `SEL_0` row, so `LF-IMP_0` holds and
   `A_{lf,0}=0`.
3. **Small-field common-record verification.** Use Theorem 8J.20G to import
   Paper-16 `HK-SF-YM2` onto this `SEL_0` record law.
4. **Counterterm ledger.** Use the Paper-11/Paper-16 pure-gauge local
   counterterm ledger of Theorem 8J.21E.
5. **Time-only scheme branch.** Use the matched-time scheme branch of
   Corollary 8J.22E.
6. **Residual analytic closure.** Use `P19-AN-IMPORT(m)` on the same
   heat-kernel record-law tower, hence the Paper-16
   `HK-AN-FINTPL-CLOSE(m)` export.
7. **Residual geometry.** Use the centered square fractional `SEL_0`
   placement of Lemma 8J.24C with `H_j=g_i^{-2}` and
   `L_j=floor(sqrt(sH_j))`, `s>0`.

Then the local coefficient-only, time-only `SEL_0` row closes with

```math
A_{sf,0}^{min}=0,
\qquad
A_{lf,0}=0,
\qquad
A_{ct,0}^{min}=0,
\qquad
A_{sch,0}^{min}=0,
\qquad
X_0=0,
\qquad
C_0^{res}=0.
```

Consequently

```math
M_{loc,0}^{clean}
:=
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho_0)\over2}
>0,
```

and the matched-time same-block/non-time row passes:

```math
HK\text{-}BLOCK\text{-}COEFF_0(0),
\qquad
HK\text{-}CROSS\text{-}COEFF_0(0),
\qquad
HK\text{-}EXTRACT\text{-}COEFF_0(0).
```

Equivalently, the entire local scalar inequality reduces to

```math
0
<
R_0^{crit}
=
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho_0)\over2}.
```

Proof.

The coefficient-only frozen row makes the transverse diagnostic space empty:
`B_0^\perp=\emptyset`. Corollary 8J.20E therefore gives
`A_sf,0^min=0`; Theorem 8J.20G verifies that this zero is computed on the
same pushed-forward `SEL_0` law, rather than in an auxiliary gauge-fixed
coordinate. Definition 8J.20A also gives `X_0=0`.

The local large-field debit is zero by Theorem 8J.15M.1 on the same
strict axial-tree finite-battery `SEL_0` row: collar-adapted bad-field
exclusion, the bounded axial-tree collar extension, the finite
`HK-LF-REP-SRC` ledger, and `t_i<=T_+g_i^2` give `LF-IMP_0` and
`A_lf,0=0`.

The counterterm debit is zero by Theorem 8J.21E: the pure-gauge
relevant/marginal counterterms are time-tangent or normalization-fixed, and
the irrelevant local projection constant `M_ct,0` is zero because the
transverse target `B_0^\perp` is empty. Thus `A_ct,0^min=0`.

The scheme debit is zero by Corollary 8J.22E: the matched-time branch has no
residual non-time local scheme coordinate after the heat-kernel time has
been separated, and the coefficient-only transverse projection is the zero
map. Thus `A_sch,0^min=0`.

`P19-AN-IMPORT(m)` imports `Delta_res^*>0` and a finite residual tail
constant `K_res^*` by Theorem 8J.24A. The centered square fractional geometry has
`d_j^{av}>=c_avL_j-b_av` by Lemma 8J.24C, and with
`L_j=floor(sqrt(s)g_i^{-1})` this linear collar dominates the logarithmic
targeted collar. Theorem 8J.24D therefore gives
`HK-CROSS-COEFF_0(0)` and `C_0^{res}=0`.

Substituting these zero debits into Corollary 8J.22G leaves exactly
`R_0^crit>0`, which holds for nontrivial `rho_0` and
`0<chi,epsilon_A<1`. The block and extraction conclusions are the
corresponding zero-debit instances of Sections 8J.20 and 8J.12. `square`

#### Corollary 8J.24F: Minimal Same-Block Scalar Margin After Closed Large Field

Under the hypotheses of Theorem 8J.24E, the same pushed-forward
coefficient-only, time-only `SEL_0` record law satisfies the exact scalar
minimal-row identity

```math
2C_{sup,0}
\left(
A_{sf,0}^{min}+A_{ct,0}^{min}+A_{sch,0}^{min}
\right)
+C_0^{res}+X_0
=0.
```

Consequently the same-block scalar margin is

```math
M_{loc,0}^{clean}
=
R_0^{crit}
=
{(1-\chi)(1-\epsilon_A)\over1+\epsilon_A}
{C_2(\rho_0)\over2}
>0.
```

Proof.

The coefficient-only branch gives `A_sf,0^min=0` and `X_0=0` by
Corollary 8J.20E and Definition 8J.20A. Theorem 8J.15M.1 gives
`A_lf,0=0`, so no large-field term enters the non-time scalar debit.
Theorem 8J.21E gives `A_ct,0^min=0`; Corollary 8J.22E gives
`A_sch,0^min=0`; and Theorem 8J.24D gives `C_0^res=0`.
Substitution into the scalar same-block inequality of Corollary 8J.22G
leaves exactly `R_0^crit>0`. This is an equality of exported finite record
laws: the axial-tree chart, collar extension, and heat-kernel time coordinate
are proof coordinates only, and the final statement is about the pushed-
forward `SEL_0` character record. `square`

#### Honest Status Of This Closure

The geometry part is now closed for the centered square fractional `SEL_0`
branch: the available collar grows like `L_j~g_i^{-1}`, while the residual
tail only asks for `O(log(1/g_i))` blocks.

The analytic source part is imported exactly through `P19-AN-IMPORT(m)`.
Thus:

```text
P19-AN-IMPORT(m)
+ centered square fractional SEL_0 placement
=> Delta_res^*>0
+ enough d_j^av
+ C_0^res=0 on the minimal local row.
```

With the coefficient-only, time-only `MIN-SEL_0` branch, Theorem 8J.24E
also gives the complete ordered local closure:

```text
CRL-SF_0
+ HK-SF-YM2 on SEL_0
+ coefficient-only MIN-SEL_0
+ Theorem 8J.15M.1 local large-field import
+ pure-gauge counterterm ledger
+ time-only scheme branch
+ P19-AN-IMPORT(m)
+ centered square fractional SEL_0 geometry
=> local SEL_0 row passes with zero source/residual debits
=> M_loc,0^clean=R_0^crit>0.
```

The executable audit `P19-AN-AUDIT(m)` is closed for this clean branch by
Theorem 0A.6. Hence Corollary 0A.7 gives `P19-AN-IMPORT(m)` and Paper 19
uses the named Paper-16 analytic certificate without reconstructing the KP
worksheet here. The remaining loss-side work is no longer analytic import;
Section 8L closes the character-tail and finite-battery constant audits on
the intended clean branch, and then decomposes the four transport ceilings
into their component same-record source audits.

## 8K. Step 1a-X: AF-Matched Direct-Witness Closure And Loss Budget

Sections 8F--8J leave one final direct-witness question: after the
AF-matched coefficient source supplies a positive scalar signal, do the
Paper-15 decoration and transport losses fit below it?

### Definition 8K.1: AF-Matched Signal Floor

Assume the hypotheses of Theorem 8J.3. Define

```math
A_{{AFM}}^*
:=
{(1+\chi)s_+C_2(\rho)\over2}
 + {s_+R_H\over1-r_*},
```

and

```math
B_{{AFM}}^*
:=
{(1-\chi)s_-C_2(\rho)\over2}
 - s_+R_H.
```

Assume `B_{AFM}^*>0`. With the thick-window constants `q_-,n_+`, define the
AF-matched signal floor

```math
Sig_{{AFM}}
:=
\exp(-n_+A_{{AFM}}^*)
\left(1-\exp(-q_-B_{{AFM}}^*)\right).
```

### Definition 8K.2: AF-Matched Loss Gate

`P19-AFM-LOSS(L_{AFM})` holds when the decoration and transport losses on
the same AF-matched tower obey

```math
\limsup_j
\left(
\Delta_{{dec},j}^{bd}+T_{{loss},j}^{bd}
\right)
\le
L_{AFM}<\infty.
```

Using Section 8E, a sufficient explicit version is

```math
L_{AFM}
=
\exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1+T_*,
```

with `P19-DW-DEC(eta_*,c_\Delta^*)` and `P19-DW-TLOSS(T_*)`.

### Theorem 8K.3: AF-Matched Direct-Witness Closure

Assume:

1. the direct Paper-15 witness is same-ledger admissible;
2. the thick direct-witness branch holds with constants `q_-,n_+`;
3. the hypotheses of Theorem 8J.3 hold, so `B_{AFM}^*>0`;
4. `P19-AFM-LOSS(L_{AFM})`;
5. the strict AF-matched signal-minus-loss inequality

   ```math
   Sig_{AFM}>L_{AFM}.
   ```

Then

```math
c_{15}^{tail}>0.
```

Consequently the debited direct-witness reserve branch proves
`AYM-CONF-ACT-CRES-P16(c_R)` for every strict

```math
0<c_R<Sig_{AFM}-L_{AFM}.
```

Proof.

Theorem 8J.3 proves `P19-THICK-COEFF(A_*,B_*)` with
`A_*=A_{AFM}^*` and `B_*=B_{AFM}^*`. Theorem 8G.3 gives
`P19-DW-THETA(n_+A_{AFM}^*)` and `P19-DW-PHI(q_-B_{AFM}^*)`, so the direct
signal floor is `Sig_AFM`. The loss gate is exactly
`P19-DW-LOSS` with total ceiling `L_AFM`. Theorem 8B.9 gives
`c_{15}^{tail}>0` and the reserve export. `square`

### Theorem 8K.4: AF-Matched Direct-Witness Falsification

On the same declared AF-matched thick branch, the direct-witness reserve
route is falsified if any of the following hold:

1. AF area mismatch:

   ```math
   S_j/g_i^{-2}\to0
   \quad\text{or}\quad
   S_j/g_i^{-2}\to\infty;
   ```

2. coefficient error failure:

   ```math
   \liminf_j S_jB_j^+\le0
   \quad\text{or}\quad
   \limsup_j S_jA_j^-=\infty;
   ```

3. loss dominance:

   ```math
   \liminf_j
   \left(\Delta_{{dec},j}^{bd}+T_{{loss},j}^{bd}\right)
   \ge
   \limsup_j
   e^{-\Theta_j}(1-e^{-\Phi_j}).
   ```

Then this declared absolute direct-witness branch cannot supply
`c_{15}^{tail}>0`.

Proof.

Clause 1 is Theorem 8I.4. Clause 2 is Theorem 8H.6. Clause 3 is Theorem
8B.10 written on the AF-matched branch. `square`

### 8K.5 Final Direct-Witness Verdict

The strongest growing-window direct-witness closure currently available in
Paper 19 is:

```text
thick/co-scaling windows
+ AF-matched area S_j ~ g_i^{-2}
+ coefficient error R_H^opt < R_H^crit
+ decoration and transport losses below Sig_AFM
=> c_15^tail > 0.
```

The source papers currently provide the formulas and compatibility ledgers,
but not the actual estimates for `R_H^opt<R_H^crit` and
`P19-AFM-LOSS(L_AFM)` with `L_AFM<Sig_AFM`. Thus Paper 19 can finish the
direct-witness route as a complete conditional theorem and an obstruction
ledger. It cannot honestly declare an unconditional proof of actual
`4D SU(N)` confinement from the present source papers.

## 8L. Step 1a-XI: Prove Or Falsify The AF-Matched Loss Budget

The remaining AF-matched direct-witness source question is now purely scalar:
does the loss ledger stay below the certified signal floor `Sig_AFM` on the
same whole-process tower?

This section proves the exact loss-budget decision theorem and then checks
what is actually imported from Papers 15--16. The ontology is deliberately
thin: the only objects being compared are record-law debits. Gauge charts,
surface expansions, decorations, and transport decompositions are proof
coordinates for bounding those debits, not additional physical beables.

### Definition 8L.1: Sharp AF-Matched Loss Envelope

On the AF-matched branch of Section 8K, define the sharp upper loss envelope

```math
L_{AFM}^{sharp}
:=
\limsup_j
\left(
\Delta_{{dec},j}^{bd}+T_{{loss},j}^{bd}
\right).
```

Whenever component estimates are used, write

```math
\eta_{{dec},j}^{bd}
=
\eta_{{res},j}^{bd}+C_{{ch},j}Tail_{{CE},j},
```

```math
\Delta_{{dec},j}^{bd}
=
\exp\left(
{c_{\Delta,j}^*\eta_{{dec},j}^{bd}
\over
1-\eta_{{dec},j}^{bd}}
\right)-1,
```

and

```math
T_{{loss},j}^{bd}
=
T_{11,j}+T_{12,j}+T_{13,j}+T_{14,j}.
```

Here `T_11`, `T_12`, `T_13`, and `T_14` are exactly the Paper-15 transport
debits from Papers 11, 12, 13, and 14 respectively.

### Theorem 8L.2: Exact Loss-Budget Pass Criterion

Assume the AF-matched signal floor `Sig_AFM` of Definition 8K.1 is positive.
If

```math
L_{AFM}^{sharp}<Sig_{AFM},
```

then `P19-AFM-LOSS(L_AFM)` holds for some `L_AFM<Sig_AFM`. Consequently
Theorem 8K.3 applies and the direct Paper-15 witness proves
`c_15^{tail}>0`.

Proof.

Choose any number `L_AFM` with

```math
L_{AFM}^{sharp}<L_{AFM}<Sig_{AFM}.
```

By the definition of limsup,

```math
\limsup_j
\left(
\Delta_{{dec},j}^{bd}+T_{{loss},j}^{bd}
\right)
\le L_{AFM}.
```

This is exactly `P19-AFM-LOSS(L_AFM)`. Since `L_AFM<Sig_AFM`, Theorem 8K.3
gives the direct-witness closure. `square`

### Theorem 8L.3: Exact Failure Of The AF-Matched Sufficient Loss Gate

If

```math
L_{AFM}^{sharp}\ge Sig_{AFM},
```

then the AF-matched sufficient theorem of Section 8K cannot be applied with
the current certified signal floor `Sig_AFM`.

If, more strongly, there are actual tail bounds

```math
\liminf_j
\left(
\Delta_{{dec},j}^{bd}+T_{{loss},j}^{bd}
\right)
\ge B_-,
```

and

```math
\limsup_j e^{-\Theta_j}(1-e^{-\Phi_j})\le A^+,
```

with `B_- >= A^+`, then the direct Paper-15 witness is falsified in its
absolute-tail form:

```math
c_{15}^{tail}\le0.
```

Proof.

The first claim is immediate: Section 8K needs a strict number
`L_AFM<Sig_AFM` with the loss limsup below `L_AFM`. If the sharp limsup is
already at least `Sig_AFM`, no such strict number can be certified from
`Sig_AFM`.

The second claim is exactly Theorem 8B.10, with the actual signal upper
ceiling `A^+` and the actual loss lower floor `B_-`. `square`

### Theorem 8L.4: Component Source Theorem For The Loss Budget

Suppose the source papers supply constants

```math
\eta_{res}^*,\eta_{ch}^*,c_\Delta^*,
T_{11}^*,T_{12}^*,T_{13}^*,T_{14}^*
```

such that

```math
\limsup_j\eta_{{res},j}^{bd}\le\eta_{res}^*,
\qquad
\limsup_jC_{{ch},j}Tail_{{CE},j}\le\eta_{ch}^*,
```

```math
\eta_*:=\eta_{res}^*+\eta_{ch}^*<1,
\qquad
\limsup_jc_{\Delta,j}^*\le c_\Delta^*<\infty,
```

and

```math
\limsup_jT_{k,j}\le T_k^*
\qquad
(k=11,12,13,14).
```

Define

```math
T_*:=T_{11}^*+T_{12}^*+T_{13}^*+T_{14}^*
```

and

```math
L_{AFM}^{src}
:=
\exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1+T_*.
```

If

```math
L_{AFM}^{src}<Sig_{AFM},
```

then the AF-matched loss budget is proved.

Proof.

The first two limsup bounds give `P19-DW-DEC-COMP`, hence
`P19-DW-DEC(eta_*,c_\Delta^*)`. The four transport bounds give
`P19-DW-TLOSS-COMP`, hence `P19-DW-TLOSS(T_*)`. By Theorem 8E.5,

```math
L_{AFM}^{sharp}
\le
\exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1+T_*
=
L_{AFM}^{src}.
```

If `L_AFM^src<Sig_AFM`, then `L_AFM^sharp<Sig_AFM`, so Theorem 8L.2 applies.
`square`

### Corollary 8L.4A: Analytic Import Substitution In The Loss Budget

Assume `P19-AN-IMPORT(m)`. Then the residual-decoration component in
Theorem 8L.4 may be fixed to

```math
\eta_{res}^*:=\eta_{19}^{res}<1.
```

The residual collar/tail constants used in the local `SEL_0` row may also
be fixed to

```math
\Delta_{res}^*:=\Delta_{19}^{an}>0,
\qquad
K_{res}^*:=K_{19}^{an}<\infty.
```

Consequently, after the analytic import, the component loss budget has only
the following non-analytic ceilings left to prove:

```math
\limsup_j C_{ch,j}Tail_{CE,j}\le \eta_{ch}^*,
\qquad
\limsup_j c_{\Delta,j}^*\le c_\Delta^*,
\qquad
\limsup_j T_{k,j}\le T_k^*
\quad(k=11,12,13,14).
```

With

```math
\eta_*:=\eta_{19}^{res}+\eta_{ch}^*,
\qquad
T_*:=T_{11}^*+T_{12}^*+T_{13}^*+T_{14}^*,
```

the AF-matched loss budget passes whenever

```math
\eta_*<1,
\qquad
\exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1+T_*<Sig_{AFM}.
```

Proof.

The residual substitution is exactly Definition 0A.1. The remaining
statements are Theorem 8L.4 with
`eta_res^*` specialized to `eta_19^{res}`. The constants
`Delta_res^*` and `K_res^*` are not decoration losses; they are the
analytic tail constants used by the local collar estimates in Section
8J.24. All substitutions are scalar constants on the same pushed-forward
record law. `square`

### Corollary 8L.5: Small-Loss Form Of The Source Test

Let

```math
x_*:={c_\Delta^*\eta_*\over1-\eta_*}.
```

The component source theorem passes whenever

```math
x_*<\log(1+Sig_{AFM}-T_*),
\qquad
T_*<Sig_{AFM}.
```

Equivalently,

```math
\eta_*<
{\log(1+Sig_{AFM}-T_*)\over
c_\Delta^*+\log(1+Sig_{AFM}-T_*)}.
```

Proof.

The inequality `L_AFM^src<Sig_AFM` is

```math
e^{x_*}-1+T_*<Sig_{AFM}.
```

This is equivalent to

```math
e^{x_*}<1+Sig_{AFM}-T_*,
```

which first requires `T_*<Sig_AFM`, and then is equivalent to the displayed
logarithmic inequality. Solving
`c_\Delta^*\eta_*/(1-\eta_*) < log(1+Sig_AFM-T_*)` for `eta_*` gives the
last displayed bound. `square`

### Theorem 8L.6: Present Source-Paper Verdict On The Loss Budget

From the current Papers 15--16 alone, the AF-matched loss budget is not
unconditionally proved and not falsified.

What is proved is the following exact reduction:

```text
limsup eta_res,j^bd <= eta_res^*
+ limsup C_ch,j Tail_CE,j <= eta_ch^*
+ eta_res^* + eta_ch^* < 1
+ limsup c_Delta,j^* <= c_Delta^*
+ limsup T_k,j <= T_k^* for k=11,12,13,14
+ exp(c_Delta^* eta_*/(1-eta_*)) - 1 + sum_k T_k^* < Sig_AFM
=> AF-matched loss budget passes.
```

After `P19-AN-IMPORT(m)`, the residual component may be fixed to
`eta_res^*:=eta_19^{res}`. At this reduction stage, the remaining actual
estimates are:

```text
1. a cofinal character-tail conversion bound eta_ch^*;
2. a cofinal finite-battery constant bound c_Delta^*;
3. cofinal transport ceilings T_11^*, T_12^*, T_13^*, T_14^*;
4. the strict scalar comparison with
   eta_* = eta_19^{res} + eta_ch^*
   against Sig_AFM.
```

Paper 15 supplies the formulas for `eta_dec^bd`, `Delta_dec^bd`, and
`T_loss^bd`. Paper 16 supplies conditional closure theorems and compatibility
ledgers for those quantities. Paper 16 now supplies the residual analytic
ceiling once `P19-AN-IMPORT(m)` is verified. The following subsections close
the character-tail item by choosing a cofinal heat-kernel representation
cutoff and close the finite-battery constant under the uniform finite-template
decoration geometry `P19-FBTPL-DEC`. The last subsection then decomposes the
transport ceilings into component audits. After that, the undecided positive
constants are the sharp same-record component transport limsups needed to
decide

```math
L_{AFM}^{sharp}<Sig_{AFM}
```

or the stronger falsifying inequality of Theorem 8L.3.

Proof.

The positive direction is Theorem 8L.4. The negative direction would require
a lower loss floor and an upper signal ceiling as in Theorem 8L.3, or at
least an exact computation of `L_AFM^sharp` showing it is at or above the
certified signal floor. The source papers provide neither the upper constants
for a pass nor the lower constants for a falsification. Therefore the honest
status is undecided from the current sources, with the displayed finite list
of constants as the exact next target. `square`

### Definition 8L.7: Character-Tail Source Audit `P19-CHTAIL-AUDIT(eta_ch^*)`

After `P19-AN-AUDIT(m)` has supplied the residual component, the next
non-residual decoration source is the non-leading character tail.

`P19-CHTAIL-AUDIT(eta_ch^*)` holds when a cofinal representation/character
cutoff schedule has been fixed on the same pushed-forward Wilson-loop record
law and the Paper-15 character-tail constants satisfy

```math
\limsup_j C_{{ch},j}Tail_{{CE},j}
\le
\eta_{ch}^*.
```

Here `Tail_CE,j` is the Paper-15 coefficient-entry tail after the selected
representation cutoff, and `C_ch,j` is the finite conversion constant from
that coefficient-entry tail to the residual-decoration activity used by the
same finite battery. The audit is same-record: the cutoff schedule, the
coefficient-entry tail, and the decoration activity must be measured after
the same record pushforward.

Define the sharp audited character-tail ceiling

```math
\eta_{ch}^{sharp}
:=
\inf_{\mathcal R}
\limsup_j C_{{ch},j}^{\mathcal R}Tail_{{CE},j}^{\mathcal R},
```

where the infimum is over the declared admissible cofinal character-cutoff
schedules `\mathcal R`.

### Theorem 8L.8: Exact Character-Tail Decision After Analytic Import

Assume `P19-AN-AUDIT(m)`, hence by Theorem 0A.4
`eta_res^*:=eta_19^{res}` is available. The character-tail part of the
decoration ledger can pass exactly when there is an admissible schedule with

```math
\eta_{19}^{res}
+
\limsup_j C_{{ch},j}Tail_{{CE},j}
<1.
```

Equivalently, the sharp ceiling must satisfy

```math
\eta_{ch}^{sharp}<1-\eta_{19}^{res}.
```

If instead one proves

```math
\eta_{ch}^{sharp}\ge1-\eta_{19}^{res},
```

then the Paper-15 decoration activity cannot be made subcritical by changing
only the admissible character cutoff schedule.

Proof.

The residual component is fixed by Theorem 0A.4. The Paper-15 decoration
activity is the sum of the residual activity and the character-tail
conversion activity. Therefore subcriticality is exactly
`eta_19^{res}+eta_ch<1`. Taking the infimum over admissible schedules gives
the sharp criterion. The negative statement is only a failure of this
character-cutoff route; it does not falsify confinement unless combined with
the lower-loss and signal-ceiling hypotheses of Theorem 8L.3. `square`

### Theorem 8L.8A: Heat-Kernel Character Cutoff Proves `P19-CHTAIL-AUDIT`

Assume the clean `SEL_0` analytic import of Corollary 0A.7, so that

```math
0\le\eta_{19}^{res}<1.
```

Choose any strict character-tail budget

```math
0<\eta_{ch}^*<1-\eta_{19}^{res}.
```

Use the converted heat-kernel character-tail normalization of Paper 16
Definition 9O.2: choose `q_ch` large enough to absorb the finite
character-to-record norm, finite Clebsch-Gordan multiplicities, and local
record-label overhead of the Paper-15 decoration battery, so that on the
same pushed-forward record law

```math
C_{{ch},j}Tail_{{CE},j}
\le
Tail_{ch}(t_{i(j)},R_j)
```

for every cofinal index `j`. Let `C_W,nu_W,R_W,t_W` be the Weyl-Casimir tail
constants of Paper 16 Lemma 9O.3 for this enlarged `q_ch` and the available
heat-kernel decay constant `a_ch>0`. Choose the cofinal representation
cutoff schedule

```math
R_j
\ge
\max\left\{
{R_W\over t_{i(j)}},
{2\over a_ch\,t_{i(j)}}
\left[
\nu_W\log {1\over t_{i(j)}}
+\log {C_W\over\eta_{ch}^*}
\right]
\right\}
```

for all sufficiently fine nodes. Then

```math
\limsup_j C_{{ch},j}Tail_{{CE},j}
\le
\eta_{ch}^*,
```

so `P19-CHTAIL-AUDIT(eta_ch^*)` holds, and

```math
\eta_{19}^{res}+\eta_{ch}^*<1.
```

Proof.

The finite block/decorated-record template has only finitely many local
character products and finitely many readout labels at each fixed cutoff.
For compact `SU(N)`, Weyl dimension growth and fixed-degree tensor product
multiplicities are polynomial in the highest weight. Increasing `q_ch` in
Paper 16 Definition 9O.2 absorbs exactly this polynomial overhead and the
finite character-to-record norm into the weighted tail. This gives the first
displayed domination after pushforward to the scalar record law.

For sufficiently fine nodes, `t_{i(j)}<=t_W` and the chosen `R_j` satisfies
`R_j>=R_W/t_{i(j)}`. Paper 16 Lemma 9O.3 gives

```math
Tail_{ch}(t_{i(j)},R_j)
\le
C_W t_{i(j)}^{-\nu_W}
\exp\left(-{a_ch\over2}t_{i(j)}R_j\right).
```

Substituting the second lower bound on `R_j` yields

```math
C_W t_{i(j)}^{-\nu_W}
\exp\left(
-\nu_W\log {1\over t_{i(j)}}
-\log {C_W\over\eta_{ch}^*}
\right)
=
\eta_{ch}^*.
```

Thus `C_ch,j Tail_CE,j<=eta_ch^*` eventually, hence the limsup bound holds.
The cutoff is cofinal because `t_i->0` on the heat-kernel continuum tail and
therefore `R_j->infinity`. The strict KP margin is the initial choice
`eta_ch^*<1-eta_19^{res}`. `square`

### Corollary 8L.8B: Canonical Half-Margin Choice

Under the hypotheses of Theorem 8L.8A, the canonical choice

```math
\eta_{ch}^*
:=
{1-\eta_{19}^{res}\over2}
```

proves `P19-CHTAIL-AUDIT(eta_ch^*)` and gives the explicit reserve

```math
1-\eta_{19}^{res}-\eta_{ch}^*
=
{1-\eta_{19}^{res}\over2}
>0.
```

Proof.

The chosen `eta_ch^*` lies strictly between `0` and `1-eta_19^{res}`.
Apply Theorem 8L.8A. `square`

### Definition 8L.9: Finite-Battery Constant Audit `P19-CDELTA-AUDIT(c_Delta^*)`

Once the character-tail activity is bounded, the next source constant is the
finite-battery decoration-growth constant. `P19-CDELTA-AUDIT(c_Delta^*)`
holds when the same cofinal battery schedule satisfies

```math
\limsup_j c_{\Delta,j}^*
\le
c_\Delta^*
<\infty.
```

The sharp audited finite-battery ceiling is

```math
c_\Delta^{sharp}
:=
\inf_{\mathcal B}
\limsup_j c_{\Delta,j}^{*,\mathcal B},
```

where the infimum is over the declared admissible cofinal finite-battery
schedules `\mathcal B` compatible with the character cutoff and the same
record law.

### Definition 8L.9A: Uniform Finite-Template Decoration Geometry

`P19-FBTPL-DEC(C_\xi,C_{\xi'})` holds when the cofinal Paper-19 Creutz and
decoration batteries use one finite list of block/collar surface templates
after rescaling by the window unit. Equivalently:

1. every Creutz loop slot is assembled from the same finite set of local
   corner, edge, and plaquette-collar types;
2. the decoration gas is the same pushed-forward finite record law used in
   `P19-AN-AUDIT(m)` and `P19-CHTAIL-AUDIT(eta_ch^*)`;
3. the collar excess counted per unit excess area is bounded by `C_\xi`;
4. the endpoint/corner collar excess not charged to area is bounded by
   `C_{\xi'}`;
5. the bounds are uniform along the cofinal window schedule.

No geometric surface is exported as ontology. The templates only certify the
two scalar Paper-15 constants `c_xi,j^*` and `c_xip,j^*`.

### Lemma 8L.9A.1: Centered Square Thick Windows Have Uniform Decoration Templates

For the centered square thick/co-scaling `SEL_0` schedule

```text
R_j=T_j=L_j,
sigma_j=floor(alpha L_j),
0<alpha<1,
```

with the fixed block/collar convention used in Sections 8F--8J, there are
finite constants

```text
C_xi^{SEL0}, C_xip^{SEL0}<infinity
```

such that

```text
P19-FBTPL-DEC(C_xi^{SEL0},C_xip^{SEL0})
```

holds.

Proof.

The square thick window is built from one lattice-aligned rectangular
template, one fixed Creutz decrement rule, and one fixed collar convention.
After rescaling by the window unit, every loop slot has only the following
local boundary types: straight edge, interior plaquette collar, convex
corner, concave corner created by the Creutz subtraction, and endpoint/corner
collar. This is a finite list independent of `j`.

The number of edge/collar cells charged per unit excess area is uniformly
bounded because the collar width is fixed in block units while the excess
area grows by adding finitely many local plaquette templates. Let the maximum
over the finite list of local area-charged templates be `C_xi^{SEL0}`.
Likewise, the endpoint and corner terms are not charged to excess area, but
there are only finitely many corners and endpoint slots in the four Creutz
loops, all drawn from the same finite list. Let their maximum total excess
be `C_xip^{SEL0}`.

The decoration gas and record map are the same pushed-forward law used in
Theorem 0A.6 and Theorem 8L.8A. Thus all five clauses of Definition 8L.9A
hold with these constants. `square`

### Theorem 8L.9B: Uniform Finite Templates Prove `P19-CDELTA-AUDIT`

Assume `P19-FBTPL-DEC(C_\xi,C_{\xi'})` on the same cofinal battery schedule
used by the analytic import and character-tail audit. Then

```math
\limsup_j c_{\Delta,j}^*
\le
C_\xi+C_{\xi'}
<\infty.
```

Consequently

```text
P19-CDELTA-AUDIT(c_Delta^*)
```

holds with

```math
c_\Delta^*:=C_\xi+C_{\xi'}.
```

Proof.

Paper 15 Definition 9A.1 gives

```math
c_{\Delta,j}^*
=
c_{\xi,j}^*+c_{\xi',j}^*,
```

where `c_xi,j^*` and `c_xip,j^*` are the finite maxima of the two
decoration-growth constants over the declared Creutz battery at row `j`.
Clauses 1--5 of `P19-FBTPL-DEC` say exactly that those finite maxima are
computed from one finite list of local surface/collar templates and are
uniformly bounded by `C_\xi` and `C_{\xi'}` on the cofinal tail. Therefore

```math
c_{\Delta,j}^*
\le
C_\xi+C_{\xi'}
```

eventually, and the displayed limsup bound follows. `square`

### Corollary 8L.9C: Decoration Debit Closed After The Three Audits

Assume:

```text
P19-AN-AUDIT(m),
P19-CHTAIL-AUDIT(eta_ch^*),
P19-FBTPL-DEC(C_xi,C_xip),
eta_19^res+eta_ch^*<1.
```

Set

```math
c_\Delta^*:=C_\xi+C_{\xi'},
\qquad
\eta_*:=\eta_{19}^{res}+\eta_{ch}^*.
```

Then

```math
\limsup_j\Delta_{{dec},j}^{bd}
\le
\exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1.
```

Proof.

Theorem 8L.9B proves `P19-CDELTA-AUDIT(c_Delta^*)`. Apply Theorem 8L.10.
`square`

### Corollary 8L.9C.1: Centered Square Branch Closes `P19-CDELTA-AUDIT`

On the centered square thick/co-scaling `SEL_0` branch,

```text
P19-CDELTA-AUDIT(c_Delta^*)
```

holds with

```math
c_\Delta^*
:=
C_\xi^{SEL0}+C_{\xi'}^{SEL0}.
```

Consequently, with the canonical character-tail half-margin

```math
\eta_{ch}^*={1-\eta_{19}^{res}\over2},
\qquad
\eta_*={1+\eta_{19}^{res}\over2},
```

the decoration debit is bounded by

```math
\limsup_j\Delta_{{dec},j}^{bd}
\le
\exp\left(
{(C_\xi^{SEL0}+C_{\xi'}^{SEL0})\eta_*
\over
1-\eta_*}
\right)-1.
```

Proof.

Lemma 8L.9A.1 gives `P19-FBTPL-DEC(C_xi^{SEL0},C_xip^{SEL0})`. Theorem
8L.9B gives `P19-CDELTA-AUDIT` with the displayed `c_Delta^*`. Corollary
8L.8B gives the canonical half-margin character-tail choice. Corollary
8L.9C then gives the decoration debit bound. `square`

### Theorem 8L.9D: Exact Obstruction To The Finite-Battery Constant Audit

For the declared cofinal battery schedule, `P19-CDELTA-AUDIT(c_Delta^*)`
fails for every finite `c_Delta^*` exactly when

```math
\limsup_j(c_{\xi,j}^*+c_{\xi',j}^*)=\infty.
```

Equivalently, either the collar excess per unit area, the endpoint/corner
excess, or the finite-template compatibility with the common record law is
not uniformly controlled on the cofinal tail.

Proof.

The first statement is the definition of `P19-CDELTA-AUDIT` together with
Paper 15's identity `c_Delta,j^*=c_xi,j^*+c_xip,j^*`. The second statement
unpacks the only possible sources of divergence in those finite maxima:
unbounded area collar multiplicity, unbounded endpoint/corner excess, or a
change of finite-battery template/readout that prevents a common uniform
maximum. `square`

### Theorem 8L.10: First Two Loss-Source Audits Prove The Decoration Bound

Assume:

```text
P19-AN-AUDIT(m),
P19-CHTAIL-AUDIT(eta_ch^*),
P19-CDELTA-AUDIT(c_Delta^*),
eta_19^{res}+eta_ch^*<1.
```

Then the Paper-15 decoration bound holds with

```math
\eta_*:=\eta_{19}^{res}+\eta_{ch}^*
```

and

```math
D_{dec}^*
=
\exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1.
```

In particular,

```math
\limsup_j\Delta_{{dec},j}^{bd}
\le
D_{dec}^*.
```

Proof.

Theorem 0A.4 gives the residual limsup bound
`limsup_j eta_res,j^bd <= eta_19^res`. Definition 8L.7 gives the
character-tail limsup bound, so the total decoration activity has limsup at
most `eta_*<1`. Definition 8L.9 gives the finite-battery constant bound.
Substitution into the Paper-15 decoration formula

```math
\Delta_{{dec},j}^{bd}
=
\exp\left(
{c_{\Delta,j}^*\eta_{{dec},j}^{bd}
\over
1-\eta_{{dec},j}^{bd}}
\right)-1
```

and monotonicity of the function
`(c,eta) -> exp(c eta/(1-eta))-1` on `c>=0`, `0<=eta<1` gives the result.
`square`

### Definition 8L.11: Component Transport Audits

The four remaining transport ceilings are audited on the same cofinal
finite-battery record law used by `P19-AN-AUDIT`, `P19-CHTAIL-AUDIT`, and
`P19-CDELTA-AUDIT`. For each row `j`, the Paper-15 transport ledger is
partitioned as

```math
T_{{loss},j}^{bd}
=
T_{11,j}+T_{12,j}+T_{13,j}+T_{14,j},
```

with the Paper-15 meanings from Definition 11A.1. The component audits are:

1. `P19-T11-AUDIT(T_{11}^*)` holds when

   ```math
   \limsup_jT_{11,j}\le T_{11}^*<\infty.
   ```

   The audited source split is

   ```math
   T_{11,j}
   \le
   \tau_{11,j}^{loc}
   +\tau_{11,j}^{RP}
   +\tau_{11,j}^{Cov}
   +\tau_{11,j}^{gauge}.
   ```

   These four terms are, respectively, the Paper-11/Paper-16 local-RG law
   drift, reflection-positivity transport, Euclidean-covariance transport,
   and gauge-reconstruction/chart transport, all evaluated after pushforward
   to the declared scalar record battery.

2. `P19-T12-AUDIT(T_{12}^*)` holds when

   ```math
   \limsup_jT_{12,j}\le T_{12}^*<\infty.
   ```

   The audited source split is

   ```math
   T_{12,j}
   \le
   \tau_{12,j}^{per}
   +\tau_{12,j}^{cusp}
   +\tau_{12,j}^{smear}
   +\tau_{12,j}^{app}.
   ```

   These are the Paper-12 perimeter, cusp, smearing-removal, and
   loop-approximant/readout losses. If a source theorem bundles these with
   projective, regulator, or volume terms, the common debit register must
   assign each bundled term to exactly one of `T_11`, `T_12`, or `T_14`; no
   term may be charged twice.

3. `P19-T13-AUDIT(T_{13}^*)` holds when

   ```math
   \limsup_jT_{13,j}\le T_{13}^*<\infty.
   ```

   The audited source split is

   ```math
   T_{13,j}
   \le
   \tau_{13,j}^{surf}
   +\tau_{13,j}^{entry}
   +\tau_{13,j}^{exact}.
   ```

   These are the Paper-13 surface-polymer transport loss, the strong-block or
   exact-entry transport loss, and the exact whole-process scalar-entry
   comparison loss. Decoration activity itself is not included here; it is
   already charged in `Delta_dec,j^bd`.

4. `P19-T14-AUDIT(T_{14}^*)` holds when

   ```math
   \limsup_jT_{14,j}\le T_{14}^*<\infty.
   ```

   The audited source split is the Paper-14 whole-process finite-block
   transport norm:

   ```math
   T_{14,j}\le \|E_{14}(\eta_j)\|_{tr}.
   ```

   Hence the canonical Paper-14 ceiling is `T_14^*=E_14^*`, whenever the
   exported Paper-14 package supplies
   `limsup_j ||E_14(eta_j)||_tr <= E_14^*`.

All four audits are operational statements about the same finite scalar
records. They do not introduce a hidden field ontology and they do not permit
composition of unobserved subprocess kernels.

### Definition 8L.11A: Component Source Packages

For concise references, write the four source packages as follows.

`P19-T11-SRC(A_{11}^{loc},A_{11}^{RP},A_{11}^{Cov},A_{11}^{gauge})` holds
when the same record law satisfies

```math
\limsup_j\tau_{11,j}^{loc}\le A_{11}^{loc},
\quad
\limsup_j\tau_{11,j}^{RP}\le A_{11}^{RP},
\quad
\limsup_j\tau_{11,j}^{Cov}\le A_{11}^{Cov},
\quad
\limsup_j\tau_{11,j}^{gauge}\le A_{11}^{gauge},
```

with all four right-hand sides finite. The intended imports are Paper 11
local-RG and gauge-reconstruction control together with Paper 16
`HK-RG-PROJ-LEDGER`, `HK-RP-LEDGER`, `HK-COV-LEDGER`, `HK-REG-CLOSE`, and
`HK-WP-CLOSE`.

`P19-T12-SRC(A_{12}^{per},A_{12}^{cusp},A_{12}^{smear},A_{12}^{app})` holds
when

```math
\limsup_j\tau_{12,j}^{per}\le A_{12}^{per},
\quad
\limsup_j\tau_{12,j}^{cusp}\le A_{12}^{cusp},
\quad
\limsup_j\tau_{12,j}^{smear}\le A_{12}^{smear},
\quad
\limsup_j\tau_{12,j}^{app}\le A_{12}^{app},
```

with finite right-hand sides. The intended imports are Paper 12's
perimeter/cusp counterterm ledger, smearing-removal ledger, and loop-modulus
theorem, transported through Paper 16 `HK-LC-TRANSPORT`.

`P19-T13-SRC(A_{13}^{surf},A_{13}^{entry},A_{13}^{exact})` holds when

```math
\limsup_j\tau_{13,j}^{surf}\le A_{13}^{surf},
\quad
\limsup_j\tau_{13,j}^{entry}\le A_{13}^{entry},
\quad
\limsup_j\tau_{13,j}^{exact}\le A_{13}^{exact},
```

with finite right-hand sides. The intended imports are Paper 13's
surface-polymer entry estimates, exact RG-entry theorem, strong-block entry
package, and the Paper-15 surface/Creutz transport ledger.

`P19-T14-SRC(E_{14}^*)` holds when Paper 14 exports a whole-process
finite-block transport budget with

```math
\limsup_j\|E_{14}(\eta_j)\|_{tr}\le E_{14}^*<\infty.
```

Each source package includes a same-ledger clause: the constants must be
computed after pushing the same cutoff law to the same record battery, with
the same loop approximants, counterterm branches, regulator maps, and
finite-battery restriction maps.

### Definition 8L.11A.1: Common-Record Transport Audit `P19-TR-COMMON`

`P19-TR-COMMON` holds when the four transport ceilings are evaluated on one
common whole-process record tower and one disjoint debit register. Concretely:

1. `P19-TOWER` is fixed, including the frozen law `Law_*`, the cofinal finite
   record algebras `F_j`, the restriction maps `rho_j`, and the debit
   register.
2. The Paper-16 common heat-kernel tower `T_HK` of Definition 9Z.1 is
   identified with the Paper-19 tower after pushforward:

   ```text
   Gamma_j = rho_j(Law_*),
   B_j = F_j or a declared common refinement,
   Pi_{j->k} = declared restriction/comparison maps.
   ```

3. `HK-WP-CLOSE` holds for the Paper-16 certificates that feed the transport
   ceilings, so the projective, regulator, RP/covariance, loop-continuity,
   nontriviality, and `X_15` ledgers use the same batteries, maps, loop
   approximants, counterterm branches, and constants.
4. The Paper-14 export chain `eta_j` is read on this same finite battery
   family; the entries of `E_14(eta_j)` are charged only to `T_14` unless a
   declared shared value is used and counted once.
5. Every source defect appearing in more than one paper has one declared
   scalar value and one debit assignment among `T_11`, `T_12`, `T_13`,
   `T_14`, or `Delta_dec`.
6. No estimate uses an unrecorded partial kernel or a gauge-fixed process as
   an independent dynamical object; proof coordinates are eliminated into
   scalar inequalities for the pushed-forward record laws.

This is the transport version of Barandes alignment: the proof compares
observable record laws produced by one whole process, not composed
subprocesses.

### Lemma 8L.11A.2: Paper-16 `HK-WP-CLOSE` Supplies The Common Transport Audit

Assume:

```text
P19-TOWER,
HK-WP-CLOSE on the identified Paper-16 tower T_HK,
same-battery Paper-14 export chain eta_j,
declared disjoint debit assignment.
```

Then `P19-TR-COMMON` holds.

Proof.

`P19-TOWER` supplies the frozen law, finite restrictions, and debit register.
Paper 16 Definition 9Z.1 supplies the common heat-kernel tower, and the
identification in clause 2 makes its pushed-forward laws the Paper-19 laws
`rho_j(Law_*)`. Paper 16 Definition 9Z.2 requires all certificates feeding
`HK-X15-CLOSE`, projectivity, regulator closure, RP/covariance,
loop-continuity, and nontriviality to use the same batteries, maps,
counterterms, loop approximants, and constants. Definition 9Z.3 forbids
hidden partial-kernel composition, and Definition 9Z.4 requires every loss to
be assigned to one declared ledger entry or shared with the same value.

The same-battery Paper-14 export clause attaches `E_14(eta_j)` to this tower
rather than to a separate finite-block process. These are exactly the six
clauses of `P19-TR-COMMON`. `square`

### Definition 8L.11A.3: Paper-14 Transport Export `P19-P14-EXPORT(E_14^*)`

`P19-P14-EXPORT(E_14^*)` holds when Paper 14 exports, on the same cofinal
finite-battery chain used by `P19-TR-COMMON`, a finite whole-process
transport norm satisfying

```math
\limsup_j\|E_{14}(\eta_j)\|_{tr}\le E_{14}^*<\infty.
```

Here `E_14(eta_j)` is the Paper-14 defect vector and `||.||_tr` is the
Paper-14 transport norm with weights dominating the finite record
Lipschitz constants exported to Paper 15.

### Theorem 8L.11A.4: Paper-14 Export Closes The `T_14` Source Package

Assume `P19-TR-COMMON` and `P19-P14-EXPORT(E_14^*)`. Then

```text
P19-T14-SRC(E_14^*)
```

holds, and consequently

```text
P19-T14-AUDIT(E_14^*)
```

holds.

Proof.

`P19-TR-COMMON` supplies the same-ledger clause required in Definition
8L.11A: the Paper-14 transport vector is evaluated after pushforward to the
same finite record law, with the same batteries and debit register. The
Paper-14 export gives the only numerical clause:

```math
\limsup_j\|E_{14}(\eta_j)\|_{tr}\le E_{14}^*<\infty.
```

Therefore `P19-T14-SRC(E_14^*)` holds. By Definition 8L.11, the rowwise
Paper-14 component satisfies

```math
T_{14,j}\le\|E_{14}(\eta_j)\|_{tr}.
```

Taking limsup gives

```math
\limsup_jT_{14,j}\le E_{14}^*,
```

which is `P19-T14-AUDIT(E_14^*)`. `square`

### Definition 8L.11A.5: Reduced `T_11` Transport Ledger

Assume `P19-TR-COMMON`. The reduced `T_11` ledger is the part of the
Paper-11/Paper-16 transport ledger not already charged to `T_12`, `T_13`,
`T_14`, or `Delta_dec`. For each row `j`, define shell tails

```math
R_{11,j}^{loc}
:=
\sum_{k\ge j}
L_j^{rec}
\left(
\eta_{locRG,k}^{B_j}
+\eta_{prec,j,k}^{(11)}
\right),
```

```math
R_{11,j}^{RP}
:=
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
R_{11,j}^{Cov}
:=
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
R_{11,j}^{gauge}
:=
\sum_{k\ge j}
\left(
\eta_{chart,j,k}^{(11)}
+\eta_{gauge-rec,j,k}^{(11)}
\right).
```

The superscript `(11)` means that the debit register assigns that source
term to `T_11`. The superscript `(11,red)` means the perimeter/cusp part has
already been removed and, if nonzero, is charged only to `T_12`. The reduced
`T_11` source ledger

```text
P19-T11-LEDGER(A_11^loc,A_11^RP,A_11^Cov,A_11^gauge)
```

holds when

```math
\limsup_jR_{11,j}^{loc}\le A_{11}^{loc},
\quad
\limsup_jR_{11,j}^{RP}\le A_{11}^{RP},
\quad
\limsup_jR_{11,j}^{Cov}\le A_{11}^{Cov},
\quad
\limsup_jR_{11,j}^{gauge}\le A_{11}^{gauge},
```

with finite right-hand sides, and when the rowwise Paper-15 component obeys

```math
T_{11,j}
\le
R_{11,j}^{loc}+R_{11,j}^{RP}+R_{11,j}^{Cov}+R_{11,j}^{gauge}.
```

The terms are imported from Paper 16 `HK-RG-PROJ-LEDGER`,
`HK-RP-LEDGER`, `HK-COV-LEDGER`, `HK-REG-CLOSE`, and `HK-WP-CLOSE`, with
the Paper-11 local-RG residual supplying `eta_locRG`.

### Theorem 8L.11A.6: Reduced `T_11` Ledger Closes `P19-T11-SRC`

If `P19-TR-COMMON` and

```text
P19-T11-LEDGER(A_11^loc,A_11^RP,A_11^Cov,A_11^gauge)
```

hold, then

```text
P19-T11-SRC(A_11^loc,A_11^RP,A_11^Cov,A_11^gauge)
```

holds. Consequently

```math
\limsup_jT_{11,j}
\le
A_{11}^{loc}+A_{11}^{RP}+A_{11}^{Cov}+A_{11}^{gauge}.
```

Proof.

`P19-TR-COMMON` supplies the same-record and disjoint-debit clauses. The
definition of `P19-T11-LEDGER` supplies the four finite limsup bounds and the
rowwise domination of `T_11,j` by the four reduced tails. Limsup
subadditivity gives the displayed bound. This is exactly `P19-T11-SRC`.
`square`

### Definition 8L.11A.7: Reduced `T_12` Loop-Transport Ledger

Assume `P19-TR-COMMON`. The reduced `T_12` ledger is the loop-side part of
Paper 12/Paper 16 `HK-LC-TRANSPORT`, after removing projective, regulator,
finite-volume, and Paper-14 whole-process defects already charged elsewhere.
For each row `j`, define

```math
R_{12,j}^{per}:=\sum_{k\ge j}\eta_{perLC,j,k},
\qquad
R_{12,j}^{cusp}:=\sum_{k\ge j}\eta_{cuspLC,j,k},
```

```math
R_{12,j}^{smear}:=\sum_{k\ge j}\eta_{smearLC,j,k},
```

and

```math
R_{12,j}^{app}
:=
\sum_{k\ge j}
\left(
\eta_{P12,j,k}
+\eta_{appLC,j,k}^{(12)}
+\eta_{binLC,j,k}^{(12)}
\right).
```

The source terms are exactly the Paper-12 perimeter/cusp counterterm
transport, smearing-removal transport, and loop-approximant/readout
transport on the pushed-forward record law. The reduced `T_12` source ledger

```text
P19-T12-LEDGER(A_12^per,A_12^cusp,A_12^smear,A_12^app)
```

holds when

```math
\limsup_jR_{12,j}^{per}\le A_{12}^{per},
\quad
\limsup_jR_{12,j}^{cusp}\le A_{12}^{cusp},
\quad
\limsup_jR_{12,j}^{smear}\le A_{12}^{smear},
\quad
\limsup_jR_{12,j}^{app}\le A_{12}^{app},
```

with finite right-hand sides, and

```math
T_{12,j}
\le
R_{12,j}^{per}+R_{12,j}^{cusp}
+R_{12,j}^{smear}+R_{12,j}^{app}.
```

### Theorem 8L.11A.8: Reduced `T_12` Ledger Closes `P19-T12-SRC`

If `P19-TR-COMMON` and

```text
P19-T12-LEDGER(A_12^per,A_12^cusp,A_12^smear,A_12^app)
```

hold, then

```text
P19-T12-SRC(A_12^per,A_12^cusp,A_12^smear,A_12^app)
```

holds. Consequently

```math
\limsup_jT_{12,j}
\le
A_{12}^{per}+A_{12}^{cusp}+A_{12}^{smear}+A_{12}^{app}.
```

Proof.

The loop-transport ledger is already expressed in the four Paper-12 buckets
used by Definition 8L.11A.7. `P19-TR-COMMON` ensures that the projective,
regulator, and finite-volume terms excluded from the reduced ledger are
charged elsewhere and not silently discarded. The four finite limsup bounds
and the rowwise domination of `T_12,j` give the conclusion by limsup
subadditivity. `square`

### Definition 8L.11A.9: Reduced `T_13` Surface/Entry Transport Ledger

Assume `P19-TR-COMMON`. The reduced `T_13` ledger is the Paper-13
surface-polymer and exact-entry transport loss after excluding decoration
activity already charged in `Delta_dec,j^bd`. For each row `j`, let
`C in B_{CR,j}` range over the four Creutz loops in the declared finite
battery and set

```math
S_{13,j}^{surf}
:=
\max_{C\in B_{CR,j}}
A_Ce^{\xi'_C}u_{\rho,s_0}^{N(C)}
{B_Cu_{\rho,s_0}\over1-B_Cu_{\rho,s_0}},
```

where the constants are the Paper-13 surface-polymer entry constants from
Definition 7.30L, evaluated on the pushed-forward scalar closed-loop record.
Let `R_{13,j}^{entry}` be the finite strong-block/exact-entry transport tail
from the actual-continuum entry package, and let `R_{13,j}^{exact}` be the
finite convergence/comparison tail for replacing the cutoff block record by
the exact whole-process scalar entry record.

The reduced `T_13` source ledger

```text
P19-T13-LEDGER(A_13^surf,A_13^entry,A_13^exact)
```

holds when

```math
\limsup_jS_{13,j}^{surf}\le A_{13}^{surf},
\quad
\limsup_jR_{13,j}^{entry}\le A_{13}^{entry},
\quad
\limsup_jR_{13,j}^{exact}\le A_{13}^{exact},
```

with finite right-hand sides, and

```math
T_{13,j}
\le
S_{13,j}^{surf}+R_{13,j}^{entry}+R_{13,j}^{exact}.
```

The inequality `B_Cu_{\rho,s_0}<1` is part of the Paper-13 entry estimate.
If it fails on a cofinal tail, `P19-T13-LEDGER` fails.

### Theorem 8L.11A.10: Reduced `T_13` Ledger Closes `P19-T13-SRC`

If `P19-TR-COMMON` and

```text
P19-T13-LEDGER(A_13^surf,A_13^entry,A_13^exact)
```

hold, then

```text
P19-T13-SRC(A_13^surf,A_13^entry,A_13^exact)
```

holds. Consequently

```math
\limsup_jT_{13,j}
\le
A_{13}^{surf}+A_{13}^{entry}+A_{13}^{exact}.
```

Proof.

The surface term is exactly the Paper-13 nonminimal-sheet tail estimate from
Theorem 7.30M, maximized over the finite Creutz battery. The entry and exact
comparison terms are the remaining same-record defects needed to pass from
the surface-polymer expansion to the exact scalar RG-entry record. By
definition these three terms dominate `T_13,j`, and their limsups are finite.
Limsup subadditivity gives the displayed inequality. The common-record audit
ensures no decoration activity is double counted: decoration is paid through
`Delta_dec,j^bd`, not through `T_13`. `square`

### Theorem 8L.11A.11: Completed Transport Ledger And Scalar AFM Comparison

Assume:

```text
P19-AN-AUDIT(m),
P19-CHTAIL-AUDIT(eta_ch^*),
P19-CDELTA-AUDIT(c_Delta^*),
P19-TR-COMMON,
P19-T11-LEDGER(A_11^loc,A_11^RP,A_11^Cov,A_11^gauge),
P19-T12-LEDGER(A_12^per,A_12^cusp,A_12^smear,A_12^app),
P19-T13-LEDGER(A_13^surf,A_13^entry,A_13^exact),
P19-P14-EXPORT(E_14^*).
```

Set

```math
\eta_*:=\eta_{19}^{res}+\eta_{ch}^*,
```

```math
D_{dec}^*
:=
\exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1,
```

and

```math
T_*^{src}
:=
A_{11}^{loc}+A_{11}^{RP}+A_{11}^{Cov}+A_{11}^{gauge}
+A_{12}^{per}+A_{12}^{cusp}+A_{12}^{smear}+A_{12}^{app}
+A_{13}^{surf}+A_{13}^{entry}+A_{13}^{exact}
+E_{14}^*.
```

If

```math
\eta_*<1
```

and the final scalar comparison passes,

```math
D_{dec}^*+T_*^{src}<Sig_{AFM},
```

then the AF-matched direct-witness loss budget passes, hence
`c_15^{tail}>0` by Theorem 8K.3.

If

```math
D_{dec}^*+T_*^{src}\ge Sig_{AFM},
```

then this sufficient theorem does not decide the route. A genuine
falsification additionally requires an actual signal upper ceiling
`Sig_AFM^+` and a lower loss floor satisfying

```math
\limsup_j e^{-\Theta_j}(1-e^{-\Phi_j})\le Sig_{AFM}^+,
\qquad
\liminf_j(\Delta_{dec,j}^{bd}+T_{loss,j}^{bd})
\ge Sig_{AFM}^+.
```

Under those stronger inequalities, the AF-matched direct-witness route is
falsified for the declared tower.

Proof.

The first three assumptions and Theorem 8L.10 give
`limsup_j Delta_dec,j^bd <= D_dec^*`. Theorems 8L.11A.6, 8L.11A.8,
8L.11A.10, and 8L.11A.4 prove the four component source packages and audits,
with total transport ceiling `T_*^{src}`. Theorem 8L.11C gives
`P19-DW-TLOSS(T_*^{src})`, so

```math
L_{AFM}^{sharp}
\le
D_{dec}^*+T_*^{src}.
```

If this is strictly below `Sig_AFM`, Theorem 8L.2 proves the AF-matched loss
budget and Theorem 8K.3 gives `c_15^{tail}>0`. If the source upper bound is
not below `Sig_AFM`, this proof route has no strict loss margin and therefore
does not decide the theorem. The final falsification statement is exactly the
lower-loss/upper-signal branch of Theorem 8L.3. `square`

### Definition 8L.11A.12: Final Source Worksheet `P19-FINAL-SRC-WORKSHEET`

The final Paper-19 source worksheet is the following single scalar ledger,
all computed on the same record tower certified by `P19-TR-COMMON`.

| Slot | Source | Meaning | Status in this paper |
| --- | --- | --- | --- |
| `Sig_AFM` | Definition 8K.1 | AF-matched signal floor | formula fixed |
| `eta_19^res` | Theorem 0A.4 | residual decoration activity | imported by `P19-AN-AUDIT(m)` |
| `eta_ch^*` | Theorem 8L.8A | character-tail activity ceiling | cofinal cutoff choice |
| `c_Delta^*` | Theorem 8L.9B | finite-battery decoration-growth ceiling | finite-template geometry |
| `E_14^*` | Definition 8L.11A.3 | Paper-14 whole-process transport ceiling | Paper-14 export |
| `A_11^loc` | Definition 8L.11A.5 | local-RG/precision tail | attacked in 8L.11A.13--15 |
| `A_11^RP` | Definition 8L.11A.5 | reflection-positivity transport tail | attacked in 8L.11A.15A |
| `A_11^Cov` | Definition 8L.11A.5 | Euclidean-covariance transport tail | attacked in 8L.11A.15B |
| `A_11^gauge` | Definition 8L.11A.5 | gauge/chart reconstruction tail | attacked in 8L.11A.15C |
| `A_12^per` | Definition 8L.11A.7 | perimeter transport tail | evaluated in 8L.11A.21A--21B |
| `A_12^cusp` | Definition 8L.11A.7 | cusp transport tail | evaluated in 8L.11A.21A--21B |
| `A_12^smear` | Definition 8L.11A.7 | smearing-removal tail | evaluated in 8L.11A.21A--21C |
| `A_12^app` | Definition 8L.11A.7 | loop approximation/readout tail | evaluated in 8L.11A.21A--21D |
| `A_13^surf` | Definition 8L.11A.9 | surface-polymer nonminimal-sheet tail | `ESURF` and `DEC` closed; `LEAD` reduced/conditionally closed in 8L.11A.22G.2--G.6 |
| `A_13^entry` | Definition 8L.11A.9 | exact-entry transport tail | attacked in 8L.11A.24 |
| `A_13^exact` | Definition 8L.11A.9 | cutoff-to-exact scalar comparison tail | attacked in 8L.11A.25--26 |

The worksheet passes when

```math
\eta_*:=\eta_{19}^{res}+\eta_{ch}^*<1
```

and

```math
\mathcal L_{19}^{src}
:=
\exp\left({c_\Delta^*\eta_*\over1-\eta_*}\right)-1
+E_{14}^*
+A_{11}^{loc}+A_{11}^{RP}+A_{11}^{Cov}+A_{11}^{gauge}
+A_{12}^{per}+A_{12}^{cusp}+A_{12}^{smear}+A_{12}^{app}
+A_{13}^{surf}+A_{13}^{entry}+A_{13}^{exact}
<
Sig_{AFM}.
```

This worksheet is deliberately scalar. It contains no gauge-fixed field
ontology and no unrecorded subprocess. Every entry is a finite record-law
defect or a scalar signal floor.

### Definition 8L.11A.13: Local-RG Source Attack `P19-T11-LOC-AF(A_11^loc)`

`P19-T11-LOC-AF(A_11^loc)` is the local-RG part of the `T_11` attack. It
holds when the Paper-11 AF local-RG residuals and the finite-precision
readout defects satisfy the weighted tail estimate

```math
\limsup_j
\sum_{k\ge j}
L_j^{rec}
\left(
\eta_{locRG,k}^{B_j}
+\eta_{prec,j,k}^{(11)}
\right)
\le
A_{11}^{loc}
<\infty.
```

A sufficient concrete Paper-11/Paper-16 source route is:

1. the common tower satisfies Paper 11 Theorem AF.14 on the growing batteries
   `B_j`;
2. the one-block constants obey Paper 11 Theorem AF.11 with

   ```math
   Q_k^*=B_sg_k+B_le^{-c_*/g_k^2}+B_cg_k^2,
   \qquad
   eD e^{\alpha+\mu}Q_k^*\le {1\over2};
   ```

3. the local ansatz radii `R_k` satisfy the weighted tail bound

   ```math
   \limsup_j
   \sum_{k\ge j}
   L_j^{rec}\,2e^\alpha G_kQ_k^*e^{-\mu R_k}
   \le
   A_{11}^{loc,AF};
   ```

4. the finite-precision tail satisfies

   ```math
   \limsup_j
   \sum_{k\ge j}
   L_j^{rec}\eta_{prec,j,k}^{(11)}
   \le
   A_{11}^{prec};
   ```

5. `A_11^loc=A_11^{loc,AF}+A_11^{prec}`.

The extra factors `L_j^{rec}` are not cosmetic. They are the finite record
sensitivities of the Paper-19 battery. A summable Paper-11 residual tail
alone proves this slot only when it remains summable after multiplication by
the actual record sensitivities.

### Theorem 8L.11A.14: Paper-11 AF Tail Proves The `A_11^loc` Slot

Assume the five clauses of Definition 8L.11A.13. Then

```text
P19-T11-LOC-AF(A_11^loc)
```

holds. Consequently the local part of `P19-T11-LEDGER` holds with the
declared value `A_11^loc`.

Proof.

Paper 11 Theorem AF.11 gives the one-block residual estimate

```math
\eta_{locRG,k}^{B_j}
\le
2e^\alpha G_kQ_k^*e^{-\mu R_k}
```

for the battery row under the uniform AF constants and smallness condition.
Paper 11 Theorem AF.14 supplies the same estimate on the multiscale
whole-process path, provided the ledger compatibility hypotheses hold. Paper
16 `HK-RG-PROJ-LEDGER` places the resulting `eta_locRG` term in the
finite-record drift budget used by `T_11`.

Multiplying by the finite record sensitivity `L_j^{rec}`, summing over the
cofinal tail `k>=j`, and taking limsup gives the third clause of Definition
8L.11A.13. The finite-precision contribution is bounded by the fourth
clause. Therefore

```math
\limsup_jR_{11,j}^{loc}
\le
A_{11}^{loc,AF}+A_{11}^{prec}
=A_{11}^{loc}.
```

This is exactly the local part of `P19-T11-LEDGER`. `square`

### Corollary 8L.11A.15: Zero Local-RG Transport Branch

If, in addition to the hypotheses of Theorem 8L.11A.14,

```math
\sum_{k\ge j}
L_j^{rec}\,G_kQ_k^*e^{-\mu R_k}\to0,
\qquad
\sum_{k\ge j}
L_j^{rec}\eta_{prec,j,k}^{(11)}\to0,
```

then `P19-T11-LOC-AF(0)` holds, so the local-RG contribution to the final
source worksheet is

```math
A_{11}^{loc}=0.
```

Proof.

The two displayed limits make both limsup bounds in Definition 8L.11A.13
zero. Apply Theorem 8L.11A.14 with
`A_11^{loc,AF}=A_11^{prec}=0`. `square`

### Definition 8L.11A.15A: Reflection-Positivity Source Attack `P19-T11-RP(A_11^RP)`

`P19-T11-RP(A_11^RP)` is the reflection-positivity part of the reduced
`T_11` attack. It imports Paper 16 `HK-RP-LEDGER` and the RP half of
`HK-RPCOV-CLOSE`, after removing the perimeter/cusp loop-counterterm tails
already assigned to `T_12`.

For each Paper-19 row `j`, set

```math
P_{11,j}^{RP}
:=
\sum_{k\ge j}
\left(
\eta_{binRP,j,k}^{(11)}
+\eta_{projRP,j,k}^{(11)}
+\eta_{regRP,j,k}^{(11)}
+\eta_{volRP,j,k}^{(11)}
+\eta_{ctRP,j,k}^{(11,red)}
\right).
```

The attack holds when:

1. the finite OS battery is symmetric-positive in the sense of Paper 16
   Definition 9W.1A;
2. Paper 16 `HK-RP-LEDGER` holds on the same pushed-forward record law and
   finite OS battery as `P19-TR-COMMON`;
3. `eta_{ctRP}^{(11,red)}` is the counterterm-weighted RP defect after the
   perimeter/cusp singular tails have been removed and assigned, if nonzero,
   to `T_12`;
4. the projective, regulator/chart, and finite-volume RP defects are assigned
   to this reduced `T_11` RP slot and are not also assigned to `T_12`,
   `T_13`, `T_14`, or `Delta_dec`;
5. the cofinal bound

   ```math
   \limsup_jP_{11,j}^{RP}\le A_{11}^{RP}<\infty
   ```

   holds.

Then the RP clause of `P19-T11-LEDGER` holds.

Proof.

Paper 16 Lemma 9W.1B gives exact finite-cutoff heat-kernel reflection
positivity before declared counterterm/readout transport. Paper 16
Definition 9W.1C says that every nonzero RP loss after transport is one of
the terms in `D_{j,k}^{RP}`: counterterm, binning, projective, regulator, or
finite-volume buffer. Theorem 9W.1D then gives the RP half of
`HK-RPCOV-CLOSE` with `r_{j,k}=D_{j,k}^{RP}`.

The reduced Paper-19 row uses the same decomposition but replaces the raw
counterterm entry by `eta_{ctRP}^{(11,red)}`, because the perimeter/cusp
transport tails have already been isolated in the `T_12` loop bucket.
Therefore `R_{11,j}^{RP}=P_{11,j}^{RP}`. Taking the declared limsup gives
the RP clause of `P19-T11-LEDGER`. `square`

### Definition 8L.11A.15B: Euclidean-Covariance Source Attack `P19-T11-COV(A_11^Cov)`

`P19-T11-COV(A_11^Cov)` is the Euclidean-covariance part of the reduced
`T_11` attack. It imports Paper 16 `HK-COV-LEDGER` and the covariance half
of `HK-RPCOV-CLOSE` on admissible Euclidean motions.

For each row `j`, set

```math
C_{11,j}^{Cov}
:=
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
\right).
```

The attack holds when:

1. `g` ranges over Paper 16's admissible Euclidean-motion ledger
   `Euc_adm`, acting only on declared scalar loop records;
2. the Euclidean-invariant counterterm/readout ledger of Paper 16 Definition
   9W.1F holds on the same finite battery;
3. Paper 16 `HK-COV-LEDGER` holds on the same pushed-forward record law and
   finite battery as `P19-TR-COMMON`;
4. `eta_appCov` is the Euclidean-motion approximant defect, not the
   `T_12` loop-readout approximant defect `eta_appLC`;
5. `eta_ctCov^{(11,red)}` is the counterterm covariance defect after
   perimeter/cusp transport tails are removed from this slot;
6. the projective, regulator/chart, block/collar, and finite-volume
   covariance defects are assigned only here or to the explicitly shared
   same-value ledgers required by `P19-TR-COMMON`;
7. the cofinal bound

   ```math
   \limsup_jC_{11,j}^{Cov}\le A_{11}^{Cov}<\infty
   ```

   holds.

Then the covariance clause of `P19-T11-LEDGER` holds.

Proof.

Paper 16 Definition 9W.1G decomposes the covariance defect into exact cutoff
symmetry error, loop/lattice approximant error, binning, counterterm,
block/collar, projective, regulator/chart, and finite-volume defects.
Theorem 9W.1H proves the Euclidean-covariance half of `HK-RPCOV-CLOSE` with
`q_{j,k}(g)=D_{j,k}^{Cov}(g)`.

The reduced Paper-19 covariance slot is exactly this Paper-16 covariance
ledger with the counterterm term made reduced, and with `eta_appCov` kept in
`T_11` because it measures covariance under an admissible Euclidean motion,
not loop-readout continuity. Hence `R_{11,j}^{Cov}=C_{11,j}^{Cov}`. Taking
the declared limsup proves the covariance clause of `P19-T11-LEDGER`.
`square`

### Definition 8L.11A.15C: Gauge/Chart Reconstruction Source Attack `P19-T11-GAUGE(A_11^gauge)`

`P19-T11-GAUGE(A_11^gauge)` is the scalar gauge/chart reconstruction part of
the reduced `T_11` attack. It imports the gauge-chart part of Paper 16
`HK-REG-CLOSE` and pays only record-level gauge/chart defects that have not
already been spent in the RP, covariance, loop, surface-entry, volume, or
Paper-14 buckets.

For row `j`, set

```math
G_{11,j}^{gauge}
:=
\sum_{k\ge j}
\left(
\eta_{chart,j,k}^{(11)}
+\eta_{gauge-rec,j,k}^{(11)}
\right).
```

The attack holds when:

1. Paper 16's concrete regulator/chart comparison scheme of Definition 9V.4
   is fixed on the same heat-kernel primary readout chart as `P19-TR-COMMON`;
2. the comparison maps are finite record maps built from declared scalar
   operations: closed-loop coordinate identification, finite bin
   refinement/coarsening, counterterm reparametrization, blocking/collar
   re-expression, gauge-chart averaging, or gauge-invariant projection;
3. `eta_{chart}^{(11)}` is the gauge-chart or gauge-fixing transport defect
   from Paper 16 Definition 9V.5 after projection to scalar closed-loop
   records;
4. `eta_{gauge-rec}^{(11)}` bounds the additional finite scalar
   reconstruction defect for forgetting proof-coordinate gauge charts,
   axial trees, local sections, or gauge-fixed covariance variables;
5. any action/regulator, block/collar, counterterm-scheme, finite-volume,
   representation-tail, or precision defect appearing in
   `HK-RG-REG-LEDGER` is assigned to its proper existing slot and is not
   recharged here unless the disjoint debit register declares this gauge slot
   as its unique home;
6. the cofinal bound

   ```math
   \limsup_jG_{11,j}^{gauge}\le A_{11}^{gauge}<\infty
   ```

   holds.

Then the gauge/chart clause of `P19-T11-LEDGER` holds.

Proof.

Paper 16 `HK-REG-CLOSE` is a common-refinement statement for finite record
laws. Definition 9V.4 restricts comparison maps to declared record maps, and
Definition 9V.5 identifies the chart/gauge-fixing defect after projection to
scalar records. Gauge charts, axial trees, and gauge-fixed covariance
variables are therefore proof coordinates only; the exported quantity is the
scalar record-law comparison defect.

By the disjoint debit clause of `P19-TR-COMMON`, every regulator/chart
comparison term has exactly one ledger home. The two terms in
`G_{11,j}^{gauge}` are precisely the chart/gauge-reconstruction terms whose
home is the reduced `T_11` gauge slot. Thus
`R_{11,j}^{gauge}=G_{11,j}^{gauge}`, and the declared limsup proves the
gauge/chart clause of `P19-T11-LEDGER`. `square`

### Theorem 8L.11A.15D: The `T_11` Source Attacks Close The Reduced Transport Ledger

Assume

```text
P19-TR-COMMON,
P19-T11-LOC-AF(A_11^loc),
P19-T11-RP(A_11^RP),
P19-T11-COV(A_11^Cov),
P19-T11-GAUGE(A_11^gauge).
```

Then

```text
P19-T11-LEDGER(A_11^loc,A_11^RP,A_11^Cov,A_11^gauge)
```

holds. Consequently

```text
P19-T11-SRC(A_11^loc,A_11^RP,A_11^Cov,A_11^gauge)
```

holds and

```math
\limsup_jT_{11,j}
\le
A_{11}^{loc}+A_{11}^{RP}+A_{11}^{Cov}+A_{11}^{gauge}.
```

Proof.

Theorem 8L.11A.14 proves the local-RG/precision clause. Definitions
8L.11A.15A, 8L.11A.15B, and 8L.11A.15C prove the RP, covariance, and
gauge/chart clauses. The rowwise reduced `T_11` domination is Definition
8L.11A.5:

```math
T_{11,j}
\le
R_{11,j}^{loc}+R_{11,j}^{RP}+R_{11,j}^{Cov}+R_{11,j}^{gauge}.
```

The common-record audit ensures that projective, regulator/chart,
finite-volume, block/collar, and counterterm terms excluded from `T_12` and
`T_13` are paid here or in the unique same-value ledger declared by
`P19-TR-COMMON`, and are not double-charged. Therefore
`P19-T11-LEDGER` holds. Theorem 8L.11A.6 gives `P19-T11-SRC` and the
displayed limsup bound. `square`

### Definition 8L.11A.16: Perimeter-Cusp Source Attack `P19-T12-PC(A_12^per,A_12^cusp)`

`P19-T12-PC(A_12^per,A_12^cusp)` is the perimeter/cusp part of the reduced
`T_12` attack. It is evaluated on the same pushed-forward record law as
`P19-TR-COMMON` and uses only the two loop-counterterm entries of Paper 16
`HK-LC-TRANSPORT`.

For each fixed Paper-19 loop battery row `j`, set

```math
P_{12,j}
:=
\sum_{k\ge j}\eta_{perLC,j,k},
\qquad
C_{12,j}
:=
\sum_{k\ge j}\eta_{cuspLC,j,k}.
```

The attack holds when the following clauses hold.

1. The finite row satisfies Paper 12 Definition 3.6, or equivalently the
   Paper-12 local connected polymer criterion of Lemma 3.6A, with the same
   perimeter and cusp calibration ledger used by the Paper-16 tower.
2. The scalar counterterm ledger is symmetric-positive in the sense of Paper
   12 Definition 5.9 whenever the row is used in a reflection-positive
   transport comparison.
3. Paper 16 `HK-LC-TRANSPORT` is computed on the same loop approximants,
   counterterm branches, and finite record maps as `P19-TR-COMMON`.
4. The reduced debit register assigns only `eta_{perLC}` and `eta_{cuspLC}`
   to this source attack. The terms

   ```math
   \eta_{projLC,j,k},\quad
   \eta_{regLC,j,k},\quad
   \eta_{volLC,j,k}
   ```

   are excluded from `P_{12,j}` and `C_{12,j}` because they are paid in the
   projective/regulator/volume transport ledgers, namely `T_11` or `T_14`.
5. The cofinal bounds

   ```math
   \limsup_jP_{12,j}\le A_{12}^{per},
   \qquad
   \limsup_jC_{12,j}\le A_{12}^{cusp}
   ```

   hold with finite right-hand sides.

The point of this definition is narrow. It does not re-charge the whole
Paper-16 loop-continuity tail. It extracts only the perimeter and cusp
counterterm transport tails after Paper 12 has identified those tails as
scalar local singular factors of the closed-loop record.

### Theorem 8L.11A.17: Perimeter-Cusp Attack Supplies The First Two `T_12` Slots

Assume `P19-TR-COMMON` and

```text
P19-T12-PC(A_12^per,A_12^cusp).
```

Then the perimeter and cusp clauses of `P19-T12-LEDGER` hold:

```math
\limsup_jR_{12,j}^{per}\le A_{12}^{per},
\qquad
\limsup_jR_{12,j}^{cusp}\le A_{12}^{cusp}.
```

Proof.

Paper 12 Definition 3.6 writes the connected loop cumulant after extracting
the local scalar factor

```math
\exp\left(-\sum_iD_{\rho_i}(C_i,a)\right),
\qquad
D_\rho(C,a)
=
\gamma_\rho(a){\rm Per}_a(C)
+\sum_{\upsilon\in{\rm Cusps}(C)}
\Gamma_\rho(\theta_\upsilon,a).
```

Lemma 3.6A gives the criterion for this extraction from the connected
polymer ledger: local singular support, calibration identification, and
connected residual summability. Thus the only loop-counterterm singular
debits left for transport are the perimeter and cusp calibration transports.
Paper 16 `HK-LC-TRANSPORT` names exactly those debits as `eta_{perLC}` and
`eta_{cuspLC}`.

By Definition 8L.11A.16,
`R_{12,j}^{per}=P_{12,j}` and `R_{12,j}^{cusp}=C_{12,j}`, while
`eta_{projLC}`, `eta_{regLC}`, and `eta_{volLC}` are not part of this reduced
bucket. Taking limsup gives the displayed inequalities. `square`

### Definition 8L.11A.18: Smearing-Removal Source Attack `P19-T12-SMEAR(A_12^smear)`

`P19-T12-SMEAR(A_12^smear)` is the smeared-to-unsmeared removal part of the
reduced `T_12` attack. For each row `j`, set

```math
S_{12,j}^{smear}
:=
\sum_{k\ge j}\eta_{smearLC,j,k}.
```

The attack holds when the following clauses hold.

1. The finite loop battery satisfies Paper 12 Definition 3.11 on the same
   pushed-forward scalar closed-loop record:

   ```math
   \epsilon_{\alpha}^{cal}(\tau)\to0,
   \qquad
   \Omega_\alpha(\tau)\to0,
   ```

   with uniform connected domination for every ordered tuple in the finite
   battery.
2. The cofinal smearing schedule `tau_j` lies inside the admissible collar
   window of Paper 12 Lemma 3.13, so smearing changes only microscopic
   loop-collar data and does not mix distinct nonadjacent arcs or distinct
   loops.
3. Paper 12 Theorem 3.12 applies to the row, giving cumulant and product
   smearing-removal after the same perimeter/cusp calibrations are removed.
4. Paper 16 `HK-LC-TRANSPORT` transports this replacement by the scalar term
   `eta_{smearLC}` and assigns no projective, regulator, or finite-volume
   term to the smearing bucket.
5. The cofinal bound

   ```math
   \limsup_jS_{12,j}^{smear}\le A_{12}^{smear}
   ```

   holds with `A_12^smear<infinity`.

Then the smearing clause of the reduced `T_12` ledger holds.

Proof.

Paper 12 Definition 3.11 decomposes the smeared-minus-unsmeared comparison
into a local calibration error and a renormalized connected-cluster error.
Theorem 3.12 bounds the cumulant difference by
`\epsilon_{\alpha}^{cal}(\tau)+\Omega_\alpha(\tau)` and then upgrades the
finite cumulant statement to finite product records using the uniform
connected domination hypothesis. Lemma 3.13 supplies the clean AF source of
these hypotheses: the smearing support remains inside each loop collar, the
perimeter/cusp calibration absorbs the local singular change, and dominated
convergence controls the remaining connected clusters.

Paper 16 `HK-LC-TRANSPORT` assigns the transported replacement loss to
`eta_{smearLC}`. Therefore
`R_{12,j}^{smear}=S_{12,j}^{smear}`, and the declared limsup bound gives the
smearing clause of `P19-T12-LEDGER`. `square`

### Definition 8L.11A.19: Loop-Approximant/Readout Source Attack `P19-T12-APP(A_12^app)`

`P19-T12-APP(A_12^app)` is the finite loop-approximant and scalar readout
part of the reduced `T_12` attack. For each row `j`, set

```math
B_{12,j}^{app}
:=
\sum_{k\ge j}
\left(
\eta_{P12,j,k}
+\eta_{appLC,j,k}^{(12)}
+\eta_{binLC,j,k}^{(12)}
\right).
```

The attack holds when the following clauses hold.

1. The Paper-12 loop-modulus package is available on the declared finite
   admissible loop stratum, after perimeter/cusp calibration and
   smearing-removal have been fixed by Definitions 8L.11A.16 and
   8L.11A.18.
2. The level-`k` loop representatives are equivariant under the admissible
   lattice symmetries up to the declared summable approximant defect
   `eta_{appLC,j,k}^{(12)}`.
3. The finite record binning and battery restriction defects for the scalar
   loop readouts are exactly `eta_{binLC,j,k}^{(12)}`.
4. The residual Paper-12 AF loop-variation and connected-tail loss after the
   finite-battery modulus is extracted is exactly `eta_{P12,j,k}`.
5. The reduced bucket excludes

   ```math
   \eta_{projLC,j,k},\quad
   \eta_{regLC,j,k},\quad
   \eta_{volLC,j,k},
   ```

   because projective drift, regulator/chart comparison, and finite-volume
   exhaustion are already assigned to `T_11` or `T_14`.
6. The cofinal bound

   ```math
   \limsup_jB_{12,j}^{app}\le A_{12}^{app}
   ```

   holds with `A_12^app<infinity`.

This is the only `T_12` bucket that may contain the residual Paper-12 loop
modulus defect `eta_{P12}`. The perimeter/cusp and smearing terms have their
own slots, and the projective/regulator/volume terms are explicitly outside
the reduced `T_12` ledger.

### Theorem 8L.11A.20: The Three `T_12` Source Attacks Close The Reduced Loop Ledger

Assume

```text
P19-TR-COMMON,
P19-T12-PC(A_12^per,A_12^cusp),
P19-T12-SMEAR(A_12^smear),
P19-T12-APP(A_12^app).
```

Then

```text
P19-T12-LEDGER(A_12^per,A_12^cusp,A_12^smear,A_12^app)
```

holds. Consequently

```text
P19-T12-SRC(A_12^per,A_12^cusp,A_12^smear,A_12^app)
```

holds and

```math
\limsup_jT_{12,j}
\le
A_{12}^{per}+A_{12}^{cusp}+A_{12}^{smear}+A_{12}^{app}.
```

Proof.

Theorem 8L.11A.17 proves the perimeter and cusp limsup clauses of
`P19-T12-LEDGER`. Definition 8L.11A.18 proves the smearing-removal clause.
Definition 8L.11A.19 proves the loop-approximant/readout clause.

It remains only to check that the rowwise reduced `T_12` inequality is the
right one. Paper 16 `HK-LC-TRANSPORT` decomposes the loop-continuity transport
tail into the Paper-12 residual loop-variation term, approximant/binning
terms, perimeter/cusp transport, smearing-removal transport, and
projective/regulator/volume transport. The reduced `T_12` ledger keeps the
first six loop-readout terms and removes the last three because
`P19-TR-COMMON` assigns them to the projective/regulator/volume transport
ledgers. Therefore

```math
T_{12,j}
\le
R_{12,j}^{per}+R_{12,j}^{cusp}
+R_{12,j}^{smear}+R_{12,j}^{app}.
```

This is precisely `P19-T12-LEDGER`. Theorem 8L.11A.8 then gives
`P19-T12-SRC` and the limsup bound. `square`

### Corollary 8L.11A.21: Zero Loop-Readout Transport Branch

If the hypotheses of Theorem 8L.11A.20 hold and

```math
P_{12,j}\to0,
\qquad
C_{12,j}\to0,
\qquad
S_{12,j}^{smear}\to0,
\qquad
B_{12,j}^{app}\to0,
```

then the reduced loop-readout contribution to the final source worksheet can
be set to

```math
A_{12}^{per}=A_{12}^{cusp}=A_{12}^{smear}=A_{12}^{app}=0.
```

Proof.

All four tails are nonnegative. The displayed convergence makes all four
limsups in the three source attacks vanish. Apply Theorem 8L.11A.20 with
zero right-hand sides. `square`

### Definition 8L.11A.21A: Reduced `T_12` Constant Evaluation Worksheet `P19-T12-EVAL`

`P19-T12-EVAL` is the exact scalar evaluation of the reduced loop-readout
constants. It is computed only from the four reduced `HK-LC-TRANSPORT`
subtails retained in `T_12`. Define

```math
A_{12}^{per,eval}
:=
\limsup_j\sum_{k\ge j}\eta_{perLC,j,k},
\qquad
A_{12}^{cusp,eval}
:=
\limsup_j\sum_{k\ge j}\eta_{cuspLC,j,k},
```

```math
A_{12}^{smear,eval}
:=
\limsup_j\sum_{k\ge j}\eta_{smearLC,j,k},
```

and

```math
A_{12}^{app,eval}
:=
\limsup_j\sum_{k\ge j}
\left(
\eta_{P12,j,k}
+\eta_{appLC,j,k}^{(12)}
+\eta_{binLC,j,k}^{(12)}
\right).
```

The evaluated reduced constants are

```math
A_{12}^{per}=A_{12}^{per,eval},
\quad
A_{12}^{cusp}=A_{12}^{cusp,eval},
\quad
A_{12}^{smear}=A_{12}^{smear,eval},
\quad
A_{12}^{app}=A_{12}^{app,eval},
```

provided all four right-hand sides are finite. If any is infinite, the
reduced `T_12` route fails for the declared tower.

This worksheet does not include

```math
\eta_{projLC,j,k},\quad
\eta_{regLC,j,k},\quad
\eta_{volLC,j,k}.
```

Those losses are paid by the reduced `T_11`/`T_14` ledgers. Including them
here would double-charge projective/regulator/volume transport.

### Theorem 8L.11A.21B: Perimeter-Cusp Constants From Calibrated Counterterm Tails

Assume `P19-T12-PC(A_{12}^{per},A_{12}^{cusp})` and `P19-T12-EVAL`. Then

```math
A_{12}^{per}=A_{12}^{per,eval},
\qquad
A_{12}^{cusp}=A_{12}^{cusp,eval}.
```

Moreover, if the calibrated perimeter and cusp counterterm branches are
cofinally stationary on every finite loop battery after pushforward to the
scalar record law, then

```math
A_{12}^{per}=A_{12}^{cusp}=0.
```

More generally, if the calibration drifts have summable cofinal tails

```math
\sum_{k\ge j}\eta_{perLC,j,k}\to0,
\qquad
\sum_{k\ge j}\eta_{cuspLC,j,k}\to0,
```

then the same zero conclusion holds.

Proof.

The first statement is the definition of the evaluated constants. The
perimeter and cusp transports in Paper 16 `HK-LC-TRANSPORT` are exactly
`eta_{perLC}` and `eta_{cuspLC}` after Paper 12's perimeter/cusp
calibrations have been extracted. If the calibrated branches are cofinally
stationary on the finite battery, these transport defects vanish termwise on
the tail. If the weaker displayed summable tails vanish, their limsups are
zero. In either case Definition 8L.11A.21A gives the zero constants. `square`

### Theorem 8L.11A.21C: Smearing-Removal Constant From The Local Subtraction Schedule

Assume `P19-T12-SMEAR(A_{12}^{smear})` and `P19-T12-EVAL`. Then

```math
A_{12}^{smear}=A_{12}^{smear,eval}.
```

A sufficient zero branch is:

```math
\tau_j\downarrow0,
\qquad
\max_{\alpha\in B_j}
\left(
\epsilon_{\alpha}^{cal}(\tau_j)+\Omega_\alpha(\tau_j)
\right)
\to0,
```

with uniform connected domination on the finite row and with the transported
smearing defects satisfying

```math
\sum_{k\ge j}\eta_{smearLC,j,k}\to0.
```

Under these clauses,

```math
A_{12}^{smear}=0.
```

Proof.

Paper 12 Definition 3.11 and Theorem 3.12 bound the finite cumulant
smearing-removal error by
`\epsilon_{\alpha}^{cal}(\tau)+\Omega_\alpha(\tau)`, and Lemma 3.13 gives
the clean AF source of this estimate when the smearing support stays inside
the loop collar. Paper 16 `HK-LC-TRANSPORT` records the transported
smeared-to-unsmeared replacement as `eta_{smearLC}`. Thus the evaluated
constant is the displayed limsup of the `eta_{smearLC}` tail. If that tail
goes to zero under the chosen cofinal schedule, the limsup is zero. `square`

### Theorem 8L.11A.21D: Loop-Approximant/Readout Constant From The Paper-12 Modulus Tail

Assume `P19-T12-APP(A_{12}^{app})` and `P19-T12-EVAL`. Then

```math
A_{12}^{app}=A_{12}^{app,eval}.
```

The constant has three and only three reduced contributions. Set

```math
L_{12}^{P12}
:=
\limsup_j
\sum_{k\ge j}
\eta_{P12,j,k},
\qquad
L_{12}^{appLC}
:=
\limsup_j
\sum_{k\ge j}
\eta_{appLC,j,k}^{(12)},
\qquad
L_{12}^{binLC}
:=
\limsup_j
\sum_{k\ge j}
\eta_{binLC,j,k}^{(12)}.
```

Then

```math
A_{12}^{app,eval}
\le
L_{12}^{P12}+L_{12}^{appLC}+L_{12}^{binLC}.
```

Equality holds when limsup additivity is sharp for the declared nonnegative
tails. In particular, for any finite constants satisfying

```math
\limsup_j\sum_{k\ge j}\eta_{P12,j,k}\le A_{12}^{P12,*},
\quad
\limsup_j\sum_{k\ge j}\eta_{appLC,j,k}^{(12)}\le A_{12}^{appLC,*},
\quad
\limsup_j\sum_{k\ge j}\eta_{binLC,j,k}^{(12)}\le A_{12}^{binLC,*}.
```

one has

```math
A_{12}^{app,eval}
\le
A_{12}^{P12,*}+A_{12}^{appLC,*}+A_{12}^{binLC,*}.
```

If all three tails vanish, then `A_{12}^{app}=0`.

Proof.

Definition 9X.1C of Paper 16 assigns the residual Paper-12 loop-variation
and connected-tail loss to `eta_{P12}`, the loop representative replacement
to `eta_{appLC}`, and finite record binning/restriction to `eta_{binLC}`.
Definition 8L.11A.19 keeps exactly these three terms in the reduced
approximant/readout bucket. The displayed identities and upper bounds are
therefore immediate from nonnegativity and limsup subadditivity. Vanishing of
all three tails gives zero by Definition 8L.11A.21A. `square`

### Theorem 8L.11A.21E: Evaluated `T_12` Constants Close The Loop-Readout Bucket

Assume `P19-TR-COMMON`, `P19-T12-EVAL`, and the three source attacks

```text
P19-T12-PC(A_12^per,A_12^cusp),
P19-T12-SMEAR(A_12^smear),
P19-T12-APP(A_12^app).
```

If the four evaluated constants in Definition 8L.11A.21A are finite, then

```text
P19-T12-LEDGER(
A_12^per, A_12^cusp, A_12^smear, A_12^app)
```

holds with the evaluated values. Consequently

```math
\limsup_jT_{12,j}
\le
A_{12}^{per,eval}
+A_{12}^{cusp,eval}
+A_{12}^{smear,eval}
+A_{12}^{app,eval}.
```

If the four evaluated tails vanish, then the reduced loop-readout bucket
contributes zero to the final source worksheet.

Proof.

Theorems 8L.11A.21B--8L.11A.21D identify the four evaluated constants with
the four reduced source slots. Theorem 8L.11A.20 closes `P19-T12-LEDGER` and
then `P19-T12-SRC`. The final zero statement is Corollary 8L.11A.21. `square`

### Definition 8L.11A.22: Cofinal Surface Subcriticality Attack `P19-T13-SUB(q_13^*)`

`P19-T13-SUB(q_13^*)` is the first and hardest gate in the reduced `T_13`
attack. It is the cofinal version of Paper 13's condition
`B_Cu_{\rho,s_0}<1` on the actual pushed-forward scalar loop record.

For each Paper-19 row `j` and each Creutz loop `C in B_{CR,j}`, let

```math
q_{C,j}:=B_{C,j}u_{\rho,s_0,j},
\qquad
B_{C,j}:=D_{C,j}E_{C,j}^{surf},
```

where `D_{C,j}` is the Paper-13 decoration-growth constant for nonminimal
sheets and `E_{C,j}^{surf}` is the finite-degree surface entropy constant of
Paper 13 Lemma 7.30Q, both evaluated on the same finite block battery and
same pushed-forward closed-loop record law as `P19-TR-COMMON`. Set

```math
q_{13,j}:=\max_{C\in B_{CR,j}}q_{C,j}.
```

The attack holds when there is a declared scalar `q_13^*<1` such that

```math
\limsup_j q_{13,j}\le q_{13}^*<1.
```

Equivalently, every cofinal Creutz window lies in the Paper-13 surface
subcriticality domain. A sufficient Paper-13 source route is any one of:

1. Paper 13 Definition 7.30L clause 6 for the target surface-polymer entry
   estimate;
2. Paper 13 Definition 7.30O clause 4 in the strong-block character domain;
3. Paper 13 Definition 7.30U clause 5, or the six-gate decomposition
   `SUB(s_0,\rho,L)` of Definition 7.30Y;
4. the mass-gap/area-law bridge package of Definition 7.30AT, with
   `0<u_{\rho,s_0}<u_*`.

This gate is not perturbative asymptotic freedom. It is the scalar statement
that the exact block loop record has a leading sheet coefficient small enough
to beat finite-degree surface entropy and decoration growth.

### Definition 8L.11A.22A: Evaluated Surface Subcriticality Constant `P19-T13-SUB-EVAL`

`P19-T13-SUB-EVAL` is the exact cofinal value of the first dynamical
`T_13` gate. With `q_{13,j}` as in Definition 8L.11A.22, set

```math
q_{13}^{act}
:=
\limsup_j q_{13,j}
=
\limsup_j
\max_{C\in B_{CR,j}}
D_{C,j}E_{C,j}^{surf}u_{\rho,s_0,j}.
```

The subcriticality margin may equivalently be recorded logarithmically. When
the displayed factors are positive and finite on a cofinal tail, define

```math
m_{C,j}^{sub}
:=
-\log u_{\rho,s_0,j}
-\log D_{C,j}
-\log E_{C,j}^{surf},
\qquad
m_{13}^{sub}
:=
\liminf_j\min_{C\in B_{CR,j}}m_{C,j}^{sub}.
```

Then

```math
q_{13}^{act}=e^{-m_{13}^{sub}}.
```

The exact pass condition for the surface-polymer route is

```math
q_{13}^{act}<1
\qquad\text{equivalently}\qquad
m_{13}^{sub}>0.
```

If `q_{13}^{act}>=1`, the reduced surface-polymer route fails at
`P19-T13-SUB`: no cofinal scalar `q_13^*<1` can dominate the actual
surface ratio. This is a failure of this proof route, not by itself a
falsification of confinement.

### Theorem 8L.11A.22B: Exact Pass/Fail Test For `P19-T13-SUB`

Assume `P19-TR-COMMON` and `P19-T13-SUB-EVAL`.

1. If `q_{13}^{act}<1`, then for every
   `q_13^*` with `q_{13}^{act}<q_13^*<1`, the gate
   `P19-T13-SUB(q_13^*)` holds.
2. If `P19-T13-SUB(q_13^*)` holds for some `q_13^*<1`, then
   `q_{13}^{act}\le q_13^*<1`.
3. If `q_{13}^{act}>=1`, then `P19-T13-SUB(q_13^*)` fails for every
   `q_13^*<1`, and Theorem 8L.11A.23 cannot be invoked.

Proof.

The first claim is the definition of `limsup`: if
`q_{13}^{act}<q_13^*`, then `q_{13,j}\le q_13^*` for all sufficiently large
`j`, uniformly over the finite Creutz battery because the maximum over
`C in B_{CR,j}` has already been taken. This is exactly
Definition 8L.11A.22. The second claim is immediate by taking `limsup_j` in
that definition. The third is the contrapositive of the second. `square`

### Theorem 8L.11A.22C: Logarithmic Surface-Margin Criterion

Assume the positive finite cofinal-factor branch of Definition 8L.11A.22A.
Set

```math
\kappa_{sheet,j}:=-\log u_{\rho,s_0,j},
\qquad
H_{surf,j}:=
\max_{C\in B_{CR,j}}
\left(\log D_{C,j}+\log E_{C,j}^{surf}\right).
```

If there is a scalar `mu_13>0` such that

```math
\liminf_j\left(\kappa_{sheet,j}-H_{surf,j}\right)\ge \mu_{13}>0,
```

then

```math
q_{13}^{act}\le e^{-\mu_{13}}<1,
```

and `P19-T13-SUB(q_13^*)` holds for every
`q_13^* in (e^{-\mu_{13}},1)`. Conversely, if

```math
\liminf_j\left(\kappa_{sheet,j}-H_{surf,j}\right)\le0,
```

then this logarithmic criterion does not prove subcriticality; if the
corresponding `q_{13}^{act}` is at least one, the route fails by
Theorem 8L.11A.22B.

Proof.

For each row,

```math
q_{13,j}
=
\exp\left(
-\kappa_{sheet,j}+H_{surf,j}
\right).
```

Taking `limsup_j` and using monotonicity and continuity of the exponential
gives the displayed bound. The final statement is only a route statement:
failure of this sufficient logarithmic lower bound does not by itself prove
`q_{13}^{act}>=1`; the exact value remains the limsup in
Definition 8L.11A.22A. `square`

### Corollary 8L.11A.22D: Import From Paper 16 `HK-SURF-CLOSE`

Assume Paper 16 `HK-SURF-CLOSE` is verified on the same Creutz battery and
same scalar record tower, with surface reserve

```math
M_{SUB}^{bd}
=
\kappa_{sheet}-h_{surf}-L_{dec}\eta_{dec}^{bd}-R_{surf}
>0.
```

Assume also that the Paper-13 nonminimal-sheet decoration/entropy envelope
used in Definition 8L.11A.22 satisfies, cofinally,

```math
\max_{C\in B_{CR,j}}
\left(\log D_{C,j}+\log E_{C,j}^{surf}\right)
\le
h_{surf}+L_{dec}\eta_{dec}^{bd}+R_{surf},
```

and that `-\log u_{\rho,s_0,j}\ge\kappa_{sheet}` on the selected block
rows. Then

```math
q_{13}^{act}\le e^{-M_{SUB}^{bd}}<1.
```

Consequently `P19-T13-SUB(q_13^*)` holds for every
`q_13^* in (e^{-M_{SUB}^{bd}},1)`.

Proof.

The two displayed cofinal inequalities imply

```math
\kappa_{sheet,j}-H_{surf,j}
\ge
\kappa_{sheet}-h_{surf}-L_{dec}\eta_{dec}^{bd}-R_{surf}
=
M_{SUB}^{bd}>0.
```

Apply Theorem 8L.11A.22C. This import is admissible only because all
quantities are evaluated on the same whole-process pushed-forward scalar
record law. No gauge-fixed field configuration, hidden subprocess kernel, or
extra decoration debit is introduced. `square`

### Definition 8L.11A.22E: Surface-Entropy Component Audit `P19-T13-ESURF(h_13^*)`

`P19-T13-ESURF(h_13^*)` is the finite geometry part of the
subcriticality attack. Let `Delta_plaq,j` be the maximum plaquette-adjacency
degree in the block plaquette graph supporting the row-`j` Creutz battery,
and let `R_loc,j` be a finite upper bound on the number of admissible
backtracking-free local replacement types per added plaquette. Define the
crude finite-degree entropy envelope

```math
E_{comb,j}
:=
\exp(3)\,R_{loc,j}\,\Delta_{plaq,j}.
```

The audit holds with constant `h_13^*<infinity` when

```math
\limsup_j\log E_{comb,j}\le h_{13}^*.
```

For the four-dimensional hypercubic block template with a fixed local
surface convention, `Delta_plaq,j` and `R_loc,j` are row-independent finite
template constants after the block shape is frozen. In that branch
`h_13^*` is just the logarithm of this finite combinatorial envelope.

### Lemma 8L.11A.22E.0: Frozen `4D` Hypercubic Plaquette Template

Use the reduced block-surface support convention: admissible surfaces are
finite backtracking-reduced supports of unoriented block plaquettes with the
declared scalar boundary loop, and orientation/sign bookkeeping is absorbed
into the scalar loop record or into decoration constants, not into the
surface-support entropy. Then, on the four-dimensional hypercubic block
lattice,

```math
\Delta_{plaq}^{4D}=20,
\qquad
R_{loc}^{4D}=1.
```

Consequently the frozen geometry envelope is

```math
E_{comb}^{4D}
=
20e^3,
\qquad
h_{13}^{geom}
:=
\log E_{comb}^{4D}
=
3+\log 20.
```

Numerically,

```math
h_{13}^{geom}\approx 5.995732.
```

If one instead insists on an orientation-doubled support convention, the
same proof gives the harmless fallback `R_loc^{4D}=2` and
`h_{13}^{geom,or}=3+\log 40`.

Proof.

A block plaquette has four boundary block edges. Fix one such edge. In a
four-dimensional hypercubic lattice, the edge direction can be paired with
one of the other three coordinate directions, and for each such direction
there are two plaquettes meeting the edge, one on each side. Hence there are
`2(4-1)=6` plaquettes incident to that edge, one of which is the original
plaquette. Thus at most five distinct neighboring plaquettes share that
edge with the original plaquette. Summing over the four boundary edges gives
the maximum edge-sharing plaquette-adjacency degree

```math
\Delta_{plaq}^{4D}\le 4\cdot5=20.
```

The bound is sharp on the interior of the infinite block lattice. Boundary
or collar restrictions can only decrease it.

Under the reduced support convention, adding one excess plaquette already
specifies the local replacement type: backtracking pairs have been removed
before the entropy count, and orientation labels are not counted as separate
surface supports. Hence `R_loc^{4D}=1`. Substituting these two frozen
template constants into `E_comb=exp(3)R_loc Delta_plaq` gives the displayed
`E_comb^{4D}` and `h_{13}^{geom}`. `square`

### Corollary 8L.11A.22E.0.1: `P19-T13-ESURF` Is Closed On The Frozen Template

On the reduced four-dimensional hypercubic block-surface template of Lemma
8L.11A.22E.0,

```text
P19-T13-ESURF(3+log 20)
```

holds. Equivalently,

```math
\limsup_j\log E_{comb,j}
\le
3+\log 20.
```

For the orientation-doubled fallback convention, the same statement holds
with `3+log 40`.

Proof.

The cofinal rows use the same frozen block-surface support convention and
the same four-dimensional hypercubic plaquette adjacency. Therefore
`Delta_plaq,j=20` and `R_loc,j=1` for every sufficiently large selected row,
up to boundary/collar reductions. Lemma 8L.11A.22E.0 gives
`E_comb,j<=20e^3` cofinally. Taking logarithms and `limsup_j` proves the
audit. `square`

### Theorem 8L.11A.22E.1: `P19-T13-ESURF` Bounds The Paper-13 Entropy Factor

Assume `P19-T13-ESURF(h_13^*)`. Then the entropy constants of Paper 13 Lemma
7.30Q may be chosen so that

```math
\limsup_j
\max_{C\in B_{CR,j}}\log E_{C,j}^{surf}
\le h_{13}^*.
```

Proof.

Paper 13 Lemma 7.30Q encodes an excess-`q` surface as connected
plaquette-deviation components in the finite plaquette-adjacency graph,
together with finitely many local replacements. In a graph of maximum degree
`Delta_plaq,j`, connected plaquette animals containing a root are bounded
exponentially by a finite-degree constant. The finite number of roots along
the minimal sheet is absorbed into `A_C`; component partitions and local
replacement choices are absorbed into the displayed `E_comb,j`. Thus
`E_{C,j}^{surf}<=E_{comb,j}` for every loop in the finite Creutz battery.
Taking `max_C`, logarithms, and `limsup_j` proves the claim. `square`

### Definition 8L.11A.22F: Decoration-Growth Component Audit `P19-T13-DEC(d_13^*)`

`P19-T13-DEC(d_13^*)` is the nonminimal-sheet decoration part of the
subcriticality attack. For row `j`, let `eta_dec,j^{surf}` be the KP
activity of the combined non-leading character and residual-decoration gas
attached to a surface collar, and let `Lambda_col,j` be the maximum number
of new collar polymer anchor sites created per unit excess surface area.
The audit holds when `eta_dec,j^{surf}<1` cofinally and

```math
\limsup_j
{\Lambda_{col,j}\eta_{dec,j}^{surf}\over1-\eta_{dec,j}^{surf}}
\le d_{13}^*<\infty.
```

Equivalently, it asserts that the Paper-13 constants `D_{C,j}` can be chosen
with cofinal logarithmic growth at most `d_13^*` per excess plaquette.

### Theorem 8L.11A.22F.1: `P19-T13-DEC` Bounds The Paper-13 Decoration Factor

Assume `P19-T13-DEC(d_13^*)`. Then

```math
\limsup_j
\max_{C\in B_{CR,j}}\log D_{C,j}
\le d_{13}^*.
```

Proof.

Paper 13 Proposition 7.30AH obtains `D_C` from the KP cluster expansion of
the combined decoration gas. A nonminimal sheet with excess area `q` creates
at most `Lambda_col,j q` additional collar anchor sites beyond the fixed
minimal collar. The standard finite polymer-gas cluster bound gives

```math
\log |Z(\Sigma)|-\log e^{\xi'_{C,j}}
\le
q\,{\Lambda_{col,j}\eta_{dec,j}^{surf}\over
1-\eta_{dec,j}^{surf}}.
```

Thus one may take

```math
\log D_{C,j}
\le
{\Lambda_{col,j}\eta_{dec,j}^{surf}\over
1-\eta_{dec,j}^{surf}}.
```

The audit's limsup bound gives the result. The finite minimal-collar
constant is `xi'_C`; it is not charged again to `D_C` or to
`Delta_dec,j^bd`. `square`

### Theorem 8L.11A.22F.2: Same-Decoration Import Closes `P19-T13-DEC`

Assume the same-record decoration audits

```text
P19-AN-AUDIT(m),
P19-CHTAIL-AUDIT(eta_ch^*),
P19-FBTPL-DEC(C_xi,C_xip),
eta_*:=eta_19^res+eta_ch^*<1.
```

Then the surface-collar decoration KP activity and collar multiplicity in
Definition 8L.11A.22F may be chosen so that

```math
\limsup_j\eta_{dec,j}^{surf}\le\eta_*,
\qquad
\limsup_j\Lambda_{col,j}\le C_\xi.
```

Consequently

```text
P19-T13-DEC(d_13^*)
```

holds with

```math
d_{13}^*
:=
{C_\xi\eta_*\over1-\eta_*}.
```

On the centered square `SEL_0` branch with the canonical half-margin
character choice of Corollary 8L.8B, this becomes

```math
d_{13}^{SEL0}
:=
{C_\xi^{SEL0}\eta_*\over1-\eta_*},
\qquad
\eta_*={1+\eta_{19}^{res}\over2}.
```

Proof.

The decoration gas in `P19-FBTPL-DEC` is, by Definition 8L.9A clause 2, the
same pushed-forward finite record law used in `P19-AN-AUDIT(m)` and
`P19-CHTAIL-AUDIT(eta_ch^*)`. Theorem 0A.4 bounds the residual component by
`eta_19^res`; the character-tail audit bounds the non-leading character
component by `eta_ch^*`. Hence the same combined surface-collar decoration
gas has cofinal KP activity at most

```math
\eta_*=\eta_{19}^{res}+\eta_{ch}^*<1.
```

Clause 3 of `P19-FBTPL-DEC(C_xi,C_xip)` bounds the collar excess counted per
unit excess area by `C_xi`. This is exactly the `Lambda_col,j` needed for
nonminimal-sheet growth: adding one unit of excess surface area creates only
the area-charged collar templates. The endpoint/corner constant `C_xip` is
not included here, because it is independent of the excess area and is
charged in the finite-battery decoration debit `Delta_dec,j^bd`.

Therefore

```math
\limsup_j
{\Lambda_{col,j}\eta_{dec,j}^{surf}\over
1-\eta_{dec,j}^{surf}}
\le
{C_\xi\eta_*\over1-\eta_*}.
```

This is exactly `P19-T13-DEC(d_13^*)`. The proof imports the same KP activity
used by the decoration ledger but does not add a second decoration debit:
`Delta_dec` pays the finite-battery decoration loss, while `d_13^*` is only
the incremental collar-growth constant needed to test surface
subcriticality. `square`

### Corollary 8L.11A.22F.3: Centered Square Branch Closes The Decoration-Growth Audit

On the centered square `SEL_0` branch,

```text
P19-T13-DEC(d_13^{SEL0})
```

holds with

```math
d_{13}^{SEL0}
=
{C_\xi^{SEL0}\eta_*\over1-\eta_*},
\qquad
\eta_*={1+\eta_{19}^{res}\over2}.
```

Equivalently,

```math
d_{13}^{SEL0}
=
C_\xi^{SEL0}
{1+\eta_{19}^{res}\over1-\eta_{19}^{res}}.
```

Proof.

Use Lemma 8L.9A.1 for `P19-FBTPL-DEC(C_xi^{SEL0},C_xip^{SEL0})`,
Corollary 8L.8B for the canonical half-margin character choice, and Theorem
8L.11A.22F.2. The algebraic simplification follows from
`eta_*=(1+eta_19^res)/2`. `square`

### Definition 8L.11A.22G: Leading-Sheet Coefficient Audit `P19-T13-LEAD(kappa_13^*)`

`P19-T13-LEAD(kappa_13^*)` is the scalar character-extraction part of the
subcriticality attack. It holds when Paper 13's character-extraction gate
`CE(s_0,\rho,L)` is verified on the same block plaquette marginal used by
the Creutz battery, with

```math
u_{\rho,s_0,j}=k_{\rho,j}\in(0,1)
```

after the real-paired convention for non-self-conjugate `rho`, and

```math
\liminf_j\left(-\log u_{\rho,s_0,j}\right)\ge\kappa_{13}^*>0.
```

The coefficient `u_{\rho,s_0,j}` is computed by the Paper-13 Haar projection
of Definition 7.30AP. This is a scalar central-record coefficient, not a
gauge-fixed plaquette field.

### Theorem 8L.11A.22G.1: `P19-T13-LEAD` Bounds The Leading Factor

Assume `P19-T13-LEAD(kappa_13^*)`. Then

```math
\limsup_j u_{\rho,s_0,j}
\le e^{-\kappa_{13}^*}<1.
```

Proof.

This is immediate from the definition of `liminf` and monotonicity of the
exponential. Paper 13 Proposition 7.30AF and Definition 7.30AP identify the
coefficient with the scalar central character projection used by
`CE(s_0,\rho,L)`. `square`

### Definition 8L.11A.22G.1A: Frozen Coefficient Target `P19-T13-COEFF-FRZ`

`P19-T13-COEFF-FRZ(rho,s_0,B_{CR},K_p)` fixes the coefficient target used
by `P19-T13-LEAD`, `P19-T13-CEWIN`, and the `T_13` surface ratio. It holds
when the following data are frozen on the same cofinal row set as
`P19-TR-COMMON`.

1. `rho` is one declared nontrivial irreducible representation of `SU(N)`;
   for non-self-conjugate `rho`, the real paired central record `Phi_rho` is
   used once.
2. `s_0` is the block scale used by the Paper-13 Creutz battery and by the
   reduced `T_13` surface/entry ledger.
3. `B_{CR,j}` is the same finite four-loop Creutz battery used in
   Definitions 8L.11A.22 and 8L.11A.22A.
4. `K_{p,j}` is the central block-plaquette marginal obtained by pushing the
   exact whole-process row law through the declared block plaquette record,
   counterterm convention, projection map, and central scalar readout.
5. The character coefficients are the Haar projections

   ```math
   k_{\lambda,j}
   :=
   {\langle K_{p,j},\chi_\lambda\rangle_{L^2(SU(N))}
   \over
   \langle\chi_\lambda,\chi_\lambda\rangle_{L^2(SU(N))}},
   ```

   with the same real-paired replacement for `rho` when needed.
6. The non-leading coefficient tail in `P19-T13-CEWIN` is measured with the
   same representation cutoff and same decoration ledger as
   `P19-T13-DEC`.

This is a scalar record-law target. The gauge chart used to compute
`K_{p,j}` is only a coordinate device inside the pushforward. It is not a
new state space and it does not introduce a hidden local-field ontology.

### Lemma 8L.11A.22G.1B: The Frozen Target Makes `LEAD-EVAL` Same-Record

If `P19-T13-COEFF-FRZ(rho,s_0,B_{CR},K_p)` holds, then the coefficients
used in `P19-T13-LEAD-EVAL` and `P19-T13-CEWIN` are defined on the same
finite scalar record tower as `P19-TR-COMMON`, `P19-T13-DEC`, and the
reduced `T_13` surface ledger.

Proof.

Clauses 2--4 identify the block scale, Creutz battery, pushforward law,
counterterm convention, and scalar readout with the objects already used in
the reduced `T_13` ledger. Clause 5 defines the coefficients by Haar
projection from the resulting central scalar marginal. Clause 6 assigns the
non-leading tail to the same decoration ledger used by `P19-T13-DEC`. Hence
the coefficient target is same-record and same-debit by construction.
`square`

### Definition 8L.11A.22G.2: Exact Leading-Coefficient Evaluation `P19-T13-LEAD-EVAL`

For each selected row `j`, let `K_{p,j}` be the central block-plaquette
marginal on the same pushed-forward scalar record tower and same Creutz
battery used in `P19-TR-COMMON`. Define the leading scalar coefficient by
the Paper-13 Haar projection

```math
k_{\rho,j}
:=
{\langle K_{p,j},\chi_\rho\rangle_{L^2(SU(N))}
\over
\langle \chi_\rho,\chi_\rho\rangle_{L^2(SU(N))}}
```

for self-conjugate `rho`; for non-self-conjugate `rho`, replace
`\chi_\rho` by the real paired central record `\Phi_\rho` as in Paper 13
Definition 7.30AP. Set

```math
u_{\rho,s_0,j}:=k_{\rho,j}.
```

The evaluated leading-sheet exponent is

```math
\kappa_{13}^{act}
:=
\liminf_j\left(-\log u_{\rho,s_0,j}\right),
```

provided `0<u_{\rho,s_0,j}<1` cofinally. If the coefficient is not
eventually positive, or if it is not eventually below one, then
`P19-T13-LEAD` fails for the declared representation `rho` and block record.

Thus the exact pass condition for a positive `T_13` leading audit is

```math
0<\kappa_{13}^*
\le
\kappa_{13}^{act}
```

with `0<u_{\rho,s_0,j}<1` cofinally.

### Theorem 8L.11A.22G.3: Exact Pass/Fail Test For `P19-T13-LEAD`

Assume `P19-T13-LEAD-EVAL`.

1. If `\kappa_{13}^{act}>0` and `0<u_{\rho,s_0,j}<1` cofinally, then
   `P19-T13-LEAD(\kappa_{13}^*)` holds for every
   `0<\kappa_{13}^*<\kappa_{13}^{act}`.
2. If `P19-T13-LEAD(\kappa_{13}^*)` holds for some
   `\kappa_{13}^*>0`, then `\kappa_{13}^{act}\ge\kappa_{13}^*>0`.
3. If `\kappa_{13}^{act}\le0`, or if the coefficient is not cofinally in
   `(0,1)`, the leading-coefficient route fails for this selected
   representation and block record.

Proof.

This is the definition of `liminf` applied to the scalar sequence
`-\log u_{\rho,s_0,j}`. Cofinal positivity and the upper bound by one are
exactly the Paper-13 `CE` leading coefficient requirements; without them the
logarithmic sheet suppression is not a valid positive scalar record
coefficient. `square`

### Definition 8L.11A.22G.4: Coefficient-Window Source Audit `P19-T13-CEWIN(kappa_13^*,epsilon_ch)`

`P19-T13-CEWIN(kappa_13^*,epsilon_ch)` holds when Paper 13's computable
character coefficient gate is verified on the same block plaquette marginal
and finite Creutz battery:

```math
0<k_{\rho,j}\le e^{-\kappa_{13}^*}<1,
\qquad
\sum_{\lambda\ne0,\rho}d_\lambda |k_{\lambda,j}|
\le
\epsilon_{ch},
```

cofinally, with the real-paired convention for non-self-conjugate `rho`.
The second inequality is not needed for the numerical value of
`\kappa_{13}^*`; it is included because Paper 13 `CE(s_0,\rho,L)` also
requires the non-leading character remainder to be controlled by the same
decoration ledger used in `P19-T13-DEC`.

### Definition 8L.11A.22G.4A: Sharp Coefficient-Window Values `P19-T13-CEWIN-EVAL`

Assume `P19-T13-COEFF-FRZ(rho,s_0,B_{CR},K_p)`. Define the sharp leading
coefficient exponent and non-leading character-tail ceiling by

```math
\kappa_{13}^{CE}
:=
\liminf_j\left(-\log k_{\rho,j}\right),
```

provided `0<k_{\rho,j}<1` cofinally, and

```math
\epsilon_{13}^{CE}
:=
\limsup_j
\sum_{\lambda\ne0,\rho}
d_\lambda |k_{\lambda,j}|.
```

If `k_{\rho,j}` is not cofinally in `(0,1)`, set the leading window status
to **failed** for this frozen target. If the non-leading tail limsup is
infinite, set the finite-tail status to **failed** for this frozen target.

The sharp coefficient-window route can pass only if

```math
\kappa_{13}^{CE}>0,
\qquad
\epsilon_{13}^{CE}<\infty.
```

### Theorem 8L.11A.22G.4B: Exact Decision For `P19-T13-CEWIN`

Assume `P19-T13-CEWIN-EVAL`.

1. If `\kappa_{13}^{CE}>0` and `\epsilon_{13}^{CE}<\infty`, then for every
   strict pair

   ```math
   0<\kappa_{13}^*<\kappa_{13}^{CE},
   \qquad
   \epsilon_{ch}>\epsilon_{13}^{CE},
   ```

   the audit `P19-T13-CEWIN(kappa_13^*,epsilon_ch)` holds.
2. If `P19-T13-CEWIN(kappa_13^*,epsilon_ch)` holds, then necessarily

   ```math
   \kappa_{13}^{CE}\ge\kappa_{13}^*,
   \qquad
   \epsilon_{13}^{CE}\le\epsilon_{ch}.
   ```

3. If the leading coefficient is not cofinally in `(0,1)`, or
   `\kappa_{13}^{CE}\le0`, or `\epsilon_{13}^{CE}=\infty`, then no positive
   finite same-record coefficient window is proved by this route. If the
   first or third failure is exact, `P19-T13-CEWIN` fails for the frozen
   target.

Boundary equality cases are decided by the original eventual inequalities
in Definition 8L.11A.22G.4, not by liminf/limsup alone.

Proof.

For clause 1, strictness and the definitions of `liminf` and `limsup` imply
that, for all sufficiently large `j`,

```math
-\log k_{\rho,j}\ge\kappa_{13}^*,
\qquad
\sum_{\lambda\ne0,\rho}d_\lambda |k_{\lambda,j}|
\le\epsilon_{ch}.
```

The first inequality is equivalent to
`0<k_{\rho,j}\le e^{-\kappa_{13}^*}<1`, giving the leading part of
`P19-T13-CEWIN`; the second gives the non-leading tail part. Clause 2 follows
by taking `liminf` and `limsup` in the two displayed inequalities of
Definition 8L.11A.22G.4. Clause 3 is the contrapositive of the necessary
conditions, with the additional observation that failure of cofinal
positivity or finite non-leading tail directly violates Paper 13's
`CE(s_0,rho,L)` coefficient window. `square`

### Definition 8L.11A.22G.4C: Six-Step Actual Coefficient-Window Attack `P19-T13-CEWIN-ACT`

The actual attack on `P19-T13-CEWIN` is the following ordered audit. It is
deliberately written as a record-law audit, not as a computation in a hidden
gauge-fixed field state.

1. **Plaquette marginal identification.** Freeze the same pushed-forward
   scalar record tower as in `P19-T13-COEFF-FRZ`. For each row `j`, the
   one-block plaquette marginal is

   ```math
   K_{p,j}:=(\pi_{p,j})_*\nu_j^{WP},
   ```

   where `\nu_j^{WP}` is the exact whole-process row law after the declared
   block/counterterm/projective readout, and `\pi_{p,j}` is the central
   block-plaquette scalar readout. If this marginal does not admit the
   central density required by Paper 13 Definition 7.30AE on a cofinal tail,
   the `CE` route fails at the absolute-continuity part of the coefficient
   gate.

2. **Leading coefficient interval.** Compute the Haar-projection coefficient

   ```math
   k_{\rho,j}
   =
   {\langle K_{p,j},\chi_\rho\rangle\over
    \langle\chi_\rho,\chi_\rho\rangle}
   ```

   with the real-paired convention for non-self-conjugate `rho`. The first
   hard test is

   ```math
   0<k_{\rho,j}<1
   ```

   cofinally.

3. **Positive leading rate.** On the branch where the interval test passes,
   define

   ```math
   \kappa_{\rho,j}:=-\log k_{\rho,j},
   \qquad
   \kappa_{13}^{CE}:=\liminf_j\kappa_{\rho,j}.
   ```

   The rate test is `\kappa_{13}^{CE}>0`.

4. **Non-leading character tail.** With the same representation schedule and
   the same decoration ledger used in `P19-T13-DEC`, compute

   ```math
   E_{CE,j}
   :=
   \sum_{\lambda\ne0,\rho}
   d_\lambda |k_{\lambda,j}|,
   \qquad
   \epsilon_{13}^{CE}:=\limsup_j E_{CE,j}.
   ```

   The tail test is `\epsilon_{13}^{CE}<\infty`. A stronger small-tail
   version may be needed later to keep `eta_dec` and the final `T_13`
   margin positive, but finite tail is the exact `CEWIN` entry condition.

5. **Same-record debit audit.** The leading coefficient uses no additional
   projective, regulator, volume, or loop-readout debit. Those terms remain
   in `T_11`, `T_12`, or `T_14`. The only coefficient-window debit allowed
   here is the non-leading character remainder already assigned to the
   decoration ledger in `P19-T13-DEC`.

6. **Decision.** If steps 1--4 pass, choose any strict constants

   ```math
   0<\kappa_{13}^*<\kappa_{13}^{CE},
   \qquad
   \epsilon_{ch}>\epsilon_{13}^{CE},
   ```

   and close `P19-T13-CEWIN` by Theorem 8L.11A.22G.4B. If any exact failure
   in steps 1, 2, or 4 is proved, the frozen coefficient-window route fails.
   If step 3 has `\kappa_{13}^{CE}\le0`, no positive leading rate is proved
   by this route, and the reduced surface-polymer proof cannot use
   `P19-T13-LEAD` with a positive rate.

### Definition 8L.11A.22G.4C.1: Plaquette Density Regularity `P19-T13-KPREG`

`P19-T13-KPREG` holds for the frozen coefficient target when, for every
cofinal row `j`, the block plaquette marginal `K_{p,j}` of Definition
8L.11A.22G.4C is represented by a central Haar density

```math
K_{p,j}\in L^1(SU(N),dHaar),
\qquad
K_{p,j}\ge0,
\qquad
\int_{SU(N)}K_{p,j}(U)\,dHaar(U)=1,
```

and its central Peter-Weyl coefficients

```math
k_{\lambda,j}
:=
{\langle K_{p,j},\chi_\lambda\rangle_{L^2(SU(N))}
\over
\langle\chi_\lambda,\chi_\lambda\rangle_{L^2(SU(N))}}
```

exist for every irreducible `\lambda`. The Peter-Weyl statement meant here
is the canonical `L^1`/distribution statement:

```math
K_{p,j}*H_\tau
=
\sum_{\lambda\in\widehat{SU(N)}}
e^{-\tau C_2(\lambda)/2}k_{\lambda,j}\chi_\lambda
\longrightarrow K_{p,j}
\quad\text{in }L^1
\quad(\tau\downarrow0),
```

where `H_\tau` is the heat-kernel approximate identity on `SU(N)`.

This regularity is only the analytic prerequisite for the coefficient
window. It does not imply

```math
0<k_{\rho,j}<1,
\qquad
\liminf_j-\log k_{\rho,j}>0,
\qquad
\limsup_j\sum_{\lambda\ne0,\rho}d_\lambda|k_{\lambda,j}|<\infty.
```

Those remain the sign/rate/tail tests of `P19-T13-CEWIN-ACT`.

### Theorem 8L.11A.22G.4C.2: Finite Heat-Kernel Rows Prove `P19-T13-KPREG`

Assume the frozen coefficient target is evaluated on the Paper-16
heat-kernel actual trajectory `HK-AYM` before taking any weak continuum
subsequence, with the same finite block/counterterm/projective readout used
by `P19-TR-COMMON`. Then `P19-T13-KPREG` holds on the selected cofinal
finite rows.

Proof.

Fix a row `j`. The underlying cutoff link space is a finite product
`G^{E_j}` with `G=SU(N)`, and Paper 16 Definition 9C.1 gives a finite
heat-kernel measure

```math
d\mu_j^{HK}(U)
=
Z_j^{-1}\prod_p K_{t_j}(U_p(U))\prod_e dHaar(U_e).
```

Its density

```math
F_j(U):=Z_j^{-1}\prod_p K_{t_j}(U_p(U))
```

is nonnegative and integrable with integral one. For positive heat-kernel
time it is in fact smooth and strictly positive on the compact finite link
space, but `L^1` is enough here.

Let

```math
P_j:G^{E_j}\to G
```

be the declared block plaquette holonomy readout before centralization. The
pushforward of product Haar by `P_j` is Haar on `G`: multiplication,
inversion, and left/right translation preserve Haar, and one link variable
on a plaquette boundary can be used as the final Haar variable after the
other finitely many links are held fixed. Hence, if `A subset G` has Haar
measure zero, then `P_j^{-1}(A)` has product-Haar measure zero.

Therefore the pushed-forward plaquette law

```math
(P_j)_*(F_j\,dHaar^{E_j})
```

is absolutely continuous with respect to Haar. Its Radon-Nikodym derivative
is the conditional expectation

```math
K_{p,j}(V)
=
E_{dHaar^{E_j}}\left[F_j(U)\mid P_j(U)=V\right],
```

defined Haar-a.e. Consequently `K_{p,j}\in L^1(G)`,
`K_{p,j}\ge0`, and `\int K_{p,j}\,dHaar=1`.

Gauge invariance gives centrality. A gauge transformation at the base point
of the block plaquette sends `P_j(U)` to `gP_j(U)g^{-1}`. The heat-kernel
action, Haar measure, counterterm convention, and closed scalar readout are
invariant under this change of variables. Hence the plaquette marginal is
conjugation invariant:

```math
K_{p,j}(gVg^{-1})=K_{p,j}(V)
```

for Haar-a.e. `V`; replacing `K_{p,j}` by its conjugation average if needed
gives a central representative without changing the law.

Finally, since `K_{p,j}` is a central `L^1` function on the compact group
`SU(N)`, every character coefficient

```math
k_{\lambda,j}
=
{\langle K_{p,j},\chi_\lambda\rangle\over
\langle\chi_\lambda,\chi_\lambda\rangle}
```

exists because characters are bounded. The heat kernels `H_\tau` form a
central approximate identity on `SU(N)`, so
`K_{p,j}*H_\tau\to K_{p,j}` in `L^1`. Peter-Weyl diagonalizes heat-kernel
convolution on central functions, giving

```math
K_{p,j}*H_\tau
=
\sum_\lambda e^{-\tau C_2(\lambda)/2}k_{\lambda,j}\chi_\lambda.
```

This is exactly `P19-T13-KPREG`. `square`

### Honest Boundary 8L.11A.22G.4C.3: Regularity Does Not Survive Weak Limits For Free

Theorem 8L.11A.22G.4C.2 is a finite-row heat-kernel theorem. If one
reinterprets `K_{p,j}` as an already-taken weak continuum plaquette marginal
rather than as the cofinal finite-row marginal used in the Paper-19 source
ledger, then absolute continuity with respect to Haar is not automatic:
weak limits of absolutely continuous measures may be singular. In that
interpretation one must add a separate same-record compactness estimate,
for example uniform integrability of the densities or convergence in total
variation on the finite plaquette record. Paper 19 uses the finite-row
source-ledger interpretation, so Theorem 8L.11A.22G.4C.2 is the relevant
regularity input.

### Lemma 8L.11A.22G.4D: Step 1 Target Identification Is Not A Coefficient Estimate

Assume `P19-TR-COMMON` and
`P19-T13-COEFF-FRZ(rho,s_0,B_{CR},K_p)`. Then step 1 of
`P19-T13-CEWIN-ACT` has a unique target marginal `K_{p,j}` on the declared
row. If the target is evaluated on finite heat-kernel rows, Theorem
8L.11A.22G.4C.2 also gives central `L^1` Peter-Weyl regularity. However,
neither target identification nor density regularity proves the
coefficient-window inequalities of steps 2--4.

Proof.

`P19-TR-COMMON` fixes the whole-process row law, and
`P19-T13-COEFF-FRZ` fixes the block scale, Creutz battery, plaquette readout,
counterterm convention, projection map, and central scalar readout. Hence
the pushforward `(\pi_{p,j})_*\nu_j^{WP}` is a unique scalar record-law
marginal. Theorem 8L.11A.22G.4C.2 adds the finite-row absolute-continuity,
centrality, and Peter-Weyl coefficient existence needed to make the Haar
projections meaningful. But those facts are still not coefficient estimates:
no sign, upper bound, logarithmic liminf, or weighted non-leading character
tail follows merely from the existence of a central `L^1` density. Those are
exactly steps 2--4. `square`

### Definition 8L.11A.22G.4D.1: Leading Sign Audit `P19-T13-CSIGN`

`P19-T13-CSIGN(rho)` is the step-2 sign audit for the frozen coefficient
target. It holds when the Haar-projection coefficient of the selected
nontrivial scalar character satisfies

```math
k_{\rho,j}
=
{\langle K_{p,j},\chi_\rho\rangle\over
 \langle\chi_\rho,\chi_\rho\rangle}
>0
```

on a cofinal tail, with the real-paired convention for non-self-conjugate
`\rho`.

The audit is intentionally only a sign audit. It does not assert
`k_{\rho,j}<1`, a positive liminf rate, or a finite non-leading tail.

### Lemma 8L.11A.22G.4D.2: Density Regularity Alone Does Not Prove The Sign

`P19-T13-KPREG` does not imply `P19-T13-CSIGN(rho)` for a nontrivial
representation `rho`.

Proof.

Let `\Phi_\rho` denote the real scalar central record used for `rho`
itself if `rho` is self-conjugate, and the real-paired central record
otherwise. Since `rho` is nontrivial, `\int\Phi_\rho\,dHaar=0`. The record
is continuous and not identically zero, so it has both positive and negative
regions. Choose a conjugation-invariant open set `U_-` on which
`\Phi_\rho<0`.

Choose a nonnegative central smooth function `f` supported in `U_-` with
`\int f\,dHaar=1`. Then `f` is a central `L^1` density, has a Peter-Weyl
expansion in the heat-regularized `L^1` sense of `P19-T13-KPREG`, but

```math
{\langle f,\Phi_\rho\rangle\over
 \langle\Phi_\rho,\Phi_\rho\rangle}<0.
```

Thus the regularity theorem makes the coefficient meaningful, but it cannot
force the coefficient to be positive. Positivity must come from an additional
source estimate about the actual heat-kernel block record law. `square`

### Definition 8L.11A.22G.4D.3: Reference-Defect Sign Route `P19-T13-CSIGN-REF`

Fix a same-record positive reference coefficient `u_{\rho,j}^{ref}>0`, for
example the heat-kernel block reference coefficient on the same selected
block scale and same representation channel. Define the leading sign defect

```math
\delta_{\rho,j}^{sign}
:=
|k_{\rho,j}-u_{\rho,j}^{ref}|.
```

The reference-defect sign route holds if there is a scalar `r_{sign}<1`
such that, cofinally,

```math
\delta_{\rho,j}^{sign}
\le
r_{sign}\,u_{\rho,j}^{ref}.
```

Equivalently,

```math
\limsup_j
{\delta_{\rho,j}^{sign}\over u_{\rho,j}^{ref}}
<1.
```

For the AF-matched heat-kernel reference used in Section 8J, this is the
same scale as the relative coefficient error

```math
r_j=\delta_j e^{a_j},
\qquad
u_{\rho,j}^{ref}=e^{-a_j},
```

provided the `\delta_j` in Section 8J is the same same-record leading
coefficient defect for the frozen `P19-T13` target.

### Theorem 8L.11A.22G.4D.4: Reference-Defect Route Proves The Leading Sign

If `P19-T13-CSIGN-REF` holds for the frozen coefficient target, then
`P19-T13-CSIGN(rho)` holds.

Proof.

For all sufficiently large `j`,

```math
k_{\rho,j}
\ge
u_{\rho,j}^{ref}-\delta_{\rho,j}^{sign}
\ge
(1-r_{sign})u_{\rho,j}^{ref}.
```

Since `u_{\rho,j}^{ref}>0` and `r_{sign}<1`, the right-hand side is
positive. Hence `k_{\rho,j}>0` cofinally. `square`

### Theorem 8L.11A.22G.4D.5: AF-Matched Coefficient-Error Route Proves The Sign When It Is Same-Target

Assume the AF-matched coefficient-error audit of Section 8J is evaluated on
the same frozen coefficient target as `P19-T13-CEWIN`, with

```math
u_{\rho,j}^{ref}=e^{-a_j},
\qquad
\delta_{\rho,j}^{sign}=\delta_j,
\qquad
r_j=\delta_j e^{a_j}.
```

If the Section-8J relative error satisfies

```math
\limsup_j r_j<1,
```

then `P19-T13-CSIGN(rho)` holds.

Proof.

The displayed identities give

```math
{\delta_{\rho,j}^{sign}\over u_{\rho,j}^{ref}}
=
\delta_j e^{a_j}
=r_j.
```

Thus `\limsup_j r_j<1` is exactly `P19-T13-CSIGN-REF`; apply Theorem
8L.11A.22G.4D.4. `square`

### Theorem 8L.11A.22G.4D.6: Current Verdict On The Leading Sign

With the current source papers, `P19-T13-CSIGN(rho)` is not proved
unconditionally and is not falsified for the actual frozen coefficient
target.

What is proved is the exact route:

```text
same-target reference defect below the positive heat-kernel coefficient
=> k_rho,j>0 cofinally.
```

What is missing is the actual same-record estimate

```math
\limsup_j
{\delta_{\rho,j}^{sign}\over u_{\rho,j}^{ref}}
<1
```

for the frozen `P19-T13` block plaquette marginal. Section 8J gives the
right relative-error ledger and several exact pass/fail criteria for such a
coefficient defect, but Theorem 8J.11I records that the needed fixed-time or
matched-time source estimate is not supplied unconditionally by current
Papers 13--16.

Consequently the honest status of step 2 is:

```text
regularity + reference-defect theorem proved;
actual same-target defect estimate missing;
leading sign not yet proved and not yet falsified.
```

Proof.

Lemma 8L.11A.22G.4D.2 shows that `P19-T13-KPREG` alone cannot prove the
sign. Theorem 8L.11A.22G.4D.4 proves the sufficient reference-defect route,
and Theorem 8L.11A.22G.4D.5 identifies the AF-matched Section-8J version
when it is evaluated on the same coefficient target. The current source
papers do not prove the required strict relative-defect bound for the frozen
`P19-T13` target, and they also do not prove an opposite lower bound forcing
`k_{\rho,j}\le0` cofinally. Therefore the sign is conditionally reduced but
not unconditionally decided. `square`

### Definition 8L.11A.22G.4D.7: Subunit Coefficient Audit `P19-T13-CUNIT`

`P19-T13-CUNIT(rho)` is the upper-bound half of the step-2 coefficient
window. It holds when

```math
k_{\rho,j}<1
```

on a cofinal tail.

This is independent of positivity. The full leading interval
`0<k_{\rho,j}<1` is the conjunction of `P19-T13-CSIGN(rho)` and
`P19-T13-CUNIT(rho)`.

### Lemma 8L.11A.22G.4D.8: Density Regularity And Positivity Do Not Prove The Subunit Bound

`P19-T13-KPREG` and `P19-T13-CSIGN(rho)` do not imply
`P19-T13-CUNIT(rho)`.

Proof.

Use the declared Paper-13 character convention in which the coefficient is
the Haar projection onto `\chi_\rho` or the real paired record `\Phi_\rho`.
For `SU(N)`, every nontrivial irreducible representation has dimension
`d_\rho>1`, and the declared central record has value `d_\rho` at the
identity.

Choose a nonnegative central smooth density `f_\epsilon` supported in a
small conjugation-invariant neighborhood of the identity, normalized by
`\int f_\epsilon\,dHaar=1`. By continuity,

```math
{\langle f_\epsilon,\chi_\rho\rangle\over
 \langle\chi_\rho,\chi_\rho\rangle}
\longrightarrow d_\rho
```

as the neighborhood shrinks, with the analogous statement for the real
paired record. For sufficiently small `\epsilon`, the coefficient is
positive and greater than one. The density is central, smooth, and has the
Peter-Weyl regularity required by `P19-T13-KPREG`. Hence regularity plus
positivity does not prove the subunit bound. `square`

### Definition 8L.11A.22G.4D.9: Reference-Gap Upper Route `P19-T13-CUNIT-REF`

Fix a same-record reference coefficient satisfying

```math
0<u_{\rho,j}^{ref}<1
```

cofinally, and use the same leading defect as in the sign route:

```math
\delta_{\rho,j}^{sign}
:=
|k_{\rho,j}-u_{\rho,j}^{ref}|.
```

The reference-gap upper route holds if

```math
\limsup_j
{\delta_{\rho,j}^{sign}\over1-u_{\rho,j}^{ref}}
<1.
```

Equivalently, there is `r_{unit}<1` such that cofinally

```math
\delta_{\rho,j}^{sign}
\le
r_{unit}(1-u_{\rho,j}^{ref}).
```

### Theorem 8L.11A.22G.4D.10: Reference-Gap Route Proves The Subunit Bound

If `P19-T13-CUNIT-REF` holds for the frozen coefficient target, then
`P19-T13-CUNIT(rho)` holds.

Proof.

For all sufficiently large `j`,

```math
k_{\rho,j}
\le
u_{\rho,j}^{ref}+\delta_{\rho,j}^{sign}
\le
u_{\rho,j}^{ref}+r_{unit}(1-u_{\rho,j}^{ref})
<1,
```

because `0<u_{\rho,j}^{ref}<1` and `r_{unit}<1`. `square`

### Theorem 8L.11A.22G.4D.11: AF-Matched Error Route Proves The Subunit Bound When It Is Same-Target

Assume the AF-matched coefficient-error audit of Section 8J is evaluated on
the same frozen coefficient target as `P19-T13-CEWIN`, with

```math
u_{\rho,j}^{ref}=e^{-a_j},
\qquad
\delta_{\rho,j}^{sign}=\delta_j,
\qquad
r_j=\delta_je^{a_j}.
```

Then

```math
{\delta_{\rho,j}^{sign}\over1-u_{\rho,j}^{ref}}
=
{r_j\over e^{a_j}-1}.
```

Consequently `P19-T13-CUNIT(rho)` holds if

```math
\limsup_j {r_j\over e^{a_j}-1}<1.
```

A sufficient AF-normalized form is: if

```math
\limsup_j H_jr_j\le R_H,
\qquad
\liminf_j H_j(e^{a_j}-1)\ge A_{unit},
\qquad
R_H<A_{unit},
```

then `P19-T13-CUNIT(rho)` holds. Under the Paper-16 scheme slack

```math
1-\chi\le {t_{i(j)}\over g_{i(j)}^2},
\qquad
H_j=g_{i(j)}^{-2},
```

one may take

```math
A_{unit}={(1-\chi)C_2(\rho)\over2},
```

because `e^a-1\ge a` and
`a_j=t_{i(j)}C_2(\rho)/2`.

Proof.

The identity follows from

```math
1-e^{-a_j}=e^{-a_j}(e^{a_j}-1),
\qquad
\delta_j=r_je^{-a_j}.
```

The strict limsup condition is exactly `P19-T13-CUNIT-REF`, so Theorem
8L.11A.22G.4D.10 applies. For the AF-normalized sufficient form,

```math
{r_j\over e^{a_j}-1}
=
{H_jr_j\over H_j(e^{a_j}-1)}.
```

The displayed limsup/liminf inequalities give an eventual upper bound
strictly below one. The scheme-slack lower bound gives

```math
H_j(e^{a_j}-1)\ge H_ja_j
\ge {(1-\chi)C_2(\rho)\over2}.
```

`square`

### Theorem 8L.11A.22G.4D.12: Current Verdict On The Subunit Bound

With the current source papers, `P19-T13-CUNIT(rho)` is not proved
unconditionally and is not falsified for the actual frozen coefficient
target.

What is proved is the exact route:

```text
same-target defect below the reference gap 1-u_ref
=> k_rho,j<1 cofinally.
```

For the AF-matched heat-kernel reference, the required source estimate is

```math
\limsup_j {r_j\over e^{a_j}-1}<1,
```

or, in sufficient normalized form,

```math
R_H<{(1-\chi)C_2(\rho)\over2}.
```

This is stronger than the sign route because the allowed defect is not the
positive reference `u_{\rho,j}^{ref}` itself, but the shrinking gap
`1-u_{\rho,j}^{ref}`. Current Papers 13--16 provide the coefficient-error
ledger and the exact Section-8J pass/fail criteria, but they do not supply
the strict same-target bound above, nor do they supply a lower bound forcing
`k_{\rho,j}\ge1` cofinally. Therefore the subunit bound is conditionally
reduced but not unconditionally decided. `square`

### Definition 8L.11A.22G.4D.13: Positive Rate Audit `P19-T13-CRATE(kappa_*)`

`P19-T13-CRATE(kappa_*)` is the positive-rate part of the leading
coefficient window. It holds when the same frozen coefficient sequence
`k_{\rho,j}` satisfies, on a cofinal tail,

```math
k_{\rho,j}>0
```

and

```math
\liminf_j(-\log k_{\rho,j})\ge\kappa_*>0.
```

Equivalently, after passing to a cofinal tail, there is a scalar
`q_*<1` such that

```math
0<k_{\rho,j}\le q_*,
\qquad
\kappa_*<-\log q_*.
```

Thus the positive-rate audit is strictly stronger than the interval audit
`0<k_{\rho,j}<1`: it requires a uniform gap away from `1`.

### Lemma 8L.11A.22G.4D.14: The Interval Bound Does Not Prove Positive Rate

`P19-T13-KPREG`, `P19-T13-CSIGN(rho)`, and `P19-T13-CUNIT(rho)` do not
imply `P19-T13-CRATE(kappa_*)` for any `kappa_*>0`.

Proof.

By Lemma 8L.11A.22G.4D.2 there is a central smooth probability density
`f_-` whose `rho`-coefficient is negative. By Lemma 8L.11A.22G.4D.8 there
is a central smooth probability density `f_+` whose `rho`-coefficient is
greater than one. The coefficient map

```math
f\mapsto
{\langle f,\chi_\rho\rangle\over\langle\chi_\rho,\chi_\rho\rangle}
```

or its real-paired variant is linear. Hence, for each `j>=2`, a convex
combination of `f_-` and `f_+` has coefficient

```math
k_{\rho,j}=1-{1\over j}.
```

Each convex combination is again a central smooth probability density and
therefore has the regularity required by `P19-T13-KPREG`. Moreover
`0<k_{\rho,j}<1` for every `j>=2`, but

```math
\liminf_j[-\log(1-1/j)]=0.
```

So sign and subunit bounds alone do not supply a positive logarithmic
rate. `square`

### Definition 8L.11A.22G.4D.15: Reference-Rate Route `P19-T13-CRATE-REF`

Fix the same-record positive reference coefficient and leading defect used
in Definitions 8L.11A.22G.4D.3 and 8L.11A.22G.4D.9:

```math
0<u_{\rho,j}^{ref}<1,
\qquad
\delta_{\rho,j}^{sign}
:=
|k_{\rho,j}-u_{\rho,j}^{ref}|.
```

The reference-rate route holds when the sign route holds and when the
reference plus defect remains uniformly below one:

```math
q_{rate}^{ref}
:=
\limsup_j
\left(u_{\rho,j}^{ref}+\delta_{\rho,j}^{sign}\right)
<1.
```

In that case every

```math
0<\kappa_*<-\log q_{rate}^{ref}
```

is an admissible target rate.

### Theorem 8L.11A.22G.4D.16: Reference-Rate Route Proves Positive Rate

If `P19-T13-CRATE-REF` holds for the frozen coefficient target, then
`P19-T13-CRATE(kappa_*)` holds for every

```math
0<\kappa_*<-\log q_{rate}^{ref}.
```

Proof.

The sign part of `P19-T13-CRATE-REF` gives `k_{\rho,j}>0` cofinally. Also,
for every `q` with `q_{rate}^{ref}<q<1`, the limsup definition gives

```math
k_{\rho,j}
\le
u_{\rho,j}^{ref}+\delta_{\rho,j}^{sign}
\le q
```

cofinally. Hence

```math
-\log k_{\rho,j}\ge -\log q
```

cofinally. Letting `q` decrease to `q_{rate}^{ref}` gives the stated
positive liminf bound. `square`

### Theorem 8L.11A.22G.4D.17: AF-Matched Log-Margin Route For The Positive Rate

Assume the AF-matched coefficient-error audit of Section 8J is evaluated on
the same frozen coefficient target as `P19-T13-CEWIN`, with

```math
u_{\rho,j}^{ref}=e^{-a_j},
\qquad
\delta_{\rho,j}^{sign}=\delta_j,
\qquad
r_j=\delta_je^{a_j}.
```

Assume also the sign route, for instance `\limsup_j r_j<1`. If

```math
A_{rate}^-
:=
\liminf_j\left(a_j-\log(1+r_j)\right)
>0,
```

then

```math
\kappa_{13}^{CE}
:=
\liminf_j(-\log k_{\rho,j})
\ge
A_{rate}^-
>0.
```

Equivalently, a sufficient separated form is

```math
\liminf_j a_j\ge a_->0,
\qquad
\limsup_j\log(1+r_j)\le e_+<a_-.
```

Proof.

The same-target defect identity gives

```math
k_{\rho,j}
\le
e^{-a_j}+\delta_j
=
e^{-a_j}(1+r_j).
```

On the cofinal tail where the sign route gives `k_{\rho,j}>0`, taking
negative logarithms yields

```math
-\log k_{\rho,j}
\ge
a_j-\log(1+r_j).
```

Taking liminf proves the first claim. The separated form implies
`A_rate^- >= a_- - e_+ >0`. `square`

### Theorem 8L.11A.22G.4D.18: Vanishing-Reference Branch Falsifies Positive Rate If It Is The Actual Target

Suppose the same frozen coefficient target satisfies

```math
u_{\rho,j}^{ref}\to1,
\qquad
\delta_{\rho,j}^{sign}\to0.
```

Then

```math
k_{\rho,j}\to1.
```

If `k_{\rho,j}>0` cofinally, then

```math
\kappa_{13}^{CE}
=
\liminf_j(-\log k_{\rho,j})
=0.
```

Consequently `P19-T13-CRATE(kappa_*)` fails for every `kappa_*>0` on that
branch.

In particular, the fixed microscopic AF heat-kernel reference with
`a_j\to0`, so `u_{\rho,j}^{ref}=e^{-a_j}\to1`, cannot prove positive rate.
If the actual frozen coefficient is same-target asymptotic to that
reference, then this branch does not merely fail as a proof route; it
falsifies the positive-rate conclusion for the selected coefficient target.

Proof.

The defect bound gives

```math
|k_{\rho,j}-u_{\rho,j}^{ref}|
=
\delta_{\rho,j}^{sign}\to0.
```

Since `u_{\rho,j}^{ref}\to1`, it follows that `k_{\rho,j}\to1`. On the
cofinal positive tail, continuity of `-\log` at `1` gives
`-\log k_{\rho,j}\to0`. Hence the liminf is zero, not positive. `square`

### Theorem 8L.11A.22G.4D.19: Current Verdict On The Positive Rate

With the current source papers, the actual statement

```math
\kappa_{13}^{CE}
=
\liminf_j(-\log k_{\rho,j})
>0
```

is not proved unconditionally and is not falsified for the actual frozen
`P19-T13` coefficient target.

What is proved is the exact rate route:

```text
same-target sign
+ limsup_j (u_ref,j + delta_sign,j) < 1
=> kappa_13^CE > 0.
```

For the AF-matched heat-kernel reference, this becomes the log-margin test

```math
\liminf_j\left(a_j-\log(1+r_j)\right)>0.
```

What is also proved is the honest obstruction to a tempting shortcut:

```text
if the chosen same-target reference has u_ref,j -> 1
and the defect tends to 0, then kappa_13^CE = 0.
```

Therefore a fixed microscopic AF-time reference whose coefficient tends to
one cannot provide the `T_13` surface suppression. The positive-rate source
must instead be a genuinely block-scale or area-matched same-record estimate
with a nonzero log margin, or a direct computation of `k_{\rho,j}` showing a
uniform gap from one.

Current Papers 13--16 provide the coefficient ledger, the exact fixed-time
and matched-time bookkeeping tests, and the consequences of a positive
`kappa_sheet`; they do not yet supply the same-target inequality
`liminf(a_j-log(1+r_j))>0`, and they do not prove that the actual frozen
coefficient target is asymptotic to the vanishing-reference branch. Thus the
positive rate is reduced to an exact source estimate but not yet decided.
`square`

### Definition 8L.11A.22G.4D.20: Non-Leading Tail Audit `P19-T13-CTAIL(epsilon_*)`

For the frozen coefficient target, define the non-leading coefficient tail

```math
E_{CE,j}
:=
\sum_{\lambda\ne0,\rho}
d_\lambda |k_{\lambda,j}|.
```

The audit `P19-T13-CTAIL(epsilon_*)` holds when

```math
\epsilon_{13}^{CE}
:=
\limsup_j E_{CE,j}
\le
\epsilon_*<\infty.
```

The sum is interpreted with the same real-paired convention and the same
declared representation/decorrelation ledger as `P19-T13-DEC`: the selected
`\rho` channel is removed once, its conjugate is not charged again in the
real-paired case, and all remaining below-cutoff character records together
with the above-cutoff Weyl-Casimir tail are exactly the Paper-15
`Tail_CE,j` object. No second representation cutoff is introduced here.

### Lemma 8L.11A.22G.4D.21: Same-Decoration Ledger Identifies The CE Tail

Assume `P19-T13-COEFF-FRZ(rho,s_0,B_CR,K_p)` and the same cofinal
representation/decorrelation schedule used by `P19-CHTAIL-AUDIT`. Then, for
every row `j`,

```math
E_{CE,j}\le Tail_{CE,j}.
```

If `Tail_CE,j` is defined as the full Paper-13 character norm rather than as
an envelope, then equality holds.

Proof.

Clause 6 of `P19-T13-COEFF-FRZ` requires the non-leading coefficient tail in
`P19-T13-CEWIN` to be measured with the same representation cutoff and same
decoration ledger as `P19-T13-DEC`. Paper 13 Definition 7.30AE and
Proposition 7.30AF define the `CE` remainder norm as

```math
\sum_{\lambda\ne0,\rho}d_\lambda|k_{\lambda,j}|,
```

with the real-paired convention for non-self-conjugate `rho`. Paper 15 names
the corresponding coefficient-entry envelope `Tail_CE,j` when that remainder
is inserted into the decoration gas. Therefore the exact character norm is
bounded by the Paper-15 tail envelope, and it is equal to it when the
envelope is chosen sharply. The above-cutoff part is not discarded; it is
included in `Tail_CE,j` through the same Weyl-Casimir tail bound used in
`P19-CHTAIL-AUDIT`. `square`

### Theorem 8L.11A.22G.4D.22: `P19-CHTAIL-AUDIT` Bounds The Non-Leading CE Tail

Assume the normalized same-record character-tail audit

```text
P19-CHTAIL-AUDIT(eta_ch^*)
```

on the same representation/decorrelation schedule used by
`P19-T13-DEC`, with conversion constants chosen in the harmless norm
normalization

```math
C_{ch,j}\ge1.
```

Then

```math
\epsilon_{13}^{CE}
\le
\eta_{ch}^*
<\infty.
```

Consequently `P19-T13-CTAIL(eta_ch^*)` holds.

Proof.

By Lemma 8L.11A.22G.4D.21,

```math
E_{CE,j}\le Tail_{CE,j}.
```

Since the conversion constants are normalized so that `C_ch,j>=1`,

```math
Tail_{CE,j}\le C_{ch,j}Tail_{CE,j}.
```

Taking limsups and applying `P19-CHTAIL-AUDIT(eta_ch^*)` gives

```math
\epsilon_{13}^{CE}
=
\limsup_j E_{CE,j}
\le
\limsup_j C_{ch,j}Tail_{CE,j}
\le
\eta_{ch}^*.
```

The normalization `C_ch,j>=1` is not a new cutoff and not a new debit. It is
only the convention of choosing the finite character-to-record norm constant
large enough to dominate both the decoration activity and the raw coefficient
tail. The cutoff schedule remains the one already declared in
`P19-CHTAIL-AUDIT` and imported by `P19-T13-DEC`. `square`

### Corollary 8L.11A.22G.4D.23: Closing `P19-T13-DEC` Closes The Finite-Tail Part Of `CEWIN`

Under the hypotheses of Theorem 8L.11A.22F.2, choose the normalized
character-tail audit from Theorem 8L.11A.22G.4D.22. Then the same import
which closes `P19-T13-DEC(d_13^*)` also proves

```math
\epsilon_{13}^{CE}<\infty.
```

In the canonical centered square branch,

```math
\epsilon_{13}^{CE}
\le
{1-\eta_{19}^{res}\over2}.
```

Proof.

Theorem 8L.11A.22F.2 assumes `P19-CHTAIL-AUDIT(eta_ch^*)` on the same
decoration ledger. Apply Theorem 8L.11A.22G.4D.22. For the centered square
branch, Corollary 8L.8B chooses
`eta_ch^*=(1-eta_19^res)/2`. `square`

### Lemma 8L.11A.22G.4E: Paper-13/15/16 Imports Do Not Skip The Leading Coefficient Test

The current source chain does not contain an unconditional proof or
falsification of the leading interval/rate tests for actual `4D SU(N)`.
The non-leading tail is different: it is controlled whenever the same
`P19-CHTAIL-AUDIT` used by `P19-T13-DEC` is imported.

More precisely:

1. Paper 13 Proposition 7.30AF and Proposition 7.30AQ identify `CE` with the
   Haar-projection inequalities

   ```math
   0<k_{\rho}<1,
   \qquad
   \sum_{\lambda\ne0,\rho}d_\lambda |k_\lambda|\le\epsilon_{ch}.
   ```

   They prove that these inequalities are sufficient and necessary for the
   `CE` gate; they do not supply the values of the coefficients for the
   actual continuum tower.
2. Paper 15 uses the coefficient window through imported quantities
   `u_-`, `u_+`, `Tail_CE`, and `M_SUB^{bd}`. Its surface and Creutz
   reserves prove consequences after the coefficient window is supplied. It
   names the non-leading tail envelope, but it does not determine the leading
   Haar projection `k_{\rho,j}`.
3. Paper 16 `HK-SURF-CLOSE` assumes a leading sheet suppression
   `kappa_sheet` and then proves the surface reserve. Importing
   `HK-SURF-CLOSE` as a proof of `kappa_sheet>0` would be circular unless a
   separate coefficient estimate for `k_{\rho,j}` has already been proved on
   the same record tower.
4. Paper 16's character-tail closure, imported through
   `P19-CHTAIL-AUDIT`, does control the non-leading coefficient tail on the
   same representation/decorrelation ledger, by Theorem
   8L.11A.22G.4D.22. This is not a leading coefficient estimate and does not
   imply `0<k_{\rho,j}<1` or a positive rate.

Thus the available source papers close target identification, finite-row
density regularity, the non-leading tail on the declared decoration ledger,
and consequence transport. The actual leading sign and positive-rate
estimates for the frozen coefficient remain open source estimates.

Proof.

Each item is a direct dependency check. Paper 13 names the coefficient
inequalities as the content of `CE`; Paper 15 lists the coefficient window
and character tail as imported Paper-14/Paper-13 data before constructing the
decoration and surface ledgers; Paper 16 Section 9Q includes
`kappa_sheet` as an input to `HK-SURF-CLOSE`. None of these statements has a
conclusion of the form `0<k_{\rho,j}<1` cofinally,
`\liminf_j-\log k_{\rho,j}>0` for the frozen actual block marginal. The
tail conclusion is supplied separately by the same character-tail audit used
for `P19-T13-DEC`, not by the leading-sheet surface theorem. Therefore the
leading tests remain unsupplied while the finite-tail test is closed under
the declared character-tail import. `square`

### Theorem 8L.11A.22G.4F: Exhausted Outcome Of `P19-T13-CEWIN-ACT`

After executing the six-step attack with the current source ledgers, the
status is:

1. Step 1 is closed as a unique same-record target identification and, on
   the finite heat-kernel source rows, as central `L^1` Peter-Weyl
   regularity by `P19-T13-KPREG`.
2. Step 2 is reduced to two same-target reference-defect routes:
   the sign route of Theorems 8L.11A.22G.4D.4--4D.6 and the subunit route
   of Theorems 8L.11A.22G.4D.10--4D.12. It is not proved unconditionally
   and is not falsified by the current source papers.
3. Step 3 is reduced to the positive-rate route of Theorems
   8L.11A.22G.4D.16--4D.19. The fixed microscopic AF-time reference branch
   is falsified as a positive-rate source if it is same-target asymptotic to
   the actual coefficient; a block-scale or area-matched same-record
   log-margin estimate remains open.
4. Step 4 is closed by the same `P19-CHTAIL-AUDIT` used in
   `P19-T13-DEC`: Theorem 8L.11A.22G.4D.22 proves
   `epsilon_13^CE<=eta_ch^*<infinity`, with no additional representation
   cutoff.
5. Step 5 is closed as a no-double-charge debit assignment.
6. Step 6 is closed as the exact decision theorem 8L.11A.22G.4B.
7. The unfinished source tasks are exactly the sign-defect estimate

   ```math
   \limsup_j
   {\delta_{\rho,j}^{sign}\over u_{\rho,j}^{ref}}<1,
   ```

   which would imply `k_{\rho,j}>0` cofinally by Theorem
   8L.11A.22G.4D.4, the subunit defect estimate

   ```math
   \limsup_j
   {\delta_{\rho,j}^{sign}\over1-u_{\rho,j}^{ref}}<1,
   ```

   which would imply `k_{\rho,j}<1` cofinally by Theorem
   8L.11A.22G.4D.10, the positive-rate log-margin estimate

   ```math
   \liminf_j\left(a_j-\log(1+r_j)\right)>0
   ```

   on a same-target block or area-matched reference, which would imply
   `\kappa_{13}^{CE}>0` by Theorem 8L.11A.22G.4D.17.

Consequently `P19-T13-CEWIN` is not yet an unconditional theorem and is not
yet falsified. It is fully reduced to the frozen same-record Haar-projection
estimates above.

Proof.

Step 1 target uniqueness is Lemma 8L.11A.22G.4D, and finite-row regularity is
Theorem 8L.11A.22G.4C.2. The sign half of Step 2 is Theorem
8L.11A.22G.4D.6; the subunit half is Theorem 8L.11A.22G.4D.12. Step 3 is
Theorem 8L.11A.22G.4D.19. Step 4 is Theorem
8L.11A.22G.4D.22, with Corollary 8L.11A.22G.4D.23 identifying the
`P19-T13-DEC` import. Step 5 is
clause 6 of `P19-T13-COEFF-FRZ` together with Theorem 8L.11A.22F.2, which
assigns the non-leading character remainder to the already declared
decoration ledger and leaves projective/regulator/volume/loop-readout losses
in their respective `T_11`, `T_12`, and `T_14` slots. Step 6 is Theorem
8L.11A.22G.4B. Lemma 8L.11A.22G.4E proves that the current source papers do
not supply or refute the coefficient estimates required to finish the
coefficient window. Hence the only honest output is the displayed reduction
and the stated open source task. `square`

### Theorem 8L.11A.22G.5: Coefficient Window Closes `P19-T13-LEAD`

Assume `P19-T13-CEWIN(kappa_13^*,epsilon_ch)` on the same pushed-forward
record law as `P19-TR-COMMON`. Then

```text
P19-T13-LEAD(kappa_13^*)
```

holds. Moreover Paper 13 `CE(s_0,\rho,L)` holds on the same battery.

Proof.

The first displayed coefficient-window inequality gives
`0<u_{\rho,s_0,j}=k_{\rho,j}\le e^{-\kappa_{13}^*}<1` cofinally. Therefore
`-\log u_{\rho,s_0,j}\ge\kappa_{13}^*` cofinally, so
`P19-T13-LEAD(kappa_13^*)` holds by Definition 8L.11A.22G. The full pair of
coefficient-window inequalities is exactly Paper 13 Proposition 7.30AF, or
its computable Haar-projection form Proposition 7.30AQ. Hence `CE` holds on
the same scalar record battery. `square`

### Corollary 8L.11A.22G.6: Current Status Of The Leading-Coefficient Gate

After Definitions 8L.11A.22G.1A, 8L.11A.22G.2, and 8L.11A.22G.4A, the
leading coefficient is not an unnamed physics assumption. It is the explicit
Haar-projection sequence `k_{\rho,j}` on one frozen block plaquette marginal.
The six-step actual attack in Definition 8L.11A.22G.4C has now been
exhausted with the current source ledgers: the target marginal is fixed, the
finite-row heat-kernel branch gives central `L^1` Peter-Weyl regularity via
`P19-T13-KPREG`, the debit assignment is fixed, and the decision theorem is
exact. The leading sign/rate estimates remain unsupplied; the non-leading
tail is bounded by the existing character-tail audit. The
gate is closed whenever one proves a same-record coefficient window

```math
0<k_{\rho,j}\le e^{-\kappa_{13}^*}<1
```

cofinally, together with a finite non-leading character tail. The exact
liminf/limsup decision is Theorem 8L.11A.22G.4B, and the source exhaustion is
Theorem 8L.11A.22G.4F. Current Papers 13--16 define this window and prove its
consequences, but they do not yet supply an unconditional numerical lower and
upper projection estimate for actual `4D SU(N)` on the selected tower. Thus
`P19-T13-LEAD` is fully reduced and conditionally closed by
`P19-T13-CEWIN`; the non-leading value `epsilon_13^{CE}` is bounded by the
same character-tail/decorrelation ledger as `P19-T13-DEC`, while proving or
falsifying the sharp positive leading value `kappa_13^{CE}` remains the
dynamical source task.

### Theorem 8L.11A.22H: Component Audits Prove Or Fail `T_13` Subcriticality

Assume `P19-TR-COMMON`,
`P19-T13-ESURF(h_13^*)`, `P19-T13-DEC(d_13^*)`, and
`P19-T13-LEAD(kappa_13^*)`. Define the component margin

```math
\mu_{13}^{comp}
:=
\kappa_{13}^*-d_{13}^*-h_{13}^*.
```

If

```math
\mu_{13}^{comp}>0,
```

then

```math
q_{13}^{act}\le e^{-\mu_{13}^{comp}}<1,
```

and `P19-T13-SUB(q_13^*)` holds for every
`q_13^* in (e^{-\mu_{13}^{comp}},1)`.

If instead the exact evaluated constant of Definition 8L.11A.22A satisfies
`q_{13}^{act}>=1`, then the surface-polymer route fails at
`P19-T13-SUB`. If `mu_13^{comp}<=0` but `q_13^{act}` is not known to be at
least one, this component route is merely inconclusive.

Proof.

Theorem 8L.11A.22E.1 gives the entropy bound, Theorem 8L.11A.22F.1 gives
the decoration bound, and Theorem 8L.11A.22G.1 gives the leading-factor
bound. Therefore

```math
\liminf_j
\left(
-\log u_{\rho,s_0,j}
-\max_{C\in B_{CR,j}}
(\log D_{C,j}+\log E_{C,j}^{surf})
\right)
\ge
\kappa_{13}^*-d_{13}^*-h_{13}^*
=
\mu_{13}^{comp}.
```

If this is positive, Theorem 8L.11A.22C gives
`q_{13}^{act}\le e^{-\mu_{13}^{comp}}<1`, and Theorem 8L.11A.22B gives the
declared `P19-T13-SUB` pass. The fail and inconclusive clauses are exactly
the pass/fail logic of Theorem 8L.11A.22B applied to the exact limsup rather
than to this sufficient component lower bound. `square`

### Theorem 8L.11A.23: Cofinal Subcriticality Gives The Surface-Tail Formula

Assume `P19-TR-COMMON` and `P19-T13-SUB(q_13^*)`. Suppose the Paper-13
surface-polymer entry constants also satisfy the finite envelope

```math
M_{13}^{surf}
:=
\limsup_j
\max_{C\in B_{CR,j}}
A_{C,j}e^{\xi'_{C,j}}u_{\rho,s_0,j}^{N_j(C)}
<\infty.
```

Then the surface tail obeys

```math
\limsup_j S_{13,j}^{surf}
\le
M_{13}^{surf}{q_{13}^*\over 1-q_{13}^*}.
```

Consequently `P19-T13-LEDGER`'s surface clause holds with any

```math
A_{13}^{surf}
\ge
M_{13}^{surf}{q_{13}^*\over 1-q_{13}^*}.
```

Proof.

Paper 13 Proposition 7.30E and Theorem 7.30M group nonminimal sheets by
excess area `q>=1` and sum the geometric tail

```math
\sum_{q\ge1}(B_{C,j}u_{\rho,s_0,j})^q
={q_{C,j}\over1-q_{C,j}}.
```

The cofinal subcriticality assumption gives, for every `epsilon>0` and all
sufficiently large `j`,

```math
q_{C,j}\le q_{13}^*+\epsilon<1
```

uniformly over the finite Creutz battery. Hence

```math
S_{13,j}^{surf}
\le
\max_{C\in B_{CR,j}}
A_{C,j}e^{\xi'_{C,j}}u_{\rho,s_0,j}^{N_j(C)}
{q_{13}^*+\epsilon\over1-q_{13}^*-\epsilon}.
```

Taking `limsup_j` and then `epsilon downarrow 0` gives the displayed bound.
The estimate is a scalar closed-loop record estimate. The decoration factors
inside `e^{xi'}` are the Paper-13 nonminimal-sheet entry constants; any
finite-battery decoration activity already paid by `Delta_dec,j^bd` remains
excluded by `P19-TR-COMMON`'s disjoint debit register. `square`

### Definition 8L.11A.24: Exact-Entry Transport Attack `P19-T13-ENTRY(A_13^entry)`

`P19-T13-ENTRY(A_13^entry)` is the source attack for the entry transport term
`R_{13,j}^{entry}`. It holds when the Paper-13 actual-entry chain is verified
on the same pushed-forward scalar block record law as `P19-TR-COMMON`, with
a finite cofinal debit.

For row `j`, let

```math
E_{13,j}^{entry}
:=
\epsilon_{BC,j}
+\epsilon_{CE,j}
+\epsilon_{RPF,j}
+\epsilon_{KPdec,j}
+\epsilon_{SUB,j}
+\epsilon_{WP,j}.
```

The terms are the scalar residuals of the six Paper-13 actual-entry gates:
block convergence `BC`, central character extraction `CE`, residual
factorization `RPF`, decoration KP control `KP_dec`, surface
subcriticality `SUB`, and whole-process covariance `WP`. A gate proved
exactly contributes zero to its `epsilon` term. A gate proved with a
quantitative record-law comparison contributes that comparison norm. The
gate `SUB` may be counted here only if it is not already counted through
`P19-T13-SUB`; on the preferred reduced route, `epsilon_{SUB,j}=0` after
Definition 8L.11A.22 is invoked.

The attack holds when:

1. Paper 13 Definition 7.30Y's six gates are evaluated on the same record
   tower as the Paper-19 finite Creutz battery;
2. Theorem 7.30Z transports those gates to `ACSB(s_0,\rho,L)`;
3. Theorem 7.30V transports `ACSB` to the strong-block character domain and
   hence to the surface-polymer entry estimates by Theorem 7.30R;
4. Theorem 7.30M transports the surface-polymer entry estimate to exact RG
   entry, and Theorem 7.30G transports exact entry to `RSB(s_0,\rho,L)`;
5. every residual in this chain is assigned to `E_{13,j}^{entry}` and not to
   `T_11`, `T_12`, `T_14`, or `Delta_dec,j^bd`;
6. the cofinal bound

   ```math
   \limsup_jE_{13,j}^{entry}\le A_{13}^{entry}<\infty
   ```

   holds.

Then the entry clause of `P19-T13-LEDGER` holds:

```math
\limsup_jR_{13,j}^{entry}\le A_{13}^{entry}.
```

Proof.

Paper 13 Theorem 7.30Z converts the six actual-entry gates into
`ACSB(s_0,\rho,L)`. Theorem 7.30V converts `ACSB` into the strong-block
character domain and then into surface-polymer entry. Theorem 7.30M converts
surface-polymer entry into exact RG entry, and Theorem 7.30G converts exact
entry into `RSB(s_0,\rho,L)`.

By construction, every quantitative defect in this chain is one of the six
terms in `E_{13,j}^{entry}`, except for losses explicitly assigned by the
disjoint debit register to `T_11`, `T_12`, `T_14`, or `Delta_dec,j^bd`.
Therefore

```math
R_{13,j}^{entry}\le E_{13,j}^{entry}.
```

Taking the declared cofinal limsup gives
`\limsup_jR_{13,j}^{entry}\le A_{13}^{entry}`. `square`

This definition is intentionally demanding. If `BC`, `CE`, `RPF`, `KP_dec`,
`SUB`, or `WP` cannot be proved on the actual continuum tower, the entry
attack does not close. That is a real nonperturbative obstruction, not a
notation gap.

### Definition 8L.11A.25: Cutoff-To-Exact Scalar Comparison Attack `P19-T13-EXACT(A_13^exact)`

`P19-T13-EXACT(A_13^exact)` is the final scalar comparison step in the
reduced `T_13` ledger. It compares the cutoff block records used in the
surface expansion with the exact whole-process scalar entry records, after
all projective, regulator, and finite-volume transport already assigned to
other buckets has been removed.

Let `B_{13,j}^{exact}` be the finite set of scalar records needed by the
row-`j` surface-entry proof: the four Creutz loop records, the finite products
appearing in the connected entry estimates, and the finite block records
needed to evaluate the constants
`u_{\rho,s_0,j},A_{C,j},B_{C,j},\xi_{C,j},\xi'_{C,j},N_j(C)`. Define

```math
X_{13,j}^{exact}
:=
\sup_{F\in B_{13,j}^{exact}}
\left|
E_{\mu_{a_j,s_0}^{blk}}F
-
E_{\mu_{s_0}^{blk}}F
\right|
+\epsilon_{read,j}^{(13)}.
```

Here `epsilon_{read,j}^{(13)}` is the finite scalar readout tolerance for
extracting the listed constants from the exact block record. It does not
include projective drift, regulator/chart comparison, finite-volume
exhaustion, or Paper-14 whole-process errors; those are already assigned to
`T_11` or `T_14`.

The attack holds when:

1. Paper 13 Definition 7.30F's finite-battery convergence clause holds for
   the four loop records and for every scalar block record in
   `B_{13,j}^{exact}`;
2. the comparison uses the same pushed-forward whole-process law and the same
   finite battery as `P19-TR-COMMON`;
3. the cofinal bound

   ```math
   \limsup_jX_{13,j}^{exact}\le A_{13}^{exact}<\infty
   ```

   holds.

Then the exact-comparison clause of `P19-T13-LEDGER` holds:

```math
\limsup_jR_{13,j}^{exact}\le A_{13}^{exact}.
```

Proof.

Paper 13 Definition 7.30F requires convergence of the finite Creutz battery
records before exact RG entry is claimed. Definition 8L.11A.25 enlarges that
finite set only to the scalar records needed to extract the entry constants.
The supremum `X_{13,j}^{exact}` therefore dominates the cutoff-to-exact
comparison on every scalar record used by the row-`j` surface-entry proof,
with `epsilon_{read,j}^{(13)}` paying the finite readout tolerance.

The projective, regulator, chart, volume, and Paper-14 whole-process terms
are not included in `X_{13,j}^{exact}` because `P19-TR-COMMON` assigns them
outside the reduced `T_13` comparison. Thus

```math
R_{13,j}^{exact}\le X_{13,j}^{exact},
```

and the declared limsup bound gives
`\limsup_jR_{13,j}^{exact}\le A_{13}^{exact}`. `square`

If the block convergence is exact on each fixed battery and the readout
tolerance tends to zero, then `A_13^exact=0` is allowed.

### Theorem 8L.11A.26: The `T_13` Source Attacks Close The Reduced Dynamical Ledger

Assume

```text
P19-TR-COMMON,
P19-T13-SUB(q_13^*),
P19-T13-ENTRY(A_13^entry),
P19-T13-EXACT(A_13^exact),
```

and assume the finite surface envelope of Theorem 8L.11A.23. Define

```math
A_{13}^{surf}
:=
M_{13}^{surf}{q_{13}^*\over1-q_{13}^*}
```

or any larger finite number. Then

```text
P19-T13-LEDGER(A_13^surf,A_13^entry,A_13^exact)
```

holds. Consequently

```text
P19-T13-SRC(A_13^surf,A_13^entry,A_13^exact)
```

holds and

```math
\limsup_jT_{13,j}
\le
A_{13}^{surf}+A_{13}^{entry}+A_{13}^{exact}.
```

Proof.

Theorem 8L.11A.23 gives the surface-polymer tail bound and proves the
surface clause of `P19-T13-LEDGER`. Definition 8L.11A.24 gives the exact
entry transport clause. Definition 8L.11A.25 gives the cutoff-to-exact scalar
comparison clause.

The rowwise domination is exactly the reduced `T_13` ledger:

```math
T_{13,j}
\le
S_{13,j}^{surf}+R_{13,j}^{entry}+R_{13,j}^{exact}.
```

The common-record audit ensures that the surface-entry constants, entry-gate
residuals, and exact scalar comparison are evaluated on one record tower, and
that losses already assigned to `Delta_dec`, `T_11`, `T_12`, or `T_14` are
not counted again. Therefore `P19-T13-LEDGER` holds. Theorem 8L.11A.10 then
gives `P19-T13-SRC` and the displayed limsup bound. `square`

### Honest Boundary 8L.11A.27: `T_13` Is The Nonperturbative Confinement Bucket

The `T_13` attack does not prove unconditional actual `4D SU(N)`
confinement. It proves the exact dependency chain:

```text
cofinal B_C u_{rho,s0}<1
+ finite surface envelope
+ Paper-13 actual-entry gates BC, CE, RPF, KP_dec, SUB, WP
+ cutoff-to-exact scalar convergence
=> P19-T13-LEDGER.
```

If the subcriticality gate fails, the nonminimal-sheet tail diverges and the
surface route is falsified for the declared tower. If the entry gates fail,
the exact continuum block law has not been shown to enter the strong-block
surface domain. If the cutoff-to-exact scalar comparison fails, the finite
surface expansion has not been connected to the exact whole-process record.
These are the main remaining dynamical obstructions in the Paper-19 route.

### Theorem 8L.11B: Source Packages Prove The Component Audits

Assume the source packages in Definition 8L.11A hold. Then the component
audits hold with

```math
T_{11}^*
:=
A_{11}^{loc}+A_{11}^{RP}+A_{11}^{Cov}+A_{11}^{gauge},
```

```math
T_{12}^*
:=
A_{12}^{per}+A_{12}^{cusp}+A_{12}^{smear}+A_{12}^{app},
```

```math
T_{13}^*
:=
A_{13}^{surf}+A_{13}^{entry}+A_{13}^{exact},
```

and

```math
T_{14}^*:=E_{14}^*.
```

Proof.

For `T_11`, Definition 8L.11 gives the rowwise bound

```math
T_{11,j}
\le
\tau_{11,j}^{loc}
+\tau_{11,j}^{RP}
+\tau_{11,j}^{Cov}
+\tau_{11,j}^{gauge}.
```

All terms are nonnegative and live on the same pushed-forward record law, so
limsup subadditivity gives

```math
\limsup_jT_{11,j}
\le
A_{11}^{loc}+A_{11}^{RP}+A_{11}^{Cov}+A_{11}^{gauge}
=T_{11}^*.
```

The proofs for `T_12` and `T_13` are identical, using their declared
rowwise source splits. For `T_14`, Paper 14's export gives

```math
T_{14,j}\le\|E_{14}(\eta_j)\|_{tr},
\qquad
\limsup_j\|E_{14}(\eta_j)\|_{tr}\le E_{14}^*,
```

hence `limsup_j T_14,j <= E_14^*`. These are exactly the four component
audits. `square`

### Theorem 8L.11C: Component Audits Prove The Transport Loss Gate

If

```text
P19-T11-AUDIT(T_11^*),
P19-T12-AUDIT(T_12^*),
P19-T13-AUDIT(T_13^*),
P19-T14-AUDIT(T_14^*)
```

hold, then

```text
P19-DW-TLOSS-COMP(T_11^*,T_12^*,T_13^*,T_14^*)
```

holds, and therefore `P19-DW-TLOSS(T_*)` holds with

```math
T_*:=T_{11}^*+T_{12}^*+T_{13}^*+T_{14}^*.
```

Proof.

The four audit conclusions are precisely the four inequalities required by
`P19-DW-TLOSS-COMP` in Definition 8E.4. Since

```math
T_{{loss},j}^{bd}
=T_{11,j}+T_{12,j}+T_{13,j}+T_{14,j},
```

limsup subadditivity gives

```math
\limsup_jT_{{loss},j}^{bd}
\le
T_{11}^*+T_{12}^*+T_{13}^*+T_{14}^*
=T_*.
```

This is `P19-DW-TLOSS(T_*)`. `square`

### Corollary 8L.11D: Transport Source Packages Close The Transport Gate

Assume all four source packages of Definition 8L.11A hold. Define
`T_11^*`, `T_12^*`, `T_13^*`, and `T_14^*` as in Theorem 8L.11B. Then
`P19-DW-TLOSS(T_*)` holds with

```math
T_*
=
A_{11}^{loc}+A_{11}^{RP}+A_{11}^{Cov}+A_{11}^{gauge}
+A_{12}^{per}+A_{12}^{cusp}+A_{12}^{smear}+A_{12}^{app}
+A_{13}^{surf}+A_{13}^{entry}+A_{13}^{exact}
+E_{14}^*.
```

Proof.

Theorem 8L.11B proves the four component audits from the source packages.
Theorem 8L.11C then proves the transport loss gate. `square`

### Theorem 8L.11E: Exact Obstruction To The Transport-Ceiling Route

For the declared cofinal battery schedule, the component transport route
fails to supply finite ceilings exactly when at least one of the following
occurs:

1. one component source limsup in Definition 8L.11A is infinite;
2. a source component is not computed on the same pushed-forward record law;
3. a bundled source defect cannot be partitioned into the four Paper-15
   debits without double counting;
4. the Paper-14 export does not give a finite `E_14^*` on the same finite
   battery family.
5. `P19-TR-COMMON` fails, so the four ceilings are not statements about one
   whole-process record law and one debit register.

In that case Paper 19 may still prove the loss budget by a sharper direct
estimate of `limsup_j T_loss,j^bd`, but it cannot prove it through the four
component ceilings `T_11^*,T_12^*,T_13^*,T_14^*`.

Proof.

If all four source packages hold, Corollary 8L.11D supplies finite component
ceilings and hence the transport gate. Therefore failure of the component
route requires failure of at least one source package or of the common debit
partition. Conversely, if any listed obstruction occurs, then one of the
limsup bounds defining `P19-Tk-AUDIT` is either infinite, undefined on the
common record law, or counted inconsistently with the Paper-15 decomposition.
The four-ceiling proof route is then unavailable by definition. `square`

## 9. Honest Status

Paper 19 has now completed the algebraic and same-ledger reduction of the
actual source-constant program inherited from Paper 18. It proves that the
following concrete source package is sufficient:

```text
P19-TOWER
+ P16-LAW-IMPORT
+ AYM-CONF-WIN-SCHED
+ [P19-CRES-RAW(c_R) or P19-CRES-DEB(c_R)]
+ P19-KQ-SRC(W_R)
+ P19-RLD-THRESH(c_R,W_R,s_R)
+ P19-PI-SRC(s_R,m_*)
+ P19-PI-THRESH(s_P,m_*)
+ P19-COF(s_R,s_P,m_*)
=> AYM-CONF-CLOSE(m_*)
=> MGAP(m_*).
```

This is a rigorous reduction, not yet an unconditional proof of actual
`4D SU(N)` confinement. The reserve-loop branch has been sharpened from a
guessed-constant inequality to an envelope decision:

```math
s_{R,route}^{tail}
=
\max_b
\left[
\gamma_R\left(c_b^{tail}-L_{R,b}\right)
-e_R
-2\max\{E_R,4W^{tail}\}
\right]
>0?
```

If yes, the reserve-loop component is proved; if no, the Paper-18
minimal-debit confinement route fails for the declared tower, target
windows, and selector family. Section 8B fully resolves Step 1a as a
decision problem for the debited reserve, and it refines the direct Paper-15
witness into the source gates `P19-DW-SIG(Theta_*,Phi_*)` and
`P19-DW-LOSS(D_*,T_*)`. Section 8C bounds the leading-sheet exponent
`Theta_j`: fixed finite Creutz batteries pass this part, but growing-window
area-law schedules require the stronger scaling
`-log u_{-,j}=O(1/N_{0,j})`. Section 8D lower-bounds the first-excess
exponent `Phi_j` and shows that, under comparable coefficient windows, a
growing-window direct witness also needs `Q_{\sigma,j}/N_{0,j}` bounded away
from zero. Section 8E reduces the loss side to a decoration gate
`eta_dec^bd<1` with finite `c_Delta^*`, a four-term transport-loss ceiling,
and the strict scalar inequality
`e^{-Theta_*}(1-e^{-Phi_*})>D_*+T_*`. The loss-side source constants are then
sharpened in Section 8L.7--11: `eta_ch^sharp` is isolated, the
finite-battery audit is named, and `P19-AN-AUDIT(m)`,
`P19-CHTAIL-AUDIT(eta_ch^*)`, and `P19-CDELTA-AUDIT(c_Delta^*)` are shown to
give `D_dec^*=exp(c_Delta^* eta_*/(1-eta_*))-1`, while the four transport
ceilings are reduced to the component audits
`P19-T11-SRC`, `P19-T12-SRC`, `P19-T13-SRC`, and `P19-T14-SRC`. Section 8F
computes the standard rectangular window geometry:
`Q_\sigma/N_0=\sigma^2/[2RT-\sigma(R+T)]`. It shows that fixed or
sub-macroscopic Creutz decrements collapse `Q_\sigma/N_0` on growing
rectangles, while thick/co-scaling windows such as `R=T=L`,
`\sigma=\alpha L` keep `Q_\sigma/N_0=\alpha^2/[2(1-\alpha)]>0`. Section 8G
therefore declares the thick/co-scaling branch as the main growing-window
direct-witness route and proves its coefficient pass theorem: if
`S_j(-log u_-,j)` is bounded above and `S_j(-log u_+,j)` is bounded below
away from zero on the same tower, then `Theta_j` is bounded and `Phi_j` is
positive. It also proves that, under comparable coefficient exponents, the
thick branch still fails unless the coefficient exponents live at the
reciprocal-area scale. Section 8H then reduces that reciprocal-area source
gate to explicit clean and error budgets:
`\mathcal A_j=S_jt_jC_2(rho_j)/2`,
`\mathcal E_j^-=S_j[-log(1-eta_j)]`, and
`\mathcal E_j^+=S_j log(1+zeta_j)`. It proves that
`liminf \mathcal A_j>E^+` with bounded `\mathcal A_j` and bounded error widths
implies the thick coefficient gate, and that `t_j=beta_j/S_j` is the clean
route. Section 8I compares this clean route with the Paper-16 heat-kernel
asymptotically-free trajectory and proves the compatibility criterion:
`S_j` must be comparable to `g_i^{-2}`. For square thick windows this means
`L_j` grows like `g_i^{-1}`, equivalently like `sqrt(log(1/a_i))` up to
the Paper-16 two-loop logarithmic correction. Section 8J reduces the
remaining coefficient-error estimate to the concrete target
`r_j=delta_j exp(a_j)=O(g_i^2)` with a small enough constant, and Section
8J.7 resolves that constant as the sharp limsup
`R_H^{opt}=limsup_j g_i^{-2}delta_j exp(a_j)`. The exact Section-8J pass
condition is `R_H^{opt}<R_H^{crit}`, with the source sufficient condition
`2 beta_0 K_CE K_L<R_H^{crit}`. Section 8J.8 then improves the attack by
replacing the chain-index route with the AF-normalized source target
`limsup delta_j/g_i^2<=K_AF`, decomposing `delta_j` into heat-kernel,
projection, chart, counterterm, volume, and tail defects, and optimizing the
threshold through `chi`, `s_-/s_+`, and `C_2(rho)`. Section 8J.9 turns that
optimization into an explicit selector: tighten `S_j/H_j` to
`[s(1-epsilon_A),s(1+epsilon_A)]`, pass to a tail with
`t_i/g_i^2 in [1-chi,1+chi]`, and choose `rho` only from the admissible class
where tail, decoration, battery, and first-excess ledgers remain controlled.
Section 8J.10 freezes the first selector candidate `SEL_0`: the fundamental
or paired-fundamental controlled channel, square windows
`L_j=floor(sqrt(sH_j))`, thick Creutz decrement `sigma_j=floor(alpha L_j)`,
and the six-source coefficient ledger
`K_0^src=K_HK^(0)+K_proj^(0)+K_chart^(0)+K_ct^(0)+K_vol^(0)+K_tail^(0)`.
Section 8J.11 now puts the decomposition first:
`K_HK^(0)` is bounded by
`K_time^(0)+K_block^(0)+K_cross^(0)+K_extract^(0)`. Only after that split
does the paper choose a branch. The fixed-time route passes under an
AF-normalized character-domain estimate and fails if the fixed-time defect is
larger than order `g_i^2`. The matched-time route can erase only the
time/scheme debit, and only when the matched time remains inside the same AF
scheme ledger; the block, cross, and extraction residuals still have to fit
under `R_0^crit`. Section 8J.12 then attacks the four decomposed constants:
`K_time` is bounded by the local time drift, `K_cross` is proved from a
Paper-16 residual exponential envelope plus a logarithmic collar schedule,
`K_extract` is zero on the exact coefficient-readout route, and `K_block`
is reduced to a local same-block coefficient normalization gate. It also
separates the non-time residual upper budget `K_NT^up` from the lower
falsification floor `K_NT^low`. Section 8J.13 attacks that local
same-block gate: after absorbing the heat-kernel time tangent into
`tau_time`, it proves `B_0=L_0^blk A_0^blk` from a finite local coefficient
Lipschitz constant and an `O(g_i^2)` transverse local residual. Section
8J.14 closes the Lipschitz part: for the finite one-block exponential-tilt
record law, `L_0^blk<=2C_sup,0`, and in a sup-dominating exact character
basis one may take `L_0^blk<=2`.
Section 8J.15 attacks the large-field part of the transverse residual:
local `HK-LF-REP`, collar-adapted bad-block finite energy with positive
margin, and `t_i<=T_+g_i^2` imply `A_lf,0=0` in the `SEL_0`
normalization. Sections 8J.15G--8J.15M then close the actual local
large-field source row for the strict axial-tree finite-battery `SEL_0`
template: same-metric heat constants are imported, `COL-EXT_0` is
constructed by a bounded axial-tree right inverse and BCH/Bianchi control,
the CAD parameters `e_col,alpha,a_ad` are chosen explicitly, the local
`HK-LF-REP-SRC` ledger is finite, and the size-one bad-collar coverage uses
the same record event. Hence `LF-IMP_0` is proved and `A_lf,0=0`.
Section 8J.16 attacks the remaining transverse pieces and proves the full
local conditional closure:
`LF-IMP_0 + SF-TRANS_0 + CT-TRANS_0 + SCH-TRANS_0` bounds the same-block
residual by `A_sf,0^src+A_ct,0^src+A_sch,0^src`, and the `SEL_0` row passes
when the resulting scalar budget plus `C_0^res+X_0` is below `R_0^crit`.
Section 8J.17 then attacks `SF-TRANS_0` itself: it proves that a finite
`SEL_0` vertex ledger through order `g_i^2`, together with neutral
odd-vertex cancellation and time-tangent absorption, implies
`SF-TRANS_0`; it also proves the falsifier that any surviving transverse
term of order `g_i^q` with `q<2` makes `SF-TRANS_0` false. Section 8J.18
then writes the one-block ledger explicitly and computes
`A_sf,0^src=sum_{a in I_sf^(2)}C_sf,a`, with the vertices
`4,33,J2,gf2,cov2,rec2,norm2`. Section 8J.19 evaluates that row
symbolically: in connected normalization, axial-tree gauge, and minimal
coefficient readout, `gf2=rec2=norm2=0`, the covariance term is
`<=M_cov,0 K_cov,0^blk`, and the pass/fail test is the single margin
`M_loc,0^eval>0` against `R_0^crit`. Section 8J.20 freezes the strongest
minimal row: exact coefficient readout, exact block-conditioned covariance,
connected normalization, axial-tree chart, and `ell^1` normalized-character
basis. This gives `X_0=K_cov,0^blk=0`, `C_sup,0=1`, finite coefficient
formulas for `M_4,0`, `M_33,0`, and `M_J,0`, and the sharper margin
`M_loc,0^min>0`. It also verifies the Paper-16 `HK-SF-YM2` clauses on the
same pushed-forward `SEL_0` record law: the odd/cubic order-`g_i` terms
vanish transversely, the order-`g_i^2` time tangent is absorbed into the
heat-kernel coordinate, the surviving labels are exactly the seven
second-order labels, and all constants are computed by the same finite
projection maps. Section 8J.21 attacks the counterterm debit: pure-gauge
relevant/marginal counterterms are time-tangent or normalization-fixed,
irrelevant local remainders contribute at most
`M_ct,0 C_ct(1+3C_cov^2)C_obs,0` when the Paper-11 exponent is `p=1`, and
contribute zero when `p>1` or when the coefficient-only minimal battery has
no transverse diagnostics. Any surviving relevant/marginal transverse
counterterm below order `g_i^2` is an explicit falsifier. Section 8J.22 then
attacks the scheme debit: after the heat-kernel time coordinate is separated,
the remaining finite local scheme chart contributes
`(1/2)H_sch,0^min(K_sch,0^min)^2`; in the time-only minimal branch or the
coefficient-only branch this debit is zero. A surviving transverse linear
scheme motion below order `g_i^2` is an explicit falsifier.
Section 8J.23 then attacks the remaining cross-residual constant. From the
Paper-19 analytic import it defines
`C_res^env = limsup K_res^* exp(-Delta_res^* d_av)/g_i^2`; if this is below
`R_0^crit`, or equivalently if a logarithmic collar schedule with target
`theta_res R_0^crit` fits inside the available window geometry, the minimal
local row closes. If the best envelope constant is at least `R_0^crit`, the
current residual-tail proof does not close the row; an actual lower floor at
that level falsifies it. Section 8J.24 proves the positive import and
geometry pass: `P19-AN-IMPORT(m)` exports
`Delta_res^*>0` and finite `K_res^*`, while the centered square
fractional `SEL_0` placement has `d_av~L_j~g_i^{-1}`, which beats the
required logarithmic collar. Hence, conditional on `P19-AN-IMPORT(m)`, the
minimal local residual constant is `C_0^res=0`.
Section 8K assembles the
final AF-matched direct-witness closure:
`Sig_AFM>L_AFM => c_15^{tail}>0`, and lists the exact falsification clauses.
Section 8L proves/falsifies the loss budget as far as the current source
papers allow: the exact pass condition is `L_AFM^sharp<Sig_AFM`, the
sufficient gate fails when `L_AFM^sharp>=Sig_AFM`, and an actual
direct-witness falsification needs a lower loss floor above an upper signal
ceiling. Papers 15--16 give formulas and conditional ledgers for these
quantities, but not the sharp cofinal constants.

The final honest status is therefore:

```text
Paper 19 is complete as a conditional source-constant decision paper.
It does not yet prove unconditional actual 4D SU(N) confinement.
It proves the exact AF-matched direct-witness route and the exact ways that
route can fail.
```

The present Papers 14--16 still do not supply the two decisive actual source
estimates unconditionally:

```text
relative character error:
  R_H^opt
    = limsup_j g_i^{-2} delta_j exp(a_j)
    < R_H^crit;

loss budget:
  L_AFM^sharp
    = limsup_j (Delta_dec,j^bd + T_loss,j^bd)
    < Sig_AFM.
```

Section 8J.6 proves that the relative-character-error estimate follows from
the Paper-14 polynomial coefficient-error rate if the standard chain is
calibrated so that `log(1/(a_i Lambda))=O(n_i^{1+p_CE})`. Without that
calibration, the current rate class does not prove the estimate, but it also
does not falsify it. Section 8J.7 sharpens the small-constant condition to

```text
R_H^opt < R_H^crit,
R_H^opt <= 2 beta_0 K_CE K_L
```

on the Paper-14/Paper-16 source route. The current source papers do not yet
prove the strict product bound `2 beta_0 K_CE K_L<R_H^crit`, and they do not
provide lower bounds falsifying it. Section 8J.8 gives the sharper route:

```text
K_HK+K_proj+K_chart+K_ct+K_vol+K_tail < R_H^crit,
```

where each `K_*` is the limsup of the corresponding coefficient-defect piece
divided by `g_i^2`. This is now the preferred next attack because it compares
the actual record-law errors directly in AF units. Section 8J.9 packages the
optimized selector test as

```text
K_AF^src(rho)
<
[(1-chi)(1-epsilon_A)/(1+epsilon_A)] C_2(rho)/2,
rho in R_adm(epsilon_A,chi).
```

The current source papers do not yet supply those six constants, and they do
not prove that any admissible `rho` satisfies this strict selector inequality.
Section 8J.10 freezes the first test row:

```text
SEL_0:
  rho_0 = fundamental or paired fundamental controlled record;
  L_j = floor(sqrt(s H_j));
  sigma_j = floor(alpha L_j);
  K_0^src < [(1-chi)(1-epsilon_A)/(1+epsilon_A)] C_2(rho_0)/2.
```

The current source papers do not yet prove this first-row inequality. The
next concrete coefficient attack is `K_HK^(0)`, the heat-kernel reference
defect for the frozen `SEL_0` row. Section 8J.11 first decomposes that defect:

```text
K_HK^(0)
<= K_time^(0)+K_block^(0)+K_cross^(0)+K_extract^(0).
```

It then proves the exact prove/falsify alternatives for that row:

```text
decomposition-first ledger => K_HK^(0) is bounded by the four debits above;
AF-RGCE_0(K_HK)           => K_HK^(0) <= K_HK;
TV distance <= K_TV g_i^2 => K_HK^(0) <= K_TV;
fixed-time defect/g_i^2 diverges
                           => K_HK^(0) fails;
matched admissible time    => K_time^(0) can be removed, residual debits remain.
```

The current source papers do not yet prove the fixed-time estimate
`|u_0^act-exp(-t_i C_0/2)|=O(g_i^2)`, and they do not falsify it. They also
do not yet prove that
`K_NT^up=B_0+C_0^res+X_0<R_0^crit`, which is the residual upper budget
needed before matched-time can help. Section 8J.12 proves the cross term
conditionally from Paper-16 residual decay and makes the exact-readout
branch `X_0=0`; the main remaining local coefficient problem is
`HK-BLOCK-COEFF_0(B_0)`. Section 8J.13 reduces that problem to

```text
B_0 = L_0^blk A_0^blk,
A_0^blk = A_sf,0 + A_ct,0 + A_sch,0 + A_lf,0,
```

with the time tangent removed into `tau_time`. The new decisive local test is

```text
L_0^blk A_0^blk + C_0^res + X_0 < R_0^crit.
```

Section 8J.14 proves

```text
L_0^blk <= 2 C_sup,0,
```

and therefore reduces the decisive local test to

```text
2 C_sup,0 A_0^blk + C_0^res + X_0 < R_0^crit.
```

Section 8J.15 proves the local large-field reduction:

```text
local HK-LF-REP on SEL_0
+ collar-adapted HK-BFE with c_B delta^2>0
+ t_i <= T_+ g_i^2
=> A_lf,0 = 0.
```

Sections 8J.15G--8J.15M now prove the local `SEL_0` inputs for this
reduction: CAD, collar extension, local large-field representation, and
size-one bad-collar support are all closed as finite same-record statements.
Thus the large-field entry contributes zero to the minimal same-block
budget.

So the remaining same-block scalar test is

```text
2 C_sup,0 (A_sf,0 + A_ct,0 + A_sch,0) + C_0^res + X_0 < R_0^crit.
```

Section 8J.16 then proves the full local conditional pass:

```text
LF-IMP_0
+ SF-TRANS_0
+ CT-TRANS_0
+ SCH-TRANS_0
+ 2 C_sup,0(A_sf,0^src+A_ct,0^src+A_sch,0^src)+C_0^res+X_0<R_0^crit
=> SEL_0 same-block/non-time row passes.
```

The large-field clause in this theorem is now supplied by Theorem 8J.15M.1.
The remaining non-large-field source verification is now exact:

```text
1. transverse small-field local vertices all have p>=1;
2. relevant/marginal counterterms have no unabsorbed transverse SEL_0 part;
3. matched-scheme first derivative is time-tangent and its displacement is O(g_i);
4. the resulting scalar budget is below R_0^crit.
```

Section 8J.17 proves/falsifies the first remaining item and Section 8J.18 writes the
finite first-row worksheet:

```text
SF-VERT_0 + SF-ODD_0 + time-tangent absorption
=> SF-TRANS_0,

but

nonzero transverse small-field term of order g_i^q, q<2
=> SF-TRANS_0 is false.
```

Section 8J.18 lists the finite `SEL_0` one-block vertices through order
`g_i^2`:

```text
I_sf^(2) = {4,33,J2,gf2,cov2,rec2,norm2},
A_sf,0^src =
  C_sf,4+C_sf,33+C_sf,J2+C_sf,gf2
 +C_sf,cov2+C_sf,rec2+C_sf,norm2.
```

It also proves the order-`g_i` odd/cubic cancellation after neutral
pushforward and absorbs the order-`g_i^2` time tangent. Thus the structural
`SF-TRANS_0` obstruction is closed at the worksheet level. Section 8J.19
then evaluates the row symbolically:

```text
C_sf,4     <= 24 M_4,0 C_4 C_cov^2,
C_sf,33    <= 18 M_33,0 C_3^2 C_cov^3,
C_sf,J2    <= M_J,0 C_J C_cov,
C_sf,gf2   = 0,
C_sf,cov2  <= M_cov,0 K_cov,0^blk,
C_sf,rec2  = 0,
C_sf,norm2 = 0.
```

The same-block local row now passes exactly when
`M_loc,0^eval>0`. What remains unconditional is numerical/symbolic source
evaluation of the finite operator constants in that margin, not another
structural small-field decomposition.

Section 8J.20 then freezes the minimal row and computes the finite projection
constants in the selected normalized-character basis:

```text
C_sup,0 = 1,
K_cov,0^blk = 0,
M_a,0 = sum_{b in B_0^perp} limsup_j |m_{a,b,j}|,
a in {4,33,J}.
```

Thus

```text
A_sf,0^min =
  24 M_4,0 C_4 C_cov^2
 +18 M_33,0 C_3^2 C_cov^3
 +M_J,0 C_J C_cov.
```

If the same-block coefficient source carries no transverse diagnostic
records, `B_0^perp` is empty and `A_sf,0^min=0`. The minimal same-block row
then passes exactly when `M_loc,0^min>0`.

Section 8J.20 also verifies the Paper-16 `HK-SF-YM2` clauses on the same
pushed-forward `SEL_0` law. The structural import is now:

```text
CRL-SF_0
+ vertices through order g_i^2
+ neutral odd cancellation
+ time-tangent absorption
+ finite SEL_0 projection constants
=> HK-SF-YM2 on SEL_0,
```

with

```text
theta_sf^SEL0 <= e C_v^{YM2,SEL0} C_G C_E g_*^2.
```

Section 8J.21 attacks the counterterm debit. The pure-gauge
relevant/marginal part is tangent or normalization-fixed:

```text
Pi_0^perp R_rel/marg,0^ct = 0.
```

The irrelevant local remainder satisfies

```text
A_ct,0^min <=
  M_ct,0 C_ct(1+3 C_cov^2) C_obs,0,  if p=1,
  0,                                      if p>1.
```

In the coefficient-only minimal row, `B_0^perp` is empty, so
`M_ct,0=0` and `A_ct,0^min=0`. The counterterm gate now has an exact
falsifier: any surviving relevant/marginal transverse counterterm of order
`g_i^q` with `q<2` makes `CT-TRANS_0` false.

Section 8J.22 attacks the scheme debit. After the heat-kernel time
coordinate is separated, the remaining finite local scheme coordinate
`lambda_j` has source constants

```text
K_sch,0^min = limsup_j ||lambda_j||/g_i,
H_sch,0^min = finite transverse Hessian norm.
```

If the first derivative is time-tangent or normalization-fixed, then

```text
A_sch,0^min = (1/2) H_sch,0^min (K_sch,0^min)^2.
```

In the time-only minimal branch, `lambda_j=0`, and in the coefficient-only
branch `B_0^perp` is empty; either way `A_sch,0^min=0`. A surviving
transverse linear scheme derivative with displacement of order `g_i^q`,
`q<2`, falsifies `SCH-TRANS_0`. A quadratic displacement larger than order
`g_i` also falsifies the quadratic route unless its Hessian projection
vanishes.

Thus the fully debited minimal local margin is

```text
M_loc,0^{min,ct,sch}
 = [(1-chi)(1-epsilon_A)/(1+epsilon_A)] C_2(rho_0)/2
   - C_0^res
   - 2(A_sf,0^min + A_ct,0^min + A_sch,0^min).
```

In the coefficient-only, time-only minimal branch this reduces to the single
remaining local inequality

```text
C_0^res
<
[(1-chi)(1-epsilon_A)/(1+epsilon_A)] C_2(rho_0)/2.
```

Section 8J.23 reduces this residual inequality to the Paper-19 analytic
import tail. With

```text
Delta_res^* = Delta_19^an > 0,
K_res^* = K_19^an,
C_res^env = limsup_j K_res^* exp(-Delta_res^* d_j^av)/g_i^2,
```

the maximal available collar proves

```text
HK-CROSS-COEFF_0(C_res^env).
```

For any target `theta_res<1`, the residual tail closes the minimal local row
if the targeted collar

```text
r_j^target =
ceil( (Delta_res^*)^{-1}
      [2 log(1/g_i)
       + log(K_res^*/(theta_res R_0^crit))] )
```

fits cofinally inside the available window geometry:

```text
r_res <= r_j^target <= d_j^av.
```

Equivalently, the growth-rate route is

```text
d_j^av - (2/Delta_res^*) log(1/g_i) -> +infty,
```

which makes `C_res^env=0`. If `C_res^env>=R_0^crit`, the current Paper-16
tail envelope is too weak for this row; if an actual lower residual floor is
also at least `R_0^crit`, the row is falsified.

Section 8J.24 closes the two named residual-tail inputs on the intended
branch. `P19-AN-IMPORT(m)` exports

```text
Delta_res^* = Delta_19^an > 0,
K_res^* = K_19^an < infinity,
eta_res^* = eta_19^{res} < 1.
```

For the centered square fractional `SEL_0` placement, the available collar
satisfies

```text
d_j^av >= c_av L_j - b_av,
0<c_av<(1-alpha)/2.
```

Since `L_j=floor(sqrt(s)g_i^{-1})`, while
`r_j^target=(2/Delta_res^*)log(1/g_i)+O(1)`, the targeted collar fits
cofinally for every `theta_res<1`. Thus

```text
P19-AN-IMPORT(m) + centered SEL_0
=> C_res^env = 0
=> C_0^res = 0 < R_0^crit
```

on the coefficient-only, time-only minimal local row. Theorem 8J.24E then
assembles the dependency-ordered clean branch:

```text
coefficient-only MIN-SEL_0
+ HK-SF-YM2 on the same SEL_0 record law
+ Theorem 8J.15M.1 local large-field import
+ pure-gauge counterterm ledger
+ time-only scheme branch
+ P19-AN-IMPORT(m)
+ centered square SEL_0 geometry
=> A_sf,0^min=A_lf,0=A_ct,0^min=A_sch,0^min=X_0=C_0^res=0
=> M_loc,0^clean=R_0^crit>0.
```

The analytic import burden is closed for the clean `SEL_0` branch:
Theorem 0A.6 proves `P19-AN-AUDIT(m)`, and Corollary 0A.7 proves
`P19-AN-IMPORT(m)`. Thus Paper 19 imports the named Paper-16 analytic
certificate and does not reconstruct the KP worksheet.

Section 8L proves that the loss budget
follows from explicit source constants
`eta_19^{res}`, `eta_ch^*`, `c_Delta^*`, and
`T_11^*,T_12^*,T_13^*,T_14^*` satisfying

```text
exp(c_Delta^* eta_*/(1-eta_*)) - 1
+ T_11^*+T_12^*+T_13^*+T_14^*
< Sig_AFM,
eta_* = eta_19^{res} + eta_ch^* < 1.
```

After Theorem 0A.6 and Corollary 0A.7, the residual part is supplied by
Paper 16. The character-tail audit is closed by Theorem 8L.8A: choose any
`eta_ch^*<1-eta_19^{res}` and use the cofinal heat-kernel cutoff schedule
there. In particular Corollary 8L.8B gives the canonical half-margin choice.
The finite-battery decoration-growth audit is closed on the centered square
branch by Lemma 8L.9A.1, Theorem 8L.9B, and Corollary 8L.9C.1:

```text
P19-CDELTA-AUDIT(C_xi^SEL0+C_xip^SEL0).
```

Thus the decoration debit is now closed on the intended centered square
`SEL_0` branch. The four transport ceilings have now been decomposed into
component audits in Section 8L.11:

```text
T_11^*: local-RG/RP/covariance/gauge reconstruction,
T_12^*: perimeter/cusp/smearing/loop approximation,
T_13^*: surface-polymer/exact-entry transport,
T_14^*: Paper-14 whole-process finite-block transport.
```

Theorems 8L.11B--8L.11D prove that finite same-record source packages for
these components imply `P19-DW-TLOSS(T_*)`. Section 8L.11A.1--8L.11A.4 now
also closes the common-record transport audit and the Paper-14 component:

```text
P19-TOWER
+ HK-WP-CLOSE
+ same-battery Paper-14 export
=> P19-TR-COMMON,

P19-TR-COMMON + P19-P14-EXPORT(E_14^*)
=> P19-T14-SRC(E_14^*)
=> P19-T14-AUDIT(E_14^*).
```

The reduced same-record source ledgers for the remaining three components
are now explicit:

```text
P19-T11-LEDGER
=> P19-T11-SRC
=> limsup T_11,j <= A_11^loc+A_11^RP+A_11^Cov+A_11^gauge,

P19-T12-LEDGER
=> P19-T12-SRC
=> limsup T_12,j <= A_12^per+A_12^cusp+A_12^smear+A_12^app,

P19-T13-LEDGER
=> P19-T13-SRC
=> limsup T_13,j <= A_13^surf+A_13^entry+A_13^exact.
```

Thus the final scalar comparison is completely exposed:

```text
D_dec^* + T_*^src < Sig_AFM,

D_dec^* = exp(c_Delta^* eta_*/(1-eta_*)) - 1,
eta_* = eta_19^res + eta_ch^*,

T_*^src =
 A_11^loc+A_11^RP+A_11^Cov+A_11^gauge
+A_12^per+A_12^cusp+A_12^smear+A_12^app
+A_13^surf+A_13^entry+A_13^exact
+E_14^*.
```

If this strict inequality is proved, Paper 19 closes the AF-matched
direct-witness loss budget and proves `c_15^tail>0`. If the inequality is not
proved, the current theorem is undecided, not falsified; falsification still
requires an actual upper signal ceiling and lower loss floor as in Theorem
8L.11A.11. The current source papers do not yet supply numerical/sharp enough
values for these transport ledgers, and they also do not supply a lower loss
floor proving failure.

The final worksheet is now frozen in Definition 8L.11A.12. The whole `T_11`
bucket is now reduced to explicit Paper-11/Paper-16 source attacks. The first
slot, Definition 8L.11A.13 and Theorem 8L.11A.14, reduces `A_11^loc` to the
weighted Paper-11 AF residual tail

```text
limsup_j sum_{k>=j} L_j^rec 2 e^alpha G_k Q_k^* exp(-mu R_k)
```

plus the weighted precision tail. Corollary 8L.11A.15 shows the
local-RG/precision debit is zero if those weighted tails vanish.

The remaining `T_11` slots are now also attacked:

```text
P19-T11-RP(A_11^RP),
P19-T11-COV(A_11^Cov),
P19-T11-GAUGE(A_11^gauge).
```

`P19-T11-RP` imports Paper 16 `HK-RP-LEDGER` and the RP half of
`HK-RPCOV-CLOSE`; `P19-T11-COV` imports `HK-COV-LEDGER` and the covariance
half of `HK-RPCOV-CLOSE`; `P19-T11-GAUGE` imports the scalar gauge/chart part
of `HK-REG-CLOSE`. Theorem 8L.11A.15D proves that these attacks, together
with the local branch, close the reduced `P19-T11-LEDGER`. This pays the
projective, regulator/chart, block/collar, finite-volume, and gauge-chart
defects that the reduced `T_12` and `T_13` ledgers explicitly exclude. It is
still a source-constant reduction: the actual cofinal limsups must be
bounded sharply enough for the final scalar worksheet.

The `T_12` loop-readout bucket is now split into three source attacks:

```text
P19-T12-PC(A_12^per,A_12^cusp),
P19-T12-SMEAR(A_12^smear),
P19-T12-APP(A_12^app).
```

These attacks use Paper 12's perimeter/cusp decomposition, local subtraction
and smearing-removal theorem, and loop-modulus/readout package, transported
through Paper 16 `HK-LC-TRANSPORT`. Theorem 8L.11A.20 proves that these three
attacks close the reduced `P19-T12-LEDGER`. Definition 8L.11A.21A and
Theorems 8L.11A.21B--8L.11A.21E now evaluate the four constants exactly as
reduced `HK-LC-TRANSPORT` limsups:

```text
A_12^per   = limsup_j sum_{k>=j} eta_perLC,j,k,
A_12^cusp  = limsup_j sum_{k>=j} eta_cuspLC,j,k,
A_12^smear = limsup_j sum_{k>=j} eta_smearLC,j,k,
A_12^app   = limsup_j sum_{k>=j}
             (eta_P12,j,k+eta_appLC,j,k^(12)+eta_binLC,j,k^(12)).
```

Thus `T_12` is no longer merely named: it is symbolically evaluated on the
common scalar record tower. What remains open is sharper source work proving
that these limsups are finite, vanish, or are small enough for the final
scalar inequality. The projective, regulator, and finite-volume
loop-continuity losses are deliberately excluded from `T_12`; they remain
charged to the `T_11`/`T_14` transport ledgers.

The `T_13` dynamical bucket is now decomposed into the actual nonperturbative
chain:

```text
P19-T13-SUB(q_13^*)
-> P19-T13 surface-tail bound
-> P19-T13-ENTRY(A_13^entry)
-> P19-T13-EXACT(A_13^exact)
-> P19-T13-LEDGER.
```

The first gate is the cofinal Paper-13 subcriticality inequality
`B_C u_{rho,s0}<1`. Definition 8L.11A.22A now evaluates this gate by the
single scalar

```text
q_13^act = limsup_j max_C D_C,j E_C,j^surf u_{rho,s0,j}.
```

Theorem 8L.11A.22B proves the exact decision:

```text
q_13^act < 1  <=>  P19-T13-SUB(q_13^*) for some q_13^*<1.
```

Theorem 8L.11A.22C gives the equivalent logarithmic margin criterion, and
Corollary 8L.11A.22D imports the Paper-16 `HK-SURF-CLOSE` reserve when it is
verified on the same scalar record tower. Definitions 8L.11A.22E--22G then
attack the three actual source factors in the natural order:

```text
P19-T13-ESURF(h_13^*)  : finite-degree surface entropy,
P19-T13-DEC(d_13^*)    : nonminimal-sheet decoration growth,
P19-T13-LEAD(kappa_13^*): leading central character coefficient.
```

Corollary 8L.11A.22E.0.1 closes the first of these on the reduced
four-dimensional hypercubic block-surface template:

```text
h_13^* = 3+log 20
```

with orientation-doubled fallback `3+log 40`. This is a finite geometry
constant, not a dynamical Yang-Mills estimate.

Theorem 8L.11A.22F.2 then closes the second component from the same-record
decoration audits:

```text
d_13^* = C_xi eta_*/(1-eta_*),
eta_* = eta_19^res + eta_ch^*.
```

On the centered square `SEL_0` branch, Corollary 8L.11A.22F.3 gives

```text
d_13^SEL0 = C_xi^SEL0 (1+eta_19^res)/(1-eta_19^res).
```

This uses only the area-charged collar multiplicity `C_xi`; the endpoint and
corner term `C_xip` remains solely in `Delta_dec` and is not charged again in
`D_C`.

Definitions 8L.11A.22G.1A--22G.6 now freeze the coefficient target and
reduce the third component to a same-record Haar-projection coefficient
window:

```text
k_rho,j = <K_p,j,chi_rho>/<chi_rho,chi_rho>,
0 < k_rho,j <= exp(-kappa_13^*) < 1.
```

The sharp decision values are

```text
kappa_13^CE = liminf_j -log k_rho,j,
epsilon_13^CE = limsup_j sum_{lambda != 0,rho} d_lambda |k_lambda,j|.
```

If `kappa_13^CE>0` and `epsilon_13^CE<infinity`, then every strict
`0<kappa_13^*<kappa_13^CE` and `epsilon_ch>epsilon_13^CE` closes
`P19-T13-CEWIN`, hence closes `P19-T13-LEAD(kappa_13^*)` and Paper 13
`CE(s_0,rho,L)` on the same finite battery. Definition 8L.11A.22G.4C and
Theorem 8L.11A.22G.4F now execute the full six-step attack:

```text
identify K_p,j
-> test 0<k_rho,j<1
-> test kappa_13^CE>0
-> test epsilon_13^CE<infinity
-> audit same-record debits
-> apply the exact CEWIN decision.
```

The outcome is precise. The target identification, no-double-charge debit
audit, and exact decision theorem are closed. The finite heat-kernel source
rows also prove the central `L^1` density and Peter-Weyl coefficient
regularity of `K_p,j` via `P19-T13-KPREG`. The leading sign now has a
proved same-target reference-defect route, and the upper bound has the
corresponding reference-gap route; the positive rate has the same-record
reference-rate/log-margin route:

```text
delta_sign,j/u_ref,j < 1 cofinally
=> k_rho,j>0 cofinally.

delta_sign,j/(1-u_ref,j) < 1 cofinally
=> k_rho,j<1 cofinally.

same-target sign + limsup_j (u_ref,j + delta_sign,j) < 1
=> kappa_13^CE>0.

For an AF-matched same-target reference this sufficient rate test is

liminf_j (a_j - log(1+r_j)) > 0.

If instead u_ref,j -> 1 and delta_sign,j -> 0 on the selected same-target
branch, then k_rho,j -> 1 and kappa_13^CE = 0.

P19-CHTAIL-AUDIT(eta_ch^*) on the P19-T13-DEC ledger
=> epsilon_13^CE <= eta_ch^* < infinity.
```

But the actual same-target leading defect estimates are not supplied
unconditionally. The interval and actual-target positive rate are therefore
not proved or falsified by current Papers 13--16. The non-leading tail is
bounded by the same `P19-CHTAIL-AUDIT` used by `P19-T13-DEC`, so it is not a
separate open cutoff problem. The vanishing-reference branch is ruled out as
a positive-rate source only if that branch is the selected same-target
coefficient asymptotic. Current source papers define and transport the
leading gate but do not yet provide an unconditional numerical leading
projection estimate for actual `4D SU(N)`.

Thus, for Paper 20, the coefficient-window burden is not a new character-tail
cutoff. It is the same-record leading estimate:

```text
0<k_rho,j<1 cofinally
and
kappa_13^CE>0.
```

Theorem 8L.11A.22H assembles them into the concrete margin

```text
mu_13^comp = kappa_13^* - d_13^* - h_13^*.
```

If `mu_13^comp>0`, then

```text
q_13^act <= exp(-mu_13^comp) < 1.
```

If `q_13^act>=1`, the surface-polymer route fails at the named
subcriticality gate. If `mu_13^comp<=0` but the exact `q_13^act` is unknown,
the component route is inconclusive rather than failed. If `q_13^act<1`,
Theorem 8L.11A.23 turns it into the explicit
surface-polymer bound

```text
A_13^surf >= M_13^surf q_13^*/(1-q_13^*).
```

Definitions 8L.11A.24 and 8L.11A.25 isolate the exact-entry transport and
cutoff-to-exact scalar comparison. Theorem 8L.11A.26 proves that these
attacks close the reduced `T_13` ledger. This is the closest part of Paper 19
to real confinement content: if subcriticality, actual entry, or exact scalar
comparison cannot be proved on the actual tower, the route remains open or is
falsified at that named gate.

Paper 20 must now do the actual-estimate work on one frozen selector: prove
or falsify `R_H^opt<R_H^crit`, and prove or falsify
`L_AFM^sharp<Sig_AFM` with the component constants already named here.
Until those estimates are supplied, Paper 19 cannot honestly declare an
unconditional proof of actual `4D SU(N)` confinement.
